# Registerdeck

Eine Präsentationsvorlage als **eine einzige HTML-Datei**: dünner Fortschrittsbalken
oben, Registerkarten am rechten Rand, die beim Überfahren mit dem Folientitel
herausfahren. Keine externen Anfragen, keine Abhängigkeiten, Schriften eingebettet.

**Warum eine Datei:** Auf einer Tagung steht selten der eigene Rechner auf dem Pult.
`vorlage.html` läuft überall per Doppelklick — offline, ohne Installation, ohne Konto.

Kopieren, Text ersetzen, vortragen. Der Kopfkommentar der Datei sagt, wo was steht;
dieses Dokument geht ins Einzelne.


## Dateien

| Datei | Zweck |
|---|---|
| `vorlage.html` | **Der Standard-Foliensatz.** Kopieren, Text ersetzen, fertig. 21 Folien — jede Darstellungsform genau einmal. |
| `CLAUDE.md` | Arbeitsanweisung für KI-Sitzungen: harte Maße, Schriftgrade, Regeln, bekannte Fallen. Claude Code liest sie beim Start automatisch. |
| `pruefen.py` | Misst jede Folie im Browser: Überlauf, Füllstand, kleinste Schrift. `python3 pruefen.py` |
| `Sessions/` | Datierte Protokolle der Arbeitssitzungen mit allen Entscheidungen und ihren Begründungen. |
| `Darstellungsformen.md` | Vorrat an Darstellungsformen: was gebaut ist, was noch kommen könnte, in welcher Reihenfolge. |
| `formeln.py` | Setzt alle Formeln: LaTeX aus `data-tex` wird zu MathML. Holt Temml und Fira Math selbst. |

Für einen neuen Vortrag: `vorlage.html` kopieren und umbenennen. Das Original bleibt
unangetastet als Ausgangspunkt.

---

## Steuerung

| Taste | Wirkung |
|---|---|
| `→` `↓` `Leertaste` `Bild ab` | erst nächster Einblendschritt, dann nächste Folie |
| `←` `↑` `Bild auf` | zurück — die Folie bleibt dabei fertig aufgebaut |
| `1` … `9` | direkt zur Folie |
| `Pos1` / `Ende` | erste / letzte Folie |
| `0` oder `O` | Übersicht aller Folien — `Esc` schließt sie wieder |
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
| Logo | `<div class="logo">` — zwei Stellen: Fußzeile und Titelfolie |
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
| `.slide.hero` | Titel- und Abschlussfolie: große blaue Karte, weiße Schrift, ohne Fußzeile |
| `.cols` | zwei gleich breite Spalten, jede als weiße Karte |
| `.cols.wide-left` | dasselbe im Verhältnis 1,15 : 0,85 |
| `ul.points` | Aufzählung mit drei Ebenen: runder Punkt, Strich, Viereck — einfach `<ul>` verschachteln, jede Ebene wird etwas kleiner |
| `ul.points.long` | kleinerer Grad für textreiche Folien |
| `ul.refs` | Quellenverzeichnis mit hängendem Einzug |
| `.stats` / `.stat` | Kennzahlenkacheln: große blaue Zahl über der Beschriftung |
| `.keys` | zweispaltige Definitionsliste |
| `figure` + `figcaption` | Grafik oder Diagramm mit Bildunterschrift |
| `pre` | Codeblock, blau getönt |
| `.chip` | Pille für Schlagworte — vorhanden, in der Vorlage derzeit ungenutzt |
| `.tiles` / `.tile` | Kachelreihe für Bilder oder Skizzen |
| `.zeit` | Zeitleiste: Phasen und Messzeitpunkte auf einem Raster mit `--spalten`, `--von`, `--dauer`, `--bei` |
| `table.vgl` | Vergleichstabelle; `.mk.ja` / `.mk.halb` / `.mk.nein` als Ausfüllgrad, `.num` für Ziffernschrift |
| `.zitat` | eine Äußerung, groß gesetzt, mit `.zitat-quelle` als Beleg |
| `.trans` | Transkript aus Zeilennummer, Sprecher, Text und Kodierung; `<mark>` hebt Stellen hervor |
| `.herleit` | schrittweise Herleitung, alle Zeilen am Relationszeichen bündig |
| `.m` | Formel im Fließtext; `<i>` setzt das Formelzeichen kursiv, `.ein` hält Einheiten aufrecht |
| `.frac` / `.wurzel` / `.vec` | Bruch, gezeichnete Wurzel, Pfeil über dem Zeichen |
| `.gr` | griechische Buchstaben und mathematische Zeichen — siehe Hinweis unten |
| `.hl` | hebt den Term hervor, um den es gerade geht |
| `.pops` | Element ploppt beim Erscheinen auf, statt einzublenden |
| `data-keep` | Element ist von Anfang an sichtbar; `data-step` löst nur seine eigene Bewegung aus (etwa den Deckel) |

### Was der eingebettete Zeichensatz nicht kann

Eingebettet ist nur der lateinische Zeichenvorrat. Vorhanden sind `· × − ½ ¼ ¾ ² ³ ° ± µ`,
**nicht** vorhanden sind `Δ π σ α β θ ω √ ≈ ≤ ≥ ≠ → ←`. Deshalb:

* Die Wurzel ist **gezeichnet** (`.wurzel`) und wächst mit ihrem Inhalt — sie braucht kein Zeichen.
* Alles Übrige holt `.gr` aus der Systemschrift (Lucida Grande, dann Helvetica Neue).
  Nachgemessen: von den verfügbaren Schriften passt Lucida Grande am besten zu Fira Sans.
* In Tabellen stehen Ausfüllgrade (`.mk`) statt Häkchen.

Diese Bausteine sind der **Notbehelf** und stammen aus der Zeit vor dem echten
Formelsatz. Für richtige Mathematik siehe den nächsten Abschnitt.

## Formeln

Der handgebaute Satz oben (`.frac`, `.wurzel`, `.vec`) reicht für eine Formel im
Fließtext, aber nicht für echte Mathematik: In der Datei steckt **kein kursiver
Schnitt**, jedes `<i>` wird vom Browser künstlich geneigt, und es gibt weder
Wurzelzeichen noch mitwachsende Klammern noch die Abstandsregeln des Formelsatzes.

Deshalb setzt der Foliensatz Formeln als **MathML in Fira Math** — der Mathe-Schwester
der Hausschrift. Den Satz erledigt der Browser, ohne JavaScript und ohne Bibliothek.

Im Quelltext steht LaTeX:

```html
<span class="tex" data-tex="T = 2\pi\sqrt{\dfrac{l}{g}}"></span>
```

Danach `python3 formeln.py` — das Skript füllt jeden solchen Kasten mit MathML und
bettet die Schrift ein. Das Attribut bleibt die Quelle, das MathML ist das Erzeugnis.
Formel ändern heißt: Attribut ändern, Skript laufen lassen.

Die Kursive ist dabei **echt**: Fira Math bringt eigene Glyphen für Formelzeichen mit,
der Browser tauscht die Buchstaben dorthin. Ein `<i>` hätte die aufrechte Form nur
schräg gestellt — kursive Schnitte enthält die Datei keine.

Hervorheben geht mit `\colorbox{#e8f1fa}{$…$}`, griechische Einzelzeichen **außerhalb**
einer Formel mit `<span class="gr">Δ</span>`.

Alles ist **eingebettet**: die Schrift als base64, keine URL bleibt übrig. Die Datei
stellt keine einzige Anfrage nach außen und läuft auf einem fremden Rechner ohne Netz —
`formeln.py` prüft das nach jedem Lauf. Vorausgesetzt wird MathML Core: Chrome und Edge
ab 109, Safari ab 16.4, Firefox seit je.

Temml und Fira Math holt das Skript beim ersten Mal selbst nach `werkzeug/` (nicht im
Repository).
| `.cite` / `.source-note` | Beleg im Fließtext, Fußnote unter dem Inhalt |
| `.byline` | Autor:innen und Einrichtung |
| `<aside class="notes">` | Sprechnotizen — nur in der Vortragendenansicht sichtbar |
| `data-anim` | Element tritt beim Folienwechsel gestaffelt auf |
| `data-step="n"` | Element erscheint erst beim n-ten Pfeildruck |
| `data-step-until="n"` | … und verschwindet beim n-ten wieder |

---

## Formensammlung

Fünf Folien in der Vorlage zeigen wiederverwendbare Darstellungen. Der Inhalt ist
Platzhalter — es geht um die Form.

| Folie | Was sie hergibt |
|---|---|
| **Verteilungen** | Boxplots aus Rohdaten: Quartile, Antennen bis 1,5·IQA und Ausreißer werden im Skript gerechnet, nicht eingetragen. Vier Gruppen, in zwei Schritten aufgebaut. |
| **Rundlauf** | Kreisprozess mit vier Stationen. Positionen und Bogenpfeile entstehen aus Winkeln; der letzte Pfeil schließt den Kreis als eigener Schritt. |
| **Von oben nach unten** | Trichter über vier Stufen mit Schwund daneben — für Stichprobenauswahl, Kodierschritte, jede Kette mit Ausfällen. |
| **Aufploppen** | Vier Kacheln, die nacheinander aufspringen. Das `<svg>` in der Kachel lässt sich gegen ein `<img>` tauschen. |
| **Deckel ab** | Eine Kiste, deren Deckel sich abhebt und in der eine Pflanze wächst. Das Wachstum ist ein Pfad, dessen Strichmuster von 100 auf 0 läuft. |

Alle Grafiken sind Inline-SVG in denselben Farben und derselben Schrift — kein Bild,
keine Fremdbibliothek, nichts nachzuladen.

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

**Satzspiegel.** Der untere Streifen ist für die Fußzeile reserviert (`--pad-b`), damit
Karten und Text nie darüber liegen. Abbildungen sind zusätzlich auf 400 px Höhe
begrenzt — das verkleinert die Zeichnung, verzerrt sie nicht.

---

## Drucken

Im Browser drucken ergibt ein PDF mit einer Folie je Seite (Ränder auf „keine" stellen).
Einblendungen erscheinen dabei vollständig.

**Bekannte Einschränkung:** Die Fußzeile fehlt im PDF, weil sie einmalig in der Bühne
liegt und nicht je Seite wiederholt wird.

---


## Hinweis zu den Inhalten

Die Vorlage enthält **Platzhalter**: Autor:innen, Zahlen und Quellenangaben sind
erfunden und auf den Folien als solche gekennzeichnet. Einzige Ausnahme ist die
korrekte Angabe zu Hestenes, Wells & Swackhamer (1992), *Force Concept Inventory*.
Vor einem echten Vortrag alle übrigen Angaben ersetzen.
