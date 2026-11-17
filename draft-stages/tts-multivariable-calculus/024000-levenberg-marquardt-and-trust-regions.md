# How Far Should We Trust a Fit? Damping and Levenberg–Marquardt

**Track:** Multivariable Calculus from First Principles. **Focus:** show why a plausible Gauss–Newton direction can fail, derive damped steps and trust-region acceptance, and distinguish step control from changing the fitted objective.

<!-- BEGIN SPOKEN LECTURE -->

# How Far Should We Trust a Fit? Damping and Levenberg–Marquardt

The Jacobian of a nonlinear model tells us how its predictions respond to very small parameter changes. Gauss–Newton takes that information and finds a correction that is optimal for the linearized residuals. Sometimes it proposes a small, sensible step. Sometimes it proposes a step so large that the original nonlinear predictions bear almost no resemblance to the linear approximation used to choose it.

A fitting algorithm needs more than a good direction. It needs a disciplined way to decide the length of the step and to recognize when its local prediction was wrong. This is the motivation behind damped least squares and the Levenberg–Marquardt family of methods. Their mathematics also leads naturally to trust regions, which compare predicted and actual improvement.

We will derive the damped equations rather than regard a damping parameter as an arbitrary button. Along the way we will distinguish three ideas that are often blurred: shrinking a trial step, regularizing a linearized correction, and imposing a lasting preference on the fitted parameters.

## A tangent that invites an enormous jump

Begin with one unknown x and one residual, x squared minus one. We seek to reduce one half the square of that residual. Its zeroes are plus one and minus one. Starting from x equal to one tenth, the residual is negative zero point nine nine, and its derivative is zero point two.

The Gauss–Newton linear model asks for a step p making negative zero point nine nine plus zero point two p equal to zero. It chooses p equal to four point nine five. The next x would be five point zero five.

But the actual residual there is five point zero five squared minus one, which is twenty-four point five zero two five. We started with a residual whose magnitude was less than one and ended with one whose magnitude exceeds twenty-four. The objective has increased from about zero point four nine to more than three hundred.

Nothing in the calculation was arithmetically wrong. The derivative at one tenth really is zero point two. The linear model would indeed reach zero at a step of four point nine five. The mistake is treating that first-order prediction as reliable over a displacement almost fifty times the size of the current position. The curvature of x squared is not remotely negligible over that interval.

The gradient at one tenth is nonzero and the Gauss–Newton direction is a descent direction, but the full step is disastrous. We need either a line search along that direction or a model that explicitly discourages giant corrections. We will focus on the second approach.

## Put a cost on the correction

For general residual vector r and Jacobian J, the original Gauss–Newton model is one half the squared length of r plus J p. Add a new term: one half times a positive damping number lambda times the squared length of the parameter correction p. We are now minimizing the local least-squares prediction while charging for a large move.

Differentiate the augmented model with respect to p. The new normal equations are J transpose J plus lambda times the identity matrix, all multiplying p, equals minus J transpose r.

For positive lambda, the coefficient matrix is positive definite, even if J has dependent columns. The local correction is uniquely defined. When lambda is small and J has full column rank, the correction approaches the ordinary Gauss–Newton step. When lambda is large, the inverse is approximately one over lambda times the identity, so the correction points roughly along the negative gradient and becomes small.

This interpolation explains the traditional association of Levenberg–Marquardt with both Newton-like and gradient-like behavior. But the exact direction depends on parameter scaling. One meter of a position parameter and one unit of a dimensionless calibration coefficient are not intrinsically comparable. Penalizing their raw squared changes as if they had the same units can make the algorithm's behavior depend on arbitrary parameter units.

A scaled version charges for the squared length of D p, where D is a nonsingular scaling matrix, often diagonal. The normal equations then contain lambda times D transpose D instead of lambda times the identity. The step norm is defined in scaled coordinates, and the interpretation of a large step reflects the chosen physical or numerical scales. A common practical scale is related to Jacobian column norms, but it needs safeguards for zero or tiny columns.

## Apply damping to the failing example

Return to the residual x squared minus one at x equal to one tenth. We calculated a residual of negative zero point nine nine and a derivative of zero point two. The Gauss–Newton normal-equation coefficient is zero point zero four, and the negative gradient is positive zero point one nine eight. With no damping, the step is four point nine five.

Now set lambda equal to one. The damped correction is zero point one nine eight divided by one point zero four, approximately zero point one nine zero four. The new x is about zero point two nine zero four, rather than five point zero five.

The actual residual is now about negative zero point nine one six. Its magnitude is smaller, and the objective has decreased. This particular choice of damping works, but another choice on another problem might not. Damping is not a proof of acceptance; it is a way to generate a more cautious candidate step.

A larger lambda would propose an even smaller move. Too much damping can be painfully slow, especially when the local linear model is actually excellent. A useful algorithm should therefore adjust its trust in the model as it learns from the results of trial steps. It should not simply make lambda large once and leave it there.

## The trust-region interpretation

Instead of adding a penalty, imagine making a geometric promise: we will only use the local model inside a ball of radius Delta in a chosen parameter scale. We minimize one half the squared length of r plus J p, subject to the scaled length of p being at most Delta.

This is the Gauss–Newton trust-region subproblem. If the unconstrained Gauss–Newton correction fits inside the ball, it is a candidate solution. If it would leave the ball, the constrained optimum lies on its boundary under ordinary nondegenerate conditions. A Lagrange multiplier for the squared-length constraint introduces the same matrix as damped least squares: J transpose J plus lambda D transpose D.

The multiplier lambda is nonnegative. It is zero when the trust-region constraint is inactive, with familiar qualifications about nonuniqueness. When the constraint is active, a positive multiplier can tune the solution to the radius. So a positive damped least-squares step can be interpreted as a trust-region solution for a corresponding radius. It is not correct to say that every implementation's update rule for lambda is exactly equivalent to an algorithm that solves a fixed-radius constrained subproblem at each iteration. The relationship is between the mathematical subproblems; practical algorithms add strategies for choosing radius, scaling, and acceptance.

There is another important subtlety. The added lambda term is a local charge for the correction from the current parameter vector. Unless it is retained as part of the outer objective, it is not a permanent statistical prior that the final parameters must be small. If the trust radius expands and lambda goes to zero near a good solution, the target remains the original sum of squared residuals. Later, when we discuss inverse problems, we will add a penalty to the parameters themselves and deliberately change the solution we are seeking. The similar-looking algebra should not obscure that conceptual difference.

## Compare prediction with reality

A trust-region method has a natural test. Before evaluating the nonlinear model at the proposed point, compute how much the local least-squares model predicts the objective will decrease. This is the model value at zero minus the model value at the proposed p. Next evaluate the actual objective after the step and compute the actual decrease.

When the predicted decrease is positive, form the ratio of actual decrease to predicted decrease. A ratio close to one means the local model described that step well. A ratio near zero means the model promised improvement but delivered almost none. A negative ratio means the true objective increased even though the local model predicted a decrease.

The trial step should be accepted or rejected using this comparison and the algorithm's chosen thresholds. If the model was poor, the method can shrink the radius and try again from the original parameter vector. If the model was accurate and the step reached the boundary, the radius may be enlarged. If the step was accurate but safely inside the radius, the current radius may already be sufficient.

Our x-squared example makes this concrete. The undamped Gauss–Newton step predicts that the local residual will become exactly zero. Its predicted decrease is the full initial objective, about zero point four nine. In fact, the actual objective jumps above three hundred, giving a strongly negative ratio. A trust-region acceptance test rejects the step rather than incorporating a disastrous move into the iterate history. The damped step near zero point one nine does not fit the model perfectly, but it produces genuine improvement and may be accepted.

Observe what is being tested: not whether the current parameters are close to a particular true parameter vector, which may be unknown, but whether this local model accurately predicts the change in the specified objective. Trust-region success is not proof that the model fits the real world, nor that the optimum found is global.

## A principled computational route

At each iterate, calculate the residual vector and its Jacobian. Choose a parameter scale. Solve a damped linear least-squares problem or a trust-region approximation. Compute the predicted reduction from the original linearized residual model, not merely from the penalty that was introduced to obtain the step. Evaluate the nonlinear residuals at the candidate point. Decide whether to accept it and how to adjust the radius or damping. Repeat.

For small dense models, a QR factorization or singular-value decomposition of the augmented least-squares system is often preferable to explicitly building and inverting J transpose J. The augmented system stacks J above the square root of lambda times D, and stacks minus r above a zero vector. It solves the same damped subproblem while avoiding an unnecessary squaring of the Jacobian's condition number. Sparse, large-scale problems have their own matrix-free approaches, but the mathematical idea is unchanged.

If the algorithm allows bounds on parameters, such as a strictly positive physical parameter, ordinary unconstrained Levenberg–Marquardt does not automatically enforce them. One may reparameterize, use a bound-aware trust-region method, or formulate a constrained problem. These strategies have different numerical and interpretive consequences. For example, changing a positive parameter to its logarithm makes the feasible set automatic but also changes the scale and geometry of steps.

Stopping rules also need interpretation. A tiny step might mean the algorithm has found a stationary point, but it might instead mean that lambda has become enormous or that parameters are badly scaled. A tiny change in the objective could indicate convergence or simply that the model is insensitive along the chosen directions. Gradient information, rank estimates, reduction ratios, and independent checks of the residual model help distinguish these situations.

## What damping buys, and what it does not

Damping gives a unique local correction when the undamped Jacobian is rank deficient, provided the damping matrix defines a positive-definite penalty. It may control wildly extrapolated steps. A trust-region acceptance rule gives a systematic test of whether the local approximation deserves to be believed over the proposed displacement.

None of these properties establishes that the data determine every parameter. Suppose the measurements depend only on the sum of two parameters. We can choose a damped step for those parameters, but no amount of step control can reveal how their sum should be divided between them. The algorithm may return a perfectly well-behaved numerical answer while the underlying inference problem still has infinitely many equally good explanations.

This is why the next mathematical question is not simply which optimizer converges fastest. It is which parameter combinations the data can actually identify. Singular values of the residual Jacobian will provide an answer, and they will show why a fitted parameter can have a large uncertainty even when a nonlinear solver reports an impressively small residual.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Damping and trust regions

At \(\theta\), let \(m(p)=\tfrac12\|r+Jp\|_2^2\), \(D\) nonsingular, \(\lambda>0\). The damped subproblem

\[
\min_p\ m(p)+\frac{\lambda}{2}\|Dp\|_2^2
\]

has unique minimizer satisfying

\[
(J^\top J+\lambda D^\top D)p=-J^\top r.
\]

It is equivalent to least squares with augmented matrix and right-hand side:

\[
\min_p\left\|
\begin{bmatrix}J\\\sqrt\lambda D\end{bmatrix}p+
\begin{bmatrix}r\\0\end{bmatrix}\right\|_2^2.
\]

The trust-region subproblem is \(\min m(p)\) subject to \(\|Dp\|_2\leq\Delta\). Its KKT equations include

\[
(J^\top J+\lambda D^\top D)p=-J^\top r,\qquad
\lambda\ge0,\quad \|Dp\|_2\le\Delta,\quad
\lambda(\|Dp\|_2^2-\Delta^2)=0.
\]

For a trial with \(m(0)>m(p)\), use \(\rho=[F(\theta)-F(\theta+p)]/[m(0)-m(p)]\). Numerator evaluates actual nonlinear residuals; denominator predicts only from the *undamped* linear residual model.

### Check the overshoot numerically

Let \(r(x)=x^2-1\), \(x=0.1\), \(J=0.2\), and \(F=\frac12r^2\).

- Undamped \(p=0.198/0.04=4.95\); \(x+p=5.05\), residual \(24.5025\), and \(F(x+p)\approx300.1863\), compared with \(F(x)=0.49005\).
- At \(\lambda=1\), \(p=0.198/1.04\approx0.190384615\), so \(x+p\approx0.290384615\) and \(F(x+p)\approx0.41923\). This step improves the objective but no single fixed \(\lambda\) is universally safe.

### Exercises with answers

1. **Large damping.** For fixed \(r,J\) and \(D=I\), show that the damped correction is \(-J^\top r/\lambda+O(\lambda^{-2})\) as \(\lambda\to\infty\). **Answer:** factor out \(\lambda\) from \((J^\top J+\lambda I)^{-1}\) and expand \((I+J^\top J/\lambda)^{-1}\) as a Neumann series for sufficiently large \(\lambda\).
2. **Singular Jacobian.** If \(J=[1\ \ 1]\), find the minimum-norm undamped correction satisfying \(Jp=-2\), then the damped solution with \(\lambda=1\). **Answer:** undamped minimum-norm \(p=(-1,-1)\). Damped \((J^\top J+I)p=(-2,-2)^\top\) gives \(p=(-2/3,-2/3)\).
3. **Trust prediction.** Why is the denominator of \(\rho\) based on \(m\), not \(m+\frac\lambda2\|Dp\|^2\)? **Answer:** the objective being minimized at the outer level is the original residual sum of squares; the penalty controls the proposed step rather than changing the goal. The ratio tests whether the *original* local model predicts that goal's behavior.
4. **Scaling.** If one parameter is measured in millimeters and re-expressed in meters, what must happen to its penalty weight to preserve the same step geometry? **Answer:** transform \(D\) under the change of variable so \(\|Dp\|\) is invariant; otherwise arbitrary units change the algorithm.

### Sources and further reading

- K. Madsen, H. B. Nielsen, and O. Tingleff, [*Methods for Non-Linear Least Squares Problems*](https://www2.imm.dtu.dk/pubdb/edoc/imm3215.pdf), §2.4 and §3.2.
- [SciPy `least_squares` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html), LM and trust-region-reflective solvers, scaling, rank limitations and stopping tests.
- [Wikipedia: Levenberg–Marquardt algorithm](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm), for orientation on damped normal equations.

*Teaching connections:* `multivariable-calculus:023000` derives Gauss–Newton; `multivariable-calculus:022000` proves local Newton bounds; `linear-algebra:021000` explains QR and least squares for the augmented problem.
