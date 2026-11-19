# What Does a Small Residual Prove? Conditioning, Backward Error, and Reliable Solves

**Track:** Linear Algebra from First Principles. **Background:** inverse matrices, vector norms, elimination, basic linear approximation. **Purpose:** derive quantitative error bounds and separate sensitivity of a mathematical problem from instability of an algorithm.

<!-- BEGIN SPOKEN LECTURE -->

# What Does a Small Residual Prove?

Imagine checking a numerical answer to a system of linear equations. We have the original matrix and right-hand side. We plug the computed vector into the equations and find that the mismatch is tiny. Is the computed solution accurate?

Not necessarily. There are two distinct questions hiding inside that one observation. Does the algorithm solve a nearby problem accurately? And if the problem's data change a little, does its answer change a little? The first question concerns backward error and algorithmic stability. The second concerns conditioning. A trustworthy calculation needs an answer to both.

We can derive this distinction without any detailed knowledge of how the computer implements matrix multiplication. Start with the exact equations and ask what they imply about mistakes.

## The exact relation between a residual and an error

Suppose A is an invertible square matrix, b is the right-hand side, and x star is the exact solution of A times x equals b. A numerical solver returns x hat. Define the residual r as b minus A times x hat. The residual measures the failure of x hat to satisfy the equations.

Subtract the two systems. Since A times x star equals b, A times x star minus x hat equals r. Apply the inverse matrix: the error x star minus x hat equals A inverse times r. This is an exact identity, not an estimate.

Taking lengths gives a bound. The error norm is at most the norm of A inverse times the residual norm, provided we use a compatible induced matrix norm. A small residual therefore gives a small error when the inverse has a moderate norm. If the inverse has a huge norm, the same residual may allow a large error.

The distinction is easiest to see in a family of two-by-two matrices. Let A have first row one, one and second row one, one plus delta, where delta is a small positive number. Its determinant is delta, so it is invertible whenever delta is positive, but it approaches a singular matrix as delta approaches zero.

Set b to be two, two plus delta. The exact solution is one, one. Now submit a deliberately wrong candidate: zero, two. Its first equation is satisfied exactly. In the second equation it predicts two plus twice delta instead of two plus delta. The residual is zero, negative delta. As delta shrinks, that residual goes to zero. But the difference between the proposed vector and the true vector stays negative one, one. Its length does not shrink at all.

The small residual is real. It simply does not establish the conclusion we wanted. The two equations are becoming nearly the same measurement. A large change in how the unknowns are divided between their two coordinates barely changes the observations.

## Measuring how the problem amplifies changes

A natural measure of sensitivity is the matrix condition number. For an invertible A, define it in an induced norm as the norm of A multiplied by the norm of its inverse. The first factor measures how strongly A can stretch a vector. The second measures how strongly recovering a vector from its image can stretch an error in the data.

In Euclidean length, this condition number is the largest singular value divided by the smallest singular value. Singular values measure how much a matrix stretches vectors along special mutually perpendicular directions. If one direction is almost crushed, then trying to recover a vector's component in that direction from its image will be sensitive to tiny observational mistakes.

For our nearly dependent two-by-two example, the infinity-norm condition number can be calculated exactly. It is the square of two plus delta, divided by delta. For small positive delta, this is approximately four divided by delta. Set delta equal to one hundredth. The condition number is a little over four hundred. That is not an accuracy guarantee or a count of lost digits; it is a worst-case sensitivity factor for relative changes in a particular norm.

To see the sensitivity directly, change only the second component of b by epsilon. Because the first equation still demands that the two unknowns sum to two, one unknown rises by epsilon divided by delta while the other falls by the same amount. If delta is one hundredth and epsilon is one thousandth, each component changes by one tenth. A one-thousandth change in one observation caused a tenth change in each parameter.

Conditioning depends on the mapping and on which data and outputs we care about. We must also state the norm, because different norms measure size differently. Rescaling variables and units changes matrix condition numbers unless we specify the corresponding weighted norms. A condition number is not a physical property divorced from representation and intended accuracy.

## Turn the residual into a relative error bound

The exact identity gives a usable relative estimate if b is nonzero. Divide the error by the length of the exact solution. Since the norm of b cannot exceed the norm of A times the norm of x star, we obtain a simple inequality: the relative solution error is at most the condition number times the residual length divided by the right-hand-side length.

This inequality makes the missing ingredient explicit. A residual that is tiny relative to b does not certify the solution if the condition number is enormous. Conversely, a moderate condition number and a rigorously known small relative residual yield a quantitative forward-error bound.

If both A and b are measured quantities, there is another effect. Suppose the true coefficients are perturbed as well as the right-hand side. The new solution satisfies the perturbed matrix times the perturbed solution equals the perturbed right-hand side. Subtracting the original system shows that the solution difference is driven by the right-hand-side change minus the coefficient change applied to the old solution. If the perturbation to A is small relative to the reciprocal of the inverse norm, we can bound the inverse of the perturbed matrix and derive a controlled relative-error estimate. The detailed inequality belongs in the written companion.

That hypothesis matters. An arbitrarily small-looking relative perturbation is not automatically harmless for a matrix whose condition number is enormous. It can move the matrix all the way to singularity.

## Backward error asks a different, often easier question

Given the approximate solution x hat, can we find a nearby right-hand side for which it is the exact solution? Yes, immediately. A times x hat equals b minus r. So it solves the problem with right-hand side b minus the residual. If the residual is small relative to b, the computed vector is the exact solution of a nearby right-hand-side problem.

A more flexible definition allows small changes in both A and b. We measure those changes relative to the sizes of the original data. A common normwise backward-error indicator is the residual norm divided by the sum of two quantities: the matrix norm times the length of x hat, and the length of b. Under standard induced-norm assumptions, it quantifies how small the permitted relative changes can be. A small value is evidence that the answer nearly satisfies a nearby input problem.

But backward error measures closeness of equations, not closeness of answers. Our example with x hat equal to zero, two has backward error approaching zero as delta approaches zero. Its forward error remains fixed. In fact, both observations follow from the same exact equations, without any contradiction.

An algorithm is called backward stable, in an appropriate setting, when its computed output is the exact solution to a nearby problem whose perturbation is controlled by rounding precision and modest problem-size factors. This is a stronger property than obtaining a small-looking answer. It is also a conditional statement: one must know the arithmetic model, the algorithm, and how any constants depend on dimension and pivot growth.

## Why stable LU and QR can still disagree in accuracy

Gaussian elimination with partial pivoting is widely useful, but its backward-error bounds depend on how much entries grow during elimination. Partial pivoting often controls that growth well in practice; it does not impose a small universal growth factor for every matrix. One must not turn an empirical expectation into an unconditional theorem.

Householder QR is attractive partly because its transformations preserve Euclidean norms. Under standard floating-point assumptions and with careful implementation, it has well-understood backward-stability properties. But a beautifully stable QR factorization applied to a fundamentally ill-conditioned least-squares problem will not recover information absent from the measurements.

Nor can changing algorithms make an infinite condition number finite for the same exact inversion task. Regularization, such as discarding very small singular directions, can produce a more stable answer, but it changes the inference. We must state the trade: a controlled bias or structural assumption replaces an attempt to recover data-sensitive components exactly.

## The residual itself must be computed

There is one final layer. A residual printed by a program is usually not the exact vector b minus A times x hat. It was computed using finite-precision arithmetic and may have rounding error or cancellation of its own. Recomputing the residual in higher precision, or bounding it with interval arithmetic, can make a diagnostic more credible.

Iterative refinement uses this observation constructively. First compute an approximate factorization and an initial solution. Then calculate a more accurate residual against the original system, solve a correction equation with the existing factors, and add the correction to the current answer. Repeat while the error indicators improve. Under appropriate conditioning, rounding and precision assumptions, refinement can recover accuracy that the initial solve did not show. It is not a magical remedy for every singular or extremely ill-conditioned system.

A numerical result should carry a little more information than its coordinates. We want to know which system was solved, what residual was checked, whether the estimated condition number makes that residual informative, and what arithmetic assumptions underlie the bounds. For a least-squares problem, we must also check the correct optimality conditions rather than demand that an inherently inconsistent system have a zero residual.

The mathematical point is concise. A residual says how closely a vector satisfies the equations. Conditioning says how strongly a change in equations may change the answer. Algorithmic stability says whether the computational procedure adds avoidable errors. Reliability comes from putting those three claims together, not from treating any one of them as a synonym for accuracy.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Residual-to-error estimate

Let \(A\in\mathbb R^{n\times n}\) be invertible, \(Ax_*=b\ne0\), and \(r=b-A\widehat x\). Then
\[
 x_*-\widehat x=A^{-1}r,\qquad
 \frac{\|x_*-\widehat x\|}{\|x_*\|}\le
 \kappa(A)\frac{\|r\|}{\|b\|},\qquad
 \kappa(A)=\|A\|\,\|A^{-1}\|.
\]
Both matrix norms must be induced by the chosen vector norms. The upper bound uses \(\|b\|\le\|A\|\|x_*\|\).

### Near-dependent family and concrete counterexample

\[
 A_\delta=\begin{bmatrix}1&1\\1&1+\delta\end{bmatrix},\quad
 b_\delta=\begin{bmatrix}2\\2+\delta\end{bmatrix},\quad
 x_*=(1,1)^T,\quad\widehat x=(0,2)^T.
\]
For \(\delta>0\), \(\det A_\delta=\delta\), \(r=(0,-\delta)^T\), \(\|x_*-\widehat x\|_2=\sqrt2\), and
\[
 A_\delta^{-1}=\frac1\delta
 \begin{bmatrix}1+\delta&-1\\-1&1\end{bmatrix},\qquad
 \kappa_\infty(A_\delta)=\frac{(2+\delta)^2}{\delta}.
\]
For \(b'=b+(0,\epsilon)^T\), the exact solution becomes \(x'=x_*+(-\epsilon/\delta,\epsilon/\delta)^T\). At \(\delta=.01\), \(\epsilon=.001\), the coordinate changes are \(\mp0.1\).

### Backward-error indicator and interpretation

For a nonzero \(A,b,\widehat x\), the standard normwise *joint* backward error under simultaneous, separately scaled bounds \(\|\Delta A\|/\|A\|\le\eta\) and \(\|\Delta b\|/\|b\|\le\eta\) is
\[
\eta=\frac{\|b-A\widehat x\|}{\|A\|\,\|\widehat x\|+\|b\|}.
\]
For Euclidean norms, a realizing perturbation can be constructed using a rank-one \(\Delta A\) aligned with \(r\widehat x^T\) and a \(\Delta b\) aligned oppositely with \(r\). The formula assumes the stated perturbation model and a mathematically evaluated residual. This is not automatically a certified bound for a rounded residual.

If \((A+E)(x_*+\Delta x)=b+f\), and \(\|A^{-1}E\|<1\), then
\[
\frac{\|\Delta x\|}{\|x_*\|}
\le \frac{\kappa(A)}{1-\kappa(A)\|E\|/\|A\|}
\left(\frac{\|f\|}{\|b\|}+\frac{\|E\|}{\|A\|}\right).
\]
The strict inequality \(\kappa(A)\|E\|/\|A\|<1\) is a convenient sufficient condition; it may be stronger than necessary.

### Arithmetic and scope

A conventional floating-point model is \(\mathrm{fl}(a\circ b)=(a\circ b)(1+\theta)\), \(|\theta|\le u\) for a correctly rounded elementary operation away from underflow/overflow and other exceptional cases. Error bounds for *algorithms* are derived from repeated such operations and may depend on dimension, scaling and pivot growth. QR can be backward stable while its least-squares **parameters** remain sensitive to perturbations in A or b.

### Exercises with answers

1. **Small residual trap:** What happens to \(\|r\|_2\) and \(\|x_* -\widehat x\|_2\) in the displayed example as \(\delta\to0^+\)? **Answer:** the former goes to zero, the latter remains \(\sqrt2\).
2. **Conditioning:** At \(\delta=.01\), compute \(\kappa_\infty(A_\delta)\). **Answer:** \((2.01)^2/.01=404.01\).
3. **Relative estimate:** If \(\kappa(A)=50\) and \(\|r\|/\|b\|=10^{-6}\), what forward-error bound follows? **Answer:** relative error at most \(5\times10^{-5}\), assuming the stated invertibility, norm and exact-residual hypotheses.
4. **Backward vs forward:** Does a backward error below machine epsilon imply a small forward error for every invertible A? **Answer:** no; an enormous condition number can amplify the permitted input change.

### Further reading and source connections

- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, second edition, SIAM, 2002, for backward-error analysis and refinement.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, SIAM, 1997, https://people.maths.ox.ac.uk/trefethen/text.html , for condition numbers and stability.
- James W. Demmel, *Applied Numerical Linear Algebra*, SIAM, 1997, for numerical error bounds and conditioning.
- Wikipedia topic pointers: [Condition number](https://en.wikipedia.org/wiki/Condition_number), [Numerical stability](https://en.wikipedia.org/wiki/Numerical_stability), [Iterative refinement](https://en.wikipedia.org/wiki/Iterative_refinement).

The broad distinctions also appear in `numerical-analysis:003000`, `numerical-analysis:004000`, and `numerical-analysis:006000`; this manuscript supplies a detailed counterexample and the quantitative derivations.
