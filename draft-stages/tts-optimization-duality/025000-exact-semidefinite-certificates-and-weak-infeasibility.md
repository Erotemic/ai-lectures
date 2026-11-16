# 025000 — Exact Semidefinite Certificates and Weak Infeasibility

**Track:** Optimization, Convexity, and Duality. **Background:** convex cones, linear programming duality, symmetric matrices, and exact arithmetic. **Central question:** when does a numerical semidefinite solver's answer become a mathematical proof?

<!-- BEGIN SPOKEN LECTURE -->

# A tiny numerical error can change a theorem

A semidefinite program optimizes a linear objective over symmetric positive semidefinite matrices subject to linear equations. Numerical solvers are highly effective at finding approximate answers, but the distinction between an approximation and a proof becomes important near the boundary of the positive semidefinite cone.

A matrix can be positive semidefinite with an eigenvalue exactly zero. A floating-point approximation may report a slightly negative eigenvalue even when the exact matrix is feasible. The reverse error is more dangerous for certification: a matrix whose true smallest eigenvalue is negative can appear nonnegative at the available precision.

Exact certification does not require solving every semidefinite problem symbolically from the beginning. It asks us to turn a proposed solution or dual certificate into an identity that can be checked in an arithmetic domain where the crucial signs are rigorous.

# An exact optimality certificate

Consider a two-by-two symmetric positive semidefinite matrix whose diagonal entries are both one. We want to maximize the off-diagonal entry.

Positive semidefiniteness requires the determinant to be nonnegative. With diagonal entries one, the off-diagonal entry must lie between negative one and positive one. The matrix with every entry one is positive semidefinite and reaches the upper bound. Therefore the optimal value is exactly one.

This can also be certified by duality. In the dual problem, assign the weight one half to each diagonal equality. The resulting dual slack is a positive semidefinite matrix with entries one half on the diagonal and negative one half off-diagonal. Its dual objective is one.

Weak duality says no primal feasible matrix can exceed a dual feasible value. A primal matrix attaining one and a dual matrix bounding the value by one prove optimality without relying on a solver tolerance. All the entries in this example are rational numbers, and their matrix signs can be checked exactly.

# A feasible set that almost exists

Now consider a different problem. Require a two-by-two matrix to be positive semidefinite, with its upper-left diagonal entry equal to zero and its off-diagonal entry equal to one. Is there a solution?

No. For a positive semidefinite matrix, if a diagonal entry is zero, every entry in the corresponding row and column must be zero. Otherwise the determinant of a two-by-two principal submatrix would be negative. So an off-diagonal entry equal to one is impossible.

That proof is elementary and exact. But something surprising happens numerically.

Consider the affine matrices with upper-left entry zero, off-diagonal entries one, and lower-right entry t, where t is very large and positive. These are all infeasible because their determinant is negative one. Yet they are arbitrarily close to positive semidefinite matrices: simply change the upper-left entry from zero to one over t. The modified matrix has determinant zero and is positive semidefinite. The change tends to zero as t grows.

Thus the affine constraint space and the positive semidefinite cone do not intersect, but their distance is zero. This is called weak infeasibility.

A numerical solver may approach matrices with larger and larger entries and smaller and smaller constraint violations. It may struggle to distinguish weak infeasibility from a feasible problem with severe scaling. The difficulty is geometric, not simply a poorly chosen tolerance.

# Why a familiar Farkas certificate can fail

For linear programming, infeasibility is usually captured by a finite dual separating certificate. For semidefinite programming, the image of the positive semidefinite cone under a linear map need not be closed. A missing point can lie in the closure of the image.

That failure of closedness is exactly what happens in weak infeasibility. There may be no strictly separating dual hyperplane in the original formulation. A standard numerical dual residual might therefore fail to provide an exact certificate even though the primal problem is genuinely infeasible.

Facial reduction and elementary reformulations can expose the right smaller face or contradiction. In our example, the zero diagonal constraint forces the feasible matrix—if one existed—to lie in a face where its entire first row vanishes. Inside that face, the requirement that the first off-diagonal entry equals one is transparently contradictory.

The sequence of deductions is short enough to verify by hand. More complicated semidefinite problems can need several exposing steps, and symbolic certification may involve rational or algebraic reconstruction followed by exact matrix checks.

# From approximate answer to proof artifact

A practical certification workflow begins with numerical computation. Solve the primal and dual approximately, inspect residuals and the likely ranks, and attempt to reconstruct simple exact values. Then verify the equalities, inequalities, and complementary slackness in exact arithmetic or with certified interval bounds.

A rational positive semidefinite matrix can be checked through exact principal minors or a suitable exact factorization. A certificate for optimality requires both a feasible primal candidate and a feasible dual candidate with matching objective values, or a separately justified rigorous bound. A certificate for infeasibility may require facial reduction instead of a single unqualified Farkas vector.

The goal is not to distrust numerical solvers. It is to use them for what they do well—finding promising structure—then use exact reasoning to establish what a theorem requires.

# The cone has a boundary worth respecting

Linear programs and semidefinite programs are both convex, but their geometries differ. The positive semidefinite cone is curved, it has faces indexed by subspaces, and its linear images can fail to be closed.

The two-by-two optimality example shows how clean exact primal-dual witnesses can be. The weakly infeasible example shows why not every status report can be justified by the same kind of certificate. Reliable semidefinite optimization requires understanding both the arithmetic of a proposed witness and the geometry of the cone that the witness inhabits.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. What upper bound does PSD impose on `|X_{12}|` when `X_{11}=X_{22}=1`? **Answer:** at most `1`.
2. Check `\det X_t`. **Answer:** `-1`, independent of t.
3. Why is the second system weakly rather than strongly infeasible? **Answer:** PSD matrices `Y_t` approach the affine set with distance `1/t\to0` although the sets never intersect.
4. What is needed beyond approximate primal and dual residuals to certify exact optimality? **Answer:** rigorous primal/dual feasibility and matching objective bounds, possibly using exact or interval arithmetic.

### Reading and source notes

- [Liu and Pataki, Exact Duality in Semidefinite Programming Based on Elementary Reformulations](https://doi.org/10.1137/140972354), exact infeasibility and facial-reduction reformulations.
- [Blekherman, Parrilo, and Thomas (eds.), Semidefinite Optimization and Convex Algebraic Geometry](https://www.mit.edu/~parrilo/sdocag/), semidefinite cones and exact algebraic certificates.
