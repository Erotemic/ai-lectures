# Inverse Problems: Regularization, Robust Fits, and Responsible Conclusions

**Track:** Multivariable Calculus from First Principles. **Focus:** distinguish noise modeling from prior information and step damping, derive Tikhonov and weighted least squares, and connect robust loss and validation to reliable inference.

<!-- BEGIN SPOKEN LECTURE -->

# Inverse Problems: Regularization, Robust Fits, and Responsible Conclusions

A scientist can fit a complicated model to data and still have good reasons not to believe the resulting parameters. Maybe the data do not distinguish two parameter combinations. Maybe a few gross measurement errors dominate the squared residuals. Maybe the optimizer is responding to weak information by choosing enormous coefficients that cancel one another. Or maybe the fitted model predicts the measured points well but performs badly on a new experiment.

These are not all problems with the optimization algorithm. They concern the inverse problem itself: what information is present, how it is corrupted, and what additional assumptions we are willing to make to draw conclusions from it.

Regularization and robust fitting are two ways to make these assumptions explicit. They are powerful, but they answer different questions. Regularization expresses a preference or constraint on the parameters; robust fitting changes how discrepancies in the data contribute to the objective. A reliable analysis also has to decide how those choices are calibrated and tested.

## First specify which disagreements count

In the simplest nonlinear least-squares problem, we take each residual, square it, and sum. This treats residuals with the same numerical magnitude as equally consequential. But suppose one sensor measures distances in meters and another measures times in microseconds. Squaring raw differences in those units does not give a physically meaningful balance. We need an error model or a deliberate choice of scales.

If measurement i has a known standard deviation s i and independent Gaussian errors, a natural standardized residual is prediction minus observation, divided by s i. Its square measures disagreement relative to the instrument's typical noise. The objective becomes one half the sum of the squared standardized residuals. This is weighted least squares, with each original squared residual weighted by the reciprocal of its variance.

If measurement errors are correlated, we cannot treat each measurement independently. Let C be the covariance matrix of the observation errors, assumed symmetric and positive definite. The correct Gaussian quadratic misfit uses the residual transpose, then C inverse, then the residual. Conceptually, we can transform the residual vector so that its errors have unit covariance. That transformation is called whitening. Ordinary least squares on the whitened residuals equals weighted least squares using C inverse.

Whitening is not a cosmetic normalization. It changes which patterns of disagreement are plausible under the noise model. Two neighboring sensor readings that share the same calibration error do not supply two entirely independent pieces of evidence. A correlated error model recognizes that dependence.

And the model for the noise must itself be defended. Equal variance, Gaussian tails, and known covariance are useful assumptions, not automatic properties of every measurement process. If those assumptions are wrong, an optimizer can solve the specified objective perfectly while the inferred uncertainty remains misleading.

## Regularization changes what solution is preferred

Return to a model with two parameters a and b and one observation: their sum should equal two. The squared-residual objective is one half the square of a plus b minus two. Any pair whose sum is two fits exactly. There is an entire line of solutions.

Suppose we have a substantive reason to prefer small parameter magnitudes. Add one half times a positive number alpha times a squared plus b squared. The first term rewards agreement with the observation. The second imposes a cost for parameter size. This is the simplest quadratic, or Tikhonov, regularization; in statistical regression the related construction is often called ridge regression.

Because the problem treats a and b symmetrically, the minimizer has equal components. Solving the two first-order equations gives both parameters equal to two divided by two plus alpha. Without regularization, the minimum-norm exact fit is a equals one and b equals one. With alpha equal to one, the regularized solution is a and b both equal to two thirds. Their sum is four thirds, so the prediction no longer matches the observation exactly.

This result should not be described as the optimizer failing. The augmented problem has a different objective, and the data fit is intentionally traded against the preference for smaller parameters. That tradeoff can be a very good decision when the original inference is unstable or the preference is justified. But it has a cost: bias toward the chosen reference or preferred structure.

Notice what changed relative to Levenberg–Marquardt damping. Damping penalizes a correction from the current iterate while proposing a temporary step. If the damping is eventually removed, the algorithm is still trying to optimize the original residual objective. Tikhonov regularization penalizes the final parameter vector, or its deviation from a stated reference, at every iteration. It selects a different target. The matrices in their linearized equations can look similar, but the modeling decisions are not the same.

## Generalize the penalty to what matters physically

Small parameter norm is only one possible preference. Suppose the unknown parameters represent a temperature profile across a line of positions. Perhaps the data cannot resolve rapid oscillations, but physics suggests the profile should vary smoothly. It may be more appropriate to penalize differences between neighboring parameter values than to penalize the temperatures themselves.

Let L be a matrix representing the quantity we want to keep controlled: it might be the identity, a discrete first derivative, or a discrete second derivative. Let theta reference be a prior guess, reference state, or physically meaningful baseline. A quadratic regularizer charges for the squared length of L times theta minus theta reference, scaled by a positive strength alpha.

For a linear observation model A theta approximately equals y, this produces an objective with two pieces: data mismatch and structured penalty. Differentiating yields the linear system with coefficient A transpose A plus alpha L transpose L, and a right-hand side combining A transpose y with the corresponding reference term. If the data are weighted, replace the first term by A transpose C inverse A and the data term by A transpose C inverse y.

A unique solution requires the combined quadratic curvature to be positive definite. If some nonzero parameter direction is invisible both to A and to L, the penalty does not remove the ambiguity. For instance, a first-difference penalty does not penalize a constant offset. If the observations also cannot see that offset, the problem still has a null direction. Regularization is not a universal guarantee of uniqueness; its operator must control the directions the data leave unresolved.

The parameter alpha controls the balance. If it is too small, noise in weak singular directions may be amplified. If it is too large, real features of the unknown parameter vector may be suppressed. The mathematical act of making a matrix invertible is not sufficient justification for a particular alpha or L.

## Why regularization filters unstable modes

In the simplest unweighted problem with a penalty on the Euclidean parameter norm, singular-value decomposition makes the tradeoff explicit. Imagine expanding the measurements along the left singular vectors of A and the unknown parameters along its right singular vectors. Each singular mode behaves like a one-dimensional inverse problem.

Without regularization, a nonzero singular value s divides the corresponding measurement component by s. When s is tiny, that division amplifies noise. With quadratic regularization of strength alpha, the reconstruction coefficient instead multiplies the measurement component by s divided by s squared plus alpha.

For large s relative to the square root of alpha, this factor behaves roughly like one divided by s, preserving the informative directions. For very small s, the factor behaves like s divided by alpha and suppresses the unstable direction. In effect, the method filters the singular modes according to how much information the data can provide and how much stabilization has been requested.

A truncated singular-value method makes a sharper decision: retain singular modes above a threshold and discard those below it. Tikhonov performs a smooth attenuation. Both improve stability at the price of suppressing some possible signal. The choice between them is a modeling and numerical decision, not a contest in which one universal method always dominates.

## A Bayesian reading, with its conditions

There is another way to understand a quadratic penalty. Suppose the measurement errors are Gaussian with a known covariance C, and our prior beliefs about the parameter vector are also Gaussian, centered at theta reference with an invertible covariance Gamma. The negative log likelihood, up to constants, is one half the C-inverse-weighted squared data residual. The negative log prior, up to constants, is one half the Gamma-inverse-weighted squared deviation from theta reference.

Bayes' rule makes the posterior density proportional to likelihood times prior. Maximizing that posterior is therefore equivalent to minimizing the sum of those two quadratic expressions. In this specific model, regularized least squares gives a maximum-a-posteriori estimate.

The words in this statement matter. It is an interpretation under a chosen likelihood and prior, not proof that every quadratic penalty represents an objectively correct physical belief. A maximum-a-posteriori estimate is one point of a posterior distribution, not a substitute for uncertainty assessment. For nonlinear models that distribution may be asymmetric, multimodal, or poorly approximated by a Gaussian near one optimizer result.

When a reference estimate is learned from the same measurements, pretending it is an independent prior can count information twice. When model discrepancy dominates sensor noise, an extremely tight Gaussian likelihood can yield overconfident inferences. The algebra is clean; sound statistical interpretation still depends on how the assumptions were obtained.

## Make the fit less sensitive to outliers

Quadratic loss has a distinct problem: the contribution of a residual grows as its square, and the derivative of that contribution grows in direct proportion to its magnitude. One very large residual can dominate the fit, even if it comes from a corrupted measurement rather than from the model's normal variation.

A robust alternative is the Huber loss. For standardized residuals whose magnitudes are below a chosen threshold, it behaves exactly like half the squared residual. For larger magnitudes, it grows linearly rather than quadratically, with a slope fixed by the threshold. Thus small errors are treated efficiently in the familiar least-squares way while very large errors receive less leverage.

A simple way to construct an algorithm is iteratively reweighted least squares. At the current residuals, calculate a weight for each observation from the loss derivative divided by the residual magnitude, using its continuous limit at zero. For the Huber loss, the weight is one inside the threshold and proportional to threshold divided by residual magnitude outside it. Solve a weighted local least-squares problem, update the residuals and repeat.

This explains the mechanism, but a nonlinear robust solver requires careful treatment of its Jacobian, acceptance tests and possibly the second derivative of its chosen loss. The reweighting picture is not by itself a global convergence proof. In particular, some aggressively redescending losses have nonconvex objectives and may introduce additional local minima.

Robustness also has limits. If a systematic model error affects many observations, downweighting a few extremes will not repair the model. If one rare event is the phenomenon we actually want to detect, labeling it an outlier can erase important evidence. A robust loss encodes a decision about the distribution of errors; that decision must be connected to the purpose of the inference.

## How to choose and assess the result

There is no single universally correct recipe for a regularization parameter or robust-loss threshold. A method can use a known bound on measurement noise to demand that the residual be compatible with that noise. With enough independent data, it may be possible to tune a penalty by testing predictive performance on measurements not used to fit the parameters. Cross-validation is useful when the holdout scheme respects dependence in the data; randomly splitting a time-correlated series may give a misleadingly optimistic test.

Sometimes the goal is not prediction but recovering an unobservable physical parameter. In that case predictive accuracy may not fully measure success. A model can predict measured outputs accurately while assigning the wrong value to a confounded parameter. Experiment design is then crucial: choose a new measurement condition in which the previously similar parameter effects become distinguishable. The singular vectors of the residual Jacobian can suggest precisely which combinations remain weakly observed.

Diagnostics should match the claim we intend to make. For numerical convergence, check the gradient or an appropriate optimality measure, accepted step sizes, reduction ratios and arithmetic conditioning. For goodness of fit, inspect standardized residuals and their structure, not just their sum of squares. For parameter reliability, inspect singular directions, sensitivity to initial guesses and choices of noise or prior model, and uncertainty under the specified assumptions. For scientific validity, compare predictions against independent phenomena when possible.

A visually small residual can be a success at interpolation and a failure at identification. A stable parameter estimate can be a result of a strong prior rather than strong data. A robust loss can be justified by contamination, or it can hide a mistaken model. None of these observations means that fitting is futile. They mean that a fitted answer has to be read alongside the question that the objective actually asked.

## The bridge to advanced mathematics

We began with multivariable calculus: differentiating a residual vector and applying the chain rule to its squared norm. Gauss–Newton turned that derivative into linear least-squares corrections. Damping and trust regions constrained how far those local corrections could be trusted. Singular values exposed parameter combinations that the data scarcely observe. Regularization and robust losses made additional assumptions mathematically explicit.

The same ideas extend to much larger settings. In inverse partial differential equations, a parameter may be an entire field, and the Jacobian becomes a sensitivity operator. In statistical inference, local Hessians and information matrices describe approximate uncertainty, while priors encode knowledge not present in the observations. In experimental design, we arrange measurements to strengthen weak singular directions. In optimization, trust-region and proximal ideas make local models usable beyond their narrow neighborhoods.

The thread connecting these subjects is not a particular solver's name. It is the separation of three things: what the measurements say, what the mathematical model assumes, and what the numerical algorithm can faithfully compute. When those three are kept distinct, a least-squares result becomes not just a number, but an explanation of how that number could be supported—and where it could fail.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Whitening, regularization and covariance

Given observations \(y=f(\theta_*)+e\), \(\operatorname{Cov}(e)=C\succ0\), let \(r(\theta)=f(\theta)-y\). The Gaussian weighted objective is

\[
F(\theta)=\tfrac12r(\theta)^\top C^{-1}r(\theta)
=\tfrac12\|C^{-1/2}r(\theta)\|_2^2.
\]

For a linear forward map \(A\theta\), structured regularization about \(\theta_0\) gives

\[
\min_\theta\ \frac12\|C^{-1/2}(A\theta-y)\|_2^2+
\frac\alpha2\|L(\theta-\theta_0)\|_2^2,
\]

with stationarity equation

\[
(A^\top C^{-1}A+\alpha L^\top L)\theta=
A^\top C^{-1}y+\alpha L^\top L\theta_0.
\]

For \(\alpha>0\), uniqueness is ensured when \(\ker(A)\cap\ker(L)=\{0\}\). If a Gaussian prior is \(N(\theta_0,\Gamma)\), choose \(\alpha L^\top L=\Gamma^{-1}\) to recover the MAP objective for the stated Gaussian likelihood. This says nothing about whether those assumptions are appropriate.

### Ridge and spectral filtering

With \(A=[1\ 1]\), \(y=2\), \(C=1\), \(L=I\), \(\theta_0=0\), and penalty strength \(\alpha\), symmetry yields \(a=b=2/(2+\alpha)\). At \(\alpha=0\), the minimum-norm exact fit is \((1,1)\) although non-minimum-norm exact fits exist; at \(\alpha=1\), the unique regularized answer is \((2/3,2/3)\).

For \(A=U\Sigma V^\top\), quadratic ridge regularization yields \(\hat\theta_\alpha=\sum_{\sigma_i>0}\frac{\sigma_i}{\sigma_i^2+\alpha}(u_i^\top y)v_i\), with the zero-singular-value terms contributing zero. Compare with the unregularized pseudoinverse coefficient \(1/\sigma_i\).

### Huber loss and iteratively reweighted least squares

For standardized residual \(u\) and threshold \(\delta>0\), define

\[
\rho_\delta(u)=
\begin{cases}\frac12u^2,&|u|\le\delta,\\
\delta|u|-\frac12\delta^2,&|u|>\delta.
\end{cases}
\]

Its score \(\psi_\delta(u)=\rho_\delta'(u)\) is \(u\) within the threshold and \(\delta\operatorname{sgn}(u)\) outside. Thus \(w(u)=\psi_\delta(u)/u\) equals \(1\) for \(|u|\le\delta\), and \(\delta/|u|\) otherwise, taking \(w(0)=1\). In a linear model, an IRLS iteration can solve a weighted least-squares problem using the weights frozen at the current residuals; this is an iterative scheme, not a proof of global convergence for arbitrary nonlinear residuals.

### Exercises with answers

1. **Penalty changes the answer.** In the one-observation two-parameter example with \(\alpha=2\), find the minimizer and its data residual. **Answer:** \(a=b=1/2\); predicted sum is \(1\), residual is \(-1\), while the original least-squares problem has exact fits.
2. **Null directions surviving a penalty.** Suppose \(A(1,1)^\top=0\) and \(L(1,1)^\top=0\). Can quadratic regularization with \(L\) make the minimizer unique? **Answer:** no; the objective is unchanged along that common null direction.
3. **One outlier.** For standardized residuals \((0,1,10)\) and Huber threshold \(\delta=2\), compute the IRLS weights. **Answer:** \((1,1,0.2)\) at that iteration. A weight of \(0.2\) does not mean the third datum is deleted.
4. **Bayesian assumptions.** Explain why a Gaussian prior learned from the same observations cannot automatically be treated as independent information. **Answer:** the posterior calculation assumes a specified joint data-generating model; reusing the data to form an apparently independent prior can double-count evidence unless the full dependence is modeled.
5. **Design rather than compute.** If two parameters have almost parallel columns in the sensitivity Jacobian, what kind of new experiment could help? **Answer:** an observation condition at which their effects differ substantially, increasing the smallest singular value of a sensibly scaled combined Jacobian.

### Sources and further reading

- B. W. Rust and D. P. O'Leary, [*Residual periodograms for choosing regularization parameters for ill-posed problems*](https://math.nist.gov/~BRust/pubs/Unfolding/InvProbs2008.pdf), for inverse-problem regularization and its relation to unstable singular directions.
- [SciPy `least_squares` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html), robust loss choices and scale-sensitive stopping diagnostics.
- [Wikipedia: Tikhonov regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization); [Huber loss](https://en.wikipedia.org/wiki/Huber_loss), for introductory orientation.
- K. Madsen, H. B. Nielsen, and O. Tingleff, [*Methods for Non-Linear Least Squares Problems*](https://www2.imm.dtu.dk/pubdb/edoc/imm3215.pdf), for the underlying nonlinear fitting algorithms.

*Teaching connections:* `multivariable-calculus:024000` distinguishes transient damping from outer regularization; `multivariable-calculus:025000` diagnoses weakly identified directions; `optimization-duality:004000` develops constrained optimum conditions; `numerical-analysis:003000` develops conditioning.
