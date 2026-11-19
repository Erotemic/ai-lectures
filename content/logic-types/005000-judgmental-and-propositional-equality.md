# 005000 — When Are Two Expressions the Same? Computation and Equality

**Track:** Logic, Type Theory, and Constructive Mathematics. **Background:** function types, induction, and simple recursive definitions. **Theme:** judgmental equality, propositional identity, reduction, and why an equality proof carries information that computation alone may not reveal.

<!-- BEGIN SPOKEN LECTURE -->

# When Are Two Expressions the Same? Computation and Equality

Suppose I have written the expression, three plus four. You have written seven. Our expressions look different, but no mathematical argument is needed to persuade anyone that they denote the same natural number. We calculate. Now suppose I have written, for every natural number n, zero plus n equals n. This sounds nearly as obvious. Yet in a precise formal language, those two equalities may require fundamentally different forms of justification.

The difference depends on how addition was defined. Some equations are consequences of computation: unfolding a definition and reducing an expression gets us from one side to the other. Other equations hold only because we can supply a proof, perhaps by induction, even though neither expression reduces to the other while a variable remains unknown. A proof assistant must keep these notions distinct. If it did not, checking a type could turn into an open-ended search for arbitrary mathematical theorems.

This lecture is about two judgments that are easy to conflate: an expression *computes* to the same expression as another, and an expression *is provably equal* to another. We will see why the distinction matters for the shape of a proof, for the performance of a checker, and for the identity types of dependent mathematics.

## Equality built into computation

Begin with a tiny function. Double of a natural number takes n and returns n plus n. If I apply double to three, I can unfold the name, replace the parameter by three, and compute three plus three. This is not a theorem about every possible function called double. It is the computational behavior specified by this particular definition.

Lambda expressions have a reduction rule: applying a function defined by a lambda expression substitutes the actual argument into the body. Inductive datatypes have reduction rules too. If we define a function by cases, applying it to a known constructor selects the corresponding case. Projections of a constructed pair reduce to its components. A name with a transparent definition may be unfolded, and a local definition may be substituted for its name. These forms of reduction are often called beta, iota, delta, and zeta reduction. Their names are less important than their common property: they are licensed by the rules of the calculus, not by an arbitrary mathematical assertion supplied later.

A type checker can treat expressions related by these built-in computations as definitionally, or judgmentally, equal. In a formal judgment, the checker can say that two types are interchangeable because reduction already identifies them. Think of it as an equality of descriptions after the system has done its authorized bookkeeping. If the expected type is a vector of length two plus three, and the produced value has a length that computes to five, the checker can often see the agreement without being handed a separate theorem.

This is sometimes called conversion. Suppose an expression has type A, and A is definitionally equal to B. The same expression may be used where B is expected. No cast object has to be inserted for a mathematical proposition that has not yet been proved. The conversion is part of the typing rules themselves.

But definitionally equal does not mean textually identical. A variable can be renamed without changing what a bound variable denotes. A function application can reduce. A match against a known constructor can reduce. It also does not mean merely that two expressions will produce the same answer after some external experiment. The type checker uses a specified notion of reduction and conversion. In particular, a theorem about two opaque mathematical functions does not become a built-in reduction rule just because a human knows the theorem.

## A recursive definition determines which equalities compute

Let us define addition in a deliberately asymmetric way. Fix the first argument m. Declare that m plus zero computes to m. Declare that m plus the successor of n computes to the successor of m plus n. These two equations define addition by recursion on the second argument.

Take seven plus the successor of two. The second argument has a visible constructor, so the second equation unfolds immediately. It becomes the successor of seven plus two, and can keep reducing. Now take seven plus an unknown variable n. The checker cannot see whether n is zero or a successor, so the recursive equation cannot choose a case. That expression may be stuck until more is known about n.

In this chosen definition, m plus zero equals m is a computation rule. Zero plus n equals n, with n still a variable, is not established simply by unfolding the recursive definition. We prove it by induction on n. At zero, both sides reduce. At a successor, the defining equation reduces zero plus successor of n to successor of zero plus n. The induction hypothesis lets us replace zero plus n by n, giving successor of n. The theorem is short, but it performs work that pure reduction does not perform.

If we had chosen the other argument as the recursive one, the pattern of immediately reducible equations would be different. The mathematical operation could still be ordinary addition. But the computational presentation would change which equations the checker knows automatically. This is one reason the exact definition of a function matters in dependent type theory, even when its mathematical meaning seems settled.

An important caveat: different libraries and implementations of addition make different choices, and proof assistants may implement special reductions. The example is about the explicitly stated recursion equations, not a claim that every system reduces arithmetic in precisely the same way.

## Equality as a proposition to be proved

When computation is not enough, we can state an equality as a proposition. Given two terms a and b of the same type, the identity proposition says that a equals b. In the familiar intensional formulation, its basic constructor says every term equals itself. The constructor is reflexivity.

That sounds too weak. How could a single constructor prove symmetry, transitivity, or substitution? The answer is the associated elimination principle. To establish a property of an arbitrary equality proof, it suffices to establish the property in the reflexive case, subject to the precise motive of the elimination rule. Once we know how the property behaves when both endpoints coincide, the equality eliminator transports that result along a proof that the endpoints are equal.

For symmetry, imagine we are given evidence that a equals b and want evidence that b equals a. By eliminating the equality proof, we reduce the argument to the case where b is a and the evidence is reflexivity. Then reflexivity proves the reversed equality. For transitivity, given a equals b and b equals c, we can eliminate one equality and reduce to the case where two endpoints coincide; the other equality finishes the job. These are not arbitrary extra axioms. They are derivable from the identity eliminator and the reflexivity constructor.

The identity proposition is therefore not merely a Boolean comparison that returns true or false. It is a type of evidence connecting terms. A proof of an equality can be passed to a function that needs to replace one term by another. This becomes essential when the *type* of a result depends on the term being replaced.

## Why reflexivity can prove a calculation

Suppose we ask a Lean-style checker to prove that applying the lambda expression which adds one to its argument, to three, equals four. We can try reflexivity. The two written sides are different. But the application reduces, arithmetic on concrete natural numbers reduces, and both sides arrive at the same canonical value. Reflexivity supplies a proof after conversion has done the computation.

There is a danger in describing this as though reflexivity were a magical theorem prover. It is not. If we ask whether two functions are equal merely because they give the same outputs for every input, conversion may not settle that claim. We generally need a theorem about equality of functions, often called function extensionality. Likewise, commutativity of addition is not made definitionally true just by our confidence in arithmetic. Reordering symbolic arguments typically requires a theorem.

The difference is not about which equation is more profound. It is about which equations are part of computation and which are mathematical statements. A proof assistant may automate a mathematical statement until the tactic script is one word long. The proof is still a theorem, and the automation must produce an acceptable derivation or depend on explicitly declared assumptions.

## The boundary with dependent types

Consider a family of types called Vector of A and n, representing sequences of elements of A whose length is n. A vector of length three and a vector of length one plus two are accepted as the same type whenever those length expressions are definitionally convertible. But suppose the lengths are described by variables m plus n and n plus m. We know from arithmetic that these are equal. The checker cannot in general reduce one symbolic expression to the other. It needs the theorem that addition is commutative.

Even after we prove the theorem, a value of type Vector of A and m plus n is not simply a value of type Vector of A and n plus m by silent conversion. We use the equality proof to move that value between the two indexed types. The mathematical contents of the vector do not change. What changes is its type-level description, and the change is licensed by evidence.

This motivates the word *transport*. A family of types gives a type at each index. A proof connecting two indices tells us how to transfer a value from the family at one index to the family at the other. When the equality is reflexive, transport computes to the identity operation. In other cases, the transported value may remain syntactically wrapped in an equality elimination, even though mathematics says its underlying data has not changed.

There is another distinction hiding nearby. Equality of propositions, logical equivalence of propositions, and equality of functions are not all the same claim. From evidence that P if and only if Q, we have methods in both directions between proofs. It takes an additional principle, proposition extensionality, to conclude that P and Q themselves are equal as propositions in Lean. From evidence that two functions agree pointwise, it takes function extensionality to obtain equality of the functions. Neither transformation should be mistaken for a basic arithmetic reduction rule.

## Why this matters for proof design

A theorem that is definitionally true can be pleasantly inexpensive to use. A theorem requiring an explicit equality can be used many times, but its use needs rewriting or transport. If we change a recursive definition, we may change the set of equations that reduce automatically, even if all the old theorems remain logically valid. Large formal developments therefore care about representation decisions that would seem irrelevant in a paper proof.

On the other hand, making everything reduce automatically would be a disastrous design goal. Imagine allowing the type checker to use any theorem in the library to decide whether two arbitrary expressions are equal. Every type-checking step could become an unrestricted proof search problem. By distinguishing conversion from theorem application, the foundational kernel stays much more tractable and its judgments remain understandable.

The distinction also gives us a useful diagnostic when a proof assistant resists an apparently obvious step. Ask: am I expecting computation, or asking for a mathematical identity? If it is computation, a definition may need unfolding or an argument may be stuck on a variable. If it is an identity, I need to name, derive, or rewrite with the theorem. If the type itself changes with the value, I may need transport rather than ordinary replacement of a phrase.

A final nuance concerns identity proofs themselves. Not every dependent type theory makes every two proofs of the same identity interchangeable. In homotopy type theory, identity can have richer structure. Lean's treatment of propositions, including proof irrelevance, supports different behavior from a general universe of higher identity types. It is important not to universalize a rule of one foundation to every foundation that uses dependent types.

We began with three plus four and seven. They are equal because calculation takes us to the same result. We moved to zero plus an unknown n and used induction because a chosen recursive definition did not compute enough. We then constructed equality as evidence and saw why dependent types need to carry that evidence across changes of index. Computation tells the checker which expressions coincide by its own rules. Propositional equality tells it which expressions have been proved to coincide. Keeping both notions is not a nuisance: it is what lets mathematics and reliable type checking coexist.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Two different judgments

- Typing: \(\Gamma\vdash t:A\).
- Judgmental conversion: \(\Gamma\vdash A\equiv B\). The conversion rule permits \(\Gamma\vdash t:B\) when \(\Gamma\vdash t:A\) and \(A\equiv B\).
- Propositional equality: a *term* \(p:(a=b)\), itself subject to type checking.

For a chosen second-argument recursion:
\[
 m+0\equiv m,\qquad m+S(n)\equiv S(m+n).
\]
The theorem \(\forall n,\ 0+n=n\) follows by induction; it is not one of those two computation equations.

### Identity elimination

In schematic dependent type theory:
\[
 \operatorname{refl}_a:a=_A a,\quad
 J:\bigl(\prod_{x:A} C(x,x,\operatorname{refl}_x)\bigr)
 \to\prod_{x,y:A}\prod_{p:x=y} C(x,y,p).
\]
The equation \(J(c,x,x,\operatorname{refl}_x)\equiv c(x)\) expresses the eliminator's reflexivity computation. Precise arguments and universe levels depend on the presentation. A Lean-specific interface is `Eq.rec`.

Illustrative Lean:

```lean
example : (fun x : Nat => x + 1) 3 = 4 := by rfl

example {α : Type} {a b : α} (p : a = b) : b = a := by
  cases p
  rfl

example {α : Type} (f : α → Nat) {a b : α} (p : a = b) :
    f a = f b := congrArg f p
```

### Exercises with answers

1. **Computation or theorem?** In a calculus where addition recurses on the second argument, classify \(m+0=m\) and \(0+n=n\) when \(n\) is a variable. **Answer:** the former is a computation equation; the latter is obtained by induction.
2. **Function equality.** If \(f(x)=g(x)\) for every \(x\), why might `rfl` fail on \(f=g\)? **Answer:** pointwise equality is a theorem hypothesis, not necessarily definitional conversion; function extensionality bridges the claims.
3. **Indices.** Why is a proof of \(m+n=n+m\) relevant for reinterpreting a vector indexed by \(m+n\)? **Answer:** it justifies transporting the vector through the indexed family.
4. **Converse.** Does \(a=b\) imply \(a\equiv b\)? **Answer:** no; propositional equality can hold without definitional conversion.

### References

- *Theorem Proving in Lean 4*, “Quantifiers and Equality,” “Inductive Types,” and “Dependent Type Theory.”
- Per Martin-Löf, *Intuitionistic Type Theory* (1984), equality and elimination rules.
- *Homotopy Type Theory: Univalent Foundations of Mathematics* (2013), Chapter 2, for an alternative treatment of identity types.
