#!/usr/bin/env python3
"""Technik von vorlage.html nach anleitung.html übernehmen.

Beide Foliensätze teilen sich denselben Unterbau: das Stylesheet, das
Gerüst der Vortragendenansicht und das Skript. Nur die Folien und die
Sprechnotizen unterscheiden sich.

Damit nichts doppelt gepflegt werden muss, gilt `vorlage.html` als
Quelle. Dieses Skript kopiert die drei geteilten Blöcke hinüber und
lässt alles andere unangetastet:

    python3 technik-uebernehmen.py

Ändere also immer zuerst die Vorlage, dann dieses Skript laufen lassen.
"""

import pathlib
import re
import sys

QUELLE = pathlib.Path(__file__).parent / "vorlage.html"
ZIEL = pathlib.Path(__file__).parent / "anleitung.html"

# Was übernommen wird. Der Titel und die Folien bleiben jeweils eigen.
# Der dritte Wert ist der Anker: Fehlt der Block im Ziel noch, wird er
# unmittelbar davor eingesetzt.
BLOECKE = [
    ("Stylesheet", r"(?s)<style>.*?</style>", None),
    ("Vortragendenansicht", r'(?s)<!-- Vortragendenansicht.*?\n</div>', "<script>\n(() => {"),
    ("Skript", r"(?s)<script>\n\(\(\) => \{.*?</script>", None),
]


def block(text, muster, name, datei, pflicht=True):
    treffer = re.findall(muster, text)
    if len(treffer) > 1:
        sys.exit(f"Abbruch: {name} kommt in {datei} {len(treffer)}× vor, erwartet höchstens 1×.")
    if not treffer:
        if pflicht:
            sys.exit(f"Abbruch: {name} fehlt in {datei}.")
        return None
    return treffer[0]


def main():
    quelle = QUELLE.read_text(encoding="utf-8")
    ziel = ZIEL.read_text(encoding="utf-8")
    vorher = ziel

    for name, muster, anker in BLOECKE:
        neu = block(quelle, muster, name, QUELLE.name)
        alt = block(ziel, muster, name, ZIEL.name, pflicht=anker is None)
        if alt is None:
            if anker not in ziel:
                sys.exit(f"Abbruch: Anker {anker!r} für {name} nicht in {ZIEL.name} gefunden.")
            ziel = ziel.replace(anker, neu + "\n\n" + anker, 1)
            print(f"  {name}: neu eingesetzt ({len(neu)} Zeichen)")
        elif alt == neu:
            print(f"  {name}: unverändert")
        else:
            ziel = ziel.replace(alt, neu, 1)
            print(f"  {name}: übernommen ({len(alt)} → {len(neu)} Zeichen)")

    if ziel == vorher:
        print("Nichts zu tun.")
        return

    # Was eigen bleiben muss, VOR dem Schreiben prüfen. Ein zu weit
    # greifendes Muster würde sonst Titel oder Fußzeile der Anleitung
    # durch die der Vorlage ersetzen, ohne dass es auffällt.
    for probe, was in (("<title>Registerdeck Anleitung</title>", "der eigene <title>"),
                       ("Registerdeck · Anleitung", "die eigene Fußzeile")):
        if probe not in ziel:
            sys.exit(f"Abbruch, nichts geschrieben: {was} der Anleitung wäre verloren gegangen.\n"
                     f"Vermutlich greift eines der Muster in BLOECKE zu weit.")

    ZIEL.write_text(ziel, encoding="utf-8")
    print(f"{ZIEL.name} geschrieben.")


if __name__ == "__main__":
    main()
