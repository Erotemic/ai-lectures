# 015000 — Integrating Along Curves: Contours, Primitives, and Holes

**Track:** Analysis from First Principles. **Background:** parametrized curves, real integration, complex derivatives, and the punctured plane. **Theme:** complex line integrals combine ordinary one-variable integration with topology; the existence of an antiderivative is the decisive path-independence condition.

<!-- BEGIN SPOKEN LECTURE -->

# Integrating Along Curves: Contours, Primitives, and Holes

Imagine walking from one point in a city to another. If you care only about the endpoints, you might record the change in your horizontal coordinate or the change in your altitude. You could take ten different streets and obtain the same net change. If you instead measure work done against a force field, the streets you choose may matter. A route that loops around a source of circulation can produce a different total from a direct route.

Complex integration has the same tension. Some complex-valued functions admit integrals that depend only on where a path begins and ends. Others produce a nonzero integral even when the path returns to its starting point. Both situations occur for perfectly continuous functions, and even for functions that possess complex derivatives at every point where they are defined.

Our goal is to make these statements precise without assuming a complex integration theory in advance. The definition uses a familiar tool: ordinary integration with respect to a real parameter. We will calculate a simple circle integral exactly. Then we will see why its value changes the meaning of an antiderivative and why a missing point in the plane can matter more than the local smoothness of the function.

## Replacing a curve by a journey through time

A curve is a continuous path in the complex plane described by a complex-valued function of a real parameter. Imagine the parameter as time. The position at time t is gamma of t. When gamma is differentiable, its derivative is the instantaneous velocity vector of the moving point, interpreted as a complex number.

A contour, for our purposes, is a piecewise continuously differentiable curve with an orientation. Piecewise means we may pass through a finite collection of corners, as we do along the edges of a triangle or a rectangle. Orientation means the direction of traversal is part of the data. Walking around the same geometric loop in reverse will reverse the sign of the integral.

Suppose f is continuous on the image of the contour. We define its complex contour integral by integrating, over the real parameter, the product of f evaluated at the current position and the derivative of the position. Because that product is complex-valued, we may integrate its real and imaginary parts separately using ordinary real integrals.

This definition is simpler than it may sound. The factor f describes what we sample along the path. The velocity factor keeps track of how the path moves through the plane. Without the velocity factor, we would merely average function values over time and obtain a quantity that could depend on how quickly we walked. With the velocity factor, a suitable change of parameter leaves the integral unchanged as long as we preserve direction.

Try a straight segment from zero to one plus i. The simplest parametrization is t times one plus i, with t running from zero to one. Its velocity is the constant one plus i. For the constant function f equal to one, the integral is the displacement one plus i. The curve could have bent in the middle, but the integral of the constant function would still equal the final position minus the initial position, because the integrand is the derivative of the position.

That suggests an important idea: a function whose values represent a complex derivative should behave like a rate of change. Integrating that rate along a path ought to recover the difference in its underlying quantity. We will make that idea a theorem in a moment.

## Three rules worth deriving

First, concatenation. Walk one curve and then a second, where the endpoint of the first matches the start of the second. The integral over the entire route is the sum of the two integrals. This follows by splitting the real parameter interval into two pieces. A polygon is therefore no harder in principle than its individual straight edges.

Second, reversal. Walk the same curve backward. Under the reverse parametrization, the velocity changes sign. The integral changes sign too. Consequently, if you travel along one edge and immediately return along that very edge, the contributions cancel.

Third, a bound. Suppose the modulus of f never exceeds some number M along the curve. Each infinitesimal contribution has modulus at most M times the speed of the curve. Adding these contributions and applying the triangle inequality shows that the modulus of the entire integral is at most M times the length of the curve. This is often called the M L estimate, for maximum magnitude times length.

The estimate is more than a convenient numerical inequality. It will be the workhorse in proofs where we shrink a circle or a triangle. If a curve gets short while the function stays bounded along it, its integral gets small. If the function grows, we need a more careful balance between the growth and the length.

For example, if f is bounded by three on a circle of radius two, that circle has length four pi, so the modulus of the integral is at most twelve pi. The inequality does not claim the integral actually reaches this bound. Cancellation from changes of direction may make it much smaller or even zero.

## The complex fundamental theorem along a path

Suppose F is holomorphic on an open region containing the path and that its complex derivative equals f there. We call F a primitive, or antiderivative, of f. Apply the real-variable chain rule to the composition of F with the moving position gamma. Its derivative with respect to time is the complex derivative of F at gamma times gamma prime. This is exactly the integrand in our contour-integral definition.

The real Fundamental Theorem of Calculus, applied to the real and imaginary components, therefore gives a compact answer: the integral of f along the curve equals F at the endpoint minus F at the starting point.

The proof works regardless of how the path bends. Once we have a primitive on a region containing the path, the integral depends only on endpoints. In particular, the integral around every closed contour in that region is zero.

Consider f of z equal to two z. Its primitive is z squared. So the integral from a point a to a point b is b squared minus a squared. Whether the curve moves in straight lines, circles, or a complicated route does not matter, provided the route lies in the domain of the primitive.

This endpoint rule is familiar, but we should not assume it applies to every continuous f. It has a hypothesis: the existence of a holomorphic primitive. Real one-dimensional calculus can obscure this issue because a continuous function on an interval always has an antiderivative. In the complex plane, a continuous function on an open set need not be holomorphic, and even a holomorphic function can fail to have a single-valued primitive on a region with holes.

## The circle that refuses to vanish

Let us compute the pivotal example. Take f of z equal to one divided by z. This function is complex differentiable at every nonzero point. Its derivative is negative one divided by z squared. We avoid the origin entirely.

Walk counterclockwise once around the unit circle. At time t, with t running from zero to one full turn, the position is cosine t plus i sine t, equivalently the exponential of i t. The velocity is i times the current position. The value of f at that position is the reciprocal of the position.

Multiplying the sampled value by the velocity produces something wonderfully simple: the position cancels, leaving the constant i. Integrate i for one full turn and the result is two pi times i. The contour is closed, and yet the integral is not zero.

This cannot be an arithmetic accident. If the reciprocal function had a holomorphic primitive defined on the entire punctured plane, our endpoint theorem would make every closed integral zero. We have just calculated a closed integral equal to two pi i. Therefore no such global primitive exists.

We did not find a failure of holomorphicity on the punctured plane: one divided by z is holomorphic everywhere in that domain. The obstruction is topological. The unit circle encloses a point missing from the domain, a point at which the function is undefined. The curve cannot be contracted to a point within the punctured plane without crossing the missing origin.

An ordinary-looking integral has detected a hole.

If we travel around the circle twice counterclockwise, we obtain four pi i. If we travel once clockwise, we obtain negative two pi i. If we take a circle that does not enclose the origin, lying in a disk that avoids zero, we can choose a suitable local logarithm as a primitive and get zero. The integral is responding not just to the geometry of the path but to how it winds around the excluded point.

## Why an angle cannot be chosen around the whole circle

Recall that a nonzero complex number has a length and an angle. Along a continuously traversed path that avoids zero, we can keep a continuous running total of the angle, even when that total exceeds a whole turn. This is sometimes called an unwrapped angle. The initial and final points of a closed loop may coincide, while the unwrapped angle has increased by one or several complete turns.

The reciprocal integrand is closely related to the differential of a logarithm. Locally, the real logarithm of the radius changes with radial motion, while the imaginary part tracks change in angle. Along a closed loop, the starting and ending radii match, so their logarithms cancel. The net change in the unwrapped angle remains. It must be an integer multiple of a full turn. That integer is the winding number of the curve around the origin.

For a piecewise smooth closed curve avoiding zero, the integral of one divided by z is two pi i times this integer. This is a precise relation, not merely a visual metaphor. A proof can be given by selecting a continuous angle along the parameter interval and integrating the radial and angular rates; the formal details are recorded in the companion.

The same idea explains the difficulty of defining a complex logarithm globally. A logarithm would need to assign a continuous angle, up to a multiple of a full turn, to every nonzero point. Going once around the origin changes the unwrapped angle by a full turn even though the point returns to where it started. A single-valued global logarithm cannot record both requirements without contradiction.

On a domain that removes a ray from the origin, however, we can choose a continuous range of angles. There the logarithm has a holomorphic branch, its derivative is one divided by z, and contour integrals of the reciprocal within that branch domain depend only on endpoints. Removing a ray is not magic; it prevents a loop from winding completely around the missing point while staying in the domain.

## Another surprise: the problem can be the function, not the hole

A nonzero closed contour integral does not always mean there is a topological hole. Consider instead the function f of z equal to the conjugate of z. This function is defined continuously on the entire complex plane, which has no holes. Walk counterclockwise around the unit circle. The conjugate of the position is the reciprocal of the position on the unit circle, so the same calculation gives an integral of two pi i.

What failed this time? The domain has no missing point. But conjugation is not holomorphic. We already saw that its difference quotients disagree by direction. There is no complex primitive whose derivative equals conjugation throughout the plane.

This pair of examples is a useful diagnostic. For one divided by z, the function is holomorphic wherever defined, but the chosen domain has a hole. For conjugation, the domain is simply connected, but the function is not holomorphic. In both cases the closed integral can be nonzero, and for different reasons.

It would therefore be wrong to declare that simply connected domains alone make all complex line integrals vanish. It would also be wrong to declare that holomorphicity alone makes all closed integrals vanish on any possible domain. Cauchy's theorem will tell us how these conditions cooperate.

## The exact equivalence behind path independence

There is a clean way to organize the logic. Work on a path-connected open domain, and suppose f is continuous there. Three conditions are equivalent.

First, f has a holomorphic primitive on the domain. Second, its contour integral between any pair of points is independent of the path connecting them within the domain. Third, its integral around every piecewise smooth closed contour in the domain is zero.

We already proved that a primitive implies path independence. Path independence implies zero around closed curves because a closed curve begins and ends at the same point. For the converse, suppose every closed integral vanishes. Choose a base point and define F at any other point by integrating f along any path from the base point to that point. The vanishing of closed integrals guarantees that two different paths give the same value, so F is well defined.

Why is F actually a primitive? Take a nearby point and connect it to the original point by a short straight segment inside a disk contained in the domain. The difference in the values of F is the integral of f along that segment. Divide by the complex displacement. Because f is continuous, the average value of f along that tiny segment approaches its value at the starting point. Thus the complex difference quotient for F tends to f. We have built a holomorphic primitive from the zero-integral condition.

That proof also shows what we cannot conclude from one or two convenient paths. To build a globally single-valued primitive by this method, we need all closed contour integrals to vanish, or a geometric theorem that implies that fact.

One such geometric theorem will come next. Holomorphic functions on disks have primitives. More generally, they do on suitable simply connected domains. A loop surrounding a hole is the place where this conclusion can fail, because it may not be deformable through the domain to a point.

## Why contour integration changes analysis

There is an apparent paradox in what we have done. The definition of a complex contour integral used nothing more exotic than an ordinary real integral with a parameter. Yet a circle integral can encode winding around a point. In a moment, Cauchy's theorem will tell us that holomorphicity can force huge families of these integrals to vanish. Then the Cauchy integral formula will use a single boundary integral to reconstruct the value of a function at an interior point.

That is the transition from familiar calculus to complex analysis. The domain is two-dimensional, so we can approach points from many directions and circulate around holes. The derivative is complex, so it has fewer allowable local forms than a general real derivative. The integral remembers the route, unless strong conditions cause the dependence to cancel.

Before using a contour theorem, ask four questions. Where is the function defined? Where is it holomorphic? Where does the contour travel, including its orientation? And what region, if any, is enclosed by that contour and included in the domain? Those questions are not legalistic additions to the mathematics; they determine whether an integral vanishes, measures winding, or is not even defined.

We have a concrete nonzero calculation, a useful estimate, and an exact criterion for path independence. The remaining task is to prove that holomorphic functions on the right regions satisfy that criterion. Cauchy's theorem will do this without assuming continuity of a second derivative, or even continuity of the first derivative. Its proof will reveal the strength of having one complex derivative in every direction.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Parametrization, length, and estimates

For a piecewise \(C^1\) contour \(\gamma:[a,b]\to U\subset\mathbb C\),
\[
\int_\gamma f(z)\,dz=\int_a^b f(\gamma(t))\gamma'(t)\,dt.
\]
The length is \(L(\gamma)=\int_a^b|\gamma'(t)|\,dt\). If \(|f|\le M\) along the image, \(\left|\int_\gamma f\,dz\right|\le ML(\gamma)\). Reversal negates the integral; concatenation adds integrals; orientation-preserving piecewise \(C^1\) reparametrization leaves it unchanged.

### Fundamental theorem of contour integration

If \(F\in\mathcal O(U)\) and \(F'=f\), then
\[
\int_\gamma f(z)\,dz=F(\gamma(b))-F(\gamma(a)),
\]
by the chain rule for \(F\circ\gamma\) and the ordinary real FTC for the two real components.

### The punctured plane and winding

For \(\gamma(t)=e^{it}\), \(0\le t\le 2\pi\),
\[
\oint_\gamma\frac{dz}{z}=\int_0^{2\pi}\frac{ie^{it}}{e^{it}}\,dt=2\pi i.
\]
If \(\gamma\) is any piecewise \(C^1\) closed contour avoiding 0, lift its angle continuously along the parameter interval and write \(\gamma(t)=r(t)e^{i\theta(t)}\), with \(r(t)>0\). On smooth pieces,
\[
\frac{\gamma'(t)}{\gamma(t)}=\frac{r'(t)}{r(t)}+i\theta'(t).
\]
On integrating, \(\log r(b)-\log r(a)=0\) and \(\theta(b)-\theta(a)=2\pi k\) for some \(k\in\mathbb Z\). Hence \(\oint_\gamma dz/z=2\pi i k\). This integer is the winding number \(\operatorname{Ind}(\gamma,0)\).

The integrand \(\bar z\) on the unit circle also yields \(2\pi i\), showing that a simply connected domain by itself does not imply zero closed integrals for nonholomorphic functions.

### Primitive/path-independence equivalence

For continuous \(f:U\to\mathbb C\) on an open path-connected \(U\), the following are equivalent: (i) \(f=F'\) for some \(F\in\mathcal O(U)\); (ii) contour integrals depend only on endpoints; (iii) all closed piecewise \(C^1\) contour integrals vanish. To show (iii) implies (i), define \(F(z)=\int_{z_0}^{z}f(w)\,dw\); path independence ensures well-definedness. For small \(h\), use the segment from \(z\) to \(z+h\):
\[
\frac{F(z+h)-F(z)}h=\int_0^1f(z+th)\,dt\longrightarrow f(z).
\]

### Exercises with answers

1. **Line segment:** Evaluate \(\int_\gamma z\,dz\) from 0 to \(1+i\). **Answer:** \(\frac12(1+i)^2=i\), by the primitive \(z^2/2\).
2. **Circle orientation:** Evaluate \(\oint_{|z|=3}\frac{dz}{z}\) clockwise. **Answer:** \(-2\pi i\).
3. **Local logarithm:** Explain why \(1/z\) has a primitive on the right half-plane. **Answer:** A holomorphic logarithm branch exists there, obtained by choosing angles in \((-\pi/2,\pi/2)\).
4. **Nonholomorphic integrand:** Evaluate \(\oint_{|z|=R}\bar z\,dz\) counterclockwise. **Answer:** \(\bar z=R^2/z\) on the circle, so the result is \(2\pi i R^2\).
5. **Estimation:** If \(|f|\le4\) on a contour of length 7, bound the integral. **Answer:** Its modulus is at most 28.

### Further reading

- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, Lecture 8, https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, Topic 3, https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- Wikipedia, *Contour integration*, https://en.wikipedia.org/wiki/Contour_integration.
- [Robert B. Ash and W. P. Novinger, Complex Variables, 2nd ed.](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesMerged.pdf) — Ash & Novinger, Complex Variables, chapter 2: contour integrals, primitives and winding.
