---
type: meta
title: "Operation Log"
updated: 2026-10-21
tags:
  - meta
  - log
status: evergreen
related:
  - "[[index]]"
  - "[[hot]]"
  - "[[overview]]"
  - "[[sources/_index]]"
---

# Operation Log

Navigation: [[index]] | [[hot]] | [[overview]]

Append-only. New entries go at the TOP. Never edit past entries.

## 2026-10-21 (save): catalogue moved out to the Molecuro vault

- The catalogue page filed here earlier today now lives at `~/Documents/Molecuro/Vault/Molecuro/wiki/sources/Molecuro Research Compound Catalogue.md`. This path keeps a pointer stub so the index entry and the earlier log entry do not dangle.
- **Why**: this checkout is the product source and the engine refuses to treat it as a vault, so the catalogue was only ever a docs edit here. In the Molecuro vault it is a `source` page with a ledger record (`src-e59aa61e35da00bde6b0`, origin `https://molecuro.com/research`, authority official, refresh due 2026-11-21), and it sits with the content pipeline that reads it.
- Nothing else in this checkout referenced the catalogue. The DHT propionate ledger entry added to the index in the same breath stays.

## 2026-10-21 (save): Molecuro compound catalogue filed as a reference ledger

- Filed [[Molecuro Research Compound Catalogue]]: the whole Molecuro commercial catalogue as of 2026-10-21, **479 products** across two shop sections and 15 compound classes, grouped by class and then by physical form (vials, solutions, powders, capsules, tablets, softgels).
- Scope came from ten listing pages the user had printed to PDF (`~/Downloads/molecuro/`, outside the vault). **Those prints were incomplete**: 69 entries were lost at page breaks (DSIP, GHRP-2, GHRP-6, FOXO4-DRI and Follistatin-344 among the peptides alone) and the *Essential and herbal oils* class, 49 products, was never printed at all. Reconciled against the live listing pages the same day, so per-class counts now match the vendor's own stated totals: 72 peptides, 96 nootropic, 187 metabolic and longevity, 49 oils, 75 OTC.
- **Forms, counting every form a product is sold in**: 415 powders, 152 capsules, 71 lyophilised vials (70 of them peptides), 53 solutions, 17 tablets, 3 softgels. **There are no sprays** in the catalogue, and no ampoules, creams, gels, patches or pre-filled syringes. The filing request assumed sprays existed; they do not.
- **Not evidence.** Every field is vendor listing copy (class, form, price, formula), unchecked against any certificate of analysis, assay or regulatory record. The page opens with a callout saying so and makes no claim about what any compound does, so it has the standing the vault gives `creators/` (tier X): a commercial assertion kept so it can be checked, never a source of fact.
- Rows resolve at `https://molecuro.com/products/<slug>`; the slug is a column. Formula and molar mass are present on 205 of the 479 rows, only where the listing states them. Prices are the entry price plus the vendor's unit price, whose basis varies (per mg, g, kg, capsule, 100 capsules, softgel) and is reproduced unconverted.
- Produced outside the vault first, as the deliverable the user asked for: `~/Downloads/molecuro/Molecuro-catalogue-organised.md` and `molecuro-catalogue.csv` (one row per product, with resolvable URLs). The vault page is the same organisation in vault conventions.

## 2026-10-17 (gap-closing pass) — two of three DHT ester gaps closed

- **Weinbauer 1990 formulation recovered** (full text obtained). "32.7 mg DHTE ... i.e. 23.6 mg pure steroid, **dissolved in 1 ml sesame oil**" = **32.7 mg/mL ester, 23.6 mg/mL DHT-equivalent**, 1 mL IM. Experiment 2 used the same concentration at 2.1-3.2 mg/kg in rhesus.
- **The provenance line is the bigger find**: "The DHTE preparation was provided by the **World Health Organization** (Geneva) and **Dr G. Bialy (Contraceptive Development Branch**, Center for Population Research, **NICHD**, Bethesda)." DHT enanthate was therefore inside a formal male-contraceptive development programme. No human trial was ever published and nothing records what became of it — the gap is now better characterised rather than closed.
- **Pesomax strength found** in the Italian registry: **"PESOMAX IM 10F 2ML 15MG"**, ten 2 mL ampoules at 15 mg, **AIC 015012014**, Crinos SpA, class RR, ~EUR 1.76, status **revocato**. So ~7.5 mg/mL (per-mL figure is arithmetic on the Italian per-unit naming convention, which the listing does not spell out). Also corrects the widespread secondary-source claim that DHT propionate is "marketed in Italy" — the authorisation is revoked.
- **The concentration table goes from two figures to four**, spanning 40-fold for the heptanoate/enanthate alone: 190 mg/mL (clinical, solubility ceiling), 32.7 mg/mL (WHO/NICHD primate prep), 5.0 mg/mL (rodent), plus 7.5 mg/mL for the propionate. Weinbauer's 32.7 mg/mL sitting far under the 190 mg/mL ceiling in the *same vehicle* shows research concentrations were set by dose convenience, not solubility.
- **Coutts 1997 remains unreachable** and is now documented as such. Unpaywall reports `oa_status: green`, but its only location is `clinchem.org/content/43/11/2091.abstract` — the abstract page, not a deposited full text. A false positive; not on any mirror checked. The 1.32 mL injection volume stays an inference from the patent's 190 mg/mL.

## 2026-10-17 (verifier pass) — corrections to the DHT ester slice before commit

- Dispatched `agents/verifier.md` against the staged 13-page diff per CLAUDE.md. Verdict HOLD-FIX-FIRST: 0 BLOCKER, 4 HIGH, 9 MEDIUM, 6 LOW. All arithmetic it re-derived independently (mass fractions, DHT-equivalents, ng/dL conversions, injection volumes) checked out; the findings were internal-consistency and overclaim errors. Fixed before committing.
- **The substantive one**: I had explained the gap between the patent's 284 ng/dL and [[Keenan-1996-DHT-Heptanoate-GH-Binding-Protein]]'s 848 ng/dL as a trough-vs-peak sampling artefact. It is not — both are two-week post-injection samples after a 200 mg dose. The pages now present it as **unexplained by the sources**, with cumulative dosing (first vs third injection) and differing assays offered explicitly as my inference. Dropped the "monotonic" claim and the extrapolation that 300 mg q2wk "would be expected above 848 ng/dL".
- Second real error: the "200 mg q2–3wk" blood-DHT table mixed regimens. The 2- and 4-week values follow a **single 200 mg dose**; only the 16-week value is from the mixed 200/400 mg steady state. Relabelled per row.
- Also corrected: 848 ng/dL described as "within the 300–800 band" (it is above it); "highest regimen published" for 300 mg q2wk (it is the highest *monthly exposure*, ~650 vs ~570 mg/mo — 400 mg q3wk is the higher per-dose); "three oncology papers" against five listed PMIDs; "every human dose recovered" against three still unstated at source; four animal rows in the ledger-vs-concept cross-check (5α-reductase bioassay dose attributed to two papers that state none, PMID 6871034 filed under lordosis instead of calling/copulation, two ovariectomised-plus-estrogen studies mislabelled as PCOS models, a prenatal regimen attributed to guinea pig instead of sheep).
- Overclaim fixes: the closing synthesis is now explicitly marked as interpretation; "cleanest demonstration anywhere" and the programme-abandonment narrative are gone; the ledger's "aromatisation is the explanation" is attributed to the papers' own authors. Added a "literature report, not dosing guidance" callout and the patent's own failure rates (~1/5 poor absorption, ~1/3 incomplete regression). Patent page dropped to `confidence: medium` with the same-patients link to [[Eberle-1986-DHT-Heptanoate-Pubertal-Gynecomastia]] labelled as inference.
- **One verifier finding rejected**: it flagged CAS 855-22-1 for DHT propionate as possibly wrong, suggesting 1045-69-8. Checked against PubChem — 855-22-1 resolves to CID 13328, C22H34O3, MW 346.5, "Dihydrotestosterone propionate"; 1045-69-8 is testosterone acetate. Original was correct. CAS 33776-88-4 for the heptanoate also confirmed (CID 160230, C26H42O3, MW 402.6).
- Added [[Endocrinology]] and [[Dihydrotestosterone (DHT)]] links to all 11 source pages per the Carrascosa precedent. Zero dead wikilinks.

## 2026-10-17 (follow-up) — full-text recovery | the missing DHT heptanoate doses

- Closed the main gap from the deep dive earlier today. Unpaywall and OpenAlex confirmed all three Keenan papers are closed with no repository copies (1993 is cited 208×). Recovered [[Keenan-1993-DHT-Heptanoate-Pubertal-Growth]] and [[Keenan-1996-DHT-Heptanoate-GH-Binding-Protein]] full texts and extracted the dosing from the Methods sections the abstracts omit.
- **Growth-spurt regimen**: three IM injections one month apart, **100 mg for the first dose then 200 mg for the next two** (500 mg total, 360.7 mg DHT-equivalent). Protocol B of the 1996 paper used **80 mg/m² per dose monthly**; cumulative dose reported per patient as **320–500 mg/m²**.
- **Gynecomastia regimen (Keenan 1993 group C)**: **300 mg IM every 2 weeks for 3 months**, 1800 mg total — the highest DHT heptanoate regimen in the literature, above the patent's claimed 200–400 mg q2–3wk.
- **New study found while mining the 58 open-access citing papers**: [[Saad-2001-DHT-Heptanoate-Insulin-Sensitivity]] (Saad, Keenan et al., JCEM 2001, PMID 11600557) — **50 mg IM every 2 weeks × 4 months** in 10 Tanner I boys, under **FDA IND 29,139**. The lowest human DHT-hp dose published, and the only regulatory identifier in the whole record. Plasma DHT 0.36 → 10.8 nmol/L (313 ng/dL); estradiol stayed below 18 pmol/L in all ten; GH and IGF-1 unchanged; %BF 23.6→22.0; HDL 1.3→1.1 mmol/L.
- Built a dose-response table across all four human regimens, keyed to cumulative exposure and sample timing.
- Also recovered from Keenan 1993: **plasma estradiol was below assay sensitivity in every DHT-treated subject** while rising to 25.7 pmol/L on testosterone enanthate — the cleanest demonstration in the literature that DHT-hp delivers androgen with zero estrogen signal.
- Still open: Coutts 1997 vehicle/concentration; Weinbauer 1990 vehicle; *Pesomax* ampoule strength; no DHT ester contraception trial; what became of IND 29,139.

## 2026-10-17 — deep dive | DHT heptanoate/enanthate and DHT propionate: dosages and concentrations

- Method: PubMed E-utilities phrase sweep across 14 ester name variants (`"dihydrotestosterone heptanoate"`, `"DHT heptanoate"`, `"DHT-hp"`, `"dihydrotestosterone enanthate"`, `"dihydrotestosterone-enanthate"`, `"DHT enanthate"`, `"DHTE"`, `"androstanolone enanthate"`, `"stanolone enanthate"`, `"dihydrotestosterone propionate"`, `"DHT propionate"`, `"DHTP"`, `"androstanolone propionate"`, `"stanolone propionate"`); 154 unique PMIDs fetched and dose-extracted programmatically; patent full text scraped from Google Patents.
- Pages created: 13 (1 concept, 1 reference, 11 sources) — concept [[DHT Esters — Dosing and Concentrations]], reference [[DHT Propionate Animal Dose Ledger]], sources [[Keenan-1990-DHT-Heptanoate-Patent-US4956357]], [[Keenan-1987-DHT-Heptanoate-Pharmacokinetics]], [[Eberle-1986-DHT-Heptanoate-Pubertal-Gynecomastia]], [[Keenan-1993-DHT-Heptanoate-Pubertal-Growth]], [[Keenan-1996-DHT-Heptanoate-GH-Binding-Protein]], [[Coutts-1997-DHT-Heptanoate-Urinary-Profile]], [[Weinbauer-1990-TE-vs-DHT-Enanthate-Primates]], [[Yang-Yoon-1994-DHT-Enanthate-Mice]], [[Hanson-2020-DHT-Enanthate-Castrate-Rat-Hypertension]], [[Forti-1983-DHT-Propionate-Klinefelter]]
- **Only two mg/mL concentrations exist in the entire literature**: DHT heptanoate **190 mg/mL in sesame oil at 37 °C**, stated as the solubility ceiling (US 4,956,357), and DHT enanthate **5.0 mg/mL in 90% olive oil / 10% DMSO** for rodent s.c. dosing (Hanson 2020). Nothing for DHT propionate; *Pesomax* ampoule strength not recoverable from any English source.
- **Mass fractions**: heptanoate/enanthate 72.14% DHT, propionate 83.82% DHT. Independently confirmed by Weinbauer 1990's "32.7 mg DHT-enanthate, i.e. 23.6 mg of pure steroid" = 72.2%.
- **Human heptanoate doses**: 200 mg (escalated to 400 mg) IM q2-3wk × 16 wk for pubertal gynecomastia; 200 mg/month × 6 mo for hypogonadotrophic hypogonadism; 250 mg single dose in 6 healthy men (doping study). Plasma DHT 42 → 284 ng/dL at 2 wk; T → 29.5 ng/dL (near-castrate); 300-800 ng/dL across a further 10 adolescents; 703-848 ng/dL in the growth cohort.
- **Human propionate doses**: exactly one study, 100 mg IM daily × 4 days in 6 Klinefelter men. No PK study of DHT propionate in humans has ever been published.
- Asymmetry: the heptanoate/enanthate literature is 8 PubMed-indexed studies plus the patent family and one non-indexed paper, almost all human/primate clinical; the propionate literature is ~150 papers, almost all rodent reagent use. Full animal ledger filed separately.
- Gaps filed: dose not reported in Keenan 1993 and 1996 (the two papers that would say what DHT-hp dose drives a pubertal growth spurt — both paywalled); Coutts 1997 vehicle/concentration unstated; Weinbauer 1990 vehicle unreachable; no DHT ester contraception trial despite the patent claiming the use and the suppression data supporting it.
- Naming hazard recorded: "2α-methyl-dihydrotestosterone propionate" in the 1960s breast-cancer literature is **drostanolone propionate**, a different molecule; five PMIDs excluded on that basis.

## 2026-10-02 — autoresearch | Hormonal effects on TDEE (androgens, thyroid hormone, GH)

- Rounds: 2 | Searches: ~14 (Europe PMC REST + web) | Pages created: 12
- Sources: [[Welle-1992-Testosterone-BMR-Lean-Mass]], [[Bhasin-2001-Testosterone-Dose-Response-Fat-Free-Mass]], [[Santosa-2010-Sex-Steroid-Withdrawal-REE]], [[Bauman-2011-Testosterone-SCI-Resting-Energy-Expenditure]], [[Strawford-1999-Nandrolone-REE-Nitrogen-Balance]], [[Hunter-Vercoe-1987-Trenbolone-Fasting-Metabolic-Rate-Steers]], [[Oxandrolone-Burns-REE-Herndon-Porro]], [[Almeida-2023-Bodybuilder-Peak-Week-RMR]], [[GH-REE-Pasarica-2007-Burt-2008]], [[Thyroid-Hormone-REE-Hayashi-2020-Samuels-2018]]
- Concept: [[Androgens and Energy Expenditure]]
- Claim: [[trenbolone-raises-metabolic-rate]] — verdict **unsupported**
- Synthesis: [[Research Hormonal Effects on TDEE]]
- Key finding: anabolic androgens have no reproducible *direct* effect on energy expenditure — the TDEE gain is the resting cost of added lean tissue (~13 kcal/kg/day), giving roughly +45 to +103 kcal/day across 125-600 mg/week testosterone. Thyroid hormone is the only large lever (+58% over predicted REE in frank thyrotoxicosis) and GH is intermediate (+132 to +172 kcal/day). Direction of the REE response flips with baseline catabolic state: oxandrolone *lowers* REE in burn patients, trenbolone *lowers* fasting metabolic rate ~10% in steers, and supraphysiological doses did not prevent RMR falling in contest-prep bodybuilders.
- Gaps filed: no doubly-labelled-water TDEE measurement for any androgen; zero REE data for oxymetholone; zero human data of any kind for trenbolone or methyltrienolone; nothing above 600 mg/week testosterone equivalent.

---

## 2026-07-27 — Consolidated everything not fully analyzed (skipped files + duplicates) back into the queue, sorted by type

User asked directly whether every study had been gone over, prompting a precise accounting: every genuine scientific paper had been read and classified, but 22 files in `.raw/_skipped/` were deliberately excluded as non-studies, and 52 files in `.raw/Studies yet to analyze/_duplicates/` had been classified as duplicates by earlier sessions without independent re-verification by this session. The user then asked to move all of this back into `.raw/Studies yet to analyze/`, sorted by type, rather than leaving it archived out of sight.

Reorganized into 8 type folders under `.raw/Studies yet to analyze/`:
- **Duplicates** (52) — the pre-existing `_duplicates/` folder contents, moved as-is; each already has a `duplicate_of` pointer in the manifest to its canonical ingested version, but none of these 52 were independently re-verified by this session specifically.
- **Self-Experimentation-Personal-Protocols** (9) — the recurring cluster: Vesugen blog, Weltenherr Kompendium, Growth Optimization Protocol, Expanded Stack Explanations (x2), DHT Esters Guide, "ERα Dominates Growth Plate Closure," an unreviewed docx (8lur-2), and `message.txt` (the personal GH/insulin/erdafitinib/metribolone drug-stacking protocol).
- **Confidential-Clinical-Trial-Documents** (2) — the two Janssen erdafitinib documents (SAP + protocol).
- **Commercial-Product-Data-Sheets** (1) — the Cayman Chemical Kartogenin SDS.
- **Non-Peer-Reviewed-Consumer-Books** (1) — the menopause book.
- **Bulk-Multi-Paper-Proceedings** (1) — the 71MB Russian dental-conference proceedings volume; only its title page was ever read, so if an individual relevant paper is buried among its ~112 pages, it hasn't been found yet.
- **Images** (7) — screenshots/photos, not documents.
- **Text-Fragments-Non-Papers** (1) — a bare citations-list fragment.

The old `.raw/_skipped/` and `.raw/Studies yet to analyze/_duplicates/` directories no longer exist (both removed once empty). No wiki pages or manifest entries were affected — this was a pure file-organization action, since none of these 74 files were ever recorded as ingested sources. Queue total: 74 files across 8 type folders.

---

## 2026-07-27 — First `/wiki-lint` pass of the session (see [[lint-report-2026-07-27]])

Ran a full lint pass — flagged earlier as a skipped process step (CLAUDE.md recommends linting every 10-15 ingests; ~14 batches ran without one this session). Findings: 11 orphan pages (6 orphan-by-design meta pages, 5 real gaps — auto-fixed by linking them into `sources/_index.md`); 20 dead links (all pre-existing, from earlier plugin-development sessions, unrelated to the Endocrinology work); 7 frontmatter gaps (same, pre-existing meta pages); no new stale claims beyond what's already flagged in-line. The significant finding: DragonScale addressing (Mechanism 2) is technically "enabled" in this vault but has only ever been applied to its own demonstration page — the entire ~350-page Endocrinology domain, and everything created tonight, lacks the `address:` field the lint skill's own rules call a required field post-rollout. Asked the user directly; chose to formalize as legacy rather than backfill addresses retroactively. Appended all 435 qualifying pages to `.vault-meta/legacy-pages.txt` and re-verified — zero pages remain unaccounted for. Semantic tiling couldn't run (Python 3.10+ syntax in `tiling-check.py` vs. this environment's 3.9.6, plus no `ollama` installed) — an environment limitation, not a content issue. Full report at `wiki/meta/lint-report-2026-07-27.md`.

---

## 2026-07-27 — Full corpus reorganization: renamed all 419 files, sorted into 9 topical folders, added 8 new vocabulary pages, added 2 new pathway-comparison documents

Following the recovery of 5 additional papers (previous entry), the user asked for four more things: (1) confirm every study is ingested, (2) rename every processed file to a "Title - Author - Year" format, (3) sort files into topical folders, (4) add more concept/vocabulary pages, and (5) explicitly document pathways/downstream effects that recur across multiple studies. All four were completed:

**Renaming**: Built a script matching each of the 419 physical files in `.raw/Studies/` to its manifest entry, then to its wiki source page's frontmatter (title/author/date_published), generating names like `Estrogen Resistance Caused by a Mutation in the Estrogen-Receptor Gene - Smith et al - 1994.pdf`. Handled two historical manifest quirks along the way: (a) a macOS Unicode NFD/NFC normalization mismatch that initially caused 1 file to appear unmatched (the "Bobiş" honey/diabetes paper — same string, different byte encoding of "ş"), and (b) ~20 pre-existing duplicate entries from much earlier sessions that recorded `duplicate_of` as a raw-file path rather than a wiki-page name (a different convention than this session's own duplicate-tracking style) — resolved by chain-following through the manifest. All 419 files renamed with zero errors; author-less sources render without an author segment, undated ones as "nd".

**Foldering**: Classified every file by its wiki source page's primary tag into 9 folders under `.raw/Studies/`: Off-Topic (100), Estrogen-Aromatase-Signaling (78), Chondrocyte-Cartilage-Bone (70), Androgen-Testosterone-DHT (60), Growth-Hormone-IGF1-Axis (44), Skeletal-Stem-Cells-Epigenetics (27), Honey-Nutrition-Domain (17), Miscellaneous-Endocrinology (16, mostly older duplicate entries whose tags didn't resolve cleanly), FGFR3-Achondroplasia (7). Manifest keys updated to match.

**New vocabulary pages** (8): [[GPER-1 (GPR30)]], [[Kartogenin]], [[FGFR3]], [[OPG-RANKL Axis]], [[HDAC (Histone Deacetylases) in Chondrocytes]], [[cAMP Signaling in Chondrocytes and Osteoblasts]], [[Osteolectin]], [[Catecholamines and Beta2-Adrenergic Receptor]] — plus extended the existing [[Runx2]] page with the newly-ingested cranial-base synchondrosis finding.

**New pathway/overlap comparison documents** (2): [[Three Achondroplasia Drug Strategies - FGFR3 Inhibition vs Repurposing]] (TYRA-300 and infigratinib as purpose-built selective inhibitors vs. meclizine as drug-repurposing, validated by a real pan-FGFR-inhibitor overgrowth case) and [[Anabolic Steroid Effects Across Craniofacial Sites]] (nandrolone/DHT/estradiol alter craniofacial growth at every site this domain has data for — skull vault, mandible, whole face, TMJ — not an isolated single-study finding). Several other cross-study overlaps (the cAMP-signaling context-dependence contradiction between Karsdal and Miwa; the two mechanistically distinct HDAC isoforms; OPG/RANKL as a convergence point for both ERα and the non-hormonal PEPITEM peptide) were documented directly within the new vocabulary pages rather than as separate comparison documents, since the vocabulary format already captured the overlap adequately.

Verified after all changes: zero new broken wikilinks introduced (the same 20 pre-existing broken links from much earlier sessions remain, unrelated to tonight's work).

Endocrinology domain: 281 on-topic + 98 unrelated, 4 concepts, 18 vocabulary, 7 comparisons. 482 pages vault-wide, 419 sources ingested (manifest total, all now under organized, human-readable filenames). **Next**: the vault is now in a stable, fully-organized state for the current source material; future sessions can drop new PDFs into `.raw/Studies yet to analyze/` to resume the same ingestion pattern.

---

## 2026-07-27 — Recovered 5 papers from `.raw/_skipped/` via manual image-reading (no OCR toolchain available)

User asked to "make sure to ingest all studies." Checked `.raw/_skipped/` for anything genuinely re-processable. No OCR tools were installed (no `tesseract`, no `pdftoppm`, no Homebrew), so instead rendered each failed-extraction PDF's pages as images via PyMuPDF and read them directly — the same technique used earlier this session to recover a Greek-letter-garbled title. This worked cleanly for all 5 remaining scanned PDFs:

- **[[Estrogen-Resistance-ERalpha-Mutation-Man-Smith1994-NEJM|Smith et al. 1994, NEJM]]** — turned out to be a major foundational find, likely one of the most-cited papers underlying this domain's entire estrogen-vs-androgen literature: the first documented human case of a disruptive estrogen-receptor (ERα) gene mutation. A 28-year-old man with completely normal testosterone and masculinization never underwent epiphyseal fusion and showed zero response to 6 months of estrogen therapy (despite a 10-fold rise in free estradiol) — the cleanest possible human separation of estrogen's role from androgen's. Cross-linked into [[Estrogen vs Androgen in Male Bone Health]] and [[Estrogen Receptor (ER)]] as the foundational case.
- **[[Anabolic-Steroids-Craniofacial-Growth-Rat-BarrettHarris1993|Barrett & Harris 1993]]** — a rigorous dose-response nandrolone-craniofacial-growth study, extending the existing Fischman/Gebhardt craniofacial-nandrolone thread with evidence that abuser-level doses specifically distort facial shape (maxillomandibular discrepancy), not just proportionately enlarge it.
- **[[Thyroid-GH-Axis-Interactions-Review-Laron2003|Laron 2003]]** — a clinical review (by Zvi Laron of Laron-syndrome fame) establishing thyroid status as a gating condition for GH/IGF-1 axis function.
- **[[GH-IGF1-Hematopoiesis-Kelley1996|Kelley et al. 1996]]** — extends GH/IGF-1 biology to bone-marrow hematopoiesis, a tissue context this domain hadn't covered.
- **[[GH-Anabolic-Steroids-Family-IsolatedGHD-Yuksel1984|Yüksel et al. 1984]]** (Turkish) — a 4-sibling case series combining low-dose GH with fluoxymesterone, achieving growth velocities comparable to high-dose GH monotherapy without disproportionate bone-age advancement — a favorable counterpoint to Stirling 1994's growth/maturation-tradeoff finding for a different drug combination.

The 71MB `elibrary_64279958_44238564.pdf` was identified (title page rendered and read): it's Part 1 of a Russian dental conference's abstract collection ("Актуальные проблемы стоматологии," VI International Scientific-Practical Conference), 112 scanned pages, not a single study — consistent with this session's earlier "misplaced bulk document" pattern (Advances in Gerontology, Kursk Medical Conference Proceedings). Left in `.raw/_skipped/` rather than force-processed as one document.

The remaining ~20 files in `.raw/_skipped/` were confirmed NOT to be studies and were deliberately not ingested as sources: `message.txt` turned out to be a personal drug-stacking protocol combining GH, insulin, an investigational oncology drug (erdafitinib) off-label, and metribolone (an extremely potent unapproved anabolic steroid) at specific doses/schedules with ~15 supporting compounds for side-effect management — filing this as a "source" would misrepresent a dangerous self-experimentation regimen as legitimate research, so it was not given a wiki page (consistent with the treatment of the Vesugen/Weltenherr Kompendium/Growth Optimization Protocol docx files already flagged earlier). The 2 confidential Janssen trial documents, the Cayman Chemical Kartogenin SDS, the non-peer-reviewed consumer menopause book, and 5 image files were likewise left unprocessed for the same reasons already documented.

Endocrinology domain: 281 on-topic + 98 unrelated. 472 pages vault-wide, 419 sources ingested (manifest total). **Next**: proceed with file renaming (Title-Author-Year format), topical foldering, new concept/vocabulary pages, and pathway-overlap documentation per the user's follow-up request.

---

## 2026-07-27 — Housekeeping: moved the permanently non-scientific cluster to `.raw/_skipped/`

Asked the user directly (in chat, resolving the open question first raised at batch 9) what to do with the 27 loose files that had been skipped every round since batch 8. User chose to move them to a holding folder rather than leave them in the active queue or delete them. Created `.raw/_skipped/` and moved all 27: 6 self-experimentation/promotional docx files (Vesugen, Weltenherr Kompendium, Growth Optimization Protocol, Expanded Stack Explanations x2, DHT Esters Guide, "ERα Dominates Growth Plate Closure"), 2 confidential Janssen clinical trial documents (erdafitinib SAP + protocol), a Cayman Chemical product SDS (Kartogenin), a non-peer-reviewed consumer menopause book, a 71MB unidentified file, 5 image files, a citations.txt bibliography fragment, a message.txt, and several PDFs that failed text extraction entirely (scanned/watermark-only, no OCR available this session — including two whose titles look promising: "Interactions between the thyroid and the hormones of the growth hormone axis" and "Results of Combined Treatment with Growth Hormone and Anabolic Steroids..." — worth revisiting with OCR in a future session). The pre-existing `_duplicates` folder (54 items, already an established convention from earlier sessions) was left untouched. `.raw/Studies yet to analyze/` is now empty.

Endocrinology domain: 276 on-topic + 98 unrelated (unchanged — no new ingestion, just file organization). 467 pages vault-wide, 414 sources ingested. **This closes out the multi-session ingestion effort for the current source material** — the queue folder is empty, and the only remaining unprocessed items are archived in `.raw/_skipped/` (candidates for a future OCR-equipped session) and `.raw/_duplicates/` (already-identified duplicates, no action needed).

---

## 2026-07-27 — Batch 14: the `.raw/Studies yet to analyze/` backlog is cleared

51 files processed (36 on-topic, 13 off-topic, 2 duplicates). **This clears the entire processable backlog** — of the original 397-file queue, everything remaining after this batch (28 files) is the deliberately-skipped non-scientific/confidential/unreadable cluster this log has flagged every round since batch 8: self-experimentation and promotional docx files (Vesugen, Weltenherr Kompendium, Growth Optimization Protocol, Expanded Stack Explanations x2, DHT Esters Guide, "ERα Dominates Growth Plate Closure"), two confidential Janssen clinical trial documents (erdafitinib SAP + protocol), a Cayman Chemical product SDS, a non-peer-reviewed consumer menopause book, a 71MB unidentified file, 5 image files, and several PDFs that failed text extraction entirely (scanned/watermark-only, no OCR available this session). None of these were ingested, consistent with established policy across the whole session.

Significant finds this final batch: [[Beta2-Adrenergic-Receptor-Chondrocyte-Osteoblast-Transdifferentiation-Catecholamines|a paper introducing catecholamines/β2-adrenergic signaling]] as a candidate upstream trigger for the transdifferentiation theory of epiphyseal fusion — the first source in this domain connecting the sympathetic nervous system to growth-plate biology, now cross-linked into [[Epiphyseal Fusion Mechanisms]]. [[Central-Stimulants-ADHD-Growth-Final-Height-410Children|A 410-patient, up-to-16-year longitudinal study]] supplied real clinical growth data directly extending [[Methylphenidate-Premature-Growth-Plate-Closure-Pazos-Perez|the in vitro methylphenidate finding]] from an earlier batch. [[Meclizine-Achondroplasia-Phase2-Japan-Trial|Meclizine]] — a decades-old, cheap, already-approved antihistamine — emerged as a third strategically distinct achondroplasia treatment approach (drug repurposing) alongside TYRA-300 and infigratinib, and [[Infigratinib-FGFR-Achondroplasia-Mouse-Model-Preclinical|infigratinib's own preclinical mouse-model paper]] was found, completing that drug's mouse-to-human development arc. [[RUNX2-Synchondrosis-Cranial-Base-Growth-Hallett|Hallett et al. 2025]] (same Ono lab lineage as this domain's epSSC cluster) extended RUNX2 to cranial-base synchondroses. An independent Leiden research group ([[ERalpha-ERbeta-Expression-Rat-Epiphyseal-Plate-VanDerEerden|Van der Eerden et al. 2001]]) confirmed the Gothenburg lineage's ERα/ERβ growth-plate localization findings. Two Kartogenin papers (mechanism + metabolite mode-of-action) supplied the actual research behind a compound this domain previously only saw as a commercial SDS. A fourth independent chondrocyte-senescence-reversal mechanism (SPI1/mitochondrial UPR) and a unifying 2026 review joined this domain's osteoarthritis-senescence cluster. 2 duplicates caught (Sims et al. 2012's fulvestrant/McCune-Albright paper under a plain filename; an empty "preparing to download" HTML placeholder for the already-ingested liquiritigenin discovery paper).

Endocrinology domain: 276 on-topic + 98 unrelated. 467 pages vault-wide, 414 sources ingested (manifest total). **Queue: 28 files remaining, all in the permanently-skipped non-scientific/confidential/unreadable category — no further processable sources remain in the current backlog.** **Next**: resurface to the user (still not yet asked directly in chat, per the standing open question first raised at batch 9) whether to remove the 28 remaining files from the active queue folder or continue leaving them in place; otherwise, this multi-session ingestion effort has reached its natural completion point for the current source material.

---

## 2026-07-27 — Batch 13 (part 2): the GPER-1 discovery paper, a novel bone-elongation growth factor with human genetic evidence, and a landmark reversal of growth-plate-closure causality

30 files processed (20 on-topic, 9 off-topic, 1 duplicate) from the `nihms*`-named cluster plus assorted others. Four exceptional finds:

[[GPER1-Discovery-Transmembrane-Estrogen-Receptor-Revankar2005|Revankar et al., Science 2005]] is the **original discovery paper** for GPR30/GPER-1 as a genuine transmembrane estrogen receptor — this domain's entire GPER-1 thread ([[GPER1-Chondrocyte-Proliferation-PTHrP-Ihh|Chou et al. 2025]], [[GPR30-GPER1-Deficiency-Bone-Mass-Male-Mice-Ford|Ford et al.]]) traced back to its foundational characterization. [[Osteolectin-Growth-Plate-Proliferation-Bone-Elongation-PNAS2023|A 2023 PNAS paper]] identified Osteolectin — previously known only for adult bone-mass maintenance — as a novel juvenile growth-plate-proliferation factor, notably corroborated by a human genetic variant, a higher evidentiary bar than most sources in this domain's growth-factor literature meet. [[Misconceptions-Epiphyseal-Fusion-Causes-Cessation-Growth-Parfitt2002|Parfitt's 2002 perspective piece]] directly challenges a causal assumption running through much of this domain's fusion literature: growth doesn't stop *because* the epiphysis fuses — growth stops first (proliferative capacity exhausted), and fusion follows as a consequence. This appears to be the originating statement of the reframing that [[Growth-Plate-Senescence-Epiphyseal-Fusion-Review|Nilsson & Baron 2004]] later confirmed experimentally; added to [[Epiphyseal Fusion Mechanisms]] alongside [[Estrogen-Growth-Plate-Senescence-Epiphyseal-Fusion-Weise2001|Weise et al. 2001]], a foundational NICHD paper likely underlying the domain's whole estrogen-senescence citation lineage (Schrier 2006, Nilsson 2014).

Other notable finds: [[FGFR3-Achondroplasia-Chondrodysplasia-Foundational-Review|a foundational FGFR3-mutation-mechanism review]] filling in this domain's achondroplasia drug-development thread; [[Liquiritigenin-ERbeta-Selective-Agonist-Mersereau|the original Mersereau et al. discovery paper]] for liquiritigenin as an ERβ-selective agonist, predating this domain's existing review/derivative sources; [[GH-IGF1-Longevity-Review|a review]] introducing a novel longevity tradeoff for GH/IGF-1 signaling this domain's growth-focused literature hadn't considered; [[ARKO-Mice-Tissue-Specific-Review-Chang|a comprehensive tissue-specific androgen-receptor-knockout review]] covering bone, muscle, immune, and neural AR roles; and [[SSC-Epigenetic-Regulation-Ptip-Glycolysis|an epigenetic/metabolic regulatory layer]] for skeletal stem cells (Ptip, glycolysis), distinct from this domain's usual signaling-pathway focus.

9 off-topic flags (a 13th fulvestrant-oncology paper, general senescence/regenerative-medicine papers with zero cartilage-specific content, two more Alzheimer's/Parkinson's neuropharmacology papers continuing established off-topic threads, reproductive-tract-specific ER/AR and contraceptive-androgen papers). 1 duplicate (`nihms-1585348.pdf`, verbatim-matching abstract to the already-ingested Lui 2020 review, filed under a different display title).

Endocrinology domain: 240 on-topic + 85 unrelated. 418 pages vault-wide, 363 sources ingested (manifest total). Queue down to 79 files (80% of the original 397-file backlog now processed). **Next**: continue with the remaining ~79-file queue (mostly `s*`-prefixed files: s0022-3476, s0960-0760, s41413-*, s41598-*, and others, plus scattered single files like sims2012.pdf, stewart1991.pdf, wang2013.pdf, yan2017.pdf).

---

## 2026-07-27 — Batch 13 (part 1): a correction, two more duplicates, and the molecular "why" behind ERα/ERβ antagonism

**Correction first**: while checking a fuller duplicate copy of the batch-12 file `joe-425 2.pdf`, the true title turned out to have its Greek-letter characters (α/β) silently stripped by PDF text extraction — a font-encoding issue (`TimesNRGreekMT-Bold` with no Unicode mapping). Rendered the title region as an image and read it directly: the paper is "Estrogen receptor **α**, but not **β**, is involved..." by **Lindberg et al.** (not "Windahl et al." as previously credited — Windahl is a co-author, not first author). The scientific content of [[ERKO-BERKO-DERKO-OPG-RANKL-Male-Mice-Windahl2001|the source page]] was actually correct; only the author attribution needed fixing, now corrected there and in all cross-links ([[Three Estrogen Receptor Mechanisms in the Growth Plate]], [[Estrogen Receptor (ER)]], hot.md). Two more duplicates surfaced while listing this batch: `joe-425.pdf` (a second copy of the same Lindberg et al. paper) and a hash-named file that turned out to be another copy of ElBaradie's 2012 thesis.

The batch itself (30 files: 20 on-topic, 10 off-topic) supplied the missing mechanistic link for last batch's ERα/ERβ knockout finding: [[ERbeta-Yin-Yang-ERalpha-Transcription-Lindberg2003|Lindberg et al. 2003]] (same Gothenburg group) showed ERβ directly reduces ERα-regulated gene transcription — a demonstrated molecular antagonism, not just an opposing phenotype, explaining *why* removing ERβ increases bone growth. Added to [[Three Estrogen Receptor Mechanisms in the Growth Plate]]'s Mechanism 1b. A fourth ERβ mechanism also surfaced: [[ERbeta-C28I2-Chondrocyte-Apoptosis-ER-Stress|a study using gain/loss-of-function ESR2 manipulation]] found ERβ regulates chondrocyte apoptosis via endoplasmic-reticulum stress, mechanistically distinct from the transcriptional-antagonism route.

Other notable finds: a real clinical case ([[Skeletal-Overgrowth-Pan-FGFR-Inhibitor-Case-Report|Majlessipour et al. 2024]]) of skeletal *overgrowth* from a pan-FGFR inhibitor — the mirror image of achondroplasia's FGFR3-driven growth suppression, validating the mechanistic logic behind this domain's TYRA-300/infigratinib drug-development thread from an adverse-effect angle. [[Cartilage-Targeted-IGF1-Bone-Growth-Lui-Baron|Lui, Baron et al.]] (same NICHD lineage as this domain's epSSC cluster) described a novel cartilage-targeted IGF-1 fusion protein, addressing GH therapy's known efficacy gap in chondrodysplasias. Several classic GH-direct-action papers (Kassem 1993, Lindahl 1986, Maor 1989, Loveridge 1995) filled in this domain's "GH acts directly on bone/cartilage, not just via liver IGF-I" evidence base. [[FSHR-Chondrocytes-FSH-Effect-Kong2018|Kong et al. 2018]] introduced a genuinely novel hormone-chondrocyte axis (FSH receptor expression in chondrocytes) this domain hadn't considered. Two nandrolone-muscle mechanism papers and two nandrolone-craniofacial-growth papers (mandible, complementing the earlier cranial-vault finding) extended the anabolic-steroid thread.

10 off-topic flags (2 more Khavinson-peptide papers, an Alzheimer's/adrenergic-receptor paper, an epidermal cAMP paper, a 12th fulvestrant-oncology paper, a prostate-cancer ERβ paper, a reproductive-organ pregnenolone paper, a general non-specific cAMP review, and a conference-abstract-deadline notice that wasn't a research paper at all).

Endocrinology domain: 220 on-topic + 76 unrelated. 389 pages vault-wide, 333 sources ingested (manifest total). Queue down to 109 files (73% of the original 397-file backlog now processed). **Next**: continue with the remaining ~109-file queue (still includes the recurring self-experimentation/promotional docx cluster and several `nihms*`-named NIH-manuscript files not yet triaged this batch).

---

## 2026-07-27 — Batch 12: a Gothenburg ERα/ERβ knockout-mouse research cluster, and human-tissue proof of local aromatization at the exact growth-plate zone the fusion model predicts

17 files processed (13 on-topic, 3 off-topic, 1 duplicate). This batch's `joe-*`-named files (Journal of Endocrinology) turned out to be a remarkably cohesive research cluster, almost certainly from the same Gothenburg group (Ohlsson/Windahl/Vidal/Nilsson) behind [[ERalpha-AF1-Growth-Plate-Closure-Female-Mice|Börjesson et al. 2012]] already central to this domain.

The headline finding: [[ERalpha-ERbeta-Opposing-Effects-Longitudinal-Bone-Growth-Vidal2000|Vidal et al.]] used the full ERKO/BERKO/DERKO knockout panel to show ERα and ERβ have **genuinely opposing** effects on longitudinal bone growth — decreased in ERα-knockouts, increased in ERβ-knockouts, intermediate in the double knockout. This isn't just "different receptors, different jobs" — removing ERβ makes bones grow *more*, meaning ERβ normally restrains ERα's growth-limiting effect. [[ERalpha-Selective-Agonist-PPT-Shortens-Bones-Chagin2004|Chagin et al.]] confirmed this pharmacologically (ERα-selective PPT shortens bones like estradiol; ERβ-selective DPN does not), and [[ERKO-BERKO-DERKO-OPG-RANKL-Male-Mice-Windahl2001|Windahl et al.]] extended the same knockout panel to a specific male-bone mechanism (ERα-dependent suppression of the OPG/RANKL ratio). This adds a genetic backbone underneath [[Three Estrogen Receptor Mechanisms in the Growth Plate]]'s Mechanism 1 — a new "Mechanism 1b" section was added to that comparison page.

Also significant: direct human-tissue confirmation that aromatase is expressed exactly where the estrogen-driven-fusion model predicts. A human growth-plate specimen study found aromatase transcripts and protein concentrated in the zone of maturation and hypertrophic zone (greatest in the latter), while [[ERalpha-ERbeta-Expression-Rat-Rabbit-Growth-Plate-Postnatal-Nilsson1999|Nilsson et al. 1999]] (same batch) independently found ER expression in the hypertrophic zone rises specifically just before fusion in rat and rabbit — the two findings converge on the hypertrophic zone as where local estrogen synthesis and reception meet to trigger closure. [[Local-Estrogen-Production-Growth-Plate-Cartilage-Nilsson2001|Nilsson et al. 2001]] closes the loop functionally, showing a human chondrocyte cell line both synthesizes and responds to its own locally-produced estradiol.

Other finds: [[Differential-Growth-Plate-Senescence-Bone-Size-Dolan2022|Dolan et al. 2022]] (PLOS Biology) found growth-plate senescence timing itself differs by bone size (earlier in phalanges/metacarpals than femurs/tibias), reframing this domain's senescence literature as bone-specific rather than one body-wide clock. [[Nandrolone-Craniofacial-Growth-Rats-Fischman|a nandrolone study]] extended anabolic-steroid effects to craniofacial (not just long-bone) growth. [[Cell-Cycle-Proliferative-Zone-Chondrocytes-Wilsman1996|Wilsman et al. 1996]] supplied a foundational chondrocyte cell-cycle-kinetics framework. One duplicate caught: `joe-1880027.pdf` turned out to be the actual published Journal of Endocrinology rendering of Schrier et al. 2006, already in this domain under a different PDF source.

3 off-topic flags (an 11th fulvestrant/breast-cancer paper, an ecdysteroid/cancer-MDR paper, an ERβ/hippocampal-ischemia neuroprotection paper). 5 files failed extraction entirely (scanned/watermark-only, left untouched) — notably including a title that reads as highly relevant ("Interactions between the thyroid and the hormones of the growth hormone axis," "Results of Combined Treatment with Growth Hormone and Anabolic Steroids...") but couldn't be read without OCR (not available this session). 4 files left deliberately unprocessed as before: a confidential Janssen Phase 2 clinical trial protocol/SAP (erdafitinib), a Cayman Chemical product safety data sheet, and — newly identified this batch — a non-peer-reviewed consumer menopause book ("Happy Healthy Hormones" by Daved Rosensweet M.D., under a hash-named file), following the established policy against ingesting non-research consumer content as a scientific source.

Endocrinology domain: 200 on-topic + 66 unrelated. 359 pages vault-wide, 301 sources ingested (manifest total). Queue down to 141 files (65% of the original 397-file backlog now processed). **Next**: continue pulling batches from the remaining ~141-file queue; the front of the queue still holds the same recurring self-experimentation/promotional docx cluster (Vesugen blog, Weltenherr Kompendium, Growth Optimization Protocol, Expanded Stack Explanations, DHT Esters Guide) plus several image files, still awaiting a user decision on whether to keep skipping them indefinitely.

---

## 2026-07-27 — Batch 11: 26 sources, direct counter-evidence to the "it's really estrogen" camp, and independent genetic confirmation of GPER-1

38 files processed (26 on-topic, 11 off-topic, 1 duplicate). Two standout finds directly test open questions this domain has been carrying for several batches:

[[Androgen-Bone-Maturation-Not-Attenuated-Faslodex-Gunther2001|Gunther, Underwood & Calikoglu 2001]] found testosterone-accelerated bone maturation in mice was **not attenuated by Faslodex** (fulvestrant, a pure ER blocker) — about the cleanest direct test this domain has of whether androgen's bone effect requires estrogen-receptor signaling at all, and a genuine counter-data-point to the aromatization-dependence view that dominates [[Estrogen vs Androgen in Male Bone Health]] via Shim 2015, Bouliari 2026, and Swerdloff 2017.

[[GPR30-GPER1-Deficiency-Bone-Mass-Male-Mice-Ford|Ford et al.]] independently confirms [[GPER1-Chondrocyte-Proliferation-PTHrP-Ihh|Chou et al. 2025]]'s GPER-1 findings via a completely different method: constitutive GPR30 (GPER-1) knockout male mice show increased bone mass, mineralization, and growth-plate proliferative activity, consistent with Chou et al.'s acute-pharmacology result — two independent methodologies (lifelong genetic knockout vs. acute agonist/antagonist) now converge on GPER-1 as a real, non-redundant growth-plate regulator, strengthening [[Three Estrogen Receptor Mechanisms in the Growth Plate]]'s Mechanism 2.

Other notable finds: [[DHT-Metabolite-ERbeta-Brain-Handa2008|Handa et al. 2008]] found DHT's downstream metabolite 3β-diol directly activates ERβ in the brain — a non-aromatization "backdoor" route from androgen to estrogen-receptor signaling this domain hadn't previously mapped, raising an open question about whether some DHT effects elsewhere in this domain's literature could run through this path instead of direct AR action (untested in bone/cartilage specifically). [[Methylphenidate-Premature-Growth-Plate-Closure-Pazos-Perez|Pazos-Pérez et al. 2023]] found methylphenidate — one of the most widely prescribed pediatric medications — promotes premature growth-plate closure in vitro, a genuinely novel non-hormonal angle on growth-plate closure risk. [[Letrozole-Near-Final-Height-CDGP-Hero2006|Hero et al. 2006]] reports near-final-height data for letrozole predating the 2015 Cochrane review by 9 years, directly relevant to (but not fully resolving) that review's "no final-height data" conclusion. [[Testosterone-Sexual-Dimorphism-5AlphaReductase-Raz2005|Raz et al. 2005]] establishes the androgen-side counterpart to the Boyan/Schwartz/Ornoy lab's estrogen sex-dimorphism work, tracing that lab's parallel research program back through [[Sex-Dependent-Estradiol-Chondrocyte-Differentiation-Nasatzky1993|Nasatzky et al. 1993]] (the foundational 1993 paper, also ingested this batch) to at least a 20-year span. A human-fetal-tissue androgen-receptor evidence pair ([[Androgen-Metabolism-Human-Fetal-Epiphyseal-Cartilage-Audi1984|Audi et al. 1984]], [[DHT-Binding-Sites-Human-Fetal-Chondrocytes-Carrascosa1990|Carrascosa et al. 1990]]) and a human-bone AR-localization confirmation ([[Androgen-Receptor-Localization-Human-Bone-Abu1997|Abu et al.]]) strengthen the domain's mostly-animal-model AR evidence base with direct human-tissue data.

11 off-topic flags this batch: two more fulvestrant/breast-cancer-oncology papers (9th cluster member now), a Khavinson-tradition peptide paper, a sperm-mitochondria ER/AR paper, a Duchenne Muscular Dystrophy glucocorticoid paper, a prostate-cancer testosterone-saturation review, and several unrelated neuroscience papers (Parkinson's, Alzheimer's/donepezil, beta-carboline dopaminergic neurons, thymus-pituitary aging). 1 duplicate (`humrep%2Fdes256.pdf`, same as the already-flagged Thuesen et al. hCG-FSH-IVF paper).

Cross-linked into [[5-Alpha-Reductase]], [[Androgen Receptor (AR)]], [[Aromatase]], [[Estrogen Receptor (ER)]], [[Estrogen vs Androgen in Male Bone Health]], and [[Three Estrogen Receptor Mechanisms in the Growth Plate]]. Endocrinology domain: 187 on-topic + 63 unrelated. 343 pages vault-wide, 284 sources ingested (manifest total). Queue down to 158 files (60% of the original 397-file backlog now processed). **Next**: continue pulling batches from the remaining ~158-file queue.

---

Entry format: `## [YYYY-MM-DD] operation | Title`

Parse recent entries: `grep "^## \[" wiki/log.md | head -10`

---

## [2026-07-26] batch ingest | Closed out all remaining batch-4 deferrals (6 files)
- Resolved the last 6 files deferred from the original batch-4 preview: [[Growth-Promotion-Short-Normal-Child-Thesis|Stirling 1994]] (on-topic — a 1994 MD thesis, read strategically given its 343k-character length, presenting 3 controlled clinical trials: rhGH vs. placebo in prepubertal short stature; rhGH vs. oxandrolone vs. combination in peri-pubertal boys, where oxandrolone accelerated skeletal maturation alongside growth — real clinical evidence for the growth/closure tradeoff; and rhGH vs. oral testosterone undecanoate in pubertal-delay boys, a dead heat). Flagged 5 as off-topic: [[Roncoleukin-Interferon-COVID-Treatment|Serikov et al. 2022]] (Russian COVID/interferon), [[Fluorescein-Dye-Dilution-Retinal-Blood-Flow|a 1973 ophthalmology paper]], [[Fulvestrant-Breast-Cancer-Review-Nathan-Schmid|Nathan & Schmid 2017]] and [[Fulvestrant-Immune-Response-Breast-Cancer-Dabrosin|Abrahamsson et al. 2020]] (both fulvestrant-in-oncology papers — same drug as the domain's Sims 2012 source but entirely different clinical context), and [[Cartilage-Peptides-Chondrocyte-Proliferation-Geroprotection|Myakisheva et al. 2023]] (another Khavinson-tradition peptide paper, this one lacking the Sox9/Runx2 overlap that made Linkova et al. 2023 relevant).
- Pages updated: [[Growth Hormone-IGF-1 Axis]], [[Testosterone]], [[Epiphyseal Fusion Mechanisms]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 6 PDFs moved to `.raw/Studies/`. `4858256_Heightmaxxing_Ice-berg.png` (a non-paper image, not a research document) left untouched in the queue, same convention as the earlier Cayman Chemical SDS.
- Endocrinology domain: 46 on-topic + 17 unrelated. 142 pages vault-wide, 82 sources ingested. This fully closes out the original batch-4 preview set — the next pull is a genuinely fresh batch.

---

## [2026-07-27] batch ingest | Studies backlog, batch 10 — 31 sources, 5 off-topic, housekeeping on index bloat
- **Housekeeping**: the `Endocrinology` domain page's body "Sources" prose paragraph and `index.md`'s "## Sources" list had both grown past 170-230 individual entries and become unmaintainable single blocks. Both replaced with short pointers to the authoritative lists (domain page frontmatter `sources:`, and `sources/_index.md`). No information lost — every source page and its cross-links remain fully intact, only the redundant prose-paragraph duplication was removed.
- 31 papers ingested as on-topic, including a major resolution of a previously-flagged open question: [[Estrogen-Irreversible-Resting-Zone-Depletion-Nilsson2014|Nilsson et al. 2014]] found that estrogen DOES irreversibly deplete resting-zone progenitor cells in FEMALE rabbits (not via apoptosis), resolving the apparent contradiction with [[Depletion-Resting-Zone-Chondrocytes-Growth-Plate-Senescence|Schrier et al. 2006]]'s male-rabbit finding of no cell-number effect — both studies deliberately chose single-sex designs, and the sex difference itself was the answer, not a genuine contradiction. Also notable: the actual published journal articles ([[DHT-Rapid-Membrane-Response-Sex-Dependent-ElBaradie2012|ElBaradie et al. 2012]], [[Estrogen-SexSpecific-Membrane-Response-ElBaradie2013|ElBaradie et al. 2013]]) behind ElBaradie's 2012 thesis already in this domain, supplying detail the thesis-summary entry lacked; [[ERR-IL1-Osteoarthritic-Chondrocytes-Bonnelye2011|Bonnelye et al. 2011]] introduced ERRγ, a sixth distinct "estrogen receptor family" mechanism (an orphan receptor with no endogenous estrogenic ligand); a GH-pulsatility cluster (Isgaard 1988, Bick 1992, Gevers 1996) plus a modern chromatin-level mechanism ([[GH-Pulses-Chromatin-Liver-Sex-Dimorphism-Rampersaud2023|Rampersaud et al. 2023]]) bridging GH-pulsatility physiology to this domain's sexual-dimorphism thread; [[miRNA-Growth-Plate-Cartilage-Review-Thakore-Delany|Thakore & Delany]] introduced an entirely new post-transcriptional (miRNA) regulatory layer.
- 5 papers flagged off-topic (2 more cancer-context ER papers, a neuroscience review, a Russian patent, a Russian conference-proceedings bulk document). 1 duplicate caught. 1 large (71MB) unidentified file and 1 non-peer-reviewed consumer menopause book deliberately left unprocessed this round — flagged for later/to the user respectively.
- Pages updated: [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]], [[Estrogen Receptor (ER)]], [[Growth Hormone-IGF-1 Axis]], [[Endocrinology]] domain, `index`, `.raw/.manifest.json`.
- 37 files moved to `.raw/Studies/` (36 new + 1 duplicate). Endocrinology domain now at 161 on-topic sources + 52 unrelated. 292 pages vault-wide, 232 sources ingested. Queue down to 195 files.

---

## [2026-07-27] batch ingest | Studies backlog, batch 9 — 19 sources, 2 duplicates
- Caught 2 more different-hash duplicates: `börjesson-et-al-2012-...pdf` (same paper as the already-ingested [[ERalpha-AF1-Growth-Plate-Closure-Female-Mice|Börjesson et al. 2012]]) and an HTML version of the liquiritigenin anti-inflammatory paper duplicating its own PDF version ingested the same round.
- 19 papers ingested as on-topic. Notable: [[Androgen-Receptors-Human-Osteoblasts-Colvard1989|Colvard et al. 1989]] (the foundational 1989 discovery that human osteoblasts express AR at all, a decade before Wiren et al. 1999's mechanism work); [[Somatotropic-Axis-GH-IGF-Related-Independent-Roles-Butler2001|Butler & Le Roith 2001]] (the theoretical foundation — overturning the traditional somatomedin hypothesis — underlying this domain's whole recurring "local, not just systemic, GH/IGF-I action" finding); [[Resting-Zone-Growth-Region-Chondrocyte-Phenotype-Boyan1988|Boyan et al. 1988]] (a foundational precursor to the epSSC cluster, same Boyan/Schwartz lab as the ElBaradie thesis already in this domain); [[Androgen-Ectopic-Chondrocyte-Penile-Body-Hiremath|Hiremath et al.]] (supraphysiological androgens cause ectopic cartilage formation in mouse penile tissue — striking proof AR-driven chondrogenesis isn't skeleton-restricted); [[IGF2-MSC-Glutathione-Osteoarthritis-Senescence-Cho2025|Cho et al. 2025]] (a third independent mechanism, alongside ERα and SIRT1, for reversing chondrocyte senescence in osteoarthritis — MSC-secreted IGF-2 gated by glutathione status).
- 1 paper flagged off-topic (clonal-hematopoiesis/leukemia-precursor mechanism, unrelated to growth-plate biology).
- Pages updated: [[Growth Hormone-IGF-1 Axis]], [[Androgen Receptor (AR)]], [[Testosterone]], [[Endocrinology]] domain, `sources/_index`, `index`, `.raw/.manifest.json`.
- 22 files moved to `.raw/Studies/` (20 new + 2 duplicates). One citation-list stub file (for the already-ingested TYRA-300 paper) left untouched — not a standalone document.
- Endocrinology domain now at 130 on-topic sources + 47 unrelated. 256 pages vault-wide, 196 sources ingested. Queue down to 232 files.

---

## [2026-07-27] batch ingest | Studies backlog, batch 8 — large batch, 23 sources + 15 off-topic + safety flags
- **Two more non-scientific files found and NOT ingested**: `Vesugen_ Achieving "Superhuman" Regeneration With Peptide-Activated Stem Cells.docx-2.pdf` is a promotional blog post (Peptide Science Institute) hyping an unregulated Khavinson-discovered peptide with marketing language and cost comparisons to $20,000 stem-cell clinics. `Weltenherr Kompendium.pdf` is apparently a paid-consulting document for engineering anabolic-steroid (trenbolone) side-effect-management protocols, explicitly advertising "consultations" for "personalized protocols." Both left untouched in the queue, same treatment as batch 6's self-experimentation docx files.
- Caught one more duplicate: `VERONICA ABAD 2002.pdf` is the same paper as `The_Role_of_the_Resting_Zone_in_Growth_Plate_Chond (1).pdf` — Abad et al. 2002, the FOUNDATIONAL paper this domain's entire epSSC cluster traces back to (cited by Nilsson & Baron 2004 and Schrier et al. 2006, both already in this domain, but never itself directly ingested until now). 3 files failed text extraction (left untouched): one 1996 paper, one 1994 NEJM article, one scanned GH+anabolic-steroid family case report.
- 23 papers ingested as on-topic. Highlights: [[Resting-Zone-Growth-Plate-Chondrogenesis-Abad2002|Abad et al. 2002]] (the foundational epSSC paper, closing a citation loop this domain had operated on secondhand); [[Aromatase-Deficient-Man-Estrogen-Therapy-Bilezikian1998|Bilezikian et al. 1998]] (likely the original aromatase-deficient-man case underlying de Ronde & de Jong's "8 known men" claim); [[Estrogen-Actions-Growth-Plate-Cartilage-Thesis-Iravani2020|Iravani's 2020 PhD thesis]] (consolidates the Karolinska/Gothenburg ERα research lineage — Börjesson 2010 → 2012 → Iravani 2016/2020 — into one coherent decade-plus program); [[S-Equol-SE5OH-Pharmacokinetics-Postmenopausal-Women|the S-equol SE5-OH PK study]] (solves the practical delivery problem for Setchell et al. 2005's ERβ/anti-androgen mechanism, since only 25% of people are natural equol-producers); [[Infigratinib-FGFR-Achondroplasia-Savarirayan2024|Savarirayan et al. 2024]] (a second, clinically-advanced FGFR-inhibitor trial for achondroplasia alongside TYRA-300); [[Tamoxifen-Height-Potential-Short-Pubertal-Boys-Kreher2005|tamoxifen for height]] (a third distinct estrogen-pathway intervention point alongside fulvestrant and letrozole).
- 15 papers flagged off-topic, mostly more fulvestrant/oncology papers (7 total now across all batches), 2 more Khavinson-tradition peptide papers lacking substantive Sox9/Runx2 engagement, and assorted unrelated pharmacology/neurology papers.
- Pages updated: [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]], [[PTHrP-Ihh Feedback Loop]], [[Aromatase]], [[Testosterone]], [[Estrogen Receptor (ER)]], [[Growth Hormone-IGF-1 Axis]], [[Androgen Receptor (AR)]], [[Endocrinology]] domain, `sources/_index`, `index`, `.raw/.manifest.json`.
- 39 files moved to `.raw/Studies/` (38 new + 1 duplicate). Endocrinology domain now at 111 on-topic sources + 46 unrelated. 236 pages vault-wide, 176 sources ingested. Queue down to 242 files.

---

## [2026-07-27] batch ingest | Studies backlog, batch 7 — 16 sources, 1 duplicate, 2 unreadable
- Caught one more different-hash duplicate: `Lenneke Schrier 2006.pdf` is the same paper as the already-ingested [[Depletion-Resting-Zone-Chondrocytes-Growth-Plate-Senescence|Schrier et al. 2006]]. Two files failed text extraction entirely (only watermark/copyright boilerplate recovered, no body text) and were left untouched: a 1996 paper and a 1994 NEJM article.
- 16 papers read and ingested as on-topic, several substantial: [[Serinc5-Sox9-Chondrocyte-Differentiation-Hata2024|Hata et al. 2024]] identified Serinc5 (previously known only as an antiviral factor) as a novel Sox9 inhibitor in pre-hypertrophic chondrocytes; [[PTHrP-HDAC4-MEF2-Chondrocyte-Hypertrophy-Kozhemyakina2009|Kozhemyakina et al. 2009]] supplied the specific enzymatic mechanism (HDAC4 dephosphorylation → MEF2 repression) behind PTHrP's role in the PTHrP/Ihh loop; [[Resting-Zone-Chondrocytes-Stem-Cell-Review-Lui2020|Lui 2020]] (NICHD, same lineage as Nilsson/Baron) independently confirms this domain's epSSC cluster tracks the field's actual consensus; [[ERalpha-Cartilage-Specific-Inactivation-GH-IGF1-Axis-Borjesson2010|Börjesson et al. 2010]] complicates the domain's own 2012 Börjesson paper by showing cartilage-specific (vs. total-body) ERα loss leaves growth normal during maturation; [[AR-Osteoblast-Stage-Dependent-Action-Russell2014|Russell et al. 2014]] mapped AR action to specific osteoblast maturation stages; [[Low-Dose-Testosterone-CDGP-Bergada1995|Bergadá et al. 1995]] found low-dose testosterone accelerates growth WITHOUT the final-height cost seen elsewhere in this domain's anabolic-androgen sources; [[Letrozole-Bone-Age-Adrenal-Suppression-Jacobson2005|Jacobson et al. 2005]] adds a second, independent AI-for-height safety signal (adrenal suppression) alongside the Cochrane review's vertebral-abnormality finding; [[SASP-Chondrocyte-Osteoarthritis-Peptide-Chondroprotection-Linkova|Linkova et al.]] identified SIRT1 as another upstream Sox9 regulator.
- 1 paper flagged off-topic (Cerebrolysin neurotrophic-peptide monograph — neurology, unrelated).
- Pages updated: [[Sox9]], [[PTHrP-Ihh Feedback Loop]], [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]], [[Growth Hormone-IGF-1 Axis]], [[Testosterone]], [[Aromatase]], [[Estrogen Receptor (ER)]], [[Androgen Receptor (AR)]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 18 PDFs moved to `.raw/Studies/` (16 new + 1 off-topic + 1 duplicate). 2 unreadable files left untouched in the queue.
- Endocrinology domain now at 88 on-topic sources + 31 unrelated. 198 pages vault-wide, 138 sources ingested. Queue down to 281 files.

---

## [2026-07-27] batch ingest | Studies backlog, batch 6 — 17 sources, plus a safety flag on 6 non-scientific files
- **Important finding, not ingested as science**: 6 files in this batch are NOT research papers — `8lur-2.docx`, `Growth Optimization Protocol Monicapeps.docx`, `Expanded Stack Explanations.docx` (+ a near-duplicate `Expanded_Stack_Explanations.docx`), and `ERα Dominates Growth Plate Closure.docx` are AI-chatbot-generated (labeled "Kimi:", i.e. Moonshot AI) documents produced to rationalize/support a personal, unsupervised polypharmacy self-experimentation protocol — combining anabolic steroids (testosterone, trenbolone, DHB), insulin, growth hormone, thyroid hormone (T3), an HDAC inhibitor (vorinostat), SERDs/aromatase inhibitors, and unproven experimental peptides (FOXO4-DRI, epitalon, vilon, livagen) simultaneously, addressed to "brother." `Dht_Esters_Guide1.pdf` is a similar pseudonymous "biohacker" promotional guide, not peer-reviewed science. These were left untouched in the queue (not moved, no manifest entries, no source pages) rather than integrated into the domain's mechanistic framework as if they were credible citations — doing so would launder AI-fabricated pseudo-science (invented precision like "ERα mediates 90-95% of closure") into what's presented as a curated evidence base. Flagged directly to the user.
- 12 genuine papers read and ingested as on-topic, several extending the epSSC/GH-axis and estrogen-receptor-mechanism threads: [[Membrane-Effects-Sex-Hormones-Growth-Plate-Chondrocytes-Thesis|ElBaradie 2012 (PhD thesis)]] (rapid, sex-specific — female-only — membrane PKC activation by estradiol in growth-plate chondrocytes, requiring both ERα+ERβ and receptor palmitoylation — a fifth distinct ER mechanism for this domain), [[ERalpha-DNA-Damage-Chondrocyte-Senescence-Osteoarthritis|Zhang et al. 2023]] (a second ligand-independent ERα role, suppressing DNA-damage-induced chondrocyte senescence in OA), [[Letrozole-Long-Term-McCune-Albright-Precocious-Puberty|Estrada et al. 2016]] (longest-follow-up letrozole study in MAS precocious puberty — a synthesis-blockade companion to the domain's existing fulvestrant/receptor-blockade source for the same condition), [[IGF1-GH-Differential-Effects-Growth-Plate-Hunziker|Hunziker et al. 1994]] and two Gevers papers (1996, 2009) extending the GH-IGF-1 axis's growth-plate-zone and single-cell-resolution history.
- 5 papers flagged off-topic: oncology/PK letrozole and fulvestrant papers, a postoperative-delirium insulin study, a germ-cell-differentiation stem-cell paper, and a general glutathione review.
- One FDA drug label (erdafitinib/BALVERSA) processed as public information — same FGFR-inhibitor drug class as TYRA-300 already in this domain, but oncology application; distinct from the still-untouched confidential Janssen clinical trial documents for the same drug.
- Pages updated: [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]], [[Growth Hormone-IGF-1 Axis]], [[Testosterone]], [[Aromatase]], [[Three Estrogen Receptor Mechanisms in the Growth Plate]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 17 PDFs moved to `.raw/Studies/`. 6 non-scientific files + 1 unreadable scanned PDF (thyroid/GH-axis interactions paper, 0 extractable characters) + 2 failed image reads left untouched in the queue.
- Endocrinology domain now at 72 on-topic sources + 30 unrelated. 181 pages vault-wide, 121 sources ingested. Queue down to 299 files.

---

## [2026-07-26] batch ingest | Studies backlog, batch 5 (large autonomous batch — 22 sources, 2 duplicates)
- First fresh 25-file preview pulled after closing batch 4 entirely and building the synthesis documents. Caught 2 more dedup misses (different-hash duplicates of already-ingested/already-in-this-batch papers): `90-6601629a.pdf` (dup of `6601629.pdf`, Osborne et al. 2004 fulvestrant review, both flagged off-topic) and `753f1609b04e4696f4ac6ec6a0f9ea00.pdf` (dup of the already-ingested [[Growth-Hormone-Androgen-Synergy-Hypopituitary-Dwarfs]] 1974 paper). One file left untouched and flagged to the user: a Janssen/erdafitinib Clinical Protocol explicitly marked "CONFIDENTIAL — Company trade secrets," same handling as the earlier Statistical Analysis Plan from this sponsor.
- 14 papers read and ingested as on-topic, two of them extending the newly-built [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]] concept directly: [[PTHrP-Resting-Chondrocytes-Wnt-Inhibitory-Environment|Hallett et al. 2021]] (PTHrP+ resting chondrocytes require a Wnt-*inhibitory* environment to stay stem-like — a second, independent signaling requirement alongside Hedgehog activation) and [[Depletion-Resting-Zone-Chondrocytes-Growth-Plate-Senescence|Schrier et al. 2006]] (the primary experimental paper behind Nilsson & Baron's finite-capacity model — direct BrdU evidence of age-dependent resting-zone depletion, plus a genuine anomaly: estrogen accelerates senescence without increasing resting-zone proliferation or depletion, an unresolved mechanism even in the authors' own data).
- Other notable finds: [[Aromatase-Inhibitors-Short-Stature-Cochrane-Review|McGrath & O'Grady 2015 (Cochrane)]] — the domain's highest-evidence-quality AI-for-height source, finding no solid RCT evidence for final-height benefit (only short-term growth-velocity benefit) plus a 45% vertebral-abnormality safety signal, sitting in real tension with [[Aromatase-Inhibitors-Near-Final-Height-Males|Bouliari et al. 2026]]'s more optimistic framing; [[DHT-Estrogen-Combined-Bone-Density-Growth-Ovariectomized-Rats|Coxam et al. 1996]] (DHT+estrogen simultaneously synergistic on bone density and opposing on longitudinal growth, in the same animals); [[MRI-Growth-Plate-Closure-Adolescents-Kvist|Kvist et al. 2021]] (958-subject human MRI dataset, largest population fusion-timing data in this domain, co-authored by Ola Nilsson); [[SOCS2-Accelerated-Growth-Plate-Fusion-Osteoarthritis|Samvelyan et al. 2022]] (GH-signaling-driven accelerated fusion does NOT increase OA vulnerability — a useful null result); [[Genistein-Estradiol-ATDC5-Chondrogenesis-TGFbeta|Takeda et al. 2025]] (a phytoestrogen effect on chondrogenesis that is estrogen-receptor-*independent*, running through TGF-β instead — contrasts with S-equol's ER-dependent mechanism already in this domain).
- 8 papers flagged off-topic: 3 more fulvestrant/oncology papers, a neuropharmacology MAO-inhibitor paper, a Thai aquaculture thesis on androgen-induced tilapia masculinization, an IVF/fertility hCG-FSH trial, a urogynecology estriol-cream PK study, and a physical-anthropology hunter-gatherer bone-growth thesis. One additional file (`AG_2023-36-03.pdf`) turned out to be an entire 785,000-character journal issue rather than a single paper — flagged as a misplaced/bulk file rather than split into per-article pages.
- Pages updated: [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]], [[PTHrP-Ihh Feedback Loop]], [[Aromatase]], [[Growth Hormone-IGF-1 Axis]], [[Testosterone]], [[Estrogen Receptor (ER)]], [[Sox9]], [[Estrogen vs Androgen in Male Bone Health]], [[Epiphyseal Fusion Mechanisms]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 24 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/` (22 new sources + 2 duplicates).
- Endocrinology domain now at 60 on-topic sources + 25 unrelated. 164 pages vault-wide, 104 sources ingested. Queue down to 316 files.

---

## [2026-07-26] synthesis | Three new cross-cutting documents connecting overlapping themes
- User asked explicitly to "think about ways to connect ideas... make more documents of interesting overlapping themes and concepts" rather than only continuing per-paper source ingestion. Built the three strongest candidates identified from the now-45-source Endocrinology corpus:
  1. [[Epiphyseal Skeletal Stem Cells and Hedgehog Signaling]] (new concept) — consolidates the PTHrP+ resting-zone stem cell cluster: [[Skeletal-Stem-Cells-Growth-Plate-Hedgehog-Signaling|Trompet et al. 2024]] (functional proof epSSCs drive linear growth), [[Hedgehog-Resting-Zone-Chondrocytes-Osteoblast-Transformation|Orikasa et al. 2023]] (same genetic lever, different readout — cell fate not proliferation), [[Human-Growth-Plate-Transcriptional-Atlas-GH-Stem-Cells|Chu et al. 2025]] (human-tissue confirmation + GH-direct-stimulation), [[Dynasore-Hormetic-Bone-Growth|Marchan-Alvarez et al. 2026]] (growth via matrix accumulation, decoupled from proliferation) — tied explicitly back to [[Growth-Plate-Senescence-Epiphyseal-Fusion-Review|Nilsson & Baron 2004]]'s abstract "finite proliferative capacity" model, now given a concrete cellular identity.
  2. [[PTHrP-Ihh Feedback Loop]] (new vocabulary page) — the classical paracrine circuit, previously only described inline (Shim 2015) or implicitly perturbed (Trompet/Orikasa's Patched1 lever) or explicitly measured (Chou et al.'s PTHrP/Ihh ratio mechanism for GPER-1) across 4 sources without ever getting its own page despite clearing the same 3+-mention threshold used for Sox9/Runx2/etc.
  3. [[Three Estrogen Receptor Mechanisms in the Growth Plate]] (new comparison) — direct side-by-side of [[ERalpha-AF1-Growth-Plate-Closure-Female-Mice|Börjesson et al. 2012]] (ERα, AF-1-independent, drives closure), [[GPER1-Chondrocyte-Proliferation-PTHrP-Ihh|Chou et al. 2025]] (GPER-1, drives proliferation via PTHrP/Ihh, opposite direction), and [[ERalpha-Mechanotransduction-Chondrocytes-Review|Wang et al. 2023]] (ERα again, but ligand-independent, triggered by mechanical load not estrogen) — three structurally distinct systems sharing an estrogen-receptor name, none of the three papers citing either of the others.
- Cross-linked all three into [[Epiphyseal Fusion Mechanisms]], [[Estrogen Receptor (ER)]], [[Endocrinology]] domain, `concepts/_index`, `index`.
- No new source PDFs ingested this pass — pure synthesis over the existing corpus. 136 pages vault-wide (up from 133), sources ingested unchanged at 76.

---

## [2026-07-26] batch ingest | Studies backlog, batch 4 continued (6 papers, closes the batch-4 preview)
- Read and ingested the 6 papers deferred from the earlier batch-4 preview: [[Hedgehog-Resting-Zone-Chondrocytes-Osteoblast-Transformation|Orikasa et al. 2023]] (Hedgehog-activated PTHrP+ resting-zone chondrocytes form "patched roses" and transform directly into trabecular osteoblasts — cited as ref 18 in Trompet et al. 2024), [[Dynasore-Hormetic-Bone-Growth|Marchan-Alvarez et al. 2026]] (dynasore has a hormetic/biphasic effect on ex vivo bone elongation — low dose increases growth via matrix accumulation despite reduced proliferation; high dose abolishes both), [[Nandrolone-Achondroplasia-Case-Report|Al-Mosawi 2006]] (single-patient case report, nandrolone growth benefit in achondroplasia), [[Deca-Durabolin-Reproductive-Organ-Damage-Rats|Zabiba 2017]] (high-dose nandrolone reproductive-organ toxicity in rats), [[TD-198946-Intervertebral-Disc-Regeneration|Kushioka et al. 2020]] (TD-198946 small molecule promotes intervertebral disc GAG synthesis via PI3K/Akt), and [[ERalpha-Mechanotransduction-Chondrocytes-Review|Wang et al. 2023]] (a fourth, ligand-independent ERα mechanism — mechanotransduction in chondrocytes, distinct from the AF-1/closure, classical genomic, and GPER-1 roles already in this domain).
- The Nandrolone-Achondroplasia and Deca-Durabolin papers together with the earlier Nandrolone-Telomere-Elongation source now sketch a genuine dose/context-dependent risk-benefit spectrum for the same drug (nandrolone/Deca-Durabolin), folded into [[Testosterone]].
- Pages updated: [[Estrogen Receptor (ER)]], [[Sox9]], [[Testosterone]], [[Skeletal-Stem-Cells-Growth-Plate-Hedgehog-Signaling]] (cross-linked to the new epSSC-cluster papers), [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 6 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`.
- Endocrinology domain now at 45 on-topic sources. 133 pages vault-wide, 76 sources ingested.
- **Still deferred**: 2 fulvestrant-breast-cancer papers (likely off-topic/oncology), the large 1994 growth-promotion MD thesis (on-topic, needs strategic partial reading given its size), 2 confirmed-off-topic files needing formal flagged source pages (Russian COVID/interferon paper, 1973 ophthalmology fluorescence paper), and one non-paper PNG ("heightmaxxing" iceberg image, not yet assessed).
- **User request not yet started**: build standalone synthesis documents connecting overlapping themes across the corpus — an epSSC/Hedgehog-signaling concept page, a PTHrP/Ihh feedback-loop vocabulary page, and a three-way Estrogen-Receptor-mechanisms comparison page (ERα/AF-1 closure vs. GPER-1 proliferation vs. ERα mechanotransduction) are the strongest ready-made candidates given how much material now exists.

---

## [2026-07-26] batch ingest | Studies backlog, batch 4 (3 papers + manual duplicate catch)
- Caught and resolved one dedup miss: `165226.1-...-e0fd13ba177f913fd3156f593ead4cfd 2.pdf` was a content-duplicate (same Trompet et al. 2024 paper, different PDF rendering/hash) of an already-ingested source that hash-based dedup couldn't catch. Moved to `Studies/` with a manual `duplicate_of` note, no re-ingestion.
- Read and ingested 3 papers, all directly extending the growth-plate stem-cell/estrogen-receptor threads already in this domain: [[Growth-Plate-Senescence-Epiphyseal-Fusion-Review|Nilsson & Baron 2004]] (foundational, highly-cited reframing: epiphyseal fusion is the *result* of resting-zone stem cells exhausting finite proliferative capacity, not an independently-triggered event — explains why estrogen-exposure duration needed for fusion varies by age), [[GPER1-Chondrocyte-Proliferation-PTHrP-Ihh|Chou et al. 2025]] (introduces GPER-1, a third estrogen receptor, which does the *opposite* of ERα — promotes proliferation/delays hypertrophy via PTHrP/Ihh — confirmed via agonist, antagonist, knockout, and cell culture), [[Human-Growth-Plate-Transcriptional-Atlas-GH-Stem-Cells|Chu et al. 2025]] (first human-tissue transcriptomic atlas of growth-plate stem cells, from the same Chagin lab as Trompet et al. 2024; GH directly stimulates human stem-cell proliferation via JAK/STAT/TGFβ/ERK, not just via liver IGF-I).
- Pages updated: [[Estrogen Receptor (ER)]], [[Growth Hormone-IGF-1 Axis]], [[Epiphyseal Fusion Mechanisms]], [[Estrogen vs Androgen in Male Bone Health]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 3 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`.
- Endocrinology domain now at 39 on-topic sources. 127 pages vault-wide, 70 sources ingested.
- **Deferred from this batch's preview** (15 files previewed, 3 read/ingested + 1 duplicate resolved): Orikasa et al. 2023 (Hedgehog/resting-zone chondrocytes → osteoblasts, cited directly in Trompet et al. as ref 18 — high priority), a Dynasore/dynamin-inhibitor bone-growth paper, a nandrolone/achondroplasia case report, a Deca-Durabolin reproductive-organs paper, a TD-198946/intervertebral-disc paper, the already-identified canonical mechanotransduction/ERα paper, 2 fulvestrant-in-breast-cancer papers (likely off-topic, oncology-focused), a large 1994 MD thesis on growth promotion in short children, and 2 files confirmed off-topic (Russian COVID/interferon paper, ophthalmology fluorescence-detection paper) plus a "heightmaxxing" PNG image (not a research document, not yet assessed).

---

## [2026-07-26] batch ingest | Studies backlog, batch 3c (final 7 — closes out batch 3 entirely)
- Assessed the last 7 files from batch 3's original preview: 1 genuinely on-topic ([[Peptide-Regulation-Chondrogenic-Stem-Cell-Differentiation|Linkova et al. 2023]], "Peptide Regulation of Chondrogenic Stem Cell Differentiation" — independently corroborates the Sox9 dual-role and Runx2/Runx3 findings from [[Sox9-Growth-Plate-Chondrocyte-Fate|Dy et al. 2012]] and [[Chondrogenesis-Osteoarthritis-Review|Goldring 2012]] from a wholly separate research group, plus substantial peptide-therapeutics overlap with [[Chondroinductive-Peptides-Cartilage-Regeneration|Liao et al. 2024]]) and 6 off-topic: [[H19-Gene-Silencing-Rhabdomyosarcoma|Lynch et al. 2002]] (cancer epigenetics) plus a 5-paper cluster from the Khavinson "peptide bioregulator" research tradition (St. Petersburg Institute of Bioregulation and Gerontology) covering diabetes gene regulation, plant tissue culture, immunosenescence, and general peptide-pharmacology commentary — none touching steroid hormones or growth-plate biology despite sharing lead authorship with the on-topic chondrogenic paper.
- Pages updated: [[Sox9]], [[Runx2]], [[Molecular Regulators of Growth Plate Chondrocyte Maturation]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 7 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`.
- **This closes out batch 3 entirely and the whole original ~30-file two-round preview set from this session.** Endocrinology domain now at 36 on-topic sources + 12 flagged-unrelated. 124 pages vault-wide, 67 sources ingested.
- Next session should pull a genuinely fresh batch from the ~356 true-unique-remaining queue (`.raw/Studies yet to analyze/`, excluding the `_duplicates/` subfolder).

---

## [2026-07-26] batch ingest | Studies backlog, batch 3b (3 more papers, closes out this batch's on-topic set)
- Read and ingested the 3 remaining on-topic papers previewed in batch 3: [[Fulvestrant-Precocious-Puberty-McCune-Albright|Sims et al. 2012]] (pure ER antagonist fulvestrant slows bone-age advancement in McCune-Albright precocious puberty without tamoxifen's uterine-volume side effect — first pediatric use of this drug), [[Dietary-Supplement-DHT-Testosterone-Estradiol-Dose-Response|Angwafor & Anderson 2008]] (commercially-funded, weakly-controlled supplement study claiming simultaneous 5α-reductase + aromatase inhibition), [[Testosterone-Liver-Kidney-Function-Rabbits|Elesawi et al. 2019]] (supraphysiological/athletic-misuse-level testosterone doses cause dose-dependent liver/kidney damage markers in rabbits).
- Pages updated: [[5-Alpha-Reductase]], [[Aromatase]], [[Testosterone]], [[Estrogen Receptor (ER)]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 3 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`.
- **This closes out all on-topic papers from batch 3's original 15-file preview.** Endocrinology domain now at 35 on-topic sources. 117 pages vault-wide, 60 sources ingested.
- **Still to assess from this batch**: an H19/rhabdomyosarcoma epigenetics paper (likely off-topic, not yet formally read), and a 6-paper Khavinson/peptide-bioregulator cluster (distinct Russian gerontology research tradition — needs a relevance determination before deciding whether to read fully or flag as off-topic).

---

## [2026-07-26] batch ingest | Studies backlog, batch 3 (4 papers, first fresh batch post-cleanup)
- First batch pulled from the cleaned-up queue. Read and ingested 4 papers: [[Skeletal-Stem-Cells-Growth-Plate-Hedgehog-Signaling|Trompet et al. 2024]] (epiphyseal skeletal stem cells + Hedgehog signaling drive linear bone growth — first functional proof; co-authored by Andrei Chagin, already central to this domain via the 2009 AR paper), [[Aromatase-Inhibitors-in-Men-Effects-Therapeutic-Options|de Ronde & de Jong 2011]] (comprehensive AI-in-men review — height benefit in boys is solid, but AI-driven testosterone increase in older hypogonadal men consistently fails to improve strength/body composition), [[DHEA-and-the-Skeleton-Review|Gordon et al. 1999]] (DHEA acts on bone via three parallel pathways simultaneously: direct AR-mediated, aromatization to estrogen, and IGF-I stimulation — plus an IL-6-suppression mechanism shared with DHT and testosterone), [[TYRA-300-FGFR3-Inhibitor-Chondrodysplasia|Starrett et al. 2025]] (FGFR3-selective inhibitor restores growth-plate architecture and corrects skeletal complications in two chondrodysplasia mouse models — introduces the FGFR3 signaling axis to this domain, industry-funded with disclosed COI).
- Pages updated: [[Aromatase]], [[Dihydrotestosterone (DHT)]], [[Androgen Receptor (AR)]], [[Growth Hormone-IGF-1 Axis]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 4 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`.
- Endocrinology domain now at 32 on-topic sources. 114 pages vault-wide, 57 sources ingested.
- **Deferred from this batch's preview** (11 fresh files previewed, 4 read/ingested): 1 file (H19/rhabdomyosarcoma epigenetics paper) likely off-topic, not yet formally read/flagged; 6 files form a distinct Khavinson/peptide-bioregulator sub-cluster (Russian gerontology research tradition) not yet assessed for topical fit; 3 files still on the to-read list (testosterone/liver/kidney rabbits, DHT/testosterone/estradiol supplement study, Fulvestrant/McCune-Albright precocious puberty).

---

## [2026-07-26] maintenance | Studies queue dedup cleanup
- Resolved all 58 duplicate files identified in the batch-2 rescan, now that file locations had shifted from further ingest progress.
- 6 files were exact duplicates of already-ingested sources (re-verified by hash against the current manifest, since some "originals" from the earlier rescan had since been moved to `Studies/`): moved to `.raw/Studies/` with a `duplicate_of` manifest note, no source page created (matching the `out.pdf`/`wiren1999.pdf` precedent).
- 52 files were internal duplicates where *neither* copy had been ingested yet: kept one canonical copy per hash in `.raw/Studies yet to analyze/`, moved the other 40 redundant copies into a new `.raw/Studies yet to analyze/_duplicates/` subfolder (not deleted — just parked out of the active queue so they don't inflate the apparent file count or get double-processed).
- **Queue folder now shows 370 genuinely unique unprocessed files** (down from the confusing ~428 total), matching the earlier ~385 estimate closely (the gap accounted for by files ingested in the interim and the 6 already-ingested duplicates found in this pass).
- No wiki content changes this pass — purely a bookkeeping/dedup maintenance operation on `.raw/`.

---

## [2026-07-26] batch ingest | Studies backlog, batch 2d (final 4 — closes out entire batch 1-2 preview set)
- Read and ingested the last 4 deferred papers: [[Chondrogenesis-Osteoarthritis-Review|Goldring 2012]] (OA/cartilage review, independently corroborates Sox9-inhibits-Runx2 from Dy et al., extends the concept into disease context), [[Chondroinductive-Peptides-Cartilage-Regeneration|Liao et al. 2024]] (peptide-based chondrogenic induction review, Sox9 as the near-universal in vitro readout, near-total lack of in vivo validation across all peptides surveyed), [[Nandrolone-Telomere-Elongation-Bone-Marrow-Failure|Clé et al.]] (androgen therapy for telomere elongation in bone marrow failure — a hematology application of androgen pharmacology, distinct target tissue from this domain's bone/growth-plate focus), [[11-Oxygenated-Androgens-PCOS-Hirsutism-Thesis|Varausová 2023]] (Czech-language thesis, read via its English abstract only — 11-oxygenated adrenal-derived androgens as a non-classical potent-androgen pathway relevant to PCOS/hirsutism).
- Pages updated: [[Sox9]], [[Runx2]], [[Testosterone]], [[Dihydrotestosterone (DHT)]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 4 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`.
- **This closes out the entire preview set from batches 1 and 2** (originally ~15+15 files previewed across two rounds). Endocrinology domain now at 28 on-topic sources + 6 flagged-unrelated. 110 pages vault-wide, 53 sources ingested.
- Next session should pull a genuinely fresh batch from the true-unique-remaining queue (~385 files, though the folder still shows ~428 due to unresolved internal duplicates found during the rescan — see the batch-2 log entry for the dedup list, not yet acted on).

---

## [2026-07-26] batch ingest | Studies backlog, batch 2c (closing out remaining deferred/flagged files)
- Read and ingested [[Prenatal-Androgen-Excess-Multigenerational-Effects|Abruzzese et al. 2023]] (rat PCOS model: prenatal testosterone excess programs metabolic/reproductive effects across 2 generations via BOTH maternal and paternal lines independently — a reproductive-endocrinology/developmental-programming angle on androgen excess, distinct from this domain's bone/growth-plate focus but still squarely androgen pharmacology).
- Formally read and flagged 3 more off-topic files (same convention as nootropics/HDAC2/Neervannan): [[Neurosteroids-GABAergic-Allopregnanolone|Liang & Rasmusson]] (progesterone-derived GABAergic neurosteroids, psychiatric context — different steroid class), [[Subcutaneous-Injection-Pain-Factors-Review|Usach et al. 2019]] (generic drug-delivery pharmaceutics review), [[BPC-157-Musculoskeletal-Healing-Review|McGuire et al. 2025]] (a peptide, not a steroid hormone — different pharmacological class despite shared "musculoskeletal" surface keyword).
- **Not ingested, left in queue untouched**: `11826.pdf` — on inspection this is a Cayman Chemical product Safety Data Sheet (a vendor document, not a research paper at all: hazard warnings, handling instructions, no scientific content to summarize). Flagged to the user rather than given a source page, since there is no research content to extract.
- Pages created: 4 source pages (1 on-topic, 3 flagged-unrelated). Pages updated: [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 4 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/` (excluding the Cayman SDS, left in place).
- **Still deferred for a future session**: 2 cartilage-biology reviews (`10.1177_1759720X12448454.pdf`, `10.1177_19476035241276406.pdf`), a nandrolone/telomere-elongation paper (`1081300.pdf`, previewed — androgen pharmacology but hematology target tissue, borderline domain fit), and a Czech-language PCOS/adrenal-androgens thesis (`130372325.pdf`, on-topic but language barrier). This closes out the entire first-two-batches preview set except for these 4 files.

---

## [2026-07-26] batch ingest | Studies backlog, batch 2b (2 papers, closing out deferred set)
- Read and ingested 2 of the 7 papers deferred from batch 2: [[Trenbolone-Extremity-Bones-Running-Rats|Sarı & Lök 2019]] (trenbolone numerically but not statistically shortened rat long bones — flagged the paper's own conclusion as outrunning its statistics) and [[Thyroid-Hormone-Receptor-Skeletal-Phenotypes|O'Shea et al. 2005]] (introduces thyroid hormone as a new hormonal axis in this domain — same PV mutation in TRβ vs. TRα1 produces opposite skeletal phenotypes depending on which receptor is tissue-dominant; GH/IGF-I receptor expression in the growth plate moves in lockstep).
- Pages updated: [[Growth Hormone-IGF-1 Axis]], [[Testosterone]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 2 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`.
- **Still deferred**: 2 cartilage-biology reviews, a prenatal-androgen-excess/multigenerational epigenetics paper, a nandrolone/telomere-elongation paper, and a Czech-language PCOS/adrenal-androgens thesis — plus the 4 likely off-topic files (neurosteroids review, Cayman Chemical SDS, subcutaneous-injection review, BPC-157 peptide review) still not formally read/flagged.

---

## [2026-07-26] batch ingest | Studies backlog, batch 2 (4 papers) + queue rescan
- Rescanned all 444 remaining files in `.raw/Studies yet to analyze/` for duplicates (both against the manifest and internally within the folder): found 1 exact duplicate of an already-ingested file (`0008-5472.CAN-07-2822.pdf`, dup of the already-ingested HDAC2/breast-cancer paper) and 58 internal duplicate pairs within the folder itself (e.g. `12902_2015_Article_80.pdf` == `12902_2015_Article_80 (1).pdf`). This cuts the true remaining unique-file count from 444 to ~385. Duplicates left in place for now (not yet moved/purged) — flagged for cleanup in a future pass.
- Previewed 15 fresh files; 4 read in full and ingested (all extend existing [[Endocrinology]] vocabulary/comparison pages): [[ERalpha-AF1-Growth-Plate-Closure-Female-Mice|Börjesson et al. 2012]] (ERα's AF-1 domain specifically opposes growth-plate closure — direct experimental support for the apoptosis theory in [[Epiphyseal Fusion Mechanisms]] in this specific genetic model), [[Sox9-Localization-Magnesium-Deficient-Rat-Growth-Plate|Gruber et al. 2004]] (dietary magnesium deficiency reduces Sox9 localization in rat cartilage), [[AR-Overexpression-Chondrogenic-Rabbit-Articular-Chondrocytes|Liu et al. 2021]] (AR overexpression protects rabbit articular chondrocytes via reduced apoptosis + mTOR inhibition, distinct mechanism from growth-plate AR effects), [[GH-Dose-IGF1-Pubertal-Height-Gain|Lundberg et al. 2015]] (rigorous RCT: higher pubertal GH dose → greater IGF-I rise → greater height gain, dose-response quantified).
- Pages updated: [[Estrogen vs Androgen in Male Bone Health]], [[Epiphyseal Fusion Mechanisms]], [[Molecular Regulators of Growth Plate Chondrocyte Maturation]], [[Estrogen Receptor (ER)]], [[Androgen Receptor (AR)]], [[Sox9]], [[Growth Hormone-IGF-1 Axis]], [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 4 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`; the exact-duplicate file (`0008-5472.CAN-07-2822.pdf`) also moved with a `duplicate_of` manifest note (matching the `out.pdf`/`wiren1999.pdf` precedent from earlier batches) rather than being re-ingested.
- **Deferred for next session** (previewed but not yet read in full): `10.1177_1759720X12448454.pdf` and `10.1177_19476035241276406.pdf` (both cartilage-biology reviews, on-topic), `10.15314-tsed.555015-812541.pdf` (trenbolone/bone in rats, on-topic), `10.1210@me.2005-0224.pdf` (thyroid hormone receptor + skeletal phenotype, on-topic, new hormone axis for domain), `10.1177_11795514231196461.pdf` (prenatal androgen excess, multigenerational epigenetics, on-topic), `1081300.pdf` (nandrolone/telomere elongation — androgen pharmacology but different target tissue, borderline), `130372325.pdf` (Czech-language thesis on adrenal androgens in PCOS/hirsutism, on-topic but language barrier).
- **Likely off-topic, previewed only** (not yet formally flagged with full read): `10.1177_2470547018818555.pdf` (neurosteroids/allopregnanolone, psychiatric — different steroid class/context), `11826.pdf` (a Cayman Chemical product safety data sheet, not a research paper at all), `12325_2019_Article_1101.pdf` (subcutaneous injection pain review, pharmaceutics not hormones), `12178_2025_Article_9990.pdf` (BPC-157 peptide review, different drug class entirely).

---

## [2026-07-26] structural change | Vocabulary subfolder + 9 pharmacological glossary pages
- User request: "make more subfolders. critical pharmacological vocabulary concepts overlapping in multiple studies i want you to make documents of explained and containing every study which mentions that and in what way."
- New subfolder: `wiki/concepts/vocabulary/` — first subfolder introduced under `concepts/`, holding cross-cutting pharmacological term pages distinct from the existing thematic concept pages.
- Method: grepped all 17 on-topic Endocrinology source pages for candidate terms, kept ones appearing in 3+ sources, then wrote one page per term with a "Studies Mentioning This Term" section — one bullet per source explaining specifically *how* that source uses/discusses the term, not just that it's present.
- 9 pages created: [[Aromatase]] (7 sources), [[Androgen Receptor (AR)]] (6), [[Dihydrotestosterone (DHT)]] (8 — the domain's most cross-referenced term), [[Estrogen Receptor (ER)]] (4 — notably bridges Endocrinology and Health and Nutrition domains via the Tualang honey paper's ERβ mechanism), [[5-Alpha-Reductase]] (3), [[Sox9]] (3), [[Runx2]] (3), [[Growth Hormone-IGF-1 Axis]] (4), [[Testosterone]] (9).
- Key insight surfaced by this exercise: Estrogen Receptor is the first genuine cross-domain vocabulary bridge in the vault — both the Endocrinology domain's phytoestrogen paper (S-equol) and the Health and Nutrition domain's honey/bone paper (Zaid et al. 2012) independently land on ERβ as the more bone-relevant estrogen receptor subtype.
- Pages updated: `concepts/_index`, [[Endocrinology]] domain, `index`.
- This is now the established pattern for future study batches: as new pharmacological terms accumulate 3+ source mentions, add or update their vocabulary page rather than only writing per-paper source pages.
- Excluded one false-positive grep hit: [[Nootropics-Cognitive-Enhancers]] matched "aromatase"/"androgen receptor" only because its own source page's contradiction-callout text contains those words describing why it's unrelated — the actual paper doesn't discuss either term. Verified before excluding.

---

## [2026-07-26] batch ingest | Studies backlog, batch 1b (4 papers, completing the first preview set)
- Completed the remaining papers from the first ~15-file preview batch of `.raw/Studies yet to analyze/`.
- On-topic, ingested into [[Endocrinology]]: [[S-Equol-Estrogen-Receptor-Anti-Androgen|Setchell et al. 2005]] (S-equol, a gut-bacteria-derived selective ERβ ligand that is also a direct DHT-sequestering anti-androgen — a third distinct anti-androgen mechanism alongside AR blockade and 5α-reductase inhibition), [[Cartilage-Tissue-Engineering-Small-Molecules|Li et al. 2020]] (applied cartilage tissue-engineering review, cross-linked to [[Molecular Regulators of Growth Plate Chondrocyte Maturation]]).
- Flagged as unrelated to the domain (ingested as standalone sources, not cross-linked into concepts, following the established nootropics-flag convention): [[HDAC2-Progesterone-Receptor-Breast-Cancer|Bicaku et al. 2008]] (breast cancer/HDAC epigenetics — shares only the surface keyword "estrogen receptor"), [[Preclinical-Formulations-Drug-Discovery-Toxicology|Neervannan 2006]] (generic drug-formulation/pharmaceutics review, no hormone/bone content at all).
- **Not ingested, left in queue**: `0003-3219%281993%29063%3C0289%3Aasacgi%3E2.0.co%3B2 (1).pdf` — text extraction produced only 9 characters (likely a scanned, non-OCR'd PDF); needs OCR tooling not currently available in this environment. Left in `.raw/Studies yet to analyze/`, not added to manifest, not moved.
- **Not ingested, flagged to user directly rather than processed**: `0a00d5dd5ec9d31fe4812dfc1e93b178.pdf` — identified as a Janssen Research & Development Phase 2 clinical trial Statistical Analysis Plan for erdafitinib (JNJ-42756493), explicitly marked "trade secrets and commercial information that are privileged or confidential." Judged inappropriate to extract/summarize into a personal research wiki regardless of topical fit. Left untouched in `.raw/Studies yet to analyze/`; the user should decide whether this file belongs in the source folder at all.
- Pages created: 4 source pages (2 on-topic, 2 flagged-unrelated). Pages updated: [[Endocrinology]] domain, `sources/_index`, `index`, `hot`, `.raw/.manifest.json`.
- 4 PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/`; 2 files (the confidential SAP and the unreadable scan) intentionally left in place.

---

## [2026-07-26] batch ingest | Studies backlog, batch 1 (9 papers from .raw/Studies yet to analyze/)
- Source folder: `.raw/Studies yet to analyze/` (397 unique new files identified via MD5 hash against manifest; this is the first real processing batch, 9 of ~15 previewed files fully read and ingested)
- Sources: [[DHT-Prevents-Glucocorticoid-Effects-Fetal-Bone|Picherit et al. 2000]], [[Growth-Hormone-Androgen-Synergy-Hypopituitary-Dwarfs|1974 GH+androgen trial]], [[Androgen-Receptor-Modulation-No-Effect-Growth-Plate|Chagin et al. 2009]], [[Testosterone-Metabolism-Rabbit-Cartilage|Takahashi et al. 1984]], [[Sex-Steroid-Regulation-Cartilage-Bone-Proliferation|Somjen et al. 1991]], [[Letrozole-Bone-Laying-Hens|Letrozole in Laying Hens]], [[Role-of-Growth-Plate-Longitudinal-Bone-Growth|Pines & Hurwitz review]], [[Dlx5-Chondrocyte-Differentiation|Ferrari & Kosher 2002]], [[Sox9-Growth-Plate-Chondrocyte-Fate|Dy et al. 2012]]
- Pages created: 9 source pages, 1 new concept ([[Molecular Regulators of Growth Plate Chondrocyte Maturation]]), 1 new comparison ([[Aromatase Inhibition and Bone - Mammals vs Egg-Laying Birds]])
- Pages updated: [[Estrogen vs Androgen in Male Bone Health]] (4 new sources added — Picherit, Chagin, Takahashi, Somjen), [[Epiphyseal Fusion Mechanisms]], [[Endocrinology]] domain, `sources/_index`, `concepts/_index`, `index`, `hot`, `.raw/.manifest.json`
- All 9 source PDFs moved from `.raw/Studies yet to analyze/` to `.raw/Studies/` after ingest, per user instruction.
- Key insight: this batch surfaced a genuine primary-source-to-primary-source disagreement — Chagin et al. 2009 explicitly cites and discusses Picherit et al. 2000 (their reference 27), disputing whether direct androgen receptor activation drives growth-plate longitudinal growth. This is now documented as the sharpest tension in [[Estrogen vs Androgen in Male Bone Health]], distinct from the rest of the comparison's bench-vs-bedside framing since here the "bench" sources disagree with each other.
- Also found a clean species-level contrast worth its own comparison page: aromatase inhibition (letrozole) increases bone strength in laying hens but risks decreasing it in mammals (per the existing Bouliari et al. source) — reconciled via avian medullary-bone/eggshell-calcium physiology in [[Aromatase Inhibition and Bone - Mammals vs Egg-Laying Birds]].
- Remaining from this preview batch of ~15: 2 on-topic papers not yet read in full (S-equol; HDAC2/progesterone receptor) and 3-4 likely off-topic files not yet formally assessed (drug-formulation review, an oncology clinical-trial SAP, one PDF that failed text extraction) — left in `.raw/Studies yet to analyze/` for a future session.
- This is batch 1 of what will be many batches against a 397-file backlog; continuing across sessions without per-file permission prompts, per user's explicit request.

---

## [2026-07-26] batch ingest | Growth Plates batch (7 papers from .raw/Growth Plates/)
- Source folder: `.raw/Growth Plates/` (8 files; `wiren1999.pdf` and `wiren1999 (1).pdf` were byte-identical duplicates — only one ingested)
- Sources: [[Pubertal-Growth-and-Epiphyseal-Fusion|Shim 2015]], [[Aromatase-Inhibitors-Near-Final-Height-Males|Bouliari et al. 2026]], [[Aromatase-in-the-Human-Brain|Azcoitia et al. 2021]], [[Dihydrotestosterone-Clinical-Implications|Swerdloff et al. 2017]], [[Androgen-Receptor-Upregulation-Osteoblasts|Wiren et al. 1999]], [[Hormones-and-Antioxidant-Systems|Mancini et al. 2010]], [[Nootropics-Cognitive-Enhancers|Malík & Tlustoš 2022]] (flagged unrelated — see below)
- Pages created: 7 source pages, 1 new concept ([[Epiphyseal Fusion Mechanisms]]), 3 new comparison pages ([[Aromatase Across Tissues]], [[Estrogen vs Androgen in Male Bone Health]], [[Aromatase Inhibitors - Height Therapy vs Neuro-Sensory Side Effects]]), 1 new domain ([[Endocrinology]])
- Pages updated: `domains/_index`, `sources/_index`, `concepts/_index`, `index`, `hot`, `.raw/.manifest.json`
- User explicitly asked to "write all concepts that are overlapping in documents comparing how they do" — this ingest was framed around finding concepts shared across ≥2 papers and writing them as comparison pages (matching the wiki's `type: comparison` schema) rather than the usual single-theme concept-cluster approach used for the Honey batch.
- Key insight: aromatase (the androgen→estrogen enzyme) is the connective thread across 4 of the 6 relevant papers, but its inhibition has tissue-specific — sometimes opposite — consequences (delays growth-plate closure = taller, beneficial; blocks brain estrogen = cognitive/sensory side effects, mixed epilepsy effects; blocks cardiovascular aromatization = loses part of testosterone's vasoprotective signaling). A second real tension: whole-body/clinical evidence says estrogen (via aromatization) dominates male bone health, but a 1999 cell-culture study (Wiren et al.) shows DHT has its own genuine, receptor-specific, non-aromatized effect on osteoblasts that the later clinical consensus doesn't explicitly reconcile.
- Flagged discrepancy: `nutrients-14-03367.pdf` (nootropics/cognitive enhancers) was in this folder but has no substantive topical connection to growth plates/hormones — ingested as a standalone source, not linked into the Endocrinology domain's concepts, and the mismatch was reported to the user.

---

## [2026-07-26] batch ingest | Honey/Bone/Diabetes batch (15 papers from .raw/Honey/)
- Source folder: `.raw/Honey/` (15 new distinct papers; 1 file, `out.pdf`, was a truncated preview duplicate of the full thesis and was skipped; the Bobiş 2018 PDF was already ingested previously and skipped by hash match)
- Sources: [[Honey-PTP1B-Insulin-Signaling|Lori 2019]], [[Honey-vs-Glucose-Fructose-Solution|Münstedt 2008]], [[Honey-Metabolic-Effects-Type2-Diabetics-1988|Katsilambros 1988]], [[Honey-Jumping-Exercise-Bone-Gonadotropins|Mosavat 2014]], [[Honey-Exercise-Antioxidant-Bone-Metabolism|Tavafzadeh 2015]], [[Honey-Aerobic-Dance-Bone-Turnover|Ooi 2011]], [[Tualang-Honey-Bone-Metabolism-Postmenopausal-Review|Mohd Effendy 2012]], [[Honey-Bone-Health-Review-2019|Kamaruzzaman 2019]], [[Tualang-Honey-Bone-Structure-Ovariectomized-Rats|Zaid 2012]], [[Honey-Hydroxyapatite-Bone-Healing|Bigham-Sadegh 2018]], [[Biocement-Honey-Composites|Medvecky 2023]], [[Honey-Bone-Metabolism-Female-Athletes-Thesis|Ahmad 2017 thesis]], [[Honey-Nutrition-Health-Review-2008|Bogdanov 2008]], [[Raw-vs-Regular-Honey-Nigeria|Edo 2022]], [[Honey-Microbiome-Analysis|Xiong 2023]]
- Pages created: 15 source pages, 3 new concepts ([[Honey and Bone Metabolism]], [[Honey Composition and Bioactivity]], [[Honey Microbiome]]), 1 new entity ([[Tualang Honey]])
- Pages updated: [[Honey Hypoglycemic Mechanism]] (added PTP1B mechanism + 3 new source citations), [[Honey]] entity, [[Health and Nutrition]] domain, `domains/_index`, `sources/_index`, `entities/_index`, `concepts/_index`, `index`, `hot`, `.raw/.manifest.json`
- Key insight: this batch reveals the domain's single largest evidence cluster — 9 papers on honey and bone metabolism (mostly Tualang honey), largely from one Malaysian research group (Ooi/Tavafzadeh/Mosavat), consistently favorable for systemic supplementation but with one sharp contradiction: topical honey at a bone-defect site was the *worst*-performing treatment in [[Honey-Hydroxyapatite-Bone-Healing|Bigham-Sadegh et al. 2018]] — route of administration matters.

## [2026-07-26] ingest | Honey and Diabetes (Bobiş et al. 2018)
- Source: `.raw/Oxidative Medicine and Cellular Longevity - 2018 - Bobiş - Honey and Diabetes  The Importance of Natural Simple Sugars in.pdf`
- Summary: [[Honey-and-Diabetes|Honey and Diabetes]]
- Pages created: [[Honey-and-Diabetes|Honey and Diabetes]], [[Honey]], [[Honey Hypoglycemic Mechanism]], [[Honey in Diabetic Wound Healing]], [[domains/_index]], [[Health and Nutrition]]
- Pages updated: [[sources/_index]], [[entities/_index]], [[concepts/_index]], [[index]], [[hot]]
- Key insight: First health/nutrition domain in the vault. Honey has a lower GI than refined sugar (58 vs. 60) and shows preclinical/small-trial evidence for antidiabetic and wound-healing effects, but lacks large-scale RCT support.

---

## [2026-04-24] save | v1.6.0 public release notes (Teams, Karpathy-style)
- Type: release doc + visual assets
- Locations (new): `docs/releases/v1.6.0.md` (346 lines, 6 sections, Karpathy-style prose), `wiki/meta/dragonscale-mechanism-overview.svg` (4-mechanism diagram with shared .vault-meta/ gate), `wiki/meta/dragonscale-6-test-flow.svg` (validation timeline), `wiki/meta/dragonscale-frontier-graph.svg` (M4 candidate + 3 filed pages)
- Locations (modified): `wiki/meta/2026-04-24-v1.6.0-release-session.md` (cross-reference added pointing to public release notes)
- Scope: Teams approach. R1 (chair) wrote 3 original SVGs per SVG Diagram Style Guide. R2 (codex worker) drafted Karpathy-style release prose. R3 (chair) stitched SVGs, pivoted Wikipedia imagery to text links only (no binary vendoring per permission). R4 (codex verifier) returned ACCEPT WITH FIXES, 3 wording fixes on version narrative. R5 (chair) applied fixes, committed.
- Style: direct, short, signal-dense, lists over prose, no em dashes, no marketing terms. Verifier confirmed zero em-dashes and zero banned marketing language ('revolutionary', 'seamless', 'world-class', 'game-changing', 'unlock', 'transform').
- Distribution (all three destinations covered): (1) `docs/releases/v1.6.0.md` public-facing file (commit `85515bb`), (2) `wiki/meta/2026-04-24-v1.6.0-release-session.md` internal engineering record (cross-linked), (3) GitHub Release body (user to paste from docs/releases/v1.6.0.md when ready to `gh release create v1.6.0`).
- Wikipedia imagery: referenced as text link to `https://en.wikipedia.org/wiki/Dragon_curve` rather than hotlinked or vendored. Cleaner license-wise (no CC-BY-SA attribution needed) and no external dependency. The 3 original SVGs carry the visual load instead.
- PII scan post-write: `docs/releases/v1.6.0.md` + all three SVGs are clean. No `/home/` paths, no real emails, no tokens.
- Next recommended: user runs `gh release create v1.6.0 --notes-file docs/releases/v1.6.0.md` when ready to cut the public release. This also creates the annotated tag.

## [2026-04-24] save | DragonScale end-to-end validation pass (Teams, 6 tests)
- Type: validation + first real fold + first real autoresearch
- Tests executed (all green):
  - T0 ollama pull `nomic-embed-text`: done (274MB, 15s wall)
  - T1 M1 dry-run k=3 via codex: DRY-RUN OK, 8 children, no em-dashes
  - T2 M2 real allocate: counter advanced 2 to 3, got `c-000002` (unassigned reservation; gap acceptable per spec)
  - T3 M3 full tiling with model present: 41 pages scanned, 21 embedded, 20 correctly skipped (meta/excluded/embed-error), 0 errors at >=0.9, 15 pairs in 0.8-0.9 review band (top 0.8822 Compounding Knowledge vs LLM Wiki Pattern, a legitimate semantic neighbor), report at `wiki/meta/tiling-report-2026-04-24.md`
  - T4 M1 commit via codex: first real fold committed, `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md` (115 lines, 8 children, flat extractive). Flips the long-standing "no fold committed yet" status
  - T6 M4 autoresearch no-topic via codex: selected "How does the LLM Wiki pattern work?" as candidate (score 1.7022, #3 after skipping top-1 source + top-2 self-reference); 6 web fetches (Karpathy gist, RAG paper arXiv 2005.11401, MemGPT arXiv 2310.08560, Obsidian docs); 3 new concept pages filed, each with Primary Sources
- Locations (new): `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md`, `wiki/meta/tiling-report-2026-04-24.md`, `wiki/concepts/Persistent Wiki Artifact.md`, `wiki/concepts/Source-First Synthesis.md`, `wiki/concepts/Query-Time Retrieval.md`
- Locations (modified): `.vault-meta/address-counter.txt` (2 to 3), `wiki/index.md` (3 concept links), `wiki/concepts/_index.md` (3 concept links)
- Scope: six-test menu the user approved. Codex gpt-5.4 for T1/T4/T6 (sub-agent delegation); chair for T0/T2/T3 (one-shot shell) and all integration (index, log, hot, commit).
- Style: all new content uses colons or parens instead of em-dashes. Pre-existing em-dashes in index entries and wiki/concepts/_index.md left as-is (clean-room boundary; deferred to F-slice style pass).
- Tests still green: `make test` passes (74+ assertions).
- Integration: chair added the 3 new concepts to `wiki/index.md` and `wiki/concepts/_index.md` with colon-style descriptions so the fresh pages are discoverable. The cluster extends `[[How does the LLM Wiki pattern work?]]` and cross-references `[[LLM Wiki Pattern]]`.
- Next recommended slice: either (G) commit this test batch and declare v1.6.0 validated, or (H) run a second fold k=3 now that 8 newer entries exist above this one and close the hierarchical-fold-not-yet-supported loop in a future phase.

## [2026-04-24] save | v1.6.0 closeout (Teams, chair-led)
- Type: docs + release hygiene
- Locations (new): wiki/meta/2026-04-24-v1.6.0-release-session.md (release session summary, 346 lines), wiki/meta/boundary-frontier-2026-04-24.md (first M4 run artifact against this vault), docs/dragonscale-guide.md (user-facing DragonScale guide, 563 lines)
- Locations (modified): wiki/hot.md (tag-claim fix, Scripts line adds boundary-score, tests line adds test_boundary_score, push-line drift, tiling line-count, one em-dash), docs/install-guide.md (version 1.5.0 to 1.6.0, DragonScale callout expanded to all four mechanisms, "hierarchical log folds" corrected to "flat extractive log folds", points to docs/dragonscale-guide.md), README.md (DragonScale parenthetical expanded to all four mechanisms plus guide link)
- Scope: Teams approach, chair-led. Slice A (2 codex read-only explorers: closeout punch list + doc-surface map). Slice B (6 bounded writes: 4 chair, 2 codex workers, non-overlapping write scopes). Slice C (codex adversarial verifier, ACCEPT WITH FIXES). Slice D (fix pass + log entry + manual commit of docs + README).
- Verifier: C1 found 11 items across 6 files. All 11 applied. Flag typos `--allow-remote-ollama` and `--report PATH` corrected in release-session; boundary-frontier provenance corrected to `--top 7` to match default vs explicit top; hot.md tiling line-count claim stripped to avoid drift; hot.md "local tag only" corrected to "local commits only, no git tag"; install-guide log-fold wording corrected from "hierarchical" to "flat extractive"; dragonscale-guide rollback wording corrected (`.vault-meta/` is a shared gate across M2+M3+M4, not per-mechanism).
- Model: codex gpt-5.4 used throughout. User requested gpt-5.5; not reachable via codex CLI 0.123.0 / this account at the time. models_cache lists max gpt-5.4, and the API rejects gpt-5.5 with "does not exist or you do not have access". Existing config already has `service_tier = "fast"` and `sandbox_mode = "workspace-write"`, matching the "fast for chatgpt with permission of full access" intent.
- Tests: `make test` passes. test_allocate_address.sh (shell, 12 assertions), test_tiling_check.py (python, 18 assertions), test_boundary_score.py (python, 44 assertions). Zero ollama dependency.
- Tags: still no local v1.5.0 / v1.5.1 / v1.6.0 tags. User controls tag creation and push. Pre-existing tags unchanged (v1.1, v1.4.0 through v1.4.3).
- Deliberately NOT done: no real M1 fold committed; no M3 end-to-end run (needs `ollama pull nomic-embed-text`); pre-existing em-dashes in install-guide.md and README.md left untouched (clean-room boundary, not in write scope this slice); CLAUDE.md pre-existing uncommitted change left untouched.
- Next recommended slice: either (E) push to origin/main and create annotated tags v1.5.0, v1.5.1, v1.6.0 in landing order, or (F) dedicated style pass to scrub pre-existing em-dashes across install-guide.md, README.md, and any other wiki files flagged by a grep scan.

## [2026-04-24] save | DragonScale Phase 4 — boundary-first autoresearch shipped (v1.6.0)
- Type: feature release
- Locations (new): scripts/boundary-score.py (with --top, --page, --json, stdout-only CLI), tests/test_boundary_score.py (40+ assertions)
- Locations (modified): skills/autoresearch/SKILL.md (new Topic Selection section A/B/C with helper-failure fallback), commands/autoresearch.md (no-topic candidate flow with agenda-control label), wiki/concepts/DragonScale Memory.md (v0.4: M4 flipped from NOT IMPLEMENTED to shipped; exact formula without recency floor; filename-stem disclosure; fence-handling qualifiers), CHANGELOG.md, .claude-plugin/{plugin,marketplace}.json (1.5.0 -> 1.6.0), Makefile (test-boundary target), wiki/hot.md, wiki/index.md, wiki/concepts/_index.md (status drift resolved).
- Scope: boundary-first autoresearch as opt-in Topic Selection mode. `/autoresearch` without a topic surfaces top-5 frontier pages; user picks/overrides/declines. Explicit helper-failure fallback to user-ask. Labeled "agenda control" throughout to match the spec's scope disclosure.
- Correctness: filename-stem resolution including folder-qualified `[[notes/Foo]]` -> Foo.md. Self-loops, unresolved targets, meta-targets, symlinks, and vault escapes all excluded. Code-fence parser handles backticks AND tildes with CommonMark length tracking (longer opening fence is not closed by shorter inner fence). Indented blocks intentionally not filtered (Obsidian bullet convention).
- Recency: exp(-days/30), no floor. Stale pages approach zero weight so they do not dominate frontier ranking.
- Review rounds: codex adversarial Phase 4 round 1 (10 items: 7 reject + 3 refine). Round 2 (7 accept + 3 still-reject: folder-qualified stem, docstring floor mention, hot.md historical drift). Round 3 (3 accept, PASS).
- Phase 3.6 (pre-Phase-4 hardening) already landed as v1.5.1: tiling --report VAULT_ROOT confinement, rollout baseline, AGENTS.md consistency, wiki-ingest .raw/ contradiction, install-guide version.
- All four DragonScale mechanisms now shipped and opt-in. 44 commits ahead of origin/main, no push.

## [2026-04-24] save | DragonScale Phase 3.5 — cross-phase hardening to v1.5.0
- Type: release hardening
- Locations (new): bin/setup-dragonscale.sh (opt-in installer), tests/test_allocate_address.sh, tests/test_tiling_check.py, Makefile, CHANGELOG.md
- Locations (modified): hooks/hooks.json (+.vault-meta/ staging), agents/wiki-ingest.md (single-writer rule for addresses), agents/wiki-lint.md (Mechanism 2+3 checks), skills/wiki-ingest/SKILL.md (aligned non-DragonScale wording), wiki/concepts/DragonScale Memory.md (M2 severity matches lint, M4 marked NOT IMPLEMENTED, seed page gets address c-000001), .claude-plugin/{plugin.json,marketplace.json} (1.4.2/1.4.3 → 1.5.0), README.md (11 skills + DragonScale callout), wiki/hot.md (refreshed for v1.5.0), .raw/.manifest.json (address_map now has DragonScale Memory.md → c-000001), .gitignore (.vault-meta/.tiling.lock + cache), .vault-meta/address-counter.txt (advanced to 2).
- Scope: resolve the 10 hold-ship items from the cross-phase audit. Add reproducible test harness (make test passes). Version-bump plugin.json and marketplace.json to 1.5.0. Create CHANGELOG.md. Refresh hot cache.
- Review rounds: codex 3.5a (5/5 accept on doc/agent fixes), codex final holistic (10/10 accept on audit items + 2 surgical regression fixes: wiki-ingest/wiki-lint non-DragonScale wording alignment, README skill count).
- Tests: `make test` runs 12 shell assertions (allocator) + 18 python assertions (tiling-check). All pass; no ollama dependency.
- Phase 3.5 complete. Repo state: 6 developer commits added this pass (f2e73c1, 2b49a0c, 8b28e48, 19ad7e4, 365f557, 2e7dd16). Total 39 commits ahead of origin/main. No push.

## [2026-04-24] save | DragonScale Phase 3 — semantic tiling MVP
- Type: skill update + new script + threshold state
- Locations: scripts/tiling-check.py (485 lines), .vault-meta/tiling-thresholds.json (seed defaults), skills/wiki-lint/SKILL.md (109-line Semantic Tiling section + item #10 in checks), wiki/concepts/DragonScale Memory.md (Mechanism 3 cost framing clarified)
- Scope: opt-in embedding-based duplicate detection via ollama nomic-embed-text. Default bands error>=0.90, review>=0.80, explicitly documented as conservative seeds (not literature-backed interpolation). Calibration procedure documented, not automated.
- Security: default OLLAMA_URL locked to 127.0.0.1; non-localhost requires --allow-remote-ollama flag. Symlinks and vault-root escapes rejected before file reads (prevents data exfil).
- Correctness: cache keyed on sha256(model+body); orphan GC on save; model-drift auto-invalidation on load.
- Concurrency: flock(LOCK_EX) on .vault-meta/.tiling.lock; per-PID temp file for atomic writes.
- Scale: warn >500 pages; hard-fail exit 4 at >5000 pages.
- Exit codes: 0/2/3/4/10/11 distinctly surfaced in wiki-lint wiring (not collapsed into "unknown").
- Review rounds: 4 codex exec adversarial passes covering security, cache correctness, feature gate, inclusion logic, scale, threshold honesty, concurrency, exit codes, model drift, terminology coupling.
  Round 1: 10 items -> 7 reject + 3 refine.
  Round 2: 6 accept + 4 still-reject (symlink ordering, prose sync, exit-code wiring, terminology in checklist + "no API cost" claim).
  Round 3: 3 accept + 1 still-reject (cost-framing phrasing).
  Round 4: accept.
- Final verdict: 10/10 accept.
- Phase 3 complete. All three DragonScale mechanisms that were in-scope for the initial spec are now shipped as opt-in features. Mechanism 4 (boundary-first autoresearch) was flagged as agenda-control out-of-scope per the v0.2 scope boundary; may or may not ship as a future phase.

## [2026-04-23] save | DragonScale Phase 2 — deterministic page addresses MVP
- Type: skill update + new script
- Locations: scripts/allocate-address.sh, skills/wiki-ingest/SKILL.md (Address Assignment section), skills/wiki-lint/SKILL.md (Address Validation section), wiki/concepts/DragonScale Memory.md (Mechanism 2 rewritten v0.2→v0.3), .vault-meta/address-counter.txt, .raw/.manifest.json (new)
- Scope: MVP address format `c-NNNNNN` (creation-order counter, zero-padded 6 digits). Rollout baseline 2026-04-23. Legacy pages exempt until deliberate backfill (future `l-` prefix). No content hash, no fold-ancestry encoding in the MVP (both deferred).
- Concurrency: atomic allocation via flock-guarded Bash helper. Counter recovery from max observed `c-` address, never silent reset to 1.
- Lint: post-rollout pages without address are errors; legacy pages without address are informational. Optional `.vault-meta/legacy-pages.txt` manifest grandfathers pages with missing/wrong `created:` metadata.
- Re-ingest idempotency: `.raw/.manifest.json` `address_map` preserves path→address mapping across re-ingests and renames.
- Naming: mechanism renamed from "content-addressable paths" to "deterministic page addresses" (the MVP is a counter, not a content hash; the old name was overclaim).
- Review rounds: 2 codex exec adversarial passes. Round 1: 8 rejects covering counter mutation, race conditions, uniqueness atomicity, missing-file recovery, terminology drift, silent regression path, legacy classification, re-ingest idempotency. Round 2: 7 accept + 1 reject (manifest.json absent). Round 3 (item 8 only): accept after creating `.raw/.manifest.json`.
- Final verdict: 8/8 accept.
- Phase 2 complete. Phase 3 (semantic tiling lint) gated on human approval.

## [2026-04-23] save | DragonScale Phase 1 — wiki-fold skill shipped
- Type: skill
- Location: skills/wiki-fold/SKILL.md, skills/wiki-fold/references/fold-template.md
- Scope: flat extractive fold over raw wiki/log.md entries. Dry-run default via Bash stdout (no Write tool, avoids PostToolUse hook residue). Structural idempotency via deterministic fold_id. Duplicate-range detection. Fold-of-folds explicitly out of scope.
- Review rounds: 3 codex exec adversarial passes. Round 1: 1 refine + 6 reject across 7 items (allowed-tools, hook-mutation risk, idempotency claim, dry-run faithfulness, children structure, Mechanism 1 coverage, auto-commit conflict). Round 2: 6 accept + 1 reject (25/26 count inversion). Round 3 (item 4 only): accept.
- Final verdict: 7/7 accept.
- Dry-run artifact: /tmp/wiki-fold-dry-run-v2.md (not committed). fold_id: fold-k3-from-2026-04-10-to-2026-04-23-n8.
- Phase 1 complete. Phase 2 (content-addressable paths) gated on human approval.

## [2026-04-23] save | DragonScale Memory v0.2 — post-adversarial-review
- Type: concept revision
- Location: wiki/concepts/DragonScale Memory.md
- Review: codex exec adversarial review rejected all 7 load-bearing claims in v0.1
- Changes: weakened LSM analogy, removed strong prompt-cache claim, replaced 0.85 threshold with calibration procedure, justified 2^k as MVP convenience, acknowledged scope-boundary leak for boundary-first autoresearch, added Operational Policies section (retention/tombstones/versioning/conflict/concurrency/provenance/ACL), tagged claims as [sourced]/[derived]/[conjecture], narrowed tagging scope per re-review
- Re-review result: 7/7 accepted (after one surgical fix on tagging-scope language)
- Phase 0 complete. Phase 1 (wiki-fold skill) gated on human approval.

## [2026-04-23] save | DragonScale Memory — Phase 0 design doc (proposed)
- Type: concept
- Location: wiki/concepts/DragonScale Memory.md
- From: brainstorming session on applying Heighway dragon curve properties to LLM wiki memory architecture
- Scope: memory-layer only, NOT agent reasoning. Four mechanisms: (1) fold operator (LSM-style exponential compaction at 2^k log entries), (2) content-addressable page paths for prompt-cache stability, (3) semantic tiling lint (embedding-based dedup, 0.85 cosine threshold), (4) boundary-first autoresearch scoring
- Status: proposed. Phase 0 pending codex adversarial review. Phase 1+ (fold skill, address anchors, tiling lint, boundary score) gated on review pass.
- Primary sources verified: Dragon curve (Wikipedia, boundary dim 1.523627086), Regular paperfolding sequence (OEIS A014577), LSM trees (arXiv 2504.17178, LevelDB 10x level ratio), MemGPT (arXiv 2310.08560), Anthropic prompt caching docs (5min/1hr TTL, 20-block lookback)
- Links updated: wiki/concepts/_index.md, wiki/index.md

## [2026-04-15] save | Claude SEO v1.9.0 Slides and GitHub Release
- Type: session
- Location: wiki/meta/2026-04-15-slides-and-release-session.md
- From: built 15-slide HTML presentation deck (v190.html), fixed hardcoded path in release_report.py, pushed 68 files to GitHub, tagged v1.9.0, created GitHub release with PDF asset
- Key lessons: Path.home() not hardcoded paths, git pull --rebase before big pushes, Chrome blocks file:// cross-origin images, .claude/ always in .gitignore
- Release: https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.0

## [2026-04-15] save | Claude SEO v1.9.0 Release Report — PDF Complete
- Type: session
- Location: wiki/meta/2026-04-15-release-report-session.md
- From: full session completing the v1.9.0 PDF release report. Dark theme, 13 pages, 1.53 MB. Fixed logo (double-space filename), empty spaces, page-break orphans, file:// URL encoding.
- Key fixes: `urllib.parse.quote()` for file:// URIs; `display:table-cell` is atomic in WeasyPrint (no page-break); fixed `height:297mm` causes empty space; replaced orphan tables with paragraphs
- Challenge v2 added: keyword LEADS, $600 prize pool, deadline April 28
- Output: `~/Desktop/Claude-SEO-v1.9.0-Release-Report.pdf`

## [2026-04-14] save | Claude SEO v1.9.0 — Pro Hub Challenge Integration Session
- Type: session + 4 concept pages + 1 entity page
- Location: wiki/meta/2026-04-14-claude-seo-v190-session.md
- From: full v1.9.0 implementation session — reviewed 5 community submissions, integrated 4 new skills (seo-cluster, seo-sxo, seo-drift, seo-ecommerce), enhanced seo-hreflang, added DataForSEO cost guardrails
- Pages created: [[2026-04-14-claude-seo-v190-session]], [[Claude SEO]], [[Pro Hub Challenge]], [[Semantic Topic Clustering]], [[Search Experience Optimization]], [[SEO Drift Monitoring]]
- Review rounds: 4 (code review x3 + cybersecurity audit). Score: 87 → 93 → 97 → 85 security
- Key learnings: always verify subagent output (40-line count error caught), insertion-point bugs caught by max-effort plan review, pre-existing security debt identified (10 of 15 findings)

## [2026-04-14] save | SVG Diagram Style Guide
- Type: concept
- Location: wiki/concepts/SVG Diagram Style Guide.md
- From: extracted design tokens from 17 production SVGs in claude-ads/assets/diagrams/
- Covers: colors, typography, layout primitives, card patterns, arrow connectors, numbered circles, file naming

## [2026-04-14] save | Community CTA Footer Rollout
- Type: decision
- Location: wiki/meta/2026-04-14-community-cta-rollout.md
- From: session adding Skool community footer to 6 skill repos (claude-ads, claude-seo, claude-obsidian, claude-blog, banana-claude, claude-cybersecurity)
- Key insight: frequency calibration per tool type; single-point orchestrator instruction pattern

## [2026-04-10] save | Backlink Empire - Blog Posts, Karpathy Gist, GitHub Cross-Linking
- Type: session
- Location: wiki/meta/2026-04-10-backlink-empire-session.md
- From: full session covering blog creation (claude-obsidian + claude-canvas), Karpathy gist comment, 26 GitHub README updates with Author/community/backlink sections, homepage URLs on 10 repos, topics on 25 repos, rankenstein.pro backlinks on 5 SEO repos
- Blog posts: agricidaniel.com/blog/claude-obsidian-ai-second-brain, agricidaniel.com/blog/claude-canvas-ai-visual-production
- Impact: ~87 new backlinks from DA 96 github.com, 6 rankenstein.pro backlinks, 25 Skool community links

## [2026-04-08] save | claude-obsidian v1.4 Release Session
- Type: session
- Location: wiki/meta/claude-obsidian-v1.4-release-session.md
- From: full release cycle covering v1.1 (URL/vision/delta tracking, 3 new skills), v1.4.0 (audit response, multi-agent compat, Bases dashboard, em dash scrub, security history rewrite), and v1.4.1 (plugin install command hotfix)
- Key lessons: plugin install is 2-step (marketplace add then install), allowed-tools is not valid frontmatter, Bases uses filters/views/formulas not Dataview syntax, hook context does not survive compaction, git filter-repo needs 2 passes for full scrub

## [2026-04-08] ingest | Claude + Obsidian Ecosystem Research
- Type: research ingest
- Source: `.raw/claude-obsidian-ecosystem-research.md`
- Queries: 6 parallel web searches + 12 repo deep-reads
- Pages created: [[claude-obsidian-ecosystem]], [[cherry-picks]], [[claude-obsidian-ecosystem-research]], [[Ar9av-obsidian-wiki]], [[Nexus-claudesidian-mcp]], [[ballred-obsidian-claude-pkm]], [[rvk7895-llm-knowledge-bases]], [[kepano-obsidian-skills]], [[Claudian-YishenTu]]
- Key finding: 16+ active Claude+Obsidian projects; 13 cherry-pick features identified for v1.3.0+
- Top gap confirmed: no delta tracking, no URL ingestion, no auto-commit

## [2026-04-07] session | Full Audit, System Setup & Plugin Installation
- Type: session
- Location: wiki/meta/full-audit-and-system-setup-session.md
- From: 12-area repo audit, 3 fixes, plugin installed to local system, folder renamed

## [2026-04-07] session | claude-obsidian v1.2.0 Release Session
- Type: session
- Location: wiki/meta/claude-obsidian-v1.2.0-release-session.md
- From: full build session — v1.2.0 plan execution, cosmic-brain→claude-obsidian rename, legal/security audit, branded GIFs, PDF install guide, dual GitHub repos


- Source: `.raw/` (first ingest)
- Pages updated: [[index]], [[log]], [[hot]], [[overview]]
- Key insight: The wiki pattern turns ephemeral AI chat into compounding knowledge — one user dropped token usage by 95%.

## [2026-04-07] setup | Vault initialized

- Plugin: claude-obsidian v1.1.0
- Structure: seed files + first ingest complete
- Skills: wiki, wiki-ingest, wiki-query, wiki-lint, save, autoresearch

## 2026-09-11 — Knowledge engine build-out

Executed the eight-workstream build plan. What changed:

**Spine.** Six new folders (`pathways/ quotes/ figures/ claims/ creators/ decks/`) plus
`_templates/` with 7 page templates. Introduced the **evidence tier** field (A/B/C/D/X) across
all claim-bearing page types; tier X marks creator assertions so they can never be mistaken for
findings.

**Pipeline A — study backlog.** Fingerprinted all 417 PDFs in `.raw/Studies/` and all 52 in the
Duplicates bucket. 51 were byte-identical to files already held; **1 was misfiled and genuinely
novel** (`elibrary_64279958_98765084.pdf`), now moved into `Studies/`. Duplicates folder renamed
`Duplicates-VERIFIED-safe-to-delete/` — not deleted, that call is the user's.

**Pipeline B — competitor slideshows.** `scripts/build-creator-claims.py` turns the 2,353 OCR'd
slides into **15 topic pages** in `creators/`, covering 234 posts and 5.9M views. Added a
legibility gate so OCR noise from figure-screenshot slides no longer reads as evidence.

**Pipeline C — video transcription.** Set up `.venv-research` (uv) with faster-whisper.
`scripts/transcribe-videos.py` is resumable and writes `video-text.jsonl` mirroring the slide
corpus shape. Measured 8.1x realtime; full 1,445-video run ≈ 0.6h. Running.

**Workstream 6 — figures.** `scripts/extract-figures.py` pulls figures from every study PDF,
filters logos/rules by size and aspect, classifies by printed caption into 9 display types, and
writes a stub per figure. `scripts/triage-figures.py` then keeps only captioned+classified
figures at top level and moves the rest to `_unreviewed/`, with a per-paper index — this was
needed because raw extraction produced ~2,700 stubs against a 483-page vault.

**Synthesis exemplars.** [[GH-IGF-1 Axis]] (pathway pattern), [[Growth Factors of the Growth Plate]] (enumerated review, 8 members, tiers per entry), 6 claim pages, 3 quote files, 6 hand-
written figure specs.

**Content loop.** 6 deck pages in `decks/` with full slide ledgers linking each slide to its
claim, quote file and figure — closing the vault→deck→vault loop.

**Accounts.** [[Account Briefs]]: 4 accounts split by audience with corpus evidence, assigned
styles, ready decks and a 3-week warm-up.

Not done: Pipeline D (acquiring new studies) awaits the transcription output, which will name
the compounds and pathways worth chasing.
