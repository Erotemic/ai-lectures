# 018000 - Monte Carlo Integration from Scratch

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** simple integrals, expectation, variance and independent sampling. **Theme:** integration as expectation, unbiased estimators, random-number generation, standard errors and multidimensional integration.

<!-- BEGIN SPOKEN LECTURE -->

# Monte Carlo Integration from Scratch

Suppose you must calculate the area under a complicated curve. You have a formula that produces the height at any point, but not a convenient antiderivative. One strategy is to place a regular grid under the curve, evaluate the height at many predetermined points, and add the resulting strips. Another is to choose evaluation points randomly and average the heights. Why should the second strategy work at all?

The explanation is a simple connection between an integral and an expected value. If U is uniformly distributed between zero and one, then the expected value of a function of U is precisely the integral of that function from zero to one, provided the function is integrable. The integral is an ordinary average over a continuum of inputs. Random sampling is a way to approximate that average when enumerating every possible input is impossible.

We will derive the method, calculate an example by hand, measure its error, and then use it for a two-dimensional area. Along the way we will ask what the random numbers need to represent and why an honest uncertainty estimate matters as much as the estimate itself.

## The same integral, two languages

Start with the integral of x squared from zero to one. Elementary calculus gives one third. In probability language, let U be a uniform random number between zero and one. Its density is one on that interval. The expected value of U squared is the integral of x squared times that density. Since the density is one, the expected value is also one third.

Now draw four numbers: point one, point four, point six, and point nine. We will treat them as an illustrative set of possible uniform samples, not claim they arose from any particular random generator. Square each number. We obtain point zero one, point one six, point three six, and point eight one. Their sum is one point three four, and their average is point three three five.

The estimate is quite close to one third. But the closeness is not a theorem about four points. We chose a convenient illustrative sample. Another set of four random draws could produce a very different result. What makes Monte Carlo a mathematical method is not lucky examples; it is what can be proved about the estimator across independent samples.

Let U one through U n be independent copies of a uniform variable, and define the Monte Carlo estimate to be the average of their squared values. Each term has expectation one third, so the average also has expectation one third. The estimator is unbiased. As n grows, a law of large numbers says that under the relevant integrability assumptions the sample average approaches one third with increasing reliability; for independent identically distributed integrable variables, it converges almost surely.

To say how quickly it concentrates, calculate the variance. The expected value of U to the fourth power is one fifth. The square of the mean of U squared is one ninth. Subtracting gives four forty-fifths. For the average of n independent terms, divide that variance by n. With four draws, the standard deviation of the estimator is the square root of one forty-fifth, about point one four nine. Our illustrative error of only point zero zero one seven was much smaller than a typical standard deviation. That does not certify the method; it emphasizes why a single favorable run can mislead.

## An interval of any length

Suppose the target is the integral of a function from a to b. If U is uniform on that interval, its density is one divided by the interval length. Therefore the integral is the interval length times the expected value of the function evaluated at U.

This gives the algorithm: generate independent uniform inputs between a and b; evaluate the function at each one; average the function values; and multiply by b minus a. If the function has finite second moment under the sampling distribution, the estimator has variance equal to the square of the interval length, times the variance of one function evaluation, divided by n.

The method extends directly to a rectangle or box in several dimensions. The integral is the volume of the box times the expected value at a uniformly drawn point in that box. If the integral is already weighted by a probability density, the extra volume factor is unnecessary: sample from the relevant density and average the integrand.

At a deeper level, probability is doing the bookkeeping of integration. An expectation is not a different species of quantity from an integral. It is an integral against a probability distribution. The simulation enters only when we choose to approximate that quantity using random draws.

## Estimating a circle without drawing its boundary

Imagine a unit square. Within it, consider the quarter disk where the square of x plus the square of y is at most one. Its area is pi divided by four. Suppose we do not know that area in advance. Draw points uniformly and independently over the square. Mark a one if a point lies in the quarter disk and a zero if it lies outside.

The expected value of that indicator equals the area of the quarter disk, because every equal-area region is equally likely under uniform sampling. Its sample average estimates pi divided by four. Multiply the average by four to obtain an estimate of pi.

If a hypothetical run uses ten thousand independent points and finds seven thousand eight hundred fifty inside the quarter disk, the resulting estimate is three point one four. This is an illustration of how to interpret a hit count, not the output of an actual experiment we are claiming to have performed.

How uncertain would that estimate be? Each hit is a Bernoulli variable whose true success probability is pi divided by four. We do not need to know pi exactly to estimate a standard error: use the observed success fraction, point seven eight five. The standard error for the estimate of pi is four times the square root of point seven eight five times point two one five divided by ten thousand. That is about point zero one six four.

An estimate of three point one four may look impressively precise because it resembles the familiar first digits of pi. Yet the sampling uncertainty is measured in hundredths, not in the displayed decimal places. The apparent agreement in the first two decimals is compatible with random fluctuation. More digits printed on a screen are not more information.

## Where the uniform random numbers come from

A computer usually gives us pseudorandom numbers. They are generated by a deterministic algorithm from an internal state and seed. A suitable generator is designed to make the sequence behave sufficiently like independent uniforms for statistical computing, but deterministic repetition is not identical to physical independence.

For reproducibility, store the generator design and seed along with the model and sample count. For independent repeats, use independent streams or carefully separated seeds rather than restarting the exact same stream and calling the result new data. And do not assume that any generator adequate for simulation is adequate for cryptographic secrecy; those are different requirements.

Uniform draws are a starting point, not a restriction. Suppose we want samples from an exponential distribution with positive rate lambda. Its cumulative distribution function at nonnegative t is one minus the exponential of negative lambda times t. If U is uniform between zero and one, set X equal to negative log of one minus U divided by lambda. Then X has the desired exponential distribution. This is inverse-transform sampling: a uniform probability level becomes a sample drawn from the inverse cumulative distribution.

The transformation is exact mathematically when U is ideal uniform and endpoints are handled appropriately. In floating-point software, implementations must consider exceptional values near zero and one, because taking a logarithm of zero is not a finite operation. Good libraries handle these numerical details for common distributions.

## Monte Carlo and ordinary quadrature are not rivals in every problem

For a smooth function of one variable, deterministic quadrature can be dramatically more accurate than crude Monte Carlo with the same number of evaluations. Our integral of x squared is already solved exactly. Sampling it randomly would make little practical sense unless we were using it to test a simulation program.

Monte Carlo becomes appealing when the dimension is high, the geometry is complicated, or evaluating an expectation over a probabilistic model is the natural statement of the problem. A regular grid with m points in each of d coordinates uses m raised to the d points. That count can become prohibitively large. Independent Monte Carlo sampling, under finite variance, retains a one-over-square-root-of-n standard error rate regardless of dimension. But the variance constant can be enormous in high dimensions, so dimension independence of the rate does not mean every high-dimensional integral is easy.

Nor is the Monte Carlo error the only error. If each function evaluation comes from an approximate physical simulation, a coarse time discretization or biased numerical model may shift the target. More samples reduce the randomness of the numerical average, not the bias of the underlying model. A careful scientific calculation separates these error sources.

## How we decide that enough samples are enough

When independent sample contributions have finite variance, we can estimate that variance from their observed spread and divide by n to estimate the variance of their mean. A normal-approximation uncertainty interval may be appropriate when the sampling distribution is sufficiently well behaved and n is large enough. If contributions are bounded, a concentration inequality may give a finite-sample guarantee, although often a conservative one.

Two practical questions belong at the end of every Monte Carlo computation. First, is the sampling rule correct for the integral or expectation we set out to calculate? Second, is the resulting uncertainty small enough for the decision we want to make? A wrong sampling density can produce a biased result no matter how many draws we use. A correct but noisy estimator can be improved by additional draws, or by designing a different estimator that has less variance in the first place.

That second possibility leads to a more surprising result than simply increasing n. We can often get a substantially more accurate estimate from the same number of function evaluations by making the samples cooperate: by dividing the domain into regions, pairing related inputs, or sampling more often where the important contributions occur. Monte Carlo need not mean blindly throwing random points at a problem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### One-dimensional estimator

For \(f\in L^2([a,b])\), \(U_i\stackrel{\rm iid}{\sim}\operatorname{Uniform}(a,b)\),
\[
I=\int_a^b f(x)\,dx=(b-a)E[f(U)],\qquad
\widehat I_n=\frac{b-a}{n}\sum_{i=1}^n f(U_i),
\]
\[
E\widehat I_n=I,\qquad \operatorname{Var}(\widehat I_n)=\frac{(b-a)^2\operatorname{Var}(f(U))}{n}.
\]
For \(f(u)=u^2\) on \([0,1]\),
\[
I=1/3,\quad E[f(U)^2]=E[U^4]=1/5,\quad
\operatorname{Var}(U^2)=1/5-1/9=4/45.
\]
Four illustrative values \(u=(.1,.4,.6,.9)\) yield \((.01+.16+.36+.81)/4=.335\). The standard deviation of the four-sample estimator is \(\sqrt{(4/45)/4}=1/\sqrt{45}\approx.149071\), showing that the good observed agreement is not an uncertainty bound.

### Area as expectation

Let \((U,V)\sim\operatorname{Uniform}([0,1]^2)\) and \(H=\mathbf 1\{U^2+V^2\le1\}\). Then
\[
EH=\pi/4,\quad \widehat\pi=4\bar H_n,\quad
\operatorname{Var}(\widehat\pi)=\frac{16(\pi/4)(1-\pi/4)}{n}.
\]
At \(n=10,000\) and an illustrative observed hit fraction \(\hat p=.785\), \(\widehat\pi=3.14\) with plug-in standard error \(4\sqrt{(.785)(.215)/10,000}\approx .01643\).

### Inverse-transform sampling

For \(U\sim\operatorname{Uniform}(0,1)\) and \(\lambda>0\), define \(X=-\log(1-U)/\lambda\). For \(t\ge0\),
\[
P(X\le t)=P(U\le 1-e^{-\lambda t})=1-e^{-\lambda t},
\]
so \(X\sim\operatorname{Exponential}(\lambda)\).

### Reproducible standard-library example

```python
import math
import random
import statistics

rng = random.Random(2026)  # Reproducible illustrative stream, not cryptographic
values = [rng.random() ** 2 for _ in range(10000)]
estimate = statistics.mean(values)
se = statistics.stdev(values) / math.sqrt(len(values))
print(estimate, se, 1.0 / 3.0)
```

This code provides an approximate standard error for independent idealized draws. It does not certify the physical model, correct integration domain, or pseudorandom-generator independence.

### Exercises with worked answers

1. **Scaling.** Estimate \(\int_2^5 x^2\,dx\) by uniform samples on \([2,5]\). What factor multiplies the sample average? **Answer:** three; the exact integral is \(39\).
2. **Random sample.** Why is \(.335\) from four selected points not enough to certify a three-digit answer to \(1/3\)? **Answer:** it is only one observed outcome; the estimator's sampling standard deviation is about \(.149\) for four independent uniforms.
3. **Accuracy cost.** Under independent finite-variance sampling, how many times more evaluations are needed to divide Monte Carlo standard error by five? **Answer:** twenty-five times.
4. **Circle.** Derive the variance of the indicator \(H\) from its mean \(p\). **Answer:** \(\operatorname{Var}H=p(1-p)\), so \(\operatorname{Var}(4\bar H)=16p(1-p)/n\).
5. **Systematic error.** What does doubling the sample count do to a fixed bias in the simulated function values? **Answer:** it does not remove the bias.

### Reading and attribution

- Art B. Owen, *Monte Carlo Theory, Methods and Examples*, Chapters 1–4, available at https://artowen.su.domains/mc/.
- MIT OpenCourseWare 18.600, *Probability and Random Variables*, expectation and laws of large numbers.
- T. Budd, *Monte Carlo Techniques*, lecture 3, direct-sampling Monte Carlo integration (https://hef.ru.nl/~tbudd/mct/lectures/monte_carlo_integration.html).
