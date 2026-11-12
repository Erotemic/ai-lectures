# G3 — Audio paper track

G3 is the paper-focused audio course. Its goal is mastery of the Davis–Kahan
journal paper (`aiq-dkps-formalization/papers/dk_formalization_journal/`): the
background constructions, the sine-theta theorem with its exact hypotheses, the
29 Davis–Kahan results, the Proposition 4.4 counterexample and Q-norm repair,
and the real trace-norm matching theorem. G2 is the complete course that skips
nothing; G3 is written for its own audience and does not adapt G2 lectures,
although topics overlap.

The browser exposes the tracks at `/` (G1, Manim), `/audio?track=g2` and
`/audio?track=g3`.

G3 assumes linear algebra, singular values, inner-product notation, and some
comfort with limits and integrals. Hilbert-space and operator-theoretic ideas
are introduced where needed.

## Sequence

`track.json` is the source of order and section membership; the reader and the
course graph follow its list order, not numeric ID order.

| Section | Lectures | Content |
| --- | --- | --- |
| orientation | 000000, 000500 | The problem and the paper; where the constructions come from |
| geometry | 003900, 004000, 004500, 005000, 005500 | Principal angles; angle operators; Halmos form and classification; the direct rotation; nonacute pairs and the squared rotation |
| spectral | 001000, 011000, 003000, 002000 | Exact decompositions; unbounded operators; trial subspaces and residuals; gap geometry |
| norms | 006000, 013000 | Unitarily invariant norms and Ky Fan dominance; operator ideals |
| sylvester | 008000, 009000, 010000, 012000 | Sylvester equation and Theorem 5.1; Theorem 5.2; distance gaps and Theorem 6.2; unbounded identities and cutoffs |
| sine-theta | 020000, 020500, 020700 | The sine-theta theorem; generalizations (Lemmas 6.1–6.2, Proposition 6.1, Theorem 6.1); real and complex scalars |
| tangent-double-angle | 014000, 021000, 016000, 022000, 023000 | Graph subspaces; tangent theorem; branch selection and repulsion (8.1); doubled sine and smallness (8.2); doubled tangent |
| transport | 017000, 018000, 018500, 024000, 025000, 025500, 025700 | Restricted displacement (4.1); basis square sums (4.2); squared displacement and Q-norms (4.3); Proposition 4.4 counterexample; matching theorem and its two-part proof |

## Editorial state

All 32 lectures were rewritten from the mathematics on 12 November 2026
(`draft_status: g3_rewrite`, `source_g2: null`), following
[`../../LECTURE_STYLE_RULES.md`](../../LECTURE_STYLE_RULES.md). There is no
length target. Each file has one spoken region and a display-only companion
with exact statements, worked numbers, and Lean declaration anchors checked
against the pinned Tau Ceti revision and the Davis–Kahan library.

[`PAPER_COVERAGE_PLAN.md`](PAPER_COVERAGE_PLAN.md) maps the paper's content and
the 29 results to lectures, records ID assignments, and lists findings that
need a primary-source check.

Sidecars in `metadata/` anchor historical and source-scope claims to spoken
text, with audit status, and list related reading. Nothing in them is spoken.
Companion slide decks under `companion-slides/` for G3 predate the rewrite and
describe the earlier lectures; decks for retired lectures (007000, 015000,
019000) were removed.

## Checks

```bash
python3 draft-stages/tts-lectures/extract_narration.py --check draft-stages/tts-paper/[0-9]*-*.md
python3 tools/audit_g3_presentation.py
uv run --extra serve --extra test pytest tests/test_audio_course_tracks.py tests/test_g3_presentation_repair.py tests/test_course_graph.py
```

Sidecar anchors are validated with `reference_metadata.validate_lecture` against
the shared catalog `draft-stages/tts-lectures/metadata/sources.json`.
