# 002000 - Natural Deduction and Lambda Calculus: How Proofs Compute

**Track:** Logic, Type Theory, and Constructive Mathematics. **Background:** basic functions and implication. **Theme:** assumptions, introduction and elimination rules, typed lambda terms, substitution, and normalization.

<!-- BEGIN SPOKEN LECTURE -->

# Natural Deduction and Lambda Calculus: How Proofs Compute

A mathematician writes, "Assume P. From this assumption we obtain Q. Therefore P implies Q." The words are so ordinary that it is easy to miss the machinery underneath them. The proof briefly enters a world in which P is available, performs some work in that world, and then closes the assumption. Whatever happened inside becomes a reusable argument: any future proof of P can be fed into it to obtain Q. This little pattern is one of the load-bearing structures of mathematics. It is also the shape of a function definition.

We are going to put that observation to work. Rather than treating a proof as a decorated paragraph, we will describe the operations permitted on mathematical evidence. Then we will notice that the resulting rules resemble a small programming language. We will evaluate one of its programs by reducing a proof, examine why the reduction is legitimate, and see what breaks when a proof makes an unjustified assumption. The payoff is a clearer account of both theorem proving and program verification: an argument can have a type, and there can be meaningful ways to simplify it without changing its conclusion.

## A temporary assumption is a precise obligation

Consider three propositions: P, Q, and R. Suppose someone has a method that turns evidence for P into evidence for Q, and another method that turns evidence for Q into evidence for R. We want to establish that P implies R. We temporarily assume P. Using the first method, we obtain Q. Using the second, we obtain R. We then discharge the original assumption and conclude P implies R.

To discharge an assumption does not mean forgetting that we used it. The final proof explicitly says what happens when that assumption is provided. It is a function waiting for evidence of P. Give it a proof of P and it runs the two transformations, returning evidence of R. This means the proof is reusable even if no one presently knows whether P is true.

That last point is worth considering. A proof of P implies R need not contain a proof of P. A map from one city to another need not contain a traveler. The conditional promise and its fulfillment are two different mathematical objects. Many failed arguments blur the distinction by treating the establishment of a conditional statement as though the premise had already been established.

Natural deduction is one systematic way to keep these obligations visible. For each logical connective, it tells us how to introduce the connective into a conclusion and how to use evidence that contains it. For implication, introduction means: assume P, derive Q, then close the assumption to obtain P implies Q. Elimination means: given P implies Q and given P, conclude Q. That elimination rule is the familiar modus ponens.

The symmetry between the two rules is striking. Introduction packages a derivation as a conditional promise. Elimination opens the package by applying it to a premise. If we introduce an implication and immediately eliminate it, the result should be no more complicated than simply carrying out the original derivation with the actual premise supplied. This observation leads straight to computation.

## Functions wearing logical clothing

Suppose we write a function that accepts a number x and returns twice x. In a programming notation we might write, "function x goes to two times x." If the function is named double, evaluating double of seven yields fourteen. We replace the parameter x in the body with the argument seven and calculate.

Now replace the number x with a proof of P and the expression twice x with a derivation of Q from that proof. The same operation occurs. A proof of P implies Q accepts proof evidence for P and constructs proof evidence for Q. When applied, the formal parameter is replaced by the actual evidence. This is the central operational meaning of the Curry-Howard correspondence.

The lambda calculus makes the comparison explicit. A lambda expression consists of a parameter and a body; application supplies an argument. We can type the parameter and the body. If the parameter has type P and the body has type Q, the lambda expression has type P implies Q. In the proof interpretation, P and Q are propositions. In the program interpretation, they are input and output types. The construction rules have the same form.

Let us make a tiny proof concrete. Assume P and Q are propositions. We wish to prove that if both hold, then P holds. A conjunction is constructed from two proofs, one of each conjunct. So we build a function that accepts evidence of P and Q together, opens that pair, and returns its first component. It proves the implication from P and Q to P. Applied to an actual conjunction, it returns precisely the proof of P that went into the pair.

Now try a slightly richer example. We want to prove that P implies Q, together with Q implies R, implies P implies R. First receive a function f from P to Q. Then receive a function g from Q to R. Then receive a proof p of P. Evaluate f on p to get Q, and g on the result to get R. The proof term is just function composition with its types visible. Its correctness requires no case analysis about what P, Q, or R mean.

But types have to line up. A method from P to Q cannot, merely by being a method, be passed an arbitrary proof of R. Likewise, a proof that a particular number is even does not prove that an unrelated number is even. A type checker rules out precisely these mismatches, in the same way a mathematical argument rules them out when written carefully.

## The human history behind the formalism

In the early twentieth century, logicians were trying to understand what counts as a legitimate deduction. Gerhard Gentzen, working in Germany in the 1930s, developed natural deduction and sequent calculus as ways of making inference steps explicit. His 1935 work analyzed the structure of proofs, including the phenomenon now described as elimination of detours. A proof might establish an intermediate statement only to unpack it immediately. Under appropriate conditions, that detour can be removed.

Around the same period, Alonzo Church developed the lambda calculus as a formal language for functions and computation. The two lines of work were motivated by different questions. One studied proof; the other studied definable operations and effective calculation. Their convergence was gradual, and it would distort the history to present Curry-Howard as a single discovery made at one desk. The correspondence grew from several results, including Haskell Curry's combinatory logic and William Howard's later explicit formulation connecting proofs to types.

The parallel has consequences even if we never use a computer. Gentzen's question about unnecessary logical detours becomes a question about reducing expressions. Church's question about evaluating functions becomes a question about simplifying proofs. Proof theory and computation illuminate each other because their rules align.

## Watch a proof reduce

Consider the conditional statement "if P then P." We prove it by assuming P and returning the same evidence. In function language this is the identity function. Now imagine we already have a proof p of P. We apply the identity proof to p. What do we obtain? The same p. The step from applying the identity function to returning its argument is a beta reduction. It removes a function definition immediately followed by its application.

In a more interesting example, suppose we constructed a proof of P and Q by pairing p with q. Then, to derive P, we take the first projection of the pair. The result reduces to p. The introduction rule built something that the elimination rule immediately dismantled. There was no intellectual need to build the pair if the intended output was only p, though the longer derivation was valid.

A disjunction offers another example. To prove P or Q, we may present evidence of P and choose the left branch. To use a proof of P or Q, we provide one procedure for the P case and another for the Q case. If we construct the left branch and immediately analyze the disjunction, only the P procedure runs. The other branch is not wrong; it is simply irrelevant to that particular computation.

These reductions reveal that proof rules are not an arbitrary list. Introduction and elimination fit together as constructors and consumers. Their interaction has computational content. A well-structured proof calculus gives us equations telling us what happens when each constructor meets the elimination rule designed for it.

This is also where care with language becomes important. A logical proof is not necessarily a useful executable program in the everyday sense. A proof term may be erased, may rely on an axiom, or may include enormous calculations that we would never want to execute. We are studying a structural relationship between derivation and computation. Whether a particular theorem yields a practical implementation depends on the logical fragment and the representation of its data.

## Substitution has rules, not just intuition

Imagine a proof in which the assumption P is named h. The proof's intermediate steps may mention h many times. When a genuine proof p of P becomes available, we substitute p wherever h was used. To preserve validity, the substitution must respect the context. The replacement has the correct type, and bound variables must not accidentally change their meaning.

The same issue occurs in ordinary algebra. If a formula contains a variable x, replacing x by an expression is usually safe. But if the formula also contains a quantifier that binds variables, careless replacement can capture a variable and change the claim. In programming-language theory, we call this variable capture. Bound-variable renaming is a mundane but essential part of defining substitution precisely.

Consider a function taking x and returning another function taking y and returning x. If we substitute an expression containing y for the free x, we cannot let the inner y accidentally bind the y in the inserted expression. We rename the inner parameter before substituting. Formal implementations commonly avoid errors by using carefully designed representations of variable binding, such as de Bruijn indices or hygienic syntax mechanisms.

These technical details have a philosophical consequence. The correctness of proof substitution is not secured by saying that the intent is obvious. It follows from explicit rules about free variables, bound variables, types, and contexts. Once the rules are sound, we can automate many of the mechanical steps. That automation is one reason a small proof checker can inspect elaborate arguments assembled by much larger programs.

## Detours, normal forms, and an important limit

Suppose we have a proof of a proposition that first builds an implication and then applies it; or first builds a pair and then extracts a component. A normalization procedure simplifies those immediate detours. In the simply typed lambda calculus with its usual type formers and without unrestricted recursion, every well-typed term reduces to a normal form after finitely many appropriate reduction steps. This property is called strong normalization when every possible reduction sequence terminates.

That claim needs its conditions. Ordinary programming languages permit general recursion and potentially nonterminating functions. If we allow arbitrary self-application or unrestricted fixed points, evaluation may loop forever. A theorem about strongly normalizing typed terms cannot be transferred to every language containing functions and types. Proof assistants restrict their logical core to maintain soundness, and they handle general computation through distinctions that matter.

A normal form is not automatically a beautiful proof. It is a proof with certain reducible patterns removed. Some transformations expand the size of terms; choices about sharing and reduction strategies affect computational cost. Normalization is a theorem about what can be simplified under a given calculus, not a promise that all proof presentations will become short, clear, or easy for people to read.

Still, the theorem is powerful. It ties the logic of a system to the dynamics of its expressions. A derivation that would otherwise remain a static artifact can be analyzed as a computation. The types constrain the allowed operations, and normalization describes the behavior of valid expressions under reduction.

## What natural deduction cannot establish for free

Let us test the system on a tempting claim. From P implies Q, may we conclude Q implies P? No. The first function goes from evidence of P to evidence of Q. The proposed conclusion would require a function in the reverse direction. Nothing in the type or in the proof rules supplies that inverse.

What about proving P or not P for every proposition P? The ordinary introduction rule for disjunction asks us to supply the left proof or the right proof. If P is arbitrary and undecidable with the available information, the constructive rules offer no way to select a branch. Classical logic adds a principle that permits this claim. That addition can be mathematically reasonable, but it is additional logical power. We must distinguish a theorem justified by the constructive rules from one justified by invoking classical axioms.

This illustrates a useful habit when reading proofs. Ask what evidence has actually been constructed. For an implication, where is the transformation from premise to conclusion? For a conjunction, where are both parts? For a disjunction, how is a branch justified? For a contradiction, which assumptions created the incompatible conclusions? These questions expose gaps more reliably than checking whether a paragraph sounds persuasive.

They also make proof debugging less mysterious. An unfilled goal is not a failure of eloquence. It is a demand for a term of a specified type. The available assumptions may provide that term directly, or they may require composition, case analysis, induction, or a new lemma. Sometimes no such term follows from the assumptions, and the correct response is to revise the proposition.

## Reading a typed proof as a small machine

Suppose we are verifying a software component that accepts a nonempty list and returns its head. A careless implementation might treat every list as nonempty and crash on the empty one. A specification can instead demand evidence that the list contains at least one element. The head operation then accepts both the list and a proof of nonemptiness. The function type records the obligation that used to be hidden inside a comment.

If the proof of nonemptiness is constructed by inspecting the list, we can think of that inspection as a case analysis. If the list is empty, there is no evidence to construct; the program must choose a different path. If the list has a head and tail, a constructor supplies the evidence. The separation between constructing evidence and consuming it resembles natural deduction's introduction and elimination rules.

The remaining challenge is to decide which properties belong in types. A type may prevent a call with an empty list, yet fail to express a more complex intended requirement, such as preserving the order of a sorted output. The type system checks the contract actually written. It does not discover the contract the programmer wished they had written.

This is where the connection between mathematics and computation becomes practical. A proof can certify that a transformation respects stated assumptions. A reduction can simplify the proof term. A type checker can verify that the pieces compose. But the human author still has to choose meaningful assumptions, find appropriate lemmas, and identify the right theorem.

## Negation and the discipline of contradiction

In natural deduction, negation gives another opportunity to see the difference between a valid inference and an unsupported assertion. To say not P is to say that P leads to contradiction. If we can assume P and derive an impossible conclusion, we may discharge the assumption and conclude not P. The proof has the form of a function from proofs of P to evidence of falsehood. In type-theoretic notation, not P is represented as P implies False.

As a small mathematical example, suppose a natural number n is claimed to be both less than itself and not less than itself. If we possess a proof of the first claim and a proof of its negation, we can apply the negation to the first proof and obtain a contradiction. But we should distinguish the mere ability to derive a contradiction from the principle allowing us to infer an arbitrary desired proposition afterward. In ordinary constructive logic, elimination from False is part of the logical rules. It expresses that there is no inhabitant of False from which a genuine computation would need to be carried out.

Now consider proving that there is no greatest natural number. Suppose there were a number m greater than or equal to every natural number. Instantiate the universal claim at m plus one. We obtain the impossible assertion that m plus one is at most m. Thus the supposed greatest number cannot exist. The contradiction depends on a concrete witness that defeats the assumption, rather than on an emotional sense that infinity must be too large to have a greatest member.

There is a distinction between proving not P and proving P from not not P. Intuitionistic logic supports the first pattern when P leads to contradiction, but the reverse double-negation elimination is a classical principle in general. The difference is easy to overlook because everyday prose often slides from "we cannot refute it" to "therefore it holds." Natural deduction forces us to identify which inference rule licenses the final step.

## A worked reduction with alternatives

Suppose a sensor reading is classified as either valid or invalid. A proof that every reading falls into one of these two categories might be represented by a disjunction, when the classification is constructively decidable. We write one procedure for valid readings and another for invalid readings. Given evidence that the reading is valid, the complete case analysis immediately selects the valid branch. Its output is whatever the valid branch produces.

Now wrap that case analysis inside a function taking a reading and its classification. If we apply the function to a particular reading and a particular classification proof, two simplifications happen. The outer function application substitutes the actual reading and proof for its formal parameters. The inner case analysis then reduces to the branch selected by the classification. This is nested beta-like computation, visible in both the logical proof and the program representation.

This example also exposes the limit of the analogy. If we assert that every arbitrary reading is valid or invalid by invoking a classical principle without specifying an effective classifier, the existence of a proof in `Prop` does not necessarily provide a runtime branching algorithm. A working classifier may need a decidable predicate, a finite representation, or a procedure establishing which alternative holds. The proof rules tell us what must be supplied; the chosen foundational system determines whether the supplies can be computed.

## The idea to carry away

A mathematical proof has both content and structure. Natural deduction makes that structure explicit by tracking assumptions and specifying how connectives are introduced and used. The lambda calculus reveals that the same structures behave like functions and applications. Substituting a proof into a conditional argument corresponds to evaluating a function; eliminating immediate proof detours corresponds to reducing a program.

The central lesson is therefore stronger than saying that proofs resemble programs. In a carefully chosen formal calculus, the rules for constructing and simplifying proofs can be the rules for constructing and evaluating typed expressions. That unity gives us tools to inspect mathematical arguments, understand the consequences of axioms, and build software whose guarantees are checked rather than merely asserted.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Introduction, elimination, and beta reduction

Given contexts `Gamma`, `Gamma, h : P |- t : Q` allows `Gamma |- (fun h => t) : P -> Q`. Given `Gamma |- f : P -> Q` and `Gamma |- p : P`, implication elimination yields `Gamma |- f p : Q`.

The beta equation is `((fun h => t) p) --> t[h := p]`, with capture-avoiding substitution. For pairs: `And.left (And.intro p q) --> p`; for sums, case analysis on `Or.inl p` reduces to the left branch.

### Small Lean illustrations

```lean
example (P Q R : Prop) : (P -> Q) -> (Q -> R) -> P -> R :=
  fun f g hp => g (f hp)

example (P Q : Prop) : P /\ Q -> P :=
  fun h => h.left

example (P Q : Prop) : P \/ Q -> Q \/ P :=
  fun h =>
    match h with
    | Or.inl hp => Or.inr hp
    | Or.inr hq => Or.inl hq
```

### Accuracy notes

- Strong normalization pertains to the simply typed lambda calculus without general recursion; do not extrapolate it to unrestricted programming languages.
- Beta reduction and eta principles depend on the formal calculus. In intensional dependent type theories, unrestricted function extensionality is a separate issue from beta computation.
- Capturing a bound variable during substitution changes meaning and is not an allowed proof reduction.

### Exercises with answers

1. **Find the term:** Given `f : P -> Q` and `g : Q -> R`, construct `P -> R`. **Answer:** `fun hp => g (f hp)`.
2. **Reduce the detour:** What does `(fun hp : P => hp) p` become? **Answer:** `p` by beta reduction.
3. **Disprove a tempting inference:** Does `P -> Q` imply `Q -> P`? **Answer:** No; set `P` false and `Q` true in ordinary Boolean semantics.
4. **Explain substitution:** Why rename a binder before substituting a term containing its name? **Answer:** To avoid capture of formerly free variables.

### References

- Gerhard Gentzen, "Investigations into Logical Deduction" (1935), translated in *The Collected Papers of Gerhard Gentzen* (1969).
- Alonzo Church, "An Unsolvable Problem of Elementary Number Theory" (1936).
- William A. Howard, "The Formulae-as-Types Notion of Construction" (published 1980).
- Jeremy Avigad et al., *Theorem Proving in Lean 4*, chapters 3 and 4: https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/
