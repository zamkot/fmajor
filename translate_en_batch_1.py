# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 1 of the full-catalog English translation pass (events 1-20 of 190)."""
import json

TRANSLATIONS = {
    1284: "Energetic, fun-loving sessions mixing pop, 2010s hits and old-school reggaeton.",
    2411: (
        "Mecànic Pizza invites you to celebrate Festa Major with Pizza Week!\n\n"
        "We head out to nature for dinner at Masia Can Domènech, at the foot of Collserola. "
        "Guided visit of the estate, the orchards and the surroundings, followed by pizza "
        "outdoors among the landscape, music and Festa Major.\n\n"
        "From 7 to 10 pm; booking required."
    ),
    1268: (
        "Festa Major begins with the ringing of bells and the opening firecracker rope by "
        "the Diables de Sant Cugat together with the Trabucaires. This is followed by the "
        "opening procession of Festa Major, with a parade of Sant Cugat's popular and "
        "traditional culture groups.\n\n"
        "Route: avinguda de Cerdanyola (at passeig de Torreblanca), carrer de la Torre, "
        "plaça d'Octavià, carrer de Santiago Rusiñol, plaça dels Quatre Cantons, carrer de "
        "Francesc Moragas, rambla del Celler and plaça de la Vila."
    ),
    1269: (
        "Given by Gemma Puig. Once it ends, the festival bursts into life! The time is "
        "approximate and depends on the arrival of the Festa Major opening procession.\n\n"
        "Meteorologist Gemma Puig will deliver the opening speech of Festa Major de Sant "
        "Cugat. Born in Berga in 1976, she holds a degree in Physical Sciences from the "
        "University of Barcelona and specializes in meteorology. She has been part of "
        "TV3's weather team since 2008 and is one of the best-known faces of weather "
        "reporting in Catalonia.\n\n"
        "A resident of Sant Cugat for 14 years, Puig has taken part in several local "
        "initiatives related to climate education and sustainability. She is also the "
        "author of the book \"Aigua, un recurs vital\" and co-author, with Mònica Usart, "
        "of \"Atrapades en el temps.\" This will be the first time Gemma Puig gives the "
        "opening speech of a Festa Major."
    ),
    1861: (
        "Thursday 25 June schedule: 8.30 pm to 1 am.\n\n"
        "The Festa Major funfair continues on the following days:\n"
        "Friday 26, 5 pm to 2 am\n"
        "Saturday 27, 5 pm to 2 am\n"
        "Sunday 28, 5 pm to 1 am\n\n"
        "From 5 to 7 pm music and intense lighting on the rides will be temporarily "
        "switched off.\n\n"
        "Monday 29, 5 pm to midnight."
    ),
    1278: (
        "Concerts with Slippin Getaway Drivers, Allseks, Dj Martins.\n"
        "Bar service available!\n\n"
        "The 2nd edition of Festa Major al Carrer Hospital is here! From 8.30 pm they'll "
        "once again bring popular culture and joy to the street."
    ),
    1270: (
        "Pop classics from yesterday and today, especially songs that have been sung "
        "and/or written by women, performed by a women's choir with band accompaniment.\n\n"
        "A Festa Major concert.\n"
        "Pop al Cor is a women's choir for women aged 30 and over who share a passion for "
        "pop music. An accessible and joyful choral experience, with a current repertoire "
        "that works on voice, pitch and harmony with quality and energy."
    ),
    1273: (
        "Year after year, the Montgrins select great hits for you to enjoy performed by "
        "our musicians. The best singers and soloists await you on the Festa Major stage!\n\n"
        "In the spring of 1884, a group of musicians led by Pere Rigau formed the cobla "
        "orchestra that would become today's oldest still-active ensemble of its kind. "
        "Throughout its long history, Cobla Orquestra Montgrins has known how to adapt and "
        "renew itself in order to satisfy even the most demanding audiences to this day."
    ),
    1277: (
        "Gospel is voice, rhythm and community. And with Gospel Beat, all of that takes "
        "the shape of a large choir with close to 90 singers, a vibrant repertoire and a "
        "stage energy that invites you to experience the music from within.\n\n"
        "Gospel Beat is a gospel singing project led by David Suarez Llorens, born in 2021 "
        "at La Unió Santcugatenca. They are a choir known for their energy on stage, as "
        "well as for a deep respect for this spiritual style of singing, committed to "
        "people and to music."
    ),
    1276: (
        "Inspired by the Valencian legend \"El Trib Reial,\" in which a group of people is "
        "condemned to dance forever for having ignored a funeral procession, Esbart Sant "
        "Cugat's new production presents dance and celebration as a collective sentence — "
        "an inertia that traps the performers in uninterrupted movement.\n\n"
        "Artistic direction and choreography: Eulàlia Mateu\n"
        "Musical direction: Selma Bruna, with support from Iker Coll\n"
        "Costume design and making: Judith Guardia\n"
        "Production support: Andreu Tarrés\n"
        "Performed by: Esbart Sant Cugat's Dance Company"
    ),
    1275: (
        "A Barcelona band with over 10 years on the scene, blending folk, blues and North "
        "American roots rock with a contemporary sensibility. Their live show offers a "
        "musical journey full of rhythm, nuance and a close connection with the audience."
    ),
    1274: (
        "Perico Sambeat, alto sax. Javier Colina, double bass. Marc Miralta, drums.\n\n"
        "One of the most acclaimed jazz trios on the Spanish scene, bringing together the "
        "exceptional careers of three musicians who converge in a language of their own, "
        "where jazz dialogues with Latin rhythms, flamenco and other musics of the world. "
        "They present \"Tres palabras,\" which includes three original compositions by "
        "Perico Sambeat alongside new readings of pieces by Thelonious Monk and works by "
        "various Latin American composers.\n\n"
        "Enjoy jazz for Festa Major!"
    ),
    1279: (
        "A café cantante for Festa Major: a close, warm and lively space where flamenco "
        "unfolds without artifice, in plain view of everyone.\n\n"
        "Cante: Pere Martinez, Cristina López and Anna Brenes\n"
        "Guitar: Roger Sabartes Rocha, Isabelle Laundenbach, Axequiel Coria\n"
        "Percussion: Álvaro López\n"
        "Bulerías mistress: Aina Núñez\n"
        "Performers: Students of La Tacones and of Aina Núñez\n"
        "Stage direction: Ana Pérez García"
    ),
    1318: (
        "A newly created dance show inspired by the Valencian legend \"El Trib Reial,\" in "
        "which a group of people is condemned to dance forever for having ignored a "
        "funeral procession. The show presents dance as a collective sentence, a movement "
        "that traps the performers within an uninterrupted rhythm.\n\n"
        "Artistic direction and choreography: Eulàlia Mateu\n"
        "Musical direction: Selma Bruna, with support from Iker Coll\n"
        "Costume design and making: Judith Guardia\n"
        "Production support: Andreu Tarrés\n"
        "Performed by: Esbart Sant Cugat's Dance Company"
    ),
    1283: (
        "Pioneers of the tribute-band movement, they are the leading U2 show in our "
        "country.\n\n"
        "Their concerts recreate the great tours of the most important Irish rock band in "
        "history. Miki Fargas's powerful voice, with an uncanny resemblance to Bono's, and "
        "the masterful playing of the rest of the band (Edu Zafra also shares The Edge's "
        "looks), bring back the real U2.\n\n"
        "A heartfelt tribute that manages to move and excite audiences, thanks to an "
        "impressive staging, flawless musicians and anthems that remain a banner for "
        "several generations."
    ),
    1280: (
        "The Montgrins, with their singers and musicians, will get you dancing with a "
        "varied repertoire of great hits from different eras. Shake a leg for Festa Major!\n\n"
        "In the spring of 1884, a group of musicians led by Pere Rigau formed the cobla "
        "orchestra that would become today's oldest still-active ensemble of its kind. "
        "Throughout its long history, Cobla Orquestra Montgrins has known how to adapt and "
        "renew itself in order to satisfy even the most demanding audiences to this day."
    ),
    1282: (
        "Ginestà will perform at Festa Major de Sant Cugat on Thursday 25 June!\n\n"
        "Ginestà have established themselves as one of the essential names in Catalan "
        "pop. Siblings Júlia and Pau Serrasolsas dazzled with \"Vida Meva\" (2024), an "
        "album that earned them two Enderrock Awards and recognition as Catalan Album of "
        "the Year.\n\n"
        "In 2025 they developed the album's imagery further and released the EP \"Només "
        "viure,\" confirming their moment of glory and their ability to move audiences "
        "with a sound world of their own and a unique connection with Catalan audiences.\n\n"
        "In 2026, Ginestà released their new album \"Gira tot igual, però diferent,\" with "
        "which both audiences and promoters have reaffirmed them as one of the most "
        "inspiring, socially committed and beloved acts on the Catalan music scene."
    ),
    1325: (
        "Two friends with disco hearts and pop brains decide one day to mix 80s "
        "synthesizers, Catalan lyrics and party beats. They're the imaginary meeting "
        "point between Daft Punk and Lluís Gavaldà. They're Sunday groove and "
        "melancholy; they're electronic music with a human soul. They're vocoder choirs. "
        "They're \"new wave\" with punch. They're stories that might be yours too."
    ),
    1324: (
        "The city's most beloved karaoke is back. Pick a song, grab the mic and be the "
        "star of Festa Major!\n\n"
        "Live Karaoke Show is a live concert where the audience chooses and sings the "
        "night's repertoire. A list of over 170 songs to choose from, 2 hours of live "
        "show with 7 musicians, a fun and participatory concert with a final medley to "
        "close the party. They play and people sing the songs they love most (in "
        "Catalan, Spanish or English), feeling like part of the show."
    ),
    1326: (
        "The Tyets, one of the headliners of Festa Major de Sant Cugat 2026!\n\n"
        "After becoming an unprecedented phenomenon in recent years, The Tyets remain "
        "unstoppable in 2026, established as one of the country's main draws and "
        "headliners. Their latest album, \"Cafè pels més cafeteros\" (Luup Records, 2025), "
        "has come with a spectacular tour that's been a genuine audience success.\n\n"
        "The Tyets will perform songs already captivating fans, such as their hit "
        "collaboration with Estopa, \"Camila,\" and \"Tàndem,\" one of the songs of the "
        "summer. Once again, their unmistakable \"tieta\" universe promises to keep "
        "growing and getting the whole country dancing."
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
