# 006000 — Linear Algebra in Finite Precision: Pivoting, Conditioning, and Residuals

**Track:** Numerical Analysis and Reliable Computation. **Background:** elementary linear systems; elimination and vector norms developed in speech. **Purpose:** explain why pivoting is algorithmically essential, what backward stability does and does not promise, and why least squares is often better solved by QR than normal equations.

<!-- BEGIN SPOKEN LECTURE -->

# Linear Algebra in Finite Precision

A computer can solve a system of thousands of linear equations without showing us its intermediate work. That convenience conceals a series of numerical choices. The program might eliminate variables row by row, pivot to avoid dangerous divisions, factor the matrix into orthogonal pieces, or exploit positive definiteness. Those choices can determine whether the answer is useful, even when they all represent exact algebraic identities on paper.

A linear system is a good place to unite the ideas of conditioning and backward stability. We will examine one tiny example where a careless elimination algorithm fails spectacularly, then ask how residuals and matrix norms turn the output into a meaningful certificate.

## One tiny pivot, one enormous intermediate number

Consider two equations. The first says one part in ten to the twentieth of x, plus y, equals approximately one. The second says x plus y equals two. The intended solution is very close to x equals one, y equals one.

If we solve by ordinary Gaussian elimination and use the tiny coefficient of x in the first row as the first pivot, we divide the second equation's x coefficient by that tiny number. The multiplier is around ten to the twentieth power. We then subtract that huge multiple of the first row from the second. The transformed coefficients and right-hand side become enormous and nearly cancel later in the solve. In limited precision, this is a recipe for losing information.

The exact algebra is legal because the tiny pivot is nonzero. But the computational path may turn small initial uncertainties into dominant intermediate rounding effects. In binary64 arithmetic, an unpivoted calculation with that tiny pivot can return a completely wrong first component even though the system itself is not ill-conditioned.

There is a simple escape: swap the rows. The second equation has coefficient one in the x column. Use it as the pivot, and the multiplier needed to eliminate x from the other row is tiny rather than enormous. The revised arithmetic avoids the catastrophic intermediate scaling.

This is partial pivoting: at each elimination step, choose an entry of greatest magnitude among the eligible rows of the current column and exchange rows. It costs comparisons and row moves, but it greatly improves reliability in ordinary cases.

## Pivoting is not an unconditional magic shield

A common shorthand says that Gaussian elimination with partial pivoting is stable. For most well-scaled practical problems, it is an effective and standard method. But an exact theorem has more detail. Its backward-error bound depends on the precision, matrix size, and how large intermediate entries become relative to the original matrix. That last quantity is the growth factor.

Some carefully constructed matrices cause large growth even with partial pivoting. This does not make pivoting a bad idea; it means we should not claim a uniform tiny backward error for every matrix without conditions. A numerical library may use additional scaling, pivot strategies, or iterative refinement, and it may estimate whether the computed solution is reliable for the user's problem.

Partial pivoting addresses a dangerous algorithmic route. It cannot fix a system whose exact solution changes dramatically under small changes in the coefficients.

## Residuals tell us what was solved

Suppose a program returns a candidate vector. Multiply the original matrix by that vector and subtract the original right-hand side. The resulting vector is the residual. Its norm measures how well the candidate satisfies the original equations.

If the matrix is invertible, the difference between the candidate and the true solution is the inverse matrix applied to the residual, with a sign according to convention. That is not an approximation; it is an exact algebraic identity. So a norm bound on the inverse converts a residual bound into a forward-error bound.

But if the inverse is large, the result may still be inaccurate. This is the conditioning side. For example, two nearly redundant equations allow quite different solutions to satisfy nearly the same right-hand sides. The algorithm might be doing a stable job of a poorly determined task.

There is another subtlety: the residual itself is usually computed in floating point. A printed residual from the same limited-precision calculation is not automatically a rigorous residual of the exact mathematical system. Recomputing it in higher precision, using fused operations, or obtaining an interval enclosure can improve its credibility. We must not mistake a diagnostic number for a mathematical certificate unless its own error is controlled.

## Forward error and backward error meet

Suppose the residual is small compared with the norms of the matrix, the candidate vector, and the right-hand side. Then the candidate is the exact solution to a nearby linear system under a common normwise perturbation measure. This is a backward-error statement. If the matrix condition number is also modest, nearby systems have nearby solutions, and we can infer a useful forward-error conclusion.

If either ingredient is missing, we must say what remains unknown. Low backward error and high condition number: stable algorithm, uncertain solution. Low condition number and high backward error: the problem is forgiving, but the computation was poor. Both low: strong evidence of a reliable numerical answer, subject to the arithmetic assumptions underlying the estimates.

A condition number is therefore not an algorithm score, and a residual is not a problem score. The two measure different obstructions to accuracy.

## Least squares needs another viewpoint

Many applications have more equations than unknowns. Measurements of a line's slope from many noisy points, for example, produce an overdetermined linear system. Typically there is no vector that satisfies all equations exactly, so we minimize the sum of squared residuals.

The optimality conditions lead to the normal equations, where the transpose of the data matrix is multiplied by the data matrix. This is algebraically correct. But forming that product squares the spectral condition number when the original matrix has independent columns. A problem with condition number one hundred becomes a normal-equations system with condition number ten thousand. In finite precision, that can throw away useful digits.

A more reliable approach is often QR factorization. Represent the matrix as an orthogonal factor times an upper triangular factor. Orthogonal transformations preserve Euclidean lengths, so they do not magnify the norm of the data during the transformation. Householder reflections are a standard stable way to construct this factorization; then solve a triangular system. Singular-value decomposition is another powerful option, especially when rank deficiency or severe conditioning matters.

It is not that normal equations are forbidden. They can be appropriate when the conditioning is mild and computational circumstances justify them. The important point is that mathematical equivalence does not imply equal numerical sensitivity of the procedures used to obtain the result.

## Other structures deserve other algorithms

Not every matrix should be attacked by a generic elimination routine. If a square matrix is symmetric and positive definite, a Cholesky factorization expresses it as a triangular factor times its transpose. This uses the special geometry of the problem and can be both faster and more reliable than ignoring the structure. If the matrix is sparse, the elimination ordering influences how many new nonzero entries appear, and therefore both time and memory. Numerical pivoting and sparse fill reduction may have competing preferences.

For least squares, if the columns are nearly linearly dependent, even QR may produce a problem whose solution is inherently sensitive. A singular-value decomposition makes near-dependence explicit. Truncating small singular values can regularize an unstable solution, but that changes the mathematical problem: it substitutes a prior assumption or a preference for smaller solution components. The output should therefore be described as a regularized estimate rather than the exact solution of the original least-squares question.

This distinction matters in inverse problems. Recovering a hidden signal from noisy measurements can be ill-conditioned even when every linear-algebra operation is backward stable. Choosing a regularization parameter then becomes part of the scientific model and error budget, not merely a numerical implementation detail.

## A responsible solver has statuses, not just vectors

Imagine a routine returning a candidate solution to a large system. What can it tell us beyond the vector? It might report whether the factorization encountered a zero or tiny pivot, whether an estimated reciprocal condition number is small, how large the scaled residual is, whether refinement improved the solution, and whether an error estimate is trustworthy.

For sparse systems, choosing pivots also affects fill-in and memory use, so the numerically safest local choice may compete with computational cost. For iterative solvers, preconditioning aims to change the geometry of the problem seen by the iteration; stopping rules must still connect residuals to meaningful error or tolerance requirements.

The user of a solver need not rederive every pivot, but should understand the contract: does it estimate a backward error, a forward error, both, or neither? Does it know when the input is nearly singular? Does the reported precision reflect data uncertainty or only arithmetic convergence?

## The matrix is the problem; the factorization is the method

The tiny-pivot example shows an avoidable algorithmic failure on a modestly conditioned problem. Row swapping can prevent it. The near-dependent-equations example shows an unavoidable data-sensitivity issue: even excellent factorization cannot manufacture information the equations lack.

When someone says that a matrix calculation is accurate, ask two questions. How does the matrix map perturbations in the data into perturbations in the solution? And what nearby problem does the computed candidate solve? Numerical linear algebra becomes reliable when these questions are answered separately and then combined.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Tiny-pivot test.** Let \(\epsilon=10^{-20}\), \(A=\begin{bmatrix}\epsilon&1\\1&1\end{bmatrix}\), \(b=\begin{bmatrix}1+\epsilon\\2\end{bmatrix}\). Exact \(x=(1,1)\). The first unpivoted elimination multiplier is \(1/\epsilon=10^{20}\); partial pivoting instead swaps rows, giving multiplier \(\epsilon\). The matrix tends to \(\left[\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right]\) as \(\epsilon\to0\), which is nonsingular and has a moderate \(\kappa_2\).

**Residual and forward error.** For \(Ax_*=b\), \(r=b-A\hat x\), \(x_*-\hat x=A^{-1}r\). Therefore
\[
\|x_*-\hat x\|\le\|A^{-1}\|\|r\|,\quad
\frac{\|x_*-\hat x\|}{\|x_*\|}\le \kappa(A)\frac{\|r\|}{\|b\|}.
\]
This needs an invertible \(A\), \(b\ne0\), and compatible induced norms.

**Normwise backward error.** For \(\hat x\), with \(r=b-A\hat x\), \(\eta=\|r\|/(\|A\|\|\hat x\|+\|b\|)\). For a rigorous claim with a *computed* \(r\), include its rounding error.

**Normal equations.** For full-column-rank \(A\), least squares minimizes \(\|Ax-b\|_2\). Normal equations are \(A^\top A x=A^\top b\), and \(\kappa_2(A^\top A)=\kappa_2(A)^2\). QR uses \(A=QR\), with \(Q^\top Q=I\), and solves \(Rx=Q^\top b\).

**Partial-pivot growth.** A standard growth factor is \(\rho=\max_{i,j,k}|a_{ij}^{(k)}|/\max_{i,j}|a_{ij}|\), measured over the elimination stages \(k\). Rounding-error bounds for elimination with partial pivoting depend on this quantity.

### Exercises with answers

1. **Pivot:** Which first pivot should be chosen in the matrix of the tiny-pivot example? **Answer:** The entry one in the second row; swap rows first.
2. **Residual versus error:** If \(\|r\|=10^{-8}\) but \(\|A^{-1}\|=10^{10}\), what does the trivial bound say? **Answer:** It allows forward error as large as \(10^2\); a small residual alone does not prove accuracy.
3. **Least squares:** What happens to the 2-norm condition number in the normal equations? **Answer:** It squares, assuming full column rank.
4. **Certifying a residual:** Why might a residual computed in the same precision as the solve mislead? **Answer:** The residual computation itself may cancel or round, so an independent error bound or higher-precision evaluation is necessary.

### References

- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, lectures 6–11 and 20–23.
- James Demmel, *Applied Numerical Linear Algebra*, chapters 2–3.
- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, chapters 8–10.
