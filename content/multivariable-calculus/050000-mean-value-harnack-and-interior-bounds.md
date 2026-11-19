# Mean Values and Harnack: From Averages to Pointwise Bounds

**Track:** Multivariable Calculus from First Principles. **Focus:** harmonic mean values, Poisson kernel, quantitative Harnack inequalities, gradient bounds, and what survives for rough coefficients.

<!-- BEGIN SPOKEN LECTURE -->

# Mean Values and Harnack: From Averages to Pointwise Bounds

A harmonic function has a property that would sound implausible for a general smooth function: its value at the center of a circle is exactly the average of its values around that circle. If the circle lies entirely inside the domain, the equality holds regardless of how irregular the boundary of the larger domain might be.

This mean-value property is the starting point for several of the strongest qualitative results about elliptic equations. It makes the strong maximum principle intuitive. It produces a formula for the solution inside a disk from values on the circle. And, for positive harmonic functions, it leads to a quantitative comparison between the value at the center and values at other interior points. That comparison is called Harnack's inequality.

We have already seen that energy estimates control gradients in an integral sense, while maximum principles control the allowed range of values. Harnack's inequality bridges those perspectives. It says that a nonnegative harmonic function cannot be extremely large at one interior point and extremely small at a nearby interior point unless the geometry permits the influence of the boundary to become strong.

## Why averages stay fixed as circles grow

Work in the plane, and let u be a smooth harmonic function, so the Laplacian of u is zero. Choose a point x nought and a disk centered there whose closure is contained in the domain. For every radius smaller than that disk's radius, form the average of u around the circle of that radius.

Now differentiate this average with respect to the radius. The derivative is the average radial derivative, which is the average outward normal derivative along the circle. Multiply and divide by the circumference. The divergence theorem converts the total outward normal derivative into the integral of the Laplacian over the enclosed disk. But the Laplacian is zero. Therefore the derivative of the circle average is zero.

The circle average does not change with the radius. As the circle shrinks to the center, continuity makes the average tend to the value of u at x nought. So every circle average equals the center value. Averaging once more over radii gives the corresponding mean-value property for the whole disk.

A concrete harmonic function makes the cancellation visible. Take u of x and y equal to three plus two x minus y. Around a circle centered at any point, the positive and negative contributions of the linear terms cancel. The average is the value at the center. The same property holds for nonlinear harmonic functions such as x squared minus y squared. Here the square terms balance because their circle averages agree.

The mean-value theorem is much more specific than the assertion that an average lies between a minimum and a maximum. A generic function certainly has that weaker property, but its circle average usually changes as the radius changes. Harmonicity is what keeps the average fixed.

## The strong maximum principle in one picture

Suppose a harmonic function reaches its greatest value at an interior point. Consider a small circle around that point. Every value on the circle is at most the maximum. Yet their average must equal the maximum itself. An average of numbers all at most M can equal M only if every number on the circle equals M.

So the function is constant on that circle. Repeating the argument at nearby interior centers and using the connectedness of the domain propagates that equality throughout the domain. This gives the strong maximum principle: a nonconstant harmonic function on a connected domain cannot attain an interior maximum. Apply the same reasoning to negative u and obtain the corresponding minimum principle.

Now consider a nonnegative harmonic function that equals zero at one interior point. Zero is its minimum. The strong principle forces the function to be zero throughout that connected domain. Otherwise, a nonnegative harmonic function is strictly positive everywhere inside. This dichotomy will matter when we divide by a value of the solution in order to compare relative sizes.

The source term changes the story. The function one minus x squared minus y squared is positive inside the unit disk and zero at its edge. Its negative Laplacian equals four. Its circle average at radius r is one minus r squared, which is not equal to its center value of one. We must not apply harmonic mean-value identities to an arbitrary solution of Poisson's equation.

## From circle averages to the Poisson kernel

For a harmonic function inside the unit disk, knowing its boundary values is enough to reconstruct it. The formula uses a positive weight called the Poisson kernel. If the interior point has polar coordinates radius r and angle theta, and the boundary point has angle t, the weight is one minus r squared divided by one minus two r times cosine of theta minus t, plus r squared.

Divide the integral by two pi and integrate the boundary values against that weight over a full turn. The result is u at the interior point. At the center, r equals zero, and every boundary point has weight one. So the formula reduces to the ordinary mean-value property.

Why isn't the weight uniform away from the center? Because a point near the edge is more influenced by the nearby portion of that edge. The denominator is the squared distance between the interior point and the unit boundary point. A smaller distance means a larger weight. The kernel is nevertheless normalized: its average over the boundary circle equals one.

The Poisson kernel has the properties we need for a physical averaging rule. It is positive, and its total mass is one. Therefore a harmonic value inside the disk is a weighted average of the boundary values. It cannot exceed their maximum or fall below their minimum.

This formula also gives a precise view of the maximum principle. The ordinary mean-value property uses uniformly weighted circles centered on the observation point; the Poisson formula uses a nonuniformly weighted boundary circle centered on the disk. Both express an internal value as an average, and both are tied to the Laplace equation rather than to arbitrary smoothness.

For a disk of radius capital R instead of one, the same formula holds after scaling. The numerator becomes R squared minus r squared, and the denominator becomes R squared minus two R r times the cosine of the angular difference, plus r squared.

## Derive Harnack's inequality by bounding the weights

Assume u is positive and harmonic in the unit disk. Fix a point at distance r from its center. In the Poisson kernel, the denominator is the squared distance from our interior point to a boundary point. That distance ranges between one minus r and one plus r. Thus the denominator lies between the squares of those two quantities.

The smallest possible Poisson weight is one minus r divided by one plus r. The largest is one plus r divided by one minus r. Both numbers are positive because r is less than one.

Since the boundary values are nonnegative, multiplying them by the kernel's lower or upper bound and integrating preserves the inequality. The integral of the boundary values with uniform weight is u at the center. Therefore u at radius r lies between two multiples of the center value: the lower multiple is one minus r over one plus r; the upper multiple is one plus r over one minus r.

That is Harnack's inequality for the planar unit disk. Its content is stronger than positivity. If u at the center is one and r is one half, then u anywhere on that smaller circle must lie between one third and three. We did not need to know the actual boundary data to state this comparison.

There is a technical refinement. A positive harmonic function need not extend continuously all the way to the boundary of the unit disk. To avoid assuming it does, perform the Poisson calculation on a smaller closed disk of radius rho, with r less than rho less than one. Then let rho approach one. This yields the same inequality for every positive harmonic function defined on the open unit disk.

It is also useful to see why the constants become large as r approaches one. Near the boundary, a positive harmonic function can be strongly influenced by data concentrated in a very small arc. A fixed center value does not prevent increasingly large values close to the edge. The Harnack estimate is deliberately an *interior* comparison.

## The constants are genuinely sharp

Can the upper and lower factors be improved uniformly for all positive harmonic functions? No. Consider the Poisson kernel itself, regarded as a function of the interior point with its source concentrated at the boundary point one on the real axis. It can be written as one minus the squared distance to the origin, divided by the squared distance to the boundary point one.

This function is positive and harmonic inside the unit disk. At the center it equals one. On the positive real axis at radius r, its value is exactly one plus r divided by one minus r: the upper Harnack bound. On the negative real axis, it equals one minus r over one plus r: the lower bound. The same function realizes both extremes at opposite points.

There is a caveat that clarifies the construction. This boundary-point kernel is singular as we approach the chosen boundary point. It does not arise from a bounded continuous boundary temperature there. It is nevertheless a legitimate positive harmonic function on the open disk. Smooth boundary data concentrated near that point can approximate these extreme ratios. Thus the sharpness concerns the class of positive interior harmonic functions, not a fixed uniformly bounded boundary class.

Contrast this with a gentle example: u of x and y equal to one plus one half times x. It is positive and harmonic in the unit disk. At radius one half on the positive x axis, its value is one and one quarter, safely between one third and three. Most functions do not saturate the bound, but all positive harmonic functions obey it.

## Pointwise control of a derivative

The Poisson formula can do something else. Differentiate it with respect to the observation point while that point is at the center. The derivative of the kernel is explicit. In the planar disk of radius R, the gradient of u at the center is twice one over R times the average of the boundary values multiplied by the outward unit direction.

Taking absolute values gives a gradient bound: the size of the gradient at the center is at most twice the largest absolute boundary value divided by R. This makes dimensional sense. The gradient measures change per unit length, so the bound must contain one inverse power of the disk radius.

For a positive harmonic function we get an even more informative version. The boundary values are nonnegative, and their average equals the center value. Hence the gradient magnitude at the center is at most twice the center value divided by R. Divide both sides by the positive center value. The gradient of the logarithm of u is bounded in magnitude by two over R.

Choosing disks centered at different interior points gives a local bound in terms of the distance to the domain boundary. This is another way to express a Harnack-type idea: the logarithm of a positive harmonic function cannot change arbitrarily fast at a point far from the boundary. Integrating such a bound along suitable interior paths gives comparisons of values, although generally with less sharp constants than the explicit Poisson-kernel inequality.

No equivalent gradient statement follows automatically for a scalar divergence-form equation with merely bounded measurable coefficients. Its weak solutions may be Hölder continuous without possessing classical gradients everywhere. We must not substitute the regularity of the Laplace equation for the regularity of every elliptic operator.

## What survives when conductivity is rough?

Suppose we replace the Laplacian by negative divergence of A gradient u, where A is uniformly elliptic and bounded but may jump or oscillate. The ordinary circle average of u is no longer necessarily equal to its center value. The explicit Poisson kernel for the Laplacian is not the representation kernel of this operator.

Yet a powerful qualitative analogue survives for scalar homogeneous equations. Under uniform ellipticity and the standard weak-solution hypotheses, the De Giorgi–Nash–Moser theory gives local Hölder continuity and a Harnack inequality for nonnegative solutions. On a smaller ball strictly inside a larger ball, the supremum is bounded by a fixed multiple of the infimum. The multiplicative constant depends on the dimension, the ellipticity bounds, and the ratio of the radii, not on the particular solution.

Proving that theorem requires substantially more than the elementary Poisson-kernel argument. One important route combines the local Caccioppoli inequality with Sobolev inequalities, truncation, and iteration. We have already developed the first ingredients. The full iteration is a later topic; the theorem here explains what those ingredients are ultimately for.

Do not carry the conclusion over without checking the setting. For equations with forcing, the estimate usually needs an additional load term and suitable integrability assumptions. For equations with lower-order coefficients, sign and size conditions matter. For general elliptic systems, scalar maximum principles and Harnack inequalities can fail. And at a rough boundary, interior regularity does not automatically become boundary regularity.

## A hierarchy of information

It is now possible to state precisely what different elliptic tools reveal. The weak energy method gives existence and stability in H one. Caccioppoli estimates control local gradient energy from surrounding values. Maximum principles and barriers provide sign information and uniform bounds when the operator preserves order. Green functions express the solution as an integral response when a suitable kernel exists. Mean values and Poisson kernels yield exact formulas for harmonic functions. Harnack inequalities add a quantitative restriction on how positive solutions can vary inside a domain.

The hierarchy matters because no single method supplies all these conclusions at once. A solution may have a rigorous energy bound without a pointwise formula. A harmonic function may have perfect interior smoothness while its gradient becomes large close to the boundary. A piecewise-rough conductivity may preserve scalar Harnack control while destroying an H-two estimate. Recognizing which theorem answers which question is a major part of learning elliptic PDEs.

The path from multivariable calculus to elliptic theory started with gradients, Hessians, and quadratic energy. It now reaches properties of entire functions that cannot be read off from any one point: conservation, positivity, reciprocity, stability, and interior comparability. Those properties are the foundation for analyzing more complicated equations, numerical schemes, and inverse problems where exact solutions are no longer available.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Mean value from the divergence theorem

For harmonic \(u\in C^2(B_R(x_0))\), let
\[
M(r)=\frac1{2\pi}\int_0^{2\pi}u(x_0+r(\cos t,\sin t))\,dt.
\]
Then \(M'(r)=(2\pi r)^{-1}\int_{\partial B_r(x_0)}\partial_nu\,ds=(2\pi r)^{-1}\int_{B_r(x_0)}\Delta u\,dx=0\), and \(M(r)=u(x_0)\). Integrate the circle averages against \(2r/R^2\) to obtain the disk average.

### Poisson representation and planar Harnack

For \(u\) harmonic on a neighborhood of \(\overline{B_1}\) and boundary values \(g\),
\[
u(re^{i\theta})=\frac1{2\pi}\int_0^{2\pi}\frac{1-r^2}{1-2r\cos(\theta-t)+r^2}g(e^{it})\,dt.
\]
The kernel \(P_r\) integrates to 1 against \(dt/(2\pi)\). Its extrema are
\[
\frac{1-r}{1+r}\le P_r(\theta-t)\le\frac{1+r}{1-r}.
\]
For \(u>0\), integrate against nonnegative boundary values and use the mean value at the center:
\[
\boxed{\frac{1-r}{1+r}u(0)\le u(re^{i\theta})\le\frac{1+r}{1-r}u(0).}
\]
For an arbitrary positive harmonic function on the *open* disk, repeat on \(B_\rho\), \(r<\rho<1\), then take \(\rho\uparrow1\).

### A sharp positive harmonic example

\[
h(z)=\operatorname{Re}\frac{1+z}{1-z}=\frac{1-|z|^2}{|1-z|^2},\qquad |z|<1.
\]
It is harmonic and positive, \(h(0)=1\), and \(h(r)=(1+r)/(1-r)\), \(h(-r)=(1-r)/(1+r)\). Thus the two bounds are attained within the class of positive harmonic functions on the open disk.

### Interior gradient estimate in two dimensions

For harmonic \(u\) on a neighborhood of \(\overline{B_R(0)}\), differentiating the radius-\(R\) Poisson formula at the origin gives
\[
\nabla u(0)=\frac2R\int_0^{2\pi}u(Re^{it})(\cos t,\sin t)\,\frac{dt}{2\pi}.
\]
Hence \(|\nabla u(0)|\le (2/R)\sup_{\partial B_R}|u|\). If \(u>0\), positivity and the mean-value identity sharpen the right side to \((2/R)u(0)\). On a general domain this applies on every disk compactly contained in the domain.

### Exercises and answers

1. **Harmonic test.** Is \(u(x,y)=x^2-y^2+3\) harmonic? **Answer:** Yes, its Laplacian is 2 minus 2, equal to zero.
2. **Not harmonic.** Find the circle average at radius r of \(u=1-x^2-y^2\). **Answer:** \(1-r^2\); it does not equal \(u(0)=1\) for positive r.
3. **Harnack scale.** If \(u(0)=5\) and \(|z|=1/3\), what bounds follow? **Answer:** \(5/2\le u(z)\le10\).
4. **Sharpness.** Evaluate \(h(z)=\operatorname{Re}((1+z)/(1-z))\) at \(z=1/2\) and \(-1/2\). **Answer:** Three and one third, the sharp Harnack endpoints for r equal to one half.
5. **Rough coefficients.** Why can't we use the Poisson formula directly for \(-\nabla\cdot(A(x)\nabla u)=0\) with variable A? **Answer:** The kernel is specific to the Laplacian; the weighted equation generally lacks the ordinary circle mean-value property.

### Sources and further reading

- [MIT OpenCourseWare, *Introduction to Partial Differential Equations*, lectures 1, 2 and 9](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2005/pages/lecture-notes/), mean values, Harnack's inequality, and gradient bounds.
- [Queen Mary University of London, *Potential Theory* notes, positive harmonic functions](https://webspace.maths.qmul.ac.uk/b.khoruzhenko/potential_th_notes%202.pdf), Poisson integral and Harnack on disks.
- [Connor Mooney, *Notes on Elliptic Partial Differential Equations*](https://www.math.uci.edu/~mooneycr/EllipticPDE_BasicTheory.pdf), local boundedness and rough-coefficient Harnack theory.
- [Wikipedia: Harmonic function](https://en.wikipedia.org/wiki/Harmonic_function); [Wikipedia: Harnack's inequality](https://en.wikipedia.org/wiki/Harnack%27s_inequality), broader context.
- Companion in this library: `multivariable-calculus:049000` for Caccioppoli and `multivariable-calculus:047000` for comparison principles.
