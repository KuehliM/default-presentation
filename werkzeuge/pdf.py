#!/usr/bin/env python3
"""PDF aus dem Foliensatz: eine Seite je Folie, Anhang eingeschlossen,
jede Folie fertig aufgebaut.

    python3 pdf.py                 # schreibt vorlage.pdf daneben
    python3 pdf.py Vortrag.pdf     # anderer Zielname

Wie es geht: Der Foliensatz kennt den Druckmodus `?druck=1`. Damit
stellt sein eigenes Skript jede Folie auf den letzten Schritt
(Einblendungen, Morph, Deckel, Hervorhebungen) und gibt jeder Folie
eine Kopie der Fusszeile mit ihrer Nummer. Das Stylesheet fuer den
Druck (@media print in vorlage.html) legt jede Folie als eigene Seite
1280 x 720 px an und blendet Register, Balken und Uebersicht aus.
Dieses Skript oeffnet die Datei so in einem unsichtbaren Chrome und
laesst ihn drucken. Von Hand geht dasselbe: `vorlage.html?druck=1`
im Browser oeffnen, Cmd/Strg+P, Raender „keine“, Hintergrundgrafiken an.

Braucht Google Chrome oder Chromium, sonst nichts.
"""

import pathlib
import re
import shutil
import subprocess
import sys

HIER  = pathlib.Path(__file__).parent
DATEI = HIER / "vorlage.html"

CHROME_ORTE = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]


def chrome():
    for ort in CHROME_ORTE:
        if ort and pathlib.Path(ort).exists():
            return ort
    sys.exit("Abbruch: kein Chrome oder Chromium gefunden.")


def main():
    ziel = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DATEI.with_suffix(".pdf")
    quelle = DATEI.read_text(encoding="utf-8")
    # Nur die Folien im Rumpf zaehlen — der Kopfkommentar zeigt eine als Beispiel.
    folien = len(re.findall(r'<section class="slide', quelle[quelle.index("<main"):]))
    r = subprocess.run(
        [chrome(), "--headless", "--disable-gpu", "--hide-scrollbars",
         "--no-pdf-header-footer",
         # Virtuelle Zeit: der Morph auf der Fall-Folie braucht 0,9 s, die
         # Auftrittsanimationen bis zu 1 s. Erst danach wird gedruckt.
         "--virtual-time-budget=6000",
         "--print-to-pdf=" + str(ziel),
         DATEI.as_uri() + "?druck=1"],
        capture_output=True, text=True)
    if r.returncode or not ziel.exists():
        sys.exit("Abbruch: Chrome hat kein PDF geschrieben.\n" + r.stderr[-600:])
    seiten = len(re.findall(rb"/Type\s*/Page[^s]", ziel.read_bytes()))
    print("  %s: %d Seiten, %.1f MB" % (ziel.name, seiten, ziel.stat().st_size / 1048576))
    if seiten != folien:
        sys.exit("Abbruch: %d Folien, aber %d Seiten — Seitenumbrueche pruefen." % (folien, seiten))
    print("  Eine Seite je Folie, Anhang eingeschlossen, alle Schritte aufgebaut.")


if __name__ == "__main__":
    main()
