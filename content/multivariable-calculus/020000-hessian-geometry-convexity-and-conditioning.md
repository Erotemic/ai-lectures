# Hessian Geometry: Curvature, Convexity, and Conditioning

**Track:** Multivariable Calculus from First Principles. **Focus:** read a quadratic form geometrically, distinguish local and global curvature claims, and derive the estimates used to analyze first- and second-order algorithms.

<!-- BEGIN SPOKEN LECTURE -->

# Hessian Geometry: Curvature, Convexity, and Conditioning

Two functions can have the same minimizer, the same minimum value, and completely different computational difficulty. One has circular level curves, while another has a long, thin valley. A gradient points uphill in both cases. Yet a small step that is safe across the narrow direction may make very little progress along the long one. The Hessian explains why.

We will begin with a quadratic function whose curvature we can analyze exactly. Then we will ask which facts survive for nonlinear functions, which require hypotheses throughout a region, and which are only local statements at a point. The goal is to connect the classification of critical points with the numerical behavior of optimization methods.

## The Hessian turns displacement into an energy

Start with a symmetric matrix A and a vector b. Let f of x equal one half x transpose A x minus b transpose x. Its gradient is A x minus b, and its Hessian is simply A. The function is exactly its own second-order Taylor polynomial. There is no approximation error anywhere.

Assume A is positive definite. There is exactly one point where the gradient vanishes, because A is invertible. At that point A x equals b. Write the displacement from this solution as h. When we expand the quadratic around the solution, the linear term cancels, and the increase in objective value is precisely one half h transpose A h.

This identity does three jobs. It proves the solution is a strict global minimizer. It measures how costly each error direction is. And it reveals that solving a linear system with a symmetric positive-definite matrix is equivalent to minimizing a quadratic energy.

The eigenvectors of A give a natural coordinate system for that energy. An eigenvector with a large positive eigenvalue is a steep direction: a small displacement changes the function sharply. An eigenvector with a small positive eigenvalue is a shallow direction: the same displacement changes the function only slightly. The matrix may be large, but the geometry is the sum of independent squared coordinates after an orthogonal rotation.

## A valley that is tilted relative to the axes

Consider the matrix with rows five, four and four, five. Its eigenvalues are nine and one. Along the direction where x and y increase together, curvature is nine. Along the direction where one increases while the other decreases, curvature is one.

Let b have both entries equal to one. The unique minimizer of the associated quadratic has both coordinates equal to one ninth. This can be checked without a matrix inverse: multiplying the matrix by the vector one ninth, one ninth gives the vector one, one.

Imagine standing above the graph and looking down at level curves. The contours are ellipses, tilted by forty-five degrees relative to the original axes. Their long direction is where the curvature is one; their short direction is where the curvature is nine. The difference between these curvatures is why an algorithm that takes a single scalar step size can move unevenly.

For ordinary gradient descent, the update is current x minus step size times the gradient. Subtract the exact minimizer and call the difference e. One iteration multiplies the error by the matrix I minus step size times A. In an eigenvector direction with eigenvalue lambda, the error is multiplied by one minus the step size times lambda.

Choose step size one ninth. The steep direction is corrected completely in one iteration. But the shallow direction is multiplied by eight ninths. After ten steps it still retains roughly a third of its original size. The method is not broken. It is faithfully obeying the local geometry while limited to one scale for all directions.

Now take a Newton step for this same quadratic. Newton uses the Hessian to solve for a direction rather than just multiplying the gradient by a number. Because the Hessian is constant, the exact Newton step moves directly to the minimizer in one iteration from any starting point. Both methods use derivatives; only one resolves the different curvatures explicitly.

## Condition numbers are ratios of curvatures

For a positive-definite matrix, the spectral condition number is the largest eigenvalue divided by the smallest. In our example, it is nine. A larger ratio means greater disparity between steep and shallow directions, measured in the chosen Euclidean coordinates.

This ratio matters in two related but distinct settings. As a linear system, A x equals b may amplify relative input perturbations in particular directions. As an optimization problem, the same eigenvalue spread limits how rapidly simple fixed-step gradient descent can reduce errors. The numbers are related because the optimization problem's first-order condition is the linear system.

But the condition number is not the shape of the function in some coordinate-free sense. If we rescale the variables, the numerical Hessian changes. For example, one half of one hundred x squared plus y squared has level curves that are narrow in the original x direction. Replacing x by a new variable ten times x makes the expression circular in the new coordinates. The optimization problem has not changed its set of physical states; we changed the units and therefore the metric in which we measure steps.

This is the motivation behind preconditioning. Rather than accepting the coordinate system in which the problem was first written, we seek a transformation that makes the geometry easier for our algorithm. The transformation must be handled consistently: gradients, Hessians, constraints, and notions of length all change with coordinates.

## From a matrix at one point to a guarantee on a region

For a nonlinear function, the Hessian changes as we move. The claim that the Hessian at the origin is positive definite says something local. It does not imply convexity throughout the plane.

Consider f of x equal x squared minus x to the fourth. At zero its derivative vanishes and its second derivative is positive. The origin is indeed a strict local minimum. Yet for sufficiently large absolute x the negative fourth-power term dominates, and the function decreases without bound. Its local curvature says nothing about a global minimum.

To derive a claim throughout a convex region, we need a uniform hypothesis throughout that region. Suppose f is twice continuously differentiable and every Hessian in that region has all eigenvalues at least m, for some positive constant m. Then every direction has curvature at least m everywhere along any segment inside the region.

Apply the exact Taylor integral identity along the segment from x to y. The quadratic curvature contribution is at least m over two times the squared distance between x and y. Therefore f at y is at least f at x, plus the gradient at x dotted with y minus x, plus m over two times the squared distance. This is a strong-convexity inequality.

It says more than ordinary convexity, which merely places the graph above its tangent plane. It says how far above the tangent plane the graph must rise. If a stationary point lies in the region and the region is the domain of interest, the inequality proves its global uniqueness as a minimizer there.

We can obtain an upper companion inequality if every Hessian eigenvalue is at most M on the region. Then the function value at y is at most the tangent-plane prediction plus M over two times the squared distance. The two inequalities trap the function between quadratic models. Lower curvature controls uniqueness and error; upper curvature controls how large a step can safely be.

There is an important qualification: these inequalities apply when the entire segment stays in the region on which the Hessian bounds were assumed. A proof cannot use a local bound to certify a remote point outside that region.

## How the gradient certifies distance from the minimizer

Suppose the function has a minimizer x star with zero gradient, and the Hessian is bounded below by m times the identity along the relevant segments. Strong convexity makes the gradient not merely a direction of increase but a measure of how far we may be from x star.

To see why, write the difference between the gradients at x and x star as the integral of Hessian matrices applied to the displacement. Dot with the displacement. The lower curvature bound gives at least m times the squared distance. Cauchy–Schwarz bounds the same dot product above by the gradient length at x times the distance. If the distance is nonzero, cancel one factor. The result says that the distance to the minimizer is at most the gradient length divided by m.

Thus, if we know a genuine uniform lower-curvature bound and we have computed a small gradient, we can bound the position error. Without a lower bound, a tiny gradient may simply indicate a very flat region. A small gradient alone is not a proof of closeness to any particular optimum.

There is also a useful function-value estimate. Strong convexity implies the objective gap between x and the minimizer is at most the squared gradient length divided by twice m. This follows by placing the minimizer into the lower quadratic inequality and minimizing its right-hand side over hypothetical displacements.

The hypotheses matter. We assume the relevant minimizer exists and the lower-curvature condition holds along the connecting segment. In constrained problems, zero gradient can fail at the optimum because the feasible boundary supplies an opposing force; then the certificate must be adapted to the constraints.

## The limits of the Hessian test

At a stationary point, a positive-definite Hessian is sufficient for a strict local minimum. A negative-definite Hessian gives a strict local maximum. An indefinite Hessian gives directions of both increase and decrease. These familiar tests are consequences of Taylor's formula with a remainder smaller than the quadratic term.

But a zero eigenvalue leaves a gap in the reasoning. At the origin, x squared plus y to the fourth has a strict local minimum. The function x squared minus y to the fourth does not. Their Hessians at the origin are identical: one positive eigenvalue, one zero eigenvalue. No second-order calculation at that single point can distinguish them.

Likewise, positive semidefiniteness at a point is not the same as convexity on a neighborhood. A convex function that is twice differentiable does have a positive-semidefinite Hessian throughout its convex domain. The converse requires the positive-semidefinite condition throughout the region, not just at the candidate solution.

There is a related distinction between a nonnegative quadratic form and a strictly positive one. If A has a zero eigenvalue, a quadratic objective can be flat along that direction, and minimizers may fail to be unique. Strong convexity rules out precisely this degeneracy, which is why it appears so often in uniqueness and convergence theorems.

## When the geometry becomes an algorithm

Hessian analysis unifies several ideas that can otherwise seem unrelated. Local calculus classifies extrema. Matrix spectral theory describes steep and shallow directions. Positive definiteness makes a linear equation into an energy minimization problem. Conditioning predicts sensitivity. Preconditioning changes the scales in which we solve. And the lower and upper Hessian bounds turn geometric intuition into inequalities suitable for proofs.

The next conceptual step is to let the Hessian change at each iteration. Newton's method takes the idea of solving one quadratic exactly, rebuilds that quadratic at the current point, and repeats. Its power comes from adapting to curvature. Its difficulties come from forgetting that each quadratic is only a local approximation, and from mistaking a stationary point for a guaranteed minimum.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Quadratic example

\[
A=\begin{pmatrix}5&4\\4&5\end{pmatrix},\quad b=(1,1)^T,\quad
f(x)=\tfrac12x^TAx-b^Tx,\quad x_*=(1/9,1/9)^T.
\]

The normalized eigenvectors \(q_+=(1,1)^T/\sqrt2\), \(q_-=(1,-1)^T/\sqrt2\) have eigenvalues \(9\) and \(1\). Thus \(f(x)-f(x_*)=\tfrac12(9u^2+v^2)\) for \(x-x_*=uq_++vq_-\). With gradient step \(\alpha=1/9\), the multipliers are \(1-9\alpha=0\) and \(1-\alpha=8/9\).

Newton solves \(Ap=-\nabla f(x)=-A(x-x_*)\), hence \(p=x_*-x\), reaching \(x_*\) in one step.

### Strong convexity and smoothness from Hessian bounds

For all segments in a convex domain \(D\), if \(mI\preceq\nabla^2 f(z)\preceq MI\) with \(0<m\le M\), then

\[
 f(y)\ge f(x)+\nabla f(x)^T(y-x)+\frac m2\|y-x\|^2,
\]
\[
 f(y)\le f(x)+\nabla f(x)^T(y-x)+\frac M2\|y-x\|^2.
\]

The first yields, for an interior minimizer \(x_*\) with \(\nabla f(x_*)=0\),

\[
\|x-x_*\|\le\frac{\|\nabla f(x)\|}{m},\qquad
0\le f(x)-f(x_*)\le\frac{\|\nabla f(x)\|^2}{2m}.
\]

For the distance bound, use \((\nabla f(x)-\nabla f(x_*))^T(x-x_*)\ge m\|x-x_*\|^2\); for the gap bound use strong convexity at \(x\), evaluate at \(x_*\), and complete the square in \(x_*-x\).

### Exercises with solutions

1. **Tilted ellipses.** Write the objective increase in the two normalized eigenvector coordinates of the worked example. **Answer:** \((9u^2+v^2)/2\).
2. **Local versus global.** Does \(f''(0)>0\) for \(f(x)=x^2-x^4\) imply global convexity? **Answer:** no; \(f''(x)=2-12x^2\), which is negative when \(|x|>1/\sqrt6\).
3. **Strong convexity.** If \(m=2\) and the gradient has norm at most \(0.04\), bound the distance to an interior optimum. **Answer:** at most \(0.02\), assuming the lower bound along the connecting segment.
4. **Flat direction.** Explain why \(x^2+y^4\) need not be strongly convex near zero even though it has a strict local minimum. **Answer:** the Hessian eigenvalue along the y direction is \(12y^2\), with infimum zero in every neighborhood of the origin.
5. **Change of units.** For \(f(x,y)=(100x^2+y^2)/2\), set \(u=10x\), \(v=y\). What is the Hessian in \((u,v)\)? **Answer:** the identity. The Euclidean metric/variable scaling has changed, not the physical objective.

### Sources and reading

- [Boyd and Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), Chapters 3 and 9 for curvature, strong convexity and unconstrained optimization.
- [MIT 6.854 notes on Newton's method](https://courses.csail.mit.edu/6.854/18/Notes/n19-newton_method.html), Hessian geometry and computational costs.
- [Wikipedia: Strongly convex function](https://en.wikipedia.org/wiki/Convex_function#Strongly_convex_functions), terminology and inequalities.
- [Wikipedia: Condition number](https://en.wikipedia.org/wiki/Condition_number), dependence of numerical sensitivity on the chosen norm.

For matrix factorizations and the positive-definite energy interpretation, see `linear-algebra:024000` and `linear-algebra:025000`. The earlier `multivariable-calculus:008000` gives the local critical-point test; this manuscript derives the uniform inequalities used by algorithms.
