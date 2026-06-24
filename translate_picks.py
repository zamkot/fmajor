# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Set description_pl for the user's currently-starred picks (manually translated)."""
import json

TRANSLATIONS = {
    1936: (
        "Organizowana przez klub Handbol Sant Cugat, popularna botifarrada to okazja, "
        "by zasiąść wspólnie do stołu w dobrej atmosferze i świątecznym nastroju, wraz "
        "z sąsiadami i sportowcami podczas Festa Major. Spotkanie otwarte dla wszystkich, "
        "by cieszyć się lokalną kuchnią w emblematycznym miejscu — Parc de Can Vernet."
    ),
    1310: (
        "Botifarrada Popular klubu Muntanyenc Sant Cugat to jedno z najbardziej "
        "tradycyjnych wydarzeń gastronomicznych Festa Major. Każdego roku gromadzi "
        "mieszkańców Sant Cugat we wspólnej, świątecznej atmosferze przy stole.\n\n"
        "Menu obejmuje kiełbasę botifarra, chleb z pomidorem (pa amb tomàquet), arbuza, "
        "koka (tradycyjny placek) oraz piwo rzemieślnicze lub wodę. Idealna propozycja, "
        "by zjeść posiłek w gronie sąsiadów i poczuć atmosferę święta z rodziną i przyjaciółmi."
    ),
    1316: (
        "Z udziałem grup: Petits Udols de Calella, Diables de Viladecans, Diables de "
        "Sant Joan Despí, Diables de la Creu Alta de Sabadell i Diables de Sant Cugat.\n\n"
        "Dwie równoległe trasy:\n"
        "Trasa dla młodzieży: plaça d'Octavià, carrer de la Plana de l'Hospital, carrer "
        "de Sant Esteve, carrer de la Indústria, carrer d'Abat Armengol, carrer de Santa "
        "Anna, plaça de Pep Ventura, carrer de Sant Martí, carrer de Castillejos, carrer "
        "de Sant Domènec, plaça de Sant Pere, carrer Major, plaça d'Octavià.\n"
        "Trasa dla dzieci: plaça d'Octavià, carrer de Santiago Rusiñol, carrer del Carme, "
        "carrer de Gorina, plaça de Magí Bartralot, carrer de Gorina, plaça dels Quatre "
        "Cantons, avinguda de Rius i Taulet, Baixada de Sant Sever, avinguda de Catalunya, "
        "carrer d'Enric Granados, plaça de Sant Pere, carrer Major, plaça d'Octavià."
    ),
    1359: (
        "Z udziałem grup castellers (budujących ludzkie wieże): Minyons de Terrassa, "
        "Nens del Vendrell i Castellers de Sant Cugat."
    ),
    1385: (
        "Z udziałem grup: Diables de Sant Joan Despí, Diables de Cubelles, Diables de la "
        "Creu Alta de Sabadell, Tro de Falguera de Sant Feliu de Llobregat i Diables de "
        "Sant Cugat.\n\n"
        "Dwie równoległe trasy:\n"
        "Trasa „Infern” (Piekło): pl. Octavià, c. Plana Hospital, c. Abat Armengol, c. de "
        "la Mina, c. Aymerich, c. Sant Martí, c. Sabadell, pl. Sant Pere, c. Major, pl. "
        "Octavià.\n"
        "Trasa „Espurna” (Iskra): pl. Octavià, c. Santiago Rossinyol, c. del Carme, c. "
        "Gorina, pl. Magí Bartralot, c. Gorina, pl. dels Quatre Cantons, av. Rius i "
        "Taulet, Baixada de Sant Sever, av. Catalunya, c. Enric Granados, pl. Sant Pere, "
        "c. Major, pl. Octavià."
    ),
    1395: (
        "Jedno z najbardziej wyczekiwanych i najtłoczniejszych wydarzeń Festa Major de "
        "Sant Cugat!\n\n"
        "Przy rekordowej liczbie 1519 zgłoszeń (1385 ważnych), losowanie odbyło się w "
        "piątek 5 czerwca w Ateneu Santcugatenc i wyłoniło numery od 1431 do 1853, które "
        "otrzymują miejsce w konkursie. Konkurs odbędzie się w niedzielę 28 czerwca na "
        "avinguda de Can Volpelleres.\n\n"
        "Wydarzenie bez obsługi barowej."
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
