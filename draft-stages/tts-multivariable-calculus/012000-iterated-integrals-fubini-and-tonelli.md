# 012000 — Iterated Integrals: Slicing Regions and Exchanging the Order

**Track:** Multivariable Calculus from First Principles. **Background:** double integrals and one-variable integration. **Question:** when can a two-dimensional integral be computed by integrating one variable at a time?

<!-- BEGIN SPOKEN LECTURE -->

# Iterated Integrals: Slicing Regions and Exchanging the Order

Imagine a triangular garden. Rather than trying to calculate its area in one two-dimensional step, we can slice it into thin vertical strips. At each x coordinate, the strip runs between a lower y boundary and an upper y boundary. Find the area or mass of the strip by integrating in y, then accumulate the strips by integrating in x. This is an iterated integral.

The method is familiar from elementary geometry. The theorem that justifies it is a form of Fubini's theorem: under suitable integrability assumptions, integrating successively in the two variables equals integrating over the whole region. We must understand the region and the assumptions, not only the notation.

## Describe a triangle carefully

Take the region where zero is at most y, y is at most x, and x is at most one. Draw it or imagine a right triangle under the diagonal y equals x in the unit square. For a fixed x between zero and one, y ranges from zero to x. The integral of x plus y over that region becomes an outer integral over x from zero to one and an inner integral over y from zero to x.

Perform the inner integral. Since x is fixed, integrating x with respect to y contributes x times x, or x squared. Integrating y contributes half of x squared. The total is three halves times x squared. Integrating from zero to one gives one half. Thus the total mass for this density is one half.

We can calculate the same integral by horizontal slicing. A fixed y lies between zero and one. The condition y at most x says x runs from y to one. Integrating x plus y first in x produces one half of one minus y squared, plus y times one minus y. Simplify and integrate from zero to one; the result is again one half.

Changing the order is often the fastest way to simplify a difficult integral. But the limits must describe the same region, not just use the same numbers in a different order. A common error is to swap the integration symbols while leaving the bounds unchanged even though the bounds depend on the other variable.

## The rectangular case

For a continuous function on a closed rectangle, both orders of iterated integration are valid and equal to the double integral. The continuity hypothesis ensures ordinary Riemann integrability and avoids many pathologies. For more general measurable functions, the correct theorem has conditions on integrability and signs.

A nonnegative measurable function can be integrated with Tonelli's theorem, even if the result is infinite. Nonnegative contributions cannot cancel to conceal a divergent total. For a signed measurable function, Fubini's theorem is safely applied when the integral of the absolute value is finite. Under this absolute-integrability condition, both iterated integrals exist almost everywhere in the relevant sense and agree with the multiple integral.

This distinction is not merely technical. Reordering infinitely many positive terms is safe in an extended sense; reordering conditionally convergent signed terms can change their sum. Integrals have a related issue. When you meet a function with singularities, or a domain of infinite extent, check nonnegativity or absolute integrability before exchanging operations.

## Slicing a solid

For a three-dimensional region, choose a coordinate such as z. At each height, the horizontal cross-section has some area A of z. The volume equals the integral of A of z over the permitted heights, for well-behaved solids.

For the unit ball, the slice at height z is a disk of radius the square root of one minus z squared. Its area is pi times one minus z squared. Integrate this from minus one to one. We get pi times two minus two thirds, or four pi over three, the volume of the unit ball. The same calculation extends to a ball of radius R and produces four pi R cubed over three.

This argument is more than memorizing the sphere-volume formula. It shows how higher-dimensional accumulation can be organized into nested lower-dimensional problems. It also explains why units multiply: an area times a small thickness produces a small volume.

## Why order can matter computationally even when it does not mathematically

Suppose the region is easier to describe vertically than horizontally. The integral with vertical slices may have simple bounds; the horizontal description could require splitting into several pieces. The two results are mathematically equal under the theorem, but one setup is easier and less error prone.

Similarly, an integrand that is hard to integrate with respect to x might be simple with respect to y. Before beginning symbolic integration, inspect the region and the formula. Choosing the order is part of solving the problem, not a mechanical afterthought.

The essential picture is that a multiple integral totals contributions over an entire region, while iterated integrals total them in successive families of slices. Tonelli and Fubini tell us when these two ways of accumulating information are equivalent.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(D=\{(x,y):0\le y\le x\le1\}\) and \(f(x,y)=x+y\). Then
\[
\int_0^1\int_0^x(x+y)\,dy\,dx
=\int_0^1\tfrac32 x^2\,dx=\tfrac12,
\]
whereas reversing order gives
\[
\int_0^1\int_y^1(x+y)\,dx\,dy
=\int_0^1\left(\tfrac12+y-\tfrac32y^2\right)dy=\tfrac12.
\]
For the unit ball \(B^3\), the section at height \(z\) has area \(\pi(1-z^2)\); hence
\[
\operatorname{Vol}(B^3)=\int_{-1}^1\pi(1-z^2)\,dz=4\pi/3.
\]
**Conditions:** Tonelli applies to nonnegative measurable functions (extended values are allowed). Fubini applies to integrable functions, for instance \(\int |f|<\infty\). For continuous functions on compact rectangular domains the Riemann versions suffice.

### Exercises with answers

1. Reverse \(\int_{x=0}^1\int_{y=0}^{x}1\,dy\,dx\). **Answer:** \(\int_{y=0}^1\int_{x=y}^11\,dx\,dy=1/2\).
2. Compute \(\int_0^1\int_0^x xy\,dy\,dx\). **Answer:** \(\int_0^1x^3/2\,dx=1/8\).
3. Find the volume of a ball of radius \(R\) by slicing. **Answer:** \(\int_{-R}^{R}\pi(R^2-z^2)\,dz=4\pi R^3/3\).
4. What hypothesis lets you exchange integrals of a signed measurable function without relying on cancellation? **Answer:** absolute integrability, \(\int |f|<\infty\).

### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), iterated integrals and regions.
- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), integration order.
- [Fubini's theorem](https://en.wikipedia.org/wiki/Fubini%27s_theorem); [Tonelli's theorem](https://en.wikipedia.org/wiki/Fubini%27s_theorem#Tonelli's_theorem).
