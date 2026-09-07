# Style analysis — 1,951 posts, 14 accounts

Scraped data included full TikTok metadata, so this is measured rather than
guessed. No need for me to predict which performed best.

---

## 1. Format: video beats slideshow, and I told you the opposite

I previously said carousels get roughly 5x the reach of video, based on 2026
marketing blog posts. **That is wrong for this niche.**

| | n | median plays |
|---|---|---|
| Video | 822 | **19,050** |
| Slideshow | 448 | 7,106 |

Video wins in 5 of the 6 accounts that post both. Save rate too: 13.9 per 1,000
plays for video against 6.2 for slideshows.

Generic platform advice did not survive contact with this niche's actual data.
Treat my earlier format claim as retracted.

## 2. But slide count changes the picture completely

The slideshow median is dragged down by 321 posts with 1-3 slides. Longer decks
behave differently:

| Slides | median plays | saves per 1,000 plays |
|---|---|---|
| 1-3 | 4,610 | 4.1 |
| 4-7 | 8,474 | 18.7 |
| 8-11 | 14,400 | 28.9 |
| 12+ | 22,500 | **33.7** |

Slideshows of 10+ slides median **20,400 plays**, which beats the all-video
median of 15,850.

**Caveat, stated honestly:** the within-account test for this is underpowered.
Only two accounts have enough long and short decks to compare, and they
disagree (bpedpremed 1.5x favouring long, doctor.morph 0.7x favouring short).
So the plays effect is partly confounded by which accounts happen to make long
decks. The **save rate** trend is much cleaner: it is per-post normalised and
rises monotonically across all four buckets, 4.1 to 33.7.

**Practical read:** your 9-10 slide decks sit mid-table. Going to 12-15 is
supported by the save data, weakly by the plays data, and costs nothing.

## 3. Video length

| Duration | n | median plays |
|---|---|---|
| 0-15s | 184 | 14,500 |
| 15-30s | 139 | 9,975 |
| 30-45s | 163 | 15,100 |
| **45-60s** | 171 | **19,700** |
| **60-90s** | 307 | **19,600** |
| 90-180s | 445 | 14,700 |
| 180s+ | 35 | 13,500 |

45 to 90 seconds is the band. 15-30s is the worst performing bucket, which
kills the "shorter is always better" assumption. My scripts target 60s, which
is correct.

## 4. Writing style, from the top performers

### rpo3212, 304,900 plays, 15,428 saves, 9 slides

Slide 1 is **pure promise, zero content**: "Want to learn how to grow taller
extremely quickly" / "NOT SURFACE LEVEL" / arrow. It sells the deck, it does not
start it. Mine always open with a claim.

Body slides are **stacked short declaratives**, each its own block with
whitespace between:

> ATP is energy and cells cannot function without it
> Without sufficient ATP you will have 0 height growth
> The growth plate is avascular which means it has no blood vessels and has low ATP compared to other cells
> This explains why height growth takes so long

Note: second person ("you will have"), absolute ("0 height growth"), jargon
defined inline ("avascular which means it has no blood vessels"), and **no
connectors at all** between statements. They just stack.

### doctor.morph, 185,600 plays, bonesmashing mechanism

Conversational opener that admits complexity then narrows:

> So there are a lot of mechanisms and pathways that play into this but lets go
> with the main one.

Then the mechanism as an explicit causal chain, with terms defined as they
appear:

> Bones have osteocytes which are cells that can convert mechanical stressors
> into cellular signals by activating sensors. When osteocytes sense a
> mechanical stressor they secrete nitric oxide and PGE2 with the goal of
> blocking SOST and sclerostin. Lowering SOST and sclerostin results in more
> Wnt which is a pathway very anabolic for bone...

Closes absolute: "Without SOST and sclerostin downregulation there is no bone
growth from a mechanical stressor."

## 5. Devices worth stealing

- **Colour-coded keywords.** Technical terms in blue and red inside black body
  text. You can skim only the coloured words and still get the mechanism. This
  is the single biggest readability difference from my decks.
- **Screenshot the actual paper.** "STUDY" with an arrow pointing at the
  journal header. Receipts as a visual, not a citation line.
- **Section headers.** "THE MECHANISM" as a slide label.
- **Slide 1 sells, it does not inform.**
- **Inline definitions.** "osteocytes which are cells that..." rather than
  assuming or avoiding the term.

## 6. What I do that they do not

| Me | Them |
|---|---|
| Third person, abstract | Second person, "you" |
| Hedged: "may", "suggests" | Absolute: "there is no bone growth" |
| Connectors: "which is why" x18 | Statements stacked, no connectors |
| Slide 1 makes a claim | Slide 1 makes a promise |
| Citation as small footer text | Screenshot of the paper itself |
| Uniform body text | Colour-coded key terms |
| 9-10 slides | 12-19 slides on the best performers |

## 7. Topic finding

The highest performing posts overall are facial aesthetics, not endocrinology:
maxilla, zygomatic bone, skin, eye colour, bone smashing. Growth plate biology
performs well but the ceiling is lower. `rpo3212`'s two 1M+ posts are both
"most important facial bone".

## 8. Mechanism I missed

doctor.morph's bonesmashing deck cites Robling et al. 2008, JBC: *Mechanical
Stimulation of Bone in Vivo Reduces Osteocyte Expression of Sost/Sclerostin*.
Mechanical load lowers sclerostin, which raises Wnt signalling, which is
anabolic for bone.

That is a real, citable pathway for load-induced bone formation and it is
stronger backing for the loading argument than the ERα mechanotransduction
material I built `mechanical-loading-bone` from. Worth adding.
