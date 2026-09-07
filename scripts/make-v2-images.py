#!/usr/bin/env python3
"""Generate per-slide diagrams for the v2 decks, in the v2 palette.

Same idea as make-deck-images.py but rebuilt for the grey ground and the
concepts the v2 decks actually need: signalling cascades, compound rankings,
energy comparisons, receptor blockade.

Output: content/<deck>/03-images/slide-NN.svg

Usage:
    python3 scripts/make-v2-images.py
    python3 scripts/make-v2-images.py --list
"""
import os
import sys

BG, INK, BLUE, RED, GREY, SOFT = "#EDEDEA", "#141414", "#1B4DE4", "#E0243B", "#8A8A8A", "#DAD8D2"
W = 940


def svg(body, h=560):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">'
            f'<rect width="{W}" height="{h}" fill="{BG}"/>{body}</svg>')


def t(x, y, s, size=26, fill=INK, weight="700", anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="Figtree,Helvetica,sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')


def cascade(steps, title="", h=560):
    """A -> B -> C chain, stacked vertically. steps = [(label, colour)]"""
    b = [t(W / 2, 52, title, 32)] if title else []
    top, gap = (96 if title else 60), 96
    for i, (lab, col) in enumerate(steps):
        y = top + i * gap
        b.append(f'<rect x="120" y="{y}" width="700" height="66" rx="12" fill="{col}"/>')
        b.append(t(W / 2, y + 44, lab, 28, BG if col != SOFT else INK, "800"))
        if i < len(steps) - 1:
            b.append(f'<path d="M{W/2},{y+70} L{W/2},{y+88}" stroke="{INK}" stroke-width="5"/>')
            b.append(f'<path d="M{W/2-11},{y+82} L{W/2},{y+94} L{W/2+11},{y+82}" fill="{INK}"/>')
    return svg("".join(b), top + len(steps) * gap + 20)


def ranked(items, title=""):
    """items = [(label, note, colour)] worst-to-best or ordered."""
    b = [t(W / 2, 52, title, 32)] if title else []
    top = 96 if title else 56
    for i, (lab, note, col) in enumerate(items):
        y = top + i * 104
        b.append(f'<rect x="90" y="{y}" width="760" height="82" rx="12" fill="{SOFT}"/>')
        b.append(f'<rect x="90" y="{y}" width="14" height="82" rx="7" fill="{col}"/>')
        b.append(t(130, y + 36, lab, 30, INK, "800", "start"))
        b.append(t(130, y + 66, note, 23, GREY, "600", "start"))
    return svg("".join(b), top + len(items) * 104 + 16)


def compare(left, right, title="", lnote="", rnote=""):
    b = [t(W / 2, 52, title, 32)] if title else []
    b.append(f'<rect x="70" y="110" width="360" height="150" rx="14" fill="{BLUE}"/>')
    b.append(t(250, 200, left, 34, BG, "800"))
    b.append(f'<rect x="510" y="110" width="360" height="150" rx="14" fill="{INK}"/>')
    b.append(t(690, 200, right, 34, BG, "800"))
    b.append(t(250, 300, lnote, 24, INK, "600"))
    b.append(t(690, 300, rnote, 24, INK, "600"))
    b.append(t(W / 2, 200, "vs", 30, GREY, "800"))
    return svg("".join(b), 340)


def bars(items, title=""):
    b = [t(W / 2, 48, title, 30)] if title else []
    n = len(items)
    slot = 780 / n
    for i, (lab, val, col) in enumerate(items):
        bw = slot * 0.56
        bx = 80 + i * slot + (slot - bw) / 2
        bh = val / 100 * 300
        b.append(f'<rect x="{bx:.0f}" y="{400-bh:.0f}" width="{bw:.0f}" height="{bh:.0f}" rx="6" fill="{col}"/>')
        b.append(t(bx + bw / 2, 438, lab, 24))
    b.append(f'<line x1="60" y1="400" x2="880" y2="400" stroke="{INK}" stroke-width="4"/>')
    return svg("".join(b), 470)


def blocked(signal, receptor, outcome):
    b = [t(230, 90, signal, 32, BLUE)]
    b.append(f'<line x1="230" y1="115" x2="230" y2="185" stroke="{BLUE}" stroke-width="9"/>')
    b.append(f'<path d="M212,178 L230,200 L248,178" fill="{BLUE}"/>')
    b.append(f'<rect x="120" y="215" width="220" height="105" rx="12" fill="none" stroke="{INK}" stroke-width="6"/>')
    b.append(t(230, 278, receptor, 26))
    b.append(f'<line x1="136" y1="230" x2="324" y2="305" stroke="{RED}" stroke-width="11"/>')
    b.append(f'<line x1="324" y1="230" x2="136" y2="305" stroke="{RED}" stroke-width="11"/>')
    b.append(f'<line x1="370" y1="268" x2="520" y2="268" stroke="{GREY}" stroke-width="6" stroke-dasharray="16 12"/>')
    b.append(t(720, 278, outcome, 34, GREY, "800"))
    return svg("".join(b), 380)


MAP = {
 "v2-why-growth-takes-so-long": {
   3: (cascade, ([("No blood vessels in the plate", SOFT), ("No oxygen delivery", SOFT),
                  ("Glycolysis instead: 2 ATP", RED), ("Oxidative would give 32 ATP", BLUE)],
                 "Why the growth plate is energy limited")),
   7: (bars, ([("at birth", 95, BLUE), ("17 weeks", 10, RED)], "Resting zone cells dividing (%)")),
 },
 "v2-what-runs-out": {
   4: (bars, ([("at birth", 95, BLUE), ("17 weeks", 10, RED)], "Resting zone cells dividing (%)")),
 },
 "v2-estrogen-closes-you": {
   4: (blocked, ("estradiol x10", "estrogen receptor", "no response")),
   6: (cascade, ([("Testosterone", SOFT), ("Aromatase in the plate", BLUE),
                  ("Estradiol", RED), ("Plate closes", INK)], "Where your closing signal is made")),
 },
 "v2-local-conversion": {
   7: (compare, ("ESTRADIOL", "DHT", "One testosterone, two fates",
                 "closes the plate", "cannot aromatise")),
 },
 "v2-loading-builds-bone": {
   3: (cascade, ([("Mechanical load", SOFT), ("Osteocytes sense strain", SOFT),
                  ("Nitric oxide and PGE2", BLUE), ("Sclerostin blocked", RED),
                  ("Wnt up, bone formed", INK)], "How force becomes bone")),
   10: (compare, ("IN RANGE", "ABOVE IT", "Loading is a dose response",
                  "COL2 and SOX9 up", "MMP13 and ADAMTS4 up")),
 },
 "v2-aas-brain": {
   3: (ranked, ([("Trenbolone", "apoptosis, neurite outgrowth down, Tubb3 down", RED),
                 ("Nandrolone", "apoptosis, mitochondria hit by 24h", RED),
                 ("Testosterone", "apoptosis, LDH release", BLUE),
                 ("Stanozolol", "necrosis instead, inflammatory", GREY)],
                "How each compound kills neurons")),
   8: (cascade, ([("Androgen receptor activated", RED), ("Mitochondrial failure", SOFT),
                  ("Caspase 3/7 fires", SOFT), ("Apoptosis", INK)],
                 "The damage pathway to target")),
 },
 "v2-gh-truth": {
   2: (bars, ([("control", 62, GREY), ("GH treated", 78, BLUE)], "ISS meta-analyses: +4 to 6 cm")),
   3: (bars, ([("untreated", 92, GREY), ("GH treated", 70, RED)], "J Pediatr 1997: 162.0 vs 154.2 cm")),
 },
 "v2-bone-age": {
   3: (bars, ([("phalanges", 38, RED), ("metacarpals", 46, RED),
               ("tibia", 78, BLUE), ("femur", 86, BLUE)], "Time left before senescence")),
 },
 "v2-catch-up": {
   7: (compare, ("SLOWED", "SPENT", "Two things a growth chart cannot tell apart",
                 "fully reversible", "permanent")),
 },
 "v2-steroids-jaw": {
   3: (bars, ([("control", 72, GREY), ("nandrolone", 80, BLUE)], "Juvenile mandibular length +24.5% vs +27.2%")),
   4: (bars, ([("control", 6, GREY), ("nandrolone", 68, BLUE)], "Adult mandibular length +0.3% vs +4.7%")),
 },
 "v2-aromatase-inhibitors": {
   3: (cascade, ([("4 randomised trials", SOFT), ("207 participants", SOFT),
                  ("All improved PREDICTED height", BLUE),
                  ("1 measured real height", RED),
                  ("No meaningful difference", INK)], "The whole evidence base")),
 },
}


def main():
    if "--list" in sys.argv:
        for d, m in MAP.items():
            print(f"{d}: slides {sorted(m)}")
        return
    n = 0
    for deck, slides in MAP.items():
        if not os.path.isdir(f"content/{deck}"):
            print(f"  skip {deck}")
            continue
        out = f"content/{deck}/03-images"
        os.makedirs(out, exist_ok=True)
        for num, (fn, args) in slides.items():
            open(f"{out}/slide-{num:02d}.svg", "w").write(fn(*args))
            n += 1
        print(f"{deck}: {len(slides)}")
    print(f"\n{n} diagrams generated")


if __name__ == "__main__":
    main()
