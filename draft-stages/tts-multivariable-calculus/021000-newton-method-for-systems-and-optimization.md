# Newton's Method for Systems and Optimization: Building the Step

**Track:** Multivariable Calculus from First Principles. **Focus:** derive Newton's step for nonlinear equations and minimization, follow two concrete iterations, and distinguish a locally useful linear model from a global guarantee.

<!-- BEGIN SPOKEN LECTURE -->

# Newton's Method for Systems and Optimization: Building the Step

Suppose an equation is too complicated to solve by rearranging symbols. We have a guess, we can compute the equations and their derivatives at that guess, and we want a better guess. One answer is to replace the nonlinear equations, locally, by linear equations that we know how to solve. Then we repeat at the new point.

That is the central idea of Newton's method in several variables. It is deceptively simple: linearize, solve, update. But there are really two common Newton methods that share this pattern. One seeks a zero of a vector-valued function; the other seeks a stationary point of a scalar objective. They use different derivative matrices and have different interpretations. Mixing them up leads to mistakes about convergence and about what a successful step proves.

## Newton for a system of equations

Let F send a vector x of n real variables to a vector of n real residuals. We want F of x to equal the zero vector. Suppose F is differentiable near our current guess, and write J for its Jacobian matrix. The derivative tells us that for a small displacement p, F at x plus p is approximately F at x plus J at x times p.

The approximation gives an immediate proposal. Make the right-hand side of this linear model zero. Solve the linear system J times p equals minus F. Then set the new guess to x plus p.

We do not actually need to construct the inverse of J. We need to solve the system, using elimination, QR, or another reliable linear algebra method. In larger computations, solving this linear system is often the dominant cost of the iteration. The work on matrix factorizations and conditioning is therefore not separate from Newton's method; it is part of making each Newton step meaningful.

The equation for p is sometimes called the Newton correction. It is not a promise that the nonlinear residual after taking p will be exactly zero. We canceled the linearized residual. What remains is the nonlinear error of the model.

## A two-equation example

Let our first equation say that x squared plus y squared equals two. Let the second say that x equals y. Geometrically, we are looking for intersections of a circle with the diagonal line. There are two solutions, one at one, one, and one at minus one, minus one.

Define F with first component x squared plus y squared minus two, and second component x minus y. The Jacobian has first row two x and two y, and second row one and minus one.

Start at x equal to three halves and y equal to one half. We are not on the circle, and we are not on the diagonal. The residual vector is one half in the first component and one in the second. The Jacobian at this guess has rows three, one and one, minus one.

To compute the correction, solve three times p x plus p y equals minus one half, and p x minus p y equals minus one. The second equation gives p y equal to p x plus one. Substitute this into the first. Four p x plus one equals minus one half, so p x is minus three eighths. Then p y is five eighths.

After one Newton step, both coordinates become nine eighths. The line equation is now satisfied exactly because the line component was linear to begin with. But the circle equation still has a residual: two times nine eighths squared minus two, which equals seventeen thirty-seconds.

That nonzero residual is not a bug. In this particular problem, the first equation is quadratic. The residual after the step is exactly the sum of the two squared correction components. The linear part was canceled, leaving the second-order part. Here the correction components were minus three eighths and five eighths; their squares sum to seventeen thirty-seconds.

At the new point, both coordinates are equal, so the next Newton correction also changes them equally. One can reduce the iteration to the scalar update for solving t squared equals one: take the average of t and its reciprocal. Starting at nine eighths, the next common coordinate is one hundred forty-five over one hundred forty-four, about one point zero zero seven. We are much closer to the solution one, one.

This calculation exhibits both the power and the limitation of Newton's method. It uses a first-order system to capture most of the nonlinear behavior, but it leaves a second-order residual. Repeating the construction can shrink that residual very rapidly when the conditions are right.

## What happens when the Jacobian cannot be inverted?

The Jacobian is the local map from a proposed displacement to a predicted residual change. If it is singular, some residual directions cannot be reached by that linear approximation, or multiple corrections may fit the same prediction. The standard square Newton step may be undefined or nonunique.

In our circle-and-line example, the Jacobian determinant is minus twice the sum of x and y. Along the line x plus y equals zero, it vanishes. At the origin, the first Jacobian row is all zeros even though the first equation has residual minus two. No first-order correction can remove that first residual. We could still invent a step using second-order information or a different method, but it would not be the standard invertible-Jacobian Newton correction.

Singularity is not the only problem. A matrix may be invertible yet nearly singular. Then a modest residual can produce a very large correction, pushing the next guess far outside the region where the linearization is accurate. A condition estimate and a residual check on the linear solve help distinguish a trustworthy correction from an unstable calculation.

## Newton for optimization uses the gradient as its equation

Now change the problem. We have a scalar function f, and we want to minimize it. An interior local minimizer of a differentiable function must have zero gradient. So we could apply the root-finding Newton method to the vector function F equal to the gradient of f.

The Jacobian of the gradient is the Hessian. Thus the optimization Newton correction solves the Hessian at x times p equals minus the gradient at x. Then we update x by adding p.

There is another way to derive the same formula. Build the quadratic Taylor model of f at the current point. Its variable part is the gradient dotted with p, plus one half p transpose H p. Differentiate this model with respect to p. Its stationary point solves H p equals minus the gradient. If H is positive definite, that stationary point is the unique minimizer of the quadratic model.

These are equivalent algebraic derivations, but the second one highlights an important condition. We are seeking to minimize the model, not merely find where its slope vanishes. If H is negative definite, the stationary point of the model is a maximum. If H is indefinite, it is a saddle of the model. Newton's equation still produces a vector when H is invertible, but it may not be a descent direction for the true objective.

A positive-definite Hessian makes the Newton direction a strict descent direction whenever the gradient is nonzero. Indeed, dot the gradient with p. Because p is minus the solution of H times p equals the gradient, this dot product is negative. A short step in direction p then decreases f. A full step of length one can still be too large; the descent-direction property only guarantees improvement for sufficiently short positive step lengths.

## A saddle that Newton finds perfectly

Consider f of x and y equal x squared minus y squared. Its gradient is two x and minus two y. Its Hessian has two on the first diagonal entry and minus two on the second. At any point, the exact Newton correction is minus x and minus y. After one step, the iteration arrives at the origin.

Has optimization succeeded? No. The origin is a saddle: the function increases along the x direction and decreases along the y direction. Newton has solved the stationarity equations perfectly while failing to locate a minimum. We need more than a small gradient to identify a minimizer. Curvature, constraints, and sometimes global comparisons matter.

The distinction becomes especially important for complicated objectives. A root-finding algorithm reports a residual; an optimizer needs a claim about the objective. A stationary-point residual may be necessary evidence, but it is not by itself a certificate of optimality.

## Why a full Newton step can be dangerous

Even when H is positive definite at the current point, the quadratic model may stop being accurate far away. Suppose the Hessian changes rapidly. The Newton direction may point downhill initially, yet a full step can overshoot into a region where the objective increases. The tangent model is a local promise, not a global map.

A simple safeguard is damping. Instead of always taking the full correction p, choose a step length alpha between zero and one and update x by alpha p. We can test the candidate objective value and shorten alpha until the actual change agrees sufficiently with the predicted descent. For minimization this is a line-search method.

For root finding, we can use the squared norm of the residual, divided by two, as a merit function. When J is invertible and the Newton correction exactly solves J p equals minus F, the directional derivative of that merit function along p is minus the squared residual norm. Therefore sufficiently small positive steps reduce the merit function. This argument justifies backtracking locally, but it does not prove that a globally damped iteration must reach a root: the merit function may have stationary points with nonzero residual.

A second safeguard is a trust region. Rather than trusting the quadratic model for any correction, we minimize or reduce the model subject to a prescribed step-length limit. The radius changes according to how well the predicted reduction agrees with the actual reduction. This method asks for evidence before allowing the model to govern a large move.

Neither damping nor trust regions remove all difficulties. They are ways to manage the gap between the nonlinear function and its local approximation.

## Reusing the linear algebra carefully

In numerical code, the phrase inverse Hessian times gradient is convenient notation, but explicitly computing an inverse is usually not the appropriate step. Formulate the system and use a solver. For a symmetric positive-definite Hessian, Cholesky can exploit that structure. For large sparse systems, one might use a Krylov method with preconditioning. An indefinite Hessian calls for different treatment, because a positive-definite Cholesky factorization is not available without modifying the system.

This also raises a distinction between exact Newton and inexact Newton. If the linear system is solved only approximately, we leave some linearized residual. We may still obtain good steps, but the error analysis must account for both the nonlinearity of F and the inaccuracy of the linear solve. As the outer iterates approach a solution, how accurately should we solve the inner system? The answer depends on whether we want to preserve Newton's rapid local rate or spend less computation on early iterations.

## The question Newton leaves open

We have constructed Newton's correction from first principles and seen it work. But one good example does not prove that the iteration converges, much less how rapidly. What needs to be true near a target solution? We need the derivative matrix to remain invertible, the derivative to change in a controlled fashion, and the initial guess to lie in a region where those conditions apply.

With those assumptions, the model error becomes quadratic in the distance moved. Solving with a bounded inverse turns that quadratic residual into a quadratic error in the new point. This is the origin of Newton's famous local quadratic convergence. Its precise proof also explains why convergence can fail when we start too far away, when the derivative is singular, or when numerical linear algebra cannot supply an accurate correction.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Root-finding Newton step

For \(F:\mathbb R^n\to\mathbb R^n\), with Jacobian \(J(x)\), compute \(p\) from

\[
J(x)p=-F(x),\qquad x^+=x+p.
\]

For the example \(F(x,y)=(x^2+y^2-2,\,x-y)^T\),

\[
J(x,y)=\begin{pmatrix}2x&2y\\1&-1\end{pmatrix}.
\]

At \((3/2,1/2)\), \(F=(1/2,1)^T\), \(J=\left(\begin{smallmatrix}3&1\\1&-1\end{smallmatrix}\right)\), and \(p=(-3/8,5/8)^T\). Thus \(x^+=(9/8,9/8)^T\) and \(F(x^+)=(17/32,0)^T\). Exact quadratic residual identity:

\[
F(x+p)=F(x)+J(x)p+(p_x^2+p_y^2,0)^T.
\]

Next iteration from \((9/8,9/8)\) gives \(p=(-17/144,-17/144)\) and \(x^{++}=(145/144,145/144)\).

### Optimization Newton step and descent

For a twice differentiable objective \(f\),

\[
H(x)p=-\nabla f(x),\quad
m_x(p)=f(x)+\nabla f(x)^Tp+\tfrac12p^TH(x)p.
\]

If \(H(x)\succ0\) and \(\nabla f(x)\ne0\), then

\[
\nabla f(x)^Tp=-\nabla f(x)^TH(x)^{-1}\nabla f(x)<0.
\]

The sign guarantees descent for sufficiently short steps \(x+\alpha p\), not necessarily for \(\alpha=1\).

For \(\phi(x)=\tfrac12\|F(x)\|_2^2\), \(\nabla\phi=J^TF\); if \(Jp=-F\), then \(D\phi(x)[p]=F^TJp=-\|F\|^2\).

### Exercises with solutions

1. **Exact residual.** Compute the new circle residual after the first Newton step. **Answer:** \((3/8)^2+(5/8)^2=17/32\).
2. **Singular Jacobian.** Where is the Jacobian of the circle-and-line system singular? **Answer:** \(\det J=-2(x+y)\), so along \(x+y=0\).
3. **Critical point versus minimum.** For \(f=x^2-y^2\), compute the Newton update from \((a,b)\). **Answer:** \((-a,-b)\), reaching the saddle \((0,0)\), not a minimum.
4. **Descent.** Show \(g^Tp<0\) for \(Hp=-g\) when \(H\) is SPD and \(g\ne0\). **Answer:** \(g^Tp=-p^THp<0\) since \(p\ne0\).
5. **Merit caveat.** Give a scalar \(F\) for which \(\tfrac12 F(x)^2\) has a stationary point with nonzero residual. **Answer:** \(F(x)=x^2+1\) at \(x=0\), where \(F=1\) but \(F'=0\).

### Sources and reading

- [Boyd and Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), Chapter 9 on Newton directions, damping, and line search.
- [MIT 6.854 optimization notes on Newton's method](https://courses.csail.mit.edu/6.854/18/Notes/n19-newton_method.html), quadratic local models.
- [Wikipedia: Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method), root finding and basins.
- [Wikipedia: Newton's method in optimization](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization), distinct optimization formulation.

For the linear solves, see `linear-algebra:020000`, `linear-algebra:021000`, and `linear-algebra:024000`. `numerical-analysis:005000` supplies the scalar root-finding and bracketing perspective; the present lecture develops the multivariable construction.
