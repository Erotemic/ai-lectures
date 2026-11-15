# 026000 — Conformal Geometry: Angles, Coordinate Changes, and Hyperbolic Distance

**Track:** Analysis from First Principles. **Background:** holomorphic derivatives, Möbius transformations, Schwarz–Pick. **Question:** If a map may change every Euclidean distance, what geometry can it preserve exactly?

<!-- BEGIN SPOKEN LECTURE -->

# Conformal Geometry: Angles, Coordinate Changes, and Hyperbolic Distance

A map of the world may preserve some features while sacrificing others. The familiar maps of the Earth's surface onto paper cannot preserve everything. Some preserve areas, some preserve angles, and many preserve neither. Complex analysis gives us an especially precise version of this distinction. A holomorphic map whose derivative is nonzero preserves angles and local orientation. But it may stretch lengths by different factors at different locations. That suggests a question: can we find a different measurement of distance for which certain complex maps become exact symmetries rather than merely angle-preserving approximations?

The unit disk offers an answer. Under its Möbius automorphisms, points can move around freely, yet there is a natural distance that does not change. It is not the Euclidean distance we see on the page. It is the hyperbolic distance. To understand why it appears, we will examine conformality locally, then build the distance from the disk's automorphisms.

## The derivative as a tiny piece of geometry

Let f be holomorphic at a point a, with derivative not equal to zero. Near a, a small displacement h is transformed into approximately f prime at a times h. That approximation has an error that becomes small compared with the length of h. In a complex plane, multiplying by a nonzero complex number has a simple geometric meaning: rotate by a fixed angle and multiply all lengths by a fixed positive number. At that particular point, every direction experiences the same rotation and scale.

A horizontal and a vertical arrow that meet at a right angle remain perpendicular, to first order. Two arrows making an angle of thirty degrees still make that angle after applying the local linear approximation. Their lengths may change, but by the same local factor. This is what the word conformal means here.

Consider the exponential function. Its derivative is itself and is never zero. Locally, the exponential is conformal everywhere in the complex plane. But globally it repeats: adding two pi i to its input leaves the output unchanged. Thus local conformality does not imply global injectivity. If we restrict the exponential to the open horizontal strip where the imaginary part lies strictly between zero and two pi, it becomes injective, with the nonnegative real ray missing from its image. The lesson is that a conformal *equivalence* between domains means a one-to-one holomorphic map onto the target with holomorphic inverse; having a nonzero derivative at every point is only the local part.

For a better global example, start with the vertical strip consisting of points whose real part lies between zero and pi. Apply the map z goes to e to the power i z. As the real part runs from zero to pi, the argument of the image runs through an interval of length pi, placing the image in the upper half-plane. The imaginary part of z changes the radius of the image. Every point in the upper half-plane has a unique angle strictly between zero and pi and a unique positive radius, so this map is one-to-one and onto. We have transformed an infinite straight strip into an upper half-plane, preserving local angles but thoroughly changing straight-line geometry.

That construction provides an explicit equivalence between shapes Möbius maps alone cannot connect: a strip has two parallel boundary lines, while a half-plane has one. The exponential sends both edges of the strip toward the same boundary line from different sides of the origin. A Möbius map cannot do this because it always sends generalized circles to generalized circles and is globally one-to-one on the sphere.

## A wedge can become a half-plane

Now imagine a wedge with opening angle alpha, between zero and two pi. Write every point in it using a positive radius and an angle strictly between zero and alpha. Multiply that angle by pi divided by alpha, and raise the radius to the same power. The resulting transformation, a carefully chosen branch of z to the power pi over alpha, maps the wedge bijectively onto the upper half-plane.

The branch choice matters. A fractional power is not automatically a single-valued function everywhere away from zero. On the wedge there is a continuous choice of argument, so we can define a holomorphic logarithm and then exponentiate its multiple. The map is a conformal equivalence on the interior. At the corner, however, it can stretch or compress at an enormous rate as we approach the vertex, and the vertex itself is not an interior point of the wedge.

For a right-angle wedge, alpha equals pi over two. The map is z squared. A right angle at the boundary opens into a straight angle. Approaching the corner, the derivative becomes small. For a wedge of angle three pi over two, the exponent is two thirds, and the magnitude of the derivative becomes arbitrarily large near the corner. Neither observation contradicts conformality, because conformality is asserted only at interior points, not automatically on boundary corners.

This already hints at the boundary complications we will return to. A conformal equivalence may behave beautifully everywhere inside a domain while becoming badly distorted near the boundary.

## A measurement adapted to the disk

Now return to the unit disk. Ordinary Euclidean distance gives the center special status: points near the center have more space around them than points near the edge. But the disk's holomorphic automorphisms can move any interior point to any other. A distance that treats those automorphisms as genuine symmetries should not give the center a privileged role.

Begin at zero. Travel radially to a point at distance r from the center, where r lies between zero and one. Define the hyperbolic length of a tiny radial step to be twice the ordinary step length divided by one minus r squared. Near the center, the denominator is almost one, so the hyperbolic measurement is approximately twice the Euclidean one. Near the boundary, the denominator approaches zero. The same Euclidean increment costs more and more hyperbolic length. The disk edge recedes indefinitely in this metric.

Integrate the radial length from zero out to r. The answer is the natural logarithm of one plus r divided by one minus r. In particular, the hyperbolic distance from the center to the point at one half is the logarithm of three. At nine tenths of the Euclidean radius, the distance is the logarithm of nineteen. As r approaches one, the logarithm grows without bound.

This is an exact calculation, not a drawing convention. The boundary circle is at infinite hyperbolic distance from every point inside the disk. The disk is bounded in Euclidean coordinates but unbounded in its own intrinsic distance.

## Why the disk automorphisms preserve it

Recall the automorphism that sends a chosen point a to zero: take z minus a divided by one minus the conjugate of a times z. Differentiating gives a local scaling factor. A second calculation compares one minus the squared magnitude before and after the transformation. The two factors cancel in just the right way. The density twice the magnitude of a tiny displacement divided by one minus the squared distance from the center is unchanged.

That cancellation means something stronger than angle preservation. If you take any differentiable path in the disk, measure its hyperbolic length, and then transform the entire path by a disk automorphism, the measured length stays exactly the same. Taking the infimum over paths gives a distance that is also unchanged.

The formula for distance between any two points becomes especially simple when we first use a disk automorphism to send one of them to zero. Take the absolute value of the fraction z minus w divided by one minus the conjugate of w times z. Call that number rho. It lies between zero and one. The hyperbolic distance between z and w is the logarithm of one plus rho divided by one minus rho. So a complicated-looking two-point measurement reduces to the radial distance we already understood.

What do shortest paths look like? A diameter of the disk is a shortest path between points on that diameter. Applying disk automorphisms turns diameters into other generalized circles. The geodesics are therefore circular arcs that meet the disk boundary at right angles, together with diameters regarded as a limiting case. They often look curved on a Euclidean drawing. Curvature of the picture does not mean the paths are longer in the hyperbolic measurement.

We should be precise about the word shortest. It means shortest for the hyperbolic line element, not for the Euclidean metric of the page. If you measure the same path with a ruler, a Euclidean straight segment is shorter. The two geometries are answering different questions.

## The half-plane has the same geometry

Our Cayley transformation takes the upper half-plane onto the disk. Transport the disk's hyperbolic metric through it. A short calculation produces an elegant formula: the hyperbolic length of a tiny movement in the half-plane is the Euclidean length of that movement divided by the point's height above the real axis.

At height one, one unit of horizontal movement has hyperbolic length one. At height one hundred, the same movement costs only one hundredth as much. Near the real axis, the same horizontal movement becomes extremely expensive. Traveling vertically toward the real axis also takes infinite hyperbolic length, because integrating one over the height produces a logarithm that diverges.

This half-plane picture can be easier to imagine than the disk. Two points at a fixed horizontal separation seem closer, in the hyperbolic sense, when they are high above the boundary. A shortest path between them may rise upward first, traverse at greater height, and descend. Such geodesics are vertical lines or semicircles meeting the real axis at right angles.

The upper half-plane and the unit disk are therefore not merely conformally equivalent. They are isometric in their intrinsic hyperbolic geometry, provided we use the line elements that correspond under the Cayley transformation.

## Schwarz–Pick becomes a geometry theorem

There is a striking extension. Suppose f is any holomorphic map from the disk into itself, not necessarily one-to-one or onto. Schwarz–Pick says that it cannot increase hyperbolic distance. The derivative version says that the local hyperbolic scale after mapping is at most the scale before mapping. Thus every holomorphic disk self-map is nonexpanding in the hyperbolic metric.

This is much stronger than an ordinary Euclidean estimate. A holomorphic map can enlarge Euclidean distances near one point, especially near the boundary. But once we measure using the geometry naturally adapted to the disk, expansion is forbidden. Equality in the sharp Schwarz–Pick comparison at two distinct points forces the map to be a disk automorphism. So automorphisms are exactly the distance-preserving cases among the holomorphic self-maps.

Take f of z equal z squared. In Euclidean distance, this map can have derivative close to two near the unit boundary, so it locally magnifies small displacements there. In the hyperbolic metric, it is still nonexpanding. At the center, the derivative is zero and the map contracts dramatically. The apparent conflict disappears once we remember that Euclidean and hyperbolic scales differ from point to point.

## What is invariant, and what is not

We now have three levels of structure. Holomorphic maps with nonzero derivative preserve local angles and orientation. Biholomorphic maps give global conformal equivalences between domains. And in the special disk or half-plane setting, automorphisms preserve a natural complete hyperbolic distance. Any holomorphic map from the disk to itself is nonexpanding in that distance.

These statements do not say all conformal maps preserve hyperbolic distance between arbitrary domains unless we first put the corresponding intrinsic metrics on those domains. Nor do they say that every complex domain is equivalent to the disk. The punctured disk has a genuine loop around its missing center that cannot shrink to a point without leaving the domain. The disk does not. A homeomorphism, and therefore a conformal equivalence, cannot erase that difference.

Our next question is more ambitious and at first less plausible. A disk, a smooth irregular blob, and an angular polygon are geometrically very different. If they have no holes and do not occupy the entire plane, could they nevertheless always be related by some conformal equivalence, not necessarily an explicit Möbius map? The answer is yes. The Riemann mapping theorem makes that claim precise, and its proof will bring together the compactness of holomorphic families with the rigidity of the disk.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Local conformality and two explicit equivalences

For \(f\) holomorphic with \(f'(a)\ne0\),

\[
f(a+h)=f(a)+f'(a)h+o(|h|),\quad h\to0.
\]

Multiplication by \(f'(a)=\rho e^{i\theta}\) rotates and scales by \(\rho>0\). A global conformal equivalence is a biholomorphism of domains. Local nonvanishing derivative alone does not force global injectivity; \(e^z=e^{z+2\pi i}\).

\[
\{0<\Re z<\pi\}\xrightarrow{\ z\mapsto e^{iz}\ }
\mathbb H=\{\Im w>0\}.
\]

\[
W_\alpha=\{r e^{i\theta}:r>0,\ 0<\theta<\alpha\}
\xrightarrow{\ z\mapsto z^{\pi/\alpha}\ }\mathbb H,
\quad 0<\alpha<2\pi,
\]

with the holomorphic branch defined by \(0<\arg z<\alpha\).

### Poincaré metrics, curvature normalization \(-1\)

\[
ds_{\mathbb D}=\frac{2|dz|}{1-|z|^2},\qquad
 ds_{\mathbb H}=\frac{|dz|}{\Im z}.
\]

\[
d_{\mathbb D}(0,r)=\int_0^r\frac{2\,dt}{1-t^2}
=\log\frac{1+r}{1-r},\qquad 0\le r<1.
\]

\[
\rho(z,w)=\left|\frac{z-w}{1-\bar w z}\right|,
\qquad d_{\mathbb D}(z,w)=\log\frac{1+\rho}{1-\rho}.
\]

For \(\Phi_a(z)=(z-a)/(1-\bar a z)\),

\[
|\Phi_a'(z)|=\frac{1-|a|^2}{|1-\bar a z|^2},\quad
1-|\Phi_a(z)|^2=\frac{(1-|a|^2)(1-|z|^2)}{|1-\bar a z|^2}.
\]

The quotient of these identities gives invariance of \(ds_{\mathbb D}\). Hyperbolic geodesics are diameter segments or circular arcs orthogonal to \(|z|=1\).

### Schwarz–Pick in metric form

For \(f:\mathbb D\to\mathbb D\) holomorphic,

\[
\frac{|f'(z)|}{1-|f(z)|^2}\le\frac1{1-|z|^2},\qquad
 d_{\mathbb D}(f(z),f(w))\le d_{\mathbb D}(z,w).
\]

Equality in the distance inequality for distinct \(z,w\) forces \(f\) to be a disk automorphism.

### Exercises and answers

1. **Strip to half-plane.** Why does \(e^{iz}\) map \(0<\Re z<\pi\) injectively onto \(\mathbb H\)? **Answer:** Its argument is \(\Re z\in(0,\pi)\), and radius is \(e^{-\Im z}\in(0,\infty)\); both coordinates are unique.
2. **A corner.** What happens to \(|f'(z)|\) near the tip of \(W_{\pi/2}\) under \(f(z)=z^2\)? **Answer:** It is \(2|z|\to0\), without violating interior conformality.
3. **Radial distance.** Compute \(d_{\mathbb D}(0,1/2)\) and \(d_{\mathbb D}(0,9/10)\). **Answer:** \(\log3\) and \(\log19\).
4. **A false contradiction.** Explain how \(z^2\) can have Euclidean derivative magnitude near 2 and still obey Schwarz–Pick. **Answer:** Schwarz–Pick compares hyperbolic scaling, with a density depending on the source and target points.
5. **Topology matters.** Why cannot the punctured disk be conformally equivalent to the disk? **Answer:** A conformal equivalence is a homeomorphism and preserves simple connectivity; a loop winding around 0 cannot contract within the punctured disk.

### References

- [Wikipedia, Conformal map](https://en.wikipedia.org/wiki/Conformal_map).
- [Wikipedia, Poincaré disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model).
- [Wikipedia, Poincaré half-plane model](https://en.wikipedia.org/wiki/Poincar%C3%A9_half-plane_model).
- [Wikipedia, Schwarz–Pick theorem](https://en.wikipedia.org/wiki/Schwarz%E2%80%93Pick_theorem).
