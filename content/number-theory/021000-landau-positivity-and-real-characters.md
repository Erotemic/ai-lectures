# 021000 — Landau's Positivity Principle and the Real-Character Case

**Track:** Number Theory from First Principles. **Background:** Dirichlet convolution, character series, analytic continuation by integrals, and power-series expansions. **Aim:** prove a positive-coefficient continuation lemma and use it to prove \(L(1,\chi)>0\) for every real nonprincipal Dirichlet character.

<!-- BEGIN SPOKEN LECTURE -->

# Landau's Positivity Principle and the Real-Character Case

The final obstacle to Dirichlet's theorem is a function that might be zero. We have proved that a genuinely complex Dirichlet character cannot have L of one comma chi equal to zero. But real characters, whose values are zero, one, and negative one, escaped that argument.

To finish the proof, we will take a different perspective. Rather than control the magnitude of a complex Euler product, we will inspect the coefficients of an ordinary Dirichlet series. There is a decisive distinction between a series whose terms can cancel and a series whose terms are all nonnegative. Cancellation can disguise divergence. Positivity cannot.

The key analytic idea is often called Landau's theorem for Dirichlet series with nonnegative coefficients. We only need a special case, and we can prove precisely that case. It is worth examining the argument carefully: the same reasoning reappears in many areas where generating functions encode counts of objects.

## Building a nonnegative series

Let chi be a real, nonprincipal Dirichlet character modulo q. Real characters take only the values zero, one, and negative one. Form the product of zeta of s and L of s comma chi, initially for real s greater than one. Both series converge absolutely here, so multiplying them and regrouping by the product of their indices is justified.

The coefficient of one over n to the s in the product is the sum of chi of d over all positive divisors d of n. Call this coefficient a of n. In the language of arithmetic functions, a is the Dirichlet convolution of the constant-one function and chi.

A convolution of two multiplicative functions is multiplicative. Thus we can understand every coefficient by examining prime powers. Take p to the kth power. Its positive divisors are one, p, p squared, through p to the kth power. Consequently a of p to the kth power is one plus chi of p plus chi of p squared, and so on.

Because a Dirichlet character is completely multiplicative, every power of chi of p is just an ordinary power of one of three numbers: zero, one, or negative one.

If chi of p is one, then all k plus one terms equal one, and a of p to the kth power is k plus one. If chi of p is negative one, the terms alternate between one and negative one. The sum is zero when k is odd, and one when k is even. If chi of p is zero, every term after the initial one vanishes, and the sum is one.

There are no negative answers in any case. By multiplicativity, every coefficient a of n is nonnegative. This is the first half of our crucial observation.

The second half concerns perfect squares. In the prime factorization of a perfect square, every exponent is even. In all three cases just examined, a of p to an even power is at least one. Therefore a of m squared is at least one for every positive integer m.

We have not merely proved that the new Dirichlet series has positive terms somewhere. We have found a dense, familiar family of indices, the perfect squares, at which its coefficients are guaranteed to be at least one. Later, those indices will produce an entire harmonic series inside a larger sum.

## What analytic continuation can and cannot do

Recall the hypothetical zero we want to rule out: suppose L of one comma chi equals zero. The zeta function has a simple pole at one, and the L-series is analytic there. A zero of L cancels zeta's pole, so their product, which we are calling F, becomes analytic throughout the half-plane where the real part of s is positive.

An analytic function has a convergent power series around points in its domain. In particular, the function F would have a Taylor expansion centered at the real number two that converges at the real number one half. The radius from two to the boundary of the positive half-plane is two, and one half lies strictly inside that disk.

The preceding analytic-continuation construction made this particular expansion explicit. Both zeta and the nonprincipal L-series were represented by integrals with bounded numerators. Under the assumption that L vanishes at one, a subtraction removes the pole and those integrals give a power-series expansion throughout the disk centered at two with radius two. We need no claim that the original Dirichlet series already converges at one half.

That distinction matters. The function may be analytic at one half while its original coefficient series diverges there. For example, the alternating series one minus one plus one minus one does not converge in the ordinary sense, although a related generating function has values elsewhere. The power-series argument we are about to use will show why such a mismatch cannot happen in the same way when all the coefficients are nonnegative.

## Landau's argument in one disk

We know F of s equals the sum of a of n divided by n to the s whenever s is greater than one. Fix the center s equal to two. Differentiate this Dirichlet series once. Each term acquires a factor of negative log n. Differentiate it twice, and it acquires the square of log n, with a positive sign. After k derivatives, the factor is negative log n raised to the kth power.

These derivative series converge absolutely at two. The coefficients are nonnegative and bounded by the number of divisors of n, while any fixed power of log n grows much more slowly than a small positive power of n. Thus termwise differentiation is legitimate near two.

Now evaluate the Taylor series at one half. The change from the center two to one half is negative three halves. The kth derivative contributes a factor of negative log n raised to the kth power. The kth power of the negative change supplies another negative sign to the same power. The signs cancel. Every term in the resulting double sum is nonnegative.

For each fixed n, the sum over k is the exponential series for three halves times log n. That exponential equals n raised to three halves. Combining it with the original denominator n squared gives one over the square root of n.

Therefore the Taylor expansion, if it converges at one half, would equal the sum of a of n divided by the square root of n. There is no rearrangement problem here. Both levels of summation have nonnegative terms. We can exchange their order, or regard the sum as an increasing limit of finite rectangles, without invoking cancellation.

The Taylor series is convergent because our assumed cancellation of the zeta pole made F analytic on the required disk. Its value at one half is finite. So the nonnegative sum of a of n divided by the square root of n would have to be finite as well.

But examine just the perfect-square indices n equal to m squared. Their contribution is a of m squared divided by m. Each coefficient is at least one. Hence the full sum is at least one plus one half plus one third plus one fourth, and so on. The harmonic series diverges.

We have reached a contradiction: the same sum would have to be finite by the Taylor expansion and infinite by the perfect-square lower bound.

Therefore our assumption was false. For every real, nonprincipal Dirichlet character, L of one comma chi is not zero.

## Why the answer is actually positive

We can sharpen nonzero to strictly positive. For real s greater than one, the Euler factor at a prime is one divided by one minus chi of p over p to the s. Chi of p is zero, one, or negative one. In all three cases the denominator is positive. Thus every Euler factor is positive, and the absolutely convergent Euler product itself is positive.

As s approaches one from above, L of s comma chi converges to the real value L of one comma chi. The limit of positive numbers cannot be negative. We have just proved it cannot be zero. Therefore it must be strictly positive.

For a simple example, the real nonprincipal character modulo four produces the alternating reciprocal series one minus one third plus one fifth minus one seventh and so on. Its limit is positive; that was already visible by grouping pairs. The argument we have given now works even when no such convenient pairwise grouping appears.

## The completed nonvanishing theorem

Combine the two cases. A nonprincipal character is either genuinely complex-valued or real-valued. For a genuinely complex character, the positive trigonometric Euler product ruled out a zero. For a real character, the positive-coefficient Dirichlet series and its perfect-square terms ruled out a zero.

We have therefore proved the full statement needed for Dirichlet's theorem: for every nonprincipal Dirichlet character modulo every positive modulus, L of one comma chi is not zero. Real nonprincipal characters, in fact, have a strictly positive value.

Consider how the proof is divided. The character's multiplicative structure created the L-series. Summation by parts gave analytic continuation. For complex characters, a sum of logarithms became a square of a cosine expression. For real characters, a product of series became a sum with nonnegative coefficients. The analytic step was not a decorative layer added to number theory; it was the mechanism that made the arithmetic information contradictory under the zero assumption.

There is one more important limitation. This establishes nonvanishing at the single point s equal to one. It does not establish nonvanishing at every point on the entire vertical line where the real part is one, and it does not prove the prime number theorem. Those questions need further work.

But it removes the exact obstacle in the progression argument. The remaining step is to return to character orthogonality, combine the prime sums, and watch the one principal character force a divergence in every reduced residue class.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Nonnegative Dirichlet coefficients

Let \(\chi\ne\chi_0\) be a real Dirichlet character modulo \(q\). For \(\Re s>1\), absolute convergence gives
\[
F(s)=\zeta(s)L(s,\chi)=\sum_{n\ge1}\frac{a(n)}{n^s},\qquad a(n)=\sum_{d\mid n}\chi(d)=(\mathbf1*\chi)(n).
\]
Because \(a\) is multiplicative,
\[
a(p^k)=\begin{cases}
k+1&\chi(p)=1,\\
1&\chi(p)=0,\\
1&\chi(p)=-1\text{ and }k\text{ even},\\
0&\chi(p)=-1\text{ and }k\text{ odd}.
\end{cases}
\]
Hence \(a(n)\ge0\) for all \(n\), and \(a(m^2)\ge1\) for every \(m\ge1\). Also \(a(n)\le d(n)\), so \(\sum a(n)n^{-\sigma}\le\zeta(\sigma)^2\) for \(\sigma>1\).

### The needed Landau lemma, proved

**Lemma (disk form sufficient here).** Let \(F(s)=\sum_{n\ge1}a(n)n^{-s}\) for \(\Re s>1\), with \(a(n)\ge0\). Suppose \(F\) admits a Taylor expansion about \(c=2\) that converges at \(s=\frac12\). Then \(\sum_{n\ge1}a(n)n^{-1/2}\) converges and equals \(F(\frac12)\).

**Proof.** For each \(k\ge0\), absolute convergence near \(2\) gives
\[
F^{(k)}(2)=\sum_{n\ge1}a(n)(-\log n)^k n^{-2}.
\]
The Taylor series at \(\frac12=2-\frac32\) is
\[
\begin{aligned}
F(\tfrac12)&=\sum_{k\ge0}\frac{(-\frac32)^k}{k!}F^{(k)}(2)
=\sum_{k\ge0}\sum_{n\ge1}\frac{a(n)}{n^2}\frac{(\frac32\log n)^k}{k!}\\
&=\sum_{n\ge1}\frac{a(n)}{n^2}\exp(\tfrac32\log n)
=\sum_{n\ge1}\frac{a(n)}{\sqrt n}.
\end{aligned}
\]
The swap is justified by Tonelli's theorem for nonnegative series, or directly by monotone convergence of finite rectangular partial sums. All sums equal the finite Taylor value. \(\square\)

**Application.** Suppose \(L(1,\chi)=0\). By the explicit integral continuation and pole cancellation in lecture 019000, \(F(s)=\zeta(s)L(s,\chi)\) has a convergent Taylor series on \(|s-2|<2\), which contains \(\frac12\). The lemma would give
\[
F(\tfrac12)=\sum_{n\ge1}\frac{a(n)}{\sqrt n}\ge\sum_{m\ge1}\frac{a(m^2)}m\ge\sum_{m\ge1}\frac1m=\infty,
\]
a contradiction. Thus \(L(1,\chi)\ne0\). The positive Euler factors for \(s>1\) and continuity imply \(\boxed{L(1,\chi)>0}\).

The general Landau theorem asserts that the real abscissa of convergence of any Dirichlet series with nonnegative coefficients is a singular point of its analytic sum. The disk lemma above is the exact statement used here and is proved in full; no unproved global Landau theorem is needed.

### Examples and exercises

1. For the character modulo four, compute \(a(3),a(9),a(5),a(25),a(45)\).
2. Give a real nonprincipal character modulo eight. Check that its prime-power coefficient formulas still give \(a(m^2)\ge1\).
3. Explain why every term in the double Taylor series in the lemma is nonnegative even though its derivatives alternate in sign.
4. Replace the evaluation point \(\frac12\) by \(\sigma\in(0,1)\). Show that if the required disk expansion is available, the same argument forces \(\sum a(n)n^{-\sigma}<\infty\). Identify the value \(\sigma\) at which the squares alone give the easiest contradiction.
5. Where does the proof use the character being real? Where does it use the character being nonprincipal?

### Sources and further reading

- Reed College, [Nonvanishing of Dirichlet L-functions at \(s=1\)](https://people.reed.edu/~jerry/361/lectures/lfnv.pdf), sections 2–3 (real characters and Landau lemma).
- Kiran Kedlaya, [Dirichlet characters and L-functions](https://kskedlaya.org/ant/chap-lfunc.html), nonvanishing proofs.
- University College London, [Introduction to Analytic Number Theory](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf), Landau's lemma and the progression theorem.
- Wikipedia: [Dirichlet series](https://en.wikipedia.org/wiki/Dirichlet_series), [Dirichlet L-function](https://en.wikipedia.org/wiki/Dirichlet_L-function), [Analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation).
