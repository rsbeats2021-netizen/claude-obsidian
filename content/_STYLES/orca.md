# Orca — the compound monograph account

## Style
`scripts/render-classic.py content/<deck> --style clinical`

White package-insert look: black Archivo headline, red section rule, one blue
keyword accent. Replaced the dark `orca` style, which was rejected. Three
alternatives were built and are still available: `clinical`, `dossier` (warm
paper, serif) and `signal` (cool grey, condensed).

Old dark style, kept but unused:

Near-black `#0B0E13`, white type, ice accent `#3BC9DB`. Anton headline. Deliberately
the opposite of restingzone's light-grey editorial look, and it reads as a clinical
dossier rather than a magazine, which suits a compound reference.

A spec strip sits above the headline on slide 1 only, read from `00-spec.txt`:
`CLASS · ROUTE · EVIDENCE LEVEL`. That line sets expectations before anyone reads a
claim, and it is where "no human height trial" gets said out loud.

### Section colour-coding
The subhead carries a section tag and the renderer colours it automatically:

| tag | colour |
|---|---|
| `BENEFIT ·` / `EVIDENCE FOR ·` | green |
| `DOWNSIDE ·` / `RISK ·` / `THE COST ·` | red |
| `COUNTER ·` / `MITIGATION ·` | ice |
| `LIMIT ·` / `UNKNOWN ·` | amber |

So a viewer can see the shape of the argument from the colours alone while
scrolling, before reading a word.

## The monograph format, 11-13 slides

1. **Cover** — compound name, class, one-line framing. Spec strip above it.
2. **What it actually is** — mechanism, in plain language, with the receptor named
3-4. **BENEFIT** — the strongest evidence, with study, design and numbers
5-6. **DOWNSIDE** — the real cost, with numbers, not hedged
7-8. **COUNTER** — what offsets it, *only where the evidence supports something*
9. **LIMIT** — what is not known, what population the data came from
10. **Verdict** — the honest summary, including when the answer is "do not"
11. **Outro** — DM for source

## Rules specific to this account

- **State the dose.** Whatever dose the study used, say it, because it is part of
  the evidence. Where a dose is community practice rather than trial-derived, say
  which it is — that is a sourcing distinction, not a disclaimer.
- **If there is no evidence-based counter, say so on the counter slide.** The
  Tresiba monograph says plainly that no mitigation exists for that use. A format
  that always produces a reassuring answer is not a monograph, it is marketing.
- **Compliance, disclaimers and advertising review are the account owner's, not
  this document's.** Nothing here should be softened for that reason. Accuracy
  against the cited source is a separate thing and stays.
- **The spec strip must state the evidence level honestly**, including
  "NO HUMAN HEIGHT TRIAL" where that is the case.
- Every number still needs a verbatim quote in `07-claims.md`, same as restingzone.

## Video
`03-video.md` per compound, generated from the slides: cover, mechanism, two
benefits, two downsides, counters, limits, verdict. Currently running 90-110s,
which is above the 45-90s band that performs best in the scrape. Worth cutting the
second benefit and second downside for the video version.

## Video scripts

`scripts/make-video.py content/<deck>` writes `03-video.md`, targeting the
45-90s band from `_style-analysis/FINDINGS.md` (15-30s is the worst performer).

It selects rather than transcribes. Reading a 13-slide post aloud at 178 wpm
lands near 110s, outside the band, so the generator scores every slide for
measured values, `==emphasis==`, and section tag, then keeps the hook, the
strongest data, the turn, and the takeaway in deck order.

Two things it had to learn:
- **Sentence choice, not sentence order.** Taking the first two sentences kept
  "Exercise alone gave an AUC of 292.6" and dropped "after pyridostigmine gave
  587.3", which is the half that matters. It now scores sentences for data.
- **Back-references need their setup.** A top-scoring sentence opening with
  "The same..." or "It..." is meaningless alone, so the preceding sentence is
  pulled in with it.
