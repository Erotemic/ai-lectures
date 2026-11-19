# 004000 — Universal Properties: Defining an Object by What It Does

**Track:** An Introduction to Category Theory. **Background:** categories, functions, basic vector spaces. **Theme:** terminal objects, products, coproducts, pairing maps and uniqueness up to isomorphism.

<!-- BEGIN SPOKEN LECTURE -->

# Universal Properties: Defining an Object by What It Does

Imagine you are designing a record that stores a person's name and their date of birth. A familiar approach is to describe its internal layout: perhaps two fields, one holding text and one holding a date. But there is a different question you could ask. Suppose a system already knows how to produce a name, and also knows how to produce a date of birth, from the same input. Is there a single operation that combines those outputs into a record, and does every such combination work in exactly one way?

This question describes the product of two sets without first specifying a memory layout. A product accepts information destined for either component, and it allows the two pieces to be bundled uniquely. That is the beginning of a universal property: an object characterized by how all other objects can map to it, or how it maps to all other objects, under a uniquely determined factorization rule.

The idea can sound abstract because the word universal is so large. We will keep a small model in view. Let A be a set of names and B a set of dates. Their usual product consists of ordered pairs, with first and second projections. The first projection retrieves the name; the second retrieves the date. If some third set X has a function f assigning each of its elements a name and a function g assigning each a date, there is exactly one function from X to the product that retrieves f and g through those projections.

For an input x, that unique function must return the pair f of x and g of x. There is nothing else it could return if both projections are required to agree. Existence comes from defining the pair. Uniqueness comes from the fact that two ordered pairs are equal exactly when both their coordinates agree.

This is a theorem about ordinary sets. But it is also a pattern that applies to vector spaces, groups, ordered structures, and other categories. Instead of inventing one definition for each setting, we can isolate the diagram that all product constructions satisfy.

## Why uniqueness is essential

Suppose somebody hands us an object P with arrows to A and B. We ask whether every pair of arrows f from X to A and g from X to B can be obtained by following a single arrow from X to P with these two projections. If the answer is yes, that provides a candidate pairing operation.

But if several different arrows X-to-P do the job, P may contain extra distinctions that the projections cannot see. It would not be the universal product we want. The uniqueness clause says the two projected outputs determine the mediating arrow completely. That removes irrelevant extra freedom from the construction.

Consider the set of triples A times B times C, with only the first two projections exposed. For each X with maps to A and B, we could perhaps pick a map into C as well, creating a triple. But the choice of C-component is undetermined. The pairing arrow is generally not unique. The triple is not the product of A and B with those two projections unless C is effectively trivial in the relevant sense.

The product of A and B is therefore characterized by a universal condition over every test object X. We must specify the projections, and for every pair of arrows to A and B there must exist exactly one arrow to the proposed product making the two triangles commute.

One consequence is that a product is unique up to a unique isomorphism compatible with its projections. Suppose P and Q are both products of A and B. Because P has projections, the universal property of Q supplies a unique arrow from P to Q that preserves both coordinates. In the other direction, Q's projections supply a unique arrow from Q to P. Composing these two arrows produces a map from P to itself that preserves both projections. But the identity on P also preserves both projections. By uniqueness, the composite must be the identity. The same argument works on Q.

Thus the two comparison arrows are inverse isomorphisms. We never needed to examine the contents of P or Q. We learned that any two valid implementations solve the same universal problem and are structurally interchangeable.

## The simplest universal object

Before products, there is an even simpler idea. An object T is terminal if every object X has exactly one arrow to T. In Set, any singleton set is terminal. There is exactly one function from any set X to a one-element set: send every input to its only element. The empty set causes no difficulty; its unique function to the singleton is the empty function.

The terminal object of a category need not look like a one-element set. In the category of groups, the one-element group is terminal. There is exactly one homomorphism from every group to it. In the category of topological spaces and continuous maps, any one-point space is terminal. In a poset viewed as a category, a terminal object is a greatest element: every element has an arrow to it.

Suppose T and U are both terminal. There is exactly one arrow from T to U and exactly one arrow from U to T. Their composites are endomorphisms of T and U. Each terminal object has only one endomorphism, and it must be the identity. Therefore the two arrows are inverses. Terminal objects are unique up to unique isomorphism, exactly as products were.

There is a dual idea called an initial object. An object I is initial if it has exactly one arrow to every object. In Set, the empty set is initial, because there is exactly one function from the empty set to any target. In a poset, an initial object is a least element. In groups, the one-element group is both initial and terminal, a zero object in that category. The distinction between initial and terminal can disappear in some categories and remain sharp in others.

Why does the empty set fail to be terminal in Set? A function from a nonempty set into the empty set cannot exist. Why does a singleton fail to be initial in Set? For a target with two elements, there are two functions from a singleton into that target, so uniqueness fails. The failure cases teach us to check arrows, not just plausible shapes.

## Products in different categories

In the category of real vector spaces and linear maps, the product of V and W is the vector space of ordered pairs, with addition and scalar multiplication performed coordinatewise. The two projection maps are linear. For linear maps f from X to V and g from X to W, the pairing map x to the pair f of x, g of x is linear. Existence and uniqueness follow as in the set case.

In the category of groups, the direct product G times H has componentwise multiplication. The projections are group homomorphisms. A homomorphism from X to each factor gives a unique homomorphism into their direct product. Here, taking the set-theoretic pair and supplying the correct group operation solves the categorical problem.

In a poset viewed as a category, a product of elements a and b is a greatest lower bound, often called their meet. Why? The projections from p to a and p to b mean p is below both a and b. For every other lower bound x, a unique arrow from x to p must exist, which means x is below p. Thus p is the greatest of all common lower bounds.

For example, in the divisibility order on the positive integers, the product of six and ten is their greatest common divisor, two. We can test it: two divides both six and ten, and any integer dividing both must divide two. Here a categorical product is not a Cartesian pair. It is a number characterized by a divisibility property. The universal diagram is the same even though the construction looks different.

This is a central reward of category theory. A familiar diagram can describe a pair of sets, a direct product of groups, or a greatest common divisor, depending on the category and its arrows. The abstract idea makes it possible to recognize the same structural problem appearing in different mathematical forms.

## Turn the arrows around: coproducts

A coproduct of A and B reverses the arrows in the product diagram. Instead of a proposed object P projecting to A and B, a coproduct S receives an injection from A and an injection from B. Given any pair of arrows from A and B into X, there is exactly one arrow from S to X that extends both.

In Set, the coproduct is the disjoint union. We label the elements to remember which summand they came from. Even when the same symbol appears in both A and B, its two tagged copies remain distinct. A function from the disjoint union to X is determined by specifying what it does on the A-part and what it does on the B-part.

Suppose A is the set containing two names and B is the set containing one date. The disjoint union has three tagged elements. To define a function out of it, give an output for each of the two names and for the date. The function out of the union exists and is unique because every tagged element belongs to exactly one summand.

Contrast that with a Cartesian product. A Cartesian product of a two-element and a one-element set has two pairs, and its projections recover both coordinates. A disjoint union of those sets has three tagged elements, and its injections mark which source supplied an element. Products and coproducts solve different mapping problems. The names of the constructions are similar because the diagrams are dual.

In the category of groups, the coproduct is the free product, not the direct product. Informally, it contains alternating words built from the two groups, with relations internal to each factor. The universal property says that a pair of homomorphisms from the two groups into X extends uniquely to a homomorphism from their free product into X. The construction is often much larger and less commutative than the direct product.

In the category of real vector spaces, finite products and finite coproducts happen to be represented by the same direct-sum vector space up to canonical isomorphism. The coproduct injections insert vectors into the chosen coordinates; the product projections extract coordinates. We use different universal properties to characterize the same underlying model. In general categories, however, products and coproducts need not coincide.

In a poset, the coproduct of a and b is their least upper bound, called the join. In divisibility order, the join of six and ten is their least common multiple, thirty. The product was two. Reversing the arrow directions has transformed greatest common divisor into least common multiple.

## A calculation in the divisibility category

Let's work this without symbols on a board. Take the positive integers ordered by divisibility. There is an arrow from a to b if a divides b. Fix six and ten. A candidate product p must have arrows from p to six and from p to ten, so p must be a common divisor. Every common divisor x must have an arrow to p, so x must divide p. The largest common divisor in the divisibility sense is two. Check one: one divides two. Check two: two divides itself, and both six and ten. Nothing else divides both six and ten except one and two.

Now for the coproduct c, arrows must go from six and ten into c, so c is a common multiple. For any other common multiple x, there must be an arrow from c to x, meaning c divides x. Thirty works: it is divisible by six and ten, and every common multiple of six and ten is a multiple of thirty.

The example reveals something deeper than a clever reinterpretation of two familiar arithmetic operations. A product is defined by arrows into its factors, and a coproduct by arrows out of its factors. The same abstract logic works in categories without elements, arithmetic order, or familiar binary operations.

## Why products make maps easier to specify

A product is often introduced as a way to store a pair of values. But its universal property is more powerful than a data-storage metaphor because it lets us define maps into a product component by component.

Suppose X is a vector space, and we want a linear map from X into the product V times W. Instead of writing one complicated formula for a function with ordered-pair outputs, we can give two linear maps, one from X to V and one from X to W. The universal property guarantees a unique combined linear map. We can then prove properties of the combined map by composing with the projections.

Here is a numerical example. Let X be the real plane, V the real line, and W another copy of the real line. Define f of x,y to be x plus y, and g of x,y to be x minus y. The product-pairing map takes x,y to the pair x plus y, x minus y. If the input is three, one, the output is four, two. The first projection recovers four, and the second recovers two.

Can we recover the input from the output? Yes. Add the two outputs to obtain twice x, and subtract the second output from the first to obtain twice y. Therefore x is half their sum and y is half their difference. This pairing map is a linear isomorphism of the plane. We have used the product to organize its coordinate formulas into independently meaningful components.

The universal property also proves a familiar distributive-looking identity in Set. A function from X into A times B is exactly the same as a pair of functions from X to A and X to B. In symbolic notation, Hom of X into the product is naturally in bijection with the product of Hom of X into A and Hom of X into B. This statement contains the universal property in one line, with a naturality condition that tracks changes in X and the factors.

Now consider products involving three sets. There are two common constructions: the product of A times B with C, and the product of A with B times C. One contains pairs of the form pair of a,b followed by c. The other contains a followed by the pair b,c. These objects are not literally equal under the usual set-theoretic encodings. But they are canonically isomorphic, and the isomorphism simply reassociates the entries.

Why is the comparison canonical? Both objects solve the same universal problem of simultaneously specifying three arrows from a test object X into A, B, and C. The uniqueness theorem for universal constructions supplies a unique comparison that preserves all three projections. The ordinary reassociation formula is a concrete expression of this universal map.

This reasoning scales beyond three factors. If we have finitely many destinations and maps to each one, any chosen parenthesization of their product gives an equivalent way to combine them. The universal property means that the resulting maps agree coherently, rather than depending on a collection of ad hoc coordinate rearrangements.

## The dual view through coproducts

The coproduct has a different practical use. To define a function out of a disjoint union, specify its action separately on each tagged summand. In programming terms, this resembles handling each variant of a tagged union or sum type. The tags matter because two values with the same spelling may have come from different branches.

Consider a type of messages where the first case is a request to log in and carries a username, while the second case is a request to log out and carries a session identifier. A handler can be defined by two separate functions, one for each variant. The coproduct's universal property says that these branch handlers combine uniquely into a function on all messages.

A product lets us collect independent pieces of information. A coproduct lets us choose among alternatives. Their categorical duality is reflected in the common pairing of record types and tagged unions. However, the analogy holds directly in categories modeling pure functions and types. Operational concerns such as exceptions, nontermination, or memory layout may require richer models.

We can also use the coproduct universal property to construct the swap isomorphism from A plus B to B plus A. Send each element tagged from A into the A-summand of B plus A, and each element tagged from B into the B-summand. The exact mapping is forced by the two branch maps. Applying the swap twice returns the identity, because it returns each tagged value to its original summand. This is the coproduct counterpart of swapping the coordinates of a product.

## A missing product is a mathematical fact

Try the category whose objects are the positive prime numbers, with one arrow from p to q when p divides q. Since distinct primes do not divide one another, the category has only identity arrows. Choose two distinct primes, two and three. A product would need an object p with arrows to both two and three. There is no such object in our category. Therefore this category does not have a product of those two objects.

There is no contradiction. The universal property specifies a possible object but does not force the category to contain one. If we enlarge our category to all positive integers under divisibility, the product appears as their greatest common divisor, one. Enlarging the category has changed which solutions are available.

A second warning concerns maps out of a product. Knowing a function from A times B to X is generally more complicated than knowing one function from A to X and another from B to X. The universal property of a product controls maps into the product. Its arrow orientation matters. For maps out of independent alternatives, the corresponding universal construction is a coproduct.

Try the simplest finite count. Let A and B each have two elements and X have two elements. There are sixteen functions from A times B, a four-element set, into X. There are four functions A-to-X and four functions B-to-X, so sixteen pairs. The counts happen to agree here, but there is no canonical matching that plays the role of the product universal property, and different cardinalities expose the mismatch. For example, if A has two elements, B has three, and X has two, there are sixty-four functions from A times B to X but only four times eight, or thirty-two, pairs of functions from A and B into X.

The universal-property definition forces us to attend to direction, quantification over all test objects, and uniqueness. Those details are the tools that make abstract reasoning reliable.

## Universal maps and representation independence

When a categorical construction is given by a universal property, we can often work with it without choosing a concrete implementation. We need only the projections, injections, or other specified maps and the rule for uniquely factoring compatible arrows.

Suppose one programming library stores pairs as two fields and another uses a nested record. If each representation has the correct projections and satisfies the same universal property in an appropriate category, there is a unique comparison isomorphism respecting those projections. This is a mathematical statement about their interfaces and behavior, not a guarantee that the programs have identical runtime costs, side effects, or memory safety properties.

In pure mathematics, the argument is still more widely useful. Two different constructions of a quotient, completion, or free object can be shown equivalent by checking the universal property rather than inventing a direct element-by-element correspondence. The diagram supplies comparison maps, and uniqueness proves they are inverse.

But the word universal does not mean every object has to exist. Some categories lack binary products or coproducts. For example, a poset without a greatest lower bound for two chosen elements lacks their categorical product. The universal property specifies what a solution would have to do; the existence of that solution is a separate theorem or hypothesis.

## What a universal property teaches

We began with a record that stores a name and a date. The key insight was that an object can be characterized by how maps to its components combine uniquely. We followed that pattern into vector spaces, groups, and divisibility. Reversing the arrows turned products into coproducts, and common divisors into common multiples.

There is one principle that unifies these calculations. We specify a mapping problem, then identify an object through the unique way it solves that problem for every possible input object. This makes representation independence precise. It also tells us exactly which arrows are relevant and which assumptions a construction needs.

Products and coproducts are only the beginning. More complicated diagrams ask us to solve simultaneous compatibility conditions rather than pair two independent outputs. Equalizers, pullbacks, and general limits are extensions of the same idea. The central skill is already available: describe the arrows, state the required commuting equations, demand a unique factorization, and verify existence separately from uniqueness.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Product:** \((P,p_A:P\to A,p_B:P\to B)\) such that for all \(f:X\to A\), \(g:X\to B\) there exists unique \(\langle f,g\rangle:X\to P\) satisfying \(p_A\langle f,g\rangle=f\), \(p_B\langle f,g\rangle=g\).

**Uniqueness:** If \((P,p_A,p_B)\) and \((Q,q_A,q_B)\) are products, arrows \(u:P\to Q\) and \(v:Q\to P\) preserving projections satisfy \(vu=1_P\), \(uv=1_Q\) by uniqueness.

**Coproduct:** \((S,i_A:A\to S,i_B:B\to S)\) such that every pair \(f:A\to X\), \(g:B\to X\) uniquely extends to \([f,g]:S\to X\).

**Poset:** Products are meets when they exist; coproducts are joins. In the divisibility poset on \(\mathbb N_{>0}\), \(6\times 10=\gcd(6,10)=2\) categorically, while \(6+10=\operatorname{lcm}(6,10)=30\) categorically. The displayed symbols \(\times,+\) refer to categorical operations, not numerical multiplication and addition.

### Exercises and answers

1. **Exercise:** What is the product of a set A and the terminal singleton set? **Answer:** Isomorphic to A, via the projection to A.
2. **Exercise:** What is the coproduct of A and the initial empty set in Set? **Answer:** Isomorphic to A, through the canonical injection.
3. **Exercise:** In the divisibility category, what are the product and coproduct of four and six? **Answer:** Two and twelve.

### References

- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- Saunders Mac Lane, *Categories for the Working Mathematician*, Springer, https://link.springer.com/book/10.1007/978-1-4612-9839-7
