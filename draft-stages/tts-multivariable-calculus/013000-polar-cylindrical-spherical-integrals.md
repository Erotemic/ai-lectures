# 013000 — Polar, Cylindrical, and Spherical Integrals: Coordinates Built for Shape

**Track:** Multivariable Calculus from First Principles. **Background:** double and triple integrals, trigonometry. **Question:** why does polar area contain a factor of radius?

<!-- BEGIN SPOKEN LECTURE -->

# Polar, Cylindrical, and Spherical Integrals: Coordinates Built for Shape

A disk is difficult to describe using horizontal and vertical bounds. Its boundary involves square roots, and a rectangular grid cuts many pieces across the edge. But in polar coordinates the same disk is described by two simple statements: the radius runs from zero to one, and the angle makes one complete turn. This simplification is worth making only if we correctly transform the area element.

Suppose the location of a point in the plane is given by its radius r and its angle theta. The Cartesian coordinates are x equals r cosine theta and y equals r sine theta. Each small change in r moves outward. Each small change in theta moves around a circle. A small angular change of size delta theta creates an arc of length approximately r times delta theta. Multiply that by a small radial thickness delta r, and the resulting thin wedge has area approximately r times delta r times delta theta.

This is why the polar area element is r times d r times d theta. It is not simply d r times d theta. Near the center, an angular interval covers almost no area; far from the center, the same angular interval sweeps a wider strip. The factor r corrects for that changing scale.

## Integrate a radial function on a disk

Consider the function x squared plus y squared over the unit disk. In polar coordinates the function is r squared. The disk is zero at most r at most one, zero at most theta at most two pi. The integral is therefore the integral of r squared times the area factor r. Integrate r cubed from zero to one to obtain one quarter, then multiply by two pi. The answer is pi over two.

We can check its meaning: the disk has area pi, and its average squared distance from the origin is one half. Points near the rim have larger squared radius than points near the center, but there is more area near the rim. The result reflects both facts.

If we had forgotten the r factor, we would have computed two pi over three, a different value with no valid geometric justification. Most early errors in polar integration are errors about area scaling rather than about antiderivatives.

## Cylindrical coordinates

In three dimensions, cylindrical coordinates keep the polar description in the horizontal plane and add height z. We write x equals r cosine theta, y equals r sine theta, and z stays z. The volume element is r times d r times d theta times d z. A cylinder of radius two and height three can be described by r between zero and two, theta over a full turn, and z between zero and three. Integrating one over that region gives twelve pi, exactly base area four pi times height three.

Cylindrical coordinates are useful for pipes, rotating shafts, radial heat distributions, and any problem with symmetry around an axis. They separate the angular variable from the vertical one without forcing the geometry into rectangular bounds.

## Spherical coordinates

For a solid ball, even cylindrical coordinates can require a square-root height bound. Spherical coordinates use distance rho from the origin, polar angle phi measured down from the positive z axis, and azimuth theta measured around that axis. A point has x equal to rho sine phi cosine theta, y equal to rho sine phi sine theta, and z equal to rho cosine phi.

A small radial displacement contributes one length factor. A small polar-angle displacement travels approximately rho times delta phi. A small azimuthal displacement travels around a circle of radius rho sine phi, contributing rho sine phi times delta theta. Multiply the three small lengths and we obtain the volume factor rho squared times sine phi.

The unit ball is described by rho between zero and one, phi between zero and pi, and theta from zero to two pi. Integrating one with the spherical volume factor gives one third from the radial integral, two from the polar-angle integral, and two pi from azimuth. The product is four pi over three, the usual unit-ball volume.

## Coordinate singularities are not physical singularities

At r equals zero, every polar angle names the same point. At the poles of spherical coordinates, the azimuth is similarly redundant. The coordinate maps lose local invertibility there, and the scale factor vanishes. This does not mean the disk or ball is singular. It means our chosen coordinates are redundant at those locations.

These singular sets have zero area or volume in the usual integrals, and the change-of-variables formula can be applied away from them, then extended across them for integrable functions. In more delicate settings, singular behavior of the integrand still requires analysis; a vanishing Jacobian factor does not automatically remove an actual divergence.

## Choose coordinates for the mathematics, not for tradition

When the region and integrand depend mostly on distance from an axis, cylindrical coordinates may reduce a triple integral to a one-variable calculation. When they depend on distance from the origin, spherical coordinates can do the same. For a rectangular box, Cartesian coordinates are usually simpler.

The lesson is not to memorize three unrelated volume elements. Each is a consequence of the same geometric principle: a small coordinate box is transformed into a tiny physical parallelepiped, and its volume is scaled by the Jacobian determinant. The general change-of-variables theorem formalizes that picture.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Polar: \((x,y)=(r\cos\theta,r\sin\theta)\), \(dA=r\,dr\,d\theta\) for \(r\ge0\). Cylindrical: \((x,y,z)=(r\cos\theta,r\sin\theta,z)\), \(dV=r\,dr\,d\theta\,dz\). Spherical (\(\phi\) measured from +z):
\[
(x,y,z)=(\rho\sin\phi\cos\theta,\rho\sin\phi\sin\theta,\rho\cos\phi),
\quad dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.
\]
For \(D=\{x^2+y^2\le1\}\),
\[
\iint_D(x^2+y^2)\,dA
=\int_0^{2\pi}\int_0^1r^3\,dr\,d\theta=\pi/2.
\]
For the unit ball,
\[
\iiint_{B^3}1\,dV=\int_0^{2\pi}\int_0^\pi\int_0^1\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=4\pi/3.
\]
Coordinate maps fail to be one-to-one on edges of a full angular interval and at the coordinate axes; restrict to domains where the map is injective in applying the general theorem, ignoring boundaries of zero measure when justified.

### Exercises with answers

1. Find the area of a disk of radius \(R\) in polar coordinates. **Answer:** \(\int_0^{2\pi}\int_0^Rr\,dr\,d\theta=\pi R^2\).
2. Find the volume of a cylinder of radius two and height three. **Answer:** \(12\pi\).
3. Compute \(\int_{x^2+y^2\le1}1/(1+x^2+y^2)\,dA\). **Answer:** \(2\pi\int_0^1r/(1+r^2)dr=\pi\log2\).
4. Why is the spherical factor \(\rho^2\sin\phi\) rather than \(\rho^2\) alone? **Answer:** the azimuthal circle has radius \(\rho\sin\phi\), which shrinks near the poles.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), coordinate systems and multiple integrals.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), polar and spherical substitutions.
- [Polar coordinate system](https://en.wikipedia.org/wiki/Polar_coordinate_system); [Spherical coordinate system](https://en.wikipedia.org/wiki/Spherical_coordinate_system).
