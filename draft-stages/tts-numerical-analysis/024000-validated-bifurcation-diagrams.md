# 024000 — Validated Bifurcation Diagrams and Computer-Assisted Proof

**Track:** Numerical Analysis. **Background:** Newton's method, interval arithmetic, the implicit-function theorem, and equilibria of parameterized differential equations. **Central question:** how can a numerical diagram be turned into a proof that branches and turning points actually exist?

<!-- BEGIN SPOKEN LECTURE -->

# A plot is persuasive, but it is not a proof

Imagine solving a nonlinear equation over a range of parameter values. A numerical package finds equilibria, draws a curve of solutions, and shows a turning point where two branches meet. The picture may look smooth and convincing. But a finite collection of approximate roots does not prove that the continuum of solutions connects as drawn.

A Newton solve can converge to an unintended branch. It can miss a narrow loop. Two nearby roots can merge, and numerical conditioning becomes poor just where the most interesting dynamics occurs. A step-size choice can create apparent gaps or crossings. Rounding can even move a computed root across a narrow threshold.

Validated numerical analysis asks for a stronger output. Instead of merely providing approximate points on a curve, produce enclosures that provably contain true solutions. Instead of estimating where a fold occurs, verify the defining equations and nondegeneracy conditions for a saddle-node bifurcation. This converts a numerical exploration into a finite chain of mathematical certificates.

# What makes a saddle-node a fold?

Start with an equilibrium equation F of x and a parameter mu equal to zero. At a regular solution, the derivative of F with respect to x is nonzero. The implicit-function theorem then says the solution can be described locally as a smooth function of mu.

At a turning point this derivative vanishes. The ordinary parameterization by mu fails. But the failure alone is not enough to prove a genuine saddle-node. We also need the parameter to unfold the degeneracy and the second derivative in x to be nonzero.

For a scalar equation, a nondegenerate fold has four essential conditions: F equals zero, its first x derivative equals zero, its second x derivative is nonzero, and its parameter derivative is nonzero. The first two locate the candidate. The last two distinguish a quadratic turning point from a higher-order degeneracy or a parameter that does not actually change the equation near the point.

A concrete model is x cubed minus x plus mu equal to zero. Its turning points are determined by three x squared minus one equal to zero. One fold has x equal to one over the square root of three, with mu equal to two over three square roots of three. The other fold is its negative counterpart.

Near the positive fold, two nearby equilibria occur for parameter values slightly below the fold value; for slightly higher values there are none in that neighborhood. The third real root of the cubic may still exist far away. The local fold statement must not be confused with the count of all roots of the equation.

# Isolate the candidate with intervals

We need not know the irrational fold coordinates as decimal approximations with many digits. A short rational interval suffices. For x, use the interval from 0.577 to 0.578. At the left endpoint, three x squared minus one is negative. At the right endpoint it is positive. The expression is strictly increasing throughout this positive interval.

Therefore exactly one value of x in the interval makes the derivative vanish. The corresponding mu is x minus x cubed. Simple interval bounds put it inside a small rational interval around 0.385. We have isolated the fold by exact inequalities rather than by a floating-point plot.

The same method works for simple polynomial examples, but large systems call for a more systematic framework. One creates an augmented system consisting of F equal to zero and the x derivative of F equal to zero. The fold is now an ordinary isolated zero of that augmented system, because its Jacobian is invertible under the nondegeneracy conditions.

# Interval Newton and the Krawczyk operator

Classical Newton iteration uses an approximate derivative to improve an approximate root. Interval Newton replaces a point derivative with an interval enclosure of all derivatives over a whole box. Its conclusion is a theorem about every possible root in that box.

The Krawczyk operator is a closely related tool. Start with a candidate center, an approximate inverse Jacobian, and an interval box. Compute a corrected center and add an interval bound for all possible linearization errors. If the resulting Krawczyk set lies strictly inside the original box, and the relevant nonsingularity or contraction conditions hold, we can establish existence and uniqueness of a true root in the box.

The distinction between existence and uniqueness matters. A small residual at the center alone does not prove either. An inward inclusion establishes an existence statement under the theorem's hypotheses; a suitable contraction bound can strengthen it to uniqueness. Neither result can be inferred simply from the number of Newton iterations that converged.

For the cubic fold, the augmented Jacobian has one row containing the x derivative and parameter derivative, and another containing the second x derivative and mixed derivative. At the fold it has nonzero determinant. That is why we can isolate the fold as an ordinary zero of a two-component system even though the original equation is singular with respect to x.

# From points to entire branches

Validating a handful of roots still does not prove the whole branch diagram. To cover a branch, we need intervals that enclose solution arcs, with verified overlaps and conditions excluding unobserved segments in the region of interest.

Away from folds, the implicit-function theorem gives smooth local parameterizations. Near a fold, pseudo-arclength continuation replaces the physical parameter by a coordinate along the solution curve. The augmented continuation equations remain nonsingular through a simple turning point.

A rigorous implementation can cover the curve by validated boxes or tube segments. Each local segment is connected to the next using verified continuation bounds. Additional global arguments may be needed to prove that no other disconnected branches exist in a chosen parameter region. A certificate of the branch we followed is not automatically a census of every solution everywhere.

This is especially important in high-dimensional discretized PDEs. A visualized branch may include unstable equilibria, folds, symmetry-breaking transitions, and reconnections. Verifying a specific branch segment and proving global completeness are distinct computational achievements.

# Floating-point direction matters

Interval arithmetic is only rigorous if its operations enclose the exact results. Ordinary rounded-to-nearest arithmetic may shrink an interval accidentally. Rigorous packages use outward rounding or exact rational arithmetic for critical steps. Bounds on transcendental functions, linear solves, and truncation errors must obey the same enclosure discipline.

One must also distinguish a verified zero of a finite discretization from a verified solution of the original continuous equation. For a PDE, a grid-based calculation might validate the discrete system while discretization error remains uncontrolled. To prove a continuous bifurcation, one needs estimates connecting the finite-dimensional approximation to the infinite-dimensional problem.

# What the final proof artifact should contain

A convincing computer-assisted bifurcation result records the equation, parameter domain, approximate centers, interval boxes, derivative enclosures, and the precise theorem applied. It identifies each validated root, branch segment, and fold, and states what has not been excluded.

In our cubic example, the hand calculation already certifies the folds. In a large reaction–diffusion system, the same logical structure can be implemented with interval matrices, validated continuation, and a priori bounds. The goal is not to replace mathematics with a plot. It is to make the computer produce the inequalities that a conventional proof would require.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Consider `F(x,mu)=x^3-x+mu`. Fold conditions are `F=0`, `F_x=3x^2-1=0`, `F_xx=6x!=0`, `F_mu=1!=0`. The positive fold is
\[
(x_*,\mu_*)=(1/\sqrt3,\ 2/(3\sqrt3)).
\]
**Exact rational isolation:** `F_x(577/1000)<0` and `F_x(578/1000)>0`, and `F_xx>0` on this interval. Thus it contains exactly one zero of F_x; setting `mu=x-x^3` isolates the fold parameter. The rough rational box `x in [577/1000,578/1000]`, `mu in [383/1000,387/1000]` contains the positive fold. For `mu<mu_*` sufficiently close to `mu_*`, two nearby roots exist; for `mu>mu_*` sufficiently close, none exists in this neighborhood.

For `G(x,mu)=(F,F_x)`, the Jacobian is
\[
 DG=\begin{pmatrix}3x^2-1&1\\6x&0\end{pmatrix},\quad
\det DG\big|_{(x_*,\mu_*)}=-2\sqrt3\ne0.
\]
For general G, Krawczyk form `K(X)=x_0-CG(x_0)+(I-CDG(X))(X-x_0)` uses an interval extension `DG(X)` and approximate inverse C. Under standard Krawczyk hypotheses, strict inward inclusion plus an appropriate contraction/nonsingularity bound certifies a unique zero. For a continuous PDE, separately bound the discretization remainder.

### Exercises with answers

1. Find the negative fold. **Answer:** `x=-1/sqrt3`, `mu=-2/(3sqrt3)`.
2. Why is solving `F=0,F_x=0` preferable to Newton on F alone at a fold? **Answer:** the augmented Jacobian is nonsingular at a nondegenerate fold while F_x vanishes there.
3. Does a validated branch segment prove no other solution branches exist in the domain? **Answer:** no; that requires global exclusion or covering arguments.
4. What makes interval arithmetic mathematically rigorous? **Answer:** outward enclosures for every operation and controlled approximation/truncation error.

### Reading and source notes

- [Sander and Wanner, Validated Saddle-Node Bifurcations and Applications to Lattice Dynamical Systems](https://epubs.siam.org/doi/10.1137/16M1061011), rigorous branch validation and fold tests.
- [J.-P. Lessard, Research on computer-assisted proofs](https://www.math.mcgill.ca/jplessard/research.html), validated nonlinear dynamics and bifurcation results.
- [SageMath documentation, Real Interval Fields](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/real_mpfi.html), outward-rounded interval computations.
