# 013300 - Curvature, Holonomy, and Chern Numbers

**Track:** Topology and Geometry. **Background:** bundles, connections, differential forms and Stokes' theorem. **Question:** how can local curvature reveal a global integer associated with a complex line bundle?

<!-- BEGIN SPOKEN LECTURE -->

# Curvature, Holonomy, and Chern Numbers

Two different paths can carry a vector from one point to another. If we use a connection to parallel transport the vector along each path, the final vectors need not agree. Going forward on one path and returning on the other gives a loop, and the discrepancy becomes a transformation of the original fiber. We call that transformation holonomy.

For a complex line bundle with a unitary connection, holonomy is multiplication by a complex number of absolute value one: a phase. For higher-rank bundles it can be a matrix. Curvature describes the first-order departure from path independence around very small loops. But curvature also has a global role. Properly normalized, its integral over a closed oriented surface can be an integer determined by the topology of the bundle.

## Curvature as failure to commute

A connection lets us differentiate a section along vector fields X and Y. We may first differentiate in X and then Y, or do them in the opposite order. Even on a curved manifold, the fields themselves may fail to commute, so we must subtract the covariant derivative in the direction of their Lie bracket as well. What remains is the curvature operator.

The result acts linearly on each fiber. In a local frame with connection d plus a matrix-valued one-form A, the curvature is the matrix-valued two-form d A plus A wedge A. The second term matters because matrices need not commute. In a complex line bundle, the matrices are just scalar one-by-one matrices and A wedge A vanishes, leaving curvature d A.

If we change the local frame, the connection form acquires an extra derivative term. The curvature instead transforms by conjugation, so its geometric content is well defined. In a line bundle conjugation does nothing, and the curvature is a globally defined imaginary-valued two-form. This is why curvature, unlike the local connection potential, can be integrated globally without choosing one frame for the whole surface.

## A rectangle measures local curvature

Recall the connection d plus i times x d y on the trivial complex line over the plane. Its curvature is i times d x wedge d y. Transport around a counterclockwise rectangle of area S multiplies the initial vector by exponential of negative i times S. For a very small rectangle, expand the exponential: the leading deviation from one is negative i times S. Curvature is the coefficient that measures this small-loop effect.

For a line bundle, Stokes' theorem makes the relationship exact whenever a loop bounds a region on which we have a single smooth frame: the holonomy phase is exponential of minus the curvature integral over that region. For a higher-rank noncommuting connection, the relation is subtler. Holonomy involves path ordering, and one cannot replace it in general by the ordinary exponential of a curvature integral without further conditions.

We should also remember the global caveat. A flat connection has zero infinitesimal curvature but may retain nontrivial holonomy around a loop that cannot be contracted to a point. The circle with a constant angular connection provided an explicit example. Local curvature and global holonomy are related but not interchangeable invariants.

## From phase to integer

Now let L be a Hermitian complex line bundle over a closed oriented surface. Choose a unitary connection. In each unitary frame its curvature is an imaginary-valued two-form, and these local expressions agree on overlaps. Multiply the curvature by the imaginary unit and divide by two pi. With the sign convention used in this lecture, that gives a real closed two-form representing the first Chern class of L in de Rham cohomology.

The first Chern number is the integral of that real two-form over the oriented surface. The remarkable claim is that the answer is always an integer. Changing the unitary connection can change the curvature point by point, but not the integer. We have moved from an arbitrary differential-geometric choice, the connection, to a topological invariant of the line bundle.

Why an integer? Cover the sphere by a northern and a southern disk, with an overlap around the equator. Choose a unitary frame in each disk. On the overlap the two frames differ by a circle-valued transition function. As we go around the equator, that transition phase must make an integer number of full turns. It has a winding number.

The two local connection potentials differ by the derivative of the transition phase. Integrating curvature over the two hemispheres and applying Stokes turns the surface integral into a difference of line integrals on their common equator. That difference is exactly the phase winding, after the two-pi normalization and sign convention are accounted for. Integrality is not a numerical coincidence. It follows from the single-valuedness of the transition function on a full loop.

## One explicit unit of Chern number

Use spherical coordinates with colatitude theta measured from the north pole and longitude phi. Choose a connection on the northern disk with an imaginary-valued potential proportional to minus one minus cosine theta, times d phi. On the southern disk use a potential proportional to one plus cosine theta, times d phi. The coefficients are arranged so that each potential is smooth at its own pole despite the coordinate singularity of longitude.

Both produce the same curvature, equal to negative one-half times the imaginary unit times sine theta d theta wedge d phi. After multiplying by i and dividing by two pi, the Chern form becomes one over four pi times the ordinary area element on the unit sphere. That normalized area integrates to one. The local frames are related around the equator by a phase that winds once. These are two calculations of the same integer: one from curvature, one from the transition function.

The signs depend on orientations, on whether we discuss a bundle or its dual, and on the connection convention. Reversing the orientation of the sphere reverses the integral. Taking the dual line bundle reverses the first Chern class. The important invariant statement is that a globally defined integer results once all conventions are fixed consistently.

## What a nonzero number proves

A trivial complex line bundle has a global nowhere-zero frame. In such a frame its connection is represented by one globally defined imaginary-valued one-form A, and its curvature is d A. On a closed surface, Stokes says the integral of d A is zero. Therefore a nonzero first Chern number obstructs triviality. We cannot choose a global frame for that bundle.

The converse needs care. On a closed oriented surface, complex line bundles are classified by their integral first Chern class, so zero first Chern number means the bundle is trivial there. In more general settings, a single number obtained by pairing with one surface may not detect every bundle class. For higher-rank bundles and higher-dimensional bases, other characteristic classes and pairings are needed. Even a trivial bundle can still carry a non-flat connection, so Chern number zero does not mean curvature zero everywhere.

The same language extends to matrix-valued curvature. Certain invariant polynomial expressions in the curvature produce closed forms whose cohomology classes are independent of the chosen connection. This is the idea of Chern-Weil theory. The first Chern class of a complex line bundle is the most accessible example because the trace and matrix commutator issues collapse to ordinary differentiation.

We began with the failure of two paths to transport a vector identically. We ended with an integer that cannot change under a smooth adjustment of the connection. Holonomy measures transport around loops. Curvature measures its local infinitesimal behavior. The first Chern number assembles curvature over a closed surface and records global twisting. This is a concrete entry point into the geometry behind gauge theory, where local potentials, observable transport and topological sectors have to be distinguished carefully.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(\nabla=d+A\) in a frame, \(F_\nabla=dA+A\wedge A\), and with \(e'=eg\), \(F'=g^{-1}Fg\). On a Hermitian complex line bundle with a unitary connection, \(F\in i\Omega^2(M;\mathbb R)\), \(F=dA\) locally and the normalized real Chern form is
\[c_1(\nabla)=\frac{i}{2\pi}F.\]
With this convention its class is the image of \(c_1(L)\in H^2(M;\mathbb Z)\) in real de Rham cohomology. On a closed oriented surface \(\Sigma\),
\[\langle c_1(L),[\Sigma]\rangle=\frac{i}{2\pi}\int_\Sigma F\in\mathbb Z.\]

**Unit-charge sphere calculation.** Use \(0\le\theta\le\pi\), \(0\le\phi<2\pi\) and the standard orientation \(\sin\theta\,d\theta\wedge d\phi\). On northern/southern patches take
\[A_N=-\frac{i}{2}(1-\cos\theta)\,d\phi,\qquad A_S=\frac{i}{2}(1+\cos\theta)\,d\phi.\]
Both yield \(F=-\frac i2\sin\theta\,d\theta\wedge d\phi\). On the equatorial overlap, \(A_S-A_N=i\,d\phi\), corresponding to \(g=e^{i\phi}\) for \(e_S=e_Ng\). Thus
\[\frac{i}{2\pi}\int_{S^2}F=\frac1{4\pi}\int_0^{2\pi}\!\int_0^\pi\sin\theta\,d\theta\,d\phi=1.\]
For \(U(1)\) holonomy in a local frame, \(\operatorname{Hol}(\partial S)=\exp(-\int_S F)\) when the loop and a spanning surface lie in a single trivializing patch and orientations agree. For general higher-rank connections, a path-ordered exponential is needed.

### Check your understanding

1. Can a line bundle with \(c_1=1\) over \(S^2\) have a global nonvanishing frame? **No:** that would make it trivial and give Chern number zero.
2. If a connection on a trivial line bundle has nonzero curvature, must its Chern number over a closed surface be nonzero? **No:** global curvature is exact and integrates to zero.
3. Does flatness force all global loop holonomies to be identity? **No:** noncontractible loops can support nontrivial flat holonomy.

### Reading and sources

- John Baez and Javier P. Muniain, [Gauge Fields, Knots and Gravity](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/PhilPhysics/Baez%2BMuniain1994GaugeFieldsKnots%2BGravity.pdf), curvature and holonomy.
- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), line bundles and characteristic classes.
- E. Meinrenken, [Sign Conventions](https://www.math.toronto.edu/mein/teaching/notes/signs.pdf), normalized first Chern form and sign comparisons.
- Overview: [First Chern class](https://en.wikipedia.org/wiki/Chern_class#First_Chern_class), [Holonomy](https://en.wikipedia.org/wiki/Holonomy).
