# The Ruler That Stays on the Surface: Metrics, Distance, and Geodesics

**Track:** Topology and Geometry  
**Lecture:** 052000  
**Preparation:** Regular surface patches, dot products, partial derivatives, and elementary integration.  
**Companion:** First fundamental forms, area elements, the energy variation, and model geodesics.

<!-- BEGIN SPOKEN LECTURE -->

Imagine being handed two sheets of paper. One lies flat on a table. The other has been rolled into a cylinder, without stretching, tearing, or creasing. From the outside they look different. But an ant walking on either sheet, equipped with a ruler and a protractor, can make the same local measurements. A little triangle on the cylinder has the same side lengths and angles as the corresponding triangle on the flat sheet. The sheet has bent in space, yet its internal geometry has not changed.

Now imagine trying to wrap a flat sheet smoothly over an entire sphere. Wrinkles, cuts, or stretching appear. This is not merely a manufacturing inconvenience. It reflects a mathematical obstruction: the internal distances of a sphere are different from those of a plane.

We need a language that describes what the ant can measure, while remaining independent of where the surface happens to sit in three-dimensional space. That language is a metric on tangent vectors. Once we have it, lengths and areas become integrals, and a straight line becomes a geodesic.

## How a ruler appears in coordinates

Take a regular parametrized surface X of u and v. A small movement in parameter space has changes du and dv. Its first-order displacement on the actual surface is X sub u times du plus X sub v times dv. Square its ordinary Euclidean length. Three coefficients appear: the dot product of X sub u with itself, the dot product of X sub u with X sub v, and the dot product of X sub v with itself.

Traditionally these are called E, F, and G. The squared length is E times du squared, plus twice F times du times dv, plus G times dv squared. We can think of E and G as measuring the lengths of the coordinate direction vectors, while F measures how far those directions are from being perpendicular.

This expression is called the first fundamental form. Its matrix is the two-by-two symmetric matrix with E and G on the diagonal and F off the diagonal. Because the original surface patch is regular, the matrix is positive definite. E and G are positive, and E times G minus F squared is positive. Every nonzero tangent direction consequently has a positive squared length.

If we switch to different coordinates, the three coefficients change. But the squared length of the geometric tangent vector does not. The matrix transforms by multiplying with the coordinate-change Jacobian and its transpose. The metric is not the individual numbers E, F, and G; it is the consistently transforming inner product those numbers represent.

Let us use this on three surfaces. Each will reveal a different piece of the story.

## A cylinder is locally a plane

Parametrize a cylinder of radius R by an angle u around its axis and a height v. Its coordinates are R cosine u, R sine u, and v. Differentiate. In the angular direction we obtain negative R sine u, R cosine u, zero. In the vertical direction we obtain zero, zero, one. Those two vectors are perpendicular. Their lengths are R and one.

Therefore E equals R squared, F equals zero, and G equals one. The squared line element is R squared times du squared plus dv squared. Set x equal to R times u and y equal to v. In these new coordinates, the same metric becomes dx squared plus dy squared, exactly the ordinary Euclidean plane metric.

This is the mathematics of unrolling the cylinder. Its angular coordinate becomes horizontal distance along the flat sheet, and its vertical coordinate stays vertical. Local lengths and angles are unchanged. In particular, a locally straight path in the flattened coordinates corresponds to a geodesic on the cylinder. Depending on its slope, that path may become a horizontal circle, a vertical line, or a helix.

There is a global qualification. The cylinder's angle repeats after one full revolution. Two different horizontal positions separated by the circumference represent the same point on the cylinder. The unrolling is a local isometry, not a global one-to-one map between the complete cylinder and the plane. The cylinder and plane differ topologically even though their local intrinsic metrics are identical.

This is a useful warning about the word flat. A surface can have zero intrinsic curvature without being globally identical to the Euclidean plane. We will make that claim precise using curvature in the next lecture.

## A sphere has a different ruler

Now parametrize a sphere of radius R with colatitude theta measured from the north pole and longitude phi. In those coordinates, the first partial derivative has length R. The longitude derivative has length R sine theta, because the circle at fixed colatitude has radius R sine theta. These directions are perpendicular. So the metric is R squared times d theta squared plus R squared sine squared theta times d phi squared.

This compact expression explains several facts that a map projection tends to obscure. A one-radian longitude change near the equator travels a distance R, but the same longitude change near the north pole travels much less, because the circle of latitude is smaller. At the pole itself, changing longitude describes no movement. The vanishing longitude coefficient there reflects the failure of these coordinates, not a degeneracy of the sphere's actual tangent-plane metric.

A meridian from the north pole to the south pole has length pi R. The equator has circumference two pi R. A small latitude circle at colatitude theta has circumference two pi R sine theta. These are not separate facts to memorize. Each follows by inserting a particular path into the same line-length rule.

The metric also gives area. On a parameterized surface, the area of the small image of a parameter rectangle is the magnitude of X sub u cross X sub v times du dv. Squaring that cross-product magnitude gives E G minus F squared. Hence the area element is the square root of E G minus F squared, times du dv.

For the sphere this becomes R squared sine theta times d theta d phi. Integrate longitude from zero to two pi and colatitude from zero to pi. The result is four pi R squared. The same metric that measures a short walk also determines the entire sphere's surface area.

## A graph that stretches your ruler

For a third example, consider the upward-opening paraboloid z equals x squared plus y squared. Use x and y as parameters. Its tangent directions are one, zero, two x and zero, one, two y. Taking their dot products gives E equal to one plus four x squared, F equal to four x y, and G equal to one plus four y squared.

The area-density square root simplifies beautifully: E G minus F squared equals one plus four x squared plus four y squared. Near the vertex, the density is close to one, so a small horizontal square and its surface image have almost equal areas. Farther out, the tangent plane tilts more, and a fixed square in the horizontal parameter plane covers a larger patch of surface.

Notice what happened. We used x and y coordinates that look Euclidean, but the surface metric is not the identity matrix. If we had silently measured path lengths using the horizontal coordinate differences, we would have underestimated the distance climbed. Coordinates label points; the metric tells us how far apart nearby labeled points actually are.

## From tangent lengths to distance between points

A metric assigns an inner product to each tangent plane, changing smoothly from point to point. Given a curve on the surface, compute its velocity as a tangent vector, measure its length with the metric, and integrate that speed. This defines the length of the curve without referring to any external space. Even an abstract surface that has not been embedded in three dimensions can carry such a rule; it is then called a Riemannian surface.

To define distance between two points, look at all suitable piecewise smooth curves connecting them and take the infimum of their lengths. This distance respects the global shape as well as the local measuring rule. It need not equal the ordinary straight-line distance between the points in the surrounding space. On a sphere, the shortest surface route between nearby points lies along a short great-circle arc, not along the chord passing through the interior of the Earth.

The distinction between path length and the resulting distance is important. A path can be extremely long even when its endpoints are close. The distance is a best possible value, and finding it is an optimization problem.

## Why geodesics come from a variational problem

In the plane, the straight segment between fixed endpoints minimizes length. A tiny deformation of that segment, keeping the endpoints fixed, cannot decrease its length to first order. This stationarity gives us a way to generalize straightness when no global planar coordinates exist.

For a surface path q of t in local coordinates, its energy is one half the integral of the metric inner product of its velocity with itself. Unlike length, energy depends on the speed of parametrization. But among fixed-endpoint paths traversed in a fixed time interval, a length-minimizing path run at constant speed also minimizes energy. Cauchy--Schwarz explains this: the integral of speed squared is at least the square of the integral of speed, divided by the time interval, with equality at constant speed.

The energy is convenient because it has a smooth quadratic expression in the velocities. Apply the Euler--Lagrange equation from the calculus of variations. The resulting differential equation says that the covariant acceleration of the path is zero. A path satisfying this equation with an affine parameter is a geodesic.

In coordinates, this is the equation whose ordinary second derivative of each coordinate is corrected by a sum of Christoffel-symbol terms quadratic in the coordinate velocities. Those symbols are assembled from the metric and its first derivatives. They are not extra physical forces. They correct for the fact that the coordinate directions themselves may change as we move. Even on a flat plane, polar coordinates have nonzero Christoffel symbols. The symbols alone are not a test for curvature.

The geodesic equation tells us about straightest paths, but it does not automatically tell us about the globally shortest path between distant points. A long arc around a circle can be a geodesic in the appropriate surface even when a shorter arc reaches the same endpoint. Global minimization requires comparing candidates and accounting for topology.

## Geodesics on the cylinder and sphere

Return to the cylinder and unroll it locally. In the flat coordinates x equals R u and y equals v, the geodesic equation is simply that x and y have zero second derivatives. So x and y are affine functions of the parameter. Rolling this line back onto the cylinder produces a helix unless it runs purely around or along the axis. It is locally straight by the surface's own ruler, although it bends as a space curve.

For the sphere, a great circle is a geodesic. One way to see this is to travel around a great circle at constant speed. Its ordinary acceleration points toward the center of the sphere, perpendicular to the tangent plane. The tangential part of its acceleration is therefore zero, which is exactly the geodesic condition for a surface with the induced metric.

A circle of latitude other than the equator is generally not a geodesic. A traveler following it must continually turn within the tangent plane to maintain the same latitude. A small variation of the route can shorten the path locally. The equator is different: it is a great circle, and the required turning is entirely normal to the sphere, not within its tangent plane.

There is also a global surprise at antipodal points. From the north pole to the south pole, infinitely many meridian semicircles have the same minimal length pi R. Geodesics are not always unique, even when the metric is smooth and the endpoints are well defined. A short segment of one meridian is uniquely minimizing in an appropriate local neighborhood, but the antipodal pair sits at the boundary of that simple behavior.

## Carrying a direction around a surface

If we wish to compare a tangent vector at one point with a tangent vector at another, there is another problem: they belong to different tangent planes. On the cylinder, flattening the surface suggests how to carry a direction without turning it intrinsically. On a general surface, the Levi-Civita connection defines parallel transport, a way to move a tangent vector along a path while keeping its covariant derivative zero. For a surface in Euclidean space, the covariant derivative along a path is the tangential component of the ordinary derivative of a tangent vector field.

Parallel transport preserves lengths and angles. It does not generally return a vector to its original orientation after traveling around a closed loop. On the sphere, the amount of rotation can detect the curvature enclosed by the path. We have reached a remarkable point: a metric gives us a rule for measuring velocities, and differentiating that rule gives us a notion of turning and curvature that may be detected entirely within the surface.

Our flat sheet and cylindrical sheet had identical local rulers. The sphere did not. The differential-geometric question is now precise: what feature of a metric prevents us from finding coordinates that make it Euclidean throughout a whole neighborhood? The answer is intrinsic curvature, and its consequences connect small triangles to the topology of an entire surface.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### The induced metric and area density

For a regular patch \(X(u,v)\), put

\[
E=X_u\cdot X_u,\qquad F=X_u\cdot X_v,\qquad G=X_v\cdot X_v.
\]

Then

\[
ds^2=E\,du^2+2F\,du\,dv+G\,dv^2,\qquad
dA=\sqrt{EG-F^2}\,du\,dv.
\]

For \(q(t)=(u(t),v(t))\),

\[
L(q)=\int\sqrt{E\dot u^2+2F\dot u\dot v+G\dot v^2}\,dt,
\quad
\mathcal E(q)=\frac12\int g_{ij}(q)\dot q^i\dot q^j\,dt.
\]

### Explicit surfaces

- Cylinder \(X(u,v)=(R\cos u,R\sin u,v)\): \(ds^2=R^2du^2+dv^2\), locally Euclidean under \(x=Ru,y=v\).
- Sphere \(X(\theta,\phi)=(R\sin\theta\cos\phi,R\sin\theta\sin\phi,R\cos\theta)\):
\[ds^2=R^2d\theta^2+R^2\sin^2\theta\,d\phi^2.\]
- Paraboloid \(z=u^2+v^2\): \(E=1+4u^2\), \(F=4uv\), \(G=1+4v^2\), \(dA=\sqrt{1+4u^2+4v^2}\,du\,dv\).

### From energy variation to geodesics

For the Lagrangian \(L(q,\dot q)=\tfrac12 g_{ij}(q)\dot q^i\dot q^j\), fixed-endpoint variations produce

\[
\ddot q^k+\Gamma^k_{ij}(q)\dot q^i\dot q^j=0,
\quad
\Gamma^k_{ij}=\tfrac12 g^{k\ell}\bigl(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}\bigr).
\]

For the sphere with colatitude \(\theta\), longitude \(\phi\),

\[
\ddot\theta-\sin\theta\cos\theta\,\dot\phi^2=0,
\quad
\ddot\phi+2\cot\theta\,\dot\theta\dot\phi=0.
\]

A constant-latitude path \(\theta\equiv\theta_0\) with nonzero \(\dot\phi\) solves these equations away from the poles only if \(\cos\theta_0=0\), i.e. the equator.

### Exercises with answers

1. A cylinder of radius two has \(ds^2=4du^2+dv^2\). Find the length of one horizontal revolution. **Answer:** \(4\pi\).
2. Why is \(\sqrt{EG-F^2}\) strictly positive on a regular patch? **Answer:** It equals \(\|X_u\times X_v\|\), which is nonzero by regularity.
3. At colatitude \(\pi/6\), find the circumference of the sphere's latitude circle. **Answer:** \(2\pi R\sin(\pi/6)=\pi R\).
4. Why is a great-circle arc longer than a chord in Euclidean three-space? **Answer:** The chord may leave the surface, so it is not an allowed path for intrinsic surface distance.
5. Give a geodesic that is not globally length-minimizing between its endpoints. **Answer:** A sphere's great-circle arc longer than a semicircle between the same endpoints.

### Reading

- MIT OCW 18.950 Differential Geometry (`tg-mit-differential`).
- MIT OCW 18.965 Geometry of Manifolds (`tg-mit-manifolds`).
- For higher-level connection, metric, and Jacobi-field theory, `topology-geometry:014000`.
- Wikipedia overviews: [First fundamental form](https://en.wikipedia.org/wiki/First_fundamental_form) and [Geodesic](https://en.wikipedia.org/wiki/Geodesic).
