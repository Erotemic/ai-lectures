# 020000 — Enriched Yoneda: Recovering Distance from Every Point of View

**Track:** An Introduction to Category Theory. **Background:** metric spaces, enriched categories, functors, and Yoneda, developed again from numerical examples. **Theme:** an enriched object is determined by its pattern of relationships, with hom-objects carrying quantitative structure.

<!-- BEGIN SPOKEN LECTURE -->

# Enriched Yoneda: Recovering Distance from Every Point of View

Suppose I give you a map with the place names erased. I will not tell you where a particular station sits, but I will give you its distances from every other station. How much have I told you? If the distances are genuine metric distances, including the distance from a station to itself, I have given you enough to recover how far that station is from any other one. In fact, there is a precise way to compare entire tables of distances that returns the original distance between two stations.

This elementary observation is one entry point to an important theorem called enriched Yoneda. Ordinary Yoneda says that a mathematical object can be understood through all the arrows leading into it. Enriched Yoneda retains that principle when the relationships between objects are themselves numbers, vector spaces, ordered quantities, or other objects carrying additional mathematical structure.

Our running example will be a railway network. We will first reconstruct distance by comparing profiles, then examine a directed network, where the distance from A to B need not equal the distance from B to A. Only after seeing both cases will we introduce the enriched form of Yoneda and explain what the theorem really states.

## A three-station calculation

Imagine three stations called Ash, Birch, and Cedar. The distance from Ash to Birch is two units. Birch to Cedar is three units. Ash to Cedar is five units. Assume we have a symmetric metric, so distances are the same in both directions and each station is distance zero from itself.

Write a station's profile as a list of its distances from Ash, Birch, and Cedar, in that order. Ash has profile zero, two, five. Birch has profile two, zero, three. Cedar has profile five, three, zero. These are three vectors of length three, but we are not claiming the railway has been physically embedded in three-dimensional space. The coordinates are measurements against named landmarks.

How far apart are the profiles for Ash and Birch? Compare corresponding entries. The first entries differ by two. The second entries differ by two. The third entries differ by two. The largest absolute difference is two, exactly the distance from Ash to Birch.

For Ash and Cedar, the first entries differ by five, the second by one, and the third by five. The largest difference is five, exactly their distance. For Birch and Cedar, the differences are three, three, and three, so the largest is three. Our table of profiles reproduces every original distance.

Why does that happen? The triangle inequality tells us that for any landmark z, the difference between its distance to a and its distance to b can be no larger than the distance between a and b. That proves every coordinate difference is bounded above by the original distance. Then choose the landmark z to be a itself. Its distance to a is zero and its distance to b is precisely the distance we wish to recover. One coordinate attains the upper bound.

The result does not depend on the special numbers two, three, and five. For any symmetric metric space, the map sending a point to its list of distances from all points is distance preserving when the lists are compared by their largest absolute coordinate difference. This is a form of the distance-profile or Kuratowski embedding.

## Why this is related to Yoneda

In an ordinary category, an object a can be represented by the assignment that sends any test object z to the set of arrows from z to a. That assignment is called a representable presheaf. Yoneda tells us that natural transformations from this representable into another presheaf are determined by a single value at a, namely what happens to the identity arrow of a.

For a metric space treated as an enriched category, the relationship from z to a is the number d of z and a. So the representable presheaf associated with a looks exactly like the distance profile we just calculated. Instead of a set of arrows from every test point, we have a distance from every test point. The format of the record changes, but the idea of probing an object through all its relationships remains.

The numerical embedding shows that a point can be recovered as a relational profile up to the distinctions recognized by the metric. The categorical theorem makes a more general statement: the space of structure-respecting comparisons from the representable profile of a to any enriched presheaf F is itself equivalent to the value of F at a. It is a statement about every appropriate F, not only about comparing one distance profile with another.

That difference matters. One might hear the profile calculation and conclude that enriched Yoneda is just a clever way of putting metric spaces into a function space. The embedding is one consequence. The full lemma identifies a universal correspondence between how profiles act as tests and how presheaves assign values to points.

## Remembering the reversed order

A Lawvere metric space can be described as a category enriched over the extended nonnegative reals. Here composition is addition, and the monoidal unit is zero. The order, however, is reversed from the usual numerical order. What is called larger in the enrichment order is numerically smaller.

Why reverse it? If a route goes from Ash to Birch at cost two and from Birch to Cedar at cost three, the direct shortest-path distance from Ash to Cedar is at most five. Category composition requires the composed cost to provide a morphism into the direct hom-value in the enriching order. Under the reversed numerical order, that requirement is exactly the triangle inequality.

The identity law says the zero cost of remaining at a station must compare appropriately with the distance from the station to itself. Nonnegativity then forces that self-distance to be zero. The structure does not force distances in opposite directions to coincide, nor does it force distinct points to have positive distance apart. Those are additional properties when we need them.

This enriched viewpoint is not merely a relabeling of the same numbers. It tells us what an enriched functor must preserve. A map of metric spaces is an enriched functor precisely when it is nonexpansive: the distance between the images is no greater than the original distance. The same change in perspective will determine what a presheaf is and how to compare two presheaves.

## A directed network that refuses symmetry

Consider just two towns, Ash and Birch. Traveling from Ash to Birch takes two hours, but returning from Birch to Ash takes five. Each town has a zero-hour route to itself. This is a valid generalized metric: the triangle inequalities hold, but symmetry fails.

There are two distance profiles. For a destination a, record the cost to reach a from every possible starting point. Ash's profile is zero from Ash and five from Birch. Birch's profile is two from Ash and zero from Birch. If we took the largest absolute coordinate difference, we would get five. That does not recover the forward distance from Ash to Birch, which is two. The absolute-value rule has erased direction.

We need an asymmetric way to compare profiles. Given one profile P and another Q, look at the amount by which Q exceeds P at each starting point. Ignore negative differences; take the largest positive difference. For the profile of Ash and the profile of Birch, the changes are plus two at Ash and minus five at Birch. The largest positive change is two. We have recovered the travel time from Ash to Birch.

Reverse the comparison. Now Birch's profile is P and Ash's is Q. The differences are minus two at Ash and plus five at Birch. The largest positive change is five, the return travel time. The asymmetry of the comparison preserves the asymmetry of the network.

This example tells us why the enriched formula cannot be replaced by an ordinary symmetric sup norm. The enriching world of extended nonnegative distances has its own internal hom, a directed residual operation. When distances are finite, that residual is the positive part of the difference between the target and source numbers. The correct function-space distance is the supremum of those directed residuals.

## Recovering every directed distance

We can prove the general directed statement with the same two-part argument as before, but without absolute values. Let a and b be any points of a Lawvere metric space. For each test point z, compare the distance from z to b with the distance from z to a. The triangle inequality says that the first distance can exceed the second by no more than d from a to b. Thus every positive coordinate excess is bounded by d of a and b.

At the test point z equal to a, the distance to a is zero and the distance to b is exactly d of a and b. So that test point realizes the bound. Therefore the greatest directed excess between the two profiles equals the original directed distance from a to b.

If some distances are infinite, careless expressions such as infinity minus infinity stop being meaningful. The exact categorical formulation uses residuation, defined by a universal inequality rather than naive subtraction. In finite examples we can use truncated subtraction safely; in the extended case the residual notation keeps the theorem correct without inventing an arithmetic value for an undefined difference.

We have obtained an isometric embedding in the generalized, asymmetric sense. Sending a point to its representable distance profile preserves the directed distance from any point a to any point b. If two distinct points have zero distance in both directions, the embedding need not distinguish them as separate underlying labels. It distinguishes them to the extent allowed by the generalized metric structure.

## What counts as a metric presheaf?

A list of arbitrary numbers is not automatically a valid enriched presheaf. Think of a function F assigning a nonnegative cost to each town. To behave as a presheaf for the metric enrichment, those numbers must satisfy a compatibility inequality. For any x and y, the cost at x can be no more than the travel cost from x to y plus the cost at y.

For example, let F of Ash be four and F of Birch be three in our directed two-town network. Ash to Birch costs two, so four is at most two plus three. Birch to Ash costs five, so three is at most five plus four. Both conditions hold. F is compatible with the travel network. But if we assigned F of Ash to be nine and F of Birch to be one, then nine would exceed two plus one. The assignment would violate the compatibility demanded by the network.

There is a useful interpretation. F of x may represent a cost-to-go estimate for a task, with the rule that moving from x to y and then paying F of y must be no cheaper than the estimate F of x. The inequality is familiar from shortest-path reasoning and admissible cost-to-go functions, although the exact interpretation depends on whether F gives an upper bound, lower bound, or a feasible potential in the application.

Representable profiles satisfy the condition automatically. If F is the distance to a fixed destination a, the required inequality is exactly the triangle inequality with endpoint a. So the most important examples of metric presheaves arise from the geometry itself, rather than being imposed from outside.

## The full Yoneda calculation

Now compare a representable profile associated with point a to an arbitrary compatible function F. The enriched function-space distance is the greatest directed excess of F over the representable profile. At test point z, compare F of z with d of z and a. The presheaf inequality says F of z is at most d of z and a plus F of a. Therefore every directed excess is at most F of a.

But at z equal to a, the distance from a to itself is zero. The excess is exactly F of a. The greatest excess is therefore F of a. We have proved the metric version of the enriched Yoneda lemma: the enriched hom from the representable profile of a to F is precisely the value F assigns to a.

This is more informative than the isometric embedding alone. If we put F equal to another representable profile, we recover the directed distance from a to b. But we may choose F to be any compatible cost-to-go function, not merely a profile of an existing destination. The representable profile of a acts like an evaluation probe: comparing it to F returns F at a.

Notice that the proof is not mysterious once the types are clear. One inequality comes from the presheaf compatibility condition. The reverse inequality comes from testing at the identity point. That is the same strategy as ordinary Yoneda, where a natural transformation is determined by what it does to the identity arrow. In the metric setting, identity is represented by zero self-distance.

## General enrichment beyond numbers

The theorem is called enriched Yoneda because distances are only one choice of enriching category. Instead of a set of arrows, each pair of objects might carry an abelian group, a vector space, or another object in a suitable monoidal category. Composition must then be a morphism out of the tensor product of the two hom-objects, and identities must come from the tensor unit.

For the general enriched Yoneda theorem, the enriching category needs enough structure to form internal homs and enriched presheaf hom-objects, with the usual size and completeness assumptions. These conditions are mathematical hypotheses, not administrative details. Without the relevant internal hom or end, the expression one writes for the comparison of two presheaves may not exist.

When those conditions hold, the enriched hom-object of natural transformations from the representable at a to F is isomorphic, inside the enriching category, to F of a. In a set-enriched world, this is a bijection of sets. In a metric-enriched world, it is an equality of generalized distance values. In a linear setting, it can be an isomorphism of vector spaces or modules, with suitable enrichment.

This provides a powerful criterion for selecting categorical models. Ask what kind of relationship you need to preserve. If the relationship is merely the existence of an arrow, one setting may suffice. If it has a quantitative cost, the enriching category must encode the arithmetic of those costs. If it is linear, the hom-objects must carry the linear structure. Yoneda then respects the type of evidence you have chosen rather than reducing everything to an unstructured set.

## How much information is enough?

Our three-station example used every station as a landmark. Is that necessary? Sometimes a small collection of landmarks distinguishes all points, and then a finite vector of distances is sufficient to identify them. But a set of landmarks that distinguishes points does not necessarily reproduce all pairwise distances under the same sup-distance formula.

For instance, suppose the only landmark in the three-station line is Birch. Then Ash's one-coordinate profile is two and Cedar's is three. Their profile difference is one, even though the distance from Ash to Cedar is five. The triangle inequality still guarantees that profile differences never overestimate distance, but the chosen landmark set lacks a witness that attains the full distance for that pair.

With all landmarks available, testing at a or b recovers equality. With only selected landmarks, one generally gets a nonexpansive map into a coordinate space, not an isometric embedding. If the selected landmarks cover the space densely, extra assumptions may give quantitative approximation bounds. Those bounds are separate theorems and depend on the geometry and the coverage of the landmark set.

This limitation is useful for thinking about representation learning. A finite feature vector can preserve some relationships while hiding others. The Yoneda principle says that the complete pattern of relationships determines the original object up to the equivalences in the category. It does not say that any arbitrary compressed selection of features retains all of that information.

## A second check with a new cost profile

We can test the full lemma on a presheaf that is not obviously the profile of either destination. Return to the directed two-town network, with two hours from Ash to Birch and five hours back. Let F of Ash be four and F of Birch be three. Both presheaf inequalities hold, as we checked earlier. Take the representable profile of Ash, which has values zero at Ash and five at Birch.

At Ash, F exceeds that profile by four. At Birch, F of Birch is three and the profile is five, so there is no positive excess. The directed comparison from the Ash profile to F is four. This is exactly F of Ash, as Yoneda predicts. Now use the representable profile of Birch, with values two at Ash and zero at Birch. At Ash the excess is two, while at Birch it is three. The greatest excess is three, exactly F of Birch.

This gives us a test of the theorem that is different from comparing two representable profiles. Neither calculation asked where F came from, only whether its values satisfied the presheaf inequalities. That is the real force of the universal statement. The identity point supplies an exact evaluation, and the compatibility conditions guarantee that no other point can give a larger result.

It is also worth checking the variance. We are representing a destination a using distances **to** a from every test point. The variable test point enters contravariantly, as a presheaf variable. If instead we decided to record distances **from** a to every target, we would be constructing the corresponding covariant representation, and the directed order of the recovered distance could reverse. In a symmetric metric this distinction disappears numerically, which is precisely why starting only with symmetric examples can conceal a categorical type error.

## The result we can now justify

Representing an object by all of its incoming relationships is faithful to the category's structure. For a symmetric metric, that representation is a vector of distances whose sup-distance reproduces the original metric. For a directed generalized metric, the correct comparison is directed residuation, and it reproduces each ordered distance. For any compatible enriched presheaf F, comparison with the representable at a evaluates F at a.

The proof depends on two simple ideas: compatibility gives the upper bound, and an identity supplies the exact witness. Enriched Yoneda is the general statement that these ideas survive when the relationships carry structure more substantial than mere membership in a set. It is a precise explanation of how an object can be understood through the ways other objects relate to it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

For \(\mathcal V=([0,\infty],\ge,+,0)\), internal hom is the residual
\[
[r,s]=\inf\{t\ge0:s\le r+t\},
\]
where the infimum is in the **ordinary numeric** order. For finite \(r,s\), this equals \((s-r)_+=\max(s-r,0)\). For \(\mathcal V\)-presheaves \(F,G:X^{op}\to\mathcal V\), the enriched hom is
\[
[F,G]=\sup_{z\in X}[F(z),G(z)]
\]
in the ordinary numeric order. A presheaf \(F\) satisfies \(F(x)\le d(x,y)+F(y)\) for all \(x,y\). The representable \(y(a)(z)=d(z,a)\) satisfies this by the triangle inequality.

**Enriched Yoneda in the Lawvere case:**
\[
[y(a),F]=F(a),\qquad [y(a),y(b)]=d(a,b).
\]
For finite values, \([y(a),F]=\sup_z(F(z)-d(z,a))_+\le F(a)\) by presheaf compatibility; choosing \(z=a\) gives the reverse inequality. The enriched Yoneda embedding preserves all directed hom-values, without requiring symmetry or separation.

**Symmetric metric special case:** for \(\phi_a(z)=d(z,a)\),
\[
\sup_z|\phi_a(z)-\phi_b(z)|=d(a,b)
\]
by the reverse triangle inequality and \(z=a\). This absolute-value statement is not the general directed formula.

**Three-station example:** positions \(A=0,B=2,C=5\) give profiles \(y(A)=(0,2,5)\), \(y(B)=(2,0,3)\), \(y(C)=(5,3,0)\). **Directed example:** \(d(A,B)=2\), \(d(B,A)=5\), \(y(A)=(0,5)\), \(y(B)=(2,0)\); the directed residual sup gives 2 one way and 5 the other.

### Exercises with answers

1. **Exercise:** Why can no profile coordinate difference exceed \(d(a,b)\) in a symmetric metric? **Answer:** The reverse triangle inequality.
2. **Exercise:** Which coordinate attains equality? **Answer:** The coordinate indexed by \(a\), since \(d(a,a)=0\).
3. **Exercise:** With directed distances \(d(A,B)=2\) and \(d(B,A)=5\), what is \([y(A),y(B)]\)? **Answer:** 2, whereas \([y(B),y(A)]=5\).
4. **Exercise:** What is missing if we keep only one landmark at Birch in the 0–2–5 line? **Answer:** The embedding no longer reproduces \(d(A,C)=5\); its one-coordinate distance is only 1.

### References

- F. William Lawvere, *Metric Spaces, Generalized Logic, and Closed Categories* (1973), https://www.tac.mta.ca/tac/reprints/articles/1/tr1abs.html
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- G. Tendas, *Enriched Categories: Theory and Examples*, https://gtendas.github.io/pdfs/ECTE.pdf
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
