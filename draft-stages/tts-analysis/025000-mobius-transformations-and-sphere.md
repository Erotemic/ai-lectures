# 025000 — Möbius Transformations: Moving the Plane Without Tearing Its Angles

**Track:** Analysis from First Principles. **Background:** complex multiplication and division, holomorphic derivatives, Schwarz's lemma. **Question:** What are all the simplest globally reversible conformal transformations, and what happens to their poles?

<!-- BEGIN SPOKEN LECTURE -->

# Möbius Transformations: Moving the Plane Without Tearing Its Angles

Imagine drawing a circle and a straight line on a sheet of paper. Then imagine moving the paper in a way that may turn the line into a circle, may send one ordinary point out to infinity, but never creates an angle where two smooth curves formerly met at a different angle. This sounds like contradictory geometry. How could a circle and a line be interchangeable? The answer begins by enlarging our picture of the complex plane. Instead of treating infinity as somewhere outside mathematics, we give it the status of one additional point. On this enlarged surface, lines become circles passing through infinity. The transformations we will study move all of these generalized circles around while preserving their angle structure.

The formulas are remarkably short. Take four complex numbers, called a, b, c, and d. Form the fraction with numerator a times z plus b, and denominator c times z plus d. Provided a times d minus b times c is nonzero, the resulting transformation is called a Möbius transformation. The determinant condition is important. If it vanished, the numerator and denominator would be proportional and the fraction would collapse to a constant wherever defined. With a nonzero determinant, we can reverse the transformation and recover every input from its output.

Before introducing the full general theory, let us make the simplest interesting examples audible. Adding three to z translates the plane. Multiplying by i rotates the plane by a quarter turn. Multiplying by two enlarges every distance by a factor of two. And taking the reciprocal, one over z, does something different: near the origin it sends points far away, while very large points are sent close to zero. These operations generate every Möbius transformation. They are translations, nonzero complex scalings and rotations, and inversion. An arbitrary four-coefficient fraction is their composition, with no other kind of elementary operation required.

## What the pole means

Consider the reciprocal map, one over z. It appears to be undefined at zero. If we insist that its domain is the ordinary complex plane, it is not even a function at that point. But enlarge the plane by adjoining a single point called infinity. Define one over zero to be infinity, and one over infinity to be zero. Now inversion has no missing input and no missing output. Applied twice, it returns the original point, even at zero and infinity.

The enlarged plane is called the Riemann sphere, because it can be represented by a sphere with one point corresponding to infinity. There is a geometric construction, stereographic projection, that matches all ordinary complex numbers with all but one point of the sphere. We need not derive the projection to use its main consequence: a line in the ordinary plane becomes a circle on the sphere that passes through the point at infinity. A finite circle stays a circle. The distinction between line and circle depends on which point of the sphere we chose to call infinity.

Now return to the general fraction. If c is nonzero, its denominator vanishes at the complex number minus d divided by c. This is the pole, sent to infinity. The point at infinity is sent to a divided by c. If c is zero, the transformation is affine, and infinity remains infinity. Because the determinant is nonzero, no cancellation erases the pole. This is a clean way to understand what the formula is doing rather than treating denominator zero as an inconvenient exception.

The inverse is just as explicit. Solving w equals the fraction for z gives d times w minus b, divided by minus c times w plus a. Composing either transformation with its inverse returns the input on the entire sphere. One subtlety is that multiplying all four coefficients by the same nonzero number changes none of the outputs. So the quadruple of coefficients is not unique, even though the transformation is.

## Angles survive, but lengths do not

To understand conformality, imagine two small arrows based at a point z. A differentiable complex map with nonzero complex derivative acts on both arrows, to first order, by multiplying by the same complex number. Complex multiplication rotates by the argument and scales by the absolute value. Both arrows rotate by the same angle and scale by the same factor. Consequently, the angle between them is preserved, including its orientation.

Different points can have different scale factors. Conformality does not mean preservation of distance, area, or straight lines. It means that, close enough to each ordinary point with nonzero derivative, the map looks like a rotation followed by a uniform enlargement or shrinkage. It is a local assertion. A global one-to-one map is an additional requirement when we speak of a conformal equivalence between domains.

Differentiate the four-coefficient fraction. Its derivative has numerator a times d minus b times c, and denominator the square of c times z plus d. The determinant never vanishes, and away from the pole the denominator never vanishes either. Thus the derivative is nonzero at every finite point where the ordinary coordinate formula applies. A change of local coordinate around infinity gives the same conclusion there. Möbius transformations are therefore conformal automorphisms of the Riemann sphere.

Compare that with taking the complex conjugate of z. Conjugation reflects across the real axis. The magnitude of every angle remains the same, but clockwise and counterclockwise are exchanged. It is not a holomorphic conformal map in our orientation-preserving sense. Preserving *unoriented* angles is weaker than being holomorphic with nonzero derivative.

## The circle-and-line phenomenon

Here is a small experiment. Look at a vertical line to the right of the origin, say the line with real part one. Apply inversion, one over z. Write the original point as one plus i times t, where t is any real number. Multiplying numerator and denominator by the complex conjugate shows that the image has real part one divided by one plus t squared, and imaginary part minus t divided by one plus t squared. These points lie on a circle whose diameter runs from zero to one on the real axis. As t tends toward either positive or negative infinity, the images approach zero. Infinity is the point completing the circle.

So inversion turns that line into a circle through zero. A line through zero is different: it is mapped to another straight line through zero, though distances along it are reversed. The general rule is that Möbius transformations carry generalized circles to generalized circles: ordinary circles and straight lines regarded as circles through infinity. They do not preserve the classification of a generalized circle as finite or straight, because the designated point at infinity may move.

There is a useful algebraic reason behind this geometry. A generalized circle can be described by a real equation involving z times its complex conjugate, z, its conjugate, and a constant. Substitute the inverse Möbius formula into that equation, then clear the denominator and its conjugate. The result has the same form. The companion gives the exact equation; the important idea for listening is that the reciprocal and complex conjugate occur in a balanced pair, so the class of such curves survives the substitution.

## Three points determine a transformation

A translation is pinned down by where it sends one point. A nonzero complex scaling needs more information. A general Möbius transformation is uniquely determined by the images of three distinct points of the Riemann sphere, provided the target points are also distinct. This is one of the most effective ways to construct them. Choose where you want three landmarks to go; the rest of the map follows.

Why three? Because we can first build a Möbius transformation that sends any three distinct points to zero, one, and infinity. Do the same for the three desired targets, then reverse the second construction and compose. To prove uniqueness, suppose two transformations agree on three distinct points. Compose one with the inverse of the other. The resulting Möbius transformation fixes zero, one, and infinity after suitable normalization. Fixing infinity forces it to be affine; fixing zero forces no translation; fixing one forces its scale to be one. It is therefore the identity.

The expression that makes this argument concrete is the cross-ratio. Given four points, it compares two differences to two other differences so that every Möbius transformation leaves the ratio unchanged, with the usual limiting meaning when one of the points is infinity. Three points define the coordinate frame; the fourth is located by its cross-ratio. This is why Möbius geometry often feels more like projective geometry than Euclidean geometry. It is about configurations and incidence rather than a fixed ruler.

But do not misunderstand the three-point theorem as saying every triple can be reached by a *disk* automorphism. The theorem is about transformations of the entire sphere. If a map must also keep the unit disk mapped to itself, that additional restriction greatly reduces the possibilities.

## The disk and the upper half-plane

Let us build one of the most useful examples. Consider the upper half-plane: all complex numbers with positive imaginary part. There is a fraction that takes this entire half-plane exactly onto the open unit disk. Subtract i from z, and divide by z plus i. Call the result C of z. When z is real, the numerator and denominator have equal magnitude, so the output has magnitude one. When z lies above the real axis, the numerator is shorter than the denominator, so the output has magnitude less than one. The point i goes to zero, while the boundary real line and the point infinity map to the unit circle.

Try a concrete height. If z equals two i, then the fraction is one i divided by three i, so the result is one third. At height one, we are at the disk center. Above that, we move up the positive real axis toward the boundary point one, never reaching it from inside. This calculation makes the formula more than a symbol: it is a coordinate conversion between two standard worlds for complex analysis.

Now consider maps from the disk back onto itself. Choose any point a strictly inside the disk. The fraction z minus a divided by one minus the complex conjugate of a times z sends a to zero. It takes the disk bijectively onto itself. Multiply by a complex number of magnitude one to add any desired rotation. These are all automorphisms of the disk, no more and no less.

A quick way to see why there are no others uses Schwarz's lemma. Given any disk automorphism, first compose with a transformation of this type so that zero is fixed. Schwarz's lemma says the magnitude of the image is no larger than the magnitude of the input. Apply the same reasoning to the inverse: the reverse inequality holds. Equality forces a rotation. Undo the first normalization. We have classified the entire group.

The classification explains an important difference between the sphere and the disk. On the sphere, three distinct landmarks can be assigned arbitrarily. On the disk, the automorphisms are so rigid that fixing one interior point leaves only a one-parameter family of rotations after normalization. Fixing that point and a direction leaves only the identity.

## What this prepares us to do

Our eventual goal is to compare domains whose boundaries may not be circles or straight lines. Möbius maps are insufficient for that: they send generalized circles to generalized circles, so they cannot directly send a disk onto a square. Yet they provide the transformations we will use repeatedly when studying more general conformal maps. We can choose base points, normalize derivatives, turn half-plane problems into disk problems, and simplify the geometry of a proof before confronting its essential difficulty.

The deepest lesson from this first mapping family is to separate three questions. Does the formula preserve angles locally? Is it one-to-one and onto the intended domain? And what happens when a point approaches the boundary or infinity? Möbius transformations answer all three questions explicitly. For more complicated domains, each question will become a theorem of its own.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Definitions and calculations

A Möbius transformation is a rational map on the Riemann sphere

\[
M(z)=\frac{az+b}{cz+d},\qquad ad-bc\ne0.
\]

The coefficient matrix is defined only up to multiplication by a nonzero scalar; composition corresponds to matrix multiplication up to scalar. On finite points away from the pole,

\[
M'(z)=\frac{ad-bc}{(cz+d)^2},\qquad
M^{-1}(w)=\frac{dw-b}{-cw+a}.
\]

For \(c\ne0\), \(M(-d/c)=\infty\) and \(M(\infty)=a/c\). For \(c=0\), \(M(\infty)=\infty\).

Generalized circles are sets of the form

\[
A|z|^2+Bz+\overline B\overline z+C=0,
\qquad A,C\in\mathbb R,\ B\in\mathbb C,
\]

where the equation is nondegenerate. \(A=0\) describes a line in the finite plane. Substitution by a Möbius inverse preserves this family on the sphere.

Inversion of \(z=1+it\) gives \(w=(1-it)/(1+t^2)\), and \((\Re w-1/2)^2+(\Im w)^2=1/4\).

For distinct finite \(z_1,z_2,z_3,z_4\), the cross-ratio convention used here is

\[
[z_1,z_2;z_3,z_4]
=\frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}.
\]

It is invariant when the *same* Möbius map is applied to all four arguments. Use limits if a point is infinity.

The Cayley transform and its inverse are

\[
C(z)=\frac{z-i}{z+i},\qquad C^{-1}(w)=i\frac{1+w}{1-w}.
\]

For \(z=x+iy\), \(y>0\),

\[
1-|C(z)|^2=\frac{4y}{|z+i|^2}>0.
\]

Every disk automorphism has the form

\[
\Phi_{a,\theta}(z)=e^{i\theta}\frac{z-a}{1-\bar a z},\quad |a|<1,
\qquad
|\Phi_{a,\theta}'(a)|=\frac1{1-|a|^2}.
\]

### Exercises and answers

1. **Pole and image of infinity.** For \(M(z)=(2z+3)/(z-1)\), find the pole, image of infinity and inverse. **Answer:** Pole \(1\), \(M(\infty)=2\), inverse \(z=(w+3)/(w-2)\).
2. **Cayley test.** Calculate \(C(2i)\) and \(C(0)\). **Answer:** \(1/3\) and \(-1\), respectively. The second is on the disk boundary because zero is on the half-plane boundary.
3. **A line becomes a circle.** Under \(w=1/z\), show \(\Re z=1\) maps to the circle with center \(1/2\) and radius \(1/2\), excluding the point \(0\) in the finite image. **Answer:** Use \(z=1+it\) as above; the missing zero is the image of the original line's point at infinity.
4. **Disk rigidity.** Show a disk automorphism fixing zero and with positive real derivative at zero is the identity. **Answer:** By Schwarz applied to the map and its inverse, it is a rotation \(e^{i\theta}z\); a positive real derivative forces the rotation to be 1.
5. **An orientation warning.** Why is \(z\mapsto\bar z\) not an analytic Möbius map? **Answer:** It reverses orientation; the complex derivative fails to exist.

### References

- [Wikipedia, Möbius transformation](https://en.wikipedia.org/wiki/M%C3%B6bius_transformation).
- [Wikipedia, Riemann sphere](https://en.wikipedia.org/wiki/Riemann_sphere).
- [Wikipedia, Schwarz lemma](https://en.wikipedia.org/wiki/Schwarz_lemma).
