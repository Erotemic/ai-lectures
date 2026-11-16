# 014200 — Jacobi Fields: Curvature Seen Through Neighboring Geodesics

**Track:** Topology and Geometry. **Background:** covariant differentiation, geodesics, simple second-order differential equations. **Central question:** what does curvature do to paths that start close together?

<!-- BEGIN SPOKEN LECTURE -->

# Jacobi Fields: Curvature Seen Through Neighboring Geodesics

Imagine standing at the north pole of Earth with several companions. Everyone begins walking due south at the same constant speed, following a great circle. At first the group spreads out as the lines of longitude separate. Later the paths begin to draw together, and if everyone continues for half a circumference, they meet at the south pole.

On a flat plane, rays leaving a point at slightly different angles would keep moving apart. The contrast between these two experiences is an operational way to detect curvature. It does not require seeing the sphere from outside. It only requires observing neighboring shortest-path candidates.

## One path is not enough

A geodesic is a curve that carries its velocity parallel along itself. To see curvature, we need a family of geodesics, each with slightly different initial data. Picture a strip of paths with a parameter labeling which path we are on and a time parameter measuring progress along each path.

Choose a reference geodesic in the strip. A displacement vector tells us how a nearby geodesic moves relative to it when we change the path label slightly. This displacement along the reference path is called a Jacobi field. It is not an arbitrary vector field; it is obtained by differentiating a genuine variation through geodesics.

There are two accelerations to distinguish. One is the acceleration along an individual geodesic, which vanishes in the covariant sense. The other is the relative acceleration of neighboring geodesics, which generally does not vanish. Curvature controls the second.

## Where the Jacobi equation comes from

Covariant derivatives in two directions need not commute. Their failure to commute is measured by the Riemann curvature tensor. Apply that commutator to the two directions of the strip: one along the paths and one between them. Because every individual path is geodesic, much of the expression cancels. What remains is a differential equation for the displacement vector.

The equation says that the second covariant derivative of the displacement, along the reference path, is balanced by a curvature term involving the displacement and the path's velocity. It looks like the equation for a spring, except the strength and sign of the restoring term are supplied by the geometry.

We should not yet conclude that positive curvature always draws every pair of paths together. The equation acts on components transverse to the path, and the relevant curvature is sectional curvature in the plane spanned by the path direction and displacement. In higher dimensions different transverse directions may behave differently.

## Three model worlds

Begin in the Euclidean plane. Curvature is zero. The equation becomes the statement that relative acceleration vanishes. If two straight paths start at the same point with a small angular difference, their separation grows linearly with distance traveled. Double the travel time and, to first order in the initial angle, double their separation.

On a round sphere the transverse equation becomes the same kind of differential equation as a harmonic oscillator. With zero initial separation and unit initial separation rate, its solution grows like a sine. The separation first increases, reaches a maximum, then decreases to zero. It becomes zero again when the travel distance is half a great-circle circumference. That is the north-pole-to-south-pole experiment.

In a surface of constant negative curvature, the transverse equation instead has a solution growing like a hyperbolic sine. Nearby geodesics leaving a point diverge faster than linearly. This is not merely a drawing of a saddle-shaped surface: it is a quantitative prediction about intrinsic distances.

These are local, first-order comparisons of paths. They do not give an exact finite separation for arbitrarily far apart paths, and they do not by themselves classify the global topology.

## When local shortest paths stop being locally shortest

On the sphere, the convergence at the south pole has another meaning. Many geodesics connect the north pole to the south pole. Vary the initial direction and the endpoint does not change. The corresponding Jacobi field vanishes at both endpoints. The south pole is a conjugate point of the north pole along that great circle.

Conjugate points arise where a geodesic variation develops this degeneracy. They are related to the failure of a geodesic to remain locally minimizing beyond the first conjugate point. But two different global phenomena must not be merged. A geodesic can stop being globally shortest because another route becomes shorter before any conjugate point appears. Global minimizing can fail at the cut locus even when local second-variation behavior is still favorable.

For example, a flat cylinder has no intrinsic curvature and no conjugate points along its straight geodesics, but two points can have competing routes winding around opposite sides of the cylinder. That is a topological global effect, not a focusing effect of positive curvature.

## Why curvature is a tensor

A reader of geodesic equations may wonder why we introduce an elaborate four-index object when a surface has just one Gaussian curvature. In two dimensions there is indeed only one independent curvature function. In three or more dimensions, however, two different planes through the same tangent direction may bend differently.

The curvature tensor packages all those directional comparisons and behaves properly when we change coordinates. Christoffel symbols alone are not tensors, because part of their apparent change comes from how the basis moves. The combination of derivatives and products that defines curvature cancels those coordinate artifacts.

This is a general pattern in geometry. A coordinate expression may look complicated, while the geometric object it represents is simple to state: how much does transport fail to close, or how do nearby geodesics accelerate relative to each other?

## A bridge to analysis and topology

The Jacobi equation is a linear differential equation along a given geodesic. Existence and uniqueness are ordinary differential-equation ideas, and its zeros have geometric meaning. Later, second variation formulas will use the same fields to analyze stability and minimizing properties. Morse theory of the energy functional on path space also builds on conjugate points and variations of geodesics.

The lesson is that curvature is not just a number attached to a shape. It makes predictions about motion. Neighboring geodesics spread, focus, or remain proportionally separated according to the curvature they encounter. With that observation, the abstract curvature tensor becomes something one can test.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Adopt \(R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z\). For a unit-speed geodesic with tangent \(T\), a Jacobi field \(J\) derived from a variation through geodesics satisfies
\[\nabla_T\nabla_TJ+R(J,T)T=0.\]
In dimension two with \(J=jN\) normal to \(T\) and \(N\) parallel along the geodesic, \(j''+Kj=0\). If \(j(0)=0\), \(j'(0)=1\), then
\[j(t)=t\quad(K=0),\qquad j(t)=R\sin(t/R)\quad(K=1/R^2),\qquad j(t)=\frac1a\sinh(at)\quad(K=-a^2).\]
The Jacobi field with \(J(0)=J(L)=0\), \(J\not\equiv0\), detects a conjugate endpoint. On the round sphere, the first such point along a unit-speed geodesic from a point is its antipode at distance \(\pi R\). A flat cylinder has no conjugate points but can have multiple length-minimizing geodesics between some point pairs due to its quotient topology.

### Exercises with answers

1. **Euclidean rays.** Solve \(j''=0\), \(j(0)=0\), \(j'(0)=\epsilon\). **Answer:** \(j(t)=\epsilon t\).
2. **Round sphere.** Solve \(j''+j/R^2=0\) for the same initial conditions. **Answer:** \(j(t)=\epsilon R\sin(t/R)\), zero again at \(t=\pi R\).
3. **Negative curvature.** Does \(j(t)=\sinh(at)/a\) become zero again for positive \(t\)? **Answer:** No. This model has no transverse focusing of this type.
4. **Global versus local.** Does the absence of conjugate points guarantee uniqueness of a shortest path? **Answer:** No. The flat cylinder supplies counterexamples.

### Sources and further reading

- MIT OpenCourseWare, [18.950 Differential Geometry](https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/).
- J. D. Moore, [Lectures on Riemannian Geometry](https://web.math.ucsb.edu/~moore/riemanniangeometry.pdf).
- Supplement: [Jacobi field](https://en.wikipedia.org/wiki/Jacobi_field), [Cut locus](https://en.wikipedia.org/wiki/Cut_locus).
