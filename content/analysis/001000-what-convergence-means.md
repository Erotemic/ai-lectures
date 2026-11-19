# 001000 — What Does It Mean for a Sequence to Converge?

**Track:** Analysis from First Principles. **Background:** elementary algebra, inequalities, and fractions. **Theme:** translating an infinite process into a precise, testable mathematical promise.

<!-- BEGIN SPOKEN LECTURE -->

# What Does It Mean for a Sequence to Converge?

Imagine a measuring instrument that becomes more accurate each time you use it. Its first report is two. Its second is one and a half. Its third is one and a third. Its fourth is one and a quarter. The readings continue in the same pattern: one plus one divided by the measurement number.

Every reading is larger than one. None equals one. Yet we want to say that the readings approach one. What could that claim mean if there is no final measurement, and if the instrument never actually reports the value one?

It cannot mean that we have inspected all the readings. There are infinitely many. It cannot mean that the difference eventually becomes exactly zero, because it does not. And it cannot merely mean that the readings appear close on a graph: how close is close enough? Analysis begins by turning that last question around. Instead of deciding in advance what counts as close, we let a skeptic demand any positive tolerance whatsoever. We then have to show that the sequence eventually stays within that tolerance.

## From a pattern to a promise

A sequence is a numbered list of mathematical objects. For now the objects are real numbers. We write the first number, the second number, and so on, but the important object is the rule assigning a number to each positive integer. There is no requirement that consecutive entries differ by the same amount, or that entries move in only one direction.

Our instrument produces the sequence whose number at stage n is one plus one divided by n. The first stage is two, the tenth is one point one, and the thousandth is one point zero zero one. To ask whether these values converge to one, we look at their distance from one. That distance is exactly one divided by n.

Suppose someone allows an error of one hundredth. We can guarantee the error is smaller after stage one hundred. Suppose the allowed error is one millionth. We can guarantee it after stage one million. The choice of stage depends on the requested accuracy, but the procedure works for every positive tolerance.

That is the meaning of convergence. A sequence converges to a number L if, for every positive tolerance epsilon, we can find a stage N such that every term from stage N onward is less than epsilon away from L.

Listen carefully to the order. First the skeptic chooses the accuracy. Only then are we allowed to choose how far into the sequence to go. Once we have chosen that stage, the guarantee applies to every later term, not just to one term that happens to be close.

For our example, if the tolerance is epsilon, choose any integer N larger than one divided by epsilon. For every n at least N, the error one divided by n is strictly smaller than epsilon. We have proved the infinite claim with a finite calculation. We did not inspect infinitely many terms; we found a rule that handles them all at once.

## Why the quantifiers matter

It helps to imagine the definition as a game with two players. One player selects a narrow band around the proposed limit. The other selects a stage after which every term must remain inside the band. The second player wins only if this can be done for every possible positive band width.

A sequence can enter that band once and leave it again. That does not meet the definition. A sequence can enter the band a million times and still leave it infinitely often. That does not meet the definition either. It must eventually stay.

Consider a sequence that alternates between positive one and negative one. At every even stage it is positive one; at every odd stage it is negative one. Its values never settle. Is there perhaps some clever proposed limit halfway between them, such as zero?

No. Suppose a limit L existed. Far enough along, both a positive-one term and a negative-one term would have to lie within, say, one quarter of L. But two numbers that are each less than one quarter away from L must be less than one half apart from each other. Positive one and negative one are two units apart. That is impossible. The alternating sequence does not converge to any real number.

Now change the rule slightly. Keep the alternating signs, but divide the number at stage n by n. The values are negative one, positive one half, negative one third, positive one quarter, and so forth. They keep crossing zero forever. Nonetheless they converge to zero. Their distance from zero is simply one divided by n, so the very same tolerance argument applies.

A convergent sequence need not move steadily in one direction; it may oscillate indefinitely. But whatever motion remains must eventually be confined to an arbitrarily small neighborhood of its limit.

## A limit is not an approximation

Sometimes a sequence reaches its limit and remains there. A constant sequence equal to seven converges to seven. But reaching the limit is not required. Our original sequence never equals one, yet converges to it.

Nor does a finite list of early errors decide the matter. Suppose the first thousand terms are wildly erratic, and after that the number at stage n is one divided by n. The entire sequence still converges to zero. Choose the starting stage large enough to be past those first thousand exceptions as well as past the requested accuracy threshold. Convergence is a property of the tail of an infinite sequence.

We can also see why there cannot be two different limits. Assume the same sequence converges both to L and to M, with L different from M. The distance between these candidates is some positive number. Demand that all sufficiently late terms lie within one third of that distance from L, and also within one third of it from M. A late term would then provide a path from L to M shorter than two thirds of their actual separation, contradicting the triangle inequality. A convergent sequence has exactly one limit.

This is not a technicality. Without uniqueness, calling a sequence an approximation to a mathematical quantity would be ambiguous. The definition guarantees that if an approximation works, it identifies one destination.

## Proofs that give usable bounds

Take another sequence: n divided by n plus one. The numerator and denominator both grow without bound. That observation alone does not prove anything about their ratio. Instead, rewrite the fraction as one minus one divided by n plus one. Its distance from one is one divided by n plus one, which becomes smaller than any requested positive tolerance.

This proof does more than say the answer is one. It lets us choose the stage needed for a desired absolute error. For an error smaller than one ten-thousandth, taking n at least ten thousand is sufficient. The limit statement contains a practical error certificate.

A similar estimate works for a sequence whose terms are trapped between two easier sequences. Suppose a middle term is always between negative one divided by n and positive one divided by n. Both boundaries approach zero. The trapped term must also approach zero, because its distance from zero never exceeds one divided by n. This is the squeeze principle.

It can be powerful even when the middle sequence behaves unpredictably. We might not know its sign or exact value at any given stage. A bound on its size is enough. For instance, suppose someone selects, at every stage, any real number between negative one divided by n and positive one divided by n, possibly making the choice adversarially. Every sequence produced in this way converges to zero.

Here is another rule that follows from the definition. A convergent real sequence is bounded: all of its terms fit within some fixed finite interval. To see why, choose tolerance one. Beyond a certain stage, all terms lie within one unit of their limit. The earlier terms are only finitely many numbers, so we can choose a larger interval that contains those as well. This does not prove every bounded sequence converges. The sequence alternating between positive and negative one is bounded and divergent.

## When small changes are misleading

An instrument may appear to settle because successive readings become almost identical. Is that enough to guarantee convergence? Not always.

Consider the partial sums of the harmonic series. The first term is one. The second adds one half. The third adds one third. Each new stage adds the reciprocal of its stage number. The change between two consecutive partial sums approaches zero.

Yet the partial sums keep increasing without any finite upper bound. Group the additions into blocks. The terms from one third through one fourth add to at least one half. The terms from one fifth through one eighth also add to at least one half. The terms from one ninth through one sixteenth add to at least one half. Every new block doubles the number of terms but contributes at least another half. No fixed ceiling can contain all the partial sums.

So getting closer from one step to the next does not imply getting closer to a fixed destination. A sequence can drift forever in smaller and smaller increments. The convergence definition controls the position of every sufficiently late term relative to one fixed limit, not merely the most recent step.

One can refine the idea of internal consistency by asking whether all sufficiently late terms are close to one another, not just consecutive terms. That leads to Cauchy sequences and to the question of whether the chosen number system contains their destinations. The distinction between consecutive differences and all late pairs is important: the harmonic partial sums fail the latter test despite passing the former.

## What counts as divergence

We use the word divergent whenever a sequence has no finite real limit, but divergence can take very different forms. The alternating ones never settle because they oscillate at a fixed scale. The harmonic partial sums never settle because they keep growing. The sequence n squared also grows without bound. In the last case we can say it tends to positive infinity, meaning that for every positive height there is a stage after which every term exceeds that height.

That statement is meaningful, but infinity is not a real number serving as the ordinary limit. Keeping the distinction clear prevents errors when applying rules about finite limits.

The definition of convergence therefore gives us a way to classify infinite behavior with precision. It separates genuine stabilization from visual resemblance, occasional accuracy from permanent accuracy, and internal small steps from approach to an actual destination.

We began with readings that never equal one. The point was not to wait for the final reading. There is none. The point was to prove that no matter what positive error someone asks us to beat, we can identify a stage after which every reading succeeds. That is what it means for a sequence to converge.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let a sequence be a function \(a:\mathbb N_{\ge1}\to\mathbb R\). The statement \(a_n\to L\in\mathbb R\) means

\[
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\ge N:\quad |a_n-L|<\varepsilon.
\]

1. **Explicit witness:** \(a_n=1+1/n\). For arbitrary \(\varepsilon>0\), choose \(N>1/\varepsilon\). Then \(|a_n-1|=1/n\le1/N<\varepsilon\) for all \(n\ge N\).
2. **Oscillation that persists:** \(a_n=(-1)^n\). If \(a_n\to L\), all sufficiently large even and odd terms lie within \(\varepsilon=1/4\) of \(L\). The triangle inequality would imply \(2<1/2\), impossible.
3. **Oscillation that decays:** \(a_n=(-1)^n/n\to0\) because \(|a_n|=1/n\to0\).
4. **Uniqueness:** If \(a_n\to L\) and \(a_n\to M\), with \(L\ne M\), set \(\varepsilon=|L-M|/3\). For large \(n\), \(|L-M|\le|L-a_n|+|a_n-M|<2|L-M|/3\), contradiction.
5. **Squeeze:** If eventually \(b_n\le a_n\le c_n\) with \(b_n\to L\), \(c_n\to L\), then \(a_n\to L\).
6. **Boundedness:** Convergence implies eventual inclusion in \((L-1,L+1)\), and a finite prefix is bounded.
7. **Consecutive differences are insufficient:** \(H_n=\sum_{k=1}^n1/k\) satisfies \(H_{n+1}-H_n=1/(n+1)\to0\), but \(H_{2^m}\ge1+m/2\to\infty\), by grouping \(2^{j-1}+1\) through \(2^j\) for \(j=1,\ldots,m\).
8. **Infinite divergence:** \(a_n\to+\infty\) means \(\forall M>0\ \exists N\ \forall n\ge N:\ a_n>M\), not convergence to a finite real number.

### Exercises and guided answers

1. **Find a witness:** Show \(\frac{3n+2}{n+1}\to3\). **Answer:** The error is \(|(3n+2)/(n+1)-3|=1/(n+1)\). Any \(N>1/\varepsilon\) suffices.
2. **Change a prefix:** Does replacing the first million terms of \(1/n\) affect its limit? **Answer:** No; choose a starting stage beyond the changed prefix and beyond the tolerance requirement.
3. **Prove nonconvergence:** Does \(a_n=0\) for odd \(n\) and \(a_n=2\) for even \(n\) converge? **Answer:** No. Its two constant subsequences would force incompatible limits.
4. **Check a tempting converse:** Is every bounded sequence convergent? **Answer:** No: \((-1)^n\) is bounded but divergent.
5. **Separate two tests:** Why does \(H_{n+1}-H_n\to0\) not contradict divergence of \(H_n\)? **Answer:** The convergence definition concerns distance from a fixed \(L\) for every sufficiently late term; step sizes alone do not control accumulated drift.

### References

- OpenStax, *Calculus Volume 2*, section 5.1, “Sequences”: https://openstax.org/books/calculus-volume-2/pages/5-1-sequences
- Stephen Abbott, *Understanding Analysis*, 2nd ed., chapters on sequences and limits.
- Terence Tao, *Analysis I*, chapters on limits of sequences.
- [MIT OpenCourseWare, 18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/pages/lecture-notes/) — MIT 18.100B, lectures 4–7: epsilon–N convergence, Cauchy sequences and monotone convergence.
