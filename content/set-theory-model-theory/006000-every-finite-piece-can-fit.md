# Every Finite Piece Can Fit: Completeness and Compactness

<!-- BEGIN SPOKEN LECTURE -->

Suppose a mathematician writes infinitely many constraints about an unknown structure. No finite group of them leads to trouble. Whenever we choose a finite number of constraints, we can build a structure satisfying those constraints. Does there have to be one structure that satisfies all the constraints at once?

For arbitrary mathematical constraints, not necessarily. We could demand a real number be greater than every natural number. Every finite selection of those inequalities has a real solution, but no real number exceeds all natural numbers. Yet first-order logic offers a remarkable theorem: if every finite subset of a first-order theory has a model, then the entire theory has a model. This is the compactness theorem.

There is no contradiction with the real-number example. The first-order theory of real closed fields does not force its models to be exactly the usual real numbers. An enlarged model can contain elements larger than every standard natural numeral. That is the power and also the warning of compactness: it creates a model, not necessarily the originally intended one.

We will prove why compactness follows from first-order completeness, and then examine the deeper construction behind completeness itself. The proof is a model-building procedure. It starts with a consistent set of sentences, manufactures names for required witnesses, and turns syntactic information into a mathematical structure.

## Finite proofs meet infinite theories

A formal derivation consists of finitely many steps, each justified by an axiom or inference rule. This means that even if our starting theory T has infinitely many axioms, any particular proof uses only finitely many of them. Suppose T proves a contradiction. Then some finite subset T zero of its axioms already proves a contradiction, because the derivation could have mentioned only finitely many assumptions.

Now assume every finite subset of T has a model. If T proved a contradiction, some finite subset would prove it too. Soundness would then say every model of that finite subset satisfies a contradiction, impossible. Therefore T is syntactically consistent: it does not prove a contradiction.

Here is the exact point at which first-order completeness enters. Completeness says that any syntactically consistent first-order theory has a model, with the ordinary classical proof system and standard semantic assumptions. Apply it to T. We obtain a model of the entire theory. That proves compactness.

The argument has three links: finite proof, consistency, model existence. If a logical system has an effective finite proof calculus but lacks the corresponding model-existence theorem, this deduction may fail. Compactness is a property of classical first-order logic, not a blanket principle for every kind of mathematical structure or every stronger logic.

## What completeness actually asserts

We need to distinguish two uses of the word complete. A proof calculus is semantically complete if every sentence true in all models of the premises can be derived from them. Written symbolically, T semantically entails phi implies T proves phi. Soundness supplies the reverse implication.

A theory is syntactically complete if, for every sentence phi in its language, either phi or its negation is derivable from the theory. The completeness theorem about first-order logic is about the proof calculus, not a promise that every consistent theory decides every sentence. A theory may have models that disagree about phi, in which case neither phi nor its negation is a semantic consequence.

We can see the difference in a simple graph theory. Let T contain only the axioms for a simple undirected graph. Some models have a triangle and others do not. So T does not decide the sentence a triangle exists. Nevertheless, if a particular graph sentence is true in every simple undirected graph, the completeness theorem guarantees a formal proof from the graph axioms. The proof calculus is complete even though the graph theory is not.

This distinction will later remove a perceived conflict with Gödel's incompleteness theorem. First-order logic as a deductive system can capture all semantic consequences, while particular effective theories of arithmetic remain unable to settle every arithmetical sentence.

## The model we build from sentences

How can a formal collection of sentences produce actual objects? The classical completeness proof gives a constructive-looking answer, though it is not necessarily an effective algorithm for arbitrary input theories. Its main idea is to build a canonical model whose elements are names.

Begin with a consistent theory T, in a countable first-order language for simplicity. If T contains a sentence saying there exists an x with property P, a model of T must provide an object with property P. We can introduce a fresh constant symbol c and add an axiom: if such an x exists, then P of c. We need to prove this addition preserves consistency. The new constant must be genuinely fresh, so it cannot carry unrelated old obligations. A contradiction involving the new witness would lead, by an appropriate existential generalization argument, to a contradiction from the earlier theory.

We repeat this for existential formulas, including formulas with parameters introduced at later stages. The expansion is called Henkinization. It is a formal way to insist that existential requirements have named witnesses, without claiming we already know what objects those names refer to.

Next extend the resulting consistent theory until it decides each sentence of the expanded language, adding one of phi or not phi while preserving consistency. In a countable language we can enumerate the sentences and make one decision at each finite stage. Since a consistent theory cannot be made inconsistent by adding both alternatives separately, at least one choice is consistent. At a limit, take the union. The union remains consistent because every contradiction would occur in a finite derivation already present at a finite stage.

Now take the closed terms of the expanded language as candidate objects. If the language has function symbols, complex terms such as f of c become names for further objects. If equality is present, two terms may be provably equal even when they are spelled differently, so we identify terms whose equality is in the completed theory. The domain of our model consists of these equivalence classes. Function symbols act by forming terms; relation symbols hold when the corresponding atomic formula belongs to the theory.

The decisive theorem is the truth lemma: for every formula and appropriate assignment of terms, the constructed model satisfies the formula exactly when its instantiated form belongs to the completed theory. We prove this by induction on formulas. Atomic formulas are true by definition. Negation works because the theory decides each sentence consistently. Conjunction works because it is deductively governed by the proof rules. The existential step uses the added witness constants. Without them, a sentence claiming an existential witness might enter the theory with no named term capable of realizing it.

The resulting structure satisfies the completed theory and hence the original T. We have turned the absence of a formal contradiction into an actual model. That construction is why Gödel's completeness theorem is more than an abstract assertion that proofs are powerful enough. It tells us how a consistent logical description can be realized.

## A number larger than every numeral

Now put compactness to work. Take the ordinary first-order axioms of arithmetic, such as Peano arithmetic, and introduce a new constant c. For each standard natural number n, add the sentence c is greater than the numeral for n. Call the expanded collection T.

Every finite subset of these demands can be satisfied in the standard natural numbers. A finite subset mentions only finitely many bounds, so interpret c as a natural number larger than the largest mentioned bound. The arithmetic axioms are already true in that standard structure. Thus every finite part has a model.

By compactness, the whole theory has a model M. Inside M there is an element interpreting c greater than zero, one, two, three, and every standard numeral. No actual natural number in the standard natural numbers has that property. So M is not the standard model. This is one route to a nonstandard model of first-order arithmetic.

We have not discovered a hidden ordinary integer larger than all integers. The domain of M is a different mathematical structure satisfying the same first-order arithmetic axioms plus the new constraints. Its internal ordering contains elements not represented by any standard numeral. Some of its elements behave like enormously large integers, but not in the sense of occupying a late position on the standard number line. The distinction between the intended structure and other models is essential.

## Compactness has an exact scope

One might object that a structure with an element greater than every standard numeral should violate induction. In the standard formulation of first-order Peano arithmetic, induction is a schema with one axiom for each formula of the language of arithmetic. Models of the axioms need not be standard. The property of being one of the standard numerals is not itself expressible by a single first-order formula inside that language, so the induction schema does not eliminate all nonstandard elements.

Another application constructs infinite graphs from finite pieces. Introduce sentences demanding at least n distinct vertices, for every n. Any finite fragment is satisfied by a sufficiently large finite graph. Compactness yields a model satisfying every size demand, so it is infinite. This is a formal route from arbitrarily large finite models to an infinite model, though the proof does not necessarily deliver any particular concrete graph.

The distinction between first-order and second-order languages is important here. Full second-order logic can impose stronger conditions, but it does not inherit the same compactness and effective completeness theorems. Replacing first-order quantifiers with unrestricted quantification over all subsets changes the mathematical system, not just the notation.

## What the theorem lets us do

Compactness is powerful whenever a global structure can be described by first-order sentences and we can solve every finite fragment. It converts a vast collection of local compatibility checks into the existence of one model satisfying the whole theory. Sometimes this gives a clean existence proof. Sometimes it shows that a proposed collection of axioms cannot uniquely describe the structure we intended.

The completeness theorem complements it. It says that semantic consequence and formal proof coincide for first-order logic. That claim is a bridge, not an identification by definition. We proved something about derivations, then built structures to show no semantic consequence could escape the proof system.

The surprising message is that finiteness and infinity help each other. A contradiction must appear in a finite derivation. A model must interpret an entire, potentially infinite theory. The Henkin construction turns the absence of a finite obstruction into an infinite mathematical object. It is a pattern that extends beyond logic: use local consistency, prove that the construction steps preserve it, and then justify a limiting object. Here the pattern becomes a precise theorem about what first-order sentences can force.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Semantic and syntactic consequence.** Soundness: \(T\vdash\varphi\Rightarrow T\models\varphi\). First-order completeness: \(T\models\varphi\Rightarrow T\vdash\varphi\) for classical first-order logic with standard semantics. Equivalent model-existence form: if \(T\) is syntactically consistent, it has a model.

**Compactness.** \(T\) has a model iff every finite subset \(T_0\subseteq T\) has a model. Proof: if \(T\) has no model, completeness yields a finite formal proof of contradiction from \(T\); that proof mentions only finitely many premises, producing a finite unsatisfiable subset.

**Henkin outline.** Expand the language with constants \(c_\psi\) and add witness implications \((\exists x\,\psi(x))\to\psi(c_\psi)\) using fresh symbols. Extend to a maximal consistent witness-complete theory; form closed terms modulo provable equality; interpret symbols syntactically. The truth lemma, proved by induction on formulas, supplies a model. The countable exposition requires suitable enumeration and preservation arguments; general languages need appropriately indexed stages.

**Nonstandard arithmetic.** \(T=\mathrm{PA}\cup\{c>\bar n:n\in\mathbb N\}\). Each finite fragment is realized in \(\mathbb N\) by choosing \(c\) larger than the finitely many numerals mentioned. Compactness yields \(M\models T\), where \(c^M\) is not represented by any standard numeral.

**Exercises with solutions.** (1) Why does a finite proof from an infinite theory involve only finitely many premises? *Answer:* it has finitely many lines. (2) Does first-order completeness imply that the theory of graphs decides every sentence? *Answer:* no; models of the graph axioms disagree on triangle existence. (3) Why does the Henkin construction need new constants? *Answer:* existential membership in the completed theory needs a named witness to make the truth lemma work. (4) Can the element \(c^M\) be an ordinary natural number? *Answer:* no, it is greater than every standard numeral in the model.

### Sources and reading

- Open Logic Project, *Sets, Logic, Computation*: https://slc.openlogicproject.org/
- Open Logic Project, *First-Order Logic*: https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf
- Stanford Encyclopedia of Philosophy, *Model Theory*: https://plato.stanford.edu/entries/model-theory/
