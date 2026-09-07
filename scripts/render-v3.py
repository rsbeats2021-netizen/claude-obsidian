#!/usr/bin/env python3
"""Same deck CSV, three different design directions, so they can be compared.

Styles:
  dark       near-black ground, off-white type, amber and cyan accents.
             Condensed heavy headline. Reads as tech / lab.
  editorial  warm paper, serif display headline, generous spacing.
             Reads as a written piece rather than a graphic.
  blocks     high contrast. Headline reversed out of a solid colour band,
             body on white. Reads as a poster.

Usage:
    python3 scripts/render-v3.py content/<deck> --style dark
    python3 scripts/render-v3.py content/<deck> --style editorial --out /tmp/x
"""
import argparse
import csv
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SIZES = {"9:16": (1080, 1920), "4:5": (1080, 1350), "1:1": (1080, 1080)}
W, H = SIZES["9:16"]

STYLES = {
    "dark": dict(
        bg="#0E1116", ink="#F2F4F7", accent="#FFB020", accent2="#3DD6D0",
        grey="#7C8794", band="#161B22",
        fonts="family=Anton&family=Inter:wght@400;600;700",
        hfont="'Anton',sans-serif", hweight="400", bfont="'Inter',sans-serif",
        bweight="400", pweight="700", htransform="none", hspacing="0px",
    ),
    "editorial": dict(
        bg="#F7F3EC", ink="#1A1815", accent="#8A3324", accent2="#3F5E4C",
        grey="#8B8378", band="#EDE6DA",
        fonts="family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;700",
        hfont="'Instrument Serif',Georgia,serif", hweight="400",
        bfont="'Inter',sans-serif", bweight="400", pweight="700",
        htransform="none", hspacing="-1px",
    ),
    "blocks": dict(
        bg="#FFFFFF", ink="#101010", accent="#FF3B30", accent2="#0A84FF",
        grey="#9A9A9A", band="#101010",
        fonts="family=Anton&family=Archivo:wght@500;700;900",
        hfont="'Anton',sans-serif", hweight="400", bfont="'Archivo',sans-serif",
        bweight="500", pweight="900", htransform="uppercase", hspacing="0.5px",
    ),
}

TPL = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>
 *{{margin:0;padding:0;box-sizing:border-box}}
 html,body{{width:{W}px;height:{H}px;background:{bg};}}
 .wrap{{position:absolute;inset:0;padding:{pad};display:flex;flex-direction:column;
        align-items:{align};text-align:{talign};justify-content:center;}}
 .band{{position:absolute;top:0;left:0;right:0;padding:74px 62px 56px;background:{bandbg};}}
 .headline{{font-family:{hfont};font-weight:{hweight};font-size:{hsize}px;
        line-height:{hlh};color:{hcolor};letter-spacing:{hspacing};
        text-transform:{htransform};}}
 .sub{{font-family:{bfont};font-weight:700;font-size:40px;color:{accent};
        margin-top:18px;letter-spacing:1px;}}
 .blocks{{margin-top:{btop}px;display:flex;flex-direction:column;gap:{bgap}px;width:100%;}}
 .b{{font-family:{bfont};font-weight:{bweight};font-size:{bsize}px;
     line-height:1.42;color:{ink};}}
 .punch{{font-family:{bfont};font-weight:{pweight};font-size:{psize}px;
     line-height:1.24;color:{ink};margin-top:54px;}}
 .rule{{width:120px;height:5px;background:{accent};margin:36px 0 0;}}
 .imgband{{margin:34px 0 6px;width:100%;display:flex;justify-content:{align};}}
 .imgband img{{max-width:96%;max-height:600px;}}
 .arrow{{font-family:{bfont};font-size:82px;font-weight:700;color:{accent};margin-top:52px;}}
 .foot{{position:absolute;bottom:44px;left:62px;right:62px;font-family:{bfont};
     font-weight:400;font-size:22px;color:{grey};text-align:{talign};}}
 em{{font-style:normal;color:{accent2};font-weight:700;}}
 strong{{font-weight:700;color:{accent};}}
</style></head><body>
{bandhtml}
<div class="wrap">
 {headhtml}
 {imgblock}
 <div class="blocks">{blocks}</div>
 {punch}
 {arrow}
</div>
<div class="foot">{foot}</div>
</body></html>"""


def marks(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def fit(t, base, floor, budget):
    return max(floor, int(base - max(0, len(t) - budget) * 0.085))


def render(deck, style, outdir):
    S = STYLES[style]
    rows = list(csv.DictReader(open(os.path.join(deck, "04-slides.csv"))))
    imgdir = os.path.join(deck, "03-images")
    credits = {}
    cp = os.path.join(imgdir, "credits.txt")
    if os.path.exists(cp):
        for line in open(cp):
            if ":" in line and not line.startswith("#"):
                k, v = line.split(":", 1)
                credits[k.strip()] = v.strip()

    os.makedirs(outdir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    for i, r in enumerate(rows, 1):
        parts = [p.strip() for p in (r.get("body") or "").split("|") if p.strip()]
        blocks = "".join(f'<div class="b">{marks(p)}</div>' for p in parts)
        img = ""
        for ext in (".svg", ".png", ".jpg"):
            c = os.path.join(imgdir, f"slide-{i:02d}{ext}")
            if os.path.exists(c):
                img = f'<div class="imgband"><img src="file://{os.path.abspath(c)}"></div>'
                break
        sub = (r.get("subhead") or "").strip()
        if sub.upper().startswith("SECTION:"):
            sub = sub.split(":", 1)[1].strip()
        punch = (r.get("punch") or "").strip()
        hsize = fit(r["headline"], 112 if style != "editorial" else 122, 64, 20)

        head = (f'<div class="headline">{marks(r["headline"])}</div>'
                + (f'<div class="sub">{marks(sub.upper())}</div>' if sub else "")
                + ('<div class="rule"></div>' if style == "editorial" else ""))
        # blocks style puts the headline in a solid band at the top
        bandhtml = f'<div class="band">{head}</div>' if style == "blocks" else ""
        headhtml = "" if style == "blocks" else head

        page = TPL.format(
            W=W, H=H, fonts=S["fonts"], bg=S["bg"], ink=S["ink"], accent=S["accent"],
            accent2=S["accent2"], grey=S["grey"],
            bandbg=S["band"], hcolor=S["bg"] if style == "blocks" else S["ink"],
            hfont=S["hfont"], hweight=S["hweight"], bfont=S["bfont"],
            bweight=S["bweight"], pweight=S["pweight"],
            htransform=S["htransform"], hspacing=S["hspacing"],
            hlh="0.98" if style != "editorial" else "1.04",
            pad="330px 62px 100px" if style == "blocks" else "96px 62px 92px",
            align="flex-start" if style == "editorial" else "center",
            talign="left" if style == "editorial" else "center",
            btop=46 if style != "blocks" else 20, bgap=40,
            hsize=hsize, bsize=fit("".join(parts) + punch, 50, 34, 210),
            psize=fit(punch, 54, 38, 80),
            headhtml=headhtml, bandhtml=bandhtml, blocks=blocks,
            punch=f'<div class="punch">{marks(punch)}</div>' if punch else "",
            imgblock=img,
            arrow='<div class="arrow">&#8594;</div>' if i == 1 else "",
            foot=html.escape(credits.get(f"slide-{i:02d}", "")))
        src = os.path.join(tmp, f"s{i:02d}.html")
        open(src, "w").write(page)
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", f"--window-size={W},{H}",
                        "--virtual-time-budget=4500",
                        f"--screenshot={os.path.join(outdir, f'slide-{i:02d}.png')}",
                        f"file://{src}"], capture_output=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"  [{style}] {len(rows)} slides -> {outdir}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--style", choices=list(STYLES), required=True)
    ap.add_argument("--out")
    ap.add_argument("--size", choices=list(SIZES), default="9:16",
                    help="4:5 keeps content clear of TikTok's UI overlay")
    a = ap.parse_args()
    global W, H
    W, H = SIZES[a.size]
    d = a.deck.rstrip("/")
    render(d, a.style, a.out or os.path.join(d, f"08-{a.style}"))


if __name__ == "__main__":
    main()
