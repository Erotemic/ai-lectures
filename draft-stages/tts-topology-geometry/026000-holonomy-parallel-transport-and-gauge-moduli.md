# 026000 — Holonomy and Gauge Moduli: Transport Around a Loop

**Track:** Topology and Geometry. **Background:** connections on bundles, differential forms, fundamental groups. **Central question:** how can transport around closed loops reveal geometry and topology invisible to local curvature measurements?

<!-- BEGIN SPOKEN LECTURE -->

# Carry a vector, return with a change

Imagine moving a vector around a closed path on a curved surface. We try to keep the vector parallel as we move. After completing the loop, the vector can point in a different direction from where it began. That mismatch is holonomy: the transformation produced by parallel transport around a closed path.

Holonomy is more general than rotating tangent vectors on a surface. A connection on a vector bundle tells us how to compare fibers at nearby points. Following that instruction along a path produces a linear map from the initial fiber to the final fiber. For a closed loop, both fibers are the same, so we obtain a linear automorphism.

The collection of transformations from all loops based at one point forms a holonomy group. It records how the connection mixes the fiber as we move through the base space.

## Local formulas for transport

Choose a local frame. In that frame a connection can be written using a matrix-valued one-form A. Along a path gamma, parallel transport is governed by an ordinary differential equation. The transport matrix changes at a rate determined by minus A evaluated on the path's velocity, multiplied by the current transport matrix.

For one-dimensional complex fibers, the matrices are scalars and commute. Transport around a closed loop is an exponential of minus the integral of A around the loop. For higher-rank bundles, matrices at different positions may fail to commute, and the order in which the path encounters them matters. The solution is a path-ordered exponential.

The curvature of a connection is a two-form built from d A plus A wedge A. It measures, to first order, the failure of parallel transport around a tiny loop to be the identity. This makes curvature a local measure of holonomy.

But local curvature does not tell the whole story.

## A flat connection with nontrivial holonomy

Consider the circle. Choose an angle coordinate phi, understood modulo two pi, and a complex line bundle with a connection whose local one-form is i times theta d phi, for a real constant theta. Its curvature is zero, because there are no nonzero two-forms on a one-dimensional base. The connection is flat.

Now transport once around the circle. The resulting multiplication is the complex phase exp of minus two pi i theta. If theta is not an integer, the phase need not equal one. We have nontrivial holonomy even though the curvature vanishes everywhere.

There is no contradiction. Curvature describes what happens on small loops that contract to a point. A loop winding around the circle cannot be contracted there. It can detect global information that no local curvature measurement sees.

If theta changes by an integer, the phase remains the same. This reflects a change of gauge: different local descriptions can represent the same global connection. The gauge-invariant information is not the raw coefficient theta, but its value modulo the appropriate equivalence.

## Gauge transformations change descriptions

A choice of local frame is a gauge choice. Changing frames alters the matrix one-form A. It also changes the coordinates used to describe parallel transport. For a closed loop, the holonomy matrix transforms by conjugation at the base point. Its trace, characteristic polynomial, and conjugacy class therefore do not depend on the chosen frame.

For a unitary rank-one bundle, conjugation does nothing, so the phase itself is gauge invariant. In a higher-rank bundle, the individual entries of a holonomy matrix are not gauge invariants, but its conjugacy class is.

One sometimes encounters a Wilson loop, the trace of the holonomy around a closed path in a chosen representation. Wilson loops are natural gauge-invariant observables because conjugation leaves traces unchanged.

The transformation law is easy to misunderstand. A gauge transformation is not an operation that physically changes the connection's parallel transport in an arbitrary way. It changes its description using a different frame. Two gauge-related connections represent the same geometric transport structure.

## Flat connections and the fundamental group

For a flat connection, parallel transport around homotopic loops agrees, provided endpoints are fixed. Holonomy therefore descends to a group homomorphism from the fundamental group of the base into the structure group, up to conjugation.

On the circle, the fundamental group is the integers. A representation of the integers is specified by the image of one generator, exactly the holonomy around one full winding. This is why a single phase captures our flat line-bundle example.

On a simply connected base, flat connections have trivial holonomy around every loop. On a multiply connected base, different holonomy representations can exist even with zero curvature. Describing all flat connections may require allowing different principal bundles, not just connections in one fixed global trivialization.

This leads to a moduli problem. We want to classify connections modulo gauge transformations. The quotient is rarely a plain smooth manifold everywhere. Some connections have nontrivial stabilizers, and nearby deformations can behave differently at reducible and irreducible connections. The earlier lecture on quotient stacks provides exactly the conceptual warning needed here: an equivalence class can conceal automorphisms.

## Two complementary invariants

Curvature and holonomy answer related but distinct questions. Curvature is infinitesimal and local. Holonomy accumulates transport along entire loops and can detect global topology. When curvature is zero, holonomy becomes homotopy-invariant; when curvature is nonzero, it generally depends on the detailed path, not only its homotopy class.

Connections turn geometry into a rule for comparison. Transport around loops tests that rule. Gauge theory studies the resulting geometric structures without confusing them with arbitrary choices of coordinates. The circle example shows why all three levels matter: local formulas, global loops, and equivalence under changes of frame.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a connection one-form `A` in a local frame along a smooth path gamma, parallel transport U satisfies
\[
\frac{dU}{dt}=-A_{\gamma(t)}(\dot\gamma(t))U(t),\qquad U(0)=I.
\]
The curvature is `F_A=dA+A wedge A`. Under gauge change `g`, `A -> g^{-1} A g+g^{-1}dg`; for loops based at x, holonomy changes by conjugation by `g(x)` (depending on the chosen frame convention).

On the trivial complex line bundle over `S^1=R/(2pi Z)`, take `A=i theta dphi`. Then `F_A=0`, but holonomy for one positive winding is `exp(-2pi i theta)`. Gauge `g(phi)=exp(i n phi)` is single-valued for `n in Z` and changes theta by an integer under the indicated transformation convention. The holonomy is invariant.

For flat connections, the holonomy of based loops factors through `pi_1(M,x)` and gives a representation `rho:pi_1(M,x)->G`, up to conjugation under basepoint-frame changes. For curved connections, holonomy is not generally invariant under ordinary homotopy of loops.

### Exercises with answers

1. What is the curvature of `A=i theta dphi` on `S^1`? **Answer:** zero, since the base has no nonzero two-forms.
2. What is its holonomy after two positive windings? **Answer:** `exp(-4pi i theta)`.
3. Why is a trace of holonomy gauge invariant? **Answer:** holonomy changes by conjugation at the base point, and trace is conjugation invariant.
4. If the base is simply connected and the connection flat, what is the holonomy of every loop? **Answer:** the identity, assuming the usual connectedness and flat transport hypotheses.

### Reading and source notes

- [Nakahara, Geometry, Topology and Physics](https://doi.org/10.1201/9781315275826), connections, curvature and holonomy.
- [Milnor, Morse Theory (Princeton University Press)](https://press.princeton.edu/books/paperback/9780691080086/morse-theory), topology background for the geometry track.
- [Freed and Uhlenbeck, Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9701-2), gauge classes and connections.
