# 006000 — Determinants: Area, Volume, and Orientation

**Track:** Linear Algebra from First Principles. **Background:** matrix multiplication, invertible maps and coordinates. **Question:** how can one number measure an entire linear transformation's effect on volume?

<!-- BEGIN SPOKEN LECTURE -->

# Determinants: Area, Volume, and Orientation

Draw a little square on a rubber sheet. Apply a linear transformation: perhaps the square tilts into a parallelogram, stretches, or collapses to a line. The determinant measures the signed factor by which its area changes. In higher dimensions, it measures the corresponding signed volume factor. This geometric idea explains the algebraic rules and also why a determinant of zero means noninvertibility.

## Start with two directions

Take two vectors in the plane. Their parallelogram area, with a sign recording orientation, can be computed from their four coordinates. If the first vector is a, c and the second is b, d, the signed area is a times d minus b times c. Write the vectors as columns of a two-by-two matrix. That expression is its determinant.

For example, take the vectors two, zero and one, three. The parallelogram has base two and height three, so area six; the determinant also gives six. Reverse the order of the columns and the oriented area becomes minus six. The geometric region did not acquire negative physical area; the sign records that we reversed the ordered directions.

If the vectors are collinear, their parallelogram is flat and has zero area. The determinant vanishes. Conversely, a zero determinant in two dimensions means one column is a multiple of the other, so there is no two-dimensional area left. We have lost an independent direction.

## Why the determinant multiplies

Suppose one linear map multiplies area by a signed factor of three. Then another map multiplies area by a signed factor of minus two. Applying both changes signed area by minus six. This gives the determinant of a composite as the product of the two determinants. In matrix language, determinant of A times B equals determinant of A times determinant of B.

This rule applies in all finite dimensions. It immediately implies that the identity has determinant one, and if A is invertible, the determinant of its inverse is one over the determinant of A. A zero determinant cannot belong to an invertible map. Indeed, any invertible map must preserve n-dimensional volume up to a nonzero scale, because its inverse would otherwise have to restore volume from a collapsed object.

Swapping two columns reverses orientation and changes the determinant's sign. Multiplying a column by a factor multiplies the determinant by that factor. Adding a multiple of one column to a different column does not change volume, because it shears the parallelepiped without changing its altitude. These properties also hold for rows and explain how to compute determinants using elimination.

## Calculating without memorizing enormous formulas

For a triangular matrix, its determinant is the product of its diagonal entries. Eliminate entries below the pivots using row additions, which do not change the determinant. Keep track of row swaps, which flip the sign, and rescalings, which change the magnitude. The final triangular matrix reveals the result as a product of pivots.

As a test, take a matrix with rows two, one and one, three. Its determinant is six minus one, or five. Elimination replaces the second row by itself minus one half of the first, leaving the lower diagonal entry at two and a half. Multiply it by the upper pivot two and you get five again.

For a larger matrix, computing the determinant is usually a consequence of a reliable factorization, not a reason to expand a huge alternating sum. The conceptual definition, however, uses the fact that there is essentially one alternating, multilinear way to assign a signed unit volume to n ordered vectors once a unit orientation is chosen.

## Determinants and linear equations

A square matrix has nonzero determinant exactly when its columns form a basis. That means the associated linear system has a unique solution for every right-hand side. A zero determinant means the columns are dependent, so some input direction is invisible and the map fails to be invertible.

This is also why a determinant appears in the inverse function theorem. A smooth map can be approximated near a point by its derivative matrix. If that derivative has nonzero determinant, its first-order behavior preserves all local directions. Under the theorem's hypotheses, the nonlinear map is locally invertible. A nonzero determinant is not a guarantee of global invertibility: two distant points may still map to the same output.

## The Jacobian in a change of variables

Now think of integrating a function over a region. If we introduce new coordinates related by a linear map, every small box has its volume scaled by the absolute value of the determinant. That is why the determinant's magnitude enters multivariable integration. We use the absolute value for ordinary unsigned volume; the sign is retained when orientation matters, such as in integrals of differential forms.

Take polar coordinates away from the origin. The map from radius and angle to Cartesian coordinates is nonlinear, but its derivative at each point has determinant equal to the radius. A tiny rectangle in radius-angle space corresponds to an area approximately radius times its coordinate area. Hence the familiar extra factor of radius in a polar integral. The derivative determinant is the local volume correction, not an algebraic decoration.

One limitation deserves emphasis. Determinants belong to square linear maps and to top exterior powers of maps between equally dimensional spaces. For a rectangular matrix, notions of volume distortion use singular values or Gram determinants instead. Never attach a determinant to an arbitrary rectangular matrix as though the usual formula applied unchanged.

The determinant compresses three stories into one number: whether the transformation loses a dimension, how much volume it scales, and whether it preserves or reverses orientation. Those stories reappear in differential geometry, degree theory, probability densities, and manifold integration.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\), \(\det A=ad-bc\). The determinant is the unique normalized alternating multilinear function of columns, and \(\det(AB)=\det A\det B\). For a triangular matrix, \(\det A=\prod_i a_{ii}\). The invertibility condition is \(\det A\ne0\). Under a smooth change of variables \(x=\Phi(u)\) with injectivity and regularity assumptions, \(dx=|\det D\Phi(u)|\,du\) in the unsigned integration formula.

### Exercises with answers

1. Compute \(\det\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}\). **Answer:** five.
2. What does swapping two columns do? **Answer:** changes the sign, preserving magnitude.
3. A map has determinant minus four. What happens to unsigned area? **Answer:** it is multiplied by four; orientation reverses.
4. What is the Jacobian magnitude of \((r,\theta)\mapsto(r\cos\theta,r\sin\theta)\) when \(r>0\)? **Answer:** \(r\).

### Sources and further reading

- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), determinants and orientation.
- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), determinants through alternating multilinear forms.
- [Determinant](https://en.wikipedia.org/wiki/Determinant).
