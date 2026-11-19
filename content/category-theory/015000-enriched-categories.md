# 015000 — Enriched Categories: How Distance Can Be Composition

**Track:** An Introduction to Category Theory. **Background:** ordinary categories and composition, ordered sets, triangle inequalities. **Theme:** categories whose hom-data have values other than sets of arrows.

<!-- BEGIN SPOKEN LECTURE -->

# Enriched Categories: How Distance Can Be Composition

A train ticket from one city to another takes forty minutes. A connection from the second city to a third takes twenty-five. Even without knowing the fastest route between the first and third cities, we know something: the fastest available journey cannot take longer than sixty-five minutes if we can make those two connections. We can express this with the triangle inequality. But there is another way to hear the statement. Journeys can be composed; the cost of a composite journey is controlled by the costs of its parts.

That observation leads to a surprising version of category theory. In the categories introduced earlier, two objects have a collection of arrows between them, and composition takes two arrows with matching endpoints and produces another arrow. Here we are going to retain the objects and the idea of composition, but replace each collection of arrows by a single number measuring how difficult it is to pass from one object to the other. The number might be a travel time, a directed cost, or a distance. Ordinary metric geometry will become an example of a broader categorical structure.

The essential question is not whether a distance is secretly a function. It is what has to be true about the values assigned to pairs of objects for composition and identity to make sense. We'll derive those conditions, calculate them on a small network, and see where the analogy ends.

## A network we can calculate in our heads

Consider three stations: Ash, Birch, and Cedar. The directed travel times from Ash to Birch and from Birch to Cedar are four and seven minutes. A direct route from Ash to Cedar takes fifteen minutes. We can save time by changing at Birch. If we represent the best available time between each ordered pair of stations, the distance from Ash to Cedar is at most eleven, because four plus seven makes eleven.

Notice the direction. If the route from Cedar back to Birch takes twelve minutes, that tells us nothing directly about the time from Birch to Cedar. Travel-time systems can be asymmetric. A one-way street, a steep hill, or a river crossing can make a journey easier in one direction than in the other. We can also have no route at all, which we'll represent by infinity.

Let us use three stations with a complete little table, measured in minutes. From Ash to Birch the best time is four; from Birch to Cedar it is seven; from Ash to Cedar it is eleven. For return trips, let Cedar to Birch be twelve, Birch to Ash be five, and Cedar to Ash be seventeen. The values have been chosen so the paths through the intermediate station never undercut the stated best times. Going from a station to itself costs zero because doing nothing is an available route.

We can check one inequality: going from Cedar to Ash by way of Birch takes twelve plus five, exactly seventeen. So the direct best-time value of seventeen is consistent. Going from Ash to Cedar by way of Birch takes four plus seven, exactly eleven. These equations are not just arithmetic coincidences; they are the equations that make path composition compatible with the numbers.

## The ordinary categorical pattern

In an ordinary category, every object X has an identity arrow. If there is an arrow from X to Y and another from Y to Z, their composite goes from X to Z. Associativity says that when three arrows form a chain, the order of grouping does not change the result.

Our network shares the organization of the endpoints, but its measurement behaves differently. We do not ask for an explicit composite arrow in a set. We ask the number assigned to X and Z to be no greater than the sum of the numbers for X to Y and Y to Z. That is the triangle inequality. And an identity journey has cost zero. Addition is associative, which takes care of the coherence that ordinarily appears as associativity of arrow composition.

To turn this observation into a formal definition, category theorists use something called enrichment. An enriched category takes its hom-data from another mathematical environment, rather than from ordinary sets. That environment must provide a way to combine hom-data, often called a tensor product, and an object that acts as a unit. The environment itself is a monoidal category.

We have already studied monoidal categories with examples such as pairs of sets and tensor products of vector spaces. Here the monoidal category will be stranger but simpler. Its objects are the extended nonnegative real numbers, including infinity. We regard the numbers as a partially ordered category, but with the order reversed. There is an arrow from the number r to the number s precisely when r is greater than or equal to s. Combining two numbers means adding them. The monoidal unit is zero.

Why reverse the order? Because a journey made of two parts has cost r plus s, and the best cost for its endpoints should be less than or equal to that sum. In the reversed-order category, that inequality becomes exactly the arrow needed for composition: from r plus s to the direct hom-value. If we had kept the ordinary order, the categorical composition law would require the wrong inequality.

## The definition hiding in the inequality

A category enriched in these extended distances consists of objects and, for every ordered pair X and Y, a number d of X to Y. The composition condition is that d of X to Y plus d of Y to Z is at least d of X to Z. The identity condition is that zero is at least d of X to X. Because all the numbers are nonnegative, the second condition forces every self-distance to equal zero.

You may recognize both conditions as two of the familiar metric axioms. But where is symmetry? Where is the requirement that zero distance implies the points are equal? Neither follows from categorical composition and identity. In this setting we are allowed to have directed distances, and we may even have distinct objects with zero cost between them.

These are often called generalized metric spaces, or Lawvere metric spaces. Familiar ordinary metric spaces are examples, but the categorical definition accommodates more. For instance, two different names for the same location may have zero travel time in both directions. The enriched structure records their indistinguishability by distance without insisting that the names be identical objects. If we want the stronger metric condition, we must add it.

There's an important limitation to the metaphor. We are assigning the cost of the *best* route, not a record of each particular route. The number eleven from Ash to Cedar does not tell us whether it came from a direct train, a transfer, or several alternative routes. If we need individual itineraries, an ordinary category of paths may be a better starting point. Enrichment by a single cost deliberately forgets route details while preserving a compositional inequality.

## Infinity and zero are informative edge cases

One reason to use extended nonnegative reals is that infinity has a clear meaning: there may be no admissible journey from X to Y. If there is a finite journey from X through Z to Y, then the triangle inequality forces the best distance from X to Y to be finite as well. A distance table assigning infinity to that pair would contradict the existence of the finite composite path.

Consider a directed graph with a one-way connection from Ash to Birch and no way back. We may have a finite distance from Ash to Birch and an infinite distance from Birch to Ash. The axioms allow this without any special exception. Composing a finite route with an infinite route yields infinity as an upper bound, which gives no new numerical information about the destination pair. We should treat infinity as an extended value, not perform ordinary real-number subtraction with it.

Zero has its own subtleties. In an ordinary metric space, zero distance in both directions implies two points are the same. Here it need not. Define X and Y as distinct records and set both directed distances to zero. The triangle inequalities still hold. In the enriched sense, the points may be indistinguishable even though their underlying labels differ. This resembles a familiar categorical theme: objects can be equivalent by the structure under study without being equal as raw names.

These examples are useful checks when designing a model. Does a missing edge mean infinite *direct* cost, or infinite best-path distance? Does zero mean truly identical resources, or merely that moving between two states incurs no cost? The mathematical structure faithfully records the answers we choose; it cannot decide them for us.


## Shortest paths from repeated composition

Suppose we initially know only the directed edges of a road graph. We assign each edge its cost and put infinity where no edge is known. Then we compute the best price of reaching one vertex from another by allowing intermediate vertices. Every time we discover a path X to Y to Z, we obtain an upper bound on the shortest-path cost from X to Z. We keep whichever upper bound is smaller.

In a finite graph with nonnegative edge weights, repeating this operation produces the shortest-path distances. An algorithm such as Floyd–Warshall formalizes the repeated comparison: the best cost with a new intermediate vertex is the smaller of the old cost and a cost obtained by going through that vertex. Addition combines successive journeys, and minimum chooses between alternatives.

These are two different operations. Addition expresses sequential composition. Minimum expresses choice among competing routes. In our enriched-category definition the final distance table already satisfies the triangle inequalities. The shortest-path algorithm can be understood as constructing such a table from raw edge information. You do not need category theory to implement the algorithm, but the categorical viewpoint identifies the invariant that the completed calculation must satisfy.

Try a miniature case. Ash to Birch costs four. Birch to Cedar costs seven. Ash to Cedar has a direct edge of fifteen. Once paths through Birch are allowed, the new best time from Ash to Cedar is the minimum of fifteen and four plus seven. That is eleven. Repeat for all triples, and the network's best-time table becomes closed under the triangle inequality.

The useful mathematical insight is that an admissible composite path never gives a tighter lower bound on the endpoint distance; it gives an upper bound on the best distance. A shortest-path proof has two jobs: it must use the triangle inequality in the direction of an achievable journey, and it must establish that the algorithm considered enough journeys to attain the minimum.

## What is a functor between these spaces?

An ordinary functor sends objects to objects and arrows to arrows while preserving identities and composition. For enriched categories, the appropriate preservation condition is expressed using the base monoidal category. In the distance setting, a functor f from one generalized metric space to another must satisfy a straightforward numerical inequality: the distance between the images f of X and f of Y cannot exceed the original distance between X and Y.

That is a nonexpansive map, also called a one-Lipschitz map. A mapping is allowed to bring points closer together; it may not stretch any directed distance. Notice that we still do not require symmetry or the separation of points. The condition must be checked for ordered pairs, not merely unordered pairs.

Here's a concrete example. Take the real line with its ordinary distance. Map every number x to one half of x. Two points originally three units apart become one and a half units apart. This map is nonexpansive. The map sending x to twice x is generally not nonexpansive: two points one unit apart become two units apart.

A constant map is always nonexpansive, since the images have distance zero from each other. That may feel too permissive for something called structure preservation, but it reveals what the structure actually says. It places an upper bound on how much the map may separate points. It does not demand that all distinctions be preserved. The same is true in ordinary category theory: a functor can identify different objects or arrows.

In the directed travel network, a map that groups nearby stations into zones can be nonexpansive if the distances assigned to the zones are no larger than the original directed distances. If some zones are assigned a longer cost, the condition fails. This gives a direct test for whether a coarse-graining preserves the intended quantitative structure.

## How to hear enriched Yoneda

One of the great ideas of category theory is that an object can be studied through its relationships to other objects. The Yoneda lemma makes that precise for ordinary categories. Distance gives us an accessible version of the same idea.

Fix a point A in an ordinary symmetric metric space. Build its distance profile: for every other point Z, record the number d of A to Z. This replaces the single point A by an entire function of Z. Two points with different distances to some landmark have different profiles. In fact, if we use all possible landmarks, the profiles recover the original distances exactly.

Here is the calculation. For any two points A and B, the triangle inequality tells us that the absolute difference between d of A to Z and d of B to Z is at most d of A to B, for every Z. Taking the largest possible absolute difference still gives at most d of A to B. But choose Z to be B. Then the two profile values are d of A to B and zero, so the absolute difference is exactly d of A to B. Thus the largest difference of the two profiles equals the original distance.

We've represented points by the functions describing their distances to all other points, and the representation preserves distance. The exact enriched Yoneda lemma uses a suitable enriched functor category and the structure of the base of enrichment. Our calculation is an elementary symmetric-metric shadow of that theorem. It is instructive because the entire argument is one application of the triangle inequality and one carefully chosen landmark.

The warning is equally useful. For an asymmetric generalized metric space, blindly replacing the enriched formula by a symmetric absolute-value supremum can lose the direction of the data. The correct enriched hom in a functor space must respect the order and residual operations of the base. Before generalizing a familiar formula, we should ask which structure made it valid.

## What enrichment adds beyond metrics

The distance example invites us to vary the environment containing the hom-values. In ordinary categories, each hom is a set. For order-enriched categories, each hom can itself be an ordered set of arrows, and composition must respect that order. For categories enriched in vector spaces, the homs are vector spaces and composition is bilinear. These examples behave quite differently, but the same organizational pattern remains: hom-objects, a monoidal product for composing, and a unit for identities.

In a vector-space-enriched category, adding two arrows can make sense because they live in a vector space. Ordinary categories do not generally allow such addition. In metric enrichment, comparing two hom-values with an order is fundamental. The important lesson is that we are choosing the algebra carried by relationships. We are not merely attaching a decorative number to each arrow.

This can matter in software and applied mathematics. A computation might carry an error bound, a process might consume a resource, or a path might incur a cost. If those quantities compose associatively and have a suitable identity, enrichment may reveal an algebra that can be reasoned about at the level of interfaces. But not every annotation gives an enriched category. A proposed combination rule must genuinely satisfy the monoidal laws, and its interaction with hom-data must satisfy the enrichment axioms.

## The original insight and its historical setting

F. William Lawvere's work on metric spaces and generalized logic in the early nineteen seventies showed how the axioms of distance could be read categorically by choosing extended nonnegative reals with reversed order and addition. The result was memorable because the category-theoretic language, which seemed suited to abstract algebra, also explained a familiar inequality from geometry. It formed part of a larger investigation of how mathematical structures can be understood through their internal logic and composition rules.

There are broader historical connections to enriched categories in algebra and topology, including developments associated with Samuel Eilenberg, G. Max Kelly, and others. The metric example is especially welcoming because it requires no theory of tensor products or higher algebra to check the main axioms. The difficult abstraction has been reduced to a calculation a listener can carry out on a three-station network.

We should be careful about claiming that this discovery makes every metric problem into an easy category-theory problem. Metric geometry has many properties that do not follow from the enriched-category axioms: compactness, completeness, curvature, and the behavior of limits require further definitions and theorems. Enrichment gives us a common grammar for composition; it does not replace specialized geometry.

## Returning to the train network

Return to Ash, Birch, and Cedar. The number four from Ash to Birch combines with seven from Birch to Cedar. Addition says the composed journey has cost eleven. The shortest time from Ash to Cedar must be no more than eleven. A zero-length stay at Ash acts like an identity. Any remapping of stations that never increases the directed travel times is a functor for this enrichment.

From these everyday statements, we have recovered the definition of a Lawvere metric space and the meaning of its structure-preserving maps. We have also seen why reversing the order is essential, why symmetry is optional, and how the distance to every landmark can represent a point in a symmetric metric space.

The larger idea is that composition can be valued in different mathematical worlds. Set-valued homs produce familiar categories of arrows. Distance-valued homs produce generalized metrics. Ordered or linear homs produce other structures. The value of enrichment lies in showing exactly which features of composition survive these changes, and exactly which familiar features we must stop assuming.


<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(\mathcal V=([0,\infty],\ge,+,0)\), the symmetric monoidal poset of extended nonnegative reals in the **reversed numerical order**. A \(\mathcal V\)-category consists of \(X\) and hom-values \(d(x,y)\in[0,\infty]\) subject to
\[
0\ge d(x,x),\qquad d(x,y)+d(y,z)\ge d(x,z).
\]
Nonnegativity forces \(d(x,x)=0\). Symmetry and separatedness are **not** axioms. For a \(\mathcal V\)-functor \(f:X\to Y\):
\[
d_X(x,x')\ge d_Y(fx,fx').
\]
For ordinary symmetric metric spaces, \(\Phi(x)(z)=d(x,z)\) satisfies
\[
\sup_z |\Phi(x)(z)-\Phi(y)(z)|=d(x,y).
\]
The inequality is the reverse triangle inequality; equality is witnessed at \(z=y\). This formula is a symmetric-metric special case, not a license to substitute symmetric sup distance into the general directed enriched Yoneda theorem.

**Shortest-path closure.** For nonnegative edge weights, \(D^{(k)}_{ij}=\min(D^{(k-1)}_{ij}, D^{(k-1)}_{ik}+D^{(k-1)}_{kj})\), and the completed distances satisfy the enrichment inequalities. Deriving the completed table needs an argument that each intermediate vertex has been admitted.

### Exercises with answers

1. **Exercise:** A route \(a\to b\) costs 3 and \(b\to c\) costs 8. May \(d(a,c)=12\) in a Lawvere metric space? **Answer:** No: \(d(a,c)\le 11\).
2. **Exercise:** Must \(d(a,b)=d(b,a)\)? **Answer:** No. Enrichment does not require symmetry.
3. **Exercise:** Is \(x\mapsto 3x\) on \(\mathbb R\) nonexpansive? **Answer:** No unless its domain metric is changed; it expands distances by three.
4. **Exercise:** Why does \(z=y\) prove equality in the symmetric distance-profile identity? **Answer:** The difference becomes \(|d(x,y)-d(y,y)|=d(x,y)\).

### References

- F. W. Lawvere, “Metric Spaces, Generalized Logic, and Closed Categories” (1973; reprint 2002), https://www.tac.mta.ca/tac/reprints/articles/1/tr1abs.html
- Brendan Fong and David I. Spivak, *Seven Sketches in Compositionality*, https://arxiv.org/abs/1803.05316
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/files/context.pdf
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
