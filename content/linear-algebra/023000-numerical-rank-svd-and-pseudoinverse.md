# When Rank Is Not a Yes-or-No Measurement: Singular Values and the Pseudoinverse

**Track:** Linear Algebra from First Principles. **Background:** orthogonal projections, eigenvalues of symmetric matrices, least squares, Euclidean norms. **Purpose:** move from the algebraic rank in elimination to rank-aware computation, minimum-norm solutions, and explicit regularization tradeoffs.

<!-- BEGIN SPOKEN LECTURE -->

# When Rank Is Not a Yes-or-No Measurement

An exact matrix has an exact rank. Either a collection of columns is linearly independent, or it is not. In an experiment, however, the matrix may be built from sensor readings or estimated coefficients. We know its entries only approximately. Then a very small singular value raises a harder question: is the matrix truly carrying a weak but meaningful direction, or has noise produced an apparent direction that should not be trusted?

Rank alone cannot answer that. We need to know how strongly the matrix acts on directions in its input space. Singular-value decomposition makes those directions and their strengths explicit. It also gives a precise way to solve inconsistent or underdetermined systems, while forcing us to state what we do with information that is too weak to recover reliably.

## Stretching a sphere into an ellipsoid

Think of a matrix as a map from input vectors to output vectors. Take every unit vector in the input space and apply A. If A is a square, invertible real matrix, the unit sphere becomes an ellipsoid, perhaps rotated or reflected. Its principal semiaxis lengths are the singular values. For a rectangular matrix, the image lies in a subspace, but the same principal-stretch picture applies.

The singular-value decomposition writes A as U times Sigma times V transpose. V changes to a set of perpendicular input directions. Sigma stretches each of those directions by a nonnegative amount, or sends it to zero. U rotates or reflects the resulting output directions. For complex matrices, transpose is replaced by conjugate transpose.

This representation differs from an eigenvector decomposition. The input and output directions can be different, and A need not be square or diagonalizable. Every real or complex matrix has a singular-value decomposition. The nonnegative singular values are the square roots of the eigenvalues of A transpose times A, but that identity is primarily structural: forming that product explicitly can make numerical conditioning worse.

The number of strictly positive singular values is the exact rank. When A is invertible and square, the ratio of its largest to smallest singular value is its condition number in the Euclidean norm. For a rectangular full-column-rank problem, the same ratio measures how sensitive the recovery of parameters can be along the column space.

## A rank-one system with many possible parameters

Consider the two-by-two matrix whose every entry is one. Both its rows are identical, and both its columns are identical, so it has rank one. Its one nonzero singular value is two. The other singular value is zero. The right input direction that survives is the diagonal direction one, one, normalized to unit length. The perpendicular direction one, negative one is completely invisible to the matrix.

Now suppose b is the vector two, zero. No exact solution exists. The matrix can predict only vectors whose two entries are equal. The closest prediction to two, zero is one, one, its orthogonal projection onto that line. Any parameter vector whose two entries add to one produces that prediction. There are infinitely many least-squares solutions.

Which parameter vector should we return? One natural additional criterion is to choose the least-squares solution of smallest Euclidean norm. Among all pairs whose entries add to one, the minimum-length pair is one-half, one-half. The difference between it and any other solution lies in the nullspace, perpendicular to the chosen minimum-norm solution. Adding a nullspace component only increases its squared length.

The Moore–Penrose pseudoinverse encodes this convention. In the singular-value decomposition, it inverts each nonzero singular value, leaves the zero singular values at zero, and reverses the input and output orthogonal transformations. Applied to b, it gives the minimum-norm least-squares solution. For our all-ones matrix, the pseudoinverse is one-quarter times the all-ones matrix, and it returns one-half, one-half.

The name can make this sound like a general-purpose replacement for a matrix inverse. It is not an answer to the question of whether the problem's data deserve to be trusted. The exact pseudoinverse of a nearly singular matrix can still amplify noise enormously. It is a clearly defined mathematical map, not an automatic regularizer.

## Small does not mean zero

Consider a diagonal two-by-two matrix with diagonal entries one and epsilon, where epsilon is positive but small. Its exact rank is two. The second input direction is transformed into an output just epsilon times as large. Recovering that component requires dividing by epsilon.

Suppose the true parameter vector is one, one. Its exact data vector is one, epsilon. Now perturb the second observation by delta. Exact inversion returns one, one plus delta divided by epsilon. When epsilon is tiny, observational noise that looks negligible in the raw output can completely dominate the recovered second parameter.

A numerical-rank rule might decide that singular values smaller than a chosen tolerance should be treated as zero. With a threshold above epsilon, the resulting truncated pseudoinverse returns one, zero, ignoring the second observation. This answer is insensitive to noise along that direction. But if the true second parameter really is one, the method introduces a bias of one in that coordinate even with perfect data.

This is a consequential choice. If our scientific task genuinely needs the tiny component and our observations are sufficiently precise, discarding it destroys information. If the observations are too noisy to support it, retaining it produces a volatile answer. No purely algebraic rule can settle the decision without an accuracy requirement or data-error model.

## What error bounds say about rank

There is a useful bridge from exact algebra to finite-precision decisions. If a matrix A is perturbed by E, every singular value changes by at most the Euclidean operator norm of E. In other words, singular values are stable as measurements of matrix stretching, even when singular vectors may rotate dramatically near repeated values.

Suppose the uncertainty in A has norm at most one thousandth. A singular value equal to one hundredth cannot be driven to zero by a perturbation inside that bound. A singular value equal to one ten-thousandth could be. This does not prove that the latter is noise; it tells us that the available accuracy does not robustly distinguish it from rank deficiency.

The singular-value gap also matters. If a few singular values are large and the remaining ones are small relative to the error bound, a low-rank approximation may capture the robustly observable part of the map. If there is no gap, choosing a sharp rank threshold may produce a discontinuous estimate: tiny changes in measurements can change which components are retained.

A common method is to keep the first k singular directions and set the rest to zero. Among all matrices of rank at most k, this truncated decomposition gives the smallest error in either the Euclidean operator norm or the Frobenius norm. The corresponding errors are the next omitted singular value and, respectively, the square root of the sum of squares of all the omitted singular values.

For a diagonal matrix with entries four, one, and epsilon, discarding the last direction leaves a rank-two matrix and changes the map by epsilon in operator norm. But it also makes every input component along that discarded direction invisible. A small approximation error in the map does not guarantee a small error in recovering every possible input.

## Regularization changes the inversion problem smoothly

Hard truncation is not the only response to weak singular directions. Another method adds a penalty for large parameter vectors. Instead of minimizing only the squared length of A times x minus b, minimize that squared residual plus lambda times the squared length of x, where lambda is positive. This is a form of Tikhonov regularization, also called ridge regularization in many statistical settings.

In singular-vector coordinates, each data component is multiplied by the singular value divided by the sum of its square and lambda. Compare this with exact inversion, which multiplies by one divided by the singular value. For large singular values relative to the penalty scale, the filter behaves approximately like inversion. For tiny singular values, the gain tends toward zero rather than exploding.

For the diagonal matrix with entries one and epsilon, the regularized solution has first component b one divided by one plus lambda, and second component epsilon times b two divided by epsilon squared plus lambda. It is stable against extreme amplification of data noise as long as lambda remains positive, but it is biased toward smaller parameter vectors. Changing lambda changes the scientific question being answered.

Other penalties encode other assumptions: smoothness of a signal, sparsity of coefficients, closeness to a prior model, or constraints from physics. The Euclidean penalty is merely one choice. There is no numerical algorithm that can infer those domain assumptions from a matrix alone.

## How singular values are actually computed

Because the squares of singular values are eigenvalues of A transpose times A, it is tempting to compute that product and use an ordinary symmetric eigenvalue routine. The identity is true. As a general dense numerical algorithm, however, explicitly forming A transpose times A can square the condition number and compromise the smallest singular values.

Reliable SVD implementations use transformations designed to preserve norms, such as Householder reductions to bidiagonal form, followed by algorithms that compute the singular values and vectors without simply treating the normal equations as a harmless shortcut. Details depend on matrix shape, precision, and desired outputs. A large sparse operator may use iterative methods to estimate selected singular directions instead of calculating them all.

There is a similar distinction when we report numerical rank. A software routine's threshold may depend on matrix dimension, largest singular value, and arithmetic precision. That is a useful computational convention, but it is not necessarily the uncertainty in the measurements. If the data have their own error scale, the scientifically meaningful rank decision should reflect that scale.

## What the pseudoinverse establishes, and what it does not

A pseudoinverse produces a precise canonical answer: the minimum-norm vector among those that minimize the residual. Singular values describe which directions the data constrain strongly, weakly, or not at all. Truncation and regularization introduce controlled preferences when weak directions are not recoverable.

These are not merely alternative matrix formulas. They mark three different kinds of claim. Exact rank is an algebraic fact about a specified matrix. Numerical rank is a decision about distinguishability at a chosen error level. A regularized estimate is an answer to a modified inference problem. Keeping those distinctions clear is what allows basic linear algebra to support serious inverse problems, scientific computing, and statistical modeling.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### SVD, pseudoinverse, and minimum norm

For \(A\in\mathbb R^{m\times n}\) let \(A=U\Sigma V^T\), where \(U,V\) are orthogonal and the nonzero diagonal entries of \(\Sigma\) are \(\sigma_1\ge\cdots\ge\sigma_r>0\). Define \(\Sigma^+\) by inverting the positive \(\sigma_i\) and transposing the rectangular shape; set \(A^+=V\Sigma^+U^T\). Then \(A^+b\) is the unique minimum-Euclidean-norm member of the set of least-squares minimizers. Proof: in singular coordinates, the nonzero modes have uniquely determined best coefficients \(u_i^Tb/\sigma_i\), while nullspace coefficients do not affect the residual and strictly increase squared norm unless zero.

For \(J=\begin{bmatrix}1&1\\1&1\end{bmatrix}\), the singular values are \(2,0\), and
\[
 J^+=\frac14\begin{bmatrix}1&1\\1&1\end{bmatrix},\quad
 b=(2,0)^T,\quad x^+=J^+b=(1/2,1/2)^T,\quad
 Jx^+=(1,1)^T.
\]
The residual \(b-Jx^+=(1,-1)^T\) is perpendicular to \(\operatorname{col}J\). Every least-squares minimizer has the form \((t,1-t)^T\).

### Weak singular direction, noise and bias

Let \(A=\operatorname{diag}(1,\epsilon)\) for \(0<\epsilon<1\), \(x_*=(1,1)^T\), and noisy data \(b=(1,\epsilon+\delta)^T\). Then
\[
 x_{\rm exact\ inverse}=(1,1+\delta/\epsilon)^T.
\]
If a threshold \(\tau\) obeys \(\epsilon<\tau<1\), the truncated-SVD estimate is \(x_{\rm TSVD}=(1,0)^T\). The first amplifies \(\delta\) by \(1/\epsilon\); the second has a bias of \(-1\) in the second coordinate for this chosen true x.

For \(\lambda>0\), Tikhonov regularization solves
\[
 \min_x \|Ax-b\|_2^2+\lambda\|x\|_2^2,
 \qquad x_\lambda=(A^TA+\lambda I)^{-1}A^Tb.
\]
In SVD coordinates the gain in the i-th singular direction is \(g_i=\sigma_i/(\sigma_i^2+\lambda)\). For the diagonal example:
\[
 x_\lambda=\left(\frac{1}{1+\lambda},\frac{\epsilon(\epsilon+\delta)}{\epsilon^2+\lambda}\right)^T.
\]

### Perturbation and best low-rank approximation

For any \(E\) of the same shape, the singular values in descending order satisfy \(|\sigma_i(A+E)-\sigma_i(A)|\le\|E\|_2\) (singular-value perturbation bound). Consequently \(\sigma_r(A)>\|E\|_2\) guarantees that the first r singular values remain positive, although the remaining singular values of A+E may also be nonzero.

Truncated SVD \(A_k=\sum_{i=1}^k \sigma_i u_i v_i^T\) minimizes the error among rank-\(k\)-or-less matrices:
\[
\min_{\operatorname{rank}B\le k}\|A-B\|_2=\sigma_{k+1},\qquad
\min_{\operatorname{rank}B\le k}\|A-B\|_F=\sqrt{\sum_{i>k}\sigma_i^2}.
\]
These identities are the Eckart–Young–Mirsky theorem. Neither one asserts accuracy of the inverse map on discarded directions.

### Exercises with answers

1. **All-ones matrix:** Solve \(Jx=(2,0)^T\) exactly, if possible, or find the minimum-norm least-squares solution. **Answer:** no exact solution; \(x=(1/2,1/2)^T\).
2. **Noise amplification:** If \(\epsilon=10^{-4}\) and \(\delta=10^{-3}\), what is the second component of the exact inverse estimate? **Answer:** \(1+\delta/\epsilon=11\).
3. **Noiseless truncation:** With the same \(\epsilon\) but \(\delta=0\), does discarding the small singular value recover x exactly? **Answer:** no; the second component becomes zero although the true component is one.
4. **Rank uncertainty:** If \(\sigma_2(A)=10^{-2}\) and \(\|E\|_2\le10^{-3}\), can the perturbed matrix lose its second nonzero singular value? **Answer:** not that one; it remains at least \(9\times10^{-3}\).
5. **Regularization:** In which limit does \(\sigma/(\sigma^2+\lambda)\) approach inverse gain \(1/\sigma\)? **Answer:** \(\lambda\to0^+\) for each fixed \(\sigma>0\); the limit is not uniform as \(\sigma\to0\).

### Further reading and source connections

- Sheldon Axler, *Linear Algebra Done Right*, fourth edition, https://linear.axler.net/ , for singular values, adjoints, orthogonal decompositions and finite-dimensional operators.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, SIAM, 1997, https://people.maths.ox.ac.uk/trefethen/text.html , for numerical rank, SVD and conditioning.
- James W. Demmel, *Applied Numerical Linear Algebra*, SIAM, 1997, for rank-revealing factorizations, least squares and sensitivity.
- Wikipedia topic pointers: [Singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition), [Moore–Penrose inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse), [Tikhonov regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization).

See `linear-algebra:006000` for an initial geometric introduction to singular values and `numerical-analysis:006000` for the numerical-analysis overview. This deep dive focuses on rank selection, minimum-norm recovery, and what regularization assumes.
