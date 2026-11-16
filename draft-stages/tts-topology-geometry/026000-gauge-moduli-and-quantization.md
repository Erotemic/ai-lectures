# Gauge moduli and quantization

<!-- BEGIN SPOKEN LECTURE -->

# Gauge moduli and quantization

## Holonomy and Gauge Moduli: Transport Around a Loop

Imagine moving a vector around a closed path on a curved surface. We try to keep the vector parallel as we move. After completing the loop, the vector can point in a different direction from where it began. That mismatch is holonomy: the transformation produced by parallel transport around a closed path.

Holonomy is more general than rotating tangent vectors on a surface. A connection on a vector bundle tells us how to compare fibers at nearby points. Following that instruction along a path produces a linear map from the initial fiber to the final fiber. For a closed loop, both fibers are the same, so we obtain a linear automorphism.

The collection of transformations from all loops based at one point forms a holonomy group. It records how the connection mixes the fiber as we move through the base space.

### Local formulas for transport

Choose a local frame. In that frame a connection can be written using a matrix-valued one-form A. Along a path gamma, parallel transport is governed by an ordinary differential equation. The transport matrix changes at a rate determined by minus A evaluated on the path's velocity, multiplied by the current transport matrix.

For one-dimensional complex fibers, the matrices are scalars and commute. Transport around a closed loop is an exponential of minus the integral of A around the loop. For higher-rank bundles, matrices at different positions may fail to commute, and the order in which the path encounters them matters. The solution is a path-ordered exponential.

The curvature of a connection is a two-form built from d A plus A wedge A. It measures, to first order, the failure of parallel transport around a tiny loop to be the identity. This makes curvature a local measure of holonomy.

But local curvature does not tell the whole story.

### A flat connection with nontrivial holonomy

Consider the circle. Choose an angle coordinate phi, understood modulo two pi, and a complex line bundle with a connection whose local one-form is i times theta d phi, for a real constant theta. Its curvature is zero, because there are no nonzero two-forms on a one-dimensional base. The connection is flat.

Now transport once around the circle. The resulting multiplication is the complex phase exp of minus two pi i theta. If theta is not an integer, the phase need not equal one. We have nontrivial holonomy even though the curvature vanishes everywhere.

There is no contradiction. Curvature describes what happens on small loops that contract to a point. A loop winding around the circle cannot be contracted there. It can detect global information that no local curvature measurement sees.

If theta changes by an integer, the phase remains the same. This reflects a change of gauge: different local descriptions can represent the same global connection. The gauge-invariant information is not the raw coefficient theta, but its value modulo the appropriate equivalence.

### Gauge transformations change descriptions

A choice of local frame is a gauge choice. Changing frames alters the matrix one-form A. It also changes the coordinates used to describe parallel transport. For a closed loop, the holonomy matrix transforms by conjugation at the base point. Its trace, characteristic polynomial, and conjugacy class therefore do not depend on the chosen frame.

For a unitary rank-one bundle, conjugation does nothing, so the phase itself is gauge invariant. In a higher-rank bundle, the individual entries of a holonomy matrix are not gauge invariants, but its conjugacy class is.

One sometimes encounters a Wilson loop, the trace of the holonomy around a closed path in a chosen representation. Wilson loops are natural gauge-invariant observables because conjugation leaves traces unchanged.

The transformation law is easy to misunderstand. A gauge transformation is not an operation that physically changes the connection's parallel transport in an arbitrary way. It changes its description using a different frame. Two gauge-related connections represent the same geometric transport structure.

### Flat connections and the fundamental group

For a flat connection, parallel transport around homotopic loops agrees, provided endpoints are fixed. Holonomy therefore descends to a group homomorphism from the fundamental group of the base into the structure group, up to conjugation.

On the circle, the fundamental group is the integers. A representation of the integers is specified by the image of one generator, exactly the holonomy around one full winding. This is why a single phase captures our flat line-bundle example.

On a simply connected base, flat connections have trivial holonomy around every loop. On a multiply connected base, different holonomy representations can exist even with zero curvature. Describing all flat connections may require allowing different principal bundles, not just connections in one fixed global trivialization.

This leads to a moduli problem. We want to classify connections modulo gauge transformations. The quotient is rarely a plain smooth manifold everywhere. Some connections have nontrivial stabilizers, and nearby deformations can behave differently at reducible and irreducible connections. An equivalence class can conceal automorphisms: the symmetry of a representative is additional information, which quotient-stack language is designed to retain.

### Two complementary invariants

Curvature and holonomy answer related but distinct questions. Curvature is infinitesimal and local. Holonomy accumulates transport along entire loops and can detect global topology. When curvature is zero, holonomy becomes homotopy-invariant; when curvature is nonzero, it generally depends on the detailed path, not only its homotopy class.

Connections turn geometry into a rule for comparison. Transport around loops tests that rule. Gauge theory studies the resulting geometric structures without confusing them with arbitrary choices of coordinates. The circle example shows why all three levels matter: local formulas, global loops, and equivalence under changes of frame.

## Prequantization: When Symplectic Area Must Be Integral

On a smooth surface we can measure distance using a metric. A symplectic form is different. It measures oriented area in pairs of tangent directions. In higher even dimensions, a symplectic form is a nondegenerate, closed two-form. Its importance in mechanics comes from the way Hamilton's equations convert the differential of energy into a vector field describing motion.

Symplectic manifolds provide the setting for Hamiltonian flows and moment maps. Geometric quantization asks a different question. Starting from a classical symplectic phase space, can we construct a mathematical framework for quantum states and observables that retains the underlying geometry?

The first step is called prequantization. It attaches a complex line bundle with a connection to the symplectic manifold. The curvature of that connection is required to reproduce the symplectic form, scaled by Planck's constant. That requirement turns out to be a topological restriction, not merely a formula we can impose at will.

## A geometric phase around a loop

Imagine carrying a vector around a closed curve on a curved surface using parallel transport. After returning to the starting point, the vector may have rotated. A line bundle with a connection can behave similarly, except the fiber is a one-dimensional complex vector space. Parallel transport around a loop multiplies a vector by a phase, a complex number of magnitude one.

If the loop bounds a small surface, curvature controls the accumulated phase. In a prequantum bundle, the accumulated phase is related to symplectic area divided by Planck's constant. This explains why the two-form appears as curvature: it measures the local failure of parallel transport to return a phase unchanged.

But suppose a loop can bound two different surfaces. We must obtain a consistent phase regardless of which surface we use to calculate it. The difference between those two surfaces forms a closed two-cycle. Consistency requires the symplectic area over that closed cycle, divided by two pi times Planck's constant, to be an integer.

That condition is the integrality condition for prequantization. It is a statement about a cohomology class. It does not demand that the symplectic form have integer coefficients in any coordinate chart; it demands that all its periods on integral two-cycles have the correct integral values.

## The sphere as a test case

Take the two-sphere with its usual orientation and a symplectic form whose total area is A. The sphere has a fundamental two-dimensional homology class, so there is one essential area period to check. A prequantum line bundle can exist only if A divided by two pi times Planck's constant is an integer. Because A is positive in the chosen orientation, call this integer n, with n positive.

For the sphere viewed as the complex projective line, the holomorphic line bundle commonly denoted O of n has first Chern number n. We can choose a compatible Hermitian connection whose curvature corresponds to the symplectic form, with an appropriate sign convention.

So a global topological class of the line bundle encodes the total classical symplectic area. The area cannot be arbitrary if we insist on this precise prequantization construction.

This does not say all classical spheres are forbidden. It says that, for a fixed value of Planck's constant, a symplectic sphere of nonintegral normalized area does not admit a prequantum line bundle of the required kind. One might study other quantization frameworks, but this particular bundle construction has a clear obstruction.

## How curvature becomes a Chern class

The first Chern class of a complex line bundle lies in degree-two integral cohomology. Its image in real cohomology is represented by the connection curvature after dividing by the appropriate multiple of the imaginary unit and two pi. The prequantization condition identifies that real class with the symplectic class divided by two pi times Planck's constant, up to a conventional sign.

This is a meeting point of several earlier subjects. De Rham cohomology turns differential forms into cohomology classes. Characteristic classes classify topological information carried by bundles. Connections and curvature provide local differential descriptions. Prequantization demands that these three viewpoints match.

It is especially helpful to understand that the curvature is not itself an integer. It is a two-form varying from point to point. The integrality condition applies to its periods, or equivalently its cohomology class. Two connections on the same line bundle can have different local connection forms while representing the same first Chern class.

## A necessary start, not the finished quantum theory

Prequantization alone produces too many states. If we took all square-integrable sections of the line bundle on a compact phase space, the resulting space would generally be infinite-dimensional. In physically familiar finite-dimensional systems, the desired quantum state space can be much smaller.

The next step is to choose a polarization: a systematic way to retain only part of the classical phase-space dependence. In Kähler geometry, a holomorphic polarization replaces arbitrary smooth sections by holomorphic sections. That can turn a large prequantum space into a finite-dimensional vector space.

Not every polarization is globally available, and different polarizations can raise nontrivial questions of comparison. Furthermore, metaplectic or half-form corrections sometimes change the quantization. We should avoid treating geometric quantization as a universal mechanical procedure that assigns a unique Hilbert space to every symplectic manifold.

What prequantization already teaches us is substantial. The attempt to represent quantum phases geometrically turns symplectic area into an integral cohomology condition. A local curvature equation imposes a global topological obstruction. Choosing a holomorphic polarization on the sphere leads to an explicit calculation of the resulting quantum state space, and explains why spin representations have finite dimension.

## Quantizing the Sphere: Holomorphic Sections and Spin

A symplectic sphere admits a prequantum line bundle when its total area, divided by two pi times Planck's constant, is an integer n. That integer is the line bundle's first Chern number. But sections of a line bundle can vary in infinitely many ways. Prequantization by itself has not explained why a quantum spin system should have a finite number of states.

To reduce the state space, geometric quantization introduces a polarization. The basic idea is to use only half of the classical phase-space variables, in a sense made precise by integrable Lagrangian distributions. On a Kähler manifold, a holomorphic polarization gives a particularly concrete answer: choose holomorphic sections of the prequantum line bundle.

The two-sphere is also the complex projective line. Its points can be represented by nonzero pairs of complex coordinates, with pairs identified when one is a nonzero complex multiple of the other. The line bundle O of n over this space is our central example.

## Counting holomorphic sections

For nonnegative n, holomorphic sections of O of n correspond to homogeneous polynomials of degree n in two complex variables. This is a theorem about projective space, but the counting is elementary once the correspondence is known.

How many monomials have total degree n? They are x to the n, x to the n minus one times y, and so on, ending with y to the n. There are n plus one of them. Each is linearly independent, and every homogeneous polynomial of degree n is their linear combination. Therefore the space of holomorphic sections has complex dimension n plus one.

If n equals zero, the space is one-dimensional: constants. If n equals one, the sections are linear polynomials in two variables, so the space is two-dimensional. If n equals two, the sections are quadratic polynomials and form a three-dimensional space.

The pattern now has a geometric explanation. Total symplectic area controls the line bundle's Chern number. The line bundle's degree controls the number of holomorphic sections. The quantum Hilbert space dimension is therefore tied to the integral geometry of the classical sphere.

## Where spin enters

Rotations of the sphere are described by the group SO three. A closely related group, SU two, is its double cover. SU two acts naturally on pairs of complex coordinates, and therefore on homogeneous polynomials in those coordinates. The degree-n polynomial space is the nth symmetric power of the fundamental two-dimensional complex representation.

That representation is irreducible and has dimension n plus one. In the standard physics convention, it is the spin-j representation with j equal to n over two. Thus n equals one gives spin one-half with two states, n equals two gives spin one with three states, and n equals three gives spin three-halves with four states.

We must be careful with the interpretation. The classical sphere here is not literally the configuration space of a tiny rigid ball. It is a coadjoint orbit carrying a symplectic form. Its group action and moment map encode classical angular momentum. Quantizing that orbit yields an irreducible representation of SU two.

This is a special case of a broad bridge between symplectic geometry and representation theory. Many finite-dimensional representations of compact Lie groups can be obtained from geometric data on appropriate orbits. The point is not only that we recover the right dimensions, but that the group action on the states comes from the action on the underlying geometry.

## Why a polarization changes the answer

Without a polarization, we might try to use all square-integrable prequantum sections. That space is much larger than the n-plus-one-dimensional space of holomorphic sections. The holomorphic condition is a differential restriction. It selects sections compatible with the complex structure and eliminates most of the freely varying functions.

On the projective line this restriction is especially transparent because all holomorphic sections can be described by finite-degree polynomials. On a general compact Kähler manifold, a similar construction uses the space of global holomorphic sections of a positive line bundle. Its dimension may be computed using Riemann–Roch and vanishing theorems, subjects already developed in the Algebra track.

So there are two independent ingredients. The integral symplectic form permits a line bundle in the first place. The polarization selects a subspace of sections. Neither step should be silently replaced by the other.

## The half-form qualification

Some geometric quantization constructions include a metaplectic correction, often called a half-form correction. This can shift which classical symplectic form corresponds to a given representation, and it changes some counting formulas. For the uncorrected holomorphic quantization of O of n on the projective line, the dimension is exactly n plus one. That is the convention we are using here.

A different correction convention may refer to a sphere with a shifted symplectic area when describing the same spin representation. These are not contradictory calculations when the geometric input and the correction are stated correctly. Trouble arises when formulas from different conventions are mixed without notice.

## A useful test of the construction

Try replacing n by a noninteger. There is no honest holomorphic line bundle O of that nonintegral degree on the projective line. So the polynomial construction cannot even begin. This is the global integrality condition reappearing in a simple algebraic form.

Next try n negative. In the same holomorphic polarization, O of a negative integer has no nonzero holomorphic sections. That is another sign that the orientation of the symplectic structure and choice of holomorphic line bundle matter. A negative degree with an incompatible polarization does not produce a state space by simply taking a negative number of monomials.

Finally, consider n large. The state-space dimension grows linearly with the normalized area of the sphere. More sophisticated semiclassical results say that dimensions of quantization spaces for higher-dimensional compact Kähler manifolds have leading terms controlled by symplectic volume. Our sphere calculation is the simplest example of that geometry-to-dimension relationship.

We have now built a complete example of quantization: integral symplectic area, a prequantum bundle, a holomorphic polarization, a finite-dimensional section space, and a symmetry representation. The same ingredients link topology, algebraic geometry, and quantum mechanics. They also show why geometric quantization is richer than simply replacing classical coordinates with noncommuting symbols.

## Quantization and Symplectic Reduction: Which Operation Comes First?

Suppose a mechanical system has a symmetry. We can use that symmetry classically to reduce the number of variables before studying the motion. Or we can first quantize the system and then retain only quantum states that transform in a specified way under the symmetry group.

Do those procedures give the same answer? This is the question behind the phrase quantization commutes with reduction. It is easy to say and surprisingly rich in mathematical content.

We will work with a compact sphere understood as the complex projective line. The sphere carries a rotational circle action. Its quantum states form an explicit finite-dimensional representation. The classical reduced spaces at regular moment-map values are points. We can check that the weight multiplicities in the quantum representation match the dimensions obtained by quantizing these reduced points.

## Classical reduction

A symplectic manifold is an even-dimensional space equipped with a closed nondegenerate two-form. A Hamiltonian circle action comes with a moment map, a real-valued function whose derivative is related to the vector field generating the circle action by contraction with the symplectic form.

Fix a value of that moment map. The level set consists of classical states having the selected conserved quantity. Under regularity and freeness hypotheses, we can divide this level set by the circle action. The quotient inherits a symplectic form and is called the reduced phase space.

The key point is that this is not merely taking the orbit space of the entire manifold. We first restrict to a level set of a conserved quantity and only then quotient by the symmetry. The dimension typically drops by twice the dimension of the group.

For a sphere with the usual axial circle rotation, a regular interior level set is a latitude circle. Quotienting by the rotation collapses that latitude circle to one point. At the north and south poles the symmetry has fixed points, so the endpoint levels are singular in the regular-value sense.

## Quantization of the sphere

Regard the sphere as the complex projective line and choose a prequantum line bundle of positive integral degree n. In a holomorphic polarization, the quantum space is the vector space of holomorphic sections of that line bundle. It has dimension n plus one.

We can write those sections explicitly as homogeneous polynomials of degree n in two coordinates. There are n plus one monomials: the first coordinate to the power zero, one, two, and so on up to n, multiplied by the appropriate power of the second coordinate.

The circle action acts on this space by scaling each monomial. With a fixed consistent choice of convention and equivariant lift, the weights are the integers from zero through n. Every weight occurs with multiplicity one.

So the quantum space has one state at each integral weight between the endpoints of the moment-map image. This is the simplest setting in which a geometric object produces a representation whose weight diagram looks like the classical moment interval.

## Compare the two constructions

Choose an interior integral weight, say k with k strictly between zero and n. On the quantum side, take the states with weight k. That space is one-dimensional because exactly one monomial has that weight.

On the classical side, reduce the sphere at the moment-map value corresponding to k. The regular level set is a circle, and after division by the circle action the reduced space is a point. The prequantum line bundle descends with the appropriate weight shift. Quantization of that point gives one complex degree of freedom.

Both procedures give dimension one. This is not a numerical coincidence. The general theorem states, under suitable geometric and representation-theoretic hypotheses, that multiplicities of quantum representations are computed by quantization of symplectic quotients.

For a nonabelian compact group, we typically look at an invariant subspace or an isotypic component associated with an irreducible representation. The corresponding reduced space can be constructed at a suitable coadjoint orbit or moment-map value, with conventions that must be tracked carefully.

## Why integrality matters

The prequantum line bundle only exists when the symplectic class obeys the appropriate integrality condition. The integer n in the sphere example is not an arbitrary discretization chosen after the fact. It measures the line bundle's first Chern number and controls both the total number of sections and the available weights.

A regular reduced space can inherit a quantization line bundle when the original geometric data and the chosen weight are compatible. If we shift the equivariant linearization, all the weights shift. If we include half-form or metaplectic corrections, the spaces and formulas can shift as well. An assertion that quantization commutes with reduction must specify which quantization construction is being used.

## What can go wrong

The clean example is compact, holomorphic, and regular at the chosen interior values. Many other settings are harder. A moment-map level can be singular. A group action may have stabilizers. The reduced space may be an orbifold or a stratified space rather than a smooth manifold. If the original manifold is noncompact, the quantum space may be infinite-dimensional and analytic conditions become essential.

There are powerful extensions of the theorem to some of these situations. But the statement is not automatically true for every possible notion of quantization or every quotient. One must check the conditions under which the comparison map is defined and invertible.

## A relationship between geometry and representation theory

The sphere calculation makes a general principle visible. Classical reduction selects a value of a conserved quantity and removes the corresponding symmetry direction. Quantum reduction selects a weight space in a representation. The moment map connects the two operations.

At integral regular values, quantization of a latitude quotient and selection of a monomial weight space agree. More generally, the topology of symplectic quotients and the multiplicities of representations are two sides of a single geometric construction. That is why symplectic geometry can answer questions about representation theory, and why representation theory can encode surprisingly detailed information about classical phase spaces.

## The Maslov Index: Why a Classical Orbit Acquires a Quantum Half-Step

The quantum harmonic oscillator has energy levels separated by a fixed amount. Its energies are not zero, one, two, and so on times that amount. They are one half, one and a half, two and a half, and so on. The one-half offset matters: even the ground state carries positive energy.

There is a geometric explanation for the offset. A semiclassical wave accumulates phase as it moves along a classical orbit. But when its path passes through a turning point, the usual local oscillatory description breaks down. Matching the wave across that turning point adds a phase correction.

The Maslov index is an integer that packages these corrections. It tells us why the naive rule of counting whole wavelengths around a classical orbit misses a half-step in a one-dimensional potential well.

## The classical action around an orbit

Consider a particle of mass m moving in a smooth confining potential. Its classical energy is kinetic energy plus potential energy. At a fixed energy, the momentum is positive as the particle moves right and negative as it returns left.

Draw the orbit in the phase plane, with position horizontally and momentum vertically. For a bound one-dimensional motion, the orbit is a closed loop. The integral of momentum against position around that loop is called the action. Geometrically, it is the area enclosed by the orbit, with a chosen orientation.

In the simplest old semiclassical rule, one demands that this action be an integer multiple of Planck's constant. That idea captures much of the spectrum at high energies, but it neglects the behavior at turning points, the positions where classical momentum becomes zero and the wave changes from oscillatory to exponentially decaying.

## What goes wrong at a turning point?

Away from a turning point, a semiclassical wave can be written approximately as a rapidly oscillating exponential whose phase comes from integrating momentum over position. The amplitude is inversely related to the square root of the local momentum.

That amplitude formula becomes singular when the momentum vanishes. The actual physical wave need not be singular. Instead, the approximation has become invalid. Near a simple turning point, one rescales the equation, and the leading local behavior is governed by an Airy function. Matching the Airy behavior to the oscillatory solutions supplies a phase shift.

Each ordinary soft turning point contributes a specific fraction of a full oscillation in the matching condition. For a one-dimensional well bounded by two simple turning points, their combined correction becomes a half-integer shift in the quantization rule.

This is a geometric correction, not a freely fitted constant. It follows from how local wave phases join as the classical orbit passes through places where the projection from phase space onto position space becomes singular.

## The Maslov index

In more geometric language, a family of tangent subspaces to the classical trajectory defines a path of Lagrangian directions. There is a distinguished set of directions where a chosen projection becomes singular. Crossing that set changes the phase of the semiclassical amplitude.

The Maslov index counts these crossings with signs and multiplicities under the chosen convention. In the ordinary one-dimensional bound-state problem with two soft turning points, the relevant index is two.

The improved quantization rule says that the action around the orbit is two pi times reduced Planck's constant, multiplied by the integer quantum number plus one quarter of the Maslov index. For index two, one quarter of the index is one half.

Different sign conventions may reverse an oriented index, but once the action orientation and phase convention are consistent, the physical quantization condition is unchanged.

## Calculate the harmonic oscillator

Now choose a harmonic potential: half the mass times the squared angular frequency times the squared position. The classical phase-plane orbit is an ellipse. Its area is the action integral. The ellipse has maximum position given by the oscillation amplitude and maximum momentum equal to mass times angular frequency times that amplitude.

Multiplying the two semi-axes and pi, we find that the enclosed area is two pi times the energy divided by the angular frequency.

Insert this action into the corrected quantization rule. Two pi times energy divided by frequency must equal two pi times reduced Planck's constant times the integer plus one half. Divide by two pi and multiply by frequency. The energy is reduced Planck's constant times angular frequency times the integer plus one half.

This is exactly the harmonic-oscillator spectrum. The semiclassical formula happens to reproduce the exact eigenvalues for this quadratic system. For a general potential well, it is an approximation, typically improved in the semiclassical or high-energy limit. The exactness of the oscillator does not license an exact spectral formula for every smooth potential.

## A comparison without turning points

Consider a free particle moving around a circle. Its classical trajectory has no turning point in the angular coordinate. The wave must be single-valued after one trip around the circle, but there is no Airy matching at a soft reflection. In the basic rotor model, the corresponding Maslov correction vanishes.

The angular momentum is an integer multiple of reduced Planck's constant, and the energy is proportional to the square of that integer. The contrast with the oscillator is instructive: both systems involve closed classical orbits, but only the oscillator's projected orbit has the two ordinary turning points responsible for the half-step.

## A topological index with spectral consequences

In higher-dimensional semiclassical mechanics, phase corrections arise at caustics where families of rays focus. The same underlying Maslov-index principle appears in wave propagation, Fourier integral operators, and geometric quantization.

The index is topological in the sense that it records how a path of Lagrangian subspaces winds relative to a singular set. Yet its effect is measurable as a shift in an energy quantization condition. The remarkable bridge is that topology of phase-space geometry changes the phase of a wave and therefore the allowed quantum states.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Holonomy and Gauge Moduli: Transport Around a Loop

**Track:** Topology and Geometry. **Background:** connections on bundles, differential forms, fundamental groups. **Central question:** how can transport around closed loops reveal geometry and topology invisible to local curvature measurements?

#### Mathematical companion (not spoken)

For a connection one-form `A` in a local frame along a smooth path gamma, parallel transport U satisfies
\[
\frac{dU}{dt}=-A_{\gamma(t)}(\dot\gamma(t))U(t),\qquad U(0)=I.
\]
The curvature is `F_A=dA+A wedge A`. Under gauge change `g`, `A -> g^{-1} A g+g^{-1}dg`; for loops based at x, holonomy changes by conjugation by `g(x)` (depending on the chosen frame convention).

On the trivial complex line bundle over `S^1=R/(2pi Z)`, take `A=i theta dphi`. Then `F_A=0`, but holonomy for one positive winding is `exp(-2pi i theta)`. Gauge `g(phi)=exp(i n phi)` is single-valued for `n in Z` and changes theta by an integer under the indicated transformation convention. The holonomy is invariant.

For flat connections, the holonomy of based loops factors through `pi_1(M,x)` and gives a representation `rho:pi_1(M,x)->G`, up to conjugation under basepoint-frame changes. For curved connections, holonomy is not generally invariant under ordinary homotopy of loops.

##### Exercises with answers

1. What is the curvature of `A=i theta dphi` on `S^1`? **Answer:** zero, since the base has no nonzero two-forms.
2. What is its holonomy after two positive windings? **Answer:** `exp(-4pi i theta)`.
3. Why is a trace of holonomy gauge invariant? **Answer:** holonomy changes by conjugation at the base point, and trace is conjugation invariant.
4. If the base is simply connected and the connection flat, what is the holonomy of every loop? **Answer:** the identity, assuming the usual connectedness and flat transport hypotheses.

##### Reading and source notes

- [Nakahara, Geometry, Topology and Physics](https://doi.org/10.1201/9781315275826), connections, curvature and holonomy.
- [Milnor, Morse Theory (Princeton University Press)](https://press.princeton.edu/books/paperback/9780691080086/morse-theory), topology background for the geometry track.
- [Freed and Uhlenbeck, Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9701-2), gauge classes and connections.

### Prequantization: When Symplectic Area Must Be Integral

**Track:** Topology and Geometry. **Background:** symplectic forms, differential forms, circle bundles, connections and Chern classes. **Central question:** why does the existence of a quantum line bundle constrain the areas of classical geometric cycles?

#### Mathematical companion (not spoken)

For a symplectic manifold `(M,omega)` and fixed positive `hbar`, a prequantum Hermitian line bundle `(L,nabla)` with unitary connection is required to satisfy, under one standard sign convention,
\[
F_\nabla=-\frac{i}{\hbar}\omega.
\]
The Chern–Weil representative then satisfies
\[
\frac{i}{2\pi}F_\nabla=\frac{[\omega]}{2\pi\hbar}
\quad\text{in}\quad H^2(M;\mathbb R),
\]
so a prequantum bundle requires `[omega]/(2 pi hbar)` to lie in the image of `H^2(M;Z)` in real cohomology. Conversely, under the usual smooth-manifold assumptions, this integrality condition yields a Hermitian line bundle with a connection of the prescribed curvature.

For `M=S^2`, take `\int_{S^2}\omega=A>0`. Since `H^2(S^2;Z)=Z`, integrality means
\[
n=\frac{A}{2\pi\hbar}\in\mathbb Z.
\]
For the standard complex structure on `CP^1`, `L=O(n)` has first Chern number n. Reversing curvature conventions can replace L by its dual, so signs must be kept consistent.

**Subtlety:** The integral cohomology class may have torsion invisible to de Rham periods. The curvature determines only its image in real cohomology, not a unique integral lift; flat line bundles can also intervene.

##### Exercises with answers

1. If a symplectic sphere has area `6 pi hbar`, what is its prequantum Chern number? **Answer:** three, under the indicated convention.
2. Why is an integer period condition not a local coordinate requirement? **Answer:** periods integrate over global closed two-cycles and depend only on cohomology.
3. Does a prequantum bundle already identify a finite-dimensional quantum Hilbert space? **Answer:** not generally; polarization is an additional step.
4. What does a flat tensor factor change? **Answer:** it can change global holonomy without changing curvature or the real Chern class.

##### Reading and source notes

- [Woodhouse, Geometric Quantization](https://doi.org/10.1093/oso/9780198536734.001.0001), prequantization, polarizations and integral symplectic classes.
- [Guillemin and Sternberg, Symplectic Techniques in Physics](https://mitpressbookstore.mit.edu/book/9780521389907), symplectic curvature, line bundles and moment maps.
- [The Stacks Project, Cohomology of Schemes](https://stacks.math.columbia.edu/download/coherent.pdf), line bundles and sheaf cohomology background.

### Quantizing the Sphere: Holomorphic Sections and Spin

**Track:** Topology and Geometry. **Background:** prequantum line bundles, complex projective space, holomorphic sections, and representation theory. **Central question:** how does a classical sphere lead to a finite-dimensional state space with precisely n plus one basis states?

#### Mathematical companion (not spoken)

Let `CP^1` carry its standard complex structure, and choose a symplectic form with prequantum degree `n>=0`. The uncorrected Kähler-polarized state space is
\[
\mathcal H_n=H^0(\mathbb{CP}^1,\mathcal O(n))
\cong\operatorname{Sym}^n((\mathbb C^2)^*),
\qquad\dim_{\mathbb C}\mathcal H_n=n+1.
\]
A basis is `z_0^n, z_0^{n-1}z_1, ..., z_1^n`; these are degree-n homogeneous polynomials in homogeneous coordinates. For `n<0`, `H^0(CP^1,O(n))=0` in the chosen holomorphic polarization.

The group SU(2) acts on `C^2`; its symmetric-power representation on degree-n homogeneous polynomials is irreducible of highest weight n and corresponds to spin `j=n/2`, with dimension `2j+1=n+1`. SO(3) acts projectively on half-integer-spin representations, whereas SU(2) acts linearly; distinguish the groups.

The Hirzebruch–Riemann–Roch expression on a curve is `chi(L)=deg L+1-g`. On `CP^1`, `g=0` and for `n>=0`, `H^1(O(n))=0`, so `h^0(O(n))=n+1`. A half-form/metaplectic correction may shift the relation between the symplectic area, the chosen bundle, and a representation. All formulas above use **uncorrected** holomorphic quantization.

##### Exercises with answers

1. How many holomorphic sections does `O(4)` have on `CP^1`? **Answer:** five, represented by the five degree-four monomials in two variables.
2. Which spin corresponds to `O(3)` under the chosen convention? **Answer:** spin three-halves, with four states.
3. Does `O(-1)` have any nonzero holomorphic sections on `CP^1`? **Answer:** no.
4. Why do rotations naturally act on the section space? **Answer:** SU(2) acts on the homogeneous coordinates, preserving the degree-n polynomial subspace.

##### Reading and source notes

- [Woodhouse, Geometric Quantization](https://doi.org/10.1093/oso/9780198536734.001.0001), holomorphic polarizations, Kähler quantization and the sphere.
- [Guillemin and Sternberg, Symplectic Techniques in Physics](https://mitpressbookstore.mit.edu/book/9780521389907), coadjoint orbits, moment maps and representation theory.
- [Fulton and Harris, Representation Theory: A First Course](https://doi.org/10.1007/978-1-4612-0979-9), symmetric powers of SU(2) and highest-weight representations.

### Quantization and Symplectic Reduction: Which Operation Comes First?

**Track:** Topology and Geometry. **Background:** symplectic manifolds, moment maps, line bundles, and group representations. **Central question:** when does taking quantum states and imposing symmetry agree with reducing the classical phase space first?

#### Mathematical companion (not spoken)

For a Hamiltonian action of a compact group G on a symplectic manifold (M,omega), with moment map `mu:M->g*`, the regular reduction at zero is `M//G=mu^-1(0)/G`, assuming zero is regular and the action on that level set is free (or allowing orbifold variants for finite isotropy). The reduced symplectic form is defined by pullback to the level set. Under compatible compact Kähler, prequantum and regularity hypotheses, quantization may satisfy `Q(M)^G ~= Q(M//G)`; at a nonzero integral weight, use the shifted character or shifting trick.

**Sphere example.** Let `M=CP^1` with prequantum line `L=O(n)`, `n>=2`, and a Hamiltonian circle action scaled so its moment image is `[0,n]`. With an appropriate lift and sign convention the holomorphic quantization has weight decomposition
\[
Q(M)=H^0(CP^1,O(n))\simeq\bigoplus_{k=0}^n \mathbb C_k,
\quad \dim Q(M)=n+1.
\]
Here C_k denotes the weight-k representation. For interior integer `0<k<n`, the reduced space `mu^-1(k)/S^1` is a point (regular free case), whose quantization is one-dimensional, matching `dim Q(M)_k=1`.

Conventions: prequantum curvature, signs for the moment map, torus action on the dual bundle and possible metaplectic correction can shift or reverse weights. Endpoint levels are fixed points and not regular; their treatment requires an appropriate singular-reduction framework. The dimension comparison is not an unconditional theorem for arbitrary noncompact or singular actions.

##### Exercises with answers

1. How many holomorphic sections does O(5) have on CP^1? **Answer:** six.
2. At an interior regular level of the standard circle moment map on CP^1, what is the reduced space? **Answer:** a single point.
3. If the quantization contains exactly one copy of weight two, what is the multiplicity of that character? **Answer:** one.
4. Why should we not apply the regular-value argument unchanged at a fixed pole? **Answer:** the pole is a critical level of the moment map and the action is not free there.

##### Reading and source notes

- [Guillemin–Sternberg theorem exposition, Hochs](https://www.math.ru.nl/~hochs/momentum_new.pdf), regular symplectic reduction and invariant quantum spaces.
- [University of Chicago, Quantization Commutes with Reduction](https://math.uchicago.edu/~may/REU2020/REUPapers/Ren%2CQiuyu.pdf), compact Kähler setting and a proof under stated freeness hypotheses.
- [Hall and Kirwin, Unitarity in Quantization Commutes with Reduction](https://arxiv.org/abs/math/0610005), distinctions involving inner products and metaplectic correction.

### The Maslov Index: Why a Classical Orbit Acquires a Quantum Half-Step

**Track:** Topology and Geometry. **Background:** Hamiltonian mechanics, symplectic phase space, and elementary wave asymptotics. **Central question:** what geometric phase correction appears when semiclassical waves pass through turning points?

#### Mathematical companion (not spoken)

For `H=p^2/(2m)+V(q)` with two simple turning points at energy E and a closed phase-plane orbit `gamma_E`, the leading corrected Bohr–Sommerfeld/EBK rule is
\[
\oint_{\gamma_E} p\,dq=2\pi\hbar\left(n+\frac\mu4\right),
\quad n=0,1,2,\ldots,
\]
where in the standard orientation and two-soft-turning-point convention `mu=2`. This is a *semiclassical* rule with regularity and nondegeneracy assumptions, not a general exact eigenvalue formula.

For `V(q)=m omega^2 q^2/2`, write the turning-point amplitude `a=sqrt(2E/(m omega^2))`. The phase-plane orbit is an ellipse with semi-axes `a` and `m omega a`, so
\[
\oint p\,dq=\pi a(m\omega a)=\frac{2\pi E}{\omega}.
\]
For `mu=2` the rule gives `E_n=hbar omega(n+1/2)`, which coincides with the exact spectrum for this quadratic Hamiltonian.

For a free rotor with coordinate theta on the circle, the action integral is `2 pi L` and the simple model has `mu=0`. Hence `L=n hbar`, `E_n=n^2 hbar^2/(2I)` for integer n (positive and negative momentum sectors). Different boundary conditions or nontrivial line bundles can shift rotor quantization, so this example specifies the ordinary periodic boundary condition.

##### Exercises with answers

1. Compute the Maslov correction `mu/4` for two soft turning points. **Answer:** `2/4=1/2`.
2. What is the classical action of a harmonic oscillator with energy E and frequency omega? **Answer:** `2 pi E/omega`.
3. Why does the naive WKB amplitude fail at a turning point? **Answer:** it contains inverse powers of momentum, which vanishes there; an Airy-type uniform approximation is needed.
4. Does the corrected Bohr–Sommerfeld rule give exact eigenvalues for every potential? **Answer:** no; exact agreement for the harmonic oscillator is a special feature of the quadratic problem.

##### Reading and source notes

- [MIT 5.73 Lecture Notes, Harmonic Oscillator and WKB](https://web.mit.edu/5.73/oldwww/Fall02/notes07.pdf), turning-point matching and oscillator quantization.
- [University of Toronto, Bohr–Sommerfeld Approximation](https://www.math.toronto.edu/ivrii/APM-textbook/Chapter6/L6.3.html), semiclassical spectral approximation and the Maslov index.
- [Bohr–Sommerfeld Quantization Lecture Notes](https://everettyou.github.io/teaching/PHYS130B/notes/ch3_path-integral/3-3-3-bohr-sommerfeld-quantization.html), phase corrections and the half-integer rule.
