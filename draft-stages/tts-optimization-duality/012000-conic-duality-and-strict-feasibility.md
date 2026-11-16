# 012000 — Conic Duality: One Language for Linear, Quadratic, and Matrix Inequalities

**Track:** Optimization and Duality. **Background:** convex cones, linear programming, Lagrangians, KKT conditions, semidefinite programming. **Central question:** how can different kinds of convex constraints share one duality theorem and one style of optimality certificate?

<!-- BEGIN SPOKEN LECTURE -->

# Conic Duality: One Language for Linear, Quadratic, and Matrix Inequalities

Linear programming constrains variables to lie in half-spaces. Semidefinite programming constrains matrices to be positive semidefinite. Second-order cone programming constrains the length of a vector to be no greater than a scalar. These look like different mathematical worlds, but they share an organizing structure: an affine subspace intersected with a convex cone.

Conic optimization expresses that structure directly. Once it does, weak duality, complementarity, and conditions for strong duality can be derived in one framework rather than as separate tricks for every problem class.

## What a cone contributes

A cone contains the nonnegative scalar multiples of its elements. A convex cone is also closed under addition, and we usually work with closed convex cones for standard finite-dimensional conic optimization.

The nonnegative orthant is the cone behind ordinary linear programming. The cone of positive semidefinite symmetric matrices gives semidefinite programming. The second-order, or Lorentz, cone consists of pairs of a scalar t and a vector u satisfying t at least the Euclidean norm of u. Convexity follows from the triangle inequality.

A conic problem can minimize a linear objective over variables x constrained by a linear equation A x equals b and membership x in a cone K. Many convex problems admit a formulation of this type after introducing auxiliary variables or slack variables.

But representation matters. Different equivalent mathematical models can have very different sizes, numerical conditioning, or constraint qualifications. A conic formulation is a common language, not a promise that every formulation is computationally equally good.

## The dual cone and weak duality

Every cone K has a dual cone K star. It contains all vectors s whose inner product with every vector in K is nonnegative. Think of a dual-cone element as a linear functional that can never assign a negative value to a feasible cone direction.

Introduce a multiplier y for the equation A x equals b. The Lagrangian takes the linear objective c dot x and subtracts y dot the constraint residual A x minus b. Collect the terms involving x: its coefficient is c minus A transpose y.

When that coefficient belongs to K star, its inner product with every x in K is nonnegative. Therefore the Lagrangian is bounded below by b dot y. This leads to the conic dual: maximize b dot y subject to c minus A transpose y belonging to K star.

The proof of weak duality now fits on one line of algebra. For primal feasible x and dual feasible y, subtract the dual objective from the primal objective. The result is the inner product of x with c minus A transpose y. One vector lies in K, the other in K star, so the difference is nonnegative.

That conclusion needs no Slater condition and no numerical algorithm. Any pair of exactly feasible points gives a rigorous lower and upper bound on the optimum.

## Three self-dual examples

The nonnegative orthant is self-dual: a vector has nonnegative dot product with every nonnegative vector exactly when its coordinates are nonnegative. That gives the usual sign restrictions in LP duality.

The second-order cone is also self-dual under the standard Euclidean inner product. Its defining inequality, t at least the norm of u, is a familiar norm bound. The self-duality can be understood using Cauchy–Schwarz: the worst direction opposing u has the same magnitude and opposite direction.

The positive semidefinite cone is self-dual under the trace inner product. If X and S are positive semidefinite, the trace of their product is nonnegative. Conversely, a symmetric matrix with a negative eigenvalue has negative trace inner product with a suitable rank-one positive semidefinite matrix. This recovers the dual constraints used in semidefinite programming.

Not every convex cone is self-dual. The cone and its dual may require different descriptions. The conic-duality framework works because it names the two separately rather than assuming they coincide.

## A norm as an optimization problem

Fix a vector a. What is its Euclidean norm? We can express it as the smallest scalar t such that the pair t and a belongs to the second-order cone. The primal answer is the norm of a by definition.

The corresponding dual viewpoint maximizes the inner product of a with a vector y constrained to have norm at most one. Cauchy–Schwarz says the inner product can never exceed the norm of a. If a is nonzero, choose y in the direction of a with unit length, and equality holds.

Thus the equality between a norm and the support function of the unit ball is a concrete case of conic duality. The primal chooses the smallest enclosing magnitude. The dual chooses the direction that certifies that magnitude cannot be smaller.

This example illustrates what a certificate does: instead of trusting a solver's claim that t is minimal, produce a feasible dual vector whose objective matches t.

## When do the bounds coincide?

Weak duality only says the dual value cannot exceed the primal value. Strong duality says their optimal values are equal. For finite-dimensional convex conic problems, a standard sufficient condition is strict feasibility, often called Slater's condition.

In the simple primal form with equality constraints, strict feasibility means there is an x satisfying A x equals b that lies in the interior of K. Together with suitable finiteness assumptions, this provides strong duality and attainment of a dual optimum. There are refinements for cones with empty interior in an ambient representation, where relative interior and facial reduction enter.

The condition is sufficient, not necessary. Strong duality can hold even if no strictly feasible point exists. Conversely, without appropriate constraint qualifications, a conic problem may have a positive duality gap, an unattained optimum, or delicate feasibility behavior. Semidefinite optimization in particular admits weak infeasibility, where an affine space has zero distance to the cone without intersecting it.

Slater's condition is a theorem hypothesis, not a setting in a software interface. A solver can report numerical feasibility without proving that the exact mathematical problem meets the required condition.

## Complementarity and certificates

Suppose primal and dual optima are both attained and the gap is zero. The inner product between the primal cone variable and the dual slack must vanish. This is complementarity. For the nonnegative orthant, it reduces to coordinatewise products of primal and dual slack variables being zero. For semidefinite optimization, it becomes orthogonality of positive semidefinite matrices in the trace inner product.

To verify a candidate solution, check the linear equalities, cone membership, and the objective gap. Approximate solutions require an additional numerical error analysis. A tiny floating-point residual is evidence of a good answer, not by itself a mathematical proof of exact feasibility or zero gap.

The unifying benefit of conic duality is clear. LP, second-order cone programs, and SDP share the same weak-duality algebra. Their cones differ, but the language of dual cones and complementary slackness does not. Theorems about strong duality then become precise statements about geometry: whether the feasible affine space reaches the cone's interior, and whether separating functionals can be used without a gap.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(K\subset\mathbb R^n\) be a nonempty closed convex cone with \(K^*=\{s:\langle s,x\rangle\ge0\ \forall x\in K\}\). In a standard equality-form convention,
\[\text{(P)}\quad\inf\{c^Tx:Ax=b,\ x\in K\},\qquad\text{(D)}\quad\sup\{b^Ty:c-A^Ty\in K^*\}.\]
For feasible \(x,y\), \(c^Tx-b^Ty=\langle x,c-A^Ty\rangle\ge0\): weak duality. When both attain a common value, \(\langle x,c-A^Ty\rangle=0\) (complementarity). A standard sufficient strong-duality qualification is primal strict feasibility \(Ax=b\) with \(x\in\operatorname{int}K\), together with finite primal optimal value; then the dual optimum is attained and values coincide (nondegenerate finite-dimensional setting).

**Three cones:**
\[\mathbb R_+^n=(\mathbb R_+^n)^*,\quad\mathcal Q_{m+1}=\{(t,u):t\ge\|u\|_2\}=\mathcal Q_{m+1}^*,\quad\mathbb S_+^m=(\mathbb S_+^m)^*\ \text{under}\ \langle X,S\rangle=\operatorname{tr}(XS).\]
**Norm duality example:** \(\|a\|_2=\min\{t:(t,a)\in\mathcal Q_{m+1}\}=\max\{a^Ty:\|y\|_2\le1\}\). The upper bound is Cauchy–Schwarz; for \(a\ne0\), \(y=a/\|a\|\) attains it.

**Certificate caution:** small numerical residuals are not exact feasibility certificates. A primal–dual feasible pair yields upper/lower bounds, while strict feasibility is a sufficient theorem hypothesis, not a necessary one. Nonclosed conic images can produce duality gaps or weak infeasibility even for a closed cone.

### Exercises with answers

1. Derive weak duality for equality-form conic programs. **Answer:** use \(Ax=b\) to rewrite the gap as \(\langle x,c-A^Ty\rangle\ge0\).
2. Why is the Lorentz cone self-dual? **Answer:** Cauchy–Schwarz shows \((t,u)\cdot(s,v)\ge ts-\|u\|\|v\|\ge0\) for cone members; testing extremal unit directions proves the converse.
3. If a primal and dual feasible pair has equal objectives, what follows even without Slater? **Answer:** both are globally optimal, because weak duality sandwiches every feasible objective.
4. Is Slater necessary for a zero duality gap? **No:** strict feasibility is sufficient under stated finiteness conditions, not necessary.

### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), dual cones, constraint qualifications, and Slater's condition.
- Lieven Vandenberghe and Stephen Boyd, [*Semidefinite Programming*](https://web.stanford.edu/~boyd/papers/sdp), self-dual PSD cone and primal-dual conditions.
- [Boyd et al., *Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding*](https://web.stanford.edu/~boyd/papers/pdf/scs.pdf), conic standard forms and numerical feasibility/optimality residuals.
