# 034300 - Bubbling and Removable Singularities: Where Instanton Energy Goes

**Track:** Topology and Geometry. **Background:** self-dual curvature, Yang-Mills energy, critical Sobolev estimates, local Uhlenbeck gauges. **Central question:** how can instantons have a convergent limit away from points while retaining a fixed total topological charge?

<!-- BEGIN SPOKEN LECTURE -->

# Bubbling and Removable Singularities: Where Instanton Energy Goes

An energy-bounded sequence of anti-self-dual connections on a compact four-manifold has strong structure. Local gauge estimates and elliptic regularity control the sequence wherever curvature energy is small. Yet a sequence may still fail to converge smoothly across a finite set of points. Curvature is gathering into smaller neighborhoods while its total squared norm stays fixed.

This phenomenon is called bubbling. To understand it, we should not imagine that a smooth solution suddenly becomes infinite at one ordinary point. Instead, an entire nontrivial connection profile is appearing at a smaller and smaller length scale. When we zoom in, the profile becomes visible; when we do not zoom in, its energy looks concentrated at a point.

## Watching a charge-one instanton shrink

Return to the charge-one instanton on Euclidean four-space. It has a center and a positive scale. As the scale shrinks toward zero, the curvature grows near the center and becomes negligible at every fixed location away from it. The integrated curvature energy remains eight pi squared under our chosen normalization.

Viewed without magnification, the field seems to approach a flat connection away from the center. But a flat connection carries no charge-one curvature energy. If we simply discarded the center, we would apparently lose a topological invariant.

Now rescale space near the center by the shrinking instanton's own length scale. The profile regains its original size and shape. The missing energy is not an artifact of a bad gauge or numerical rounding. It belongs to a genuine additional instanton that lives on the zoomed-in geometry.

## Energy measures remember what ordinary limits forget

There is a precise way to record this. Associate to each connection a measure that assigns to a region the integral of squared curvature over that region. Because the total energy is uniformly bounded, subsequences of these measures have weak limits.

For a bubbling sequence of anti-self-dual SU-two connections, the limit measure has two pieces. One is the energy density of the limiting connection away from the concentration points. The other is a finite sum of point masses at the bubbling locations. Under the standard compactness and energy-identity hypotheses, each mass is eight pi squared times a positive integer, with our normalization.

Why integers? A bubble, after rescaling and adding the point at infinity, corresponds to a finite-energy instanton on the four-sphere. Its second Chern number is an integer. The topological energy equality turns that integer into a fixed energy packet.

This quantization is a special feature of the anti-self-dual SU-two setting with the specified normalization. For arbitrary Yang-Mills critical points or other structure groups, energy spectra and quantization statements require their own hypotheses. The phrase 'every bubble has energy eight pi squared' would be wrong when a bubble can carry higher charge; it can be a positive integer multiple in this setting.

## What changes about the limiting bundle

Suppose the original bundle has second Chern number k. If one unit-charge bubble separates, the smooth limiting connection away from the bubbling point can extend across that point as a connection on a bundle with second Chern number k minus one. The missing charge is recorded at the point in the compactified moduli space.

More generally, the total charge splits into the charge of the limiting bundle and the positive integer charges carried by the bubbles. Understanding this topological accounting is one purpose of the Uhlenbeck compactification of the instanton moduli space. It adds ideal instantons: a lower-charge smooth instanton together with a finite unordered collection of weighted concentration points.

The compactification does not simply declare a singular one-form to be a new smooth connection. It keeps separate the genuine connection data and the ideal point charges representing vanished scales.

## Apparent singularity versus removable singularity

There is another issue. Suppose we have a finite-energy Yang-Mills connection on a punctured ball in four dimensions. It is smooth away from the missing center. Does the puncture mean the field is genuinely singular?

Uhlenbeck's removable-singularity theorem says that under the appropriate Yang-Mills and finite-energy hypotheses, a suitable gauge transformation allows the connection to extend smoothly across the missing point, with the appropriate bundle interpretation. The result does not say arbitrary finite-energy connection one-forms automatically extend smoothly in their original gauge.

In bubbling arguments, removable singularities let us treat the rescaled nontrivial limit on Euclidean four-space as a smooth Yang-Mills connection over the four-sphere, including the point at infinity. That is how the integer topological charge of the bubble becomes available.

## Why this is not a contradiction

If removable singularities exist, why can the original sequence fail to converge smoothly across a bubbling point? Because there are two different objects. The limiting connection away from the point may extend smoothly after an appropriate gauge and may live on a lower-charge bundle. The energy lost from the original sequence appears as a separate bubble at another scale. Removability concerns the regularity of an individual finite-energy solution on a punctured domain; it does not force all energy in a sequence to remain in the unrescaled limit.

This distinction connects the analytic and topological halves of the theory. The small-energy theorem identifies where gauge-fixed convergence is possible. Blow-up analysis identifies a nontrivial rescaled solution. Removable-singularity theory completes that solution across infinity. Chern-Weil theory measures its integer charge. The compactification records the pieces together.

When later lectures invoke Uhlenbeck compactness, the content is not merely 'take a convergent subsequence.' It is a structured account of how subsequences converge, how gauges are chosen, where smooth convergence fails, and why the failure has quantized topological information. This is the foundation for understanding the boundaries and degenerations of instanton moduli spaces.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an ASD SU(2) sequence \(A_j\) of fixed topological charge \(k\) over a closed oriented four-manifold, after passing to a subsequence and gauges there is a finite singular set \(\{x_1,\dots,x_m\}\), a smooth ASD connection \(A_\infty\) on a possibly lower-charge bundle, and positive integers \(k_\ell\), such that under standard Uhlenbeck compactness and energy identity conclusions,
\[|F_{A_j}|^2\,d\mathrm{vol}\ \rightharpoonup\ |F_{A_\infty}|^2\,d\mathrm{vol}+8\pi^2\sum_{\ell=1}^m k_\ell\,\delta_{x_\ell},\qquad k=c_2(P_\infty)[X]+\sum_{\ell=1}^m k_\ell.\]
Multiple nested scales at one point require a bubble-tree analysis; the aggregate point mass may contain several bubbles. The numbers shown use the standard matrix-trace and orientation convention of 034100. On a round \(S^4\), charge-one BPST instantons with scale \(\rho_j\to0\) give \(|F_{A_j}|^2\,dx\rightharpoonup8\pi^2\delta_0\) on a stereographic chart while the unrescaled limit is flat away from the center.

Uhlenbeck's removable-singularity theorem applies to finite-energy four-dimensional Yang-Mills connections on punctured balls, up to gauge and the appropriate extension of bundle data. It does not assert that any finite-energy distributional connection, or any arbitrary sequence, extends smoothly without using its equation.

### Exercises with answers

1. **Energy packet.** Under the specified ASD SU(2) convention, how much energy can a charge-two bubble carry? **Answer:** \(16\pi^2\).
2. **Bookkeeping.** If the original charge is four and the limit has charge one, what is the sum of bubble charges? **Answer:** three.
3. **Removability.** Does a removable-singularity theorem force an entire sequence to converge smoothly at a concentration point? **Answer:** no; it concerns the individual rescaled or punctured limiting solution.
4. **Dimension.** Why can bubble scales shrink without increasing energy in dimension four? **Answer:** \(\int|F|^2\) is scale invariant in four dimensions.

### Sources and further reading

- Karen Uhlenbeck, [Removable singularities in Yang-Mills fields](https://doi.org/10.1007/BF01947068), *Communications in Mathematical Physics* 83 (1982), 11-29.
- Karen Uhlenbeck, [Connections with L-p bounds on curvature](https://doi.org/10.1007/BF01947069), *Communications in Mathematical Physics* 83 (1982), 31-42.
- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), compactness chapter.
- Overviews: [Uhlenbeck compactness theorem](https://en.wikipedia.org/wiki/Uhlenbeck%27s_compactness_theorem), [BPST instanton](https://en.wikipedia.org/wiki/BPST_instanton).
