# Image inbox — drop images here

Drop anything in this folder. Claude inventories it, looks at each image, and
sorts it by subject, pathway, deck fit, and **licence status**.

## Before you drop: the one thing that matters

**Keep the source with the file.** The classification I can do from looking at
an image (what it shows, which deck it fits) is the easy half. Whether you can
legally publish it is the half that actually blocks you, and I cannot determine
that from pixels.

Best to worst, for each image:

1. **Name the file with the source** — `PMC12525321-fig3.png`, `hallett2019-fig1.png`
2. **Drop a `sources.txt`** in the same folder, one line per image:
   `filename.png — https://pmc.ncbi.nlm.nih.gov/articles/PMC12525321/`
3. **Sub-folder per paper** — `PMC12525321/fig1.png, fig3.png`
4. Nothing — then it lands in `unknown-licence/` and is unusable until traced

A screenshot with no source is a dead end. Not because I'm being strict — because
your channel is monetised, so everything counts as commercial use, and
CC BY-NC is already off-limits to you.

## What happens next

1. `python3 scripts/inventory-images.py content/_image-inbox`
   Dedupes, flags anything under 700px wide (soft on a 1080px slide), groups by shape.
2. Claude looks at each usable image and writes `_classified.md`:
   subject · pathway/mechanism · which decks and slides it fits · licence status
3. Cleared images get renamed `subject__source__licence.ext` and moved to
   `content/_image-library/`
4. Everything unresolved goes to `unknown-licence/` rather than into the library

## Sorting categories

By type: photograph · histology · schematic/pathway diagram · chart/graph ·
anatomical illustration · X-ray or imaging

By pathway/topic: growth plate zones · PTHrP–Ihh · FGFR3 · GH/IGF-1 ·
estrogen/aromatase · androgen/AR · thyroid · stem cells/Hedgehog ·
bone structure · craniofacial

## Practical limit

Looking at images is the expensive step. **50–100 per batch** is comfortable.
More than that, drop them in batches or tell me which subfolder to prioritise —
otherwise I burn the budget on images that were never going to be usable.
