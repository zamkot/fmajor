# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Batch 1 of remaining description_pl translations (15 events)."""
import json

TRANSLATIONS = {
    1296: (
        "Z udziałem combo Jazzin’ Time oraz młodzieży z niepełnosprawnością intelektualną."
    ),
    1294: (
        "Otwarte dla wszystkich mieszkańców, niezależnie od ich kondycji – dostępne i pełne "
        "respektu dla odmienności. Przestrzeń eksperymentu i wspólnego tworzenia, z tematem "
        "obchodów Festa Major jako wspólnym motywem.\n\n"
        "Windown narodził się z inicjatywy Andrésa Moctezumy, zainspirowanej relacją "
        "Gustiego z jego synem z zespołem Downa, przekształcając się w ruch sztuki i "
        "inkluzji. Od 2014 roku prowadzą inkluzywną przestrzeń twórczą pod kierunkiem Inge "
        "Nouws, Ismy Guzmána i Gustiego Rosemffeta. Warsztat opiera się na „estetyce "
        "relacyjnej”, która sprzyja interakcji między uczestnikami oraz swobodnej, "
        "spontanicznej twórczości artystycznej."
    ),
    1302: (
        "Nadchodzi 2. edycja FM League! Jeśli masz od 10 do 14 lat, stwórz zespół i ciesz "
        "się swoim ulubionym sportem w tym turnieju z 15-minutowymi meczami piłki nożnej "
        "3×3, piłki ręcznej 4×4, koszykówki 3×3 i siatkówki 4×4.\n\n"
        "Wymagana wcześniejsza rejestracja na omet.santcugat.cat"
    ),
    1924: (
        "Znajdziesz tu namiot, w którym przygotujesz swój transparent na korowód Batucada "
        "Orgullosa."
    ),
    1305: (
        "Otwarta sesja treningu całego ciała z muzyką, łącząca interwały pracy kardio z "
        "treningiem siłowym. To dynamiczna i dostępna dla każdego aktywność, proponująca "
        "ogólny trening ciała poprzez interwały o różnej intensywności, dostosowane tak, by "
        "każdy uczestnik mógł zachować własne tempo.\n\n"
        "Sportowa propozycja w ramach Festa Major de Sant Cugat, stworzona, by poruszać "
        "ciałem, poprawić formę fizyczną i cieszyć się aktywną sesją na świeżym powietrzu.\n\n"
        "Udział otwarty dla wszystkich (bez wcześniejszej rejestracji)"
    ),
    1304: (
        "Turniej petanki wraca do Sant Cugat już po dwunasty raz w ramach Festa Major – "
        "zawody otwarte dla wszystkich, by cieszyć się tym tradycyjnym sportem na świeżym "
        "powietrzu.\n\n"
        "Petanka to sport precyzyjny, w który gra się zespołowo lub indywidualnie, a polega "
        "on na rzucaniu metalowymi kulami z myślą o ustawieniu ich możliwie najbliżej małej "
        "kulki zwanej „boliche”."
    ),
    1303: (
        "Zbuduj swój pojazd-cudak z przyjaciółmi, rodziną albo z kim chcesz i przygotuj się "
        "na najbardziej spektakularny zjazd roku!\n\n"
        "Zapisy: androminesfmsantcugat@gmail.com do 25 czerwca"
    ),
    1308: (
        "19.30 Spektakl „El viatge. Sortir del centre” w wykonaniu Associació Mengue "
        "Guinée. Przedstawienie ukazuje i kwestionuje globalne nierówności poprzez dialog "
        "między artystycznymi światami: różne rytmy i tańce z Gwinei Konakry spotykają się "
        "z tradycyjnymi tańcami katalońskimi, asturyjskimi i argentyńskimi.\n\n"
        "20.15 Rozmowa prowadzona przez Associació Joves Africans de Catalunya. Dialog "
        "między prowadzącym i muzykami, by bliżej poznać ich instrumenty, korzenie i "
        "kulturę oraz zbliżyć do siebie różne kultury.\n\n"
        "21.00 Koncert Kamben, zespołu złożonego z afrykańskich artystów z Senegalu i "
        "Gwinei Konakry. Tradycyjna muzyka Afryki Zachodniej związana z Imperium Mandinka "
        "oraz muzyka afro-mandinka."
    ),
    1307: (
        "Els Pocavergonya to inkluzywna grupa teatralna prowadzona przez Marię Vancells, "
        "działająca w ramach kwartalnych warsztatów Casa de Cultura. Każdy piątek "
        "spotykamy się i pracujemy razem, odkrywając poprzez zabawę i muzykę nasze "
        "talenty, dając przestrzeń różnicom, by docenić to, co nas łączy. Przyjdź zobaczyć "
        "nas i baw się z nami!"
    ),
    1306: (
        "Korowód z grupą perkusyjną Karabassà z okazji Dnia Orgull LGBTI+.\n"
        "Muzyczna i protestacyjna propozycja, która wypełnia ulice rytmem, energią i "
        "celebracją różnorodności.\n\n"
        "Trasa: plaça de Lluís Millet, carrer de Valldoreix, carrer de Sant Antoni, plaça "
        "de Barcelona."
    ),
    1312: (
        "Backline Choir to chór złożony z bardzo różnorodnych osób, które łączy chęć "
        "śpiewania i wspólnego spędzania dobrego czasu. Powstał w 2014 roku, a obecnie "
        "prowadzi go Aleix Losa. Śpiewają zawsze a cappella, bez instrumentów, dowolne "
        "utwory muzyki nowoczesnej, które im się podobają i które – ich zdaniem – "
        "zachwycą również słuchaczy."
    ),
    1311: (
        "20.00 Manifest z okazji Dnia Orgull LGBTI+\n\n"
        "20.15 Bingo Musical „Special Pride” z @bingomusical.\n"
        "Najlepsze z bingo i karaoke w jednym. Najlepsze piosenki do tańca, śpiewu i "
        "celebrowania dnia wyzwolenia seksualnego."
    ),
    1309: (
        "Z udziałem Radicel·la\n\n"
        "„Horabaixa” to ta chwila dnia, gdy słońce zachodzi a codzienna rutyna "
        "zatrzymuje się – czas, który zaprasza do ponownego spotkania i dzielenia się "
        "czasem bez pośpiechu. Podróżujemy przez tańce ludowe, które każdy czuje jako "
        "swoje, odkrywając ruchy, które na początku mogą wydawać się obce, lecz z czasem "
        "każdy czyni je własnymi."
    ),
    1315: (
        "Malabarada i wierszowane okrzyki dla dzieci dają sygnał do startu dziecięcego i "
        "młodzieżowego correfoc Festa Major de Sant Cugat.\n\n"
        "Najmłodsi będą mogli wziąć udział w świątecznym, otwartym na uczestnictwo "
        "wydarzeniu opartym na kulturze ludowej, z odczytaniem dziecięcych wierszowanych "
        "okrzyków i charakterystyczną atmosferą obchodów organizowanych przez Diables de "
        "Sant Cugat."
    ),
    1945: (
        "Música al Xiringuit-U gości jazzową propozycję Andrei Calderón & Jazzin’ Time – "
        "koncert w ramach muzycznego programu Festa Major.\n\n"
        "Jazzin’ Time to zespół skoncentrowany na języku jazzu współczesnego, z otwartą, "
        "elastyczną interpretacją opartą na improwizacji i muzycznym dialogu między "
        "wykonawcami. Tym razem dzielą scenę z wokalistką i interpretatorką Andreą "
        "Calderón, wnosząc świeżą, elegancką propozycję pełną niuansów.\n\n"
        "Sesja stworzona, by cieszyć się jazzem na żywo w bliskiej, plenerowej atmosferze, "
        "w świątecznym nastroju Festa Major."
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
