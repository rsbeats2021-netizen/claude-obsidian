# Slideshow — "Fusion is the receipt, not the cause"

10 slides · 1080x1920 · Bulk Create input: **`04-slides.csv`**

> **`04-slides.csv` is the single source of truth for slide copy.** This file
> holds only what the CSV can't: visual direction, structure, and design notes.
> Copy is deliberately NOT duplicated here — the two drifted apart once already.

## CSV column mapping

Matches the visual language already in your decks:

| Column | Design element | Styling |
|---|---|---|
| `headline` | big black condensed display line | regular |
| `subhead` | blue all-caps line completing the sentence | regular |
| `body` | centred body copy | regular |
| `punch` | **separate text element below body** | **bold — set once in the template** |
| `tag` | small footer — citation or tier flag | small |

### Why `punch` is its own element

Bulk Create carries plain text, so **inline bold on individual words does not
survive regeneration** — element-level styling does. Putting the payoff line in
its own permanently-bold element means the emphasis is baked into the template
and never has to be re-applied. Without this you'd hand-bold ten slides on every
deck, forever.

Any remaining word-level emphasis (e.g. the young/old ↔ fast/slow contrast pair
on slide 3) is still manual — but that's one line, not a whole slide.

### Size the boxes against these ceilings

| Element | Longest | Which slide |
|---|---|---|
| `body` | 263 chars / 44 words | 3 |
| `punch` | 127 chars / 23 words | 8 |
| `subhead` | 26 chars | 9 |

Size against those and every slide fits by definition.

## Structure

| # | Beat | Visual direction |
|---|---|---|
| 1 | Hook — causality is reversed | Growth plate cross-section, causal arrow flipping. **Sparse slide** — competing with autoplay video to stop a scroll. |
| 2 | Conflict — fusion treated as a deadline | Text-led. Maybe a crossed-out calendar/clock. |
| 3 | **The transplant experiment** | **Hero slide.** Two-panel: young plate → old animal = fast; old plate → young animal = slow. Redraw needed — no OA figure exists. Spend the design time here; this is the slide that carries the argument. |
| 4 | The clock is inside the plate | Candidate: PMC12525321 Fig 3 (stem-cell niche schematic, CC-BY) |
| 5 | Finite cell divisions | Candidate: `fig-zones-hallett2019-CCBY.png` — zones labelled, resting zone highlighted |
| 6 | Growth slows years before fusion | Simple decline curve with fusion marked late. Redraw. |
| 7 | Catch-up growth — the proof | Curve dipping then overshooting baseline. Redraw. Biggest "wait, what?" beat in the deck. |
| 8 | Real target is proliferative capacity | Text-led. |
| 9 | Caveat — mechanism unresolved (Tier 3) | Four theory labels, none ticked. |
| 10 | CTA | Brand slide. |

## Design notes

- **Density is intentional.** Body slides run 40–60 words. Reverse swipes are a
  positive ranking signal, so slides worth re-reading help. Do not thin these
  out — see `wiki/references/tiktok-format-research.md`.
- **Every slide ends on an open loop.** Check this survives editing; it's what
  drives swipe-through, which is the metric the carousel algorithm ranks on.
- **Slide 7 is the retention save.** If people are dropping before the end,
  test moving catch-up growth earlier — it's the most surprising beat and it
  currently sits late.
- Attribution required on any slide using the Hallett figure:
  `Hallett et al. 2019, Int J Mol Sci — CC BY 4.0`

## Related
- `01-research.md` — tier-tagged brief
- `03-video.md` — 60s spoken version
- `03-images/manifest.md` — licence status per asset
