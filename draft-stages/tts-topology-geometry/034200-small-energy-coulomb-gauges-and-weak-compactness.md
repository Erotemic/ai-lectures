# 034200 - Small-Energy Gauges and Compactness: The Local Uhlenbeck Estimate

**Track:** Topology and Geometry. **Background:** Sobolev spaces, Coulomb gauge, elliptic estimates, Yang-Mills curvature energy. **Central question:** how can bounded curvature control a connection when the connection form itself can be arbitrarily large in a bad gauge?

<!-- BEGIN SPOKEN LECTURE -->

# Small-Energy Gauges and Compactness: The Local Uhlenbeck Estimate

Suppose we know the curvature of a connection has bounded square-integrable norm. We would like to say that the connection itself is controlled well enough to extract a convergent subsequence. But a difficulty appears immediately. Curvature is gauge covariant, and its norm is gauge invariant. A local connection one-form is not gauge invariant. By making a rapidly varying gauge transformation, we can turn a harmless connection form into one with very large derivatives, while leaving its curvature norm unchanged.

So there cannot be a useful theorem saying that an arbitrary chosen connection one-form is bounded whenever its curvature is bounded. We first need a gauge in which the one-form can be estimated. Uhlenbeck's local gauge theorem supplies exactly such a gauge when curvature energy is sufficiently small.

## The flat but wildly written connection

Take the trivial unitary line bundle on a disk. Start with the zero connection one-form, so the curvature is zero. Apply a gauge transformation whose phase oscillates rapidly in space. In the new trivialization, the connection form is the differential of that phase, times the imaginary unit. Its coefficients may vary as rapidly as we like. Yet its curvature is still zero, because differentiating a gradient twice in the alternating exterior sense gives zero.

This example shows why ordinary componentwise bounds are not geometric. We must choose a representative along the gauge orbit. A Coulomb gauge, with zero covariant divergence relative to a reference, is a natural choice.

## The nonlinear estimate in a ball

On a four-dimensional ball, assume the squared curvature is sufficiently small in the scale-invariant norm. Under the hypotheses of the local theorem, there exists a gauge in which the connection one-form satisfies a Coulomb condition and a compatible boundary condition. In that gauge its first-Sobolev norm is bounded by a constant times the square-integrable curvature norm.

Why should that be plausible? In a Coulomb gauge, the exterior derivative and codifferential of the connection form together form an elliptic system. Curvature controls the exterior derivative up to the quadratic product of the form with itself. The Sobolev embedding in four dimensions puts the form in fourth-power integrable space, so its quadratic product is square integrable.

The crucial step is absorption. If curvature energy is sufficiently small, the nonlinear term can be handled in the elliptic estimate. The result controls the full first-Sobolev norm of the gauge-fixed connection form by curvature. The proof requires the actual gauge construction and nonlinear estimates; the heuristic does not produce the theorem by itself.

The smallness threshold matters. We should not replace it by 'bounded energy on a ball' without checking the bound. Large energy could be concentrated in that ball, precisely the situation where bubbling becomes possible.

## Covering a manifold without too much energy

Now consider a sequence of smooth connections on a fixed compact four-manifold, with their curvature energies uniformly bounded. Fix a small energy threshold from the local gauge theorem. Divide the manifold into small balls. Wherever the curvature energy stays below threshold, choose the controlled local gauges and obtain first-Sobolev bounds.

A bounded sequence in a first-Sobolev Hilbert space has weakly convergent subsequences. Compact Sobolev embedding gives stronger convergence in lower-order spaces. By extracting subsequences on overlapping balls and controlling the transition functions, one can assemble a limiting geometric connection away from regions where energy concentrates.

There can be only finitely many distinct concentration points above a fixed positive threshold, because the total energy is bounded. But the number and location of such points depend on the sequence. This is why the compactness statement naturally takes the form 'after gauges and subsequences, away from finitely many points.'

## Two compactness results that should not be confused

There is a useful contrast between curvature controlled in an integrability exponent strictly above the scale-critical exponent and curvature controlled only at the critical exponent. In four dimensions, that critical exponent is two.

With appropriate supercritical integrability and global hypotheses, Uhlenbeck's compactness theory can give weak compactness after gauge without the same point-bubbling obstruction. At the critical square-integrable exponent, bounded energy can concentrate. One generally extracts a limit only away from finitely many points, and more information is required to describe the missing energy.

This is not because weak compactness ceases to exist in all senses at the critical exponent. It is because the gauge estimates cannot be made uniformly small on every shrinking ball centered at a concentration point. The geometry of the limit may also live on a bundle whose topological charge differs from that of the approximating connections.

## Regularity after choosing a gauge

For a sequence of connections satisfying the anti-self-dual equation, the Coulomb-gauge equations form an elliptic system. Where the local estimates remain uniform, elliptic regularity can improve the convergence and produce a smooth limiting anti-self-dual connection after further gauges and subsequences.

That upgrade depends on the solutions satisfying the appropriate differential equation. A completely arbitrary sequence of connections with bounded curvature is not automatically a sequence of smooth-convergent Yang-Mills solutions. We must distinguish a compactness theorem for connections with integrability bounds from the stronger conclusions obtained for solutions of a fixed elliptic gauge equation.

The overall strategy is now clear. Use gauge invariance to select local Coulomb representatives; use small curvature to control their Sobolev norms; take weak and strong limits where the estimates apply; and use elliptic regularity for actual solutions. The only remaining obstacle is energy concentration in shrinking regions, which will be the subject of the next lecture.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a connection \(A=d+a\) on a bundle trivialized over a four-ball \(B\), Uhlenbeck's small-energy gauge theorem has the schematic form: if \(\|F_A\|_{L^2(B)}<\varepsilon\) (with appropriate geometric and bundle hypotheses), there is a gauge such that
\[d^*a=0,\qquad a\cdot\nu|_{\partial B}=0,\qquad \|a\|_{W^{1,2}(B)}\le C\|F_A\|_{L^2(B)}.\]
Local gauge conventions, boundary formulations, and exact function spaces vary among statements. The mechanism uses \(F_A=da+a\wedge a\), a first-order elliptic estimate for \(d+d^*\), and \(\|a\wedge a\|_{L^2}\lesssim\|a\|_{L^4}^2\lesssim\|a\|_{W^{1,2}}^2\). The nonlinear inequality requires a small-energy argument; it is not a global linear estimate for arbitrary \(a\).

For an energy-bounded ASD sequence \(A_j\) over a fixed closed oriented four-manifold, the standard compactness framework obtains local gauge convergence away from a finite concentration set, followed by elliptic bootstrapping for solutions. The supercritical \(L^p\) compactness theorem for \(p>n/2\) is distinct from the critical \(p=n/2=2\) bubbling regime. Do not infer uniform global Coulomb gauges or smooth convergence from an \(L^2\) energy bound alone.

### Exercises with answers

1. **Flat gauge.** Can a flat connection have a large local connection one-form? **Answer:** yes, after a rapidly varying gauge transformation.
2. **Smallness.** Which scale-critical curvature norm appears in four-dimensional local gauge fixing? **Answer:** \(L^2\).
3. **Quadratic term.** Why is \(a\wedge a\) in \(L^2\) when \(a\in W^{1,2}\)? **Answer:** \(W^{1,2}\hookrightarrow L^4\) and \(L^4\cdot L^4\subset L^2\).
4. **Conclusion.** Does bounded energy alone give globally smooth convergence modulo gauge? **Answer:** no; energy concentration may obstruct it.

### Sources and further reading

- Karen Uhlenbeck, [Connections with L-p bounds on curvature](https://doi.org/10.1007/BF01947069), *Communications in Mathematical Physics* 83 (1982), 31-42.
- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), chapters on compactness and Sobolev gauge transformations.
- Overviews: [Uhlenbeck compactness theorem](https://en.wikipedia.org/wiki/Uhlenbeck%27s_compactness_theorem), [Gauge fixing](https://en.wikipedia.org/wiki/Gauge_fixing).
