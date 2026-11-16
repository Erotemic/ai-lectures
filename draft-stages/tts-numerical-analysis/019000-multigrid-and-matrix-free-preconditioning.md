# 019000 — Multigrid and Matrix-Free Preconditioning

**Track:** Numerical Analysis. **Background:** finite-difference Poisson equations, sparse solvers, residuals, iterative methods. **Central question:** how can a solver remove errors on many spatial scales without paying a high cost for the finest grid?

<!-- BEGIN SPOKEN LECTURE -->

# Why smoothing is not the same as solving

Take a discretized Poisson equation on a fine mesh. The matrix is sparse and well structured, but as the mesh is refined its condition number grows. A basic iterative method such as Jacobi can quickly remove some kinds of error and barely touch others. The surprising observation behind multigrid is that the distinction is spatial: oscillatory error is easy to eliminate locally, while slowly varying error can be stubborn.

To see this, imagine alternating positive and negative errors on adjacent grid points. Each local averaging step sees those strong variations and damps them rapidly. Now imagine a smooth hump that changes gradually over many grid cells. A local update sees neighboring values that are almost identical, so it makes little progress.

If we stop here, the number of iterations needed for convergence gets worse as the mesh becomes finer. Multigrid adds an entirely different operation: it represents the slowly varying error on a coarser grid, where that same error is no longer so slow relative to the mesh.

## Start with the one-dimensional Laplacian

The standard centered finite-difference approximation to the negative second derivative gives a tridiagonal matrix: two on the diagonal, minus one on each neighboring diagonal, and a factor of the inverse grid spacing squared. With zero boundary conditions, the matrix is symmetric positive definite.

A weighted Jacobi step updates the current vector using the residual. In a Fourier-mode analysis on an idealized regular grid, an error wave with frequency theta is multiplied by one minus the weight times one minus the cosine of theta.

Take the weight two thirds. For an alternating error, theta is pi, so one Jacobi sweep multiplies the error by minus one third. Its magnitude drops by a factor of three. But for a low-frequency error, theta is close to zero and the multiplier is close to one. That smooth error hardly changes.

This computation explains why multigrid does not simply run more Jacobi sweeps. It uses Jacobi or a related method for what it does well: smoothing the error, not solving every scale.

## Correct the error on a coarse grid

Suppose the fine-grid equation is A times u equals b. Given a current approximation, compute the residual b minus A times the approximation. The unknown error satisfies the same matrix A applied to the error equals that residual.

Now restrict the residual to a coarser grid. Solve a coarse equation for a coarse approximation to the error. Interpolate that error correction back to the fine grid and add it to the current solution. The low-frequency error that resisted fine-grid smoothing has become representable with fewer unknowns.

The process usually includes smoothing before the correction and often smoothing afterward. These steps target the high-frequency error components that may be introduced by interpolation or not fully removed before restriction.

A two-grid method uses one fine level and one coarse level. A multigrid method recurses, using a hierarchy of increasingly coarse grids. The resulting cycle is often drawn as a V: descend through the levels, solve on the coarsest grid, and ascend while correcting.

## The coarse operator is a mathematical choice

There are at least two ways to get a coarse-grid operator. In geometric multigrid we may discretize the same differential equation on the coarser mesh. In algebraic multigrid, we build coarse spaces and transfer operators from the matrix graph and algebraic relationships, often without direct knowledge of the physical geometry.

A common Galerkin choice is to construct the coarse matrix by multiplying restriction, the fine matrix, and prolongation. That choice makes coarse correction compatible with the fine-grid energy. But it does not by itself guarantee convergence. Smoothing properties, coarse approximation properties, interpolation stability, boundary treatment, and coefficients still matter.

The subtlety becomes visible with strongly varying or anisotropic material coefficients. A naive geometric coarse space may fail to represent the error modes that the smoother leaves behind. Then a multigrid cycle can stagnate. Better smoothers, semicoarsening, or algebraic interpolation may be needed.

## Matrix-free multigrid

The matrix in a high-order finite element discretization can be expensive to assemble and store. But evaluating its action on a vector may be much cheaper. Matrix-free methods compute these actions directly from element operations or local stencils. Krylov solvers can use such an action without ever storing a global sparse matrix.

Multigrid can also be organized around matrix-free fine-level actions, matrix-free smoothing, and compact coarse levels. The goal is to reduce memory traffic and improve scalability. The main caution is that an approximate coarse operator must still model the error modes left by smoothing.

Multigrid is often used as a preconditioner rather than as a standalone solver. One or more cycles provide an approximate inverse that a Krylov method can use. For a symmetric positive-definite problem, conjugate gradients require a compatible symmetric positive-definite preconditioner. A nonsymmetric multigrid cycle may instead be paired with GMRES or another appropriate method.

## When nearly linear cost is plausible

On a regular hierarchy, each coarser level has a fixed fraction of the unknowns on the preceding one. If the work on each level is proportional to the number of unknowns and the number of cycles needed stays bounded, total work can be proportional to the finest-grid size.

That near-linear scaling is conditional, not automatic. Difficult coefficients, changing geometry, inadequate coarse spaces, and communication overhead can spoil it. Multigrid success comes from matching the mathematics of error to the hierarchy, not from merely having more than one grid.

The central lesson is to split the problem by scales. Local relaxation attacks oscillations. Coarse spaces attack smooth error. If both mechanisms work together, refinement need not make the linear solve progressively more expensive in iteration count.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the 1D Dirichlet Poisson operator, `A_h=(1/h^2) tridiag(-1,2,-1)` on the interior points. Weighted Jacobi is `u_new=u+omega D^{-1}(b-Au)`. On idealized infinite or periodic grid Fourier error modes `e_j=exp(i j theta)` have amplification
\[
\mu(\theta)=1-\omega(1-\cos\theta).
\]
For `omega=2/3`, `mu(pi)=1-4/3=-1/3`, whereas for small theta `mu(theta)=1-O(theta^2)`. Boundary and finite-grid effects alter the exact eigenvectors but not the smoothing insight.

Let `R` be restriction and `P` prolongation. A coarse correction for residual `r_h=b_h-A_hu_h` solves `A_H e_H=R r_h`, then updates `u_h<-u_h+P e_H`. Galerkin coarse choice: `A_H=R A_h P`. With pre-smoother error propagation S, the two-grid error operator without post-smoothing is
\[
E_{TG}=(I-P A_H^{-1}R A_h)S.
\]
V-cycles recurse on the coarse solve. If level sizes contract geometrically, per-level work is linear, and iteration count remains bounded, work is `O(N)`; this is not universal for arbitrary coefficient fields or transfers.

For preconditioned conjugate gradients, the preconditioner must meet the required symmetry and positivity assumptions. A variable or nonsymmetric cycle may demand flexible or nonsymmetric Krylov methods. A small *linear* residual and a small *discretization* error are separate questions.

### Exercises with answers

1. For `omega=2/3`, compute the Jacobi amplification of an alternating error. **Answer:** minus one third.
2. Why does coarse correction help smooth errors? **Answer:** those errors can be well represented on a coarser space even though fine-grid local smoothing barely changes them.
3. Write the Galerkin coarse operator. **Answer:** `A_H=R A_h P`.
4. When may multigrid have linear work in the number of fine unknowns? **Answer:** when each level costs proportional work, hierarchy sizes shrink geometrically, and convergence needs a bounded number of cycles.

### Reading and source notes

- [Weinan E and collaborators, numerical analysis notes: multigrid](https://web.math.princeton.edu/~weinan/papers/main.pdf), two-grid and coarse correction.
- [Briggs, Henson and McCormick, A Multigrid Tutorial, 2nd edition](https://epubs.siam.org/doi/book/10.1137/1.9780898719505), smoothing and multilevel convergence.
- [Yousef Saad, Iterative Methods for Sparse Linear Systems](https://www-users.cse.umn.edu/~saad/IterMethBook_2ndEd.pdf), Krylov and preconditioning background.
