# 013000 — Primality Tests, Compositeness Witnesses, and Certificates

**Track:** Number Theory from First Principles. **Background:** divisibility, modular exponentiation, Fermat's little theorem, the Chinese remainder theorem. **Theme:** distinguishing quick evidence, proof, and the separate task of finding factors.

<!-- BEGIN SPOKEN LECTURE -->

# Primality Tests, Compositeness Witnesses, and Certificates

A prime has only two positive divisors. That definition is short, but it is not an algorithm. If someone hands us a number with a thousand decimal digits, should we try dividing by every integer up to its square root? Can we establish primality without knowing all its factors? And what would it mean to provide a proof that another person or program can verify?

Number theory makes an important distinction between three questions. Does a number have a nontrivial factor? Can we find such a factor? Can we certify that there is no such factor? These questions are related, but their algorithms need not have the same cost. A compositeness test may produce evidence without actually finding a factor. A primality certificate may prove primality without performing trial division up to the square root.

We will build these distinctions from elementary arithmetic. Our main example will be the number three hundred forty-one, which is composite but can fool a simple test. We will also construct an exact certificate that twenty-nine is prime.

## The straightforward methods and their cost

If n equals a times b with integers a and b both greater than one, at least one of a or b is at most the square root of n. Otherwise their product would exceed n. Therefore trial division by every integer from two through the square root of n is an exact primality test. If none divides, n is prime. It is also a factoring method whenever it encounters a divisor.

There are fewer candidates if we test only primes, and we can generate those primes with the sieve of Eratosthenes. Start with the integers up to a bound, mark the multiples of two after two, then of three after three, and continue. Any composite up to the bound has a prime divisor no larger than its square root, so crossing out multiples for primes up to that point is enough. Begin crossing out at p squared because every smaller composite multiple of p was already crossed out by a smaller prime factor.

The sieve answers a *batch* question: which integers up to a specified bound are prime? Trial division answers a *single-number* question. Both are exact. Their cost depends on what we count. The number of divisibility trials up to square root n grows roughly like square root n, which is exponential in half the number of binary digits of n. Efficient sieving over an interval has a much better cost per integer when we need the whole interval, but sieving up to the square root of a thousand-digit input is still an enormous request.

We need to use properties other than direct division.

## Modular exponentiation is cheap, but its converse is false

Fermat's little theorem says that if n is prime and a is not divisible by n, then a to the power n minus one leaves remainder one modulo n. We can compute this enormous-looking power without expanding it. Square a, reduce the answer modulo n, square again, reduce again, and multiply only the powers indicated by the binary digits of the exponent. This repeated-squaring method needs only a number of modular multiplications proportional to the number of exponent bits.

That gives a fast way to detect some composite numbers. If we choose a and a to the power n minus one is not one modulo n, we have a **proof of compositeness**. A prime could not behave that way, assuming a is coprime to n. If a shares a nontrivial greatest common divisor with n, we already have an even more direct proof: we have found a factor.

But if the power *is* one, the result does not prove primality. Three hundred forty-one equals eleven times thirty-one, yet two to the power three hundred forty is one modulo three hundred forty-one. This number is a Fermat pseudoprime to base two. It passes a necessary test for primes despite being composite.

There are even composite numbers that pass the Fermat congruence for **every** base coprime to them. They are called Carmichael numbers; five hundred sixty-one is a standard example. The failure is structural, not just bad luck with one base. We must extract more information from the repeated squarings.

## What a prime allows when we take square roots of one

For an odd prime p, suppose x squared is one modulo p. Then x minus one times x plus one is zero modulo p. Since p is prime, p divides at least one of the factors. Therefore x is congruent to one or negative one. There are no other square roots of one in a field with odd prime modulus.

For a composite modulus, there may be other roots. Modulo three hundred forty-one, the number thirty-two is neither one nor negative one, yet thirty-two squared, which is one thousand twenty-four, leaves remainder one. Indeed, one thousand twenty-four equals three times three hundred forty-one plus one.

This is what the Miller–Rabin test looks for. Write n minus one as an odd number d multiplied by a power of two, say two to the s. For a chosen base a, compute x equal to a to the power d modulo n. If x is one or negative one, the base passes. Otherwise repeatedly square x, at most s minus one times, checking whether negative one appears. If negative one appears, the base passes. If it never appears, the base is a **witness of compositeness**. A nontrivial greatest common divisor between the base and n is also immediate evidence of compositeness.

Why can a prime never fail this test? For a prime, Fermat's theorem guarantees that after s total squarings the result is one. If the first value is already one, we pass. If not, consider the first point in the squaring chain at which one appears. Its predecessor is a square root of one that is not one. Modulo a prime, that predecessor must be negative one. So a prime necessarily passes at every allowed base.

This is a proof of the test's one-sided correctness: **a reported witness means composite, never prime**. A passing base, however, means only that this particular attempt found no witness.

## Three hundred forty-one exposes the failure

For three hundred forty-one, n minus one is three hundred forty, equal to four times eighty-five. Here s is two and d is eighty-five. Choose base two. Repeated modular squaring gives two to the power eighty-five congruent to thirty-two modulo three hundred forty-one. The next square is one.

But thirty-two is neither one nor negative one modulo three hundred forty-one, and no negative one appeared along the way. The test declares the number composite. It has caught precisely the phenomenon that the simpler Fermat test ignored: a nontrivial square root of one.

In this example, we can even extract the factors. Because thirty-two squared minus one factors as thirty-one times thirty-three, and three hundred forty-one divides their product, taking the greatest common divisor of thirty-one and three hundred forty-one gives thirty-one. The corresponding divisor from thirty-three is eleven. The test did not require those gcd calculations to establish compositeness, and not every witness makes factoring equally convenient.

Try five hundred sixty-one, the Carmichael number. Base two passes its Fermat test, but the strong test's squaring chain is not compatible with the behavior of a prime. A theorem can fail to recognize compositeness because it ignores intermediate structure; strengthening the invariant can restore its usefulness.

## Why some witness always exists for an odd composite

Can an odd composite fool the strong test at every base? No. Here is a direct existence proof that does not use probability.

First suppose n has at least two distinct prime divisors. Split its prime-power factors into two nontrivial, coprime integers r and t with n equal to r times t. The Chinese remainder theorem lets us choose a number b that is one modulo r and negative one modulo t. Because both moduli are odd and greater than one, b is neither one nor negative one modulo n. But b squared is one modulo both r and t, hence modulo n.

The odd exponent d in the strong test preserves b: b to the power d is b. Its next square is one. So the strong test sees a value different from both one and negative one, followed by one. It must declare n composite. We have constructed a strong witness using the Chinese remainder theorem.

There is one remaining type of odd composite: a power p to the k of a single odd prime, with k at least two. Choose the base one plus p to the k minus one. The binomial theorem shows that raising this base to n minus one gives one plus the product of n minus one and p to the k minus one, modulo p to the k. Since n minus one is not divisible by p, that result is **not** one. This base already fails Fermat's test, and therefore also fails the strong test.

We have proved that every odd composite has at least one Miller–Rabin witness. The argument establishes existence, not how many bases are witnesses. The proportion matters when bases are selected at random.

## Where the probability guarantee comes from

A deeper counting result due to Louis Monier and Michael Rabin says that for every odd composite n, at most one quarter of the bases from one through n minus one are strong liars: bases that pass the strong test even though n is composite. Thus a uniformly sampled independent base gives a false pass with probability at most one quarter. After k independent random tests, the probability that a fixed odd composite passes every test is at most one quarter to the power k.

That **one-quarter bound is an additional theorem**, not something implied by our existence proof. It relies on counting suitable residue classes and subgroups; its proof is available in the cited references. We are using it here with its precise hypotheses rather than disguising it as an immediate consequence of Fermat's theorem.

There are two further qualifications. First, probability belongs to the random choice of bases, not to some uncertain status of the integer. The integer is prime or composite regardless of our sampling. Second, repeating a fixed or correlated list of bases is not the same probability experiment as drawing independent uniformly random bases. For bounded machine integers, carefully established fixed-base lists can instead give deterministic algorithms, but their correctness requires a separate finite-range proof.

## A certificate that a number really is prime

It is possible to go beyond probable primality and produce a finite object that proves primality. One particularly instructive criterion starts from the factorization of n minus one.

Suppose we know every prime factor q of n minus one, and find one integer a with two properties. First, a to the power n minus one is one modulo n. Second, for every distinct prime q dividing n minus one, the greatest common divisor of a to the power (n minus one) divided by q minus one, and n, is one.

These conditions force n to be prime. To prove it, let p be any prime factor of n. The first condition means that the multiplicative order of a modulo p divides n minus one. The gcd conditions ensure that for every prime q dividing n minus one, this order does **not** divide (n minus one) divided by q. Therefore the order includes the full power of every prime q occurring in n minus one, and must equal n minus one itself.

But modulo the prime p, the multiplicative order divides p minus one. Thus n minus one divides p minus one, so p is at least n. Since p also divides n and is positive, p equals n. The original number has no proper prime factor. It is prime.

Let's verify twenty-nine. Its predecessor, twenty-eight, factors as four times seven; two and seven are primes. Use a equal to two. Two to the twenty-eighth power is one modulo twenty-nine. Two to the fourteenth is negative one modulo twenty-nine, so its difference from one has gcd one with twenty-nine. Two to the fourth is sixteen, and sixteen minus one also has gcd one with twenty-nine. These are exactly the required checks for q equal to two and seven. We have a complete primality certificate for twenty-nine using only modular powers, greatest common divisors, and the short list of prime factors of twenty-eight.

If the prime factors of n minus one are not already known, the certificate may require serious additional work. Recursive certificates can themselves certify those smaller primes. Other methods, including elliptic-curve primality proving and deterministic polynomial-time algorithms, use different machinery. The logical distinction persists: checking a supplied proof can be far easier than finding it.

## Primality is not factoring

A Miller–Rabin witness can establish compositeness without yielding a useful factor. A primality certificate can establish primality without trying every possible divisor. None of this says factoring is easy. Nor does a fast test for primality by itself provide a fast factoring algorithm.

For actual computations one should also care about arithmetic cost, handling of edge cases such as n equal to one or an even number, and the quality of randomness when making probabilistic claims. The mathematics tells us what the evidence means. Engineering determines whether a particular program implements the test correctly.

The most useful lesson is not a preferred algorithm name. It is the separation between **necessary tests, decisive witnesses, probabilistic confidence, and verifiable proofs**. Once we keep those distinctions straight, a large number is no longer a mysterious yes-or-no question. It is a mathematical object about which different algorithms can supply different, precisely justified kinds of information.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Cost and proof obligations

- Trial division: if \(n=ab\) with \(1<a\le b\), then \(a\le\sqrt n\). No divisor \(\le\sqrt n\) proves primality.
- Sieve of Eratosthenes: to mark composites \(\le B\), mark multiples of each unmarked prime \(p\le\sqrt B\), beginning at \(p^2\).
- Binary modular exponentiation computes \(a^e\bmod n\) in \(O(\log e)\) modular multiplications; this is **not** a statement that the multiplications have constant bit cost.

### Strong probable-prime test, for odd \(n\ge5\) (handle 2 and 3 separately)

Write \(n-1=2^s d\) with \(d\) odd and choose a base \(1<a<n-1\). If \(\gcd(a,n)>1\), n is composite. Otherwise set \(x=a^d\bmod n\). If \(x=\pm1\), the base passes. Otherwise square up to \(s-1\) times. If \(-1\) occurs, pass; otherwise the base is a **strong witness**.

**Prime soundness:** by Fermat, \(a^{2^s d}\equiv1\pmod n\) for prime n. The first \(1\) in the squaring chain must be preceded by \(-1\), unless the initial value was already \(1\), since a field has no other roots of \(X^2-1\).

**Every odd composite has a strong witness:**

1. If \(n=rt\) with \(r,t>1\) odd coprime, CRT gives \(b\equiv1\pmod r\), \(b\equiv-1\pmod t\). Then \(b^2\equiv1\pmod n\), \(b\not\equiv\pm1\pmod n\), and \(b^d=b\), so it is a witness.
2. If \(n=p^k,\ k\ge2\), take \(b=1+p^{k-1}\). Since \(2k-2\ge k\), binomial expansion gives
\[
b^{n-1}\equiv1+(n-1)p^{k-1}\not\equiv1\pmod {p^k}.
\]
Hence it is a Fermat witness and therefore a strong witness.

**Quantitative theorem (cited, not proved here):** for odd composite n, at most \((n-1)/4\) of bases \(1\le a\le n-1\) are strong liars (Monier–Rabin). Independent uniform sampling gives failure probability at most \(4^{-k}\) after k tests. A deterministic base list has a different justification.

### A composite that fools Fermat but not Miller–Rabin

\[
341=11\cdot31,\quad 340=4\cdot85,\quad
2^{340}\equiv1\pmod{341},\quad 2^{85}\equiv32\pmod{341},\quad32^2\equiv1\pmod{341}.
\]

The value 32 is neither 1 nor \(-1\) modulo 341. Therefore 2 is a strong witness. In this example \(\gcd(32-1,341)=31\), \(\gcd(32+1,341)=11\).

### Lucas-type primality certificate with fully factored \(n-1\)

Let \(n\ge2\), let the distinct prime divisors \(q\) of \(n-1\) be known and proved prime, and suppose an integer a satisfies
\[
a^{n-1}\equiv1\pmod n,\qquad
\gcd\bigl(a^{(n-1)/q}-1,n\bigr)=1
\quad\text{for every prime }q\mid n-1.
\]
For each prime \(p\mid n\), \(\operatorname{ord}_p(a)\mid n-1\) and does not divide \((n-1)/q\) for any such q. Hence \(\operatorname{ord}_p(a)=n-1\mid p-1\), forcing \(p\ge n\), so \(p=n\) and n is prime.

For \(n=29\), \(n-1=28=2^2\cdot7\), \(a=2\):
\[
2^{28}\equiv1,\quad2^{14}\equiv28,\quad2^4\equiv16\pmod{29};
\quad \gcd(27,29)=\gcd(15,29)=1.
\]

### Practice and reasoning checks

1. Verify all residues in the Miller–Rabin chain for \(n=341,a=2\) using repeated squaring, not direct expansion of \(2^{340}\).
2. For \(n=91\), find a base that fails Fermat's congruence, and explain what its output proves.
3. Use CRT to construct a nontrivial square root of 1 modulo \(15\) and explain why it is a strong witness.
4. Give a full certificate that 13 is prime by factoring 12 and finding a suitable base.
5. Explain why the mere existence of one strong witness does **not** imply the one-quarter error bound.

### Sources and further reading

- Menezes, van Oorschot and Vanstone, [*Handbook of Applied Cryptography*, Chapter 4](https://cacr.uwaterloo.ca/hac/about/chap4.pdf), especially Fact 4.23 and Algorithm 4.24 on strong liars and Miller–Rabin.
- Cornell CS 4820, [Miller–Rabin lecture notes](https://www.cs.cornell.edu/courses/cs4820/2019sp/handouts/MillerRabin.pdf), discussion of strong witnesses.
- Wikipedia background: [Miller–Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test), [Carmichael number](https://en.wikipedia.org/wiki/Carmichael_number), [Pratt certificate](https://en.wikipedia.org/wiki/Pratt_certificate), [AKS primality test](https://en.wikipedia.org/wiki/AKS_primality_test), [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
