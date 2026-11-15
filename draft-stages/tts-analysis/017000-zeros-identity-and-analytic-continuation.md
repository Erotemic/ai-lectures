# 017000 — Power Series, Isolated Zeros, and Analytic Continuation

**Track:** Analysis from First Principles. **Background:** Cauchy's integral formula, limits of power series, complex derivatives, connected open sets. **Theme:** local Taylor data control a holomorphic function; a zero is either isolated with a definite order or forces the function to vanish on a connected domain.

<!-- BEGIN SPOKEN LECTURE -->

# Power Series, Isolated Zeros, and Analytic Continuation

Consider a question about information. Suppose a function is defined on a disk in the complex plane, and you measure it at a few locations. Can those measurements force its values everywhere else? Usually not. A continuous function can be adjusted between any finite collection of samples. Even a smooth function of two real variables can hide a bump inside a tiny region without changing its values outside that region.

But if the function is holomorphic, knowing its values on an infinite set can be enough to determine it everywhere on a connected region. There is a condition on that set: the sample points must accumulate at a point inside the region. There is also a condition on the function: complex differentiability must hold on an open set, not just along a line. Under those hypotheses, two holomorphic functions that agree on the sample points agree on the whole connected region.

This is the identity theorem. It sounds implausibly strong if we think of a function as an arbitrary graph. It begins to feel natural if we think of holomorphic functions as locally convergent power series. A convergent power series cannot have infinitely many zeros approaching its center unless every coefficient vanishes. The proof turns that observation into a precise statement, and then uses connectedness to propagate it beyond one disk.

Along the way we will distinguish three ideas that are often blurred together: the convergence of a Taylor series, the order of a zero, and analytic continuation. Each is a different way of understanding how nearby complex values constrain one another.

## Why Taylor series are exact here

In ordinary real calculus, Taylor's theorem provides a polynomial approximation, often with a remainder estimate. Infinite differentiability alone does not guarantee that the full Taylor series converges to the original real function. We can build a real function that is infinitely differentiable, has every derivative equal to zero at the origin, and yet is positive at every nearby positive input. Its Taylor series at the origin is identically zero, but the function is not.

Holomorphicity changes that situation. If a function is holomorphic on an open region containing a closed disk centered at a, then Cauchy's integral formula expresses its value inside the disk as an integral over the boundary. In the integrand sits a fraction with a denominator involving the boundary point minus the interior point. We can rewrite that denominator to reveal a geometric series, because every interior point is strictly closer to a than the boundary is.

Expand that geometric series, and interchange the sum and contour integral. Why is the interchange justified? Fix a smaller closed disk strictly inside the boundary. The geometric series converges uniformly there, even as its terms depend on the boundary point. The contour is finite in length, and the function is bounded on it, so the error in integrating a truncated series tends uniformly to zero.

The resulting coefficients are the familiar derivatives at a divided by the corresponding factorials. Thus the Taylor series does not merely approximate the holomorphic function: it equals the function throughout a disk that fits inside the holomorphic domain. We did not assume beforehand that the Taylor series represents the function. Cauchy's formula proved it.

Here is a concrete example. Consider the function one divided by one minus z. When z has modulus less than one, the geometric series gives one plus z plus z squared, and so on. Its coefficients are all one. Near z equal to zero, the series is not a numerical trick: it is an exact formula for the function. Yet at z equal to one, the original function is undefined. The Taylor series centered at zero cannot converge past the circle of radius one. The obstruction is a singularity of the function, not a failure of our patience in adding terms.

A less obvious example is one divided by one plus z squared. On the real line it behaves smoothly for every real input. Nevertheless, its Taylor series about zero has radius one, because the function has poles at i and negative i. The complex plane reveals obstacles that cannot be seen by looking only at the real line.

Be precise about the radius. A Taylor series represents its function on the largest open disk about its center on which that expansion converges. Sometimes a function can be continued outside that disk along a different route. A disk of convergence is not a claim that the function ceases to exist everywhere outside it. The example one divided by one minus z remains perfectly well defined at z equal to two. Its expansion about zero simply cannot reach that point in a single convergent Taylor disk.

## How many zeros can a nonzero holomorphic function have?

Now suppose a holomorphic function f is zero at some point a. Its Taylor series at a begins with a constant coefficient, which must be zero. Perhaps the coefficient of the first power is also zero. Perhaps the first several coefficients vanish. If there is a first nonzero coefficient, say at power m, we can factor that power out of the series.

The function becomes the m-th power of z minus a, multiplied by another holomorphic function that is nonzero at a. By continuity, that second factor remains nonzero throughout a sufficiently small disk. Within that disk, f can therefore vanish only at the center. The zero is isolated. The number m is called its multiplicity or order.

This factorization gives a useful interpretation of multiplicity. A simple zero has order one. Near it, the function behaves approximately like a nonzero constant times z minus a. A double zero behaves like a nonzero constant times the square of z minus a. If we travel once around the center on a small circle, the dominant local model rotates the output around zero once for a simple zero, twice for a double zero, and m times for an order-m zero. That winding picture will eventually let contour integrals count zeros.

For example, take f of z equal to z squared times one plus z. At zero there is a zero of order two, because the factor one plus z is holomorphic and nonzero there. At negative one there is a zero of order one. The polynomial is not identically zero, so these zeros are isolated.

What if there is no first nonzero Taylor coefficient? Then every coefficient is zero. The Taylor series is identically zero, and because the Taylor series represents the function on a disk, f vanishes throughout that disk. We obtain a sharp local alternative: either a zero has finite order and is isolated, or the function is identically zero on a neighborhood.

There is no third option in which a nonzero holomorphic function has increasingly dense zeros near an interior point. That is exactly the option smooth real functions can sometimes exhibit. Complex holomorphicity rules it out.

## A sequence of zeros that gives away the whole function

Imagine a sequence of distinct points approaching a, where all the points and their limit a belong to a connected open region. Suppose f is holomorphic on that region, and f vanishes at every point of the sequence. Continuity tells us f at a must also vanish. If that zero had finite order, a sufficiently small punctured disk around a would contain no other zeros. But our sequence supplies zeros arbitrarily close to a. Contradiction. So f must vanish on a whole small disk around a.

This is already surprising: samples on a sequence have determined an open patch of the function. To extend the conclusion to the entire connected region, we use a simple topological idea. Call a point a zero-neighborhood point if f vanishes on some open disk around it. The set of these points is open by definition. It is also closed relative to the region. Indeed, if zero-neighborhood points approach b, then they give a sequence of zeros approaching b; by the same local reasoning, f vanishes on a neighborhood of b.

A connected region cannot be split into two nonempty disjoint sets that are both open and closed relative to it. Since we have at least one zero-neighborhood point, every point of the region must be such a point. The function is zero everywhere.

Apply this to the difference of two holomorphic functions. If they agree at a sequence with a limit inside their connected common domain, the difference has accumulating zeros and must vanish everywhere. That is the identity theorem.

The condition that the accumulation point lie inside the domain matters. Consider sine of pi times z. It vanishes at every integer, but the integers do not accumulate at any finite point. This function is emphatically not zero everywhere. We can also take the geometric series example: a sequence approaching the boundary point one can be prescribed without obtaining the same conclusion from the identity theorem on the unit disk, because the limit lies outside the disk.

The condition that the domain be connected matters as well. On one component, a function can be identically zero; on a disjoint component, it can be one. Both pieces are holomorphic. Nothing forces information to cross a gap between components that the function's domain never connects.

## An equality verified on a real interval

Here is a useful consequence. Suppose f and g are holomorphic on the same connected complex region containing a nontrivial interval of the real line. If they agree at every real point of that interval, they agree throughout the complex region. We do not need agreement on an open patch of the complex plane. A real interval is already an infinite set with interior accumulation points in the complex region.

This fact justifies many familiar identities for the complex exponential, sine, and cosine. If both sides are holomorphic on the connected region in question, and we establish an identity on a real interval, the identity holds throughout that region. But the holomorphic-domain condition is doing real work. Equality on the real axis between two merely smooth functions of two real variables would prove nothing about their values elsewhere in the plane.

It also suggests why we cannot arbitrarily patch together holomorphic formulas. Suppose I define a function to agree with one formula on the left half of a connected region and a different one on the right, while claiming the combined function is holomorphic everywhere. If the two formulas agree on an overlap with an accumulation point, the identity theorem forces them to describe the same holomorphic function throughout their common connected domain. If they do not, the patch must fail to be holomorphic somewhere.

This is a mathematical form of rigidity, not a statement about ease of numerical reconstruction. An identity theorem promises uniqueness, not stability. Very small measurement errors can make the task of reconstructing values far away from the sampling interval drastically ill-conditioned. Uniqueness of an exact answer should never be confused with robustness of an approximation.

## Continuing a function by overlapping disks

Now think about the geometric series for one divided by one minus z. Its Taylor series at zero reaches only the unit disk. Yet the rational function is defined at z equal to two. How might we reach two if all we were given was the power series at zero?

Move to a point inside the original convergence disk, perhaps one half. We know the function and all its derivatives there, so we can construct a new Taylor series centered at one half. That series may reach beyond the original disk. We can continue this process with a chain of overlapping disks, always requiring the new formula to agree with the old formula where both are defined.

This process is analytic continuation. At each overlap the identity theorem prevents arbitrary choices: once the values on the overlap are fixed, there is at most one holomorphic continuation across it. But continuation along distinct paths need not give a single global function on a region with holes. The complex logarithm supplies the warning.

Near the positive real number one, choose a holomorphic logarithm whose value at one is zero. Differentiate it; the derivative is one divided by z. Continue that local logarithm along a path that circles once counterclockwise around the origin. Locally the derivative still equals one divided by z, but when we return to the starting point, the continued logarithm has increased by two pi i. We have returned to the same input and a different output. The obstruction is the nonzero integral of one divided by z around that loop.

There is no contradiction with local uniqueness. Along each small overlapping segment, the continuation is uniquely determined. The global result can depend on the route because a single-valued holomorphic logarithm cannot exist on the entire punctured plane. Analytic continuation is controlled by local agreement and by the topology of the region through which we try to continue.

The square root offers another accessible version: begin with a chosen square root near one, continue it once around the origin without crossing it, and you return to the negative of the initial value. Two turns return to the original. These examples illustrate why the word 'analytic' refers not merely to being able to write a series at one point, but to a coherent system of local series and their possible continuation.

## What the local information can and cannot do

We have developed three progressively stronger statements. Cauchy's formula says a holomorphic function equals its Taylor series locally. That local expansion says every zero of a nonzero holomorphic function has a definite finite multiplicity and is isolated. And the identity theorem says that a set of zeros accumulating at an interior point forces the function to vanish on the entire connected domain.

The qualifications stay important. We need an open region of holomorphicity, not differentiability at one point. We need an accumulation point inside the domain, not merely on its boundary. We need connectedness to propagate a conclusion between neighborhoods. We also must separate analytic uniqueness from numerical stability, and local continuation from a globally single-valued formula.

Once these distinctions are secure, a further question becomes compelling. Taylor series involve nonnegative powers. What happens around a point where the function is not holomorphic, but is holomorphic everywhere nearby except at that one point? The function may blow up, remain bounded, or oscillate in complicated ways as we approach the missing center. To describe that behavior, we need to let negative powers enter the expansion. The geometry of an annulus, rather than a filled disk, provides the right setting.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Local Taylor representation and coefficients

Suppose the closed disk \(\overline{D(a,R)}\) lies in an open set on which f is holomorphic. Then for |z-a|<R,

\[
f(z)=\sum_{n=0}^{\infty}c_n(z-a)^n,
\qquad c_n=\frac{f^{(n)}(a)}{n!}
=\frac{1}{2\pi i}\oint_{|\zeta-a|=R}\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta.
\]

Derivation: write \(1/(\zeta-z)=(1/(\zeta-a))\sum_{n\ge0}((z-a)/(\zeta-a))^n\). On each smaller closed disk \(|z-a|\le r<R\) the series is uniform for \(|\zeta-a|=R\), permitting integration termwise. If the original domain is only an open disk, use any \(r<R\) as the contour radius, not the boundary of an open domain itself.

**Zero-order factorization:** If f is not identically zero on a connected domain and f(a)=0, there exists m>=1 and a holomorphic g near a such that
\[f(z)=(z-a)^m g(z),\qquad g(a)\ne0.\]
Hence zeros are isolated and multiplicity m is well-defined. The identity theorem follows from the existence of a limiting zero in the domain and connected propagation.

**Smooth-real counterexample:** \(h(x)=e^{-1/x^2}\) for x>0 and h(x)=0 for x<=0 has all derivatives zero at zero but is not represented by its Taylor series there. It is a function of a real variable, not holomorphic on a complex neighborhood of zero.

**Radius example:** \(1/(1+z^2)=\sum_{n\ge0}(-1)^n z^{2n}\) for |z|<1. Poles at +/-i obstruct enlarging the disk about zero.

### Identity theorem: precise statement

Let D be connected and open, and f,g holomorphic on D. If \(\{z_n\}\subset D\) consists of distinct points, f(z_n)=g(z_n) for all n, and z_n tends to a point \(a\in D\), then \(f\equiv g\) on D. Distinctness is essential: repeatedly sampling one point supplies no accumulation of distinct zeros.

**Analytic continuation note:** continuation along overlapping disks is unique on each connected overlap, but a continuation around a loop can return with a different germ when the ambient domain is not simply connected. A holomorphic logarithm is a canonical example; locally \(\mathrm{Log}'(z)=1/z\), and \(\oint_{|z|=1}dz/z=2\pi i\).

### Worked problems

1. **Orders:** Find the multiplicity of the zeros of \(f(z)=z^3(z-2)^2 e^z\). **Answer:** Three at zero and two at two; the exponential has no zeros.
2. **Identity:** Suppose f is entire and \(f(1/n)=0\) for every positive integer n. What is f? **Answer:** f is identically zero because the zeros accumulate at 0, which belongs to the domain.
3. **Boundary trap:** Is it enough to know a holomorphic f on the open unit disk vanishes at \(z_n=1-1/n\) for every n>=2 to conclude f is zero? **Answer:** No. The zeros accumulate only at the boundary point 1. For an explicit nonzero example, use \(f(z)=\sin(\pi/(1-z))\), which is holomorphic on the unit disk and vanishes at those points.
4. **Taylor radius:** Explain why \(1/(1-z)\) has a Taylor radius one at zero though it is defined at z=2. **Answer:** The pole at z=1 obstructs a larger *disk* of convergence; local continuation can reach 2 along paths avoiding 1.
5. **Real versus complex:** If f,g are entire and f(x)=g(x) for every x in (-1,1), what follows? **Answer:** f=g everywhere by the identity theorem.

### Sources and further reading

- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, lectures on power series and holomorphic functions: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, topics 4, 7 and 13: https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- Wikipedia, *Identity theorem*: https://en.wikipedia.org/wiki/Identity_theorem.
- Wikipedia, *Analytic continuation*: https://en.wikipedia.org/wiki/Analytic_continuation.
