# 032000 — Homotopy Limits: Why a Pullback Can Contain Loops

**Track:** Introduction to Category Theory. **Background:** pullbacks, spaces, paths, mapping spaces, and infinity-categories. **Theme:** derived limits, homotopy pullbacks, loop spaces, and universal properties.

<!-- BEGIN SPOKEN LECTURE -->

# Homotopy Limits: Why a Pullback Can Contain Loops

Take a circular running track and choose a starting point on its edge. A runner can leave that point, travel once around the circle, and come back. Another runner can stand still. A third can travel twice around. All three begin and end at exactly the same location. If we inspect only their endpoints, the three journeys look identical. If we remember the actual paths, they are fundamentally different.

Now consider two maps from a single point into that same circle. Both maps select the starting point. In the ordinary category of sets, their pullback is just a point. There is only one way to choose that point in the left-hand set and that point in the right-hand set so that their images agree. But in homotopy theory, a more informative pullback contains all paths from the chosen point back to itself. It remembers the stationary runner, the once-around runner, the twice-around runner, and infinitely many other winding classes.

This is a compelling reason to study homotopy limits. An ordinary limit asks for exact agreement. A homotopy limit asks for compatibility together with the data that witness agreement up to homotopy. In a category where maps can be deformed, replacing equality by a mere yes-or-no answer discards useful information.

The goal is to understand this change precisely. We will derive a model for a homotopy pullback, calculate its simplest nontrivial example, explain the corresponding universal property, and see when an ordinary pullback can safely compute the homotopy answer.

## Ordinary pullbacks as a compatibility test

Consider a diagram of sets. A maps to C, and B maps to C. Call the maps f and g. The pullback consists of pairs, one element a from A and one element b from B, satisfying the condition that f of a equals g of b.

We can think of A as a catalog of employees, B as a catalog of office keys, and C as a catalog of departments. A record in the pullback is an employee and a key assigned to the same department. If an employee belongs to department two and a key belongs to department three, the pair is excluded. The agreement must be exact.

The universal property says that for any set T, a map from T into the pullback is equivalent to giving a map from T into A and a map from T into B whose composites to C agree. There is no freedom beyond that agreement. Once the two maps are compatible, their pairing is unique.

That definition is correct for sets. But the same formula applied naively to topological spaces may fail to respect the homotopy type of the diagram. Two spaces can be weakly equivalent while an ordinary pullback changes dramatically after replacing one of them by a weakly equivalent model.

The problem is that equality of points is a rigid condition. A homotopy-theoretic construction should remain meaningful when the inputs are replaced by equivalent spaces. The strict pullback need not do that unless a suitable fibration or other technical hypothesis makes it homotopy invariant.

## Replace equality with a path

Let A and B be topological spaces mapped into C. Instead of demanding that f of a equal g of b, select a path in C from f of a to g of b. A point in the resulting construction is a triple: an element of A, an element of B, and a connecting path in C.

The first two entries locate the data we wish to compare. The third entry certifies their compatibility up to continuous deformation. Crucially, two different paths may count as different evidence. One path could go clockwise around an obstacle and another counterclockwise. Even if both begin and end at the same points, they need not be deformable into each other while the endpoints remain fixed.

This gives a standard path-space model of the homotopy pullback. Rather than write a set of compatible pairs, we construct a space of compatible triples. The topology on the path space lets the triples themselves vary continuously, so it records higher homotopies among choices of connecting path.

This model shows the basic principle without requiring the full technical language of model categories. More generally, in a model category one constructs a homotopy pullback by replacing the original diagram with a suitably fibrant one and taking its ordinary pullback. In the infinity-category of spaces, the homotopy pullback is simply the pullback specified by the higher-categorical universal property.

It is helpful to distinguish a construction from its invariant meaning. A path-space triple is one practical model. The invariant object is the homotopy type characterized by the mapping-space universal property. Another correct model may have different-looking points while representing an equivalent space.

## The calculation: pull back a point along itself

Return to the circle. Let C be the circle, and let both A and B consist of one point. The two maps choose the same basepoint of the circle. Under strict equality, the pullback contains one compatible pair, because the images coincide.

For the homotopy pullback, a point is that same pair together with a loop based at the chosen point. The resulting space is called the based loop space of the circle. We commonly write it as omega of the circle.

What are the connected components of this loop space? Start by counting winding numbers. A loop can run once counterclockwise, twice counterclockwise, once clockwise, or not wind at all. A continuous deformation through based loops cannot change the total integer number of turns. The winding number is therefore constant along each connected component.

Conversely, two based loops of the circle with the same winding number can be deformed into one another through based loops. Thus the components are indexed by all integers. The based loop space is homotopy equivalent to the discrete set of integers. More precisely, each component is contractible; the component label is the integer winding number.

Compare the answers. The strict pullback gives one point. The homotopy pullback gives countably many components. These spaces are not equivalent. The missing information is exactly the possible paths witnessing equality of the two chosen points.

This example is compact, yet it contains much of the motivation for infinity-categorical limits. A limit can carry genuine topological information even when its input diagram contains only three spaces and two maps.

## When endpoints are different

What if the two point maps choose different locations on the circle? As a strict pullback of sets or spaces, the construction is empty: the selected points are not equal. But in the homotopy pullback, we are asked to choose a path from one selected location to the other. Such paths exist because the circle is path connected.

There are again infinitely many components, indexed by the number of extra times a path winds around the circle. To make the indexing precise we choose a reference path between the two locations; comparing any other path against it yields a based loop and hence an integer. Without that choice, it is accurate to say the components form an integer torsor rather than a canonically numbered set of integers.

That small qualification matters. A basepoint or reference path is often the extra choice needed to label a collection canonically. Algebraic topology distinguishes having a collection with the structure of a torsor from having a chosen origin in that collection.

The result also explains why physical metaphors are useful but insufficient by themselves. The mere fact that two points are joined by a path does not say which path was chosen. The mathematical object must record both existence and the possible witnesses of existence.

## Homotopy fibers

The same construction produces the homotopy fiber of a map. Let f send a space E into a space B, and choose a point b of B. Form the homotopy pullback of E to B and the chosen point to B.

A point in this homotopy fiber consists of a point e of E and a path in B from f of e to b. This remembers the ways an element can land at b up to homotopy, instead of demanding exact equality in the chosen model.

For instance, if f is a covering map, the ordinary fiber over b already consists of the points mapping exactly to b. Under standard fibration hypotheses, that ordinary fiber models the homotopy fiber. But for arbitrary maps, the homotopy fiber behaves better under weak equivalence and allows us to discuss the fiber sequence of a map invariantly.

Notice the connection to path lifting. If one has a fibration in the topological sense, paths in the base can be lifted appropriately, allowing the path-data in the homotopy fiber to be replaced, up to homotopy, by an actual point in the strict fiber. That is a geometric explanation for the technical condition that makes strict pullbacks reliable in some cases.

A homotopy fiber is useful for measuring how far a map is from being an equivalence. If a suitable map has contractible homotopy fibers everywhere, it is frequently a candidate for a weak equivalence, subject to the appropriate hypotheses on the setting. More generally, homotopy fibers fit into long exact sequences of homotopy groups. They are one of topology's basic computational tools.

## Equalizers with homotopies

Pullbacks are not the only ordinary limits that require adjustment. An equalizer of two maps f and g from A to B consists of those points a where f of a and g of a are equal. The homotopy equalizer instead records a point a together with a path from f of a to g of a.

This is a direct analogue of the compatible triple construction. The point in A supplies the candidate input; the path in B supplies the witness that its two images agree up to homotopy. The homotopy equalizer is no longer determined just by the subset where the functions happen to coincide.

If A itself is a point and both f and g pick the same basepoint of B, the homotopy equalizer is again a loop space of B. The extra path does the mathematical work. If the two picked points are different but path connected, the homotopy equalizer can still be nonempty.

This makes the general lesson visible: homotopy limits do not simply mean applying an ordinary limit and then taking homotopy classes of the result. Doing that throws away precisely the path information we needed to construct the right object in the first place.

## A universal property of spaces, not sets

An ordinary pullback P is characterized by a bijection between maps from a test object T into P and compatible pairs of maps to A and B. In higher category theory, replace those hom-sets by mapping spaces. The mapping space from T into the homotopy pullback must be equivalent to the homotopy pullback of the mapping spaces from T into the original diagram.

The word equivalent matters. We do not ask for literal equality of points in two models. We ask for an equivalence preserving paths and higher information. That is the appropriate higher-categorical statement that the proposed object represents the system of compatible maps.

For the pullback of a point along itself over the circle, this universal property forces the answer to remember loops. If we used a single point, we would fail the universal property when testing against spaces that detect winding and homotopies.

The same approach defines arbitrary homotopy limits. A cone to a diagram consists of compatible maps from a proposed vertex into every object, together with coherent comparison data. A homotopy limit is an object that represents the space of such cones. It is characterized up to equivalence rather than by a particular point-set model.

This is why homotopy limits live naturally in infinity-categories. Ordinary categories ask whether two composites are equal. Higher categories ask for the full spaces of coherent comparisons, and the universal property is designed to respect them.

## A common trap: taking limits after passing to classes

Suppose we first replace every mapping space by its set of components, producing the ordinary homotopy category. Then we compute a pullback there. Would that recover the homotopy pullback? Generally no. The resulting calculation sees equivalence classes of maps but not the particular homotopies witnessing compatibility.

For the circle, the basepoint map and itself become the same arrow in the homotopy category. The set-level diagram does not remember the infinitely many based loops that will constitute the homotopy pullback. The homotopy type is absent from the input data.

One might object that ordinary categories can be enhanced with model structures, simplicial enrichment, or explicit derived functors. That is correct. Homotopy limits were studied extensively in those languages. The point is that the homotopical enhancement contains additional information beyond a bare ordinary homotopy category. Infinity-category theory organizes that enhancement through mapping spaces and coherent cones.

This distinction is also useful in algebra. A right-derived functor is not normally obtained by ignoring resolutions and simply applying an ordinary functor to isomorphism classes. We replace or resolve objects so that the construction respects the intended equivalences. Homotopy pullbacks provide a geometric model of the same principle.

## Replacing a diagram instead of hoping it behaves

In a model category, a homotopy pullback is often calculated by replacing one of the arrows into the base with a fibration. That replacement must be a weak equivalence to the original object, and the new diagram should genuinely represent the same homotopical problem. We can see the idea in the circle example without using all the formal model-category axioms.

Replace the map from a point to the circle by the space of paths that begin at the chosen point, together with evaluation at the other endpoint. The total space of these starting paths is contractible: each path can be shortened toward its starting point. Evaluation at the endpoint is a path-space fibration. Taking an ordinary fiber of that endpoint map over the chosen basepoint yields exactly the based loops of the circle.

This is a concrete fibrant replacement calculation. The point has been replaced by a contractible path space, so it has the same weak homotopy type. But the new map to the circle is better behaved under taking fibers. The ordinary pullback after replacement gives the homotopy pullback we wanted. There is no mysterious instruction to add infinitely many points by hand; the loop components emerge from an ordinary construction applied to an appropriate model.

This method also makes the invariance requirement explicit. A derived construction should not change merely because we replaced an object by a weakly equivalent one to make calculation possible. Choosing good replacements is a way of ensuring that the operation respects the intended equivalences.

## Why a homotopy pushout is the dual story

The dual construction is a homotopy pushout. An ordinary pushout glues two spaces along a shared subspace by identifying corresponding points. A homotopy pushout glues with a cylinder or other homotopically sound replacement that records the gluing process rather than enforcing a potentially troublesome identification too early.

Take two copies of a point and let a space consisting of two discrete points map to each of them by the unique map. The ordinary pushout identifies the two target points and gives a single point. A standard homotopy pushout attaches a segment for each of the two source points between the target points. The result is a graph with two vertices connected by two edges, which has the homotopy type of a circle.

This is a dual analogue of the loop-space calculation. The naive point-set quotient cannot see the cycle made by the two separate gluing witnesses. The homotopy pushout remembers it as a loop in the resulting space. It illustrates how higher colimits preserve information from the way objects are identified.

Homotopy colimits appear in gluing spaces, classifying spaces, and topology of diagrams. Homotopy limits appear in compatible sections, deformation problems, and descent. The common principle is to preserve homotopically meaningful witnesses rather than collapse all compatibility to strict equality at the beginning of the calculation.

## From loops to local-to-global reconstruction

Homotopy limits appear in descent. Imagine a space covered by overlapping regions. A global object should restrict to local objects on each region. On an overlap the restrictions should be compatible. But if the objects have automorphisms, compatibility is often expressed through isomorphisms rather than literal equality.

On triple overlaps those isomorphisms must satisfy coherence conditions. For still richer objects, the coherence itself has higher comparisons. A homotopy limit over the diagram formed by all intersections of the cover provides a systematic way to record this tower of compatibility data.

That is one mathematical route from sheaves to stacks and higher stacks. A set-valued sheaf glues local values. A groupoid-valued stack glues objects and their isomorphisms. A space-valued higher sheaf can retain homotopies among the gluing maps themselves. In each case, the relevant limit must preserve the level of structure present in the objects.

There is a practical reason for requiring descent: local coordinates and local constructions are often easier than global ones. But local simplicity does not imply global triviality. The way local pieces match can encode global topology. The circle's loops provide a miniature example of how compatibility witnesses can contain more than a single yes-or-no answer.

## Choosing the right construction

We have reached a useful decision rule. An ordinary pullback of sets is exactly right when agreement is an equality of values. A strict pullback of spaces may also be homotopy correct when a suitable fibration condition is present. Without those conditions, the strict construction can depend on an unfortunate choice of presentation.

A homotopy pullback asks for agreement through a path. Its answer can contain many components even where the ordinary pullback has only one point, or it can be nonempty where the strict pullback is empty. The path is part of the answer because the way two things agree can carry information of its own.

When we say that two maps agree up to homotopy, we ought to ask what homotopy witnesses that agreement and how different witnesses compare. The space of answers may be the actual object we need. That is what homotopy limits are built to preserve.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Given maps \(f:A\to C\) and \(g:B\to C\) of suitably nice spaces, a path-space model of their homotopy pullback is
\[
 A\times_C^h B=\{(a,b,\gamma)\mid a\in A,\ b\in B,\ \gamma:[0,1]\to C,\ \gamma(0)=f(a),\ \gamma(1)=g(b)\}.
\]
It is the ordinary pullback of \(A\times B\xrightarrow{(f,g)}C\times C\) along the endpoint evaluation \(C^{[0,1]}\to C\times C\). This realizes a derived pullback under the standard homotopical hypotheses.

For a pointed space \((C,c)\),
\[
 *\times_C^h *\simeq\Omega_c C.
\]
For \(C=S^1\), \(\pi_0(\Omega S^1)\cong\pi_1(S^1)\cong\mathbb Z\), and all components of \(\Omega S^1\) are contractible. Thus \(\Omega S^1\simeq\mathbb Z\) as a discrete homotopy type. The strict pullback \(*\times_{S^1}*\) at the same basepoint is a single point.

In an infinity-category \(\mathcal C\), a pullback \(P=A\times_C B\) satisfies the natural equivalence
\[
 \mathrm{Map}_{\mathcal C}(T,P)\simeq
 \mathrm{Map}_{\mathcal C}(T,A)\times^h_{\mathrm{Map}_{\mathcal C}(T,C)}\mathrm{Map}_{\mathcal C}(T,B).
\]
In model categories, a strict pullback can compute the derived one when the diagram is appropriately fibrant; for spaces with fibrant objects, it suffices that one map into the base be a fibration under standard conventions.

The homotopy equalizer of \(f,g:A\rightrightarrows B\) can be modeled by
\[\mathrm{Eq}^h(f,g)=\{(a,\gamma)\mid a\in A,\ \gamma:f(a)\leadsto g(a)\}.\]

### Exercises with answers

1. **Same basepoint.** Compute the ordinary pullback of \(*\to S^1\leftarrow *\) with identical selected points. **Answer:** one point.
2. **Homotopy answer.** Compute its homotopy pullback up to weak equivalence. **Answer:** the based loop space \(\Omega S^1\), equivalent to discrete \(\mathbb Z\).
3. **Different points.** Why can the homotopy pullback of two distinct points over \(S^1\) be nonempty? **Answer:** a path connects them; components are a \(\mathbb Z\)-torsor after choosing a reference path.
4. **Homotopy equalizer.** What extra datum does it require beyond a strict equalizer? **Answer:** a connecting path witnessing \(f(a)\simeq g(a)\).
5. **Fibration condition.** Why can a strict fiber model a homotopy fiber for a fibration? **Answer:** path lifting gives a deformation from path-witnessed fibers to strict fibers, up to equivalence.

### References

- Daniel Dugger, *A Primer on Homotopy Colimits* (sections on homotopy limits).
- Kerodon, *Limits and Colimits* and *Limits of Spaces*.
- nLab, *Homotopy Pullback*.
- Philip S. Hirschhorn, *Model Categories and Their Localizations*.
