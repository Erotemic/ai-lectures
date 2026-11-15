# 021000 — The Maximum Modulus Principle: Why the Interior Cannot Hide a Peak

**Track:** Analysis from First Principles. **Background:** holomorphic functions, complex power series, Cauchy's integral formula, compactness. **Question:** How can values on a boundary constrain every point inside, and exactly which assumptions make that possible?

<!-- BEGIN SPOKEN LECTURE -->

# The Maximum Modulus Principle: Why the Interior Cannot Hide a Peak

Imagine drawing a circle in the complex plane and recording the magnitude of a complex-valued function around that circle. Now try to choose its value at the center independently. If the function is merely continuous, there is almost no restriction: you can place a large bump at the center and taper it smoothly to zero at the boundary. If the function is holomorphic, the situation is profoundly different. Its value at the center is an average of its values around the circle. You cannot quietly insert a peak in the middle without changing what happens on the surrounding curve.

This is the intuition behind the maximum modulus principle. The surprising part is not just that the boundary controls the center of one disk. It is that a nonconstant holomorphic function cannot achieve even a *local* maximum of its absolute value at any interior point of a connected open region. To see why, we will start with a concrete example, extract the mechanism from Cauchy's formula, and then examine what breaks when the hypotheses change.

## A model you can hold in your head

Take the function that returns its input: f of z equals z. On a disk of radius two centered at the origin, its absolute value is simply the distance from the origin. At the center it is zero; on the surrounding circle it is two. No interior point can have magnitude larger than the boundary magnitude. That example may seem too simple. Try replacing z by z squared: its magnitude is the square of the distance, and again the largest magnitude occurs at the rim. Try a polynomial with many terms, where the values oscillate and interfere. The graph becomes difficult to picture, but the same conclusion survives.

Be careful about the statement. We are not saying that the function's real part increases toward the boundary, nor that its magnitude is monotone along each radius. There can be many rises and falls. The claim is about the *largest* magnitude in a region, not an ordering along a path. Nor does every boundary point have to be large. The function might be tiny on most of the boundary and large on a short arc. The theorem says the interior cannot surpass the highest boundary magnitude.

Why should a complex derivative, a local condition, prevent a global interior peak? The bridge is the integral formula. Holomorphicity on a neighborhood of a closed disk permits us to compute the center value by averaging the function around the circle. Averages do not exceed the maximum magnitude of what they average. But that argument alone seems to leave open one possibility: the center could equal the maximum while all values around the circle somehow combine just right. To rule that out for a nonconstant function, we must examine the equality case.

## The ordinary bound is easy; the equality case does the work

Let a be a point inside a region where f is holomorphic. Choose a small circle around a that stays inside the region. Cauchy's formula says the value at a is the average of the values of f on that circle, with the circle parameterized at constant angular speed. When we take absolute values and apply the triangle inequality, the magnitude at a is at most the average of the magnitudes on the circle. That average, in turn, is at most the largest magnitude there.

So every disk gives a center-to-circle bound. Suppose, however, that the absolute value at a is already a local maximum. On a sufficiently small disk, every point on its boundary has magnitude at most the magnitude at a. Put the inequalities together. The center is at most the average, and the average is at most the center. Equality must hold throughout.

What does equality mean? Think of complex numbers as arrows. Their average can have the same length as every contributing arrow only when those arrows do not point in different directions. Any angular disagreement would shorten the average. Since the average is the center value, all the values around the circle must agree with that center value. Continuity excludes exceptional angular positions. When the center value is zero, the same conclusion follows more simply: nonnegative magnitudes on the circle have average zero, so they are all zero.

There is an even more algebraic way to see the rigidity. Near a, write f as a convergent Taylor series. The average, around a small circle, of the square of the magnitude of f is the square of the center magnitude plus a sum of nonnegative terms. Each extra term corresponds to the squared magnitude of a nonconstant Taylor coefficient, multiplied by a positive power of the radius. If the center is a local maximum, that average cannot exceed the square of the center magnitude. Hence every extra term must be zero. Every nonconstant Taylor coefficient disappears. The function is constant near a.

That final sentence is local. To pass from local constancy to constancy throughout the whole region, we need connectedness and the identity theorem. If a holomorphic function agrees with a constant on one nonempty open disk, it agrees with that constant on the entire connected domain. Thus any interior local maximum of the modulus forces global constancy on the connected component containing that point.

Notice the precise chain: local maximum, circle averages, equality rigidity, local constancy, then connectedness to propagate the result. A slogan about the boundary omits the most important part of the proof.

## From a local prohibition to a boundary theorem

Now suppose our domain is bounded, and f is holomorphic throughout it and continuous on its closure. The closure is compact in the plane, so the continuous function giving the magnitude of f actually attains a largest value there. If f is nonconstant and the domain is connected, that largest value cannot occur at an interior point. Therefore it must occur somewhere on the boundary.

This is often the version used in estimates: on a bounded domain with a continuous extension to the boundary, the largest magnitude of a nonconstant holomorphic function occurs at the boundary. If f is constant, the statement that the boundary also attains the largest magnitude remains true, but the stronger claim of *no interior maximizer* does not.

Consider a disk of radius one centered at zero. Suppose a holomorphic function extends continuously to its boundary and has magnitude at most five everywhere along the circle. The maximum modulus principle tells us its magnitude is at most five everywhere inside. There is no need to sample a grid or search for interior critical points. The complete continuum of interior points is controlled by the boundary condition.

There is also a useful distinction between strict and non-strict bounds. If the function is not constant and the boundary magnitudes are at most five, then every interior magnitude is strictly less than five. If it reached five inside, it would have an interior local maximum and thus be constant. But unless the boundary maximum actually equals five, the true bound may be smaller still.

We have to watch the topology and the regularity conditions. A domain may have holes. The maximum principle still holds, but the boundary then includes the edges of those holes as well as the outer edge. If we estimate only on the outer edge and ignore the inner boundary, we have not bounded the whole domain. Imagine the function one over z on an annulus between two circles. The magnitude is greatest along the inner circle. The inner boundary is not optional data.

## A companion principle for minima, with a crucial exception

There is a corresponding statement about minimum magnitude, but it requires care. Suppose f is holomorphic and never zero on a connected region. Then one over f is holomorphic there. If the magnitude of f had an interior local minimum, the magnitude of one over f would have an interior local maximum. The maximum principle would force one over f, and hence f, to be constant. So a nonconstant *zero-free* holomorphic function has no interior local minimum of its magnitude.

Drop the zero-free condition and that conclusion becomes false. The function z has magnitude zero at the origin, an interior global minimum. Indeed, its zero is the entire reason the minimum is possible. This is not a minor technical exception. It allows the modulus of a holomorphic function to detect zeros: wherever a nonconstant holomorphic function attains a genuine interior minimum, that minimum must be zero.

For example, suppose a holomorphic f on a bounded region extends continuously to the boundary, never vanishes on the closure, and has boundary magnitude at least two. Applying the maximum principle to one over f yields magnitude at least two throughout the region. If f has a zero somewhere inside, taking a reciprocal would not be legal, and the lower bound could fail catastrophically.

## The real part has its own version

The same boundary-control theme appears if we replace magnitude with the real part of a holomorphic function. The real part is harmonic: roughly speaking, its second derivatives in the two coordinate directions cancel. Harmonic functions satisfy a mean-value property. The value at a center equals the average of values on a surrounding circle. Therefore a nonconstant harmonic function cannot have a local interior maximum or minimum on a connected region.

For a simple illustration, let f of z equal z squared. In rectangular coordinates, its real part is x squared minus y squared. Along the horizontal direction the origin looks like a minimum; along the vertical direction it looks like a maximum. Taken together it is a saddle, not a peak. The two directions counterbalance. This is the geometric shadow of the Laplace equation.

The real-part principle can also be used directly for holomorphic functions. If the real part of f reaches a local maximum in the interior, it is constant on the connected region. The Cauchy–Riemann equations then force the imaginary part to be constant as well, so f itself is constant. This explains why the familiar harmonic maximum principle and the holomorphic maximum modulus principle are closely related but not identical statements.

## What happens when the domain is unbounded?

One last example protects us from overgeneralizing. Consider f of z equal to the exponential of negative z squared, but restrict attention to the open upper half-plane. On the real axis, the magnitude is the exponential of negative x squared, so it is at most one. Inside the upper half-plane, along the imaginary axis, z equals i times a positive real number. Then negative z squared is positive, and the magnitude becomes an exponentially growing function. Boundary magnitudes are at most one, while interior magnitudes become arbitrarily large.

There is no contradiction. The usual boundary maximum theorem assumed a bounded domain with compact closure. The upper half-plane is unbounded. Controlling values along its real boundary does not control what happens far away toward infinity. Additional growth restrictions can restore boundary principles on unbounded domains, but they have to be proved and stated.

The local maximum modulus principle never failed in this example. At no interior point does our exponential attain a local maximum of its magnitude. The magnitude simply continues growing as we move upward. The distinction between the local theorem and the compact-boundary corollary is essential.

## What boundary information can and cannot tell us

We have developed three increasingly powerful statements from one source of rigidity. First, Cauchy's integral formula controls a value by nearby values. Second, equality at an interior local maximum forces a holomorphic function to be constant on a connected region. Third, compactness lets us turn the local fact into a boundary estimate on bounded domains.

The principle does not say that boundary data uniquely determine an arbitrary continuous function, nor that the modulus of a holomorphic function moves monotonically toward the boundary. It says that holomorphic functions cannot conceal a new magnitude peak inside. The theorem is a tool for proving bounds without explicitly knowing the function's values at every point. Its full force comes from a structural fact: local complex differentiability couples the values around a point so tightly that an interior extremum becomes an obstruction to nonconstant behavior.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Theorems and hypotheses

Let \(\Omega\subset\mathbb C\) be a **domain** (connected open set), and \(f\in\mathcal O(\Omega)\).

- **Maximum modulus principle:** If \(|f|\) has a local maximum at \(a\in\Omega\), then \(f\) is constant on \(\Omega\).
- **Boundary form:** If \(\Omega\) is bounded and \(f\in\mathcal O(\Omega)\cap C(\overline\Omega)\), then
  \[\max_{\overline\Omega}|f|=\max_{\partial\Omega}|f|.\]
  For nonconstant \(f\), no interior point attains this value.
- **Minimum modulus principle:** If \(f\) is zero-free and nonconstant on a domain, \(|f|\) has no local interior minimum. On a compact closure, \(\min_{\overline\Omega}|f|=\min_{\partial\Omega}|f|\) provided \(f\) is nonvanishing on \(\Omega\) and continuous on the closure (where a boundary zero makes the minimum zero).

### A proof through Parseval on circles

For \(f(z)=\sum_{n\ge0}a_n(z-a)^n\) on \(|z-a|<R\) and \(0<r<R\), uniform convergence on the circle gives
\[
\frac1{2\pi}\int_0^{2\pi}|f(a+re^{it})|^2\,dt
=\sum_{n=0}^\infty |a_n|^2r^{2n}.
\]
If \(|f|\) has a local maximum at \(a\), choose \(r>0\) with \(|f(a+re^{it})|\le |f(a)|=|a_0|\) for all \(t\). Nonnegative summands imply \(a_n=0\) for all \(n\ge1\). Identity theorem supplies global constancy on connected \(\Omega\).

### Useful calculations and failure examples

1. **Cauchy coefficient estimate:** If \(|f|\le M\) on \(|z-a|=R\), \(|f^{(n)}(a)|\le n!M/R^n\). This is a quantitative boundary-to-interior result.
2. **Holes matter:** On \(\Omega=\{1<|z|<3\}\), \(f(z)=1/z\) has \(|f|=1\) at the inner boundary and \(1/3\) at the outer boundary.
3. **An unbounded-domain counterexample:** For \(\Im z>0\), \(f(z)=e^{-z^2}\); boundary modulus \(e^{-x^2}\le1\), while \(|f(iy)|=e^{y^2}\to\infty\).
4. **Zero-free minimum:** If \(f\) never vanishes, \(1/f\) is holomorphic and the maximum principle applies to \(|1/f|\). If \(f(z)=z\), the minimum zero at \(z=0\) is allowed.

### Exercises and answers

1. If \(f\) is holomorphic on a neighborhood of \(\{|z|\le2\}\) and \(|f|\le7\) on \(|z|=2\), how large can \(|f(0)|\) be? **Answer:** At most 7; if equality holds then \(f\) is constant.
2. Suppose \(|f(z)|\ge3\) on \(|z|=1\), and \(f\) is holomorphic and zero-free on a neighborhood of the closed unit disk. Prove the same lower bound inside. **Answer:** Apply maximum modulus to \(1/f\), with boundary modulus at most \(1/3\).
3. Does \(\max_{\{|z|\le1\}}\Re(z^2)=1\) occur in the interior? **Answer:** No; \(\Re(z^2)=x^2-y^2\) is harmonic and nonconstant.
4. Does the boundary conclusion require simple connectivity? **Answer:** No; it requires controlling the entire boundary, including boundaries of holes.
5. Why is connectedness present in the local maximum statement? **Answer:** A function may be constant on one connected component and nonconstant on another; the identity theorem propagates within a component only.

### Sources and further reading

- MIT OCW, *18.112 Functions of a Complex Variable*, Lecture 12: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- Harvard Mathematics 55b complex analysis notes, harmonic and maximum principles: https://abel.math.harvard.edu/~ctm/home/text/class/harvard/55b/10/html/home/course/course.pdf.
