# 020000 — Complex Characters and the Positive Euler-Product Inequality

**Track:** Number Theory from First Principles. **Background:** character orthogonality, Euler products, logarithmic series, and analytic continuation of L-series at one. **Aim:** prove \(L(1,\chi)\ne0\) for every nonreal Dirichlet character without importing the corresponding theorem as a black box.

<!-- BEGIN SPOKEN LECTURE -->

# Complex Characters and the Positive Euler-Product Inequality

Consider a number that is not zero but is becoming very small. We might try to prove that it cannot reach zero by showing it is at least some fixed positive distance from zero. For an ordinary positive number, a lower bound is easy to visualize. For a complex number, the appropriate measure is its magnitude, its distance from the origin of the complex plane.

We face such a problem with Dirichlet L-series. For every nonprincipal character chi, the value L of one comma chi exists. We need to show that it is not zero. This lecture proves the claim when chi takes genuinely complex values. By the end we will know exactly why real-valued characters require a different proof.

## The first attempt

For real s greater than one, the Euler product tells us that the logarithm of L of s comma chi is a sum over primes and their powers. At a given prime p and exponent k, the contribution is chi of p to the kth power divided by k times p to the power k s.

If chi takes the complex value cos theta plus i times sin theta at a prime, its kth power has real part cos of k theta. The logarithm of the magnitude of L therefore collects cosines. Those cosines may be negative, so there is no immediate reason for the whole logarithm to stay above zero.

What if we multiply L by zeta? Taking logarithms adds one to every cosine coefficient. One plus cos of any real angle is nonnegative. Thus the magnitude of zeta times L is at least one for real s greater than one.

This is promising. Unfortunately, it is not sufficient. Zeta has a simple pole at one. If L had a simple zero there, zeta times L could tend to a positive nonzero number. The lower bound would not be contradicted. We need an expression that would be forced to zero by a hypothetical zero of L, despite the pole of zeta.

Try giving L two copies instead of one. The extra zero would defeat the single pole. But the cosine coefficient would become one plus twice cos theta, and that is negative when the cosine is close to minus one. Our attempt to strengthen the vanishing creates a sign problem in the Euler product.

The trick is to build a square from the cosines. It is a small piece of algebra with a surprisingly large consequence.

## A combination that cannot be small

For the moment, suppose chi is a nonreal character. That means there is at least one unit residue for which its value is neither one nor negative one. The square of chi, meaning the character obtained by squaring each value, is then nonprincipal. If the square were principal, every nonzero character value would be a square root of one, so chi would in fact be real-valued.

Consider this product for real s greater than one: zeta of s cubed, times L of s comma chi to the fourth power, times L of s comma chi squared, meaning the L-series of the squared character. Call the entire product F of s.

The powers three, four, and one are chosen for a precise reason. Expand the logarithm of the Euler products. At a prime that does not divide the modulus, and at its kth power, the real part of the combined numerator is three plus four times cos of k theta plus cos of twice k theta.

Recall the double-angle identity: cos of twice an angle equals twice the square of its cosine minus one. Substitute this into our numerator. Three minus one becomes two, and we have two plus four cosine plus two cosine squared. Factor out two. What remains is the square of one plus cosine.

So the combined numerator is twice the square of one plus cos of k theta. A square of a real number is never negative. Every prime-power contribution to the real part of log F is therefore nonnegative.

At primes dividing the modulus, chi of p is zero, as is the square of chi of p. Only the three zeta copies remain. Their logarithmic contribution is positive as well. Thus there is no exception hiding at the bad primes.

Because the Euler logarithm series is absolutely convergent when s is greater than one, these observations are legitimate term by term. Their sum is nonnegative. Exponentiating gives a clean inequality: the magnitude of F of s is at least one, for every real s greater than one.

That is the lower bound we wanted. It is not an asymptotic guess and not the result of sampling some primes. It comes from the exact identity involving a squared cosine, applied to every prime and every positive exponent.

## Now assume a zero

Suppose, for contradiction, that our nonreal character satisfies L of one comma chi equal to zero. The preceding analytic construction tells us that L is analytic at one. Hence its zero has at least one factor of s minus one. In particular, as real s approaches one from above, the magnitude of L of s comma chi is bounded by a constant times s minus one.

The zeta function has a simple pole at one. Its cube therefore grows at most like a constant times one over the cube of s minus one. Raising L to its fourth power gives at least four factors of s minus one in the numerator. Multiply: four factors of vanishing against three factors of divergence leave one factor of s minus one. That tends to zero.

What about the final factor, the L-series of chi squared? That is where the nonreal assumption enters. Chi squared is nonprincipal, so its L-series is analytic and finite at one. We do not need to know whether its value is zero or nonzero. Boundedness is enough.

Consequently the magnitude of F must tend to zero as s approaches one from above. But we proved that the magnitude of F is at least one for every such s. A quantity bounded below by one cannot tend to zero. The contradiction rules out our hypothetical zero.

We have proved: if chi is a nonreal Dirichlet character, then L of one comma chi is nonzero. No general prime-distribution theorem was used in this argument. Its central inputs were an Euler product, a simple pole, an analytic character series, and the nonnegative trigonometric identity.

## A concrete character modulo five

The units modulo five are one, two, three, and four. Two generates them: its successive powers modulo five are two, four, three, and then one again. Define a character by sending two to the imaginary unit i. Its values on the four units are therefore one, i, negative one, and negative i, in that power order.

This is a genuinely complex character. Its square sends two to negative one, sends four to one, sends three to negative one, and sends one to one. The squared character is nonprincipal. Both characters have value zero on multiples of five.

At a prime whose character value is i, consider the first prime-power logarithm term. Its angle has cosine zero. Our combined numerator is three plus zero plus cosine pi, which equals two. At a prime whose value is negative one, the angle is pi. The numerator is three minus four plus one, which equals zero. At a prime whose value is one, the numerator is eight. All three examples agree with the formula twice one plus cosine squared.

The numerical illustrations are not the proof; they show what the general identity is controlling. Every power of every root of unity works in exactly the same way.

## Why the real case survives

A real nonprincipal character takes only the values zero, one, and negative one. Squaring it gives the principal character of the same modulus. The squared-character L-series therefore carries a pole at one, not a bounded value.

Return to our product. If L of s comma chi had a simple zero, its fourth power would contribute four vanishing factors. But zeta cubed contributes three poles, and L of chi squared contributes one more pole. Four zeros could cancel four poles, leaving a nonzero limit. Our lower bound of one would no longer contradict that possibility.

The formula did not suddenly become false for real characters. The issue is the accounting of poles and zeros. A proof may give a true inequality and still fail to establish the particular conclusion one wants.

For real characters, another feature becomes available instead. Their values are real, and we can combine their coefficients with the positive coefficients of zeta. The resulting Dirichlet series will have nonnegative coefficients and, on perfect-square indices, coefficients at least one. Those properties will be too strong to reconcile with a hypothetical zero.

We will exploit that feature using a positivity principle for Dirichlet series. This is not merely a second trick. It illustrates a structural distinction: an analytic continuation can sometimes make a series look harmless past its convergence boundary, but a series with nonnegative coefficients cannot hide divergence through cancellation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Statement and square-completion proof

Let \(q\ge2\) and let \(\chi\) be a nonreal Dirichlet character modulo \(q\). Then \(\chi^2\ne\chi_0\), and
\[
\boxed{L(1,\chi)\ne0.}
\]
For \(s>1\), let
\[
F(s)=\zeta(s)^3L(s,\chi)^4L(s,\chi^2).
\]
Absolute convergence of each Euler logarithm and \(\log|e^z|=\Re z\) give
\[
\log|F(s)|=\sum_p\sum_{k\ge1}\frac{3+4\Re(\chi(p)^k)+\Re(\chi(p)^{2k})}{k p^{ks}}.
\]
If \(p\mid q\), the numerator is 3. Otherwise set \(\chi(p)=e^{i\theta_p}\); then the numerator equals
\[
3+4\cos(k\theta_p)+\cos(2k\theta_p)
=2\bigl(1+\cos(k\theta_p)\bigr)^2\ge0.
\]
Therefore \(|F(s)|\ge1\) for \(s>1\). If \(L(1,\chi)=0\), analyticity on \(\Re s>0\) implies \(L(s,\chi)=O(s-1)\) as real \(s\downarrow1\). Also \(\zeta(s)=O((s-1)^{-1})\) and \(L(s,\chi^2)=O(1)\) because \(\chi^2\) is nonprincipal. Thus \(F(s)=O(s-1)\to0\), contradiction.

This argument proves nonvanishing for all nonreal characters without assuming nonvanishing of \(L(1,\chi^2)\). Replacing \(\zeta\) with \(L(s,\chi_0)\) would also work for nonreal characters, but the above zeta product keeps the pole bookkeeping explicit.

### Modulo-five example

Let \(2\) generate \((\mathbb Z/5\mathbb Z)^\times\) and choose \(\chi(2)=i\). Then
\[
\chi(1)=1,\quad \chi(2)=i,\quad \chi(4)=-1,\quad \chi(3)=-i,
\]
with \(\chi(n)=0\) for \(5\mid n\). The square \(\chi^2\) is the nonprincipal quadratic character modulo five. For an angle \(0,\pi/2,\pi\), the positive trigonometric numerator is respectively 8, 2, and 0.

### Why this is not a proof for real characters

If \(\chi\ne\chi_0\) is real, then \(\chi^2=\chi_0\), and \(L(s,\chi^2)\) has a simple pole at one. Under a hypothetical simple zero of \(L(s,\chi)\), the product above need not tend to zero: its nominal zero order is four and its nominal pole order is also four. A separate argument is required.

### Exercises

1. Prove that \(\chi^2=\chi_0\) for a nonprincipal character if and only if \(\chi\) is real-valued.
2. Check explicitly why the inequality \(1+\cos\theta\ge0\) only proves \(|\zeta(s)L(s,\chi)|\ge1\), which is insufficient at the pole.
3. Expand \(3+4t+(2t^2-1)\) and factor it for real \(-1\le t\le1\).
4. For the character modulo five, list the values of \(\chi(p)^2\) on each unit residue. What would fail if this squared character were principal?
5. Explain where absolute convergence is required in taking the logarithm of the Euler product.

### Sources and further reading

- Reed College lecture notes, [Nonvanishing of Dirichlet L-functions at \(s=1\)](https://people.reed.edu/~jerry/361/lectures/lfnv.pdf), sections 1–2, for the classical three-four-one positivity argument.
- Manuel Eberl, [Dirichlet L-functions and Dirichlet's theorem](https://isa-afp.org/entries/Dirichlet_L.html), formal proof development.
- Mathlib, [NumberTheory.LSeries.Nonvanishing](https://leanprover.github.io/hex/docs/Mathlib/NumberTheory/LSeries/Nonvanishing.html), theorem and proof outline.
- Wikipedia: [Dirichlet character](https://en.wikipedia.org/wiki/Dirichlet_character), [Euler product](https://en.wikipedia.org/wiki/Euler_product), [Dirichlet L-function](https://en.wikipedia.org/wiki/Dirichlet_L-function).
