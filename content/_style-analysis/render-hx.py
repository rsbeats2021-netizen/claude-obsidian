"""Render the growth-remaining deck to 1080x1920 via headless Chrome."""
import subprocess, shutil, re
from pathlib import Path
HERE=Path(__file__).parent
SRC=HERE/'deck-hypoxia-native.html'; BUILD=HERE/'hx-build'; OUT=HERE/'hx-out'
CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W,H=1080,1920
html=SRC.read_text()
n=len(re.findall(r'<div class="sl[ "]',html))
print(f"{n} slides")
for d in (BUILD,OUT):
    shutil.rmtree(d,ignore_errors=True); d.mkdir(parents=True)
for k in range(1,n+1):
    css=f"""<style>
      html,body{{margin:0;padding:0;background:#000}}
      .masthead,.cap,.tmpl,.note{{display:none!important}}
      .wrap{{max-width:none;padding:0;gap:0}}
      .track{{display:block;overflow:visible;padding:0}}
      .track .sl{{display:none}}
      .track .sl:nth-of-type({k}){{display:flex;width:{W}px;height:{H}px;
        aspect-ratio:auto;border-radius:0;padding-bottom:270px}}
    </style>"""
    p=BUILD/f"{k}.html"; p.write_text(html+css)
    png=OUT/f"hypoxia-{k:02d}.png"
    subprocess.run([CHROME,'--headless=new','--disable-gpu','--hide-scrollbars',
      f'--screenshot={png}',f'--window-size={W},{H}','--force-device-scale-factor=1',
      '--virtual-time-budget=12000',f'file://{p}'],check=True,capture_output=True)
    subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','92',
      str(png),'--out',str(OUT/f"{png.stem}.jpg")],check=True,capture_output=True)
print(f"-> {OUT}")
