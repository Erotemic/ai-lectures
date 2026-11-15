# Four-agent completion campaign — 15 November 2026

**Baseline:** November 15 snapshot `c3d362d`, with the manifest repair and expanded ownership installer in the same coordinator patch as this document. This is a handoff plan for **continuing existing lecture tracks**, not launching more tracks or imposing a quota of lectures.

## The regression and its disposition

The comedy-history `track.json` advertised manuscripts `050000–053000`, but none of their `.md` files or `metadata/<id>.json` sidecars exists in the supplied snapshot. The `047c759` commit added the manifest rows while only committing `054000–057000`. Those latter four manuscripts are present and should be kept. The coordinator repair unindexes the four missing items and converts their broken README links into a visible Agent B recovery backlog. There is no placeholder text and no invented word counts. **Agent B is responsible for recovering or writing the actual four lectures** and may reindex them only when they are complete and source-backed.

Three one-lecture tracks (`modern-world`, `numerical-analysis`, `physical-world`) each have a playable `002000` but no `001000` in the snapshot. Their owners must decide whether authentic `001000` content can be recovered; otherwise they should write an introduction that complements rather than duplicates `002000`. A number being absent is a backlog item, **not** permission to add a ghost row.

## Census and exclusive ownership

Counts are the **existing playable manuscripts before new authoring**, not estimates of course completeness. The original G2 and G3 tracks are assigned to Agent C for **content stewardship only** but remain read-only for ordinary overlays because G2 contains shared extraction code and G3 is tied to the DKPS paper.

| Owner | Track (stable ID) | Existing | Next responsibility |
| --- | --- | ---: | --- |
| A | `fiction-writing` | 44 | Maintain and audit; deeper additions after smaller tracks |
| A | `modern-literature` | 9 | Broaden twentieth-century geographic and linguistic coverage |
| A | `world-reconsidered` | 12 | Assess conceptual gaps and add synthesis only where needed |
| B | `comedy-history` | 30 | **Recover/write 050000–053000**; preserve 054000–057000 |
| B | `modern-world` | 1 | **Reintroduce 001000**, then build connected history since 1500 |
| B | `history` | 50 | Historical/math-portrait corrections, documented human context |
| B | `world-history` | 110 | Evidence and coverage review, fill actual omissions selectively |
| C | `numerical-analysis` | 1 | **Reintroduce 001000**, then build reliability/stability sequence |
| C | `logic-types` | 4 | Extend proof-theory and type-theory foundations |
| C | `optimization-duality` | 4 | Extend convex analysis and numerical optimization |
| C | `probability-measure` | 12 | Finish decision theory, formal foundations and stochastic processes |
| C | `analysis` | 40 | Maintain prerequisite and proof continuity; gaps only |
| C | `category-theory` | 35 | Audit a long and advanced sequence; bridge foundational gaps |
| C | `g2` | 156 | Stewardship only, coordinator approval for any modifications |
| C | `g3` | 32 | Stewardship only, coordinator approval for any modifications |
| D | `physical-world` | 1 | **Reintroduce 001000**, then build core physics sequence |
| D | `music-theory` | 12 | Advance composition, counterpoint, form, style and listening |
| D | `deep-time` | 36 | Preserve evidence-based reconstruction; audit coverage |

**Totals:** A 65, B 191, C 284, D 49 = **589 manuscripts in 18 tracks**. Workload is allocated by **deficit**, not by these historical totals. Agents B/C/D each have one almost empty track, while A's most useful expansion is the nine-lecture twentieth-century literature track. The first wave therefore does not focus on fiction (44), analysis (40), world history (110), G2 (156), or G3 (32).

## Priority ordering

1. **Repair missing indexed material without inventing completion.** B owns comedy 050000–053000. Already repaired at the coordinator level: manifests now reflect only playable content.
2. **Restore introductions to existing tracks with only 002000 present.** B: `modern-world/001000`; C: `numerical-analysis/001000`; D: `physical-world/001000`. Integrate with existing `002000`, not overwrite it.
3. **Build their first coherent conceptual arcs.** B: early-modern global history; C: numerical conditioning, stable methods, error certificates; D: thermodynamics, fields, waves. A: wider literary geography and divergent narrative forms in twentieth-century works.
4. **Complete partially developed foundations.** C: `logic-types` and `optimization-duality` (four each), then `probability-measure` (twelve, with 013000–015000 outlined in planning); D: music composition practice beyond the initial twelve; A: `world-reconsidered` cross-concept synthesis; B: historical comedy gaps 007000–030000, only after missing 050000–053000.
5. **Curate the large collections, rather than growing them by inertia.** A fiction 44; B mathematical portraits 50 and world history 110; C analysis 40, category theory 35, G2/G3; D deep time 36. Use audits and gap-directed additions, not arbitrary numerical targets.

## What “complete enough” means

Completeness is a **coverage and comprehension judgment**, not a lecture-number quota, word target or mandated format. A track is a good stopping point when its central conceptual arc is coherent; the difficult transitions, counterexamples and competing perspectives are actually taught; there is a usable starting point; key topics have enough substance to stand alone; major historical or technical assertions are supported; source and metadata references resolve; and the audio reader can load everything indexed. A track can remain open for new questions after reaching that state.

A missing or lost **track** (not just a lecture) is to be assigned to its owner for reintroduction with its manifest, manuscripts, source catalog and sidecars. It must not be reintroduced by editing a shared registry alone. A missing lecture is likewise assigned to its track owner. Search supplied Git history and available prior source first; if unavailable, clearly label new work as a new composition, not as a recovered original.

## Hard ownership boundaries

The revised `tools/apply_track_overlay.py` accepts only each owner's assigned **manifest-backed** `draft-stages/tts-<track>/` roots, plus `docs/planning/agent-<letter>-<track>/` and `tests/agent-<letter>-<track>/` for those tracks. It preflights every touched track's merged manuscript set and manifest **before writing**. There are no overlapping writable roots.

- **A:** `fiction-writing`, `modern-literature`, `world-reconsidered`.
- **B:** `comedy-history`, `modern-world`, `history`, `world-history`.
- **C:** `analysis`, `category-theory`, `logic-types`, `numerical-analysis`, `optimization-duality`, `probability-measure`. G2/G3 review only in the first wave.
- **D:** `music-theory`, `physical-world`, `deep-time`.

No agent may modify the root planning document, shared tools, `LECTURE_STYLE_RULES.md`, `AGENTS.md`, central `tests/`, audio reader/UI, TTS configuration, shared source assets, or another agent's course. Agent C must not modify `draft-stages/tts-lectures/` or `draft-stages/tts-paper/` without a separately approved coordinator patch. No worktrees. All ZIP overlays are text only; never bundle binary media or images unless separately requested.

The materials **determine their own form and length**. Dialogue, humor, first-person voice, literary experiment, quotation (within rights), mathematics, and difficult nuance are legitimate when useful. Do not add stylistic quotas, banned words, mandatory scene structure, required bibliography counts, or automatic “literary quality” tests. Use technical verification for real invariants only.

## Batch and merge protocol

1. **Coordinator first:** Apply this repair to the frozen base checkout, verify inventory and reader tests, then commit once. Distribute that *same fixed source snapshot* and the matching per-agent handoff files to all four forks. Stop using their older snapshots as a source of shared indexes.
2. **Agents independently:** Read their assigned existing manifests, manuscripts, planning, and sidecars. Select the next genuine gap. Write original standalone narration, display-only companions when useful, and source-specific metadata. Update only indexes in their own tracks. Do not edit shared code or use another agent's artifacts.
3. **Deliverables:** Each batch is a **ZIP overlay**, with exact `unzip`/preflight/apply commands and exact `git add`/`git commit --only` commands. Deliver a concise coverage update (what gap is now closed and what still remains). Do not assert that audio was generated unless it was. Avoid long repetitive test suites or test-count targets.
4. **Coordinator integrates serially in one shared checkout:** `python tools/apply_track_overlay.py <agent> ZIP --check`, then apply, run `python tools/lecture_inventory.py`, run the relevant audio tests, stage only the ZIP's files, and commit with the co-author trailer. If any check fails, **stop and return the ZIP to its owner**; do not work around a failure with direct `unzip` into the checkout or bulk staging.
5. **Source of truth:** The file system + manifest and the output of `lecture_inventory.py`. A planned title in documentation does not make a lecture playable. Keep distinct `track.json` per track, and don't manufacture missing work to make the count round.

Example single-agent integration (for a ZIP that contains only files, no directory entries):

```bash
cd ~/code/ai-lectures
ZIP="$HOME/Downloads/agent-b-example.zip"
REVIEW=$(mktemp -d)
unzip -o "$ZIP" -d "$REVIEW"
python tools/apply_track_overlay.py b "$ZIP" --check
python tools/apply_track_overlay.py b "$ZIP"
python tools/lecture_inventory.py
python -m pytest -q tests/test_audio_course_tracks.py tests/test_audio_lecture_library.py tests/test_audio_manifest_discovery.py
mapfile -t FILES < <(unzip -Z1 "$ZIP")
git add -- "${FILES[@]}"
git diff --cached --stat -- "${FILES[@]}"
git commit --only -m "Extend assigned lectures" -m "Co-authored-by: ChatGPT <noreply@openai.com>" -- "${FILES[@]}"
```

## Ready-to-send prompts

See `docs/planning/agent-handoffs/agent-a.md` through `agent-d.md`. They are deliberately self-contained because each agent was forked before this reassignment. Supply the **post-repair** archive when restarting each fork. Every prompt contains ownership roots, first tasks, next tasks, prohibited edits, acceptance rules and ZIP handoff instructions.
