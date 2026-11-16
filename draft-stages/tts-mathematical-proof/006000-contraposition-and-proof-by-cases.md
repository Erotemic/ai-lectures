# 006000 — Contraposition and Cases: Changing the Route, Not the Claim

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Implication and direct proof. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Contraposition and Cases: Changing the Route, Not the Claim

Sometimes the conclusion of a theorem is a negative statement, and approaching it directly is awkward. We can change the route without changing the claim. Contraposition does this for a conditional statement. A second technique, proof by cases, divides the possible inputs into exhaustive alternatives and handles each one. Both methods depend on a precise understanding of which possibilities have been covered.

Take the theorem: if an integer n squared is even, then n is even. A direct approach might begin by trying to extract information about n from the parity of its square. A more convenient approach is to prove the contrapositive: if n is not even, then n squared is not even. Every integer that is not even is odd. Write n as twice k plus one. Expanding the square gives four k squared plus four k plus one, which is twice the integer two k squared plus two k, plus one. Hence n squared is odd. We have proved the contrapositive, so the original conditional follows in classical mathematics.

## Why the direction works

The original implication forbids a case where n squared is even but n is odd. The contrapositive forbids exactly the same case, described from the opposite direction. In elementary classical logic, 'if P then Q' and 'if not Q then not P' have the same truth conditions. This justifies proving one in place of the other. It does not justify proving the converse, 'if Q then P,' or the inverse, 'if not P then not Q.' Their counterexamples may differ.

Contraposition is particularly useful when a conclusion says that an object is injective, nonzero, independent, or impossible. Instead of forcing the desired positive structure, assume its failure and derive the failure of the hypothesis. One should still check that the negation of the conclusion has been written correctly. 'Not all' and 'all not' are different.

## A proof by exhaustive cases

Suppose a whole number n is any integer. We want to show that n times n plus one is even. Every integer is either even or odd. If n is even, then n is twice k, and n times n plus one contains the factor two. If n is odd, n equals twice k plus one, so n plus one equals twice k plus two and is even. In either case one factor in the product is even, so the product is even. We have handled every integer because parity exhausts the possibilities.

One can also observe that two consecutive integers always have opposite parity, which compresses the proof. But that shorter sentence is itself a theorem about parity. If a learner does not yet know it, the two-case argument makes its content explicit.

A case split does not need to be an 'either-or' that excludes overlap. If we know that P or Q holds and both cases separately imply R, then R follows even when P and Q are both true. The important condition is completeness: every admissible input falls under at least one case. Disjoint cases can simplify bookkeeping but are not always required.

## Case splits can hide gaps

A common example is dividing a proof into x positive and x negative, forgetting x equals zero. Another is dividing functions into increasing and decreasing without considering functions that are neither. Before you proceed, ask whether your alternatives are really exhaustive.

Even a correct split may leave details unproved. Suppose an expression depends on the sign of a denominator. If the denominator might be zero, neither positive nor negative cases permit division. You must establish nonzeroness first or add a separate case. Hypotheses are not decorations; they prevent illicit operations.

## Selecting a technique rather than memorizing it

How should you choose between direct proof, contraposition, and cases? Read the goal. If it asks for a witness or an identity, direct proof is often natural. If it says that a bad outcome cannot occur, contraposition may turn the negative conclusion into a concrete assumption. If the domain comes with a natural finite classification, such as even versus odd, signs, or residues modulo three, cases can turn a general claim into manageable subclaims.

For example, the square of any integer has remainder zero or one when divided by four. Prove this by even and odd cases. In the even case n equals twice k, and n squared is divisible by four. In the odd case the expansion gives four times the sum of k squared and k, plus one. This small lemma later becomes useful in proving that certain Diophantine equations have no integer solutions. The point of a proof technique is not to display cleverness. It is to expose the structure that makes a theorem true.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Parity calculation

For any \(n\in\mathbb Z\), \(n^2\equiv 0\) or \(1\pmod4\).

- If \(n=2k\), then \(n^2=4k^2\).
- If \(n=2k+1\), then \(n^2=4k(k+1)+1\).

Thus no integer square is congruent to \(2\pmod4\).

### Exercises with answers

1. Prove that if \(n^2\) is odd, then \(n\) is odd by contraposition. **Answer:** if \(n=2k\), then \(n^2=4k^2\) is even.
2. Show \(n(n+1)\) is even. **Answer:** for even \(n\), the first factor is even; for odd \(n\), \(n+1\) is even.
3. Why do cases \(x<0\) and \(x>0\) not exhaust the reals? **Answer:** \(x=0\) is omitted.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Proof by contrapositive](https://en.wikipedia.org/wiki/Proof_by_contrapositive).
