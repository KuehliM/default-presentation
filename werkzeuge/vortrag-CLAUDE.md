# Arbeitsanweisung für diesen Vortrag

Dieser Ordner ist **ein Vortrag** auf Grundlage der Vorlage „Registerdeck"
(github.com/KuehliM/default-presentation), angelegt am {datum} mit `neu.py`.
Er ist in sich vollständig — das Repo wird nicht mehr gebraucht.

| Datei | Rolle |
|---|---|
| `{datei}` | **Der Vortrag.** Nur hier wird gearbeitet. Eine HTML-Datei, läuft per Doppelklick, lädt nichts nach. |
| `vorlage.html` | Der Musterbogen: 67 Folien Vortrag + 3 Anhang, jede Darstellungsform genau einmal, alle Inhalte Platzhalter. **Nur lesen und daraus kopieren** — nicht ändern, nicht vortragen. |
| `Darstellungsformen.md` | Katalog der Formen mit ihren Foliennummern in `vorlage.html`. |
| `werkzeuge/` | `pruefen.py`, `formeln.py`, `pdf.py`, `schriften.py` — immer mit dem Dateinamen aufrufen: `python3 werkzeuge/pruefen.py {datei}`. `geholt/` darin holt sich Temml und Schriften bei Bedarf (braucht einmal Netz und `npm`). |
| `bilder/` | Quellen der Bilder. In der Folie stecken sie als Daten-URI, die Datei lädt nichts nach. |

## Ablauf

1. **Kopf:** Titelfolie (`.eyebrow`, `h1`, `.lead`, `.byline`), Dankfolie, Fußzeile
   (`p.foot-meta` unter den Folien) und `title` — die Platzhalter ersetzen. Die blaue Karte
   wächst mit. Titel über etwa 27 Zeichen: `class="lang"` am `h1` (72 px statt 84, zwei Zeilen
   à ~31 Zeichen); die Byline muss über 584 bleiben (`pruefen.py` misst das). Danach die
   Titelfolie **ansehen** — weiße Schrift neben der Karte meldet kein Werkzeug.
2. **Folien anlegen**, zwei Wege, beliebig gemischt:
   * leer: den Block „Erste Folie" kopieren (`eyebrow`, `h2`, `ul.points`, `aside.notes`);
   * aus der Vorlage: Form im Katalog suchen, in `vorlage.html` die **ganze `section`** samt
     Kommentar davor kopieren, hierher setzen, Text ersetzen. Sie funktioniert sofort — der
     Unterbau ist derselbe.
   * **Diagramme:** Die Zahlen stehen nicht in der Folie, sondern im Skript **dieses** Vortrags,
     Block `buildXyz`, der die `id="xyzSvg"` der Folie liest. Dort die Arrays ändern; Achsen,
     Skalen, Beschriftungen entstehen daraus. Jede Form einmal je Datei (die id ist eindeutig);
     dieselbe Form zweimal → Block im Skript kopieren, id in Folie und Block umbenennen.
   * `data-title` beschriftet die Registerkarte, `data-step="n"` lässt etwas beim n-ten
     Pfeildruck erscheinen, `aside.notes` sind Sprechnotizen (Taste `P`).
   * Gliederung: `section.slide.trenner` als Abschnittstrenner (gruppiert Register und Übersicht
     von selbst), `section.slide.anhang` für die Fragerunde ans Ende. Muster in der Vorlage.
3. **Formeln:** LaTeX in `data-tex="…"`, dann `python3 werkzeuge/formeln.py {datei}`.
4. **Messen:** `python3 werkzeuge/pruefen.py {datei}` — Überlauf ist ein Fehler, „Luft" ein
   Hinweis. `python3 werkzeuge/schriften.py {datei} --pruefen` meldet Zeichen, die die Schrift
   nicht hat.
5. **PDF:** `python3 werkzeuge/pdf.py {datei}`.
6. Zum Abschluss einmal durchblättern (kopflos oder im Browser) und auf JavaScript-Fehler horchen.

## Regeln — Kurzfassung der Vorlage

* Bühne 1280 × 720. Inhalt beginnt bei 40 px und endet bei **650 px**; darunter die Fußzeile.
  Satzspiegel 68 px links und rechts. Abbildungen höchstens 430 px hoch.
* **Karten so hoch wie ihr Inhalt, Grafiken so groß wie die Fläche:** Die `viewBox`-Höhe einer
  Grafik so wählen, dass ihre Karte bei 650 endet (`pruefen.py` sagt, wie viel frei ist). Keine
  erzwungene Symmetrie zwischen Spalten; Textfolien dürfen Luft haben.
* Schrift **nie unter 15 px** für alles, was gelesen werden soll. Grundgrad der Formeln 26 px.
* **Keine Änderung an Farben, Schriftgraden, Geometrie oder Formensprache** — das ist Sache
  der Vorlage im Repo. Hier nur Folien und Zahlen.
* Die Datei stellt **keine Anfrage nach außen** (`formeln.py` bricht sonst ab). Bilder als
  Daten-URI: vorher beschneiden, etwa 1200 px breit, bei Zeichnungen Farbzahl reduzieren.
* Zeichen, die die Textschrift nicht hat (`↔ ⇒ ∇ ℏ ℃ ■ ● ▲`), nur in Formeln (`data-tex`).
  `Δ π ≈ ≤ → ←` stehen direkt im Text.
* `<b>` für Betonung, nicht `<em>` (in Stichpunkten ist `em` die Ziffernschrift).
* In Kommentaren keine Elementnamen in spitzen Klammern — Suchen und Ersetzen erwischt sie.
* Keine Quellen erfinden. Platzhalter als solche kennzeichnen, bis echte Inhalte da sind.

## Was hier nicht passiert

Änderungen am Unterbau: Stil, Skriptfunktionen, Register, Übersicht. Wenn etwas daran fehlt
oder hakt, gehört es in die Vorlage im Repo; von dort wird der Block von Hand übernommen.
