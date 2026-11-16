# 027000 — Prequantization: When Symplectic Area Must Be Integral

**Track:** Topology and Geometry. **Background:** symplectic forms, differential forms, circle bundles, connections and Chern classes. **Central question:** why does the existence of a quantum line bundle constrain the areas of classical geometric cycles?

<!-- BEGIN SPOKEN LECTURE -->

# A symplectic form measures more than length

On a smooth surface we can measure distance using a metric. A symplectic form is different. It measures oriented area in pairs of tangent directions. In higher even dimensions, a symplectic form is a nondegenerate, closed two-form. Its importance in mechanics comes from the way Hamilton's equations convert the differential of energy into a vector field describing motion.

Symplectic manifolds provide the setting for Hamiltonian flows and moment maps. Geometric quantization asks a different question. Starting from a classical symplectic phase space, can we construct a mathematical framework for quantum states and observables that retains the underlying geometry?

The first step is called prequantization. It attaches a complex line bundle with a connection to the symplectic manifold. The curvature of that connection is required to reproduce the symplectic form, scaled by Planck's constant. That requirement turns out to be a topological restriction, not merely a formula we can impose at will.

# A geometric phase around a loop

Imagine carrying a vector around a closed curve on a curved surface using parallel transport. After returning to the starting point, the vector may have rotated. A line bundle with a connection can behave similarly, except the fiber is a one-dimensional complex vector space. Parallel transport around a loop multiplies a vector by a phase, a complex number of magnitude one.

If the loop bounds a small surface, curvature controls the accumulated phase. In a prequantum bundle, the accumulated phase is related to symplectic area divided by Planck's constant. This explains why the two-form appears as curvature: it measures the local failure of parallel transport to return a phase unchanged.

But suppose a loop can bound two different surfaces. We must obtain a consistent phase regardless of which surface we use to calculate it. The difference between those two surfaces forms a closed two-cycle. Consistency requires the symplectic area over that closed cycle, divided by two pi times Planck's constant, to be an integer.

That condition is the integrality condition for prequantization. It is a statement about a cohomology class. It does not demand that the symplectic form have integer coefficients in any coordinate chart; it demands that all its periods on integral two-cycles have the correct integral values.

# The sphere as a test case

Take the two-sphere with its usual orientation and a symplectic form whose total area is A. The sphere has a fundamental two-dimensional homology class, so there is one essential area period to check. A prequantum line bundle can exist only if A divided by two pi times Planck's constant is an integer. Because A is positive in the chosen orientation, call this integer n, with n positive.

For the sphere viewed as the complex projective line, the holomorphic line bundle commonly denoted O of n has first Chern number n. We can choose a compatible Hermitian connection whose curvature corresponds to the symplectic form, with an appropriate sign convention.

So a global topological class of the line bundle encodes the total classical symplectic area. The area cannot be arbitrary if we insist on this precise prequantization construction.

This does not say all classical spheres are forbidden. It says that, for a fixed value of Planck's constant, a symplectic sphere of nonintegral normalized area does not admit a prequantum line bundle of the required kind. One might study other quantization frameworks, but this particular bundle construction has a clear obstruction.

# How curvature becomes a Chern class

The first Chern class of a complex line bundle lies in degree-two integral cohomology. Its image in real cohomology is represented by the connection curvature after dividing by the appropriate multiple of the imaginary unit and two pi. The prequantization condition identifies that real class with the symplectic class divided by two pi times Planck's constant, up to a conventional sign.

This is a meeting point of several earlier subjects. De Rham cohomology turns differential forms into cohomology classes. Characteristic classes classify topological information carried by bundles. Connections and curvature provide local differential descriptions. Prequantization demands that these three viewpoints match.

It is especially helpful to understand that the curvature is not itself an integer. It is a two-form varying from point to point. The integrality condition applies to its periods, or equivalently its cohomology class. Two connections on the same line bundle can have different local connection forms while representing the same first Chern class.

# A necessary start, not the finished quantum theory

Prequantization alone produces too many states. If we took all square-integrable sections of the line bundle on a compact phase space, the resulting space would generally be infinite-dimensional. In physically familiar finite-dimensional systems, the desired quantum state space can be much smaller.

The next step is to choose a polarization: a systematic way to retain only part of the classical phase-space dependence. In Kähler geometry, a holomorphic polarization replaces arbitrary smooth sections by holomorphic sections. That can turn a large prequantum space into a finite-dimensional vector space.

Not every polarization is globally available, and different polarizations can raise nontrivial questions of comparison. Furthermore, metaplectic or half-form corrections sometimes change the quantization. We should avoid treating geometric quantization as a universal mechanical procedure that assigns a unique Hilbert space to every symplectic manifold.

What prequantization already teaches us is substantial. The attempt to represent quantum phases geometrically turns symplectic area into an integral cohomology condition. A local curvature equation imposes a global topological obstruction. Choosing a holomorphic polarization on the sphere leads to an explicit calculation of the resulting quantum state space, and explains why spin representations have finite dimension.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. If a symplectic sphere has area `6 pi hbar`, what is its prequantum Chern number? **Answer:** three, under the indicated convention.
2. Why is an integer period condition not a local coordinate requirement? **Answer:** periods integrate over global closed two-cycles and depend only on cohomology.
3. Does a prequantum bundle already identify a finite-dimensional quantum Hilbert space? **Answer:** not generally; polarization is an additional step.
4. What does a flat tensor factor change? **Answer:** it can change global holonomy without changing curvature or the real Chern class.

### Reading and source notes

- [Woodhouse, Geometric Quantization](https://doi.org/10.1093/oso/9780198536734.001.0001), prequantization, polarizations and integral symplectic classes.
- [Guillemin and Sternberg, Symplectic Techniques in Physics](https://mitpressbookstore.mit.edu/book/9780521389907), symplectic curvature, line bundles and moment maps.
- [The Stacks Project, Cohomology of Schemes](https://stacks.math.columbia.edu/download/coherent.pdf), line bundles and sheaf cohomology background.
