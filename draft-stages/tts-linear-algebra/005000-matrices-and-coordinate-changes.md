# 005000 — Matrices, Composition, and Changing Coordinates

**Track:** Linear Algebra from First Principles. **Background:** bases and linear maps. **Question:** how can the same transformation have different matrices without changing its action?

<!-- BEGIN SPOKEN LECTURE -->

# Matrices, Composition, and Changing Coordinates

Suppose a city uses streets running east and north, while a surveyor uses directions running northeast and southeast. Both can describe the same movement, but the pairs of numbers assigned to it differ. The movement does not change. The coordinate language changes. This distinction is the central discipline behind matrix algebra.

## Columns tell us what happens to basis directions

Choose a basis of an input vector space and a basis of an output vector space. To represent a linear map, ask where each input basis vector goes and write the coordinates of its image as a column. The resulting rectangle of columns is a matrix. Multiplying that matrix by a coordinate column gives the output coordinates.

For a simple example, let a map of the plane send the first coordinate direction to twice itself, and send the second to the sum of the two coordinate directions. Its matrix has first column two, zero and second column one, one. An input with coordinates three, four becomes ten, four, because three copies of two, zero plus four copies of one, one give ten, four.

The dimensions of a matrix tell us the types of vectors it accepts and produces. A matrix with m rows and n columns represents a map from an n-dimensional coordinate space to an m-dimensional one. A square matrix is needed to describe an endomorphism, a map from a space to itself in chosen bases, but linear maps need not be square.

## Matrix multiplication is composition

Suppose the first transformation sends a vector x to B times x. A second sends that result to A times it. Performing B and then A is the composite map: A times B times x. This fixes the order of matrix multiplication. The rightmost transformation acts first.

Why are the entries of the product formed from rows dotted against columns? Take a basis input. The columns of B are its outputs under the first map. Apply A to each of those output columns. Those are precisely the columns of the composite map. The usual multiplication formula is not arbitrary bookkeeping; it is forced by composition and the column convention.

Order matters. Rotate a rectangle ninety degrees and then stretch its horizontal direction. Stretch horizontally first and rotate afterward. The final shapes are generally different. Matrices therefore need not commute. A times B usually differs from B times A. Never cancel or rearrange matrix factors merely because ordinary real numbers permit it.

## One vector, two descriptions

Let the standard coordinates of the plane be x and y. The surveyor's new basis is the vector one, one followed by the vector one, minus one. Call them u and v. To represent the point with standard coordinates four, two, find coefficients a and b with a u plus b v equal to four, two. The equations are a plus b equals four and a minus b equals two. Thus a equals three and b equals one. The same vector is four, two in standard coordinates and three, one in the surveyor's basis.

Place the new basis vectors as columns in a matrix P. Then ordinary coordinates equal P times new coordinates. To go the other way, multiply by the inverse of P. For this example, the inverse takes x, y to one half of x plus y and one half of x minus y. New coordinates are not an alternative physical vector; they are an alternative list of coefficients describing it.

If a linear operator T acts on the plane, and A is its standard matrix, its new-coordinate matrix is P inverse times A times P. Read the operations from right to left: convert new coordinates into standard ones; apply the operator; convert the output back to the new basis. This is the similarity transformation. It changes the matrix but not the underlying linear operator.

## Why eigenvalues survive changing bases

Consider multiplying all horizontal coordinates by two and all vertical ones by three. Its matrix in standard coordinates is diagonal, with two and three on the diagonal. In the diagonal-and-antidiagonal surveyor basis, the matrix is no longer diagonal; each displayed coordinate mixes with the other. Yet the map still stretches one physical direction by two and another by three. Those characteristic stretch factors, the eigenvalues, do not depend on our choice of coordinate language.

This observation explains why much of linear algebra seeks invariants. A rank is the number of independent output directions, not the number of nonzero entries in one displayed matrix. An eigenvalue is a property of an operator, not of the visual position of a matrix entry. A determinant changes predictably with bases for maps between different spaces, but for a single operator the determinant is unchanged by similarity.

## Inverses and identity maps

An identity map leaves every vector fixed. Its matrix has ones on the diagonal and zeros elsewhere. If a map is invertible, there is another map that exactly undoes it. In coordinates, multiplying the two matrices in either order yields the identity. Row reduction supplies a systematic way to determine whether this is possible and, if so, to calculate the inverse.

For a linear map between finite-dimensional spaces of equal dimension, invertibility, injectivity, surjectivity, and full rank are equivalent. They are not equivalent without the equal-dimension qualification. Embedding a plane into three-space is injective, but no inverse defined on all of three-space is possible.

The main lesson is that a matrix is a coordinate account of a transformation. Choosing convenient coordinates may make a calculation much easier, but the map's mathematical content must not depend on which coordinate system we happen to write down.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Given ordered bases \(\mathcal B\) of \(V\) and \(\mathcal C\) of \(W\), \([T]_{\mathcal C\leftarrow\mathcal B}\) has columns \([T(b_j)]_{\mathcal C}\). Composition gives \([S\circ T]=[S][T]\) with bases matched. Let \(P=[u\ v]=\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}\). Then \([x]_{\mathrm{std}}=P[x]_{\mathcal B}\), \([x]_{\mathcal B}=P^{-1}[x]_{\mathrm{std}}\), and \([T]_{\mathcal B}=P^{-1}[T]_{\mathrm{std}}P\). For \(A=\operatorname{diag}(2,3)\), \(P^{-1}AP=\begin{psmallmatrix}5/2&-1/2\\-1/2&5/2\end{psmallmatrix}\).

### Exercises with answers

1. What are the columns of the identity matrix? **Answer:** the coordinate basis vectors.
2. Express \((4,2)\) in the basis \(((1,1),(1,-1))\). **Answer:** \((3,1)\).
3. Why is \(AB\) the matrix for first \(B\), then \(A\)? **Answer:** its \(j\)-th column is \(A\) applied to the \(j\)-th column of \(B\).
4. Does changing basis change the kernel dimension? **Answer:** no, because coordinate isomorphisms do not change the underlying solution space.

### Sources and further reading

- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), matrices and coordinate systems.
- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), matrices of linear maps.
- [Change of basis](https://en.wikipedia.org/wiki/Change_of_basis).
