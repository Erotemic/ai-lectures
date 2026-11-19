# Analysis to PDE: listening path and prerequisites audit

This is an auditory-learning route within *Analysis from First Principles*. It does not replace advanced PDE, finite-element or functional-analysis courses. Its central question is: how do abstract statements about operators become rigorous claims about differentiating, smoothing and evolving rough functions?

## Entering the bridge

A listener should know convergence and L-p norms (001000–012000, 029000–037000), the Hilbert-space inner product (036000), and bounded operators and the Baire theorem (038000–040000). Functional calculus (041000–052000) supplies the spectrum, domains and spectral-evolution story, but the Fourier/distribution sequence below can be approached with just Hilbert-space basics.

## Stage A: complete the operator-and-measure prerequisites

- **053000:** Open mapping, closed graph and bounded inverse. Distinguish a bijection from a *stable* bijection. Example: diagonal sequence operator with coefficients `1/n` has an unbounded inverse on its proper range.
- **054000:** Compactness and Fredholm alternative. Example: the constant-function projection makes the equation `(I-P)u=f` solvable precisely for mean-zero forcing.
- **055000:** Radon–Nikodym and the two Riesz representation theorems. Know the difference between a density, an L-two vector, and a point mass.

Checkpoint: Given a proposed inverse and source term, say what the domain and norm are and why a solution is unique, stable, or subject to a compatibility condition.

## Stage B: Fourier and distributional language

- **056000:** Fourier series and convolution; distinguish energy convergence from pointwise convergence, and an approximate identity from a sharp cutoff.
- **057000:** Fourier transforms, Gaussian pulses, Plancherel and the derivative multiplier.
- **058000:** Frequency localization and regularity; explain why `I - d^2/dx^2` gains two weak derivatives on the whole line.
- **059000:** Distributions and delta impulses; derive the distributional derivative of a step.
- **060000:** Mollifiers and weak derivatives; distinguish a corner from a jump in `W^{1,2}`.

Checkpoint: Explain why the Fourier transform of a merely L-two function need not be an ordinary pointwise integral; differentiate a step in distributions; describe the domain of a growing frequency multiplier.

## Stage C: PDEs built from weak derivatives

- **061000:** Sobolev embeddings, traces and compactness. Dimension affects whether integral regularity implies continuity.
- **062000:** Weak Poisson equation and Lax–Milgram. Derive the energy identity for a loaded string and the Neumann compatibility condition.
- **063000:** Elliptic regularity and smoothing. Explain interior versus boundary regularity and how Fourier multiplier estimates gain derivatives.
- **064000:** Strongly continuous semigroups and unbounded generators. Compare translation and heat and distinguish mild from strong solutions.

Checkpoint: Formulate `-u''=1` with Dirichlet data in an H-one test space; explain why heat and translation flows are strongly continuous but have unbounded generators; distinguish existence of a weak solution from extra classical smoothness.

## Why this changes access to advanced lectures

- `content/differential-equations/027000-semilinear-wave-equations-and-local-theory.md` assumes Sobolev spaces, weak PDE solutions, linear propagators, nonlinear product estimates and fixed-point arguments. This bridge covers the first three explicitly. A dedicated nonlinear product/fixed-point lecture remains a gap.
- `content/numerical-analysis/027000-goal-oriented-dual-weighted-residual.md` assumes weak formulations and an adjoint problem. This bridge teaches both at an introductory level, but Galerkin approximation and rigorous output-error bounds still deserve further worked examples.
- Functional-calculus applications in `content/g2/` become easier to connect to concrete differential operators after 057000–064000. The specialized spectral theory remains more detailed.

## Not solved by this bridge

The advanced algebraic geometry, gauge theory and p-adic courses require additional foundations in homological algebra, manifolds, differential forms, cohomology, commutative algebra and number theory. Do not confuse an increase in lecture count with closure of those prerequisites.

Lecture lengths are determined by the teaching, not a runtime target.


## Next available foundations

The continuation 065000–076000 develops Banach/C-star algebras, weak-star compactness, analytic semigroups, Sobolev traces, fractional function spaces, nonlinear products, contraction principles, Duhamel formulas, energy estimates, spacetime compactness and nonlinear variational methods. Continue with [NONLINEAR_PDE_LEARNING_PATH.md](NONLINEAR_PDE_LEARNING_PATH.md). The earlier gap in introductory nonlinear product and fixed-point arguments has been addressed; critical nonlinear PDE theory remains separate.
