# 010000 — Lagrange Multipliers: Optimization Along Constraints

**Track:** Multivariable Calculus from First Principles. **Background:** gradients, level sets, constrained geometry. **Question:** how can an extremum occur where the gradient is not zero?

<!-- BEGIN SPOKEN LECTURE -->

# Lagrange Multipliers: Optimization Along Constraints

Suppose a designer can choose x and y, but not independently. The available budget fixes x plus y equal to one. The designer wants to minimize x squared plus y squared. The unconstrained minimum would be x equals zero and y equals zero, but that point violates the constraint. We must optimize only along the line of feasible choices.

On that line, y equals one minus x. Substitute into the objective. It becomes x squared plus the square of one minus x. Differentiate the one-variable expression: four x minus two. The minimum occurs at x equals one half, y equals one half. The objective value is one half. This direct substitution method is reliable when the constraint is easy to solve.

Lagrange multipliers generalize the same geometry when substitution is inconvenient.

## Allowed directions at a constraint

Write the constraint as g of x and y equals zero. If the gradient of g is nonzero at a feasible point, it is normal to the constraint curve. Any velocity along the curve is perpendicular to the gradient of g. At an extremum of f restricted to that curve, the derivative of f in every allowed tangent direction must vanish. So the gradient of f must also be perpendicular to the tangent direction.

In the plane, when the constraint is a regular smooth curve, two nonzero vectors perpendicular to the same tangent line are parallel. Therefore the gradient of f is a scalar multiple of the gradient of g. We call that scalar lambda, the Lagrange multiplier.

The equations are gradient f equals lambda times gradient g, together with g equals zero. They are necessary conditions for a regular constrained extremum. They do not automatically guarantee that a solution is a minimum or maximum. We still need to compare candidates or analyze second-order behavior along the constraint.

## Solve the example using the multiplier

Let f equal x squared plus y squared and let g equal x plus y minus one. The gradients are two x comma two y and one comma one. The multiplier condition says two x equals lambda and two y equals lambda. Thus x equals y. Combined with x plus y equals one, we obtain x and y both one half.

For this problem we can also prove global minimality without derivatives. The identity x squared plus y squared equals one half times the square of x plus y, plus one half times the square of x minus y, shows that every feasible point has objective at least one half. Equality occurs exactly when x equals y. This is a useful check on a stationary-point calculation.

What does lambda mean? If the constraint right-hand side changes from one to a nearby value b, the minimum becomes b squared divided by two. Its derivative with respect to b is b. At b equals one, that derivative equals one, which is precisely the multiplier under our convention g equals x plus y minus b. The multiplier measures how the optimum changes when the constraint level changes, under suitable regularity and uniqueness assumptions. This sensitivity interpretation is not merely a trick of algebra.

## A curved constraint

Consider maximizing and minimizing f equals x plus y on the unit circle x squared plus y squared equals one. The objective gradient is one comma one. The constraint gradient is two x comma two y. The multiplier equation gives one comma one equals lambda times two x comma two y. Consequently x equals y at a regular solution. On the unit circle that leaves two points: both coordinates one over square root of two, or both negative one over square root of two. Their objective values are square root of two and negative square root of two.

The circle is compact, so these are the global maximum and minimum after checking the candidate values. The Lagrange equations alone only generated candidates; compactness and comparison completed the argument.

## Why regularity cannot be ignored

Now impose the constraint x squared plus y squared equals zero. There is only one feasible point: the origin. Every objective function defined there attains both its feasible maximum and feasible minimum at that singleton. But the constraint gradient vanishes at the origin. Take the objective f equals x, whose gradient is one comma zero. There is no lambda that makes one comma zero equal to lambda times zero comma zero.

The multiplier condition fails, not because the extremum is unreal, but because the constraint is singular at the point. The theorem assumes the constraint gradients are independent and nonzero in the required sense. Singular constraints demand separate analysis.

With several constraints, their gradients span a normal space, and the objective gradient must lie in that span at a regular constrained extremum. Independence of constraint gradients is the matrix rank condition that makes the feasible set locally smooth.

## What to do in a real optimization problem

First write the constraints clearly and determine the feasible set. Check whether it is compact, whether it has a boundary, and whether the constraints are regular. Solve the multiplier equations only for regular interior points of the feasible constraint set. Analyze any singular points, corners and inequality boundaries separately. Compare the actual objective values. If the feasible set is not compact, establish existence or rule out escape to infinity by another argument.

Lagrange multipliers are not a magic equation that replaces geometry. They are the algebraic expression of a simple fact: at an optimum, change in the objective vanishes along directions you are allowed to move.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For one smooth equality constraint \(g(x)=0\), if \(\nabla g(a)\ne0\) and \(f\) has a local constrained extremum at \(a\), then
\[
\nabla f(a)=\lambda\nabla g(a),\qquad g(a)=0.
\]
For constraints \(g_1=\dots=g_k=0\) with linearly independent gradients (rank \(k\)), \(\nabla f=\sum_i\lambda_i\nabla g_i\). Regularity is a substantive hypothesis.

With \(f=x^2+y^2\), \(g=x+y-b\), \(x=y=b/2\), optimal value \(V(b)=b^2/2\), and \(V'(b)=b=\lambda\) under the convention \(\nabla f=\lambda\nabla(x+y-b)\). For the singular constraint \(x^2+y^2=0\), \(\nabla g(0)=0\), so the multiplier necessary condition is inapplicable.

### Exercises with answers

1. Maximize \(xy\) subject to \(x+y=2\) over real x,y. **Answer:** maximum one at \((1,1)\); there is no minimum because \(x(2-x)\to-\infty\).
2. Find extrema of \(x\) on \(x^2+y^2=4\). **Answer:** maximum two at \((2,0)\), minimum minus two at \((-2,0)\).
3. Why does \(\nabla f=0\) need not hold at a constrained extremum? **Answer:** only derivatives along feasible tangent directions must vanish.
4. Give a singular constraint. **Answer:** \(x^2+y^2=0\) at the origin has vanishing constraint gradient.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), Lagrange multipliers.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), constrained optimization.
- [Lagrange multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier); [Karush–Kuhn–Tucker conditions](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions), an extension to inequality constraints.
