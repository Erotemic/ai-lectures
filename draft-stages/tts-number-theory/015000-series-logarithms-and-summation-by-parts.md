# 015000 — Series, Logarithms, and Summation by Parts

**Track:** Number Theory from First Principles. **Background:** algebra, fractions, finite sums, the harmonic series, and the elementary idea of a limit. **Theme:** how a question about integers becomes a precise question about a growing sum.

<!-- BEGIN SPOKEN LECTURE -->

# Series, Logarithms, and Summation by Parts

If somebody tells us that primes become rarer, we can ask what the statement means. The proportion of numbers up to a million that are prime is smaller than the proportion up to a hundred. But a few measurements cannot establish a trend forever, and the word “rarer” hides several different questions. Are we comparing counts, proportions, the sum of reciprocals, or gaps between successive primes?

Analytic number theory begins when we replace a vague impression with a function of a growing bound and learn to estimate that function. We will build the needed analysis from elementary sums. The methods matter beyond primes: they are the same methods used to count divisors, estimate algorithms, and convert information about a sequence into information about a weighted sequence.

## What an infinite sum actually asserts

Write down one, then one half, then one quarter, then one eighth. Every finite partial sum is a perfectly ordinary rational number. After N terms, counting one as the first, its value is two minus two to the power one minus N. As N increases, the difference from two becomes arbitrarily small. To say the infinite geometric series equals two means exactly that its partial sums approach two. An infinite sum is a limit of finite sums; it is not an instruction to add infinitely many numbers in one operation.

Now replace successive powers of two by the positive integers. The harmonic sum through N is one plus a half plus a third, all the way to one over N. It also has smaller and smaller added terms, but that fact is not enough for convergence. Group terms from one over two through one over three, then one over four through one over seven, then one over eight through one over fifteen. Each new block contributes at least a half. The harmonic partial sums have no finite limit.

There are two different facts here. A necessary condition for a series to converge is that its individual terms approach zero: otherwise the increments between partial sums could not approach zero. But that condition is not sufficient. The harmonic series is the standard counterexample, and it warns us not to confuse a local property of a term with the global behavior of its sum.

For a series with positive terms, the partial sums never decrease. It converges exactly when these partial sums remain bounded above. Why? A bounded increasing sequence approaches its least upper bound: once a partial sum is within a chosen margin of that least upper bound, all subsequent sums lie between the same partial sum and the bound. This simple completeness principle is behind the comparison tests we use next.

## Comparison turns a difficult sum into a familiar one

Suppose each nonnegative term a sub n is at most another nonnegative term b sub n. Then every finite partial sum of the a series is at most the corresponding partial sum of the b series. If the larger series converges, the smaller one must converge. Conversely, if the smaller series diverges, so must the larger one. The direction of each inference matters.

Take the sum of reciprocals of squares. Starting from n equal to two, one over n squared is no larger than one divided by n times n minus one. The latter expression is one over n minus one minus one over n. Summing these differences causes all middle terms to cancel. Every partial sum is less than one. Thus the reciprocal-square series converges, without knowing its exact value.

What about the series whose terms are one over n to the power s? If s is greater than one, compare each term with an area under a decreasing curve. For n at least two, one over n to the power s is bounded above by the integral of t to the negative s from n minus one to n. Summing, we find that the tail beyond N is no larger than N to the power one minus s divided by s minus one. That bound tends to zero. For s equal to one we already have the harmonic divergence. For positive s less than one, its terms are at least one over n, and the series also diverges. For s at most zero the terms do not even tend to zero. So the positive-term series converges precisely when s is greater than one.

We have now located the first important boundary in analytic number theory: s equal to one. To the right of it, summing one over n to the power s is safe. At the boundary, the same summation becomes infinite. Later, a function called zeta will package that change into a useful analytic object.

## Why the logarithm keeps appearing

For a positive real number x, the natural logarithm of x is the area under one over t between one and x. This is an efficient definition because it tells us how logarithms measure sums of reciprocals. The function one over t decreases. Compare each rectangular bar of height one over n with the nearby area under the curve. For every positive integer N, the logarithm of N plus one is no larger than the harmonic sum through N, and that harmonic sum is no larger than one plus the logarithm of N.

These inequalities do more than prove divergence. They show that the harmonic sum grows on the scale of the logarithm, with an error no larger than one. We do not need a special numerical constant to establish this. If we later choose to prove that the difference between the harmonic sum and log N approaches Euler's constant, that is an additional result, not a prerequisite for our present estimates.

Logarithms also turn products into sums. The logarithm of a product of positive numbers is the sum of their logarithms. For a small positive u, the negative logarithm of one minus u is close to u. The precise estimate we will use is that it lies between u and u divided by one minus u. It comes directly from integrating one over one minus t, whose value across the interval from zero to u stays between one and one divided by one minus u. If u is at most one half, the difference between negative log of one minus u and u is at most twice u squared.

That last statement is a small but powerful tool. In a prime product, we will have u equal to one over p to the power s. Summing the first-order terms will reveal the role of primes, while the errors, involving squared reciprocals, remain bounded. A difficult product can become a manageable sum plus a controlled remainder.

## Summation by parts: the discrete counterpart of integration by parts

Suppose we have a sequence a sub one, a sub two, and so forth. We know something about its cumulative sums, but we want to study a weighted sum in which a sub n is multiplied by a slowly changing number b sub n. Define A sub n to be the sum of the a terms from one through n. Then a sub n is A sub n minus A sub n minus one.

Substitute this difference into the weighted sum and rearrange the finite terms. The result is a discrete integration-by-parts formula: the weighted sum through N equals A sub N times b sub N, plus the sum from n equal one through N minus one of A sub n times the difference between b sub n and b sub n plus one. Nothing infinite has happened. It is an exact finite identity, sometimes called Abel summation or partial summation.

The importance is that cancellation inside the original a sequence is already recorded in A. If A remains small, the weighted sum may be controlled even when the absolute values of the a terms are large. A good weight b changes gradually, so each difference b sub n minus b sub n plus one is small.

For example, let a sub n alternate between one and negative one. Its cumulative sums are either zero or one, so they remain bounded. Weight those signs by one over n. The discrete formula bounds the remaining tail by a constant times one over the starting index. Consequently the alternating harmonic series converges. It does not converge absolutely, because the sum of the absolute values is the divergent harmonic series. The distinction between ordinary and absolute convergence is essential: rearranging a conditionally convergent series as though all terms were positive can change its value.

Here is a version that resembles calculus more closely. Let A of x be the sum of a sub n for integers n no larger than a positive real x, and let f be a continuously differentiable function on the interval from one to x. Then the weighted sum of a sub n times f of n, for n at most x, equals A of x times f of x minus the integral from one to x of A of t times the derivative of f at t. To check this, regard A as constant between successive integers and add up those small integrals. Their endpoint terms telescope into the discrete identity.

This formula tells us how to use an estimate for the unweighted count A of x. If A of x is roughly x, for example, we can plug that approximation into the integral and determine the main behavior of many weighted sums. If A of x is bounded, a decreasing weight may yield convergence. We have exchanged a difficult collection of individual coefficients for the cumulative information we actually possess.

## A useful general test

Let a sequence have bounded partial sums, and let b sub n be nonnegative, decreasing, and approaching zero. Then the weighted series with terms a sub n times b sub n converges. Prove it by applying our finite identity to a tail starting at M. The partial sums within that tail are bounded by a constant. The sum of successive drops of b telescopes, and the boundary term is also small. The whole tail is therefore at most a constant times b sub M, which tends to zero. This is Dirichlet's test for series.

We can apply it to a sequence with a repeating pattern, not just alternating signs. Imagine the cycle one, one, negative two, repeated indefinitely. Each whole cycle sums to zero, so the cumulative sums are bounded. Divide the nth term by n. The weighted series converges even though the absolute-value series does not. The periodic cancellation, rather than the small size of each individual term, is doing the work.

This observation will be crucial when we attach signs, or even complex roots of unity, to integers according to their remainders. Such functions can have bounded partial sums because a complete period sums to zero. Their reciprocal-weighted series may converge at s equal to one, even though the ordinary zeta series diverges there. We now have a tool capable of explaining that difference without assuming complex analysis.

## Counting and weighting are not the same task

Suppose A of x counts certain integers up to x. If we know exactly that A of x is x divided by three plus an error bounded by one, we can estimate not only how many such integers there are but also the sum of their reciprocals. Consider the multiples of three. The count through x is the integer part of x divided by three. Its reciprocal sum is one third of the harmonic sum through the integer part of x divided by three. Hence it grows like one third of log x, with a bounded error.

The same conclusion follows by partial summation from the counting function. More generally, if the number of selected positive integers up to x equals delta times x plus a bounded error, then the sum of one over n across the selected integers up to x equals delta times log x plus a bounded error. The calculation uses the exact formula with f of t equal to one over t. The main term contributes delta times log x; the error contributes a bounded integral of one over t squared.

But beware of weakening the input without checking the output. Merely knowing that the count is asymptotic to delta x, with an error smaller than x but not necessarily bounded, gives the corresponding reciprocal sum delta log x plus an error that is small compared with log x; it does not automatically give a bounded error. Our theorems have hypotheses, and the strength of the conclusion depends on the strength of those hypotheses.

## Estimates are agreements, not evasions

Mathematicians often write that an error is big O of a function g. This means the absolute error is bounded by a fixed constant times g once the argument is large enough. The constant is independent of the growing variable, although it may depend on parameters explicitly held fixed. An error that is big O of one is simply bounded. By contrast, an error described as little o of x is smaller than every fixed positive multiple of x for sufficiently large x.

These two notations should not be treated as interchangeable. A bound of big O of the square root of x is also little o of x, but it is not big O of one. In analytic number theory, even an apparently small change in the error can distinguish an elementary estimate from a deep theorem.

We began with infinitely many arithmetic observations and reduced them to a few disciplined moves: compare positive sums with integrals; use logarithms to translate products into sums; control errors rather than dropping them; and transfer information about cumulative sums into weighted sums by partial summation. These are the tools that make it possible to approach the primes analytically. Before using them on primes, we will build a way to select one residue class at a time. The key idea is an arithmetic version of a Fourier filter.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Convergence and comparison

For real \(s>1\), decreasing-integral comparison gives
\[
0<\sum_{n>N}n^{-s}\leq\int_N^\infty t^{-s}\,dt=\frac{N^{1-s}}{s-1}.
\]
For \(0<s\leq1\), \(n^{-s}\geq n^{-1}\), so divergence follows from the harmonic series. For \(s\leq0\) the terms fail to vanish.

For \(n\geq2\): \(1/n^2\leq1/[n(n-1)]=1/(n-1)-1/n\). Hence \(\sum_{n=2}^\infty1/n^2\leq1\).

### Harmonic sums, logarithms, and a local approximation

\[
\log(N+1)\leq H_N=\sum_{n=1}^{N}\frac1n\leq1+\log N.
\]
For \(0\leq u\leq1/2\):
\[
u\leq-\log(1-u)=\int_0^u\frac{dt}{1-t}\leq\frac{u}{1-u},\qquad
0\leq-\log(1-u)-u\leq\frac{u^2}{1-u}\leq2u^2.
\]
The error term is genuinely quadratic; it can be summed over primes using the convergent square-reciprocal series.

### Exact finite Abel summation

Let \(A_n=\sum_{k=1}^{n}a_k\), \(A_0=0\). Then
\[
\sum_{n=1}^{N} a_n b_n=A_N b_N+\sum_{n=1}^{N-1}A_n(b_n-b_{n+1}).
\]
For \(A(t)=\sum_{n\leq t}a_n\) and continuously differentiable \(f\),
\[
\sum_{n\leq x}a_nf(n)=A(x)f(x)-\int_1^x A(t)f'(t)\,dt.
\]
For a tail \(\sum_{n=M}^{N}a_nb_n\), use partial sums starting at M; if all have absolute value at most C and b decreases to zero, the tail is bounded by \(2Cb_M\), proving Dirichlet's test.

### Worked weighted count

If \(A(x)=\delta x+E(x)\) and \(|E(x)|\leq C\) for \(x\geq1\), partial summation with \(f(t)=1/t\) gives
\[
\sum_{n\leq x}\frac{a_n}{n}=\frac{A(x)}x+\int_1^x\frac{A(t)}{t^2}\,dt
=\delta\log x+O_{\delta,C}(1).
\]
With merely \(E(x)=o(x)\), the error is \(o(\log x)\) instead of necessarily \(O(1)\), by splitting the integral at a fixed large threshold.

### Exercises and conceptual checks

1. Prove \(\sum_{n\geq1}(2n-1)^{-2}\) converges without calculating its value.
2. For \(a_n=(-1)^{n-1}\), compute \(A_n\) and obtain an explicit bound on the alternating harmonic tail starting after N.
3. Let \(a_n\) repeat \(1,1,-2\). Explain why \(\sum a_n/n\) converges and \(\sum |a_n|/n\) diverges.
4. Derive \(\sum_{n\leq x} \log n=x\log x-x+O(\log x)\) from the integral version of partial summation, without invoking Stirling's formula.
5. Give an example where \(E(x)=o(x)\) but \(E(x)\) is not bounded; explain why the distinction matters for a weighted estimate.

### Sources and further reading

- NIST Digital Library of Mathematical Functions, [Euler Products and Dirichlet Series](https://dlmf.nist.gov/27.4), for the analytic context in which these estimates will be used.
- Terence Tao, [Elementary multiplicative number theory](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/), for quantitative summation and multiplicative number theory.
- Wikipedia background: [Series (mathematics)](https://en.wikipedia.org/wiki/Series_(mathematics)), [Integral test for convergence](https://en.wikipedia.org/wiki/Integral_test_for_convergence), [Summation by parts](https://en.wikipedia.org/wiki/Summation_by_parts), [Dirichlet's test](https://en.wikipedia.org/wiki/Dirichlet%27s_test), [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation).
