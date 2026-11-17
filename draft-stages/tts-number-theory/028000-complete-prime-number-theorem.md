# 028000 - The Prime Number Theorem, from Zeta to Counting Primes

**Track:** Number Theory from First Principles. **Background:** 017000 (prime-power Dirichlet series), 023000 (Chebyshev bound), 026500 (nonvanishing on the line one), 026750 (fully proved Newman Tauberian theorem). **Aim:** prove \(\psi(x)\sim x\), \(\vartheta(x)\sim x\), and \(\pi(x)\sim x/\log x\) without assuming an unstated inversion theorem or global zero-free region.

<!-- BEGIN SPOKEN LECTURE -->

# The Prime Number Theorem, from Zeta to Counting Primes

Here is one of the central results in mathematics: as x grows, the number of prime numbers no greater than x is approximately x divided by the natural logarithm of x, with the ratio of the two quantities approaching one. The statement is simple enough to describe to someone who has just learned what a prime number is. A proof, however, has led us through prime factorization, logarithms, infinite series, complex functions, and a theorem about recovering a limit from a Laplace transform.

We are now ready to assemble those pieces. Our task is not to wave at the zeta function and announce that a boundary property makes the asymptotic follow. We have already proved the zero-free boundary, and the previous analytic lecture proved the needed Tauberian theorem. Today we will verify every hypothesis for the actual arithmetic function, recover the prime-power count, and then remove both prime-power weights and logarithmic weights.

The prime number theorem was proved independently by Jacques Hadamard and Charles-Jean de la Vallée Poussin in 1896. Our route uses a later short analytic argument associated with Donald Newman, presented by Don Zagier. The historical distinction matters: the theorem is much older than the particular proof device we are using.

## Count primes in three increasingly convenient ways

Let pi of x be the number of primes at most x. This is the ordinary count we ultimately want. The first weighted count, often called theta of x, adds the logarithm of each prime at most x. The second weighted count, psi of x, adds the von Mangoldt function for every integer at most x. For a prime power, the von Mangoldt function equals the logarithm of that prime; for an integer that is not a prime power, it is zero.

Psi includes primes, squares of primes, cubes of primes, and so forth. Theta includes only the first powers. Why work with psi when it counts more than we need? Because the logarithmic derivative of zeta equals the Dirichlet series of the von Mangoldt function. Its analytic structure is therefore directly related to psi.

Both theta and psi are nondecreasing: as x passes another prime or prime power, they receive a positive contribution. And the earlier Chebyshev lecture gave us a bound of the form psi of x is at most a fixed constant times x. This upper bound is far weaker than our final goal, but is precisely enough to make the next transform bounded.

We will prove psi of x divided by x approaches one. After that, the path to pi of x is elementary.

## Put prime powers on a logarithmic clock

The prime number theorem concerns numbers x that go to infinity. Introduce a new time variable t by writing x as exponential of t. Define q of t to be psi of exponential of t, divided by exponential of t. In this new variable the desired assertion becomes simply that q of t approaches one as t grows.

The Chebyshev bound tells us q is bounded. It is also nonnegative and locally integrable. It jumps whenever exponential of t passes a prime power, but on any finite interval there are only finitely many such jumps.

Define f of t to be q of t minus one. Our goal is to prove f tends to zero. The Tauberian theorem from the previous lecture, however, will first prove something different: the ordinary improper integral of f converges. We must not conflate these conclusions. A function can have a convergent integral while occasionally taking large values. The final monotonicity argument will close that gap for this particular f.

Now form the Laplace transform of f for complex z with positive real part. It is the integral, from zero to infinity, of f of t times exponential of negative z t. Split f into q minus one. The integral of the constant one gives one over z. The q term has a direct interpretation in the original x variable.

Replace exponential of t by x. Because dt equals dx divided by x, the integral of q with its damping becomes the integral from one to infinity of psi of x divided by x to the power z plus two. The series for the von Mangoldt function lets us evaluate this exactly. Replace psi of x by the sum of Lambda of n for integers n no larger than x, and interchange sum and integral. The interchange is legitimate for positive real part of z because the corresponding Dirichlet series converges absolutely there.

For each n, the integral from n to infinity of x to the power negative z minus two equals n to the power negative z minus one divided by z plus one. Summing gives negative zeta prime over zeta at one plus z, divided by one plus z.

Thus the Laplace transform G of f equals negative zeta prime over zeta, evaluated at one plus z and divided by one plus z, and then minus one divided by z. This explicit formula is the bridge. Everything on the right has already been developed in the course.

## Check the analytic continuation at every boundary point

Our Tauberian theorem requires G to extend holomorphically across each point of the imaginary axis. Let us verify that without omitting the point zero, where a pole is hiding.

Recall that zeta has a simple pole at s equal to one, with residue one. Consequently negative zeta prime over zeta has a simple pole there, also with residue one. Write that logarithmic derivative as one over s minus one plus a function B that is holomorphic near one.

Set s equal to one plus z. The singular term becomes one over z. Substitute this expression into our transform G. The apparent one-over-z divergence cancels exactly against the one-over-z term that came from subtracting the constant function one. When simplified, the result is B at one plus z minus one, all divided by one plus z. This is holomorphic at z equal to zero.

What happens at another point on the imaginary axis, say z equal to i t with t nonzero? Then s equals one plus i t. The zero-free theorem in lecture 026500 says zeta is nonzero there. Because it is also holomorphic there, its logarithmic derivative is holomorphic in a neighborhood. The denominator one plus z is nonzero, and the separate term one over z is holomorphic since z is not zero. Thus G continues holomorphically across this point too.

To the right of the imaginary axis, the Euler product and absolutely convergent Dirichlet series already define G. So we have a consistent holomorphic continuation to an open region containing the entire closed right half-plane. We did not need a fixed-width strip to the left, or a quantitative bound on how rapidly zeta grows at great imaginary heights. The previous lecture's contour proof was designed to require only these local boundary neighborhoods.

All Tauberian hypotheses are now checked: f is bounded and locally integrable, and its Laplace transform has the required continuation. Therefore the ordinary integral of q of t minus one, from zero to T, converges to a finite limit as T tends to infinity.

This is the precise analytic consequence. The remaining step uses the arithmetic origin of q.

## Turn convergent averages into a pointwise limit

If an improper integral converges, then the integral of its integrand over any fixed-length interval far out on the time axis approaches zero. Choose any positive length a. The integral of q between t and t plus a therefore approaches a. The same is true between t minus a and t. These statements follow by subtracting two late partial integrals; no pointwise convergence has been assumed.

Now use the fact that psi is nondecreasing. If we move forward from t by h, psi of exponential of t plus h is at least psi of exponential of t. The new denominator is exponential of h times as large. Therefore q at t plus h is at least exponential of negative h times q at t.

Integrate this inequality from h equal to zero to h equal to a. The left side is the forward interval average, which approaches a. The right side is q of t multiplied by one minus exponential of negative a. This shows that the eventual upper limit of q is no greater than a divided by one minus exponential of negative a.

For the lower limit, look backward. If h lies between zero and a, monotonicity says psi of exponential of t minus h is no greater than psi of exponential of t. After accounting for the denominator, q at t minus h is at most exponential of h times q at t. Integrate backward over that interval. The integral approaches a, and it cannot exceed q of t multiplied by exponential of a minus one. Thus the eventual lower limit of q is at least a divided by exponential of a minus one.

We have trapped the possible long-term values of q between two expressions. This works for every fixed positive a. Let a decrease to zero. Both expressions approach one, as the first-order approximation to the exponential shows. Therefore the upper and lower limits of q both equal one.

So q of t approaches one. Translating back from t to x, we have proved psi of x divided by x approaches one. This is the weighted prime-power form of the prime number theorem. No part of the argument assumed that q was continuous, and no unjustified interchange of the limits a going to zero and t going to infinity occurred: first fix a, take the large-time upper and lower limits, and only then let a shrink.

## Remove the extra prime powers

Psi counts all prime powers; theta counts primes only. What is the size of their difference? Every extra term comes from a prime power p squared or higher no larger than x. Such a prime p cannot exceed the square root of x.

Fix one such prime p. There are at most log x divided by log p positive exponents k for which p to the k is at most x. Every corresponding von Mangoldt weight is log p. Their total, even including the first power, is at most log x. There are at most the square root of x primes we could be considering. Therefore psi of x minus theta of x is between zero and a constant times the square root of x times log x.

That error is small compared with x: square root of x times log x divided by x tends to zero. Since psi of x is asymptotic to x, theta of x is also asymptotic to x.

This step does not require any new facts about the spacing of primes. It uses only the elementary observation that higher powers must come from relatively small bases.

## Remove the logarithmic weights

Theta of x adds log p for each prime p at most x. Pi of x simply adds one. We can recover the unweighted count by summation by parts.

The exact formula says pi of x equals theta of x divided by log x, plus the integral from two to x of theta of t divided by t times the square of log t. It is the discrete-to-continuous integration-by-parts identity applied to the prime jumps.

Because theta of x is asymptotic to x, the first term is asymptotic to x divided by log x. We need to check the correction integral is smaller. The Chebyshev bound theta of t at most a constant times t makes the correction at most a constant times the integral from two to x of one over log t squared.

Split this integral at square root of x. The first piece has length no more than square root of x and its denominator is bounded below by a positive constant. It is therefore of order square root of x. On the second piece, log t is at least half log x, so the integrand is at most four over log x squared. Its contribution is at most four x over log x squared. Both quantities are small compared with x divided by log x.

The correction is therefore negligible in the leading asymptotic. We conclude that pi of x is asymptotic to x divided by log x. This is the prime number theorem itself.

## What the theorem does, and does not, predict

The result says the ratio of the actual prime count to x divided by log x approaches one. It does not assert that the difference is always small in absolute terms. Both functions grow without bound; even a relative error tending to zero can correspond to a substantial numerical discrepancy.

The theorem also implies that the n-th prime is asymptotic to n times log n. To see the idea, set x equal to the n-th prime in the counting formula and then compare log of the n-th prime with log n. The logarithm changes sufficiently slowly that the ratios line up. The companion gives the exact limiting calculation.

Another consequence is that for every fixed positive fraction epsilon, every sufficiently large interval from x to one plus epsilon times x contains at least one prime. Apply the asymptotic count at both endpoints: the expected difference is asymptotically epsilon times x divided by log x, which is positive and grows. This says nothing, by itself, about intervals whose relative width shrinks with x. That stronger type of question requires more precise estimates.

We have not proved the Riemann hypothesis, a quantitative zero-free region, or a numerical error term for prime counting. Our proof uses nonvanishing only on the line with real part one. That weaker boundary fact, combined with a Tauberian theorem and monotonicity, is enough for the leading asymptotic.

## The endpoint of a long chain

There is something satisfying about the structure of this proof. Ordinary prime factorization allowed the Euler product. The Euler product produced the logarithmic derivative and the von Mangoldt weights. Complex analysis continued zeta and proved its zero-free boundary. Chebyshev's elementary estimate made the normalized prime-power count bounded. Newman's contour argument then recovered convergence of an ordinary integral from a transform. Finally, monotonicity, an elementary prime-power estimate, and summation by parts converted that convergence into the count we wanted.

Every link has a job. If we omit nonvanishing, the transform may have boundary poles. If we omit boundedness, the Tauberian theorem is unavailable. If we omit monotonicity, a convergent average need not force a pointwise limit. If we omit the prime-power and logarithmic comparisons, we have proved a theorem about psi, not yet about the number of primes.

We can now regard the prime number theorem as a proved result in this course, rather than a destination marked on the horizon. Further analytic number theory asks much more delicate questions about errors, zeros off the line, primes in narrow intervals, and primes in arithmetic progressions. But their starting point is the result established here: the primes thin out at the logarithmic rate, and the leading coefficient is exactly one.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Inputs from completed lectures

- \(\psi(x)=\sum_{n\le x}\Lambda(n)=O(x)\) and \(\psi\) is nondecreasing (023000).
- \(A(s):=-\zeta'(s)/\zeta(s)=\sum_{n\ge1}\Lambda(n)n^{-s}\) for \(\Re s>1\) (017000).
- \(\zeta\) has a simple pole at \(s=1\) of residue one, and has no zeros on \(\Re s=1\) (026500).
- Newman's bounded-function Tauberian theorem has been **proved**, not merely cited (026750).

### Transform and removal of the pole

Put \(q(t)=e^{-t}\psi(e^t)\), \(f(t)=q(t)-1\). Then \(|f(t)|\le H\) for some \(H\), and for \(\Re z>0\), absolute convergence justifies
\[
\begin{aligned}
\int_0^\infty q(t)e^{-zt}\,dt
&=\int_1^\infty\psi(x)x^{-z-2}\,dx\\
&=\sum_{n\ge1}\Lambda(n)\int_n^\infty x^{-z-2}\,dx\\
&=\frac{A(1+z)}{1+z}.
\end{aligned}
\]
Therefore
\[
G(z)=\int_0^\infty f(t)e^{-zt}\,dt
=\frac{A(1+z)}{1+z}-\frac1z.
\tag{P1}
\]
Near zero write \(A(1+z)=z^{-1}+B(1+z)\) with \(B\) holomorphic. Then
\[
G(z)=\frac{B(1+z)-1}{1+z},
\]
removing the apparent pole. Near each \(it\ne0\), zeta's nonvanishing and the regularity of \(1/z\) give continuation. Together these form a holomorphic continuation to a neighborhood of \(\Re z\ge0\). Hence Newman's theorem proves
\[
\int_0^T (q(t)-1)\,dt\longrightarrow G(0).
\]

### Monotone unsmoothing, with the order of limits explicit

For every **fixed** \(a>0\), convergence implies
\[
\int_T^{T+a}q(t)\,dt\to a,
\qquad \int_{T-a}^Tq(t)\,dt\to a.
\]
Since \(\psi\) is nondecreasing, for \(0\le h\le a\),
\[
q(T+h)\ge e^{-h}q(T),\qquad q(T-h)\le e^{h}q(T).
\]
Integrating,
\[
\limsup_{T\to\infty}q(T)\le\frac a{1-e^{-a}},\qquad
\liminf_{T\to\infty}q(T)\ge\frac a{e^a-1}.
\]
Only now take \(a\downarrow0\). Both bounds approach one, yielding
\[
\boxed{\psi(x)\sim x}.
\]

### Prime powers and logarithmic summation

Let \(\vartheta(x)=\sum_{p\le x}\log p\). Every extra prime power counted by \(\psi-\vartheta\) has base \(p\le\sqrt x\), and the total weight per base is \(\le\log x\). Thus
\[
0\le\psi(x)-\vartheta(x)\le\sqrt x\log x=o(x),
\quad\boxed{\vartheta(x)\sim x}.
\]
Abel summation gives the exact identity for \(x\ge2\):
\[
\pi(x)=\frac{\vartheta(x)}{\log x}+
\int_2^x\frac{\vartheta(t)}{t(\log t)^2}\,dt.
\]
By \(\vartheta(t)=O(t)\), the integral is
\[
O\left(\int_2^{\sqrt x}1\,dt+
\int_{\sqrt x}^x\frac{4\,dt}{(\log x)^2}\right)
=O(\sqrt x+x/(\log x)^2)=o(x/\log x).
\]
Consequently \(\boxed{\pi(x)\sim x/\log x}\).

### Consequences and limitations

For the \(n\)-th prime \(p_n\), substituting \(\pi(p_n)=n\) yields \(n\sim p_n/\log p_n\), hence \(\log n/\log p_n\to1\) and \(p_n\sim n\log n\).
For each **fixed** \(\varepsilon>0\),
\[
\pi((1+\varepsilon)x)-\pi(x)
=(\varepsilon+o(1))\frac{x}{\log x}>0
\]
for all sufficiently large \(x\). Nothing in this proof gives an effective numerical error bound or a uniform assertion for \(\varepsilon=\varepsilon(x)\to0\).

### Exercises

1. Derive (P1) from the positive measure \(d\psi\), checking absolute convergence for complex \(z\) with \(\Re z>0\).
2. Explain why a singularity at \(z=it\ne0\) would invalidate Newman's theorem, even though the singularity at zero was removed.
3. Re-prove the upper and lower unsmoothing inequalities without interchanging the limits in \(T\) and \(a\).
4. Prove \(\psi-\vartheta=O(\sqrt x\log x)\) without using any nontrivial result about the distribution of primes.
5. Starting from the Stieltjes integral \(\pi(x)=\int_{2^-}^x(\log t)^{-1}\,d\vartheta(t)\), derive the Abel-summation identity exactly, including the lower endpoint.
6. Show that the theorem implies a prime in \((x,(1+\varepsilon)x]\) for fixed \(\varepsilon>0\), and explain what goes wrong if \(\varepsilon\) is allowed to depend on \(x\).

### Reading and source notes

- Don Zagier, [Newman's Short Proof of the Prime Number Theorem](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2975232/fulltext.pdf), *American Mathematical Monthly* 104 (1997), pp. 705–708. Original theorem proved independently by Jacques Hadamard and Charles-Jean de la Vallée Poussin in 1896; Newman's analytic argument is later.
- D. J. Newman, *Simple analytic proof of the prime number theorem*, *American Mathematical Monthly* 87 (1980), pp. 693–696, for the original short Tauberian method.
- Isabelle Archive of Formal Proofs, [Newman–Ingham Tauberian theorem](https://isa-afp.org/browser_info/current/AFP/Prime_Number_Theorem/Newman_Ingham_Tauberian.html), independently formalized version of the underlying analytic step.
- Wikipedia: [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem), [Chebyshev function](https://en.wikipedia.org/wiki/Chebyshev_function), [Tauberian theorems](https://en.wikipedia.org/wiki/Tauberian_theorems), [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function).
