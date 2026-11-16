# 041000 — Seiberg–Witten Monopoles and Smooth Four-Manifolds

**Track:** Topology and Geometry. **Background:** differential geometry, bundles, Dirac operators, and characteristic classes. **Central question:** how can a nonlinear equation involving a spinor distinguish smooth structures on four-dimensional spaces?

<!-- BEGIN SPOKEN LECTURE -->

# Four dimensions are a difficult meeting place

Classifying a surface topologically is a tractable problem. Genus tells us much of what we need. Four-dimensional manifolds behave differently. Their topology, differentiable structure, and geometry interact in ways that cannot be reduced to a single Euler characteristic or intersection form.

Gauge theory provided new tools for this difficulty. Donaldson's theory studies connections whose curvature is anti-self-dual. Seiberg–Witten theory instead couples an abelian connection to a spinor, a field that transforms under a spin representation. The equations are nonlinear, but their moduli spaces are often more compact and manageable than the corresponding spaces of nonabelian instantons.

The reward is a numerical invariant that can remain unchanged while one changes the metric used to define the equations. It is then an invariant of the smooth four-manifold together with additional topological data and orientation choices.

# The ingredients of a monopole

Begin with a closed oriented smooth four-manifold. Choose a spin-c structure, which supplies two bundles of spinors, commonly called positive and negative spinors, and a determinant line bundle. A unitary connection on that line bundle defines a Dirac operator taking positive spinors to negative ones.

A Seiberg–Witten solution consists of a connection and a positive spinor obeying two linked equations. First, the Dirac operator annihilates the spinor. Second, the self-dual part of the connection's curvature equals a quadratic expression in the spinor, possibly with a prescribed perturbation.

Why self-duality? In four dimensions the Hodge star splits two-forms into two eigenspaces, positive and negative. That splitting exists for an oriented metric, and it lets the curvature equation select one half of the available two-form data.

Gauge transformations alter the local description of the connection and spinor without altering their physical or geometric class. Thus the object of study is not the raw solution set but the quotient by gauge transformations: a moduli space.

# Counting solutions after understanding dimension

The expected dimension of this moduli space is governed by topological quantities. It uses the square of the first Chern class of the determinant line, the Euler characteristic, and the signature of the four-manifold. When the expected dimension is zero and perturbations produce a regular compact moduli space with no reducible complications, signed counting of solutions can define an integer invariant.

There are several qualifications in that sentence. The count depends on an orientation. Reducible solutions require care. When the dimension of the positive part of second cohomology is one, chamber choices can matter. When it is larger than one, a better metric-independence statement is available under the standard conditions.

This is why Seiberg–Witten invariants are not merely counts of whatever a numerical solver happens to find. They arise after geometric analysis establishes compactness, transversality, and control of the gauge quotient.

# A check on a K3 surface

A K3 surface supplies a useful exact calculation. Its Euler characteristic is twenty-four and its signature is negative sixteen. Twice the Euler characteristic plus three times the signature is forty-eight minus forty-eight, which is zero.

For the spin-c structure with trivial determinant line, the first Chern class is zero. Its square is zero too. Therefore the expected Seiberg–Witten dimension is zero.

That dimension calculation does not alone count the monopoles. But it explains why the corresponding invariant is numerical rather than a higher-degree class. In the standard orientation and appropriate chamber-independent setting, the zero basic class of a K3 surface has a nonzero Seiberg–Witten invariant.

This is a powerful pattern in geometry. A characteristic number predicts how many degrees of freedom a solution space ought to have; analysis turns that prediction into a moduli problem; topology extracts a deformation-invariant answer.

# What the invariant can and cannot distinguish

Seiberg–Witten invariants have proved useful for detecting smooth phenomena invisible to coarser topological data. They yield genus bounds for embedded surfaces and restrictions on the existence of certain geometric structures. Their relationship to symplectic geometry is especially strong through Taubes's results connecting Seiberg–Witten and pseudoholomorphic-curve counts.

Yet the invariant is not a complete classifier of smooth four-manifolds. Different manifolds may have identical Seiberg–Witten data, and vanishing of an invariant does not imply that the manifold is geometrically trivial. The choice of spin-c structure and the hypotheses for metric independence have to be retained.

# A nonlinear route to topology

The surprising step is to use a field equation as a measuring instrument for smooth structure. We choose a metric to write a Dirac equation and a curvature equation. Then, under controlled conditions, the resulting signed count no longer depends on that metric. What began as analytic data becomes a smooth-topological invariant.

Four-dimensional topology is full of such transitions: a connection encodes curvature, a spinor constrains it, the gauge group identifies redundant descriptions, and a moduli space yields an invariant. Seiberg–Witten theory demonstrates that a nonlinear equation can tell us something about the space on which it is posed, rather than merely about a field moving through that space.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `X` be a smooth closed oriented Riemannian four-manifold with spin-c structure `\mathfrak s`, determinant line `L`, and spinor bundles `W^\pm`. For a unitary connection `A` on `L` and `\psi\in\Gamma(W^+)`, the (schematic, convention-dependent) Seiberg–Witten equations are
\[
D_A\psi=0,\qquad F_A^+=q(\psi)+i\eta,
\]
where `q` is a trace-free quadratic form with appropriate normalization and `\eta` is a self-dual perturbation. Divide the solution space by `\mathrm{Map}(X,S^1)`. The virtual dimension is
\[
d(\mathfrak s)=\frac{c_1(L)^2-(2\chi(X)+3\sigma(X))}{4}.
\]
For K3, `\chi=24`, `\sigma=-16`, `2\chi+3\sigma=0`. For `c_1(L)=0`, `d=0`. K3 has `b_2^+=3`, so it lies in the chamber-independent regime of the standard integer-valued invariant (subject to orientations and regularity conventions).

The comparison with Donaldson invariants requires careful handling of `b_2^+`, reducibles, orientation, perturbation, and compactness; the standard Seiberg–Witten equations are `U(1)` rather than `SU(2)` gauge equations.

### Exercises with answers

1. Compute `2\chi+3\sigma` for K3. **Answer:** `2(24)+3(-16)=0`.
2. What is the expected dimension for a determinant line with `c_1^2=8` on a manifold with `2\chi+3\sigma=0`? **Answer:** `2`.
3. Why divide solutions by gauge transformations? **Answer:** gauge-related fields represent the same geometric configuration.
4. Does expected dimension zero by itself establish an integer invariant? **Answer:** No; regularity, compactness, orientations, and reducibles require analysis.

### Reading and source notes

- [Edward Witten, Monopoles and Four-Manifolds](https://arxiv.org/abs/hep-th/9411102), original Seiberg–Witten perspective on smooth topology.
- [Taubes, The Seiberg–Witten Invariants and Symplectic Forms](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/1994/0001/0006/MRL-1994-0001-0006-a015.pdf), connections to symplectic structures and pseudoholomorphic curves.
