# 022000 — Chern–Weil Theory: How Curvature Records Bundle Topology

**Track:** Topology and Geometry. **Background:** vector bundles, differential forms, connections and curvature, cohomology. **Central question:** how can a local connection produce a topological invariant that survives every change of connection?

<!-- BEGIN SPOKEN LECTURE -->

# Connections, Curvature, and Chern–Weil Theory

Imagine transporting a small arrow around a closed loop on a curved surface. When it returns, its direction may have changed. This failure to return unchanged is a form of holonomy, and it is controlled locally by curvature. But curvature has another role: when combined in the right way and integrated across the manifold, it can reveal how a bundle is twisted globally.

Chern–Weil theory develops that link. It begins with a connection, a rule for differentiating sections or transporting vectors from one fiber to another. It constructs differential forms from the connection's curvature. Then it proves that the cohomology classes of those forms do not depend on the particular connection chosen. Local differential information has produced a global topological invariant.

To understand why this is a substantial claim, consider a complex line bundle. Locally it looks like a product of the base space with a copy of the complex numbers. On overlapping charts the local coordinates can differ by multiplication by a unit complex number. Those transition functions may wind around the circle. The bundle can therefore be locally trivial everywhere while remaining globally twisted.

A connection can be described locally by a one-form, a kind of gauge potential. Two charts usually have different potentials, related by a change-of-trivialization rule. The curvature, however, agrees across the overlap, so it defines a globally meaningful two-form.

## A sphere with two gauge potentials

Take the two-dimensional sphere and cover it by a region that excludes the south pole and a region that excludes the north pole. Consider a circle bundle with one unit of topological twisting. We can write one local potential on the northern region and a different one on the southern region.

The northern potential is half of one minus cosine theta, multiplied by the differential of longitude. The southern potential is minus half of one plus cosine theta, multiplied by that same longitude differential. Neither formula is intended to be a globally smooth one-form on the whole sphere; each is valid on its own patch.

On the overlap the two potentials differ by the differential of longitude. This is exactly the kind of difference produced by a gauge transformation with one winding around the circle. Taking exterior derivatives of either local potential gives the same curvature: one half of sine theta times the spherical area element in coordinates.

Integrate that curvature over the entire sphere and divide by two pi. The result is one. If we used a transition function winding n times, the result would be n. The integer is the first Chern number of the line bundle.

The local connection forms depend on our choices; the Chern number does not. We could choose another connection and obtain a different curvature function, but its difference from the original curvature would be an exact form. By Stokes' theorem, its integral over a closed surface would be unchanged.

## Why we cannot always choose a global potential

This also explains why a nontrivial line bundle needs more than one gauge potential. If the curvature on the sphere were the exterior derivative of a globally defined one-form, its integral over the closed sphere would vanish by Stokes' theorem. But our curvature integral is two pi. So no single globally defined ordinary potential exists in this trivialization-based sense.

There is a conceptual distinction here. The connection itself is a globally defined geometric object on the bundle, even though its local potential forms do not fit together as one ordinary one-form on the base. Confusing the global connection with a global gauge potential is a common source of mistakes.

## Higher rank bundles

For a vector bundle with several complex dimensions in each fiber, the connection becomes matrix-valued. Its curvature is not just the exterior derivative of the matrix of one-forms; there is an additional product term, because matrix multiplication does not commute in general.

Individual entries of the curvature matrix depend on the chosen frame. Yet invariant polynomials of the curvature, such as appropriately normalized traces of powers, survive changes of frame. These become closed differential forms representing characteristic classes. The total Chern class and Chern character package families of such invariants.

The word invariant matters. If we simply select one matrix entry, nothing guarantees that it survives a change of coordinates. Chern–Weil theory uses polynomials preserved under conjugation, exactly the transformation law induced by changing a local frame.

The theorem also says that changing the connection changes the resulting characteristic form only by an exact form. There is a transgression formula explaining the difference. Thus the de Rham cohomology class remembers the bundle rather than the particular derivative rule we used to compute it.

## What curvature does not see

Chern–Weil forms live in real de Rham cohomology. Integral characteristic classes can have torsion components that become zero when mapped to real cohomology. Those components cannot be detected by integrating ordinary curvature forms. A flat connection may therefore coexist with some nontrivial global topology.

This is an important boundary on the method. Chern–Weil theory gives strong, computable characteristic classes, but it does not encode every possible topological distinction among bundles.

The larger significance is how many mathematical subjects meet here. Connections come from differential geometry; curvature comes from differential forms and transport; cohomology determines which curvature expressions carry global information; and characteristic classes appear in Riemann–Roch and index theory. The same bundle can be studied through local equations, global gluing, and numerical integrals. Chern–Weil theory proves that those descriptions are compatible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On a principal \(U(1)\)-bundle, use a real-valued local connection potential \(a_i\) with gauge conventions in which \(a_j-a_i=d\lambda_{ij}\). Curvature \(f=da_i\) is globally defined, and the de Rham image of the first Chern class is represented by \(f/(2\pi)\) with the chosen orientation and connection conventions.

For the degree-one bundle on \(S^2\), let
\[a_N=\tfrac12(1-\cos\theta)\,d\phi,\qquad a_S=-\tfrac12(1+\cos\theta)\,d\phi.\]
Then \(a_N-a_S=d\phi\), and
\[f=da_N=da_S=\tfrac12\sin\theta\,d\theta\wedge d\phi,\qquad\frac1{2\pi}\int_{S^2}f=1.\]
The difference of potentials is only asserted on the overlap; each local formula is regular on its own coordinate patch. For a unitary matrix-valued connection A, \(F=dA+A\wedge A\). Invariant polynomials of F yield closed forms. One normalization of the Chern character is \(\mathrm{ch}(E)=\mathrm{tr}\exp(iF/2\pi)\), depending on the skew-Hermitian connection convention.

Chern–Weil detects the real cohomology images of integral classes. Torsion classes vanish in real de Rham cohomology and are not detected by curvature integration. A different connection changes characteristic representatives by exact forms, not their de Rham classes.

### Exercises with answers

1. Compute \(\int_{S^2}f\) for the stated degree-one connection. **Answer:** \(2\pi\).
2. Why can no global base one-form a satisfy \(da=f\) in this example? **Answer:** Stokes would force \(\int_{S^2}f=0\), contradicting the calculation.
3. If a line bundle has first Chern number n, what is \(\int f\)? **Answer:** \(2\pi n\) with the adopted orientation and convention.
4. Does zero curvature force a complex bundle to be topologically trivial in every sense? **Answer:** no; real characteristic forms cannot detect torsion classes.

### Reading and source notes

- [University of Toronto, Symplectic Geometry lecture notes](https://www.math.toronto.edu/~mein/teaching/LectureNotes/symplectic.pdf), geometric background on connections, actions, and forms.
- [Cambridge University Press, Lectures on Kähler Geometry: Chern classes](https://doi.org/10.1017/CBO9780511618666.017), Chern–Weil representatives of characteristic classes.
- [University of Toronto, equivariant cohomology notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf), principal circle bundles and first Chern classes.
