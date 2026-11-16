# 017000 — Surface Integrals: Area, Normal Vectors, and Flux

**Track:** Multivariable Calculus from First Principles. **Background:** cross products, double integrals, Jacobians. **Question:** how can we measure a curved surface and the field passing through it?

<!-- BEGIN SPOKEN LECTURE -->

# Surface Integrals: Area, Normal Vectors, and Flux

A curved roof occupies area even when viewed from above as a flat floor plan. If we want enough material to cover it, the projected area is not enough. If we want to calculate how much air crosses it, we also need its orientation. Surface integrals solve both problems by describing the surface through two parameters and measuring how a small patch changes under that parametrization.

A curve uses one parameter. A surface patch uses two. Think of a flexible sheet marked with grid coordinates u and v. Its location in three-dimensional space is a vector-valued map r of u comma v. Hold v fixed and vary u: this traces one family of curves on the surface. Hold u fixed and vary v: this traces another. Their velocity vectors r sub u and r sub v are tangent to the surface.

## From a coordinate patch to an area element

A tiny rectangle in the u-v grid, with side lengths delta u and delta v, becomes approximately a parallelogram in space. Its sides are r sub u times delta u and r sub v times delta v. The parallelogram's area is the length of the cross product of those sides. Thus the surface-area element is the length of r sub u cross r sub v times d u d v.

The cross product itself is perpendicular to the tangent plane. Its magnitude gives area scale, while its direction gives an orientation. Dividing by its magnitude gives a unit normal wherever the parametrization is regular. If we reverse the order of the parameters, the cross product changes sign, so orientation reverses even though area is unchanged.

This is the surface analogue of the Jacobian determinant for ordinary change of variables. A two-dimensional patch in a three-dimensional ambient space has two tangent directions, not a square three-by-three Jacobian. The cross-product magnitude is the correct area scale.

## A graph that curves upward

Consider the surface z equals x squared plus y squared above the unit disk in the x-y plane. Use x and y themselves as parameters. The position map is r of x comma y equals x comma y comma x squared plus y squared. Its x tangent vector is one comma zero comma two x. Its y tangent vector is zero comma one comma two y. Their cross product is minus two x comma minus two y comma one.

Its length is the square root of one plus four x squared plus four y squared. Therefore the curved surface area is the double integral of this square root over the unit disk. Polar coordinates reduce the calculation to a radial integral: two pi times the integral from zero to one of r times square root of one plus four r squared.

Substitute one plus four r squared as a new variable. The resulting area is pi divided by six times five to the three halves minus one. This is greater than pi, the area of the flat unit disk, as it should be: a sloping surface has more area than its horizontal projection.

It is worth checking units and limiting behavior. If the surface were flattened to z equals zero, the tangent cross-product length would be one everywhere, and the surface area would return to pi. The extra square-root factor is exactly the correction for slope.

## Scalar surface integrals

Suppose a thin coating on this curved surface has density sigma in kilograms per square meter of actual surface. Its mass is the integral of sigma times the surface area element. If sigma is constant, we multiply the computed area by that constant. If sigma varies with position, evaluate it at the points of the surface before integrating.

Like a scalar line integral, a scalar surface integral does not depend on the chosen orientation. Density is accumulated with a nonnegative area element. Care is still required to avoid counting overlapping parametrized patches twice.

## Flux needs a direction

Now imagine a constant upward flow F equal to the vector zero comma zero comma one. Its flux through the upward-oriented curved surface is the integral of F dotted with the oriented area vector r sub x cross r sub y. The dot product is one at every point. So the upward flux is simply the area of the unit disk, pi.

This does not contradict the fact that the curved surface has area greater than pi. On a steeper patch, the surface area increases, but the upward flow crosses that patch at a more oblique angle. The cosine factor from the dot product cancels the slope correction. Only the horizontal projected area remains for a uniform vertical field.

Reversing the surface normal reverses the flux. The physical flow has not changed, but we have reversed the direction we call positive. Flux measures signed crossing, not the total amount of fluid touching a surface.

## Closed surfaces and outward normals

For a closed surface such as a sphere, outward orientation is customary. At each regular point, the unit normal points away from the enclosed solid. A field may flow outward through one part and inward through another. The total flux adds these with opposite signs.

If a surface consists of several patches, their orientations must be consistent on overlaps. On an oriented closed surface, the outward normals can be chosen continuously. On a nonorientable surface, a global continuous normal may not exist. This is one reason orientation becomes a structural property rather than just an arrow drawn in a diagram.

## Where this leads

The same surface can carry two kinds of integrals. A scalar surface integral measures density weighted by actual area. A flux integral measures a vector field's normal component weighted by oriented area. Their difference mirrors the earlier distinction between scalar arc-length integrals and oriented work integrals along curves.

We now have enough machinery to see Stokes' theorem as a relation between circulation around a surface boundary and curl through the surface. And we can see the divergence theorem as a relation between outward flux through a closed surface and local net outflow inside the solid. Surface parametrization turns those statements into quantities we can calculate, not merely names to recognize.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a regular parametrization \(r:U\subset\mathbb R^2\to\mathbb R^3\),
\[
dS=\|r_u\times r_v\|\,du\,dv,\qquad
\int_S\sigma\,dS=\iint_U\sigma(r(u,v))\|r_u\times r_v\|\,du\,dv,
\]
and oriented flux is
\[
\int_SF\cdot n\,dS=\iint_UF(r(u,v))\cdot(r_u\times r_v)\,du\,dv.
\]
For the graph \(r(x,y)=(x,y,x^2+y^2)\),
\[
r_x\times r_y=(-2x,-2y,1),\quad
\operatorname{Area}(S)=2\pi\int_0^1 r\sqrt{1+4r^2}\,dr=\frac{\pi}{6}(5^{3/2}-1).
\]
The upward flux of \(F=(0,0,1)\) is \(\int_D1\,dx\,dy=\pi\).

### Exercises with answers

1. Find the area factor for the plane \(r(u,v)=(u,v,2u)\). **Answer:** \(\|r_u\times r_v\|=\sqrt5\).
2. Find the upward flux of \(F=(0,0,3)\) through \(z=x^2+y^2\) over the unit disk. **Answer:** \(3\pi\).
3. Does reversing a surface orientation change \(\int_S\sigma\,dS\)? **Answer:** no; scalar area is nonnegative.
4. Does reversing orientation change vector-field flux? **Answer:** yes, it reverses the sign.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), surface integrals.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), surface area and flux.
- [Surface integral](https://en.wikipedia.org/wiki/Surface_integral); [Normal (geometry)](https://en.wikipedia.org/wiki/Normal_(geometry)).
