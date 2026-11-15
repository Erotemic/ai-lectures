# 011000 — Uniform Convergence: When Limits Preserve Structure

**Track:** Analysis from First Principles. **Background:** sequences, continuity, compactness, derivatives and Riemann integration. **Theme:** the order of quantifiers determines which operations survive the limit of functions.

<!-- BEGIN SPOKEN LECTURE -->

# Uniform Convergence: When Limits Preserve Structure

Imagine constructing a curve by successive approximations. Each approximation is smooth and easy to study. As you increase the level of detail, the curves appear to settle into a final shape. Can you trust that final shape to be continuous? Can you integrate it by integrating the approximations? Can you differentiate it the same way?

The answer depends on what it means for the functions to converge. We already know how numbers converge. For functions, however, there is an extra choice. We can look at one input location at a time and ask whether the approximation becomes accurate there. Or we can demand that a single approximation index makes the error small everywhere at once.

These statements sound close in ordinary language, but they are mathematically different. The stronger one is called uniform convergence. Much of analysis consists of knowing exactly when that stronger form of control is available and what it allows us to conclude.

## A separate clock at every input

Let a sequence of functions all have the same domain, and suppose we have a proposed limit function. Pointwise convergence says the following. Choose any input. Then, however small an error tolerance you request, sufficiently late functions evaluate near the limiting value at that input.

What counts as sufficiently late can depend on the input. For one position the tenth approximation may be enough. For another, we might need the millionth. If the bad region shifts or shrinks as the index grows, every fixed input may eventually be accurate even while somewhere on the domain a large error remains.

Here is a concrete example. On the closed interval from zero to one, define the nth function to be x raised to the nth power. At any fixed input strictly smaller than one, repeated multiplication by x drives the value toward zero. At x equal to one, every term equals one. So the pointwise limit is zero on the interval below one, but equals one at the endpoint.

Every approximating function is continuous. The limit is not continuous at one. As x approaches one from below, the limit remains zero, then jumps to one at the endpoint.

The example shows that a pointwise limit of continuous functions need not be continuous. It is not a technical exception. It is what can happen whenever our approximation schedule is allowed to depend separately on each input.

To see the problem in the example, look near one. For every n there are inputs strictly below one but so close to it that x to the nth power remains near one. The location of the large error moves toward the endpoint as n increases. Fixing an input hides that moving error; looking across the whole interval exposes it.

## One clock for the entire domain

Uniform convergence changes the order of the choices. Given an error tolerance, we must find one index N such that every later function is within that error of the limit at every input in the domain. The same N works everywhere.

If our functions are real-valued, we can measure the worst absolute error across the domain. Uniform convergence means that this worst error tends to zero. When the supremum exists as a finite number, it gives the distance used in the supremum metric on functions.

The x-to-the-n example fails this test on the closed interval. For any n, the error below one can be made arbitrarily close to one by choosing x sufficiently close to one. So the supremum error is one, not something tending to zero. Pointwise convergence occurs, but uniform convergence does not.

Now restrict the domain to the closed interval from zero to three quarters. The nth power is then at most three quarters to the nth power. This bound is independent of the input and tends to zero. We have uniform convergence on the smaller interval.

The functions have not changed; only the domain on which we demand a common bound has changed. This distinction will become essential for complex power series. A series can converge uniformly on every compact region strictly inside a disk without converging uniformly on the entire disk or near its boundary.

## Why continuous approximations now stay continuous

Suppose every approximating function is continuous at a chosen input point, and suppose the functions converge uniformly to f. We want to prove that f is continuous there.

Request any positive output error. Uniform convergence lets us choose one approximating function whose values are within one third of that error from f, at every input. Freeze that approximation. Since it is continuous at the chosen point, there is a neighborhood in which its own output changes by less than one third of the error.

Now compare the value of f at a nearby input with its value at our chosen point. Travel through the frozen approximation at the nearby input, then across the approximation's local change, then back to f at the chosen point. By the triangle inequality, the total difference is less than three thirds of the requested error.

That proves continuity. The critical move was choosing the approximation before varying the input. Pointwise convergence could not have guaranteed that the same approximation worked at both points.

The conclusion does not require a compact domain. If the functions are defined on any metric space and take values in another metric space, uniform convergence of continuous functions preserves continuity, as long as convergence is interpreted using the output metric. Compactness often helps us establish uniform estimates, but it is not an additional hypothesis of this particular theorem.

## A complete space of continuous functions

On a compact real interval, the supremum distance between two continuous functions is finite. If a sequence of continuous functions is Cauchy in this distance, then for sufficiently late indices any two functions are uniformly close. At each input their numerical values form a Cauchy sequence and hence converge in the real numbers.

Passing to the pointwise limits while retaining the uniform Cauchy estimate gives uniform convergence. The continuity theorem we just proved shows that the resulting function is continuous. We have therefore produced a limit within the same space.

So continuous real functions on a compact interval form a complete metric space under supremum distance. We can take Cauchy sequences of entire functions and remain inside the class of continuous functions.

This formulation is useful because it gives a way to prove convergence without guessing the limiting function first. Establish uniform Cauchy control, use completeness, and the limiting function follows.

## What about integration?

For Riemann integration on a closed interval, uniform convergence is strong enough to pass the limit through the integral, provided the approximating functions are Riemann integrable.

Let the nth function approach f uniformly. The accumulated difference between their integrals cannot exceed the interval length times the largest absolute difference between the functions. Once the function error is uniformly small, its integrated effect is also small.

There is one more point to justify: the limit f itself must be Riemann integrable. Uniform convergence of Riemann-integrable functions ensures this. One way to see it uses Darboux sums. Choose a late approximation close to f everywhere; then choose a partition whose upper and lower sums for that approximation are close. The corresponding sums for f differ by no more than twice the uniform error times the interval length. This makes f integrable.

We can therefore conclude that the integral of the limit equals the limit of the integrals. The interval length appears because integration accumulates error across a domain. A small worst-case error everywhere produces a small total error.

Pointwise convergence alone does not justify the same exchange. For a counterexample, imagine tall narrow triangular spikes on the interval from zero to one. Each spike has height proportional to n and width proportional to one over n, so its area stays fixed. Place the spike increasingly close to zero while ensuring its support lies strictly above zero. At every fixed input, the spike eventually disappears, yet each integral remains the same positive number. The pointwise limit is zero and its integral is zero, so the limit and the integral do not agree.

This spike example separates pointwise convergence from integration without invoking any advanced integration theory. Under the Riemann integral, every individual spike function is perfectly legitimate.

## Why differentiation is more delicate

Now suppose every approximating function is differentiable. Even if the approximations converge uniformly, the limit need not be differentiable. Consider the smooth functions given by the square root of x squared plus one over n, on the interval from minus one to one. They converge uniformly to the absolute value of x, because the difference is bounded by one over the square root of n.

Each approximation is differentiable everywhere. The absolute-value limit has a corner at zero and is not differentiable there. Uniform control of function values does not guarantee uniform control of slopes. Very small vertical errors can hide very sharp changes over short horizontal scales.

The failure is not an invitation to abandon limit interchange. It tells us what additional information is needed. If each approximating function has a continuous derivative on a closed interval, if those derivatives converge uniformly, and if the function values converge at even one fixed input, then the original functions converge uniformly to a differentiable limit whose derivative is the uniform limit of the derivatives.

Why is one fixed input enough? The Fundamental Theorem of Calculus reconstructs each function at any other input as its value at the fixed point plus the integral of its derivative. The values at the fixed point converge by assumption. Uniform convergence of derivatives lets us pass the limit through those integrals. The result is a function with a continuous derivative equal to the limiting derivative.

The derivative hypothesis is doing the real work. The original functions do not have to be uniformly close in advance; the derivative bound and one anchor value create that control.

## A useful warning about logical order

It is tempting to hear a sentence like “for each input, eventually the approximation is accurate” and silently turn it into “eventually the approximation is accurate for every input.” Mathematics does not permit that exchange of words. In the first statement, the required index may vary with the input. In the second, one index must control all inputs simultaneously.

The two sentences differ only in the order of their quantifiers, yet one allows the x-to-the-n counterexample and the other forbids it. Uniform convergence is a place where logical precision has immediate geometric consequences.

This also explains a common proof strategy. If you want to swap an infinite limit with another operation, first determine how the operation reacts to a controlled error. For evaluation at a point, pointwise control may be enough. For continuity at nearby points, a common local approximation matters. For a definite integral, the total error is bounded by length times worst error. For differentiation, function-value errors alone do not control difference quotients.

The next natural object is an infinite sum of functions. We will no longer be given an arbitrary sequence of approximations; instead, each approximation will add another term to a running total. Uniform convergence then becomes the tool for deciding whether that infinite sum defines a continuous function, whether we may integrate it term by term, and why power series behave so well strictly inside their radius of convergence.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Quantifier distinction

For functions \(f_n:E\to\mathbb R\):

**Pointwise:** \(\forall x\in E\;\forall\varepsilon>0\;\exists N=N(x,\varepsilon)\;\forall n\ge N:\ |f_n(x)-f(x)|<\varepsilon.\)

**Uniform:** \(\forall\varepsilon>0\;\exists N=N(\varepsilon)\;\forall n\ge N\;\forall x\in E:\ |f_n(x)-f(x)|<\varepsilon.\)

If the suprema are finite, uniform convergence is equivalent to \(\|f_n-f\|_\infty\to0\). For general unbounded functions, use the quantified definition or permit the supremum to be \(+\infty\).

**Continuity:** Uniform convergence of \(f_n:E\to Y\), where \(Y\) is metric and each \(f_n\) continuous, implies \(f\) continuous. Proof: choose \(N\) with \(d_Y(f_N(z),f(z))<\varepsilon/3\) for all \(z\), then use continuity of \(f_N\) near the chosen point.

**Riemann integration:** For Riemann-integrable \(f_n:[a,b]\to\mathbb R\) with \(f_n\to f\) uniformly, \(f\) is Riemann integrable and \(\int_a^b f=\lim_n\int_a^b f_n\). Estimate:
\[
\left|\int_a^b(f_n-f)\right|\le(b-a)\|f_n-f\|_\infty.
\]
For integrability, if \(\|f-f_N\|_\infty<\eta\), then for any partition \(P\), \(U(f,P)-L(f,P)\le U(f_N,P)-L(f_N,P)+2\eta(b-a)\).

**Derivative theorem (sufficient conditions):** Suppose \(f_n\in C^1([a,b])\), \(f_n'(x)\to g(x)\) uniformly and \(f_n(x_0)\to c\) for some \(x_0\in[a,b]\). Then \(f_n\to f\) uniformly, where \(f(x)=c+\int_{x_0}^x g(t)\,dt\), and \(f'=g\) in the interior. The continuity of \(g\) comes from uniform convergence of continuous \(f_n'\).

### Counterexamples with exact estimates

- \(f_n(x)=x^n\) on \([0,1]\): pointwise limit \(f(x)=0\) for \(0\le x<1\), \(f(1)=1\); \(\sup_{x\in[0,1]}|f_n(x)-f(x)|=1\). On \([0,r]\) with \(r<1\), the same supremum is \(r^n\to0\).
- \(f_n(x)=\sqrt{x^2+1/n}\) on \([-1,1]\): \(f_n\to|x|\) uniformly since \(0\le\sqrt{x^2+1/n}-|x|\le1/\sqrt n\); every \(f_n\in C^1\), but \(|x|\) is not differentiable at zero.
- **Shrinking spikes:** Let \(f_n\) be the tent of base \([1/(n+1),3/(n+1)]\) and height \(n+1\), centered at \(2/(n+1)\). For all sufficiently large \(n\), support lies in \((0,1]\). For each \(x\in[0,1]\), \(f_n(x)\to0\) eventually; \(\int_0^1f_n=1\) for \(n\ge2\).

### Exercises and guided answers

1. **Order of quantifiers.** Explain why choosing a different \(N\) for each \(x\) proves only pointwise convergence. **Answer:** It does not produce a single bound valid across all inputs.
2. **Domain effect.** Is \(x^n\to0\) uniformly on \([0,0.9]\)? **Answer:** Yes, \(\sup|x^n|=0.9^n\to0\).
3. **Integral control.** If \(\|f_n-f\|_\infty\le 0.01\) on \([2,5]\), how far apart can their integrals be? **Answer:** At most \(3(0.01)=0.03\).
4. **Differentiation trap.** If \(f_n\to f\) uniformly and all \(f_n\) differentiable, must \(f\) be differentiable? **Answer:** No; \(f_n(x)=\sqrt{x^2+1/n}\) is a counterexample.
5. **Enough derivative control.** What two hypotheses beyond differentiability suffice in the stated \(C^1\) theorem? **Answer:** Uniform convergence of the derivatives and convergence of values at one fixed input.

### Focused references

- [Wikipedia: Uniform convergence](https://en.wikipedia.org/wiki/Uniform_convergence) — quantifiers, continuity, integration, differentiation, counterexamples.
- [University of Notre Dame: Uniform Convergence](https://www3.nd.edu/~math/restricted/CourseArchive/300Level/366/3662001S/Lectures/02.UniformConvergence.pdf) — compact lecture notes with examples and interchange questions.
- Stephen Abbott, *Understanding Analysis*, the uniform convergence chapter.
