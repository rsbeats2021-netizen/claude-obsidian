# Style library

Every design built so far, in one place, with the command to reproduce it.

Account: **@restingzone**

---

## 01-morph-palettes  — for the new account test

Eight colour worlds on one layout. The layout is modelled on doctor.morph,
whose deck is the second highest performing slideshow in the scrape. The colour
is deliberately not his, so these read as their own brand.

```bash
.venv/bin/python scripts/render-morph.py content/<deck> --palette <name> --brand RESTINGZONE
```

| palette | ground | headline gradient | mechanism | numbers |
|---|---|---|---|---|
| `slate` | pale blue-grey | black to blue | blue | red |
| `forest` | sage wash | black to green | green | burnt orange |
| `ember` | warm cream | black to orange | amber | red |
| `violet` | pale lilac | black to violet | purple | pink |
| `paper` | warm neutral | black to sage | green | rust |
| `midnight` | deep navy | white to cyan | teal | soft red |
| `carbon` | near black | white to amber | amber | coral |
| `deepgreen` | dark forest | white to mint | mint | soft red |

Sizes: `--size 3:4` (default, his canvas), `4:5`, `9:16`.
Images: `--images none | few | mixed | many`. `mixed` is the default and is the
recommended blend.

**Testing plan.** One palette per account, or one palette per week on a single
account. Log results in `content/FORMATS.md`. Do not change two variables at
once or the result tells you nothing.

---

## 02-other-styles  — earlier directions, kept for reference

```bash
.venv/bin/python scripts/render-v3.py content/<deck> --style <name> --size 4:5
```

| style | look |
|---|---|
| `editorial` | warm paper, serif headline, left aligned |
| `editorial-grey` | light grey, serif, blue rule |
| `editorial-centre` | neutral grey, centred, green accent |
| `dark` | near-black, Anton condensed, amber and cyan |
| `blocks` | headline reversed out of a black band, poster style |
| `morph` | light blue-grey, Archivo Black caps |

The three editorial variants are too close to each other to be worth testing
separately. If you want that direction, pick one.

---

## Emphasis markers

Same in every renderer. Each treatment means something specific so a returning
viewer learns to read them:

| marker | renders as | means |
|---|---|---|
| `*term*` | accent colour | mechanism, receptor, gene, enzyme |
| `**number**` | second colour, bold | a figure or hard finding |
| `_phrase_` | underline | the conclusion of the slide |
| `==phrase==` | highlight | the thing to remember |

---

## Images

| mode | what it does |
|---|---|
| `none` | text only |
| `few` | generated diagrams only |
| `mixed` | diagrams, plus real figures, plus **one** study receipt |
| `many` | fills every spare slide with a receipt |

**One receipt per deck.** Repeating the same screenshot across slides reads as
padding rather than evidence.

### Two kinds of receipt

```bash
# just the journal line and title, cropped tight
.venv/bin/python scripts/extract-study-quote.py "<pdf>" --title out.png

# the exact sentence a claim rests on, highlighted in the paper
.venv/bin/python scripts/extract-study-quote.py "<pdf>" --quote "increased by an average of 27.2%" out.png
```

The quote crop is stronger. Instead of "here is a paper" it shows "here is the
line that says it", with the line marked, so the viewer can read the evidence
themselves.

It also catches errors. Running it on the mandible paper surfaced "No
statistical group difference existed" sitting immediately after the juvenile
numbers, which had been presented as a finding in two earlier versions of that
deck.

## 03 — classic (the original restingzone look)

Measured from the first Canva decks. Grey ground `#D9D9D9`, Anton headline in
black, Montserrat 800 subhead in `#004AAD` caps, Poppins body, one white image
card mid-slide, bold punch. Light blue `#9ACEE8` for highlights. Outro is the
boxer, `03-classic-assets/outro-boxer.png`.

```bash
.venv/bin/python scripts/render-classic.py content/<deck> --size orig
```

Unlike morph, this style reads the `subhead` column. Headline + subhead is the
sentence, body explains, image shows, punch lands. Image on nearly every slide:
a study figure cropped from the PDF, a generated diagram, or a receipt with the
sentence highlighted. Same `03-images/` conventions as morph, plus
`slide-NN-a` / `slide-NN-b` for two images side by side.

### Image sets (same deck, different image folders)

`render-classic.py --images <folder>` swaps the image folder, so one deck can
carry several sets for A/B testing:

- `03-images-copy` — only what the top creators use: PubMed page screenshots
  (bpedpremed), paper text with a highlighted sentence (_sox9), figures cropped
  from the PDF, one flat icon (rpo3212)
- `03-images-best` — a figure where the claim is visual, a graph where it is
  numeric, a receipt where it is a sentence
- `03-images` — generated graphs + quote receipts + pathway figures

Layout keeps everything inside TikTok's safe zone: top 11.5% and bottom 19%
are empty, right margin is wider for the button column.
