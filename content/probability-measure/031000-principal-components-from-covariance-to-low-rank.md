# Principal Components: From Covariance to Low-Rank Approximation

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 031000  
**Preparation:** Covariance matrices, unit vectors, eigenvalues, and linear projections.  
**Companion:** Two-dimensional PCA, variational proof, and SVD connection.

<!-- BEGIN SPOKEN LECTURE -->

You measure a complicated object with ten different sensors. Many readings move together, perhaps because a small number of underlying mechanisms drive them. You want to replace the ten readings with two or three numbers without throwing away too much of what the instruments recorded. How could you choose the new numbers, and what exactly would it mean to keep most of the information?

Principal component analysis, or PCA, offers a particular mathematical answer. It finds orthogonal directions through centered numerical data that capture as much squared variation as possible. This is not automatically the same as preserving the information relevant to a prediction task, nor does it guarantee recovering the physical mechanisms that generated the measurements. Its strength is the precision of the optimization problem it actually solves.

Start with two centered sensor measurements. Four observed pairs are negative two and negative one; negative one and negative two; one and two; and two and one. We already know their divisor-four covariance matrix has two point five on the diagonal and two off the diagonal. Their main variation lies near the line where both coordinates increase together. Their smaller variation is in the perpendicular direction where one coordinate increases while the other decreases.

Suppose we must summarize each two-coordinate reading by one number. Choose a unit vector u and take the dot product of each centered reading with u. That dot product is the coordinate along the direction u. If we want to preserve large differences among observations, we can choose the direction maximizing the average square of those projected coordinates. Algebraically, this objective is u transpose times the covariance matrix times u, subject to u having length one.

The length constraint matters. Without it, we could multiply a direction by a million and increase its projected variance by a trillion, without discovering anything about the data. We are choosing an orientation, not a scale. For a symmetric covariance matrix, the Rayleigh-quotient theorem tells us the maximum over unit vectors equals the largest eigenvalue, attained by a corresponding eigenvector. Thus the first principal component points along a largest-variance eigenvector.

In our example, that eigenvector points equally in both coordinate directions. Its variance is four point five. The perpendicular direction has variance point five. Their sum is five, the total variance of the original coordinates. So using only the first principal component captures ninety percent of the original total coordinate variance, according to this quadratic criterion. The remaining ten percent lies in the discarded perpendicular direction. This is an exact statement about the four observed pairs and the chosen scaling convention, not a claim about future data.

How do we reconstruct an approximate original observation from its single principal component? Project the centered two-dimensional vector onto the chosen unit direction and keep the resulting point on that line. Then add back the original mean, zero in this example. Each observation moves to the nearest point on that line in Euclidean distance. The squared reconstruction error is the squared length of the component perpendicular to the line. Averaging that error over the data gives point five, exactly the discarded covariance eigenvalue.

This exposes a second characterization of PCA. The direction that maximizes retained variance also minimizes squared reconstruction error among one-dimensional linear subspaces through the centered mean. The two objectives agree because a vector's squared length is the sum of squared lengths of its orthogonal projection and orthogonal residual. Total squared length is fixed, so maximizing what we keep is the same as minimizing what we lose. This is the Pythagorean theorem, applied to a dataset.

In higher dimensions, choose several mutually perpendicular directions, ordered by decreasing eigenvalue. The first maximizes variance. The second maximizes variance among directions perpendicular to the first. Continue. Keeping the first k principal components produces the best rank-k orthogonal reconstruction of the centered data under squared Euclidean error. The remaining error equals the sum of the discarded covariance eigenvalues, multiplied by the chosen covariance divisor when converted back to a sum over observations.

Computationally, it is often better not to calculate a covariance matrix and then find its eigenvectors. Put the centered observations in a rectangular data matrix Z, with observations as rows and measured variables as columns. A singular-value decomposition writes Z as left singular vectors, diagonal singular values, and right singular vectors. The right singular vectors are principal directions. Squared singular values divided by the covariance divisor are the covariance eigenvalues. Working from the data matrix directly can have better numerical properties, especially when columns are nearly dependent.

There is an essential preprocessing choice. A covariance-based PCA gives more influence to variables with larger numerical variance. If one feature is measured in meters and another in millimeters, changing units changes the covariance matrix and potentially its principal components. Standardizing every feature to variance one before PCA creates correlation-based PCA. That makes the result invariant to positive rescaling of individual variables, but it also discards differences in scale that may be scientifically meaningful. There is no universally correct preprocessing independent of the question being asked.

Another limitation is that large variance is not always valuable variance. Imagine a medical signal in which one channel contains huge, irrelevant environmental noise, while a smaller-amplitude channel contains the information useful for diagnosis. PCA may select the noisy direction first because it carries the most variation. In supervised prediction, keeping the leading components could remove a low-variance direction that is strongly related to the target. A principal component is not inherently a causal factor, a class label, or a useful predictor. It is a direction that solves a specified variance problem.

Principal directions are also not always unique. If the largest two eigenvalues are equal, any orthonormal basis of their shared eigenspace is equally valid. Even when eigenvalues are distinct, an eigenvector and its negative encode the same one-dimensional subspace, so the sign of a principal component is arbitrary. If eigenvalues are nearly equal, small perturbations can rotate individual estimated directions substantially. This connects PCA to spectral perturbation theory: the separation between eigenvalues or invariant subspaces influences how stable an estimated component can be.

Outliers matter as well. Covariance uses squared deviations, so a single distant observation can dominate a principal direction. If your objective is robust summary rather than squared-error reconstruction, you may want robust covariance methods or a different optimization criterion. And fitting PCA on a complete dataset before splitting into training and evaluation subsets can leak distributional information from held-out observations. Even unsupervised transformations must be learned only from the appropriate training subset when assessing a predictive pipeline.

The importance of PCA is not that it always uncovers hidden truth. It makes an exact bridge from probability to optimization and linear algebra. A covariance matrix tells us how fluctuations interact. An eigenvalue problem finds directions of maximal fluctuation. Orthogonal projection turns those directions into a lower-dimensional approximation. Singular-value decomposition computes that approximation efficiently. The entire method can be understood as one constrained mathematical question followed through several representations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For centered data \(Z\in\mathbb R^{n\times p}\) and divisor \(d=n\) or \(n-1\) as defined, \(S=Z^\top Z/d\). The first principal direction solves
\[
\max_{\|u\|_2=1}u^\top S u=\lambda_{\max}(S).
\]
By the spectral theorem, express \(u\) in the orthonormal eigenbasis: the Rayleigh quotient is a convex combination of eigenvalues, so its maximum is the largest. For orthonormal columns \(U_k\), the rank-k reconstruction is \(\widehat Z=ZU_kU_k^\top\), and
\[
\|Z-\widehat Z\|_F^2=d\sum_{j>k}\lambda_j(S).
\]
This is optimal among rank-k linear orthogonal projections; the Eckart-Young-Mirsky theorem extends the optimality claim to all rank-k matrix approximations under Frobenius norm.

For the four-point example, \(S=\begin{psmallmatrix}2.5&2\\2&2.5\end{psmallmatrix}\); eigenvalues \(4.5,0.5\). Retained variance ratio for the first component is \(4.5/5=0.9\). Mean squared reconstruction error is \(0.5\) under divisor four, and total squared reconstruction error is \(4\cdot0.5=2\).

### Exercises with answers

1. **Maximal variance.** Why constrain a principal direction to unit length? **Answer:** Without a norm constraint the quadratic variance objective can grow without bound by rescaling.
2. **Reconstruction.** What is the average squared reconstruction error using the first component of the four-point data? **Answer:** Point five, the discarded eigenvalue under divisor four.
3. **Nonuniqueness.** If the leading two eigenvalues are equal, is the first eigenvector uniquely determined? **Answer:** No; any unit vector in the top eigenspace attains the same value.
4. **Prediction.** Can PCA discard a direction highly predictive of an outcome? **Answer:** Yes, because PCA does not optimize prediction of that outcome.

### Reading and attribution

- Penn State STAT 505, multivariate methods and principal component analysis: https://online.stat.psu.edu/stat505/.
- Hastie, Tibshirani, and Friedman, *The Elements of Statistical Learning*, second edition: https://hastie.su.domains/ElemStatLearn/.
- The numerical example is an original calculation, explicitly reusing the four observations from the covariance lecture.
