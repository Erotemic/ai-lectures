# 021400 — Lagrangian Geometry: Graphs, Intersections, and Exactness

**Track:** Topology and Geometry. **Background:** differential forms, cotangent bundles, symplectic Hamiltonian flow, gradients. **Central question:** why do critical points of a function become intersections of two geometric submanifolds?

<!-- BEGIN SPOKEN LECTURE -->

# Lagrangian Geometry: Graphs, Intersections, and Exactness

Imagine a position-momentum phase space. A general point records where a particle is and how fast it is moving. Now imagine selecting just those states whose momentum obeys a rule determined by position. Such a set is a graph over position space.

Many of the most important graphs in symplectic geometry are Lagrangian submanifolds. They have half the dimension of the full phase space, and the symplectic form vanishes when both arguments lie along the graph. Their intersections turn out to encode critical points of functions. That simple observation is the finite-dimensional doorway into Lagrangian Floer homology.

## Why half dimension is special

On the ordinary q-p plane, every smooth one-dimensional curve has zero symplectic area when evaluated on two tangent vectors to the curve. Both tangent vectors point along the same line, and an alternating two-form vanishes on parallel directions.

In four-dimensional phase space, however, an arbitrary two-dimensional surface need not have this property. Consider the surface spanned by the first position direction and the first momentum direction. Those directions have nonzero symplectic pairing. It is not Lagrangian.

A submanifold is Lagrangian if its tangent space is as large as possible while carrying no symplectic area internally. In a phase space of dimension two n, a Lagrangian therefore has dimension n. In each tangent space it is its own symplectic orthogonal complement.

## The zero section

Take a circle as position space. At each point of the circle attach a momentum line. The resulting cylinder is the cotangent bundle of the circle. The zero section is the central circle consisting of all positions with momentum zero.

Along the zero section, every tangent vector points in the position direction. The symplectic form pairs position with momentum, so it vanishes on the zero section. The zero section is Lagrangian. The same construction works for any smooth position manifold: its zero section inside the cotangent bundle is Lagrangian.

Now consider a smooth function f on position space. At each position q, assign momentum equal to the derivative of f at q. The graph of this derivative is another Lagrangian. The reason is that mixed second derivatives of f agree, and the antisymmetric part required to produce symplectic area cancels.

More generally, the graph of a one-form is Lagrangian exactly when that one-form is closed. A derivative is always closed, so graph-of-derivative is a special case. Closed does not always mean globally a derivative, and that difference will matter.

## Critical points become intersections

Where does the graph of the derivative intersect the zero section? Precisely where the derivative is zero. Thus the intersection points are the critical points of f.

Choose the function cosine of the angle around the circle. It has a maximum at one point and a minimum at the opposite point. Its derivative vanishes at exactly those two places. Hence its graph meets the zero section twice. A simple calculus exercise has turned into a count of Lagrangian intersections.

Move the graph by a small amount while preserving the symplectic structure through a Hamiltonian motion. We expect the number of intersections to vary, but topology prevents us from always eliminating them. Lagrangian Floer theory will replace simple intersection counts with a chain complex that is more stable under such motions.

A picture of two crossing curves is not enough, however. An intersection must be transverse if we want it to be isolated and behave predictably under perturbation. For the graph of d f, transversality at a critical point means the Hessian of f is nonsingular: it is exactly the Morse nondegeneracy condition.

## Exactness is more information than closedness

The cotangent bundle carries a natural one-form built from momentum and position. With our sign convention, take minus p times d q; its exterior derivative is the symplectic form d q wedge d p. A Lagrangian is called exact when this one-form becomes the differential of a globally defined function after restriction to the Lagrangian.

On the graph of d f, the natural one-form restricts to minus d f. So this graph is exact. The zero section is also exact, with zero primitive.

Contrast that with a graph on the circle where the momentum is a fixed nonzero constant. Its defining one-form is closed, because a one-form on a one-dimensional manifold is automatically closed. But it is not the derivative of a single-valued periodic function: its integral once around the circle is nonzero. The graph is Lagrangian but not exact.

This distinction has consequences for intersections. The constant-momentum graph never intersects the zero section. It is produced by shifting every momentum by the same amount, which is a symplectic transformation. But it is not Hamiltonian isotopic to the zero section through compactly supported or appropriate global Hamiltonian flows. Otherwise the intersection results we will eventually prove would give a contradiction.

## Exactness controls a future analytic problem

When we study a holomorphic disk whose boundary lies on one Lagrangian, the symplectic area of the disk equals an integral of the natural one-form around its boundary, provided the ambient symplectic form is exact. If the Lagrangian is exact, that boundary integral vanishes.

Holomorphic disks have nonnegative energy, and in the compatible setting energy equals symplectic area. Thus a disk with boundary on an exact Lagrangian in an exact symplectic manifold must be constant. This removes one important kind of bubbling from later compactness arguments.

It does not remove every difficulty. Curves can still escape to infinity in noncompact cotangent bundles unless geometric estimates prevent it. They may also break into multiple strips. Exactness is a specific tool, not an automatic proof of all Floer theory.

## From calculus to geometry and back

We have now walked a full circle. The derivative of a function gives a Lagrangian graph. Critical points become intersections. Nonsingular Hessians become transverse intersections. Gradients and the trajectories connecting critical points will reappear as thin solutions of a two-variable elliptic equation.

In the simplest cotangent-bundle model, Floer homology will recover the homology of the original position space. Understanding that result begins here, with the ordinary geometry of the zero section and the graph of a derivative. The infinite-dimensional machinery will be more complicated, but its basic generators have already appeared in first-year calculus.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(T^*Q\), use local canonical coordinates \((q_i,p_i)\), \(\omega=\sum_i dq_i\wedge dp_i\), and \(\lambda=-\sum_i p_i dq_i\), so \(d\lambda=\omega\). If \(\alpha=\sum_i a_i(q)dq_i\), the graph of \(\alpha\) pulls back \(\omega\) to \(-d\alpha\). Therefore \(\Gamma_\alpha\) is Lagrangian iff \(d\alpha=0\), and it is exact when \(\alpha=df\) because \(\lambda|_{\Gamma_{df}}=-df\). The zero section is \(\Gamma_0\).

At \(q\in Q\), \(\Gamma_{df}\cap\Gamma_0\) means \(df_q=0\). Linearizing \(df\) shows that transversality at the intersection is equivalent to nondegeneracy of \(\mathrm{Hess}_q f\). On \(S^1=\mathbb R/\mathbb Z\), \(f(q)=\cos(2\pi q)\) has exactly two such intersections. The graph \(p=c\neq0\) is a closed nonexact Lagrangian; \(\int_{S^1}c\,dq=c\neq0\).

For a compatible \(J\)-holomorphic disk \(u:(D,\partial D)\to(M,L)\) with \(\omega=d\lambda\) and \(\lambda|_L=df\), \(E(u)=\int_Du^*\omega=\int_{\partial D}u^*df=0\), hence \(u\) is constant. No compactness at infinity is implied.

### Exercises with answers

1. **Lagrangian graph.** Why is \(\Gamma_{df}\) Lagrangian? **Answer:** \(d(df)=0\).
2. **Intersections.** How many transverse intersections do the zero section and \(\Gamma_{d\cos(2\pi q)}\) have? **Answer:** two, at \(q=0\) and \(q=1/2\).
3. **Closed versus exact.** Why is \(c\,dq\) on the circle not exact for \(c\neq0\)? **Answer:** it has nonzero integral around the circle.
4. **No disks.** Why is every compatible holomorphic disk with boundary on a compact exact Lagrangian in an exact symplectic manifold constant? **Answer:** Stokes and exactness give zero area, hence zero energy.

### Sources and further reading

- Andreas Floer, [Morse Theory for Lagrangian Intersections](https://doi.org/10.4310/JDG/1214442477), *Journal of Differential Geometry* 28 (1988), 513–547.
- Michael Hutchings, [Floer Theory course](https://math.berkeley.edu/~hutching/teach/277-2008/index.html), intersection and holomorphic-curve prerequisites.
- [Cotangent bundle](https://en.wikipedia.org/wiki/Cotangent_bundle); [Lagrangian submanifold](https://en.wikipedia.org/wiki/Lagrangian_submanifold).
