# 002000 - Convex Sets and Supporting Hyperplanes: Geometry That Proves Bounds

**Track:** Optimization, Convexity, and Duality. **Background:** algebra, functions, two-dimensional geometry; elementary derivatives are explained. **Theme:** convex combinations, first-order bounds, projection, separation, and certificates.

<!-- BEGIN SPOKEN LECTURE -->

# Convex Sets and Supporting Hyperplanes: Geometry That Proves Bounds

Suppose you are trying to find the safest operating point for a machine. You have two controls: one adjusts speed, the other adjusts temperature. Some combinations are permitted, others are dangerous. You draw all permissible settings on a page. The resulting shape looks like an ordinary geometric region. And now a question about that shape becomes a question about whether we can trust an optimization algorithm: if it gets stuck at a setting that cannot be improved by a small adjustment, has it found the best setting anywhere?

Sometimes yes. Sometimes a local stopping point is just a trap. Much depends on the geometry of the permissible region and of the quantity we are trying to optimize. A particularly useful kind of geometry is convexity. It gives a precise setting in which local arguments can establish global conclusions. It also explains how a straight line or flat plane can certify bounds for an entire curved region.

We will begin with line segments, work through convex and nonconvex feasible regions, derive a supporting-line inequality for differentiable functions, and prove a geometric fact about the closest point in a convex set. By the end, a simple dot product will provide a certificate that no other feasible point can improve a proposed answer.

## The segment test

Take two points in a region. Join them with a straight line segment. If every point on that segment is also in the region, no matter which two points we selected, the region is convex. This definition is disarmingly simple. A filled disk is convex: the chord joining any two points stays inside the disk. A crescent with a missing bite is generally not convex. So is a region made from two separated islands.

Imagine a production system with two nonnegative outputs, x and y, whose total cannot exceed ten units. The feasible settings satisfy x at least zero, y at least zero, and x plus y at most ten. Draw them and you obtain a triangle. Select any two feasible production plans. If you blend them, choosing a fraction of one plan and the rest of the other, the blended plan also satisfies every constraint. The feasible triangle is convex.

This blending argument works because linear inequalities behave well under averages. If two plans each use no more than ten units of a resource, any weighted average also uses no more than ten. We do not need a picture to prove it. The definition in two dimensions extends to hundreds or thousands of dimensions, where a picture is no longer possible but the algebra remains the same.

One subtlety is that a convex combination is a mathematical average of points, not necessarily a physically realizable mixture of decisions. If a machine must be either fully on or fully off, the average between those states may not be allowed. Modeling that decision with a continuous control creates a convex relaxation rather than an exact description. Convexity helps us solve the relaxed problem, but we must still decide whether its solutions are valid for the original task.

A union of convex sets need not be convex. An intersection of any family of convex sets is convex. That is why systems of many linear inequality constraints remain well-behaved: each inequality describes a halfspace, and the feasible set is their intersection. Adding another inequality may shrink the region but cannot introduce a hole or disconnected island inside it.

## Convex functions: a different use of the word

We also call a function convex, but the definition concerns its graph rather than its allowed inputs. A function is convex when the straight segment connecting two points on its graph lies on or above the graph between them. Think of a bowl: the middle of the bowl does not rise above the chord joining two rim points. The graph of the square function is convex; an upside-down bowl is not.

In algebraic language, the function value at a weighted average of two inputs is no greater than the same weighted average of their function values. This inequality is called Jensen's inequality in a basic two-point form. A convex function assigns a value to a mixture that is no worse than the weighted average of the individual values, when smaller values are preferred.

For example, consider the cost equal to the square of the speed setting. Compare speed two and speed four. Their costs are four and sixteen. The average speed three costs nine, which is less than the average cost ten. That is convexity in arithmetic rather than in a drawing. The numbers make the distinction memorable: average inputs first, then compute the cost, or compute the costs first and average them. A convex function puts the first answer no higher.

The convexity of a feasible set and the convexity of an objective are separate requirements. We can have a convex region with a nonconvex cost, or a convex cost on a disconnected region. To obtain the strongest global optimality guarantees in minimization, we typically need a convex feasible set and a convex objective.

Why is that combination so helpful? Suppose a feasible point is allegedly a local minimum, but a distant feasible point has a strictly lower cost. Convexity lets us follow the line segment between them while remaining feasible. The function's convexity says that near the alleged local minimum, the cost along that segment would already be smaller. That contradicts local minimality. Therefore, under the usual definitions, every local minimum is global in a convex minimization problem.

This argument is almost entirely geometric. It does not require searching the full feasible set. We use the hypothetical better point to construct a nearby improvement, thereby ruling out the possibility that the local answer was misleading.

## A tangent line can make a global promise

For a smooth convex function, the derivative at a point tells us more than a local slope. The tangent line lies below the entire graph. At a point x, the line has the function's value at x plus its slope multiplied by the displacement from x. Convexity ensures that the actual function value at any other point y is at least that tangent-line prediction.

For the square function, choose x equal to two. The function value is four and the slope is four. The tangent line predicts four plus four times the amount by which y exceeds two. At y equal to five, the line predicts sixteen; the true function value is twenty-five. At y equal to zero, the line predicts negative four, while the true value is zero. The tangent line need not provide a useful numerical approximation far away. Its importance is the direction of the inequality: it is a valid lower bound everywhere.

We can derive this directly. Write the square of y as the square of x plus two x times the difference y minus x, plus the square of that difference. The last term cannot be negative. Drop it, and we obtain exactly the tangent-line lower bound. That remainder is a concrete witness to the global nature of the inequality.

Now suppose the slope at an interior feasible point is zero. The tangent line is horizontal. The global lower-bound inequality then says the function value anywhere else is at least the value at the point. We have proved optimality with one derivative calculation and one convexity theorem. A stationary point is not always a global minimum; it is convexity that upgrades the local derivative fact into a global guarantee.

The same idea works in many dimensions. A gradient is a vector of partial derivatives. The tangent line becomes a tangent plane or, more generally, a linear function of the displacement. The first-order inequality says that a convex differentiable objective lies above its supporting affine function everywhere in its domain.

## Nonsmooth functions also have supporting slopes

What about the absolute-value function? Its graph is a V, with a corner at zero. There is no single derivative at that corner. Yet zero is clearly a global minimum. We should not lose our optimality theory just because the graph is not smooth.

A subgradient solves the problem. It is any slope that defines a line lying below the entire graph and touching the graph at the chosen point. At zero for absolute value, every slope between negative one and positive one is valid. The horizontal line at height zero is one such supporting line. Its existence certifies that zero is globally minimizing.

Away from zero, the slope is ordinary: positive one for positive inputs and negative one for negative inputs. At the corner, a whole interval of slopes works. The set of all valid slopes at a point is the subdifferential. For a differentiable convex function it contains just the usual gradient; for a nonsmooth one it can contain many vectors.

This observation foreshadows algorithms for nonsmooth optimization. We can still ask for a certificate that zero is among the subgradients at a feasible point. We can also use subgradients to move toward improvement, though algorithms must manage step sizes and potential nonsmoothness. The concept broadens the reach of first-order reasoning without pretending every function is smooth.

## Closest points and separating lines

Now let us return from objectives to feasible regions. Suppose C is a nonempty closed convex set in ordinary Euclidean space, and z is a point outside C. Because C is closed and we are in finite dimensions, there is a point p in C closest to z. Convexity makes that closest point unique. Imagine drawing the shortest arrow from z to the region. It ends at p.

There is a striking fact about that arrow. Point it from p toward z. For every feasible point x in C, the dot product of the arrow with the displacement from p to x is nonpositive. In plain language, none of the feasible displacements has a positive component pointing toward z. If one did, moving a little in that direction would shorten the distance to z, contradicting the claim that p is closest.

This dot-product inequality defines a supporting hyperplane. In two dimensions it is a line through p, perpendicular to the arrow from p to z. All of C lies on one side, while z lies strictly on the other side. The line separates the outside point from the feasible region. Nothing about the full boundary of C needs to be drawn or described point by point. One vector gives a global geometric certificate.

There is an important role for the assumptions. The argument uses a closest point, so we need its existence. If the set is open and the closest point would lie on the missing boundary, the minimum distance may not be attained. If the region is nonconvex, a nearest point may exist but the line through it need not put the entire region on one side. The separation certificate is the consequence of geometry plus hypotheses, not merely of our ability to draw a plausible tangent.

## Deriving the projection inequality

Let us work through the logic without concealing the main step. Choose any feasible x. Since C is convex, every point on the segment from p to x is also feasible. Write a point on that segment as p plus t times the displacement from p to x, with t between zero and one.

Because p is closest to z, the squared distance from z to the segment point cannot be smaller than the squared distance from z to p. Expand the squared distance as a function of t. The linear coefficient is negative two times the dot product of z minus p with x minus p. The quadratic coefficient is the squared length of x minus p, which is nonnegative.

If that dot product were positive, the linear coefficient would be negative, and for sufficiently small positive t the distance would decrease. That contradicts minimality. So the dot product is nonpositive. We have proved the supporting-plane inequality for every x by testing only an infinitesimal move toward each candidate.

It is a satisfying proof because the geometric picture and algebra agree. The closest-point arrow is normal to a boundary that may be curved or even have corners. The region cannot extend into the halfspace on the outside-point side of the supporting plane. The argument works in any finite dimension and is a basic tool in projection algorithms and convex analysis.

There is also a converse. If p lies in C and satisfies this dot-product inequality for every feasible x, expanding squared distances shows that p is at least as close to z as any x is. So the inequality does more than follow from optimality: it characterizes the closest point. It is a certificate we can check independently of how p was found.

## Convexity as a basis for duality

Why should a geometric supporting plane help with optimization of resources and costs? Suppose a feasible region is cut out by inequalities, and we want to minimize an objective. A valid lower bound on the objective over the entire region proves that no candidate can beat that bound. Supporting affine functions are a natural way to construct such lower bounds.

A dual problem takes this idea further. It searches over combinations of constraints that yield the strongest available global bound. Each combination is another mathematical object with a value that can be checked. The primal problem searches for a feasible answer; the dual searches for a bound on what any feasible answer could achieve. When the two values meet, we have an optimality certificate.

Even before learning the full algebra of duality, the geometric interpretation is useful. A convex objective supplies supporting planes. A convex feasible region admits separating planes. Multipliers tell us how constraint information can combine into a statement about the objective. Under appropriate regularity conditions, these pieces can fit together with no gap between the best attainable objective and the strongest dual bound.

But a duality gap may occur when hypotheses are not met. A purported gradient certificate can also fail if the candidate lies on a constrained boundary and we demand zero gradient where the correct condition involves a normal vector. Convexity provides a language for precise guarantees, not a replacement for stating assumptions.

## A historical change in what geometry was for

Convex geometry grew through several mathematical traditions. Hermann Minkowski developed geometric methods involving convex bodies and numbers. The Hahn-Banach theorem, in work associated with Hans Hahn and Stefan Banach, later made separation and extension arguments central to functional analysis. In finite dimensions, supporting and separating hyperplanes can often be visualized as lines and planes; in infinite-dimensional spaces, the analogous statements require care about topology and continuous linear functionals.

The historical significance is conceptual. Geometry became a way to prove inequalities and existence results far beyond ordinary diagrams. Convexity now links analysis, numerical algorithms, economics, signal processing, and machine learning. The same supporting-plane intuition can explain a simple absolute-value minimum or a sophisticated optimization certificate.

It is tempting to make the history sound like an inevitable march toward modern software. It was not. Results were developed for different problems and within different mathematical traditions. Their later use in optimization depends on how those mathematical tools were combined, and on computing technologies that made large optimization problems practical.

## Constrained optimality is not the same as zero gradient

There is an important trap in applying the tangent-plane argument. If we minimize a convex function over the entire real line and find a point where the derivative is zero, we have an unconstrained global minimum. But if the permitted points occupy only a half-line or a polygon, the optimum can lie on the boundary, where the derivative is not zero.

Consider minimizing the square of x over the region where x is at least two. The unconstrained minimizer would be zero, which is forbidden. The actual minimum occurs at x equal to two, where the derivative is four. A demand for zero derivative would reject the correct answer. The right optimality condition says that the derivative points in a direction that cannot be followed while staying feasible and decreasing the objective.

For a convex differentiable function f on a convex feasible set C, a point p is optimal if and only if the gradient at p has nonnegative inner product with every feasible displacement x minus p. Why is this sufficient? The supporting-plane inequality says f of x is at least f of p plus that inner product. If the inner product is nonnegative for every feasible x, no feasible point can have lower cost. Under suitable differentiability assumptions, necessity follows by looking at the derivative along each feasible segment starting at p.

This condition links the objective's gradient to the normal geometry of the feasible set. At an interior optimum the normal restriction disappears and the gradient must vanish. At a boundary optimum the gradient can be nonzero because moving against it would leave the allowed region. This is the geometric seed of the Karush-Kuhn-Tucker conditions: constraint multipliers account for directions blocked by the boundary.

## Convex hulls and what an average is permitted to mean

The convex hull of a collection of points is the smallest convex set containing them. For a finite collection, it consists of all convex combinations of those points: weighted averages with nonnegative weights summing to one. A triangle is the convex hull of its three corners; a line segment is the convex hull of its endpoints.

In optimization, a convex hull can relax a discrete choice problem. Suppose a system may use either setting A or setting B, but no intermediate setting. The convex hull includes every point on the segment between them. Solving over this hull can produce a bound on the original problem because it allows additional choices. Whether the relaxed solution can be implemented requires a separate argument, perhaps by randomized scheduling or by showing an optimal vertex exists.

The distinction is worth remembering when a mathematical model looks elegant. The geometry may be exactly right for a time-sharing system that alternates between modes, where averages represent meaningful long-run allocations. It may be wrong for a single indivisible decision that must be made once. Convexity establishes useful theorems about the modeled set; it does not prove that the model faithfully represents the real system.

## How to use the geometry responsibly

When someone claims an algorithm found a global optimum, ask four questions. Is the feasible region convex? Is the objective convex for a minimization problem? Has the proposed point satisfied the correct first-order or dual conditions? And are any required closure, differentiability, or constraint qualifications actually true?

A candidate may be feasible yet suboptimal. An approximate numerical gradient may be close to zero without proving an exact theorem. A solver may use floating-point arithmetic and return a point that slightly violates a constraint. We can often turn these approximations into certified bounds, but the error analysis must be performed rather than presumed.

Consider again the machine with controls for speed and temperature. If the safe operating region is convex and the cost is convex, a supporting-plane argument may show that no permissible adjustment anywhere can improve a candidate. If the machine has discrete modes, hidden switching costs, or thresholds that destroy convexity, the argument may no longer apply. We might still solve a convex relaxation and use its value as a bound, but that is a different claim.

This is the practical virtue of a geometric foundation: it tells us when a simple proof can cover a huge search space, and it tells us precisely what would invalidate that proof. Convexity is a property we can verify. Supporting planes are certificates we can state. Projection and first-order inequalities connect the two. The result is a framework in which a local calculation can justify a global conclusion, provided the geometry supports it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Definitions

A set `C` is convex if `x,y in C` and `0 <= t <= 1` imply `(1-t)x+ty in C`. A function `f` is convex on `C` if `f((1-t)x+ty) <= (1-t) f(x) + t f(y)`.

If `f` is differentiable convex, then `f(y) >= f(x)+ <grad f(x), y-x>`. At `x=2` for `f(x)=x^2`: `f(y) >= 4 + 4(y-2)`, since the difference is `(y-2)^2`.

### Projection theorem, finite dimension

Let `C` be nonempty closed convex in `R^n`, `z in R^n`, and `p=Proj_C(z)`. Then for every `x in C`, `<z-p,x-p> <= 0`. This follows by expanding `||z-(p+t(x-p))||^2` and letting `t` decrease to zero. Conversely this variational inequality characterizes the projection by expanding `||z-x||^2`.

### Nonsmooth example

For `f(x)=|x|`: `partial f(0)=[-1,1]`; `0 in partial f(0)` certifies global minimality on the real line.

### Exercises and answers

1. **Intersection:** Why is the intersection of convex sets convex? **Answer:** Any segment between two common points lies in every set separately.
2. **Convexity check:** Is `f(x)=x^2` convex? **Answer:** Yes; its second derivative is 2 on `R`.
3. **Projection:** Project `z=(2,0)` onto the closed halfspace `x1<=1`. **Answer:** `p=(1,0)`; the outward normal is `(1,0)`.
4. **Counterexample:** Does a local minimum of a nonconvex objective imply global optimality? **Answer:** No; a polynomial with two wells can have a higher local minimum.

### References

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004), chapters 2 and 3: https://web.stanford.edu/~boyd/cvxbook/
- R. Tyrrell Rockafellar, *Convex Analysis* (1970), projection and separation chapters.
- Jonathan Borwein and Adrian Lewis, *Convex Analysis and Nonlinear Optimization* (2006).
