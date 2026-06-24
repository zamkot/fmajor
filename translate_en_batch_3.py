# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 3 of the full-catalog English translation pass (events 41-60 of 190)."""
import json

TRANSLATIONS = {
    1296: "With the Jazzin' Time combo and the participation of young people with intellectual disabilities.",
    1294: (
        "Open to everyone regardless of their condition, accessible and respectful of "
        "difference. A space for experimentation and collective creation, with the "
        "celebration of Festa Major as its guiding theme.\n\n"
        "Windown was born from an initiative by Andrés Moctezuma following the bond "
        "between Gusti and his son with Down syndrome, growing into an art and "
        "inclusion movement. Since 2014 they've run an inclusive creative space led by "
        "Inge Nouws, Isma Guzmán and Gusti Rosemffet. The workshop is based on "
        "\"relational aesthetics,\" fostering interaction among participants and free, "
        "spontaneous artistic creation."
    ),
    1302: (
        "The 2nd edition of the FM League arrives! If you're between 10 and 14 years "
        "old, form a team and enjoy your favorite sport in this tournament with 15-minute "
        "matches of 3x3 football, 4x4 handball, 3x3 basketball and 4x4 volleyball.\n\n"
        "Prior registration required at omet.santcugat.cat"
    ),
    1924: "Here you'll find a tent to prepare your banner for the Batucada Orgullosa parade.",
    1305: (
        "An open full-body training session with musical backing, combining cardio "
        "intervals with muscle strength work. A dynamic, accessible activity offering a "
        "full-body workout through intensity intervals, adapted so each participant can "
        "follow their own pace.\n\n"
        "A sporting activity within Festa Major de Sant Cugat designed to get moving, "
        "improve fitness and enjoy an active outdoor session.\n\n"
        "Open to everyone (no prior registration needed)"
    ),
    1304: (
        "The petanque tournament returns to Sant Cugat for its twelfth Festa Major "
        "edition, a competition open to everyone to enjoy this traditional outdoor "
        "sport.\n\n"
        "Petanque is a precision sport played in teams or individually, consisting of "
        "throwing metal balls trying to get them as close as possible to a small ball "
        "called the \"boliche.\""
    ),
    1303: (
        "Build your soapbox cart with friends, family or whoever you like, and get ready "
        "for the most spectacular downhill run of the year!\n\n"
        "Registration: androminesfmsantcugat@gmail.com until June 25th"
    ),
    1308: (
        "7.30 pm \"El viatge. Sortir del centre\" show, by Associació Mengue Guinée. The "
        "piece highlights and questions global inequalities through a dialogue between "
        "artistic worlds: different rhythms and dances from Guinea-Conakry meet "
        "traditional Catalan, Asturian and Argentine dances.\n\n"
        "8.15 pm Talk by Associació Joves Africans de Catalunya. A dialogue between the "
        "host and the musicians to learn more about their instruments, their roots and "
        "their culture, building bridges between cultures.\n\n"
        "9 pm Concert with Kamben, a group formed by African artists from Senegal and "
        "Guinea-Conakry. Traditional West African music linked to the Mandinka Empire "
        "and Afro-Mandinka music."
    ),
    1307: (
        "Els Pocavergonya is an inclusive theater group directed by Maria Vancells, part "
        "of the workshops offered in the Casa de Cultura's quarterly course catalog. "
        "Every Friday we come together and work to discover, through play and music, our "
        "talents, making room for differences to value what unites us. Come see us and "
        "enjoy it with us!"
    ),
    1306: (
        "Parade with the percussion group Karabassà for LGBTI+ Pride Day. A musical and "
        "activist proposal that fills the streets with rhythm, energy and a celebration "
        "of diversity.\n\n"
        "Route: plaça de Lluís Millet, carrer de Valldoreix, carrer de Sant Antoni, plaça "
        "de Barcelona."
    ),
    1936: (
        "Organized by Handbol Sant Cugat, the popular botifarrada (sausage feast) is an "
        "opportunity to share the table, good company and festive spirit with neighbors "
        "and athletes during Festa Major. A gathering open to everyone to enjoy popular "
        "cuisine in an emblematic setting like Parc de Can Vernet."
    ),
    1312: (
        "Backline Choir is made up of a very diverse group of people who share a love of "
        "singing and good times together. Founded in 2014 and currently directed by "
        "Aleix Losa. They always sing a cappella, without instruments, performing any "
        "modern music piece they like and that they think will also delight their "
        "audience."
    ),
    1311: (
        "8 pm LGBTI+ Pride Day Manifesto\n\n"
        "8.15 pm \"Special Pride\" Musical Bingo with @bingomusical. The best of bingo and "
        "karaoke at once. The best songs to dance, sing and celebrate the day of sexual "
        "liberation."
    ),
    1310: (
        "The Club Muntanyenc Sant Cugat's Botifarrada Popular is one of the most "
        "traditional culinary gatherings of Festa Major. Year after year, it brings "
        "Sant Cugat residents together in a festive, convivial atmosphere around the "
        "table.\n\n"
        "The menu includes botifarra sausage, bread with tomato, watermelon, coca "
        "(traditional flatbread) and craft beer or water. An ideal way to share a "
        "popular meal and enjoy the festive atmosphere with family and friends."
    ),
    1309: (
        "With Radicel·la\n\n"
        "\"Horabaixa\" (late afternoon) is that moment of the day when the sun sets and "
        "routine pauses, a time that invites us to reconnect and share without rushing. "
        "We travel through popular dances that everyone feels are their own, and "
        "discover movements that may at first seem foreign but that, over time, "
        "everyone ends up making their own."
    ),
    1315: (
        "The Malabarada and children's versots kick off the children's and youth "
        "correfoc of Festa Major de Sant Cugat.\n\n"
        "The youngest will enjoy a festive, participatory event led by popular culture, "
        "with the reading of children's versots and the characteristic atmosphere of "
        "the celebrations organized by the Diables de Sant Cugat."
    ),
    1316: (
        "With Petits Udols de Calella, Diables de Viladecans, Diables de Sant Joan "
        "Despí, Diables de la Creu Alta de Sabadell and Diables de Sant Cugat\n\n"
        "Two simultaneous routes:\n"
        "Youth route: plaça d'Octavià, carrer de la Plana de l'Hospital, carrer de Sant "
        "Esteve, carrer de la Indústria, carrer d'Abat Armengol, carrer de Santa Anna, "
        "plaça de Pep Ventura, carrer de Sant Martí, carrer de Castillejos, carrer de "
        "Sant Domènec, plaça de Sant Pere, carrer Major, plaça d'Octavià\n"
        "Children's route: plaça d'Octavià, carrer de Santiago Rusiñol, carrer del "
        "Carme, carrer de Gorina, plaça de Magí Bartralot, carrer de Gorina, plaça dels "
        "Quatre Cantons, avinguda de Rius i Taulet, Baixada de Sant Sever, avinguda de "
        "Catalunya, carrer d'Enric Granados, plaça de Sant Pere, carrer Major, plaça "
        "d'Octavià."
    ),
    1945: (
        "Música al Xiringuit-U hosts a jazz set with Andrea Calderón & Jazzin' Time, a "
        "concert within Festa Major's musical program.\n\n"
        "Jazzin' Time is a group focused on contemporary jazz language, with an open, "
        "flexible performance style based on improvisation and musical dialogue between "
        "the performers. This time they share the stage with singer Andrea Calderón, "
        "bringing a fresh, elegant proposal full of nuance.\n\n"
        "A session designed to enjoy live jazz in a close, open-air setting, within the "
        "festive atmosphere of Festa Major."
    ),
    1322: (
        "Olivia is a 12-year-old girl whose life turns upside down when her family is "
        "evicted and she has to move with her mother Íngrid and little brother Tim to an "
        "apartment in an outlying neighborhood. Íngrid falls into depression, so Olivia "
        "has to take care of Tim and herself while facing her own emotional earthquake. "
        "She then creates a fantasy: everything she's living isn't real, they're filming "
        "a movie. Olivia will find a new \"family\" that will help her rebuild her life "
        "and learn to survive adversity.\n\n"
        "Recommended age: for all ages\n"
        "Runtime: 71 min.\n\n"
        "In collaboration with: El Cinèfil"
    ),
    1321: (
        "An emerging band blending Andalusian and Catalan roots, led by guitarist Juan "
        "Slands with the magnetic voice of Ángela Quiralte. Their sound fuses funk and "
        "rock with touches of jazz and pop, always driven by an infectious groove."
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
