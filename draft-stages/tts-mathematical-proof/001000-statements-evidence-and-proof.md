# 001000 — What Counts as a Mathematical Proof?

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Everyday arithmetic; no prior proof training. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# What Counts as a Mathematical Proof?

A mathematical argument is not just a persuasive story. It is an account of why a conclusion must follow from assumptions that have been stated. The word 'must' matters. Suppose someone claims that the sum of two odd numbers is always even. Checking three plus five, seven plus nine, and a hundred other examples makes the claim plausible. But the claim covers infinitely many pairs of odd integers. A proof must explain why a counterexample is impossible, not merely why we have failed to encounter one.

The argument can begin with an arbitrary odd integer. By definition it is twice an integer plus one. Take another odd integer and write it the same way. Adding their expressions gives twice the sum of those two integers plus two, which is twice an integer. So the result is even. The important step was not the arithmetic alone. It was replacing a particular example by an arbitrary pair, while keeping the information that makes them odd. That is how a finite argument can establish an infinite collection of claims.

## Statements and the world they describe

A mathematical statement is a sentence that can be evaluated as true or false once its meaning and the objects under discussion are fixed. 'Seven is prime' is a statement. 'A triangle has three sides' is a statement once triangle has been defined. 'The number is prime' may not yet be a statement, because we have not said which number. Instead, it may be a property of a variable, something that becomes a statement after we supply a number or quantify over it.

Definitions give the words in a statement precise meanings. A theorem says that one statement follows from declared assumptions. An example illustrates a definition or a theorem. A counterexample defeats a claim that asserted more than is actually true. A conjecture is an unproved claim, no matter how compelling the evidence. These roles are different, and confusing them makes mathematical writing hard to evaluate.

Consider the assertion that every even number greater than two is the sum of two primes. It has been checked for immense ranges of integers, but an enormous finite computation cannot by itself settle the entire infinite assertion. Conversely, a single even number for which no such prime decomposition exists would refute it. The logical asymmetry between supporting examples and a disproof by counterexample is one of the first things a proof writer learns to notice.

## Assumptions are part of the theorem

A claim can change truth value when the domain changes. 'Every nonzero number has a multiplicative inverse' is true for nonzero real numbers, but false for nonzero integers if the inverse is also required to be an integer. The phrase 'number' has hidden a crucial choice. 'A function with derivative zero everywhere is constant' is true on an interval, but if its domain consists of two separated intervals, it can take different constants on each. An assumption about connectedness, not merely differentiability, was doing work.

A complete proof therefore has a beginning and an end. At the beginning, it declares the objects and hypotheses. In the middle, each inference uses a definition, an earlier result, an allowed algebraic operation, or a justified construction. At the end, the requested conclusion has been reached. That skeleton does not require stiff writing. It requires the reader to be able to locate the reason for every important step.

For our odd-number example, the key question is not whether we used advanced mathematics. We used almost none. The questions are whether every odd integer has the required representation, whether the symbols denote integers, and whether the final expression meets the definition of evenness. If so, the argument is sound regardless of how short it is.

## Looking for the weak joint

Here is a tempting but invalid argument. We want to prove that multiplying two positive real numbers gives a positive number. Someone writes: let the numbers be a and b. Their product is positive, as required. The conclusion has merely been restated. A valid argument must use a known property of the ordered real numbers, such as the axiom that the product of positive elements is positive, or derive it from a set of more basic order rules.

Another common failure is to prove only a special case. If we want all triangles, drawing an equilateral triangle does not give a general proof. That drawing might help discover a relationship, but the proof must either apply to arbitrary triangles or explain why every triangle reduces to the chosen case.

When you read a theorem, ask three questions. What would count as one admissible input? What are we promised about it? What must we establish about every such input? When you write a proof, start by answering those questions. The rest of the course develops methods for moving from one side of that contract to the other. The reward is not formality for its own sake. It is the freedom to rely on a result because its limitations and reasons are visible.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Formal proof patterns

The claim that sums of odd integers are even has the quantified form
\[
\forall a,b\in\mathbb Z\;[(\exists r\in\mathbb Z\;a=2r+1)\land(\exists s\in\mathbb Z\;b=2s+1)\Rightarrow(\exists t\in\mathbb Z\;a+b=2t)].
\]
Choose the witnesses promised by the antecedent and let \(t=r+s+1\):
\[
a+b=(2r+1)+(2s+1)=2(r+s+1).
\]
Checking examples illustrates but cannot justify the universal quantifier. The Goldbach conjecture is mentioned only as an example of the distinction between a conjecture and a theorem; no claim of its resolution is intended.

### Exercises with answers

1. State the domain required for 'every nonzero number has a multiplicative inverse.' **Answer:** it is true in a field such as \(\mathbb R\) with the inverse in that field, but false over \(\mathbb Z\), where \(2\) has no integer inverse.
2. Prove that the difference of two odd integers is even. **Answer:** \((2r+1)-(2s+1)=2(r-s)\).
3. What is the logical role of \(n=2\) in the claim 'every prime is odd'? **Answer:** a counterexample; it satisfies the hypothesis 'prime' but violates the conclusion 'odd'.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Mathematical proof](https://en.wikipedia.org/wiki/Mathematical_proof).
