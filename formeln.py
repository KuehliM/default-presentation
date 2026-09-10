#!/usr/bin/env python3
"""Formeln setzen: LaTeX im Quelltext, MathML in der Folie.

Im Foliensatz steht die Formel als LaTeX in einem Attribut:

    <span class="tex" data-tex="T = 2\\pi\\sqrt{\\frac{l}{g}}"></span>

Dieses Skript füllt jeden solchen Kasten mit dem passenden MathML
(erzeugt von Temml) und bettet die Mathe-Schrift ein. Das Attribut
bleibt stehen — es ist die Quelle, das MathML ist das Erzeugnis.
Formel ändern heißt: Attribut ändern, Skript laufen lassen.

Gesetzt wird damit vom Browser selbst, nicht von einer Bibliothek.
Die fertige Folie braucht kein JavaScript.

**Bedingung, die alles bestimmt:** Die fertige Datei stellt keine
Anfrage nach außen. Auf Tagungen steht selten der eigene Rechner auf
dem Pult. Schrift als base64, keine URL bleibt übrig; das Skript
prüft es nach jedem Lauf.

    python3 formeln.py            # setzt alle Formeln neu
    python3 formeln.py --pruefen  # nur zeigen, was zu tun wäre

Warum Fira Math: Es ist die Mathe-Schwester von Fira Sans, also
dieselbe Handschrift. Und sie bringt die echten kursiven Glyphen aus
dem Unicode-Block „Mathematical Alphanumeric Symbols" mit. Der
Browser tauscht die Zeichen dorthin (`text-transform: math-auto`) —
nachgemessen, auf 0,01 px deckungsgleich. Ein `<i>` dagegen hätte nur
die aufrechte Form schräg gestellt, weil die Datei keinen kursiven
Schnitt enthält.
"""

import base64
import html
import json
import pathlib
import re
import shutil
import subprocess
import sys

HIER     = pathlib.Path(__file__).parent
DATEIEN  = ["vorlage.html"]
WERKZEUG = HIER / "werkzeug"          # nicht im Repository, wird bei Bedarf geholt
FIRA_MATH_URL = ("https://github.com/firamath/firamath/releases/download/"
                 "v0.3.4/FiraMath-Regular.otf")
GRAD = "26px"     # Grundgrad. Nicht kleiner: doppelt Tiefgestelltes ist die
                  # Hälfte davon und fiele sonst unter die 15-px-Lesegrenze.


# ── Werkzeug ───────────────────────────────────────────────────────

def werkzeug_holen():
    WERKZEUG.mkdir(exist_ok=True)
    if not (WERKZEUG / "node_modules" / "temml").exists():
        print("  hole Temml …")
        if not shutil.which("npm"):
            sys.exit("Abbruch: npm wird gebraucht, um Temml zu holen.")
        subprocess.run(["npm", "init", "-y"], cwd=WERKZEUG, capture_output=True)
        r = subprocess.run(["npm", "install", "temml", "--no-audit", "--no-fund"],
                           cwd=WERKZEUG, capture_output=True, text=True)
        if r.returncode:
            sys.exit("Abbruch: npm install fehlgeschlagen.\n" + r.stderr[-800:])
    if not (WERKZEUG / "FiraMath-Regular.otf").exists():
        print("  hole Fira Math …")
        r = subprocess.run(["curl", "-sfL", "-o", str(WERKZEUG / "FiraMath-Regular.otf"),
                            FIRA_MATH_URL], capture_output=True)
        if r.returncode or not (WERKZEUG / "FiraMath-Regular.otf").exists():
            sys.exit("Abbruch: Fira Math nicht geladen (" + FIRA_MATH_URL + ").")


def setzen(formeln):
    """LaTeX in MathML übersetzen — einmal beim Bauen, nicht beim Vortrag."""
    if not formeln:
        return []
    skript = """
      const temml = require('temml');
      console.log(JSON.stringify(JSON.parse(process.argv[1]).map(t =>
        temml.renderToString(t, { xml: true, trust: true }))));
    """
    r = subprocess.run(["node", "-e", skript, json.dumps(formeln)],
                       cwd=WERKZEUG, capture_output=True, text=True)
    if r.returncode:
        sys.exit("Abbruch: Temml fehlgeschlagen.\n" + r.stderr[-800:])
    fertig = json.loads(r.stdout)
    for tex, mml in zip(formeln, fertig):
        if "temml-error" in mml:
            sys.exit("Abbruch: Temml kommt mit dieser Formel nicht zurecht:\n    " + tex)
    return fertig


def schrift():
    """OTF nach WOFF wandeln — spart ein Drittel und braucht kein brotli."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        sys.exit("Abbruch: fontTools wird gebraucht (pip install fonttools).")
    otf  = WERKZEUG / "FiraMath-Regular.otf"
    woff = WERKZEUG / "FiraMath-Regular.woff"
    if not woff.exists() or woff.stat().st_mtime < otf.stat().st_mtime:
        f = TTFont(otf)
        if "MATH" not in f:
            sys.exit("Abbruch: der Schrift fehlt die MATH-Tabelle, MathML bliebe unbrauchbar.")
        f.flavor = "woff"
        f.save(woff)
    return base64.b64encode(woff.read_bytes()).decode()


# ── Blöcke ─────────────────────────────────────────────────────────

def stilblock():
    return f'''<style id="stil-formelsatz">
/* Formelsatz: MathML, gesetzt vom Browser anhand der MATH-Tabelle
   der Schrift. Erzeugt von formeln.py — nicht von Hand ändern.
   Der Block steht bewusst getrennt vom Haupt-Stylesheet: jenes
   erkennt technik-uebernehmen.py daran, dass sein Anfangszeichen
   kein Attribut trägt. Dieses hier hat eins. */
@font-face{{
  font-family:'Fira Math'; font-style:normal; font-weight:400; font-display:block;
  src:url(data:font/woff;base64,{schrift()}) format('woff');
}}
math{{ font-family:'Fira Math', math }}
.tex{{ display:inline-block }}
.keys dd .tex math,
.formeln dd math{{ font-size:{GRAD}; line-height:1.5 }}
.herleit math{{ font-size:23px }}
/* In der Begründungsspalte gilt deren eigener Grad, nicht der der
   Formelspalte — sonst überragt eine Nebenbemerkung die Herleitung. */
.herleit .grund math{{ font-size:1em }}
ul.points li math{{ font-size:20px }}
</style>'''


def block_setzen(text, name, inhalt, anker):
    auf, zu = "<!-- %s: Anfang -->" % name, "<!-- %s: Ende -->" % name
    neu = auf + "\n" + inhalt + "\n" + zu
    muster = re.compile(re.escape(auf) + ".*?" + re.escape(zu), re.S)
    if muster.search(text):
        return muster.sub(lambda m: neu, text, count=1)
    if text.count(anker) != 1:
        sys.exit("Abbruch: Anker für %s kommt %d× vor, erwartet 1×." % (name, text.count(anker)))
    return text.replace(anker, neu + "\n" + anker, 1)


# ── Hauptlauf ──────────────────────────────────────────────────────

KASTEN = re.compile(r'(<span class="tex" data-tex="([^"]*)"[^>]*>)(.*?)(</span>)', re.S)


def main():
    nur_pruefen = "--pruefen" in sys.argv
    werkzeug_holen()
    gesamt = 0

    for name in DATEIEN:
        p = HIER / name
        s = p.read_text(encoding="utf-8")
        kaesten = KASTEN.findall(s)
        if not kaesten:
            print("  %-16s keine Formeln" % name)
            continue

        tex = [html.unescape(k[1]) for k in kaesten]
        if nur_pruefen:
            print("  %-16s %d Formeln" % (name, len(tex)))
            gesamt += len(tex)
            continue

        fertig = setzen(tex)
        i = iter(fertig)
        s = KASTEN.sub(lambda m: m.group(1) + next(i) + m.group(4), s)
        s = block_setzen(s, "FORMELSATZ", stilblock(), "</head>")

        aussen = re.findall(r'(?:src|href)\s*=\s*["\'](https?:|//)', s) + \
                 re.findall(r'url\(\s*["\']?(?:https?:|//)', s)
        if aussen:
            sys.exit("Abbruch, nichts geschrieben: äußere Verweise gefunden: %s" % aussen[:3])
        p.write_text(s, encoding="utf-8")
        print("  %-16s %d Formeln gesetzt, %.2f MB" % (name, len(tex), len(s) / 1048576))
        gesamt += len(tex)

    print("  %d Formeln insgesamt." % gesamt)
    if not nur_pruefen:
        print("  Keine äußeren Verweise: läuft ohne Netz und auf fremden Rechnern.")


if __name__ == "__main__":
    main()
