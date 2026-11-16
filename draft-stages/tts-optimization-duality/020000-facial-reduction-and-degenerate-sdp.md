# 020000 — Facial Reduction: Finding the True Interior of a Semidefinite Program

**Track:** Optimization and Duality. **Background:** positive semidefinite matrices, conic duality, Slater conditions, and convex geometry. **Central question:** how can a feasible semidefinite program have no strictly feasible matrix, and what should an algorithm do about it?

<!-- BEGIN SPOKEN LECTURE -->

# Feasible but nowhere inside

Imagine optimizing over symmetric positive semidefinite matrices. The feasible matrices are all nonnegative in the quadratic-form sense. Interior-point methods work especially well when there is at least one feasible matrix that is positive definite, comfortably inside the cone.

But consider a constraint that forces the first diagonal entry of the matrix to be zero. For a positive semidefinite matrix, that condition forces the entire first row and first column to vanish. Every feasible matrix is singular. There may be plenty of feasible matrices, and the optimization problem may have a perfectly finite answer, but the feasible set never enters the interior of the full positive-semidefinite cone.

This is not infeasibility. It is failure of strict feasibility. The distinction matters because strong-duality theorems and interior-point algorithms often invoke a condition called Slater's condition, which asks for a feasible point in the relative interior of the relevant cone, or its interior in a standard conic representation. If the formulation hides the smaller space where all feasible solutions lie, the familiar guarantees may not apply.

Facial reduction finds that smaller space explicitly. Instead of insisting on an interior point in the wrong cone, it changes the representation to the smallest face that contains the feasible set.

# A two-by-two matrix makes the geometry visible

Write a symmetric two-by-two matrix with diagonal entries a and c and off-diagonal entry b. Positive semidefiniteness requires a and c to be nonnegative, and it requires the determinant a times c minus b squared to be nonnegative.

Now constrain a to equal zero. The determinant condition becomes negative b squared greater than or equal to zero. That forces b to be zero. The matrix must be diagonal with first entry zero and second entry c nonnegative.

If we add the constraint that its trace equals one, the only feasible matrix is the diagonal matrix with entries zero and one. It is certainly positive semidefinite, and all constraints are satisfied. Yet it is not positive definite, because a nonzero vector in the first coordinate direction has quadratic form zero.

The correct feasible cone is a one-dimensional face consisting of matrices whose only potentially nonzero entry is the lower-right entry. Within that face, the feasible point with c equal to one is strictly positive in its reduced coordinate. The apparent lack of interior was caused by embedding a one-dimensional problem into a larger cone.

# A positive semidefinite witness exposes the face

The face can be found with a simple certificate. Take the matrix with one in the upper-left entry and zero everywhere else. Its inner product with any feasible matrix is exactly the first diagonal entry, which is forced to zero.

Both this witness matrix and every feasible matrix are positive semidefinite. The trace of their product is zero. For positive semidefinite matrices this is particularly strong: they must have orthogonal support in a suitable sense. The feasible matrix has no component in the direction exposed by the witness.

The witness is called an exposing vector. It gives a linear equation that every feasible matrix satisfies and identifies a proper face of the cone. We can then parameterize matrices in that face using a smaller positive semidefinite matrix, thereby removing the direction that can never be active.

In our example, choose a one-column matrix whose entry is zero in the first row and one in the second. Every feasible matrix can be written as that column times a nonnegative scalar times its transpose. The reduced semidefinite constraint is simply that this scalar is nonnegative.

# The general conic picture

For a conic feasibility problem, write the constraints as a linear map applied to x equals b, with x lying in a closed convex cone. The dual cone contains linear functionals that are nonnegative on all cone elements.

If a nonzero dual-cone element comes from a linear combination of the equality constraints and has zero pairing with b, then every feasible x has zero pairing with that element. This exposes a face containing the entire feasible set. Replace the original cone by that face and repeat.

The process can require several rounds. After reducing once, the new cone lives in a smaller linear space, and a further exposing direction may become visible only within that space. The smallest face containing the feasible set is called its minimal face. The number of exposing steps required by a particular definition of the algorithm relates to the singularity degree.

If the feasibility set is nonempty and the facial-reduction process reaches its minimal face, the reduced formulation has a feasible point in the relative interior of that face. That is the strict-feasibility condition appropriate for the reduced problem.

# Why the original duality theorem can fail

Slater's condition is a sufficient condition for strong duality and dual attainment in familiar convex programs. Its absence does not prove there is a duality gap. Our two-by-two example is perfectly well behaved after reduction, and may even have zero gap in its original formulation.

But semidefinite programs without strict feasibility can show pathological behavior: nonattainment of a dual optimum, positive duality gaps in some formulations, or severe sensitivity to small perturbations. An algorithm that assumes strict feasibility may return unstable multipliers or struggle to approach the feasible boundary.

Facial reduction is a preprocessing and reformulation tool, not a universal proof that every degenerate optimization problem becomes numerically easy. Finding exposing vectors can itself be delicate, especially in floating-point arithmetic. Exact rational or interval certificates can help verify a claimed exposing equation.

# A square-root sensitivity at the boundary

Return to the two-by-two matrix and relax the upper-left diagonal constraint slightly. Instead of a equal to zero, set it equal to a small positive delta, while keeping trace one. The second diagonal becomes one minus delta.

Positive semidefiniteness allows the off-diagonal entry b to range between minus the square root of delta times one minus delta and the corresponding positive square root. As delta tends to zero, this allowed interval shrinks like the square root of delta, not linearly in delta.

A tiny perturbation in the equality constraint can therefore produce a much larger proportional change in an off-diagonal feasible coordinate. The exact boundary problem was hiding a sharp geometric corner. A solver might interpret this sensitivity as numerical instability, while the mathematics shows that the sensitivity is real.

If we work in the minimal face at delta equal to zero, the off-diagonal coordinate is removed entirely, producing a clean reduced problem. But that reduced model describes the exact original constraint; it must not be reused unchanged when the constraint is genuinely perturbed.

# How facial reduction interacts with certificates

The exposing vector is itself a certificate that all feasible matrices lie in a smaller face. When its entries are exact or rigorously bounded, an independent checker can validate the reduction: confirm the witness is positive semidefinite, confirm it is a linear combination of equality-constraint matrices, and confirm its inner product with the right-hand side vanishes.

In the reduced coordinates, standard conic duality may again supply primal and dual optimality certificates. A trustworthy workflow records both stages—the certificate justifying dimension reduction and the certificate justifying the optimum in the reduced problem.

That separation is important because a solver can report an apparently excellent primal residual while failing to recognize the minimal face. Small residuals are not automatically exact equations, especially when the exposing direction is nearly singular or only approximately orthogonal to feasible matrices.

# Find the right cone before optimizing

Facial reduction changes how we think about degeneracy. The issue is not always that a semidefinite problem has too many constraints or that its feasible region is empty. The issue may be that the feasible region belongs to a lower-dimensional face of a much larger cone.

Our two-by-two example gives the full mechanism: a zero diagonal forces a zero row, an exposing positive matrix proves that fact, a reduced coordinate removes the impossible direction, and strict feasibility returns relative to the correct face. In larger semidefinite programs the geometry is more elaborate, but the objective is the same: discover the genuine domain of the optimization before asking an interior-point method to navigate it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `X=[[a,b],[b,c]] in S_+^2`. PSD is equivalent to `a>=0,c>=0,ac-b^2>=0`. If `a=0`, then `b=0`; adding `tr(X)=1` yields the unique feasible `X=diag(0,1)`. There is no `X positive definite` satisfying `X11=0`.

The exposing matrix `Z=e_1 e_1^T=diag(1,0)` satisfies `Z>=0` and `<Z,X>=X11=0` on every feasible X. Thus the minimal face is
\[
F=\{\operatorname{diag}(0,t):t\ge0\}=\{VYV^T:Y\in S_+^1\},\quad V=e_2.
\]
In reduced coordinate `Y=t`, the equality `tr X=1` gives `t=1>0`, which is strictly feasible relative to `S_+^1`.

More generally, for `A(x)=b, x in K` and `y` with `A^*y in K^* \setminus\{0\}` and `<y,b>=0`, each feasible x obeys `<A^*y,x>=0`, so feasibility lies in the proper exposed face `K cap (A^*y)^perp` when this is a proper face. The reduced cone can require further facial-reduction steps. Absence of Slater's condition does **not** logically imply a positive duality gap.

**Perturbation:** setting `X11=delta`, `tr X=1` yields `|X12|<=sqrt(delta(1-delta))` for `0<=delta<=1`, showing square-root boundary sensitivity. The reduced face for delta=0 is not equivalent to the perturbed problem with delta>0.

### Exercises with answers

1. Why does a PSD matrix with `X11=0` have `X12=0`? **Answer:** the determinant of its principal 2x2 block would otherwise be negative.
2. What exposes the face in this example? **Answer:** `Z=diag(1,0)` with `<Z,X>=0` on all feasible X.
3. Does Slater failure imply that primal and dual optimal values must differ? **Answer:** no; it removes a sufficient guarantee, not the possibility of equality.
4. What is the maximal absolute off-diagonal entry for `X11=1/100`, `tr X=1`? **Answer:** `sqrt((1/100)(99/100))=sqrt(99)/100`.

### Reading and source notes

- [Borwein and Wolkowicz, Facial Reduction for a Cone-Convex Programming Problem](https://doi.org/10.1017/S1446788700017250), foundational facial-reduction principle.
- [Facial reduction for symmetry-reduced semidefinite and doubly nonnegative programs](https://pmc.ncbi.nlm.nih.gov/articles/PMC10195748/), exposing vectors and minimal faces.
- [Pataki, Bad Semidefinite Programs: They All Look the Same](https://arxiv.org/abs/1112.1436), pathological duality and degeneracy in SDP.
