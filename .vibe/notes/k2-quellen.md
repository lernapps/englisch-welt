# Kapitel 2 `british-or-american`: Quellen, Wörter, Hörliste, Abweichungen

Stand: 2026-11-24. Alle Fakten sind eigene Sätze nach den Quellen (keine Sätze übernommen). Wikipedia-Texte stehen unter CC BY-SA, hier nur Fakten.

## Quellen je Seite (geöffnet per Wikipedia-API, englisch)

### `be-ae-wortschatz`
- Geöffnet: `Comparison of American and British English` (Klartext und, für die Tabellen, die geparste Fassung).
- Fakten daraus: pavement – sidewalk (footpath), petrol – gas (gasoline), lift – elevator, football in Großbritannien = association football, in den USA = American football, soccer = amerikanisches Wort für association football; biscuit (britisch auch für Cookies) – cookie; fall – autumn; holiday (britisch) – vacation (amerikanisch, für Ferienreisen); queue – line (Warteschlange); trousers – pants, in Großbritannien meint pants meist Unterhosen; car park – parking lot, bonnet – hood, boot – trunk, motorway – freeway (Tabelle Straßenverkehr); courgette – zucchini; hockey = in Großbritannien oft Feldhockey, in den USA meist Eishockey; gesprochenes britisches und amerikanisches Englisch sind meist gegenseitig verständlich.
- **Nicht geprüft:** flat – apartment steht nicht in dem geöffneten Artikel. Das Paar kommt aus dem „Ich kann“-Satz der Karte (`englisch.json`, `be-ae-wortschatz`). Der Wikipedia-Artikel `Apartment` konnte nicht geöffnet werden (HTTP 429, zwei Versuche). Hinweis: Der im Auftrag genannte Artikel `List of pairs of American and British English words` existiert nicht (API: „missing“); stattdessen `Comparison of American and British English`.
- Nicht aufgenommen, weil nicht belegt: crisps – chips, sweets – candy, rubbish – trash.

### `be-ae-aussprache`
- Geöffnet: `General American English`, `Received Pronunciation`, `Comparison of American and British English` (Abschnitt Pronunciation).
- Fakten: Die meisten amerikanischen Akzente sind rhotisch (r in allen Stellungen, zum Beispiel pearl, car, fort), die meisten Akzente Englands (RP) sind nicht rhotisch (r nur vor einem Vokal; stalk und stork, father und farther klingen gleich); amerikanisch t- und d-Flapping zwischen Vokalen (later, party; ladder und latter, metal und medal klingen gleich; bitter und bidder gleich in Nordamerika, nicht in England); britische Akzente sprechen t zwischen Vokalen anders (Glottalverschluss, behaucht); BATH-Vokal: /ɑː/ in bath und glass gilt in RP als richtig, viele Menschen im Norden Englands lehnen den langen Vokal ab; im amerikanischen Englisch hat bath den kurzen Vokal (TRAP/BATH-Vokal /æ/).
- Nicht geprüft und weggelassen: tomato (britisch /ɑː/, amerikanisch /eɪ/), weitere RP-Vokale. Australisch, schottisch, indisch: keine Stimme, nicht in diesem Kapitel.
- Lesehilfen („kah“, „kahr“, „bahth“, „bäth“, „bedder“, „stohk“, „stohrk“, „grahss“, „gräss“) sind eigene deutsche Annäherungen, kein Beleg der Quellen. Niemand hat sie mit den Hörproben abgeglichen.

### `be-ae-schreibung`
- Geöffnet: `American and British English spelling differences` (Klartext und geparste Tabellen).
- Fakten: -our – -or (colour, honour, humour, neighbour, favourite); -re – -er (centre, litre, theatre, fibre); -ise – -ize (organise, realise, recognise; -ize ist auch im Britischen verbreitet, die OUP empfiehlt es; Amerikanisch meidet -ise); verdoppeltes l (travelling, cancelled, labelled – traveling, canceled, labeled); jewellery – jewelry; advise, exercise mit -se in beiden Varietäten; tyre – tire, kerb – curb, plough – plow; grey (britisch) – gray (amerikanisch häufiger); programme – program (britisch programme, außer bei Computerprogrammen; amerikanisch program); Schüler sollen laut Artikel einheitlich schreiben.
- Nicht aufgenommen: defence – defense (steht im Artikel, aber nicht im Kapitel genutzt).

## Wörter außerhalb von A1 und A2 (Prüfliste `/tmp/gw.json`), je Seite erklärt
- `be-ae-wortschatz`: apartment, elevator, pavement, sidewalk, parking lot, gas, cookie, soccer, queue, vacation, pants (Randglossar); bonnet, hood, boot, trunk, motorway, freeway, courgette, zucchini, hockey (Merke und Bild, mit deutscher Bedeutung); Cornwall (Name).
- `be-ae-aussprache`: accent, vowel, voice message, silent, soft (Randglossar). Die Sätze der Hörpaare enthalten nur bekannte Wörter.
- `be-ae-schreibung`: Randglossar mit allen Wortpaaren (color, favorite, gray, neighbor, center, theater, organize, program, traveling); Rückblick mit full stop, period, railway, railroad, kerb, curb, plough, plow (mit deutscher Bedeutung in der Tabelle); Merke und Bild mit honour, litre, realise, cancelled, jewellery, tyre.

## Hörliste (nichts davon hat ein Mensch angehört)
Erzeugt mit `regen_audio.py` (schneidet das Ausklingen ab), `bf_emma` (britisch) und `af_sarah` mit `ACCENT=us`. Es gab keine Dip-Schnitt-Meldungen; bei allen Dateien meldete das Skript nur einen Schnitt des Ausklingens (95 bis 240 ms, höchstens 0,15 % Energie, die längste Kürzung bei „…after his bath.“ britisch).
Sätze, die auf ein einsilbiges Wort enden (bitte gezielt anhören):
- „The lift in our building is very slow.“ (slow)
- „We waited in a long queue at the bus stop.“ (stop)
- „The cars are in the car park behind the shop.“ (shop)
- „Autumn is my favourite time of the year.“ (year)
- „Her sister parked the car near the door.“ britisch und amerikanisch (door)
- „I wrote a better letter about the party.“ britisch und amerikanisch (party, zweisilbig)
- „He drinks a glass of milk after his bath.“ britisch und amerikanisch (bath)
- „My favourite colour is yellow.“ (zweisilbig)
- „The neighbours are travelling to the centre.“ (zweisilbig)
- „They organise a programme at the theatre on Friday.“ (Friday, zweisilbig)
- „The centre of the town is busy on Saturday.“ (zweisilbig)
- „We play football in the park at the weekend.“ (zweisilbig)
- „Is there a lift in your building?“ (zweisilbig)
- „The neighbors organize a program at the theater.“ amerikanisch (zweisilbig)
Zusätzlich anhören: ob die Hörpaare wirklich verschieden klingen (r in car, door, parked; weiches t in better, letter, party; kurzes a in bath bei `af_sarah`). Die Aufgaben „Welche Stimme?“ setzen das voraus; geprüft ist nur, welche Stimme erzeugt wurde, nicht der Klang.

## Abweichungen vom Plan
- Die Quelle `List of pairs of American and British English words` gibt es nicht; `Comparison of American and British English` ersetzt sie. flat – apartment bleibt nur aus der Karte belegt.
- Grey/gray und programme/program kommen aus der Tabelle der Schreibungsseite und stehen im Kapitel (Randglossar, Übungen).
- Die Seite `be-ae-aussprache` nutzt `direction: to-source` und `mode: choice` mit Audio für „Welche Stimme?“ (die Antwort „britisch/amerikanisch“ ist die deutsche Seite). Der Build nimmt es an; das Verhalten in der App wurde im Browser nur als Anzeige gesehen (Auswahlfeld „...“), nicht durchgespielt.
- Je Seite ein Schemabild (`be-ae-auto`, `be-ae-klang`, `be-ae-buchstaben`, Skript `bilder_k2.py`), damit die Seiten etwas zum Anschauen haben.
- Wiederholungsseite hat zwei Kontrollfragen und keinen `weiter`-Abschnitt.
