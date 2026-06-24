# schedule.html — UX review

Scope: the toolbar/header area and the per-row controls. Verified live with the
Playwright MCP browser against `http://localhost:8743/schedule.html` (PL, EN, a
generated share link in share mode, and a 390px-wide mobile viewport). Every issue
below was reproduced on screen, not just inferred from source.

## 1. Category filters and personal-state controls are visually fused

**What's there today:** `#filters` contains, in this order: search box → "All" →
4 special filters (★ Your picks, ♥ Want to go, 👪 For parents, ⊘ Hidden) → 7 category
filters (Music, Folk, Theatre/Dance, Food, Kids, Sport, Other) → expand/collapse/generate-link
buttons. All of these render as the same pill-shaped `.filter-btn`/`.export-btn`, same row,
same low-contrast outline style (build_html.py:480-488).

**Why it's a problem:** "★ Your picks" and "♥ Want to go" are *personal state filters*
(derived from what you've clicked), while Music/Sport/etc. are *content taxonomy*. They're
unrelated axes — one says "what kind of event is this," the other says "what have I done
with it" — but they're rendered as one undifferentiated button soup with no separator,
heading, or grouping. A first-time user can't tell ★/♥/👪/⊘ apart from Music/Sport without
reading each label carefully.

**Confirmed live:** in the PL screenshot, the toolbar wraps to two rows: row 1 is
`Wszystkie / Twoje wybrane / Chcę pójść / Dla rodziców / Skryte / Dla dzieci / Gastronomia
/ Inne`, row 2 is `Muzyka / Sport / Teatr-Taniec / Tradycje ludowe`. The wrap point falls
*in the middle* of the personal-state group, so on this exact viewport width "Skryte"
(state) and "Dla dzieci" (category) end up adjacent on the same line with zero separation
— the two unrelated axes are not just unioned, they're interleaved.

**Options to consider:**
- Split into two visually distinct rows/groups with a small label or just a gap + rule:
  "My lists:" [★ ♥ 👪 ⊘] and "Category:" [Music Folk Theatre…].
  Likely the lowest-effort fix.
- Give the two groups different shapes (e.g. category = colored outline pill as now,
  personal = filled/icon-only toggle chip) so the eye separates them even without reading.
- Move personal-state filters to live next to the star/want/hide *columns* they filter on,
  reinforcing "these are about you," not "these are about the event."

## 2. Expand all / Collapse all / Generate link float with no anchor

**What's there today:** These three buttons are appended at the very end of `#filters`
(build_html.py:485-487), after 12 filter pills, with no visual separator besides
`.export-btn`'s `margin-left: auto` pulling only the *first* one (`export-btn` class is
shared, but only one rule uses `margin-left: auto` — actually all three get it, see CSS at
build_html.py:301-312, so they all try to push right, fighting for the same flex space).

**Why it's a problem:** They're functionally unrelated to filtering (one is a view-state
toggle, one is a sharing action) but sit in the filter bar with identical button styling,
so they read as "three more filter categories" rather than distinct actions. On narrow
viewports the flex-wrap will drop them onto a new line in an order that depends on
how many category buttons preceded them — their position is effectively non-deterministic
to the user from session to session/viewport to viewport.

**Confirmed live:** switching PL → EN proves this isn't theoretical. In PL, the three
buttons wrap as `[Rozwiń wszystko] [Generuj link]` on one row, then `[Zwiń wszystko]`
alone, centered, on the next. In EN — same viewport, same window — they reflow as
`[Expand all] [Collapse all]` together, with `[Generate link]` dropping to its own row.
Same three buttons, same intent, two completely different visual groupings purely because
the English labels are different pixel widths. In share mode a fourth/fifth button
("Sync to this device", "👀 Picks: Tomasz") join the same flex soup and reflow again.
Nothing here is anchored — it's all just whatever fits per line.

**Options to consider:**
- Move these three into a small dedicated toolbar row, separate from `#filters` —
  e.g. a thin second header row: `[Expand all] [Collapse all]` on the left,
  `[Generate link]` (and "Sync to this device" when present) on the right.
- At minimum, give them a distinct visual treatment (e.g. icon + filled background)
  so they don't look like more filter pills.
- Consider collapsing "Expand all / Collapse all" into a single toggle button that
  flips label+behavior based on current state, reducing two buttons to one.

## 3. "Sync to this device" wording doesn't say what it does

**Current copy:** PL "Synchronizuj z tym urządzeniem" / EN "Sync to this device",
title text "Dodaj wybory z linku do Twoich lokalnych wyborów na tym urządzeniu" /
"Merge this link's picks into your own picks on this device" (build_html.py:187-188).

**Why it's a problem:** "Sync" implies an ongoing, bidirectional, possibly automatic
relationship ("these two things will stay in sync"). What it actually does is a
**one-time, one-way merge**: it unions the link-sender's starred/want/hidden ids into
*your* local storage, once, when clicked. There's no ongoing sync. The accurate mental
model is closer to "import" or "copy in."

**Options to consider (your own framing, "copy Tomasz's picks to mine," is good):**
- Make the button label name-specific when a sender name is known:
  PL "Dodaj wybory Tomasza" / EN "Add Tomasz's picks" — this also reduces reliance on
  the title attribute, which most users never read.
- Generic fallback when no name: "Copy these picks to my device" / "Skopiuj te wybory
  do moich".
- Consider a confirm step or undo, since it's a merge with no easy reversal (you'd
  have to manually unstar everything you imported) — at minimum, the button should
  not look identical to a low-stakes filter toggle (relates to issue #2).

## 4. Owner columns (shared-link view) aren't labeled

**What's there today:** In share mode (`?share=...&by=...`), three extra columns appear
(`owner-star-cell`, `owner-want-cell`, `owner-hide-cell`, build_html.py:118-120) showing
the *sender's* ★/♥/⊘ marks in purple, next to *your own* ★/♥/⊘ columns in
gold/blue/grey. There is no `<thead>` anywhere in the table (event rows go straight into
`<tbody>` with no header row at all), so neither set of columns has a visible label —
the only hint is the share-header paragraph above the table and the (undiscoverable)
`#owner-filter-btn`, whose text is "👀 Picks: {name}" but which only filters, doesn't
label the columns themselves.

**Confirmed live:** generated a real share link (`?share=...&by=Tomasz`) and opened it.
Filtering to "👀 Picks: Tomasz" surfaces rows like "Botifarrada popular" showing
`★ ♡ ⊘ ★` — a filled gold star (mine), an empty heart and circle (mine, unset), then a
filled *purple* star (Tomasz's) sitting directly next to my own gold star with no gap,
divider, or label between "my" group and "his" group. The only thing separating the two
4-icon clusters is a 1px vertical rule with no annotation — easy to misread the second
star as a duplicate or a different action entirely rather than "this is someone else's
mark."

**Why it's a problem:** With 6 icon-only star/want/hide cells (your 3 + their 3) sitting
side by side, color is the *only* signal distinguishing "mine" from "theirs," and color
meaning isn't taught anywhere in the row itself. A user has to infer it from the
share-header sentence and remember it while scanning 190 rows below.

**Options to consider (your framing — name the column explicitly):**
- Add a real `<thead>` row with column labels: blank/★/♥/⊘ for yours, then
  "Tomasz" spanning his 3 columns (or repeat ★/♥/⊘ under his name). A `colspan`
  header naming the sender turns 3 mystery columns into one labeled group.
- Sticky-position that header so it stays visible while scrolling 190 rows.
- Alternative if a header row feels heavy: prefix the sender's icons differently
  (e.g. outline-only vs filled) rather than relying purely on color, for users with
  color-vision deficiency too.

## 5. Day headers (weekday + date) aren't translated in English mode

**What's there today:** `build_schedule.py` only computes `date_pl` (via `WEEKDAY_PL`/
`MONTH_PL` dicts) — there is no `date_en`. `build_html.py` renders day section headers
as `<h2>{escape(day)}</h2>` using that single `date_pl` value unconditionally
(build_html.py:140), with no `data-i18n` hook. So switching the page to EN translates
every button, badge, and footer string, but the 5 day headers ("Czwartek, 25 czerwca,"
etc.) stay in Polish — the one thing you'd expect a "weekday + date" heading to need
translated, since it's pure data, not a label.

**Why it's a problem:** It's the most visible inconsistency in an otherwise fully
bilingual page — every EN user immediately hits 5 Polish headers running down the page.

**Confirmed live:** toggled PL → EN. Every button, badge, and the subtitle translate
correctly ("25–29 czerwca 2026 · program wydarzeń" → "25–29 June 2026 · event schedule"),
but the day heading directly below stays exactly "CZWARTEK, 25 CZERWCA" in both languages.

**Fix:** Add `WEEKDAY_EN`/`MONTH_EN` maps in `build_schedule.py` alongside the PL ones,
compute `date_en` the same way `date_pl` is computed, then in `build_html.py` either
(a) render both `date_pl`/`date_en` as a `data-i18n`-style pair of spans toggled by
`html[lang]` (consistent with how `.desc-lang` already does PL/EN toggling), or
(b) thread it through `TRANSLATIONS` per-day. (a) is more consistent with the existing
pattern in the codebase.

## Additional findings (not in your list, found while reading the code)

- **No table header row at all**, even outside share mode. The star/want/hide icon
  columns (☆ ♡ ⊘) have no header cells — their only identification is `title`/`aria-label`
  on hover/focus, which mouse users skim past and which doesn't exist visually for anyone
  scanning quickly. A header row (even just icon glyphs repeated as column headers) would
  help first-time users understand the three icon columns exist and what they mean,
  before they start clicking.
- **Active filter state is low-contrast.** `.filter-btn.active` only changes opacity
  (0.55 → 1) and adds a faint 12%-tint background (build_html.org:269) — on a fast
  glance, especially with several filters toggled, it can be hard to tell at a glance
  which of 12 similarly-styled pills are currently active.
- **Generate-link / Sync buttons give no indication of *what* will happen before
  clicking** beyond a tooltip. "Generate link" pops a native `window.prompt()` for a
  name with no other context — fine once you know it, opaque the first time.
- **Icon-only buttons (☆ ♡ ⊘ 👪) carry meaning entirely through color + a single glyph**,
  with no text label visible without hovering. Combined with issue #1 (categories also
  use color), the page leans heavily on color to disambiguate several unrelated systems
  (event taxonomy, your-state, their-state, hidden-state) at once. Worth auditing whether
  any single color is reused for two different meanings (e.g. is purple used for owner
  columns *and* anything else?) — currently it isn't, but it's a fragile invariant as more
  features get added.
- **Mobile/narrow viewport (390px, normal mode)**: checked live — the table itself holds
  up fine; rows wrap location text onto extra lines and stay legible. The toolbar wraps to
  ~6 rows of pills, which is a lot of vertical scroll before reaching any events, but
  nothing breaks. Share-mode at this width (6 icon columns) was not separately checked and
  is worth a follow-up screenshot given how cramped it already looked at desktop width.
