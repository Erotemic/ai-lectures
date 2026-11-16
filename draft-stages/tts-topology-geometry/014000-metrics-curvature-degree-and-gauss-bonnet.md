# Metrics, curvature, degree, and Gauss-Bonnet

<!-- BEGIN SPOKEN LECTURE -->

# Metrics, curvature, degree, and Gauss-Bonnet

## Riemannian Metrics, Geodesics, and Intrinsic Curvature

Imagine living on the surface of a sphere but having no access to the third dimension. You can draw curves, measure the lengths of small segments, and compare directions in the tangent plane. Could you determine that your world is curved? You can. The geometry of distances within a surface contains enough information to detect curvature, even without any external viewpoint.

Riemannian geometry formalizes this idea. A Riemannian metric measures lengths and angles on each tangent space. Its associated connection defines geodesics and parallel transport. Curvature measures how those geometric operations depart from Euclidean behavior.

### A metric is more than a distance formula

At each point of a smooth manifold, a Riemannian metric assigns an inner product to pairs of tangent vectors. The assignment varies smoothly from point to point and is positive definite. It therefore tells us the length of every infinitesimal tangent vector and the angle between two tangent directions.

To find the length of a smooth curve, we integrate the norm of its velocity vector along the curve. The distance between two points is the infimum of the lengths of piecewise smooth curves joining them. Under standard connectedness assumptions, this produces the metric-space distance associated with the Riemannian metric.

The same manifold can carry many different Riemannian metrics. Topology specifies what it means for points and neighborhoods to fit together; a metric adds quantitative geometry. A flat plane can be stretched differently in different directions while retaining its topological identity.

### Coordinates are not the geometry

In local coordinates, the metric is represented by a symmetric positive-definite matrix of functions, often written g with indices i and j. A velocity vector with coordinate components v has squared length given by the quadratic form built from that matrix.

For the ordinary Euclidean plane, Cartesian coordinates give the diagonal metric matrix with ones on the diagonal. But switch to polar coordinates. The squared length of a small displacement is dr squared plus r squared times d theta squared. The metric coefficients now vary with position.

That variation does not mean the plane has acquired curvature. We changed coordinates, not the underlying geometry. Curvature must be expressed in a way that is unchanged by legitimate coordinate transformations.

This is an early test for every geometric formula. A coefficient can be nonzero because of coordinate choice alone. A genuine invariant cannot depend on that choice.

### The Levi-Civita connection

A connection describes how vectors are transported in a bundle. A Riemannian metric singles out a particularly important connection on the tangent bundle. The Levi-Civita connection is characterized by two requirements: it preserves the metric under parallel transport, and it has no torsion.

Metric compatibility says that when two vectors are transported in parallel along a curve, their inner product remains constant. Torsion-freeness says the difference between differentiating vector fields in opposite orders is governed exactly by their Lie bracket. These conditions determine one and only one connection.

In local coordinates its coefficients are called Christoffel symbols. They can be calculated from the metric coefficients and their first derivatives. Christoffel symbols are not themselves tensor components, and they can be nonzero even in flat space: polar coordinates in the Euclidean plane provide an example.

### Geodesics: straightness defined internally

A geodesic is a curve whose velocity vector remains parallel along the curve, according to the Levi-Civita connection. Its covariant acceleration is zero. This is the intrinsic replacement for the Euclidean condition that a straight line has zero ordinary acceleration.

In coordinates, the geodesic equation is a coupled system of second-order differential equations. The ordinary second derivative of each coordinate is corrected by terms involving the Christoffel symbols and products of velocity components.

On the Euclidean plane in Cartesian coordinates, all Christoffel symbols vanish, and the equations reduce to constant velocity. On a sphere with its standard round metric, geodesics are great circles, traversed at constant speed. A great circle need not look straight in three-dimensional space, but its acceleration as a curve in the ambient space points normally to the sphere. Its *tangential* acceleration vanishes.

Here is an important qualification. A geodesic is locally length-minimizing over sufficiently short segments, but not necessarily globally shortest between any two of its points. On a sphere, a segment of a great circle longer than half the circumference continues to be geodesic while no longer giving the shortest route between its endpoints.

### Curvature from parallel transport

Curvature measures what happens when covariant derivatives fail to commute. For the Levi-Civita connection, this produces the Riemann curvature tensor. In two dimensions, all its essential information at a point is summarized by one scalar, the Gaussian curvature.

A round sphere of radius R has Gaussian curvature one divided by R squared. The ordinary Euclidean plane has curvature zero. A cylinder has curvature zero as a surface in its intrinsic geometry, despite its visibly bent appearance in three-dimensional space. Small patches of a cylinder can be unrolled onto a plane without changing their lengths.

Why does the sphere differ from the cylinder? A sphere cannot be flattened onto a plane without distortion, even locally. One way to detect this is by measuring geodesic triangles: their angles on a positively curved surface can sum to more than a straight angle, whereas Euclidean triangles sum to exactly a straight angle. For sufficiently small geodesic triangles, the angular excess relates to the curvature integrated over the enclosed region.

### Gauss's Theorema Egregium

Historically, Carl Friedrich Gauss established that the Gaussian curvature of a regular surface is intrinsic. Although curvature can first be defined using how a surface bends in three-dimensional space, Gauss showed that it can be computed from the metric and its derivatives alone.

This was called the Theorema Egregium. It says that no local isometry can map a patch of the round sphere onto a patch of the Euclidean plane, because local isometries preserve Gaussian curvature. Conversely, the cylinder and plane have the same intrinsic curvature, even though they are embedded differently.

In higher dimensions, a single number no longer captures all directional curvature. Sectional curvature assigns curvature to a two-dimensional plane within a tangent space, and the full Riemann curvature tensor combines this information. It governs geodesic deviation, the way nearby freely traveling paths converge or diverge.

### Completeness and the global existence of geodesics

There is a final connection to differential equations. A geodesic is a solution of an ordinary differential equation on a manifold. Local existence and uniqueness follow under smoothness assumptions. But can the solution be continued for all time?

For a connected Riemannian manifold, the Hopf–Rinow theorem links several forms of completeness. Completeness as a metric space is equivalent to geodesic completeness: every geodesic with initial data extends for all real parameter time. In this setting any two points can also be joined by a minimizing geodesic. Without completeness these conclusions may fail. The open unit disk with the Euclidean metric is an example: a straight line can reach the missing boundary in finite time.

Riemannian geometry therefore links the local and the global. The metric gives infinitesimal lengths. The Levi-Civita connection gives a rule for straight motion. Curvature detects the non-Euclidean geometry seen by local measurements. Completeness determines whether local geodesic motion can continue indefinitely. All of it is intrinsic to the space and its chosen metric.

## Riemannian Geometry by Calculation: Metric, Connection, and Geodesics

A person walking on a sphere can describe their motion with latitude and longitude. But those coordinates do not measure equal distances: one degree of longitude is a much shorter walk near a pole than near the equator. That basic observation is the starting point of Riemannian geometry. The coordinate grid is a description. The metric tells us which displacements represent the same physical length.

Our goal is practical. We will take a metric, compute the correction terms needed to differentiate a moving vector, and use them to decide whether a path is a geodesic. We will compare the flat plane and a round sphere. The comparison matters because many advanced geometric theories use these calculations but seldom pause to carry them through.

### Begin with a moving ruler

In Cartesian coordinates on the plane, a small displacement has horizontal and vertical components. Its squared length is the sum of their squares. In polar coordinates we describe the same displacement by a radial change and an angular change. One unit of radial movement always has length one. A small angular change has length approximately the radius times the size of that change. Thus the metric says: squared length equals radial change squared, plus radius squared times angular change squared.

This formula is not a new geometry. It is the same plane expressed in different coordinates. In particular, a varying metric coefficient is not proof that a space is curved. Curvature is something the observer can measure even after changing their coordinates.

A general Riemannian metric supplies such a positive-definite quadratic form at every point. We may picture it as an infinitesimal ruler: feed it a tangent direction and it reports the square of the length. Feed it two directions and it reports their inner product. Integrating the infinitesimal speed of a curve gives the curve's length.

### Why ordinary derivatives of vector components fail

Imagine carrying an arrow while moving around the origin in the plane. If the arrow keeps pointing in one fixed Cartesian direction, it is not turning. But its components in the rotating polar basis change, because the radial and angular basis vectors themselves rotate. Simply differentiating the two component numbers would report a change even when the arrow has not turned at all.

A connection fixes that problem. A covariant derivative differentiates both the vector components and the moving coordinate basis. The extra correction coefficients are called Christoffel symbols. They describe how the basis changes, not necessarily how the underlying space bends.

For a metric there is a distinguished choice of connection. The Levi-Civita connection keeps inner products constant under parallel transport and has zero torsion. Those two requirements determine the connection uniquely. That makes the correction coefficients calculable from the metric, instead of introducing them as independent unknowns.

### A complete example in polar coordinates

Take the plane, remove the origin so polar coordinates are well-defined, and use its ordinary Euclidean metric. The Christoffel symbols with an angular-angular input produce an inward radial correction proportional to the radius. The symbols coupling radial and angular directions produce a correction inversely proportional to the radius.

Let us see what those statements mean for a path of constant radius. A person moving around a circle may keep the radius fixed while their angular coordinate changes uniformly. Their ordinary radial coordinate has zero second derivative. But the covariant radial acceleration does not vanish. Its correction points inward. That circle is not a geodesic of the Euclidean plane: the person has to keep turning.

Now consider a radial ray, with angular coordinate constant and radial coordinate changing at constant speed. In the geodesic equation, all the angular velocity terms vanish. The remaining equation simply says the radial speed is constant. A radial ray is a geodesic, as expected.

We have obtained a familiar fact using symbols that were nonzero throughout the calculation. This is why Christoffel symbols and curvature must not be confused. They play different roles.

### Now change the space, not just the coordinates

Consider a round sphere of radius R. Use the polar angle measured down from the north pole and an azimuthal angle around the axis. A small change in polar angle has length R times that change. A small azimuthal change has length R times the sine of the polar angle, times the azimuthal change. At the poles, changing longitude has no first-order physical effect. At the equator, it has the greatest effect.

The metric now has an angular coefficient that shrinks near the poles. As before, we can compute a Levi-Civita connection from the coefficient and its derivatives. One correction involves minus sine times cosine of the polar angle. Another involves the ratio of cosine to sine. The formulas are singular at the poles because the longitude coordinate becomes singular there; the sphere itself is smooth.

Which circles of latitude are geodesics? Set the polar angle constant and let the azimuthal angle advance. The polar component of the geodesic equation contains a sine-times-cosine factor. Away from the poles, this vanishes at the equator. The equator is a geodesic. An ordinary line of latitude farther north is not. To follow it, a traveler must continually turn relative to intrinsic straight motion.

Great circles are all geodesics. We used one particular coordinate grid to verify the equator, but rotating the sphere carries that example to any great circle and preserves the metric.

### Speed and parameter choice

There are two easily confused ideas: a geodesic as an unparameterized route and a geodesic traversed at a particular rate. The equation with zero covariant acceleration assumes an affine parameter, often arc length or a constant multiple of arc length. If we speed up and slow down while following the same great circle, the trace remains a geodesic path, but the new parameter may not satisfy the same equation.

The distinction matters in mechanics and numerical work. When a simulation produces an apparent extra force along the direction of motion, check whether it is a genuine departure from geodesic motion or an artifact of how time was parameterized.

### What this gives us

We can now read a metric as a local ruler, derive a connection that respects that ruler, and solve for paths whose covariant acceleration vanishes. We also know two checks on our work. First, coordinate singularities are not necessarily geometric singularities. Second, nonzero Christoffel symbols are not evidence of nonzero curvature.

These ideas prepare the ground for geodesic deviation, in which we compare two neighboring geodesics. That comparison finally reveals a property of the geometry that no coordinate change can remove.

## Jacobi Fields: Curvature Seen Through Neighboring Geodesics

Imagine standing at the north pole of Earth with several companions. Everyone begins walking due south at the same constant speed, following a great circle. At first the group spreads out as the lines of longitude separate. Later the paths begin to draw together, and if everyone continues for half a circumference, they meet at the south pole.

On a flat plane, rays leaving a point at slightly different angles would keep moving apart. The contrast between these two experiences is an operational way to detect curvature. It does not require seeing the sphere from outside. It only requires observing neighboring shortest-path candidates.

### One path is not enough

A geodesic is a curve that carries its velocity parallel along itself. To see curvature, we need a family of geodesics, each with slightly different initial data. Picture a strip of paths with a parameter labeling which path we are on and a time parameter measuring progress along each path.

Choose a reference geodesic in the strip. A displacement vector tells us how a nearby geodesic moves relative to it when we change the path label slightly. This displacement along the reference path is called a Jacobi field. It is not an arbitrary vector field; it is obtained by differentiating a genuine variation through geodesics.

There are two accelerations to distinguish. One is the acceleration along an individual geodesic, which vanishes in the covariant sense. The other is the relative acceleration of neighboring geodesics, which generally does not vanish. Curvature controls the second.

### Where the Jacobi equation comes from

Covariant derivatives in two directions need not commute. Their failure to commute is measured by the Riemann curvature tensor. Apply that commutator to the two directions of the strip: one along the paths and one between them. Because every individual path is geodesic, much of the expression cancels. What remains is a differential equation for the displacement vector.

The equation says that the second covariant derivative of the displacement, along the reference path, is balanced by a curvature term involving the displacement and the path's velocity. It looks like the equation for a spring, except the strength and sign of the restoring term are supplied by the geometry.

We should not yet conclude that positive curvature always draws every pair of paths together. The equation acts on components transverse to the path, and the relevant curvature is sectional curvature in the plane spanned by the path direction and displacement. In higher dimensions different transverse directions may behave differently.

### Three model worlds

Begin in the Euclidean plane. Curvature is zero. The equation becomes the statement that relative acceleration vanishes. If two straight paths start at the same point with a small angular difference, their separation grows linearly with distance traveled. Double the travel time and, to first order in the initial angle, double their separation.

On a round sphere the transverse equation becomes the same kind of differential equation as a harmonic oscillator. With zero initial separation and unit initial separation rate, its solution grows like a sine. The separation first increases, reaches a maximum, then decreases to zero. It becomes zero again when the travel distance is half a great-circle circumference. That is the north-pole-to-south-pole experiment.

In a surface of constant negative curvature, the transverse equation instead has a solution growing like a hyperbolic sine. Nearby geodesics leaving a point diverge faster than linearly. This is not merely a drawing of a saddle-shaped surface: it is a quantitative prediction about intrinsic distances.

These are local, first-order comparisons of paths. They do not give an exact finite separation for arbitrarily far apart paths, and they do not by themselves classify the global topology.

### When local shortest paths stop being locally shortest

On the sphere, the convergence at the south pole has another meaning. Many geodesics connect the north pole to the south pole. Vary the initial direction and the endpoint does not change. The corresponding Jacobi field vanishes at both endpoints. The south pole is a conjugate point of the north pole along that great circle.

Conjugate points arise where a geodesic variation develops this degeneracy. They are related to the failure of a geodesic to remain locally minimizing beyond the first conjugate point. But two different global phenomena must not be merged. A geodesic can stop being globally shortest because another route becomes shorter before any conjugate point appears. Global minimizing can fail at the cut locus even when local second-variation behavior is still favorable.

For example, a flat cylinder has no intrinsic curvature and no conjugate points along its straight geodesics, but two points can have competing routes winding around opposite sides of the cylinder. That is a topological global effect, not a focusing effect of positive curvature.

### Why curvature is a tensor

A reader of geodesic equations may wonder why we introduce an elaborate four-index object when a surface has just one Gaussian curvature. In two dimensions there is indeed only one independent curvature function. In three or more dimensions, however, two different planes through the same tangent direction may bend differently.

The curvature tensor packages all those directional comparisons and behaves properly when we change coordinates. Christoffel symbols alone are not tensors, because part of their apparent change comes from how the basis moves. The combination of derivatives and products that defines curvature cancels those coordinate artifacts.

This is a general pattern in geometry. A coordinate expression may look complicated, while the geometric object it represents is simple to state: how much does transport fail to close, or how do nearby geodesics accelerate relative to each other?

### A bridge to analysis and topology

The Jacobi equation is a linear differential equation along a given geodesic. Existence and uniqueness are ordinary differential-equation ideas, and its zeros have geometric meaning. Later, second variation formulas will use the same fields to analyze stability and minimizing properties. Morse theory of the energy functional on path space also builds on conjugate points and variations of geodesics.

The lesson is that curvature is not just a number attached to a shape. It makes predictions about motion. Neighboring geodesics spread, focus, or remain proportionally separated according to the curvature they encounter. With that observation, the abstract curvature tensor becomes something one can test.

## Gauss–Bonnet: Curvature Counts Topology

A sphere and a torus can both be made smooth, and both can be bent in space. A torus may have regions of positive and negative curvature, while a round sphere has positive curvature everywhere. These statements concern the shapes we see. Gauss–Bonnet goes further: when curvature is integrated across a compact closed oriented surface, the result is determined by its topology, not by the particular smooth metric used to measure it.

That is a remarkable claim. Curvature is local: it measures how the geometry behaves near a point. Topology is global: it records properties that survive continuous deformation. Gauss–Bonnet is an exact bridge between them.

### Curvature is not the same as bending in space

For a surface with a Riemannian metric, Gaussian curvature measures the intrinsic geometry of small patches. A sphere of radius R has Gaussian curvature equal to one divided by R squared. Its area is four pi R squared. Multiplying these gives four pi, independent of the radius.

Why does the radius disappear? Because enlarging the sphere reduces its curvature and increases its area in exactly compensating ways. The total curvature, unlike the pointwise curvature, remembers something stable.

A cylinder may look bent in three-dimensional space, but its intrinsic Gaussian curvature is zero. You can cut and unroll a cylinder into a flat sheet without stretching its metric locally. This illustrates why the theorem concerns intrinsic Gaussian curvature, not simply how much a surface appears to bend in a surrounding space.

### Triangles that refuse to have Euclidean angles

On a plane, the angles of an ordinary triangle sum to one hundred eighty degrees. On a sphere, geodesics are arcs of great circles, and geodesic triangles can have a larger angle sum.

Choose the north pole and two points on the equator separated by a quarter of the equator. Join them by shortest great-circle arcs. All three interior angles are right angles. Their sum is two hundred seventy degrees, an excess of ninety degrees. The triangle covers one eighth of the sphere. On the unit sphere its area is pi over two, exactly the angle excess measured in radians.

This is a local form of Gauss–Bonnet for a geodesic triangle: the integral of Gaussian curvature over the triangle equals the sum of its interior angles minus pi. On a flat surface the curvature integral vanishes and the Euclidean rule returns.

But what if the triangle's edges are not geodesics? Then the curve itself bends within the surface. We need a boundary term called geodesic curvature. It measures how a curve departs from being a geodesic, using the surface's own metric. At corners, we must also count the change in direction, described by exterior turning angles.

### The theorem with a boundary

For a compact oriented Riemannian surface with piecewise smooth boundary, the integral of Gaussian curvature over the surface, plus the integral of geodesic curvature along the positively oriented boundary, plus the sum of the exterior corner angles, equals two pi times the Euler characteristic of the surface.

The Euler characteristic can be computed from a triangulation: number of vertices minus number of edges plus number of faces. On a topological sphere it is two. On a torus it is zero. On an orientable closed surface with g handles, it is two minus twice g.

If the surface has no boundary, both boundary contributions vanish. Total Gaussian curvature is therefore two pi times Euler characteristic. For a sphere, that is four pi. For a torus, it is zero. For a double torus it is negative four pi. The exact total cannot be changed by stretching the metric, so long as we remain in the theorem's geometric setting.

A torus can have positively and negatively curved regions. Its total must balance to zero, but the theorem does not require its curvature to be zero at every point. A flat torus is possible as an abstract Riemannian manifold, even though a smooth isometric embedding as a standard torus in three-dimensional Euclidean space cannot have zero Gaussian curvature everywhere.

### Why triangulation makes topology appear

There is a proof strategy that lets us see where vertices, edges, and faces enter. Subdivide the surface into many small geodesic triangles. For each triangle, compare the sum of its angles with pi; the difference is its integrated curvature. Now add those identities over all triangles.

Every interior edge is shared, so the boundary effects on one side cancel those on the other. At an interior vertex, the angles around a smooth surface add to two pi. What remains is a count built from triangles, their edges, and their vertices. That count is the Euler characteristic. The formulas are geometric locally, but their global bookkeeping becomes combinatorial.

For a surface with boundary, the uncanceled edge turns and corner jumps produce exactly the geodesic-curvature and exterior-angle terms. The boundary formula is therefore not an optional amendment to the closed-surface formula. It is the form that makes the cancellation mechanism work when the surface has an edge.

Consider a flat circular disk of radius R. Gaussian curvature is zero. The geodesic curvature of its boundary circle is one divided by R, and the circumference is two pi R. The boundary integral is two pi. The disk has Euler characteristic one, so the theorem checks out. If we omitted the boundary term, we would obtain a false statement.

### Geometry puts limits on topology

Gauss–Bonnet can also rule out proposed metrics. If a compact closed oriented surface has Gaussian curvature strictly positive at every point, its total curvature is positive, so its Euler characteristic must be positive. Among connected closed orientable surfaces, this forces the topology of a sphere. If the curvature is everywhere negative, the Euler characteristic must be negative, ruling out the sphere and torus.

The converse statements require care. Knowing Euler characteristic is positive does not mean every metric on that surface is everywhere positively curved. Total curvature constrains the integral; it does not dictate the sign at every point.

This is an early example of a principle that recurs in global geometry: integrate local differential information, and topology emerges as a constraint on the result.

### A theorem about what cannot be changed

Curvature seems to describe the shape of a surface at an instant, and Euler characteristic seems to describe its topological identity. Gauss–Bonnet shows that they are connected by an exact equation. On a sphere, any smooth metric distributes a total of four pi units of Gaussian curvature, whatever the local peaks and valleys. On a torus, the signed total must cancel.

The theorem is both an analytic calculation and a counting argument. That combination—local differential geometry, boundary correction, and global topological invariant—is why Gauss–Bonnet remains a prototype for much more general index and characteristic-class theorems.

## Gauss–Bonnet by Triangulation: From Angle Excess to Euler Characteristic

Draw a triangle on a flat sheet of paper. Its three angles sum to one hundred and eighty degrees. Now draw a triangle on a sphere, with sides following great circles. Start at the north pole, go down to the equator, travel a quarter of the way around it, and return to the north pole along another meridian. All three angles are right angles. Their sum is two hundred and seventy degrees.

That extra ninety degrees is not a measurement error. It is a consequence of positive curvature. Gauss–Bonnet shows that when these angular discrepancies are accumulated over an entire closed surface, the result is always an integer multiple of two pi. The integer is the Euler characteristic, which can be computed by counting vertices, edges, and faces.

Our aim is to see the mechanism rather than quote the finished theorem.

### A triangle records curvature

Consider a small geodesic triangle on an oriented surface. Geodesic means that its sides have zero intrinsic turning as we travel along them. The only sharp turns occur at the vertices. In the Euclidean plane, the three interior angles sum to pi radians. On a curved surface they need not.

For a geodesic triangle, the integrated Gaussian curvature over its interior equals the sum of its three interior angles minus pi, when the boundary and orientations have the usual compatible conventions. Positive curvature creates angle excess; negative curvature creates angle deficit.

On the sphere of radius R, curvature is constant at one divided by R squared. Our three-right-angle triangle covers one eighth of the sphere. Its area is one half pi times R squared, so its curvature integral is pi over two. The three angles sum to three halves pi, and subtracting pi gives the same answer. This calculation checks every part of the formula.

### Tile the surface and watch the cancellations

Suppose we have a closed oriented surface decomposed into geodesic triangles. Add the angle-excess formula for every triangle. The sum of the curvature integrals is the curvature integral over the whole surface, since the triangle interiors cover it without overlap.

The sum of all triangle angles can be counted in a different way. At each vertex, all incident triangles fill one complete turn. Their angles sum to two pi. If the triangulation has V vertices, the total of all angles is two pi times V.

Every triangle contributes one subtraction of pi. If there are F faces, the total curvature is two pi times V minus pi times F. Now every triangular face has three edges, and every edge belongs to two triangles because our surface is closed. Thus three F equals two E, where E is the number of edges.

Replace the face term using that counting identity. The curvature integral becomes two pi times V minus E plus F. The parenthesized quantity is the Euler characteristic. We have arrived at Gauss–Bonnet using local triangle geometry and two simple counting facts.

A rigorous proof must justify the existence of an appropriate geodesic triangulation or use a closely related local argument with curvature and boundary terms. But the arithmetic of the proof is visible: angles at vertices give V, sides shared by triangles give E, and the individual triangles give F.

### Three surfaces with different total curvature

For a sphere, Euler characteristic is two, so the integral of Gaussian curvature is four pi. That is true for any smooth Riemannian metric on the sphere, not merely for a perfectly round sphere. Curvature may concentrate in some regions and diminish elsewhere, but its total integral is fixed.

For a torus, Euler characteristic is zero. A flat torus makes this evident because curvature vanishes everywhere. A torus embedded as the familiar doughnut shape in three-dimensional space does not have zero Gaussian curvature at every point: it has positive and negative regions whose contributions integrate to zero.

A closed orientable surface with genus g has Euler characteristic two minus two g. For genus greater than one, the total curvature is negative. This does not mean every metric on the surface has negative curvature at every point. Gauss–Bonnet constrains the integral, not each point separately.

The remarkable feature is that a flexible geometric quantity, curvature, produces a rigid topological total.

### What changes when there is a boundary?

A flat disk has zero Gaussian curvature but Euler characteristic one. Does that contradict our formula? No, because a disk has a boundary. We omitted the turning contributed by the boundary curve.

For a smooth boundary, Gauss–Bonnet includes its geodesic curvature. For a piecewise smooth boundary, it also includes the exterior turning angles at corners. The sum of the interior curvature, smooth boundary turning, and corner turning equals two pi times the Euler characteristic.

On a Euclidean circular disk, interior curvature is zero. The circular boundary turns through one full revolution, giving two pi. On a Euclidean polygon, straight sides contribute zero continuous geodesic curvature, but its exterior angles sum to two pi. Both descriptions give the same topology.

This is the right way to understand a boundary term: it is not an arbitrary correction appended to save a theorem. It records part of the geometry that was excluded when we stopped counting only interior curvature.

### Why topology appears in a curvature integral

A local observer can measure Gaussian curvature from small distances, angles, or geodesic spreading. An observer with a global triangulation can count vertices, edges, and faces. Gauss–Bonnet proves that these are not unrelated forms of information. The geometry imposes a fixed total because the local turning contributions cancel internally when assembled into a closed surface.

In a more advanced formulation, the normalized curvature form represents the Euler class of the tangent bundle. Integrating that class over the fundamental cycle gives the Euler characteristic. This is the two-dimensional model for characteristic-class formulas that express topological integers as integrals of curvature polynomials.

So the derivation is worth remembering. First, curvature changes the angles of a small triangle. Next, triangles tile the surface and internal data cancel. Finally, counting vertices, edges, and faces turns the remaining total into a topological invariant. That sequence of ideas recurs in Chern–Weil theory and index theorems.

## Degree Theory, Brouwer Fixed Points, and Global Constraints

A map can fold a sphere, stretch one hemisphere over another, and reverse orientation in some regions. If we watch only its image, it may be hard to tell what the map does globally. Yet there is an integer that survives every continuous deformation of the map. It is called the degree.

On the circle, degree is familiar from winding numbers. Take a point running once around the unit circle. A map that sends its angle to three times that angle makes the image run around three times. Its degree is three. Reverse the angle and the degree becomes minus one. Collapse the entire circle to one fixed point and the degree is zero.

The circle is only the first case. For every positive dimension n, a continuous map from the n-dimensional sphere to itself induces multiplication by an integer on its top homology group. That integer is the degree. This definition needs no differentiability, and it remembers orientation as well as multiplicity.

### Why degree cannot change continuously

Imagine a continuous family of maps from the sphere to itself. At the start, the map wraps the sphere twice. At the end, suppose it somehow wraps only once. That would require the integer degree to move from two to one during a homotopy. But homotopic maps induce the same map on homology. Degree therefore stays fixed.

This makes degree useful for existence questions. If a map has nonzero degree, it must be onto. For suppose some point of the target sphere were missing. Then the map would factor through the sphere with that point removed. A punctured sphere is contractible and has no top-dimensional homology. The induced map on top homology would be zero. But nonzero degree says it is not zero. Contradiction.

The proof doesn't identify a preimage. It proves that a preimage has to exist. That distinction is the strength of a topological argument: it can force a solution even when no formula is available.

### Counting preimages with signs

For a smooth map between compact oriented manifolds of the same dimension, degree also has a local description. Pick a regular target value. Its preimages are isolated and, under compactness, finite. At each preimage the derivative either preserves or reverses orientation. Assign plus one or minus one accordingly, then add the signs.

The signed total is the degree. A fold may create two new preimages, but typically one contributes plus one and the other minus one. Their total is zero. That is how the integer survives geometric changes that alter the raw number of preimages.

Counting unsigned preimages would be too unstable. One pair can appear or disappear under a small deformation. The orientation signs cancel exactly the kind of change that would spoil the invariant.

### The fixed-point problem on a disk

Now take a continuous map from a closed disk to itself. Must some point stay fixed? Brouwer's fixed-point theorem says yes. The claim is not that every point stays in place, nor that we can easily compute the fixed point. It is a pure existence result.

For a two-dimensional disk, suppose instead that no point is fixed. From each proposed point x, draw the ray that starts at its image and passes through x. Because the image differs from x, the ray is defined. Continue it until it reaches the boundary circle. This constructs a continuous map from the disk onto its boundary that fixes every boundary point.

Such a map is called a retraction. But a disk cannot retract onto its boundary circle. The boundary circle has a nontrivial first homology group, while the disk is contractible and has zero first homology. If a retraction existed, composing the inclusion of the circle into the disk with the retraction back onto the circle would be the identity. On first homology the composition would have to be both the identity and zero. Impossible.

The same argument works in higher dimensions with the appropriate reduced homology group. Degree theory expresses the same obstruction in a particularly compact language: the identity map of the boundary sphere has degree one, yet any map from the sphere extending over the disk must have degree zero.

### Why topology does not compute the answer

This theorem does not make fixed-point iteration automatically converge. A continuous map of a disk may have several fixed points, and a naïve numerical iteration may cycle or behave badly. Existence and effective computation are different questions.

Nor can we drop the disk's compactness and convexity without replacing them with other hypotheses. Translation on the real line, for example, has no fixed point. Topology says which structural constraints are responsible for existence, not that fixed points must appear everywhere.

Degree provides a kind of algebraic conservation law for maps. As long as a deformation respects the boundary and stays continuous, the signed count cannot change. The consequence is a proof that a missing solution would violate an integer invariant. This reasoning underlies many existence theorems in nonlinear analysis.

## Regular Values and Degree: Counting Solutions with Signs

Consider the map that takes a point on a circle and winds it around the circle three times. Most people can see that it has degree three. But what does that phrase mean if the map is distorted, if its speed varies, or if its formula is written in coordinates that hide the winding?

Degree theory gives a robust way to count. Choose a target point and ask how many source points map to it. Count with signs determined by whether the map preserves or reverses local orientation. Under suitable compactness and smoothness hypotheses, this signed total is independent of the ordinary target point chosen. It is an integer that survives continuous deformation.

### What makes a target value regular?

Start with a smooth function of two real variables: x squared plus y squared. The set on which this function equals one is a circle. At every point of that circle, the gradient is nonzero. The implicit function theorem then tells us that the level set locally looks like a smooth curve.

At level zero, the set has collapsed to one point, the origin. There the gradient vanishes. The implicit-function argument does not apply. This does not prove that every singular level set is badly behaved, but it explains why a nonvanishing derivative is an effective condition for predictable geometry.

For a smooth map between manifolds, a target value is called regular when the derivative is surjective at every source point mapping to it. The regular-value theorem says that the inverse image is a submanifold of the expected dimension, assuming the usual smoothness hypotheses. If source and target have the same dimension, that inverse image is discrete. If the source manifold is compact, a discrete closed subset is finite.

Regular values therefore allow us to replace an infinite geometric object with a finite list of points.

### Count each point with the right sign

Let source and target be connected, closed, oriented manifolds of the same dimension. At a preimage of a regular value, the derivative is an invertible linear map between oriented tangent spaces. It either preserves orientation or reverses it. Assign plus one in the first case and minus one in the second.

Add those local signs. The result is the degree of the map. Why should it not change when we move the target point a little? The inverse function theorem makes the preimages move smoothly nearby, and their signs stay constant until a critical value is crossed. At crossings, preimages can appear or disappear in opposite-sign pairs. The signed count stays unchanged.

A complete proof uses homology or a regular-value argument supported by Sard's theorem, which says smooth maps have regular values densely and in fact outside a set of measure zero in the target. Smoothness and compactness prevent the kinds of uncontrolled behavior that would defeat our count.

### Winding the circle by an integer

Write a point of the circle as a complex number of modulus one. Map it to its mth power, where m is a nonzero integer. A generic target point has the absolute value of m distinct preimages. If m is positive, the map preserves the orientation at each of them. If m is negative, it reverses orientation at each. The signed count is exactly m.

When m is two, the target point one has two preimages. Each contributes plus one. When m is negative two, each contributes minus one. A direct counting of points would give two in both cases; signed counting distinguishes the direction of winding.

This example is easy because the map is explicit. The power of degree theory is that the integer remains meaningful even after a complicated deformation of the formula, as long as the map remains continuous between the appropriate compact oriented spaces.

### Why nonzero degree forces a solution

Suppose a smooth map has nonzero degree. It must be onto. If some target point were missed, choose that point as a regular value: its preimage is empty, so the signed sum would be zero. That contradicts nonzero degree.

This turns a calculation into an existence theorem. You may not know where a solution of the equation f of x equals y lies. But if the map has nonzero degree, a solution must exist for every y in the target.

Degree also behaves well under composition. The degree of a composition is the product of the degrees. An orientation-preserving homeomorphism of a connected oriented closed manifold has degree plus one; an orientation-reversing one has degree minus one. On a two-dimensional sphere, the antipodal map has degree minus one. On a circle, the antipodal map has degree plus one: turning a circle by half a revolution preserves its orientation.

### From degree to the fixed-point theorem

The Brouwer fixed-point theorem says that every continuous map from a closed disk to itself has a fixed point. The classic proof is indirect. Assume a map has no fixed points. From each point of the disk, draw a ray starting at its image and passing through the original point. Extend the ray to the boundary. This assigns each disk point a boundary point continuously, and on the boundary it acts as the identity.

We would have constructed a retraction of the disk onto its boundary circle. But such a retraction cannot exist. Passing to first homology, the identity on the circle would have to factor through the disk's first homology, which is zero. The identity map on the integers cannot factor through the zero group.

Here the fixed-point theorem emerges not from an inequality or a contraction estimate but from a topological obstruction. Degree and homology provide a global reason a solution must exist.

### A reusable method

When a later theorem asks for existence of a zero, a fixed point, or a critical solution, it may be worth looking for a degree. Identify an oriented domain, locate regular values, determine signs, and check that solutions cannot escape through a boundary or to infinity. If the domain is noncompact, extra properness hypotheses are needed; if it has boundary, one must prevent the target value from appearing on the boundary during a homotopy.

The basic idea is already present on the circle. Count solutions with orientation. The count is stable even when individual solutions move or cancel. That is how local derivatives produce a global integer, and how a global integer can force the existence of a solution.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Riemannian Metrics, Geodesics, and Intrinsic Curvature

**Track:** Topology and Geometry. **Background:** manifolds, tangent spaces, covariant derivatives, differential forms. **Central question:** how can people who live entirely within a curved space measure distance and curvature without looking outside it?

#### Mathematical companion (not spoken)

A Riemannian metric \(g\) on a smooth manifold \(M\) is a smoothly varying positive-definite symmetric bilinear form on \(T_pM\). In coordinates,
\[ds^2=\sum_{i,j}g_{ij}(x)\,dx^i dx^j,\qquad L(\gamma)=\int\sqrt{g_{\gamma(t)}(\dot\gamma(t),\dot\gamma(t))}\,dt.\]
The Levi-Civita connection is uniquely characterized by \(\nabla g=0\) and zero torsion. Its symbols are
\[\Gamma^k_{ij}=\tfrac12g^{k\ell}(\partial_i g_{j\ell}+\partial_jg_{i\ell}-\partial_\ell g_{ij}),\]
and affine-parameter geodesics satisfy
\[\ddot x^k+\Gamma^k_{ij}\dot x^i\dot x^j=0.\]
For the Euclidean plane in polar coordinates \(g=dr^2+r^2d\theta^2\), the nonzero symbols (away from \(r=0\)) are \(\Gamma^r_{\theta\theta}=-r\), \(\Gamma^\theta_{r\theta}=\Gamma^\theta_{\theta r}=1/r\), while Gaussian curvature is still \(0\). For a round sphere of radius \(R\), \(K=1/R^2\). A cylinder has \(K=0\) despite nonzero extrinsic bending.

The Riemann curvature operator (one common convention) is \(R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z\). Under a local isometry, the Riemann tensor and sectional curvature are preserved; Gauss's Theorema Egregium is the surface case. On connected Riemannian manifolds, the Hopf–Rinow theorem relates metric completeness to geodesic completeness and existence of minimizing geodesics between points.

##### Exercises with answers

1. Does nonzero Christoffel symbol imply nonzero curvature? **No:** polar coordinates on the Euclidean plane have nonzero symbols but zero Gaussian curvature.
2. Are all geodesic segments globally minimizing? **No:** a great-circle arc longer than half the circumference is a counterexample.
3. Can the round sphere be flattened locally onto the plane by an isometry? **No:** their Gaussian curvatures differ.
4. Is the Euclidean open disk a complete Riemannian manifold? **No:** a straight geodesic reaches its missing boundary in finite affine time.

##### Reading and source notes

- Sucharit Sarkar, [UCLA Differential Geometry Lecture 24: Gauss's Theorema Egregium](https://math.ucla.edu/~sucharit/120A-notes.html), intrinsic computation of Gaussian curvature.
- [University of Colorado lecture on the Theorema Egregium and geodesic spreading](https://math.colorado.edu/~sbc21/teaching/26fall/4230/lecture_notes/).
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), metrics, geodesics, connections and curvature.

### Riemannian Geometry by Calculation: Metric, Connection, and Geodesics

**Track:** Topology and Geometry. **Background:** derivatives of several variables, smooth coordinates, tangent vectors, and the meaning of a Riemannian metric. **Central question:** how can we calculate straight motion on a curved manifold without trusting a picture of its embedding?

#### Mathematical companion (not spoken)

On a smooth manifold, a metric has coordinate expression \(g=g_{ij}(x)dx^i\otimes dx^j\) with positive-definite matrix \((g_{ij})\). Length of \(\gamma\) is \(L(\gamma)=\int\sqrt{g_{ij}(\gamma)\dot\gamma^i\dot\gamma^j}\,dt\). The Levi-Civita symbols satisfy
\[\Gamma^k{}_{ij}=\tfrac12 g^{k\ell}(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}),\qquad \ddot x^k+\Gamma^k{}_{ij}\dot x^i\dot x^j=0.\]
For the flat punctured plane, \(ds^2=dr^2+r^2d\theta^2\): \(\Gamma^r{}_{\theta\theta}=-r\) and \(\Gamma^\theta{}_{r\theta}=\Gamma^\theta{}_{\theta r}=1/r\). A circle \(r=r_0\), \(\dot\theta\ne0\), violates the radial geodesic equation \(\ddot r-r\dot\theta^2=0\). Despite the nonzero connection coefficients, \(R=0\).

On the round sphere away from the coordinate poles, \(g=R^2(d\vartheta^2+\sin^2\vartheta\,d\varphi^2)\), \(\Gamma^\vartheta{}_{\varphi\varphi}=-\sin\vartheta\cos\vartheta\), and \(\Gamma^\varphi{}_{\vartheta\varphi}=\Gamma^\varphi{}_{\varphi\vartheta}=\cot\vartheta\). Constant \(\vartheta\) and nonzero constant \(\dot\varphi\) solves the polar geodesic equation only at \(\vartheta=\pi/2\); coordinate poles cannot be tested with this chart.

##### Exercises with answers

1. **Flat coordinates.** On the polar plane, is \(r=2,\theta=t\) a geodesic? **Answer:** No: its radial covariant acceleration is \(-2\), although \(\ddot r=0\).
2. **Radial motion.** Test \(r(t)=3+t,\theta(t)=\theta_0\). **Answer:** It satisfies the geodesic equations on any interval where \(r>0\).
3. **Sphere.** Why does a non-equatorial latitude circle fail? **Answer:** The polar equation includes \(-\sin\vartheta\cos\vartheta\,\dot\varphi^2\), which is nonzero away from the poles and equator.
4. **Interpretation.** Does \(\cot\vartheta\) becoming infinite near a pole imply infinite intrinsic curvature? **Answer:** No. Longitude coordinates degenerate there; the round sphere has finite constant Gaussian curvature \(1/R^2\).

##### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds: lecture notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- MIT OpenCourseWare, [18.950 Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/).
- Background overview: [Christoffel symbols](https://en.wikipedia.org/wiki/Christoffel_symbols), [Levi-Civita connection](https://en.wikipedia.org/wiki/Levi-Civita_connection).

### Jacobi Fields: Curvature Seen Through Neighboring Geodesics

**Track:** Topology and Geometry. **Background:** covariant differentiation, geodesics, simple second-order differential equations. **Central question:** what does curvature do to paths that start close together?

#### Mathematical companion (not spoken)

Adopt \(R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z\). For a unit-speed geodesic with tangent \(T\), a Jacobi field \(J\) derived from a variation through geodesics satisfies
\[\nabla_T\nabla_TJ+R(J,T)T=0.\]
In dimension two with \(J=jN\) normal to \(T\) and \(N\) parallel along the geodesic, \(j''+Kj=0\). If \(j(0)=0\), \(j'(0)=1\), then
\[j(t)=t\quad(K=0),\qquad j(t)=R\sin(t/R)\quad(K=1/R^2),\qquad j(t)=\frac1a\sinh(at)\quad(K=-a^2).\]
The Jacobi field with \(J(0)=J(L)=0\), \(J\not\equiv0\), detects a conjugate endpoint. On the round sphere, the first such point along a unit-speed geodesic from a point is its antipode at distance \(\pi R\). A flat cylinder has no conjugate points but can have multiple length-minimizing geodesics between some point pairs due to its quotient topology.

##### Exercises with answers

1. **Euclidean rays.** Solve \(j''=0\), \(j(0)=0\), \(j'(0)=\epsilon\). **Answer:** \(j(t)=\epsilon t\).
2. **Round sphere.** Solve \(j''+j/R^2=0\) for the same initial conditions. **Answer:** \(j(t)=\epsilon R\sin(t/R)\), zero again at \(t=\pi R\).
3. **Negative curvature.** Does \(j(t)=\sinh(at)/a\) become zero again for positive \(t\)? **Answer:** No. This model has no transverse focusing of this type.
4. **Global versus local.** Does the absence of conjugate points guarantee uniqueness of a shortest path? **Answer:** No. The flat cylinder supplies counterexamples.

##### Sources and further reading

- MIT OpenCourseWare, [18.950 Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/).
- J. D. Moore, [Lectures on Riemannian Geometry](https://web.math.ucsb.edu/~moore/riemanniangeometry.pdf).
- Supplement: [Jacobi field](https://en.wikipedia.org/wiki/Jacobi_field), [Cut locus](https://en.wikipedia.org/wiki/Cut_locus).

### Gauss–Bonnet: Curvature Counts Topology

**Track:** Topology and Geometry. **Background:** Riemannian surfaces, tangent spaces, differential forms, Euler characteristic. **Central question:** why does adding curvature over an entire surface recover a topological invariant?

#### Mathematical companion (not spoken)

Let M be a compact oriented two-dimensional Riemannian manifold with piecewise smooth boundary \(\partial M\). With the induced positive boundary orientation, Gaussian curvature K, signed geodesic curvature \(k_g\), and signed exterior turns \(\theta_j\) at corners, **Gauss–Bonnet** is
\[\int_M K\,dA+\int_{\partial M} k_g\,ds+\sum_j\theta_j=2\pi\chi(M).\]
For a closed surface, \(\int_M K\,dA=2\pi\chi(M)\). A closed connected orientable genus-g surface has \(\chi(M)=2-2g\).

**Geodesic triangle:** with interior angles \(\alpha,\beta,\gamma\) and geodesic sides,
\[\int_T K\,dA=\alpha+\beta+\gamma-\pi.\]
**Sphere:** \(K=R^{-2}\), \(\operatorname{Area}(S_R^2)=4\pi R^2\), so \(\int K=4\pi=2\pi\chi(S^2)\). **Flat disk:** \(K=0\) and \(k_g=1/R\), so \(\int_{\partial D_R}k_g ds=2\pi\). **Torus:** \(\chi(T^2)=0\), so total signed curvature is zero for every smooth metric.

Proof outline for closed M: triangulate into geodesic triangles. Summing the geodesic triangle angle excesses, every interior vertex contributes \(2\pi\), while each triangle contributes \(-\pi\). With \(3F=2E\), \(2\pi V-\pi F=2\pi(V-E+F)\). The general proof handles nongeodesic edges and boundary terms by geodesic curvature.

##### Exercises with answers

1. What is the total curvature of a genus-three closed orientable surface? **Answer:** \(2\pi(2-6)=-8\pi\).
2. Can a closed torus carry a metric of strictly positive Gaussian curvature? **Answer:** no; its total curvature must be zero.
3. Why is the planar disk not a counterexample to Gauss–Bonnet? **Answer:** the boundary geodesic-curvature integral contributes \(2\pi\).
4. What is the spherical angle excess of a unit-sphere octant geodesic triangle? **Answer:** \(\pi/2\), equal to its area.

##### Reading and source notes

- [UCLA, Math 120A geometry notes](https://math.ucla.edu/~sucharit/120A-notes.html), geodesic triangles and the global result.
- [Notre Dame, Euler Characteristic and Gauss–Bonnet lecture](https://sites.nd.edu/2023cmndthematicprogram/files/2023/06/lecture4-Lehmann-updated.pdf), boundary terms and triangulation proof.
- [MIT OpenCourseWare, Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/), manifold and curvature background.

### Gauss–Bonnet by Triangulation: From Angle Excess to Euler Characteristic

**Track:** Topology and Geometry. **Background:** Gaussian curvature, geodesics, triangles, Euler characteristic. **Central question:** how can a local curvature measurement determine a global integer?

#### Mathematical companion (not spoken)

For a geodesic triangle \(T\) on an oriented smooth Riemannian surface with interior angles \(\alpha,\beta,\gamma\),
\[\int_T K\,dA=\alpha+\beta+\gamma-\pi.\]
For a geodesic triangulation of a closed surface, \(\sum_T(\alpha_T+\beta_T+\gamma_T)=2\pi V\) and \(3F=2E\); hence \(\int_MK\,dA=2\pi V-\pi F=2\pi(V-E+F)=2\pi\chi(M)\).

For an oriented compact surface with piecewise smooth boundary, a compatible sign convention yields
\[\int_M K\,dA+\int_{\partial M}k_g\,ds+\sum_j(\pi-\alpha_j)=2\pi\chi(M),\]
where \(\alpha_j\) are the interior corner angles and the positive boundary orientation keeps the surface on the left. On a Euclidean unit disk \(K=0\), \(k_g=1\), so \(\int_{\partial D}k_g ds=2\pi\). For a closed genus-g oriented surface, \(\chi=2-2g\).

##### Exercises with answers

1. **Spherical octant.** Compute the angle excess of a triangle with three right angles. **Answer:** \(3\pi/2-\pi=\pi/2\).
2. **Count.** A geodesic triangulation of a closed surface has \(V=12,E=30,F=20\). What is \(\int K\,dA\)? **Answer:** \(2\pi(12-30+20)=4\pi\).
3. **Torus.** Must a torus with nonflat metric have curvature zero everywhere? **Answer:** No. Its total integrated curvature is zero.
4. **Flat disk.** Where is the missing \(2\pi\) if \(K=0\)? **Answer:** In the turning of the boundary curve or its corners.

##### Sources and further reading

- University of Notre Dame, [Euler characteristic and Gauss–Bonnet lecture](https://sites.nd.edu/2023cmndthematicprogram/files/2023/06/lecture4-Lehmann-updated.pdf).
- MIT OpenCourseWare, [18.950 Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/).
- Overviews: [Gauss–Bonnet theorem](https://en.wikipedia.org/wiki/Gauss%E2%80%93Bonnet_theorem), [Euler characteristic](https://en.wikipedia.org/wiki/Euler_characteristic).

### Degree Theory, Brouwer Fixed Points, and Global Constraints

**Track:** Topology and Geometry. **Background:** homology, continuous maps, orientation, the sphere and disk. **Central question:** how can a map's algebraic winding force it to attain a value?

#### Mathematical companion (not spoken)

For n>=1, \(\widetilde H_n(S^n;\mathbf Z)\cong\mathbf Z\). The induced map of continuous \(f:S^n\to S^n\) is multiplication by \(\deg(f)\in\mathbf Z\). Degree is homotopy invariant and multiplicative under composition. For n=1, the map \(z\mapsto z^m\) has degree m. Reflection in a hyperplane has degree -1; the antipodal map has degree \((-1)^{n+1}\).

If f is smooth and y a regular value, \(\deg f=\sum_{x\in f^{-1}(y)}\mathrm{sign}\det(Df_x)\) relative to chosen orientations. This sum is finite for maps between compact manifolds of the same dimension. If \(\deg f\ne0\), f is onto, because \(S^n\setminus\{y\}\) has trivial degree-n homology.

**Brouwer's theorem:** every continuous \(F:D^n\to D^n\), n>=1, has a fixed point. For n>=2, if there were none, the ray from F(x) through x determines a continuous retraction r:D^n->S^{n-1}. Since inclusion i:S^{n-1}->D^n satisfies r o i=id, reduced \(H_{n-1}\) would imply id=0. For n=1 the same proof uses reduced \(\widetilde H_0(S^0)\cong\mathbf Z\). The continuous ray construction requires F(x) different from x everywhere and uses compactness of D^n.

##### Exercises with answers

1. What is the degree of z->z^5 on S^1? **Answer:** 5.
2. Can a degree minus two map S^2->S^2 omit a point? **Answer:** no; every nonzero-degree map is surjective.
3. Can a disk deformation retract onto its boundary? **Answer:** no; the induced homology map would give identity=zero.
4. Does Brouwer's theorem imply iteration x_{k+1}=F(x_k) converges? **Answer:** no; existence of a fixed point is not a convergence theorem.

##### Reading and source notes

- [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), degree, homology and the Brouwer fixed-point theorem.
- [University of Chicago topology notes](https://math.uchicago.edu/~may/REUDOCS/06-25-2015.pdf), a disk retraction argument for Brouwer's theorem.

### Regular Values and Degree: Counting Solutions with Signs

**Track:** Topology and Geometry. **Background:** derivatives and Jacobian determinants, orientation, homology of spheres, smooth maps. **Central question:** how can counting the preimages of one ordinary point reveal a global property of a map?

#### Mathematical companion (not spoken)

For a smooth map \(f:M^n\to N^n\) between connected closed oriented smooth n-manifolds and a regular value \(y\in N\),
\[\deg(f)=\sum_{x\in f^{-1}(y)}\operatorname{sgn}\det(Df_x).\]
The sum is finite by compactness. The equivalent homological definition is \(f_*[M]=\deg(f)[N]\). Hence degree is homotopy invariant and \(\deg(g\circ f)=\deg(g)\deg(f)\). Nonzero degree implies surjectivity. Smooth maps have sufficiently many regular values by Sard's theorem; for the degree count, smoothness avoids technical differentiability thresholds.

For \(f_m:S^1\to S^1\), \(z\mapsto z^m\), \(m\in\mathbf Z\setminus\{0\}\), every target has \(|m|\) preimages, each with local degree \(\operatorname{sgn}(m)\); thus \(\deg f_m=m\). For a smooth function \(h(x,y)=x^2+y^2\), \(1\) is a regular value and \(h^{-1}(1)=S^1\), while \(0\) is critical. Brouwer's theorem follows because a retraction \(r:D^2\to S^1\) would induce \(r_*\circ i_*=\mathrm{id}\) on \(H_1(S^1)=\mathbf Z\), yet \(H_1(D^2)=0\).

##### Exercises with answers

1. **Power map.** Compute the degree of \(z\mapsto z^{-3}\) on \(S^1\). **Answer:** \(-3\).
2. **Regular value.** Is zero a regular value of \(x^2+y^2\)? **Answer:** No; the gradient vanishes at its only preimage.
3. **Existence.** If \(\deg f=5\) for a map of connected closed oriented n-manifolds, may f omit a target point? **Answer:** No, because degree is nonzero.
4. **Fixed points.** Which homology group obstructs a retraction of the disk onto its circle boundary? **Answer:** \(H_1(S^1)=\mathbf Z\), since \(H_1(D^2)=0\).

##### Sources and further reading

- Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), degree and homological fixed-point obstructions.
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), regular values and Sard's theorem.
- Overviews: [Degree of a continuous mapping](https://en.wikipedia.org/wiki/Degree_of_a_continuous_mapping), [Regular value theorem](https://en.wikipedia.org/wiki/Preimage_theorem).
