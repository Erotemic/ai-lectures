# Boundary Harnack: Comparing Two Functions That Both Vanish at a Wall

**Track:** Multivariable Calculus from First Principles. **Focus:** boundary Harnack comparison, positive harmonic functions, flat and corner models, and the relationship with harmonic measure.

<!-- BEGIN SPOKEN LECTURE -->

# Boundary Harnack: Comparing Two Functions That Both Vanish at a Wall

Imagine two positive temperatures inside a room, each maintained at zero along the same cold wall. As you walk toward the wall, both temperatures approach zero. Which one approaches zero faster? Does their ratio remain meaningful, or does dividing one tiny number by another make the question hopeless?

Interior Harnack inequalities compare values of a positive harmonic function at points separated from the boundary. Hopf's lemma, under smoothness and an interior-ball condition, says that a nontrivial positive harmonic function cannot meet a zero boundary value with a flat normal derivative. But neither statement by itself controls the ratio of two such functions as both tend to zero.

The boundary Harnack principle does precisely that. In geometrically controlled domains, two positive harmonic functions that vanish on the same boundary portion are comparable, even arbitrarily close to that portion. Their *relative* decay can be much better behaved than either function's individual derivatives. That distinction opens the way to understanding boundaries that are not smooth enough for ordinary Taylor expansions.

## Start with the upper half-ball

Work in ordinary Euclidean space, with a last coordinate we call height. Consider the part of the unit ball above the plane of height zero. Let u and v be positive harmonic functions in that half-ball. Assume both extend continuously to zero on its flat boundary face. We do not insist they vanish on the curved spherical part; whatever is prescribed there is what drives the two solutions.

Choose a reference point safely inside, at height one half on the vertical axis. Because u and v are positive there, we can divide by their values at that point. The boundary Harnack statement says that, within a smaller half-ball near the center of the flat face, the normalized ratio of u to v is bounded above and below by constants that depend on the dimension and the geometry, not on the particular functions.

Equivalently, if u and v happen to have the same value at the reference point, neither can overwhelm the other by an arbitrarily large factor when we approach the middle of the common zero boundary. More generally, one ratio measured at an interior reference point controls ratios at all points of a smaller boundary neighborhood.

The principle has a stronger form: on a Lipschitz boundary patch, the ratio has a Hölder-continuous extension toward the patch under the customary local hypotheses. Hölder continuity means that nearby values differ by at most a constant times a positive power of their separation. The exponent and constant are determined by the boundary geometry and the normalization. We must not mistake this for a claim that either individual harmonic function has a smooth normal derivative at every boundary point.

Notice the hypotheses. Both functions must be positive and harmonic in the same local domain, and must vanish continuously on the same part of its boundary. If one has a nonzero boundary source, or if the boundary geometry is arbitrary, this particular comparison theorem cannot simply be invoked unchanged.

## A calculation where the ratio stays visible

Take the two-dimensional upper half-disk. Let the first function equal the height y. Let the second equal y times the quantity one plus x divided by four. Both are harmonic. For the first, all second derivatives vanish. For the second, the only extra term is x times y, whose Laplacian also vanishes. In the unit half-disk, one plus x divided by four stays strictly positive, so both functions are positive in the interior. They vanish on the horizontal diameter.

Their ratio is one divided by one plus x divided by four. The height y has disappeared completely. We may let y approach zero without creating a singular ratio. At the center of the boundary the ratio tends to one. A little to the right it is slightly less than one; a little to the left it is slightly greater.

This is just a polynomial example, not a proof of boundary Harnack in general. Its value is that we can see the conclusion in the simplest possible way. Two separately vanishing functions carry a stable quotient because their boundary decay has a shared geometric factor: distance from the wall.

In this flat, smooth example, the inward normal derivative of the first function is one. For the second it is one plus x divided by four. Their quotient at the boundary equals the limiting ratio of the functions. That is exactly what an ordinary first-order Taylor expansion would predict.

But a boundary Harnack theorem continues to have content when this derivative argument is unavailable.

## Why an interior estimate is not enough

Suppose we attempt to use the ordinary interior Harnack inequality on u and v separately. For every ball wholly inside the domain, that inequality bounds the ratio of a positive harmonic function's maximum and minimum on a smaller concentric ball. Yet as our test point approaches the wall, the largest ball centered there shrinks. A chain of overlapping balls reaching a fixed reference point may require more and more links, and the resulting comparison constant can deteriorate without bound.

We cannot infer uniform boundary control just by repeating an interior estimate and ignoring that deterioration. Boundary Harnack needs the zero boundary condition. That shared condition is not a distraction; it is the crucial extra information.

One way to visualize the proof in a flat model is through positive harmonic representation. Values near the middle of the zero wall come from nonzero data on portions of the boundary farther away. Their influence kernels vanish at the flat wall with comparable rates. Integrating those kernels against different nonnegative boundary data keeps the resulting functions comparable after normalization. Making this argument uniform for curved or merely Lipschitz walls takes substantial work: one combines boundary barriers, interior Harnack chains, and the geometry of paths that remain a controlled distance from the boundary.

A common geometric class is a Lipschitz domain, locally lying above the graph of a function with bounded slope. A broader useful class is a non-tangentially accessible domain, where interior and exterior accessibility and quantitative connecting paths are controlled. The precise theorems have slightly different hypotheses. The shared lesson is that boundary comparison is a theorem about the *equation together with the domain*.

## A corner makes the difference between value and derivative

Now replace the flat wall by the two rays bounding a planar wedge. Use polar coordinates, with radius r and angle theta measured from one ray. Let the opening angle be omega. A classical positive harmonic function in the wedge is radius to the power pi divided by omega, multiplied by the sine of pi theta divided by omega.

Why this particular exponent? Separation of variables for the planar Laplacian gives angular sine and cosine factors. Requiring zero values on the rays at angles zero and omega selects sine, and forces the frequency to be pi divided by omega. The radial power must have the same exponent to make the Laplacian vanish.

For a half-plane, omega is pi, and the exponent is one. The function is just height, in rotated coordinates. For a reentrant wedge of opening three pi over two, the exponent is two thirds. Now the function decays like radius to the two-thirds power. Its gradient grows like radius to the negative one-third power as we approach the vertex.

The gradient is no longer bounded near that corner. We certainly cannot justify a finite nonzero normal derivative at the vertex by the flat-wall Taylor argument. Nevertheless, when two positive harmonic functions vanish on the same local wedge boundary, boundary Harnack can still compare their ratios. The wedge is Lipschitz, despite the corner. The two functions share the dominant boundary geometry even when individual derivatives become singular.

This is the main conceptual upgrade: *relative boundary behavior* can remain stable where absolute derivative estimates fail.

## What the theorem does, and does not, promise

Boundary Harnack does not say every harmonic function vanishes at the same rate everywhere. At different corners the geometry changes. Nor does it say that all ratios are literally constant. The polynomial example had a varying ratio, and a genuine boundary Harnack theorem permits that variation while controlling its size and continuity.

It is also not a comparison theorem for arbitrary signed solutions. Positivity matters because maximum principles and Harnack inequalities are fundamentally order-based. Nor can we simply replace harmonicity by an inhomogeneous Poisson equation with unrestricted forcing. A source can change the leading order of vanishing. There are modified boundary Harnack theorems that account for right-hand sides, but they need additional assumptions.

In smoother domains, the boundary ratio may equal a quotient of nonzero normal derivatives, precisely as in our polynomial example. At a corner, it is better to think of the ratio as an independent object that may extend to the boundary even when neither normal derivative has a classical limit.

## From comparing solutions to comparing boundary influence

Consider the Dirichlet Green function of a bounded domain. Fix two source points in its interior, away from the boundary patch we are studying. As a function of the observation point near that patch, each Green function is positive, harmonic, and zero on the same boundary region. Boundary Harnack therefore compares the two Green functions there.

This has consequences for potential theory. Ratios of Green functions help measure how the same boundary region is seen from different source points. In suitable domains, they are one path toward understanding harmonic measure and, more deeply, minimal positive harmonic functions associated with boundary points. The claim is about ratios under controlled hypotheses, not about surface area automatically being interchangeable with harmonic measure.

We began by asking how two temperatures approach the same cold wall. We can now answer at two levels. If the wall is smooth enough, the first normal derivative often describes each temperature's leading decay. If the wall has a corner, those separate derivatives may fail, but the quotient of two positive harmonic functions can still be controlled. Boundary Harnack preserves the comparison even when a naive derivative-based explanation breaks down.

That is why the principle belongs alongside Hopf's lemma and harmonic measure, and why it prepares us to ask a harder question: which sets and boundary features are actually large enough to affect a harmonic function?

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Local boundary Harnack statement

For a local Lipschitz graph domain \(D\) with \(0\in\partial D\), and \(u,v>0\) harmonic in \(D\cap B_1\), continuously zero on \(\partial D\cap B_1\), choose a corkscrew reference point \(A\in D\cap B_{1/2}\). On a sufficiently smaller neighborhood, a boundary Harnack estimate has the schematic form
\[
 C^{-1}\frac{u(A)}{v(A)}\le \frac{u(x)}{v(x)}\le C\frac{u(A)}{v(A)},
 \quad x\in D\cap B_c,
\]
and the quotient extends Hölder-continuously to the local boundary, with constants depending on geometry and normalization. Precise choices of \(c,C\), and the Hölder exponent vary by theorem. This is **not** asserted for arbitrary domains or for arbitrary inhomogeneous equations.

### Direct planar example

In \(D=B_1\cap\{y>0\}\), let
\[
 u(x,y)=y,\qquad v(x,y)=y\left(1+\frac x4\right).
\]
Then \(\Delta u=\Delta v=0\); \(u,v>0\) in \(D\); \(u=v=0\) on \(y=0\); and
\[
\frac uv=\frac1{1+x/4},\quad
\lim_{y\downarrow0}\frac uv=\frac1{1+x/4}
=\frac{\partial_yu(x,0)}{\partial_yv(x,0)}.
\]
For \(x=\pm1/4\) the ratios are \(16/17\) and \(16/15\), respectively.

### Wedge Laplacian check

For \(W_\omega=\{(r,\theta):r>0,\ 0<\theta<\omega\}\), put \(\lambda=\pi/\omega\) and
\[
 U(r,\theta)=r^\lambda\sin(\lambda\theta).
\]
Using \(\Delta=\partial_{rr}+r^{-1}\partial_r+r^{-2}\partial_{\theta\theta}\),
\[
\Delta U=
\bigl[\lambda(\lambda-1)+\lambda-\lambda^2\bigr]
 r^{\lambda-2}\sin(\lambda\theta)=0.
\]
On \(\omega=3\pi/2\), \(\lambda=2/3\); along any fixed interior angle, \(U\asymp r^{2/3}\) and \(|\nabla U|\asymp r^{-1/3}\). A classical finite derivative at the wedge vertex is not available, although local boundary Harnack remains relevant to ratios of positive harmonic functions.

### Exercises and answers

1. **Polynomial harmonicity.** Compute \(\Delta[xy]\). **Answer:** zero, since both pure second derivatives vanish.
2. **Boundary quotient.** For \(u=y\) and \(v=y(1+x/4)\), find the limit of \(u/v\) as \(y\downarrow0\) at \(x=1/4\). **Answer:** \(16/17\).
3. **Corner exponent.** Determine the exponent for a wedge of opening \(\pi/2\). **Answer:** \(\lambda=2\); the leading positive harmonic model is \(r^2\sin 2\theta\).
4. **Reentrant corner.** For \(\omega=3\pi/2\), does the gradient of the wedge model remain bounded at the tip? **Answer:** no; its order is \(r^{-1/3}\).
5. **Missing hypothesis.** Can boundary Harnack in its classical form be applied to a solution of \(-\Delta u=1\) and a positive harmonic function, just because both have zero trace? **Answer:** no; unrestricted forcing changes the equation and may alter boundary decay.

### Sources and further reading

- [Xavier Fernández-Real and Xavier Ros-Oton, *Regularity Theory for Elliptic PDE*, Appendix B](https://sma.epfl.ch/~xafernan/Documents/Fernandez-Real_Ros-Oton_Book.pdf), a proof of boundary Harnack in Lipschitz graph domains.
- [A new boundary Harnack principle (equations with right hand side)](https://link.springer.com/article/10.1007/s00205-019-01415-3), the classical statement and why forcing requires new hypotheses.
- [Wikipedia: Harnack's inequality](https://en.wikipedia.org/wiki/Harnack%27s_inequality), the interior comparison principle, which is not itself a boundary estimate.
- [Wikipedia: Harmonic measure](https://en.wikipedia.org/wiki/Harmonic_measure), the connection to boundary data and Green functions.
- Library connections: `multivariable-calculus:051000` (Hopf), `052000` (harmonic measure), `046000` (wedge corner singularity).
