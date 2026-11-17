# 026500 - The Zeta Function, Its Zeros, and the Line One

**Track:** Number Theory from First Principles. **Background:** series and summation by parts, Euler products, Dirichlet characters and analytic continuation, the Cauchy and Laurent toolkit. **Aim:** prove rigorously that zeta has no zero on the line with real part one, derive its logarithmic-derivative prime series, and isolate the remaining Tauberian step before the prime number theorem.

<!-- BEGIN SPOKEN LECTURE -->

# The Zeta Function, Its Zeros, and the Line One

A single vertical line in the complex plane separates what we already know about prime numbers from the prime number theorem. The line consists of complex numbers whose real part is one. On its right, the Euler product expresses zeta in terms of all primes. On the line itself, the original sum and product stop converging absolutely. If we wish to move from Chebyshev's estimate, which says the number of primes up to x is comparable to x divided by log x, to an asymptotic formula with the correct constant one, we need to know how zeta behaves as we approach this boundary.

In particular, zeta must not vanish at any point one plus i times t with t nonzero. A zero there would create a pole in a logarithmic derivative precisely where we are trying to extract the main term from prime data. We will prove this nonvanishing statement. And then we will be precise about why it is an essential step, but not yet a proof of the prime number theorem.

## Recover a function after its series stops converging

For a complex s with real part greater than one, zeta of s is the sum over positive integers n of n to the power negative s. Write s as sigma plus i times t. The real part sigma controls the magnitude of each term, so this series converges absolutely for sigma greater than one.

We previously continued zeta beyond this half-plane by partial summation. Recall the simple device: the number of positive integers up to x is the integer part of x. The integer part equals x minus the fractional part. The fractional part always lies between zero and one. Applying summation by parts splits zeta into a rational term, s divided by s minus one, minus s times the integral from one to infinity of the fractional part of x divided by x to the power s plus one.

The integral now converges whenever sigma is positive, since its integrand is bounded by a constant times x to the negative sigma minus one. Within any smaller region bounded away from sigma equal to zero, derivatives with respect to s can also be passed into the integral: every derivative adds a power of log x, and powers of log x do not overcome a fixed positive power of decay. Thus the integral is holomorphic throughout the open right half-plane.

The only singularity introduced by this expression is the rational term at s equal to one. It is a simple pole. More precisely, as s approaches one, the product of s minus one and zeta of s approaches one. That constant, called the residue, will later determine the main coefficient in a counting formula.

This construction should be understood literally. At a point with sigma below one, we are not claiming that the original series suddenly converges there. We are using a different expression, consistent with the original series where both are defined. The identity theorem from complex analysis ensures that a holomorphic continuation cannot have two incompatible versions on a connected overlapping region.

## Put prime powers into one series

Now return briefly to the region sigma greater than one. Unique factorization gives the Euler product: zeta is the product over primes p of one divided by one minus p to the negative s. The product converges absolutely there, and none of its factors vanishes. We may take a logarithm locally and differentiate term by term. Each prime contributes not only itself but all its positive powers. After differentiation, the contribution from p to the k is log p divided by p to the k s.

Gathering these prime powers by their integer values produces the von Mangoldt function. Lambda of n equals log p if n is a positive power of a prime p, and equals zero otherwise. We obtain an exact identity: negative zeta prime over zeta equals the sum of Lambda of n over n to the s, valid for sigma greater than one.

Why keep the prime powers rather than only the primes? Because differentiation of a product naturally counts every repetition of a prime. Those repetitions make the analytic formula simpler. They also have a controlled total size: the difference between summing log p over primes and summing Lambda over prime powers is small compared with x, as follows from elementary prime-counting bounds. So a leading asymptotic for the accumulated Lambda weights will deliver the desired statement about ordinary primes.

Define psi of x as the sum of Lambda of n for n up to x. It is a nondecreasing step function: every new prime power adds a positive logarithmic weight. Partial summation turns the exact series into an integral. Negative zeta prime over zeta at s equals s times the integral from one to infinity of psi of x divided by x to the power s plus one, for sigma greater than one.

Notice the roles. The Dirichlet series is an analytic transform of a nondecreasing arithmetic quantity. Zeta's singularities will constrain that transform. But converting information about the transform back into an asymptotic for psi requires justification. That inversion is the Tauberian problem we will return to.

## The inequality whose factors cannot all be small

The key zero-free result has a short proof, but only after every convergence issue has been separated from the boundary. Work with a real sigma strictly greater than one. Since the Euler product converges absolutely, the logarithm of the magnitude of zeta at sigma plus i t can be written as a double sum over primes and positive integers k. Its terms are cosine of k times t times log p, divided by k times p to the k sigma.

This means a linear combination of such logarithms becomes a linear combination of cosines. Pick coefficients three, four, and one, using the three points sigma, sigma plus i t, and sigma plus two i t. The cosine expression becomes three plus four cosine theta plus cosine twice theta. A trigonometric identity makes it exactly twice the square of one plus cosine theta. Every term is nonnegative.

Consequently the sum of the corresponding logarithms of magnitudes cannot be negative. Exponentiate. We have an inequality that says zeta at sigma, raised to the third power, times the fourth power of the magnitude of zeta at sigma plus i t, times the magnitude at sigma plus two i t, is at least one.

Every part of this argument takes place to the right of the line. We have used absolute convergence there, where we are entitled to rearrange the prime-power sums. No step has taken a logarithm of zeta on a possible zero. The final inequality involves only magnitudes, and so we can pass to the boundary using our independently constructed analytic continuation.

## Assume a zero and watch the inequality fail

Fix t not equal to zero, and suppose for contradiction that zeta at one plus i t equals zero. Because this point is not the pole, zeta is holomorphic near it. Its Taylor series begins with a positive power of the displacement from that point. In particular, as real sigma decreases to one, the magnitude of zeta at sigma plus i t is bounded by a constant times sigma minus one. Raising that magnitude to the fourth power gives a factor bounded by a constant times the fourth power of sigma minus one.

Meanwhile zeta at sigma has a simple pole, so its third power grows like the reciprocal of the third power of sigma minus one. And zeta at sigma plus two i t stays bounded: because t is nonzero, the point one plus two i t is not the pole. It might be a zero or a nonzero regular value, but either way it is finite.

Multiply these three estimates. The combined product is bounded by a constant times sigma minus one. It therefore tends to zero as sigma decreases to one. But the Euler-product inequality says that same product is at least one for every sigma greater than one. Contradiction.

We have proved that zeta has no zeros at any point one plus i t with t nonzero. At t equal to zero, zeta has a pole, not a zero. Thus the entire line with real part one is free of zeros of the continued zeta function; the only exceptional feature is the pole at the real point one.

The proof works because of the exponents. The pole contributes three negative powers of sigma minus one, while the hypothetical zero contributes at least four positive powers. The extra positive power overwhelms the pole. The last zeta factor remains bounded. That is the reason for the particular trigonometric square. It is not a numerical coincidence.

## What we have really gained

On the region to the right of one, negative zeta prime over zeta is the prime-power Dirichlet series. Because zeta is holomorphic and does not vanish near any point of the line one except for its pole, this logarithmic derivative also has a meromorphic continuation across a small neighborhood of every point on that line. At s equal to one, negative zeta prime over zeta has a simple pole with residue one. Subtract one divided by s minus one and the remainder is holomorphic there.

Everywhere else on the line, no zero or pole interferes, so the logarithmic derivative remains holomorphic in a neighborhood. These facts give very strong control at every fixed boundary point. They are exactly the kind of boundary information used by the Wiener-Ikehara Tauberian theorem.

Here is the shape of that theorem in our situation. Suppose a Dirichlet series has nonnegative coefficients and its difference from a simple pole of residue A continues suitably and regularly to the boundary line with real part one. Under the theorem's precise hypotheses, the sum of its coefficients up to x is asymptotic to A times x. Applied to the coefficients Lambda of n and residue one, this would give psi of x asymptotic to x, and hence the prime number theorem.

But I have just stated the Tauberian theorem, not proved it. Holomorphic continuation alone does not entitle us to exchange a limit with a discontinuous counting function or to read the coefficient sum straight off a pole. Nonnegativity of Lambda matters, and proving the bridge requires a further argument. We must not hide it under the phrase standard analysis.

It is also important not to overstate the zero-free result. We have ruled out zeros exactly on the line sigma equal to one. We have not proved a quantitative zero-free strip whose width depends on the imaginary height. Such regions are needed for refined explicit error estimates. Nor have we proved the Riemann hypothesis, which concerns a different vertical line, with real part one half.

We began with Chebyshev's order-of-magnitude bounds and an Euler product that lived only to the right of one. We now possess an analytic continuation, a prime-power logarithmic derivative, a boundary inequality, and a complete contradiction proving nonvanishing on the line one. The bridge from transform to count remains open, but its input is now ready. That is a meaningful stopping point: a proof must distinguish the hypotheses it has earned from the theorem it hopes to apply.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Continuation and the pole at one

For \(\Re s>1\), partial summation gives
\[
\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\]
The second integral converges locally uniformly on \(\Re s>0\), as do the termwise derivatives, since \(\int_1^\infty x^{-1-\sigma}(\log x)^k dx=k!/\sigma^{k+1}\) for \(\sigma>0\). It gives a holomorphic correction to the simple pole. Hence
\[
\lim_{s\to1}(s-1)\zeta(s)=1.
\]

### Logarithmic derivative, Mangoldt weights, and partial summation

For \(\Re s>1\), absolute local uniform convergence of the Euler-product logarithm yields
\[
\log\zeta(s)=\sum_p\sum_{k\ge1}\frac{1}{k p^{ks}},\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{p}\sum_{k\ge1}\frac{\log p}{p^{ks}}=
\sum_{n\ge1}\frac{\Lambda(n)}{n^s}.
\]
With \(\psi(x)=\sum_{n\le x}\Lambda(n)\),
\[
-\frac{\zeta'(s)}{\zeta(s)}=s\int_1^\infty\psi(x)x^{-s-1}\,dx
\quad(\Re s>1).
\]
From elementary estimates \(\sum_{p^k\le x,\ k\ge2}\log p=O(\sqrt{x}\log^2 x)\), hence \(\psi(x)=\vartheta(x)+o(x)\). In particular \(\psi(x)\sim x\) implies \(\vartheta(x)\sim x\), and standard partial summation gives \(\pi(x)\sim x/\log x\).

### Complete proof of the zero-free boundary

For \(\sigma>1\), the positive coefficients of \(\log|\zeta|\) and the identity
\[
3+4\cos\theta+\cos(2\theta)=2(1+\cos\theta)^2\ge0
\]
give, for every real \(t\),
\[
\boxed{\zeta(\sigma)^3\,|\zeta(\sigma+it)|^4\,|\zeta(\sigma+2it)|\ge1.}
\]
Suppose \(t\ne0\) and \(\zeta(1+it)=0\). Holomorphy near \(1+it\) yields \(|\zeta(\sigma+it)|=O(\sigma-1)\). Holomorphy near \(1+2it\) yields \(|\zeta(\sigma+2it)|=O(1)\), and the simple pole at one yields \(\zeta(\sigma)=O((\sigma-1)^{-1})\). The product on the left is \(O(\sigma-1)\to0\), a contradiction. At \(t=0\) there is a pole rather than a zero.

### Exactly where the prime number theorem remains unproved

\(F(s)=-\zeta'(s)/\zeta(s)\) has nonnegative Dirichlet coefficients \(\Lambda(n)\). The function
\[
F(s)-\frac{1}{s-1}
\]
continues holomorphically through a neighborhood of each point of the line \(\Re s=1\), using the zero-free result and the residue-one pole at one. A **Tauberian theorem** such as Wiener-Ikehara (with its stated regularity and positivity assumptions) then gives \(\psi(x)\sim x\). This manuscript has **not** proved Wiener-Ikehara, so it has not completed the prime number theorem. The theorem provides the planned bridge, not an already-derived conclusion.

### Exercises

1. Derive \(-\zeta'/\zeta\) by differentiating the absolutely convergent Euler-product logarithm. Explain why this is not initially valid at \(\Re s=1\).
2. Verify the trigonometric identity and its minimum value. Why do coefficients \(3,4,1\) give a contradiction from a hypothetical simple zero?
3. Show that if \(f\) is holomorphic near \(s_0\) and vanishes there, then \(f(s_0+h)=O(|h|)\). What happens if the zero has order at least two?
4. Prove \(\sum_{p^k\le x,\ k\ge2}\log p=O(\sqrt{x}\log^2 x)\) using only \(\pi(y)\le y\) and bounds on the possible exponents.
5. Explain, in your own words, which theorem would still be needed to turn \(F(s)=1/(s-1)+\text{regular}\) into a conclusion about \(\sum_{n\le x}\Lambda(n)\).

### Reading and source notes

- Ben Green, [The prime number theorem, chapter 8](https://people.maths.ox.ac.uk/greenbj/papers/primenumbers.pdf), section on zero-free boundary and the trigonometric inequality.
- Harvard Mathematics, [Prime Number Theorem lecture notes](https://abel.math.harvard.edu/archive/113_fall_01/113pnt.pdf), for the half-plane continuation and boundary argument.
- B. E. Petersen, [Prime Number Theorem](https://www2.math.upenn.edu/~kazdan/609S09/PrimeNoTh/LectureNotes-Petersen1996.pdf), section on zeta along the line \(\Re s=1\).
- Wikipedia: [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function), [Von Mangoldt function](https://en.wikipedia.org/wiki/Von_Mangoldt_function), [Wiener-Ikehara theorem](https://en.wikipedia.org/wiki/Wiener%E2%80%93Ikehara_theorem), [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem).
