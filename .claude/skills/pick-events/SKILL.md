---
name: pick-events
description: Suggest Festa Major events. Use when the user asks for event recommendations for this festival, wants a share link for specific events, or asks whether a remembered/past event or type of activity (e.g. "is the open-air ball happening this year?") is on this year's schedule.
---

Confirm which ones the user actually wants, then generate a share link with exactly those starred. 

Suggest -> confirm -> link. If you are very confident in your suggestions you can provide the link right away.

1. **Suggest**: query `events_schedule.json` (e.g. `jq`) for candidates matching the
   request. Present a short list with title, date/time, location, and why it matches —
   not raw JSON.
2. **Confirm**: ask which of the suggestions to keep. Resolve any user-named additions
   back to ids yourself.
3. **Link**: run `scripts/make_share_link.sh [--label <text>] <id> [id ...]` with the
   confirmed ids. Pass `--label` with a short (1-3 word) summary of the request — not
   the user's name — e.g. "Balls" for an open-air ball pick, "Food" for food stalls. The
   script prints the finished share URL; the label shows up on the page as "👀 Picks: <label>".
