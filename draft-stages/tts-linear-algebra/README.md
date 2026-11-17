# Linear Algebra from First Principles

A calculation-first and proof-driven course from linear equations and bases through spectral geometry, duals, and finite-dimensional operator theory. The matrix-operator route connects basic eigenvectors to generalized eigenspaces, functional calculus, and constant-coefficient differential equations. A separate numerical-matrix route develops reliable finite-dimensional computation. It distinguishes exact algebra from stable numerical computation and the separate hypotheses required for infinite-dimensional operators.

The pack contains **15 authored lecture manuscripts**. The original three composite foundation lectures retain their texts and IDs. Four exact-operator manuscripts (`016000`–`019000`), six numerical-solver manuscripts (`020000`–`025000`), and two numerical-spectral manuscripts (`026000`–`027000`) have independent spoken regions, mathematical companions, worked examples, exercises, and sources.

## Listening routes

- **Foundations** (`linear-algebra:survey`, the default): `001000` → `006000` → `012000`. This preserves a clear introductory route without adding specialist work automatically.
- **Matrix Operators** (`linear-algebra:operator-bridge`): `016000` → `017000` → `018000` → `019000`. Preparation: matrix multiplication, determinants, ordinary eigenvectors and matrix powers; derivatives and the scalar exponential for the final lecture.
- **Numerical Matrix Algorithms** (`linear-algebra:numerical-matrix-bridge`): `020000` → `021000` → `022000` → `023000` → `024000` → `025000`. Preparation: matrix elimination, inner products, orthogonal projection and basic matrix norms. Concrete factorization, error analysis, least squares, numerical rank, positive definite systems and conjugate gradients.
- **Numerical Spectral Theory** (`linear-algebra:spectral-computation-bridge`): `026000` → `027000`. Preparation: QR, eigenvalues, matrix exponentials and singular values; unitary Schur form, eigenvalue algorithms and pseudospectral sensitivity.
- **Complete sequence** (`linear-algebra:main`): all fifteen manuscripts, preserving the original full-source route and its bookmark identity.

## Current manuscripts

Durations below are measured from extracted spoken text at 145 words per minute; they are descriptions, not writing targets.

| ID | Lecture | Approximate minutes | Route |
| --- | --- | ---: | --- |
| `001000` | [From elimination to coordinate-free linear maps](001000-from-elimination-to-coordinate-free-linear-maps.md) | 34.3 | Foundation |
| `006000` | [Volume, spectral directions, and best approximation](006000-volume-spectral-directions-and-best-approximation.md) | 38.6 | Foundation |
| `012000` | [Linear measurements and constructions beyond vectors](012000-linear-measurements-and-constructions-beyond-vectors.md) | 27.9 | Foundation |
| `016000` | [When a Matrix Satisfies Its Own Polynomial: Cayley–Hamilton and the Minimal Polynomial](016000-when-matrices-satisfy-polynomials.md) | 12.4 | Matrix operators |
| `017000` | [Beyond Ordinary Eigenvectors: Jordan Chains and Generalized Eigenspaces](017000-generalized-eigenvectors-and-jordan-chains.md) | 12.9 | Matrix operators |
| `018000` | [Separating Mixed Modes: Polynomial Spectral Projectors and Primary Decomposition](018000-polynomial-projectors-and-primary-decomposition.md) | 12.4 | Matrix operators |
| `019000` | [From Repeated Steps to Continuous Motion: The Matrix Exponential](019000-matrix-exponential-and-linear-flows.md) | 13.9 | Matrix operators |
| `020000` | [Elimination That Remembers Its Work: Pivoted LU and Rank Factorization](020000-pivoted-elimination-lu-and-rank-factorization.md) | 11.9 | Numerical matrix algorithms |
| `021000` | [Orthogonalize Without Losing the Geometry: QR, Householder Reflections, and Least Squares](021000-qr-householder-and-least-squares.md) | 11.7 | Numerical matrix algorithms |
| `022000` | [What Does a Small Residual Prove? Conditioning, Backward Error, and Reliable Solves](022000-conditioning-residuals-and-backward-error.md) | 11.9 | Numerical matrix algorithms |
| `023000` | [When Rank Is Not a Yes-or-No Measurement: Singular Values and the Pseudoinverse](023000-numerical-rank-svd-and-pseudoinverse.md) | 12.1 | Numerical matrix algorithms |
| `024000` | [Positive-Definite Matrices: Why Cholesky Works and When It Fails](024000-positive-definite-matrices-and-cholesky.md) | 12.5 | Numerical matrix algorithms |
| `025000` | [Conjugate Gradients: From a Quadratic Energy to a Working Algorithm](025000-conjugate-gradients-from-energy-to-algorithm.md) | 13.7 | Numerical matrix algorithms |
| `026000` | [From Eigenvectors to Schur Form: Orthogonal Similarity and the QR Algorithm](026000-schur-form-and-qr-eigenvalue-iteration.md) | 13.5 | Numerical spectral theory |
| `027000` | [Beyond Eigenvalue Lists: Nonnormality, Resolvents, and Pseudospectra](027000-nonnormal-matrices-resolvents-and-pseudospectra.md) | 14.7 | Numerical spectral theory |

## Scope and applications

- `016000` establishes the Cayley–Hamilton identity and minimal polynomial, including a proof by adjugate-coefficient comparison and exact matrix-power reduction.
- `017000` uses explicit shear/Jordan examples and the dimensions of kernels of powers to explain generalized eigenspaces and block sizes. Jordan form is not presented as a numerically stable algorithm.
- `018000` constructs spectral projectors using polynomial Chinese remainders, illustrates Hermite interpolation for a defective matrix, and distinguishes algebraic and orthogonal projections.
- `019000` constructs the matrix exponential from its series, proves the linear evolution formula, computes Jordan and rotation examples, and treats transient growth, forcing, and noncommutativity.
- `020000` constructs a pivoted LU factorization with two row exchanges and a reusable solve, then distinguishes exact rank factorization from numerical pivot decisions.
- `021000` builds Gram–Schmidt/Householder QR explicitly and proves least-squares optimality by orthogonal projection, showing where normal equations amplify conditioning.
- `022000` derives forward-error and backward-error bounds, with a family where the residual tends to zero while the solution error stays nonzero.
- `023000` derives rank-aware SVD recovery, the minimum-norm pseudoinverse and the bias–variance trade of truncated SVD and Tikhonov regularization.
- `024000` derives Cholesky from positive Schur complements, solves an exact 3-by-3 system, and distinguishes semidefinite breakdown, floating-point ambiguity and sparse fill.
- `025000` derives conjugate gradients from energy minimization, executes two iterations with exact fractions, and develops the Krylov polynomial and preconditioning viewpoint.
- `026000` proves the complex Schur theorem, compares orthogonal and spectral projectors, and performs an exact QR iteration before explaining practical shifts and Hessenberg form.
- `027000` relates pseudospectra to singular values, resolvents and perturbations, with exact nonnormal examples of eigenvalue sensitivity and transient growth.

These lectures are finite-dimensional. Infinite-dimensional spectral theorems, operator domains, and strongly continuous semigroups remain subjects of the Analysis and advanced operator tracks. See the pack-local `BACKLOG.md` for additional missing core material.

## Sources and authorship

Per-lecture source records and teaching-preparation links are in `metadata/`; bibliographic entries are in `metadata/sources.json`. Previously consolidated manuscripts retain their inherited provenance. The twelve new manuscripts are attributed separately in `provenance.yaml`. Spoken-region markers select only narration for TTS; exact notation, equations and further reading remain in display-only companions. No media is generated by this content pack.
