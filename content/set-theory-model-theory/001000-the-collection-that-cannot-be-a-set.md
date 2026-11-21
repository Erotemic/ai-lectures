# The Collection That Cannot Be a Set: Why Set Theory Needs Axioms

<!-- BEGIN SPOKEN LECTURE -->

A set seems like the least demanding mathematical object we could ask for. A number has to obey arithmetic. A function needs an input, an output, and a rule. But a set is merely a collection. Put some things together, and you have one. At least that is how elementary set notation encourages us to think.

Suppose we describe a collection by a sentence: all prime numbers; all continuous functions; all graphs with no cycles. Usually that works. Now describe the collection of all sets that are not members of themselves. Give it a name, R. Does R belong to R? If it does, its defining condition says it does not. If it does not, its defining condition says it does. Neither answer is possible.

The contradiction is not a curiosity about self-reference that can be banished by avoiding one phrase. It exposes a false rule: that every condition defines a set. The distinction between a legitimate collection and a set is our starting point. We will construct the basic idea of axiomatic set theory, see how mathematics survives the restriction, and prove one of its most beautiful results: no set can list all of its own subsets.

## A promise we cannot keep

In elementary notation, we often write a set-builder expression such as the set of all integers greater than zero. The surrounding universe is already a known set, the integers, and the condition selects some of its members. There is no difficulty. In axiomatic set theory, the distinction between filtering an existing set and collecting all objects satisfying a description is decisive.

Consider a rule called unrestricted comprehension: for every property P, there exists a set containing exactly the objects with property P. Choose the property, x is not an element of x. If unrestricted comprehension holds, we obtain R. Substituting R for x produces the contradiction we just found. In logic this is Russell's paradox. It is a proof, not merely a verbal puzzle, that unrestricted comprehension cannot be an axiom of any consistent ordinary set theory.

A safer principle is separation. If we already possess a set A, and we have a well-formed condition P, then we may form the subset of elements of A satisfying P. If we take the property x is not a member of x, separation gives us a subset R sub A. There is no contradiction, because membership of R in A is not guaranteed. If R were in A, the familiar argument would indeed force a contradiction. Consequently, R cannot belong to A. This proves that no set A contains every set. It does not prove there are no collections worth describing more broadly. We may speak about the class of all sets; we just must not treat it as one more set within the same theory.

Notice how a precise qualification saves a powerful construction. We have not abandoned set-builder notation. We have corrected its domain of use. Every time a proof says, take the set of all objects with such-and-such property, we should now ask: from which already existing set are these objects being selected, or which axiom constructs their collection?

## What the axioms actually supply

The standard framework is Zermelo–Fraenkel set theory, often abbreviated ZF. Adding the axiom of choice gives ZFC. We do not need to memorize a recital of axioms to understand their division of labor. Extensionality says that sets having the same members are equal. The empty set axiom supplies an object with no members, although in some axiom lists it is derivable from other assumptions. Pairing lets us collect two already given objects. Union flattens a set of sets into the collection of their elements. Power set collects all subsets of a particular set. Infinity ensures a set large enough to support the natural numbers. Separation filters a given set. Replacement says, roughly, that the image of a set under a definable single-valued rule is again a set. Foundation rules out infinitely descending membership chains in the relevant sense.

These are not permissions to say any arbitrary collection exists. Each gives a disciplined way to build. Pairing, for example, allows the singleton containing the empty set. This singleton is not the empty set: it has exactly one member, which happens itself to have no members. Pairing again allows us to construct a set containing the empty set and its singleton. Define zero as the empty set, one as the singleton containing zero, and two as the set containing zero and one. The successor of a number n is n together with the singleton n. At each finite stage we have constructed a new set whose members are the earlier numbers.

The axiom of infinity allows these stages to exist together in an infinite set. Separation then gives the least such inductive set, omega, whose members are the finite von Neumann ordinals. This is a model of the natural numbers inside set theory, not a claim that numbers were originally invented as collections of their predecessors. Different foundations can encode the same arithmetic differently. The important fact is that ordinary arithmetic can be interpreted within a disciplined theory of sets.

The same approach constructs ordered pairs, functions, relations, the integers, rationals, and eventually real numbers. A function is represented by a set of ordered pairs satisfying uniqueness of output. That representation is useful because existence claims about functions now reduce to set existence claims. It is not usually necessary to inspect the internal nested-pair encoding in a mathematics paper. It is necessary when foundational axioms or formal representations become part of the question.

## Why power sets are so powerful

Take a small set A containing Alice, Bob, and Carol. How many subsets does it have? Each person is either included or excluded, so there are two to the third power, or eight subsets. We can identify a subset with a three-entry pattern of yes and no choices. The power set of A is the set of all eight such patterns, interpreted as subsets.

For any finite set with n members, the power set has two to the n members. The surprise is that the power set remains strictly larger than its parent even when the parent is infinite. This is Cantor's theorem, and its proof is a diagonal argument rather than a numerical calculation.

Suppose that someone offers a way to assign to every element x of A a subset F of x's own set A. In other words, the person offers a function from A to its power set. They claim every subset of A appears somewhere on the list. We can defeat the claim by defining a new subset D. Put x in D exactly when x does not belong to the subset assigned to x. This definition is legitimate separation: D is a subset of the already existing set A.

Now ask whether D equals F of a for some particular a in A. If a belongs to D, the defining condition says a does not belong to F of a. If a does not belong to D, the condition says a belongs to F of a. So D and F of a always disagree at a. Therefore D is absent from the list, however the function F was chosen. No function from A can be onto the power set of A.

The proof works for an empty set, for a three-element set, and for an infinite set. On three elements it gives an ordinary eight-versus-three counting fact. On an infinite set it produces a hierarchy of increasingly large infinities. We have also learned a reusable method: to refute a proposed exhaustive enumeration, construct an object that disagrees with the item at every possible index.

Do not confuse this argument with Russell's contradiction. They share a self-referential-looking condition, but the outcomes are different because Cantor's diagonal set is formed inside a specified set A. There is no contradiction; there is a perfectly legal new subset that evades one particular enumeration. The dangerous move would be declaring a universal set A containing every set. That would force the power set of A to sit inside A and violate Cantor's theorem.

## The universe as a succession of stages

A useful picture of set theory is the cumulative hierarchy. Start at stage zero with the empty set. At the next stage, take the power set. At every successor stage, take the power set of the previous stage. At a limit stage, take the union of all earlier stages. These stages are labeled by ordinals, including labels beyond the finite numbers.

The first few are easy to see. The zero stage has nothing. The first stage contains only the empty set. The second has two members: the empty set and the singleton containing it. The third has four members, namely all subsets of the second stage. The growth is faster than ordinary counting, but more importantly the hierarchy organizes how sets can appear without placing all sets inside a single final set.

In ZF with Foundation, every set lies in some stage. There is no last stage, no final V that is itself a set containing everything. The hierarchy V is a proper class. Its description tells us how the axioms picture the universe; it is not a proof that a completed universal set exists.

The logical role of the stages is also instructive. We use mathematics about ordinals to say what happens at limit stages, and we use set axioms to prove those stages exist. Set theory studies the objects it uses to organize itself. That apparent circularity is handled by formal proofs inside a stated axiom system, not by pretending we can build the entire universe from outside mathematics in a single afternoon.

## What an axiom does and does not certify

Axioms are the assumptions of a mathematical theory. If we derive a theorem from ZFC, the derivation establishes that every model of ZFC satisfies the theorem, assuming the ordinary soundness of first-order reasoning. It does not by itself establish that ZFC is consistent. In fact, once we understand arithmetic and Gödel's incompleteness theorem, we will learn why a sufficiently strong consistent effective system cannot prove its own consistency by its standard formalized means.

There is a further distinction between a description of a set and a proof that a particular set exists. The phrase the smallest uncountable ordinal points toward a legitimate object in standard set theory; proving its existence requires nontrivial constructions. The phrase the set of all sets looks syntactically similar but is impossible in ZF. Familiar grammar gives no guarantee of mathematical existence.

That is a useful habit in every field. When a proof introduces the optimal function, the space of all solutions, or the union of every compatible structure, ask what existence theorem authorizes that move. Sometimes it is finite enumeration. Sometimes compactness, completeness, an axiom of choice, or a fixed-point theorem. Good mathematical arguments expose such commitments rather than smuggling them into notation.

## An ending that is really a beginning

We started with the apparent simplicity of a collection and found a boundary: describing a condition is not sufficient to create a set. We then built mathematical objects by specified operations, obtained the natural numbers, and proved that power sets always escape attempts to list them using their own members. The same discipline that prevents Russell's paradox makes Cantor's argument possible.

Set theory is therefore not merely bookkeeping for objects already understood. It offers methods of construction, proofs of existence, and a language for asking exactly what assumptions a theorem needs. Behind the ordinary word set is a theory that has learned to distinguish a meaningful definition from an available mathematical object. That distinction becomes essential when we count infinities, construct models of logical theories, and formalize mathematics on a machine.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Axioms and schemas.** ZF includes Extensionality, Pairing, Union, Power Set, Infinity, Foundation, Separation schema, and Replacement schema (with minor variations in primitive axiom lists). ZFC adds Choice. Restricted Separation has form
\[
\forall A\,\exists B\,\forall x\; [x\in B\leftrightarrow (x\in A\wedge\varphi(x,\vec p))].
\]
Unrestricted comprehension \(\exists B\,\forall x\,(x\in B\leftrightarrow\varphi(x))\) is inconsistent when \(\varphi(x)\) is \(x\notin x\).

**Cantor's theorem.** For \(f:A\to\mathcal P(A)\), define \(D=\{a\in A:a\notin f(a)\}\). For each \(a\in A\), \(a\in D\leftrightarrow a\notin f(a)\), so \(D\ne f(a)\). Consequently \(|A|<|\mathcal P(A)|\), where strict comparison means there is an injection \(A\hookrightarrow\mathcal P(A)\) and no bijection. The injection is \(a\mapsto\{a\}\).

**Cumulative hierarchy.** \(V_0=\varnothing\), \(V_{\alpha+1}=\mathcal P(V_\alpha)\), \(V_\lambda=\bigcup_{\beta<\lambda}V_\beta\) for limit \(\lambda\). Within ZF with Foundation, every set belongs to some \(V_\alpha\). Do not treat \(V=\bigcup_{\alpha\in\mathrm{Ord}}V_\alpha\) as a set.

**Exercises with solutions.** (1) Explain why \(\{\varnothing\}\ne\varnothing\). *Answer:* the left set has one element, the right has zero. (2) Prove that a universal set would violate Separation without mentioning power sets. *Answer:* separate the non-self-membered elements from the alleged universal set, then ask whether that subset belongs to itself. (3) Give the diagonal set for a proposed listing of subsets of \(\{a,b\}\), indexed by \(a,b\). *Answer:* \(D=\{x\in\{a,b\}:x\notin f(x)\}\); it differs from \(f(a)\) at \(a\) and from \(f(b)\) at \(b\). (4) State the existence hypothesis behind \(\{x\in A:P(x)\}\). *Answer:* an already existing set \(A\), with \(P\) expressed by a formula of the theory.

### Sources and reading

- Stanford Encyclopedia of Philosophy, *Set Theory*: https://plato.stanford.edu/entries/set-theory/
- Open Logic Project, *Set Theory* (open text): https://builds.openlogicproject.org/content/set-theory/set-theory.pdf
- Open Logic Project, *Sets, Logic, Computation*: https://slc.openlogicproject.org/

The examples and narration are original teaching material, not reproduced source text.
