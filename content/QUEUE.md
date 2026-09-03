# Content production queue

## ▶ START HERE NEXT SESSION

**State as of 2026-09-03.** Eight decks built, all CSVs validated against the
Canva template. Pipeline is proven end-to-end on deck 1.

| Deck | brief | visual plan | video | CSV | figure catalogue |
|---|---|---|---|---|---|
| growth-plate-fusion | ✅ | ✅ | ✅ | ✅ | 1 cleared figure |
| estrogen-sets-final-height | ✅ | ✅ | ✅ | ✅ | ✅ |
| gh-height-myth | ✅ | ✅ | held | ✅ | thin (2) |
| resting-zone-stem-cells | ✅ | ✅ | ✅ | ✅ | ✅ best |
| catch-up-growth | ✅ | ✅ | ✅ | ✅ | ✅ |
| stimulants-and-growth | ✅ | ✅ | ✅ | ✅ | thin/adjacent |
| aromatase-inhibitor-monitoring-gap | ✅ | ✅ | ✅ | ✅ | thin |
| fgfr3-overgrowth | ✅ | ✅ | ✅ | ✅ | thin (2 usable) |

**All eight decks are complete**: tier-tagged brief · per-slide visual plan
with named figure assignments · validated 5-column CSV · figure catalogue ·
video script. Two intentional gaps only:
- `gh-height-myth` video script held pending per-study citation verification
- `growth-plate-fusion` also holds one actually-cleared CC-BY image file

**Highest-value single visuals across the batch** (if design time is limited):
1. `estrogen` slide 4 — estradiol ×10 arrow hitting a broken receptor
2. `gh-height-myth` slide 4 — $35,000 per inch, enormous, minimal else
3. `resting-zone` slide 3 — >95% → <10% proliferation collapse chart
4. `catch-up-growth` slide 1 — the dip-then-overshoot curve
5. `growth-plate-fusion` slide 3 — the transplant two-panel

**First three things to do next session, in order:**

1. **Template needs a 5th text element** — bold, connected to the `punch`
   column — before ANY of these six run through Bulk Create. Deck 1 was built
   on the old 4-column schema; all six CSVs are now 5-column.
2. **GH deck was rebuilt twice — read `gh-height-myth/01-research.md` first.**
   The original script's "height decrease" claims turned out to be **real**:
   J Pediatr 1997 found non-GH-deficient boys reached 154.2 cm treated vs
   162.0 cm untreated. So the meta-analytic rebuttal was also too clean. The
   deck now presents the genuine split, which is the strongest version of it.
   Per-study citations (Bierich, Koplowitz, Lach, Kawaii, Bernasconi, Lanes,
   Witt) remain unverified — the CSV cites only the two confirmed claims. Verify
   before writing the video script.
3. **Pull the actual figure images.** Each deck has `05-figures.md` listing
   CC-BY papers with ⭐-flagged diagram figures and direct PMC links. PMC blocks
   scripted image downloads, so this is click-and-save. Log each one in a
   `03-images/manifest.md` with its attribution line.

**Known gaps, deliberately left:**
- 9 image files exist across 4 decks (2 extracted CC-BY, 3 generated SVG charts,
  1 earlier Hallett figure). The other 4 decks still need images.
- Two extraction routes now proven: `scan-figure-licences.py` finds CC-BY papers
  in the LOCAL library (PMC blocks scripted download, local PDFs don't), and
  `make-deck-charts.py` generates brand-palette SVG for chart slides.
- Remaining redraws are conceptual, not chart-shaped: the estrogen deck's
  broken-receptor graphic, the FGFR3 mirror-image axis, the aromatase
  two-checklists. Those need a designer, not a script.
- No deck has actual image files except growth-plate-fusion (1 cleared figure).
- Redraws owed: deck 1 slide 3 transplant two-panel + slides 6/7 curves;
  resting-zone slide 3 proliferation-collapse chart; catch-up slides 1 and 6.

**Commands:**
```bash
python3 scripts/check-deck.py "content/*/04-slides.csv"     # validate all decks
python3 scripts/find-oa-figures.py "<topic>" --reviews      # find CC-BY figures
python3 scripts/scan-figure-licences.py                     # audit own library
```
`find-oa-figures.py` and PDF figure extraction need pymupdf:
`python3 -m venv .venv && .venv/bin/pip install pymupdf`

---


Standing work list. Claude works down this autonomously; you reorder, add, or
strike items whenever. Newest status at the top of each item.

**Scope**: mechanism explainers, myth teardowns, what the literature actually
shows, nutrition/natural levers. Not dosing or protocol content — see
[[tiktok-format-research]] on why that category is also the account-risk one.

---

## In progress

- [ ] **Deck 1 — "Fusion is the receipt, not the cause"** (`growth-plate-fusion/`)
  - ✅ research brief, slideshow script, video script, CSV
  - ✅ one CC-BY figure cleared (Hallett 2019)
  - ✅ **2026-09-03 — CSV rewritten for density + swipe mechanics.** 9 → 10
        slides. Body copy expanded to 40–60 words (reverse swipes are a positive
        ranking signal, so re-read-worthy slides help). Every slide now ends on
        an open loop. Added a catch-up-growth slide — it's the strongest proof
        of the bank-account model and the biggest "wait, what?" beat in the deck.
  - ✅ **2026-09-03 — drift bug fixed.** `02-slideshow.md` had duplicated the
        slide copy and the two had already diverged. Prose file now holds only
        visual direction, structure and design notes; `04-slides.csv` is the
        single source of truth for copy.
  - ✅ **2026-09-03 — CSV schema changed to 5 columns (added `punch`).** First
        Canva run showed body sizing was fixable but that hand-added bold
        emphasis would be wiped by every regeneration (Bulk Create carries plain
        text; only element-level styling survives). Payoff line now lives in its
        own permanently-bold element. Removes a 10-slide manual pass from every
        future deck. **Template needs a 5th text element before the next run.**
  - [ ] swap in PMC12525321 Fig 3 (stem-cell niche schematic, CC-BY)
  - [ ] redraw slide 3 transplant two-panel

## Ready for Canva (validated, 5-column schema)

- [ ] **Deck 2 — "Estrogen, not testosterone, sets final height"**
      (`estrogen-sets-final-height/`) — brief ✅ CSV ✅ video ✅
      Built on Smith 1994 NEJM (ERα mutation, normal testosterone, never stopped
      growing) with the six-month estrogen-therapy null result as a built-in
      control. Ends on genuine contested evidence (Gunther 2001, GPER-1) rather
      than a clean resolution.
- [ ] **Deck 3 — "What GH actually buys"** (`gh-height-myth/`) — brief ✅ CSV ✅
      ⚠️ **Reframed after fact-check.** The original script's claim ("can't grow
      taller with GH unless deficient") contradicts the meta-analyses: +0.84 SD,
      4–6 cm gain in idiopathic short stature. New angle is the defensible one —
      modest, ~$35k/inch, and studied on a population most viewers aren't in.
      Includes a correction slide, which is itself on-brand.
      Video script held until the individual citations are verified.

- [ ] **Deck 4 — "The cells you actually run out of"** (`resting-zone-stem-cells/`)
      brief ✅ CSV ✅ — PTHrP+ epSSCs. Schrier 2006 (>95% → <10% proliferation),
      Chu 2025 human confirmation, Trompet 2024 Hedgehog bead. Pairs directly
      with deck 1 — this is the cellular identity of its "finite resource".
- [ ] **Deck 5 — "Catch-up growth"** (`catch-up-growth/`) brief ✅ CSV ✅
      The reversible/irreversible split (Nilsson 2014) is the payload: slowed
      growth is recoverable, spent progenitors are not, and a growth chart
      can't tell you which happened.
- [ ] **Deck 6 — "Stimulants and the growth plate"** (`stimulants-and-growth/`)
      brief ✅ CSV ✅ — genuinely under-covered. ⚠️ **Slide 7 (do not stop
      prescribed medication) is non-negotiable.** If cutting for length, cut a
      mechanism slide instead.

## Next topics (not yet built)

Vault material exists for these; no brief or CSV written yet.

- [ ] **AAS accelerate skeletal maturation** — Stirling 1994 controlled trial:
      oxandrolone accelerated growth *and* skeletal maturation in peri-pubertal
      boys. The tradeoff with real trial data, not animal models.
- [ ] **Aromatase inhibition in birds vs mammals** — vault comparison page
      exists. Genuinely novel angle nobody in this niche covers.
- [ ] **Sox9 / Runx2 / Dlx5** — the transcription-factor network governing
      chondrocyte maturation. Pairs with `resting-zone-stem-cells`.
- [ ] **Craniofacial / mandibular growth** — audience clearly wants it (video 4
      in style refs). Vault sources are AAS-in-rats studies, so the honest
      version is "what the animal literature actually shows", not a protocol.

## Library / tooling

- [ ] Resolve the 235 UNKNOWN licences — cross-check DOIs against Unpaywall or
      Crossref; many are OA with the licence only on the journal landing page.
- [ ] Build OA figure catalogues per topic with `scripts/find-oa-figures.py`:
      androgens+growth plate, estrogen/aromatase, GH/IGF-1, skeletal stem cells
- [ ] Standing figure library at `content/_figures/` — cleared assets, reusable
      across decks, each with its attribution line

## Why the loop was stopped 2026-09-03

Not because the work ran out — because the remaining work splits into two
piles, and neither is worth autonomous cycles right now:

1. **Blocked on you.** Every deck is gated on the Canva template existing.
2. **Speculative volume.** Building decks 2–4 before deck 1 has been through
   Canva once risks being wrong four times instead of once. If the CSV column
   structure needs changing, better to learn that on one deck.

Unblock either and this restarts in one message. The library work (235 unknown
licences, per-topic figure catalogues) is real but not the bottleneck — 59
cleared papers and 164 figures already exceed what the next several decks need.

## Open questions for you

- Canva template: build the 4-layout family so Bulk Create has something to
  fill? Blocks every deck until it exists.
- Do you want the wiki page written for each topic too, or scripts only?

---

## Reference

- Format + algorithm: [[tiktok-format-research]]
- Figure licensing: [[figure-licensing-audit]]
- Pipeline guide: `~/Documents/Claude/Prompts/tiktok-slideshow-pipeline.md`
- `python3 scripts/find-oa-figures.py "<topic>" --reviews`
- `python3 scripts/scan-figure-licences.py`

## Decks 7-8 (added late session)

- [ ] **aromatase-inhibitor-monitoring-gap** — COMPLETE (brief/visual/video/CSV)
      The most useful thing this channel could say about AIs: paediatric
      height studies don't screen for the sensory/cognitive outcomes oncology
      treats as standard monitoring. Bouliari's cohort had zero cognitive
      endpoints over ~25 months. "No reported side effects" ≠ "no side effects".
- [ ] **fgfr3-overgrowth** — COMPLETE (brief/visual/video/CSV)
      Hook is a 2024 case report: child on a pan-FGFR inhibitor for a tumour
      developed skeletal *overgrowth* — the mechanism confirmed by accident, in
      a human, in reverse. Then the three drug strategies (TYRA-300,
      infigratinib, and meclizine, a repurposed motion-sickness pill).
      ⚠️ Slide 8 framing is required: these treat a genetic dysplasia in people
      who have it, not a height pathway for people who don't.
      Cross-link found: PMC paper on FGFR3 disrupting *resting zone chondrocyte
      turnover* via CREB — ties this deck directly to `resting-zone-stem-cells`.
