# From Jacobians to Uncertainty Budgets: Errors, Correlations, and Nonlinearity

<!-- BEGIN SPOKEN LECTURE -->

# From Jacobians to Uncertainty Budgets: Errors, Correlations, and Nonlinearity

A measurement is rarely a perfectly known number. A ruler has finite resolution, a sensor has noise, and a fitted parameter carries uncertainty. Now suppose we combine several measurements into a new quantity. How uncertain is that result?

If we multiply a measured length by a measured width, the result is an area. If we divide one reading by another, the result may be a ratio. If we pass uncertain inputs through a complicated computer model, the result may be a predicted temperature or a flight time. Each example poses the same question: how does uncertainty at the inputs propagate through a function?

This is where the multivariable derivative joins probability and numerical analysis. The Jacobian describes the first-order response of outputs to changes in inputs. Covariance describes how random input errors vary together. Put these two structures together and we obtain a first-order uncertainty budget. But that calculation is not an exact probability theorem for an arbitrary nonlinear model. We will derive what it says, check a numerical example, and see precisely where it stops working.

## Begin with an ordinary product

Suppose a rectangular object has length two meters and width three meters. The reported area is six square meters. The length measurement may be wrong by a small amount a; the width may be wrong by a small amount b. The actual area is two plus a, times three plus b. Expand that product. The result is six plus three a plus two b plus a b.

There are three pieces. Six is the area at the nominal measurements. Three a plus two b is the first-order change in area. The product a b is a second-order correction. The linearized area change is therefore three times the length error plus two times the width error.

That statement is the differential of the area function. Its two coefficients, three and two, are the partial derivatives of area with respect to length and width. They also tell us the units of sensitivity. Three meters of width times an error in meters of length contributes square meters of area error.

Suppose we know only deterministic error limits: the length error is at most one tenth of a meter in magnitude, and the width error at most two tenths. We can bound the absolute linearized area error by three tenths plus four tenths, or seven tenths of a square meter. The neglected product has magnitude at most two hundredths. So a rigorous absolute area error bound is seven tenths plus two hundredths, or seventy-two hundredths of a square meter.

This is an error budget without probability. It applies no matter how the errors were generated, provided the stated bounds hold. A stochastic uncertainty budget is related but answers a different question.

## Random errors and covariance

Now model the two errors as random variables with mean zero. Suppose the length error has variance four hundredths of a square meter. Its standard deviation is two tenths of a meter. The width error has variance nine hundredths of a square meter, with standard deviation three tenths. Let their covariance be twelve thousandths of a square meter.

The covariance matters because the two errors may move together. For example, a common temperature fluctuation might affect both measurements in the same direction. Treating them as independent when they share a disturbance can underestimate the uncertainty of a product.

The linearized area error is three a plus two b. The variance of that linear combination is nine times the variance of a, plus four times the variance of b, plus twelve times their covariance. Substitute the numbers: nine times four hundredths is thirty-six hundredths. Four times nine hundredths is another thirty-six hundredths. Twelve times twelve thousandths is one hundred forty-four thousandths. The total is eight hundred sixty-four thousandths of a square meter squared, meaning units of meters to the fourth power. The corresponding standard deviation of area is about ninety-three hundredths of a square meter.

The arithmetic is more enlightening when written as a matrix. Put the two measurement variances on the diagonal of a two-by-two covariance matrix, and the covariance in both off-diagonal positions. Put the two partial derivatives of area into a one-row Jacobian, with entries three and two. Multiply the Jacobian by the covariance matrix and then by the transpose of the Jacobian. The result is exactly the variance we just calculated.

For a vector-valued function, the same operation produces a covariance matrix for all output quantities. If the input covariance is Sigma and the Jacobian is J, then the linearized output covariance is J times Sigma times J transpose. The shape of each matrix tells you which spaces are being measured: input uncertainty lives in the input coordinates, while propagated uncertainty lives in the output coordinates.

## Why the covariance matrix has the correct geometry

A covariance matrix does more than store separate error bars. For any vector of weights, multiplying those weights by the random error vector produces a new random variable. Its variance equals the weight vector transpose, times the covariance matrix, times the weight vector. A variance cannot be negative. Therefore every covariance matrix is positive semidefinite.

The Jacobian transfers that property to the output. For any output direction, the variance in that direction after linearization is nonnegative because it can be written as a quadratic form in the input covariance. When the output Jacobian has a null direction, some combinations of input errors have no first-order effect. Conversely, directions that the Jacobian stretches strongly can create large output uncertainty.

The singular values of a suitably scaled Jacobian are a compact way to describe these sensitivities. But we must choose scaling carefully. A raw singular value changes when a parameter is converted from meters to millimeters; a physically meaningful analysis includes units, error magnitudes, or dimensionless coordinates.

A covariance ellipse is a picture of this geometry. It shows directions of relatively large and small variance, with axes determined by eigenvectors of the covariance matrix. By itself, an ellipse of a stated quadratic radius does not guarantee any particular coverage probability. For such a probability interpretation we need additional distribution assumptions, such as a multivariate Gaussian model.

## The nonlinear correction is visible in the same example

We dropped the product a b when computing the linearized variance. Did that discard anything important?

First, the expected area is not necessarily six, even though both measurement errors have mean zero. Expanding the exact product and taking expectations gives six plus the expectation of a b. Because both errors have mean zero, that expectation is their covariance. In our example the expected area is six point zero one two square meters. Correlation has shifted the mean upward.

This is a simple version of nonlinear bias. Averaging the inputs first and then passing them through a nonlinear function need not give the same result as passing each noisy observation through the function and averaging afterward.

For jointly Gaussian zero-mean measurement errors, we can even calculate the exact area variance. It equals the linearized variance, plus the product of the two input variances, plus the square of their covariance. In our numbers that is zero point eight six four, plus zero point zero zero three six, plus zero point zero zero zero one four four. The exact variance is zero point eight six seven seven four four. The first-order estimate was close here but not exact.

The closeness is due to the errors being reasonably small compared with the nominal dimensions, not because the extra terms are always negligible. If the input errors were comparable to the measured lengths, the quadratic term could dominate. The formula for exact variance just used also relies on a joint Gaussian assumption; it is not a general identity for all noise distributions sharing the same covariance matrix.

## An example where linearization tells us almost nothing

Consider a single random input X with mean zero and small positive variance. Let the output be X squared. The derivative of the squaring function at the mean input zero is zero. The first-order rule therefore predicts zero output variance. But X squared is random unless X has constant absolute value.

If X is normally distributed with mean zero and variance sigma squared, the expected output is sigma squared, and the output variance is two times sigma to the fourth power. Both are nonzero. The linearization about the mean has missed the leading behavior entirely because the derivative vanishes at that point. Here a second-order expansion, or a calculation using the full distribution, is necessary.

There is another failure mode. Take the ratio of two measurements, where the denominator might be close to zero. Its derivatives can become enormous. A first-order covariance calculation about a safe-looking nominal denominator may conceal a small chance of extreme ratios. Even when the input errors are well behaved, the resulting ratio may have a heavy tail, and certain moments may not exist. Blindly reporting a standard deviation from a Jacobian can be misleading.

Neither counterexample means linearization is useless. It tells us what must be checked: the domain of the function, distance from singularities, the size of nonlinear remainder terms, and whether a first-order approximation is adequate over the input distribution that matters.

## From a scalar example to an inverse problem

Suppose instead that a model maps a parameter vector theta to a collection of predicted sensor readings. We fit the parameters to observations. After fitting, we may want uncertainty in a derived output, such as the time at which a threshold will be crossed.

There are two distinct Jacobians in this story. The model Jacobian describes how the predicted observations respond to changes in the parameters. Under suitable local, identifiability, and noise assumptions, it helps determine an approximate covariance for the fitted parameters. A second Jacobian describes how the derived output responds to parameter changes. The latter propagates parameter covariance to output covariance.

These two uses of derivatives should not be collapsed into one step. The first estimate of parameter covariance depends on the statistical model and the information actually present in the observations. The propagation step depends on the accuracy of the output linearization. A perfectly computed Jacobian cannot repair biased data, non-identifiability, or an incorrect noise model.

Numerical error is a third category. If the computational solver produces a parameter vector only approximately, that error is not the same as measurement noise. A solver residual might allow a deterministic bound on the numerical contribution if a conditioning estimate is available. Combining that with a probabilistic standard error requires care; adding a deterministic bound to a probability interval changes its meaning.

## An error budget with named assumptions

A useful report of uncertainty keeps the sources separate. State the nominal inputs and their units. State which uncertainties are random and which are worst-case bounds. Record correlations rather than just standard deviations. Explain which derivative or Jacobian was evaluated and where. Note any known nonlinear terms or singular boundaries. If you give a confidence statement, identify the stochastic assumptions that support its coverage.

We began with the almost trivial fact that the area of a rectangle is length times width. The derivative of that product supplied a local linear prediction. Covariance turned the prediction into a variance estimate. A second-order term exposed both a shift in the mean and an error in the variance. Numerical analysis asked whether the approximation was stable and whether the units were meaningful.

The same pattern applies to data fitting, parameter calibration, sensor fusion, simulations, and scientific computing. Uncertainty propagation is not a recipe for multiplying three matrices and forgetting the rest. It is a way to connect a local model of change with a stated account of how the inputs can be wrong.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Deterministic error and first-order covariance

For area \(A(L,W)=LW\), with nominal \((L_0,W_0)=(2,3)\),

\[
A(2+a,3+b)=6+3a+2b+ab,
\quad dA=(3,2)\binom{a}{b},
\quad |\Delta A|\le3|a|+2|b|+|ab|.
\]

With \(|a|\le0.1, |b|\le0.2\), the exact bound is \(|\Delta A|\le 0.72\,\mathrm{m}^2\).

For random vector \(Z\) with covariance \(\Sigma\) and smooth output \(g\), the first-order covariance formula is
\[
 \operatorname{Cov}(g(Z))\approx J_g(\mu)\Sigma J_g(\mu)^T.
\]
Its accuracy depends on the distribution's spread, higher derivatives, and domain; it is the **delta method**, not a general exact equality.

### Numerical example and exact Gaussian correction

\[
\Sigma=\begin{pmatrix}0.04&0.012\\0.012&0.09\end{pmatrix}\,\mathrm{m}^2,
\quad J=(3,2)\,\mathrm{m},
\quad J\Sigma J^T=0.864\,\mathrm{m}^4,
\quad \sqrt{0.864}\approx0.9295\,\mathrm{m}^2.
\]

If \((a,b)\) is jointly centered Gaussian with the displayed covariance, then
\[
E[(2+a)(3+b)]=6+\operatorname{Cov}(a,b)=6.012\,\mathrm{m}^2,
\]
\[
\operatorname{Var}((2+a)(3+b))=0.864+0.04(0.09)+(0.012)^2
=0.867744\,\mathrm{m}^4.
\]

For \(X\sim N(0,\sigma^2)\), \(g(X)=X^2\), we have \(g'(0)=0\) but \(E[g(X)]=\sigma^2\) and \(\operatorname{Var}(g(X))=2\sigma^4\).

### Exercises and solutions

1. **Independent measurements.** Set \(\operatorname{Cov}(a,b)=0\) while retaining the two variances. **Answer:** first-order area variance \(0.72\,\mathrm m^4\); Gaussian exact variance \(0.7236\,\mathrm m^4\).
2. **Negative covariance.** Use covariance \(-0.012\). **Answer:** first-order area variance \(0.576\,\mathrm m^4\); expected area \(5.988\,\mathrm m^2\).
3. **Units.** Check the dimensions of \(J\Sigma J^T\). **Answer:** each derivative of area with respect to a length has units meters, so the resulting covariance has units meters to the fourth, appropriate for variance of square meters.
4. **Zero derivative.** Suppose \(X\) takes \(-1\) and \(+1\) with equal probability and \(g(X)=X^2\). What is the true output variance? **Answer:** zero, despite input variance one; the output is identically one. This also shows covariance alone does not determine a nonlinear output distribution.
5. **Variance preservation.** Show the matrix \(J\Sigma J^T\) is positive semidefinite when \(\Sigma\) is. **Answer:** \(v^TJ\Sigma J^Tv=(J^Tv)^T\Sigma(J^Tv)\ge0\).

### Sources and further reading

- [OpenStax, *Calculus Volume 3*](https://openstax.org/details/books/calculus-volume-3), multivariable derivatives and chain rule.
- [Penn State STAT 505, Applied Multivariate Statistical Analysis](https://online.stat.psu.edu/stat505/), covariance matrices and linear combinations.
- [Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*](https://nhigham.com/accuracy-and-stability-of-numerical-algorithms/), error and conditioning distinctions.
- Related lectures: `multivariable-calculus:067000`, `multivariable-calculus:019000`, `probability-measure:029000`, `probability-measure:031000`, `numerical-analysis:003000`.
