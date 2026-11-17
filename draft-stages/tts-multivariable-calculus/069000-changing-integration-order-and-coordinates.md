# Changing Integration Order and Coordinates: Where the Jacobian Comes From

<!-- BEGIN SPOKEN LECTURE -->

# Changing Integration Order and Coordinates: Where the Jacobian Comes From

Imagine spreading a thin layer of material over a table. Its density varies with position. To calculate the total mass, you add up density times little pieces of area. That idea is familiar from single-variable integration, but now the pieces of area can be sliced in more than one direction, and we can describe their positions using different coordinates.

Most mistakes in multiple integration do not begin with an antiderivative. They begin with an incorrect description of the region, a missing Jacobian, or an angle interval that covers the same area twice. We will practice a complete calculation from the region to the answer, and use it to understand why a change of variables works.

## Slice the same triangle two ways

Consider the triangle in the first quadrant bounded by the axes and the line x plus two y equals two. The vertices are zero, zero; two, zero; and zero, one. Suppose the density at the point x, y is simply x. The material is heavier farther to the right.

We can slice this region horizontally. Fix y between zero and one. The left edge is x equal to zero. The right edge is x equal to two minus two y. At that fixed height, integrate x across the slice. The result is one half of the squared right endpoint. Integrate that result over y from zero to one. It gives two thirds.

Now slice vertically. Fix x between zero and two. The lower edge is y equals zero. The upper edge is y equals one minus x divided by two. At that fixed x, the density x is constant along the vertical slice, so the slice contributes x times its height. Integrating from zero to two gives the same two thirds.

Both descriptions are correct. Neither is automatically preferable; one may be simpler when the density changes. But both require that the bounds describe precisely the same triangle, without omitting or double-counting any interior point.

A good way to set bounds is to say the region aloud before writing an integral. Every point has x nonnegative, y nonnegative, and x plus twice y at most two. Then choose a direction to sweep. Ask where a sweep line enters and leaves the region. Express those two edges in terms of the outer variable.

That method prevents a common confusion: an outer integral's bounds must be constants or depend only on variables integrated even farther outside, not on a variable that has already been integrated away.

## The determinant measures local area distortion

Now replace the physical x and y coordinates by new coordinates u and v. Take the simple transformation x equals u plus v, and y equals u minus v. Under this transformation, a tiny increase in u moves the physical point right by one and up by one. A tiny increase in v moves it right by one and down by one.

A small rectangle in u-v coordinates does not remain a rectangle in the physical plane. It becomes a parallelogram. The two edge vectors are one, one and one, minus one. The area of their parallelogram is the absolute value of their determinant, which is two. Therefore a tiny u-v rectangle of area one ten-thousandth maps to a physical parallelogram of area about two ten-thousandths.

For this linear map the factor is exactly two, at every location and every scale. For a nonlinear transformation, the derivative matrix varies from point to point. On a sufficiently small coordinate patch, the transformation behaves nearly like its derivative, so the determinant of that derivative gives the local area scaling.

Notice the absolute value. The determinant of our particular transformation is negative two, because it reverses orientation. But area does not become negative. When transforming an ordinary mass or area integral, use the absolute determinant. Orientation will matter later when we integrate directed flux and circulation, but there we will account for it with an oriented normal or tangent rather than by making area negative.

Let's compute with the new coordinates. Take the unit square where u and v each run from zero to one. Map it into the physical plane using our transformation. This produces a parallelogram. Suppose the density is x squared plus y squared. Under the substitution, x squared plus y squared becomes twice u squared plus twice v squared. The area scale contributes another factor of two. The total integral is therefore the double integral over the unit square of four times the sum of u squared and v squared. Each square contributes one third upon integration across the unit interval, so the total is eight thirds.

This example is useful because every step can be checked: transform the region, transform the density, and transform the area element. Forget any one of them and you get a different answer.

## Polar coordinates are a moving basis

The linear transformation just used had fixed edge vectors. Polar coordinates instead depend on radius and angle. A point is described by its distance r from the origin and its angle theta. The physical coordinates are r times cosine theta and r times sine theta.

An increase in radius moves the point outward by one unit per unit change of r. An increase in angle turns the point around a circle. At radius r, a small angular change of size delta theta sweeps out an arc whose length is approximately r times delta theta. So a tiny radial-angular rectangle has physical area approximately delta r times r delta theta.

This is the missing factor in polar integration: r. It comes from how the coordinates stretch lengths, not from a convention to memorize. If you integrate a constant density on a disk and forget r, you would incorrectly find an answer proportional to the disk's radius instead of to its radius squared.

Try a more informative example. Over the disk of radius two, integrate the function x squared plus y squared. In polar coordinates, that density is simply r squared. The area element contributes one more r, so the radial part is r cubed. Integrating r from zero to two gives four; integrating angle over one full turn gives two pi. The result is eight pi.

There is a useful interpretation. The disk has area four pi, and the average value of squared distance from its center is two. Four pi times two is eight pi. That independent check is a good way to catch a lost factor of r.

## When the coordinates fold or overlap

Polar coordinates raise an important question. The point at the origin has no uniquely determined angle. Even away from the origin, theta and theta plus a full turn describe the same point. How can the change-of-variables theorem still be valid?

For the disk calculation we restrict theta to one interval spanning a full turn, so each nonzero point is represented once except along the chosen seam. The origin and seam are lower-dimensional sets that do not change the area integral of an ordinary bounded, integrable density. The Jacobian is zero at radius zero, precisely where polar coordinates lose their ordinary local inverse.

The general theorem requires attention to the map's domain and multiplicity. A smooth one-to-one coordinate transformation with an appropriate nonzero Jacobian on the interior gives the familiar absolute-determinant rule. If the map covers the same region twice, simply integrating over the full parameter domain usually counts its contribution twice. If the map collapses entire positive-area regions, different analysis is needed. The determinant is local; it does not by itself tell you how many times the domain is covered globally.

## The third dimension: cylindrical and spherical volume

Cylindrical coordinates are polar coordinates with an additional height z. The physical volume element is r times the radial, angular, and vertical increments. In a vertical cylinder, this is often the most economical description: one radius, one angle, and one independent height.

Spherical coordinates add another geometric scale. Let rho be distance from the origin, theta the angle around the vertical axis, and phi the angle measured down from the positive vertical axis. At fixed rho and phi, changing theta sweeps a circle of radius rho times sine phi. Changing phi sweeps a meridian arc of length rho times the change in phi. Changing rho moves radially. Multiply the three local lengths, and the volume factor is rho squared times sine phi.

We can verify this using the volume of a ball of radius R. Integrate the volume factor over rho from zero to R, phi from zero to pi, and theta over a full turn. The radial integral gives R cubed divided by three. The phi integral of sine phi gives two, and the theta integral gives two pi. We obtain four pi R cubed divided by three, as expected.

A more diagnostic check is to integrate z squared over that ball. In spherical coordinates z is rho cosine phi. Multiplying by the volume element gives rho to the fourth times cosine squared phi times sine phi. The three integrals produce four pi R to the fifth divided by fifteen. We can independently check that answer using symmetry: the integrals of x squared, y squared, and z squared over a ball are equal, and their sum is the integral of squared radial distance.

You do not need to memorize three disconnected Jacobian formulas if you can reconstruct their geometry. The determinant is the area or volume of the tiny parallelogram or parallelepiped formed by coordinate edge vectors. Polar and spherical factors are cases of the same principle.

## The complete substitution checklist

Before computing a multiple integral in new coordinates, do four things. First, specify the original region as inequalities or boundaries. Second, describe the transformation and the new parameter region, watching for overlaps or missing pieces. Third, replace the integrand with its expression in the new coordinates. Fourth, multiply by the absolute value of the Jacobian determinant.

Then test the result against something simple: an area, a volume, a symmetry argument, or a second integration order. These independent checks are often more valuable than another page of algebra.

The deeper connection is that differentiation and integration are not separate subjects here. Differentiation tells us how a coordinate map stretches tiny regions. Integration adds the contributions of those regions. Once you understand the Jacobian as a local linear map, the change-of-variables theorem becomes a natural next step rather than a mysterious extra factor.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### A triangular region in two orders

For \(T=\{(x,y):x,y\ge0,\ x+2y\le2\}\),
\[
\iint_T x\,dA
=\int_0^1\int_0^{2-2y}x\,dx\,dy
=\int_0^1\frac12(2-2y)^2\,dy=\frac23.
\]
Alternatively,
\[
\iint_Tx\,dA=\int_0^2\int_0^{1-x/2}x\,dy\,dx
=\int_0^2\left(x-\frac{x^2}{2}\right)dx=\frac23.
\]

### A linear change of variables with a sign reversal

Let \(x=u+v\), \(y=u-v\), with \(0\le u,v\le1\). Then
\[
DT=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
\det DT=-2,\quad |\det DT|=2.
\]
For the image parallelogram \(P=T([0,1]^2)\),
\[
\iint_P(x^2+y^2)\,dA
=\int_0^1\!\int_0^1[2u^2+2v^2]2\,du\,dv=\frac83.
\]

### Polar and spherical Jacobians

With \(T(r,\theta)=(r\cos\theta,r\sin\theta)\),
\[
DT=\begin{pmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{pmatrix},\quad
\det DT=r.
\]
Thus
\[
\iint_{x^2+y^2\le4}(x^2+y^2)\,dA
=\int_0^{2\pi}\!\int_0^2r^3\,dr\,d\theta=8\pi.
\]
For spherical coordinates \((x,y,z)=(\rho\sin\phi\cos\theta,\rho\sin\phi\sin\theta,\rho\cos\phi)\),
\[
|\det DT|=\rho^2\sin\phi,\quad 0\le\phi\le\pi,
\]
and
\[
\iiint_{B_R}z^2\,dV
=\int_0^{2\pi}\!\int_0^\pi\!\int_0^R\rho^4\cos^2\phi\sin\phi\,d\rho\,d\phi\,d\theta
=\frac{4\pi R^5}{15}.
\]

### What the theorem assumes

For a \(C^1\) injective coordinate transformation with nonzero Jacobian on the interior, the usual change-of-variables theorem says
\[
\int_{T(U)} f(x)\,dx=\int_U f(T(u))\,|\det DT(u)|\,du
\]
under standard regularity/integrability hypotheses. Polar and spherical charts may have seam or pole sets of measure zero; these should be handled by chart restrictions or almost-everywhere arguments, not by pretending the mapping is globally one-to-one.

### Exercises with answers

1. **Reverse the triangle.** Describe \(T\) with x outermost. **Answer:** \(0\le x\le2\), \(0\le y\le1-x/2\).
2. **Constant area check.** Find the area of the parallelogram \(P\). **Answer:** determinant magnitude \(2\) times unit-square area \(1\), hence \(2\).
3. **Radial power.** Find \(\iint_{x^2+y^2\le a^2} (x^2+y^2)\,dA\). **Answer:** \(2\pi\int_0^a r^3dr=\pi a^4/2\).
4. **Spherical symmetry.** Compute \(\iiint_{B_R}(x^2+y^2+z^2)\,dV\). **Answer:** \(4\pi R^5/5\); each coordinate-square integral is one third of it.
5. **Double covering.** Why not integrate over \(0\le\theta\le4\pi\) to find the area of the unit disk without another factor? **Answer:** nonzero points are covered twice; the resulting integral counts the area twice.

### Sources and further reading

- [OpenStax, *Calculus Volume 3*, §5.7, Change of Variables in Multiple Integrals](https://openstax.org/books/calculus-volume-3/pages/5-7-change-of-variables-in-multiple-integrals), the determinant rule and coordinate examples.
- [MIT OpenCourseWare 18.02SC](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), double and triple integration practice.
- [Wikipedia: Change of variables](https://en.wikipedia.org/wiki/Integration_by_substitution#Substitution_for_multiple_variables), overview and measure-sensitive qualification.
- [Wikipedia: Spherical coordinate system](https://en.wikipedia.org/wiki/Spherical_coordinate_system), geometry and coordinate conventions; note that texts interchange the angle names.
- Existing survey: `multivariable-calculus:008000` summarizes multiple integrals and Jacobian geometry.
