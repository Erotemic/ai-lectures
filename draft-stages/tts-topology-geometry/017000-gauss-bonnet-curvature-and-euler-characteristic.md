# 017000 — Gauss–Bonnet: Curvature Counts Topology

**Track:** Topology and Geometry. **Background:** Riemannian surfaces, tangent spaces, differential forms, Euler characteristic. **Central question:** why does adding curvature over an entire surface recover a topological invariant?

<!-- BEGIN SPOKEN LECTURE -->

# Gauss–Bonnet: Curvature Counts Topology

A sphere and a torus can both be made smooth, and both can be bent in space. A torus may have regions of positive and negative curvature, while a round sphere has positive curvature everywhere. These statements concern the shapes we see. Gauss–Bonnet goes further: when curvature is integrated across a compact closed oriented surface, the result is determined by its topology, not by the particular smooth metric used to measure it.

That is a remarkable claim. Curvature is local: it measures how the geometry behaves near a point. Topology is global: it records properties that survive continuous deformation. Gauss–Bonnet is an exact bridge between them.

## Curvature is not the same as bending in space

For a surface with a Riemannian metric, Gaussian curvature measures the intrinsic geometry of small patches. A sphere of radius R has Gaussian curvature equal to one divided by R squared. Its area is four pi R squared. Multiplying these gives four pi, independent of the radius.

Why does the radius disappear? Because enlarging the sphere reduces its curvature and increases its area in exactly compensating ways. The total curvature, unlike the pointwise curvature, remembers something stable.

A cylinder may look bent in three-dimensional space, but its intrinsic Gaussian curvature is zero. You can cut and unroll a cylinder into a flat sheet without stretching its metric locally. This illustrates why the theorem concerns intrinsic Gaussian curvature, not simply how much a surface appears to bend in a surrounding space.

## Triangles that refuse to have Euclidean angles

On a plane, the angles of an ordinary triangle sum to one hundred eighty degrees. On a sphere, geodesics are arcs of great circles, and geodesic triangles can have a larger angle sum.

Choose the north pole and two points on the equator separated by a quarter of the equator. Join them by shortest great-circle arcs. All three interior angles are right angles. Their sum is two hundred seventy degrees, an excess of ninety degrees. The triangle covers one eighth of the sphere. On the unit sphere its area is pi over two, exactly the angle excess measured in radians.

This is a local form of Gauss–Bonnet for a geodesic triangle: the integral of Gaussian curvature over the triangle equals the sum of its interior angles minus pi. On a flat surface the curvature integral vanishes and the Euclidean rule returns.

But what if the triangle's edges are not geodesics? Then the curve itself bends within the surface. We need a boundary term called geodesic curvature. It measures how a curve departs from being a geodesic, using the surface's own metric. At corners, we must also count the change in direction, described by exterior turning angles.

## The theorem with a boundary

For a compact oriented Riemannian surface with piecewise smooth boundary, the integral of Gaussian curvature over the surface, plus the integral of geodesic curvature along the positively oriented boundary, plus the sum of the exterior corner angles, equals two pi times the Euler characteristic of the surface.

The Euler characteristic can be computed from a triangulation: number of vertices minus number of edges plus number of faces. On a topological sphere it is two. On a torus it is zero. On an orientable closed surface with g handles, it is two minus twice g.

If the surface has no boundary, both boundary contributions vanish. Total Gaussian curvature is therefore two pi times Euler characteristic. For a sphere, that is four pi. For a torus, it is zero. For a double torus it is negative four pi. The exact total cannot be changed by stretching the metric, so long as we remain in the theorem's geometric setting.

A torus can have positively and negatively curved regions. Its total must balance to zero, but the theorem does not require its curvature to be zero at every point. A flat torus is possible as an abstract Riemannian manifold, even though a smooth isometric embedding as a standard torus in three-dimensional Euclidean space cannot have zero Gaussian curvature everywhere.

## Why triangulation makes topology appear

There is a proof strategy that lets us see where vertices, edges, and faces enter. Subdivide the surface into many small geodesic triangles. For each triangle, compare the sum of its angles with pi; the difference is its integrated curvature. Now add those identities over all triangles.

Every interior edge is shared, so the boundary effects on one side cancel those on the other. At an interior vertex, the angles around a smooth surface add to two pi. What remains is a count built from triangles, their edges, and their vertices. That count is the Euler characteristic. The formulas are geometric locally, but their global bookkeeping becomes combinatorial.

For a surface with boundary, the uncanceled edge turns and corner jumps produce exactly the geodesic-curvature and exterior-angle terms. The boundary formula is therefore not an optional amendment to the closed-surface formula. It is the form that makes the cancellation mechanism work when the surface has an edge.

Consider a flat circular disk of radius R. Gaussian curvature is zero. The geodesic curvature of its boundary circle is one divided by R, and the circumference is two pi R. The boundary integral is two pi. The disk has Euler characteristic one, so the theorem checks out. If we omitted the boundary term, we would obtain a false statement.

## Geometry puts limits on topology

Gauss–Bonnet can also rule out proposed metrics. If a compact closed oriented surface has Gaussian curvature strictly positive at every point, its total curvature is positive, so its Euler characteristic must be positive. Among connected closed orientable surfaces, this forces the topology of a sphere. If the curvature is everywhere negative, the Euler characteristic must be negative, ruling out the sphere and torus.

The converse statements require care. Knowing Euler characteristic is positive does not mean every metric on that surface is everywhere positively curved. Total curvature constrains the integral; it does not dictate the sign at every point.

This is an early example of a principle that recurs in global geometry: integrate local differential information, and topology emerges as a constraint on the result.

## A theorem about what cannot be changed

Curvature seems to describe the shape of a surface at an instant, and Euler characteristic seems to describe its topological identity. Gauss–Bonnet shows that they are connected by an exact equation. On a sphere, any smooth metric distributes a total of four pi units of Gaussian curvature, whatever the local peaks and valleys. On a torus, the signed total must cancel.

The theorem is both an analytic calculation and a counting argument. That combination—local differential geometry, boundary correction, and global topological invariant—is why Gauss–Bonnet remains a prototype for much more general index and characteristic-class theorems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let M be a compact oriented two-dimensional Riemannian manifold with piecewise smooth boundary \(\partial M\). With the induced positive boundary orientation, Gaussian curvature K, signed geodesic curvature \(k_g\), and signed exterior turns \(\theta_j\) at corners, **Gauss–Bonnet** is
\[\int_M K\,dA+\int_{\partial M} k_g\,ds+\sum_j\theta_j=2\pi\chi(M).\]
For a closed surface, \(\int_M K\,dA=2\pi\chi(M)\). A closed connected orientable genus-g surface has \(\chi(M)=2-2g\).

**Geodesic triangle:** with interior angles \(\alpha,\beta,\gamma\) and geodesic sides,
\[\int_T K\,dA=\alpha+\beta+\gamma-\pi.\]
**Sphere:** \(K=R^{-2}\), \(\operatorname{Area}(S_R^2)=4\pi R^2\), so \(\int K=4\pi=2\pi\chi(S^2)\). **Flat disk:** \(K=0\) and \(k_g=1/R\), so \(\int_{\partial D_R}k_g ds=2\pi\). **Torus:** \(\chi(T^2)=0\), so total signed curvature is zero for every smooth metric.

Proof outline for closed M: triangulate into geodesic triangles. Summing the geodesic triangle angle excesses, every interior vertex contributes \(2\pi\), while each triangle contributes \(-\pi\). With \(3F=2E\), \(2\pi V-\pi F=2\pi(V-E+F)\). The general proof handles nongeodesic edges and boundary terms by geodesic curvature.

### Exercises with answers

1. What is the total curvature of a genus-three closed orientable surface? **Answer:** \(2\pi(2-6)=-8\pi\).
2. Can a closed torus carry a metric of strictly positive Gaussian curvature? **Answer:** no; its total curvature must be zero.
3. Why is the planar disk not a counterexample to Gauss–Bonnet? **Answer:** the boundary geodesic-curvature integral contributes \(2\pi\).
4. What is the spherical angle excess of a unit-sphere octant geodesic triangle? **Answer:** \(\pi/2\), equal to its area.

### Reading and source notes

- [UCLA, Math 120A geometry notes](https://math.ucla.edu/~sucharit/120A-notes.html), geodesic triangles and the global result.
- [Notre Dame, Euler Characteristic and Gauss–Bonnet lecture](https://sites.nd.edu/2023cmndthematicprogram/files/2023/06/lecture4-Lehmann-updated.pdf), boundary terms and triangulation proof.
- [MIT OpenCourseWare, Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/), manifold and curvature background.
