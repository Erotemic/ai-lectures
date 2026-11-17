# Constrained Newton Methods: Building and Solving the KKT System

**Track:** Multivariable Calculus from First Principles. **Focus:** linearize constrained stationarity, compute the saddle-point Newton correction, and connect reduced Hessians, Schur complements, and nonlinear feasibility.

<!-- BEGIN SPOKEN LECTURE -->

# Constrained Newton Methods: Building and Solving the KKT System

Unconstrained Newton's method replaces a nonlinear function by a local quadratic model and chooses the step that minimizes that model, provided the curvature permits it. But suppose the variables must satisfy a budget equation, or a physical conservation law. A Newton step can lower the model objective and still leave the allowed set. We cannot repair the difficulty merely by taking a smaller step: a generic direction outside the tangent space violates an affine equality for every nonzero step length.

We need to compute a correction that respects the constraints at least to first order, and that recognizes how the constraints bend the feasible space. The natural result is not a single ordinary Hessian solve. It is a larger system with zeros on a diagonal block, linking decision variables to Lagrange multipliers. Such systems are called KKT systems, or saddle-point systems.

These are the linear algebra problems behind equality-constrained Newton methods, sequential quadratic programming, and many models in mechanics and scientific computing. We will derive the blocks, solve a small example completely, and then ask when the system is invertible and what its solution actually guarantees.

## Start from two kinds of residual

Let f be a smooth objective and c the vector of equality constraints. Define the Lagrangian by adding lambda times the constraints to f. At a regular constrained local optimum, the constraints vanish and the gradient of the Lagrangian with respect to the decision variables vanishes. These are two different equations: primal feasibility and Lagrangian stationarity.

At a current guess for x and lambda, we usually have neither equation exactly. Call the stationarity error the dual residual. It is the objective gradient plus the transpose of the constraint Jacobian times lambda. Call the feasibility error the primal residual. It is simply c of x.

Now use Newton's method on this combined system of equations. We must differentiate both residuals with respect to both sets of unknowns. Differentiating stationarity with respect to x gives the Hessian of the Lagrangian, not in general the Hessian of f. Differentiating it with respect to lambda gives the transpose of the constraint Jacobian. Differentiating feasibility with respect to x gives the constraint Jacobian. Feasibility has no dependence on lambda, so its derivative with respect to lambda is zero.

Assemble these four blocks into a square matrix. The upper left is the Lagrangian Hessian. The upper right is J transpose. The lower left is J. The lower right is zero. Multiplying this matrix by the corrections to x and lambda gives the negative of the two residuals.

Why must the lower right block be zero? Because multipliers are not extra physical degrees of freedom whose values directly alter the constraint equation. They enforce the constraint through stationarity. That zero block makes the matrix generally indefinite even when the objective Hessian is positive definite. It also explains why blindly applying an algorithm designed for positive-definite linear systems to the entire KKT matrix is a mistake.

## Solve an equality-constrained quadratic exactly

Consider two variables x and y. Minimize one half of the square of x minus two, plus two times y squared. Constrain x plus y to equal one. The objective's Hessian is diagonal: one in the x direction and four in the y direction. The constraint Jacobian is the row one, one.

Begin from the feasible point x equals one, y equals zero, with a trial multiplier of zero. The objective gradient there is negative one, zero. Thus the dual residual is negative one, zero, and the primal residual is zero. Our Newton correction must solve three equations.

The first equation says the x correction plus the multiplier correction equals one. The second says four times the y correction plus the multiplier correction equals zero. The third says the x correction plus the y correction equals zero, because we started feasible and want to remain on the budget line.

The third equation gives the y correction as the negative of the x correction. The second then says the multiplier correction is four times the x correction. Substitute into the first and obtain five times the x correction equals one. Therefore the x correction is one fifth, the y correction is minus one fifth, and the multiplier correction is four fifths.

After one full Newton step we reach x equal to six fifths and y equal to negative one fifth, with multiplier four fifths. This is the exact constrained minimizer. You can check it directly: the gradient components are minus four fifths and minus four fifths, which are canceled by the multiplier times the constraint normal. The two variables still sum to one.

The one-step result is not a universal convergence rate for constrained Newton. It happens because the objective is quadratic and the constraint affine. The KKT equations are then linear, so Newton solves them in one step if the KKT matrix is nonsingular. A nonlinear model generally requires repeated recomputation of its residuals, Jacobian, and Hessian.

## Feasible directions and the reduced system

There is another way to understand this step. Since our starting point already satisfies x plus y equals one, any acceptable correction must have its coordinates sum to zero. Every such correction is a multiple of the vector one, negative one. We can eliminate the constraint by working with that single free coordinate.

Restrict the quadratic model to this tangent direction. The curvature along the vector one, negative one is one plus four, giving five. The objective's directional derivative at the starting point is negative one. Minimizing the resulting one-variable quadratic gives a step length of one fifth. We have recovered exactly the KKT correction without ever solving for the multiplier first.

In higher dimensions, collect a basis of the null space of J into a matrix Z. At a feasible start the primal correction can be expressed as Z times a vector q. The reduced Newton equation contains the smaller Hessian Z transpose H Z and the reduced gradient Z transpose times the stationarity residual. Since Z transpose J transpose is zero, the current multiplier makes no contribution to the reduced gradient.

This way of solving emphasizes curvature on the feasible tangent space. If the reduced Hessian is positive definite, the reduced quadratic has a unique minimizer. The full Hessian H need not be positive definite in directions that constraints forbid. Conversely, if the reduced Hessian has a negative direction, solving the stationarity equations alone may produce a correction aimed toward a saddle or maximum rather than a minimum.

## When is the saddle matrix invertible?

Here is a useful exact criterion. Suppose the constraint Jacobian has full row rank and H is symmetric and positive definite on the nonzero vectors in the kernel of J. Then the KKT matrix is invertible.

The proof is short and revealing. Assume the KKT matrix sends some pair of vectors, call them u and v, to zero. The lower equation gives J times u equals zero, so u is tangent. The upper equation is H times u plus J transpose times v equals zero. Take its dot product with u. Since J u is zero, the multiplier term vanishes, leaving u transpose H u equal to zero. Positive tangent curvature forces u to be zero. The upper equation then reduces to J transpose times v equals zero. Full row rank of J forces v to be zero. The kernel is trivial, so the square KKT matrix is invertible.

This argument shows why constrained curvature, rather than ambient positive definiteness, is the relevant sufficient condition. As an example, let H have diagonal entries negative one and positive two, and let the constraint fix the first coordinate. H is indefinite in the full plane, but along the allowed vertical direction its quadratic form is positive. The associated KKT matrix is nevertheless invertible, and the reduced quadratic is well behaved.

If H is invertible and suitable for stable elimination, another computational method is to eliminate the primal correction. Solve formally for it in terms of the multiplier correction, then substitute into the linearized constraint equation. The result is a smaller system in multipliers involving J times H inverse times J transpose, called a Schur complement. When H is positive definite and J has full row rank, that matrix is positive definite, though its numerical conditioning still needs attention.

The formula is valuable for understanding algorithms, not an instruction to form H inverse explicitly. Solving linear systems with H is preferable. For large sparse KKT systems, sparse symmetric-indefinite factorizations, null-space methods, and suitable iterative methods can exploit the block structure. A direct normal-equations construction can worsen conditioning. A regularized or approximate Hessian can make a step more stable, but it changes the model, and that choice must be explicit.

## Nonlinear constraints introduce an extra difficulty

For a nonlinear constraint, the equation c of x plus J times the correction equals zero only enforces feasibility to first order. If the correction is large, the updated point can violate the original constraint. Furthermore, as the current x or lambda changes, the Lagrangian Hessian changes, including the multiplier-weighted second derivatives of the constraints.

Our circle example makes this concrete. Minimize the horizontal coordinate on a unit circle. At the leftmost stationary point, the objective Hessian is zero but the Lagrangian Hessian is the identity. If we replace the Lagrangian Hessian by the objective Hessian, we discard the only curvature that makes the constrained minimum detectable. The Newton model ceases to represent the second variation of the true problem.

There are several strategies for controlling nonlinear feasibility. A line search can judge progress using a merit function that penalizes constraint violations; a filter method can compare objective decrease against feasibility improvement without folding everything into a single scalar; a trust-region method can limit how far the local quadratic and linearized constraints are trusted. Some methods explicitly project or retract a trial step back to a constraint manifold. None is a free guarantee of global convergence. The assumptions of the method, the constraint regularity, and the accuracy of the linear solve remain important.

For nonlinear inequality constraints, a sequential quadratic programming method incorporates linearized active inequalities, not just equalities. It solves a constrained quadratic subproblem, updates a Hessian model and a working set or related dual variables, and decides whether to accept the step. Incorrect active-set guesses may require a different subproblem. The critical cone and complementarity distinctions from the inequality lecture explain why the behavior is more subtle near a switching boundary.

## Why the block solve is reusable

The same block matrix appears in two different tasks. During optimization, we multiply it by an unknown correction to reduce KKT residuals. After optimization, when we want to know how the solution changes as a measured parameter changes, we multiply it by an unknown derivative instead. The right-hand side changes, but the geometry and the main matrix are the same.

That observation is more than a mathematical coincidence. It means the factorization used for constrained Newton can sometimes be reused to compute sensitivities or adjoint gradients, which is especially valuable when optimization is embedded inside another algorithm. It also means that a nearly singular KKT matrix warns about both unreliable numerical steps and potentially large changes in the optimizer under small perturbations.

The point of constrained Newton is therefore not merely to solve a bigger linear system. It is to solve the right linear system: one that carries the feasible directions, the curvature of the constraints, and the multipliers in the same calculation. From here, implicit differentiation becomes a direct extension rather than an unrelated technique.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Linearization of the KKT residual

For equality constraints \(c(x)=0\), let

\[
L(x,\lambda)=f(x)+\lambda^\top c(x),\quad
r_d=\nabla_xL,\quad r_p=c(x),\quad J=Dc(x),\quad H=\nabla_{xx}^2L.
\]

Newton's equation for the root \((r_d,r_p)=0\) is

\[
\underbrace{\begin{bmatrix}H&J^\top\\J&0\end{bmatrix}}_{K}
\begin{bmatrix}\Delta x\\\Delta\lambda\end{bmatrix}
=-\begin{bmatrix}r_d\\r_p\end{bmatrix}.
\]

At \(r_p=0\), the Newton primal step is tangent: \(J\Delta x=0\). For an orthonormal kernel basis \(Z\), \(\Delta x=Zq\) and

\[
(Z^\top HZ)q=-Z^\top r_d=-Z^\top\nabla f.
\]

If \(J\) has full row rank and \(H\) is positive definite on \(\ker J\setminus\{0\}\), the KKT matrix is nonsingular. If \(H\) itself is invertible, eliminating \(\Delta x\) gives

\[
(JH^{-1}J^\top)\Delta\lambda=r_p-JH^{-1}r_d,\qquad
\Delta x=-H^{-1}(r_d+J^\top\Delta\lambda).
\]

Never form a dense inverse in an implementation simply because an inverse appears in this algebraic identity.

### Exact quadratic example

\[
f(x,y)=\tfrac12(x-2)^2+2y^2,\qquad c(x,y)=x+y-1,\quad H=\operatorname{diag}(1,4),\quad J=\begin{bmatrix}1&1\end{bmatrix}.
\]

At \((x,y,\lambda)=(1,0,0)\), \(r_d=(-1,0)^\top\), \(r_p=0\). Thus

\[
\begin{bmatrix}1&0&1\\0&4&1\\1&1&0\end{bmatrix}
\begin{bmatrix}\Delta x\\\Delta y\\\Delta\lambda\end{bmatrix}=
\begin{bmatrix}1\\0\\0\end{bmatrix}
\quad\Rightarrow\quad
\begin{bmatrix}\Delta x\\\Delta y\\\Delta\lambda\end{bmatrix}=
\begin{bmatrix}1/5\\-1/5\\4/5\end{bmatrix}.
\]

One step reaches \((x_*,y_*,\lambda_*)=(6/5,-1/5,4/5)\). The reduced tangent vector \(d=(1,-1)\) has \(d^\top Hd=5\).

### Exercises with answers

1. **Constraint offset:** starting from \(x+y=2\) instead of \(1\), with the same objective, what changes in the right-hand side? **Answer:** the primal residual \(r_p=x+y-2\); the lower Newton equation becomes \(\Delta x+\Delta y=-r_p\).
2. **Invertibility proof:** if \(J\) has full row rank but \(H\) is merely positive semidefinite on \(\ker J\), does the proof above establish invertibility? **Answer:** no. A nonzero tangent vector with zero quadratic form may create singularity; strict positivity was essential for that proof.
3. **Schur complement:** in the worked example, compute \(JH^{-1}J^\top\). **Answer:** \(1+1/4=5/4\), giving \(\Delta\lambda=(0-(-1))/(5/4)=4/5\).
4. **Curved equality:** at \((-1,0)\) for minimizing x on \(x^2+y^2=1\), what is \(H\)? **Answer:** \(H=\nabla^2f+\lambda\nabla^2c=0+(1/2)(2I)=I\). Using only \(\nabla^2f=0\) discards true tangent curvature.

### Sources and further reading

- S. Boyd and L. Vandenberghe, [*Convex Optimization*, Chapter 10, Equality Constrained Minimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), for feasible-start and infeasible-start equality-constrained Newton systems, null-space methods and Schur complements.
- [Stanford *Convex Optimization* lecture slides, Chapter 10](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf), for equations and descent safeguards.
- [Wikipedia: Sequential quadratic programming](https://en.wikipedia.org/wiki/Sequential_quadratic_programming), for the connection to nonlinear inequality-constrained subproblems.
- [Wikipedia: Schur complement](https://en.wikipedia.org/wiki/Schur_complement), for block elimination notation.

*Teaching connections:* `linear-algebra:020000` gives factorizations of linear systems; `multivariable-calculus:021000` explains the unconstrained Newton step; `multivariable-calculus:027000` derives the Lagrangian Hessian; `multivariable-calculus:028000` discusses active inequality constraints.
