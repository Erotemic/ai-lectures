# One Fit, Three Mathematical Languages: Projection, Optimization, and Statistical Evidence

<!-- BEGIN SPOKEN LECTURE -->

# One Fit, Three Mathematical Languages: Projection, Optimization, and Statistical Evidence

Imagine recording the output of a small instrument at three settings. The setting is zero and the response is one. At setting one, the response is two. At setting two, the response is also two. We want a straight line to summarize the measurements. What is the right line, how accurately have we found it, and what can it legitimately predict?

These may sound like three questions belonging to three subjects. Linear algebra explains the geometry of the fitted line. Optimization explains why no competing line has a smaller sum of squared residuals. Probability explains what we may learn about a hidden relationship, but only after we declare what made the measurements random. The same calculation acquires three interpretations without changing its arithmetic. This is one of the most useful connections in applied mathematics.

## Turning a line into a vector problem

A line has an intercept, called a, and a slope, called b. At input x, its predicted output is a plus b times x. With our three inputs zero, one, and two, its predicted outputs are a, a plus b, and a plus two b. The measurements form a vector with entries one, two, two. The predictions form another three-dimensional vector.

Notice what has happened. We are not trying to force three observations to equal two unknowns exactly. We are looking for the point among all prediction vectors of the form a times the vector one, one, one, plus b times the vector zero, one, two, which lies closest to the observations.

The set of possible predictions is a plane through the origin in three-dimensional measurement space. Its two spanning vectors represent the intercept and the slope. Their span is the column space of the design matrix. Finding the best line is equivalent to projecting the observation vector onto that plane.

This picture also explains residuals. A residual is observed minus predicted. At the best fit, the residual vector must be perpendicular to the entire prediction plane. If it had a component parallel to that plane, we could adjust the line in that direction and make the squared distance smaller.

We can write this orthogonality as two equations. The residuals must sum to zero, because the all-ones vector belongs to the prediction plane. And the residuals weighted by their x-values must sum to zero, because the vector zero, one, two also belongs to that plane. These are the normal equations, but their meaning is geometric before it is algebraic.

## The calculation, all the way through

Let the residual for the first observation be one minus a, the second be two minus a minus b, and the third be two minus a minus twice b. We minimize the sum of their three squares. Differentiating with respect to a and to b gives two linear equations: three a plus three b equals five; three a plus five b equals six.

Subtract the first equation from the second. Twice b equals one. The slope is one half. Substitute back: the intercept is seven sixths. Our fitted line predicts seven sixths, five thirds, and thirteen sixths. The residuals are minus one sixth, plus one third, and minus one sixth. The middle reading lies above the fitted line, and the outer readings lie below it.

Check the orthogonality directly. Add the three residuals: minus one sixth plus two sixths minus one sixth is zero. Multiply them by the inputs and add: zero plus two sixths minus two sixths is also zero. No arithmetic trick is hiding here. These two identities certify that the residual is perpendicular to every prediction the model can make.

Now compute the squared error. One thirty-sixth plus four thirty-sixths plus one thirty-sixth equals one sixth. The squared norm of the residual is therefore one sixth. Every other line has a residual squared norm at least that large. We can prove this without searching through all possible slopes and intercepts. If another line changes the predictions by a vector inside the prediction plane, the residual of the new line is the old residual minus that vector. Because those two components are perpendicular, their squared lengths add. The increase in squared error is exactly the squared length of the change in predictions.

This is a global optimality certificate, not just a first-order test. The quadratic is convex. And because our two design columns are linearly independent, the coefficient pair is unique.

## Why the normal equations are not always the best algorithm

The normal equations are wonderfully transparent on paper. In numerical work we must be more careful. The design matrix has three rows and two columns. The normal-equation matrix is formed by multiplying the transpose of the design matrix by the matrix itself. This multiplication can make a sensitivity problem worse: for a full-column-rank matrix, the two-norm condition number of the normal-equation matrix is the square of the condition number of the original matrix.

Suppose the x-values were all clustered near a million, differing by only tiny amounts. Then the intercept column and the slope column would become difficult to distinguish numerically. The normal equations would magnify that difficulty. A QR factorization solves the least-squares problem by using orthogonal transformations instead of forming the cross-product matrix. An SVD exposes directions that the data cannot determine reliably. Centering and scaling the x-values can also improve the representation, provided we interpret the coefficients in the original units afterward.

A small residual does not prove that the slope has been determined precisely. If all our x-values are nearly equal, many different slopes can produce predictions that scarcely differ on the measured range. The geometry of approximation and the geometry of parameter uncertainty are related, but they are not identical.

## Probability enters through assumptions, not through the minimizer

So far there has been no probability in the problem. We have three numbers and an optimization rule. We could compute a fitted line even if the observations were hand-drawn or deliberately manipulated. To call the coefficients estimators, or to attach confidence intervals, we must specify a statistical model.

Consider the model in which each measured response equals a true intercept plus a true slope times the chosen input, plus a noise term. Assume the inputs are fixed and the noise terms have mean zero, are uncorrelated, and have the same variance, which we call sigma squared. Under these assumptions, ordinary least squares produces unbiased estimates of the intercept and slope. Their covariance matrix is sigma squared times the inverse of the design cross-product matrix. If the errors are additionally jointly normal, we obtain exact normal sampling distributions for the coefficients, conditional on the chosen inputs.

For our three x-values, the inverse cross-product matrix has first row five sixths, minus one half, and second row minus one half, one half. Therefore the variance of the estimated slope is sigma squared divided by two. The slope's standard error would be sigma divided by the square root of two if sigma were known. Notice that this uncertainty calculation is not the residual. It describes variation in the fitted slope across hypothetical repeated samples under the model.

If sigma is unknown, we may estimate its variance by dividing the squared residual norm by the residual degrees of freedom. We have three observations and two fitted coefficients, leaving only one degree of freedom. Our residual norm squared was one sixth, so the estimated noise variance is one sixth, and the estimated slope standard error is the square root of one twelfth. But one degree of freedom is very little evidence about an unknown noise variance. A familiar normal-based plus-or-minus two standard-error interval would not have the claimed coverage here. Under normal errors and the stated assumptions, the appropriate exact small-sample interval uses a Student t distribution with just one degree of freedom; it is very wide.

It is possible to calculate a tidy line and still have a weak inferential result. That is a feature of the mathematics, not a defect in the implementation.

## When the errors do not have equal variance

Suppose the first observation came from a precise laboratory instrument, while the next two came from a much noisier sensor. Assigning all three squared residuals equal weight no longer reflects the relative information in the measurements. If we know their noise variances and the errors are uncorrelated, we can minimize the sum of each squared residual divided by its variance.

This is weighted least squares. Geometrically, it changes the metric used to measure distance in observation space. Statistically, it is maximum likelihood under independent Gaussian noise with those variances. The fitted residual is orthogonal to the model plane in the weighted inner product, not necessarily in the ordinary dot product. If errors are correlated, a full covariance matrix can replace the diagonal weights. When the covariance is positive definite, whitening transforms the problem into ordinary least squares in a transformed space.

Each interpretation imposes a different responsibility. Geometry asks whether the prediction space and metric are correct. Optimization asks whether the chosen algorithm reaches or certifies the minimizer. Statistics asks whether the noise model is credible and whether the design carries enough information to answer the scientific question.

## Why regularization changes the question

Now suppose measurements barely constrain a coefficient. One common response is ridge regularization: add a nonnegative penalty proportional to the squared size of the coefficients. This can improve numerical conditioning and reduce variance, but it generally changes the fitted coefficients. It is not the same as choosing a more stable numerical algorithm for the original least-squares problem.

QR can compute the original minimizer more reliably. Ridge deliberately chooses a different minimizer, balancing agreement with observations against a preference for smaller coefficients. The penalty should also respect units and the role of the intercept; penalizing an intercept measured in volts the same way as a slope measured in volts per second is not automatically sensible.

The distinction matters when someone says an algorithm is more accurate. More accurate at solving which problem? Better at predicting new measurements under which assumptions? Less sensitive to noise in what parameterization? We should ask these questions before accepting a performance claim.

## A common structure, three honest conclusions

Return to the three observations: one, two, two. The line has intercept seven sixths and slope one half. The residual is orthogonal to every possible change in fitted predictions. That gives us a proof that the line minimizes squared error. QR or an SVD would let us compute the same target without squaring a troublesome condition number. A stochastic noise model, if justified, adds uncertainty statements about the coefficients and predictions.

The deeper lesson is that the mathematics does not suddenly become statistical when we put the word regression on a matrix calculation. Probability enters when we specify how observations could have varied. Likewise, a least-squares objective does not automatically make a numerical output reliable; we still need to consider conditioning and finite precision. By keeping these layers distinct and relating them precisely, we can use one simple fitted line as a model for much more ambitious inverse problems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Geometry and a complete small calculation

For fixed design matrix and observations,

\[
X=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad y=\begin{pmatrix}1\\2\\2\end{pmatrix},\qquad
\min_{\beta\in\mathbb R^2}\|X\beta-y\|_2^2.
\]

\[
X^TX=\begin{pmatrix}3&3\\3&5\end{pmatrix},\quad X^Ty=\begin{pmatrix}5\\6\end{pmatrix},\quad
\hat\beta=\begin{pmatrix}7/6\\1/2\end{pmatrix},\quad
r=y-X\hat\beta=\begin{pmatrix}-1/6\\1/3\\-1/6\end{pmatrix}.
\]

\(X^Tr=0\) and \(\|r\|_2^2=1/6\). For every \(h\in\mathbb R^2\),

\[
\|y-X(\hat\beta+h)\|_2^2=\|r-Xh\|_2^2=\|r\|_2^2+\|Xh\|_2^2.
\]

Since \(X\) has full column rank, the minimum is unique.

### Statistical statements and their hypotheses

Under \(y=X\beta+\varepsilon\), with fixed full-rank \(X\), \(E\varepsilon=0\), \(\operatorname{Cov}(\varepsilon)=\sigma^2I\),

\[
E\hat\beta=\beta,\qquad \operatorname{Cov}(\hat\beta)=\sigma^2(X^TX)^{-1}
=\frac{\sigma^2}{6}\begin{pmatrix}5&-3\\-3&3\end{pmatrix}.
\]

With independent normal errors, \((\hat\beta_j-\beta_j)/(\hat\sigma\sqrt{(X^TX)^{-1}_{jj}})\sim t_{n-p}\), where \(\hat\sigma^2=\|r\|^2/(n-p)\) and here \(n-p=1\). Without the Gaussian assumption the exact Student t conclusion does not follow.

### Weighting, conditioning and regularization

For a positive definite covariance \(\Sigma\), generalized least squares minimizes \((y-X\beta)^T\Sigma^{-1}(y-X\beta)\), giving \(X^T\Sigma^{-1}(y-X\hat\beta)=0\). If \(X\) has full column rank, \(\kappa_2(X^TX)=\kappa_2(X)^2\). QR and SVD are preferred to unguarded normal equations for sensitive numerical problems. Ridge minimizes \(\|X\beta-y\|^2+\lambda\|P\beta\|^2\); unless \(\lambda=0\) or the penalty is inactive, the target differs from ordinary least squares.

### Exercises and solutions

1. **Certificate.** Find the squared error when the fitted slope increases by \(1/2\) and intercept stays fixed. **Answer:** \(h=(0,1/2)\), \(Xh=(0,1/2,1)\); squared error becomes \(1/6+5/4=17/12\).
2. **Shift the inputs.** Replace each input \(x\) by \(z=x-1\). Find the fitted intercept and slope as functions of \(z\). **Answer:** intercept \(5/3\), slope \(1/2\); fitted predictions and residuals are unchanged.
3. **Inferential precision.** With known \(\sigma^2=2\), find the variance of the estimated slope. **Answer:** \(1\). This is a coefficient variance, not the residual variance for the observed dataset.
4. **Rank failure.** If all the inputs are \(x=1\), can intercept and slope be identified separately? **Answer:** no; design columns are equal and only their sum is identified.
5. **Algorithm vs model.** Distinguish an SVD computation of ordinary least squares from ridge regression. **Answer:** SVD can solve the unchanged least-squares objective; ridge modifies it by a penalty, usually changing the estimate.

### Sources and further reading

- [Jim Hefferon, *Linear Algebra*](https://hefferon.net/linearalgebra/), projections and least squares.
- [MIT OpenCourseWare 18.06SC, *Linear Algebra*](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), column spaces, orthogonal projections and matrix factorizations.
- [Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*](https://people.maths.ox.ac.uk/trefethen/text.html), QR and sensitivity.
- [Penn State STAT 501, Multiple Regression](https://online.stat.psu.edu/stat501/), statistical interpretation and assumptions.
- Related lectures: `linear-algebra:006000`, `linear-algebra:021000`, `probability-measure:026000`, `probability-measure:030000`, `multivariable-calculus:023000`.
