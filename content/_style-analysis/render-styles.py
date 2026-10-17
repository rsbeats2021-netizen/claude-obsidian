"""Render each style-library slide to 1080x1920 via headless Chrome.

Rather than parsing slides out of the HTML (they contain nested markup), this
loads the whole gallery and uses injected CSS to isolate one figure at a time.
"""
import subprocess, shutil, re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / 'style-library.html'
BUILD = HERE / 'styles-build'
OUT = HERE / 'styles-out'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920

html = SRC.read_text()
n_slides = len(re.findall(r'<div class="slide s\d\d"', html))
assert n_slides == 20, f"expected 20 slides, found {n_slides}"

# names for the output files, taken from each figcaption's bold label
labels = re.findall(r'<figcaption><b>\d+ · ([^<]+)</b>', html)
assert len(labels) == 20, f"expected 20 labels, found {len(labels)}"

for d in (BUILD, OUT):
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)

def isolate_css(i):
    return f"""
    <style>
      html,body{{margin:0;padding:0;background:#000}}
      .masthead,figcaption{{display:none!important}}
      .wrap{{max-width:none;padding:0;gap:0}}
      .grid{{display:block}}
      figure{{display:none;gap:0}}
      figure:nth-of-type({i}){{display:block}}
      .slide{{width:{W}px;height:{H}px;aspect-ratio:auto}}
    </style>"""

for i, label in enumerate(labels, 1):
    slug = re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')
    page = html + isolate_css(i)
    p = BUILD / f"{i:02d}.html"
    p.write_text(page)

    png = OUT / f"{i:02d}-{slug}.png"
    subprocess.run([
        CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
        f'--screenshot={png}', f'--window-size={W},{H}',
        '--force-device-scale-factor=1', '--virtual-time-budget=12000',
        f'file://{p}',
    ], check=True, capture_output=True)
    subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '92',
                    str(png), '--out', str(OUT / f"{i:02d}-{slug}.jpg")],
                   check=True, capture_output=True)
    print(f"{i:02d}  {label}")

print(f"\n{len(labels)} slides -> {OUT}")
