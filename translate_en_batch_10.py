# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 10 (final) of the full-catalog English translation pass (events 181-190 of 190)."""
import json

TRANSLATIONS = {
    1441: (
        "With the city's Seguici and the dancers of \"Paga-li, Joan\"\n\n"
        "The time is approximate and will depend on the progress of the Sant Pere "
        "Procession"
    ),
    1442: (
        "Get ready for an afternoon full of color, music and fun! Dance, jump and "
        "enjoy a unique experience for all ages, with entertainment, a DJ, confetti, "
        "giveaways and lots of surprises. Don't miss it and fill Sant Cugat with "
        "color!\n\n"
        "By Holi Colours Festival"
    ),
    1444: (
        "L'Estovallada is back this Festa Major! Lay your picnic blanket on the grass "
        "and have a picnic dinner with Bon Vent!'s concert!\n\n"
        "Bon Vent! is Ebri Knight's family-music project, through which they want to "
        "pass on Xesco Boix's spirit to 21st-century generations. In a world where kids "
        "are so glued to screens and technology, it's worth standing up for what "
        "shouldn't be lost: a happy childhood, connected to music and culture, to "
        "community and to kinship."
    ),
    1443: "The start time of the Mass is approximate and will depend on the Sant Pere Procession",
    1445: (
        "Offering dance with the Ball de Bastons and blessing of the branches\n\n"
        "The time is approximate and will depend on the progress of the Sant Pere "
        "Procession"
    ),
    1446: (
        "Joint showcase of the city's Seguici\n\n"
        "(The time is approximate and will depend on the progress of the Sant Pere "
        "Procession)."
    ),
    1447: (
        "Fan and branch dance at Hort de l'Abat, with Cobla Sant Jordi-Ciutat de "
        "Barcelona\n\n"
        "\"Paga-li, Joan\" is Sant Cugat's most traditional dance. It's always danced "
        "on June 29th, to celebrate Sant Pere, patron saint of Festa Major.\n\n"
        "(The time is approximate and will depend on the progress of the earlier Sant "
        "Pere Procession events)."
    ),
    1448: (
        "L'Estovallada is back this Festa Major! Lay your picnic blanket on the grass "
        "and have a picnic dinner with the Afònic Karaoke Kids show. Afònic Karaoke "
        "Kids is a family event combining music and dance where the audience is the "
        "star. A mix of karaoke, entertainment, choreography and performance that "
        "turns the stage into a space of fun for all ages. Come sing!\n\n"
        "If you don't have a picnic blanket, you can buy one at the park (price: €12)."
    ),
    1449: "Accompanied by Cobla Sant Jordi-Ciutat de Barcelona, the La Lira choir presents its traditional Festa Major concert",
    1450: (
        "Send off five days of Festa Major with the spectacular fireworks display!\n"
        "With Pirotècnia Tomàs, from Benicarló"
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
