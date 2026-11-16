# 030200 - Spin and Spin-C Structures: Gluing Rotations and Spinors

**Track:** Topology and Geometry. **Background:** bundles, transition functions, characteristic classes, Clifford algebra. **Central question:** when can local spin representations be glued to a global bundle on a manifold?

<!-- BEGIN SPOKEN LECTURE -->

# Spin and Spin-C Structures: Gluing Rotations and Spinors

Suppose we have an oriented Riemannian manifold. At each point, its tangent space looks like ordinary Euclidean space, so we can construct the Clifford algebra and its spinor representations. The problem is that one tangent space has no preferred orientation-preserving orthonormal basis. As we move from chart to chart, the bases rotate. Do those rotations act consistently on the spinors we want to glue together?

This question is not solved by choosing enough charts. It is a global topological problem. The extra datum that solves it, when possible, is a spin structure. A related and more flexible datum is a spin-C structure.

## A familiar bundle-gluing problem

Recall how a vector bundle is assembled. Over each chart it looks like a product with a fixed vector space. On an overlap between two charts, we use a transition function to change one trivialization to the other. On a triple overlap, the three changes of trivialization must compose to the identity.

For an oriented orthonormal frame bundle, the transition functions take values in the rotation group. Our Clifford construction has another group, the spin group, which maps two-to-one onto rotations. A spin structure amounts to lifting the rotation transition functions to spin-valued transition functions that still obey the triple-overlap compatibility condition.

We can always choose lifts locally on sufficiently small overlaps. But the signs accumulated on triple overlaps may not cancel. If they do not, there is no globally consistent spinor bundle built by this recipe. The obstruction is encoded in the second Stiefel-Whitney class of the tangent bundle, a cohomology class with coefficients modulo two.

For an oriented manifold, a spin structure exists exactly when that obstruction vanishes. When one spin structure exists, the distinct choices form a family parameterized by first cohomology with modulo-two coefficients. Thus existence and uniqueness are different questions.

## A small example with two answers

The circle provides the simplest example. Its oriented tangent bundle is trivial, so it admits spin structures. But it has two different spin structures. In a convenient trivialization, a spinor carried once around the circle can return with the same sign or with the opposite sign.

These choices become periodic and antiperiodic boundary conditions for the simplest flat Dirac operator. They change its spectrum: periodic complex spinors permit a zero mode, while antiperiodic ones do not. The underlying circle and its Riemannian metric have not changed. The spin structure supplies genuine additional global data.

The two-sphere is spin as well. On an oriented surface, the relevant modulo-two obstruction is the Euler class reduced modulo two. The two-sphere has Euler characteristic two, so the obstruction vanishes. The projective plane over the complex numbers gives the contrasting four-dimensional example. Its second Stiefel-Whitney class is nonzero, and it is not spin.

## Repairing the sign obstruction with a circle phase

A spin-C structure enlarges the spin group by incorporating a unit complex phase. Formally, we take the spin group times the circle group, identifying the pair of negative signs with the pair of positive signs.

This construction permits a failure of the spin lifts to close up if a compensating phase repairs it. The combined transition functions form a spin-C bundle even when there is no spin bundle. Attached to this structure is a complex line bundle called its determinant line. Its first Chern class reduces modulo two to the second Stiefel-Whitney class of the tangent bundle.

That leads to a precise existence criterion. An oriented manifold has a spin-C structure if and only if its second Stiefel-Whitney class is the modulo-two reduction of an integral second cohomology class. The criterion is weaker than requiring the Stiefel-Whitney class to vanish. Not every oriented manifold in arbitrary dimension satisfies it, although every oriented smooth four-manifold does.

For the complex projective plane, the generator of second integral cohomology reduces to the nonzero modulo-two class. It supplies a compatible determinant line, even though it cannot make the manifold spin. The complex structure also supplies a canonical spin-C construction, with determinant line related to the complex tangent bundle.

## Why the determinant line matters

The spin-C structure does more than allow spinors to exist. A connection on its determinant line, combined with the Levi-Civita connection, defines a connection on the spinor bundle. Changing that line connection changes the Dirac operator. The determinant-line curvature then appears explicitly in the equation for the square of the Dirac operator.

In four dimensions, the complex spinor bundle splits into positive and negative chirality pieces. A spin-C Dirac operator maps positive spinors to negative spinors. This is the operator that later enters the Seiberg-Witten equations, paired with an equation involving the self-dual curvature of the determinant line.

We should distinguish three notions. An oriented manifold has frames whose transition functions lie in the rotation group. A spin structure lifts those transitions to the spin double cover. A spin-C structure allows an additional phase and carries a determinant line whose Chern class records the remaining modulo-two obstruction. Saying only that 'spinors are like vectors with two components' loses the global issue and also misses the line bundle on which gauge theory depends.

Our next job is to construct the resulting global spinor bundle and its differential operator. The local Clifford algebra will provide the multiplication, while the spin-C gluing and determinant connection make that construction independent of which charts and frames we use.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an oriented rank-\(n\) real bundle \(E\), a spin structure lifts its oriented orthonormal frame bundle \(P_{SO(n)}\) through \(\operatorname{Spin}(n)\to SO(n)\). Its obstruction is \(w_2(E)\in H^2(X;\mathbb Z/2)\). If \(w_2(E)=0\), spin structures form a torsor for \(H^1(X;\mathbb Z/2)\) (subject to the standard equivalence of lifts over the fixed frame bundle).

\[\operatorname{Spin}^c(n)=(\operatorname{Spin}(n)\times U(1))/\{(1,1),(-1,-1)\}.\]
The determinant character \([s,z]\mapsto z^2\) defines a line bundle \(L\) with \(c_1(L)\bmod 2=w_2(E)\). Existence is equivalent to \(W_3(E)=\beta(w_2(E))=0\), equivalently to the existence of an integral lift of \(w_2\). Spin-C structures, when they exist, form a torsor for \(H^2(X;\mathbb Z)\), with twisting by a line bundle \(Q\) changing \(L\) to \(L\otimes Q^{\otimes2}\).

For \(\mathbb{CP}^2\), \(w_2(T\mathbb{CP}^2)=h\bmod2\neq0\) and \(c_1(T^{1,0}\mathbb{CP}^2)=3h\) is an integral lift. For \(S^1\), the two spin structures correspond to the two elements of \(H^1(S^1;\mathbb Z/2)\). Do not conflate a spin-C determinant line with an arbitrary line: its parity must match \(w_2\).

### Exercises with answers

1. **Obstruction.** Which class obstructs a spin structure on an oriented bundle? **Answer:** \(w_2\).
2. **Two structures.** Why does an oriented circle have two spin structures? **Answer:** \(H^1(S^1;\mathbb Z/2)\cong\mathbb Z/2\).
3. **Spin-C.** Must the determinant line of a spin-C structure have trivial first Chern class? **Answer:** no; its reduction modulo two must equal \(w_2\).
4. **Example.** Why can \(\mathbb{CP}^2\) be spin-C but not spin? **Answer:** its nonzero \(w_2\) has an integral lift \(h\).

### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), discussion of spin and spin-C structures.
- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Overviews: [Spin structure](https://en.wikipedia.org/wiki/Spin_structure), [Spin-C structure](https://en.wikipedia.org/wiki/Spinc_structure), [Stiefel-Whitney class](https://en.wikipedia.org/wiki/Stiefel%E2%80%93Whitney_class).
