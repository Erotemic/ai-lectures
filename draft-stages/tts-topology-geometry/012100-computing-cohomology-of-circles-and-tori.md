# 012100 - Computing Cohomology of Circles and Tori

**Track:** Topology and Geometry. **Background:** closed and exact forms, integration over cycles, Stokes' theorem. **Question:** can we compute de Rham cohomology rather than merely define it?

<!-- BEGIN SPOKEN LECTURE -->

# Computing Cohomology of Circles and Tori

De Rham cohomology is defined as closed differential forms modulo exact ones. That definition sounds compact, but what does an actual computation look like? We will compute the cohomology of a circle and a two-dimensional torus. Both calculations have geometric meaning: they show precisely how integrals around fundamental cycles classify the obstruction to a global potential.

We begin with the circle because the entire calculation can be understood as a careful version of the fundamental theorem of calculus with periodic boundary conditions.

## A closed one-form on a circle

Imagine a point traveling around a circle, tracked by an angle theta. Theta increases continuously while we travel, but after one revolution we have returned to the same point even though theta has increased by two pi. The angle is not a globally defined real-valued function on the circle. Nevertheless the local differentials d theta agree where angle charts overlap, because two branches of angle differ by constant multiples of two pi. They define a global one-form.

Every one-form on a circle is closed: its exterior derivative would be a two-form, and there are no nonzero two-forms on a one-dimensional manifold. The question is which one-forms are exact. An exact form is d f for a smooth real function f defined all the way around the circle. Its integral over one full revolution must be zero, since the endpoint is the starting point.

Conversely, suppose a smooth one-form has zero integral over a full revolution. Lift it to the real line, where the angle becomes a genuine coordinate. On the real line we can integrate its coefficient to construct a potential. Because the integral over a period is zero, the potential takes the same value when theta is increased by two pi. It is periodic and therefore descends to a well-defined function on the circle. The original form is its differential.

This proves something precise. Two one-forms on the circle represent the same cohomology class exactly when they have the same integral around a positively oriented revolution. Every real number occurs as such an integral by taking a constant multiple of the angular one-form. The first de Rham cohomology of the circle is a one-dimensional real vector space.

The zeroth cohomology is also one-dimensional: a function whose differential is zero is constant on a connected circle, and no negative-degree differential makes a constant into a boundary. Cohomology in degrees two and higher vanishes because the circle has no nonzero forms in those degrees.

## From one loop to two independent loops

A two-dimensional torus can be thought of as a square with opposite edges identified. It has two basic types of loops: one circles around the first periodic coordinate, and the other around the second. Call the angular coordinates theta and phi. Both d theta and d phi are global closed one-forms.

Integrate d theta along the first basic loop. The result is two pi. Integrate it along the second basic loop. The result is zero. For d phi the roles are reversed. These two forms detect independent directions of winding.

Suppose omega is any closed one-form on the torus. Let its integral around the first basic loop be two pi times a, and its integral around the second be two pi times b. The coefficients a and b do not depend on which parallel representative of the basic loops we choose, because sliding the loop across a cylinder changes the integral by that of d omega over the intervening strip, and d omega is zero.

Subtract a times d theta plus b times d phi from omega. The remaining closed form integrates to zero around both generators of the torus's first homology. Consequently it has zero integral around every closed loop. A path integral from a fixed base point then defines a smooth global potential. The remaining form is exact.

We have classified every first cohomology class by the two real numbers a and b. The first de Rham cohomology of the two-torus has dimension two. It is not merely that the torus appears to have two holes in a picture. The classification is an explicit test using two integrals and the existence of a potential when both periods vanish.

## The top-degree class

A two-form on a two-dimensional torus is automatically closed, because its exterior derivative would have degree three. Every two-form can be written as a smooth periodic coefficient times d theta wedge d phi. Its integral over the torus is one real number.

If a two-form is exact, that integral vanishes by Stokes' theorem because the torus has no boundary. Conversely, a smooth two-form whose total integral is zero is exact. One way to see this is to average its coefficient in one angular direction, subtract off that average using an explicit antiderivative in the other direction, and then use the zero-total-integral condition to integrate the remaining one-dimensional function periodically. The resulting one-form has the original two-form as its derivative.

Thus the second de Rham cohomology of the torus is another copy of the real numbers. A normalized area form represents its generator, just as a normalized angular one-form represents the circle's first cohomology generator.

## Wedge products and the cohomology ring

There is more structure than a list of vector-space dimensions. Differential forms can be multiplied using the wedge product, and this multiplication descends to cohomology. For the torus, the product of the class of d theta with the class of d phi is the nonzero second-degree class represented by d theta wedge d phi. Swapping the factors reverses the sign. Wedge-multiplying either one-form by itself gives zero.

In other words, the cohomology ring of the two-torus is the exterior algebra on two degree-one generators. The word ring means we can add classes and multiply them, with the appropriate graded sign. This structure expresses how the two winding directions combine to give an oriented area class.

## A higher-dimensional pattern

An n-dimensional torus is the product of n circles. It has n angular one-forms, one for each circular direction. Their wedge products, taken over distinct directions, represent all cohomology classes. There is one degree-zero generator, n degree-one generators, a generator for each pair of directions in degree two, and so on. The number of independent degree-k classes is the number of ways to choose k directions out of n.

The full proof can be given by the de Rham Kunneth theorem or constructed directly from periodic forms. It is important not to present the pattern as a consequence of visual hole-counting alone. What makes it rigorous is the ability to reduce arbitrary closed forms to these constant-coefficient representatives, and the use of period integrals to prove their independence.

These computations explain what cohomology does. On a circle, one period detects every first cohomology class. On a two-torus, two loop periods detect first cohomology, and the total surface integral detects second cohomology. The objects are analytic differential forms, the tests are integrals, and the answers depend on the topology of the underlying space rather than on its choice of coordinates or metric.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(S^1=\mathbb R/(2\pi\mathbb Z)\),
\[H^0_{\mathrm{dR}}(S^1)=\mathbb R,\quad H^1_{\mathrm{dR}}(S^1)=\mathbb R[d\theta],\quad H^{k>1}_{\mathrm{dR}}(S^1)=0.\]
An arbitrary \(f(\theta)d\theta\) is exact iff \(\int_0^{2\pi}f(\theta)\,d\theta=0\), since a primitive on \(\mathbb R\) descends iff its period vanishes.

On \(T^2=(\mathbb R/2\pi\mathbb Z)^2\),
\[
H^0=\mathbb R,\quad H^1=\mathbb R[d\theta]\oplus\mathbb R[d\phi],\quad H^2=\mathbb R[d\theta\wedge d\phi].
\]
For a closed \(\omega=P\,d\theta+Q\,d\phi\), set
\[a={1\over2\pi}\int_0^{2\pi}P(\theta,\phi_0)\,d\theta,\qquad b={1\over2\pi}\int_0^{2\pi}Q(\theta_0,\phi)\,d\phi.\]
Closedness \(\partial_\theta Q=\partial_\phi P\) makes these independent of \(\phi_0,\theta_0\). Then \(\omega-a\,d\theta-b\,d\phi\) has zero periods and is exact.

**Explicit two-form primitive when the average vanishes.** Let \(h(\theta,\phi)\) be smooth periodic with \(\int_{T^2}h\,d\theta d\phi=0\). Set
\[f(\theta)={1\over 2\pi}\int_0^{2\pi}h(\theta,s)\,ds,\quad b(\theta)=\int_0^\theta f(t)\,dt,\quad k(\theta,\phi)=\int_0^\phi(h(\theta,s)-f(\theta))\,ds.\]
Both \(b\) and \(k\) are periodic in their respective angular variables. The one-form \(\beta=b(\theta)d\phi-k(\theta,\phi)d\theta\) satisfies \(d\beta=h\,d\theta\wedge d\phi\).

For \(T^n\), \(H^*_{\mathrm{dR}}(T^n)\cong\Lambda^*(\mathbb R^n)^*\) and \(\dim H^k=\binom nk\).

### Check your understanding

1. Does the form \(d\theta\) on \(S^1\) have a global real-valued primitive? **No:** its period is \(2\pi\).
2. What is \([d\phi]\wedge[d\theta]\) on the torus? **Answer:** \(-[d\theta\wedge d\phi]\).
3. How many independent degree-two classes does the three-torus have? **Answer:** three, corresponding to the three choices of pairs of coordinates.

### Reading and sources

- Dietmar Salamon, [Differential Topology, de Rham cohomology and torus example](https://people.math.ethz.ch/~salamon/PREPRINTS/difftop.pdf).
- Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), the topology of products and cohomology.
- Overview: [De Rham cohomology](https://en.wikipedia.org/wiki/De_Rham_cohomology), [Cohomology ring](https://en.wikipedia.org/wiki/Cohomology_ring).
