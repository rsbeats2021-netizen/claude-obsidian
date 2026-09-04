#!/usr/bin/env python3
"""Validate a slideshow CSV before it goes anywhere near Canva Bulk Create.

Catches the failure modes that cost a full re-run: wrong column set, empty
cells (Bulk Create leaves a blank element), copy that overflows the text box,
and slides with no open loop to drive the swipe.

Usage:
    python3 scripts/check-deck.py content/<deck>/04-slides.csv
    python3 scripts/check-deck.py "content/*/04-slides.csv"    # quote in zsh

Note the quotes on the glob: zsh errors on an unmatched glob before the script
ever runs, so quoting hands the pattern through for the script to expand.
"""
import csv
import glob
import re
import sys

COLUMNS = ["headline", "subhead", "body", "punch"]

# Ceilings measured against the built Canva template. Raise these only after
# re-testing the template — they are what guarantees copy fits the boxes.
LIMITS = {"headline": 30, "subhead": 30, "body": 300, "punch": 160}

# Deliberately NOT checked: whether each slide leaves an open loop. That's a
# semantic property, and a regex for it fired on 4 of 9 slides that genuinely
# had hooks. A lint that cries wolf gets ignored, which is worse than no lint.
# Open loops stay a human review item — see 02-slideshow.md design notes.


def check(path):
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    errs, warns = [], []

    if not rows:
        return [f"{path}: empty file"], []

    cols = [c for c in rows[0].keys() if c is not None]
    if cols != COLUMNS:
        errs.append(f"columns are {cols}, expected {COLUMNS}")

    # Field drift: an unquoted comma inside a field splits it, pushing the tail
    # into DictReader's None key. The row still has all five NAMED keys, so a
    # column check alone sails straight past it — and Canva then renders a
    # truncated punch line with the tier flag as the tag. Caught this only
    # after 10 rows across 8 decks had already drifted.
    for i, r in enumerate(rows, 1):
        if None in r:
            errs.append(
                f"slide {i}: field drift — an unquoted comma split a field "
                f"(overflow: {r[None]!r}). Quote the field containing the comma."
            )

    if not (8 <= len(rows) <= 12):
        warns.append(f"{len(rows)} slides — target 8-12 for swipe-through completion")

    for i, r in enumerate(rows, 1):
        for col in cols:
            val = (r.get(col) or "").strip()
            if not val:
                errs.append(f"slide {i}: '{col}' is empty — Bulk Create will leave a blank element")
                continue
            cap = LIMITS.get(col)
            if cap and len(val) > cap:
                errs.append(f"slide {i}: '{col}' is {len(val)} chars, over the {cap} ceiling — will overflow")
    # Em dashes are banned in deck copy by house style.
    for i, r in enumerate(rows, 1):
        for col in COLUMNS:
            if "\u2014" in (r.get(col) or ""):
                errs.append(f"slide {i}: em dash in '{col}' - house style bans them")

    return errs, warns


def main():
    paths = []
    for arg in sys.argv[1:]:
        paths.extend(glob.glob(arg))
    if not paths:
        sys.exit("usage: check-deck.py <csv> [csv ...]")

    failed = False
    for path in sorted(paths):
        errs, warns = check(path)
        status = "FAIL" if errs else ("warn" if warns else "ok")
        print(f"\n[{status}] {path}")
        for e in errs:
            print(f"   ERROR  {e}")
        for w in warns:
            print(f"   warn   {w}")
        if not errs and not warns:
            print("   all checks passed")
        failed |= bool(errs)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
