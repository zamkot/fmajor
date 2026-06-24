# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_pl for newly-starred picks (manually translated), batch 2."""
import json

TRANSLATIONS = {
    1358: (
        "Z udziałem grup: Geganters de La Llàntia de Mataró, Geganters de Santa Eulàlia "
        "de Ronçana, Gegants de Puigcerdà, Gegants de Sant Jaume de Barcelona, Geganters "
        "de Valldoreix, Gegants de Rubí, Gegants de Falset, Gegant Inquiet de Catalònia "
        "Fundació Creactiva i Geganters de Sant Cugat."
    ),
    2039: (
        "Z udziałem grup: Geganters de La Llàntia de Mataró, Geganters de Santa Eulàlia "
        "de Ronçana, Gegants de Puigcerdà, Gegants de Sant Jaume de Barcelona, Geganters "
        "de Valldoreix, Gegants de Rubí, Gegants de Falset, Gegant Inquiet de Catalònia "
        "Fundació Creactiva i Geganters de Sant Cugat.\n\n"
        "Trasa: av. de Cerdanyola, c. de la Creu, c. Torre, pl. Octavià, c. Santiago "
        "Rusiñol, pl. dels Quatre Cantons, av. Rius i Taulet, c. Enric Granados, pl. de "
        "Sant Pere, c. Major, pl. Octavià.\n\n"
        "Spokojny, dostosowany odcinek: c. Enric Granados."
    ),
    2049: (
        "Z udziałem grup: Geganters de La Llàntia de Mataró, Geganters de Santa Eulàlia "
        "de Ronçana, Gegants de Puigcerdà, Gegants de Sant Jaume de Barcelona, Geganters "
        "de Valldoreix, Gegants de Rubí, Gegants de Falset, Gegant Inquiet de Catalònia "
        "Fundació Creactiva i Geganters de Sant Cugat."
    ),
    1394: (
        "Przemarsz wszystkich grup Bastoners de Sant Cugat (tancerzy z kijkami w "
        "tradycyjnych strojach) oraz grupy byłych tancerzy. Towarzyszy im zespół gralli "
        "(instrumentów dętych) i bębnów.\n\n"
        "Trasa: La Unió – Centre Cultural (c. Anselm Clavé 13-17), c. Teatre, c. Santa "
        "Maria, pl. dels Quatre Cantons, c. Endavallada, pl. Sant Pere, c. Major, pl. "
        "Octavià, c. Plana de l'Hospital, c. Abat Armengol, c. Salvador Espriu, Parc de "
        "Can Vernet."
    ),
}

with open("events_schedule.json", encoding="utf-8") as f:
    sched = json.load(f)

updated = 0
for e in sched:
    if e["id"] in TRANSLATIONS:
        e["description_pl"] = TRANSLATIONS[e["id"]]
        updated += 1

with open("events_schedule.json", "w", encoding="utf-8") as f:
    json.dump(sched, f, ensure_ascii=False, indent=2)

print(f"Updated description_pl for {updated} events")
