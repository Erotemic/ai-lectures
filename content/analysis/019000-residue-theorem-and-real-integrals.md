# 019000 — The Residue Theorem: One Coefficient Controls an Entire Contour

**Track:** Analysis from First Principles. **Background:** contour integration, Cauchy–Goursat, Laurent expansions, isolated singularities. **Theme:** the residue is the negative-first Laurent coefficient; deformations of contours turn local coefficient data into exact global integrals.

<!-- BEGIN SPOKEN LECTURE -->

# The Residue Theorem: One Coefficient Controls an Entire Contour

Imagine walking once around a closed path in the complex plane while measuring a complex-valued function. The path could be a circle, a rectangle, or a complicated loop. Inside it, the function may have several singularities: points where it is not defined or fails to be holomorphic. Can we compute the entire contour integral without following the path point by point?

Under suitable conditions, yes. We can replace the integral by a finite sum of numbers attached to the enclosed singularities. Each number is a residue, and the entire answer is two pi i times their sum. The remarkable part is that a residue depends only on the behavior of the function arbitrarily close to one isolated singularity, while the contour may be far away from it.

This is not magic and it is not an excuse to skip checking hypotheses. The residue theorem is the result of two precise facts. First, integrals of holomorphic functions can be deformed through regions where they remain holomorphic. Second, when we integrate a Laurent series around a small circle, every term cancels except one. We will see both facts directly, work through the calculation of several residues, and then use the result to evaluate real integrals whose antiderivatives are inconvenient or unavailable in elementary functions.

## Why one negative power survives a full turn

Start with a single singularity at a, surrounded by a punctured disk of holomorphicity. There the function has a Laurent series. Imagine integrating each term of that series around a small circle centered at a, counterclockwise. A term in a positive power has a primitive, so its closed integral vanishes. The constant term does too. For negative powers smaller than negative one, there is again an elementary primitive away from a, so the integral vanishes.

But the negative first power is different. One divided by z minus a has no single-valued holomorphic primitive on a full punctured disk. Parametrize the circle. As its position goes once around, the velocity contributes a factor of i times z minus a. That factor cancels the denominator. We integrate the constant i over one full turn and obtain two pi i.

Thus the integral of the whole Laurent series around the circle is two pi i multiplied by the coefficient of one divided by z minus a. That coefficient is the residue of the function at a. We are not approximating by keeping just the most singular term. In fact, the most singular term may not contribute at all. We are extracting exactly the one Laurent coefficient to which a full-turn contour integral responds.

Consider the function one divided by z cubed, plus seven divided by z, plus z squared, centered at zero. The cubic reciprocal dominates in magnitude near zero. If we focused only on the largest growth, we might expect it to control the integral. It does not. The residue is seven, so the contour integral around a small counterclockwise circle is fourteen pi i. The more severe reciprocal-cubed term contributes zero.

This example separates two ideas: pole order measures how the function grows near the point; residue measures the circulation detected by the contour integral. A pole of order three may have zero residue, and an essential singularity may have a perfectly simple nonzero residue.

## From one little circle to a large contour

Now take a positively oriented simple closed contour, perhaps an irregular boundary around several isolated singularities. Assume the function is holomorphic on an open neighborhood of the contour and on the enclosed region except for finitely many isolated singularities. That 'open neighborhood' condition matters: if the function fails on the contour itself, the integral may not even be defined in the ordinary sense.

Draw a small disjoint circle around each singularity, lying entirely inside the large contour. Remove the interiors of those little disks. The remaining region has no singularities. Cauchy's theorem for a region with holes says that the integral around its entire oriented boundary is zero. The outer boundary is traversed counterclockwise; each little boundary is traversed clockwise. If we instead orient every little circle counterclockwise, the outer integral equals the sum of the little-circle integrals.

Each small-circle integral is two pi i times the corresponding residue. Add them. That is the residue theorem: the outer integral equals two pi i times the sum of residues at the singularities inside.

Notice how little of the singularity's behavior survives into the final answer. We do not need to know its complete Laurent series. We do not need to evaluate the original integral directly. We need the residues, the location of each relevant singularity, and an honest account of which points the contour encloses.

If the contour is traversed clockwise, the sign reverses. If the path winds around a point multiple times, its contribution is weighted by the winding number. For our first calculations, simple counterclockwise contours will keep the geometry unambiguous.

## Computing residues without constructing the entire Laurent series

For a simple pole at a, a convenient formula is the limit of z minus a times the function as z approaches a. Why? Near a, the Laurent expansion starts with the residue divided by z minus a, plus a holomorphic remainder. Multiplying by z minus a removes the singular denominator and reveals the residue as a finite limit.

Consider one divided by z squared plus one. The denominator factors into z minus i times z plus i. Both zeros are simple, so the function has simple poles at i and negative i. At i, multiply by z minus i and take the limit. The result is one divided by two i. At negative i the residue is negative one divided by two i. The values are opposites, which already tells us that a contour containing both poles has zero integral.

A useful general formula applies to a quotient h divided by g when h and g are holomorphic near a, g vanishes at a, and g prime at a is nonzero. The residue is h at a divided by g prime at a. It follows because g has a simple zero and looks to first order like g prime at a times z minus a. However, if the numerator also vanishes, the singularity might be removable. The formula is still valid for the coefficient computed after cancellation, but we must not automatically call it a simple pole without checking that h at a is nonzero.

For higher-order poles, multiplying by a single factor is not enough. Suppose f equals a holomorphic h divided by the m-th power of z minus a. Then the residue is the coefficient of the power m minus one in h's Taylor expansion. Equivalently, it is the m-minus-one-st derivative of h at a divided by m-minus-one factorial. The formula takes a small amount of differentiation rather than requiring every Laurent coefficient.

As a particular example, take exponential of z divided by z cubed. The exponential series begins with one, then z, then z squared over two. After division by z cubed, the coefficient of one divided by z is one half. Therefore a positively oriented circle around zero has integral pi i. The pole is order three, but the residue comes from the second derivative of the numerator.

An essential singularity can be handled just as exactly. Exponential of one divided by z has infinitely many negative powers, but the coefficient of one divided by z is one. Its residue at zero is one. The contour integral around a circle centered at zero is therefore two pi i. The rest of the infinite principal part cancels over the full loop. This is one reason the residue theorem is much more general than a technique for rational functions.

## A real integral hidden inside a complex contour

Let us calculate the area under one divided by one plus x squared along the entire real line. A familiar substitution from elementary calculus gives pi, but we will approach it through complex analysis because the method generalizes to integrands where no convenient elementary antiderivative is available.

Use the complex function one divided by one plus z squared. Close a large real interval from negative R to positive R with the upper semicircle of radius R, traversed counterclockwise. The boundary has two pieces: the straight real segment and the curved arc.

The straight segment contributes precisely the ordinary real integral from negative R to R, since z equals a real parameter and the contour velocity is one. The upper semicircle encloses the pole at i, once R exceeds one. It does not enclose the pole at negative i. The residue inside is one divided by two i. The residue theorem says that the entire contour integral equals pi, because two pi i times one divided by two i is pi.

But that includes the contribution of the arc. To extract the desired real integral, we must prove that the arc contribution vanishes as R grows. It does not vanish just because the arc gets 'far away.' Its length is growing proportionally to R, so distance alone is not enough. We need the competition between the length and the decay of the function.

On the semicircle, the modulus of z is R. The denominator one plus z squared has modulus at least R squared minus one by the reverse triangle inequality. Thus the modulus of the integrand is at most one divided by R squared minus one. The arc has length pi R. Multiply those bounds. The arc integral has modulus at most pi R divided by R squared minus one, which tends to zero.

Therefore the real integral tends to pi. Every step is visible: identify the upper-half-plane pole, compute its residue, bound the closing arc, and pass to the limit. If we omitted the arc estimate, the answer would not be justified.

There is also a useful self-check. The integrand is positive on the real axis. Our contour orientation and residue multiplication produced the positive real number pi. A sign error from traversing the semicircle clockwise would have produced a negative answer, contradicting positivity.

## A second real integral where residues earn their keep

Now consider the integral along the whole real line of x squared divided by one plus x to the fourth power. This time the integral does not reduce as directly to the arctangent example. We can still use exactly the same contour idea because the integrand decays like one divided by x squared at large magnitude.

The complex denominator z to the fourth power plus one has four roots on the unit circle, each located halfway between neighboring fourth roots of unity. Two lie in the upper half-plane: the one at angle pi over four and the one at angle three pi over four. The other two lie in the lower half-plane, outside our semicircular contour.

At each root a, the denominator has a simple zero: its derivative is four times a cubed, which is nonzero because a lies on the unit circle. The quotient formula therefore gives a residue of a squared divided by four a cubed, or one divided by four a.

Add the two upper-half-plane residues. The real parts cancel, while the imaginary parts add to negative one divided by two times the square root of two, multiplied by i. That purely imaginary sum is exactly what we want, because multiplying by two pi i produces a positive real value: pi divided by the square root of two.

We must bound the arc again. On a semicircle of radius R greater than one, the numerator has modulus R squared, while the denominator has modulus at least R to the fourth minus one. The function's magnitude is at most R squared divided by R to the fourth minus one. The arc has length pi R. Their product tends to zero like one divided by R.

Consequently the integral of x squared divided by one plus x to the fourth over the whole real line equals pi divided by the square root of two. The integrand is even, so the corresponding integral from zero to infinity is half that value.

The calculation shows why complex residues can simplify a real problem. Instead of seeking an antiderivative of a rational function and negotiating a partial-fraction decomposition over the reals, we identify the complex roots, evaluate two local expressions, and justify one arc estimate.

## When the obvious contour is the wrong contour

There are important restrictions. If a pole lies directly on the real line, then closing the real axis with a semicircle can place a singularity on the contour itself. The ordinary residue theorem does not apply to that contour. Some problems call for a principal value, a small indentation around the pole, or a different contour. Those are distinct mathematical choices and require their own estimates and orientation conventions.

If the integrand decays only like one divided by z, the length of a semicircle may cancel that decay and leave a nonvanishing arc contribution. Additional oscillation can sometimes help, but it must be shown. Similarly, branch points of logarithms and fractional powers may require branch cuts and keyhole contours, because there is no globally single-valued integrand on the whole region we initially imagined.

Nor should we assume that only poles contribute. The residue theorem covers isolated essential singularities as well, so long as the function is holomorphic in the punctured region and the contour's hypotheses hold. The residue coefficient is what we compute; visualizing the singularity is optional.

One final observation points to another powerful use. A residue is a local coefficient detected by the integral of f. What if we integrate the ratio of a function's derivative to the function itself? Near a zero, that ratio behaves like the multiplicity divided by z minus a. Near a pole, the ratio behaves like minus the pole order divided by z minus a. The residue theorem should then count zeros minus poles inside a contour, using only values along its boundary.

That leads to the argument principle. The local theory of zeros and poles, the global geometry of winding, and the residue theorem fit together to count solutions of equations without ever solving them explicitly.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Residue theorem and orientation

Let \(\Gamma\) be a positively oriented piecewise \(C^1\) Jordan curve bounding a region \(U\). Suppose f is holomorphic on a neighborhood of \(\overline U\) except at finitely many isolated points \(a_1,\ldots,a_N\in U\). Then

\[
\oint_\Gamma f(z)\,dz=2\pi i\sum_{j=1}^N\operatorname{Res}(f,a_j),
\quad \operatorname{Res}(f,a)=c_{-1}
=\frac{1}{2\pi i}\oint_{|z-a|=\rho} f(z)\,dz.
\]

For a general closed contour avoiding singularities in a suitable domain, the generalization is \(2\pi i\sum_a n(\Gamma,a)\operatorname{Res}(f,a)\), with winding numbers \(n(\Gamma,a)\). This includes a domain/homology hypothesis; the Jordan-curve version above suffices for the examples.

**Proof:** Remove pairwise disjoint small disks about all singularities. Cauchy's theorem on the resulting region gives \(\oint_\Gamma f-\sum_j\oint_{C_j}f=0\). On each \(C_j\) the Laurent series converges uniformly; termwise integration kills every power except exponent -1.

### Computing residues

For a simple pole of \(f=h/g\) at \(a\), with \(g(a)=0\), \(g'(a)\ne0\), and \(h(a)\ne0\),
\[\operatorname{Res}(h/g,a)=h(a)/g'(a).\]
For \(f(z)=h(z)/(z-a)^m\), where h is holomorphic near a,
\[\operatorname{Res}(f,a)=h^{(m-1)}(a)/(m-1)!.\]
More generally, if the pole order is m, use \(h(z)=(z-a)^m f(z)\), which extends holomorphically.

### Real integral 1

Use \(f(z)=1/(z^2+1)\). For \(R>1\), the positively oriented upper semicircle encloses \(i\) but not \(-i\). Then
\[
\operatorname{Res}(f,i)=\frac1{2i},\quad
\left|\int_{\text{arc}_R}f(z)\,dz\right|\le\frac{\pi R}{R^2-1}\to0,
\quad \int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\pi.
\]

### Real integral 2

For \(f(z)=z^2/(z^4+1)\), the upper-half-plane poles are \(a=e^{i\pi/4}\) and \(b=e^{3i\pi/4}\). Their residues are \(1/(4a)\) and \(1/(4b)\), summing to \(-i/(2\sqrt2)\). Hence
\[
\int_{-\infty}^{\infty}\frac{x^2\,dx}{1+x^4}
=2\pi i\left(-\frac{i}{2\sqrt2}\right)=\frac{\pi}{\sqrt2},
\qquad
\int_0^{\infty}\frac{x^2\,dx}{1+x^4}=\frac{\pi}{2\sqrt2}.
\]
The semicircle bound is \(\pi R^3/(R^4-1)\to0\).

### Exercises with answers

1. Compute \(\oint_{|z|=1}(z^{-3}+7z^{-1}+z^2)dz\). **Answer:** \(14\pi i\).
2. Compute \(\operatorname{Res}(e^z/z^3,0)\). **Answer:** 1/2.
3. Compute \(\operatorname{Res}(e^{1/z},0)\). **Answer:** 1.
4. Compute \(\oint_{|z|=3}dz/(z^2+1)\) counterclockwise. **Answer:** 0, since the residues at i and -i cancel.
5. Why not use the same contour unmodified for \(\int_{-\infty}^\infty dx/x\)? **Answer:** The integrand is singular at zero, directly on the real segment; the ordinary integral diverges and the residue theorem cannot be applied to a contour passing through the pole. A Cauchy principal value is a separate construction.
6. If a meromorphic function has a pole of order two at a, must its residue be nonzero? **Answer:** No; \(1/(z-a)^2\) has zero residue.

### Sources and further reading

- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, Topics 8 and 9: https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, Lecture 14 and Lecture 15: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- *A First Course in Complex Analysis*, Residue Theorem: https://complexanalysis.org/web/sec_residue-thm.html.
- Wikipedia, *Residue theorem*: https://en.wikipedia.org/wiki/Residue_theorem.
- [Tero Kilpeläinen and Antti Vähäkangas, Complex Analysis 2 (2024)](https://users.jyu.fi/~salomi/teaching/ca2_2024/Lecture_notes_eng.pdf) — Kilpeläinen & Vähäkangas, Complex Analysis 2, chapter 3: residue theorem and applications.
