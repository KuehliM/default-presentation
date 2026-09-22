# Arbeitsanweisung für dieses Repository

Foliensatz als einzelne HTML-Datei. Diese Datei beschreibt die Regeln so, dass
sie ohne Rückfrage befolgt werden können. **Zuerst lesen, dann anfassen.**

## Reihenfolge zu Sitzungsbeginn

1. Diese Datei.
2. Das neueste Protokoll in `Sessions/` — dort stehen Begründungen und bereits
   zugeschnappte Fallen.
3. Bei Layoutfragen **nicht schätzen, sondern messen:** `python3 werkzeuge/pruefen.py`.

## Was wo liegt

```
default-presentation/
├── CLAUDE.md               diese Datei
├── README.md               Doku für Menschen — einzige Stelle neben dem Skript mit der Tastenbelegung
├── vorlage.html            die Vorlage, zugleich Musterbogen
├── Darstellungsformen.md   Vorrat: was gebaut ist (mit Foliennummern), was noch kommen könnte
├── Sessions/<datum>.md     Protokolle; bei nennenswerten Änderungen ein neues anlegen
├── werkzeuge/              alle Skripte; geholt/ (ignoriert) für Temml und Schriften
└── quellen/                Klimabox.png, RWTH_Logo_3.svg
```

| Datei | Rolle |
|---|---|
| `vorlage.html` | **Die Vorlage, zugleich Musterbogen.** 67 Folien Vortrag, 3 Anhang; jede Darstellungsform genau einmal. Wird nicht vorgetragen, sondern folienweise in Vorträge kopiert. Der Kopfkommentar erklärt Aufbau, Bedienung und Grenzen. |
| `werkzeuge/neu.py` | **Legt einen Vortragsordner an:** `python3 werkzeuge/neu.py <ordner> "Titel"` — Vortragsdatei mit dem Unterbau der Vorlage (drei Folien, Platzhalter), dazu Kopien von `vorlage.html`, `Darstellungsformen.md`, den vier Werkzeugen, eine eigene `CLAUDE.md` aus `vortrag-CLAUDE.md`, `bilder/`, `.gitignore`. Dateiname aus dem Ordnernamen. |
| `werkzeuge/vortrag-CLAUDE.md` | Vorlage der Arbeitsanweisung für einen Vortragsordner — Kurzfassung der Regeln hier, Ablauf, was dort nicht passiert. **Wer hier Regeln ändert, zieht sie dort nach.** Platzhalter `{datei}`, `{datum}`. |
| `werkzeuge/formeln.py` | Setzt alle Formeln: liest LaTeX aus `data-tex`, schreibt MathML hinein, bettet Fira Math ein. Nach jeder Formeländerung laufen lassen. |
| `werkzeuge/pruefen.py` | Misst jede Folie im Browser: Überlauf, Füllstand, kleinste Schrift; „Luft" unter 85 %. |
| `werkzeuge/pdf.py` | Schreibt das PDF: eine Seite je Folie samt Anhang, jede Folie auf dem letzten Schritt, Fußzeile je Seite. Nutzt den Druckmodus `?druck=1` und Chrome headless; `[datei.html] [ziel.pdf]`. |
| `werkzeuge/schriften.py` | Bettet Fira Sans und Fira Mono als Teilsatz ein (Latein, Griechisch, Pfeile, Rechenzeichen). `--pruefen` meldet Zeichen, die aus der Schrift fallen. Nur bei Änderung des Vorrats laufen lassen. |
| `quellen/Klimabox.png` | Quelle des einen Rasterbilds (Folie „Klimabox"). In `vorlage.html` steckt es beschnitten, auf 1200 px gebracht, 64 Farben, als Daten-URI — die Datei lädt nichts nach. |
| `quellen/RWTH_Logo_3.svg` | Quelle des Logos. In `vorlage.html` steht es als Symbol `logo-rwth` am Anfang von TEIL B, eingebettet. Logo tauschen: Pfade und `viewBox` im Symbol ersetzen, sonst nichts. |

Alle Werkzeuge nehmen einen Dateipfad (relativ zum Arbeitsverzeichnis oder zum Ordner über
`werkzeuge/`), ohne Angabe die Vorlage. Sie liegen in `werkzeuge/`, damit das Repo an der
Wurzel nur zeigt, was man liest oder kopiert — und damit `neu.py` sie als Ordner mitnehmen kann.

**Regel:** Es gibt **eine** Vorlage; Vorträge sind eigene Dateien, die `neu.py` daraus
anlegt (seit dem 15.09.). Ein Vortrag ist ein Schnappschuss des Unterbaus vom Tag seiner
Erzeugung und bekommt spätere Änderungen der Vorlage nicht mit — es gibt bewusst **kein**
Übertragungsskript: Die frühere `anleitung.html` war eine zweite Datei mit demselben
Unterbau und einem eigenen Übertragungsskript; beides ist am 11.09. entfallen, der Aufwand
stand in keinem Verhältnis, und die Anleitung war monatelang unbemerkt kaputt. Wer eine
Verbesserung des Unterbaus in einen Vortrag holen will, kopiert den Block von Hand oder
erzeugt den Vortrag neu. **Am Unterbau wird nur in `vorlage.html` gearbeitet;** in einem
Vortrag nur an seinen Folien und seinen Zahlen im Skript — dort gilt die `CLAUDE.md` des
Vortragsordners, nicht diese. Der Arbeitsablauf steht in der `README.md` („Einen neuen Vortrag
anlegen"), samt Rezept für Claude in einem frischen Ordner: Repo nach `/tmp` klonen,
`neu.py .` aufrufen. Vorträge liegen **nicht** in diesem Repo. PDFs, `.claude/` und
`werkzeuge/geholt/` sind per `.gitignore` ausgenommen.

---

## Geometrie — die harten Grenzen

Die Bühne ist fest **1280 × 720** (Tokens `--stage-w` / `--stage-h`) und wird als
Ganzes skaliert. Alle Maße unten sind Bühnenpixel, unabhängig vom Bildschirm.

```
        0                                                        1280
        ├─────────────────────────────────────────────────────────┤
     0  │  Fortschrittsbalken (4 px, liegt über der Folie)        │
    40  │  ┌───────────────────────────────────────────────────┐  │  ← Inhalt beginnt
        │  │  Abschnitt (eyebrow)                              │  │
        │  │  Titel                                            │  │
        │  │  … Inhalt …                                       │  │
   650  │  └───────────────────────────────────────────────────┘  │  ← Inhalt endet
        │      Fußzeile: Logo · Name · Nummer                     │
   720  └─────────────────────────────────────────────────────────┘
          68                                                  1212
```

| Größe | Wert | Token |
|---|---|---|
| Satzspiegel links/rechts | 68 px | `--pad-x` |
| Inhalt beginnt bei | 40 px | `.slide` padding-top |
| **Inhalt endet bei** | **650 px** | `720 − --pad-b (70)` — seit dem 15.09. (vorher 640 / 80) |
| Nutzbare Höhe | **610 px** | |
| Nutzbare Breite | **1144 px** | |
| Abbildungen höchstens | 430 px hoch | `.slide figure svg` — das ist 650 − Kartenoberkante 144 − Polsterung 48 − Lücke 10 − einzeilige Unterschrift 20; bei zweizeiliger Unterschrift passen nur 409 |
| Rasterbilder höchstens | 410 px hoch | `.slide figure img` |

**Unverhandelbar:** Text und Karten dürfen nie unter 650 px reichen. Der Streifen
darunter gehört der Fußzeile (Logo ab 662). Für `.slide.hero` (Titel- und Dankfolie) gilt
**584 px** (seit dem 15.09. abends): Die blaue Karte wächst mit ihrem Inhalt und endet 40 px
unter der Byline; das große Logo beginnt bei 644, dazwischen bleiben 20 px. Ein Titel darf
drei Zeilen haben (84 px), dann mit einzeiligem oder zweizeiligem Untertitel — mehr passt nicht.
Besser: ab etwa 27 Zeichen `h1.lang` (72 px), dann stehen 31 Zeichen je Zeile und ein Titel
bis 60 Zeichen bleibt zweizeilig (Max' Entscheidung vom 15.09. abends, nicht noch kleiner).

**Die Fläche wird genutzt (seit dem 15.09., Max):** Karten sind so hoch wie ihr Inhalt —
**keine** gestreckten Karten, keine erzwungene Symmetrie zwischen Spalten. Aber der Inhalt
wird so groß gebaut, wie die Fläche hergibt: **eine Grafik bekommt die Höhe, bei der ihre
Karte bei 650 endet.** Die Bauer rechnen aus `h`; die `viewBox`-Höhe ist deshalb je Folie
anders (620 × 430–450 in der breiten Spalte, 1112 × 386–436 auf voller Breite, je nach
Unterschrift und Fußnote). Wer eine Grafik einbaut: `python3 werkzeuge/pruefen.py` sagt, wie viel
Platz bleibt („frei") — den nimmt die Grafik. Textfolien bleiben, wie ihr Inhalt sie macht;
dort ist Luft in Ordnung. Der Streifen zwischen 650 und der Fußzeile ist Absicht (12 px).

### Wie viel passt hinein

Erfahrungswerte aus dem gemessenen Bestand (`python3 werkzeuge/pruefen.py`):

| Aufbau | belegte Höhe | Füllstand |
|---|---|---|
| Kopf allein (Abschnitt + Titel einzeilig) | ~110 px | — |
| Kopf + Karte mit 4 langen Stichpunkten (je 2 Zeilen) | 496 px | 76 % |
| Kopf + Kennzahlenreihe + 2 Stichpunkte | 458 px | 70 % |
| Kopf + zwei Spalten mit Diagramm und Text | 583 px | 91 % |
| Kopf + zwei Spalten: Bild (360 px) mit einzeiliger Unterschrift, 4 Stichpunkte | 582 px | 90 % — zweizeilige Unterschrift: 94 %, eng |
| Kopf + Bildpaar (zwei Bilder à 360 px, je eine Unterschrift) | 582 px | 90 % |
| Kopf + Foto mit Zeigern (SVG 2200 × 660, volle Breite) + Unterschrift | 549 px | 85 % |
| Kopf + wide-left: Diagramm 620 × 340 mit Unterschrift + 3–4 Stichpunkte (Hantel, Forest, Slopegraph, Histogramm, Heatmap, Freikörperbild) | 544–564 px | 84–87 % |
| Kopf + Aufgabe (Stamm 2 Zeilen, 4 Optionen) + Fußnote | 531 px | 82 % |
| Satztitel (2 Zeilen, 38 px) + Säulen 1112 × 300 + Fußnote | 565 px | 88 % |
| Frage (2 Zeilen, 34 px) + Antwortkarte mit 2 Punkten + Fußnote | 421 px | 64 % |
| Kopf + Gegenüberstellung, 3 Zeilen + Fußnote | 511 px | 79 % |
| Kopf + Hypothesen-Bilanz, 4 Zeilen + Fußnote | 457 px | 70 % |
| Kopf + drei Botschaften / drei Fragen | 404–413 px | 61–62 % |
| Kernsatz (2 Zeilen, 33 px) + Erläuterung, 3 Zeilen + Fußnote | 436 px | 66 % |
| Kopf + Gleichung (3 Terme à 190 px) + 2 Stichpunkte + Fußnote | 475 px | 73 % |
| Kopf + Konvergenz, 3 Befunde + Fußnote | 499 px | 77 % |
| Kopf + Studiendesign (Kopfzeile + 2 Gruppen) + 2 Stichpunkte + Fußnote | 529 px | 82 % |
| Kopf + 4 Kennzahlen mit Veränderung + 2 Stichpunkte + Fußnote | 487 px | 75 % |
| Kopf + Gantt, 6 Zeilen + Fußnote | 508 px | 78 % |
| Kopf + Pyramide / Zuordnung (1112 × 300–320) mit Unterschrift | 535 px | 83 % |
| Kopf + zwei Grafiken 520 × 280 nebeneinander, Unterschriften à 2 Zeilen + Fußnote | 552 px | 85 % — mit 300 hoch und 3 Zeilen: 92 % |
| Kopf + Quellenverzeichnis, 5 Einträge | 423 px | 64 % |
| Kopf + Herleitung, 6 Zeilen mit Brüchen und Wurzeln | 577 px | 90 % |
| Kopf + Vergleichstabelle, 4 Spalten × 5 Zeilen | 525 px | 81 % |
| Kopf + Zeitleiste (zwei Ebenen, 7 Marken) + 2 Stichpunkte | 562 px | 87 % |
| Kopf + 10 waagerechte Balken mit Unterschrift | 545 px | 84 % |
| Kopf + Likert, 6 Aussagen mit Legende | 545 px | 84 % |
| Kopf + Chevron-Kette, 3 Spalten à 2–3 Punkte | 442 px | 67 % |
| Kopf + 4 große Kacheln | 494 px | 76 % |
| Kopf + 2 Karten mit Titelschild à 2 Punkte | 474 px | 72 % |
| Kopf + Schwimmbahnen, 4 Phasen × 3 Rollen | 584 px | 91 % |
| Kopf + zwei kleine Grafiken nebeneinander (420 × 236) + Fußnote | 563 px | 87 % |
| Kopf + Sankey / Baum / Weichen (1112 × 250–330) mit Unterschrift | 467–565 px | 71–88 % |
| Kopf + Transkript, 6 Zeilen | 442 px | 67 % |

Die Tabelle ist vor dem 15.09. gemessen (Grenze 640); Grafikfolien stehen seither bei
96–100 %, weil ihre Grafik die Fläche nimmt. **Unter 85 % meldet `pruefen.py` „Luft"** —
bei einer Grafikfolie heißt das: Grafik höher bauen; bei einer Textfolie ist es in Ordnung.
Überlauf über 650 bleibt der Fehler. Wird es auf dem Beamer gedrängt: Inhalt kürzen, nicht
die Schrift verkleinern.

---

## Schriftgrade

Nicht unterschreiten: **15 px** für alles, was gelesen werden soll. Auszeichnungen
dürfen kleiner sein.

| Rolle | Klasse | Grad |
|---|---|---|
| Titelfolie | `h1` | 84 px — langer Titel `h1.lang` 72 px (zwei Zeilen à ~31 Zeichen statt ~26) |
| Folientitel | `h2` | 46 px — als Satz (`.slide.these`) 38 px |
| Untertitel, Vorspann | `.lead` | 26 px |
| Aufzählung Ebene 1 | `ul.points li` | 19 px |
| Aufzählung Ebene 2 | verschachteltes `ul` | 17 px |
| Aufzählung Ebene 3 | doppelt verschachtelt | 15,5 px |
| Fließtext | `.body` | 19 px |
| Quellen | `ul.refs li` | 16 px |
| Code | `pre` | 14,5 px |
| Zitatfolie | `.zitat` | 33 px |
| Forschungsfrage | `.frage` | 34 px, Antwort `.antwort-kurz` 23 px |
| Fragen an das Publikum | `ol.fragen li` | 28 px |
| Botschaft | `.botschaft p` | 21 px, Ziffer 64 px |
| Kernsatz | `.kern` | 33 px, blau; Erläuterung `.erl p` 19 px |
| Gleichung | `.gleichung .term b` | 30 px, Unterzeile 16 px, Zeichen `.op` 64 px |
| Konvergenz | `.konv-befund` / `.konv-ziel` | 19 px / 21 px |
| Studiendesign | `.design-kopf` / `.design-gruppe` / Zellen | 15 px Versalien / 17 px / 15 px |
| Kennzahl mit Veränderung | `.stat .von` / `.stat .delta` | 17 px / 14 px Mono-Pille |
| Gantt | `.gantt-q` / `.gantt-aufgabe` / `.gantt-balken` | 15 px Versalien / 16 px / 14 px |
| Herleitung | `.herleit` | 23 px |
| Formel | `math` | 26 px, in der Herleitung 23 px |
| Tabelle | `table.vgl` | 18 px |
| Transkript | `.trans` | 17 px |
| Abschnittszeile | `.eyebrow` | 12,5 px |
| Bildunterschrift | `figcaption` | 13,5 px |

---

## Bausteine

Karten entstehen automatisch: `.cols > *` sowie `ul.points`, `ul.refs`, `figure`
und `.keys` als **direkte Kinder** von `.slide` bekommen weißen Grund, Radius und
Schatten.

| Klasse | Wirkung |
|---|---|
| `.slide.hero` | Titel-/Abschlussfolie: blaue Karte, weiße Schrift, ohne Fußzeile. Die Karte **wächst mit dem Inhalt:** Die Folie ist ein Raster aus vier Zeilen (Abschnitt, Titel, Untertitel, Byline), das `::before` spannt sie alle und ragt 40 px darüber hinaus — Titel bis drei Zeilen |
| `.cols` | zwei gleich breite Spalten, je eine Karte |
| `.cols.wide-left` | Verhältnis 1,15 : 0,85 |
| `ul.points` | drei Ebenen: Punkt, Strich, Viereck — `<ul>` einfach verschachteln |
| `ul.points.long` | kleinerer Grad für textreiche Folien |
| `ul.refs` | Quellen mit hängendem Einzug |
| `.stats` / `.stat` | Kennzahlenkacheln |
| `.keys` | zweispaltige Definitionsliste |
| `.tiles` / `.tile` | Kachelreihe für Bilder oder Skizzen |
| `figure` + `img` | Rasterbild als Daten-URI in einer Abbildung: Kasten auf Kartenbreite, `object-fit: contain` hält das Bild unverzerrt und mittig |
| `.chip` | Pille für Schlagworte — im Abschnittstrenner als Agenda-Chips genutzt |
| `.cite` / `.source-note` | Beleg im Fließtext, Fußnote |
| `.pops` | ploppt beim Erscheinen auf statt einzublenden |
| `data-anim` | tritt beim Folienwechsel gestaffelt auf |
| `data-step="n"` | erscheint beim n-ten Pfeildruck |
| `data-step-until="n"` | verschwindet beim n-ten wieder |
| `data-keep` | bleibt sichtbar, `data-step` löst nur die eigene Bewegung aus |
| `<aside class="notes">` | Sprechnotizen, nur in der Vortragendenansicht |
| `.slide.anhang` | Folie für die Fragerunde — eigener Abschnitt unten |
| `.slide.trenner` | Abschnittstrenner: blaue Karte über der Fläche, Agenda als Chips, der laufende mit `.aktiv`; Fußzeile bleibt. **Eröffnet in der Übersicht automatisch eine Gruppe** — Trennzeile mit dem `data-title`, die Folien danach in neuer Zeile |
| `.kacheln` / `.kachel` | große Kacheln: `.nr`, Schlagwort in `b`, eine Zeile in `span`; `data-step` + `data-keep` färbt eine Kachel beim Schritt blau |
| `.kette` / `.glied` / `.kette-kopf` | Chevron-Kette: Pfeilkopf (clip-path) über einer Spalte `ul.points`; das erste Glied ohne Kerbe, links gerundet |
| `.karten` / `.karte` | Karten mit Titelschild: `h3` sitzt als blaue Pille halb auf der Oberkante, darunter `ul.points` |
| `.bahnen` / `.bahn-koepfe` / `.bahn` | Schwimmbahnen: Kopfzeile und jede Bahn sind eigene Raster mit derselben Spaltenvorlage (`--phasen`) **und derselben rechten Polsterung** — sonst stehen die Köpfe nicht über den Zellen; `.bahn-rolle` links, `.bahn-zelle` je Phase, `.leer` als Rahmen |

### Anhangsfolien

`<section class="slide anhang">`. Eine Klasse trägt alles Weitere:

Geblättert wird **ganz normal**: die Pfeile gehen durch den Anhang hindurch wie durch
jede andere Folie. Eigen sind ihm nur drei Dinge:

* **Fortschrittsbalken** zählt ihn nicht (`total` lässt ihn aus, `scaleX` ist auf 1
  begrenzt). Auf der letzten Vortragsfolie steht der Balken voll und bleibt es.
* **Register** zeigt ihn nicht — es bliebe sonst für den Vortrag weniger Platz. Die
  **Übersicht** zeigt ihn, abgesetzt unter einer Trennzeile — als letzte Gruppe.

### Druckmodus und PDF

Vor jedem Drucken (`beforeprint`, also Cmd+P wie `pdf.py`) stellt `druckAn()` jede
Folie auf ihren letzten Schritt (`showSteps(sl, stepsOf(sl))`) und hängt jeder Folie
außer `.hero` eine Kopie der Fußzeile als `.foot-druck` mit ihrer Nummer an;
`afterprint` nimmt es zurück. `@media print` zeigt die Kopie und setzt Wachsendes und
Aufploppendes in die Endlage. `?druck=1` hält den Zustand dauerhaft. `python3 werkzeuge/pdf.py`
druckt kopflos (`--print-to-pdf`, `@page` 1280 × 720 px) und prüft Seiten gegen Folien. **Wer eine
Animation baut, die per JavaScript oder Keyframes zu einer Endlage läuft, muss ihr im
Druck die Endlage geben** — der Morph prüft `root.classList.contains('druck')`, Stiel und
Blätter haben eine Print-Regel. `vorlage.pdf` ist Erzeugnis, nicht Quelle (`.gitignore`).

### Gruppen in der Übersicht

Die Übersicht (`0`) ist in **Gruppen** geteilt: Jede `.slide.trenner` eröffnet eine
(Trennzeile mit ihrem `data-title`, die Folien bis zum nächsten Trenner beginnen in
einer neuen Zeile), der Anhang bildet die letzte. Die Folien vor dem ersten Trenner
stehen ohne Zeile oben. Das geschieht **automatisch** aus den Klassen (`gruppen` im
Skript, `passeUebersicht()` rechnet die Trennzeilen in die Kachelgröße ein): Wer
einen Abschnittstrenner einbaut, muss dafür nichts weiter tun. Angefangene Zeilen
stehen mittig — so gewünscht, nicht linksbündig „nachbessern".
* **Kein Aufbau.** Eine Schleife entfernt `data-anim` und `data-step` von allen
  Anhangsfolien; sie muss **nach** den Diagramm-Bauern stehen, die `data-step` selbst
  setzen. In der Fragerunde soll die Antwort sofort ganz dastehen.

Die Fußzeile zeigt `A1`, `A2`, … über `nummer(i)`.

Weil Register und Übersicht ihre Karten nicht mehr über die Position zuordnen können,
trägt jede Karte ihre Folienzahl in `dataset.nr`; `paint()` vergleicht damit. Wer am
Aufbau beider Leisten etwas ändert, muss das mitnehmen.

Titel nach der **Frage** benennen, nicht nach dem Inhalt.

### Zahlen, Formeln, Belege

| Klasse | Wirkung |
|---|---|
| `.zeit` | Zeitleiste. Raster mit `--spalten`; `.zeit-phase` trägt `--von` und `--dauer`, `.zeit-marke` trägt `--bei`. Darüber eine zweite Ebene: `.zeit-ebene` (grau) mit `.zeit-marke.klein` für Anfang und Ende — Karte und Punkt in derselben Farbe |
| `table.vgl` | Vergleichstabelle; `.mk.ja` / `.mk.halb` / `.mk.nein` als Ausfüllgrad, `.num` für Ziffernschrift |
| `.zitat` | eine Äußerung, groß gesetzt; `.zitat-quelle` als Beleg darin |
| `.trans` | Transkript: `.nr`, `.wer`, `.txt`, `.kode`; `<mark>` hebt Stellen hervor |
| `.herleit` | Herleitung; jede Zeile `.lhs` · `.rel` · Formel · `.grund`, alle am Relationszeichen bündig |
| `.tex` + `data-tex` | Formel: LaTeX im Attribut, MathML darin — von `formeln.py` gesetzt |
| `#kiSvg` | Säulen mit 95-%-Konfidenzintervall — Werte im Skript, `buildKI` |
| `#balkenSvg` | Balken waagerecht, Nennungen absteigend — sortiert im Skript, `buildBalken` |
| `#likertSvg` | Likert: divergierende Stapelbalken, Ablehnung grau nach links, Zustimmung blau nach rechts; Skala aus den Daten — `buildLikert` |
| `#sankeySvg` | Übergangsmatrix als Sankey: 3 × 3 Zahlen, Bandbreite nach Anzahl, Rückwege als Schritt — `buildSankey`, Klassen `.ub-*` |
| `#vennSvg` / `#felderSvg` | Schnittmenge (drei Kreise, Mitte als Schritt) und Vier-Felder-Matrix (jeder Baustein nennt sein Feld 0–3 und steht dort mittig, Chipbreite am Text gemessen) — `buildVenn`, `buildFelder`; teilen sich eine Folie |
| `#spiraleSvg` | Spirale: Radius wächst mit dem Winkel, je Windung vier Stationen, jede Windung ein Schritt — `buildSpirale` |
| `#weicheSvg` | Verzweigung: Ja/Nein-Weichen in einer Reihe, „nein" zweigt nach unten ab; Startzahl und Abgänge im Skript, Rest gerechnet — `buildWeiche` |
| `#baumSvg` | Baum: verschachtelte Liste, Wurzel oben, jeder Ast klappt als eigener Schritt auf — `buildBaum` |
| `#hakeSvg` | Zugewinn: Nachtest gegen Vortest mit Linien gleichen *g* — `buildHake` |
| `#kurveSvg` | Messkurve über der Zeit: Reihen als Arrays, Achsen daraus, Modellkurve aus Parametern — `buildKurve`, Klassen `.kv-*` |
| `#hantelSvg` | Hantel: Prä/Post je Aufgabe, sortiert nach Zuwachs — `buildHantel`, `.ha-*` |
| `#glockenSvg` | Zwei Normalverteilungen, Cohens *d* als Klammer, Φ(*d*) als Anteil — `buildGlocken`, `.gl-*` |
| `#flussSvg` | Energiefluss: Sankey mit Knoten in Spalten, Liste `KNOTEN`/`FLUSS`, je Spalte ein Schritt; Beschriftung mit weißem Halo (`paint-order`) — `buildFluss`, `.ef-*` |
| Zeiger (`.zg-*`) | Foto mit Zeigern: `image` und Zeiger-Gruppen in einem SVG (2200 breit), Grade auf 31 Einheiten = 15 px gerechnet — kein Skript, alles im Quelltext |
| `#sternSvg` | Stern: Kern und Satelliten auf einer Ellipse, Pillenbreite am Text gemessen — `buildStern`, `.st-*` |
| `#pfadSvg` | Pfadmodell: Knoten mit Lage, Kanten mit Koeffizient, Pfeile enden am Kastenrand; Koeffizienten seitlich der Linie versetzt — `buildPfad`, `.pf-*` |
| `#abweichungSvg` | Divergierende Säulen um eine Nulllinie, sortiert, Mittel als Schritt — `buildAbweichung`, `.ab-*` |
| `#punktfeldSvg` | Punktfeld: 100 Punkte, Anteile als Liste ganzer Zahlen, je Anteil ein Schritt — `buildPunktfeld`, `.pk-*` |
| `#ircSvg` | Item-Antwortkurven: je Option eine Linie über Gruppenmitten, Endbeschriftungen mit 15 px Mindestabstand entzerrt, Marke gerechnet — `buildIRC`, `.ir-*` |
| `#forestSvg` | Forest Plot: Punkt und Antenne je Zeile, Gesamt als Raute im Schritt — `buildForest`, `.fp-*` |
| `.gegen` | Gegenüberstellung: Raster 1fr · 48px · 1fr, Zeilenlinien über `border-top`, rechte Seite als Schritte |
| `.bilanz` / `.hyp` | Hypothesen-Bilanz: Raster 52px · 1fr · auto, Befund als Pille (`.ja` / `.nein` / `.offen`) mit `data-step` |
| `.botschaften` / `.botschaft` | drei Karten, Ziffer 64 px, Satz 21 px |
| `.kern` / `.erl` | Kernsatz mit Erläuterung: `p.kern` statt `h2`, darunter `.erl` als Karte (steht in der Kartenliste von Abschnitt 8) mit einem `p` je Zeile, `b` in Blau |
| `.gleichung` | A + B → C: `.term` als Kachel (`b`, `span`), `.term.ergebnis` blau, `.op` als Zeichen; Term und Zeichen tragen dasselbe `data-step` |
| `.konv` | Konvergenz: Raster 1,05fr · 120px · 0,95fr. Links `.konv-quellen` mit drei `p.konv-befund` in gleich hohen Zeilen ohne Lücke (Luft als `margin` in der Karte), Mitten bei 1/6, 1/2, 5/6; `.konv-mitte` mit SVG `preserveAspectRatio="none"` und `vector-effect: non-scaling-stroke`; `p.konv-ziel` blau, mittig, Spitze als `::before` |
| `.design` | Studiendesign: Raster `190px var(--spalten)` (Spaltenvorlage an der Folie), `.design-kopf` mit `span`, `.design-gruppe`, `.design-mess` (Pille, `.offen` gestrichelt), `.design-block` (blau, `.kontrolle` Rahmen); Karte über Abschnitt 8 |
| `.stat .von` / `.stat .delta` | Kennzahl mit Veränderung: `.von` über dem `b`, `.delta` absolut oben rechts (`.stat` ist dafür `position:relative`), `.null` grau |
| `.gantt` | Zeitplan: Kopf und Zeilen eigene Raster mit `--links` (230 px) + `--spalten`; Balken `--von`/`--dauer`; `.gantt-heute` absolut mit `--anteil`, rechnet die Kartenpolsterung `--kp` ein, weil der Bezug der Polsterkasten der Karte ist; Karte über Abschnitt 8 |
| `#triadeSvg` / `#zwiebelSvg` | Triade (Pillenbreite gemessen, Doppelpfeile an den Kantenmitten) und Zwiebel (außen zuerst gezeichnet, innen zuerst eingeblendet) — `buildTriade`, `buildZwiebel`, `.tr-*`, `.zw-*` |
| `#pyramideSvg` | Pyramide: Trapeze aus Stufenzahl, Erläuterung rechts — `buildPyramide`, `.py-*` |
| `#zuordnungSvg` | Zuordnung: zwei Spalten, Linien aus Indexpaaren, je Ziel ein Schritt — `buildZuordnung`, `.zu-*` |
| `#kraefteSvg` | Freikörperbild: alles aus dem Winkel gerechnet, Pfeilspitzen als Polygone (keine Marker — Marker hängen an IDs, die Miniaturen entfernen IDs) — `buildKraefte`, `.fk-*` |
| `#histoSvg` | Histogramm: Klassen aus Rohwerten, `nmax` mit einer Stufe Luft für die Zahl über der Säule, Schwelle und Anteil gerechnet — `buildHisto`, `.hg-*` |
| `#heatSvg` | Item-Heatmap: `fill-opacity` = 0,05 + 0,9 · (v/100)^1,5, Schrift hell ab 58 — `buildHeat`, `.hm-*` |
| `#slopeSvg` | Slopegraph: Paare Prä/Post je Person, steigend blau, fallend grau; Mittel und Zahl der Fallenden gerechnet, Beschriftungen rechts mit 18 px Mindestabstand — `buildSlope`, `.sl-*` |
| `ol.fragen` | nummerierte Fragen 28 px, Ziffer 44 px aus CSS-Zähler; als Karte |
| `.slide.these` | Behauptung + Beleg: `h2` als Satz in 38 px, zwei Zeilen; darunter genau ein Beleg |
| `.frage` / `.antwort-karte` | Frage groß, Antwort als blaue Karte (steht in der Kartenliste von Abschnitt 8, eigene Regel hält sie blau) |
| `.pm.plus` / `.pm.minus` | Plus / Minus: Zeichen statt Punkte über `ul.points li::before` |
| `.aufgabe` | Aufgabenfolie, nur CSS: `--p` je Option, `.antwort` trägt den Schritt, die richtige Option `data-step` + `data-keep` |

### Formelsatz

Entschieden am 11.09.: **MathML mit eingebetteter Fira Math.** Kein JavaScript, keine
Fremdbibliothek — den Satz erledigt der Browser anhand der MATH-Tabelle der Schrift.

Im Quelltext steht LaTeX, das Erzeugnis daneben:

```html
<span class="tex" data-tex="T = 2\pi\sqrt{\dfrac{l}{g}}"><math>…</math></span>
```

Das Attribut ist die Quelle, das MathML das Erzeugnis. **Formel ändern heißt: Attribut
ändern, dann `python3 werkzeuge/formeln.py`.** Das Skript geht über `vorlage.html`,
übersetzt mit Temml und setzt den Stilblock mit der Schrift.

* **Die Kursive ist echt.** Fira Math bringt die Glyphen aus dem Unicode-Block
  „Mathematical Alphanumeric Symbols" mit; der Browser tauscht die Zeichen dorthin
  (`text-transform: math-auto`). Nachgemessen: `<mi>a</mi>` ist 56,91 px breit, genau
  wie U+1D44E, und weicht von der aufrechten (54,41) wie von der schräg gestellten
  (50,00) ab. Ein `<i>` wäre bloß geneigt gewesen — die Datei enthält **keinen**
  kursiven Schnitt.
* **Hervorheben** mit `\colorbox{#e8f1fa}{$…$}`.
* **Grundgrad 26 px.** Nicht kleiner: doppelt Tiefgestelltes ist die Hälfte davon und
  fiele sonst unter die 15-px-Lesegrenze.
* **Voraussetzung beim Vortragen:** MathML Core — Chrome/Edge ab 109, Safari ab 16.4,
  Firefox seit je. Bewusst in Kauf genommen zugunsten der Schrifteinheit.
* Der frühere handgebaute Satz (`.m`, `.frac`, `.wurzel`, `.vec`, `.hl`) ist
  **entfernt**, seit dem 11.09. auch `.gr` — die Textschrift trägt die Zeichen selbst.

**Bedingung, die über allem steht:** Die fertige Datei stellt **keine** Anfrage nach
außen. Auf Tagungen steht selten der eigene Rechner auf dem Pult. `formeln.py` prüft
das nach jedem Lauf und bricht ab, wenn auch nur ein `url(http…)` übrig bleibt.

**Zeichenvorrat.** Seit dem 11.09. schneidet `schriften.py` den Teilsatz selbst aus
der vollständigen Fira (Ausgabe 4.203, Maße unverändert): Latein mit Extended-A,
Griechisch, Satzzeichen, Hoch-/Tiefgestelltes, Pfeile `← → ↑ ↓`, Rechenzeichen
`√ ≈ ≤ ≥ ≠ ∞ ∑ ∫ ∂ ± ×`. Diese Zeichen im Fließtext **direkt setzen**, ohne Klasse.
**Fehlt weiterhin,** weil Fira Sans es nicht hat: `↔ ⇒ ∇ ℏ ℃ ᵢ ■ ● ▲`. Solche Zeichen
in eine Formel (`data-tex`) setzen — Fira Math kennt sie. Prüfen:
`python3 werkzeuge/schriften.py --pruefen`. Datei je Schnitt 38 KB (Sans) / 21 KB (Mono),
Kyrillisch bewusst weggelassen (+11 KB je Schnitt).

### Eine Folie anlegen

```html
<section class="slide" data-title="Ergebnisse">
  <p class="eyebrow" data-anim>Auswertung</p>
  <h2 data-anim>Was wir gefunden haben</h2>
  <ul class="points" data-anim>
    <li>Erster Punkt.</li>
    <li data-step="1">Erscheint beim ersten Pfeildruck.</li>
  </ul>
  <aside class="notes">Zwei Minuten. Auf die Streuung hinweisen.</aside>
</section>
```

`data-title` beschriftet die Registerkarte. Register, Übersicht, Fortschrittsbalken
und Zifferntasten richten sich selbst nach der Zahl der Folien.

---

## Steuerung

`→ ↓ Leertaste Bild-ab` weiter · `← ↑ Bild-auf` zurück · `1…9` Folie · `Pos1/Ende`
· `0`/`O` Übersicht (`Esc` schließt) · `F`/`F5` Vollbild · `P` Vortragendenansicht · `B`/`.`
Schwarzbild · `K` Tastenanzeige. Bild-ab und Bild-auf sind absichtlich belegt: USB-
Presenter senden genau die.

**Die Tastenbelegung steht an zwei Stellen:** im `switch` des Skripts und in der Tabelle
der `README.md`. Wird eine Taste ergänzt, müssen beide nachgezogen werden — sonst
dokumentiert der Foliensatz etwas anderes, als er tut. Eine dritte Stelle gab es bis zum
11.09. auf der Folie „Steuerung" der Anleitung; genau dort war sie einmal veraltet.

---

## Fallen — schon einmal zugeschnappt

- **Spezifität im SVG.** `.slide svg [data-step] { transform:none }` enthält einen
  Elementselektor und schlägt jede Regel aus zwei Klassen. Eigene Bewegungen brauchen
  drei, etwa `.slide svg .kiste-lid.shown`.
- **Animation gegen Präsentationsattribut.** Nie beides auf dieselbe Eigenschaft
  desselben SVG-Elements. Keyframes mit `transform: scale()` löschen ein
  `transform="rotate()"`. Drehung an die Form, Skalierung an eine `<g>`-Hülle.
- **Kartenpolsterung.** Die Kartenregel heißt `.slide .cols > *`, nicht `.cols > *` —
  `ul.points { padding:0 }` ist sonst spezifischer und hebelt sie aus.
- **`width:100%` schlägt `max-height`.** Ein Kasten mit fester Breite wird
  beschnitten, nicht verkleinert. Zum Einpassen: absolut, `inset:0`, `margin:auto`,
  `max-width`/`max-height`.
- **`margin-top:auto` in Flex.** Setzt die Unterkante unabhängig von Rändern und war
  auf der Titelfolie 18 px zu tief. Für feste Ecken absolut positionieren.
- **`position` prüfen, nicht raten.** `.slide > *` trägt `position:relative` aus der
  Formen-Ebene. Ein Filter auf `static` schließt deshalb alles aus.
- **Geklonte Folien erben.** Farbe und Schriftgrad kommen vom neuen Elternteil —
  in der dunklen Vortragendenansicht wurde die Folie deshalb grau.
- **Suchmuster.** Die Zeichenkette `<script>` steht auch im Kopfkommentar des
  Stylesheets. Muster präzise fassen, sonst erfasst eine Ersetzung den halben Rest.
- **`<em>` ist belegt.** In `ul.points li` setzt `em` auf Ziffernschrift in Blau — das
  ist die alte Kurzform für Formelzeichen. Für Betonung `<b>` nehmen, sonst steht
  mitten im Satz plötzlich Code.
- **Bruch und Grundlinie.** Ein `inline-grid` gibt die Grundlinie seiner *ersten* Zeile
  ab. Ein Bruch hängt damit unter der Zeile. `vertical-align: middle` setzt seine Mitte
  auf die Mittelachse — dort gehört der Bruchstrich hin.
- **Hervorhebung um einen Bruch.** `.hl` muss `inline-block` sein. Als reines Inline-
  Element umfasst der Grund nur die Zeilenhöhe, der Nenner steht draußen.
- **Elementnamen in Kommentaren.** Zweimal zugeschnappt: erst stand `<script>` im
  Kopfkommentar des Stylesheets, dann `<style>` in einem Kommentar des Formelblocks.
  Beide Male hat eine Suche nach dem Element den Kommentar erwischt und den halben Rest
  mitgenommen. **In Kommentaren keine Elementnamen in spitzen Klammern.**
- **Messwerte der Titelfolie schwanken — aufgeklärt am 15.09.** Unter
  `--virtual-time-budget` laufen CSS-Animationen nicht mit: Die Sonde fand alle Animationen
  der aktiven Folie bei `running@0`, und jedes `data-anim`-Element saß auf der Startlage des
  Auftritts (`rise`, `translateY(18px)`) — das waren die „18 px höher". Ob es zuschlägt, hängt
  vom Zeitverhalten ab (im 0,6-MB-Vortrag ja, in der 0,85-MB-Vorlage nicht). Seit dem 15.09.
  bringt die Sonde vor dem Messen alle Animationen mit `finish()` in die Endlage; die
  Messung ist damit deterministisch. Wer in `pruefen.py` etwas Neues misst: **nach** dieser Zeile.
- **Weiße Schrift außerhalb der Karte ist kein Überlauf.** Die Hero-Karte stand bis zum
  15.09. fest bei 48–478 px (`bottom:242px`), gebaut für „Registerdeck" in einer Zeile. Ein
  dreizeiliger Titel schob Untertitel und Byline aus der Karte — weiß auf hellem Grund, unlesbar —
  und `pruefen.py` meldete nichts, weil nichts unter die Grenze rutschte. Seither wächst die
  Karte mit (Raster, siehe Bausteine). Lehre: **Blaue Karten mit festem Maß gibt es nicht mehr;
  bei Titel- und Dankfolie das Bild ansehen,** die Messung sieht nur Text.
- **Ein Button erbt die Schrift nicht.** Register (`.rail-item`) und Übersicht (`.ov-item`) sind
  Buttons; das Register hatte `font:inherit`, die Übersicht nicht — ihre Miniaturen und
  Beschriftungen standen seit je in der Systemschrift (kopflos: Arial), am Bildschirm kaum zu
  sehen, in der Messung eindeutig (`getComputedStyle(klon).fontFamily`). Seit dem 15.09. abends
  `font:inherit` auch dort. **Wer einen Button anlegt, gibt ihm `font:inherit`.**
- **Leere Gruppe mit `data-step` = Schritt ins Leere.** `stepsOf` zählt jedes `data-step`,
  auch an einem `<g>` ohne Inhalt. `buildFluss` legte je Spalte eine Gruppe für die abgehenden
  Bänder an — aus der letzten Spalte geht keins ab, die Gruppe war leer, und der Pfeil musste
  am Ende zweimal gedrückt werden. Bauer, die Gruppen aus Listen erzeugen: **ohne Inhalt keine
  Gruppe.** `pruefen.py` sieht das nicht (es zählt nur); die Sonde `leere_schritte.py` aus dem
  Protokoll vom 15.09. findet es.
- **Skript ohne sein Element.** Das Skript greift beim ersten Tastendruck auf
  `#schwarz` zu. In der früheren Anleitung fehlte das Element, die Ausnahme flog vor
  allem anderen — die Tastatur war dort tot, monatelang, ohne dass es auffiel.
  `pruefen.py` misst Geometrie, nicht Funktion. **Zum Abschluss den Foliensatz einmal
  durchblättern und auf JavaScript-Fehler horchen.**
- **Klassenpräfixe im SVG.** `.sk-*` war schon vergeben (Skizzen der Kacheln: `.sk`,
  `.sk-f`, `.sk-t` gestrichelt) — ein neues `.sk-t` für Sankey-Beschriftungen hat die
  Skizzenregel überschrieben, und die Beschriftung stand plötzlich gestrichelt da. Vor
  einem neuen Präfix `grep "^\.xx-"` — und beim Umbenennen nur die eigenen Vorkommen
  anfassen, nicht per Muster über die ganze Datei.
- **Kopflose Schnappschüsse bei Maßstab ≠ 1.** Chrome headless zieht bei
  `--window-size=1280,720` 87 px ab (innerHeight 633), die Bühne läuft auf 0,88 — und
  SVG-Texte werden mit dem alten Maßstab gerastert: Beschriftungen verschoben, gekappt,
  „8" statt „0,8". Das DOM ist dabei richtig, im echten Browser passiert es nicht. **Für
  Bilder `--window-size=1280,807` nehmen** (Maßstab 1, unten 43 px abschneiden), dann
  sind vier von vier Läufen byteweise gleich. Das erklärt rückwirkend die „Zeitartefakte"
  des Fortschrittsbalkens im Protokoll — die der Titelfolie nicht, die hatten den Auftritt
  als Ursache (siehe „Messwerte der Titelfolie schwanken").
- **Grid-Zeile voll, Zellen ohne Spalte.** Ein Element mit `grid-column:1/-1` in einer
  Zeile lässt der automatischen Platzierung dort keinen Platz — weitere Zellen derselben
  Zeile wandern in unsichtbare Zusatzspalten rechts hinaus. Entweder jede Zelle mit
  Koordinate, oder (so die Schwimmbahnen) je Zeile ein eigenes Raster.
- **Tabellenpolsterung und `border-collapse`.** Im Collapse-Modus ignoriert der
  Browser `padding` am Tabellenelement — die Kartenregel griff nicht, der Text klebte
  an der abgerundeten Kante. `table.vgl` steht deshalb auf `separate` mit
  `border-spacing:0`; die Linien kommen ohnehin von den Zellen.
- **Register, Übersicht und Fensterhöhe.** Beide hängen am Fenster, nicht an der
  skalierten Bühne, und beide rechnen ihre Größe aus Fensterhöhe und Folienzahl:
  `passeRegister()` und `passeUebersicht()`, bei jeder Größenänderung neu. Feste Werte
  reichten ab etwa 15 Folien nicht mehr — das Register lief unten aus dem Bild, die
  Übersicht oben und unten. **Die Übersicht wird nie scrollbar; sie zeigt alle Folien
  auf einen Blick und macht die Kacheln dafür kleiner.**
- **Chrome malt am Bühnenrand eine Spalte in Kartenfarbe.** Bei manchen Maßstäben (1,25 ·
  1,37 · 1,49 nachgestellt, nicht bei 1,11 und 1,31) steht am rechten Bühnenrand eine halb
  gedeckte Linie in `--blau`, von oben bis unter die große Karte — auf Titel-, Dank- und
  Trennerfolie, obwohl die Karte 56 px vorher endet. Radius, `overflow`, `clip-path`,
  `z-index` und Lage ändern nichts; `transform: translateZ(0)` an `::before` (eigene
  Kompositionsebene) schon. Nachweis: Karte rot gefärbt, Linie rosa. Regel in Abschnitt 7.
- **Der Zeilenkasten setzt der Karte den Boden.** `passeRegister()` schrumpfte nur die
  Miniatur; die Beschriftung daneben (13,5 px mit Durchschuss = 17 px) hielt jede Karte
  auf 27 px. Bei 34 Folien war der Stapel 1017 px hoch und ragte auf jedem Bildschirm
  oben und unten hinaus, ohne dass es auffiel. Seit dem 14.09.: `line-height:1` an der
  Beschriftung, der Stapel bekommt höchstens 95 % der Fensterhöhe (Max' Wunsch: nur oben
  und unten ein Rand), und in vier Stufen weichen Polsterung, Abstand, Miniatur und zuletzt
  der Grad (`--rail-font`, 13,5 → 9 px). 42 Karten passen so noch in 600 px — **54 nicht mehr:**
  bei 813 px Fensterhöhe 97 %, bei 720 px 105 %. Der Musterbogen ist damit an der Grenze eines
  einspaltigen Registers. **Entschieden am 15.09.: so lassen** — die Vorlage zeigt Möglichkeiten,
  echte Vorträge haben 15–25 Folien. Kein zweispaltiges Register, keine Obergrenze.
  **Seit dem 15.09. abends (Max: „sieht aus wie ein Zaun"):** Radius der Karten 4 px statt 14
  (bei 14 px Kartenhöhe waren es Pillen), Streifen `--stripe` 8 px statt 14, in Ruhe `--peek`
  12 px statt 21 sichtbar, der Block in Ruhe auf 70 % gedeckt (`.rail{opacity:.7}`), unter
  Maus oder Fokus voll. Beschlossene Formensprache — nicht zurückdrehen.
- **Flex zerreißt den Satz um eine Formel.** `display:flex` auf einem Absatz macht jedes
  Kind zum eigenen Flex-Element — ein `.tex`-Span mitten im Satz stand plötzlich als dritte
  Spalte zwischen zwei Textstücken (Konvergenz, erster Wurf). Zum senkrechten Zentrieren von
  Fließtext `align-content:center` am Block nehmen (Chrome ab 123, Safari ab 17.4; fällt sonst
  auf „oben“ zurück), nicht Flex oder Grid.
- **`align-items:center` im Raster verschiebt die Zeilenlinien.** Die Gegenüberstellung
  zentrierte ihre Zellen in der Zeile; eine einzeilige Zelle neben einer zweizeiligen wurde
  dadurch kürzer und ihre `border-top` rutschte unter die des Nachbarn — die Linien standen
  auf drei Höhen. Zellen mit Linien müssen die Zeile füllen (`stretch`), der Text darin
  wird mit `align-content:center` mittig gesetzt.
- **Flex-Spalte dehnt das Bild, `max-height` staucht es.** Ein `img` in `figure`
  (`display:flex; flex-direction:column`) wird auf Kartenbreite gestreckt; greift dann
  `max-height`, bleibt die Breite stehen — verzerrt, ohne Fehlermeldung. Nachgemessen
  503 × 360 statt 437 × 360. `object-fit: contain` hält das Bild im Kasten unverzerrt.

---

## Vor dem Abschluss

```bash
python3 werkzeuge/pruefen.py            # muss 0 zurückgeben
python3 werkzeuge/formeln.py            # wenn eine Formel geändert wurde
python3 werkzeuge/schriften.py --pruefen  # kein Zeichen außerhalb der Schrift
```

Dazu einmal durchblättern und auf JavaScript-Fehler horchen — `pruefen.py` misst
Geometrie, nicht Funktion.

Änderungen an Text oder Inhalt ohne Rückfrage. Änderungen an Farben, Schriftgraden,
Geometrie oder Formensprache **nur auf ausdrückliche Bitte** — diese Entscheidungen
sind gefallen und stehen begründet im Protokoll.

Die Vorlage enthält Platzhalter (Autor:innen, Zahlen, Quellen), auf den Folien als
solche gekennzeichnet. Das Logo ist seit dem 14.09. echt (RWTH, als Symbol eingebettet), das Bild der Klimabox ebenso. Einzige echte Angabe: Hestenes, Wells & Swackhamer (1992).
Beim Befüllen mit echtem Inhalt keine Quellen erfinden.
