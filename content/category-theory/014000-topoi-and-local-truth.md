# 014000 — Topoi: Mathematical Universes with Local Truth

**Track:** An Introduction to Category Theory. **Background:** sets, functions, products, universal properties, predicates as subobjects, and the notion of a sheaf. **Theme:** derive generalized truth values from the structure of sheaf categories and distinguish classical from intuitionistic logic.

<!-- BEGIN SPOKEN LECTURE -->

# Topoi: Mathematical Universes with Local Truth

Suppose a mathematician asks whether a proposition is true. We are accustomed to a simple choice: true or false. For an ordinary statement about a finite set, that works well. An element either belongs to a specified subset or it does not. But imagine a statement whose meaning depends on the region of a space in which we are working. It might be supported over one open area, fail to be established over a larger area, and become valid again when we restrict our attention to a smaller region.

This is not an invitation to make logical truth subjective. It is an invitation to ask what a mathematical truth value must look like when the objects being studied are themselves local data, with restriction maps and gluing rules. Category theory offers a disciplined answer through structures called topoi.

A topos has much of the organizational machinery of the category of sets, including products, functions, and a way to classify subobjects. But in a sheaf topos the truth values can reflect the topology of a space. We can make this exact using a tiny example with only two points.

## Begin with what makes Set behave like a universe

The category Set contains sets as objects and functions as arrows. It has a terminal object, any one-element set. It has products, such as ordered pairs. It has equalizers, which select elements on which two functions agree. It also has function spaces: the set of functions from A to B, conventionally written B to the A, behaves as an exponential object.

The less obvious construction is the subobject classifier. Take a subset S of a set A. Its membership information can be encoded as a function from A to the two-element set consisting of false and true. The function sends elements of S to true and other elements to false. The subset can be recovered as the inverse image of true.

This is a universal property. The inclusion of S into A is, up to the appropriate notion of equality, the pullback of the inclusion of the one-element true object into the two-element truth-value object. Every subobject receives a unique classifying map.

In Set the object of truth values has two elements. But what if the objects of a category are not ordinary sets? What if they are sheaves of sets, whose elements can vary across open regions of a space? The structure of classification can survive, while the classifier takes a different form.

An elementary topos is a category with finite limits, exponentials, and a subobject classifier. The category Set is one. Categories of sheaves on topological spaces are important examples. This definition is a structural contract; it does not say that every topos is literally a category of sheaves on an ordinary topological space.

## A tiny topological space with a strange feature

Take a space X with two points, p and q. Declare that its open sets are the empty set, the singleton containing p, and the whole space X. The singleton containing q is *not* open. This is a legitimate topology, often called the Sierpiński space.

In a usual line, each point has arbitrarily small open neighborhoods. In this finite example, q has only one open neighborhood, the entire space. The point p has the smaller neighborhood consisting of p alone. That asymmetry is what will make our logic interesting.

Imagine a proposition that is established precisely on the open region containing p alone. Its region of validity is U, the singleton p. We might ask what it means for this proposition to be false. In classical set logic the complement contains q, so we would expect its negation to hold precisely at q.

But the singleton q is not open. In a framework where truth is expressed by open regions, there is no nonempty open region on which the proposition can be certified as everywhere false. The largest open subset disjoint from U is empty. So the internal negation of U is empty.

We now have a surprising calculation. U is not the entire space. Its negation is empty. The union of U and its negation is just U, not the whole space. The law of excluded middle, which would say a proposition or its negation always holds, has failed in this open-set logic.

This is a precise mathematical example. We are not asserting that the external proposition 'p belongs to U' lacks a Boolean truth value. As ordinary set theorists outside the model, we know whether p and q belong. The result concerns the internal logic induced by the lattice of open regions and, ultimately, by the sheaf category built over the space.

There is a useful count we can perform at each stage. Over X, Omega has three sections, one for each open subset of X. Over the smaller open U, Omega has only two sections, empty and U itself. The restriction from X to U sends empty to empty, U to U, and X to U. So two distinct truth values at the global stage can become indistinguishable after restriction. This is not a flaw in the construction. It expresses precisely that a smaller region can forget distinctions that only exist outside it. A listener can check the entire behavior of the classifier with these three global sections and two local sections, without needing any advanced machinery.

## Why open sets support a logic

The open subsets of any topological space form a partially ordered collection under inclusion. Intersections of finitely many open sets are open, so they can represent conjunction. Arbitrary unions of open sets are open, so they can represent disjunction, including infinite disjunctions.

Implication takes more thought. For open regions U and V, we want the largest open region W with the property that W intersect U is contained in V. This W is the interior of the union of the complement of U with V. It plays the role of 'U implies V'. Negation is the special case 'U implies false', which becomes the interior of the complement of U.

This structure is a Heyting algebra. In a Boolean algebra every proposition U has a complement that behaves as an internal negation, and excluded middle holds. In the open-set Heyting algebra, negation need not be a set-theoretic complement. We retain precise rules for conjunction, disjunction, implication, and negation, but some classical identities require additional assumptions.

Let's redo the two-point calculation. The open sets are empty, U, and X. The complement of U is the singleton q, which is not open. Its interior is empty. Therefore not U equals empty. U or not U is U. That is a strict subset of X. The calculation proves that this Heyting algebra is not Boolean.

The example is small enough to check entirely by hand, but it captures a general phenomenon. Local validity has different logical behavior from ordinary two-valued membership. Which statements are true can depend on how they restrict to smaller pieces, and the logical operations must respect those restrictions.

## Where sheaves enter

We need to connect this lattice calculation to an actual category. Let Sh of X denote the category of sheaves of sets on X. An object assigns sections to open regions and satisfies the gluing condition. An arrow is a family of functions on sections that commutes with restriction.

The terminal sheaf assigns exactly one section to every open region, including the empty region. Think of it as the sheaf with no choices to make. A subobject of this terminal sheaf records on which open regions its unique section is allowed to appear.

Every open subset U of X determines such a subterminal sheaf. On an open region V contained in U, there is one allowed section; on an open region not contained in U, there are none. If a family of regions covers V and each lies within U, their union V lies within U, so the gluing condition behaves correctly.

This gives a correspondence between open subsets of X and subobjects of the terminal sheaf. In particular, for the Sierpiński space, the subobjects of one form the same three-element Heyting algebra we just calculated. Our open-set logic is therefore more than a convenient analogy: it is the logic of global truth values in a category of sheaves.

In Set the terminal object has two subobjects, corresponding to false and true. In Sh of X, it can have more. On the Sierpiński space it has three, reflecting the available open regions. The richer logic follows from the structure of the category.

## The truth-value sheaf

We can go further and describe the subobject classifier itself. In the sheaf category over X, the classifier Omega assigns to each open region V the set of open subsets of V. Restrictions are given by intersection: if we restrict a truth value W inside V to a smaller region T, we obtain W intersect T.

The true map from the terminal sheaf into Omega selects the entire region V at every stage V. A subobject of any sheaf can then be classified by a map into Omega, just as a subset of an ordinary set is classified by a function to false and true.

Why does Omega contain *all* open subsets of V? A section may satisfy a predicate only on part of the region where the section is defined. Its classifying truth value records the open subregion on which the predicate holds. Restrict the section to a smaller region, and the truth value restricts by intersection. The construction respects the local nature of the data.

To check the principle in a simple case, take the subterminal sheaf associated with U. Its classifying map sends the unique section over V, when we evaluate the terminal sheaf, to the open subset V intersect U. If V lies entirely in U, the truth value is all of V. If V lies outside U in the sense of having no nonempty open intersection, the truth value is empty. Intermediate regions record partial validity.

This is a genuine universal construction. We are not making up a menu of many-valued logic out of preference. The available truth values are derived from how subobjects and pullbacks work in the category of sheaves.

## What becomes of 'there exists' and 'for every'?

The connection with logic extends beyond individual predicates. In Set, a function f from A to B lets us pull predicates on B back to predicates on A. There are also existential and universal operations along f. Existential image asks whether some element in the fiber satisfies a predicate. Universal image asks whether all elements in the fiber satisfy it.

In many categorical settings, including elementary topoi, suitable adjunctions express these quantifiers. Pullback corresponds to substitution. The existential construction is its left adjoint, and the universal construction is its right adjoint, in the appropriate subobject order.

The directions matter. For a predicate P on A and Q on B, existential image of P is below Q exactly when P is below the pullback of Q. This is the universal property of the smallest predicate on B that includes all images of P. Universal image is the largest predicate on B whose pullback lies inside P.

The same architecture underlies ordinary finite-set quantification and the logical operations in a sheaf topos. But the resulting truth values and inference rules can differ because the underlying category differs. Generalizing a mathematical concept responsibly means carrying along the assumptions that make each adjunction exist.

## Double negation exposes another difference

The two-point example lets us go one step further. We calculated that the internal negation of U, the singleton containing p, is empty. What is the negation of that empty open set? Its complement is all of X, whose interior is all of X. Therefore double negation of U is X.

In classical Boolean logic, a proposition and its double negation are equivalent. In this open-set logic they differ: U is a proper open subset of X, while double negation U is the whole space. So the model validates one direction—U implies not not U—but not the converse for every proposition.

Why is that reasonable in a local interpretation? The absence of an open region where U is definitely false is weaker than possessing evidence for U on the entire space. A proposition may resist refutation everywhere locally without having been established everywhere. Double negation captures that distinction in a precise algebraic way.

Do not extend the intuition recklessly. The open subset U itself is entirely well-defined as a set. There is no ambiguity about which points it contains. What changes is the interpretation of the logical operations when truth values are required to be open and to respect restriction. The algebra is a mathematical consequence of that requirement.

Now compare a discrete two-point space. There every subset is open. The interior of a complement is just the complement, so excluded middle and double-negation elimination hold in the open-set algebra. The contrast shows that classicality depends on the topology in the sheaf examples, even though both spaces have exactly two underlying points.

## Classical reasoning still has its place

It would be a mistake to conclude that the law of excluded middle is somehow refuted for all mathematics. In the ordinary category Set, the subobject classifier is the two-element Boolean object, and classical reasoning is available. The sheaf model demonstrates that the basic structural definition of a topos does not *force* classical logic.

An elementary topos has intuitionistic internal logic in general. Some topoi are Boolean, meaning that their internal logic validates excluded middle. Others are not. Classical reasoning can also be added as an assumption in an appropriate formal environment, but that choice changes what can be deduced without proof.

A constructive proof often provides witnesses or constructions where a classical argument might rely on an alternative asserted without a witness. Topos theory supplies mathematical models in which such distinctions have concrete content. Yet one should not imagine that every constructive proof can be read as a program with no further qualifications. Computational interpretations depend on the particular logic, type theory, and semantic model chosen.

Topos theory is a bridge between geometry and logic because it lets us study mathematical worlds in which location, variation, and inference are connected by categorical structure.

## A glimpse of the historical development

The theory emerged through several lines of mathematical work. Alexander Grothendieck's school used sheaf categories and generalized coverings as organizing tools in algebraic geometry. Later, F. William Lawvere and Myles Tierney developed the elementary, axiomatic viewpoint in which the logical structure of a topos becomes central.

These were connected developments rather than one instant invention. The geometric side needed a way to study objects locally and reconstruct global behavior. The logical side recognized that categories with certain universal properties already contain interpretations of logical operations. Their meeting opened a broad field of research across geometry, logic, and foundations.

The historical names can make the subject sound remote. But the simplest example is still our two-point space. You do not need algebraic geometry to check that its opens form a three-element Heyting algebra. The advanced theory grows from the decision to treat such calculations as structural, not accidental.

## Maps into Omega make predicates behave naturally

Let's unpack the characteristic map once more with the two-point space. Take the proposition associated with U. At the largest region X, its truth value is U itself. Restrict attention to the smaller open region U, and the truth value becomes U intersect U, which is the whole smaller region. At that stage the proposition is completely true. We have changed the context by restriction, and the truth value has changed by exactly the rule required of a sheaf morphism.

If instead we classify the empty subobject, its truth value on every region V is empty. If we classify the terminal sheaf itself, the value on V is all of V. Those behave as false and true in every local context. The intermediate case U is what enriches the logic.

The classifier is therefore doing something very concrete. It records how membership in a subobject changes across restrictions while preserving the maps that relate those regions. This is why it would be wrong to treat Omega merely as a bag of unrelated truth labels. Its sections and restriction maps are the structure that makes local semantics coherent.

## What a topos does not give us automatically

A topos is a mathematical setting with a specified collection of constructions. It does not provide a solution to every local-to-global problem. A sheaf may have no global section even while having many local sections. A topos need not have the same classical truth principles as Set. And describing a system as a category does not by itself establish that it has finite limits, exponentials, or a subobject classifier.

The word 'universe' is a helpful metaphor if used carefully. Objects and arrows in a topos support a coherent internal mathematics, but a particular topos may differ sharply from familiar sets in what it can express or prove internally. We must determine which laws hold instead of importing them by habit.

The Sierpiński example makes this discipline tangible. The truth region U is neither empty nor the entire space. Its internal negation is empty. The failure of U or not U to cover X follows from the topology and the definition of implication. There is a definite calculation behind the philosophical-sounding conclusion.

## A different way to ask about truth

Return to the opening question: can a proposition have more structure than being simply true or false? In an ordinary set-based model, membership is two-valued. In a sheaf category, the truth of a predicate on a section can be recorded by the open region where it holds. Gluing and restriction make that assignment coherent.

The step from sets to sheaves is not a rejection of mathematical rigor. It is an extension of rigor to situations where information varies over space. The step from sheaves to topoi asks which categorical features are responsible for that coherent logic, and which other mathematical environments share them.

We have now seen how a category can carry its own interpretation of propositions, implication, and quantification. The same tools that began with products and pullbacks can describe truth varying locally. The resulting question is larger than whether a statement is true at one isolated point: it is how mathematical claims behave under restriction, combination, and reconstruction. Topos theory makes that question a subject of mathematics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Elementary topos.** A category \(\mathcal E\) with finite limits, exponentials, and a subobject classifier \(\mathrm{true}:1\to\Omega\). This supports cartesian closed structure and internal higher-order intuitionistic logic.

**Sierpiński space.** \(X=\{p,q\}\), \(\mathcal O(X)=\{\varnothing,U,X\}\) with \(U=\{p\}\). The Heyting operations on opens are \(U\wedge V=U\cap V\), \(U\vee V=U\cup V\), \(U\Rightarrow V=\operatorname{int}((X\setminus U)\cup V)\). For this particular \(U\), \(\neg U=\operatorname{int}(X\setminus U)=\varnothing\), hence \(U\vee\neg U=U\ne X\).

**Sheaf classifier.** In \(\operatorname{Sh}(X)\), \(\Omega(V)=\mathcal O(V)\). Restriction along \(T\subseteq V\) sends \(W\) to \(W\cap T\). The true map selects \(V\in\Omega(V)\).

**Subterminal sheaves.** For \(U\in\mathcal O(X)\), define \(1_U(V)=\{*\}\) if \(V\subseteq U\), otherwise \(1_U(V)=\varnothing\). Its canonical map to \(1\) is monic. Every subobject of \(1\) arises this way, up to isomorphism, and \(\operatorname{Sub}_{\operatorname{Sh}(X)}(1)\cong\mathcal O(X)\).

**Predicate classification.** A mono \(S\hookrightarrow A\) is the pullback of \(\mathrm{true}:1\to\Omega\) along a unique \(\chi_S:A\to\Omega\). For \(1_U\hookrightarrow1\), \(\chi_U(V)(*)=V\cap U\).

**Quantifier adjunctions.** For \(f:A\to B\), under the appropriate subobject semantics, \(\exists_f\dashv f^*\dashv\forall_f\). In Set they reduce to existential and universal images over fibers.

### Exercises with answers

1. **Exercise:** List the open sets of the Sierpiński space. **Answer:** \(\varnothing,\{p\},X\).
2. **Exercise:** Compute \(\neg\{p\}\) in its open-set Heyting algebra. **Answer:** \(\operatorname{int}(\{q\})=\varnothing\).
3. **Exercise:** What is \(\Omega(V)\) in the sheaf topos of a space? **Answer:** The collection of open subsets of \(V\), restricted by intersection.
4. **Exercise:** Does an elementary topos have to be Boolean? **Answer:** No. \(\operatorname{Sh}(X)\) for the Sierpiński space supplies a non-Boolean example.

### References

- The Stacks Project, *Sites and Sheaves*, sections on sheaves and topoi, https://stacks.math.columbia.edu/download/sites.pdf
- The Stacks Project, *Sheaves on Spaces*, https://stacks.math.columbia.edu/browse
- Steve Awodey, *Category Theory* and *Categorical Logic* course notes, https://awodey.github.io/catlog/
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic*.
- nLab, “subobject classifier,” https://ncatlab.org/nlab/show/subobject%20classifier
