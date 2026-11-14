# 002000 — Functors: Translating One Mathematical World into Another

**Track:** An Introduction to Category Theory. **Background:** categories, functions, elementary algebra. **Theme:** functor laws, covariant and contravariant maps, faithful and full functors.

<!-- BEGIN SPOKEN LECTURE -->

# Functors: Translating One Mathematical World into Another

Suppose somebody gives you a map of a subway system. Stations become dots on the page, routes become lines, and a complicated transport network becomes a picture. The picture preserves certain facts: which stations are connected and which journeys can follow one another. It does not preserve the smell of the platforms, the number of tiles on the walls, or the cost of constructing the tunnels. A useful representation is selective. It tells us exactly which relationships survive the translation.

Mathematics contains many such translations. A vector space can be regarded merely as a set. A group can be regarded as a set with an operation, and then as its underlying set. A topological space can be viewed as a set when we temporarily ignore which subsets are open. A directed graph can be transformed into its category of paths. We also map structures into new structures: from a set we can form a set of finite lists, and from a linear map we can build a map on tensor powers. What does it mean for one construction to respect the arrows of a category?

The answer is a functor. A functor translates objects and arrows, while preserving identity arrows and the operation of composition. It provides a systematic way to change the context of a mathematical problem without losing the relationships on which categorical reasoning depends.

This idea is especially useful when a diagram expresses a problem. If two different paths through a diagram give the same arrow, a functor sends them to two different paths in the new diagram that still give the same result. We can transport an entire coherent system of relationships rather than translating its pieces independently.

## The simplest translation: forget structure

Consider the category of groups and group homomorphisms. A group is a set equipped with an associative operation, an identity, and inverses. A homomorphism is a function that respects the operation. There is a natural way to view any group as a set: simply look at its underlying elements and ignore its multiplication.

This construction sends each group to its underlying set. It also sends each group homomorphism to the same underlying function. Suppose f goes from group G to group H, and g goes from H to K. Their composite as group homomorphisms is the underlying function that first applies f and then g. If we forget the group structure before composing, we obtain the very same function. Likewise, the identity homomorphism becomes the identity function.

So forgetting is a functor from groups to sets. The definition tells us that the translation respects composition and identity. It does not claim that nothing was lost. We have thrown away the multiplication table and the obligation to preserve it. The arrows remaining between two underlying sets may include many functions that could never serve as group homomorphisms.

An important mathematical habit is to ask what a forgetful construction preserves and what it makes invisible. If two groups have the same finite number of elements, their underlying sets are isomorphic in Set, because a bijection exists. But the groups need not be isomorphic as groups. For example, the cyclic group with four elements and the group whose nonidentity elements all have order two both become four-element sets. Their group structures differ.

The forgetful functor sends genuine group isomorphisms to bijections. In fact, for a group homomorphism, a bijective underlying function has an inverse that is also a homomorphism, so this particular functor reflects isomorphisms. But an arbitrary bijection between the underlying sets need not be a group homomorphism in the first place. That is a failure of fullness, rather than a failure of reflection of isomorphisms.

## Two functor laws

Let C and D be categories. A functor F from C to D assigns to each object A of C an object F of A in D. It assigns to each arrow f from A to B an arrow F of f from F of A to F of B. It must preserve the identity of each object. And it must preserve composition: the image of g after f equals the image of g after the image of f.

We can check these laws in the group example. They hold because the forgetful operation does not alter the underlying functions. Now consider a construction that really changes the objects. Take any set A, and form the collection of all finite sequences of elements of A, including the empty sequence. We call these lists over A.

Given a function f from A to B, transform a list by applying f to each entry. The list a-one, a-two, a-three becomes f of a-one, f of a-two, f of a-three. The empty list stays empty. If we first map every entry by f and then by g, we get the same list as mapping each entry by the composite of g after f. Applying the identity function to every entry leaves the list unchanged.

The list construction is therefore a functor from sets to sets. It changes objects, but carries arrows along in a compatible way. This example will become especially fruitful because the same list operation also has a way to flatten a list of lists. That second structure leads to a concept called a monad. For now, the functor laws are the foundation on which that later algebraic structure can be built.

A different functor sends a set to its power set, the set of all subsets. For a function f from A to B, we can map a subset of A to its image under f, a subset of B. Images respect composition, and the image under the identity is unchanged. Thus power set with direct image is a covariant functor on sets.

But there is another power-set construction. Given a subset of B, we can take its preimage under f, which is a subset of A. This arrow points backward, from subsets of B to subsets of A. Preimages respect identity and reverse composition in the appropriate way. The same assignment of an object to its collection of subsets therefore supports two distinct kinds of translation, and the direction of arrows determines which sort we are using.

## Why direction matters

A covariant functor sends an arrow from A to B to an arrow from F of A to F of B. A contravariant functor sends it to an arrow from F of B back to F of A. The prefix contra records reversal of direction.

For a concrete preimage calculation, let A contain the numbers one, two, and three. Let B contain red and blue. Suppose f assigns one and three to red, and two to blue. The preimage of the subset containing only red is the subset containing one and three. The preimage of the subset containing blue is the singleton containing two. The preimage of the whole target is the whole source. This direction reversal is forced by the question: which inputs are sent into a chosen target condition?

If another function g maps red and blue into a third set C, then the preimage under the composite of g after f equals taking preimage under g and then preimage under f. The order of the preimage operations reverses the order of the original maps. This is a contravariant functor, or equivalently an ordinary functor from the opposite category of Set into Set.

An opposite category has the same objects as the original but reverses every arrow. A composite in the opposite category is defined so that the categorical laws still hold. The idea sounds formal until we notice how often it describes familiar mathematics: preimages of sets, pullbacks of functions, and dual spaces of vector spaces.

For a real vector space V, its dual space consists of linear maps from V to the real numbers. A linear map from V to W induces a linear map from the dual of W to the dual of V by precomposition. A functional that knows how to evaluate a vector in W can be used on V by first sending the vector through the map to W. This pullback points backward, precisely as the inverse image of subsets did.

Try a small example. Let V be the real line, W the real plane, and let f send a number t to the point with coordinates t and twice t. A functional on W of the form first coordinate plus three times the second coordinate pulls back to the functional seven times t on V. The direction changed, but the evaluation is straightforward: apply f, then evaluate.

The double dual construction, from V to the dual of its dual, returns us to the original arrow direction when applied to a linear map. For finite-dimensional vector spaces, the canonical evaluation map into the double dual is an isomorphism. The word canonical is important. The map sends a vector to the operation of evaluating every functional on that vector. It requires no basis choice.

## How much of a map does a functor remember?

Not all functors preserve the same amount of arrow information. Fix two objects A and B in a category. A functor induces a function from the collection of arrows A-to-B into the collection of arrows F-of-A to F-of-B. If this function is injective for every pair, the functor is called faithful. Distinct source arrows remain distinct after translation.

If the induced function is surjective for every pair, the functor is called full. Every arrow between the two translated objects arises from an arrow in the original category. Fullness is a claim about morphisms between images, not a claim that the target category contains no other objects.

The forgetful functor from groups to sets is faithful. Two distinct homomorphisms are distinct underlying functions, so forgetting multiplication does not merge them. But it is generally not full: some functions between underlying sets are not homomorphisms.

A helpful tiny case is the homomorphism from the group of integers under addition to itself. Multiplication by two is a homomorphism. The function that sends every integer to its square is not a group homomorphism, since the square of a sum generally differs from the sum of the squares. The target category Set contains the squaring function as an arrow between the same underlying sets. The source category of groups does not.

Faithfulness and fullness need not travel together. Consider a category where there is exactly one arrow from every object to every object, and map all objects to a single object in the terminal one-object category. Every source hom-set has one element, and the target hom-set has one element, so this functor is fully faithful despite collapsing all the objects. Being fully faithful means retaining the structure of individual collections of arrows; it does not mean sending different objects to different literal objects.

A functor can also preserve particular constructions, such as products or terminal objects, but the two functor laws alone do not force it to preserve every possible limit or colimit. Asking exactly what a functor preserves is a major source of useful mathematical questions.

## Diagrams and why they commute

Picture two paths that both start at A and end at D. One goes from A to B to D. The other goes from A to C to D. A commutative diagram says those two composites are equal. This can express a compatibility condition among four different transformations, not merely a decorative picture.

Suppose we have sets of students, courses, departments, and campuses. We can assign students to courses and then courses to departments; or assign students to campuses and then campuses to departments. The diagram commutes if those two ways of assigning a department always agree. If they disagree, a data model may contain incompatible relationships. Diagram commutativity is a precise test of consistency.

Apply a functor to every object and arrow in a commutative diagram. Since the functor preserves composition and equality of arrows, the new diagram also commutes. This is one way category theory helps make mathematical translation reliable. The proof is immediate once the functor laws are explicit, but the resulting capability applies to large diagrams with many paths.

A functor can send a diagram to another diagram that is simpler to calculate. For instance, by forgetting vector-space structure we can inspect the underlying functions. The simpler view may answer a question about injectivity or cardinality. But if the question concerns linear combinations, we must return to the richer setting. Forgetfulness is useful only when we know what we have forgotten.

## A surprising functor from ordered information

We have considered categories of sets and their functions, but functors can also connect categories built from order relations. Suppose P and Q are partially ordered sets. Treat each as a category: there is one arrow from p to p-prime exactly when p is below p-prime. A functor from P to Q sends objects to objects and must preserve these arrows. Thus it is exactly an order-preserving, or monotone, function.

Take the positive integers ordered by divisibility. Define a function that sends every positive integer n to the collection of its positive divisors. Put an inclusion order on the set of these divisor collections. If a divides b, then every divisor of a divides b. So the divisor set of a is contained in the divisor set of b. This assignment is monotone and therefore a functor between the two poset categories.

Why is this useful? We have translated arithmetic divisibility into ordinary subset inclusion. We can test properties of an integer by looking at which smaller numbers divide it. But different target categories highlight different information. The divisor-set construction is injective on positive integers because n belongs to its own divisor set and is the largest element of that set under the ordinary numerical order, though that extra comparison is a feature of the chosen representation. We can study multiplication and least common multiples by asking what the translation does to unions and intersections of these sets.

In fact the divisor set of the greatest common divisor of a and b is the intersection of their divisor sets. To check this, a positive integer d belongs to both sets exactly when it divides both a and b, which holds exactly when it divides their greatest common divisor. Thus the functor sends a categorical product in the divisibility category, a greatest common divisor, to the intersection of the corresponding divisor sets. Intersection is the categorical product in the inclusion poset.

But it does not simply send least common multiples to unions. The divisor set of twelve contains four and six, while the union of the divisor sets of four and six does not contain twelve. The least common multiple can introduce new common multiples and their divisors. This provides a concrete example of a functor preserving one kind of universal construction while failing to preserve another.

That distinction is central to categorical mathematics. A functor is required to preserve identities and composition, or order in the poset case. Any further preservation claim must be proved. We should not infer that a translation carries every arithmetic operation to an identically shaped operation in its target category.

## A nonexample: a translation that breaks composition

Suppose we assign to each function f from one finite set to another the number of values in its image. Could that number be the arrow part of a functor from finite sets and functions into the one-object category of nonnegative integers under addition? The target category would treat composition of arrows as addition of the assigned numbers.

The function that sends every input to itself on a three-element set has an image of size three. But a functor must send an identity arrow to the identity arrow in the target, which is zero for addition. Our proposed rule sends that identity to three, so it immediately fails. Changing addition to multiplication would make the target identity one, and the same identity would still go to three. This proposal is a statistic about functions, but it is not a functor in either of those target categories.

We can try another idea: assign to a function the number of inputs that map to one selected output. That number depends on which output was selected, and it generally does not compose by simple multiplication. Recording a property of each arrow is not enough to create a functor. It must respect the compositional laws exactly.

For a positive example of a more algebraic arrow translation, consider an endomorphism of a finite-dimensional vector space and its determinant. The determinant of a composite is the product of the determinants. The identity has determinant one. If we restrict to the one-object category whose arrows are endomorphisms of a fixed vector space, determinant defines a functor into the one-object category with real numbers under multiplication. This is a categorical rendering of the multiplicativity of determinant.

The domain restriction is essential: if we allowed arbitrary linear maps between vector spaces of different dimensions, determinants would not be defined for every arrow. By choosing the endomorphism monoid of one fixed finite-dimensional vector space, we obtain a genuine functor. An abstraction is useful partly because it forces us to say which mathematical objects and arrows our formulas actually govern.

## A comparison map that gives real information

Consider the forgetful functor from vector spaces to sets, and ask about zero maps. Every pair of vector spaces has a distinguished linear transformation sending every input to the zero vector of the target. The underlying function is constant, so it certainly exists in Set. But not every constant function between underlying vector-space sets is linear; a linear constant function has to take every vector to the zero vector. The forgotten structure is what singles out the right constant map.

Likewise, a bijective linear map is an isomorphism of vector spaces because its inverse function is also linear. We can prove that directly: if T is bijective and linear, and u and v are target vectors, write them as images of source vectors. The inverse sends their sum to the sum of their inverses, and it respects scalar multiplication by the same argument. That inverse belongs to the linear-map category.

A bijective arbitrary function of the underlying sets need not be linear. We therefore learn a distinction between preserving isomorphisms and reflecting them. Every functor preserves isomorphisms, because a functor sends inverses to inverses. A functor need not always reflect isomorphisms. This particular forgetful functor does reflect them for arrows that are linear maps, but it is not full: most underlying set functions, including many bijections, do not come from linear maps. Distinguishing those claims prevents a basic mistake about functor properties.

This gives another reason to track what is being translated. The source tells us which arrows are legitimate; the target may admit many more. Functoriality ensures consistency, but it does not guarantee that the target sees all of the constraints that made the source interesting.

## Recognizing a translation without forcing an equivalence

Two categories may describe related mathematics at different levels of detail. A functor connects them without claiming they contain the same information. If we can translate from C to D and back and obtain the original structures up to coherent isomorphism, we may have an equivalence of categories. This is stronger than the existence of an arbitrary functor and generally weaker than literal equality of categories.

A simple warning comes from the category of vector spaces. Choosing a basis identifies an n-dimensional real vector space with n-tuples of real numbers. But a change of basis changes the coordinates, and the coordinate description is not automatically compatible with every linear map unless the chosen bases and induced matrices are tracked. The underlying coordinate operations can be perfectly valid while the choices fail to yield a natural identification independent of representation.

The question of dependence on choices leads to a deeper concept. Suppose two functors carry the same category into another, and we want to compare their outputs object by object. It is easy to choose a map between the images of each individual object. Harder is asking whether these comparisons respect every arrow of the source category. That extra coherence is called naturality.

For now, the central calculation is already in hand. A functor transports arrows and respects the two laws of composition and identities. A contravariant functor transports arrows backward according to a coherent rule. Faithful and full functors measure how much arrow information survives. These distinctions let us compare mathematical worlds with precision, without pretending that every translation loses nothing.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

A covariant functor \(F:\mathcal C\to\mathcal D\) consists of \(F:\operatorname{Ob}(\mathcal C)\to\operatorname{Ob}(\mathcal D)\) and maps \(F_{A,B}:\mathcal C(A,B)\to\mathcal D(FA,FB)\), satisfying \(F(1_A)=1_{FA}\) and \(F(g\circ f)=F(g)\circ F(f)\). Contravariant functors are functors \(\mathcal C^{op}\to\mathcal D\).

**Powerset variants:** For \(f:A\to B\), direct image \(f_!:P(A)\to P(B)\) and inverse image \(f^*:P(B)\to P(A)\), with \((g\circ f)^*=f^*\circ g^*\). Direct image preserves unions; inverse image preserves unions, intersections and complements.

**Dual map:** \(f^*:W^*\to V^*\), \(f^*(\varphi)=\varphi\circ f\). For \(f(t)=(t,2t)\) and \(\varphi(x,y)=x+3y\), \(f^*(\varphi)(t)=7t\).

**Faithful versus full:** faithful iff every \(F_{A,B}\) is injective; full iff every \(F_{A,B}\) is surjective. The forgetful functor \(\mathrm{Grp}\to\mathrm{Set}\) is faithful and not full.

### Exercises and answers

1. **Exercise:** Is the finite-list assignment with entrywise application of a function a functor? **Answer:** Yes: list mapping preserves identity and composition entry by entry.
2. **Exercise:** Why does inverse image reverse arrows? **Answer:** An output-side property selects the inputs satisfying it, so \(f^{-1}:P(B)\to P(A)\).
3. **Exercise:** Does fully faithful imply injective on objects? **Answer:** No. Distinct but isomorphic objects may have the same image.

### References

- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- Eilenberg and Mac Lane (1945), https://doi.org/10.1090/S0002-9947-1945-0013131-6
