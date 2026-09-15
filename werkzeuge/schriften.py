#!/usr/bin/env python3
"""Schriften einbetten: Fira Sans und Fira Mono als Teilsatz in der Datei.

Der Foliensatz trägt seine Textschriften als Base64 in sechs
@font-face-Blöcken. Bis zum 11.09.2026 stammten sie von Google Fonts
und enthielten nur Latein — kein Δ, kein π, kein →. Griechische und
mathematische Zeichen außerhalb einer Formel holte `.gr` aus der
Systemschrift, je nach Rechner eine andere.

Dieses Skript schneidet den Teilsatz selbst: aus der vollständigen
Fira (dieselbe Ausgabe 4.203 wie bisher, also dieselben Maße) mit
Latein, Griechisch, Pfeilen und Rechenzeichen. Was die Schrift nicht
hat, gehört in eine Formel (`data-tex`) — Fira Math kennt alles.

    python3 schriften.py            # bettet alle sechs Schnitte neu ein
    python3 schriften.py Vortraege/x/x.html --pruefen   # anderer Vortrag
    python3 schriften.py --pruefen  # welche Zeichen des Foliensatzes
                                    # fallen noch aus der Schrift?

**Bedingung, die alles bestimmt:** Die fertige Datei stellt keine
Anfrage nach außen. Netz braucht nur dieses Skript, einmal, um die
Schriftdateien nach `werkzeug/` zu holen. Das Erzeugnis läuft offline.

Braucht fontTools und brotli (WOFF2 ist Brotli-komprimiert):
    pip install fonttools brotli
"""

import base64
import io
import logging
import pathlib
import re
import subprocess
import sys

HIER     = pathlib.Path(__file__).parent          # werkzeuge/
WURZEL = HIER.parent                        # der Ordner mit der Vorlage bzw. dem Vortrag
WERKZEUG = HIER / "geholt"            # nicht im Repository, wird bei Bedarf geholt
QUELLE   = "https://github.com/google/fonts/raw/main/ofl/%s/%s.ttf"
VERSION  = {"Fira Sans": "Version 4.203", "Fira Mono": "Version 3.206"}

# Familie, Gewicht, Ordner und Datei bei Google Fonts.
SCHNITTE = [
    ("Fira Sans", 300, "firasans", "FiraSans-Light"),
    ("Fira Sans", 400, "firasans", "FiraSans-Regular"),
    ("Fira Sans", 500, "firasans", "FiraSans-Medium"),
    ("Fira Sans", 700, "firasans", "FiraSans-Bold"),
    ("Fira Mono", 400, "firamono", "FiraMono-Regular"),
    ("Fira Mono", 700, "firamono", "FiraMono-Bold"),
]

# Was eingebettet wird. Bereiche, die die Schrift nicht kennt, bleiben
# still leer — kosten also nichts. Kyrillisch ist bewusst nicht dabei
# (+11 KB je Schnitt, nie gebraucht).
BEREICHE = [
    ("U+0000-017F", "Latein mit Umlauten und Latin Extended-A: Č Ł ő ş ğ"),
    ("U+0218-021B", "ș ț (Rumänisch)"),
    ("U+1E9E",      "ẞ"),
    ("U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0300-036F", "Akzente, auch kombinierend"),
    ("U+0370-03FF", "Griechisch: Δ π σ α β θ ω φ"),
    ("U+2000-206F", "Satzzeichen: – — … „ “ ‰ ′ ″"),
    ("U+2070-209F", "Hoch- und Tiefgestelltes: ⁿ ₀ ₁ ₂"),
    ("U+20A0-20CF", "Währungen: €"),
    ("U+2100-214F", "Buchstabenähnliches: ℓ ™ Ω"),
    ("U+2150-218F", "Brüche und Zahlzeichen: ⅓ ⅔ ⅛"),
    ("U+2190-21FF", "Pfeile: ← → ↔ ↑ ↓"),
    ("U+2200-22FF", "Rechenzeichen: √ ≈ ≤ ≥ ≠ ∞ ∑ ∫ ∂ ± ×"),
    ("U+2300-23FF", "Technisches"),
    ("U+25A0-25FF", "Geometrische Formen"),
    ("U+FB00-FB06", "Ligaturen fi fl"),
    ("U+FEFF,U+FFFD", "Byte-Order-Mark, Ersatzzeichen"),
]

# Layout-Merkmale. tnum trägt `font-variant-numeric: tabular-nums`,
# das die Kennzahlen und Tabellen nutzen. sups/subs/zero/onum/lnum
# sind billig (3 KB je Schnitt) und stehen für Einzelfälle bereit.
MERKMALE = ["calt", "ccmp", "dnom", "frac", "liga", "locl", "numr", "pnum", "tnum",
            "kern", "mark", "mkmk", "zero", "sups", "subs", "onum", "lnum", "case"]

BLOCK = re.compile(
    r"(@font-face \{\s*font-family: '(Fira Sans|Fira Mono)';\s*font-style: normal;\s*"
    r"font-weight: (\d+);\s*font-display: block;\s*src: url\(data:font/woff2;base64,)"
    r"([A-Za-z0-9+/=]+)(\) format\('woff2'\);)")


# ── Werkzeug ───────────────────────────────────────────────────────

def werkzeug_holen():
    try:
        import brotli  # noqa: F401  — fontTools braucht es für WOFF2
        from fontTools import subset  # noqa: F401
    except ImportError as e:
        sys.exit("Abbruch: %s fehlt (pip install fonttools brotli)." % e.name)
    WERKZEUG.mkdir(exist_ok=True)
    for _, _, ordner, datei in SCHNITTE:
        ziel = WERKZEUG / (datei + ".ttf")
        if ziel.exists():
            continue
        url = QUELLE % (ordner, datei)
        print("  hole %s …" % datei)
        r = subprocess.run(["curl", "-sfL", "-o", str(ziel), url], capture_output=True)
        if r.returncode or not ziel.exists():
            sys.exit("Abbruch: %s nicht geladen (%s)." % (datei, url))


def teilsatz(familie, datei):
    """TTF lesen, auf die Bereiche beschneiden, als WOFF2 zurückgeben."""
    from fontTools.ttLib import TTFont
    from fontTools import subset
    # fontTools moniert beim Schreiben ein OS/2-Bit, das Fira selbst so setzt.
    logging.getLogger("fontTools").setLevel(logging.ERROR)
    # recalcTimestamp=False: sonst schreibt jeder Lauf ein neues Datum in
    # die Schrift und die Datei ändert sich, ohne dass sich etwas ändert.
    f = TTFont(WERKZEUG / (datei + ".ttf"), recalcTimestamp=False)
    version = f["name"].getDebugName(5)
    if not version.startswith(VERSION[familie]):
        sys.exit("Abbruch: %s ist %s, erwartet %s — andere Maße, anderes Layout."
                 % (datei, version, VERSION[familie]))
    opt = subset.Options()
    opt.layout_features = MERKMALE
    opt.hinting = False            # Google liefert ohne; spart zwei Drittel
    opt.notdef_outline = True
    ss = subset.Subsetter(opt)
    ss.populate(unicodes=subset.parse_unicodes(",".join(b for b, _ in BEREICHE)))
    ss.subset(f)
    f.flavor = "woff2"
    puffer = io.BytesIO()
    f.save(puffer)
    return puffer.getvalue(), len(f.getBestCmap())


# ── Prüfen ─────────────────────────────────────────────────────────

def eingebettete_zeichen(text):
    """Welche Zeichen kennt die eingebettete Fira Sans 400?"""
    from fontTools.ttLib import TTFont
    for m in BLOCK.finditer(text):
        if m.group(2) == "Fira Sans" and m.group(3) == "400":
            f = TTFont(io.BytesIO(base64.b64decode(m.group(4))))
            return set(f.getBestCmap())
    sys.exit("Abbruch: Fira Sans 400 nicht gefunden.")


def fehlende_zeichen(text):
    """Zeichen im Folientext, die nicht aus der eingebetteten Schrift kommen.

    Formeln (MathML) zählen nicht — dort setzt Fira Math. Ebenso wenig
    Base64, Kommentare und Auszeichnung."""
    kennt = eingebettete_zeichen(text)
    t = re.sub(r"data:font/[a-z0-9]+;base64,[A-Za-z0-9+/=]+", "", text)
    t = re.sub(r"<math\b.*?</math>", "", t, flags=re.S)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"/\*.*?\*/", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", "", t)
    fehlt = {}
    for ch in t:
        if ord(ch) > 0x7F and ord(ch) not in kennt and not ch.isspace():
            fehlt[ch] = fehlt.get(ch, 0) + 1
    return fehlt


def datei_aus(args, standard="vorlage.html"):
    """Pfad aus dem Aufruf: erst wie angegeben (relativ zum Arbeitsverzeichnis),
    sonst im Ordner über den Werkzeugen. Ohne Angabe die Vorlage."""
    name = args[0] if args else standard
    p = pathlib.Path(name)
    if not p.exists() and not p.is_absolute() and (WURZEL / name).exists():
        p = WURZEL / name
    if not p.exists():
        sys.exit("Abbruch: %s gibt es nicht." % p)
    return p.resolve()          # absolut: Chrome braucht eine file-URI


# ── Hauptlauf ──────────────────────────────────────────────────────

def main():
    nur_pruefen = "--pruefen" in sys.argv
    DATEI = datei_aus([a for a in sys.argv[1:] if not a.startswith("--")])
    text = DATEI.read_text(encoding="utf-8")
    bloecke = BLOCK.findall(text)
    if len(bloecke) != len(SCHNITTE):
        sys.exit("Abbruch: %d Schriftblöcke gefunden, erwartet %d." % (len(bloecke), len(SCHNITTE)))

    if nur_pruefen:
        werkzeug_holen()
        fehlt = fehlende_zeichen(text)
        if fehlt:
            print("  Zeichen außerhalb von Formeln, die die Schrift nicht hat:")
            for ch, n in sorted(fehlt.items(), key=lambda t: -t[1]):
                print("    U+%04X  %s  %d×" % (ord(ch), ch, n))
            print("  Abhilfe: in eine Formel setzen (data-tex), dort trägt Fira Math.")
            sys.exit(1)
        print("  Jedes Zeichen außerhalb von Formeln kommt aus der eingebetteten Schrift.")
        return

    werkzeug_holen()
    neu = {}
    for familie, gewicht, _, datei in SCHNITTE:
        woff2, n = teilsatz(familie, datei)
        neu[(familie, str(gewicht))] = base64.b64encode(woff2).decode()
        print("  %-10s %d  %3d KB  %4d Zeichen" % (familie, gewicht, len(woff2) // 1024, n))

    def ersetzen(m):
        return m.group(1) + neu[(m.group(2), m.group(3))] + m.group(5)
    text, anzahl = BLOCK.subn(ersetzen, text)
    if anzahl != len(SCHNITTE):
        sys.exit("Abbruch, nichts geschrieben: %d Blöcke ersetzt." % anzahl)

    aussen = re.findall(r'(?:src|href)\s*=\s*["\'](https?:|//)', text) + \
             re.findall(r'url\(\s*["\']?(?:https?:|//)', text)
    if aussen:
        sys.exit("Abbruch, nichts geschrieben: äußere Verweise gefunden: %s" % aussen[:3])
    DATEI.write_text(text, encoding="utf-8")
    print("  %s: %.2f MB" % (DATEI.name, len(text) / 1048576))

    fehlt = fehlende_zeichen(text)
    if fehlt:
        print("  Fällt weiterhin aus der Schrift: " + " ".join(fehlt))
    print("  Keine äußeren Verweise: läuft ohne Netz und auf fremden Rechnern.")


if __name__ == "__main__":
    main()
