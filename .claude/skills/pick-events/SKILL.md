---
name: pick-events
description: Suggest Festa Major events. Use when the user asks for event recommendations for this festival, wants a share link for specific events, or asks whether a remembered/past event or type of activity (e.g. "is the open-air ball happening this year?") is on this year's schedule.
---

Generate a share link with the suggested events as soon as you present them — don't
wait for confirmation first. The user can ask for tweaks afterward, which just means
regenerating the link with an updated id list.

1. **Suggest**: query `events_schedule.json` (e.g. `jq`) for candidates matching the
   request. Present a short list with title, date/time, location, and why it matches —
   not raw JSON.
2. **Link**: immediately run `scripts/make_share_link.sh [--label <text>] <id> [id ...]`
   with those candidate ids. Pass `--label` with a short (1-3 word) summary of the
   request — not the user's name — e.g. "Balls" for an open-air ball pick, "Food" for
   food stalls. The script prints the finished share URL; the label shows up on the page
   as "👀 Picks: <label>". Give the user both the list and the link in the same reply.
3. **Adjust**: if the user asks to add/remove/swap anything, resolve any user-named
   additions back to ids yourself and re-run the script with the updated id list to
   produce a fresh link.
