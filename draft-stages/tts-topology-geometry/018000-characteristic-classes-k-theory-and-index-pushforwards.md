# Characteristic classes, K-theory, and index pushforwards

<!-- BEGIN SPOKEN LECTURE -->

# Characteristic classes, K-theory, and index pushforwards

## Characteristic Classes: Detecting the Twist in a Bundle

A line bundle looks like an ordinary line when viewed near any one point. But the Möbius line bundle over a circle cannot be given a continuous global choice of a nonzero vector. Local frames exist and global frames do not. How can we measure this failure without relying on a picture of a twisted band?

Characteristic classes provide the answer. They assign cohomology classes to vector bundles. These classes are insensitive to the choice of local coordinates and respect maps between base spaces. They translate global twisting into algebraic invariants that can be calculated, compared, and sometimes used to prove a global construction impossible.

### A loop that reverses a vector

Start with a real line bundle over a circle. If you carry a nonzero vector once around the circle and return with its sign reversed, the line bundle is Möbius rather than trivial. The reversal is not a property of the local line at any point. It appears only after following the loop around the entire base.

The first Stiefel–Whitney class captures this obstruction. It lives in first cohomology with coefficients modulo two. For a real line bundle, it completely classifies the bundle when the base is a reasonable topological space, such as a paracompact space. On the circle there are exactly two classes: zero for the trivial line, and the nonzero class for the Möbius line.

The same first class for a higher-rank real vector bundle measures its orientability. It vanishes exactly when the bundle admits a consistent orientation, provided we work in the usual setting of real vector bundles over paracompact spaces. For the tangent bundle of a manifold, this gives an algebraic test for whether the manifold is orientable.

The class is a global invariant, but it has a very concrete source. Choose local frames on patches. On overlaps, transition matrices relate the frames. Their determinant signs record whether orientation flips. On triple overlaps these signs satisfy a consistency condition, so they determine a cohomology class. Changing the local frames changes the representative of the class, but not the class itself.

### The Euler class and zeros of vector fields

The first Stiefel–Whitney class detects orientation. What if a bundle is orientable but still has no nowhere-vanishing section? For an oriented real rank-n vector bundle, there is an Euler class in degree n integral cohomology. A nonzero Euler class obstructs a nowhere-zero section.

Take the tangent bundle of the two-sphere. A section of this bundle is a tangent vector field. If such a field never vanished, one could comb every tangent direction continuously without a bald spot. The hairy-ball theorem says this is impossible. The Euler class explains the obstruction in cohomological terms.

Evaluate the Euler class of the tangent bundle on the fundamental class of the sphere. The result is the Euler characteristic, which is two. The nonzero value proves that every continuous tangent vector field on the sphere must vanish somewhere. On a torus, the Euler characteristic is zero, and indeed a torus admits nowhere-zero tangent vector fields. These two facts are compatible, but the general converse from vanishing Euler class to existence of a nonzero section requires dimensional and other hypotheses; it is not an unrestricted equivalence for all bundles over all spaces.

This connects directly with Gauss–Bonnet. On an oriented Riemannian surface, differential geometry represents the Euler class of the tangent bundle using Gaussian curvature. Integrating that curvature representative recovers Euler characteristic. The curvature formula and the topological obstruction are two realizations of the same underlying class.

### Complex bundles have their own invariants

Complex vector bundles have Chern classes. The first Chern class of a complex line bundle belongs to integral second cohomology. For suitable spaces, it completely classifies complex line bundles. The class of a tensor product is the sum of the classes of the two factors. This is a particularly clean relationship between a geometric operation and cohomological addition.

The complex projective line is topologically a sphere. It carries a tautological complex line bundle whose first Chern class is a generator, up to the conventional choice of sign. In contrast, every complex line bundle over the ordinary circle is topologically trivial, because the circle has no nonzero second integral cohomology. Real line bundles over that circle can twist, but complex line bundles cannot twist in this particular way.

That contrast is a useful warning against treating all vector bundles alike. The coefficient field changes the relevant structure group and therefore the characteristic classes that can appear.

### Why curvature is not the whole story

A connection on a bundle allows us to compare vectors along paths, and its curvature measures the failure of infinitesimal parallel transport to commute. For complex vector bundles, certain differential forms built from curvature represent the real images of Chern classes in de Rham cohomology. For an oriented surface, a curvature form similarly represents the real Euler class.

But the topology of a bundle is not always visible in curvature forms alone. The Möbius real line bundle can carry a flat connection while its first Stiefel–Whitney class remains nonzero. Its twist is a two-valued holonomy effect, invisible to differential forms with real coefficients that detect only curvature. Torsion classes are another general source of information lost when integral cohomology is replaced by real cohomology.

Thus characteristic classes should not be reduced to a recipe for integrating curvature. Some classes have differential-form representatives after passing to real coefficients. Others are intrinsically integral or modulo-two phenomena and require different tools.

### Natural behavior and calculation

Characteristic classes are natural under pullback. If a bundle is pulled back along a continuous map, the characteristic classes of the new bundle are the pullbacks of the original classes. This lets us calculate complicated examples by comparing them with standard spaces and universal bundles.

They also obey product rules. Stiefel–Whitney classes assemble into a total class whose value on a direct sum is the product of the total classes of the summands. Chern classes satisfy an analogous Whitney-sum rule for complex bundles. For line bundles, these operations reduce to simpler additions and products, but in higher rank they give substantial constraints on how bundles may split.

An immediate application is obstruction by contradiction. Suppose we claim that a vector bundle admits a global frame. A globally framed bundle is trivial. A trivial bundle has no positive-degree characteristic classes. Therefore a computed nonzero class disproves the claim. The method avoids trying every possible frame; it rules all of them out at once.

### A language for global impossibility

The Möbius twist, the impossibility of combing a sphere, and the nontriviality of complex line bundles over a projective line are different examples of one theme. Local triviality does not imply global triviality. Characteristic classes describe the obstruction in cohomology, where it can be manipulated without fixing local coordinates.

Their power lies in turning geometric impossibility into an algebraic calculation. A nonzero class is not merely a name for a twist: it is a proof that certain global sections, frames, or decompositions cannot exist. And the relation to curvature shows how these topological obstructions can sometimes be measured by local differential geometry.

## Characteristic Classes by Example: Gluing Lines over a Sphere

Picture two smooth disks, one covering the northern hemisphere of a sphere and the other covering the southern hemisphere. Over each disk, place a copy of the complex plane at every point. Locally, everything looks like an ordinary product: a disk times a complex line.

To make one line bundle over the entire sphere, we must identify the fibers where the two disks overlap. We are free to rotate a complex fiber by a phase before gluing it to the fiber described in the other chart. If that phase winds as we go around the equator, the resulting bundle may be globally twisted even though it looks trivial from either hemisphere.

This construction makes the first Chern class tangible. Instead of beginning with an abstract characteristic class, we will build a family of bundles and ask what integer distinguishes them.

### Gluing by an angle-dependent rotation

On the equatorial circle, choose an angle that increases once around the circle. Define the gluing rule to rotate each complex line through an angle equal to k times the equatorial angle. Here k is an integer.

Why must k be an integer for this simple rule? Returning to the same equatorial point must give the same rotation. If the angle increases by one full turn, the fiber rotation changes by k full turns. That is the identity exactly when k is integral.

For k equal to zero, gluing uses the identity rotation. We recover the product bundle: every fiber can be identified with one fixed complex line globally. For k equal to one, the fiber undergoes one turn around the equator. For k equal to two, it undergoes two. Each choice has a winding number.

One can change the trivializations on the northern and southern disks. Doing so changes the formula for the transition function, but not its winding number. A phase defined throughout a disk cannot acquire nonzero boundary winding without becoming singular or discontinuous somewhere. Therefore the integer survives changes of local description.

### A characteristic class records the obstruction

For a complex line bundle over the sphere, the first Chern number equals the winding integer, after fixing compatible sphere orientation and gluing conventions. More generally, the first Chern class is an integral cohomology class in degree two. Its evaluation on an oriented closed surface gives an integer.

The word integral here is important. A characteristic class belongs to cohomology with integer coefficients. A differential form representing its image in real cohomology may reveal the same integer after integration, but real forms cannot see torsion classes. These are two related descriptions, not identical stores of information.

For complex line bundles over suitable spaces, including smooth manifolds, the first Chern class actually classifies the isomorphism class of the bundle. For higher-rank bundles, characteristic classes are powerful invariants but need not determine the bundle completely.

### Why a nowhere-vanishing section matters

A section chooses one vector from each fiber, continuously. If a complex line bundle has a nowhere-zero section, that section gives a global way to identify every fiber with the complex line: multiply the chosen vector by arbitrary complex numbers. The bundle must therefore be trivial.

Consequently, a line bundle with nonzero first Chern class cannot have a section that avoids zero everywhere. This obstruction is visible in the hemisphere construction. A proposed section would have to agree with itself after being rotated by a nonzero winding along the equator. Something must give: the section cannot remain globally continuous and nonvanishing.

For a real oriented rank-two bundle, rotation of each fiber makes it into a complex line bundle. In that case the Euler class agrees with the first Chern class under the induced orientation convention. The tangent bundle of the two-sphere is the standard example. Its Euler number is two, matching the sphere's Euler characteristic. That is one reason the hairy-ball theorem is true: a continuous tangent vector field on the sphere cannot be everywhere nonzero.

### Curvature finds the same integer

Now equip the bundle with a unitary connection. Locally it is represented by an imaginary-valued one-form. Its curvature is an imaginary-valued two-form. The local curvature expressions agree across charts in the abelian case, even though the connection one-forms themselves differ by derivatives of the transition phases.

With a fixed conventional normalization, multiplying the curvature by the imaginary unit and dividing by two pi produces a real two-form representing the first Chern class in de Rham cohomology. Integrating it over the oriented sphere gives the same integer detected by the winding of the transition function.

There is a chain of reasoning hidden inside that conclusion. First we construct the bundle from gluing maps. Next we choose a connection. Then we prove that the resulting curvature form changes by an exact form when the connection changes, so its cohomology class does not depend on that choice. Finally an integrality theorem relates that class to the transition-map winding. One should not assume that every arbitrary real two-form integrates to an integer.

### Twisting and holonomy are different questions

Suppose we have a flat connection on a circle. Transport a vector once around the circle and it can return rotated by a phase. That is nontrivial holonomy, even though every complex line bundle over a circle is topologically trivial because the circle has no second cohomology.

Thus a curved connection need not live on a twisted bundle, and a flat connection need not have trivial parallel transport. Bundle topology, connection curvature, and holonomy are three related but distinct pieces of information.

Later gauge-theoretic lectures use this distinction constantly. An instanton is not defined only by a topological bundle class. It is a special connection, satisfying differential equations, on a bundle. Characteristic classes constrain which connections are possible and can assign topological charges to their curvature.

The sphere construction gives a complete example to keep in mind: two locally trivial pieces, an equatorial phase winding, an integer Chern number, and a curvature integral representing that integer. When a more complicated invariant appears, look for the same ingredients: local data, compatibility on overlaps, and a global obstruction that cannot be transformed away.

## Vector Bundle K-Theory: Why Subtraction Needs New Objects

There are two ways to compare a pair of vector bundles. We can ask whether they are isomorphic as they stand, or we can ask whether they become isomorphic after adding an auxiliary bundle. The second question is less rigid. It is also the one that occurs naturally when we study elliptic differential operators, because the dimensions of a kernel and cokernel can change in a family even when their formal difference remains meaningful.

The simplest analogy comes from counting apples. Natural numbers let us add collections. If one collection contains three apples and another contains five, then a difference of the collections would have value negative two. The natural numbers do not contain that answer, so we pass to the integers. K-theory performs a related construction on vector bundles. We must take care: a bundle is much more than its rank. Two bundles of the same rank may twist differently over the same base.

### The addition we already possess

Fix a compact space such as a finite CW complex. A complex vector bundle assigns a complex vector space to each point, varying locally like a product. If we have bundles E and F, their direct sum has fiber E at x direct-summed with F at x. Its rank is the sum of their ranks. Direct sum is associative and commutative up to canonical isomorphism, and the rank-zero bundle is an identity.

But there is no ordinary inverse bundle. If E has positive rank, there is no bundle F with E direct-summed with F equal to the rank-zero bundle. The rank would have to be negative. This is exactly the obstruction that prevents the natural numbers from supporting subtraction.

To create a difference, write a formal pair: E minus F. Two such pairs represent the same virtual bundle if adding suitable auxiliary bundles makes their positive and negative parts isomorphic. In the group of virtual bundles, the difference of E and F plus the difference of F and E is zero. The resulting group is K zero of the space.

This does not say there is an actual vector bundle of negative rank sitting over each point. A virtual bundle is an algebraic class represented by a difference, not a mysterious physical bundle with negative-dimensional fibers.

### Stable equivalence and an embedding trick

Suppose E is a complex vector bundle over a compact Hausdorff base. We can find another bundle F such that E plus F is a trivial bundle of some finite rank. The idea is to use finitely many local generating sections, combine them with a partition of unity, and embed E into a sufficiently large trivial bundle. A Hermitian metric lets us take an orthogonal complement.

This is an important surprise. A bundle need not be trivial, but it can be a direct summand of a trivial bundle. Consequently, stabilization by trivial summands is not an arbitrary game: it has the geometry of embeddings and complements behind it.

If two bundles become isomorphic after adding trivial summands of possibly different ranks, they define the same appropriate stable difference. Conversely, equality in K zero can be expressed in terms of stable isomorphisms. One must still track rank, because the trivial line and the rank-zero bundle represent different classes even though neither has any twisting.

### Calculate K zero of a point

Over a point, every complex bundle is merely a vector space. Its isomorphism class is determined by a nonnegative integer, its dimension. Direct sum adds dimensions. Completing that monoid to a group gives the integers. Thus K zero of a point is the ordinary integer group.

There is a rank map from K zero of a connected space to the integers. It sends E minus F to rank E minus rank F. The reduced K group is the kernel of the restriction to a chosen basepoint. Reduced classes remember twisting after the rank information has been discarded.

The distinction matters. A class of rank zero can still be nonzero in reduced K-theory. We will encounter one on the sphere, where a complex line bundle differs from the trivial line without changing the rank.

### Multiplication comes from tensor products

We also know how to multiply bundles: take a tensor product. A fiber of E tensor F has dimension rank E times rank F. Tensor product distributes over direct sum, so it extends to products of virtual classes. K zero is therefore not only an additive group but a ring. The trivial complex line is the multiplicative identity.

For the Möbius real line over a circle, tensoring the line with itself gives a trivial real line. This hints at torsion-like multiplicative behavior in real K-theory. We focus on complex K-theory first; its periodicity is simpler. The underlying theme remains the same: addition records direct sum, while multiplication records tensor product.

### Why an index wants this language

An elliptic operator between spaces of sections has a finite-dimensional kernel and cokernel, despite acting between infinite-dimensional function spaces. For one operator, the analytic index is dimension kernel minus dimension cokernel. In a family of operators, neither kernel nor cokernel need form a vector bundle because their dimensions can jump. After finite-dimensional stabilization, however, their formal difference defines a class in K zero of the parameter space.

When the parameter space is a point, we recover the familiar integer index. When it has loops or surfaces, the K class may contain information not captured by any list of integers. This is why virtual bundles are not just a convenient abstraction: they preserve geometry that dimensions alone forget.

The key moves are now visible. Begin with actual bundles and direct sums. Allow formal differences, while respecting stable equivalence. Remember rank separately from twisting. Add tensor products to obtain a ring. These steps turn vector-bundle geometry into an algebra suited to families and index problems.

## K-Theory of the Sphere: The Hopf Bundle as a Generator

A line bundle over a sphere is locally just a copy of the complex numbers. Over a northern hemisphere, we can choose a frame. Over a southern hemisphere, we can choose another. The entire distinction between a trivial line and a twisted one is hidden in how these frames meet around the equator.

This is the right place to calculate rather than simply announce a K group. We will build one nontrivial line bundle, subtract one trivial line, and see why this rank-zero virtual class generates reduced complex K-theory of the two-sphere.

### Clutch two disks together

Identify the two-sphere with the complex projective line. Cover it by two disks whose overlap retracts to a circle. To glue complex line bundles, specify a continuous map from the equatorial circle to nonzero complex numbers. After normalizing lengths, this map lands in the unit circle. Its winding number is an integer.

A constant clutching map has winding zero and gives the trivial line. A map that winds once gives a nontrivial line. Let L denote the degree-positive line bundle, commonly written O of one on the complex projective line. Its first Chern class evaluates to plus one on the oriented sphere. Its dual is the tautological line O of minus one.

Tensoring L with itself produces a clutching map that winds twice. Tensor powers L to the k give every degree k. The classification by winding number agrees with the first Chern class: on a two-sphere, the first Chern number completely classifies complex line bundles.

### Subtract rank and retain the twist

Both L and the trivial complex line have rank one. Their formal difference, L minus one, has virtual rank zero. Yet it is not zero in K-theory, because stabilization cannot erase the nonzero first Chern class. Call this reduced class beta.

A stable complex bundle over the sphere is governed by a clutching map into a sufficiently large unitary group. Its stable homotopy class is still measured by an integer winding number, which can be seen through determinant. Therefore reduced complex K zero of the two-sphere is the integers, generated by beta, with a choice of orientation fixing the sign.

The full group K zero of the sphere contains one integer for rank and another for twisting. A typical class can be written r plus n times beta. The rank is r. The first Chern number of its rank-zero part is n. This is a concrete example of why K-theory remembers more than dimension.

### Multiply the generator by itself

K zero is a ring, so ask what beta squared means. Expand the product: L minus one, multiplied by L minus one, equals L tensor L minus twice L plus one. This virtual class has rank zero. Its first Chern class is twice the first Chern class of L minus twice the same class, hence zero.

On the two-sphere, reduced complex K zero is completely detected by the first Chern number. Therefore beta squared equals zero. The K ring is a pair of integers with a generator beta whose square vanishes. This is not a statement that L tensor L is trivial. The actual bundle L squared has degree two. Only the particular alternating *virtual difference* is zero.

The nilpotent relation resembles the cohomology ring of the sphere, where a degree-two generator squares to zero because the space has no cohomology in degree four. But K-theory and ordinary cohomology are different theories. Their agreement in this small example will be explained by the Chern character, which passes from K-theory to rational cohomology.

### Why the next sphere is different

A complex line bundle over a circle is trivial because its first Chern class would need to live in degree two, and that cohomology group vanishes. In fact, every complex vector bundle over the circle is trivial. Its reduced complex K zero group is zero.

That sounds as if odd spheres have no K-theoretic topology. This is too quick. K-theory has two degrees. Odd K-theory is nontrivial on the circle: K minus one of the circle is the integers, with a generator related to a unitary map winding once. Complex Bott periodicity repeats this two-degree pattern. Even-dimensional spheres have reduced K zero equal to the integers, while odd-dimensional spheres have zero reduced K zero. In the other degree the roles reverse.

Bott periodicity is a theorem, not a consequence of computing the two-sphere alone. The two-sphere provides its basic geometric building block, which later appears as an external product in the periodicity map.

### Return to the index

Consider a family of elliptic operators parameterized by the sphere. Suppose its index bundle has rank zero but represents beta. Every operator in the family has numerical index zero, yet the family index is nonzero. It has one unit of twisting around the parameter sphere.

This is exactly the sort of information that a single integer could not have reported. To understand families index theory, the central example is not an abstract K group. It is the difference between a nontrivial line and a trivial line, where subtraction removes the rank but retains the obstruction to global trivialization.

## The Chern Character: Why Exponentials Connect Bundles to Cohomology

There are two natural ways to combine complex vector bundles. We can take a direct sum, which adds ranks, or a tensor product, which multiplies ranks. Characteristic classes are especially effective at recognizing the global twisting, but their formulas for these two operations do not always look simple. The Chern character is designed to make both operations behave naturally.

To see its construction, we begin with line bundles. For a complex line bundle L, its first Chern class is an integral class of degree two. Tensoring lines adds that class. If we want tensor product to become multiplication, we should look for a function that turns sums into products. The exponential function does precisely that.

### The exponential of a two-dimensional class

Write x for the first Chern class of L. Define the Chern character of L as the formal exponential of x: one plus x plus one-half x squared plus one-sixth x cubed, and so on. On any finite-dimensional manifold, only finitely many terms can survive because powers in degrees above the dimension vanish.

Suppose M is another line with first Chern class y. The tensor product has first Chern class x plus y. Therefore its Chern character is the exponential of x plus y, equal to the exponential of x times the exponential of y. Tensor products of lines have become ordinary multiplication of cohomology classes.

What about direct sums? We declare the Chern character of a direct sum to be the sum of the characters. For a general bundle, the splitting principle allows us to work formally as if the bundle decomposed into line bundles after pulling back to a suitable space. If x one through x r are its formal Chern roots, the character is the sum of their exponentials.

The degree-zero component is the rank. The degree-two component is the first Chern class. The degree-four component is one-half the square of the first Chern class minus twice the second Chern class. Already at this stage, rational coefficients appear. The Chern character does not usually land in integral cohomology.

### A calculation on the sphere

Take the complex projective line, which is a two-sphere, with positive generator h in second cohomology. The degree-positive line L has first Chern class h. Since the sphere has no degree-four cohomology, h squared vanishes. Its Chern character is just one plus h.

Now subtract the trivial line in K-theory. The reduced class beta equals L minus one. The Chern character of beta is h. Thus the rank-zero K-theory generator maps to the degree-two cohomology generator. This explains why our sphere computation looked so much like ordinary cohomology.

On more complicated spaces, Chern character is still an isomorphism after tensoring K-theory with the rational numbers, with the appropriate even or odd grading. This is a deep structural fact. It does not mean integral K-theory and integral cohomology are identical: torsion information can be lost when rationalizing.

### A calculation on the projective plane

The complex projective plane has a degree-two cohomology class h whose square is nonzero and integrates to one. For the line L with first Chern class h, the character is one plus h plus one-half h squared. The fraction is not a defect in the calculation; it is built into the exponential.

Now form the reduced K class L minus one. Its character is h plus one-half h squared. The square of that reduced class has character h squared, because all higher terms are too high in degree. There is no contradiction with the sphere relation beta squared equals zero: on the complex projective plane, a degree-four cohomology class actually exists.

The exponential creates a bridge between the algebra of bundles and the cup-product structure of cohomology, but the bridge has rational coefficients. This will matter when calculating indices, which must come out as integers even though intermediate characteristic-class expressions contain fractions.

### Curvature and normalizations

If a Hermitian vector bundle carries a unitary connection with curvature F, Chern–Weil theory represents the Chern character in differential forms using the matrix exponential of a normalized curvature matrix. The precise factor of the imaginary unit and two pi depends on whether one writes the curvature as a skew-Hermitian matrix or a real-valued two-form for a line bundle.

For a line bundle of first Chern number one over a sphere, the normalized curvature integrates to one. Its exponential contains a constant term and a degree-two term. On the sphere, only the degree-two term contributes to the integral. This is the same Chern character we calculated topologically.

Yet a curvature form cannot detect torsion Chern classes after passing to real cohomology. Differential forms and rational characteristic classes give a powerful part of the story, not every integral detail.

### Why the index formula needs another factor

A tempting guess is that the index of a Dolbeault operator twisted by L equals the integral of the Chern character of L. But on a complex curve, integrating just the first Chern class would give the degree k for a line of degree k. The actual holomorphic Euler characteristic of a line on the projective line is k plus one.

The missing one comes from the geometry of the tangent bundle and is encoded by the Todd class. The general Riemann–Roch formula contains Chern character times Todd class. We can already see why a correction is necessary: a bundle does not live alone; the elliptic operator also depends on the manifold and its tangent directions.

The Chern character is therefore not simply a new notation for Chern classes. It is the map that carries stable vector-bundle arithmetic into cohomological arithmetic in the form suited to index theory, while exposing exactly where rational coefficients and tangent-bundle correction terms enter.

## Bott Periodicity and Index Pushforwards: Turning Symbols into Integers

We have built virtual bundles and computed one generator of reduced K-theory on the two-sphere. How does this help us understand a differential operator? The missing link has two parts. Bott periodicity tells us how K-theory behaves when two new spatial directions are introduced. A pushforward tells us how to turn a class defined over a geometric space into a class over a point or parameter space.

Our aim here is to understand that meaning through a completely calculable example; this does not amount to a proof of the full Atiyah–Singer theorem.

### The symbol knows which directions matter

Take a differential operator D acting on sections of a bundle over a compact manifold. Its principal symbol is a bundle map depending on a point x and a cotangent vector xi. For an elliptic operator, that map is invertible whenever xi is nonzero. This is a local, high-frequency condition. It says the only possible failure of invertibility is concentrated at the zero section of the cotangent bundle.

Because the symbol is invertible away from that section, it defines a class in K-theory with compact support on the cotangent bundle. It is not, in general, simply a class in K zero of the original manifold. The variable xi, representing the direction and frequency of oscillation, is essential to the construction.

The analytic index counts kernel minus cokernel. The topological index starts with this symbol class, transports it through K-theoretic constructions, and ends in the integers. The index theorem says the two integers agree.

### Why the plane acts like the two-sphere

The real plane becomes a sphere after adding one point at infinity. Compactly supported K-theory on the plane is therefore reduced K-theory of the two-sphere. Our class beta, built from the Hopf line minus a trivial line, generates this group.

There is a canonical Bott class on the plane; it is the K-theoretic orientation of a complex one-dimensional vector space. Multiplying a class by this Bott element and using the two additional real directions yields an isomorphism in compactly supported K-theory. This is Bott periodicity in a geometric form.

Its deeper implication is that complex K-theory repeats every two degrees. The periodicity is not obvious from the definition by bundles. Establishing it is one of the major theorems behind topological index theory.

### Push a class toward a point

Imagine integrating a differential form over a compact oriented fiber. The result is a form of lower degree on the base. A K-theoretic pushforward plays an analogous role. But ordinary orientation is not enough. Complex K-theory needs a K-orientation, supplied, for example, by a spin-C structure or by an almost-complex structure in appropriate geometric settings.

For an elliptic symbol over a compact manifold, embedding into a Euclidean space, using Thom classes and excision, and then Bott periodicity gives a topological index in the integers. This paragraph compresses a substantial construction. Its important warning is that different orientations yield different pushforwards; a pushforward is not defined automatically for any continuous map.

With families, the target is not necessarily a point. For a smooth proper family of spin-C manifolds over a base B, one pushes fiberwise and obtains a class in K zero of B. This is the topological counterpart of the index bundle of a family of Dirac operators.

### A worked complex curve

Take the complex projective line. Twist the Dolbeault operator by the holomorphic line bundle O of k, where k is an integer. Its analytic index equals the dimension of holomorphic sections minus the dimension of first sheaf cohomology.

For nonnegative k, global holomorphic sections correspond to homogeneous polynomials of degree k in two coordinates. There are k plus one independent monomials, and the first cohomology vanishes. So the index is k plus one. For negative k, the same formula still holds, although the kernel may be zero and the cokernel nonzero.

Now compute the topological expression. Let h be the positive degree-two generator of cohomology, normalized to integrate to one. The Chern character of O of k is one plus k h. The holomorphic tangent bundle of the projective line has first Chern class two h. In complex dimension one its Todd class is one plus h. Multiplying gives one plus k plus one times h, after discarding the degree-four term. Integrating the degree-two term gives k plus one.

This is a small Riemann–Roch theorem we can actually check. The fractional terms of Todd theory did not spoil integrality. They corrected the index to the right integer.

### What this example does not prove

The calculation verifies an index formula for one family of examples. It does not prove that all elliptic symbols have matching analytic and topological indices. Nor does it establish the families theorem, which may produce nonzero classes in higher-degree cohomology on the parameter base.

But it provides a map of the ideas. The principal symbol supplies a compactly supported K class. Bott periodicity makes Euclidean stabilization possible. A K-oriented pushforward turns the class into an index. The Chern character translates that pushforward into an integral with characteristic-class corrections.

The heavy index theorem is no longer a string of unfamiliar names. Each step has a distinct mathematical job, and we have verified the output in a case where both analysis and cohomology can be counted by hand.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Characteristic Classes: Detecting the Twist in a Bundle

**Track:** Topology and Geometry. **Background:** vector bundles, cohomology, orientations, tangent bundles, Gauss–Bonnet. **Central question:** what invariants prove that a locally trivial bundle cannot be globally trivial?

#### Mathematical companion (not spoken)

For a real rank-r vector bundle \(E\to X\), Stiefel–Whitney classes are \(w_i(E)\in H^i(X;\mathbb Z/2)\). The **first class** detects orientability: \(w_1(E)=0\) iff E is orientable. For real line bundles over a paracompact base, \(w_1\) provides classification by \(H^1(X;\mathbb Z/2)\). The total class is \(w(E)=1+w_1(E)+\cdots+w_r(E)\), and \(w(E\oplus F)=w(E)\smile w(F)\).

For an oriented real rank-r bundle E, its Euler class is \(e(E)\in H^r(X;\mathbb Z)\). If E has a nowhere-zero section then \(e(E)=0\); the converse needs extra conditions. For an oriented closed surface M,
\[\langle e(TM),[M]\rangle=\chi(M),\qquad e(TM)_{\mathrm{dR}}=[K\,dA/(2\pi)].\]
For \(S^2\), the Euler number is 2, ruling out a nowhere-zero tangent field.

For complex rank-r E, \(c_i(E)\in H^{2i}(X;\mathbb Z)\). For complex line bundles L,M, \(c_1(L\otimes M)=c_1(L)+c_1(M)\). Over paracompact X, complex line bundles are classified by \(H^2(X;\mathbb Z)\). Hence \(\operatorname{Pic}_{\mathrm{top}}(S^1)=0\), while \(\operatorname{Pic}_{\mathrm{top}}(\mathbb {CP}^1)\cong\mathbb Z\). Under a unitary connection with curvature F, \(F/(2\pi i)\) represents the real image of \(c_1\) with the corresponding convention.

##### Exercises with answers

1. What is \(w_1\) of the Möbius line over \(S^1\)? **Answer:** the nonzero generator of \(H^1(S^1;\mathbb Z/2)\).
2. Why can the tangent bundle of the sphere not have a global frame? **Answer:** even one nowhere-zero tangent section is impossible because the Euler class evaluates to 2.
3. Does a flat connection prove that a real line bundle is trivial? **Answer:** no; the Möbius line can have a flat connection with nontrivial holonomy and \(w_1\ne0\).
4. What happens to \(c_1\) under tensor product of line bundles? **Answer:** it adds.

##### Reading and source notes

- Allen Hatcher, [*Vector Bundles and K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), characteristic classes and bundle obstructions.
- Allen Hatcher, [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html), cohomology and characteristic-class prerequisites.
- [UCLA, Differential Geometry lecture notes](https://math.ucla.edu/~sucharit/120A-notes.html), curvature and Gauss–Bonnet context.

### Characteristic Classes by Example: Gluing Lines over a Sphere

**Track:** Topology and Geometry. **Background:** vector bundles, transition functions, winding numbers, de Rham cohomology, basic curvature. **Central question:** how can local triviality hide a global twist, and how do we measure it?

#### Mathematical companion (not spoken)

Write \(S^2=D_N\cup D_S\) with overlapping equatorial annulus retracting to \(S^1\). Clutch a complex line bundle with \(g_k:S^1\to U(1)\), \(g_k(e^{i\varphi})=e^{ik\varphi}\). The winding number is \(k\). With corresponding orientation and clutching conventions, \(\langle c_1(L_k),[S^2]\rangle=k\). Reversing the sphere orientation or the gluing convention reverses this signed evaluation.

For a unitary line connection written \(\nabla=d+A\), \(A\in i\Omega^1\), \(F=dA\). The adopted normalization is \(c_1(L)_{\mathbf R}=[iF/(2\pi)]\) (the real image of the integral class). Under a local gauge change \(g\), \(A'=A+g^{-1}dg\), while \(F'=F\). For a globally defined change of connection \(A\mapsto A+i\eta\) on a fixed line bundle, \(iF/(2\pi)\) changes by the exact form \(-d\eta/(2\pi)\).

An oriented rank-two real vector bundle is a complex line bundle after choosing a compatible complex structure, with \(e(E)=c_1(E_{\mathbf C})\). For \(E=TS^2\), \(\int_{S^2}e(TS^2)=\chi(S^2)=2\). Over \(S^1\), all complex line bundles have \(c_1=0\), but flat \(U(1)\) connections can have nontrivial holonomy.

##### Exercises with answers

1. **Winding.** What Chern number results from a phase rotating three times around the equator? **Answer:** \(+3\) in the stated orientation and gluing convention.
2. **Section.** Could a complex line bundle with Chern number one have a global nowhere-zero section? **Answer:** No. Such a section would trivialize it.
3. **Tangent sphere.** What is the Euler number of \(TS^2\)? **Answer:** Two, so a globally nonzero tangent field does not exist.
4. **Flat transport.** Does vanishing curvature on a circle force trivial holonomy? **Answer:** No. Global transport can retain a phase.

##### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html).
- University of Toronto, [Equivariant Cohomology lecture notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf).
- Overviews: [Chern class](https://en.wikipedia.org/wiki/Chern_class), [Clutching construction](https://en.wikipedia.org/wiki/Clutching_construction).

### Vector Bundle K-Theory: Why Subtraction Needs New Objects

**Track:** Topology and Geometry. **Background:** vector bundles, direct sums, homotopy. **Central question:** what information survives when we permit adding trivial bundles and formally subtracting bundles?

#### Mathematical companion (not spoken)

For compact Hausdorff X, let `Vect_C(X)` be the commutative monoid of isomorphism classes of finite-rank complex bundles under direct sum. Its Grothendieck group `K^0(X)` is generated by `[E]` with relations `[E⊕F]=[E]+[F]`. An equality `[E]-[F]=[E']-[F']` holds precisely when some auxiliary bundle `G` makes `E⊕F'⊕G ≅ E'⊕F⊕G`. Because bundles are summands of trivial bundles on compact Hausdorff X, this can be expressed using sufficiently large trivial stabilizations.

The rank homomorphism `K^0(X)→H^0(X;Z)` is locally constant. On connected based X, `\widetilde K^0(X)=ker(K^0(X)→K^0(pt))`, and `K^0(X)≈Z⊕\widetilde K^0(X)` by restriction and pullback. Tensor products supply the ring product.

##### Exercises with answers

1. For E of rank 4 and F of rank 6, what is the rank of `[E]-[F]`? **Answer:** minus two, although this is not an actual negative-dimensional bundle.
2. Why is `K^0(pt)=Z`? **Answer:** bundles over a point are classified by nonnegative integer dimension; group completion adds formal additive inverses.
3. If E is nontrivial but `E⊕F` is trivial, must E be trivial? **Answer:** no; being a summand of a trivial bundle is weaker than being trivial.
4. What does multiplication of `[E]` and `[F]` represent? **Answer:** the tensor product class `[E⊗F]`.

##### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), Chapters 1–2.
- [Topological K-theory](https://en.wikipedia.org/wiki/Topological_K-theory); [Grothendieck group](https://en.wikipedia.org/wiki/Grothendieck_group).

### K-Theory of the Sphere: The Hopf Bundle as a Generator

**Track:** Topology and Geometry. **Background:** clutching functions, Chern classes, virtual bundles. **Central question:** how can a virtual rank-zero class detect a sphere's global twisting?

#### Mathematical companion (not spoken)

Let `X=CP^1≈S^2`, `h=c_1(O(1))`, and `∫_X h=1`. Define `β=[O(1)]-[1]`. The stable clutching classification gives `\widetilde K^0(S^2)≈π_1(U)=Z`, generated by β. Thus

\[
K^0(S^2)\cong\mathbb Z[\beta]/(\beta^2),\qquad
\beta^2=[O(2)]-2[O(1)]+[1]=0.
\]

The last relation follows from the classification of stable bundles over S² by rank and first Chern class, not from an isomorphism `O(2)≅O(1)⊕O(1)` (their ranks differ). With a chosen basepoint, `K^0(S^1)=Z`, `\widetilde K^0(S^1)=0`, while `K^{-1}(S^1)=Z`. Bott periodicity gives `\widetilde K^0(S^{2n})=Z`, `\widetilde K^0(S^{2n+1})=0` for `n≥1`.

##### Exercises with answers

1. What is the rank of beta? **Answer:** zero.
2. What is the degree of `O(3)`? **Answer:** three; its clutching map winds three times.
3. Why does `β²=0` not imply `O(2)` is trivial? **Answer:** it is an equality of virtual bundle classes; O(2) has Chern number two.
4. Can a rank-zero index family over S² be nontrivial? **Answer:** yes, its index bundle can be a nonzero multiple of beta.

##### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), clutching and Bott periodicity.
- [Hopf bundle](https://en.wikipedia.org/wiki/Hopf_bundle); [Bott periodicity theorem](https://en.wikipedia.org/wiki/Bott_periodicity_theorem).

### The Chern Character: Why Exponentials Connect Bundles to Cohomology

**Track:** Topology and Geometry. **Background:** Chern classes, tensor products, rational cohomology. **Central question:** how do multiplicative bundle data become additive cohomology classes?

#### Mathematical companion (not spoken)

For a complex bundle E with formal Chern roots `x_i`,

\[
\operatorname{ch}(E)=\sum_i e^{x_i}
=\operatorname{rank}(E)+c_1(E)
+\tfrac12(c_1(E)^2-2c_2(E))+\cdots.
\]

Extend by `ch([E]-[F])=ch(E)-ch(F)`. It satisfies `ch(E⊕F)=ch(E)+ch(F)` and `ch(E⊗F)=ch(E)ch(F)`. On `CP²` with `h=c_1(O(1))`, `∫h²=1`, the truncation is `ch(O(1))=1+h+h²/2`. The Chern character induces a natural isomorphism `K^0(X)⊗Q ≅ H^{even}(X;Q)` for finite CW complexes (and `K^{-1}(X)⊗Q ≅ H^{odd}(X;Q)`). Rationalization may annihilate torsion.

##### Exercises with answers

1. Compute `ch(O(2))` on `CP¹`. **Answer:** `1+2h`.
2. Compute `ch([O(1)]-[1])` on `CP²`. **Answer:** `h+h²/2`.
3. Can a torsion K-theory class have nonzero rational Chern character? **Answer:** no.
4. Does the integral of `ch(O(k))` alone always equal the holomorphic Euler characteristic on `CP¹`? **Answer:** no; the Todd class contributes the extra one.

##### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), Sections on Chern classes and K-theory.
- [Chern character](https://en.wikipedia.org/wiki/Chern_character); [Splitting principle](https://en.wikipedia.org/wiki/Splitting_principle).

### Bott Periodicity and Index Pushforwards: Turning Symbols into Integers

**Track:** Topology and Geometry. **Background:** reduced K-theory of spheres, elliptic symbols, Chern character. **Central question:** why is the topological index of an elliptic operator a K-theoretic pushforward rather than a count of zeros?

#### Mathematical companion (not spoken)

For compact M, an elliptic symbol determines `[\sigma(D)]∈K_c^0(T^*M)`. The analytic index is `dim ker D - dim coker D`. The topological index uses an embedding, the K-theory Thom isomorphism and Bott periodicity to map that class to `K_c^0(R^{2N})≈Z`. For a spin-C family `π:X→B`, the K pushforward is `π_!:K^0(X)→K^0(B)` (with the required K-orientation and degree conventions). Its Chern character satisfies the relevant families Riemann–Roch relation.

For `X=CP¹`, write `h=c_1(O(1))`, `∫h=1`. Then

\[
\operatorname{ch}(O(k))=1+kh,\quad
\operatorname{Td}(TX)=1+\tfrac12 c_1(TX)=1+h,\quad
\chi(O(k))=\int_X (1+kh)(1+h)=k+1.
\]

The formula for `chi` holds for every integer k. For `k=-2`, `h^0=0`, `h^1=1`, and the index equals minus one. The explicit sheaf-cohomology count is developed later.

##### Exercises with answers

1. Where does an elliptic principal symbol define a K class? **Answer:** in compactly supported K-theory of the cotangent bundle, because it is invertible off the zero section.
2. Why is `K_c^0(R²)` isomorphic to `\widetilde K^0(S²)`? **Answer:** the one-point compactification of R² is S².
3. Find `chi(O(2))` on CP¹. **Answer:** three.
4. Find `chi(O(-2))` and interpret its sign. **Answer:** minus one; the first cohomology has dimension one while holomorphic sections vanish.

##### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), Bott periodicity and Thom constructions.
- [Atiyah–Singer index theorem](https://en.wikipedia.org/wiki/Atiyah%E2%80%93Singer_index_theorem); [Hirzebruch–Riemann–Roch theorem](https://en.wikipedia.org/wiki/Hirzebruch%E2%80%93Riemann%E2%80%93Roch_theorem).
