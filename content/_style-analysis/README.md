# Style analysis — drop competitor slideshows here

## How to give them to me

Account, then slideshow, then screenshots in order:

```
content/_style-analysis/
  @accountname/
    deck-01/
      01.png  02.png  03.png ...
    deck-02/
      01.png  02.png ...
  @otheraccount/
    deck-01/
      ...
```

This grouping is better than a flat pile, because voice belongs to the account
and topic belongs to the deck. Several decks from one account show me that
creator's sentence habits. Decks across accounts show me what's common to the
format itself rather than to one person. I can't separate those from a flat
folder.

Numbering the screenshots is the only thing that has to be right. Slide order
carries the argument, and a deck read out of order tells me nothing about how
they build a swipe.

Anything you happen to know per account is useful in `notes.txt` at the top
level, but none of it is required:
```
@accountname = big account, mostly height
@otheraccount = smaller, more general fitness
```

**Do NOT tell me which performed best.** That's the point of the exercise. I
guess first, you correct me, and the gap between my guess and reality is the
actual information.

## What I'll produce

For each deck:
- **Sentence shapes.** Length, how many clauses, where the verbs sit
- **Opening move.** How slide 1 earns the swipe
- **Connectors.** How they get from slide to slide (this is where I'm weakest)
- **Vocabulary level.** Which technical words survive, which get replaced
- **Closing move.** How the last content slide lands
- **What they leave out.** Often more informative than what they include

Then a **ranked guess** at which performed best, with my reasoning stated so
you can see whether I read it right or got lucky.

## Why the guess matters

If I predict correctly, my model of what works is roughly right and I can write
against it. If I'm wrong, my model is wrong, and that's more useful to find out
on your examples than on twenty of my decks that flop.

## Batch size

10 to 20 slides per deck, 3 to 6 decks per batch. More than that and I'm
skimming rather than reading.

## What I already know I do badly

Measured across my own 44 decks:

- "Which is why" opens a slide **18 times**. 33 slides open with some
  "which..." connector.
- "The honest read / position / version" appears **7 times**.
- "X is not the same as Y" used as a closing line **7 times**.

Same sentence shape reused. Real writing varies its connectors. If the decks you
send do this differently, that's the first thing I want to copy.

---

# Videos

Same structure, videos alongside the slideshow folders:

```
content/_style-analysis/
  @accountname/
    deck-01/          slideshow screenshots
    video-01.mp4      video files sit at the account level
    video-02.mp4
```

## How videos get read

I can't watch video or transcribe audio. But captions are almost always burned
in, so frames recover the spoken script visually:

```bash
.venv/bin/python scripts/extract-video-frames.py content/_style-analysis/@account
```

It samples a frame a second, then drops near-identical neighbours, so a 60
second video collapses to roughly 15-25 frames: about one per caption change.
Then I read those.

It also reports pacing, which is a real stylistic variable in itself: duration,
number of caption changes, and seconds per caption. A creator changing captions
every 1.2s is writing very differently from one changing every 4s.

**If a video has no burned-in captions I can't recover the script.** Paste the
words in a text file next to it and I'll work from that.

## What I'm comparing across the two formats

Slideshow and video are different problems and should read differently:

| | Slideshow | Video |
|---|---|---|
| Who sets the pace | Reader | Creator |
| Re-reading | Free | Impossible |
| Engagement action | Swipe | Keep watching |
| Sentence length | Can carry longer | Has to land first time |
| Hook window | Slide 1, self-paced | ~3 seconds of autoplay |

So the questions are: do the accounts write these differently, or reuse one
voice for both? Are the same topics structured differently per format? Does the
hook change shape when the viewer can't control the pace?

If a creator uses one voice for both, that's worth knowing. If they split, the
split itself is the lesson.
