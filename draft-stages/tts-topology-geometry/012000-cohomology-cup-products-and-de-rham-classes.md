# 012000 — Cohomology, Cup Products, and de Rham Classes

**Track:** Topology and Geometry. **Background:** homology, differential forms, Stokes' theorem, basic linear algebra. **Central question:** how can functions on cycles detect topology, and why does multiplying cohomology classes reveal more than their group sizes?

<!-- BEGIN SPOKEN LECTURE -->

# Cohomology, Cup Products, and de Rham Classes

Homology organizes cycles and boundaries. There is a natural complementary question: instead of building cycles, could we assign measurements to them? Integrating a differential form around a loop is one such measurement. When the form is closed, that integral depends only on the homology class of the loop, under the appropriate smoothness and orientation conditions. A boundary contributes zero by Stokes' theorem.

Cohomology develops this dual viewpoint. But it does more than record the same information with arrows reversed. Cohomology classes can be multiplied, and that multiplication can distinguish spaces whose individual groups look alike.

## From chains to cochains

For a simplicial complex, an integer-valued cochain of degree k is a homomorphism from the group of k-chains into the integers. Think of it as a rule that assigns a compatible integer measurement to each oriented k-simplex and extends linearly to chains.

The boundary operator lowers dimension. Its dual, called the coboundary, raises degree. A cochain is a cocycle if its coboundary is zero. It is a coboundary if it is the coboundary of a lower-degree cochain. The identity that boundary applied twice vanishes implies that coboundary applied twice also vanishes.

Cohomology is cocycles modulo coboundaries. Notice the symmetry: homology divides closed chains by chains that bound; cohomology divides closed measuring rules by rules obtained from a lower-dimensional potential.

For the circle, first cohomology with integer coefficients is the integers. A generator can be understood as a rule measuring how many times an oriented loop winds around the circle. More precisely, cohomology pairs with homology: a cocycle evaluates on a cycle, and the value does not change when either representative is changed by an appropriate boundary or coboundary.

## Closed differential forms

Now work on a smooth manifold. Differential forms provide a second cochain complex. The exterior derivative takes k-forms to k-plus-one forms and satisfies d squared equals zero. A form is closed when its exterior derivative vanishes and exact when it is the derivative of a form one degree lower. De Rham cohomology is the quotient of closed forms by exact forms.

On the punctured plane, consider the one-form that measures angular change around the origin. In coordinates it is negative y times d x plus x times d y, divided by x squared plus y squared. This form is smooth away from the origin, and its exterior derivative is zero. But its integral around the unit circle is two pi. If it were exact globally, its integral around every closed loop would be zero. Therefore it represents a nontrivial first de Rham cohomology class.

The point here is not that a derivative fails locally. On sufficiently small simply connected neighborhoods avoiding the origin, one can choose a local angle coordinate and express the form as a derivative. The obstruction is global. A family of local potentials cannot be assembled into one globally defined potential around the missing point.

## What de Rham's theorem says

A foundational theorem identifies de Rham cohomology with singular cohomology using real coefficients for smooth manifolds. Integration provides the bridge: a closed differential form yields a cochain by integrating over smooth singular simplices, and Stokes guarantees compatibility with the differentials. Proving that the resulting map induces an isomorphism requires real work, including local exactness and a gluing argument.

The coefficient field is important. Real differential forms do not detect finite torsion in integral cohomology. An integer cohomology group may contain torsion that vanishes after passage to real coefficients. So de Rham cohomology gives a powerful geometric model of real cohomology, not a replacement for every integral calculation.

## Why a product appears

Cohomology contains more structure than a sequence of abelian groups. Given a degree p class and a degree q class, their cup product is a class of degree p plus q. On the cochain level, the product evaluates one factor on an initial face of a simplex and the other on a complementary final face, with choices made consistently with the combinatorial construction.

The cup product is associative on cohomology and has a unit in degree zero. With integer coefficients, it is graded commutative: exchanging a degree p class and a degree q class introduces a sign of negative one raised to p times q. This sign carries geometric information about the orientation of intersections.

A space's cohomology ring is the direct sum of its cohomology groups together with this product. Two spaces may have isomorphic groups in every degree but different cup products. The ring remembers how different families of classes intersect or combine, not just how many there are.

## The torus calculation

Consider the surface of a doughnut, a two-dimensional torus. It has two basic kinds of loops, one going around the long direction and one around the short. First integral cohomology is free abelian of rank two, generated by classes we may call a and b. Its second cohomology is free abelian of rank one, generated by the oriented surface class u.

The product of a with b is u after a consistent choice of orientations. Reversing their order changes sign. The product of a with itself is zero, and the same for b. This multiplication says that the two independent one-dimensional directions combine to detect the two-dimensional orientation.

Compare the torus with a wedge of two circles and a separate sphere attached at a single point. Its reduced cohomology groups have the same ranks in degrees one and two as the torus: two in degree one, one in degree two. But every product of positive-degree classes is zero in that wedge space. Thus the groups agree and the rings differ. The cup product distinguishes them.

This example is why cohomology should not be treated as just homology in reverse. The multiplication can carry geometric information absent from a bare list of groups.

## Pullbacks and naturality

A continuous map between spaces pulls cohomology classes backward. On manifolds, a smooth map pulls differential forms backward, and this operation commutes with the exterior derivative. In both settings, it is compatible with products. That gives a method for testing maps: a proposed map must respect the cohomology ring structure.

For example, if the image of a degree-one class under a pullback is specified, then products of those classes constrain what can happen in degree two. Sometimes these algebraic constraints prove that a certain continuous map cannot exist with prescribed behavior on cycles or orientations.

Homology measures cycles that fail to bound. Cohomology measures closed rules that cannot be reduced to potentials. De Rham theory turns those rules into calculus, while the cup product shows that independent measurements can interact. The result is a new language for global geometry: not just the existence of holes, but the algebra of how their dual classes fit together.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a chain complex \((C_\bullet,\partial)\), cochains with coefficients in an abelian group \(G\) are \(C^k=\operatorname{Hom}_{\mathbb Z}(C_k,G)\), with \(\delta\varphi=\varphi\circ\partial\). Then \(H^k(C;G)=\ker\delta^k/\operatorname{im}\delta^{k-1}\).

On a smooth manifold, \(H^k_{\mathrm{dR}}(M)=\ker(d:\Omega^k\to\Omega^{k+1})/\operatorname{im}(d:\Omega^{k-1}\to\Omega^k)\). De Rham's theorem identifies this with \(H^k(M;\mathbb R)\). For \(M=\mathbb R^2\setminus\{0\}\), the form
\[
\omega=\frac{-y\,dx+x\,dy}{x^2+y^2},\qquad d\omega=0,\qquad\int_{S^1}\omega=2\pi
\]
represents a nonzero class. No globally defined smooth function \(f\) satisfies \(df=\omega\).

The cup product gives \(H^p(X;R)\times H^q(X;R)\to H^{p+q}(X;R)\), graded commutative on cohomology:
\[
a\smile b=(-1)^{pq}b\smile a.
\]
For the oriented torus \(T^2\), with \(a,b\in H^1(T^2;\mathbb Z)\) and \(u\in H^2(T^2;\mathbb Z)\) suitably oriented, \(a\smile b=u\), \(b\smile a=-u\), and \(a^2=b^2=0\). The wedge \(S^1\vee S^1\vee S^2\) has the same cohomology groups in nonnegative degrees but all positive-degree cup products zero.

### Exercises with answers

1. What is \(H^1_{\mathrm{dR}}(S^1)\)? **Answer:** \(\mathbb R\).
2. Does a closed form always equal \(df\) globally? **No:** the angular form on the punctured plane is a counterexample.
3. What degree has the product of a class in \(H^1\) with one in \(H^2\)? **Answer:** degree three.
4. Does real de Rham cohomology detect integral torsion? **No:** torsion classes vanish when passing to real coefficients.
5. Why do identical cohomology group ranks not guarantee equivalent cohomology rings? **Answer:** the cup-product maps can differ, as for \(T^2\) and \(S^1\vee S^1\vee S^2\).

### Reading and source notes

- Allen Hatcher, [*Algebraic Topology*, Chapter 3: Cohomology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), cup products and cohomology rings.
- MIT OCW, [*Geometry of Manifolds*](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/), differential forms and de Rham theory.
