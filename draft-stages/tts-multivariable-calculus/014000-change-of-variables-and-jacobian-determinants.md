# 014000 — The Change-of-Variables Theorem: What the Jacobian Measures

**Track:** Multivariable Calculus from First Principles. **Background:** determinants, Jacobians, multiple integration. **Question:** why must an integral be rescaled after changing coordinates?

<!-- BEGIN SPOKEN LECTURE -->

# The Change-of-Variables Theorem: What the Jacobian Measures

Imagine drawing a fine square grid on a sheet of rubber and stretching the sheet. A small square becomes approximately a parallelogram. The area of that parallelogram may be larger or smaller than the original square, and it may be turned over. The determinant of the derivative matrix describes the signed first-order area scale. Its absolute value tells us how much area, independent of orientation, is gained or lost.

This is the geometric heart of the change-of-variables theorem. When we integrate a density over a region using new coordinates, the integrand must be multiplied by the absolute value of the Jacobian determinant of the coordinate map. Otherwise we count equal-sized coordinate boxes as equal physical areas even though the transformation may stretch some more than others.

## First see a linear transformation

Take the map from coordinates u and v to x equals two u and y equals three v. A unit square in the u-v plane becomes a rectangle with side lengths two and three in the x-y plane. Its area is six. The derivative matrix has diagonal entries two and three; its determinant is six. This exact computation illustrates the general rule.

Now take x equals u plus v and y equals u minus v. The derivative matrix has rows one comma one and one comma minus one. Its determinant is minus two. The negative sign means the orientation is reversed; the magnitude two means areas are doubled. A unit square maps to a parallelogram of area two. An ordinary area integral must use two, not negative two.

Why retain the sign at all? Signed determinants matter for orientation-sensitive integration, especially differential forms. If we reverse an oriented coordinate chart, an oriented area form changes sign. But mass, physical area and unsigned volume do not become negative. Their change-of-variables formula uses the absolute value.

## A nonlinear map with varying scale

Let x equal u, and let y equal the product of one plus u and v. Take both u and v between zero and one. For a fixed u, the v interval maps to y from zero to one plus u. The image region is therefore between y equals zero and y equals one plus x, with x between zero and one.

The Jacobian matrix has first row one comma zero. The second row is v comma one plus u. Its determinant is one plus u. Integrate that factor over the unit u-v square. The v integral contributes one, and the u integral of one plus u from zero to one gives three halves. So the image has area three halves.

Check by direct geometry. The region is a trapezoid with vertical height one at x equals zero and height two at x equals one. Average height is three halves over width one. Same answer. The nonlinear coordinate calculation and geometric slicing agree.

Notice that the Jacobian is not constant here. A small box at u equals zero maps with area scale one; a small box at u equals one maps with scale two. The integral averages the local stretching across the whole domain. This is why a nonlinear map's area factor must remain inside the integral.

## Statement of the theorem and its boundaries

Suppose a smooth enough coordinate map is one-to-one from a region in the new coordinates onto the region of integration, with a smooth inverse and nonzero Jacobian determinant in the interior. Then the integral of f over the image equals the integral over the new-coordinate region of f composed with the map, times the absolute value of the determinant.

In practical cases it is enough to split the region into suitable pieces, ignoring boundary sets of zero measure. The theorem has more general versions for measurable maps and regions; the essential local picture persists.

A warning: the magnitude of a Jacobian does not correct for multiple counting by itself. If the map traces the same physical region twice, a naive integral over both copies counts it twice. Polar coordinates with angle running from zero to four pi trace the disk twice. Integrating the usual polar area factor over that interval gives twice the disk area. The transformation must be injective almost everywhere on the chosen parametrization or the multiplicity must be handled explicitly.

## Derive the rule from linearization

Take a tiny coordinate box centered at a point. A differentiable map sends its edges approximately to the images of the coordinate edge vectors under the derivative matrix. The volume of the resulting parallelepiped is the absolute determinant times the original box volume. The nonlinear error becomes negligible as the box shrinks. Summing the transformed local contributions and passing to the limit yields the change-of-variables formula under the theorem's hypotheses.

This argument links three foundational ideas. The derivative is a local linear map. The determinant measures the volume scaling of a linear map. The integral is a limit of weighted sums. Their combination makes the change-of-variables theorem almost inevitable.

In later geometry, the same mechanism appears in the transformation law for top-degree differential forms, where orientation is retained instead of discarded. Understanding both versions prevents a persistent confusion: the determinant has a sign, but a physical volume element carries its magnitude.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a \(C^1\) diffeomorphism \(T:U\to V\) between open subsets of \(\mathbb R^n\), and integrable \(f\),
\[
\int_V f(x)\,dx=\int_U f(T(u))\,|\det DT(u)|\,du.
\]
Extensions cover suitable domains up to null boundaries. For \(T(u,v)=(u,(1+u)v)\) on \([0,1]^2\),
\[
DT=\begin{pmatrix}1&0\\v&1+u\end{pmatrix},\quad
\det DT=1+u,\quad
\operatorname{Area}(T([0,1]^2))=\int_0^1\int_0^1(1+u)\,dv\,du=3/2.
\]
For \(T(u,v)=(u+v,u-v)\), \(\det DT=-2\) (oriented scale) and \(|\det DT|=2\) (unsigned area scale). A noninjective parametrization counts with multiplicity unless the domain is appropriately restricted.

### Exercises with answers

1. Find the area scale of \(T(u,v)=(4u,v/2)\). **Answer:** \(|\det DT|=2\).
2. What is the area of the image of \([0,1]^2\) under \((u,v)\mapsto(u+v,u-v)\)? **Answer:** two.
3. Why is \(\det DT\), not \(|\det DT|\), appropriate for oriented top forms? **Answer:** reversing orientation must reverse the sign of an oriented integral.
4. What happens if polar angle covers \(0\le\theta\le4\pi\) on a disk? **Answer:** almost every physical point is counted twice.

### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), change of coordinates.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), Jacobians and substitutions.
- [Integration by substitution](https://en.wikipedia.org/wiki/Integration_by_substitution); [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant).
