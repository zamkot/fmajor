# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_en for batch 9 of the full-catalog English translation pass (events 161-180 of 190)."""
import json

TRANSLATIONS = {
    1419: "Oriental dance showcase with the participation of students and guest dancers.",
    1421: "Havaneres, tavern songs and burnt rum",
    1423: (
        "With cia. Kamchàtka. A traveling street show that \"dances\" above all borders "
        "and within our shared humanity.\n\n"
        "Eight characters lost in a city, each with their own suitcase and memories. "
        "Who are they? What are they doing here? Are they travelers or migrants? "
        "Naive, curious and emotionally exposed, they don't know our rules or our way "
        "of life. How will we treat them? Will we build a future with the Kamchàtka, "
        "or will we reject them?"
    ),
    1422: (
        "With Planeta Trampolí\n\n"
        "A fresh, close and intimate trampoline show, blending classic circus with "
        "urban cultures through dance, music and the art of turntablism (vinyl "
        "scratching). A journey to the past full of humor, poetry, innocence and "
        "rhythm."
    ),
    1420: "With Cobla Marinada",
    1424: (
        "Concertmaster: Gerard Claret. Direction: Albert Gumí\n\n"
        "A symphonic concert in which the orchestra presents the program \"Exotismes "
        "Simfònics,\" featuring popular composers. The concert has an inclusive side "
        "and includes the participation of Catalonia Fundació Creactiva members in some "
        "pieces."
    ),
    1425: "Showcase of urban dance choreographies that the students have worked on at the school throughout the year.",
    2131: "Three female voices will perform Cuban and Catalan havaneres, accompanied by guitar and percussion.",
    2133: (
        "An intellectual folk group honoring the legacy of \"the Star\" Quimi Portet and "
        "his work with Los Burros and El Último de la Fila. They also play original "
        "songs to avoid being called a \"tribute\" act."
    ),
    1380: (
        "Set in Han dynasty China, the plot follows the adventures of the slave girl "
        "Ping and the ancient dragon Long Danzi. Dragons, once friends and wise allies "
        "of humans, have long been hunted and caged. Ping helps Long Danzi, the last "
        "living dragon, escape, and joins him to find the last remaining dragon egg, "
        "stolen by an evil sorcerer. Pursued by the Emperor's armies, this odd pair "
        "embarks on a thrilling journey across China. Inevitably, both will learn to "
        "trust each other to defeat their enemies and ensure the survival of the dragon "
        "lineage.\n\n"
        "Recommended age: for all ages\n\n"
        "Runtime: 90 min."
    ),
    1430: (
        "Good morning, it's eight o'clock. The commuter rail isn't working. The far "
        "right is on the rise. The use of Catalan is in decline. An undercover police "
        "officer is uncovered at a neighborhood community center. There are 10,000 "
        "festival tourists at the Fòrum. And did they say a new brunch place just "
        "opened?! Today is, simply, just another day in Catalonia.\n\n"
        "In this Catalonia where everything's going downhill, Fetus set out to document "
        "the most local everyday disasters in the style of the old ballad-singers. "
        "Following in the footsteps of master Arnella, who has lit their way so well, "
        "and sitting at the point where the legacy of The Clash meets that of La "
        "Trinca, they present at Festa Major \"Romancer tartera,\" thirteen songs like "
        "thirteen stones."
    ),
    1429: (
        "A blues rock classics band. They perform pieces like \"The Thrill Is Gone,\" "
        "\"Further On Up the Road\" and \"Sweet Home Chicago,\" among others. With guitar "
        "front and center and a powerful, characterful voice, they cover Clapton, "
        "Freddy King and Gary Moore with great skill. With a forceful rhythm section, "
        "they range from Chicago to Texas blues, by way of country and rock'n'roll.\n\n"
        "Toni Marimon: Vocals, guitar. Oriol Saltor: Guitar. Arnau Pàmies: Bass. Joan "
        "Llopis: Drums"
    ),
    1434: (
        "Opening firecracker rope and bell ringing with gralla and drum players and "
        "trabucaires from the city\n\n"
        "Route: pl. Octavià, c. de la Torre, c. de la Creu, c. Montserrat, c. Orient, "
        "pg. Francesc Macià, c. Castellví, c. Indústria, c. Sant Esteve, pl. Pep "
        "Ventura, c. Sallés, pl. Sant Pere, c. Major, pl. Octavià"
    ),
    1436: (
        "Discover pickleball, a dynamic sport accessible to everyone! You'll be able to "
        "enjoy a hands-on introductory session.\n\n"
        "Prior registration required at omet.santcugat.cat (limited places)\n\n"
        "Ages 18 and up"
    ),
    1435: "Botifarra sausage and bread with tomato",
    1438: (
        "The drought is over and the Water Festival is back! You'll find water "
        "inflatables, slides, water games, slip n' slides and a giant 40 m slide to "
        "cool off, play and have a blast! Don't forget your swimsuit, flip-flops and "
        "sunscreen!"
    ),
    1437: (
        "A festive procession led by children and young people, presided over by the "
        "city's Children's Council and Youth Council (ages 12-17)\n\n"
        "Route: pl. Doctor Galtés (in front of the Parish Retirement Home), c. Santa "
        "Maria, c. Santiago Rusiñol, pl. Octavià"
    ),
    1439: "Vermouth with the Escola de Música Tradicional de Sant Cugat and the musicians of the Seguici Festiu",
    1293: (
        "From 5 to 7 pm music and intense lighting on the rides will be temporarily "
        "switched off"
    ),
    1440: (
        "Sant Pere Procession, June 29th\n"
        "Route: pl. de la Vila, rbla. del Celler, c. Francesc Moragas, c. Rius i "
        "Taulet, c. Enric Granados, pl. Sant Pere, c. Major, pl. Octavià and the "
        "Monastery's small gallery"
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
