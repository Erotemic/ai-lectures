# 012000 — Categorical Logic: When Maps Behave Like Proofs

**Track:** An Introduction to Category Theory. **Background:** functors, products, adjunctions, universal properties. **Theme:** propositions as subobjects, implication as exponentiation, quantifiers as adjoints, and constructive logic.

<!-- BEGIN SPOKEN LECTURE -->

# Categorical Logic: When Maps Behave Like Proofs

Consider a claim about a number: it is even. We can treat that sentence as something to mark true or false. But we can also ask what mathematical structure a predicate creates. Given a set of numbers, the predicate singles out those numbers for which it holds. It defines a subset. If we change the numbers by a function, the predicate can be pulled backward to the original domain. If we combine two predicates, we can intersect their satisfying sets. If we quantify over values of a function, we obtain new predicates on its output.

These ordinary operations suggest a surprising connection. Much of logic can be studied using categories, maps, products, and universal properties. The connection is not simply that we can label truth values with objects. It is that logical operations can be characterized by relationships among arrows. In suitable categories, proofs and programs can be represented by morphisms; conjunction, implication, and quantification have categorical meanings.

This is **categorical logic**. We will approach it through finite sets, where every equation can be checked by listing elements. Then we will look at a mathematical setting in which some classical logical laws fail even though a coherent logic remains. The goal is to see how the category determines which forms of reasoning it supports.

## A predicate is a collection of allowed inputs

Let A be the finite set containing zero, one, two, and three. The predicate 'is even' is satisfied by zero and two. We can represent it by the subset E consisting of those two elements. The predicate 'is positive' corresponds to P containing one, two, and three. Both are conditions on elements of A.

Their conjunction means 'even and positive.' Its satisfying set is the intersection of E and P, containing only two. Their disjunction means 'even or positive.' Its satisfying set is the union of E and P, containing every element of A. Negation of 'even' gives the complementary subset, one and three.

That may look like elementary set theory, and it is. But we can reinterpret inclusion of a subset into A as a morphism. The map from E into A sends each even number to itself. It is a **monomorphism**: two inputs cannot become the same output. Two injections into A can describe the same predicate even if their domains have different names, so we identify subobjects up to the appropriate isomorphism over A.

A subobject is a categorical way to talk about a predicate on A. In Set, subobjects correspond exactly to subsets. In other categories, a subobject may be something more general, such as a subspace, a substructure, or a suitable notion of varying property.

Now suppose f maps a set X into A. If E describes the even elements of A, what should 'f of x is even' mean as a predicate on X? It selects precisely the elements x whose images land in E. That is the inverse image of E under f. Categorically, it is obtained by a pullback of the inclusion E into A along f.

The pullback construction explains why substitution of variables is structurally fundamental. Changing the input by a function should transport a property in the opposite direction. Properties on the output become properties on the input by asking whether the transformed value satisfies them.

## An example of substitution

Take X to contain the labels a, b, and c. Let f send a to zero, b to one, and c to two. The predicate even on A was satisfied by zero and two. Pulling it back along f yields the subset containing a and c. The new predicate is exactly 'f of the label is even.'

Now suppose g sends a different set Y into X. Pulling back the even predicate along f and then along g gives the same condition as pulling it back along f after g. This is the functoriality of inverse image: preimages respect composition. It is also the mathematical law behind substituting one expression into another in a logical formula.

The direction is worth emphasizing. A function f goes from X to A. A predicate on A pulls back to a predicate on X. Therefore predicate substitution is contravariant in the underlying function. This reversed arrow direction is not a technical annoyance; it expresses how conditions on outputs become tests on inputs.

In Set the inverse image also preserves intersections, unions, and complements. For example, pulling back the conjunction of even and positive gives exactly the conjunction of the two pulled-back predicates. This can be verified one element at a time: f of x satisfies both conditions if and only if it satisfies each separately.

Other categories may support different combinations of logical operations. We cannot assume that every category has subobjects, pullbacks, or the same propositional laws. Categorical logic asks which structural hypotheses justify each logical rule.

## Products as conjunction, functions as implication

There is another way to read logical operations, often associated with the correspondence between propositions, types, and proofs. Suppose A is a type of evidence for one proposition and B a type of evidence for another. Evidence for 'A and B' is a pair: one piece of evidence of type A and one of type B. That is the product type A times B.

The universal property of a product expresses the proof rule precisely. To construct a map from X into A times B, it is necessary and sufficient to construct one map from X into A and another from X into B. If X represents assumptions or available data, producing both conclusions is exactly what a proof of a conjunction requires.

The terminal object corresponds to a trivially inhabited unit type: for every X there is a unique map to it. In Set that terminal object is a singleton. In a type-theoretic reading, there is exactly one canonical piece of unit evidence. This is a different viewpoint from viewing a proposition solely as a subset of a fixed domain, though the two are related in richer categorical settings.

What about implication? If we have evidence of A, and a proof that A implies B, we should obtain evidence of B. A function from A to B does exactly that. In Set, the collection of all such functions is itself a set, written B to the A power, or B raised to A. More generally, a **cartesian closed category** has an exponential object B to the A, characterized by a natural correspondence between maps from X times A into B and maps from X into B to the A.

This is called currying. A function that accepts two inputs, one from X and one from A, can be converted into a function that accepts X and returns a function from A to B. The two styles carry the same information.

Take A to be the two-element set zero and one, B to be the two-element set false and true, and X to be a singleton. A function from X times A to B is exactly a truth table with one Boolean output for each of the two A-values. There are four such functions. A function from X to the function set B to the A is a choice of one of those four truth tables. Currying gives a bijection between the choices.

The existence of exponential objects is an extra property. A category can have products without having the objects needed to represent all function-like maps this way. That is why the categorical account of implication requires hypotheses rather than appearing in every category automatically.

## Deriving the evaluation rule

Let us unpack one arrow that a cartesian closed category guarantees. Given an exponential B to the A, there is an evaluation map from the product of B to the A with A into B. It takes a function and an input and returns the function's output at that input.

Suppose we have a map h from X times A into B. Currying produces a map from X into B to the A. Compose that with the identity on A and then evaluate. The result is the original h. This is the categorical beta rule: abstracting a function and then applying it recovers the original computation.

There is also an eta rule: if you take an existing function-like value, evaluate it on a variable, and abstract back over that variable, you recover the original function-like value. Both laws are statements of the universal property of the exponential.

These equations explain a close relationship among the typed lambda calculus, programming-language function types, and cartesian closed categories. A mathematical model can interpret an expression with a free variable as a morphism, and function abstraction as the transpose given by currying. But a specific programming language may have partial functions, side effects, recursion, or evaluation rules that require richer semantics. The cartesian closed model directly describes a pure total fragment, not every program execution.

## Truth values as arrows

So far predicates appeared as subsets. Can truth values themselves be expressed categorically? In Set, there is a two-element set containing false and true. For each subset E of A, define a characteristic function from A to the two-element truth-value set. It returns true on elements of E and false otherwise.

Conversely, every such function determines a subset by taking the inverse image of true. There is a universal square behind this correspondence: the inclusion of the one-element true set into the two-element set classifies every subset inclusion by pullback.

An object with this classifying property is called a **subobject classifier**. Its role is sometimes denoted by the Greek letter omega. A subobject classifier is more than 'an object with truth values': it includes a designated truth arrow from the terminal object and a universal property for monomorphisms.

In Set, omega has exactly two elements. But in an arbitrary category with a subobject classifier, omega need not behave as a two-element Boolean set. It may encode a richer notion of truth, including stages of information or local validity.

This leads to a subtle lesson about mathematical logic. Classical two-valued logic is natural in Set. The categorical definition of a truth-value object does not force every model to have classical negation or the law of excluded middle.

## Quantifiers arise as adjoints

Let's return to our finite subsets and functions. Let f map A to B. A predicate P on A can be projected forward to a predicate on B in two different ways. One asks whether **some** input over b satisfies P. The other asks whether **every** input over b satisfies P.

Define the existential image of P to contain those b that have at least one preimage lying in P. Define the universal image of P to contain those b for which every preimage lies in P. The universal condition is true when there are no preimages, by the ordinary convention that a statement about every element of an empty set is vacuously true.

Consider an explicit example. Let B consist of the labels left, right, and unused. Let A have three values a-one, a-two, and b-one. Send both a-values to left and b-one to right. Nothing maps to unused. Let the predicate P hold on a-one and b-one, but not on a-two.

The existential image of P contains left and right. Left qualifies because a-one satisfies P; right qualifies because b-one does. Unused does not qualify because it has no witnesses.

The universal image contains right and unused. Every element over right satisfies P because the only one is b-one. Left fails because a-two is a counterexample. Unused qualifies because its fiber is empty and therefore contains no counterexample.

These two constructions are characterized by adjunctions. Inverse image along f takes a subset of B back to a subset of A. Existential image is left adjoint to inverse image, while universal image is right adjoint to inverse image.

To see the left adjunction concretely, the statement 'the existential image of P is contained in Q' is equivalent to 'P is contained in the inverse image of Q.' Both say that every element satisfying P maps into Q. The right adjunction says that 'the inverse image of Q is contained in P' is equivalent to 'Q is contained in the universal image of P.' Both say that every input lying over a Q-value satisfies P.

This is an important conceptual bridge. Quantifiers are not arbitrary extra symbols pasted onto a category. In suitable categorical settings, they are determined by universal mapping relationships with substitution. Logical operations and categorical adjunctions describe the same order-theoretic constraints.

## Why quantifier direction matters

The words 'left' and 'right' in these adjunctions are easy to mix up. We can derive the direction from a test case. Suppose P is true of one input that maps to left. Existentially quantifying over the fiber puts left into the output condition. That is the smallest predicate on B whose inverse image contains P. This minimality corresponds to the left adjoint.

By contrast, the universal image is the largest predicate on B whose inverse image is contained in P. It includes every b for which pulling back that single b-value produces only inputs satisfying P. This maximality corresponds to the right adjoint.

Take the previous example and let Q contain only left. Its inverse image contains both a-one and a-two. Since P lacks a-two, Q is not contained in the universal image of P. The right-adjoint criterion correctly rejects it. But the existential image of P still includes left because it needed only the witness a-one.

This calculation is small enough to keep in mind when the notation becomes complicated. An existential condition needs a witness. A universal condition needs the absence of a counterexample. Both can be recovered from how predicates behave under inverse image.

We should not automatically generalize the elementary Set construction to any category with arrows. General categorical quantification requires the necessary subobject structures and adjoints, with appropriate stability laws if it is to interpret substitution and first-order logic consistently.

## When classical negation fails

Let us now build a concrete logical structure where every proposition has a sensible interpretation but excluded middle fails. Consider a small topological space X with two points, which we will call open and closed merely as labels. Choose the open subsets to be the empty set, the singleton containing the first point, and the whole space. These three sets are closed under finite intersections and arbitrary unions, so they form a topology.

Treat open subsets as propositions. The intersection of opens serves as conjunction and their union serves as disjunction. But the complement of the singleton open set is the other singleton, which is not open. So ordinary set complement is not available as a negation within the lattice of open sets.

Instead define implication of two opens U and V as the largest open W such that W intersect U is contained in V. A concrete formula is the interior of the union of the complement of U with V. Negation of U is implication from U to the empty open set: the largest open disjoint from U.

Choose U to be the singleton containing the first point. Every nonempty open set intersects U, so the largest open disjoint from U is empty. Thus not U is empty. The disjunction U or not U is just U, which is not the whole space. The law of excluded middle fails in this algebra of open-set propositions.

This does not make the logic incoherent. It is a **Heyting algebra**, which validates intuitionistic propositional reasoning. Its implication is characterized by an adjunction with conjunction, rather than by assuming a Boolean complement. Double negation also need not return the starting proposition: not not U is the whole space here, larger than U.

The example warns us against a common overstatement. A different logical model is not necessarily one where 'anything can be true.' It can have precise inference laws, a definite mathematical semantics, and counterexamples to particular classical principles. The category or lattice tells us which rules hold.

## What do topoi contribute?

A topos is a category with substantial structure; an elementary topos has finite limits, exponentials, and a subobject classifier. The category Set is a central example. Categories of sheaves on suitable spaces also form topoi, but their internal truth values can reflect the local structure of the space rather than a global yes-or-no test.

The internal logic of a general elementary topos is intuitionistic rather than necessarily Boolean. In a sheaf model, a statement may hold locally over some open regions without holding everywhere. Gluing and restriction become parts of the semantics. We need additional lectures to explain sheaves properly; here it is enough to understand why the categorical study of predicates can lead beyond classical two-valued logic.

A distinction matters: the Heyting algebra of open subsets in our two-point example is a useful model of intuitionistic propositional logic. It is not by itself a proof that the category of all open subsets, viewed merely as a poset, is an elementary topos. To make categorical assertions about sheaves or topoi, we must specify the relevant category and check its structure.

This kind of careful separation is valuable throughout the subject. A subobject can behave like a predicate. An exponential can behave like implication. Quantifier operations can be adjoints. But each statement depends on the categorical constructions actually available. The correspondences are theorems in suitable settings, not licenses to rename every arrow as a proof.

## A worked proof-theoretic example

Let's combine the ideas in a very small logical program. Suppose A is a type of sensor readings and B is a type of alert messages. A rule r from A to B says how to turn an accepted reading into a message. Another map s from B to C converts messages into actions. Their composite s after r turns a reading into an action.

In a proof-as-programs interpretation, the type A represents a proposition whose evidence is a value of A. The function r is a construction that turns evidence of A into evidence of B, so it witnesses the implication A implies B. The function s similarly witnesses B implies C. Composing them witnesses A implies C.

If we also have another rule t from A to D, the pair r,t gives a map from A into B times D. It witnesses that evidence of A is sufficient to construct both B-evidence and D-evidence. The product's universal property guarantees that this pairing is uniquely determined by its two projections.

The category-theoretic explanation is straightforward: composition models chaining proofs, and products model combining proofs. But we must keep the interpretation honest. An arbitrary program might diverge or depend on an external sensor in a way that a simple total function model does not capture. The categorical structure is a semantics of a chosen formal fragment.

This is the discipline that gives the theory its strength. The connection between logic and categories is precise enough to test examples, recover proof rules, and locate the boundary where a richer model is needed.

## The idea in one return to a predicate

Return to the finite set A containing zero, one, two, and three. 'Is even' was a subobject. Pulling it back along a function was substitution. Intersecting it with 'is positive' was conjunction. Taking existential and universal images along a map produced quantifiers. Once we pass to function types, the exponential supplies a universal construction for implication-like behavior. A subobject classifier explains how predicates correspond to characteristic maps.

Each step translates an operation familiar from logic into a structural feature of a category. This translation makes the rules portable. It lets us ask, in a new mathematical setting, which logical operations exist and which inferences they support, instead of assuming that every setting behaves like finite subsets of a set.

The resulting perspective is powerful precisely because it has limits. Classical logic works in Set. Intuitionistic logic arises naturally in many categories of spaces and varying data. Typed functional programs can be studied in cartesian closed categories, while richer computational effects call for additional constructions.

Category theory has not made logic disappear into arrows. It has revealed a deep source of logical laws: the ways mathematical objects can be mapped, paired, classified, and quantified. The structures we choose determine the forms of reasoning we can carry out.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Subobjects in Set.** The subobjects of a set \(A\) are represented by injections \(E\hookrightarrow A\), up to isomorphism over \(A\); they correspond to \(\mathcal P(A)\). The pullback along \(f:X\to A\) gives \(f^{-1}(E)\subseteq X\).

**Cartesian closure.** An exponential \(B^A\) represents the functor \(X\mapsto\mathcal C(X\times A,B)\). Thus \(\mathcal C(X\times A,B)\cong\mathcal C(X,B^A)\) naturally in \(X\). Evaluation \(\mathrm{ev}:B^A\times A\to B\) supplies beta/eta rules.

**Subobject classifier.** In Set, \(\Omega=\{\bot,\top\}\) and \(\mathrm{true}:1\to\Omega\). For each mono \(E\hookrightarrow A\), there is a unique characteristic map \(\chi_E:A\to\Omega\) exhibiting the inclusion as a pullback of true.

**Quantification in Set.** Given \(f:A\to B\) and \(P\subseteq A\), put \(\exists_f(P)=\{b\mid\exists a\in P:f(a)=b\}\) and \(\forall_f(P)=\{b\mid f^{-1}(\{b\})\subseteq P\}\). Then \(\exists_f\dashv f^{-1}\dashv\forall_f\) as monotone maps of powerset posets. Empty fibers belong to \(\forall_f(P)\), not \(\exists_f(P)\).

**Open-set Heyting algebra.** Let \(X=\{p,q\}\) with open sets \(\varnothing,\{p\},X\). In this lattice, \(U\Rightarrow V=\operatorname{int}((X\setminus U)\cup V)\), \(\neg U=U\Rightarrow\varnothing\). For \(U=\{p\}\), \(\neg U=\varnothing\), so \(U\vee\neg U=U\neq X\).

### Exercises and answers

1. **Exercise:** For \(f(a_1)=f(a_2)=L\) and \(f(b_1)=R\), with no preimage of \(N\), compute \(\exists_f(P)\) and \(\forall_f(P)\) if \(P=\{a_1,b_1\}\). **Answer:** \(\exists_f(P)=\{L,R\}\), \(\forall_f(P)=\{R,N\}\).
2. **Exercise:** Why is the preimage of a predicate contravariant? **Answer:** \(f:A\to B\) induces \(f^{-1}:\mathcal P(B)\to\mathcal P(A)\), reversing the direction.
3. **Exercise:** What universal property characterizes an exponential \(B^A\)? **Answer:** Natural bijections between maps \(X\times A\to B\) and maps \(X\to B^A\).
4. **Exercise:** Does the poset of open subsets of a space automatically constitute an elementary topos? **Answer:** No; it is a Heyting algebra of propositions, while an elementary topos requires additional category-theoretic structure.

### References

- Steve Awodey, *Categorical Logic* course and notes, https://awodey.github.io/catlog/
- Steve Awodey, *Introduction to Categorical Logic* (course notes), https://awodey.github.io/typetheory/notes/catlog2024.pdf
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Brendan Fong and David I. Spivak, *Seven Sketches in Compositionality*, https://arxiv.org/abs/1803.05316
