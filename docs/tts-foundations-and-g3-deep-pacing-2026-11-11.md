# Audio-first foundations and G3 proof-body revision — 11 November 2026

This incremental editorial pass builds on `ai-lectures-tts-mental-model-pacing-2026-11-11.zip`. It changes **22 numbered lectures**: ten foundational G2 recordings and twelve G3 proof-body recordings. It preserves narration/companion boundaries, existing lecture identifiers, theorem statements, source excerpts, reference sidecars, and production code. No slides or audio were rendered.

## G2 foundation improvements

| Recordings | Development added or clarified |
| --- | --- |
| `004000–005000` | Differentiation on polynomials as a linear but unbounded map for the supremum norm; a three-term Neumann approximation with an exact residual and a general operator-norm tail estimate |
| `006000–007000` | A norm-one Hahn–Banach extension that recovers the norm of one chosen vector; explicit complex eigenvectors for a real quarter-turn, with the scalar-extension distinction made audible |
| `033000–034000` | Entrywise positive matrices with negative quadratic directions, and the identity/reflection example showing why positivity selects a unique operator square root even on repeated eigenspaces |
| `035000–036000` | Follow the same rank-one map through surviving and collapsed directions; construct nonzero input/output Gram correspondence and account for the extra zero eigenvalue in a rectangular output space |
| `037000–038000` | Explain the polar factor through its action on the surviving vertical direction; test two different unitary completions on a vector annihilated by the modulus |

The added equations and numerical witnesses are in display-only companions where needed.

## G3 proof-body improvements

| Recordings | Development added or clarified |
| --- | --- |
| `002000–004000` | Signed Sylvester denominators for interlaced spectra; compare Ritz and non-Ritz residuals with their **different** spectral gaps; source-indexed cosine/sine Gram identity checked direction by direction |
| `007000`, `009000` | An invariant but non-reducing triangular operator; interpret the ordered Sylvester integral as simultaneous reciprocal denominators with a uniform slowest decay rate |
| `011000` | Two sequence-space cutoffs that converge in input norm but have different transformed-output behavior; explicit graph-norm tail |
| `015000–016000` | Mirror-conjugation exposes the off-diagonal coupling; replace the infinite-dimensional spectral-repulsion shortcut with its coercivity, closed-range, dense-range, and invertibility steps |
| `017000–019000` | Distinguish the first and second singular-value min–max tests; calculate basis-independent squared escape with a rotated orthonormal basis; explain where unsquared ambient transport acquires independent freedom |
| `022000` | Separate the geometric doubling by reflection from the two-perturbation norm estimate, keeping the branch limitation explicit |

The G3 `track.json` word counts were regenerated from the actual narration extractor. The highest revised G3 count is 1,726 words, within the track's 1,750-word limit.

## Validation

- 76 focused pytest checks passed: audio course tracks, audio library, companion exports, course graph, and G3 presentation repair.
- `tools/audit_g3_presentation.py`: 27 recordings, 0 issues.
- `python -m dkvis.presentation.course_graph`: 211 nodes and 679 typed edges, with all 156 G2 and 27 G3 positions available.
- Independent numerical checks covered positive-matrix spectra, positive square roots, Neumann truncation, real complexification, Sylvester coefficients, Ritz residuals and gaps, one-way invariant blocks, spectral repulsion, and basis-independent escape energy.

## Follow-on review targets

The revisions above target passages where a correct formula needed another mental-model step, rather than applying a uniform expansion to every recording. The remaining early G2 lectures `008000–012000` already contain developed standalone constructions; an additional listener-led pass should be driven by specific feedback on their proof pacing. For G3, `001000`, `005000–006000`, `008000`, `010000`, `012000–014000`, `018500`, `020000–021000`, and `023000–025000` retain their earlier substantive revisions. These were left unchanged here to avoid duplicating explanations that already have worked examples.
