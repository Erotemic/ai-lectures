# 023000 — Chebyshev Functions and the First Serious Bounds on Prime Counts

**Track:** Number Theory from First Principles. **Background:** prime factorization, binomial coefficients, logarithms, summation by parts, and Euler products. **Aim:** prove \(\psi(x)=\Theta(x)\) and \(\pi(x)=\Theta(x/\log x)\) by elementary arguments and locate the remaining gap to the prime number theorem.

<!-- BEGIN SPOKEN LECTURE -->

# Chebyshev Functions and the First Serious Bounds on Prime Counts

How many primes are there below a large number x? Euclid guarantees that the answer grows without bound. Dirichlet's theorem guarantees infinitely many primes in every arithmetic progression whose remainder is relatively prime to its modulus. Neither result tells us how quickly the count grows.

A first guess might be that primes thin out as numbers get larger. They do. But a guess is not a bound, and a bound is not an asymptotic formula. We will now prove that the number of primes up to x grows on the scale of x divided by log x. We will not prove that the ratio approaches one. That last assertion is the prime number theorem and requires additional work.

The most efficient route begins with an object that does not look like a prime-counting function at all: the least common multiple of the integers up to x.

## Two ways to weigh primes

Write pi of x for the number of primes no greater than x. It counts each prime with weight one. We will introduce two related sums that weigh primes using natural logarithms.

The first, conventionally called theta of x, adds log p once for each prime p up to x. Exponentiate the sum and you get the product of all those primes. In other words, theta is the logarithm of the product of the distinct primes no greater than x.

The second, called psi of x, adds log p for every prime power p, p squared, p cubed, and so on that is at most x. Equivalently, it is the sum of the von Mangoldt function over positive integers at most x. The von Mangoldt function is log p at a prime power and zero elsewhere.

Psi has another exact interpretation. The least common multiple of one, two, three, and so on up to the integer part of x contains each prime raised to the largest power of that prime not exceeding x. Taking its logarithm counts one log p for each exponent level. That is exactly psi of x.

For example, consider the integers through ten. The least common multiple of one through ten is two thousand five hundred twenty. The prime powers through ten are two, three, four, five, seven, eight, and nine. Each contributes the logarithm of its prime base. Together they give the logarithm of two thousand five hundred twenty. Theta of ten, on the other hand, is the logarithm of two times three times five times seven, the product of distinct primes only.

Why would psi be easier to estimate than pi? Factorials and binomial coefficients contain primes raised to powers. Psi is built to register those powers directly, making it a natural intermediary between elementary combinatorics and prime distribution.

## What a central binomial coefficient knows

Look at the central binomial coefficient: two m choose m. It counts the ways to select m objects from a collection of two m objects. The binomial theorem tells us that the sum of all two m plus one binomial coefficients in that row is four to the power m. The central coefficient is the largest entry in the row. Therefore it is at least four to the m divided by two m plus one, and at most four to the m.

Take natural logarithms. We have a lower estimate for log of the central coefficient, roughly two m times log two, and an upper estimate of two m times log two. The difference in the lower estimate is just log of two m plus one, which is small compared with m for large m.

Now examine the prime factorization of the central coefficient. The exponent of a prime p in a factorial is the number of multiples of p, plus the number of additional multiples of p squared, plus the number of additional multiples of p cubed, and so on. That is Legendre's factorial valuation formula.

Subtract the two copies of the exponent in m factorial from the exponent in two m factorial. At the level p to the kth power, the difference is the floor of two m divided by p to the kth, minus twice the floor of m divided by p to the kth. This quantity is either zero or one. The reason is elementary: doubling a real number doubles its integer part, and the remaining fractional part can contribute either zero or one additional integer when doubled.

Thus the exponent of p in the central binomial coefficient is at most the number of powers of p not exceeding two m. Multiplying the prime-power contributions gives an upper bound on the binomial coefficient by the least common multiple of all integers up to two m. Taking logarithms, log of two m choose m is no greater than psi of two m.

Combined with the lower bound from the binomial theorem, this yields our first major estimate: psi of two m is at least two m times log two, minus log of two m plus one. For large m, the first term dominates. Therefore psi of x is at least a positive constant times x when x is sufficiently large.

We have proved a lower bound on a function built from primes, using nothing more than counting subsets and inspecting prime exponents in factorials.

## An upper bound using the same coefficient

The same binomial coefficient provides the complementary bound. Consider a prime power p to the kth lying strictly between m and two m. At that level of the factorial valuation formula, the floor of two m divided by p to the kth is one, while the floor of m divided by p to the kth is zero. Thus this prime power contributes one full log p to the logarithm of the central binomial coefficient.

Different prime powers may belong to the same prime, but they correspond to different terms in the valuation formula. Adding them gives an exact inequality: psi of two m minus psi of m is at most log of two m choose m. And the binomial coefficient is at most four to the m.

Therefore the increase in psi between m and two m is at most two m times log two. In plain language, doubling the range can increase psi by at most a constant times the endpoint.

Apply this at m equal to one, two, four, eight, and so on. The increments from one to two, two to four, four to eight, and the rest are bounded by a geometric series. Summing that geometric series shows psi of two to the j is at most a constant times two to the j. Every positive x lies between successive powers of two. Since psi never decreases, the same kind of upper bound holds for every x.

We now have both sides: psi of x is bounded below by a positive constant times x and above by another positive constant times x, for all sufficiently large x. Mathematicians summarize this by saying psi of x has order x, or psi of x is theta of x in the asymptotic-order notation. The word theta here means an order-of-growth symbol, distinct from the named function theta of x; context separates them.

This is a real theorem, not a heuristic. It does not identify the best constants, and it does not claim the ratio psi of x divided by x has a limit. But it locates the correct linear scale.

## Remove the repeated prime powers

Psi counts prime powers. Theta counts only primes. Could all the extra copies of small primes account for most of psi? No, because a prime whose square is at most x must be at most the square root of x.

For each such prime, the total contribution from its squared, cubed, and higher powers is at most log x. There are at most square root x possible primes in that range, even under the crude bound that every integer might be prime. Therefore psi of x minus theta of x is at most square root x times log x.

That difference is small compared with x as x tends to infinity. The ratio of square root x times log x to x is log x divided by square root x, which tends to zero. Hence theta and psi differ by a lower-order term.

Since psi is bounded above and below by positive multiples of x, the same is true of theta for sufficiently large x. We have removed the complication of higher prime powers without sacrificing the scale of our estimate.

## Translate weights into counts

Every prime up to x contributes log p to theta, and log p cannot exceed log x. Thus theta of x is at most pi of x times log x. Rearranging gives a lower bound for the prime count: pi of x is at least theta of x divided by log x. Since theta is at least a constant times x, pi is at least a constant times x divided by log x.

The upper bound requires slightly more care, because log p can be much smaller than log x for the smallest primes. Divide the prime list into those at most the square root of x and those larger than the square root of x.

There are at most square root x primes in the first group. Each prime in the second group has log p greater than half of log x. Consequently the number of primes in the second group is at most twice theta of x divided by log x.

Add the two groups. Pi of x is at most square root x plus twice theta of x divided by log x. The theta bound makes the second term at most a constant times x divided by log x. The first term, square root x, is smaller order than x divided by log x. We conclude that pi of x is also at most a constant times x divided by log x.

Both inequalities are established. For sufficiently large x, the number of primes up to x lies between two fixed positive multiples of x divided by log x. This is a version of Chebyshev's theorem on the scale of the prime-counting function.

Pause to compare what we have and have not proved. We did not derive an approximation by fitting numerical prime counts. We obtained matching orders of growth from factorial arithmetic and the binomial theorem. But we have not proved that the quotient of pi of x by x divided by log x approaches one. Matching upper and lower scales leave room for different constants and for oscillations between them.

## Summation by parts connects the scales

There is a direct relation between pi and theta. Theta adds log p; pi adds one. To convert one into the other, write one as log p times one over log p and apply summation by parts. The result is pi of x equals theta of x divided by log x, plus the integral, from two to x, of theta of t divided by t times the square of log t.

This exact formula explains why knowledge of theta controls the prime count. If we somehow established the much stronger statement that theta of x divided by x tends to one, then the first term would behave like x divided by log x. The integral would be a smaller correction, on the order of x divided by the square of log x. That would prove pi of x is asymptotic to x divided by log x.

Conversely, an asymptotic for pi would imply the corresponding one for theta. The assertion that theta of x is asymptotic to x, or equivalently that psi of x is asymptotic to x, is another form of the prime number theorem. We have reached the correct framework but not yet the theorem itself.

The analytic side of our course also knows about psi. For real s greater than one, the negative logarithmic derivative of zeta is the Dirichlet series whose coefficients are the von Mangoldt function. By summation by parts, it is s times the integral of psi of x against x to the negative s minus one.

We therefore have two complementary views of the same function. The binomial-coefficient argument estimates it through finite arithmetic. The zeta logarithmic derivative encodes it through an infinite analytic transform. The prime number theorem emerges when one proves enough about the analytic transform to determine the leading coefficient of psi, not merely its order of growth.

## The boundary ahead

Chebyshev's bounds are valuable independently of the prime number theorem. They show that primes are neither so scarce that the count has lower order than x over log x, nor so abundant that it has a higher order. They also illustrate a useful principle in mathematical research: before trying to prove an exact asymptotic, identify the right quantity and obtain robust upper and lower estimates.

The same discipline will matter when we count primes in residue classes. Dirichlet's theorem gives their infinitude and reciprocal divergence, and character methods give their Dirichlet density. To obtain a counting formula for each class, we need stronger uniform analytic information. We should build that information without confusing a theorem about a single value of an L-function with a theorem about an entire vertical line.

For now, we have carried number theory from unique factorization and congruences to a universal lower and upper scale for prime counts. The proof required no unproved assertion about the zeroes of zeta. Everything rests on explicit estimates that can be checked, refined, and eventually connected to the more delicate theory of the prime number theorem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Definitions and exact arithmetic interpretations

For real \(x\ge2\),
\[
\pi(x)=\#\{p\le x:p\text{ prime}\},\quad
\vartheta(x)=\sum_{p\le x}\log p,\quad
\psi(x)=\sum_{p^k\le x}\log p=\sum_{n\le x}\Lambda(n).
\]
The least common multiple and primorial identities are
\[
\psi(x)=\log\operatorname{lcm}(1,2,\ldots,\lfloor x\rfloor),\qquad
\vartheta(x)=\log\prod_{p\le x}p.
\]
For example, \(\psi(10)=\log2520\) and \(\vartheta(10)=\log210\).

### Binomial inequalities and Chebyshev bounds

For integer \(m\ge1\),
\[
\frac{4^m}{2m+1}\le {2m\choose m}\le4^m.
\]
Legendre's formula gives
\[
v_p{2m\choose m}=\sum_{k\ge1}\left(\left\lfloor\frac{2m}{p^k}\right\rfloor-2\left\lfloor\frac m{p^k}\right\rfloor\right),
\]
where every term in parentheses is 0 or 1. It is 1 whenever \(m<p^k\le2m\). Thus
\[
\psi(2m)-\psi(m)\le\log{2m\choose m}\le\psi(2m).
\]
The right inequality together with the binomial lower bound yields
\[
\psi(2m)\ge2m\log2-\log(2m+1).
\]
For real \(x\), set \(m=\lfloor x/2\rfloor\). Then \(2m\ge x-1\), so
\[
\psi(x)\ge(x-1)\log2-\log(x+1),
\]
which is \(\ge c x\) for any chosen \(c<\log2\) and sufficiently large \(x\).

For \(m=2^{j-1}\), \(\psi(2^j)-\psi(2^{j-1})\le2^j\log2\). Summing from \(j=1\) to \(J\) gives \(\psi(2^J)<2^{J+1}\log2\). For any \(x\ge2\), choose \(J\) with \(x\le2^J<2x\), obtaining
\[
\psi(x)<4x\log2.
\]
Hence there are constants \(c,C>0\) with \(cx\le\psi(x)\le Cx\) for all sufficiently large \(x\).

For prime powers of exponent \(k\ge2\), the base prime is at most \(\sqrt{x}\), and the total extra contribution per prime is at most \(\log x\). Consequently
\[
0\le\psi(x)-\vartheta(x)\le\sqrt{x}\log x=o(x).
\]
Thus \(\vartheta(x)=\Theta(x)\). The count satisfies
\[
\frac{\vartheta(x)}{\log x}\le\pi(x)
\le\pi(\sqrt{x})+\frac{2\vartheta(x)}{\log x}
\le\sqrt{x}+\frac{2\vartheta(x)}{\log x}.
\]
Therefore
\[
\boxed{\pi(x)=\Theta\!\left(\frac{x}{\log x}\right)}.
\]
Here \(\Theta\) in the box denotes the two-sided order-of-growth relation, while \(\vartheta\) is Chebyshev's first function.

### Partial summation and what is not proved

The exact Abel-summation identity is
\[
\pi(x)=\frac{\vartheta(x)}{\log x}+\int_2^x\frac{\vartheta(t)}{t(\log t)^2}\,dt.
\]
For \(\Re s>1\),
\[
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=s\int_1^\infty\psi(x)x^{-s-1}\,dx.
\]
The **prime number theorem**, not established here, is equivalent to \(\psi(x)\sim x\), to \(\vartheta(x)\sim x\), and to \(\pi(x)\sim x/\log x\). For example, if \(\vartheta(x)\sim x\), the integral term in the partial-summation identity is \(O(x/(\log x)^2)\), so \(\pi(x)\sim x/\log x\). Conversely, if \(\pi(x)\sim x/\log x\), summation by parts gives \(\vartheta(x)=\pi(x)\log x-\int_2^x\pi(t)/t\,dt\sim x\). The elementary Chebyshev bounds do not establish those asymptotic equivalences on their own.

### Exercises

1. Compute \(\operatorname{lcm}(1,\ldots,12)\), \(\psi(12)\), and \(\vartheta(12)\). Which prime powers account for the difference?
2. Prove that the middle entry of row \(2m\) in Pascal's triangle is the largest, and derive both binomial bounds.
3. Verify for \(m=5\) the inequalities \(\psi(10)-\psi(5)\le\log{10\choose5}\le\psi(10)\).
4. Prove that every summand in Legendre's formula for \(v_p{2m\choose m}\) is 0 or 1.
5. Write the dyadic sum explicitly, with no asymptotic notation, and find a valid numerical upper constant for \(\psi(x)/x\) for all \(x\ge2\).
6. Prove \(\sqrt{x}\log x=o(x)\), and show why the prime-power correction is negligible in a statement about limits divided by \(x\).
7. Derive the partial-summation formula relating \(\pi\) and \(\vartheta\). Explain what new assertion would convert the bounds to the full prime number theorem.

### Sources and further reading

- Manuel Eberl, [Prime Distribution Elementary: Elementary Prime Bounds](https://isa-afp.org/browser_info/current/AFP/Prime_Distribution_Elementary/Elementary_Prime_Bounds.html), formally checked elementary Chebyshev-type bounds.
- Andrew V. Sutherland, [Number Theory I, MIT OpenCourseWare](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/), for the analytic prime-counting context and distinctions among estimates.
- Wikipedia: [Chebyshev function](https://en.wikipedia.org/wiki/Chebyshev_function), [Prime-counting function](https://en.wikipedia.org/wiki/Prime-counting_function), [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem), [Von Mangoldt function](https://en.wikipedia.org/wiki/Von_Mangoldt_function).
