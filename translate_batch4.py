# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Batch 4 of remaining description_pl translations (15 events)."""
import json

TRANSLATIONS = {
    1346: "Z Vinylics",
    1345: (
        "Przyjdź na zabawne i twórcze doświadczenie gastronomiczne. Dzieci będą gotować "
        "przepisy inspirowane różnymi kuchniami świata, nauczą się technik kulinarnych "
        "dopasowanych do swojego wieku i, co najważniejsze, będą się świetnie bawić, "
        "eksperymentując, tworząc i działając w zespole.\n\n"
        "Oryginalna, edukacyjna i smakowita aktywność, by przeżyli kuchnię jako wielką "
        "przygodę!\n\n"
        "Wiek: 6–12 lat\nCzas trwania: 1 godz.\nWstęp wolny\n"
        "Zapisy indywidualne lub zespołowe (maks. 5 dzieci) na "
        "https://tallersalombra-tallerdecuina.eventbrite.es"
    ),
    2009: (
        "Swing, pop, ballady… koncert pełen rytmu, by celebrować Festa Major.\n\n"
        "Kierownictwo: Enric Mestre"
    ),
    1350: (
        "Wymagana wcześniejsza rejestracja na Instagramie klubu.\n@rugbysantcugat"
    ),
    2024: (
        "Wesołe miasteczko trwa w kolejnych dniach:\n"
        "Niedziela 28, od 17.00 do 1.00\n"
        "Poniedziałek 29, od 17.00 do 0.00\n\n"
        "Od 17.00 do 19.00 muzyka i intensywne światła na atrakcjach zostaną tymczasowo "
        "wyłączone."
    ),
    2018: "Udział otwarty dla wszystkich",
    1355: (
        "„Pintxo Pote” to gastronomiczna tradycja Kraju Basków, łącząca „pintxo” "
        "(przekąskę) z „pote” (drinkiem). Znajdziesz tu też tradycyjne baskijskie "
        "aktywności i muzykę.\n\n"
        "17.00 Otwarcie przestrzeni\n"
        "18.00 Start „Pintxopote” (6 odmian „pintxos” + drink)\n"
        "19.00 „Txapela” – baskijskie gry ludowe\n"
        "20.00 „Sokatira” (przeciąganie liny)\n"
        "20.30 Muzyka z gramofonu do zamknięcia\n\n"
        "Przez całe popołudnie będzie grana tradycyjna muzyka Kraju Basków, by ożywić "
        "atmosferę.\n"
        "Zachęcamy grupy do udziału w pierwszej Txapeli gier ludowych. Zwycięska grupa "
        "otrzyma nagrodę!"
    ),
    1352: (
        "Komedia świątecznego oporu. W jakimś europejskim biurze pełnym papierów "
        "postanawia się, że Festa Major de Sant Cugat jest za głośna… ale dom seniora "
        "staje w obronie święta!\n\n"
        "Z Grup de Teatre Còmic Llar, w reżyserii Giseli Figueras"
    ),
    1340: (
        "Mini Festiwal Literatury dla dzieci od 0 do 5 lat, organizowany przez Institut "
        "de la Infància.\n"
        "Mały festiwal, by cieszyć się i zakochać w najlepszych książkach, ilustrowanych "
        "albumach i opowiadaniach dla dzieci od 0 do 5 lat.\n\n"
        "Wymagana wcześniejsza rejestracja na https://museu.santcugat.cat/agenda/\n"
        "Wstęp wolny, ograniczona liczba miejsc"
    ),
    2032: (
        "Przyjdź cieszyć się Festa de l’Esport, z zabawami i aktywnościami sportowymi dla "
        "całej rodziny. Przestrzeń pełna aktywności i sprzętu, gdzie duzi i mali będą "
        "mogli się poruszać, grać i odkrywać różne propozycje sportowe.\n\n"
        "18.00 Zumba\n"
        "19.00 La gàbia: fizyczne wyzwania dla młodzieży inspirowane crossfitem i innymi "
        "dyscyplinami."
    ),
    1357: "Z Sossy de Swert, we współpracy z Jambo Art",
    1295: (
        "Pokaz kulinarny otwarty dla wszystkich, z letnią kuchnią i produktami oraz "
        "napojami na świętowanie. Kucharz i wykładowca Aula Gastronòmica, Manel "
        "Guirado, przygotuje danie, które zostanie podane uczestnikom w formie tapas. "
        "Anton Sabariego, ekspert i producent piwa i wina oraz współwłaściciel "
        "Bocamoll, sparuje je z piwem i winem.\n\n"
        "Zapisy na centresculturals.santcugat.cat lub casaltorreblanca@santcugat.cat"
    ),
    1272: "Program FMA",
    1362: (
        "Tradycyjny koncert repertuaru ludowego katalońskiego i Clavé, z stuletnim "
        "chórem Coral La Unió oraz innymi zaproszonymi chórami.\n\n"
        "Wstęp wolny"
    ),
    1363: (
        "18.45 Dj Fem Lindy\n"
        "19.00 Otwarta lekcja solo jazz z Roser Ros (taniec swingowy indywidualny)\n"
        "19.45 Otwarta lekcja lindy hop z Bertą i Miquelem Claparols (taniec swingowy w "
        "parach)\n"
        "20.45 Otwarta lekcja wprowadzająca do bluesa z Sandrą Fuentes i Jordim "
        "Figuerasem (taniec w parach)\n\n"
        "Współpraca: Xarxa de Centres Culturals"
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
