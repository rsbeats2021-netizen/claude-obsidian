# Image library

Every licence-cleared image available for the decks. All are either **CC BY 4.0**
(commercial reuse permitted with attribution) or generated from scratch.

Filename convention: `subject__source__licence.ext`

## Photographs and journal figures (CC BY 4.0 — attribution required)

| File | Shows | Best for | Credit line |
|---|---|---|---|
| `growth-plate-pathways-schematic__paparella2025__CC-BY.png` | Growth plate zones labelled + PTHrP–Ihh loop, IGF1R, FGFR3, CNP–NPR2 | **Most reusable image here.** Any deck needing a growth plate diagram: growth-plate-fusion, resting-zone-stem-cells, bone-age-drivers, gh-vs-igf1, fgfr3-overgrowth | Paparella et al. 2025, *Children* — CC BY 4.0 |
| `femur-pair-vehicle-vs-SAG__trompet2024__CC-BY.png` | Two femurs side by side against a ruler, vehicle vs Hedgehog-agonist treated, treated visibly longer | resting-zone-stem-cells slide 5. **Strongest single asset** — a photo, no chart-reading needed | Trompet et al. 2024, *JCI Insight* — CC BY 4.0 |
| `bone-length-over-time__trompet2024__CC-BY.png` | Femur / tibia / whole-leg length at 1, 2, 6 months | Quantified backup to the photo above | Trompet et al. 2024, *JCI Insight* — CC BY 4.0 |
| `growth-plate-zones__hallett2019__CC-BY.png` | Colour-coded resting / proliferating / hypertrophic zones, stem-cell self-renewal, PTHrP, Ihh | resting-zone-stem-cells, growth-plate-fusion | Hallett et al. 2019, *Int J Mol Sci* — CC BY 4.0 |
| `tyra300-growth-curves__jci2025__CC-BY.png` | Dose-dependent growth: 14 > 12 mg/kg > vehicle | fgfr3-overgrowth slide 5 | *JCI Insight* 2025;10(9):e189307 — CC BY 4.0 |
| `tyra300-bone-lengths__jci2025__CC-BY.png` | Tibia and femur length by dose at 8 weeks | fgfr3-overgrowth, cleaner single-number version | *JCI Insight* 2025;10(9):e189307 — CC BY 4.0 |
| `androgen-biosynthesis-pathways__swerdloff2017__CC-BY.png` | Classical and "back-door" androgen biosynthesis pathways | testosterone-conversion-rates, androgen-receptors-in-bone | Swerdloff et al. 2017 — CC BY 4.0 |
| `gh-signalling-pathways__bolamperti__CC-BY.png` | Main intracellular signalling pathways activated by GH | gh-vs-igf1-division-of-labor, cartilage-targeted-igf1 | Bolamperti et al. — CC BY 4.0 |
| `chondrocyte-zones-histology__insulin-aromatase__CC-BY.png` | Chondrocyte histology by growth plate zone, control vs obese | insulin-aromatase-obesity | See `content/insulin-aromatase-obesity/06-sources.md` — CC BY 4.0 |

## Generated charts (no attribution needed — made for you)

| File | Shows | For |
|---|---|---|
| `chart-proliferation-collapse__generated.svg` | >95% dividing at birth → <10% by 17 weeks | resting-zone-stem-cells slide 3 |
| `chart-catchup-curve__generated.svg` | Growth dipping under suppression, then overshooting expected | catch-up-growth slide 1 |
| `chart-gh-conflicting-results__generated.svg` | ISS meta-analysis gain vs J Pediatr 1997 deficit, side by side | gh-height-myth slide 3 |

Regenerate or restyle: `python3 scripts/make-deck-charts.py` (palette constants
at the top of that file).

## Rules

- **Attribution is required** on every CC BY image. Put the credit line in the
  `tag` field of that slide, or as small footer text.
- **Not in this folder = not cleared.** `fig-senescence-baron2004.png` lives in
  `content/growth-plate-fusion/03-images/` and is Elsevier all-rights-reserved —
  reference only, gitignored, never publish it.
- Verify the credit line at the source before publishing; per-deck source paths
  are in each deck's `06-sources.md`.

## Adding more

`python3 scripts/scan-figure-licences.py` finds CC-BY papers in your own
library. Extraction is render-then-crop (journal figures are vector, so raster
extraction returns nothing):

```python
import pymupdf
d = pymupdf.open(path)
d[page].get_pixmap(dpi=600, clip=pymupdf.Rect(x0, y0, x1, y1)).save(out)
```
