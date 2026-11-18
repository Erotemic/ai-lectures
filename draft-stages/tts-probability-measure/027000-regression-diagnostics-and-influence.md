# 027000 - A Fitted Line Is Not a Checked Model

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** simple least squares, conditional means, and sample variance. **Theme:** residual patterns, heteroskedasticity, dependence, leverage, influence, and model checking.

<!-- BEGIN SPOKEN LECTURE -->

# A Fitted Line Is Not a Checked Model

A regression program prints a slope, an intercept, and a number called R-squared. The slope looks plausible. R-squared is high. The temptation is to close the notebook and use the model. But the most useful part of a regression analysis may begin after those numbers appear.

A fitted line can hide a curve. It can be driven by a single data point far from the others. Its error bands can widen with the input, or its residuals can move together over time. In all these cases, the least-squares calculation may have been performed perfectly. The problem is that the fitted model is answering the wrong question or that its assumptions fail.

We will use one small dataset to calculate residuals and leverage exactly, then use larger imaginary patterns to understand what plots can reveal. The goal is not to pass an arbitrary diagnostic checklist. It is to learn which features of the data the line has explained and which it has merely ignored.

## Residuals: what the model leaves behind

Recall five observations at inputs zero, one, two, three, and four, with outcomes one, two, two, four, and five. The least-squares line predicts point eight plus the input. Its fitted values are point eight, one point eight, two point eight, three point eight, and four point eight.

Subtract each prediction from its observation. The residuals are point two, point two, negative point eight, point two, and point two. These five numbers are the information left after the line has been fitted. They are not the true unobserved errors, because the line's coefficients were estimated from the same data. But they can help us detect a poor model.

Plot each residual against its fitted value or input. A simple linear mean model predicts residuals without a systematic trend in conditional mean. If the residuals are negative at both ends and positive in the middle, that may suggest a curved response that the straight line is missing. If their spread increases from left to right, we may need to reconsider the constant-variance assumption. If the signs remain positive for many consecutive time points and then negative for many more, the observations may be dependent or the mean may be changing.

These are clues, not automatic diagnoses. Our five-point dataset, for example, has one negative middle residual. Five points cannot tell us whether that reflects curvature, ordinary noise, or a measurement problem. The appropriate next step may be to collect more independent observations at nearby input values, examine the equipment, or fit a scientifically justified model with a quadratic term and see whether it predicts better outside the fitting sample.

## What constant variance means

The standard basic regression model supposes that, for a fixed input, the response varies around its conditional mean with the same error variance at all input values. This is homoskedasticity. When the variation grows or shrinks with the input, we call it heteroskedasticity.

Imagine predicting a household's monthly expenditure from its income. A simple line might describe average expenditure reasonably well, while the variation among households becomes much larger as income rises. The conditional mean could still be approximately linear. The difficulty is that the uncertainty is not equally large at every income.

Under the standard homoskedastic model, ordinary least squares has familiar coefficient standard-error formulas. If variance changes substantially with input, those formulas can be misleading. Heteroskedasticity-robust standard errors can address certain variance-estimation problems under suitable independence and large-sample conditions. They do not correct an incorrect conditional mean, a biased sample, confounding, or severe dependence.

If the variance structure is known from measurement physics, weighted least squares may be a more efficient fit. If it is only guessed after viewing a noisy small dataset, arbitrary weights can cause new problems. The choice should be tied to a defensible error model.

## Dependence: when rows are not separate experiments

Suppose each observation is taken once per minute from the same sensor. A positive drift in the sensor can produce several positive residuals in a row. These errors are not independent, even if the line passes through the cloud of data.

Dependence changes how many independent pieces of evidence the dataset contains. We cannot replace ten independently randomized devices by taking ten rapid readings from one device and pretend that the sample size is the same for uncertainty calculations.

A residual-versus-time plot can show trends, periodicity, or persistent positive and negative runs. If the design has repeated measurements or clusters, we may need a correlated-error model, cluster-aware standard errors, or a design-based estimator. The choice depends on what was repeated and what mechanism generated the dependence.

Independence and linearity are different assumptions. A sensor can have independent errors around a curved mean; another can have correlated errors around a perfectly straight mean. The residual patterns point to different remedies.

## Leverage: how far an input can pull the line

Return to our five input values. The sample mean input is two, and the sum of squared input deviations is ten. In simple regression with an intercept, each observation has a leverage number. It is one divided by the number of points, plus the squared distance of that input from the mean divided by the total squared input spread.

For inputs zero and four, the leverage is point six. For inputs one and three, it is point three. For input two, it is point two. These numbers measure how sensitive the fitted value at an observed input is to its own outcome. Their sum is two, the number of fitted coefficients.

Leverage depends on the inputs, not the outcomes. A point at input four has high leverage even if it sits exactly on the fitted line. A point at input two can have a large residual and low leverage. This is why a vertical outlier and a high-leverage point are not the same thing.

Influence asks another question: how much would the fitted model change if we removed an observation? A high-leverage point can be influential, especially if its outcome conflicts with the pattern in the rest of the data. But leverage alone does not guarantee influence.

In our example, the center observation has residual negative point eight and leverage point two. The endpoint observations have residual point two and leverage point six. Comparing only raw residuals would miss the fact that removing one endpoint can shift the fitted line noticeably. Comparing only leverages would miss the center point's larger vertical error.

## Leave-one-out predictions

There is a direct way to inspect predictive influence. Fit a regression to all points except one, predict the omitted point, and record the prediction error. Repeat for each point. These are leave-one-out or deleted residuals.

For ordinary least squares with a full-rank design, a useful identity makes this calculation possible without refitting every model. The deleted residual equals the ordinary residual divided by one minus the observation's leverage, provided the reduced design remains full rank.

For our center observation, the ordinary residual is negative point eight and leverage is point two. Divide negative point eight by point eight; the leave-one-out residual is negative one. For an endpoint, the ordinary residual is point two, leverage point six, so the deleted residual is point five. The endpoint becomes a larger miss when it no longer helps determine the line.

Notice that the deleted residuals are not just ordinary residuals expressed in different units. They evaluate each observation using a model not fitted on that observation. In this five-point sample, the sum of squared deleted residuals is about one point six six, substantially larger than the training sum of squares, point eight. That is a small illustration of the optimism built into in-sample fitting.

Leave-one-out assessment is not universally appropriate. If data arrive in time order, training on observations from the future to predict earlier observations may conceal leakage. If several rows come from the same patient or chamber, leaving out one row while retaining its close relatives does not test generalization to a new patient or chamber. Validation must respect the unit and time structure of the intended prediction problem.

## Model checking is about consequences

Suppose a residual plot shows a clear U-shape. We could introduce a squared-input term. That model is still linear in its coefficients, even though its mean response is curved as a function of input. We then have to ask whether the extra flexibility predicts well and whether the relationship makes scientific sense. A low training error alone is not enough.

Suppose a residual-versus-input plot fans outward. We might change the scale of the outcome, use a variance model, or retain the mean model with robust standard errors appropriate for the design. We should explain which problem each choice addresses.

Suppose an extreme input controls the slope. We must inspect whether it is a data entry mistake, a physically meaningful operating condition, or an observation outside the intended range. Deleting it solely because the regression becomes more convenient is not a justification. A useful report can show estimates with and without it, with reasons for any exclusion.

A model can fail in several dimensions at once. A curved mean can coexist with correlated errors and selective missingness. No single residual plot proves all assumptions. We combine mathematical diagnostics with knowledge of how observations were produced.

## What a good report should say

A report should specify the response and predictors with units, the sample selection and independent experimental units, the fitted equation, a summary of residual behavior, potential influential observations, and the intended prediction range. If the purpose is inference, it should state which error assumptions support its uncertainty intervals. If the purpose is causal explanation, it must make an additional argument about design and confounding.

The most important habit is to avoid treating regression as a stamp of approval. The algorithm finds the best line according to a specified objective. Diagnostics tell us whether that objective and the surrounding assumptions produce a useful model of the phenomenon. A high R-squared cannot substitute for that examination.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — leverage, deleted residuals, and error structure

For \(X=[\mathbf1\;x]\) with full column rank, the hat matrix is \(H=X(X^TX)^{-1}X^T\). The fitted values satisfy \(\hat y=Hy\), the residuals satisfy \(e=(I-H)y\), and \(\operatorname{tr}H=2\).

For simple least squares with intercept,
\[
h_{ii}=\frac1n+\frac{(x_i-\bar x)^2}{S_{xx}}.
\]
For \(x=(0,1,2,3,4)\), \(\bar x=2\) and \(S_{xx}=10\), giving \(h=(0.6,0.3,0.2,0.3,0.6)\). With \(e=(0.2,0.2,-0.8,0.2,0.2)\), deletion residuals are \(d_i=e_i/(1-h_{ii})\), yielding
\[
d=(0.5,2/7,-1,2/7,0.5),\quad \operatorname{PRESS}=\sum d_i^2=\tfrac12+\tfrac8{49}+1=\tfrac{163}{98}\approx1.6632653.
\]
The leave-one-out shortcut requires each deletion fit to remain well defined. It is not a replacement for validation with independent subjects or future observations.

Under a fixed full-rank design with \(E[\varepsilon\mid X]=0\), constant error variance \(\sigma^2\), and independent errors, \(\operatorname{Var}(\hat\beta\mid X)=\sigma^2(X^TX)^{-1}\). If instead \(\operatorname{Var}(\varepsilon\mid X)=\Omega\), then
\[
\operatorname{Var}(\hat\beta\mid X)=(X^TX)^{-1}X^T\Omega X(X^TX)^{-1},
\]
assuming the stated conditional mean and covariance structure. A heteroskedasticity-robust covariance estimator targets a suitable version of this structure under appropriate sampling conditions, but does not make a wrong mean model correct.

### Exercises with worked answers

1. **Leverage.** Compute leverage at input two. **Answer:** \(1/5+0/10=0.2\).
2. **PRESS.** Compute the center deleted residual. **Answer:** \(-0.8/(1-0.2)=-1\).
3. **Curvature.** What does a U-shaped residual pattern suggest? **Answer:** the conditional mean may not be linear in the included predictor; the pattern alone does not identify its cause.
4. **Heteroskedasticity.** Does a robust standard error repair omitted-variable bias? **Answer:** no; it concerns estimated sampling variance under particular assumptions.
5. **Validation.** Why leave out entire patients instead of individual visits when predicting new patients? **Answer:** repeated visits from one patient share information and would otherwise leak into training.

### Reading and attribution

- Penn State STAT 501, Lesson 4, *Simple Linear Regression Assumptions*, https://online.stat.psu.edu/stat501/Lesson04.
- Penn State STAT 501, Lesson 11, *Influential Points*, https://online.stat.psu.edu/stat501/Lesson11.
- Penn State STAT 501, Lesson 7, *Multiple Regression Assumptions*, https://online.stat.psu.edu/stat501/Lesson07.
