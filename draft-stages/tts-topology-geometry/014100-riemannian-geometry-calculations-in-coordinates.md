# 014100 — Riemannian Geometry by Calculation: Metric, Connection, and Geodesics

**Track:** Topology and Geometry. **Background:** derivatives of several variables, smooth coordinates, tangent vectors, and the meaning of a Riemannian metric. **Central question:** how can we calculate straight motion on a curved manifold without trusting a picture of its embedding?

<!-- BEGIN SPOKEN LECTURE -->

# Riemannian Geometry by Calculation: Metric, Connection, and Geodesics

A person walking on a sphere can describe their motion with latitude and longitude. But those coordinates do not measure equal distances: one degree of longitude is a much shorter walk near a pole than near the equator. That basic observation is the starting point of Riemannian geometry. The coordinate grid is a description. The metric tells us which displacements represent the same physical length.

Our goal is practical. We will take a metric, compute the correction terms needed to differentiate a moving vector, and use them to decide whether a path is a geodesic. We will compare the flat plane and a round sphere. The comparison matters because many advanced geometric theories use these calculations but seldom pause to carry them through.

## Begin with a moving ruler

In Cartesian coordinates on the plane, a small displacement has horizontal and vertical components. Its squared length is the sum of their squares. In polar coordinates we describe the same displacement by a radial change and an angular change. One unit of radial movement always has length one. A small angular change has length approximately the radius times the size of that change. Thus the metric says: squared length equals radial change squared, plus radius squared times angular change squared.

This formula is not a new geometry. It is the same plane expressed in different coordinates. In particular, a varying metric coefficient is not proof that a space is curved. Curvature is something the observer can measure even after changing their coordinates.

A general Riemannian metric supplies such a positive-definite quadratic form at every point. We may picture it as an infinitesimal ruler: feed it a tangent direction and it reports the square of the length. Feed it two directions and it reports their inner product. Integrating the infinitesimal speed of a curve gives the curve's length.

## Why ordinary derivatives of vector components fail

Imagine carrying an arrow while moving around the origin in the plane. If the arrow keeps pointing in one fixed Cartesian direction, it is not turning. But its components in the rotating polar basis change, because the radial and angular basis vectors themselves rotate. Simply differentiating the two component numbers would report a change even when the arrow has not turned at all.

A connection fixes that problem. A covariant derivative differentiates both the vector components and the moving coordinate basis. The extra correction coefficients are called Christoffel symbols. They describe how the basis changes, not necessarily how the underlying space bends.

For a metric there is a distinguished choice of connection. The Levi-Civita connection keeps inner products constant under parallel transport and has zero torsion. Those two requirements determine the connection uniquely. That makes the correction coefficients calculable from the metric, instead of introducing them as independent unknowns.

## A complete example in polar coordinates

Take the plane, remove the origin so polar coordinates are well-defined, and use its ordinary Euclidean metric. The Christoffel symbols with an angular-angular input produce an inward radial correction proportional to the radius. The symbols coupling radial and angular directions produce a correction inversely proportional to the radius.

Let us see what those statements mean for a path of constant radius. A person moving around a circle may keep the radius fixed while their angular coordinate changes uniformly. Their ordinary radial coordinate has zero second derivative. But the covariant radial acceleration does not vanish. Its correction points inward. That circle is not a geodesic of the Euclidean plane: the person has to keep turning.

Now consider a radial ray, with angular coordinate constant and radial coordinate changing at constant speed. In the geodesic equation, all the angular velocity terms vanish. The remaining equation simply says the radial speed is constant. A radial ray is a geodesic, as expected.

We have obtained a familiar fact using symbols that were nonzero throughout the calculation. This is why Christoffel symbols and curvature must not be confused. They play different roles.

## Now change the space, not just the coordinates

Consider a round sphere of radius R. Use the polar angle measured down from the north pole and an azimuthal angle around the axis. A small change in polar angle has length R times that change. A small azimuthal change has length R times the sine of the polar angle, times the azimuthal change. At the poles, changing longitude has no first-order physical effect. At the equator, it has the greatest effect.

The metric now has an angular coefficient that shrinks near the poles. As before, we can compute a Levi-Civita connection from the coefficient and its derivatives. One correction involves minus sine times cosine of the polar angle. Another involves the ratio of cosine to sine. The formulas are singular at the poles because the longitude coordinate becomes singular there; the sphere itself is smooth.

Which circles of latitude are geodesics? Set the polar angle constant and let the azimuthal angle advance. The polar component of the geodesic equation contains a sine-times-cosine factor. Away from the poles, this vanishes at the equator. The equator is a geodesic. An ordinary line of latitude farther north is not. To follow it, a traveler must continually turn relative to intrinsic straight motion.

Great circles are all geodesics. We used one particular coordinate grid to verify the equator, but rotating the sphere carries that example to any great circle and preserves the metric.

## Speed and parameter choice

There are two easily confused ideas: a geodesic as an unparameterized route and a geodesic traversed at a particular rate. The equation with zero covariant acceleration assumes an affine parameter, often arc length or a constant multiple of arc length. If we speed up and slow down while following the same great circle, the trace remains a geodesic path, but the new parameter may not satisfy the same equation.

The distinction matters in mechanics and numerical work. When a simulation produces an apparent extra force along the direction of motion, check whether it is a genuine departure from geodesic motion or an artifact of how time was parameterized.

## What this gives us

We can now read a metric as a local ruler, derive a connection that respects that ruler, and solve for paths whose covariant acceleration vanishes. We also know two checks on our work. First, coordinate singularities are not necessarily geometric singularities. Second, nonzero Christoffel symbols are not evidence of nonzero curvature.

These ideas prepare the ground for geodesic deviation, in which we compare two neighboring geodesics. That comparison finally reveals a property of the geometry that no coordinate change can remove.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On a smooth manifold, a metric has coordinate expression \(g=g_{ij}(x)dx^i\otimes dx^j\) with positive-definite matrix \((g_{ij})\). Length of \(\gamma\) is \(L(\gamma)=\int\sqrt{g_{ij}(\gamma)\dot\gamma^i\dot\gamma^j}\,dt\). The Levi-Civita symbols satisfy
\[\Gamma^k{}_{ij}=\tfrac12 g^{k\ell}(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}),\qquad \ddot x^k+\Gamma^k{}_{ij}\dot x^i\dot x^j=0.\]
For the flat punctured plane, \(ds^2=dr^2+r^2d\theta^2\): \(\Gamma^r{}_{\theta\theta}=-r\) and \(\Gamma^\theta{}_{r\theta}=\Gamma^\theta{}_{\theta r}=1/r\). A circle \(r=r_0\), \(\dot\theta\ne0\), violates the radial geodesic equation \(\ddot r-r\dot\theta^2=0\). Despite the nonzero connection coefficients, \(R=0\).

On the round sphere away from the coordinate poles, \(g=R^2(d\vartheta^2+\sin^2\vartheta\,d\varphi^2)\), \(\Gamma^\vartheta{}_{\varphi\varphi}=-\sin\vartheta\cos\vartheta\), and \(\Gamma^\varphi{}_{\vartheta\varphi}=\Gamma^\varphi{}_{\varphi\vartheta}=\cot\vartheta\). Constant \(\vartheta\) and nonzero constant \(\dot\varphi\) solves the polar geodesic equation only at \(\vartheta=\pi/2\); coordinate poles cannot be tested with this chart.

### Exercises with answers

1. **Flat coordinates.** On the polar plane, is \(r=2,\theta=t\) a geodesic? **Answer:** No: its radial covariant acceleration is \(-2\), although \(\ddot r=0\).
2. **Radial motion.** Test \(r(t)=3+t,\theta(t)=\theta_0\). **Answer:** It satisfies the geodesic equations on any interval where \(r>0\).
3. **Sphere.** Why does a non-equatorial latitude circle fail? **Answer:** The polar equation includes \(-\sin\vartheta\cos\vartheta\,\dot\varphi^2\), which is nonzero away from the poles and equator.
4. **Interpretation.** Does \(\cot\vartheta\) becoming infinite near a pole imply infinite intrinsic curvature? **Answer:** No. Longitude coordinates degenerate there; the round sphere has finite constant Gaussian curvature \(1/R^2\).

### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds: lecture notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- MIT OpenCourseWare, [18.950 Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/).
- Background overview: [Christoffel symbols](https://en.wikipedia.org/wiki/Christoffel_symbols), [Levi-Civita connection](https://en.wikipedia.org/wiki/Levi-Civita_connection).
