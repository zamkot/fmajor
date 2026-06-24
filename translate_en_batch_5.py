# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 5 of the full-catalog English translation pass (events 81-100 of 190)."""
import json

TRANSLATIONS = {
    1972: (
        "The \"Petits! Grans! Llibres!\" festival comes to the Cloister of Sant Cugat "
        "with a program dedicated to literature for early childhood.\n\n"
        "Organized by Institut de la Infància, this mini festival invites families to "
        "discover and enjoy a selection of books, picture books and stories especially "
        "designed for children aged 0 to 5.\n\n"
        "The activity offers a space to bring reading closer to the youngest and share "
        "moments around stories, imagination and books in a unique heritage setting "
        "like the Monastery's Cloister.\n\n"
        "Prior registration at https://museu.santcugat.cat/agenda/\n"
        "Free activity, limited capacity"
    ),
    1339: (
        "A space of art workshops to enjoy as a family!\n\n"
        "\"Connexions,\" a creative game for building free structures with wooden sticks "
        "and connectors, and \"Assemblatges,\" a 3D construction game. With Koala Art for "
        "Kids.\n\n"
        "\"El més forçut del circ,\" with Gest Lúdic l'Obrador. Workshop to build a "
        "circus character.\n\n"
        "\"Mastercook Experience\" cooking workshop, with The Playcook Kids (prior "
        "registration required)."
    ),
    1338: (
        "Come and enjoy a fun, creative culinary experience. Kids will cook recipes "
        "inspired by different cuisines from around the world, learn age-appropriate "
        "cooking techniques, and above all have a great time experimenting, creating "
        "and sharing as a team.\n\n"
        "An original, educational and delicious activity so they can experience "
        "cooking as a great adventure!\n\n"
        "Recommended age: 6-12 years\n"
        "Duration: 1 hour\n"
        "Free activity\n\n"
        "Individual or team registration (max 5 children per team) at "
        "https://tallersalombra-tallerdecuina.eventbrite.es"
    ),
    1342: "With the gralla and drum ensemble from the Escola de Música Tradicional.",
    1341: (
        "Come enjoy and share the passion for motorbikes! Ride open to all kinds of "
        "bikes: classic, modern and scooters. Free drinks and snacks for all attendees. "
        "During the gathering there will be small awards and recognitions: oldest bike, "
        "dirtiest bike, the Rat Penat award for most characterful exhaust, and many more "
        "surprises!\n\n"
        "In collaboration with: Vallès27, motorcycle workshop\n\n"
        "No registration needed\n\n"
        "Route: pl. Sant Francesc, c. Joan XXIII, c. Salvador Espriu, pg. Francesc "
        "Macià, rbla. Celler, c. Francesc Moragas, av. Rius i Taulet, av. Lluís "
        "Companys i Jover, c. Àngel Guimerà, rbla. Ribatallada, av. Pla del Vinyet, av. "
        "Torre Blanca, rbla. del Celler, c. Francesc Macià, c. Abat Guillem d'Avinyó, "
        "av. Ragull, c. Santa Engràcia, Jardins de Sant Francesc"
    ),
    1400: (
        "Alba, a city in Italy's Piedmont region, has been twinned with Sant Cugat "
        "since 2007. This year, to strengthen ties between the twin cities, their "
        "Compagnia Sbandieratori e Musici Borgo San Lorenzo has been invited to take "
        "part in Festa Major.\n\n"
        "They will accompany various events of our popular culture and paint several "
        "squares blue and white with their characteristic flag display, waving and "
        "throwing flags into the sky. Founded in 1984, the Sbandieratori Borgo San "
        "Lorenzo strive to keep this tradition of their homeland alive, teaching and "
        "performing the art of flag-waving. They are members of the Italian Flag-Wavers "
        "League and compete every year in their National Championship with excellent "
        "results."
    ),
    1344: (
        "A guided visit to the Monastery centered on the three summer festivities of "
        "interest to Sant Cugat: Sant Joan and the start of summer, Sant Pere, the "
        "town's patron saint; and Sant Cugat, patron saint of the Monastery.\n\n"
        "Free activity\n\n"
        "Prior registration at https://museu.santcugat.cat/agenda/"
    ),
    1347: (
        "Sign up for the wildest tournament of the year — fast, strategic and a lot of "
        "fun! Pair up with a friend and get ready to eliminate as many pairs as you "
        "can... before they eliminate you!\n\n"
        "Pair registration from June 11th at cugat.cat/fm-torneig-globus"
    ),
    1346: "With Vinylics",
    1345: (
        "Come and enjoy a fun, creative culinary experience. Kids will cook recipes "
        "inspired by different cuisines from around the world, learn age-appropriate "
        "cooking techniques, and above all have a great time experimenting, creating "
        "and sharing as a team.\n\n"
        "An original, educational and delicious activity so they can experience "
        "cooking as a great adventure!\n\n"
        "Recommended age: 6-12 years\n"
        "Duration: 1 hour\n"
        "Free activity\n"
        "Individual or team registration (max 5 children per team) at "
        "https://tallersalombra-tallerdecuina.eventbrite.es"
    ),
    2009: (
        "Swing, pop, ballads... a concert full of rhythm to celebrate Festa Major.\n\n"
        "Direction: Enric Mestre"
    ),
    1349: None,
    1351: None,
    1350: (
        "Prior registration required on the club's Instagram.\n"
        "@rugbysantcugat"
    ),
    2024: (
        "The funfair continues on the following days:\n"
        "Sunday 28, 5 pm to 1 am\n"
        "Monday 29, 5 pm to midnight\n\n"
        "From 5 to 7 pm music and intense lighting on the rides will be temporarily "
        "switched off."
    ),
    2018: "Open participation for everyone",
    1355: (
        "\"Pintxo Pote\" is a culinary tradition from the Basque Country combining a "
        "\"pintxo\" with a \"pote\" (drink). You'll also find traditional Basque activities "
        "and music.\n\n"
        "5 pm Space opens\n"
        "6 pm \"Pintxopote\" begins (6 varieties of pintxos + drink)\n"
        "7 pm \"Txapela\" of Basque popular games\n"
        "8 pm \"Sokatira\" (tug of war)\n"
        "8.30 pm DJ music until closing\n\n"
        "Throughout the afternoon, traditional Basque music will set the mood for the "
        "space.\n"
        "We encourage local groups (\"penyes\") to take part in the first Txapela of "
        "popular games. There will be a prize for the winning group!"
    ),
    1352: (
        "A comedy of festive resistance. In some European office full of binders, it's "
        "decided that Festa Major de Sant Cugat is too noisy... but the retirement home "
        "declares itself ready to party!\n\n"
        "With Grup de Teatre Còmic Llar, directed by Gisela Figueras"
    ),
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
