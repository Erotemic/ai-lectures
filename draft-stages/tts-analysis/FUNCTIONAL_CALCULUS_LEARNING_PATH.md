# Functional calculus: listening path and coverage audit

This is a **foundational bridge** inside *Analysis from First Principles*, not a replacement for the deeper operator-theory and DKPS lectures. The purpose is to make the words “apply a scalar function to an operator” comprehensible before a listener encounters spectral measures, Hamiltonian dynamics, or operator inequalities in a research-level lecture.

## What existed before this continuation

The G2 operator-theory sequence in `draft-stages/tts-lectures/` already has substantial, focused mathematical treatments:

- `025000`, `026000`, `032000`, `034000`: self-adjoint matrices, finite spectral theorem, coordinate-free finite functional calculus, and positive square roots.
- `072000`–`079000`: infinite Hilbert examples, sigma-algebras, integration, continuous calculus, projection-valued measures, scalar spectral measures, multiplication models, and bounded Borel functional calculus.
- `080000`, `080500`, `081000`, `082000`: measurable restrictions, approximate eigenvectors, resolvents, and spectral cutoffs.
- `087000`–`092000`: Cayley transforms, unbounded spectral theorem and domains, reducing domains, Yosida approximations, and one-parameter unitary groups.
- `144000`: stability of functions of operators.

Those lectures provide **depth**. What was missing was a listener-facing bridge in the general analysis course: it reached bounded operators at `038000` and uniform boundedness at `040000` without an introduction to functional calculus as a coherent subject. The new `041000`–`052000` sequence addresses that gap.

## New sequence: three listening stages

### Stage 1: From ordinary linear algebra to spectrum

| Lecture | Starting question | What should become clear |
|---|---|---|
| `041000` — Adjoints | What does moving an operator across an inner product mean? | Adjoint, shift, range/kernel orthogonality, positivity of \(T^*T\) |
| `042000` — Self-adjoint and positive | Which operators behave like real-valued energy measurements? | Quadratic forms, orthogonal eigendirections, square roots, positivity vs matrix entries |
| `043000` — Spectrum and resolvent | How can an operator have spectral values without eigenvectors? | Resolvent, continuous spectrum, approximate eigenvectors, inverse amplification |
| `044000` — Matrix functions | What is the exponential or square root of a matrix? | Spectral projections and finite functional calculus; where Jordan blocks change the answer |

### Stage 2: From discrete eigenvalues to spectral measures

| Lecture | Starting question | What should become clear |
|---|---|---|
| `045000` — Compact and continuous spectrum | Why does an eigenbasis exist for some operators but not others? | Compact diagonal example vs multiplication on an interval |
| `046000` — Continuous calculus | How does uniform polynomial approximation define \(f(A)\)? | Norm formula, completeness, isometric \(*\)-homomorphism, spectral mapping |
| `047000` — Spectral projections | How do we keep a selected part of a spectrum? | PVMs, countable strong additivity, scalar spectral measures, spectral filters |
| `048000` — Borel calculus | How do jumps and indicator functions act on operators? | Simple functions, strong convergence, spectral null sets, essential supremum |

### Stage 3: Domains, non-normal operators, and physical equations

| Lecture | Starting question | What should become clear |
|---|---|---|
| `049000` — Unbounded domains | Why can differentiation be defined for some vectors but not others? | Domains, closed graphs, symmetry vs self-adjointness, graph norms |
| `050000` — Unbounded calculus | How is the domain of \(f(A)\) determined? | The weighted spectral-square-integral test; bounded functions of unbounded operators |
| `051000` — Holomorphic calculus | What if the operator is non-normal? | Cauchy/resolvent contour formula, Jordan derivatives, limitations of spectral norm equality |
| `052000` — Heat, waves, and quantum motion | What is functional calculus used for? | Contractions, unitary groups, wave cosine family, regularity and energy |

## Suggested entry point for a general mathematics listener

Start with `036000` (Hilbert geometry) and `038000` (bounded operators) if these are new. The essential measure background is covered in `029000`–`035000`, though a first listen to `041000`–`046000` does not depend on every technical measure-theoretic proof. Complex integration `013000`–`020000` prepares for `051000` but is not required for the earlier stages.

After the bridge, revisit the more technical G2 operator lectures in this order:

1. `075000` — Continuous functional calculus and C-star identities.
2. `076000`–`079000` — PVMs, scalar spectral measures, multiplication models, bounded Borel calculus.
3. `080500`, `081000`, `082000` — Continuous spectrum, resolvents, and cutoffs.
4. `087000`–`092000` — Unbounded domains, the unbounded theorem, regularization and one-parameter groups.

This is a recommended **conceptual** route. These G2 lectures have their own prerequisites and research-specific objectives; the analysis bridge does not replace them.

## Concept checkpoints, not duration checkpoints

A listener is ready to use functional calculus in a research lecture when they can explain, in ordinary language and with one concrete example, the following distinctions:

- Eigenvalues vs spectrum: multiplication by t on L-two of an interval has a full interval of spectrum but no nonzero eigenvectors.
- Continuous vs Borel calculus: uniform scalar approximation gives norm convergence; bounded pointwise approximation generally gives strong convergence.
- Supremum vs spectral essential supremum: a singleton indicator can give the zero operator even if its point lies in the spectrum.
- Bounded vs unbounded calculus: a scalar function can define an everywhere bounded operator, or an unbounded operator whose domain depends on its growth.
- Symmetric vs self-adjoint: an unbounded differential expression does not fix its domain or self-adjoint extension.
- Self-adjoint vs non-normal: contour calculus can evaluate analytic functions of Jordan blocks, but values on the spectrum alone are insufficient for a general continuous calculus.
- Evolution: \(e^{-tA}\) and \(e^{-itA}\) behave differently because their scalar multipliers have different magnitudes.

If a distinction fails, replay the relevant **example** rather than memorizing an abstract theorem statement first.

## What still needs foundational work

This bridge improves functional-calculus access. It does not make the entire advanced mathematics library fully self-contained. Important follow-up areas include:

- A standalone, complete treatment of **open mapping, closed graph, and bounded inverse theorems**, as well as compact operators and the Fredholm alternative at a slower pace.
- **Fourier transform, convolution, distributions, and Sobolev spaces**, to connect spectral operators rigorously to PDEs.
- **Radon–Nikodym, weak compactness, and the Riesz representation theorem** at the depth needed by later measure and operator theory.
- **C-star and Banach algebras**, including the difference between continuous, measurable and analytic calculi and operator perturbation behavior.
- A prerequisite audit for the algebraic geometry, gauge theory and number theory tracks. Functional calculus alone cannot supply their missing topology, manifolds, cohomology, algebra, or probability.

The next mathematics continuation should be chosen by a **listener-readiness audit** of a selected advanced lecture, not simply by incrementing the advanced topic indexes.
