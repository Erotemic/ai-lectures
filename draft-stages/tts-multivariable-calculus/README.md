# Multivariable Calculus from First Principles

A calculation-first and proof-aware bridge from single-variable calculus and basic linear algebra to smooth manifolds, PDEs, optimization and vector calculus. The three existing consolidated manuscripts give the guided survey. Eleven depth routes, each with four lectures, develop Taylor/Newton theory, nonlinear least squares/inverse problems, constrained Newton/KKT sensitivity, variational weak formulations, nonlinear existence via weak compactness, mixed finite elements with inf–sup stability, and elliptic boundary-value theory, qualitative principles, harmonic measure, Hölder versus L-p regularity, boundary Harnack, capacity, removable sets and the Wiener test, followed by semilinear energy methods, monotone iteration, positive-solution thresholds and bifurcation, with worked proofs and examples.

## Listening routes

- **Foundations survey** (`multivariable-calculus:survey`): `001000`, `008000`, `015000`; this preserves the three-manuscript entry path.
- **Local Models and Newton Methods** (`multivariable-calculus:taylor-newton-bridge`): `019000`, `020000`, `021000`, `022000`; a worked continuation from second-order calculus to convergence proofs.
- **Nonlinear Least Squares and Inverse Problems** (`multivariable-calculus:nonlinear-least-squares-bridge`): `023000`, `024000`, `025000`, `026000`; connects Gauss–Newton and trust regions to identifiability, uncertainty, regularization and robust fitting.
- **Constrained Newton and Implicit Sensitivity** (`multivariable-calculus:constrained-newton-sensitivity-bridge`): `027000`, `028000`, `029000`, `030000`; derives tangent and critical-cone geometry, KKT Newton block systems, and differentiated optimality conditions.
- **Variational Methods and Weak PDEs** (`multivariable-calculus:variational-weak-formulations-bridge`): `031000`, `032000`, `033000`, `034000`; first and second variations, boundary terms, energy-space existence, and finite-element assembly with a checked error proof.
- **Weak Compactness and Nonlinear Existence** (`multivariable-calculus:variational-compactness-direct-method-bridge`): `035000`–`038000`; weak limits, Sobolev compactness, nonlinear direct-method existence and a solved obstacle free boundary.
- **Mixed Finite Elements and Inf–Sup Stability** (`multivariable-calculus:mixed-inf-sup-stability-bridge`): `039000`–`042000`; mixed flux/temperature variables, saddle-point stability, compatible discrete spaces and Stokes block solvers.
- **Traces and Elliptic Regularity** (`multivariable-calculus:boundary-traces-elliptic-regularity-bridge`): `043000`–`046000`; Dirichlet lifting, Neumann/Robin boundary conditions, interior H-two smoothing, and reentrant-corner FEM error limits.
- **Elliptic Principles and Estimates** (`multivariable-calculus:elliptic-maximum-green-harnack-bridge`): `047000`–`050000`; weak comparison and barriers, the interval Green kernel, localized Caccioppoli energy estimates, and sharp disk Harnack bounds.
- **Boundary Behavior and Regularity** (`multivariable-calculus:elliptic-boundary-harmonic-regularity-bridge`): `051000`–`054000`; Hopf barriers, harmonic measure, Schauder Hölder estimates, and Calderón–Zygmund L-p theory.
- **Boundary Harnack, Capacity and Wiener Regularity** (`multivariable-calculus:elliptic-boundary-capacity-wiener-bridge`): `055000`–`058000`; relative boundary decay, energy capacity, polar/removable sets and pointwise Dirichlet regularity.
- **Semilinear Existence and Bifurcation** (`multivariable-calculus:semilinear-existence-bifurcation-bridge`): `059000`–`062000`; nonlinear weak energy and existence, ordered barriers with shifted iteration, first-eigenvalue positive-solution threshold, and pitchfork/fold branch continuation.
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

| `043000` | [Traces and Boundary Data: How an Energy Solution Meets the Edge](043000-traces-boundary-data-and-dirichlet-lifting.md) | 13.0 | Elliptic traces and regularity bridge |
| `044000` | [Neumann and Robin Problems: Boundary Flux, Compatibility, and Uniqueness](044000-neumann-robin-compatibility-and-boundary-forms.md) | 13.2 | Elliptic traces and regularity bridge |
| `045000` | [Elliptic Regularity: Why a Weak Solution Can Have More Derivatives](045000-elliptic-regularity-difference-quotients-and-h2.md) | 14.3 | Elliptic traces and regularity bridge |
| `046000` | [Corners and Singularities: When a Valid Solution Defeats a High-Order Error Bound](046000-corner-singularities-regularity-and-mesh-error.md) | 14.2 | Elliptic traces and regularity bridge |

| `047000` | [Maximum Principles: Comparison, Positivity, and Barriers](047000-maximum-principles-comparison-and-barriers.md) | 13.1 | Elliptic principles and estimates bridge |
| `048000` | [Green's Functions: An Elliptic Equation as an Integral Operator](048000-green-functions-and-inverse-operators.md) | 13.1 | Elliptic principles and estimates bridge |
| `049000` | [Elliptic Energy Estimates: From Global Stability to Caccioppoli](049000-energy-estimates-and-caccioppoli.md) | 15.3 | Elliptic principles and estimates bridge |
| `050000` | [Mean Values and Harnack: From Averages to Pointwise Bounds](050000-mean-value-harnack-and-interior-bounds.md) | 17.0 | Elliptic principles and estimates bridge |

| `051000` | [Hopf's Boundary Lemma: Why a Positive Solution Cannot Touch Flatly](051000-hopf-boundary-lemma-and-nonflat-contact.md) | 12.5 | Boundary behavior and regularity bridge |
| `052000` | [Harmonic Measure: Which Part of the Boundary Matters?](052000-harmonic-measure-boundary-data-and-brownian-exit.md) | 12.8 | Boundary behavior and regularity bridge |
| `053000` | [Schauder Estimates: How Smooth Data Become Smooth Derivatives](053000-schauder-estimates-and-holder-regularity.md) | 12.5 | Boundary behavior and regularity bridge |
| `054000` | [Calderón–Zygmund: Second Derivatives When the Source Is Only Integrable](054000-calderon-zygmund-w2p-and-endpoint-failures.md) | 14.4 | Boundary behavior and regularity bridge |

| `055000` | [Boundary Harnack: Comparing Two Functions That Both Vanish at a Wall](055000-boundary-harnack-and-relative-boundary-growth.md) | 11.9 | Boundary capacity and Wiener bridge |
| `056000` | [Capacity: When a Small Set Still Has a Large Effect](056000-capacity-energy-and-the-size-of-a-set.md) | 12.9 | Boundary capacity and Wiener bridge |
| `057000` | [Removable Singularities: When a Missing Set Can Be Filled In](057000-removable-singularities-and-polar-sets.md) | 12.3 | Boundary capacity and Wiener bridge |
| `058000` | [The Wiener Criterion: When a Boundary Point Cannot Enforce Its Value](058000-wiener-criterion-and-irregular-boundaries.md) | 13.6 | Boundary capacity and Wiener bridge |

| ID | Lecture | Approximate minutes | Route |
|---|---|---:|---|
| `059000` | [Semilinear Elliptic Equations: When the Source Depends on the Solution](059000-semilinear-elliptic-equations-and-energy.md) | 11.9 | Semilinear existence and bifurcation bridge |
| `060000` | [Subsolutions and Supersolutions: Constructing a Nonlinear Solution Between Barriers](060000-subsolutions-supersolutions-and-monotone-iteration.md) | 12.2 | Semilinear existence and bifurcation bridge |
| `061000` | [Positive Solutions and Principal Eigenvalues: When a Nonlinear State Can Exist](061000-positive-solutions-and-principal-eigenvalue-thresholds.md) | 12.4 | Semilinear existence and bifurcation bridge |
| `062000` | [Bifurcation and Continuation: Following Nonlinear Solutions Through Singular Jacobians](062000-bifurcation-linearization-and-continuation.md) | 12.5 | Semilinear existence and bifurcation bridge |

## Editorial boundaries and evidence

The old combined `001000`, `008000`, and `015000` manuscripts remain unchanged, including their inherited mathematical companions and consolidation provenance. The extensions add quantitative material beyond the original Hessian survey: integral remainder estimates, strong-convexity bounds, Newton convergence, least-squares model geometry, damping safeguards, singular-value sensitivity, structured inverse-problem assumptions, equality and inequality constrained geometry, saddle-point Newton solves, implicit/adjoint sensitivity, weak PDE/finite-element methods, weak compactness, nonlinear variational existence, obstacle variational inequalities, mixed flux methods, discrete inf–sup stability, Stokes block solvers, trace lifting, Neumann/Robin compatibility, H-two regularity, and corner-dependent FEM error, elliptic comparison and barriers, Green kernels, Caccioppoli stability, and Harnack inequalities, Hopf boundary growth, harmonic measure, Schauder estimates, and Calderón–Zygmund L-p theory, boundary Harnack comparisons, capacities, removability, and Wiener regularity, semilinear nonlinear energies, monotone barrier iteration, eigenvalue thresholds for positive solutions, and bifurcation near singular Jacobians. Worked examples, derivations and exercises appear in each non-spoken mathematical companion.

`track.json` is the authoritative inventory. Source records live in `metadata/sources.json`; per-lecture citation links, original authorship and teaching prerequisites live in `metadata/*.json`; authorship lineage and editorial changes live in `provenance.yaml`. Consult [`LECTURE_STYLE_RULES.md`](../../LECTURE_STYLE_RULES.md) before further authoring. No runtime pack build or audio synthesis is required for content handoff.
