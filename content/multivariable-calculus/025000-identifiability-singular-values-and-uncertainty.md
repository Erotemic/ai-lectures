# Can the Data Determine the Parameters? Identifiability and Singular Values

**Track:** Multivariable Calculus from First Principles. **Focus:** expose the distinction between an accurate fit and an identifiable parameter, derive the singular-value view of sensitivity, and qualify covariance estimates.

<!-- BEGIN SPOKEN LECTURE -->

# Can the Data Determine the Parameters? Identifiability and Singular Values

Imagine fitting a model with two adjustable components. The optimizer runs to completion. The residual is nearly zero. The displayed parameters have six decimal places. Does this mean we have learned both parameter values accurately?

Not necessarily. A numerical algorithm can determine that the model predicts the measurements well while having almost no information about how to distribute that prediction among individual parameters. This is the distinction between fitting and identifying. The mathematics of singular values turns that distinction into something we can measure.

We will start with a model whose ambiguity is exact, add a tiny distinguishing signal, and see how a very small measurement error can produce a large change in fitted parameters. Then we will examine what a covariance estimate does and does not tell us. These arguments apply to calibration, inverse problems, nonlinear regression and any scientific model in which several parameters can imitate one another.

## A perfect fit with infinitely many explanations

Suppose we model three observations by multiplying one, two and three by the sum of two unknown parameters, a plus b. The observed values are one, two and three. Any parameter pair whose sum is one matches the observations exactly.

The pair a equals one and b equals zero works. So does a equals zero and b equals one. So does a equals one hundred and b equals minus ninety-nine. All yield the same predicted data and a residual vector of zero.

The residual Jacobian has three rows, with entries one and one, two and two, and three and three. Its columns are identical. Change a upward and b downward by the same amount, and none of the model predictions changes. The parameter direction one, minus one is invisible to these measurements.

There is no numerical solver that can extract the invisible difference from this data alone. A singular normal-equation matrix is not merely an implementation inconvenience here. It is a correct warning that the question has no unique answer. Adding damping may give a unique correction, or imposing a prior may select a preferred parameter pair, but neither creates the missing measurement information.

Among all exact fits in this example, the pair one half and one half has the smallest Euclidean parameter norm. That is the Moore–Penrose pseudoinverse solution to this linear problem. It is often a reasonable computational convention. It is not evidence that each physical component actually contributes one half.

The phrase identifiability has several levels. We have demonstrated structural nonidentifiability: even exact, noise-free data from the stated experiment cannot determine a and b separately. Local identifiability of a nonlinear model is related to the rank of the Jacobian near a solution, but local Jacobian rank alone does not settle every possible global ambiguity. Different, widely separated parameter vectors can still generate identical observations, and nonlinearities can have higher-order information invisible to a first-order rank test. A full inference claim needs a specified model and observation design.

## Singular values separate visible and invisible directions

Take the Jacobian J at a candidate fit. Its singular-value decomposition expresses it as an orthogonal change of coordinates in measurement space, a diagonal action by nonnegative singular values, and an orthogonal change of coordinates in parameter space.

Each right singular vector is a parameter direction. The corresponding singular value tells us how strongly the measurements change, to first order, when we move one unit in that direction. A large singular value means the model's predictions are sensitive to that direction. A small singular value means a substantial parameter motion can produce a very small predicted change. A zero singular value is a direction the linearized measurements do not see at all.

The smallest singular value is especially important. When the Jacobian has full column rank, the ratio of its largest singular value to its smallest is its two-norm condition number. This is a worst-case local amplification factor after we measure input and output perturbations in compatible relative norms. For absolute errors in the linearized inverse problem, it is the reciprocal of the smallest singular value that controls how large a parameter correction may be for a given residual perturbation.

There is an important difference between poor conditioning and exact nonidentifiability. If a singular value is zero, the local linear model has no unique inverse in that direction. If it is merely tiny, an inverse may exist mathematically, but the corresponding parameter estimate is sensitive to noise and rounding. A numerical rank threshold is an operational decision based on scale and error, not a theorem that a tiny nonzero singular value has literally become zero.

## Let the experiment barely distinguish two parameters

Here is a two-observation model where the ambiguity is almost, but not quite, broken. The first observation measures a plus b. The second measures a plus the quantity one plus epsilon, multiplied by b. In other words, its coefficient on b is just slightly greater than one. Epsilon is a small positive number that records how differently the two measurements respond to b.

The Jacobian therefore has first row one, one, and second row one, one plus epsilon. Its determinant is epsilon. If epsilon is nonzero, the matrix is invertible. If epsilon is extremely small, the columns are nearly parallel.

Take epsilon equal to one hundredth and suppose the true parameters are a equals one, b equals one. The exact observations are two and two point zero one. Now imagine that the second observation is too high by one thousandth, while the first is measured exactly. A fit matching both perturbed observations must satisfy a plus b equals two and a plus one point zero one b equals two point zero one one.

Subtract the first equation from the second. One hundredth of b equals eleven thousandths, so b equals one point one. Then a equals zero point nine. One measurement changed by just zero point zero zero one. Each inferred parameter changed by one tenth. The fitted predictions remain exact for the perturbed data, but the inferred mechanism has shifted considerably.

We can calculate the amplification generally. The error in b is measurement error divided by epsilon, and the error in a is its negative. As epsilon tends to zero, the parameter errors become arbitrarily large for fixed nonzero measurement error. The two-by-two matrix remains invertible for every positive epsilon, yet its inverse becomes increasingly sensitive.

The singular values make this transparent. For small epsilon, the larger singular value is near two, while the smaller is near epsilon divided by two. Their ratio is therefore near four divided by epsilon. At epsilon one hundredth, it is about four hundred. The normal-equation matrix J transpose J has a condition number equal to the square of that of J, roughly one hundred sixty thousand. This is why forming normal equations can make an already delicate fitting problem numerically more delicate.

More digits in an optimizer's output do not add independent observations. To improve the inference, we need either better measurement precision, a different experiment that separates the parameter effects, or assumptions about the parameters that we are willing to state explicitly.

## From singular values to uncertainty

Suppose the data are generated by a correct model with small independent measurement errors, each with zero mean and the same variance sigma squared. Suppose the residual Jacobian has full column rank and is evaluated near the true parameter or a suitably accurate estimate. Linearize the data model around that point.

A small observation error produces, to first order, a parameter error obtained by applying the pseudoinverse of J to the observation error, with a sign depending on how the residual was defined. Because the noise covariance is sigma squared times the identity, the parameter-error covariance in this linear approximation is sigma squared times the inverse of J transpose J.

This formula predicts large variances along directions associated with small singular values. If we rotate into the right singular-vector coordinates, the variance along one of those directions is sigma squared divided by the square of its singular value. So the same matrix that diagnoses the difficulty of a numerical least-squares solve also describes uncertainty amplification under a statistical error model.

But the formula is conditional. It depends on the measurement-error model, the quality of the linear approximation, the assumed independence and variance, and full column rank. In a nonlinear problem, it describes local uncertainty, not a universal confidence region. It says nothing automatic about errors from misspecified physics, biased sensors, correlated measurements or multiple distant solutions.

If sigma is not known, one often estimates it from the residual sum of squares divided by the number of observations minus the number of fitted parameters. That degrees-of-freedom adjustment requires the relevant full-rank, correctly specified setting and more observations than independent parameters. If the model interpolates the measurements exactly, a zero residual does not prove the measurement noise is zero. It may instead mean that the model is flexible enough to absorb the noise.

For correlated errors with a known positive-definite covariance matrix C, the corresponding local information matrix is J transpose C inverse J, and the covariance approximation becomes its inverse. Equivalently, we whiten the residual and Jacobian using a factor of C inverse square root. Weighting should be justified by the data-error model, not used merely to make the residual graph visually appealing.

## Small numerical singular values do not certify a physical truth

A solver may announce that it found a rank of one even when a matrix is mathematically rank two. That can be the correct *numerical* conclusion if the smaller singular value is overwhelmed by the precision of the data or arithmetic. But numerical rank must be compared to units, parameter scaling and expected perturbations. If a parameter is rescaled from seconds to milliseconds, the columns of the unscaled Jacobian change; a naive threshold can change its rank verdict even though the experiment's physical information is identical.

A better question is which combinations of physically scaled parameters can be estimated with useful precision under a stated noise model. The right singular vectors, expressed in sensible parameter coordinates, can identify those combinations. A large uncertainty in one parameter and an opposite movement in another often mean their sum or another combination is well identified while the components are not.

One can also study a profile objective: hold one parameter or parameter combination at a series of values, re-optimize the others, and observe how much the best possible residual sum of squares increases. This can reveal asymmetry, long valleys, or multiple solutions that a symmetric covariance ellipse near one optimum misses. Profiles are computationally more expensive and do not remove the need for a statistical observation model, but they give a different view of the geometry of the fit.

## Regularizing directions is not identifying them

A truncated singular-value solution discards components associated with singular values below a selected threshold. A ridge or Tikhonov step instead attenuates those components smoothly. Both can improve numerical stability. Both also encode a decision about which changes to suppress, beyond the raw observations alone.

Suppose the previous two-parameter example is almost singular. A regularized solver may give parameters closer to each other, or closer to zero, or closer to a prior estimate. Those choices can be useful for prediction or scientific interpretation when justified. But the small residual remains compatible with many parameter combinations if the experiment lacks distinguishing power. The software has not discovered information that the measurements never contained.

The main lesson is a practical hierarchy. First, ask whether the specified model can reproduce the observations. Second, ask whether its parameters can be inferred from those observations. Third, ask whether the inference is stable under realistic observation errors. Fourth, ask how modeling assumptions or prior information affect the answer. These are related questions, but they cannot be collapsed into a single success flag from a minimizer.

A trustworthy nonlinear fit reports enough information to answer them: residual behavior, local rank and singular directions, dependence on starting conditions when relevant, assumptions behind uncertainty estimates, and sensitivity to the data. The next step is to decide what to do when some of those diagnostics are poor. That brings us to regularization, robust losses and inverse-problem design.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Exact versus near rank deficiency

Consider

\[
A=\begin{bmatrix}1&1\\2&2\\3&3\end{bmatrix},\quad y=\begin{bmatrix}1\\2\\3\end{bmatrix}.
\]

Every \(\theta=(a,b)\) with \(a+b=1\) fits exactly. The nullspace is \(\operatorname{span}(1,-1)\). The minimum-norm solution is \((1/2,1/2)\), but the experiment does not identify \(a,b\) individually.

For

\[
J_\varepsilon=\begin{bmatrix}1&1\\1&1+\varepsilon\end{bmatrix},\quad
J_\varepsilon\begin{bmatrix}1\\1\end{bmatrix}=
\begin{bmatrix}2\\2+\varepsilon\end{bmatrix},
\]

perturb the second datum by \(\eta\), keeping the first unchanged. Solving exactly gives

\[
\hat b=1+\eta/\varepsilon,\quad
\hat a=1-\eta/\varepsilon.
\]

As \(\varepsilon\to0^+\), \(\sigma_{\max}(J_\varepsilon)\to2\), \(\sigma_{\min}(J_\varepsilon)\sim\varepsilon/2\), and \(\kappa_2(J_\varepsilon)\sim4/\varepsilon\). When full rank, \(\kappa_2(J^\top J)=\kappa_2(J)^2\).

### Statistical approximation and its scope

For a correctly specified linear model \(y=A\theta_*+e\) with \(\mathbb E e=0\), \(\operatorname{Cov}(e)=\sigma^2I\) and full-column-rank \(A\), least squares yields

\[
\hat\theta-\theta_*=(A^\top A)^{-1}A^\top e,
\qquad \operatorname{Cov}(\hat\theta)=\sigma^2(A^\top A)^{-1}.
\]

For nonlinear models substitute a local Jacobian only as a first-order approximation; do not present it as exact finite-sample covariance. With known \(C\succ0\), replace \(A^\top A\) by \(A^\top C^{-1}A\). Singular information matrices do not yield finite uncertainty along unidentified directions without additional constraints or priors.

### Exercises with answers

1. **Invisible direction.** For \(r(a,b)=(a+b-1,2a+2b-2,3a+3b-3)\), calculate \(J(1,-1)^\top\). **Answer:** zero, so this direction cannot be determined by those observations.
2. **Near-singular inverse.** Take \(\varepsilon=0.02\) and \(\eta=0.001\). What are the fitted parameters in the two-observation model? **Answer:** \(\hat a=0.95\), \(\hat b=1.05\).
3. **Covariance directions.** If \(J=U\operatorname{diag}(4,0.01)V^\top\) and white noise has variance \(\sigma^2\), compare local parameter variances in the two right-singular directions. **Answer:** \(\sigma^2/16\) versus \(10^4\sigma^2\), a ratio of \(160000\).
4. **What an exact fit cannot prove.** Does a zero residual vector imply zero measurement noise? **Answer:** no; an interpolating or overparameterized model can fit noisy measurements exactly. Identifiability and variance claims require more than residual size.

### Sources and further reading

- [SciPy `curve_fit` and least-squares implementation notes](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html), parameter scaling, covariance approximation, rank deficiency.
- [SciPy `least_squares` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html), SVD/QR-oriented numerical solvers and rank behavior.
- [Wikipedia: Identifiability](https://en.wikipedia.org/wiki/Identifiability), general structural and practical distinctions.
- [Wikipedia: Singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition), geometry and pseudoinverse.

*Teaching connections:* `linear-algebra:023000` develops singular values and pseudoinverses; `multivariable-calculus:023000` introduces residual Jacobians; `multivariable-calculus:026000` makes regularization's extra assumptions explicit.
