# Volume, spectral directions, and best approximation

<!-- BEGIN SPOKEN LECTURE -->

# Volume, spectral directions, and best approximation

## Determinants: Area, Volume, and Orientation

Draw a little square on a rubber sheet. Apply a linear transformation: perhaps the square tilts into a parallelogram, stretches, or collapses to a line. The determinant measures the signed factor by which its area changes. In higher dimensions, it measures the corresponding signed volume factor. This geometric idea explains the algebraic rules and also why a determinant of zero means noninvertibility.

### Start with two directions

Take two vectors in the plane. Their parallelogram area, with a sign recording orientation, can be computed from their four coordinates. If the first vector is a, c and the second is b, d, the signed area is a times d minus b times c. Write the vectors as columns of a two-by-two matrix. That expression is its determinant.

For example, take the vectors two, zero and one, three. The parallelogram has base two and height three, so area six; the determinant also gives six. Reverse the order of the columns and the oriented area becomes minus six. The geometric region did not acquire negative physical area; the sign records that we reversed the ordered directions.

If the vectors are collinear, their parallelogram is flat and has zero area. The determinant vanishes. Conversely, a zero determinant in two dimensions means one column is a multiple of the other, so there is no two-dimensional area left. We have lost an independent direction.

### Why the determinant multiplies

Suppose one linear map multiplies area by a signed factor of three. Then another map multiplies area by a signed factor of minus two. Applying both changes signed area by minus six. This gives the determinant of a composite as the product of the two determinants. In matrix language, determinant of A times B equals determinant of A times determinant of B.

This rule applies in all finite dimensions. It immediately implies that the identity has determinant one, and if A is invertible, the determinant of its inverse is one over the determinant of A. A zero determinant cannot belong to an invertible map. Indeed, any invertible map must preserve n-dimensional volume up to a nonzero scale, because its inverse would otherwise have to restore volume from a collapsed object.

Swapping two columns reverses orientation and changes the determinant's sign. Multiplying a column by a factor multiplies the determinant by that factor. Adding a multiple of one column to a different column does not change volume, because it shears the parallelepiped without changing its altitude. These properties also hold for rows and explain how to compute determinants using elimination.

### Calculating without memorizing enormous formulas

For a triangular matrix, its determinant is the product of its diagonal entries. Eliminate entries below the pivots using row additions, which do not change the determinant. Keep track of row swaps, which flip the sign, and rescalings, which change the magnitude. The final triangular matrix reveals the result as a product of pivots.

As a test, take a matrix with rows two, one and one, three. Its determinant is six minus one, or five. Elimination replaces the second row by itself minus one half of the first, leaving the lower diagonal entry at two and a half. Multiply it by the upper pivot two and you get five again.

For a larger matrix, computing the determinant is usually a consequence of a reliable factorization, not a reason to expand a huge alternating sum. The conceptual definition, however, uses the fact that there is essentially one alternating, multilinear way to assign a signed unit volume to n ordered vectors once a unit orientation is chosen.

### Determinants and linear equations

A square matrix has nonzero determinant exactly when its columns form a basis. That means the associated linear system has a unique solution for every right-hand side. A zero determinant means the columns are dependent, so some input direction is invisible and the map fails to be invertible.

This is also why a determinant appears in the inverse function theorem. A smooth map can be approximated near a point by its derivative matrix. If that derivative has nonzero determinant, its first-order behavior preserves all local directions. Under the theorem's hypotheses, the nonlinear map is locally invertible. A nonzero determinant is not a guarantee of global invertibility: two distant points may still map to the same output.

### The Jacobian in a change of variables

Now think of integrating a function over a region. If we introduce new coordinates related by a linear map, every small box has its volume scaled by the absolute value of the determinant. That is why the determinant's magnitude enters multivariable integration. We use the absolute value for ordinary unsigned volume; the sign is retained when orientation matters, such as in integrals of differential forms.

Take polar coordinates away from the origin. The map from radius and angle to Cartesian coordinates is nonlinear, but its derivative at each point has determinant equal to the radius. A tiny rectangle in radius-angle space corresponds to an area approximately radius times its coordinate area. Hence the familiar extra factor of radius in a polar integral. The derivative determinant is the local volume correction, not an algebraic decoration.

One limitation deserves emphasis. Determinants belong to square linear maps and to top exterior powers of maps between equally dimensional spaces. For a rectangular matrix, notions of volume distortion use singular values or Gram determinants instead. Never attach a determinant to an arbitrary rectangular matrix as though the usual formula applied unchanged.

The determinant compresses three stories into one number: whether the transformation loses a dimension, how much volume it scales, and whether it preserves or reverses orientation. Those stories reappear in differential geometry, degree theory, probability densities, and manifold integration.

## Eigenvalues and Eigenvectors: Finding Directions That Do Not Turn

Suppose a transformation stretches some vectors, rotates others, and mixes coordinates. If we apply it repeatedly, a generic vector may become difficult to track. But perhaps there are special directions that the transformation does not turn at all. They may grow, shrink, or reverse, yet remain on the same line. Those are eigenvectors, and their scaling factors are eigenvalues.

### An eigenvector is a direction, not just a number

A nonzero vector v is an eigenvector of a linear operator T if applying T gives a scalar multiple of v. The scalar is its eigenvalue. The zero vector is excluded because every scalar would satisfy the equation at zero and tell us nothing.

Take the map that doubles the x coordinate and triples the y coordinate. The horizontal direction is an eigenvector with eigenvalue two; the vertical direction is an eigenvector with eigenvalue three. Apply the map ten times: the horizontal component is multiplied by two ten times and the vertical component by three ten times. The decomposition makes long-term behavior transparent.

A vector such as one, one is not an eigenvector, because its image two, three points in a different direction. Yet one, one is the sum of the two coordinate eigenvectors. Knowing those modes tells us exactly how its image evolves.

### Finding the special directions

To find an eigenvalue of a matrix A, solve A v equals lambda times v. Rearrange this as A minus lambda times the identity, acting on v, equals zero. We seek a nonzero solution, so this new matrix must have a nontrivial kernel. In a finite-dimensional square matrix that happens precisely when its determinant is zero. The resulting polynomial equation in lambda is the characteristic equation.

Consider the matrix with first row two, one and second row zero, three. The characteristic polynomial is the product of two minus lambda and three minus lambda, because the matrix is triangular. Its eigenvalues are two and three. For eigenvalue two, the equation forces the second coordinate to be zero; the first coordinate can be anything. The vector one, zero works. For eigenvalue three, the equations force the two coordinates to be equal. The vector one, one works.

Those two eigenvectors are independent. Arrange them as the columns of a change-of-basis matrix. In their basis, our original upper-triangular matrix becomes diagonal, with entries two and three. That is diagonalization. It is not making the map simpler by approximation; it is describing the exact same map in directions adapted to its action.

### Why distinct eigenvalues help

Eigenvectors for distinct eigenvalues are linearly independent. To see the central idea, suppose one vector with eigenvalue two were a multiple of another with eigenvalue three. Applying the operator would have to multiply that same nonzero direction by both two and three, which is impossible. A slightly longer induction proves the result for any number of distinct eigenvalues.

Therefore, an n-dimensional operator with n distinct eigenvalues has an eigenbasis and is diagonalizable. But repeated eigenvalues do not guarantee enough eigenvectors. Consider a matrix with first row one, one and second row zero, one. Its only eigenvalue is one. The eigenvector equation forces the second coordinate to be zero. Only one independent eigenvector remains, so there is no basis of eigenvectors for the plane.

Repeated application of this matrix is revealing. It contains a shear. After n steps, the upper-right entry becomes n. The evolution includes polynomial growth even though every eigenvalue equals one. A theory based only on eigenvalues would miss this behavior. Generalized eigenvectors and Jordan blocks explain it; they are a later refinement, not a reason to dismiss eigenvalues.

### Real versus complex modes

Rotate the plane by ninety degrees. No nonzero real vector stays on its own line; every one is turned. So the real matrix has no real eigenvector. If we allow complex scalars, it has eigenvalues i and minus i. Complex vector spaces make many spectral statements cleaner, even when the original system is real.

A real symmetric matrix is better behaved than an arbitrary real matrix: it has real eigenvalues and an orthonormal eigenbasis. This is the spectral theorem, which will follow after we introduce inner products and adjoints. Thus diagonalization is not universal, but structure can guarantee it.

### Modes in differential equations and physical systems

Imagine a linear differential equation whose time derivative equals A times the current state. If the initial state is an eigenvector, the solution stays in that eigen-direction, multiplied by an exponential of the eigenvalue times time. A positive real eigenvalue grows, a negative one decays. Complex conjugate eigenvalues can produce oscillation. A general state decomposed into eigenmodes, when a basis exists, becomes a sum of such simpler solutions.

In vibration problems, normal modes are eigenvectors of suitable operators; the associated eigenvalues determine frequencies or frequency squares. In data analysis, eigenvectors of covariance matrices describe principal directions of variation. In quantum mechanics, eigenvectors of self-adjoint operators describe states with definite measured values. Each application adds hypotheses, but the shared core is the search for directions that do not mix.

An eigenvalue is not the same thing as a singular value. Eigenvalues describe invariant directions for a square operator and may be negative or complex. Singular values measure nonnegative stretch factors and exist for every real or complex matrix. We will build that distinction carefully rather than treating the two as synonyms.

The true power of eigenvectors is that they can turn a coupled problem into independent scalar problems. When they do not form a basis, the failure itself has a mathematical explanation. That is an essential part of learning the subject.

## Inner Products: Measuring Angles and Finding Projections

The ordinary plane comes with lengths and angles. An abstract vector space does not. Knowing how to add vectors and scale them tells us how to construct lines and planes, but not whether two directions meet at a right angle. An inner product adds that geometric information. It is the bridge from algebra to least squares, Fourier coefficients, orthogonal projections, and the spectral theorem.

### The dot product as a measuring device

For real coordinate vectors, take the dot product by multiplying corresponding coordinates and adding the results. The dot product of one, two and three, minus one is one times three plus two times minus one, giving one. A vector's squared length is its dot product with itself. Thus the vector three, four has squared length twenty-five and length five.

The dot product is linear in each input and symmetric. Most importantly, a nonzero vector has positive dot product with itself. An inner product on a real vector space abstracts these features. On complex spaces, the symmetry is replaced by conjugate symmetry: reversing the inputs complex-conjugates the answer. Conjugation also means that linearity must be assigned to one input and conjugate linearity to the other. Either convention is workable when stated and used consistently.

Orthogonality means inner product zero. In Euclidean space, this is the usual perpendicularity. Two nonzero vectors can be orthogonal without either being shorter or longer. Orthogonality is a relation between directions, not a claim about their magnitudes.

### Find the closest point on a line

Suppose we have a vector v equal to two, zero and want the closest point on the line generated by u equal to one, one. Points on the line have the form t times u. Consider the error v minus t u. Its squared length is the square of two minus t, plus the square of zero minus t. Expanding gives four minus four t plus two t squared. Complete the square: two times t minus one squared plus two. The minimum occurs when t equals one. The closest point is one, one; the remaining error is one, minus one.

Notice that the error is perpendicular to the line: one, minus one dotted with one, one gives zero. This is not a coincidence. The closest-point condition is that the error be orthogonal to every direction in the subspace we are approximating by.

The projection of v onto a nonzero vector u is the scalar equal to the inner product of v with u divided by the squared length of u, multiplied by u. For our example, the numerator is two and the denominator is two, so the scalar is one. The formula is the algebraic form of dropping a perpendicular.

### Pythagoras becomes a theorem about approximation

Write v as its projection p plus its orthogonal residual r. The squared length of v equals the squared length of p plus the squared length of r, because the cross terms vanish. This is Pythagoras in inner-product language. For a different candidate point q in the same subspace, v minus q equals r plus p minus q; these two terms are orthogonal. Its squared distance is therefore the squared residual distance plus a nonnegative extra term. The projection is closest, and it is unique.

In a finite-dimensional inner-product space, every subspace has an orthogonal projection. In an infinite-dimensional Hilbert space, the corresponding theorem requires the subspace to be closed. A nonclosed subspace can have points arbitrarily close to a vector without containing an actual nearest point. This is one place where the topology introduced by the norm becomes essential.

### Build perpendicular coordinates with Gram–Schmidt

Suppose our first direction is one, one and the second is one, zero. The first can be normalized to unit length by dividing by the square root of two. To make the second perpendicular to the first, subtract its projection onto the first. The result is one half, minus one half. Normalize that vector too. We now have an orthonormal basis: its vectors have length one and are perpendicular to one another.

This process is Gram–Schmidt orthogonalization. It turns an independent list into an orthonormal one spanning the same subspace. The method makes expansion formulas simple: to find the coefficient of a vector along an orthonormal basis direction, simply take an inner product with that direction. Without orthonormality, computing coordinates requires solving a coupled linear system.

The method also explains the QR factorization of a matrix: Q records orthonormal directions, and R records how the original columns combine to make them. This factorization is useful numerically, though naive Gram–Schmidt can be sensitive to floating-point errors and may require more stable variants.

### Orthogonality in function spaces

The idea extends beyond finite lists of numbers. On a suitable interval, define the inner product of two square-integrable real functions as the integral of their product. Two functions can be orthogonal even if both are nonzero at many points. Sine and cosine waves of different integer frequencies are examples under standard periodic boundary conditions.

Fourier series use this structure. Each coefficient is a projection onto a frequency direction. The residual after using finitely many frequencies is orthogonal to the subspace spanned by those frequencies. The infinite-dimensional version requires convergence theorems, but the geometric picture is already here.

The main lesson is that linear combinations tell us what can be represented, whereas inner products tell us how well one vector approximates another. Projections turn geometry into an optimization problem with an exact answer, and their logic is the foundation of least squares and orthogonal spectral decompositions.

## Least Squares: Fitting Data without Solving an Impossible System

A measurement instrument may be noisy. Ask it three times for the same physical quantity and receive three slightly different answers. If we demand that one unknown equal all three observations exactly, the equations are inconsistent. Yet we still want the best estimate. Least squares replaces an impossible exact system with a precise optimization question, and linear algebra solves it by perpendicularity.

### An overdetermined line fit

Suppose we record three points: at time zero the value is one, at time one it is two, and at time two it is two again. We seek a line with intercept a and slope b, so the prediction at time t is a plus b times t. Fitting exactly would require a equals one, a plus b equals two, and a plus twice b equals two. From the first two equations b equals one, but then the third predicts three, not two. No line passes through all three points.

The residual is the observed value minus the prediction. A least-squares fit chooses a and b to minimize the sum of the squares of the three residuals. Squaring treats positive and negative errors equally and makes the objective a smooth quadratic. Squaring is not always the best statistical model, but it gives a clean mathematical problem and has a strong interpretation when measurement errors are independent Gaussian observations with equal variance.

Put the three observations in a vector y and the model predictions in a vector A times c, where c contains a and b. The first column of A is all ones, representing the intercept. The second contains the time values zero, one, two, representing the slope. The possible predicted vectors form the column space of A, a plane inside the three-dimensional space of possible observations. Our problem is to project y onto that plane.

### Derive the normal equations

At the closest prediction, the residual must be perpendicular to the entire column space of A. In particular, its dot product with each column must vanish. Combining those two conditions gives the normal equations: A transpose times A times c equals A transpose times y.

For the three data points, A transpose times A has rows three, three and three, five. A transpose times y is five, six. So three a plus three b equals five, and three a plus five b equals six. Subtracting gives two b equals one, or b equals one half. Then a equals seven sixths.

The fitted predictions are seven sixths, five thirds, and thirteen sixths. Their differences from the observations are small, and the residual vector, observation minus prediction, is minus one sixth, one third, minus one sixth. Check the orthogonality conditions directly. Its entries sum to zero, so it is perpendicular to the constant column. Multiply the residuals by zero, one and two, and the weighted sum is also zero, so it is perpendicular to the time column. That is the geometry behind the solution.

### Why the solution is best

Could another line fit better? Suppose c star solves the normal equations and c is any alternative. Write the residual for c as the residual for c star minus A times the difference of coefficients. The first residual is perpendicular to every vector of the form A times something. By Pythagoras, the squared error for c is the optimal squared error plus the squared length of A times the coefficient difference. This cannot be smaller.

If the columns of A are independent, then A times the difference vanishes only when the coefficients are equal. In that case the best coefficients are unique. If the columns are dependent, the best predicted vector is still unique, but different coefficient lists may produce it. That distinction between a unique output and nonunique parameters is crucial in statistical modeling.

### Why not always solve the normal equations numerically?

The normal equations are exact mathematics. But forming A transpose times A can worsen numerical conditioning. If the singular values of A range from a large value to a very small one, those of A transpose times A are their squares. The disparity becomes larger, making roundoff errors harder to control.

A QR factorization avoids this squaring. It writes A as an orthonormal-column factor Q times an upper triangular factor R, assuming full column rank. The residual-orthogonality condition becomes R times c equals Q transpose times y, which is solved by back substitution. In more delicate problems, a singular value decomposition helps identify directions the data hardly constrain.

Thus the shortest symbolic formula is not always the most trustworthy numerical algorithm. One should understand both the mathematical minimizer and the floating-point method used to compute it.

### Where the same geometry appears

Least squares underlies polynomial fitting, numerical calibration, linear regression, and parameter estimation. In Fourier analysis, approximating a function by finitely many orthogonal basis functions is also an orthogonal projection: the coefficients are inner products, and the residual is perpendicular to the selected subspace.

If we assign different reliability weights to measurements, the metric changes and so does the projection. If we penalize large coefficients to discourage an unstable fit, we obtain regularized least squares. Those modifications follow naturally once we understand the original problem as projection onto the image of a linear map.

Least squares is not a compromise in rigor because the equations had no exact solution. It asks a different, exactly solvable question: which attainable prediction is closest to the data, under a chosen measure of error? Linear algebra gives both a construction and a proof of optimality.

## Adjoints and the Spectral Theorem: Symmetry Makes Operators Solvable

Imagine stretching a sheet more in one direction than another. If the stretch is purely symmetric, we can find perpendicular axes along which the sheet expands or contracts without shearing between them. A symmetric matrix has an orthonormal eigenbasis. That remarkable conclusion is the finite-dimensional spectral theorem. It explains why many physical and mathematical operators can be studied by independent modes.

### Move an operator across an inner product

Let T be a linear map on an inner-product space. Its adjoint is the operator T star characterized by the following rule: taking the inner product of T applied to u with v is the same as taking the inner product of u with T star applied to v. For real coordinates with the standard dot product, the adjoint matrix is the transpose. For complex coordinates, it is the conjugate transpose.

This is an exact identity for every pair of vectors, not a statement that T and T star have equal entries. It describes the same bilinear measurement from the other side. In a real example, if T sends x, y to two x plus y, three y, then the matrix transpose sends the test vector in the opposite direction of the pairing.

An operator is self-adjoint if T equals T star. For real matrices, that means symmetry across the diagonal. For complex matrices it means Hermitian symmetry: entries below the diagonal are complex conjugates of those above. Complex self-adjoint operators have real eigenvalues, despite acting on complex vector spaces.

### Why the eigenvalues are real

Suppose T is self-adjoint and T v equals lambda v with v nonzero. Pair T v with v. By the eigenvector equation the result is lambda times the squared length of v, under our convention. By self-adjointness this number equals its own complex conjugate. Since squared length is a positive real number, lambda must be real. This is a structural consequence, not a happy accident of a particular matrix.

Two eigenvectors for distinct eigenvalues must be perpendicular. Take the inner product of T u with v. We can evaluate it as lambda times the pairing of u with v. Or move T across the inner product and evaluate it as mu times that pairing. If lambda and mu differ, the pairing must be zero. Thus the independent modes of a self-adjoint operator are automatically orthogonal.

### A symmetric example with actual numbers

Take the matrix with rows two, one and one, two. Apply it to the vector one, one: the output is three, three, so that direction has eigenvalue three. Apply it to one, minus one: the output is one, minus one, so that direction has eigenvalue one. These two directions are perpendicular. Normalize each by dividing by the square root of two and we obtain an orthonormal eigenbasis.

In this basis, the operator is diagonal with entries three and one. Any input decomposes uniquely into those two modes. The first is stretched threefold and the second is unchanged. Matrix powers, exponentials, and many other functions of the operator can now be computed by applying the scalar function to each eigenvalue.

For example, applying the matrix ten times multiplies the first mode by three to the tenth power and leaves the second mode unchanged. Applying an exponential of the matrix multiplies the modes by the corresponding scalar exponentials. This is the finite-dimensional origin of functional calculus.

### Why an orthonormal eigenbasis exists

The difficult part of the spectral theorem is not that different eigenvalues give perpendicular eigenvectors; it is that a self-adjoint operator actually has enough eigenvectors to span the whole space. Here is the finite-dimensional argument in outline.

On the unit sphere, consider the real-valued function sending v to the inner product of T v with v. The unit sphere is compact and this function is continuous, so it attains a maximum. At a maximizing vector, varying v slightly in any perpendicular direction shows that T v has no component in that perpendicular direction. Hence T v is a multiple of v: we found an eigenvector.

Now consider its orthogonal complement. Self-adjointness shows that this complement is preserved by T. Restrict T to that smaller space and repeat. Induction gives an orthonormal basis of eigenvectors. This proof makes clear why finite dimensionality and self-adjointness are doing work. It does not automatically establish the spectral theorem for every unbounded or infinite-dimensional operator; there one needs domain, measure and convergence hypotheses.

### Positive operators and quadratic energy

A self-adjoint operator is positive semidefinite if the inner product of T v with v is never negative. In its eigenbasis this energy is a sum of eigenvalues times squared coordinate magnitudes. Consequently, positivity is equivalent to all eigenvalues being nonnegative. Strict positive definiteness means every eigenvalue is positive in the finite-dimensional self-adjoint setting.

The same structure appears in the Hessian matrix of a smooth real function. Near a critical point, a positive-definite Hessian means the quadratic approximation bends upward in every direction. In mechanical systems, symmetric stiffness matrices have eigenvectors representing normal modes. In statistics, covariance matrices are positive semidefinite because they measure average squared fluctuations.

A symmetric matrix is easy to analyze because its different modes do not interfere under an orthonormal change of coordinates. The spectral theorem turns symmetry in a bilinear pairing into a complete set of independent directions. That is why it reappears in operator theory, geometry, differential equations, and quantum mechanics.

## Singular Values: Stretching, Rank, and Conditioning

Eigenvectors of a square operator can fail to form a basis, and a rectangular matrix may have no ordinary eigenvalue problem at all. Yet every real or complex matrix admits a particularly useful geometric description: rotate the input coordinates, stretch or collapse along perpendicular directions, and rotate the output. The stretch factors are the singular values.

### From circles to ellipses

Imagine the unit circle. A linear transformation usually sends it to an ellipse, possibly flattened into a line segment or point. The ellipse's principal semiaxis lengths are the singular values of the transformation. They describe how much the matrix stretches special perpendicular input directions. This picture generalizes to higher dimensions, including transformations between spaces of different dimensions.

To find the directions, measure the squared output length of an input v. It is the inner product of A v with A v. Move A across the pairing using its adjoint. The result is the inner product of A star A applied to v with v. The operator A star A is self-adjoint and positive semidefinite. The spectral theorem supplies an orthonormal basis of input eigenvectors with nonnegative eigenvalues. The singular values are the square roots of those eigenvalues.

If A star A sends v to sigma squared times v, then A sends that input direction to an output with length sigma times the input length. For two orthogonal input eigenvectors with nonzero singular values, their outputs are orthogonal too. After normalization, those output directions form part of an orthonormal output basis.

### A rank-one example

Take the matrix that sends the input pair x, y to the output pair x plus y, zero. It reports the sum of two coordinates and discards their difference. The vector one, one, normalized by the square root of two, is stretched by a factor of the square root of two and sent horizontally. The perpendicular vector one, minus one, similarly normalized, is completely erased.

Thus the singular values are square root of two and zero. The rank is one because exactly one singular value is positive. The kernel is the one-dimensional direction along which the input is annihilated. This interpretation works for arbitrary matrices: the number of positive singular values equals rank, and the zero-singular-value directions form the kernel.

The singular value decomposition writes A as U times Sigma times V star, where U and V are unitary or orthogonal changes of coordinates and Sigma is a rectangular diagonal array of nonnegative singular values. Unlike diagonalization, it exists for every finite matrix. Singular values do not require a square map or real eigenvalues.

### The operator norm and the weakest direction

The largest singular value is the largest possible output length of a unit input. It is therefore the operator norm induced by Euclidean length. The smallest singular value, when the matrix has full column rank, measures the least stretch of a unit input. If that smallest value is tiny, some input directions hardly change the observations. Recovering the input from slightly perturbed outputs becomes sensitive to noise.

For an invertible square matrix, the ratio of the largest to the smallest singular value is its Euclidean condition number. A ratio near one means similar stretch in all directions. A large ratio indicates strong anisotropy and an ill-conditioned inversion problem. The exact problem can have a perfectly well-defined answer and still be numerically sensitive.

Consider the diagonal matrix with entries one and one millionth. Its inverse exists and has a million on the second diagonal. An observation error of one millionth in the second output coordinate can produce an error of order one in the reconstructed input. No algorithm can reconstruct that input accurately from noisy data without additional information; the instability belongs to the problem, not just the implementation.

### Pseudoinverses and meaningful approximations

A matrix may be rectangular or rank deficient. Singular value decomposition still identifies its supported input and output directions. To compute a least-squares solution of minimum input length, divide by each positive singular value and set the component along each null direction to zero. This constructs the Moore–Penrose pseudoinverse.

That construction explains why the pseudoinverse does not make lost information reappear. If a singular value is zero, no measurement can distinguish movement along its corresponding input direction. Setting that component to zero chooses one particular answer, the minimum-norm one. It does not recover a uniquely determined physical truth.

In practice, dividing by an extremely small positive singular value can amplify noise catastrophically. Truncated singular value decomposition or regularization may deliberately avoid such divisions. Then the result is biased but more stable. The appropriate choice depends on the reliability of data and the scientific question.

### Polar decomposition

There is another useful way to separate geometric actions. Define the positive operator absolute value of A as the positive square root of A star A. Then A can be written as a partial isometry multiplied by this positive stretch operator. Reading the composition from right to left, the stretch occurs first. In the square invertible case, A equals U times the absolute value of A, with U unitary. This is polar decomposition: first stretch along principal directions, then rotate or reflect.

If A has a kernel, the isometric factor need not be unitary on the entire domain; it acts as an isometry on the perpendicular complement of the kernel. That qualification becomes important in infinite-dimensional operator theory, where ranges, closures, and partial isometries require more care.

Singular values are the metric anatomy of a linear map. Eigenvalues explain invariant directions when those exist. Singular values answer a different, always available question: how much can the map stretch, compress, or erase? This is the language connecting least squares, numerical reliability, data compression, inverse problems, and functional analysis.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Determinants: Area, Volume, and Orientation

**Track:** Linear Algebra from First Principles. **Background:** matrix multiplication, invertible maps and coordinates. **Question:** how can one number measure an entire linear transformation's effect on volume?

#### Mathematical companion (not spoken)

For \(A=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\), \(\det A=ad-bc\). The determinant is the unique normalized alternating multilinear function of columns, and \(\det(AB)=\det A\det B\). For a triangular matrix, \(\det A=\prod_i a_{ii}\). The invertibility condition is \(\det A\ne0\). Under a smooth change of variables \(x=\Phi(u)\) with injectivity and regularity assumptions, \(dx=|\det D\Phi(u)|\,du\) in the unsigned integration formula.

##### Exercises with answers

1. Compute \(\det\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}\). **Answer:** five.
2. What does swapping two columns do? **Answer:** changes the sign, preserving magnitude.
3. A map has determinant minus four. What happens to unsigned area? **Answer:** it is multiplied by four; orientation reverses.
4. What is the Jacobian magnitude of \((r,\theta)\mapsto(r\cos\theta,r\sin\theta)\) when \(r>0\)? **Answer:** \(r\).

##### Sources and further reading

- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), determinants and orientation.
- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), determinants through alternating multilinear forms.
- [Determinant](https://en.wikipedia.org/wiki/Determinant).

### Eigenvalues and Eigenvectors: Finding Directions That Do Not Turn

**Track:** Linear Algebra from First Principles. **Background:** matrices, kernels and determinants. **Question:** can one coordinate system reveal a transformation's independent modes?

#### Mathematical companion (not spoken)

An eigenpair satisfies \(Av=\lambda v\), \(v\ne0\). Eigenvalues of \(A\in\mathbb F^{n\times n}\) satisfy \(\det(A-\lambda I)=0\) over a field containing the roots; the eigenspace is \(\ker(A-\lambda I)\). For \(A=\begin{psmallmatrix}2&1\\0&3\end{psmallmatrix}\), eigenvectors \((1,0)\) and \((1,1)\) form columns of \(P=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\); \(P^{-1}AP=\operatorname{diag}(2,3)\). The Jordan shear \(J=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\) has \(J^n=\begin{psmallmatrix}1&n\\0&1\end{psmallmatrix}\) and only one independent eigenvector.

##### Exercises with answers

1. Find the eigenvalues of \(\operatorname{diag}(4,-1)\). **Answer:** four and minus one.
2. Is \((1,1)\) an eigenvector of \(\operatorname{diag}(2,3)\)? **Answer:** no.
3. Is every triangular matrix diagonalizable? **Answer:** no; the Jordan shear is a counterexample.
4. Why does a ninety-degree rotation have no real eigenvector? **Answer:** it takes each nonzero vector to a perpendicular direction, not a real multiple.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), invariant subspaces, eigenvalues and upper-triangular operators.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), eigenvalue computations.
- [Eigenvalues and eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors).

### Inner Products: Measuring Angles and Finding Projections

**Track:** Linear Algebra from First Principles. **Background:** vectors, bases and linear transformations. **Question:** how do distance and perpendicularity arise from a bilinear measurement?

#### Mathematical companion (not spoken)

In a real inner-product space \(\langle\cdot,\cdot\rangle\) is symmetric, bilinear and positive definite. The induced norm is \(\|v\|=\sqrt{\langle v,v\rangle}\). For \(u\ne0\),
\[
\operatorname{proj}_{\mathbb Ru}v=\frac{\langle v,u\rangle}{\langle u,u\rangle}u.
\]
If \(v=p+r\) with \(p\in U\), \(r\perp U\), then \(\|v-q\|^2=\|r\|^2+\|p-q\|^2\) for all \(q\in U\), giving uniqueness of the orthogonal projection. Over \(\mathbb C\), choose the mathematical convention linear in the first argument and conjugate-linear in the second; orthogonal-projection formulas then use \(\langle v,u\rangle/\langle u,u\rangle\).

##### Exercises with answers

1. Project \((2,0)\) onto \(\operatorname{span}\{(1,1)\}\). **Answer:** \((1,1)\).
2. Find the residual. **Answer:** \((1,-1)\), orthogonal to \((1,1)\).
3. Why is \((1,0),(0,1)\) orthonormal? **Answer:** each has unit length and their inner product is zero.
4. What changes for projection onto a nonclosed subspace in an infinite-dimensional space? **Answer:** an actual closest point may not exist.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), inner products, orthonormal bases and operators.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), projections and Gram–Schmidt.
- [Orthogonal projection](https://en.wikipedia.org/wiki/Orthogonal_projection).

### Least Squares: Fitting Data without Solving an Impossible System

**Track:** Linear Algebra from First Principles. **Background:** matrices, orthogonal projections and inner products. **Question:** what is the best approximate answer when equations conflict?

#### Mathematical companion (not spoken)

For \(A\in\mathbb R^{m\times n}\) and \(y\in\mathbb R^m\), minimize \(F(c)=\|Ac-y\|_2^2\). The stationarity condition is \(A^T(Ac-y)=0\). When \(A\) has full column rank, \(A^TA\) is positive definite and the minimizer is unique. For
\[
A=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\quad y=\begin{pmatrix}1\\2\\2\end{pmatrix},\quad
A^TA=\begin{pmatrix}3&3\\3&5\end{pmatrix},\quad A^Ty=\begin{pmatrix}5\\6\end{pmatrix},
\]
one obtains \(c=(7/6,1/2)\) and residual \(r=y-Ac=(-1/6,1/3,-1/6)\), satisfying \(A^Tr=0\). For full-column-rank \(A=QR\) with \(Q^TQ=I\), solve \(Rc=Q^Ty\).

##### Exercises with answers

1. Can a line pass through \((0,1),(1,2),(2,2)\)? **Answer:** no; the slopes between consecutive pairs differ.
2. Compute the residual sum for the least-squares solution above. **Answer:** zero.
3. Why can dependent columns produce nonunique coefficients? **Answer:** a nonzero vector in \(\ker A\) can be added without changing the prediction.
4. Why might QR be numerically preferable to normal equations? **Answer:** it avoids squaring the condition number via \(A^TA\).

##### Sources and further reading

- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), projections and least squares.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), orthogonal projection and fitting.
- [Linear least squares](https://en.wikipedia.org/wiki/Linear_least_squares).

### Adjoints and the Spectral Theorem: Symmetry Makes Operators Solvable

**Track:** Linear Algebra from First Principles. **Background:** inner products, eigenvectors and matrices. **Question:** why are symmetric transformations so much easier to understand than arbitrary ones?

#### Mathematical companion (not spoken)

Use the convention that \(\langle\cdot,\cdot\rangle\) is linear in its first input. The adjoint satisfies \(\langle Tu,v\rangle=\langle u,T^*v\rangle\). In standard real coordinates \([T^*]=[T]^T\); over complex coordinates \([T^*]=\overline{[T]}^T\). If \(T=T^*\), every eigenvalue is real and eigenvectors for different eigenvalues are orthogonal. Finite-dimensional spectral theorem: \(A=Q\Lambda Q^*\) with \(Q\) unitary (orthogonal over \(\mathbb R\)), \(\Lambda\) real diagonal. For \(A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\), normalized eigenvectors are \(u_+=(1,1)/\sqrt2\), \(u_-=(1,-1)/\sqrt2\), with eigenvalues \(3,1\).

##### Exercises with answers

1. Is \(\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) self-adjoint? **Answer:** yes; it equals its transpose.
2. Find the eigenvalues of \(\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\). **Answer:** three and one.
3. Does positive semidefinite mean invertible? **Answer:** no; zero eigenvalues are allowed.
4. Why do distinct eigenvectors of a self-adjoint operator become orthogonal? **Answer:** compare \(\langle Tu,v\rangle\) and \(\langle u,Tv\rangle\).

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), operators on inner-product spaces and the spectral theorem.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), symmetric matrices.
- [Spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem).

### Singular Values: Stretching, Rank, and Conditioning

**Track:** Linear Algebra from First Principles. **Background:** adjoints, positive operators and orthonormal bases. **Question:** can we describe the size distortion of any matrix, even a rectangular one?

#### Mathematical companion (not spoken)

For \(A\in\mathbb C^{m\times n}\), \(A^*A\) is Hermitian positive semidefinite, so its eigenvalues are \(\sigma_i^2\ge0\). An SVD is \(A=U\Sigma V^*\) with \(U\in U(m),V\in U(n)\), \(\Sigma\) rectangular diagonal. \(\|A\|_2=\sigma_{\max}\); \(\operatorname{rank} A\) equals the number of strictly positive singular values. For invertible square \(A\), \(\kappa_2(A)=\sigma_{\max}/\sigma_{\min}\). For \(A=\begin{psmallmatrix}1&1\\0&0\end{psmallmatrix}\), \(A^*A=\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\), with eigenvalues two and zero, so singular values \(\sqrt2,0\). Define \(|A|=(A^*A)^{1/2}\); the polar factor satisfies \(A=U|A|\), with partial-isometry \(U\) on the support of \(|A|\).

##### Exercises with answers

1. Find singular values of \(\operatorname{diag}(3,1)\). **Answer:** three and one.
2. Is zero always a singular value of a rank-deficient square matrix? **Answer:** yes.
3. What does a condition number of one imply for an invertible square matrix? **Answer:** all singular values coincide, so the map is a uniform scale followed by a unitary/orthogonal map.
4. Does a pseudoinverse recover information in the kernel? **Answer:** no; it selects the minimum-norm solution.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), singular value decomposition and positive operators.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), SVD and pseudoinverse.
- [Singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition).
