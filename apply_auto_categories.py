# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Overwrite categories_pl in events_schedule.json with LLM-generated categories
from events_categories_auto.json (the official WP categories were too sparse,
e.g. almost no events were tagged "Dla dzieci" despite many being kid-friendly)."""
import json

with open("events_categories_auto.json", encoding="utf-8") as f:
    auto_categories = json.load(f)

with open("events_schedule.json", encoding="utf-8") as f:
    sched = json.load(f)

updated = 0
for e in sched:
    categories = auto_categories.get(str(e["id"]))
    if categories is not None:
        e["categories_pl"] = categories
        updated += 1

with open("events_schedule.json", "w", encoding="utf-8") as f:
    json.dump(sched, f, ensure_ascii=False, indent=2)

print(f"Updated categories_pl for {updated} events")
