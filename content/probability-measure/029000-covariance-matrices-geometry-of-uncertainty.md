# Covariance Matrices: The Geometry of Uncertainty

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 029000  
**Preparation:** Variance and covariance of two variables, vectors, and matrix multiplication.  
**Companion:** A two-dimensional dataset, eigenstructure, and proof of positive semidefiniteness.

<!-- BEGIN SPOKEN LECTURE -->

Suppose two sensors measure changes in a machine. Each sensor varies, and the variation of each alone can be summarized by a variance. But the machine's most interesting motion may not belong to either sensor separately. Perhaps the two readings rise together. Perhaps one rises as the other falls. To understand the variation of the pair, we must describe not only how much each sensor changes, but how the changes relate.

For two random quantities X and Y, covariance is the expected product of their deviations from their means. When the deviations tend to have the same sign, covariance is positive. When one tends to be above its mean while the other is below, it is negative. When their centered product averages to zero, the covariance is zero. That does not generally imply independence. A curved relationship, such as Y equal to X squared for a symmetric distribution of X, can have zero covariance while Y remains entirely determined by X.

Now collect several measurements into one random vector. Let its components be X one through X p, and let its mean be the vector of component means. The covariance matrix has, in position i comma j, the covariance of component i with component j. Its diagonal entries are individual variances. Its off-diagonal entries record pairwise relationships. Because covariance is symmetric, the matrix is symmetric. This is not merely a convenient rectangular table. It defines the variance of every linear combination of the measurements.

Take a vector of numerical coefficients a. Form the random quantity a one times X one, plus a two times X two, and so on. Its variance is a transpose times the covariance matrix times a. This identity comes from expanding the square of the centered sum. It is valuable because the coefficients might represent how we combine sensors, construct a portfolio, compute a weighted estimate, or form a direction through data. One matrix tells us the uncertainty of every possible linear combination.

There is an immediate constraint on which symmetric matrices can be covariance matrices. A variance cannot be negative. Therefore a transpose Sigma a must be nonnegative for every coefficient vector a. A symmetric matrix with this property is called positive semidefinite. An arbitrary table of variances and covariances that violates this condition cannot describe a genuine joint distribution. This observation also explains why numerical estimates of covariance may need care: a collection of inconsistent separately estimated correlations might fail to be positive semidefinite even if every individual pair looks plausible.

Let's calculate a small dataset. Four paired sensor readings are negative two and negative one; negative one and negative two; one and two; and two and one. The average of each coordinate is zero. Each coordinate has a sum of squared deviations equal to ten. The sum of the products of the two coordinates is eight. Using the population-style divisor four for this finite list gives a covariance matrix with two point five on its diagonal and two on each off-diagonal. If these were an independent sample used to estimate a population covariance under the usual sample convention, we would divide the centered sums by three instead. The matrix entries would then be ten over three and eight over three. The two conventions differ by a positive scaling factor; they have the same directions of variation.

What does this matrix tell us? Consider the direction in which both sensors rise together. Add the coordinates and scale to a unit vector. Along this direction, the variance is four point five under the divisor-four convention. Consider the direction in which one sensor rises while the other falls. Subtract the coordinates and scale to a unit vector. Along this direction, the variance is only point five. The cloud of data stretches much farther along the rising-together diagonal than along the opposing diagonal. In ordinary geometry we might draw an elongated ellipse. The covariance matrix determines its orientation and axis scales.

Those directions are eigenvectors. Multiplying the covariance matrix by the vector pointing equally in both coordinates returns four point five times that same vector. Multiplying by the opposite-sign direction returns point five times that direction. The eigenvalues tell us the variance of the corresponding unit-length directional measurements. The sum of the eigenvalues is five, equal to the trace of the matrix and to the sum of individual coordinate variances. In this example, ninety percent of the total coordinate variance lies along the rising-together direction, because four point five divided by five is ninety percent.

It is worth pausing on the meaning of this calculation. The diagonal variances alone were equal: two point five for each sensor. If we had looked only at those numbers, we would have seen no preferred sensor. But the joint covariance reveals a preferred direction between the axes. The information lives in the relationship, not in either measurement alone.

We can standardize each variable by subtracting its mean and dividing by its standard deviation, when that deviation is nonzero. The covariance matrix of these standardized variables is the correlation matrix. Its diagonal entries are one. The off-diagonal entries are unitless correlations, bounded between negative one and one. This is useful when one coordinate measures millimeters and another degrees, because raw covariance magnitudes depend on units. But standardization changes the question. It gives equal marginal variance to each coordinate regardless of their original physical scales. In a mechanical system where a millimeter has a defined engineering meaning, throwing away that scale may or may not be appropriate.

The covariance matrix also describes uncertainty in estimates. Suppose you estimate an intercept and a slope from a noisy sample. Each coefficient has a variance, and the two coefficients can be correlated. To predict a mean response at input x, combine the intercept with x times the slope. The variance of that predicted mean is a quadratic form in the coefficient covariance matrix. Ignoring the off-diagonal term can produce a wrong uncertainty estimate, especially far from the center of the original inputs.

Covariance matrices have limitations. Two data-generating processes can share exactly the same means and covariances yet have very different tails, nonlinear patterns, or outlier probabilities. A covariance matrix summarizes second moments, not an entire probability distribution. If the distribution is multivariate Gaussian, mean and covariance do determine it, provided the covariance matrix is valid; in the non-Gaussian case they generally do not. Also, if a variable has infinite variance, the ordinary covariance matrix may not exist as a finite object. The formulas require the relevant second moments.

There is a subtle issue at perfect correlation. If one sensor always equals twice the other, their covariance matrix has a zero eigenvalue. It is positive semidefinite, but not positive definite. A zero-variance linear combination exists: two times the first reading minus the second is identically zero after centering. Such a matrix is singular. An inverse-covariance calculation that assumes all directions have nonzero variance cannot be applied without modification. This will matter in multivariate modeling and in numerical linear algebra, where poorly conditioned covariance matrices can amplify estimation error.

One can also estimate covariance badly. With more variables than independent observations, the ordinary centered sample covariance is necessarily singular: the centered data matrix has rank at most the sample size minus one. This is not a bug that a numerical solver can repair by improving floating-point precision. It is a lack of information in the observations. Shrinkage or structural assumptions may produce a useful estimator, but they introduce modeling choices and should be acknowledged.

The essential bridge is now visible. Probability gives us variance as a statement about fluctuations. Linear algebra organizes those fluctuations in a symmetric positive-semidefinite operator. Its eigenvectors are directions in which uncertainty can be compared, and its quadratic forms tell us the uncertainty of any specified measurement. This is the foundation for principal component analysis, multivariate regression, correlated-noise models, and many spectral methods.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For a random vector \(X\in\mathbb R^p\) with finite second moments and mean \(\mu\),
\[
\Sigma=\operatorname{E}[(X-\mu)(X-\mu)^\top],\qquad a^\top\Sigma a=\operatorname{Var}(a^\top X)\ge0.
\]
For centered rows \((-2,-1),(-1,-2),(1,2),(2,1)\),
\[
\Sigma_{\mathrm{divisor}\,4}=\begin{pmatrix} 5/2&2\\2&5/2\end{pmatrix},\quad
v_+=(1,1)/\sqrt2,\quad v_-=(1,-1)/\sqrt2,\quad
\lambda_+=9/2,\quad\lambda_-=1/2.
\]
The unbiased conventional sample covariance divides sums by \(n-1=3\), giving eigenvalues \(6\) and \(2/3\). Both conventions yield a variance proportion of \(9/10\) in the leading direction.

**Sample rank.** With \(n\) centered observations of \(p\) variables, the centered matrix \(Z\) has rank at most \(\min(p,n-1)\). Since \(\widehat\Sigma=Z^\top Z/(n-1)\), the sample covariance has the same rank bound. It is singular whenever \(p>n-1\).

### Exercises and answers

1. **Zero covariance.** Can two dependent variables have covariance zero? **Answer:** Yes. If X is symmetric about zero and Y equals X squared with finite required moments, \(\operatorname{Cov}(X,Y)=\operatorname{E}[X^3]-\operatorname{E}[X]\operatorname{E}[X^2]=0\), despite deterministic dependence.
2. **Variance along a direction.** For the worked matrix, what is the variance along \((1,-1)/\sqrt2\)? **Answer:** One half under divisor four.
3. **Singularity.** What does a zero covariance eigenvalue mean? **Answer:** Some nonzero linear combination of centered measurements has variance zero, hence is zero almost surely.
4. **Units.** Why might one prefer a correlation matrix? **Answer:** Its entries do not depend on units; but it changes the weighting of variables.

### Reading and attribution

- Penn State STAT 501, multiple regression and covariance concepts: https://online.stat.psu.edu/stat501/.
- Penn State STAT 505, principal components and multivariate methods: https://online.stat.psu.edu/stat505/.
- The four-pair dataset, eigenvalue calculation, and explanations are original worked exposition.
