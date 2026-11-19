# 018000 — Laurent Series and Isolated Singularities: The Anatomy of a Missing Point

**Track:** Analysis from First Principles. **Background:** power series, identity theorem, Cauchy's integral formula on disks and annuli. **Theme:** Laurent expansions decompose holomorphic behavior around a puncture into ordinary Taylor terms and a principal part; the latter classifies isolated singularities exactly.

<!-- BEGIN SPOKEN LECTURE -->

# Laurent Series and Isolated Singularities: The Anatomy of a Missing Point

Suppose a complex function is perfectly holomorphic throughout a neighborhood except at one missing point. What can it do as we approach that point? The answer is not simply that the function either stays finite or blows up. Both of those behaviors occur, but there is a third kind of singularity in which the function's values behave far less predictably. One example becomes arbitrarily large on some approaches, arbitrarily small on others, and repeatedly approaches any nonzero complex number along carefully chosen sequences.

The example is the complex exponential of one divided by z, near z equal to zero. We will understand it without relying on pictures of a spiral. We will build a new kind of power series that allows negative powers, then read the behavior at the missing point directly from those powers.

This is the idea of a Laurent series. A Taylor series is centered on a point that belongs to the domain of holomorphicity. A Laurent series is built to work on an annulus: a ring with an inner hole. The missing center may be a benign omission, a pole of finite order, or an essential singularity. In this lecture, the classification will come from a theorem about the coefficients, not from visual guesswork.

## Why a hole changes the algebra of an expansion

Recall the geometric series for one divided by one minus z. Inside the unit circle, we expand it as one plus z plus z squared and onward. Outside that circle, there is another useful expansion. Factor out negative one divided by z, leaving a geometric series in one divided by z. The resulting terms are negative one divided by z, then negative one divided by z squared, and so on. Both formulas describe the same rational function where they converge, but their domains are disjoint.

This is the first hint that a complex function may need positive powers on one side of a circle and negative powers on another. The negative powers are not an arbitrary addition to notation. They reflect the geometry of a domain that does not include the center about which we are expanding.

To see the mechanism, fix a point a and two concentric circles, one small and one large. Assume our function is holomorphic throughout the closed annular region between them, with a little room on either side. Choose a point z strictly between the circles. The Cauchy formula for an annulus expresses f at z as the outer-boundary integral minus the inner-boundary integral. The inner boundary has a minus sign because the positively oriented boundary of a region with a hole runs clockwise around the hole.

Now expand the kernel in those two integrals. On the outer circle, z is closer to a than the boundary point is, so the familiar geometric expansion produces nonnegative powers of z minus a. On the inner circle, the boundary point is closer to a than z is, so expanding in the opposite ratio produces negative powers of z minus a. Adding the contributions gives a two-sided series. It runs through positive powers, a constant term, and then negative powers all the way downward if necessary.

This is the Laurent expansion. Its coefficients are uniquely determined by contour integrals around circles lying in the annulus. The same coefficient can be computed on any such circle, because the integrand is holomorphic between those circles. We can also differentiate and integrate the series term by term on any compact subannulus. The qualifications about staying away from both boundaries are what make the convergence estimates legitimate.

The positive-power part resembles an ordinary Taylor series and is called the regular part. The sum of all negative-power terms is called the principal part. Every classification of an isolated singularity will depend on that principal part.

## A missing point that is not a real singularity

Begin with a function that looks undefined at zero: sine of z divided by z. The quotient is not defined at z equal to zero if we take the formula literally. But its Taylor expansion reveals what happens. Sine of z is z minus z cubed over six, plus higher odd powers. Dividing by z leaves one minus z squared over six, plus higher even powers. No negative powers survive.

The limit at zero is one. We can fill in the missing value by defining the function to equal one there. Once we do that, the new function is holomorphic at zero. Such a point is called a removable singularity. The phrase means the original formula had a hole, but the holomorphic function did not intrinsically need one.

In the Laurent description, removability has a precise signature: every coefficient of every negative power is zero. There is then no genuine principal part. The series reduces to an ordinary Taylor series, including a constant term that supplies the missing value.

There is another way to detect the same situation that is often easier than computing coefficients. If a holomorphic function on a punctured disk stays bounded sufficiently close to the center, the singularity is removable. This is the removable singularity theorem. Its proof is short once we know the coefficient formula.

Take the coefficient of one of the negative powers. It is a contour integral around a small circle. If the function's magnitude is bounded by M there, the length estimate bounds the coefficient by M times a positive power of the radius. Shrink the radius toward zero. That bound tends to zero, while the coefficient itself stays the same. Therefore every negative-power coefficient must be zero.

Notice what bounded means. We need a bound uniform over every point in some punctured neighborhood, not just a bound along a favorite approach. A function may appear harmless along the real axis and still become unbounded along imaginary directions. Complex analysis always asks us to inspect all paths of approach within the domain.

## A pole has a finite principal part

Next consider one divided by z cubed. The function is holomorphic everywhere except zero, and it diverges in magnitude like the reciprocal of the cube of the distance to zero. Its Laurent series is just one negative-power term. Zero is a pole of order three.

More generally, suppose the Laurent principal part has finitely many nonzero terms, and its most negative power is the negative m-th power. We can factor the function into one divided by z minus a to the power m, times a holomorphic function that is nonzero at a. The number m is the order of the pole. It tells us exactly how severe the divergence is in the local sense: multiplying f by the m-th power of z minus a produces a finite nonzero limit.

A pole is not just a point where a formula looks large or a denominator is zero. Cancellation can change the classification. Consider z squared minus one divided by z minus one. If we first factor the numerator and cancel, the expression becomes z plus one away from one. The apparent singularity at one is removable. By contrast, one divided by z minus one has a genuine simple pole there, because no holomorphic numerator cancels its zero denominator.

For a pole, the modulus of f tends to infinity as z approaches the center from every direction. That last phrase distinguishes a pole from an essential singularity. You may see a function becoming large along one sequence without having found a pole. The finite principal part, with a nonzero leading coefficient, is what establishes the uniform growth to infinity.

In practice, one efficient test is to multiply by a power of z minus a and ask whether the product extends holomorphically with a nonzero value at a. The smallest such positive power is the pole order. That is often cleaner than explicitly generating a Laurent series.

## An essential singularity never settles into one finite order

Now turn to the exponential of one divided by z. The ordinary exponential series says exponential of w equals one plus w plus w squared divided by two factorial, and so on. Substitute one divided by z. Near zero, the resulting Laurent series has infinitely many nonzero negative-power terms. No finite power of z will clear them all. This is an essential singularity.

Let us approach zero along the positive real axis. One divided by z becomes large and positive, so its exponential grows without bound. Approach along the negative real axis. One divided by z becomes large and negative, so its exponential tends to zero. Approach along the imaginary axis. One divided by z is purely imaginary; the exponential stays on the unit circle, rotating more and more rapidly as z approaches zero. The same missing point produces growth, decay, and oscillation, depending on the path.

This example makes it dangerous to classify a singularity by sampling a handful of directions. If we examined only the positive real axis, we might falsely pronounce it a pole. If we examined only the negative real axis, we might hope for a removable singularity with value zero. Both guesses miss the full two-dimensional behavior.

The three classes are exhaustive for an isolated singularity. Either the principal part has no nonzero terms, in which case the singularity is removable; it has finitely many with a most negative nonzero exponent, in which case we have a pole; or it has infinitely many nonzero negative-power terms, in which case the singularity is essential.

We are classifying a single missing point surrounded by a punctured disk on which the function is holomorphic. If singularities themselves pile up at the point, there may be no punctured disk free of other singularities, and this classification theorem does not apply there. The word isolated is a mathematical hypothesis, not a decorative adjective.

## Why an essential singularity has dense nearby values

There is a striking theorem behind the irregular behavior. Near an essential isolated singularity, the values of the function come arbitrarily close to every complex number. This is the Casorati–Weierstrass theorem. It does not claim that every value is actually attained. For example, exponential of one divided by z never equals zero, but its values approach zero along suitable paths.

We can prove the density statement using the classification already established. Suppose, toward a contradiction, that some complex number b is excluded not merely as an exact value but by a whole open disk around b: throughout some punctured neighborhood, the function stays at least a fixed positive distance from b.

Then one divided by f minus b is holomorphic and bounded on that punctured neighborhood. The removable singularity theorem fills its missing point. Call the extended reciprocal g. If g at the center is nonzero, then one divided by g is holomorphic there and f itself extends after adding b. We would have a removable singularity. If g at the center is zero, the zero is isolated with some finite multiplicity because g is not identically zero near the center. Taking the reciprocal shows that f has a pole. Either way, the original point could not be essential.

Thus no open disk of output values can be avoided throughout an entire punctured neighborhood. The image of every sufficiently small punctured neighborhood is dense in the complex plane. This says much more than merely that the function is unbounded. It also says less than the stronger Great Picard theorem, which addresses the actual taking of values and possible exceptions. We have proved exactly the density statement we claimed.

It is worth recognizing what made this proof possible. The holomorphic reciprocal transformed a claim about missing output values into a boundedness statement. Boundedness gave removability. The possible value of the reciprocal at the center divided the situation into an ordinary extension or a pole. An essential singularity had nowhere to hide.

## A little contour calculation foreshadows something bigger

Take a circle about zero, traversed counterclockwise. If we integrate one divided by z squared around that circle, the result is zero. If we integrate one divided by z, the result is two pi i. Why do negative powers with different exponents behave so differently?

Parametrize the circle by a fixed radius and a changing angle. A term like z to the negative third power contributes an oscillatory exponential of a nonzero integer frequency after multiplication by the path velocity. Over a full turn, its positive and negative contributions cancel. Exactly one exponent is special: negative one. The velocity contributes one power of z, so one divided by z times the velocity becomes a constant multiple of i. There is no oscillation left to cancel.

For a general Laurent series, term-by-term integration therefore singles out the coefficient of one divided by z minus a. All the other coefficients disappear from the circle integral. That surviving coefficient is called the residue. It can exist at a pole, at an essential singularity, or even at a removable point, where it is zero.

Our classification of singularities has been about all the negative powers. A contour integral will turn out to care about just one of them. That is why the residue theorem can compute integrals of functions whose complete Laurent expansions are complicated or infinite.

The lasting distinction is this. A Taylor expansion describes a holomorphic function through a filled disk. A Laurent expansion describes a holomorphic function through a ring. The missing point is removable when negative coefficients vanish, a pole when only finitely many survive, and essential when infinitely many survive. Those facts characterize the possible local behaviors, while the single coefficient of the negative first power will control the integral around the hole.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Laurent theorem on an annulus

Let \(A=\{z:r<|z-a|<R\}\), with \(0\le r<R\le\infty\), and suppose f is holomorphic on A. There are unique coefficients \(c_n\), \(n\in\mathbb Z\), such that

\[
f(z)=\sum_{n=-\infty}^{\infty}c_n(z-a)^n,
\qquad c_n=\frac{1}{2\pi i}\oint_{|\zeta-a|=\rho}\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta,
\qquad r<\rho<R.
\]

Convergence is uniform on each compact subannulus. The coefficient integral is independent of the allowed circle radius \(\rho\) by Cauchy's theorem applied to the annular region between two circles.

One derivation uses \(f(z)=(2\pi i)^{-1}(\oint_{C_\text{outer}}-\oint_{C_\text{inner}})f(\zeta)/(\zeta-z)\,d\zeta\). Expand the outer kernel in positive powers of \(z-a\), and the inner kernel in negative powers. To justify this formula, work first in a closed annulus compactly contained in A, where f is holomorphic in a neighborhood of the closed region.

### Isolated singularities: exhaustive trichotomy

If f is holomorphic on \(0<|z-a|<R\), then exactly one holds:

1. **Removable:** \(c_n=0\) for every \(n<0\), equivalently f is bounded on some punctured neighborhood of a, equivalently f extends holomorphically across a.
2. **Pole of order m:** \(c_{-m}\ne0\) and \(c_n=0\) for \(n<-m\). Equivalently \(f(z)=g(z)/(z-a)^m\) with g holomorphic near a and g(a) nonzero. Then \(|f(z)|\to\infty\) as z tends to a.
3. **Essential:** Infinitely many negative Laurent coefficients are nonzero; neither a holomorphic extension nor a pole is possible.

For bounded f, \(|c_{-k}|\le M\rho^k\) as \(\rho\to0\), so every negative coefficient vanishes. This is a direct proof of the removable singularity theorem.

### Worked examples and answers

1. \(\sin z/z\) at zero: removable, with extension value 1.
2. \((e^z-1-z)/z^2\) at zero: removable, with extension value 1/2.
3. \(z^3/(z^5)\) at zero, away from cancellation: pole of order two.
4. \(z\sin(1/z)\) at zero: essential. Its Laurent expansion begins \(1-1/(3!z^2)+1/(5!z^4)-\cdots\).
5. \(e^{1/z}\) at zero: essential. It omits zero but has values approaching zero; this does not contradict Casorati–Weierstrass.
6. \(1/(z(z-2))\) about zero: for \(0<|z|<2\), write \(-1/(2z)\sum_{n\ge0}(z/2)^n\); the residue is \(-1/2\). For \(|z|>2\), a distinct negative-power expansion is valid. Different annuli support different Laurent expansions.

### Casorati–Weierstrass theorem and proof

For f holomorphic on \(0<|z-a|<R\) with an essential singularity at a, and any \(0<r<R\), the image \(f(\{0<|z-a|<r\})\) is dense in \(\mathbb C\). If it omitted an open disk centered at b, then \(1/(f-b)\) would be bounded and holomorphic on that punctured disk, hence removable. A nonzero extension value implies f removable; a zero extension value implies f has a pole. Contradiction.

### Further reading

- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, Topic 7, Taylor and Laurent series: https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, isolated singularities: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- Wikipedia, *Laurent series*: https://en.wikipedia.org/wiki/Laurent_series.
- Wikipedia, *Casorati–Weierstrass theorem*: https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem.
- [Tero Kilpeläinen and Antti Vähäkangas, Complex Analysis 2 (2024)](https://users.jyu.fi/~salomi/teaching/ca2_2024/Lecture_notes_eng.pdf) — Kilpeläinen & Vähäkangas, Complex Analysis 2, chapters 2–3: Laurent series and isolated singularities.
