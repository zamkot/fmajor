# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 7 of the full-catalog English translation pass (events 121-140 of 190)."""
import json

TRANSLATIONS = {
    2063: (
        "Introduced by the film's director, Sant Cugat local Judith Colell.\n\n"
        "In 1943, in the midst of World War II, dictator Franco has blocked the "
        "Pyrenees crossing for Jews fleeing Nazi repression toward Spain. A customs "
        "officer with a Republican past decides to disobey orders and help as many "
        "people escape as he can. Through this act of resistance, he and his wife will "
        "also have to confront the scars left by the recent Civil War.\n\n"
        "Runtime: 101 min.\n"
        "In collaboration with: El Cinèfil"
    ),
    2059: (
        "The vintage pop of Sergi Carós, who has found success on international radio "
        "and at Liverpool's iconic Cavern. He'll perform as a quartet (Sergi Carós, Nau "
        "León, Miguel Alberte, Roberto Olori), running through tracks from "
        "\"Popteràpia\" and 60s pop classics."
    ),
    1379: (
        "After a long 8-year absence, the rockiest lizards of the Barcelona scene are "
        "back. With 5 albums released and over 800 concerts behind them, and having "
        "shared the stage with Whitesnake, M-Clan, Fito & Fitipaldis and Jarabe de Palo, "
        "Sol Lagarto's return isn't meant to prove anything to anyone, but to pay "
        "tribute to themselves and remind everyone that, however much they shed their "
        "skin, they're made for rock and the stage.\n\n"
        "In 2025 they released three songs: \"Siempre,\" \"Con sólo una mirada\" and "
        "\"Fuego,\" signaling a new creative chapter full of energy and authenticity. "
        "Long live."
    ),
    1378: (
        "A guided visit to discover the Monastery's cloister by candlelight, learning "
        "about medieval lighting methods and the symbolism of light at night.\n\n"
        "Registration required at https://museu.santcugat.cat/agenda/"
    ),
    1376: (
        "This choir unites a passion for rock, the energy of live performance and "
        "choral music. Sant Cugat Rock Choir was formed in 2021 as part of a national "
        "network of rock choirs. They've performed at the Palau Sant Jordi alongside "
        "sister choirs on Miguel Ríos's tour, and this year performed at the "
        "Teatre-auditori Emma Vilarasau with over 200 singers on stage. Their concert at "
        "the city's Festa Major is without doubt a must-see for the choir!"
    ),
    1382: None,
    1383: "In collaboration with: Xarxa de Centres Culturals",
    1384: (
        "Like a good wine, Sybarites are approaching 15 years on the scene at a moment "
        "of complete maturity. Sybarites are a party, a cover band with soul and a key "
        "presence in Catalonia's Jamaican music scene over the last decade.\n\n"
        "Established as the leading festive proposal for Jamaican music, with 200 "
        "performances to prove it: local festivals, private celebrations, music "
        "festivals... The formula is simple: great hits revisited in ska and rocksteady "
        "style. Yesterday's hits (Whitney Houston, Abba, Cher) and today's (Lady Gaga, "
        "Dua Lipa, Miley Cyrus), an accessible, inclusive repertoire that brings "
        "Jamaican music to the wider public."
    ),
    1381: "Covers from the 70s, 80s and 90s!",
    1385: (
        "With Diables de Sant Joan Despí, Diables de Cubelles, Diables de la Creu Alta "
        "de Sabadell, Tro de Falguera de Sant Feliu de Llobregat and Diables de Sant "
        "Cugat\n\n"
        "Two simultaneous routes:\n"
        "\"Infern\" route: pl. Octavià, c. Plana Hospital, c. Abat Armengol, c. de la "
        "Mina, c. Aymerich, c. Sant Martí, c. Sabadell, pl. Sant Pere, c. Major, pl. "
        "Octavià.\n\n"
        "\"Espurna\" route: pl. Octavià, c. Santiago Rossinyol, c. del Carme, c. Gorina, "
        "pl. Magí Bartralot, c. Gorina, pl. dels Quatre Cantons, av. Rius i Taulet, "
        "Baixada de Sant Sever, av. Catalunya, c. Enric Granados, pl. Sant Pere, c. "
        "Major, pl. Octavià."
    ),
    1386: (
        "Saxophonist, clarinetist and singer, Australian Adrian Cunningham is one of "
        "the leading figures of classic jazz today. Based in New York, he has performed "
        "at international clubs and festivals such as Montreux, the Blue Note Jazz "
        "Festival and the Melbourne International Jazz Festival, and has shared the "
        "stage with musicians like Wynton Marsalis, Wycliffe Gordon and Jeff "
        "Hamilton.\n\n"
        "With an elegant, virtuosic style deeply rooted in tradition, Cunningham "
        "combines authenticity and energy in every concert. This time he's joined by "
        "musicians Joan Mar Sauque Vila (trumpet), Gerard Nieto (piano), Giuseppe "
        "Campisi (double bass) and Arnau Julià (drums).\n\n"
        "In collaboration with: Xarxa de Centres Culturals"
    ),
    2140: (
        "An explosion of Black music, funk, sweat and tears of joy is what they offer "
        "every time they take the stage. Venues, festivals and parties across Spain and "
        "Europe confirm it. Throughout 2025-26 they've been presenting their new lineup "
        "and playing tracks from their latest LP \"Ain't no talkin' bout the wig.\""
    ),
    1432: (
        "With the Seguici's traditional figures, the Escola de Música Tradicional de "
        "Sant Cugat and the electronic beats of Marcel Casellas."
    ),
    1433: (
        "Concert of today's best popular, festive melodies with a gralla, percussion "
        "and electronic ensemble."
    ),
    1394: (
        "Parade of all the Bastoners de Sant Cugat groups and a group of former "
        "dancers, accompanied by the group's gralla and drum players.\n\n"
        "Route: La Unió-Centre Cultural (c. Anselm Clavé 13-17), c. Teatre, c. Santa "
        "Maria, pl. dels Quatre Cantons, c. Endavallada, pl. Sant Pere, c. Major, pl. "
        "Octavià, c. Plana de l'Hospital, c. Abat Armengol, c. Salvador Espriu, Parc de "
        "Can Vernet."
    ),
    2082: (
        "Before the traditional Festa Major Rice Contest begins, participants can "
        "collect the materials they need.\n\n"
        "The organizers will provide basic ingredients — water, rice and oil — as well "
        "as fire numbers, handed out between 9.30 and 11 am.\n\n"
        "As every year, all proceeds raised will go to Càritas Sant Cugat."
    ),
    1396: "Petanque competition for randomly drawn pairs.",
    1399: (
        "If you've ever wanted to have a fencing duel with family or friends, now's "
        "your chance!\n"
        "Beginner fencing activity, on regulation pistes, open to everyone, young and "
        "old.\n\n"
        "Prior registration required at https://esgrimasantcugat.cat/festa-de-duels/ "
        "or info@esgrimasntcugat.cat"
    ),
    1398: "Circuit of baseball and softball activities, open to everyone, young and old.",
    1397: "Beginner tennis activity, open to everyone.",
}

with open("events_schedule.json", encoding="utf-8") as f:
    sched = json.load(f)

updated = 0
for e in sched:
    if e["id"] in TRANSLATIONS:
        value = TRANSLATIONS[e["id"]]
        if value is not None:
            e["description_en"] = value
            updated += 1

with open("events_schedule.json", "w", encoding="utf-8") as f:
    json.dump(sched, f, ensure_ascii=False, indent=2)

print(f"Updated description_en for {updated} events")
