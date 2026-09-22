# Registerdeck

Eine Präsentationsvorlage als **eine einzige HTML-Datei**: dünner Fortschrittsbalken
oben, Registerkarten am rechten Rand, die beim Überfahren mit dem Folientitel
herausfahren. Keine externen Anfragen, keine Abhängigkeiten, Schriften eingebettet.

**Warum eine Datei:** Auf einer Tagung steht selten der eigene Rechner auf dem Pult.
`vorlage.html` läuft überall per Doppelklick — offline, ohne Installation, ohne Konto.

Ein neuer Vortrag ist ein eigener Ordner, den `werkzeuge/neu.py` anlegt — mit demselben
Unterbau, dem Musterbogen zum Kopieren und den Werkzeugen. Der Ablauf steht gleich unten,
auch als Rezept für Claude in einem frischen Ordner. Der Kopfkommentar der Datei sagt, wo
was steht; dieses Dokument geht ins Einzelne.


## Dateien

```
default-presentation/
├── README.md               dieses Dokument
├── CLAUDE.md               Arbeitsanweisung für KI-Sitzungen an der Vorlage
├── vorlage.html            die Vorlage, zugleich Musterbogen — 67 + 3 Folien, jede Form einmal
├── Darstellungsformen.md   Katalog: was gebaut ist (mit Foliennummern), was noch kommen könnte
├── Sessions/               datierte Protokolle mit Entscheidungen und Begründungen
├── werkzeuge/
│   ├── neu.py              legt einen Vortragsordner an
│   ├── pruefen.py          misst jede Folie im Browser: Überlauf, Füllstand, kleinste Schrift
│   ├── formeln.py          setzt Formeln: LaTeX aus data-tex wird MathML, Fira Math eingebettet
│   ├── pdf.py              schreibt das PDF, eine Seite je Folie, alles aufgebaut
│   ├── schriften.py        bettet Fira Sans/Mono als Teilsatz ein; --pruefen meldet fremde Zeichen
│   ├── vortrag-CLAUDE.md   Vorlage der Arbeitsanweisung, die jeder Vortragsordner bekommt
│   └── geholt/             (nicht im Repo) Temml und Schriften, bei Bedarf geholt
└── quellen/                Klimabox.png, RWTH_Logo_3.svg — Quellen der eingebetteten Bilder
```

Alle Werkzeuge nehmen einen Dateipfad, relativ zum Arbeitsverzeichnis oder zum Ordner über
`werkzeuge/`; ohne Angabe die Vorlage: `python3 werkzeuge/pruefen.py`, `… formeln.py`,
`… pdf.py [datei.html] [ziel.pdf]`, `… schriften.py [datei.html] --pruefen`. Sie brauchen
Python 3 und Google Chrome; `formeln.py` und `schriften.py` einmalig Netz und `npm`.

---

## Einen neuen Vortrag anlegen

Die Vorlage ist der Musterbogen: jede Darstellungsform genau einmal, mit Platzhaltern.
Ein Vortrag beginnt **leer**, in einem eigenen Ordner, und holt sich aus dem Musterbogen,
was er braucht. Der Ordner ist danach unabhängig vom Repo.

### Für Claude: in einem neuen Ordner

Im Vortragsordner genügt der Satz *„Erstelle mir eine Blanko-Präsentation aus
github.com/KuehliM/default-presentation."* Das Rezept dahinter:

```bash
git clone --depth 1 https://github.com/KuehliM/default-presentation.git /tmp/registerdeck
python3 /tmp/registerdeck/werkzeuge/neu.py . "Titel des Vortrags"
```

Danach `CLAUDE.md` im Ordner lesen — sie ist die Arbeitsanweisung für genau diesen Vortrag.
Das Repo in `/tmp` wird nicht mehr gebraucht.

### Was `neu.py` anlegt

```
<ordner>/
├── <name>.html            der Vortrag — Titel, erste Folie, Dank, alles Platzhalter;
│                          mit dem kompletten Unterbau der Vorlage (0,6 MB)
├── vorlage.html           der Musterbogen zum Nachschlagen und Kopieren — nicht vortragen
├── Darstellungsformen.md  Katalog der Formen mit ihren Foliennummern
├── CLAUDE.md              Arbeitsanweisung für diesen Vortrag
├── werkzeuge/             pruefen.py, formeln.py, pdf.py, schriften.py
├── bilder/                für Bildquellen
└── .gitignore             PDFs, geholte Werkzeuge
```

Der Dateiname kommt aus dem Ordnernamen (`DPG Frühjahr 2027` → `dpg-fruehjahr-2027.html`),
`--datei name.html` setzt ihn ausdrücklich. Vorhandene Dateien werden nicht überschrieben.

### Von Hand, Schritt für Schritt

**1. Anlegen** — aus dem Repo heraus, Zielordner beliebig:

```bash
python3 werkzeuge/neu.py ~/Vortraege/dpg-2027 "Wie Lernende Wärme verstehen"
cd ~/Vortraege/dpg-2027
```

**2. Kopf ausfüllen** — alles ist als Platzhalter beschriftet:

| Was | Wo |
|---|---|
| Tagung, Titel, Untertitel, Autor:innen, Einrichtung | Titelfolie: `.eyebrow`, `h1`, `.lead`, `.byline` |
| Kontakt | Dankfolie, `.affil` |
| Name und Tagung in der Fußzeile | `<p class="foot-meta">` unter den Folien |
| Fenstertitel | `<title>` im Kopf |
| Logo | Symbol `logo-rwth` am Anfang des Rumpfs: Pfade und `viewBox` ersetzen, sonst nichts |

**3. Folien anlegen** — zwei Wege, beliebig gemischt:

* **Leer:** den Block „Erste Folie" kopieren (`eyebrow`, `h2`, `ul.points`, `notes`).
  `data-title` beschriftet die Registerkarte, `data-step` staffelt Punkte.
* **Aus der Vorlage:** die Form in `Darstellungsformen.md` (Tabelle mit Foliennummern)
  oder in `vorlage.html` mit Taste `0` suchen, die ganze `<section … </section>` samt
  Kommentar davor kopieren, zwischen die eigenen Folien setzen, Text ersetzen. Sie
  funktioniert sofort — der Unterbau ist derselbe.
* **Diagramme:** Die Zahlen stehen nicht in der Folie, sondern im Skript des Vortrags,
  im Block `buildXyz` — die Folie trägt `id="xyzSvg"`, der Block liest genau diese id.
  Dort die Arrays ändern; Achsen, Skalen und Beschriftungen entstehen daraus. **Jede
  Form einmal je Datei**, weil die id eindeutig sein muss. Dieselbe Form zweimal: Block im
  Skript kopieren, id in Folie und Block umbenennen (`slopeSvg2`).
* **Bilder:** Quelle nach `bilder/`, in die Folie als Daten-URI (Muster: Klimabox, Bildpaar,
  Zeiger). Vorher beschneiden, auf etwa 1200 px Breite bringen, bei Zeichnungen die Farbzahl
  reduzieren — steht in `Darstellungsformen.md`.
* **Gliederung:** `.slide.trenner` als Abschnittstrenner gruppiert Register und Übersicht
  von selbst; `.slide.anhang` für die Fragerunde ans Ende (Muster in der Vorlage unten).

**4. Formeln setzen** — LaTeX in `data-tex`, dann:

```bash
python3 werkzeuge/formeln.py dpg-2027.html
```

**5. Messen** — Überlauf ist der Fehler, „Luft" ein Hinweis:

```bash
python3 werkzeuge/pruefen.py   dpg-2027.html
python3 werkzeuge/schriften.py dpg-2027.html --pruefen
```

**6. PDF** — landet als `dpg-2027.pdf` daneben:

```bash
python3 werkzeuge/pdf.py dpg-2027.html
```

**7. Vortragen:** Datei doppelklicken, `F` für Vollbild, `P` für die Vortragendenansicht
im zweiten Fenster. Die ganze Steuerung steht im nächsten Abschnitt.

**Was der Vortrag nicht mitbekommt:** spätere Änderungen an der Vorlage. Er ist ein
Schnappschuss des Unterbaus vom Tag seiner Erzeugung. Wer eine Verbesserung nachziehen
will, kopiert den betroffenen Block (Stilabschnitt, Skriptblock) von Hand hinüber — oder
legt den Vortrag neu an und setzt die Folien wieder ein.

---

## Steuerung

| Taste | Wirkung |
|---|---|
| `→` `↓` `Leertaste` `Bild ab` | erst nächster Einblendschritt, dann nächste Folie |
| `←` `↑` `Bild auf` | zurück — die Folie bleibt dabei fertig aufgebaut |
| `1` … `9` | direkt zur Folie |
| `0` oder `O` | Übersicht aller Folien, gruppiert nach Abschnittstrennern und Anhang — `Esc` schließt sie wieder |
| `Pos1` / `Ende` | erste / letzte Folie |
| `F` oder `F5` | Vollbild |
| `P` | Vortragendenansicht im zweiten Fenster |
| `B` oder `.` | Schwarzbild — jede Taste holt zurück |
| `K` | zeigt an, welche Taste ankommt |

### Presenter am USB-Anschluss

Ein Presenter meldet sich beim Rechner als **Tastatur**. Die üblichen Belegungen sind
abgedeckt:

| Knopf | sendet meist | hier |
|---|---|---|
| vor | `Bild ab`, manchmal `→` | weiter |
| zurück | `Bild auf`, manchmal `←` | zurück |
| Mitte | `B` oder `.` (Schwarzbild), `F5` (Vortrag starten) | Schwarzbild bzw. Vollbild |

Die Modelle unterscheiden sich. Welche Taste dein Gerät wirklich schickt, zeigt **`K`**:
Danach erscheint bei jedem Tastendruck unten der Name der Taste. Nochmal `K` beendet es.
Schickt der mittlere Knopf etwas anderes, lässt es sich in einer Zeile ergänzen.

Auf dem Tablet wischen. Die Foliennummer steht in der Adresszeile: `datei.html#3`
springt direkt auf Folie 3.

Am rechten Rand liegt der **Karteikasten**: in Ruhe sieht man nur die farbige Kante
jeder Folie — kräftiges Blau für die offene, helles Blau für die übrigen. Nähert sich
die Maus, treten die Miniaturen hervor; auf einer Karte fährt sie ganz heraus und zeigt
Vorschau, Foliennummer und Titel. Ein Klick springt dorthin.

---

## Präsentationsmodus

`P` öffnet dieselbe Datei ein zweites Mal — diesmal als **Vortragendenansicht**:
aktuelle Folie, nächste Folie, Sprechnotizen und eine Uhr mit Start und Rücksetzen.

Der Ablauf beim Vortrag:

1. Beide Bildschirme anschließen und den Foliensatz öffnen.
2. `P` drücken — das zweite Fenster erscheint.
3. Das zweite Fenster auf den Laptopbildschirm ziehen.
4. Im ersten Fenster `F` für Vollbild auf dem Beamer drücken.

Geblättert werden kann in beiden Fenstern; der Zustand bleibt gekoppelt, auch die
Einblendschritte. Die Vorschau der aktuellen Folie zeigt den echten Aufbaustand,
die Vorschau der nächsten Folie zeigt sie fertig aufgebaut.

Aufteilung: links die aktuelle Folie, darunter die nächste, rechts über die volle
Höhe die Notizen. Notizen sind meist stichpunktartig und brauchen eine hohe, schmale
Spalte statt einer breiten.

### Aufteilung anpassen

Zwischen den Bereichen liegen zwei Griffe — ein senkrechter zwischen Folien und
Notizen, ein waagerechter zwischen aktueller und nächster Folie. Ziehen verschiebt die
Aufteilung, je nachdem ob du im konkreten Vortrag mehr von der Folie oder mehr von
den Notizen brauchst.

| Bedienung | Wirkung |
|---|---|
| Ziehen | Bereich vergrößern oder verkleinern (24 – 80 %) |
| Doppelklick | zurück auf die Voreinstellung |
| Tab, dann Pfeiltasten | in Schritten von 2 % verschieben |

Die Notizen sind der Teil, den du im abgedunkelten Saal wirklich lesen musst. In der
Kopfzeile stellen **A−** und **A+** ihren Schriftgrad zwischen 14 und 34 px; `+` und
`−` auf der Tastatur tun dasselbe. Auch diese Wahl merkt sich der Browser.

Die Einstellung merkt sich der Browser und stellt sie beim nächsten Öffnen wieder her.

Die beiden Fenster verständigen sich über `postMessage`. Das ist bewusst so gewählt:
gemeinsamer Speicher und `BroadcastChannel` scheitern bei `file://` an der
undurchsichtigen Herkunft, `postMessage` funktioniert auch dort.

### Sprechnotizen

Notizen stehen als `<aside class="notes">` in der Folie. Im Foliensatz sind sie
unsichtbar, im zweiten Fenster erscheinen sie groß gesetzt.

```html
<section class="slide" data-title="Ergebnisse">
  <h2 data-anim>Was wir gefunden haben</h2>
  …
  <aside class="notes">Auf die Streuung hinweisen. Etwa zwei Minuten.</aside>
</section>
```

---

## Wo steht welcher Text

Alles Änderbare liegt im `<body>`. Der Kopfkommentar in der Datei führt dieselbe Liste.

| Was | Wo |
|---|---|
| Text einer Folie | `<section class="slide">` — eine Folie je Abschnitt |
| Beschriftung der Registerkarte | `data-title="…"` an der `<section>` |
| Name und Tagung in der Fußzeile | `<p class="foot-meta">` — eine einzige Stelle |
| Autor:innen und Einrichtung | `<div class="byline">` auf der Titelfolie |
| Logo | Symbol `logo-rwth` am Anfang des `<body>` — **eine** Stelle; Titel-, Dankfolie und Fußzeile setzen es per `<use>` ein. Quelle: `RWTH_Logo_3.svg` |
| Folienformat | `--stage-w` / `--stage-h` im `<style>`, Abschnitt 1 |
| Farben | `<style>`, Abschnitt 1 |

### Gliederungsebenen

Verschachtelte `<ul>` brauchen keine Klasse — die Ebene ergibt sich aus der Tiefe.

```html
<ul class="points">
  <li>Erhebung in zwei Wellen
    <ul>
      <li>Vortest im September
        <ul><li>Konzepttest und Fragebogen</li></ul>
      </li>
    </ul>
  </li>
</ul>
```

| Ebene | Marke | Schriftgrad |
|---|---|---|
| 1 | runder Punkt, Blau 100 % | 19 px |
| 2 | Strich, Blau 75 % | 17 px |
| 3 | Viereck, Blau 50 % | 15,5 px |

### Eine Folie hinzufügen

```html
<section class="slide" data-title="Ausblick">
  <p class="eyebrow" data-anim>Diskussion</p>
  <h2 data-anim>Was daraus folgt</h2>
  <ul class="points" data-anim>
    <li>Erster Punkt.</li>
    <li data-step="1">Erscheint beim ersten Pfeildruck.</li>
  </ul>
</section>
```

Register, Übersicht, Fortschrittsbalken und Zifferntasten richten sich automatisch
nach der Zahl der Folien.

---

## Bausteine

| Klasse | Wirkung |
|---|---|
| `.slide.hero` | Titel- und Abschlussfolie: große blaue Karte, weiße Schrift, ohne Fußzeile; die Karte wächst mit dem Inhalt; langer Titel als `h1.lang` (72 px, zwei Zeilen) |
| `.cols` | zwei gleich breite Spalten, jede als weiße Karte |
| `.cols.wide-left` | dasselbe im Verhältnis 1,15 : 0,85 |
| `ul.points` | Aufzählung mit drei Ebenen: runder Punkt, Strich, Viereck — einfach `<ul>` verschachteln, jede Ebene wird etwas kleiner |
| `ul.points.long` | kleinerer Grad für textreiche Folien |
| `ul.refs` | Quellenverzeichnis mit hängendem Einzug |
| `.stats` / `.stat` | Kennzahlenkacheln: große blaue Zahl über der Beschriftung |
| `.keys` | zweispaltige Definitionsliste |
| `.slide.these` | Behauptung + Beleg: Titel als Satz in 38 px, zwei Zeilen erlaubt |
| `.frage` / `.antwort-karte` | Frage groß, Antwort als blaue Karte mit `.antwort-kurz` und `ul.points` |
| `.pm.plus` / `.pm.minus` | Karte mit `h3` und `ul.points`, Plus- oder Minuszeichen statt Punkte |
| `.gegen` | Gegenüberstellung: Raster aus `.gegen-kopf`, dann je Zeile `.gegen-l`, `.gegen-pfeil`, `.gegen-r` |
| `.bilanz` / `.hyp` | Hypothesen-Bilanz: `.hyp-nr`, `.hyp-txt`, `.hyp-mark.ja/.nein/.offen` |
| `.botschaften` / `.botschaft` | drei Karten mit `.nr` und einem `p` |
| `.kern` / `.erl` | Kernsatz mit Erläuterung: der Satz als `p.kern` (33 px, blau) statt eines `h2`, darunter `.erl` als Karte mit einem `p` je Zeile, `b` als Stichwort in Blau |
| `.gleichung` | Merkform A + B → C: `.term` als Kachel mit `b` und `span`, `.term.ergebnis` blau, dazwischen `.op` mit dem Zeichen; Zeichen und Term tragen dasselbe `data-step` |
| `.design` | Studiendesign: Raster `190px var(--spalten)`; erste Zeile leer + `p.design-kopf` (mit `span` für die Woche), dann je Gruppe `p.design-gruppe` und Zellen `p.design-mess` (Pille, `.offen` gestrichelt) oder `p.design-block` (blau, `.kontrolle` als Rahmen) |
| `.stat .von` / `.stat .delta` | Kennzahl mit Veränderung: `span.von` („48 % →") über dem `b`, `i.delta` als Pille oben rechts in der Kachel (`.null` grau) |
| `.gantt` | Zeitplan: `--spalten` Quartale, `.gantt-kopf` mit `p.gantt-q`, je Paket eine `.gantt-zeile` aus `p.gantt-aufgabe` und `p.gantt-balken` (`--von`, `--dauer`, `.fertig` blau); `.gantt-heute` mit `--anteil` 0–1 als Linie |
| `.konv` | Konvergenz: `.konv-quellen` mit drei `p.konv-befund`, `.konv-mitte` mit dem Pfeil-SVG, `p.konv-ziel` als blaue Karte; die Mitten der drei Karten liegen bei 1/6, 1/2 und 5/6 der Höhe — dort setzen die Pfeile an |
| `ol.fragen` | nummerierte Fragen, groß; die Ziffer kommt aus dem Zähler |
| `.aufgabe` | Aufgabenfolie: `.aufgabe-nr`, `.aufgabe-stamm`, `ol.optionen` mit `li.option` (`--p` als Anteil), darin `.buchst`, `.txt`, `.antwort` (Balken und Wert) |
| `figure` + `figcaption` | Grafik oder Diagramm mit Bildunterschrift. Auch für ein Rasterbild: `<img>` als Daten-URI hinein, es steht unverzerrt und mittig, höchstens 410 px hoch (seit dem 15.09.; die Karte endet dann bei 650) |
| `pre` | Codeblock, blau getönt |
| `.chip` | Pille für Schlagworte — vorhanden, in der Vorlage derzeit ungenutzt |
| `.slide.anhang` | Folie für die Fragerunde, nur über die Übersicht erreichbar |
| `.tiles` / `.tile` | Kachelreihe für Bilder oder Skizzen |
| `.kacheln` / `.kachel` | Große Kacheln mit wenig Inhalt: Nummer (`.nr`), Schlagwort (`b`), eine Zeile (`span`). Eine Kachel mit `data-step` und `data-keep` wird beim Schritt blau |
| `.kette` / `.glied` / `.kette-kopf` | Chevron-Kette: Pfeilköpfe als Phasen, darunter je eine Spalte Stichpunkte. Glieder lassen sich mit `data-step` nacheinander aufbauen |
| `.karten` / `.karte` | Karten mit Titelschild: `h3` als blaue Pille auf der Oberkante, darunter Stichpunkte — für Kategorien |
| `.slide.trenner` | Abschnittstrenner: blaue Karte, großer Abschnittstitel, Agenda als Chips mit `.aktiv` für den laufenden. Jeder Trenner eröffnet in der Übersicht automatisch eine eigene Gruppe mit Trennzeile |
| `.bahnen` | Schwimmbahnen: `.bahn-koepfe` mit den Phasen, dann je Rolle eine `.bahn` aus `.bahn-rolle` und `.bahn-zelle`n; Spaltenzahl in `--phasen`, `.leer` für eine bewusst leere Zelle |
| `.zeit` | Zeitleiste: Phasen und Messzeitpunkte auf einem Raster mit `--spalten`, `--von`, `--dauer`, `--bei`. `.zeit-ebene` legt eine zweite Ebene darüber, `.zeit-marke.klein` setzt deren Anfang und Ende als kleine Punkte — Karte und Punkt in derselben Farbe |
| `table.vgl` | Vergleichstabelle; `.mk.ja` / `.mk.halb` / `.mk.nein` als Ausfüllgrad, `.num` für Ziffernschrift |
| `.zitat` | eine Äußerung, groß gesetzt, mit `.zitat-quelle` als Beleg |
| `.trans` | Transkript aus Zeilennummer, Sprecher, Text und Kodierung; `<mark>` hebt Stellen hervor |
| `.herleit` | schrittweise Herleitung, alle Zeilen am Relationszeichen bündig |
| `.tex` + `data-tex` | Formel: LaTeX im Attribut, MathML darin — siehe „Formeln" |
| `.pops` | Element ploppt beim Erscheinen auf, statt einzublenden |
| `data-keep` | Element ist von Anfang an sichtbar; `data-step` löst nur seine eigene Bewegung aus (etwa den Deckel) |

### Zeichenvorrat

Die eingebettete Fira Sans und Fira Mono tragen **Latein mit allen Akzenten,
Griechisch, Pfeile und Rechenzeichen**: `Δ π σ α β θ ω φ`, `√ ≈ ≤ ≥ ≠ ∞ ∑ ∫ ∂`,
`← → ↑ ↓`, `₀ ₁ ₂ ⁿ ½ ‰ €`, dazu `Č Ł ő ş ğ`. Solche Zeichen stehen im Fließtext
einfach so — keine Klasse, kein Ersatz.

Was Fira Sans nicht hat (etwa `↔ ⇒ ∇ ℏ ■ ●`), gehört in eine Formel: `data-tex`,
dort setzt Fira Math alles. `python3 werkzeuge/schriften.py --pruefen` sagt, ob im Foliensatz
ein Zeichen steht, das aus der Schrift fällt.

Den Teilsatz schneidet `schriften.py` aus der vollständigen Fira (Google-Fonts-Ausgabe
4.203, dieselbe wie zuvor — die Maße sind unverändert). Kyrillisch ist bewusst nicht
dabei. Wer den Vorrat ändern will, ändert die Liste `BEREICHE` im Skript und lässt es
laufen; das Netz braucht nur dieser Schritt, die fertige Datei nicht.

## Formeln

Für eine Formel reicht der Zeichenvorrat nicht: In der Datei steckt **kein kursiver
Schnitt**, jedes `<i>` wird vom Browser künstlich geneigt, und es gibt weder
mitwachsende Wurzeln noch mitwachsende Klammern noch die Abstandsregeln des Formelsatzes.

Deshalb setzt der Foliensatz Formeln als **MathML in Fira Math** — der Mathe-Schwester
der Hausschrift. Den Satz erledigt der Browser, ohne JavaScript und ohne Bibliothek.

Im Quelltext steht LaTeX:

```html
<span class="tex" data-tex="T = 2\pi\sqrt{\dfrac{l}{g}}"></span>
```

Danach `python3 werkzeuge/formeln.py` — das Skript füllt jeden solchen Kasten mit MathML und
bettet die Schrift ein. Das Attribut bleibt die Quelle, das MathML ist das Erzeugnis.
Formel ändern heißt: Attribut ändern, Skript laufen lassen.

Die Kursive ist dabei **echt**: Fira Math bringt eigene Glyphen für Formelzeichen mit,
der Browser tauscht die Buchstaben dorthin. Ein `<i>` hätte die aufrechte Form nur
schräg gestellt — kursive Schnitte enthält die Datei keine.

Hervorheben geht mit `\colorbox{#e8f1fa}{$…$}`. Griechische Einzelzeichen **außerhalb**
einer Formel brauchen nichts — die Textschrift hat sie (siehe „Zeichenvorrat").

Alles ist **eingebettet**: die Schrift als base64, keine URL bleibt übrig. Die Datei
stellt keine einzige Anfrage nach außen und läuft auf einem fremden Rechner ohne Netz —
`formeln.py` prüft das nach jedem Lauf. Vorausgesetzt wird MathML Core: Chrome und Edge
ab 109, Safari ab 16.4, Firefox seit je.

Temml und Fira Math holt das Skript beim ersten Mal selbst nach `werkzeuge/geholt/` (nicht im
Repository).
| `.cite` / `.source-note` | Beleg im Fließtext, Fußnote unter dem Inhalt |
| `.byline` | Autor:innen und Einrichtung |
| `<aside class="notes">` | Sprechnotizen — nur in der Vortragendenansicht sichtbar |
| `data-anim` | Element tritt beim Folienwechsel gestaffelt auf |
| `data-step="n"` | Element erscheint erst beim n-ten Pfeildruck |
| `data-step-until="n"` | … und verschwindet beim n-ten wieder |

---


## Anhangsfolien

Folien für die Fragerunde: Dinge, für die im Vortrag kein Platz war, nach denen aber
gefragt wird. Sie tragen eine Klasse, alles Weitere folgt daraus.

```html
<section class="slide anhang" data-title="Wie gut trennen die Items?">
```

| | Verhalten |
|---|---|
| **Pfeile** | blättern ganz normal hindurch. Der Anhang ist eingereiht wie jede andere Folie. |
| **Fortschrittsbalken** | zählt sie **nicht** mit. Auf der letzten Folie des Vortrags steht er voll und bleibt es. |
| **Register** | zeigt sie **nicht** — es bliebe sonst für den Vortrag weniger Platz. |
| **Übersicht** (`0`) | zeigt sie, abgesetzt unter der Zeile „Anhang". Von dort springt man gezielt hin. |
| **Fußzeile** | `A1`, `A2`, `A3` statt weiterzuzählen. |
| **Auftritt** | keiner. `data-anim` und `data-step` werden entfernt: in der Fragerunde soll die Antwort sofort ganz dastehen. |

**Beschrifte sie nach der Frage, nicht nach dem Inhalt.** Also `data-title="Wie gut
trennen die Items?"` statt `data-title="Itemkennwerte"`. In der Fragerunde suchst du in
der Übersicht nach der Frage, die man dir gerade gestellt hat.

**Sprechnotizen auch dort.** Anhangsfolien liegen oft Monate brach; wenn die Frage kommt,
ist die Zahl darauf nicht mehr präsent.

## Formensammlung

Fünfundvierzig Folien in der Vorlage zeigen wiederverwendbare Darstellungen. Der Inhalt ist
Platzhalter — es geht um die Form.

| Folie | Was sie hergibt |
|---|---|
| **Einordnung** | Zwei kleine Formen auf einer Folie: Schnittmenge aus drei Kreisen (Mitte als Schritt) und Vier-Felder-Matrix, jeder Baustein mittig in seinem Feld. |
| **Übergänge** | Übergangsmatrix als Sankey: 3 × 3 Zahlen im Skript, Bandbreite nach Anzahl, Farbe nach Ausgangskategorie; ein Schritt zeichnet die Rückwege nach. |
| **Kategoriensystem** | Baum aus einer verschachtelten Liste: Wurzel, Kategorien, Unterkategorien — jeder Ast klappt als eigener Schritt auf. |
| **Spirale** | Der offene Kreis: drei Windungen, je vier Stationen, jede Windung ein Schritt. Für alles, was sich wiederholt und dabei vorankommt. |
| **Ausschluss** | Ja/Nein-Weichen in einer Reihe: „ja" führt weiter, „nein" zweigt mit Anzahl und Grund ab; die Restzahlen rechnet das Skript. |
| **Einschätzung** | Likert-Stapelbalken: fünf Anteile je Aussage, Ablehnung grau nach links, Zustimmung blau nach rechts, die Mitte halb auf jeder Seite. Skala aus den Daten, sortiert nach Zustimmung. Ein Schritt zeigt die Summen. |
| **Verteilungen** | Boxplots aus Rohdaten: Quartile, Antennen bis 1,5·IQA und Ausreißer werden im Skript gerechnet, nicht eingetragen. Vier Gruppen, in zwei Schritten eingeblendet. |
| **Wünsche** | Zehn waagerechte Balken, absteigend nach Nennungen. Die Liste im Skript darf ungeordnet sein — sortiert wird beim Aufbau. Ein Schritt legt eine Bezugslinie („Hälfte der Befragten") hinein. |
| **Rundlauf** | Kreisprozess mit vier Stationen. Positionen und Bogenpfeile entstehen aus Winkeln; der letzte Pfeil schließt den Kreis als eigener Schritt. |
| **Von oben nach unten** | Trichter über vier Stufen mit Schwund daneben — für Stichprobenauswahl, Kodierschritte, jede Kette mit Ausfällen. |
| **Aufploppen** | Vier Kacheln, die nacheinander aufspringen. Das `<svg>` in der Kachel lässt sich gegen ein `<img>` tauschen. |
| **Deckel ab** | Eine Kiste, deren Deckel sich abhebt und in der eine Pflanze wächst. Das Wachstum ist ein Pfad, dessen Strichmuster von 100 auf 0 läuft. |
| **Gegenüberstellung** | Vorstellung der Lernenden links, Fachkonzept rechts, Zeile für Zeile mit Pfeil dazwischen (`.gegen`); die rechte Seite erscheint zeilenweise. |
| **Antwortkurven** | Item-Antwortkurven: je Antwortoption eine Linie über der Gesamtpunktzahl (Gruppenmitten und Anteile im Skript); die richtige Option blau, der Distraktor mit Vorstellung gestrichelt. Die Marke „ab hier führt B" wird aus den Daten gerechnet. |
| **Forest Plot** | Effektstärke mit Intervall je Teilgruppe, Punkt und Antenne; der Gesamteffekt als Raute mit eigener Linie im Schritt. |
| **Hypothesen** | Hypothesen-Bilanz (`.bilanz`): Nummer, Erwartung, Befund als Pille im Schritt — `.ja` blau, `.nein` umrandet, `.offen` hellblau. |
| **Drei Botschaften** | Drei Karten (`.botschaften`), große Ziffer und ein Satz; die zweite und dritte als Schritte. |
| **Fragen an Sie** | `ol.fragen`: nummerierte Fragen groß gesetzt, als Schritte — die letzte Folie, bleibt in der Diskussion stehen. |
| **Kernsatz** | Eine Aussage groß in Blau (`.kern`, 33 px), darunter das Kleingedruckte Zeile für Zeile als Schritte (`.erl`). Kein `h2` — der Satz ist der Titel. |
| **Konvergenz** | Drei Befunde laufen auf einen Schluss zu (`.konv`): Karten links, Pfeile in der Mitte, die Folgerung als blaue Karte rechts. Befunde einzeln, Pfeile und Schluss zusammen im letzten Schritt. Gegenstück zur Verzweigung. |
| **Gleichung** | A + B → C als Merkform (`.gleichung`): drei Terme als Kacheln, das Ergebnis blau, Plus und Pfeil groß dazwischen; Term und Zeichen erscheinen zusammen. |
| **Dreieck und Zwiebel** | Triade (drei Ecken als Pillen, Breite am Text gemessen, Kanten mit Doppelpfeil als Schritt) und Zwiebel (Kern und drei Schichten, je Schicht ein Schritt, Beschriftung im Band) auf einer Folie. |
| **Stufen** | Pyramide: Stufen als Trapeze von unten nach oben, rechts je eine Erläuterung mit punktierter Linie; Liste im Skript, jede Stufe ein Schritt. |
| **Zuordnung** | Zwei Spalten mit Kästen, Linien dazwischen aus Indexpaaren im Skript; die Linien eines Konzepts erscheinen zusammen als Schritt — mehrere Vorstellungen treffen dasselbe Konzept. |
| **Freikörperbild** | Körper auf schiefer Ebene, alles aus dem Winkel gerechnet: Gewichtskraft, Normalkraft, Haftreibung als Schritte 1–3, Zerlegung in Hangabtrieb und Anpresskraft als Schritt 4. Pfeilspitzen als Polygone, keine Marker. |
| **Studiendesign** | Gruppen × Zeitpunkte als Raster (`.design`): Messung als Pille, Intervention als blauer Kasten, Kontrollbedingung als Rahmen, ausstehendes Follow-up gestrichelt. Nur CSS. |
| **Histogramm** | Klassen zu 10 Punkten, gezählt aus den Rohwerten im Skript; Schritt 1 die Referenzlinie, Schritt 2 die Säulen darüber hervorgehoben samt Anteil — gerechnet. |
| **Heatmap** | Items × Gruppen, Zelle blau mit Deckkraft nach Wert (Potenz 1,5 gespreizt), Schrift hell auf dunkler Zelle; Nachtest als Schritt 1, Zuwachs als Schritt 2. |
| **Veränderung** | Kennzahlenkacheln mit vorher → nachher und Differenz als Pille (`.stat .von`, `.stat .delta`); grau, wo sich nichts bewegt hat. |
| **Zeitplan** | Gantt (`.gantt`): Pakete über Quartalen, jeder Balken nennt `--von` und `--dauer`, die Heute-Linie `--anteil` als Schritt. Nur CSS. |
| **Slopegraph** | Eine Linie je Person vom Vortest zum Nachtest, steigend blau, fallend grau; Schritt 1 legt das Gruppenmittel als dicke Linie darüber, Schritt 2 hebt die Fallenden hervor und zählt sie — beides gerechnet aus den Paaren im Skript. |
| **Einflüsse** | Stern: ein Kern, Satelliten auf einer Ellipse, Lage aus der Zahl der Satelliten; Beschriftung, Unterzeile und Schritt als Liste im Skript, Pillenbreite am Text gemessen. |
| **Pfadmodell** | Kästen und Pfeile aus einer Liste (Knoten mit Lage, Kanten mit Koeffizient); die Pfeile enden am Kastenrand. Schritt 1 die Koeffizienten, Schritt 2 der indirekte Weg, hervorgehoben und ausgerechnet. |
| **Behauptung** | Assertion-Evidence: `.slide.these` — der Titel ein ganzer Satz (38 px, zwei Zeilen erlaubt), darunter genau ein Beleg. Hier divergierende Säulen um eine Nulllinie (positiv blau, negativ grau, sortiert), das Mittel als Schritt. |
| **Punktfeld** | Hundert Punkte, zeilenweise gefärbt nach einer Liste ganzer Zahlen, je Anteil ein Schritt, Legende daneben. „27 von 100" statt 27 %. |
| **Frage und Antwort** | Forschungsfrage groß (`.frage`), die Antwort als blaue Karte (`.antwort-karte`) im ersten Schritt, Stützpunkte im zweiten. Als Schlussfolie: die Leitfrage wiederholen und in zwei Sätzen beantworten. |
| **Stärken und Grenzen** | Plus / Minus: zwei Karten (`.pm.plus`, `.pm.minus`), Zeichen statt Punkte, die Grenzen als Schritt. |
| **Zeiger** | Foto mit Zeigern: Bild (`<image>` mit Daten-URI) und Zeiger in einem SVG mit einem Koordinatensystem — Ziel, Linie und Beschriftung stehen als Zahlen im Quelltext, jeder Zeiger ein Schritt. Für ein eigenes Foto: `href` tauschen, `width`/`height` auf dessen Seitenverhältnis setzen, Zeiger neu setzen. |
| **Bildpaar** | Zwei Bilder nebeneinander, je eine Unterschrift, das zweite als Schritt. Beide im selben Seitenverhältnis, sonst stehen die Unterschriften nicht auf einer Höhe. |
| **Messkurve** | Liniendiagramm über der Zeit: Reihen als Arrays im Skript, Achsen daraus; jede Reihe ein Schritt, die Modellkurve (Sättigung mit Endtemperatur und Zeitkonstante) gestrichelt. Beschriftet am Linienende, ohne Legende. |
| **Aufgabe** | Ein Testitem im Wortlaut, je Option ein Balken mit der Lösungshäufigkeit (`--p` an der Option). Schritt 1 zeigt die Balken, Schritt 2 hebt die richtige Option hervor (`data-step` + `data-keep`). Kein SVG, nur CSS. |
| **Hantel** | Je Aufgabe zwei Punkte (Vortest grau, Nachtest blau) mit Strich dazwischen, nach Zuwachs sortiert — sortiert wird beim Aufbau. |
| **Effektstärke** | Zwei Normalverteilungen gleicher Streuung, die Achse in Standardabweichungen; Cohens *d* als Klammer zwischen den Mitten, dazu der Anteil über dem Kontrollmittel (Φ(*d*)). |
| **Energiefluss** | Sankey mit frei benannten Knoten in Spalten: Knoten nennen ihre Spalte, Flüsse ihren Anteil, Höhe und Lage werden gerechnet; jede weitere Spalte ein Schritt. Anders als „Übergänge" nicht an 3 × 3 gebunden. |
| **Klimabox** | Bild mit Text: ein Rasterbild (PNG, als Daten-URI eingebettet, 21 KB) in der linken Karte, Stichpunkte rechts, die einzeln erscheinen. Vor dem Einbetten Weißrand beschneiden und auf etwa 1200 px Breite bringen — mehr braucht die Bühne nicht. |

Alle Grafiken sind Inline-SVG in denselben Farben und derselben Schrift; das eine
Rasterbild (Klimabox) steckt als Daten-URI in der Datei. Keine Fremdbibliothek,
nichts nachzuladen.

---

## Wie es funktioniert

**Bühne.** Alle Folien liegen deckungsgleich übereinander, genau eine trägt `.active`.
Die Bühne misst fest 1280 × 720 px und wird als Ganzes per `transform: scale()` ans
Fenster angepasst. Dadurch sind alle Maße in Pixeln verlässlich.

**Übergänge.** Ein Vorzeichen entscheidet über die Richtung: die neue Folie kommt von
der Seite herein, in die geblättert wird, die alte geht in dieselbe Richtung ab.
Innerhalb der Folie treten Elemente gestaffelt auf.

**Register.** Die Karte schiebt sich um ihre *eigene* Breite nach rechts aus dem Bild,
abzüglich des sichtbar bleibenden Teils — `translateX(calc(100% - var(--peek)))`. Weil
sich `100%` auf die Elementbreite bezieht, gilt dieselbe Regel für jede Titellänge.
In Ruhe bleiben 12 px sichtbar (Streifen 8 px, `--stripe`, plus 4 px Papier, `--peek`), der
ganze Block ist auf 70 % gedeckt; unter der Maus oder mit Tastaturfokus tritt er voll hervor.

**Miniaturen.** Keine Bilder, sondern echte Kopien der Folien (`cloneNode`), per
`scale()` verkleinert. Ändert man eine Folie, ändert sich die Miniatur mit.

**Diagramme.** Achsen, Teilstriche, Beschriftung und Kurven entstehen aus den Zahlen
im Quelltext, nicht umgekehrt. Der Verlauf kann von Schritt zu Schritt wandern
(Morph), ohne dass es eine zweite Folie braucht.

**Barrierefreiheit.** Bei `prefers-reduced-motion` fällt jede Bewegung weg, der Inhalt
bleibt vollständig. Das Register ist mit der Tastatur bedienbar.

**Seitenverhältnis.** Der Foliensatz ist 16:9. Passt das Fenster nicht dazu, bleiben
Streifen frei: im Fenster in der Farbe des Folienhintergrunds, also unsichtbar, im
**Vollbild schwarz** — so hält es PowerPoint auch. Beamer und Hörsaalprojektoren sind
in aller Regel 16:9, dort entfallen die Streifen ganz; sichtbar werden sie vor allem
auf Laptopbildschirmen im Format 16:10.

**Satzspiegel.** Der untere Streifen ist für die Fußzeile reserviert (`--pad-b`, 70 px:
Inhalt bis 650, das Logo beginnt bei 662), damit Karten und Text nie darüber liegen.
Abbildungen sind zusätzlich auf 430 px Höhe begrenzt — das verkleinert die Zeichnung,
verzerrt sie nicht.

**Fläche nutzen.** Karten sind so hoch wie ihr Inhalt; Spalten müssen nicht gleich hoch
sein. Dafür ist jede Grafik so hoch gebaut, dass ihre Karte bei 650 endet — die Höhe der
`viewBox` ist deshalb je Folie anders. `pruefen.py` meldet „Luft", wenn eine Folie unter
85 % bleibt: bei einer Grafik heißt das „höher bauen", bei Text ist es in Ordnung.

---

## PDF und Drucken

```bash
python3 werkzeuge/pdf.py                          # vorlage.html → vorlage.pdf daneben
python3 werkzeuge/pdf.py dpg-2027.html            # ein Vortrag → dpg-2027.pdf daneben
python3 werkzeuge/pdf.py dpg-2027.html Abgabe.pdf # anderer Name
```

Ergebnis: **eine Seite je Folie, Anhang eingeschlossen, jede Folie fertig aufgebaut** —
alle Einblendungen sichtbar, der Morph auf der Parabel, der Deckel offen, die
hervorgehobene Kachel blau. Jede Seite trägt die Fußzeile mit ihrer Nummer (`09`, `A1`);
nur Titel- und Dankfolie bleiben ohne, wie im Vortrag. Seitenformat 16:9 (1280 × 720 px
aus `@page`). Das Skript zählt am Ende Seiten gegen Folien und bricht ab, wenn es nicht
aufgeht. Es braucht nur Google Chrome oder Chromium.

**Von Hand geht es genauso:** Im Browser Cmd/Strg+P, Ränder „keine", Hintergrundgrafiken
an, als PDF sichern — von jeder Folie aus, in jedem Aufbauzustand. Der Foliensatz merkt
das Drucken (`beforeprint`), stellt jede Folie auf ihren letzten Schritt und gibt jeder
Folie eine Kopie der Fußzeile mit ihrer Nummer (die echte liegt einmal in der Bühne und
käme im Druck sonst auf keine Seite); nach dem Drucken steht der Vortrag wieder, wo er
war. Das Druck-Stylesheet (`@media print`) legt jede Folie als eigene Seite an und blendet
Register, Balken und Übersicht aus. `pdf.py` macht dasselbe in einem unsichtbaren Chrome.

`vorlage.html?druck=1` schaltet diesen Zustand dauerhaft ein — zum Ansehen im Browser,
was gedruckt würde.

---


## Hinweis zu den Inhalten

Die Vorlage enthält **Platzhalter**: Autor:innen, Zahlen und Quellenangaben sind
erfunden und auf den Folien als solche gekennzeichnet. Einzige Ausnahme ist die
korrekte Angabe zu Hestenes, Wells & Swackhamer (1992), *Force Concept Inventory*.
Vor einem echten Vortrag alle übrigen Angaben ersetzen.
