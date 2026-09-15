# Vorrat an Darstellungsformen

Arbeitspapier, kein Protokoll. Hier steht, **was gebaut ist** und **was noch kommen
könnte** — damit Vorschläge nicht im Gesprächsverlauf verloren gehen und beim nächsten
Mal nicht neu erfunden werden müssen.

Stand: 15. September 2026. Entscheidungen und Begründungen zum Gebauten stehen im
Protokoll unter `Sessions/`.

---

## Was gebaut ist

Jede Form liegt in `vorlage.html` auf genau einer Folie — der Foliensatz ist
zugleich sein eigener Musterbogen.

| # | Folie | Form | Zahlen kommen aus |
|---|---|---|---|
| 01 · 52 | Registerdeck · Vielen Dank | Titel- und Dankfolie | — |
| 02 | Agenda | Aufzählung, drei Ebenen | — |
| 03 | Forschungsstand | reine Textfolie mit Belegen | — |
| 04 | Erkenntnisgewinn | **Ablaufkette** mit zwei Rückwegen | Quelltext |
| 05 | Einordnung | **Schnittmenge** (drei Kreise) und **Vier-Felder-Matrix** auf einer Folie | Skript, `buildVenn`, `buildFelder` |
| 06 | Einflüsse | **Stern**: ein Kern, sechs Satelliten, paarweise als Schritte | Skript, `buildStern` |
| 07 | Gegenüberstellung | **Gegenüberstellung**: Vorstellung links, Fachkonzept rechts, Zeile für Zeile als Schritte | — |
| 08 | Formelsatz | **Formeln** als MathML in Fira Math | LaTeX in `data-tex` |
| 09 | Herleitung | **schrittweise Herleitung**, am Relationszeichen bündig | LaTeX in `data-tex` |
| 10 | Stichprobe | Kennzahlenkacheln | — |
| 11 | Erhebungsplan | **Zeitleiste** aus Phasen und Marken, zweite Ebene darüber | Quelltext |
| 12 | Vergleich | **Tabelle** mit Ausfüllgraden | — |
| 13 | Entwicklungszyklus | **Chevron-Kette** mit Spalten darunter | — |
| 14 | Praktikumsablauf | **Große Kacheln**, ein Schlagwort je Kachel | — |
| 15 | Unterrichtsverlauf | **Schwimmbahnen**: Rollen als Zeilen, Phasen als Spalten | Quelltext |
| 16 | Klimabox | **Bild mit Text**: Rasterbild als Daten-URI links, Stichpunkte rechts | Bild `Klimabox.png` |
| 17 | Zeiger | **Foto mit Zeigern**: Bild und Zeiger in einem SVG, ein Koordinatensystem, Zeiger als Schritte | Quelltext |
| 18 | Bildpaar | **Bildpaar**: zwei Bilder gleichen Seitenverhältnisses, je eine Unterschrift | Bilder |
| 19 | Erhebung | **Karten mit Titelschild**, Stichpunkte nach Kategorien | — |
| 20 | Ergebnisse | **Abschnittstrenner** mit Agenda-Chips | — |
| 21 | Freier Fall | **Streudiagramm** mit Ausgleichsgerade, Morph in die Parabel | Skript |
| 22 | Messkurve | **Messkurve über der Zeit**: Reihen einzeln, Modellkurve gestrichelt | Skript, `buildKurve` |
| 23 | Verteilungen | **Boxplots** | Quelltext |
| 24 | Gruppenmittel | **Säulen mit 95-%-Intervall** | Skript, `buildKI` |
| 25 | Aufgabe | **Aufgabenfolie**: Item im Wortlaut, Lösungshäufigkeit je Option, Lösung als Schritt | Quelltext (`--p`) |
| 26 | Antwortkurven | **Item-Antwortkurven**: Anteil je Option über der Gesamtpunktzahl, Marke „ab hier führt B" gerechnet | Skript, `buildIRC` |
| 27 | Hantel | **Hantel-Diagramm**: Prä und Post je Aufgabe, nach Zuwachs sortiert | Skript, `buildHantel` |
| 28 | Effektstärke | **Zwei Verteilungen überlappend**, Abstand der Mitten in Streuungseinheiten | Skript, `buildGlocken` |
| 29 | Forest Plot | **Forest Plot**: *d* mit Intervall je Teilgruppe, Gesamt als Raute im Schritt | Skript, `buildForest` |
| 30 | Pfadmodell | **Pfadmodell**: Kästen und Pfeile, Koeffizienten und indirekter Weg als Schritte | Skript, `buildPfad` |
| 31 | Wünsche | **Balken waagerecht**, Nennungen absteigend, Bezugslinie | Skript, `buildBalken` |
| 32 | Einschätzung | **Likert-Stapelbalken**, divergierend um die Mitte | Skript, `buildLikert` |
| 33 | Zugewinn | **Nachtest gegen Vortest**, Linien gleichen *g* | Skript, `buildHake` |
| 34 | Behauptung | **Behauptung + Beleg** (Assertion-Evidence): Titel als Satz, darunter **divergierende Säulen** um eine Nulllinie | Skript, `buildAbweichung` |
| 35 | Übergänge | **Übergangsmatrix als Sankey**, Prä → Post, Rückwege als Schritt | Skript, `buildSankey` |
| 36 | Energiefluss | **Energiefluss**: Sankey mit Knoten in Spalten, jede Spalte ein Schritt | Skript, `buildFluss` |
| 37 | Punktfeld | **Punktfeld**: 100 Punkte, Anteile als Farbe, je Anteil ein Schritt | Skript, `buildPunktfeld` |
| 38 | Frage und Antwort | **Frage und Antwort**: Forschungsfrage groß, Antwort als blaue Karte, Stützpunkte als zweiter Schritt | — |
| 39 | Hypothesen | **Hypothesen-Bilanz**: Erwartung je Zeile, Befund als Pille im Schritt (bestätigt · nicht bestätigt · offen) | — |
| 40 | Stimmen | **Zitat**, groß gesetzt | — |
| 41 | Transkript | **Transkript** mit Kodierspalte | — |
| 42 | Kategoriensystem | **Baum**, Äste einzeln aufklappbar | Skript, `buildBaum` |
| 43 | Rundlauf | **Kreisprozess** | Winkel im Skript |
| 44 | Spirale | **Spirale**: der offene Kreis, drei Windungen | Skript, `buildSpirale` |
| 45 | Von oben nach unten | **Trichter** mit Schwund je Stufe | Quelltext |
| 46 | Ausschluss | **Verzweigung**: Ja/Nein-Weichen mit Abgängen | Skript, `buildWeiche` |
| 47 | Aufploppen | **Kachelreihe** mit Skizzen | — |
| 48 | Deckel ab | Metapherngrafik | — |
| 49 | Stärken und Grenzen | **Plus / Minus**: zwei Karten, Zeichen statt Punkte, die Grenzen als Schritt | — |
| 50 | Drei Botschaften | **Drei Botschaften**: große Ziffer, ein Satz, je eine Karte | — |
| 51 | Quellen | Quellenverzeichnis | — |
| 53 | Zusammenfassung | **Schlussfolie**, bleibt in der Diskussion stehen | — |
| 54 | Fragen an Sie | **Fragen an das Publikum**: nummeriert, groß, als Schritte — bleibt in der Diskussion stehen | — |
| A1 | Wie gut trennen die Items? | **Itemkennwerte**: Schwierigkeit gegen Trennschärfe | Skript, `buildItem` |
| A2 | Was genau gerechnet wurde | Varianzanalyse als Tabelle | — |
| A3 | Voraussetzungen erfüllt? | geprüfte Voraussetzungen | — |

**Abgedeckt sind damit:** lineare Folge (Kette, Chevrons, Weichen), Kreis und Spirale,
Trichter, Streuung, Verteilung, Gruppenvergleich, Rangfolge, Zustimmung (Likert),
Übergänge (Sankey), Zeit (zwei Ebenen), Schwimmbahnen, Tabelle, Kacheln, Kategorien,
Schnittmenge, Vier-Felder, Baum, Abschnittstrenner, Zitat, Transkript, Formel, Bild mit Text,
Foto mit Zeigern, Bildpaar, Messkurve über der Zeit, Aufgabe mit Lösungshäufigkeit, Hantel,
zwei Verteilungen, Energiefluss, Stern, Pfadmodell, Behauptung + Beleg mit divergierenden
Säulen, Punktfeld, Frage und Antwort, Plus / Minus, Gegenüberstellung, Item-Antwortkurven,
Forest Plot, Hypothesen-Bilanz, Drei Botschaften, Fragen an das Publikum.

Die vier PowerPoint-Muster, die Max am 11.09. gezeigt hat (Kästen mit Titelschild,
Ablauf mit Detailkästen, große Schlagwort-Kacheln, Chevron-Kette mit Spalten), sind
damit auf den Folien 13, 14 und 19 in der Formensprache der Vorlage nachgebaut.
Seit demselben Tag gilt: **mehrere kleine Formen dürfen sich eine Folie teilen**, wenn
eine allein die Fläche nicht füllt (Folie 05).

---

## Vorrat A — Statistik und Ergebnisse

| Form | Sagt aus | Aufwand |
|---|---|---|
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
| **Repräsentationswechsel** | Realbild → Diagramm → Formel, nebeneinander oder per Morph ineinander. Der Morph von Folie 21 ist wiederverwendbar. | groß |

## Vorrat G — Bild und Aufgabe

Vorgeschlagen am 14.09., am selben Tag gebaut: Bildpaar (16), Foto mit Zeigern (15),
Aufgabenfolie (25), Energiefluss (36), Messkurve (22, samt Modellkurve — damit ist auch
„Modell und Realität" abgedeckt), Hantel (27), zwei Verteilungen (28). Geblieben ist:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Video** | Ein kurzes Versuchsvideo als `<video>`. **Vorbehalt:** Die Datei müsste neben dem Foliensatz liegen oder als Daten-URI hinein (schnell mehrere MB) — bricht das Prinzip „eine Datei, nichts nachzuladen". Zurückgestellt. | klein, aber ein Prinzipienbruch |

## Vorrat F — Medien und Rhetorik

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Bild vollflächig** | Ein Foto ohne Karte, bis an den Rand — als Stimmungsfolie. Bild *mit* Unterschrift und Text ist seit dem 14.09. gebaut (Folie 16, im Kartenraster, endet über der Fußzeile). Offen bleibt nur die Frage vom 10.09., ob ein Bild je bis zur Kante laufen darf. | klein, aber eine Entscheidung nötig |
| **Merksatzfolie** | Eine Aussage groß, sonst nichts. | klein |

---

## Vorrat H — Text strukturieren *(14.09., nach Websuche)*

Rahmen dafür ist **Assertion-Evidence** (Alley, Penn State): der Titel ein ganzer Satz, darunter
ein Beleg, kein Stichpunktblock. Gebaut sind davon: Behauptung + Beleg (34), Frage und Antwort
(38), Stern (06), Plus / Minus (49) am 14.09.; Gegenüberstellung (07), Hypothesen-Bilanz (39),
Drei Botschaften (50), Fragen an das Publikum (54) am 15.09. Geblieben:

| Form | Beziehung / Aussage | Aufwand |
|---|---|---|
| **Kernsatz mit Erläuterung** | Eine Aussage groß (33 px), das Kleingedruckte darunter als Schritte. | klein |
| **These – Beleg – Folgerung** | Argumentkette in drei Kästen mit Pfeilen, Sätze statt Stichpunkte. Für die Diskussion. | klein |
| **Konvergenz** | Mehrere Pfeile auf ein Ziel: drei Befunde → eine Schlussfolgerung. Gegenstück zur Verzweigung (46). | klein–mittel |
| **Gleichung** | A + B → C: „Vorwissen + Intervention → Zuwachs". Als Merkform stärker als ein Satz. | klein |
| **Klammer-Liste** | Eine Gruppe, eine Klammer: „diese drei Aufgaben messen dasselbe Konstrukt". | klein |
| **Nummerierte Schritte** | Ablauf in Worten: große Ziffer links, ein bis zwei Sätze rechts — die Kacheln (14) senkrecht, mit Platz für Text. | klein |
| **Lesefolie mit Hervorhebung** | Ein Absatz, Stellen werden nacheinander markiert — `<mark>` als Schritte, die Technik hat das Transkript (41). | klein |
| **Definition und Beispiel** | Begriff als Pille, Definition, dann ein Beispiel im Kasten. | klein |
| **Befund / Einordnung** | Zwei Spalten, links das Ergebnis, rechts seine Bedeutung — empfiehlt der Münsteraner Leitfaden für Ergebnisfolien. `.cols` reicht; eine Folie als Muster fehlt. | klein |
| **Was wir wissen / was offen ist** | Limitationen und Ausblick als zwei Spalten mit gegensätzlichen Schildern; nahe an Plus / Minus (49). | klein |
| **Zitat mit Kommentar** | Äußerung links, Einordnung rechts; das Zitat (40) hat den Kommentar nicht. | klein |

## Vorrat I — Daten und Fachliches *(14.09., nach FT Visual Vocabulary und PER-Literatur)*

Gebaut sind davon: divergierende Säulen (34), Punktfeld (37), Pfadmodell (30) am 14.09.;
Item-Antwortkurven (26) und Forest Plot (29) am 15.09. Geblieben:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Modellanalyse (Bao & Redish)** | Modellzustand als Punkt im Dreieck richtig / Fehlvorstellung / gemischt, Vortest → Nachtest als Pfeil. | groß |
| **Kleine Vielfache** | Sechs Klassen, sechs Mini-Messkurven im Raster — Muster auf einen Blick statt sechs Folien. `buildKurve` sechsmal, kleiner. | mittel |
| **Konfidenzband** | Die Messkurve (22) mit Unsicherheit als Fläche; im FT-Raster „Fächer". | klein |
| **Kennzahl mit Veränderung** | Kachel mit vorher → nachher und Δ; die Kennzahlenkacheln (10) zeigen nur einen Wert. | klein |
| **Studiendesign als Schema** | Gruppen × Zeitpunkte, der Interventionsblock als Kasten — was jedes Methodenkapitel braucht; Schwimmbahnen (15) sind die Vorlage. | klein |
| **Punktstreifen** | Jeder Lernende ein Punkt auf einer Achse — ehrlicher als der Boxplot (23) bei n < 30. | klein |
| **Lollipop** | Balken als Strich mit Punkt, wenn der Wert wichtiger ist als die Fläche. Variante von 31. | klein |
| **Verbundenes Streudiagramm** | Jede Klasse als Pfad Vortest → Nachtest in zwei Merkmalen. Nur, wenn es wirklich zwei Merkmale gibt. | mittel |
| **Kumulierte Kurve** | Wenn Ungleichheit die Aussage ist: y kumulierte Häufigkeit, x das Maß. | klein |

## Wenn davon etwas gebaut wird

Vorgeschlagene Reihenfolge, falls nichts dagegen spricht:

1. **Kernsatz mit Erläuterung**, **Konvergenz**, **Gleichung** — drei kleine Textformen
2. **Slopegraph** — eine Linie je Person, Prä → Post
3. **Studiendesign als Schema** und **Kennzahl mit Veränderung** — Methodenteil
4. **Triade, Pyramide, Zwiebel** — drei kleine Strukturbilder, gern zu zweit auf einer Folie
5. **Zuordnung mit Verbindungslinien** — Fehlvorstellung ↔ Fachkonzept
6. **Freikörperbild** — Kraftpfeile einzeln einblendbar

**Hinweis ab hier:** Der Musterbogen hat 54 + 3 Folien. Das Register ist damit an der
unteren Stufe angekommen (813 px Fensterhöhe: 97 %, 720 px: 105 %). Entschieden am 15.09.:
so lassen — die Vorlage zeigt Möglichkeiten, echte Vorträge haben 15–25 Folien. Weitere
Formen dürfen dazukommen; das Register ist dann bei kleinen Fenstern voll.

Danach **Gantt**, **Item-Heatmap**, **Histogramm**, **Merksatzfolie**; die
**Versuchsskizze** (der Zeiger-Baukasten von Folie 17 ist dafür der Anfang) und der
**Repräsentationswechsel** sind die aufwendigsten.

Für Rasterbilder gilt seit dem 14.09.: vor dem Einbetten Weißrand beschneiden, auf
etwa 1200 px Breite bringen, Farbzahl reduzieren, wenn es eine Zeichnung ist (die
Klimabox: 3508 × 2480 und 192 KB → 1200 × 989 und 21 KB). Höchstens 360 px hoch auf
der Folie, mit einzeiliger Unterschrift.

### Randbedingungen, die für alles gelten

* Nutzbare Fläche 1144 × 600 px, Abbildungen höchstens 400 px hoch. Breite Formen
  (Zeitleiste, Stapelbalken, Schwimmbahnen) passen nur quer, nicht neben einer Textspalte.
* Datengetriebenes folgt dem Muster von `buildFall`: Zahlen als Array im Quelltext,
  Achsen und Geometrie daraus gerechnet.
* Eine Folie je Form. Keine Sammelfolien.
* Bewusst nicht: Kreis- und Donutdiagramme (Balken lesen sich besser), Wortwolken, alles
  Dreidimensionale.
* Keine neuen Farben ohne ausdrückliche Bitte. Blau-Staffel und Grau reichen für zwei
  bis fünf Gruppen; Rot und Grün sind mit „gescheitert" und „trägt" belegt.
* Formeln immer als `data-tex`, dann `python3 formeln.py`. Einzelne Zeichen
  **außerhalb** einer Formel (`Δ π ≈ ≤ → ←`) stehen direkt im Text — die Schrift hat
  sie. Was sie nicht hat (`↔ ⇒ ∇`), gehört in eine Formel.
