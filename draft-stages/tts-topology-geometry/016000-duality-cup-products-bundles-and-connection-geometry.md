# Duality, cup products, bundles, and connection geometry

<!-- BEGIN SPOKEN LECTURE -->

# Duality, cup products, bundles, and connection geometry

## Poincaré Duality: Why a Manifold's Dimensions Pair Up

A sphere has a zero-dimensional homology class representing its one connected component and a two-dimensional class representing the entire oriented surface. The group in degree one vanishes. A torus has the same groups at the extremes, but two independent one-dimensional cycles wind around its two directions.

These patterns are not independent. On a closed, connected, oriented manifold of dimension n, the cohomology in degree k is naturally related to the homology in degree n minus k. This is Poincaré duality. It is among the strongest reasons that manifolds are more than arbitrary topological spaces.

### Orientation creates a global class

A manifold looks locally like Euclidean space. If we can choose orientations consistently from one coordinate neighborhood to the next, it is orientable. If it is also compact and has no boundary, it possesses a fundamental homology class in its top dimension, once an orientation has been chosen.

For a connected n-dimensional manifold, this class expresses the manifold itself as an oriented cycle. It is not the same as a physical boundary: the manifold has none. Algebraically, the local orientations join into a global top-dimensional homology class.

The fundamental class is the ingredient that turns cohomology into homology. Cohomology classes can be thought of as rules for evaluating, measuring, or detecting cycles. The cap product lets a cohomology class act on a homology class and lower its dimension.

Apply a degree-k cohomology class to the degree-n fundamental class. The result is a homology class in degree n minus k. Poincaré duality says this map is an isomorphism, not merely a useful construction.

### A torus makes the pairing visible

Consider a torus, the surface of a doughnut. It has two independent one-dimensional loops: one goes around the hole, and the other goes around the tube. Call their homology classes a and b. They cannot be continuously deformed into one another, and together they generate the first homology group, a copy of the integers squared.

Now consider the corresponding degree-one cohomology classes. They can evaluate on oriented loops, counting winding in one direction or the other. Their cup product is a degree-two cohomology class. When evaluated on the fundamental class of the torus, the product of the two basic degree-one classes gives plus one for a consistent choice of orientation.

Reverse their order, and the cup product changes sign, because degree-one cohomology products anticommute. The resulting alternating form records the oriented intersection of the two types of loops. This is not just a count of holes; it remembers how different cycles meet.

On a closed oriented surface of genus g, the first homology has rank two g. One can choose g pairs of basic cycles whose intersection form is the standard alternating pairing. The fact that the rank is even is a geometric constraint visible in the algebra.

### Duality beyond a surface

In dimension three, Poincaré duality pairs degree-one cohomology with degree-two homology. An oriented surface inside a three-manifold can represent a degree-two homology class, while a degree-one cohomology class may detect how loops cross such surfaces. The pairing is the higher-dimensional analogue of winding and intersection on a torus.

In even dimensions, complementary middle-dimensional cycles can intersect in isolated points. Their signed intersections define a bilinear pairing. For a closed oriented four-manifold, for example, the intersection form on its second homology modulo torsion can carry deep information about the manifold's topology.

Duality is not claiming all homology groups in complementary degrees are literally the same. It relates cohomology to homology. If we work over a field, finite-dimensional vector-space duality can turn this into a symmetry of Betti numbers. Over the integers, torsion makes the relationship more subtle, and universal coefficient theorems must be handled explicitly.

### The proof idea is local-to-global

Why should one global fundamental class produce an isomorphism everywhere? At a point of an oriented manifold, the local relative homology in degree n is a copy of the integers. This is the infinitesimal version of a fundamental class.

To pass from local to global, one proves that the cap-product construction behaves naturally under suitable restrictions and open covers. The Mayer–Vietoris sequences on the cohomology side and homology side form a compatible diagram. On small neighborhoods, where the topology is that of a ball, the desired map is readily checked. Exactness and diagram-chasing then let the result propagate through a cover.

This is a broad proof strategy in topology: prove a local claim on simple neighborhoods, show the construction respects gluing, and obtain the global theorem. The gluing algebra from Mayer–Vietoris is not incidental. It is part of why Poincaré duality exists.

### What changes at a boundary or without orientation

The familiar theorem has hypotheses. For a compact oriented manifold with boundary, the fundamental class naturally lives in relative homology, not the absolute top homology. The appropriate version is Poincaré–Lefschetz duality, pairing absolute cohomology with relative homology, and vice versa.

Take a disk. Its ordinary second homology is zero: the disk can contract, and its boundary prevents it from being an absolute two-cycle. But its relative second homology, measured modulo the boundary circle, is the integers. The relative class is precisely what duality needs.

If a manifold is nonorientable, integral Poincaré duality cannot be stated using an ordinary globally chosen fundamental class. With coefficients modulo two, orientation signs disappear and a version still holds. More generally, an orientation local system gives the correct integral formulation.

Noncompact manifolds require another change, often involving compactly supported cohomology. A noncompact oriented plane, for example, does not possess the same ordinary top-dimensional fundamental class as a closed sphere.

### What this theorem explains

Poincaré duality is a structural symmetry. It tells us that on a closed oriented manifold, topological information in degree k has a complementary life in dimension n minus k. Cup products and intersection pairings turn the symmetry into calculations with genuine geometric meaning.

And it explains why exact hypotheses matter. Orientation, compactness, and the presence of boundary are not small print. They determine which fundamental class exists and therefore which form of duality is true. A theorem that pairs dimensions so elegantly is powerful because it says exactly when—and exactly how—the pairing works.

## Cup Products and Intersection Numbers: What Two Holes Say to Each Other

A torus has two independent directions in which a loop can wind: around its central hole and around the tube. We can describe those directions with two integers. But we can ask more than how many loops there are. We can ask how two loops meet, and whether two different one-dimensional measurements combine to detect the entire surface.

The mathematical tools for those questions are the cup product and intersection pairing. They are also the beginning of ideas that appear in characteristic classes, four-manifold topology, and gauge-theoretic invariants. Let us work through their meaning on the simplest nontrivial example.

### A closed form as a measurement

View a torus as a square with opposite sides identified. Choose a horizontal coordinate, x, and a vertical coordinate, y, each understood modulo one. The number x itself is not a globally single-valued real function on the torus. If you walk once around the horizontal direction, x has advanced by one even though you have returned to the same point.

Its infinitesimal differential, however, is globally well-defined. The one-form called d x assigns the horizontal component of a tiny displacement. Integrating it once around a horizontal loop gives one; integrating it around a vertical loop gives zero. Similarly, the form d y measures vertical winding.

Both forms are closed. Neither is globally exact, because the integral of an exact one-form around a closed loop would be zero. The two forms therefore represent distinct cohomology classes. They are dual measurements of the two fundamental loop directions.

What if we combine the two measurements? The wedge product d x wedge d y is an area form. Integrated over the oriented torus, it gives one when the square has unit area. Its two-dimensional cohomology class is not zero. The product of two one-dimensional classes has discovered a two-dimensional feature.

### Multiplication has orientation built in

Switch the order of the two one-forms. The wedge product changes sign: d y wedge d x is the negative of d x wedge d y. A small parallelogram oriented horizontal-then-vertical is positive, while vertical-then-horizontal is negative in our chosen orientation.

Cohomology has a corresponding multiplication, the cup product. On de Rham classes it is represented by wedge product. The rule is graded commutativity: exchanging degrees p and q introduces a sign determined by their product. For two degree-one classes the sign is negative.

This is why the two independent generators of first cohomology on a torus do not behave like ordinary commuting variables. Their product remembers orientation. Over real coefficients, a degree-one class wedged with itself is zero. The mixed product of our two generators is not.

The dimensions of the cohomology groups of a space are called its Betti numbers. Betti numbers tell us that the torus has one class in degree zero, two in degree one, and one in degree two. The cup product tells us how those classes interact. Two spaces can have the same Betti numbers yet different cohomology rings. Multiplication contains genuinely additional information.

### From products of forms to crossings of loops

Now draw one horizontal loop and one vertical loop on the torus. After choosing representatives in general position, they cross at one point. Give both loops directions, and give the torus an orientation. At each transverse crossing, we can count plus one or minus one according to whether the two tangent directions agree with the orientation of the surface.

For the standard horizontal and vertical loops, the signed intersection number is plus one. Reverse one loop and it becomes minus one. Move either loop without changing its homology class and, provided crossings are counted with signs, the total remains the same. Pairs of crossings can be created or canceled, but they appear with opposite signs.

The connection to differential forms is Poincaré duality. An oriented submanifold defines a cohomology class of complementary degree. Intersecting two suitably positioned cycles is reflected algebraically by multiplying their dual classes and integrating over the whole manifold.

There is an easy sign trap here. A one-form that integrates to one along a particular loop is not automatically the Poincaré dual of that same loop. Integrating along cycles and taking the dual class defined by intersection are related notions, but they involve a complementary direction and an orientation convention. One must write the pairing rather than guess the sign from a drawing.

### Why the pairing is nondegenerate

On a closed oriented manifold of dimension n, Poincaré duality pairs degree k cohomology with degree n minus k cohomology. Over the real numbers, the pairing integrates the wedge product of representatives over the manifold. Nondegenerate means that a nonzero class can be detected by pairing it with some complementary class.

On our two-torus, any first-degree class can be expressed as a multiple of d x plus a multiple of d y. If the first multiple is nonzero, pairing with d y detects it. If the second is nonzero, pairing with d x detects it, with an orientation sign. No nonzero first-degree class is invisible to every complementary class.

The statement requires the hypotheses. Without compactness, orientation, or appropriate treatment of boundaries, a naive integral pairing can fail to have this property. For a manifold with boundary, absolute and relative cohomology play different roles. Over the integers, torsion also requires care: integration against real differential forms cannot detect torsion classes.

### A short look at four dimensions

For an oriented four-manifold, two-dimensional cohomology can pair with itself. The resulting intersection form is a bilinear form on the middle-degree cohomology, after treating torsion appropriately. Its signature, parity, and other properties can constrain the topology and smooth structure of the manifold.

That observation explains why later lectures about Donaldson invariants and Seiberg–Witten theory care so much about intersection forms and classes of embedded surfaces. They are not merely counting individual holes. They are studying how cycles coexist, intersect, and interact with the smooth geometry.

The torus is the small model in which the algebra can be seen completely. One-dimensional measurements multiply to give an area measurement. Oriented loop intersections give signed integers. Poincaré duality identifies these two ways of describing the same underlying interaction. Once this example is secure, advanced cohomological pairings have a concrete starting point.

## Fiber Bundles, Connections, and Curvature

In elementary geometry, a vector can be drawn as an arrow in a fixed plane. We can move it from one point to another without changing its components, because every tangent space of that plane has been identified with the same vector space. On a curved surface, that identification is no longer automatic. Vectors based at different points live in different tangent spaces. Even on a topologically simple space, a family of vector spaces can be arranged with a twist.

Fiber bundles provide a language for the family itself. Connections tell us how to compare neighboring fibers. Curvature measures the failure of that comparison to be independent of the route taken.

### A bundle looks like a product nearby

A fiber bundle is a space E equipped with a projection onto a base space B. Above a point b in the base sits the fiber: all points of E that project to b. The key local property is that around each point of the base, the bundle looks like a product of a neighborhood with a fixed typical fiber.

For a vector bundle, the fibers are vector spaces of a fixed dimension, and the local product maps are linear on each fiber. The tangent bundle of a smooth manifold is the central example. At each point, its fiber is the tangent space. When we collect all tangent vectors at all points, we obtain a new geometric space, with a projection that remembers which point each vector belongs to.

A local trivialization supplies coordinates for this construction. We choose a basis of vectors over a small open set and represent each vector by its coefficients in that basis. But bases chosen on overlapping neighborhoods need not agree. Their change-of-basis functions, called transition functions, encode how the bundle fits together globally.

### The Möbius strip: local simplicity, global twist

Take a rectangle and identify its two ends after giving one end a half-turn. The resulting Möbius strip is a real line bundle over a circle if we regard each short cross-section as a one-dimensional vector space. Locally there is no twist: over a short arc it is just an arc times a line. But if you follow the local choice of positive direction around the whole circle, it returns reversed.

Compare the cylinder. It is also a line bundle over a circle, but it is globally a product. The cylinder has a continuous nowhere-zero section: choose the same positive vector in every fiber. The Möbius line bundle does not. If we represent such a section by a nonzero real function along one traversal, the twist would require its final value to be the negative of its starting value. By continuity, a real function cannot do that without passing through zero.

This is a concrete obstruction to global triviality. Every local piece has a basis, yet no single continuous nonzero basis vector exists everywhere. It is why an object can be locally ordinary and globally different.

### Sections and the need for comparison

A section of a vector bundle assigns one vector in the fiber over each base point. A vector field on a smooth manifold is a section of its tangent bundle. Suppose such a section varies from point to point. We want to differentiate it.

Ordinary differentiation subtracts vector values at nearby points. But those vectors lie in different fibers, so subtraction is not defined until we choose a way to identify them. A connection supplies the missing rule.

For a smooth vector bundle, a covariant derivative maps a vector field X and a section s to another section, written nabla in the direction X of s. It is linear in X over smooth functions, linear in s over constants, and obeys a Leibniz rule: differentiating f times s gives the directional derivative of f times s, plus f times the covariant derivative of s. That extra term makes the construction compatible with ordinary calculus.

In a local frame, the rule looks like differentiation plus a matrix-valued one-form A. The ordinary derivative differentiates the coordinate components; A corrects for the changing local frame. Choosing a different frame changes the matrix A, even though the connection itself is geometric.

### Parallel transport

Once a connection is specified, we can transport a vector along a smooth path by requiring its covariant derivative along that path to vanish. This is parallel transport. Given a starting vector and suitable regularity, a linear differential equation determines its transported value.

Parallel transport along two different paths with the same endpoints may produce different results. That phenomenon is called holonomy. If you transport a tangent vector around a loop on a curved surface, the final vector can be rotated relative to the initial one. The comparison is not the familiar rotation of an arrow against some external coordinate axes; it is a property of the connection used to identify tangent spaces.

Parallel transport is additional structure. A bare topological vector bundle does not choose a preferred connection, and even a trivial bundle can carry connections with nonzero curvature.

### Curvature is the obstruction to commuting derivatives

A connection lets us differentiate a section along two vector fields X and Y. We can take the derivative along X and then Y, or reverse the order. The difference is not generally zero. After correcting for the Lie bracket of the vector fields, the resulting operator is the curvature of the connection.

In a local matrix frame, if the connection is written as d plus A, its curvature form is dA plus A wedge A. For a line bundle, the matrix multiplication issue disappears, and the formula reduces to dA. The curvature is geometric even though A changes with the choice of frame.

Consider a trivial complex line bundle over the plane. Give it the connection d plus i times x dy, where i is the imaginary unit. Its curvature is i times dx wedge dy. Parallel transport once around a counterclockwise rectangle changes a unit complex vector by the phase obtained from the negative exponential of i times the enclosed area. Two routes can differ even though the underlying bundle is just a product.

This illustrates an important distinction: twisting of the bundle is topological; curvature belongs to a chosen connection. They interact, but they are not the same data.

### Flat does not always mean globally trivial transport

A connection with zero curvature is called flat. On a sufficiently small simply connected neighborhood, flatness allows path-independent parallel transport. But global topology still matters. On a circle, a flat connection can have nontrivial holonomy around a full loop. Local curvature may vanish, while the global return map is nontrivial.

This mirrors the themes of topology we have already studied. Local exactness of a differential form need not imply global exactness. A local trivialization need not produce a global trivialization. In both cases, understanding how local choices fit together reveals the global obstruction.

Fiber bundles, connections, and curvature are therefore different layers of a single story. The bundle says what vector space lives at each point. The connection says how vectors are compared as we move. The curvature says what that comparison does around small loops. The same ideas appear in differential geometry, gauge theory, and modern topology, but their mathematical content begins with these precise distinctions.

## Bundle Transition Functions and Global Twisting

Hold a narrow strip of paper, give it half a twist, and join its ends. The result is a Mobius band. At every small patch of the central circle, the band looks like an ordinary interval attached to a piece of the circle. But as we travel around once, the transverse direction has been reversed. This is the simplest image of a fiber bundle that is locally ordinary and globally twisted.

A fiber bundle has a base space and a fiber sitting above each point. For a vector bundle, every fiber is a vector space of the same finite dimension. Over a sufficiently small open set, we can choose a trivialization: a smooth way to identify all the fibers there with a fixed vector space. The word local matters. The entire bundle need not admit one such identification covering the whole base.

### Two local descriptions of the same fiber

Suppose two trivializations overlap. Each one assigns coordinates to vectors in the same fiber. On the overlap, converting from one set of coordinates to the other is an invertible linear map. The map depends smoothly on the base point. Such maps are called transition functions.

For a real line bundle, the transition function is a nonzero real number at each point of the overlap. For a complex line bundle, it is a nonzero complex number. For a rank-r real vector bundle, it is an invertible r-by-r real matrix. These are not extra arbitrary decorations on top of a bundle. They encode how the different local product pictures fit together.

If three trivializations overlap, converting coordinates from the first to the third directly must agree with converting through the second. This compatibility is the cocycle condition. Without it, a journey through different charts could produce inconsistent fiber coordinates depending on the sequence of charts used. With it, one can build a global bundle by gluing local products according to the transition functions.

### The Mobius line bundle

Think of the Mobius band as a real line bundle over a circle, with the fiber an entire copy of the real line rather than only a narrow paper interval. Start from the product of an interval of angles and the real line, and identify the two ends so that the fiber coordinate changes sign: the vector t at the first end is identified with the vector negative t at the other end.

Locally nothing went wrong. Every short arc of the circle has a product neighborhood. Globally, after one complete circuit, the chosen real basis of the fiber reverses orientation. Could we choose a continuous, nowhere-zero vector in each fiber, making a global basis? Suppose we could. In the interval description it would be a continuous nonzero real-valued function that must change sign between the endpoints under the gluing rule. By the intermediate value theorem, it would have to vanish somewhere. That contradiction shows there is no global nonzero section, and therefore no global product trivialization as a real line bundle.

Notice a refinement. For two overlapping arcs covering the circle, their intersection has two disconnected pieces. One can use a transition function with opposite signs on those components. It would be wrong to summarize the Mobius twist as one globally defined nonzero real function that continuously changes from positive to negative on a connected overlap. Such a sign change would have to pass through zero and cease to be invertible. The disconnected overlap is how the topology enters.

### Gauge choices are not physical twists

A local trivialization is not unique. On any patch we may change the basis of the fiber by a smoothly varying invertible matrix. This changes the transition functions according to the corresponding basis changes. Two sets of transition data related in this way describe isomorphic bundles. A complicated transition matrix may be removable by choosing better frames. Its mere complexity does not establish genuine global twisting.

For a real line bundle over the circle, the important information is the sign accumulated around a circuit. A real line bundle with no sign reversal is trivial; one with sign reversal is the Mobius type. Complex line bundles over the circle behave differently: because nonzero complex numbers can be continuously rotated from one phase to another, all complex line bundles over the circle are topologically trivial. The scalar field changes the possible twisting.

### A two-dimensional base can support another kind of twist

Now cover a sphere by northern and southern disk-like patches whose overlap is an equatorial band. Consider complex line fibers and choose a frame on each patch. On the overlap, let the southern frame rotate in complex phase once as we go around the equator, relative to the northern frame. The phase does not come back having traced a contractible loop in the nonzero complex numbers: its winding number is one.

This construction produces a nontrivial complex line bundle over the sphere. Different integers of phase winding produce different isomorphism classes of complex line bundles over the sphere. This is the clutching construction. Its invariant will later appear as the first Chern number, obtained by integrating a curvature two-form over the sphere.

Why does a complex line bundle over the circle trivialize while a complex line bundle over the sphere may not? The sphere construction glues two disks along an overlap whose essential loop carries the transition map. Its winding cannot necessarily be removed by changing frames over the disks. The topology of the base and the structure group of the fibers interact. We cannot infer one case from the other merely by saying both have circular directions somewhere in the picture.

### Sections and the tangent bundle

A section assigns one vector in the fiber above each point. A vector field on a manifold is a section of its tangent bundle. A local coordinate chart supplies coordinate basis vector fields and therefore a local frame of the tangent bundle. On overlaps, these frames are related by Jacobian matrices. That makes the tangent bundle a particularly important example of transition-function gluing.

Whether a bundle admits a global frame is a global topological question. The tangent bundle of the sphere has local frames in every chart, but there is no smooth nowhere-zero tangent vector field on the two-sphere. That fact, often pictured by the impossibility of combing a hairy ball without a cowlick, is a genuine theorem. It reminds us that a global choice of basis can fail even though every local patch looks harmless.

Bundles separate two kinds of information. The fiber tells us what kind of object can live at a point: a line, a plane, or another vector space. The transition functions tell us how local coordinates on those fibers are identified. The pattern of those identifications determines whether a global trivialization exists. This is what it means for geometry to be locally simple but globally twisted.

## Covariant Derivatives and Parallel Transport

Picture a small arrow drawn on the surface of a sphere. Move it along a path, always trying to keep it parallel. If the path is a loop, the arrow may return rotated. What did it mean to keep it parallel in the first place? The arrow at the beginning lives in one tangent plane, while the arrow at a later point lives in another. We cannot simply subtract them as vectors in one shared plane without making an additional choice.

That missing choice is a connection. A connection specifies a rule for differentiating a section of a bundle in a direction tangent to the base. Once we have that rule, we can define parallel transport along a curve by demanding that the covariant derivative of the moving vector vanish. This turns the geometric idea of maintaining direction into a differential equation.

### Ordinary derivatives assume a fixed vector space

In a trivial bundle over the real line, every fiber is a copy of the same vector space. A section is an ordinary vector-valued function. Differentiating it component by component makes sense because the product structure has identified all fibers in advance. But choose a different smoothly varying basis along the line. A constant geometric vector will generally acquire changing components. The ordinary derivative of those new components need not vanish.

We need a derivative that compensates for the changing basis. Locally a connection does this by adding a matrix-valued one-form A to the ordinary differential. When the section has component column v, its covariant derivative has components d v plus A times v. The one-form A tells us how the chosen frame itself varies relative to the connection.

A connection must satisfy a product rule. If f is a scalar function and s is a section, the covariant derivative of f times s is d f times s plus f times the covariant derivative of s. This resembles the ordinary Leibniz rule, but the output now carries a cotangent direction as well as a fiber component.

### Parallel transport becomes an initial-value problem

Give a smooth curve gamma and a vector in the fiber at its starting point. Parallel transport asks for a section along the curve whose covariant derivative in the direction of the curve's velocity is zero and whose starting value is the given vector. In a local frame, if v of t is the component column, the equation says the ordinary derivative of v plus A evaluated on the curve's velocity, multiplied by v, equals zero.

This is a linear ordinary differential equation. On a finite interval with a smooth connection and smooth path, it has a unique solution for each initial vector. The final vector depends linearly and invertibly on the initial vector. Traversing the path backward gives the inverse transport map; following two paths in sequence composes their transport maps.

What happens when the curve crosses a chart boundary? We switch local frames and transform the components. The differential equation changes in a compatible way. The resulting geometric transport map is independent of the local frames used to calculate it.

### A connection that rotates phases

For a complex line bundle, each fiber is one-dimensional over the complex numbers. Choose a unitary frame over the plane. Then a metric-compatible connection can be expressed as the ordinary differential plus i times a real one-form, where i is the imaginary unit. The parallel transport equation changes only the phase of a vector; its magnitude stays constant.

Take the simple connection given by d plus i times x d y. If a path moves horizontally, d y along its velocity is zero, so there is no phase change on that segment. If it moves vertically at fixed x, the phase change is proportional to x times the vertical displacement. Travel counterclockwise around a rectangle. The four segments together change a unit vector by the complex phase whose exponent is negative i times the enclosed area.

This is a valuable example because the underlying line bundle is completely trivial. Every fiber can be globally identified with the complex numbers. Yet our chosen connection has nonzero curvature and produces nontrivial transport around loops. Topological twisting of the bundle and geometric bending of the connection are distinct.

### How local connection forms change

If we replace a local frame by one related through an invertible matrix g, a section's component column changes by the inverse matrix. To keep the covariant derivative geometric, the connection matrix cannot transform by simple conjugation alone. There is an extra term involving the derivative of g. In the language of gauge theory, that is the inhomogeneous gauge transformation law.

For a complex line with a unitary change of frame by the phase exponential of i times a local function chi, the real potential a changes to a plus d chi, with our choice of connection sign. The local potential therefore depends on the frame. But its exterior derivative does not change, since differentiating d chi once more gives zero. We will call that exterior derivative the curvature in the line-bundle case.

This is an important distinction for physical interpretations: one must not treat the entries of a local connection matrix as direct frame-independent observables. Parallel transport around a closed loop and curvature transform in controlled ways; the matrix of connection coefficients depends on the chosen local basis.

### Parallel along a circle

There is an even simpler global example. On the trivial complex line bundle over a circle, let the connection be d plus i times a constant real number a times the global angular one-form. The curvature is zero because every two-form on a circle vanishes. Nonetheless, parallel transport around one full positively oriented turn multiplies a vector by the phase exponential of negative two pi i a. For many values of a this phase is not one.

So flatness does not imply trivial holonomy. A flat connection is locally equivalent to an ordinary derivative on a small simply connected patch, but going around a noncontractible loop can still accumulate phase. If we change the frame by a globally defined phase that winds an integer number of times around the circle, the coefficient a changes by that integer while the full-turn holonomy stays the same.

### The Levi-Civita connection is a special case

On a Riemannian manifold we can ask for a connection on the tangent bundle that preserves the metric under transport and has no torsion. These requirements single out the Levi-Civita connection. Its parallel transport preserves lengths and angles. For the sphere, such transport around a closed path can rotate a tangent arrow even when the path ends where it began. The rotation is related to the sphere's intrinsic curvature.

But it would be a mistake to infer that every vector bundle comes with a canonical connection or that every connection is Levi-Civita. A general vector bundle admits many connections, and the geometry under study determines which properties we require. The connection supplies a rule for comparison that the bare bundle does not provide.

Covariant derivatives, parallel transport, and curvature are successive aspects of one construction. The connection tells us how to differentiate sections. Its differential equation tells us how to carry vectors along paths. Comparing transport around different routes reveals geometric information that ordinary pointwise fiber coordinates cannot see.

## Curvature, Holonomy, and Chern Numbers

Two different paths can carry a vector from one point to another. If we use a connection to parallel transport the vector along each path, the final vectors need not agree. Going forward on one path and returning on the other gives a loop, and the discrepancy becomes a transformation of the original fiber. We call that transformation holonomy.

For a complex line bundle with a unitary connection, holonomy is multiplication by a complex number of absolute value one: a phase. For higher-rank bundles it can be a matrix. Curvature describes the first-order departure from path independence around very small loops. But curvature also has a global role. Properly normalized, its integral over a closed oriented surface can be an integer determined by the topology of the bundle.

### Curvature as failure to commute

A connection lets us differentiate a section along vector fields X and Y. We may first differentiate in X and then Y, or do them in the opposite order. Even on a curved manifold, the fields themselves may fail to commute, so we must subtract the covariant derivative in the direction of their Lie bracket as well. What remains is the curvature operator.

The result acts linearly on each fiber. In a local frame with connection d plus a matrix-valued one-form A, the curvature is the matrix-valued two-form d A plus A wedge A. The second term matters because matrices need not commute. In a complex line bundle, the matrices are just scalar one-by-one matrices and A wedge A vanishes, leaving curvature d A.

If we change the local frame, the connection form acquires an extra derivative term. The curvature instead transforms by conjugation, so its geometric content is well defined. In a line bundle conjugation does nothing, and the curvature is a globally defined imaginary-valued two-form. This is why curvature, unlike the local connection potential, can be integrated globally without choosing one frame for the whole surface.

### A rectangle measures local curvature

Recall the connection d plus i times x d y on the trivial complex line over the plane. Its curvature is i times d x wedge d y. Transport around a counterclockwise rectangle of area S multiplies the initial vector by exponential of negative i times S. For a very small rectangle, expand the exponential: the leading deviation from one is negative i times S. Curvature is the coefficient that measures this small-loop effect.

For a line bundle, Stokes' theorem makes the relationship exact whenever a loop bounds a region on which we have a single smooth frame: the holonomy phase is exponential of minus the curvature integral over that region. For a higher-rank noncommuting connection, the relation is subtler. Holonomy involves path ordering, and one cannot replace it in general by the ordinary exponential of a curvature integral without further conditions.

We should also remember the global caveat. A flat connection has zero infinitesimal curvature but may retain nontrivial holonomy around a loop that cannot be contracted to a point. The circle with a constant angular connection provided an explicit example. Local curvature and global holonomy are related but not interchangeable invariants.

### From phase to integer

Now let L be a Hermitian complex line bundle over a closed oriented surface. Choose a unitary connection. In each unitary frame its curvature is an imaginary-valued two-form, and these local expressions agree on overlaps. Multiply the curvature by the imaginary unit and divide by two pi. With the sign convention used in this lecture, that gives a real closed two-form representing the first Chern class of L in de Rham cohomology.

The first Chern number is the integral of that real two-form over the oriented surface. The remarkable claim is that the answer is always an integer. Changing the unitary connection can change the curvature point by point, but not the integer. We have moved from an arbitrary differential-geometric choice, the connection, to a topological invariant of the line bundle.

Why an integer? Cover the sphere by a northern and a southern disk, with an overlap around the equator. Choose a unitary frame in each disk. On the overlap the two frames differ by a circle-valued transition function. As we go around the equator, that transition phase must make an integer number of full turns. It has a winding number.

The two local connection potentials differ by the derivative of the transition phase. Integrating curvature over the two hemispheres and applying Stokes turns the surface integral into a difference of line integrals on their common equator. That difference is exactly the phase winding, after the two-pi normalization and sign convention are accounted for. Integrality is not a numerical coincidence. It follows from the single-valuedness of the transition function on a full loop.

### One explicit unit of Chern number

Use spherical coordinates with colatitude theta measured from the north pole and longitude phi. Choose a connection on the northern disk with an imaginary-valued potential proportional to minus one minus cosine theta, times d phi. On the southern disk use a potential proportional to one plus cosine theta, times d phi. The coefficients are arranged so that each potential is smooth at its own pole despite the coordinate singularity of longitude.

Both produce the same curvature, equal to negative one-half times the imaginary unit times sine theta d theta wedge d phi. After multiplying by i and dividing by two pi, the Chern form becomes one over four pi times the ordinary area element on the unit sphere. That normalized area integrates to one. The local frames are related around the equator by a phase that winds once. These are two calculations of the same integer: one from curvature, one from the transition function.

The signs depend on orientations, on whether we discuss a bundle or its dual, and on the connection convention. Reversing the orientation of the sphere reverses the integral. Taking the dual line bundle reverses the first Chern class. The important invariant statement is that a globally defined integer results once all conventions are fixed consistently.

### What a nonzero number proves

A trivial complex line bundle has a global nowhere-zero frame. In such a frame its connection is represented by one globally defined imaginary-valued one-form A, and its curvature is d A. On a closed surface, Stokes says the integral of d A is zero. Therefore a nonzero first Chern number obstructs triviality. We cannot choose a global frame for that bundle.

The converse needs care. On a closed oriented surface, complex line bundles are classified by their integral first Chern class, so zero first Chern number means the bundle is trivial there. In more general settings, a single number obtained by pairing with one surface may not detect every bundle class. For higher-rank bundles and higher-dimensional bases, other characteristic classes and pairings are needed. Even a trivial bundle can still carry a non-flat connection, so Chern number zero does not mean curvature zero everywhere.

The same language extends to matrix-valued curvature. Certain invariant polynomial expressions in the curvature produce closed forms whose cohomology classes are independent of the chosen connection. This is the idea of Chern-Weil theory. The first Chern class of a complex line bundle is the most accessible example because the trace and matrix commutator issues collapse to ordinary differentiation.

We began with the failure of two paths to transport a vector identically. We ended with an integer that cannot change under a smooth adjustment of the connection. Holonomy measures transport around loops. Curvature measures its local infinitesimal behavior. The first Chern number assembles curvature over a closed surface and records global twisting. This is a concrete entry point into the geometry behind gauge theory, where local potentials, observable transport and topological sectors have to be distinguished carefully.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Poincaré Duality: Why a Manifold's Dimensions Pair Up

**Track:** Topology and Geometry. **Background:** homology, cohomology, cup products, orientation, manifolds. **Central question:** why should cohomology in one degree know about homology in the complementary degree?

#### Mathematical companion (not spoken)

For a connected, closed, oriented \(n\)-manifold \(M\), the chosen fundamental class \([M]\in H_n(M;\mathbb Z)\) induces isomorphisms
\[D_M:H^k(M;\mathbb Z)\xrightarrow{\ \frown[M]\ }H_{n-k}(M;\mathbb Z)\quad\text{for all }k.\]
For a compact orientable manifold with boundary, one Poincaré–Lefschetz form is \(H^k(M;\mathbb Z)\cong H_{n-k}(M,\partial M;\mathbb Z)\), and the complementary form is \(H^k(M,\partial M;\mathbb Z)\cong H_{n-k}(M;\mathbb Z)\).

**Torus:** \(H^*(T^2;\mathbb Z)\cong\Lambda_{\mathbb Z}(\alpha,\beta)\), with \(|\alpha|=|\beta|=1\), \(\alpha\smile\beta=-\beta\smile\alpha\), and orientation chosen so \(\langle\alpha\smile\beta,[T^2]\rangle=1\). For a closed orientable genus-\(g\) surface \(\Sigma_g\), \(H_1\cong\mathbb Z^{2g}\), with nondegenerate skew-symmetric intersection form on the free part.

**Boundary example:** \(H_2(D^2;\mathbb Z)=0\) while \(H_2(D^2,S^1;\mathbb Z)\cong\mathbb Z\). Ordinary top homology cannot replace the relative fundamental class. For nonorientable manifolds, \(\mathbb Z/2\)-coefficient duality or orientation local coefficients give appropriate replacements. For noncompact oriented manifolds, compactly supported cohomology enters: \(H_c^k(M;\mathbb Z)\cong H_{n-k}(M;\mathbb Z)\), with the usual hypotheses and correct cohomology theory.

##### Exercises with answers

1. What is the dual of \(H^0(M;\mathbb Z)\cong\mathbb Z\) in a connected closed oriented \(n\)-manifold? **Answer:** \(H_n(M;\mathbb Z)\cong\mathbb Z\), via the fundamental class.
2. Why can an oriented torus have two independent degree-one classes? **Answer:** its first homology and cohomology both have rank two, and the two loops pair by a nondegenerate intersection form.
3. Does integral duality in this form apply directly to a Möbius band? **No:** it is nonorientable and has boundary; use suitable coefficients/local systems and relative groups.
4. Why does \(D^2\) not contradict duality when \(H_2(D^2)=0\)? **Answer:** the disk has boundary; its fundamental class is relative in \(H_2(D^2,\partial D^2)\).

##### Reading and source notes

- Allen Hatcher, [*Algebraic Topology*, Section 3.3](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html), orientation, cap products, duality theorem, and boundary variants.
- [Hatcher's cap-product and duality excerpt](https://pi.math.cornell.edu/~hatcher/AT/ATcapprod.pdf), naturality and Mayer–Vietoris proof architecture.
- [MIT 18.905 Algebraic Topology I](https://ocw.mit.edu/courses/18-905-algebraic-topology-i-fall-2016/), homology and cohomology foundations.

### Cup Products and Intersection Numbers: What Two Holes Say to Each Other

**Track:** Topology and Geometry. **Background:** cycles, cohomology, closed forms, the circle and torus. **Central question:** why do the dimensions of cohomology groups not tell the whole story?

#### Mathematical companion (not spoken)

For \(T^2=\mathbf R^2/\mathbf Z^2\) oriented by \(dx\wedge dy\), \(H^*(T^2;\mathbf R)\) is the exterior algebra on \(a=[dx]\), \(b=[dy]\): \(a\wedge a=b\wedge b=0\), \(a\wedge b=-b\wedge a\), and \(\int_{T^2}a\wedge b=1\). The Betti numbers are \((1,2,1)\).

For a closed oriented smooth n-manifold, the real Poincaré pairing is \(H^k_{\mathrm{dR}}(M)\times H^{n-k}_{\mathrm{dR}}(M)\to\mathbf R\), \(([\alpha],[\beta])\mapsto\int_M\alpha\wedge\beta\); Poincaré duality says it is nondegenerate. The cup product on singular cohomology corresponds to wedge product under the de Rham isomorphism. If \(A,B\) are oriented cycles meeting transversely in complementary dimensions, then \(A\cdot B=\int_M\operatorname{PD}(A)\smile\operatorname{PD}(B)\), with consistent orientation and degree conventions.

For the coordinate loops \(A\) (positive x direction) and \(B\) (positive y direction), \(A\cdot B=+1\). Under conventions where \(\int_M\operatorname{PD}(C)\wedge\beta=\int_C\beta\), the duals are \(\operatorname{PD}(A)=-[dy]\), \(\operatorname{PD}(B)=[dx]\), so \(\int_M(-dy)\wedge dx=1\). This illustrates why integration-dual and Poincaré-dual are not the same identification.

##### Exercises with answers

1. **Product.** Evaluate \(\int_{T^2}dy\wedge dx\). **Answer:** \(-1\) for the orientation \(dx\wedge dy\).
2. **Detection.** If \(u=3a+2b\), compute \(\int u\wedge a\) and \(\int u\wedge b\). **Answer:** \(-2\) and \(3\), respectively.
3. **Intersection.** What is the intersection number after reversing the vertical loop's orientation? **Answer:** \(-1\).
4. **Hypotheses.** Why does real de Rham pairing not see \(H_1(\mathbf{RP}^2;\mathbf Z)=\mathbf Z/2\)? **Answer:** Torsion maps to zero with real coefficients.

##### Sources and further reading

- Allen Hatcher, [Algebraic Topology, Chapter 3: Cohomology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html).
- MIT OpenCourseWare, [18.966 Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/).
- Overviews: [Cup product](https://en.wikipedia.org/wiki/Cup_product), [Intersection theory](https://en.wikipedia.org/wiki/Intersection_theory).

### Fiber Bundles, Connections, and Curvature

**Track:** Topology and Geometry. **Background:** quotient spaces, smooth manifolds, tangent spaces, differential forms. **Central question:** how can a family of vector spaces twist globally, and what extra structure lets us compare vectors at different points?

#### Mathematical companion (not spoken)

A rank-\(r\) smooth vector bundle \(\pi:E\to M\) is locally isomorphic, fiberwise linearly, to \(U\times\mathbb F^r\). On overlapping trivializations, frames differ by smooth transition maps \(g_{\alpha\beta}:U_\alpha\cap U_\beta\to\operatorname{GL}(r,\mathbb F)\) satisfying cocycle relations.

A connection \(\nabla\) acts on smooth sections and obeys \(\nabla_X(fs)=X(f)s+f\nabla_X s\). In a local frame, \(\nabla=d+A\). With frame transformation \(e'=eg\),
\[A'=g^{-1}Ag+g^{-1}dg,\qquad F_\nabla=dA+A\wedge A,\qquad F'=g^{-1}Fg.\]
In invariant form,
\[F_\nabla(X,Y)s=(\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]})s.\]
For a complex line bundle over \(\mathbb R^2\) with \(A=i x\,dy\), \(F=i\,dx\wedge dy\). On a counterclockwise rectangle \(\gamma\) enclosing area \(ab\), parallel transport has scalar holonomy \(e^{-\oint_\gamma A}=e^{-iab}\) (with the stated sign convention).

**Möbius example:** the real line bundle \(([0,2\pi]\times\mathbb R)/((0,t)\sim(2\pi,-t))\to S^1\) is locally trivial but admits no everywhere-nonzero continuous section. Such a section would correspond to a continuous \(f\) on the interval with \(f(2\pi)=-f(0)\) and no zeros, contradicting the intermediate value theorem.

##### Exercises with answers

1. Can a trivial line bundle have a connection with nonzero curvature? **Yes:** \(A=i x\,dy\) above is an explicit example.
2. Is \(A\) invariant under change of frame? **No:** it changes by \(g^{-1}Ag+g^{-1}dg\), while curvature transforms by conjugation.
3. Does curvature zero imply trivial holonomy around every global loop? **No:** a flat connection on a nonsimply-connected base can have nontrivial global holonomy.
4. What is a section of the tangent bundle? **Answer:** a vector field, assigning a tangent vector to each point.

##### Reading and source notes

- Allen Hatcher, [*Vector Bundles & K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), bundles, transition functions and global nontriviality.
- John Baez and Javier P. Muniain, [*Gauge Fields, Knots and Gravity*](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/PhilPhysics/Baez%2BMuniain1994GaugeFieldsKnots%2BGravity.pdf), vector-bundle connections and curvature.
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), smooth bundle and connection prerequisites.

### Bundle Transition Functions and Global Twisting

**Track:** Topology and Geometry. **Background:** manifolds, smooth charts, linear algebra. **Question:** how can every local fiber look like a product while the entire bundle is twisted?

#### Mathematical companion (not spoken)

Choose local frames \(e_i\) on \(U_i\subset M\) and write \(e_j=e_i g_{ij}\) on overlaps, with \(g_{ij}:U_i\cap U_j\to GL(r,\mathbb F)\). Then
\[g_{ii}=I,\quad g_{ji}=g_{ij}^{-1},\quad g_{ij}g_{jk}=g_{ik}\text{ on triple overlaps}.\]
A change of frame \(e'_i=e_i h_i\) yields \(g'_{ij}=h_i^{-1}g_{ij}h_j\). The equivalence class of transition data, not an individual matrix entry, represents the bundle.

**Mobius line bundle:** \(E=([0,2\pi]\times\mathbb R)/((0,t)\sim(2\pi,-t))\). A nonvanishing section would yield a nonzero continuous function \(f:[0,2\pi]\to\mathbb R\) with \(f(2\pi)=-f(0)\), impossible by the intermediate value theorem.

**Complex lines on \(S^2\):** two disk trivializations glue on the equator through \(g:S^1\to U(1)\), \(g(e^{i\phi})=e^{in\phi}\). The homotopy class is its integer degree \(n\); fixing orientation and frame conventions fixes the sign of the associated Chern number.

##### Check your understanding

1. Why must transition matrices be invertible? **Answer:** they describe changes of basis within the same fiber.
2. Is a nonconstant transition function automatically evidence of a nontrivial bundle? **No:** a change of local frames may simplify it to the identity.
3. Why is the complex Mobius-looking gluing over \(S^1\) trivializable? **Answer:** the complex frame can rotate continuously to absorb the sign; complex line bundles over \(S^1\) are trivial.

##### Reading and sources

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), transition functions, clutching construction and characteristic classes.
- Overview: [Vector bundle](https://en.wikipedia.org/wiki/Vector_bundle), [Clutching construction](https://en.wikipedia.org/wiki/Clutching_construction), [Mobius strip](https://en.wikipedia.org/wiki/M%C3%B6bius_strip).

### Covariant Derivatives and Parallel Transport

**Track:** Topology and Geometry. **Background:** vector bundles, tensor fields, differential equations. **Question:** how can vectors in different fibers be compared along a path?

#### Mathematical companion (not spoken)

A connection \(\nabla:\Gamma(E)\to\Omega^1(M;E)\) satisfies \(\nabla(fs)=df\otimes s+f\nabla s\). In a local frame \(e\), \(\nabla=d+A\). For \(e'=eg\), \(v'=g^{-1}v\), and
\[A'=g^{-1}Ag+g^{-1}dg.\]
Along a smooth path \(\gamma:[0,1]\to M\), parallel transport solves
\[\dot v(t)+A_{\gamma(t)}(\dot\gamma(t))v(t)=0.\]

For a unitary complex line connection \(\nabla=d+ia\) with real \(a\), the transport factor is \(\exp(-i\int_\gamma a)\). If \(a=x\,dy\), then on a counterclockwise rectangle of area \(S\), the factor is \(e^{-iS}\). On \(S^1\) with \(a=c\,d\theta\), \(F=0\) and the full-turn factor is \(e^{-2\pi ic}\). A gauge \(g=e^{ik\theta}\) for \(k\in\mathbb Z\) changes \(c\mapsto c+k\) without changing holonomy.

##### Check your understanding

1. Does parallel transport on a line bundle preserve lengths automatically? **No:** only if the connection is compatible with a chosen Hermitian or Euclidean fiber metric.
2. Can a trivial bundle carry a curved connection? **Yes:** \(d+i x\,dy\) on \(\mathbb R^2\times\mathbb C\).
3. Does zero curvature on a circle force full-turn holonomy one? **No:** \(d+ic\,d\theta\) provides counterexamples.

##### Reading and sources

- John Baez and Javier P. Muniain, [Gauge Fields, Knots and Gravity](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/PhilPhysics/Baez%2BMuniain1994GaugeFieldsKnots%2BGravity.pdf), connections and transport.
- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Connection (vector bundle)](https://en.wikipedia.org/wiki/Connection_(vector_bundle)), [Parallel transport](https://en.wikipedia.org/wiki/Parallel_transport).

### Curvature, Holonomy, and Chern Numbers

**Track:** Topology and Geometry. **Background:** bundles, connections, differential forms and Stokes' theorem. **Question:** how can local curvature reveal a global integer associated with a complex line bundle?

#### Mathematical companion (not spoken)

For \(\nabla=d+A\) in a frame, \(F_\nabla=dA+A\wedge A\), and with \(e'=eg\), \(F'=g^{-1}Fg\). On a Hermitian complex line bundle with a unitary connection, \(F\in i\Omega^2(M;\mathbb R)\), \(F=dA\) locally and the normalized real Chern form is
\[c_1(\nabla)=\frac{i}{2\pi}F.\]
With this convention its class is the image of \(c_1(L)\in H^2(M;\mathbb Z)\) in real de Rham cohomology. On a closed oriented surface \(\Sigma\),
\[\langle c_1(L),[\Sigma]\rangle=\frac{i}{2\pi}\int_\Sigma F\in\mathbb Z.\]

**Unit-charge sphere calculation.** Use \(0\le\theta\le\pi\), \(0\le\phi<2\pi\) and the standard orientation \(\sin\theta\,d\theta\wedge d\phi\). On northern/southern patches take
\[A_N=-\frac{i}{2}(1-\cos\theta)\,d\phi,\qquad A_S=\frac{i}{2}(1+\cos\theta)\,d\phi.\]
Both yield \(F=-\frac i2\sin\theta\,d\theta\wedge d\phi\). On the equatorial overlap, \(A_S-A_N=i\,d\phi\), corresponding to \(g=e^{i\phi}\) for \(e_S=e_Ng\). Thus
\[\frac{i}{2\pi}\int_{S^2}F=\frac1{4\pi}\int_0^{2\pi}\!\int_0^\pi\sin\theta\,d\theta\,d\phi=1.\]
For \(U(1)\) holonomy in a local frame, \(\operatorname{Hol}(\partial S)=\exp(-\int_S F)\) when the loop and a spanning surface lie in a single trivializing patch and orientations agree. For general higher-rank connections, a path-ordered exponential is needed.

##### Check your understanding

1. Can a line bundle with \(c_1=1\) over \(S^2\) have a global nonvanishing frame? **No:** that would make it trivial and give Chern number zero.
2. If a connection on a trivial line bundle has nonzero curvature, must its Chern number over a closed surface be nonzero? **No:** global curvature is exact and integrates to zero.
3. Does flatness force all global loop holonomies to be identity? **No:** noncontractible loops can support nontrivial flat holonomy.

##### Reading and sources

- John Baez and Javier P. Muniain, [Gauge Fields, Knots and Gravity](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/PhilPhysics/Baez%2BMuniain1994GaugeFieldsKnots%2BGravity.pdf), curvature and holonomy.
- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), line bundles and characteristic classes.
- E. Meinrenken, [Sign Conventions](https://www.math.toronto.edu/mein/teaching/notes/signs.pdf), normalized first Chern form and sign comparisons.
- Overview: [First Chern class](https://en.wikipedia.org/wiki/Chern_class#First_Chern_class), [Holonomy](https://en.wikipedia.org/wiki/Holonomy).
