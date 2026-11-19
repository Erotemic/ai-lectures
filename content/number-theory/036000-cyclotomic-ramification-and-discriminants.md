# 036000 — Roots of Unity, Ramification, and Cyclotomic Discriminants

**Track:** Number Theory from First Principles. **Background:** 014000 (roots of unity and finite fields), 025000–025500 (finite-field construction), 032000 (Eisenstein and totally ramified extensions), 035000–035750 (different and discriminant). **Aim:** prove the integral-basis and discriminant formula for prime-power cyclotomic fields and distinguish tame from wild cyclotomic ramification.

<!-- BEGIN SPOKEN LECTURE -->

# Roots of Unity, Ramification, and Cyclotomic Discriminants

The primitive fifth roots of unity are five points equally spaced around the complex unit circle. Adjoin one of them to the rational numbers and you get a number field of degree four. There is only one rational prime that ramifies in that field: five. Its discriminant is five cubed.

Now replace the fifth root by a ninth root of unity. The degree becomes six, the only ramified prime is three, and the absolute discriminant is three to the ninth power. The exponent nine is much larger than the tame baseline of five. The reason is that this extension is wildly ramified at three.

Roots of unity provide a setting where we can derive both phenomena explicitly. We can see the integral basis, the ramified prime, the different, and the discriminant in one coherent calculation. That will also show why the polynomial derivative formula is powerful only after the correct integer ring has been justified.

## The polynomial of a prime-power root of unity

Fix a prime p and a positive integer r. Let zeta be a primitive p-to-the-r-th root of unity. Its cyclotomic polynomial is the quotient of X to the p-to-the-r minus one by X to the p-to-the-r-minus-one minus one. It is also the sum of the p monomials whose exponents are zero, p-to-the-r-minus-one, twice that number, up to p minus one times that number.

The degree is phi of p-to-the-r, namely p-to-the-r-minus-one times p minus one. Call that number n. Cyclotomic irreducibility was already motivated by the theory of roots of unity; for this prime-power polynomial, we can prove irreducibility directly using Eisenstein.

Shift the variable by one. Work modulo p. In characteristic p, X to the p-to-the-r minus one is X minus one raised to the p-to-the-r. Similarly, the denominator is X minus one raised to the p-to-the-r-minus-one. So our polynomial reduces modulo p to X minus one raised to n. After shifting X to X plus one, every nonleading coefficient is divisible by p. Meanwhile, substituting one into the original polynomial gives p, because the polynomial is a sum of p ones. Thus the constant term of the shifted polynomial is p, not divisible by p squared.

Those are exactly the Eisenstein conditions. Therefore the shifted polynomial is irreducible over the rationals, and it also defines a totally ramified extension at p. The element pi equal to zeta minus one is a local uniformizer. The degree is n, the residue field is still the p-element field, and the ideal p is the n-th power of the unique local prime up to a unit.

This tells us where the ramification occurs locally. But it is not yet enough to assert that the full global integer ring is Z of zeta. A polynomial can be irreducible and Eisenstein at one prime while failing to give an integral basis at another prime. We need to rule out that possibility.

## Establishing the full ring of integers

Let R be Z of zeta. It is an order inside the full integer ring O of the cyclotomic field. The index of R in O is finite, and the discriminant of R is the square of this index times the field discriminant. Any rational prime dividing the index must therefore divide the discriminant of the power basis in R.

We will soon compute that power-basis discriminant and find that it is a pure power of p. Therefore no prime other than p can divide the index. At p, the Eisenstein calculation does more than give irreducibility. The local ring Z-p of zeta is a complete discrete valuation ring: pi is its uniformizer, and the extension is totally ramified of degree n. It is already the full local integer ring. So p cannot divide the global index either.

Every possible prime divisor of the index has been excluded. Hence the index is one and the full ring of integers is Z of zeta. This argument closes the logical gap that sometimes appears in a quick treatment of cyclotomic fields: one must prove maximality, not infer it simply from having a convenient polynomial.

There is a small ordering issue in that proof. We have invoked the power-basis discriminant before calculating it, but we can calculate it from the roots of the polynomial without assuming that R is maximal. We do so now, then return to the index argument with an explicit result.

## Differentiate the cyclotomic equation

Write F of X for the quotient defining the cyclotomic polynomial. At zeta, the numerator X to p-to-the-r minus one vanishes, and the denominator does not, since zeta has exact order p-to-the-r. Differentiate the quotient. The term involving the derivative of the denominator vanishes at zeta because it is multiplied by the numerator. The surviving term is p to the r, times zeta to the p-to-the-r minus one, divided by zeta to the p-to-the-r-minus-one minus one.

That is F prime of zeta. Its numerator contains a rational factor p to the r and a root of unity, whose norm has absolute value one. The denominator is a difference between one and a primitive p-th root of unity. We know that the norm of one minus a primitive p-th root from the p-th cyclotomic field to the rationals is p: multiply one minus all its conjugates, or simply evaluate the p-th cyclotomic polynomial at one.

There is a tower here. The p-th root belongs to our larger p-to-the-r field, and the larger field has degree p-to-the-r-minus-one over the p-th cyclotomic field. Consequently the absolute norm of the denominator in our larger field is p raised to the p-to-the-r-minus-one.

The absolute norm of the numerator is p raised to r times n. Divide the two norms. The absolute norm of F prime of zeta is p raised to r n minus p-to-the-r-minus-one.

By the discriminant formula for a power basis, which follows either from the squared Vandermonde determinant or from the norm of the derivative, this is the absolute discriminant of the order R. Only p divides it. That justifies the index argument we started. Thus R equals the full integer ring, and our computed power-basis discriminant really is the field discriminant.

We have a complete formula: the absolute discriminant of the p-to-the-r cyclotomic field is p raised to p-to-the-r-minus-one times the quantity r times p minus r minus one. Its sign is determined by the embedding signature. When the order is greater than two, all embeddings are complex, so the sign is negative one raised to half the degree. For the exceptional case of order two, the field is just the rationals and the discriminant is one.

## Three revealing examples

Take p equal to five and r equal to one. The degree is four. The exponent of five in the discriminant is one times four minus one, which is three. So the discriminant is positive five cubed. The extension is totally ramified of index four at five, and five does not divide four. It is tame. The different exponent is e minus one, which is three, exactly as expected.

Take p equal to three and r equal to two. We are adjoining a primitive ninth root of unity. The degree is six. The exponent of three in the discriminant is two times six minus three, equal to nine. The discriminant is negative three to the ninth, because the three conjugate pairs give a negative sign. The ramification index is six, and three divides six. The extension is wild. The tame baseline would be five, but the actual different exponent is nine.

Finally take p equal to two and r equal to three. This is the field with a primitive eighth root of unity from our earlier tower example. The degree is four. The exponent of two is three times four minus four, equal to eight. The discriminant is positive two to the eighth, or two hundred fifty-six. This independently confirms the two-stage calculation through the Gaussian integers.

The pattern also explains why prime-power cyclotomic fields are natural laboratories for ramification. At the first layer with odd p, the ramification index is p minus one, prime to p, so the extension is tame. At higher p-power layers, p divides the ramification index and the extension is wild. At p equal to two, the first nontrivial layer already has index divisible by two.

## What this calculation prepares us to ask

We can now calculate an exact discriminant in a family whose degrees grow without bound. But there is a deeper structure behind the exponent. The field is Galois over the rationals, with automorphisms sending zeta to its powers. Some automorphisms move the local uniformizer zeta minus one by a large p-adic amount; others move it by a smaller amount. The higher ramification groups organize those motions by valuation. Summing their contributions recovers the different exponent, including the wild excess above e minus one.

We have not proved that higher-ramification-group formula here. We do not need it for the cyclotomic discriminant computation: the derivative and the norm already gave an exact answer. But the answer tells us what the future theory must explain. Why does the exponent of the different grow by a particular amount at each new p-power layer? What governs the jumps between successive groups? How does this connect to conductors, local class field theory, and the arithmetic of characters?

Our calculation also has a clear limitation. We worked with prime-power roots of unity. For roots of unity of general composite order, several rational primes can ramify, and one must combine prime-power fields carefully. The general cyclotomic discriminant formula is a natural extension, but the field compositum and integral-basis arguments deserve their own treatment rather than being hidden behind a product sign.

For now, we have reached a satisfying endpoint to the first course of different and discriminant theory. A trace pairing measured the failure of integral self-duality. Its inverse fractional ideal was the different. A polynomial derivative computed that ideal whenever our generator gave the full ring of integers. Norms and tower formulas carried the information back to discriminants. And cyclotomic fields showed the entire mechanism operating in an infinite, explicitly calculable family. The next step is to understand the higher ramification groups that account for the wild part of those exponents, and later to connect discriminants to conductors and global field invariants.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `m=p^r`, `r>=1`, `n=phi(p^r)=p^(r-1)(p-1)`, `K=Q(zeta_m)`, and `F=Phi_m`.

\[
F(X)=\frac{X^{p^r}-1}{X^{p^{r-1}}-1}
=\sum_{j=0}^{p-1}X^{jp^{r-1}},\quad
F(X+1)\text{ is Eisenstein at }p.
\]

Therefore `pi=zeta_m-1` is a local uniformizer at the unique prime above `p`, and `e=n, f=1`. The derivative is
\[
F'(\zeta_m)=\frac{p^r\zeta_m^{p^r-1}}{\zeta_m^{p^{r-1}}-1}.
\]

Since `N_{Q(zeta_p)/Q}(1-zeta_p)=p` and `[K:Q(zeta_p)]=p^(r-1)`, we get
\[
|N_{K/Q}(F'(\zeta_m))|=p^{rn-p^{r-1}}.
\]

`Z[zeta_m]` is maximal at `p` by Eisenstein and at every other prime by the power-basis discriminant; hence
\[
\boxed{\ O_K=\mathbf Z[\zeta_m],\quad
|\Delta_K|=p^{p^{r-1}(rp-r-1)}\ }.
\]

For `m>2`, the sign is `(-1)^(n/2)`. For `m=2`, `K=Q`, `Delta=1`.

| `m` | Degree | Signed discriminant | Ramification type at `p` |
|---|---:|---:|---|
| `5` | 4 | `+5^3` | tame, `e=4,d=3` |
| `9` | 6 | `-3^9` | wild, `e=6,d=9` |
| `4` | 2 | `-2^2` | wild, `e=2,d=2` |
| `8` | 4 | `+2^8` | wild, `e=4,d=8` |

### Exercises

1. Prove `Phi_{p^r}(X+1)` is Eisenstein and identify exactly where the constant-term condition is used.
2. Derive the derivative identity at zeta from the quotient rule, without cancelling a zero denominator.
3. Compute the absolute discriminants of the cyclotomic fields of orders 7, 16, and 25.
4. Explain carefully why maximality at p and discriminant support at p prove `O_K=Z[zeta]` globally.
5. Compare the different exponent with `e-1` for the ninth, eighth, and sixteenth cyclotomic fields.

## Sources and reading

- Andrew V. Sutherland, *18.785 Number Theory I*, Lecture 12, and Lecture 11 (totally ramified extensions): https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec12.pdf
- Stanford Pairing-Based Cryptography Notes, *Cyclotomic Fields*: https://crypto.stanford.edu/pbc/notes/numberfield/cyclo.html
- Wikipedia: [Cyclotomic field](https://en.wikipedia.org/wiki/Cyclotomic_field), [Cyclotomic polynomial](https://en.wikipedia.org/wiki/Cyclotomic_polynomial), [Different ideal](https://en.wikipedia.org/wiki/Different_ideal).

**Proof scope:** Proves the integral ring, full discriminant formula, and prime-power ramification via Eisenstein, index squares and derivative norms. Uses the separability/trace-discriminant formula proved earlier; does not claim a full conductor or higher ramification-group theorem, nor the general composite-order cyclotomic discriminant formula.
