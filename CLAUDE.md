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
| `vorlage.html` | **Quelle der Wahrheit.** Standard-Foliensatz, 13 Folien. |
| `anleitung.html` | Bedienungsanleitung, selbst ein Foliensatz. Teilt sich den Unterbau. |
| `technik-uebernehmen.py` | Überträgt Stylesheet, Vortragendenansicht und Skript von der Vorlage in die Anleitung. |
| `pruefen.py` | Misst jede Folie im Browser: Überlauf, Füllstand, kleinste Schrift. |
| `Sessions/<datum>.md` | Protokolle. Bei nennenswerten Änderungen ein neues anlegen. |

**Regel:** Technik immer in `vorlage.html` ändern, danach `python3 technik-uebernehmen.py`.
Nie direkt in `anleitung.html` am Stylesheet oder Skript arbeiten.

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
| Untertitel, Vorspann | `.lead` | 24 px |
| Aufzählung Ebene 1 | `ul.points li` | 19 px |
| Aufzählung Ebene 2 | verschachteltes `ul` | 17 px |
| Aufzählung Ebene 3 | doppelt verschachtelt | 15,5 px |
| Fließtext | `.body` | 19 px |
| Quellen | `ul.refs li` | 16 px |
| Code | `pre` | 14,5 px |
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
| `.chip` | Pille für Agenda oder Schlagworte |
| `.cite` / `.source-note` | Beleg im Fließtext, Fußnote |
| `.pops` | ploppt beim Erscheinen auf statt einzublenden |
| `data-anim` | tritt beim Folienwechsel gestaffelt auf |
| `data-step="n"` | erscheint beim n-ten Pfeildruck |
| `data-step-until="n"` | verschwindet beim n-ten wieder |
| `data-keep` | bleibt sichtbar, `data-step` löst nur die eigene Bewegung aus |
| `<aside class="notes">` | Sprechnotizen, nur in der Vortragendenansicht |

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
· `O`/`Esc` Übersicht · `F`/`F5` Vollbild · `P` Vortragendenansicht · `B`/`.`
Schwarzbild · `K` Tastenanzeige. Bild-ab und Bild-auf sind absichtlich belegt: USB-
Presenter senden genau die.

**Die Tastenbelegung steht an drei Stellen:** im Skript von `vorlage.html`, in der
Tabelle der `README.md` und auf der Folie „Steuerung" der `anleitung.html`. Wird eine
Taste ergänzt, müssen alle drei nachgezogen werden — sonst dokumentiert der
Foliensatz etwas anderes, als er tut.

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

---

## Vor dem Abschluss

```bash
python3 pruefen.py            # muss 0 zurückgeben
python3 technik-uebernehmen.py
```

Änderungen an Text oder Inhalt ohne Rückfrage. Änderungen an Farben, Schriftgraden,
Geometrie oder Formensprache **nur auf ausdrückliche Bitte** — diese Entscheidungen
sind gefallen und stehen begründet im Protokoll.

Die Vorlage enthält Platzhalter (Autor:innen, Zahlen, Quellen), auf den Folien als
solche gekennzeichnet. Einzige echte Angabe: Hestenes, Wells & Swackhamer (1992).
Beim Befüllen mit echtem Inhalt keine Quellen erfinden.
