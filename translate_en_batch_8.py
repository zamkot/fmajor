# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 8 of the full-catalog English translation pass (events 141-160 of 190)."""
import json

TRANSLATIONS = {
    2093: (
        "Shows and recreational activities for the youngest and the whole family!\n\n"
        "Circus workshop, with Aire Circ Viu\n"
        "\"El Laberint,\" with Itinerància\n"
        "\"L'estrany viatge del Sr. Tonet,\" with Tombs Creatius\n"
        "Free experimentation and play space, with Pájaro Jocs\n"
        "Village of huts, with Gest Lúdic l'Obrador\n"
        "\"El Gargot picat,\" with Guixot de 8\n"
        "Inflatables\n"
        "Veolia space: mission H20"
    ),
    2090: (
        "Alba, a city in Italy's Piedmont region, has been twinned with Sant Cugat "
        "since 2007. This year, to strengthen ties between the twin cities, their "
        "Compagnia Sbandieratori e Musici Borgo San Lorenzo has been invited to take "
        "part in Festa Major. They will accompany various events of our popular "
        "culture and paint several squares blue and white with their characteristic "
        "flag display, waving and throwing flags into the sky.\n\n"
        "Founded in 1984, the Sbandieratori Borgo San Lorenzo strive to keep this "
        "tradition of their homeland alive, teaching and performing the art of "
        "flag-waving. They are members of the Italian Flag-Wavers League and compete "
        "every year in their National Championship with excellent results."
    ),
    1403: (
        "Swap and sell second-hand items! Join in with your friends and family! Check "
        "the rules here (santcugat.cat/festa major/andròmines).\n\n"
        "In-person registration at the activity venue."
    ),
    1401: (
        "A guided visit to the Monastery and the cloister led by people with Asperger "
        "syndrome, an autism spectrum disorder, aiming to overcome the stigma and "
        "prejudice surrounding this condition.\n\n"
        "Free activity\n\n"
        "Prior registration at https://museu.santcugat.cat/agenda/"
    ),
    1404: (
        "A traveling theatrical visit, led by Roger Casadellà, through the town's most "
        "iconic spots: the monastery, plaça d'Octavià, carrer Major and La Unió "
        "Santcugatenca.\n\n"
        "Activity linked to the Museu de Sant Cugat's temporary exhibition \"La capsa "
        "vermella d'Antoni Campañà. Fotos de guerra, art i Sant Cugat.\"\n\n"
        "Free activity\n\n"
        "Registration required at https://museu.santcugat.cat/agenda/"
    ),
    1395: (
        "One of the most anticipated and crowded events of Festa Major de Sant Cugat!\n\n"
        "With a record 1,519 entries (1,385 valid), the draw was held on Friday, June "
        "5th at the Ateneu Santcugatenc and determined that numbers between 1431 and "
        "1853 get a place in the contest, which will take place on Sunday, June 28th "
        "on avinguda de Can Volpelleres.\n\n"
        "Activity without bar service"
    ),
    1406: "With Emanems\n\nActivity without bar service",
    1298: None,
    2101: (
        "The funfair continues:\n"
        "Monday 29, 5 pm to midnight\n\n"
        "From 5 to 7 pm music and intense lighting on the rides will be temporarily "
        "switched off."
    ),
    1413: (
        "Setup of the beasts with the Guita from Ball de Diables de Santa Eulàlia de "
        "Ronçana i Lliçà d'Amunt and the Bou de l'Hospitalet."
    ),
    1411: (
        "Once again, Sound Qgat opens a space for all lovers of sound system culture in "
        "all its forms. Sotasons invites you on a journey from Africa to London, by way "
        "of the Caribbean, in a party featuring many different underground culture "
        "styles.\n\n"
        "6 pm Riki undersounds (ska to groove)\n"
        "7.30 pm La cara B (latin)\n"
        "9 pm Kharloss Selektah (dancehall)\n"
        "10.30 pm Trivnv (global bass)\n"
        "Midnight Lorast (dub to jungle)\n"
        "2 am End of party"
    ),
    1409: (
        "With Laberta Delpoblet\n\n"
        "In a forest a cuckoo sang with great eagerness, calling for its companion "
        "from the top of a tall oak... Little animals and creatures play hide and seek "
        "among the branches. When we find them, each one brings us its own story! Will "
        "you help us look for them?\n\n"
        "Recommended age: 3+\n"
        "Duration: 45-50 min."
    ),
    1408: (
        "Registration for the Festa Major Rummikub tournament until June 22nd at "
        "info@afavalles.com\n\n"
        "No prior registration needed for the board games\n"
        "Donation per team: €10 (see tournament rules)\n\n"
        "There will also be the finishing touches on a large painting made with the "
        "people of Espai Respir AFA and the Windown art collective, to experience art "
        "with all the senses.\n\n"
        "From 6 to 8 pm; limited to 64 participants"
    ),
    1402: (
        "Shows and recreational activities for the youngest and the whole family!\n\n"
        "Circus workshop, with Aire Circ Viu\n"
        "\"El Laberint,\" with Itinerància\n"
        "\"L'estrany viatge del Sr. Tonet,\" with Tombs Creatius\n"
        "Free experimentation and play space, with Pájaro Jocs\n"
        "Village of huts, with Gest Lúdic l'Obrador\n"
        "\"El Gargot picat,\" with Guixot de 8\n"
        "Inflatables\n"
        "Veolia space: mission H20\n\n"
        "Shows:\n"
        "6 pm and 7 pm \"Batibull de contes al parc,\" stories with Laberta Delpoblet\n"
        "7 pm \"K'Mon Tour,\" traveling show by cia. PerNassos\n"
        "8 pm \"Back2Classics,\" circus and clowning with Planeta Trampolí."
    ),
    2114: (
        "Parade with the Ball de Diables de Torredembarra, the Guita from Ball de "
        "Diables de Santa Eulàlia de Ronçana i Lliçà d'Amunt, the Bou de l'Hospitalet "
        "and the Ball de Panderos dels Monjos. With the participation of the Ball de "
        "Cintes de Sant Cugat.\n\n"
        "Route: pl. Barcelona, c. Xerric, c. Sant Bonaventura, rbla. del Celler, c. "
        "Sant Medir, pl. d'Octavià"
    ),
    1412: (
        "Will you be able to solve Gaudire's operation in time?\n\n"
        "Extra, extra! A smoke device threatens to plunge the city into darkness. "
        "Solve the trials and decipher the riddles to find out who's behind it! Time "
        "is running out and there's less than an hour to act. Follow the clues and "
        "deactivate the mysterious device before everything is covered in darkness!\n\n"
        "Activity aimed at young people aged 12 and up (children under 12 cannot "
        "participate)\n"
        "Registration at "
        "https://www.entrapolis.com/entrades/escape-room-sant-cugat-del-valles\n"
        "Teams of 4 to 6 people, one registration per team\n"
        "Limited capacity\n\n"
        "By Gaudire"
    ),
    2117: (
        "With Laberta Delpoblet\n\n"
        "In a forest a cuckoo sang with great eagerness, calling for its companion "
        "from the top of a tall oak... Little animals and creatures play hide and seek "
        "among the branches. When we find them, each one brings us its own story! Will "
        "you help us look for them?\n\n"
        "Recommended age: 3+\n"
        "Duration: 45-50 min."
    ),
    1417: (
        "With cia. PerNassos\n\n"
        "A traveling show where two tour guides lead a particular \"tour\" to discover "
        "the town's iconic spots. Through the clown's eyes, it puts urban space at the "
        "center and seeks, as a backdrop, collective reflection on mass tourism and its "
        "impact on the community and the territory. An experience meant to be lived "
        "walking, laughing, sharing and looking at public space with different eyes.\n\n"
        "Starting point: circus workshop space"
    ),
    1415: (
        "Rhythms of India, Bollywood dance and Bollywood Folk blending different styles "
        "and creating colorful, eye-catching musical numbers."
    ),
    2120: (
        "Showcase of Festa Major dances at plaça d'Octavià, with the Ball de Diables de "
        "Torredembarra, the Guita from Ball de Diables de Santa Eulàlia de Ronçana i "
        "Lliçà d'Amunt, the Bou de l'Hospitalet and the Ball de Panderos dels Monjos. "
        "With the participation of the Ball de Cintes de Sant Cugat."
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
