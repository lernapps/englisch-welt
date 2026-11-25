---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Englisch in der Welt: USA, Kanada und Australien“: Explainer (Einheiten-App `subject: englisch`, Format 2, Sprache Deutsch, englische Texte). Auftrag: Issue lernapps/apps#484 (Epic lernapps/apps#489, Konventionen dort). Umfang der ersten Version: alle fünf Kapitel (Stufe 7-8: Kapitel 1 bis 3, Stufe 9-10: Kapitel 4 und 5), 21 Bausteine und vier Wiederholungsseiten. **Stand des Baus:** siehe die Liste „Gebaut“ am Ende von „Content structure“ (sie wird mit jeder Seite fortgeschrieben).

## Curriculum

Englisch als erste Fremdsprache, Stufe 7-8 und 9-10 der Karte. Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`, Einheiten-App über die Stränge `landeskunde`, `wortschatz`, `texte`, `aussprache`). Vorwissen: Hello, Millbrook! (#470), Großbritannien (#478), Klang und Schrift (#482), Geschichten (#479). Nicht hier: Großbritannien und London (#478), Schulsysteme mit Abschlüssen (#486), Politik als Diskussionsthema und Bewerbung (#487, #486), eigene Videos, Fotos.

## Competencies

Alle 21 sind Lücken der Karte (`practisedBy` leer). Eine Seite je Baustein; die „Ich kann“-Sätze stehen wie in der Karte in der Seitendatei (nicht umformulieren). `competencies:` nennt Karten-Ids; Wiederholungsseiten haben `recap:` und keine `competencies`.

1. Kapitel `hello-america` („Hello, America!“, Band 7-8): `das-brauchst-du` (`recap: [englisch/schule-uk, englisch/feste-uk]`), `usa-ueberblick` (Musterseite), `usa-staedte`, `kanada`, `jugend-usa`, `schule-usa`, `feste-usa`.
2. Kapitel `british-or-american` („British or American?“, 7-8): `das-brauchst-du` (`recap: [englisch/vokale, englisch/laut-buchstabe]`), `be-ae-wortschatz`, `be-ae-aussprache`, `be-ae-schreibung`.
3. Kapitel `wie-die-usa-entstanden` („Wie die USA entstanden“, 7-8, keine Wiederholungsseite): `mayflower`, `einwanderung-usa`, `unabhaengigkeit-usa`, `westen-native-americans`, `politik-usa`.
4. Kapitel `freiheit-gleichheit` („Freiheit und Gleichheit“, 9-10): `das-brauchst-du` (`recap: englisch/vielfalt-gb`), `sklaverei-buergerkrieg`, `gesellschaft-politik`, `buergerrechtsbewegung`, `migration-heute`.
5. Kapitel `englisch-weltweit` („Englisch weltweit“, 9-10): `das-brauchst-du` (`recap: [englisch/britische-inseln, englisch/gruss-hoeflichkeit]`), `australien`, `weitere-varietaet`, `kulturelle-konventionen`.

Seiten-Id = Karten-Id. Reihenfolge nach `requires`: jedes `requires` steht auf einer früheren Seite oder auf der Wiederholungsseite. Übungs-IDs: Präfix = Seite (`usa-karte`), Diktat `<präfix>-hoeren`, Nachsprechen `<präfix>-nachsprechen`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`, Daten `src/data/`, Bilder `src/images/`, Audio `src/audio/`.
- Jede Inhaltsseite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Vorwissen-Frage als erste leichte Aufgabe, „Das kannst du danach“, Verbindung zur Seite davor), `lesen` (ein Lesestück in zwei bis drei kurzen Abschnitten, Zeilen nummeriert, Randglossar als `vocabulary`-Block), `verstehen` (drei Stufen: Verstehen, Belegen mit Zeile, Meinung), `neu` (Bild oder Karte, Merke-Kasten, höchstens eine Wörtertabelle), `uebung` (mindestens vier Übungen, leicht → schwer, wechselnde Arten), `anwenden` (`speaking-task`, `open-task`), `weiter` (nächster Halt auf der Weltkarte; am Kapitelende ein Rückblick „Schulkalender · …“). Wiederholungsseiten: nur `einstieg` mit Text, höchstens einer Tabelle, höchstens zwei Kontrollfragen, Links zur Karte.
- Länge: höchstens 350 Wörter Erklärtext (das Lesestück zählt nicht), höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken, höchstens etwa 25 Items und 10 Übungen. Lesestück Stufe 7-8: etwa 150 bis 300 Wörter, Stufe 9-10: 300 bis 600.
- Je Kapitel eine Selbsteinschätzung (`chapter.yaml`, zwei Übungen je Seite).
- **Geschichte:** Die Weltkarte ist der rote Faden: Jede Seite ist ein „Halt“ (Station einer Reise über die Karte); die Zeitachse der USA wächst in Kapitel 3 und 4. Stufe 7-8 (Kapitel 1 bis 3): Sophie (Hauptfigur) chattet mit **Jayden**, einem Jugendlichen aus Chicago; im Klassenraum sprechen Mr Hill, Ellie, Amir, Peter als Stimmen. Der Seitentext führt keine Figur ein (keine Altersangaben, keine Familie, kein Datum); die Startseite nennt nur Namen und Rollen. Jayden schreibt amerikanisch (color, apartment), Sophie britisch. Stufe 9-10 (Kapitel 4 und 5): realer Fall mit Daten, Quellen und einer Entscheidung, keine erfundenen Kinder mehr; Figuren erscheinen dort nicht mehr (höchstens „Sophie“ als Leserin einer Aufgabe, ohne Handlung). Kein Lagerraum, kein Schulfest, keine Ausstellung als Handlung.
- **Zeitachse:** Datendatei `src/data/usa-zeitachse.yaml` (jedes Ereignis einmal: Jahr, Titel, kurze Fassung, Perspektive(n), Quelle), Kapitel 3 und 4 lesen sie mit `timeline`.
- Heikle Themen (Geschichte der USA, Sklaverei, Native Americans, Migration, Politik): sachlich, mehrere Perspektiven (je Ereignis „Wer gewinnt, wer verliert?“), ohne Bewertung der Gegenwart, keine erfundenen Details zu Religion oder Herkunft realer Gruppen, kein Belehren. Zahlen und Jahre nur mit geöffneter Quelle.
- Anrede „du“.
- **Gebaut (alle fünf Kapitel):**
  - Kapitel 1 `hello-america`: `das-brauchst-du` (Wiederholung schule-uk, feste-uk), `usa-ueberblick` (Musterseite), `usa-staedte`, `kanada`, `jugend-usa`, `schule-usa`, `feste-usa` (letzte Seite mit Rückblick „Schulkalender · Rückblick Kapitel 1“). Bilder `usa-schema-natur`, `usa-schema-aufgabe` (in `make_images.py`), `usa-schema-staedte`, `kanada-schema`, `kanada-schema-aufgabe`, `schule-stundenplan` (`bilder_k1.py`). Audio `audio-texte.json` (6 Sätze Musterseite) und `audio-texte-k1.json` (30 Sätze). 3 Schritte Selbsteinschätzung.
  - Kapitel 2 `british-or-american`: `das-brauchst-du` (Wiederholung vokale, laut-buchstabe), `be-ae-wortschatz`, `be-ae-aussprache` (Hörpaare `bf_emma` und `af_sarah`), `be-ae-schreibung` (Rückblick Kapitel 2). Bilder `bilder_k2.py` (`be-ae-auto`, `be-ae-klang`, `be-ae-buchstaben`). Audio `audio-texte-k2.json` (13 Sätze GB) und `audio-texte-k2-us.json` (4 Sätze US).
  - Kapitel 3 `wie-die-usa-entstanden`: `mayflower`, `einwanderung-usa`, `unabhaengigkeit-usa`, `westen-native-americans`, `politik-usa` (Rückblick Kapitel 3, `timeline` aus `src/data/usa-zeitachse.yaml` mit 12 Ereignissen). Bilder `bilder_k3.py` (Karten, Zeitachse in Teilen, Gewalten). Audio `audio-texte-k3.json` (30 Sätze).
  - Kapitel 4 `freiheit-gleichheit`: `das-brauchst-du` (Wiederholung vielfalt-gb), `sklaverei-buergerkrieg`, `gesellschaft-politik`, `buergerrechtsbewegung` (`timeline` aus `src/data/usa-zeitachse-heute.yaml`, 14 Ereignisse), `migration-heute` (Rückblick Kapitel 4). Stufe 9-10: Sachtexte 326 bis 475 Wörter, Quotes aus National Archives (gemeinfrei). Bilder `bilder_k4.py`. Audio `audio-texte-k4.json` (24 Sätze).
  - Kapitel 5 `englisch-weltweit`: `das-brauchst-du` (Wiederholung britische-inseln, gruss-hoeflichkeit), `australien`, `weitere-varietaet` (Text und Wortliste, keine nachgeahmten Akzente), `kulturelle-konventionen` (Gesprächsszenen mit Hörfassung, Rückblick Kapitel 5). Bilder `bilder_k5.py`. Audio `audio-texte-k5.json` (17 Sätze GB) und `audio-texte-k5-us.json` (1 Satz US).
  - Insgesamt 21 Inhaltsseiten und 4 Wiederholungsseiten, 125 Hörsätze, Selbsteinschätzung in jedem Kapitel. Quellen, Wörter außerhalb von A1/A2 je Seite, Hörlisten und Abweichungen je Kapitel: `.vibe/notes/k1-quellen.md` bis `k5-quellen.md` (gehören zum Inhaltsführer; beim Erweitern eines Kapitels dort fortschreiben).
- Zeitachsen-Daten: zwei Dateien, `src/data/usa-zeitachse.yaml` (Kapitel 3) und `src/data/usa-zeitachse-heute.yaml` (Kapitel 4); das Schema erlaubt kein Quellenfeld, die Quelle steht am Ende des Ereignistexts oder in den Notizen. `timeline` zeigt immer die ganze Datei.
- Stufe 9-10: der Hinweis `explainer-text-load` („mehr als 350 Wörter Text“) bleibt bei den Seiten mit Lesestück (300 bis 600 Wörter) bestehen, weil die Konventionen das Lesestück nicht zu den 350 Wörtern Erklärtext zählen.

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, sentence.
- Karten-Begriffe, immer dieselben: **Weltkarte** (der rote Faden der App), **Halt** (eine Seite auf der Reise), **Schemakarte** (selbst gezeichnet, „nicht genau nach Maßstab“), **Zeitachse** (die Datendatei und der `timeline`-Block), **Lesestück**, **Randglossar**.
- Britisches Englisch in allen eigenen Sätzen (favourite, colour, centre); amerikanische Schreibung nur dort, wo sie das Thema ist oder in Jaydens Chatzeilen, und dann markiert („Jayden schreibt amerikanisch“). Englische Aufgaben enthalten kein deutsches Wort. Englisches mit deutscher Bedeutung, wo ein Wort neu ist.
- Länder und Begriffe: USA = die Vereinigten Staaten von Amerika (nicht „Amerika“); Native Americans (First Nations und Inuit nur für Kanada); Aborigines und Torres-Strait-Insulaner für Australien; Varietät des Englischen, nicht „Dialekt“ und nie „falsches Englisch“.
- Aussprache: Lesehilfe in deutscher Annäherung (`gud-BAI`), betonte Silbe in Großbuchstaben, keine Lautschrift (IPA gehört zu #482).

## Exercise patterns

Aufbau leicht → schwer: wählen/zuordnen → Lücke → schreiben mit Cue → eigene Aussage. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten mit `(a|b)`; `punctuation: ok`. Die Arten wechseln von Seite zu Seite.

- Karte und Fakten: `matching`, `single-choice`, `true-false` mit Begründung; Zeitachse: `ordering` und `timeline`; Quelle: `quote` mit `origin`, `source`, `licence` und `single-choice` zur Aussage.
- Lesestück: Aufgaben in drei Stufen (Verstehen: `single-choice`, `true-false`, `matching`; Belegen: `single-choice` „Welche Zeile belegt …?“; Meinung: `open-task` mit Punkten oder `single-choice` mit Begründung).
- BE/AE: Zuordnen in zwei Spalten (`matching`), mode `choice`, mode `table` (Regelmuster ableiten), Diktat mit zwei Stimmen.
- Perspektiven: „Wer sagt das?“ (`single-choice`), Quellenvergleich (zwei kurze Aussagen, welche passt zur Frage).
- Form: mode `choice`, `write` mit `cue`, `gap`; Diktat `language-task` mit `audio` (höchstens drei Sätze), Nachsprechen `speaking-task`, freies Schreiben `open-task`.
- Typische Fehler (jeweils `mistakes`): USA = America, Washington D.C. = Washington State, Toronto/Montreal als Hauptstadt, football/soccer, High School = Gymnasium, Thanksgiving = Erntedank, pavement/sidewalk vertauscht, -ise im AE, Mayflower = Kolumbus, Declaration = Verfassung, Kongress = Präsident, Native Americans nur Vergangenheit, nur eine Ursache des Bürgerkriegs, Einwanderung = Flucht, Hauptstadt Sydney, Varietät = Dialekt = falsch.
- Keine Komponente (`prefer-built-in-block`); jede Tatsache steht einmal in ihrer Seite oder in `usa-zeitachse.yaml`.

## Figures

- Eigene Zeichnungen, `CC-BY-4.0`, Quelle „eigene Zeichnung“, `src/images/`, erzeugt vom Skript `.agents/skills/app-content/scripts/make_images.py` (neues Bild: Funktion ergänzen und Skript starten, nie die SVG von Hand ändern). Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox, bei 360 px lesbar. Skizzen in `.vibe/sketches/`.
- Karten (USA, Kanada, Australien, Welt): **Schemakarten**, selbst gezeichnet, „nicht genau nach Maßstab“ in Alt-Text und Bildunterschrift; nichts aus einem Atlas oder aus Wikipedia kopiert; Lage und Namen nach den geöffneten Quellen. Aufgabenbilder (`material`) zeigen andere Beschriftungen als die Bilder im Erklärteil (Buchstaben statt Namen).
- Keine Fotos und keine Videos (Lizenz und Quelle nicht geprüft). Bilder nur, wo sie etwas zeigen. `alt` sagt, was das Bild zeigt, nie die Lösung.
- Poster und Kalender sind `vocabulary`- oder `table`-Blöcke: „Klassenzimmer-Poster · …“ und „Schulkalender · Rückblick Kapitel …“.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json` (geöffnet 2026-11-24); Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2). Wörter außerhalb der Liste werden auf der Seite mit Bedeutung eingeführt und hier gelistet (keine Wörter listen, die nirgends vorkommen). Jede Faktenangabe steht mit geöffneter Quelle: Fakten, keine Sätze (CC BY-SA bei Wikipedia). Geöffnet am 2026-11-24 (englische Wikipedia, per API): `Canada`, `Australia`, `Chicago`, `Pilgrims (Plymouth Colony)`, `Thanksgiving (United States)`, `United States Declaration of Independence`, `American frontier`, `Slavery in the United States`, `Rosa Parks`, `Voting Rights Act of 1965`. Weitere Artikel werden je Seite einzeln und langsam geöffnet (HTTP 429 bei zu schneller Folge); was nicht lesbar war, ist als „nicht geprüft“ hier vermerkt und kommt nicht in den Text. Originaltexte (Declaration of Independence, Verfassung, Emancipation Proclamation, UDHR) als Fakten oder kurze Zitate mit Quelle und Lizenz. „I have a dream“ ist urheberrechtlich geschützt: nur Fakten, kein Zitat, keine Hörfassung. Nicht benutzt: BBC Newsround, Newsela, CommonLit, The Conversation, Jugendmagazine. VOA Learning English nur nach geöffneter Lizenzseite. Beispielsätze und Lesestücke sind eigene Texte nach Fakten. Audio: KI-Stimmen `bf_emma` (britisch) und `af_sarah` (amerikanisch), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert; für australisches, schottisches und indisches Englisch gibt es keine Stimme (Merkmale nur als Text und Wortliste, keine nachgeahmten Akzente). Material der Ersteller:in: keines. **Nicht geprüft / offen:** Artikel, die HTTP 429 lieferten, wurden nicht benutzt (Aussage entfiel); je Kapitel in `.vibe/notes/kN-quellen.md`: Indian English (nicht geöffnet, indisches Englisch fehlt), School bus, Thirteen Colonies, Wampanoag (eigener Artikel), Indian Removal Act, Homestead Acts, Transcontinental railroad, United States Congress, President of the United States, Apartment (flat – apartment nur aus der Karte). Zitate (Declaration, Emancipation Proclamation, Zusatzartikel) aus Wikipedia/National Archives, Lizenz gemeinfrei; der Wortlaut der Declaration stammt aus dem Wikipedia-Artikel, archives.gov wurde dafür nicht geöffnet. Die Lesehilfen in deutscher Annäherung (Kapitel 2, 5) sind eigene Annäherungen ohne Beleg. Zahlen in Kapitel 4 stehen so in den Wikipedia-Artikeln (Originalquellen Census/ONS nicht geöffnet).

## Adding a chapter or round

1. Baustein auf der Karte wählen; die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen.
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `lesen`, `verstehen`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` und `src/app.yaml` eintragen, Karten-Id als `competencies` setzen.
3. Karte oder Zeitachse in `bilder_<kapitel>.py` bzw. `src/data/usa-zeitachse*.yaml` erweitern; Poster um die Zeilen der Seite.
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 1 bis 3 ihrer Übungen in `selfAssessment` aufnehmen (Skill `lernapps-explainer-self-assessment`).
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in einer Liste `audio-texte-<kapitel>.json` (GB) oder `audio-texte-<kapitel>-us.json` (US, `VOICE=af_sarah ACCENT=us`), erzeugt mit `regen_audio.py` (schneidet das Ausklingen ab); anhören; Sätze nicht zwischen Seiten wiederholen, Namen am Satzende zweisilbig.
6. Wörter gegen den Grundwortschatz prüfen (`pruefe_seiten.py`), `npx --no -- lernapps check`, committen.

## Rules learned from mistakes

Aus den Konventionen Abschnitt 7 und 8 und den Vorgängern (#470 bis #482):
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen; eine Tabelle, die eine Übung beantwortet, steht nicht direkt darüber; die Antwort einer Frage steht nie im Absatz direkt darüber. Poster, Merke, Einstieg und Bild nennen andere Beispielsätze und Wörter als die Übungen darunter.
- Kein Hörsatz steht wörtlich oder fast wörtlich im Einstieg, Poster, Merke, Bildtext, Lesestück oder in einer Aufgabe derselben Seite (Skript `pruefe_seiten.py` prüft es).
- Distraktoren nur echte Lernerfehler, keine Unwörter; jeder Distraktor und jedes Fehlerbild hat eine eigene Meldung. Ein Einstiegs-`single-choice` hat mindestens drei Optionen.
- Höchstens eine kurze Wörtertabelle je Seite (Vokabelblock `vocabulary`); Seiten mit mehr als etwa 25 Items oder 10 Übungen kürzen.
- Englische Aufgaben enthalten kein deutsches Wort; der Cue ist englisch. Mit `(a|b)` gleichwertige Antworten zulassen; `punctuation: ok`.
- Audio: Hörsätze bleiben natürlich, kein Name und kein Wort nur wegen des Klangs anhängen; `regen_audio.py` schneidet das Ausklingen und den Fehllaut ab; Sätze, die auf ein einsilbiges Wort enden, stehen in der Hörliste. Lesestücke nur in kurzen Abschnitten als Audio. „Ding“ nur für Gegenstände, nie für Menschen; „Besitzer“ nur für Gegenstände.
- Keine Figuren-Einführung im Seitentext (keine Altersangaben, keine Familie, kein Datum); die Startseite nennt nur Namen und Rollen. In Kapitel 4 und 5 keine erfundenen Kinder.
- Jede Faktenangabe und jedes Zitat steht mit geöffneter Quelle in „Sources“; ohne Beleg kein Satz. Zitate exakt, mit Herkunft und Lizenz.
- Geschichte und Gesellschaft: mehrere Sichtweisen, keine Bewertung der Gegenwart, keine erfundenen Details zu Religion oder Herkunft realer Gruppen.
- Die `competencies:` jeder Seite sind Karten-Ids (nicht Seitentitel); Wiederholungsseiten haben keine.
- Vorlage: `ordering` zeigt Auswahlfelder, `accepted` einer Sprach-Aufgabe wirkt nicht (Gruppen `(a|b)`), im Modus `choice` zeigt die App `mistakes` nicht, `punctuation: hint` meldet bei richtiger Antwort „Achte auf die Satzzeichen“ (`punctuation: ok`).

## Hörliste

Alle 125 Sätze sind mit `regen_audio.py` (Ausklingen und Fehllaut abgeschnitten) erzeugt. Die Orchestrator-Session bestätigt das Hörurteil in Namen der Ersteller:in; die Listen der Sätze mit einsilbigem Schlusswort und der Dip-Schnitte stehen je Kapitel in `.vibe/notes/kN-quellen.md`, Abschnitt „Hörliste“. **Gezielt hören:** Musterseite: „Hawaii is far from the other states.“, „The United States has fifty states.“ (Schluss states), „Alaska has very high mountains.“ (Dip-Schnitt 75 ms). Kapitel 1: „France gave the Statue of Liberty to the United States.“ (Dip 95 ms, größter Schnitt), „Some people go to parades and American football games.“ (75 ms). Kapitel 2: Hörpaare `bf_emma`/`af_sarah` (klingen die r, das weiche t und das kurze a hörbar verschieden?), Schluss slow, stop, shop, year, door, bath. Kapitel 3: Squanto, Massachusetts, Cherokee, „Each senator is elected for six years.“, Dip-Schnitte bei countries, questions, visitors, languages, judges, representatives. Kapitel 4: acht Sätze mit Dip-Schnitt 45 bis 85 ms (Liste in `k4-quellen.md`). Kapitel 5: „…the sixth largest country in the world.“, „…kilometres long.“, „I am sorry, I did not catch your name.“, die US-Zeile „Yes, please. Water would be wonderful.“.
