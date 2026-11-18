# 026000 - A Regression Line You Can Derive and Check

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** averages, variance, one-variable derivatives and basic algebra. **Theme:** the least-squares objective, normal equations, fitted values, residuals, and what a regression coefficient means.

<!-- BEGIN SPOKEN LECTURE -->

# A Regression Line You Can Derive and Check

We measure how much a small experimental component stretches under five different loads. The loads are zero, one, two, three, and four units. The measured stretches are one, two, two, four, and five units. We expect stretch to increase with load, but the measurements do not fall on one perfect line. How should we summarize the relationship?

A drawing program can place a line through these points, but what makes one line better than another? We need an objective we can calculate, not simply an impression that the line looks right. We also need to separate the line's useful predictions from stronger claims it cannot make, such as whether load alone caused the observed stretch.

The simplest regression model has two adjustable numbers: an intercept, which tells us where the line crosses the vertical axis, and a slope, which tells us how much the predicted outcome changes when the input increases by one unit. We will derive those two numbers, check them on all five measurements, and then look at the assumptions required to interpret the fitted line as a statistical model rather than just a geometric summary.

## What does it mean to fit a line?

For each input, the line produces a predicted stretch. Subtract that prediction from the actual stretch to get a residual. Some residuals are positive, because the measured point lies above the line. Others are negative, because it lies below the line.

If we simply add residuals, positive and negative errors can cancel. A line that misses wildly in opposite directions might achieve a total residual of zero. A common solution is to square each residual and add the squares. This sum of squared errors is never negative, and large misses receive greater weight than small ones.

Least squares chooses the intercept and slope that make this sum as small as possible. It is a mathematical criterion. It does not by itself say that errors are normal, or that the relationship is causal, or that the line will predict new data well. Those are separate matters.

The squared-error criterion is useful partly because we can solve it exactly. Start by changing only the intercept. If the line sits too low, moving it upward reduces most positive residuals. If it sits too high, moving it downward helps. At the optimum, the sum of residuals must be zero, provided we have included an intercept and used ordinary unweighted least squares.

Next change the slope while adjusting the intercept. A slope that's too shallow makes high-input residuals systematically positive and low-input residuals systematically negative. At the optimum, the input-weighted sum of residuals must also vanish. These two conditions are called the normal equations. They are the equations that force the residual vector to be perpendicular to the two columns used to build the line: the column of ones and the column of input values.

We can solve the normal equations without matrix notation. First average the inputs and outcomes. The fitted line has to pass through the point whose coordinates are those two averages. This is an exact consequence of the zero-sum residual condition. Then calculate how the input and outcome depart from their respective averages. The slope is the sum of the products of those departures divided by the sum of squared input departures. Finally, the intercept is average outcome minus slope times average input.

## The five measurements, one arithmetic step at a time

For our five loads, zero through four, the average input is two. For stretches one, two, two, four, and five, the average outcome is fourteen divided by five, or two point eight.

The input departures from the mean are negative two, negative one, zero, one, and two. Their squares add to ten. The outcome departures from two point eight are negative one point eight, negative point eight, negative point eight, one point two, and two point two.

Multiply the corresponding departures and add. We get three point six, plus point eight, plus zero, plus one point two, plus four point four. The sum is ten. Divide by the input-square sum, also ten, and the fitted slope is exactly one.

To find the intercept, subtract slope times average input from average outcome. Two point eight minus two gives point eight. Our fitted line therefore predicts a stretch of point eight plus one times the applied load.

Let's verify it instead of trusting the formula. At loads zero through four, the line predicts point eight, one point eight, two point eight, three point eight, and four point eight. Subtract these predictions from the actual measurements. The residuals are point two, point two, negative point eight, point two, and point two. They sum to zero.

Now weight each residual by its input and add. Zero times point two, plus one times point two, plus two times negative point eight, plus three times point two, plus four times point two. That is point two minus one point six plus point six plus point eight, again zero. The two normal equations check out.

Square and sum the residuals: four copies of point zero four, and one copy of point six four. The total is point eight. This is the minimum sum of squared errors among all straight lines with a free intercept and slope, because the squared-error objective is a convex quadratic, and our five input values are not all identical.

## What the line explains, and what it does not

There is another useful calculation. If we predicted every stretch by the same constant, the best constant under squared error would be the sample mean, two point eight. The total squared deviation around that mean is ten point eight. Our line reduced that sum to point eight. The fraction removed is ten divided by ten point eight, about ninety-two point six percent. That is the coefficient of determination, called R-squared, for this ordinary regression with an intercept.

An R-squared of ninety-two point six percent means that, for these five points, the fitted line removes that fraction of the total sum of squared deviations relative to predicting their mean. It does not mean the slope is correct ninety-two point six percent of the time. It does not tell us the probability a prediction is right, and it does not prove a causal relationship.

There are situations in which an in-sample R-squared is impressive because the model has memorized patterns that will not recur. Adding more adjustable terms can never increase the training sum of squared residuals. It may decrease it dramatically even when the fitted patterns are noise. The more flexible the model, the more important it is to test prediction on observations that did not guide the fit.

## The mathematical line and the statistical model

So far, our line is an algebraic summary of five pairs of numbers. We have made no claim about how those numbers were produced. To draw conclusions about an unknown population relationship, we need a probability model.

One common model says that, at any specified load, the conditional average stretch equals an intercept plus slope times load. An individual observation equals that conditional mean plus an error. The errors need not be zero in every observation. Instead we often assume that their mean, conditional on the inputs, is zero. If the errors are independent and share a constant variance, we can derive standard formulas for the variability of the estimated intercept and slope. Under additional normality assumptions, exact small-sample t intervals are available.

The requirements should not be bundled into a single vague claim that regression assumes normal data. Ordinary least squares is defined for any numerical dataset. Its coefficient estimates can be useful without normal errors. Normality is an additional assumption for particular exact finite-sample tests and intervals; mean-zero errors and a suitable design play a more basic role in whether the fitted slope targets the intended population slope.

One subtlety concerns the input. In a controlled laboratory, we might set the load deliberately and regard it as fixed. In an observational dataset, both load and response may vary for many reasons. In either case, fitting a line measures how the observed response changes with the recorded input. If another unrecorded factor drives both, the slope need not equal the causal effect of changing the load.

## What changes when measurements have different reliability?

Suppose measurements at large loads are noisier because the sensor reaches the edge of its operating range. Ordinary least squares gives every squared residual equal weight. If we have a reliable model for unequal measurement variances, we might instead assign weights inversely proportional to those variances. That is weighted least squares, and it solves a different fitting objective. Choosing weights merely to favor points we like would not be a sound statistical justification.

Similarly, if one sensor produces ten readings at a fixed load, those readings may be correlated. Treating them as ten independent confirmations of the same slope can exaggerate precision. We should keep track of the experimental units and dependence structure developed in experimental design, even when the eventual calculation is regression.

There is also a distinction between fitting the conditional mean and predicting any individual outcome. A fitted conditional mean may be precise while individual outcomes still vary widely around it. We will need two different intervals: one for uncertainty about the mean response, another for the response of a new unit. Their formulas have almost the same shape, but the individual interval includes an extra source of variance.

## Geometry as a useful way to remember the calculation

Imagine that our five outcomes form a vector with five coordinates. Every line produces another five-coordinate vector: its predicted outcomes at the five measured inputs. As we vary intercept and slope, these fitted vectors move within a two-dimensional plane spanned by the all-ones vector and the input vector.

Least squares chooses the point in that plane closest to the observed outcome vector. The difference between the observed vector and its closest point is perpendicular to the plane. That single geometric fact explains both normal equations, the zero-sum residual property, and why the fitted vector does not change when we add to the data a residual already perpendicular to the model plane.

The picture generalizes immediately. If we include several predictors, each contributes a column to a larger design matrix. Least squares projects the response onto the space spanned by those columns. When columns are dependent, coefficients may not be uniquely determined even though the fitted values are. This is why rank and conditioning matter in numerical regression.

Return to the five loads. The data give an exact least-squares line with slope one and intercept point eight. We know exactly how those numbers were obtained and how to check them. We have not yet decided whether the residuals show curvature, whether a single extreme point is controlling the result, or how wide a prediction interval should be. Deriving a line is the beginning of regression analysis, not its completion.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — least squares and projection

For \(n\) pairs \((x_i,y_i)\), minimize
\[
S(a,b)=\sum_{i=1}^n (y_i-a-bx_i)^2.
\]
Setting derivatives to zero gives \(\sum e_i=0\), \(\sum x_i e_i=0\), where \(e_i=y_i-\hat y_i\). For \(S_{xx}=\sum(x_i-\bar x)^2>0\),
\[
\hat b=\frac{S_{xy}}{S_{xx}},\quad S_{xy}=\sum(x_i-\bar x)(y_i-\bar y),\quad \hat a=\bar y-\hat b\bar x.
\]
For the example \(x=(0,1,2,3,4)\), \(y=(1,2,2,4,5)\): \(\bar x=2\), \(\bar y=2.8\), \(S_{xx}=10\), \(S_{xy}=10\), \(\hat b=1\), \(\hat a=0.8\). Thus
\[
\hat y=(0.8,1.8,2.8,3.8,4.8),\quad e=(0.2,0.2,-0.8,0.2,0.2),\quad \mathrm{SSE}=0.8.
\]
Total sum of squares \(\mathrm{SST}=\sum(y_i-\bar y)^2=10.8\). Therefore \(R^2=1-0.8/10.8=25/27\approx0.925926\).

With \(X\in\mathbb R^{n\times2}\) whose columns are ones and \(x\), the normal equations are \(X^T X\hat\beta=X^T y\). If \(X\) has full column rank, \(\hat\beta=(X^T X)^{-1}X^Ty\) and the residual is orthogonal to the column space of \(X\). For computation with poorly conditioned matrices, prefer QR or SVD over explicitly forming \((X^TX)^{-1}\).

### Exercises with worked answers

1. **Fit by hand.** Fit a line to \((x,y)=(0,2),(1,4),(2,6)\). **Answer:** slope two, intercept two, every residual zero.
2. **Normal equations.** Check \(\sum e_i\) and \(\sum x_i e_i\) for the five-point dataset. **Answer:** both zero; explicit sums appear in narration.
3. **No spread.** What happens if every \(x_i=3\)? **Answer:** \(S_{xx}=0\); with a free intercept, the separate slope and intercept are not identifiable.
4. **Fitting versus causation.** If temperature drives both load selection and observed stretch, does the fitted slope necessarily measure a causal load effect? **Answer:** no; the regression is a conditional association without a design/identification argument.
5. **Residual degrees of freedom.** Under a full-rank two-parameter linear mean model with constant error variance, how many residual degrees of freedom remain for five observations? **Answer:** three, provided the relevant model assumptions hold.

### Reading and attribution

- Penn State STAT 501, Lesson 1, *Simple Linear Regression*, https://online.stat.psu.edu/stat501/Lesson01.
- OpenStax *Introductory Statistics 2e*, Section 12.3, https://openstax.org/books/introductory-statistics-2e/pages/12-3-the-regression-equation.
- Penn State STAT 501, Lesson 4, *Simple Linear Regression Assumptions*, https://online.stat.psu.edu/stat501/Lesson04.
