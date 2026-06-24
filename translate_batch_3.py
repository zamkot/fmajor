# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_pl for batch 1-3 of the full-catalog translation pass (events 1-39 of 175)."""
import json

TRANSLATIONS = {
    1284: "Sesje pełne energii i radości, które łączą pop, przeboje z 2010 roku i starszy reggaeton.",
    2411: (
        "Mecànic Pizza zaprasza do obchodu Festa Major z okazji Pizza Week!\n\n"
        "Uciekamy w naturę na kolację do Masia Can Domènech u podnóża Collserola.\n"
        "Przewodnia wizyta po posiadłości, ogrodach i okolicy, następnie pizza na świeżym powietrzu w otoczeniu krajobrazu, muzyki i Festa Major.\n\n"
        "Od 19 do 22; rezerwacja obowiązkowa."
    ),
    1268: (
        "Rozpoczyna się Festa Major dzwonieniem dzwonów i racą początkową w wykonaniu Diables de Sant Cugat wspólnie z Trabucaires. "
        "Następnie procesja otwarcia Festa Major z przemarszem przedstawicieli kultury ludowej i tradycyjnej Sant Cugat.\n\n"
        "Trasa: avinguda de Cerdanyola (na wysokości passeig de Torreblanca), carrer de la Torre, plaça d'Octavià, "
        "carrer de Santiago Rusiñol, plaça dels Quatre Cantons, carrer de Francesc Moragas, rambla del Celler i plaça de la Vila."
    ),
    1269: (
        "Przemówienie wygłosi Gemma Puig. Po jego zakończeniu — wybuch festynu! Godzina jest orientacyjna i zależy od przybycia "
        "korowodu otwierającego Festa Major.\n\n"
        "Meteorolożka Gemma Puig będzie odpowiedzialna za wygłoszenie przemówienia inauguracyjnego Festa Major de Sant Cugat. "
        "Urodzona w Berga w 1976 roku, jest absolwentką nauk fizycznych na Uniwersytecie Barcelońskim i specjalizuje się w meteorologii. "
        "Od 2008 roku jest częścią zespołu prognoz pogody TV3 i jedną z najbardziej znanych twarzy informacji meteorologicznej w Katalonii.\n\n"
        "Mieszkająca w Sant Cugat od 14 lat, Puig brała udział w licznych lokalnych inicjatywach związanych z edukacją klimatyczną "
        "i zrównoważonym rozwojem. Jest również autorką książki „Aigua, un recurs vital” oraz współautorką, wraz z Mònicą Usart, "
        "książki „Atrapades en el temps”. Będzie to pierwszy raz, gdy Gemma Puig wygłosi przemówienie inauguracyjne festynu."
    ),
    1861: (
        "Czwartek, 25 czerwca: od 20.30 do 01.00\n\n"
        "Jarmark Festa Major trwa w kolejne dni:\n"
        "Piątek 26, od 17 do 02\n"
        "Sobota 27, od 17 do 02\n"
        "Niedziela 28, od 17 do 01\n\n"
        "Od 17 do 19 muzyka i intensywne światła na atrakcjach zostaną tymczasowo wyłączone.\n\n"
        "Poniedziałek 29, od 17 do 00"
    ),
    1278: (
        "Koncerty z Slippin Getaway Drivers, Allseks, Dj Martins.\n"
        "Dostępny serwis barowy!\n\n"
        "2. edycja Festa Major al Carrer Hospital to rzeczywistość! Od godziny 20.30 znów wniosą kulturę ludową i radość na ulicę."
    ),
    1270: (
        "Klasyki popu z wczoraj i dzisiaj, szczególnie piosenki śpiewane i/lub skomponowane przez kobiety, w wersji chóralnej "
        "kobiecej z towarzyszeniem zespołu.\n\n"
        "Koncert Festa Major.\n"
        "Pop al Cor to chór żeński dla kobiet od 30 lat wzwyż, które łączy pasja do muzyki pop. Dostępne i radosne doświadczenie "
        "chóralne, z aktualnym repertuarem, w którym pracuje się nad głosem, intonacją i harmonią, z dbałością o jakość i energię."
    ),
    1273: (
        "Co roku Montgrins wybiera dla Was wielkie przeboje, abyście mogli się nimi cieszyć w wykonaniu naszych artystów. "
        "Najlepsi śpiewacy i soliści czekają na Was na scenie Festa Major!\n\n"
        "Wiosną 1884 roku grupa muzyków pod wodzą Pere Rigaua utworzyła cobla-orquestra, która stała się obecnie najstarszą "
        "wciąż działającą formacją tego typu. Przez całą swoją długą historię Cobla Orquestra Montgrins umiała się dostosowywać "
        "i odnawiać, by do dziś satysfakcjonować najbardziej wymagającą publiczność."
    ),
    1277: (
        "Gospel to głos, rytm i wspólnota. A wraz z Gospel Beat wszystko to przybiera formę wielkiego chóru liczącego blisko "
        "90 śpiewaków, z porywającym repertuarem i sceniczną energią, która zaprasza do przeżywania muzyki od wewnątrz.\n\n"
        "Gospel Beat to projekt śpiewu gospel prowadzony przez Davida Suareza Llorensa, który powstał w 2021 roku w La Unió "
        "Santcugatenca. To chór wyróżniający się energią na scenie oraz głębokim szacunkiem dla tego duchowego śpiewu, "
        "zaangażowanego w ludzi i muzykę."
    ),
    1276: (
        "Inspirowany walenckiej legendą „El Trib Reial”, w której grupa ludzi zostaje skazana na wieczne tańczenie za "
        "zignorowanie pochodu pogrzebowego, nowy spektakl Esbart Sant Cugat ukazuje taniec i zabawę jako zbiorową karę — "
        "bezwładność, która uwięzia tancerzy w nieprzerwanym ruchu.\n\n"
        "Reżyseria artystyczna i choreografia: Eulàlia Mateu\n"
        "Reżyseria muzyczna: Selma Bruna ze wsparciem Ikera Colla\n"
        "Projekt i wykonanie kostiumów: Judith Guardia\n"
        "Wsparcie produkcji: Andreu Tarrés\n"
        "Wykonanie: Cos de Dansa de l'Esbart Sant Cugat"
    ),
    1275: (
        "Barcelońska kapela z ponad 10-letnim stażem, łącząca folk, blues i amerykański roots rock ze współczesną "
        "wrażliwością. Ich koncerty na żywo to muzyczna podróż pełna rytmu, niuansów i bliskiego kontaktu z publicznością."
    ),
    1274: (
        "Perico Sambeat, saksofon altowy. Javier Colina, kontrabas. Marc Miralta, perkusja.\n\n"
        "Jedno z najbardziej uznanych trio jazzowych na hiszpańskiej scenie, łączące wybitne dokonania trzech muzyków, "
        "którzy zbiegają się we własnym języku muzycznym, w którym jazz prowadzi dialog z rytmami latynoskimi, flamenco "
        "i innymi muzykami świata. Prezentują „Tres palabras”, na który składają się trzy oryginalne kompozycje Perico "
        "Sambeata wraz z nowymi odczytaniami utworów Theloniousa Monka i dzieł różnych autorów latynoamerykańskich.\n\n"
        "Ciesz się jazzem na Festa Major!"
    ),
    1279: (
        "Café cantante z okazji Festa Major: bliska, ciepła i żywa przestrzeń, w której flamenco rozbrzmiewa bez sztuczności, "
        "na oczach wszystkich.\n\n"
        "Śpiew: Pere Martinez, Cristina López i Anna Brenes\n"
        "Gitara: Roger Sabartes Rocha, Isabelle Laundenbach, Axequiel Coria\n"
        "Perkusja: Álvaro López\n"
        "Mistrzyni bulerías: Aina Núñez\n"
        "Wykonawcy: uczniowie La Tacones i Ainy Núñez\n"
        "Reżyseria sceniczna: Ana Pérez García"
    ),
    1318: (
        "Nowy spektakl taneczny inspirowany walenckiej legendą „El Trib Reial”, w której grupa ludzi zostaje skazana na "
        "wieczne tańczenie za zignorowanie pochodu pogrzebowego. Spektakl ukazuje taniec jako zbiorową karę — ruch, który "
        "uwięzia tancerzy w nieprzerwanym rytmie.\n\n"
        "Reżyseria artystyczna i choreografia: Eulàlia Mateu\n"
        "Reżyseria muzyczna: Selma Bruna ze wsparciem Ikera Colla\n"
        "Projekt i wykonanie kostiumów: Judith Guardia\n"
        "Wsparcie produkcji: Andreu Tarrés\n"
        "Wykonanie: Cos de Dansa de l'Esbart Sant Cugat"
    ),
    1283: (
        "Pionierzy ruchu zespołów tworzących hołd swoim idolom, są najważniejszym show U2 w naszym kraju.\n\n"
        "Ich koncerty przywołują wielkie trasy najważniejszego irlandzkiego zespołu w historii rocka. Potężny głos Mikiego "
        "Fargasa, niezwykle przypominający głos Bono, oraz mistrzowskie wykonanie pozostałych członków zespołu (sam Edu "
        "Zafra ma podobną fizjonomię do The Edge) przywołują wspomnienia autentycznego U2.\n\n"
        "Hołd zrobiony z sercem, który zachwyca i wzrusza publiczność dzięki imponującej inscenizacji, bezbłędnym muzykom "
        "i hymnom, które są sztandarem wielu pokoleń."
    ),
    1280: (
        "Montgrins, ze swoimi śpiewakami i muzykami, sprawi, że zatańczycie do upadłego przy bardzo zróżnicowanym "
        "repertuarze wielkich przebojów z różnych epok. Ruszcie się na Festa Major!\n\n"
        "Wiosną 1884 roku grupa muzyków pod wodzą Pere Rigaua utworzyła cobla-orquestra, która stała się obecnie najstarszą "
        "wciąż działającą formacją tego typu. Przez całą swoją długą historię Cobla Orquestra Montgrins umiała się dostosowywać "
        "i odnawiać, by do dziś satysfakcjonować najbardziej wymagającą publiczność."
    ),
    1282: (
        "Ginestà wystąpi na Festa Major de Sant Cugat w czwartek, 25 czerwca!\n\n"
        "Ginestà utrwalił się jako jedna z niezbędnych grup katalońskiego popu. Rodzeństwo Júlia i Pau Serrasolsas "
        "zachwyciło płytą „Vida Meva” (2024), która przyniosła im dwie nagrody Premis Enderrock i tytuł Katalońskiej Płyty Roku.\n\n"
        "W 2025 roku rozwinęli świat tej płyty i wydali EP „Només viure”, potwierdzając swój moment rozkwitu i zdolność do "
        "wzruszania własnym uniwersum dźwiękowym oraz wyjątkową więzią z katalońską publicznością.\n\n"
        "W 2026 roku Ginestà wydał swój nowy album „Gira tot igual, però diferent”, dzięki któremu zarówno publiczność, jak "
        "i organizatorzy potwierdzili ich pozycję jako jednej z najbardziej inspirujących, społecznie zaangażowanych i "
        "ulubionych propozycji katalońskiej sceny muzycznej."
    ),
    1325: (
        "Dwaj koledzy o disco-sercu i pop-neuronie, pewnego dnia postanawiają zmieszać syntezatory z lat 80., teksty w "
        "języku katalońskim i imprezowe beaty. Są wyimaginowaną kawą między Daft Punk i Lluísem Gavaldą. Są groove'em i "
        "niedzielną melancholią; są elektroniką z duszą człowieka. Są chórami z vocoderem. Są „V-H-S” z mocą uderzenia. "
        "Są historiami, które być może są też Wasze."
    ),
    1324: (
        "Powraca najbardziej kochane karaoke w mieście. Wybierz piosenkę, weź mikrofon i zostań gwiazdą Festa Major!\n\n"
        "Live Karaoke Show to koncert na żywo, na którym publiczność wybiera i śpiewa repertuar wieczoru. Lista licząca "
        "ponad 170 piosenek do wyboru, 2 godziny spektaklu z 7 muzykami na żywo, koncert szalony i pełen udziału publiczności, "
        "z finałowym medleyem jako zakończeniem zabawy. My gramy, a ludzie śpiewają te piosenki, które najbardziej im się "
        "podobają (po katalońsku, hiszpańsku lub angielsku), czując się częścią spektaklu."
    ),
    1326: (
        "The Tyets, jedna z gwiazd Festa Major de Sant Cugat 2026!\n\n"
        "Po tym, jak w ostatnich latach stali się bezprecedensowym fenomenem, The Tyets w 2026 roku wciąż są nie do "
        "zatrzymania, utrwalając swoją pozycję jednej z głównych atrakcji i gwiazd naszego kraju. Ich najnowszy album, "
        "„Cafè pels més cafeteros” (Luup Records, 2025), został wydany wraz ze spektakularną trasą koncertową, która "
        "okazała się prawdziwym sukcesem wśród publiczności.\n\n"
        "The Tyets zaprezentują utwory, które już oczarowują fanów, takie jak ich udana współpraca z Estopą, „Camila”, "
        "czy „Tàndem”, jedna z piosenek lata. Po raz kolejny ich charakterystyczne „tieta” universum obiecuje dalej rosnąć "
        "i sprawiać, że tańczy cały kraj."
    ),
    1328: (
        "Z rąk kolektywu Phonodisco Club przybywa Olau, didżej i mieszkaniec La Floresta, który zaproponuje autorski set "
        "elektroniki: disco & jackin' house, by nie przestać tańczyć."
    ),
    1329: (
        "Marc Navarro to wszechstronny didżej, który dostosowuje się do każdej sesji w zależności od publiczności i "
        "momentu, oferując dynamiczne i pełne energii sety. Obecnie jest rezydentnym didżejem w Moon Sant Cugat, a także "
        "występował w uznanych klubach takich jak Bling Bling Barcelona, Twenties Barcelona, Costa Este czy BeOut, między "
        "innymi, i ugruntował styl, który łączy się z każdym typem publiczności."
    ),
    1327: (
        "Jeśli szukasz czegoś delikatnego, szukaj dalej, ale jeśli chcesz imprezy z gitarami, które wybuchają, riffami, "
        "które unoszą Cię do góry, i koncertu na żywo, który rozwali Ci głowę, Big Mouthers to Twój zespół coverowy. "
        "Koncert, który przechodzi przez wszystkie hymny historii muzyki i najbardziej przebojowe piosenki współczesności, "
        "z zespołem o wrodzonej elegancji, w skórzanych kurtkach, butach, dopasowanych spodniach i z większą postawą niż "
        "uliczny buntownik."
    ),
    1285: (
        "Turniej padla z okazji Festa Major, w różnych kategoriach.\n\n"
        "Wymagana rejestracja na www.familiaamic.cat, familiaamic@gmail.com / 623 101 549\n\n"
        "Stowarzyszenie FamiliaAMIC to organizacja niedochodowa, której głównym celem jest promowanie równości szans oraz "
        "szerszego dostępu do praw społecznych i indywidualnych dla osób z niepełnosprawnością intelektualną i ich rodzin."
    ),
    1286: (
        "Wraz z nadejściem lata, Casa Aymat. Espai de Creació otwiera swoje drzwi z okazji Festa Major!\n\n"
        "10:00 Powitanie i śniadanie\n"
        "Od 10:00 do 13:00:\n\n"
        "- Sztuka w rodzinie. Krosna na ulicy, z zespołem edukacyjnym art.santcugat. Naucz się tkać gobelin razem z rodziną\n"
        "- Wątek, wątek, wątek, z zespołem edukacyjnym art.santcugat. Zajęcia umożliwiające odkrycie i poznanie techniki "
        "tkania gobelinów.\n"
        "- Warsztaty i otwarte studia: przechadzka po przestrzeniach Casa Aymat, podczas której można poznać prace uczniów "
        "oraz projekty tegorocznych artystów rezydujących.\n\n"
        "13:30 Wspólne pica-pica (poczęstunek). Przynieś coś do jedzenia, aby się podzielić i wspólnie pożegnać sezon.\n\n"
        "Z udziałem użytkowniczek Casa Aymat. Espai de creació.\n"
        "Pod patronatem Rabassaires i Katia."
    ),
    1287: (
        "Wielka aranżacja gier do wspólnej zabawy w rodzinie z okazji Festa Major!\n\n"
        "„Pirene” zespołu Apikipala. Zaproszenie do odkrywania pejzaży Pirenejów w instalacji łączącej sztukę, rzemiosło, "
        "mechanikę i zabawę.\n"
        "„Lilliput” zespołu Tombs Creatius. Propozycja, w której baśnie nie są opowiadane… są rozgrywane!\n"
        "Warsztat gier wielkoformatowych z Circ de les Musaranyes\n\n"
        "Od 10.30 do 13.30"
    ),
    1288: (
        "Stoisko La Teulada to punkt informacyjny, w którym udzielane jest wsparcie techniczne i porady dotyczące "
        "transformacji energetycznej. Odbędą się tam również warsztaty animacyjne, mające na celu przybliżenie mieszkańcom "
        "energii odnawialnej w sposób jasny i praktyczny.\n\n"
        "Od 11:00 do 20:00"
    ),
    1289: (
        "Big band tworzona przez studentów i wykładowców Aula de So, gdzie muzyka rozwija się w atmosferze współpracy i "
        "wysokich wymagań artystycznych. Z repertuarem obejmującym jazz, muzykę latynoską i nowoczesne brzmienia, AJO "
        "występowała na festiwalach i prestiżowych scenach, umacniając swoją pozycję jako projektu z wyrazistą tożsamością "
        "i bogatym doświadczeniem scenicznym."
    ),
    1290: (
        "Inspektorka Aparicio i Jeni potrzebują twojej pomocy, aby rozwiązać zbrodnię w Archiwum. Przyjdź i pomóż im w "
        "tym śledztwie!\n\n"
        "Dla wszystkich grup wiekowych. Bezpłatna aktywność w ramach Festa Major. Liczba miejsc ograniczona.\n\n"
        "Zapisy: arxiu@santcugat.cat\n\n"
        "Współpraca: Mira-sol teatre"
    ),
    1291: (
        "Wymagana wcześniejsza rejestracja na adres handbolsantcugat@hotmail.com\n\n"
        "Piłka ręczna plażowa to sport zespołowy, w którym dwie drużyny podają sobie piłkę oraz odbijają ją lub kozłują, "
        "starając się umieścić ją w bramce przeciwnika. Gra przypomina standardową piłkę ręczną, jednak rozgrywana jest "
        "na piasku, a nie na twardej powierzchni."
    ),
    1899: "Mecz siatkówki między lokalnymi mediami a politykami Sant Cugat z okazji Festa Major.",
    1292: (
        "Turniej szachowy Festa Major powraca do Sant Cugat z drugą edycją, pomyślaną tak, by cieszyć się szachami w "
        "otwartej, szybkiej i bardzo angażującej atmosferze. Ten turniej szybkich partii organizuje Club d'Escacs Dos "
        "Torres Sant Cugat w ramach Festa Major, z celem przybliżenia szachów graczom wszystkich wieków i poziomów.\n\n"
        "System szwajcarski, 8 rund\n"
        "Turniej szybkich partii, otwarty dla wszystkich.\n"
        "Wymagana wcześniejsza rejestracja: escacsdostorres@gmail.com lub www.escacsdostorresdesantcugat.cat\n\n"
        "Od 17.00 do 20.30. Przed rozpoczęciem, prezentacja odbędzie się o 16.45, a wręczenie nagród o 20.45."
    ),
    1271: (
        "Wesołe miasteczko będzie działać w kolejnych dniach:\n"
        "Sobota 27, od 17 do 02\n"
        "Niedziela 28, od 17 do 01\n"
        "Poniedziałek 29, od 17 do 00\n\n"
        "Od 17 do 19 muzyka i intensywne światła na atrakcjach zostaną tymczasowo wyłączone."
    ),
    2416: (
        "Mecànic Pizza zaprasza na Festa Major z okazji Pizza Week!\n\n"
        "Otwieramy wystawę Mirai Ceramies w Mecànic Pizza wraz z aperitifem i degustacją naszych produktów. Otwarte "
        "spotkanie na styku ceramiki, pizzy, ognia i ręcznego rzemiosła.\n\n"
        "Wstęp wolny; od 18 do 20"
    ),
    1916: (
        "Przyjdź i baw się na Festa de l'Esport, pełnym zabawowych i sportowych aktywności dla całej rodziny. To miejsce "
        "pełne atrakcji i sprzętu sportowego, w którym mali i duzi będą mogli się poruszać, grać i odkrywać różnorodne "
        "propozycje sportowe."
    ),
    1907: (
        "Pokaz kulinarny otwarty dla wszystkich, z letnią kuchnią i produktami sezonowymi oraz napojami w świątecznym "
        "nastroju. Szef kuchni Bocamoll, Pepe Vidal, przygotuje danie, które zostanie zaserwowane w formie tapas. Manel "
        "Guirado, kucharz, sommelier i koordynator Aula Gastronòmica, dobierze do niego wino oraz drink.\n\n"
        "Zapisy na centresculturals.santcugat.cat lub casaltorreblanca@santcugat.cat"
    ),
    1301: (
        "Dla osób od 18 lat\n\n"
        "Wymagana jest wcześniejsza rejestracja — prosimy o kontakt z klubem w jego biurze.\n\n"
        "Turniej F7 (piłka nożna 7-osobowa) to zawody sportowe, w których zespoły rozgrywają mecze piłki nożnej w "
        "składzie 7 zawodników na boisku, łącznie z bramkarzem. To bardziej kompaktowa i dynamiczna forma niż piłka "
        "nożna 11-osobowa, z szybkimi meczami i dużym tempem gry."
    ),
    1299: (
        "18:00 Sekcja gimnastyki rytmicznej CMSC\n"
        "19:00 Club Gimnàstica Rítmica i Estètica Sant Cugat"
    ),
    1297: (
        "Inspektorka Aparicio i Jeni potrzebują twojej pomocy w rozwiązaniu zbrodni w Archiwum. Przyjdź i pomóż im w "
        "tym śledztwie!\n\n"
        "Dla wszystkich. Bezpłatna aktywność. Ograniczona liczba miejsc\n\n"
        "Zapisy: arxiu@santcugat.cat\n\n"
        "Współpraca: Mira-sol teatre"
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
