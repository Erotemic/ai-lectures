# 012000 — Infinite Sums of Functions: Uniform Series and the First Power Series

**Track:** Analysis from First Principles. **Background:** numerical series, uniform convergence, continuity and integration. **Theme:** an infinite sum is a limit of partial-sum functions, and its algebraic power depends on controlling the tails uniformly.

<!-- BEGIN SPOKEN LECTURE -->

# Infinite Sums of Functions: Uniform Series and the First Power Series

An infinite sum of numbers can be approached through partial sums. Add the first term, then the second, and keep going. If those totals settle toward a finite limit, we say the series converges.

Now imagine that every term is a function. We could add a sequence of waves to build a sound, a sequence of corrections to build an approximate solution, or a sequence of powers to build a familiar curve. At each input, the addition creates an ordinary numerical series. But the entire sum is intended to be one function, valid across a domain.

This introduces the same question we faced for sequences of functions. Does the infinite construction behave well at each individual input, or does one error estimate control the whole domain? The difference determines whether the sum can be trusted to preserve continuity and whether integration and differentiation can be performed one term at a time.

## The partial sum is the real object

Start with a list of functions: the first term function, the second term function, and so on. For each positive integer N, form a partial-sum function by adding the first N terms at every input. The purported infinite sum is defined to be the limit of these partial-sum functions wherever that limit exists.

This definition avoids pretending that infinitely many additions happen all at once. At any finite stage we have an ordinary function. Convergence describes what happens to those ordinary functions as the stage grows.

At a fixed input, convergence is just convergence of a numerical series. A function series converges uniformly when its partial-sum functions converge uniformly on the chosen domain. Once that happens, the uniform-limit theorems become available. If every term is continuous, every partial sum is continuous; therefore the uniform sum is continuous.

If every term is Riemann integrable on a closed interval, then the partial sums are integrable, and a uniformly convergent series may be integrated term by term. The integral of the sum equals the limit of the finite sums of integrals. We have turned a potentially dangerous exchange of an infinite limit and an integral into an application of a theorem already proved.

The challenge is finding a practical test for uniform convergence without first knowing the exact sum.

## A tail must become small everywhere

For numerical series, a standard convergence test asks whether every sufficiently far-out tail is small. Take two late partial sums and subtract them. Their difference consists of the terms added between those stages. If all such tails become arbitrarily small, the partial sums are Cauchy.

For a series of real- or complex-valued functions, the uniform Cauchy criterion asks for more. Given a positive tolerance, find one index after which any finite tail sum has magnitude below that tolerance at every input. The threshold depends on the tolerance, but neither on the input nor on the number of later terms included in the tail.

Because real and complex numbers are complete, uniformly Cauchy partial sums converge at each input; the common tail estimate then upgrades pointwise convergence to uniform convergence. This is the basic engine behind many convergence tests.

It is often easier to control the sizes of the individual terms than to estimate the entire tail directly. The triangle inequality says the magnitude of a tail sum is no more than the sum of the magnitudes of the individual terms. If the individual magnitudes are themselves bounded by a suitable numerical sequence, one common numerical tail will control all inputs.

## The Weierstrass M-test

Here is the precise tool. Suppose that, for each term number n, we have a nonnegative number M at n which bounds the magnitude of the nth function at every point of the domain. Suppose further that the numerical series obtained by adding all these bounds converges.

Then the original series of functions converges absolutely at every input and uniformly across the entire domain. This is the Weierstrass M-test.

The proof is a single useful estimate. Take any far-out finite tail of our function series. Its magnitude is at most the sum of the corresponding bounds M. Since the numerical series of bounds converges, we can make all such tail sums small by choosing the starting index sufficiently large. That bound makes no reference to the input. Thus the function series is uniformly Cauchy and consequently uniformly convergent.

The M-test is sufficient, not necessary. If the proposed numerical bounds fail to form a convergent series, we have not proved that our function series diverges. We have only failed to certify it with this particular test. Cancellation between positive and negative terms can make a function series converge uniformly even when a sum of absolute-value bounds diverges.

A useful example of that distinction comes from the alternating series with nth term equal to the nth power of x divided by n, and alternating signs, on the interval from zero to one. At each fixed x, the terms decrease in magnitude, so the alternating-series estimate bounds the remainder after N terms by one over N plus one. The same remainder bound works for every x in the interval, so the convergence is uniform.

But at x equal to one, the series of absolute magnitudes becomes the harmonic series, which diverges. Thus the original alternating series is uniformly convergent on the interval even though it is not absolutely convergent at every point. Demanding an M-test proof would have overlooked this valid uniform convergence.

## A geometric series of functions

Now consider the familiar geometric expression: one plus x plus x squared, plus x cubed, and so on. At any fixed real x whose magnitude is less than one, the numerical geometric series converges to one divided by one minus x.

For a domain-wide estimate, pick any fixed number r strictly between zero and one. Restrict x to the interval from minus r to r. The magnitude of the nth power term is at most r to the nth power. The numerical geometric series in r converges, so the M-test says our function series converges uniformly on that whole smaller interval.

We can say more than that it converges. The remainder after the term of degree N has magnitude at most r to the power N plus one divided by one minus r. That gives a concrete error bound. It tells us exactly how many terms suffice for an intended accuracy, uniformly across the selected interval.

What if we expand the domain to all x strictly between zero and one? At each fixed x, the sum still exists and equals one divided by one minus x. But the convergence is not uniform on this entire open interval. The limiting function becomes arbitrarily large as x approaches one, while each finite partial-sum function stays bounded there. A uniform limit of bounded functions would have to be bounded, so uniform convergence is impossible.

There is no contradiction. The geometric series converges uniformly on every closed interval that stops short of one, and it converges pointwise throughout the open interval. The missing ingredient for global uniform convergence is one error estimate that survives as x approaches the boundary.

## The first appearance of complex power series

A complex number has a real part and an imaginary part. Its magnitude measures its ordinary Euclidean distance from zero in the plane. The triangle inequality holds, and the complex numbers are complete under this distance. Therefore the same uniform Cauchy and M-test arguments apply to complex-valued functions.

Replace x by a complex input z. The geometric series in powers of z converges whenever the magnitude of z is less than one. For every fixed radius r less than one, the convergence is uniform on the entire closed disk consisting of points of magnitude at most r.

This is the first geometric picture behind complex analysis. The natural domain of convergence is a disk, and the useful uniform estimates hold on each smaller closed disk. The boundaries matter because a series can behave very differently exactly at the edge of its region of convergence.

More generally, a power series centered at a complex point c is an infinite sum of coefficients times powers of the difference between z and c. Its coefficients may also be complex. A power series has a radius of convergence: it converges absolutely inside that radius, uniformly on every smaller closed disk, and diverges outside the radius. At points on the boundary circle, different series can behave in different ways, so the interior theorem does not settle the boundary cases.

We can see why a disk appears without computing any special formula for the radius. Suppose the series converges at one point a positive distance R away from its center. Then the terms at that point must tend to zero and are therefore bounded. At any nearer point, rewrite each term as the corresponding term at the known convergence point multiplied by the ratio of the two distances to the appropriate power. On a closed disk whose radius is smaller than R, that ratio is bounded by one fixed number less than one. A convergent geometric bound follows, so the M-test gives absolute and uniform convergence on the smaller disk.

This argument is one of the bridges from real convergence estimates to complex-variable analysis. We have not yet defined a complex derivative. Nevertheless, we already know a great deal about where a complex power series converges and how it behaves as a continuous function.

## Integrating and differentiating the sum

If a series of continuous real-valued functions converges uniformly on a closed interval, we may integrate term by term there. With complex-valued functions on a path, analogous results follow by applying the real result to the real and imaginary components after parametrizing the path, under the usual continuity and regularity hypotheses.

Differentiation requires stronger care. Uniform convergence of the original series does not itself imply that its sum is differentiable, and it does not license differentiating every term. To justify that operation for general real function series, a standard sufficient route is to establish uniform convergence of the series of derivatives on the interval, together with convergence of the original series at one anchor point, under the regularity assumptions used in the derivative-limit theorem.

Power series have a particularly favorable structure. Strictly inside their radius of convergence, the series obtained by differentiating each power also converges uniformly on smaller closed disks. The extra factor of n from differentiating the nth power is harmless on those smaller disks because a geometric factor with ratio less than one eventually outweighs the polynomial factor n.

That last statement needs a proof, not a slogan. Choose a slightly larger disk still inside the convergence radius. Bound the original coefficients using that larger radius. Then on the smaller disk, the derivative terms are bounded by a constant times n times a geometric sequence with ratio strictly below one. That numerical series converges, so the derivative series has uniform control.

This is why power series are more than convenient shorthand. Inside their convergence disks they define functions with a robust analytic structure. The shape of the coefficients determines the radius, but the strict interior is a region where convergence, continuity, differentiation, and integration cooperate.

## What to check before exchanging a sum and an operation

When you face an infinite sum of functions, begin with the partial sums. Decide on the exact domain. Determine whether you have pointwise convergence, uniform convergence, or a stronger estimate. Then look separately at the operation you wish to interchange with the sum.

For continuity, uniform convergence of continuous partial sums suffices. For Riemann integration on a closed interval, uniform convergence of integrable partial sums suffices. For differentiation, ask for control of the derivatives or use a theorem specific to the structured series, such as a power series in the interior of its convergence disk.

Above all, do not treat convergence at every individual input as though it supplied a uniform bound. Nor should you conclude divergence just because a convenient sufficient test fails.

We now have the tools to move into the complex plane with confidence: metric limits, compact subsets, uniform estimates, and power series that behave consistently on closed disks inside their convergence region. With that foundation, the next step is to understand what it means for a function to have a complex derivative, and why that definition is much more restrictive than its real counterpart.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Uniform Cauchy criterion and M-test

For \(u_n:E\to\mathbb C\), write \(S_N(x)=\sum_{n=0}^{N}u_n(x)\). The series is uniformly Cauchy iff
\[
\forall\varepsilon>0\ \exists N\ \forall p>q\ge N\ \forall x\in E:\quad\left|\sum_{n=q+1}^{p}u_n(x)\right|<\varepsilon.
\]
Since \(\mathbb C\) is complete, uniformly Cauchy partial sums converge uniformly to a complex-valued function.

**Weierstrass M-test.** If \(|u_n(x)|\le M_n\) for all \(x\in E\), with \(M_n\ge0\) and \(\sum_nM_n<\infty\), then
\[
\sup_{x\in E}|S_p(x)-S_q(x)|\le \sum_{n=q+1}^{p}M_n\longrightarrow 0
\]
as \(q\to\infty\), uniformly in \(p>q\). Therefore \(\sum u_n\) converges uniformly and absolutely pointwise.

### Two instructive series

**Geometric series:** On \(\{z\in\mathbb C:|z|\le r\}\) with \(r<1\),
\[
\sum_{n=0}^{\infty}z^n=\frac{1}{1-z},\qquad
\left|\frac1{1-z}-\sum_{n=0}^Nz^n\right|\le\frac{r^{N+1}}{1-r}.
\]
This is not uniformly convergent on \((0,1)\), since the limit \((1-x)^{-1}\) is unbounded there but every partial sum is bounded.

**Uniform but not pointwise absolute at every point:** On \([0,1]\), \(\sum_{n=1}^{\infty}(-1)^{n+1}x^n/n\) converges uniformly because the alternating remainder is bounded by \(1/(N+1)\); at \(x=1\), \(\sum_n|(-1)^{n+1}/n|\) diverges. The M-test is not necessary.

### A complex-power-series theorem

For \(\sum_{n=0}^{\infty}a_n(z-c)^n\), there is a radius \(R\in[0,\infty]\) with absolute convergence for \(|z-c|<R\), divergence for \(|z-c|>R\), and uniform convergence on every closed disk \(|z-c|\le r<R\). Boundary points \(|z-c|=R\) require separate analysis.

If convergence holds at \(\zeta\ne c\), let \(\rho=|\zeta-c|\). The sequence \(a_n(\zeta-c)^n\) is bounded by some \(M\), and for \(r<\rho\),
\[
\sup_{|z-c|\le r}|a_n(z-c)^n|\le M(r/\rho)^n.
\]
The M-test proves absolute uniform convergence on the smaller disk.

For \(r<s<R\), the differentiated terms admit bounds of the form \(C n r^{n-1}/s^n\), summable in \(n\). This justifies termwise differentiation and yields an analytic derivative on the interior.

### Exercises and guided answers

1. **M-test.** If \(|u_n(x)|\le 4^{-n}\) for all \(x\), does \(\sum_{n=1}^\infty u_n\) converge uniformly? **Answer:** Yes; the numerical geometric bound has a finite sum.
2. **Failure of a test.** If the only available bound is \(|u_n(x)|\le 1/n\), can we conclude nonuniform convergence? **Answer:** No. A divergent majorant only means the M-test is inconclusive.
3. **Error control.** For \(|z|\le1/2\), bound the remainder after degree N in the geometric series. **Answer:** \(2^{-N}\), since \((1/2)^{N+1}/(1-1/2)=2^{-N}\).
4. **Boundary behavior.** Does uniform convergence of a power series on every \(|z|\le r<1\) prove uniform convergence on \(|z|<1\)? **Answer:** No; the geometric series is a counterexample.
5. **Interchanging derivative and sum.** Why does uniform convergence of \(\sum u_n\) alone not license \((\sum u_n)'=\sum u_n'\)? **Answer:** Uniform limits of differentiable functions need not be differentiable. Stronger derivative controls or a power-series theorem are required.

### Focused references

- [Wikipedia: Weierstrass M-test](https://en.wikipedia.org/wiki/Weierstrass_M-test) — a sufficient test for uniform convergence of function series.
- [Wikipedia: Power series](https://en.wikipedia.org/wiki/Power_series) — convergence radius, boundary behavior and termwise operations.
- [David Ash, *Complex Variables* notes, hosted at the University of South Carolina](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesMerged.pdf) — M-test and uniform convergence on closed subdisks.
- [University of Washington: Series notes](https://sites.math.washington.edu/~marshall/math_135/series.pdf) — concise proof of the M-test and power-series radius arguments.
