# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Generate a Tufte-style static HTML schedule from events_schedule.json."""
import json
from html import escape
from itertools import groupby

with open("events_schedule.json", encoding="utf-8") as f:
    events = json.load(f)

CATEGORY_COLORS = {
    "Muzyka": "#a33",
    "Popularne": "#3a6",
    "Inne": "#888",
    "Sportowe": "#36a",
    "Dla dzieci": "#c80",
    "Teatr/Taniec": "#838",
    "Gastronomia": "#a73",
}

all_categories = sorted({c for e in events for c in e["categories_pl"]})

def event_row(e):
    cats = e["categories_pl"]
    cat_attr = escape(" ".join(cats))
    badges = "".join(
        f'<span class="badge" style="--c:{CATEGORY_COLORS.get(c, "#666")}">{escape(c)}</span>'
        for c in cats
    )
    desc = e.get("description_pl")
    detail_html = (
        f'<p class="desc">{escape(desc)}</p>'
        if desc
        else '<p class="desc placeholder">Brak opisu — do uzupełnienia na żądanie.</p>'
    )
    return f"""
    <tr class="event" data-cats="{cat_attr}" tabindex="0">
      <td class="time">{escape(e['time_pl'])}</td>
      <td class="title">
        <a href="{escape(e['url'])}" target="_blank" rel="noopener">{escape(e['title'])}</a>
        {badges}
      </td>
      <td class="loc">{escape(e['location'])}</td>
    </tr>
    <tr class="detail-row"><td colspan="3"><div class="detail">{detail_html}</div></td></tr>
    """

events_sorted = sorted(events, key=lambda e: (e["sort_key"][0], e["sort_key"][1]))

day_sections = []
for day, day_events in groupby(events_sorted, key=lambda e: e["date_pl"]):
    day_events = list(day_events)
    rows = "\n".join(event_row(e) for e in day_events)
    day_sections.append(f"""
    <section class="day">
      <h2>{escape(day)}</h2>
      <table>
        <tbody>
          {rows}
        </tbody>
      </table>
    </section>
    """)

filter_buttons = "".join(
    f'<button class="filter-btn" data-cat="{escape(c)}" style="--c:{CATEGORY_COLORS.get(c, "#666")}">{escape(c)}</button>'
    for c in all_categories
)

html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Festa Major de Sant Cugat 2026 — Program</title>
<style>
  :root {{
    --bg: #fdfdfb;
    --ink: #1a1a1a;
    --ink-light: #555;
    --rule: #ddd;
    --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    background: var(--bg);
    color: var(--ink);
    font-family: var(--serif);
    font-size: 19px;
    line-height: 1.5;
    max-width: 780px;
    margin: 0 auto;
    padding: 3rem 1.5rem 6rem;
  }}
  header {{
    margin-bottom: 2.5rem;
    border-bottom: 1px solid var(--rule);
    padding-bottom: 1.5rem;
  }}
  h1 {{
    font-size: 2rem;
    font-weight: normal;
    margin: 0 0 0.3rem;
    letter-spacing: -0.01em;
  }}
  .subtitle {{
    color: var(--ink-light);
    font-style: italic;
    font-size: 1rem;
    margin: 0;
  }}
  .filters {{
    margin-top: 1.2rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }}
  .filter-btn {{
    font-family: var(--serif);
    font-size: 0.78rem;
    border: 1px solid var(--c, #666);
    color: var(--c, #666);
    background: transparent;
    border-radius: 2px;
    padding: 0.2rem 0.6rem;
    cursor: pointer;
    opacity: 0.55;
    transition: opacity 0.15s;
  }}
  .filter-btn.active {{ opacity: 1; background: color-mix(in srgb, var(--c) 12%, transparent); }}
  .filter-btn:hover {{ opacity: 0.85; }}

  .day {{ margin-bottom: 2.8rem; }}
  .day h2 {{
    font-size: 1.05rem;
    font-weight: normal;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--ink-light);
    border-bottom: 1px solid var(--rule);
    padding-bottom: 0.4rem;
    margin-bottom: 0;
  }}
  table {{ width: 100%; border-collapse: collapse; }}
  tr.event {{ cursor: pointer; }}
  tr.event td {{
    padding: 0.55rem 0.3rem;
    border-bottom: 1px solid #eee;
    vertical-align: top;
  }}
  tr.event:hover td {{ background: #f5f3ee; }}
  td.time {{
    font-variant-numeric: tabular-nums;
    color: var(--ink-light);
    width: 4.2rem;
    white-space: nowrap;
    font-size: 0.92rem;
    padding-top: 0.65rem;
  }}
  td.title a {{
    color: var(--ink);
    text-decoration: none;
    border-bottom: 1px dotted #bbb;
  }}
  td.title a:hover {{ border-bottom-color: var(--ink); }}
  td.loc {{
    color: var(--ink-light);
    font-size: 0.88rem;
    text-align: right;
    width: 11rem;
  }}
  .badge {{
    display: inline-block;
    font-size: 0.68rem;
    color: var(--c);
    border: 1px solid var(--c);
    border-radius: 2px;
    padding: 0 0.35rem;
    margin-left: 0.4rem;
    vertical-align: middle;
    opacity: 0.85;
  }}
  tr.detail-row td {{ padding: 0; border-bottom: 1px solid #eee; }}
  .detail {{
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.25s ease, padding 0.25s ease;
  }}
  tr.event.open + tr.detail-row .detail {{
    max-height: 400px;
    padding: 0.2rem 0.3rem 0.9rem 0.3rem;
  }}
  .desc {{
    margin: 0;
    font-size: 0.92rem;
    color: #333;
    max-width: 38em;
  }}
  .desc.placeholder {{ color: #999; font-style: italic; }}
  tr.hidden, tr.hidden + tr.detail-row {{ display: none; }}
  .day.empty {{ display: none; }}
  footer {{
    margin-top: 3rem;
    color: var(--ink-light);
    font-size: 0.8rem;
    border-top: 1px solid var(--rule);
    padding-top: 1rem;
  }}
</style>
</head>
<body>
<header>
  <h1>Festa Major de Sant Cugat</h1>
  <p class="subtitle">25–29 czerwca 2026 · program wydarzeń</p>
  <div class="filters" id="filters">
    <button class="filter-btn active" data-cat="all" style="--c:#1a1a1a">Wszystkie</button>
    {filter_buttons}
  </div>
</header>

{''.join(day_sections)}

<footer>
  190 wydarzeń · źródło: <a href="https://fmsantcugat.cat/">fmsantcugat.cat</a> ·
  kliknij wydarzenie, aby rozwinąć opis (jeśli dostępny)
</footer>

<script>
document.querySelectorAll('tr.event').forEach(row => {{
  row.addEventListener('click', () => row.classList.toggle('open'));
  row.addEventListener('keydown', e => {{
    if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); row.classList.toggle('open'); }}
  }});
}});

const filterBtns = document.querySelectorAll('.filter-btn');
filterBtns.forEach(btn => {{
  btn.addEventListener('click', () => {{
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const cat = btn.dataset.cat;
    document.querySelectorAll('tr.event').forEach(row => {{
      const cats = row.dataset.cats.split(' ');
      const show = cat === 'all' || cats.includes(cat);
      row.classList.toggle('hidden', !show);
    }});
    document.querySelectorAll('.day').forEach(day => {{
      const visible = day.querySelectorAll('tr.event:not(.hidden)').length > 0;
      day.classList.toggle('empty', !visible);
    }});
  }});
}});
</script>
</body>
</html>
"""

with open("schedule.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Wrote schedule.html ({len(events)} events, {len(all_categories)} categories)")
