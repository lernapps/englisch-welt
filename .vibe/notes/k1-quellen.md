# Kapitel 1 `hello-america`: Quellen, Wörter, Hörliste, Abweichungen

Stand 2026-11-24. Geöffnet wurde jede Quelle per API (englische Wikipedia, Klartext, `action=query&prop=extracts&explaintext=1`), Fakten ohne Sätze übernommen (CC BY-SA, eigene Formulierung). Persönliche Aussagen Jaydens („in my school …“, Basketball spielen, Musik als Wahlfach) und Sophies („I play football with Ellie“) sind erfundene Erzählung der Chats, keine Faktenangaben über die USA.

## Quellen je Seite

### das-brauchst-du (Wiederholungsseite)
- Karte `https://lernapps.net/apps/map/englisch.json` (aus `/tmp/map.json`): „Ich kann“-Sätze von `schule-uk` und `feste-uk` wörtlich.
- Keine neuen Fakten. Wörter der Tabelle (school uniform, school day, Christmas, Bonfire Night, Halloween) stammen aus den „Ich kann“-Sätzen. **Nicht geprüft** (Allgemeinwissen, nicht aus einer Quelle): „Halloween am Ende des Oktobers“, „Bonfire Night: Abend mit Feuer und Feuerwerk“; Schulbeginn 8:45 in Millbrook ist Vorgabe der Konventionen.

### usa-staedte
- Geöffnet: `New York City` (en.wikipedia), `Washington, D.C.` (en.wikipedia), `United States` (`/tmp/wp/United_States.txt`).
- Fakten: New York ist die bevölkerungsreichste Stadt der USA; New York war von 1785 bis 1790 Hauptstadt (hier nur „für kurze Zeit“); Freiheitsstatue, Geschenk Frankreichs, im New Yorker Hafen (1886 eingeweiht, nicht im Text); Central Park in Manhattan, viel besuchter Stadtpark (42 Millionen Besuche 2023, hier nur „Millionen“); Times Square, hell erleuchtet, Zentrum der Broadway-Theater; mehr als 800 gesprochene Sprachen (hier „many languages“). Washington, D.C.: Hauptstadt und einziger Bundesdistrikt, gehört zu keinem Staat; steht am Potomac, umgeben von Maryland, gegenüber von Virginia; „District of Columbia“; White House, Capitol, Supreme Court; National Mall mit Lincoln Memorial, Washington Monument, Jefferson Memorial; Smithsonian-Sammlungen kostenlos zugänglich; ab 1800 tagte der Kongress im Capitol.
- Aussage „Congress meets in the Capitol“ (Gegenwart) stützt sich auf die Liste der Bundesgebäude und den Einzug 1800; „Washington State ist einer der fünfzig Staaten“ stützt sich auf `United States` (fünfzig Staaten, D.C. kein Staat); die Lage des Bundesstaats Washington im Nordwesten steht nicht im Text (bewusst weggelassen).
- **Nicht geprüft:** Empire State Building steht nur in der Liste „major landmarks“ und kommt nicht im Text vor; keine Höhenangaben. „Hamburg/Berlin“ nicht benutzt (Merke mit erfundenem Beispiel „hall … biggest room in our school“).

### kanada
- Geöffnet: `Canada` (`/tmp/wp/Canada.txt`), `Official bilingualism in Canada` (en.wikipedia).
- Fakten: zehn Provinzen, drei Territorien; Atlantik, Pazifik und Arktischer Ozean; zweitgrößtes Land nach Gesamtfläche (nach Landfläche Platz vier, hier „Only one country is bigger“ und „second biggest“ als vereinfachte Gesamtfläche); längste internationale Landgrenze (mit den USA); Hauptstadt Ottawa, größte Großräume Toronto, Montreal, Vancouver; Englisch und Französisch Amtssprachen der Bundesregierung; mehr als 82 Prozent der französischsprachigen Kanadier leben in Quebec (hier „most“); Muttersprache Französisch ca. 19 Prozent (hier „a first language for many Canadians“); Lebensmittel müssen mit Englisch und Französisch gekennzeichnet sein (hier „many packages“); Indigene Völker (First Nations, Inuit, Métis) leben seit Tausenden Jahren dort; ca. 5 Prozent (1,8 Millionen, Zählung 2021); elf indigene Sprachgruppen, mehr als 65 Sprachen und Dialekte (hier „many different languages“); Inuktitut Mehrheitssprache und eine von drei Amtssprachen in Nunavut; etwa 80 Prozent der Bevölkerung leben nahe der Grenze zu den USA (hier „Many people live near the border“).
- **Nicht geprüft:** Lage von Vancouver, Toronto und Montreal auf der Schemakarte (Städte sind belegt, die Lage ist grob nach Allgemeinwissen gezeichnet; „nicht genau nach Maßstab“). Aussprache von Inuktitut und Nunavut: kein Hörsatz mit diesen Wörtern (das Sprachmodell kann sie falsch sprechen).

### jugend-usa
- Geöffnet: `American football`, `Basketball` (beide en.wikipedia), `United States` (Abschnitt Sports und Cuisine), `Chicago` (`/tmp/wp/Chicago.txt`).
- Fakten: beliebteste Zuschauersportarten sind American football, Basketball, Baseball, soccer und Eishockey; American football in den USA kurz „football“; Basketball 1891 in den USA erfunden (Jahr nicht im Text); High-School-Football und -Basketball sind verbreitet (Footballs Schulebene „most popular sport played by boys“, hier nur „many high schools have a team“); amerikanische Gerichte (Hamburger, Hot Dogs, Pizza, Mac and Cheese, Apple Pie) gehen auf Rezepte verschiedener Einwanderergruppen zurück; Chicago: deep-dish pizza, viele öffentliche Strände am Lake Michigan (Chicago.txt nennt an einer Stelle 24 öffentliche Strände, an anderer 31 Sandstrände: deshalb keine Zahl), im Sommer viele Konzerte in Grant Park und Millennium Park, bekanntes Basketballteam (Bulls); Basketball: zwei Teams mit je fünf Spielern.
- Die Aussage „In den USA heißt Sophies football soccer“ stützt sich auf die Sportliste im Artikel `United States` („soccer“ neben „American football“) und auf `American football` („referred to simply as football in the United States and Canada“).
- **Nicht geprüft:** Zahlen zu Sportlern (bewusst nicht benutzt); die Aussage „Burgers and hot dogs are popular“ stützt sich nur auf die Liste charakteristischer Gerichte.

### schule-usa
- Geöffnet: `High school in the United States` (en.wikipedia), `Homeroom` (en.wikipedia), `Locker` (en.wikipedia).
- Fakten: meist grades neun bis zwölf; ninth grade entspricht in England Year Ten; freshman, sophomore, junior, senior; Schulbeginn zwischen sieben und neun Uhr morgens, Schulende zwischen zwei und vier Uhr; vier bis acht class periods von vierzig bis neunzig Minuten; Mittagessen meist in der Schule, an manchen Schulen darf man gehen; Wahlfächer (electives); Sportmannschaften trainieren direkt nach der Schule; öffentliche High Schools sind kostenlos (Steuern) und nehmen alle Kinder ihres Bezirks auf; Schuljahr etwa neun Monate; Homeroom: kurze Zeit am Morgen mit Anwesenheitsliste und Mitteilungen, in Großbritannien form time oder registration; Locker: abschließbares Fach für persönliche Sachen, häufig in Schulen.
- **Nicht geprüft:** Schulbus (Artikel `School bus in the United States` ließ sich nicht öffnen, HTTP 429): die Aussage entfiel. Der Stundenplan im Bild („Jaydens Schultag, Beispiel“) ist ein erfundenes Beispiel ohne Uhrzeiten; die Reihenfolge der Mittagspause ist nicht belegt. „In my school I can choose music“ und „I keep my books in my locker“ sind Jaydens persönliche Aussagen. Schulabschlüsse und Noten bewusst nicht behandelt (Issue #486).

### feste-usa
- Geöffnet: `Thanksgiving (United States)` (`/tmp/wp/Thanksgiving__United_States_.txt`), `United States Declaration of Independence` (`/tmp/wp/United_States_Declaration_of_Independence.txt`), `Independence Day (United States)` (en.wikipedia).
- Fakten Thanksgiving: Bundesfeiertag, vierter Donnerstag im November (einheitlich seit 1941), also wechselndes Datum; Familienessen mit Truthahn, Kartoffeln, Mais, Kürbiskuchen; Paraden (Macy's in New York seit 1924) und American-football-Spiele; Kanada hat ein eigenes Thanksgiving; Erntefest 1621 in Plymouth (Pilgrims und Wampanoag, mutual-protection-Abkommen); Erzählung der Nachfahren der Wampanoag: das Fest sei zuerst nur für die Pilgrims angesetzt gewesen, die Wampanoag seien nicht eingeladen worden, um beim Anbau zu helfen („popular story“ hier als verbreitete Fassung); der heutige Feiertag geht auf mehrere Tage des Dankens in Neuengland zurück (1863 Lincoln, keine Jahreszahl im Text); einige Native Americans nennen den Tag National Day of Mourning (seit 1970 Protest in Plymouth), die Haltungen sind verschieden.
- Fakten Independence Day: Bundesfeiertag am 4. Juli, erinnert an die Annahme der Declaration of Independence (4. Juli 1776), umgangssprachlich Fourth of July, Picknicks, Barbecues, Paraden, Feuerwerk (meist abends), Rot, Weiß und Blau.
- **Nicht geprüft:** „Erntedank“ wird nur als Fehlvorstellung beim Namen genannt (keine Aussage über das deutsche Erntedankfest, nur über Thanksgiving). „Weihnachten am 25. Dezember“ (Allgemeinwissen, als Distraktor).

## Wörter außerhalb von A1/A2 (Grundwortschatzliste `/tmp/gw.json`)

Auf der Seite erklärt (Randglossar) oder als Name/Eigenname; in dieser Liste, damit niemand etwas Ungeklärtes findet.
- **usa-staedte:** harbor (AE), theater (AE), capital, gift, free, District of Columbia, Congress, Capitol, biggest, Potomac (Name).
- **kanada:** border, province, territory, Arctic, official language, package, Indigenous, First Nations, Inuit, Métis, neighbor (AE, im Chat markiert), Quebec, Nunavut, Inuktitut (Namen).
- **jugend-usa:** team, invented, popular, soccer (AE), American football, immigrant, dish, recipe, mac and cheese, specialty, deep-dish pizza, ice hockey, public; baseball, basketball (Fremdwörter).
- **schule-usa:** grade, homeroom, attendance, announcement, class period, elective, locker, tax, sports practice; freshman, sophomore, junior, senior (Merke).
- **feste-usa:** federal holiday, turkey, corn, pumpkin pie, harvest, feast, to invite, Pilgrims, Wampanoag, National Day of Mourning, Declaration of Independence, fireworks, parade, colors (AE); shown (im Hörsatz).

## Hörliste

30 Hörsätze (`bf_emma`, `regen_audio.py`, Datei `audio-texte-k1.json`). **Niemand hat die Dateien angehört.** Erzeugt und technisch geprüft (Tags, Text) vom Skript; das Gehör der Ersteller:in steht aus.

Sätze mit einsilbigem Schlusswort (gezielt hören auf Fehllaut am Ende):
- usa-staedte: „Millions of people visit Central Park every year.“ (year); „New York was the capital of the country for a short time.“ (time); „People speak many languages in New York.“ (York); „France gave the Statue of Liberty to the United States.“ (States); „The District of Columbia is not a state.“ (state)
- kanada: „Canada is the second biggest country in the world.“ (world)
- jugend-usa: „Apple pie is a typical American dish.“ (dish); „Chicago has a famous basketball team.“ (team); „Each basketball team has five players on the court.“ (court)
- schule-usa: „A school year is about nine months long.“ (long); „School teams often train after school.“ (school); „Most students eat lunch at school.“ (school)
- feste-usa: „Some people go to parades and American football games.“ (games)

Dip-Schnitt-Meldungen von `regen_audio.py` (gezielt hören, ob das Ende vollständig ist):
- „Some people go to parades and American football games.“ (75 ms)
- „French is a first language for many Canadians.“ (65 ms)
- „Students can choose some subjects.“ (45 ms)
- „Students in twelfth grade are called seniors.“ (65 ms)
- „The capital of the USA has many free museums.“ (75 ms)
- „France gave the Statue of Liberty to the United States.“ (95 ms, der größte Schnitt)
- „The District of Columbia is not a state.“ (25 ms)

Aussprache gezielt hören: „Washington“ kommt in keinem Hörsatz vor (D.C. bewusst vermieden: „The capital of the USA …“, „The District of Columbia …“). Wörter mit Namen: Ottawa, Toronto, Canadians, Michigan, Indigenous.

## Abweichungen vom Plan

- **Schulbus, locker (Quelle), homeroom:** Der Auftrag nannte „homeroom, locker, Fächer/Wahlfächer, Schulbus“. `Homeroom` und `Locker` wurden geöffnet und sind belegt, der Schulbus ließ sich nicht öffnen und entfiel.
- **Stundenplan:** statt einer Skizze mit Uhrzeiten eine Skizze der Reihenfolge eines Tages (Beispiel, ohne Zeiten), weil die Zeiten an jeder Schule anders sind.
- **Kanada-Schemakarte:** zwei Bilder (Erklärbild mit Hauptstadt und drei Städten; Aufgabenbild mit Markierungen für die drei Ozeane und die USA, die Ozeannamen kommen nur in der Aufgabe vor).
- **Wiederholungsseite:** zwei Kontrollfragen (Schule, Feste), eine Tabelle, ohne Datumsangaben.
- **Seitenvielfalt:** `kanada-verstehen` und `schule-verstehen` sind `single-choice` statt `true-false`, `jugend-fair` ist `multiple-choice` (Hinweis `explainer-page-variety`).
- **Selbsteinschätzung:** drei Schritte zu je vier Übungen (zwei je Inhaltsseite, ohne Wiederholungsseite und ohne Hör- und Sprechübungen).
- `chapter.yaml`: `pages` erweitert um `das-brauchst-du` an erster Stelle; `src/app.yaml` unverändert (enthält bereits `hello-america`).

## Fortschreibung Gesamtcheck (Stand 2026-11-25)

- **jugend-usa:** „twenty-four public beaches“ entfällt, jetzt „many public beaches“ (Chicago.txt: 24 öffentliche Strände an einer, 31 Sandstrände an anderer Stelle). Rückblick in feste-usa: „Deep-dish pizza is a specialty of Chicago.“ (Chicago.txt, jugend-usa). Rückmeldung zu „emigrants“ erklärt das Wort nicht mehr (Emigrant kommt erst in Kapitel 3).
- **feste-usa:** „Some Wampanoag say the feast was first only for the Pilgrims“ belegt durch `Thanksgiving__United_States_.txt` (Absatz „According to accounts by Wampanoag descendants, the harvest feast was originally set up for the Pilgrims alone“). Neu im Randglossar „Native Americans“ (United_States.txt: 3,7 Millionen Native Americans, rund ein Prozent, 574 anerkannte Stämme; Canada.txt: Indigenous peoples in Kanada); kanada-Merke grenzt ab: in Kanada Indigenous peoples, für die USA Native Americans. „American Indian“ kommt in Kapitel 1 nicht vor. Tabelle „Schulkalender · Feste in den USA“ jetzt zwei Spalten. Erwartete Antworten: „(on|at|for) Thanksgiving“, „(remembers|celebrates|commemorates)“.
- **schule-usa:** Hörsatz „A school year is about nine months long“ ist jetzt im Chat vorbereitet (Zeilen 14 und 15, Frage nach der Länge des Schuljahres; Quelle `High school in the United States`, siehe oben). „registration“ in der Tabelle erklärt (Homeroom-Artikel). „nine a.m.“ und „nine in the morning“ werden angenommen.
- **usa-ueberblick / usa-staedte:** Karte „Great Lakes“ heißt jetzt „Lake Michigan“ (Chat nennt Lake Michigan, Chicago.txt: Chicago am Lake Michigan; „one of the Great Lakes“ ist in den geöffneten Quellen nicht ausdrücklich belegt). Mexiko-Markierung auf x 44, y 86. „Das kannst du danach“ in usa-staedte nennt die Antwort der Vorfrage nicht mehr.
- **Bilder:** Kanada-Karte entzerrt (Ottawa, Toronto, Montreal mit Linien, Beschriftungen in den USA); Stundenplan endet bei 87 Prozent der Höhe (Badge).
- **Zurückgestellt (nicht Kapitel 1):** Dopplung football/soccer mit be-ae-wortschatz, neighbo(u)r mit be-ae-schreibung, Independence Day mit unabhaengigkeit-usa, „Congress“-Bedeutung (Kapitel 3; in usa-staedte jetzt „heute das Parlament der USA“): Kapitel 2 und 3 verweisen zurück. Keine neuen Hörsätze; Hörliste unverändert, alle 30 Dateien weiter nicht angehört.
