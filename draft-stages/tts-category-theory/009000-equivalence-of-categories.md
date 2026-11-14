# 009000 — Equivalence of Categories: When Different Descriptions Mean the Same Mathematics

**Track:** An Introduction to Category Theory. **Background:** categories, functors, natural isomorphisms, full and faithful functors. **Theme:** equivalence, skeletons, quasi-inverses, and invariants.

<!-- BEGIN SPOKEN LECTURE -->

# Equivalence of Categories: When Different Descriptions Mean the Same Mathematics

Suppose you are cataloging finite sets. In one notebook, you have every finite set you can name: a set of colored pencils, a set of chairs, a set of filenames, and many others. In a second notebook, you keep only one standard set of each possible size. The standard set of size three is simply the numbers zero, one, and two. Have you thrown away mathematics by discarding all the other three-element sets?

You have certainly thrown away their names. You have discarded the ability to distinguish the pencils from the chairs as particular labeled collections. But if you are studying how finite sets relate through functions, every discarded object can still be represented by a standard set of the same size. Every function can be translated into a function between standard representatives. That observation leads to a central refinement of the word 'same' in category theory.

Two categories may fail to be isomorphic as categories and still express the same structure up to reversible translation. The right notion is **equivalence of categories**. We will build it carefully, see exactly what it preserves, and learn why the weaker word 'equivalent' can be more useful than 'identical.'

## Two catalogs of finite sets

Start with the category of finite sets and functions. Its objects are finite sets. Its arrows are all functions between them. Now choose a smaller category whose objects are the standard finite sets: the empty set, the one-element set, the two-element set, and so on. Include every function between those standard sets, not merely the obvious order-preserving ones.

There is an inclusion functor from the small catalog into the large one. It sends each standard finite set to itself, viewed as an ordinary finite set, and each function to the very same function. The inclusion is faithful: two distinct functions in the small catalog never become the same function in the large catalog. It is full: between any two standard objects, every function allowed in the large category was already present in the small one.

But it is not onto the objects of the large category. The set containing 'red' and 'blue' is not literally the standard set containing zero and one. Those two sets are isomorphic, however: send red to zero and blue to one, with the obvious inverse. More generally, every finite set of size n is isomorphic to the standard n-element set.

So the inclusion is **essentially surjective on objects**. It can reach every object of the larger category, perhaps only after applying an isomorphism. This word 'essentially' makes the difference between a category and a list of object names.

An ordinary function between two named finite sets can be transported to a function between their standard representatives. To do that, choose a bijection from each named set to its corresponding standard set. Convert the input name into its number, perform the transported function, then convert back if needed. Different choices of bijections may lead to different-looking transported formulas. They remain related by invertible changes of labels.

Notice what would go wrong if the smaller catalog kept only some functions between its standard objects. A translator might preserve every object type and still erase possibilities for interaction. That is why we need fullness and faithfulness in addition to essential surjectivity.

## Three tests for a translation

Let F be a functor from a category C to a category D. The first test asks whether F is faithful. For each fixed pair of objects A and B, consider the map taking a C-arrow from A to B to its image in D. Faithfulness means this map is injective. Distinct arrows with the same source and target remain distinct after translation.

The second test asks whether F is full. For each pair A and B, that same map is surjective onto all arrows from F of A to F of B. There are no extra D-arrows between translated objects that the translator cannot account for.

Fullness and faithfulness together mean the map on each hom-set is a bijection. The translator captures exactly the relationships between objects it has translated. This is stronger than preserving just the number of arrows; it preserves how those arrows compose, because F is a functor.

The third test asks whether F is essentially surjective: every object in D is isomorphic to some F of A. Not equal to it, and not merely linked to it by an arbitrary arrow, but genuinely interchangeable by an arrow with an inverse.

For ordinary small categories in familiar set-theoretic mathematics, these three tests characterize equivalences of categories. There is a foundational qualification: to construct a single quasi-inverse functor from the existential choices implicit in essential surjectivity, one may use an appropriate axiom of choice. In finite examples we can make the choices explicitly. The course will work in the usual classical setting, where the test is valid.

Let's separate the tests with examples. An inclusion that selects only one object from each isomorphism class, but keeps all arrows between selected objects, passes all three. An inclusion of finite sets into all sets passes fullness and faithfulness but fails essential surjectivity: an infinite set cannot be bijective to any finite set. The functor that forgets the operation on a group and remembers only its underlying set is faithful in the usual category of groups, but not full: a set-theoretic function between underlying sets need not respect multiplication.

The three properties detect different forms of lost information. Forgetting objects up to isomorphism can be harmless. Forgetting arrows, or inventing arrows between translated objects, generally is not.

## A quasi-inverse is an inverse up to coherent isomorphism

How can we define equivalence without mentioning these three tests? We can instead demand a translation back. Suppose F goes from C to D, and G goes from D to C. We want to start in C, apply F and then G, and recover the original object. But 'recover' may mean isomorphic rather than equal. So require a natural isomorphism from the identity functor on C to G after F. Similarly, require a natural isomorphism from F after G to the identity functor on D.

This is the definition of an equivalence. G is called a quasi-inverse. An ordinary inverse would demand exact equality of the composite functors with the identities. A quasi-inverse accepts natural isomorphisms as the coherent comparison.

The adjective 'natural' is doing work. If we had an arbitrary isomorphism for each object, those choices could clash with arrows. Naturality says that converting an object, applying an arrow, and converting back agrees with first translating the arrow and then making the comparison. The same pattern appears whenever mathematics treats two coordinate descriptions as equivalent.

Return to finite sets. For each finite set X, choose a bijection from X to the standard set of size X. The chosen bijection tells us what G does to X. For a function from X to Y, transport it across the two chosen bijections. This defines G on arrows, and the transport respects identity and composition. The choices determine a natural isomorphism comparing the composite with the identity. If we choose different labels for the elements, we may obtain a different G, but it still witnesses the same equivalence.

We should not mistake natural isomorphism for literal equality. If an application depends on the printed names 'red' and 'blue,' choosing arbitrary replacements may be unacceptable. Equivalence of categories makes a statement about the structure recorded by objects and arrows. It does not promise to preserve every external convention someone might attach to those objects.

## What does an equivalence preserve?

Let's derive one important consequence rather than treating equivalence as a slogan. Suppose a category C has a terminal object T. That means that for every X in C, there is exactly one arrow from X to T. Apply a full and faithful functor F. For every X, arrows from F of X to F of T correspond bijectively to arrows from X to T. Hence there is exactly one such arrow between those translated objects.

But the target category D may contain objects not literally equal to F of X. Essential surjectivity says each D-object Y is isomorphic to some F of X. Transporting along that isomorphism gives exactly one arrow from Y to F of T. Thus F of T is terminal in D.

This is a general pattern: a construction defined by an appropriate universal property is preserved by an equivalence, up to a canonical isomorphism. The details depend on which construction is under discussion, but the principle comes from two ingredients. Full faithfulness preserves the relevant mapping problems. Essential surjectivity makes sure all target objects can participate in them.

An equivalence also preserves whether two objects are isomorphic, the structure of each hom-set up to its specified bijection, and finite limits and colimits when they exist. It does not preserve the literal number of objects. One category might have many named copies of the same structure; an equivalent skeleton can have one object representing each isomorphism class.

This matters when we decide what a classification theorem should count. Are we counting presentations, or structures up to isomorphism? A category can have many ways to present an object even when there is a single isomorphism type. The language of equivalence tells us which differences are mathematical and which are changes of representation.

## Skeletons and a sharp example

A **skeleton** of a category is a full subcategory containing one representative of each isomorphism class of objects. In our finite-set example, the standard sets with zero, one, two, and more elements form a skeleton. Every category in the ordinary small classical setting has a skeleton after making the relevant choices; the inclusion of a skeleton is an equivalence.

A skeleton has no two distinct isomorphic objects. It may still have nonidentity automorphisms. For example, the standard two-element set has the identity function and the swap function as invertible self-maps. Removing duplicate objects does not remove symmetries within an object.

That point prevents a common mistake. If we replaced the category of finite sets by the natural numbers ordered by size, we would retain the list of possible cardinalities but lose the different functions between sets. A two-element set has two permutations; a bare number in a poset-category has only its identity endomorphism. These categories are not equivalent. A list of isomorphism classes is not, by itself, a skeleton: the skeleton retains all arrows among the chosen representatives.

There is a second useful distinction. A category may be equivalent to a one-object category and yet have more than one object. Take two isomorphic objects A and B with exactly one arrow in each hom-set, all arrows invertible. This is a small groupoid. It is equivalent to the terminal one-object category, because every object is isomorphic to A and there is exactly one arrow between any two objects. It is not isomorphic as a category to the one-object category, because an isomorphism of categories must give a bijection on objects, and these categories have different numbers of objects.

Here we can see the whole difference in one example. Equivalence ignores duplicated objects connected by complete, reversible information; isomorphism of categories still counts the duplicates.

## Equivalence in mathematical practice

Why care about this distinction when developing a theorem? Imagine you want to understand finite-dimensional vector spaces over a fixed field. Every such space is isomorphic to a coordinate space of some dimension. You could keep all finite-dimensional vector spaces, or choose a category with one standard coordinate space of each dimension and all linear maps between them. The latter gives a skeleton.

Working with standard coordinates can simplify calculations. But choosing coordinates is not the same as producing a canonical coordinate assignment. Two different bases may give different matrices for the same linear map. The categorical equivalence certifies that neither choice discards the underlying linear-map structure. It does not manufacture a preferred basis for every vector space.

That observation also warns us against treating isomorphism as identity. A vector space has no built-in preferred list of basis vectors. Its category may be equivalent to one with explicit coordinate representatives, but a mathematical construction that claims to be natural must still respect all linear maps, including changes of basis.

Now consider groups. A single group can be presented by generators and relations in many ways. Two presentations may define isomorphic groups. But a category of presentations with its presentation-changing maps needs a carefully stated relationship to the category of groups before we declare it equivalent. An informal claim that 'both describe the same groups' is insufficient: arrows and their compositions must also be accounted for.

The same caution applies to programming interfaces, databases, and physics. A translation may preserve the kinds of objects while breaking how they interact. Calling it an equivalence requires a proof of its behavior on every relevant map, not a persuasive analogy.

## Why the choice of arrows comes first

Suppose you have two file formats representing finite graphs. One stores edge lists, the other adjacency matrices. If you permit only graph isomorphisms as arrows, you are asking whether the formats describe the same graphs up to relabeling. If you permit all graph homomorphisms, you are asking a richer question about structure-preserving maps, and the translator must now preserve those as well.

Equivalence is always relative to the chosen categories. It cannot be evaluated before specifying which objects and which arrows count. Two systems may be equivalent for one purpose and inequivalent for another because the morphisms encode different operations.

A useful practical test is therefore to ask three questions in order. What information distinguishes arrows? Does the proposed translator preserve that distinction? Can every arrow between translated objects be represented in the source? Can every target object be matched with a translated source object by an isomorphism? Each question has a definite mathematical answer.

Our finite-set example passes because the standard representatives retain every function. If we had kept only bijections between standard sets, we would obtain a groupoid rather than the whole category of finite sets. That groupoid is important in its own right, but it is not equivalent to the original category of all finite sets and functions. There is no way to recover a many-to-one function as an invertible arrow.

## A symmetry test that catches mistakes

There is a particularly quick way to expose a failed equivalence: compare the symmetries of corresponding objects. The invertible arrows from an object A to itself form a group under composition, called the automorphism group of A. A fully faithful functor gives a bijection on the entire set of arrows from A to itself. Because it preserves composition, the bijection carries invertible arrows to invertible arrows and respects their multiplication. The automorphism groups of A and F of A are therefore isomorphic.

Take a two-element set. Its automorphism group has two members: do nothing, or exchange the two elements. A category that merely remembers the cardinal number two as an object in a poset has an automorphism group with one member, the identity. No equivalence can identify those two objects while preserving the relevant category structure. The difference survives even though both descriptions agree about the size of the set.

The same test applies to the groupoid containing two isomorphic objects and exactly one arrow between every pair. Each object has no nontrivial automorphisms, so the one-object terminal category passes the symmetry test. It also passes the full hom-set test, and essential surjectivity handles the extra duplicate object. This example really is an equivalence.

Automorphisms are only one invariant. A complete proof still needs to account for every hom-set, not just the invertible endomorphisms. But a mismatch of automorphism groups is a decisive obstruction. This makes the abstract definition practical: to disprove equivalence, we often need only find one type of compositional information that cannot survive the proposed translation.

## A reconstruction argument

Let us sketch why the three tests are sufficient in the usual classical setting. For each object Y of D, choose an object G of Y in C and an isomorphism from F of G of Y to Y. These choices exist because F is essentially surjective. We have now defined G on objects.

What should G do to an arrow h from Y to Z? Use the chosen isomorphisms to convert h into an arrow from F of G of Y to F of G of Z. Since F is full, some arrow in C maps to that converted arrow. Since F is faithful, that arrow is unique. Define G of h to be it.

Now verify that G preserves identities. The converted identity arrow is the identity arrow between the appropriate translated object, so its unique preimage under the hom-set bijection is the identity in C. Verify composition the same way: the conversion of a composite equals the composite of conversions, and the uniqueness of preimages forces preservation of composition.

The selected isomorphisms produce a natural comparison from F after G to the identity on D. Full faithfulness also constructs a natural comparison between the identity on C and G after F. The two functors are quasi-inverses.

This proof explains why the hypotheses fit together. Essential surjectivity supplies representatives, fullness supplies candidate arrows, and faithfulness makes those candidates unique and compatible. If any ingredient is missing, the reconstruction can fail.

## What the weaker notion accomplishes

A classification rarely needs every name assigned to every representation. Often it needs a way to preserve the genuine operations while replacing objects by manageable representatives. Category equivalence formalizes that balance. It lets us simplify without pretending that a change of coordinates or a chosen encoding is literally invisible.

Remember the two catalogs of finite sets. Every named set can be replaced by a standard one, and every function has a transported counterpart. The second notebook loses labels but preserves all the compositional relationships that made the first notebook a category. That is the content of equivalence: a reversible translation of mathematical structure, where reversible is understood through coherent isomorphism rather than exact sameness of names.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Equivalence.** Functors \(F:\mathcal C\to\mathcal D\), \(G:\mathcal D\to\mathcal C\) and natural isomorphisms \(\eta:1_{\mathcal C}\cong GF\), \(\varepsilon:FG\cong 1_{\mathcal D}\). A given equivalence can be adjusted to an adjoint equivalence with triangle identities. The definition here does not require those identities as extra data.

**Recognition theorem (classical setting).** A functor is an equivalence if and only if it is fully faithful and essentially surjective. Constructing a quasi-inverse from merely existential essential surjectivity can require choice.

**Example.** Let \(\mathbf{FinSet}_{\mathrm{sk}}\) be the full subcategory with chosen finite sets \([n]=\{0,\dots,n-1\}\). Inclusion \(i:\mathbf{FinSet}_{\mathrm{sk}}\hookrightarrow\mathbf{FinSet}\) is fully faithful and essentially surjective, hence an equivalence. It is not an isomorphism of categories when distinct finite sets outside the selected representatives are present.

**Terminal-object argument.** If \(T\) is terminal in \(\mathcal C\), for any \(Y\in\mathcal D\) choose \(\alpha:FA\xrightarrow{\sim}Y\). Then \(\mathcal D(Y,FT)\cong\mathcal D(FA,FT)\cong\mathcal C(A,T)\), a singleton. The existence of the chosen isomorphism uses essential surjectivity and the hom-bijection uses full faithfulness.

**Skeleton.** A full subcategory with exactly one object in each isomorphism class (where representatives can be chosen). Its inclusion is an equivalence. A skeleton retains automorphism groups and all maps between chosen objects.

### Exercises and answers

1. **Exercise:** Show that the inclusion \(\mathbf{FinSet}\to\mathbf{Set}\) is not an equivalence. **Answer:** It is full and faithful, but not essentially surjective: an infinite set is not isomorphic to a finite one.
2. **Exercise:** Why is the cardinality poset not equivalent to \(\mathbf{FinSet}\)? **Answer:** A two-element set has two endomorphisms that are permutations, plus noninvertible maps; a poset object has only an identity endomorphism, so no full-and-faithful comparison can preserve its hom-set.
3. **Exercise:** Does an equivalence preserve the literal number of objects? **Answer:** No; a groupoid with two objects and one arrow between each ordered pair is equivalent to the terminal category.

### References

- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- nLab, *Equivalence of categories*, https://ncatlab.org/nlab/show/equivalence+of+categories
