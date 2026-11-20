# A Surface Has Many Maps: Charts, Tangents, and Differentials

**Track:** Topology and Geometry  
**Lecture:** 051000  
**Preparation:** Vectors, partial derivatives, the chain rule, and elementary topology.  
**Companion:** Parametric and implicit tangent planes, change of coordinates, and derivative of height on a sphere.

<!-- BEGIN SPOKEN LECTURE -->

A globe maker has a problem that a person drawing a map of a city does not. Every flat map of the whole Earth must either distort some measurements, overlap itself, or tear the surface along a seam. Yet someone walking on the Earth can always make a small enough map of the neighborhood around them. This is the organizing idea of a smooth surface: locally, a surface looks like a piece of the plane, even when no single planar coordinate system describes it globally.

There are two reasons to be careful about that word locally. One is topological. A sphere, a torus, and an infinitely extending plane have different global shapes, even though a small neighborhood around any ordinary point resembles a disk. The second is differential. We want coordinate maps that are not just continuous, but differentiable, so we can ask about velocity, tangent directions, gradients, and the way distances change.

We'll build a working surface calculus through explicit examples. The sphere will be our companion, along with a graph, a torus, and a surface that looks like it ought to exist smoothly but fails at one point.

## How to draw a surface without drawing all of it

In three-dimensional Euclidean space, a surface patch can be described by a vector-valued map X of two parameters, u and v. It assigns to each pair a point in space with three coordinates. For the patch to be regular, the two derivative vectors X sub u and X sub v must be linearly independent. Imagine drawing a tiny square in the parameter plane. The derivative vectors describe the two edges of its image as a tiny parallelogram on the surface. If those vectors collapse onto one direction, the small square has lost a dimension, and the coordinates are failing to describe a regular patch.

The simplest example is a graph: z equals f of x and y. Choose u equal to x and v equal to y. Then X of u,v has coordinates u, v, and f of u,v. The first partial derivative is the vector one, zero, f sub u; the second is zero, one, f sub v. These are independent for every differentiable f, because the first two components already distinguish them. A smooth graph is always a regular patch, no matter how steep its local slopes become.

At a point on that graph, the tangent plane is the plane through the point spanned by those two vectors. If a traveler moves a small amount du in one parameter direction and dv in the other, the first-order displacement in space is approximately X sub u times du plus X sub v times dv. This is the surface version of linear approximation. The actual surface curves away from the tangent plane, but to first order the tangent plane is its best linear model.

Take the graph z equals x squared plus y squared. At the origin, both partial derivatives of f vanish, so the tangent plane is horizontal. At the point where x is one and y is zero, the tangent vectors become one, zero, two and zero, one, zero. One direction now slopes uphill, while the perpendicular parameter direction is level. We can already tell which small movements change height without computing the length of any path.

## What fails at the poles

For a sphere of radius R, a familiar parametrization uses a colatitude angle theta measured down from the north pole and a longitude angle phi. The coordinates are R sine theta cosine phi, R sine theta sine phi, and R cosine theta. Away from the poles, changing theta moves north or south and changing phi moves east or west.

At the north pole, theta is zero. Every longitude gives exactly the same point. Worse, the derivative in the phi direction is the zero vector there. This coordinate system fails the independence requirement. But the sphere itself is not singular at the pole. We can instead solve locally for z as the positive square root of R squared minus x squared minus y squared and use x and y as coordinates near the north pole. This graph patch is perfectly regular there.

One chart has failed. Another chart has succeeded. The surface has not changed. This is why manifolds are built with an atlas of overlapping coordinate charts rather than one set of global coordinates.

On an overlap, the coordinate transition map tells us how to convert one pair of local numbers into another. For smooth calculus to make sense, these transition maps must be smooth with smooth inverses. The derivative of a transition map changes the numerical components of a tangent vector, but it does not change the underlying geometric tangent direction. We will see this explicitly soon.

## A second way to specify the surface

Instead of parametrizing all points, we can specify an equation. A sphere satisfies x squared plus y squared plus z squared equals R squared. Write F of x,y,z for the left side minus R squared. The sphere is the zero level set of F.

If a differentiable curve gamma remains on the surface, then F of gamma of t is always zero. Differentiate using the chain rule. The gradient of F dotted with gamma prime must equal zero. So every tangent velocity is perpendicular to the gradient of F. If that gradient is nonzero, the implicit function theorem guarantees that the level set is locally a smooth surface, and the tangent plane consists of all vectors perpendicular to the gradient.

For the sphere, the gradient is twice the position vector. Therefore the tangent plane at the point p consists of all vectors v whose dot product with p is zero. At the north pole, p is zero, zero, R. The tangent vectors have zero z component: the plane is horizontal, just as the graph chart predicted. At the point R, zero, zero, the tangent vectors have zero x component, so the tangent plane is vertical.

The implicit and parametric approaches agree because they describe the same geometry. They offer different practical advantages. A parametrization gives convenient coordinates and tangent directions. An equation gives a quick normal vector and can make geometric constraints easier to recognize.

The gradient condition really matters. Consider the cone defined by z squared equals x squared plus y squared. Away from the origin, it consists of regular surface points. At the origin, the gradient of the defining function vanishes. The cone has a pointed tip and no unique tangent plane there. This is not merely a bad choice of longitude. The object genuinely fails to be a smooth surface at that point. A vanishing gradient alone does not always prove singularity, because one equation may be a poor defining function, but the cone gives a genuine example of a singular level set.

## Tangent vectors do not need an ambient arrow

The picture of arrows lying in three-dimensional space is helpful, but a manifold may not come with any preferred ambient space. We can define a tangent vector intrinsically as the velocity of a smooth curve passing through a point, with different curves identified when they have the same first-order effect on smooth coordinate functions. Equivalently, it is a linear rule that differentiates smooth functions and obeys the product rule.

Take a curve on a sphere. Its velocity vector in ordinary space is perpendicular to the radius. If we only had local latitude and longitude coordinates, we could instead record how quickly the two coordinates changed. These two coordinate rates are the components of the tangent vector in that chart. Both descriptions represent the same first-order motion.

Suppose the coordinates q change to new coordinates r by a smooth transition map. The velocity in r coordinates is the Jacobian of the transition map multiplied by the velocity in q coordinates. This is just the multivariable chain rule. A tangent vector is not one fixed list of numbers; it is a geometric object whose lists of components must change together under a chart change.

This matters whenever geometry is computed in more than one coordinate system. A vector that looks like the pair one, zero in one chart may have two nonzero components in another. Declaring them different vectors because their component lists differ would be like saying a distance has changed because we switched from meters to feet.

## Differentiating a function on a surface

Let h assign a real number to each point on a surface. Its differential at p is a rule that takes a tangent vector and returns the instantaneous change of h in that direction. If gamma passes through p with tangent v, then the differential of h applied to v is the derivative of h of gamma at that instant. In coordinates, this is the ordinary gradient of the coordinate expression dotted with the coordinate velocity. The numerical gradient components depend on the coordinates, but the final directional derivative does not.

For a concrete example, let h be height above the equatorial plane on a sphere. In ambient coordinates, h is just z. At the point p equals R, zero, zero, consider the tangent velocity zero, zero, one. The rate of change of height is one. That makes sense: this direction initially moves straight toward higher altitude.

At the north pole, however, every tangent vector is horizontal. The rate of change of height is zero in every tangent direction. The north pole is a critical point of the height function. It has maximum height R, but our conclusion did not require any coordinate formula for latitude. We only used the tangent plane.

There is a useful distinction between the differential and the gradient. The differential takes a direction and returns a number without requiring a notion of length. To define a gradient as a tangent vector, we need an inner product on tangent vectors: the gradient is the unique tangent vector whose inner product with any v reproduces the differential applied to v. On a sphere using the ambient Euclidean metric, the surface gradient of height is the ambient vertical unit vector with its component normal to the sphere removed. At p it is the vertical vector minus z divided by R squared times p. At the poles this becomes zero, and at the equator it becomes the vertical vector.

This is an early example of how the surface's metric changes the meaning of a familiar calculus construction. Differentiation comes first; turning the resulting differential into a gradient requires a ruler.

## The torus and the limits of a picture

Consider a ring-shaped surface formed by revolving a circle of radius r around an axis at distance R, where R is greater than r. A point can be described with two angles. One runs around the large circle of the ring. The other runs around the small circular tube. The three coordinates are obtained by taking the distance R plus r cosine v from the axis, multiplying it by cosine u and sine u for the first two coordinates, and taking height r sine v.

The two parameter directions are independent everywhere when R exceeds r. This gives regular local coordinates, although the angles repeat periodically. There is no single open rectangular parameter patch that describes the whole torus one-to-one without identifying its edges. The periodic identification is part of its topology, not a calculus defect.

The sphere and torus are both smooth two-dimensional surfaces, yet their global arrangements differ. On the sphere, a closed loop can be continuously contracted to a point. On the torus, a loop that goes once through the hole cannot be contracted while remaining on the surface. Local tangent planes will not reveal that fact by themselves; it belongs to topology. This is why the two strands of the track, topology and differential geometry, need one another.

There is another global distinction. A sphere admits a consistent choice of outward normal at every point. A torus also admits a consistent normal. A Mobius strip, despite being locally a perfectly smooth surface with boundary, does not have a continuous globally consistent choice of one side. It is nonorientable. Nothing goes wrong with its tangent plane at an ordinary point; what fails is the attempt to make a compatible choice across all patches.

## From maps to geometry

We have built a surface in two interchangeable ways: as a regular parametrized patch or as a regular level set. We have defined tangent vectors as first-order motions, explained the change-of-coordinates rule, and differentiated functions without confusing their coordinate expressions with the functions themselves. We have also seen three different obstructions. A coordinate chart can fail at a perfectly smooth point, as at a sphere's pole. A surface can genuinely fail to be smooth, as at a cone's tip. And a smooth surface can fail to support one global coordinate or normal choice, as the torus and Mobius strip remind us in different ways.

Now the question changes. If two nearby tangent directions have different lengths, or meet at a certain angle, where do those measurements come from? We have been using the Euclidean dot product almost invisibly. The next tool is to turn that borrowed ruler into a mathematical object on the surface itself. From that ruler we will recover lengths, areas, and straightest paths, even when no external three-dimensional picture is available.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Regularity, tangent planes, and the chain rule

For a regular patch \(X:U\subset\mathbb R^2\to\mathbb R^3\), require
\(X_u\times X_v\neq0\). Then

\[
T_{X(u,v)}S=\operatorname{span}\{X_u,X_v\}.
\]

For a regular level set \(S=F^{-1}(0)\) with \(\nabla F(p)\neq0\),

\[
T_pS=\{v\in\mathbb R^3:\nabla F(p)\cdot v=0\}.
\]

For a smooth function \(h:S\to\mathbb R\),
\(dh_p:T_pS\to\mathbb R\) is the directional derivative; if
\(h\) extends to the ambient space, \(dh_p(v)=\nabla\bar h(p)\cdot v\).
A surface gradient requires a metric to identify \(dh_p\) with a vector.

### Explicit calculations

- Sphere of radius \(R\): \(F(x,y,z)=x^2+y^2+z^2-R^2\); \(T_pS^2_R=p^\perp\).
- Sphere height \(h(p)=p_z\): under the induced metric,
  \[\nabla_S h(p)=e_z-\frac{p_z}{R^2}p.\]
- Graph \(X(u,v)=(u,v,u^2+v^2)\): at \((1,0,1)\), tangent directions \((1,0,2)\) and \((0,1,0)\).
- Embedded torus \(X(u,v)=((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v)\), \(R>r>0\). The partial derivatives are orthogonal, with lengths \(R+r\cos v\) and \(r\), hence are independent.

### Exercises with answers

1. At \((0,R,0)\) on the sphere, describe the tangent plane. **Answer:** \(v_y=0\).
2. For the graph \(z=xy\), find the tangent plane at \((1,2,2)\). **Answer:** \(z-2=2(x-1)+(y-2)\).
3. Is \(z^2=x^2+y^2\) a regular smooth surface at the origin? **Answer:** No; the cone tip has no unique two-dimensional tangent plane.
4. At \((R,0,0)\) on the sphere, find the surface gradient of height. **Answer:** \((0,0,1)\).
5. If \(u=u(a,b)\) and \(v=v(a,b)\) are overlapping coordinates, how do their tangent components compare? **Answer:** The column of \((u,v)\) velocities equals the Jacobian \(D(u,v)/D(a,b)\) times the column of \((a,b)\) velocities; to go the other way use the inverse Jacobian.

### Reading

- MIT OCW 18.965, *Geometry of Manifolds* (`tg-mit-manifolds`).
- MIT OCW 18.950, *Differential Geometry* (`tg-mit-differential`).
- For further inverse/implicit-function and tensor arguments, `topology-geometry:008000`.
- Wikipedia overview: [Differentiable manifold](https://en.wikipedia.org/wiki/Differentiable_manifold).
