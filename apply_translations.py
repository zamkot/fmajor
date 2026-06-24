# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Apply hand-translated descriptions from translations_pl.json and
translations_en.json into events_schedule.json, keyed by event id.

These two JSON files are the single source of truth for description_pl /
description_en — edit them directly (don't write one-off patch scripts) when
translating newly-starred events, then re-run this script."""
import json

with open("translations_pl.json", encoding="utf-8") as f:
    pl = json.load(f)
with open("translations_en.json", encoding="utf-8") as f:
    en = json.load(f)
with open("events_schedule.json", encoding="utf-8") as f:
    sched = json.load(f)

updated_pl = 0
updated_en = 0
for e in sched:
    key = str(e["id"])
    if key in pl:
        e["description_pl"] = pl[key]
        updated_pl += 1
    if key in en:
        e["description_en"] = en[key]
        updated_en += 1

with open("events_schedule.json", "w", encoding="utf-8") as f:
    json.dump(sched, f, ensure_ascii=False, indent=2)

print(f"Updated description_pl for {updated_pl} events, description_en for {updated_en} events")
