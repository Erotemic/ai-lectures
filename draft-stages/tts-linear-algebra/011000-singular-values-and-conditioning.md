# 011000 — Singular Values: Stretching, Rank, and Conditioning

**Track:** Linear Algebra from First Principles. **Background:** adjoints, positive operators and orthonormal bases. **Question:** can we describe the size distortion of any matrix, even a rectangular one?

<!-- BEGIN SPOKEN LECTURE -->

# Singular Values: Stretching, Rank, and Conditioning

Eigenvectors of a square operator can fail to form a basis, and a rectangular matrix may have no ordinary eigenvalue problem at all. Yet every real or complex matrix admits a particularly useful geometric description: rotate the input coordinates, stretch or collapse along perpendicular directions, and rotate the output. The stretch factors are the singular values.

## From circles to ellipses

Imagine the unit circle. A linear transformation usually sends it to an ellipse, possibly flattened into a line segment or point. The ellipse's principal semiaxis lengths are the singular values of the transformation. They describe how much the matrix stretches special perpendicular input directions. This picture generalizes to higher dimensions, including transformations between spaces of different dimensions.

To find the directions, measure the squared output length of an input v. It is the inner product of A v with A v. Move A across the pairing using its adjoint. The result is the inner product of A star A applied to v with v. The operator A star A is self-adjoint and positive semidefinite. The spectral theorem supplies an orthonormal basis of input eigenvectors with nonnegative eigenvalues. The singular values are the square roots of those eigenvalues.

If A star A sends v to sigma squared times v, then A sends that input direction to an output with length sigma times the input length. For two orthogonal input eigenvectors with nonzero singular values, their outputs are orthogonal too. After normalization, those output directions form part of an orthonormal output basis.

## A rank-one example

Take the matrix that sends the input pair x, y to the output pair x plus y, zero. It reports the sum of two coordinates and discards their difference. The vector one, one, normalized by the square root of two, is stretched by a factor of the square root of two and sent horizontally. The perpendicular vector one, minus one, similarly normalized, is completely erased.

Thus the singular values are square root of two and zero. The rank is one because exactly one singular value is positive. The kernel is the one-dimensional direction along which the input is annihilated. This interpretation works for arbitrary matrices: the number of positive singular values equals rank, and the zero-singular-value directions form the kernel.

The singular value decomposition writes A as U times Sigma times V star, where U and V are unitary or orthogonal changes of coordinates and Sigma is a rectangular diagonal array of nonnegative singular values. Unlike diagonalization, it exists for every finite matrix. Singular values do not require a square map or real eigenvalues.

## The operator norm and the weakest direction

The largest singular value is the largest possible output length of a unit input. It is therefore the operator norm induced by Euclidean length. The smallest singular value, when the matrix has full column rank, measures the least stretch of a unit input. If that smallest value is tiny, some input directions hardly change the observations. Recovering the input from slightly perturbed outputs becomes sensitive to noise.

For an invertible square matrix, the ratio of the largest to the smallest singular value is its Euclidean condition number. A ratio near one means similar stretch in all directions. A large ratio indicates strong anisotropy and an ill-conditioned inversion problem. The exact problem can have a perfectly well-defined answer and still be numerically sensitive.

Consider the diagonal matrix with entries one and one millionth. Its inverse exists and has a million on the second diagonal. An observation error of one millionth in the second output coordinate can produce an error of order one in the reconstructed input. No algorithm can reconstruct that input accurately from noisy data without additional information; the instability belongs to the problem, not just the implementation.

## Pseudoinverses and meaningful approximations

A matrix may be rectangular or rank deficient. Singular value decomposition still identifies its supported input and output directions. To compute a least-squares solution of minimum input length, divide by each positive singular value and set the component along each null direction to zero. This constructs the Moore–Penrose pseudoinverse.

That construction explains why the pseudoinverse does not make lost information reappear. If a singular value is zero, no measurement can distinguish movement along its corresponding input direction. Setting that component to zero chooses one particular answer, the minimum-norm one. It does not recover a uniquely determined physical truth.

In practice, dividing by an extremely small positive singular value can amplify noise catastrophically. Truncated singular value decomposition or regularization may deliberately avoid such divisions. Then the result is biased but more stable. The appropriate choice depends on the reliability of data and the scientific question.

## Polar decomposition

There is another useful way to separate geometric actions. Define the positive operator absolute value of A as the positive square root of A star A. Then A can be written as a partial isometry multiplied by this positive stretch operator. Reading the composition from right to left, the stretch occurs first. In the square invertible case, A equals U times the absolute value of A, with U unitary. This is polar decomposition: first stretch along principal directions, then rotate or reflect.

If A has a kernel, the isometric factor need not be unitary on the entire domain; it acts as an isometry on the perpendicular complement of the kernel. That qualification becomes important in infinite-dimensional operator theory, where ranges, closures, and partial isometries require more care.

Singular values are the metric anatomy of a linear map. Eigenvalues explain invariant directions when those exist. Singular values answer a different, always available question: how much can the map stretch, compress, or erase? This is the language connecting least squares, numerical reliability, data compression, inverse problems, and functional analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A\in\mathbb C^{m\times n}\), \(A^*A\) is Hermitian positive semidefinite, so its eigenvalues are \(\sigma_i^2\ge0\). An SVD is \(A=U\Sigma V^*\) with \(U\in U(m),V\in U(n)\), \(\Sigma\) rectangular diagonal. \(\|A\|_2=\sigma_{\max}\); \(\operatorname{rank} A\) equals the number of strictly positive singular values. For invertible square \(A\), \(\kappa_2(A)=\sigma_{\max}/\sigma_{\min}\). For \(A=\begin{psmallmatrix}1&1\\0&0\end{psmallmatrix}\), \(A^*A=\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\), with eigenvalues two and zero, so singular values \(\sqrt2,0\). Define \(|A|=(A^*A)^{1/2}\); the polar factor satisfies \(A=U|A|\), with partial-isometry \(U\) on the support of \(|A|\).

### Exercises with answers

1. Find singular values of \(\operatorname{diag}(3,1)\). **Answer:** three and one.
2. Is zero always a singular value of a rank-deficient square matrix? **Answer:** yes.
3. What does a condition number of one imply for an invertible square matrix? **Answer:** all singular values coincide, so the map is a uniform scale followed by a unitary/orthogonal map.
4. Does a pseudoinverse recover information in the kernel? **Answer:** no; it selects the minimum-norm solution.

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), singular value decomposition and positive operators.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), SVD and pseudoinverse.
- [Singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition).
