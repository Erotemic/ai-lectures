# 017100 — Gauss–Bonnet by Triangulation: From Angle Excess to Euler Characteristic

**Track:** Topology and Geometry. **Background:** Gaussian curvature, geodesics, triangles, Euler characteristic. **Central question:** how can a local curvature measurement determine a global integer?

<!-- BEGIN SPOKEN LECTURE -->

# Gauss–Bonnet by Triangulation: From Angle Excess to Euler Characteristic

Draw a triangle on a flat sheet of paper. Its three angles sum to one hundred and eighty degrees. Now draw a triangle on a sphere, with sides following great circles. Start at the north pole, go down to the equator, travel a quarter of the way around it, and return to the north pole along another meridian. All three angles are right angles. Their sum is two hundred and seventy degrees.

That extra ninety degrees is not a measurement error. It is a consequence of positive curvature. Gauss–Bonnet shows that when these angular discrepancies are accumulated over an entire closed surface, the result is always an integer multiple of two pi. The integer is the Euler characteristic, which can be computed by counting vertices, edges, and faces.

Our aim is to see the mechanism rather than quote the finished theorem.

## A triangle records curvature

Consider a small geodesic triangle on an oriented surface. Geodesic means that its sides have zero intrinsic turning as we travel along them. The only sharp turns occur at the vertices. In the Euclidean plane, the three interior angles sum to pi radians. On a curved surface they need not.

For a geodesic triangle, the integrated Gaussian curvature over its interior equals the sum of its three interior angles minus pi, when the boundary and orientations have the usual compatible conventions. Positive curvature creates angle excess; negative curvature creates angle deficit.

On the sphere of radius R, curvature is constant at one divided by R squared. Our three-right-angle triangle covers one eighth of the sphere. Its area is one half pi times R squared, so its curvature integral is pi over two. The three angles sum to three halves pi, and subtracting pi gives the same answer. This calculation checks every part of the formula.

## Tile the surface and watch the cancellations

Suppose we have a closed oriented surface decomposed into geodesic triangles. Add the angle-excess formula for every triangle. The sum of the curvature integrals is the curvature integral over the whole surface, since the triangle interiors cover it without overlap.

The sum of all triangle angles can be counted in a different way. At each vertex, all incident triangles fill one complete turn. Their angles sum to two pi. If the triangulation has V vertices, the total of all angles is two pi times V.

Every triangle contributes one subtraction of pi. If there are F faces, the total curvature is two pi times V minus pi times F. Now every triangular face has three edges, and every edge belongs to two triangles because our surface is closed. Thus three F equals two E, where E is the number of edges.

Replace the face term using that counting identity. The curvature integral becomes two pi times V minus E plus F. The parenthesized quantity is the Euler characteristic. We have arrived at Gauss–Bonnet using local triangle geometry and two simple counting facts.

A rigorous proof must justify the existence of an appropriate geodesic triangulation or use a closely related local argument with curvature and boundary terms. But the arithmetic of the proof is visible: angles at vertices give V, sides shared by triangles give E, and the individual triangles give F.

## Three surfaces with different total curvature

For a sphere, Euler characteristic is two, so the integral of Gaussian curvature is four pi. That is true for any smooth Riemannian metric on the sphere, not merely for a perfectly round sphere. Curvature may concentrate in some regions and diminish elsewhere, but its total integral is fixed.

For a torus, Euler characteristic is zero. A flat torus makes this evident because curvature vanishes everywhere. A torus embedded as the familiar doughnut shape in three-dimensional space does not have zero Gaussian curvature at every point: it has positive and negative regions whose contributions integrate to zero.

A closed orientable surface with genus g has Euler characteristic two minus two g. For genus greater than one, the total curvature is negative. This does not mean every metric on the surface has negative curvature at every point. Gauss–Bonnet constrains the integral, not each point separately.

The remarkable feature is that a flexible geometric quantity, curvature, produces a rigid topological total.

## What changes when there is a boundary?

A flat disk has zero Gaussian curvature but Euler characteristic one. Does that contradict our formula? No, because a disk has a boundary. We omitted the turning contributed by the boundary curve.

For a smooth boundary, Gauss–Bonnet includes its geodesic curvature. For a piecewise smooth boundary, it also includes the exterior turning angles at corners. The sum of the interior curvature, smooth boundary turning, and corner turning equals two pi times the Euler characteristic.

On a Euclidean circular disk, interior curvature is zero. The circular boundary turns through one full revolution, giving two pi. On a Euclidean polygon, straight sides contribute zero continuous geodesic curvature, but its exterior angles sum to two pi. Both descriptions give the same topology.

This is the right way to understand a boundary term: it is not an arbitrary correction appended to save a theorem. It records part of the geometry that was excluded when we stopped counting only interior curvature.

## Why topology appears in a curvature integral

A local observer can measure Gaussian curvature from small distances, angles, or geodesic spreading. An observer with a global triangulation can count vertices, edges, and faces. Gauss–Bonnet proves that these are not unrelated forms of information. The geometry imposes a fixed total because the local turning contributions cancel internally when assembled into a closed surface.

In a more advanced formulation, the normalized curvature form represents the Euler class of the tangent bundle. Integrating that class over the fundamental cycle gives the Euler characteristic. This is the two-dimensional model for characteristic-class formulas that express topological integers as integrals of curvature polynomials.

So the derivation is worth remembering. First, curvature changes the angles of a small triangle. Next, triangles tile the surface and internal data cancel. Finally, counting vertices, edges, and faces turns the remaining total into a topological invariant. That sequence of ideas recurs in Chern–Weil theory and index theorems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a geodesic triangle \(T\) on an oriented smooth Riemannian surface with interior angles \(\alpha,\beta,\gamma\),
\[\int_T K\,dA=\alpha+\beta+\gamma-\pi.\]
For a geodesic triangulation of a closed surface, \(\sum_T(\alpha_T+\beta_T+\gamma_T)=2\pi V\) and \(3F=2E\); hence \(\int_MK\,dA=2\pi V-\pi F=2\pi(V-E+F)=2\pi\chi(M)\).

For an oriented compact surface with piecewise smooth boundary, a compatible sign convention yields
\[\int_M K\,dA+\int_{\partial M}k_g\,ds+\sum_j(\pi-\alpha_j)=2\pi\chi(M),\]
where \(\alpha_j\) are the interior corner angles and the positive boundary orientation keeps the surface on the left. On a Euclidean unit disk \(K=0\), \(k_g=1\), so \(\int_{\partial D}k_g ds=2\pi\). For a closed genus-g oriented surface, \(\chi=2-2g\).

### Exercises with answers

1. **Spherical octant.** Compute the angle excess of a triangle with three right angles. **Answer:** \(3\pi/2-\pi=\pi/2\).
2. **Count.** A geodesic triangulation of a closed surface has \(V=12,E=30,F=20\). What is \(\int K\,dA\)? **Answer:** \(2\pi(12-30+20)=4\pi\).
3. **Torus.** Must a torus with nonflat metric have curvature zero everywhere? **Answer:** No. Its total integrated curvature is zero.
4. **Flat disk.** Where is the missing \(2\pi\) if \(K=0\)? **Answer:** In the turning of the boundary curve or its corners.

### Sources and further reading

- University of Notre Dame, [Euler characteristic and Gauss–Bonnet lecture](https://sites.nd.edu/2023cmndthematicprogram/files/2023/06/lecture4-Lehmann-updated.pdf).
- MIT OpenCourseWare, [18.950 Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/).
- Overviews: [Gauss–Bonnet theorem](https://en.wikipedia.org/wiki/Gauss%E2%80%93Bonnet_theorem), [Euler characteristic](https://en.wikipedia.org/wiki/Euler_characteristic).
