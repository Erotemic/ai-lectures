# TTS listening polish: two-projection geometry and singular-value reasoning

11 November 2026. Incremental pass following `ai-lectures-tts-foundations-g3-deep-pacing-2026-11-11.zip`. The changes cover **13 lecture narrations** (10 G2 and 3 G3) and update G3 extracted word-count metadata. The existing lecture order, reference sidecars, theorem statements, Lean source excerpts, and production code are retained.

## G2: geometry before operator algebra

- `046000`: Show the commutation of `(P-Q)^2` with both projections rather than merely announcing it; use nested subspaces to distinguish the ambient sine operator from the directed source-side sine. Companion gives explicit matrices.
- `047000`: Construct a preimage under projection from the bounded inverse of `(PQP)|_U`; illustrate why graph slopes diverge as cosines approach zero. Companion records the inverse formula.
- `048000`: Relate the norm identity of the Sz.-Nagy–Kato intermediary to a sixty-degree plane before applying polar decomposition.
- `050000`: Explain why the kernel of the projection-based intermediary consists exactly of the crossed defects; distinguish the skew quarter-turn from a reflection.
- `051000`: Slow the compactness-to-eigenvector step and conclude with the contrast between compact eigenvalue lists and continuous-spectrum multiplication operators.

## G2: dimension arguments and cumulative singular-value comparisons

- `052000`: Make the min–max intersection argument tangible in three dimensions and distinguish the two quantifier orders.
- `053000`: Interpret the Frobenius lower bound as a finite-dimensional output-space capacity allocation, with the same `diag(5,2,1)` example used for both norms.
- `054000`: Work the orthonormal-frame maximum for `diag(5,2)` before passing to arbitrary singular bases. Companion checks the `7/2` one-direction pairing.
- `055000`: Give an audible running-total interpretation of weak majorization, then connect prefixes, decreasing weights and transfers.
- `056000`: Work explicit sign-flip averages for shrinking coordinates from 4 to 3 and 2 to 1. Companion gives the averaging weights.

Several exercise-list endings were replaced by short conclusions that return to the developed mathematical example.

## G3: compact proof-body explanations

- `006000`: Explain *why* weak-majorization control passes to a convex symmetric gauge before applying the matrix-norm triangle inequality; remove repeated signposting.
- `008000`: Replace a future-tense promise with an actual interlaced two-by-two Sylvester calculation, showing all four denominators and the Frobenius estimate. Companion contains the matrix equations.
- `023000`: Make the reflected-form/semigroup argument audible by relating the sign of the quadratic form to the selected upper spectral branch before the tangent denominator appears.

## Validation

- All 156 G2 and 27 G3 narrations extracted successfully.
- G3 audit: 27 lectures, zero issues, each at most 1,750 extracted words.
- Focused pytest regression: 76 passed (audio course tracks, audio library, course graph, companion export, G3 presentation audit).
- Independent numerical checks: Sylvester residual and Frobenius cost, nested projection operators, graph-coordinate inverse, orthonormal pairing, signed averaging.
- No audio synthesis, video/slide rendering, new tests, or production-tool changes.

## Continuing editorial judgment

The next review should prioritize a listener's actual feedback about confusing transitions rather than expanding every lecture uniformly. The nearby G2 direct-rotation lecture `049000` and G3 canonical-rotation lecture `005000` already have full worked narratives and were intentionally left unchanged in this pass.
