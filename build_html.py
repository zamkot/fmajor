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

# Seed value for localStorage on a visitor's first load — the user's initial picks:
# Castellers, Correfoc (x2), Botifarrada (x2), "Paella" (Concurs d'Arrossos).
DEFAULT_STARRED = [1359, 1316, 1385, 1936, 1310, 1395]

# Calmer, visual, no-fire picks suggested for first-time-visiting parents.
PARENT_PICKS = {1359, 1316, 1385}  # castellers + both correfocs, watched from a distance
PARENT_EXTRA = {
    "38a Trobada gegantera: plantada de gegants",
    "38a Trobada gegantera: cercavila de gegants",
    "38a Trobada gegantera: ball conjunt",
    "Ballada de sardanes",
    "XV Trobada de balls i entremesos d’arreu de Catalunya: cercavila",
}
PARENT_IDS = PARENT_PICKS | {e["id"] for e in events if e["title"].strip() in PARENT_EXTRA}


def render_description(e):
    desc_pl = e.get("description_pl")
    desc_ca = e.get("description_ca")

    original_col = (
        f'<div class="desc-original">'
        f'<p class="desc-original-label">Oryginał (katalońsku)</p>{desc_ca}</div>'
        if desc_ca
        else ""
    )

    if desc_pl:
        pl_html = "".join(f"<p>{escape(p)}</p>" for p in desc_pl.split("\n\n"))
        left_col = f'<div class="desc-pl">{pl_html}</div>'
        if original_col:
            return f'<div class="desc-cols">{left_col}{original_col}</div>'
        return left_col

    if desc_ca:
        note = (
            '<p class="desc-note">Brak tłumaczenia — oryginał po katalońsku '
            "(kliknij prawym przyciskiem myszy i wybierz „Przetłumacz na polski”, "
            'jeśli używasz Chrome):</p>'
        )
        return f'<div class="desc-cols"><div class="desc-pl">{note}</div>{original_col}</div>'

    return '<p class="desc-note placeholder">Brak opisu dla tego wydarzenia.</p>'


def event_row(e):
    cats = list(e["categories_pl"])
    is_parent = e["id"] in PARENT_IDS
    if is_parent:
        cats.append("__parents__")
    cat_attr = escape(" ".join(cats))
    badges = "".join(
        f'<span class="badge" style="--c:{CATEGORY_COLORS.get(c, "#666")}">{escape(c)}</span>'
        for c in e["categories_pl"]
    )
    if is_parent:
        badges += '<span class="badge parent" title="Polecane dla rodziców">👪 dla rodziców</span>'
    detail_html = render_description(e)
    search_attr = escape(f"{e['title']} {e['location']}")
    return f"""
    <tr class="event" data-id="{e['id']}" data-cats="{cat_attr}" data-search="{search_attr}" tabindex="0">
      <td class="star-cell"><button class="star-btn" data-id="{e['id']}" aria-label="Oznacz gwiazdką" title="Oznacz gwiazdką">☆</button></td>
      <td class="want-cell"><button class="want-btn" data-id="{e['id']}" aria-label="Chcę pójść" title="Chcę pójść">♡</button></td>
      <td class="hide-cell"><button class="hide-btn" data-id="{e['id']}" aria-label="Skryj" title="Skryj to wydarzenie">⊘</button></td>
      <td class="time">{escape(e['time_pl'])}</td>
      <td class="title">
        <a href="{escape(e['url'])}" target="_blank" rel="noopener">{escape(e['title'])}</a>
        {badges}
      </td>
      <td class="loc">{escape(e['location'])}</td>
    </tr>
    <tr class="detail-row"><td colspan="6"><div class="detail">{detail_html}</div></td></tr>
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
special_filter_buttons = (
    '<button class="filter-btn special" data-cat="__starred__" style="--c:#b8860b">★ Twoje wybrane</button>'
    '<button class="filter-btn special" data-cat="__wantgo__" style="--c:#2a6ea3">♥ Chcę pójść</button>'
    '<button class="filter-btn special" data-cat="__parents__" style="--c:#2a7a6b">👪 Dla rodziców</button>'
    '<button class="filter-btn special" data-cat="__hidden__" style="--c:#a33">⊘ Skryte</button>'
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
    align-items: center;
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
  .filter-btn.special {{ font-weight: bold; }}
  .search-input {{
    font-family: var(--serif);
    font-size: 0.85rem;
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 0.25rem 0.6rem;
    color: var(--ink);
    background: #fff;
    width: 9rem;
  }}
  .search-input:focus {{ outline: none; border-color: var(--ink-light); }}
  .export-btn {{
    margin-left: auto;
    font-family: var(--serif);
    font-size: 0.75rem;
    color: var(--ink-light);
    background: transparent;
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 0.2rem 0.6rem;
    cursor: pointer;
  }}
  .export-btn:hover {{ border-color: var(--ink-light); color: var(--ink); }}

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
  tr.event td {{
    padding: 0.55rem 0.3rem;
    border-bottom: 1px solid #eee;
    vertical-align: top;
  }}
  tr.event:hover td {{ background: #f5f3ee; }}
  tr.event.starred td {{ background: #fdf6e3; }}
  tr.event.starred:hover td {{ background: #fbeec9; }}
  tr.event.starred td.time {{ border-left: 3px solid #b8860b; padding-left: calc(0.3rem - 3px); }}
  tr.event.want-to-go:not(.starred) td {{ background: #eef4fa; }}
  tr.event.want-to-go:not(.starred):hover td {{ background: #e0ecf6; }}
  tr.event.want-to-go:not(.starred) td.time {{ border-left: 3px solid #2a6ea3; padding-left: calc(0.3rem - 3px); }}
  tr.event.is-hidden td {{ opacity: 0.5; }}
  td.star-cell, td.want-cell, td.hide-cell {{
    width: 1.6rem;
    text-align: center;
    cursor: pointer;
  }}
  .star-btn {{
    background: none;
    border: none;
    font-size: 1.05rem;
    line-height: 1;
    cursor: pointer;
    color: #b8860b;
    padding: 0;
  }}
  .want-btn {{
    background: none;
    border: none;
    font-size: 1.05rem;
    line-height: 1;
    cursor: pointer;
    color: #2a6ea3;
    padding: 0;
  }}
  .hide-btn {{
    background: none;
    border: none;
    font-size: 1.05rem;
    line-height: 1;
    cursor: pointer;
    color: #999;
    padding: 0;
  }}
  tr.event.is-hidden .hide-btn {{ color: #a33; }}
  tr.event .title {{ cursor: pointer; }}
  td.time {{
    font-variant-numeric: tabular-nums;
    color: var(--ink-light);
    width: 4.2rem;
    white-space: nowrap;
    font-size: 0.92rem;
    padding-top: 0.65rem;
    cursor: pointer;
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
    cursor: pointer;
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
    transition: max-height 0.3s ease, padding 0.3s ease;
  }}
  tr.event.open + tr.detail-row .detail {{
    max-height: 900px;
    padding: 0.2rem 0.3rem 0.9rem 2rem;
  }}
  .desc-pl p {{
    margin: 0 0 0.6em;
    font-size: 0.92rem;
    color: #333;
    white-space: pre-line;
  }}
  .desc-note {{
    margin: 0 0 0.4em;
    font-size: 0.82rem;
    color: #888;
    font-style: italic;
  }}
  .desc-note.placeholder {{ color: #999; }}
  .desc-cols {{
    display: flex;
    gap: 1.8rem;
    align-items: flex-start;
  }}
  .desc-cols > div {{ flex: 1 1 50%; min-width: 0; }}
  @media (max-width: 700px) {{
    .desc-cols {{ flex-direction: column; gap: 0.6rem; }}
  }}
  .desc-original-label {{
    font-size: 0.78rem;
    color: var(--ink-light);
    margin: 0 0 0.4em;
  }}
  .desc-original {{
    font-size: 0.88rem;
    color: #444;
  }}
  .desc-original p {{ margin: 0.4em 0; }}
  .badge.parent {{ color: #2a7a6b; border-color: #2a7a6b; opacity: 1; }}
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
    <input type="search" id="search-input" class="search-input" placeholder="Szukaj…" aria-label="Szukaj wydarzeń">
    <button class="filter-btn active" data-cat="all" style="--c:#1a1a1a">Wszystkie</button>
    {special_filter_buttons}
    {filter_buttons}
    <button class="export-btn" id="expand-all-btn" title="Rozwiń opisy wszystkich wydarzeń">Rozwiń wszystko</button>
    <button class="export-btn" id="collapse-all-btn" title="Zwiń opisy wszystkich wydarzeń">Zwiń wszystko</button>
    <button class="export-btn" id="export-btn" title="Skopiuj ID oznaczonych gwiazdką wydarzeń do schowka">Eksportuj ID ★</button>
    <button class="export-btn" id="export-want-btn" title="Skopiuj ID wydarzeń „chcę pójść” do schowka">Eksportuj ID ♥</button>
  </div>
</header>

{''.join(day_sections)}

<footer>
  190 wydarzeń · źródło: <a href="https://fmsantcugat.cat/">fmsantcugat.cat</a> ·
  kliknij wydarzenie, aby rozwinąć opis · kliknij ☆, aby oznaczyć gwiazdką (zapisywane lokalnie w przeglądarce)
</footer>

<script>
const STORAGE_KEY = 'fmajor-starred-v1';
const WANT_STORAGE_KEY = 'fmajor-wantgo-v1';
const HIDDEN_STORAGE_KEY = 'fmajor-hidden-v1';
const DEFAULT_STARRED = {json.dumps(DEFAULT_STARRED)};

function loadSet(key, defaults) {{
  const raw = localStorage.getItem(key);
  if (raw === null) {{
    localStorage.setItem(key, JSON.stringify(defaults));
    return new Set(defaults);
  }}
  try {{ return new Set(JSON.parse(raw)); }} catch {{ return new Set(); }}
}}
function saveSet(key, set) {{
  localStorage.setItem(key, JSON.stringify([...set]));
}}

let starred = loadSet(STORAGE_KEY, DEFAULT_STARRED);
let wantToGo = loadSet(WANT_STORAGE_KEY, []);
let hidden = loadSet(HIDDEN_STORAGE_KEY, []);

function applyStarredState() {{
  document.querySelectorAll('tr.event').forEach(row => {{
    const id = Number(row.dataset.id);
    const isStarred = starred.has(id);
    row.classList.toggle('starred', isStarred);
    row.querySelector('.star-btn').textContent = isStarred ? '★' : '☆';
    const isWant = wantToGo.has(id);
    row.classList.toggle('want-to-go', isWant);
    row.querySelector('.want-btn').textContent = isWant ? '♥' : '♡';
    const isHidden = hidden.has(id);
    row.classList.toggle('is-hidden', isHidden);
    row.querySelector('.hide-btn').textContent = isHidden ? '🚫' : '⊘';
  }});
}}
applyStarredState();

document.querySelectorAll('.star-btn').forEach(btn => {{
  btn.addEventListener('click', e => {{
    e.stopPropagation();
    const id = Number(btn.dataset.id);
    if (starred.has(id)) {{ starred.delete(id); }} else {{ starred.add(id); }}
    saveSet(STORAGE_KEY, starred);
    applyStarredState();
    applyFilter();
  }});
}});

document.querySelectorAll('.want-btn').forEach(btn => {{
  btn.addEventListener('click', e => {{
    e.stopPropagation();
    const id = Number(btn.dataset.id);
    if (wantToGo.has(id)) {{ wantToGo.delete(id); }} else {{ wantToGo.add(id); }}
    saveSet(WANT_STORAGE_KEY, wantToGo);
    applyStarredState();
    applyFilter();
  }});
}});

document.querySelectorAll('.hide-btn').forEach(btn => {{
  btn.addEventListener('click', e => {{
    e.stopPropagation();
    const id = Number(btn.dataset.id);
    if (hidden.has(id)) {{ hidden.delete(id); }} else {{ hidden.add(id); }}
    saveSet(HIDDEN_STORAGE_KEY, hidden);
    applyStarredState();
    applyFilter();
  }});
}});

document.querySelectorAll('tr.event').forEach(row => {{
  row.addEventListener('click', () => row.classList.toggle('open'));
  row.addEventListener('keydown', e => {{
    if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); row.classList.toggle('open'); }}
  }});
}});

document.querySelectorAll('td.title a').forEach(a => {{
  a.addEventListener('click', e => e.stopPropagation());
}});

document.getElementById('expand-all-btn').addEventListener('click', () => {{
  document.querySelectorAll('tr.event').forEach(row => row.classList.add('open'));
}});
document.getElementById('collapse-all-btn').addEventListener('click', () => {{
  document.querySelectorAll('tr.event').forEach(row => row.classList.remove('open'));
}});

const filterBtns = document.querySelectorAll('.filter-btn');
const searchInput = document.getElementById('search-input');
const activeCats = new Set();

function rowMatchesCat(row, cat) {{
  if (cat === '__starred__') return row.classList.contains('starred');
  if (cat === '__wantgo__') return row.classList.contains('want-to-go');
  return row.dataset.cats.split(' ').includes(cat);
}}

function normalizeSearch(s) {{
  return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase();
}}

function fuzzyMatch(query, text) {{
  query = normalizeSearch(query);
  text = normalizeSearch(text);
  let qi = 0;
  for (let i = 0; i < text.length && qi < query.length; i++) {{
    if (text[i] === query[qi]) qi++;
  }}
  return qi === query.length;
}}

function applyFilter() {{
  const query = searchInput.value.trim();
  document.querySelectorAll('tr.event').forEach(row => {{
    let show;
    if (activeCats.has('__hidden__')) {{
      show = row.classList.contains('is-hidden');
    }} else {{
      show = activeCats.size === 0 || [...activeCats].some(cat => rowMatchesCat(row, cat));
      if (row.classList.contains('is-hidden')) {{ show = false; }}
    }}
    if (show && query) {{ show = fuzzyMatch(query, row.dataset.search); }}
    row.classList.toggle('hidden', !show);
  }});
  document.querySelectorAll('.day').forEach(day => {{
    const visible = day.querySelectorAll('tr.event:not(.hidden)').length > 0;
    day.classList.toggle('empty', !visible);
  }});
  filterBtns.forEach(btn => {{
    const cat = btn.dataset.cat;
    const active = cat === 'all' ? activeCats.size === 0 : activeCats.has(cat);
    btn.classList.toggle('active', active);
  }});
}}

function toggleFilter(cat) {{
  if (cat === 'all') {{
    activeCats.clear();
  }} else if (cat === '__hidden__') {{
    if (activeCats.size === 1 && activeCats.has('__hidden__')) {{
      activeCats.clear();
    }} else {{
      activeCats.clear();
      activeCats.add('__hidden__');
    }}
  }} else {{
    activeCats.delete('__hidden__');
    if (activeCats.has(cat)) {{ activeCats.delete(cat); }} else {{ activeCats.add(cat); }}
  }}
  applyFilter();
}}

filterBtns.forEach(btn => {{
  btn.addEventListener('click', () => toggleFilter(btn.dataset.cat));
}});
searchInput.addEventListener('input', applyFilter);
applyFilter();

document.getElementById('export-btn').addEventListener('click', () => {{
  const ids = JSON.stringify([...starred]);
  navigator.clipboard.writeText(ids).then(() => {{
    const btn = document.getElementById('export-btn');
    const original = btn.textContent;
    btn.textContent = 'Skopiowano!';
    setTimeout(() => {{ btn.textContent = original; }}, 1500);
  }});
}});

document.getElementById('export-want-btn').addEventListener('click', () => {{
  const ids = JSON.stringify([...wantToGo]);
  navigator.clipboard.writeText(ids).then(() => {{
    const btn = document.getElementById('export-want-btn');
    const original = btn.textContent;
    btn.textContent = 'Skopiowano!';
    setTimeout(() => {{ btn.textContent = original; }}, 1500);
  }});
}});
</script>
</body>
</html>
"""

with open("schedule.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Wrote schedule.html ({len(events)} events, {len(all_categories)} categories)")
