# From functional calculus to nonlinear PDE: listening route

This path builds on **Analysis from First Principles** and connects the preceding bridge (053000–064000) to the advanced PDE and numerical-analysis courses. It is a set of prerequisite checkpoints, not a claim that every nonlinear PDE can now be followed without additional theory.

## Before starting

Review convergence and completeness (001000–012000), measure and L-p norms (029000–037000), operator spectra and self-adjoint functional calculus (041000–052000), Fourier/distribution methods (056000–060000), Sobolev spaces (061000), weak Poisson equations (062000), and semigroups (064000). Different stages need different subsets; listeners can return to these as a concrete example demands.

## Stage A — operators, weak limits, and boundary conditions (065000–068000)

- **065000, Banach and C-star algebras:** Why functional calculus works for bounded normal operators. Check: distinguish C(K) from the whole noncommutative B(H) and explain why continuous calculus is not the same as arbitrary Borel calculus.
- **066000, weak/weak-star compactness:** Why bounded sequences of approximate solutions can have useful limits without norm convergence. Check: prove unit coordinate vectors converge weakly to zero in l-two but not strongly.
- **067000, analytic semigroups:** Why heat smooths while translation does not. Check: calculate the maximum of s exp(-ts), explain the unbounded generator, and identify the role of the resolvent.
- **068000, boundary traces:** What a Dirichlet or Neumann condition means for an H-one solution. Check: analyze the shrinking triangular boundary spike and the derivative-energy cost.

## Stage B — scales and nonlinear products (069000–071000)

- **069000:** Fractional Sobolev norms, dyadic frequencies and why half a derivative has a meaning independent of classical pointwise differentiability.
- **070000:** Interpolate between integrability estimates; distinguish estimates for a function from estimates for an operator.
- **071000:** Show H-one on a bounded interval is a multiplication algebra, and explain the exact failure of that argument in higher dimensions.

Checkpoint: Decide whether u cubed lies in H-one or L-two for a given dimension, rather than treating products of Sobolev functions as automatically legal.

## Stage C — existence, uniqueness, evolution (072000–076000)

- **072000:** Build a contraction for u'=u² and state why its interval must be short.
- **073000:** Derive Duhamel's formula and use the heat semigroup to solve a quadratic reaction equation locally; distinguish mild and classical solutions.
- **074000:** Derive energy dissipation and Gronwall uniqueness for heat with a bounded reaction coefficient.
- **075000:** Use spatial compactness and a weak time derivative bound to obtain strong spacetime convergence by Aubin–Lions.
- **076000:** Obtain a nonlinear elliptic solution by minimizing a coercive convex energy and prove uniqueness by monotonicity.

Checkpoint: Given a nonlinear PDE, say whether a contraction, an energy estimate, a compactness limit, or a variational minimizer is doing the essential work, and state its assumptions.

## Connection to advanced courses

- `draft-stages/tts-differential-equations/027000-semilinear-wave-equations-and-local-theory.md`: 071000–074000 supply an introductory nonlinear-estimate and contraction route, but wave Strichartz and critical-index estimates require additional harmonic analysis.
- `draft-stages/tts-differential-equations/029000-strichartz-estimates-and-endpoint-failures.md`: 069000–070000 supply frequency and interpolation vocabulary, not an entire proof of endpoint Strichartz bounds.
- `draft-stages/tts-numerical-analysis/027000-goal-oriented-dual-weighted-residual.md`: 062000 and 074000–076000 supply energy and weak-compactness language, but a separate first Galerkin example is still a priority.

## Further work

A geometry/manifold/differential-forms foundation path is still missing for gauge and four-manifold courses. The algebraic geometry, homological algebra and p-adic courses need their own foundations rather than pretending that further functional analysis is sufficient.

The duration of each lecture is set by what is needed to explain it well; estimates in catalog metadata are not targets.
