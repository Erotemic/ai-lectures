# Holomorphic curves, Fredholm dimensions, and strip boundaries

<!-- BEGIN SPOKEN LECTURE -->

# Holomorphic curves, Fredholm dimensions, and strip boundaries

## Riemann Surfaces and Holomorphic Maps: The Models We Can Calculate

Before we use holomorphic curves in a symplectic manifold, it is worth returning to their simplest setting: ordinary complex analysis. There, a map can be holomorphic for a very concrete reason. The derivative respects multiplication by the imaginary number i. The Cauchy-Riemann equations express exactly that compatibility.

When the source and target are curved surfaces, the same idea survives. But the geometry of a sphere, a torus, and a disk leads to different questions about degree, energy, boundary behavior, and families of maps. Those differences will matter when we attempt to count solutions.

### What is a Riemann surface?

A smooth surface may be covered by local coordinate patches. A Riemann surface is a two-dimensional real manifold whose patches use complex coordinates, and whose coordinate-change maps are holomorphic wherever they overlap.

The sphere is a first example. Remove its north pole and project the remaining points onto a plane, giving a complex coordinate z. Remove its south pole to obtain another complex coordinate w. On their overlap, w equals one over z. This change is holomorphic away from zero. The two charts give the sphere a global complex structure even though a single complex coordinate cannot cover it.

The standard sphere viewed this way is called the Riemann sphere, or complex projective line. Its points are one-dimensional complex subspaces of a two-dimensional complex vector space. Another picture is the ordinary complex plane together with one point at infinity.

A torus also admits complex structures. Start with the complex plane and identify points that differ by integer combinations of two linearly independent complex periods. The quotient is a compact complex torus. Different period lattices can describe different complex shapes even though their underlying topological space is always a torus.

### Holomorphicity without a global coordinate

At a point of a Riemann surface, multiplication by i in the local chart determines a quarter-turn on the tangent plane. Because the coordinate changes are holomorphic, this definition does not depend on which chart we used.

A smooth map between two Riemann surfaces is holomorphic if its derivative commutes with these quarter turns. In coordinates this is the usual Cauchy-Riemann condition. The definition does not require either surface to be flat.

Take the map from the complex plane to itself sending z to z squared. It doubles the angle and squares the distance from the origin. Away from zero it is locally two-to-one. At zero the derivative vanishes: the map is branched. There is no contradiction with holomorphicity, because a holomorphic map need not have invertible derivative everywhere.

The same map extends to the Riemann sphere by sending infinity to infinity. This gives a map of degree two. A generic target point has two preimages, counted with multiplicity. The two special points, zero and infinity, are branch points.

### Degree measured by area

Give the Riemann sphere a positive area form normalized so that its total area is one. Pull that area form back through the squaring map and integrate it over the source sphere. The result is two. Each regular target area element is covered twice, with positive orientation.

More generally, the map sending z to z raised to the d-th power extends to a holomorphic map of degree d for positive integers d. Its pulled-back symplectic area is d times the target's total area. This is a geometric way to read degree from an integral.

Why emphasize orientation? In ordinary topology, maps can have positive or negative local degrees. A nonconstant holomorphic map between oriented Riemann surfaces has nonnegative local multiplicities. Complex linear maps preserve the complex orientation wherever their derivative is nonzero. In the spherical examples, the degree is a nonnegative integer.

We should not confuse degree with the number of distinct preimages of every point. A branch point changes that count. Degree is the stable multiplicity-weighted number, and the area integral remembers it even in the presence of branching.

### Why spheres and tori behave differently

The sphere admits many nonconstant holomorphic maps to itself. A torus admits translations and maps induced by suitable complex-linear transformations of its covering plane. Yet there is no nonconstant holomorphic map from the sphere to a complex torus.

Here is an approachable reason. A map from the simply connected sphere to the torus lifts to the complex plane. The lifted map is holomorphic on the compact Riemann sphere, so it must be constant: a holomorphic function on a compact connected Riemann surface cannot be nonconstant if its target is the complex plane. Thus the original map was constant.

This is a reminder that target topology and complex structure restrict which curves exist. Later, existence and nonexistence of holomorphic spheres will become decisive in compactness questions.

### Families and symmetries of maps

There is a second complication. The same geometric curve can be described by many parameterizations. A fractional linear transformation of the sphere is a holomorphic change of its coordinate. Composing a map with such a transformation changes the formula without necessarily changing the underlying image.

The group of holomorphic automorphisms of the sphere has real dimension six. When we compute the expected dimension of a space of holomorphic spheres, we need to decide whether parameterizations count as different objects. If not, we must account for these six dimensions, with care around maps having symmetries.

For the degree-one maps from the Riemann sphere to itself, every such map is a holomorphic automorphism. Modulo reparameterization, there is essentially one degree-one map. That simple example is a useful check on a much later Fredholm index calculation.

### The bridge to almost-complex targets

The formulas we have used rely on genuine complex charts, but the key equation only says that the map's derivative respects a quarter turn. In symplectic geometry, we can choose a compatible almost-complex structure on any symplectic target and write that equation even without global holomorphic target coordinates.

Gromov's theory of pseudoholomorphic curves starts from that extension. Local complex-analysis estimates survive in modified form because the equation is elliptic. Positivity of area survives because the almost-complex structure is compatible with the symplectic form. But the classification by rational functions no longer applies, and counting curves requires functional analysis and compactness.

Keep the Riemann sphere examples close at hand. They will supply explicit curves, degrees, and branch points against which more abstract definitions can be tested. They also make clear that a holomorphic curve is not merely a drawn picture: it is a smooth map satisfying a rigid differential equation with topological consequences.

## Pseudoholomorphic Curves: The Equation and the Area–Energy Identity

Suppose a small rubber sheet is stretched across a curved space. We can ask how much it bends, how much area it covers, and whether it obeys a differential equation. These are different questions. A map might have a large derivative while covering very little signed area, for example when its two derivative directions nearly cancel.

A pseudoholomorphic curve is a map for which that ambiguity largely disappears. The map respects a quarter-turn on its domain and a compatible quarter-turn on its target. As a result, its derivative is highly constrained, and its geometric area equals a natural analytic energy.

### The equation starts in ordinary complex analysis

Let the domain have coordinates s and t, and regard them as the real and imaginary parts of a complex coordinate. The quarter-turn on the domain sends the s direction to the t direction. Let J be a compatible almost-complex structure on the target symplectic manifold.

The map is J-holomorphic when differentiating after turning the domain direction gives the same result as turning the derivative in the target. Written another way, the derivative in the s direction plus J applied to the derivative in the t direction is zero.

When both domain and target are the complex plane with their standard rotations, this is exactly the Cauchy-Riemann equation. The remarkable extension is that the target rotation need only vary smoothly. It does not have to come from genuine complex coordinate charts. The equation still makes sense on arbitrary symplectic manifolds.

### Energy measures the size of the entire derivative

Use the metric built from the symplectic form and J. At each point of the domain, measure the squared lengths of the derivative in both coordinate directions, add them, and divide by two. Integrate this quantity over the surface. The result is the energy of the map.

For an arbitrary map, energy and symplectic area are different. The area is obtained by inserting the two derivative vectors into the symplectic form and integrating. It remembers orientation. Energy is nonnegative and remembers the magnitudes of derivatives, regardless of their orientation.

Here is the central calculation. Take the difference between energy and symplectic area. Complete a square. What remains is one half of the squared length of precisely the expression that appears in the Cauchy-Riemann equation. The difference is therefore nonnegative, and it vanishes exactly for a J-holomorphic map.

So any compatible J-holomorphic curve has energy equal to symplectic area. This is not a definition arranged to make the result true; it follows from linear algebra at every point of the domain.

### A sphere with energy two

Return to the Riemann sphere with its standard complex structure and normalize its total symplectic area to one. The map that squares a complex coordinate and extends across infinity is holomorphic of degree two.

Its pullback of the area form integrates to two. By the energy identity, its analytic energy is also two. We have calculated a norm involving derivatives without solving a differential equation explicitly across the whole sphere. Topological degree and compatibility did the work.

A degree-three holomorphic self-map has energy three under the same normalization. These integer values are not the energy of every possible map or every possible symplectic manifold. They arise because this particular area class pairs integrally with the degree of the map.

### Why positive area constrains maps

Now suppose we have a symplectic manifold whose symplectic form integrates to zero over every sphere mapped into it. Such a manifold is symplectically aspherical. A holomorphic sphere in this target would have energy equal to its symplectic area, hence zero. Since the energy is an integral of nonnegative squared derivative lengths, the derivative must vanish everywhere. The map is constant.

This gives a powerful nonexistence theorem: a symplectically aspherical target has no nonconstant J-holomorphic spheres for compatible J. The two-torus is an example, because every map from a sphere to a torus is null-homotopic and therefore has zero symplectic area.

This matters for Floer homology. One way for a sequence of cylinders to lose compactness is by producing tiny holomorphic spheres at points where derivatives concentrate. In an aspherical target, the spheres that such a blow-up would produce cannot be nonconstant. One major source of noncompactness is removed.

### Why the energy identity is not a compactness theorem

We still need to control what happens to a whole sequence of maps. A bound on the integral of squared derivatives does not automatically give a bound on the derivative at every point. Energy can become concentrated in a shrinking region. That failure of pointwise control is called bubbling.

The equation supplies additional elliptic estimates that ordinary maps do not enjoy. Under suitable assumptions, bounded-energy J-holomorphic maps have subsequences that converge smoothly away from finitely many concentration points, and rescaling near those points reveals holomorphic bubbles. Establishing that result takes more than the identity we just derived. It needs local regularity, monotonicity or mean-value inequalities, and a precise description of the limiting domain.

There is an important contrast with Yang-Mills instanton bubbling. In both settings energy can concentrate and a rescaled geometric solution emerges. But the dimensions, scaling exponents, topology, and analytic equations differ. One should learn the analogy without importing theorems from one theory into the other uncritically.

### Why the equation matters for geometry

In ordinary differential geometry, curves can be found by solving geodesic equations. In symplectic topology, J-holomorphic curves provide another sort of probe. Their area is tied to topology, and their behavior is governed by an elliptic equation. The target's symplectic structure limits what they can do.

The first lesson is the area–energy identity. The second, to be developed next, is that it comes from an elliptic first-order operator. The third is that control of energy plus elliptic analysis produces a compactness theory with carefully classified exceptions. Together these facts make it possible to count curves and to extract genuinely global information from local differential equations.

## Cauchy–Riemann Operators: From Complex Derivatives to Elliptic Estimates

The equations defining a holomorphic map look deceptively simple: differentiate in two directions, turn one derivative by a quarter turn, and add. But these equations are unlike ordinary evolution equations. They do not prescribe how a state changes with time from initial data. Instead, they constrain a map throughout a two-dimensional region all at once.

This is an elliptic problem. Understanding that word is the next necessary step toward moduli spaces of pseudoholomorphic curves and Floer trajectories.

### Start with a complex-valued function

Write a function f of two real variables as its real part plus i times its imaginary part. Being holomorphic means its real and imaginary derivatives satisfy the Cauchy-Riemann equations. In a compact notation, the derivative in the s direction plus i times the derivative in the t direction must vanish.

Differentiate those equations again, eliminate the cross terms, and both real and imaginary parts satisfy Laplace's equation. Harmonic functions have strong regularity properties. In particular, a sufficiently well-behaved weak solution is smooth, even when we initially define it using only integrated derivatives.

That is the basic reason holomorphic functions are much more rigid than arbitrary differentiable functions. Their first-order equation secretly controls second-order elliptic behavior.

### What ellipticity means at high frequency

Suppose we test the operator on a rapidly oscillating plane wave. Differentiation multiplies that wave by a frequency component. The two directional derivatives combine into a linear map depending on the frequency vector.

For the Cauchy-Riemann operator, that map is invertible for every nonzero frequency vector. It cannot lose all control of a nontrivial rapidly oscillating mode just because the mode points in an inconvenient direction. This invertibility is the principal-symbol condition for ellipticity.

One may think of it as a way of ruling out hidden directions where the highest-order derivatives become invisible. It is stronger than merely being able to write down the PDE, and it is what supports estimates of the full first derivative from the equation plus lower-order information.

### The correct function spaces

A smooth curve is what we ultimately want, but to solve nonlinear equations one often starts with a completed space of less regular maps. Sobolev spaces allow first derivatives to exist in a weak sense and measure them by integral norms.

On a two-dimensional domain, a first-order Sobolev function with integrability exponent strictly greater than two has a continuous representative, under standard local hypotheses. That matters because a nonlinear expression such as J evaluated at the map needs the map itself to be well-defined pointwise. The two-dimensional exponent is not incidental: it reflects how Sobolev embedding depends on the dimension of the domain.

We can therefore model the space of maps by a suitable first-order Sobolev space, and put the Cauchy-Riemann defect in an integrable target space. The nonlinear equation becomes the zero set of a section of a Banach-space bundle.

The actual construction requires coordinate charts, exponential maps, and care about boundary conditions. But the picture is simple: the unknown is a map, the equation produces its defect, and a zero defect is a pseudoholomorphic curve.

### Linearization is the first serious tool

Suppose we already have one solution u. Move it slightly in a direction given by a vector field along u. Differentiate the nonlinear equation with respect to that perturbation. The result is a linear first-order operator acting on variations of u.

Its highest-order part is a Cauchy-Riemann operator. Terms involving derivatives of J or the target connection contribute lower-order corrections. These corrections complicate estimates, but they do not destroy ellipticity.

If the linearized operator is surjective between suitable Banach spaces, an implicit function theorem gives a smooth local solution space whose dimension equals the dimension of its kernel, after treating relevant symmetries. In other words, the infinite-dimensional equation can have a finite-dimensional family of solutions.

This is the analytic mechanism underlying the phrase 'moduli space of holomorphic curves.' A moduli space is not necessarily smooth, and surjectivity can fail. We must examine those failures rather than assuming all solutions belong to a nice manifold.

### Two simple kernels to compare

On the Riemann sphere, every globally holomorphic complex-valued function is constant. So the kernel of the ordinary Cauchy-Riemann operator on complex-valued functions consists of constants, a complex one-dimensional space. The associated cokernel is zero for the standard trivial complex line bundle.

On a complex torus, holomorphic complex-valued functions are again constant. But the cokernel now has complex dimension one. The same local differential operator has a different global index because the domain topology differs.

This is an important conceptual shift. Ellipticity is local, but the difference between kernel and cokernel dimensions is global. An index theorem can calculate that difference from topological data even when we cannot explicitly solve the PDE.

### Why a finite-energy limit can become smooth

Suppose a sequence of weak solutions converges in an appropriate weak topology. The elliptic equation often allows us to upgrade the regularity of the limit wherever the needed local estimates remain uniform. For fixed smooth J and a solution whose coefficients are controlled, elliptic bootstrapping promotes a weak solution to a smooth one.

But regularity and compactness are not identical. The right estimates may fail near points where derivatives grow without bound. Bubbling analysis is designed to isolate those points and understand their rescaled geometry.

The vocabulary is now in place. Sobolev spaces give a setting for the equation. Ellipticity controls local derivatives. Linearization produces a Fredholm operator. Surjectivity creates a smooth local moduli space. Compactness then asks whether a family of such solutions can escape the space by degeneration.

Every later Floer or pseudoholomorphic-curve construction relies on this sequence, often with significant additional work for noncompact domains and Lagrangian boundary conditions.

## Fredholm Index and Transversality: Counting Dimensions Before Curves

Suppose we want to count holomorphic spheres in a symplectic manifold. Before finding even one, there is a more basic question. Should we expect isolated solutions, a family with several continuous parameters, or no solutions at all?

An elliptic index gives a first approximation. It measures the difference between the number of infinitesimal solutions and the number of infinitesimal obstructions. This is not automatically the actual number of independent solutions. But it is a computable, topological quantity that guides the analysis.

### A linear operator with two finite dimensions

Take one holomorphic curve u. Perturb it by a small vector field along the curve. Linearizing the Cauchy-Riemann equation produces an elliptic operator. Its kernel consists of first-order deformations that continue to satisfy the equation to first order.

A nonzero cokernel represents obstructions: infinitesimal errors that cannot be corrected by any first-order deformation. The Fredholm index is the real dimension of the kernel minus the real dimension of the cokernel.

Ellipticity on a compact domain makes both dimensions finite. The index is stable under continuous perturbations of lower-order terms. That stability allows topology, rather than detailed coefficients, to determine the answer.

### Riemann–Roch as a dimension formula

Let the domain be a closed Riemann surface of genus g, and suppose the target has complex dimension n. The linearized operator acts on sections of the pullback tangent bundle. Its real index has two contributions.

The first depends on the Euler characteristic of the domain, which is two minus two g, multiplied by n. The second is twice the first Chern number of the target tangent bundle evaluated on the curve's homology class.

Think of the first term as the number of directions available from the basic topology of the domain. Think of the Chern term as measuring the twisting of the complex vector bundle along the map. This is a version of the Riemann–Roch theorem for Cauchy-Riemann operators.

That formula applies to the parameterized curve problem with a fixed complex structure on the domain. It is not yet the expected dimension of the space of unparameterized geometric curves.

### Count projective lines in the complex projective plane

Consider the complex projective plane, which has complex dimension two. Its lines are themselves copies of the Riemann sphere. A projective line represents the basic degree-one homology class.

The target tangent bundle has first Chern number three on that class. The domain is a sphere, so its Euler characteristic is two. The real Fredholm index is therefore two times two, plus two times three: ten.

Why ten and not four, the familiar real dimension of the family of projective lines? Because the operator treats differently parameterized copies of the same sphere as distinct. The Riemann sphere has a six-real-dimensional group of holomorphic automorphisms. Subtract those reparameterizations, assuming the action behaves well, and ten minus six is four.

Indeed, projective lines in the projective plane form another projective plane, the dual projective plane. It has complex dimension two, or real dimension four. Our index calculation has matched the geometry exactly.

### The hidden hypothesis: regularity

The computation worked because the holomorphic line is regular. The linearized Cauchy-Riemann operator has no obstruction space beyond those already accounted for, and quotienting by reparameterization is well-behaved in this example.

For an arbitrary J-holomorphic map, the actual dimension can differ from the expected one. The cokernel might be nonzero. Multiple covers can have stabilizers or fail generic transversality. Constant maps create their own automorphism complications. Merely subtracting six from every sphere index would be wrong.

A powerful method is to choose a generic compatible almost-complex structure J. Under appropriate hypotheses, moduli spaces of somewhere-injective, or simple, curves become regular. In functional-analytic language, this uses a version of Sard's theorem for infinite-dimensional spaces, together with a carefully constructed universal moduli space.

This does not automatically regularize every multiply covered curve. Those are among the reasons modern theories sometimes require virtual fundamental cycles or related perturbation machinery. We should not present the word generic as a universal solvent.

### What the index cannot tell us

A predicted dimension of zero does not prove that a solution exists. It says that if solutions exist and are regular, we expect them to be isolated after quotienting symmetries. A predicted negative dimension often suggests that generic simple curves in that class are absent, but exceptional maps or nongeneric data still require care.

Nor does index zero imply a finite count. An infinite sequence of isolated solutions might escape through bubbling or degeneration. Compactness is a logically separate ingredient. Orientations are also needed for integer counts, or one can sometimes work with coefficients modulo two.

The full path to an invariant therefore has several steps: define a geometric equation, compute the linearized index, obtain transversality, control degenerations, quotient symmetries, and only then count solutions.

### Why this prepares us for Floer theory

For a Floer cylinder, the same principle applies with a noncompact domain. The index is related to a spectral-flow or Conley–Zehnder index difference between its limiting periodic orbits. We must additionally account for translation of the cylinder along its length.

As with spheres, a zero-dimensional quotient space is where a numerical count becomes plausible. A one-dimensional quotient space is where its boundary can encode an algebraic identity. But both dimensions are only predictions until we establish regularity and compactness.

The projective-line calculation gave an encouraging example: algebraic topology predicted exactly the dimension of a classical geometric family. The advanced theory will reuse this logic, while facing harder analytic and symmetry problems.

## Boundary Conditions for Holomorphic Strips and the Maslov Index

A holomorphic curve defined on a closed sphere has no boundary. But the geometry of Lagrangian intersections naturally leads to maps from strips: two long parallel edges must land on two specified Lagrangian submanifolds. A solution may travel from one intersection point to another as we move along the strip.

The boundary condition is much more than a drawing. It has to make the Cauchy-Riemann equation into a well-posed elliptic problem. It also contributes an integer to the Fredholm index. That integer is closely related to the Maslov index.

### A strip between two lines

Work first in the complex plane. Take the horizontal real axis as one Lagrangian. Take another straight line passing through the origin at some angle as the other. Both are one-dimensional curves in a two-dimensional symplectic plane and hence are Lagrangian.

Picture a map from an infinite strip. The bottom edge lands on the horizontal line, and the top edge lands on the tilted line. Along the interior, the map satisfies the Cauchy-Riemann equation. The imposed boundary values do not specify exact positions; they say that each boundary point must remain on its assigned line.

When the two lines meet transversely at the origin, their intersection is isolated. This provides the simplest local model for the ends of Lagrangian Floer strips. In a curved manifold, the tangent spaces of the two Lagrangians play the roles of these lines, and the boundary condition varies with the map.

### The boundary cannot be chosen arbitrarily

For a first-order elliptic equation, giving completely arbitrary boundary data may be too strong, too weak, or incompatible with ellipticity. The condition that boundary variations lie inside a Lagrangian tangent space has precisely the correct half-dimensional character for a Cauchy-Riemann operator.

This is why Lagrangian boundary conditions recur in complex analysis, symplectic topology, and mathematical physics. They allow a complex-linear interior equation to interact with a real subspace at the boundary without destroying the Fredholm framework.

The domain can be a disk instead of a strip. Then the entire boundary may lie on a single Lagrangian. Holomorphic disks with Lagrangian boundary are central to understanding when Lagrangian Floer theory works as simply as the first picture suggests.

### Follow a line around a loop

Take an unoriented line through the origin in the plane. Start with the horizontal line. Rotate it continuously through half a turn. At the end it is horizontal again, because a line does not remember which direction along it counts as forward.

We have traced a nontrivial loop in the space of Lagrangian lines. The Maslov index assigns this basic loop the integer one under the standard normalization. Rotating through a full turn gives index two. In higher-dimensional symplectic spaces, the same index measures how a loop of Lagrangian subspaces winds in the Lagrangian Grassmannian.

This is not merely a winding number attached as decoration. In a holomorphic boundary problem, the changing Lagrangian boundary data affects the Fredholm index. The Maslov class records the topological part of that change.

### A holomorphic hemisphere

Use the Riemann sphere and choose its equator as a Lagrangian circle. One hemisphere is a holomorphic disk whose boundary is the equator, after choosing the appropriate complex orientation.

Double this disk across its boundary. The two halves combine to form a degree-one sphere. The disk's Maslov index is two. This is an example where the boundary winding can be calculated geometrically by reflection and doubling.

The Fredholm index of a parameterized holomorphic disk with fixed disk complex structure has a term equal to the real dimension of the Lagrangian plus its Maslov index. Here the Lagrangian dimension is one and the Maslov index is two, so the index is three. The disk has a three-dimensional group of holomorphic reparameterizations. In the regular, nonconstant setting, taking that quotient can leave an isolated unparameterized hemisphere.

This is a simple rehearsal of the more abstract dimension accounting we will need for strips.

### What the index predicts for strips

Suppose two Lagrangians intersect transversely at points x and y. A holomorphic strip may approach x as its long coordinate tends to minus infinity and y as it tends to plus infinity.

To predict the dimension of the space of such strips, we examine the linearized Cauchy-Riemann operator with Lagrangian boundary conditions. Its index is a relative Maslov index, expressed through the two asymptotic intersection points and appropriate choices of grading and trivialization.

A nonconstant strip can be translated along its infinite direction. That translation gives one parameter describing the same geometric trajectory. Consequently, the dimension after dividing by translation is the Fredholm index minus one at a regular nonconstant strip.

Rigid strips, meaning isolated solutions after this quotient, are the ones that can contribute to a Floer differential. One-dimensional families after the quotient are the ones whose boundaries will eventually prove the differential squares to zero.

### The complication of disk bubbling

A sequence of strips can degenerate in more ways than a pair of strips breaking apart. A nonconstant holomorphic disk may bubble from a boundary point and remain attached to one of the Lagrangians. Its Maslov index affects the expected dimensions of the possible boundary strata.

In an exact symplectic manifold with exact Lagrangians, such nonconstant disks are excluded by the area–energy identity and Stokes' theorem, provided the relevant hypotheses hold. In nonexact settings, disk bubbles may obstruct the naive identity that the Floer differential squares to zero. This is one reason more general Lagrangian Floer theory develops additional algebraic structures and bounding cochains.

We do not yet need the full obstruction theory. We do need to remember that a strip's boundary condition has geometry of its own, and that geometry can appear in compactness limits.

### The bridge from intersections to counts

The chain generators will be intersection points. The curves contributing to the differential will be strips with boundaries on two Lagrangians. Their expected dimensions will be governed by a relative Maslov index, just as ordinary Morse trajectories are governed by differences of Morse indices.

This connects three pieces of mathematics: real Lagrangian geometry at the boundary, complex elliptic analysis in the interior, and integer-valued topology through the Maslov index. Without all three, the words 'count holomorphic strips' would conceal much of the work needed to make the count meaningful.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Riemann Surfaces and Holomorphic Maps: The Models We Can Calculate

**Track:** Topology and Geometry. **Background:** complex differentiation, smooth manifolds, integration, degree and orientation. **Central question:** what changes when holomorphic functions become maps between curved surfaces?

#### Mathematical companion (not spoken)

Identify \(\mathbb{CP}^1=\mathbb C\cup\{\infty\}\) with atlas \(w=1/z\) on the overlap. A holomorphic map \(u_d(z)=z^d\) extends over \(\infty\) and has topological degree \(d\ge1\). Normalize the Fubini–Study form by
\[
\omega_{FS}=\frac{i}{2\pi}\frac{dz\wedge d\bar z}{(1+|z|^2)^2},\qquad \int_{\mathbb{CP}^1}\omega_{FS}=1.
\]
Then \(\int_{\mathbb{CP}^1}u_d^*\omega_{FS}=d\). The map has local branching at \(0\) and \(\infty\) when \(d>1\). The Riemann–Hurwitz formula for a degree-\(d\) sphere-to-sphere map gives total branching \(2d-2\), consistent with two branch points of order \(d-1\).

For \(\mathbb C/\Lambda\), a holomorphic map \(\mathbb{CP}^1\to\mathbb C/\Lambda\) lifts to an entire map on \(\mathbb{CP}^1\) since \(\mathbb{CP}^1\) is simply connected; it is constant. Holomorphic automorphisms of \(\mathbb{CP}^1\) form \(\mathrm{PSL}_2(\mathbb C)\), real dimension six, a fact needed when quotienting parameterized sphere moduli.

##### Exercises with answers

1. **Atlas.** What is the transition function between the two standard \(\mathbb{CP}^1\) charts? **Answer:** \(w=1/z\) on their overlap.
2. **Degree.** What is the total normalized symplectic area of \(z\mapsto z^3\)? **Answer:** three.
3. **Branching.** Why does the fiber above zero have fewer than three distinct points for \(z^3\)? **Answer:** zero is a branch point of multiplicity three.
4. **Target topology.** Can a nonconstant holomorphic sphere map into a complex torus? **Answer:** no; it lifts to a holomorphic map from the compact sphere to \(\mathbb C\), hence is constant.

##### Sources and further reading

- Mikhail Gromov, [Pseudo-holomorphic Curves in Symplectic Manifolds](https://doi.org/10.1007/BF01388806), *Inventiones Mathematicae* 82 (1985), 307–347.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), first examples and complex structures.
- [Riemann surface](https://en.wikipedia.org/wiki/Riemann_surface); [Riemann sphere](https://en.wikipedia.org/wiki/Riemann_sphere); [Riemann–Hurwitz formula](https://en.wikipedia.org/wiki/Riemann%E2%80%93Hurwitz_formula).

### Pseudoholomorphic Curves: The Equation and the Area–Energy Identity

**Track:** Topology and Geometry. **Background:** Riemann surfaces, symplectic forms, compatible almost-complex structures and basic calculus of variations. **Central question:** how can an elliptic equation convert topological area into analytic energy?

#### Mathematical companion (not spoken)

For a domain \((\Sigma,j)\) with local conformal coordinates \((s,t)\) and a compatible \(J\), the pseudoholomorphic equation is \(\bar\partial_Ju=\tfrac12(du+J\circ du\circ j)=0\), equivalent locally to \(u_s+J(u)u_t=0\). For a general smooth map,
\[
E(u)=\frac12\int_\Sigma (|u_s|^2+|u_t|^2)\,ds\,dt,\qquad
E(u)-\int_\Sigma u^*\omega=\frac12\int_\Sigma|u_s+J(u)u_t|^2\,ds\,dt\ge0.
\]
The identity uses a conformal domain metric and \(g(\cdot,\cdot)=\omega(\cdot,J\cdot)\). It extends globally by conformal invariance of energy in dimension two. For a \(J\)-holomorphic map, \(E(u)=\langle[\omega],u_*[\Sigma]\rangle\) on a closed oriented domain.

If \(\omega|_{\pi_2(M)}=0\), every compatible \(J\)-holomorphic \(u:S^2\to M\) is constant, because \(E(u)=\int_{S^2}u^*\omega=0\). This only rules out spherical bubbling; other degeneration modes require separate arguments.

##### Exercises with answers

1. **Square identity.** What quantity must vanish for equality between energy and symplectic area? **Answer:** \(u_s+J(u)u_t\), equivalently \(\bar\partial_Ju=0\).
2. **Degree.** If \(\int_{\mathbb{CP}^1}\omega=1\), what energy does \(z\mapsto z^4\) have? **Answer:** four.
3. **Aspherical.** Why does symplectic asphericity rule out nonconstant holomorphic spheres? **Answer:** all sphere areas vanish, so the energy vanishes.
4. **Limitation.** Does bounded energy imply uniform derivative bounds for an arbitrary sequence of J-curves? **Answer:** no; derivatives may concentrate and create bubbles.

##### Sources and further reading

- Mikhail Gromov, [Pseudo-holomorphic Curves in Symplectic Manifolds](https://doi.org/10.1007/BF01388806) (1985), original framework.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), energy and local estimates.
- [Pseudoholomorphic curve](https://en.wikipedia.org/wiki/Pseudoholomorphic_curve); [Symplectically aspherical manifold](https://en.wikipedia.org/wiki/Aspherical_space#Symplectically_aspherical_manifolds).

### Cauchy–Riemann Operators: From Complex Derivatives to Elliptic Estimates

**Track:** Topology and Geometry. **Background:** Cauchy–Riemann equations, weak derivatives, Sobolev spaces, elliptic regularity. **Central question:** what analytic machinery makes a nonlinear holomorphic-curve equation tractable?

#### Mathematical companion (not spoken)

On \(\mathbb C=\mathbb R^2\) with coordinates \((s,t)\), set \(D=\partial_s+i\partial_t\) acting on complex-valued functions. Its principal symbol at \(\xi=(\xi_s,\xi_t)\) is multiplication by \(i\xi_s-\xi_t\); its squared complex modulus is \(\xi_s^2+\xi_t^2\), nonzero for \(\xi\ne0\). Also \((\partial_s-i\partial_t)D=\Delta\) on smooth functions.

For \(p>2\), the embedding \(W^{1,p}(\Sigma)\hookrightarrow C^0(\Sigma)\) holds on a compact smooth real surface (indeed it embeds into \(C^{0,\alpha}\) with \(\alpha=1-2/p\)). For a \(J\)-curve, \(D_u\) is a real Cauchy–Riemann-type operator \(W^{1,p}(\Sigma,u^*TM)\to L^p(\Omega^{0,1}(\Sigma,u^*TM))\). On a compact domain it is Fredholm with suitable boundary conditions; for punctured/cylindrical domains one usually needs asymptotic and weighted-space hypotheses.

For the trivial complex line bundle on a closed genus-\(g\) Riemann surface, the complex index of \(\bar\partial\) is \(1-g\). The sphere has kernel dimension one and cokernel dimension zero; the torus has kernel and cokernel each of complex dimension one. Elliptic regularity upgrades distributional solutions when the coefficients and relevant norms satisfy standard smoothness hypotheses.

##### Exercises with answers

1. **Symbol.** What is the squared modulus of the symbol of \(D=\partial_s+i\partial_t\) at frequency \((a,b)\)? **Answer:** \(a^2+b^2\).
2. **Harmonicity.** What second-order equation does a holomorphic function satisfy componentwise? **Answer:** Laplace's equation.
3. **Index.** What is the complex index of the scalar \(\bar\partial\) on a torus? **Answer:** zero.
4. **Caveat.** Does ellipticity alone imply the nonlinear moduli space is smooth at every solution? **Answer:** no; transversality or surjectivity can fail.

##### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), nonlinear Cauchy–Riemann operators and regularity.
- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), Fredholm analysis and compactness.
- [Elliptic partial differential equation](https://en.wikipedia.org/wiki/Elliptic_partial_differential_equation); [Cauchy–Riemann equations](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations).

### Fredholm Index and Transversality: Counting Dimensions Before Curves

**Track:** Topology and Geometry. **Background:** Riemann surfaces, elliptic operators, bundles and characteristic classes, implicit function theorem. **Central question:** how can topology predict the dimension of a space of solutions to a nonlinear PDE?

#### Mathematical companion (not spoken)

For a closed genus-\(g\) Riemann surface \(\Sigma\), a fixed domain complex structure \(j\), and \(u:\Sigma\to M^{2n}\) in homology class \(A\), the real index of the linearized Cauchy–Riemann operator is
\[
\operatorname{ind}_{\mathbb R}D_u=n(2-2g)+2\langle c_1(TM,J),A\rangle.
\]
For unparameterized genus-\(g\) simple curves with \(k\) marked points and the stable-domain setup, the standard expected real dimension is \((2n-6)(1-g)+2c_1(A)+2k\). The distinction includes variations in complex structure and quotienting automorphisms. For \(\mathbb{CP}^2\), \(n=2\), \(g=0\), and a line \(A=[\mathbb{CP}^1]\), \(c_1(T\mathbb{CP}^2)(A)=3\), hence fixed-domain parameterized index \(4+6=10\). Subtracting the free six-dimensional sphere-automorphism action gives \(4\), matching the dual projective plane parameterizing lines.

Regularity requires surjectivity of \(D_u\); for simple curves, generic \(J\) can produce transversality under appropriate setup. Multiple covers, automorphisms, compactness, and orientations require separate handling. Index is a virtual dimension, not an existence statement.

##### Exercises with answers

1. **Line index.** Compute the parameterized real index of a degree-one sphere in \(\mathbb{CP}^2\). **Answer:** \(2(2)+2(3)=10\).
2. **Unparameterized.** Why does the dimension drop from ten to four for a projective line? **Answer:** quotient by the real six-dimensional \(\mathrm{PSL}_2(\mathbb C)\) parameterization symmetry.
3. **Index zero.** Does a zero Fredholm index guarantee a nonempty finite moduli space? **Answer:** no; existence, regularity, and compactness are independent issues.
4. **Cokernel.** If \(\dim\ker D=7\) and \(\dim\operatorname{coker}D=2\), what is its index? **Answer:** five.

##### Sources and further reading

- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), Fredholm and transversality chapters.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), index, simple curves, and moduli spaces.
- [Riemann–Roch theorem](https://en.wikipedia.org/wiki/Riemann%E2%80%93Roch_theorem); [Fredholm operator](https://en.wikipedia.org/wiki/Fredholm_operator).

### Boundary Conditions for Holomorphic Strips and the Maslov Index

**Track:** Topology and Geometry. **Background:** Lagrangian submanifolds, holomorphic disks, elliptic boundary problems, the Maslov index survey. **Central question:** what counts as an elliptic boundary condition when a curve's edges must lie in two Lagrangians?

#### Mathematical companion (not spoken)

For \(u:\mathbb R\times[0,1]\to M\), impose \(\bar\partial_Ju=0\), \(u(s,0)\in L_0\), \(u(s,1)\in L_1\). The linearized operator \(D_u\) acts on sections \(\xi\) with \(\xi(s,i)\in T_{u(s,i)}L_i\). On suitable weighted Sobolev spaces with transverse asymptotics, \(D_u\) is Fredholm. For regular nonconstant strips, quotienting the \(\mathbb R\)-action by translation lowers the local dimension by one.

The Lagrangian Grassmannian in complex dimension one is \(\Lambda(1)=\mathbb{RP}^1\cong S^1\). The loop \(\ell(t)=\operatorname{span}_\mathbb R(\cos(\pi t),\sin(\pi t))\), \(0\le t\le1\), is a generator of \(\pi_1(\Lambda(1))\cong\mathbb Z\), with Maslov index \(+1\) under the conventional generator orientation. A disk in \((\mathbb{CP}^1,\mathbb{RP}^1)\) covering a hemisphere has Maslov index \(2\); its fixed-domain real Cauchy–Riemann index is \(n\chi(D)+\mu=1+2=3\), before quotienting disk automorphisms and after checking stability/regularity.

For nonexact Lagrangians, boundary disk bubbling can contribute codimension-one degenerations to one-dimensional strip moduli; the naive \(\partial^2=0\) argument is then incomplete without suitable monotonicity, unobstructedness, or additional algebraic machinery.

##### Exercises with answers

1. **Lines.** Is every smooth curve in a symplectic surface Lagrangian? **Answer:** every one-dimensional immersed curve is Lagrangian wherever immersed.
2. **Maslov loop.** What index does a half-turn of an unoriented line have under the stated normalization? **Answer:** one.
3. **Hemisphere.** What Maslov index does the standard hemisphere disk bounded by \(\mathbb{RP}^1\subset\mathbb{CP}^1\) have? **Answer:** two.
4. **Translation.** Why subtract one from the Fredholm index for a regular nonconstant strip modulo translation? **Answer:** moving its s-origin does not change the geometric trajectory and gives a free one-dimensional symmetry.

##### Sources and further reading

- Andreas Floer, [Morse Theory for Lagrangian Intersections](https://doi.org/10.4310/JDG/1214442477), original intersection-complex construction.
- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), boundary-value and index foundations.
- [Maslov index](https://en.wikipedia.org/wiki/Maslov_index); [Lagrangian submanifold](https://en.wikipedia.org/wiki/Lagrangian_submanifold).
