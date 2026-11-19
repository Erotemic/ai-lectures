# 008000 — What Does a Proof Assistant Actually Check? Elaboration, Kernels, and Meaning

**Track:** Logic, Type Theory, and Constructive Mathematics. **Background:** propositions as types, equality, inductive recursion, and dependent elimination. **Theme:** the difference between a theorem statement, a tactic's search, the term that the kernel checks, computation, and explicit axioms.

<!-- BEGIN SPOKEN LECTURE -->

# What Does a Proof Assistant Actually Check? Elaboration, Kernels, and Meaning

A mathematician asks a proof assistant to prove a theorem. A few lines of tactics run. The editor announces that the goals are closed. What exactly has happened? Has the machine discovered a proof? Has it executed the theorem on every possible input? Has it verified the intended meaning of the problem? Or has it simply accepted that the tactic reported success?

The answer depends on the architecture of the proof assistant, but systems built around a small logical kernel make a powerful separation. The convenient language in which humans write proofs may be complex. It may infer arguments, invent names, search libraries, simplify expressions, and call external algorithms. But the trusted checker accepts a much smaller form of evidence: a term whose type is the proposition asserted. The checker does not have to trust the reasoning procedure that found the term.

That separation is the result of a long interaction between logic, programming-language semantics, and software engineering. It is worth understanding carefully, because there are two opposite mistakes one can make. The first is to imagine a proof assistant as an infallible oracle that understands whatever a human intended. The second is to dismiss it as a fancy text editor that merely rubber-stamps generated arguments. Neither is right.

We will follow one theorem from a human-facing statement to a core typing judgment, examine which assumptions a proof can depend on, and see what it means for computation and verification to meet inside a dependent type theory.

## What the theorem actually says

Imagine a function that sorts a list of integers. The user claims, 'My sorting routine is correct.' There are at least two independent requirements. The result must be ordered, and it must contain the same elements as the input, with the same multiplicities. A routine that returns the empty list is always sorted. It nevertheless loses all the input elements. Proving only sortedness would certify the wrong specification.

Before a checker can help, we must express the requirements in a formal language. We need a type of input lists, a function that returns a list, a predicate saying the result is sorted, and a relation saying its multiset of entries agrees with the input's. The theorem can quantify over every input list and assert both properties. Only then is there a proposition for the checker to verify.

The first point is easy to underestimate. A proof assistant can establish that a term inhabits the formal type we supplied. It cannot, simply by checking that proof, establish that the type captures all the real-world requirements. The intended specification is partly a mathematical modeling obligation. It deserves tests, review, examples, and connections to the system being verified.

In type-theoretic notation, the central judgment has the form: under assumptions collected in a context called gamma, the term t has type A. If A is a proposition, t is a proof of A. If A is a datatype, t is a value or program of that type. This is one of the points of the propositions-as-types interpretation: the same typing discipline can describe data and mathematical evidence.

## Elaboration: from readable syntax to an explicit term

Humans rarely want to write the fully explicit core term. Consider a function that maps over a list. A caller might not mention the element type because the checker can infer it. A theorem might use overloaded notation for addition, with the intended operation determined by a type-class argument. A proof might rely on implicit universe parameters, syntactic sugar for pairs, or pattern matching that must be compiled into recursor applications.

The elaborator resolves these conveniences. It chooses inferred arguments, disambiguates overloaded symbols, synthesizes type-class instances, elaborates pattern matches, and turns the surface expression into a more explicit term. When the elaborator needs an equality proof to reconcile dependent indices, it may insert one. When it cannot solve a constraint, it reports an elaboration error.

Elaboration can be sophisticated. It is allowed to guess, backtrack, and use heuristics. This is useful because writing full core terms would be tedious for most mathematics. But elaboration is not the final authority on whether a theorem is valid. Its output must be a term of the required type according to the accepted core typing rules.

This is why it matters that dependent pattern matching is elaborated into recursors and equality eliminations. The convenient syntax is not a new law of logic. It is a method for producing a term whose construction can be checked by a smaller system.

## Tactics as programs that construct proofs

A tactic like 'apply this theorem' tries to transform the current goal into premises required by another theorem. A tactic like 'rewrite' uses an equality to transform an expression. An induction tactic chooses an eliminator and creates cases. A simplifier searches through selected equations and reduction rules. A decision procedure may carry out a nontrivial computation and then supply evidence connecting the computed result to the proposition.

From the user's perspective these operations manipulate goals on a screen. At the foundational level the desirable result is a proof term. Closing a goal means all the required pieces have been assembled into evidence accepted by the checker. The user need not inspect every reduction of that term, but the fact that it is checkable matters.

We can compare this with an ordinary scientific computation. A numerical solver outputs an approximate answer, perhaps with a residual and a backward-error estimate. Its correctness depends on the algorithm, floating-point behavior, and a theorem relating the residual to the intended solution. In a proof assistant, a tactic may also produce a complicated output, but that output can be a formal certificate whose validity is checked by rules much smaller than the search procedure.

The certificate can still be large, and verification may be expensive. Keeping the checker small does not make proof search easy, nor does it eliminate implementation bugs. It does, however, put an architectural boundary around what must be trusted for ordinary proof-term checking.

## What the kernel knows

The kernel checks typing and definitional conversion. It knows how variables are scoped, how dependent functions are formed and applied, which inductive constructors and eliminators are valid, and which computation rules are part of the theory. It checks that a proposed proof has the claimed proposition as its type.

Consider proof by induction. In a surface proof, we might write 'induction on n' and then provide base and step cases. The kernel need not trust the phrase 'induction' as an unexplained command. The generated core term applies the natural-number eliminator to the base and step evidence. The eliminator's type expresses the induction principle. The kernel checks that each piece has the required type.

Similarly, when a rewriting tactic replaces an expression using an equality theorem, the resulting proof contains justified equality eliminations or congruence constructions. The tactic may choose a useful order of rewrites, but the kernel checks that each transformation is licensed by proof terms or definitions.

Not every accepted declaration expands into a long proof term made entirely of elementary inference steps. A theory may have primitives or explicitly declared axioms. Checking means checking relative to those accepted rules and assumptions. We must therefore distinguish the trustworthiness of *checking a term* from the strength of the *foundation in which that term is checked*.

## Computation, reduction, and proof search are not the same

Suppose the proposition says that two concrete natural-number expressions are equal. If both reduce to the same canonical numeral, reflexivity may suffice. The kernel can use definitional equality as part of type checking. This is computation inside the logic.

Now suppose the proposition says a complicated polynomial is always nonnegative. A symbolic algebra tactic may normalize the polynomial, search for a certificate, or invoke a specialized decision procedure. The kernel does not know that every polynomial claim is true. The tactic must connect its calculation to the desired theorem through accepted reasoning, or the result must be explicitly marked as relying on a stronger trusted mechanism.

This distinction helps explain why some proofs run instantly and others consume minutes or hours. A theorem's mathematical simplicity need not correspond to the ease of normalization in a chosen representation. A computer can quickly evaluate a concrete arithmetic expression yet struggle to derive a general inequality; a human can recognize a structural invariant at once while a naive search enumerates countless useless rewrite sequences.

There is no contradiction. Computation, proof search, and proof checking answer different questions. The task of a good formalization is to choose definitions and lemmas that let the machine express the insight without requiring brute-force exploration of every possible argument.

## Axioms and what a proof depends on

Lean provides powerful mathematical principles as axioms or in ways that depend on axioms. Classical choice is one example. Proposition extensionality is another: it lets logically equivalent propositions be treated as equal propositions. A quotient-soundness principle allows equivalence classes to be identified according to the chosen relation.

These assumptions support ordinary classical mathematics, but they are not all mere reductions of concrete programs. A proof of a theorem using classical choice may be correct relative to the assumed theory while not providing a constructive algorithm for producing the chosen object. The distinction matters especially when the theorem is used as a software interface or as a claim about executable behavior.

There is also a deliberately unsafe placeholder mechanism: 'sorry' allows an unfinished proof to stand in for an actual justification. Internally this introduces an axiom strong enough to inhabit the missing proposition. A development containing a sorry can type check, but it has not established the theorem from the intended ordinary assumptions. Calling a file 'verified' without noticing the placeholder would be misleading.

A useful audit command asks what axioms a particular declaration depends on. That is different from asking whether the declaration type-checks. A theorem may type-check with the help of classical choice, with the help of quotient axioms, or with the help of an unfinished placeholder. A reviewer needs to know which foundation is intended.

Some performance-oriented proof mechanisms broaden the trust boundary in more specific ways. For example, Lean's reference manual explains that proofs accepted through native evaluation can introduce dedicated axioms whose soundness depends on the compiled computation. This is not the same trust story as checking a proof term built solely from the small kernel's ordinary reductions. It can be an appropriate engineering tradeoff, but it is important to describe the tradeoff accurately.

## Propositions, computational data, and erasure

A declaration proving that a number is prime is evidence of a proposition. A declaration returning a prime number is computational data. A dependent pair may combine a number with evidence that it is prime. These objects can look similar in a proof assistant but play different roles when compiled to executable code.

Lean distinguishes the universe of propositions from universes of data types. Proof irrelevance makes it possible to treat different proofs of the same proposition as indistinguishable for the logic, and proof arguments are generally not runtime data. By contrast, a natural number or a vector may have a computational representation that a program can inspect. Not every existence proof therefore yields usable executable witness data. Classical existential reasoning may establish truth without supplying an algorithm for computing a witness.

This does not make proof assistants bad at verified programming. It gives us a design decision. If a caller needs an actual witness, we can return data in a computational type and prove a theorem about it. If a property is required only to justify correctness, it can remain a proposition carried or referenced by proofs. The interface should make clear which part of a result the executable program can inspect.

## The word 'semantics' has several jobs

We have described an operational semantics of computation: which expressions reduce to which others. We have described a typing semantics: which terms inhabit which types. We can also speak about mathematical or denotational meaning: a proof term may be interpreted in a model of the underlying type theory. These are related, but they are not interchangeable.

An implementation can faithfully type-check an expression while the user has chosen an unintended mathematical interpretation of the input. A sorting theorem can be perfectly proved yet omit preservation of multiplicities. A numerical theorem can correctly bound exact real arithmetic yet say nothing about finite-precision rounding. A formalization can prove the correctness of a high-level algorithm yet fail to establish the fidelity of the compiled machine code or an external database it reads.

To connect those layers, we need correspondence theorems or trusted interfaces. A compiler correctness theorem relates source-level behavior to target behavior under stated conditions. A refinement proof relates a concrete implementation to an abstract specification. A verified numerical routine relates its rounded operations and outputs to a mathematical approximation guarantee. These bridges do not follow automatically from the fact that a proof assistant verified some nearby theorem.

The same caution applies to mathematics. If we formalize a theorem from a paper, we must ensure that its assumptions, definitions, and conclusion genuinely match the paper's mathematical claim. A formal result with a missing hypothesis may be false; a formal result with an accidentally stronger assumption may be true but fail to address the intended theorem. The kernel can protect the derivation only after we have given it the right statement.

## Universes and consistency pressure

There is one more structural detail that helps explain why foundational designs are careful. In Lean, types themselves have types, organized into a hierarchy of universes. A universe called Type sits inside a larger universe, rather than simply containing itself as an element at the same level. The hierarchy prevents certain self-referential constructions that would arise if arbitrary types could contain themselves without restriction.

These universe rules are not a complete proof that any concrete implementation has no defects, and consistency of a rich foundational system is a mathematical question relative to a metatheory. But they illustrate the design goal: make the rules precise enough that one can study their metatheory, test their implementations, and explain which assumptions are being made. A proof checker is trustworthy because its rules are explicit and small enough to analyze, not because it is infallible by decree.

## The actual trust contract

When someone says a theorem has been checked in Lean, the careful reading is that a declaration with a particular type has been accepted by Lean's kernel, subject to the axioms and trusted mechanisms it uses. That is a meaningful guarantee. It is stronger than 'the tactic printed success' and different from 'the theorem has been tested on many examples.' It is also narrower than 'the program works in every deployed environment' or 'the formal statement captures every intention of its author.'

A good mathematical development therefore has several layers of care. It formulates a specification that actually expresses the target result. It constructs arguments or programs within a stated foundational theory. It checks those arguments with a kernel. It audits axioms and placeholders. And when it claims something about executable software, numerical behavior, or an external system, it establishes the needed bridges between the formal object and the real artifact.

We began with a few tactics and an announcement that the goals were closed. We can now say what that announcement is supposed to mean: the elaborator found a core term, the kernel checked it against the formal proposition, and the result is valid relative to the theory's rules and assumptions. This architecture lets sophisticated search coexist with a modest trusted checker. It does not remove the mathematician's obligation to choose the right theorem. In fact, it sharpens that obligation by making the exact statement visible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Core judgments and conversion

The central typing form is \(\Gamma\vdash t:A\). Conversion allows \(\Gamma\vdash t:B\) when \(A\equiv B\) by the calculus's definitional-equality rules. This is different from deriving the proposition \(A=B\) and using transport.

A schematic pipeline:

```text
Surface Lean syntax / commands
       |
       v
Elaboration (implicit args, type classes, tactics, pattern compilation)
       |
       v
Core term and declaration dependencies
       |
       v
Kernel type check under declared axioms and reduction rules
```

This is a conceptual architecture, not a claim that all intermediate implementation objects have these exact names or that every evaluation mechanism uses the same trust boundary.

### Examples of assumption auditing

```lean
-- Lean 4 illustration: the first theorem is proved by a small term.
theorem id_imp (P : Prop) : P → P := fun h => h

#print axioms id_imp

-- The following, if admitted, is not a completed proof.
-- theorem unfinished (P : Prop) : P := by sorry
-- #print axioms unfinished
```

Check a declaration's axiom list before claiming a theorem is constructive or free of placeholders. Kernel acceptance alone does not mean its assumptions are empty.

### Model and implementation distinctions

- A formal specification may omit a requirement: `Sorted (sort xs)` does **not** imply that `sort xs` preserves every element of `xs`.
- A correctness theorem over exact real numbers does **not** by itself establish a floating-point error bound.
- Verification of an algorithmic specification does **not** by itself establish correctness of a native compiler, runtime libraries, or device I/O.
- An explicit `sorry` is an admitted obligation, not a derivation from the intended axioms.

### Exercises with answers

1. **Statement quality.** Why is `Sorted (sort xs)` insufficient for a sorting specification? **Answer:** a constant empty-list result could satisfy sortedness while losing input elements; add preservation of the input multiset.
2. **Tactic trust.** Why can an elaborate proof-search tactic be outside the kernel's trusted base? **Answer:** it produces a proof term whose type the kernel checks independently.
3. **Axiom audit.** What should be checked when a theorem relies on `Classical.choice`? **Answer:** whether classical choice is an intended assumption, and whether a computational witness is being claimed without an algorithm.
4. **Computational equality.** Is proving a symbolic algebraic identity equivalent to reducing a concrete numeral? **Answer:** not generally; reduction uses definitional computation, while symbolic identities may need theorems or certificates.
5. **Representation.** When does a mathematical proof establish that a compiled routine works? **Answer:** only with appropriate assumptions and correspondence between the formal specification, implementation, compiler, runtime, and environment.

### References

- *Theorem Proving in Lean 4*, “Dependent Type Theory,” “Inductive Types,” “Induction and Recursion,” “Axioms and Computation.”
- Lean 4 Reference Manual, “Axioms,” for `Classical.choice`, `propext`, `Quot.sound`, `sorryAx`, and native-evaluation trust notes.
- Benjamin C. Pierce, *Types and Programming Languages* (2002), operational semantics and type soundness.
- Per Martin-Löf, *Intuitionistic Type Theory* (1984), judgments, typing and computational meaning.
