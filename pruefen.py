#!/usr/bin/env python3
"""Foliensatz vermessen: Überlauf, Füllstand, kleinste Schrift.

Statt zu schätzen, ob ein Text noch auf eine Folie passt, wird die Datei
in einem unsichtbaren Browser geöffnet und jede Folie ausgemessen. Der
Bericht sagt für jede Folie:

  unten       Unterkante des Inhalts in Bühnenkoordinaten (von 720)
  Überlauf    wie weit der Inhalt in den Fußzeilenstreifen ragt (soll 0 sein)
  Füllstand   wie viel der nutzbaren Höhe belegt ist
  kl. Schrift kleinster Schriftgrad im Fließtext und in Grafiken

Gemessen wird der **vollständig aufgebaute** Zustand: Elemente mit
data-step sind zwar unsichtbar, belegen ihren Platz aber weiterhin.

    python3 pruefen.py                 # vorlage.html
    python3 pruefen.py anleitung.html
    python3 pruefen.py --json          # maschinenlesbar
"""

import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

CHROME_ORTE = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]

SONDE = r"""
<script>
window.addEventListener('load', () => setTimeout(() => {
  const root = document.documentElement;

  const zahl = n => parseFloat(getComputedStyle(root).getPropertyValue(n));
  const W = zahl('--stage-w'), H = zahl('--stage-h');

  const deck = document.getElementById('deck');
  const skala = deck.getBoundingClientRect().width / W;

  const bericht = [...deck.querySelectorAll('.slide')].map((s, i) => {
    /* Die Grenzen kommen aus der Folie selbst. Damit gilt fuer die
       Titel- und Dankfolie automatisch ihr eigener, kleinerer unterer
       Rand — dort ist die Fusszeile ausgeblendet. */
    const cs = getComputedStyle(s);
    const pl = parseFloat(cs.paddingLeft),  pr = parseFloat(cs.paddingRight);
    const pt = parseFloat(cs.paddingTop),   pb = parseFloat(cs.paddingBottom);
    const grenze = H - pb;

    /* Gemessen wird gegen die Folie selbst, nicht gegen die Buehne.
       Dadurch kuerzen sich beide Transformationen heraus: der Massstab
       der Buehne und die Uebergangslage nicht aktiver Folien
       (translateX(76px) scale(.972)). */
    const sr = s.getBoundingClientRect();
    const eig = sr.width / W;
    const px = v => Math.round(v / eig);

    const kinder = [...s.children].filter(k => k.tagName !== 'ASIDE');
    let oben = Infinity, unten = -Infinity, links = Infinity, rechts = -Infinity;
    for (const k of kinder) {
      const r = k.getBoundingClientRect();
      oben   = Math.min(oben,   px(r.top    - sr.top));
      unten  = Math.max(unten,  px(r.bottom - sr.top));
      links  = Math.min(links,  px(r.left   - sr.left));
      rechts = Math.max(rechts, px(r.right  - sr.left));
    }

    /* Kleinste Schrift, getrennt nach Fliesstext und Grafik. Reine
       Auszeichnungen wie Augenbraue oder Bildunterschrift sind bewusst
       klein und zaehlen nicht als Fliesstext. */
    const AUSZEICHNUNG = '.eyebrow, .caption, .source-note, .foot-meta, .demo-note';
    let minText = Infinity, woText = '', minSvg = Infinity;
    for (const el of s.querySelectorAll('*')) {
      if (el.closest('aside')) continue;
      if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
      const fs = parseFloat(getComputedStyle(el).fontSize) / eig;
      if (!fs) continue;
      if (el.closest('svg')) { minSvg = Math.min(minSvg, fs); continue; }
      if (el.closest(AUSZEICHNUNG)) continue;   /* bewusst klein gesetzt */
      if (fs < minText) {
        minText = fs;
        woText = el.getAttribute('class') || el.tagName.toLowerCase();
      }
    }

    const schritte = [...s.querySelectorAll('[data-step]')].map(e => +e.dataset.step || 0);

    return {
      nr: i + 1,
      titel: s.dataset.title || '',
      hero: s.classList.contains('hero'),
      oben, unten, links, rechts,
      grenze: Math.round(grenze),
      randLinks: Math.round(pl), randRechts: Math.round(W - pr),
      ueberlauf: Math.max(0, unten - Math.round(grenze)),
      randVerletzt: links < Math.round(pl) - 1 || rechts > Math.round(W - pr) + 1,
      fuellstand: Math.round((unten - oben) / (grenze - oben) * 100),
      platzUebrig: Math.round(grenze) - unten,
      schritte: schritte.length ? Math.max(...schritte) : 0,
      notizen: !!s.querySelector('.notes'),
      minText: isFinite(minText) ? +minText.toFixed(1) : null,
      minTextWo: woText,
      minSvg: isFinite(minSvg) ? +minSvg.toFixed(1) : null,
    };
  });

  const daten = { skala: +skala.toFixed(3), hoehe: H, breite: W, folien: bericht };
  document.documentElement.innerHTML =
    '<head></head><body><pre id="bericht">' + JSON.stringify(daten) + '</pre></body>';
}, 900));
</script>
"""


def chrome():
    for ort in CHROME_ORTE:
        if ort and pathlib.Path(ort).exists():
            return ort
    sys.exit("Abbruch: Kein Chrome oder Chromium gefunden.")


def messen(datei: pathlib.Path):
    quelle = datei.read_text(encoding="utf-8")
    if "</body>" not in quelle:
        sys.exit(f"Abbruch: {datei.name} hat kein </body>.")
    with tempfile.TemporaryDirectory() as tmp:
        probe = pathlib.Path(tmp) / datei.name
        probe.write_text(quelle.replace("</body>", SONDE + "</body>"), encoding="utf-8")
        roh = subprocess.run(
            [chrome(), "--headless", "--disable-gpu", "--hide-scrollbars",
             "--window-size=1280,720", "--virtual-time-budget=8000",
             "--dump-dom", probe.as_uri()],
            capture_output=True, text=True, timeout=120).stdout
    treffer = re.search(r'<pre id="bericht">(.*?)</pre>', roh, re.S)
    if not treffer:
        sys.exit("Abbruch: Die Sonde hat keinen Bericht geliefert.")
    return json.loads(treffer.group(1))


def ausgeben(daten, datei):
    f = daten["folien"]
    print(f"\n{datei.name} — {len(f)} Folien, Bühne "
          f"{daten['breite']:.0f}×{daten['hoehe']:.0f}\n")
    kopf = (f"{'Nr':>3}  {'Titel':22} {'Schr':>4} {'unten':>6} {'Grenze':>7} "
            f"{'frei':>5} {'Füll':>5}  {'Text':>5} {'SVG':>5}  Notiz")
    print(kopf); print("─" * len(kopf))
    for s in f:
        warn = "!" if s["ueberlauf"] or s["randVerletzt"] else " "
        print(f"{s['nr']:>3}{warn} {s['titel'][:22]:22} {s['schritte']:>4} "
              f"{s['unten']:>6} {s['grenze']:>7} {s['platzUebrig']:>5} "
              f"{str(s['fuellstand'])+'%':>5}  "
              f"{s['minText'] or '–':>5} {s['minSvg'] or '–':>5}  "
              f"{'ja' if s['notizen'] else '—'}")

    probleme = [s for s in f if s["ueberlauf"] or s["randVerletzt"]]
    knapp    = [s for s in f if not s["ueberlauf"] and s["fuellstand"] > 92]
    klein    = [s for s in f if s["minText"] and s["minText"] < 15]
    ohne     = [s for s in f if not s["notizen"] and not s["hero"]]

    print()
    if probleme:
        for s in probleme:
            grund = []
            if s["ueberlauf"]:
                grund.append(f"ragt {s['ueberlauf']} px in den Fußzeilenstreifen")
            if s["randVerletzt"]:
                grund.append("verletzt den seitlichen Satzspiegel")
            print(f"  FEHLER  Folie {s['nr']} ({s['titel']}): {', '.join(grund)}")
    else:
        print("  Kein Überlauf, kein Folientext über der Fußzeile.")
    if knapp:
        print("  eng    " + ", ".join(f"Folie {s['nr']} ({s['fuellstand']}%)" for s in knapp))
    if klein:
        print("  klein  " + ", ".join(f"Folie {s['nr']}: {s['minText']} px in .{s['minTextWo']}" for s in klein))
    if ohne:
        print("  ohne Notizen: " + ", ".join(str(s["nr"]) for s in ohne))
    print()
    return 1 if probleme else 0


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    datei = pathlib.Path(__file__).parent / (args[0] if args else "vorlage.html")
    if not datei.exists():
        sys.exit(f"Abbruch: {datei} gibt es nicht.")
    daten = messen(datei)
    if "--json" in sys.argv:
        print(json.dumps(daten, indent=2, ensure_ascii=False))
        return 0
    return ausgeben(daten, datei)


if __name__ == "__main__":
    sys.exit(main())
