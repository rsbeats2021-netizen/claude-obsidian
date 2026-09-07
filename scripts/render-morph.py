#!/usr/bin/env python3
"""A close copy of the doctor.morph slide design.

Built by reading his actual slides. His deck is the second highest performing
slideshow in the scrape, so this is worth copying precisely rather than
approximating.

What his design does, element by element:
  - pale blue-grey ground with a soft cloudy wash, not a flat fill
  - letterspaced brand line in caps at the very top
  - headline in heavy geometric caps with a black-to-blue gradient and a soft
    drop shadow
  - body in bold geometric sans, black, with individual terms in red or blue
  - a thin double-rule ornament with a diamond, separating head from body
  - 960x1280 (3:4), which is his actual canvas

Markers, same as render-v3:
  *term*   blue      **term**  red      _phrase_  underline   ==phrase==  highlight

Usage:
    python3 scripts/render-morph.py content/<deck>
    python3 scripts/render-morph.py content/<deck> --tone darker --brand "YOURNAME"
"""
import argparse
import csv
import glob
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SIZES = {"3:4": (960, 1280), "4:5": (1080, 1350), "9:16": (1080, 1920)}

# His ground is a pale blue-grey wash. 'darker' and 'dark' step it down for
# people who find the original too close to white.
TONES = {
    "original": ("#EAF0F3", "#DCE6EB", "#F2F6F8"),
    "darker":   ("#D2DAE0", "#BFCBD4", "#DBE2E7"),
    "dark":     ("#B8C4CC", "#A5B4BE", "#C6D0D7"),
}

TPL = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
 *{{margin:0;padding:0;box-sizing:border-box}}
 html,body{{width:{W}px;height:{H}px;}}
 body{{background:
    radial-gradient(120% 80% at 78% 8%, {wash2} 0%, transparent 55%),
    radial-gradient(100% 70% at 12% 92%, {wash3} 0%, transparent 60%),
    {bg};}}
 .wrap{{position:absolute;inset:0;padding:{padtop}px 46px 54px;
        display:flex;flex-direction:column;align-items:center;text-align:center;}}
 .body{{flex:1;display:flex;flex-direction:column;align-items:center;
        justify-content:center;width:100%;}}
 .brand{{font-family:Poppins,sans-serif;font-weight:800;font-size:{brandsize}px;
        letter-spacing:{brandls}px;color:#12183A;margin-bottom:{brandgap}px;}}
 .headline{{font-family:Poppins,sans-serif;font-weight:900;font-size:{hsize}px;
        line-height:1.02;letter-spacing:-0.5px;text-transform:uppercase;
        background:linear-gradient(96deg,#080A14 12%,#1B2AA8 58%,#2438E8 100%);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        filter:drop-shadow(0 5px 7px rgba(20,30,80,0.30));}}
 .divider{{width:76%;margin:{divgap}px auto 0;display:flex;align-items:center;
        justify-content:center;gap:12px;}}
 .divider .ln{{flex:1;height:3px;background:linear-gradient(90deg,transparent,#12183A 35%,#12183A 65%,transparent);}}
 .divider .dot{{width:16px;height:16px;background:#12183A;transform:rotate(45deg);}}
 .blocks{{margin-top:{btop}px;display:flex;flex-direction:column;gap:{bgap}px;width:100%;}}
 .b{{font-family:Poppins,sans-serif;font-weight:700;font-size:{bsize}px;
     line-height:1.30;color:#0A0C10;}}
 .punch{{font-family:Poppins,sans-serif;font-weight:900;font-size:{psize}px;
     line-height:1.24;color:#0A0C10;margin-top:{pgap}px;}}
 .imgband{{margin:{igap}px 0 4px;width:100%;display:flex;justify-content:center;}}
 .imgband img{{max-width:98%;max-height:{imax}px;}}
 .imgband.study img{{background:#fff;padding:12px;border:2px solid #12183A22;max-height:{smax}px;}}
 .studylabel{{font-family:Poppins,sans-serif;font-weight:900;font-size:{slsize}px;
     color:#1B2AA8;letter-spacing:4px;margin-top:26px;}}
 .arrow{{font-family:Poppins,sans-serif;font-size:{arrowsize}px;font-weight:800;
     color:#1B2AA8;margin-top:34px;}}
 .foot{{position:absolute;bottom:26px;left:46px;right:46px;font-family:Poppins,sans-serif;
     font-weight:600;font-size:{footsize}px;color:#7B8792;text-align:center;}}
 em{{font-style:normal;color:#2438E8;}}
 strong{{color:#E23A2E;font-weight:800;}}
 u{{text-decoration:underline;text-decoration-thickness:4px;text-underline-offset:6px;
    text-decoration-color:#2438E8;}}
 mark{{background:#FFD84D;color:inherit;padding:2px 9px;border-radius:4px;}}
</style></head><body>
<div class="wrap">
 <div class="brand">{brand}</div>
 <div class="headline">{headline}</div>
 <div class="divider"><div class="ln"></div><div class="dot"></div><div class="ln"></div></div>
 <div class="body">
  {imgblock}
  <div class="blocks">{blocks}</div>
  {punch}
  {arrow}
 </div>
</div>
<div class="foot">{foot}</div>
</body></html>"""


def marks(s):
    s = html.escape(s)
    s = re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"_(.+?)_", r"<u>\1</u>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--size", choices=list(SIZES), default="3:4")
    ap.add_argument("--tone", choices=list(TONES), default="darker")
    ap.add_argument("--brand", default="METRORAZ")
    ap.add_argument("--images", choices=["none", "few", "mixed", "many"], default="mixed")
    ap.add_argument("--out")
    a = ap.parse_args()

    deck = a.deck.rstrip("/")
    W, H = SIZES[a.size]
    bg, wash2, wash3 = TONES[a.tone]
    k = H / 1280.0                      # everything scales off his canvas height

    rows = list(csv.DictReader(open(os.path.join(deck, "04-slides.csv"))))
    imgdir = os.path.join(deck, "03-images")
    credits = {}
    cp = os.path.join(imgdir, "credits.txt")
    if os.path.exists(cp):
        for line in open(cp):
            if ":" in line and not line.startswith("#"):
                kk, v = line.split(":", 1)
                credits[kk.strip()] = v.strip()

    outdir = a.out or os.path.join(deck, "09-morph")
    os.makedirs(outdir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    receipts = 0

    for i, r in enumerate(rows, 1):
        parts = [p.strip() for p in (r.get("body") or "").split("|") if p.strip()]
        blocks = "".join(f'<div class="b">{marks(p)}</div>' for p in parts)
        punch = (r.get("punch") or "").strip()

        img = ""
        if a.images != "none":
            for ext in (".svg", ".png", ".jpg"):
                c = os.path.join(imgdir, f"slide-{i:02d}{ext}")
                if os.path.exists(c):
                    img = f'<div class="imgband"><img src="file://{os.path.abspath(c)}"></div>'
                    break
            if not img and a.images in ("mixed", "many"):
                pool = sorted(glob.glob(os.path.join(imgdir, "studies", "*.png")))
                cap = 2 if a.images == "mixed" else 99
                if pool and receipts < cap and 1 < i < len(rows):
                    img = ('<div class="studylabel">THE STUDY</div>'
                           f'<div class="imgband study"><img src="file://'
                           f'{os.path.abspath(pool[receipts % len(pool)])}"></div>')
                    receipts += 1

        body_len = len("".join(parts)) + len(punch)
        page = TPL.format(
            W=W, H=H, bg=bg, wash2=wash2, wash3=wash3,
            brand=html.escape(a.brand), headline=marks(r["headline"]),
            blocks=blocks,
            punch=f'<div class="punch">{marks(punch)}</div>' if punch else "",
            imgblock=img,
            arrow='<div class="arrow">&#10148;</div>' if i == 1 else "",
            foot=html.escape(credits.get(f"slide-{i:02d}", "")),
            padtop=int(30 * k), brandsize=int(30 * k), brandls=int(7 * k),
            brandgap=int(12 * k), divgap=int(20 * k), btop=int(30 * k),
            bgap=int(26 * k), pgap=int(34 * k), igap=int(26 * k),
            imax=int(430 * k), smax=int(330 * k), slsize=int(24 * k),
            arrowsize=int(60 * k), footsize=int(19 * k),
            hsize=max(int(40 * k), int((78 - max(0, len(r["headline"]) - 16) * 1.5) * k)),
            bsize=max(int(24 * k), int((40 - max(0, body_len - 150) * 0.030) * k)),
            psize=max(int(26 * k), int((44 - max(0, len(punch) - 60) * 0.055) * k)))

        src = os.path.join(tmp, f"s{i:02d}.html")
        open(src, "w").write(page)
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", f"--window-size={W},{H}",
                        "--virtual-time-budget=4500",
                        f"--screenshot={os.path.join(outdir, f'slide-{i:02d}.png')}",
                        f"file://{src}"], capture_output=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"  {len(rows)} slides -> {outdir}  ({a.size}, {a.tone})")


if __name__ == "__main__":
    main()
