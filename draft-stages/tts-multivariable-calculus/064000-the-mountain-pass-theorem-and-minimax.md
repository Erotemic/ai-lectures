# The Mountain-Pass Theorem: From a Forced Barrier to a Critical Point

**Track:** Multivariable Calculus from First Principles. **Focus:** minimax critical levels, exact hypotheses, a deformation argument, and the role of Palais–Smale compactness.

<!-- BEGIN SPOKEN LECTURE -->

# The Mountain-Pass Theorem: From a Forced Barrier to a Critical Point

We have seen a simple landscape where a path between two low points must climb over a barrier. In the polynomial example we could solve for the critical point explicitly. In a space of functions we usually cannot. A theorem must replace the explicit calculation. The mountain-pass theorem is one of the central results that makes this possible.

It is associated with Antonio Ambrosetti and Paul Rabinowitz, whose 1973 work developed critical-point methods for nonlinear problems. The statement is appealingly geometric, but it has two logically separate parts. The geometry creates a positive minimax energy level. A compactness condition ensures that the level is realized by an actual stationary function. Neither part should be silently substituted for the other.

## The setting and the energy barrier

Let X be a real Banach space. That means a complete normed vector space, and it may be infinite dimensional. Our unknown may be a vector, but it may also be a function. Let J assign a real energy to each point of X. Assume J is continuously Fréchet differentiable. Its derivative at a point u is a bounded linear functional acting on possible variations v. A critical point is a point where the derivative is zero as a functional, so every first-order variation vanishes.

For simplicity, suppose the energy at zero is zero. Suppose there is a sphere of radius r centered at zero on which the energy is at least some positive number a. This is the barrier: every shape at that distance from zero costs at least a units of energy.

Also suppose there is a point e farther from zero than r, but its energy is zero or negative. So we begin at zero, have to cross the positive-energy sphere, and eventually reach a point whose energy is no greater than where we started.

Now consider every continuous path through the space that starts at zero and ends at e. Each such path has a largest energy. Call the infimum of these largest energies c. Because every path must cross the sphere of radius r, and because the energy is at least a on that sphere, c is at least a. In particular, c is strictly positive. This already shows that the barrier separates the desired critical point from the trivial solution at zero.

But we still know only a number. We have not proved that any particular path reaches a stationary point. The minimizing path may not exist. Even if it did, the point where its energy is largest might not be stationary against variations that move away from the path.

## An analogy with climbing down

Suppose for a moment the space were ordinary Euclidean space, and the energy had a smooth gradient. At any point where the gradient is nonzero, there is a direction of steepest descent: minus the gradient. If we move a little in that direction, the energy decreases. Along a smooth gradient-descent trajectory, the rate of change of energy equals minus the square of the gradient norm. It cannot increase.

This suggests a contradiction argument. Imagine that there were no critical points whose energies were near c. If the gradient stayed uniformly away from zero throughout that energy band, we could deform every nearly optimal path downward while keeping its endpoints fixed. A path whose highest energy is just above c would turn into one whose highest energy is below c. That contradicts the definition of c as the least possible highest energy.

What can prevent this argument? The gradient might be nonzero at each point but become arbitrarily small along a sequence of points whose energy approaches c. Then no single amount of descent works uniformly throughout the band. Such a sequence is an *almost critical sequence*: energy approaches the candidate level, and the size of the derivative approaches zero.

The mountain-pass argument can produce such an almost critical sequence. It is a powerful conclusion even before compactness is imposed. But an almost critical sequence does not automatically converge to a critical point. In an infinite-dimensional space, a bounded family need not even have a strongly convergent subsequence.

## The Palais–Smale condition

The missing hypothesis is traditionally expressed through the Palais–Smale condition. At an energy level c, it says this: whenever the energies of a sequence approach c and the derivative norms approach zero, there is a subsequence that converges in the norm of X.

The phrase “derivative norm” matters. A derivative is a linear functional, not necessarily another point of X. We measure its norm in the dual space of continuous linear functionals. When X is a Hilbert space, the Riesz representation theorem lets us identify the derivative with a gradient, but we should not assume this identification in every Banach space.

If the Palais–Smale condition holds at c, take the almost critical sequence provided by the mountain-pass argument. Pass to a strongly convergent subsequence, converging to some u. Continuity of J shows that J of u equals c. Continuity of the derivative shows that the derivative at u is zero. So u is an actual critical point. And because its energy is positive, it is not the zero solution.

Here is the theorem in words. For a continuously differentiable energy on a real Banach space, if zero lies inside a sphere of uniformly higher energy and there is a lower-energy point outside that sphere, then the least possible maximal energy along connecting paths is an almost critical level. If Palais–Smale compactness holds at that level, there is a nonzero critical point at that energy.

Notice the specificity. We do not assume every bounded sequence is compact. We do not assume the energy is convex. We do not even require a global lower bound for the energy. We require precisely enough compactness for the almost critical sequences generated by the geometry.

## What happens in finite dimensions

Return to the polynomial of the previous lecture: one half x squared minus one quarter x to the fourth. Choose a small positive radius, and the energy is positive at both points on the sphere, which in one dimension is just the pair of points at plus and minus that radius. Choose e equal to two. Its energy is negative, and every path from zero to two crosses one. The minimax level is one quarter, attained at x equal to one.

Here we did not need the Palais–Smale condition to guess the answer, but we can see why it is satisfied at the relevant level. A sequence whose energy approaches one quarter cannot escape toward positive or negative infinity, because the energy becomes negative infinity there. It is therefore bounded. In one dimension, bounded sequences have convergent subsequences. If the derivatives also approach zero, the limit is critical.

Do not turn that observation into the claim that *every* smooth function in finite dimensions satisfies Palais–Smale. A smooth function may have an almost critical sequence escaping to infinity at a finite energy level. Compactness must still be checked. In this polynomial it follows from the behavior of the energy at infinity.

## Why a small derivative may not be enough

Imagine the Hilbert space of square-summable sequences. Give the coordinate in position n a quadratic penalty weighted by one divided by n. A unit vector concentrated entirely in the n-th coordinate has norm one, no matter how large n is. But its energy tends to zero because that coordinate becomes cheaper and cheaper. The gradient norm also tends to zero. These unit vectors never approach one another in norm: they point in mutually orthogonal directions.

So we have a sequence of almost critical points whose energies approach zero, but which has no strongly convergent subsequence. The energy functional still has a genuine critical point at zero; this example does not prove the absence of a critical point. It proves only that the Palais–Smale compactness condition can fail for elementary-looking quadratic energies in infinite-dimensional spaces.

That distinction is essential. The theorem provides a sufficient condition for existence. Failure of its hypothesis means the theorem alone cannot resolve the problem; it does not automatically mean no solution exists.

## Applying the theorem to differential equations

Our fixed-endpoint string energy was one half the squared slope integral minus one quarter the fourth-power displacement integral. Its critical points solve the equation negative u double prime equals u cubed. We have already verified the mountain-pass geometry: zero has a positive barrier on a sufficiently small energy-norm sphere, while the energy becomes negative along a large multiple of any fixed nonzero shape.

To finish the existence proof, we must establish Palais–Smale compactness for this energy. That will require two ideas. First, an algebraic identity combining the energy and its derivative controls the slope norm of any almost critical sequence. Second, one-dimensional Sobolev compactness converts that norm bound into strong convergence of the nonlinear displacement term. The derivative equation then recovers strong convergence of the slopes.

The algebra is manageable, but each step matters. Bounding energy alone does not always bound the unknown; the negative quartic term is the reason. Weak convergence does not automatically pass a cubic nonlinearity to the limit. And a strong limit of the displacement alone must be upgraded to a strong limit in the energy norm.

The mountain-pass theorem is therefore not a shortcut around analysis. It organizes the work. Geometry says where a solution could be. Compactness says why the candidate cannot vanish into an escaping sequence. Together they yield a stationary shape that ordinary energy minimization could never find.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### The mountain-pass theorem, precisely stated

Let \(X\) be a real Banach space and \(J\in C^1(X,\mathbb R)\) with \(J(0)=0\). Suppose there are \(r>0\), \(a>0\), and \(e\in X\) such that
\[
 \|e\|>r,\qquad J(e)\leq0,\qquad \inf_{\|u\|=r}J(u)\geq a.
\]
Define \(\Gamma=\{\gamma\in C([0,1],X):\gamma(0)=0,\gamma(1)=e\}\) and
\[
 c=\inf_{\gamma\in\Gamma}\max_{t\in[0,1]}J(\gamma(t)).
\]
Then \(c\geq a\). The standard minimax/deformation result provides a sequence \(u_k\) with \(J(u_k)\to c\) and \(\|J'(u_k)\|_{X^*}\to0\). If \((PS)_c\) holds, meaning every such sequence has a norm-convergent subsequence, there is \(u\in X\) such that \(J(u)=c\) and \(J'(u)=0\). In particular \(u\neq0\).

The deformation argument uses a locally Lipschitz pseudogradient (or another suitable deformation construction), rather than assuming arbitrary \(C^1\) Banach-space functionals possess complete smooth gradient flows. If there were no almost-critical sequence near \(c\), the gradient would be bounded away from zero in a small energy band, allowing one to deform a nearly optimal path below \(c\) without moving its low-energy endpoints; contradiction.

### Noncompact quadratic example

On \(\ell^2\), let \(Q(x)=\sum_{n\geq1}x_n^2/n\). This is \(C^1\) with \(Q'(x)[h]=2\sum x_nh_n/n\). For the standard basis vectors \(e_n\),
\[
 Q(e_n)=1/n\to0,\qquad \|Q'(e_n)\|=2/n\to0,
\]
but \(\|e_n-e_m\|=\sqrt2\) for \(n\neq m\). Thus \((PS)_0\) fails. The example makes **no** assertion that \(Q\) lacks critical points; \(0\) is one.

### Exercises with answers

1. **Sphere barrier.** Why must each \(\gamma\in\Gamma\) meet \(\{u:\|u\|=r\}\)? **Answer:** the continuous function \(t\mapsto\|\gamma(t)\|\) starts at zero and ends above \(r\).
2. **Critical energy.** If \(J(0)=0\) and \(c\geq a>0\), can the conclusion be the zero point? **Answer:** no, because its energy is zero.
3. **PS versus boundedness.** Does a bounded Palais–Smale sequence necessarily converge in a Banach space? **Answer:** no; boundedness gives weak subsequences in some spaces, not strong convergence in general.
4. **Dual norm.** For \(Q\) on \(\ell^2\), compute \(\|Q'(e_n)\|\). **Answer:** \(2/n\).
5. **Geometry alone.** What conclusion does the minimax theorem support without \((PS)_c\)? **Answer:** an almost-critical sequence, not necessarily an attained critical point.

### Sources and further reading

- [A. Ambrosetti and P. H. Rabinowitz (1973), *Dual variational methods in critical point theory and applications*](https://doi.org/10.1016/0022-1236(73)90051-7), original research paper.
- [University of Pisa, *Metodi Variazionali*, §7](https://poisson.phc.dm.unipi.it/~fpmaiale/notes/MetodiVariazionali.pdf), deformation lemma and mountain-pass proof.
- [Nonlinear Differential Equations, Palais–Smale and Mountain Pass notes](https://citeseerx.ist.psu.edu/document?doi=76cf2ed80f7d4b86ab165a1b91a04a3c72ac8d46&repid=rep1&type=pdf), precise distinction between a Palais–Smale sequence and a compactness conclusion.
- [Wikipedia: Palais–Smale compactness condition](https://en.wikipedia.org/wiki/Palais%E2%80%93Smale_compactness_condition), terminology.
- Library preparation: `multivariable-calculus:063000`, `035000`, `037000`; `analysis:038000`.
