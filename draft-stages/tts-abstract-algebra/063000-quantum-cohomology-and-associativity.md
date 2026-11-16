# 063000 — Quantum Cohomology: When Curves Change Multiplication

**Track:** Abstract Algebra. **Background:** intersection theory, moduli of stable maps, Poincaré duality and Gromov–Witten invariants. **Central question:** how can counting rational curves deform ordinary cohomology into a new ring?

<!-- BEGIN SPOKEN LECTURE -->

# A multiplication rule that remembers curves

Ordinary cohomology packages geometric intersections into a multiplication. If two classes represent conditions on a space, their cup product records where those conditions meet. For the complex projective line, there is a degree-two class representing a point. The square of that class vanishes: there is no nonzero cohomology in degree four on a space of real dimension two.

Quantum cohomology changes exactly that multiplication rule. On the projective line the point class, call it H, satisfies H times H equals q rather than zero. The symbol q is a formal record of the degree of a rational curve. The new product contains not only the intersection behavior of static subspaces, but also the contribution of maps from a sphere into the target.

It is worth asking why a count of curves should define an associative multiplication. Ordinary cup products are associative for topological reasons. A curve-counting product could easily fail that basic algebraic law. The answer comes from looking at the moduli space of four marked points on a sphere and how the sphere degenerates into two components.

# Three constraints define a structure constant

Fix a smooth projective target. Consider genus-zero stable maps with three marked points. At each mark, we can demand that its image lie in a cycle representing a cohomology class. If the dimensions match the virtual dimension of the moduli space, the intersection of these conditions gives a number: a three-point Gromov–Witten invariant.

To build a product, pair this three-point count with the Poincaré duality metric. Given two input classes, we define their quantum product by requiring its pairing with a third class to equal the generating series of these invariants, summed over curve degrees and weighted by corresponding formal variables. Degree zero recovers the usual cup product. Positive degrees are the correction terms.

The adjective virtual matters. Stable-map moduli spaces may be singular, have components of unexpected dimension, or contain maps with automorphisms. The intersection number is taken against a virtual fundamental class, not obtained by naively enumerating all parameterized maps. Curves may contribute multiplicities or rational weights. The resulting algebra is a mathematically organized curve count, not always an elementary cardinality.

# The projective line from start to finish

On the projective line there are just two ordinary cohomology generators: the identity and the point class H. In classical cohomology, H squared is zero. To determine its quantum square, pair it with H again. The relevant invariant asks for degree-one maps from a marked sphere to the projective line that send three specified marks to three given points.

A degree-one map is a projective transformation. Once three distinct marked source points and three distinct target points are specified, there is exactly one such transformation, after accounting for the natural equivalence of marked maps. The corresponding genus-zero, degree-one invariant is one. Higher-degree terms cannot contribute to this particular multiplication because the grading rules them out.

Thus H multiplied by H equals q. The full small quantum cohomology ring becomes polynomials in H and q, with the relation H squared equals q, over the chosen coefficient or Novikov ring. Set q to zero and the classical relation returns. Set q to a nonzero value and the algebra changes: at generic q the polynomial H squared minus q factors into two distinct roots over a suitable field extension.

This is a deformation of a ring, not of the underlying topological space. The target is still the projective line. What has changed is the multiplication used to organize its intersection data.

# Why four marked points guarantee associativity

Consider now four cohomology classes and a sphere with four marked points. Different ways of grouping four factors correspond to different boundary degenerations: the sphere can break into two spheres with the first two marks on one component, or with the first and third marks together. Both boundary configurations appear as special points in the moduli space of four-marked genus-zero curves.

These boundary points are rationally equivalent. Pull that equivalence back through the stable-map construction, and use the splitting axiom, which says that a stable map on a nodal curve is built by gluing maps on the two components and pairing their common evaluation class. The two degenerations produce the two orders of multiplication. Their equality is the WDVV equation.

The equality of these gluing expressions makes the quantum product associative. In other words, associativity is not inserted as a hope; it is a theorem forced by the geometry of the boundary of a moduli space.

The WDVV equation also gives nontrivial relations among curve counts. Knowing a small number of invariants and the classical intersection pairing can sometimes determine many others recursively. Quantum cohomology becomes a computational tool rather than only a new definition.

# Formal parameters are not optional decoration

The q variable keeps track of curve degree and preserves a grading. For the projective line, H has cohomological degree two and q has degree four. That makes the equation H squared equals q homogeneous. For targets with several independent effective curve classes, one needs several degree variables or a Novikov completion to manage possibly infinite sums.

There is also a distinction between small and big quantum cohomology. Small quantum cohomology deforms the product using the basic three-point theory. Big quantum cohomology lets an additional cohomology parameter enter, summing invariants with further insertions. The resulting product varies over a parameter space and gives a Frobenius-manifold structure under appropriate assumptions.

One must not treat a formal series automatically as a convergent numerical function. The algebraic product often makes sense formally even when analytic convergence has not been established. Confusing the two obscures the rigor of the construction.

# A ring that stores geometry in its structure constants

The projective line calculation is small enough to memorize but rich enough to contain the idea. Classical multiplication sees intersections of static cycles. Quantum multiplication adds the ways a rational curve can meet those cycles. The geometric degeneration of a four-marked sphere enforces associativity. Degree variables remember how much curve geometry was used.

This is why a single relation, H squared equals q, carries more information than a clever polynomial identity. It is the algebraic shadow of enumerative geometry, and it explains how the geometry of maps can modify the ring we use to study a space.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let X be smooth projective and work in a suitable Novikov ring. With a homogeneous cohomology basis `{phi_a}` and Poincaré inverse metric `g^{ab}`, define the genus-zero quantum product by
\[
(\alpha * \beta,\gamma)=\sum_{d\in H_2(X)} q^d\langle\alpha,\beta,\gamma\rangle_{0,3,d},\qquad
\alpha*\beta=\sum_{d,a,b}q^d\langle\alpha,\beta,\phi_a\rangle_{0,3,d}g^{ab}\phi_b.
\]
For `X=P^1`, take `1,H` with `int_{P1}H=1`, `H^2=0` classically and `deg H=2`. The only nonzero correction to `H*H` in the small ring is the degree-one invariant `\langle H,H,H\rangle_{0,3,1}=1`. Therefore
\[
QH^*(\mathbf P^1)=\mathbb Q[H,q]/(H^2-q),\qquad \deg(q)=4.
\]
The equation arises from the virtual count of degree-one stable maps, not a literal count of all parameterized rational functions. For general X, WDVV follows from equality of the two boundary divisors in `\overline M_{0,4}` and the splitting axiom. Unrestricted assertions of convergence or integrality are not part of the formal genus-zero construction.

### Exercises with answers

1. What happens to quantum cohomology of P1 when q is set to zero? **Answer:** the classical ring `Q[H]/(H^2)` is recovered.
2. Why does the multiplication `H*H=q` respect the quantum grading? **Answer:** both sides have degree four.
3. What geometric space supplies the associativity relation? **Answer:** the moduli space of four-marked genus-zero curves and its boundary splitting configurations.
4. Does the number of stable maps necessarily equal the number of embedded curves? **Answer:** no; automorphisms, multiple covers and virtual multiplicities can affect the invariant.

### Reading and source notes

- [Kontsevich and Manin, Gromov–Witten Classes, Quantum Cohomology, and Enumerative Geometry](https://arxiv.org/abs/hep-th/9402147), the genus-zero product and WDVV framework.
- [Cox and Katz, Mirror Symmetry and Algebraic Geometry](https://bookstore.ams.org/surv-68), examples of the small quantum product and enumerative constructions.
- [Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), intersection classes and Gysin maps.
