# 018000 — Dirichlet L-Series and the Boundary of the Progression Theorem

**Track:** Number Theory from First Principles. **Background:** series and partial summation, characters and orthogonality, Euler products, and the distinction between convergent series and nonzero limits. **Theme:** derive the arithmetic-progression mechanism rigorously, prove its small-modulus instances, and identify the separate nonvanishing theorem needed in general.

<!-- BEGIN SPOKEN LECTURE -->

# Dirichlet L-Series and the Boundary of the Progression Theorem

Consider the integers that leave remainder two when divided by five: two, seven, twelve, seventeen, twenty-two, and so on. Many are composite; some are prime. Euclid proves that the list of all primes cannot stop, but his argument does not say whether this particular progression contains infinitely many primes.

The general answer is yes whenever the chosen remainder is coprime to the modulus. This is Dirichlet's theorem on primes in arithmetic progressions. It is a deeper statement than it first appears. The number five is not special here; we want a single explanation for every modulus q and every reduced residue a.

We have built the tools for the main idea. Characters select a residue by averaging multiplicative weights. Euler products translate multiplicative weights into sums over primes. Partial summation controls character series at the point where ordinary zeta diverges. The difficult step lies at a precise boundary: showing that a certain convergent character series does not converge to zero.

We will derive the mechanism in detail, carry it all the way through for some simple moduli, and mark honestly what the general theorem requires beyond these foundations.

## A Dirichlet series for each character

Fix a modulus q and a Dirichlet character chi. For real s greater than one, define capital L of s comma chi as the infinite sum of chi of n divided by n to the s. This is called a Dirichlet L-series. It converges absolutely there, because the absolute value of chi of n is at most one and the ordinary zeta series converges.

By complete multiplicativity and unique factorization, we can repeat the Euler-product argument. Capital L of s comma chi is the product over all primes p of one divided by one minus chi of p over p to the s. The product is absolutely convergent and nonzero when s is greater than one. This last point is important: a product of nonzero factors can sometimes tend to zero, but absolute convergence of the relevant logarithm series rules that out in our present region.

If chi is the principal character, the series includes precisely the integers coprime to q. Its Euler product agrees with zeta except that the factors at primes dividing q are missing. Consequently its value equals zeta of s times the product, over prime divisors p of q, of one minus p to the negative s.

There are only finitely many prime divisors of a fixed modulus. As s approaches one from above, their finite product approaches the product of one minus one over p. By the familiar totient formula, that limit is phi of q divided by q, a positive number. Since zeta grows like one over s minus one, the principal L-series also diverges on that scale.

This is the source of the main term in the progression problem. The principal character sees all integers that are coprime to q and makes a large positive contribution.

## Nonprincipal characters are different

Now take a nonprincipal character. Its values sum to zero over a complete period of q integers. In particular the partial sums of chi of n remain bounded, independently of how many periods we traverse.

Our partial-summation theorem says that a bounded-cumulative-sum sequence, weighted by one over n, produces a convergent series. Therefore capital L of one comma chi, meaning the sum of chi of n divided by n, is well defined for every nonprincipal character. No analytic continuation is needed for this assertion. In fact, by the same argument, the defining series converges for every positive real s, though it need not converge absolutely below or at one.

This is where the principal and nonprincipal cases separate. The principal series has positive reciprocal terms on all reduced residues and diverges. A nonprincipal series has enough cancellation over its periods to converge. But one logical step is missing: a convergent series may converge to zero. Convergence by itself gives no assurance that its limit can safely appear inside a logarithm or a denominator.

For s greater than one, the Euler product does show that capital L of s comma chi is nonzero. It does *not* follow merely by continuity that the value at s equal to one is nonzero. A function can be nonzero at every point to the right of a boundary and tend to zero at the boundary. The elementary example is the function s minus one for s greater than one.

This is exactly the obstacle that the general proof of Dirichlet's theorem must overcome.

## Logarithms and their error terms

For s greater than one, expand the logarithm of the Euler product for L. Each prime contributes chi of p divided by p to the s, plus terms from higher powers of that prime. The higher-power terms have a uniformly bounded total, even as s approaches one. Their absolute values are bounded by the same convergent reciprocal-square comparison we used for the ordinary zeta product.

Thus, after choosing the continuous logarithm supplied by the absolutely convergent product, log L of s comma chi equals the sum over primes of chi of p divided by p to the s, plus a bounded remainder.

This identity isolates the key distinction. The principal character has log L growing like log of one over s minus one. For a nonprincipal character, if we additionally know that L of one comma chi is nonzero, the logarithm stays bounded as s descends to one. That would force the prime sum weighted by chi to stay bounded too.

Why insist on a nonzero limiting value? Because the logarithm of a number approaching zero tends without bound in its real part. In a character average, an uncontrolled logarithm from a nonprincipal character could compete with the principal divergence. Orthogonality alone cannot prevent that competition.

The hard fact, which we state here but have not proved, is that L of one comma chi is nonzero for every nonprincipal Dirichlet character. Standard proofs establish this with additional analytic or algebraic arguments. It is not a consequence of the simple periodic cancellation we already proved.

## Reassemble a particular residue class

Recall the character filter. For an integer a relatively prime to q, the indicator that an integer n is congruent to a modulo q equals one over phi of q times the sum, over all characters, of chi of n times the conjugate of chi of a.

Apply this identity to each prime and weight by one over p to the s, with s greater than one. The sum over primes p congruent to a modulo q equals one over phi of q times a sum over characters. Each character contributes the conjugate of its value at a times the prime series weighted by that character.

The principal character contributes a quantity growing like log of one over s minus one. The finitely many primes dividing q do not affect that divergence. For every nonprincipal character, the previously described nonvanishing theorem would make its contribution bounded. There are only phi of q characters, a fixed number when q is fixed.

Therefore, *assuming that nonvanishing theorem*, the entire sum over primes in our chosen residue class grows like one over phi of q times log of one over s minus one, up to a bounded error. It tends to infinity as s approaches one from above.

If the class contained only finitely many primes, its weighted prime sum would remain bounded in this limit. So we obtain a contradiction. The class must contain infinitely many primes. In fact, this argument yields the stronger conclusion that the reciprocals of the primes in every reduced residue class have divergent sum.

Notice the order of logic. Character orthogonality is proved. Euler products and their logarithmic expansion are proved for s greater than one. Convergence of nonprincipal L-series at one is proved. The missing general input is nonvanishing at one, and only after it is supplied does the argument prove Dirichlet's theorem for all moduli.

This is a complete conditional derivation, not a claimed proof of the missing input.

## The case modulo three needs no missing theorem

We can use the same framework to obtain an unconditional result for modulus three. There are two units, one and two, and therefore two characters. The principal character is one on numbers not divisible by three and zero on multiples of three. The other character has value one on numbers congruent to one, negative one on numbers congruent to two, and zero on multiples of three.

Call the nonprincipal one chi. Its L-series at one is one minus one half plus one quarter minus one fifth plus one seventh minus one eighth, and so on. Group each consecutive pair according to residues one and two modulo three. The kth pair has the form one over three k plus one minus one over three k plus two. Every pair is strictly positive, and the resulting series converges. Thus L of one comma chi is strictly positive, not merely finite. We have proved nonvanishing for this character without any deep theorem.

Return to the prime sums. The principal logarithm diverges. The logarithm for our nonprincipal character stays bounded because its L-value tends to a positive constant. Taking the sum and difference of the two character contributions isolates primes that are one modulo three and primes that are two modulo three. In each class the reciprocal-power prime sum grows like one half of log one over s minus one, up to a bounded error.

Consequently both reduced residue classes modulo three contain infinitely many primes, and the reciprocal series of the primes in either class diverges. We have not merely quoted Dirichlet's theorem in this example: we have proved the necessary nonvanishing and completed the argument.

## Another concrete case: modulus four

Modulo four the nonprincipal character is zero on even integers, one on integers congruent to one, and negative one on integers congruent to three. Its L-value at one is the alternating series one minus one third plus one fifth minus one seventh and so on.

We can identify this series as the integral from zero to one of one divided by one plus t squared. Expand the denominator into alternating powers on a truncated interval, integrate term by term, and then pass to the endpoint using the alternating-series error bound. The integral is arctangent of one minus arctangent of zero, which is pi divided by four. In particular, the L-value is positive.

The same character-filter argument therefore proves divergent prime-reciprocal sums separately for the classes one and three modulo four. We already proved infinitude for these classes by elementary constructions, but the present route strengthens the statement and explains how the argument generalizes.

For modulus five, there are complex-valued nonprincipal characters. Their convergence at one follows from periodic cancellation, but the elementary positivity arguments we just used no longer settle the nonvanishing question. That is a real increase in difficulty, not a defect of the character method.

## What the method does and does not count

At this point we have established that a weighted sum over primes in a reduced progression diverges as s approaches one, either under the general nonvanishing theorem or unconditionally for our two small moduli. The immediate consequence is infinitude. It does not automatically tell us how many such primes lie below x.

Dirichlet's theorem says each reduced progression contains infinitely many primes. The prime number theorem in arithmetic progressions makes a substantially sharper claim: for a fixed modulus q and a reduced class a, the number of primes up to x in that class is asymptotic to x divided by phi of q times log x. Proving that requires further estimates and control of L-functions, beyond the nonvanishing at one that suffices for infinitude.

Even when an analytic expression looks approximately proportional to log one over s minus one, converting it to a precise statement about the counting function is its own mathematical task. Summation by parts can move between certain kinds of information, but it cannot manufacture estimates stronger than those supplied as input.

## Where a complete proof should go next

We can now describe the remaining work in a future proof of Dirichlet's theorem. First, prove that L of one comma chi is nonzero for every nonprincipal complex character, not just the real characters in small examples. Second, justify the limiting logarithms for all characters using that result. Third, feed the character average into the prime-product identity, as we have already done conditionally.

There are multiple routes to the nonvanishing theorem. One elementary analytic approach uses nonnegative Dirichlet-convolution coefficients and a careful treatment of real and complex characters; another uses deeper algebraic number theory to interpret special L-values. Both require arguments we should develop in full rather than hide behind the phrase “standard methods.”

The structure of the problem is now visible. Unique factorization turns an integer series into a prime product. Characters turn a residue condition into a finite average. Summation by parts makes cancellation precise. A logarithm exposes the contribution of each prime. And one theorem about nonzero L-values is what prevents those contributions from cancelling the main divergence. That is the precise bridge from foundational arithmetic to analytic number theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Dirichlet L-series and Euler products

For any character \(\chi\bmod q\) and real \(s>1\), absolute convergence gives
\[
L(s,\chi)=\sum_{n\geq1}\frac{\chi(n)}{n^s}
=\prod_p\left(1-\frac{\chi(p)}{p^s}\right)^{-1} \neq0.
\]
For the principal \(\chi_0\),
\[
L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}),\qquad
\lim_{s\downarrow1}(s-1)L(s,\chi_0)=\prod_{p\mid q}(1-p^{-1})=\frac{\varphi(q)}{q}.
\]
For nonprincipal \(\chi\), \(\sum_{n\leq x}\chi(n)=O(q)\). Abel summation proves \(L(1,\chi)=\sum\chi(n)/n\) converges and, more generally, uniform convergence of \(L(s,\chi)\) for real \(s\in[1,2]\). For a tail starting after N, \(\sum_{n>N}\chi(n)/n^s=O(q N^{-s})\) for real \(s>0\), with the implicit constant absolute for s in a compact interval away from zero.

### Prime logarithms and the missing boundary theorem

For \(s>1\), define \(\log L(s,\chi)\) by the absolutely convergent Euler logarithm series. Then
\[
\log L(s,\chi)=\sum_p\frac{\chi(p)}{p^s}
+\sum_p\sum_{k\geq2}\frac{\chi(p)^k}{k p^{ks}},
\quad\left|\sum_p\sum_{k\geq2}\frac{\chi(p)^k}{k p^{ks}}\right|\leq 2\sum_{n\geq2}n^{-2}.
\]
If \(L(1,\chi)\ne0\), continuity makes the logarithm bounded as \(s\downarrow1\). Thus \(\sum_p\chi(p)p^{-s}=O_q(1)\) for each nonprincipal character. The general assertion \(L(1,\chi)\ne0\) is **stated but not proved** in this course installment.

### Orthogonality and conditional derivation of Dirichlet's theorem

For \(\gcd(a,q)=1\),
\[
\sum_{\substack{p\ \mathrm{prime}\\p\equiv a\pmod q}}\frac1{p^s}
=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(a)}\sum_p\frac{\chi(p)}{p^s}
=\frac1{\varphi(q)}\log\frac1{s-1}+O_q(1),\quad s\downarrow1,
\]
**conditional on** the nonvanishing of \(L(1,\chi)\) for all nonprincipal \(\chi\). The last expression diverges, so the progression contains infinitely many primes. Monotone convergence also implies \(\sum_{p\equiv a\ (q)}1/p=\infty\). This is not, by itself, the prime number theorem in progressions.

### Unconditional special-modulus calculations

Modulo 3 the nonprincipal real character satisfies
\[
L(1,\chi_3)=\sum_{k=0}^\infty\left(\frac1{3k+1}-\frac1{3k+2}\right)>0.
\]
Modulo 4,
\[
L(1,\chi_4)=1-\frac13+\frac15-\frac17+\cdots
=\int_0^1\frac{dt}{1+t^2}=\frac\pi4>0.
\]
These establish nonvanishing for all nonprincipal characters modulo 3 and 4, so the conditional progression argument is unconditional for these moduli. For \(q=2\) there are no nonprincipal characters, and the principal contribution covers the odd primes.

### Exercises and reasoning checks

1. Derive the Euler product for a character modulo 5 from finite prime products. Identify exactly where absolute convergence is used.
2. Show that \(\sum_{n\geq1}\chi(n)/n\) need not converge absolutely, even when it converges conditionally.
3. Prove directly that \(L(1,\chi_3)>0\) using the displayed grouped series, and show how it prevents cancellation of the principal contribution.
4. Carefully explain why \(L(s,\chi)\ne0\) for every real s>1 does **not** establish \(L(1,\chi)\ne0\).
5. Write the character projection for a=2 modulo 5 and identify which four weighted prime series it would require.
6. Distinguish each of the following claims: infinitely many primes in a progression, divergent reciprocals of primes in that progression, and an asymptotic formula for the number of those primes up to x.

### Sources and further reading

- NIST Digital Library of Mathematical Functions, [Dirichlet L-functions](https://dlmf.nist.gov/25.15), particularly definitions, Euler products, and the nonvanishing theorem at one.
- Terence Tao, [Elementary multiplicative number theory](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/), including a complete route through nonvanishing and Dirichlet's theorem; our course has **not** reproduced that final proof.
- Terence Tao, [The prime number theorem in arithmetic progressions, and dueling conspiracies](https://terrytao.wordpress.com/2009/09/24/the-prime-number-theorem-in-arithmetic-progressions-and-dueling-conspiracies/), for the later stronger counting theorem and nonvanishing issues.
- Wikipedia background: [Dirichlet L-function](https://en.wikipedia.org/wiki/Dirichlet_L-function), [Dirichlet's theorem on arithmetic progressions](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions), [Dirichlet character](https://en.wikipedia.org/wiki/Dirichlet_character), [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem).
