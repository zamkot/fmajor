# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Retry description_en for the 2 events skipped by the batch passes that actually
have description_ca content (the other 5 flagged as missing have no description_ca
at all — empty in the source site, nothing to translate)."""
import json

TRANSLATIONS = {
    1340: (
        "Mini Literature Festival for ages 0-5, run by the Institut de la Infància.\n"
        "A small festival to enjoy and fall in love with the best books, illustrated "
        "albums and stories for children aged 0 to 5.\n\n"
        "Prior registration at https://museu.santcugat.cat/agenda/\n"
        "Free activity, limited capacity"
    ),
    2032: (
        "Come and enjoy the Festa de l'Esport, with recreational and sports activities "
        "for the whole family. A space full of activities and equipment where adults "
        "and children alike can move, play and discover different sports.\n\n"
        "6 PM Zumba\n"
        "7 PM La gàbia: physical challenges for young people inspired by \"crossfit\" "
        "and other disciplines."
    ),
}

with open("events_schedule.json", encoding="utf-8") as f:
    sched = json.load(f)

updated = 0
for e in sched:
    if e["id"] in TRANSLATIONS:
        e["description_en"] = TRANSLATIONS[e["id"]]
        updated += 1

with open("events_schedule.json", "w", encoding="utf-8") as f:
    json.dump(sched, f, ensure_ascii=False, indent=2)

print(f"Updated description_en for {updated} events")
