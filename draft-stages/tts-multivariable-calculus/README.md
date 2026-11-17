# Multivariable Calculus from First Principles

A calculation-first and proof-aware bridge from single-variable calculus and basic linear algebra to smooth manifolds, PDEs, optimization and vector calculus. The three existing consolidated manuscripts give the guided survey. Six depth routes, each with four lectures, develop Taylor/Newton theory, nonlinear least squares/inverse problems, constrained Newton/KKT sensitivity, variational weak formulations, nonlinear existence via weak compactness, and mixed finite elements with inf–sup stability, with worked proofs and examples.

## Listening routes

- **Foundations survey** (`multivariable-calculus:survey`): `001000`, `008000`, `015000`; this preserves the three-manuscript entry path.
- **Local Models and Newton Methods** (`multivariable-calculus:taylor-newton-bridge`): `019000`, `020000`, `021000`, `022000`; a worked continuation from second-order calculus to convergence proofs.
- **Nonlinear Least Squares and Inverse Problems** (`multivariable-calculus:nonlinear-least-squares-bridge`): `023000`, `024000`, `025000`, `026000`; connects Gauss–Newton and trust regions to identifiability, uncertainty, regularization and robust fitting.
- **Constrained Newton and Implicit Sensitivity** (`multivariable-calculus:constrained-newton-sensitivity-bridge`): `027000`, `028000`, `029000`, `030000`; derives tangent and critical-cone geometry, KKT Newton block systems, and differentiated optimality conditions.
- **Variational Methods and Weak PDEs** (`multivariable-calculus:variational-weak-formulations-bridge`): `031000`, `032000`, `033000`, `034000`; first and second variations, boundary terms, energy-space existence, and finite-element assembly with a checked error proof.
- **Weak Compactness and Nonlinear Existence** (`multivariable-calculus:variational-compactness-direct-method-bridge`): `035000`–`038000`; weak limits, Sobolev compactness, nonlinear direct-method existence and a solved obstacle free boundary.
- **Mixed Finite Elements and Inf–Sup Stability** (`multivariable-calculus:mixed-inf-sup-stability-bridge`): `039000`–`042000`; mixed flux/temperature variables, saddle-point stability, compatible discrete spaces and Stokes block solvers.
- **Full source sequence** (`multivariable-calculus:main`): all indexed manuscripts in `track.json` order.

The optional `navigation.json` separates introductory listening from depth; it does not replace the full source inventory or imply any proof prerequisites by itself. These are declared separately in each new lecture's `metadata/` sidecar.

## Current manuscripts

Durations below are descriptive measurements of spoken text at 145 words per minute, before synthesis; they are not composition targets.

| ID | Lecture | Approximate minutes | Route |
|---|---|---:|---|
| `001000` | [Local geometry and the total derivative](001000-local-geometry-and-the-total-derivative.md) | 44.9 | Foundations survey |
| `008000` | [Curvature, constrained extrema, and volume integration](008000-curvature-constrained-extrema-and-volume-integration.md) | 43.1 | Foundations survey |
| `015000` | [Integrating over curves, surfaces, and boundaries](015000-integrating-over-curves-surfaces-and-boundaries.md) | 27.4 | Foundations survey |
| `019000` | [Multivariable Taylor Remainders: From a Line to a Reliable Bound](019000-taylor-remainders-from-lines-to-bounds.md) | 12.7 | New local-model bridge |
| `020000` | [Hessian Geometry: Curvature, Convexity, and Conditioning](020000-hessian-geometry-convexity-and-conditioning.md) | 13.3 | New local-model bridge |
| `021000` | [Newton's Method for Systems and Optimization: Building the Step](021000-newton-method-for-systems-and-optimization.md) | 14.0 | New local-model bridge |
| `022000` | [Why Newton Converges: Remainders, Basins, and Safeguards](022000-newton-convergence-bounds-and-globalization.md) | 16.5 | New local-model bridge |
| `023000` | [Nonlinear Least Squares: Residual Geometry and Gauss–Newton](023000-nonlinear-least-squares-and-gauss-newton.md) | 14.1 | Nonlinear least-squares bridge |
| `024000` | [How Far Should We Trust a Fit? Damping and Levenberg–Marquardt](024000-levenberg-marquardt-and-trust-regions.md) | 14.5 | Nonlinear least-squares bridge |
| `025000` | [Can the Data Determine the Parameters? Identifiability and Singular Values](025000-identifiability-singular-values-and-uncertainty.md) | 14.2 | Nonlinear least-squares bridge |
| `026000` | [Inverse Problems: Regularization, Robust Fits, and Responsible Conclusions](026000-regularization-robust-fitting-and-inverse-problems.md) | 16.6 | Nonlinear least-squares bridge |
| `027000` | [Constraints as Geometry: Tangent Spaces and the Hessian of the Lagrangian](027000-tangent-spaces-lagrange-hessians-and-second-order-tests.md) | 12.8 | Constrained Newton/sensitivity bridge |
| `028000` | [Active Inequalities: Feasible Directions, Complementarity, and Critical Cones](028000-active-inequalities-critical-cones-and-regularity.md) | 12.5 | Constrained Newton/sensitivity bridge |
| `029000` | [Constrained Newton Methods: Building and Solving the KKT System](029000-constrained-newton-and-kkt-saddle-systems.md) | 13.4 | Constrained Newton/sensitivity bridge |
| `030000` | [Differentiating an Optimizer: Implicit Functions, Envelope Theorems, and Adjoints](030000-implicit-differentiation-envelope-and-adjoint-sensitivity.md) | 16.1 | Constrained Newton/sensitivity bridge |
| `031000` | [First Variation: Optimizing a Function Instead of a Vector](031000-first-variation-and-energy-minimization.md) | 13.4 | Variational and weak-formulation bridge |
| `032000` | [Euler–Lagrange Equations: The Differential Equation and the Boundary Terms](032000-euler-lagrange-equations-and-boundaries.md) | 13.2 | Variational and weak-formulation bridge |
| `033000` | [Weak Solutions: When the Integral Equation Is the Right Equation](033000-weak-solutions-and-energy-spaces.md) | 14.6 | Variational and weak-formulation bridge |
| `034000` | [Finite Elements: From a Weak Equation to a Matrix and an Error Bound](034000-finite-elements-from-weak-form-to-error.md) | 16.8 | Variational and weak-formulation bridge |

| `035000` | [Weak Convergence: What Survives When Energy Is Bounded](035000-weak-convergence-and-energy-limits.md) | 15.1 | Variational compactness and nonlinear existence bridge |
| `036000` | [Sobolev Embeddings and Compactness: How Slopes Control Shapes](036000-sobolev-embeddings-and-compactness.md) | 16.0 | Variational compactness and nonlinear existence bridge |
| `037000` | [The Direct Method: Proving a Nonlinear Minimizer Exists](037000-direct-method-nonlinear-minimizers.md) | 16.3 | Variational compactness and nonlinear existence bridge |
| `038000` | [Obstacle Problems: From Energy Minima to Variational Inequalities](038000-obstacle-problems-variational-inequalities.md) | 15.9 | Variational compactness and nonlinear existence bridge |

| `039000` | [Mixed Variational Formulations: When One Unknown Is Not Enough](039000-mixed-formulations-fluxes-and-constraints.md) | 12.4 | Mixed FEM and inf–sup stability bridge |
| `040000` | [Saddle-Point Stability: What the Inf–Sup Condition Measures](040000-saddle-point-stability-and-inf-sup.md) | 12.6 | Mixed FEM and inf–sup stability bridge |
| `041000` | [Discrete Inf–Sup: A Two-Cell Failure and a Compatible Repair](041000-discrete-inf-sup-and-compatible-elements.md) | 13.0 | Mixed FEM and inf–sup stability bridge |
| `042000` | [Stokes Flow and Mixed Solvers: Pressure, Blocks, and Reliable Refinement](042000-stokes-block-solvers-and-pressure-stability.md) | 14.4 | Mixed FEM and inf–sup stability bridge |

## Editorial boundaries and evidence

The old combined `001000`, `008000`, and `015000` manuscripts remain unchanged, including their inherited mathematical companions and consolidation provenance. The extensions add quantitative material beyond the original Hessian survey: integral remainder estimates, strong-convexity bounds, Newton convergence, least-squares model geometry, damping safeguards, singular-value sensitivity, structured inverse-problem assumptions, equality and inequality constrained geometry, saddle-point Newton solves, implicit/adjoint sensitivity, weak PDE/finite-element methods, weak compactness, nonlinear variational existence, obstacle variational inequalities, mixed flux methods, discrete inf–sup stability, and Stokes block solvers. Worked examples, derivations and exercises appear in each non-spoken mathematical companion.

`track.json` is the authoritative inventory. Source records live in `metadata/sources.json`; per-lecture citation links, original authorship and teaching prerequisites live in `metadata/*.json`; authorship lineage and editorial changes live in `provenance.yaml`. Consult [`LECTURE_STYLE_RULES.md`](../../LECTURE_STYLE_RULES.md) before further authoring. No runtime pack build or audio synthesis is required for content handoff.
