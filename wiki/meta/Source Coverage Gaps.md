---
type: meta
title: "Source coverage gaps"
generated_by: "scripts/coverage-gaps.py"
gaps: 17
created: 2026-09-11
updated: 2026-09-11
tags: [meta, pipeline-d, acquisition]
---

# Source coverage gaps

Terms the competitor corpus discusses that `wiki/sources/` cannot back up.
Ranked by corpus reach. Regenerate any time with:

```
.venv-research/bin/python scripts/coverage-gaps.py
```

**Closed since the first run:** Minoxidil (34 posts, 1.53M views) →
[[messenger-2004-brjdermatol--minoxidil-mechanisms]] + [[Minoxidil]].

| Term | Posts | Views | Account | Why it matters | Start with |
|---|---|---|---|---|---|
| **Retinoid / tretinoin** | 24 | 1,274,436 | Skin & hair | Photoageing reversal RCTs. Tretinoin is one of very few tier-A topicals; the corpus discusses it without any of the trial data. | Kligman photoaging trials; Mukherjee 2006 Clin Interv Aging review |
| **Myostatin** | 10 | 1,014,136 | Harm reduction | Follistatin/myostatin inhibition is heavily hyped. Human data is thin and that gap is the story. | Myostatin inhibitor human trials — most failed endpoints |
| **VEGF** | 12 | 627,315 | Growth | Already appears in three vault pages as a node but has no source. Links the avascular plate to ossification. | Gerber 1999 Nat Med — VEGF and endochondral ossification |
| **CNP / NPR-B** | 14 | 357,087 | Growth | **Highest-value gap.** Vosoritide is tier-A human evidence in achondroplasia — the growth-factor family's only translational win. | Savarirayan 2020 Lancet — vosoritide phase 3 |
| **Sclerostin** | 10 | 345,487 | Growth | Romosozumab is approved; the Wnt/sclerostin axis is the best-evidenced bone anabolic pathway there is. | Cosman 2016 NEJM — romosozumab FRAME trial |
| **HIF-1α** | 6 | 322,800 | Growth | Now partly covered by [[schipani-2001-genes-dev--hif1a-chondrocyte-survival]]. Needs the broader HIF biology. | Semenza reviews; Schipani 2001 already filed |
| **Melatonin** | 13 | 277,374 | Cognition | Sleep is the corpus whitespace and melatonin is its most-discussed compound with zero backing. | Dose-response and phase-shift literature; Zhdanova dose work |
| **GHK-Cu** | 12 | 185,460 | Skin & hair | 12 posts, 185k views, almost entirely in-vitro evidence. A tier-honesty piece writes itself. | Pickart reviews — note the author's commercial interest |
| **Orexin** | 7 | 128,799 | Cognition | Mechanistic backbone for wake/sleep content; orexin antagonists are an approved drug class. | Suvorexant/lemborexant trials |
| **Odanacatib** | 4 | 124,300 | Growth | Cathepsin K inhibitor, withdrawn after stroke signal. A good 'why promising drugs die' piece. | LOFT trial and its termination |
| **CJC-1295** | 3 | 85,400 | Harm reduction | GHRH analogue. Human data minimal; peptide category is the corpus's biggest opening. | Teichman 2006 JCEM |
| **Creatine** | 7 | 79,599 | Cognition | Hundreds of human RCTs exist and the vault has none of them. Easiest gap to close well. | Rae 2003; Avgerinos 2018 meta-analysis on cognition |
| **SARMs** | 2 | 66,600 | Harm reduction | Low corpus volume but high harm relevance. | Ostarine/enobosarm trial data and FDA warnings |
| **TB-500 / thymosin** | 2 | 55,800 | Harm reduction | Essentially no human evidence. That absence is the content. | Thymosin beta-4 trial landscape |
| **Semaglutide / GLP-1** | 5 | 44,155 | Harm reduction | Adjacent and growing fast; worth a position before it saturates. | STEP trials |
| **PEMF** | 1 | 3,488 | Growth | One post, but it appeared in the corpus attached to a growth-plate claim. | PEMF bone healing meta-analyses |

## How to close one
1. Find the paper. Prefer **PubMed Central** or the publisher's open-access version — free and legal.
2. Create a source page with the DOI as the filename stem, `evidence_tier`, and `key_claims`.
3. Pull 2-4 verbatim lines into a `wiki/quotes/` file with tiers attached.
4. Write or extend the `entities/` monograph or `pathways/` page.
5. Re-run the gap script; the term should drop off.

## Note on acquisition
A Sci-Hub MCP is installed in this workspace. It distributes copyrighted papers without
authorisation, so it is not used by this pipeline. PMC, publisher open access, preprint
servers and institutional access cover most of the list above.

## Highest value first
**CNP / NPR-B.** It is the only member of [[Growth Factors of the Growth Plate]] besides FGFR3
with tier-A human evidence, it sits under the biggest account, and the vault currently has nothing.
