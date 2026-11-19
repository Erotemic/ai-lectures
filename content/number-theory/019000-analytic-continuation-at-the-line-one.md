# 019000 — Crossing the Line One: Analytic Functions, Zeta, and Character Series

**Track:** Number Theory from First Principles. **Background:** real and complex numbers, series, partial summation, Dirichlet characters, and Euler products. **Aim:** establish the precise continuation and power-series facts needed for the nonvanishing proof, without treating analytic continuation as magic.

<!-- BEGIN SPOKEN LECTURE -->

# Crossing the Line One: Analytic Functions, Zeta, and Character Series

A formula can stop converging even when the function it describes has more to say. That distinction is about to settle a question concerning prime numbers.

For a real number s greater than one, the Riemann zeta function is the sum of the reciprocals of the positive integers raised to the power s. Its series diverges at s equal to one. Dirichlet's L-series, obtained by weighting the summands with a character, can behave differently. For a nonprincipal character, the cancellation among the weights makes the series converge at one. Our next problem concerns a much sharper question: could that convergent L-series have value zero?

It helps to permit s to be complex. The word complex does not mean vague; it means a number with a real part and an imaginary part. Write s as sigma plus i times t. Then n to the power negative s has magnitude n to the power negative sigma, and its argument rotates by negative t times the natural logarithm of n. The real part controls decay. The imaginary part controls oscillation. In particular, absolute convergence of the zeta series still requires sigma greater than one.

We do not intend to learn all of complex analysis before understanding Dirichlet's theorem. We need a small, explicit piece: a way to continue two particular functions, and a way to expand them in power series where their original defining sums no longer converge. Both constructions can be obtained from summation by parts.

## The character series as an integral

Fix a positive modulus q and a nonprincipal character chi modulo q. Let A of x denote the sum of chi of n over positive integers n up to x. The character has period q, and its values sum to zero over a whole period. Therefore A of x is bounded by a constant depending on q, no matter how large x becomes.

This boundedness is stronger than a vague expectation of cancellation. It is a uniform inequality. In partial summation, a uniformly bounded cumulative sum can be multiplied by a steadily decreasing weight without losing control of the tail.

For s with positive real part, apply summation by parts to the sum of chi of n divided by n to the s. The boundary contribution tends to zero, because A of x is bounded and the magnitude of x to the negative s tends to zero. What remains is s times the integral, from one to infinity, of A of x divided by x to the power s plus one.

The integral converges absolutely whenever sigma is positive. Indeed, A of x has bounded magnitude, and the absolute value of the remaining factor is a constant times x to the negative sigma minus one. That comparison has a finite integral for every positive sigma.

So the familiar L-series was not merely an arbitrary sum that happened to converge at s equal to one. Its summation-by-parts integral gives a consistent formula throughout the entire right half of the complex plane, excluding the boundary sigma equal to zero. On real positive s it agrees with the ordinary conditionally convergent series. On complex s it gives the same extension, with no new choices to make.

An example is the alternating character modulo four. Its nonzero values are one on numbers congruent to one and negative one on numbers congruent to three. The cumulative sum never grows without bound. The corresponding L-series at one is one minus one third plus one fifth minus one seventh and so on, a convergent series. The integral construction explains why the same function continues smoothly as the real part of s moves below one, even though its absolute-value series no longer converges there.

## What does analytic mean here?

A function is analytic near a point if it can be represented there by a convergent power series: a constant, plus a multiple of the change in s, plus a multiple of its square, and so forth. A convergent power series does more than imply continuity. It says precisely how small changes propagate, and it lets us speak rigorously about a zero cancelling a pole.

Why should our integral have that property? Suppose the center is a real number c greater than zero, and write s as c plus a small change h. The factor x to the negative s is x to the negative c times the exponential of negative h times log x. Expand the exponential into its ordinary power series. For the coefficient of the kth power of h, the integral contains the kth power of log x, multiplied by x to the negative c minus one.

Every one of these integrals is finite. More importantly, the entire collection of terms can be summed absolutely if the magnitude of h is smaller than c. To see why, replace the series of absolute values by the exponential of the magnitude of h times log x. That is just x to the magnitude of h. The resulting comparison integral has a tail like x to the negative one minus c plus the magnitude of h, which is integrable precisely when the magnitude of h is less than c.

This is a useful, concrete version of analyticity. We are not guessing that a formal series must converge. We have a single integrable majorant that permits us to exchange the expansion and the integral. Thus our continued nonprincipal L-series has a convergent power series around every point of the open right half-plane.

## Zeta's one pole

The zeta series calls for a similar construction, but the cumulative sum of its coefficients is not bounded. The number of positive integers up to x is the floor of x. The important observation is that the floor of x equals x minus its fractional part. The fractional part is always between zero and one.

Partial summation gives zeta of s as s times the integral of the floor of x divided by x to the power s plus one, initially for sigma greater than one. Substitute x minus its fractional part. The part involving x integrates to s divided by s minus one. The remaining integral has the bounded fractional part in its numerator, so it converges absolutely throughout sigma greater than zero.

We have written zeta as one explicit rational term, s divided by s minus one, minus a perfectly well-behaved integral. This expression agrees with the zeta series wherever the series originally converged. Away from s equal to one, it also defines zeta in the larger right half-plane.

What happens at s equal to one? The rational term is one divided by s minus one, plus one. The integral stays finite. Thus zeta has a simple pole at one, with coefficient one in front of the reciprocal of s minus one. There are no other poles in the open right half-plane supplied by this formula.

A pole is a controlled kind of divergence. If we multiply zeta of s by s minus one, the result has a finite limit of one as s approaches one. This precise behavior will let us distinguish between a character L-series that is zero at one and one that is nonzero there.

## Zeros and cancellation

Suppose a nonprincipal character did satisfy L of one comma chi equal to zero. Analyticity would then give a factorization near one: L of s comma chi equals s minus one times another analytic function. The second function may itself vanish at one; that makes no difference. Multiplying by zeta would cancel the lone pole. The product zeta times L would then be analytic at one.

In fact, it would be analytic on the entire region where the real part of s is positive. Zeta has only that one pole there, and the L-series is analytic everywhere in the region. Once the pole is cancelled, the product has no remaining singularity in this half-plane.

This makes an apparently harmless assumption, L of one comma chi equals zero, surprisingly powerful. It would turn a product whose ordinary Dirichlet series is known to converge only to the right of one into a function analytic in a much larger region. For a series with arbitrary positive and negative coefficients, that can happen. For a Dirichlet series with nonnegative coefficients, it creates a severe restriction. We will use that restriction in the real-character proof.

There is a subtle but important distinction here. An analytic continuation does not mean that the original numerical series starts converging at points where it previously diverged. It means we have obtained a new, compatible formula for the function. To get an actual contradiction from nonnegative series coefficients, we will need a separate theorem that links positivity to the region of convergence.

## The exact analytic facts we have earned

We now know four things. First, a nonprincipal character has bounded cumulative sums. Second, its L-series and the integral continuation are analytic throughout the positive-real-part half-plane. Third, zeta has an explicit continuation there, with exactly one simple pole, at one. Fourth, a hypothetical zero of a nonprincipal L-series at one would cancel that pole in the product zeta times L.

Notice what we have not asserted. We have not shown that the L-series is nonzero at one. Nor have we established that zeta is free of zeros on an entire vertical line, which is a different and much deeper problem. What we have done is expose a precise way to test the hypothetical zero.

The next ingredient will come from the Euler products. For complex-valued characters, a carefully chosen combination of those products cannot become too small, while a hypothetical zero at one would force it to become small. For real-valued characters, a positive-coefficient series and a power-series argument will perform the same work.

The point of extending our functions has not been to invent values outside a series's territory. It is to obtain enough structure to turn an arithmetic question, the distribution of primes, into a contradiction that we can actually prove.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Complex-variable setup and continuation

For \(s=\sigma+it\), \(n^{-s}=e^{-s\log n}\) and \(|n^{-s}|=n^{-\sigma}\). Let \(A_\chi(x)=\sum_{n\le x}\chi(n)\). For nonprincipal \(\chi\), \(|A_\chi(x)|\le q\). Partial summation, including the vanishing boundary term for \(\sigma>0\), gives
\[
L(s,\chi)=s\int_1^\infty A_\chi(x)x^{-s-1}\,dx,\qquad \Re s>0.
\]
On a compact subset \(\Re s\ge\delta>0\), the integral and every derivative with respect to \(s\) converge absolutely and uniformly: the kth derivative involves \((\log x)^k x^{-\delta-1}\). Around any real \(c>0\), expanding \(x^{-h}=\sum_{k\ge0}(-h\log x)^k/k!\) is justified when \(|h|<c\), since
\[
\int_1^\infty x^{-c-1}\sum_{k\ge0}\frac{|h\log x|^k}{k!}\,dx
=\int_1^\infty x^{-1-c+|h|}\,dx=\frac1{c-|h|}.
\]

For \(\Re s>1\), \(\zeta(s)=s\int_1^\infty \lfloor x\rfloor x^{-s-1}\,dx\). Since \(\lfloor x\rfloor=x-\{x\}\),
\[
\boxed{\zeta(s)=\frac{s}{s-1}-s\int_1^\infty \{x\}x^{-s-1}\,dx}\qquad (\Re s>0,\ s\ne1).
\]
The bounded fractional part and the comparison above make the integral analytic on \(\Re s>0\). Thus \(\zeta\) has one simple pole there, at \(s=1\), with residue one.

### An explicit power-series route when a zero is assumed

One can avoid invoking a general Cauchy-integral theorem for the later Landau argument. If \(L(1,\chi)=0\), then \(\int_1^\infty A_\chi(x)x^{-2}\,dx=0\) and, for \(s\ne1\),
\[
\frac{L(s,\chi)}{s-1}
= s\int_1^\infty A_\chi(x)x^{-2}\frac{x^{-(s-1)}-1}{s-1}\,dx
=-s\int_1^\infty\!A_\chi(x)x^{-2}\log x\int_0^1 x^{-u(s-1)}du\,dx.
\]
This extends to \(s=1\). On any compact \(\Re s\ge\delta>0\), the integral is absolutely convergent, with uniform comparison by \(x^{-2}\log x\,\max(1,x^{1-\delta})\). Fix real \(c>1\) and \(|h|<c\). Expanding \(x^{-uh}\) is absolutely justified, since for each \(u\in[0,1]\) the majorant is \(x^{-2-u(c-1-|h|)}\log x\), whose exponent is strictly below \(-1\) for \(|h|<c\). Therefore \(L(s)/(s-1)\), \(L(s)\), and the fractional-part integral have convergent Taylor expansions on \(|s-c|<c\), and so does
\[
F(s)=\zeta(s)L(s,\chi)=s\frac{L(s,\chi)}{s-1}-s\left(\int_1^\infty\{x\}x^{-s-1}dx\right)L(s,\chi).
\]
This is the exact disk-expansion property required later, established directly from integrals. The complementary standard complex-analysis formulation is that a function holomorphic on \(\Re s>0\) has Taylor radius at least \(c\) when centered at the real point \(c>0\).

### Exercises

1. Prove that the partial sum of a nonprincipal character is at most \(q\) in absolute value. Why does this fail for the principal character?
2. Derive \(L(s,\chi)=s\int A_\chi(x)x^{-s-1}dx\) by writing down the finite summation-by-parts identity first.
3. Show directly that \(\int_1^\infty (\log x)^k x^{-\delta-1}dx=k!/\delta^{k+1}\) for every positive \(\delta\).
4. Why is the formula for \(\zeta(s)\) meromorphic rather than analytic at one? Compute \(\lim_{s\to1}(s-1)\zeta(s)\).
5. Show, using the integral identity above, that \(F(s)=\zeta(s)L(s,\chi)\) has a convergent Taylor expansion around any real \(c>1\) with radius at least \(c\), assuming \(L(1,\chi)=0\).

### Sources and further reading

- University of New Mexico, *Complex Analysis* lecture notes, section 9.3, [meromorphic continuation of zeta](https://math.unm.edu/~lorenz/562/h.pdf).
- Kiran Kedlaya, [Dirichlet characters and L-functions](https://kskedlaya.org/ant/chap-lfunc.html), for the analytic framework used in proofs of nonvanishing.
- Wikipedia: [Analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation), [Dirichlet series](https://en.wikipedia.org/wiki/Dirichlet_series), [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function).
