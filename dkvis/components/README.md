# Reusable slide components

Lecture content follows [LECTURE_STYLE_RULES.md](../../LECTURE_STYLE_RULES.md).
This guide describes reusable rendering components.

This package owns reusable visual primitives. Topic scenes and numerical examples
live in `dkvis/learning/<topic>/`; transcripts live in numbered `lectures/` folders
indexed by `lectures/index.yaml`. See
`../learning/README.md`. Deck manifests compose those scenes and
`dkvis/presentation/` supplies the shared production pipeline.

The remaining `dkvis.slides_*` modules support the narrated sine-theta lecture.
`common/` contains shared geometry, layout, and readout primitives. Keep reusable
mathematical explanations in topic packages and numerical models separate from
renderers. Unnarrated reference decks are maintained in the `dk` repository.

When migrating a scene, keep its class name stable until the deck manifests have
been deliberately updated.  Prefer extracting shared primitives first, then move
whole conceptual groups.  Do not create `v2`, `final2`, or similar scene names;
use descriptive alternatives when two explanations are worth comparing.

`lean_code.py` renders Lean 4 syntax using the bundled, licensed JuliaMono font
under `fonts/`; no system font installation or rendering-time download is needed.
`LessonLean` shows one checked example per slide, its symbolic formula and scope,
and a separate library-proof highlight. `DKVIS_LEAN_FONT` overrides the font.
Inherited sine-theta scenes retain their existing typography.

`llm_credit.py` supplies the robot/model disclosure for `LessonTitle`. It reads
recorded source attribution rather than claiming the current renderer authored
the lecture. Known model/configuration names remain visible; unknown variants
are stated as unrecorded. Covers use the existing vector robot asset so they do
not depend on an emoji font.
