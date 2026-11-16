# 004000 — Definitions and If-and-Only-If: Keeping Both Directions

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Implications and quantifiers. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Definitions and If-and-Only-If: Keeping Both Directions

A mathematical definition is a contract for how a word may be used. Suppose we define an integer to be even exactly when it equals twice another integer. This gives us two directions: if an integer is even, there is an integer that doubles to it; and if an integer equals twice an integer, it is even. Both directions are available because 'even' has been defined by an equivalence.

That may sound obvious, but many proofs fail because they use only one part of a definition or silently replace a precise definition by a picture. To prove a number is even, we can exhibit the required integer. To use the assumption that a number is even, we can introduce the integer promised by the definition. Definitions are tools we can unpack in either direction.

## Necessary and sufficient

If P implies Q, then Q is a necessary condition for P: P cannot occur without Q. The same implication says that P is sufficient for Q: P alone guarantees Q. If we assert P if and only if Q, each is necessary and sufficient for the other. These words are easiest to read by converting them back into the implication they describe.

For example, being divisible by four is sufficient for being even, but not necessary. Being even is necessary for divisibility by four, but not sufficient. Six is the concrete counterexample to the reverse direction. One short example is often enough to separate two claims that sound interchangeable in casual speech.

An equivalence proof requires two complete arguments. To show that an integer n is even if and only if n squared is even, first assume n is even. Write n as twice an integer, and its square is divisible by four, hence even. For the reverse direction, assume n squared is even. If n were odd, writing n as twice an integer plus one shows that its square is odd. That contradiction tells us n cannot be odd; since every integer is even or odd, n must be even. The two arguments have distinct work to do.

## Definitions with several clauses

Consider a function being injective. The definition says: for every two inputs x and y in its domain, if the outputs are equal, then the inputs are equal. To prove injectivity, begin with arbitrary x and y, assume equal outputs, and derive equal inputs. To use injectivity in a proof, you may conclude x equals y only after showing that the corresponding outputs match. You cannot conclude that an arbitrary output has an input: that is surjectivity, a separate property.

Now define a relation to be an equivalence relation when it is reflexive, symmetric, and transitive. That is a three-part conjunction. A proof that a relation is an equivalence relation must establish all three properties. Conversely, whenever we know we have an equivalence relation, we can use each property independently. Words such as 'continuous,' 'compact,' 'normal,' and 'measurable' will later hide more elaborate contracts, but the reading method is the same.

## Definitions are not all theorems

Definitions introduce names; theorems establish facts about the objects named. We may define a prime number as an integer greater than one with no positive divisors except one and itself. That does not establish that every integer greater than one is a product of primes. Factorization requires a proof. Likewise, defining a limit does not prove that every sequence has a limit. Existence remains a mathematical question.

Sometimes a single object has several equivalent descriptions. A topology course may prove that a set is closed exactly when its complement is open; depending on the chosen starting axioms, one side may be a definition and the other a theorem. In metric spaces, the sequential criterion for closedness is another equivalent characterization. The fact that mathematicians freely exchange these descriptions is earned by an equivalence proof, not by the similarity of the words.

## How to audit a definition-based argument

When reading a long proof, underline every use of a defined term. Ask whether the writer is using the term to obtain information or trying to prove the term applies. In the first situation, unpack the assumption. In the second, check all the requirements of the definition. Be alert to missing domain restrictions: 'n is prime' means a positive integer greater than one, not a negative integer or a unit. Be alert also to vacuous cases. The statement 'every element of the empty set has a certain property' is true because there is no violating element, but it does not assert that such an element exists.

This habit keeps mathematical explanations honest without making them cumbersome. A definition tells us exactly what has been promised and what must be delivered. Most of the reasoning methods that follow are ways of carrying those promises from hypotheses into conclusions.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Directions of a biconditional

To prove \(P\iff Q\), supply two implications \(P\Rightarrow Q\) and \(Q\Rightarrow P\).

Example for \(n\in\mathbb Z\):
\[
n\equiv0\pmod 2\iff n^2\equiv0\pmod2.
\]
For the forward direction \(n=2k\) gives \(n^2=2(2k^2)\). For the reverse, prove the contrapositive: if \(n=2k+1\), then \(n^2=2(2k^2+2k)+1\), hence it is odd.

### Exercises with answers

1. Is 'multiple of six' necessary or sufficient for 'multiple of three'? **Answer:** sufficient, not necessary.
2. Prove \(n\) divisible by \(10\) iff it is divisible by \(2\) and \(5\). **Answer:** necessity follows from \(10=2\cdot5\). For sufficiency, write \(n=5k\); its evenness forces \(k\) even (since \(5k\) and \(k\) have the same parity), so \(n=10m\).
3. Why does a proof of \(P\Rightarrow Q\) not automatically establish \(P\iff Q\)? **Answer:** the reverse implication remains to be shown.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Mathematics in Lean, Lean community documentation](https://leanprover-community.github.io/mathematics_in_lean/index.html).
- [Wikipedia: Necessity and sufficiency](https://en.wikipedia.org/wiki/Necessity_and_sufficiency).
