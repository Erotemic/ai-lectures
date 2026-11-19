# 004000 - Lagrange Multipliers and KKT Conditions: When Local Equations Certify an Optimum

**Track:** Optimization, Convexity, and Duality. **Background:** one-variable derivatives, convex functions, linear programming duality. **Theme:** multipliers, stationarity, complementary slackness, strong duality, Slater's condition, and failures of constraint qualification.

<!-- BEGIN SPOKEN LECTURE -->

# Lagrange Multipliers and KKT Conditions: When Local Equations Certify an Optimum

A designer wants a numerical parameter as close to three as possible, but the specification prohibits values greater than one. We can describe the preference by taking the squared distance from three. Without any restriction the optimal choice is three, where that distance is zero. Under the restriction, the best possible choice is one. Every other permitted value lies farther from three. The answer seems so clear that a derivative calculation may feel unnecessary.

Now suppose the parameter is one coordinate among a million, and the restrictions describe a complicated convex set. Looking at all feasible choices is no longer practical. We need a compact certificate that a proposed solution is truly optimal. Lagrange multipliers and the Karush–Kuhn–Tucker conditions provide just such a certificate in a broad class of problems. They describe an equilibrium between the direction in which the objective wants to decrease and the directions forbidden by active constraints.

We will derive that equilibrium in a one-dimensional model, calculate its dual bound, and show why the result works for convex problems. Then we will expose two failures: stationary points of nonconvex objectives need not be minima, and a constrained minimum may exist without any finite multiplier satisfying the textbook conditions. Those failures explain the roles of convexity and constraint qualifications.

## Start by separating the objective from feasibility

Our objective is the square of x minus three. Our feasible set consists of all real x at most one. The squared distance is smaller when x is closer to three. Among feasible values, one is closest, so the minimum value is four. We have the candidate x equal to one and a geometric argument for it.

Think about what the derivative does. The derivative of the squared distance is two times x minus three. At the optimum x equals one, that derivative is negative four. Ordinarily, a differentiable function minimized in the interior of its domain has derivative zero. Here the derivative is not zero because the minimizer sits on a boundary. A tiny movement to the right would improve the objective, but it would violate the constraint. A movement to the left would be allowed, but it would worsen the objective.

That is the balance a multiplier will record. The objective gradient points toward the desired improvement. The boundary prevents taking that step. A multiplier represents the strength with which an active restriction counters the objective's gradient. Its sign encodes the direction of the allowed inequality.

We shall write every inequality in the form a function of x being at most zero. Our particular constraint is x minus one at most zero. That sign convention will make the multiplier nonnegative. Changing conventions without changing the multiplier sign would break the argument, so the orientation is part of the mathematical setup.

## Building a Lagrangian lower bound

For any nonnegative number lambda, consider the objective plus lambda times x minus one. This new expression is called a Lagrangian. Because every feasible x satisfies x minus one at most zero, the added term is nonpositive. Thus for every feasible x, the Lagrangian is at most the original objective.

This is the first key inequality. If we minimize the Lagrangian over all real x, allowing infeasible values too, we obtain a number that is no larger than the objective at any feasible point. Such a number is a lower bound on the constrained minimum. The multiplier does not need to be optimal for the bound to be valid. Its only requirement for this inequality is nonnegativity.

Now calculate. The Lagrangian is the square of x minus three, plus lambda times x minus one. The derivative with respect to x is two times x minus three, plus lambda. Setting that derivative to zero gives the unconstrained Lagrangian minimizer: three minus half of lambda. Completing the square, or substituting that minimizer, shows that the minimum Lagrangian value is two lambda minus one quarter of lambda squared.

We can choose lambda to make this lower bound as large as possible. The resulting concave quadratic is maximized at lambda equal to four, and its value there is four. But four is exactly the objective value of our feasible candidate x equal to one. We have two sides of a certificate. Feasibility gives an upper bound of four on the optimal value, because a concrete candidate achieves four. The dual construction gives a lower bound of four on every possible feasible objective value. Equality forces the candidate to be globally optimal.

This is stronger than saying a numerical solver found one. The certificate has a direct proof: the lower bound applies to all feasible competitors, and the proposed point attains it. In exact arithmetic the proof is a few lines; with approximate numerical outputs we must also account for residuals and rounding errors.

## The four KKT ingredients

Look at what happened at the matching primal and dual choices. First, our candidate x equals one satisfies the constraint. This is primal feasibility. Second, lambda equals four is nonnegative. This is dual feasibility for our inequality convention.

Third, the derivative of the Lagrangian with respect to x vanishes at our candidate and multiplier. At x equal to one, the objective derivative is negative four. The constraint derivative is positive one. The product of the multiplier four and that derivative exactly cancels the objective derivative. This is stationarity.

Fourth, the multiplier times the constraint value is zero. In our example, x minus one equals zero at the optimum, so the product vanishes for any multiplier. This is complementary slackness. It says that a constraint with a strictly negative slack must have multiplier zero. A positive multiplier can be assigned only where the constraint is active, meaning it holds with equality.

Together these are the KKT conditions for a differentiable problem with inequality constraints, when there are no additional domain restrictions. Their algebraic form is short, but each part has a different job. Feasibility identifies an admissible answer. Sign restrictions make the Lagrangian a valid lower bound. Stationarity solves the inner minimization when convexity is present. Complementary slackness makes the lower bound meet the candidate's objective.

It is tempting to memorize the four labels and treat them as a magic test. Their real value comes from following the inequalities they support. We will show that chain explicitly, because it also tells us precisely when the certificate stops working.

## A proof of global optimality from KKT in a convex problem

Consider a differentiable convex objective, and several differentiable convex constraint functions, each required to be at most zero. Suppose we find a feasible point and nonnegative multipliers satisfying stationarity and complementary slackness.

Fix those multipliers. The Lagrangian is the objective plus a nonnegative weighted sum of convex constraint functions. Therefore it is itself convex. Stationarity at the proposed point says its gradient is zero. For a differentiable convex function on the whole real coordinate space, a point with zero gradient is a global minimizer. Consequently, the Lagrangian at the proposed point is no greater than its value at any other point.

Complementary slackness tells us that the proposed point's Lagrangian value equals its objective value, since every multiplier-constraint product vanishes. Meanwhile, at any competing feasible point, each multiplier is nonnegative and each constraint value is nonpositive. The competing point's Lagrangian is therefore at most its objective.

Combine these observations in the right direction. The objective at our candidate equals its Lagrangian. That is no greater than the Lagrangian at any competitor, because our candidate minimizes the Lagrangian. And the competitor's Lagrangian is no greater than the competitor's objective, because the competitor is feasible. Thus our candidate's objective is no greater than every competing feasible objective. Global optimality follows.

We have proved sufficiency of the KKT conditions in this convex differentiable setting. Notice what was used: convexity of the objective and constraints, nonnegative multipliers, the stationarity equation, and complementary slackness. We did not need a promise that some optimization algorithm had converged, and we did not need to enumerate the feasible set.

If there are affine equality constraints, we add their multiplier terms to the Lagrangian without a sign restriction. An equality has value zero at every feasible point, so its term does not move a feasible objective up or down. Stationarity includes the corresponding equality gradients. If the domain is restricted to a separate convex set, the correct condition uses a normal cone or a constrained minimization of the Lagrangian over that set, rather than always setting the full gradient to zero.

## Why do multipliers exist at an optimum?

Sufficiency starts with a candidate and suitable multipliers. Necessity asks a different question: suppose we know a convex problem has an optimum. Can we always find multipliers satisfying KKT? The answer requires additional hypotheses.

One common sufficient condition is Slater's condition. For a convex optimization problem with convex inequality constraints and affine equalities, it asks for a point satisfying the affine equalities and all relevant nonlinear inequality constraints strictly, together with the appropriate relative-interior domain assumptions in the general formulation. This point need not optimize anything. Its role is to establish that the feasible problem has enough room for a separating-hyperplane or duality argument.

Under standard regularity and finite-optimum hypotheses, Slater's condition yields zero duality gap and dual attainment. When a primal optimum also exists, the attained primal and dual solutions satisfy the KKT conditions. In smooth convex cases this produces the gradient and complementary-slackness equations we have been using.

Our one-dimensional example satisfies the simple strict-feasibility condition: x equal to zero lies strictly below one. The dual multiplier four is attained, and the primal and dual values meet at four. The existence of a strictly feasible point did not tell us the answer by itself. It gave a theorem that an appropriate dual certificate would exist under the rest of the problem's assumptions.

This is an important separation of ideas. Once we exhibit valid KKT data in a convex problem, the sufficiency proof establishes optimality. Slater's condition is most useful beforehand, when we need to know that an optimal solution can be accompanied by multipliers. It is a qualification for a necessity and duality result, rather than an extra line in the verification of a known convex certificate.

## A constraint that has no interior

Now change the problem. Minimize x subject to x squared at most zero. Because every real square is nonnegative, the constraint forces x to be exactly zero. The feasible set contains one point. That point is trivially a global minimizer, with objective value zero. Every part of this conclusion is straightforward.

Try to write the KKT stationarity equation. The objective has derivative one. The constraint x squared has derivative two x. At the sole feasible point x equals zero, the constraint derivative is zero. So the stationarity equation would say one plus lambda times zero equals zero. No finite multiplier can make that true. The problem has a perfectly valid optimum but no KKT multiplier satisfying the usual gradient equations.

Slater's strict-feasibility condition fails here. To satisfy x squared strictly less than zero would require a negative square. There is no such real number. At the feasible point, the constraint has a flat derivative even though it excludes every neighboring point. The first-order gradient description loses the actual shape of the feasible region.

We can push the example further. Its dual Lagrangian is x plus lambda x squared, with lambda nonnegative. For positive lambda the minimum over x occurs at negative one divided by twice lambda, and the minimum value is negative one divided by four lambda. As lambda increases without bound, these lower bounds approach zero. Thus the supremum of the dual values equals the primal optimum, zero. Nevertheless no finite positive lambda achieves zero, and lambda equal to zero gives a Lagrangian unbounded below.

We have zero duality gap but no attained dual optimum. That is why we must distinguish strong duality in the sense of equality of values from dual attainment and from the existence of KKT multipliers. Textbook statements sometimes package these consequences together under a constraint qualification. Removing the qualification can separate them.

The example also reveals why stationarity is a statement about local linearized information. At x equal to zero, the linearization of x squared is just zero: it does not convey the restriction of the original quadratic. No positive multiple of that zero gradient can counteract the derivative of the objective.

## Nonconvex stationarity can point the wrong way

A different failure occurs when the objective is nonconvex. Take the unconstrained task of minimizing negative x squared on the interval from negative one to one. At x equal to zero, the derivative vanishes. There are no active inequality multipliers if we represent the interval by the usual endpoint constraints, and zero satisfies the interior stationarity equation.

But zero is not a minimum. Its objective value is zero, while either endpoint has value negative one. Indeed, zero is a local maximum. Stationarity in a nonconvex problem identifies a candidate where first-order change vanishes, or where constraints balance that change. It does not by itself certify global optimality.

A second-order test may reveal the local shape, but even positive curvature at one point need not establish global optimality over a nonconvex region. The convex proof worked because a stationary point globally minimized the Lagrangian. Without convexity that step is unavailable. The chain of inequalities breaks at a named place.

This distinction becomes practical when inspecting solver reports. A nonlinear solver may say it satisfied a first-order optimality tolerance. That is evidence of an approximately stationary feasible point under its chosen conditions. It is not automatically an exact global certificate. For a convex problem we can often convert sufficiently accurate primal and dual outputs into a bounded optimality gap; for a nonconvex problem we must ask what additional global information is available.

## The geometry of active constraints

It helps to visualize the stationarity equation in several dimensions. The objective gradient indicates the direction of steepest local increase. Its negative indicates steepest local decrease. At an interior convex optimum with no active constraints, the gradient is zero. At a boundary optimum, the negative objective gradient can point into a forbidden region.

An active differentiable inequality has a gradient normal to its boundary, oriented toward increasing the constraint function. Nonnegative multiples of these normals, together with unrestricted multiples of equality normals, form the balancing contribution in the stationarity equation. At an optimum, the objective gradient plus that combination vanishes.

When several constraints meet, the optimal multiplier for one may be zero even when the constraint happens to be active. Complementary slackness gives the implication from positive multiplier to active constraint, and the implication from strictly inactive constraint to zero multiplier. It does not assert that every active constraint must have a positive multiplier. A boundary can be geometrically present without carrying a nonzero price in the chosen dual solution.

This interpretation leads to sensitivity analysis. Under suitable regularity, a multiplier can describe the first-order change in optimal value when a constraint bound is relaxed. In our squared-distance example, the active upper bound of one has multiplier four. If we permit the boundary to move a tiny amount to the right, the objective improves at approximately four units of objective value per unit of relaxation. One can verify that by differentiating the optimal value as a function of the allowed upper bound near one.

The word approximately is important. Multipliers are local sensitivity information under the relevant differentiability and regularity assumptions. With changes large enough to switch the active constraints, the same linear estimate may no longer apply. A multiplier should not be read as a universal price for any size of change.

## Numerical certificates and their limits

Suppose a solver returns a feasible x and a nonnegative multiplier, but its stationarity equation holds only within some tolerance. We should not erase that tolerance and declare an exact proof. An approximate primal objective gives an upper bound if feasibility is certified. A dual-feasible multiplier gives a lower bound after the Lagrangian is minimized or bounded correctly. Their difference is an optimality gap certificate.

In our one-dimensional problem, a nearby value of lambda produces a valid explicit lower bound. Even if lambda is not exactly four, its dual quadratic gives a number below four. We may compare it to the objective value of a feasible candidate and obtain an interval containing the true optimum. For computer arithmetic, a rigorous interval requires attention to outward rounding and verification of constraints as well as arithmetic error.

The KKT residuals can guide numerical termination, but an exact or interval-validated dual bound is preferable when a proof-grade guarantee is required. When constraints are nonlinear, finding a certified global minimum of the Lagrangian may require more work. Convexity makes the stationarity route tractable, and exact arithmetic may be possible for rational examples. The proof obligation remains mathematical even when the numbers are delivered by software.

## Returning to the bound at one

Our initial problem had a derivative of negative four at the optimum, apparently contradicting the rule that a minimum has zero derivative. The contradiction vanished once we incorporated the active boundary. Its normal contribution had multiplier four, balancing the objective gradient. The same multiplier made the best Lagrangian lower bound equal to the feasible objective value, four.

For differentiable convex optimization problems, feasible primal data, nonnegative inequality multipliers, stationarity, and complementary slackness are sufficient to certify a global optimum. Constraint qualifications such as Slater's condition help ensure that such multipliers exist at a primal optimum. The example with x squared at most zero showed an optimum without finite KKT multipliers; the nonconvex example showed stationary data without an optimum.

These are three distinct mathematical questions: does an optimum exist, can it be described by first-order multipliers, and do the multiplier equations certify global optimality? The KKT framework answers the last question under convexity, and constraint qualifications connect it to the second. A useful numerical certificate makes both the assumptions and the primal-dual inequalities explicit.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Consider the primal problem:
\[
 p^*=\min_{x\le1}(x-3)^2=4,\qquad x^*=1.
\]
For \(g(x)=x-1\le0\),
\[
 L(x,\lambda)=(x-3)^2+\lambda(x-1),\quad \lambda\ge0,
\]
\[
 q(\lambda)=\inf_{x\in\mathbb R}L(x,\lambda)
 =2\lambda-\frac{\lambda^2}{4},\quad
 q(4)=4=p^*.
\]
The KKT conditions at \((x^*,\lambda^*)=(1,4)\) are
\[
 g(x^*)\le0,\quad \lambda^*\ge0,\quad
 2(x^*-3)+\lambda^*=0,\quad
 \lambda^*g(x^*)=0.
\]

For differentiable convex \(f,g_i\) and affine equalities \(h_j\), stationarity is
\[
 \nabla f(x^*)+\sum_i\lambda_i^*\nabla g_i(x^*)
 +\sum_j\nu_j^*\nabla h_j(x^*)=0.
\]
Under primal feasibility, \(\lambda_i^*\ge0\), and complementary slackness, convexity gives the proof certificate, for every feasible \(y\):
\[
 f(x^*)=L(x^*,\lambda^*,\nu^*)
 \le L(y,\lambda^*,\nu^*)\le f(y).
\]
The first inequality uses stationarity plus convexity of \(L\); the second uses feasibility.

**Constraint qualification counterexample:**
\[
 \min_{x\in\mathbb R}x\quad\text{subject to }x^2\le0.
\]
Here \(x^*=0\) and \(p^*=0\), but stationarity requires \(1+2\lambda x^*=1=0\), impossible. Dual values are \(q(\lambda)=-1/(4\lambda)\) for \(\lambda>0\), approaching \(0\) without attainment. This distinguishes dual value equality from dual attainment.

### Exercises with answers

1. **Bound calculation.** What is \(q(2)\) in the main example? **Answer:** \(4-1=3\), a valid lower bound on the optimal value four.
2. **Complementary slackness.** If \(g_i(x^*)<0\), what must \(\lambda_i^*\) equal? **Answer:** zero.
3. **Slater.** Find a strict feasible point for \(x-1\le0\). **Answer:** \(x=0\).
4. **Broken qualification.** Why does the constraint \(x^2\le0\) produce no KKT multiplier? **Answer:** the only feasible point is zero, where its constraint derivative vanishes while the objective derivative is one.
5. **Nonconvexity.** Why doesn't \(f'(0)=0\) prove optimality for \(f(x)=-x^2\) on \([-1,1]\)? **Answer:** \(f(0)=0>-1=f(1)\).

### References

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Chapter 5: Duality, Slater's condition and KKT.
- Stanford Engineering Everywhere, EE364A, Lecture 9: complementary slackness and KKT.
- Dimitris Bertsimas and John N. Tsitsiklis, *Introduction to Linear Optimization*, primal-dual certificate viewpoint.
