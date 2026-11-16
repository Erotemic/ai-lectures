# 016000 — Homogeneous Self-Dual Embeddings and Infeasibility Certificates

**Track:** Optimization and Duality. **Background:** conic programming, weak duality, KKT conditions, primal and dual feasibility. **Central question:** can one mathematical system reveal an optimum or explain why an optimization problem has no feasible solution?

<!-- BEGIN SPOKEN LECTURE -->

# A solver should be able to explain failure

A numerical optimizer may return a vector that looks promising. It may also report that a problem is infeasible, unbounded, or numerically difficult. These statements are not interchangeable. An infeasibility claim should be supported by evidence, just as an optimality claim should be supported by a duality gap and feasibility residuals.

Homogeneous self-dual embedding provides one way to organize these alternatives. Rather than solving the primal and dual optimization problems completely separately, we enlarge the variables and build a homogeneous feasibility problem. A nonzero solution of that larger system can encode an optimal primal-dual pair, or in other cases, a certificate of infeasibility.

The key is to remember what a certificate means. It is a mathematical object whose defining equations can be checked independently. A solver's printed status is only as trustworthy as the residuals, tolerances, and assumptions that support that status.

## Begin with a cone program

Let x be an unrestricted vector of decision variables. The objective is a linear function of x. The constraints can be written by introducing a slack vector s that belongs to a closed convex cone. A linear map of x plus s must equal a specified right-hand side.

The dual problem uses a vector y in the dual cone. Its linear equality connects the transpose of the constraint map to the objective coefficients. Weak duality says that the dual objective cannot exceed the primal objective whenever both points are feasible.

A zero duality gap between feasible primal and dual points certifies optimality. But if the primal constraints cannot be met at all, we need a different kind of witness. A separating vector in the dual cone can make the right-hand side have a sign that every feasible slack would contradict. This is a conic version of Farkas' lemma.

## Add two nonnegative scalars

The embedding introduces two nonnegative scalar variables, commonly called tau and kappa. It makes the primal constraints, dual constraints, and zero-gap equation homogeneous. Setting all variables to zero always satisfies the resulting equations, so the meaningful question is whether we obtain an appropriately normalized nonzero solution.

If tau is positive, divide the original variables by tau. The normalized vectors satisfy the primal and dual constraints. Algebraic identities inside the embedding imply that kappa must be zero and the primal-dual gap vanishes. Under these exact conditions, the normalized vectors are an optimal pair.

If kappa is positive, tau must be zero. The remaining equations instead encode a direction of infeasibility. One can inspect whether the certificate contradicts primal feasibility or dual feasibility. This provides a structured alternative to having a solver simply run out of iterations.

It is important not to assume that every nonzero embedded solution falls neatly into one of those two cases. The degenerate case with both tau and kappa zero can occur, and conic pathologies may require further analysis. An approximate numerical iterate also needs thresholds and independent residual checks.

## A primal infeasibility example

Consider a one-dimensional decision variable constrained to be at least one and at most zero. There is no feasible value: the interval is empty. In conic form these are two linear inequalities with two nonnegative slack variables.

Assign the same positive multiplier to each inequality. When we add their linear left-hand sides, the decision variable cancels. What remains would require a nonnegative quantity to equal a negative number. That contradiction is a certificate of infeasibility. It does not depend on trying many candidate values of x.

In the homogeneous embedding, the dual multiplier and the nonnegative kappa variable can encode precisely this contradiction. The algebraic equations verify it, and the sign condition is impossible for any primal-feasible x and slack.

The example is deliberately simple. In large cone programs, certificates can involve thousands of variables, semidefinite matrices, second-order cones, or exponential cones. The same separation principle continues to apply, but accuracy of the computed certificate becomes a serious numerical question.

## One skew-symmetric linear system

A standard embedding can be expressed using a skew-symmetric block matrix. It combines the constraint matrix, objective coefficients, and right-hand side. A vector containing x, y, and tau is mapped to a vector containing a zero block, the primal slack s, and kappa.

Skew symmetry matters because the quadratic form obtained by taking the inner product of a vector with its image is zero. Along with cone duality, this forces complementarity conditions. The structure makes the embedding compatible with operator-splitting methods and projection algorithms.

A popular implementation, SCS, applies operator splitting to this homogeneous feasibility system. Such first-order methods can address very large cone programs, though modest-accuracy solutions and rigorous high-precision certificates are different goals. Interior-point embeddings use related ideas with different numerical behavior.

## Diagnosing what the solver actually found

Suppose a numerical result has positive tau but a visibly nonzero normalized primal residual. It is not yet a certified optimum. Suppose it reports positive kappa but the proposed separating vector has the wrong sign, or lies outside the dual cone beyond tolerance. It is not a valid infeasibility witness.

This is particularly important in ill-conditioned problems or those lacking strict feasibility. Facial reduction may be required to expose the correct lower-dimensional face before standard duality arguments become reliable.

The mathematical benefit of homogeneous self-dual embedding is a shared framework for success and failure. It makes optimality and infeasibility part of the same geometry, while leaving us with concrete equations that can be checked rather than status labels that must be trusted.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. For feasible primal and dual points, prove weak duality. **Answer:** `c^Tx+b^Ty=s^Ty>=0` because `s in K` and `y in K*`.
2. What does `tau>0` allow? **Answer:** normalization of the embedded x,s,y to a feasible primal-dual zero-gap pair.
3. Give a certificate that `x>=1` and `x<=0` cannot both hold. **Answer:** add the inequalities or use `y=(1,1)` in the specified cone representation to obtain `b^Ty=-1<0`.
4. Does `tau=kappa=0` certify optimality or infeasibility? **Answer:** no; it is a potentially degenerate case requiring further analysis.

### Reading and source notes

- [O'Donoghue, Chu, Parikh and Boyd, Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding](https://www-leland.stanford.edu/~boyd/papers/scs.html), embedding and first-order algorithm.
- [Permenter, Friberg and Andersen, Self-Dual Embedding and Facial Reduction](https://optimization-online.org/2015/09/5104/), degeneracy and failure of strict feasibility.
- [SCS, Algorithm and Conic Solver Documentation](https://www.cvxgrp.org/scs/), practical residual and status conventions.
