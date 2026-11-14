# 017000 — Kan Extensions: Extending a Diagram Without Guesswork

**Track:** An Introduction to Category Theory. **Background:** functors, natural transformations, limits and colimits, adjunctions. **Theme:** universal ways to extend indexed data along a functor.

<!-- BEGIN SPOKEN LECTURE -->

# Kan Extensions: Extending a Diagram Without Guesswork

A research group has two kinds of data. One collection describes measurements taken at individual stations. Another collection describes combined regions. At first, measurements exist only for the stations. The group now wants to extend its assignment to the larger network of stations and regions, preserving every relation that was already recorded. What should the data attached to a combined region be?

If two stations contribute independent observations, perhaps we should keep both sets of observations, tagged by their origins. If two observations are already related by a transition, perhaps they should be identified. If we're instead asking for every possible choice that remains compatible with existing measurements, a product or a limit might be appropriate. The answer depends on the arrows in the indexing diagram and on what the extension is required to preserve.

Category theory provides two systematic constructions for this problem. They are called left and right Kan extensions. They are general enough to recover ordinary colimits and limits, but their starting point is quite practical: how can a functor defined on one indexing category be extended along a map of indexing categories, without making arbitrary extra choices?

We'll work through a two-source example, then state the universal properties. The key will be to keep three categories and functors straight rather than drowning in a diagram of unnamed arrows.

## Two independent sources, one new destination

Begin with a category A containing two unrelated objects, West and East. There are only identity arrows. Give West a set of two observations, a and b. Give East a set containing one observation, c. This is a functor F from A to Set, but because A has no nonidentity arrows, F is simply the choice of those two sets.

Now build a larger category B. Keep West and East, and add a new object called Archive. Put an arrow from West to Archive and an arrow from East to Archive. There are no arrows between West and East. The inclusion of A in B will be called K.

We want to define a new functor on B that agrees with F as much as possible. What must its set at Archive contain? If every observation is to be admitted without identifying independent sources, a natural answer is a disjoint union: tagged West a, West b, and East c. The two arrows into Archive are the corresponding injections.

This construction has an important property. Suppose someone proposes a different archive H, and gives a function from our West observations into H at Archive, and another from East observations into H at Archive. There is exactly one function from our three-element disjoint union to H at Archive that combines those two choices. That universal mapping property, not the word 'archive,' explains the construction.

Here the left Kan extension of F along K assigns exactly this coproduct to Archive. For West and East themselves it gives the original values, because the inclusion is fully faithful in this example. We have extended the diagram with only the identifications required by its arrows.

## What if the source already has a relation?

The previous case had independent sources. Change the original category A so there is an arrow from West to East. Let F send West's two observations to East's single observation by a map that collapses both onto c. Extend A by an Archive object with arrows from West and East, required to agree with the original West-to-East arrow.

What should the left Kan extension put at Archive now? If we simply copied the three tagged observations and kept them distinct, we would forget the existing relation. West a and West b both pass through East c. The diagram tells us those presentations must become identified when they reach Archive.

The colimit at Archive is therefore a singleton, represented by c. The original West observations are not lost because the new construction dislikes them; they are identified because the arrows in the source diagram already express how they are related. This is the same quotient-like behavior we encountered in coends.

The lesson is that 'combine the input sets' is not a complete algorithm. We must combine them *according to the source arrows*. If the indexing category contains no arrows, the result is a disjoint union. If it contains a relation that makes one object terminal within the relevant indexing diagram, that object alone may determine the result.

## The left universal property

Let's name the roles explicitly. We have a functor K from a category A to a category B. We have data F from A to a target category D, often Set. A left Kan extension is a functor L from B to D, together with a natural transformation from F to L after L is composed with K.

That natural transformation is the way our old data enter the extension. We call it the unit of the universal problem, although it should not be confused automatically with the unit of an unrelated adjunction. Now suppose another proposed extension H from B to D comes with a way of mapping the original data F into H after restriction along K. The left Kan extension is universal if that map factors through L in exactly one natural way.

In less symbolic language, L is the most general extension receiving the original data. Anyone who wants to send the original data into another B-shaped diagram can do so uniquely through L. This is why coproducts and colimits appear: they are universal recipients of compatible maps.

An important qualification is that a Kan extension is defined by a universal property even when its values cannot be computed with a neat pointwise formula. Existence needs hypotheses. In Set, with a small indexing category, we usually have the relevant colimits, so the pointwise construction can be made explicit.

## Pointwise calculation by looking backward

Fix one object b in the larger category B. To compute the left Kan extension at b, examine every way an old object K of a can map to b. An entry in the relevant indexing category is a pair: an old object a, and an arrow from K of a into b. Arrows between entries must respect these maps into b.

This is the comma category often pronounced 'K down b.' We take the functor F on this indexing category and form its colimit. That colimit is the value of the left Kan extension at b, under the usual smallness and cocompleteness assumptions.

For our Archive object, the entries are the map from West to Archive and the map from East to Archive. Because West and East were unrelated in the first example, there are no connecting arrows between these entries. The colimit is the disjoint union, with three tagged observations. In the second example, there is also the West-to-East arrow, and the map through East agrees with the direct West-to-Archive map. The colimit identifies both West observations with c.

This calculation supplies the exact criterion for what gets merged. Rather than inventing archive rules by hand, we enumerate ways existing observations reach the new object and impose the relations already present among those ways.

## A right extension asks a different question

A right Kan extension reverses the arrows in the universal problem. Instead of a universal recipient of old data, it is a universal source of data compatible with the old values. In its pointwise form, we look at arrows that go *from* the new object b *to* the existing objects K of a, then take a limit of the corresponding F values.

To make that tangible, construct a different indexing category. Again take two unrelated observed objects West and East. But now add a new object called Query, with an arrow from Query to West and an arrow from Query to East. We want a value at Query that can map into both observed sets. The natural choice is their product.

With West values a and b, and East value c, the product has two elements: the pair a with c, and the pair b with c. A query answer specifies a choice at West and a choice at East. The projections provide its required maps to the existing observations. Any other candidate with functions into both observed sets factors uniquely through this product.

Thus the right Kan extension at Query is a product in this simple example. It collects compatible selections. If the indexing diagram has more arrows, the limit imposes equations between those selections. This matches the role of ends as objects of compatibility.

## Which way do the arrows point?

This is the most common place to make a conceptual mistake. For a left Kan extension at b, the pointwise indexing objects are arrows from K of a into b. For a right Kan extension, they are arrows from b into K of a. The difference is the difference between receiving data from existing objects and projecting choices toward existing objects.

Do not assume the same new object yields a coproduct on the left and a product on the right merely because its shape looks like two spokes. In the Archive example the spokes point *into* Archive. Its left extension gets a coproduct. Its right extension at Archive would be indexed by arrows from Archive toward the old sources. In our simple category there are no such arrows, so its right pointwise value is a terminal object, a singleton in Set. By contrast, the Query example has spokes pointing *out of* Query, so its right extension gets a product.

This distinction also clarifies why universal properties must include types and directions. A diagram can be drawn with the same nodes and still describe a completely different problem after we reverse one set of arrows. The category records those directions as mathematical data.

## A boundary test for the formula

Consider what happens when a new object b has no arrows coming from old objects K of a. Then the comma category K down b is empty. In Set, its colimit is the empty set. This is exactly what we should expect from a left extension that introduces no arbitrary observations: no old data can reach the new object.

Conversely, if there are no arrows from b to any old K of a, the comma category b down K is empty. Its limit in Set is a singleton, because there is exactly one compatible choice over an empty family of constraints: the empty tuple. At first this contrast can sound like a paradox. It is simply the difference between a freely generated recipient with no generators and a universal compatible family with no conditions to satisfy.

This edge case makes a useful diagnostic. If a proposed implementation returns a nonempty collection of invented values for an empty left-indexing diagram, it is importing information from outside the Kan-extension property. If it returns an empty set for an empty right-indexing diagram in Set, it has confused the initial and terminal objects.


## Kan extensions as adjoints to restriction

We can now recognize an adjunction. Suppose the relevant Kan extensions exist for all the diagrams we want. Precomposing a B-shaped functor with K produces an A-shaped functor: we simply look at its values and arrows on the old indexing category. Call this restriction along K.

Left Kan extension is left adjoint to restriction. That means maps from the left extension of F into a B-shaped diagram H correspond naturally to maps from F into the restriction of H. Right Kan extension is right adjoint to restriction. Maps from the restriction of H into F correspond to maps from H into the right extension of F.

These are the general versions of the coproduct and product mapping properties we used earlier. A coproduct is a universal recipient of maps from components. A product is a universal recipient of maps into components. The adjunctions explain why their appearance in the extension problem is systematic.

A practical benefit is that Kan extensions are determined up to unique natural isomorphism when they exist. Two constructions that satisfy the same universal property are equivalent in the precise categorical sense. That frees us to choose whichever explicit model is easiest to compute, rather than treating one implementation as canonical by declaration.

## Ordinary colimits are an instance

Here is a useful specialization. Let A be any small indexing category, and let B be formed by adding a new terminal object t to A, together with one arrow from each object of A into t, compatible with all existing arrows. Include A into B. Extending an A-shaped diagram F by a left Kan extension then assigns its ordinary colimit to t.

We've seen this when A had two discrete objects: the colimit was a coproduct. When A had a connecting arrow into a terminal object, the colimit was determined by that object. More elaborate A-shaped diagrams yield coequalizers, pushouts, and other colimits. Kan extension supplies the common extension language behind them.

Dually, if we add a new initial object s with arrows from s to every old object, the right Kan extension at s computes the ordinary limit of F. Products are the simplest disconnected case; equalizers and pullbacks arise when the source already has compatibility arrows. This is a useful memory aid: left extension by receiving arrows leads to colimits, right extension by issuing arrows leads to limits.

The phrase 'all concepts are Kan extensions,' associated with Mac Lane's presentation and developed in later texts, is a provocative reminder of this organizing power. It should not be heard as a proof that every mathematical definition has only one possible Kan-extension expression, or that the expression makes calculations automatic. The particular functor, target category, and universal property still do the mathematical work.

## A practical application to feature aggregation

Imagine a dataset with values recorded by neighborhood but a report organized by larger districts. A mapping K assigns each neighborhood to its district. If neighborhoods are discrete objects and each contributes a set of labeled observations, left Kan extension along K forms, for each district, the disjoint union of the observations of neighborhoods mapped to it.

Suppose instead the values are numbers that should be added. The right target category and its monoidal or algebraic operations now matter: ordinary Set colimits do not automatically add numbers. We would need a functor into an appropriate category and a universal construction that actually expresses the desired aggregation. Category theory organizes structure; it does not infer the business rule from a suggestive diagram.

A right extension in a set-valued setting might assemble all mutually consistent neighborhood choices into district-level records. Its limit can be empty if constraints are incompatible, even when each neighborhood has an individually valid choice. This is an important caution in local-to-global problems: pointwise existence does not guarantee a compatible global selection.

The difference between left and right extensions becomes useful in data migration, logical semantics, and algebraic topology because these domains repeatedly face the problem of transporting information between indexing schemes. But an application must say what its arrows mean. Is the arrow a restriction, an inclusion, a measurement transform, or a dependency? The universal formula only becomes interpretable after those choices are made.

## How coends enter the picture

There is a second way to write the left Kan extension in Set-like situations, using a coend. At the new object b, we combine all pairs consisting of an arrow from K of a to b and an element of F of a. Then we identify two such presentations whenever a morphism in A lets us move information between the arrow part and the data part.

This is exactly the pattern of a coend. The arrow into b is contravariant in the old object a, while F is covariant in a. The balancing relation identifies two ways of representing the same contribution. The quotient that results is the universal extension value.

You can hear the formula directly in the Archive example. We have one way for each source to reach Archive, and each observation contributes a tagged pair with that way. If the sources are unrelated, no identifications occur between the two groups. If a West observation maps into an East observation and the corresponding arrows commute, those tagged pairs become equivalent. The abstract formula is just the explicit quotient we already computed.

The usefulness of this perspective is that Kan extensions and coends are not two unrelated tricks. The pointwise colimit and the coend quotient are alternate descriptions of the same construction under their appropriate assumptions. Understanding one helps you debug the other.

## What universality does and does not promise

A left Kan extension is universal with respect to maps *out* of its result. A right Kan extension is universal with respect to maps *into* its result. Neither automatically means that a new value is empirically accurate, statistically optimal, or the only possible sensible modeling choice. Universality takes place inside a specified category with specified arrows.

Nor do Kan extensions guarantee that an original diagram embeds without information loss. If K identifies objects or arrows, extending and then restricting may change the data. The natural transformation from F into its left extension after restriction need not be an isomorphism for an arbitrary K. We saw an especially favorable case with a fully faithful inclusion and well-behaved examples, but should not generalize that feature without checking the hypotheses.

Even for fully faithful K, the unit of a pointwise left Kan extension is an isomorphism when the construction exists in the standard setting; the nice behavior follows from the indexing-category analysis, not from the word 'extension' alone. Outside these conditions, we must examine the actual unit or counit.

## One last calculation

Let West have two records and East have one. The original indexing category is discrete; the larger category adds Archive with arrows from each source. The left Kan extension at Archive has three tagged records. Every proposed archive assignment from the two source sets corresponds uniquely to a map out of those three records. That is the defining universal property in miniature.

If instead the new object Query points to both source objects, its right Kan extension has two paired records: one choice from the two-element West set and the unique East choice. Every compatible way to project another object into both sources factors uniquely through those pairs.

These two computations are small enough to be checked without writing a single abstract symbol, but they have already displayed the defining shapes of left and right Kan extensions. The general theory says how to perform the same kind of extension over arbitrary categories, with every existing arrow contributing its share of compatibility or identification. The result is a controlled answer to a problem that appears whenever mathematical data must be carried from one context into another.


<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

For \(K:A\to B\), \(F:A\to D\), the **left Kan extension** \((\operatorname{Lan}_K F,\eta)\), where \(\eta:F\Rightarrow (\operatorname{Lan}_K F)K\), satisfies naturally in \(H:B\to D\)
\[
\operatorname{Nat}(\operatorname{Lan}_K F,H)\cong\operatorname{Nat}(F,HK).
\]
The **right Kan extension** \((\operatorname{Ran}_K F,\varepsilon)\), \(\varepsilon:(\operatorname{Ran}_K F)K\Rightarrow F\), satisfies
\[
\operatorname{Nat}(H,\operatorname{Ran}_K F)\cong\operatorname{Nat}(HK,F).
\]
For small \(A\) and suitably (co)complete \(D\), pointwise formulas are
\[
(\operatorname{Lan}_K F)(b)=\operatorname{colim}_{(K\downarrow b)}F(a),\quad
(\operatorname{Ran}_K F)(b)=\operatorname{lim}_{(b\downarrow K)}F(a).
\]
In \(\mathbf{Set}\), a coend formula for the left extension is
\[
(\operatorname{Lan}_K F)(b)\cong \int^{a\in A}B(K a,b)\times F(a).
\]
The last formula assumes the relevant size conditions and uses the balancing relation from the coend.

### Exercises with answers

1. **Exercise:** For discrete A on two objects, B adding a receiving object t, with F-values of sizes 2 and 3, how large is \(\operatorname{Lan}F(t)\)? **Answer:** Five tagged elements.
2. **Exercise:** For B adding a source s pointing to those two objects, what is \(\operatorname{Ran}F(s)\) in Set? **Answer:** Their product, of size six.
3. **Exercise:** What is the indexing category for a pointwise left Kan extension at b? **Answer:** \((K\downarrow b)\), with objects \((a,Ka\to b)\).
4. **Exercise:** Is the unit \(F\to(\operatorname{Lan}_K F)K\) always an isomorphism? **Answer:** No, not for an arbitrary K. In the standard pointwise setting it is an isomorphism for a fully faithful K.

### References

- Emily Riehl, *Category Theory in Context*, Chapter 6, https://emilyriehl.github.io/files/context.pdf
- Emily Riehl, *Categorical Homotopy Theory*, Section 1, https://emilyriehl.github.io/files/cathtpy.pdf
- Saunders Mac Lane, *Categories for the Working Mathematician*, Chapter X, Springer.
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
