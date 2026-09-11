# Vorrat an Darstellungsformen

Arbeitspapier, kein Protokoll. Hier steht, **was gebaut ist** und **was noch kommen
könnte** — damit Vorschläge nicht im Gesprächsverlauf verloren gehen und beim nächsten
Mal nicht neu erfunden werden müssen.

Stand: 11. September 2026. Entscheidungen und Begründungen zum Gebauten stehen im
Protokoll unter `Sessions/`.

---

## Was gebaut ist

Jede Form liegt in `vorlage.html` auf genau einer Folie — der Foliensatz ist
zugleich sein eigener Musterbogen.

| # | Folie | Form | Zahlen kommen aus |
|---|---|---|---|
| 01 · 27 | Registerdeck · Vielen Dank | Titel- und Dankfolie | — |
| 02 | Agenda | Aufzählung, drei Ebenen | — |
| 03 | Forschungsstand | reine Textfolie mit Belegen | — |
| 04 | Erkenntnisgewinn | **Ablaufkette** mit zwei Rückwegen | Quelltext |
| 05 | Formelsatz | **Formeln** als MathML in Fira Math | LaTeX in `data-tex` |
| 06 | Herleitung | **schrittweise Herleitung**, am Relationszeichen bündig | LaTeX in `data-tex` |
| 07 | Stichprobe | Kennzahlenkacheln | — |
| 08 | Erhebungsplan | **Zeitleiste** aus Phasen und Marken, zweite Ebene darüber | Quelltext |
| 09 | Vergleich | **Tabelle** mit Ausfüllgraden | — |
| 10 | Entwicklungszyklus | **Chevron-Kette** mit Spalten darunter | — |
| 11 | Praktikumsablauf | **Große Kacheln**, ein Schlagwort je Kachel | — |
| 12 | Erhebung | **Karten mit Titelschild**, Stichpunkte nach Kategorien | — |
| 13 | Ergebnisse | **Abschnittstrenner** mit Agenda-Chips | — |
| 14 | Freier Fall | **Streudiagramm** mit Ausgleichsgerade, Morph in die Parabel | Skript |
| 15 | Verteilungen | **Boxplots** | Quelltext |
| 16 | Gruppenmittel | **Säulen mit 95-%-Intervall** | Skript, `buildKI` |
| 17 | Wünsche | **Balken waagerecht**, Nennungen absteigend, Bezugslinie | Skript, `buildBalken` |
| 18 | Einschätzung | **Likert-Stapelbalken**, divergierend um die Mitte | Skript, `buildLikert` |
| 19 | Zugewinn | **Nachtest gegen Vortest**, Linien gleichen *g* | Skript, `buildHake` |
| 20 | Stimmen | **Zitat**, groß gesetzt | — |
| 21 | Transkript | **Transkript** mit Kodierspalte | — |
| 22 | Rundlauf | **Kreisprozess** | Winkel im Skript |
| 23 | Von oben nach unten | **Trichter** mit Schwund je Stufe | Quelltext |
| 24 | Aufploppen | **Kachelreihe** mit Skizzen | — |
| 25 | Deckel ab | Metapherngrafik | — |
| 26 | Quellen | Quellenverzeichnis | — |
| 28 | Zusammenfassung | **Schlussfolie**, bleibt in der Diskussion stehen | — |
| A1 | Wie gut trennen die Items? | **Itemkennwerte**: Schwierigkeit gegen Trennschärfe | Skript, `buildItem` |
| A2 | Was genau gerechnet wurde | Varianzanalyse als Tabelle | — |
| A3 | Voraussetzungen erfüllt? | geprüfte Voraussetzungen | — |

**Abgedeckt sind damit:** lineare Folge (Kette, Chevrons), Kreis, Trichter, Streuung,
Verteilung, Gruppenvergleich, Rangfolge, Zustimmung (Likert), Zeit (zwei Ebenen),
Tabelle, Kacheln, Kategorien, Abschnittstrenner, Zitat, Transkript, Formel.

Die vier PowerPoint-Muster, die Max am 11.09. gezeigt hat (Kästen mit Titelschild,
Ablauf mit Detailkästen, große Schlagwort-Kacheln, Chevron-Kette mit Spalten), sind
damit auf den Folien 10, 11 und 12 in der Formensprache der Vorlage nachgebaut.

---

## Vorrat A — Statistik und Ergebnisse

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Übergangsmatrix / Sankey Prä→Post** | Wer wechselt von der Fehlvorstellung zum Fachkonzept — und wer zurück. Bei Concept Inventories der Befund, den jeder Mittelwert verschluckt. | groß |
| **Forest Plot** | Mehrere Effektstärken mit Intervall untereinander. Für den Forschungsstand und für Subgruppen. | mittel |
| **Item-Heatmap** | Lösungshäufigkeit je Item × Gruppe. Ergänzt die Kennwertkarte auf A1, ersetzt sie nicht. | mittel |
| **Prä-Post-Verbindungslinien** (Slopegraph) | Eine Linie je Person. Zeigt individuelle Entwicklung statt Gruppenmittel. | mittel |
| **Histogramm mit Referenzlinie** | Verteilung einer Skala, Normwert markiert. | klein |
| **Netzdiagramm (Radar)** | Ein Profil über mehrere Merkmale, zwei Gruppen übereinander. | mittel |

## Vorrat B — Ablauf, wenn die Reihenfolge die Aussage ist

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Schwimmbahnen** | Wer macht was wann. Zeilen sind Rollen (Lehrkraft, Lernende, Material), Spalten Phasen. Für Unterrichtsverläufe die klarste Form. | mittel |
| **Spirale** | Es wiederholt sich, aber es kommt voran. Der Kreisprozess auf Folie 22 zeigt nur den geschlossenen Kreis — Design-Based Research braucht den offenen. | mittel |
| **Verzweigung** | Hier wird entschieden. Ja/Nein-Weiche mit zwei Pfaden: Ausschlussverfahren, Kodierregeln, Auswertungslogik. | mittel |
| **Gegenläufige Ketten** | Zwei Stränge laufen aufeinander zu. Theorie ↔ Empirie, fachliche Klärung ↔ Lernerperspektive. | mittel |
| **Arbeits- und Zeitplan** (Gantt) | Projektphasen über Quartalen, Stand als Linie. Für den Teil „Pläne". | mittel |

## Vorrat C — Struktur, wenn die Beziehung die Aussage ist

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Schnittmenge (Venn)** | Das Interessante liegt in der Überlappung. Fachwissen ∩ Pädagogik = fachdidaktisches Wissen. | klein |
| **Triade / Dreieck** | Drei Größen bedingen sich gegenseitig. Didaktisches Dreieck, Modell der Didaktischen Rekonstruktion. | klein |
| **Pyramide / Stufen** | Es baut aufeinander auf, oben wird es enger. Kompetenz- und Niveaustufen. | klein |
| **Schichten / Zwiebel** | Ein Kern, um den sich Kontexte legen. | klein |
| **Baum** | Das zerfällt in Teile. Kategoriensystem, Codebaum der Inhaltsanalyse, Ebenen einzeln aufklappbar. | mittel |
| **Vier-Felder-Matrix** | Zwei Achsen spannen vier Typen auf. | klein |
| **Concept Map** | Begriffe mit beschrifteten Relationen — auch als Erhebungsergebnis. | mittel |

## Vorrat D — Vergleich und Zuordnung

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Zuordnung mit Verbindungslinien** | Was gehört zu was. Zwei Spalten, Linien dazwischen: Fehlvorstellung ↔ Fachkonzept. | klein |
| **Waage** | Zwei Seiten wiegen unterschiedlich schwer. Für Abwägungen im Ausblick. | klein |

## Vorrat E — fachlich, physiknah

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Beschriftete Versuchsskizze** | Aufbau mit Zeigern, die einzeln erscheinen. Die `.sk`-Klassen der Kacheln gibt es schon. | mittel |
| **Freikörperbild** | Kraftpfeile am Körper, einzeln einblendbar — der klassische Gegenstand von Fehlvorstellungen. | mittel |
| **Repräsentationswechsel** | Realbild → Diagramm → Formel, nebeneinander oder per Morph ineinander. Der Morph von Folie 14 ist wiederverwendbar. | groß |

## Vorrat F — Medien und Rhetorik

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Bild vollflächig / mit Unterschrift** | Offener Punkt 8.2 im Protokoll: Text nie über der Fußzeile, Fotos gelegentlich schon. Vor dem Bauen ist zu klären, ob solche Bilder bis zur Kante laufen. | klein, aber eine Entscheidung nötig |
| **Merksatzfolie** | Eine Aussage groß, sonst nichts. | klein |

---

## Wenn davon etwas gebaut wird

Vorgeschlagene Reihenfolge, falls nichts dagegen spricht:

1. **Schwimmbahnen** — für jeden Unterrichtsverlauf
2. **Spirale** — schließt die Lücke, die der Kreisprozess offen lässt
3. **Schnittmenge** — fachdidaktisches Standardbild, billig zu bauen
4. **Verzweigung** — Auswertungs- und Kodierlogik
5. **Baum** — Kategoriensystem

Danach aus Vorrat A die **Übergangsmatrix** — die aufwendigste und inhaltlich die
stärkste.

### Randbedingungen, die für alles gelten

* Nutzbare Fläche 1144 × 600 px, Abbildungen höchstens 400 px hoch. Breite Formen
  (Zeitleiste, Stapelbalken, Schwimmbahnen) passen nur quer, nicht neben einer Textspalte.
* Datengetriebenes folgt dem Muster von `buildFall`: Zahlen als Array im Quelltext,
  Achsen und Geometrie daraus gerechnet.
* Eine Folie je Form. Keine Sammelfolien.
* Keine neuen Farben ohne ausdrückliche Bitte. Blau-Staffel und Grau reichen für zwei
  bis fünf Gruppen; Rot und Grün sind mit „gescheitert" und „trägt" belegt.
* Formeln immer als `data-tex`, dann `python3 formeln.py`. Einzelne Zeichen
  **außerhalb** einer Formel (`Δ π ≈ ≤ → ←`) stehen direkt im Text — die Schrift hat
  sie. Was sie nicht hat (`↔ ⇒ ∇`), gehört in eine Formel.
