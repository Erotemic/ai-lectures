# 001000 — Categories and Composition: What Can Arrows Tell Us?

**Track:** An Introduction to Category Theory. **Background:** functions, sets and elementary algebra; all categorical terminology introduced here. **Theme:** composition, identity, arrows, and examples that behave differently from sets.

<!-- BEGIN SPOKEN LECTURE -->

# Categories and Composition: What Can Arrows Tell Us?

A train map contains stations and routes. The stations are interesting places, but a traveler needs to know which journeys can be combined. If one route goes from Albany to New York and another goes from New York to Philadelphia, a complete travel plan connects them. We can study the possible journeys without first cataloging the architecture of the stations. This is the beginning of a useful mathematical shift: examine the relationships between things and the laws for combining those relationships.

A function is a more exact example. A function takes an input from one set and returns an output in another set. If the first function assigns each student a classroom, and the second function assigns each classroom a building, then following both functions assigns each student a building. This combined assignment is another function. The particular names of the students and buildings are irrelevant to the rule that makes the combination valid.

Now ask a broader question. Are there situations in which we can combine relationships exactly as we combine functions, even when the things being related are not sets? Yes. Maps between vector spaces, continuous maps between spaces, transformations between programs, inclusion relations between ordered objects, and paths through a network all provide examples. Category theory begins by isolating the common structure of these examples.

In the nineteen forties, Samuel Eilenberg and Saunders Mac Lane were trying to compare constructions arising in topology and algebra. Their 1945 paper gave precise definitions of categories, functors, and natural transformations. The original motivation involved sophisticated mathematics, but the entry point is elementary: composable arrows and identity arrows. Eilenberg and Mac Lane were interested in how constructions related to one another, and their language proved useful far beyond its original application.

## Start with actual functions

Take three sets. The first contains the integers zero, one, and two. The second contains the words zero, one, and two. The third contains the two labels even and odd. Define one function that writes each integer as its word. Define another that sends the words zero and two to even, and the word one to odd. Following the two gives the parity of an integer.

There is no mystery about the combined function. Starting with two, the first function gives the word two; the second gives even. Starting with one, the answer is odd. A mathematician calls this operation composition. When we say the second function after the first, we mean apply the first and then apply the second. The order matters because the output of the first must be a valid input for the second.

Add a fourth set, perhaps the set of two colors, with green assigned to even and red to odd. Now we have three successive functions. We can first compose the word-conversion and parity functions, then apply the color function. Or we can first compose parity with the color function, then follow the word-conversion function. Both procedures produce green for zero and two, red for one.

This is associativity. The grouping of successive operations does not affect the combined result, provided their inputs and outputs match. We have not claimed that composition is commutative. Reversing two functions can make no sense at all, because their domains may not fit. Even when the reversal makes sense, it may produce a different answer. Associativity concerns parentheses, not order.

Every set also has an identity function, which sends each element back to itself. Following a function by the identity of its target does nothing. Preceding that function by the identity of its source also does nothing. These identity functions may seem almost too obvious to mention. They give us a way to describe operations that preserve an object while fitting the same composition laws as all other maps.

The words source and target are important. A function from A to B is an arrow with source A and target B. A second function from B to C can follow it. We would not ordinarily compose a function from C to D with a function from A to B in the wrong order. Category theory maintains this bookkeeping explicitly, because many abstract mistakes are mistakes about domains and codomains.

## The definition that all these examples share

A category consists of objects, arrows between objects, identity arrows, and a way to compose arrows whenever the target of one agrees with the source of the next. Each object has an identity arrow from itself to itself. Composition is associative, and identity arrows act as left and right identities.

That is the definition. There are technical conventions about the size of collections of objects and arrows; we will avoid those set-theoretic difficulties by using small examples whenever possible. The essential requirements are the two laws we have already checked for ordinary functions.

Think about how little the definition says. It does not tell us what an object is made of. A category does not have to provide elements of its objects, distances between them, or coordinates on them. It tells us which arrows are available and how arrows can be composed. We are permitted to learn about an object by examining the arrows leading into and out of it.

One important example is the category of sets and functions, commonly called Set. The objects are sets, and the arrows are functions. If the sets are large or taken all together, the collection of objects is too large to be an ordinary set in common foundations. We can work with a suitable small fragment for our calculations, or use the standard language of large categories. Either choice leaves the composition laws unchanged.

A second example is the category of vector spaces over the real numbers with linear maps as arrows. A linear map preserves addition and scalar multiplication. Two linear maps compose to another linear map. An identity map is linear. Associativity follows from ordinary function composition. Notice that not every function between vector spaces is an arrow in this category; only the structure-preserving ones qualify.

A third example uses topological spaces and continuous maps. The word continuous carries mathematical content about neighborhoods and open sets, but the categorical laws are again familiar. Composing continuous maps gives a continuous map, and an identity map is continuous. Thus the category packages the spaces and the maps that respect their topology.

These examples are not interchangeable. A function can be perfectly valid in Set and fail to be linear. An arbitrary function between topological spaces can fail to be continuous. Category theory lets us describe their common formal pattern without erasing those distinctions.

## A category with almost no elements

Suppose we have three tasks. Task A must finish before task B, and task B must finish before task C. We can represent this ordering by arrows from A to B, from B to C, and from A to C. Every task has an arrow to itself, meaning that it is no later than itself. Combining A-to-B with B-to-C yields A-to-C.

This is an example of an order as a category. In a partially ordered set, put a single arrow from x to y whenever x is less than or equal to y. There is at most one arrow between any fixed pair of objects. Reflexivity supplies identity arrows. Transitivity supplies composition. Associativity holds automatically because, if an arrow exists between a specified pair, there is at most one choice for it.

For instance, consider the numbers one, two, three, and six, ordered by divisibility. There is an arrow from one to six because one divides six. There is an arrow from two to six because two divides six. There is no arrow from three to two. An arrow from one to two followed by one from two to six gives the arrow from one to six. The category records divisibility without representing any numerical function at all.

The shape of this example challenges a common misunderstanding. An arrow does not have to be an ordinary function between underlying sets. In a poset category, an arrow expresses a relation. Some categories have many different arrows between the same two objects. Some have only one or none. The same composition laws govern them all.

A partially ordered set also illustrates the special meaning of an isomorphism. In a general category, an arrow from A to B is an isomorphism if there is an arrow back from B to A such that both round trips are identities. In the category of sets, these are precisely bijections. For vector spaces with linear maps, they are invertible linear transformations. For posets treated as categories, isomorphism of two objects means both x is less than or equal to y and y is less than or equal to x. Antisymmetry then forces x and y to be the same element.

If we used a preorder, which need not be antisymmetric, two distinct objects could have arrows in both directions and therefore be isomorphic. Category theory is often more interested in isomorphism than in literal equality. The distinction already appears in this tiny example.

## An arrow can be a process

For a different sort of category, imagine a directed graph of rooms and one-way doors. There may be an arrow along each door. But if our category contains only individual doors, we cannot compose two doors and obtain another arrow unless that two-door route has already been named. One common solution is to allow every finite directed path as an arrow.

The objects are rooms. An arrow is a path from one room to another. The identity at a room is the empty path that stays where it started. Composition concatenates paths. If a path goes from the library to the hall and another goes from the hall to the laboratory, their concatenation is a path from library to laboratory. Concatenating several paths is associative. Empty paths change nothing.

This construction is called the free category on a directed graph. We have added precisely the paths needed to make composition possible, without arbitrarily declaring different paths equivalent. If two routes through a building start and end at the same rooms but pass through different corridors, they remain distinct arrows.

We can see why it is not always safe to identify an arrow merely by its source and target. In a poset there is at most one arrow between two objects. In a path category there may be many. A category's arrows can carry meaningful distinctions between different ways of reaching the same destination.

An important single-object example works differently again. Take a monoid: a set of operations with an associative multiplication and an identity element. Make a category with one object, say a computer state, and one arrow for every element of the monoid. Composition is monoid multiplication. The identity operation becomes the identity arrow. The entire algebraic structure lives in the arrows, even though there is only one object.

For a tangible case, let the arrows be the nonnegative integers, with composition given by addition. There is one object. The arrow called three followed by the arrow called five is the arrow called eight. The identity is zero. We cannot get an inverse to the arrow three within this category, because there is no nonnegative integer that adds to three to produce zero. This makes three an endomorphism, an arrow from an object to itself, but not an isomorphism.

If we used all integers instead, under addition, every arrow would have an inverse: three is undone by negative three. The resulting one-object category comes from a group. Thinking of a group as a category with one object lets us compare group actions and other constructions with the same language used for sets and spaces.

## What can we infer from arrows?

Let us try a small theorem. Suppose there is an isomorphism from A to B. We claim its inverse arrow is unique. Imagine two proposed inverses, called g and h, both going from B back to A. Each undoes the original arrow f on both sides. We can begin with g. Because f followed by h is the identity of A in the appropriate orientation, we can insert that identity into g's composition. Associativity allows us to regroup the arrows. The inverse laws then reduce the result to h. So g equals h.

The exact symbolic calculation is short and appears in the mathematical companion, but its meaning is worth hearing. Two arrows that really undo the same arrow on both sides must agree. The proof uses only identities and associativity. It never inspects the elements of A or B. Therefore it is valid in every category.

Another useful distinction is between an object and the way we represent it. In the category of real vector spaces, the plane can be modeled by ordered pairs of real numbers. A different two-dimensional real vector space may be given by polynomials of degree at most one. Both have an addition and scalar multiplication. Sending the pair of numbers a and b to the polynomial a plus b times x gives a linear isomorphism. The spaces are not literally constructed in the same way, but their linear structure is equivalent.

It is tempting to say the category ignores internal structure entirely. That would go too far. The allowed arrows encode much of the structure, because they are chosen to preserve it. Continuous maps reveal topological behavior; linear maps reveal linear behavior; group homomorphisms reveal algebraic behavior. Category theory directs attention to what can be recognized and transported through these maps.

## Why a graph is not automatically a category

Let's revisit the difference between a drawing of arrows and an actual category. Suppose a directed graph contains three objects A, B, and C, with an arrow from A to B and another from B to C. Nothing about the definition of a graph requires an arrow from A to C. But the definition of a category does. If the two given arrows can be composed, their composite must be an arrow from A to C.

We could add a single arrow from A to C and declare it to be the composite. Is that always enough? Not if the graph has more paths. Suppose there is another arrow from B to C, or a loop at B. We must specify the composite of every composable pair, and those choices must obey associativity for all longer chains. Adding arrows is one part of the task; defining a consistent composition law is another.

The free category solves both problems with almost no discretionary identifications. Take the paths in the graph, including paths of length zero. Every path is a list of composable edges. Concatenate lists to compose paths. Associativity follows from associativity of list concatenation, and the empty list is an identity. We have built a category from arbitrary directed-graph data using an entirely concrete construction.

There is a subtle consequence. If the graph has an edge from A to B and an edge back from B to A, the free category does not automatically make A and B isomorphic. The two-edge round trip is a nonempty path from A to A; it differs from the empty identity path. Having arrows in both directions is weaker than having inverse arrows. To create an isomorphism, we would need to impose equations identifying those round trips with identities.

The same warning applies when working with functions. A function f from A to B and a function g from B to A need not be inverses merely because they travel in opposite directions. We must check both composites, g after f and f after g. If only the first composite is the identity, then f is a section and g is a retraction, and the structure is weaker than an isomorphism.

Try an example. Let A contain one element, and let B contain two. Send the unique element of A to the first element of B. Send both elements of B back to the unique element of A. Then g after f is the identity of A. But f after g sends both elements of B to its first element, so it is not the identity of B. The distinction is visible even in tiny sets.

## Composition is an algebra with types

One reason categorical notation helps is that arrows carry their source and target as part of their mathematical role. Ordinary multiplication lets us write a product of numbers without checking anything except that the numbers belong to a suitable number system. Function composition is more restrictive: an output type has to fit the next input type.

Imagine three computer data formats. A parser sends a text string to a structured record. A validator sends a structured record to a Boolean answer. A reporter sends a Boolean answer to a status message. The three operations compose in that order. But we cannot generally compose the reporter directly after the parser, because the reporter expects a Boolean rather than a record. In typed programming notation, the expression would be rejected before execution.

The categorical account of sources and targets is a formal version of that discipline. It makes illegal composites distinguishable from legal but perhaps incorrect composites. This is valuable in mathematical arguments involving many spaces: forgetting a codomain can conceal an error that ordinary algebraic manipulation would not reveal.

Matrix multiplication is another example. A matrix with three rows and two columns represents a linear map from two-dimensional coordinate space to three-dimensional coordinate space. A matrix with four rows and three columns can follow it, yielding a four-by-two matrix. The product in the reverse order is not defined because the inner dimensions do not match. Associativity of matrix multiplication corresponds to associativity of composition of linear maps.

Take the two-by-two matrix that swaps coordinates and the diagonal matrix that doubles the first coordinate but leaves the second unchanged. Applying the diagonal map and then the swap doubles the first input and moves it to the second output. Applying the swap and then the diagonal map doubles what was originally the second input. Both composites exist, but they are different maps. This concrete calculation separates the failure of commutativity from the always-valid associativity law.

## Identities are more than decoration

Could we remove identities and keep just associative composition? We could, and the resulting structure is related to a semicategory. But some basic arguments would become unavailable. Inverse arrows are defined relative to identity arrows. The Yoneda lemma makes essential use of the identity at the representing object. Universal constructions rely on unique maps and comparisons whose compositions are proved to be identities. Functors are required to preserve identities because we need the translations to respect the structure that later proofs use.

A category can have a surprisingly large number of arrows while having a very small number of objects. Conversely, a preorder can have many objects but almost no multiplicity in its arrows. Counting objects is therefore a poor way to estimate a category's complexity. The mathematical content often lies in its endomorphisms, its isomorphisms, or the patterns of composition among different arrows.

To see this in one object, take the collection of positive whole numbers under multiplication. There is one object and an arrow for each positive integer. Composition multiplies integers, and the identity arrow is one. Only one arrow is invertible, because no positive integer greater than one has a positive-integer multiplicative inverse. Change the arrow set to the positive rational numbers under multiplication and every arrow becomes invertible. The object remains the same; the algebra of arrows has changed dramatically.

The one-object view therefore exposes a difference between monoids and groups without relying on lists of group elements acting on another set. A group is a monoid in which every operation can be undone. A categorical isomorphism is the same idea applied to an arrow that may run between two different objects.

These examples also explain why a category is more than a decorated network. It has a coherent algebra of paths, identities, and composites. Once that algebra is established, an apparently modest set of axioms supports a large collection of deductions. We can identify inverse arrows, define universal mapping problems, and ask when two entire systems preserve the same compositional information.

## The boundary of the abstraction

A category does not tell us which of its objects are useful, how a programmer should implement its operations, or which physical system a mathematical model represents. The same bare category can appear in several interpretations. Conversely, two constructions that look similar informally can belong to different categories because their allowable arrows differ.

If we study all functions between sets, the number of elements often controls whether certain functions exist. If we study groups with homomorphisms, the structure of multiplication constrains maps. If we study a preorder, the arrows tell us nothing about internal elements beyond the ordering relation. We must always identify the category before asking whether a particular arrow or construction exists.

This is also why categorical reasoning can produce strikingly general theorems. Once a proof uses only composition and identity laws, it applies to paths, functions, linear maps, and any other example satisfying those laws. The benefit is not that every mathematical fact becomes obvious. We isolate exactly which structural assumptions a proof needs.

Return to the little travel network. We began with stations and routes. We learned that routes can be composed, that staying put behaves as an identity, and that different journeys between the same stations need not be the same journey. In a poset, by contrast, the mere existence of a route can be the entire story. In a one-object category, the interesting algebra happens entirely among operations.

A category is the shared mathematical grammar of these examples. Once we know what counts as an arrow and how arrows compose, we can begin comparing whole mathematical worlds. For now, the definition has earned its place: it is the minimal structure that allows us to speak precisely about objects through their composable relationships.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(\mathcal C\) be a locally small category, with \(\mathcal C(A,B)\) the set of morphisms from \(A\) to \(B\). If \(f:A\to B\) and \(g:B\to C\), then \(g\circ f:A\to C\). The laws are \(h\circ(g\circ f)=(h\circ g)\circ f\), \(f\circ 1_A=f\), and \(1_B\circ f=f\).

**Inverse uniqueness:** If \(g,h:B\to A\) both invert \(f:A\to B\), then \(g=g\circ 1_B=g\circ(f\circ h)=(g\circ f)\circ h=1_A\circ h=h\).

**Order category:** A preorder \((P,\leq)\) has one arrow \(x\to y\) exactly when \(x\leq y\). Antisymmetry identifies isomorphic objects in a poset, whereas a preorder can have distinct isomorphic objects.

**One-object category:** A monoid \((M,\cdot,e)\) defines a category with \(\operatorname{End}(*)=M\), composition \(m\circ n=m\cdot n\), and \(1_*=e\). Orientation is a convention; specify it when interpreting actions.

### Exercises and answers

1. **Exercise:** Why do arrows of a reflexive but nontransitive relation fail to form a category? **Answer:** A composable pair can lack the arrow demanded as its composite.
2. **Exercise:** In the path category of a graph, when is a path invertible? **Answer:** Only empty paths are invertible in the freely generated path category; concatenating nonempty paths cannot yield an empty one.
3. **Exercise:** Does a category force \(g\circ f=f\circ g\)? **Answer:** No; one or both expressions may be undefined, and even endomorphisms need not commute.

### References

- Samuel Eilenberg and Saunders Mac Lane, “General Theory of Natural Equivalences,” *Transactions of the American Mathematical Society* 58 (1945), 231–294, https://doi.org/10.1090/S0002-9947-1945-0013131-6
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- David Eisenbud, “Saunders and Sammy” (recollections), MacTutor, https://mathshistory.st-andrews.ac.uk/Extras/MacLane_Eisenbud/
