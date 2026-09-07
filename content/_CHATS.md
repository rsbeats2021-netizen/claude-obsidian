# How to split this work across chats

## Using this file

Paste **one** prompt into a new chat, not the whole file. The other four
workstreams are wasted context in a chat that will not touch them.

Shorter and self-updating, since Claude Code can read the repo:

```
Read content/_CHATS.md and follow the RESEARCH AND CLAIMS section. Topic: <X>
```

That one line works for any of the five. Swap the section name. If I later
change the rules in this file, the prompt stays correct without you editing
anything, which the pasted version does not.

Use the full pasted prompts below when you want to override or add to what the
section says for a one-off.

## Use Claude Code, not Cowork

Everything here is files and scripts in this repo: decks, briefs, claims
ledgers, renderers, the OCR corpus. Claude Code reads and writes those directly
and can run the tooling. Cowork is a different surface aimed at connecting
external tools, and would mean handing files back and forth for work that is
already local.

Stay in Claude Code. Open a **new session per workstream** rather than one long
one.

## Why split at all

Every turn re-sends the whole conversation. A long chat costs more per message
than a short one for the same work, and the growth is not gentle. Splitting also
means a mistake in one workstream does not sit in the context of the others.

The vault is the shared memory. `01-research.md`, `07-claims.md`, `FORMATS.md`,
`_STYLES/README.md` and `_style-analysis/FINDINGS.md` all persist, so a fresh
chat picks up without being re-briefed.

---

## The five chats

### 1. RESEARCH AND CLAIMS  — Opus, high effort

The expensive thinking. Reading papers, verifying claims, writing briefs. This
is where accuracy is decided, and it is worth the best model.

```
Read content/FORMATS.md and content/_style-analysis/CLAIM-AUDIT.md first.

I want a research brief for <TOPIC>, following the pattern in
content/v2-local-conversion/01-research.md.

Rules:
- Every numeric or directional claim needs a verbatim quote from the PDF, saved
  to 07-claims.md with the source path and page
- Use scripts/extract-study-quote.py to pull the exact sentence
- Search outside .raw/Studies before claiming anything does not exist. The vault
  is what got downloaded, not the literature
- If evidence is not strong enough for a claim with no serious counter argument,
  say so or drop it
- Tier tag every point 1/2/3
```

### 2. DECK WRITING  — Opus

Voice is the hard part and does not delegate well. Feed it a finished brief.

```
Read content/FORMATS.md and content/_STYLES/README.md.

Write the deck for content/<deck>/ from its 01-research.md.

- 13 slides, 4 columns: headline, subhead, body, punch
- body statements separated by " | "
- markers: *term* mechanism, **number** figure, _phrase_ conclusion,
  ==phrase== the thing to remember
- slide 1 is a promise with no content
- second person, absolute, statements stacked, no connectors
- no em dashes, no literature commentary, no "nobody knows" endings
- every number must already exist in 07-claims.md

Then run: .venv/bin/python scripts/check-deck.py "content/<deck>/04-slides.csv"
```

### 3. RENDERING AND EXPORT  — Sonnet

Mechanical. Does not need the expensive model.

```
Read content/_STYLES/README.md.

Render <deck(s)> with:
  .venv/bin/python scripts/render-morph.py content/<deck> --palette <name> --brand RESTINGZONE

Then zip the output to /tmp and send it to me. If total size is over 30MB,
convert to JPEG q88 first.
```

### 4. COMPETITOR ANALYSIS  — Sonnet for the crunching, Opus to interpret

The corpus is already built and costs nothing to query.

```
content/_style-analysis/slide-text.jsonl holds 2,353 OCR-transcribed competitor
slides across 14 accounts. content/_style-analysis/all-posts.csv holds their
stats.

Join them and tell me <QUESTION>, for example:
- which topics get the most views, per account and overall
- which claims recur across creators and how they are evidenced
- which studies are cited most often
- what topics nobody covers

Do the counting in Python. Do not read the images.
```

### 5. VIDEO  — Opus for scripts, Sonnet if we build the ffmpeg renderer

```
Read content/_style-analysis/FINDINGS.md section 3 for the length data.

Write the video script for content/<deck>/ from its 01-research.md.
60 seconds, ~178 words, spoken lines separated from visual directions.
```

---

## Model guide

| work | model | why |
|---|---|---|
| research, verification, briefs | **Opus** | accuracy decisions, worth the cost |
| deck copy, video scripts | **Opus** | voice does not delegate |
| rendering, exporting, file wrangling | **Sonnet** | mechanical |
| stats and corpus queries | **Sonnet** | it is Python, not judgment |
| interpreting what the stats mean | **Opus** | that part is judgment |

## Keeping cost down

- Local tools are free. OCR, ffmpeg, pymupdf, every script in `scripts/`. The
  2,353-slide transcription cost nothing.
- Me reading an image costs ~1.2k tokens. Reading transcribed text costs almost
  nothing. Prefer the corpus over the screenshots.
- Do not ask me to re-read files I just wrote.
- Batch: "render these six decks" beats six messages.
- Start a fresh chat when a workstream is done rather than continuing.
