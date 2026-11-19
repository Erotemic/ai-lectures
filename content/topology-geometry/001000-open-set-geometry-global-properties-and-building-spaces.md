# Open-set geometry, global properties, and building spaces

<!-- BEGIN SPOKEN LECTURE -->

# Open-set geometry, global properties, and building spaces

## Open Sets and Continuity: Geometry Without a Ruler

Imagine a rubber sheet bearing a drawing. You stretch it gently, fold it, or pull it into a curved shape without tearing or joining points that were separate. Lengths change, angles change, and circles may become distorted. Yet there are aspects of the drawing that survive: which points can be reached by continuous paths, which parts are separated, and which points remain near which other points in a purely qualitative sense.

Topology begins by asking how much mathematics can be done with this qualitative structure alone. To answer, we need a way to say what a neighborhood is, even when we have no ruler.

### Open sets on the number line

Start with the real line. An open interval from a to b contains all numbers strictly between a and b, but not the endpoints. A set U of real numbers is open if every point x in U has some positive breathing room: there is a positive epsilon such that every real number within epsilon of x is also in U.

For example, the interval from zero to one is open. At a point x strictly between zero and one, choose a positive epsilon smaller than both the distance from x to zero and the distance from x to one. The epsilon neighborhood lies entirely inside the interval. By contrast, the half-open interval including zero but excluding one is not open in the real line: the point zero has no symmetric neighborhood contained in the set.

The empty set and the entire real line are open by convention and by the definition, respectively. The empty set satisfies the breathing-room condition vacuously because it contains no counterexample point.

There are two rules worth inspecting. The union of any collection of open sets is open. Why? A point in the union belongs to at least one of the member sets, and that member gives it the necessary breathing room. The intersection of finitely many open sets is also open. For each set choose some acceptable positive radius around the point, and take the smallest of these finitely many radii.

But infinite intersections can fail. Consider the open interval centered at zero with radius one, then radius one half, then one third, and so forth. The only point that belongs to all of them is zero. The one-point set containing zero is not open in the real line. We cannot take the minimum of infinitely many positive radii and assume that minimum is still positive.

This failure explains why topology singles out arbitrary unions but only finite intersections. It is not an arbitrary asymmetry; it captures the way ordinary neighborhoods actually behave.

### The abstraction

A topology on a set X is a selected family of subsets called open sets, satisfying three axioms. The empty set and X are open. Any union of open sets is open. Every finite intersection of open sets is open. That is the entire definition.

The points of X need not be numbers. They might be functions, geometric shapes, infinite sequences, or states of a system. If we can specify which subsets should count as open and verify the axioms, we have a topological space.

Every metric, or distance function, supplies a topology. Declare a set open if each point has a sufficiently small metric ball contained in the set. Different metrics can produce the same topology, because topology remembers which neighborhoods exist rather than their exact radii. And some topological spaces cannot be described by any metric at all.

Two extreme examples clarify how much freedom the definition allows. In the discrete topology, every subset is open. A point can be isolated from every other point by the one-element open set containing it. In the indiscrete topology, only the empty set and the whole set are open. It is impossible to distinguish individual points using nontrivial open sets.

These are not two different distance scales on the same space; the indiscrete topology on a set with more than one point cannot arise from a metric, because metric spaces can separate distinct points with disjoint small balls. The topology carries actual structural information.

### Continuity without epsilon and delta

For real functions, continuity is usually explained through nearby inputs producing nearby outputs. In a topological space, we can express the same idea with open sets. A function f from X to Y is continuous if, for every open set V in Y, the set of all inputs mapped into V is open in X. That input set is called the preimage of V.

It can be useful to think of this as an experimental test. Pick any open target region. Ask which source points land in that target. A continuous map requires that the resulting source region be open. This is a statement about all target neighborhoods at once.

On metric spaces, the preimage definition is equivalent to the familiar epsilon-delta definition. To sketch one direction, suppose f satisfies epsilon-delta continuity at every point. Take an open target region V. Every source point x whose image lies in V has an output ball around f of x contained in V. Epsilon-delta continuity then supplies a source ball around x mapping into that output ball. Hence the preimage of V is open.

For the reverse direction, take any source point x and any positive target radius. The ball centered at f of x with that radius is open. Its preimage is an open set containing x, so it contains a source ball around x. That source ball maps into the target ball. We have recovered epsilon-delta continuity.

Thus topology is not inventing a different notion for familiar real functions. It is exposing the part of continuity that does not depend on numerical distances.

### Images and preimages are not interchangeable

A tempting mistake is to say a continuous function sends every open set to an open set. That is false. Take the continuous function that squares real numbers. The image of the open interval from negative one to one is the interval from zero inclusive to one exclusive. That image is not open in the real line, because it includes zero without including nearby negative numbers.

The correct continuity test concerns preimages, not images. This matters because a preimage of a union is the union of preimages, and a preimage of an intersection is the intersection of preimages, for any function whatsoever. Those set-theoretic identities cooperate perfectly with the topology axioms.

If a continuous function is also a bijection and its inverse is continuous, it is called a homeomorphism. Homeomorphic spaces have the same topological structure up to a renaming of points. A continuous bijection alone may not be a homeomorphism, because the inverse need not be continuous. That distinction becomes important when compactness enters the picture.

### Closed sets and limiting behavior

A set is closed when its complement is open. On the real line, a closed interval including its endpoints is closed. The set of all integers is closed, even though it is not an interval. The entire real line and the empty set are both open and closed. “Open” and “closed” are not mutually exclusive categories: their definitions concern neighborhoods and complements, not an everyday door that must be one or the other.

A point x lies in the closure of a set A if every open neighborhood of x meets A. Thus zero lies in the closure of the open interval from zero to one, even though it is not a member of that interval. More generally, the closure consists of all points that cannot be separated from A by an open neighborhood.

In a metric space, this can be related to sequences: x is in the closure of A if some sequence of points of A converges to x. But in an arbitrary topological space, sequences need not detect every closure point. This is a first warning that many tools familiar from real analysis silently rely on properties of metric spaces. The open-set definition works at the wider level.

### What we have deliberately forgotten

Topology does not distinguish a circle of radius one from a circle of radius one hundred. It does distinguish an interval from a circle in ways we will later make precise, and it distinguishes a connected space from two separated pieces. The first step, however, is simpler: specify the open sets, preserve them under preimages, and recognize which conclusions need no measurement of distance.

The power of an abstraction is not that it says everything. It is that it says exactly the things we can carry from one setting into another. Open sets give us a portable definition of continuity; later they will give us portable definitions of compactness and connectedness. The geometry starts here, with neighborhoods instead of a ruler.

## Compactness and Connectedness: Two Global Consequences of Open Sets

An open set is local information. It tells us that each included point comes with some neighborhood. Yet collections of open sets can encode remarkable global facts. One fact says that an infinite collection of local observations can sometimes be reduced to a finite collection without losing coverage. Another says that a space cannot be split cleanly into two nonempty open pieces.

The first is compactness. The second is connectedness. Together they explain why continuous functions on closed intervals behave so well, and why that behavior can fail when an endpoint is missing.

### Cover a space with neighborhoods

An open cover of a space X is a collection of open subsets whose union contains every point of X. The collection may be infinite. A finite subcover is a finite selection from the collection that still covers all of X.

A space is compact if every open cover has a finite subcover. Notice the quantifiers: we require this property for *every* possible open cover, not merely for a convenient family. Compactness is not a synonym for being small. It is a theorem about the way infinitely many local neighborhoods can cover the space.

Take the closed interval from zero to one with its ordinary real-line topology. It is compact. One way to see the underlying reason is through the completeness of the real numbers. Given an arbitrary open cover, consider how far to the right we can cover the interval using finitely many selected open sets. There is at least a little progress starting at zero, because some open set contains zero. Let s be the least upper bound of all the right endpoints reached by such finite coverage.

If s were less than one, choose an open set containing s. That set contains points a little to the left and a little to the right of s. A finite cover reaching sufficiently close to s, together with this one additional open set, would extend the covered interval past s. That contradicts the definition of s. Therefore the supremum must be one. A final open set containing one lets us extend finite coverage to the endpoint itself. We have produced a finite subcover of the entire interval.

The proof is a sketch of the Heine–Borel phenomenon in one dimension. It depends on the least-upper-bound property of the real numbers. In Euclidean space, a set is compact exactly when it is closed and bounded. That equivalence is special to Euclidean space and certain related settings; in a general topological space, the open-cover definition is the fundamental one.

### Missing an endpoint changes everything

Consider the interval greater than zero and at most one. We can cover it by the open sets that, for each positive integer n, contain all real numbers greater than one over n and less than two. Every positive point eventually lies in one of these sets. But any finite selection has a smallest included left threshold, so it misses points sufficiently close to zero. There is no finite subcover. The interval is not compact.

It is tempting to say the failure has no practical effect because the set is bounded and almost closed. Yet compactness is not approximate. Its consequences can disappear completely when one endpoint is removed.

Consider the function one divided by x on this half-open interval. The function is continuous everywhere in its domain, but it is unbounded as x approaches zero. On a compact interval a real-valued continuous function must be bounded and must attain its maximum and minimum. On the noncompact half-open interval, the corresponding claim fails. The topology explains why a missing point can matter more than its negligible size.

### Continuous images of compact spaces

Suppose f is continuous from a compact space X into a space Y. We claim the image f of X is compact, with the subspace topology inherited from Y. Take any open cover of f of X. Each covering open set has an open preimage in X because f is continuous. These preimages cover X. Compactness of X supplies a finite subcover, and taking the corresponding target open sets gives a finite cover of f of X.

We proved a global preservation theorem from one line of local information: preimages of open sets remain open. Nothing in the proof requires Y to have a distance function. This is why open-cover compactness is a successful topological definition.

In the real numbers, compact sets are closed and bounded. So if f maps a compact X continuously into the real line, its image is compact and therefore bounded, with maximum and minimum attained. The familiar extreme value theorem is one consequence of a broader theorem about continuous images.

There is a useful related result. A continuous bijection from a compact space X onto a Hausdorff space Y is automatically a homeomorphism. Hausdorff means distinct points can be separated by disjoint open neighborhoods; every metric space is Hausdorff. The proof uses the fact that a compact subset of a Hausdorff space is closed: the continuous bijection sends closed subsets of compact X to compact, hence closed, subsets of Y. That makes the inverse continuous.

Without compactness, the conclusion can fail. The map that sends each angle t in the half-open interval from zero inclusive to two pi exclusive to its point on the unit circle, using cosine and sine, is continuous and bijective. But the inverse cannot be continuous near the point corresponding to angle zero, because nearby points on the circle approached from one direction have angles approaching two pi rather than zero. The interval and the circle are not homeomorphic. Compactness catches the obstruction: the circle is compact and the half-open interval is not.

### Connectedness prevents a split

A topological space X is disconnected if it can be written as a union of two nonempty, disjoint open sets. Otherwise it is connected. The definition says the space cannot be separated into two pieces that are both open within the space. We do not require that two arbitrary points can be joined by a path; path connectedness is stronger in general.

Every interval in the real line is connected. To understand why, imagine an interval split into two disjoint nonempty open pieces. Pick a point in one piece and a point in the other. Travel along the numerical order between them. At some boundary between the pieces, neither side can maintain its supposed openness: the least-upper-bound property forces a point that cannot be assigned an open neighborhood staying entirely in its designated piece. A rigorous proof uses a supremum argument similar in spirit to the compactness proof.

Connectedness explains the intermediate value theorem. A continuous map sends connected spaces to connected spaces. The proof is by contradiction. If the image could be separated into disjoint nonempty open pieces, the preimages of those pieces would be disjoint, nonempty, open sets separating the domain. But a connected domain admits no such separation.

A connected subset of the real line must be an interval: if it contains two values a and b but misses some value c strictly between them, it splits into the part below c and the part above c. Therefore a continuous real-valued function on an interval takes every intermediate value between any two values it attains. This is the intermediate value theorem as a statement about connected images.

### Connected does not mean path connected

Consider the closure in the plane of the graph of sine of one over x for positive x near zero. The oscillating graph is connected, and its closure includes a vertical line segment at x equal to zero. The whole set remains connected because the closure of a connected set is connected. Yet it is not path connected: there is no continuous path inside that set from a point on the vertical segment to a point on the oscillating graph.

The point of the example is not to make the topology needlessly strange. It shows that “cannot be separated by open sets” and “can be traversed along a continuous path” are distinct claims. They coincide in many familiar regions, but they are not equivalent for arbitrary spaces.

A related distinction is local connectedness: having small connected neighborhoods. A space can be connected without being locally connected. When a theorem needs paths, neighborhoods, or differentiable curves, the precise hypothesis matters.

### Two powerful kinds of global control

Compactness says any open cover admits a finite subcover. Connectedness says no separation into two nonempty open pieces is possible. Under continuous maps, both properties survive. Their consequences are different: compactness helps guarantee extrema and finite control; connectedness helps guarantee intermediate values and the impossibility of certain partitions.

Together they illustrate why topology is more than a vocabulary for deforming pictures. Local openness produces global mathematical theorems. The conditions state exactly what is preserved, and examples with missing endpoints or oscillating curves tell us where seemingly obvious conclusions stop being valid.

## Products, Quotients, and Gluing: How to Build Spaces

A circle and a line look like different kinds of objects. Yet there is a direct construction of a circle from a closed interval: identify its two endpoints. A torus, the surface of a doughnut, can be assembled from two circles, or by identifying opposite edges of a square. These are not informal descriptions of shape. They are precise constructions of new topological spaces from old ones.

Two operations do much of the work: products, which let coordinates vary independently, and quotients, which declare selected points indistinguishable. Both have universal continuity rules that make them useful far beyond familiar pictures.

### The topology of a product

Start with topological spaces X and Y. The underlying set of their product is the set of ordered pairs, one coordinate from X and one from Y. We want each coordinate projection to be continuous. The most natural topology is generated by rectangles U times V, where U is open in X and V is open in Y.

Why rectangles? If we demand that the first coordinate lie in an open set U and the second lie in V, the permitted pairs are exactly U times V. The intersection of two such rectangles is again a rectangle, obtained by intersecting the corresponding coordinate sets. Arbitrary unions of rectangles give a topology.

The projections from the product to each factor are continuous because the inverse image of U under the first projection is U times the whole of Y. Conversely, a map into the product is continuous exactly when its two component maps into X and Y are continuous. To prove the converse, take the inverse image of a basic rectangle U times V; it is the intersection of the inverse images of U and V under the component maps, hence open.

This coordinatewise criterion makes product constructions manageable. A path into the plane is continuous precisely when its horizontal and vertical coordinates are continuous. Two circles multiplied together give a torus as a topological space. Whether we draw that torus as an embedded surface in three-dimensional space is a separate geometric decision.

### Finite and infinite products differ

For a finite product, basic open sets constrain every coordinate, with one open set per factor. In an infinite product, the *product topology* permits basic open sets that constrain only finitely many coordinates and leave all the others unrestricted.

Consider an infinite list of real numbers, viewed as a point of the product of countably many copies of the real line. A sequence converges in this product topology exactly when it converges in every fixed coordinate. For example, let e-n be the sequence whose n-th coordinate is one and every other coordinate zero. As n grows, any given coordinate eventually becomes zero. Thus e-n converges to the zero sequence in the product topology.

There is a stronger topology, sometimes called the box topology, where every coordinate may be independently constrained by an open set. In that topology, the box requiring every coordinate to lie between negative one-half and positive one-half contains the zero sequence but contains none of the e-n. So the same sequence does not converge there. Infinite products require a deliberate choice of what continuity should mean. The product topology is the one characterized by continuity of all coordinate projections with the least possible open-set structure.

### Identifying points: the quotient topology

Now begin with a space X and an equivalence relation on its points. The quotient set consists of equivalence classes. Let q send each point to its class. We declare a set U of classes open precisely when its inverse image under q is open in X. This is the quotient topology.

The definition is chosen to make q continuous and to make it as easy as possible to recognize continuous maps *out* of the quotient. Suppose f from X to another space Y is continuous and assigns the same value to equivalent points. Then f factors uniquely through the quotient: there is a map f-bar from the quotient to Y with f equal to f-bar after q. The map f-bar is continuous because the inverse image of an open set under f-bar pulls back through q to the corresponding inverse image under f, which is open in X.

The condition that f be constant on each equivalence class is essential. Without it, the proposed f-bar would assign two different values to one quotient point and would not be a function.

### Making a circle from an interval

Take the interval from zero to one. Identify its endpoints, zero and one, while keeping all other points distinct. The quotient should be a circle. To prove this, map a real t in the interval to the point on the unit circle with coordinates cosine of two pi t and sine of two pi t. This map is continuous and agrees at zero and one, so it factors through the quotient.

The induced map from the quotient to the unit circle is continuous and bijective. At this point, bijection and continuity alone do not always give a homeomorphism; a continuous inverse still needs justification. But the quotient is compact, because it is the continuous image of a compact interval. The unit circle is Hausdorff, because it is a metric space. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism. So the circle construction is fully justified.

For the torus, start with a square and identify the left edge with the right edge, and the bottom edge with the top edge. Equivalently, take one circle coordinate for each direction. We obtain the product of two circles. A continuous path can wrap around either direction, or both; those winding possibilities will become fundamental-group calculations later.

### Gluing can also produce pathological spaces

Not every quotient looks like a familiar surface. Imagine two copies of the real line. Identify their corresponding points everywhere except at the two origins, which remain distinct. The resulting space is called the line with two origins.

Any neighborhood of one origin includes points with very small nonzero coordinates. The same is true around the other origin. Once the nonzero points from the two copies are identified, any two neighborhoods of the origins intersect. The origins cannot be separated by disjoint open neighborhoods. So this quotient is not Hausdorff, even though each original real line is Hausdorff.

The example matters because it prevents a false rule: the quotient of a Hausdorff space need not be Hausdorff. Some constructions preserve compactness or connectedness because a quotient map is continuous, but separation properties require additional hypotheses.

### Universal properties as practical instructions

Product and quotient topologies are not just recipes for open sets. Each comes with an exact test for continuity. To map *into* a product, check the coordinate functions. To map *out of* a quotient, check a function on representatives and verify that it is constant on identified classes.

These two tests let us build spaces in layers. First establish what the points of a proposed object are, then decide which identifications are intended, and finally prove the maps we care about are continuous. The familiar pictures of circles and tori help intuition, but the continuity rules are what let the constructions remain valid in dimensions and settings where no picture is available.

## Separation Axioms: When Can Points and Sets Be Told Apart?

A topological space tells us which collections of points count as open. That alone does not guarantee that individual points can be distinguished by open neighborhoods. A topology can be so coarse that two different points have exactly the same neighborhoods. A quotient construction can make distinct points impossible to separate, as happens on the line with two origins.

Separation axioms organize the different ways a space can distinguish its points and closed sets. They are not simply a ladder of increasingly abstract definitions. Each one supports concrete theorems about limits, compactness, and the existence of continuous functions.

### The first distinctions

A space is T-zero if, given two distinct points, there is some open set containing one but not the other. This is the weakest of the standard point-separation conditions. It permits one point to lie in every neighborhood of another, so the distinction may work only in one direction.

A space is T-one if, for two different points, each has an open neighborhood excluding the other. Equivalently, every singleton is a closed set. A proof of that equivalence is short. If the singleton containing x is closed, its complement is open and contains every other point. Conversely, if every other point has an open neighborhood avoiding x, their union is the complement of the singleton, which is therefore open.

A space is Hausdorff, or T-two, if any two distinct points have *disjoint* open neighborhoods. This is stronger than merely finding different neighborhoods. Ordinary metric spaces are Hausdorff: given points at positive distance d, open balls of radius less than half d around each point do not intersect.

To see that the distinctions matter, consider an infinite set with the cofinite topology, where the open sets are the empty set and all sets whose complements are finite. Every singleton is closed, so the space is T-one. But any two nonempty open sets intersect, because the complement of their intersection is the union of two finite sets and cannot exhaust an infinite set. Thus the space is not Hausdorff.

### Why Hausdorff spaces matter for limits

Suppose a sequence converges to x and also to y in a Hausdorff space. If x and y were different, choose disjoint neighborhoods U of x and V of y. Eventually the sequence would have to lie in U, and eventually it would have to lie in V. Beyond the later of those two points in the sequence, it would have to lie in their empty intersection. That is impossible. Therefore a sequence in a Hausdorff space has at most one limit.

The same argument applies to nets, which generalize sequences to spaces where ordinary sequences do not detect all topological behavior. Hausdorffness is the condition needed for uniqueness of limits in that general setting.

Hausdorffness also interacts decisively with compactness. If K is a compact subset of a Hausdorff space X, then K is closed. To prove it, take any point x outside K. For each y in K, find disjoint neighborhoods U-y of y and V-y of x. The U-y cover K. Compactness provides finitely many of them. Intersect the corresponding finitely many V-y neighborhoods of x to obtain one neighborhood V disjoint from K. Every point outside K has such a neighborhood; the complement of K is open.

This proof explains a result used when we glued an interval into a circle. A continuous bijection from a compact space to a Hausdorff space must be a homeomorphism. Indeed, it sends closed subsets of the compact domain to compact subsets of the Hausdorff codomain, hence to closed subsets. So it is a closed map, and the inverse is continuous.

### Points versus closed sets

Hausdorffness separates two points. Sometimes we want to separate a point from an entire closed set. A space is regular if, given a point x outside a closed set F, there are disjoint open neighborhoods of x and F. By a common convention, T-three means regular together with T-one. Some books build T-one into the word regular, so the convention must be checked when reading a theorem.

The next condition is normality. A space is normal if two disjoint closed sets can be placed in disjoint open neighborhoods. Under the usual convention, T-four means normal together with T-one.

Every metric space is normal. One can see this without constructing disjoint balls of a fixed radius, which may not exist. Let A and B be disjoint nonempty closed sets in a metric space. Define the distance from x to A as the infimum of distances from x to points of A, and similarly for B. Because A and B are closed and disjoint, their distances from any particular point cannot both be zero. The ratio distance to A divided by the sum of distance to A and distance to B is therefore a well-defined continuous function. It equals zero on A and one on B. The sets where this ratio is less than one-third and greater than two-thirds are disjoint open neighborhoods of A and B.

The formula shows something stronger than open-set separation: a continuous real-valued function can distinguish the two closed sets. In general topology, the Urysohn lemma guarantees such functions in normal T-one spaces. It is an important bridge from topology back to analysis.

### When a topology comes from a metric

If every familiar example were metrizable, we might wonder why not simply define distances from the beginning. But not every topology arises from a metric. The cofinite topology on an infinite set is not Hausdorff and so cannot be metrizable. There are also Hausdorff topologies that do not come from any metric.

A countable base is one useful condition. A space is second countable if there is a countable family of open sets such that every open set is a union of members of that family. The real line is second countable: intervals with rational endpoints form a countable base. A discrete space with uncountably many points is not second countable, because each singleton must appear in any base, although it is metrizable using the distance zero for identical points and one for distinct points.

There is a deep theorem that links these ideas: a regular T-one space with a countable base is metrizable. This is one form of the Urysohn metrization theorem. We will not prove it from scratch here; the construction is much longer than the preceding separation arguments. Its content is that a sufficiently rich supply of separations, together with countable control of the topology, permits a metric description.

That theorem does not assert that every Hausdorff space is metrizable, or that second countability is necessary for metrizability. Our uncountable discrete space already disproves the second claim.

### Applying the tests to constructions

When we form a quotient, compactness and connectedness survive continuous images under their usual hypotheses. Hausdorffness can fail. When we want to identify a geometric quotient with a familiar metric object, the compact-to-Hausdorff theorem can restore control, provided we have an actual continuous bijection to the proposed target.

Separation axioms therefore function as proof tools. Before using unique limits, ask for Hausdorffness. Before treating compact subsets as closed, ask the same. Before separating closed sets by a continuous function, ask for normality and the appropriate point-separation convention. These conditions mark which steps in familiar Euclidean proofs remain valid when we work in a space built abstractly from open sets.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Open Sets and Continuity: Geometry Without a Ruler

**Track:** Topology and Geometry. **Background:** real-number intervals and elementary functions. **Question:** how can we speak about nearby points without assigning distances?

#### Mathematical companion (not spoken)

A topology \(\tau\subseteq\mathcal P(X)\) contains \(\varnothing,X\), is closed under arbitrary unions, and is closed under finite intersections. A continuous map \(f:(X,\tau_X)\to(Y,\tau_Y)\) obeys
\[
V\in\tau_Y\implies f^{-1}(V)\in\tau_X.
\]
On metric spaces this is equivalent to pointwise \(\varepsilon\)-\(\delta\) continuity. The open interval example shows that
\[
\bigcap_{n=1}^{\infty}(-1/n,1/n)=\{0\}
\]
need not be open. Continuous functions need not map open sets to open sets: \(f(x)=x^2\) maps \((-1,1)\) to \([0,1)\).

**Closure:** \(x\in\overline A\iff U\cap A\neq\varnothing\) for every open neighborhood \(U\) of \(x\). Sequence-based characterization is valid for metric and first-countable spaces, not every topological space.

##### Exercises with answers

1. Is \([0,1)\) open in \(\mathbb R\)? **Answer:** No; the point zero has no contained open ball.
2. Is every set continuous from a discrete domain? **Answer:** Every function from a discrete space is continuous, because every preimage is an open subset of the domain.
3. Does continuity require images of open sets to be open? **Answer:** No; squaring gives a counterexample.
4. Which subsets are simultaneously open and closed in a connected interval? **Answer:** Only the empty set and the whole interval.

##### Reading

James R. Munkres, *Topology*, sections on topological spaces and continuous functions; MIT 18.901 Introduction to Topology course and reading syllabus.

### Compactness and Connectedness: Two Global Consequences of Open Sets

**Track:** Topology and Geometry. **Background:** open sets, continuity, elementary real analysis. **Question:** how can local neighborhood conditions guarantee global results?

#### Mathematical companion (not spoken)

**Compactness:** Every open cover \(\{U_i\}_{i\in I}\) of \(X\) has a finite subcover. **Heine–Borel in \(\mathbb R^n\):** \(K\subseteq\mathbb R^n\) is compact iff closed and bounded. Outside this setting, closed and bounded need not characterize compactness.

**Continuous preservation:** If \(f:X\to Y\) is continuous and \(X\) compact, then \(f(X)\) is compact. If \(X\) connected, then \(f(X)\) is connected. In a Hausdorff space, compact subsets are closed; hence continuous bijections from compact spaces to Hausdorff spaces have continuous inverses.

**Counterexamples:** \((0,1]\) has the open cover \(\{(1/n,2)\cap(0,1]\}_{n\ge1}\) with no finite subcover. The mapping
\[
f:[0,2\pi)\to S^1,\quad f(t)=(\cos t,\sin t)
\]
is a continuous bijection but not a homeomorphism. The closure of \(\{(x,\sin(1/x)):0<x\le1\}\) is connected but not path connected.

##### Exercises with answers

1. Is the open interval \((0,1)\) compact in \(\mathbb R\)? **Answer:** No; it is not closed, and one can exhibit covers with no finite subcover.
2. Why does a continuous real function on \([0,1]\) achieve its maximum? **Answer:** The image is compact in \(\mathbb R\), so it is closed and bounded and contains its supremum.
3. Is every continuous bijection a homeomorphism? **Answer:** No; the half-open angle interval mapping to the circle is a counterexample.
4. Does connectedness always imply path connectedness? **Answer:** No; the closed topologist's sine curve is a standard counterexample.

##### Reading

Munkres, *Topology*, sections on connectedness, compactness, and quotient topology; MIT 18.901, course notes and syllabus.

### Products, Quotients, and Gluing: How to Build Spaces

**Track:** Topology and Geometry. **Background:** open sets, continuity, compactness, and connectedness. **Question:** how can we assemble spaces without choosing a distance formula?

#### Mathematical companion (not spoken)

For spaces \(X,Y\), the product topology on \(X\times Y\) has basis \(\{U\times V:U\subseteq X,V\subseteq Y\text{ open}\}\). A map \(f:Z\to X\times Y\) is continuous iff \(\pi_X\circ f\) and \(\pi_Y\circ f\) are continuous.

For a quotient map \(q:X\twoheadrightarrow X/{\sim}\),
\[
U\subseteq X/{\sim}\text{ open}\iff q^{-1}(U)\subseteq X\text{ open}.
\]
If \(f:X\to Y\) is continuous and constant on equivalence classes, there is a unique continuous \(\bar f:X/{\sim}\to Y\) such that \(f=\bar f\circ q\).

**Circle:** \([0,1]/(0\sim1)\cong S^1\), through \([t]\mapsto(\cos2\pi t,\sin2\pi t)\). Compact-to-Hausdorff continuity makes the induced bijection a homeomorphism.

**Infinite product:** the standard basis constrains only finitely many coordinates. In \(\mathbb R^{\mathbb N}\), standard basis vectors \(e_n\to0\) in the product topology but not the box topology.

##### Exercises with answers

1. When is \(f:Z\to X\times Y\) continuous? **Answer:** exactly when both coordinate maps are continuous.
2. Why does a continuous map that identifies zero and one factor through \([0,1]/(0\sim1)\)? **Answer:** it is constant on each equivalence class, meeting the quotient factorization criterion.
3. Does every quotient of a Hausdorff space remain Hausdorff? **Answer:** no; the line with two origins is a counterexample.
4. Why is \([0,1]/(0\sim1)\) compact? **Answer:** it is the continuous image of the compact interval under the quotient map.

##### Reading

James Munkres, *Topology*, second edition, product and quotient topologies; MIT OCW 18.901, topology lecture notes and readings.

### Separation Axioms: When Can Points and Sets Be Told Apart?

**Track:** Topology and Geometry. **Background:** open sets, compactness, continuity, and quotient topology. **Question:** why does a continuous bijection sometimes fail to be a homeomorphism?

#### Mathematical companion (not spoken)

Standard conventions used here:

- **T0:** distinct points are distinguished by an open set in at least one direction.
- **T1:** all singletons are closed.
- **T2 / Hausdorff:** distinct points admit disjoint open neighborhoods.
- **Regular:** every point and disjoint closed set have disjoint open neighborhoods; **T3** adds T1.
- **Normal:** every two disjoint closed sets admit disjoint open neighborhoods; **T4** adds T1.

**Compact-to-Hausdorff theorem:** a continuous bijection \(f:K\to H\) with \(K\) compact and \(H\) Hausdorff is a homeomorphism. Its inverse is continuous because \(f\) sends closed sets to closed sets.

**Metric normality witness:** for disjoint nonempty closed sets \(A,B\),
\[
h(x)=\frac{d(x,A)}{d(x,A)+d(x,B)}
\]
is continuous, \(h|_A=0\), \(h|_B=1\).

**Urysohn metrization theorem (one standard form):** every regular T1 second-countable space is metrizable. This theorem is recorded here, not proved in the spoken lecture.

##### Exercises with answers

1. Is an infinite set with the cofinite topology T1? **Answer:** yes, every singleton is closed.
2. Is that topology Hausdorff? **Answer:** no, any two nonempty open sets intersect.
3. Why are compact subsets of Hausdorff spaces closed? **Answer:** separate an external point from each compact-set point and take a finite subcover.
4. Does metrizability imply second countability? **Answer:** no; an uncountable discrete metric space is a counterexample.

##### Reading

Munkres, *Topology*, second edition, countability and separation axioms; MIT OCW 18.901, notes on Hausdorff spaces, regularity, normality, and metrization.
