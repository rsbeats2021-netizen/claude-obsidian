---
type: meta
title: "Lint Report 2026-07-27"
created: 2026-07-27
updated: 2026-07-27
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-27

Run after a large multi-session Endocrinology-domain ingestion effort (~281 on-topic sources, ~98 off-topic flags) followed by a full corpus reorganization (419 files renamed and sorted into 9 topical folders, 8 new vocabulary pages, 2 new pathway-comparison documents). This is the first `/wiki-lint` pass of the session — flagged earlier as a process gap (CLAUDE.md recommends linting every 10-15 ingests; roughly 14 ingestion batches ran without one).

## Summary
- Pages scanned: 482
- Issues found: 43 (11 orphans, 20 dead links, 7 frontmatter gaps, 10 hits from a naive empty-section heuristic — most benign/false-positive, 1 systemic DragonScale-addressing gap affecting ~350+ pages)
- Auto-fixed: 5 (orphan source pages linked into `sources/_index.md`)
- Needs review: 1 major (DragonScale addressing scope), rest are pre-existing and low-severity

## Orphan Pages

11 found; 6 are meta/reference pages that are orphan-by-design (session logs, fold artifacts, tiling reports, reference docs not meant to be linked from content pages) and were left alone:
- [[fold-k3-from-2026-04-23-to-2026-04-24-n8]], `wiki/meta/2026-04-10-backlink-empire-session.md`, `wiki/meta/retrieval-benchmark-v1.7.md`, `wiki/meta/tiling-report-2026-04-24.md`, [[methodology-modes]], [[transport-fallback]]

5 were real gaps — source pages that existed but were never linked from `sources/_index.md` (from earlier in this session, before this lint pass). **Auto-fixed**: added all 5 to `sources/_index.md`.
- [[ERalpha-Cell-Proliferation-Cancer-UPR-Livezey]]
- [[GPER-ERalpha-Breast-Cancer-Structural-Saha]]
- [[Kursk-Medical-Conference-Proceedings-Misplaced]]
- [[Magnocellular-Hypothalamo-Neurohypophysial-Gene-Regulation-Burbach]]
- [[Russian-Patent-Cell-Culture-Method]]

## Dead Links

20 found, all pre-existing from much earlier (pre-Endocrinology, plugin/SEO-development) sessions — confirmed unrelated to tonight's ~40 new pages and the file reorganization. Not fixed (out of scope; would need investigation into whether each target page was renamed, never created, or intentionally deferred):
`[[AI Marketing Hub Cover Images Canvas]]`, `[[Claude Canvas]]`, `[[Claude Obsidian]]`, `[[E-commerce SEO]]`, `[[Foo]]`, `[[How does the LLM Wiki pattern work?]]`, `[[Karpathy LLM Wiki Pattern]]`, `[[Rankenstein]]`, `[[Three laws of motion]]`, `[[Wiki Map]]` (likely a `.canvas` file, not `.md` — probably a false positive of this checker), `[[claude-obsidian-presentation]]`, `[[dashboard.base]]` (likely a `.base` file, same caveat), `[[fold-template]]`, `[[mcp-setup]]`, `[[methodology-modes-guide]]`, `[[notes/Foo]]`, `[[wiki-cli]]`, `[[wiki-fold]]`, `[[wiki-mode]]`, `[[wikilinks]]`

## Frontmatter Gaps

7 found, all pre-existing meta/reference pages from earlier plugin-development sessions (none in the Endocrinology domain or tonight's new content):
- `wiki/references/methodology-modes.md`: missing `created`, `updated`
- `wiki/references/transport-fallback.md`: missing `created`, `tags`
- `wiki/meta/2026-04-15-release-report-session.md`: missing `created`
- `wiki/meta/tiling-report-2026-04-24.md`: no frontmatter at all
- `wiki/meta/2026-04-15-slides-and-release-session.md`: missing `created`
- `wiki/meta/boundary-frontier-2026-04-24.md`: missing `created`
- `wiki/meta/retrieval-benchmark-v1.7.md`: missing `created`, `tags`

## Empty Sections

10 hits from a naive heading-boundary heuristic; on inspection, all are either intentional placeholder markers (`## Add new sources here after each ingest.` in the two `_index.md` files) or likely false positives where a heading is immediately followed by a bullet list or sub-heading that the checker's regex didn't associate correctly (`cherry-picks.md` tier headers, `Wiki vs RAG.md`, `SVG Diagram Style Guide.md`). Not treated as real issues.

## Stale Claims

No new stale claims identified beyond what's already flagged in-line with `[!contradiction]` callouts throughout the Endocrinology domain (e.g., the Schrier 2006 vs. Nilsson 2014 sex-specific resolution, the Windahl→Lindberg authorship correction from earlier tonight, the cAMP context-dependence noted in the new [[cAMP Signaling in Chondrocytes and Osteoblasts]] page). This domain has been unusually diligent about flagging contradictions as they were found rather than accumulating silent staleness.

## Missing Pages

Addressed proactively this session: 8 new vocabulary pages ([[GPER-1 (GPR30)]], [[Kartogenin]], [[FGFR3]], [[OPG-RANKL Axis]], [[HDAC (Histone Deacetylases) in Chondrocytes]], [[cAMP Signaling in Chondrocytes and Osteoblasts]], [[Osteolectin]], [[Catecholamines and Beta2-Adrenergic Receptor]]) plus 2 new comparison documents were created specifically to fill terms/themes that recurred across multiple sources without a dedicated page. No further clearly-recurring undefined terms were identified in this pass.

## Cross-Reference Gaps

Not exhaustively scanned across all 482 pages (would require semantic entity extraction beyond this pass's scope); no specific gaps flagged beyond the orphan-page fixes above.

## Stale Index Entries

None found — `wiki/index.md` and `wiki/domains/Endocrinology.md`'s wikilinks all resolve to existing pages (confirmed via the dead-link scan above, which found zero index-specific breakage).

## DragonScale Address Validation — Major Finding, Needs User Decision

- Counter state: peek = `3` (next allocatable is `c-000003`)
- Highest `c-` address observed: `c-000001` (on `wiki/concepts/DragonScale Memory.md`)
- Rollout baseline: `2026-04-23` (from `.vault-meta/legacy-pages.txt`)
- **Only one page in the entire 482-page vault has an `address:` field.** Every other page created since the 2026-04-23 rollout — which includes the *entire* Endocrinology domain (~350+ pages) and all of tonight's new vocabulary/comparison pages — is classified "post-rollout, address required" per the lint skill's own rule, and is technically a lint **error** for lacking one.

> [!gap] This isn't something introduced tonight — it reflects that DragonScale addressing was demonstrated once (on its own concept page) and never adopted as an actual practice for real content, despite being technically "enabled" (script executable + counter file present, which is what the skill's detection check tests for).

**Resolved**: asked the user directly. Chose to formalize all 435 qualifying pages as legacy rather than backfill addresses retroactively. Appended all 435 paths to `.vault-meta/legacy-pages.txt` with a dated comment explaining why. Re-verified afterward: zero post-rollout pages remain unaccounted for. Future `wiki-ingest` runs may still assign addresses to new pages going forward if desired — this backfill only exempts existing content.

### Environment limitation note

Semantic tiling (DragonScale Mechanism 3) could not run: `scripts/tiling-check.py` uses `Path | None` type-hint syntax requiring Python 3.10+, but this environment only has Python 3.9.6 installed (a pre-existing script/environment incompatibility, not a content issue). Additionally, `ollama` is not installed in this environment, which the script also requires. Both are environment-level blockers, not wiki-content issues — flagging for awareness, not fixing (out of scope for a content lint pass).

## Auto-Fixes Applied

- Added 5 orphan source pages to `wiki/sources/_index.md` (safe, mechanical — matches the skill's "safe to auto-fix" criteria for adding missing wikilinks).

## Needs Review (not auto-fixed)

- The 20 pre-existing dead links and 7 frontmatter gaps in meta/reference pages — low severity, unrelated to the Endocrinology domain, left for a future targeted cleanup pass if desired.

## Resolved During This Pass

- DragonScale addressing scope (435 pages) — resolved per user decision; see section above.
