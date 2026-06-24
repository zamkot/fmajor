# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Batch 2 of remaining description_pl translations (15 events)."""
import json

TRANSLATIONS = {
    1322: (
        "Olivia jest 12-letnią dziewczynką, której życie się rozsypuje, gdy jej rodzinę "
        "eksmitują i musi przeprowadzić się z matką Íngrid oraz młodszym bratem Timem do "
        "mieszkania na przedmieściach. Íngrid zapada w depresję, więc Olivia musi opiekować "
        "się Timem i sobą samą, stawiając czoła własnemu emocjonalnemu „trzęsieniu ziemi”. "
        "Wtedy tworzy fantazję: wszystko, co przeżywa, nie jest prawdziwe, lecz to kręcenie "
        "filmu. Olivia znajdzie nową „rodzinę”, która pomoże jej odbudować życie i nauczyć "
        "się przetrwać przeciwności.\n\n"
        "Wiek: dla wszystkich\nCzas trwania: 71 min.\n\n"
        "Współpraca: El Cinèfil"
    ),
    1321: (
        "Wschodzący zespół łączący andaluzyjskie i katalońskie korzenie, prowadzony przez "
        "gitarzystę Juana Slandsa i z magnetycznym głosem Ángeli Quiralte. Ich brzmienie "
        "łączy funk i rock z nutami jazzu i popu, prowadzone przez zaraźliwy groove."
    ),
    1319: (
        "Koncert pełen energii z klasycznymi i współczesnymi piosenkami gospel, z zespołem "
        "muzyków na żywo.\n\n"
        "Cor de Gòspel Sant Cugat został założony w 2008 roku z inicjatywy Erwyna "
        "Seerutona i grupy uczestników jednego z jego warsztatów. Chór składa się z "
        "dziesiątek entuzjastycznych wokalistów, tworzących ambitny projekt muzycznego i "
        "artystycznego rozwoju, będący przykładem do naśladowania.\n\n"
        "Chór organizuje koncerty o charakterze przede wszystkim charytatywnym, na rzecz "
        "projektów organizacji działających społecznie, i przez wszystkie te lata udało im "
        "się zebrać znaczne środki dla tych organizacji."
    ),
    1317: (
        "Alba Careta – trąbka i wokal. Lucas Martínez – saksofon tenorowy. Roger "
        "Santacana – fortepian. Giuseppe Campisi – kontrabas. Jordi Pallarés – bębny\n\n"
        "Alba Careta to jedna z najwybitniejszych wykonawczyń i kompozytorek jazzowych w "
        "Hiszpanii oraz punkt odniesienia europejskiego jazzu. Prezentuje album „Panical”, "
        "który zagłębia się w ziemię jako źródło inspiracji, prowadzony siłą korzeni i "
        "kobiecymi wzorcami, które wyznaczają rytm tej pracy. To manifest oporu i "
        "nieujarzmionej piękności, zainspirowany silnymi, zbuntowanymi kobietami, wiernymi "
        "sobie samym."
    ),
    2487: (
        "Widowisko taneczne Festa Major z udziałem Esbart Mediterrània i muzycznym "
        "akompaniamentem Cobla Marinada, pod kierunkiem mistrza Daniego Gasulli i Porty.\n\n"
        "Program: Tańce ludowe i choreografie Salvadora Mel·lo, Alberta Sansa, Davida "
        "Martíneza, Laii Travé, Mercè Andrés, Marty Manyoses i Davida Gila.\n"
        "Śpiew: Adrià Garcia Alegre\n"
        "Kierownictwo: David Gil, Esther Madrona, Anna Mayol i Francesc Picornell.\n"
        "Organizacja: Esbart Mediterrània"
    ),
    1323: (
        "Rock, energia, zabawa, emocje i muzyczna rapsodia – to wnosi Indubio na scenę. "
        "Występ na żywo pełen własnej muzyki, mocnych kawałków, ballad i kilku ikonicznych "
        "coverów, by skakać, tańczyć i śpiewać razem z tymi, którzy spędzą z nimi tę noc."
    ),
    1387: (
        "Są jedyne, niepowtarzalne, nieporównywalne… to Pubilles Ninja! Zespół folk "
        "rockowy z dużą dawką humoru."
    ),
    1388: "Wierszowane okrzyki Festa Major w wykonaniu Diables de Sant Cugat.",
    1389: (
        "Coco, w 100% kobiecy zespół coverowy, który robi furorę! Prawdziwy show, w "
        "którym zaserwują wam koktail coverów z różnych epok, w formacie „medley” i z "
        "dużym wdziękiem.\n\n"
        "Coco stał się punktem odniesienia dla artystycznego wzmocnienia kobiet, choć bez "
        "chęci robienia z tego sloganu, z czterema charyzmatycznymi członkiniami i "
        "umiejętnością łączenia piosenek, które od pierwszej minuty głęboko poruszają "
        "publiczność. Uwaga jednak na ich koncerty, bo gwarantują chrypkę, zakwasy, "
        "euforię i ekstremalne szczęście!"
    ),
    2077: "Muzyka swingowa i tańce\n\nWspółpraca: Xarxa de Centres Culturals",
    1392: (
        "Doświadczona animatorka barcelońskiej scenie na wielu frontach. Na koniec lat "
        "dziewięćdziesiątych założyła w Barcelonie klub Magic in the Air, który stał się "
        "niezaprzeczalnym punktem odniesienia kultury lat sześćdziesiątych, zwłaszcza w "
        "jej popowo-rockowym wydaniu, nie zapominając przy tym o czarnej muzyce i rytmach "
        "groove."
    ),
    1390: (
        "Tapeo Sound System obchodzi w 2026 roku swoje 15-lecie specjalną trasą "
        "koncertową. Prezentują najpełniejszy spektakl, jaki do tej pory stworzyli, z "
        "unikalnym, pełnym energii repertuarem coverów, który łączy pokolenia. Z "
        "dopracowaną w każdym szczególe inscenizacją oraz charakterystycznym dla nich "
        "poczuciem humoru i bliskością, wciąż łączą się z publicznością, która z roku na "
        "rok rośnie."
    ),
    1393: (
        "DJ stawiający na zróżnicowane i dynamiczne sety, łączące aktualne hity z "
        "kultowymi piosenkami, które każdy w końcu śpiewa. Z bliskim i naturalnym stylem, "
        "umie czytać atmosferę i dopasowywać muzykę do każdej chwili, by parkiet nie "
        "tracił rytmu. Jego sety mieszają zabawę, nostalgię i energię, łącząc się z bardzo "
        "różną publicznością, nigdy nie gubiąc nitki nocy. W tym roku przyjeżdża na Festa "
        "Major w nocnym terminie, adaptując format – by tańczyć, śpiewać i bawić się do "
        "samego końca."
    ),
    1333: (
        "La Botiga al carrer wraca na Festa Major de Sant Cugat, zmieniając ulice miasta "
        "w wielką witrynę lokalnego handlu. W zgodzie z początkiem letnich wyprzedaży, "
        "uczestniczące sklepy wychodzą na ulicę, by zaprezentować mieszkańcom swoje "
        "produkty i usługi.\n\n"
        "Inicjatywa ta stała się jedną z najbardziej tradycyjnych i angażujących "
        "aktywności Festa Major, przyciągając tysiące osób, które wykorzystują ten dzień, "
        "by się przejść, robić zakupy i odkrywać ofertę lokalnych sklepów.\n\n"
        "Oprócz promocji i specjalnych rabatów, niektóre sklepy uzupełniają swój udział "
        "warsztatami i aktywnościami otwartymi dla publiczności, przyczyniając się do "
        "tworzenia świątecznej i ożywionej atmosfery w centrum miasta."
    ),
    1332: (
        "ZEM La Guinardera gości Mistrzostwa Hiszpanii w Szermierce Weteranów – zawody "
        "krajowe, które gromadzą sportowców z różnych kategorii wiekowych (+30, +40, +50, "
        "+60 i +70) w kategorii męskiej i kobiecej.\n\n"
        "Mistrzostwa obejmują indywidualne zawody w trzech rodzajach broni szermierczej: "
        "florecie, szpadzie i szabli."
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
