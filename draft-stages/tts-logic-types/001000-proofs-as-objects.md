# 001000 — Proofs as Objects: Why Propositions Can Be Types

**Track:** Logic, Type Theory, and Constructive Mathematics. **Background:** functions, basic mathematical proofs, and elementary logic; no proof-assistant experience required. **Theme:** proofs as structured witnesses, implication as a function, quantifiers as dependent types, and the distinction between truth and computation.

<!-- BEGIN SPOKEN LECTURE -->

# Proofs as Objects: Why Propositions Can Be Types

Imagine someone hands you a program and claims it will never return the wrong kind of answer. They show you a thousand successful tests. You may be impressed, but a thousand examples do not establish a universal claim. Perhaps the thousand-and-first input triggers a failure. Now imagine that, along with the program, they hand you a mathematical argument that covers every possible input. What sort of object is that argument? Could it have a structure that a machine can inspect without depending on the machine to be clever or trusting its author's intentions?

This question leads to an idea that connects logic, programming languages, foundations of mathematics, and formal verification: a proposition can be represented as a type, and a proof as a value inhabiting that type. That sentence sounds like a metaphor. We will make it literal. By the end, we will have constructed proofs in much the same way we construct programs, seen how mathematical quantifiers change the kinds of programs we need, and learned why some claims cannot be proved by simply producing a value.

Begin with a familiar statement: if an integer is divisible by four, then it is even. To justify it, take an arbitrary integer divisible by four. It has the form four times another integer. Rearranging gives two times twice that integer. Therefore it is even. A standard written proof tells a reader why the conclusion follows. But notice its executable shape. Given evidence that a number is four times an integer, we transform that evidence into evidence that the number is twice an integer.

The proof does more than report agreement with a conclusion. It describes a transformation from one sort of evidence into another. That transformation is a function in the mathematical sense. We can give it an input, and it produces an output of the required kind. This is the first connection to programming.

## What a type demands

In ordinary programming, a type constrains the possible values of a variable. A Boolean is either true or false. An integer is a whole number, positive, negative, or zero. A pair containing an integer and a Boolean must have both components. If I declare a function that accepts an integer, I cannot safely give it an arbitrary string and assume the meaning will be clear.

The type of a function is itself a description of what it expects and produces. A function from integers to Booleans takes an integer and returns a Boolean. A function from pairs of integers to integers could add the coordinates or select one of them. These functions have the same type even though their behavior differs. The type places conditions on a result without specifying everything about its contents.

Now consider the mathematical statement, P implies Q. We could ask what it would mean to possess evidence of this claim. One natural answer is: give me a proof of P, and I will give you a proof of Q. The proof of an implication is therefore a function from proofs of P to proofs of Q. The notation P arrow Q is doing two jobs at once: expressing logical implication and expressing the type of a function.

Try the simplest possible example. Suppose P is a proposition, and Q is another. We want a proof of the statement, if P and Q are both true, then P is true. Someone presents evidence for the conjunction. We take the first component. That is the proof. The argument has an input, a fixed operation, and an output. Nothing about P or Q needs to be inspected or guessed. The proof works for every pair of propositions.

It is helpful to make the direction explicit. A function that turns evidence of P into evidence of Q proves P implies Q. A function that turns evidence of Q into evidence of P proves the reverse implication. Those are different demands. Confusing the direction is as serious here as confusing the domain and codomain of an ordinary function.

A proof assistant based on dependent type theory can check whether a proposed term has the type assigned to a proposition. It need not determine whether the proposition is intuitively persuasive. It checks a structured derivation under explicitly stated rules. This division of labor is powerful: people invent definitions, choose lemmas, and discover arguments; the checker verifies that the submitted proof fits the logical system.

## A conjunction is something you can take apart

Suppose you want to prove P and Q. What would count as adequate evidence? You would need a proof of P and a proof of Q. Put those two pieces together as a pair. Conversely, given a proof of P and Q, you may extract either member. These are called introduction and elimination rules, but the everyday names are simpler: build the pair, and take it apart.

Disjunction behaves differently. To prove P or Q constructively, you can present a proof of P and mark it as the left alternative, or present a proof of Q and mark it as the right alternative. To use a proof of P or Q, you must be prepared for either case. This is the logical version of handling a program value that might have one of two possible variants.

For example, suppose a device sends either an integer reading or an error report. To process a result safely, a program must handle the integer case and the error case. In the logical interpretation, a proof of a disjunction carries the information about which branch is supported. That makes constructive reasoning surprisingly similar to a typed case analysis.

Be careful with the word proof. In the logical fragment we are describing, the representation tells us how to construct and use evidence. There are variants of type theory, and proof assistants can deliberately erase information irrelevant to computation. In Lean, for instance, propositions live in a special sort called Prop, and proofs of the same proposition are treated as proof-irrelevant. It would be misleading to say that a Lean proof always contains runtime data that can be extracted like an ordinary list or pair. The analogy is exact at the level of typing and proof rules; computational behavior depends on the language and its treatment of propositions.

## The excluded middle is a real dividing line

Consider a claim that every proposition P satisfies P or not P. Classical logic accepts this law of excluded middle. A constructive proof must ordinarily do more than assert that some alternative is correct: it must supply the evidence required for a disjunction, including a branch. For an arbitrary proposition, we may have no method that determines which branch holds.

This does not mean constructive mathematicians believe classical mathematics is wrong. They are asking what can be established using proof rules that preserve computational evidence. In a constructive setting, existence and disjunction often demand an explicit witness or method. Classical reasoning permits additional principles that can prove a disjunction without computing which alternative holds.

As a small example, take the claim that a real number is either rational or irrational. In classical mathematics, this is immediate from excluded middle applied to rationality. Constructively, deciding rationality for an arbitrary abstract real number can require information not supplied by its representation. The words 'arbitrary real' hide a crucial choice about how a real number is given to us. One cannot automatically turn a classical classification into a general terminating program that settles the question.

The distinction becomes practical when developing verified algorithms. Sometimes a theorem asserting that an answer exists is enough. Other times you need an algorithm that computes the answer. A proof system can express both goals, but the hypotheses and the forms of evidence differ. A careful formalization makes that difference visible before one confuses theorems with executable procedures.

## Universal claims are programs that accept an argument

A mathematical sentence can say something about one fixed object or something about every object of a certain kind. 'Every natural number has a successor' is the second sort. To prove it, begin with an arbitrary natural number n and construct n plus one. This is a function from natural numbers to witnesses of successorhood.

In ordinary mathematics, we write 'for every n, P of n.' In dependent type theory, the corresponding proof object resembles a function that accepts n and returns a proof of P of n. The output type depends on the input. If n is four, the function returns a proof about four. If n is one thousand, it returns a proof about one thousand. This dependence is what makes the type richer than an ordinary function type with a single fixed codomain.

Think of a box-making program. Given a width n, it returns a vector with exactly n elements. A list contains elements but generally does not encode its length in the type. A length-indexed vector does. The return type varies with the input width, so a vector of length three and a vector of length four have different types. A program that promises a vector of length n must satisfy the promise for the actual n it receives.

Now the analogy between universal quantification and dependent functions is concrete. A universal statement is a family of obligations indexed by objects. A proof is one construction that discharges the appropriate obligation for any supplied index. The quantifier is not just a word placed at the front of a sentence; it changes the structure of the evidence needed.

## Existence needs a witness

Existential claims have a different direction. To establish that there exists a natural number greater than five, select six, and then prove six is greater than five. The evidence comes in two pieces: the witness and a proof that the witness satisfies the claimed property. A dependent pair is the natural type-theoretic representation of this structure.

In many type theories, dependent sums are written with a capital sigma. One component specifies the object, and the second component has a type determined by that object. A sigma of n and a property of n represents a witness together with evidence that it meets the requirement.

We should distinguish this mathematical picture from a particular implementation. In Lean, the existential quantifier over propositions is represented by `Exists` in Prop, and a dependent pair `Sigma` is a data structure in Type. Their introduction rules look related, but elimination and computational use are not identical. Since Lean treats proofs as proof-irrelevant, you generally cannot extract arbitrary computational data from a proof of existence into an executable Type-valued function. If an algorithm must return a witness, state its result in a suitable data-bearing type and supply the computational construction.

This is a lesson in specification design. If I only want assurance that a solution exists, a proposition may be appropriate. If I need a verified solver to return a solution with a certificate, a dependent pair or a subtype in a computational context may be closer to the contract. Mathematically similar sentences can impose quite different engineering requirements.

## A proof that combines two implications

Let's build something more interesting. Suppose we know P implies Q and Q implies R. We want to prove P implies R. Start with a hypothetical proof of P. Feed it into the first implication to obtain a proof of Q. Feed the result into the second implication to obtain a proof of R. The combined transformation is just function composition.

That small proof exposes an important fact. Logical consequences can be composed. The type of the first proof tells us where the output goes, and the type of the second tells us what input it accepts. We can discuss this with the language of categories: propositions act like objects, implications like arrows, and composition like chaining reasons. But the proof-as-program interpretation provides more detail than an unstructured arrow. It explains the construction that carries evidence through the chain.

Take the proof apart carefully. We are given two functions, one from P to Q and one from Q to R. We must produce a function from P to R. We do not magically construct a value of P. We assume someone supplies one, then explain what we would do with it. A proof of implication can exist when its premise is false, because the proof only commits to converting any given evidence of the premise; it does not promise that such evidence can be produced.

This distinction prevents another common mistake: believing that a proof of P implies Q proves Q outright. The implication needs a premise. In a typed setting, the missing premise is a missing argument to the function. The analogy makes the logical error almost tangible.

## Equality is more than printing the same answer twice

Programs need to establish that operations preserve invariants: a list's length remains nonnegative, a parser returns values of the declared kind, a rotation maintains distances, a numerical method respects specified bounds. These are propositions about values and functions. When those propositions become types, they can appear in the declarations of programs and theorems.

But equality requires care. Two expressions might simplify to the same value according to the computation rules of a language. Alternatively, we might have to prove a mathematical theorem connecting them. Type theory distinguishes conversion by computation from equality that must be established using a proof. A machine can normalize an elementary arithmetic expression, yet it will not automatically accept every true equality between arbitrary mathematical objects without the appropriate proof.

For instance, 'adding zero leaves a number unchanged' can be computationally immediate in one direction for recursively defined natural-number addition and require induction in another direction, depending on which argument the recursion examines. The underlying mathematical equation is symmetric, but the program's reduction rules may be asymmetric. This difference is one reason formalization teaches precise habits: it forces us to ask whether a statement is true by the definition, by a theorem, or by an assumption.

## Where did this connection come from?

The link between formal proofs and programs did not arrive from a single inventor working in isolation. Haskell Curry and others developed correspondences between systems of combinators and logical deduction. William Alvin Howard circulated notes in 1969, later published as 'The Formulae-as-Types Notion of Construction,' explaining a striking match between natural deduction and typed lambda calculus. Under that correspondence, introducing an implication resembles constructing a function, and using the implication resembles applying it.

It is tempting to tell this history as a succession of inevitable discoveries. It was instead a meeting between several lines of research: philosophical work on constructive mathematics, mathematical logic, type systems, and the practical need for reliable programming languages. Different communities cared about different questions. Some wanted to characterize valid reasoning. Others wanted to describe computation. Others wanted machines to check complex theorems without asking humans to inspect every detail.

The correspondence became important precisely because these objectives began reinforcing one another. One can learn a great deal about proofs by studying programs, and about programs by studying proofs. Neither viewpoint eliminates the other. The act of finding an insightful mathematical argument remains a creative problem, while the resulting object can be subjected to formal checking.

## The first serious obstruction: what can the checker know?

A proof assistant has a small logical core and a much larger surrounding environment. The environment elaborates convenient notation, searches for lemmas, applies automation, and simplifies expressions. The core checks that the final term is valid under the system's rules and declared axioms. This separation is often described as a small trusted kernel. The word small refers to the intended scope of trusted reasoning, not a guarantee that every installed system is bug-free or every imported axiom is philosophically uncontroversial.

A proof checker cannot turn an incorrect mathematical specification into the intended one. Suppose we accidentally prove that our algorithm returns some number, when we meant to prove it returns a minimum. The proof may be formally valid and practically irrelevant. Or suppose an algorithm is formalized using an assumption inconsistent with its intended execution environment. A rigorous derivation does not repair a mistaken premise.

That is why a full understanding of type theory includes its boundary with mathematical modeling. The types and propositions must express the right task. The proof must establish the stated properties. The final implementation must correspond to the objects being modeled. Each of those is a separate obligation. Formal methods let us make these obligations explicit and connect them, but they do not relieve us of judgment.

## The place where dependent types really earn their complexity

Return to the length-indexed vector. Suppose we want a function that concatenates a vector of length m and a vector of length n. The result should have length m plus n. That is a declaration strong enough to rule out whole classes of mistakes before a program runs. If we implement concatenation recursively, the shape of the result and its declared length must agree at every constructor step.

One way to build a vector is with two constructors. The empty vector has length zero. Given a vector of length n and an element, we can attach that element and obtain a vector of length n plus one. The type records the relationship between the data structure and the count. An induction proof about vectors can follow exactly the constructors that define them.

At this point, 'proof as a value' is no longer a curious slogan. It suggests a design method: represent the invariant in the type, construct values only through operations that preserve it, and use the checker to reject code that loses track of the invariant. For another problem, the type might record a matrix dimension, a sorting relation, a valid syntax tree, or the preconditions for a certified numerical result.

Not every invariant belongs inside a type. Extremely dependent interfaces can make simple code hard to write, and some properties require substantial theorems about operations. The useful question is which commitments should be carried by ordinary data, which by checked proofs, and which remain assumptions about the world outside the formal system.

## What we have actually established

We began by asking whether a proof could be an object a machine checks. For implication, a proof behaves like a function transforming evidence of the premise into evidence of the conclusion. For conjunction, it contains both pieces of evidence. For disjunction, it distinguishes alternatives. For universal claims, it supplies a family of proofs indexed by inputs. For constructive existence, it provides a witness together with evidence that the witness qualifies.

From those examples, the central idea follows. A type can state a contract about a value. A proposition can state a contract about mathematical evidence. A dependent type can express a contract whose content changes with the input. We can prove implications by building functions, prove universals by accepting arguments, and prove properties of recursive data by following its constructors.

The final distinction is perhaps the most important. Mathematics contains questions of truth, computation, and specification. These overlap, but they are not identical. Type theory gives us a language precise enough to see where one question ends and another begins. When a theorem proves the correct property of a correctly modeled object, the result is more than a reassuring statement. It is a piece of structured evidence that can be checked, reused, and composed with other mathematical results.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Core correspondences

| Logic | Type-theoretic construction | Evidence |
|---|---|---|
| \(P\Rightarrow Q\) | \(P\to Q\) | Function transforming proofs |
| \(P\wedge Q\) | Product-like constructor in `Prop` | Proof of both |
| \(P\vee Q\) | Sum-like constructor in `Prop` | Left or right proof |
| \(\forall x:A,\ P(x)\) | Dependent function \(\prod_{x:A}P(x)\) | Construction for each \(x\) |
| \(\exists x:A,\ P(x)\) | `Exists` in `Prop`; analogous to \(\Sigma\) in computational `Type` | Witness and predicate proof, with elimination restrictions |

### Elementary Lean illustrations

```lean
example (P Q : Prop) : P ∧ Q → Q ∧ P :=
  fun h => And.intro h.right h.left

example (P Q R : Prop) : (P → Q) → (Q → R) → P → R :=
  fun f g hp => g (f hp)

example (P : Nat → Prop) (h : ∀ n, P n) : P 7 := h 7
```

These examples use no classical axioms. In Lean, `Prop` is proof-irrelevant; `Sigma` carries Type-valued data, while `Exists` is a proposition. A constructive `Exists` proof does not generally supply executable data through elimination into `Type`.

### An equality example

For natural numbers, the definitional behavior of `n + 0` and `0 + n` depends on the recursive definition of addition; an equality may be definitional in one orientation and require a theorem or induction in the other. Avoid declaring both directions definitional.

### Exercises and answers

1. **Exercise:** Given `P → Q` and `Q → R`, what proof term establishes `P → R`? **Answer:** `fun h => g (f h)` if `f : P → Q`, `g : Q → R`.
2. **Exercise:** What extra output must a program return to establish constructive `∃ n : Nat, n > 8` as data? **Answer:** A witness such as nine and evidence `9 > 8`, e.g., a dependent pair or subtype.
3. **Exercise:** Why does `P → Q` alone not establish `Q`? **Answer:** It is a function waiting for a proof of `P`; none has been supplied.
4. **Exercise:** Which part of a specification can a proof assistant fail to detect? **Answer:** Whether the proposition faithfully expresses the informal intent or physical assumptions.

### References

- Jeremy Avigad, Leonardo de Moura, Soonho Kong, Sebastian Ullrich, *Theorem Proving in Lean 4*, chapters 2–4, https://leanprover.github.io/theorem_proving_in_lean4/
- W. A. Howard, “The Formulae-as-Types Notion of Construction,” circulated 1969, published in *To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism* (1980).
- Per Martin-Löf, “Intuitionistic Type Theory” (1984), https://www.cs.cmu.edu/~rwh/courses/chtt/pdfs/martinlof84.pdf
