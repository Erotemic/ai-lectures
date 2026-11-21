# How Small Can an Infinite Model Be? Löwenheim–Skolem and the Skolem Paradox

<!-- BEGIN SPOKEN LECTURE -->

Suppose we write axioms intended to describe an immense mathematical universe. We want the natural numbers, every subset of the natural numbers, functions between arbitrary sets, and towers of larger infinite collections. The language of the axioms is countable: it uses a finite alphabet, and every formula is a finite string. The structures described by the axioms may be vast.

Now comes a theorem that sounds almost like sabotage. If a first-order theory in a countable language has an infinite model, then it has a model whose domain is countably infinite. That model can satisfy the same axioms, including claims that certain sets are uncountable. How can a countable model contain something uncountable?

This is the downward Löwenheim–Skolem phenomenon, and the apparent contradiction is called Skolem's paradox. It is not a formal inconsistency. It shows how sharply we must distinguish the elements that exist in a structure from the objects seen by a mathematician describing that structure from outside. We will learn both a construction of small models and the resolution of the paradox.

## A structure only needs witnesses it can see

Take an infinite structure M in some countable first-order language. Begin with a countable set of elements we want to keep, perhaps just one element. We will enlarge that seed so that whenever a formula with parameters from our chosen elements has a witness in M, the enlarged set contains at least one such witness.

For a concrete example, suppose M is a graph. If a chosen vertex has a neighbor in M, add one neighbor. If two chosen vertices share a common neighbor somewhere in M, add one such common neighbor. Do this not just for graph adjacency but for every first-order existential formula with parameters drawn from the chosen set. There are countably many formulas in a countable language, and for a countable set of parameters there are countably many finite parameter tuples. So at each stage we can add only countably many witnesses.

Repeat the process through stages indexed by natural numbers. Take the union of all the elements collected. A countable union of countable sets is countable in ordinary ZFC mathematics. Why is the final set closed under the witness requests? Any finite tuple of its members appeared by some finite stage. If an existential statement about that tuple is true in M, the process supplies a witness at the next stage. The union includes it.

This is the heart of the Tarski–Vaught test for an elementary substructure. A subset N of the domain of M is elementary when every first-order formula with parameters from N has the same truth value in N as in M. It is enough to ensure that each existential statement true in M with parameters from N has a witness in N, assuming N interprets the function symbols appropriately. The proof is another induction on formulas. Atomic statements agree by restriction. Boolean connectives follow by induction. At an existential quantifier, the witness condition supplies the needed element.

Thus, starting from an appropriate seed, the closure procedure constructs a countable elementary substructure of an infinite structure in a countable language. The argument can be made with Skolem functions or directly with witness choices. In the ambient ZFC setting, the required choices can be made. This is a stronger result than merely finding some countable model of the same sentences: the smaller model sits inside the larger one and agrees with it about all first-order formulas on its own parameters.

## Elementary does not mean identical

Consider the integers under addition as a structure in a language with addition and zero. A substructure needs to be closed under the named operations. A subset containing zero and closed under addition may be a substructure, but it need not be elementary. If it lacks an element required by a first-order statement true in the larger structure, it fails the test.

For example, take the ordered additive structure of the rationals in a language that names addition, additive inverse, zero, order, and the constant one. The integers form a substructure: they are closed under those operations and contain the named constants. But they are not an elementary substructure. The sentence saying there exists an x strictly between zero and one holds in the rationals and fails in the integers. A substructure preserves the interpretations of the symbols on its own domain. An elementary substructure preserves the truth of every first-order statement with its parameters. This is much stronger.

The word elementary does not mean the substructure has every external set-theoretic property of the larger domain. It means it cannot be distinguished by the chosen first-order language, with parameters from the smaller structure. That limitation of expressibility is precisely what the theorem exploits.

## The paradox inside set theory

Now assume, for the sake of the mathematical discussion, that ZFC has a model. Since ZFC is a countable first-order theory, the completeness theorem and downward Löwenheim–Skolem give a countable model M of ZFC. This is a conditional conclusion, not a proof from ZFC that ZFC is consistent. A sufficiently strong consistent theory cannot establish its own consistency by the ordinary internal method.

Externally, the entire domain of M is a countable collection. We can enumerate its members using natural numbers in our surrounding mathematics. In particular, the collection of objects that M calls subsets of its natural numbers is externally countable, because it is contained in the countable domain of M.

But M satisfies Cantor's theorem and the other relevant axioms. Inside M there is no bijection from its internal natural numbers to its internal power set of natural numbers. M therefore satisfies the sentence that its power set of the naturals is uncountable. How can both assertions hold?

The two assertions quantify over different collections of functions. Outside M, we have an enumeration of the domain. That enumeration is a function in the surrounding mathematics. Nothing says the enumeration is an element of M. When M asserts that no bijection exists, it means no object in its domain that M recognizes as a function serves as a bijection of the required internal kind. It does not quantify over every external function that a mathematician in the surrounding universe can describe.

There is a second boundary as well. The natural numbers of M need not coincide with the standard natural numbers of the surrounding universe. A countable model of set theory can have nonstandard natural-number elements from the external perspective. Even when both sides use the phrase the naturals, the interpretation is controlled by the structure.

The resolution is therefore not that Cantor's theorem fails. It is that countability is relative to an ambient notion of which functions and which sets are available. From outside, M's domain is countable. From inside M, it has no internal enumeration of its power set of the naturals. No sentence and its negation are both true in the same structure under the same interpretation.

## Finite language can describe unbounded size

We might wonder whether the limited number of sentences in a countable language somehow forces every model to be countable. It does not. Consider the theory of infinite sets in a language with equality and no other nonlogical symbols. Include, for each positive integer n, a sentence requiring at least n distinct elements. Any infinite set is a model, regardless of whether its cardinality is countable or uncountable.

The theory itself is countable, but its models can have every infinite cardinality in ordinary ZFC. A first-order theory cannot, by that size of language alone, assign a unique infinite cardinality to its models. There are general upward and downward Löwenheim–Skolem theorems relating the size of a language, a model, and other models of the same theory. Their precise forms account for language cardinality, infinity, and specified sets of parameters.

The simplest example also shows a difference between categoricity and completeness of a theory. A theory is categorical in a cardinality if all its models of that cardinality are isomorphic. Being complete means deciding every sentence of its language. These are related notions, but they are not synonyms. A complete first-order theory can have nonisomorphic models of different infinite sizes, and even different nonisomorphic models of the same size in many cases.

For instance, the complete first-order theory of a dense linear order without endpoints has a unique countable model up to isomorphism: the order of the rational numbers. It also has uncountable models. So complete logical information about all first-order sentences does not necessarily pin down one infinite structure across all cardinalities.

## Why this is useful rather than merely paradoxical

Small-model theorems often make mathematical questions manageable. Suppose a first-order theory in a countable language has any infinite model. If we only need to show that some model exists, we may be able to work with a countable one. In some contexts that allows a construction by a sequence of stages or a combinatorial argument over countably many objects.

But there is a cost to remember. The countable model may not be the intended model. Results concerning its internal sets, functions, or arithmetic do not automatically transport to all external interpretations. This is relevant in formal methods, where a specification language may admit models other than the software state or mathematical structure an engineer had in mind. Proving that a sentence follows from a specification is valuable, yet proving that the specification characterizes exactly the intended behavior may require stronger assumptions.

Löwenheim–Skolem supplies a disciplined lesson in perspective. We always reason inside some ambient mathematics, and we often study a smaller structure that has its own internal quantifiers. When those perspectives are named separately, the paradox dissolves. When they are silently mixed, even a perfectly consistent mathematical theory can appear to say something impossible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Downward Löwenheim–Skolem.** For an \(L\)-structure \(M\), an infinite cardinal \(\kappa\ge|L|\), and \(A\subseteq M\) with \(|A|\le\kappa\), there exists \(N\preccurlyeq M\) with \(A\subseteq N\) and \(|N|\le\kappa\), assuming the usual ZFC setup. For countable \(L\) and countable \(A\), this yields a countable elementary substructure when \(M\) is infinite.

**Tarski–Vaught test.** A substructure \(N\subseteq M\) is elementary if for every formula \(\varphi(x,\bar a)\) with \(\bar a\in N\), whenever \(M\models\exists x\varphi(x,\bar a)\), there exists \(b\in N\) with \(M\models\varphi(b,\bar a)\).

**Skolem paradox.** If ZFC has a model, there is (externally) a countable model \(M\models\mathrm{ZFC}\). Internally \(M\models\) “\(\mathcal P(\omega)\) is uncountable.” An external enumeration of \(M\)'s domain does not give an internal bijection in \(M\); the relevant quantifiers range over different universes.

**Exercises with solutions.** (1) State the difference between a substructure and elementary substructure. *Answer:* closure under named functions and inherited relations versus truth-preservation for every first-order formula with parameters. (2) Why do we iterate witness closure through countably many rounds? *Answer:* newly adjoined witnesses become parameters for new formulas, which need witnesses at later rounds. (3) Why does external countability of a model not contradict its internal uncountability statement? *Answer:* the external enumeration need not belong to the model. (4) Does a countable theory only have countable models? *Answer:* no; the theory of an infinite set in pure equality has models of every infinite cardinality.

### Sources and reading

- Open Logic Project, *Sets, Logic, Computation*: https://slc.openlogicproject.org/
- Open Logic Project, *First-Order Logic*: https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf
- Stanford Encyclopedia of Philosophy, *Set Theory*: https://plato.stanford.edu/entries/set-theory/
