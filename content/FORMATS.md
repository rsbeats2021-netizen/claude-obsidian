# Deck formats — and the performance log

You post 3-5x a day and report back what won. For that feedback to teach us
anything, decks have to differ in a **controlled** way. Otherwise "this one did
well" just means "that topic was interesting" and we learn nothing reusable.

So every deck gets a format tag. When you report a winner, say the deck name and
I can tell whether it was the format, the topic, or the hook doing the work.

## The formats

| Tag | Shape | Best guess at what it tests |
|---|---|---|
| **A-CLASSIC** | 9-10 slides. Hook, conflict, evidence, mechanism, caveat, CTA | The baseline. Everything before today. |
| **B-COUNTDOWN** | Ranked list, 4-6 items, counting down | Listicles travel. Does ranking beat argument? |
| **C-MYTH-FACT** | Alternating. "They say X" then "Actually Y" | Rapid contradiction, very swipe-driven |
| **D-ONE-STUDY** | Single paper walked through slide by slide | Depth over breadth. Tests whether people want one thing properly |
| **E-TIMELINE** | Chronological. How the understanding changed | Story shape. Tests narrative vs argument |
| **F-NUMBERS** | Every slide leads with a figure | Screenshot bait. Numbers get saved |
| **G-AMMO** | Gives the viewer an argument to use on someone else | Tests whether "be right in a conversation" beats "learn something" |
| **H-GAPS** | What nobody has studied | Tests whether absence is as interesting as presence |
| **I-SHORT** | 5-6 slides, very tight | Tests whether shorter finishes better |

## Performance log

Fill in as you go. Even rough numbers are enough to see a pattern.

| Date | Deck | Format | Views | Saves | Completion | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |

## What to tell me

Minimum useful report: **deck name + roughly how it did vs your average.**

Better: where people dropped off. If they leave at slide 3 consistently, that's
a slide problem. If they leave at slide 1, it's a hook problem. Those get fixed
completely differently.

## What I'll do with it

After ~10 posts across formats there should be a signal. Then I stop spreading
effort evenly and start building more of whatever is working, and we test
variations inside the winning format instead of across formats.

Until then the spread is deliberate. Don't read early single results as strong
evidence, and I won't either.

## Decks by format (built 5 Sep)

**B-COUNTDOWN**
- `countdown-what-ages-your-plates` — 4 things ranked, then slide 7 turns on
  itself and points out the ranking implies false independence

**C-MYTH-FACT**
- `myth-vs-fact-growth-plates` — 6 rapid "they say / actually", covers six
  topics in one deck instead of one topic in nine slides

**D-ONE-STUDY**
- `one-study-the-transplant` — Nilsson & Baron 2004 walked through as a
  detective story: question, setup, prediction, result, consequence

**E-TIMELINE**
- `timeline-how-we-figured-it-out` — 1963 to 2025, six decades of the field
  being wrong in different ways. Ends on the currently unresolved edge

**F-NUMBERS**
- `numbers-that-matter` — seven figures, one per slide. Built to be
  screenshotted rather than read

**G-AMMO**
- `how-to-spot-a-fake-height-claim` — five questions to use on anyone selling
  something, with the last slide turning them back on this account

**A-CLASSIC** — everything else (37 decks)

## Writing rules (revised 6 Sep, after feedback)

The old decks argued. These explain. Every deck is now one of two shapes and
nothing else.

**SHAPE 1 — How something works**
Mechanism, then the evidence for it, then what it means for you. No detour
through what the literature debates.

**SHAPE 2 — A problem and what to do about it**
What goes wrong, how it goes wrong, which variants are worst, what actually
changes the outcome. If nothing changes it, say that plainly.

### Banned

- **Literature commentary.** "Chagin cites the earlier work and argues they are
  not strictly contradictory" tells a viewer nothing they can use.
- **Ending on 'nobody knows'.** If the last slide leaves someone with "we have
  androgen receptors in bone and don't know what they do", the deck failed.
- **Claim, then counterclaim, then a third point.** Pick the thing that is true
  and explain it properly.
- **Being vague to stay safe.** If a claim needs a caveat, state the caveat in
  one line and move on. Do not build a slide around hedging.

### Still required

- If the evidence isn't strong enough for a claim with no serious counter
  argument, say so in one line, or drop the claim. Do not fudge it.
- Dose, species and population stay attached to numbers. "4.5 to 9.6 cm/year in
  paediatric growth disorders" is usable. "It increases growth" is not.
- Where a real tradeoff exists it goes in as information, not as hedging.
  Oxandrolone gained height AND advanced bone age 3 to 7 months. Both are facts
  a viewer needs.

### Correction logged

`androgen-receptors-in-bone` has been deleted and replaced by
`local-conversion-growth-plate`. The old deck leaned on Chagin 2009 (no effect
of testosterone or oxandrolone on longitudinal growth in organ culture) and
presented that as the state of play. That was incomplete: a review of 45
studies found oxandrolone produced 4.5 to 9.6 cm/year growth velocity and 2.3
to 4.6 cm additional adult height in paediatric growth disorders. The organ
culture null result does not override the clinical record.

## Voice (measured 14 Sep from the corpus)

Compared the top play-count quartile of competitor slideshows (81 decks,
32,000+ plays) against the rest, per 1,000 words. The winners are not louder.
They are more like a good teacher walking a class through papers.

| move | top / rest |
|---|---|
| "we / our / us" | 1.6x |
| "the study showed that / found that" | 1.9x |
| jargon used, then glossed in the same sentence | 2.2x |
| "first study / second study / third study" | 2.7x |
| spoken connectors: so, but, lets, now | 1.4x |
| shock words: shocking, crazy, insane, wrong | **0.8x** |
| "you" | **0.9x** |
| "I" | **0.7x** |

Density also rises with plays: top quartile decks run ~60 words per slide over
7+ slides. The bottom quartile is 2 slides and 39 words. A wall of text does
not hurt. A thin deck does.

### What the winners actually sound like

doctor.morph, 186k plays, cleanest transcription in the set:

> "So there are a lot of mechanisms and pathways that play into this but lets
> go with the main one. Bones have osteocytes which are cells that can convert
> mechanical stressors into cellular signals..."

> "A very important study, Cullen 2001, compared soft vs hard loads and 40,
> 120 and 400 loads. The results showed that hitting hard = more bone
> formation. But the most shocking part was that 120 loads was almost as good
> if not better than the group that received 400 loads. This means that..."

> "How do we use this to our advantage? So from the previous studies there
> seems to be a mechanism that... To use this mechanism to our advantage we
> will not do all our smashing at once but instead..."

_sox9, 149k: "many of you will think this is bad, which is wrong because...",
"And now with the third study we learn that..."

### The rules that replace "second person, absolute, stacked, no connectors"

That rule was mine and the corpus does not support it. Replace with:

1. **Guide voice.** "We" and "lets" when walking through evidence. "You" for
   the payoff. "I" rarely.
2. **Name the study inline, then report it.** "Kvist 2021 imaged 958 people
   and found that..." beats a bare number with a citation in the footer.
3. **Use the real term, then gloss it in the same breath.** "growth plate
   senescence, which is the plate running out of divisions". Never dumb the
   term out. Never leave it unexplained.
4. **Connectors are allowed.** So, but, now, what this means is, the shocking
   part is. They are how a person talks. Sentences can run 20+ words.
5. **Number the studies** when there is more than one. "The first study...",
   "the second study..." Viewers track it.
6. **Pre-empt the objection** once per deck. "You might think X. That is wrong
   because..."
7. **End on application.** "So how do we use this?" then the answer.
8. **No hype vocabulary.** Shock words score below average. Confidence comes
   from "the study showed", not from "insane".

### Text per slide, by position (measured 14 Sep, top quartile, all text on the slide)

| slide | words | what it is |
|---|---|---|
| 1 | **8-12** | the hook. rpo3212, _sox9, sy934821 run 8. never more than 15 |
| 2 | ~50 | setup, where the number comes from |
| 3-4 | 100-120 | the peak. argue hardest here |
| 5 | ~75 | the receipt. the screenshot carries it |
| 6-8 | 95-110 | mechanism and second study |
| 9-10 | 50-65 | payoff, thinning out |
| last | ~45 | CTA |

Cover is 10% of the deck's peak. The shape is a ramp, not a plateau. My first
drafts were the inverse (covers 25-60 words, middles 55-85). Fixed 15 Sep.

## Density, measured against the top 12 (3 Oct)

Compared my slideshows with the 12 highest-play competitor slideshows that have
5+ slides and 200+ words. The gaps were large and all in one direction.

| metric | theirs | mine (before) | fix |
|---|---|---|---|
| **words per slide** | **101** | 50 | roughly double the body |
| sentence length | 19.4 | 13.3 | let sentences run |
| questions per post | 2.5 | 0 | use question headlines |
| numeric words | 10.7% | 3.8% | put the comparison values in |
| "I" per 1k words | 7.7 | 0 | occasional first person |
| "we" per 1k | 2.5 | 0 | "we" for the application step |
| "you" per 1k | 4.8 | 9.6 | ease off |

### The moves doctor.morph makes on a 113-188 word slide

1. **Define the term inline.** "Loading frequency = how often does the bone get hit."
2. **Study, design and result in one flow.** "Cullen 2001, compared soft vs hard
   loads and 40 - 120 - 400 loads. The results showed..."
3. **Translate after every technical sentence.** "What this means is that you want
   a pulsatile and thus a rapid load and not a continuous load."
4. **Stakes in the headline.** "Everyone bone smashes COMPLETELY WRONG."
5. **Question headlines.** "How long should you smash?", "How do we use this to
   our advantage?"
6. **"we" for application.** "we will not do all our smashing at once but instead,
   we will spread it out throughout the day."
7. **Each slide teaches one complete sub-lesson** rather than carrying a fragment.

Target: ~100 words of body per content slide, 2-3 question headlines per post.

### The numeric-density gap was an artifact, and the real finding is better

Their text measured 10.7% numeric against my 3.8%, which looked like a 3x gap.
Separating OCR'd figure text from actual prose:

| | numeric words |
|---|---|
| their prose lines only | **4.7%** |
| their full on-slide text | 11.1% |
| mine | 3.2% |

So their prose is only slightly more number-dense than mine. The gap was coming
from somewhere else: **26% of all the text on their slides is the study figure
itself** — axis labels, p-values, sample sizes, legible enough that OCR reads
them. Their screenshots are large and show DATA.

Mine crop a highlighted sentence, which is a stronger receipt for one claim but
puts far less on the slide. Worth testing a larger figure crop that shows the
actual plot, not only the sentence.

### Renderer change this forced
At ~100 words the fit pass used to starve the diagram down to a stamp, because
the image yielded before the copy did. `render-classic.py` now shrinks copy to a
19px floor FIRST and only then squeezes the image, with a hard minimum of 30% of
frame height. Dense copy and a legible diagram now coexist.

## Standing rules added 2 Oct

- **Never use the word "deck" on a slide.** It is production vocabulary. Viewers
  see a slideshow, a post, or nothing at all. Say "here", "in this", or rewrite
  the sentence.
- **The last slide says only `DM for source`.** No sources line, no hashtags, no
  "comment SOURCES". One instruction.
- **The cover is a hook, never a CTA.** 8-15 words, headline + subhead + one punch
  line, no body. "DM for source" belongs on the last slide only.
- **Layout is vertically centred.** `render-classic.py` centres headline and body
  as one block in the middle of the frame, so a TikTok crop eats empty margin
  instead of the headline.

## Rule added 7 Sep: no exhaustiveness claims

The aromatase inhibitor deck said "the entire evidence base is four randomised
trials, 207 participants." That was false.

Where it came from: a vault source note reporting that **one systematic review
found 4 RCTs meeting its inclusion criteria** (AI vs placebo, male children and
adolescents, short stature). A narrow filter applied by one review became, in my
deck, a census of the whole literature.

It was checkable and I did not check it. Searching outside the vault found
Hero 2006 (near final height, constitutional delay), Mauras (AI vs GH vs
combination), Salehpour (letrozole vs oxandrolone, placebo controlled), a 2024
three year anastrozole vs letrozole trial in 79 males, an anastrozole plus GH
multicentre trial, and a 2019 monotherapy study reporting no adult height gain.
I had also already used Jacobson 2005 in another deck, which alone disproves the
claim.

### The rule

**Never claim a literature is complete, small, or settled from a single source.**

Banned phrasings unless verified by an actual literature search:
- "the entire evidence base is..."
- "there are only N studies"
- "no trial has ever..."
- "nobody has looked at..."

A systematic review's inclusion count describes **that review's filter**, not the
field. Say "one systematic review found 4 RCTs meeting its criteria" or say
nothing.

### And search outside the vault

The vault is what happened to get downloaded. It is not the literature. Any
claim about what does or does not exist has to be checked against the actual
literature, not against the file count in `.raw/Studies`.

Where a claim cannot be verified, leave the question open rather than closing it
in the direction that sounds stronger.

## Image rule (added 2 Oct, after an audit)

**Every content slide carries an image.** Cover and outro are the only text-only
slides. The top creators run one on nearly every slide; six of the ten HGH
slideshows shipped with images on 2 of 9 before this was caught.

Three kinds, mixed:
- a generated diagram (bars, flow, two-column compare, checklist, quote card)
- a figure cropped from the source PDF
- one highlighted-sentence receipt per slideshow

`scripts/check-deck.py` now parses every SVG in the slideshow's image folder. A
bare `<` or `&` in copy like "P < 0.001" makes the file invalid XML; Chrome then
renders **nothing** and the slide ships with a hole in it, silently. Ten files
were broken that way, one of them in a slideshow from weeks earlier.
