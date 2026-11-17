# Active Inequalities: Feasible Directions, Complementarity, and Critical Cones

**Track:** Multivariable Calculus from First Principles. **Focus:** build the local geometry of inequalities, calculate multipliers and critical directions, and distinguish valid active-set calculations from switches and degeneracy.

<!-- BEGIN SPOKEN LECTURE -->

# Active Inequalities: Feasible Directions, Complementarity, and Critical Cones

Suppose we are trying to fit two nonnegative quantities into a budget that allows their sum to be at most one. At a candidate solution, some restrictions may be tight while others have room to spare. If the sum is already one, a small increase in both quantities is forbidden. If one quantity is already zero, decreasing that coordinate is forbidden too. But increasing it may be permitted if the other coordinate decreases enough.

The directions available to us now form something more complicated than the tangent space to an equality constraint. A tangent space lets us move in both directions along a line. An inequality boundary ordinarily permits motion to one side but not the other. The local object is a cone of feasible velocities. Its shape changes when constraints become active or inactive.

In a convex optimization survey, the Karush–Kuhn–Tucker conditions provide elegant optimality certificates. Here our question is more constructive: when we write those conditions for a nonlinear model, what directions do they describe, what second derivative should we test, and what happens to a numerical algorithm when the active set changes?

## Distinguish active from inactive constraints

Write each inequality as g of x less than or equal to zero. A constraint is active when its value is exactly zero. Otherwise it is inactive, with negative slack. At an inactive constraint, a sufficiently small perturbation leaves it satisfied, so its first derivative need not restrict the local direction. At an active one, however, a feasible path starting at the point cannot initially increase g. Therefore its velocity d must satisfy the gradient of g dotted with d less than or equal to zero.

Equality constraints still demand zero first-order change. Together, the equality tangent equations and the active inequality half-spaces define a linearized cone. In a well-behaved problem, this cone accurately describes first-order feasible motions. In a singular problem it may exaggerate them, exactly as the zero derivative of x squared failed to describe the one-point feasible set.

To find a constrained minimum, start with the simple directional test: the objective cannot decrease to first order along any truly feasible direction. Thus its gradient dotted with a feasible velocity is nonnegative. If we can express all these inequalities through a finite collection of active constraint normals, we get multipliers. For the convention g less than or equal to zero, those inequality multipliers must be nonnegative. Equality multipliers remain unrestricted in sign.

Stationarity says the objective gradient plus the weighted gradients of equality and inequality constraints sum to zero. Complementarity says each inequality multiplier multiplied by the corresponding constraint value is zero. An inactive constraint therefore has multiplier zero. But the reverse is not guaranteed: an active constraint can have multiplier zero. The distinction between a binding equation and a positive multiplier becomes crucial in sensitivity calculations.

## Compute a two-variable example

Let the objective be one half the squared distance from the target point with coordinates two and negative one. In ordinary notation, we minimize half of the sum of x minus two squared and y plus one squared. Constrain x and y to be nonnegative and their sum to be at most one.

The unconstrained target lies outside the feasible triangle: it wants x to be two and y to be negative one. The best feasible point is one, zero. We can see this geometrically as the nearest point in the triangle to the target, but let us calculate the multipliers and see how the answer is certified.

Write the nonnegativity restrictions as negative x at most zero and negative y at most zero. Write the budget as x plus y minus one at most zero. At the proposed point, negative x is strictly negative, while negative y and the budget are both zero. The first multiplier is therefore zero. Call the other two multipliers mu for the y boundary and nu for the budget.

The objective gradient at one, zero is negative one in the x direction and positive one in the y direction. The gradient of the y boundary is zero, negative one. The budget normal is one, one. Stationarity says negative one plus nu equals zero in the x component, so nu equals one. In the y component, one minus mu plus nu equals zero, so mu equals two. Both are nonnegative. Feasibility and complementary slackness also hold.

Because the objective is convex and all three constraints are affine, these KKT equations certify global optimality. We need not inspect infinitely many points in the triangle. The multipliers say that tightening the budget or insisting on positive y would oppose what the objective wants to do. The fact that both active multipliers are positive also means neither of these boundaries is merely touching our solution by accident.

Now consider a slightly different target, two and one, with the same triangle. The nearest point is again one, zero, but the objective gradient there is negative one, negative one. The budget multiplier equals one; the y-boundary multiplier equals zero. The y boundary is active but has no positive multiplier. This is called weak activity. If we nudge the target's second coordinate upward, the optimizer may move into the interior of that boundary immediately. Treating every active inequality as a permanently binding equality would predict the wrong derivative across such a change.

## Which directions matter at second order?

The linearized cone alone is not the whole answer to second-order optimality. Many feasible directions already increase the objective at first order. Along them, the first derivative has decided the local behavior; a negative second derivative need not hurt the minimum if the positive linear term dominates sufficiently close to the point.

The directions that remain delicate are those in the linearized feasible cone along which the first-order objective change is zero. They form the critical cone. At a stationary KKT point, these can also be described using the multipliers: an active inequality with a strictly positive multiplier must have zero directional derivative along a critical direction, while an active inequality with a zero multiplier is only required to have a nonpositive directional derivative. Equality constraints always require zero directional derivative.

For smooth data and an appropriate constraint qualification, a local minimum must have nonnegative curvature of the Lagrangian in every critical direction. A standard second-order sufficient condition asks for strictly positive Lagrangian curvature on every nonzero critical direction. These statements differ from the equality-only rule in two respects. The set of critical directions may be a cone rather than a subspace, and the multiplier-weighted Hessians of the nonlinear constraints still contribute.

At our triangle example with two positive multipliers, the two independent active normals force a critical direction to have zero change in both y and x plus y. Only the zero direction remains. This is not a paradox. The optimizer sits at a pointed vertex where every nonzero feasible movement already raises the objective to first order. No second-order curvature test is needed to distinguish a nearby minimum from a maximum in those directions.

At a weakly active boundary, the critical cone is larger. It can include directions that move into the formerly active constraint and have zero first-order objective change. That is why dropping every active inequality into an equality-constrained Newton system is not automatically justified. The sign of the multiplier and the actual feasible cone must guide the calculation.

## Why a qualification is a mathematical requirement

A frequently used regularity condition is that the gradients of all equality constraints and all currently active inequalities are linearly independent. This is called the linear independence constraint qualification, abbreviated LICQ. Under the usual differentiability assumptions, it supplies unique KKT multipliers at a local minimum and makes the active-constraint geometry tractable.

A weaker condition, often called the Mangasarian–Fromovitz constraint qualification, requires the equality Jacobian to have full row rank and a direction tangent to the equalities that strictly decreases every active inequality. It often ensures multiplier existence without uniqueness. For nonlinear inequalities, these conditions help justify the relationship between feasible directions and their linearization. The choice of condition depends on the theorem we want, not just on the desire to attach an acronym to the problem.

Here is the counterexample worth remembering. Minimize x subject to x squared being at most zero. The only feasible value is zero, so it is a global minimizer. The constraint is active, but its derivative at zero is zero. The objective derivative is one. A nonnegative multiplier times a zero constraint gradient cannot cancel it. KKT stationarity fails, even at the global minimizer, because the qualification has failed.

Also beware the opposite error. Satisfying KKT is not a proof of a minimum for an arbitrary nonconvex problem. The unconstrained function negative x squared has derivative zero at x equal to zero, but zero is a maximum. Constraints can make the geometric test more delicate, not less. Convexity supplies one global sufficiency theorem; second-order conditions supply local tests under regularity. They are different tools.

## An active-set switch you can solve exactly

Consider a one-variable fitting problem: minimize one half of x minus p squared, subject to x being nonnegative. The parameter p is the target measurement. If p is positive, the optimum is x equal to p, and the boundary is inactive. If p is negative, the best permitted choice is x equal to zero, and the boundary is active. At p equal to zero, x remains zero, but the multiplier also becomes zero.

The solution is the larger of p and zero. On the positive side its derivative with respect to p is one. On the negative side its derivative is zero. At zero there is no single ordinary derivative. The objective is strongly convex, the constraint gradient is nonzero, and the optimizer is uniquely determined for every p. Yet the solution map has a corner.

This separates several concepts that are often conflated. A unique minimizer need not depend differentiably on data. A non-singular Hessian of the objective does not eliminate an active-set switch. LICQ alone does not guarantee smooth parameter sensitivity for inequality-constrained solutions. At the transition, strict complementarity fails because an active inequality has multiplier zero. In a neighborhood where the active set is fixed, an implicit derivative can be valid; across the transition, a different mathematical description is required.

We now know how to read an inequality constraint as local geometry, how to use complementary slackness to distinguish its active roles, and how to restrict second-order tests to the directions the first-order conditions leave unresolved. This is the groundwork for choosing an active set inside a constrained Newton or sequential quadratic programming algorithm. It is also the warning label on any attempt to differentiate blindly through such an optimizer.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Cone and KKT notation

For \(h(x)=0\) and \(g(x)\leq0\), let \(A(x)=\{i:g_i(x)=0\}\). The linearized cone is

\[
\mathcal L(x)=\{d:Dh(x)d=0,\ \nabla g_i(x)^\top d\leq0\ (i\in A(x))\}.
\]

With \(L=f+\lambda^\top h+\mu^\top g\) and \(\mu\geq0\), KKT conditions are

\[
\nabla_x L=0,\quad h=0,\quad g\leq0,\quad\mu\geq0,\quad\mu_i g_i=0.
\]

The critical cone at a KKT point is \(\mathcal C(x)=\{d\in\mathcal L(x):\nabla f(x)^\top d=0\}\). Equivalently, active constraints with \(\mu_i>0\) have \(\nabla g_i^\top d=0\), while active zero-multiplier constraints retain \(\nabla g_i^\top d\leq0\). Under appropriate CQ such as LICQ, second-order necessity gives \(d^\top\nabla^2_{xx} Ld\geq0\) for \(d\in\mathcal C\); strict inequality on \(\mathcal C\setminus\{0\}\) is a standard sufficient condition for a strict local minimum, assuming the usual smoothness and KKT hypotheses. A feasible tangent **cone** must not be confused with the kernel of all active gradients when some active multipliers vanish.

### Triangle projection, exact multipliers

\[
\min_{x,y}\ \frac12\big((x-2)^2+(y+1)^2\big),\qquad -x\leq0,\ -y\leq0,\ x+y-1\leq0.
\]

At \((x,y)=(1,0)\), \(\nabla f=(-1,1)\) and the active normals are \((0,-1)\), \((1,1)\). Stationarity reads

\[
(-1,1)+2(0,-1)+1(1,1)=(0,0).
\]

The inactive \(-x\) multiplier is zero. Strict convexity and affine constraints make the solution unique and globally optimal. With target \((2,1)\) instead, the multipliers at \((1,0)\) become \(\mu_y=0\), \(\nu=1\); the y boundary is weakly active.

### Scalar active-set transition

For \(\min_{x\geq0}\frac12(x-p)^2\), using \(g(x)=-x\leq0\), the optimizer and multiplier are

\[
x_*(p)=\max\{p,0\},\qquad\mu_*(p)=\max\{-p,0\}.
\]

Hence \(x_*'(p)=0\) for \(p<0\), equals \(1\) for \(p>0\), and does not exist at \(p=0\), where the active multiplier is zero.

### Exercises with answers

1. **Signs:** for minimizing \(f(x)=(x-3)^2\) subject to \(x\leq1\), find the multiplier of \(g=x-1\). **Answer:** \(x_*=1\), \(f'(1)=-4\), \(g'(1)=1\), so \(\mu=4\geq0\).
2. **Weak activity:** verify the multiplier values for the target \((2,1)\) in the triangle. **Answer:** \(\nabla f(1,0)=(-1,-1)\), so \((-1,-1)+\nu(1,1)+\mu(0,-1)=0\) gives \(\nu=1,\ \mu=0\).
3. **Critical direction:** with \(g(x)=x\leq0\) and stationary \(f(x)=x^2\) at \(x=0\), find the linearized and critical cones. **Answer:** both are \(\{d:d\leq0\}\), since \(f'(0)=0\) and the unique KKT multiplier is zero. The Hessian \(2\) is positive on all nonzero critical directions.
4. **A failed qualification:** why does \(\min x\) subject to \(x^2\leq0\) fail multiplier stationarity? **Answer:** \(f'(0)=1\), \(g'(0)=0\), and \(1+\mu0\ne0\) for all \(\mu\geq0\).

### Sources and further reading

- [Stanford CME307/MS&E311, Lecture Note 07: Second-Order Necessary Conditions for Constrained Optimization](https://web.stanford.edu/class/msande314/lecture07.pdf), for critical/tangent directions and the Lagrangian Hessian.
- [Optimization for Decision Science: Constraint Qualifications](https://ndcbe.github.io/optimization/notebooks/7/constraint-qualifications/), for the distinctions among LICQ, MFCQ, and geometric linearization.
- S. Boyd and L. Vandenberghe, [*Convex Optimization*, §5.5](https://web.stanford.edu/~boyd/cvxbook/), for the convex KKT sufficiency theorem and dual interpretation.
- [Wikipedia: Karush–Kuhn–Tucker conditions](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions), for an introductory account of complementary slackness.

*Teaching connections:* `optimization-duality:004000` proves the convex certificate; `multivariable-calculus:027000` derives second variation for equality constraints; `multivariable-calculus:025000` distinguishes stable parameter recovery from small residuals.
