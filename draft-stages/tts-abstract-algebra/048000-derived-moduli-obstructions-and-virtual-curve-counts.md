# Derived moduli, obstructions, and virtual curve counts

<!-- BEGIN SPOKEN LECTURE -->

# Derived moduli, obstructions, and virtual curve counts

## Complexes, Riemann-Roch, and moduli obstructions

### Deformation-Obstruction Complexes in Moduli Problems

A moduli problem asks us to organize mathematical objects into a family. Each point is meant to represent something: a curve, a vector bundle, a surface, or perhaps a representation. We can then ask whether nearby points correspond to nearby objects, how many independent ways an object can vary, and whether a first-order variation extends to an actual family.

For an ordinary smooth curve, tangent vectors at a point describe possible directions of motion. In a moduli problem, a tangent direction is often a deformation of the object over the dual numbers, a ring with one infinitesimal parameter whose square is zero. This lets us study first-order changes without claiming they extend indefinitely.

A second question appears immediately: what if the object has automorphisms? Two descriptions of a deformation can be equivalent through a symmetry. A third question is whether a first-order deformation can be lifted from a small infinitesimal thickening to a larger one. An obstruction may prevent that lift.

These three phenomena lead naturally to a complex rather than to a single tangent vector space.

#### Ext groups as a deformation dictionary

Fix a smooth projective variety X and a coherent sheaf E on it, in a setting where the standard deformation theory applies. The vector space Ext one of E with itself governs first-order deformations of E. Ext two receives obstruction classes for lifting deformations. Ext zero records infinitesimal automorphisms.

The numbers zero, one, and two are not ranks of three arbitrary matrices. They arise from the cohomological degrees of a derived endomorphism object. A deformation problem is controlled by how a mathematical object maps to itself, including higher extension data.

It is important not to overstate the dictionary. An obstruction group may be nonzero even when a particular deformation problem is unobstructed. The obstruction is a class in that group, and the class may vanish. Likewise, a tangent space of positive dimension does not by itself prove that a smooth family of that dimension exists.

Consider a line bundle L on a smooth projective curve C of genus g. Its derived endomorphism groups simplify because its endomorphism sheaf is the structure sheaf. Ext one of L with itself is therefore the first cohomology of the structure sheaf. That vector space has dimension g. Ext two vanishes on a smooth curve, so the standard obstruction group for line-bundle deformations vanishes. This explains the smooth g-dimensional local behavior of the Picard variety.

For a genus-one curve, that tangent space is one-dimensional. We can change the line bundle infinitesimally in one independent direction. The calculation is not just counting coefficients in an equation; it is measuring cohomology of the underlying curve.

#### Deforming the space instead of a sheaf

Now let the geometric space X itself vary. For a smooth proper scheme, its infinitesimal automorphisms are measured by the global sections of the tangent sheaf, while first-order deformations are measured by its first cohomology and potential obstructions by second cohomology. This is the familiar smooth-case pattern.

When X has singularities, the tangent sheaf alone misses information. The cotangent complex replaces the sheaf of differentials as the object that correctly remembers equations and relations among equations. Derived Hom from that cotangent complex to the structure sheaf organizes the tangent, deformation, and obstruction groups. The precise degree conventions depend on whether we are deforming the space, a map, or a sheaf.

Here is a concrete way to see why relations matter. Suppose a space is cut out by polynomial equations. Perturb the coordinates by a first-order epsilon. The linearized equations say which directions are initially allowed. But if the equations satisfy dependencies, the linearized conditions can also satisfy dependencies. On attempting a second-order lift, a quadratic error can survive that cannot be corrected by changing the next coefficient. That residual error is the obstruction.

#### Why moduli spaces can be singular

A naive picture of moduli would be a smooth manifold with as many coordinates as deformation parameters. In reality, automorphisms may lead to stack-like quotients, and obstruction equations may cut out singular loci. A space of first-order possibilities may be much larger than the space of genuine nearby solutions.

Derived deformation theory supplies a systematic record of these features. It does not magically turn every moduli problem smooth. Instead, it keeps track of the reason smoothness may fail, while preserving the data needed for virtual dimensions and intersection invariants.

Think of a coarse moduli point, for example, as a label for an isomorphism class. That label can conceal a symmetry group. A moduli stack retains the symmetry information. A derived enhancement can also retain higher deformation-obstruction information. Each layer adds structure that a set of labels cannot express.

The broad principle is that moving objects create more than coordinates. They create automorphisms, first-order possibilities, and possible barriers to realizing those possibilities. Complexes and Ext groups provide the language in which all three can be calculated and compared.

### Derived Deformation Theory: Obstructions Beyond the Tangent Space

Imagine drawing a tangent arrow on a surface at a point. On an ordinary smooth surface, a short curve can follow that arrow. But a space defined by equations can have tangent arrows that fail to extend to actual curves. At a crossing, a tangent space can be larger than either branch. In moduli problems, the mismatch is even richer: one might be able to change an object infinitesimally, but encounter a genuine obstruction when trying to continue the change.

The deformation-obstruction description above used Ext groups. We can now go inside that mechanism. The central distinction is between the *space that could hold an obstruction* and the *obstruction itself*. A nonzero second Ext group does not tell us that every attempted deformation fails. We must calculate a class and ask whether it vanishes.

Start with an elementary example. Consider the equation x squared equals zero. At the solution x equals zero, the linearization has zero derivative, so it places no restriction on an infinitesimal change. Over the dual numbers, with epsilon squared equal to zero, x equals epsilon solves the equation. But over a ring in which epsilon cubed, rather than epsilon squared, is zero, the same choice produces epsilon squared. That term is nonzero. We cannot fix it by adding a multiple of epsilon squared to x, because squaring x still produces epsilon squared at the first nonvanishing order.

This is a complete second-order obstruction in a one-equation example. It shows why a tangent direction need not arise from a genuine family. The obstruction is not a numerical error; it is a failure of an equation over a thicker infinitesimal ring.

#### Organizing corrections by order

A deformation can be built order by order. At order one, solve the linearized equations. At order two, substitute the proposed solution back into the original nonlinear equations and collect the new error. If the error can be canceled by an order-two correction, move on. Otherwise the process stops. The correction problem repeats at higher orders.

For many deformation problems in characteristic zero, a differential graded Lie algebra, often shortened to a D G Lie algebra, organizes this calculation. It consists of graded vector spaces, a differential, and a bracket that remembers how two infinitesimal changes interact. A degree-one element is a candidate change. The Maurer–Cartan equation says that its differential plus half its self-bracket must vanish.

Why a bracket? A linear equation would only see independent first-order changes. The bracket records quadratic interaction. Two changes may each be allowed individually while their interaction creates a second-order error. That interaction is what our simple squared-variable example makes visible.

Consider an especially small model: one degree-one generator called e and one degree-two generator called f. Let the differential be zero, and let the bracket of e with itself be twice f. Take a candidate deformation equal to t times e. The Maurer–Cartan expression is t squared times f. It vanishes if t squared is zero, but not if t cubed is zero and t squared survives. The obstruction is the class represented by f. We have written the failure as a concrete calculation, not just named a cohomology group.

#### Why triangles appear

In derived categories, a short exact sequence is expressed by a distinguished triangle. When a deformation problem is controlled by a complex, the tangent and obstruction data are not isolated spaces: they are successive cohomology groups of that complex. A map of deformation problems can therefore give a triangle of controlling complexes and a long exact sequence of tangent and obstruction groups.

Think of forgetting structure. We might deform a vector bundle together with a section, then forget the section and retain only the bundle. The relative deformation complex measures the extra conditions imposed by preserving the section. The long exact sequence compares infinitesimal automorphisms, tangent directions, and obstructions before and after forgetting.

The triangle does not mean that a derived category somehow solves every extension problem automatically. It means that the *relationship* between different extension problems is recorded without throwing away higher information. Under the relevant finiteness and perfectness assumptions, that information can be presented locally by a two-term complex and used to define virtual dimensions and virtual fundamental classes. Those are not ordinary counts of smooth parameters; they take the obstruction theory seriously.

#### From calculation to geometry

The example x squared equals zero deserves a final interpretation. As a set of classical points over a field, it contains only zero. As a scheme, it still remembers the nilpotent direction. As a deformation problem, that direction is real at first order and obstructed at second order. Reducing the scheme to its underlying point would erase the entire calculation.

The lesson is not that every geometric space has hidden pathologies. It is that our mathematical description should keep exactly the information the question requires. Ordinary tangent spaces answer a linear question. Deformation complexes organize the nonlinear sequence of lifting questions. Derived objects preserve enough of the latter to compare moduli problems through maps, triangles, and cohomology.

When a proof says a moduli space is unobstructed, ask what makes the actual obstruction classes vanish. When it claims a virtual dimension, ask which complex provides it. And when a first-order solution looks convincing, check whether it survives one more power of the infinitesimal parameter.

## Quotient Stacks: Spaces That Remember Symmetry

A group action lets us declare certain points equivalent. Rotating a shape produces a different description but perhaps not a different geometric object. The ordinary quotient attempts to identify all the points in each orbit. For many purposes this is sensible. Yet an orbit is more than a label: some points may have symmetries that others lack.

Imagine the plane rotating about the origin. A nonzero point moves around a circle, while the origin remains fixed under every rotation. If we reduce each orbit to a single point, we may forget that the origin has a much larger stabilizer group. In a moduli problem, forgetting stabilizers means forgetting automorphisms of the objects being classified.

A quotient stack is designed to retain this information. It does not merely record which points become equivalent. It records the ways they are equivalent, and the symmetries of those equivalences.

### A scaling example

Let the multiplicative group act on the affine line by scaling. Every nonzero geometric point can be moved to every other nonzero point; the origin cannot be moved at all. A coarse orbit description sees two kinds of orbits. But the ordinary affine invariant ring consists only of constants, so the categorical affine quotient is just one point. This is a warning: depending on the quotient construction, an orbit-space intuition can fail even to distinguish the origin from nonzero points.

Now examine automorphisms. At a nonzero point, the only scalar fixing it is one. Its stabilizer is trivial. At the origin, every scalar fixes it, so the stabilizer is the whole multiplicative group. A quotient stack distinguishes these situations even when the affine invariant quotient has forgotten them.

The symbol for the quotient stack is often written as X in square brackets divided by G. To understand what it means, we should resist describing it as simply a set of orbit labels. Over a test scheme S, an object is a principal G-bundle over S, together with a G-equivariant map from that bundle to X. An isomorphism is an isomorphism of bundles compatible with these maps.

Why introduce principal bundles instead of just taking maps from S to X? Because local choices of representatives need not glue globally into one representative. We may have local descriptions related by transition functions. A principal bundle records those transitions, and equivariance ensures that the geometric object is consistently defined.

### The simplest stack is not a space of points

Take X to be a single point. The quotient stack of that point by G is called B G, the classifying stack of G. Over a test scheme S, its objects are principal G-bundles on S. Its one geometric point carries automorphism group G.

Compare that with an ordinary one-point scheme. The scheme's unique point has no such attached family of principal bundles or automorphism groups. If all we need is a count of underlying isomorphism classes over an algebraically closed field, they might look similar. As moduli objects, they are not the same.

This difference becomes crucial in families. For a finite group, the classifying stack records finite torsors. For a connected algebraic group, it records more elaborate principal bundles. These may have nontrivial gluing even though each small piece looks trivial.

### Inertia remembers symmetries of objects

There is another construction called the inertia stack. An object of the inertia stack is an object of the original stack together with an automorphism of that object. For a quotient stack of X by G, one can picture its geometric points as pairs consisting of a point x of X and a group element g that fixes x, with a suitable quotient by conjugation and transport of x.

For the scaling action, at the origin we retain every scalar as an automorphism. At a nonzero point only the identity remains. The inertia stack therefore separates sectors of the quotient according to their stabilizer behavior.

This is not simply extra decorative metadata. Stabilizers affect deformation theories, intersection theories on stacks, and orbifold invariants. They also explain why counting objects in a moduli problem may require weighting by their automorphism groups rather than just counting labels.

### Why the quotient needs a groupoid

A groupoid is like a group where arrows can move between different objects, not only from an object to itself. The action groupoid has an arrow from x to g times x for every group element g. Composing arrows corresponds to multiplying group elements. Stabilizers are the arrows from an object back to itself.

A stack can be thought of as a groupoid-valued object satisfying a gluing condition. This makes it compatible with descent: objects and their isomorphisms can be assembled from local data, provided the compatibility conditions hold. A coarse quotient generally cannot reconstruct all that information after it has been forgotten.

There is no reason to replace every geometric space by a stack. If no automorphisms matter and a geometric quotient behaves well, ordinary spaces are often sufficient. But a moduli space of curves, bundles, or representations may contain objects with nontrivial symmetries. Treating each isomorphism class as an unadorned point can hide exactly the phenomenon we want to understand.

The general principle is straightforward. When mathematical objects can be equivalent in several ways, the equivalences are themselves mathematical data. Quotient stacks preserve those data. Stabilizers measure self-equivalences. Inertia organizes them. And descent ensures that the whole structure works in families, not just for individual points.

## Cotangent complexes, derived intersections, and virtual counts

### The Cotangent Complex: Differentials That Remember Singularities

At a smooth point of a curve, we expect one independent direction of motion. If a curve is given by one equation in the plane, its differential usually removes one of the two ambient directions. This is the familiar Jacobian picture of tangent spaces. At a singular point, however, the Jacobian can lose rank. We may then see too many apparent tangent directions. What has happened to the equation that was supposed to constrain them?

It has not disappeared. Its first derivative may have vanished, but the equation is still part of the way the space was constructed. The cotangent complex is a way of retaining both the infinitesimal directions and the relations among them. Ordinary Kähler differentials are only one part of that structure.

To see why the extra part matters, consider the algebra of dual numbers. Start with a polynomial variable x and impose x squared equals zero. The resulting ring contains a nonzero nilpotent element x. If we look only at geometric points over a field, this ring resembles a single point. But a function with a square-zero value carries a first-order direction. A reduced point and a dual-number point cannot be treated as the same infinitesimal object.

### How relations enter the differential calculation

Suppose an algebra B is presented as a polynomial algebra P modulo an ideal I. A variation of the generators belongs to the module of differentials of P. A variation must also respect the imposed relations. So there is a map from the relations, modulo relations multiplied by relations, into the differentials of P restricted to B. Each defining equation goes to its differential.

For a sufficiently well-behaved presentation, this gives a two-term model: relations in degree minus one, differentials of generators in degree zero. The map between them is the Jacobian of the defining equations. Its degree-zero homology is precisely the familiar module of Kähler differentials. Its degree-minus-one homology detects relations whose first derivatives vanish.

There is one qualification. For an arbitrary quotient, this two-term object describes the first stages of the cotangent complex, but higher syzygies may require a fuller resolution. We must not assume that every singular algebra has a two-term cotangent complex. Hypersurfaces and, more generally, suitable local complete intersections do admit the two-term model.

Return to the dual numbers over a field of characteristic different from two. There is one relation, x squared, and one generator, x. Differentiating the relation gives two x times d x. The cotangent complex is represented by a map multiplying by two x. Its degree-zero homology sees one infinitesimal direction supported at the origin. Its degree-minus-one homology is also nonzero: the relation has a nontrivial element killed by its own derivative.

If instead we worked with the reduced algebra of an ordinary point, both parts would vanish. So the cotangent complex distinguishes a thickened point from a reduced point even though the underlying set of geometric points is identical.

### Why use a complex rather than another module?

The answer becomes clearer when we change the presentation. One algebra may be described using many different generators and equations. A presentation-dependent list of Jacobian rows is not the invariant we want. We need a construction that behaves coherently under replacing an algebra by a free resolution. The result is an object of a derived category: a complex considered up to quasi-isomorphism.

This means that two computational models can have different numbers of generators, yet describe the same infinitesimal information. The cohomology groups, and more importantly the derived object that links them, are independent of the chosen resolution.

There is also a transitivity principle. If A maps to B and B maps to C, the cotangent information for C over A is related to that for B over A and C over B by an exact triangle. You can think of this as a derived version of the chain rule. Varying the final object includes variation inherited from its intermediate base and variation relative to that base.

### Lifting along a square-zero extension

The cotangent complex becomes especially useful when we try to lift a map through a small thickening. Imagine that a target ring has a square-zero ideal M, so multiplying any two elements of M gives zero. We have a map into the quotient and ask whether it lifts to the thickened ring.

A first-order deformation is not necessarily a unique answer. There can be several lifts, related by derivations. There can also be an obstruction that prevents any lift. The derived Hom groups of the cotangent complex organize these possibilities: degree zero describes infinitesimal variations, while the next Ext group can contain an obstruction. Which Ext degree appears depends on whether we are deforming a map, an algebra, or a more elaborate moduli object, so the deformation problem must always be specified.

This structure explains an important feature of singularities. Smooth objects allow infinitesimal lifts under appropriate hypotheses. Singular objects may fail the same lifting test. The extra terms of the cotangent complex provide a language in which that failure can be computed.

### The bridge to derived geometry

Ordinary algebraic geometry treats equations by taking their quotient ring. Derived algebraic geometry asks us also to retain higher homological information created by those equations, especially when constructions such as intersections are not transverse. The cotangent complex is the natural differential object in this enlarged setting.

It is tempting to call all negative-degree information an error term. That would miss the point. The extra data are not numerical artifacts to discard; they record geometric multiplicity, obstruction, and hidden relations. We need them because equations can constrain a space even when their first-order Jacobian data alone do not tell the whole story.

The practical lesson is this. If the problem involves smooth coordinate changes, ordinary differentials may be enough. If it involves singularities, deformation obstructions, or intersections with excess dimension, ask what the full cotangent complex remembers. That question leads directly to our next subject: derived intersections.

### Derived Intersections: Where Hidden Multiplicity Lives

Imagine two lines crossing in the plane. The intersection is a point, and the defining equations remove two independent directions. Now imagine intersecting a line with itself. As a set, the answer is still the line. But the two equations are not independent. If we count equations as constraints, we expected something of lower dimension. Where did the missing constraint go?

In ordinary algebraic geometry, an intersection of affine schemes is represented by a tensor product of coordinate rings. This faithfully constructs the ordinary fiber product. Yet an ordinary tensor product does not always preserve the homological information that tells us why the intersection has greater dimension than expected.

A derived tensor product retains that information. The purpose is not to replace the visible geometric intersection with an entirely different picture. It is to add the homological structure that the ordinary intersection forgot.

### A calculation with one equation

Let R be the polynomial ring in one variable t over a field k. A point at the origin corresponds to the quotient R modulo t, which is just k. Intersect that point with itself over the affine line. The ordinary tensor product of k with k over R is again k. It records a single reduced point.

Now resolve one copy of k by free R-modules. The resolution has two terms: a copy of R mapped to another copy of R by multiplication by t. Tensor this complex with the second copy of k. Multiplication by t becomes zero, because t acts as zero on k. So the resulting two-term complex has zero differential.

The homology in degree zero is k, just as for the ordinary intersection. But there is also k in homological degree one. That extra k is the first Tor group. It measures that both copies imposed the same equation. The equation was not independent the second time.

We can describe this as an excess-intersection direction. The visible point remains, but its derived structure records how it was produced. An ordinary point and the self-intersection of a point inside a line are not equivalent as derived intersections.

### Transversality is a vanishing condition

Now consider two different coordinate axes inside the affine plane. One is described by x equals zero, the other by y equals zero. Their coordinate rings are R modulo x and R modulo y, where R is the polynomial ring in x and y. When we resolve one quotient and tensor with the other, multiplication by x remains injective on the ring of the other axis. No positive Tor survives. The derived intersection is equivalent to the ordinary one.

That is the algebraic content of transversality in this example. The two constraints interact without redundancy. More generally, a pair of modules or algebras is Tor-independent over a base if their higher Tor groups vanish. Under suitable hypotheses, Tor-independence is what allows ordinary fiber products to behave as expected under base change.

Notice the difference between an ordinary intersection being nonempty and its having excess homology. Intersections can be nonempty and perfectly transverse. Tor is not a test for whether two sets meet; it tests the homological independence of the equations used to produce the meeting.

### The Koszul picture

With several defining equations, the Koszul complex offers a computational model. It combines the equations with exterior generators and a differential that inserts each equation. If the equations form a regular sequence, the Koszul complex resolves the quotient: positive homology vanishes. If they fail to be regular, higher Koszul homology can reveal the redundancy.

For example, take one equation t, then impose t again. The second constraint contributes no new ordinary restriction after the first quotient. The Koszul or derived-tensor calculation records the dependence in degree one. With more repeated or dependent constraints, several homological degrees can appear.

This is why derived intersection theory is useful in enumerative geometry. When we count solutions, the ordinary set of solutions may have positive-dimensional components where isolated answers were expected. A derived model can carry obstruction data that makes an expected-dimensional or virtual count possible, under additional hypotheses.

### A warning about multiplicity

We should not make the claim that the dimension of Tor alone gives the intersection multiplicity in every setting. Classical local intersection multiplicity is often expressed as an alternating sum of lengths of Tor groups. To use such a formula, we need conditions ensuring that the relevant lengths are finite and that we are in the appropriate regular local setting. The sign and the alternating sum both matter.

For two transverse axes, higher Tor vanishes, and the degree-zero tensor has length one: the local intersection number is one. For an isolated tangency between curves, the ordinary tensor may already have length greater than one. For self-intersections or other excess-dimensional situations, additional geometric machinery is needed. Derived homology gives the right raw information, but turning it into a number still requires a theory of integration or intersection classes.

### Why this matters beyond algebraic geometry

The same pattern occurs in algebra. Tensor product is right exact, not generally exact. Its derived functors, the Tor groups, quantify the failure of exactness. Derived intersections translate that algebraic phenomenon into geometry: a failure of independent constraints becomes nontrivial higher homology.

The central lesson is that a space is not always determined by the points it contains. It may matter how that space arose, especially when equations are repeated, redundant, or singular. A derived fiber product retains this construction data in an invariant form. The same viewpoint also applies to moduli problems: families of complexes can carry deformation directions, automorphisms, and higher obstructions invisible in an ordinary set of isomorphism classes.

### Deforming a Complex: Ext Groups as Tangents and Obstructions

Many geometric classification problems begin with points, curves, or vector bundles. But sometimes the natural object is a complex of sheaves: a sequence of bundles and maps, considered up to quasi-isomorphism. Such complexes may encode solutions of linear differential equations, coherent sheaves, or geometric objects resolved by bundles.

A moduli problem asks us to organize all these objects into families. For an ordinary moduli space, one hopes to describe its tangent directions. For a moduli stack, we must also remember automorphisms. And for a derived moduli object, we should retain the higher obstruction data that explains why a proposed family cannot always be extended.

The bridge between these three levels is remarkably concrete. For a perfect complex E, the derived endomorphism complex of E controls its infinitesimal deformation theory. Its cohomology consists of the Ext groups from E to itself.

### The three neighboring Ext groups

Begin with Ext in degree zero. This describes endomorphisms of the object in the derived category. Invertible elements give automorphisms. A moduli stack that forgets these automorphisms can misrepresent the classification problem.

Ext in degree one describes first-order deformation classes in the standard deformation theory of a perfect complex with suitable conditions. Intuitively, we have a family depending on a tiny parameter whose square is zero. The degree-one Ext group contains the ways to vary E over that first-order thickening.

Ext in degree two is where the primary obstructions to extending a chosen deformation can live. For example, we might have lifted the complex over first-order dual numbers, and now try to lift it to a thicker ring where the parameter cubed vanishes. There can be an obstruction class in Ext two. If that class is nonzero, the specified lift cannot be extended in the way requested.

This does not mean every nonzero Ext-two group guarantees an obstruction. The group is the space where an obstruction may land. The particular obstruction class must still be calculated. Conversely, vanishing Ext two is a useful sufficient condition for unobstructedness in many standard setups, but it is not a universal shortcut for every moduli problem.

### A line bundle on a curve

Consider a smooth projective connected curve C over an algebraically closed field, and a line bundle L on C. Because L is locally free of rank one, the derived endomorphisms reduce to cohomology of the structure sheaf. The zeroth Ext group is the global functions on the curve, usually just the field. The first Ext group is the first cohomology of the structure sheaf, of dimension equal to the genus. And Ext two vanishes because a smooth curve has coherent cohomological dimension one.

So the family of line bundles has genus-many infinitesimal directions, while the obstruction group vanishes. This is why the Picard variety of a smooth projective curve is smooth of dimension equal to its genus. But the moduli stack of line bundles still has scalar automorphisms; the Picard variety and the stack do not contain exactly the same information.

On the projective line, the genus is zero. A fixed-degree line bundle has no infinitesimal deformations. On an elliptic curve, the genus is one, and a degree-zero line bundle has one infinitesimal deformation direction. This example lets us see a whole derived deformation story through three familiar cohomology groups.

### Why the shift matters

For the derived moduli stack of perfect complexes, the tangent complex at E is represented, with a common cohomological convention, by the derived endomorphisms shifted by one. This shift places infinitesimal automorphisms in degree minus one, first-order deformation classes in degree zero, and obstructions in degree one.

A single tangent vector space would see only the middle term. A derived tangent complex explains how the middle term is related to automorphisms below it and obstructions above it. That is the value of derived enhancement: we are not adding arbitrary layers of abstraction, but keeping the deformation problem's natural chain of homological information intact.

### When finite presentation matters

There is an important restriction. Not every unbounded complex behaves well in families. The perfect complexes, which locally have bounded resolutions by finite-rank projective modules, provide an especially useful class. They support duality and good base-change behavior under appropriate hypotheses. On reasonable geometric bases, they form a moduli problem that can be given a derived stack structure.

If we abandon boundedness or finite-generation conditions, the moduli problem can become too large or fail to have the desired geometric finiteness. The word perfect is therefore doing real mathematical work. It is not just a more flattering name for a complex.

### From deformation groups to geometric counts

Suppose a moduli problem has too many actual directions because some conditions fail to cut transversely. Its tangent and obstruction groups may nevertheless predict an expected dimension. The difference between the dimensions of deformation and obstruction spaces is the starting point for a virtual dimension calculation, after accounting correctly for automorphisms and the specific obstruction theory.

That is why the Ext groups are more than labels attached to a classification problem. They can determine whether the moduli space is locally smooth, how many parameters we should expect, and what additional structure is needed to define meaningful counts. An obstruction theory can sometimes turn this expected-dimensional information into a virtual fundamental class even when the ordinary space has the wrong dimension.

### Virtual Fundamental Classes: Counting with Obstructions

Suppose we want to count the common zeros of several equations. In a favorable problem, each independent equation removes one dimension. We get isolated solutions, and we may assign multiplicities and sum them. But the equations might become dependent. Their common zero set might contain curves, or even an entire surface, where isolated points were expected.

One response is to perturb the equations and count the solutions that remain. In analysis and differential topology, transversality often makes this strategy effective. In algebraic geometry, perturbing may change the structure we want to preserve, or the moduli problem may be too global to admit a suitable perturbation.

Virtual fundamental classes offer another route. Instead of insisting that the ordinary zero set have the expected dimension, we retain a controlled model of the equations and their obstructions. This model can produce an intersection class in the expected degree, even when the underlying moduli space has the wrong dimension.

### A section of a vector bundle

Begin with the simplest geometric situation. Let X be a smooth space of dimension n and let E be a vector bundle of rank r. A section of E chooses one vector in each fiber. Its zero locus is the set of points where the chosen vector vanishes.

If the section meets the zero section transversely, the zero locus has dimension n minus r. This is the expected dimension. If the section is not transverse, the actual zero locus can be larger. But the original presentation of the zero locus as the zeros of a section still predicts the dimension n minus r.

For a bundle section, a canonical two-term obstruction theory can be built from the tangent bundle of X and the restriction of E to the zero locus. The derivative of the section maps tangent directions into the bundle's fibers. The failure of that derivative to be surjective is exactly the failure of transversality. A virtual class uses this two-term structure to produce an expected-dimensional cycle.

The technical construction goes through the intrinsic normal cone and an intersection with the zero section. These terms describe a precise operation in intersection theory, not an arbitrary correction to the number of solutions.

### A zero section that vanishes everywhere

Take the projective line as X and the trivial line bundle on it. Choose the section that is identically zero. The actual zero locus is the entire projective line, a one-dimensional space. But the bundle has rank one, so the expected dimension is zero.

What should its virtual zero-dimensional class be? For a section of a vector bundle over a smooth complete base, the virtual zero class is the top Chern class of the bundle capped with the fundamental class of the base. The top Chern class of a trivial line bundle is zero. So the virtual class is zero.

This is not claiming that the zero locus has no points. It has infinitely many. Nor are we declaring every point to count with weight zero by fiat. We are calculating an intersection class associated with the specified equation system. The trivial line bundle's Euler or top Chern class vanishes, and the virtual count reflects that fact.

If instead we take a generic section of the line bundle of degree one on the projective line, it has a single zero counted with multiplicity one. The virtual class has degree one. So the bundle and its class, not just the set-theoretic size of the zero locus, are essential to the count.

### The role of a perfect obstruction theory

For a general moduli space, we may not have a global smooth ambient space and vector bundle. A perfect obstruction theory is a replacement. It is, roughly, a two-term complex of vector bundles mapping to the cotangent complex of the moduli space, with compatibility conditions on its low-degree cohomology.

Those conditions are strong. They ensure that the obstruction theory faithfully captures infinitesimal deformations and obstructions up to the required degree. Its virtual rank determines a virtual dimension. Under the standard constructions, the intrinsic normal cone can then be intersected in a vector-bundle stack to produce a class of that dimension.

Different obstruction theories on the same underlying space may yield different virtual classes. The result is an invariant of the moduli problem together with the specified obstruction-theoretic structure, not a number determined solely by the set of geometric points.

### The connection to derived geometry

A quasi-smooth derived space has a cotangent complex of Tor-amplitude in degrees minus one and zero. Its derived structure naturally supplies the kind of two-term information needed for a perfect obstruction theory on its ordinary truncation. This makes derived geometry more than a vocabulary for hidden Tor groups. It explains why a virtual class belongs naturally to a moduli problem whose equations may have dependent constraints.

One should still distinguish constructing a virtual class from integrating it to obtain a numerical invariant. A numerical count generally needs properness, a class of the correct degree, and suitable choices of insertions or evaluation maps. If the moduli space is not proper, its virtual class may exist without there being a finite number to report.

### What the count is actually saying

Virtual classes appear in enumerative geometry, for instance when counting curves subject to incidence conditions. The ordinary moduli space of curves can have components of unexpected dimension, and some curves have automorphisms. A complete theory needs to account for both deformation-obstruction data and stack-theoretic symmetries.

The central idea is not that every geometric count should be replaced by a virtual one. In a transverse problem the virtual class agrees with the ordinary fundamental class of the solution locus. Its value appears when transversality fails but the underlying problem retains enough structure to define an expected-dimensional class.

The broader mathematical picture connects four ideas. Cotangent complexes reveal relations beyond ordinary differentials. Derived intersections retain excess Tor. Derived moduli connect tangent directions, automorphisms, and obstructions. Virtual fundamental classes convert that information into intersection-theoretic invariants, with carefully stated hypotheses about the moduli problem and the chosen obstruction theory.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Complexes, Riemann-Roch, and moduli obstructions

### Complexes, Riemann-Roch, and moduli obstructions

#### Companions, sources, and study material (not spoken)

##### Deformation-Obstruction Complexes in Moduli Problems

**Track:** Abstract Algebra. **Background:** Ext groups, cotangent complexes, line bundles, families, deformation theory. **Central question:** why can a space of mathematical objects have tangent directions, symmetries, and obstructions all at once?

###### Mathematical companion (not spoken)

For a coherent sheaf E on a fixed smooth projective X, the standard deformation-obstruction complex is `RHom_X(E,E)` (with the customary shifts in the derived moduli formalism). In classical deformation theory:
\[
\operatorname{Ext}^0_X(E,E)\;\text{(infinitesimal automorphisms)},\quad
\operatorname{Ext}^1_X(E,E)\;\text{(first-order deformations)},\quad
\operatorname{Ext}^2_X(E,E)\;\text{(obstruction space)}.
\]
An obstruction is an actual class in `Ext^2`; a nonzero obstruction *space* does not guarantee obstruction for a given deformation.

For an invertible sheaf L on a smooth projective curve C, `RHom(L,L)=R Gamma(O_C)`, so `Ext^i(L,L)=H^i(C,O_C)`. Thus `dim Ext^1=g`, `Ext^2=0` and `Ext^0=k` for a geometrically connected curve over an algebraically closed field. This matches the tangent dimension of `Pic(C)`; the scalar automorphisms of L still matter if one studies the moduli *stack* rather than the Picard *scheme*.

For the deformation of a smooth proper scheme X, the classical groups are `H^i(X,T_X)` in degrees `i=0,1,2`. More generally, cotangent-complex expressions `Ext^i_X(L_{X/k},O_X)` encode deformations and obstructions (with indexing dependent on the exact deformation functor). Smoothness and properness are not optional assumptions when using the simplest tangent-sheaf formula.

##### Exercises with answers

1. What is the infinitesimal deformation dimension of a line bundle on a smooth genus-two curve? **Answer:** two, since `dim H^1(O_C)=2`.
2. Does `Ext^2(E,E) != 0` prove every deformation is obstructed? **Answer:** no; obstruction classes can vanish.
3. Why can a coarse moduli point conceal information? **Answer:** it records an isomorphism class but not necessarily its automorphism group.
4. What replaces the ordinary sheaf of differentials in singular deformation theory? **Answer:** the cotangent complex.

##### Reading and source notes

- [Stacks Project, Deformation Theory](https://stacks.math.columbia.edu/download/defos.pdf), deformations of modules, schemes, and complexes.
- [Stacks Project, Key example in Artin's axioms](https://stacks.math.columbia.edu/tag/07YI), explicit obstruction maps from equations.
- [Stacks Project, Cotangent complex](https://stacks.math.columbia.edu/tag/08P5), derived control of infinitesimal deformations.

##### Derived Deformation Theory: Obstructions Beyond the Tangent Space

**Track:** Abstract Algebra. **Background:** Ext, cotangent complexes, derived categories, first-order deformation theory. **Central question:** how can a deformation be possible to first order but impossible to second order?

###### Mathematical companion (not spoken)

Take `A_1=k[t]/(t^2)` and `A_2=k[t]/(t^3)` with `char(k) != 2`. For `F(x)=x^2`, `x=t` solves `F(x)=0` in `A_1`. Every lift with the same linear term in `A_2` has the form `x=t+a t^2`, so `F(x)=t^2 (mod t^3) != 0`: the lift is obstructed.

A simple dg Lie algebra model has `g^1=k e`, `g^2=k f`, `d=0`, `[e,e]=2f`, and `f` central. This satisfies graded antisymmetry (odd-degree self-brackets need not vanish) and Jacobi. For `alpha=t e`, the Maurer–Cartan equation is
\[
d\alpha+\tfrac12[\alpha,\alpha]=t^2 f=0.
\]
It holds over `A_1` but fails over `A_2`. In the standard characteristic-zero dg-Lie convention, `H^0(g)` measures infinitesimal automorphisms, `H^1(g)` the first-order tangent space and `H^2(g)` the obstruction *space*; an actual obstruction is a specific class in `H^2(g)`. The zero-bracket case illustrates unobstructed formal directions, subject to the precise deformation functor and convergence or algebraization questions.

For a distinguished triangle of complexes `A -> B -> C -> A[1]`, the cohomology sequence includes
\[
H^1(A)\to H^1(B)\to H^1(C)\xrightarrow{\delta} H^2(A)\to H^2(B).
\]
The connecting map `delta` provides a mechanism by which a deformation in `C` can fail to lift to `B`. Not every triangle is automatically a tangent-obstruction triangle: the complexes must actually control the relevant deformation problems.

##### Exercises with answers

1. Over `k[t]/(t^4)`, can `x=t+a t^2+b t^3` solve `x^2=0`? **Answer:** no; its `t^2` coefficient is always one.
2. If an obstruction group is nonzero, must the deformation be obstructed? **Answer:** no; the particular obstruction class can vanish.
3. In the two-generator dg-Lie example, what is the obstruction class for `alpha=t e`? **Answer:** the coefficient `f` of `t^2`, representing a nonzero class in degree two.
4. Which map in a long exact sequence can obstruct lifting a tangent class? **Answer:** a connecting homomorphism from the relevant degree-one group to a degree-two group.

##### Reading and source notes

- [The Stacks Project, Deformation Theory](https://stacks.math.columbia.edu/download/defos.pdf), deformation and obstruction calculations for algebraic objects.
- [The Stacks Project, Cotangent Complex](https://stacks.math.columbia.edu/tag/08P5), derived deformation data and comparison sequences.
- [Manetti, Lectures on Deformations of Complex Manifolds](https://arxiv.org/abs/math/0507286), differential graded Lie algebras and deformation functors.

### Quotient Stacks: Spaces That Remember Symmetry

**Track:** Abstract Algebra. **Background:** algebraic group actions, schemes, moduli, descent and torsors. **Central question:** what is lost when we replace objects with their isomorphism classes?

#### Mathematical companion (not spoken)

For an action of a group scheme G on X, a test scheme S-point of `[X/G]` consists of a G-torsor `P -> S` together with a G-equivariant map `P -> X`; arrows are equivariant torsor isomorphisms respecting the maps. For X a point, `[Spec(k)/G]=BG` classifies G-torsors.

For the action `G_m x A^1 -> A^1`, `(t,x) -> tx`, the invariant ring is `k[x]^{G_m}=k`, so the affine categorical quotient is `Spec k`. Geometrically, the stabilizer of `x=0` is `G_m`; for `x != 0` it is trivial. The two geometric orbit types are not captured by the invariant affine quotient.

For a quotient stack, the inertia stack can be presented by the quotient of the fixed-pair scheme:
\[
I([X/G]) \simeq [\{(x,g)\in X\times G: gx=x\}/G],
\]
where `h in G` acts on `(x,g)` by `(hx,hgh^{-1})` (with the scheme-theoretic fiber product construction underlying this formula). Over arbitrary base fields, twisting and torsors matter; a list of geometric fixed pairs is not a complete description of all S-points.

##### Exercises with answers

1. What is an object of `BG` over S? **Answer:** a principal G-bundle on S.
2. What is the stabilizer of zero in the scaling action of `G_m`? **Answer:** all of `G_m`.
3. Why is a coarse invariant quotient inadequate for the scaling example? **Answer:** the invariant ring is only k, so it collapses all geometric points and loses the different stabilizers.
4. What extra datum does the inertia stack remember? **Answer:** a chosen automorphism of an object, up to the stack's equivalence relation.

##### Reading and source notes

- [The Stacks Project, Algebraic Stacks](https://stacks.math.columbia.edu/download/algebraic.pdf), quotient stacks, groupoids and descent.
- [The Stacks Project, Groupoid Schemes](https://stacks.math.columbia.edu/download/groupoids.pdf), action groupoids and quotient presentations.
- [Edidin, Notes on the Construction of the Moduli Space of Curves](https://arxiv.org/abs/math/9805101), quotient stacks and moduli motivation.

### Cotangent complexes, derived intersections, and virtual counts

### Cotangent complexes, derived intersections, and virtual counts

#### Companions, sources, and study material (not spoken)

##### The Cotangent Complex: Differentials That Remember Singularities

**Track:** Abstract Algebra. **Background:** Kahler differentials, modules, derived functors, deformations, and affine schemes. **Central question:** how can a tangent-space construction detect the equations and relations that ordinary differentials forget?

###### Mathematical companion (not spoken)

For a map of commutative rings `A -> B`, the cotangent complex `L_{B/A}` is an object of the derived category of B-modules. With cohomological indexing it is commonly represented in nonpositive degrees. Its zeroth cohomology is `Omega_{B/A}`.

For a **local complete intersection** quotient `B=P/I`, where P is smooth over A and I is locally generated by a regular sequence, a two-term model is
\[
L_{B/A}\simeq [I/I^2\xrightarrow{d}\Omega_{P/A}\otimes_P B],
\]
with `I/I^2` in degree `-1`. For a general quotient the same two-term expression gives the truncation through degree `-1`, not necessarily the full derived object.

**Dual-number calculation.** Let `k` be a field with `char(k) != 2` and `B=k[x]/(x^2)`. Then
\[
L_{B/k}\simeq [B\xrightarrow{2x}B],\quad
H^0(L)=B/(2x)\cong k,\quad H^{-1}(L)=\ker(2x)=(x)\cong k.
\]
By comparison, `L_{k/k}=0`. The singularity is detected by nonvanishing degree `-1` homology.

For composable `A -> B -> C`, the transitivity triangle is
\[
L_{B/A}\otimes_B^{\mathbf L} C\longrightarrow L_{C/A}\longrightarrow L_{C/B}\longrightarrow (L_{B/A}\otimes_B^{\mathbf L} C)[1].
\]
In an appropriate deformation/lifting problem, the obstruction to lifting a specified morphism against a square-zero extension lies in an `Ext^1` group of the relevant pulled-back cotangent complex; when it vanishes, lifts form a torsor under `Ext^0`, assuming the standard finiteness and setup hypotheses. For deformation of an **algebra** against a fixed base, the conventional degree indexing often appears as `Ext^2(L_{B/A},M)` for obstruction and `Ext^1` for isomorphism classes of deformations. The two settings must not be conflated.

##### Exercises with answers

1. For `B=k[x]`, compute `L_{B/k}`. **Answer:** the free B-module `B dx` in degree zero; there is no negative-degree term.
2. For the dual numbers over characteristic zero, why is `H^{-1}` nonzero? **Answer:** multiplication by `2x` kills the nonzero element `x` in B.
3. Can two different free resolutions define different cotangent complexes? **Answer:** not up to the derived equivalence used in the construction.
4. What goes wrong if an arbitrary quotient is assumed to have only a two-term cotangent complex? **Answer:** higher syzygies and higher homology may be omitted.

##### Reading and source notes

- [The Stacks Project, The Cotangent Complex](https://stacks.math.columbia.edu/download/cotangent.pdf), resolutions, transitivity and local complete intersections.
- [The Stacks Project, Deformation Theory](https://stacks.math.columbia.edu/download/defos.pdf), square-zero extensions, lifting and obstructions.
- [Toën, Higher and Derived Stacks: A Global Overview](https://arxiv.org/abs/math/0604504), why derived structures enter moduli geometry.

##### Derived Intersections: Where Hidden Multiplicity Lives

**Track:** Abstract Algebra. **Background:** tensor products, Tor, affine schemes, regular sequences, and cotangent complexes. **Central question:** what information is lost when two geometric pieces meet nontransversely?

###### Mathematical companion (not spoken)

For `R=k[t]`, consider the free resolution of `k=R/(t)`:
\[
0\longrightarrow R\xrightarrow{t}R\longrightarrow k\longrightarrow0.
\]
After tensoring over R with k, the differential becomes zero:
\[
k\otimes_R^{\mathbf L}k\simeq[k\xrightarrow{0}k].
\]
Thus `Tor^R_0(k,k)=k` and `Tor^R_1(k,k)=k`, with higher Tor zero. Ordinary `k\otimes_R k=k` keeps only degree zero.

For `R=k[x,y]`, `A=R/(x)`, `B=R/(y)`, the resolution `[R --x--> R]` tensored with B becomes `[k[x] --x--> k[x]]`, which has no positive homology because x is a nonzerodivisor. Hence `Tor_i^R(A,B)=0` for `i>0` and `A\otimes_R B=k`.

Under suitable finite-length conditions for finitely generated modules over a **regular local ring**, Serre's intersection multiplicity takes the form
\[
\chi(M,N)=\sum_{i\ge 0}(-1)^i\operatorname{length}_R\operatorname{Tor}_i^R(M,N).
\]
Do not apply this expression as a finite number when tensor products or Tor groups do not have finite length. A Koszul complex on a regular sequence is a free resolution of its quotient; for a nonregular sequence, positive Koszul homology need not vanish.

##### Exercises with answers

1. Compute `Tor_1^{k[t]}(k[t]/(t),k[t]/(t))`. **Answer:** k, using the two-term resolution.
2. Why do two transverse coordinate axes have no positive Tor in the given model? **Answer:** x acts injectively on `R/(y)=k[x]`.
3. Is positive Tor required for an intersection to be nonempty? **Answer:** no; a transverse point has no positive Tor.
4. Why is `dim_k Tor_1` not in general an intersection multiplicity? **Answer:** proper definitions may require an alternating sum of finite lengths and suitable regularity/properness conditions.

##### Reading and source notes

- [The Stacks Project, More on Algebra](https://stacks.math.columbia.edu/download/more-algebra.pdf), Tor, Koszul complexes and regular sequences.
- [The Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), multiplicities, excess intersection and intersection products.
- [Toën, Higher and Derived Stacks: A Global Overview](https://arxiv.org/abs/math/0604504), derived fiber products and intersection-theoretic motivation.

##### Deforming a Complex: Ext Groups as Tangents and Obstructions

**Track:** Abstract Algebra. **Background:** derived categories, perfect complexes, Ext, sheaf cohomology, and deformation theory. **Central question:** if our objects are complexes rather than points or bundles, what counts as an infinitesimal motion?

###### Mathematical companion (not spoken)

For a perfect complex E on an appropriate scheme X, the derived endomorphism complex is `RHom_X(E,E)`. Under standard conventions for the derived moduli of perfect complexes,
\[
T_E\mathcal{P}erf(X)\simeq \operatorname{RHom}_X(E,E)[1],\qquad
H^{-1}(T_E)=\operatorname{Ext}^0(E,E),\quad
H^0(T_E)=\operatorname{Ext}^1(E,E),\quad
H^1(T_E)=\operatorname{Ext}^2(E,E).
\]
The `Ext^0` group is an infinitesimal automorphism space, not automatically the full automorphism group; invertibility is an additional condition. `Ext^2` is a possible obstruction **space**, not a proof of an actual obstruction.

For a line bundle L on a smooth projective geometrically connected curve C over an algebraically closed field,
\[
\operatorname{RHom}(L,L)\simeq R\Gamma(C,L^\vee\otimes L)=R\Gamma(C,\mathcal O_C).
\]
Hence `Ext^0(L,L)=k`, `dim Ext^1(L,L)=g`, and `Ext^i(L,L)=0` for `i>=2`. On `P^1`, `g=0`; on an elliptic curve `g=1`. The Picard **stack** still has `G_m` automorphisms, while the fixed-degree Picard **scheme** has tangent dimension g.

The local perfectness requirement means E is locally quasi-isomorphic to a bounded complex of finite-rank vector bundles. Obstruction theories for other objects or for complexes over singular bases may require additional hypotheses. The expected dimension of a derived moduli stack must treat negative-degree tangent terms (automorphisms) appropriately; it is not generally `dim Ext^1 - dim Ext^2` without qualification.

##### Exercises with answers

1. What is the first-order deformation space of a perfect complex in the standard setup? **Answer:** `Ext^1(E,E)`.
2. Does nonzero `Ext^2(E,E)` imply every deformation is obstructed? **Answer:** no; the actual obstruction class may vanish.
3. For a line bundle on a genus-two smooth projective curve, what are the dimensions of `Ext^1` and `Ext^2`? **Answer:** two and zero, respectively.
4. Why do we retain `Ext^0` in a moduli stack? **Answer:** it records infinitesimal self-equivalences, which an ordinary set of isomorphism classes forgets.

##### Reading and source notes

- [The Stacks Project, Derived Categories](https://stacks.math.columbia.edu/download/derived.pdf), derived Hom and perfect complexes.
- [Toën and Vaquié, Moduli of Objects in dg-Categories](https://arxiv.org/abs/math/0503269), derived moduli and tangent complexes.
- [The Stacks Project, Cohomology of Schemes](https://stacks.math.columbia.edu/download/coherent.pdf), coherent cohomology and geometric examples.

##### Virtual Fundamental Classes: Counting with Obstructions

**Track:** Abstract Algebra. **Background:** tangent complexes, local complete intersections, vector bundles, Chow groups, and moduli problems. **Central question:** how can geometry define a meaningful expected-dimensional count when a solution space is larger or more singular than expected?

###### Mathematical companion (not spoken)

For smooth X of pure dimension n and rank-r vector bundle E with section s and zero locus Z, the two-term perfect obstruction theory on Z can be represented dually by the map `T_X|_Z -> E|_Z`, with expected dimension `n-r`. If the section is regular, Z has the expected dimension and the virtual class equals its ordinary fundamental class. In general, the virtual zero-locus class pushed to X is
\[
i_*[Z]^{\mathrm{vir}}=c_r(E)\cap[X],
\]
where `i:Z->X`, provided the standard intersection-theoretic hypotheses hold.

**Example 1.** `X=P^1`, `E=O_{P^1}`, `s=0`: `Z=P^1` actually has dimension one; the virtual dimension is zero; `c_1(O)=0`, hence `[Z]^vir=0` in `A_0(P^1)`.

**Example 2.** `X=P^1`, `E=O_{P^1}(1)`, a generic nonzero section: the zero locus is one reduced point, and `deg(c_1(O(1)) cap [P^1])=1`.

For a perfect obstruction theory `phi:E^\bullet -> L_M` of amplitude `[-1,0]`, standard hypotheses require `h^0(phi)` to be an isomorphism and `h^{-1}(phi)` a surjection. The virtual dimension is the virtual rank of `(E^\bullet)^\vee` (equivalently, rank of degree-zero bundle minus degree-minus-one bundle under a compatible presentation). Having an obstruction **space** does not mean all deformation classes are obstructed. Nonproper moduli spaces need not yield numerical virtual counts merely from the existence of a class.

##### Exercises with answers

1. What is the expected dimension of the zero locus of a section of rank-three E on smooth fivefold X? **Answer:** two.
2. Why is the zero section of a trivial line bundle not a transverse example? **Answer:** its derivative is zero, hence cannot surject onto a rank-one fiber.
3. Does the same underlying zero set uniquely determine a virtual class? **Answer:** no; the chosen obstruction theory and moduli presentation matter.
4. Which additional condition is generally needed to integrate a zero-dimensional virtual class to a finite count? **Answer:** properness, or an alternative construction that justifies the integral.

##### Reading and source notes

- [Behrend and Fantechi, The Intrinsic Normal Cone](https://arxiv.org/abs/alg-geom/9601010), perfect obstruction theories and virtual fundamental classes.
- [The Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), Chern classes, Gysin maps and intersection products.
- [Toën, Higher and Derived Stacks: A Global Overview](https://arxiv.org/abs/math/0604504), derived enhancement and virtual intersection theory.
