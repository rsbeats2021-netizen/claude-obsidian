"""Render the three finished decks to 1080x1920 via headless Chrome."""
import subprocess, shutil, re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / 'decks-height-skin-face.html'
BUILD = HERE / 'decks-build'
OUT = HERE / 'decks-out'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920

html = SRC.read_text()
decks = re.findall(r'<div class="dh"><b>Deck \d+ — ([^<]+)</b>', html)
counts = [len(re.findall(r'class="sl s', blk)) for blk in re.split(r'<section class="deck">', html)[1:]]
assert len(decks) == len(counts), 'deck/label mismatch'
print(f"{len(decks)} decks, {sum(counts)} slides")

for d in (BUILD, OUT):
    shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)

for di, (name, n) in enumerate(zip(decks, counts), 1):
    slug = re.sub(r'[^a-z0-9]+', '-', name.replace('&amp;', 'and').lower()).strip('-')
    for k in range(1, n + 1):
        css = f"""<style>
          html,body{{margin:0;padding:0;background:#000}}
          .masthead,.dh,.cap{{display:none!important}}
          .wrap{{max-width:none;padding:0;gap:0}}
          .deck{{display:none;gap:0;border:0;padding:0}}
          .deck:nth-of-type({di}){{display:block}}
          .track{{display:block;overflow:visible;padding:0}}
          .track .sl{{display:none}}
          .track .sl:nth-of-type({k}){{display:flex;width:{W}px;height:{H}px;
            aspect-ratio:auto;border-radius:0;padding-bottom:270px}}
        </style>"""
        p = BUILD / f"{di}-{k}.html"; p.write_text(html + css)
        png = OUT / f"deck{di}-{slug}-{k:02d}.png"
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
            f'--screenshot={png}', f'--window-size={W},{H}', '--force-device-scale-factor=1',
            '--virtual-time-budget=12000', f'file://{p}'], check=True, capture_output=True)
        subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '92',
            str(png), '--out', str(OUT / f"{png.stem}.jpg")], check=True, capture_output=True)
    print(f"  deck {di} — {name} — {n} slides")
print(f"\n-> {OUT}")
