# Why Newton Converges: Remainders, Basins, and Safeguards

**Track:** Multivariable Calculus from First Principles. **Focus:** prove local quadratic convergence with visible constants, exhibit a failure away from the root, and explain how damping and inexact solves alter the guarantee.

<!-- BEGIN SPOKEN LECTURE -->

# Why Newton Converges: Remainders, Basins, and Safeguards

Newton's method can appear almost magical. A handful of iterations often turns a rough guess into many correct digits. It can also oscillate forever between two guesses or attempt a step at which the derivative matrix is singular. The same formula produces both behaviors.

A theorem about Newton's method must therefore be local and conditional, unless extra safeguards and global assumptions are supplied. We will prove a version with explicit constants, see exactly where each hypothesis enters, and then compare the proof with the failures that occur outside its scope.

## What quadratic convergence actually says

Let x star be an exact solution of a nonlinear system F of x equals zero. Suppose an iteration produces points x zero, x one, and so on. Write e k for the distance from x k to x star.

A sequence converges quadratically in the usual error-bound sense if, once it is close enough, each new error is bounded by a fixed constant times the square of the preceding error. This is much stronger than a fixed fraction reduction. If the error is about one hundredth and the constant is moderate, its square is around one ten-thousandth. The next squaring can produce a number around one hundred millionth, and the effect accelerates.

But it is not correct to say that every Newton iteration doubles the number of correct decimal digits. The constants, norm, proximity to the target, and arithmetic accuracy matter. Quadratic convergence is an asymptotic relation between errors under hypotheses, not a universal timer or a promise that every early step is spectacular.

We will use Euclidean distance and a compatible operator norm for matrices. The reasoning works with other consistent norms, but changing the norm changes some numerical constants.

## The theorem and its neighborhood

Assume F maps an open region of n-dimensional real space to n-dimensional real space, is continuously differentiable, and has a root x star. Suppose there is a closed ball centered at x star, contained in that open region, with three properties.

First, every Jacobian matrix in the ball is invertible. Second, the norm of each Jacobian inverse is at most a fixed number B. Third, the Jacobian is Lipschitz in the ball: the norm of the difference between Jacobians at two points is at most L times the distance between those points.

The ball must be convex, as an ordinary Euclidean ball is, so the segment between the current iterate and the root stays in the region of control. If the radius is r, choose it small enough that B times L times r divided by two is less than one.

Then the full Newton iteration, started anywhere in this ball, remains in the ball and converges to x star. More precisely, after each step the new distance to x star is no more than B times L over two times the square of the previous distance. In particular, if we start strictly inside the stated radius, the sequence approaches the root at least quadratically in this bound.

These are sufficient conditions, not necessary ones. Newton can converge in settings outside this theorem. The point of the theorem is to show why controlled change of the Jacobian and a bounded inverse together create the square in the error estimate.

## The proof: cancel the linear part and bound what remains

Let x be the current point and let e be the displacement from the root x star to x. In symbols, x equals x star plus e. The exact root equation says F at x star is zero.

Now compare F at x with its linear prediction using the Jacobian at x. Follow the straight segment from x star to x. The fundamental theorem of calculus tells us that the difference F of x minus F of x star is the integral of the Jacobian along this segment, applied to e.

If the Jacobian were constant, that integral would equal the Jacobian at x times e, and one Newton step would eliminate the error exactly. But the Jacobian changes. Subtract the constant-Jacobian expression from the integral. The leftover is an average of the difference between the Jacobian at the current point and the Jacobian at an intermediate point, applied to e.

At a fraction t of the way from the root toward x, the distance back to x is one minus t times the length of e. The Lipschitz condition therefore bounds the Jacobian difference by L times one minus t times the error length. Applying it to e contributes another factor of the error length. Integrating one minus t from zero to one gives one half. So the linearization residual is at most L over two times the squared distance from x to the root.

Newton's update subtracts the inverse Jacobian at x multiplied by F at x. Algebraically, the new displacement from the root is the inverse Jacobian times exactly that linearization residual, with the appropriate sign. Multiplying our residual bound by the inverse norm bound B gives the promised estimate: new error at most B L over two times old error squared.

That is the entire mechanism. One factor of the error comes from moving a distance e. The second comes from how much the Jacobian varies over that movement. The inverse bound prevents the linear solve from magnifying the remaining discrepancy without limit.

Finally, why does the iteration stay inside the ball? If the present error is at most r, the bound says the new error is at most B L r over two times the present error. Our radius condition makes that multiplying factor strictly less than one. Therefore the distance shrinks and remains below r. Repeating the argument yields a decreasing sequence of errors tending to zero.

The proof has simultaneously established convergence, a region of attraction, and a rate. It did not require us to assert vaguely that Newton works when the initial guess is good enough; it said which properties make that phrase meaningful.

## A one-variable model with an exact squared error

Consider the function f of a positive variable x equal to x minus the natural logarithm of x. Its derivative is one minus one over x, and its second derivative is one over x squared. Its unique minimizer is x equal to one.

Apply optimization Newton to the derivative equation. The correction is minus the first derivative divided by the second derivative. After simplifying, the next iterate is two x minus x squared.

Write the present error as x minus one. The next error is exactly minus the square of the present error. Not approximately; exactly. If we start at x equal to one point two, the error is positive zero point two. One step moves to zero point nine six, with error negative zero point zero four. Another moves to zero point nine nine eight four, with error negative zero point zero zero one six. The squaring is visible without an asymptotic argument.

The example also exposes a basin boundary. If we start with x strictly between zero and two, the next iterate is positive and at most one; the error subsequently squares toward zero. Start with x greater than two, however, and two x minus x squared is negative. The new point is outside the function's domain. A formula with perfect local quadratic convergence can still be globally unusable without a step safeguard.

## A simple two-cycle that never converges

For a failure in root finding, consider the scalar equation x cubed minus two x plus two equals zero. Its derivative is three x squared minus two. Start Newton at zero. The function is two and the derivative is minus two, so the correction is plus one. The next guess is one.

At one, the function is one and the derivative is one, so the correction is minus one. We return to zero. Repeat, and the same two values alternate forever. Neither is a root.

There is a real root elsewhere, between minus two and minus one. The cycling demonstrates that a root's existence and differentiability of the function are not enough for global convergence from an arbitrary starting guess. The local theorem does not apply because we are not staying inside a controlled neighborhood of that root.

This example matters in higher dimensions as well. There, the basin can have complicated geometry, multiple roots may compete, and the Jacobian can become ill-conditioned in ways that are hard to see from a scalar plot. A numerical solver should report what it checked, not merely how many iterations it ran.

## How the theorem changes for minimization

For minimizing a twice differentiable scalar objective, apply the root theorem to F equal to the gradient. Its Jacobian is the Hessian. A local quadratic-convergence theorem for optimization therefore asks for a Hessian that remains invertible and varies in a Lipschitz-controlled way near a stationary point.

To know the stationary point is a strict local minimum, we add positive definiteness of the Hessian at the target. By continuity, the Hessian stays positive definite in a sufficiently small neighborhood, and its inverse is bounded there. If the Hessian is also Lipschitz on that neighborhood, the same proof gives quadratic convergence of full Newton steps started sufficiently close to the minimizer.

The conclusion must not be reversed. Quadratic convergence to a stationary point alone does not prove that point is a minimum; Newton can converge to a saddle. Positive definiteness supplies the local optimization interpretation. Global convexity or another global certificate is needed for broader claims about a global optimum.

An extra complication is that optimization Hessians are frequently indefinite far from a minimizer. In that region a Newton direction may not decrease the objective. Changing the direction, regularizing the Hessian, or using a trust-region formulation can be necessary before a line search even makes sense as a descent safeguard.

## Backtracking: earn the right to take a long step

Suppose we have found a direction p with negative directional derivative of f at x. That means the gradient dotted with p is negative. The ordinary derivative test guarantees that small enough positive movements along p decrease the objective, because the first-order term dominates for sufficiently small step lengths.

Backtracking line search turns that local observation into a procedure. Begin with a proposed step length of one. Test the new objective value against a prescribed fraction of the linear predicted decrease. If the test fails, multiply the step length by a number between zero and one and try again. Continue until the decrease condition holds.

A common test is called the Armijo condition. The right-hand side is the old objective plus a positive fraction, smaller than one, of the step length times the negative directional derivative. The test requires genuine decrease, not merely a better prediction by the model.

If the gradient is Lipschitz near the path with constant M, the descent lemma bounds the actual objective above by the linear prediction plus M over two times the squared step length times the squared direction norm. Consequently sufficiently small steps satisfy the Armijo test. This is a mathematical explanation for why backtracking terminates when the direction is truly descending and the local smoothness conditions hold.

A line search does not automatically establish convergence to a global minimum. That requires further hypotheses about the objective, the directions, and how much progress is made. Nor does the Armijo test apply unchanged to a Newton direction that is not descending. The purpose of damping is to connect a good *local* direction to actual observed improvement.

Once Newton enters a sufficiently well-behaved neighborhood of a strict local minimizer, a full step may pass the line-search test, and the rapid local rate can resume. A practical strategy often combines conservative progress farther away with fast quadratic steps near a solution.

## What if the linear solve is not exact?

In large systems, it may be wasteful to solve each Newton linear system to nearly machine precision, especially early in the outer iteration. Suppose we compute a correction p that leaves a linear residual r: the Jacobian times p plus F equals r, rather than zero.

Redo the convergence proof. The new error now has two contributions. The nonlinear model error is bounded by the constant B L over two times the old error squared. The imperfect linear solve adds at most B times the norm of r. Thus a quadratic local bound for the outer iteration survives if the inner linear residual shrinks on the order of the square of the current error.

If the inner residual is only a fixed fraction of the current nonlinear residual, the second contribution is generally first order in the current error. We may still converge, but we should not claim the exact quadratic rate. This observation motivates adaptive forcing tolerances: solve the inner system loosely when far away, then tighten it as the nonlinear residual becomes small.

This distinction is critical when connecting mathematics to software. An algorithm written with an exact inverse is not automatically an algorithm implemented with approximate sparse solves. A complete numerical claim must account for the accuracy of those solves and for finite-precision arithmetic.

## What is actually certified after an iteration?

There are several different questions we may ask of the final point. Is the residual small? Is the Jacobian well-conditioned? Is the point close to a genuine root? Has the objective decreased? Is a stationary point a minimum? Are we within a proven convergence neighborhood?

These are not interchangeable questions. A small residual may coexist with large forward error when the derivative is nearly singular. A small gradient may indicate a flat region rather than proximity to a minimizer. Decreasing an objective does not guarantee finding its global minimum. Local quadratic convergence is a statement about the sequence near a particular nondegenerate solution, not an after-the-fact certificate from one small number.

The strength of Newton's method lies in how much structure it captures with one local linear solve. The strength of its mathematics lies in making that structure accountable. Taylor remainders control the nonlinear part, inverse bounds control the linear correction, and step safeguards test whether a local model has earned our trust. Those three ingredients connect basic calculus to the algorithms used in nonlinear systems, optimization, and numerical simulation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Local quadratic-convergence theorem and proof

Assume \(F(x_*)=0\), \(F\in C^1\) on an open region containing the closed ball \(B_r(x_*)\), \(J=DF\) is \(L\)-Lipschitz on the ball, \(J(x)\) is invertible throughout it, and \(\|J(x)^{-1}\|\le B\). Set \(C=BL/2\), and choose \(Cr<1\). For \(e=x-x_*\),

\[
F(x)-F(x_*)=\int_0^1J(x_*+te)e\,dt.
\]

The full Newton update \(N(x)=x-J(x)^{-1}F(x)\) obeys

\[
N(x)-x_*=J(x)^{-1}\int_0^1[J(x)-J(x_*+te)]e\,dt,
\]
\[
\|N(x)-x_*\|\le BL\|e\|^2\int_0^1(1-t)\,dt
=\frac{BL}{2}\|e\|^2.
\]

Hence \(\|e_{k+1}\|\le C\|e_k\|^2\le Cr\|e_k\|\) and all iterates remain in the ball. With \(Cr<1\), the errors tend to zero and satisfy a quadratic bound. To establish the neighborhood from a nonsingular \(J(x_*)\), continuous invertibility supplies a bounded inverse on a small ball, while Lipschitz continuity of \(J\) on that ball gives \(L\).

### Domain-sensitive scalar example

For \(f(x)=x-\log x\), \(x>0\),

\[
f'(x)=1-1/x,\qquad f''(x)=1/x^2,\qquad
N(x)=x-\frac{f'(x)}{f''(x)}=2x-x^2.
\]

Thus \(N(x)-1=-(x-1)^2\). If \(0<x<2\), then \(0<N(x)\le1\), and subsequent iterates tend to \(1\); if \(x>2\), the full step leaves the domain. Exact cycle example for \(F(x)=x^3-2x+2\): \(N(0)=1\), \(N(1)=0\).

### Armijo and inexact Newton estimates

For a descent direction \(g^Tp<0\) and \(M\)-Lipschitz gradient along the candidate segment,

\[
f(x+\alpha p)\le f(x)+\alpha g^Tp+\frac M2\alpha^2\|p\|^2.
\]

For Armijo parameter \(c\in(0,1)\), the sufficient condition

\[
0<\alpha\le\frac{2(1-c)(-g^Tp)}{M\|p\|^2}
\]

guarantees \(f(x+\alpha p)\le f(x)+c\alpha g^Tp\). If \(M=0\), the quadratic remainder term vanishes and every step within the domain satisfies the sufficient inequality for a descent direction.

For an inexact correction \(J(x)p=-F(x)+r\),

\[
\|x+p-x_*\|\le \frac{BL}{2}\|x-x_*\|^2+B\|r\|.
\]

The rate depends on how \(\|r\|\) scales with the outer error. In particular, \(\|r\|=O(\|x-x_*\|^2)\) preserves the local quadratic error bound. Near a simple root, \(\|F(x)\|\) and \(\|x-x_*\|\) are locally comparable, so \(\|r\|=O(\|F(x)\|^2)\) is a practical sufficient forcing rule.

### Exercises with solutions

1. **Proof constant.** Where does the factor one half in the Newton error bound arise? **Answer:** from integrating \(1-t\) along the segment connecting the root and the iterate.
2. **Basin.** What happens to \(f(x)=x-\log x\) when Newton starts at \(x=3\)? **Answer:** \(N(3)=6-9=-3\), leaving the domain \(x>0\); local quadratic convergence does not ensure a safe full step.
3. **Two-cycle.** Verify the Newton updates for \(F(x)=x^3-2x+2\). **Answer:** \(F(0)=2\), \(F'(0)=-2\), so \(N(0)=1\); \(F(1)=1\), \(F'(1)=1\), so \(N(1)=0\).
4. **Armijo.** Let \(g^Tp=-2\), \(\|p\|=1\), \(M=4\), and \(c=1/4\). Find a sufficient positive step bound. **Answer:** \(\alpha\le2(3/4)(2)/4=3/4\).
5. **Inner accuracy.** If \(\|r_k\|\le0.1\|F(x_k)\|\) with a fixed factor, why is quadratic convergence not guaranteed by the displayed bound? **Answer:** the residual term generally scales like the first power of the distance to the root, potentially dominating the quadratic term.

### Sources and reading

- [Stanford CME307/MS&E311, Lecture 12: Local Convergence Theorem of Newton's Method](https://web.stanford.edu/class/msande311/lecture12.pdf), a local Newton argument and sensitivity assumptions.
- [Boyd and Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), Chapter 9, line search and local Newton convergence.
- [MIT 6.854 notes on Newton's method](https://courses.csail.mit.edu/6.854/18/Notes/n19-newton_method.html), practical and theoretical contrasts.
- [MIT 6.7220/15.084 lecture notes: Self-concordant functions](https://www.mit.edu/~gfarina/2025/67220s25_L19_self_concordance/L19.pdf), an example with exact squared error and limits of Lipschitz-Hessian assumptions.
- [Wikipedia: Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method) and [Backtracking line search](https://en.wikipedia.org/wiki/Backtracking_line_search), supplementary orientation.

This proof route connects `multivariable-calculus:019000`, `multivariable-calculus:020000`, and `multivariable-calculus:021000` to `optimization-duality:005000` and `numerical-analysis:005000`. It is a local theorem, not a global optimality or finite-precision correctness certificate.
