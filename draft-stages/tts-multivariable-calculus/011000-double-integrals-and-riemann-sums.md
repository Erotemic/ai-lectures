# 011000 — Double and Triple Integrals: Adding Values Across a Region

**Track:** Multivariable Calculus from First Principles. **Background:** one-variable Riemann integrals, areas and volumes. **Question:** how does an integral add contributions over a two- or three-dimensional domain?

<!-- BEGIN SPOKEN LECTURE -->

# Double and Triple Integrals: Adding Values Across a Region

A road map can describe the temperature at every point on a field. A single temperature reading tells us little about the total heat content. To combine information across the whole field, we divide the region into small patches, multiply each patch's area by a representative temperature, add the contributions, and let the patches become small. That is a double integral.

The familiar one-variable integral uses intervals of small length. In two variables the pieces have small area. In three variables they have small volume. The principle is the same: a sum weighted by the size of each piece converges to an integral if the function and domain behave well enough.

## A rectangle and a complete calculation

Take the unit square, where x and y each run from zero to one. Let the density at a point be x plus twice y. This is nonnegative on the square and increases as we move right or up. To find the total mass of a sheet with this density, divide the square into tiny rectangles. At a sample point in each rectangle, evaluate x plus twice y and multiply by the rectangle's area. Add the contributions.

As the subdivisions become fine, the sum approaches the double integral over the square. We can calculate it using one-variable antiderivatives. First integrate with respect to x while keeping y fixed. The result from zero to one is one half plus twice y. Next integrate that expression with respect to y from zero to one. We obtain one half plus one, or three halves.

There is a useful check. The average value of x on the unit square is one half; the average value of y is one half. The average of x plus twice y is one half plus twice one half, which is three halves. Since the square has area one, its total mass is also three halves.

The units keep the calculation honest. If density is measured in kilograms per square meter and coordinates are measured in meters, then density times area gives kilograms. The integral is not a mysterious anti-derivative symbol; it is the limit of a weighted sum.

## Integrating over a curved region

What if the region is a disk rather than a rectangle? We can still divide a containing rectangle into small boxes, count the pieces that lie inside the region, and approximate the curved boundary more and more closely. For a bounded region with a sufficiently regular boundary and a continuous bounded integrand, the boundary contribution disappears in the limit as the mesh gets fine.

The value of the integral depends on both the function and the region. Two regions with the same area need not give the same integral of a nonconstant density. The function may be larger on one region than the other. This is why the domain must be specified explicitly, not merely sketched vaguely.

When the integrand equals one, the double integral gives the area of the region. When it equals a constant density rho, the integral gives rho times area. When it varies, the integral adds all local contributions. Similarly, integrating one over a solid region gives its volume.

## Three dimensions

Imagine a cube one meter on each side with a density that depends only on height z, say one plus z. The bottom has density one and the top density two. Divide the cube into tiny boxes. Each contribution is density times small volume. Integrating first over the horizontal square gives area one times the density at height z. Integrating from height zero to one gives one plus one half, or three halves units of mass.

This shows how triple integration can sometimes be understood as stacking thin slices. The same idea works when each horizontal slice has a different area, provided we describe that area correctly. A ball is a natural example: its slices perpendicular to an axis are disks of varying radius.

## What conditions are being assumed?

For a continuous function on a compact rectangle, ordinary Riemann sums converge to an integral. For bounded regions with suitably negligible boundaries, the same works after extending the integrand by zero outside. There are more complicated bounded functions and sets for which Riemann integration is inadequate; Lebesgue integration offers a broader framework. Our first goal is to understand the geometric sum and compute it on well-behaved regions.

A double integral is not automatically a single-variable integral with an extra symbol attached. It expresses a fundamentally two-dimensional sum. The reason iterated single-variable integrals can compute it is a theorem, with hypotheses. That theorem is the subject of the next step.

## Looking ahead conceptually

Double and triple integrals appear whenever a local quantity must be accumulated over an area or volume. Density gives mass, probability density gives probability, and energy density gives total energy. A change of variables will let us use coordinates adapted to the shape of the region. But that change will require a scale factor: a tiny coordinate rectangle may not represent a rectangle of equal physical area.

For now the defining picture is enough. Cut the region into small pieces, approximate each contribution, add, and take the limit. Every later integration theorem is a way of making that fundamental construction more efficient or more invariant.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(R=[a,b]\times[c,d]\), with tagged partitions \(R=\bigcup R_{ij}\), the Riemann integral is the limit of
\[
\sum_{i,j}f(\xi_{ij},\eta_{ij})\,\Delta x_i\Delta y_j
\]
as mesh size tends to zero, independent of sample choices. For \(f(x,y)=x+2y\) on \([0,1]^2\),
\[
\int_0^1\!\int_0^1(x+2y)\,dx\,dy
=\int_0^1(1/2+2y)\,dy=3/2.
\]
For \(\rho(x,y,z)=1+z\) on \([0,1]^3\), \(\iiint\rho\,dV=3/2\). For a bounded Jordan-measurable region \(D\), integrals over \(D\) can be viewed as integrals of \(f\mathbf 1_D\) over an enclosing rectangle, when that function is Riemann-integrable.

### Exercises with answers

1. Compute \(\int_{[0,2]\times[0,1]}1\,dA\). **Answer:** two, the area of the rectangle.
2. Compute \(\int_{[0,1]^2}xy\,dA\). **Answer:** one fourth.
3. A cube of side two has constant density three. What is its mass? **Answer:** \(3\cdot 2^3=24\).
4. Why does an integrand of one yield area or volume? **Answer:** each weighted Riemann-sum contribution equals the geometric size of its piece.

### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), multiple integration.
- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), double and triple integrals.
- [Multiple integral](https://en.wikipedia.org/wiki/Multiple_integral); [Riemann integral](https://en.wikipedia.org/wiki/Riemann_integral).
