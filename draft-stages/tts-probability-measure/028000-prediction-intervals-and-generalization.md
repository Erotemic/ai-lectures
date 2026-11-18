# 028000 - Predicting a New Observation Is Harder Than Estimating an Average

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** simple least squares, sample variance, and elementary confidence intervals. **Theme:** uncertainty in fitted means, prediction intervals, extrapolation, train-test separation, and generalization.

<!-- BEGIN SPOKEN LECTURE -->

# Predicting a New Observation Is Harder Than Estimating an Average

We have fitted a line to laboratory measurements. Someone now asks, "What stretch should we expect under a load of two units?" A moment later, another person asks, "How far might the next single measurement be from that prediction?"

Those questions sound almost identical, yet they need different uncertainty calculations. The first concerns an average response at a specified load. The second concerns a new observation, which can vary even if we knew the true average perfectly. A statistical model must distinguish uncertainty in what we have learned from randomness in what will happen next.

We will work this distinction all the way through a small regression example, including numerical intervals. Then we will ask whether the calculations should be trusted when we move outside the range of data or evaluate a model on new conditions.

## The fitted line and its residual spread

Our laboratory dataset has five inputs: zero, one, two, three, and four. The observed responses are one, two, two, four, and five. Least squares gives the fitted line: predicted response equals point eight plus the input.

The residuals are point two, point two, negative point eight, point two, and point two. Their squared values add to point eight. We fitted two coefficients, slope and intercept, from five observations. Under the standard straight-line error model, that leaves three residual degrees of freedom.

Divide the residual sum of squares by three. We get about point two six seven. Its square root is about point five one six. This is the residual standard error, an estimate of the standard deviation of individual observation errors around the true conditional mean, assuming the model and its variance conditions are appropriate.

This estimate does not say that every future residual will fall between negative point five one six and positive point five one six. A standard deviation is a scale, not a hard bound. To build intervals we need a probability model for the errors and a desired coverage level.

## First question: where is the conditional average?

At input two, our fitted mean is point eight plus two, or two point eight. How uncertain is this estimate of the *population mean response* at load two?

The answer depends on how much data we have, how noisy it is, and where the requested input sits relative to the inputs used for fitting. In simple regression, the variance of the fitted mean at a particular input is proportional to one divided by the number of observations plus the squared distance between that input and the mean training input, divided by the total squared spread of training inputs.

At input two, which is exactly the average training input, the second term vanishes. With five observations, the factor is one fifth. Multiply our estimated error variance, about point two six seven, by one fifth and take a square root. The standard error of the fitted mean is about point two three one.

For a small sample with independent normal errors of equal variance around an exactly linear conditional mean, we can use a Student t critical value with three degrees of freedom. For a two-sided ninety-five-percent confidence interval, that multiplier is about three point one eight two. Multiply it by point two three one and get roughly point seven three five.

The resulting interval for the mean response at load two runs from about two point zero six five to three point five three five. If the assumptions and repeated-sampling scheme are correct, this procedure produces intervals containing the fixed true conditional mean at that input in ninety-five percent of repetitions. It does not assign a ninety-five-percent probability to the fixed parameter in a frequentist interpretation of the realized interval.

## Second question: what about the next individual measurement?

Now imagine we will test a brand-new component at load two. Its response can differ from the mean, even with infinite prior training data. There is irreducible scatter from manufacturing variation, measurement noise, and other influences represented in the error term.

The uncertainty of a new response therefore has two parts. The first is uncertainty about our estimated mean line. The second is the new observation's own error around that mean. For an independent new error with the same variance as training errors, the two variance contributions add.

The mean-estimation factor at input two was one fifth. For a new observation, it becomes one plus one fifth. Multiply that by the estimated error variance and take the square root. The predictive standard error is about point five six six, substantially larger than point two three one.

Use the same three-degree-of-freedom t multiplier of about three point one eight two. The prediction interval's half-width is about one point eight. So the ninety-five-percent interval for one new observation at load two runs from about one to four point six.

These are model-based values from a sample of only five points. They are not a claim that laboratory equipment is calibrated to those exact numbers. The purpose of the calculation is to show the extra term. Even if the slope and intercept were known perfectly, a single future measurement could still wander around its mean.

A confidence interval for a mean and a prediction interval for an individual response can both have ninety-five-percent coverage, yet describe different targets. Reporting a narrow mean interval as though it covered ninety-five percent of future outcomes is a serious mistake.

## Why predictions become fragile far from the data

Now ask for a prediction at load five, just beyond the largest tested load. Our fitted line gives five point eight. The average input in the data is two, so load five lies three units away from the center. The extra factor involving squared distance is nine divided by ten. Add one fifth and we get one point one for the uncertainty of the fitted mean, compared with point two at the center.

Under the same model, the standard error of the mean prediction at load five is about point five four two, more than twice the value at the center. The standard error for a new individual response is about point seven four eight. The corresponding ninety-five-percent prediction interval has a half-width of about two point three eight.

This widening reflects uncertainty in the estimated slope. The further we move from the center of the observed inputs, the more a small slope error matters. A line with slope just a little too steep may predict accurately near the center but miss badly at a distant load.

Yet the formula has a limitation more important than its arithmetic. It assumes the straight-line mean relationship continues to hold at the new input. Perhaps the material begins to yield beyond load four. Perhaps it breaks entirely. The model-based prediction interval becomes wider outside the data, but its width cannot compensate for a regime change the model does not include. Extrapolation is a scientific assumption, not just a statistical operation.

## Interpolation can also be dangerous

Staying within the measured input range is safer, but not foolproof. Imagine a dataset with many measurements near load zero and load four, but almost none near load two. A line may interpolate between the clusters even if the actual relationship has a sharp bend in the middle. The formula for uncertainty of a fitted linear mean only measures uncertainty under the linear model. It will not announce a hidden curve if that possibility is excluded by assumption.

Similarly, a prediction model may perform well for one population of devices but badly for a new production line whose materials or calibration differ. Such distribution shift can overwhelm a carefully calculated interval. Validation needs to resemble the setting in which we intend to make predictions.

## Training performance and future performance

One common assessment reports the average squared residual on the same data used to choose the model. This is training error. It is useful for checking arithmetic, but usually optimistic as a measure of future prediction error, because the model was chosen to reduce those very residuals.

To estimate performance on genuinely new data, reserve observations that do not influence the model fitting or selection. Fit on the training set and evaluate on the held-out set. If hyperparameters, predictor transformations, or model families are chosen by trying many variants, use a validation strategy that keeps the final test set out of those decisions.

For small datasets, cross-validation can be helpful. But the folds must reflect the intended use. If we want to predict a new patient, separate entire patients, not visits by the same patient. If we want to forecast next month, train only on earlier months and assess the future months. Randomly shuffling a time series may let information from the future leak into the apparent past.

There is no universal split ratio. What matters is what independence or distributional similarity the test is meant to represent. A huge randomly split dataset may still give false confidence if train and test share duplicated records or hidden group identities.

## What does coverage actually require?

A nominal ninety-five-percent prediction interval has a coverage interpretation only under the conditions used to derive it. For our exact t formula, we assumed a linear conditional mean, independent normal errors, constant variance, fixed or conditionally fixed full-rank input design, and an independent future observation following the same error model at the requested input.

If errors are strongly skewed, variances depend on input, observations share clusters, or the future setting differs from training, the stated coverage may fail. Sometimes distribution-free or robust methods can provide alternative guarantees under exchangeability or other conditions. But they too require assumptions. No finite-width prediction interval can guarantee useful coverage for an arbitrarily changing future without any restrictions.

There is also a difference between average coverage across a population and coverage at every individual input. A procedure calibrated across many inputs might achieve a ninety-five-percent marginal coverage rate while performing badly for a particular subgroup. When subgroup performance matters, it should be examined rather than hidden in one overall number.

## Connecting prediction to decisions

Imagine we must choose whether a component can safely operate at load two. The estimated mean stretch of two point eight may sound encouraging. But if the component fails whenever stretch exceeds four, the individual prediction interval extending to about four point six raises a different concern. We need to think about the probability of exceeding the relevant threshold, the cost of failure, and whether our model is credible at the operating point.

A model can be good at estimating average effects and poor at predicting individual outcomes. It can also be good at prediction without describing a causal mechanism. The right statistical summary depends on whether the decision concerns a population mean, a single future event, or the effect of changing a treatment.

We now have a complete elementary regression workflow. Design the study; specify the intended comparison; fit the line; inspect residuals and influential points; calculate uncertainty for the target of interest; and evaluate prediction on data that reflect the intended deployment. None of these steps can fully replace the others.

The most important calculation may be the simple extra one inside the predictive variance. It reminds us that knowing the average and knowing the next outcome are different achievements.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — two intervals, two targets

For fixed inputs \(x_1,\ldots,x_n\) with \(S_{xx}>0\), assume the conditional normal linear model \(Y_i=\beta_0+\beta_1x_i+\varepsilon_i\), where the \(\varepsilon_i\) are independent \(N(0,\sigma^2)\). Define
\[
s^2=\frac{\mathrm{SSE}}{n-2},\quad h(x_0)=\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}.
\]
For confidence level \(1-\alpha\) and \(t_*=t_{1-\alpha/2,n-2}\):
\[
\begin{aligned}
\text{Mean CI: }&\hat y(x_0)\pm t_*s\sqrt{h(x_0)},\\
\text{Individual PI: }&\hat y(x_0)\pm t_*s\sqrt{1+h(x_0)}.
\end{aligned}
\]
The extra variance \(\sigma^2\) in the second line comes from an independent new observation error.

For \(x=(0,1,2,3,4)\), \(y=(1,2,2,4,5)\), \(\hat y=0.8+x\), \(n=5\), \(S_{xx}=10\), \(\mathrm{SSE}=0.8\), so \(s^2=4/15\), \(s=\sqrt{4/15}\), and \(t_{0.975,3}\approx3.182446\).

At \(x_0=2\), \(h=1/5\), \(\hat y=2.8\). Mean interval half-width \(t_*\sqrt{4/75}\approx0.735\); individual interval half-width \(t_*\sqrt{8/25}\approx1.800\).

At \(x_0=5\), \(h=1/5+9/10=11/10\), \(\hat y=5.8\); individual interval half-width \(t_*\sqrt{(4/15)(21/10)}\approx2.382\). These are *conditional-on-model* intervals; extrapolation can invalidate the linear-mean assumption.

### Exercises with worked answers

1. **Residual scale.** With five observations, two fitted coefficients, and SSE 0.8, find \(s^2\). **Answer:** \(0.8/(5-2)=4/15\).
2. **Mean versus individual.** Why is the individual variance factor \(1+h\) rather than \(h\)? **Answer:** add the independent new-error variance to the uncertainty of the fitted mean.
3. **Extrapolation.** Compute \(h(5)\). **Answer:** \(1/5+(5-2)^2/10=1.1\).
4. **Leakage.** When predicting a new patient, should two visits by the same patient be split across training and test? **Answer:** not for an evaluation intended to measure generalization to unseen patients.
5. **Coverage.** Does the normal-model 95% PI promise 95% conditional coverage for future observations after a regime change? **Answer:** no; the data-generating model assumptions no longer match.

### Reading and attribution

- Penn State STAT 501, Lesson 3, *SLR Estimation and Prediction*, https://online.stat.psu.edu/stat501/Lesson03.
- Penn State STAT 501, Lesson 4, *SLR Model Assumptions*, https://online.stat.psu.edu/stat501/Lesson04.
- Penn State STAT 501, Lesson 11, *Influential Points*, https://online.stat.psu.edu/stat501/Lesson11.
