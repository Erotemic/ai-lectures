# 014000 — Riemannian Metrics, Geodesics, and Intrinsic Curvature

**Track:** Topology and Geometry. **Background:** manifolds, tangent spaces, covariant derivatives, differential forms. **Central question:** how can people who live entirely within a curved space measure distance and curvature without looking outside it?

<!-- BEGIN SPOKEN LECTURE -->

# Riemannian Metrics, Geodesics, and Intrinsic Curvature

Imagine living on the surface of a sphere but having no access to the third dimension. You can draw curves, measure the lengths of small segments, and compare directions in the tangent plane. Could you determine that your world is curved? You can. The geometry of distances within a surface contains enough information to detect curvature, even without any external viewpoint.

Riemannian geometry formalizes this idea. A Riemannian metric measures lengths and angles on each tangent space. Its associated connection defines geodesics and parallel transport. Curvature measures how those geometric operations depart from Euclidean behavior.

## A metric is more than a distance formula

At each point of a smooth manifold, a Riemannian metric assigns an inner product to pairs of tangent vectors. The assignment varies smoothly from point to point and is positive definite. It therefore tells us the length of every infinitesimal tangent vector and the angle between two tangent directions.

To find the length of a smooth curve, we integrate the norm of its velocity vector along the curve. The distance between two points is the infimum of the lengths of piecewise smooth curves joining them. Under standard connectedness assumptions, this produces the metric-space distance associated with the Riemannian metric.

The same manifold can carry many different Riemannian metrics. Topology specifies what it means for points and neighborhoods to fit together; a metric adds quantitative geometry. A flat plane can be stretched differently in different directions while retaining its topological identity.

## Coordinates are not the geometry

In local coordinates, the metric is represented by a symmetric positive-definite matrix of functions, often written g with indices i and j. A velocity vector with coordinate components v has squared length given by the quadratic form built from that matrix.

For the ordinary Euclidean plane, Cartesian coordinates give the diagonal metric matrix with ones on the diagonal. But switch to polar coordinates. The squared length of a small displacement is dr squared plus r squared times d theta squared. The metric coefficients now vary with position.

That variation does not mean the plane has acquired curvature. We changed coordinates, not the underlying geometry. Curvature must be expressed in a way that is unchanged by legitimate coordinate transformations.

This is an early test for every geometric formula. A coefficient can be nonzero because of coordinate choice alone. A genuine invariant cannot depend on that choice.

## The Levi-Civita connection

In the previous lecture we introduced connections on vector bundles. A Riemannian metric singles out a particularly important connection on the tangent bundle. The Levi-Civita connection is characterized by two requirements: it preserves the metric under parallel transport, and it has no torsion.

Metric compatibility says that when two vectors are transported in parallel along a curve, their inner product remains constant. Torsion-freeness says the difference between differentiating vector fields in opposite orders is governed exactly by their Lie bracket. These conditions determine one and only one connection.

In local coordinates its coefficients are called Christoffel symbols. They can be calculated from the metric coefficients and their first derivatives. Christoffel symbols are not themselves tensor components, and they can be nonzero even in flat space: polar coordinates in the Euclidean plane provide an example.

## Geodesics: straightness defined internally

A geodesic is a curve whose velocity vector remains parallel along the curve, according to the Levi-Civita connection. Its covariant acceleration is zero. This is the intrinsic replacement for the Euclidean condition that a straight line has zero ordinary acceleration.

In coordinates, the geodesic equation is a coupled system of second-order differential equations. The ordinary second derivative of each coordinate is corrected by terms involving the Christoffel symbols and products of velocity components.

On the Euclidean plane in Cartesian coordinates, all Christoffel symbols vanish, and the equations reduce to constant velocity. On a sphere with its standard round metric, geodesics are great circles, traversed at constant speed. A great circle need not look straight in three-dimensional space, but its acceleration as a curve in the ambient space points normally to the sphere. Its *tangential* acceleration vanishes.

Here is an important qualification. A geodesic is locally length-minimizing over sufficiently short segments, but not necessarily globally shortest between any two of its points. On a sphere, a segment of a great circle longer than half the circumference continues to be geodesic while no longer giving the shortest route between its endpoints.

## Curvature from parallel transport

Curvature measures what happens when covariant derivatives fail to commute. For the Levi-Civita connection, this produces the Riemann curvature tensor. In two dimensions, all its essential information at a point is summarized by one scalar, the Gaussian curvature.

A round sphere of radius R has Gaussian curvature one divided by R squared. The ordinary Euclidean plane has curvature zero. A cylinder has curvature zero as a surface in its intrinsic geometry, despite its visibly bent appearance in three-dimensional space. Small patches of a cylinder can be unrolled onto a plane without changing their lengths.

Why does the sphere differ from the cylinder? A sphere cannot be flattened onto a plane without distortion, even locally. One way to detect this is by measuring geodesic triangles: their angles on a positively curved surface can sum to more than a straight angle, whereas Euclidean triangles sum to exactly a straight angle. For sufficiently small geodesic triangles, the angular excess relates to the curvature integrated over the enclosed region.

## Gauss's Theorema Egregium

Historically, Carl Friedrich Gauss established that the Gaussian curvature of a regular surface is intrinsic. Although curvature can first be defined using how a surface bends in three-dimensional space, Gauss showed that it can be computed from the metric and its derivatives alone.

This was called the Theorema Egregium. It says that no local isometry can map a patch of the round sphere onto a patch of the Euclidean plane, because local isometries preserve Gaussian curvature. Conversely, the cylinder and plane have the same intrinsic curvature, even though they are embedded differently.

In higher dimensions, a single number no longer captures all directional curvature. Sectional curvature assigns curvature to a two-dimensional plane within a tangent space, and the full Riemann curvature tensor combines this information. It governs geodesic deviation, the way nearby freely traveling paths converge or diverge.

## Completeness and the global existence of geodesics

There is a final connection to differential equations. A geodesic is a solution of an ordinary differential equation on a manifold. Local existence and uniqueness follow under smoothness assumptions. But can the solution be continued for all time?

For a connected Riemannian manifold, the Hopf–Rinow theorem links several forms of completeness. Completeness as a metric space is equivalent to geodesic completeness: every geodesic with initial data extends for all real parameter time. In this setting any two points can also be joined by a minimizing geodesic. Without completeness these conclusions may fail. The open unit disk with the Euclidean metric is an example: a straight line can reach the missing boundary in finite time.

Riemannian geometry therefore links the local and the global. The metric gives infinitesimal lengths. The Levi-Civita connection gives a rule for straight motion. Curvature detects the non-Euclidean geometry seen by local measurements. Completeness determines whether local geodesic motion can continue indefinitely. All of it is intrinsic to the space and its chosen metric.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A Riemannian metric \(g\) on a smooth manifold \(M\) is a smoothly varying positive-definite symmetric bilinear form on \(T_pM\). In coordinates,
\[ds^2=\sum_{i,j}g_{ij}(x)\,dx^i dx^j,\qquad L(\gamma)=\int\sqrt{g_{\gamma(t)}(\dot\gamma(t),\dot\gamma(t))}\,dt.\]
The Levi-Civita connection is uniquely characterized by \(\nabla g=0\) and zero torsion. Its symbols are
\[\Gamma^k_{ij}=\tfrac12g^{k\ell}(\partial_i g_{j\ell}+\partial_jg_{i\ell}-\partial_\ell g_{ij}),\]
and affine-parameter geodesics satisfy
\[\ddot x^k+\Gamma^k_{ij}\dot x^i\dot x^j=0.\]
For the Euclidean plane in polar coordinates \(g=dr^2+r^2d\theta^2\), the nonzero symbols (away from \(r=0\)) are \(\Gamma^r_{\theta\theta}=-r\), \(\Gamma^\theta_{r\theta}=\Gamma^\theta_{\theta r}=1/r\), while Gaussian curvature is still \(0\). For a round sphere of radius \(R\), \(K=1/R^2\). A cylinder has \(K=0\) despite nonzero extrinsic bending.

The Riemann curvature operator (one common convention) is \(R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z\). Under a local isometry, the Riemann tensor and sectional curvature are preserved; Gauss's Theorema Egregium is the surface case. On connected Riemannian manifolds, the Hopf–Rinow theorem relates metric completeness to geodesic completeness and existence of minimizing geodesics between points.

### Exercises with answers

1. Does nonzero Christoffel symbol imply nonzero curvature? **No:** polar coordinates on the Euclidean plane have nonzero symbols but zero Gaussian curvature.
2. Are all geodesic segments globally minimizing? **No:** a great-circle arc longer than half the circumference is a counterexample.
3. Can the round sphere be flattened locally onto the plane by an isometry? **No:** their Gaussian curvatures differ.
4. Is the Euclidean open disk a complete Riemannian manifold? **No:** a straight geodesic reaches its missing boundary in finite affine time.

### Reading and source notes

- Sucharit Sarkar, [UCLA Differential Geometry Lecture 24: Gauss's Theorema Egregium](https://math.ucla.edu/~sucharit/120A-notes.html), intrinsic computation of Gaussian curvature.
- [University of Colorado lecture on the Theorema Egregium and geodesic spreading](https://math.colorado.edu/~sbc21/teaching/26fall/4230/lecture_notes/).
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), metrics, geodesics, connections and curvature.
