---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Plan: englisch-welt, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-24. Explore, Plan, Code, Commit.*

## Goal

Lernende der Stufen 7-8 und 9-10 lernen die englischsprachige Welt außerhalb Großbritanniens kennen (USA, Kanada, Australien), erzählen Abschnitte der Geschichte der USA, erkennen Unterschiede zwischen britischem, amerikanischem und weiteren Varietäten des Englischen und üben angemessenes Verhalten in Gesprächen mit anderen Kulturen. Alle 21 Bausteine des Issues lernapps/apps#484 werden geübt, mit Lesestück, Aufgaben in drei Stufen und Schreib- oder Sprechauftrag je Seite.

## Key decisions

- Archetyp: `explainer` (Einheiten-App `subject: englisch`, Format 2): Lernende lesen Seiten mit Lesestück und üben auf jeder Seite; kein Spiel, keine Zeitnahme. `quiz` reicht nicht (Erklärung und Lesestück), `interactive` nicht nötig.
- Umfang: ganzer Explainer, 5 Kapitel, 21 Bausteine; dazu 4 Wiederholungsseiten (`recap`) für Bausteine anderer Explainer: Kapitel 1 (schule-uk, feste-uk), Kapitel 2 (vokale, laut-buchstabe), Kapitel 4 (vielfalt-gb), Kapitel 5 (britische-inseln, gruss-hoeflichkeit). Kapitel 3 braucht keine (usa-ueberblick steht in Kapitel 1).
- Figuren: Sophie (Hauptfigur) und die bekannten Figuren der Reihe; neu **Jayden** aus Chicago, Sophies Chat-Freund. Stufe 7-8 (Kapitel 1-3): Chats, kurze Dialoge, Lesestücke. Stufe 9-10 (Kapitel 4-5): reale Fälle mit Daten, Quellen und Entscheidung, keine erfundenen Kinder; Personen der Geschichte (Rosa Parks, Martin Luther King) nur mit belegten Fakten.
- Keine Figuren-Einführung im Seitentext (keine Alter, Familie, Daten); die Startseite nennt nur Namen und Rollen.
- Sprache der Seiten: Deutsch, englische Texte, britische Rechtschreibung in eigenen Texten; amerikanische Schreibung nur dort, wo sie das Thema ist und markiert (Jayden schreibt amerikanisch).
- Audio: `bf_emma` für britische Sätze; für die amerikanische Gegenprobe in Kapitel 2 `af_sarah` (erlaubt, nach Rücksprache). Keine Stimme für Australisch, Schottisch, Indisch: siehe Frage an die Orchestrator-Session (guess: Merkmale dieser Varietäten als Text und Wortliste, Hörsätze nur in GB/US).
- Videoszenen (Kapitel 5): keine eigenen Videos möglich; (guess) kurze Gesprächsszenen als Text und Hörszene (bf_emma/af_sarah), kein Video.
- Karte und Zeitachse: selbst gezeichnete Schemakarten (SVG, Skript wie im Vorgänger), `timeline`-Blöcke aus Datendatei `src/data/`.
- Kein Vue-Bauteil (`prefer-built-in-block`).

## Notes

**Karte:** Fach `englisch`, Fokus `competency`, Einheiten-App; Stränge `landeskunde` (die meisten), `wortschatz`/`texte`/`aussprache` (Kapitel 2, 5). Alle 21 Bausteine sind Lücken der Karte (`practisedBy` leer), Bänder 7-8 (K1-3) und 9-10 (K4-5). `competencies:` sind Karten-Ids.

**Kapitel und Seiten** (Ordner · Seite → Karten-Id; `requires` außerhalb der App → Wiederholung)
1. `hello-america` Hello, America!: `das-brauchst-du` recap [englisch/schule-uk, englisch/feste-uk] · `usa-ueberblick` · `usa-staedte` (req usa-ueberblick) · `kanada` · `jugend-usa` · `schule-usa` (req schule-uk, Recap) · `feste-usa` (req feste-uk, Recap)
2. `british-or-american` British or American?: `das-brauchst-du` recap [englisch/vokale, englisch/laut-buchstabe] · `be-ae-wortschatz` · `be-ae-aussprache` (req vokale) · `be-ae-schreibung` (req laut-buchstabe; laut-buchstabe hat noch keine App → Recap)
3. `wie-die-usa-entstanden` Wie die USA entstanden: `mayflower` · `einwanderung-usa` · `unabhaengigkeit-usa` · `westen-native-americans` · `politik-usa` (Reihenfolge nach requires; keine Wiederholung)
4. `freiheit-gleichheit` Freiheit und Gleichheit: `das-brauchst-du` recap [englisch/vielfalt-gb] · `sklaverei-buergerkrieg` · `gesellschaft-politik` · `buergerrechtsbewegung` · `migration-heute` (req vielfalt-gb, Recap; einwanderung-usa steht in K3)
5. `englisch-weltweit` Englisch weltweit: `das-brauchst-du` recap [englisch/britische-inseln, englisch/gruss-hoeflichkeit] · `australien` · `weitere-varietaet` (req be-ae-* aus K2) · `kulturelle-konventionen`

**Seitenform (Konventionen Abschnitt 8):** je Inhaltsseite ein Lesestück (K1-3 etwa 150-300 Wörter, K4-5 300-600; zählt nicht zu den 350 Wörtern Erklärtext). Abschnitte: `einstieg` (Vorwissen-Frage, Ziel), `lesen` (Lesestück in Abschnitten mit Randglossar als Tabelle/Glossar), `verstehen` (Aufgaben in drei Stufen: Verstehen, Belegen mit Zeile, Meinung), `neu` (Merke, höchstens eine Wörtertabelle), `uebung`, `anwenden` (Schreib- oder Sprechauftrag), `weiter`. Höchstens etwa 25 Items, höchstens 10 Übungen.

**Wie Lernende dorthin kommen** (Kurzform; Details bei „Content method“): Landeskunde: Lesestück → Belegfragen (Zeile nennen) → zuordnen/ordnen/Karte lesen → eigene Aussage schreiben. Wortschatz BE/AE: Karten in zwei Spalten sortieren (`matching`), Chat-Lücken, dann selbst übertragen. Aussprache: Hörsatz-Paare (bf_emma/af_sarah), erkennen, nachsprechen. Schreibung: Regelmuster ableiten (-our/-or, -re/-er, -ise/-ize) aus Wortpaaren, dann anwenden. Geschichte: Zeitachse ordnen (`ordering`, `timeline` aus Datendatei), je Ereignis „Wer gewinnt, wer verliert?“ (mehrere Perspektiven), Quelle mit Herkunft (`quote`). Kulturelle Konventionen: Gesprächsszenen lesen/hören, angemessene Antwort wählen und begründen.
Typische Fehlvorstellungen (je eine eigene Rückmeldung): USA = Amerika; Kanada nur englisch; Washington = Washington D.C. und der Staat; Thanksgiving = Erntedank/Weihnachten; High School = Gymnasium; American football = Fußball (soccer); grade/high school-Stufen; BE/AE: pavement ≠ sidewalk vertauscht, football/soccer; -ise gilt auch im AE; „americanisch“ als falsch bewerten; Pilgerväter = erste Menschen in Amerika; Mayflower = Kolumbus; Declaration = Verfassung; Kongress = Präsident; Native Americans nur als Vergangenheit; Bürgerkrieg nur über Sklaverei vs. Süd (mehrere Ursachen, sachlich); Rosa Parks war müde (vereinfachte Legende) → nur belegte Fakten; Migration: Einwanderung = Flucht; Australien: Aborigines = ein einziges Volk, Hauptstadt Sydney; Varietät = falsches Englisch; Small Talk überall gleich.

**Umfang:** 21 Bausteine, 4 Wiederholungsseiten, je Seite 4 bis 6 Hörsätze (Diktat, Nachsprechen, Kapitel 2 mehr), Schemakarten und Zeitachsen als SVG, Datendatei `src/data/usa-zeitachse.yaml` (Ereignisse einmal), Selbsteinschätzung je Kapitel. **Nicht:** Schulsysteme mit Abschlüssen (#486), Großbritannien und London (#478), eigene Videos, Fotos (Lizenz nicht geprüft), Bevölkerungszahlen ohne Beleg. Heikle Themen (Geschichte der USA, Sklaverei, Native Americans, Migration, Politik): sachlich, mehrere Perspektiven, ohne Bewertung der Gegenwart, keine erfundenen Details zu Religion oder Herkunft realer Gruppen.

**Quellen (Fakten, keine Sätze):** Karte `https://lernapps.net/apps/map/englisch.json` (geöffnet 2026-11-24); Grundwortschatz. Wikipedia (en), per API am 2026-11-24 geöffnet: geöffnet: Canada, Australia, Chicago, Pilgrims (Plymouth Colony), Thanksgiving (United States), United States Declaration of Independence, American frontier, Slavery in the United States, Rosa Parks, Voting Rights Act of 1965. **Nicht geprüft (HTTP 429):** United States, New York City, Washington D.C., Official bilingualism in Canada, Independence Day, Mayflower, Ellis Island, Boston Tea Party, Constitution, American Civil War, Martin Luther King Jr., Civil Rights Movement, History of Australia, Aboriginal Australians, Varietäten-Artikel; sie werden beim Bau der jeweiligen Seite einzeln und langsam geöffnet (kein Scraper, keine Schleife) oder die Aussage entfällt. Weitere Quellen: Klexikon und Library of Congress/National Archives (Originaltexte: Declaration, Verfassung, Rede „I have a dream“ nur als Faktenbeleg, Zitate nur kurz und mit Quelle, Lizenz vorher lesen); VOA Learning English nur nach Prüfung der Lizenzseite. Keine Texte aus BBC Newsround, Newsela usw.

**Offene Punkte für die Orchestrator-Session:** (1) Hörproben für australisches, schottisches, indisches Englisch gibt es nicht (nur US/GB-Stimmen erlaubt); (2) Videoszenen in Kapitel 5 als Text/Hörszene; (3) Stufe 7-8 Kapitel 3 mit der Frage „Wer gewinnt, wer verliert?“ und Native-American-Perspektiven: eigene Quellen, keine Bilder Dritter.

## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [x] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.
      Creator: Orchestrator-Session (in der Rolle der Ersteller:in): Recherche bestätigt; Kapitel 2 bf_emma gegen af_sarah; Kapitel 5 Varietäten als Text und Wortliste, Hörsätze nur GB/US; Videoszenen als Gesprächsszenen mit Hörfassung; 429-Quellen pro Seite langsam öffnen oder Aussage weglassen.

### Answers

- Goal: siehe Issue #484 (Leitidee): Ich kenne die englischsprachige Welt außerhalb Großbritanniens, kann Länder, Geschichte und Gesellschaft beschreiben und höre, wie verschieden Englisch klingt. (Quelle: Auftrag, beantwortet von der Orchestrator-Session in der Rolle der Ersteller:in.)
- Learners: Englisch als erste Fremdsprache, Stufe 7-8 (Kapitel 1-3) und 9-10 (Kapitel 4-5); Vorwissen: Hello, Millbrook!, Großbritannien (#478), Klang und Schrift (#482).
- Look and feel: fixed by the archetype (ruhig wie ein Arbeitsblatt, Dunkelmodus folgt dem Gerät).
- Content: aus Karte, Issue, eigenen Texten nach Fakten (Konventionen Abschnitt 8); kein Material der Ersteller:in.
- Amount: ganzer Explainer, 5 Kapitel, 21 Bausteine (Startnachricht).
- Languages: Deutsch (Erklärungen), Englisch (Texte, Beispiele), Konventionen Abschnitt 4.
- Hurdles, Terms, Model and focus, Finding the app: Konventionen und Issue; Terminologie wie Vorgänger (Ausdruck, Halt, Karte, Zeitachse); Vorbild die fertigen Vorgänger #478, #479, #482, #471; Suchbegriffe: Englisch Landeskunde USA Kanada Australien, British vs American English, Geschichte der USA (guess).
- Interview: nicht an die Ersteller:in gerichtet; alles stammt aus dem Auftrag und den Konventionen.

<!-- topics -->

- Goal: what learners do in the app, what they learn.
- Learners: subject, school year, prior knowledge.
- Model and focus: an app of the catalog (https://lernapps.net/apps/llms.txt) as model; what matters most (exercises,
  visualisations, game feel).
- Hurdles: misconceptions and mistakes of the learners; the creator's examples and experiments.
- Content: who writes it (creator, you, from sources); own material (worksheets, tests).
- Amount: how much content in the first version; what comes later.
- Languages: German only, or German and English. Never English only.
- Look and feel: calm like a worksheet, or like a game (colours, praise, effects); dark mode.
- Terms: the creator's words for the main things in the app, used everywhere.
- Finding the app: what teachers and parents would search for.

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [x] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [x] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [x] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [x] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [x] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [x] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Orchestrator-Session (in der Rolle der Ersteller:in): Plan bestätigt; nach dem Muster-Checkpoint dürfen die übrigen Kapitel mit Sub-Agenten in eigenen Worktrees entstehen, gemeinsame Dateien bleiben bei mir.

### Content method

**Seitenform (alle Inhaltsseiten), gleiche Abschnitts-Ids in dieser Reihenfolge:** `einstieg` (Vorwissen-Frage als erste leichte Aufgabe, „Das kannst du danach“, Verbindung zur Seite davor), `lesen` (ein Lesestück in 2 bis 3 kurzen Abschnitten, Randglossar als `vocabulary`-Block „Randglossar · …“, Zeilen nummeriert), `verstehen` (drei Stufen: Verstehen, Belegen mit Zeile, Meinung), `neu` (Bild/Karte, Merke-Kasten, höchstens eine Wörtertabelle als `vocabulary`), `uebung` (mindestens vier Übungen, leicht → schwer, wechselnde Arten), `anwenden` (`speaking-task` und/oder `open-task` mit Punkten), `weiter` (nächster Halt). Höchstens etwa 25 Items, höchstens 10 Übungen, höchstens 350 Wörter Erklärtext (das Lesestück zählt nicht). Wiederholungsseiten: nur `einstieg` mit `recap:`, den „Ich kann“-Sätzen der Karte, höchstens einer Tabelle und höchstens zwei Kontrollfragen.

**Figuren und Form:** Stufe 7-8: Lesestücke als Chats Sophie ↔ Jayden, kurze Dialoge im Klassenraum (Mr Hill, Ellie, Amir, Peter, Mrs Parker nur als Stimmen, ohne Einführung), Berichte; keine Altersangaben, keine Familie, kein Datum im Seitentext; ein Bild nur wo es etwas zeigt (Schemakarten, Zeitachse). Stufe 9-10: Sachtexte mit Daten, Quellenvergleich, Entscheidung („Welche Quelle nutzt du für …?“), keine erfundenen Kinder.

**Muster je Baustein** (je Übung `mistakes` mit eigener Meldung, `hint`, `(a|b)`, `punctuation: ok`; Übungsarten wechseln):
- usa-ueberblick (Musterseite): Schemakarte mit Regionen, Alaska/Hawaii; `matching` Region ↔ Lage; Karte lesen; Satz schreiben (`language-task`); Diktat; Fehler: USA = America, Hawaii in Asien.
- usa-staedte: Chat; nummerierte Orte; `matching` Sehenswürdigkeit ↔ Stadt; Lückentext; Fehler: Washington D.C. = Washington State, New York = Hauptstadt.
- kanada: Lesestück, zwei Amtssprachen, First Nations und Inuit sachlich; `true-false` mit Begründung; Fehler: nur Englisch, Toronto = Hauptstadt.
- jugend-usa: Chat über Freizeit, Sport, Essen; Vergleich Sophie/Jayden (`matching`); `ordering`; Fehler: football/soccer, Klischees als Alltag.
- schule-usa: Stundenplan (Tabelle), Begriffe grade, locker; Vergleich mit Millbrook; mode `choice`; Fehler: High School = Gymnasium.
- feste-usa: Thanksgiving, Independence Day; Kalender „Schulkalender · …“; `ordering`; Fehler: Thanksgiving = Erntedank, Datum.
- be-ae-wortschatz: Chat; Karten zweispaltig (`matching`); Lücke; Übersetzen; Fehler: vertauschte Wörter.
- be-ae-aussprache: Hörpaare bf_emma/af_sarah als Diktat; Merkmale in Wortliste mit Lesehilfe (keine IPA); Nachsprechen; Fehler: amerikanisch = falsch.
- be-ae-schreibung: Regelmuster aus Wortpaaren ableiten, mode `table`, Korrektur; Fehler: -ise im AE.
- mayflower, einwanderung-usa, unabhaengigkeit-usa, westen-native-americans, politik-usa: Lesestück (Bericht), `timeline` aus `src/data/usa-zeitachse.yaml`, `ordering`, `matching`, je Ereignis „Wer gewinnt, wer verliert?“ mit mehreren Perspektiven; Zitate nur kurz mit Quelle und Lizenz; politik-usa mit `labelled-figure` der drei Gewalten; Fehler: Mayflower = Kolumbus, Declaration = Verfassung, Kongress = Präsident, Native Americans nur Vergangenheit.
- sklaverei-buergerkrieg, gesellschaft-politik, buergerrechtsbewegung, migration-heute: Sachtext 300 bis 600 Wörter, Zeitachse, Quellenvergleich, Zitat nur wo Lizenz klar (Verfassungs-/Gesetzestexte, UDHR; „I have a dream“ ist urheberrechtlich geschützt: nur Fakten, kein Zitat, keine Hörfassung); Daten nur belegt; Fehler: nur eine Ursache des Bürgerkriegs, Rosa Parks war nur müde (Legende), Einwanderung = Flucht.
- australien, weitere-varietaet, kulturelle-konventionen: Schemakarte, Zeitachse, Wortlisten mit Varietät, Gesprächsszenen mit Hörfassung (bf_emma/af_sarah, ohne nachgeahmten Akzent); `single-choice` angemessene Antwort mit Begründung; `open-task` Dialog; Fehler: Hauptstadt Sydney, Varietät = Dialekt = falsch.

**Daten:** `src/data/usa-zeitachse.yaml` (Ereignisse einmal: Jahr, Titel, Perspektive, Quelle; K3 und K4). Sonst keine Datendatei: jede Tatsache steht einmal in ihrer Seite.
**Bilder:** Skript `make_images.py` (SVG, Schemakarten „nicht genau nach Maßstab“, `CC-BY-4.0`, Quelle eigene Zeichnung), keine Fotos, keine Komponente.
**Audio:** `bf_emma` (GB), `af_sarah` (US) nur in Kapitel 2 und den Gesprächsszenen von Kapitel 5; je Seite vier bis sechs ganze Sätze, `regen_audio.py`, Hörliste im Inhaltsführer, kein Satz zweimal.
**Engagement:** Eröffnung: erste leichte Frage vor der Erklärung; Wechsel: lesen, zuordnen, hören, schreiben; Belohnung: Halt auf der Weltkarte, am Kapitelende „Schulkalender · …“-Rückblick; Geschichte: Chat von Sophie und Jayden, Karte und Zeitachse wachsen von Halt zu Halt; Wiederholung nur absichtlich.
**Weiterbauen:** Seite anlegen, in `chapter.yaml` und `src/app.yaml` eintragen, Karten-Id als `competencies`, Datendatei und Hörliste erweitern.

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [x] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [x] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [ ] Load skill `lernapps-explainer`.
- [ ] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [ ] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [ ] Musterseite hello-america/usa-ueberblick: Lesestück (Chat), Schemakarte der USA, Randglossar, Aufgaben in drei Stufen, Übungen, Diktat und Nachsprechen (bf_emma), Schreibauftrag; app.yaml, chapter.yaml und Skript make_images.py
<!-- tasks: pattern (1 added): the one page or screen that is the pattern for the others -->
- [ ] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
- [ ] Kapitel 1 Teil 1: Wiederholungsseite das-brauchst-du (schule-uk, feste-uk), Seiten usa-staedte und kanada mit Karte, Audio
- [ ] Kapitel 1 Teil 2: Seiten jugend-usa, schule-usa und feste-usa mit Audio, Kapitel-Rückblick und Selbsteinschätzung
- [ ] Kapitel 2 british-or-american: Wiederholungsseite (vokale, laut-buchstabe), Seiten be-ae-wortschatz, be-ae-aussprache (bf_emma gegen af_sarah) und be-ae-schreibung, Selbsteinschätzung
- [ ] Kapitel 3 Teil 1: Datendatei usa-zeitachse, Seiten mayflower, einwanderung-usa und unabhaengigkeit-usa mit Zeitachse und Audio
- [ ] Kapitel 3 Teil 2: Seiten westen-native-americans und politik-usa (mehrere Perspektiven), Selbsteinschätzung
- [ ] Kapitel 4 freiheit-gleichheit: Wiederholungsseite vielfalt-gb, Seiten sklaverei-buergerkrieg, gesellschaft-politik, buergerrechtsbewegung, migration-heute (Sachtexte mit Quellen), Selbsteinschätzung
- [ ] Kapitel 5 englisch-weltweit: Wiederholungsseite (britische-inseln, gruss-hoeflichkeit), Seiten australien, weitere-varietaet und kulturelle-konventionen mit Gesprächsszenen und Hörfassung, Selbsteinschätzung
- [ ] Prüfskript für Hörsätze (keine Hörsätze im Text derselben Seite), Wörter außerhalb A1/A2 im Inhaltsführer, Hörliste; Medienübersicht prüfen
<!-- tasks: pages (8 added): the other pages or screens, after the pattern -->
- [ ] Update the content guide so that it describes the app as built (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
