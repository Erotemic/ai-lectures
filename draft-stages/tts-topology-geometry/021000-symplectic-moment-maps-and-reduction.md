# 021000 — Moment Maps: Symmetry, Conserved Quantities, and Reduction

**Track:** Topology and Geometry. **Background:** smooth manifolds, differential forms, group actions, Hamiltonian systems. **Central question:** when does a geometric symmetry have a numerical quantity that records its motion?

<!-- BEGIN SPOKEN LECTURE -->

# Symplectic Geometry and Moment Maps

A sphere can rotate while preserving its surface area. A mechanical system can evolve while preserving energy. A Hamiltonian system may have a continuous symmetry, and that symmetry often leads to a conserved quantity. These phenomena share a geometric explanation through symplectic forms and moment maps.

A symplectic form is a closed, nondegenerate differential two-form. Its nondegeneracy lets us associate vector fields with the differentials of functions. In Hamiltonian mechanics, this is how a function called the Hamiltonian generates a flow on phase space. Rather than regard position and momentum as two unrelated lists, symplectic geometry treats them as coordinates on a space with a special kind of area structure.

Now suppose a circle acts on such a space by symmetries that preserve the symplectic form. For every point in the space, the circle action traces an orbit. Infinitesimally, that orbit gives a vector field. Contracting the symplectic form with this vector field produces a one-form. Because the action preserves the symplectic form, this one-form is closed.

But a closed one-form is not always the differential of a globally defined function. The existence of such a function is the difference between a symplectic action and a Hamiltonian action. When it exists, that function is the component of a moment map.

## Height as a moment map

The two-dimensional sphere supplies a memorable example. Equip the sphere with its standard area form and let the circle rotate it around the vertical axis. Each point follows its latitude circle, except at the poles, which stay fixed. The height of a point remains constant during rotation.

Use spherical coordinates, with theta measuring angle down from the north pole and phi measuring longitude. The area form is the sine of theta times the wedge product of the theta and phi differentials. The vector field generating rotation is differentiation with respect to phi. Contract the area form with that vector field. The result is minus sine theta times the differential of theta, which is exactly the differential of cosine theta.

Thus the height, cosine theta, is a moment map for this circle action, with a consistent convention for the sign. The poles, where the rotation has fixed points, are the maximum and minimum of the height function. Between them, the latitude circles are the orbits of the symmetry.

The example turns an abstract contraction identity into a concrete observation: a symmetry is encoded by a function whose level sets are preserved by that symmetry.

## A counterexample on the torus

It would be tempting to say every circle action preserving a symplectic form has a moment map. That is false. Consider a flat two-dimensional torus, obtained by making both coordinates periodic. Translation in one coordinate preserves the standard area form. The contracted one-form is the differential of the other coordinate in a local chart.

But the other coordinate is periodic; it is not a globally defined real-valued function on the torus. The corresponding one-form is closed but not exact, because its integral around the appropriate fundamental loop is nonzero. So the action is symplectic but not Hamiltonian.

This is a direct connection between moment maps and de Rham cohomology. The obstruction to a Hamiltonian function is the cohomology class of the closed one-form obtained by contraction. Local formulas can exist everywhere, while a single global Hamiltonian does not.

## Symmetry reduction

Suppose a Hamiltonian group action has a moment map, and we fix a conserved momentum value. Instead of considering every point in the original phase space, we restrict to the level set of that value. Then we identify points lying along the same symmetry orbit. Under appropriate regularity and freeness assumptions, the resulting quotient inherits a symplectic form.

This is the Marsden–Weinstein reduction procedure. Its power lies in reducing dimension without discarding the Hamiltonian structure. If a group of dimension r acts freely and the chosen momentum value is regular and invariant, the reduction typically removes twice r dimensions: r from the momentum constraints and r from identifying symmetry orbits.

Return to the sphere. The zero-height level set is the equator, a circle. Rotations act transitively on that equator, so the quotient is a single point. A two-dimensional symplectic space has been reduced to zero dimensions at that momentum value. The quotient is simple because we chose a regular level away from the poles.

At singular values or nonfree orbits the quotient can have singularities, and the smooth-manifold version of the theorem no longer applies without modification. The hypotheses are part of the geometry, not administrative conditions.

## From one quantity to a polytope

For an action by a higher-dimensional torus, the moment map takes values in a vector space with one coordinate for each independent circle direction. On a compact connected symplectic manifold with a Hamiltonian torus action, its image is a convex polytope. This remarkable convexity theorem converts a highly curved geometric object into a finite-dimensional convex shape.

The sphere's interval of heights is the simplest instance: its moment image is the interval from the south pole to the north pole. More elaborate toric manifolds have polygons and higher-dimensional polytopes as their moment images, encoding substantial information about the geometry and symmetry.

Moment maps therefore connect conserved quantities, global topology, and convex geometry. The symmetry produces a closed one-form; cohomology decides whether it has a global Hamiltonian; and a regular momentum level can be reduced to a smaller symplectic space. The construction tells us not merely that a symmetry exists, but how to use it to simplify the mathematical system.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a symplectic manifold \((M,\omega)\), adopt the convention \(\iota_{X_H}\omega=dH\). A symplectic circle action with generating vector field X is Hamiltonian if \(\iota_X\omega=d\mu\) for a globally defined function \(\mu:M\to\mathbf R\). Cartan's formula gives \(d(\iota_X\omega)=\mathcal L_X\omega-\iota_Xd\omega=0\) for a symplectic action, but exactness is an additional global condition.

On \(S^2\), \(\omega=\sin\theta\,d\theta\wedge d\phi\), \(X=\partial_\phi\), and
\[\iota_X\omega=-\sin\theta\,d\theta=d(\cos\theta).\]
Thus \(\mu=\cos\theta\) with this convention. On \(T^2=\mathbf R^2/\mathbf Z^2\), \(\omega=dx\wedge dy\), \(X=\partial_x\) gives \(\iota_X\omega=dy\), whose integral around the y-circle equals one; it is not exact.

For a Hamiltonian action of a compact Lie group G with equivariant moment map \(\mu:M\to\mathfrak g^*\), if \(0\) is a regular value and G acts freely and properly on \(\mu^{-1}(0)\), the reduced space \(M//G=\mu^{-1}(0)/G\) is symplectic, with \(\dim(M//G)=\dim M-2\dim G\). For nonzero levels one typically reduces by the stabilizer of the coadjoint value. Singular reductions require different language.

### Exercises with answers

1. Compute the moment-map values at the north and south poles of the standard sphere. **Answer:** +1 and −1.
2. Why is translation on a flat torus not necessarily Hamiltonian? **Answer:** \(\iota_X\omega\) can represent a nonzero cohomology class even though it is closed.
3. What is the zero-level symplectic quotient of the standard sphere by rotation? **Answer:** a point, since the equator is one circle orbit.
4. What happens to dimension in a free regular reduction by a two-dimensional group? **Answer:** it drops by four.

### Reading and source notes

- [University of Toronto, Symplectic Geometry lecture notes](https://www.math.toronto.edu/~mein/teaching/LectureNotes/symplectic.pdf), Hamiltonian group actions, moment maps, and reduction.
- [ETH Zurich, Geometry of the Moment Map (2026)](https://people.math.ethz.ch/~acannas/Teaching/Moment_Map_2026/), contemporary examples and geometric context.
