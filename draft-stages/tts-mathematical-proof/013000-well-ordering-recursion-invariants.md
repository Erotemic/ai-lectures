# 013000 — Strong Induction, Recursion, and Well-Ordering

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Mathematical induction and divisibility. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Strong Induction, Recursion, and Well-Ordering

Ordinary induction proves a statement at n plus one from its truth at n. Sometimes a problem needs information about several earlier stages, not just the immediately preceding one. Strong induction says we may assume the statement for every smaller natural number when proving it for n, provided we have established the appropriate starting point. Strong induction is not a stronger conclusion than ordinary induction; it is a different way of organizing the same well-ordering structure.

## Factoring a natural number into primes

Every integer greater than one is a product of primes. To prove this, consider any integer n greater than one and suppose the claim is already known for every integer strictly between one and n. If n is prime, it is a product of one prime, itself. Otherwise n is composite, so n equals a times b for integers a and b strictly between one and n. By the strong induction hypothesis, both a and b can be expressed as products of primes. Concatenating those factorizations gives a prime factorization of n.

The proof would be awkward using only the case n minus one, because the factors a and b need not be n minus one. Strong induction permits us to use whatever smaller values the structure of the number actually supplies. We must still show that a and b are smaller than n; otherwise the use of the induction hypothesis would be unjustified.

## The least-counterexample viewpoint

Suppose the theorem were false. Then there would be at least one integer greater than one with no prime factorization. By the well-ordering principle, the set of counterexamples has a least element n. It cannot be prime. If it is composite, its two proper positive factors are smaller than n and therefore are not counterexamples. They have prime factorizations, so n does too, a contradiction. This proof is the strong-induction argument told from the other direction.

Well-ordering says every nonempty subset of the natural numbers has a least element. It is more than the assertion that we can sort a finite list. It applies to arbitrary nonempty sets of natural numbers, even infinite ones. This principle can be used to prove ordinary induction and vice versa, given the standard natural-number setting.

## Recursive descriptions and algorithms

A recursive definition expresses a new value through earlier ones. The factorial function satisfies factorial of zero equals one, and factorial of n plus one equals n plus one times factorial of n. These clauses specify a value at every natural number because each evaluation moves toward the base case. A recursive program that calls itself on the same input may not terminate; the mere presence of recursive syntax does not establish a well-defined finite computation.

For the greatest common divisor, the Euclidean algorithm repeatedly replaces a pair of nonnegative integers by the smaller member and its remainder. The key fact is that the remainder is strictly smaller than the previous positive divisor. That quantity is a decreasing nonnegative integer, so the process cannot continue forever. The algorithm also preserves the set of common divisors because a number divides both a and b exactly when it divides b and the remainder after dividing a by b. Together, preservation and termination justify its result.

This is a common two-part proof in algorithms: an invariant establishes correctness if the algorithm stops, and a well-founded measure establishes that it must stop. In discrete mathematics, structural induction on trees, lists, and expressions follows the same idea: prove a property for basic constructors, then show that building a larger object from smaller ones preserves it.

## A recurrence with two predecessors

Consider the Fibonacci sequence, defined by its first two values and by each later value being the sum of the previous two. To prove that all terms are nonnegative, the base requires both starting values. In the step for term n plus one, we need nonnegativity of two earlier terms. Strong induction provides both, or we can strengthen the ordinary induction invariant to cover a consecutive pair. This choice illustrates proof design: sometimes a more informative induction hypothesis makes an argument easier.

Induction is not only a technique for statements involving an n in a formula. It is a way of exploiting well-founded construction. Whenever a mathematical object is made from smaller objects, ask what the notion of 'smaller' is and why descending forever is impossible. The answer may be a natural number, tree height, expression size, or another well-founded order. Once that structure is explicit, a proof that initially looked infinite becomes a finite case analysis plus a justified recursive step.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Strong induction and a termination measure

Let \(P(n)\): 'if \(n\geq2\), then \(n\) is a finite product of primes.' Assuming \(P(k)\) for every \(2\leq k<n\), either \(n\) is prime or \(n=ab\) with \(2\leq a,b<n\). By the hypothesis both factors have prime factorizations. This proves \(P(n)\).

For the Euclidean algorithm, if \(a=qb+r\), \(0\leq r<b\), then
\[
\gcd(a,b)=\gcd(b,r).
\]
The positive divisor in the recursive pair strictly decreases, guaranteeing termination by well-ordering of \(\mathbb N\).

### Exercises with answers

1. Prove a finite rooted binary tree has an odd number of vertices when each internal vertex has two children. **Answer:** by structural induction: a leaf has one; joining two trees under a new root changes the count to \(1+(2a+1)+(2b+1)=2(a+b+1)+1\).
2. Explain why a recursive function with a base clause might still fail to terminate. **Answer:** recursive calls may not approach a well-founded smaller argument.
3. State a measure proving termination of repeated subtraction from a positive integer. **Answer:** the nonnegative integer current value, provided each step strictly decreases it and remains nonnegative.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Mathematics in Lean, Lean community documentation](https://leanprover-community.github.io/mathematics_in_lean/index.html).
- [Wikipedia: Well-ordering principle](https://en.wikipedia.org/wiki/Well-ordering_principle).
