# 003000 — Natural Transformations: What Does It Mean to Work the Same Way Everywhere?

**Track:** An Introduction to Category Theory. **Background:** categories and functors. **Theme:** naturality squares, natural isomorphisms, canonical maps, and the difference between a construction and a choice.

<!-- BEGIN SPOKEN LECTURE -->

# Natural Transformations: What Does It Mean to Work the Same Way Everywhere?

You have a list of names. You want a collection in which every name appears only once, because duplicates do not help you answer whether someone is present. There are two obvious operations available. First, you could change every name in the list according to a dictionary and then remove duplicates. Or you could remove duplicates first and then change every retained name according to the dictionary. Will the results agree?

They will agree if the result is regarded as a set. Suppose Alice and Alicia both become the same standardized name. Removing duplicates before renaming produces a set containing Alice and Alicia, then the renaming collapses them to the same value. Renaming first may create two copies of the same standardized name, but removing duplicates collapses those too. Either way, the result is the set of all renamed values. The order of the two operations does not affect the final set.

That small observation is a model of naturality. We have one construction that turns a set into its finite lists. Another construction turns a set into its finite subsets. We can compare the two by sending each list to the finite set of its entries. The comparison works compatibly with every function that renames the entries. It is a family of maps, one for each underlying set, constrained by the available functions.

Category theory calls such a coherent comparison a natural transformation. The word natural carries a mathematical test. It does not mean elegant, obvious, or morally preferable. It means that moving through the source category before comparing gives the same result as comparing first and then moving through the target category.

## A family of maps is only the beginning

Suppose F and G are functors from one category C into another category D. For every object A of C, imagine a map from F of A to G of A. This produces a family of arrows. But there may be many unrelated choices, and an arbitrary family need not say anything coherent about how F and G behave on arrows.

To earn the name natural transformation, the family must satisfy a condition for every arrow f from A to B in C. We can go from F of A to G of B in two ways. First apply F of f, reaching F of B, and then use the comparison at B. Or first use the comparison at A, reaching G of A, and then apply G of f. These routes must agree.

Mathematicians draw this as a square. The upper horizontal arrow is F of f, the lower horizontal arrow is G of f, and the two vertical arrows are the comparison maps at A and B. A naturality square commutes when the two paths across the square have equal composites.

We should be precise about the order. Start with an element of F of A, if the target category happens to be sets. Travel right then down, or down then right. Both procedures must land at the same element of G of B. In an abstract category we do not need elements; equality of the two composite arrows expresses the whole condition.

This is substantially stronger than checking the comparison only for one object. Every arrow in the source category imposes a compatibility requirement. A transformation can exist at each object while failing to be natural because some arrow reveals a disagreement.

## Work the list-to-set example completely

Let L of A be the set of finite lists of elements of A. A function f from A to B acts on these lists by applying f to each entry. Let P-finite of A be the set of finite subsets of A. A function f acts on finite subsets by taking their direct images. Both constructions are functors from Set to Set.

Define a map alpha at A: send a list to the subset of values appearing in it. We want to check naturality. Take a list with entries a, b, a. Following the list functor through f gives the list f of a, f of b, f of a. Turning that into a set gives the set containing f of a and f of b. On the other route, first forget multiplicity and ordering, obtaining the set containing a and b. Take the direct image under f: again, the set containing f of a and f of b.

The calculation is not special to two entries. For any list, the image of its support is the support of the image list. The same identity proves naturality for every function. We did not have to make different decisions for different sets. The procedure of taking a list's support is uniform, and the equation confirms that uniformity.

Notice what the transformation loses. The lists a, b, a and b, a can have the same support. So the component map need not be invertible. A natural transformation is not necessarily a natural isomorphism. It can perform a genuine simplification, and the compatibility condition still holds.

A second example is the singleton map. Send an element a of A to the list containing exactly a. Let I be the identity functor on Set, sending every set and function to itself. The singleton assignments form a natural transformation from I to L. Applying f before taking the singleton or taking the singleton before applying f entrywise produces the one-element list containing f of a.

The empty-list assignment does something different. For every set A, there is a function from the singleton set to the set of lists over A that picks out the empty list. Taking the singleton set as a constant functor, the empty-list assignments also form a natural transformation. Naturality here says that mapping any function over the empty list leaves it empty.

These examples show how a single functor can participate in several natural transformations with very different meanings. Some insert data, some discard information, some choose a distinguished construction. The naturality equation is the common structural constraint.

## When a choice destroys naturality

Take an arbitrary two-element set A. Can we select a preferred element from it in a way that works naturally for every bijection? If the set is given as zero and one, a person may say 'choose zero.' But suppose we swap zero and one. A selection that is natural under this permutation would have to be carried along by the swap and remain the chosen element. No element is fixed by that swap. Therefore no natural choice of one element exists for every two-element set with all bijections allowed.

This is a useful way to understand what mathematicians mean by canonical. A construction is often called canonical when it does not depend on an arbitrary labeling or basis. Naturality provides a precise expression of this independence, though 'canonical' is used in several related ways and does not have one universal formal definition.

A similar problem occurs in linear algebra. Every finite-dimensional vector space has a basis, but choosing a basis is a separate decision. A two-dimensional vector space can be described by infinitely many bases. A generic linear automorphism moves a chosen basis to another one. No selection can be simultaneously compatible with all invertible linear transformations in the naive sense that it singles out a preferred basis of every vector space.

On the other hand, each vector space V has a natural map to its double dual. A vector v determines a functional on the dual space: give it a functional phi and it returns phi evaluated at v. If T goes from V to W, then the double-dual map induced by T carries the image of v exactly to the evaluation functional associated with T of v. This compatibility is expressed by a naturality square.

For finite-dimensional vector spaces, the evaluation map is an isomorphism. In infinite dimensions, the canonical map to the algebraic double dual is generally injective but not onto. Both the naturality and the dimensional qualification are important. Naturality says the comparison commutes with linear maps; isomorphism requires an additional property.

This distinction is a reason not to confuse 'natural' with 'always invertible.' A natural map may be an injection, a surjection, neither, or an isomorphism, depending on the setting.

## The historical problem behind the definition

The language of natural transformations arose from the work of Samuel Eilenberg and Saunders Mac Lane on algebraic topology. Mathematicians were using constructions that turned spaces into algebraic objects, such as homology groups. Different ways of making a construction could yield groups that were isomorphic, but an isomorphism chosen separately for every space was not automatically enough.

If a continuous map between spaces induces a homomorphism between their homology groups, then an identification between two homology constructions should respect those induced homomorphisms. The compatibility over every map is what the later language calls naturality.

In their 1945 paper, Eilenberg and Mac Lane placed natural equivalences at the center. The terms category and functor were introduced as part of a framework for understanding such comparisons. This historical order is worth noticing: a formal theory that now begins with a definition of category grew from a problem about when two mathematical constructions count as the same in a coherent way.

David Eisenbud's recollection of the two founders at a 1969 conference describes different temperaments in discussion, one more playful and teasing, the other more forceful and direct. We need not turn that recollection into an explanation of a theorem. It does remind us that mathematical abstractions were developed in conversations among people who had different tastes, styles, and judgments about what was worth formalizing.

## Vertical composition: comparisons can be compared

Suppose alpha is a natural transformation from F to G, and beta is a natural transformation from G to H. At each object A, first apply alpha at A and then beta at A. This composite runs from F of A to H of A. We claim the new family is also natural.

To see why, begin with F of A and an arrow f from A to B. One route uses F of f and then the two comparison maps at B. By naturality of alpha, we can move the first comparison past f, replacing the route by alpha at A followed by G of f. By naturality of beta, we can move the second comparison past f, obtaining the two comparisons at A followed by H of f. We have therefore shown that the large square commutes.

This is sometimes called vertical composition, because one imagines stacking natural transformations. It is associative because composition in the target category is associative, and the identity transformation on F has identity arrows as its components. Thus functors from C to D can themselves serve as objects of a category, with natural transformations as arrows.

This is a beautiful example of categorical thinking folding back on itself. We started with objects related by arrows. Then we developed functors that relate whole categories. Now natural transformations relate functors, and those transformations themselves compose. The layers are connected by the same structural idea, though the exact definitions at each level differ.

An important extra operation, horizontal composition, combines natural transformations along functors as well as between them. It leads toward the two-dimensional structure of category theory. For an introduction, the key observation is simpler: a natural transformation is a compatible family of arrows, and composition preserves compatibility.

## When is a transformation an isomorphism?

Suppose every component of a natural transformation alpha is invertible in the target category. Do their inverses form another natural transformation going backward? Yes. Starting from the naturality equation and composing with the appropriate inverses on both sides yields the naturality equation for the inverse components.

Therefore a natural transformation is a natural isomorphism exactly when all its components are isomorphisms. That theorem is useful because it allows a local check at each object to establish a coherent global invertibility statement. The naturality of the original comparison already supplies the hard compatibility information.

Consider the product of sets A and B. There is a standard bijection from the ordered pairs in A times B to the ordered pairs in B times A, obtained by swapping coordinates. This operation respects functions in both variables. It is a natural isomorphism between two ways of forming a product with reversed factors.

We can test it on a pair consisting of a student and a course. The swap sends student-course to course-student. If we rename students and courses, swapping before renaming produces the same pair as renaming before swapping. The bijection has an evident inverse: swap again. The proof of naturality can be checked on one arbitrary pair, then expressed without reliance on any particular names.

By contrast, a bijection from each finite set of a given size to the standard set of the first n integers depends on a chosen enumeration. A collection of such bijections is not generally natural with respect to all bijections between the source sets. The abstract distinction explains why coordinate systems are useful but are not necessarily intrinsic to a problem.

## Naturality as a test of supposed definitions

Here is a practical way to use naturality. Someone proposes an operation that acts on every set of values. Instead of asking whether the operation sounds canonical, we ask whether it behaves correctly under a function that renames, duplicates, or merges values. If an operation treats values differently because of their labels, an appropriate renaming may expose the problem.

For example, imagine a proposal that chooses the first element of every nonempty finite subset of a set. A finite subset is unordered, so the phrase first element needs an extra ordering. We might declare that every set carries some hidden ordering, but then we have changed the category: its objects are now ordered sets, and its arrows might be required to respect that order. Without that additional structure, a permutation of a two-element set swaps its two elements and defeats any natural choice of one of them.

The argument is short enough to make completely formal. Take a two-element set A containing a and b. Assume we have a natural selection rule that picks an element of every nonempty finite subset. Apply it to the subset consisting of both a and b. The output is either a or b. Now apply the permutation that swaps a and b. The subset itself remains the same, so a selection rule that is natural under this permutation would have to return an element that the swap leaves fixed. Neither a nor b is fixed. Contradiction.

Notice the limits of the proof. It rules out a natural selection rule on this category of arbitrary sets and functions, or even on sets and bijections. It does not rule out choosing the least element of every finite nonempty subset of a totally ordered set, provided the arrows preserve sufficient order structure. The result is a theorem about a specified collection of permissible transformations.

The same reasoning clarifies the relation between naturality and symmetry. If an object has many automorphisms, a natural choice must be compatible with all of them. Highly symmetric objects often admit few distinguished choices. This is one way to turn the vague objection 'that depends on coordinates' into a clean proof that no coordinate-free selection exists under the stated symmetry group.

## A natural comparison that is not an isomorphism

Let's return to the support map from finite lists to finite subsets. It is natural because mapping each entry before forgetting order and multiplicity yields the same finite subset as forgetting order and multiplicity before taking the direct image. But the map is far from invertible.

Suppose A has two elements, red and blue. The lists red-blue and blue-red have identical support, and so do red-red-blue and red-blue. The support map loses order and repetition. There is no function back from finite subsets to finite lists that would invert support on every list, because the same subset has many preimages.

Could we at least choose one list for every finite subset naturally? If we try to list the elements of a two-element set in some order, an automorphism swapping the elements prevents any choice from being compatible with all permutations. For an empty subset, choosing an empty list is easy. For a singleton, choosing the one-element list is easy. For a two-element set, the symmetry obstruction appears.

This gives two distinct reasons that a construction may fail to be a natural isomorphism. One is ordinary noninvertibility of its component maps, as with support. Another is failure to make compatible choices even when we have pointwise isomorphisms available, as with arbitrary enumerations of finite sets. Keeping these reasons separate helps in algebra, where objectwise isomorphism is common but natural isomorphism is a more demanding conclusion.

## Functor categories make diagrams into objects

We have already described vertical composition of natural transformations. We can push this one step further. For two fixed categories C and D, consider all functors from C to D as the objects of a new category, and natural transformations as its arrows. This construction is called a functor category, often denoted by brackets around C and D.

Its identity transformation at a functor F assigns the identity arrow of F of A to each A. The naturality condition holds because composing with identities changes nothing. Given transformations from F to G and from G to H, their vertical composite is natural, as we proved. Associativity of vertical composition follows from associativity of arrows in D. Therefore the functors and natural transformations satisfy the category axioms.

A particularly vivid instance arises when C is a category describing a small diagram shape and D is Set. A functor from C to Set is a diagram of sets of that shape. A natural transformation is then a compatible map between two such diagrams. In other words, an entire interconnected dataset can act as one object, and a coherent translation between datasets acts as an arrow.

Suppose C consists of two objects, Source and Target, with one arrow from Source to Target. A functor from C to Set is simply a function between two sets. A natural transformation between two such functors consists of a function on their sources and a function on their targets that make a square commute. The familiar notion of a morphism between functions has emerged directly from naturality.

If you have ever changed an input representation and an output representation simultaneously, this square states what it means for the original computation and the translated computation to agree. The category theory does not do the data migration for you; it identifies the coherence equation the migration must satisfy.

## A numerical double-dual check

Take a two-dimensional real vector space with coordinates x and y. A vector v has coordinates two and three. A linear functional phi sends a vector with coordinates x,y to four times x minus y. Evaluating phi on v gives eight minus three, or five. The canonical map from the vector space to its double dual sends v to the operation that returns this evaluation for every phi.

Now apply a linear map T that sends x,y to x plus y and y. The image of v has coordinates five and three. A functional psi on the target that returns its first coordinate evaluates T of v to five. Alternatively, pull psi back along T: its pullback on the source sends x,y to x plus y. Evaluate that pulled-back functional on v, and the answer is again five.

The agreement is the naturality square for double dual evaluation. The calculation is simple, but it shows why the construction is independent of a basis choice. We did not identify v with an arbitrary coordinate functional; we used the way every linear functional evaluates v. The compatibility with T is built into composition of functions.

This is an example of how naturality can do more than provide terminology. It determines which comparisons can be used consistently across a family of changing objects, and it lets us prove that consistency by one equation rather than a long catalog of special cases.

## What the square is really asking

A naturality square turns a broad claim of consistency into one small equation repeated across all arrows. Its strength comes from quantification. We must check every arrow in the source category, not merely every object and not merely one favorite example.

In programming, the idea can illuminate polymorphic operations, though there are important caveats about which mathematical model of programs we use. A transformation that treats values uniformly may satisfy an analogue of naturality. Side effects, runtime type inspection, partial functions, and nontermination can change the setting, so slogans about uniform behavior do not substitute for a specified category and proof.

In algebra and geometry, the applications are more direct. Constructions should commute with structure-preserving maps. If we build a quotient or assign a group to a space, the value of the construction is only part of the story. Its behavior under arrows determines whether it is truly functorial, and the compatibility of two such constructions determines whether they are naturally related.

A natural transformation therefore gives us a precise answer to the question with which we began. Changing the names first and then forgetting duplicates has the same effect as forgetting duplicates first and then changing the names. We can express the same consistency in a vast number of mathematical situations. The key is to compare two paths and demand equality for every arrow. A diagram that commutes everywhere is a statement about a construction that behaves coherently across an entire mathematical world.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(F,G:\mathcal C\to\mathcal D\). A natural transformation \(\alpha:F\Rightarrow G\) has components \(\alpha_A:FA\to GA\), satisfying \(G(f)\circ\alpha_A=\alpha_B\circ F(f)\) for every \(f:A\to B\).

**List support:** \(\operatorname{supp}_A:L(A)\to P_{fin}(A)\) is natural because \(P_{fin}(f)(\operatorname{supp}(\ell))=\operatorname{supp}(L(f)(\ell))\).

**Double dual:** \(\eta_V:V\to V^{**}\), \(\eta_V(v)(\varphi)=\varphi(v)\); naturality \(T^{**}\eta_V=\eta_W T\). The map is an isomorphism for finite-dimensional \(V\). For general algebraic vector spaces it is typically not onto.

**Invertible components theorem:** If each \(\alpha_A\) is invertible, apply \(\alpha_B^{-1}\) on the left and \(\alpha_A^{-1}\) on the right of the naturality equation to obtain \(F(f)\alpha_A^{-1}=\alpha_B^{-1}G(f)\).

### Exercises and answers

1. **Exercise:** Is reversal of finite lists a natural transformation \(L\Rightarrow L\)? **Answer:** Yes; reversing a list commutes with mapping an arbitrary function over entries.
2. **Exercise:** Is sorting a list of arbitrary elements natural in Set? **Answer:** There is no specified order on an arbitrary set, so no such sorting operation is defined without added structure.
3. **Exercise:** Is taking the head of every list a natural map \(L\Rightarrow I\)? **Answer:** No; the empty list has no head. It works instead for the nonempty-list functor.

### References

- Samuel Eilenberg and Saunders Mac Lane, “General Theory of Natural Equivalences” (1945), https://doi.org/10.1090/S0002-9947-1945-0013131-6
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- David Eisenbud, recollections, https://mathshistory.st-andrews.ac.uk/Extras/MacLane_Eisenbud/
