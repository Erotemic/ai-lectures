# Independent lecture authoring: four-agent baseline (2026-11-14)

This document is the shared contract for **four agents forked from the same baseline**. No agent needs to edit the audio reader, central track list, global library data, another agent's planning documents, or the same Git files as another agent. Overlays are text-only ZIP files, installed serially into one checkout with `tools/apply_track_overlay.py`.

## Exact ownership

| Agent | Subject | Exclusive lecture directory | Exclusive planning directory | Exclusive tests directory |
| --- | --- | --- | --- | --- |
| A | How to write fiction | `content/fiction-writing/` | `docs/planning/agent-a-fiction-writing/` | `tests/agent-a-fiction-writing/` |
| B | How to write comedy; history/theories of comedy; satire | `content/comedy-history/` | `docs/planning/agent-b-comedy-history/` | `tests/agent-b-comedy-history/` |
| C | Real analysis and complex analysis | `content/analysis/` | `docs/planning/agent-c-analysis/` | `tests/agent-c-analysis/` |
| D | Music theory and composition | `content/music-theory/` | `docs/planning/agent-d-music-theory/` | `tests/agent-d-music-theory/` |

Within their respective lecture directory, agents own lecture `.md` manuscripts, `track.json`, `README.md`, `metadata/sources.json`, `metadata/<id>.json`, and other text-only per-track reference material. They do **not** share or need a global bibliography. Repeated `001000` IDs in different tracks are intentional: every audio request and cache is qualified by track ID.

All paths outside these three namespaces are **read-only for every agent**, especially `dkvis/`, `tools/`, `lectures/`, `AGENTS.md`, `README.md` at repository root, existing global tests, and all other `draft-stages/tts-*` directories. No binary files (including cover art, screenshots, recordings, weights, fonts) in overlays. Do not delete or rename another track's files. Do not create/switch worktrees. Agents should not apply their own patches to the shared checkout; deliver ZIPs only, with no branch-wide Git diff and no installer that performs global search-and-replace.

## Baseline index census

At snapshot `713d5ff`, **461 existing numbered manuscripts** were found across **17 audio tracks**. The four-agent baseline indexes all 461: 156 G2 manuscripts by filename (the G2 directory deliberately has no `track.json`); 305 other manuscripts by 16 per-track manifests, with manifest ordering preserved. The inventory checks spoken-region extraction, recorded word totals, sidecar references, and every track's manuscript-to-manifest correspondence.

Four previously listed `001000` opening lectures are **not present** in the supplied repository snapshot and are therefore *not* treated as playable: `tts-analysis/001000-what-convergence-means.md`, `tts-modern-world/001000-the-world-around-1500.md`, `tts-physical-world/001000-discovering-laws-of-motion.md`, and `tts-numerical-analysis/001000-when-to-trust-a-computed-answer.md`. Their stale manifest rows have been removed (the lesson descriptions remain documented in prior planning materials). Recovery must retrieve the real text or author new lectures, not synthesize placeholder files or falsely count them. Agent C may choose to recreate the analysis opening in its own namespace. The other three tracks are not assigned to these agents.

The audio reader now discovers every `draft-stages/tts-*/track.json` at **service startup**. It verifies that a manifest's `id` matches its directory (`g3` is the `tts-paper` exception), uses the manifest's `title` and `summary`, counts indexed files, and reads them in declared order. The browser builds navigation from `/api/audio-tracks`; no static track-specific button registration remains. **Restart the audio service after installing overlays that create a new track.** Invalid or unindexed content is rejected instead of silently omitted.

## Track content contract

- Each lecture file is named `<six-digit-id>-<slug>.md`; IDs need only be unique **within** a track. A separate per-track `track.json` lists only present manuscripts and their IDs, filenames, titles, sections, and accurate `spoken_words`, in intended listening order. Never list proposed or missing manuscripts as delivered. Plans for future lectures belong under the agent's own planning namespace.
- Every lecture has one `<!-- BEGIN SPOKEN LECTURE -->` and one `<!-- END SPOKEN LECTURE -->` marker. It is understandable on its own when listened to without a previous lecture. Narrative depth takes priority over hitting a rigid duration; avoid slides-only language or raw TeX in the spoken portion. The canonical extractor is `content/g2/extract_narration.py` (shared, read-only).
- References, mathematical examples, composition examples, exercises, annotations, and further reading can live **outside** the spoken markers. References belong in that track's `metadata/sources.json` and per-lecture `metadata/<id>.json`. Reuse source IDs within the track; do not edit the global references.
- Agent D creates `content/music-theory/track.json` with `"id": "music-theory"`, readable `title` and `summary`, and at least one completed lecture before presenting the track as populated. No shared reader changes.
- Agents may work on multiple ZIP overlays over successive turns. Each ZIP must be self-consistent when applied to the baseline plus that agent's earlier ZIPs. The manifest must contain **all** numbered manuscripts in its directory after application. Repeating a path in multiple ZIPs from the **same** agent is permitted and considered an intentional revision, but overlays from **different** agents can never share a path.

## Preflight, installation, and verification

First apply the baseline ZIP in the repository root, before forking the four chats. Review and commit the baseline, and distribute that same commit/archive to each fork. Do not begin work from the original unpatched `713d5ff` snapshot.

```bash
# Run from the repo root, with the baseline ZIP downloaded into ~/Downloads.
unzip -o ~/Downloads/ai-lectures-four-agent-baseline.zip -d .
python tools/lecture_inventory.py
python -m pytest -q tests/test_audio_manifest_discovery.py

git add dkvis/presentation/audio_library.py dkvis/presentation/audio_library.html \
  content/analysis content/modern-world \
  content/physical-world content/numerical-analysis \
  docs/planning/four-agent-lecture-baseline.md tools/apply_track_overlay.py \
  tools/lecture_inventory.py tests/test_audio_manifest_discovery.py \
  tests/test_category_theory_track.py tests/test_foundational_expansion_tracks.py \
  tests/test_math_foundations_tracks.py tests/test_modern_literature_track.py \
  tests/test_world_reconsidered_track.py
# Replace the example co-author identity with your usual author trailer if desired.
git commit -m "Make audio lecture tracks independently discoverable" \
  -m "Co-authored-by: ChatGPT <noreply@openai.com>"
```

For each later agent ZIP, in the shared repository root:

```bash
python tools/apply_track_overlay.py a ~/Downloads/agent-a-overlay.zip --check
python tools/apply_track_overlay.py a ~/Downloads/agent-a-overlay.zip
python tools/lecture_inventory.py
python -m pytest -q tests/test_audio_manifest_discovery.py

git add content/fiction-writing docs/planning/agent-a-fiction-writing tests/agent-a-fiction-writing
git commit -m "Expand fiction-writing lecture track"
```

Replace `a` / file / three staging directories with the matching agent's values (`b`, `c`, or `d`). Missing directories in the `git add` example may be omitted. The installer rejects any cross-track or global edits, directory traversal, symlinks, non-text payloads, duplicate ZIP entries, and an inconsistent merged lecture manifest **before modifying files**. Never `unzip -o` a multi-agent overlay directly over the checkout, since that bypasses the checks. Avoid broad staging such as `git add -A` when working with partially applied agent artifacts. Apply and commit ZIPs **serially** in the same Git checkout; agents themselves need no coordination.

Run `python tools/lecture_inventory.py` for a complete source/index audit. Restart the library service after a newly created track is installed; visit `/audio`, check that all audio track buttons appear, and open `?track=music-theory` once Agent D delivers. If inventory fails, do not commit; have the originating agent repair *its own namespace*. Central reader changes are a separate future maintenance task, not part of these four tracks.

## Copyable fork instructions

Give **each** fork the current baseline commit/archive and this shared document, then append exactly one assignment:

**Agent A:** "Own only fiction-writing. Produce substantive, independently understandable lectures on fiction craft, with a coherent listening sequence covering character, scene, plot, prose, perspective, worldbuilding and revision. Extend `tts-fiction-writing` and only your own planning and tests directories. Deliver text-only ZIP overlays; do not edit shared code, other tracks, or Git worktrees."

**Agent B:** "Own only comedy-history. Develop a deep, source-grounded sequence on the history of comedy across cultures, competing theories of humor, comedy techniques, and satire as art and social criticism. Distinguish evidence from legend and avoid reducing global comedy to a single Western chronology. Extend `tts-comedy-history` and only your own planning and tests directories. Deliver text-only ZIP overlays; do not edit shared code, other tracks, or Git worktrees."

**Agent C:** "Own only analysis. Build rigorous, concept-first real and complex analysis tracks within `tts-analysis` using this track's internal sections, explicit hypotheses, worked mathematical examples and sound proofs. The original `001000` manuscript is absent; recreate it if pedagogically necessary rather than assuming it is available. Own only `tts-analysis` plus your planning and tests directories. Deliver text-only ZIP overlays; do not edit shared code, other tracks, or Git worktrees."

**Agent D:** "Own only music-theory. Introduce music theory through listening, intervals, rhythm and meter, harmony, voice leading, counterpoint, form, composition and orchestration. Explicitly differentiate tuning systems and style-specific conventions; include usable examples in text or display-only notation, not binary music assets. Create the new manifest-backed `tts-music-theory` track and only your own planning and tests directories. Deliver text-only ZIP overlays; do not edit shared code, other tracks, or Git worktrees."
