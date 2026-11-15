# Analysis from First Principles

Limits, continuity, completeness, differentiation, integration, function spaces, and rigorous reasoning.

## Available lectures

- 001000 — What Does It Mean for a Sequence to Converge? (1,855 spoken words; about 12.8 minutes at 145 wpm)
- 002000 — The Number Line Without Gaps: Completeness and the Real Numbers (3,231 spoken words; about 22.3 minutes at 145 wpm)
- 003000 — From Nearby Inputs to Nearby Outputs: Limits and Continuity (1,919 spoken words; about 13.2 minutes at 145 wpm)
- 004000 — What Continuity Guarantees: Roots, Bounds, and Extrema (2,077 spoken words; about 14.3 minutes at 145 wpm)
- 005000 — The Derivative as a Local Linear Approximation (1,902 spoken words; about 13.1 minutes at 145 wpm)
- 006000 — The Mean Value Theorem: From Local Slopes to Global Bounds (1,987 spoken words; about 13.7 minutes at 145 wpm)
- 007000 — Building an Integral from Finite Sums (2,010 spoken words; about 13.9 minutes at 145 wpm)
- 008000 — The Fundamental Theorem of Calculus: Recovering Change from Rates (2,019 spoken words; about 13.9 minutes at 145 wpm)

## Sequence and authoring notes

The opening sequence progresses from epsilon-N control of numerical sequences through completeness and Cauchy sequences, then epsilon-delta continuity, then the consequences of continuity on closed real intervals. The 002000 completeness manuscript is retained intact from the source snapshot; this overlay restores the missing 001000 manuscript and adds 003000 and 004000.

Audio extraction uses the single `BEGIN SPOKEN LECTURE` / `END SPOKEN LECTURE` marker pair in each manuscript. Exact equations, proofs, references, and exercises remain available outside the spoken markers in display-only companions.

Every numbered manuscript is indexed in `track.json`; each lecture has a per-lecture `metadata/<id>.json` and all source IDs resolve through `metadata/sources.json`. Section labels are internal to this track and do not require central reader changes.

The earlier planning discussion is in `docs/planning/foundational-curriculum-expansion-batch2.md` (read-only to Agent C).

## Continuation through integration

Lectures 005000–008000 cover the derivative as an exact first-order linear model,
Rolle's theorem and the Mean Value Theorem, tagged Riemann sums and Darboux
integrability, and both forms of the Fundamental Theorem of Calculus. Each
manuscript includes a display-only mathematical companion and per-lecture
references; spoken regions avoid symbolic TeX and cross-episode chronology.
The manifest includes only present manuscripts.

## Metric spaces and function limits (lectures 009000–012000)

- 009000 — Distance Without Coordinates: Metric Spaces and Completeness (1,978 spoken words; about 13.6 minutes at 145 wpm)
- 010000 — Compactness: Turning Infinite Possibilities into Finite Control (1,927 spoken words; about 13.3 minutes at 145 wpm)
- 011000 — Uniform Convergence: When Limits Preserve Structure (1,898 spoken words; about 13.1 minutes at 145 wpm)
- 012000 — Infinite Sums of Functions: Uniform Series and the First Power Series (2,070 spoken words; about 14.3 minutes at 145 wpm)

The sequence establishes metric-space completeness, compactness in equivalent metric formulations, uniform convergence with its limit-exchange hypotheses, and the M-test with closed-subdisk power-series control. The next step is complex differentiation and Cauchy–Riemann geometry.

## Complex analysis foundations (lectures 013000–016000)

- 013000 — The Complex Plane: Algebra, Geometry, and Limits
- 014000 — Complex Differentiation and the Cauchy–Riemann Equations
- 015000 — Integrating Along Curves: Contours, Primitives, and Holes
- 016000 — Cauchy's Theorem and Integral Formula: How a Boundary Controls the Interior

The lectures move from complex arithmetic and planar topology through the
complex derivative and its correct Cauchy–Riemann hypotheses, to contour
integration and its dependence on the path, then to Goursat's theorem, Cauchy's
integral formula, Taylor expansions, Cauchy's estimates, Liouville, and the
Fundamental Theorem of Algebra. Formal companions include statements, proof
details, failure cases, and worked exercises. Theorem scope (holomorphic
interiors, domain geometry, orientation) is part of the exposition.

**Length policy:** The `estimated_minutes_at_145_wpm` and `spoken_words`
fields are descriptive catalog metadata, not target values or acceptance
thresholds. Choose the content, proof depth, and examples required for
understanding; do not truncate or pad to meet any runtime or word-count rule.
The track's validation checks exact catalog/prose consistency, not length.

## Complex continuation and residue theory (017000–020000)

- 017000 — Power Series, Isolated Zeros, and Analytic Continuation
- 018000 — Laurent Series and Isolated Singularities: The Anatomy of a Missing Point
- 019000 — The Residue Theorem: One Coefficient Controls an Entire Contour
- 020000 — Counting Invisible Roots: The Argument Principle and Rouché's Theorem

This batch develops local analytic uniqueness, annular Laurent coefficients and
isolated singularity classification, contour residues and worked real-integral
estimates, and zero counts via logarithmic derivatives and strict Rouché
inequalities. Exact formulas and exercises are in nonspoken companions.
Lecture length is determined by mathematical teaching needs, without a runtime
or word-count target. The metadata records observed word counts, not quotas.
The next topics may include maximum modulus, open mapping, Schwarz lemma,
normal families, harmonic functions, and selected applications.

## Boundary rigidity, harmonicity, and compactness (021000–024000)

- 021000 — The Maximum Modulus Principle: Why the Interior Cannot Hide a Peak
- 022000 — The Open Mapping Theorem and Schwarz's Lemma: Two Forms of Rigidity
- 023000 — Harmonic Functions: A Value Determined by Its Neighbors
- 024000 — Normal Families: Finding Convergent Functions in an Infinite Collection

The lectures use local maximum-modulus rigidity to explain compact-boundary
bounds, Rouché zero-counting to prove openness even at branch points, and
disk automorphisms to obtain Schwarz–Pick. Harmonic conjugates, the Poisson
formula, and punctured-plane periods distinguish local PDE constraints from
global topology. Montel compactness leads to Hurwitz zero-stability and
Vitali convergence, with finite-valued versus spherical normal-family
conventions explained. Each lesson has a proof-and-exercise companion and
track-local references. No lecture duration or word-count threshold is used.
