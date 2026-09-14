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
| 01 · 33 | Registerdeck · Vielen Dank | Titel- und Dankfolie | — |
| 02 | Agenda | Aufzählung, drei Ebenen | — |
| 03 | Forschungsstand | reine Textfolie mit Belegen | — |
| 04 | Erkenntnisgewinn | **Ablaufkette** mit zwei Rückwegen | Quelltext |
| 05 | Einordnung | **Schnittmenge** (drei Kreise) und **Vier-Felder-Matrix** auf einer Folie | Skript, `buildVenn`, `buildFelder` |
| 06 | Formelsatz | **Formeln** als MathML in Fira Math | LaTeX in `data-tex` |
| 07 | Herleitung | **schrittweise Herleitung**, am Relationszeichen bündig | LaTeX in `data-tex` |
| 08 | Stichprobe | Kennzahlenkacheln | — |
| 09 | Erhebungsplan | **Zeitleiste** aus Phasen und Marken, zweite Ebene darüber | Quelltext |
| 10 | Vergleich | **Tabelle** mit Ausfüllgraden | — |
| 11 | Entwicklungszyklus | **Chevron-Kette** mit Spalten darunter | — |
| 12 | Praktikumsablauf | **Große Kacheln**, ein Schlagwort je Kachel | — |
| 13 | Unterrichtsverlauf | **Schwimmbahnen**: Rollen als Zeilen, Phasen als Spalten | Quelltext |
| 14 | Erhebung | **Karten mit Titelschild**, Stichpunkte nach Kategorien | — |
| 15 | Ergebnisse | **Abschnittstrenner** mit Agenda-Chips | — |
| 16 | Freier Fall | **Streudiagramm** mit Ausgleichsgerade, Morph in die Parabel | Skript |
| 17 | Verteilungen | **Boxplots** | Quelltext |
| 18 | Gruppenmittel | **Säulen mit 95-%-Intervall** | Skript, `buildKI` |
| 19 | Wünsche | **Balken waagerecht**, Nennungen absteigend, Bezugslinie | Skript, `buildBalken` |
| 20 | Einschätzung | **Likert-Stapelbalken**, divergierend um die Mitte | Skript, `buildLikert` |
| 21 | Zugewinn | **Nachtest gegen Vortest**, Linien gleichen *g* | Skript, `buildHake` |
| 22 | Übergänge | **Übergangsmatrix als Sankey**, Prä → Post, Rückwege als Schritt | Skript, `buildSankey` |
| 23 | Stimmen | **Zitat**, groß gesetzt | — |
| 24 | Transkript | **Transkript** mit Kodierspalte | — |
| 25 | Kategoriensystem | **Baum**, Äste einzeln aufklappbar | Skript, `buildBaum` |
| 26 | Rundlauf | **Kreisprozess** | Winkel im Skript |
| 27 | Spirale | **Spirale**: der offene Kreis, drei Windungen | Skript, `buildSpirale` |
| 28 | Von oben nach unten | **Trichter** mit Schwund je Stufe | Quelltext |
| 29 | Ausschluss | **Verzweigung**: Ja/Nein-Weichen mit Abgängen | Skript, `buildWeiche` |
| 30 | Aufploppen | **Kachelreihe** mit Skizzen | — |
| 31 | Deckel ab | Metapherngrafik | — |
| 32 | Quellen | Quellenverzeichnis | — |
| 34 | Zusammenfassung | **Schlussfolie**, bleibt in der Diskussion stehen | — |
| A1 | Wie gut trennen die Items? | **Itemkennwerte**: Schwierigkeit gegen Trennschärfe | Skript, `buildItem` |
| A2 | Was genau gerechnet wurde | Varianzanalyse als Tabelle | — |
| A3 | Voraussetzungen erfüllt? | geprüfte Voraussetzungen | — |

**Abgedeckt sind damit:** lineare Folge (Kette, Chevrons, Weichen), Kreis und Spirale,
Trichter, Streuung, Verteilung, Gruppenvergleich, Rangfolge, Zustimmung (Likert),
Übergänge (Sankey), Zeit (zwei Ebenen), Schwimmbahnen, Tabelle, Kacheln, Kategorien,
Schnittmenge, Vier-Felder, Baum, Abschnittstrenner, Zitat, Transkript, Formel.

Die vier PowerPoint-Muster, die Max am 11.09. gezeigt hat (Kästen mit Titelschild,
Ablauf mit Detailkästen, große Schlagwort-Kacheln, Chevron-Kette mit Spalten), sind
damit auf den Folien 11, 12 und 14 in der Formensprache der Vorlage nachgebaut.
Seit demselben Tag gilt: **mehrere kleine Formen dürfen sich eine Folie teilen**, wenn
eine allein die Fläche nicht füllt (Folie 05).

---

## Vorrat A — Statistik und Ergebnisse

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Forest Plot** | Mehrere Effektstärken mit Intervall untereinander. Für den Forschungsstand und für Subgruppen. | mittel |
| **Item-Heatmap** | Lösungshäufigkeit je Item × Gruppe. Ergänzt die Kennwertkarte auf A1, ersetzt sie nicht. | mittel |
| **Prä-Post-Verbindungslinien** (Slopegraph) | Eine Linie je Person. Zeigt individuelle Entwicklung statt Gruppenmittel. | mittel |
| **Histogramm mit Referenzlinie** | Verteilung einer Skala, Normwert markiert. | klein |
| **Netzdiagramm (Radar)** | Ein Profil über mehrere Merkmale, zwei Gruppen übereinander. | mittel |

## Vorrat B — Ablauf, wenn die Reihenfolge die Aussage ist

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Gegenläufige Ketten** | Zwei Stränge laufen aufeinander zu. Theorie ↔ Empirie, fachliche Klärung ↔ Lernerperspektive. | mittel |
| **Arbeits- und Zeitplan** (Gantt) | Projektphasen über Quartalen, Stand als Linie. Für den Teil „Pläne". | mittel |

## Vorrat C — Struktur, wenn die Beziehung die Aussage ist

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Triade / Dreieck** | Drei Größen bedingen sich gegenseitig. Didaktisches Dreieck, Modell der Didaktischen Rekonstruktion. | klein |
| **Pyramide / Stufen** | Es baut aufeinander auf, oben wird es enger. Kompetenz- und Niveaustufen. | klein |
| **Schichten / Zwiebel** | Ein Kern, um den sich Kontexte legen. | klein |
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
| **Repräsentationswechsel** | Realbild → Diagramm → Formel, nebeneinander oder per Morph ineinander. Der Morph von Folie 16 ist wiederverwendbar. | groß |

## Vorrat F — Medien und Rhetorik

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Bild vollflächig / mit Unterschrift** | Offener Punkt 8.2 im Protokoll: Text nie über der Fußzeile, Fotos gelegentlich schon. Vor dem Bauen ist zu klären, ob solche Bilder bis zur Kante laufen. | klein, aber eine Entscheidung nötig |
| **Merksatzfolie** | Eine Aussage groß, sonst nichts. | klein |

---

## Wenn davon etwas gebaut wird

Vorgeschlagene Reihenfolge, falls nichts dagegen spricht:

1. **Forest Plot** — Effektstärken mit Intervall, für Forschungsstand und Subgruppen
2. **Slopegraph** — eine Linie je Person, Prä → Post
3. **Triade, Pyramide, Zwiebel** — drei kleine Strukturbilder, gern zu zweit auf einer Folie
4. **Zuordnung mit Verbindungslinien** — Fehlvorstellung ↔ Fachkonzept
5. **Freikörperbild** — Kraftpfeile einzeln einblendbar

Danach **Gantt**, **Item-Heatmap**, **Histogramm**, **Merksatzfolie**; die
**Versuchsskizze** und der **Repräsentationswechsel** sind die aufwendigsten.

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
