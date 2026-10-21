# Claims — androgens-igf1-ranking

## What this file is, and what it is not

No deck CSV exists for this topic yet, so there are no `## slide N` blocks for
`scripts/verify-claims.py` to score. When the CSV is written, each numbered slide
gets its own `## slide N` block with `CLAIM:` / `QUOTE:` / `SOURCE:`, drawn from
the sections below.

**Provenance warning, and it is the important part.** This topic was built from
three **Sci-Bot (sci-hub AI) answer pages**, dated 21 Oct 2026:

```
~/Downloads/Sci hub ai/Nandrolone.pdf   androgens -> IGF-1 axis, 64 refs
~/Downloads/Sci hub ai/HGH.pdf          GH concentration/dose vs proliferation
~/Downloads/Sci hub ai/EGFR.pdf         EGF/EGFR at the growth plate
```

These are **secondary AI synthesis**, not papers. They were audited: the
references are real, the DOIs resolve, the mechanistic spine is correct, and no
fabricated data was found. But the numbers below carry the Gebhardt failure mode
exactly — paper → summary → deck, with direction and magnitude lost in the middle.
Every figure marked UNVERIFIED must be pulled from the primary before it reaches a
slide.

**Verification status, 21 Oct 2026.** Seven claims — B1, B2, B3, B5, B6, and both
legs of B7 — are verified (PMIDs 17363459, 16368782, 18676717, 26440329, 11788382,
8501143, 9329378, plus Urban 1995 / PMID 7491931 read from the rendered PDF). Two
were taken past the abstract into the full text: **Lewis 2002** and **Urban 1995**.

Verifying eight papers caught **seven errors that had come through the synthesis**
and **narrowed one rule I had written myself**, which is the argument for doing the
rest:

| What the synthesis said | What the paper says |
|---|---|
| DHT raised IGF-1 "7-fold mRNA, 8-fold protein" | **7-fold covers both**; no 8-fold exists |
| "DHT increased IGF-1 mRNA more than testosterone" | "DHT and T **each**" — they are **equal** |
| Flutamide **and Casodex** abolished it | Flutamide only |
| Nandrolone IGF-1 localised to IIx/b fibres "+29%" | CSA is **+20% IIa / +30% IIx/b**; the localisation result carries **no percentage** |
| E2 implants "+58–78% at day 7; +65–71% at day 28" | 58% is **day 7**, 78% is **day 28**, both E2 alone; 65% is day 28 for TBA/E2. No 71% exists. |
| Inhibitors "abolish" TBA-stimulated proliferation | "**suppressed**" |
| JB1 and flutamide part of the Thornton inhibitor set | Different papers; Thornton used GDPβS, MMPI, CRM197, AG1024, AG1478, AG879 |
| Weissberger & Ho dated 1994 | **1993**, *JCEM* 76:1407–12 |

Two details I had carried are **absent from the abstracts** and remain unverified
rather than Tier 1: additive ARE activity, and abolition by a DNA-binding-deficient
AR (Wu 2007).

A third — **"serum IGF-1 unchanged"** (Lewis 2002), the claim the entire
"nandrolone acts purely locally" reading depends on — was chased into the **full
text and settled**: serum 287.6 ± 106.1 vs 297.5 ± 86.0 ng/ml, n = 7 per group.
Real null, underpowered. B6 is the only claim here verified past the abstract, and
reading it turned up three things the abstract does not contain (a human
corroboration, an IGF-1 negative-feedback result, and a testosterone-assay caveat).
That is the case for doing this to the rest.

One claim moved the other way. **Le 2006 cannot support "androgens up-regulate
IGF-1R"**: it reports IGF-1R explicitly unchanged by all four steroids.

**And one correction to my own synthesis, not to Sci-Bot's.** I had written the
blood-arm rule as "testosterone raised IGF-1 in hypogonadal men, it did not in
elderly men, so baseline governs the size". Verifying B7 says that is the wrong
split. Urban's elderly men **doubled their estradiol** (17 → 36 pg/ml, significant)
and serum IGF-1 still rose only a non-significant +16% — the same modest effect
Weissberger detected at +22%. The rule survives but shrinks: the human serum IGF-1
response to testosterone is **~15–25%**, the robust androgen effect is on **GH
pulse amplitude**, and **no one in this set has measured a non-aromatizable
androgen lowering serum IGF-1 in men**. The bottom of the blood-arm ranking is
mechanism, not measurement, and the brief now says so.

Also narrowed: Veldhuis 1997 measures **ApEn** — the orderliness of GH secretion —
not IGF-1 levels. I had cited it as "DHT failed to reproduce testosterone's GH
effect", which is too loose for a slide.

B4, B8 and the human leg of B9 are still unverified, as is all of section D. No
deck is cleared to post.

---

# A. Verified quotes already in this repo

These two are the only claims in this topic with a verbatim quote behind them, and
both were verified for other decks.

## Mauras et al. 2000, JCEM — the ceiling of the GH dose evidence
Verified in `content/hgh-02-dose/07-claims.md`.
`.raw/Studies/Growth-Hormone-IGF1-Axis/High Dose Recombinant Human Growth Hormone Treatment of GH-Deficient - Mauras et al - 2000.pdf`

CLAIM: 0.1 mg/kg/day is the highest GH dose with randomised adult-height evidence,
and it buys about 4.6 cm over standard replacement.
QUOTE: "All patients were randomly assigned to continued treatment with GH ... at
  either 0.3 mg/kg·week (standard dose) or 0.7 mg/kg·week (high dose), sc, daily."
QUOTE: "subjects in the high dose group were significantly taller at near-adult
  height than subjects in the standard dose group by an average of 4.6 cm
  (n = 75; P < 0.001; 95% confidence interval, 2.6–6.5 cm)."
QUOTE: "An interesting and important finding of these studies is the normal pace of
  bone maturation, with bone ages advancing approximately 1 yr/chronological yr in
  both the standard and high dose groups."
QUOTE: "a greater increase in fasting insulin (P = 0.011) and C peptide (P = 0.019)
  in the high dose"
SOURCE: Mauras et al. 2000, JCEM
→ 0.7 mg/kg/week = **0.1 mg/kg/day**, which is above every approved paediatric
  label (GHD ~0.025–0.035; Turner/SGA/ISS top out near 0.067 mg/kg/day). Trial
  regimen, GH-deficient adolescents, open plates, IGF-1 monitored. Not a protocol.

## Ly et al. 2020, Front Endocrinol — the real ceiling is IGF-1, not mg/kg
Verified in `content/hgh-09-igf1-ceiling/07-claims.md`.

CLAIM: the dose limit is an IGF-1 SDS limit, and dose predicts IGF-1 badly between
individuals.
QUOTE: "It is recommended that levels of IGF-1 should not exceed 2 SDS due to
  concerns about increasing the potential risk of adverse events (5)."
QUOTE: "The IGF-1 >=2 SDS samples had a higher median (range) GH dose, 0.042
  (0.02-0.10) mg/kg/day, compared with the IGF-1 <2 SDS samples, 0.038 (0.01-0.10)
  mg/kg/day, p<0.001."
SOURCE: Ly et al. 2020, Front Endocrinol
→ The ranges overlap almost entirely. "The highest dose that is best" is not a
  number that can be handed to anyone; it is whatever puts that person's IGF-1 just
  under the ceiling.

---

# B. Androgen -> IGF-1: the ranking claims

Ordered by how load-bearing they are. B1, B2, B3, B5 and B6 are verified with
verbatim quotes. For the rest: the exact figure to pull, and the DOI to pull it
from.

## B1. The androgen response elements — the keystone
**VERIFIED** against the PubMed record, 21 Oct 2026. PMID 17363459.

CLAIM: two AREs between −1320 and −1420 bases of the human IGF-1 upstream promoter,
activated 5-fold more by AR than by the glucocorticoid receptor.
QUOTE (abstract, verbatim): "Testosterone increased IGF-I mRNA levels in HepG2 and
  LNCaP cells and stimulated the activity of reporter genes controlled by 1.6 kb of
  the upstream promoter of the human IGF-I gene."
QUOTE (abstract, verbatim): "An androgen-responsive region that was located between
  -1320 and -1420 bases upstream of the first codon was identified by truncation
  studies. The androgen-responsive region was found to contain two sequences
  resembling known androgen receptor (AR)-binding sites from the Pem1 gene."
QUOTE (abstract, verbatim): "Each of the androgen-responsive elements (AREs) bound
  recombinant AR-DNA-binding domain in gel-shift experiments; binding was greatly
  enhanced by sequences flanking the apparent AR-binding half-sites. Testosterone
  induced recruitment of AR to sequences of genomic DNA containing these AREs. The
  two AREs were activated 5-fold more by AR than glucocorticoid receptor."
QUOTE (abstract, verbatim): "Collectively, these findings indicate the presence of
  two AREs within the IGF-I upstream promoter that act in cis to activate IGF-I
  expression."
SOURCE: Wu Y, Zhao W, Zhao J, Pan J, Wu Q, Zhang Y, Bauman WA, Cardozo CP.
  "Identification of androgen response elements in the insulin-like growth factor I
  upstream promoter." *Endocrinology* 2007;148(6):2984–2993.
  DOI: 10.1210/en.2006-1653

→ **Keep the cell lines attached to the number.** This is HepG2 (hepatoma) and
  LNCaP (prostate carcinoma), not muscle and not cartilage. The abstract's own
  framing of muscle is background, not result: "Testosterone stimulates the
  expression of IGF-I in cells and tissues that include prostate, muscle and muscle
  satellite cells, and the uterus."
→ **Two details I previously carried are still UNVERIFIED**, because the abstract
  does not state them and they came from the Sci-Bot synthesis: that the two AREs
  act **additively**, and that a **DNA-binding-deficient AR abolishes** the
  response. Both are plausibly in the full text. Do not put either on a slide until
  the full text is read.

## B2. DHT induction magnitude — top of the induction list
**VERIFIED** against the PubMed record, 21 Oct 2026. PMID 16368782.

CLAIM: DHT and testosterone each raised IGF-1 7-fold and cut IGFBP-3 2-fold, in
mRNA and secreted protein, in human prostatic stromal cells; AR-mediated.
QUOTE (abstract, verbatim): "DHT and T each increased IGF-I (7-fold) and decreased
  IGFBP-3 (2-fold) mRNA expression and protein secretion in a dose- and
  time-dependent manner and increased IGFBP-2 (2-fold) mRNA in a dose- and
  time-dependent manner. DHEA and E2 did not significantly alter these measures."
QUOTE (abstract, verbatim): "Flutamide abolished the DHT-modulated increases in
  IGF-I and IGFBP-2, suggesting that the influences of DHT and T on these measures
  were androgen receptor mediated."
QUOTE (abstract, verbatim): "None of the four steroids significantly affected
  IGF-IR, IGF-II, or IGFBP-5 mRNA levels or stromal cell proliferation."
QUOTE (abstract, verbatim): "The effects of DHT on IGF-I, IGFBP-2, and IGFBP-3 were
  more pronounced in stromal cultures that did not express desmin."
SOURCE: Le H, Arnold JT, McFann KK, Blackman MR. "DHT and testosterone, but not
  DHEA or E2, differentially modulate IGF-I, IGFBP-2, and IGFBP-3 in human
  prostatic stromal cells." *Am J Physiol Endocrinol Metab* 2006;290(5):E952–E960.
  DOI: 10.1152/ajpendo.00451.2005

→ **Three corrections to what I had written.**
  1. There is **no 8-fold**. The 7-fold covers mRNA *and* protein secretion. The
     synthesis's "~7-fold mRNA and ~8-fold protein" split does not exist here.
  2. **DHT is not above testosterone in this paper.** The abstract says "DHT and T
     **each**". The synthesis's "DHT increased IGF-1 mRNA more than testosterone"
     is not supported; if it is anywhere, it is a full-text subgroup detail. The
     induction ranking must read **DHT = testosterone**, not DHT > T.
  3. **Casodex is not in the abstract** — flutamide only.
→ **IGF-1R was explicitly unchanged**, by all four steroids. So this paper cannot
  be used for "androgens up-regulate IGF-1R"; that claim came from the Adzavon 2024
  review (DOI 10.1038/s41585-024-00942-3), a different and still-unverified source.
→ **No proliferation effect**, in a paper about prostate cancer risk. Worth keeping:
  the IGF axis moved 7-fold and the cells did not divide faster. That is the
  induction/outcome gap in miniature.
→ Tissue stays attached: primary cultures of **human prostatic stromal cells**. Not
  muscle, not cartilage.

## B3. Trenbolone does nothing to muscle IGF-1 in vivo — the dissociation
**VERIFIED** against the PubMed record, 21 Oct 2026. PMID 18676717.

CLAIM: trenbolone acetate alone did not raise longissimus IGF-1 mRNA, while
estradiol alone and TBA/E2 both did, and the authors attribute the combined
implant's effect to the estradiol.
QUOTE (abstract, verbatim): "In contrast, the TBA implant did not increase
  (P = 0.99) LM IGF-I mRNA levels after 28 d of implantation."
QUOTE (abstract, verbatim): "On d 7 and 28, IGF-I mRNA levels were greater (58 and
  78%, respectively; P < 0.009) in E2-implanted animals than in control steers.
  Similarly, on d 28 the LM IGF-I mRNA level was 65% greater (P = 0.017) in
  TBA/E2-implanted steers than in control animals."
QUOTE (abstract, verbatim): "Muscle IGFR-1, AR, and ER-alpha mRNA levels were not
  different (P > 0.47) in any of the treated groups compared with the control
  group."
QUOTE (abstract, verbatim): "These data suggest that E2 is responsible for the
  increased muscle IGF-I mRNA level observed in steers implanted with a combined
  TBA/E2 implant."
SOURCE: Pampusch MS, White ME, Hathaway MR, Baxa TJ, Chung KY, Parr SL,
  Johnson BJ, Weber WJ, Dayton WR. "Effects of implants of trenbolone acetate,
  estradiol, or both, on muscle insulin-like growth factor-I, insulin-like growth
  factor-I receptor, estrogen receptor-α, and androgen receptor messenger
  ribonucleic acid levels in feedlot steers." *J Anim Sci* 2008;86(12):3418–3423.
  DOI: 10.2527/jas.2008-1085

→ **The synthesis garbled these numbers and I passed the garble through.** It gave
  "+58–78% at day 7; +65–71% at day 28". The real structure: **58% is day 7 and 78%
  is day 28, both for E2 alone**; 65% is day 28 for TBA/E2. There is no 71%
  anywhere. Corrected here; the earlier version of this file was wrong.
→ Doses, which stay attached: TBA 120 mg, E2 25.7 mg in the E2-alone implant,
  TBA 120 mg / E2 24 mg in the combined implant. Twenty yearling crossbred steers,
  average initial BW 421.1 ± 3.6 kg, biopsies at d 0, 7, 14, 28.
→ This is the single cleanest result in the topic: same animals, same assay, three
  implants, and only the estradiol-containing ones move IGF-1.

## B4. Trenbolone in culture, and the "100-fold" error to not repeat
CLAIM: TBA at 1 and 10 nM raised IGF-1 mRNA to 1.7× control; E2 gave 3.5× at the
same 1–10 nM.
STATUS: **UNVERIFIED**, and the synthesis drew a bad inference from it — it called
this "E2 is roughly 100-fold more potent than trenbolone". At equal concentration,
3.5× vs 1.7× is a ~2× magnitude difference, not a 100-fold potency difference. **Do
not put "100-fold" on a slide.** If a potency gap is wanted, it needs a real
EC50 comparison.
SOURCE: Kamanga-Sollo E, Pampusch MS, Xi G, White ME, Hathaway MR, Dayton WR.
  *J Cell Physiol* 2004;201(2):181–189. DOI: 10.1002/jcp.20000

## B5. Trenbolone's IGF-1R dependence — top of the dependence list
**VERIFIED** against the PubMed record, 21 Oct 2026. PMID 26440329.

CLAIM: TBA-stimulated bovine satellite cell proliferation runs GPCR → MMP2/MMP9 →
hbEGF → EGFR/erbB2 → IGF-1R, and blocking any step suppresses it.
QUOTE (abstract, verbatim): "our results indicate that TBA may also initiate a
  quicker, nongenomic response that involves activation of G protein-coupled
  receptors (GPCR) resulting in activation of matrix metalloproteinases 2 and 9
  (MMP2 and MMP9) that release membrane-bound heparin-binding epidermal growth
  factor-like growth factor (hbEGF), which then binds to and activates the
  epidermal growth factor receptor (EGFR) and/or erbB2."
QUOTE (abstract, verbatim): "Furthermore, the EGFR has been shown to regulate
  expression of the IGF-1 receptor (IGF-1R), which is well known for its role in
  modulating muscle growth."
QUOTE (abstract, verbatim): "As expected, BSC cultures treated with 10 n TBA showed
  ( < 0.05) increased proliferation rate when compared with control cultures.
  Additionally, treatment with 5 ng hbEGF/mL stimulated proliferation in BSC
  cultures ( < 0.05). Treatment with GDPβS, MMPI, CRM197, AG1024, AG1478, and/or
  AG879 all suppressed ( < 0.05) TBA-induced increases in proliferation."
SOURCE: Thornton KJ, Kamange-Sollo E, White ME, Dayton WR. "Role of G
  protein-coupled receptors (GPCR), matrix metalloproteinases 2 and 9 (MMP2 and
  MMP9), heparin-binding epidermal growth factor-like growth factor (hbEGF),
  epidermal growth factor receptor (EGFR), erbB2, and insulin-like growth factor 1
  receptor (IGF-1R) in trenbolone acetate-stimulated bovine satellite cell
  proliferation." *J Anim Sci* 2015;93(9):4291–4301. DOI: 10.2527/jas.2015-9191

→ **The verb is "suppressed", not "abolished".** The synthesis said each inhibitor
  "abolishes" the effect; the paper says each "suppressed" it. Use "suppressed" or
  "blocked" on any slide. The difference matters — abolition would mean the pathway
  is the whole mechanism, suppression does not.
→ The abstract's P-values render as "( < 0.05)" because the PubMed plain-text
  record drops the italic *P*. All are P < 0.05. Note also that the abstract itself
  writes "10 n TBA" for 10 nM and "CRM19" once before "CRM197" — PubMed rendering
  artefacts, not errors in the paper.
→ **Attribution fix:** JB1 and flutamide are **not** from this paper. They come
  from the Kamanga-Sollo protein-synthesis and receptor-role papers
  (DOI: 10.1016/j.domaniend.2010.08.007 and 10.1016/j.domaniend.2008.02.003), both
  still unverified. This paper's inhibitor list is exactly GDPβS, MMPI, CRM197,
  AG1024, AG1478, AG879.
→ Endpoint is **proliferation only** (³H-thymidine), in culture, ≥9 replicates from
  ≥3 animals, in cells from steers with no prior androgen or estrogen exposure. It
  is not protein synthesis and not an in vivo result.

## B6. Nandrolone's local effect and the IGFBP switch
**VERIFIED AGAINST THE FULL TEXT**, 21 Oct 2026. PMID 11788382. Free to read at
`journals.physiology.org/doi/full/10.1152/ajpendo.00191.2001` (APS, free after 12
months). The serum question below is now settled.

CLAIM: 17-day nandrolone infusion raised diaphragm IGF-1 50%, IGFBP-3 69%, and cut
IGFBP-4 40%, alongside type II fibre hypertrophy, with serum IGF-1 unchanged.
QUOTE (abstract, verbatim): "NAN (6.6 mg. kg(-1) x day(-1)) was infused
  continuously for 17 days using a subcutaneous Silastic implant, whereas controls
  (CTL) received blank capsules."
QUOTE (abstract, verbatim): "NAN increased the CSA of type IIa (20%) and type IIx/b
  (30%) diaphragm fibers. Levels of IGF-I in the diaphragm muscle were
  significantly higher (50%) in NAN-treated animals. Immunohistochemistry revealed
  increased localization of IGF-I within type IIx/b diaphragm fibers. In addition,
  NAN increased IGFBP-3 within the diaphragm (69%), whereas IGFBP-4 decreased
  (40%)."
QUOTE (abstract, verbatim): "We conclude that NAN-induced diaphragm muscle fiber
  hypertrophy is mediated, in part, by influences of the IGF system within the
  muscle, such that coordinated changes in IGFBPs reflect a direction of change
  that has been associated with an anabolic response in other test systems."
SOURCE: Lewis MI, Horvitz GD, Clemmons DR, Fournier M. "Role of IGF-I and
  IGF-binding proteins within diaphragm muscle in modulating the effects of
  nandrolone." *Am J Physiol Endocrinol Metab* 2002;282(2):E483–E490.
  DOI: 10.1152/ajpendo.00191.2001

### The serum result, from the full text — SETTLED
QUOTE (Results, "Serum IGF-I", verbatim): "No differences were observed between the
  groups with regard to serum IGF-I levels (CTL: 287.6 ± 106.1; NAN: 297.5 ±
  86.0 ng/ml)."
QUOTE (Discussion, verbatim): "In the present study, serum IGF-I levels were not
  elevated with the use of the anabolic steroid as reported in some studies
  (15, 26)."
QUOTE (Results, verbatim): "The levels of IGF-I within the diaphragm muscle were
  significantly elevated in the NAN animals compared with CTL (50%; P < 0.05)"
QUOTE (Results, verbatim): "the mean IGFBP-3 level was significantly higher (69% by
  scanning densitometry; P < 0.01) ... whereas the mean IGFBP-4 level was
  significantly lower (40% by scanning densitometry; P < 0.01)"
QUOTE (Methods, verbatim): "Fourteen adult female Sprague-Dawley rats with initial
  body weights of ∼282 g were studied and divided into two groups, control
  (CTL; n = 7) and nandrolone (NAN) treated (n = 7)."

→ **The dissociation is real and now quotable**: muscle IGF-1 +50% while serum sat
  at 287.6 vs 297.5 ng/ml. Nandrolone's effect here is local.
→ **But say it as a null, not as an equivalence.** n = 7 per group and the SDs are
  enormous — ±106 on a mean of 288, i.e. ~37% of the mean. This study could not
  have detected a modest serum rise. "Serum IGF-1 did not change" is supportable;
  "nandrolone does not raise serum IGF-1" is more than the data carry.
→ **The +29% I carried does not exist.** CSA is **+20% type IIa, +30% type IIx/b**,
  and the IGF-I localisation result carries **no percentage at all**. The synthesis
  welded a fibre-size number onto an immunostaining result.
→ The authors' own reading of the IGFBP switch, which is the line to use:
  QUOTE (Discussion, verbatim): "IGFBP-4 is the only binding protein thought to
    function only as an inhibitor of IGF-I"
  QUOTE (Discussion, verbatim): "the increments of muscle IGFBP-3 and decrements in
    IGFBP-4 noted in the present report may be interpreted as a series of
    coordinated changes in the muscles to liberate more free IGF-I to bind its
    receptors."
→ Dose and model stay attached: **6.6 mg/kg/day continuous infusion, 17 days,
  n = 7 per group, adult female Sprague-Dawley rats, diaphragm.** Continuous
  subcutaneous Silastic implant, not injection.
→ Note this paper **does** show fibre hypertrophy (+20/+30% CSA), which is the
  opposite of the Gayan-Ramirez result below, where IGF-1 mRNA rose with no
  hypertrophy. Different dose, route and muscle. Both go in if either does.

### Two findings from the full text that are new to this topic
1. **A human corroboration of the local/systemic split**, in the authors' own
   words:
   QUOTE (Discussion, verbatim): "Similarly, in the clinical study by Urban et al.,
     serum IGF-I levels were also not elevated in the men receiving testosterone
     despite augmented IGF-I mRNA in the vastus lateralis muscle of these
     subjects."
   → This cuts both ways and must be carried honestly. It supports "serum is a poor
     surrogate for the intramuscular axis" **and** it complicates B7: testosterone
     did not raise serum IGF-1 in Urban's elderly men, while it did in Weissberger
     & Ho's hypogonadal men. The aromatization rule governs *whether* the GH axis
     can be activated; baseline androgen status plainly governs *how much*. Do not
     state the blood-arm ranking without that qualifier.
2. **Systemic IGF-1 suppresses local muscle IGF-1.**
   QUOTE (Discussion, verbatim): "we have recently reported that long-term systemic
     infusion of IGF-I downregulates IGF-I protein expression in the diaphragm
     muscle, possibly due to a negative feedback effect (19, 34)."
   → Negative feedback from the endocrine pool onto the autocrine pool. Pairs with
     the Sculthorpe finding that exogenous IGF-1 suppresses IGF-1 mRNA in human
     muscle cells. Relevant well beyond this topic.

### One methodological caveat worth knowing about this model
QUOTE (Discussion, verbatim): "Although one might expect very low endogenous
  testosterone values due to suppression by NAN, the higher levels are accounted
  for by an extremely large degree of cross-reactivity of NAN for the testosterone
  RIA antiserum."
→ The "serum testosterone" readout in this paper is substantially measuring
  nandrolone. Do not quote testosterone levels from it.
SUPPORTING, also unverified: Gayan-Ramirez G et al. "Nandrolone Decanoate Does Not
  Enhance Training Effects but Increases IGF-I mRNA in Rat Diaphragm." *J Appl
  Physiol* 2000;88(1):26–34. DOI: 10.1152/jappl.2000.88.1.26 — dose-dependent
  IGF-1 mRNA +73% high-dose males, +58%/+96% low/high females, **with no fibre
  hypertrophy**; the authors called the mRNA rise and the morphology dissociated.
  That dissociation is a caveat the deck must carry, not drop.
COUNTERPOINT, keep it in: Zhao J et al. *Muscle Nerve* 2007;37(1):42–49
  (DOI: 10.1002/mus.20888) — in chronically denervated gastrocnemius, nandrolone
  changed neither IGF-1, IGF-1R nor IGFBP-2/-3/-4/-5 at any time point. Context
  decides direction; "nandrolone raises muscle IGF-1" is false in denervated muscle.

## B7. The aromatization rule, human end
**VERIFIED**, 21 Oct 2026. PMIDs 8501143 (Weissberger & Ho), 9329378 (Veldhuis),
7491931 + rendered PDF Table 1 (Urban).

This was the loose end after B6, and chasing it **narrowed the rule rather than
confirming it as stated**. Read the three together before writing the blood arm.

### B7a. Weissberger & Ho 1993 — the positive result
CLAIM: testosterone activates the GH axis and raises IGF-1 in hypogonadal men, and
an antiestrogen reverses it.
QUOTE (abstract, verbatim): "Compared to the normal men, the hypogonadal men had
  significantly reduced mean GH pulse amplitude (3.1 +/- 0.6 vs. 8.4 +/-
  1.7 micrograms/L, P < 0.05), but not pulse frequency."
QUOTE (abstract, verbatim): "Testosterone treatment resulted in a significant
  increase in 24-h mean serum GH (0.7 +/- 0.2 to 1.4 +/- 0.2 micrograms/L,
  P < 0.05), mean GH pulse amplitude (3.1 +/- 0.6 to 5.2 +/- 0.8 micrograms/L,
  P < 0.01) and serum IGF-I (0.9 +/- 0.1 to 1.1 +/- 0.1 U/mL, P < 0.05)."
QUOTE (abstract, verbatim): "In the normal men, tamoxifen significantly reduced
  24-h mean serum GH (1.1 +/- 0.3 to 0.5 +/- 0.1 micrograms/L, P < 0.05), mean GH
  pulse amplitude (8.4 +/- 1.7 to 4.7 +/- 0.4 micrograms/L, P < 0.05), and serum
  IGF-I (1.0 +/- 0.1 to 0.7 +/- 0.1 U/mL, P < 0.001)."
QUOTE (abstract, verbatim): "We conclude that testosterone plays an important role
  in the modulation of the male somatotropic axis in adulthood, as appears to be
  the case in puberty, and that this effect is partly dependent on the
  aromatization of testosterone to estradiol."
SOURCE: Weissberger AJ, Ho KK. *JCEM* 1993;76(6):1407–12.
  DOI: 10.1210/jcem.76.6.8501143
→ n = 5 hypogonadal men (aged 20–32) and 6 normal men (21–27). Testosterone
  enanthate 250 mg im monthly; tamoxifen 20 mg/day for 3 weeks.
→ **"Partly dependent"** is the authors' own hedge. Keep the word.
→ Note tamoxifen is an **antiestrogen (SERM)**, not an aromatase inhibitor. It
  blocks the receptor, not the conversion. The inference is that the effect is
  **ER-mediated**; the aromatization step itself is inferred, not blocked.
→ The IGF-1 effect size is **modest**: 0.9 → 1.1 U/mL, about +22%. The large,
  robust effect is on **GH pulse amplitude**, not on IGF-1.

### B7b. Veldhuis 1997 — the DHT comparison, and what it is actually about
CLAIM: a non-aromatizable androgen fails to reproduce testosterone's effect.
QUOTE (abstract, verbatim): "Third, in 5 boys with constitutionally delayed
  puberty, im testosterone administration also significantly increased ApEn of 24-h
  GH time series (P = 0.0045). In counterpoint, 5 alpha-dihydrotestosterone, a
  nonaromatizable androgen, failed to produce a significant ApEn increase
  (P > 0.43)."
QUOTE (abstract, verbatim): "oral administration of ethinyl estradiol for 5 weeks
  to 7 prepubertal girls with Turner's syndrome also augmented ApEn significantly
  (P = 0.018), thus showing that estrogen per se can induce greater irregularity of
  GH secretion."
QUOTE (abstract, verbatim): "We conclude from these three distinct experimental
  contexts that aromatization of testosterone to estrogen in boys, or estrogen
  itself in girls, is likely the proximate sex-steroid stimulus amplifying
  secretory activity of the GH axis in puberty."
SOURCE: Veldhuis JD, Metzger DL, Martha PM Jr, Mauras N, Kerrigan JR, Keenan B,
  Rogol AD, Pincus SM. "Estrogen and testosterone, but not a nonaromatizable
  androgen, direct network integration of the hypothalamo-somatotrope (growth
  hormone)-insulin-like growth factor I axis in the human." *JCEM*
  1997;82(10):3414–20. DOI: 10.1210/jcem.82.10.4317
→ **I previously described this as "DHT failed to reproduce testosterone's GH
  effect". That is too loose.** The endpoint is **ApEn** — approximate entropy, the
  statistical *orderliness* of the 24-h GH secretion pattern. Not GH amplitude, not
  GH mean, and **not IGF-1 levels at all**.
→ So this paper supports the aromatization rule for **GH secretory pattern in
  puberty**, in n = 5 boys. It is not evidence about serum IGF-1 in men, and it
  must not be cited as if it were.

### B7c. Urban 1995 — the awkward one, and the reconciliation
Read from the rendered PDF page at `journals.physiology.org/doi/pdf/...E820`
(free to read); Table 1 transcribed from the page image, in the same way
`orca-09-gh-concentration` handles Pan 2010.
QUOTE (abstract, verbatim): "Ribonuclease protection assays done on total RNA from
  muscle showed that testosterone administration increased mRNA concentrations of
  IGF-I and decreased mRNA concentrations of insulin-like growth factor binding
  protein-4."
TABLE 1 (transcribed, basal → testosterone, means ± SE, n = 6):
  IGF-I 141 ± 27 → 163 ± 23 ng/ml (**not significant**)
  GH 0.9 ± 0.2 → 1.1 ± 0.3 ng/ml (**not significant**)
  Estradiol 17 ± 2 → 36 ± 6 pg/ml (**significant**)
  PSA 1.7 ± 0.6 → 2.1 ± 0.7 (significant); HDL 54 ± 8 → 45 ± 8 (significant)
SOURCE: Urban RJ, Bodenburg YH, Gilkison C, Foxworth J, Coggan AR, Wolfe RR,
  Ferrando A. *Am J Physiol* 1995;269(5 Pt 1):E820–6.
  DOI: 10.1152/ajpendo.1995.269.5.E820

→ **This is not a failure of aromatization.** Estradiol roughly **doubled**
  (17 → 36 pg/ml, significant) and serum IGF-1 still did not reach significance.
  Whatever separates Urban from Weissberger, it is not the conversion step.
→ **The two studies agree on direction and roughly on size.** Weissberger: 0.9 →
  1.1 U/mL, ~+22%, P < 0.05, hypogonadal men, 24-h sampling. Urban: 141 → 163
  ng/ml, ~+16%, ns, elderly men with low-normal testosterone, n = 6, 4 weeks. These
  are the same small effect, detected in one study and not in the other.
→ **So the correct statement of the rule is narrower than I had it.** Not
  "testosterone raises serum IGF-1 in hypogonadal men and not in elderly men", but:
  **the serum IGF-1 response to testosterone is small (~15–25%), and whether it
  reaches significance depends on the size of the baseline deficit, the sampling
  and the power.** The big, reliable androgen effect on the GH axis is on **pulse
  amplitude** in frank hypogonadism, not on the IGF-1 number.
→ What is genuinely aromatization/ER-dependent, with direct evidence: tamoxifen
  reversing GH and IGF-I in men (B7a), and DHT failing on GH pattern in boys (B7b).
→ **What is still inference:** that DHT, trenbolone or any non-aromatizable
  androgen *lowers* serum IGF-1 in men. Nobody in this set measured it. The
  blood-arm ranking is a mechanistic prediction with a small expected effect size,
  and it must be labelled as one.
→ Lewis 2002's characterisation of Urban (B6) is accurate on significance but
  hides both of these: that E2 doubled, and that IGF-1 rose 16% anyway.

## B8. Boldenone — the gap claim
CLAIM: no study has measured IGF-1, IGF-1R, IGF-1 splice variants or IGFBPs after
boldenone or boldione.
STATUS: **CHECKED INDEPENDENTLY, HOLDS.** Searched beyond the synthesis: rabbit,
lamb, buffalo-calf, horse and veal-calf literature exists and reports growth
performance, carcass traits, meat protein, thyroid hormones, reproductive hormones,
haematology and oxidative-stress markers. None found measuring the IGF axis.
→ Safe to state as an absence, which is unusual and is why it carries a deck.
→ Boldenone is aromatizable, so mechanism predicts it should behave like
  testosterone on the blood arm. **Prediction, not data** — label it as such on the
  slide. Do not put a number on "boldenone aromatizes at about half the rate of
  testosterone"; that figure is weakly sourced.

## B9. Nandrolone and circulating IGF-1 in humans — open item
CLAIM (as the synthesis made it): nandrolone does not change circulating IGF-1.
STATUS: **RAT LEG SETTLED, HUMAN LEG STILL OPEN.** The rat leg is B6 (Lewis 2002),
now verified from the full text: serum 287.6 ± 106.1 (CTL) vs 297.5 ± 86.0 ng/ml
(NAN), n = 7 per group — a genuine null, but an underpowered one. The human leg is
untouched. Human trials exist and did measure IGF-1 —
Johansen et al. 1999 *JAMA* (nandrolone decanoate in dialysis patients) lists IGF-1
in its results tables, and the HIV wasting trials are adjacent. Direction not
retrieved. Treat as an **open question**, not a settled null, until the full text is
read.

---

# C. Audit findings that correct existing topics

These came out of the same read and belong to decks that already exist.

## C1. `orca-09-gh-concentration` — provenance correction
The Sci-Bot EGFR page cites its central source as **Zhu H-J et al., *Clin Exp
Pharmacol Physiol* 2011** (DOI: 10.1111/j.1440-1681.2011.05547.x). The paper the
100 ng/mL dose–response actually comes from is **Pan Si-nian et al., *J Sun Yat-sen
Univ (Med Sci)* 2010;31(4):497–503**, which `orca-09-gh-concentration/07-claims.md`
already reads correctly off the rendered page images.
→ Two papers from the same Guangzhou group, silently merged into one citation. The
  AG490 / AG1478 / EGFR-Tyr1068 inhibitor data are from the 2011 English paper; the
  dose–response table and the 18 h EGF mRNA peak are from the 2010 Chinese paper.
→ `orca-09`'s numbers are unaffected and remain the better record of the two.

## C2. `hgh-02-dose` — the synthesis is missing its own keystone
The Sci-Bot HGH page recommends "0.05–0.1 mg/kg/day" for maximum stature without
citing Mauras 2000, the only randomised trial that tested the top of that range. It
also omits the IGF-1 SDS ceiling entirely, which leaves "highest tolerated dose"
undefined. `hgh-02-dose` and `hgh-09-igf1-ceiling` together are already stronger
than the synthesis on this question.

## C3. Unflagged contradictions inside the HGH page
Section 3 gives the rat systemic threshold as ~1 µg/day with 100–200 µg/day
saturating; section 4 says the response is monotonic to 400 µg/day. Both tensions
are real features of the literature and are presented as settled. If either number
is used, the tension goes on the slide as information.

## C4. `in vitro ng/mL` -> `mg/kg/day` is still not convertible
`orca-09-gh-concentration/07-claims.md` already states the two reasons (avascular
diffusion-limited plate; no GHBP buffering or hepatic clearance in medium). Three
more from this read, all worth adding there:
- **Pulse pattern, not level, drives the local pool.** Isgaard 1988, quoted in
  `hgh-04-exogenous/07-claims.md`: pulsatile GH raised muscle IGF-1 mRNA 3–5-fold,
  continuous GH did nothing, while hepatic IGF-1 mRNA was indifferent to pattern.
- **There is a time optimum as well as a concentration optimum.** Pan 2010:
  proliferation peaked at day 4 and was significantly lower by day 7 under
  continuous exposure.
- **The only quantity that bridges the two is IGF-1 SDS**, which is why clinical
  practice titrates on IGF-1 rather than on mg/kg.

## C5. An inference that is NOT cleared for a slide
Subcutaneous rhGH at 0.1 mg/kg produces a transient serum GH peak in roughly the
50–150 ng/mL band, which lands at the top of the in vitro inverted-U where
cultured chondrocytes stop improving. Two independent lines appearing to run out of
room at the same concentration is an attractive synthesis and it is **mine, from
approximate PK, with no paper behind it**. It needs a real PK study giving peak
serum GH by dose before it is said out loud.

---

# D. EGFR at the growth plate — separate deck, same read

## D1. A thicker growth plate can mean a shorter bone
CLAIM: blocking EGFR with gefitinib for 7 days in 1-month-old rats roughly doubled
growth-plate thickness — a 2.3-fold expansion of the hypertrophic zone — and
produced significantly shorter tibiae and femurs. Cartilage-specific EGFR
inactivation reproduces it.
STATUS: **UNVERIFIED**, and it is the best hook in the whole set, because the
intuition it breaks ("a wider plate means more growth left") is everywhere.
SOURCE: Zhang X, Siclari VA, Lan S, et al. "The critical role of the epidermal
  growth factor receptor in endochondral ossification." *J Bone Miner Res*
  2011;26(11):2622–2633. DOI: 10.1002/jbmr.502
SUPPORTING: "EGFR signaling regulates epiphyseal cartilage development through
  β-catenin-dependent and -independent pathways." *J Biol Chem* 2013.
  DOI: 10.1074/jbc.m113.463554
→ Mechanism to state: the plate is a conveyor. EGFR licenses the demolition end
  (MMP-9/-13/-14, RANKL, osteoclast recruitment at the chondro-osseous junction).
  Block it and cartilage piles up — better histology, shorter animal.

## D2. The EGF ligand is the minor half of the mechanism
CLAIM: in the GnRHa/GH chondrocyte experiments, the EGFR kinase inhibitor AG1478
**completely** abolished GH-induced proliferation while an EGF-neutralising
antibody only **partially** blocked it.
STATUS: **UNVERIFIED** — from the Zhu 2011 paper, see C1 for which paper is which.
→ Reading that the synthesis stated but did not underline: GH reaches ERK mainly by
  JAK2 phosphorylating EGFR at Tyr1068 and using it as a **scaffold** (no EGFR
  kinase activity needed), with the secreted-EGF autocrine loop as the smaller
  second arm. So the EGF that the 2010 paper measured is the lesser half.

## D3. EGF cannot be given, and the direction of interest is negative
CLAIM: EGF-overexpressing transgenic mice are growth retarded with a
prehypertrophic pile-up; betacellulin transgenics have shorter femurs
EGFR-dependently; systemic EGF at 150 µg/kg/day lowered circulating IGF-1 ~25% and
IGFBP-3 ~45%.
STATUS: **UNVERIFIED**, and the synthesis misattributed the first one — it cited
Schneider's 2009 *Trends Endocrinol Metab* **review**. The primary is Chan & Wong,
*JBC* 2000, EGF-overexpressing transgenics.
→ Usable conclusion: the actionable direction is "do not block EGFR in a growing
  child", not "add EGF".

## D4. EGFR is where three unrelated inputs converge
CLAIM: GH (GHR/JAK2 → EGFR-Tyr1068 → ERK1/2), trenbolone (GPCR → MMP2/9 → HB-EGF →
EGFR/erbB2 → IGF-1R) and cyclic mechanical loading (PKCδ → EGFR → PI3K-Akt →
ERK1/2) all reach proliferation through the same EGFR transactivation cassette.
STATUS: assembled from three separate UNVERIFIED sources (B5, D2, and
DOI: 10.1159/000447833 for the loading arm). None of the three Sci-Bot pages spotted
it, because each was answering its own question.
→ Strongest cross-topic finding available here. Verify all three legs before it
  carries a deck; it is also the natural bridge between this topic, `orca-09` and
  `mechanical-loading-bone`.

## D5. Where EGFR sits in the height equation — the bound on the claim
Growth rate ≈ k × (chondrocytes produced per column per unit time) × (final
hypertrophic cell volume), and hypertrophy dominates — terminal cell volume
correlates with growth rate at r ≈ 0.98 (Hunziker 1994, quoted verbatim in
`hgh-04-exogenous/07-claims.md`). EGFR acts on the proliferative pool and on the
clearance step. It does not set terminal cell volume.
→ So: fine-tuner, bidirectional, and **no human evidence links EGF concentration to
  stature**. Per `FORMATS.md` this does not get built into a hedging slide — it is
  one caveat line, stated and moved past.
