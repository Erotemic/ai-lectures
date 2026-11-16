# 021100 — Symplectic Geometry by Example: Area Forms and Hamiltonian Motion

**Track:** Topology and Geometry. **Background:** differential forms, vector fields and flows, partial derivatives, basic mechanics. **Central question:** how can a two-form prescribe the motion of a mechanical system?

<!-- BEGIN SPOKEN LECTURE -->

# Symplectic Geometry by Example: Area Forms and Hamiltonian Motion

A pendulum has a position and a momentum. If we describe only its position, its future motion is not determined: two pendulums at the same angle can be moving in opposite directions. But the pair of position and momentum gives a state from which the evolution can be determined.

The space of all such states is called phase space. Symplectic geometry gives this space a special structure, a nondegenerate closed two-form, that converts the derivative of an energy function into a direction of motion. This is not merely a shorthand for Newton's laws. It is a geometry of conserved quantities, canonical coordinate changes, and constraints on possible transformations.

## Area in the position-momentum plane

Start with one position coordinate q and one momentum coordinate p. At every point of the phase plane, the expression d q wedge d p measures oriented infinitesimal area. Its sign changes if we reverse the order of the two directions. It is nondegenerate: no nonzero tangent vector has zero pairing with every possible tangent direction.

The two-form is also closed. Its exterior derivative vanishes. In two dimensions that is automatic for any top-degree form, but in higher-dimensional phase spaces closedness becomes a substantive requirement. A symplectic form in dimension two n has n conjugate pairs of position and momentum coordinates, at least locally.

A symplectic form is different from a Riemannian metric. A metric is symmetric and measures lengths and angles. A symplectic form is alternating and measures oriented two-dimensional pairing. It does not assign a positive squared length to a vector; pairing a vector with itself always gives zero.

## Turn energy into a vector field

Take a smooth energy function H, called the Hamiltonian. At a point of phase space, its derivative tells us how the energy changes in each infinitesimal direction. Nondegeneracy of the symplectic form makes it possible to associate exactly one vector field with that derivative.

We adopt the convention that inserting the Hamiltonian vector field into the first slot of the symplectic form gives the differential of H. For the standard position-momentum two-form this produces Hamilton's equations: the rate of change of position equals the derivative of H with respect to momentum, and the rate of change of momentum equals minus the derivative of H with respect to position.

Try the oscillator with energy equal to half the sum of position squared and momentum squared. The position rate is the momentum, and the momentum rate is minus the position. Differentiate the first equation once more and the result is the familiar harmonic oscillator equation. The trajectories in phase space are circles.

Why is the energy constant along these trajectories? The derivative of H along its own Hamiltonian vector field equals the symplectic form of that vector with itself. An alternating form evaluated twice on the same vector is zero. Energy conservation follows directly from the geometry, for a time-independent Hamiltonian.

## Symplectic motion preserves more than energy

Hamiltonian flow preserves the symplectic form. One way to see why is through the formula relating change along a vector field to exterior differentiation and contraction. The differential of the symplectic form is zero, and the contraction with the Hamiltonian vector field is an exact form. Apply another exterior derivative and the change vanishes.

In the phase plane, preserving the symplectic form means preserving oriented area. In higher even dimension, the symplectic form's repeated wedge product defines a volume form that Hamiltonian flow also preserves. This is the geometric content of Liouville's theorem in Hamiltonian mechanics.

But preserving volume is weaker than preserving the full symplectic form. In four or more dimensions, a transformation can preserve total volume while distorting the areas of particular two-dimensional directions. Later symplectic nonsqueezing results are built on this distinction: certain embeddings are forbidden by symplectic geometry even when the raw volume calculation would allow them.

## Local standard form and global restrictions

Every symplectic manifold looks locally like the standard position-momentum model. This is Darboux's theorem. A symplectic form has no local curvature invariant analogous to Gaussian curvature of a Riemannian metric. Appropriate local coordinates can always put it into the canonical sum of d q wedge d p terms.

Yet local standardness does not imply all symplectic manifolds are globally equivalent. A sphere with its area form has a nonzero total area. If that area form were the exterior derivative of a globally defined one-form, Stokes' theorem on the closed sphere would make its integral zero. Therefore it cannot be globally exact. The obstruction is topological, living in cohomology.

This provides an instructive contrast. Every tiny patch of a symplectic sphere has canonical coordinates. There is no single global pair of canonical coordinates covering the sphere in the same way as a full Euclidean plane.

## A rotation on the sphere

There is even a Hamiltonian picture for rotation around the north-south axis. Use a sphere of unit radius, with polar angle from the north pole and azimuthal angle around the axis. The area form is sine of the polar angle times the wedge of the two angular differentials.

The vector field that rotates azimuth while leaving polar angle fixed is Hamiltonian. With our sign convention, its Hamiltonian is the cosine of the polar angle, the vertical height. The level sets of this Hamiltonian are circles of latitude, and its flow moves points along them. The poles are fixed points of the rotation.

Now imagine a whole group of symmetries acting on a symplectic manifold. Under suitable hypotheses, a moment map collects the Hamiltonians generating the infinitesimal symmetries. Taking a level set of that map and dividing by the group action can yield a smaller symplectic space. This process is symplectic reduction.

Reduction needs qualifications: the level should be regular, and the group action on that level should have the necessary freeness and properness properties for a smooth quotient. Otherwise the result may be singular or stratified rather than an ordinary smooth manifold.

## What to carry forward

Hamiltonian mechanics can be described by one function and one nondegenerate closed two-form. The function gives energy, and the form turns its differential into motion. The resulting flow preserves both energy and symplectic structure. Local canonical coordinates simplify calculations, while global cohomology constrains what is possible.

Those are the essential foundations for moment maps, prequantization, geometric quantization, Floer homology, and symplectic capacities. The advanced subjects are different ways of exploring the interaction among dynamics, topology, and the area-like structure of phase space.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A symplectic manifold \((M^{2n},\omega)\) has \(d\omega=0\) and nondegenerate \(\omega_p\). On \(\mathbf R^{2n}\), \(\omega=\sum_{i=1}^n dq_i\wedge dp_i\). Fix the convention \(\iota_{X_H}\omega=dH\), giving
\[\dot q_i=\partial H/\partial p_i,\qquad\dot p_i=-\partial H/\partial q_i.\]
For \(H=(p^2+q^2)/2\), \(\dot q=p\), \(\dot p=-q\), \(\ddot q+q=0\). Energy conservation follows from \(\frac{d}{dt}H=dH(X_H)=\omega(X_H,X_H)=0\). Cartan's formula implies \(\mathcal L_{X_H}\omega=d(\iota_{X_H}\omega)+\iota_{X_H}d\omega=d^2H=0\), so the flow preserves \(\omega\) and \(\omega^n/n!\).

On the oriented unit sphere with \(\omega=\sin\vartheta\,d\vartheta\wedge d\varphi\), \(X=\partial_\varphi\) satisfies \(\iota_X\omega=-\sin\vartheta\,d\vartheta=d(\cos\vartheta)\), so \(H=\cos\vartheta\). The area form is not exact because \(\int_{S^2}\omega=4\pi\ne0\), in contrast with any global exact two-form on a closed manifold. Darboux's theorem is local; it does not imply global exactness or global canonical coordinates.

### Exercises with answers

1. **Oscillator.** With \(H=(p^2+4q^2)/2\), find Hamilton's equations. **Answer:** \(\dot q=p\), \(\dot p=-4q\).
2. **Conservation.** Explain why \(dH(X_H)=0\). **Answer:** It equals \(\omega(X_H,X_H)\), zero by antisymmetry.
3. **Spherical rotation.** Compute \(\iota_{\partial_\varphi}(\sin\vartheta\,d\vartheta\wedge d\varphi)\). **Answer:** \(-\sin\vartheta\,d\vartheta=d(\cos\vartheta)\).
4. **Global obstruction.** Why can the sphere's area form not equal \(d\alpha\) globally? **Answer:** Stokes' theorem would force its integral to vanish, but the area is positive.

### Sources and further reading

- University of Toronto, [Symplectic Geometry lecture notes](https://www.math.toronto.edu/mein/teaching/LectureNotes/symplectic.pdf).
- MIT OpenCourseWare, [18.966 Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/).
- Overviews: [Symplectic manifold](https://en.wikipedia.org/wiki/Symplectic_manifold), [Hamiltonian mechanics](https://en.wikipedia.org/wiki/Hamiltonian_mechanics).
