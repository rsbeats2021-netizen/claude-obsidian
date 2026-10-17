"""Render every slide in styles-by-topic.html to 1080x1920 via headless Chrome.

Isolates one .sl at a time with injected CSS rather than parsing the markup,
so nested slide structures and the canvas slides both survive intact.
"""
import subprocess, shutil, re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / 'styles-by-topic.html'
BUILD = HERE / 'v3-build'
OUT = HERE / 'v3-out'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920

html = SRC.read_text()

# topic name per <section>, and how many slides each contains
sections = re.findall(r'<p class="tn">([^<]+)</p>', html)
per_section = [len(re.findall(r'class="sl ', block))
               for block in re.split(r'<section class="topic">', html)[1:]]
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
      .masthead,.brief{{display:none!important}}
      .wrap{{max-width:none;padding:0;gap:0}}
      .topic{{gap:0;border:0;padding:0;grid-template-columns:1fr}}
      .trio{{display:block;max-width:none;gap:0}}
      .sl{{display:none}}
      .sl:nth-of-type({n}){{display:flex;width:{W}px;height:{H}px;aspect-ratio:auto;
        padding-bottom:270px}}
    </style>"""

idx = 0
for s_i, (name, count) in enumerate(zip(sections, per_section), 1):
    # unescape first so "&amp;" doesn't slugify into a stray "amp"
    slug = re.sub(r'[^a-z0-9]+', '-', name.replace('&amp;', 'and').lower()).strip('-')
    for k in range(1, count + 1):
        idx += 1
        # hide every section but this one, then pick the kth slide inside it
        css = isolate(k) + f"""
        <style>
          section.topic{{display:none}}
          section.topic:nth-of-type({s_i}){{display:grid}}
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
