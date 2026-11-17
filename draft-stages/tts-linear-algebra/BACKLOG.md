# Linear Algebra from First Principles — core gaps after the operator bridge

**Current indexed inventory:** eleven manuscripts: three original consolidated foundations (`001000`, `006000`, `012000`), four exact operator bridges (`016000`–`019000`), and four numerical matrix bridges (`020000`–`023000`). The original 15 short chapters were consolidated into the first three manuscripts on 16 November 2026; the older 15-entry manifest is not a separate playable inventory.

## Newly completed (17 November 2026)

- **016000** — Cayley–Hamilton and minimal polynomial: exact matrix-power reduction, proof, and diagonalization criterion.
- **017000** — Generalized eigenvectors and Jordan chains: kernel growth, multiplicities, proof structure, and numerical sensitivity.
- **018000** — Polynomial projectors and primary decomposition: Bézout/CRT, invariant subspaces, Hermite interpolation and the finite functional calculus.
- **019000** — Matrix exponential: series, differential equations, nilpotent and oscillatory modes, transients, forcing, and noncommuting matrices.

These close the previously recorded gap between elementary eigenvector calculations and the finite-dimensional algebra used by ODE, spectral, and functional-calculus courses.

## Newly completed numerical bridge (17 November 2026)

- **020000** — Pivoted elimination, exact `PA=LU`, reusable triangular solves, rank factorization and the pivot-growth caveat.
- **021000** — Constructive Gram–Schmidt, Householder reflections, stable QR, and an exact least-squares projection example.
- **022000** — Conditioning versus backward stability, a counterexample with vanishing residual and fixed forward error, and rigorous error inequalities.
- **023000** — Singular values, numerical rank, minimum-norm pseudoinverse, perturbations, truncated SVD and regularization.

The original `linear-algebra:survey` and `linear-algebra:operator-bridge` remain unchanged. New listening route: `linear-algebra:numerical-matrix-bridge`. The numerical-analysis pack keeps its own introductory material; the new work develops constructions and proofs rather than duplicating the overview.


## Highest-priority gaps for further basic-to-advanced bridges

1. **Cholesky and structure-aware solvers:** positive definite matrices, Cholesky construction and breakdown criteria, sparse fill, and the link to conjugate gradients; distinguish exact positivity from floating-point checks.
2. **Invariant subspaces and numerical spectral computation:** Schur decomposition, orthogonal projections versus oblique spectral projectors, pseudospectra and nonnormality; do not present computed Jordan normal forms as numerically stable.
3. **Exterior powers and Jacobians:** orientation, signed volume, differential determinants, and geometric applications, aligned with multivariable calculus and topology.
4. **Real canonical structures:** irreducible quadratic factors, real invariant planes, quadratic form signatures, symplectic matrices, and characteristic-sensitive caveats over finite fields.
5. **Infinite-dimensional boundaries:** compact versus bounded operators, continuous spectrum, unbounded domains, and Borel calculus. These require coordination with `analysis:046000`, `analysis:065000` and the G2 foundations, not silent extension of finite-dimensional arguments.

Further curriculum-wide bridge priorities (in other independent packs) include proof repair exercises, detailed multivariable Taylor/Newton error estimates, and probability/statistical decision theory from finite examples. Audit existing consolidated manuscripts before proposing a duplicate.

**Editorial constraint:** no fixed narration length or word-count target; judge mathematical completeness, worked examples, and honest prerequisites.
