# 018000 — Characteristic Classes: Detecting the Twist in a Bundle

**Track:** Topology and Geometry. **Background:** vector bundles, cohomology, orientations, tangent bundles, Gauss–Bonnet. **Central question:** what invariants prove that a locally trivial bundle cannot be globally trivial?

<!-- BEGIN SPOKEN LECTURE -->

# Characteristic Classes: Detecting the Twist in a Bundle

A line bundle looks like an ordinary line when viewed near any one point. But the Möbius line bundle over a circle cannot be given a continuous global choice of a nonzero vector. Local frames exist and global frames do not. How can we measure this failure without relying on a picture of a twisted band?

Characteristic classes provide the answer. They assign cohomology classes to vector bundles. These classes are insensitive to the choice of local coordinates and respect maps between base spaces. They translate global twisting into algebraic invariants that can be calculated, compared, and sometimes used to prove a global construction impossible.

## A loop that reverses a vector

Start with a real line bundle over a circle. If you carry a nonzero vector once around the circle and return with its sign reversed, the line bundle is Möbius rather than trivial. The reversal is not a property of the local line at any point. It appears only after following the loop around the entire base.

The first Stiefel–Whitney class captures this obstruction. It lives in first cohomology with coefficients modulo two. For a real line bundle, it completely classifies the bundle when the base is a reasonable topological space, such as a paracompact space. On the circle there are exactly two classes: zero for the trivial line, and the nonzero class for the Möbius line.

The same first class for a higher-rank real vector bundle measures its orientability. It vanishes exactly when the bundle admits a consistent orientation, provided we work in the usual setting of real vector bundles over paracompact spaces. For the tangent bundle of a manifold, this gives an algebraic test for whether the manifold is orientable.

The class is a global invariant, but it has a very concrete source. Choose local frames on patches. On overlaps, transition matrices relate the frames. Their determinant signs record whether orientation flips. On triple overlaps these signs satisfy a consistency condition, so they determine a cohomology class. Changing the local frames changes the representative of the class, but not the class itself.

## The Euler class and zeros of vector fields

The first Stiefel–Whitney class detects orientation. What if a bundle is orientable but still has no nowhere-vanishing section? For an oriented real rank-n vector bundle, there is an Euler class in degree n integral cohomology. A nonzero Euler class obstructs a nowhere-zero section.

Take the tangent bundle of the two-sphere. A section of this bundle is a tangent vector field. If such a field never vanished, one could comb every tangent direction continuously without a bald spot. The hairy-ball theorem says this is impossible. The Euler class explains the obstruction in cohomological terms.

Evaluate the Euler class of the tangent bundle on the fundamental class of the sphere. The result is the Euler characteristic, which is two. The nonzero value proves that every continuous tangent vector field on the sphere must vanish somewhere. On a torus, the Euler characteristic is zero, and indeed a torus admits nowhere-zero tangent vector fields. These two facts are compatible, but the general converse from vanishing Euler class to existence of a nonzero section requires dimensional and other hypotheses; it is not an unrestricted equivalence for all bundles over all spaces.

This connects directly with Gauss–Bonnet. On an oriented Riemannian surface, differential geometry represents the Euler class of the tangent bundle using Gaussian curvature. Integrating that curvature representative recovers Euler characteristic. The curvature formula and the topological obstruction are two realizations of the same underlying class.

## Complex bundles have their own invariants

Complex vector bundles have Chern classes. The first Chern class of a complex line bundle belongs to integral second cohomology. For suitable spaces, it completely classifies complex line bundles. The class of a tensor product is the sum of the classes of the two factors. This is a particularly clean relationship between a geometric operation and cohomological addition.

The complex projective line is topologically a sphere. It carries a tautological complex line bundle whose first Chern class is a generator, up to the conventional choice of sign. In contrast, every complex line bundle over the ordinary circle is topologically trivial, because the circle has no nonzero second integral cohomology. Real line bundles over that circle can twist, but complex line bundles cannot twist in this particular way.

That contrast is a useful warning against treating all vector bundles alike. The coefficient field changes the relevant structure group and therefore the characteristic classes that can appear.

## Why curvature is not the whole story

A connection on a bundle allows us to compare vectors along paths, and its curvature measures the failure of infinitesimal parallel transport to commute. For complex vector bundles, certain differential forms built from curvature represent the real images of Chern classes in de Rham cohomology. For an oriented surface, a curvature form similarly represents the real Euler class.

But the topology of a bundle is not always visible in curvature forms alone. The Möbius real line bundle can carry a flat connection while its first Stiefel–Whitney class remains nonzero. Its twist is a two-valued holonomy effect, invisible to differential forms with real coefficients that detect only curvature. Torsion classes are another general source of information lost when integral cohomology is replaced by real cohomology.

Thus characteristic classes should not be reduced to a recipe for integrating curvature. Some classes have differential-form representatives after passing to real coefficients. Others are intrinsically integral or modulo-two phenomena and require different tools.

## Natural behavior and calculation

Characteristic classes are natural under pullback. If a bundle is pulled back along a continuous map, the characteristic classes of the new bundle are the pullbacks of the original classes. This lets us calculate complicated examples by comparing them with standard spaces and universal bundles.

They also obey product rules. Stiefel–Whitney classes assemble into a total class whose value on a direct sum is the product of the total classes of the summands. Chern classes satisfy an analogous Whitney-sum rule for complex bundles. For line bundles, these operations reduce to simpler additions and products, but in higher rank they give substantial constraints on how bundles may split.

An immediate application is obstruction by contradiction. Suppose we claim that a vector bundle admits a global frame. A globally framed bundle is trivial. A trivial bundle has no positive-degree characteristic classes. Therefore a computed nonzero class disproves the claim. The method avoids trying every possible frame; it rules all of them out at once.

## A language for global impossibility

The Möbius twist, the impossibility of combing a sphere, and the nontriviality of complex line bundles over a projective line are different examples of one theme. Local triviality does not imply global triviality. Characteristic classes describe the obstruction in cohomology, where it can be manipulated without fixing local coordinates.

Their power lies in turning geometric impossibility into an algebraic calculation. A nonzero class is not merely a name for a twist: it is a proof that certain global sections, frames, or decompositions cannot exist. And the relation to curvature shows how these topological obstructions can sometimes be measured by local differential geometry.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a real rank-r vector bundle \(E\to X\), Stiefel–Whitney classes are \(w_i(E)\in H^i(X;\mathbb Z/2)\). The **first class** detects orientability: \(w_1(E)=0\) iff E is orientable. For real line bundles over a paracompact base, \(w_1\) provides classification by \(H^1(X;\mathbb Z/2)\). The total class is \(w(E)=1+w_1(E)+\cdots+w_r(E)\), and \(w(E\oplus F)=w(E)\smile w(F)\).

For an oriented real rank-r bundle E, its Euler class is \(e(E)\in H^r(X;\mathbb Z)\). If E has a nowhere-zero section then \(e(E)=0\); the converse needs extra conditions. For an oriented closed surface M,
\[\langle e(TM),[M]\rangle=\chi(M),\qquad e(TM)_{\mathrm{dR}}=[K\,dA/(2\pi)].\]
For \(S^2\), the Euler number is 2, ruling out a nowhere-zero tangent field.

For complex rank-r E, \(c_i(E)\in H^{2i}(X;\mathbb Z)\). For complex line bundles L,M, \(c_1(L\otimes M)=c_1(L)+c_1(M)\). Over paracompact X, complex line bundles are classified by \(H^2(X;\mathbb Z)\). Hence \(\operatorname{Pic}_{\mathrm{top}}(S^1)=0\), while \(\operatorname{Pic}_{\mathrm{top}}(\mathbb {CP}^1)\cong\mathbb Z\). Under a unitary connection with curvature F, \(F/(2\pi i)\) represents the real image of \(c_1\) with the corresponding convention.

### Exercises with answers

1. What is \(w_1\) of the Möbius line over \(S^1\)? **Answer:** the nonzero generator of \(H^1(S^1;\mathbb Z/2)\).
2. Why can the tangent bundle of the sphere not have a global frame? **Answer:** even one nowhere-zero tangent section is impossible because the Euler class evaluates to 2.
3. Does a flat connection prove that a real line bundle is trivial? **Answer:** no; the Möbius line can have a flat connection with nontrivial holonomy and \(w_1\ne0\).
4. What happens to \(c_1\) under tensor product of line bundles? **Answer:** it adds.

### Reading and source notes

- Allen Hatcher, [*Vector Bundles and K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), characteristic classes and bundle obstructions.
- Allen Hatcher, [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html), cohomology and characteristic-class prerequisites.
- [UCLA, Differential Geometry lecture notes](https://math.ucla.edu/~sucharit/120A-notes.html), curvature and Gauss–Bonnet context.
