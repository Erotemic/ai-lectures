# Discrete Inf–Sup: A Two-Cell Failure and a Compatible Repair

**Track:** Multivariable Calculus from First Principles. **Focus:** a spurious pressure mode on two cells, stable derivative-pressure pairs, uniform discrete inf–sup bounds, Raviart–Thomas spaces, and local conservation.

<!-- BEGIN SPOKEN LECTURE -->

# Discrete Inf–Sup: A Two-Cell Failure and a Compatible Repair

It is possible to build a finite-element approximation in which every individual basis function looks perfectly respectable, the mesh is simple, and the assembled equations cannot distinguish zero pressure from an oscillating nonzero pressure. You do not need a computer to find the failure. Two cells are enough.

The reason matters well beyond finite elements. When one variable enforces a constraint on another, choosing approximations for the variables independently can create degrees of freedom that no equation actually sees. The cure is to match the spaces to the differential operator connecting them.

We will do a complete one-dimensional calculation. We are not pretending that one-dimensional incompressible fluid flow is a realistic Stokes experiment. The interval is a minimal model for the coupling between a field derivative and a scalar multiplier, the same algebraic pattern that appears with velocity divergence and pressure in higher dimensions.

## What the discrete condition asks

Let a field v vanish at the endpoints of the unit interval. Let q be a square-integrable scalar function with mean zero. Couple them by integrating q times v prime. In the continuous setting this is a healthy coupling. For any mean-zero q, define v at x to be the integral of q from zero to x. Then v is zero at both endpoints, its derivative is q, and its derivative norm equals the norm of q. The coupling of v and q is the squared norm of q.

Thus, if we use the derivative norm for v and the L two norm for q, the continuous inf–sup constant is exactly one. No scalar mode is undetectable. This calculation is our reference: we know the continuous problem has excellent coupling before discretization.

Now split the interval at one half. For the field space, use continuous piecewise linear functions that vanish at both endpoints. There is only one independent field function, the hat that rises from zero at the left endpoint to one at the midpoint, then falls to zero at the right endpoint. Its derivative equals positive two on the left cell and negative two on the right cell.

For the scalar space, make what seems a natural choice: continuous piecewise linear functions with mean zero, the same polynomial degree as the field. There are two independent scalar degrees of freedom after imposing the mean-zero condition. Both spaces are conforming subspaces of their respective continuous spaces. Both can approximate smooth functions when refined in suitable ways. Yet this pair already contains an invisible scalar.

## A pressure that every velocity test misses

Give the scalar function values one at the left endpoint, negative one at the midpoint, and one at the right endpoint. Join these values with straight lines. It makes a V-shaped trough, though it rises again toward the right end. It is not zero. Its squared L two norm integrates to one third, so its size is one over the square root of three.

But the average of this scalar over the left half is zero: the line descends symmetrically from one to negative one. Its average over the right half is also zero: the line rises from negative one to one. Therefore its mean over the whole interval is zero, as required.

Remember that our field test has constant derivative within each cell. Multiply the scalar by that derivative and integrate. On the left cell the integral is positive two times the cell integral of the scalar, which is zero. On the right it is negative two times another zero. The total coupling is zero.

And since every admissible discrete field is merely a multiple of this one hat, the coupling vanishes for every discrete field. We have exhibited a nonzero scalar mode in the kernel of the transpose of the discrete coupling matrix. The discrete inf–sup constant is exactly zero.

This is more serious than an approximation that is a little inaccurate. If pressure or a Lagrange multiplier lives in this scalar space, a multiple of that mode can be added without changing the tested equations. The multiplier is not uniquely determined. A solver may report singularity, or select a representative using a numerical convention, but the missing information is a property of the discretization.

It is tempting to blame the two-element mesh, yet the real mismatch is visible by counting what the derivative of a field can represent. Our field space has one degree of freedom. Our chosen mean-zero scalar space has two. Even before constructing the oscillation, a linear map from a one-dimensional field space cannot detect every direction of a two-dimensional scalar space.

Dimension counting is a useful first alarm. It is not a complete stability proof. In more complicated spaces the dimensions may look favorable while some multiplier modes still become arbitrarily weak as the mesh is refined.

## Repair the scalar space

Keep exactly the same field space but change the scalar space to functions that are constant on each cell and have mean zero. Such a scalar has value c on the left and negative c on the right. This space has one degree of freedom, matching the derivative of the hat function.

Compute the coupling. The derivative of the hat is two on the left and negative two on the right. The integral of q times v prime is one half times two c, plus one half times two c, giving two c. The derivative norm of the hat is two. The L two norm of q is the absolute value of c. Therefore the normalized coupling has magnitude one.

The discrete inf–sup constant is exactly one. We have repaired the defect without raising the polynomial degree or adding a penalty term. We changed which functions the multiplier is allowed to represent.

There is an even stronger result. This repair works not just on two equal intervals but on any partition of the unit interval. Take continuous piecewise linear fields with zero endpoint values, and piecewise constant scalars with zero mean. Given any such scalar q, integrate it from zero to x. The result is a continuous piecewise linear field, and because q has zero mean it vanishes at the right endpoint. Its derivative is exactly q on every cell. Once again the normalized coupling equals one. So the discrete inf–sup constant is one for every mesh, regardless of how many cells it has.

This is what a mesh-uniform stability estimate looks like when we can see the construction directly. We have not merely shown that a particular finite-dimensional matrix is invertible. We have supplied the same quantitative bound on every partition in the family.

## Discrete spaces and conservation laws

The derivative of a continuous piecewise linear function is piecewise constant. That simple fact explains the successful pair. In a diffusion problem, the discrete flux can live in the continuous piecewise linear space and the scalar potential in the piecewise constant space. Because flux derivative belongs to the scalar space, testing conservation against cell indicators forces the correct integrated balance on every cell.

On a surface or in a volume, the corresponding operator is divergence. We want an approximation space for vector fluxes whose normal components match across internal faces, and a scalar space suited to their divergences. The lowest-order Raviart–Thomas family is a standard answer on simplicial meshes.

On a triangle, a lowest-order Raviart–Thomas field is a constant vector plus a constant scalar times the position vector. Its divergence is constant within that triangle, and its normal component is constant along each straight edge. Degrees of freedom can be chosen as the integral of normal flux across each edge. Adjacent cells share the same flux moment with opposite outward orientations. That makes the assembled field conforming in H div and produces cancellation of interior fluxes in the sum of cell balances.

Pair that flux space with cellwise constants for the scalar potential. The derivative-divergence relationship is built into the approximation spaces. Under the standard mesh assumptions and appropriate boundary conditions, this pair satisfies the discrete stability requirements for the mixed Poisson problem.

One should not conclude that any space called continuous or discontinuous automatically works. For incompressible Stokes flow, the velocity belongs to an H one space, not generally to the H div flux space used for Darcy's law. The pressure is coupled through velocity divergence, and the appropriate stable element pairs have their own theory. A familiar example is the Taylor–Hood family, which uses continuous quadratic velocity and continuous linear pressure on suitable meshes.

What transfers from one problem to another is the design principle: identify the differential operator and choose discrete spaces that preserve its meaningful range, null spaces, and constraints. The precise pair must be checked for the particular equation and mesh family.

## An abstract way to certify compatibility

There is a useful strategy for proving a uniform discrete inf–sup bound without finding each worst pressure mode. Begin with a continuous inf–sup condition. Then construct a projection or interpolation operator from continuous fields into the discrete field space. Require two properties. First, the projection must preserve the coupling with every discrete multiplier: testing the projected field should give the same result as testing the original field. Second, the projection must have a norm bound independent of mesh size.

Such an operator is commonly called a Fortin operator. Here is why it helps. Fix a discrete pressure q. Continuous stability says there is a continuous field v that detects q. Project v into the discrete space. The coupling does not change, while the size of the projected field grows by at most the projection's uniform norm bound. Consequently the discrete inf–sup constant is at least the continuous constant divided by that bound.

This is more than a formal trick. In compatible finite-element families, specially designed interpolation operators often commute with divergence or another differential operator. The algebraic relation is the reason conservation and stability can persist through discretization. Some natural interpolators are not bounded on the full lowest-regularity space, so their proof domains and any smoothing required must be stated carefully. But the strategy—preserve the constraint while controlling size—is broadly useful.

## What we actually learned from two cells

The failed equal-order pair was not defective because it used low-order polynomials. The successful pair used low-order polynomials too. Failure occurred because the multiplier space contained a mode orthogonal to the derivative of every test field. Repair came from matching the multiplier space to the discrete derivative.

That is why checking interpolation error alone is insufficient for a mixed method. We also need an inf–sup estimate that stays positive as the mesh changes. For a diffusion problem we can make flux conservation exact cell by cell. For incompressible flow we can control pressure without a spurious kernel. For other equations, compatible discrete structures can preserve identities such as divergence of curl equals zero.

The interval example gave us a complete diagnostic. We can now approach Stokes flow with a clear mathematical question instead of memorizing a table of element names: does the velocity space detect every allowed pressure mode, with a mesh-independent bound, and does the energy control the remaining velocity directions?

<!-- END SPOKEN LECTURE -->

## Mathematical companion: the two-cell inf–sup counterexample

Let \(\Omega=(0,1)\), \(V=H^1_0(0,1)\) with norm \(\|v\|_V=\|v'\|_{L^2}\), and \(Q=L^2_0(0,1)\) with its \(L^2\)-norm. Define \(b(v,q)=\int_0^1qv'\,dx\).

Given any \(q\in Q\), choose \(v(x)=\int_0^xq(t)\,dt\). Then \(v(0)=v(1)=0\), \(v'=q\), and

\[
\sup_{v\ne0}\frac{b(v,q)}{\|v\|_V}=\|q\|_{L^2},\qquad\beta=1.
\]

For the two-cell mesh, \(V_h=\operatorname{span}\{\phi\}\), where

\[
\phi(x)=\begin{cases}2x,&0\le x\le\frac12,\\2(1-x),&\frac12\le x\le1.\end{cases}
\quad
\phi'(x)=\begin{cases}2,&0<x<1/2,\\-2,&1/2<x<1.\end{cases}
\]

Choose \(Q_h^{\rm bad}\) to be continuous piecewise affine mean-zero functions. The function

\[
q_h(x)=\begin{cases}1-4x,&0\le x\le\frac12,\\4x-3,&\frac12\le x\le1\end{cases}
\]

has nodal data \((1,-1,1)\), \(\int_0^1q_h=0\), \(\int_0^1q_h^2=1/3\), and \(\int_{K_i}q_h=0\) on each cell. Thus \(b(\phi,q_h)=0\), so \(\beta_h=0\).

For \(Q_h^{\rm good}=\{q:q|_{K_1}=c,\ q|_{K_2}=-c\}\),

\[
b(\phi,q)=2c,\quad\|\phi\|_V=2,\quad\|q\|_{L^2}=|c|,\quad\beta_h=1.
\]

For an *arbitrary* partition, \(V_h=P_1^{\rm cont}\cap H^1_0\) and \(Q_h=P_0^{\rm broken}\cap L^2_0\) obey \(\beta_h=1\): for every \(q_h\in Q_h\), the integral \(v_h(x)=\int_0^xq_h(t)\,dt\) belongs to \(V_h\) with \(v'_h=q_h\).

### Compatibility in two dimensions

On a triangle \(K\subset\mathbb R^2\), the local lowest-order Raviart–Thomas space is

\[
\mathrm{RT}_0(K)=\{a+c\,x:a\in\mathbb R^2,\ c\in\mathbb R\},\qquad
\nabla\cdot(a+cx)=2c\in P_0(K).
\]

On a straight edge \(e\), \(x\cdot n\) is constant, so \((a+cx)\cdot n\) is constant. Matching integrated normal flux degrees of freedom on shared edges defines an \(H(\mathrm{div})\)-conforming global space. With cellwise constant scalars, the divergence maps into the scalar space. For mixed Poisson, stability also requires the correct norm, boundary constraints, and mesh-independent estimates; this algebraic inclusion alone is not the full proof.

### Fortin argument, including the hypothesis

Suppose \(V_h\subset V\), \(Q_h\subset Q\), continuous inf–sup constant \(\beta>0\), and an operator \(\Pi_h:V\to V_h\) satisfies

\[
b(\Pi_hv,q_h)=b(v,q_h)\ \forall v\in V,\ q_h\in Q_h,
\qquad \|\Pi_hv\|_V\le C\|v\|_V
\]

with \(C\) independent of mesh size. For any fixed \(q_h\ne0\),

\[
\sup_{v_h\in V_h\setminus\{0\}}\frac{b(v_h,q_h)}{\|v_h\|_V}
\ge\frac1C\sup_{v\in V\setminus\{0\}}\frac{b(v,q_h)}{\|v\|_V}
\ge\frac\beta C\|q_h\|_Q.
\]

Therefore \(\beta_h\ge\beta/C\). An actual proof must construct such a bounded operator, possibly with additional regularization in low-regularity settings.

### Exercises with answers

1. **Exact ghost mode:** Verify \(\int_0^{1/2}(1-4x)\,dx=0\). **Answer:** \([x-2x^2]_0^{1/2}=1/2-1/2=0\).
2. **Norm:** Compute \(\|q_h\|_2^2\) for the V-shaped ghost mode. **Answer:** \(1/3\), two symmetric integrals of \(1/6\).
3. **Arbitrary mesh:** Prove \(\int_0^1q_h=0\) is exactly what makes \(v_h(x)=\int_0^xq_h\) satisfy the right boundary condition. **Answer:** \(v_h(1)=\int_0^1q_h=0\).
4. **Conservation:** If \(q_h\in\mathrm{RT}_0\), why do internal edge contributions cancel when summing cell balances? **Answer:** The two adjacent cells use opposite outward normals, while the global normal flux trace agrees.
5. **Fortin proof:** Where does mesh independence enter the bound \(\beta_h\ge\beta/C\)? **Answer:** Through a constant \(C\) uniformly bounding \(\Pi_h\); if \(C\) grows with refinement, the argument gives no uniform lower bound.

### Sources and further reading

- Franco Brezzi and Michel Fortin, [*Mixed and Hybrid Finite Element Methods* (1991)](https://link.springer.com/book/10.1007/978-1-4612-3172-1), on discrete inf–sup and stable element design.
- Daniele Boffi, Franco Brezzi and Michel Fortin, [*Mixed Finite Element Methods and Applications* (2013)](https://link.springer.com/book/10.1007/978-3-642-36519-5), on Raviart–Thomas elements and Fortin operators.
- Douglas N. Arnold, Richard S. Falk and Ragnar Winther, [*Finite element exterior calculus*](https://doi.org/10.1090/S0273-0979-10-01278-4) (2010), for compatible complexes and commuting projections.
- [Wikipedia: Ladyzhenskaya–Babuška–Brezzi condition](https://en.wikipedia.org/wiki/Ladyzhenskaya%E2%80%93Babu%C5%A1ka%E2%80%93Brezzi_condition) and [Mixed finite element method](https://en.wikipedia.org/wiki/Mixed_finite_element_method).

*Teaching connections:* `040000` develops the abstract stability requirement, `039000` explains flux conservation, and `034000` supplies the ordinary finite-element assembly against which the mixed method can be compared.
