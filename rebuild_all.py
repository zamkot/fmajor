# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Run the full non-network pipeline in the correct, fixed order:

    build_schedule.py -> merge_descriptions.py -> apply_auto_categories.py
        -> apply_translations.py -> build_html.py

scrape_events.py is deliberately excluded — it's the slow, network-hitting
step and should only be run manually when the source site has actually
changed. Run it first by hand if needed, then run this script.

build_schedule.py regenerates events_schedule.json from scratch and resets
description_pl/description_en — that's expected, because every step after it
re-applies them from their respective source files."""
import subprocess
import sys

STEPS = [
    "build_schedule.py",
    "merge_descriptions.py",
    "apply_auto_categories.py",
    "apply_translations.py",
    "build_html.py",
]

for step in STEPS:
    print(f"=== {step} ===")
    result = subprocess.run(["uv", "run", step])
    if result.returncode != 0:
        print(f"Aborting: {step} failed (exit code {result.returncode})")
        sys.exit(result.returncode)

print("Rebuild complete.")
