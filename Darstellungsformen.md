# Vorrat an Darstellungsformen

Arbeitspapier, kein Protokoll. Hier steht, **was gebaut ist** und **was noch kommen
könnte** — damit Vorschläge nicht im Gesprächsverlauf verloren gehen und beim nächsten
Mal nicht neu erfunden werden müssen.

Stand: 10. September 2026. Entscheidungen und Begründungen zum Gebauten stehen im
Protokoll unter `Sessions/`.

---

## Was gebaut ist

Jede Form liegt in `vorlage.html` auf genau einer Folie — der Foliensatz ist
zugleich sein eigener Musterbogen.

| # | Folie | Form | Zahlen kommen aus |
|---|---|---|---|
| 01 · 20 | Registerdeck · Vielen Dank | Titel- und Abschlussfolie | — |
| 02 | Agenda | Aufzählung, drei Ebenen | — |
| 03 | Forschungsstand | reine Textfolie mit Belegen | — |
| 04 | Erkenntnisgewinn | **Ablaufkette** mit zwei Rückwegen | Quelltext |
| 05 | Formelsatz | **Formeln** als MathML in Fira Math | LaTeX in `data-tex` |
| 06 | Herleitung | **schrittweise Herleitung**, am Relationszeichen bündig | LaTeX in `data-tex` |
| 07 | Stichprobe | Kennzahlenkacheln | — |
| 08 | Erhebungsplan | **Zeitleiste** aus Phasen und Marken | Quelltext |
| 09 | Vergleich | **Tabelle** mit Ausfüllgraden | — |
| 10 | Freier Fall | **Streudiagramm** mit Ausgleichsgerade, Morph in die Parabel | Skript |
| 11 | Verteilungen | **Boxplots** | Quelltext |
| 12 | Gruppenmittel | **Balken mit 95-%-Intervall** | Skript, `buildKI` |
| 13 | Zugewinn | **Nachtest gegen Vortest**, Linien gleichen *g* | Skript, `buildHake` |
| 14 | Stimmen | **Zitat**, groß gesetzt | — |
| 15 | Transkript | **Transkript** mit Kodierspalte | — |
| 16 | Rundlauf | **Kreisprozess** | Winkel im Skript |
| 17 | Von oben nach unten | **Trichter** mit Schwund je Stufe | Quelltext |
| 18 | Aufploppen | **Kachelreihe** | — |
| 19 | Deckel ab | Metapherngrafik | — |
| 21 | Quellen | Quellenverzeichnis | — |

**Abgedeckt sind damit:** lineare Folge, Kreis, Trichter, Streuung, Verteilung,
Gruppenvergleich, Zeit, Tabelle, Zitat, Transkript, Formel.

---

## Vorrat A — Statistik und Ergebnisse

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Divergierende Stapelbalken** (Likert) | Wie sich Zustimmung verteilt, um die Mitte zentriert. Für Fragebogenitems unverzichtbar. | mittel |
| **Übergangsmatrix / Sankey Prä→Post** | Wer wechselt von der Fehlvorstellung zum Fachkonzept — und wer zurück. Bei Concept Inventories der Befund, den jeder Mittelwert verschluckt. | groß |
| **Forest Plot** | Mehrere Effektstärken mit Intervall untereinander. Für den Forschungsstand und für Subgruppen. | mittel |
| **Item-Heatmap** | Lösungshäufigkeit je Item × Gruppe. Geht mit der Blau-Staffel 10/25/50/75/100 %, ohne neue Farben. | mittel |
| **Prä-Post-Verbindungslinien** (Slopegraph) | Eine Linie je Person. Zeigt individuelle Entwicklung statt Gruppenmittel. | mittel |
| **Histogramm mit Referenzlinie** | Verteilung einer Skala, Normwert markiert. | klein |
| **Netzdiagramm (Radar)** | Ein Profil über mehrere Merkmale, zwei Gruppen übereinander. | mittel |

## Vorrat B — Ablauf, wenn die Reihenfolge die Aussage ist

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Schwimmbahnen** | Wer macht was wann. Zeilen sind Rollen (Lehrkraft, Lernende, Material), Spalten Phasen. Für Unterrichtsverläufe die klarste Form. | mittel |
| **Spirale** | Es wiederholt sich, aber es kommt voran. Der Kreisprozess auf Folie 16 zeigt nur den geschlossenen Kreis — Design-Based Research braucht den offenen. | mittel |
| **Verzweigung** | Hier wird entschieden. Ja/Nein-Weiche mit zwei Pfaden: Ausschlussverfahren, Kodierregeln, Auswertungslogik. | mittel |
| **Chevron-Kette** | Dieselbe Aussage wie die Kette auf Folie 04, aber kompakter und mit Richtungsdruck. Gut für sechs Phasen nebeneinander. | klein |
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
| **Repräsentationswechsel** | Realbild → Diagramm → Formel, nebeneinander oder per Morph ineinander. Der Morph von Folie 10 ist wiederverwendbar. | groß |

## Vorrat F — Medien und Rhetorik

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Bild vollflächig / mit Unterschrift** | Offener Punkt 8.2 im Protokoll: Text nie über der Fußzeile, Fotos gelegentlich schon. Vor dem Bauen ist zu klären, ob solche Bilder bis zur Kante laufen. | klein, aber eine Entscheidung nötig |
| **Abschnittstrenner** | Zwischenfolie, die den laufenden Agendapunkt hervorhebt. | klein |
| **Merksatzfolie** | Eine Aussage groß, sonst nichts. | klein |
| **Backup-Folien** | Nach der Dankfolie für die Fragerunde. Nur eine Konvention, wie sie sich abheben. | klein |

---

## Wenn davon etwas gebaut wird

Vorgeschlagene Reihenfolge, falls nichts dagegen spricht:

1. **Schwimmbahnen** — für jeden Unterrichtsverlauf
2. **Spirale** — schließt die Lücke, die der Kreisprozess offen lässt
3. **Schnittmenge** — fachdidaktisches Standardbild, billig zu bauen
4. **Verzweigung** — Auswertungs- und Kodierlogik
5. **Baum** — Kategoriensystem

Danach aus Vorrat A die **Likert-Stapelbalken** und die **Übergangsmatrix**; letztere
ist die aufwendigste und inhaltlich die stärkste.

### Randbedingungen, die für alles gelten

* Nutzbare Fläche 1144 × 600 px, Abbildungen höchstens 400 px hoch. Breite Formen
  (Zeitleiste, Stapelbalken, Schwimmbahnen) passen nur quer, nicht neben einer Textspalte.
* Datengetriebenes folgt dem Muster von `buildFall`: Zahlen als Array im Quelltext,
  Achsen und Geometrie daraus gerechnet.
* Eine Folie je Form. Keine Sammelfolien.
* Keine neuen Farben ohne ausdrückliche Bitte. Blau-Staffel und Grau reichen für zwei
  bis fünf Gruppen; Rot und Grün sind mit „gescheitert" und „trägt" belegt.
* Formeln immer als `data-tex`, dann `python3 formeln.py`. Einzelne fehlende Zeichen
  **außerhalb** einer Formel (`Δ π ≈ ≤ → ←`) nie direkt setzen, sondern mit `.gr`.
