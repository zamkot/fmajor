# schedule.html — manual test plan

Steps used to validate the mobile event-row redesign (`build_html.py`'s
`@media (max-width: 700px)` block). Captured here so an automated Playwright
suite can be built from it later — each case below is written as
setup → action → assertion so it maps directly onto a `test()` block.

## Setup

```bash
uv run build_html.py        # regenerate schedule.html from current template
python3 -m http.server 8743 # serve repo root (MCP browser blocks file://)
```

Base URL: `http://localhost:8743/schedule.html`

Two viewports matter for every case below:
- **Mobile**: 390×844 (iPhone-12-ish) — triggers the `max-width: 700px` rules.
- **Desktop**: 900×700 — must keep rendering the original `<table>` layout.

## Case 1 — Mobile row layout reflows into a stacked card

- **Setup**: load the page at the mobile viewport.
- **Action**: inspect the first event row (`tr.event`).
- **Assert**:
  - `thead` is not visible (`display: none`).
  - Within one row, `td.time` and the three icon cells
    (`td.star-cell`, `td.want-cell`, `td.hide-cell`) render on the same
    line, icons right-aligned (icons cell `offsetLeft` > time cell's).
  - `td.title` renders on its own line below them, full row width.
  - `td.loc` renders on its own line below the title, full row width,
    left-aligned (not right-aligned as on desktop).
  - No horizontal scrollbar / no text overflow clipping on the row.

## Case 2 — Desktop table layout is unaffected

- **Setup**: load the page at the desktop viewport.
- **Action**: inspect the same first event row.
- **Assert**:
  - `thead` is visible with column headers (★/♡/⊘, EVENT, LOCATION).
  - The row is a normal table row: `td.loc` is right-aligned in its own
    column, on the same visual line as `td.time` and `td.title`.

## Case 3 — Expand/collapse description still works in the mobile layout

- **Setup**: mobile viewport, page loaded.
- **Action**: click an event row's title/time/location area (any cell
  except the star/want/hide buttons) to toggle `.open` on the `tr.event`.
- **Assert**:
  - The row gains class `open` and the following `tr.detail-row .detail`
    expands (non-zero rendered height) and shows the description text.
  - Clicking again removes `.open` and the detail collapses.
  - "Expand all" / "Collapse all" buttons toggle `.open` on every
    `tr.event` at once and the visual result matches per-row toggling.

## Case 4 — Star/want/hide state persists across reload (mobile)

- **Setup**: mobile viewport, page loaded, `localStorage` cleared for the
  origin beforehand.
- **Action**:
  1. Click `.star-btn` on the first event row.
  2. Reload the page.
- **Assert**:
  - After step 1: row gains class `starred`, button glyph changes
    `☆` → `★`, and `localStorage['fmajor-starred-v1']` contains the
    event's `data-id`.
  - After reload: the same row still has class `starred` and shows `★`
    (state survives reload, not just in-memory).
  - Repeat the same check for `.want-btn` (`♡`→`♥`,
    `fmajor-wantgo-v1`) and `.hide-btn` (`⊘`→`🚫`, `fmajor-hidden-v1`,
    row gains `is-hidden` and dims).

## Case 5 — Badge and long-title wrapping doesn't break the mobile card

- **Setup**: mobile viewport, page loaded.
- **Action**: find an event with a long title and/or multiple category
  badges (e.g. an event with 2+ `.badge` spans).
- **Assert**:
  - Title text wraps onto multiple lines without being clipped or
    overlapping the icon row above it.
  - Badges wrap onto their own line(s) under the title without
    overlapping the location line below.

## Case 6 — Search and category/personal filters still narrow the list (mobile)

- **Setup**: mobile viewport, page loaded.
- **Action**:
  1. Type a known event-title fragment into `#search-input`.
  2. Clear it, then click a category filter button (e.g. "Music").
  3. Click "★ Your picks" after starring at least one event.
- **Assert**:
  - After step 1: only `tr.event` rows whose `data-search` fuzzy-matches
    the query are visible (others get class `hidden`); empty `.day`
    sections get class `empty`.
  - After step 2: only rows whose `data-cats` includes that category's
    slug are visible.
  - After step 3: only rows with class `starred` are visible.

## Case 7 — Language toggle re-renders text without breaking layout (mobile)

- **Setup**: mobile viewport, page loaded in PL (default).
- **Action**: click the "EN" language button.
- **Assert**:
  - `html[lang]` becomes `en`, all `[data-i18n*]` text switches to
    English, day headings switch to the `data-lang="en"` span.
  - The mobile card layout from Case 1 still holds (no regression caused
    by longer/shorter EN strings).

## Case 8 — Share link generation and share-mode rendering (mobile)

- **Setup**: mobile viewport, at least one event starred.
- **Action**:
  1. Click "Generate link", confirm a name prompt, read the URL written
     to the clipboard.
  2. Open that URL in a fresh context (simulating a different visitor).
- **Assert**:
  - Step 1: clipboard text matches `<origin><pathname>?share=...&by=...`.
  - Step 2: `body` gains class `share-mode`; the share header banner is
    visible and names the sharer; rows the sharer starred/wanted/hid show
    the corresponding owner-column glyph.

## Case 9 — Untranslated event falls back to Catalan original

- **Setup**: mobile or desktop viewport; find an event whose
  `description_en`/`description_pl` is `null` in `events_schedule.json`.
- **Action**: expand that event's row.
- **Assert**: the detail panel shows the Catalan original (`lang="ca"`)
  plus the "right-click → Translate" note, instead of empty text.

## Notes for automation

- Star/want/hide state lives in `localStorage` under
  `fmajor-starred-v1` / `fmajor-wantgo-v1` / `fmajor-hidden-v1` — seed or
  clear these directly via `page.evaluate` instead of clicking through
  the UI when a test only cares about resulting state.
- The repo's `.mcp.json` Playwright MCP server expects a system Chrome
  binary; in containers without one, drive the bundled Chromium directly
  via the `playwright` Node/Python package with
  `executablePath: '/opt/pw-browsers/chromium'` instead of fighting the
  MCP server's `--browser chrome` default.
