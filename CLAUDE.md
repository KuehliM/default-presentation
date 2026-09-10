# Arbeitsanweisung für dieses Repository

Foliensatz als einzelne HTML-Datei. Diese Datei beschreibt die Regeln so, dass
sie ohne Rückfrage befolgt werden können. **Zuerst lesen, dann anfassen.**

## Reihenfolge zu Sitzungsbeginn

1. Diese Datei.
2. Das neueste Protokoll in `Sessions/` — dort stehen Begründungen und bereits
   zugeschnappte Fallen.
3. Bei Layoutfragen **nicht schätzen, sondern messen:** `python3 pruefen.py`.

## Was wo liegt

| Datei | Rolle |
|---|---|
| `vorlage.html` | **Der Foliensatz.** 22 Folien Vortrag, 3 Anhang; jede Darstellungsform genau einmal. Steht allein: der Kopfkommentar erklärt Aufbau, Bedienung und Grenzen. |
| `formeln.py` | Setzt alle Formeln: liest LaTeX aus `data-tex`, schreibt MathML hinein, bettet Fira Math ein. Nach jeder Formeländerung laufen lassen. |
| `pruefen.py` | Misst jede Folie im Browser: Überlauf, Füllstand, kleinste Schrift. |
| `README.md` | Die Dokumentation für Menschen: Bedienung, Bausteine, Formeln. **Einzige Stelle neben dem Skript, an der die Tastenbelegung steht.** |
| `Darstellungsformen.md` | Vorrat: was gebaut ist und was noch kommen könnte. Vor neuen Formen dort nachsehen. |
| `Sessions/<datum>.md` | Protokolle. Bei nennenswerten Änderungen ein neues anlegen. |

**Regel:** Es gibt nur noch **einen** Foliensatz. Die frühere `anleitung.html` war eine
zweite Datei mit demselben Unterbau und einem eigenen Übertragungsskript; beides ist am
11.09. entfallen — der Aufwand stand in keinem Verhältnis, und die Anleitung war
monatelang unbemerkt kaputt. Was sie erklärte, steht in der `README.md`; was sie vorführte,
führt die Vorlage auf ihren eigenen Folien vor.

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
   640  │  └───────────────────────────────────────────────────┘  │  ← Inhalt endet
        │      Fußzeile: Logo · Name · Nummer                     │
   720  └─────────────────────────────────────────────────────────┘
          68                                                  1212
```

| Größe | Wert | Token |
|---|---|---|
| Satzspiegel links/rechts | 68 px | `--pad-x` |
| Inhalt beginnt bei | 40 px | `.slide` padding-top |
| **Inhalt endet spätestens bei** | **640 px** | `720 − --pad-b (80)` |
| Nutzbare Höhe | **600 px** | |
| Nutzbare Breite | **1144 px** | |
| Abbildungen höchstens | 400 px hoch | `.slide figure svg` |

**Unverhandelbar:** Text und Karten dürfen nie unter 640 px reichen. Der Streifen
darunter gehört der Fußzeile. Für `.slide.hero` (Titel- und Dankfolie) gilt 664 px,
weil dort die Fußzeile ausgeblendet ist.

### Wie viel passt hinein

Erfahrungswerte aus dem gemessenen Bestand (`python3 pruefen.py`):

| Aufbau | belegte Höhe | Füllstand |
|---|---|---|
| Kopf allein (Abschnitt + Titel einzeilig) | ~110 px | — |
| Kopf + Karte mit 4 langen Stichpunkten (je 2 Zeilen) | 496 px | 76 % |
| Kopf + Kennzahlenreihe + 2 Stichpunkte | 458 px | 70 % |
| Kopf + zwei Spalten mit Diagramm und Text | 583 px | 91 % |
| Kopf + Quellenverzeichnis, 5 Einträge | 423 px | 64 % |
| Kopf + Herleitung, 6 Zeilen mit Brüchen und Wurzeln | 577 px | 90 % |
| Kopf + Vergleichstabelle, 4 Spalten × 5 Zeilen | 477 px | 73 % |
| Kopf + Zeitleiste + 2 Stichpunkte | 493 px | 76 % |
| Kopf + Transkript, 6 Zeilen | 442 px | 67 % |

Ab **92 % Füllstand** meldet `pruefen.py` „eng". Darüber wird es auf einem Beamer
gedrängt — dann Inhalt kürzen, nicht die Schrift verkleinern.

---

## Schriftgrade

Nicht unterschreiten: **15 px** für alles, was gelesen werden soll. Auszeichnungen
dürfen kleiner sein.

| Rolle | Klasse | Grad |
|---|---|---|
| Titelfolie | `h1` | 84 px |
| Folientitel | `h2` | 46 px |
| Untertitel, Vorspann | `.lead` | 26 px |
| Aufzählung Ebene 1 | `ul.points li` | 19 px |
| Aufzählung Ebene 2 | verschachteltes `ul` | 17 px |
| Aufzählung Ebene 3 | doppelt verschachtelt | 15,5 px |
| Fließtext | `.body` | 19 px |
| Quellen | `ul.refs li` | 16 px |
| Code | `pre` | 14,5 px |
| Zitatfolie | `.zitat` | 33 px |
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
| `.slide.hero` | Titel-/Abschlussfolie: blaue Karte, weiße Schrift, ohne Fußzeile |
| `.cols` | zwei gleich breite Spalten, je eine Karte |
| `.cols.wide-left` | Verhältnis 1,15 : 0,85 |
| `ul.points` | drei Ebenen: Punkt, Strich, Viereck — `<ul>` einfach verschachteln |
| `ul.points.long` | kleinerer Grad für textreiche Folien |
| `ul.refs` | Quellen mit hängendem Einzug |
| `.stats` / `.stat` | Kennzahlenkacheln |
| `.keys` | zweispaltige Definitionsliste |
| `.tiles` / `.tile` | Kachelreihe für Bilder oder Skizzen |
| `.chip` | Pille für Schlagworte — vorhanden, derzeit ungenutzt |
| `.cite` / `.source-note` | Beleg im Fließtext, Fußnote |
| `.pops` | ploppt beim Erscheinen auf statt einzublenden |
| `data-anim` | tritt beim Folienwechsel gestaffelt auf |
| `data-step="n"` | erscheint beim n-ten Pfeildruck |
| `data-step-until="n"` | verschwindet beim n-ten wieder |
| `data-keep` | bleibt sichtbar, `data-step` löst nur die eigene Bewegung aus |
| `<aside class="notes">` | Sprechnotizen, nur in der Vortragendenansicht |
| `.slide.anhang` | Folie für die Fragerunde — eigener Abschnitt unten |

### Anhangsfolien

`<section class="slide anhang">`. Eine Klasse trägt alles Weitere:

* **Fortschrittsbalken** zählt sie nicht (`total` lässt sie aus, `scaleX` ist auf 1 begrenzt).
* **Register** zeigt sie nicht — es bliebe sonst für den Vortrag weniger Platz.
* **Übersicht** zeigt sie unter einer Trennzeile. Der einzige Weg hinein.
* **Fußzeile** zeigt `A1`, `A2`, … über `nummer(i)`.
* **`→`** baut Einblendungen auf, verlässt die Folie aber nie. Am Ende des Vortrags
  bleibt `→` ebenfalls stehen — ein Druck zu viel darf den Anhang nicht an die Wand werfen.
* **`←`** führt aus dem Anhang zurück auf `vortragEnde`, fertig aufgebaut.
* **`Ende`** springt auf `vortragEnde`, nicht auf die letzte Folie der Datei.

Weil Register und Übersicht ihre Karten nicht mehr über die Position zuordnen können,
trägt jede Karte ihre Folienzahl in `dataset.nr`; `paint()` vergleicht damit. Wer am
Aufbau beider Leisten etwas ändert, muss das mitnehmen.

Titel nach der **Frage** benennen, nicht nach dem Inhalt.

### Zahlen, Formeln, Belege

| Klasse | Wirkung |
|---|---|
| `.zeit` | Zeitleiste. Raster mit `--spalten`; `.zeit-phase` trägt `--von` und `--dauer`, `.zeit-marke` trägt `--bei` |
| `table.vgl` | Vergleichstabelle; `.mk.ja` / `.mk.halb` / `.mk.nein` als Ausfüllgrad, `.num` für Ziffernschrift |
| `.zitat` | eine Äußerung, groß gesetzt; `.zitat-quelle` als Beleg darin |
| `.trans` | Transkript: `.nr`, `.wer`, `.txt`, `.kode`; `<mark>` hebt Stellen hervor |
| `.herleit` | Herleitung; jede Zeile `.lhs` · `.rel` · Formel · `.grund`, alle am Relationszeichen bündig |
| `.tex` + `data-tex` | Formel: LaTeX im Attribut, MathML darin — von `formeln.py` gesetzt |
| `.gr` | einzelne griechische und mathematische Zeichen **außerhalb** einer Formel |
| `#kiSvg` | Balken mit 95-%-Konfidenzintervall — Werte im Skript, `buildKI` |
| `#hakeSvg` | Zugewinn: Nachtest gegen Vortest mit Linien gleichen *g* — `buildHake` |

### Formelsatz

Entschieden am 11.09.: **MathML mit eingebetteter Fira Math.** Kein JavaScript, keine
Fremdbibliothek — den Satz erledigt der Browser anhand der MATH-Tabelle der Schrift.

Im Quelltext steht LaTeX, das Erzeugnis daneben:

```html
<span class="tex" data-tex="T = 2\pi\sqrt{\dfrac{l}{g}}"><math>…</math></span>
```

Das Attribut ist die Quelle, das MathML das Erzeugnis. **Formel ändern heißt: Attribut
ändern, dann `python3 formeln.py`.** Das Skript geht über `vorlage.html`,
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
  **entfernt**. Geblieben ist `.gr` für einzelne Zeichen außerhalb einer Formel.

**Bedingung, die über allem steht:** Die fertige Datei stellt **keine** Anfrage nach
außen. Auf Tagungen steht selten der eigene Rechner auf dem Pult. `formeln.py` prüft
das nach jedem Lauf und bricht ab, wenn auch nur ein `url(http…)` übrig bleibt.

**Zeichenvorrat.** Eingebettet ist nur Latein. Vorhanden: `· × − ½ ¼ ¾ ² ³ ° ± µ`.
**Fehlt:** `Δ π σ α β θ ω √ ≈ ≤ ≥ ≠ → ←`. Die Wurzel ist deshalb gezeichnet, alles
Übrige holt `.gr` aus der Systemschrift. Erweitern ginge nur mit der vollständigen
Fira Sans und `brotli` — beides lag hier nicht vor. Keine fehlenden Zeichen direkt
in den Text setzen, immer `.gr` verwenden.

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

`→ ↓ Leertaste Bild-ab` weiter · `← ↑ Bild-auf` zurück · `1…9` Folie · `Pos1/Ende` (Ende = letzte Folie des **Vortrags**)
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
- **Messwerte der Titelfolie schwanken.** Mit eingebautem KaTeX meldet `pruefen.py`
  für Folie 1 einen um 18 px höheren Inhalt und 3 % kleinere Grade. Nachgeprüft: die
  gerenderten Bilder sind **byteweise identisch**. Es ist ein Zeitartefakt der
  kopflosen Messung, kein Unterschied im Bild — nicht daran herumbessern.
- **Skript ohne sein Element.** Das Skript greift beim ersten Tastendruck auf
  `#schwarz` zu. In der früheren Anleitung fehlte das Element, die Ausnahme flog vor
  allem anderen — die Tastatur war dort tot, monatelang, ohne dass es auffiel.
  `pruefen.py` misst Geometrie, nicht Funktion. **Zum Abschluss den Foliensatz einmal
  durchblättern und auf JavaScript-Fehler horchen.**
- **Register, Übersicht und Fensterhöhe.** Beide hängen am Fenster, nicht an der
  skalierten Bühne, und beide rechnen ihre Größe aus Fensterhöhe und Folienzahl:
  `passeRegister()` und `passeUebersicht()`, bei jeder Größenänderung neu. Feste Werte
  reichten ab etwa 15 Folien nicht mehr — das Register lief unten aus dem Bild, die
  Übersicht oben und unten. **Die Übersicht wird nie scrollbar; sie zeigt alle Folien
  auf einen Blick und macht die Kacheln dafür kleiner.**

---

## Vor dem Abschluss

```bash
python3 pruefen.py            # muss 0 zurückgeben
python3 formeln.py            # wenn eine Formel geändert wurde
```

Dazu einmal durchblättern und auf JavaScript-Fehler horchen — `pruefen.py` misst
Geometrie, nicht Funktion.

Änderungen an Text oder Inhalt ohne Rückfrage. Änderungen an Farben, Schriftgraden,
Geometrie oder Formensprache **nur auf ausdrückliche Bitte** — diese Entscheidungen
sind gefallen und stehen begründet im Protokoll.

Die Vorlage enthält Platzhalter (Autor:innen, Zahlen, Quellen), auf den Folien als
solche gekennzeichnet. Einzige echte Angabe: Hestenes, Wells & Swackhamer (1992).
Beim Befüllen mit echtem Inhalt keine Quellen erfinden.
