# 001000 — Divisibility, Euclid's Algorithm, and the Architecture of Prime Factorization

**Track:** Number Theory from First Principles. **Background:** integer arithmetic and basic algebra. **Theme:** turning questions about whole numbers into proofs and algorithms.

<!-- BEGIN SPOKEN LECTURE -->

# Divisibility, Euclid's Algorithm, and the Architecture of Prime Factorization

Suppose you have two lengths of ribbon, two hundred fifty-two centimeters and one hundred ninety-eight centimeters. You want to cut both into pieces of the same integer length, with no waste. How long can the pieces be? You could test every possible length. But there is a better question: what remains unchanged when you replace the longer ribbon by the difference between the two lengths?

Any length that divides both original ribbons also divides their difference. And any length that divides the shorter ribbon and that difference also divides the longer ribbon, because the longer length is the sum of the other two. We have discovered an operation that changes the numbers but does not change their common divisors. That is the key to one of the most productive algorithms in mathematics.

The subject is number theory: the study of integers, the relationships of divisibility among them, and the structures that emerge when we ask which equations have integer solutions. Integers are familiar enough to invite experiments, but rigid enough to support proofs that work for arbitrarily large numbers. We will begin with divisibility, build an algorithm for greatest common divisors, and use it to explain why prime factorization is unique.

## Dividing exactly is a relation, not an operation

When we say that a divides b, we mean there is an integer k such that b equals a times k. This is different from ordinary division, which can always produce a fraction when the divisor is nonzero. Eight divides forty, because forty is eight times five. Eight does not divide forty-two, because no integer multiplier works.

The multiplier may be negative or zero. Three divides negative fifteen. Every nonzero integer divides zero, since zero is its product with zero. Zero divides only zero; it cannot divide a nonzero integer. These details are not accidents. They are consequences of the definition, and making definitions do the work is an essential proof habit.

Divisibility composes. If a divides b, and b divides c, then a divides c: write b as a times one integer and c as b times another, then substitute. Divisibility also survives integer linear combinations. If d divides a and b, it divides a times any integer plus b times any integer. Keep that second fact in mind. It will turn a greatest common divisor into a certificate you can carry around.

A common divisor of a and b divides each. Their greatest common divisor, usually abbreviated G C D, is the largest positive common divisor when at least one number is nonzero. The positive convention avoids ambiguity from signs. The G C D of zero and a nonzero integer is the absolute value of that integer. We will not need to assign a positive greatest common divisor to the pair zero, zero.

Back to our ribbons. Their G C D is eighteen. Eighteen is the longest integer piece length that cuts both exactly. But asserting eighteen is not the same as demonstrating it. We want a procedure that finds eighteen and a proof that no larger common divisor was overlooked.

## Why the Euclidean algorithm works

Here is the division principle for positive integers. Given a number a and a positive divisor b, there is a unique quotient q and remainder r such that a equals q times b plus r, with r at least zero and strictly less than b. For instance, two hundred fifty-two is one hundred ninety-eight plus fifty-four.

Now notice: a number divides both a and b precisely when it divides both b and the remainder r. In one direction, if it divides a and b, it divides their difference a minus q times b, which is r. In the other direction, if it divides b and r, it divides q times b plus r, which is a. So the set of common divisors is identical for the two pairs. In particular, the greatest common divisor is unchanged.

Apply this repeatedly. Two hundred fifty-two divided by one hundred ninety-eight leaves fifty-four. One hundred ninety-eight divided by fifty-four leaves thirty-six. Fifty-four divided by thirty-six leaves eighteen. Thirty-six divided by eighteen leaves zero. The last nonzero remainder is eighteen.

Why does this stop? At each step the next nonzero remainder is a smaller positive integer than the previous divisor. There cannot be an infinite strictly decreasing sequence of positive integers. The algorithm terminates, and each step has preserved the G C D. When the remainder is zero, the divisor plainly divides the preceding number; it is their greatest common divisor.

That is a complete algorithmic proof. It gives a computational procedure, says why every move preserves the answer, and supplies a reason the procedure finishes. Those are separate requirements. A procedure that usually works in examples, but has no termination argument, is not yet a full algorithmic theorem.

## An answer that comes with a witness

The calculation can do more than output eighteen. We can reverse the steps to express eighteen as an integer combination of our original numbers. From the last nontrivial division, eighteen is fifty-four minus thirty-six. Since thirty-six is one hundred ninety-eight minus three times fifty-four, eighteen is four times fifty-four minus one hundred ninety-eight. And fifty-four is two hundred fifty-two minus one hundred ninety-eight. Therefore eighteen is four times two hundred fifty-two minus five times one hundred ninety-eight.

This is an instance of Bézout's identity. For integers a and b, not both zero, there exist integers s and t such that the greatest common divisor of a and b equals s times a plus t times b. The Euclidean algorithm can find those coefficients by back-substitution. They are not generally unique.

The identity is more than a computational convenience. Suppose someone claims that the G C D of our two ribbon lengths is thirty-six. We can refute the claim without searching all divisors: every common divisor divides every integer combination of the numbers, hence must divide eighteen. A common divisor larger than eighteen could not do that.

There is also a beautiful proof of Bézout's identity that starts not with the algorithm but with the smallest positive number expressible as an integer combination of a and b. Call it d. Divide a by d, getting a remainder smaller than d. Because both a and d are integer combinations of a and b, so is that remainder. If the remainder were positive, it would contradict the choice of d as the smallest positive such combination. So d divides a. The same reasoning shows d divides b. Every common divisor divides d, because it divides every integer combination. Thus d is exactly the G C D.

The two proofs illuminate different aspects of the same theorem. The least-positive-combination argument proves existence conceptually. The Euclidean algorithm produces an explicit witness efficiently. In mathematics, an existence proof and a construction are complementary, not interchangeable.

## Relatively prime does not mean prime

Two integers are called coprime, or relatively prime, when their greatest common divisor is one. Fifteen and twenty-eight are coprime, even though neither is prime. Being coprime describes a relationship between two numbers, not a property of either number alone.

Bézout's identity becomes particularly strong in this case. If a and b are coprime, some integer combination of them is exactly one. Multiply that equation by any integer c and you get a new identity involving c. This leads to the following divisibility principle: if a is coprime to b and a divides b times c, then a divides c.

To see it, take integers s and t with s times a plus t times b equal to one, and multiply by c. The term s times a times c is divisible by a. The term t times b times c is also divisible by a under our assumption. Their sum is c. Therefore a divides c.

We are now ready for primes. A prime is a positive integer greater than one whose only positive divisors are one and itself. Every integer greater than one has some prime divisor: if the integer is not itself prime, split it into smaller positive factors; continue until a factor can no longer be split. The process cannot descend indefinitely.

If a prime p divides a product b times c, then p divides at least one of b or c. Why? If p does not divide b, their greatest common divisor must be one, because p has only two positive divisors. Our coprime divisibility principle then forces p to divide c. This is Euclid's lemma.

Be careful: the lemma is not true with an arbitrary composite number in place of p. Six divides two times three, but six divides neither two nor three. The primality hypothesis carries the entire conclusion.

## Why prime factorization is unique

Existence of prime factorization follows by repeatedly breaking composites into smaller factors. Uniqueness is a different question. Could the same positive integer have two genuinely different lists of prime factors?

Assume a number greater than one has two prime factorizations. Take one prime p from the first list. Since p divides the whole product on the other side, Euclid's lemma says it divides at least one prime factor on that side. A prime can divide another prime only if the two are equal. So p occurs in both lists. Cancel that common factor and repeat. Eventually every factor is matched. The factorizations differ only by their order.

This is the fundamental theorem of arithmetic: every positive integer greater than one factors as a product of primes, uniquely up to reordering. For negative integers, a sign is added. The positive and negative units, one and negative one, do not count as primes.

The theorem explains why prime factors act as atoms of ordinary integer multiplication. It also explains why many questions about integers can be broken into independent questions about prime powers. But it is important not to project that conclusion onto every arithmetic system. When mathematicians later study rings of algebraic integers, unique factorization into elements can fail. This failure is a major motivation for ideals and algebraic number theory. Here, for ordinary integers, we have proved exactly why it works.

## An infinite supply of primes

Prime factorization is not the end of the story. Could there be only finitely many primes? Imagine a complete list: p one through p k. Multiply them all together and add one. The new integer is greater than one, so it has a prime divisor. Yet division by any prime on our list leaves remainder one, because our number is one more than a multiple of that prime. Its prime divisor cannot be on the list. We have contradicted the claim that the list was complete.

Notice what this argument does not establish. The product plus one need not itself be prime. For instance, two times three times five times seven times eleven times thirteen plus one is not guaranteed to be prime merely because of its construction. The proof needs only a prime factor not already in the list.

This distinction is a useful model of rigorous reasoning. Prove the conclusion you need, not a stronger sentence that merely sounds related. An argument can be decisive without being extravagant.

We began with a cutting problem and found an algorithm, a proof of termination, an integer identity, a divisibility lemma, unique factorization, and infinitely many primes. The sequence is not a collection of tricks. Each idea supplies exactly the missing ingredient for the next. The Euclidean algorithm is a machine for discovering structure; Bézout's identity turns its answer into a certificate; prime factorization shows how much structure can be built from that certificate.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Exact statements and computations

For integers \(a,b\) with \(b>0\), division with remainder supplies unique \(q,r\) with \(a=bq+r\), \(0\le r<b\). The key invariant is

\[
\gcd(a,b)=\gcd(b,a-qb)=\gcd(b,r).
\]

For the running example:

\[
\begin{aligned}
252&=1(198)+54,\\
198&=3(54)+36,\\
54&=1(36)+18,\\
36&=2(18),\\
18&=4(252)-5(198).
\end{aligned}
\]

For \((a,b)\ne (0,0)\), there exist \(s,t\in\mathbb Z\) such that \(\gcd(a,b)=sa+tb\). A useful equivalent formulation is that the ideal \(a\mathbb Z+b\mathbb Z\) equals \(\gcd(a,b)\mathbb Z\). This language is optional preparation for abstract algebra.

Euclid's lemma: for prime \(p\), \(p\mid ab\Rightarrow p\mid a\) or \(p\mid b\). The distinct stronger-looking statement for composite \(p\) is false: \(6\mid2\cdot3\) while \(6\nmid2\) and \(6\nmid3\).

### Practice and reasoning checks

1. Compute \(\gcd(414,662)\) with the Euclidean algorithm. Back-substitute to express it as an integer combination. *Check:* \(\gcd(414,662)=2\).
2. Prove that \(\gcd(a,a+b)=\gcd(a,b)\), including cases where \(a\) or \(b\) is negative.
3. Prove that if \(\gcd(a,b)=1\), \(a\mid c\) and \(b\mid c\), then \(ab\mid c\).
4. Explain precisely why the product of all primes on a hypothetical finite list, plus one, does **not** have to be prime.

### Sources and further reading

- MIT OpenCourseWare, *18.781 Theory of Numbers*, lectures 1–2: divisibility, GCD, Euclidean algorithm, and primes: https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/
- William Stein, *Elementary Number Theory: Primes, Congruences, and Secrets*, chapters on primes: https://www.wstein.org/ent/
- Wikipedia background: [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm), [Bézout's identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity), [Fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic).
