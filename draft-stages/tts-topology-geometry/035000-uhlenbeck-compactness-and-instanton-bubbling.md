# 035000 - Uhlenbeck Compactness: Where Instanton Energy Goes

**Track:** Topology and Geometry. **Background:** connections on bundles, curvature, Yang-Mills energy, four-dimensional geometry, and anti-self-duality. **Central question:** how can a sequence of smooth gauge fields fail to converge while preserving a precise accounting of its lost energy?

<!-- BEGIN SPOKEN LECTURE -->

# Smooth fields that develop a point of infinite concentration

Imagine a sequence of smooth connections on a four-dimensional manifold. Each connection has finite Yang-Mills energy. Every connection obeys the same anti-self-duality equation. One might expect that a uniform energy bound would force a convergent subsequence, so that a family of instantons could never run away to a singular configuration.

That expectation is almost right, but one subtle form of escape remains. A lump of curvature can become narrower and narrower while keeping a fixed amount of total energy. In the limit, the lump shrinks to a point. Away from that point, the connections behave regularly after a suitable change of gauge. At the point, energy has concentrated on a scale the limiting smooth field cannot see.

Uhlenbeck compactness makes this precise. It does not say that every bounded sequence of connections converges smoothly everywhere. It says that, under appropriate four-dimensional anti-self-dual or Yang-Mills hypotheses, we can choose gauges and extract a convergent subsequence away from finitely many concentration points. The missing curvature has a quantized accounting, and the punctures can often be filled by extending the limiting connection on a possibly different bundle.

# Gauge freedom complicates ordinary convergence

A connection is a way of differentiating sections of a vector bundle. The same geometric connection can be represented by very different local matrix-valued one-forms after a gauge transformation. Therefore direct convergence of matrix coefficients is not a gauge-invariant question.

Before applying compactness, we need to choose gauges in which the connection forms satisfy useful analytic estimates. Locally, Uhlenbeck's gauge-fixing theorem says that sufficiently small curvature energy on a ball can be used to put the connection in a controlled Coulomb gauge. Roughly, the divergence of the gauge potential is set to zero, and the potential is bounded by the curvature.

This is the first stage of the argument. If the curvature energy is small on a ball, one gains a gauge in which elliptic estimates become available. If the energy is not small, that ball may contain a concentration point. A global gauge on the original bundle need not exist, so the analysis is necessarily local and patched together.

# Why four dimensions are critical

Curvature is a two-form. Under rescaling of spatial coordinates by a factor rho, its pointwise magnitude changes like rho to the minus two. The volume of a four-dimensional region changes like rho to the fourth. Therefore the integral of the squared curvature is scale invariant in four dimensions.

This exact balance is the reason a curvature lump can shrink without losing its energy. In lower dimensions, the same scaling favors one behavior; in higher dimensions, a different analytic regime appears. Four-dimensional Yang-Mills energy is critical for rescaling.

An explicit family illustrates the phenomenon. The basic charge-one instanton on Euclidean four-space has a scale parameter. At large scale it is spread out; at small scale its curvature is concentrated near a single center. Its density has the shape of a fourth power of the scale divided by a fourth power of radius squared plus scale squared, up to normalization. The integral stays constant as the scale changes.

Take the scale toward zero. On any region that stays away from the center, the curvature tends to zero. Yet the full Yang-Mills energy never tends to zero. Its mass has become concentrated at the center. This is why convergence away from a finite set can coexist with an energy defect.

# Curvature is tied to topology

For an anti-self-dual connection on a suitable rank-two bundle with structure group SU two, the Yang-Mills energy is related to the second Chern number, an integer usually called instanton charge. With a standard normalization, the charge-one anti-self-dual instanton has energy eight pi squared.

Consequently the concentrated defect cannot be an arbitrary tiny amount of energy. Each nontrivial instanton bubble carries a positive integer unit of topological charge in the conventional setting. When a sequence has total charge k, the smooth limiting connection may have charge smaller than k. The lost difference is accounted for by instanton bubbles at the concentration points.

For example, a sequence of charge-two instantons can converge away from one point to a charge-one instanton, while one unit of charge concentrates into a bubble. The limiting smooth connection by itself no longer describes the same bundle topological class as the original sequence. The bubble data restores the missing integer.

Do not confuse this energy accounting with a general theorem that arbitrary curvature measures are sums of point masses. The clean quantized bubbling statement uses special equations, topological normalization, and compactness hypotheses. Anti-self-duality is an important reason the concentration set is so controlled.

# Zooming in reveals another instanton

To understand what disappeared, zoom in near a concentration point using the scale at which curvature becomes large. The rescaled connections can approach a nontrivial finite-energy anti-self-dual connection on Euclidean four-space. Compactifying the space by adding a point at infinity relates it to an instanton on the four-sphere.

In this sense the bubble is not destroyed. It has moved to a different scale. The original manifold sees a point of concentration, while the rescaled picture sees a full smooth instanton. This gives a striking physical metaphor: energy escapes in scale, not in space.

There can be more than one bubble at a given spatial point, occurring at successively smaller scales. The complete description is then a bubble tree. Each level has its own limiting connection and energy. The total charge is the sum of the charge of the background limit and of all bubbles, provided the sequence satisfies the necessary energy identity.

# Filling a puncture

After we remove the concentration points, the limiting connection is smooth on the punctured manifold. It is natural to ask whether a puncture represents a genuine geometric singularity. Uhlenbeck's removable-singularity theorem says that an anti-self-dual connection with finite energy on a punctured four-ball can, after a suitable gauge transformation, extend smoothly across the missing point.

The extension may live on a bundle with different global topology from the original sequence. That qualification is crucial. Removable singularity does not mean the original concentration event was imaginary. It means the smooth background limit extends, while its missing charge is separately recorded by bubbles.

# Why compactification changes counting problems

Instanton moduli spaces are rarely compact as ordinary smooth spaces. Families can degenerate by shrinking instantons, so naive counting or intersection operations may fail to have compact domains. Uhlenbeck compactification adds ideal instantons: a smooth background connection together with a finite collection of concentration points carrying multiplicities.

This compactification underlies major constructions in four-manifold topology, including Donaldson theory. It supplies a controlled boundary for moduli spaces and makes it possible to ask which intersections or cobordisms are well behaved. The boundary is not merely a technical patch. It expresses the topology and analysis of degenerating gauge fields.

The main lesson is a refined meaning of conservation. A bounded sequence can fail to converge as a smooth global field. But after gauge fixing, rescaling and recording bubble charges, its energy and topology remain intelligible. Uhlenbeck compactness tells us not just where convergence breaks, but what geometry is hiding at the broken scale.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Why is four the critical dimension for the L2 norm of curvature? **Answer:** curvature scales as length to the minus two, so its square and four-dimensional volume have cancelling powers.
2. If k=3 and the limiting background has charge one, what can the total bubble charge be? **Answer:** two.
3. Why is a gauge transformation needed before taking limits of connection forms? **Answer:** gauge-equivalent connections can have arbitrarily different local representatives.
4. Does removal of a point singularity restore the original topological bundle? **Answer:** not necessarily; bubble charges may account for lost second Chern class.

### Reading and source notes

- [Donaldson and Kronheimer, The Geometry of Four-Manifolds](https://doi.org/10.1093/oso/9780198535539.001.0001), gauge fixing, compactification and instanton geometry.
- [Uhlenbeck, Connections with Lp Bounds on Curvature](https://doi.org/10.1007/BF01947069), gauge-theoretic compactness and control from curvature.
- [Uhlenbeck, Removable Singularities in Yang-Mills Fields](https://doi.org/10.1007/BF01947068), extension across finite-energy isolated singularities.
