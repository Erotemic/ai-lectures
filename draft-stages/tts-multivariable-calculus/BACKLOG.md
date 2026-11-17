# Multivariable calculus — bridge coverage and next gaps

**Existing survey retained:** three consolidated manuscripts (`001000`, `008000`, `015000`) representing the original core material; their recorded `consolidated_from` IDs are not separate current manuscripts.

**New depth path (2026-11-17):** `019000`–`022000` expand Taylor bounds, strong convexity and conditioning, exact Newton steps, and local quadratic-convergence proofs. The material is intentionally more detailed than the short introduction in `008000` and the optimization/numerical-analysis surveys.

**New nonlinear least-squares bridge (2026-11-17):** `023000`–`026000` derive Gauss–Newton, Levenberg–Marquardt and trust-region step acceptance, distinguish structural from numerical identifiability, and develop Gaussian weighting, regularization and robust losses.

**New constrained optimization and sensitivity bridge (2026-11-17):** `027000`–`030000` derive feasible tangent and critical-cone geometry, KKT Newton block solves, local implicit derivatives, envelope and adjoint sensitivity. The survey in Optimization/Duality remains the reference for convex certificates.

**New variational and weak-formulation bridge (2026-11-17):** `031000`–`034000` construct functional derivatives, Euler–Lagrange boundary conditions, energy-space weak existence, and a full Ritz–Galerkin finite-element assembly with a checked error. This deepens—not duplicates—the weak/PDE overview in Differential Equations `010000` and Numerical Analysis error theory `018000`.

**New variational compactness and nonlinear-existence bridge (2026-11-17):** `035000`–`038000` develop Hilbert weak convergence and lower semicontinuity, dimension-dependent Sobolev and Rellich compactness, the direct method for a concrete nonlinear quartic energy, and a solved obstacle variational inequality with exact contact points. Prerequisites follow `031000`–`034000`; numerical and functional-analysis surveys are not replaced.

**New mixed finite element and inf–sup bridge (2026-11-17):** `039000`–`042000` derive the mixed Poisson formulation and conservation, the Babuška–Brezzi stability test and Schur complement, a two-cell spurious pressure mode with an exact stable repair, and the Stokes velocity-pressure formulation with compatible elements and block preconditioners. These extend the variational and constrained Newton material without rewriting them.

**New boundary-value and elliptic-regularity bridge (2026-11-17):** `043000`–`046000` derive a trace inequality and Dirichlet lift, solve Neumann/Robin problems with sign-correct compatibility, establish interior H-two regularity by difference quotients, and construct a cutoff reentrant-corner solution with smooth source but no global H-two regularity. Coordinate with the fractional-boundary overview in Analysis `068000`; do not duplicate its Littlewood–Paley material.

**New elliptic principles and estimates bridge (2026-11-17):** `047000`–`050000` prove weak maximum/comparison and a quadratic barrier; construct the exact interval Dirichlet Green kernel and its spectral representation; derive global and localized energy estimates; and show disk mean values, Poisson kernels, sharp Harnack and the measurable-coefficient distinction. The previous 43–46 boundary-regularity manuscripts remain unchanged.

**New Hopf, harmonic measure and advanced elliptic regularity bridge (2026-11-17):** `051000`–`054000` prove strict boundary growth by an annular barrier, derive Brownian exit/harmonic measure and a disk arc probability, explain C2-alpha Schauder estimates with divergence-form counterexample, and derive local W2p Calderón–Zygmund theory with bounded-source/unbounded-Hessian counterexample. Prior 47–50 manuscripts remain unchanged.

## Further bridge candidates, subject to a fresh cross-pack coverage audit

- Further nonlinear inverse-problem theory: parameter constraints and projected steps, adjoint-state sensitivity for expensive forward models, optimal experimental design, and uncertainty beyond a local Gaussian approximation; coordinate with Numerical Analysis and Optimization.
- Advanced constrained numerics: SQP globalization, primal-dual interior-point methods and sparse KKT preconditioning; avoid duplicating Optimization/Duality and Numerical Analysis.
- Further elliptic and potential-theoretic extensions: boundary Harnack beyond the disk, capacity and removable sets, semilinear comparison and monotone iteration; check Analysis and Differential Equations first.
- Further variational extensions: higher-dimensional quasiconvexity and polyconvexity, loss of compactness at critical exponents, boundary regularity for mixed Dirichlet–Neumann junctions, higher-order variable-coefficient and boundary regularity refinements, higher-dimensional compatible de Rham complexes, robustness under coefficient jumps, numerical convergence of obstacle active sets; coordinate with Differential Equations and Numerical Analysis.
- Multivariable integration over less regular domains: approximation and boundary convergence, only where Analysis and Measure Theory have gaps.

Do not treat lecture count, duration, or the presence of a topic label as evidence that a prerequisite has been taught adequately. Check actual manuscripts, proofs, and examples before adding material.
