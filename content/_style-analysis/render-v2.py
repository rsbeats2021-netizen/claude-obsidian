"""Render every slide in slideshow-styles-v2.html to 1080x1920 via headless Chrome.

Isolates one .sl at a time with injected CSS rather than parsing the markup,
so nested slide structures and the canvas slides both survive intact.
"""
import subprocess, shutil, re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / 'slideshow-styles-v2.html'
BUILD = HERE / 'v2-build'
OUT = HERE / 'v2-out'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920

html = SRC.read_text()

# style name per <section>, and how many slides each contains
sections = re.findall(r'<div class="set-hd"><b>\d+ · ([^<]+)</b>', html)
per_section = [len(re.findall(r'class="sl ', block))
               for block in re.split(r'<section class="set">', html)[1:]]
assert len(sections) == len(per_section), 'section/label mismatch'
total = sum(per_section)
print(f"{len(sections)} styles, {total} slides")

for d in (BUILD, OUT):
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)

def isolate(n):
    """CSS that shows only the nth .sl on the page, sized to the frame."""
    return f"""
    <style>
      html,body{{margin:0;padding:0;background:#000}}
      .masthead,.set-hd{{display:none!important}}
      .wrap{{max-width:none;padding:0;gap:0}}
      .set{{gap:0}}
      .trio{{display:block;max-width:none;gap:0}}
      .sl{{display:none}}
      .sl:nth-of-type({n}){{display:flex;width:{W}px;height:{H}px;aspect-ratio:auto;
        padding-bottom:270px}}
    </style>"""

idx = 0
for s_i, (name, count) in enumerate(zip(sections, per_section), 1):
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    for k in range(1, count + 1):
        idx += 1
        # hide every section but this one, then pick the kth slide inside it
        css = isolate(k) + f"""
        <style>
          section.set{{display:none}}
          section.set:nth-of-type({s_i}){{display:flex}}
        </style>"""
        p = BUILD / f"{s_i:02d}-{k}.html"
        p.write_text(html + css)
        png = OUT / f"{s_i:02d}{chr(96+k)}-{slug}.png"
        subprocess.run([
            CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
            f'--screenshot={png}', f'--window-size={W},{H}',
            '--force-device-scale-factor=1', '--virtual-time-budget=12000',
            f'file://{p}',
        ], check=True, capture_output=True)
        subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '92',
                        str(png), '--out', str(OUT / f"{png.stem}.jpg")],
                       check=True, capture_output=True)
    print(f"  {s_i:02d} {name} — {count} slides")

print(f"\n{idx} slides -> {OUT}")
