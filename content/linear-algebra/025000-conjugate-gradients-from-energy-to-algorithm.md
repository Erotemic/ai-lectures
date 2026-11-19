# Conjugate Gradients: From a Quadratic Energy to a Working Algorithm

**Track:** Linear Algebra from First Principles. **Background:** positive-definite matrices, quadratic functions, inner products, matrix-vector products. **Purpose:** derive and execute conjugate gradients, explain conjugacy and the Krylov-subspace minimization principle, and separate exact-arithmetic guarantees from numerical stopping decisions.

<!-- BEGIN SPOKEN LECTURE -->

# Conjugate Gradients: From a Quadratic Energy to a Working Algorithm

A positive-definite matrix gives us two ways to think about solving A x equals b. We can regard it as an algebraic equation and use a factorization. Or we can regard its solution as the bottom of a strictly convex quadratic landscape. In the second view, every candidate x has an energy, and the residual tells us in which direction that energy is decreasing.

Conjugate gradients turns this geometric picture into a computational method. It needs only matrix-vector products, inner products, and a few stored vectors. For a large sparse system, that can be a decisive advantage over storing a Cholesky factor. But its apparent simplicity rests on a rather specific structure: A must be symmetric positive definite, or Hermitian positive definite in the complex case. We will see exactly where this assumption enters.

## A quadratic whose minimum solves the equation

Take the function f of x equal to one half x transpose A x minus b transpose x. If A is symmetric, its gradient is A x minus b. Thus the stationary points of f solve the desired equation. If A is positive definite, the energy has a unique minimum, not merely a stationary point. In fact, if x star is the exact solution, then the difference in energy between a candidate x and x star equals one half the squared error measured in the A norm.

The A norm of a vector e is the square root of e transpose A e. It weights directions according to the eigenvalues of A. A direction with a large eigenvalue incurs a larger energy penalty for the same ordinary Euclidean displacement. This is why a quadratic with very unequal eigenvalues looks like a narrow valley.

Let r be b minus A x. It is the negative gradient of f. Starting from any guess x, the most immediate idea is to move along r. That gives steepest descent. How far should we move? Substitute x plus alpha times r into f, differentiate with respect to alpha, and choose the minimum. The optimal step is the squared Euclidean length of r divided by r transpose A r.

That step is the best we can do along the chosen line. It is not necessarily the best next move overall. A steepest-descent step may produce a new residual that points almost back across a long, narrow valley, and the algorithm can zigzag. In exact arithmetic the residual after an optimal step is perpendicular to the direction just used, but orthogonality in the ordinary inner product does not prevent us from partially undoing older work in the A geometry.

## Directions that do not undo one another

Suppose we have two nonzero search directions p and q. Call them A-conjugate when p transpose A q equals zero. They are orthogonal under the inner product defined by A, although they need not be perpendicular in ordinary Euclidean space.

Why is that useful? If we change x along p, then the change in the quadratic energy has a cross term involving any other step direction q. When p and q are A-conjugate, that cross term vanishes. Once we have minimized along p, a later change along q does not disturb the minimization condition along p. This is the sense in which a conjugate direction preserves earlier progress.

If we could somehow produce n mutually A-conjugate directions in an n-dimensional space, we could minimize successively along each one and reach the exact solution in at most n steps in exact arithmetic. Constructing all those directions by full Gram–Schmidt with the A inner product would be expensive. Conjugate gradients discovers a remarkable short recurrence that constructs what it needs from the current residual, the current direction, and one matrix-vector product.

## The recurrence, and why its fractions appear

Start with x zero, an initial guess. Compute r zero equal to b minus A x zero, and set the first search direction p zero equal to r zero. At each step, choose alpha equal to the squared norm of the residual divided by p transpose A p. Update x by adding alpha times p. Update the residual by subtracting alpha times A p. Then construct the next direction by adding the new residual to beta times the old search direction, where beta is the squared length of the new residual divided by the squared length of the old one.

Those formulas are not magic constants. The numerator in alpha expresses how much the current residual aligns with a suitable conjugate search direction. The denominator measures the curvature of the quadratic along that direction. The beta coefficient corrects the new residual so that the new direction is A-conjugate to the previous one. In exact arithmetic, the recurrence also preserves conjugacy with all the earlier directions because of the orthogonality relations generated by the method.

There are several mathematically equivalent ways to write conjugate-gradient recurrences in exact arithmetic. The one we are using is the standard residual-norm form for symmetric positive-definite A. Every denominator involving p transpose A p is strictly positive when p is nonzero. That is exactly where positive definiteness protects the algorithm from division by zero or a negative curvature step.

## Solve a two-dimensional system without a factorization

Let A be diagonal with entries one and two. Let b be the vector one, one, and start from x zero equal to zero. The exact answer is one, one half, but we will let the algorithm discover it.

The first residual and first direction are both one, one. Their squared length is two. Applying A to the direction gives one, two. The curvature p transpose A p is three. So alpha zero equals two thirds. The first iterate is two thirds, two thirds. Its residual is one third, negative one third. Notice that this residual is perpendicular to the first direction: the two components cancel when we take their dot product.

The new residual has squared length two ninths. Dividing by the original squared length, two, gives beta one equal to one ninth. Add one ninth of the old direction to the new residual. The second search direction becomes four ninths, negative two ninths. Apply A and we get four ninths, negative four ninths. Its dot product with the original direction is zero. That is conjugacy, not merely ordinary perpendicularity.

The second step size is three fourths. Add three fourths of the new direction to the first iterate. The result is exactly one, one half. The new residual is zero. We have solved the two-variable system in two iterations with vector operations and no inverse or stored matrix factor.

For this tiny example, Cholesky would be just as easy. The point is the structure. In a million-dimensional sparse system, computing A times a vector may be fast, while a direct factorization can generate many new nonzero entries. Conjugate gradients can exploit sparse matrix-vector multiplication without constructing the fill-producing factors.

## The Krylov space is what the algorithm has searched

Consider the initial residual r zero and the vectors obtained by repeatedly applying A: r zero, A r zero, A squared r zero, and so forth. The span of the first k such vectors is called a Krylov subspace. Every conjugate-gradient iterate after k steps lies in the initial guess plus this subspace. More strongly, among all candidates in that affine space, it minimizes the quadratic energy. Equivalently, it minimizes the error in the A norm.

This characterization is more informative than a formula for updating x. The method is finding the best candidate among a growing family of polynomial corrections. The error after k steps can be written as a polynomial in A applied to the initial error. The polynomial has degree at most k and takes the value one at zero. Its task is to become small on the eigenvalues of A, because those eigenvalues control the action of the polynomial on the error.

For a positive-definite matrix there are no zero eigenvalues, so such a polynomial can eventually vanish on the finite collection of distinct eigenvalues. If the matrix has only a few distinct eigenvalues, exact arithmetic can give exact convergence in fewer than n iterations. Otherwise, n is a general upper bound on the number of steps in exact arithmetic, absent an earlier zero residual.

The polynomial perspective also explains the familiar condition-number convergence estimate. If every eigenvalue lies between a positive minimum and maximum and kappa is their ratio, a carefully chosen polynomial based on Chebyshev polynomials gives an A-norm error bound involving the factor square root of kappa minus one, divided by square root of kappa plus one, raised to the iteration count. The standard bound includes a factor of two. A kappa near one predicts rapid convergence; a large kappa makes the worst-case estimate slow.

That bound is a guarantee, not a schedule. Actual convergence can be much faster when the eigenvalues cluster, because the error polynomial can be small on those clusters without being small everywhere in the interval between the extreme eigenvalues.

## What preconditioning changes

Suppose A is positive definite but very ill-conditioned. We might find a simpler positive-definite matrix M that approximately represents A yet is cheap to solve against. In preconditioned conjugate gradients, the residual is transformed using M inverse. A symmetric change of variables shows that, under the positive-definite assumptions, the method corresponds to applying ordinary conjugate gradients to the transformed matrix M to the minus one-half times A times M to the minus one-half.

The ideal preconditioner would make the transformed eigenvalues close to one, or at least cluster favorably. But applying the preconditioner has a cost. A dense exact factorization of M could erase the savings we hoped to gain from iteration. Incomplete Cholesky, diagonal scaling, multigrid and other techniques instead trade setup, storage, and approximation quality against convergence speed. An incomplete factorization may need safeguards to remain usable and positive definite.

The important distinction is between two kinds of improvement. A better algorithm can make each step cheaper, while a better preconditioner can reduce how many steps are needed. Both matter in assessing the real total computational work.

## The limit of the exact-arithmetic story

Real machines do not maintain perfect A-conjugacy and orthogonality. Rounding errors accumulate. The residual tracked recursively by subtracting alpha times A p can drift away from the residual recomputed directly as b minus A x. Exact termination in at most n steps is therefore not a realistic promise of perfect accuracy after n floating-point steps. In practice we monitor the true residual, scaling, conditioning, and the requirements of the application.

A small residual alone is still not a forward-error guarantee. If A has a very small eigenvalue, an error along that direction can produce a small residual. Our earlier discussion of conditioning applies unchanged. A solver should be judged against a meaningful accuracy criterion, not merely whether an iteration counter stopped.

Also, do not apply these recurrences to arbitrary nonsymmetric or indefinite matrices just because they produce numbers. Without positive definiteness, p transpose A p can vanish or fail to represent positive curvature; the energy-minimization proof collapses. Other Krylov methods, including MINRES for suitable symmetric indefinite problems and GMRES for general nonsymmetric ones, have different algebra and guarantees.

## A new way to solve a familiar equation

Conjugate gradients is an unusually clear example of geometry producing an algorithm. A positive-definite matrix defines an energy and an inner product. Those produce noninterfering directions. The directions produce a short recurrence. The recurrence searches a growing polynomial space and gives concrete convergence estimates.

The method is most valuable when the cost of multiplying by A is small compared with storing a direct factorization. Its limitations are equally instructive: it depends on the problem's symmetry and positivity, on a good error criterion, and often on a carefully chosen preconditioner. Numerical linear algebra is not a collection of formulas divorced from assumptions. Its algorithms are theorems made computational.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Energy identity and minimization

For real SPD \(A\), let \(x_*=A^{-1}b\), \(e=x-x_*\), and
\[
f(x)=\tfrac12x^TAx-b^Tx.
\]
Then \(\nabla f(x)=Ax-b\) and
\[
f(x)-f(x_*)=\tfrac12 e^TAe=\tfrac12\|e\|_A^2.
\]
Positive definiteness ensures uniqueness and makes \(\langle u,v\rangle_A=u^TAv\) an inner product. For \(p\ne0\), line minimization gives
\[
\alpha=\frac{p^T(b-Ax)}{p^TAp}.
\]
CG maintains \(p_k^Tr_k=r_k^Tr_k\) in exact arithmetic, giving the standard recurrence below.

### Conjugate-gradient recurrence (SPD, exact arithmetic)

\[
\begin{aligned}
r_0&=b-Ax_0, &p_0&=r_0,\\
\alpha_k&=\frac{r_k^Tr_k}{p_k^TAp_k},
&x_{k+1}&=x_k+\alpha_kp_k,\\
r_{k+1}&=r_k-\alpha_kAp_k,
&\beta_{k+1}&=\frac{r_{k+1}^Tr_{k+1}}{r_k^Tr_k},\\
p_{k+1}&=r_{k+1}+\beta_{k+1}p_k.
\end{aligned}
\]
If \(r_k=0\), stop before computing the next ratio. In exact arithmetic the residuals are mutually orthogonal, and \(p_i^TAp_j=0\) for \(i\ne j\). The CG iterate minimizes \(f\) over \(x_0+\mathcal K_k(A,r_0)\), where
\[
\mathcal K_k(A,r_0)=\operatorname{span}\{r_0,Ar_0,\ldots,A^{k-1}r_0\}.
\]

### Two steps with exact fractions

\[
A=\operatorname{diag}(1,2),\quad b=(1,1)^T,\quad x_0=(0,0)^T.
\]
\[
\begin{array}{c|c|c|c}
k&r_k&p_k&\alpha_k\\\hline
0&(1,1)&(1,1)&2/3\\
1&(1/3,-1/3)&(4/9,-2/9)&3/4
\end{array}
\]
\(\beta_1=1/9\). The iterates are \(x_1=(2/3,2/3)^T\) and \(x_2=(1,1/2)^T\). Check \(p_0^TAp_1=(1,1)\cdot(4/9,-4/9)=0\).

### Spectral-polynomial view and condition bound

In exact arithmetic \(e_k=p_k(A)e_0\) for a polynomial \(p_k\) of degree at most k satisfying \(p_k(0)=1\). Since A is SPD and unitarily diagonalizable,
\[
\|e_k\|_A\le \min_{\substack{p(0)=1\\\deg p\le k}}
\max_{\lambda\in\sigma(A)}|p(\lambda)|\,\|e_0\|_A.
\]
Chebyshev polynomials on \([\lambda_{\min},\lambda_{\max}]\) yield
\[
\|e_k\|_A\le2\left(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\right)^k\|e_0\|_A,
\qquad\kappa=\lambda_{\max}/\lambda_{\min}.
\]
The inequality is often pessimistic for clustered spectra and does not incorporate finite-precision loss of conjugacy.

### Preconditioning

For SPD \(M\), the symmetric transformed matrix is \(\widetilde A=M^{-1/2}AM^{-1/2}\succ0\). Standard PCG applies \(z_k=M^{-1}r_k\) using solves, not an explicit inverse; \(\widetilde A\)'s spectral spread governs the usual idealized bound. Neither \(M\) nor \(A\) must be assembled densely when efficient operators are available.

### Exercises with answers

1. **Energy:** Show \(x_*\) uniquely minimizes \(f\). **Answer:** \(f(x)-f(x_*)=\frac12\|x-x_*\|_A^2>0\) when \(x\ne x_*\).
2. **First step:** For the displayed diagonal example, calculate \(x_1\) and \(r_1\). **Answer:** \(x_1=(2/3,2/3)^T\), \(r_1=(1/3,-1/3)^T\).
3. **Conjugacy:** Verify \(p_0^TAp_1=0\). **Answer:** \(4/9-4/9=0\).
4. **Exact termination:** If an SPD matrix has only two distinct eigenvalues, how many CG steps suffice in exact arithmetic? **Answer:** at most two from any starting guess, absent earlier convergence, because a polynomial of degree two vanishing at both eigenvalues gives zero error.
5. **Method selection:** Why is a cheap sparse matvec insufficient to justify CG for a nonsymmetric system? **Answer:** the SPD energy, positive denominators and conjugacy/minimization guarantees may fail; choose a method for the actual operator class.

### Sources and reading

- Yousef Saad, [*Iterative Methods for Sparse Linear Systems*, second edition](https://www-users.cse.umn.edu/~saad/books.html), for Krylov methods, PCG, stopping criteria and sparse preconditioning.
- Lloyd N. Trefethen and David Bau III, [*Numerical Linear Algebra*](https://people.maths.ox.ac.uk/trefethen/text.html), for the polynomial/CG view and spectral estimates.
- James W. Demmel, [*Applied Numerical Linear Algebra*](https://doi.org/10.1137/1.9781611971446), for conditioning and scientific computation.
- Wikipedia topic pointers: [Conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method), [Krylov subspace](https://en.wikipedia.org/wiki/Krylov_subspace), [Preconditioner](https://en.wikipedia.org/wiki/Preconditioner).

`numerical-analysis:010000` already introduces iterative solvers and their residual logic. This lecture supplies the energy identity, short recurrence, complete exact CG trace, polynomial minimization and SPD-specific derivation.
