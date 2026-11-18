# When the Response Is a Probability: Logistic Regression and Likelihood

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 032000  
**Preparation:** Likelihood, logarithms, derivatives, and multiple regression.  
**Companion:** A grouped Bernoulli example, score, curvature, and model checks.

<!-- BEGIN SPOKEN LECTURE -->

Suppose a device sometimes fails after a stress test. You record the settings of the test and whether failure occurred. You want to predict a probability of failure for a new device. One tempting approach is to code success as one and failure as zero, fit an ordinary regression line, and interpret the fitted value as a probability. But a straight line can predict negative two tenths or one point three, neither of which is a probability. Worse, the variation of a binary outcome changes with its success probability. A probability close to one half has more Bernoulli variance than one close to zero or one.

We need a model whose mean respects the range from zero to one. Logistic regression supplies such a model. Let p be the probability of success conditional on the recorded predictors. Instead of fitting p directly as a linear combination, fit the log odds: the logarithm of p divided by one minus p. Make that quantity equal to an intercept plus coefficients times the predictors. Solving back for p gives one divided by one plus the exponential of the negative linear predictor. This logistic function always produces a number strictly between zero and one for finite coefficients.

What are odds? If an event has probability one quarter, its odds are one to three, or one third. The log odds are the negative logarithm of three. If probability becomes three quarters, odds become three to one and log odds become positive logarithm of three. Odds are not probability. An odds ratio is not a risk ratio, and the distinction matters when events are common.

Consider eight independent test outcomes at two settings. At the low setting, one of four devices succeeds. At the high setting, three of four succeed. Let the predictor x be zero for the low setting and one for the high setting. A logistic model with intercept alpha and slope beta predicts probability one quarter for x zero and three quarters for x one when alpha is negative log three and beta is two log three. The slope corresponds to an odds ratio of the exponential of beta, which is nine. Moving from low to high multiplies modeled odds by nine, while the modeled success probability changes from one quarter to three quarters. Those are different numerical statements.

How do we obtain those coefficients? Begin with the Bernoulli likelihood. For an observed binary outcome y, the probability assigned by the model is p when y equals one and one minus p when y equals zero. For independent observations, multiply these contributions. The logarithm converts the product into a sum. Each observation contributes y times log p plus one minus y times log of one minus p. Rewriting in terms of the linear predictor eta gives y times eta minus log of one plus the exponential of eta.

This expression is not just a convenient function to send to an optimizer. It says exactly what assumptions connect the data to the fitted coefficients: conditional Bernoulli outcomes with stated success probabilities and independence across observations for this simple likelihood. For the two groups in our example, the data proportions maximize the binomial likelihood within each group, so the fitted probabilities are one quarter and three quarters. Two distinct x settings and two free coefficients let the model match both group proportions, provided neither proportion is zero or one.

Differentiate the log likelihood with respect to a coefficient. The derivative is a sum of predictor values multiplied by observed outcome minus predicted probability. In vector notation, the score is X transpose times y minus p. At a finite optimum with a full-rank design, the score vanishes. The second derivative matrix is negative X transpose W X, where W is diagonal with terms p times one minus p. Since those terms are nonnegative, the log likelihood is concave. Under nonseparation and appropriate rank conditions, this makes numerical optimization well behaved and the coefficient solution unique.

Contrast this with least squares. In ordinary linear regression with independent Gaussian errors of common variance, maximizing likelihood is equivalent to minimizing the sum of squared residuals. In logistic regression, maximizing the Bernoulli likelihood means minimizing the negative log likelihood, often called logistic loss or cross-entropy. Different response distributions lead to different loss functions. This is one of the central ideas of generalized linear models: connect a systematic linear predictor to a conditional mean through a link function, and choose a probability model appropriate to the response.

The model can include several predictors, interactions, or transformed inputs. A coefficient beta for a numerical predictor changes the modeled log odds by beta for each one-unit increase while other included predictors remain fixed. Its exponential multiplies the modeled odds by a fixed factor. But the associated probability change is not constant. Near probability one half, a given log-odds shift can change probability substantially. Near zero or one, the same shift may change probability much less. A logistic coefficient therefore should not be announced as a fixed number of percentage points.

There is a trap with perfectly separated data. Imagine every device at the low setting fails and every device at the high setting succeeds. The logistic likelihood increases as the fitted probability at the low setting approaches zero and the high-setting probability approaches one. The corresponding coefficient magnitudes can grow without bound. With the ordinary unpenalized logistic model there may be no finite maximum-likelihood coefficient vector. An optimizer that reports a huge coefficient is not evidence of an enormous precisely estimated effect. It may be a sign of separation. Penalization or an appropriate prior can produce finite estimates, but those choices change the model.

We also need to think carefully about what counts as an independent observation. Suppose one machine generates a hundred highly correlated sensor readings during one test. Treating those as a hundred independent devices would overstate the effective evidence. Likewise, failure labels collected under a changed operating regime may not have the same conditional distribution as those used for fitting. Conditional probability estimates depend on the stability of the measurement and data-collection process, not only on having a plausible link function.

How should the fitted probabilities be checked? A classifier that outputs a probability is making a stronger claim than just predicting a label. We can examine calibration: among cases assigned probabilities near point seven, is the observed event rate near point seven, at an appropriate aggregation scale? We can assess log loss or the Brier score on held-out data. We can inspect residual patterns across predictors and relevant subgroups. A model may rank cases effectively while giving poorly calibrated probabilities, or be calibrated on average while missing important variation. No single score answers every question.

There is also a connection to optimization geometry. The logistic likelihood is concave in the coefficients for the ordinary linear predictor, whereas least-squares loss is a convex quadratic. Both can be fit using gradients, curvature, and matrix computations. Both become difficult to interpret when predictors are nearly collinear. Both can overfit if we include many flexible terms relative to the information in the data. Yet their mathematical error models are distinct, and their fitted values answer different questions.

Generalized linear models extend the same organizing principle beyond binary outcomes. A Poisson regression for nonnegative counts can use a log link so the expected count is positive. Its variance assumption differs from a Bernoulli model, and real counts may be more dispersed than a Poisson distribution allows. The right link function and likelihood arise from what is being measured and from the process generating variation. There is no magical family of curves that converts data into trustworthy probabilities automatically.

Our example began with two groups and eight observed outcomes. The arithmetic gave a probability model, an odds ratio, and a concrete maximum-likelihood fit. The larger lesson is about building a bridge between algebra and uncertainty: a linear predictor describes systematic effects, a link function respects the outcome's domain, and a probability model tells us how observations differ from their expectations. A fitted coefficient becomes meaningful only when all three parts are understood.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For \(\eta_i=x_i^\top\beta\), \(p_i=1/(1+e^{-\eta_i})\), the independent Bernoulli log likelihood is
\[
\ell(\beta)=\sum_i\left[y_i\eta_i-\log(1+e^{\eta_i})\right],\quad
\nabla\ell=X^\top(y-p),\quad
\nabla^2\ell=-X^\top W X,
\]
with \(W_{ii}=p_i(1-p_i)\). The Hessian is negative semidefinite. Full column rank alone does not ensure a finite MLE; complete or quasi-complete separation may prevent one.

For four x=0 outcomes with one success, and four x=1 outcomes with three successes, the fitted group proportions are \(\hat p_0=1/4\), \(\hat p_1=3/4\), giving \(\hat\alpha=\log(1/3)=-\log 3\), \(\hat\beta=\log(3)-\log(1/3)=2\log 3\), and odds ratio \(e^{\hat\beta}=9\).

**Caution:** This exact grouped MLE relies on the two-setting design and finite group proportions; do not generalize the closed form to arbitrary multiple-predictor logistic regression.

### Exercises and answers

1. **Odds versus probability.** At probability three quarters, what are the odds? **Answer:** Three to one.
2. **Effect size.** For a logistic coefficient log two, what changes by a factor of two? **Answer:** The conditional odds, not generally the probability.
3. **Separated data.** Why might an unpenalized logistic coefficient diverge? **Answer:** Predicted success probabilities can approach zero and one on perfectly separated groups without attaining a finite coefficient maximum.
4. **Prediction.** Does good training classification accuracy prove probability calibration? **Answer:** No; evaluate held-out probabilistic predictions and calibration separately.

### Reading and attribution

- Penn State STAT 501, multiple regression and generalized linear modeling course resources: https://online.stat.psu.edu/stat501/.
- Hastie, Tibshirani, and Friedman, *The Elements of Statistical Learning*: https://hastie.su.domains/ElemStatLearn/.
- Gelman et al., *Bayesian Data Analysis*, third edition, for predictive checking: https://sites.stat.columbia.edu/gelman/book/.
- The eight-device grouped calculation is an original worked teaching example.
