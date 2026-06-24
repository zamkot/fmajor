# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///
"""Scrape all Festa Major Sant Cugat 2026 events into a JSON dataset.

Step 1: pull the full post list (title, url, category) from the WP REST API.
Step 2: fetch each event's page HTML and extract Data/Hora/Ubicació.
Raw text is kept as a fallback whenever the expected pattern doesn't match,
so no event is silently dropped.
"""

import json
import re
import sys
import time

import requests

BASE = "https://fmsantcugat.cat"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; personal-schedule-scraper/1.0)"}
DELAY_SECONDS = 0.4

FIELD_RE = re.compile(
    r"<strong>(Data|Hora|Ubicaci[oó]):</strong>\s*([^<]*)", re.IGNORECASE
)


def fetch_categories() -> dict[int, str]:
    resp = requests.get(
        f"{BASE}/wp-json/wp/v2/categories", params={"per_page": 100}, headers=HEADERS
    )
    resp.raise_for_status()
    return {c["id"]: c["slug"] for c in resp.json()}


def fetch_all_posts() -> list[dict]:
    posts = []
    page = 1
    while True:
        resp = requests.get(
            f"{BASE}/wp-json/wp/v2/posts",
            params={"per_page": 50, "page": page},
            headers=HEADERS,
        )
        if resp.status_code == 400:
            break
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        posts.extend(batch)
        total_pages = int(resp.headers.get("X-WP-TotalPages", "1"))
        if page >= total_pages:
            break
        page += 1
    return posts


def parse_event_page(html: str) -> dict:
    fields = {"date_raw": None, "time_raw": None, "location_raw": None}
    key_map = {
        "data": "date_raw",
        "hora": "time_raw",
        "ubicacio": "location_raw",
        "ubicació": "location_raw",
    }
    for label, value in FIELD_RE.findall(html):
        key = key_map.get(label.lower())
        if key:
            fields[key] = value.strip()
    return fields


def main():
    print("Fetching categories...", file=sys.stderr)
    categories = fetch_categories()

    print("Fetching post list...", file=sys.stderr)
    posts = fetch_all_posts()
    print(f"Found {len(posts)} posts.", file=sys.stderr)

    events = []
    for i, post in enumerate(posts, 1):
        url = post["link"]
        title = post["title"]["rendered"]
        category_ids = post.get("categories", [])
        category_slugs = [categories.get(cid, "unknown") for cid in category_ids]

        print(f"[{i}/{len(posts)}] {title}", file=sys.stderr)
        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)
            resp.raise_for_status()
            parsed = parse_event_page(resp.text)
            fetch_error = None
        except requests.RequestException as exc:
            parsed = {"date_raw": None, "time_raw": None, "location_raw": None}
            fetch_error = str(exc)

        events.append(
            {
                "id": post["id"],
                "title": title,
                "url": url,
                "category_slugs": category_slugs,
                "content_html": post["content"]["rendered"],
                "date_raw": parsed["date_raw"],
                "time_raw": parsed["time_raw"],
                "location_raw": parsed["location_raw"],
                "fetch_error": fetch_error,
            }
        )
        time.sleep(DELAY_SECONDS)

    out_path = "events_raw.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(events)} events to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
