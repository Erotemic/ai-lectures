# 007000 — Dependent Pattern Matching: Why Some Cases Cannot Happen

**Track:** Logic, Type Theory, and Constructive Mathematics. **Background:** inductive types, equality proofs, transport. **Theme:** indexed inductive families, dependent elimination, impossible branches, and the link between high-level pattern matching and core recursors.

<!-- BEGIN SPOKEN LECTURE -->

# Dependent Pattern Matching: Why Some Cases Cannot Happen

Suppose you are writing a function that returns the first element of a vector. Not a list, but a vector whose length is recorded in its type. The function accepts only vectors of length at least one. In an ordinary list implementation, you need to decide what to do with an empty input: raise an error, return an option, or assume the caller behaved. With a vector indexed by its length, the empty case is not merely unlikely. It is inconsistent with the input type.

That sounds like exactly what we want from a safe interface. But it raises a question. If a vector is built with either the empty constructor or the constructor that attaches a head, why can the function omit the empty constructor? Doesn't a pattern match have to consider every constructor?

The answer requires more than looking at the shape of the data. We have to look at what each constructor says about the vector's *index*. A constructor is not always a way of building a value at every index. Some constructors build values only at very specific indices. When an index appears in the type of the value being inspected, pattern matching simultaneously learns information about the index. This is dependent pattern matching.

We will see how the empty branch becomes impossible, why the type of a result can change after a match, what the equality eliminator has to do with it, and how a proof assistant can accept a convenient pattern-match notation without trusting the pattern-matching compiler as a new logical axiom.

## An indexed family of finite lists

Define Vector of A and n to mean a finite sequence of values of type A, with exactly n elements. It has two constructors. Empty constructs a vector of length zero. Cons takes an element of A and a vector of length n, and returns a vector of length n plus one.

These constructors do not have a common fixed result type. They return values in different members of the family. Empty belongs to Vector of A and zero. Cons belongs to Vector of A and successor of n. A value of Vector of A and five can only have been built by the cons constructor; empty is a constructor of the family, but it cannot inhabit that particular indexed type.

Now define head for a vector whose length is the successor of n. Its output is an element of A. The input length is known to be positive, so only cons is possible. In mathematical language, the empty case would require an equality between zero and a successor of n. The natural numbers' constructors are disjoint, so that equality cannot be proved. There is nothing to return in the empty case because the case cannot occur.

This is very different from attaching a runtime assertion to a list. We have not examined an arbitrary list and checked its length. The function's input type rules out empty vectors from the start. Of course, to *construct* an admissible argument, someone else has to supply a vector whose index is a successor. The obligation has moved to the caller or to the constructor that produces the input.

This technique is useful whenever a datatype contains a meaningful invariant. A parser could return a syntax tree indexed by a grammar category. A matrix could be indexed by dimensions. A machine state could carry a phase that determines which transitions are legal. The index tells us something beyond the value's raw shape.

## Why an ordinary match is not quite enough

For a plain list, a match can return a fixed type B in every branch. Nil returns one B. Cons returns another B. This is a familiar nondependent case split: whichever constructor we encounter, the goal type stays the same.

For a vector, the correct result type may depend on the length discovered by the match. Consider taking the tail of a nonempty vector. The input has type Vector of A and n plus one. The output should have type Vector of A and n. The cons constructor exposes a tail whose length is some k. To return it at length n, the checker needs to know k equals n. That equality comes from comparing the constructor's output index, successor of k, with the input index, successor of n.

There is a hidden reasoning step here. Because the successor constructor on natural numbers is injective, successor of k equals successor of n implies k equals n. Once we have that equation, we can transport the tail from Vector of A and k to Vector of A and n. A high-level dependent match may perform this inference for us, but a foundational account must explain why the result type is valid.

Think of the match as doing two things at once. It inspects the shape of the value, and it refines what the context knows about the index. In the empty branch it derives contradictory index information and dismisses the branch. In the cons branch it obtains a new index k and an equation relating k to n. Those facts justify the returned value.

An ordinary nondependent eliminator does not necessarily make all of that convenient. We may need to choose a result family, called a *motive*, that mentions the index and the value being examined. Instead of demanding the same result type in every case, the motive says what type must be produced for each possible index and constructor instance. Modern proof assistants offer syntax and elaboration mechanisms to infer that motive from the function we want to write.

## How an impossible branch is justified

Let's examine the impossible case carefully rather than waving it away. Suppose an empty vector had type Vector of A and successor of n. By its constructor declaration, the empty vector has length zero. So type compatibility would require zero equals successor of n. The natural numbers are an inductive type with distinct constructors zero and successor. Constructor disjointness says no proof of zero equals a successor exists.

In a dependent pattern match, a branch can become impossible because the index equations inferred from the scrutinee type are inconsistent. The corresponding elimination can use a contradiction to produce a value of any result type, not because contradictions are allowed, but because there are no inhabitants of the impossible branch from which a concrete bad result could arise.

That last point is central to soundness. If a system incorrectly deleted a genuinely possible branch, a program might become stuck at runtime or a proof might establish a false conclusion. A proof assistant cannot safely decide that a branch is impossible just because a heuristic finds it inconvenient. The impossibility must be justified by the constructor and equality rules of the theory.

The converse is also important. A programmer may know from a sophisticated theorem that a certain branch cannot occur, but the dependent pattern matcher may not automatically discover the theorem. A branch can be mathematically impossible without being syntactically eliminated by simple index unification. The programmer may have to provide the missing equation or contradiction explicitly.

## Pattern matching is not a new foundational oracle

In Lean, convenient pattern matching is elaborated into functions and applications of generated recursors. For indexed inductive families, this transformation may introduce auxiliary matching functions, equality constraints, and transports. The elaborator is allowed to search for a suitable construction. But the core term it produces is checked by the kernel according to the calculus's accepted rules.

This separation is a reliability advantage. A bug in the high-level pattern compiler should ordinarily lead to a generated term that fails to type check, not to the addition of a new trusted inference rule. The kernel must still be trusted, and there are subtleties around which constructs and axioms the language admits, but the convenient surface syntax does not automatically enlarge the logical foundation.

The distinction resembles compiling a high-level programming language to a small instruction set. The frontend may perform sophisticated transformations and optimization, while the backend executes only the established instructions. For proof assistants the analogy is stronger: the generated artifact can carry a formal type that the checker verifies independently of the frontend's reasoning.

There are limits to the analogy, however. A conventional compiler is expected to preserve operational behavior, while a proof elaborator is expected to produce a term inhabiting a specified type. A term can type check yet fail to be the program the human intended if the specification was too weak. Verification of the generated proof term does not automatically verify that the *statement we chose* expresses the application requirement.

## The role of motive selection

Suppose we define the property that every vector can be mapped elementwise while preserving its length. The output type of mapping should be Vector of B and n when the input has type Vector of A and n. If we inspect an empty input, the result is an empty vector of B at length zero. If we inspect a cons input, the result is a cons of the transformed head and recursively mapped tail, at successor length.

Why can we claim that the output length matches the input length? Because the motive says so for each index. For every n and every input vector of length n, the result should be a vector of length n. The empty branch fulfills the motive at zero. The cons branch fulfills it at successor of n, assuming recursive fulfillment for the tail. The index-preserving property is not a separate afterthought; it is the very type of the recursive construction.

For a different function we might choose a different motive. To prove every vector of length n has ordinary-list length n, the result family is a proposition about the vector. To concatenate vectors, the result family must account for the sum of the input lengths. Depending on which argument recursion follows and how addition is defined, some length equalities compute and others require rewriting. This is exactly where the preceding distinction between definitional equality and proved equality becomes operational.

Motive selection is powerful, but it can make an error message look mysterious. The checker says two indexed types do not match even though the underlying lists appear identical. Often the problem is not the list-processing algorithm. It is the arithmetic equation required to reconcile the indices. A good diagnosis asks: which index was known before the match, which index did the constructor reveal, and which equality would connect the two?

## Finite indices as an interface contract

A related datatype is Fin of n, the type of natural numbers strictly below n. Fin of zero has no inhabitants. Fin of five has exactly five possible index values. If a vector is indexed by n, then indexing it by a value of Fin of n cannot refer outside its bounds.

In an ordinary array program, we might accept an integer index and separately check whether it lies between zero and n minus one. In a dependently typed interface, that bound is part of the argument type. The function accepts only legitimate indices. If we pass a particular index, such as three, we must still supply evidence that three is below n, or construct it in a context where that bound is known. The runtime array access may be inexpensive, but the type-level guarantee has already constrained the set of admissible calls.

Now imagine we split a vector of length n plus m into two pieces. We might want to map an index less than n into the first piece and an index between n and n plus m into the second. The necessary inequalities form the mathematical content of the implementation. Indexed types can prevent us from forgetting them, but they cannot prove an inequality by wishful thinking.

For verification, this shifts the center of effort. Instead of sprinkling defensive checks throughout the implementation, we state invariants at the boundaries and prove that transformations preserve them. Those proofs can be reused, but they must be designed to match the actual transformations.

## When the index is a proposition

Indexed inductive families also encode derivations. Suppose an inductive predicate Even of n has a constructor for zero and a constructor that takes evidence of Even of n and produces evidence of Even of n plus two. A proof of Even of seven cannot be formed by repeatedly applying those constructors starting at zero. If we attempt to invert such a proof, the index equations expose the contradiction.

This is the same mechanism as the empty-vector case. The family does not merely store a number and a Boolean label. It stores derivations whose constructors constrain the index. The elimination principle allows proofs by examining the possible derivation constructors, while respecting how the indices change in each case.

There is a subtle distinction between a datatype of evidence and an arbitrary decidable predicate. A proof of Even of n records how n was built from evenness constructors; a decision procedure might simply compute n modulo two. Both can justify the same mathematical proposition, but the evidence representations and their computations can differ. Proving they agree is often a useful bridge between logical and algorithmic views.

## Limits and design choices

Indexed types are not automatically the best interface for every program. An enormous amount of arithmetic transported through types can obscure an otherwise simple algorithm, and a caller may need a practical runtime error for invalid external input rather than a theorem that such input could never be supplied. It can be wise to validate raw input at the boundary, then convert it into a representation that carries invariants for internal processing.

There are also different notions of dependently typed programming. A rich typed core may permit direct dependent pattern matching with computational equality, while a system like Lean distinguishes propositions from ordinary data and uses elaboration to make inductive elimination ergonomic. Proof irrelevance and classical axioms affect what can be computed from proofs. We should not infer operational behavior from the phrase 'dependent types' alone.

Return to our head function. Its safety is not a clever run-time trick. It is a consequence of the constructors of an indexed family and the fact that zero cannot equal a successor. The empty branch has no valid input; the cons branch exposes exactly the data we need. Transport and equality explain how the indices line up. A proof assistant's pattern matcher may hide this work, but the justification remains a mathematical argument about constructors, indices, and dependent elimination. This is how a data structure can carry a proof of which cases are possible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Indexed vectors

An indexed inductive presentation:

```lean
universe u
inductive Vect (α : Type u) : Nat → Type u where
  | nil : Vect α 0
  | cons {n : Nat} : α → Vect α n → Vect α (n + 1)
```

Constructor disjointness excludes \(\mathrm{nil}\) at successor length, because \(0\neq n+1\). Injectivity of successor provides \(k+1=n+1\implies k=n\).

### The motive

Schematic vector induction:
\[
\begin{aligned}
P&:\prod_{n:\mathbb N}\mathrm{Vect}(A,n)\to\mathsf{Type},\\
P(0,\mathrm{nil}) &\quad\text{(base)},\\
\prod_{n:\mathbb N}\prod_{v:\mathrm{Vect}(A,n)}\prod_{a:A}\bigl(P(n,v)&\to P(n+1,\mathrm{cons}(a,v))\bigr)\quad\text{(step)}.
\end{aligned}
\]
Given suitable base and step arguments, elimination supplies \(\prod_n\prod_{v:\mathrm{Vect}(A,n)}P(n,v)\).

An index-preserving map has type
\[
 \mathrm{map}:(A\to B)\to\prod_n\mathrm{Vect}(A,n)\to\mathrm{Vect}(B,n).
\]
The motive is \(P(n,v)=\mathrm{Vect}(B,n)\). Pattern matching constructs `nil` at zero and `cons` at successor length.

### Finite indices

\(\mathrm{Fin}(n)=\{k\in\mathbb N\mid k<n\}\), as a subtype-like representation. The type \(\mathrm{Fin}(0)\) is empty. An indexed lookup has schematic type
\[
 \mathrm{lookup}:\prod_n\mathrm{Vect}(A,n)\to\mathrm{Fin}(n)\to A.
\]
No `Fin 0` argument exists for an empty vector.

### Exercises with answers

1. **Impossible branch.** Why is there no `nil` branch for a function accepting \(\mathrm{Vect}(A,n+1)\)? **Answer:** `nil` would impose \(0=n+1\), impossible by constructor disjointness.
2. **Tail index.** A cons input exposes a tail of length \(k\). How do we justify a return type indexed by \(n\)? **Answer:** obtain \(k+1=n+1\), use successor injectivity to prove \(k=n\), then transport if necessary.
3. **Map motive.** What must be preserved by the recursive step in vector mapping? **Answer:** the tail's length index, so a mapped cons has index \(n+1\) when the original did.
4. **Fin.** Explain why a function \(\mathrm{Fin}(0)\to A\) can be defined for any \(A\) without giving a value of \(A\). **Answer:** its input type has no inhabitants, so there is no case to compute.

### References

- *Theorem Proving in Lean 4*, “Induction and Recursion,” section “Dependent Pattern Matching.”
- Lean 4 Reference Manual, “Terms: Pattern Matching” (inaccessible patterns, explicit motives, index generalization).
- Per Martin-Löf, *Intuitionistic Type Theory* (1984), families and induction.
