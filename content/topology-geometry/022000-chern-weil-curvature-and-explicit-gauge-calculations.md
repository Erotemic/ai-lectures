# Chern-Weil curvature and explicit gauge calculations

<!-- BEGIN SPOKEN LECTURE -->

# Chern-Weil curvature and explicit gauge calculations

## Chern–Weil Theory: How Curvature Records Bundle Topology

Imagine transporting a small arrow around a closed loop on a curved surface. When it returns, its direction may have changed. This failure to return unchanged is a form of holonomy, and it is controlled locally by curvature. But curvature has another role: when combined in the right way and integrated across the manifold, it can reveal how a bundle is twisted globally.

Chern–Weil theory develops that link. It begins with a connection, a rule for differentiating sections or transporting vectors from one fiber to another. It constructs differential forms from the connection's curvature. Then it proves that the cohomology classes of those forms do not depend on the particular connection chosen. Local differential information has produced a global topological invariant.

To understand why this is a substantial claim, consider a complex line bundle. Locally it looks like a product of the base space with a copy of the complex numbers. On overlapping charts the local coordinates can differ by multiplication by a unit complex number. Those transition functions may wind around the circle. The bundle can therefore be locally trivial everywhere while remaining globally twisted.

A connection can be described locally by a one-form, a kind of gauge potential. Two charts usually have different potentials, related by a change-of-trivialization rule. The curvature, however, agrees across the overlap, so it defines a globally meaningful two-form.

### A sphere with two gauge potentials

Take the two-dimensional sphere and cover it by a region that excludes the south pole and a region that excludes the north pole. Consider a circle bundle with one unit of topological twisting. We can write one local potential on the northern region and a different one on the southern region.

The northern potential is half of one minus cosine theta, multiplied by the differential of longitude. The southern potential is minus half of one plus cosine theta, multiplied by that same longitude differential. Neither formula is intended to be a globally smooth one-form on the whole sphere; each is valid on its own patch.

On the overlap the two potentials differ by the differential of longitude. This is exactly the kind of difference produced by a gauge transformation with one winding around the circle. Taking exterior derivatives of either local potential gives the same curvature: one half of sine theta times the spherical area element in coordinates.

Integrate that curvature over the entire sphere and divide by two pi. The result is one. If we used a transition function winding n times, the result would be n. The integer is the first Chern number of the line bundle.

The local connection forms depend on our choices; the Chern number does not. We could choose another connection and obtain a different curvature function, but its difference from the original curvature would be an exact form. By Stokes' theorem, its integral over a closed surface would be unchanged.

### Why we cannot always choose a global potential

This also explains why a nontrivial line bundle needs more than one gauge potential. If the curvature on the sphere were the exterior derivative of a globally defined one-form, its integral over the closed sphere would vanish by Stokes' theorem. But our curvature integral is two pi. So no single globally defined ordinary potential exists in this trivialization-based sense.

There is a conceptual distinction here. The connection itself is a globally defined geometric object on the bundle, even though its local potential forms do not fit together as one ordinary one-form on the base. Confusing the global connection with a global gauge potential is a common source of mistakes.

### Higher rank bundles

For a vector bundle with several complex dimensions in each fiber, the connection becomes matrix-valued. Its curvature is not just the exterior derivative of the matrix of one-forms; there is an additional product term, because matrix multiplication does not commute in general.

Individual entries of the curvature matrix depend on the chosen frame. Yet invariant polynomials of the curvature, such as appropriately normalized traces of powers, survive changes of frame. These become closed differential forms representing characteristic classes. The total Chern class and Chern character package families of such invariants.

The word invariant matters. If we simply select one matrix entry, nothing guarantees that it survives a change of coordinates. Chern–Weil theory uses polynomials preserved under conjugation, exactly the transformation law induced by changing a local frame.

The theorem also says that changing the connection changes the resulting characteristic form only by an exact form. There is a transgression formula explaining the difference. Thus the de Rham cohomology class remembers the bundle rather than the particular derivative rule we used to compute it.

### What curvature does not see

Chern–Weil forms live in real de Rham cohomology. Integral characteristic classes can have torsion components that become zero when mapped to real cohomology. Those components cannot be detected by integrating ordinary curvature forms. A flat connection may therefore coexist with some nontrivial global topology.

This is an important boundary on the method. Chern–Weil theory gives strong, computable characteristic classes, but it does not encode every possible topological distinction among bundles.

The larger significance is how many mathematical subjects meet here. Connections come from differential geometry; curvature comes from differential forms and transport; cohomology determines which curvature expressions carry global information; and characteristic classes appear in Riemann–Roch and index theory. The same bundle can be studied through local equations, global gluing, and numerical integrals. Chern–Weil theory proves that those descriptions are compatible.

## Gauge Geometry by Calculation: Connections, Curvature, and Holonomy

Imagine transporting an arrow around a closed route. We need a rule telling us how the arrow changes as we move. If the rule is a connection, we can compare the arrow before and after the trip. The comparison is holonomy.

But we also need a way to describe the arrow at each point. A local basis or frame gives us coordinates. If we replace that frame with another one that varies from point to point, the coordinate formula for the connection changes. This is a gauge transformation. The geometry of transport must not depend on our arbitrary choice of local frame.

Gauge theory is built on precisely this distinction between descriptions and observables. We will derive the local form of that distinction and use a simple circle example to see why zero curvature does not mean trivial holonomy.

### Why a bundle needs local frames

A vector bundle assigns a vector space to each point of a manifold. A local frame chooses a basis in each fiber over a neighborhood. Inside that neighborhood we can represent a section as an ordinary column of component functions.

Over an overlap between neighborhoods, two frames may be related by a position-dependent invertible matrix. For a unitary bundle the matrices may lie in a unitary group, and for a general principal bundle they lie in a chosen Lie group G. The transition functions must satisfy compatibility rules when three neighborhoods overlap.

There need not be one global frame. That is how the underlying bundle can be twisted. A connection can nevertheless exist globally because its local formulas transform compatibly across those overlaps.

### Connections as matrix-valued one-forms

In a chosen local frame, the covariant derivative of a section has the form ordinary differentiation plus a matrix-valued one-form acting on the section. Call that one-form A. Evaluating A on a tangent direction gives a matrix that corrects how the section's components change along that direction.

A vector transported parallel along a curve has zero covariant derivative along its velocity. In coordinates, this is a first-order linear differential equation. The solution is a transport matrix taking initial components to final components.

When the matrices at different times commute, the solution resembles an ordinary exponential of the integral. When they do not commute, the order in which the matrices are encountered matters. The transport is described by an ordered exponential, or equivalently by solving the matrix differential equation directly.

The failure of parallel transport to commute around an infinitesimal loop is measured by curvature. For a matrix connection, curvature is not just the exterior derivative of A. There is also a quadratic term involving A with itself, because matrix multiplication does not generally commute.

### Changing the local frame

Let g be a smooth field of invertible matrices. Change the local frame by g, and components of a section change inversely. For the covariant derivative to represent the same geometric operation, its connection one-form must also change. The new one-form equals the old one conjugated by g, plus an extra term involving the derivative of g.

That derivative term is essential. A position-dependent frame rotates or twists as we move. Even if the original connection has zero local coefficients, the new coordinates can have nonzero coefficients purely because the frame itself moves.

Curvature transforms differently. The derivative terms cancel in the complete expression for curvature, leaving only conjugation. Consequently, traces of suitable curvature polynomials are gauge invariant. That is why Chern–Weil characteristic forms can be globally meaningful even when the connection is represented by different matrices in different neighborhoods.

For an abelian group such as U one, conjugation has no effect. Curvature is literally unchanged under a local gauge transformation. For a nonabelian group such as SU two, the matrix components of curvature can rotate by conjugation while gauge-invariant quantities built from them remain the same.

### A complete circle calculation

Take the trivial complex line bundle over a circle, with an angular coordinate theta. Choose the connection one-form equal to the imaginary unit times a real number a, times d theta. Since the base is one-dimensional, every two-form on it vanishes. The curvature is therefore zero.

Transport a complex number once around the circle. The parallel transport equation multiplies it by a phase. After a full turn, that phase is the exponential of minus the imaginary unit times two pi times a. Unless a is an integer, the phase need not equal one.

Here is a flat connection with nontrivial holonomy. It has no infinitesimal curvature, yet a finite trip around a topologically noncontractible loop produces a measurable rotation.

Now perform a gauge change that winds n times around the circle. It changes the connection parameter a by the integer n. But the holonomy phase does not change, because the exponential of minus two pi times the imaginary unit times an integer is one. The parameter a is not itself a gauge-invariant observable; its value modulo integers is the relevant quantity in this family.

This example is an important warning. Flatness is a local curvature condition. Triviality of holonomy is a global transport condition. On simply connected regions, flatness imposes much stronger consequences for parallel transport than it does on a circle with a nontrivial fundamental group.

### Transport around a loop in a nonabelian theory

For a matrix-valued connection, choose a base point and a frame there. Transport around a loop gives a group element. Change the frame at the base point and the resulting group element is conjugated. Its individual matrix entries are not invariant under that change, but its conjugacy class is. In a matrix representation, the trace of the holonomy can be gauge invariant. Such traced loop observables are often called Wilson loops.

If the loop is based at a different point, the comparison requires a path connecting the base points. The group element is not an absolute, coordinate-free number. Keeping track of base points and frame changes prevents false conclusions about what a gauge computation has measured.

### Toward gauge-theoretic equations

Gauge theory usually studies a space of connections modulo gauge transformations, sometimes restricted by differential equations. For example, in four-dimensional Riemannian geometry, the Hodge star splits curvature two-forms into self-dual and anti-self-dual parts. An instanton equation can require one of those parts to vanish.

The equation is nonlinear in the connection because curvature contains a quadratic term. If we linearize around a solution, we obtain a differential operator. But changes of connection produced by infinitesimal gauge transformations should not be counted as physically or geometrically independent deformations. The right infinitesimal structure is therefore a complex of operators, with kernels describing solutions and quotients removing gauge directions.

This is where elliptic theory, chain complexes, and bundle topology come together. Characteristic classes can constrain the bundle. The connection supplies curvature and holonomy. Gauge equivalence removes redundant coordinates. Elliptic Fredholm theory describes local deformation and obstruction spaces.

With the circle calculation in mind, these pieces become separable. Changing coordinates can change A without changing the connection. Curvature detects local failure of flat transport. Holonomy detects transport around finite loops, including global topology that local curvature may miss. A moduli space records connections after all allowable frame changes have been identified.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Chern–Weil Theory: How Curvature Records Bundle Topology

**Track:** Topology and Geometry. **Background:** vector bundles, differential forms, connections and curvature, cohomology. **Central question:** how can a local connection produce a topological invariant that survives every change of connection?

#### Mathematical companion (not spoken)

On a principal \(U(1)\)-bundle, use a real-valued local connection potential \(a_i\) with gauge conventions in which \(a_j-a_i=d\lambda_{ij}\). Curvature \(f=da_i\) is globally defined, and the de Rham image of the first Chern class is represented by \(f/(2\pi)\) with the chosen orientation and connection conventions.

For the degree-one bundle on \(S^2\), let
\[a_N=\tfrac12(1-\cos\theta)\,d\phi,\qquad a_S=-\tfrac12(1+\cos\theta)\,d\phi.\]
Then \(a_N-a_S=d\phi\), and
\[f=da_N=da_S=\tfrac12\sin\theta\,d\theta\wedge d\phi,\qquad\frac1{2\pi}\int_{S^2}f=1.\]
The difference of potentials is only asserted on the overlap; each local formula is regular on its own coordinate patch. For a unitary matrix-valued connection A, \(F=dA+A\wedge A\). Invariant polynomials of F yield closed forms. One normalization of the Chern character is \(\mathrm{ch}(E)=\mathrm{tr}\exp(iF/2\pi)\), depending on the skew-Hermitian connection convention.

Chern–Weil detects the real cohomology images of integral classes. Torsion classes vanish in real de Rham cohomology and are not detected by curvature integration. A different connection changes characteristic representatives by exact forms, not their de Rham classes.

##### Exercises with answers

1. Compute \(\int_{S^2}f\) for the stated degree-one connection. **Answer:** \(2\pi\).
2. Why can no global base one-form a satisfy \(da=f\) in this example? **Answer:** Stokes would force \(\int_{S^2}f=0\), contradicting the calculation.
3. If a line bundle has first Chern number n, what is \(\int f\)? **Answer:** \(2\pi n\) with the adopted orientation and convention.
4. Does zero curvature force a complex bundle to be topologically trivial in every sense? **Answer:** no; real characteristic forms cannot detect torsion classes.

##### Reading and source notes

- [University of Toronto, Symplectic Geometry lecture notes](https://www.math.toronto.edu/~mein/teaching/LectureNotes/symplectic.pdf), geometric background on connections, actions, and forms.
- [Cambridge University Press, Lectures on Kähler Geometry: Chern classes](https://doi.org/10.1017/CBO9780511618666.017), Chern–Weil representatives of characteristic classes.
- [University of Toronto, equivariant cohomology notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf), principal circle bundles and first Chern classes.

### Gauge Geometry by Calculation: Connections, Curvature, and Holonomy

**Track:** Topology and Geometry. **Background:** bundles, differential forms, matrix multiplication, parallel transport. **Central question:** what exactly changes when we change gauge, and what remains geometric?

#### Mathematical companion (not spoken)

In a local frame, \(\nabla=d+A\). For a frame change \(g:U\to G\), sections transform as \(s'=g^{-1}s\), and
\[A^g=g^{-1}Ag+g^{-1}dg,\qquad F_A=dA+A\wedge A,\qquad F_{A^g}=g^{-1}F_Ag.\]
Here \(A\wedge A\) uses matrix multiplication (equivalently \(\tfrac12[A\wedge A]\) with bracket convention). Along \(\gamma\), parallel transport \(U(t)\) satisfies \(\dot U=-A(\dot\gamma)U\), \(U(0)=I\). Under a gauge change, \(U^g(\gamma)=g(\gamma(1))^{-1}U(\gamma)g(\gamma(0))\), so a loop holonomy changes by conjugation at its base point.

For the trivial \(U(1)\) line bundle on \(S^1\), \(A=i a\,d\theta\), \(a\in\mathbf R\), \(F_A=0\), but \(\operatorname{Hol}(S^1)=e^{-2\pi i a}\). Under the global gauge \(g(\theta)=e^{in\theta}\), \(n\in\mathbf Z\), \(A^g=i(a+n)d\theta\); the holonomy is unchanged. On simply connected domains, a flat connection has path-independent transport up to endpoints, under the standard triviality assumptions; on \(S^1\), flat holonomy can be nontrivial.

For a Riemannian oriented four-manifold, \(*^2=1\) on two-forms and \(\Omega^2=\Omega^2_+\oplus\Omega^2_-\). Anti-self-dual equations take one common sign convention \(F_A^+=0\); swapping orientation interchanges the plus and minus spaces. Their moduli theory must quotient by the gauge group and analyze an associated elliptic deformation complex.

##### Exercises with answers

1. **Gauge law.** For an abelian connection \(A\) and \(g=e^{i\chi}\), what is \(A^g\)? **Answer:** \(A+i\,d\chi\), locally, where \(\chi\) is a chosen phase lift.
2. **Circle.** What is the holonomy of \(A=i\tfrac13d\theta\) around a positive full turn? **Answer:** \(e^{-2\pi i/3}\).
3. **Gauge winding.** Does replacing \(a\) by \(a+2\) change the holonomy? **Answer:** No.
4. **Nonabelian loop.** How does based holonomy transform if the frame changes by g at the base point? **Answer:** By conjugation \(U\mapsto g^{-1}Ug\).

##### Sources and further reading

- John C. Baez and Javier P. Muniain, [Gauge Fields, Knots and Gravity](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/PhilPhysics/Baez%2BMuniain1994GaugeFieldsKnots%2BGravity.pdf).
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), connections and vector bundles.
- Overviews: [Connection (principal bundle)](https://en.wikipedia.org/wiki/Connection_(principal_bundle)), [Holonomy](https://en.wikipedia.org/wiki/Holonomy).
