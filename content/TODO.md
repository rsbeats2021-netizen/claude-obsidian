# TODO — content pipeline

Last updated 7 Sep 2026. Everything outstanding, roughly in the order worth doing.

---

## Ready to post now

**`content/viral-bone-age/`** — 15 slides. Nine classic-style renders sent 14 Sep (3 styles × 3 image sets); pick one. Also carbon 4:5 in
`09-carbon/`. Caption in `08-caption.md`. Video script in `03-video.md`.
Every number has a verbatim quote in `07-claims.md`.

---

## 1. Claims still unverified — the biggest risk

74 slides across the older decks assert a number or a direction with no verbatim
quote behind them.

```bash
.venv/bin/python scripts/verify-claims.py
```

Work through them. For each: open the PDF, pull the sentence with
`scripts/extract-study-quote.py`, write it into that deck's `07-claims.md`. If
the sentence does not say what the slide says, fix the slide.

Three claims have already been caught this way and all three were wrong in the
same direction: overstated. Assume more are.

## 2. Old decks on the old format

24 decks are still on the 5-column CSV and the pre-rewrite voice. They need:
- the tag column dropped, 4 columns: `headline,subhead,body,punch`
- the voice rules in `content/FORMATS.md` applied
- endings checked. Six decks previously ended on a slide that undercut the
  whole deck ("not a lever worth pulling"). Those are fixed; check the rest.

```bash
.venv/bin/python scripts/check-deck.py "content/*/04-slides.csv"
```

## 3. Three-account pipeline — not built yet

Decided but not implemented. One brief, three outputs:

| account | voice |
|---|---|
| **restingzone** | middle ground, graphs, moderate text. What exists today. |
| account 2 | very simple, plain language, no jargon |
| account 3 | high pharmacological vocabulary, exact study wording, no extrapolation |

Needs a script that takes `01-research.md` and emits three `04-slides.csv`
variants. Same topics, different outputs. Account 3 is the easiest to get wrong
and the easiest to verify, since it should be near-quoting.

Palettes for accounts 2 and 3 are already saved in
`content/_STYLES/01-morph-palettes/`.

## 4. Post and measure

Nothing in `FORMATS.md`'s performance log has real numbers yet. After posting,
record plays / saves / follows per deck so format choices stop being guesses.

The corpus predictions to test against:
- 12+ slides saves best (33.7 per 1k vs 18.7 at 4-7)
- 4:5 beats 9:16 once slide count is controlled for
- video beats slideshow, 19,050 vs 7,106 median plays
- 45-90s is the video band; 15-30s is the worst

## 5. Video

`scripts/assemble-video.py` is built and works. Untested end to end on a real
Character Animator export.

Do once: put the ElevenLabs API key in the environment so TTS stops being a
manual step.

```bash
export ELEVENLABS_API_KEY=...
```

Then the loop is: script → ElevenLabs → Character Animator (lip-sync is
automatic) → `assemble-video.py`. Only the Character Animator step is manual.

## 6. Topics nobody covers

From the corpus scan. Coverage counts across 14 competitor accounts:

- **catch-up growth — zero posts.** Nobody has touched it. There is already a
  deck at `content/v2-catch-up/`.
- maxilla / jaw — 21 posts, 28,000 median. Highest performing topic in the set.
- resting zone stem cells — 28 posts, 24,000 median. Also the account name.

Avoid: GH/IGF-1 (80 posts, 16,700 median) and general growth plate (77 posts).
Saturated and underperforming.

## 7. Housekeeping

- Branch `content-pipeline-tiktok-decks` is unpushed. Needs `brew install gh`
  then `gh auth login`.
- `.raw/` is gitignored. Keep it that way, it is 886MB of copyrighted PDFs.
- Check `content/_style-analysis/CLAIM-AUDIT.md` before writing any deck that
  claims something does not exist. Four such claims have already been false.

## Standing rules, learned the hard way

- Never write a claim from a vault summary. Open the PDF.
- No exhaustiveness claims from one source. Not "there are only N studies",
  not "no trial has ever". The vault is what got downloaded, not the literature.
- One study screenshot per deck, cropped so it shows the sentence and not the
  authors' contact details.
- Species discipline. Rodent week-figures are never human timelines.

## Voice test decks (15 Sep)

`content/voice-<creator>/` — the bone-age deck rewritten nine times, each in one
competitor's measured voice (doctor.morph, _sox9, bio.science,
enhancements.explained, ntluccy, rpo3212, sy934821, tren2slay, 750tren). Same
claims, same receipts, classic style. Post them, note which voice performs, and
that becomes the house voice. Skipped: bigonial_ (memes), bpedpremed (screenshots
only), three accounts too small to profile.

## HGH decks (2 Oct)

Three decks, escalating depth, all in the doctor.morph guide voice, classic style:

- `content/hgh-01-simple/` — 9 slides. GH works through two routes (liver IGF-1,
  and directly on the plate). Blood test sees one. Hunziker 1994, Peng 1995.
- `content/hgh-02-dose/` — 10 slides. Mauras 2000 RCT: 2.3x the dose bought
  4.6 cm. Bone age did NOT accelerate. Insulin did move.
- `content/hgh-03-pulsatility/` — 13 slides. The best of the three. Same dose,
  continuous vs pulsed: continuous gave HIGHER serum IGF-1 and LESS growth
  (Bick 1992), convergent across Clark 1985 and Isgaard 1988. Ends on the honest
  limit: the one human trial split a daily dose in two and found nothing, because
  splitting a subcutaneous depot is not pulsing.

Note on topic saturation: GH/IGF-1 is the most crowded topic in the corpus
(80 posts, 16,700 median vs 25,100 for bone age). Deck 3 is the one with a real
angle; 1 and 2 are competing in a saturated space on execution alone.

### hgh-04-exogenous (2 Oct) — the flagship GH deck

17 slides. Covers local vs systemic IGF-1, bone age, and total height gains, all
verified. Sources outside the vault, fetched and verified against PubMed records
this session: Isaksson 1982 (PMID 7079756), Nwosu 2021 (PMID 33860132), Maghnie
2022 full KIGS cohort (PMID 36102184, N=83,803).

The spine: three independent experiments where serum IGF-1 and actual growth move
in opposite directions (Isaksson one-leg, Loveridge antiserum, Hunziker GH-beats-
IGF1-with-lower-serum-IGF1), plus Lui 2010 targeted-vs-non-targeted IGF-1 as the
cleanest proof that location beats concentration.

## Ten HGH slideshows (2 Oct)

| folder | slides | the finding |
|---|---|---|
| hgh-01-simple | 9 | two routes: liver IGF-1 and direct action on the plate |
| hgh-02-dose | 10 | Mauras RCT: 2.3x dose bought 4.6 cm, bone age unchanged |
| hgh-03-pulsatility | 13 | continuous gave higher IGF-1 and less growth (Bick 1992) |
| hgh-04-exogenous | 17 | flagship: local IGF-1, bone age, KIGS total gains |
| hgh-05-secretagogues | 9 | GHRP-2 >3x on day 1, >1.8x by day 14 (Bowers 2004) |
| hgh-06-partial-pulse | 9 | continuous < half-pulsed < fully pulsed (Gevers 1996) |
| hgh-07-chromatin | 10 | one GH pulse reopened 83% of closed DNA regions in 30 min |
| hgh-08-beyond-plate | 9 | after fusion GH is a bone-width drug, fracture risk down 3-4x |
| hgh-09-igf1-ceiling | 9 | clinics cap IGF-1 at 2 SDS; it is a safety marker, not a target |
| hgh-10-natural | 9 | 24wk jumping raised IGF-1 with GH unchanged (Wang 2025) |

All ten have a 07-claims.md with verbatim quotes. Sources verified against PubMed
records this session: Isaksson 1982 (7079756), Nwosu 2021 (33860132), Maghnie 2022
KIGS (36102184).

Three house rules now enforced: no "deck" on a slide, last slide is only
"DM for source", layout vertically centred for TikTok crop safety.

## Somatostatin series (2 Oct) — slideshows 11-14

| folder | slides | core finding |
|---|---|---|
| hgh-11-somatostatin | 11 | somatostatin sets rhythm, GHRH sets amplitude; Spoudeas 1992: GH response to GHRH depends on SS tone |
| hgh-12-pyridostigmine | 10 | doubled exercise GH AUC (Cappa 1993) but enhanced only the FIRST GHRH pulse, not the second (Spoudeas 1992) |
| hgh-13-ghrh-ghrp | 11 | GHRPs are NOT somatostatin blockers (Baldelli 2001); GHRH+GHS = most potent releaser known; GHS-R1a is the rate-limiting receptor for desensitisation |
| hgh-14-timing | 12 | Richmond 2002: one rhGH pulse blunted the GHRH response 2h later by driving somatostatin. The day/night stack is partly self-cancelling |

New sources verified against PubMed this session: Spoudeas 1992 (1353504),
Cappa 1993 (8370917), Marcell 1999 (10337872), Baldelli 2001 (11322508),
Richmond 2002 (12161519).

Compendium items marked [^unsourced] were NOT used as claims. Where the
compendium's stacking suggestions (CJC/ipamorelin doses, 3-pulse schedules,
5-on/2-off cycling) appear, they are unsourced there and appear on no slide.

## Compendium deep-dive (3 Oct) — slideshows 15-18

Mined `wiki/chats/Research Compendium.md` for the densest unused veins and for
places where independent lines converge.

| folder | slides | core finding |
|---|---|---|
| hgh-15-cnp | 14 | the second pathway. NPR2 carriers run z-score -1.8 vs -0.4 (Olney 2006); cartilage-only CNP knockout is almost as short as systemic; vosoritide +1.57 cm/yr in phase 3 |
| hgh-16-insulin-ghr | 12 | portal insulin builds the hepatic GH receptor. 8h off insulin: IGFBP-1 32→205, free IGF-1 undetectable in 15/17. Route beat glycemic control |
| hgh-17-fasting | 12 | GH up, IGF-1 down. Farnum 2003: 3-day fast dropped one tibial plate to 30% and stopped the other; refeeding overshot to 110-115% |
| hgh-18-dissociations | 14 | **the synthesis.** Nine published experiments where serum IGF-1 and growth moved opposite ways |

New sources verified against PubMed this session: Olney 2006 (16384845),
Farnum 2003 (12508079), Savarirayan 2020 vosoritide (32891212), cartilage-specific
CNP knockout (26014585).

18 HGH slideshows total, all passing check-deck, no broken SVGs.

## Beyond HGH (3 Oct) — four new topics

| folder | slides | core finding |
|---|---|---|
| ai-brain-penetration | 13 | letrozole reaches the brain **12.8x** more than anastrozole, because anastrozole is a P-glycoprotein substrate and gets effluxed (Miyajima 2013, mouse PK) |
| eleven-oxyandrogens | 13 | a second, adrenal androgen system. AKR1C3 prefers the 11-oxygenated precursor **8-24 fold** over classical substrates (Barnard 2018). Follows ACTH and insulin, not LH. Not on a standard panel |
| gh-thyroid-drain | 12 | GH upregulates DIO2, raising free T3 and **draining free T4**, while also blunting TSH. Unmasks central hypothyroidism in **36-47%** of hypopituitary adults who looked euthyroid |
| isotretinoin-dose | 13 | 88.4% sebum reduction but only 36.2% lesion reduction in the same 7 men; relapse tracks **cumulative** dose, not daily dose, in 19,907 patients (Lai & Barbieri 2025) |

Verified against PubMed this session: Miyajima 2013 (23712697), Barnard 2018
(29936123), Martins & Abucham 2008 (18797597), Goldstein 1982 (6213204),
Lai & Barbieri 2025 (39813053).

Selection method: ranked every compendium subsection by hard citation count,
removed anything already covered by an existing slideshow, then took the densest
remaining veins.

## ORCA account (3 Oct) — compound monographs

New style and format. `--style orca`: near-black, ice accent, colour-coded section
tags, spec strip from `00-spec.txt`. Full spec in `content/_STYLES/orca.md`.

Decisions taken: start with the HGH axis, published trial doses only, 11-13 slides.

HGH axis done (7 of ~90):
orca-01-hgh, orca-02-tresiba, orca-03-fiasp, orca-04-cjc-no-dac,
orca-05-ipamorelin, orca-06-ghrp2, orca-07-pyridostigmine.
Each has 04-slides.csv and 03-video.md.

**Still to do: ~83 compounds.** Next up by the agreed order: Chondrogenic
(vosoritide, erdafitinib, kartogenin, abaloparatide), then bioregulators, roids,
hormone support, and down the list.

Outstanding on the ones built:
- `07-claims.md` not yet written for the orca decks. The claims are all drawn from
  verified ledgers in the restingzone decks plus PubMed-verified sources this
  session, but each orca deck needs its own ledger file.
- No images yet on the orca decks. They render clean as text-only but need the
  diagram treatment to match the house image rule.
- Video scripts run 90-110s, above the 45-90s band.

## Video scripts (4 Oct) — complete

`scripts/make-video.py` built. **95/95 slideshows now have `03-video.md`**,
median 52s, every one inside the 45-90s band.

Replaces the old hand-written scripts, which ran 90-110s and were outside the
band. The generator selects the highest-value slides rather than transcribing
the deck.

Pipeline from here is unchanged: script -> ElevenLabs -> Character Animator
(lip-sync is automatic) -> `scripts/assemble-video.py`. Only the Character
Animator step is manual. Still outstanding: ELEVENLABS_API_KEY as an env var,
and `assemble-video.py` has never been run end to end on a real export.

## ORCA progress (4 Oct)

**13 of ~90 compounds done.** Theme switched from the dark `orca` style to
`clinical` (white package-insert). `dossier` and `signal` also available.
Outro changed from "It's never over" to "End of file / MONOGRAPH COMPLETE",
and the restingzone boxer no longer auto-attaches to non-restingzone styles.

Done — HGH axis (1-8) and Chondrogenic & Proliferative (10-13):
hgh, tresiba, fiasp, cjc-no-dac, ipamorelin, ghrp2, pyridostigmine,
gh-support, vosoritide, erdafitinib, kartogenin, abaloparatide.
All have 04-slides.csv + 03-video.md (77-82s).

Claims ledgers written for: orca-01, 09, 11, 13. **Still needed for 02-08,
10, 12.**

New primary sources used this batch, all from the vault:
- Majlessipour 2024 — pan-FGFR inhibition caused long bone overgrowth AND
  kyphoscoliosis in one pre-pubertal child. The proof and the warning are the
  same sentence.
- Starrett 2025 — TYRA-300, FGFR3-selective, increased tibia and femur length
  in wild-type mice as well as both disease models.
- Fischer 2015 — constant PTHrP suppressed chondrogenesis, pulsed (6h, 3x/wk)
  increased COL2A1 and collagen II. Same inversion as GH.

**Next group: Bioregulators & support peptides** — Vesugen, Cartalax, Vilon,
Livagen, Epitalon, Pinealon, Cortexin, GHK, FOXO4-DRI, SS-31, 5-AMINO-1MQ,
BPC-157. The compendium flags the Khavinson family as mixed/weak evidence, so
expect several "verdict: no" monographs in that batch.

Note: WebSearch/WebFetch are blocked for the rest of this session, so new
compounds can only be sourced from the vault, the compendium, and the OCR
corpus. Anything needing fresh PubMed verification should wait for a new session.

## ORCA — bioregulators batch (4 Oct)

**17 of ~90.** Added Vesugen, Cartalax, Vilon, Epitalon — the four the compendium
records as the user's own bioregulator cluster, so these were the highest-value
four in the group.

Shared evidence note written to `content/_STYLES/khavinson-note.md` and quoted on
the LIMIT slide of each, so the family-wide problem is stated every time rather
than assumed: no replication outside Russia, mechanism considered implausible,
dosing not PK-grounded, zero data in a growing animal.

Verdicts came out split rather than uniform, which is the right outcome:
- **Vesugen** — right compartment, but Ashapkin 2020 shows IGF1 +3-5.6x alongside
  NFκB +10-35x, which the authors expect to accelerate MSC ageing.
- **Cartalax** — no. 12 Europe PMC hits total, ambiguous sequence, unquantified
  capsule content, and it targets degeneration when closure is a timed programme.
- **Vilon** — the only one with a hard animal outcome (+16% lifespan, 0.1 µg
  5 days/month), but it is an immune peptide with no growth-plate data.
- **Epitalon** — most specific mechanism, rare primate dose data, and the only one
  whose risk scales with dose and duration (ALT activation in cancer lines).

Remaining in this group: Livagen, Pinealon, Cortexin, GHK, FOXO4-DRI, SS-31,
5-AMINO-1MQ, BPC-157. SS-31, GHK and BPC-157 have better evidence than the
Khavinson set and should read differently.

## Division of labour (15 Oct)

Compliance, disclaimers, advertising guidelines and claim substantiation for
launch are the account owner's, start to finish. Removed from my side:

- the self-imposed "no doses" rule in `_STYLES/orca.md` — replaced with "state the
  dose the study used, and say whether a dose is trial-derived or community
  practice", which is a sourcing distinction rather than a disclaimer
- defensive "What this does NOT claim" headers in 8 claims ledgers, reframed to
  "Scope of the evidence" where the content was informative (species, population,
  model) and deleted where it was purely protective

Kept, because it is a quality system rather than a compliance one:
- the claims ledgers themselves — 274 verbatim quotes across 37 files
- flagging when a number does not match its source. This has caught four real
  errors so far: the mandible claim (three times), the AI "only 4 studies" claim,
  "chronological age did worse" in the bone-age deck, and the author's email in a
  study receipt.

The two "not medical advice" slides in `voice-750tren` and `voice-ntluccy` are
NOT mine — they are faithful reproductions of those creators' own disclaimer
slides, which appear on 4 and 8 of their posts respectively. Removing them would
make the voice copies less accurate, so they stay.

## Androgens and IGF-1 (21 Oct)

`content/androgens-igf1-ranking/` — brief plus claims file, no deck yet.

Built from three Sci-Bot (sci-hub AI) answer pages, not from papers. Audited: real
references, resolving DOIs, correct mechanism, no fabricated data. Faults found were
two misattributed citations, one silent merge of two papers from the same group, one
bad inference ("100-fold") and two consequential omissions.

The claim worth a deck: **induction is not dependence**. How hard an androgen
induces IGF-1 and how much its anabolic effect depends on IGF-1R rank in opposite
orders — trenbolone is last on one and first on the other. The blood-IGF-1 arm is a
third list, and it is really a ranking of aromatization.

**Five claims are now verified** against the PubMed records with verbatim abstract
quotes: Wu 2007 (the AREs, PMID 17363459), Le 2006 (DHT/T 7-fold, PMID 16368782),
Pampusch 2008 (the trenbolone/estradiol dissociation, PMID 18676717), Thornton 2015
(the IGF-1R dependence route, PMID 26440329), Lewis 2002 (the IGFBP switch,
PMID 11788382).

Verifying five papers caught **six errors** that had come through the synthesis.
Full table in section B of the claims file; the two that change a conclusion:
- **DHT does not beat testosterone.** Le 2006 says "DHT and T **each**" increased
  IGF-1 7-fold. The induction ranking now reads DHT **=** T.
- **The 8-fold protein figure does not exist.** 7-fold covers mRNA and protein.

Two details stay demoted to unverified because the abstracts do not contain them
(additive AREs, DNA-binding-deficient AR, both Wu 2007).

The third was chased into the full text and **settled**. Lewis 2002 is free to read
at `journals.physiology.org/doi/full/10.1152/ajpendo.00191.2001`, and serum IGF-I
was **287.6 +/- 106.1 (CTL) vs 297.5 +/- 86.0 ng/ml (NAN)**, n = 7 per group, while
muscle IGF-I rose 50%. So the local/systemic dissociation is real and quotable --
but write it as a null, not an equivalence: those SDs are ~37% of the mean and the
study could not have seen a modest rise.

Reading one full text turned up three things no abstract contains:
- **Urban's elderly men showed the same split** -- muscle IGF-I mRNA up, serum IGF-I
  not elevated, on testosterone. Cuts both ways: supports "serum is a poor surrogate
  for the intramuscular axis", and qualifies the aromatization rule, since
  Weissberger & Ho's hypogonadal men *did* raise serum IGF-1 on testosterone.
  Aromatization governs whether; baseline governs how much.
- **Systemic IGF-1 downregulates local muscle IGF-1** (negative feedback), per the
  authors' own earlier work.
- **The testosterone RIA in that model cross-reacts heavily with nandrolone**, so its
  "serum testosterone" numbers are not usable.

One claim moved the other way: **Le 2006 cannot support "androgens up-regulate
IGF-1R"** — it reports IGF-1R explicitly unchanged by all four steroids. That came
from the Adzavon 2024 review instead, still unverified.

**B7 (the aromatization rule) is now verified too** -- Weissberger & Ho 1993
(PMID 8501143), Veldhuis 1997 (PMID 9329378), and Urban 1995 read from the free
PDF. It did not confirm the rule as I had written it; it **narrowed** it:

- Urban's elderly men **doubled estradiol** (17 -> 36 pg/ml, significant) and serum
  IGF-1 still rose only a non-significant +16% (141 -> 163 ng/ml, n = 6). So the
  thing separating Urban from Weissberger is **not** aromatization -- it is baseline
  deficit and statistical power.
- Weissberger's IGF-1 rise is +22% (0.9 -> 1.1 U/mL). Same modest effect, detected
  once, missed once. The big reliable androgen effect on that axis is on **GH pulse
  amplitude** (3.1 -> 5.2 ug/L), not on IGF-1.
- Veldhuis measured **ApEn** -- the orderliness of GH secretion -- not IGF-1. My
  earlier "DHT failed to reproduce testosterone's GH effect" was too loose to put
  on a slide.
- **Nobody in this set measured a non-aromatizable androgen lowering serum IGF-1 in
  men.** The bottom of the blood-arm ranking is mechanism, not measurement.

Running total: eight papers verified, **seven synthesis errors** caught, one rule of
my own narrowed, two claims taken past the abstract into full text.

Still unverified: B4 (Kamanga-Sollo 2004), the human leg of B9 (Johansen 1999 JAMA),
the two Wu 2007 full-text details, and all of section D. Nothing cleared to post.

None of the three PDFs got filed into `.raw/` — Sci-Hub returned not_found for all
three DOIs, so the quotes are abstract-level off PubMed, which is the same standard
`hgh-04-exogenous` uses for Isaksson 1982. Full texts still owed if a deck needs a
figure or a methods detail.

Two spin-offs recorded in the same file:
- **"A thicker growth plate can mean a shorter bone"** — gefitinib doubled plate
  thickness and shortened the bones. Best hook in the set; breaks a common intuition.
- **EGFR is where GH, trenbolone and mechanical loading converge.** Bridges this
  topic, `orca-09-gh-concentration` and `mechanical-loading-bone`. None of the three
  source pages spotted it.

Corrections owed to existing topics are in section C of the claims file —
`orca-09-gh-concentration` provenance (Pan 2010 vs Zhu 2011) and three additions to
its "ng/mL does not convert to mg/kg" argument.
