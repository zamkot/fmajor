# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Turn events_raw.json into a chronologically sorted, Polish-labeled dataset
plus a human-readable Markdown table.

Event titles are left in Catalan (proper nouns / act names shouldn't be
translated). Category names and weekday names are translated to Polish.
"""

import html
import json
import re

WEEKDAY_PL = {
    "dilluns": "poniedziałek",
    "dimarts": "wtorek",
    "dimecres": "środa",
    "dijous": "czwartek",
    "divendres": "piątek",
    "dissabte": "sobota",
    "diumenge": "niedziela",
}

MONTH_PL = {
    "juny": "czerwca",
}

CATEGORY_PL = {
    "musica": "Muzyka",
    "populars": "Tradycje ludowe",
    "teatre-dansa": "Teatr/Taniec",
    "gastronomiques": "Gastronomia",
    "infantils": "Dla dzieci",
    "esportives": "Sport",
    "altres": "Inne",
    "unknown": "Inne",
}

DATE_RE = re.compile(r"(\w+)\s+(\d{1,2})\s+de\s+(\w+)", re.IGNORECASE)
TIME_RE = re.compile(r"(\d{1,2}):(\d{2})")


def parse_date(date_raw: str | None) -> tuple[int, str]:
    """Returns (day_number_for_sorting, polish_date_label)."""
    if not date_raw:
        return (99, "brak daty")
    m = DATE_RE.search(date_raw)
    if not m:
        return (99, date_raw)
    weekday_ca, day, month_ca = m.groups()
    day = int(day)
    weekday_pl = WEEKDAY_PL.get(weekday_ca.lower(), weekday_ca)
    month_pl = MONTH_PL.get(month_ca.lower(), month_ca)
    return (day, f"{weekday_pl}, {day} {month_pl}")


def parse_time(time_raw: str | None) -> tuple[int, str]:
    """Returns (minutes_since_midnight_for_sorting, label)."""
    if not time_raw:
        return (9999, "brak godziny")
    m = TIME_RE.search(time_raw)
    if not m:
        return (9999, time_raw)
    h, mnt = int(m.group(1)), int(m.group(2))
    return (h * 60 + mnt, f"{h:02d}:{mnt:02d}")


def main():
    with open("events_raw.json", encoding="utf-8") as f:
        raw_events = json.load(f)

    enriched = []
    for e in raw_events:
        day_num, date_pl = parse_date(e["date_raw"])
        minutes, time_pl = parse_time(e["time_raw"])
        categories_pl = [CATEGORY_PL.get(c, c) for c in e["category_slugs"]] or ["Inne"]

        enriched.append(
            {
                "id": e["id"],
                "title": html.unescape(e["title"]),
                "url": e["url"],
                "date_pl": date_pl,
                "time_pl": time_pl,
                "location": html.unescape(e["location_raw"]) if e["location_raw"] else "(brak lokalizacji)",
                "category_slugs": e["category_slugs"],
                "categories_pl": categories_pl,
                "sort_key": [day_num, minutes],
                "description_pl": None,  # filled in later, on request
            }
        )

    enriched.sort(key=lambda e: e["sort_key"])

    with open("events_schedule.json", "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)

    lines = [
        "# Festa Major Sant Cugat 2026 — Harmonogram",
        "",
        "| Data | Godzina | Wydarzenie | Kategoria | Miejsce |",
        "|---|---|---|---|---|",
    ]
    for e in enriched:
        cats = ", ".join(e["categories_pl"])
        title_md = f"[{e['title']}]({e['url']})"
        lines.append(
            f"| {e['date_pl']} | {e['time_pl']} | {title_md} | {cats} | {e['location']} |"
        )

    with open("schedule.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote {len(enriched)} events to events_schedule.json and schedule.md")


if __name__ == "__main__":
    main()
