# Infeasibility embeddings, faces, and exact arithmetic

<!-- BEGIN SPOKEN LECTURE -->

# Infeasibility embeddings, faces, and exact arithmetic

## Homogeneous Self-Dual Embeddings and Infeasibility Certificates

A numerical optimizer may return a vector that looks promising. It may also report that a problem is infeasible, unbounded, or numerically difficult. These statements are not interchangeable. An infeasibility claim should be supported by evidence, just as an optimality claim should be supported by a duality gap and feasibility residuals.

Homogeneous self-dual embedding provides one way to organize these alternatives. Rather than solving the primal and dual optimization problems completely separately, we enlarge the variables and build a homogeneous feasibility problem. A nonzero solution of that larger system can encode an optimal primal-dual pair, or in other cases, a certificate of infeasibility.

The key is to remember what a certificate means. It is a mathematical object whose defining equations can be checked independently. A solver's printed status is only as trustworthy as the residuals, tolerances, and assumptions that support that status.

### Begin with a cone program

Let x be an unrestricted vector of decision variables. The objective is a linear function of x. The constraints can be written by introducing a slack vector s that belongs to a closed convex cone. A linear map of x plus s must equal a specified right-hand side.

The dual problem uses a vector y in the dual cone. Its linear equality connects the transpose of the constraint map to the objective coefficients. Weak duality says that the dual objective cannot exceed the primal objective whenever both points are feasible.

A zero duality gap between feasible primal and dual points certifies optimality. But if the primal constraints cannot be met at all, we need a different kind of witness. A separating vector in the dual cone can make the right-hand side have a sign that every feasible slack would contradict. This is a conic version of Farkas' lemma.

### Add two nonnegative scalars

The embedding introduces two nonnegative scalar variables, commonly called tau and kappa. It makes the primal constraints, dual constraints, and zero-gap equation homogeneous. Setting all variables to zero always satisfies the resulting equations, so the meaningful question is whether we obtain an appropriately normalized nonzero solution.

If tau is positive, divide the original variables by tau. The normalized vectors satisfy the primal and dual constraints. Algebraic identities inside the embedding imply that kappa must be zero and the primal-dual gap vanishes. Under these exact conditions, the normalized vectors are an optimal pair.

If kappa is positive, tau must be zero. The remaining equations instead encode a direction of infeasibility. One can inspect whether the certificate contradicts primal feasibility or dual feasibility. This provides a structured alternative to having a solver simply run out of iterations.

It is important not to assume that every nonzero embedded solution falls neatly into one of those two cases. The degenerate case with both tau and kappa zero can occur, and conic pathologies may require further analysis. An approximate numerical iterate also needs thresholds and independent residual checks.

### A primal infeasibility example

Consider a one-dimensional decision variable constrained to be at least one and at most zero. There is no feasible value: the interval is empty. In conic form these are two linear inequalities with two nonnegative slack variables.

Assign the same positive multiplier to each inequality. When we add their linear left-hand sides, the decision variable cancels. What remains would require a nonnegative quantity to equal a negative number. That contradiction is a certificate of infeasibility. It does not depend on trying many candidate values of x.

In the homogeneous embedding, the dual multiplier and the nonnegative kappa variable can encode precisely this contradiction. The algebraic equations verify it, and the sign condition is impossible for any primal-feasible x and slack.

The example is deliberately simple. In large cone programs, certificates can involve thousands of variables, semidefinite matrices, second-order cones, or exponential cones. The same separation principle continues to apply, but accuracy of the computed certificate becomes a serious numerical question.

### One skew-symmetric linear system

A standard embedding can be expressed using a skew-symmetric block matrix. It combines the constraint matrix, objective coefficients, and right-hand side. A vector containing x, y, and tau is mapped to a vector containing a zero block, the primal slack s, and kappa.

Skew symmetry matters because the quadratic form obtained by taking the inner product of a vector with its image is zero. Along with cone duality, this forces complementarity conditions. The structure makes the embedding compatible with operator-splitting methods and projection algorithms.

A popular implementation, SCS, applies operator splitting to this homogeneous feasibility system. Such first-order methods can address very large cone programs, though modest-accuracy solutions and rigorous high-precision certificates are different goals. Interior-point embeddings use related ideas with different numerical behavior.

### Diagnosing what the solver actually found

Suppose a numerical result has positive tau but a visibly nonzero normalized primal residual. It is not yet a certified optimum. Suppose it reports positive kappa but the proposed separating vector has the wrong sign, or lies outside the dual cone beyond tolerance. It is not a valid infeasibility witness.

This is particularly important in ill-conditioned problems or those lacking strict feasibility. Facial reduction may be required to expose the correct lower-dimensional face before standard duality arguments become reliable.

The mathematical benefit of homogeneous self-dual embedding is a shared framework for success and failure. It makes optimality and infeasibility part of the same geometry, while leaving us with concrete equations that can be checked rather than status labels that must be trusted.

## Facial Reduction: Finding the True Interior of a Semidefinite Program

Imagine optimizing over symmetric positive semidefinite matrices. The feasible matrices are all nonnegative in the quadratic-form sense. Interior-point methods work especially well when there is at least one feasible matrix that is positive definite, comfortably inside the cone.

But consider a constraint that forces the first diagonal entry of the matrix to be zero. For a positive semidefinite matrix, that condition forces the entire first row and first column to vanish. Every feasible matrix is singular. There may be plenty of feasible matrices, and the optimization problem may have a perfectly finite answer, but the feasible set never enters the interior of the full positive-semidefinite cone.

This is not infeasibility. It is failure of strict feasibility. The distinction matters because strong-duality theorems and interior-point algorithms often invoke a condition called Slater's condition, which asks for a feasible point in the relative interior of the relevant cone, or its interior in a standard conic representation. If the formulation hides the smaller space where all feasible solutions lie, the familiar guarantees may not apply.

Facial reduction finds that smaller space explicitly. Instead of insisting on an interior point in the wrong cone, it changes the representation to the smallest face that contains the feasible set.

## A two-by-two matrix makes the geometry visible

Write a symmetric two-by-two matrix with diagonal entries a and c and off-diagonal entry b. Positive semidefiniteness requires a and c to be nonnegative, and it requires the determinant a times c minus b squared to be nonnegative.

Now constrain a to equal zero. The determinant condition becomes negative b squared greater than or equal to zero. That forces b to be zero. The matrix must be diagonal with first entry zero and second entry c nonnegative.

If we add the constraint that its trace equals one, the only feasible matrix is the diagonal matrix with entries zero and one. It is certainly positive semidefinite, and all constraints are satisfied. Yet it is not positive definite, because a nonzero vector in the first coordinate direction has quadratic form zero.

The correct feasible cone is a one-dimensional face consisting of matrices whose only potentially nonzero entry is the lower-right entry. Within that face, the feasible point with c equal to one is strictly positive in its reduced coordinate. The apparent lack of interior was caused by embedding a one-dimensional problem into a larger cone.

## A positive semidefinite witness exposes the face

The face can be found with a simple certificate. Take the matrix with one in the upper-left entry and zero everywhere else. Its inner product with any feasible matrix is exactly the first diagonal entry, which is forced to zero.

Both this witness matrix and every feasible matrix are positive semidefinite. The trace of their product is zero. For positive semidefinite matrices this is particularly strong: they must have orthogonal support in a suitable sense. The feasible matrix has no component in the direction exposed by the witness.

The witness is called an exposing vector. It gives a linear equation that every feasible matrix satisfies and identifies a proper face of the cone. We can then parameterize matrices in that face using a smaller positive semidefinite matrix, thereby removing the direction that can never be active.

In our example, choose a one-column matrix whose entry is zero in the first row and one in the second. Every feasible matrix can be written as that column times a nonnegative scalar times its transpose. The reduced semidefinite constraint is simply that this scalar is nonnegative.

## The general conic picture

For a conic feasibility problem, write the constraints as a linear map applied to x equals b, with x lying in a closed convex cone. The dual cone contains linear functionals that are nonnegative on all cone elements.

If a nonzero dual-cone element comes from a linear combination of the equality constraints and has zero pairing with b, then every feasible x has zero pairing with that element. This exposes a face containing the entire feasible set. Replace the original cone by that face and repeat.

The process can require several rounds. After reducing once, the new cone lives in a smaller linear space, and a further exposing direction may become visible only within that space. The smallest face containing the feasible set is called its minimal face. The number of exposing steps required by a particular definition of the algorithm relates to the singularity degree.

If the feasibility set is nonempty and the facial-reduction process reaches its minimal face, the reduced formulation has a feasible point in the relative interior of that face. That is the strict-feasibility condition appropriate for the reduced problem.

## Why the original duality theorem can fail

Slater's condition is a sufficient condition for strong duality and dual attainment in familiar convex programs. Its absence does not prove there is a duality gap. Our two-by-two example is perfectly well behaved after reduction, and may even have zero gap in its original formulation.

But semidefinite programs without strict feasibility can show pathological behavior: nonattainment of a dual optimum, positive duality gaps in some formulations, or severe sensitivity to small perturbations. An algorithm that assumes strict feasibility may return unstable multipliers or struggle to approach the feasible boundary.

Facial reduction is a preprocessing and reformulation tool, not a universal proof that every degenerate optimization problem becomes numerically easy. Finding exposing vectors can itself be delicate, especially in floating-point arithmetic. Exact rational or interval certificates can help verify a claimed exposing equation.

## A square-root sensitivity at the boundary

Return to the two-by-two matrix and relax the upper-left diagonal constraint slightly. Instead of a equal to zero, set it equal to a small positive delta, while keeping trace one. The second diagonal becomes one minus delta.

Positive semidefiniteness allows the off-diagonal entry b to range between minus the square root of delta times one minus delta and the corresponding positive square root. As delta tends to zero, this allowed interval shrinks like the square root of delta, not linearly in delta.

A tiny perturbation in the equality constraint can therefore produce a much larger proportional change in an off-diagonal feasible coordinate. The exact boundary problem was hiding a sharp geometric corner. A solver might interpret this sensitivity as numerical instability, while the mathematics shows that the sensitivity is real.

If we work in the minimal face at delta equal to zero, the off-diagonal coordinate is removed entirely, producing a clean reduced problem. But that reduced model describes the exact original constraint; it must not be reused unchanged when the constraint is genuinely perturbed.

## How facial reduction interacts with certificates

The exposing vector is itself a certificate that all feasible matrices lie in a smaller face. When its entries are exact or rigorously bounded, an independent checker can validate the reduction: confirm the witness is positive semidefinite, confirm it is a linear combination of equality-constraint matrices, and confirm its inner product with the right-hand side vanishes.

In the reduced coordinates, standard conic duality may again supply primal and dual optimality certificates. A trustworthy workflow records both stages—the certificate justifying dimension reduction and the certificate justifying the optimum in the reduced problem.

That separation is important because a solver can report an apparently excellent primal residual while failing to recognize the minimal face. Small residuals are not automatically exact equations, especially when the exposing direction is nearly singular or only approximately orthogonal to feasible matrices.

## Find the right cone before optimizing

Facial reduction changes how we think about degeneracy. The issue is not always that a semidefinite problem has too many constraints or that its feasible region is empty. The issue may be that the feasible region belongs to a lower-dimensional face of a much larger cone.

Our two-by-two example gives the full mechanism: a zero diagonal forces a zero row, an exposing positive matrix proves that fact, a reduced coordinate removes the impossible direction, and strict feasibility returns relative to the correct face. In larger semidefinite programs the geometry is more elaborate, but the objective is the same: discover the genuine domain of the optimization before asking an interior-point method to navigate it.

## Exact Semidefinite Certificates and Weak Infeasibility

A semidefinite program optimizes a linear objective over symmetric positive semidefinite matrices subject to linear equations. Numerical solvers are highly effective at finding approximate answers, but the distinction between an approximation and a proof becomes important near the boundary of the positive semidefinite cone.

A matrix can be positive semidefinite with an eigenvalue exactly zero. A floating-point approximation may report a slightly negative eigenvalue even when the exact matrix is feasible. The reverse error is more dangerous for certification: a matrix whose true smallest eigenvalue is negative can appear nonnegative at the available precision.

Exact certification does not require solving every semidefinite problem symbolically from the beginning. It asks us to turn a proposed solution or dual certificate into an identity that can be checked in an arithmetic domain where the crucial signs are rigorous.

## An exact optimality certificate

Consider a two-by-two symmetric positive semidefinite matrix whose diagonal entries are both one. We want to maximize the off-diagonal entry.

Positive semidefiniteness requires the determinant to be nonnegative. With diagonal entries one, the off-diagonal entry must lie between negative one and positive one. The matrix with every entry one is positive semidefinite and reaches the upper bound. Therefore the optimal value is exactly one.

This can also be certified by duality. In the dual problem, assign the weight one half to each diagonal equality. The resulting dual slack is a positive semidefinite matrix with entries one half on the diagonal and negative one half off-diagonal. Its dual objective is one.

Weak duality says no primal feasible matrix can exceed a dual feasible value. A primal matrix attaining one and a dual matrix bounding the value by one prove optimality without relying on a solver tolerance. All the entries in this example are rational numbers, and their matrix signs can be checked exactly.

## A feasible set that almost exists

Now consider a different problem. Require a two-by-two matrix to be positive semidefinite, with its upper-left diagonal entry equal to zero and its off-diagonal entry equal to one. Is there a solution?

No. For a positive semidefinite matrix, if a diagonal entry is zero, every entry in the corresponding row and column must be zero. Otherwise the determinant of a two-by-two principal submatrix would be negative. So an off-diagonal entry equal to one is impossible.

That proof is elementary and exact. But something surprising happens numerically.

Consider the affine matrices with upper-left entry zero, off-diagonal entries one, and lower-right entry t, where t is very large and positive. These are all infeasible because their determinant is negative one. Yet they are arbitrarily close to positive semidefinite matrices: simply change the upper-left entry from zero to one over t. The modified matrix has determinant zero and is positive semidefinite. The change tends to zero as t grows.

Thus the affine constraint space and the positive semidefinite cone do not intersect, but their distance is zero. This is called weak infeasibility.

A numerical solver may approach matrices with larger and larger entries and smaller and smaller constraint violations. It may struggle to distinguish weak infeasibility from a feasible problem with severe scaling. The difficulty is geometric, not simply a poorly chosen tolerance.

## Why a familiar Farkas certificate can fail

For linear programming, infeasibility is usually captured by a finite dual separating certificate. For semidefinite programming, the image of the positive semidefinite cone under a linear map need not be closed. A missing point can lie in the closure of the image.

That failure of closedness is exactly what happens in weak infeasibility. There may be no strictly separating dual hyperplane in the original formulation. A standard numerical dual residual might therefore fail to provide an exact certificate even though the primal problem is genuinely infeasible.

Facial reduction and elementary reformulations can expose the right smaller face or contradiction. In our example, the zero diagonal constraint forces the feasible matrix—if one existed—to lie in a face where its entire first row vanishes. Inside that face, the requirement that the first off-diagonal entry equals one is transparently contradictory.

The sequence of deductions is short enough to verify by hand. More complicated semidefinite problems can need several exposing steps, and symbolic certification may involve rational or algebraic reconstruction followed by exact matrix checks.

## From approximate answer to proof artifact

A practical certification workflow begins with numerical computation. Solve the primal and dual approximately, inspect residuals and the likely ranks, and attempt to reconstruct simple exact values. Then verify the equalities, inequalities, and complementary slackness in exact arithmetic or with certified interval bounds.

A rational positive semidefinite matrix can be checked through exact principal minors or a suitable exact factorization. A certificate for optimality requires both a feasible primal candidate and a feasible dual candidate with matching objective values, or a separately justified rigorous bound. A certificate for infeasibility may require facial reduction instead of a single unqualified Farkas vector.

The goal is not to distrust numerical solvers. It is to use them for what they do well—finding promising structure—then use exact reasoning to establish what a theorem requires.

## The cone has a boundary worth respecting

Linear programs and semidefinite programs are both convex, but their geometries differ. The positive semidefinite cone is curved, it has faces indexed by subspaces, and its linear images can fail to be closed.

The two-by-two optimality example shows how clean exact primal-dual witnesses can be. The weakly infeasible example shows why not every status report can be justified by the same kind of certificate. Reliable semidefinite optimization requires understanding both the arithmetic of a proposed witness and the geometry of the cone that the witness inhabits.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Homogeneous Self-Dual Embeddings and Infeasibility Certificates

**Track:** Optimization and Duality. **Background:** conic programming, weak duality, KKT conditions, primal and dual feasibility. **Central question:** can one mathematical system reveal an optimum or explain why an optimization problem has no feasible solution?

#### Mathematical companion (not spoken)

Take the conic primal and dual, using the sign convention
\[
(P)\quad\min_x c^Tx\quad\text{s.t. }Ax+s=b,\ s\in K,
\qquad
(D)\quad\max_y -b^Ty\quad\text{s.t. }A^Ty+c=0,\ y\in K^*.
\]
For any feasible x,s,y, `c^T x+b^T y=s^T y>=0` gives weak duality. An exact homogeneous embedding is
\[
Ax+s=b\tau,\qquad A^Ty+c\tau=0,\qquad c^Tx+b^Ty+\kappa=0,\quad
s\in K,\ y\in K^*,\ \tau,\kappa\ge0.
\]
Multiply the first equation by y and the second by x to derive `s^Ty=tau(c^Tx+b^Ty)=-tau kappa`; dual-cone nonnegativity implies `s^Ty=0` and `tau kappa=0`.

If `tau>0`, normalization by tau gives a primal-dual feasible zero-gap pair. If `kappa>0`, then `tau=0` and `c^Tx+b^Ty=-kappa<0`. If `b^Ty<0` with `A^Ty=0`, `y in K*`, any primal-feasible `Ax+s=b` implies `b^Ty=s^Ty>=0`, contradiction: a primal infeasibility certificate. If `c^Tx<0` with `Ax+s=0`, `s in K`, then any dual-feasible y would imply `c^Tx=y^Ts>=0`, contradiction: a dual infeasibility certificate. At least one of these two strict inequalities holds when `kappa>0`; both can hold in pathological instances. `tau=kappa=0` requires separate analysis and gives neither conclusion alone.

Let `u=(x,y,tau)`, `v=(0,s,kappa)` and
\[
Q=\begin{pmatrix}0&A^T&c\\-A&0&b\\-c^T&-b^T&0\end{pmatrix},
\qquad v=Qu,\quad Q^T=-Q.
\]
For an infeasible toy problem `x>=1, x<=0`, choose `A=(-1,1)^T`, `b=(-1,0)^T`, `K=R_+^2`, `c=0`. Then `y=(1,1)` gives `A^Ty=0`, `b^Ty=-1`: a primal infeasibility certificate. In an approximate solve, check primal/dual feasibility residuals, cone membership, scalar signs and scaled objective gap independently; use numerical tolerances rather than exact equalities.

##### Exercises with answers

1. For feasible primal and dual points, prove weak duality. **Answer:** `c^Tx+b^Ty=s^Ty>=0` because `s in K` and `y in K*`.
2. What does `tau>0` allow? **Answer:** normalization of the embedded x,s,y to a feasible primal-dual zero-gap pair.
3. Give a certificate that `x>=1` and `x<=0` cannot both hold. **Answer:** add the inequalities or use `y=(1,1)` in the specified cone representation to obtain `b^Ty=-1<0`.
4. Does `tau=kappa=0` certify optimality or infeasibility? **Answer:** no; it is a potentially degenerate case requiring further analysis.

##### Reading and source notes

- [O'Donoghue, Chu, Parikh and Boyd, Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding](https://www-leland.stanford.edu/~boyd/papers/scs.html), embedding and first-order algorithm.
- [Permenter, Friberg and Andersen, Self-Dual Embedding and Facial Reduction](https://optimization-online.org/2015/09/5104/), degeneracy and failure of strict feasibility.
- [SCS, Algorithm and Conic Solver Documentation](https://www.cvxgrp.org/scs/), practical residual and status conventions.

### Facial Reduction: Finding the True Interior of a Semidefinite Program

**Track:** Optimization and Duality. **Background:** positive semidefinite matrices, conic duality, Slater conditions, and convex geometry. **Central question:** how can a feasible semidefinite program have no strictly feasible matrix, and what should an algorithm do about it?

#### Mathematical companion (not spoken)

Let `X=[[a,b],[b,c]] in S_+^2`. PSD is equivalent to `a>=0,c>=0,ac-b^2>=0`. If `a=0`, then `b=0`; adding `tr(X)=1` yields the unique feasible `X=diag(0,1)`. There is no `X positive definite` satisfying `X11=0`.

The exposing matrix `Z=e_1 e_1^T=diag(1,0)` satisfies `Z>=0` and `<Z,X>=X11=0` on every feasible X. Thus the minimal face is
\[
F=\{\operatorname{diag}(0,t):t\ge0\}=\{VYV^T:Y\in S_+^1\},\quad V=e_2.
\]
In reduced coordinate `Y=t`, the equality `tr X=1` gives `t=1>0`, which is strictly feasible relative to `S_+^1`.

More generally, for `A(x)=b, x in K` and `y` with `A^*y in K^* \setminus\{0\}` and `<y,b>=0`, each feasible x obeys `<A^*y,x>=0`, so feasibility lies in the proper exposed face `K cap (A^*y)^perp` when this is a proper face. The reduced cone can require further facial-reduction steps. Absence of Slater's condition does **not** logically imply a positive duality gap.

**Perturbation:** setting `X11=delta`, `tr X=1` yields `|X12|<=sqrt(delta(1-delta))` for `0<=delta<=1`, showing square-root boundary sensitivity. The reduced face for delta=0 is not equivalent to the perturbed problem with delta>0.

##### Exercises with answers

1. Why does a PSD matrix with `X11=0` have `X12=0`? **Answer:** the determinant of its principal 2x2 block would otherwise be negative.
2. What exposes the face in this example? **Answer:** `Z=diag(1,0)` with `<Z,X>=0` on all feasible X.
3. Does Slater failure imply that primal and dual optimal values must differ? **Answer:** no; it removes a sufficient guarantee, not the possibility of equality.
4. What is the maximal absolute off-diagonal entry for `X11=1/100`, `tr X=1`? **Answer:** `sqrt((1/100)(99/100))=sqrt(99)/100`.

##### Reading and source notes

- [Borwein and Wolkowicz, Facial Reduction for a Cone-Convex Programming Problem](https://doi.org/10.1017/S1446788700017250), foundational facial-reduction principle.
- [Facial reduction for symmetry-reduced semidefinite and doubly nonnegative programs](https://pmc.ncbi.nlm.nih.gov/articles/PMC10195748/), exposing vectors and minimal faces.
- [Pataki, Bad Semidefinite Programs: They All Look the Same](https://arxiv.org/abs/1112.1436), pathological duality and degeneracy in SDP.

### Exact Semidefinite Certificates and Weak Infeasibility

**Track:** Optimization, Convexity, and Duality. **Background:** convex cones, linear programming duality, symmetric matrices, and exact arithmetic. **Central question:** when does a numerical semidefinite solver's answer become a mathematical proof?

#### Mathematical companion (not spoken)

**Exact optimality.** For `X\in\mathbb S_+^2`, consider
\[
\max X_{12}\quad\text{subject to }X_{11}=X_{22}=1.
\]
Define `C=\frac12\begin{pmatrix}0&1\\1&0\end{pmatrix}` so `\langle C,X\rangle=X_{12}`. The primal candidate is `X_* = \begin{pmatrix}1&1\\1&1\end{pmatrix}=vv^T`, `v=(1,1)^T`. The dual minimizes `y_1+y_2` subject to `\mathrm{diag}(y_1,y_2)-C\succeq0`. Take `y_1=y_2=1/2` and `S_*=(1/2)\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0`. Both objectives equal `1`; weak duality proves exact optimality. Complementary slackness `\langle X_*,S_*\rangle=0` also holds.

**Weak infeasibility.** Let the affine family be
\[
X_t=\begin{pmatrix}0&1\\1&t\end{pmatrix},\quad t\in\mathbb R.
\]
Every `X_t` has determinant `-1`; no one is PSD. For `t>0`,
\[
Y_t=\begin{pmatrix}1/t&1\\1&t\end{pmatrix}=\begin{pmatrix}1/\sqrt t\\\sqrt t\end{pmatrix}\begin{pmatrix}1/\sqrt t&\sqrt t\end{pmatrix}\succeq0,
\]
and `\|X_t-Y_t\|_F=1/t\to0`. Thus the affine space and PSD cone are disjoint but have distance zero. This is weak infeasibility, so one cannot demand a standard strictly separating Farkas witness in the original formulation.

For an exact *multistep* contradiction, use `X\succeq0` and `\langle E_{11},X\rangle=X_{11}=0`, which imply `X_{1j}=0` for all j by the PSD Cauchy–Schwarz inequality `|X_{ij}|^2\le X_{ii}X_{jj}`. The independent constraint `X_{12}=1` then contradicts the restricted face. This illustrates a facial reduction explanation, not a universal one-step certificate for all infeasible SDPs.

##### Exercises with answers

1. What upper bound does PSD impose on `|X_{12}|` when `X_{11}=X_{22}=1`? **Answer:** at most `1`.
2. Check `\det X_t`. **Answer:** `-1`, independent of t.
3. Why is the second system weakly rather than strongly infeasible? **Answer:** PSD matrices `Y_t` approach the affine set with distance `1/t\to0` although the sets never intersect.
4. What is needed beyond approximate primal and dual residuals to certify exact optimality? **Answer:** rigorous primal/dual feasibility and matching objective bounds, possibly using exact or interval arithmetic.

##### Reading and source notes

- [Liu and Pataki, Exact Duality in Semidefinite Programming Based on Elementary Reformulations](https://doi.org/10.1137/140972354), exact infeasibility and facial-reduction reformulations.
- [Blekherman, Parrilo, and Thomas (eds.), Semidefinite Optimization and Convex Algebraic Geometry](https://www.mit.edu/~parrilo/sdocag/), semidefinite cones and exact algebraic certificates.
