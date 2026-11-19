# 022000 — A Complete Proof of Dirichlet's Theorem on Primes in Progressions

**Track:** Number Theory from First Principles. **Background:** character orthogonality, Euler products, and the proved nonvanishing theorem at \(s=1\). **Aim:** give an unconditional proof for every reduced arithmetic progression, including the stronger reciprocal-prime divergence and Dirichlet density statements.

<!-- BEGIN SPOKEN LECTURE -->

# A Complete Proof of Dirichlet's Theorem on Primes in Progressions

Pick a positive integer q and a remainder a that is relatively prime to q. Start at a and repeatedly add q. Are there infinitely many primes among the resulting integers? When q is two, the claim is easy: all primes except two are odd. When q is five, the claim includes every nonzero remainder class, not just the class of one. For an arbitrary modulus, there is no elementary trick that works one remainder at a time.

Dirichlet proved the general theorem in the nineteenth century. We are now ready to prove it from the ingredients we have established, including the difficult fact that no nonprincipal Dirichlet L-series vanishes at one. The proof will establish a little more than the existence of infinitely many primes in each class. It will show that the sum of their reciprocals diverges, and it will identify their Dirichlet density among all primes.

We will first collect the relevant estimates, then let character orthogonality do the reconstruction. Every step is unconditional because the nonvanishing result is no longer an assumption left outside the argument.

## Turn a prime sum into a logarithm

Fix a Dirichlet character chi modulo q. For real s greater than one, its L-series has an absolutely convergent Euler product. Take logarithms factor by factor, using the power-series identity for negative log of one minus z. The first term contributed by a prime p is chi of p divided by p to the s. The remaining terms come from the second, third, and higher powers of p.

The combined higher-power remainder stays bounded as s approaches one from above. Here is the estimate. At a given prime, the absolute value of the sum of all the terms from the second power onward is no larger than the sum of p to the negative k s over k at least two. That geometric tail is p to the negative two s divided by one minus p to the negative s. Since p is at least two and s is at least one, the denominator is at least one half. Summing over primes gives a bound by twice the convergent sum of one over p squared.

Thus the logarithm of L of s comma chi equals the sum of chi of p divided by p to the s, up to an error bounded independently of s near one. All the prime powers beyond the first are packed into a harmless finite remainder.

There is one detail about logarithms of complex numbers. A nonzero complex number has many logarithms differing by multiples of two pi i. Here we use the logarithm defined by the absolutely convergent Euler expansion for s greater than one. If L stays nonzero near one, this chosen logarithm stays bounded as s approaches one. We can see this by choosing a small neighborhood of its nonzero limiting value, using a continuous logarithm there, and noticing that the difference from the Euler logarithm is a fixed multiple of two pi i on our connected interval. That fixed difference cannot diverge.

The statement is simple to use: a nonprincipal L-series with nonzero value at one has a bounded prime-weighted logarithm as s approaches one.

## The principal character supplies the divergence

Let chi naught be the principal character, one on integers coprime to q and zero on the others. Its L-series is zeta of s, multiplied by the finite product over primes dividing q of one minus p to the negative s.

As s descends to one, the finite product approaches a positive constant, phi of q divided by q. Zeta, by its explicit pole calculation, behaves like one over s minus one. Taking logarithms, the principal character contributes log of one over s minus one, plus a bounded term.

Every other character behaves differently. Our full nonvanishing theorem says that L of one comma chi is nonzero for every nonprincipal chi, real or complex. The analytic continuation ensures its value as s tends to one is finite. The local logarithm argument then shows that each nonprincipal character contributes only a bounded quantity.

This is the separation that makes the proof possible. Among finitely many characters, exactly one has a logarithm growing without bound at the point in question. All others stay bounded. Averaging them cannot erase that one divergent term.

## Project onto the chosen remainder

Recall the finite-group orthogonality formula. For any integer n, the indicator that n is congruent to our chosen a modulo q is one over phi of q times the sum over all characters chi of chi of n multiplied by the complex conjugate of chi of a.

The formula also handles integers not coprime to q. Every character vanishes there, and a, being a unit residue, cannot be congruent to a nonunit integer. Thus the indicator identity works for every integer n, including primes dividing q.

Multiply that identity by one over p to the s, for each prime p, and sum over all primes. For s greater than one, the sums converge absolutely and there are only finitely many characters, so exchanging the order of summation is legitimate.

The result is a formula for the reciprocal-power sum over primes in our chosen residue class. It is one over phi of q times a finite sum of prime-weighted character series. In each character series, replace the prime sum by the corresponding Euler logarithm, plus the uniformly bounded prime-power error.

The coefficient of the principal logarithm is exactly one. The principal character takes value one at the unit a, and so does its complex conjugate. The remaining character coefficients have absolute value one, but that hardly matters: each multiplies a bounded logarithm, and there are only finitely many of them.

Therefore the sum of one over p to the s, over primes p congruent to a modulo q, equals one over phi of q times log of one over s minus one, plus a bounded error as real s approaches one from above.

That is the central estimate. We have isolated one residue class without directly finding any of its primes. Character orthogonality located the class; the principal L-series forced growth; nonvanishing prevented the other L-series from cancelling that growth.

## The theorem and its stronger companion

Let s approach one from above. The logarithm of one over s minus one increases without bound. The error remains bounded. Hence the reciprocal-power sum over primes in our class increases without bound.

Suppose there were only finitely many such primes. Their reciprocals to the power s would form a finite sum and would have a finite limit as s approached one. That contradicts the divergence we just proved. So there must be infinitely many primes congruent to a modulo q.

We can say more. For each individual prime, one over p to the s increases to one over p as s decreases to one. Since all the summands are nonnegative, the limit of the entire sum is the sum of prime reciprocals, allowing infinity as a possible value. Our estimate forces that limit to be infinity. Thus the sum of one over p among primes in any reduced class diverges.

Infinitely many primes need not, in general, contribute a divergent reciprocal sum. Dirichlet's theorem in the form proved here rules out that possibility for a complete reduced arithmetic progression.

If q is one, there is only one residue class and the result is Euclid's theorem together with Euler's divergence of prime reciprocals. For every q at least two, the character argument above applies directly. We have therefore covered all positive moduli.

## See the filter work modulo five

For a concrete picture, use q equal to five. The units are one, two, three, and four. Two generates this group. There are four characters. Index them by j equal to zero, one, two, or three, and let the jth character send two to i to the jth power.

We want primes congruent to three modulo five. Three is the cube of two modulo five. Therefore the complex conjugate of the jth character at three is i to the jth power. The filter for remainder three is one quarter of the sum of i to the jth power times the jth character of n, with j ranging from zero to three.

If n is three modulo five, all four terms equal one and the average is one. If n is two modulo five, the terms alternate one and negative one, averaging to zero. If n belongs to the other unit classes, the four complex roots of unity cancel as well. If n is divisible by five, every character value is zero.

So the character average really does select the exact remainder, not an approximation to it. The theorem says that the primes three, thirteen, twenty-three, forty-three, and the later primes in this same class are not merely a list that happens to continue in the examples. There are infinitely many of them, and their reciprocals have divergent sum.

Notice that modulus five contains nonreal characters. Its proof uses the positive trigonometric Euler-product argument from the complex-character case. Modulus eight, by contrast, has only real characters; the positive-coefficient Landau argument is essential for the general method to cover it. Our proof does not choose one or the other based on q. It has already dealt with all characters, so the final orthogonality step is uniform.

## How evenly distributed?

There is a natural quantitative measure that this argument does establish. Let P of s be the sum of one over p to the s over all primes. Its growth near one is log of one over s minus one, up to a bounded term. For our residue class, the same sum is one over phi of q times that main growth, up to a bounded term.

Divide the class sum by the all-primes sum and let s approach one from above. The ratio tends to one over phi of q. This limit is called the Dirichlet density. Every reduced residue class has the same Dirichlet density among the primes.

That conclusion should not be confused with the stronger counting statement that the number of primes in a class up to x is asymptotic to x divided by phi of q times log x. This is the prime number theorem for arithmetic progressions. The existence of a Dirichlet density is not, on its own, a proof of that counting asymptotic.

What would be needed for the stronger theorem? We would need much more control over the L-functions, particularly on a whole boundary line in the complex plane, not merely at the single point s equal to one. We would also need an argument converting that control into estimates for counts up to a large number x.

For our present goal, no such further theorem is required. We have established Dirichlet's theorem for every reduced progression, proved the stronger divergence of reciprocal primes, and computed their Dirichlet density. The proof shows exactly how elementary arithmetic, multiplicative characters, series, and analytic continuation cooperate. In the next part of this course, we can turn from the existence of primes in residue classes to estimating how many primes there are up to a given size.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Complete theorem and prime-logarithm estimate

**Dirichlet's theorem (with reciprocal divergence).** For all integers \(q\ge1\) and \(a\) with \(\gcd(a,q)=1\),
\[
\boxed{\sum_{\substack{p\ \mathrm{prime}\\p\equiv a\ (q)}}\frac1p=\infty.}
\]
In particular, infinitely many primes satisfy \(p\equiv a\pmod q\).

For any \(\chi\bmod q\) and real \(s>1\), the Euler logarithm satisfies
\[
\log L(s,\chi)=\sum_p\frac{\chi(p)}{p^s}+R_\chi(s),\quad
R_\chi(s)=\sum_p\sum_{k\ge2}\frac{\chi(p)^k}{k p^{ks}},\quad
|R_\chi(s)|\le2\sum_p p^{-2}.
\]
The \(\log\) on the left is the branch determined by this convergent series. For \(\chi\ne\chi_0\), lectures 020000 and 021000 prove \(L(1,\chi)\ne0\). By analyticity and a local analytic logarithm, the Euler-defined \(\log L(s,\chi)\) is bounded on the real interval \(1<s<1+\epsilon\): the two logarithms differ by one constant integer multiple of \(2\pi i\) on that connected interval. Hence \(\sum_p\chi(p)p^{-s}=O_q(1)\).

For the principal character,
\[
L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}),\quad
\log L(s,\chi_0)=\log\frac1{s-1}+O_q(1).
\]
For any unit residue \(a\bmod q\), orthogonality gives
\[
\begin{aligned}
\sum_{p\equiv a\ (q)}p^{-s}
&=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(a)}\sum_p\chi(p)p^{-s}\\
&=\boxed{\frac1{\varphi(q)}\log\frac1{s-1}+O_q(1)},\qquad s\downarrow1.
\end{aligned}
\]
This diverges, proving the reciprocal-sum assertion by monotone convergence. It also implies Dirichlet density \(1/\varphi(q)\), since \(\sum_p p^{-s}=\log(1/(s-1))+O(1)\).

### Modulo-five character filter

Let \(\chi_j(2)=i^j\) for \(j\in\{0,1,2,3\}\). Since \(3\equiv2^3\pmod5\), \(\overline{\chi_j(3)}=i^j\), hence
\[
\mathbf1_{n\equiv3\ (5)}=\frac14\sum_{j=0}^3 i^j\chi_j(n).
\]
This holds also for nonunit \(n\), since each character is zero on multiples of five.

### Boundaries and exercises

- **Proved:** infinitude, divergence of reciprocal sums, and Dirichlet density \(1/\varphi(q)\) for every reduced class.
- **Not proved:** the prime number theorem in arithmetic progressions \(\pi(x;q,a)\sim x/(\varphi(q)\log x)\). Dirichlet density and natural-density/counting asymptotics are distinct notions.

1. State precisely where in the proof convergence is absolute, and where it is only conditional.
2. Check the prime-power remainder bound for \(s\ge1\), including primes dividing \(q\).
3. Prove the boundedness of the Euler-defined logarithm near one from the local logarithm and connectedness argument.
4. Compute the four-character projection for remainder two modulo five.
5. Explain why bounded-error logarithmic growth is enough to prove divergence of reciprocals but does not imply a precise asymptotic for \(\pi(x;q,a)\).
6. Use \(\sum_{p\equiv a(q)}p^{-s}\) and \(\sum_p p^{-s}\) to derive Dirichlet density without invoking the prime number theorem.

### Sources and further reading

- Andrew V. Sutherland, MIT 18.785, [Lecture 18: Dirichlet L-functions and primes in arithmetic progressions](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec18.pdf), §18.4.
- Kiran Kedlaya, [Primes in arithmetic progressions](https://kskedlaya.org/ant/chap-primes-in-ap.html), §4.3.
- Manuel Eberl, [Dirichlet L-functions and Dirichlet's theorem](https://isa-afp.org/entries/Dirichlet_L.html), formalized proof.
- Wikipedia: [Dirichlet's theorem on arithmetic progressions](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions), [Dirichlet density](https://en.wikipedia.org/wiki/Dirichlet_density), [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem).
