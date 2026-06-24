# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 2 of the full-catalog English translation pass (events 21-40 of 190)."""
import json

TRANSLATIONS = {
    1328: (
        "Courtesy of the Phonodisco Club collective, Olau arrives — the DJ and La "
        "Floresta local will offer a signature electronic set: disco & jackin' house to "
        "keep you dancing all night."
    ),
    1329: (
        "Marc Navarro is a versatile DJ who adapts each set to the audience and the "
        "moment, offering dynamic, energy-packed sets. He is currently resident DJ at "
        "Moon Sant Cugat and has also played in well-known booths such as Bling Bling "
        "Barcelona, Twenties Barcelona, Costa Este and BeOut, among others, building a "
        "style that connects with all kinds of audiences."
    ),
    1327: (
        "If you're after something mellow, keep looking, but if you want a party with "
        "guitars that pop, riffs that lift you up and a live show that will blow your "
        "mind, Big Mouthers is your cover band. A concert that runs through all the "
        "anthems of music history and today's most festive songs, with a band of "
        "innate flair — leather jackets, boots, tight pants and more attitude than a "
        "neighborhood rebel."
    ),
    1285: (
        "Festa Major padel tournament with different categories.\n\n"
        "Registration required at www.familiaamic.cat, familiaamic@gmail.com / 623 101 549\n\n"
        "The FamiliaAMIC association is a non-profit organization whose main goal is to "
        "promote equal opportunities and greater access to social and individual rights "
        "for people with intellectual disabilities and their families."
    ),
    1286: (
        "With summer's arrival, Casa Aymat. Espai de Creació opens its doors for Festa "
        "Major!\n\n"
        "10 am Welcome and breakfast\n"
        "10 am to 1 pm:\n"
        "- Art as a family. Looms in the street, with the art.santcugat educational team. "
        "Learn to weave a tapestry as a family.\n"
        "- Weft, weft, weft, with the art.santcugat educational team. An activity to "
        "discover and learn the technique of tapestry weaving.\n"
        "- Open workshops and studios: a tour through the spaces of Casa Aymat to see the "
        "students' work and the projects of this year's resident artists.\n\n"
        "1.30 pm Communal snack. Bring something to eat and share to close out the season "
        "together.\n\n"
        "With the participation of Casa Aymat. Espai de creació's members.\n"
        "Sponsored by Rabassaires and Katia."
    ),
    1287: (
        "A great spread of games to enjoy as a family for Festa Major!\n\n"
        "\"Pirene,\" by Apikipala. An invitation to discover the landscapes of the "
        "Pyrenees in an installation that combines art, craft, mechanics and play.\n"
        "\"Lilliput,\" by Tombs Creatius. A proposal where stories aren't told... they're "
        "played!\n"
        "Giant games workshop, with Circ de les Musaranyes\n\n"
        "From 10.30 am to 1.30 pm"
    ),
    1288: (
        "La Teulada is an information point offering technical support and advice on "
        "energy transition. There will also be hands-on workshops aimed at bringing "
        "renewable energy closer to the public in a clear and practical way.\n\n"
        "From 11 am to 8 pm"
    ),
    1289: (
        "A big band made up of students and teachers from Aula de So, where music is "
        "developed in a collaborative, high-standard environment. With a repertoire of "
        "jazz, Latin and modern music, AJO has performed at landmark festivals and "
        "venues, establishing itself as a project with a track record and an identity of "
        "its own."
    ),
    1290: (
        "Inspector Aparicio and Jeni need your help to solve a crime at the Archive. Come "
        "help them crack this investigation!\n\n"
        "For all ages. Free Festa Major activity. Limited places\n\n"
        "Registration at arxiu@santcugat.cat\n\n"
        "In collaboration with: Mira-sol teatre"
    ),
    1291: (
        "Prior registration required at handbolsantcugat@hotmail.com\n\n"
        "Beach handball is a team sport in which two teams pass and bounce or roll a "
        "ball, trying to get it into the opposing team's goal. The game is similar to "
        "standard handball, but played on sand instead of a solid surface."
    ),
    1899: (
        "Volleyball match between Sant Cugat's local media and politicians, for Festa "
        "Major."
    ),
    1292: (
        "The Festa Major chess tournament returns to Sant Cugat with a second edition "
        "designed to enjoy chess in an open, fast-paced and highly participatory "
        "atmosphere. The Club d'Escacs Dos Torres Sant Cugat organizes this rapid-game "
        "tournament as part of Festa Major, aiming to bring chess closer to players of "
        "all ages and levels.\n\n"
        "Swiss system, 8 rounds\n"
        "Rapid-game tournament, open to everyone.\n"
        "Prior registration required at escacsdostorres@gmail.com or "
        "www.escacsdostorresdesantcugat.cat\n\n"
        "From 5 pm to 8.30 pm. Presentation at 4.45 pm before it starts and prize-giving "
        "at 8.45 pm"
    ),
    1271: (
        "The funfair continues on the following days:\n"
        "Saturday 27, 5 pm to 2 am\n"
        "Sunday 28, 5 pm to 1 am\n"
        "Monday 29, 5 pm to midnight\n\n"
        "From 5 to 7 pm music and intense lighting on the rides will be temporarily "
        "switched off."
    ),
    2416: (
        "Mecànic Pizza invites you to celebrate Festa Major with Pizza Week!\n\n"
        "We open the Mirai Ceramies exhibition at Mecànic Pizza with an aperitif and "
        "tasting of our products. An open gathering bringing together ceramics, pizza, "
        "fire and handcraft.\n\n"
        "Free entry; 6 to 8 pm"
    ),
    1916: (
        "Come and enjoy the Sports Festival, with recreational and sporting activities "
        "for the whole family. A space full of activities and equipment where young and "
        "old alike can move, play and discover different sports."
    ),
    1912: None,
    1907: (
        "A food showcase open to everyone, with summer cuisine and produce and drinks "
        "that bring the party. Bocamoll's chef, Pepe Vidal, will prepare a dish served as "
        "a tapa. Manel Guirado — cook, sommelier and coordinator of the Aula "
        "Gastronòmica — will pair it with a wine and a cocktail.\n\n"
        "Registration at centresculturals.santcugat.cat or casaltorreblanca@santcugat.cat"
    ),
    1301: (
        "Ages 18 and up\n\n"
        "Prior registration required — contact the Club at its offices.\n\n"
        "The F7 (7-a-side football) tournament is a sporting competition in which teams "
        "play football matches with 7 players on the field, including the goalkeeper. "
        "It's a smaller, more dynamic format than 11-a-side football, with fast-paced, "
        "high-tempo matches."
    ),
    1299: (
        "6 pm CMSC rhythmic gymnastics section\n"
        "7 pm Club Gimnàstica Rítmica i Estètica Sant Cugat"
    ),
    1297: (
        "Inspector Aparicio and Jeni need your help to solve a crime at the Archive. Come "
        "help them crack this investigation!\n\n"
        "For all ages. Free activity. Limited places\n\n"
        "Registration at arxiu@santcugat.cat\n\n"
        "In collaboration with: Mira-sol teatre"
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
