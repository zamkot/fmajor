# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Batch 3 of remaining description_pl translations (15 events)."""
import json

TRANSLATIONS = {
    1331: (
        "Torneig Solidari de Bàsquet 3×3 to sportowa propozycja otwarta na udział w "
        "ramach Festa Major de Sant Cugat.\n\n"
        "Zorganizowany w współpracy z Thionck Essyl Basketball, turniej ma charakter "
        "charytatywny i cały zebrany dochód zostanie przekazany na projekt w Senegalu, z "
        "którym współpracuje QBasket Sant Cugat.\n\n"
        "Wymagana wcześniejsza rejestracja na "
        "https://qbasketsantcugat.com/producte/inscripcio-3x3-solidari-per-senegal/"
    ),
    1330: (
        "Pokaz w formie zawodów w różnych dyscyplinach strzelectwa z łuku.\n\n"
        "Otwarty udział w zajęciach wprowadzających do strzelectwa z łuku.\n\n"
        "Wymagana wcześniejsza rejestracja, skontaktuj się z klubem: "
        "arquersdesantcugat@gmail.com"
    ),
    1968: "Odkryj, jak środowisko naturalne jest dotykane przez współczesne konflikty.",
    1300: (
        "Przyjdź cieszyć się Festa de l’Esport, z zabawami i aktywnościami sportowymi dla "
        "całej rodziny. Przestrzeń pełna aktywności i sprzętu, gdzie duzi i mali będą "
        "mogli się poruszać, grać i odkrywać różne propozycje sportowe.\n\n"
        "11.00 Joga dla wszystkich, prowadzona przez Ashtanga Yoga Sant Cugat."
    ),
    1337: (
        "Symultaniczne partie szachowe są częścią programu Festa Major de Sant Cugat i "
        "odbędą się z udziałem Mistrza Katalonii z klubu.\n\n"
        "Aktywność jest otwarta dla wszystkich i daje okazję do cieszenia się szachami w "
        "przystępnej, angażującej atmosferze, spędzając dzień wokół tej strategicznej "
        "gry.\n\n"
        "Propozycja stworzona, by zbliżyć szachy do mieszkańców w ramach programu "
        "aktywności Festa Major."
    ),
    1335: (
        "Zwiedzanie, które pozwoli ci przejść się praktycznie samemu po wnętrzu Monestir "
        "i jego kościoła. Odkryjesz historię najpotężniejszego klasztoru hrabstwa "
        "Barcelony oraz symbolikę jego wspaniałego krużganka, najważniejszego w Europie w "
        "zakresie sztuki rzeźbiarskiej romańskiej.\n\n"
        "Wymagana wcześniejsza rejestracja na "
        "https://visit.santcugat.cat/visita-guiada-monestir-de-sant-cugat/"
    ),
    1334: (
        "Rajd rowerowy na 10 km, by rodziny mogły cieszyć się jazdą na rowerze, "
        "odkrywając przy tym swoje najbliższe otoczenie.\n\n"
        "Trasa: Parc Central (c. Manel Farrés rogu c. Rovellat); c. Ramon Llull, droga "
        "rowerowa av. Països Catalans, droga rowerowa ctra. Rubí, rondo hipòdrom "
        "Martins, c. Cerdanya, av. Can Graells, c. Antoni Bell, stacja Volpelleres, c. "
        "Mare de déu del Roser, c. Alfons d’Aragó, av. Can Volpelleres, c. Ventura Gasol, "
        "droga rowerowa c. Carles Riba, c. Màrius Torres, c. Clementina Arderiu, wnętrze "
        "Parc Pla Farreras, c. Abat Biure, droga rowerowa av. Ragull, rbla. Torrent d’en "
        "Xandri, c. d’Orient, rbla. del Celler, droga rowerowa c. Josep Puig i Cadafalch, "
        "droga rowerowa av. Corts Catalanes, droga rowerowa av. Pla del Vinyet, av. de "
        "Gràcia, c. Francesc Moragas, droga rowerowa c. Rius i Taulet, av. Lluís Companys, "
        "c. Esperanto, c. Mercè Rodoreda, droga rowerowa c. Manel Farrès, Parc Central."
    ),
    1972: (
        "Festiwal „Petits! Grans! Llibres!” trafia do Claustre w Sant Cugat z propozycją "
        "poświęconą literaturze dla najmłodszych dzieci.\n\n"
        "Zorganizowany przez Institut de la Infància, ten mini festiwal zaprasza rodziny "
        "do odkrywania i cieszenia się wyborem książek, ilustrowanych albumów i "
        "opowiadań stworzonych specjalnie dla dzieci od 0 do 5 lat.\n\n"
        "Aktywność daje przestrzeń, by przybliżyć czytanie najmłodszym i dzielić się "
        "chwilami wokół historii, wyobraźni i książek w wyjątkowym, historycznym "
        "otoczeniu krużganka klasztoru.\n\n"
        "Wymagana wcześniejsza rejestracja na https://museu.santcugat.cat/agenda/\n"
        "Wstęp wolny, ograniczona liczba miejsc"
    ),
    1339: (
        "Przestrzeń warsztatów artystycznych, by cieszyć się nimi w rodzinie!\n\n"
        "„Connexions” – twórcza gra polegająca na budowaniu swobodnych konstrukcji z "
        "drewnianych kijków i łączników, oraz „Assemblatges” – gra konstrukcyjna "
        "trójwymiarowa. Z Koala Art for Kids.\n\n"
        "„El més forçut del circ” z Gest Lúdic l’Obrador. Warsztat tworzenia cyrkowej "
        "postaci.\n\n"
        "Warsztat kulinarny „Experiència Mastercook” z The Playcook Kids (wymagana "
        "wcześniejsza rejestracja)."
    ),
    1338: (
        "Przyjdź na zabawne i twórcze doświadczenie gastronomiczne. Dzieci będą gotować "
        "przepisy inspirowane różnymi kuchniami świata, nauczą się technik kulinarnych "
        "dopasowanych do swojego wieku i, co najważniejsze, będą się świetnie bawić, "
        "eksperymentując, tworząc i działając w zespole.\n\n"
        "Oryginalna, edukacyjna i smakowita aktywność, by przeżyli kuchnię jako wielką "
        "przygodę!\n\n"
        "Wiek: 6–12 lat\nCzas trwania: 1 godz.\nWstęp wolny\n\n"
        "Zapisy indywidualne lub zespołowe (maks. 5 dzieci) na "
        "https://tallersalombra-tallerdecuina.eventbrite.es"
    ),
    1342: "Z zespołem gralli i kotłów ze Escola de Música Tradicional.",
    1341: (
        "Przyjdź, baw się i podziel się pasją do motocykli! Wyjazd otwarty dla wszystkich "
        "typów motocykli: klasycznych, nowoczesnych i skuterów. Dla wszystkich "
        "uczestników darmowy napój i przekąski. Podczas zjazdu zostaną przyznane drobne "
        "wyróżnienia i nagrody: najstarszy motocykl, najbrudniejszy, nagroda Rat Penat za "
        "najbardziej charakterny wydech, i wiele innych niespodzianek!\n\n"
        "Współpraca: Vallès27, warsztat motocyklowy\n\n"
        "Bez wcześniejszej rejestracji\n\n"
        "Trasa: pl. Sant Francesc, c. Joan XXIII, c. Salvador Espriu, pg. Francesc Macià, "
        "rbla. Celler, c. Francesc Moragas, av. Rius i Taulet, av. Lluís Companys i "
        "Jover, c. Àngel Guimerà, rbla. Ribatallada, av. Pla del Vinyet, av. Torre "
        "Blanca, rbla. del Celler, c. Francesc Macià, c. Abat Guillem d’Avinyó, av. "
        "Ragull, c. Santa Engràcia, Jardins de Sant Francesc"
    ),
    1400: (
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
    ),
    1344: (
        "Zwiedzanie z przewodnikiem klasztoru wokół trzech letnich świąt ważnych dla "
        "Sant Cugat: Sant Joan i początek lata, Sant Pere, patron miasta, oraz Sant "
        "Cugat, patron klasztoru.\n\n"
        "Wstęp wolny\n\n"
        "Wymagana wcześniejsza rejestracja na https://museu.santcugat.cat/agenda/"
    ),
    1347: (
        "Zapisz się na najbardziej szaleńczy turniej roku – szybki, strategiczny i bardzo "
        "zabawny! Stwórz parę z przyjacielem lub przyjaciółką i przygotujcie się, by "
        "wyeliminować tyle par, ile zdołacie… zanim wyeliminują was!\n\n"
        "Zapisy par od 11 czerwca na cugat.cat/fm-torneig-globus"
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
