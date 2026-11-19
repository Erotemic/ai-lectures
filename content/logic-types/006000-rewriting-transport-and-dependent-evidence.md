# 006000 — Rewriting and Transport: Moving Evidence Across Equality

**Track:** Logic, Type Theory, and Constructive Mathematics. **Background:** dependent families and the difference between judgmental and propositional equality. **Theme:** the substitution principle, dependent transport, congruence, and how algebraic rewriting becomes a proof about families of types.

<!-- BEGIN SPOKEN LECTURE -->

# Rewriting and Transport: Moving Evidence Across Equality

Imagine two researchers agree that a particular natural number has two different descriptions. One calls it n plus m; the other calls it m plus n. They have proved the two expressions are equal. Each researcher owns a collection of objects indexed by their preferred description. One has a vector declared to have n plus m entries. The other needs a vector declared to have m plus n entries. The element sequence can be identical. Yet a dependent type checker sees two types that do not automatically compute to the same expression.

What must be supplied to use the first vector in the second position? Not another copy of the vector and not a promise that arithmetic is trustworthy. We must apply the *equality proof* to the family of types. That operation is called transport. It is the general mathematical mechanism behind rewriting in dependent type theory.

We are going to construct transport from a single equality principle, trace what happens when the transported object carries a proof, and distinguish rewriting an expression from making an unjustified identification of types. We will also confront a practical difficulty: equality proofs can make a formal statement harder to read even when the underlying mathematics is simple. The right response is not to erase the reasoning but to choose useful interfaces.

## A family, not just one type

Start with an ordinary type A and a proposition P about its elements. For each a in A, P of a is a different proposition, or at least potentially a different proposition. To say that a number is positive is not the same statement as saying a different number is positive. Even when two such claims happen to have the same truth value, their statements mention different numbers.

Now suppose we have a proof p that a equals b, and we also have evidence of P of a. The substitution principle allows us to obtain evidence of P of b. If a and b are genuinely the same element, a property of one must be a property of the other. The formal construction records how we passed from one indexed proposition to another.

The same idea extends beyond propositions. Let F assign a *type* F of x to each x in A. If p says a equals b, and v is a value of F of a, transport along p produces a value of F of b. In ordinary mathematical speech we might say simply, 'identify the two indices using p.' In the type theory, that identification is an operation with a type and a computation rule.

When p is reflexivity, transport does nothing. We start with a value of F of a and end with the same value of F of a. That reflexive computation is the basic case. An equality elimination principle extends it from reflexivity to arbitrary proven equalities. Notice the direction: transport along a proof from a to b takes us from F of a to F of b. Reversing the direction requires the symmetric equality.

This is already more general than replacing one visible occurrence of an expression with another in a printed formula. Rewriting may change which type an entire term belongs to. The type checker must maintain that dependency through the whole expression.

## Moving a proof of positivity

Consider a concrete case. We have natural numbers a and b, a proof that a equals b, and a proof that a is positive. We want to prove b is positive. Positivity is a family of propositions indexed by natural numbers. Applying the substitution principle gives us the desired proof immediately.

A direct paper argument says, 'Since a equals b, the property is unchanged.' That sentence is correct, but it conceals the key generality: it works for any predicate on any type because it is an instance of equality elimination. We did not need to know anything special about positivity.

Transport becomes concrete when the objects being rewritten carry type-level structure. Suppose a matrix carries row and column dimensions in its type. A theorem may establish that the number of columns of one matrix equals the number of rows of another. That equality lets us construct a well-typed matrix product. Without it, the multiplication interface should refuse the operation. The role of transport is to turn arithmetic facts about dimensions into compatibility of the types describing the matrices.

In practical systems the dimension equality may be hidden behind a helper lemma, a rewrite tactic, or a cast operation. Hiding an explicit cast can make code more pleasant, but it does not mean the requirement has disappeared. It has been justified, and the machinery is being managed by an abstraction.

## Transport is itself a proof-driven function

Let us reason through transport's definition. We are given a type A, a family F of types indexed by A, two indices a and b, a proof p of a equals b, and a value v in F of a. What should the output be? A value of F of b.

Instead of inventing a case for every possible a, b, and p, we eliminate the proof p. The identity eliminator tells us it is enough to handle the reflexive case. In that case b is a, and the output type F of b is F of a. The input v is already the required output. So the entire definition can be summarized as: when the equality proof is reflexivity, return the original value.

The eliminator guarantees that this recipe is well typed for arbitrary equality evidence. It is important that we prove a *family-dependent* statement: the output type changes with b. Ordinary nondependent pattern matching would not explain the result's type.

Now consider two equalities: p says a equals b, and q says b equals c. We can transport from F of a to F of b and then from F of b to F of c. We can also compose p and q into one equality from a to c and transport once. These two constructions are propositionally equal in the standard identity-type calculus, using equality induction. They need not unfold to identical expressions for symbolic p and q; the equivalence is another theorem whose proof ultimately reduces to reflexivity cases.

Likewise, transport along p and then along the inverse of p returns a result equal to the starting value. You can think of these laws as saying that equality proofs act coherently on type families. The laws are not arbitrary conveniences: they are consequences of the elimination rule.

## The difference between congruence and transport

A closely related operation is congruence. If a equals b and f is a function from A to B, then f of a equals f of b. Congruence moves an *equality* forward through an ordinary function. Transport moves a *value* between types in a family.

Here is the distinction with an example. Suppose length is a function from lists to natural numbers. Given proof that lists xs and ys are equal, congruence yields proof that length of xs equals length of ys. We remain inside the type of natural numbers, producing an equality of their values.

Now suppose we have a vector whose type is indexed by length of xs. To reinterpret it as a vector indexed by length of ys, we use the equality supplied by congruence as the path along which we transport the vector. Congruence first manufactures an equality between indices. Transport then moves a dependent object along that equality. These are different stages and different outputs.

Ordinary algebraic rewriting is often expressed by combining them with substitution. If we know a equals b, we may replace a by b inside a larger expression because that expression is a function of the subexpression being replaced. When the surrounding expression is a proposition, the rewritten result is a proposition. When it is a type, a cast may be necessary. When it is a term, congruence may be what we need. Good tactics automate these distinctions but do not abolish them.

## Rewriting is contextual

Suppose we know x equals y. Can we rewrite every appearance of the printed letter x in a document? Of course not. An x inside a bound variable, an unrelated local declaration, or a quoted string is not necessarily the same mathematical occurrence. Rewriting must respect syntax and scope. In a proof assistant, names are resolved to precise terms in a context. A rewrite works on expressions where the equality actually applies, preserving typing and variable binding.

It also matters what the equality asserts. If we know two real numbers have the same square, we cannot generally replace one by the other: negative three and positive three have equal squares but are not equal. If we know two functions produce the same output on a particular input, we cannot replace one function with the other on every input. An equality at one level is not automatically an equality at another.

A rewrite tactic may fail even when a mathematically valid equivalence is available, because the expression in the goal is presented in a different but propositionally equivalent form. For example, the goal may contain n plus zero while the theorem is written zero plus n, or the terms may differ under normalization or coercions. The correct remedy may be a preliminary rewrite, an explicit instantiation, or a more suitable lemma. Rewriting is a disciplined transformation of a particular formal expression, not free association among familiar identities.

This is particularly visible with dependent pairs. Suppose a value consists of an index n and data of type F of n. If we change n to an equal index m, we also have to move the second component. We cannot just edit the first coordinate and leave the dependent component untouched: its type is tied to the original index. The equality evidence connects the two parts.

## Can two transports be equal without being the same computation?

Consider a symbolic equality p between numbers a and b. Transporting a vector along p is well-typed, but the checker may not reduce it further because p is a variable and the reflexive case is not visible. This is not a defect in the mathematical definition. The computation rule tells us exactly what happens when p is reflexivity; the general case may require a theorem or an abstraction to compare.

Suppose we later prove that two equality paths p and q from a to b are equal as proofs. By congruence, transport along p and transport along q act equally on the same input. In Lean, proof irrelevance for propositions often means equality proofs can be treated as interchangeable at the propositional level. But that is a property of Lean's logical design, not a principle common to all intensional identity type theories. In homotopy type theory, distinct identity paths may carry meaningful structure, and treating them as trivially interchangeable would discard information.

There is a useful engineering lesson here. If we define an API that asks callers to provide an equality proof to move between representations, we should usually supply a small set of coherent helper theorems: transport along reflexivity, transport along composed equalities, and transport through common families. Otherwise every downstream user repeatedly reconstructs the same bookkeeping. The helpers should be proved from foundational rules; they should not be accepted as silent casts based on an unchecked assertion.

## A trustworthy use of simplification

In Lean, a tactic called rewriting uses equality theorems to transform expressions. A simplifier can repeatedly apply rewrite rules and reduction steps, along with logic-specific simplifications. The resulting proof is not merely the unverified text of a transformed goal. In the normal proof path, the tactics construct proof terms that the kernel checks. The transformation can be sophisticated, but the justification must still reduce to accepted inference rules and declared constants.

Not every equality is an appropriate simplification rule. If a simplifier is allowed to use both directions of a symmetric equality, it can loop: replace a with b, then b with a, forever. If it rewrites associativity back and forth, it can produce endless rearrangements. A useful simplifier therefore chooses oriented rules and controls when rewriting takes place. There are mathematical reasons for those engineering choices. Rewriting has to preserve truth, but it also has to make progress toward a manageable normal form.

The main point is deeper than tactics. Once we understand that a proof of equality licenses substitution in any appropriate family, we can separate the mathematical validity of a rewrite from the algorithm that finds a useful rewrite. The theorem tells us *why* the step is allowed. The tactic tells us *when and where* to perform it.

## Returning to the vectors

We started with a vector whose length was n plus m, and a destination that demanded m plus n. Arithmetic provides a proof of the required index equality. Transport supplies a value of the new indexed type. We do not pretend the two symbolic lengths reduce to the same syntactic form, and we do not rebuild the vector by hand. We use exactly the equality that mathematics has earned.

Transport is thus a bridge between ordinary mathematical identities and types that encode invariants. It explains rewriting, substitution of equals, dependent casts, and why indexed programs sometimes need proofs about arithmetic to even be well-typed. The important questions are always the same: what equality do we have, which family depends on it, which direction should we travel, and what computation rule justifies the result? Once those are answered, the proof assistant can do the bookkeeping without doing the mathematics for us.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Transport and substitution

For a family \(F:A\to\mathsf{Type}\):
\[
 \operatorname{transport}_F : (a=_A b)\to F(a)\to F(b),
 \qquad \operatorname{transport}_F(\operatorname{refl}_a,v)\equiv v.
\]
For a predicate \(P:A\to\mathsf{Prop}\), the same operation is substitution:
\[
 p:a=b,\quad h:P(a)\quad\Longrightarrow\quad p_*h:P(b).
\]
For a nondependent function \(f:A\to B\), congruence is
\[
 \operatorname{ap}_f:(a=b)\to(f(a)=f(b)).
\]
Transport functoriality, propositionally:
\[
 \operatorname{transport}_F(q,\operatorname{transport}_F(p,v))
 =\operatorname{transport}_F(p\mathbin{\cdot}q,v).
\]
Both sides reduce to \(v\) in the reflexivity case; equality induction proves the general law. The orientation of \(p\mathbin{\cdot}q\) here is \(a\xrightarrow{p}b\xrightarrow{q}c\).

### Lean illustrations

```lean
example {α : Type} {a b : α} (P : α → Prop)
    (p : a = b) (ha : P a) : P b := by
  exact p ▸ ha

example {α : Type} {a b : α} (f : α → Nat)
    (p : a = b) : f a = f b := by
  exact congrArg f p

-- Schematic family; may be replaced by any indexed datatype.
def move {A : Type} (F : A → Type) {a b : A}
    (p : a = b) (v : F a) : F b := by
  cases p
  exact v
```

### A dependent-pair warning

For \(\Sigma(n:\mathbb N).F(n)\), an equality of indices \(p:n=m\) permits
\[
 (n,v)\quad\longmapsto\quad(m,\operatorname{transport}_F(p,v)),
\]
not merely changing the first component of the pair while leaving the dependent second component untyped.

### Exercises with answers

1. **Direction.** Given \(p:a=b\) and \(v:F(b)\), what equality proves the reverse move? **Answer:** symmetry \(p^{-1}:b=a\), then \(\operatorname{transport}_F(p^{-1},v):F(a)\).
2. **Lengths.** Given \(p:m+n=n+m\) and \(v:\mathrm{Vec}(A,m+n)\), identify the target family. **Answer:** \(F(k)=\mathrm{Vec}(A,k)\).
3. **Composition.** Why is a direct, one-step transport comparable to two successive transports? **Answer:** equality induction reduces both to identity in the reflexive case, giving a propositional coherence theorem.
4. **Not an equality.** Why does \(a^2=b^2\) not justify rewriting \(a\) to \(b\)? **Answer:** the hypothesis states equality of the squares, not of their roots; choose \(a=1,b=-1\).

### References

- *Theorem Proving in Lean 4*, “Quantifiers and Equality” (substitution and rewriting), “Inductive Types” (equality recursor).
- Per Martin-Löf, *Intuitionistic Type Theory* (1984), equality elimination.
- *Homotopy Type Theory: Univalent Foundations of Mathematics*, Chapter 2 (transport, action on paths, higher structure).
