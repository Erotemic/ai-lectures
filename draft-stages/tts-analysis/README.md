# Analysis from First Principles

Limits, continuity, completeness, differentiation, integration, function spaces, and rigorous reasoning.

## Available lectures

- 001000 — What Does It Mean for a Sequence to Converge?
- 002000 — The Number Line Without Gaps: Completeness and the Real Numbers
- 003000 — From Nearby Inputs to Nearby Outputs: Limits and Continuity
- 004000 — What Continuity Guarantees: Roots, Bounds, and Extrema
- 005000 — The Derivative as a Local Linear Approximation
- 006000 — The Mean Value Theorem: From Local Slopes to Global Bounds
- 007000 — Building an Integral from Finite Sums
- 008000 — The Fundamental Theorem of Calculus: Recovering Change from Rates

## Sequence and authoring notes

The opening sequence progresses from epsilon-N control of numerical sequences through completeness and Cauchy sequences, then epsilon-delta continuity, then the consequences of continuity on closed real intervals. The 002000 completeness manuscript came from the original source snapshot; the track also includes the restored 001000 and newly authored subsequent lectures.

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

- 009000 — Distance Without Coordinates: Metric Spaces and Completeness
- 010000 — Compactness: Turning Infinite Possibilities into Finite Control
- 011000 — Uniform Convergence: When Limits Preserve Structure
- 012000 — Infinite Sums of Functions: Uniform Series and the First Power Series

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

## Conformal geometry, the Riemann map and boundary behavior (025000–028000)

- 025000 — Möbius Transformations: Moving the Plane Without Tearing Its Angles
- 026000 — Conformal Geometry: Angles, Coordinate Changes, and Hyperbolic Distance
- 027000 — The Riemann Mapping Theorem: A Shape-Free Disk and a Proof by Extremality
- 028000 — Beyond the Riemann Map: Boundaries, Corners, and the Limits of Equivalence

The material derives Möbius and disk automorphism structure, the curvature-minus-one
Poincaré metrics and Schwarz–Pick contraction, the full normalized Riemann mapping
theorem via extremal derivatives and a missed-point square-root contradiction, and
boundary extension under Jordan hypotheses. The last lecture treats slit-boundary
prime ends, Schwarz–Christoffel corner exponents, the transported Poisson solution
to the Dirichlet problem, and the topological/conformal obstructions caused by
annuli. The speaker-facing prose does not assume a screen; exact display-only
mathematics, counterexamples, exercises and references follow each spoken region.
Word counts are catalog metadata, not a length quota. The lecture content determines the duration.

Next possible material: conformal capacity and extremal length, elliptic
functions and doubly connected uniformization, or a return to real-variable
analysis via measure and Lebesgue integration. No planned manuscripts are indexed.

## Editorial review and source verification

See [`polishing-audit-2026-11-14.md`](../../docs/planning/agent-c-analysis/polishing-audit-2026-11-14.md) for the review census, theorem-qualification checks, the fixed open-versus-closed disk exercise, repaired source metadata, and replacement of a broken reference. The complete 28-lecture sequence retains its ID ordering.

## Measure theory and Lebesgue integration (029000–032000)

- 029000 — Sigma-Algebras: What Does It Mean to Measure a Set?
- 030000 — Building Lebesgue Measure: Coverings, Null Sets, and a Necessary Boundary
- 031000 — Measurable Functions: Seeing a Function Through Its Level Sets
- 032000 — The Lebesgue Integral: Building an Area That Survives Limits

The sequence develops a general measurable-space framework, constructs Lebesgue
outer measure and the Carathéodory sigma-algebra, distinguishes Borel sets
from their Lebesgue completion, and derives simple approximations,
almost-everywhere convergence, Egoroff's theorem, monotone convergence,
and Fatou's lemma. Definite failure examples (Vitali selection, nonuniform
function limits, concentrating mass) are retained alongside proof hypotheses.
Source notes link to Axler's open-access textbook, MIT 18.125, Tao's notes,
and selected Wikipedia overviews. Lecture length has no target or threshold;
word counts and estimates are descriptive metadata.

Next: dominated convergence, signed and complex integration, product measures
and Fubini–Tonelli, followed by L-p spaces and Hilbert-space foundations.

## Dominated convergence, product measures, and function spaces (033000–036000)

- 033000 — Dominated Convergence: When Limits May Pass Through Integrals
- 034000 — Fubini and Tonelli: When Two Integrals May Trade Places
- 035000 — Measuring Functions: L-p Spaces, Hölder, and Minkowski
- 036000 — Complete Spaces of Functions: Riesz–Fischer, Hilbert Geometry, and Fourier Projection

This sequence proves DCT via Fatou and L-one convergence, with distinct
concentration and escape-to-infinity counterexamples. Product measure,
Tonelli and Fubini are taught with sigma-finiteness, section measurability,
and a concrete signed-integrand counterexample whose repeated integrals differ.
L-p spaces are defined as almost-everywhere equivalence classes; Hölder,
Minkowski and finite-measure embeddings are proved. Riesz–Fischer completeness
is proved using a summable-difference subsequence, followed by L-two
projection geometry, Bessel's inequality, and an explicit distinction between
metric completeness and spanning completeness of an orthonormal family.

All four have self-contained audio-first narration plus non-spoken proof,
example, exercise, and bibliography companions. Recorded word counts and
estimated durations are descriptive data **only**. No duration or word-count
limits were applied in authoring or validation.

Next possible directions: L-p duality and weak convergence; bounded linear
operators and Hahn–Banach; Fourier convergence and density; convolution and
approximate identities; probability measures and conditional expectation.

## Duality, operators, Hahn–Banach and uniform boundedness (037000–040000)

- 037000 — The Dual View of a Function: Linear Measurements and L-p Duality
- 038000 — Bounded Linear Operators: When Transformations of Functions Are Stable
- 039000 — Hahn–Banach: Extending Measurements and Seeing Weak Convergence
- 040000 — Baire Category and Uniform Boundedness: From Individual Control to a Common Bound

The sequence identifies stable scalar measurements of L-p functions with L-q
weights (under sigma-finiteness and finite p), distinguishes the L-infinity
endpoint, and uses explicit accumulation/differentiation and sequence projection
examples to motivate bounded operator norms. Hahn–Banach is developed through
one-direction extension, Zorn's lemma, norming functionals and weak convergence.
Baire category then yields Banach–Steinhaus, with an explicit noncomplete-domain
counterexample, strong-versus-operator-norm convergence, and boundedness of
weakly convergent sequences. Radon–Nikodym is stated as a named prerequisite
for the L-p representation proof and merits its own later lecture.

Each manuscript has independently understandable spoken narration, a separate
math companion, exercises with solutions, and track-local source metadata.
No runtime or minimum-word target was imposed; manifest counts are descriptive.

Next options: full Radon–Nikodym proof, open mapping and closed graph theorems,
Banach adjoints and reflexivity, weak compactness, compact operators, and
Hilbert-space spectral theory.

## Functional calculus foundation bridge (041000–052000)

A listener-first route from adjoints and spectrum to measurable/unbounded functions of operators, holomorphic contour calculus, and heat/wave/quantum evolution. The new sequence starts with finite matrix examples and multiplication on L-two before presenting the general theorems.

Listening route and remaining prerequisites: [FUNCTIONAL_CALCULUS_LEARNING_PATH.md](FUNCTIONAL_CALCULUS_LEARNING_PATH.md).

- 041000 — [Adjoints: Moving an Operator Across an Inner Product](041000-adjoints-and-inner-product-geometry.md)
- 042000 — [Self-Adjoint and Positive Operators: The Geometry of Energy](042000-positivity-and-self-adjoint-operators.md)
- 043000 — [Spectra and Resolvents: What If an Operator Cannot Be Inverted?](043000-spectrum-resolvents-and-approximate-eigenvectors.md)
- 044000 — [Matrix Functions: Turning Scalar Formulas into Operator Formulas](044000-matrix-functions-from-eigenvectors.md)
- 045000 — [Compact Operators and Continuous Spectrum: Two Ways Infinity Enters](045000-compact-operators-and-continuous-spectrum.md)
- 046000 — [Continuous Functional Calculus: Build the Operator by Approximation](046000-continuous-functional-calculus-from-approximation.md)
- 047000 — [Spectral Projections: Filtering an Operator by Frequency](047000-spectral-projections-as-filters.md)
- 048000 — [Borel Functional Calculus: When a Function Has Jumps](048000-borel-functional-calculus-and-strong-limits.md)
- 049000 — [Unbounded Operators: Why the Domain Is Part of the Definition](049000-unbounded-operators-and-their-domains.md)
- 050000 — [Unbounded Functional Calculus: A Formula with an Input Test](050000-unbounded-functional-calculus-and-spectral-integrals.md)
- 051000 — [Holomorphic Functional Calculus: Cauchy's Formula for Operators](051000-holomorphic-functional-calculus-and-resolvents.md)
- 052000 — [Functional Calculus in Motion: Heat, Waves, and Quantum Evolution](052000-functional-calculus-heat-waves-and-quantum-motion.md)

Spoken narration is independent of visual companions; exact mathematics, exercises, and references are retained after the spoken markers. Counts and estimates are descriptive only.
