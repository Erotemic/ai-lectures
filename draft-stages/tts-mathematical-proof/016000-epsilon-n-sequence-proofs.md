# 016000 — Epsilon Proofs for Sequences: Making Eventually Precise

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Real numbers, inequalities, quantifiers. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Epsilon Proofs for Sequences: Making Eventually Precise

A sequence converges to a real number L when its terms eventually remain as close to L as we demand. The word 'eventually' is not a vague promise. It has a precise meaning: for every positive tolerance epsilon, there is an integer N such that every index n at least N has the term within epsilon of L. The threshold N may depend on epsilon. Once N is chosen, however, it must work for all later terms, not just one convenient term.

We will use the sequence one over n, for positive integers n. Its terms approach zero. To prove this, begin with an arbitrary positive epsilon. Choose a positive integer N larger than one divided by epsilon. Such an integer exists by the Archimedean property of the real numbers. For every n at least N, one over n is no greater than one over N, which is strictly less than epsilon. Since the absolute distance from one over n to zero is one over n, the convergence condition holds.

## Follow the quantifiers in order

The proof is a small game. Someone asks for accuracy epsilon. We respond with N. Then they may choose any n beyond that threshold. We must show the inequality for that n. If we instead checked only n equals N, the argument could fail for an oscillating sequence that later wanders away. If we chose one N without looking at epsilon, we might accidentally be demanding eventual exact equality with L.

Sometimes the threshold appears as a formula. For a sequence of the form three over n, choosing N larger than three divided by epsilon works. For one over n squared, any N larger than one over the square root of epsilon works. Exact ceiling details are not the point; the proof must establish an integer threshold that exists and makes every later term satisfy the requested bound.

## Sums of convergent sequences

Suppose a sequence a n converges to A and a sequence b n converges to B. To prove their sum converges to A plus B, take a desired tolerance epsilon. Convergence of a gives a threshold after which its error is less than epsilon over two. Convergence of b gives another threshold for the same half-error. Choose N to be the larger of the two thresholds. For every n at least N, both estimates hold. The triangle inequality bounds the error of the sum by the sum of the errors, which is less than epsilon.

The trick of splitting an error budget is a reusable proof method. We allocate room for two independent sources of error, choose one stage where both bounds apply, and combine them with a triangle inequality. In analysis this pattern recurs in continuity of compositions, approximation by dense subsets, and estimates for differential equations.

## Uniqueness of the limit

Could one sequence converge to two different real limits L and M? Suppose it did. If the limits were distinct, their distance d would be positive. Choose epsilon smaller than half of d, say one third of d. Eventually the sequence would be within epsilon of L and, after another threshold, within epsilon of M. Beyond the larger threshold, the triangle inequality would force the distance from L to M to be less than two epsilon, smaller than d. Contradiction. Therefore the limits coincide.

Notice how the proof uses both limits at a common late index. Two different thresholds need not be equal; taking their maximum is enough. This tiny step often separates a valid epsilon proof from a merely suggestive one.

## A sequence that does not converge

Let a n equal one when n is even and minus one when n is odd. Suppose it converged to L. Every sufficiently late even term would force L to be near one, while every sufficiently late odd term would force L to be near minus one. Choosing an error tolerance less than one makes those requirements incompatible. Alternatively, extract the even subsequence, which is constantly one, and the odd subsequence, constantly minus one. Any subsequence of a convergent sequence must converge to the same limit. The two different subsequence limits refute convergence.

This is an example of proving a negative statement about a quantified definition. To disprove convergence to a proposed L, we find one tolerance for which no matter how late a threshold is chosen, a later term lies too far away. To disprove convergence to any L, we need an argument valid for every possible candidate L; the two-subsequence method supplies one clean way.

The language of epsilon and N initially feels more complicated than saying 'the terms get close.' But it lets us combine limits, prove uniqueness, and identify exactly how approximations depend on requested accuracy. These are the tools on which rigorous calculus is built.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Sequence limit definition and error budgets

\[
a_n\longrightarrow L\iff
\forall\varepsilon>0\,\exists N\,\forall n\geq N:\ |a_n-L|<\varepsilon.
\]
For \(a_n=1/n\), let \(N>1/\varepsilon\). Then \(n\ge N\Rightarrow 1/n\le1/N<\varepsilon\).

If \(a_n\to A\) and \(b_n\to B\), given \(\varepsilon>0\) select \(N_a,N_b\) for errors below \(\varepsilon/2\). For \(n\ge\max(N_a,N_b)\),
\[
|(a_n+b_n)-(A+B)|\le|a_n-A|+|b_n-B|<\varepsilon.
\]
To prove uniqueness, take distinct limits \(A,B\), let \(d=|A-B|>0\), and use \(\varepsilon=d/3\) for both. Eventually \(d\le|A-a_n|+|a_n-B|<2d/3\), a contradiction.

### Exercises with answers

1. Show \(5/n\to0\). **Answer:** take \(N>5/\varepsilon\).
2. Prove \((-1)^n\) does not converge. **Answer:** even and odd subsequences have limits \(1\) and \(-1\), respectively.
3. Why choose \(\max(N_a,N_b)\)? **Answer:** it ensures both error estimates hold at the same index.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [OpenStax, Calculus Volume 1, Rice University](https://openstax.org/books/calculus-volume-1/pages/preface).
- [Wikipedia: Limit of a sequence](https://en.wikipedia.org/wiki/Limit_of_a_sequence).
