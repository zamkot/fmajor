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

# Keyed by the Polish label actually stored in categories_pl (the canonical field —
# it's overwritten post-hoc by apply_auto_categories.py independent of category_slugs,
# so category_slugs can't be trusted as a stable join key/translation lookup anymore).
CATEGORY_INFO = {
    "Muzyka": {"slug": "musica", "en": "Music", "color": "#a33"},
    "Tradycje ludowe": {"slug": "populars", "en": "Folk traditions", "color": "#3a6"},
    "Teatr/Taniec": {"slug": "teatre-dansa", "en": "Theatre/Dance", "color": "#838"},
    "Gastronomia": {"slug": "gastronomiques", "en": "Food & drink", "color": "#a73"},
    "Dla dzieci": {"slug": "infantils", "en": "For kids", "color": "#c80"},
    "Sport": {"slug": "esportives", "en": "Sport", "color": "#36a"},
    "Inne": {"slug": "altres", "en": "Other", "color": "#888"},
}
FALLBACK_CATEGORY_INFO = {"slug": "altres", "en": "Other", "color": "#666"}

all_category_labels = sorted({c for e in events for c in e["categories_pl"]})
CATEGORY_TRANSLATIONS = {
    CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["slug"]: {"pl": c, "en": CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["en"]}
    for c in all_category_labels
}

DESC_NOTE_PL = (
    '<p class="desc-note">Brak tłumaczenia — oryginał po katalońsku '
    "(kliknij prawym przyciskiem myszy i wybierz „Przetłumacz na polski”, "
    'jeśli używasz Chrome):</p>'
)
DESC_NOTE_EN = (
    '<p class="desc-note">No translation yet — Catalan original below '
    "(right-click and use your browser's translate option):</p>"
)
DESC_EMPTY_PL = 'Brak opisu dla tego wydarzenia.'
DESC_EMPTY_EN = 'No description for this event.'


def render_description_lang(desc_ca, desc_text, note_html, empty_text, original_label):
    original_col = (
        f'<div class="desc-original">'
        f'<p class="desc-original-label">{original_label}</p>{desc_ca}</div>'
        if desc_ca
        else ""
    )

    if desc_text:
        text_html = "".join(f"<p>{escape(p)}</p>" for p in desc_text.split("\n\n"))
        left_col = f'<div class="desc-pl">{text_html}</div>'
        if original_col:
            return f'<div class="desc-cols">{left_col}{original_col}</div>'
        return left_col

    if desc_ca:
        note = f'<div class="desc-pl">{note_html}</div>'
        return f'<div class="desc-cols">{note}{original_col}</div>'

    return f'<p class="desc-note placeholder">{empty_text}</p>'


def render_description(e):
    desc_ca = e.get("description_ca")
    pl_block = render_description_lang(
        desc_ca, e.get("description_pl"), DESC_NOTE_PL, DESC_EMPTY_PL, "Oryginał (katalońsku)"
    )
    en_block = render_description_lang(
        desc_ca, e.get("description_en"), DESC_NOTE_EN, DESC_EMPTY_EN, "Original (Catalan)"
    )
    return (
        f'<div class="desc-lang" data-lang="pl">{pl_block}</div>'
        f'<div class="desc-lang" data-lang="en">{en_block}</div>'
    )


def event_row(e):
    cat_slugs = [CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["slug"] for c in e["categories_pl"]]
    cat_attr = escape(" ".join(cat_slugs))
    badges = "".join(
        f'<span class="badge" data-i18n-cat="{CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["slug"]}" '
        f'style="--c:{CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["color"]}">{escape(c)}</span>'
        for c in e["categories_pl"]
    )
    detail_html = render_description(e)
    search_attr = escape(f"{e['title']} {e['location']}")
    return f"""
    <tr class="event" data-id="{e['id']}" data-cats="{cat_attr}" data-search="{search_attr}" tabindex="0">
      <td class="star-cell"><button class="star-btn" data-id="{e['id']}" aria-label="Oznacz gwiazdką" title="Oznacz gwiazdką" data-i18n-aria="starLabel" data-i18n-title="starLabel">☆</button></td>
      <td class="want-cell"><button class="want-btn" data-id="{e['id']}" aria-label="Chcę pójść" title="Chcę pójść" data-i18n-aria="wantLabel" data-i18n-title="wantLabel">♡</button></td>
      <td class="hide-cell"><button class="hide-btn" data-id="{e['id']}" aria-label="Skryj" title="Skryj to wydarzenie" data-i18n-aria="hideAria" data-i18n-title="hideTitle">⊘</button></td>
      <td class="owner-cell owner-star-cell" data-id="{e['id']}"></td>
      <td class="owner-cell owner-want-cell" data-id="{e['id']}"></td>
      <td class="owner-cell owner-hide-cell" data-id="{e['id']}"></td>
      <td class="time">{escape(e['time_pl'])}</td>
      <td class="title">
        <a href="{escape(e['url'])}" target="_blank" rel="noopener">{escape(e['title'])}</a>
        {badges}
      </td>
      <td class="loc">{escape(e['location'])}<span class="expand-cue" aria-hidden="true">&#9662;</span></td>
    </tr>
    <tr class="detail-row"><td colspan="9"><div class="detail">{detail_html}</div></td></tr>
    """


events_sorted = sorted(events, key=lambda e: (e["sort_key"][0], e["sort_key"][1]))

day_sections = []
for day, day_events in groupby(events_sorted, key=lambda e: e["date_pl"]):
    day_events = list(day_events)
    day_en = day_events[0]["date_en"]
    rows = "\n".join(event_row(e) for e in day_events)
    day_sections.append(f"""
    <section class="day">
      <h2>
        <span class="day-date" data-lang="pl">{escape(day)}</span>
        <span class="day-date" data-lang="en">{escape(day_en)}</span>
      </h2>
      <table>
        <thead>
          <tr>
            <th class="star-cell" title="Oznacz gwiazdką" data-i18n-title="starLabel">☆</th>
            <th class="want-cell" title="Chcę pójść" data-i18n-title="wantLabel">♡</th>
            <th class="hide-cell" title="Skryj to wydarzenie" data-i18n-title="hideTitle">⊘</th>
            <th class="owner-group-header" colspan="3"></th>
            <th class="time"></th>
            <th class="title" data-i18n="colEvent">Wydarzenie</th>
            <th class="loc" data-i18n="colLocation">Miejsce</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    </section>
    """)

filter_buttons = "".join(
    f'<button class="filter-btn" data-cat="{CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["slug"]}" '
    f'data-i18n-cat="{CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["slug"]}" '
    f'style="--c:{CATEGORY_INFO.get(c, FALLBACK_CATEGORY_INFO)["color"]}">{escape(c)}</button>'
    for c in all_category_labels
)
special_filter_buttons = (
    '<button class="filter-btn special" data-cat="__starred__" style="--c:#b8860b" data-i18n="filterStarred">★ Twoje wybrane</button>'
    '<button class="filter-btn special" data-cat="__wantgo__" style="--c:#2a6ea3" data-i18n="filterWantgo">♥ Chcę pójść</button>'
    '<button class="filter-btn special" data-cat="__hidden__" style="--c:#a33" data-i18n="filterHidden">⊘ Skryte</button>'
)

footer_html_pl = (
    f'{len(events)} wydarzeń · źródło: <a href="https://fmsantcugat.cat/">fmsantcugat.cat</a> · '
    'kliknij wydarzenie, aby rozwinąć opis · kliknij ☆, aby oznaczyć gwiazdką (zapisywane lokalnie w przeglądarce)'
)
footer_html_en = (
    f'{len(events)} events · source: <a href="https://fmsantcugat.cat/">fmsantcugat.cat</a> · '
    'click an event to expand its description · click ☆ to star it (saved locally in your browser)'
)

TRANSLATIONS = {
    "subtitle": {"pl": "25–29 czerwca 2026 · program wydarzeń", "en": "25–29 June 2026 · event schedule"},
    "searchPlaceholder": {"pl": "Szukaj…", "en": "Search…"},
    "filterAll": {"pl": "Wszystkie", "en": "All"},
    "filterStarred": {"pl": "★ Twoje wybrane", "en": "★ Your picks"},
    "filterWantgo": {"pl": "♥ Chcę pójść", "en": "♥ Want to go"},
    "filterHidden": {"pl": "⊘ Skryte", "en": "⊘ Hidden"},
    "groupPersonal": {"pl": "Twoje listy:", "en": "My lists:"},
    "groupCategory": {"pl": "Kategoria:", "en": "Category:"},
    "expandAll": {"pl": "Rozwiń wszystko", "en": "Expand all"},
    "expandAllTitle": {"pl": "Rozwiń opisy wszystkich wydarzeń", "en": "Expand all event descriptions"},
    "collapseAll": {"pl": "Zwiń wszystko", "en": "Collapse all"},
    "collapseAllTitle": {"pl": "Zwiń opisy wszystkich wydarzeń", "en": "Collapse all event descriptions"},
    "generateLink": {"pl": "Generuj link", "en": "Generate link"},
    "generateLinkTitle": {"pl": "Wygeneruj link z Twoimi wyborami do wysłania", "en": "Generate a shareable link with your picks"},
    "namePrompt": {"pl": "Twoje imię:", "en": "Your name:"},
    "anonymousName": {"pl": "Anonim", "en": "Friend"},
    "syncDevicePrefix": {"pl": "Dodaj wybory: ", "en": "Add picks: "},
    "syncDeviceTitlePrefix": {"pl": "Jednorazowo doda wybory ", "en": "One-time merge of "},
    "syncDeviceTitleSuffix": {
        "pl": " do Twoich własnych na tym urządzeniu (nie da się łatwo odwrócić)",
        "en": "'s picks into your own on this device (not easily reversible)",
    },
    "shareHeaderPrefix": {"pl": "Lista: ", "en": "List: "},
    "shareNote": {"pl": " — fioletowe kolumny pokazują wybory: ", "en": " — purple columns show "},
    "shareNoteSuffix": {"pl": "", "en": "'s picks"},
    "shareHeaderHint": {
        "pl": ". Możesz klikać ★ i ♥, aby ułożyć własną listę podczas przeglądania, albo dodać wszystkie wybory {name} do swojej listy.",
        "en": ". You can click ★ and ♥ to curate your own list while browsing, or add all of {name}'s picks to your list.",
    },
    "exitShare": {"pl": "Wyjdź z udostępnionego widoku", "en": "Exit shared view"},
    "exitShareTitle": {
        "pl": "Wróć do własnego widoku i usuń dane udostępnionej listy z adresu URL",
        "en": "Return to your own view and remove the shared list from the URL",
    },
    "groupShare": {"pl": "Udostępnianie:", "en": "Sharing:"},
    "ownerFilterPrefix": {"pl": "👀 Wybory: ", "en": "👀 Picks: "},
    "colEvent": {"pl": "Wydarzenie", "en": "Event"},
    "colLocation": {"pl": "Miejsce", "en": "Location"},
    "starLabel": {"pl": "Oznacz gwiazdką", "en": "Star this event"},
    "wantLabel": {"pl": "Chcę pójść", "en": "Want to go"},
    "hideAria": {"pl": "Skryj", "en": "Hide"},
    "hideTitle": {"pl": "Skryj to wydarzenie", "en": "Hide this event"},
    "footer": {"pl": footer_html_pl, "en": footer_html_en},
    "copied": {"pl": "Skopiowano!", "en": "Copied!"},
}

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
    --owner-color: #a335d9;
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
  .share-header {{
    color: var(--owner-color);
    font-style: italic;
    font-size: 0.92rem;
    margin: 0.4rem 0 0;
  }}
  .filters {{
    margin-top: 1.2rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    align-items: center;
  }}
  .filter-group {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    align-items: center;
    margin-top: 0.5rem;
  }}
  .filter-group-label {{
    font-size: 0.72rem;
    color: var(--ink-light);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-right: 0.1rem;
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
  .filter-btn.active {{ opacity: 1; background: color-mix(in srgb, var(--c) 22%, transparent); border-width: 2px; }}
  .filter-btn:hover {{ opacity: 0.85; }}
  .filter-btn.special {{
    font-weight: bold;
    background: color-mix(in srgb, var(--c) 10%, transparent);
    border-radius: 1rem;
  }}
  .filter-btn.special.active {{ background: color-mix(in srgb, var(--c) 28%, transparent); }}
  .lang-toggle {{
    margin-top: 0.8rem;
    display: flex;
    gap: 0.3rem;
  }}
  .lang-btn {{
    font-family: var(--serif);
    font-size: 0.72rem;
    border: 1px solid var(--ink-light);
    color: var(--ink-light);
    background: transparent;
    border-radius: 2px;
    padding: 0.15rem 0.5rem;
    cursor: pointer;
    opacity: 0.55;
  }}
  .lang-btn.active {{ opacity: 1; background: #eee; color: var(--ink); }}
  .lang-btn:hover {{ opacity: 0.85; }}
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
  .toolbar {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    align-items: center;
  }}
  #list-toolbar {{ margin-bottom: 2rem; }}
  .export-btn {{
    font-family: var(--serif);
    font-size: 0.75rem;
    color: var(--ink-light);
    background: #f3f1ec;
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
  thead th {{
    font-family: var(--serif);
    font-weight: normal;
    font-size: 0.68rem;
    color: var(--ink-light);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    text-align: left;
    border-bottom: 1px solid var(--rule);
    padding: 0.2rem 0.3rem 0.4rem;
    position: sticky;
    top: 0;
    background: var(--bg);
    cursor: default;
  }}
  thead th.star-cell, thead th.want-cell, thead th.hide-cell, thead th.owner-group-header {{ text-align: center; }}
  thead th.loc {{ text-align: right; }}
  thead th.owner-group-header {{
    display: none;
    color: var(--owner-color);
    font-weight: bold;
  }}
  body.share-mode thead th.owner-group-header {{ display: table-cell; }}
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
  td.owner-cell {{
    width: 1.6rem;
    text-align: center;
    color: var(--owner-color);
    font-size: 1.05rem;
    display: none;
  }}
  body.share-mode td.owner-cell {{ display: table-cell; }}
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
  .expand-cue {{
    display: inline-block;
    margin-left: 0.45rem;
    color: var(--ink-light);
    transition: transform 0.2s ease;
    transform: rotate(-90deg);
  }}
  tr.event.open .expand-cue {{ transform: rotate(0deg); }}
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
  .desc-lang {{ display: none; }}
  html[lang="pl"] .desc-lang[data-lang="pl"] {{ display: block; }}
  html[lang="en"] .desc-lang[data-lang="en"] {{ display: block; }}
  .day-date {{ display: none; }}
  html[lang="pl"] .day-date[data-lang="pl"] {{ display: inline; }}
  html[lang="en"] .day-date[data-lang="en"] {{ display: inline; }}
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
  <p class="subtitle" data-i18n="subtitle">25–29 czerwca 2026 · program wydarzeń</p>
  <p class="share-header" id="share-header" style="display:none"></p>
  <div class="lang-toggle" role="group" aria-label="Language / Język">
    <button class="lang-btn" data-lang="pl">PL</button>
    <button class="lang-btn" data-lang="en">EN</button>
  </div>
  <div class="filters" id="filters">
    <input type="search" id="search-input" class="search-input" placeholder="Szukaj…" aria-label="Szukaj wydarzeń" data-i18n-placeholder="searchPlaceholder" data-i18n-aria="searchPlaceholder">
    <button class="filter-btn active" data-cat="all" style="--c:#1a1a1a" data-i18n="filterAll">Wszystkie</button>
  </div>
  <div class="filter-group" id="personal-filters">
    <span class="filter-group-label" data-i18n="groupPersonal">Twoje listy:</span>
    {special_filter_buttons}
  </div>
  <div class="filter-group" id="category-filters">
    <span class="filter-group-label" data-i18n="groupCategory">Kategoria:</span>
    {filter_buttons}
  </div>
  <div class="filter-group" id="share-toolbar">
    <span class="filter-group-label" data-i18n="groupShare">Udostępnianie:</span>
    <button class="export-btn" id="generate-link-btn" title="Wygeneruj link z Twoimi wyborami do wysłania" data-i18n="generateLink" data-i18n-title="generateLinkTitle">Generuj link</button>
  </div>
</header>

<div class="toolbar" id="list-toolbar">
  <button class="export-btn" id="expand-all-btn" title="Rozwiń opisy wszystkich wydarzeń" data-i18n="expandAll" data-i18n-title="expandAllTitle">Rozwiń wszystko</button>
  <button class="export-btn" id="collapse-all-btn" title="Zwiń opisy wszystkich wydarzeń" data-i18n="collapseAll" data-i18n-title="collapseAllTitle">Zwiń wszystko</button>
</div>

{''.join(day_sections)}

<footer data-i18n-html="footer">
  {footer_html_pl}
</footer>

<script>
const STORAGE_KEY = 'fmajor-starred-v1';
const WANT_STORAGE_KEY = 'fmajor-wantgo-v1';
const HIDDEN_STORAGE_KEY = 'fmajor-hidden-v1';
const LANG_STORAGE_KEY = 'fmajor-lang-v1';
const TRANSLATIONS = {json.dumps(TRANSLATIONS, ensure_ascii=False)};
const CATEGORY_TRANSLATIONS = {json.dumps(CATEGORY_TRANSLATIONS, ensure_ascii=False)};

const BASE62_CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

function bigIntToBase62(n) {{
  if (n === 0n) return '0';
  let s = '';
  while (n > 0n) {{
    s = BASE62_CHARS[Number(n % 62n)] + s;
    n = n / 62n;
  }}
  return s;
}}
function base62ToBigInt(s) {{
  let n = 0n;
  for (const ch of s) {{
    n = n * 62n + BigInt(BASE62_CHARS.indexOf(ch));
  }}
  return n;
}}
function idsToBits(ids) {{
  let bits = ids.length.toString(2).padStart(8, '0');
  for (const id of ids) {{ bits += id.toString(2).padStart(12, '0'); }}
  return bits;
}}
function encodeSharePayload(starredIds, wantIds, hiddenIds) {{
  const bits = '1' + idsToBits(starredIds) + idsToBits(wantIds) + idsToBits(hiddenIds);
  return bigIntToBase62(BigInt('0b' + bits));
}}
function decodeSharePayload(str) {{
  let bits = base62ToBigInt(str).toString(2).slice(1);
  let pos = 0;
  function readIds() {{
    const count = parseInt(bits.slice(pos, pos + 8), 2); pos += 8;
    const ids = [];
    for (let i = 0; i < count; i++) {{
      ids.push(parseInt(bits.slice(pos, pos + 12), 2));
      pos += 12;
    }}
    return ids;
  }}
  const starredIds = readIds();
  const wantIds = readIds();
  const hiddenIds = readIds();
  return {{ starredIds, wantIds, hiddenIds }};
}}
function getShareDataFromUrl() {{
  const params = new URLSearchParams(location.search);
  const payload = params.get('share');
  if (!payload) return null;
  try {{
    const decoded = decodeSharePayload(payload);
    return {{
      name: params.get('by') || null,
      starred: new Set(decoded.starredIds),
      want: new Set(decoded.wantIds),
      hidden: new Set(decoded.hiddenIds),
    }};
  }} catch (e) {{
    return null;
  }}
}}

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

let currentLang = 'pl';

function getInitialLang() {{
  const urlLang = new URLSearchParams(location.search).get('lang');
  if (urlLang === 'pl' || urlLang === 'en') {{
    localStorage.setItem(LANG_STORAGE_KEY, urlLang);
    return urlLang;
  }}
  const saved = localStorage.getItem(LANG_STORAGE_KEY);
  if (saved === 'pl' || saved === 'en') {{ return saved; }}
  return navigator.language.startsWith('en') ? 'en' : 'pl';
}}

function setLanguage(lang) {{
  currentLang = lang;
  document.documentElement.lang = lang;
  document.querySelectorAll('[data-i18n]').forEach(el => {{
    el.textContent = TRANSLATIONS[el.dataset.i18n][lang];
  }});
  document.querySelectorAll('[data-i18n-html]').forEach(el => {{
    el.innerHTML = TRANSLATIONS[el.dataset.i18nHtml][lang];
  }});
  document.querySelectorAll('[data-i18n-title]').forEach(el => {{
    el.title = TRANSLATIONS[el.dataset.i18nTitle][lang];
  }});
  document.querySelectorAll('[data-i18n-aria]').forEach(el => {{
    el.setAttribute('aria-label', TRANSLATIONS[el.dataset.i18nAria][lang]);
  }});
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {{
    el.placeholder = TRANSLATIONS[el.dataset.i18nPlaceholder][lang];
  }});
  document.querySelectorAll('[data-i18n-cat]').forEach(el => {{
    el.textContent = CATEGORY_TRANSLATIONS[el.dataset.i18nCat][lang];
  }});
  document.querySelectorAll('.lang-btn').forEach(btn => {{
    btn.classList.toggle('active', btn.dataset.lang === lang);
  }});
  localStorage.setItem(LANG_STORAGE_KEY, lang);
  refreshShareUI();
}}

function refreshShareUI() {{
  if (!shareData) return;
  const header = document.getElementById('share-header');
  if (header) {{
    header.textContent = TRANSLATIONS.shareHeaderPrefix[currentLang] + shareData.name
      + TRANSLATIONS.shareNote[currentLang] + shareData.name + TRANSLATIONS.shareNoteSuffix[currentLang]
      + TRANSLATIONS.shareHeaderHint[currentLang].replace('{{name}}', shareData.name);
  }}
  const ownerFilterBtn = document.getElementById('owner-filter-btn');
  if (ownerFilterBtn) {{
    ownerFilterBtn.textContent = TRANSLATIONS.ownerFilterPrefix[currentLang] + shareData.name;
  }}
  document.querySelectorAll('.owner-group-header').forEach(th => {{
    th.textContent = shareData.name;
  }});
  const syncBtn = document.getElementById('sync-btn');
  if (syncBtn) {{
    syncBtn.textContent = TRANSLATIONS.syncDevicePrefix[currentLang] + shareData.name;
    syncBtn.title = TRANSLATIONS.syncDeviceTitlePrefix[currentLang] + shareData.name
      + TRANSLATIONS.syncDeviceTitleSuffix[currentLang];
  }}
  const exitBtn = document.getElementById('exit-share-btn');
  if (exitBtn) {{
    exitBtn.textContent = TRANSLATIONS.exitShare[currentLang];
    exitBtn.title = TRANSLATIONS.exitShareTitle[currentLang];
  }}
}}

let shareData = getShareDataFromUrl();
if (shareData && !shareData.name) {{
  shareData.name = navigator.language.startsWith('en') ? 'Friend' : 'Anonim';
}}

document.querySelectorAll('.lang-btn').forEach(btn => {{
  btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
}});
setLanguage(getInitialLang());

let starred = loadSet(STORAGE_KEY, []);
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
    if (shareData) {{
      row.querySelector('.owner-star-cell').textContent = shareData.starred.has(id) ? '★' : '';
      row.querySelector('.owner-want-cell').textContent = shareData.want.has(id) ? '♥' : '';
      row.querySelector('.owner-hide-cell').textContent = shareData.hidden.has(id) ? '⊘' : '';
    }}
  }});
}}
applyStarredState();

function initShareMode() {{
  if (!shareData) return;
  document.body.classList.add('share-mode');
  document.getElementById('share-header').style.display = '';

  const ownerFilterBtn = document.createElement('button');
  ownerFilterBtn.className = 'filter-btn special';
  ownerFilterBtn.id = 'owner-filter-btn';
  ownerFilterBtn.dataset.cat = '__ownertouched__';
  ownerFilterBtn.style.setProperty('--c', '#a335d9');
  document.getElementById('personal-filters').appendChild(ownerFilterBtn);

  const syncBtn = document.createElement('button');
  syncBtn.className = 'export-btn';
  syncBtn.id = 'sync-btn';
  syncBtn.textContent = TRANSLATIONS.syncDevicePrefix[currentLang] + shareData.name;
  syncBtn.title = TRANSLATIONS.syncDeviceTitlePrefix[currentLang] + shareData.name
    + TRANSLATIONS.syncDeviceTitleSuffix[currentLang];
  syncBtn.addEventListener('click', () => {{
    shareData.starred.forEach(id => starred.add(id));
    shareData.want.forEach(id => wantToGo.add(id));
    shareData.hidden.forEach(id => hidden.add(id));
    saveSet(STORAGE_KEY, starred);
    saveSet(WANT_STORAGE_KEY, wantToGo);
    saveSet(HIDDEN_STORAGE_KEY, hidden);
    applyStarredState();
    applyFilter();
    const original = syncBtn.textContent;
    syncBtn.textContent = TRANSLATIONS.copied[currentLang];
    setTimeout(() => {{
      syncBtn.textContent = TRANSLATIONS.syncDevicePrefix[currentLang] + shareData.name;
    }}, 1500);
  }});
  document.getElementById('share-toolbar').appendChild(syncBtn);

  const exitBtn = document.createElement('button');
  exitBtn.className = 'export-btn';
  exitBtn.id = 'exit-share-btn';
  exitBtn.textContent = TRANSLATIONS.exitShare[currentLang];
  exitBtn.title = TRANSLATIONS.exitShareTitle[currentLang];
  exitBtn.addEventListener('click', () => {{
    location.href = location.pathname;
  }});
  document.getElementById('share-toolbar').appendChild(exitBtn);

  refreshShareUI();
}}
initShareMode();

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
  if (cat === '__ownertouched__') {{
    if (!shareData) return false;
    const id = Number(row.dataset.id);
    return shareData.starred.has(id) || shareData.want.has(id) || shareData.hidden.has(id);
  }}
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
if (shareData) {{ activeCats.add('__ownertouched__'); }}
applyFilter();

document.getElementById('generate-link-btn').addEventListener('click', () => {{
  let name = window.prompt(TRANSLATIONS.namePrompt[currentLang], '');
  if (name === null) return;
  name = name.trim() || TRANSLATIONS.anonymousName[currentLang];
  const payload = encodeSharePayload([...starred], [...wantToGo], [...hidden]);
  const url = new URL(location.origin + location.pathname);
  url.searchParams.set('share', payload);
  url.searchParams.set('by', name);
  navigator.clipboard.writeText(url.toString()).then(() => {{
    const btn = document.getElementById('generate-link-btn');
    const original = btn.textContent;
    btn.textContent = TRANSLATIONS.copied[currentLang];
    setTimeout(() => {{ btn.textContent = original; }}, 1500);
  }});
}});
</script>
</body>
</html>
"""

with open("schedule.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Wrote schedule.html ({len(events)} events, {len(all_category_labels)} categories)")
