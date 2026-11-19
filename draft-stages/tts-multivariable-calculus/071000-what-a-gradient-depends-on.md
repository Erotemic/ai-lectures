# What a Gradient Depends On: Differentials, Geometry, and Steepest Descent

<!-- BEGIN SPOKEN LECTURE -->

# What a Gradient Depends On: Differentials, Geometry, and Steepest Descent

A map tells you how elevation changes across a landscape. At a point on the map, you would like an arrow pointing most steeply uphill. That seems like a straightforward calculus question. Take the partial derivatives and put them together into a vector called the gradient. But there is a hidden choice in that recipe. What do we mean by the length of an arrow? What counts as a step of the same size in two different directions?

If both map coordinates measure the same physical distance, the ordinary Euclidean answer is sensible. If one coordinate measures kilometers and another measures minutes, a coordinate arrow does not come with a natural physical length. Before choosing the steepest direction, we must decide how to compare moves. This lecture connects three ideas that are often taught apart: the derivative as a linear measurement, the gradient as a vector chosen using geometry, and steepest descent as an optimization rule.

## The derivative is a measurement, not yet an arrow

Suppose a scalar function f assigns a number to every point in a two-dimensional coordinate system. Starting at point p, move by a small displacement h. Differentiability means that the change in f is approximately a linear function of h, with an error negligible compared with the length of the displacement. This linear function is the differential of f at p.

For a concrete example, let f of x and y be x squared plus three x y. At the point one, two, change x by a little amount a and y by a little amount b. Expanding gives a first-order change of eight a plus three b. Terms involving a squared or a times b form the higher-order remainder. The differential is therefore the rule that sends the displacement a, b to the number eight a plus three b.

Notice what we have defined. We have defined a device for measuring displacement. Feed it a vector, and it returns a number. Such a linear measurement is called a covector, or a linear functional. The differential is an object in the dual space of the tangent vectors. Its coefficients are eight and three in these coordinates, but the differential itself is not fundamentally an arrow pointing somewhere.

Why insist on the distinction? Because the measurement has a simple meaning even when the coordinates are changed. It still gives the first-order change of the same physical quantity along the same displacement. Only the coordinate numbers change.

## How a gradient becomes an arrow

To get a gradient vector, we first select an inner product for measuring vectors. In Euclidean two-dimensional coordinates, the inner product of vectors a, b and c, d is a c plus b d. It lets us turn the linear rule eight a plus three b into the dot product of the vector eight, three with the displacement a, b. We call eight, three the Euclidean gradient.

This correspondence works because every linear functional in a finite-dimensional inner-product space can be represented by taking an inner product with a unique vector. The statement is a finite-dimensional case of the Riesz representation principle. The derivative tells us what change to measure. The inner product tells us which vector represents that measurement.

We can use another inner product. Imagine that moving one unit in the x direction has cost one, while moving one unit in the y direction has cost three times as much in the sense of length. Define the squared length of a displacement to be a squared plus nine b squared. This length corresponds to the positive-definite metric matrix with diagonal entries one and nine.

What vector now represents the differential eight a plus three b? We seek components g-one and g-two such that the inner product of the vector g with any displacement a, b gives eight a plus three b. In this metric, the inner product contributes g-one times a plus nine g-two times b. Therefore g-one is eight and g-two is one third. The gradient vector in this geometry is eight, one third, not eight, three.

Both vectors represent exactly the same differential when paired with the matching inner products. Neither is an arithmetic mistake. They answer the question after two different geometric choices.

## Steepest is a constrained question

Now consider the direction of greatest increase. We might try every possible displacement and choose the one that makes the differential largest. Without any size restriction, that problem has no answer: multiplying a favorable displacement by ten makes the predicted increase ten times larger. We must compare displacements of equal length.

Fix a metric and restrict attention to displacements of metric length one. The Cauchy–Schwarz inequality tells us that the differential in a unit direction cannot exceed the metric length of the gradient. Equality occurs when the displacement points along the metric gradient. Therefore the direction of steepest ascent is the metric gradient normalized to unit metric length. Steepest descent points in the opposite direction.

In a general coordinate system, if the metric is represented by a symmetric positive-definite matrix G, the differential has a column of coefficients, and the gradient vector is G inverse times that column. The coordinate formula is short. Its meaning is that we translate a linear measurement into a displacement using our selected geometry.

A gradient-descent iteration moves against this vector, usually multiplied by a step size. Change the metric, and you change the direction of a step. That is why a choice of metric can act as a preconditioner for optimization.

## A two-coordinate quadratic, measured two ways

Take the objective f of x and y equal to the square of x minus one, plus nine times the square of y minus one. The unique minimum lies at one, one. At the origin, the ordinary gradient has components minus two and minus eighteen. So a Euclidean gradient-descent step points strongly toward increasing y. With step size one tenth, the proposed new point is two tenths, one point eight. It overshoots the minimum badly in the steep y direction.

Now equip parameter space with the metric whose squared length is the x displacement squared plus nine times the y displacement squared. The metric gradient at the origin has components minus two and minus two. A step of size one half against that gradient moves directly to one, one, the minimizer. The metric has compensated for the different scale of the two quadratic terms.

This does not prove that a particular metric solves every optimization problem. We chose a quadratic for which the metric matches the shape of the objective. If the objective changes across the domain, an effective metric may also change. If the metric badly approximates the curvature, performance can get worse. The point of the example is narrower and more useful: the apparently obvious Euclidean gradient direction was not an intrinsic feature of the objective. It depended on how we measured steps in parameter space.

We can see the same phenomenon through a change of coordinates. Introduce a new variable v equal to three y, and keep u equal to x. In the new coordinates, our objective becomes the square of u minus one plus the square of v minus three. Ordinary Euclidean geometry in u, v corresponds exactly to the weighted geometry in x, y. A Euclidean gradient step in the well-scaled variables, mapped back to x, y, is a metric-gradient step in the original variables.

The numbers of a gradient vector do not transform the way the numbers of a differential do. The differential transforms like a covector, by the transpose of the coordinate change. A gradient transforms like a vector only after we transform the metric consistently.

## Units can reveal a bad geometry

Suppose one parameter is a distance measured in meters, and another is the same kind of distance measured in millimeters. Changing the unit label should not alter the physical direction we recommend moving. Yet if we compute a bare Euclidean gradient in the two coordinate lists without adjusting the metric, the relative sizes of the components change when we convert units. A numerical algorithm may then behave very differently.

This is not a reason to ban Euclidean gradients. It is a reason to make the scaling choice visible. Standardizing features in a regression, nondimensionalizing a physical model, or selecting a diagonal preconditioner are all ways of introducing a considered geometry. Sometimes they are also necessary to make a numerical calculation stable. The correct choice depends on the meaning of the parameters and the objective, not on a universal rule that all coordinates deserve equal numerical weight.

In statistical estimation, one may choose a metric related to how sensitively a probability model changes when its parameters move. The Fisher information matrix provides such a local geometry under regularity and identifiability assumptions. A natural-gradient method uses the inverse of this matrix, or an approximation to it, to translate score covectors into steps. This is the same derivative-versus-gradient distinction on a richer space. But a singular information matrix may prevent a unique inverse, and a natural gradient is not automatically the right algorithm for every statistical task.

## Constraints add one more geometric layer

Imagine that the point must stay on a circle. An arbitrary gradient may point off the circle. A feasible first-order motion must lie in the tangent line at the current point. The derivative still tells us the first-order change in every direction, but only tangent directions are allowed. The direction of steepest feasible increase is obtained by projecting the metric gradient onto that tangent line, using the selected metric.

At a constrained optimum, the differential can be nonzero in the ambient plane even though it vanishes along every allowed tangent direction. This is the geometric origin of Lagrange multipliers. The differential of the objective can be a combination of differentials of active constraints. It does not mean the entire gradient vector must vanish.

For a concrete check, maximize x plus two y on the unit circle. The Euclidean gradient is the constant vector one, two. The maximum occurs where the radial unit vector points in this direction: at x equal to one over the square root of five and y equal to two over the square root of five. At that point the gradient is normal to the circle, so its tangent projection is zero. The objective is not flat in every direction in the plane, but it is stationary under feasible infinitesimal motions.

## What carries across subjects

Calculus gives a differential, a linear map that measures infinitesimal change. Linear algebra supplies inner products that convert measurements into vectors. Optimization uses that conversion to choose a direction of improvement subject to a notion of step size. Statistics and physics supply meaningful scales or metrics, making some directions more costly, variable, or informative than others.

The next time you see a gradient, ask two questions before using it. First, which linear measurement of displacement does it represent? Second, which inner product was used to turn that measurement into an arrow? If you can answer both, coordinate changes, optimization step directions, Lagrange multipliers, and metric-aware algorithms become parts of one idea rather than separate collections of formulas.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Differential and metric gradient

For \(f:U\subset\mathbb R^n\to\mathbb R\), \(df_p\) is a covector. With an SPD metric \(G(p)\), define \(\operatorname{grad}_G f\) by

\[
  df_p[h]=\langle\operatorname{grad}_G f,h\rangle_G
  =(\operatorname{grad}_G f)^T G h,
  \qquad \operatorname{grad}_G f=G^{-1}\nabla_E f.
\]

Cauchy–Schwarz gives \(\sup_{h^TGh=1}df_p[h]=\|\operatorname{grad}_G f\|_G=\sqrt{(df_p)^TG^{-1}(df_p)}\), with maximizer proportional to \(\operatorname{grad}_G f\) when this gradient is nonzero.

### Coordinate changes

For the linear change \(x=Bz\) with invertible \(B\), the covector transforms by \((df)_z=B^T(df)_x\), while \(G_z=B^TG_xB\). Consequently \((\operatorname{grad} f)_z=B^{-1}(\operatorname{grad} f)_x\). For nonlinear reparameterizations these hold locally with \(B\) replaced by the Jacobian at the point.

Example: \(f(x,y)=x^2+3xy\), \(p=(1,2)\), \(df_p=(8,3)\), \(G=\operatorname{diag}(1,9)\), so \(\operatorname{grad}_G f=(8,1/3)\).

### Quadratic and constrained example

\[
 f(x,y)=(x-1)^2+9(y-1)^2,
 \quad \nabla f(0,0)=(-2,-18),
 \quad \operatorname{grad}_{\operatorname{diag}(1,9)}f(0,0)=(-2,-2).
\]

The metric-gradient iteration with step \(1/2\) goes from \((0,0)\) to \((1,1)\). On \(x^2+y^2=1\), the tangent space is \(T_pS^1=\{h:p^Th=0\}\). The projected Euclidean gradient for \(f=x+2y\) vanishes at \(p=(1,2)/\sqrt5\), the maximizer.

### Exercises and solutions

1. **Metric scaling.** For \(df=(2,8)\) and \(G=\operatorname{diag}(1,4)\), find the metric gradient. **Answer:** \((2,2)\).
2. **Unit ascent.** Normalize the previous metric gradient. **Answer:** \((2,2)/\sqrt{20}\), since its squared metric length is \(4+16=20\).
3. **Parameter change.** For \(x=2u\), \(y=v/3\) and \(df_x=(4,6)\), calculate \(df_{(u,v)}\). **Answer:** \((8,2)\).
4. **Feasible directions.** At \(p=(1,0)\) on the unit circle, identify the tangent space and derivative of \(f=x+2y\) along its upward unit tangent. **Answer:** vertical vectors; derivative equals \(2\).
5. **Singular metric.** What fails when \(G=\operatorname{diag}(1,0)\)? **Answer:** it does not define an inner product on all directions, so gradient representation and unit-direction optimization need additional structure.

### Sources and further reading

- [MIT OCW 18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), total derivatives and directional derivatives.
- [Sheldon Axler, *Linear Algebra Done Right*](https://linear.axler.net/), dual spaces, linear functionals and inner products.
- [Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), scaling, gradients, constraints and optimization geometry.
- Related lectures: `multivariable-calculus:067000`, `linear-algebra:012000`, `optimization-duality:005000`, `multivariable-calculus:027000`.
