# 034000 — Symplectic Nonsqueezing: A Constraint That Volume Cannot See

**Track:** Topology and Geometry. **Background:** symplectic forms, Hamiltonian flows, volume, and embeddings. **Central question:** why can't a symplectic map squeeze a ball into an arbitrarily thin symplectic cylinder, even when the cylinder has infinite volume?

<!-- BEGIN SPOKEN LECTURE -->

# Volume seems to permit the impossible

Imagine a ball in four-dimensional phase space. We are allowed to deform it by smooth transformations that preserve the symplectic form. Such transformations preserve the associated volume. One might therefore guess that every rearrangement compatible with volume is possible. If a target region has more than enough volume, why should the ball fail to fit?

Now choose a target shaped like a cylinder. In one position-momentum coordinate pair, the cylinder is a disk of radius R. In every other pair, it extends without bound. Its total volume is infinite. No ordinary volume argument can prevent a finite ball of radius r from fitting inside it, regardless of how small R is.

Gromov's nonsqueezing theorem says something much stronger than volume preservation. A symplectic embedding of the ball into this cylinder exists only when the ball radius is no larger than the cylinder radius. A ball with radius two cannot be squeezed through a symplectic cylinder of radius one, even though the cylinder is unbounded in all other directions.

This is a genuinely multidimensional obstruction. In a single position-momentum plane, area preservation already supplies the relevant bound. In four or more dimensions, a two-dimensional area restriction survives despite all the additional directions into which volume might be redistributed.

# The cylinder must use a conjugate pair

The statement is precise about which coordinates form the narrow disk. The disk is measured in one conjugate pair, such as a position coordinate q one and its matching momentum coordinate p one. The standard symplectic form is the sum of each dq wedged with its corresponding dp.

Why does that pairing matter? A symplectic linear map can shrink a position coordinate if it expands its conjugate momentum by the reciprocal factor. The product of the two scale factors remains one, preserving the two-form in that pair.

Thus ordinary narrowing in position space is perfectly possible. A linear map sending q to a small multiple of q and p to the reciprocal large multiple of p is symplectic. It turns a disk into a long ellipse of the same area. But the ellipse cannot lie inside a smaller disk in that conjugate plane. The nonsqueezing theorem says that even elaborate nonlinear symplectic maps cannot evade the underlying obstruction by trading distortion with the other coordinate pairs.

If the target were narrow only in two position coordinates rather than one conjugate position-momentum pair, the simple scaling trick could fit the ball. Symplectic nonsqueezing is not a universal prohibition on making shapes narrow. It is a prohibition on squeezing their symplectic two-dimensional size.

# Why volume is not the whole geometry

Symplectic geometry begins with a closed nondegenerate two-form. In dimension two n, its n-fold wedge product determines a volume form. Every symplectomorphism preserves that volume. The converse is false: volume-preserving maps need not preserve the symplectic form.

So there is more structure to preserve than a single number associated with volume. The surprising part of Gromov's theorem is that preserving a two-form pointwise implies a global embedding obstruction. Local linear algebra alone does not prove the nonlinear statement.

An intuitive strategy for understanding the theorem uses holomorphic curves. Choose an almost complex structure compatible with the symplectic form. Certain pseudoholomorphic curves carry an energy equal to symplectic area. Their existence and monotonicity properties constrain how a ball may sit inside a cylinder.

Very roughly, one constructs a curve in an appropriate compactification of the cylinder, arranges for it to meet the embedded ball, and compares an upper bound from the cylinder's disk area with a lower bound forced by the ball. The resulting inequality is that pi times r squared cannot exceed pi times R squared. This is a proof strategy, not an elementary derivation from volume alone. The analytic existence and compactness results for those curves are the deep part.

# Capacities assign numbers to symplectic domains

The nonsqueezing theorem motivated the development of symplectic capacities. A capacity assigns a nonnegative size, possibly infinite, to symplectic domains. It must be monotone under symplectic embeddings and scale correctly when the symplectic form is multiplied by a positive factor.

A normalized capacity assigns the same standard value to a ball of radius r and a cylinder of radius r: pi times r squared. These domains have drastically different volumes. The capacity measures the kind of size relevant to symplectic embeddings, not ordinary spatial occupancy.

If a symplectic embedding carried a larger ball into a smaller cylinder, monotonicity of capacity would require its capacity to be no larger than the cylinder's capacity. But that would mean pi times r squared is no larger than pi times R squared. For r greater than R this is impossible.

One capacity, called the Gromov width, is defined by asking for the largest symplectic ball that can embed into a given domain and recording the corresponding area. Other capacities capture additional embedding obstructions. In four dimensions, a sequence of embedded contact homology capacities can distinguish some domains that have the same volume and even similar simpler capacity measurements.

# A worked comparison of two proposed embeddings

Take a four-dimensional ball of radius three and a cylinder whose first conjugate pair lies in a disk of radius two. The cylinder is infinite in the second pair. Despite this infinite volume, no symplectic embedding exists because the ball's capacity is nine pi and the cylinder's normalized capacity is four pi.

Now take a ball of radius one and a cylinder of radius two. There is an obvious embedding: put the ball inside the cylinder without distorting it at all. The theorem asserts no obstruction in that direction; the identity inclusion works.

Notice that the ball radius is a geometric parameter in the standard Euclidean coordinates. Under arbitrary symplectic transformations, ordinary Euclidean radii and lengths are not preserved. The invariant is the capacity, not the radius of a particular image shape.

# Rigidity is compatible with flexibility

Darboux's theorem says every symplectic manifold is locally symplectomorphic to standard phase space. That is a powerful local flexibility statement: symplectic manifolds have no local curvature invariant analogous to the curvature of a Riemannian metric.

Nonsqueezing is a global statement about finite-size embeddings. There is no contradiction between the two. Being able to straighten the symplectic form in a small neighborhood does not mean one can fit a large ball through every thin global region.

The resulting picture is central to modern symplectic topology. Hamiltonian dynamics preserves volume, but also preserves stronger geometric constraints. Holomorphic curves and symplectic capacities reveal those constraints. What looked like a problem of packing volume becomes a problem of preserving the area structure of conjugate coordinate pairs.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On `R^{2n}` let `omega_0=sum_{j=1}^n dq_j wedge dp_j`. Define the open ball `B^{2n}(r)={sum_j(q_j^2+p_j^2)<r^2}` and the symplectic cylinder `Z^{2n}(R)={q_1^2+p_1^2<R^2}`. Gromov's nonsqueezing theorem gives
\[
B^{2n}(r)\stackrel{\mathrm{sympl}}{\hookrightarrow}Z^{2n}(R)
\quad\Longleftrightarrow\quad r\le R.
\]
The easy direction is ordinary inclusion. The difficult implication is proved using pseudoholomorphic-curve methods (not by volume comparison). For n>1, `Vol(Z)=infinity`, but the normalized capacity still satisfies `c(B(r))=pi r^2`, `c(Z(R))=pi R^2`, giving the obstruction.

The linear map `(q_1,p_1)->(a q_1,p_1/a)` preserves `dq_1 wedge dp_1`; it shrinks a q coordinate but not the disk in the conjugate `(q_1,p_1)` plane in both directions. By contrast a target disk in `(q_1,q_2)` is not symplectic, and a map shrinking both q coordinates while expanding both conjugate p coordinates can fit the ball into an arbitrarily small q-only cylinder. This distinction is essential.

### Exercises with answers

1. Can `B^4(2)` symplectically embed into `Z^4(1)`? **Answer:** no, since `2>1`.
2. Does an infinite-volume target imply that a finite symplectic ball can embed? **Answer:** no; capacity can obstruct.
3. Show that `(q,p)->(a q,p/a)` preserves the standard area form. **Answer:** `d(aq) wedge d(p/a)=dq wedge dp` for constant a>0.
4. Is nonsqueezing a consequence of Darboux's theorem alone? **Answer:** no, Darboux is local while nonsqueezing is a global rigidity result.

### Reading and source notes

- [McDuff and Salamon, Introduction to Symplectic Topology: Symplectic capacities](https://academic.oup.com/book/43512/chapter-abstract/364195459), capacities and nonsqueezing.
- [Dusa McDuff, Lectures on Symplectic Topology](https://citeseerx.ist.psu.edu/document?doi=84ffca37956ebaa36ed874299ed20c067b1684e5&repid=rep1&type=pdf), introduction to the pseudoholomorphic-curve proof.
- [Michael Hutchings, Symplectic Weyl Laws (ICM 2026)](https://epubs.siam.org/doi/10.1137/25M1807277), Gromov width and modern capacity invariants.
