# Multigrid from near-nullspace to anisotropy

<!-- BEGIN SPOKEN LECTURE -->

# Multigrid from near-nullspace to anisotropy

## Multigrid and Matrix-Free Preconditioning

Take a discretized Poisson equation on a fine mesh. The matrix is sparse and well structured, but as the mesh is refined its condition number grows. A basic iterative method such as Jacobi can quickly remove some kinds of error and barely touch others. The surprising observation behind multigrid is that the distinction is spatial: oscillatory error is easy to eliminate locally, while slowly varying error can be stubborn.

To see this, imagine alternating positive and negative errors on adjacent grid points. Each local averaging step sees those strong variations and damps them rapidly. Now imagine a smooth hump that changes gradually over many grid cells. A local update sees neighboring values that are almost identical, so it makes little progress.

If we stop here, the number of iterations needed for convergence gets worse as the mesh becomes finer. Multigrid adds an entirely different operation: it represents the slowly varying error on a coarser grid, where that same error is no longer so slow relative to the mesh.

### Start with the one-dimensional Laplacian

The standard centered finite-difference approximation to the negative second derivative gives a tridiagonal matrix: two on the diagonal, minus one on each neighboring diagonal, and a factor of the inverse grid spacing squared. With zero boundary conditions, the matrix is symmetric positive definite.

A weighted Jacobi step updates the current vector using the residual. In a Fourier-mode analysis on an idealized regular grid, an error wave with frequency theta is multiplied by one minus the weight times one minus the cosine of theta.

Take the weight two thirds. For an alternating error, theta is pi, so one Jacobi sweep multiplies the error by minus one third. Its magnitude drops by a factor of three. But for a low-frequency error, theta is close to zero and the multiplier is close to one. That smooth error hardly changes.

This computation explains why multigrid does not simply run more Jacobi sweeps. It uses Jacobi or a related method for what it does well: smoothing the error, not solving every scale.

### Correct the error on a coarse grid

Suppose the fine-grid equation is A times u equals b. Given a current approximation, compute the residual b minus A times the approximation. The unknown error satisfies the same matrix A applied to the error equals that residual.

Now restrict the residual to a coarser grid. Solve a coarse equation for a coarse approximation to the error. Interpolate that error correction back to the fine grid and add it to the current solution. The low-frequency error that resisted fine-grid smoothing has become representable with fewer unknowns.

The process usually includes smoothing before the correction and often smoothing afterward. These steps target the high-frequency error components that may be introduced by interpolation or not fully removed before restriction.

A two-grid method uses one fine level and one coarse level. A multigrid method recurses, using a hierarchy of increasingly coarse grids. The resulting cycle is often drawn as a V: descend through the levels, solve on the coarsest grid, and ascend while correcting.

### The coarse operator is a mathematical choice

There are at least two ways to get a coarse-grid operator. In geometric multigrid we may discretize the same differential equation on the coarser mesh. In algebraic multigrid, we build coarse spaces and transfer operators from the matrix graph and algebraic relationships, often without direct knowledge of the physical geometry.

A common Galerkin choice is to construct the coarse matrix by multiplying restriction, the fine matrix, and prolongation. That choice makes coarse correction compatible with the fine-grid energy. But it does not by itself guarantee convergence. Smoothing properties, coarse approximation properties, interpolation stability, boundary treatment, and coefficients still matter.

The subtlety becomes visible with strongly varying or anisotropic material coefficients. A naive geometric coarse space may fail to represent the error modes that the smoother leaves behind. Then a multigrid cycle can stagnate. Better smoothers, semicoarsening, or algebraic interpolation may be needed.

### Matrix-free multigrid

The matrix in a high-order finite element discretization can be expensive to assemble and store. But evaluating its action on a vector may be much cheaper. Matrix-free methods compute these actions directly from element operations or local stencils. Krylov solvers can use such an action without ever storing a global sparse matrix.

Multigrid can also be organized around matrix-free fine-level actions, matrix-free smoothing, and compact coarse levels. The goal is to reduce memory traffic and improve scalability. The main caution is that an approximate coarse operator must still model the error modes left by smoothing.

Multigrid is often used as a preconditioner rather than as a standalone solver. One or more cycles provide an approximate inverse that a Krylov method can use. For a symmetric positive-definite problem, conjugate gradients require a compatible symmetric positive-definite preconditioner. A nonsymmetric multigrid cycle may instead be paired with GMRES or another appropriate method.

### When nearly linear cost is plausible

On a regular hierarchy, each coarser level has a fixed fraction of the unknowns on the preceding one. If the work on each level is proportional to the number of unknowns and the number of cycles needed stays bounded, total work can be proportional to the finest-grid size.

That near-linear scaling is conditional, not automatic. Difficult coefficients, changing geometry, inadequate coarse spaces, and communication overhead can spoil it. Multigrid success comes from matching the mathematics of error to the hierarchy, not from merely having more than one grid.

The central lesson is to split the problem by scales. Local relaxation attacks oscillations. Coarse spaces attack smooth error. If both mechanisms work together, refinement need not make the linear solve progressively more expensive in iteration count.

## Anisotropic Multigrid: When the Grid Has a Preferred Direction

Consider heat diffusion in a thin layered material. Heat moves easily along the layers but much less easily across them. The governing elliptic equation contains derivatives in two directions, but the coefficients multiplying them differ greatly.

A multigrid solver that handles the ordinary Laplacian in a handful of cycles might slow drastically on this problem. That is not because multigrid has somehow forgotten calculus. Its standard components—point relaxation and uniform coarsening—are matched to an assumption that the equation couples neighboring grid points comparably in different directions. Strong anisotropy breaks that assumption.

The cure is to make the smoother or the coarse grid aware of direction. Two classical remedies are line relaxation, which solves many strongly coupled unknowns together, and semicoarsening, which reduces resolution selectively in the direction where ordinary relaxation has already smoothed the error.

## A model with one weak derivative

Write the elliptic equation as minus epsilon times the second derivative in x, minus the second derivative in y, equals a source. Think of epsilon as small and positive. Diffusion in y is strong, and diffusion in x is weak.

On a square grid with equal spacing, the five-point finite-difference stencil has horizontal neighbor weights proportional to epsilon and vertical neighbor weights proportional to one. The diagonal entry is proportional to twice one plus epsilon. As epsilon approaches zero, the system almost decouples into independent vertical columns.

This suggests where trouble could occur. If two adjacent columns have opposite errors but the error is nearly constant down each column, their difference across x has only a weak effect on the residual. A pointwise update sees a large diagonal dominated by strong y coupling and a tiny residual from the weak x coupling. It barely changes the alternating-column error.

## A one-line Fourier calculation diagnoses failure

Imagine an error that alternates sign from one x grid point to the next but is constant in y. In an interior Fourier-mode calculation, the discrete operator acts on this error with a factor proportional to four epsilon divided by the grid spacing squared. The diagonal of the discrete matrix is twice one plus epsilon divided by the grid spacing squared.

Weighted Jacobi changes that error by a factor of one minus twice the relaxation weight times epsilon divided by one plus epsilon. If epsilon is very small, this factor is near one. The method can perform many relaxation sweeps without significantly reducing the error.

Normally a high-frequency alternating error is precisely what a smoother should remove. Here it is high frequency in x but low energy because coupling in x is weak. Uniform coarsening in x and y discards the ability to represent that oscillation on the coarse grid, while the smoother has failed to eliminate it. The classic multigrid division of labor breaks down.

The calculation is more informative than saying a convergence curve looked bad. It identifies the error mode and predicts how the smoothing factor behaves as epsilon goes to zero.

## Remedy one: update an entire strong line

Because y coupling is strong, group the unknowns along a vertical line and solve the corresponding block system together. A line Gauss–Seidel smoother effectively treats strong y coupling implicitly, then updates columns in sequence. This changes the scale of the correction for errors that pointwise relaxation could barely touch.

For a regular grid, the block along each vertical line is tridiagonal, so one can solve it efficiently. The method is also straightforward to parallelize across independent groups for a block Jacobi variant, though serial Gauss–Seidel dependencies and memory layout affect real performance.

Line relaxation is not a universal solution. If the principal diffusion direction rotates through the domain, a fixed set of vertical lines may no longer align with strong couplings. In three dimensions, a problem with strong coupling in two directions can require plane relaxation, and solving plane subproblems may be expensive. Unstructured meshes add further complexity.

## Remedy two: coarsen only where errors are smooth

The other approach is to retain every x grid point while coarsening in y, the strong-coupling direction. Ordinary point smoothing already removes many high-frequency errors in y. A coarse grid with fewer y nodes but all the x nodes can still represent error that alternates from one weakly coupled column to the next.

This is semicoarsening. It deliberately reduces the unknown count more slowly per level than full coarsening, but it repairs the approximation property that full coarsening lost. It can therefore reduce the total cost of solving the problem even though each coarse-grid hierarchy is larger.

Why coarsen in the strong direction rather than the weak direction? Because interpolation along strongly coupled directions represents the remaining smooth errors accurately. In the weak direction, the troublesome unsmoothed oscillations must remain representable. The choice follows from the smoothing analysis, not from the geometry of the drawing.

Line smoothing and semicoarsening are often alternative strategies, though combinations can be effective. Which is faster depends on coefficient variation, anisotropy orientation, grid structure, coarse solver, and hardware.

## A concrete failure ratio

Choose epsilon equal to one thousandth and a Jacobi relaxation weight of two thirds. The alternating-column mode is multiplied by approximately one minus four thirds of one thousandth, or about zero point nine nine eight six seven. After ten sweeps, more than ninety-eight percent of that mode's amplitude remains.

The problem is not that ten sweeps are always insufficient. With isotropic diffusion, the same alternating mode would be strongly damped. Anisotropy has made that particular error almost invisible to the point smoother. A directional method addresses this root cause instead of simply increasing the sweep count.

The same phenomenon arises when the continuous PDE is isotropic but the mesh cells are highly stretched. Discretization weights involve coefficient divided by grid spacing squared. A small spatial step in one direction can create strong numerical coupling even if the physical diffusion coefficients are equal. Numerical anisotropy and physical anisotropy lead to similar solver design questions.

## Algebraic multigrid and strength of connection

On an unstructured mesh, or when coefficients vary sharply, it is difficult to decide on directions by looking at coordinate axes. Algebraic multigrid constructs coarsening and interpolation from the matrix graph and numerical strengths of connections. Properly designed algebraic methods can recognize strongly coupled sets and build coarse representations suited to the operator.

But the label algebraic multigrid is not itself a guarantee of robustness. Strength-of-connection heuristics, interpolation quality and smoother choices matter, particularly for rotated anisotropy, discontinuous coefficients, systems of equations, and nearly singular operators.

We can inspect a solver with the same questions used in the Fourier calculation. Which error modes does the smoother leave behind? Can the coarse space approximate those modes? Is the transfer operator stable in the relevant energy norm? Do the two components cooperate as the anisotropy ratio becomes extreme?

## The criterion is uniform performance

A robust anisotropic multigrid method should not require more and more iterations simply because epsilon approaches zero, within the regime covered by its assumptions. Uniform convergence estimates make that claim precise. Real implementations must also account for work per cycle, communication and memory access, not only the contraction factor.

The key lesson is that low-frequency and high-frequency error are not absolute labels. They are meaningful relative to the operator and its couplings. A checkerboard across weakly connected columns can be a hard error even though it looks highly oscillatory. A good multigrid scheme adapts its notion of smoothing and coarse representation to that fact.

## Algebraic Multigrid for Rotated Anisotropy

Multigrid methods accelerate the solution of elliptic differential equations by separating errors according to how they behave under simple relaxation. Rapidly oscillating errors are often reduced quickly by a smoother such as weighted Jacobi or Gauss–Seidel. Smooth, slowly varying errors survive. A coarser representation can correct those slow modes more efficiently.

That picture is straightforward for isotropic diffusion on a regular rectangular grid. But imagine diffusion that is thousands of times faster along a diagonal direction than across it. The strongest coupling no longer follows the horizontal or vertical coordinate lines. A coarse grid built only by deleting every other horizontal and vertical node may fail to represent the slow modes accurately.

Algebraic multigrid asks a different question. Instead of trusting the original geometric coordinates, can we infer the relevant coarse structure from the sparse matrix itself?

## A matrix is a graph of interactions

For a standard diffusion discretization, the matrix has positive diagonal entries and nonpositive off-diagonal entries. A large negative off-diagonal entry says that two unknowns are strongly coupled. If one changes while the other does not, the energy cost can be high.

Classical algebraic multigrid defines a notion of strength of connection by comparing the magnitude of each negative off-diagonal with the strongest such connection in its row. Coarse points are selected so that the strong interactions are represented, directly or through interpolation. Fine-point values are then approximated using selected coarse neighbors.

This is an algorithmic decision. The method does not have to know which way the physical material was rotated. The pattern and weight of matrix edges reveal the important directions.

But the classical criterion assumes a particular matrix sign pattern. Systems of elasticity, indefinite matrices, and general nonsymmetric operators may need different strength measures or near-nullspace information. Even for rotated anisotropy, an unfortunate discretization can obscure the strong direction. Algebraic does not mean automatic for every operator.

## A two-variable exact calculation

Consider the symmetric matrix with diagonal entries one plus epsilon and off-diagonal entries negative one, where epsilon is a small positive number. It has two natural error patterns. In the first, both unknowns have the same value. In the second, their values are opposite.

The same-value mode has eigenvalue epsilon. It is a low-energy mode and changes little under relaxation. The opposite-value mode has eigenvalue two plus epsilon. It is high-energy and much easier to smooth.

Use weighted Jacobi with weight one half. The same-value mode is multiplied by nearly one when epsilon is tiny. The opposite-value mode is multiplied by approximately zero. Therefore relaxation efficiently kills the alternating error but hardly touches the error in which the variables move together.

Now choose a one-dimensional coarse space represented by the vector whose two entries are both one. That space contains the slow mode exactly. A Galerkin coarse correction removes that mode exactly in this toy problem. One inexpensive coarse degree of freedom has done what many Jacobi iterations could not.

This is the central design principle of multigrid: interpolate algebraically smooth error well, not necessarily geometrically smooth error in the original coordinates.

## What rotated diffusion changes

On a two-dimensional rotated-anisotropy problem, the low-energy patterns may form long narrow structures along the direction of strong diffusion. A naive point smoother may not damp them. Classical geometry-based coarsening may misidentify which fine-grid values can be reconstructed from the coarse grid.

Several remedies are available. Strength-of-connection graphs can select coarse points along the relevant couplings. Long-range interpolation can capture information beyond immediate neighbors. Adaptive or bootstrap algebraic multigrid can learn near-nullspace modes from test vectors. For elasticity, the near-nullspace includes rigid motions rather than only constants.

An algebraic multigrid hierarchy consists of interpolation operators and coarse matrices formed by the Galerkin product. On each level, a smoother reduces error outside the coarse space, and a coarse correction reduces error inside it. Good convergence depends on both halves: a weak smoother cannot be rescued by merely adding levels, and poor interpolation leaves persistent errors that the coarse solve never sees.

## A preconditioner rather than a magic inverse

A multigrid cycle can be a standalone iterative solver or a preconditioner inside conjugate gradients. For symmetric positive definite problems, the preconditioner must meet the appropriate symmetry and positivity conditions to use standard conjugate gradients safely. An arbitrary nonsymmetric relaxation sequence does not automatically satisfy them.

In practice, choices such as strength thresholds, coarsening, interpolation sparsity, and relaxation schemes affect both convergence and memory. Rich interpolation can reduce iterations but create expensive coarse operators. Sparse interpolation can be cheap but fail on rotated or highly heterogeneous problems.

Thus performance should be judged using more than the number of multigrid cycles. Setup cost, total work, memory, and actual residual reduction all matter.

## Let the operator choose the grid

The two-variable calculation captures why algebraic multigrid works when it works. The slow mode is invisible to a simple smoother but obvious to the energy defined by the matrix. The coarse basis is constructed to preserve that mode, so the solver can correct it efficiently.

For rotated anisotropy, there may be no simple geometric picture of a good coarse grid. The matrix itself becomes the map. Algebraic multigrid turns the pattern of sparse couplings into a hierarchy of approximations, provided the chosen strength and interpolation machinery reflect the actual near-nullspace of the problem.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Multigrid and Matrix-Free Preconditioning

**Track:** Numerical Analysis. **Background:** finite-difference Poisson equations, sparse solvers, residuals, iterative methods. **Central question:** how can a solver remove errors on many spatial scales without paying a high cost for the finest grid?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. For `omega=2/3`, compute the Jacobi amplification of an alternating error. **Answer:** minus one third.
2. Why does coarse correction help smooth errors? **Answer:** those errors can be well represented on a coarser space even though fine-grid local smoothing barely changes them.
3. Write the Galerkin coarse operator. **Answer:** `A_H=R A_h P`.
4. When may multigrid have linear work in the number of fine unknowns? **Answer:** when each level costs proportional work, hierarchy sizes shrink geometrically, and convergence needs a bounded number of cycles.

##### Reading and source notes

- [Weinan E and collaborators, numerical analysis notes: multigrid](https://web.math.princeton.edu/~weinan/papers/main.pdf), two-grid and coarse correction.
- [Briggs, Henson and McCormick, A Multigrid Tutorial, 2nd edition](https://epubs.siam.org/doi/book/10.1137/1.9780898719505), smoothing and multilevel convergence.
- [Yousef Saad, Iterative Methods for Sparse Linear Systems](https://www-users.cse.umn.edu/~saad/IterMethBook_2ndEd.pdf), Krylov and preconditioning background.

### Anisotropic Multigrid: When the Grid Has a Preferred Direction

**Track:** Numerical Analysis. **Background:** elliptic finite differences, relaxation, Fourier modes, and multigrid. **Central question:** why can a solver that works for the Laplacian fail when diffusion is much stronger in one direction?

#### Mathematical companion (not spoken)

Take `A_h` from the five-point discretization of `-epsilon u_xx-u_yy=f` on an equal-spacing grid. For an interior periodic Fourier mode `e_{i,j}=(-1)^i`, constant in j, the symbol is `lambda_h=4 epsilon/h^2`. The Jacobi diagonal is `D=2(1+epsilon)/h^2`, so the weighted-Jacobi amplification factor is
\[
\mu=1-\omega D^{-1}\lambda_h=1-\frac{2\omega\epsilon}{1+\epsilon}.
\]
At `epsilon=10^{-3}`, `omega=2/3`, this is approximately `0.998668`. After ten iterations, its amplitude factor is about `0.98676`. The periodic Fourier mode is a local smoothing analysis device; it is not claimed to satisfy homogeneous Dirichlet boundary conditions globally.

**Line smoothing:** group unknowns along vertical (strong y) lines. Block solves incorporate the large y coupling. **Semicoarsening:** retain x resolution and coarsen only in y to keep poorly smoothed, oscillatory-in-x errors representable. These remedies use different divisions of labor. Rotated anisotropy, stretched grids, variable coefficients and parallel complexity require separate analysis; a generic solver named multigrid is not automatically anisotropy robust.

##### Exercises with answers

1. In `-epsilon u_xx-u_yy`, which is the strongly coupled direction for small epsilon and equal mesh steps? **Answer:** y.
2. What happens to the weighted-Jacobi amplification factor of the alternating x mode as epsilon tends to zero? **Answer:** it tends to one, indicating little smoothing.
3. Which direction should be semicoarsened with point relaxation in this model? **Answer:** y, the strong direction; preserve x resolution.
4. Why can a stretched grid mimic coefficient anisotropy? **Answer:** stencil weights scale like the diffusion coefficient divided by the squared mesh spacing.

##### Reading and source notes

- [Naik and van Rosendale, The Improved Robustness of Multigrid Elliptic Solvers Based on Multiple Semicoarsened Grids](https://doi.org/10.1137/0730010), anisotropic convergence remedies.
- [Apel and Schöberl, Multigrid Methods for Anisotropic Edge Refinement](https://doi.org/10.1137/S0036142900375414), line smoothing and semicoarsening.
- [Briggs, Henson and McCormick, A Multigrid Tutorial](https://epubs.siam.org/doi/book/10.1137/1.9780898719505), Fourier error modes and anisotropic coarsening.

### Algebraic Multigrid for Rotated Anisotropy

**Track:** Numerical Analysis and Reliable Computation. **Background:** sparse symmetric matrices, eigenvectors, iterative solvers, and geometric multigrid. **Central question:** can a solver discover the slow error modes of a differential operator directly from its matrix?

#### Mathematical companion (not spoken)

For `\varepsilon>0`, define
\[
A_\varepsilon=\begin{pmatrix}1+\varepsilon&-1\\-1&1+\varepsilon\end{pmatrix}.
\]
The eigenpairs are `e_+=(1,1)^T`, `\lambda_+=\varepsilon` and `e_-=(1,-1)^T`, `\lambda_-=2+\varepsilon`. Weighted Jacobi `S=I-\omega D^{-1}A_\varepsilon` with `D=(1+\varepsilon)I`, `\omega=1/2` has multipliers
\[
\mu_+=1-\frac{\varepsilon}{2(1+\varepsilon)},\qquad
\mu_-=1-\frac{2+\varepsilon}{2(1+\varepsilon)}=\frac{\varepsilon}{2(1+\varepsilon)}.
\]
As `\varepsilon\to0^+`, `\mu_+\to1`, `\mu_-\to0`. For prolongation `P=e_+`, the Galerkin coarse matrix is `A_c=P^TA_\varepsilon P=2\varepsilon`. The exact coarse correction `I-P A_c^{-1}P^TA_\varepsilon` annihilates `e_+`, while leaving `e_-` unchanged. Together with smoothing, the two-level method handles both modes.

Classical AMG for an M-matrix typically defines a strong edge `i\to j` when `-a_{ij}\ge\theta\max_{k\ne i}(-a_{ik})` for threshold `\theta\in(0,1]`, with various conventions for nonnegative entries. Rotated anisotropy can require long-range interpolation or strength measures that reflect couplings missed by this simple threshold. The example above is an algebraic slow-mode illustration, *not* a complete rotated-grid discretization.

##### Exercises with answers

1. Why is `A_\varepsilon` positive definite for `\varepsilon>0`? **Answer:** both eigenvalues `\varepsilon` and `2+\varepsilon` are positive.
2. What is `P^TA_\varepsilon P` for `P=(1,1)^T`? **Answer:** `2\varepsilon`.
3. Which mode is poorly damped by weighted Jacobi as `\varepsilon\to0`? **Answer:** the same-value mode `e_+`.
4. Is a symmetric positive definite matrix alone sufficient to guarantee every AMG configuration converges well? **Answer:** No; interpolation and smoother must capture complementary error components.

##### Reading and source notes

- [hypre, BoomerAMG Documentation](https://hypre.readthedocs.io/en/stable/solvers-boomeramg.html), practical coarsening, interpolation, strength thresholds, and system modes.
- [Trottenberg, Oosterlee, and Schüller, Multigrid (book information)](https://books.google.com/books/about/Multigrid.html?id=nrD-zwEACAAJ), multigrid convergence mechanisms and anisotropy.
