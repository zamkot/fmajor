# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 4 of the full-catalog English translation pass (events 61-80 of 190)."""
import json

TRANSLATIONS = {
    1319: (
        "An energy-packed concert with classic and contemporary gospel songs, backed by "
        "a live band.\n\n"
        "Cor de Gòspel Sant Cugat was founded in 2008 on the initiative of Erwyn "
        "Seerutton and a group of participants from one of his workshops. The choir is "
        "made up of dozens of enthusiastic singers who form an ambitious project of "
        "exemplary musical and artistic growth.\n\n"
        "The choir offers tailored concerts mainly for charitable purposes in support of "
        "social action organizations, and over the years has raised significant funds "
        "for these social organizations."
    ),
    1317: (
        "Alba Careta, trumpet and voice. Lucas Martínez, tenor sax. Roger Santacana, "
        "piano. Giuseppe Campisi, double bass. Jordi Pallarés, drums\n\n"
        "Alba Careta is one of the most prominent jazz performers and composers in "
        "Spain and a reference in European jazz. She presents \"Panical,\" an album that "
        "delves into the land as a source of inspiration, guided by the strength of "
        "roots and the female figures that set the pulse of this work. A celebration of "
        "resistance and untamed beauty, inspired by strong, rebellious women who stay "
        "true to themselves."
    ),
    2487: (
        "A Festa Major dance show with Esbart Mediterrània and musical accompaniment by "
        "Cobla Marinada, directed by maestro Dani Gasulla i Porta.\n\n"
        "Program: Popular dances and choreographies by Salvador Mel·lo, Albert Sans, "
        "David Martínez, Laia Travé, Mercè Andrés, Marta Manyoses and David Gil.\n"
        "Vocals: Adrià Garcia Alegre\n"
        "Direction: David Gil, Esther Madrona, Anna Mayol and Francesc Picornell.\n"
        "Organized by: Esbart Mediterrània"
    ),
    1323: (
        "Rock, energy, party, emotions and musical rhapsody is what Indubio brings to "
        "the stage. A live show full of original music, hard-hitting songs, ballads and "
        "a couple of iconic covers to make everyone who shares the night with them jump, "
        "dance and sing."
    ),
    1387: "They're the one and only, the unmistakable, the incomparable... they're Pubilles Ninja! A folk rock band with generous doses of humor.",
    1388: "Festa Major versots by the Diables de Sant Cugat.",
    1389: (
        "Coco, the 100% female cover band that's killing it! A genuine show serving up a "
        "cocktail of covers from all eras, medley-style and full of fun.\n\n"
        "Coco has become a reference for artistic female empowerment, without wanting to "
        "turn it into a slogan, with four charismatic members and a knack for blending "
        "songs that connect deeply with the audience from minute one. Watch out at their "
        "concerts though, because they guarantee lost voices, sore muscles, euphoria and "
        "extreme happiness!"
    ),
    2077: "Swing music and dancing\n\nIn collaboration with: Xarxa de Centres Culturals",
    1392: (
        "A veteran shaker of the Barcelona scene on multiple fronts. In the late "
        "nineties, she founded the Magic in the Air club in Barcelona, which became an "
        "unquestionable reference for sixties culture, especially its pop and rock side, "
        "without leaving aside Black music and groove rhythms."
    ),
    1390: (
        "Tapeo Sound System celebrate their 15th anniversary in 2026 with a very special "
        "tour. They present the most complete show they've ever done, with a unique, "
        "energy-packed cover repertoire that unites generations. With staging carefully "
        "crafted down to the last detail and their characteristic touch of humor and "
        "closeness, they always connect with an audience that keeps growing year after "
        "year."
    ),
    1393: (
        "A DJ who favors varied, dynamic sets, mixing current hits with legendary songs "
        "everyone ends up singing. With an easygoing, natural style, he knows how to "
        "read the room and adapt the music to each moment so the dance floor never loses "
        "its rhythm. His sets blend party, nostalgia and energy, connecting with very "
        "different audiences while never losing the thread of the night. This year he "
        "comes to Festa Major in a nighttime slot with an adapted format; for dancing, "
        "singing and enjoying until the end."
    ),
    1333: (
        "La Botiga al carrer returns to Festa Major de Sant Cugat, turning the city's "
        "streets into a great showcase for local commerce. Coinciding with the start of "
        "the summer sales season, participating businesses take to the street to bring "
        "their products and services closer to the public.\n\n"
        "This initiative has established itself as one of the most traditional and "
        "participatory activities of Festa Major, drawing thousands of people who take "
        "the day to stroll, shop and discover what local businesses have to offer.\n\n"
        "Beyond special promotions and discounts, some businesses round out their "
        "participation with workshops and activities open to the public, helping create "
        "a festive, lively atmosphere in the city center."
    ),
    1332: (
        "ZEM La Guinardera hosts the Spanish Veterans Fencing Championship, a national "
        "competition bringing together athletes from different age categories (+30, "
        "+40, +50, +60 and +70) in men's and women's events.\n\n"
        "The championship includes individual events in all three fencing weapons: "
        "foil, épée and sabre."
    ),
    1331: (
        "The 3x3 Charity Basketball Tournament is a sporting event open to participation "
        "as part of Festa Major de Sant Cugat.\n\n"
        "Organized in collaboration with Thionck Essyl Basketball, the tournament has a "
        "charitable purpose, with proceeds going to the Senegal project supported by "
        "QBasket Sant Cugat.\n\n"
        "Prior registration required at "
        "https://qbasketsantcugat.com/producte/inscripcio-3x3-solidari-per-senegal/"
    ),
    1330: (
        "A competition-format exhibition in different archery disciplines.\n\n"
        "Open participation for archery beginners.\n\n"
        "Prior registration required — contact the club at "
        "arquersdesantcugat@gmail.com"
    ),
    1968: "Discover how the environment is affected by today's conflicts.",
    1300: (
        "Come and enjoy the Sports Festival, with recreational and sporting activities "
        "for the whole family. A space full of activities and equipment where young and "
        "old alike can move, play and discover different sports.\n\n"
        "11 am Yoga for everyone, by Ashtanga Yoga Sant Cugat."
    ),
    1337: (
        "Simultaneous chess games are part of Festa Major de Sant Cugat's program and "
        "will feature the participation of a Catalan Master from the club.\n\n"
        "The activity is open to everyone and offers a chance to enjoy chess in a "
        "participatory, accessible atmosphere, sharing a day around this strategy "
        "game.\n\n"
        "An event designed to bring chess closer to the public as part of Festa Major's "
        "activity program."
    ),
    1335: (
        "A visit that lets you stroll practically alone through the interior of the "
        "Monastery and its church. You'll discover the history of the most powerful "
        "Monastery in the county of Barcelona and the symbolism of its magnificent "
        "cloister, the most important in Europe for Romanesque sculpture.\n\n"
        "Prior registration required at "
        "https://visit.santcugat.cat/visita-guiada-monestir-de-sant-cugat/"
    ),
    1334: (
        "A 10 km family bike ride so families can enjoy cycling while discovering their "
        "immediate surroundings.\n\n"
        "Route: Parc Central (c. Manel Farrés corner c. Rovellat); c. Ramon Llull, bike "
        "lane av. Països Catalans, bike lane ctra. Rubí, Martins racetrack roundabout, "
        "c. Cerdanya, av. Can Graells, c. Antoni Bell, Volpelleres station, c. Mare de "
        "déu del Roser, c. Alfons d'Aragó, av. Can Volpelleres, c. Ventura Gasol, bike "
        "lane c. Carles Riba, c. Màrius Torres, c. Clementina Arderiu, through Parc Pla "
        "Farreras, c. Abat Biure, bike lane av. Ragull, rbla. Torrent d'en Xandri, c. "
        "d'Orient, rbla. del Celler, bike lane c. Josep Puig i Cadafalch, bike lane av. "
        "Corts Catalanes, bike lane av. Pla del Vinyet, av. de Gràcia, c. Francesc "
        "Moragas, bike lane c. Rius i Taulet, av. Lluis Companys, c. Esperanto, c. Mercè "
        "Rodoreda, bike lane c. Manel Farrès, Parc Central."
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
