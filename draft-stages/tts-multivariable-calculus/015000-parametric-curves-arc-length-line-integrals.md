# 015000 — Curves and Line Integrals: Measuring Along a Path

**Track:** Multivariable Calculus from First Principles. **Background:** derivatives of curves and one-variable integration. **Question:** how can a scalar field or vector field be integrated along a moving path?

<!-- BEGIN SPOKEN LECTURE -->

# Curves and Line Integrals: Measuring Along a Path

A path through the plane may bend, loop, or retrace itself. Its length is not simply the change in its endpoints. If a particle moves in a circle and returns to its starting point, its net displacement is zero, but it has traveled a nonzero distance. Calculus distinguishes these quantities by studying a parametrized curve.

Let a smooth curve be given by a position vector r of t, with t ranging over an interval. Its derivative r prime is the velocity vector. Over a short time interval delta t, the path travels approximately the speed, which is the length of the velocity vector, multiplied by delta t. Add these small distances and let the time intervals shrink. We obtain the arc-length integral: integrate the speed over the parameter interval.

## Arc length around a circle

Take the quarter circle starting at one comma zero and ending at zero comma one. Parametrize it as cosine t comma sine t, with t from zero to pi over two. The velocity is minus sine t comma cosine t. Its length is one. Integrating the constant speed one over that time interval gives arc length pi over two. The result agrees with one quarter of the circumference of a unit circle.

If we make the particle travel the same curve twice as fast, its velocity doubles while its time interval halves. The computed length stays the same. Arc length does not depend on the choice of smooth regular parametrization, as long as the path's traversal and multiplicity are preserved.

## Integrating a scalar along the curve

Now imagine a thin wire lying along that quarter circle, with linear density equal to x plus y. The mass of a small segment is approximately its density times its small length. The total mass is the line integral of x plus y with respect to arc length.

On the quarter circle, the density becomes cosine t plus sine t, and the speed is one. Integrate from zero to pi over two. The integral of cosine is one; the integral of sine is also one. The mass is two in the chosen units.

For a scalar line integral, reversing the traversal direction does not change the result. The arc-length factor is nonnegative. Traversing the entire curve twice, however, doubles the result because we have counted the wire twice. If we mean the geometric set rather than the path with multiplicity, we must parametrize it accordingly.

## Integrating a vector field along the curve

A vector field assigns a vector, such as force, to each point. To calculate the work done along a moving path, take the dot product of force with the infinitesimal displacement. In a parametrization, that becomes the vector field evaluated along the curve dotted with velocity, integrated over time. Unlike scalar arc-length integration, this line integral depends on orientation.

Take a force field F of x comma y equal to y comma x. This field is the gradient of the scalar potential x times y. The work done along any smooth path from one comma zero to zero comma one is the final potential minus the initial potential. Both endpoint products are zero, so the total work is zero. The force may do positive work on one part of a path and negative work on another; only the net difference remains.

This is the fundamental theorem for line integrals. Whenever F is the gradient of a differentiable potential on the region containing the path, integration along the path becomes an endpoint calculation. In particular, the integral around every closed loop is zero.

## A field with nonzero circulation

Now choose F of x comma y equal to minus y comma x. Along the unit circle parametrized counterclockwise, the field equals the velocity vector. Their dot product is one, and integrating over a full turn gives two pi. The field continually pushes in the direction of motion, so its circulation is positive.

Reverse the direction of travel, and the work becomes negative two pi. The geometric circle has not changed, but the oriented path has. This reversal is central to the boundary integrals in Green's and Stokes' theorems.

A subtler example is a field that points around circles but decays like inverse radius. Away from the origin it can have zero local curl yet nonzero circulation around a loop enclosing the missing origin. That example explains why local derivative conditions alone may not guarantee a globally defined potential when the domain has holes.

## What a line integral is really measuring

Scalar integration with respect to arc length accumulates density along a geometric path. Vector-field work integration accumulates the component of the field along oriented motion. Their formulas look similar only because both use a curve parametrization. In one the speed appears as a nonnegative length; in the other the full velocity, including its direction, appears in a dot product.

These two integrals bridge elementary calculus and differential geometry. The work integral is naturally the integral of a differential one-form along a curve. The scalar line integral relies on a metric to measure arc length. Distinguishing them now will make the more abstract language later feel necessary rather than arbitrary.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a piecewise \(C^1\) curve \(r:[a,b]\to\mathbb R^n\),
\[
L(r)=\int_a^b\|r'(t)\|\,dt,\qquad
\int_r f\,ds=\int_a^bf(r(t))\|r'(t)\|\,dt,
\]
while work or circulation is
\[
\int_r F\cdot dr=\int_a^bF(r(t))\cdot r'(t)\,dt.
\]
For \(r(t)=(\cos t,\sin t)\), \(0\le t\le\pi/2\), the length is \(\pi/2\) and \(\int_r(x+y)\,ds=2\). For \(F=\nabla(xy)=(y,x)\), \(\int_rF\cdot dr=xy\big|_{\mathrm{end}}-xy\big|_{\mathrm{start}}=0\). For \(F=(-y,x)\) and the full positively oriented unit circle, circulation is \(2\pi\).

### Exercises with answers

1. Find the length of \(r(t)=(3t,4t)\), \(0\le t\le2\). **Answer:** \(\int_0^2 5\,dt=10\).
2. Integrate density \(f=2\) along a segment of length three. **Answer:** six.
3. Compute work for \(F=(2x,2y)\) along any curve from \((0,0)\) to \((1,1)\). **Answer:** two, the change in potential \(x^2+y^2\).
4. What happens to \(\int_rF\cdot dr\) when orientation reverses? **Answer:** it changes sign.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), parametrized curves and line integrals.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), line integrals.
- [Line integral](https://en.wikipedia.org/wiki/Line_integral); [Conservative vector field](https://en.wikipedia.org/wiki/Conservative_vector_field).
