# Hamiltonian geometry, symmetries, and local normal forms

<!-- BEGIN SPOKEN LECTURE -->

# Hamiltonian geometry, symmetries, and local normal forms

## Symplectic Geometry by Example: Area Forms and Hamiltonian Motion

A pendulum has a position and a momentum. If we describe only its position, its future motion is not determined: two pendulums at the same angle can be moving in opposite directions. But the pair of position and momentum gives a state from which the evolution can be determined.

The space of all such states is called phase space. Symplectic geometry gives this space a special structure, a nondegenerate closed two-form, that converts the derivative of an energy function into a direction of motion. This is not merely a shorthand for Newton's laws. It is a geometry of conserved quantities, canonical coordinate changes, and constraints on possible transformations.

### Area in the position-momentum plane

Start with one position coordinate q and one momentum coordinate p. At every point of the phase plane, the expression d q wedge d p measures oriented infinitesimal area. Its sign changes if we reverse the order of the two directions. It is nondegenerate: no nonzero tangent vector has zero pairing with every possible tangent direction.

The two-form is also closed. Its exterior derivative vanishes. In two dimensions that is automatic for any top-degree form, but in higher-dimensional phase spaces closedness becomes a substantive requirement. A symplectic form in dimension two n has n conjugate pairs of position and momentum coordinates, at least locally.

A symplectic form is different from a Riemannian metric. A metric is symmetric and measures lengths and angles. A symplectic form is alternating and measures oriented two-dimensional pairing. It does not assign a positive squared length to a vector; pairing a vector with itself always gives zero.

### Turn energy into a vector field

Take a smooth energy function H, called the Hamiltonian. At a point of phase space, its derivative tells us how the energy changes in each infinitesimal direction. Nondegeneracy of the symplectic form makes it possible to associate exactly one vector field with that derivative.

We adopt the convention that inserting the Hamiltonian vector field into the first slot of the symplectic form gives the differential of H. For the standard position-momentum two-form this produces Hamilton's equations: the rate of change of position equals the derivative of H with respect to momentum, and the rate of change of momentum equals minus the derivative of H with respect to position.

Try the oscillator with energy equal to half the sum of position squared and momentum squared. The position rate is the momentum, and the momentum rate is minus the position. Differentiate the first equation once more and the result is the familiar harmonic oscillator equation. The trajectories in phase space are circles.

Why is the energy constant along these trajectories? The derivative of H along its own Hamiltonian vector field equals the symplectic form of that vector with itself. An alternating form evaluated twice on the same vector is zero. Energy conservation follows directly from the geometry, for a time-independent Hamiltonian.

### Symplectic motion preserves more than energy

Hamiltonian flow preserves the symplectic form. One way to see why is through the formula relating change along a vector field to exterior differentiation and contraction. The differential of the symplectic form is zero, and the contraction with the Hamiltonian vector field is an exact form. Apply another exterior derivative and the change vanishes.

In the phase plane, preserving the symplectic form means preserving oriented area. In higher even dimension, the symplectic form's repeated wedge product defines a volume form that Hamiltonian flow also preserves. This is the geometric content of Liouville's theorem in Hamiltonian mechanics.

But preserving volume is weaker than preserving the full symplectic form. In four or more dimensions, a transformation can preserve total volume while distorting the areas of particular two-dimensional directions. Later symplectic nonsqueezing results are built on this distinction: certain embeddings are forbidden by symplectic geometry even when the raw volume calculation would allow them.

### Local standard form and global restrictions

Every symplectic manifold looks locally like the standard position-momentum model. This is Darboux's theorem. A symplectic form has no local curvature invariant analogous to Gaussian curvature of a Riemannian metric. Appropriate local coordinates can always put it into the canonical sum of d q wedge d p terms.

Yet local standardness does not imply all symplectic manifolds are globally equivalent. A sphere with its area form has a nonzero total area. If that area form were the exterior derivative of a globally defined one-form, Stokes' theorem on the closed sphere would make its integral zero. Therefore it cannot be globally exact. The obstruction is topological, living in cohomology.

This provides an instructive contrast. Every tiny patch of a symplectic sphere has canonical coordinates. There is no single global pair of canonical coordinates covering the sphere in the same way as a full Euclidean plane.

### A rotation on the sphere

There is even a Hamiltonian picture for rotation around the north-south axis. Use a sphere of unit radius, with polar angle from the north pole and azimuthal angle around the axis. The area form is sine of the polar angle times the wedge of the two angular differentials.

The vector field that rotates azimuth while leaving polar angle fixed is Hamiltonian. With our sign convention, its Hamiltonian is the cosine of the polar angle, the vertical height. The level sets of this Hamiltonian are circles of latitude, and its flow moves points along them. The poles are fixed points of the rotation.

Now imagine a whole group of symmetries acting on a symplectic manifold. Under suitable hypotheses, a moment map collects the Hamiltonians generating the infinitesimal symmetries. Taking a level set of that map and dividing by the group action can yield a smaller symplectic space. This process is symplectic reduction.

Reduction needs qualifications: the level should be regular, and the group action on that level should have the necessary freeness and properness properties for a smooth quotient. Otherwise the result may be singular or stratified rather than an ordinary smooth manifold.

### What to carry forward

Hamiltonian mechanics can be described by one function and one nondegenerate closed two-form. The function gives energy, and the form turns its differential into motion. The resulting flow preserves both energy and symplectic structure. Local canonical coordinates simplify calculations, while global cohomology constrains what is possible.

Those are the essential foundations for moment maps, prequantization, geometric quantization, Floer homology, and symplectic capacities. The advanced subjects are different ways of exploring the interaction among dynamics, topology, and the area-like structure of phase space.

## Moment Maps: Symmetry, Conserved Quantities, and Reduction

A sphere can rotate while preserving its surface area. A mechanical system can evolve while preserving energy. A Hamiltonian system may have a continuous symmetry, and that symmetry often leads to a conserved quantity. These phenomena share a geometric explanation through symplectic forms and moment maps.

A symplectic form is a closed, nondegenerate differential two-form. Its nondegeneracy lets us associate vector fields with the differentials of functions. In Hamiltonian mechanics, this is how a function called the Hamiltonian generates a flow on phase space. Rather than regard position and momentum as two unrelated lists, symplectic geometry treats them as coordinates on a space with a special kind of area structure.

Now suppose a circle acts on such a space by symmetries that preserve the symplectic form. For every point in the space, the circle action traces an orbit. Infinitesimally, that orbit gives a vector field. Contracting the symplectic form with this vector field produces a one-form. Because the action preserves the symplectic form, this one-form is closed.

But a closed one-form is not always the differential of a globally defined function. The existence of such a function is the difference between a symplectic action and a Hamiltonian action. When it exists, that function is the component of a moment map.

### Height as a moment map

The two-dimensional sphere supplies a memorable example. Equip the sphere with its standard area form and let the circle rotate it around the vertical axis. Each point follows its latitude circle, except at the poles, which stay fixed. The height of a point remains constant during rotation.

Use spherical coordinates, with theta measuring angle down from the north pole and phi measuring longitude. The area form is the sine of theta times the wedge product of the theta and phi differentials. The vector field generating rotation is differentiation with respect to phi. Contract the area form with that vector field. The result is minus sine theta times the differential of theta, which is exactly the differential of cosine theta.

Thus the height, cosine theta, is a moment map for this circle action, with a consistent convention for the sign. The poles, where the rotation has fixed points, are the maximum and minimum of the height function. Between them, the latitude circles are the orbits of the symmetry.

The example turns an abstract contraction identity into a concrete observation: a symmetry is encoded by a function whose level sets are preserved by that symmetry.

### A counterexample on the torus

It would be tempting to say every circle action preserving a symplectic form has a moment map. That is false. Consider a flat two-dimensional torus, obtained by making both coordinates periodic. Translation in one coordinate preserves the standard area form. The contracted one-form is the differential of the other coordinate in a local chart.

But the other coordinate is periodic; it is not a globally defined real-valued function on the torus. The corresponding one-form is closed but not exact, because its integral around the appropriate fundamental loop is nonzero. So the action is symplectic but not Hamiltonian.

This is a direct connection between moment maps and de Rham cohomology. The obstruction to a Hamiltonian function is the cohomology class of the closed one-form obtained by contraction. Local formulas can exist everywhere, while a single global Hamiltonian does not.

### Symmetry reduction

Suppose a Hamiltonian group action has a moment map, and we fix a conserved momentum value. Instead of considering every point in the original phase space, we restrict to the level set of that value. Then we identify points lying along the same symmetry orbit. Under appropriate regularity and freeness assumptions, the resulting quotient inherits a symplectic form.

This is the Marsden–Weinstein reduction procedure. Its power lies in reducing dimension without discarding the Hamiltonian structure. If a group of dimension r acts freely and the chosen momentum value is regular and invariant, the reduction typically removes twice r dimensions: r from the momentum constraints and r from identifying symmetry orbits.

Return to the sphere. The zero-height level set is the equator, a circle. Rotations act transitively on that equator, so the quotient is a single point. A two-dimensional symplectic space has been reduced to zero dimensions at that momentum value. The quotient is simple because we chose a regular level away from the poles.

At singular values or nonfree orbits the quotient can have singularities, and the smooth-manifold version of the theorem no longer applies without modification. The hypotheses are part of the geometry, not administrative conditions.

### From one quantity to a polytope

For an action by a higher-dimensional torus, the moment map takes values in a vector space with one coordinate for each independent circle direction. On a compact connected symplectic manifold with a Hamiltonian torus action, its image is a convex polytope. This remarkable convexity theorem converts a highly curved geometric object into a finite-dimensional convex shape.

The sphere's interval of heights is the simplest instance: its moment image is the interval from the south pole to the north pole. More elaborate toric manifolds have polygons and higher-dimensional polytopes as their moment images, encoding substantial information about the geometry and symmetry.

Moment maps therefore connect conserved quantities, global topology, and convex geometry. The symmetry produces a closed one-form; cohomology decides whether it has a global Hamiltonian; and a regular momentum level can be reduced to a smaller symplectic space. The construction tells us not merely that a symmetry exists, but how to use it to simplify the mathematical system.

## Almost-Complex Structures: Turning Symplectic Area into Length

Imagine that someone gives you a map of a city that records the signed area of every tiny parallelogram, but supplies no rulers and no way to measure angles. That is roughly the information carried by a symplectic form. It compares two directions at a time, changes sign when we exchange them, and assigns zero when both directions are the same.

To talk about the length of a curve, or the energy of a map from a surface, we need something more. An almost-complex structure supplies a consistent way to turn a tangent direction through a quarter turn. Combining this rotation with symplectic area produces a metric. This is the bridge that lets methods from complex analysis and partial differential equations enter symplectic geometry.

### A quarter turn in the plane

Take the ordinary position-momentum plane with coordinates q and p. Its symplectic form is d q wedge d p. It reports positive area on the ordered pair consisting of the q direction followed by the p direction.

Define an operation J that sends the q direction to the p direction and the p direction to minus the q direction. Apply J twice and every vector changes sign. This is the equation J squared equals minus the identity. Multiplication by the imaginary number i has exactly the same property, which is why we use the word complex.

Now take any vector v. Pair v with J of v using symplectic area. In the standard plane the answer is the ordinary squared length of v. For two potentially different vectors v and w, pairing v with J of w gives their usual dot product. A quantity that was originally antisymmetric has become a symmetric positive metric, because the quarter turn makes the second argument different.

That construction has three requirements. J squared must be minus the identity. The symplectic form must remain unchanged if we rotate both inputs by J. And the pairing of a nonzero vector with its J rotation must be strictly positive. When all three hold, we call J compatible with the symplectic form.

### More than one useful choice

The standard quarter turn is not forced. Suppose that one unit along q should have length different from one unit along p. Choose a positive number a. Define J to send the unit q direction to a times the p direction, and send the unit p direction to minus one over a times the q direction. Two applications of J still reverse every vector. The resulting metric measures q displacements with squared scale a and p displacements with squared scale one over a.

Every choice of positive a gives a legitimate compatible complex structure. The symplectic area d q wedge d p has not changed; only the associated metric has. So a symplectic manifold does not single out one metric. Instead it permits a large family of metrics tied to choices of compatible J.

This flexibility matters later. A well-chosen J can simplify a differential equation, make a geometric symmetry visible, or help make a moduli space of solutions regular. Yet changing J does not mean changing the underlying symplectic form.

### From one plane to a manifold

At each point of a symplectic manifold, the tangent space is an even-dimensional symplectic vector space. Linear algebra produces compatible complex structures on such spaces. More importantly, these choices can be made smoothly as we move from point to point. Every symplectic manifold therefore admits compatible almost-complex structures.

Why 'almost'? Because each tangent space separately looks like a complex vector space, but that does not guarantee complex coordinates that fit together on neighborhoods. The integrability condition asks whether we can choose genuine complex charts whose derivatives agree with J. A complex manifold has such charts; a general almost-complex manifold need not.

In real dimension two, every smooth almost-complex structure is integrable. On surfaces, the analytic and almost-complex pictures coincide locally. In four or more real dimensions, the integrability obstruction can be nonzero. That is precisely why studying curves that respect J is more flexible than requiring the entire target to be a complex manifold.

### Compatible versus merely tame

Another word appears often in the advanced literature: tame. A symplectic form tames J if the area pairing of v with J of v is positive for every nonzero v. Compatibility demands more, including preservation of the symplectic form under J on both arguments. Taming is the weaker condition.

For a tame J, the quantity obtained by pairing v with J of w need not itself be symmetric. It does, however, have a positive quadratic part and still gives useful positivity for J-holomorphic curves. For our first calculations, compatible J is simpler because it produces a genuine metric directly.

### Why a complex rotation helps analyze curves

Suppose a map carries a two-dimensional surface into our symplectic manifold. A small region in the surface has two coordinate directions. We can ask whether differentiating in the second direction is the same as differentiating in the first direction and then applying J. If the domain also has its own quarter-turn operation, the clean statement is that differentiation commutes with those two quarter turns.

This is the definition of a pseudoholomorphic, or J-holomorphic, map. In the ordinary complex plane it reduces to the Cauchy-Riemann equations. On an arbitrary symplectic manifold the same equation still makes sense, even when there is no complex coordinate system on the target.

For such a map, area and energy become linked. The metric constructed from the symplectic form and J measures the total squared derivative of the map. The map's adherence to the complex-rotation equation forces that energy to equal its symplectic area, with a suitable normalization. Thus area controls an analytic quantity that can constrain sequences of curves.

The relationship is powerful but should not be overread. Positive energy by itself does not establish compactness, and the existence of a compatible J does not make all maps holomorphic. What it does is turn symplectic geometry into a setting where precise elliptic equations can be posed and estimated.

When you next encounter a holomorphic curve in a symplectic manifold, remember the sequence of constructions. We begin with alternating area, choose a quarter turn on tangent vectors, obtain a positive metric, and then ask which surface maps respect the two quarter turns. The apparently abstract J is the device that makes all the later analysis possible.

## Darboux and Moser: Why Symplectic Forms Are Locally Simple

In Riemannian geometry, curvature can distinguish two spaces even when we inspect them through a microscope. A sphere has positive curvature, while a flat plane has zero curvature. Symplectic geometry behaves differently: every symplectic manifold has local coordinates in which its area form looks exactly like the standard one.

That is Darboux's theorem. Why should it be true, and why does it not imply that all symplectic manifolds are globally the same? The key idea is a method of moving differential forms by flowing points. It is often called Moser's method.

### Begin with two area forms

Picture a sphere with two ways to measure area. One form gives larger weight near the northern hemisphere; the other gives larger weight near the southern hemisphere. Suppose both forms are positive everywhere, and suppose their total areas are equal.

They do not agree point by point. But there is a diffeomorphism of the sphere that carries one area measurement to the other. The map redistributes area without tearing the surface. It need not preserve the latitude circles, and there is no reason for it to be unique.

Total area is an obvious necessary condition. A change of coordinates cannot alter the integral of a pulled-back top-degree form on a closed oriented manifold. Moser's argument shows that, on a compact connected oriented surface, equality of total area is also sufficient for positive area forms.

### Connect the forms by a path

Instead of trying to find the final coordinate change in one step, imagine a continuous movie of forms. At time zero, we see the first form. At time one, we see the second. In between, use a weighted average of the two.

On a surface, any positive weighted average of positive area forms remains positive. So every frame of the movie is still symplectic. In higher dimensions, a straight-line average of symplectic forms might become degenerate, and we cannot skip checking this condition.

Equality of total area on a sphere means the forms represent the same de Rham cohomology class. Their difference is the exterior derivative of a one-form. That one-form will be the input for a vector field designed to undo the change in area measurement.

### Find a moving coordinate system

We seek a family of diffeomorphisms that pulls each moving form back to the original one. What should its velocity be?

The rate of change of a pulled-back form contains two contributions. First the form itself is changing with time. Second the diffeomorphism is moving points through the form. The latter is described by the Lie derivative along the motion's vector field.

Cartan's formula expresses the Lie derivative of a closed form as the exterior derivative of its contraction with the vector field. This is the opening: the time derivative of our family of forms is also an exterior derivative. We can arrange for the two contributions to cancel by choosing the vector field whose contraction with the current symplectic form is minus the one-form measuring the difference.

Nondegeneracy guarantees a unique vector field satisfying that equation at each point. Smooth dependence on time makes it into a time-dependent flow. On a compact manifold the flow exists throughout the finite time interval. When we differentiate the pullback along this flow, its derivative is zero. The pulled-back symplectic form is therefore constant throughout the movie.

At the end we have the desired coordinate transformation.

### Darboux's theorem is a local application

For Darboux's theorem we do not start with two global area forms on one sphere. We stand near one point of an arbitrary symplectic manifold. Choose ordinary local coordinates and make a linear adjustment so that the given symplectic form agrees with the standard form at that point.

Now interpolate between the constant standard form and the actual varying form. Because they agree at the center, shrinking the coordinate neighborhood ensures that all intermediate forms remain nondegenerate. A local version of the same flow argument supplies new coordinates in which the symplectic form becomes exactly standard.

Every symplectic manifold of dimension two n therefore has local coordinates consisting of n position directions and n momentum directions, with the standard sum of position-momentum area pairings.

The local theorem does not state that all symplectic manifolds are diffeomorphic, nor that every symplectic form on a fixed manifold belongs to the same global cohomology class. The existence of one local coordinate system says almost nothing about how the systems must fit together over the whole manifold.

### Why global topology survives

Return to the sphere. Its area form cannot be the derivative of a globally defined one-form. If it were, Stokes' theorem would say its total area is zero, contradicting positivity. So a symplectic sphere cannot be globally equivalent to a region of the standard phase plane in a way that pulls back the standard exact symplectic form to its whole area form.

The same obstruction reappears in prequantization. Integrating a symplectic form over closed surfaces produces periods of a cohomology class. Those periods do not disappear under local coordinate changes.

Moser's method also has limitations. On a higher-dimensional manifold, cohomologous symplectic forms need not be linked by a path of symplectic forms. Without such a path the basic isotopy argument cannot even begin. Compactness or suitable control at infinity matters too, because the chosen vector field must have a flow for the intended time interval.

### A technique you will see again

This method is more general than a theorem about symplectic coordinates. It teaches a recurring strategy: express variation as an exact differential, find a vector field that cancels the variation, and integrate the vector field to transport structure.

Later we will study moduli spaces where choosing coordinates that follow a family of objects is not nearly so easy. Moser's calculation is a first example of how local infinitesimal solvability can, under explicit hypotheses, be turned into a global geometric equivalence. Keep the distinction clear: the local equations are flexible, while global topology and completeness impose the constraints.

## Lagrangian Geometry: Graphs, Intersections, and Exactness

Imagine a position-momentum phase space. A general point records where a particle is and how fast it is moving. Now imagine selecting just those states whose momentum obeys a rule determined by position. Such a set is a graph over position space.

Many of the most important graphs in symplectic geometry are Lagrangian submanifolds. They have half the dimension of the full phase space, and the symplectic form vanishes when both arguments lie along the graph. Their intersections turn out to encode critical points of functions. That simple observation is the finite-dimensional doorway into Lagrangian Floer homology.

### Why half dimension is special

On the ordinary q-p plane, every smooth one-dimensional curve has zero symplectic area when evaluated on two tangent vectors to the curve. Both tangent vectors point along the same line, and an alternating two-form vanishes on parallel directions.

In four-dimensional phase space, however, an arbitrary two-dimensional surface need not have this property. Consider the surface spanned by the first position direction and the first momentum direction. Those directions have nonzero symplectic pairing. It is not Lagrangian.

A submanifold is Lagrangian if its tangent space is as large as possible while carrying no symplectic area internally. In a phase space of dimension two n, a Lagrangian therefore has dimension n. In each tangent space it is its own symplectic orthogonal complement.

### The zero section

Take a circle as position space. At each point of the circle attach a momentum line. The resulting cylinder is the cotangent bundle of the circle. The zero section is the central circle consisting of all positions with momentum zero.

Along the zero section, every tangent vector points in the position direction. The symplectic form pairs position with momentum, so it vanishes on the zero section. The zero section is Lagrangian. The same construction works for any smooth position manifold: its zero section inside the cotangent bundle is Lagrangian.

Now consider a smooth function f on position space. At each position q, assign momentum equal to the derivative of f at q. The graph of this derivative is another Lagrangian. The reason is that mixed second derivatives of f agree, and the antisymmetric part required to produce symplectic area cancels.

More generally, the graph of a one-form is Lagrangian exactly when that one-form is closed. A derivative is always closed, so graph-of-derivative is a special case. Closed does not always mean globally a derivative, and that difference will matter.

### Critical points become intersections

Where does the graph of the derivative intersect the zero section? Precisely where the derivative is zero. Thus the intersection points are the critical points of f.

Choose the function cosine of the angle around the circle. It has a maximum at one point and a minimum at the opposite point. Its derivative vanishes at exactly those two places. Hence its graph meets the zero section twice. A simple calculus exercise has turned into a count of Lagrangian intersections.

Move the graph by a small amount while preserving the symplectic structure through a Hamiltonian motion. We expect the number of intersections to vary, but topology prevents us from always eliminating them. Lagrangian Floer theory will replace simple intersection counts with a chain complex that is more stable under such motions.

A picture of two crossing curves is not enough, however. An intersection must be transverse if we want it to be isolated and behave predictably under perturbation. For the graph of d f, transversality at a critical point means the Hessian of f is nonsingular: it is exactly the Morse nondegeneracy condition.

### Exactness is more information than closedness

The cotangent bundle carries a natural one-form built from momentum and position. With our sign convention, take minus p times d q; its exterior derivative is the symplectic form d q wedge d p. A Lagrangian is called exact when this one-form becomes the differential of a globally defined function after restriction to the Lagrangian.

On the graph of d f, the natural one-form restricts to minus d f. So this graph is exact. The zero section is also exact, with zero primitive.

Contrast that with a graph on the circle where the momentum is a fixed nonzero constant. Its defining one-form is closed, because a one-form on a one-dimensional manifold is automatically closed. But it is not the derivative of a single-valued periodic function: its integral once around the circle is nonzero. The graph is Lagrangian but not exact.

This distinction has consequences for intersections. The constant-momentum graph never intersects the zero section. It is produced by shifting every momentum by the same amount, which is a symplectic transformation. But it is not Hamiltonian isotopic to the zero section through compactly supported or appropriate global Hamiltonian flows. Otherwise the intersection results we will eventually prove would give a contradiction.

### Exactness controls a future analytic problem

When we study a holomorphic disk whose boundary lies on one Lagrangian, the symplectic area of the disk equals an integral of the natural one-form around its boundary, provided the ambient symplectic form is exact. If the Lagrangian is exact, that boundary integral vanishes.

Holomorphic disks have nonnegative energy, and in the compatible setting energy equals symplectic area. Thus a disk with boundary on an exact Lagrangian in an exact symplectic manifold must be constant. This removes one important kind of bubbling from later compactness arguments.

It does not remove every difficulty. Curves can still escape to infinity in noncompact cotangent bundles unless geometric estimates prevent it. They may also break into multiple strips. Exactness is a specific tool, not an automatic proof of all Floer theory.

### From calculus to geometry and back

We have now walked a full circle. The derivative of a function gives a Lagrangian graph. Critical points become intersections. Nonsingular Hessians become transverse intersections. Gradients and the trajectories connecting critical points will reappear as thin solutions of a two-variable elliptic equation.

In the simplest cotangent-bundle model, Floer homology will recover the homology of the original position space. Understanding that result begins here, with the ordinary geometry of the zero section and the graph of a derivative. The infinite-dimensional machinery will be more complicated, but its basic generators have already appeared in first-year calculus.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Symplectic Geometry by Example: Area Forms and Hamiltonian Motion

**Track:** Topology and Geometry. **Background:** differential forms, vector fields and flows, partial derivatives, basic mechanics. **Central question:** how can a two-form prescribe the motion of a mechanical system?

#### Mathematical companion (not spoken)

A symplectic manifold \((M^{2n},\omega)\) has \(d\omega=0\) and nondegenerate \(\omega_p\). On \(\mathbf R^{2n}\), \(\omega=\sum_{i=1}^n dq_i\wedge dp_i\). Fix the convention \(\iota_{X_H}\omega=dH\), giving
\[\dot q_i=\partial H/\partial p_i,\qquad\dot p_i=-\partial H/\partial q_i.\]
For \(H=(p^2+q^2)/2\), \(\dot q=p\), \(\dot p=-q\), \(\ddot q+q=0\). Energy conservation follows from \(\frac{d}{dt}H=dH(X_H)=\omega(X_H,X_H)=0\). Cartan's formula implies \(\mathcal L_{X_H}\omega=d(\iota_{X_H}\omega)+\iota_{X_H}d\omega=d^2H=0\), so the flow preserves \(\omega\) and \(\omega^n/n!\).

On the oriented unit sphere with \(\omega=\sin\vartheta\,d\vartheta\wedge d\varphi\), \(X=\partial_\varphi\) satisfies \(\iota_X\omega=-\sin\vartheta\,d\vartheta=d(\cos\vartheta)\), so \(H=\cos\vartheta\). The area form is not exact because \(\int_{S^2}\omega=4\pi\ne0\), in contrast with any global exact two-form on a closed manifold. Darboux's theorem is local; it does not imply global exactness or global canonical coordinates.

##### Exercises with answers

1. **Oscillator.** With \(H=(p^2+4q^2)/2\), find Hamilton's equations. **Answer:** \(\dot q=p\), \(\dot p=-4q\).
2. **Conservation.** Explain why \(dH(X_H)=0\). **Answer:** It equals \(\omega(X_H,X_H)\), zero by antisymmetry.
3. **Spherical rotation.** Compute \(\iota_{\partial_\varphi}(\sin\vartheta\,d\vartheta\wedge d\varphi)\). **Answer:** \(-\sin\vartheta\,d\vartheta=d(\cos\vartheta)\).
4. **Global obstruction.** Why can the sphere's area form not equal \(d\alpha\) globally? **Answer:** Stokes' theorem would force its integral to vanish, but the area is positive.

##### Sources and further reading

- University of Toronto, [Symplectic Geometry lecture notes](https://www.math.toronto.edu/mein/teaching/LectureNotes/symplectic.pdf).
- MIT OpenCourseWare, [18.966 Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/).
- Overviews: [Symplectic manifold](https://en.wikipedia.org/wiki/Symplectic_manifold), [Hamiltonian mechanics](https://en.wikipedia.org/wiki/Hamiltonian_mechanics).

### Moment Maps: Symmetry, Conserved Quantities, and Reduction

**Track:** Topology and Geometry. **Background:** smooth manifolds, differential forms, group actions, Hamiltonian systems. **Central question:** when does a geometric symmetry have a numerical quantity that records its motion?

#### Mathematical companion (not spoken)

For a symplectic manifold \((M,\omega)\), adopt the convention \(\iota_{X_H}\omega=dH\). A symplectic circle action with generating vector field X is Hamiltonian if \(\iota_X\omega=d\mu\) for a globally defined function \(\mu:M\to\mathbf R\). Cartan's formula gives \(d(\iota_X\omega)=\mathcal L_X\omega-\iota_Xd\omega=0\) for a symplectic action, but exactness is an additional global condition.

On \(S^2\), \(\omega=\sin\theta\,d\theta\wedge d\phi\), \(X=\partial_\phi\), and
\[\iota_X\omega=-\sin\theta\,d\theta=d(\cos\theta).\]
Thus \(\mu=\cos\theta\) with this convention. On \(T^2=\mathbf R^2/\mathbf Z^2\), \(\omega=dx\wedge dy\), \(X=\partial_x\) gives \(\iota_X\omega=dy\), whose integral around the y-circle equals one; it is not exact.

For a Hamiltonian action of a compact Lie group G with equivariant moment map \(\mu:M\to\mathfrak g^*\), if \(0\) is a regular value and G acts freely and properly on \(\mu^{-1}(0)\), the reduced space \(M//G=\mu^{-1}(0)/G\) is symplectic, with \(\dim(M//G)=\dim M-2\dim G\). For nonzero levels one typically reduces by the stabilizer of the coadjoint value. Singular reductions require different language.

##### Exercises with answers

1. Compute the moment-map values at the north and south poles of the standard sphere. **Answer:** +1 and −1.
2. Why is translation on a flat torus not necessarily Hamiltonian? **Answer:** \(\iota_X\omega\) can represent a nonzero cohomology class even though it is closed.
3. What is the zero-level symplectic quotient of the standard sphere by rotation? **Answer:** a point, since the equator is one circle orbit.
4. What happens to dimension in a free regular reduction by a two-dimensional group? **Answer:** it drops by four.

##### Reading and source notes

- [University of Toronto, Symplectic Geometry lecture notes](https://www.math.toronto.edu/~mein/teaching/LectureNotes/symplectic.pdf), Hamiltonian group actions, moment maps, and reduction.
- [ETH Zurich, Geometry of the Moment Map (2026)](https://people.math.ethz.ch/~acannas/Teaching/Moment_Map_2026/), contemporary examples and geometric context.

### Almost-Complex Structures: Turning Symplectic Area into Length

**Track:** Topology and Geometry. **Background:** tangent vectors, differential forms, linear maps, symplectic two-forms. **Central question:** how can an antisymmetric area measurement be combined with a complex structure to define a positive metric?

#### Mathematical companion (not spoken)

Adopt the track convention \(\omega=dq\wedge dp\) and \(\iota_{X_H}\omega=dH\). On \(\mathbb R^2\), define \(J_0\partial_q=\partial_p\), \(J_0\partial_p=-\partial_q\). Then \(J_0^2=-I\), \(\omega(J_0v,J_0w)=\omega(v,w)\), and \(g(v,w)=\omega(v,J_0w)=v\cdot w\). More generally for \(a>0\), \(J_a=\begin{psmallmatrix}0&-a^{-1}\\a&0\end{psmallmatrix}\) in the ordered basis \((\partial_q,\partial_p)\), and \(g_a=\mathrm{diag}(a,a^{-1})\).

A compatible almost-complex structure satisfies \(J^2=-I\), \(\omega(Jv,Jw)=\omega(v,w)\), and \(\omega(v,Jv)>0\) for nonzero \(v\). A tame one only requires the final positivity in addition to \(J^2=-I\). A \(J\)-holomorphic map \(u:(\Sigma,j)\to(M,J)\) satisfies \(du\circ j=J\circ du\). For compatible \(J\) and a conformal metric on the domain, \(E(u)=\frac12\int_\Sigma |du|^2=\int_\Sigma u^*\omega\) for a \(J\)-holomorphic map, assuming suitable convergence if the domain is noncompact.

##### Exercises with answers

1. **Quarter turn.** Compute \(J_0^2\partial_q\). **Answer:** \(-\partial_q\).
2. **Scaled lengths.** What are \(g_a(\partial_q,\partial_q)\) and \(g_a(\partial_p,\partial_p)\)? **Answer:** \(a\) and \(a^{-1}\).
3. **Symmetry.** Why is \(g(v,w)=\omega(v,Jw)\) symmetric for compatible \(J\)? **Answer:** \(g(w,v)=\omega(w,Jv)=-\omega(Jv,w)=\omega(v,Jw)\) by compatibility and alternation.
4. **Scope.** Does existence of a compatible almost-complex structure imply the target is a complex manifold? **Answer:** no; integrability is an additional condition.

##### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), almost-complex geometry and compatibility.
- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), foundational monograph.
- [Almost complex manifold](https://en.wikipedia.org/wiki/Almost_complex_manifold); [Symplectic manifold](https://en.wikipedia.org/wiki/Symplectic_manifold).

### Darboux and Moser: Why Symplectic Forms Are Locally Simple

**Track:** Topology and Geometry. **Background:** forms and pullbacks, Lie derivatives, flows, cohomology, the symplectic plane. **Central question:** how can a differential equation transform one symplectic form into another?

#### Mathematical companion (not spoken)

Let \(\omega_t\) be a smooth family of symplectic forms on a compact manifold with constant de Rham class. Suppose \(\dot\omega_t=d\sigma_t\). Solve \(\iota_{X_t}\omega_t=-\sigma_t\), and let \(\phi_t\) be the flow of \(X_t\), \(\phi_0=\operatorname{id}\). Then
\[
\frac{d}{dt}\phi_t^*\omega_t=\phi_t^*(\dot\omega_t+\mathcal L_{X_t}\omega_t)=\phi_t^*(d\sigma_t+d\iota_{X_t}\omega_t)=0,
\]
using \(d\omega_t=0\). Hence \(\phi_t^*\omega_t=\omega_0\). The assertion requires a path remaining symplectic and a flow defined for the full time interval.

On \(S^2\), positive area forms of equal total area are cohomologous; their convex interpolation remains positive. For Darboux, choose coordinates in which \(\omega(0)=\omega_0\), put \(\omega_t=(1-t)\omega_0+t\omega\), shrink the neighborhood until all \(\omega_t\) are symplectic, and apply a local relative version of the argument. In higher dimensions, cohomology equality alone does not imply equivalence of arbitrary symplectic forms.

##### Exercises with answers

1. **Necessity.** Why do pulled-back area forms on a compact oriented surface have equal total area? **Answer:** change of variables for top-degree forms.
2. **Moser equation.** What vector field equation cancels \(\dot\omega_t=d\sigma_t\)? **Answer:** \(\iota_{X_t}\omega_t=-\sigma_t\).
3. **Global obstruction.** Why can a positive area form on \(S^2\) not be globally exact? **Answer:** Stokes would force its positive total area to vanish.
4. **Limitation.** Is every convex combination of symplectic forms in dimension four symplectic? **Answer:** no; nondegeneracy may fail in between.

##### Sources and further reading

- Jürgen Moser, [On the Volume Elements on a Manifold](https://doi.org/10.1090/S0002-9947-1965-0182927-5), *Transactions of the AMS* 120 (1965), 286–294; source of the moving-volume-form method.
- Dusa McDuff and Dietmar Salamon, [Introduction to Symplectic Topology](https://global.oup.com/academic/product/introduction-to-symplectic-topology-9780198794905), Darboux and Moser arguments.
- [Darboux's theorem](https://en.wikipedia.org/wiki/Darboux%27s_theorem_(symplectic_geometry)); [Moser's theorem](https://en.wikipedia.org/wiki/Moser%27s_trick).

### Lagrangian Geometry: Graphs, Intersections, and Exactness

**Track:** Topology and Geometry. **Background:** differential forms, cotangent bundles, symplectic Hamiltonian flow, gradients. **Central question:** why do critical points of a function become intersections of two geometric submanifolds?

#### Mathematical companion (not spoken)

On \(T^*Q\), use local canonical coordinates \((q_i,p_i)\), \(\omega=\sum_i dq_i\wedge dp_i\), and \(\lambda=-\sum_i p_i dq_i\), so \(d\lambda=\omega\). If \(\alpha=\sum_i a_i(q)dq_i\), the graph of \(\alpha\) pulls back \(\omega\) to \(-d\alpha\). Therefore \(\Gamma_\alpha\) is Lagrangian iff \(d\alpha=0\), and it is exact when \(\alpha=df\) because \(\lambda|_{\Gamma_{df}}=-df\). The zero section is \(\Gamma_0\).

At \(q\in Q\), \(\Gamma_{df}\cap\Gamma_0\) means \(df_q=0\). Linearizing \(df\) shows that transversality at the intersection is equivalent to nondegeneracy of \(\mathrm{Hess}_q f\). On \(S^1=\mathbb R/\mathbb Z\), \(f(q)=\cos(2\pi q)\) has exactly two such intersections. The graph \(p=c\neq0\) is a closed nonexact Lagrangian; \(\int_{S^1}c\,dq=c\neq0\).

For a compatible \(J\)-holomorphic disk \(u:(D,\partial D)\to(M,L)\) with \(\omega=d\lambda\) and \(\lambda|_L=df\), \(E(u)=\int_Du^*\omega=\int_{\partial D}u^*df=0\), hence \(u\) is constant. No compactness at infinity is implied.

##### Exercises with answers

1. **Lagrangian graph.** Why is \(\Gamma_{df}\) Lagrangian? **Answer:** \(d(df)=0\).
2. **Intersections.** How many transverse intersections do the zero section and \(\Gamma_{d\cos(2\pi q)}\) have? **Answer:** two, at \(q=0\) and \(q=1/2\).
3. **Closed versus exact.** Why is \(c\,dq\) on the circle not exact for \(c\neq0\)? **Answer:** it has nonzero integral around the circle.
4. **No disks.** Why is every compatible holomorphic disk with boundary on a compact exact Lagrangian in an exact symplectic manifold constant? **Answer:** Stokes and exactness give zero area, hence zero energy.

##### Sources and further reading

- Andreas Floer, [Morse Theory for Lagrangian Intersections](https://doi.org/10.4310/JDG/1214442477), *Journal of Differential Geometry* 28 (1988), 513–547.
- Michael Hutchings, [Floer Theory course](https://math.berkeley.edu/~hutching/teach/277-2008/index.html), intersection and holomorphic-curve prerequisites.
- [Cotangent bundle](https://en.wikipedia.org/wiki/Cotangent_bundle); [Lagrangian submanifold](https://en.wikipedia.org/wiki/Lagrangian_submanifold).
