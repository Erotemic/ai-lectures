# Yang-Mills energy, small-energy gauges, bubbling, and compactness

<!-- BEGIN SPOKEN LECTURE -->

# Yang-Mills energy, small-energy gauges, bubbling, and compactness

## Yang-Mills Energy and Instanton Charge: Why Four Dimensions Matter

We have learned to study the local deformation theory of anti-self-dual connections. But this does not tell us what happens to a sequence of solutions as they vary. For compactness we need an energy estimate. In four-dimensional gauge theory, the central energy is the integral of the squared magnitude of curvature.

The striking fact is that on an oriented four-manifold, curvature energy is tied to a characteristic number of the bundle. The anti-self-dual equation realizes an equality case of a topological lower bound. At the same time, the energy is unchanged under rescaling in dimension four, so curvature can concentrate on smaller and smaller regions without raising the total energy. The same dimension creates both rigidity and difficulty.

### Why curvature has two halves

A two-form on an oriented Riemannian four-manifold has a special symmetry. The Hodge star sends two-forms to two-forms and squares to the identity. Its plus-one eigenspace consists of self-dual forms; its minus-one eigenspace consists of anti-self-dual forms.

Every curvature two-form splits uniquely into its self-dual and anti-self-dual pieces. They are orthogonal for the natural metric. So the total squared curvature norm is the sum of the squared norms of the two pieces.

But there is another combination: the difference of those two squared norms. That difference is the four-form obtained from curvature wedged with curvature, interpreted with the invariant inner product and orientation. When integrated and properly normalized, it determines the second Chern number of an SU-two bundle, up to a consistent sign convention.

Thus the sum of two nonnegative energies is constrained by their difference. The sum cannot be smaller than the absolute value of the difference. This elementary inequality is the origin of the topological energy bound.

### A bound that detects anti-self-duality

Fix conventions in which the second Chern number k is nonnegative for anti-self-dual connections. The curvature energy is at least eight pi squared times the absolute value of k, when we use the standard matrix-trace normalization.

For positive k, equality holds precisely when the self-dual curvature piece vanishes, meaning the connection is anti-self-dual. For negative k, equality instead selects self-dual connections. The orientation matters: reversing it swaps the two Hodge-star eigenspaces and changes the signed topological charge.

The anti-self-dual equation is therefore not simply another arbitrary partial differential equation. It selects absolute minimizers of Yang-Mills curvature energy in a topological class, under the stated normalization and for the relevant sign of the charge.

### The unit-charge instanton

On Euclidean four-space, there is a famous family of finite-energy anti-self-dual SU-two connections, related to the BPST instanton. It includes a center and a positive scale parameter. Stereographic compactification relates the finite-energy field on four-space to a connection over the four-sphere.

The scale parameter has an important effect. Shrink the scale and the curvature peak becomes narrower and taller. The field is still a smooth instanton for every positive scale. Its total energy stays fixed at eight pi squared for charge one, but that energy lies in an ever smaller neighborhood of the center.

A sequence obtained by letting the scale tend to zero need not converge smoothly across the center. Away from it, the connections can approach a flat limit after gauge transformations. The lost energy has not vanished: it is concentrating at the center.

### Why dimension four is the threshold

Scale the coordinates by a length factor. A connection one-form has scaling dimension one over length, and curvature has dimension one over length squared. Its squared norm therefore scales as one over length to the fourth power. The volume element in n dimensions scales as length to the nth power. So the total curvature-squared integral scales as length to the power n minus four.

Only in dimension four does this exponent vanish. There the energy does not prefer a large or a small scale. That critical scaling helps explain why a uniformly bounded energy sequence can develop finer and finer structures without violating the bound.

In higher dimensions, curvature energy is not scale invariant and different regularity difficulties appear. In lower dimensions, concentration at a point interacts with energy bounds differently. Results proved for four-dimensional instantons should not be exported automatically to arbitrary dimension.

### Minimizers and compactness are separate questions

Knowing every anti-self-dual connection minimizes energy does not make the set of minimizers compact. A sequence of minimizing configurations can move its center, change gauge, or shrink its scale. On a compact four-manifold, centers cannot run away to infinity, but scales can still collapse toward zero.

To understand limits, we need both the weak compactness tools of Sobolev analysis and a way to repair gauge freedom. We then need to identify what happens near the points where the energy concentrates. This is the content of the local gauge estimates and bubbling analysis that follow.

The two identities worth carrying forward are the decomposition of curvature into self-dual and anti-self-dual parts, and the scale invariance of squared curvature energy in four dimensions. The first gives topological control. The second tells us why the control is not enough to prevent concentration.

## Small-Energy Gauges and Compactness: The Local Uhlenbeck Estimate

Suppose we know the curvature of a connection has bounded square-integrable norm. We would like to say that the connection itself is controlled well enough to extract a convergent subsequence. But a difficulty appears immediately. Curvature is gauge covariant, and its norm is gauge invariant. A local connection one-form is not gauge invariant. By making a rapidly varying gauge transformation, we can turn a harmless connection form into one with very large derivatives, while leaving its curvature norm unchanged.

So there cannot be a useful theorem saying that an arbitrary chosen connection one-form is bounded whenever its curvature is bounded. We first need a gauge in which the one-form can be estimated. Uhlenbeck's local gauge theorem supplies exactly such a gauge when curvature energy is sufficiently small.

### The flat but wildly written connection

Take the trivial unitary line bundle on a disk. Start with the zero connection one-form, so the curvature is zero. Apply a gauge transformation whose phase oscillates rapidly in space. In the new trivialization, the connection form is the differential of that phase, times the imaginary unit. Its coefficients may vary as rapidly as we like. Yet its curvature is still zero, because differentiating a gradient twice in the alternating exterior sense gives zero.

This example shows why ordinary componentwise bounds are not geometric. We must choose a representative along the gauge orbit. A Coulomb gauge, with zero covariant divergence relative to a reference, is a natural choice.

### The nonlinear estimate in a ball

On a four-dimensional ball, assume the squared curvature is sufficiently small in the scale-invariant norm. Under the hypotheses of the local theorem, there exists a gauge in which the connection one-form satisfies a Coulomb condition and a compatible boundary condition. In that gauge its first-Sobolev norm is bounded by a constant times the square-integrable curvature norm.

Why should that be plausible? In a Coulomb gauge, the exterior derivative and codifferential of the connection form together form an elliptic system. Curvature controls the exterior derivative up to the quadratic product of the form with itself. The Sobolev embedding in four dimensions puts the form in fourth-power integrable space, so its quadratic product is square integrable.

The crucial step is absorption. If curvature energy is sufficiently small, the nonlinear term can be handled in the elliptic estimate. The result controls the full first-Sobolev norm of the gauge-fixed connection form by curvature. The proof requires the actual gauge construction and nonlinear estimates; the heuristic does not produce the theorem by itself.

The smallness threshold matters. We should not replace it by 'bounded energy on a ball' without checking the bound. Large energy could be concentrated in that ball, precisely the situation where bubbling becomes possible.

### Covering a manifold without too much energy

Now consider a sequence of smooth connections on a fixed compact four-manifold, with their curvature energies uniformly bounded. Fix a small energy threshold from the local gauge theorem. Divide the manifold into small balls. Wherever the curvature energy stays below threshold, choose the controlled local gauges and obtain first-Sobolev bounds.

A bounded sequence in a first-Sobolev Hilbert space has weakly convergent subsequences. Compact Sobolev embedding gives stronger convergence in lower-order spaces. By extracting subsequences on overlapping balls and controlling the transition functions, one can assemble a limiting geometric connection away from regions where energy concentrates.

There can be only finitely many distinct concentration points above a fixed positive threshold, because the total energy is bounded. But the number and location of such points depend on the sequence. This is why the compactness statement naturally takes the form 'after gauges and subsequences, away from finitely many points.'

### Two compactness results that should not be confused

There is a useful contrast between curvature controlled in an integrability exponent strictly above the scale-critical exponent and curvature controlled only at the critical exponent. In four dimensions, that critical exponent is two.

With appropriate supercritical integrability and global hypotheses, Uhlenbeck's compactness theory can give weak compactness after gauge without the same point-bubbling obstruction. At the critical square-integrable exponent, bounded energy can concentrate. One generally extracts a limit only away from finitely many points, and more information is required to describe the missing energy.

This is not because weak compactness ceases to exist in all senses at the critical exponent. It is because the gauge estimates cannot be made uniformly small on every shrinking ball centered at a concentration point. The geometry of the limit may also live on a bundle whose topological charge differs from that of the approximating connections.

### Regularity after choosing a gauge

For a sequence of connections satisfying the anti-self-dual equation, the Coulomb-gauge equations form an elliptic system. Where the local estimates remain uniform, elliptic regularity can improve the convergence and produce a smooth limiting anti-self-dual connection after further gauges and subsequences.

That upgrade depends on the solutions satisfying the appropriate differential equation. A completely arbitrary sequence of connections with bounded curvature is not automatically a sequence of smooth-convergent Yang-Mills solutions. We must distinguish a compactness theorem for connections with integrability bounds from the stronger conclusions obtained for solutions of a fixed elliptic gauge equation.

The overall strategy is now clear. Use gauge invariance to select local Coulomb representatives; use small curvature to control their Sobolev norms; take weak and strong limits where the estimates apply; and use elliptic regularity for actual solutions. The remaining obstacle is energy concentration in shrinking regions. We can now examine what happens where the small-curvature bound fails.

## Bubbling and Removable Singularities: Where Instanton Energy Goes

An energy-bounded sequence of anti-self-dual connections on a compact four-manifold has strong structure. Local gauge estimates and elliptic regularity control the sequence wherever curvature energy is small. Yet a sequence may still fail to converge smoothly across a finite set of points. Curvature is gathering into smaller neighborhoods while its total squared norm stays fixed.

This phenomenon is called bubbling. To understand it, we should not imagine that a smooth solution suddenly becomes infinite at one ordinary point. Instead, an entire nontrivial connection profile is appearing at a smaller and smaller length scale. When we zoom in, the profile becomes visible; when we do not zoom in, its energy looks concentrated at a point.

### Watching a charge-one instanton shrink

Return to the charge-one instanton on Euclidean four-space. It has a center and a positive scale. As the scale shrinks toward zero, the curvature grows near the center and becomes negligible at every fixed location away from it. The integrated curvature energy remains eight pi squared under our chosen normalization.

Viewed without magnification, the field seems to approach a flat connection away from the center. But a flat connection carries no charge-one curvature energy. If we simply discarded the center, we would apparently lose a topological invariant.

Now rescale space near the center by the shrinking instanton's own length scale. The profile regains its original size and shape. The missing energy is not an artifact of a bad gauge or numerical rounding. It belongs to a genuine additional instanton that lives on the zoomed-in geometry.

### Energy measures remember what ordinary limits forget

There is a precise way to record this. Associate to each connection a measure that assigns to a region the integral of squared curvature over that region. Because the total energy is uniformly bounded, subsequences of these measures have weak limits.

For a bubbling sequence of anti-self-dual SU-two connections, the limit measure has two pieces. One is the energy density of the limiting connection away from the concentration points. The other is a finite sum of point masses at the bubbling locations. Under the standard compactness and energy-identity hypotheses, each mass is eight pi squared times a positive integer, with our normalization.

Why integers? A bubble, after rescaling and adding the point at infinity, corresponds to a finite-energy instanton on the four-sphere. Its second Chern number is an integer. The topological energy equality turns that integer into a fixed energy packet.

This quantization is a special feature of the anti-self-dual SU-two setting with the specified normalization. For arbitrary Yang-Mills critical points or other structure groups, energy spectra and quantization statements require their own hypotheses. The phrase 'every bubble has energy eight pi squared' would be wrong when a bubble can carry higher charge; it can be a positive integer multiple in this setting.

### What changes about the limiting bundle

Suppose the original bundle has second Chern number k. If one unit-charge bubble separates, the smooth limiting connection away from the bubbling point can extend across that point as a connection on a bundle with second Chern number k minus one. The missing charge is recorded at the point in the compactified moduli space.

More generally, the total charge splits into the charge of the limiting bundle and the positive integer charges carried by the bubbles. Understanding this topological accounting is one purpose of the Uhlenbeck compactification of the instanton moduli space. It adds ideal instantons: a lower-charge smooth instanton together with a finite unordered collection of weighted concentration points.

The compactification does not simply declare a singular one-form to be a new smooth connection. It keeps separate the genuine connection data and the ideal point charges representing vanished scales.

### Apparent singularity versus removable singularity

There is another issue. Suppose we have a finite-energy Yang-Mills connection on a punctured ball in four dimensions. It is smooth away from the missing center. Does the puncture mean the field is genuinely singular?

Uhlenbeck's removable-singularity theorem says that under the appropriate Yang-Mills and finite-energy hypotheses, a suitable gauge transformation allows the connection to extend smoothly across the missing point, with the appropriate bundle interpretation. The result does not say arbitrary finite-energy connection one-forms automatically extend smoothly in their original gauge.

In bubbling arguments, removable singularities let us treat the rescaled nontrivial limit on Euclidean four-space as a smooth Yang-Mills connection over the four-sphere, including the point at infinity. That is how the integer topological charge of the bubble becomes available.

### Why this is not a contradiction

If removable singularities exist, why can the original sequence fail to converge smoothly across a bubbling point? Because there are two different objects. The limiting connection away from the point may extend smoothly after an appropriate gauge and may live on a lower-charge bundle. The energy lost from the original sequence appears as a separate bubble at another scale. Removability concerns the regularity of an individual finite-energy solution on a punctured domain; it does not force all energy in a sequence to remain in the unrescaled limit.

This distinction connects the analytic and topological halves of the theory. The small-energy theorem identifies where gauge-fixed convergence is possible. Blow-up analysis identifies a nontrivial rescaled solution. Removable-singularity theory completes that solution across infinity. Chern-Weil theory measures its integer charge. The compactification records the pieces together.

When later lectures invoke Uhlenbeck compactness, the content is not merely 'take a convergent subsequence.' It is a structured account of how subsequences converge, how gauges are chosen, where smooth convergence fails, and why the failure has quantized topological information. This is the foundation for understanding the boundaries and degenerations of instanton moduli spaces.

## Uhlenbeck Compactness: Where Instanton Energy Goes

Imagine a sequence of smooth connections on a four-dimensional manifold. Each connection has finite Yang-Mills energy. Every connection obeys the same anti-self-duality equation. One might expect that a uniform energy bound would force a convergent subsequence, so that a family of instantons could never run away to a singular configuration.

That expectation is almost right, but one subtle form of escape remains. A lump of curvature can become narrower and narrower while keeping a fixed amount of total energy. In the limit, the lump shrinks to a point. Away from that point, the connections behave regularly after a suitable change of gauge. At the point, energy has concentrated on a scale the limiting smooth field cannot see.

Uhlenbeck compactness makes this precise. It does not say that every bounded sequence of connections converges smoothly everywhere. It says that, under appropriate four-dimensional anti-self-dual or Yang-Mills hypotheses, we can choose gauges and extract a convergent subsequence away from finitely many concentration points. The missing curvature has a quantized accounting, and the punctures can often be filled by extending the limiting connection on a possibly different bundle.

## Gauge freedom complicates ordinary convergence

A connection is a way of differentiating sections of a vector bundle. The same geometric connection can be represented by very different local matrix-valued one-forms after a gauge transformation. Therefore direct convergence of matrix coefficients is not a gauge-invariant question.

Before applying compactness, we need to choose gauges in which the connection forms satisfy useful analytic estimates. Locally, Uhlenbeck's gauge-fixing theorem says that sufficiently small curvature energy on a ball can be used to put the connection in a controlled Coulomb gauge. Roughly, the divergence of the gauge potential is set to zero, and the potential is bounded by the curvature.

This is the first stage of the argument. If the curvature energy is small on a ball, one gains a gauge in which elliptic estimates become available. If the energy is not small, that ball may contain a concentration point. A global gauge on the original bundle need not exist, so the analysis is necessarily local and patched together.

## Why four dimensions are critical

Curvature is a two-form. Under rescaling of spatial coordinates by a factor rho, its pointwise magnitude changes like rho to the minus two. The volume of a four-dimensional region changes like rho to the fourth. Therefore the integral of the squared curvature is scale invariant in four dimensions.

This exact balance is the reason a curvature lump can shrink without losing its energy. In lower dimensions, the same scaling favors one behavior; in higher dimensions, a different analytic regime appears. Four-dimensional Yang-Mills energy is critical for rescaling.

An explicit family illustrates the phenomenon. The basic charge-one instanton on Euclidean four-space has a scale parameter. At large scale it is spread out; at small scale its curvature is concentrated near a single center. Its density has the shape of a fourth power of the scale divided by a fourth power of radius squared plus scale squared, up to normalization. The integral stays constant as the scale changes.

Take the scale toward zero. On any region that stays away from the center, the curvature tends to zero. Yet the full Yang-Mills energy never tends to zero. Its mass has become concentrated at the center. This is why convergence away from a finite set can coexist with an energy defect.

## Curvature is tied to topology

For an anti-self-dual connection on a suitable rank-two bundle with structure group SU two, the Yang-Mills energy is related to the second Chern number, an integer usually called instanton charge. With a standard normalization, the charge-one anti-self-dual instanton has energy eight pi squared.

Consequently the concentrated defect cannot be an arbitrary tiny amount of energy. Each nontrivial instanton bubble carries a positive integer unit of topological charge in the conventional setting. When a sequence has total charge k, the smooth limiting connection may have charge smaller than k. The lost difference is accounted for by instanton bubbles at the concentration points.

For example, a sequence of charge-two instantons can converge away from one point to a charge-one instanton, while one unit of charge concentrates into a bubble. The limiting smooth connection by itself no longer describes the same bundle topological class as the original sequence. The bubble data restores the missing integer.

Do not confuse this energy accounting with a general theorem that arbitrary curvature measures are sums of point masses. The clean quantized bubbling statement uses special equations, topological normalization, and compactness hypotheses. Anti-self-duality is an important reason the concentration set is so controlled.

## Zooming in reveals another instanton

To understand what disappeared, zoom in near a concentration point using the scale at which curvature becomes large. The rescaled connections can approach a nontrivial finite-energy anti-self-dual connection on Euclidean four-space. Compactifying the space by adding a point at infinity relates it to an instanton on the four-sphere.

In this sense the bubble is not destroyed. It has moved to a different scale. The original manifold sees a point of concentration, while the rescaled picture sees a full smooth instanton. This gives a striking physical metaphor: energy escapes in scale, not in space.

There can be more than one bubble at a given spatial point, occurring at successively smaller scales. The complete description is then a bubble tree. Each level has its own limiting connection and energy. The total charge is the sum of the charge of the background limit and of all bubbles, provided the sequence satisfies the necessary energy identity.

## Filling a puncture

After we remove the concentration points, the limiting connection is smooth on the punctured manifold. It is natural to ask whether a puncture represents a genuine geometric singularity. Uhlenbeck's removable-singularity theorem says that an anti-self-dual connection with finite energy on a punctured four-ball can, after a suitable gauge transformation, extend smoothly across the missing point.

The extension may live on a bundle with different global topology from the original sequence. That qualification is crucial. Removable singularity does not mean the original concentration event was imaginary. It means the smooth background limit extends, while its missing charge is separately recorded by bubbles.

## Why compactification changes counting problems

Instanton moduli spaces are rarely compact as ordinary smooth spaces. Families can degenerate by shrinking instantons, so naive counting or intersection operations may fail to have compact domains. Uhlenbeck compactification adds ideal instantons: a smooth background connection together with a finite collection of concentration points carrying multiplicities.

This compactification underlies major constructions in four-manifold topology, including Donaldson theory. It supplies a controlled boundary for moduli spaces and makes it possible to ask which intersections or cobordisms are well behaved. The boundary is not merely a technical patch. It expresses the topology and analysis of degenerating gauge fields.

The main lesson is a refined meaning of conservation. A bounded sequence can fail to converge as a smooth global field. But after gauge fixing, rescaling and recording bubble charges, its energy and topology remain intelligible. Uhlenbeck compactness tells us not just where convergence breaks, but what geometry is hiding at the broken scale.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Yang-Mills Energy and Instanton Charge: Why Four Dimensions Matter

**Track:** Topology and Geometry. **Background:** connections and curvature, self-dual two-forms, characteristic classes, Riemannian Hodge star. **Central question:** why does an anti-self-dual connection minimize curvature energy inside a topological class, and why is the dimension four critical?

#### Mathematical companion (not spoken)

Let \(P\to X^4\) be an SU(2)-bundle with anti-Hermitian matrix-valued curvature \(F_A\), and use \(|F|^2\mathrm{vol}=-\operatorname{tr}(F\wedge *F)\). With the standard Chern-Weil normalization, choose
\[k=c_2(P)[X]=\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A).\]
Write \(F=F^++F^-\), \(*F^\pm=\pm F^\pm\). Then
\[E(A)=\int_X|F|^2=\|F^+\|_2^2+\|F^-\|_2^2,\qquad 8\pi^2k=\|F^-\|_2^2-\|F^+\|_2^2.\]
Thus \(E(A)\ge8\pi^2|k|\). If \(k\ge0\), equality holds iff \(F^+=0\), and if \(k\le0\), equality holds iff \(F^-=0\). This sign convention is consistent with the ASD index formula in 030800. Under dilation in dimension \(n\), \(F\) scales as \(\ell^{-2}\), so \(\int|F|^2\) scales as \(\ell^{n-4}\). In dimension four it is scale invariant.

##### Exercises with answers

1. **Split.** If \(F^+=0\), what is \(E(A)\) for charge \(k>0\) in the stated convention? **Answer:** \(8\pi^2k\).
2. **Orientation.** What happens to self-duality when orientation reverses? **Answer:** self-dual and anti-self-dual components exchange.
3. **Scaling.** Why is four the critical dimension for Yang-Mills energy? **Answer:** the scaling exponent \(n-4\) vanishes.
4. **Limit.** Does a constant energy bound imply smooth convergence of a shrinking instanton family? **Answer:** no; energy can concentrate in a shrinking region.

##### Sources and further reading

- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), Yang-Mills energy and compactness.
- Karen Uhlenbeck, [Connections with L-p bounds on curvature](https://doi.org/10.1007/BF01947069).
- Overviews: [Yang-Mills theory](https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_theory), [BPST instanton](https://en.wikipedia.org/wiki/BPST_instanton), [Self-dual two-form](https://en.wikipedia.org/wiki/Self-dual_two-form).

### Small-Energy Gauges and Compactness: The Local Uhlenbeck Estimate

**Track:** Topology and Geometry. **Background:** Sobolev spaces, Coulomb gauge, elliptic estimates, Yang-Mills curvature energy. **Central question:** how can bounded curvature control a connection when the connection form itself can be arbitrarily large in a bad gauge?

#### Mathematical companion (not spoken)

For a connection \(A=d+a\) on a bundle trivialized over a four-ball \(B\), Uhlenbeck's small-energy gauge theorem has the schematic form: if \(\|F_A\|_{L^2(B)}<\varepsilon\) (with appropriate geometric and bundle hypotheses), there is a gauge such that
\[d^*a=0,\qquad a\cdot\nu|_{\partial B}=0,\qquad \|a\|_{W^{1,2}(B)}\le C\|F_A\|_{L^2(B)}.\]
Local gauge conventions, boundary formulations, and exact function spaces vary among statements. The mechanism uses \(F_A=da+a\wedge a\), a first-order elliptic estimate for \(d+d^*\), and \(\|a\wedge a\|_{L^2}\lesssim\|a\|_{L^4}^2\lesssim\|a\|_{W^{1,2}}^2\). The nonlinear inequality requires a small-energy argument; it is not a global linear estimate for arbitrary \(a\).

For an energy-bounded ASD sequence \(A_j\) over a fixed closed oriented four-manifold, the standard compactness framework obtains local gauge convergence away from a finite concentration set, followed by elliptic bootstrapping for solutions. The supercritical \(L^p\) compactness theorem for \(p>n/2\) is distinct from the critical \(p=n/2=2\) bubbling regime. Do not infer uniform global Coulomb gauges or smooth convergence from an \(L^2\) energy bound alone.

##### Exercises with answers

1. **Flat gauge.** Can a flat connection have a large local connection one-form? **Answer:** yes, after a rapidly varying gauge transformation.
2. **Smallness.** Which scale-critical curvature norm appears in four-dimensional local gauge fixing? **Answer:** \(L^2\).
3. **Quadratic term.** Why is \(a\wedge a\) in \(L^2\) when \(a\in W^{1,2}\)? **Answer:** \(W^{1,2}\hookrightarrow L^4\) and \(L^4\cdot L^4\subset L^2\).
4. **Conclusion.** Does bounded energy alone give globally smooth convergence modulo gauge? **Answer:** no; energy concentration may obstruct it.

##### Sources and further reading

- Karen Uhlenbeck, [Connections with L-p bounds on curvature](https://doi.org/10.1007/BF01947069), *Communications in Mathematical Physics* 83 (1982), 31-42.
- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), chapters on compactness and Sobolev gauge transformations.
- Overviews: [Uhlenbeck compactness theorem](https://en.wikipedia.org/wiki/Uhlenbeck%27s_compactness_theorem), [Gauge fixing](https://en.wikipedia.org/wiki/Gauge_fixing).

### Bubbling and Removable Singularities: Where Instanton Energy Goes

**Track:** Topology and Geometry. **Background:** self-dual curvature, Yang-Mills energy, critical Sobolev estimates, local Uhlenbeck gauges. **Central question:** how can instantons have a convergent limit away from points while retaining a fixed total topological charge?

#### Mathematical companion (not spoken)

For an ASD SU(2) sequence \(A_j\) of fixed topological charge \(k\) over a closed oriented four-manifold, after passing to a subsequence and gauges there is a finite singular set \(\{x_1,\dots,x_m\}\), a smooth ASD connection \(A_\infty\) on a possibly lower-charge bundle, and positive integers \(k_\ell\), such that under standard Uhlenbeck compactness and energy identity conclusions,
\[|F_{A_j}|^2\,d\mathrm{vol}\ \rightharpoonup\ |F_{A_\infty}|^2\,d\mathrm{vol}+8\pi^2\sum_{\ell=1}^m k_\ell\,\delta_{x_\ell},\qquad k=c_2(P_\infty)[X]+\sum_{\ell=1}^m k_\ell.\]
Multiple nested scales at one point require a bubble-tree analysis; the aggregate point mass may contain several bubbles. The numbers shown use the standard matrix-trace and orientation convention of 034100. On a round \(S^4\), charge-one BPST instantons with scale \(\rho_j\to0\) give \(|F_{A_j}|^2\,dx\rightharpoonup8\pi^2\delta_0\) on a stereographic chart while the unrescaled limit is flat away from the center.

Uhlenbeck's removable-singularity theorem applies to finite-energy four-dimensional Yang-Mills connections on punctured balls, up to gauge and the appropriate extension of bundle data. It does not assert that any finite-energy distributional connection, or any arbitrary sequence, extends smoothly without using its equation.

##### Exercises with answers

1. **Energy packet.** Under the specified ASD SU(2) convention, how much energy can a charge-two bubble carry? **Answer:** \(16\pi^2\).
2. **Bookkeeping.** If the original charge is four and the limit has charge one, what is the sum of bubble charges? **Answer:** three.
3. **Removability.** Does a removable-singularity theorem force an entire sequence to converge smoothly at a concentration point? **Answer:** no; it concerns the individual rescaled or punctured limiting solution.
4. **Dimension.** Why can bubble scales shrink without increasing energy in dimension four? **Answer:** \(\int|F|^2\) is scale invariant in four dimensions.

##### Sources and further reading

- Karen Uhlenbeck, [Removable singularities in Yang-Mills fields](https://doi.org/10.1007/BF01947068), *Communications in Mathematical Physics* 83 (1982), 11-29.
- Karen Uhlenbeck, [Connections with L-p bounds on curvature](https://doi.org/10.1007/BF01947069), *Communications in Mathematical Physics* 83 (1982), 31-42.
- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), compactness chapter.
- Overviews: [Uhlenbeck compactness theorem](https://en.wikipedia.org/wiki/Uhlenbeck%27s_compactness_theorem), [BPST instanton](https://en.wikipedia.org/wiki/BPST_instanton).

### Uhlenbeck Compactness: Where Instanton Energy Goes

**Track:** Topology and Geometry. **Background:** connections on bundles, curvature, Yang-Mills energy, four-dimensional geometry, and anti-self-duality. **Central question:** how can a sequence of smooth gauge fields fail to converge while preserving a precise accounting of its lost energy?

#### Mathematical companion (not spoken)

Let X be a closed oriented Riemannian four-manifold, P an SU(2) bundle, and A_n a sequence of smooth anti-self-dual connections with fixed `c_2(P)=k`. With the convention `YM(A)=int_X |F_A|^2 dvol` and the standard trace pairing, ASD implies
\[
 YM(A_n)=8\pi^2k.
\]
Uhlenbeck compactness: after a subsequence and gauge transformations on compact subsets of `X\setminus {x_1,...,x_r}`, the connections converge smoothly to a limiting ASD connection on a (possibly different) bundle. Under the usual compactness and no-energy-loss theorem,
\[
 k=k_\infty+\sum_{j=1}^r m_j,\qquad m_j\in\mathbb N.
\]
Concentrated energy measures have masses `8 pi^2 m_j` for this normalization. There may be bubble trees with several scales at one point. Finite-energy ASD connections extend across an isolated puncture after gauge transformation (removable singularity theorem).

Scale calculation in dimension four: `|F_rho|^2` scales like `rho^(-4)` while `dx` scales like `rho^4`, leaving YM energy invariant. For a BPST-type charge-one instanton, the curvature density is proportional to `rho^4/(|x|^2+rho^2)^4`. Do not generalize the finite-point concentration theorem to arbitrary L2-bounded connections without ASD/Yang-Mills control.

##### Exercises with answers

1. Why is four the critical dimension for the L2 norm of curvature? **Answer:** curvature scales as length to the minus two, so its square and four-dimensional volume have cancelling powers.
2. If k=3 and the limiting background has charge one, what can the total bubble charge be? **Answer:** two.
3. Why is a gauge transformation needed before taking limits of connection forms? **Answer:** gauge-equivalent connections can have arbitrarily different local representatives.
4. Does removal of a point singularity restore the original topological bundle? **Answer:** not necessarily; bubble charges may account for lost second Chern class.

##### Reading and source notes

- [Donaldson and Kronheimer, The Geometry of Four-Manifolds](https://doi.org/10.1093/oso/9780198535539.001.0001), gauge fixing, compactification and instanton geometry.
- [Uhlenbeck, Connections with Lp Bounds on Curvature](https://doi.org/10.1007/BF01947069), gauge-theoretic compactness and control from curvature.
- [Uhlenbeck, Removable Singularities in Yang-Mills Fields](https://doi.org/10.1007/BF01947068), extension across finite-energy isolated singularities.
