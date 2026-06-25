# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal scraper + static-site generator for the "Festa Major de Sant Cugat" festival
schedule (https://fmsantcugat.cat/, a WordPress/Bricks site). It pulls all event posts via
the WP REST API, scrapes date/time/location out of each event's page HTML (those fields
aren't exposed via the API), translates labels to Polish, and renders a single static
`schedule.html` page for browsing.

There is no build system, package.json, or test suite — this is a small one-off data
pipeline of standalone scripts, each runnable independently.

## Running scripts

All scripts are PEP 723 single-file scripts (dependencies declared in a `# /// script` header
at the top of the file) and must be run with `uv run <script>.py`, not plain `python3`.

```bash
uv run scrape_events.py          # network call: re-scrapes all event pages from fmsantcugat.cat
uv run rebuild_all.py            # runs every step below in order, in one go
# ...or step by step:
uv run build_schedule.py         # events_raw.json -> events_schedule.json + schedule.md
uv run merge_descriptions.py     # merges description_ca into events_schedule.json from events_raw.json
uv run apply_auto_categories.py  # overwrites categories_pl from events_categories_auto.json
uv run apply_translations.py     # applies description_pl/description_en from translations_pl.json / translations_en.json
uv run build_html.py             # events_schedule.json -> schedule.html (final output)
```

## Pipeline / data flow

```
scrape_events.py  --(network, slow, ~190 page fetches)-->  events_raw.json
                                                                  |
                                                    build_schedule.py
                                                                  v
                                              events_schedule.json + schedule.md
                                                                  ^
                                                    merge_descriptions.py
                                                    (re-reads events_raw.json,
                                                     adds description_ca field)
                                                                  ^
                                                    apply_auto_categories.py
                                                    (overwrites categories_pl from
                                                     events_categories_auto.json)
                                                                  ^
                                                    apply_translations.py
                                                    (applies description_pl/description_en
                                                     from translations_pl.json /
                                                     translations_en.json)
                                                                  |
                                                    build_html.py
                                                                  v
                                                          schedule.html
```

`rebuild_all.py` runs the five steps from `build_schedule.py` through `build_html.py` in
this exact order via `uv run`, and aborts if any step fails. **Always use it (or follow
this exact order by hand) instead of running individual steps ad hoc** —
`build_schedule.py` regenerates `events_schedule.json` from scratch and resets
`description_pl`/`description_en`, on the assumption that `apply_translations.py` always
re-applies them right after. Running `build_schedule.py` without following through with
the rest of the chain silently wipes every hand translation (this has happened once
already — see git history around the "fix up all translations" commit).

- `events_raw.json` is the only artifact that talks to the network. Don't re-run
  `scrape_events.py` unless the source site changed or data looks stale — it's slow
  (one HTTP request per event, ~190 total) and the site has no JS rendering, so plain
  `requests` is sufficient (no headless browser needed).
- `events_schedule.json` is the canonical processed dataset everything downstream reads.
  Each event has `description_ca` (raw Catalan HTML scraped from the event page),
  `description_pl`, and `description_en` (both `null` until translated for specific
  events).
- Event **titles stay in Catalan** (proper nouns / act names aren't translated).
  Category names, weekday/date strings, and description content ARE translated —
  see `CATEGORY_PL` / `WEEKDAY_PL` / `MONTH_PL` / `WEEKDAY_EN` / `MONTH_EN` in
  `build_schedule.py`. `categories_pl` is later overwritten by `apply_auto_categories.py`
  from `events_categories_auto.json` (LLM-generated; the WP categories were too sparse),
  so `category_slugs` should not be relied on as a stable join key once that step has run.
- `translations_pl.json` and `translations_en.json` are flat `{"<event_id>": "text"}` maps
  and are the single source of truth for hand translations — edit them directly, don't
  write one-off patch scripts, then run `uv run apply_translations.py`.
- Translating all 190 descriptions to Polish up front was deliberately deferred; English
  was eventually done for (almost) all events. Treat `translations_pl.json` as
  Polish-on-demand (mainly starred events) and `translations_en.json` as the fuller pass.

## schedule.html — starring and translation model

`schedule.html` is a static page with no backend. It is a **generated file** — `build_html.py`
contains the actual HTML/CSS/JS template (as an f-string) and writes `schedule.html` from it.
Never hand-edit `schedule.html` directly: those changes look fine locally but get silently
wiped out the next time anyone runs `build_html.py` or `rebuild_all.py`. Always edit the
template in `build_html.py`, then run `uv run build_html.py` to regenerate `schedule.html`
(this has already bitten us once — see git history around the "shared view exit button" work).

A few more things to know before touching it:

- **Starring is client-side only.** Stars are stored in the browser's `localStorage`
  (key `fmajor-starred-v1`), empty on first load — there is no preselected/default set.
  There is no server round-trip — if the user stars new events in the
  browser, those ids only exist in that browser's `localStorage` until the user copies
  them out via the page's "Eksportuj ID ★" button (copies starred ids as JSON to the
  clipboard) and pastes them back into a chat for translation.
- **Untranslated events fall back to the Catalan original** (rendered with `lang="ca"`)
  with a note suggesting Chrome's built-in "Przetłumacz na polski" (right-click translate),
  since there's no API wired up for on-demand machine translation.
- When asked to translate newly starred events: take the ids, look up `description_ca`
  for each in `events_schedule.json`, hand-translate to Polish, add the entries to
  `translations_pl.json` keyed by event id, then run
  `uv run apply_translations.py && uv run build_html.py`.

## Git workflow

- Only fast-forward merges onto `main` — no merge commits. When integrating a worktree
  branch, rebase/cherry-pick it onto `main`'s tip first if needed, then fast-forward.

## Validating changes to schedule.html

This repo has a project-scoped Playwright MCP server (`.mcp.json`, `npx @playwright/mcp`)
for driving a real (isolated, non-system) Chromium browser — it does not touch your
installed Chrome, its profile, or settings. It runs headed by default so you can watch it.

The MCP browser blocks the `file:` protocol, so `schedule.html` can't be opened directly
by path — serve it over HTTP first, started as a tracked background task (not a bare `&`)
so it can be stopped cleanly afterwards instead of left running:

```bash
python3 -m http.server 8743   # from the repo root, run with run_in_background
```

then navigate the MCP browser to `http://localhost:8743/schedule.html`. When validation is
done, stop that same background task by its task id rather than killing anything by port
number — killing by port risks taking down an unrelated process if 8743 is reused elsewhere.

After editing `schedule.html`, use the Playwright MCP browser tools to actually exercise
the behavior rather than just eyeballing the diff:

- star/unstar an event and reload, to confirm `localStorage` (`fmajor-starred-v1`) persists
- click "Eksportuj ID ★" and check the exported JSON
- open an untranslated event and confirm it falls back to the Catalan original (`lang="ca"`)
  with the "Przetłumacz na polski" suggestion

This is ad-hoc/manual validation, not a maintained test suite — there's no fixed script to
keep in sync, just drive the browser tools each time to check the flows the edit touched.

## Tool conventions

- For one-shot JSON inspection/filtering, prefer `jq`.
- For anything beyond a simple filter (merges, building id->value lookup maps,
  multi-step transforms), write a small standalone Python script instead of a complex
  `jq` pipeline — easier to review, and consistent with the existing scripts.
