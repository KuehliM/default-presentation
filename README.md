# Registerdeck

Ein Foliensatz als **einzelne HTML-Datei**. Kein Framework, kein Server, kein Build,
keine Internetverbindung — auch die Schriften stecken in der Datei. Doppelklick genügt.

Gebaut für Vorträge in der Physikdidaktik: Pläne und Ergebnisse vor Fachpublikum,
im Farbklang der RWTH Aachen.

![Folienformat 16:9](https://img.shields.io/badge/Format-16%3A9-00549F) ![Eine Datei](https://img.shields.io/badge/Abh%C3%A4ngigkeiten-keine-00549F)

---

## Dateien

| Datei | Zweck |
|---|---|
| `vorlage.html` | **Der Standard-Foliensatz.** Kopieren, Text ersetzen, fertig. Acht Folien, die alle Bausteine einmal zeigen. |
| `anleitung.html` | Die Bedienungsanleitung — selbst ein Foliensatz, läuft auf derselben Technik. Erklärt Aufbau, Übergänge, Register und Bausteine. |
| `technik-uebernehmen.py` | Überträgt Stylesheet, Vortragendenansicht und Skript von der Vorlage in die Anleitung, damit der Unterbau nur an einer Stelle gepflegt wird. |
| `Sessions/` | Datierte Protokolle der Arbeitssitzungen mit allen Entscheidungen und ihren Begründungen. |

Für einen neuen Vortrag: `vorlage.html` kopieren und umbenennen. Das Original bleibt
unangetastet als Ausgangspunkt.

---

## Steuerung

| Taste | Wirkung |
|---|---|
| `→` `↓` `Leertaste` | erst nächster Einblendschritt, dann nächste Folie |
| `←` `↑` | zurück — die Folie bleibt dabei fertig aufgebaut |
| `1` … `9` | direkt zur Folie |
| `Pos1` / `Ende` | erste / letzte Folie |
| `O` oder `Esc` | Übersicht aller Folien |
| `F` | Vollbild |
| `P` | Vortragendenansicht im zweiten Fenster |

Auf dem Tablet wischen. Die Foliennummer steht in der Adresszeile: `datei.html#3`
springt direkt auf Folie 3.

Am rechten Rand liegt der **Karteikasten**: in Ruhe sieht man nur die farbige Kante
jeder Folie. Nähert sich die Maus, treten die Miniaturen hervor; auf einer Karte
fährt sie ganz heraus und zeigt den Folientitel. Ein Klick springt dorthin.

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
| `ul.points` | Aufzählung, erste Ebene runder blauer Punkt |
| `ul.points.long` | kleinerer Grad für textreiche Folien |
| `ul.refs` | Quellenverzeichnis mit hängendem Einzug |
| `.stats` / `.stat` | Kennzahlenkacheln: große blaue Zahl über der Beschriftung |
| `.keys` | zweispaltige Definitionsliste |
| `figure` + `figcaption` | Grafik oder Diagramm mit Bildunterschrift |
| `pre` | Codeblock, blau getönt |
| `.chip` | Pille für Agenda oder Schlagworte |
| `.tiles` / `.tile` | Kachelreihe für Bilder oder Skizzen |
| `.pops` | Element ploppt beim Erscheinen auf, statt einzublenden |
| `data-keep` | Element ist von Anfang an sichtbar; `data-step` löst nur seine eigene Bewegung aus (etwa den Deckel) |
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

## Beide Dateien gleich halten

`vorlage.html` und `anleitung.html` teilen sich Stylesheet, Vortragendenansicht und
Skript — nur Folien und Notizen unterscheiden sich. **Die Vorlage ist die Quelle.**
Nach einer Änderung an der Technik:

```bash
python3 technik-uebernehmen.py
```

Das Skript überträgt die drei geteilten Blöcke und lässt Titel, Fußzeile und Folien
der Anleitung unangetastet. Es bricht ab, bevor es schreibt, falls dabei etwas
Eigenes verloren ginge.

---

## Hinweis zu den Inhalten

Die Vorlage enthält **Platzhalter**: Autor:innen, Zahlen und Quellenangaben sind
erfunden und auf den Folien als solche gekennzeichnet. Einzige Ausnahme ist die
korrekte Angabe zu Hestenes, Wells & Swackhamer (1992), *Force Concept Inventory*.
Vor einem echten Vortrag alle übrigen Angaben ersetzen.
