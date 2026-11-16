# 014000 — Countable and Uncountable: Comparing Infinite Sets

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Functions and injections. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Countable and Uncountable: Comparing Infinite Sets

Two finite sets have the same number of elements when there is a pairing that matches each element of one set with exactly one element of the other, with nothing left over. This idea extends to infinite sets. A bijection—one-to-one and onto—becomes the definition of equal cardinality. It can lead to surprising results, but the surprises become manageable when we prove the pairings carefully.

The natural numbers and the even natural numbers can be paired by sending n to two n. Every natural number has a unique even image, and every even natural number is twice a unique natural number. The even numbers form a proper subset of the natural numbers, yet the two infinite sets have the same cardinality. This would be impossible for finite sets. Infinity changes how containment relates to size.

## Enumerating the integers

The set of all integers is countable: one can list zero, one, minus one, two, minus two, and continue. Every integer appears after finitely many steps, and no integer needs to appear more than once. A countably infinite set is one whose members can be matched bijectively with the natural numbers. Some authors include finite sets under the label countable; whenever the distinction matters, say 'at most countable' or 'countably infinite.'

Fractions require more work. Every positive rational number has some representation as a positive numerator divided by a positive denominator. Arrange the pairs of positive integers in an infinite grid. Traverse the grid along diagonals of fixed numerator plus denominator. This ensures that each pair is eventually visited. Some pairs represent the same rational number, so skip repetitions in reduced form. The resulting list contains every positive rational number. Include zero and negative rationals by interleaving, and the full set of rational numbers is countable.

The argument is about an explicit enumeration, not an unexplained slogan that a grid is 'obviously' countable. The diagonal order is what ensures no pair is permanently postponed.

## Why the real numbers are different

Consider the set of all infinite sequences of zeros and ones. Suppose someone claims to list every such sequence. Read the first entry's first digit, the second entry's second digit, and so on. Construct a new sequence that differs from the first entry in digit one, from the second in digit two, and generally from entry n in digit n. Change zero to one and one to zero at the diagonal position. The new sequence differs from every listed sequence somewhere, so it cannot be in the list. No claimed enumeration is complete.

This is Cantor's diagonal argument. It does not rely on choosing a large number of counterexamples; it builds one counterexample tailored to any proposed infinite list. The universal part is the phrase 'any proposed list.'

To connect this to real numbers without getting tangled in nonunique binary decimal representations, encode each zero-one sequence as a real number whose base-three digits are only zero and two. Distinct such sequences give distinct real numbers in the Cantor set; restricting to those digits prevents the standard ambiguous expansion from equating two different restricted sequences. The set of these reals is therefore uncountable. Since it sits inside the real interval from zero to one, that interval is uncountable too.

## What the diagonal proof does and does not show

A diagonal argument disproves the existence of a complete enumeration. It does not provide a physical procedure that prints every real number, and it does not claim that one could inspect infinitely many rows in finite time. It is a mathematical construction specified for any hypothetical list, with a clear reason that the new object evades each entry.

The distinction between countable and uncountable often appears when interpreting 'almost every,' genericity, and the size of families of functions. The real line contains infinitely more possibilities in cardinality than the natural numbers, but cardinality is not probability or length. The rationals are countable and dense on the real line; between any two distinct reals lies a rational. A dense set need not have large cardinality or positive length.

## Proofs about infinite sets require explicit maps

When you claim two sets have equal cardinality, write down a bijection or combine precise inequalities using a theorem such as Cantor–Bernstein. When you claim a set is countable, exhibit an enumeration or an injection into the natural numbers. When you claim a set is uncountable, explain why no enumeration can work. The subject is often introduced through paradoxes, but its proof obligations are the same as in elementary functions: construct maps, check domains, verify injectivity or surjectivity, and justify every quantifier.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Explicit countability and diagonal arguments

\(\mathbb Z\) is countable by \(0,1,-1,2,-2,\ldots\). The positive rationals are covered by pairs \((p,q)\in\mathbb N_{>0}^2\) ordered by \(p+q\), skipping duplicate fractions.

Given any alleged enumeration \(s_1,s_2,\ldots\) of binary sequences \(s_n\in\{0,1\}^{\mathbb N}\), define
\[
t_n=1-s_n(n).
\]
Then \(t\neq s_n\) for every \(n\), since they differ at position \(n\). Thus binary sequences are uncountable.

To inject binary sequences into \([0,1]\), use
\[
(b_n)_{n\ge1}\mapsto\sum_{n=1}^\infty\frac{2b_n}{3^n}.
\]
This map is injective: at the earliest differing digit \(k\), the difference in that digit's contribution, \(2/3^k\), exceeds the entire maximal tail difference \(\sum_{n>k}2/3^n=1/3^k\).

### Exercises with answers

1. Give a bijection between \(\mathbb N\) and the even nonnegative integers. **Answer:** \(n\mapsto 2n\).
2. Why does the diagonal sequence differ from every listed sequence? **Answer:** it differs from row \(n\) at coordinate \(n\).
3. Does density imply uncountability? **Answer:** no; \(\mathbb Q\) is countable and dense in \(\mathbb R\).

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Cantor%27s diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument).
