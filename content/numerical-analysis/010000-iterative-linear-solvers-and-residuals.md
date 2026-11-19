# 010000 — Iterative Linear Solvers: Residuals, Spectra, and Conjugate Gradients

**Track:** Numerical Analysis and Reliable Computation. **Background:** linear systems, matrix norms, condition numbers, floating-point error. **Question:** when does repeated correction converge, and when does a small residual certify an accurate solution?

<!-- BEGIN SPOKEN LECTURE -->

# Iterative Linear Solvers: Residuals, Spectra, and Conjugate Gradients

Solving a linear system means finding x so that A times x equals b. Direct methods, such as Gaussian elimination or a factorization, aim to reduce the problem to a finite sequence of algebraic operations. Iterative methods instead begin with a guess and improve it repeatedly. That can be much more practical when A is very large but sparse, because multiplying a sparse matrix by a vector may be cheap even when storing a complete factorization is expensive.

But iteration introduces new questions. Why should the updates converge? How fast? What if the method reports a tiny residual although the computed solution is still wrong? We will compare simple stationary updates with conjugate gradients, and separate exact-arithmetic theorems from the behavior of floating-point implementations.

## The residual is the equation's complaint

Given a candidate x, define its residual to be b minus A x. This vector tells us exactly how badly the candidate fails the stated equation. If the true solution is x star and A is invertible, subtracting equations gives the error x star minus x equals A inverse times the residual.

This identity gives a bound. The error norm is at most the norm of A inverse times the residual norm. A small residual therefore guarantees a small error only when A inverse is not excessively large in the chosen norm. In relative terms, conditioning also matters: the condition number of A multiplies an appropriately scaled relative residual bound.

Consider a matrix with diagonal entries one and one-millionth, with zeros elsewhere. Suppose the right-hand side is zero and our proposed solution is the vector with first coordinate zero and second coordinate one. The residual has magnitude one-millionth, seemingly tiny. But the true solution is zero, and our second coordinate has error one. Small residual, significant error, entirely because one direction of the matrix is poorly conditioned.

This example is not an indictment of residuals. They are precisely computable evidence of equation satisfaction, and often the best practical diagnostic. It is an argument against silently interpreting residual size as an error bound without conditioning information.

## Jacobi iteration as a fixed-point equation

Write A as D plus the remainder R, where D contains only the diagonal entries. Assuming every diagonal entry is nonzero, rearrange A x equals b into x equals D inverse times b minus D inverse times R x. The Jacobi method evaluates the right-hand side using the previous iterate. All coordinates are updated simultaneously from the old vector.

For the system four x minus y equals one and negative x plus three y equals two, the updates are x new equals one plus y old, divided by four; and y new equals two plus x old, divided by three. Starting from zero, the first guess after one update is one fourth and two thirds. Another update gives five twelfths and three fourths. The true answer is five elevenths and nine elevenths. The guesses approach it.

Why does this particular iteration work? Let B be its iteration matrix. Subtract the fixed-point equation for the exact solution from the iteration equation, and the error after each step equals B times the preceding error. Thus after k steps the error is B to the k times the initial error. The method converges from every starting guess exactly when the powers of B approach zero, which for a finite square matrix is equivalent to the spectral radius of B being strictly less than one.

For our two-by-two example, B has zero diagonal, one-fourth in the upper-right corner, and one-third in the lower-left. Its eigenvalues have magnitudes one divided by the square root of twelve, approximately 0.289. This is less than one, so the method converges. For a different matrix the same algebraic rearrangement might have spectral radius greater than one and diverge. Calling Jacobi an algorithm does not grant it a general convergence guarantee.

## Gauss–Seidel and choosing an update order

Gauss–Seidel uses the newest available component values as soon as they are computed. In the same system, update x using the old y, then update y using the new x. Starting from zero, x becomes one fourth and y becomes three fourths. The method often converges faster than Jacobi on suitable problems, but there is no universal ordering-independent speed comparison.

Both methods are stationary iterations: the same fixed linear update is applied at every step. Their convergence can be studied using iteration matrices, diagonal dominance, or positive-definiteness assumptions, with hypotheses stated precisely. Strict row diagonal dominance is a familiar sufficient condition for convergence of Jacobi and Gauss–Seidel under the standard splittings; it is not necessary. Positive definiteness of A ensures Gauss–Seidel convergence for the usual symmetric positive-definite setting, but does not by itself guarantee Jacobi convergence for every dimension and matrix.

The lesson is to inspect the structure of A, not just the update formula. When matrix structure is favorable, a simple iteration may be excellent. When it is unfavorable, an apparently modest equation can defeat a naive correction scheme.

## Conjugate gradients exploits geometry

For a real symmetric positive-definite matrix A, there is a deeper connection. Solving A x equals b is equivalent to minimizing the strictly convex quadratic function one half x transpose A x minus b transpose x. Its gradient is A x minus b, the negative residual. So we can view the linear system as an optimization problem with a unique minimizer.

Steepest descent moves in the residual direction and chooses a step length that minimizes the quadratic along that line. But successive steepest-descent directions can undo progress in narrow valleys when the matrix is poorly conditioned. Conjugate gradients constructs directions that are orthogonal under the A inner product rather than the ordinary dot product. These directions are called A-conjugate.

In exact arithmetic, each new direction removes an additional component of the error without undoing the progress made in previous conjugate directions. Conjugate gradients minimizes the quadratic over progressively larger Krylov subspaces, generated by the initial residual and its successive images under A. In an n-dimensional space, it reaches the exact answer after at most n iterations, assuming exact arithmetic and exact matrix-vector products. This finite-termination statement is a structural theorem, not a practical claim that an n-step floating-point run will always yield a perfect answer.

There is a quantitative bound in the A-energy norm. If kappa is the spectral condition number of the symmetric positive-definite matrix, the error after k conjugate-gradient steps is at most twice the initial energy error times the k-th power of a contraction factor: square root of kappa minus one, divided by square root of kappa plus one. When kappa is near one, this factor is small; when kappa is enormous, the worst-case guarantee can be slow.

The actual speed also depends on how the eigenvalues are distributed, not only their extreme ratio. Clusters of eigenvalues can make convergence much faster than a bound based solely on the condition number suggests.

## Preconditioning changes the question

If the original matrix is difficult, choose a preconditioner M that approximates A but is easy to solve against. Instead of using the raw residual as the correction direction, use M inverse applied to the residual. For symmetric positive-definite problems, the usual conjugate-gradient analysis uses an appropriate symmetric transformation involving M, so the transformed operator is again self-adjoint and positive definite in the relevant inner product.

The hope is that the preconditioned operator has a smaller effective condition number or more favorable spectral clusters. But a preconditioner is not automatically beneficial. It must be cheap enough to apply, stable enough, and effective enough to outweigh its construction cost. For sparse matrices, memory use and fill-in matter as much as an abstract iteration count.

## Stopping safely in finite precision

Floating-point conjugate gradients does not maintain perfect orthogonality or conjugacy. Its recursive residual may drift away from the explicitly recomputed value b minus A x. If a solver is claiming high accuracy, periodically recomputing the true residual helps check the claim. Scaling also matters: a relative residual divided by the norm of b is meaningless when b is zero, and a residual tolerance should account for both b and A times x, as well as the intended application.

Backward error asks which nearby system the candidate exactly solves. For a normwise perturbation to A and b, a common scaled residual is the residual norm divided by the norm of A times the norm of x plus the norm of b. This expresses equation satisfaction relative to the sizes of the data. It does not automatically turn into forward accuracy when the problem is ill-conditioned.

Thus a reliable iterative solver reports more than an iteration count or a success flag. It states the measured residual, the chosen scaling, the problem class and convergence assumptions, and, when available, an error bound that explicitly incorporates conditioning. The computational result is trustworthy not because the method is famous, but because the evidence matches the question we wanted to solve.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For nonsingular \(A\), \(r_k=b-Ax_k\), \(e_k=x_*-x_k\), and
\[
Ae_k=r_k,\qquad \|e_k\|\le \|A^{-1}\|\,\|r_k\|.
\]
A normwise scaled residual / backward-error diagnostic is \(\|r\|/(\|A\|\|x\|+\|b\|)\) when the denominator is nonzero.

**Jacobi:** \(A=D+R\), \(x_{k+1}=D^{-1}(b-Rx_k)\), \(B=-D^{-1}R\), so \(e_{k+1}=Be_k\). It converges for every start iff \(\rho(B)<1\).

**Worked system:** \(A=\begin{pmatrix}4&-1\\-1&3\end{pmatrix}\), \(b=(1,2)^T\), \(x_*=(5/11,9/11)^T\). Jacobi \(B=\begin{pmatrix}0&1/4\\1/3&0\end{pmatrix}\), with \(\rho(B)=1/\sqrt{12}\).

**Conjugate gradients** (real SPD \(A\), exact arithmetic): \(x_k\) minimizes \(\tfrac12x^TAx-b^Tx\) over \(x_0+\mathcal K_k(A,r_0)\), where \(\mathcal K_k=\mathrm{span}\{r_0,Ar_0,\dots,A^{k-1}r_0\}\). With \(\|z\|_A=\sqrt{z^TAz}\) and \(\kappa_2(A)=\lambda_{\max}/\lambda_{\min}\),
\[
\|e_k\|_A\le2\left(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\right)^k\|e_0\|_A.
\]
This bound is an exact-arithmetic theorem; floating-point effects require separate monitoring.

### Exercises with answers

1. Compute the first Jacobi iterate of the worked system from zero. **Answer:** \((1/4,2/3)^T\).
2. Find the error and residual for \(A=\operatorname{diag}(1,10^{-6})\), \(b=0\), \(x=(0,1)^T\). **Answer:** \(x_*=0\); error norm one, residual norm \(10^{-6}\).
3. Why is CG not directly guaranteed for an arbitrary nonsymmetric matrix? **Answer:** the positive-definite quadratic and A-inner-product conjugacy arguments do not apply.
4. Can a residual bound alone guarantee small forward error? **Answer:** not without control of \(\|A^{-1}\|\) or conditioning.

### Reading

James W. Demmel, *Applied Numerical Linear Algebra*, on residuals, conditioning and iterative methods; Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, on Krylov subspaces and conjugate gradients; MIT OpenCourseWare, [18.330 numerical analysis notes](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2004/pages/lecture-notes/).
