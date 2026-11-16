# 056000 — Virtual Fundamental Classes: Counting with Obstructions

**Track:** Abstract Algebra. **Background:** tangent complexes, local complete intersections, vector bundles, Chow groups, and moduli problems. **Central question:** how can geometry define a meaningful expected-dimensional count when a solution space is larger or more singular than expected?

<!-- BEGIN SPOKEN LECTURE -->

# When equations fail to cut down dimension

Suppose we want to count the common zeros of several equations. In a favorable problem, each independent equation removes one dimension. We get isolated solutions, and we may assign multiplicities and sum them. But the equations might become dependent. Their common zero set might contain curves, or even an entire surface, where isolated points were expected.

One response is to perturb the equations and count the solutions that remain. In analysis and differential topology, transversality often makes this strategy effective. In algebraic geometry, perturbing may change the structure we want to preserve, or the moduli problem may be too global to admit a suitable perturbation.

Virtual fundamental classes offer another route. Instead of insisting that the ordinary zero set have the expected dimension, we retain a controlled model of the equations and their obstructions. This model can produce an intersection class in the expected degree, even when the underlying moduli space has the wrong dimension.

# A section of a vector bundle

Begin with the simplest geometric situation. Let X be a smooth space of dimension n and let E be a vector bundle of rank r. A section of E chooses one vector in each fiber. Its zero locus is the set of points where the chosen vector vanishes.

If the section meets the zero section transversely, the zero locus has dimension n minus r. This is the expected dimension. If the section is not transverse, the actual zero locus can be larger. But the original presentation of the zero locus as the zeros of a section still predicts the dimension n minus r.

For a bundle section, a canonical two-term obstruction theory can be built from the tangent bundle of X and the restriction of E to the zero locus. The derivative of the section maps tangent directions into the bundle's fibers. The failure of that derivative to be surjective is exactly the failure of transversality. A virtual class uses this two-term structure to produce an expected-dimensional cycle.

The technical construction goes through the intrinsic normal cone and an intersection with the zero section. These terms describe a precise operation in intersection theory, not an arbitrary correction to the number of solutions.

# A zero section that vanishes everywhere

Take the projective line as X and the trivial line bundle on it. Choose the section that is identically zero. The actual zero locus is the entire projective line, a one-dimensional space. But the bundle has rank one, so the expected dimension is zero.

What should its virtual zero-dimensional class be? For a section of a vector bundle over a smooth complete base, the virtual zero class is the top Chern class of the bundle capped with the fundamental class of the base. The top Chern class of a trivial line bundle is zero. So the virtual class is zero.

This is not claiming that the zero locus has no points. It has infinitely many. Nor are we declaring every point to count with weight zero by fiat. We are calculating an intersection class associated with the specified equation system. The trivial line bundle's Euler or top Chern class vanishes, and the virtual count reflects that fact.

If instead we take a generic section of the line bundle of degree one on the projective line, it has a single zero counted with multiplicity one. The virtual class has degree one. So the bundle and its class, not just the set-theoretic size of the zero locus, are essential to the count.

# The role of a perfect obstruction theory

For a general moduli space, we may not have a global smooth ambient space and vector bundle. A perfect obstruction theory is a replacement. It is, roughly, a two-term complex of vector bundles mapping to the cotangent complex of the moduli space, with compatibility conditions on its low-degree cohomology.

Those conditions are strong. They ensure that the obstruction theory faithfully captures infinitesimal deformations and obstructions up to the required degree. Its virtual rank determines a virtual dimension. Under the standard constructions, the intrinsic normal cone can then be intersected in a vector-bundle stack to produce a class of that dimension.

Different obstruction theories on the same underlying space may yield different virtual classes. The result is an invariant of the moduli problem together with the specified obstruction-theoretic structure, not a number determined solely by the set of geometric points.

# The connection to derived geometry

A quasi-smooth derived space has a cotangent complex of Tor-amplitude in degrees minus one and zero. Its derived structure naturally supplies the kind of two-term information needed for a perfect obstruction theory on its ordinary truncation. This makes derived geometry more than a vocabulary for hidden Tor groups. It explains why a virtual class belongs naturally to a moduli problem whose equations may have dependent constraints.

One should still distinguish constructing a virtual class from integrating it to obtain a numerical invariant. A numerical count generally needs properness, a class of the correct degree, and suitable choices of insertions or evaluation maps. If the moduli space is not proper, its virtual class may exist without there being a finite number to report.

# What the count is actually saying

Virtual classes appear in enumerative geometry, for instance when counting curves subject to incidence conditions. The ordinary moduli space of curves can have components of unexpected dimension, and some curves have automorphisms. A complete theory needs to account for both deformation-obstruction data and stack-theoretic symmetries.

The central idea is not that every geometric count should be replaced by a virtual one. In a transverse problem the virtual class agrees with the ordinary fundamental class of the solution locus. Its value appears when transversality fails but the underlying problem retains enough structure to define an expected-dimensional class.

The broader mathematical picture connects four ideas. Cotangent complexes reveal relations beyond ordinary differentials. Derived intersections retain excess Tor. Derived moduli connect tangent directions, automorphisms, and obstructions. Virtual fundamental classes convert that information into intersection-theoretic invariants, with carefully stated hypotheses about the moduli problem and the chosen obstruction theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For smooth X of pure dimension n and rank-r vector bundle E with section s and zero locus Z, the two-term perfect obstruction theory on Z can be represented dually by the map `T_X|_Z -> E|_Z`, with expected dimension `n-r`. If the section is regular, Z has the expected dimension and the virtual class equals its ordinary fundamental class. In general, the virtual zero-locus class pushed to X is
\[
i_*[Z]^{\mathrm{vir}}=c_r(E)\cap[X],
\]
where `i:Z->X`, provided the standard intersection-theoretic hypotheses hold.

**Example 1.** `X=P^1`, `E=O_{P^1}`, `s=0`: `Z=P^1` actually has dimension one; the virtual dimension is zero; `c_1(O)=0`, hence `[Z]^vir=0` in `A_0(P^1)`.

**Example 2.** `X=P^1`, `E=O_{P^1}(1)`, a generic nonzero section: the zero locus is one reduced point, and `deg(c_1(O(1)) cap [P^1])=1`.

For a perfect obstruction theory `phi:E^\bullet -> L_M` of amplitude `[-1,0]`, standard hypotheses require `h^0(phi)` to be an isomorphism and `h^{-1}(phi)` a surjection. The virtual dimension is the virtual rank of `(E^\bullet)^\vee` (equivalently, rank of degree-zero bundle minus degree-minus-one bundle under a compatible presentation). Having an obstruction **space** does not mean all deformation classes are obstructed. Nonproper moduli spaces need not yield numerical virtual counts merely from the existence of a class.

### Exercises with answers

1. What is the expected dimension of the zero locus of a section of rank-three E on smooth fivefold X? **Answer:** two.
2. Why is the zero section of a trivial line bundle not a transverse example? **Answer:** its derivative is zero, hence cannot surject onto a rank-one fiber.
3. Does the same underlying zero set uniquely determine a virtual class? **Answer:** no; the chosen obstruction theory and moduli presentation matter.
4. Which additional condition is generally needed to integrate a zero-dimensional virtual class to a finite count? **Answer:** properness, or an alternative construction that justifies the integral.

### Reading and source notes

- [Behrend and Fantechi, The Intrinsic Normal Cone](https://arxiv.org/abs/alg-geom/9601010), perfect obstruction theories and virtual fundamental classes.
- [The Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), Chern classes, Gysin maps and intersection products.
- [Toën, Higher and Derived Stacks: A Global Overview](https://arxiv.org/abs/math/0604504), derived enhancement and virtual intersection theory.
