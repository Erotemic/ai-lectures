# A Curve Carries a Clock: Arc Length, Curvature, and Turning

**Track:** Topology and Geometry  
**Lecture:** 050000  
**Preparation:** Derivatives, vectors, the chain rule, and the Euclidean plane.  
**Companion:** Parametrization invariance, signed curvature, turning, and the helix calculation.

<!-- BEGIN SPOKEN LECTURE -->

A road can be described by a map, by the distance traveled along it, or by the instructions a driver receives from the steering wheel. These are not three versions of the same information. The map locates points. The distance supplies a ruler. The steering wheel responds to the way the road bends. The first step toward differential geometry is learning to keep these descriptions separate, and then discovering how to reconstruct one from another.

A curve is a simple place to begin because we can see its geometry while carrying out nearly every calculation with elementary calculus. By the end we will have a measurement of turning that does not depend on how fast we travel. We will also discover why bending a line into a circle changes something that an inhabitant of that one-dimensional line cannot measure using distances alone.

## The path and its clock

Write a plane curve as a vector-valued function gamma of t. For each value of the parameter t, gamma gives a point with an x coordinate and a y coordinate. The derivative gamma prime is the velocity, and its length is the speed. If the velocity is not zero, we call the parametrization regular there. That last condition lets us identify a definite direction along the curve.

Consider a circle of radius three. One description is x equals three cosine t, y equals three sine t. Over one full revolution, t runs from zero to two pi. Its velocity has components negative three sine t and three cosine t. The speed is constantly three. But nothing in the circle requires us to move that quickly. We could let t equal two times a new parameter, or a smoothly varying function of that parameter. As long as the change of parameter is locally invertible, we trace the same geometric curve with a different clock.

Under a new parameter u, the chain rule multiplies the velocity by the derivative of t with respect to u. The speed is multiplied by the absolute value of that derivative. So speed is generally not a property of the unparametrized curve. It is a property of the curve together with a chosen clock.

A subtlety appears when the new clock comes to a halt. Suppose a straight line is described by gamma of t equals the point whose coordinates are t cubed and zero. The image is still the horizontal line, but the velocity vanishes at t equals zero. The geometric line has no corner there; the parametrization has introduced an artificial failure of regularity. When we derive geometric formulas, we should not mistake that failure for a feature of the line.

## The clock that measures distance

There is one particularly useful parameter: distance traveled along the curve. Between two parameter values, approximate the curve by many short straight segments. A small change in the position is approximately the velocity times the change in time. Adding the lengths and taking a limit gives the arc-length integral: integrate the speed over the parameter interval.

For our radius-three circle, the speed is three. One revolution has length three times two pi, or six pi. This calculation has a second virtue. Under a smooth monotone reparametrization, the change in speed is canceled by the corresponding change in the integration variable. The arc length does not care which admissible clock we chose.

Starting from a point on a regular curve, define s of t to be the arc length accumulated since that point. Its derivative is the positive speed. Because this derivative is nonzero, we can locally invert s and use distance itself as the parameter. The resulting curve has unit speed: one unit of the parameter corresponds to one unit of length. This is called arc-length parametrization. It often makes geometry simpler because the tangent vector now has length one automatically.

The word locally is important. A closed circle is periodic, so there is no globally one-to-one distance coordinate on it. We can still use arc length around the circle, but the coordinate repeats after the circumference. Differential geometry works with local coordinates precisely because global coordinates may be obstructed by the shape of the object.

## Turning without reference to speed

Imagine following a regular plane curve with a compass needle always pointing in the direction of travel. Its unit tangent vector is velocity divided by speed. For a unit-speed curve, this tangent already has length one. Therefore differentiating its squared length gives zero: the dot product of the tangent with its derivative is zero. In the plane, the derivative of the unit tangent must point perpendicular to the tangent. It measures turning, not speeding up.

The magnitude of the change in tangent per unit arc length is the curvature. Zero curvature means that the tangent direction is not changing, so a connected regular unit-speed segment with zero curvature is part of a straight line. High curvature means that a small amount of travel produces a large change in direction.

A circle of radius R offers a useful calibration. Travel one unit of arc length and the central angle changes by one divided by R radians. Its unit tangent rotates by exactly the same angle. So the circle's curvature is one divided by R. A big circle turns gently; a small circle turns sharply. This is why we describe curvature as an inverse length.

When a plane has a chosen orientation, we can distinguish turning left from turning right. Rotate the unit tangent counterclockwise through ninety degrees to obtain its unit normal. There is then a signed curvature k such that the derivative of the unit tangent with respect to arc length equals k times that normal. Reversing the direction of travel changes the sign of signed curvature, as does reflecting the plane. Its magnitude does not depend on which way we travel.

The signed formula is worth understanding rather than memorizing. If gamma has coordinates x of t and y of t, its signed curvature is x prime times y double prime minus y prime times x double prime, divided by speed cubed. The numerator is a two-dimensional determinant: it measures the part of acceleration perpendicular to velocity, with a sign for the turning direction. Dividing by speed cubed removes the clock dependence. It is the same geometric idea as unit-tangent differentiation, written in a parameter we may find easier to use.

## A parabola under the microscope

Take the parabola y equals x squared, parametrized by x equals t and y equals t squared. Its velocity is the vector one, two t. Its acceleration is zero, two. The determinant of velocity and acceleration is two. The speed squared is one plus four t squared. Consequently, the curvature is two divided by one plus four t squared, raised to the three-halves power.

At the vertex, t equals zero, so the curvature is two. Move to the point where t equals one, and the curvature falls to two divided by five to the three-halves, a little below one fifth. This matches the picture: the bottom of the parabola bends more abruptly, while the arms become flatter.

Near a point of nonzero curvature, a circle can closely approximate the curve's position, tangent direction, and second-order turning. Its radius is the reciprocal of the curvature magnitude. At the vertex of our parabola, the approximating circle has radius one half. Because the parabola bends toward increasing y there, the center of that circle is half a unit above the vertex. This is the osculating circle. It captures not just where the curve is or which way it points, but the local rate at which it is turning.

There is a common trap here. Curvature is not simply the second derivative of y with respect to x. That second derivative equals two everywhere for this parabola. But the geometric turning depends on the slope as well, because a fixed change in x represents different amounts of travel along different portions of the curve. The denominator in the curvature formula performs exactly that correction.

## A curve can leave the plane

Now suppose the road climbs upward while circling a tower. Write a helix with radius R and rise parameter a: its coordinates are R cosine t, R sine t, and a t. When t increases by a full revolution, the height increases by two pi a. Its speed is the constant square root of R squared plus a squared.

The helix's curvature is R divided by R squared plus a squared. If a equals zero, it is a circle, and the formula becomes one over R. As a grows, the helix becomes less sharply bent even though its horizontal projection keeps the same radius. The climb spreads the turn over a greater length of road.

Three-dimensional curves have another local feature: how their bending plane twists. Provided curvature is nonzero, take the unit tangent, the principal normal pointing toward the change in tangent, and the binormal perpendicular to both. Their evolution is described by the Frenet equations. The coefficient governing rotation out of the current bending plane is torsion. With the conventional orientation, the helix has torsion a divided by R squared plus a squared. A planar curve with nonzero curvature has zero torsion. Curvature says how much the road turns; torsion says how its plane of turning twists.

Torsion requires a little more care than curvature. At a point where curvature vanishes, the principal normal and binormal may not be defined. The path itself is not necessarily singular. We have simply chosen a geometric frame that depends on having a preferred bending direction. This is a recurring theme in geometry: a formula may fail because its chosen coordinates or frame fail, rather than because the underlying object fails.

## Turning all the way around

A surprisingly global quantity comes from adding local turning. On a plane curve, signed curvature times an infinitesimal arc length equals the infinitesimal change in the tangent's angle. Thus the integral of signed curvature is the total change in tangent direction, measured continuously rather than resetting the angle after every revolution.

For a counterclockwise circle, the tangent makes one full turn, so the integral equals two pi. For a simple smooth closed plane curve traversed counterclockwise, the same total is two pi even if the curve is almost rectangular in some regions and nearly flat in others. That is the turning-tangent theorem. It links a local derivative to a global winding number.

If a closed curve crosses itself, the total signed turning can be a different integer multiple of two pi, including zero. If we instead integrate the absolute curvature, left and right turns stop canceling. We must distinguish accumulated bending from net winding. These are different measurements, and both can be useful.

## What a one-dimensional inhabitant can know

Imagine two very thin flexible wires, one straight and one bent into a gentle arc. Mark off equal distances along them. An ant living on either wire can measure the distance between nearby points by following the wire and can locally tell that the length rule is the same. Without seeing the surrounding plane, it cannot detect from that one-dimensional metric alone whether the wire is straight or curved. Curvature of a curve in a plane is extrinsic: it refers to how the curve sits inside a larger space.

This is not the conclusion for surfaces. A two-dimensional inhabitant can arrange triangles, compare small circles, and detect certain kinds of curvature without looking into an ambient third dimension. The difference is one of the central discoveries of differential geometry.

Our first toolkit is now complete. A parametrization supplies a clock; speed supplies a distance ruler; arc length removes the arbitrary clock; curvature measures turning per unit distance; torsion adds twisting in three dimensions. These quantities are not merely names. We have computed them on a circle, a parabola, and a helix, and we know which aspects survive a change of parameter. That is the right foundation for asking what changes when the object is not a curve but a surface.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Definitions and formulas

For a regular curve \(\gamma:I\to\mathbb R^n\),

\[
L(\gamma|_{[a,b]})=\int_a^b\|\gamma'(t)\|\,dt,
\quad T=\frac{\gamma'}{\|\gamma'\|},
\quad \kappa=\left\|\frac{dT}{ds}\right\|.
\]

For a regular plane curve, with the plane orientation fixed,

\[
\kappa_{\rm signed}(t)=\frac{x'(t)y''(t)-y'(t)x''(t)}{(x'(t)^2+y'(t)^2)^{3/2}}.
\]

For a space curve where \(\gamma'\times\gamma''\ne0\),

\[
\kappa=\frac{\|\gamma'\times\gamma''\|}{\|\gamma'\|^3},\qquad
\tau=\frac{\det(\gamma',\gamma'',\gamma''')}{\|\gamma'\times\gamma''\|^2}.
\]

For the helix \(\gamma(t)=(R\cos t,R\sin t,at)\), \(R>0\),
\(\kappa=R/(R^2+a^2)\) and \(\tau=a/(R^2+a^2)\).

### Worked proofs

1. **Parameter independence of length.** If \(t=h(u)\) is a smooth monotone bijection with nonzero derivative, then \(\|d\gamma(h(u))/du\|=\|\gamma'(h(u))\|\,|h'(u)|\). Change variables in the integral.
2. **Why the denominator is speed cubed.** Write \(v=\|\gamma'\|\), \(T=\gamma'/v\), and use \(dT/ds=(1/v)d(\gamma'/v)/dt\). Taking its oriented component along the ninety-degree rotation of \(T\) yields the determinant formula.
3. **The planar turning formula.** Locally write \(T=(\cos\theta,\sin\theta)\). Then \(dT/ds=\theta'(s)(-\sin\theta,\cos\theta)\), so \(\kappa_{\rm signed}=\theta'(s)\). A global closed-curve turning claim additionally uses the turning-number theorem.

### Exercises, with answers

- For \(\gamma(t)=(t,t^2)\), compute the osculating-circle radius at \(t=0\). **Answer:** \(1/2\).
- For \(\gamma(t)=(a\cos t,b\sin t)\), \(a,b>0\), find curvature at \(t=0\). **Answer:** \(a/b^2\). At \(t=\pi/2\) it is \(b/a^2\).
- Does \(\gamma(t)=(t^3,0)\) have zero curvature at \(t=0\) according to the regular-curve formula? **Answer:** The formula is undefined there because \(\gamma'(0)=0\); the underlying line is smooth and admits a regular parametrization with zero curvature.
- Find the rise after one turn of the helix and describe its torsion when \(a=0\). **Answer:** Rise \(2\pi a\); torsion zero for its planar circle.

### Reading

- MIT OpenCourseWare, *18.950 Differential Geometry* (`tg-mit-differential`): classical differential geometry of curves and surfaces.
- UCLA Math 120A notes (`tg-ucla-gauss`): surface curvature and local geometric calculation.
- Existing deeper lecture `topology-geometry:014000` studies intrinsic curvature and the Gauss--Bonnet theorem.
- Wikipedia overview: [Curvature](https://en.wikipedia.org/wiki/Curvature).
