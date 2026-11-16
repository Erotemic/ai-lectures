# 059000 — Stable Maps and Gromov–Witten Invariants: Counting Curves with Multiplicity

**Track:** Abstract Algebra. **Background:** projective varieties, moduli spaces, divisors, and virtual fundamental classes. **Central question:** how do we count curves when families degenerate, components split, and automorphisms appear?

<!-- BEGIN SPOKEN LECTURE -->

# The line that everybody can count

Two distinct points in the projective plane determine exactly one projective line. This is the kind of enumerative geometry problem that seems almost too easy to require a sophisticated theory. But ask for more complicated curves meeting several constraints. Some curves become singular, some break into components, and others move in families of larger dimension than we expected. At the boundary of a family, a sequence of smooth curves can converge to a nodal curve.

How can a count remain consistent when the objects we are counting change their appearance? One answer is to enlarge the space of allowable curves so that limits are included. Another is to use intersection theory, and in harder situations a virtual fundamental class, to assign a count with the proper multiplicities. Gromov–Witten theory combines these moves.

We will keep returning to the unique line through two points. It is a small example where we can check every dimension and see what the general apparatus is trying to preserve.

# A curve and a map are not the same thing

In a moduli problem of maps, an object consists of a source curve, marked points on that curve, and a map into a target variety. Different parametrizations related by an isomorphism of marked source curves count as the same object.

Why include the map rather than only its image? The image forgets important information. A parametrization can cover the same target curve more than once. A map can contract an entire component to a point. Multiple covers and contracted components have different deformation behavior, and the invariant must be able to see that difference.

For a stable map, the source is allowed to be a nodal curve. Stability requires its automorphism group, respecting the map and all marked points, to be finite. In genus zero this has a particularly clear consequence: a rational component collapsed to a point must have at least three special points, where special means marked points or nodal attachments.

A nonconstant component can be stable with fewer markings because the map itself may eliminate continuous automorphisms. The condition is not simply that every rational component must carry three marks.

# Why we compactify

Consider a family of degree-two maps into the plane. Its image may be a smooth conic at first. In a limiting family the conic may split into two lines. If our parameter space contains only smooth conics, this limit is missing and intersection numbers may change when constraints move.

The moduli space of stable maps contains appropriately nodal limits. For a projective target, fixed genus, marked-point count, and curve class, the moduli stack of stable maps is proper under the standard hypotheses. Properness is the formal condition that supports specialization arguments and the construction of numerical intersection invariants.

There are caveats. The space is generally a stack rather than an ordinary space, because maps may have finite automorphisms. It may also be singular or have components of unexpected dimension. Compactness alone does not fix the dimension problem. That is where obstruction theory enters.

# Expected dimension

Suppose our target is the complex projective plane. A degree-one map has a line as its image, and the family of all lines is two-dimensional over the complex numbers. If we mark two source points, their images give two additional dimensions. The resulting space of degree-one stable maps with two marked points has expected complex dimension four.

Now ask the first marked point to hit one specified general point in the target. A point has complex codimension two in the projective plane. Imposing this condition removes two expected dimensions. Asking the second marked point to hit another general point removes another two. Four dimensions minus two minus two leaves zero.

The unique line through those two points gives exactly one map up to the source isomorphism, with the marks determined by the preimages. This is a case in which the invariant equals the familiar answer: one.

With higher degree, the expected dimension and the incidence constraints can still be calculated, but the actual moduli geometry is harder. A naive count of smooth curves might miss degenerations or fail to account for multiplicity.

# Evaluation maps and intersection products

Every marked point gives an evaluation map. It sends a stable map to the target point where the marked source point lands. If we want a map to pass through a fixed point or meet a divisor, we pull back the corresponding cohomology class along its evaluation map.

We then intersect these classes with the moduli space's virtual fundamental class. When the result has degree zero and the moduli space is proper, its degree is a number. That number is the Gromov–Witten invariant associated with the selected genus, curve class, and insertions.

The virtual dimension formula predicts which combinations can produce a number. If the insertions have too little codimension, the intersection does not naturally give a zero-dimensional count. If they have too much, the corresponding degree can vanish for dimensional reasons.

# What virtual means here

A smooth target does not guarantee smoothness of the stable-map moduli space. Deformations of the map are constrained by the geometry of the source curve and the target. Some first-order deformations cannot be extended. An obstruction theory records that failure and gives a virtual class of the expected dimension.

There is a particular danger in translating the result into words. A Gromov–Witten invariant is not always literally the number of honest smooth curves satisfying our incidence conditions. Multiple covers, nodal maps, stack automorphisms, and virtual multiplicities can contribute. Interpreting the invariant as an integer-valued enumerative count requires additional hypotheses.

In the unique-line example, these complications do not spoil the answer. In general they are part of the reason the theory works.

# A count that survives degeneration

The construction has a useful structure. Proper moduli include the limits. Markings and evaluation maps specify geometric conditions. Deformation theory supplies the expected dimension even when the actual space is too large. Intersection with the virtual class defines an invariant subject to the appropriate hypotheses.

The line through two points is still one line. But now the same language can describe a problem involving intersecting curves, degenerations, or an entire family of maps in which no ordinary isolated-point count was available. The sophisticated count is valuable precisely when a simple count is no longer stable under deformation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth projective target X of complex dimension r and curve class beta, the standard expected complex dimension of the moduli stack of n-pointed genus-g stable maps is
\[
\operatorname{vdim}_{\mathbb C}\overline M_{g,n}(X,\beta)
=(1-g)(r-3)+\int_\beta c_1(TX)+n.
\]
Evaluation maps `ev_i: Mbar_{g,n}(X,beta)->X` give classes `prod_i ev_i^*(gamma_i)`; when their combined complex codimension equals vdim and the moduli is proper, integrating them against `[Mbar]^{vir}` yields a numerical Gromov–Witten invariant. Additional psi-class insertions lead to descendant invariants.

**Degree-one line count.** For X=P^2, `c1(TP^2)=3H`; a degree-d map has `int_beta c1=3d`. At `g=0, d=1, n=2`, `vdim=(-1)+3+2=4`. Two point classes contribute codimension `2+2=4`, so
\[
\int_{[\overline M_{0,2}(\mathbf P^2,1)]^{\mathrm{vir}}}
\operatorname{ev}_1^*([p])\operatorname{ev}_2^*([q])=1,
\]
for two distinct general points p,q. A degree-one map is an isomorphism onto its image line, so the marks and map are unique up to isomorphism. The line count is one rather than a stack-weighted fractional contribution in this case.

Stability for genus-zero contracted irreducible components requires at least three special points. Stability of a *nonconstant* component depends on finiteness of automorphisms preserving the map. In moduli with multiple covers and automorphisms, a GW invariant is not automatically a literal number of embedded smooth curves.

### Exercises with answers

1. Compute `vdim_C Mbar_{0,3}(P^2,1)`. **Answer:** `-1+3+3=5`.
2. What is the codimension of the condition that an evaluation point lies on a line in P^2? **Answer:** complex codimension one.
3. Why is an unmarked, degree-zero genus-zero map unstable? **Answer:** its constant source P^1 has an infinite automorphism group.
4. Do two generic point constraints determine a unique degree-two plane curve? **Answer:** no; the dimension count leaves a positive-dimensional family.

### Reading and source notes

- [Kontsevich and Manin, Gromov–Witten Classes, Quantum Cohomology, and Enumerative Geometry](https://arxiv.org/abs/hep-th/9402147), marked stable maps and enumerative invariants.
- [Behrend and Fantechi, The Intrinsic Normal Cone](https://arxiv.org/abs/alg-geom/9601010), obstruction theories and virtual fundamental classes.
- [The Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), intersection products and Gysin constructions.
