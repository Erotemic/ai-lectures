# Constraints as Geometry: Tangent Spaces and the Hessian of the Lagrangian

**Track:** Multivariable Calculus from First Principles. **Focus:** derive equality-constrained optimality from feasible curves, explain why the Hessian of the Lagrangian is the correct curvature, and identify when second-order tests apply.

<!-- BEGIN SPOKEN LECTURE -->

# Constraints as Geometry: Tangent Spaces and the Hessian of the Lagrangian

Imagine a point moving on a circle. You can tell it to move left, but if it is already at the leftmost point, there is no way to move farther left without leaving the circle. This makes the leftmost point a minimum of its horizontal coordinate, even though the horizontal coordinate, considered as a function on the entire plane, has no minimum at all. Its gradient is constant and never vanishes. Its Hessian is zero everywhere.

This is our starting puzzle: how can a function with no unconstrained stationary point have a sharply defined constrained minimum? The ordinary rule, set the gradient to zero, is the wrong rule because it permits directions the constraint forbids. We need a way to differentiate only along paths that stay feasible. Once we do that, Lagrange multipliers and the less familiar Hessian of the Lagrangian emerge from the same calculation.

The destination is a second-order test that we can actually use in Newton's method. We will derive it, test it on a circle and a line, and distinguish the hypotheses that make the test meaningful from the equations that are merely convenient to write down.

## Which directions exist?

Write the decision vector as x with n components. Suppose there are m smooth equality constraints, assembled in a vector function c of x, and feasibility means that every component of c is zero. Think of two measurements defining a curve in three-dimensional space, or one equation defining a surface. At a feasible point, differentiate all the constraint functions. Their derivatives form a matrix J with one row for each constraint and one column for each variable.

Take any differentiable feasible path x of t passing through our point when t is zero. Because c of x of t stays zero, the chain rule says that J times the path's velocity at zero must be zero. The allowed first-order velocities therefore lie in the null space of J. This is the tangent space, provided J has full row rank in a neighborhood of the point. Under that regularity assumption, every vector in the null space is the initial velocity of some nearby feasible curve. Without that assumption, the linear equation can claim that directions are available when the true feasible set is singular or isolated.

Here is the first geometric idea worth keeping: a smooth equality constraint removes degrees of freedom. If J has m independent rows, it removes m independent directions, leaving n minus m tangent dimensions. A proposed change that points outside the tangent space violates feasibility already to first order. A change inside it respects the linearized constraints, but may still leave the feasible set by a second-order amount. The tangent line to a circle is not the circle.

At a constrained local minimum, every feasible curve through the point has a one-variable local minimum of the objective. Its first derivative must be zero. Thus the objective gradient must have zero dot product with every tangent vector. In linear algebra terms, it is perpendicular to the null space of J. The orthogonal complement of that null space is the row space of J, so the objective gradient belongs to the span of the constraint gradients.

We express the resulting balance as the objective gradient plus J transpose times a vector of multipliers equals zero. The multiplier vector is often called lambda. For equality constraints its components can have either sign. We have not guessed this equation: we have obtained it by applying a one-variable derivative test to all feasible curves and then using a fact about null spaces.

Under independent constraint gradients, these multipliers are unique at a given stationary point. Redundant constraints can produce many multiplier vectors, or can prevent us from using this straightforward derivation. The rank assumption is about the representation of the feasible geometry, not about whether the objective happens to be convex.

## Why a circle requires a different Hessian

Return to the circle of radius one, and minimize the horizontal coordinate x. The constraint is x squared plus y squared minus one equals zero. The minimum occurs at negative one, zero. The objective gradient points in the positive horizontal direction. The constraint gradient at that point points in the negative horizontal direction, with magnitude two. To make stationarity hold, its multiplier must be one half.

The objective has zero second derivatives. Yet a little feasible motion away from the leftmost point increases x, so the minimum has real curvature when viewed along the circle. Where did the curvature go? It lives in the constraint, because a feasible curved path has acceleration as well as velocity.

To see this, differentiate the constraint along a feasible path a second time. The result contains two pieces: J times the path's acceleration, and a quadratic expression in its velocity involving the second derivatives of the constraints. Their sum is zero. Next differentiate the objective along that same path twice. Its second derivative contains the usual Hessian quadratic form in the velocity, but it also contains the objective gradient dotted with the path's acceleration.

At a stationary constrained point, replace the objective gradient using our multiplier equation. Then replace the constraint-gradient acceleration term using the twice-differentiated feasibility equation. The acceleration vanishes from the final expression. What remains is the quadratic form of the objective Hessian plus the multiplier-weighted sum of constraint Hessians, applied to the tangent velocity.

That matrix is the Hessian with respect to x of the Lagrangian: the objective plus each multiplier times its constraint. Notice that the multiplier is held fixed while differentiating with respect to x. We have derived a formula for actual second variation along feasible curves. It is not a cosmetic modification of the unconstrained Hessian.

On the circle at the leftmost point, the objective Hessian is zero and the constraint Hessian is two times the identity. Multiplying it by lambda equal to one half produces the identity matrix. A vertical tangent velocity of magnitude one therefore has second variation equal to one, which is positive. Indeed, a local circle parameterization near the leftmost point gives a horizontal coordinate of approximately negative one plus half the square of the vertical displacement.

At the rightmost point, the same stationarity equation produces lambda equal to negative one half. The Lagrangian Hessian is negative the identity, and the point is a constrained maximum, not a minimum. The function, constraint, and tangent-space dimension have not changed. The multiplier has recorded which side of the curved feasible set we are examining.

## What second-order conditions actually say

For a twice continuously differentiable problem with equality constraints whose Jacobian has full row rank, a local minimum satisfies first-order stationarity for some multipliers. Moreover, its Lagrangian Hessian must have a nonnegative quadratic form on every tangent direction. If we find a tangent direction with strictly negative curvature, the point cannot be a constrained local minimum.

Nonnegative curvature is a necessary condition, not a sufficient one. A flat quadratic test can miss the behavior of fourth or higher powers, just as in one-variable calculus. But if stationarity holds and the Lagrangian Hessian is strictly positive in every nonzero tangent direction, the point is a strict local minimum. Under the stated smoothness and regularity assumptions, we can parameterize the nearby feasible set by its free coordinates. The ordinary second-order Taylor expansion in those coordinates then has a positive quadratic term that dominates its smaller remainder.

The condition is about tangent directions, not every direction in the ambient space. The Lagrangian Hessian can be indefinite as a full matrix and still be positive definite on the directions that matter. It is equally important not to apply the unconstrained objective Hessian when the constraints are curved. Neither shortcut gives the correct general test.

A useful computational form chooses a matrix Z whose columns form a basis of the null space of J. Every tangent direction can be written as Z times a shorter vector. The reduced Hessian is Z transpose times the Lagrangian Hessian times Z. Testing that smaller matrix for positive definiteness gives exactly the tangent-space criterion. This bridges geometry to numerical linear algebra: choose a basis of feasible directions, then study curvature only there.

## A line where everything can be calculated

Consider minimizing the sum of the squared distances of x and y from two, subject to x plus y equals one. The line constraint has gradient one, one, so tangent motions add an amount to x and subtract the same amount from y. Both squared terms prefer their coordinate to be two, but that preference conflicts with the sum constraint.

The stationarity equations say that two times the quantity x minus two, plus lambda, equals zero, and the same equation holds for y. Subtract the equations: x and y must be equal. With their sum fixed at one, both equal one half. Substitute either back to obtain lambda equal to three.

The constraint is affine, so its Hessian is zero. The Lagrangian Hessian is simply twice the identity. A tangent direction with coordinates one and negative one has positive quadratic form equal to four. Therefore our stationary point is a strict local minimum. Because the squared-distance objective is globally convex and the feasible set is an affine line, it is also the unique global minimum.

Compare this with the circle. For an affine constraint the feasible set has no intrinsic curvature, and the objective Hessian already contains all the relevant second-order information. For a curved constraint the multiplier times constraint Hessian cannot generally be discarded. This distinction is the essential preparation for constrained Newton methods.

## What happens when the constraint is singular?

There is a short example in one variable that prevents overconfidence. Minimize x subject to x squared equals zero. The only feasible point is x equal to zero. It is automatically the global minimum and the global maximum on that feasible set.

But at zero, the constraint derivative vanishes. No multiplier can cancel the objective derivative, which equals one. The familiar stationarity equation has no solution. This is not evidence that the feasible point is wrong; it is evidence that our regularity assumption failed. The formal null space of the zero constraint derivative would be the whole line, even though there is no feasible curve moving away from zero. Linearization has lost the geometry.

There are more sophisticated constraint qualifications that apply beyond independent equality gradients, especially with inequalities. But none should be invoked as a ceremonial phrase. We need to know exactly what it guarantees: the tangent description, the existence of multipliers, or the validity of a second-order test.

The lesson from feasible curves is now complete. First derivatives identify the directions a feasible point can move. Lagrange multipliers translate objective stationarity into linear algebra. Second derivatives of the constraints then restore the curvature that a tangent approximation alone has discarded. A constrained optimizer is not just an unconstrained optimizer with an extra equation attached: it lives on a geometry that determines the right equations and the right Hessian.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Feasible paths and the first and second variations

Let \(f,c_i\in C^2\) near \(x_*\in\mathbb R^n\), \(c(x_*)=0\), and \(J=Dc(x_*)\in\mathbb R^{m\times n}\) have full row rank \(m\leq n\). The implicit function theorem gives a local feasible manifold of dimension \(n-m\) with tangent space \(T_{x_*}=\ker J\).

For any \(C^2\) feasible curve \(x(t)\) with \(x(0)=x_*\), \(d=x'(0)\), \(a=x''(0)\),

\[
Jd=0,\qquad Ja+\begin{bmatrix}d^\top\nabla^2c_1(x_*)d\\\vdots\\d^\top\nabla^2c_m(x_*)d\end{bmatrix}=0.
\]

At a local minimum \(\nabla f(x_*)+J^\top\lambda_*=0\). For \(L(x,\lambda)=f(x)+\lambda^\top c(x)\),

\[
\frac{d^2}{dt^2}f(x(t))\bigg|_{t=0}
=d^\top\nabla^2 f(x_*)d+\nabla f(x_*)^\top a
=d^\top\underbrace{\left(\nabla^2 f(x_*)+\sum_{i=1}^m\lambda_{*,i}\nabla^2c_i(x_*)\right)}_{H_L}d.
\]

Necessity: \(d^\top H_Ld\geq0\) for every \(d\in\ker J\). Sufficiency for a **strict local minimum**: stationarity and \(d^\top H_Ld>0\) for every nonzero \(d\in\ker J\), with the smoothness and rank hypotheses above. An orthonormal null-space basis \(Z\) yields the reduced Hessian \(Z^\top H_LZ\). Positivity on the tangent is not necessarily positivity on \(\mathbb R^n\).

### Two explicit geometries

**Circle:** \(f(x,y)=x\), \(c(x,y)=x^2+y^2-1\). At \((-1,0)\), \(\lambda_*=1/2\), \(H_L=I\), and \(\ker J=\mathrm{span}\{(0,1)\}\). At \((1,0)\), \(\lambda_*=-1/2\) and \(H_L=-I\). The objective Hessian alone is zero at both points.

**Affine line:** \(f(x,y)=(x-2)^2+(y-2)^2\), \(c=x+y-1\). At \((1/2,1/2)\), \(\lambda_*=3\), \(H_L=2I\). Taking \(d=(1,-1)\) gives \(d^\top H_Ld=4>0\).

### Exercises with answers

1. **Constraint sign:** replace \(c=0\) by \(-c=0\). What happens to \(\lambda_*\) and \(H_L\)? **Answer:** the multiplier changes sign; the product \(\lambda c\), and thus \(H_L\), is unchanged.
2. **A curved graph:** minimize \(f(x,y)=y\) subject to \(c(x,y)=y-x^2=0\). Classify \((0,0)\). **Answer:** \(\nabla f=(0,1)\), \(\nabla c=(0,1)\), \(\lambda=-1\), \(H_L=\mathrm{diag}(2,0)\). The tangent is horizontal; its quadratic form is strictly positive, so the point is a strict local minimum.
3. **A degenerate constraint:** for \(c(x)=x^2\), compute \(Dc(0)\), its kernel, and the actual feasible set. **Answer:** \(Dc(0)=0\), so the linearized kernel is all of \(\mathbb R\), but the feasible set contains only zero. The full-row-rank premise is false.
4. **Reduced curvature:** let \(H=\mathrm{diag}(-3,2)\) and \(J=(1,0)\). Is \(H\) acceptable for a strict constrained second-order minimum? **Answer:** yes: feasible tangent vectors are \((0,t)\), with quadratic form \(2t^2>0\) for \(t\ne0\), although \(H\) is indefinite in ambient space.

### Sources and further reading

- S. Boyd and L. Vandenberghe, [*Convex Optimization*, §§5.5, 10.1–10.2](https://web.stanford.edu/~boyd/cvxbook/), for Lagrangian stationarity and constrained Newton geometry (with convexity assumptions made explicit there).
- [Stanford CME307/MS&E311, Lecture Note 07: Second-Order Necessary Conditions for Constrained Optimization](https://web.stanford.edu/class/msande314/lecture07.pdf), for the Hessian of the Lagrangian restricted to tangent spaces.
- [Wikipedia: Lagrange multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier) and [Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem), for orientation on the geometric concepts.

*Teaching connections:* `multivariable-calculus:020000` develops Hessian curvature; `multivariable-calculus:021000` explains unconstrained Newton systems; `optimization-duality:004000` covers multipliers as convex optimality certificates.
