# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 6 of the full-catalog English translation pass (events 101-120 of 190)."""
import json

TRANSLATIONS = {
    1358: (
        "With the groups Geganters de La Llàntia de Mataró, Geganters de Santa Eulàlia "
        "de Ronçana, Gegants de Puigcerdà, Gegants de Sant Jaume de Barcelona, "
        "Geganters de Valldoreix, Gegants de Rubí, Gegants de Falset, Gegant Inquiet de "
        "Catalònia Fundació Creactiva and Geganters de Sant Cugat."
    ),
    1359: "With Minyons de Terrassa, Nens del Vendrell and Castellers de Sant Cugat",
    1357: "With Sossy de Swert, in collaboration with Jambo Art",
    1295: (
        "A food showcase open to everyone, with summer cuisine and produce and drinks "
        "that bring the party. The Aula Gastronòmica's chef and teacher, Manel Guirado, "
        "will prepare a dish served to attendees as a tapa. Anton Sabariego, beer and "
        "wine expert and brewer, and co-owner of Bocamoll, will pair it with a beer and "
        "a wine.\n\n"
        "Registration at centresculturals.santcugat.cat or casaltorreblanca@santcugat.cat"
    ),
    1272: "FMA program",
    1362: (
        "Traditional concert of Catalan popular repertoire and Clavé songs, with the "
        "century-old Coral La Unió and other guest choirs.\n\n"
        "Free entry"
    ),
    1363: (
        "6.45 pm Dj Fem Lindy\n"
        "7 pm Open solo jazz class with Roser Ros (individual swing dance)\n"
        "7.45 pm Open lindy hop class with Berta and Miquel Claparols (partner swing "
        "dance)\n"
        "8.45 pm Open beginner's blues class with Sandra Fuentes & Jordi Figueras "
        "(partner dance)\n\n"
        "In collaboration with: Xarxa de Centres Culturals"
    ),
    2039: (
        "With the groups Geganters de La Llàntia de Mataró, Geganters de Santa Eulàlia "
        "de Ronçana, Gegants de Puigcerdà, Gegants de Sant Jaume de Barcelona, "
        "Geganters de Valldoreix, Gegants de Rubí, Gegants de Falset, Gegant Inquiet de "
        "Catalònia Fundació Creactiva and Geganters de Sant Cugat.\n\n"
        "Route: av. Cerdanyola, c. de la Creu, c. Torre, pl. Octavià, c. Santiago "
        "Rusiñol, pl. dels Quatre Cantons, av. Rius i Taulet, c. Enric Granados, pl. de "
        "Sant Pere, c. Major, pl. Octavià.\n\n"
        "Accessible quiet section: c. Enric Granados"
    ),
    1365: (
        "With Jazzduopop. Ten wineries and over 40 wines from different designations of "
        "origin to taste!\n\n"
        "Advance sale at Vins Noè and at tastos.vinsnoe.com from June 15th\n"
        "Tickets sold one hour before start, at Celler Modernista\n"
        "Limited capacity\n\n"
        "Smoking, outside food and pets are not allowed inside the venue. Drink "
        "responsibly."
    ),
    1364: "Urban dance festival performed by students of Escola Sant Cugat.",
    1354: (
        "A sporting event open to all audiences, no prior registration needed.\n\n"
        "Follow them on social media @jaleo.santcugat"
    ),
    1367: (
        "With the traditional dance groups Caporales San Simón, Morenada Sant Cugat, "
        "Morenada Central Oruro and Morenada Unión Boliviana\n\n"
        "Route: pl. Lluís Millet, c. Villà, c. Valldoreix, c. Sant Antoni, c. Xerric, c. "
        "Sant Bonaventura, c. Valldoreix, pl. Doctor Caltés, c. Martorell, av. Lluís "
        "Companys, c. Rosselló, c. Valldoreix, pl. Lluís Millet."
    ),
    1369: "Club Rugby Sant Cugat",
    1368: (
        "A chance to enjoy a vibrant concert. An explosion of energy, emotion and voices "
        "that will reach your heart with music that will get you out of your seat."
    ),
    1370: "Dance show by the Color Dansa Carol Morgado school",
    2049: (
        "With the groups Geganters de La Llàntia de Mataró, Geganters de Santa Eulàlia "
        "de Ronçana, Gegants de Puigcerdà, Gegants de Sant Jaume de Barcelona, "
        "Geganters de Valldoreix, Gegants de Rubí, Gegants de Falset, Gegant Inquiet de "
        "Catalònia Fundació Creactiva and Geganters de Sant Cugat."
    ),
    1348: (
        "World premiere of the symphonic version of \"Paga-li, Joan,\" arranged by Sant "
        "Cugat local Biel Vouillamoz.\n\n"
        "Direction: Xavier Pagès-Corella\n\n"
        "Concert in aid of Càritas Sant Cugat"
    ),
    1343: (
        "Alba, a city in Italy's Piedmont region, has been twinned with Sant Cugat "
        "since 2007. This year, to strengthen ties between the twin cities, their "
        "Compagnia Sbandieratori e Musici Borgo San Lorenzo has been invited to take "
        "part in Festa Major.\n\n"
        "They will accompany various events of our popular culture and paint several "
        "squares blue and white with their characteristic flag display, waving and "
        "throwing flags into the sky. Founded in 1984, the Sbandieratori Borgo San "
        "Lorenzo strive to keep this tradition of their homeland alive, teaching and "
        "performing the art of flag-waving. They are members of the Italian "
        "Flag-Wavers League and compete every year in their National Championship with "
        "excellent results."
    ),
    1375: (
        "An explosive group that revives the vibrant spirit of the great swing and "
        "lindy hop nights. With a repertoire full of rhythm, elegance and infectious "
        "energy, they invite the audience to travel to the jazz clubs of the thirties "
        "and forties, where music was synonymous with dance, improvisation and "
        "celebration.\n\n"
        "The band brings together some of the most prominent musicians on the Catalan "
        "jazz scene: Oriol Vallès on trumpet, Lluc Casares on tenor sax, Alba Pujals on "
        "trombone, Jöel González on piano, Camil Arcarazo on double bass and Xavi "
        "Hinojosa on drums.\n\n"
        "In collaboration with: Xarxa de Centres Culturals"
    ),
    1374: (
        "A showcase full of energy and excitement from all the students. A celebration "
        "open to everyone to enjoy the art of dance and the festive spirit of Festa "
        "Major."
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
