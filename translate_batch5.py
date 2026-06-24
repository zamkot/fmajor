# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Batch 5 of remaining description_pl translations (15 events)."""
import json

SBANDIERATORI = (
    "Alba, miasto w włoskim Piemoncie, i Sant Cugat są miastami partnerskimi od 2007 "
    "roku. W tym roku, by wzmocnić te więzi, zaproszono do udziału w Festa Major ich "
    "Compagnia Sbandieratori e Musici Borgo San Lorenzo.\n\n"
    "Będą towarzyszyć różnym wydarzeniom naszej kultury ludowej i pomalują na "
    "niebiesko-biało różne place swoim charakterystycznym pokazem flag, które "
    "powiewają i są wyrzucane w niebo. Założeni w 1984 roku, Sbandieratori Borgo San "
    "Lorenzo starają się utrzymać przy życiu tę tradycję swojej ziemi, ucząc i "
    "prezentując sztukę powiewania flagami. Są członkami Włoskiej Ligi Powiewaczy "
    "Flagami i co roku biorą udział w swoich Mistrzostwach Narodowych z doskonałymi "
    "wynikami."
)

TRANSLATIONS = {
    1365: (
        "Z Jazzduopop. Dziesięć winnic i ponad 40 win z różnych D.O. do degustacji!\n\n"
        "Przedsprzedaż w Vins Noè i na tastos.vinsnoe.com od 15 czerwca\n"
        "Sprzedaż wejściówek godzinę przed startem, w Celler Modernista\n"
        "Ograniczona liczba miejsc\n\n"
        "Na terenie obiektu nie wolno palić, wnosić jedzenia ani zwierząt domowych. Pij "
        "z umiarem."
    ),
    1364: "Festiwal tańców ulicznych w wykonaniu uczniów Escola Sant Cugat.",
    1354: (
        "Wydarzenie sportowe otwarte dla wszystkich, bez wcześniejszej rejestracji.\n\n"
        "Śledźcie ich w sieciach: @jaleo.santcugat"
    ),
    1367: (
        "Z grupami tańców tradycyjnych Caporales San Simón, Morenada Sant Cugat, "
        "Morenada Central Oruro i Morenada Unión Boliviana\n\n"
        "Trasa: pl. Lluís Millet, c. Villà, c. Valldoreix, c. Sant Antoni, c. Xerric, c. "
        "Sant Bonaventura, c. Valldoreix, pl. Doctor Caltés, c. Martorell, av. Lluís "
        "Companys, c. Rosselló, c. Valldoreix, pl. Lluís Millet."
    ),
    1369: "Club Rugby Sant Cugat",
    1368: (
        "Okazja, by cieszyć się żywym koncertem. Eksplozja energii, emocji i głosów, "
        "która dotrze do twojego serca, z muzyką, która zerwie cię z krzesła."
    ),
    1370: "Widowisko taneczne szkoły Color Dansa Carol Morgado",
    1348: (
        "Światowa premiera symfonicznej wersji „Paga-li, Joan” w aranżacji "
        "pochodzącego z Sant Cugat Biela Vouillamoza.\n\n"
        "Kierownictwo: Xavier Pagès-Corella\n\n"
        "Koncert na rzecz Càritas Sant Cugat"
    ),
    1343: SBANDIERATORI,
    1375: (
        "Wybuchowy skład, który przywraca żywego ducha wielkich nocy swingu i lindy "
        "hopu. Z repertuarem pełnym rytmu, elegancji i zaraźliwej energii, zapraszają "
        "publiczność do podróży do jazzowych klubów lat trzydziestych i czterdziestych, "
        "gdzie muzyka była synonimem tańca, improwizacji i celebracji.\n\n"
        "Zespół zrzesza niektórych z najwybitniejszych muzyków katalońskiej scenie "
        "jazzowej: Oriol Vallès – trąbka, Lluc Casares – saksofon tenorowy, Alba "
        "Pujals – puzon, Jöel González – fortepian, Camil Arcarazo – kontrabas i Xavi "
        "Hinojosa – bębny.\n\n"
        "Współpraca: Xarxa de Centres Culturals"
    ),
    1374: (
        "Pokaz pełen energii i entuzjazmu wszystkich uczniów. Celebracja otwarta dla "
        "wszystkich, by cieszyć się sztuką tańca i świątecznym duchem Festa Major."
    ),
    2063: (
        "Prezentacja w wykonaniu reżyserki filmu, pochodzącej z Sant Cugat Judith "
        "Colell.\n\n"
        "W 1943 roku, w trakcie II wojny światowej, dyktator Franco zablokował "
        "przejście przez Pireneje Żydom uciekającym do Hiszpanii przed nazistowskimi "
        "represjami. Celnik z republikańską przeszłością postanawia nie wykonywać "
        "rozkazów i pomóc w ucieczce tak wielu osobom, jak zdoła. Tym aktem oporu on i "
        "jego żona będą musieli stawić czoła także blizn pozostawionym przez niedawną "
        "wojnę domową.\n\n"
        "Czas trwania: 101 min.\nWspółpraca: El Cinèfil"
    ),
    2059: (
        "Vintage pop Sergiego Carósa, który odniósł sukces w międzynarodowym radiu i w "
        "słynnym Cavern w Liverpoolu. Wystąpi w składzie kwartetu (Sergi Carós, Nau "
        "León, Miguel Alberte, Roberto Olori) i przypomni utwory z „Popteràpia” oraz "
        "klasyki popu lat 60."
    ),
    1379: (
        "Po 8 latach długiej nieobecności, najbardziej rockowe jaszczurki barcelońskiej "
        "scenie wracają do gry. Po 5 wydanych płytach i ponad 800 koncertach na koncie, "
        "mając za sobą wspólną scenę z Whitesnake, M-Clan, Fito & Fitipaldis czy Jarabe "
        "de Palo, powrót Sol Lagarto nie ma na celu niczego nikomu udowadniać, lecz "
        "uhonorować samych siebie i przypomnieć, że choć zmieniają skórę, są stworzeni "
        "do rocka i scen.\n\n"
        "W 2025 roku wydali trzy piosenki: „Siempre”, „Con sólo una mirada” i „Fuego”, "
        "zapowiadając nowy etap twórczy pełen energii i autentyczności. Niech żyją "
        "długo."
    ),
    1378: (
        "Zwiedzanie z przewodnikiem, by odkryć krużganek klasztoru w świetle świec, "
        "poznając sposób oświetlenia w średniowieczu oraz symbolikę światła nocą.\n\n"
        "Wymagana rejestracja na https://museu.santcugat.cat/agenda/"
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
