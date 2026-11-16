# 012000 — Induction: Why Proving One Step Can Prove Infinitely Many

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Natural numbers, algebra, implications. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Induction: Why Proving One Step Can Prove Infinitely Many

How could we prove one statement about every natural number without checking infinitely many numbers one by one? Mathematical induction provides an answer when the statements have a structure that passes from one integer to the next. It is not a prediction that a pattern will continue because we saw it continue many times. It is a proof that the mechanism forcing the next case works for every case.

The principle has two parts. First establish a base case. Then prove that whenever the claim holds at a generic natural number n, it also holds at the next number. The base case starts the chain, and the general step ensures it never stops. Together they establish the claim for all natural numbers in the chosen range.

## A sum formula from the ground up

Consider the sum of the first n positive integers. We claim it equals n times n plus one, divided by two. For n equals one, the sum is one, and the formula also gives one. This is the base case. Now assume, for some arbitrary positive integer n, that the formula is correct. This is the induction hypothesis. The sum through n plus one is the old sum plus n plus one. Replace the old sum using the hypothesis. Factor the resulting expression: it becomes n plus one times n plus two, divided by two. That is exactly the formula with n replaced by n plus one.

The algebra completes the step. The induction principle completes the universal conclusion. It is worth distinguishing them. A correct calculation of the step does not help without a valid starting case. A correct starting case does not help unless the step handles an arbitrary n rather than just the first few values.

## Why the induction hypothesis is allowed

At first, induction sounds suspicious: how can we assume what we are trying to prove? We do not assume the theorem for all numbers. We prove a conditional statement: if it holds at an arbitrary n, then it holds at n plus one. That conditional can be valid even before we know whether the antecedent holds at any particular n. Once the base case is established, repeated application of the conditional covers each natural number.

A useful analogy is a staircase. You prove you can stand on the first step. You prove that from any occupied step you can move to the next. It follows that you can reach any step, provided the steps are the natural-number sequence and there are no missing links. The analogy is intuitive, but the mathematical principle is the well-ordering structure of the natural numbers.

## Induction can prove divisibility

Prove that seven divides eight to the n minus one for every nonnegative integer n. At n equals zero, eight to the zero minus one is zero, divisible by seven. Assume eight to the n minus one equals seven times some integer k. Then eight to the n plus one minus one equals eight times eight to the n minus one plus seven. Substitute the hypothesis and obtain seven times eight k plus one. Therefore the next value is divisible by seven. The witness for divisibility is eight k plus one.

This proof illustrates an important technique: rewrite the n plus one expression in terms of the n expression. A successful induction step almost always relies on finding that connection. If the new expression looks unrelated, try factoring, splitting the final summand, or using a recursive description.

## Invariants in algorithms

Induction also explains loop invariants. A loop invariant is a property true before the first iteration and preserved by every iteration. If the program terminates, the invariant is true when it stops. But an invariant alone does not prove termination, and it may not establish the desired output without a final argument connecting the stopping condition to the result.

For example, a running-sum algorithm maintains the claim that its accumulator equals the sum of entries already processed. At initialization no entries have been processed, and the accumulator is zero. Processing one more entry adds its value to both the intended sum and the accumulator, preserving equality. At termination all entries have been processed, so the invariant identifies the accumulator with the total sum.

## Indexing discipline

If a theorem starts at n equals zero, check zero. If it starts at one, check one. If a step needs n minus one or division by n, confirm that the values under discussion permit those operations. One can accidentally prove a statement only for n at least two while claiming it for all natural numbers.

The value of induction extends far beyond numerical formulas. It underlies recursive data structures, combinatorial arguments, finite graphs, formal verification, and constructive proofs. To use it well, identify the statement that needs to be preserved and make the move from one stage to the next explicit. The point is a justified infinite conclusion from a finite pattern of reasoning, not a pattern of successful numerical trials.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Sum and divisibility inductions

For \(n\geq1\), let \(P(n):\sum_{k=1}^n k=n(n+1)/2\). Base \(n=1\) holds; the step is
\[
\sum_{k=1}^{n+1}k=\frac{n(n+1)}2+(n+1)
=\frac{(n+1)(n+2)}2.
\]
For \(n\geq0\), \(7\mid(8^n-1)\). With \(8^n-1=7k\),
\[
8^{n+1}-1=8(8^n-1)+7=7(8k+1).
\]

### Exercises with answers

1. Show \(1+3+\cdots+(2n-1)=n^2\) for positive \(n\). **Answer:** add \(2n+1\) to \(n^2\) and obtain \((n+1)^2\).
2. Why does the step \(P(n)\Rightarrow P(n+1)\) alone not prove all \(P(n)\)? **Answer:** no base case has been established.
3. Give the invariant of an array-summing loop. **Answer:** after processing the first \(k\) entries, the accumulator is their sum.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Mathematical induction](https://en.wikipedia.org/wiki/Mathematical_induction).
