# Contact boundaries, wrapping, and embedding obstructions

<!-- BEGIN SPOKEN LECTURE -->

# Contact boundaries, wrapping, and embedding obstructions

## Contact Forms and Reeb Flows: Dynamics on an Odd-Dimensional Boundary

A symplectic manifold has even dimension because its defining nondegenerate two-form pairs directions in twos. But the boundary of a compact symplectic region has odd dimension. What geometry can survive there? In many important cases, the answer is contact geometry: a maximally twisting family of hyperplanes, together with a distinguished direction of motion called the Reeb field.

This is the language of characteristic trajectories on energy surfaces, of symplectic filling problems, and of the periodic orbits counted by embedded contact homology.

### Start with planes that cannot fit together into surfaces

In ordinary three-space, imagine assigning a two-dimensional plane of permitted directions at every point. If those planes were horizontal everywhere, we could stack them into ordinary surfaces of constant height. Contact geometry begins with a different possibility: the planes twist as we move, so they cannot locally be the tangent planes of a family of surfaces.

A one-form alpha can describe a plane at each point by declaring that its kernel consists of the permitted directions. For a concrete model use coordinates x, y, z and define alpha to be d z minus y times d x. The permitted vectors have z component equal to y times their x component. The plane tips as y changes. Its two convenient spanning directions are the x direction plus y times the z direction, and the y direction.

Take the exterior derivative of alpha. It is d x wedge d y. This form measures area in the x-y directions. The three-form alpha wedge d alpha is d z wedge d x wedge d y, a nonzero volume form. Therefore this one-form defines a contact structure.

In general, on a manifold of dimension two n plus one, the contact condition says alpha wedged with n copies of d alpha is nowhere zero. It ensures that d alpha is nondegenerate when restricted to the hyperplane distribution given by the kernel of alpha. The form alpha is a contact form, and the hyperplane field is the underlying cooriented contact structure.

Contrast alpha equals d z. Its exterior derivative is zero. The kernel consists of horizontal planes that really do fit together into surfaces. It is not a contact form. The distinction is not whether a plane field exists; it is how strongly it twists.

### Find the direction that contact planes do not determine

A contact form determines a unique vector field R called the Reeb field. It satisfies two equations. First alpha of R equals one. Second, inserting R into d alpha gives zero in every direction. These conditions pick the motion direction left over after the contact planes have been equipped with their nondegenerate two-form.

For our model alpha equals d z minus y d x, the z coordinate vector field is the Reeb field. The contact form evaluates it to one, and d alpha, which uses only d x and d y, evaluates it to zero against any other vector. Thus Reeb trajectories are lines moving straight in the z direction.

On all of three-space those lines do not close. If the z coordinate is instead periodic, they become closed loops. The example shows why local differential equations alone do not decide whether a Reeb trajectory is periodic. Global topology matters.

### Periods become integrals

Consider a Reeb trajectory that closes after time T, where Reeb time is normalized by alpha of R equals one. Integrating alpha along the trajectory gives the integral over time of alpha evaluated on R. That integrand is one, so the result is T. The action of a closed Reeb orbit, measured by the contact form, equals its period.

This relation provides an action scale for dynamics on contact manifolds. When we later build Hamiltonians near a cylindrical symplectic end, the slopes of those Hamiltonians interact with these Reeb periods. New periodic orbits can appear precisely when the radial Hamiltonian motion matches an appropriate Reeb period.

Rescaling the contact form can change the Reeb field and the periods. If we multiply alpha by a positive constant, the Reeb field scales by the reciprocal constant. For a nonconstant positive rescaling, the new Reeb field generally acquires a component inside the contact planes as well. The hyperplane distribution stays the same, but the parametrized dynamics need not.

### Contact geometry is not just lower-dimensional symplectic geometry

A contact structure does not possess a nondegenerate two-form on its whole odd-dimensional tangent space. Instead, d alpha is nondegenerate only on the contact hyperplanes. The Reeb direction is singled out by its complementary role. This is why a contact manifold naturally couples a plane distribution with a flow, whereas a symplectic manifold starts from a nondegenerate two-form on every tangent direction.

Contact geometry also carries local flexibility. Darboux's theorem for contact manifolds says contact structures have a standard local model, just as symplectic forms do. Yet the global Reeb dynamics can be highly constrained and can distinguish contact manifolds, contact forms, and their fillings.

A Reeb orbit is not the same thing as an arbitrary closed curve. It must solve the Reeb ordinary differential equation. In three dimensions, embedded contact homology builds algebraic generators from appropriate collections of Reeb orbits, with multiplicities and admissibility conditions. The index and holomorphic-curve counts belong to the later theory. Before encountering them, it matters to understand exactly where those orbit generators come from.

Our concrete contact form has shown every essential local ingredient: a twisting plane field, a nondegenerate area form on those planes, and a uniquely normalized transverse flow. The next question is how a contact manifold arises as the boundary of a symplectic domain and how the boundary can be stretched into a noncompact end.

## Liouville Domains and Completions: Turning a Boundary into Infinity

A compact symplectic region has a boundary. Many Floer-theoretic problems, however, need a noncompact space on which Hamiltonian trajectories may travel farther and farther out. A Liouville completion provides a controlled way to attach an infinite cylindrical end. The crucial point is that the added infinity has a simple formula rather than arbitrary geometry.

### An exact symplectic form has a primitive

A symplectic form omega is a closed, nondegenerate two-form. If it can be written globally as the exterior derivative of a one-form lambda, we call the symplectic manifold exact. The one-form lambda is a primitive of omega. Exactness is a global property; a symplectic form always has local primitives on sufficiently simple coordinate neighborhoods, but may lack a global primitive.

For a cotangent bundle, the geometry supplies a preferred primitive. In the position-momentum coordinates used in our track, omega is d q wedge d p and lambda is minus p d q. Differentiating lambda gives d q wedge d p. Different texts often choose the opposite convention for omega and lambda. We retain this pair so the Hamiltonian convention and action formula remain consistent with the earlier lectures.

A vector field Z is called Liouville if inserting it into omega gives lambda. By the Cartan formula, the flow of Z expands omega: its Lie derivative along Z equals omega. Thus Liouville flow rescales the symplectic structure rather than preserving it. In cotangent coordinates, Z points radially outward in the momentum directions.

### A Liouville domain

A Liouville domain is a compact manifold with boundary, equipped with a one-form lambda such that omega equals d lambda is symplectic and its Liouville vector field points strictly outward along the boundary. Outward transversality is the condition that lets us regard the boundary as the entrance to a radial end.

Restrict lambda to the boundary and call the resulting one-form alpha. This is a contact form. To understand why, notice that the Liouville vector field is transverse to the boundary. Contracting the nonvanishing top symplectic volume form with that outward direction gives a nonvanishing volume form on the boundary. Up to a positive scale, the resulting expression is alpha wedged with the appropriate number of copies of d alpha. That is precisely the contact condition.

In other words, a boundary of contact type carries a contact structure because the ambient exact symplectic geometry supplies a preferred normal scaling direction and a nondegenerate area form on the remaining tangent hyperplanes.

### The collar formula

Follow the Liouville vector field outward from the boundary. Introduce a radial coordinate r which equals one on the original boundary and grows along this flow. The primitive on the collar has the form r times alpha. Taking its exterior derivative produces two terms: d r wedge alpha and r times d alpha. This simple formula is the basis of the completion.

Attach a half-infinite end consisting of boundary points and radial values greater than or equal to one. Keep lambda equal to r alpha and omega equal to its exterior derivative there. The resulting noncompact exact symplectic manifold is the completion of the Liouville domain. Its infinity is not featureless. Each large-radius slice carries a scaled copy of the same contact structure, and the Reeb dynamics on the boundary remain visible.

This is why Liouville completions are natural for wrapped Floer theory. A Hamiltonian that grows with r acquires a predictable vector field along the Reeb direction. We can relate new periodic Hamiltonian trajectories and Lagrangian chords to Reeb orbits and chords on the original contact boundary.

### The cotangent disk as a model

Let Q be a closed smooth manifold with a Riemannian metric. Its cotangent bundle consists of all covectors attached to points of Q. Use the metric to define the norm of a covector. The disk cotangent bundle is the part where that norm is at most one. Its boundary is the unit cotangent bundle. With the canonical primitive and symplectic form, this disk bundle is a Liouville domain: radial scaling of covectors points outward at norm one.

Its completion is the full cotangent bundle. Every covector of length greater than one lies on the attached radial end. This correspondence explains why wrapped Floer homology of a cotangent fiber can recover information about paths or loops in Q. The relevant Hamiltonian motion is able to explore large momenta, but the geometry there is organized by the contact dynamics of unit covectors.

For the circle Q, the unit cotangent boundary has two components, corresponding to positive and negative momentum. The Reeb directions on these components point in opposite coordinate directions under our sign convention. The completed cotangent cylinder contains all momentum values, so trajectories can wind in either direction around the base circle. Both windings matter in the based-loop calculation.

### Exactness controls energy, not everything

Exactness has a powerful analytic consequence. If a closed surface is mapped into an exact symplectic manifold, the integral of the pulled-back symplectic form is zero by Stokes' theorem. A nonconstant compatible holomorphic sphere would have positive area, so it cannot exist in an exact symplectic manifold. This removes one important source of sphere bubbling in Floer compactness arguments.

But exactness by itself does not prevent trajectories from escaping to infinity. The completed manifold is noncompact. To control solutions of the Floer equation, one also needs appropriate Hamiltonians, almost-complex structures, and boundary or asymptotic conditions. A maximum principle or no-escape lemma supplies this additional control in settings where its hypotheses hold.

The distinction is worth preserving. Exactness gives algebraic control of symplectic area and suppresses certain bubbles. Cylindrical geometry gives a structured end. Analytic estimates then show which trajectories stay in a compact region. Wrapped Floer theory depends on all three pieces, not on any one of them in isolation.

A Liouville completion is therefore more than a convenient way to remove the boundary from a picture. It turns contact dynamics at a finite boundary into symplectic dynamics at a controlled infinity, while retaining a primitive that makes action and energy estimates possible.

## Wrapping Hamiltonians and No-Escape Estimates

Wrapped Floer homology deliberately uses Hamiltonian flows that travel far into a noncompact symplectic manifold. That is the whole point of wrapping. But to count trajectories reliably, we must also stop solutions of the Floer differential equation from escaping without control. The central idea is to choose Hamiltonians whose growth near infinity is simple enough that Reeb dynamics and a maximum principle govern what happens.

### Radial Hamiltonians see Reeb flow

Take the cylindrical end of a Liouville completion. It has a radial coordinate r, a contact form alpha on each boundary slice, and symplectic form equal to the exterior derivative of r alpha. Choose a Hamiltonian depending only on radius: H equals h of r.

Its derivative points in the radial direction. The Hamiltonian vector field must therefore point along the complementary Reeb direction. Let us check the sign rather than guessing. Our track defines the Hamiltonian vector field by inserting it into omega to obtain d H. On the cylindrical end, omega pairs the Reeb field with the outward radial direction to give minus one. Consequently, X H equals minus h prime of r times the Reeb field.

Some texts define the Hamiltonian vector field using the negative of d H and obtain the opposite Reeb orientation. Both conventions are valid when the definitions of action and Floer equations change consistently. We will keep the minus sign in this paragraph to match the earlier geometry lectures.

If a radial level is stationary under the Hamiltonian flow, its motion is a reparametrized Reeb trajectory. One-periodic Hamiltonian orbits on that level correspond to Reeb orbits whose period matches the absolute value of the slope h prime. For a slope that avoids the relevant Reeb periods, the cylindrical region has no such one-periodic Hamiltonian orbits.

### A circle example where the sign can be checked

Consider the cotangent bundle of the circle, with angle q taken modulo two pi and momentum p. Keep lambda equal to minus p d q and omega equal to d q wedge d p. On the positive-momentum end, r equals p and alpha is minus d q on the unit boundary. Its Reeb field is minus the q direction, whose closed orbits have period two pi.

Take H equal to a times p on that end, for a positive constant a. Hamilton's equations, in our convention, give q dot equals a and p dot equals zero. A trajectory closes after one unit of time only when a is an integer multiple of two pi. The cylindrical formula agrees: X H is minus a times the Reeb field, which is plus a times the q direction.

Choose a slope a that is not a multiple of two pi. Then this end has no new one-periodic Hamiltonian orbit. Increase the slope past successive multiples of two pi, and families of Reeb-related periodic trajectories appear in the unperturbed radial model. A small time-dependent perturbation is used where necessary to achieve nondegeneracy. This is how increasing Hamiltonians detect more winding classes.

### Action is a second filter

In an exact symplectic manifold, our convention for Hamiltonian action is minus the integral of lambda along the orbit, minus the time integral of H. For a radial one-periodic Hamiltonian orbit on the cylindrical end, lambda of X H equals minus r times h prime. Hence the action is r times h prime minus h, evaluated at the orbit's radius.

If h is exactly linear, with slope a and intercept b, this value is minus b. If h is convex in a transition region, the relationship between radius, slope and action can distinguish orbits arising at different levels. Action filtrations make infinite collections of generators manageable, but they do not by themselves prove all required compactness statements.

For Hamiltonian chords with Lagrangian endpoints, one also includes primitives of lambda on the exact Lagrangians and endpoint conventions. The basic radial relation still identifies wrapping chords near infinity with appropriately oriented Reeb chords. This is the geometric bridge from contact boundary dynamics to wrapped Lagrangian intersections.

### Why a maximum principle is needed

Consider a Floer cylinder solving the negative-gradient equation for Hamiltonian action. Even if its incoming and outgoing periodic orbits lie in a compact region, why must the entire connecting cylinder stay near them? In a noncompact target, there is no automatic answer. A sequence of solutions might travel arbitrarily far out before returning, preventing compactness of the moduli space.

On a cylindrical end, choose an almost-complex structure of contact type. In logarithmic radial coordinate s, the complex structure pairs the outward radial direction with the Reeb direction, and it respects the contact planes. For an unperturbed holomorphic curve, the logarithmic radius becomes a subharmonic function. Roughly, its Laplacian is a nonnegative measure of the curve's derivative in the contact planes. A nonconstant subharmonic function cannot have a strict interior maximum.

This is the analytic heart of a no-escape argument. With suitable radial Hamiltonians, cylindrical almost-complex structures and compatible asymptotic or Lagrangian boundary conditions, related maximum principles show that a Floer solution whose ends lie inside a certain radial level cannot push out past that level. The exact hypotheses differ between periodic-orbit Floer theory and wrapped Lagrangian Floer theory, and between Hamiltonians that are linear or more general at infinity. It would be incorrect to claim that every convex Hamiltonian and every almost-complex structure automatically gives such a bound.

### A local proof idea

For a holomorphic map into the symplectization, write the cylindrical coordinate as s and the map's contact-manifold component as v. The holomorphic equation relates the derivative of s in one domain direction to alpha of the derivative of v in the perpendicular direction. Differentiate once more and combine the identities. The resulting Laplacian of s is d alpha of a contact-plane derivative with its image under the compatible complex structure. Positivity of that pairing gives nonnegativity of the Laplacian.

The argument relies on the particular cylindrical geometry; it is not just a generic consequence of being symplectic. For Hamiltonian-perturbed equations, additional terms appear, so restrictions on the radial profile and the end structure matter. This is why serious treatments state a maximum principle as a lemma with hypotheses instead of a slogan.

### The two limiting procedures

Wrapped Floer theory uses a collection of Hamiltonians with increasingly large admissible slopes and continuation maps between the corresponding Floer complexes. At each stage, no-escape and compactness estimates keep the moduli problems under control. Then a directed limit captures information from arbitrarily large wrapping without asking us to count an uncontrolled infinite moduli space in one step.

The cotangent circle again gives the intuition. Larger slopes can see more loops with positive or negative winding. The resulting wrapped theory of a cotangent fiber has generators corresponding to all integer winding classes. Its relation to the based loop space is a global theorem requiring the appropriate Floer-theoretic hypotheses, not a mere consequence of counting slopes.

Contact geometry tells us which trajectories are available at the end. Radial Hamiltonians turn those trajectories into periodic or chord generators. Action and energy organize the counts. A maximum principle prevents loss of compactness by uncontrolled radial escape. These are the missing mechanics behind the phrase 'wrap the Lagrangian toward infinity.'

## Wrapped Floer Homology and Symplectic Cohomology

Imagine two Lagrangian submanifolds inside a symplectic manifold. Their intersections are the starting points for a version of Floer theory. A differential counts certain solutions of a nonlinear elliptic equation connecting intersection points. Under suitable compactness and transversality conditions, the homology carries information that survives Hamiltonian deformations.

That construction works especially naturally in compact settings. But many symplectic spaces of central interest are noncompact. A cotangent bundle, for example, extends indefinitely in momentum directions. Its fiber over one base point is also noncompact. Two copies of that fiber may intersect at one point, yet the ambient geometry contains an entire space of based loops that the single intersection cannot reveal.

Wrapped Floer theory changes the problem deliberately. Instead of forbidding the Lagrangians from exploring infinity, it allows Hamiltonian dynamics that grow appropriately toward infinity. New Hamiltonian chords appear, and their homology captures information invisible to the most literal intersection count.

## The symplectic geometry of a cotangent bundle

Let Q be a smooth closed manifold. Its cotangent bundle consists of all covectors attached to points of Q. It carries a canonical one-form and a symplectic form obtained by differentiating that one-form. These are not arbitrary choices; they come from the very definition of cotangent vectors.

A cotangent fiber is the set of all covectors over one fixed point. It is a Lagrangian submanifold, meaning the symplectic form restricts to zero on it and its dimension is half the dimension of the cotangent bundle.

Take a Hamiltonian that grows with momentum. Its trajectories project to paths in Q, and chords whose endpoints lie on the fixed cotangent fiber correspond, under standard kinetic Hamiltonians and appropriate nondegeneracy conditions, to based paths that start and end at the selected point. Such a path is a based loop.

This observation is the geometric clue behind the comparison between wrapped Floer homology of a cotangent fiber and homology of the based loop space of Q. The wrapped generators are not just points of intersection. They encode paths with different winding or homotopy behavior.

## A circle gives infinitely many generators

Take Q to be a circle. Fix a base point. A based loop may go around the circle zero times, once in the positive direction, once in the negative direction, or any integer number of times. The winding number classifies its based homotopy class.

The based loop space of a circle therefore has connected components indexed by all integers. Each component is contractible. Its degree-zero homology has one generator for every integer and can be described as the group ring of the integers, or Laurent polynomials in a symbol t and its inverse.

The wrapped Floer cohomology of a cotangent fiber in the cotangent bundle of the circle recovers this structure, with appropriate grading and coefficient conventions. That is a dramatic improvement over the naive picture of a single fiber intersecting itself at one point.

The infinite collection of wrapped generators does not mean that the resulting theory has lost control. The generators are filtered by Hamiltonian action, and the differential counts solutions with energy estimates. Taking a directed limit over larger Hamiltonian slopes reveals successively more of the noncompact geometry.

## Why the word wrapped is literal

On a Liouville manifold, there is a natural radial direction near infinity. The Hamiltonian flow winds a Lagrangian along this end. A wrapping Hamiltonian is chosen to grow so that new chords are created in a controlled manner.

One then forms a Floer complex from these chords, counts rigid Floer strips as the differential, and uses continuation maps to compare different choices of wrapping Hamiltonian. The wrapped Floer homology is obtained through an appropriate direct limit or an equivalent cofinal construction.

The maximum principle and exactness conditions help keep relevant Floer trajectories from escaping uncontrollably to infinity. Without such analytic controls, an infinite collection of chords could become an ill-defined counting problem. Wrapped Floer theory is not simply “count everything at infinity.” It is an organized limit of well-posed chain complexes.

The precise foundations depend on exactness, grading, orientations, coefficients, stops or boundary conditions, and on the ambient symplectic category. A result proved for exact cotangent bundles should not be casually transferred to arbitrary nonexact symplectic manifolds.

## A product hides in the loop-space comparison

Floer homology often supports more than a vector-space structure. In the wrapped setting, one can compose chords using operations defined by holomorphic polygons. At the chain level, these operations organize into an A-infinity algebra or category.

On based loops, there is a natural operation: concatenate two loops that share a base point. Under suitable hypotheses, the wrapped algebra of a cotangent fiber matches chains on the based loop space with this concatenation-type product, up to the appropriate homotopical structures.

For the circle, winding numbers add under concatenation. A loop with winding three followed by one with winding minus one has winding two. The corresponding Laurent monomials multiply in the obvious way. This makes the topology visible directly in the algebra.

We should distinguish an isomorphism of graded homology groups from an equivalence of chain-level algebraic structures. The latter is a stronger statement and requires care with higher products, gradings, and signs. The underlying homology calculation is the accessible entrance, not the whole theorem.

## From one Lagrangian to the ambient manifold

Wrapped Floer theory is centered on noncompact Lagrangian objects. Symplectic cohomology is a related invariant of the noncompact symplectic manifold itself. Its generators are periodic Hamiltonian orbits rather than chords with Lagrangian endpoints.

The same wrapping philosophy appears. We use Hamiltonians with prescribed behavior at infinity, build Floer complexes, and pass to a limit. On cotangent bundles, symplectic cohomology is related to the homology of the free loop space, where loops no longer have a fixed base point.

The distinction is instructive. Based loops correspond to cotangent-fiber endomorphisms. Free loops correspond to the ambient Hamiltonian periodic-orbit problem. These constructions are related by deep open–closed maps and categorical structures, but their generators and algebraic operations are different.

## What wrapping can detect

An invariant of a noncompact symplectic manifold should be sensitive to its geometry at infinity. Wrapped Floer theory and symplectic cohomology accomplish this in a controlled way. They can distinguish symplectic spaces with similar ordinary topology, provide obstructions to certain fillings, and test generation statements for Fukaya categories.

The circle calculation is a miniature model of the broader principle. A cotangent fiber is locally simple, but its interaction with Hamiltonian trajectories encodes all the based loops of the underlying manifold. Allowing controlled motion at infinity converts local intersection information into global loop-space topology.

This is why wrapped Floer theory belongs simultaneously to symplectic geometry, algebraic topology, and categorical algebra. Its analytic foundation consists of solutions to differential equations; its generators come from Hamiltonian dynamics; and its answer can be the homology of an infinite-dimensional space of loops.

## Symplectic Nonsqueezing: A Constraint That Volume Cannot See

Imagine a ball in four-dimensional phase space. We are allowed to deform it by smooth transformations that preserve the symplectic form. Such transformations preserve the associated volume. One might therefore guess that every rearrangement compatible with volume is possible. If a target region has more than enough volume, why should the ball fail to fit?

Now choose a target shaped like a cylinder. In one position-momentum coordinate pair, the cylinder is a disk of radius R. In every other pair, it extends without bound. Its total volume is infinite. No ordinary volume argument can prevent a finite ball of radius r from fitting inside it, regardless of how small R is.

Gromov's nonsqueezing theorem says something much stronger than volume preservation. A symplectic embedding of the ball into this cylinder exists only when the ball radius is no larger than the cylinder radius. A ball with radius two cannot be squeezed through a symplectic cylinder of radius one, even though the cylinder is unbounded in all other directions.

This is a genuinely multidimensional obstruction. In a single position-momentum plane, area preservation already supplies the relevant bound. In four or more dimensions, a two-dimensional area restriction survives despite all the additional directions into which volume might be redistributed.

## The cylinder must use a conjugate pair

The statement is precise about which coordinates form the narrow disk. The disk is measured in one conjugate pair, such as a position coordinate q one and its matching momentum coordinate p one. The standard symplectic form is the sum of each dq wedged with its corresponding dp.

Why does that pairing matter? A symplectic linear map can shrink a position coordinate if it expands its conjugate momentum by the reciprocal factor. The product of the two scale factors remains one, preserving the two-form in that pair.

Thus ordinary narrowing in position space is perfectly possible. A linear map sending q to a small multiple of q and p to the reciprocal large multiple of p is symplectic. It turns a disk into a long ellipse of the same area. But the ellipse cannot lie inside a smaller disk in that conjugate plane. The nonsqueezing theorem says that even elaborate nonlinear symplectic maps cannot evade the underlying obstruction by trading distortion with the other coordinate pairs.

If the target were narrow only in two position coordinates rather than one conjugate position-momentum pair, the simple scaling trick could fit the ball. Symplectic nonsqueezing is not a universal prohibition on making shapes narrow. It is a prohibition on squeezing their symplectic two-dimensional size.

## Why volume is not the whole geometry

Symplectic geometry begins with a closed nondegenerate two-form. In dimension two n, its n-fold wedge product determines a volume form. Every symplectomorphism preserves that volume. The converse is false: volume-preserving maps need not preserve the symplectic form.

So there is more structure to preserve than a single number associated with volume. The surprising part of Gromov's theorem is that preserving a two-form pointwise implies a global embedding obstruction. Local linear algebra alone does not prove the nonlinear statement.

An intuitive strategy for understanding the theorem uses holomorphic curves. Choose an almost complex structure compatible with the symplectic form. Certain pseudoholomorphic curves carry an energy equal to symplectic area. Their existence and monotonicity properties constrain how a ball may sit inside a cylinder.

Very roughly, one constructs a curve in an appropriate compactification of the cylinder, arranges for it to meet the embedded ball, and compares an upper bound from the cylinder's disk area with a lower bound forced by the ball. The resulting inequality is that pi times r squared cannot exceed pi times R squared. This is a proof strategy, not an elementary derivation from volume alone. The analytic existence and compactness results for those curves are the deep part.

## Capacities assign numbers to symplectic domains

The nonsqueezing theorem motivated the development of symplectic capacities. A capacity assigns a nonnegative size, possibly infinite, to symplectic domains. It must be monotone under symplectic embeddings and scale correctly when the symplectic form is multiplied by a positive factor.

A normalized capacity assigns the same standard value to a ball of radius r and a cylinder of radius r: pi times r squared. These domains have drastically different volumes. The capacity measures the kind of size relevant to symplectic embeddings, not ordinary spatial occupancy.

If a symplectic embedding carried a larger ball into a smaller cylinder, monotonicity of capacity would require its capacity to be no larger than the cylinder's capacity. But that would mean pi times r squared is no larger than pi times R squared. For r greater than R this is impossible.

One capacity, called the Gromov width, is defined by asking for the largest symplectic ball that can embed into a given domain and recording the corresponding area. Other capacities capture additional embedding obstructions. In four dimensions, a sequence of embedded contact homology capacities can distinguish some domains that have the same volume and even similar simpler capacity measurements.

## A worked comparison of two proposed embeddings

Take a four-dimensional ball of radius three and a cylinder whose first conjugate pair lies in a disk of radius two. The cylinder is infinite in the second pair. Despite this infinite volume, no symplectic embedding exists because the ball's capacity is nine pi and the cylinder's normalized capacity is four pi.

Now take a ball of radius one and a cylinder of radius two. There is an obvious embedding: put the ball inside the cylinder without distorting it at all. The theorem asserts no obstruction in that direction; the identity inclusion works.

Notice that the ball radius is a geometric parameter in the standard Euclidean coordinates. Under arbitrary symplectic transformations, ordinary Euclidean radii and lengths are not preserved. The invariant is the capacity, not the radius of a particular image shape.

## Rigidity is compatible with flexibility

Darboux's theorem says every symplectic manifold is locally symplectomorphic to standard phase space. That is a powerful local flexibility statement: symplectic manifolds have no local curvature invariant analogous to the curvature of a Riemannian metric.

Nonsqueezing is a global statement about finite-size embeddings. There is no contradiction between the two. Being able to straighten the symplectic form in a small neighborhood does not mean one can fit a large ball through every thin global region.

The resulting picture is central to modern symplectic topology. Hamiltonian dynamics preserves volume, but also preserves stronger geometric constraints. Holomorphic curves and symplectic capacities reveal those constraints. What looked like a problem of packing volume becomes a problem of preserving the area structure of conjugate coordinate pairs.

## ECH Capacities and Symplectic Embedding Staircases

In ordinary geometry, two objects may be reshaped to fit one inside another when enough room exists. In symplectic geometry, a map must preserve a specific two-form. This forces constraints that volume alone cannot detect.

Gromov's nonsqueezing theorem gives a first example. A four-dimensional ball of one symplectic capacity cannot be embedded symplectically into a cylinder whose cross-sectional disk has smaller capacity, even if the cylinder extends infinitely far in the other directions. The cylinder has infinite volume, so the obstruction cannot be a shortage of total space.

Embedded contact homology capacities, usually abbreviated ECH capacities, turn this qualitative rigidity into an infinite sequence of numerical tests in four dimensions. A symplectic embedding of suitable domains forces every capacity of the source to be at most the corresponding capacity of the target. The resulting sequence can rule out an embedding even when simpler volume and nonsqueezing inequalities do not.

## Standardize the units before comparing shapes

A symplectic ellipsoid in four dimensions can be specified by two positive parameters, often written a and b. Each parameter has units of symplectic area. The ellipsoid consists of complex coordinate pairs whose normalized squared radii sum to at most one.

When a equals b, the ellipsoid is a ball. The notation is designed so that the ball parameter is its two-dimensional capacity, not its geometric radius. Confusing those conventions is an easy way to produce factors of pi in the wrong place.

The symplectic volume of the ellipsoid is one-half the product of its two area parameters. For a ball of capacity c, the volume is one-half c squared. Any volume-preserving embedding of the ellipsoid into the ball therefore requires c at least the square root of a times b.

That is a necessary condition, not a constructive proof that such an embedding exists. Symplectic maps preserve more than volume, and their extra restrictions are where capacity sequences become useful.

## Build the capacity sequence of an ellipsoid

For a four-dimensional ellipsoid, its ECH capacities are found by listing all nonnegative integer combinations of a and b, including zero, arranging them in nondecreasing order, and keeping repeated values. The zeroth capacity is zero. The first positive capacity is the smaller of a and b.

Take an ellipsoid with parameters one and four. The ordered list begins zero, one, two, three, four, four, five, and so on. The repeated four comes from two different ways of forming the same area value: four copies of the first parameter or one copy of the second.

For a ball of capacity c, the two parameters both equal c. Its sequence begins zero, c, c, two c, two c, two c, three c, and so forth. Again, repetitions are real data, not duplicate entries to discard.

If the ellipsoid is to embed into the ball, every entry in the first list must be at most the corresponding entry in the second. For instance, comparing the fourth entries, counting from zero, requires three to be at most two c, giving c at least one and a half. This inequality is weaker than the volume bound of two in this example. Other pairs of ellipsoids and balls produce capacity inequalities that are genuinely stronger than volume.

The example illustrates how the calculation works while also guarding against overstatement. One numerical capacity check might be redundant, but the full sequence can still encode a sharp obstruction.

## Where the capacities come from

Embedded contact homology is built from Reeb orbits on the boundary of a suitable symplectic domain. Reeb dynamics arise from a contact form, which appears naturally on the boundary of a star-shaped Liouville domain.

A chain complex is generated by specified orbit sets, and its differential counts holomorphic curves satisfying an index condition. The capacities record action thresholds needed to represent distinguished homology classes. This is why the resulting numbers can be interpreted as successive amounts of symplectic action available in the domain.

The algebraic definition is intricate. But for ellipsoids, explicit Reeb dynamics simplify the answer to the sorted-integer-combination rule. This explicit formula is a major reason ECH capacities are effective in embedding problems.

Monotonicity is the critical theorem. If a suitable four-dimensional domain embeds symplectically into another, then its entire capacity sequence is bounded term by term. One must keep track of whether domains are open or closed and whether the embedding lands in the interior when using strict inequalities or limiting arguments.

## The staircase phenomenon

Now vary the shape of an ellipsoid while keeping one parameter fixed. Ask for the smallest ball capacity into which it can symplectically embed. The volume constraint gives a smooth square-root lower bound. Capacity constraints introduce a second kind of behavior: different inequalities dominate at different parameter values.

In a celebrated four-dimensional ellipsoid-into-ball problem, the optimal embedding function has an infinite staircase over an interval of shape parameters. Pieces of the graph are determined by distinct capacity obstructions, with an accumulation point related to powers of the golden ratio.

This is not a generic property of all symplectic embedding problems. The precise staircase is a theorem for a specific four-dimensional family, built on deep embedding and capacity results. It demonstrates how integer lattice arithmetic can control the geometry of continuous regions.

The staircase has a striking interpretation. As an ellipsoid's aspect ratio changes continuously, the most restrictive holomorphic-curve obstruction can switch discretely. Continuous geometry is governed by an ordered sequence of integer combinations.

## Why four dimensions matter

ECH capacities are particularly powerful in four-dimensional symplectic geometry. Their construction uses three-dimensional contact boundaries and the special analytic structure available there. Some embedding problems in higher dimensions admit other capacities and obstructions, but the ellipsoid formula and four-dimensional sharpness results should not be presented as a universal algorithm for arbitrary dimension.

Even in four dimensions, satisfying every ECH capacity inequality is not automatically sufficient for an arbitrary pair of domains. Sufficiency has been proved in important specific cases, including ellipsoid-to-ellipsoid embeddings, using additional geometric results. A necessary obstruction is not generally a recipe for constructing an embedding.

This distinction parallels many problems in mathematics. An invariant can prove impossibility with one violated inequality, while existence may demand an entirely different construction. In symplectic geometry, capacities are especially valuable because failure of a single inequality can settle a problem conclusively.

## A practical way to reason about embeddings

Given an ellipsoid and a target ball, first fix the capacity normalization. Compute the volume bound. Compute the initial ECH capacities and compare term by term. If an inequality fails, the proposed symplectic embedding is impossible. If all the inequalities checked so far pass, that is not yet proof of existence; further capacities or a constructive theorem may be required.

The broader message is that symplectic geometry measures more than space occupied. It measures which two-dimensional areas can be carried by a map preserving the symplectic form. ECH capacities convert that rigidity into arithmetic data. The resulting staircases are a visible trace of deep interactions among dynamical orbits, holomorphic curves, and integer lattice counting.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Contact Forms and Reeb Flows: Dynamics on an Odd-Dimensional Boundary

**Track:** Topology and Geometry. **Background:** vector fields, differential forms, exterior derivatives and symplectic geometry. **Question:** what geometry remains on the boundary of a symplectic region, and how does it determine distinguished trajectories?

#### Mathematical companion (not spoken)

On \(Y^{2n+1}\), \(\alpha\) is a contact form iff \(\alpha\wedge(d\alpha)^n\) is nowhere vanishing; \(\xi=\ker\alpha\), and \(d\alpha|_\xi\) is symplectic. The Reeb field satisfies \(\alpha(R_\alpha)=1\), \(\iota_{R_\alpha}d\alpha=0\). For \(\alpha=dz-y\,dx\) on \(\mathbb R^3\), \(d\alpha=dx\wedge dy\), \(\alpha\wedge d\alpha=dz\wedge dx\wedge dy\), and \(R_\alpha=\partial_z\). A Reeb orbit \(\gamma:[0,T]\to Y\) satisfies \(\dot\gamma=R_\alpha\), \(\gamma(0)=\gamma(T)\), hence \(\int_\gamma\alpha=T\). If \(\alpha'=c\alpha\), \(c>0\) constant, then \(R_{\alpha'}=R_\alpha/c\). A nonconstant factor does not generally give the same simple formula.

##### Exercises with answers

1. Test \(\alpha=dz\) for contactness on \(\mathbb R^3\). **Answer:** not contact, since \(d\alpha=0\).
2. Find the Reeb field for \(dz-y\,dx\). **Answer:** \(\partial_z\).
3. What is the alpha-action of a closed Reeb orbit of period seven? **Answer:** seven.
4. Does multiplying a contact form by a positive function preserve its kernel? **Answer:** yes, though not generally its Reeb flow.

##### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), contact models and Reeb fields.
- Michael Hutchings, [Lecture Notes on Embedded Contact Homology](https://arxiv.org/abs/1303.5789), Reeb orbits, actions and the ECH setting.
- [Contact geometry](https://en.wikipedia.org/wiki/Contact_geometry).

### Liouville Domains and Completions: Turning a Boundary into Infinity

**Track:** Topology and Geometry. **Background:** symplectic two-forms, exterior derivatives, contact forms and vector fields. **Question:** how can a compact symplectic region be enlarged while retaining geometric control near infinity?

#### Mathematical companion (not spoken)

An exact symplectic manifold has \(\omega=d\lambda\). Its Liouville vector field \(Z\) satisfies \(\iota_Z\omega=\lambda\), so \(\mathcal L_Z\omega=d\iota_Z\omega=d\lambda=\omega\). A Liouville domain \((W,\lambda)\) has compact boundary and outward-transverse \(Z\); \(\alpha=\lambda|_{\partial W}\) is contact. On its completion \(\widehat W=W\cup_{\partial W}([1,\infty)\times\partial W)\),
\[
\lambda=r\alpha,\qquad \omega=d(r\alpha)=dr\wedge\alpha+r\,d\alpha,\qquad Z=r\partial_r.
\]
For \(T^*Q\) with local coordinates \((q,p)\), fix \(\lambda=-\sum_i p_i\,dq_i\), \(\omega=d\lambda=\sum_i dq_i\wedge dp_i\); then \(Z=\sum_i p_i\partial_{p_i}\). With a Riemannian metric, the unit disk cotangent bundle is a Liouville domain. For a \(J\)-holomorphic sphere \(u:S^2\to\widehat W\) compatible with \(\omega=d\lambda\), \(E(u)=\int_{S^2}u^*\omega=\int_{S^2}d(u^*\lambda)=0\), hence u is constant.

##### Exercises with answers

1. Differentiate \(r\alpha\) on a cylindrical end. **Answer:** \(dr\wedge\alpha+r\,d\alpha\).
2. What is the Liouville field of \(-p\,dq\) on the cotangent plane with \(dq\wedge dp\)? **Answer:** \(p\partial_p\).
3. Why is a nonconstant compatible holomorphic sphere impossible in an exact symplectic manifold? **Answer:** its positive energy would equal an exact symplectic area integral, which vanishes by Stokes.
4. Does exactness alone prevent a noncompact Floer trajectory from escaping? **Answer:** no; geometric and analytic end controls are still needed.

##### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), symplectic fillings, contact-type boundaries and exactness.
- Denis Auroux, [A Beginner's Introduction to Fukaya Categories](https://arxiv.org/abs/1301.7056), exact symplectic geometry and Fukaya-theoretic context.
- [Symplectic manifold](https://en.wikipedia.org/wiki/Symplectic_manifold); [Cotangent bundle](https://en.wikipedia.org/wiki/Cotangent_bundle).

### Wrapping Hamiltonians and No-Escape Estimates

**Track:** Topology and Geometry. **Background:** contact/Reeb dynamics, Liouville completions, Hamiltonian action and Floer energy. **Question:** how do periodic orbits appear at infinity, and what prevents Floer trajectories from disappearing there?

#### Mathematical companion (not spoken)

On \(([1,\infty)\times Y,\lambda=r\alpha)\), \(\omega=dr\wedge\alpha+r\,d\alpha\). Fix the track convention \(\iota_{X_H}\omega=dH\). For \(H=h(r)\), the Hamiltonian vector field is
\[
X_H=-h'(r)R_\alpha,
\]
because \(\iota_{R_\alpha}\omega=-dr\). A one-periodic orbit at fixed \(r\) follows (the inverse orientation of) a Reeb orbit with period \(|h'(r)|\). For exact action \(\mathcal A_H(x)=-\int_x\lambda-\int_0^1 H(x(t))dt\), such an orbit has \(\mathcal A_H=rh'(r)-h(r)\). For \(h(r)=ar+b\), this equals \(-b\).

On \(T^*S^1\), \(q\in\mathbb R/2\pi\mathbb Z\), \(\lambda=-p\,dq\), \(\omega=dq\wedge dp\); for \(p>1\), \(H=ap\), \(\dot q=a\), \(\dot p=0\), so one-periodicity occurs exactly at \(a\in2\pi\mathbb Z\). The end Reeb field at \(p=1\) is \(R_\alpha=-\partial_q\).

For cylindrical contact-type \(J\) with \(J\partial_s=R_\alpha\) and \(J|_\xi\) compatible with \(d\alpha|_\xi\), a \(J\)-holomorphic map \(u=(s,v)\) satisfies \(\Delta s=d\alpha(\pi_\xi v_\sigma,J\pi_\xi v_\sigma)\ge0\) in conformal coordinates \((\sigma,\tau)\). This is a model subharmonicity statement; Hamiltonian-perturbed maximum principles require additional assumptions on \(H,J\), and the relevant boundaries.

##### Exercises with answers

1. Under \(\iota_{X_H}\omega=dH\), what is the vector field for \(H=h(r)\)? **Answer:** \(-h'(r)R_\alpha\).
2. When is \(H=ap\) on the positive cotangent-cylinder end one-periodic? **Answer:** when \(a\) is an integer multiple of \(2\pi\).
3. Compute the action of a radial orbit for \(h(r)=ar+b\). **Answer:** \(-b\) with the stated action convention.
4. Does noncompact exactness alone imply Floer compactness? **Answer:** no; radial and analytic control are also required.

##### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), cylindrical almost-complex structures and holomorphic curves.
- Mohammed Abouzaid, [On the Wrapped Fukaya Category and Based Loops](https://arxiv.org/abs/0907.5606), wrapped cotangent fibers and based loops.
- [Contact geometry](https://en.wikipedia.org/wiki/Contact_geometry); [Maximum principle](https://en.wikipedia.org/wiki/Maximum_principle).

### Wrapped Floer Homology and Symplectic Cohomology

**Track:** Topology and Geometry. **Background:** exact symplectic manifolds, Lagrangian intersection theory, Hamiltonian flows, and Floer complexes. **Central question:** how can counting Hamiltonian chords at infinity recover topology of loop spaces?

#### Mathematical companion (not spoken)

For an exact cotangent bundle `T^*Q` of a closed smooth manifold `Q` with a cotangent fiber `L=T^*_qQ`, the wrapped Floer cohomology of `L` is related by the Abbondandolo–Schwarz/Abouzaid comparison, with grading and coefficient hypotheses, to based-loop homology:
\[
HW^*(L,L)\cong H_{-*}(\Omega_q Q).
\]
At an A-infinity level, the wrapped endomorphism algebra corresponds to chains on `Omega_q Q`, with based-loop concatenation. For `Q=S^1`, components are labeled by integers, each contractible, hence `H_0(Omega S^1;Z) ~= Z[t,t^{-1}]` and other homology vanishes. Symplectic cohomology of `T^*Q` is instead related to homology of the **free** loop space `LQ`, with degree shifts and orientation conventions.

##### Exercises with answers

1. What distinguishes Hamiltonian chords from periodic Hamiltonian orbits? **Answer:** chords have specified Lagrangian endpoint conditions; periodic orbits close in phase space.
2. How many connected components does the based loop space of a circle have? **Answer:** countably infinitely many, indexed by winding numbers.
3. What operation corresponds to multiplication of Laurent monomials in the circle example? **Answer:** concatenation of based loops, adding winding numbers.
4. Why does a wrapped theory require analytic control at infinity? **Answer:** to keep Floer trajectories and counts compact or otherwise well-defined.

##### Reading and source notes

- [Abouzaid, On the Wrapped Fukaya Category and Based Loops](https://arxiv.org/abs/0907.5606), comparison of cotangent fibers with chains on based loops.
- [Abbondandolo and Schwarz, On the Floer Homology of Cotangent Bundles](https://arxiv.org/abs/math/0408280), cotangent-bundle Floer and loop-space comparisons.

### Symplectic Nonsqueezing: A Constraint That Volume Cannot See

**Track:** Topology and Geometry. **Background:** symplectic forms, Hamiltonian flows, volume, and embeddings. **Central question:** why can't a symplectic map squeeze a ball into an arbitrarily thin symplectic cylinder, even when the cylinder has infinite volume?

#### Mathematical companion (not spoken)

On `R^{2n}` let `omega_0=sum_{j=1}^n dq_j wedge dp_j`. Define the open ball `B^{2n}(r)={sum_j(q_j^2+p_j^2)<r^2}` and the symplectic cylinder `Z^{2n}(R)={q_1^2+p_1^2<R^2}`. Gromov's nonsqueezing theorem gives
\[
B^{2n}(r)\stackrel{\mathrm{sympl}}{\hookrightarrow}Z^{2n}(R)
\quad\Longleftrightarrow\quad r\le R.
\]
The easy direction is ordinary inclusion. The difficult implication is proved using pseudoholomorphic-curve methods (not by volume comparison). For n>1, `Vol(Z)=infinity`, but the normalized capacity still satisfies `c(B(r))=pi r^2`, `c(Z(R))=pi R^2`, giving the obstruction.

The linear map `(q_1,p_1)->(a q_1,p_1/a)` preserves `dq_1 wedge dp_1`; it shrinks a q coordinate but not the disk in the conjugate `(q_1,p_1)` plane in both directions. By contrast a target disk in `(q_1,q_2)` is not symplectic, and a map shrinking both q coordinates while expanding both conjugate p coordinates can fit the ball into an arbitrarily small q-only cylinder. This distinction is essential.

##### Exercises with answers

1. Can `B^4(2)` symplectically embed into `Z^4(1)`? **Answer:** no, since `2>1`.
2. Does an infinite-volume target imply that a finite symplectic ball can embed? **Answer:** no; capacity can obstruct.
3. Show that `(q,p)->(a q,p/a)` preserves the standard area form. **Answer:** `d(aq) wedge d(p/a)=dq wedge dp` for constant a>0.
4. Is nonsqueezing a consequence of Darboux's theorem alone? **Answer:** no, Darboux is local while nonsqueezing is a global rigidity result.

##### Reading and source notes

- [McDuff and Salamon, Introduction to Symplectic Topology: Symplectic capacities](https://academic.oup.com/book/43512/chapter-abstract/364195459), capacities and nonsqueezing.
- [Dusa McDuff, Lectures on Symplectic Topology](https://citeseerx.ist.psu.edu/document?doi=84ffca37956ebaa36ed874299ed20c067b1684e5&repid=rep1&type=pdf), introduction to the pseudoholomorphic-curve proof.
- [Michael Hutchings, Symplectic Weyl Laws (ICM 2026)](https://epubs.siam.org/doi/10.1137/25M1807277), Gromov width and modern capacity invariants.

### ECH Capacities and Symplectic Embedding Staircases

**Track:** Topology and Geometry. **Background:** symplectic forms, nonsqueezing, Hamiltonian dynamics, and ellipsoids. **Central question:** why can two regions have enough volume for an embedding and still fail to fit symplectically?

#### Mathematical companion (not spoken)

Use capacity-normalized ellipsoids in `C^2`:
\[
E(a,b)=\{(z_1,z_2):\pi|z_1|^2/a+\pi|z_2|^2/b\le1\},
\quad B(c)=E(c,c).
\]
Their symplectic volumes are `ab/2` and `c^2/2`, hence embedding into a ball requires `c>=sqrt(ab)`. ECH ellipsoid capacities are
\[
c_k(E(a,b))=N_k(a,b),
\]
where `N_k` is the `k`th entry, **starting at k=0**, of the ordered multiset `{ma+nb:m,n in Z_{>=0}}`, with multiplicities. For `E(1,4)`, the first entries are `(0,1,2,3,4,4,5,...)`; for `B(c)` they are `(0,c,c,2c,2c,2c,3c,...)`. At `k=3`, monotonicity requires `3<=2c`; volume gives the stronger `c>=2`. ECH-capacity inequalities are necessary for general domains, not universally sufficient.

##### Exercises with answers

1. What volume bound applies to `E(2,8) -> B(c)`? **Answer:** `c>=4`.
2. Why is the value four repeated in the capacity list of `E(1,4)`? **Answer:** `4=4*1+0*4=0*1+1*4`.
3. Does infinite volume of a cylinder defeat nonsqueezing? **Answer:** no; nonsqueezing is not a volume obstruction.
4. Do all capacity inequalities guarantee an arbitrary symplectic embedding? **Answer:** not in general; additional existence theorems are needed.

##### Reading and source notes

- [Hutchings, Quantitative Embedded Contact Homology](https://arxiv.org/abs/1005.2260), definition, monotonicity, and explicit ellipsoid capacities.
- [McDuff and Schlenk, The Embedding Capacity of Four-Dimensional Symplectic Ellipsoids](https://arxiv.org/abs/0912.0532), the ellipsoid-to-ball staircase.
