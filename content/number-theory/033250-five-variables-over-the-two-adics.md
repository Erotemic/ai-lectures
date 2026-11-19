# 033250 — Five Variables at the Prime Two

**Track:** Number Theory from First Principles. **Background:** 031000 (Hensel lifting), 031250 (two-adic squares), 032500 (the Hilbert symbol at two), 032750 (local quadratic forms). **Aim:** prove, rather than cite, that every nondegenerate quadratic form of dimension at least five over Q-two is isotropic, and exhibit an anisotropic form of dimension four.

<!-- BEGIN SPOKEN LECTURE -->

# Five Variables at the Prime Two

We ended the previous study of local quadratic forms at a conspicuous gap. At every odd prime, five variables force a nonzero zero. The proof reduced three unit coefficients modulo the prime, found a nonsingular solution in a finite field, and lifted it. At the prime two, the derivative of a square is always even. That argument does not survive. But the conclusion does: every quadratic form in five or more variables over Q-two has a nontrivial zero.

Today we will prove that assertion without quoting a classification theorem. We will need only the square classes we have already studied, a calculation modulo eight, and the strengthened form of Hensel's lemma. The arithmetic is small enough to follow case by case, but the reason the cases work is structural. A quadratic form can hide obstruction in four coordinates; a fifth gives enough freedom to cancel it.

## First reduce the coefficients

Let our form have five variables and nonzero coefficients. Because the field has characteristic zero, completing the square diagonalizes it. We therefore write the form as a sum of five terms, each a coefficient times a square. The coefficients need not be integers at first.

Every nonzero two-adic number has a unique integer valuation. Multiply an individual variable by a suitable power of two: this changes its coefficient by a power of four. Thus, without changing the existence of nonzero solutions, each coefficient can be put into one of two categories: an odd two-adic unit, or twice an odd two-adic unit. We will call the first category a unit coefficient and the second an even coefficient. It is the valuation parity, not the sign or the size of the coefficient, that matters for this reduction.

Why is this allowed when our aim is only existence? Multiplying a coordinate by two is not an invertible operation over the ring of two-adic integers. But it is invertible over the field Q-two: its inverse is multiplication by one-half. We are classifying solutions over the field, so the change loses no solution.

A unit square modulo eight is always one. The square of a number divisible by two can contribute either zero or four modulo eight. By contrast, twice an odd unit times a square contributes either zero or twice that unit modulo eight. These are the only residues we will use.

## What a liftable congruence looks like

A solution to the form modulo eight is not automatically an exact two-adic solution. An all-even solution, for example, tells us almost nothing; it could be an artifact of reducing modulo a small power of two. We need to arrange a solution where at least one variable corresponding to a unit coefficient is odd.

Suppose that happens. Hold the other four variables fixed, and regard the left-hand side as a polynomial in the remaining variable. At the odd chosen value, its derivative is twice an odd number, so its two-adic valuation is exactly one. If the polynomial vanishes modulo eight, its value has valuation at least three. Three is strictly greater than twice one. The strengthened Hensel criterion therefore produces an exact root near that chosen value. Because the chosen variable stays odd, the resulting vector is nonzero.

The whole problem has become finite: construct a zero modulo eight with an odd variable attached to a unit coefficient. We will make that construction for every possible distribution of the two coefficient types.

## Two unit coefficients

Start with exactly two unit coefficients. Set both corresponding variables to one. Their combined contribution is even, because the sum of two odd numbers is even. Three coefficients remain, each twice an odd unit. Setting each of their variables either to zero or to one lets us add selected members of three numbers, each congruent to two or six modulo eight.

Those subset sums attain every even residue modulo eight. To see why, divide by two and work modulo four. Each of three available summands is plus one or minus one modulo four. Selecting none gives zero; selecting appropriate one, two, or all three gives the other three residue classes. If all three are plus one, the partial sums are zero, one, two, and three. If some are minus one, the same four classes remain available after changing which summands are selected.

Choose a subset sum that cancels the first two coefficients. We now have a zero modulo eight, and in fact two variables associated with unit coefficients are odd. The Hensel criterion applies.

## Three unit coefficients

Suppose instead that three coefficients are units and two are twice units. Set two unit-coefficient variables equal to one. Their total contribution is again some even residue. Leave the third unit-coefficient variable temporarily at zero. The two even-coefficient variables can contribute zero, twice one odd unit, twice the other, or their sum. In a moment we can also set the third unit-coefficient variable to two, which adds four modulo eight regardless of its coefficient.

These choices cover all four even residues modulo eight. For example, if both even coefficients are two modulo eight, their subset sums are zero, two, and four; adding the optional four supplies six. If both are six, the argument is the same with two and six exchanged. If one is two and the other six, their subset sums include zero, two, and six; the optional four supplies the missing four. Thus we can always cancel the contribution of the first two unit coefficients, without changing their odd variables.

Again a primitive, liftable congruence is found.

## Four and five unit coefficients

With four unit coefficients and one even coefficient, set two unit variables to one, a third unit variable to either zero or two, and the even-coefficient variable to either zero or one. The adjustable contributions from the last two choices are zero or four, plus zero or two or six. Together these yield all even residues modulo eight. The initial two odd unit contributions can therefore be canceled. The fourth unit variable can remain zero.

With five unit coefficients, look at their residues modulo four. Each is either one or three. Among five of them, choose four whose sum is divisible by four. This is always possible: remove a coefficient so that the chosen group contains an even number of threes. Set the four corresponding variables to one. Their total is either zero or four modulo eight. Set the remaining variable to zero if the total is zero, and to two if the total is four. In the second case the extra contribution is four, making the total zero modulo eight. At least four unit variables are odd, so lifting is assured.

We have proved the assertion whenever at least two of the five coefficients are units. What if there are zero or one?

## The apparent missing cases

If all five coefficients are twice units, divide the whole form by two. The equation is unchanged, and all five coefficients become units. That case is finished.

If exactly one coefficient is a unit, replace its variable by twice a new variable and divide the whole form by two. The distinguished coefficient becomes twice a unit; the other four coefficients become units. We are back in the four-unit case. This substitution is invertible over Q-two, so a solution of the transformed equation gives a solution of the original.

These exhaust the possibilities. There were five variables, two valuation-parity types, a small residue calculation, and a precise lifting test. We have now proved that every nondegenerate five-variable quadratic form over Q-two is isotropic. A form with six or more variables contains a nondegenerate five-variable diagonal subform, so the same result holds in every higher dimension.

## Why four still is not enough

We should test the sharpness. Take the four-variable form x squared minus five y squared minus twice z squared plus ten w squared. Group it as a norm from Q-two with the square root of five, minus twice another such norm. The extension Q-two of the square root of five is unramified and quadratic. The valuation of every nonzero norm from that extension is even.

If the two norms were equal after multiplying one by two, their valuations would have to be both even and odd. That is impossible. A norm can vanish only on the zero element of the field extension. Consequently all four variables must vanish. This is an anisotropic four-variable form over Q-two.

There is a natural temptation to treat our modulo-eight argument as a magic list of congruences. But it answers a more general question: how much finite precision is enough to certify an exact p-adic solution? The answer depends not only on the residual value of the polynomial, but also on the valuation of one derivative. Here eight was exactly the precision we needed once a unit-coefficient coordinate was odd.

The prime two has now caught up with the odd primes for the statement we need: five variables always force a local zero. That does not prove anything yet about whether compatible local zeros arise from one rational vector. The next step is global. We will first prove the decisive three-variable case using the geometry of numbers, where a lattice inside a carefully chosen cylinder forces an exact zero.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(q=\langle a_1,\dots,a_5\rangle\) over \(\mathbb Q_2\), with all \(a_i\ne0\). After coordinate scaling by squares, \(a_i=2^{e_i}u_i\) with \(e_i\in\{0,1\}\) and \(u_i\in\mathbb Z_2^\times\). The useful residues modulo 8 are

\[
 u(2m+1)^2\equiv u,\quad u(2m)^2\in\{0,4\},\quad 2u(2m+1)^2\equiv 2u\in\{2,6\}\pmod8.
\]

**Precise lifting condition:** If \(F(T)=aT^2+C\) with \(a,T_0\) odd and \(F(T_0)\equiv0\pmod8\), then \(v_2(F(T_0))\ge3>2v_2(F'(T_0))=2\). Strengthened Hensel lifting gives \(T\in\mathbb Z_2\) with \(F(T)=0\), \(T\equiv T_0\pmod2\).

**Finite construction by number \(k\) of unit coefficients:** For \(k=2\), two unit variables equal 1 and the three even-coefficient variables in \(\{0,1\}\) provide all even residues. For \(k=3\), take two unit variables 1, the third 0 or 2, and the two even-coefficient variables 0 or 1. For \(k=4\), use two unit variables 1, another 0 or 2, and the single even variable 0 or 1. For \(k=5\), select four of the five odd coefficients whose sum is divisible by 4; set these variables to 1 and the fifth to 0 or 2. For \(k=0\), divide through by 2. For \(k=1\), replace the unique unit-coefficient variable \(x\) by \(2X\), then divide by 2, obtaining \(k=4\).

**Sharp counterexample:** \(q=\langle1,-5,-2,10\rangle\). Write \(q=N(x+y\sqrt5)-2N(z+w\sqrt5)\) with \(N\) the norm from the unramified extension \(\mathbb Q_2(\sqrt5)\). Norm valuations are even; hence \(q\) is anisotropic.

### Exercises

1. Work modulo 8 for \(q=\langle1,3,2,6,2\rangle\) and exhibit a vector satisfying the lifting condition. Specify the variable to which you apply Hensel's lemma.
2. Show directly why the usual simple-root mod-2 version of Hensel's lemma cannot be applied to a diagonal quadratic form.
3. Check that the four-selected-odd-coefficient argument works for each possible number of coefficients congruent to 3 modulo 4.
4. Prove that an isotropic nondegenerate quadratic form over a field of characteristic different from two represents every element of that field.

## Sources and reading

- Michael Stoll, *Introductory Number Theory*, sections 19–20: https://www.mathe2.uni-bayreuth.de/stoll/lecture-notes/IntroductoryNumberTheory.pdf
- John Voight, *Quaternion Algebras*, local quadratic-form chapters: https://jvoight.github.io/quat-book.pdf
- Wikipedia: [p-adic number](https://en.wikipedia.org/wiki/P-adic_number), [Hensel's lemma](https://en.wikipedia.org/wiki/Hensel%27s_lemma), [Quadratic form](https://en.wikipedia.org/wiki/Quadratic_form).

**Proof scope:** Complete proof of five-variable isotropy over \(\mathbb Q_2\) using a finite congruence construction and strengthened Hensel lifting. The general classification by determinant and Hasse invariant is not used.
