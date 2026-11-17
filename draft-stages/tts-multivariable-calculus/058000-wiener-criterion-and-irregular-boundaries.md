# The Wiener Criterion: When a Boundary Point Cannot Enforce Its Value

**Track:** Multivariable Calculus from First Principles. **Focus:** boundary regularity, barriers, Wiener capacity sums, punctured domains, and geometrically thin complements.

<!-- BEGIN SPOKEN LECTURE -->

# The Wiener Criterion: When a Boundary Point Cannot Enforce Its Value

A boundary condition seems to make a simple promise. Prescribe a temperature at each point of the wall, solve Laplace's equation inside, and the temperature should approach the prescribed value as we move toward that point from inside the room.

On a smooth room, the promise is reliable. But remove the center point of a ball, and declare that missing point to be part of the boundary. Can we now demand temperature one at that point while keeping the outer sphere at temperature zero? The boundary data are perfectly continuous as a function on this peculiar boundary: the isolated point is separated from the outer sphere. Yet no bounded harmonic function can satisfy them continuously.

This failure is not caused by a badly chosen numerical algorithm. It is a property of the domain. Some boundary points are too thinly supported by the complement to impose their own Dirichlet values. The Wiener criterion provides a precise answer, using capacity at every distance scale.

## First distinguish two meanings of regularity

In elliptic PDE we have called a solution regular when it possesses derivatives, perhaps measured in a Sobolev or Hölder norm. Wiener's *regular boundary point* means something different.

Fix a bounded domain D and a point x-zero on its boundary. We call that point regular for the Laplace Dirichlet problem if, for every continuous boundary function g, the harmonic solution obtained by the standard Perron or probabilistic construction tends to g at x-zero as we approach x-zero through D.

The phrase every continuous boundary function is important. A particular choice of data might accidentally be satisfied even at an irregular point. Regularity is a property of the geometry and the equation that guarantees the boundary limit for all continuous data.

It is equally important not to confuse pointwise boundary regularity with second-derivative estimates. A domain may have corners where the solution's Hessian is singular, yet every boundary point can still be Wiener regular. Conversely, our punctured ball has a perfectly smooth outer sphere but an additional irregular boundary point at its center.

## The punctured ball is the decisive example

Let D be the unit ball in three dimensions with its center removed. Its boundary consists of the usual outer sphere together with the isolated origin.

Assign boundary value zero on the outer sphere and value one at the origin. This is continuous on the boundary as a topological space because the origin is isolated from the outer sphere.

Suppose there existed a bounded harmonic solution that approached those values everywhere. By the removable singularity theorem, any bounded harmonic function in the punctured ball extends harmonically across the origin. The extension would be harmonic in the full ball and zero on its outer boundary. The maximum principle would force it to be identically zero. Hence its limit at the origin would be zero, not one.

So the origin is an irregular boundary point. Giving it a new Dirichlet value cannot override the interior harmonic equation.

The same conclusion has a probabilistic interpretation. Brownian motion started inside a three-dimensional ball does not hit one specified interior point before it exits. That point has harmonic measure zero. A boundary payoff assigned only at the origin therefore does not affect the harmonic solution in the punctured ball. The Perron solution for our boundary data is simply zero.

Recall the energy calculation for a shrinking inner ball. In three dimensions its capacity is proportional to its radius, which tends to zero. The isolated origin has zero capacity. This is already a strong clue about which boundary points can be ignored.

## Contrast a regular point on a round ball

Choose a point x-zero on the unit sphere of an ordinary unit ball. There is an elementary harmonic barrier for it: one minus the dot product of x with x-zero.

The function is harmonic because it is affine. Inside the unit ball it is positive. It approaches zero at x-zero, and no other point of the closed unit ball makes it vanish. This is exactly the kind of function needed to localize the effect of the boundary data.

Given continuous boundary data g, continuity makes g close to g at x-zero on a small boundary patch. On the rest of the boundary, the positive barrier has a definite lower bound. Multiply it by a large constant and add a small tolerance. The resulting upper and lower comparison functions trap the harmonic solution near x-zero. Let the tolerance shrink to zero, and the solution tends to the prescribed value.

That is the barrier method for proving regularity. The ball is not regular merely because its boundary looks nice. We can exhibit a function whose comparison properties enforce the boundary limit. Similar barriers work under an exterior sphere condition and, more generally, an exterior cone condition.

## What if the complement is thin but not absent?

The punctured ball may feel too simple: there is literally only a missing point. Now imagine a domain whose complement contains solid obstacles arbitrarily close to a boundary point, yet each obstacle becomes extremely small compared with its distance from that point.

Is the mere presence of these obstacles at every scale enough to make the point regular? No. Their capacity matters, and the sizes have to be accumulated across scales.

For a boundary point x-zero in three or higher dimensions, draw concentric shells centered at x-zero. Choose shell radii that halve at each step: one half, one quarter, one eighth, and so on. In each shell, collect the part of the complement of D that lies there. Call it E at that scale.

Measure the Newtonian capacity of that exterior set. In dimension n, divide by the radius raised to the power n minus two. This quotient is dimensionless, because the capacity of a ball of that radius scales like the same power. Then add those quotients over all sufficiently small shells.

Wiener's criterion says: the boundary point is regular if and only if this sum diverges.

This is a deep theorem. We will not pretend its proof is a one-line application of the maximum principle. But the terms are concrete, the scaling is derived from the ball capacity calculation, and the criterion explains both regular and irregular examples.

## Why the exterior cone condition works

Suppose the complement of D contains a fixed-aperture cone emanating from x-zero. At every sufficiently small scale, the part of that cone in the corresponding shell contains a ball whose radius is a fixed fraction of the shell radius.

Capacity is monotone: a set that contains a ball has capacity at least that ball's capacity. A ball of radius proportional to r has capacity proportional to r to the power n minus two. Thus the capacity of the exterior piece, divided by r to the power n minus two, is bounded below by a fixed positive constant.

The Wiener sum includes infinitely many terms that never become small. It diverges, and the boundary point is regular.

This is a satisfying consistency check. The criterion recovers the classical exterior cone result from one capacity estimate and a geometric picture. We do not need to know the exact shape of the complement; a scale-invariant chunk at every level is enough.

## Solid obstacles at every scale can still be too small

Here is a more surprising example, still in three dimensions. Place a sequence of tiny closed balls along the positive horizontal axis, with their centers tending to the origin. At the k-th scale, put the center at three quarters of two to the negative k. Give that little ball radius two to the negative k squared. Begin at a sufficiently large k so the balls are disjoint and each lies within its assigned dyadic shell.

Let K contain all those small balls together with the origin, and let D be the unit ball with K removed. The origin is a boundary point. Unlike the punctured-ball example, the complement contains genuinely three-dimensional obstacles arbitrarily close to the origin, one at every scale.

But the capacity of a three-dimensional ball is four pi times its radius. The k-th obstacle therefore has capacity four pi times two to the negative k squared. Divide by the shell radius two to the negative k. The normalized contribution is four pi times two to the power k minus k squared.

Those numbers become tiny extraordinarily quickly, and their sum is finite. Wiener's criterion declares the origin irregular. Solid exterior obstacles are present at every scale, yet they are too small in total capacitary thickness to enforce all continuous boundary data at that point.

This is the kind of case that mere volume, or a sketch of a perforated domain, does not settle. Capacity supplies the relevant scale and the criterion supplies the correct accumulation rule.

## Why a sum, rather than a single scale?

A boundary is not regular or irregular because of one isolated annulus. Harmonic influence is built up as the process approaches the point through a nested sequence of neighborhoods. A strong exterior obstruction at one scale may not determine what happens at infinitely many smaller scales.

The Wiener series accumulates the effective strength of the exterior complement. The divergence condition can be thought of as saying that the boundary keeps presenting enough obstruction, at sufficiently many scales, to force the limit to respect the prescribed value. A finite sum means the exterior becomes too weak in aggregate near the point.

The Brownian picture supports that intuition: an accessible exterior set gives a diffusion opportunities to exit, but the probabilities and dependencies across nested scales are subtle. The actual proof uses potential-theoretic estimates and barriers. We should not claim the summands themselves are independent hitting probabilities.

## The plane requires a different normalization

We have stated the simple dyadic formula for dimensions at least three. If we mechanically substitute dimension two, the power n minus two becomes zero, which hides the logarithmic behavior we computed for planar annuli.

The planar Wiener criterion has a logarithmic formulation. It uses the corresponding two-dimensional capacity and potential-theoretic normalization, not the three-dimensional Newtonian formula with the exponent set to zero. This is another reason to keep the definition of capacity explicit rather than treat it as an arbitrary numerical measure of a set's size.

The underlying question remains the same: how thick is the complement, in the potential-theoretic sense, near the boundary point? The detailed scale formula must respect the dimension.

## Boundary values, numerical methods, and honest hypotheses

What does this mean for PDE computations? Finite-element convergence in an energy norm does not automatically imply that the numerical solution approaches an arbitrarily assigned pointwise value at every boundary point. A boundary value attached to a zero-capacity set may not define a meaningful energy-space constraint at all.

On ordinary Lipschitz domains, exterior cone-type geometry gives us regular boundary points, and familiar boundary formulations work as expected. On highly perforated or irregular domains, it matters which trace is prescribed, in what function space, and whether the underlying continuous Dirichlet problem actually honors that trace pointwise.

Wiener's theorem gives a clean end to our sequence. Boundary Harnack compares two positive harmonic solutions as they approach a shared wall. Capacity measures how strongly a set can influence an energy field. Removability tells us when an interior hole carries no bounded harmonic information. The Wiener criterion uses that same capacity, measured across scales, to decide whether a boundary point can enforce the value assigned to it.

A set can be visible geometrically and negligible analytically. The difference is not a paradox. It is precisely the distinction potential theory was built to measure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Dirichlet regularity and the Wiener test in dimensions \(n\ge3\)

For \(x_0\in\partial D\), regularity means that the Perron solution \(H_g\) of the Laplace Dirichlet problem satisfies
\[
 \lim_{D\ni x\to x_0}H_g(x)=g(x_0)
\]
for every \(g\in C(\partial D)\) (with the standard assumptions for the Perron solution). Let \(r_k=2^{-k}\), and define exterior shell pieces
\[
 E_k=(\mathbb R^n\setminus D)\cap
 \{x:r_{k+1}\le |x-x_0|\le r_k\}.
\]
A dyadic form of the classical Wiener criterion, for \(n\ge3\), says
\[
 x_0\text{ is regular}\iff
 \sum_{k\ge k_0}\frac{\operatorname{Cap}(E_k)}{r_k^{n-2}}=+\infty,
\]
where \(\operatorname{Cap}\) is the absolute Newtonian capacity, with a fixed normalization such as the Dirichlet energy normalization used here. Replacing dyadic shells by comparable geometric shells does not change divergence.

### Smooth-ball barrier

For \(D=B_1(0)\), \(x_0\in\partial B_1\), define
\[
 b(x)=1-x\cdot x_0.
\]
Then \(\Delta b=0\), \(b>0\) in \(B_1\), \(b(x_0)=0\), and \(b>0\) on \(\overline B_1\setminus\{x_0\}\). Positivity on the compact complement of any neighborhood of \(x_0\) lets multiples of \(b\) dominate bounded boundary-data errors away from \(x_0\); comparison then gives the desired boundary limit.

### Two diagnostic Wiener sums

For an exterior cone, every shell \(E_k\) contains a ball of radius \(c r_k\), so
\[
 \frac{\operatorname{Cap}(E_k)}{r_k^{n-2}}
 \ge (n-2)\sigma_{n-1} c^{n-2}>0;
\]
thus the Wiener series diverges.

For the three-dimensional superthin obstacle construction, let \(r_k=2^{-k}\) and put \(c_k=(3r_k/4,0,0)\), \(a_k=2^{-k^2}\) for \(k\ge3\), with \(K=\{0\}\cup\bigcup_{k\ge3}\overline B(c_k,a_k)\). For large \(k\), each ball lies inside its dyadic annulus; the finitely many initial scales can be adjusted harmlessly. For \(D=B_1\setminus K\) near the origin,
\[
 \operatorname{Cap}(E_k)=4\pi a_k,
 \qquad \sum_{k\ge3}\frac{\operatorname{Cap}(E_k)}{r_k}
 =4\pi\sum_{k\ge3}2^{k-k^2}<\infty.
\]
Therefore 0 is irregular, despite positive-volume exterior obstacles at arbitrarily small scales. The computation uses three-dimensional ball capacity; in dimension two the criterion needs its logarithmic version.

### The punctured ball and continuous boundary data

Let \(D=B_1\setminus\{0\}\) for \(n\ge2\), with \(g|_{\partial B_1}=0\) and \(g(0)=1\). The function \(g\) is continuous on \(\partial D=S^{n-1}\cup\{0\}\). Every bounded harmonic \(u\) with zero outer boundary values extends over 0 and must equal zero by the maximum principle. Hence no bounded harmonic solution can attain \(g(0)=1\) continuously, and 0 is irregular.

### Exercises and worked answers

1. **Barrier verification.** For unit \(x_0\), compute \(\Delta(1-x\cdot x_0)\). **Answer:** zero; it is affine.
2. **Puncture data.** Is \(g(0)=1\), \(g=0\) on \(\partial B_1\), continuous on \(\partial(B_1\setminus\{0\})\)? **Answer:** yes; 0 is an isolated boundary point.
3. **Cone capacity.** In \(\mathbb R^3\), if every \(E_k\) contains a ball of radius \(r_k/10\), what is the lower bound on \(\operatorname{Cap}(E_k)/r_k\)? **Answer:** at least \(4\pi/10\).
4. **Thin obstacles.** Why does \(\sum_k 2^{k-k^2}\) converge? **Answer:** from \(k\ge2\), \(k-k^2\le-k\), so the terms are bounded by a geometric sequence.
5. **Capacity scale.** In dimension five, what power of \(r_k\) normalizes Newtonian capacity? **Answer:** \(r_k^3\).
6. **Two kinds of regularity.** Does a reentrant corner's failure of global \(H^2\) regularity prove the corner Wiener irregular? **Answer:** no; pointwise Dirichlet regularity and second-derivative Sobolev regularity are different properties.

### Sources and further reading

- [On the Wiener criterion in higher dimensions](https://link.springer.com/article/10.1186/s13661-017-0907-5), explicit dyadic exterior-capacity criterion and exterior-cone implication.
- [The Wiener criterion for fully nonlinear elliptic equations](https://pmc.ncbi.nlm.nih.gov/articles/PMC9900964/), barriers, classical boundary regularity, and extensions beyond the Laplacian.
- [Michael Taylor, *Harmonic Functions on Domains in Rn*, Section 8](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2021/02/dprn.pdf), why a puncture is removable for bounded harmonic functions.
- [Wikipedia: Capacity of a set](https://en.wikipedia.org/wiki/Capacity_of_a_set), capacitary normalization and physical intuition.
- [Wikipedia: Harmonic measure](https://en.wikipedia.org/wiki/Harmonic_measure), probabilistic boundary influence.
- Library connections: `multivariable-calculus:056000` (capacity), `057000` (removability), `052000` (harmonic measure), `046000` (corner regularity).
