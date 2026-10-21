---
type: meta
title: "Wiki Index"
updated: 2026-10-21
tags:
  - meta
  - index
status: evergreen
related:
  - "[[overview]]"
  - "[[log]]"
  - "[[hot]]"
  - "[[dashboard]]"
  - "[[Wiki Map]]"
  - "[[concepts/_index]]"
  - "[[entities/_index]]"
  - "[[sources/_index]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Hot Cache]]"
  - "[[Compounding Knowledge]]"
  - "[[Andrej Karpathy]]"
---

# Wiki Index

Last updated: 2026-09-11 | Total pages: 500+ | Sources ingested: 417

Navigation: [[overview]] | [[log]] | [[hot]] | [[dashboard]] | [[Wiki Map]] | [[getting-started]]

---

## Knowledge engine layers (added 2026-09-11)

The vault now separates **receipts** from **synthesis** from **what the niche merely believes**.

| Folder | Holds | Tier | Count |
|---|---|---|---|
| `sources/` | one page per study — a receipt | A-C | 408 |
| `concepts/` | synthesis, enumerated reviews | varies | 25 |
| `pathways/` | one page per signalling cascade | varies | 1 |
| `entities/` | compound and hormone monographs | varies | 11 |
| `claims/` | one page per contested claim, with a verdict | varies | 7 |
| `quotes/` | verbatim extracts, filed by topic | inherits | 3 |
| `figures/` | study images, filed by what they display | — | see `figures/_index` |
| `creators/` | what competitor accounts assert | **X** | 15 |
| `decks/` | one page per post, closing the loop | — | 6 |

### Evidence tiers
`A` human RCT/meta · `B` human observational · `C` animal or in-vitro ·
`D` mechanistic inference · **`X` creator assertion — never a source of fact**

Anything in `creators/` is tier X by construction. It records what 234 competitor posts
across 5.9M views claim, so those claims can be checked, not repeated.

### Start here
- [[Account Briefs]] — the four accounts and what each carries
- [[Growth Factors of the Growth Plate]] — the enumerated-review pattern
- [[GH-IGF-1 Axis]] — the pathway pattern
- [[plate-hypoxia-implies-intervention]] — the claim pattern, on a contested claim
- `wiki/_templates/` — seven page templates so new pages stay comparable

---

## Concepts

- [[DHT Esters — Dosing and Concentrations]] — every published dose and the only two mg/mL concentrations for DHT heptanoate/enanthate and DHT propionate; ester mass-fraction arithmetic (status: developing)
- [[LLM Wiki Pattern]] — the pattern for building persistent, compounding knowledge bases using LLMs (status: mature)
- [[Hot Cache]] — ~500-word session context file, updated after every ingest and session (status: mature)
- [[Compounding Knowledge]] — why wiki knowledge grows more valuable over time, unlike RAG (status: mature)
- [[cherry-picks]] — prioritized feature backlog from ecosystem research; 13 features to add to claude-obsidian (status: current)
- [[SVG Diagram Style Guide]] — canonical visual style for all diagrams: Space Grotesk, #0A0A0A dark theme, #E07850 accent, full design tokens (status: evergreen)
- [[Pro Hub Challenge]] — community challenge pattern for building claude-seo/claude-blog extensions; first challenge produced 6 submissions, 5 integrated in v1.9.0 (status: evergreen)
- [[Semantic Topic Clustering]] — SERP-based keyword grouping replacing paid tools; hub-spoke architecture with interactive visualization (status: evergreen)
- [[Search Experience Optimization]] — "read SERPs backwards" methodology for page-type mismatch detection and persona scoring (status: evergreen)
- [[SEO Drift Monitoring]] — "git for SEO" baseline/diff/track with 17 comparison rules and SQLite persistence (status: evergreen)
- [[DragonScale Memory]] — memory-layer spec inspired by the Heighway dragon curve; fold operator, deterministic page addresses, semantic tiling, boundary-first autoresearch (status: shipped v0.4, all four mechanisms opt-in)
- [[Persistent Wiki Artifact]]: durable Markdown page as the LLM's memory object, distinct from ephemeral chat turns (status: developing)
- [[Source-First Synthesis]]: provenance discipline; raw sources stay immutable while the wiki layer is synthesized and cited (status: developing)
- [[Query-Time Retrieval]]: wiki query path synthesizes with citations; complementary to Obsidian's in-vault search (status: developing)
- [[Androgens and Energy Expenditure]] — androgens raise TDEE via added lean tissue, not thermogenesis; the sign of the REE response flips with baseline catabolic state (status: developing)
- [[Honey Hypoglycemic Mechanism]] — how honey's fructose/glucose composition, GI, PTP1B inhibition, and antioxidants may affect blood glucose (status: developing)
- [[Honey in Diabetic Wound Healing]] — honey's antimicrobial and tissue-regenerative role in diabetic wound care (status: developing)
- [[Honey and Bone Metabolism]] — honey (esp. Tualang honey) as an osteoporosis-prevention agent; 9-source cluster (status: developing)
- [[Honey Composition and Bioactivity]] — honey's phytochemistry; raw vs. processed honey differences (status: developing)
- [[Honey Microbiome]] — bacterial/fungal communities naturally present in raw honey (status: developing)
- [[Epiphyseal Fusion Mechanisms]] — the four competing cellular theories of growth plate closure (status: developing)
- [[Molecular Regulators of Growth Plate Chondrocyte Maturation]] — Sox9/Dlx5/Runx2 transcription-factor network for chondrocyte maturation (status: developing)
- [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]] — PTHrP+ resting-zone stem cell cluster (Trompet, Orikasa, Chu, Marchan-Alvarez), tied to Nilsson & Baron's finite-capacity model (status: developing)

**Vocabulary** (`concepts/vocabulary/`): [[Aromatase]], [[Androgen Receptor (AR)]], [[Dihydrotestosterone (DHT)]], [[Estrogen Receptor (ER)]], [[5-Alpha-Reductase]], [[Sox9]], [[Runx2]], [[Growth Hormone-IGF-1 Axis]], [[Testosterone]], [[PTHrP-Ihh Feedback Loop]], [[GPER-1 (GPR30)]], [[Kartogenin]], [[FGFR3]], [[OPG-RANKL Axis]], [[HDAC (Histone Deacetylases) in Chondrocytes]], [[cAMP Signaling in Chondrocytes and Osteoblasts]], [[Osteolectin]], [[Catecholamines and Beta2-Adrenergic Receptor]] — each lists every source mentioning the term and how

---

## Entities

- [[Andrej Karpathy]] — AI researcher, creator of the LLM Wiki pattern, former Tesla AI director (status: developing)
- [[Ar9av-obsidian-wiki]] — multi-agent compatible LLM Wiki plugin; delta tracking manifest (status: current)
- [[Nexus-claudesidian-mcp]] — native Obsidian plugin + MCP bridge; workspace memory, task management (status: current)
- [[ballred-obsidian-claude-pkm]] — goal cascade PKM; auto-commit hooks, /adopt command (status: current)
- [[rvk7895-llm-knowledge-bases]] — 3-depth query system, Marp slides, parallel deep research (status: current)
- [[kepano-obsidian-skills]] — official skills from Obsidian creator; defuddle, obsidian-bases (status: current)
- [[Claudian-YishenTu]] — native Obsidian plugin embedding Claude Code; plan mode, @mention (status: current)
- [[Claude SEO]] — Tier 4 Claude Code skill for SEO analysis; 23 skills, 17 agents, 30 scripts at v1.9.0 (status: evergreen)
- [[Honey]] — natural sweetener; subject of antidiabetic, bone-metabolism, and wound-healing research (status: developing)
- [[Tualang Honey]] — Malaysian wild multi-floral honey; most-studied variety in the bone-metabolism cluster (status: current)

---

## Sources

- [[claude-obsidian-ecosystem-research]] — 2026-04-08 | web research across 16+ repos | 8 wiki pages created
- [[Honey-and-Diabetes|Honey and Diabetes]] — 2026-07-26 | Bobiş et al. 2018 review paper | 6 wiki pages created
- [[Honey-PTP1B-Insulin-Signaling|Honey Inhibits PTP1B]] — 2026-07-26 | Lori et al. 2019
- [[Honey-vs-Glucose-Fructose-Solution|Honey vs. Matched Sugar Solution]] — 2026-07-26 | Münstedt et al. 2008
- [[Honey-Metabolic-Effects-Type2-Diabetics-1988|Metabolic Effects in Type II Diabetics]] — 2026-07-26 | Katsilambros et al. 1988
- [[Honey-Jumping-Exercise-Bone-Gonadotropins|Honey + Jumping Exercise on Bone/Gonadotropins]] — 2026-07-26 | Mosavat et al. 2014
- [[Honey-Exercise-Antioxidant-Bone-Metabolism|Honey + Exercise on Bone/Antioxidant Status]] — 2026-07-26 | Tavafzadeh et al. 2015
- [[Honey-Aerobic-Dance-Bone-Turnover|Honey + Aerobic Dance on Bone Turnover]] — 2026-07-26 | Ooi et al. 2011
- [[Tualang-Honey-Bone-Metabolism-Postmenopausal-Review|Tualang Honey, Postmenopausal Bone (review)]] — 2026-07-26 | Mohd Effendy et al. 2012
- [[Honey-Bone-Health-Review-2019|Honey and Bone Health (review)]] — 2026-07-26 | Kamaruzzaman et al. 2019
- [[Tualang-Honey-Bone-Structure-Ovariectomized-Rats|Tualang Honey, Ovariectomized Rat Bone Structure]] — 2026-07-26 | Zaid et al. 2012
- [[Honey-Hydroxyapatite-Bone-Healing|Honey + Hydroxyapatite Bone Healing]] — 2026-07-26 | Bigham-Sadegh et al. 2018
- [[Biocement-Honey-Composites|Biocement/Honey Composites]] — 2026-07-26 | Medvecky et al. 2023
- [[Honey-Bone-Metabolism-Female-Athletes-Thesis|Honey and Bone in Female Athletes (PhD thesis)]] — 2026-07-26 | Ahmad 2017
- [[Honey-Nutrition-Health-Review-2008|Honey for Nutrition and Health (review)]] — 2026-07-26 | Bogdanov et al. 2008
- [[Raw-vs-Regular-Honey-Nigeria|Raw vs. Regular Honey (Nigeria)]] — 2026-07-26 | Edo et al. 2022
- [[Honey-Microbiome-Analysis|Microbiome Analysis of Raw Honey]] — 2026-07-26 | Xiong et al. 2023

Endocrinology domain sources (281 in-domain + 98 unrelated as of 2026-07-27) are no longer individually listed here — this list grew past 170 entries and became unmaintainable. See [[Endocrinology]] domain page (frontmatter `sources:` list) or `sources/_index.md` for the full, current list.

---

## Questions

- [[How does the LLM Wiki pattern work]] — how the pattern works and why it outperforms RAG at human scale (status: developing)
- [[Research Hormonal Effects on TDEE]] — how much androgens, thyroid hormone and GH actually raise daily energy expenditure, per compound, with the gaps named (status: developing)

---

## Comparisons

- [[Wiki vs RAG]] — when to use a wiki knowledge base versus RAG; verdict: wiki wins at <1000 pages
- [[claude-obsidian-ecosystem]] — feature matrix of 16+ Claude+Obsidian projects; where claude-obsidian wins and gaps
- [[Aromatase Across Tissues]] — same enzyme (aromatase), different consequences in bone, brain, cardiovascular tissue
- [[Estrogen vs Androgen in Male Bone Health]] — clinical evidence favors estrogen/aromatization; cell-culture evidence shows a real direct-androgen mechanism too
- [[Aromatase Inhibitors - Height Therapy vs Neuro-Sensory Side Effects]] — same drug class, deliberate use for height vs. incidental brain effects
- [[Aromatase Inhibition and Bone - Mammals vs Egg-Laying Birds]] — same drug mechanism, opposite bone outcome by species
- [[Three Estrogen Receptor Mechanisms in the Growth Plate]] — ERα/AF-1-independent closure vs. GPER-1 proliferation vs. ligand-independent ERα mechanotransduction; three distinct systems, one receptor family name
- [[Three Achondroplasia Drug Strategies - FGFR3 Inhibition vs Repurposing]] — TYRA-300 and infigratinib (novel selective inhibitors) vs. meclizine (repurposed antihistamine); a pan-FGFR-inhibitor overgrowth case validates the shared mechanism
- [[Anabolic Steroid Effects Across Craniofacial Sites]] — nandrolone/DHT/estradiol alter craniofacial growth at every site studied (skull vault, mandible, TMJ), not an isolated finding

---

## References

Reference ledgers live in `wiki/references/`: large extracted tables that other pages cite rather than restate.

- [[Molecuro Research Compound Catalogue]] - the full Molecuro commercial catalogue as of 2026-10-21: 479 products, 15 compound classes, grouped by class and physical form. Vendor listing copy: a record of what is sold, not evidence about any compound.
- [[DHT Propionate Animal Dose Ledger]] - every DHT propionate dosing regimen extractable from PubMed abstracts (~50 regimens)

---

## Decisions

- [[2026-04-14-community-cta-rollout]] - Skool community CTA footer added to 6 skill repos with per-tool frequency rules (status: active)
- [[2026-04-15-slides-and-release-session]] - Claude SEO v1.9.0 slides (15-slide HTML deck) + GitHub release v1.9.0 with PDF asset (status: complete)
- [[2026-04-15-release-report-session]] - Claude SEO v1.9.0 Release Report PDF: dark theme, 13 pages, WeasyPrint layout fixes, Challenge v2 added (status: complete)
- [[2026-04-14-claude-seo-v190-session]] - Claude SEO v1.9.0 Pro Hub Challenge integration: 5 submissions, 4 new skills, 4 review rounds, cybersecurity audit (status: complete)

---

## Domains

- [[Health and Nutrition]] — honey research: diabetes/glycemic effects, bone metabolism, composition, microbiome (status: developing, 16 sources)
- [[Endocrinology]] — steroid hormone biology: growth plates, aromatase, androgens vs. estrogen, oxidative stress (status: developing, 281 sources + 98 unrelated, 4 concepts, 18 vocabulary, 7 comparisons)
