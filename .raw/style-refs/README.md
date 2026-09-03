# Style references — short-form content

Drop examples of the slideshows and videos you want to make here. Claude reads
these once and distills them into `wiki/concepts/House Style - Short Form.md`,
which every future script/deck generation reads first.

Full guide: `~/Documents/Claude/Prompts/tiktok-slideshow-pipeline.md`

## Where things go

```
slideshows/<deck-name>/01.png, 02.png, ...   one screenshot per slide, IN ORDER
slideshows/<deck-name>/note.md               1-2 lines: what you like about it

scripts/<video-name>.md                      transcript (spoken words), plus
                                             1-2 lines on why it works

anti-examples/<name>/                         same shape as above, plus WHY it
                                              underperformed
```

## Format rules that matter

- **Slideshows: screenshots, not transcribed text.** Screenshots carry the copy
  *and* the hierarchy, emphasis, and words-per-slide. Transcription throws away
  half the signal.
- **Videos: transcripts as text, not video files.** Claude can't watch video.
  Paste the spoken words, or the auto-captions with timestamps.
- **Number slides so sort order matches read order** (`01`, `02`, ... not `1`,
  `2`, ... `10`).
- **Always add the 1-2 line note.** Without it Claude reverse-engineers your
  taste from raw artifacts and will guess wrong on some of it.

## How much

3-5 slideshow decks, 2-3 scripts, 1-2 anti-examples. Patterns repeat fast;
more than that has diminishing returns.

Anti-examples and any TikTok drop-off data (which slide lost people) are the
highest-signal items here — worth more than extra good examples.
