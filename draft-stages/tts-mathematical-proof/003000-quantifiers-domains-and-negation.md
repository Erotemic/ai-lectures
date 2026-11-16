# 003000 — For Every and There Exists: Quantifiers and Their Scope

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Basic logical connectives. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# For Every and There Exists: Quantifiers and Their Scope

There are two short phrases that let mathematics make claims about infinitely many objects: 'for every' and 'there exists.' Their order, scope, and domain can change a theorem completely. A listener who understands those three details already understands much of the structure of a formal proof.

Start with the claim that every natural number has a larger natural number. Read it as follows: take any natural number n. There is some natural number m, which may depend on n, such that m is larger. We can prove it by selecting n plus one. Notice that our choice is allowed to change when n changes. A different claim would say that there exists one natural number m which is larger than every natural number n. That claim is false. The two sentences contain the same words and comparisons, but the quantifiers appear in the opposite order.

## Domains control the meaning

The sentence 'for every x, x squared is nonnegative' is true when x ranges over the real numbers. Without a domain it is incomplete, and over complex numbers 'nonnegative' has no usual order meaning. Likewise, 'there exists an x with x squared equal to minus one' is false over the reals and true over the complex numbers. A good proof names its universe before starting its argument.

An unrestricted variable is not an invitation to choose your favorite example. When a theorem begins 'for every integer n,' you introduce an arbitrary integer n and reason in a way that does not depend on a special value. For an existential claim, by contrast, one successful witness is enough. To prove there exists an even prime, choose two and verify both properties. To prove every prime is even, that single example is useless; three refutes the claim.

## Negating a quantified statement

Imagine the assertion, 'every student in a class solved at least one problem.' To show it is false, it is enough to identify one student who solved none. The negation of a universal assertion is an existential counterexample. Similarly, to deny that there exists a student who solved every problem is to say that each student failed at least one problem. This is a universal statement with an existential failure inside it.

In classical logic, the negation of 'for every x, P of x' is equivalent to 'there exists an x for which P fails.' The negation of 'there exists an x with P of x' is equivalent to 'for every x, P fails.' The classical qualification is important in foundational mathematics: intuitionistic and constructive logics distinguish some directions that classical mathematics treats as interchangeable. The everyday proof methods in this course will use classical logic, and later a constructive logic track can explain which witnesses become computational data.

Now combine the patterns. Negate 'for every real x there exists a real y greater than x.' The result is 'there exists a real x such that every real y fails to be greater than x.' This says that the real numbers have a greatest element. That is false, as expected, because adding one always gives a greater number. Negating one quantifier at a time, while flipping its kind, keeps the dependencies straight.

## Moving quantifiers changes the claim

Compare two statements about students and books. First: every student has read some book. Second: there is a book every student has read. In the first, each student may name a different book. In the second, all students share a single book. We must not swap the order just because both sentences contain 'every' and 'some.'

The same issue appears in analysis. A sequence converges to L when, for every positive error tolerance, there exists a sufficiently late index after which all terms lie within that tolerance of L. The index may depend on the tolerance. If we accidentally require one fixed index that works for every positive tolerance, we demand that all sufficiently late terms equal L exactly. That is much stronger than convergence.

Uniform continuity adds another dependency question. The required input tolerance may depend on the desired output error, but must work at every point in the domain. Ordinary pointwise continuity allows the input tolerance also to depend on the chosen base point. This is why quantifier order matters even when the formulas look nearly identical.

## A method for reading dense definitions

When confronted with a quantified claim, translate it into a game. The opponent chooses the objects governed by universal quantifiers. You must provide witnesses for existential quantifiers at the moment they become available. In the convergence definition, the opponent presents an epsilon. You then produce a threshold N. They choose a later index n, and you must verify the required inequality. A proof wins only if its choices work for every legal move.

This game is not a complete theory of logic, but it is an excellent reading discipline. It reveals why some proposed proofs fail: they secretly pick a witness before seeing the universal input on which it needs to depend, or they check just one value rather than all values. Quantifiers are the grammar of mathematical dependence. Learning to hear that grammar makes much of advanced mathematics less mysterious.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Quantified forms

\[
\forall n\in\mathbb N\;\exists m\in\mathbb N\;(m>n)
\qquad\text{versus}\qquad
\exists m\in\mathbb N\;\forall n\in\mathbb N\;(m>n).
\]
The first is proved by \(m=n+1\); the second is false.

Classically:
\[
\neg\forall x\,P(x)\iff\exists x\,\neg P(x),\qquad
\neg\exists x\,P(x)\iff\forall x\,\neg P(x).
\]
A sequence \((a_n)\) converges to \(L\) if
\[
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\geq N:\ |a_n-L|<\varepsilon.
\]
The choice of \(N\) may depend on \(\varepsilon\).

### Exercises with answers

1. Negate \(\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x)\). **Answer:** \(\exists x\in\mathbb R\;\forall y\in\mathbb R\;(y\leq x)\).
2. Why is \(\forall n\,\exists m>n\) true but \(\exists m\,\forall n\,(m>n)\) false on \(\mathbb N\)? **Answer:** \(n+1\) is an allowed dependent witness; there is no fixed maximum natural number.
3. Negate 'some student solved every problem.' **Answer:** every student failed at least one problem.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Wikipedia: Quantifier (logic)](https://en.wikipedia.org/wiki/Quantifier_(logic)).
