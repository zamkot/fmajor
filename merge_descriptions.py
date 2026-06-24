# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Merge Catalan content_html descriptions from events_raw.json into events_schedule.json
as a new `description_ca` field, keyed by event id."""
import json

with open("events_raw.json", encoding="utf-8") as f:
    raw = json.load(f)
with open("events_schedule.json", encoding="utf-8") as f:
    sched = json.load(f)

desc_by_id = {e["id"]: e.get("content_html") for e in raw}

missing = 0
for e in sched:
    desc = desc_by_id.get(e["id"])
    e["description_ca"] = desc
    if not desc:
        missing += 1

with open("events_schedule.json", "w", encoding="utf-8") as f:
    json.dump(sched, f, ensure_ascii=False, indent=2)

print(f"Merged description_ca into {len(sched)} events ({missing} missing)")
