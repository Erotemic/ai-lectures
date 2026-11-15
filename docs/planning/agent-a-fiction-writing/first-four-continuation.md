# Agent A: first four continuation lectures

**Baseline:** the shared four-agent audio-library overlay over original repository commit `713d5ff`. **Track:** `fiction-writing`. **Delivered in this overlay:** `004000`–`007000` (four new manuscripts) while preserving `001000`–`003000`.

## Decisions

- The pre-existing first three manuscripts remain indexed and unchanged. This batch follows the next four curriculum IDs rather than replacing extant work.
- `004000` distinguishes narrator voice, focalization, distance and unreliability through three viewpoints on one incident.
- `005000` develops *work-level* plot architecture, differentiated from the existing scene-level treatment in `002000`, through the causal and informational timelines of a harbor-bell incident.
- `006000` tests competing reader contracts using three first paragraphs on a common book-return premise, then extends one opening into a causally coherent first scene.
- `007000` builds non-caricatured opposition through an agricultural quarantine dispute. Its explicit distinction between understanding motives and endorsing harms prevents forced moral symmetry.
- Each transcript stands alone, with a sustained original example, a failure case, an alternative model and display-only exercises. Bibliographic connections are recorded by lecture in the track-local metadata. No external quotations from fiction are used.

## Editorial continuation

The next planned batch is `008000`–`011000`: character over time; dialogue as action; subtext outside dialogue; and pacing at the paragraph/scene scale. These will be authored only inside `draft-stages/tts-fiction-writing/`, with any notes here. Preserve manifest IDs and existing manuscripts. Do not edit shared reader code, global planning documents, other agents' tracks, or global tests.

## Validation contract

Use `python tools/apply_track_overlay.py a <zip> --check` and the corresponding apply command; then run `python tools/lecture_inventory.py`. The installer's per-agent namespace check is required before applying any ZIP. The source/manifest counts were computed using `draft-stages/tts-lectures/extract_narration.py`. No audio was generated in this batch.
