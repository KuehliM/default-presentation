# Vorrat an Darstellungsformen

Arbeitspapier, kein Protokoll. Hier steht, **was gebaut ist** und **was noch kommen
könnte** — damit Vorschläge nicht im Gesprächsverlauf verloren gehen und beim nächsten
Mal nicht neu erfunden werden müssen.

Stand: 15. September 2026, abends. Entscheidungen und Begründungen zum Gebauten stehen im
Protokoll unter `Sessions/`.

---

## Was gebaut ist

Jede Form liegt in `vorlage.html` auf genau einer Folie — der Foliensatz ist
zugleich sein eigener Musterbogen.

| # | Folie | Form | Zahlen kommen aus |
|---|---|---|---|
| 01 · 65 | Registerdeck · Vielen Dank | Titel- und Dankfolie | — |
| 02 | Agenda | Aufzählung, drei Ebenen | — |
| 03 | Forschungsstand | reine Textfolie mit Belegen | — |
| 04 | Erkenntnisgewinn | **Ablaufkette** mit zwei Rückwegen | Quelltext |
| 05 | Einordnung | **Schnittmenge** (drei Kreise) und **Vier-Felder-Matrix** auf einer Folie | Skript, `buildVenn`, `buildFelder` |
| 06 | Dreieck und Zwiebel | **Triade** (drei Ecken, Doppelpfeile als Schritt) und **Zwiebel** (Kern und drei Schichten, je Schicht ein Schritt) auf einer Folie | Skript, `buildTriade`, `buildZwiebel` |
| 07 | Stufen | **Pyramide**: vier Stufen von unten nach oben, rechts je eine Erläuterung, jede Stufe ein Schritt | Skript, `buildPyramide` |
| 08 | Einflüsse | **Stern**: ein Kern, sechs Satelliten, paarweise als Schritte | Skript, `buildStern` |
| 09 | Gegenüberstellung | **Gegenüberstellung**: Vorstellung links, Fachkonzept rechts, Zeile für Zeile als Schritte | — |
| 10 | Zuordnung | **Zuordnung mit Verbindungslinien**: Vorstellungen links, Fachkonzepte rechts, Linien je Konzept als Schritt | Skript, `buildZuordnung` |
| 11 | Formelsatz | **Formeln** als MathML in Fira Math | LaTeX in `data-tex` |
| 12 | Herleitung | **schrittweise Herleitung**, am Relationszeichen bündig | LaTeX in `data-tex` |
| 13 | Gleichung | **Gleichung**: A + B → C als Merkform, Terme als Kacheln, Ergebnis blau; Term und Zeichen als Schritte | — |
| 14 | Freikörperbild | **Freikörperbild**: Körper auf schiefer Ebene, Gewichts-, Normal- und Reibungskraft einzeln, Zerlegung als vierter Schritt | Skript, `buildKraefte` |
| 15 | Stichprobe | Kennzahlenkacheln | — |
| 16 | Studiendesign | **Studiendesign als Schema**: Gruppen × Zeitpunkte, Intervention als Kasten, Kontrollgruppe und Follow-up als Schritte | — |
| 17 | Erhebungsplan | **Zeitleiste** aus Phasen und Marken, zweite Ebene darüber | Quelltext |
| 18 | Vergleich | **Tabelle** mit Ausfüllgraden | — |
| 19 | Entwicklungszyklus | **Chevron-Kette** mit Spalten darunter | — |
| 20 | Praktikumsablauf | **Große Kacheln**, ein Schlagwort je Kachel | — |
| 21 | Unterrichtsverlauf | **Schwimmbahnen**: Rollen als Zeilen, Phasen als Spalten | Quelltext |
| 22 | Klimabox | **Bild mit Text**: Rasterbild als Daten-URI links, Stichpunkte rechts | Bild `quellen/Klimabox.png` |
| 23 | Zeiger | **Foto mit Zeigern**: Bild und Zeiger in einem SVG, ein Koordinatensystem, Zeiger als Schritte | Quelltext |
| 24 | Bildpaar | **Bildpaar**: zwei Bilder gleichen Seitenverhältnisses, je eine Unterschrift | Bilder |
| 25 | Erhebung | **Karten mit Titelschild**, Stichpunkte nach Kategorien | — |
| 26 | Ergebnisse | **Abschnittstrenner** mit Agenda-Chips | — |
| 27 | Freier Fall | **Streudiagramm** mit Ausgleichsgerade, Morph in die Parabel | Skript |
| 28 | Messkurve | **Messkurve über der Zeit**: Reihen einzeln, Modellkurve gestrichelt | Skript, `buildKurve` |
| 29 | Verteilungen | **Boxplots** | Quelltext |
| 30 | Histogramm | **Histogramm mit Referenzlinie**: Klassen aus Rohwerten, Schwelle als Schritt, Anteil darüber gerechnet | Skript, `buildHisto` |
| 31 | Gruppenmittel | **Säulen mit 95-%-Intervall** | Skript, `buildKI` |
| 32 | Aufgabe | **Aufgabenfolie**: Item im Wortlaut, Lösungshäufigkeit je Option, Lösung als Schritt | Quelltext (`--p`) |
| 33 | Antwortkurven | **Item-Antwortkurven**: Anteil je Option über der Gesamtpunktzahl, Marke „ab hier führt B" gerechnet | Skript, `buildIRC` |
| 34 | Hantel | **Hantel-Diagramm**: Prä und Post je Aufgabe, nach Zuwachs sortiert | Skript, `buildHantel` |
| 35 | Slopegraph | **Slopegraph**: eine Linie je Person, Prä → Post, steigend blau, fallend grau; Mittel und Zahl der Fallenden als Schritte | Skript, `buildSlope` |
| 36 | Heatmap | **Item-Heatmap**: Items × Gruppen, Zelle nach Wert gefärbt, Nachtest und Zuwachs als Schritte | Skript, `buildHeat` |
| 37 | Effektstärke | **Zwei Verteilungen überlappend**, Abstand der Mitten in Streuungseinheiten | Skript, `buildGlocken` |
| 38 | Forest Plot | **Forest Plot**: *d* mit Intervall je Teilgruppe, Gesamt als Raute im Schritt | Skript, `buildForest` |
| 39 | Pfadmodell | **Pfadmodell**: Kästen und Pfeile, Koeffizienten und indirekter Weg als Schritte | Skript, `buildPfad` |
| 40 | Wünsche | **Balken waagerecht**, Nennungen absteigend, Bezugslinie | Skript, `buildBalken` |
| 41 | Einschätzung | **Likert-Stapelbalken**, divergierend um die Mitte | Skript, `buildLikert` |
| 42 | Zugewinn | **Nachtest gegen Vortest**, Linien gleichen *g* | Skript, `buildHake` |
| 43 | Veränderung | **Kennzahl mit Veränderung**: Kacheln mit vorher → nachher, Differenz als Pille im Schritt | — |
| 44 | Behauptung | **Behauptung + Beleg** (Assertion-Evidence): Titel als Satz, darunter **divergierende Säulen** um eine Nulllinie | Skript, `buildAbweichung` |
| 45 | Übergänge | **Übergangsmatrix als Sankey**, Prä → Post, Rückwege als Schritt | Skript, `buildSankey` |
| 46 | Energiefluss | **Energiefluss**: Sankey mit Knoten in Spalten, jede Spalte ein Schritt | Skript, `buildFluss` |
| 47 | Punktfeld | **Punktfeld**: 100 Punkte, Anteile als Farbe, je Anteil ein Schritt | Skript, `buildPunktfeld` |
| 48 | Frage und Antwort | **Frage und Antwort**: Forschungsfrage groß, Antwort als blaue Karte, Stützpunkte als zweiter Schritt | — |
| 49 | Hypothesen | **Hypothesen-Bilanz**: Erwartung je Zeile, Befund als Pille im Schritt (bestätigt · nicht bestätigt · offen) | — |
| 50 | Stimmen | **Zitat**, groß gesetzt | — |
| 51 | Transkript | **Transkript** mit Kodierspalte | — |
| 52 | Kategoriensystem | **Baum**, Äste einzeln aufklappbar | Skript, `buildBaum` |
| 53 | Rundlauf | **Kreisprozess** | Winkel im Skript |
| 54 | Spirale | **Spirale**: der offene Kreis, drei Windungen | Skript, `buildSpirale` |
| 55 | Von oben nach unten | **Trichter** mit Schwund je Stufe | Quelltext |
| 56 | Ausschluss | **Verzweigung**: Ja/Nein-Weichen mit Abgängen | Skript, `buildWeiche` |
| 57 | Aufploppen | **Kachelreihe** mit Skizzen | — |
| 58 | Deckel ab | Metapherngrafik | — |
| 59 | Konvergenz | **Konvergenz**: drei Befunde laufen auf einen Schluss zu, Pfeile und Schluss im letzten Schritt — Gegenstück zur Verzweigung | — |
| 60 | Stärken und Grenzen | **Plus / Minus**: zwei Karten, Zeichen statt Punkte, die Grenzen als Schritt | — |
| 61 | Kernsatz | **Kernsatz mit Erläuterung**: eine Aussage groß in Blau, das Kleingedruckte darunter Zeile für Zeile als Schritte | — |
| 62 | Zeitplan | **Arbeits- und Zeitplan (Gantt)**: Pakete über Quartalen, Heute-Linie als Schritt | — |
| 63 | Drei Botschaften | **Drei Botschaften**: große Ziffer, ein Satz, je eine Karte | — |
| 64 | Quellen | Quellenverzeichnis | — |
| 66 | Zusammenfassung | **Schlussfolie**, bleibt in der Diskussion stehen | — |
| 67 | Fragen an Sie | **Fragen an das Publikum**: nummeriert, groß, als Schritte — bleibt in der Diskussion stehen | — |
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
Forest Plot, Hypothesen-Bilanz, Drei Botschaften, Fragen an das Publikum, Kernsatz mit
Erläuterung, Konvergenz, Gleichung, Slopegraph, Triade, Zwiebel, Pyramide, Zuordnung,
Freikörperbild, Studiendesign, Histogramm, Item-Heatmap, Kennzahl mit Veränderung, Gantt.

Die vier PowerPoint-Muster, die Max am 11.09. gezeigt hat (Kästen mit Titelschild,
Ablauf mit Detailkästen, große Schlagwort-Kacheln, Chevron-Kette mit Spalten), sind
damit auf den Folien 19, 20 und 25 in der Formensprache der Vorlage nachgebaut.
Seit demselben Tag gilt: **mehrere kleine Formen dürfen sich eine Folie teilen**, wenn
eine allein die Fläche nicht füllt (Folie 05).

---

## Vorrat A — Statistik und Ergebnisse

Histogramm (30) und Item-Heatmap (36) sind am 15.09. gebaut. Geblieben:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Netzdiagramm (Radar)** | Ein Profil über mehrere Merkmale, zwei Gruppen übereinander. | mittel |

## Vorrat B — Ablauf, wenn die Reihenfolge die Aussage ist

Gantt (62) ist am 15.09. gebaut. Geblieben:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Gegenläufige Ketten** | Zwei Stränge laufen aufeinander zu. Theorie ↔ Empirie, fachliche Klärung ↔ Lernerperspektive. | mittel |

## Vorrat C — Struktur, wenn die Beziehung die Aussage ist

Triade und Zwiebel (06) und Pyramide (07) sind am 15.09. gebaut. Geblieben:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Concept Map** | Begriffe mit beschrifteten Relationen — auch als Erhebungsergebnis. | mittel |

## Vorrat D — Vergleich und Zuordnung

Zuordnung (10) ist am 15.09. gebaut. Geblieben:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Waage** | Zwei Seiten wiegen unterschiedlich schwer. Für Abwägungen im Ausblick. | klein |

## Vorrat E — fachlich, physiknah

Freikörperbild (14) ist am 15.09. gebaut. Geblieben:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Beschriftete Versuchsskizze** | Aufbau mit Zeigern, die einzeln erscheinen. Die `.sk`-Klassen der Kacheln gibt es schon. | mittel |
| **Repräsentationswechsel** | Realbild → Diagramm → Formel, nebeneinander oder per Morph ineinander. Der Morph von Folie 27 ist wiederverwendbar. | groß |

## Vorrat G — Bild und Aufgabe

Vorgeschlagen am 14.09., am selben Tag gebaut: Bildpaar (24), Foto mit Zeigern (23),
Aufgabenfolie (32), Energiefluss (46), Messkurve (28, samt Modellkurve — damit ist auch
„Modell und Realität" abgedeckt), Hantel (34), zwei Verteilungen (37). Geblieben ist:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Video** | Ein kurzes Versuchsvideo als `<video>`. **Vorbehalt:** Die Datei müsste neben dem Foliensatz liegen oder als Daten-URI hinein (schnell mehrere MB) — bricht das Prinzip „eine Datei, nichts nachzuladen". Zurückgestellt. | klein, aber ein Prinzipienbruch |

## Vorrat F — Medien und Rhetorik

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Bild vollflächig** | Ein Foto ohne Karte, bis an den Rand — als Stimmungsfolie. Bild *mit* Unterschrift und Text ist seit dem 14.09. gebaut (Folie 22, im Kartenraster, endet über der Fußzeile). Offen bleibt nur die Frage vom 10.09., ob ein Bild je bis zur Kante laufen darf. | klein, aber eine Entscheidung nötig |
| **Merksatzfolie** | Eine Aussage groß, sonst nichts. | klein |

---

## Vorrat H — Text strukturieren *(14.09., nach Websuche)*

Rahmen dafür ist **Assertion-Evidence** (Alley, Penn State): der Titel ein ganzer Satz, darunter
ein Beleg, kein Stichpunktblock. Gebaut sind davon: Behauptung + Beleg (44), Frage und Antwort
(48), Stern (08), Plus / Minus (60) am 14.09.; Gegenüberstellung (09), Hypothesen-Bilanz (49),
Drei Botschaften (63), Fragen an das Publikum (67), Kernsatz (61), Konvergenz (59), Gleichung (13)
am 15.09. Geblieben:

| Form | Beziehung / Aussage | Aufwand |
|---|---|---|
| **These – Beleg – Folgerung** | Argumentkette in drei Kästen mit Pfeilen, Sätze statt Stichpunkte. Für die Diskussion. | klein |
| **Klammer-Liste** | Eine Gruppe, eine Klammer: „diese drei Aufgaben messen dasselbe Konstrukt". | klein |
| **Nummerierte Schritte** | Ablauf in Worten: große Ziffer links, ein bis zwei Sätze rechts — die Kacheln (20) senkrecht, mit Platz für Text. | klein |
| **Lesefolie mit Hervorhebung** | Ein Absatz, Stellen werden nacheinander markiert — `<mark>` als Schritte, die Technik hat das Transkript (51). | klein |
| **Definition und Beispiel** | Begriff als Pille, Definition, dann ein Beispiel im Kasten. | klein |
| **Befund / Einordnung** | Zwei Spalten, links das Ergebnis, rechts seine Bedeutung — empfiehlt der Münsteraner Leitfaden für Ergebnisfolien. `.cols` reicht; eine Folie als Muster fehlt. | klein |
| **Was wir wissen / was offen ist** | Limitationen und Ausblick als zwei Spalten mit gegensätzlichen Schildern; nahe an Plus / Minus (60). | klein |
| **Zitat mit Kommentar** | Äußerung links, Einordnung rechts; das Zitat (50) hat den Kommentar nicht. | klein |

## Vorrat I — Daten und Fachliches *(14.09., nach FT Visual Vocabulary und PER-Literatur)*

Gebaut sind davon: divergierende Säulen (44), Punktfeld (47), Pfadmodell (39) am 14.09.;
Item-Antwortkurven (33) und Forest Plot (38) am 15.09., Studiendesign (16) und Kennzahl mit
Veränderung (43) am Nachmittag. Geblieben:

| Form | Sagt aus | Aufwand |
|---|---|---|
| **Modellanalyse (Bao & Redish)** | Modellzustand als Punkt im Dreieck richtig / Fehlvorstellung / gemischt, Vortest → Nachtest als Pfeil. | groß |
| **Kleine Vielfache** | Sechs Klassen, sechs Mini-Messkurven im Raster — Muster auf einen Blick statt sechs Folien. `buildKurve` sechsmal, kleiner. | mittel |
| **Konfidenzband** | Die Messkurve (28) mit Unsicherheit als Fläche; im FT-Raster „Fächer". | klein |
| **Punktstreifen** | Jeder Lernende ein Punkt auf einer Achse — ehrlicher als der Boxplot (29) bei n < 30. | klein |
| **Lollipop** | Balken als Strich mit Punkt, wenn der Wert wichtiger ist als die Fläche. Variante von 40. | klein |
| **Verbundenes Streudiagramm** | Jede Klasse als Pfad Vortest → Nachtest in zwei Merkmalen. Nur, wenn es wirklich zwei Merkmale gibt. | mittel |
| **Kumulierte Kurve** | Wenn Ungleichheit die Aussage ist: y kumulierte Häufigkeit, x das Maß. | klein |

## Wenn davon etwas gebaut wird

Vorgeschlagene Reihenfolge, falls nichts dagegen spricht:

1. **Merksatzfolie** und **Definition und Beispiel** — zwei kleine Textformen
2. **Punktstreifen** und **Lollipop** — zwei kleine Varianten zu Boxplot und Balken
3. **Netzdiagramm** und **Konfidenzband** — Profil und Unsicherheit
4. **Gegenläufige Ketten** und **Waage** — Struktur
5. **Versuchsskizze** — der Zeiger-Baukasten (23) ist der Anfang
6. **Kleine Vielfache** — `buildKurve` sechsmal

Der ganze Vorschlag vom 15.09. (Kernsatz, Konvergenz, Gleichung, Slopegraph, Studiendesign,
Kennzahl mit Veränderung, Triade, Pyramide, Zwiebel, Zuordnung, Freikörperbild) und dazu Gantt,
Histogramm und Item-Heatmap sind am selben Tag gebaut worden.

**Hinweis ab hier:** Der Musterbogen hat 67 + 3 Folien. Das Register ist damit an der
unteren Stufe angekommen (813 px Fensterhöhe: 97 %, 720 px: 105 %). Entschieden am 15.09.:
so lassen — die Vorlage zeigt Möglichkeiten, echte Vorträge haben 15–25 Folien. Weitere
Formen dürfen dazukommen; das Register ist dann bei kleinen Fenstern voll.

Die aufwendigsten bleiben **Modellanalyse**, **Concept Map** und der **Repräsentationswechsel**.

Für Rasterbilder gilt seit dem 14.09.: vor dem Einbetten Weißrand beschneiden, auf
etwa 1200 px Breite bringen, Farbzahl reduzieren, wenn es eine Zeichnung ist (die
Klimabox: 3508 × 2480 und 192 KB → 1200 × 989 und 21 KB). Höchstens 410 px hoch auf
der Folie (seit dem 15.09., Grenze 650), mit einzeiliger Unterschrift.

### Randbedingungen, die für alles gelten

* Nutzbare Fläche 1144 × 610 px, Abbildungen höchstens 430 px hoch — und so hoch sollen
  sie auch werden: Karten so hoch wie ihr Inhalt, der Inhalt so groß wie die Fläche (15.09.). Breite Formen
  (Zeitleiste, Stapelbalken, Schwimmbahnen) passen nur quer, nicht neben einer Textspalte.
* Datengetriebenes folgt dem Muster von `buildFall`: Zahlen als Array im Quelltext,
  Achsen und Geometrie daraus gerechnet.
* Eine Folie je Form. Keine Sammelfolien.
* Bewusst nicht: Kreis- und Donutdiagramme (Balken lesen sich besser), Wortwolken, alles
  Dreidimensionale.
* Keine neuen Farben ohne ausdrückliche Bitte. Blau-Staffel und Grau reichen für zwei
  bis fünf Gruppen; Rot und Grün sind mit „gescheitert" und „trägt" belegt.
* Formeln immer als `data-tex`, dann `python3 werkzeuge/formeln.py`. Einzelne Zeichen
  **außerhalb** einer Formel (`Δ π ≈ ≤ → ←`) stehen direkt im Text — die Schrift hat
  sie. Was sie nicht hat (`↔ ⇒ ∇`), gehört in eine Formel.
