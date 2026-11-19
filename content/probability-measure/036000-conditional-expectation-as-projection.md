# Conditional Expectation as Projection: Why Regression Is Only One Kind of Prediction

<!-- BEGIN SPOKEN LECTURE -->

# Conditional Expectation as Projection: Why Regression Is Only One Kind of Prediction

You have measured an input X and want to predict an output Y. Perhaps X is the speed of a machine and Y is its wear. Perhaps X is the time of day and Y is demand for electricity. A familiar first step is to draw a scatterplot and fit a straight line. But what if the true relationship bends upward on both sides of zero? A linear fit can then be nearly flat, even when the input strongly determines the output.

This is not merely a warning about choosing the wrong curve. It points to a general mathematical fact. Under squared-error loss, the best prediction of Y from all available information about X is the conditional expectation of Y given X. That statement belongs to probability. Its proof is an orthogonal-projection argument, which belongs to linear algebra and functional analysis. Ordinary linear regression is a smaller projection onto a restricted family of functions. Seeing the two projections side by side clarifies what regression can and cannot tell us.

## Start with three possible inputs

Let X take the values minus one, zero, and plus one, each with probability one third. Define the output Y to be X squared plus an independent noise term E. Assume the noise has mean zero and variance sigma squared. Its distribution need not be Gaussian for the argument we are about to make.

When X is minus one, the noiseless part of Y is one. When X is zero, it is zero. When X is plus one, it is one again. In other words, the average output is one at both ends and zero in the middle. This is a perfectly predictable pattern at the level of conditional means, but it is not a rising or falling straight line.

First compute the average input. It is zero, because minus one and plus one cancel. Next compute the average of X squared. Two of the three input values have square one, so the average of X squared is two thirds. Since the noise has mean zero, the average output Y is also two thirds.

Now ask what straight line gives the smallest expected squared prediction error. Write a line as a plus b times X. The optimal intercept is the mean of Y minus b times the mean of X. Since the input mean is zero, the intercept must be two thirds regardless of b. The optimal slope is the covariance of X and Y divided by the variance of X, provided the input variance is nonzero.

What is that covariance? It is the average of X times Y because the mean of X is zero. The noise contributes zero, by independence and mean zero. The remaining term is the average of X cubed. But X cubed is minus one, zero, or plus one with equal weights, so its mean is zero. Therefore the covariance is zero, and the best straight-line slope is zero.

We have reached a striking result. The optimal linear predictor ignores X entirely and predicts two thirds every time. Yet the best nonlinear predictor uses X in an exact and simple way: predict X squared.

## Compare the prediction errors exactly

The ideal predictor based on X is X squared. When we use it, the prediction residual is exactly the noise E. Its mean squared error is sigma squared.

The fitted linear predictor is the constant two thirds. Its error is X squared minus two thirds, plus E. The two terms are uncorrelated because E is independent and has mean zero. So its mean squared error is the variance of X squared plus sigma squared.

Compute that variance. Because X squared is either zero or one, the expectation of its fourth power is the same as the expectation of X squared: two thirds. Subtract the square of its mean, which is four ninths. The variance is two ninths. The optimal linear predictor therefore has mean squared error sigma squared plus two ninths, while the nonlinear conditional-mean predictor has error sigma squared.

Even when the measurement noise is extremely small, the straight line leaves behind a nonzero modeling error of two ninths. The data may contain a very strong relationship even though its Pearson correlation is zero. Covariance measures linear association, not all statistical dependence.

There is a lesson here for real data analysis. A zero regression slope does not by itself establish that the input is irrelevant to prediction. And adding a squared term is not always enough; the appropriate function class depends on the question and the evidence. But we can understand why a richer class is sometimes needed by looking at projection geometry.

## Predictions form a space of random variables

Imagine the set of random variables with finite second moments. We can add them and multiply them by scalars. We can also define an inner product: the expected product of two random variables. Two random variables are orthogonal when their expected product is zero. The corresponding squared distance between a prediction and a target is the expected squared prediction error.

Now choose a collection of candidate predictors. If we allow only constants and multiples of X, we have a two-dimensional linear space consisting of expressions a plus b X. Ordinary population linear regression chooses the member of this space closest to Y in mean squared error. Its residual is orthogonal to the constant function and to X. Those two orthogonality conditions are the population normal equations.

But we might allow every square-integrable function of X, not just straight lines. This is a much larger space. It contains X squared, indicator functions of whether X exceeds a threshold, and countless other transformations. The conditional expectation of Y given X is the orthogonal projection of Y onto this space. The residual after conditioning is orthogonal to every square-integrable function of X.

That last claim deserves a proof idea, not just a slogan. Let m of X denote the conditional expectation of Y given X. The defining property of conditional expectation says that, whenever we multiply the residual Y minus m of X by a suitable function of X and take its expectation, the answer is zero. The output of that function is determined entirely by X, so the conditional residual has no remaining linear correlation with any square-integrable transformation of the information we conditioned on.

This is much stronger than having zero covariance with X itself. A residual can be uncorrelated with X while still being predictably related to X squared. The difference between these two statements is exactly the difference between linear regression and unrestricted conditional-mean prediction.

## The Pythagorean theorem in prediction space

Let m of X be the conditional expectation. Take any alternative square-integrable predictor g of X. Write the prediction error Y minus g as two pieces: Y minus m, plus m minus g. The first part is the irreducible residual after using X. The second is the avoidable error caused by using the wrong prediction function.

When we square the sum and take expectation, a cross term appears. But that cross term is zero because the conditional residual is orthogonal to every function of X, including m minus g. Therefore the total mean squared error equals the minimum attainable mean squared error, plus the expected square of the gap between g and m.

This identity proves optimality. No predictor using only X can beat the conditional mean under squared error. It also quantifies precisely how much performance is lost by restricting the function family. In our example, when g is the best straight line, that excess error is two ninths.

If we take g to be the unconditional mean of Y, the same decomposition gives the law of total variance. The total variance of Y is the average conditional variance of Y given X, plus the variance of the conditional mean as X varies. One part represents uncertainty that remains even after X is known. The other represents variation that knowing X can explain.

In our example, the first part is sigma squared, because the conditional noise variance is constant. The second is two ninths, because the conditional mean is X squared. The total variance of Y is their sum. This tells us what fraction of variability is potentially predictable from X, without insisting that predictability must be linear.

## Conditioning on information, not only on numbers

We have spoken as though conditioning always means knowing one numerical variable. More generally, we condition on a collection of information: a sigma algebra. It specifies which events and quantities an observer can distinguish. The conditional expectation is the best square-integrable approximation to Y using that information.

This viewpoint explains a fact sometimes called the tower property. Suppose we know detailed information first, then deliberately forget part of it. We can predict Y from the detailed information and then take the conditional expectation of that prediction using the coarser information. The result is the same as predicting Y directly using the coarser information.

Geometrically, we are projecting onto a smaller subspace inside a larger subspace. Projecting first onto the large space and then onto the nested smaller one gives the same final result as projecting directly onto the small space. This is a useful connection between nested conditional expectations and nested linear subspaces.

It also clarifies what happens when we add features to a predictive model. At the population level, granting a predictor access to more information cannot increase the *minimum possible* expected squared error; the old predictor remains available. In a finite sample, however, a fitted flexible model can generalize worse because estimating a complicated function from limited data introduces variance and can overfit. Population optimality is not a guarantee about an estimated model's out-of-sample performance.

## Different losses produce different predictions

We should not turn the conditional mean into a universal prediction rule. Its optimality depends on squared-error loss. Suppose large errors are penalized in proportion to their absolute magnitude rather than their square. A conditional median minimizes expected absolute error, under the usual conditions. For classification with zero-one loss, the best label is a most probable class given the available information. For probabilistic classification with log loss, reporting the true conditional probability distribution is optimal when the relevant expectations exist.

A mathematical prediction problem must therefore specify three ingredients: the information available, the class of predictions permitted, and the loss function used to judge them. Much apparent disagreement about the 'best predictor' disappears when these ingredients are made explicit.

And prediction does not automatically establish causation. Our construction describes what we can infer about Y when X is observed. It does not say what would happen if an intervention forced X to a new value. Observational relationships can be produced by common causes, selection, or feedback. Conditional expectation is a tool for prediction; causal interpretation requires additional assumptions and designs.

## The connection to least squares and statistical modeling

In finite-dimensional least squares, a design matrix determines a column space of possible predicted data vectors. The residual is perpendicular to that column space. In population regression, a chosen collection of feature functions determines a subspace of random variables, and the residual is orthogonal to those features. Conditional expectation extends the same geometry to all square-integrable quantities measurable using the available information.

This geometric progression is powerful. We can understand a regression line as a projection, a nonlinear regression as a projection onto a larger function class, and an ideal conditional predictor as the projection onto the full information space. Statistics then asks how to estimate such predictions from finite samples, how to control overfitting, and how uncertainty should be reported.

Our three-point input example made the distinction impossible to miss. The fitted straight line had zero slope, but the conditional mean had a clear U-shaped pattern. The correct conclusion was not that the input carried no information. It was that the class of straight lines could not express the relationship. Understanding that difference is the beginning of sensible regression, feature design, and statistical learning.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Exact population example

Let \(P(X=-1)=P(X=0)=P(X=1)=1/3\), and \(Y=X^2+\varepsilon\), where \(E\varepsilon=0\), \(\operatorname{Var}(\varepsilon)=\sigma^2\), and \(\varepsilon\) is independent of \(X\). Then
\[
E[X]=0,\quad E[X^2]=2/3,\quad E[X^3]=0,\quad E[X^4]=2/3,
\quad E[Y\mid X]=X^2.
\]

The population linear projection on \(\operatorname{span}\{1,X\}\) has coefficients \((a,b)=(2/3,0)\) because \(\operatorname{Cov}(X,Y)=0\). Its risk is
\[
E[(Y-2/3)^2]=\sigma^2+\operatorname{Var}(X^2)=\sigma^2+2/9,
\]
while the conditional-mean risk is \(E[(Y-X^2)^2]=\sigma^2\).

### Projection identity and total variance

For \(Y\in L^2\) and \(\mathcal G=\sigma(X)\), let \(m=E[Y\mid\mathcal G]\). For every \(g\in L^2(\mathcal G)\),
\[
E[(Y-g)^2]=E[(Y-m)^2]+E[(m-g)^2],
\quad E[(Y-m)g]=0.
\]
In particular,
\[
\operatorname{Var}(Y)=E[\operatorname{Var}(Y\mid X)]+
\operatorname{Var}(E[Y\mid X]).
\]
Nested projections yield \(E[E[Y\mid\mathcal H]\mid\mathcal G]=E[Y\mid\mathcal G]\) whenever \(\mathcal G\subseteq\mathcal H\) and the required integrability holds.

### Exercises and solutions

1. **Expand the features.** Fit \(a+bX+cX^2\) to the noiseless target \(Y=X^2\) in the population. **Answer:** \((a,b,c)=(0,0,1)\), exactly; the features are linearly independent on the three-point support.
2. **Compute a risk.** Let \(\sigma^2=1/9\). What are the risks of the best linear and conditional-mean predictors? **Answer:** \(1/3\) and \(1/9\), respectively.
3. **Residual test.** For the best linear predictor, compute the expectation of the residual times \(X^2\). **Answer:** \(E[(X^2-2/3)X^2]=2/3-4/9=2/9\), not zero. The residual is orthogonal to X but not to all functions of X.
4. **Information increase.** Does adding X squared to the feature set necessarily reduce test error in a finite sample? **Answer:** no; it expands the population class but may increase estimation variance and overfitting in a sample.
5. **Different loss.** Under absolute-error loss, what summary of the conditional distribution is optimal? **Answer:** any conditional median, rather than necessarily its mean.

### Sources and further reading

- [MIT OpenCourseWare 18.125 Measure and Integration](https://ocw.mit.edu/courses/18-125-measure-and-integration-fall-2003/), conditional expectation as an \(L^2\) projection.
- [Penn State STAT 501, Regression Methods](https://online.stat.psu.edu/stat501/), linear model assumptions and residual orthogonality.
- [Trevor Hastie, Robert Tibshirani, and Jerome Friedman, *The Elements of Statistical Learning*](https://hastie.su.domains/ElemStatLearn/), model classes and prediction error.
- Related lectures: `probability-measure:005000`, `probability-measure:026000`, `probability-measure:027000`, `linear-algebra:006000`, `linear-algebra:028000`.
