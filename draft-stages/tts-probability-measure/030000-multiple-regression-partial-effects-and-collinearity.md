# Multiple Regression: What Changes When You Hold Another Variable Fixed?

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 030000  
**Preparation:** Simple least-squares regression, covariance, vectors, and linear equations.  
**Companion:** An exact two-predictor fit and an omitted-variable calculation.

<!-- BEGIN SPOKEN LECTURE -->

A school finds that students who study more hours tend to score higher on an exam. Does another hour of study predict a fixed improvement? Perhaps students taking harder courses both study more and face harder exams. Perhaps prior preparation affects both study time and score. A regression line involving only study time can summarize the observed association, but it cannot separate two predictors that vary together. Multiple regression addresses a more precise mathematical question: how does the fitted response change with one input when the other recorded inputs are held fixed?

Start with a model containing an intercept and two numerical predictors. We write the fitted outcome as intercept plus beta one times x, plus beta two times z. For every observation, the residual is observed outcome minus fitted outcome. Ordinary least squares chooses the three coefficients to minimize the sum of squared residuals. This is the same least-squares principle as the one-predictor case; we have added one column to the design matrix.

Let's solve an example, not merely describe the formula. Four observations have inputs x equal to zero, one, one, and two. Their other input z is zero, zero, one, and one. Outcomes y are two, two, five, and nine. The average x is one, the average z is one half, and the average y is four point five. Around those averages, the sum of squared deviations of x is two and the sum of squared deviations of z is one. The cross-product sum of x and z is one. The cross-product sum of x and y is seven; that of z and y is five.

If we regress y on x alone, the slope is seven divided by two, or three point five. This is a perfectly valid description of the least-squares association in these four points. But it combines the relationship of y to x with the fact that high x values also tend to accompany high z values. The model has no way to distinguish those two sources of variation.

Add z to the regression. The two centered normal equations are: two times beta one plus one times beta two equals seven; and one times beta one plus one times beta two equals five. Subtract the second equation from the first. Beta one is two. Substitute back, and beta two is three. The intercept is average y minus two times average x minus three times average z: four point five minus two minus one point five, giving one.

The fitted values are therefore one, three, six, and eight. The residuals are one, negative one, negative one, and one. Check their sum: zero. Multiply them by x and sum: zero. Multiply them by z and sum: zero. These are precisely the three normal equations. The squared residuals sum to four. Nothing about this tiny dataset establishes a population law, but the finite calculation is exact.

Why did the x coefficient fall from three point five to two? The omitted z predictor has a coefficient of three, and in these four observations z increases with x. In fact the centered cross-product of x with z, divided by the centered square sum of x, equals one half. The simple-regression slope becomes two plus three times one half, which is three point five. This is an exact algebraic decomposition for this fitted dataset, not a causal theorem. It shows how leaving out a correlated predictor changes a least-squares coefficient.

The phrase 'holding z fixed' is important, but it does not turn an observational regression coefficient into a causal effect. We are comparing fitted outcomes at different x values for the same value of z, within the model. Whether changing x while holding z fixed is a physically possible intervention, and whether the measured covariates remove confounding, are separate questions. If an omitted variable influences both x and y, beta one may still be misleading as a causal estimate. If z is a mediator of the effect of x, controlling for it changes which effect is being estimated. If z is a collider, conditioning on it can create an association. Regression algebra does not decide which causal structure applies.

There is a deeper geometric way to understand beta one. First remove from x the part that can be explained by the intercept and z. Also remove from y the part that can be explained by the intercept and z. Regress the remaining part of y on the remaining part of x. The slope is exactly the multiple-regression coefficient of x. This is the Frisch-Waugh-Lovell partialling-out identity when the relevant rank conditions hold. It says that beta one is determined by the variation in x not already linearly predictable from the other included columns.

That identity also reveals a danger. What if x and z almost always rise together? After removing the part of x explained by z, very little x variation remains. The denominator of the partial regression slope is then very small. Small errors in observations or small changes in the sample can lead to large changes in individual coefficients. This is multicollinearity. Predictions based on the combined direction of x and z can remain stable even when a unique allocation of the effect between the two coefficients is unstable.

At exact collinearity, such as z always equal to twice x with an intercept included, the design matrix loses column rank. There is no unique pair of beta one and beta two. Many coefficient choices make exactly the same fitted predictions. A software package may return one solution by convention or use a pseudoinverse. That numerical choice does not manufacture information the data lack. When interpreting coefficients, we should ask which combinations are identifiable from the design.

The computational form is straightforward. Stack the observed outcomes into a vector y. Make a design matrix X with a column of ones, a column of x values, and a column of z values. We want the vector of coefficients beta minimizing the squared norm of y minus X beta. At an optimum, the residual is perpendicular to every column of X. So X transpose times X times beta equals X transpose times y. These are the normal equations. When X has full column rank there is a unique least-squares coefficient vector.

One should not necessarily solve the normal equations by explicitly inverting X transpose X. The matrix X transpose X squares the condition number of X in the standard two-norm when X has full rank. If columns are nearly dependent, that can make a numerical problem substantially harder. QR decomposition or singular-value decomposition is generally a safer computational route. This is exactly where regression, optimization, and numerical linear algebra describe the same calculation from different angles.

What about uncertainty? Least squares is defined even if the residuals are not normally distributed. But a standard error for beta one is not determined by geometry alone. Under a common homoskedastic independent-error model with fixed full-rank design, and conditional mean zero, the covariance matrix of the coefficient estimator is sigma squared times the inverse of X transpose X. Estimating sigma squared from residuals also requires appropriate degrees of freedom: n minus the number of fitted independent columns. In our four-observation, three-parameter example, only one residual degree of freedom remains. That is far too little for strong empirical confidence in error assumptions.

Correlated errors or changing error variances require different uncertainty calculations. Predictors selected after examining the outcomes complicate interpretation. Fitted coefficients may be precise in-sample but fail under distribution shifts. And a new predictor can always weakly reduce the least-squares training error, even when it hurts predictions on new data. Multiple regression increases expressiveness; it does not remove the need for model criticism.

We can now give a precise answer to the opening question. A simple fitted slope describes how the response varies along the observed mixture of x and z. A multiple-regression coefficient describes the fitted change in response with x at fixed recorded z. The distinction is algebraically exact. Interpreting either as a causal effect or a reliable forecast requires evidence beyond the normal equations. The useful mathematical connection is that partialling-out, orthogonal projection, covariance, and numerical conditioning are not separate tricks. They are different views of one least-squares problem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For \(x=(0,1,1,2)\), \(z=(0,0,1,1)\), \(y=(2,2,5,9)\), the centered cross-products are \(S_{xx}=2\), \(S_{zz}=1\), \(S_{xz}=1\), \(S_{xy}=7\), \(S_{zy}=5\). The simple slope of y on x is \(7/2\). The multiple slopes solve
\[
\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}\beta_x\\\beta_z\end{pmatrix}=
\begin{pmatrix}7\\5\end{pmatrix},\quad (\beta_x,\beta_z)=(2,3),\quad\beta_0=1.
\]
Fitted responses \((1,3,6,8)\), residuals \((1,-1,-1,1)\), SSE \(4\). The identity \(\hat\beta_{x,\text{simple}}=\hat\beta_{x,\text{multiple}}+\hat\beta_{z,\text{multiple}}S_{xz}/S_{xx}\) holds for this centered two-predictor least-squares fit.

With design matrix \(X\), full column rank and \(y=X\beta+\varepsilon\), \(E[\varepsilon\mid X]=0\), \(\operatorname{Cov}(\varepsilon\mid X)=\sigma^2I\), we have \(\hat\beta=(X^\top X)^{-1}X^\top y\) and \(\operatorname{Cov}(\hat\beta\mid X)=\sigma^2(X^\top X)^{-1}\). Computational practice usually favors QR or SVD instead of forming this inverse.

### Exercises and answers

1. **Reproduce the fit.** Compute the x coefficient after controlling for z. **Answer:** Solve the two centered equations to obtain two.
2. **Omitted-variable decomposition.** Why is the simple slope three point five? **Answer:** Two plus three times the x-z simple slope, one half.
3. **Rank.** If z equals twice x for every observation, what happens to the separate x and z coefficients? **Answer:** They are not uniquely identifiable; only a combination is determined.
4. **Interpretation.** Does holding observed z fixed establish the causal effect of x? **Answer:** No; intervention, unmeasured confounding, selection, and causal roles remain open.

### Reading and attribution

- Penn State STAT 501, Lesson 7, *Multiple Regression Estimation*: https://online.stat.psu.edu/stat501/lesson/7.
- Hernan and Robins, *Causal Inference: What If*, https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/.
- The four-observation regression and omitted-variable calculation are original teaching examples.
