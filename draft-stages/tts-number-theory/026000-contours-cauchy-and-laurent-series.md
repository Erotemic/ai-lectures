# 026000 - Contours, Cauchy's Formula, and the Geometry of Complex Analysis

**Track:** Number Theory from First Principles. **Background:** complex numbers, functions and limits, elementary integration, series, the analytic continuation constructed in 019000. **Aim:** build the complex-variable vocabulary and give proofs of Cauchy's formula, local power series, isolated zeros, and residues, with a clear statement of which general contour facts are being used.

<!-- BEGIN SPOKEN LECTURE -->

# Contours, Cauchy's Formula, and the Geometry of Complex Analysis

Why should a question about the density of prime numbers lead us to draw loops in the complex plane? We have already met the zeta function, a sum which can be continued beyond the domain where the sum converges. We know its values along a certain vertical line will matter in the prime number theorem. What we do not yet possess is a general way to control a function throughout a region, not just at a point. Complex analysis supplies that control. The surprising feature is that knowing a complex differentiable function around a loop can tell us its value at the loop's center.

Think of the complex plane as the ordinary plane, where a point has a horizontal real coordinate and a vertical imaginary coordinate. Multiplication by i rotates a vector through a quarter turn. A complex function sends points in this plane to other points in the same plane. A complex derivative is a limit of the ratio of two complex differences. Unlike a derivative in one real variable, the incoming difference can approach zero from any direction. Requiring the same quotient limit in all directions is extremely restrictive.

Consider the function that replaces each complex number by its conjugate. If we approach zero along the real axis, the quotient of the change in output by the change in input is one. Along the imaginary axis, it is negative one. Therefore conjugation has no complex derivative at zero, nor anywhere else. By contrast the function that squares its input has derivative twice the input: the identity follows by expanding the square, no matter which direction we approach from.

A function with a complex derivative at every point of an open region is called holomorphic there. We have sometimes used the word analytic, meaning representable by a convergent power series. One of the great theorems we will earn today is that in this setting those two notions agree. It is not true for ordinary real differentiability. A smooth real function can have a Taylor series that fails to reconstruct the function. For holomorphic functions the local series is forced by an integral around a circle.

## How to integrate along a path

Take a smooth path through the complex plane. At each point, evaluate a function f, multiply by the little complex displacement along the path, and add. The limit of these sums is the contour integral of f times d z. The direction matters: reversing a path reverses the integral. The integral is additive when we join paths end to end.

For a concrete calculation, go once counterclockwise around a circle centered at a, with radius r. Parameterize the circle by a plus r times the complex exponential of i t, for t from zero to two pi. The tiny displacement is i r times that exponential, times d t. The function one divided by z minus a is the reciprocal of r times the exponential. Everything cancels except i d t. Its integral is two pi i, regardless of the radius.

By contrast, the integral of one around a closed path is zero, since it is the net displacement. So is the integral of z along a closed path: z has the antiderivative one half z squared. The reciprocal function behaves differently because the point a is missing from its domain. No continuous choice of a complex logarithm exists around a complete loop encircling a. The hole in the domain is visible in the integral.

This distinction is why we must say where a function is holomorphic. It is not enough that the boundary curve looks safe. To apply the elementary version of Cauchy's theorem, the function must be holomorphic throughout the region enclosed by that curve, as well as in a neighborhood of its boundary.

## Why integrals around small triangles vanish

Cauchy's theorem says that a holomorphic function has integral zero around the boundary of a filled triangle, and hence around boundaries built from triangles inside its domain. A tempting proof would be to differentiate the real and imaginary parts and apply the usual two-dimensional Green theorem. That works with additional continuity of partial derivatives. The stronger result, called Cauchy-Goursat, needs only the existence of the complex derivative.

Here is the mechanism of its proof. Divide a triangle into four similar triangles of half the side length. Their oriented boundary integrals add up to the integral around the original triangle, because interior edges cancel. At least one smaller triangle must have an integral whose magnitude is a quarter as large as the original integral's magnitude. Choose such a triangle and repeat. We obtain nested triangles shrinking toward one point, call it z zero.

Near z zero, differentiability gives a first-order approximation: f of z equals f of z zero plus f prime of z zero times z minus z zero, plus an error smaller than any fixed positive constant times the distance from z to z zero, once we are sufficiently close. The constant and linear terms integrate to zero around a triangle because they have antiderivatives. The remaining error has small magnitude, and the perimeter of the tiny triangle is also small. Thus the integral around the selected tiny triangle is bounded by an arbitrarily small constant times the square of its side length.

But each stage reduced the triangle's area by exactly a factor of four, while our choice ensured that the selected integral retained at least one quarter of the previous integral. Multiply the tiny estimate back by four at each stage. The original triangle's integral must be smaller than every positive bound. It is zero. That is the heart of the Cauchy-Goursat proof, not an unexplained appeal to smoothness.

Triangulating an ordinary polygonal region now cancels all interior edges. For a disk or other region with a sufficiently regular boundary, polygonal approximation or a deformation argument gives the familiar contour version. We will use the version in which a function is holomorphic on a neighborhood of a disk and its boundary. If the region has holes, their boundary integrals must be included with the appropriate orientation.

## A value recovered from its boundary

Let a be inside a positively oriented circle C, and let f be holomorphic on a neighborhood of the closed disk. Form the function obtained by dividing f of z minus f of a by z minus a. This quotient is holomorphic away from a, and is bounded near a, because its limit there is the derivative of f. Cut out a small circle around a. Cauchy's theorem on the punctured disk says the outer integral of this quotient equals its inner circle integral. But the quotient remains bounded while the inner circle's length tends to zero. Its inner integral tends to zero, and therefore its outer integral is zero.

Rearrange what remains, using our explicit integral of one over z minus a. We learn that two pi i times f of a equals the integral around C of f of z divided by z minus a. That is Cauchy's integral formula. It says the entire value at a is encoded in values of f on a circle around a.

There is another way to see why this is plausible. Cut a tiny circle around a out of the larger disk. The quotient f of z divided by z minus a is holomorphic on the punctured region. Its integral on the large boundary equals its integral on the tiny boundary. As the tiny circle shrinks, f of z becomes nearly f of a, and the remaining reciprocal integral is two pi i. The integral does not depend on the radius because the excluded point is the only obstruction.

Now vary a inside the circle while keeping the contour fixed. The denominator one over z minus a can be expanded as a geometric series when a is close enough to the center. This series converges uniformly on the contour, so integration term by term is valid. Every holomorphic function therefore equals a convergent power series locally. We have proved the promised equivalence between complex differentiability and local analyticity.

Differentiate the formula with respect to a. Each derivative brings down another power of the denominator and an integer factor. On a circle of radius r, if f has magnitude at most M, the absolute value of its n-th derivative at the center is at most n factorial times M divided by r to the n. These are Cauchy's estimates. A local bound on f controls every derivative, something with no analogue for arbitrary real differentiable functions.

## What zeros look like

Power series also govern zeros. Suppose f is holomorphic near a and is not identically zero. Look for the first nonzero coefficient of its Taylor series about a. If that coefficient has degree m, then f of z equals z minus a to the power m times a holomorphic function g, with g of a nonzero. Near a, g remains nonzero, so a is the only zero nearby. We call m the multiplicity of the zero.

This proves that zeros of a nonzero holomorphic function are isolated. If zeros accumulate at an interior point, every Taylor coefficient vanishes and the function is identically zero in a neighborhood. Repeating across overlapping disks gives the identity theorem on a connected region. It is why analytic continuation, when it exists, is unique: two holomorphic candidates agreeing on even a small open set must agree wherever both are defined on a connected domain.

It also gives us a reliable way to discuss nonvanishing. If we know f is holomorphic and nonzero at a particular point, continuity keeps it nonzero in some neighborhood. If f vanishes to order m, its logarithmic derivative, f prime divided by f, behaves near that point like m divided by z minus a plus a harmless holomorphic term. A zero becomes a simple pole of the logarithmic derivative, carrying a whole-number weight.

## Laurent series and residues

What if a function really does have a singularity at the center? On a ring-shaped region, the series can contain negative powers as well as positive powers. This is a Laurent series. A term like one over z minus a cannot appear in an ordinary Taylor series at a, but it makes perfect sense on a punctured disk.

The coefficient of that reciprocal term has a special name: the residue. Integrate the Laurent series term by term around a circle in the annulus. Every integer power except the power negative one has integral zero. The reciprocal contributes two pi i. So the contour integral divided by two pi i extracts the residue.

For instance, one divided by z times z minus one has a pole at zero and another at one. Near zero it expands as negative one over z minus one minus z minus z squared, and so forth. Its residue at zero is negative one. At one its residue is positive one. A contour enclosing both poles has integral zero because those residues cancel. A contour enclosing just one gives the corresponding nonzero answer.

More generally, we can divide a region with several isolated poles into pieces and small circles around the poles. The interior boundaries cancel, just as triangle edges did. The remaining contour integral is two pi i times the sum of the residues inside. This is the residue theorem. The important qualification is that only isolated singularities are involved and the contour stays away from them.

For prime-number questions, the residue of zeta at its pole will encode a main term, while zeros of zeta will make singularities in its logarithmic derivative. Contour integrals provide a disciplined way to account for those contributions. But this lecture has not proved any theorem about the distribution of primes. It has proved why holomorphic functions are rigid, why a contour can recover a central value, and why singularities contribute discrete terms. Those are the analytic tools a proof of the prime number theorem must use, not a substitute for the remaining argument.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### The contour and circle integrals

For a piecewise continuously differentiable path \(\gamma:[a,b]\to\mathbb C\),
\[
\int_\gamma f(z)\,dz=\int_a^b f(\gamma(t))\gamma'(t)\,dt.
\]
If \(C_r:a+re^{it}\) for \(0\le t\le2\pi\), then
\[
\oint_{C_r}\frac{dz}{z-a}=2\pi i,\qquad
\oint_{C_r}(z-a)^k\,dz=0\quad(k\in\mathbb Z,\ k\ne-1).
\]

### Cauchy-Goursat on a triangle: quantitative proof sketch

Let \(I_0=\oint_{\partial T_0}f(z)\,dz\). After \(n\) subdivisions choose nested \(T_n\) with
\[
|I_n|\ge |I_0|/4^n,\quad\operatorname{diam}(T_n)=2^{-n}\operatorname{diam}(T_0),\quad
\operatorname{length}(\partial T_n)=2^{-n}\operatorname{length}(\partial T_0).
\]
At the unique limit point \(z_0\), \(f(z)=f(z_0)+f'(z_0)(z-z_0)+\epsilon(z)(z-z_0)\), \(\epsilon(z)\to0\). The constant and affine terms have primitives. For sufficiently large \(n\),
\[
|I_n|\le\sup_{T_n}|\epsilon|\,\operatorname{diam}(T_n)\,\operatorname{length}(\partial T_n)
\le\sup_{T_n}|\epsilon|\, 4^{-n}C.
\]
Therefore \(|I_0|\le C\sup_{T_n}|\epsilon|\to0\). This proves the triangle theorem without assuming continuous \(f'\). Extending it to general disk-boundary contours requires triangulation or polygonal approximation and the usual boundary regularity. The removable-singularity and Laurent theorems are standard consequences of Cauchy's formula on circles/annuli; the spoken proof explains their construction.

### Integral formula, estimates, and zeros

For a positively oriented simple boundary \(C\) with \(f\) holomorphic in a neighborhood of its interior and closure,
\[
f(a)=\frac{1}{2\pi i}\oint_C\frac{f(z)}{z-a}\,dz,
\qquad
f^{(n)}(a)=\frac{n!}{2\pi i}\oint_C\frac{f(z)}{(z-a)^{n+1}}\,dz.
\]
For a circle radius \(R\) and \(M_R=\max_{|z-a|=R}|f(z)|\),
\[
|f^{(n)}(a)|\le\frac{n! M_R}{R^n}.
\]
If \(f\not\equiv0\), \(f(a)=0\) of order \(m\) implies \(f(z)=(z-a)^m g(z)\) with \(g(a)\ne0\), hence
\[
\frac{f'(z)}{f(z)}=\frac{m}{z-a}+\frac{g'(z)}{g(z)}.
\]
For a meromorphic function, poles contribute negative integer residues to \(f'/f\). Integrating \(f'/f\) around a contour yields \(2\pi i\) times number of zeros minus poles, counted with multiplicity, provided none lie on the contour.

### Laurent series and residues

In an annulus \(r<|z-a|<R\), \(f(z)=\sum_{n\in\mathbb Z}c_n(z-a)^n\), where
\[
c_n=\frac{1}{2\pi i}\oint_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}\,dz,
\quad r<\rho<R.
\]
Thus \(\operatorname{Res}_{a} f=c_{-1}\). With \(f(z)=1/[z(z-1)]\),
\[
\operatorname{Res}_{0} f=-1,\qquad \operatorname{Res}_{1}f=1.
\]
For a positively oriented simple contour \(C\) whose interior contains finitely many poles and no singularity on \(C\), \(\oint_C f(z)dz=2\pi i\sum_{a\text{ inside}}\operatorname{Res}_a f\).

### Exercises

1. Parameterize a clockwise circle and show explicitly how the sign of \(\int (z-a)^{-1} dz\) changes.
2. Using Cauchy's formula, calculate \(\oint_{|z|=2} e^z/z^3\,dz\).
3. Verify that conjugation has different directional difference quotients at every point, while \(z\mapsto z^3\) is holomorphic.
4. Expand \(1/[z(z-1)]\) in a Laurent series valid for \(0<|z|<1\), and in another valid for \(|z|>1\). Compare which contour each series describes.
5. Apply the argument principle to \(f(z)=z^3(z-2)/(z+1)\) on \(|z|=3\) and explain the result without performing the contour integral.

### Reading and source notes

- MIT OpenCourseWare, [18.04 Complex Variables with Applications: lecture notes](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/): the complex derivative, Cauchy-Goursat, integral formula, Laurent expansions, and residues; see the indexed lecture topics.
- MIT OpenCourseWare, [18.112 Functions of a Complex Variable](https://www.ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/resources/lecture-notes/): lecture sequence 8-14 for contours and isolated singularities.
- Wikipedia: [Holomorphic function](https://en.wikipedia.org/wiki/Holomorphic_function), [Cauchy's integral formula](https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula), [Laurent series](https://en.wikipedia.org/wiki/Laurent_series), [Residue theorem](https://en.wikipedia.org/wiki/Residue_theorem), [Argument principle](https://en.wikipedia.org/wiki/Argument_principle).
