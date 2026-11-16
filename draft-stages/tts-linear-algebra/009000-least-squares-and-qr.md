# 009000 — Least Squares: Fitting Data without Solving an Impossible System

**Track:** Linear Algebra from First Principles. **Background:** matrices, orthogonal projections and inner products. **Question:** what is the best approximate answer when equations conflict?

<!-- BEGIN SPOKEN LECTURE -->

# Least Squares: Fitting Data without Solving an Impossible System

A measurement instrument may be noisy. Ask it three times for the same physical quantity and receive three slightly different answers. If we demand that one unknown equal all three observations exactly, the equations are inconsistent. Yet we still want the best estimate. Least squares replaces an impossible exact system with a precise optimization question, and linear algebra solves it by perpendicularity.

## An overdetermined line fit

Suppose we record three points: at time zero the value is one, at time one it is two, and at time two it is two again. We seek a line with intercept a and slope b, so the prediction at time t is a plus b times t. Fitting exactly would require a equals one, a plus b equals two, and a plus twice b equals two. From the first two equations b equals one, but then the third predicts three, not two. No line passes through all three points.

The residual is the observed value minus the prediction. A least-squares fit chooses a and b to minimize the sum of the squares of the three residuals. Squaring treats positive and negative errors equally and makes the objective a smooth quadratic. Squaring is not always the best statistical model, but it gives a clean mathematical problem and has a strong interpretation when measurement errors are independent Gaussian observations with equal variance.

Put the three observations in a vector y and the model predictions in a vector A times c, where c contains a and b. The first column of A is all ones, representing the intercept. The second contains the time values zero, one, two, representing the slope. The possible predicted vectors form the column space of A, a plane inside the three-dimensional space of possible observations. Our problem is to project y onto that plane.

## Derive the normal equations

At the closest prediction, the residual must be perpendicular to the entire column space of A. In particular, its dot product with each column must vanish. Combining those two conditions gives the normal equations: A transpose times A times c equals A transpose times y.

For the three data points, A transpose times A has rows three, three and three, five. A transpose times y is five, six. So three a plus three b equals five, and three a plus five b equals six. Subtracting gives two b equals one, or b equals one half. Then a equals seven sixths.

The fitted predictions are seven sixths, five thirds, and thirteen sixths. Their differences from the observations are small, and the residual vector, observation minus prediction, is minus one sixth, one third, minus one sixth. Check the orthogonality conditions directly. Its entries sum to zero, so it is perpendicular to the constant column. Multiply the residuals by zero, one and two, and the weighted sum is also zero, so it is perpendicular to the time column. That is the geometry behind the solution.

## Why the solution is best

Could another line fit better? Suppose c star solves the normal equations and c is any alternative. Write the residual for c as the residual for c star minus A times the difference of coefficients. The first residual is perpendicular to every vector of the form A times something. By Pythagoras, the squared error for c is the optimal squared error plus the squared length of A times the coefficient difference. This cannot be smaller.

If the columns of A are independent, then A times the difference vanishes only when the coefficients are equal. In that case the best coefficients are unique. If the columns are dependent, the best predicted vector is still unique, but different coefficient lists may produce it. That distinction between a unique output and nonunique parameters is crucial in statistical modeling.

## Why not always solve the normal equations numerically?

The normal equations are exact mathematics. But forming A transpose times A can worsen numerical conditioning. If the singular values of A range from a large value to a very small one, those of A transpose times A are their squares. The disparity becomes larger, making roundoff errors harder to control.

A QR factorization avoids this squaring. It writes A as an orthonormal-column factor Q times an upper triangular factor R, assuming full column rank. The residual-orthogonality condition becomes R times c equals Q transpose times y, which is solved by back substitution. In more delicate problems, a singular value decomposition helps identify directions the data hardly constrain.

Thus the shortest symbolic formula is not always the most trustworthy numerical algorithm. One should understand both the mathematical minimizer and the floating-point method used to compute it.

## Where the same geometry appears

Least squares underlies polynomial fitting, numerical calibration, linear regression, and parameter estimation. In Fourier analysis, approximating a function by finitely many orthogonal basis functions is also an orthogonal projection: the coefficients are inner products, and the residual is perpendicular to the selected subspace.

If we assign different reliability weights to measurements, the metric changes and so does the projection. If we penalize large coefficients to discourage an unstable fit, we obtain regularized least squares. Those modifications follow naturally once we understand the original problem as projection onto the image of a linear map.

Least squares is not a compromise in rigor because the equations had no exact solution. It asks a different, exactly solvable question: which attainable prediction is closest to the data, under a chosen measure of error? Linear algebra gives both a construction and a proof of optimality.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A\in\mathbb R^{m\times n}\) and \(y\in\mathbb R^m\), minimize \(F(c)=\|Ac-y\|_2^2\). The stationarity condition is \(A^T(Ac-y)=0\). When \(A\) has full column rank, \(A^TA\) is positive definite and the minimizer is unique. For
\[
A=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\quad y=\begin{pmatrix}1\\2\\2\end{pmatrix},\quad
A^TA=\begin{pmatrix}3&3\\3&5\end{pmatrix},\quad A^Ty=\begin{pmatrix}5\\6\end{pmatrix},
\]
one obtains \(c=(7/6,1/2)\) and residual \(r=y-Ac=(-1/6,1/3,-1/6)\), satisfying \(A^Tr=0\). For full-column-rank \(A=QR\) with \(Q^TQ=I\), solve \(Rc=Q^Ty\).

### Exercises with answers

1. Can a line pass through \((0,1),(1,2),(2,2)\)? **Answer:** no; the slopes between consecutive pairs differ.
2. Compute the residual sum for the least-squares solution above. **Answer:** zero.
3. Why can dependent columns produce nonunique coefficients? **Answer:** a nonzero vector in \(\ker A\) can be added without changing the prediction.
4. Why might QR be numerically preferable to normal equations? **Answer:** it avoids squaring the condition number via \(A^TA\).

### Sources and further reading

- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), projections and least squares.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), orthogonal projection and fitting.
- [Linear least squares](https://en.wikipedia.org/wiki/Linear_least_squares).
