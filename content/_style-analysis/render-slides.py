"""Render the carousel slides to 1080x1920 image files via headless Chrome.

Extracts the <style> block and each <article class="slide"> from the deck and
emits one standalone, viewport-sized page per slide, then screenshots each.
"""
import re, subprocess, shutil
from pathlib import Path

HERE = Path(__file__).parent
DECK = HERE / 'first-ninety-minutes.html'
BUILD = HERE / 'slides-build'
OUT = HERE / 'slides-out'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

W, H = 1080, 1920

html = DECK.read_text()

# the deck's <link> font tags and its <style> block travel with each slide
fonts = "\n".join(re.findall(r'<link[^>]+fonts\.(?:googleapis|gstatic)[^>]*>', html))
style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)

# each slide is one <article class="slide ..."> ... </article>
slides = re.findall(r'(<article class="slide.*?</article>)', html, re.S)
assert len(slides) == 9, f"expected 9 slides, found {len(slides)}"

# export overrides: fill the viewport exactly, drop the on-page card chrome.
# Bottom padding clears the TikTok/IG UI overlay (caption, buttons, progress),
# which covers roughly the lowest 250px of a 1920-tall frame.
EXPORT_CSS = f"""
  html, body {{ margin:0; padding:0; background:var(--ink); }}
  .slide {{
    width:{W}px; height:{H}px; aspect-ratio:auto;
    border:0; border-radius:0; flex:none;
    scroll-snap-align:none;
    padding:110px 80px 270px;
  }}
"""

for tmpl in (BUILD, OUT):
    shutil.rmtree(tmpl, ignore_errors=True)
    tmpl.mkdir(parents=True)

pages = []
for i, slide in enumerate(slides, 1):
    page = (
        f"<!doctype html><html><head><meta charset='utf-8'>{fonts}"
        f"<style>{style}{EXPORT_CSS}</style></head><body>{slide}</body></html>"
    )
    p = BUILD / f"slide-{i:02d}.html"
    p.write_text(page)
    pages.append(p)

for p in pages:
    png = OUT / f"{p.stem}.png"
    subprocess.run([
        CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
        f'--screenshot={png}', f'--window-size={W},{H}',
        '--force-device-scale-factor=1', '--virtual-time-budget=10000',
        f'file://{p}',
    ], check=True, capture_output=True)
    # JPEG copy for upload
    subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '92',
                    str(png), '--out', str(OUT / f"{p.stem}.jpg")],
                   check=True, capture_output=True)
    print(f"rendered {png.name}")

print(f"\n{len(pages)} slides -> {OUT}")
