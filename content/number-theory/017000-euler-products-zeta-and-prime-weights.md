# 017000 — Euler Products, the Zeta Function, and Prime Weights

**Track:** Number Theory from First Principles. **Background:** unique factorization, series comparison and logarithms, Möbius inversion, and partial summation. **Theme:** use absolute convergence to turn prime factorization into an infinite product without manipulating divergent expressions.

<!-- BEGIN SPOKEN LECTURE -->

# Euler Products, the Zeta Function, and Prime Weights

Imagine giving every positive integer n a weight of one over n squared. The total of all those weights is finite. Now ask a different question: instead of summing over all integers, could we recover the total by making an independent choice at each prime? Choose no factor of two, one factor of two, two factors of two, and so on. Do the same for three, for five, and for every other prime. Multiply all the corresponding geometric sums. Unique factorization suggests that each integer will appear exactly once.

The suggestion is correct, but it hides a mathematical obligation. Infinite sums and infinite products are limits, and rearranging infinitely many terms is not automatically legitimate. We will prove the identity in a region where convergence supplies the required control. Then we will learn what happens as we approach the boundary where convergence fails.

## The zeta series before complex analysis

For a real number s greater than one, define zeta of s as the sum, over all positive integers n, of one over n to the power s. We proved that this series converges exactly for s greater than one, at least if we take positive real s as our starting point. For s equal to two its opening terms are one, one quarter, one ninth, one sixteenth and so on. The exact value at two is famous, but we will not need to evaluate it.

We can already estimate zeta near one. Because t to the negative s decreases, the integral from one to infinity of t to the negative s is at most the full series. Conversely, the series is at most one plus that integral. The integral equals one divided by s minus one. Consequently zeta of s lies between one over s minus one and one plus one over s minus one.

When s moves down toward one from above, zeta grows without bound, on the scale of one over s minus one. This is a precise version of the harmonic-series divergence. For the moment we need only real s; the same expression later defines a function of a complex variable in the region where the real part is greater than one.

## From finitely many primes to all integers

Choose a finite collection of primes, say two, three and five. For each prime p, form the geometric sum one plus one over p to the s plus one over p to twice s and so forth. That sum equals one divided by one minus one over p to the s. Multiply the three sums. Each term in the expansion corresponds to a choice of exponents for two, three and five. Unique factorization says that different choices give different positive integers.

The resulting product is therefore the sum of one over n to the s across all positive integers whose prime factors belong to our chosen set. This is an exact identity involving only a finite number of convergent geometric series. In particular it is no larger than zeta of s.

Now include every prime up to some cutoff P. As P grows, the product increases, because it includes more nonnegative terms. It never exceeds zeta of s, so it has a finite limit. Every fixed positive integer eventually appears: once the cutoff exceeds its largest prime factor, its reciprocal power is included. Thus the limit cannot omit any term of the zeta series. The limit equals zeta of s.

We have proved Euler's product formula: for s greater than one, zeta of s equals the product over all primes p of one divided by one minus p to the negative s. The proof does not rely on a formal multiplication of two unspecified infinite objects. It proceeds through finite prime sets and a monotone limit.

There is even a direct error bound. Any integer missing from the product through P has some prime factor greater than P, and therefore is itself greater than P. So the difference between zeta of s and that finite product is no more than the tail of the full reciprocal-power series beyond P. Our integral comparison bounds the difference by P to the power one minus s divided by s minus one. This is a useful way to separate an exact infinite identity from a finite numerical approximation.

## Taking logarithms reveals the primes

The product expresses all integers in terms of primes. To compare their contributions, take logarithms. The logarithm of zeta of s is the sum over primes of the negative logarithm of one minus one over p to the s. This is legitimate for real s greater than one: all factors are positive, and the corresponding logarithm series converges absolutely.

Recall that negative log of one minus u equals u plus an error of at most twice u squared when u is at most one half. Every u equal to p to the negative s lies below one half when s is greater than one. Therefore the logarithm of zeta equals the sum of p to the negative s, over all primes, plus a bounded error. The bound is uniform even as s approaches one from above, because the error is dominated by twice the convergent series of reciprocal squares.

Meanwhile zeta of s grows on the scale of one divided by s minus one. Its logarithm therefore grows like the logarithm of one divided by s minus one, up to a bounded error. Combining these observations, the sum over primes of one over p to the s grows like log of one over s minus one, again up to a bounded error.

This is a second route to the divergence of prime reciprocals. Suppose the sum of one over p converged. Then for every s greater than one, one over p to the s is at most one over p. The corresponding sums would remain uniformly bounded as s approached one. But the logarithmic argument proves that they grow without bound. Contradiction.

The new perspective is not merely another proof of a familiar fact. It shows *why* the boundary s equals one feels the cumulative pressure of all the primes. Euler's product translates the divergence of an integer sum into divergence of a prime sum, with a precise logarithmic transformation between them.

## An example we can calculate

Keep just the prime factors two, three and five, and set s equal to two. The finite product is four thirds times nine eighths times twenty-five twenty-fourths. Multiplying gives twenty-five sixteenths. This number is the sum of one over n squared over all positive integers n of the form two to the a times three to the b times five to the c, with a, b and c nonnegative integers.

It is smaller than zeta of two because integers such as seven and eleven have been excluded. It is also larger than the sum of reciprocals of squares through six, because it contains many integers greater than six. A prime cutoff and an integer cutoff are different approximations to the same limit. The integral tail bound compares them rigorously even when their terms are ordered differently.

A partial Euler product and a partial sum over consecutive integers have different errors: for the product, the relevant missing terms are the integers excluded by its choice of primes.

## From zeta to other arithmetic functions

We have already met the Möbius function, which is zero on integers with squared prime factors and alternates sign according to the number of distinct prime factors. Möbius inversion gives an identity for arithmetic functions under Dirichlet convolution. Euler products let us package that identity into ordinary multiplication of series.

Suppose F of s is the sum of f of n divided by n to the s, and G of s is the corresponding sum for g. Assume both series converge absolutely. Multiply them. We obtain terms with denominators a to the s times b to the s. Group together all pairs a and b whose product is a given integer n. Their coefficients sum to the Dirichlet convolution of f and g evaluated at n. Because of absolute convergence, this regrouping is valid. Thus multiplication of Dirichlet series corresponds exactly to Dirichlet convolution of their coefficients.

Take f to be the constant arithmetic function one and g to be Möbius. Their convolution is the identity function that equals one at n equal to one and zero elsewhere. The generating series for the constant function is zeta. Therefore the generating series for Möbius is the reciprocal of zeta, when s is greater than one. This is not a statement about a potentially divergent series at s equal to one; the domain of absolute convergence is part of the result.

Similarly, the totient function is the Dirichlet convolution of the identity function n with Möbius. Its Dirichlet series is zeta of s minus one divided by zeta of s, valid when s is greater than two. The stronger restriction appears because the totient grows on the scale of n, so its reciprocal-power series needs an additional power in the denominator.

There is a general lesson in these examples. Arithmetic convolution is a complicated-looking sum over divisors. A Dirichlet series can turn it into multiplication, just as an ordinary power series turns convolution of sequences into a product. The price of this convenience is attention to convergence.

## A weight that finds prime powers

There is another arithmetic function worth defining. Call it capital Lambda. It assigns log p to an integer n when n is a positive power of a prime p, and zero otherwise. For example, Lambda of eight is log two, Lambda of nine is log three, and Lambda of twelve is zero because twelve has two different prime factors. This is the von Mangoldt function.

Why make a function that counts prime powers rather than primes themselves? Because differentiation of the logarithm of Euler's product produces exactly these weights. Start from the logarithm of zeta of s. Expand each factor using the geometric logarithm series. The contribution from a prime p is the sum, over positive integers k, of one divided by k times p to the power k s.

Differentiate with respect to s. The k from the exponent cancels the one over k, leaving log p times p to the negative k s, with a minus sign. Summing over primes and positive exponents gives an exact identity: negative zeta prime of s divided by zeta of s equals the sum over all n of Lambda of n divided by n to the s. Here “zeta prime” means the derivative of the function zeta, not a new collection of prime integers.

We may differentiate term by term in the region s greater than one because the series of log n divided by n to the s converges there; one can verify this by an integral comparison. The identity is rigorous in that region. It describes a weighted prime-counting problem as a logarithmic derivative of a function built from all integers.

If we could understand the behavior of this derivative close to s equal to one with sufficiently strong control, we could obtain powerful results about primes. This points toward the prime number theorem. But the derivative identity alone does not prove the prime number theorem. Extracting sharp counts from it requires additional arguments that we have not supplied.

## Why a twisted product is next

The ordinary Euler product sees every prime without distinguishing its residue class. Our characters, however, assign a multiplicative complex weight to each integer. We can therefore build a new Dirichlet series whose coefficients are chi of n rather than one. For s greater than one, the same unique-factorization argument will give a product over primes with chi of p in each factor.

Combining this twisted Euler product with the character filter can, in principle, isolate one arithmetic progression. The decisive distinction will be between the principal character, whose series behaves like zeta near one, and the nonprincipal characters, whose periodic cancellation lets their series converge there. There is a further issue: convergence does not guarantee that the limiting value is nonzero. That issue is the gateway to Dirichlet's theorem.

We have earned the gateway without skipping steps. Euler products are justified by convergence and unique factorization; logarithms expose a sum over primes; Dirichlet series turn arithmetic convolution into multiplication; and a logarithmic derivative produces the weights of prime powers. These are the mechanisms, not merely a collection of formulas.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Zeta and its finite-prime approximation

For real \(s>1\):
\[
\zeta(s):=\sum_{n\geq1}n^{-s},\qquad
\frac1{s-1}\leq\zeta(s)\leq1+\frac1{s-1}.
\]
For \(P\geq2\), let \(E_P(s)=\prod_{p\leq P}(1-p^{-s})^{-1}\). Expanding finite products of convergent geometric sums shows
\[
E_P(s)=\sum_{\substack{n\geq1\\\text{all prime factors of }n\leq P}}n^{-s},\quad
0\leq\zeta(s)-E_P(s)\leq\sum_{n>P}n^{-s}\leq\frac{P^{1-s}}{s-1}.
\]
This proves \(\zeta(s)=\prod_p(1-p^{-s})^{-1}\) for real \(s>1\). Absolute convergence extends the same proof to complex \(s\) with \(\operatorname{Re}s>1\), using appropriate complex convergence arguments.

For \(s=2\), \(E_5(2)=(4/3)(9/8)(25/24)=25/16\).

### Uniform logarithmic remainder

\[
\log\zeta(s)=\sum_p\sum_{k\geq1}\frac{1}{k p^{ks}}
=\sum_p p^{-s}+R(s),\quad
0\leq R(s)\leq 2\sum_{n\geq2}n^{-2}<\infty
\]
for all real s>1. Since \(\zeta(s)=(s-1)^{-1}(1+O(s-1))\) as \(s\downarrow1\),
\[
\sum_p p^{-s}=\log\frac1{s-1}+O(1).
\]
This proves \(\sum_p1/p\) diverges, by monotone comparison as \(s\downarrow1\). It does **not** prove the prime number theorem.

### Dirichlet convolution and generating series

If \(F(s)=\sum f(n)n^{-s}\) and \(G(s)=\sum g(n)n^{-s}\) both converge absolutely, then
\[
F(s)G(s)=\sum_{n\geq1}\frac{(f*g)(n)}{n^s},\qquad
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d).
\]
Taking \(\mathbf1*\mu=\varepsilon\) yields \(\sum\mu(n)n^{-s}=1/\zeta(s)\) for \(s>1\). Taking \(\varphi=\operatorname{id}*\mu\) yields \(\sum\varphi(n)n^{-s}=\zeta(s-1)/\zeta(s)\) for \(s>2\).

### Von Mangoldt and the logarithmic derivative

\[
\Lambda(n)=\begin{cases}\log p&n=p^k\ (k\geq1),\\0&\text{otherwise}.\end{cases}
\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{p}\sum_{k\geq1}\frac{\log p}{p^{ks}}
=\sum_{n\geq1}\frac{\Lambda(n)}{n^s},\quad s>1.
\]
Termwise differentiation is justified on each real interval \(s\geq1+\varepsilon\), because \(\sum_{n\geq1}(\log n)n^{-1-\varepsilon}\) converges.

### Exercises and reasoning checks

1. Show exactly which integers are counted by \(E_3(s)\). Compare the first ten terms with the full zeta series.
2. Derive a finite-prime product for the sum of \(\mu(n)/n^s\) over squarefree integers with prime factors at most P, and pass to the limit.
3. Use the bound on \(\zeta(s)\) to find \(\lim_{s\downarrow1}(s-1)\zeta(s)\).
4. Explain why the logarithmic remainder contains only prime powers with exponent at least two and why their total weight stays bounded at s=1.
5. For n equal to 8, 9, 12, 25 and 30, evaluate \(\Lambda(n)\). Explain why the logarithmic derivative counts prime powers instead of only primes.

### Sources and further reading

- NIST Digital Library of Mathematical Functions, [Euler Products and Dirichlet Series](https://dlmf.nist.gov/27.4), including the zeta, Möbius and totient identities with their convergence regions.
- NIST Digital Library of Mathematical Functions, [Riemann Zeta Function: Definition and Expansions](https://dlmf.nist.gov/25.2).
- Terence Tao, [Elementary multiplicative number theory](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/), for Euler products and prime sums.
- Wikipedia background: [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function), [Euler product](https://en.wikipedia.org/wiki/Euler_product), [Dirichlet series](https://en.wikipedia.org/wiki/Dirichlet_series), [Von Mangoldt function](https://en.wikipedia.org/wiki/Von_Mangoldt_function), [Dirichlet convolution](https://en.wikipedia.org/wiki/Dirichlet_convolution).
