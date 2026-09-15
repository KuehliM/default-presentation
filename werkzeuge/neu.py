#!/usr/bin/env python3
"""Neuen Vortrag aus der Vorlage anlegen — als vollständigen Ordner.

    python3 werkzeuge/neu.py Vortraege/dpg-2027 "Wie Lernende Wärme verstehen"
    python3 /tmp/registerdeck/werkzeuge/neu.py . "Titel"      # im Vortragsordner selbst

Legt im Zielordner an:

    <name>.html            der Vortrag: Titel, erste Folie, Dank — mit dem kompletten
                           Unterbau der Vorlage (Stil, Schriften, Logo, Register,
                           Übersicht, Vortragendenansicht, Druck, alle Diagramm-Bauer)
    vorlage.html           der Musterbogen zum Nachschlagen und Kopieren
    Darstellungsformen.md  Katalog der Formen mit Foliennummern
    CLAUDE.md              Arbeitsanweisung für diesen Vortrag (aus vortrag-CLAUDE.md)
    werkzeuge/             pruefen.py, formeln.py, pdf.py, schriften.py
    bilder/                für Bildquellen
    .gitignore             PDFs, geholte Werkzeuge, .DS_Store

Der Name der Datei kommt aus dem Ordnernamen (kleingeschrieben, Umlaute
aufgelöst), `--datei name.html` setzt ihn ausdrücklich. Danach ist der Ordner
unabhängig vom Repo. Vorhandene Dateien werden nicht überschrieben
(`--ueberschreiben` erzwingt es).
"""

import datetime
import pathlib
import re
import shutil
import sys

HIER   = pathlib.Path(__file__).parent          # werkzeuge/ im Repo
WURZEL = HIER.parent
VORLAGE = WURZEL / "vorlage.html"
MITNEHMEN = ["pruefen.py", "formeln.py", "pdf.py", "schriften.py"]

ANFANG = '<main class="deck" id="deck" aria-live="polite">'
ENDE   = '    <footer class="foot">'

FOLIEN = '''

    <!-- Titelfolie — Tagung, Titel, Autor:innen, Einrichtung ..........
         Alles hier ist Platzhalter: eyebrow, h1, lead, byline. -->
    <section class="slide hero" data-title="Titel">
      <p class="eyebrow" data-anim>Tagung · Ort · Jahr</p>
      <h1 data-anim>{titel}</h1>
      <p class="lead" data-anim>Untertitel oder die Frage, um die es geht — ein Satz.</p>
      <div class="byline" data-anim>
        <p class="authors"><b>Vorname Nachname</b> · Mitautor:in · Mitautor:in</p>
        <p class="affil">Einrichtung · Institut</p>
      </div>
      <div class="logo logo-lg" data-anim>
        <svg viewBox="0 0 361.36 98" role="img" aria-label="RWTH Aachen University"><use href="#logo-rwth"/></svg>
      </div>
      <aside class="notes">Begrüßen, Thema in einem Satz einordnen, sagen, worauf der Vortrag hinausläuft.</aside>
    </section>

    <!-- Erste Inhaltsfolie — Muster. Weitere Folien: diesen Block kopieren
         oder eine Folie aus vorlage.html als ganze section hierher kopieren
         (Katalog in Darstellungsformen.md, Übersicht dort mit Taste 0). -->
    <section class="slide" data-title="Erste Folie">
      <p class="eyebrow" data-anim>Abschnitt</p>
      <h2 data-anim>Titel der ersten Folie</h2>
      <ul class="points" data-anim>
        <li>Erster Punkt — steht sofort da.</li>
        <li data-step="1">Zweiter Punkt — erscheint beim ersten Pfeildruck.</li>
        <li data-step="2">Dritter Punkt — beim zweiten.
          <ul><li>Unterpunkt, zweite Ebene.</li></ul>
        </li>
      </ul>
      <aside class="notes">Sprechnotiz — nur in der Vortragendenansicht (Taste P) zu sehen.</aside>
    </section>

    <!-- Dankfolie — Kontakt, bleibt in der Diskussion stehen ........... -->
    <section class="slide hero" data-title="Vielen Dank">
      <p class="eyebrow" data-anim>Tagung · Ort · Jahr</p>
      <h1 data-anim>Vielen Dank</h1>
      <p class="lead" data-anim>Ich freue mich auf Ihre Fragen und Anmerkungen.</p>
      <div class="byline" data-anim>
        <p class="authors"><b>Vorname Nachname</b></p>
        <p class="affil">Einrichtung · Institut<br>vorname.nachname@rwth-aachen.de</p>
      </div>
      <div class="logo logo-lg" data-anim>
        <svg viewBox="0 0 361.36 98" role="img" aria-label="RWTH Aachen University"><use href="#logo-rwth"/></svg>
      </div>
      <aside class="notes">Kontakt stehen lassen. Zeit für Fragen im Blick behalten.</aside>
    </section>

    <!-- Anhangsfolien (für die Fragerunde) kommen hierher, als
         section class="slide anhang" — Muster in vorlage.html ganz unten. -->

'''

FUSS_ALT = re.compile(r'<p class="foot-meta">[^<]*</p>')
FUSS_NEU = '<p class="foot-meta">Vorname Nachname · Tagung Ort Jahr</p>'
GITIGNORE = ".DS_Store\n.claude/\n*.pdf\nwerkzeuge/geholt/\n"


def slug(name):
    t = name.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "vortrag"


def vortrag_bauen(titel):
    s = VORLAGE.read_text(encoding="utf-8")
    a, b = s.index(ANFANG) + len(ANFANG), s.index(ENDE)
    s = s[:a] + FOLIEN.replace("{titel}", titel) + s[b:]
    s = s.replace("<title>Registerdeck</title>", "<title>%s</title>" % titel, 1)
    s, n = FUSS_ALT.subn(FUSS_NEU, s, count=1)
    if n != 1:
        sys.exit("Abbruch: Fußzeile (foot-meta) nicht gefunden.")
    s = s.replace("<body>\n", "<body>\n<!-- Erzeugt mit neu.py aus vorlage.html am %s. Unterbau unverändert;\n"
                  "     weitere Folien aus vorlage.html hierher kopieren. -->\n" % datetime.date.today().isoformat(), 1)
    folien = len(re.findall(r'<section class="slide', s[s.index("<main"):]))
    aussen = re.findall(r'(?:src|href)\s*=\s*["\'](https?:|//)', s) + re.findall(r'url\(\s*["\']?(?:https?:|//)', s)
    if folien != 3 or aussen:
        sys.exit("Abbruch, nichts geschrieben: %d Folien, äußere Verweise: %s" % (folien, aussen[:3]))
    return s


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    ordner = pathlib.Path(args[0]).resolve()
    titel = args[1] if len(args) > 1 else "Titel des Vortrags"
    ueber = "--ueberschreiben" in sys.argv
    name = None
    if "--datei" in sys.argv:
        name = sys.argv[sys.argv.index("--datei") + 1]
        if not name.lower().endswith(".html"):
            sys.exit("Abbruch: --datei muss auf .html enden.")
    else:
        name = slug(ordner.name) + ".html"
    datei = ordner / name

    ordner.mkdir(parents=True, exist_ok=True)
    ziele = [datei, ordner / "vorlage.html", ordner / "Darstellungsformen.md", ordner / "CLAUDE.md"] + \
            [ordner / "werkzeuge" / w for w in MITNEHMEN]
    da = [z for z in ziele if z.exists()]
    if da and not ueber:
        sys.exit("Abbruch: schon vorhanden: %s — --ueberschreiben erzwingt es." % ", ".join(str(z.relative_to(ordner)) for z in da))

    datei.write_text(vortrag_bauen(titel), encoding="utf-8")
    shutil.copy2(VORLAGE, ordner / "vorlage.html")
    shutil.copy2(WURZEL / "Darstellungsformen.md", ordner / "Darstellungsformen.md")
    (ordner / "werkzeuge").mkdir(exist_ok=True)
    for w in MITNEHMEN:
        shutil.copy2(HIER / w, ordner / "werkzeuge" / w)
    (ordner / "bilder").mkdir(exist_ok=True)
    anweisung = (HIER / "vortrag-CLAUDE.md").read_text(encoding="utf-8")
    (ordner / "CLAUDE.md").write_text(anweisung.replace("{datei}", name).replace("{datum}", datetime.date.today().isoformat()), encoding="utf-8")
    gi = ordner / ".gitignore"
    if not gi.exists():
        gi.write_text(GITIGNORE, encoding="utf-8")

    print("  %s/" % ordner)
    print("    %-24s der Vortrag: Titel, erste Folie, Dank (%.2f MB)" % (name, datei.stat().st_size / 1048576))
    print("    %-24s Musterbogen zum Kopieren — nicht vortragen" % "vorlage.html")
    print("    %-24s Katalog der Formen" % "Darstellungsformen.md")
    print("    %-24s Arbeitsanweisung für diesen Vortrag" % "CLAUDE.md")
    print("    %-24s %s" % ("werkzeuge/", ", ".join(MITNEHMEN)))
    print("    %-24s für Bildquellen" % "bilder/")
    print("  Weiter: CLAUDE.md lesen, Kopf ausfüllen, Folien anlegen; dann")
    print("  python3 werkzeuge/formeln.py %s · python3 werkzeuge/pruefen.py %s · python3 werkzeuge/pdf.py %s" % (name, name, name))


if __name__ == "__main__":
    main()
