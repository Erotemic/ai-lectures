# 029000 — Quantization and Symplectic Reduction: Which Operation Comes First?

**Track:** Topology and Geometry. **Background:** symplectic manifolds, moment maps, line bundles, and group representations. **Central question:** when does taking quantum states and imposing symmetry agree with reducing the classical phase space first?

<!-- BEGIN SPOKEN LECTURE -->

# Two ways to remove a symmetry

Suppose a mechanical system has a symmetry. We can use that symmetry classically to reduce the number of variables before studying the motion. Or we can first quantize the system and then retain only quantum states that transform in a specified way under the symmetry group.

Do those procedures give the same answer? This is the question behind the phrase quantization commutes with reduction. It is easy to say and surprisingly rich in mathematical content.

We will work with a compact sphere understood as the complex projective line. The sphere carries a rotational circle action. Its quantum states form an explicit finite-dimensional representation. The classical reduced spaces at regular moment-map values are points. We can check that the weight multiplicities in the quantum representation match the dimensions obtained by quantizing these reduced points.

# Classical reduction

A symplectic manifold is an even-dimensional space equipped with a closed nondegenerate two-form. A Hamiltonian circle action comes with a moment map, a real-valued function whose derivative is related to the vector field generating the circle action by contraction with the symplectic form.

Fix a value of that moment map. The level set consists of classical states having the selected conserved quantity. Under regularity and freeness hypotheses, we can divide this level set by the circle action. The quotient inherits a symplectic form and is called the reduced phase space.

The key point is that this is not merely taking the orbit space of the entire manifold. We first restrict to a level set of a conserved quantity and only then quotient by the symmetry. The dimension typically drops by twice the dimension of the group.

For a sphere with the usual axial circle rotation, a regular interior level set is a latitude circle. Quotienting by the rotation collapses that latitude circle to one point. At the north and south poles the symmetry has fixed points, so the endpoint levels are singular in the regular-value sense.

# Quantization of the sphere

Regard the sphere as the complex projective line and choose a prequantum line bundle of positive integral degree n. In a holomorphic polarization, the quantum space is the vector space of holomorphic sections of that line bundle. It has dimension n plus one.

We can write those sections explicitly as homogeneous polynomials of degree n in two coordinates. There are n plus one monomials: the first coordinate to the power zero, one, two, and so on up to n, multiplied by the appropriate power of the second coordinate.

The circle action acts on this space by scaling each monomial. With a fixed consistent choice of convention and equivariant lift, the weights are the integers from zero through n. Every weight occurs with multiplicity one.

So the quantum space has one state at each integral weight between the endpoints of the moment-map image. This is the simplest setting in which a geometric object produces a representation whose weight diagram looks like the classical moment interval.

# Compare the two constructions

Choose an interior integral weight, say k with k strictly between zero and n. On the quantum side, take the states with weight k. That space is one-dimensional because exactly one monomial has that weight.

On the classical side, reduce the sphere at the moment-map value corresponding to k. The regular level set is a circle, and after division by the circle action the reduced space is a point. The prequantum line bundle descends with the appropriate weight shift. Quantization of that point gives one complex degree of freedom.

Both procedures give dimension one. This is not a numerical coincidence. The general theorem states, under suitable geometric and representation-theoretic hypotheses, that multiplicities of quantum representations are computed by quantization of symplectic quotients.

For a nonabelian compact group, we typically look at an invariant subspace or an isotypic component associated with an irreducible representation. The corresponding reduced space can be constructed at a suitable coadjoint orbit or moment-map value, with conventions that must be tracked carefully.

# Why integrality matters

The prequantum line bundle only exists when the symplectic class obeys the appropriate integrality condition. The integer n in the sphere example is not an arbitrary discretization chosen after the fact. It measures the line bundle's first Chern number and controls both the total number of sections and the available weights.

A regular reduced space can inherit a quantization line bundle when the original geometric data and the chosen weight are compatible. If we shift the equivariant linearization, all the weights shift. If we include half-form or metaplectic corrections, the spaces and formulas can shift as well. An assertion that quantization commutes with reduction must specify which quantization construction is being used.

# What can go wrong

The clean example is compact, holomorphic, and regular at the chosen interior values. Many other settings are harder. A moment-map level can be singular. A group action may have stabilizers. The reduced space may be an orbifold or a stratified space rather than a smooth manifold. If the original manifold is noncompact, the quantum space may be infinite-dimensional and analytic conditions become essential.

There are powerful extensions of the theorem to some of these situations. But the statement is not automatically true for every possible notion of quantization or every quotient. One must check the conditions under which the comparison map is defined and invertible.

# A relationship between geometry and representation theory

The sphere calculation makes a general principle visible. Classical reduction selects a value of a conserved quantity and removes the corresponding symmetry direction. Quantum reduction selects a weight space in a representation. The moment map connects the two operations.

At integral regular values, quantization of a latitude quotient and selection of a monomial weight space agree. More generally, the topology of symplectic quotients and the multiplicities of representations are two sides of a single geometric construction. That is why symplectic geometry can answer questions about representation theory, and why representation theory can encode surprisingly detailed information about classical phase spaces.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a Hamiltonian action of a compact group G on a symplectic manifold (M,omega), with moment map `mu:M->g*`, the regular reduction at zero is `M//G=mu^-1(0)/G`, assuming zero is regular and the action on that level set is free (or allowing orbifold variants for finite isotropy). The reduced symplectic form is defined by pullback to the level set. Under compatible compact Kähler, prequantum and regularity hypotheses, quantization may satisfy `Q(M)^G ~= Q(M//G)`; at a nonzero integral weight, use the shifted character or shifting trick.

**Sphere example.** Let `M=CP^1` with prequantum line `L=O(n)`, `n>=2`, and a Hamiltonian circle action scaled so its moment image is `[0,n]`. With an appropriate lift and sign convention the holomorphic quantization has weight decomposition
\[
Q(M)=H^0(CP^1,O(n))\simeq\bigoplus_{k=0}^n \mathbb C_k,
\quad \dim Q(M)=n+1.
\]
Here C_k denotes the weight-k representation. For interior integer `0<k<n`, the reduced space `mu^-1(k)/S^1` is a point (regular free case), whose quantization is one-dimensional, matching `dim Q(M)_k=1`.

Conventions: prequantum curvature, signs for the moment map, torus action on the dual bundle and possible metaplectic correction can shift or reverse weights. Endpoint levels are fixed points and not regular; their treatment requires an appropriate singular-reduction framework. The dimension comparison is not an unconditional theorem for arbitrary noncompact or singular actions.

### Exercises with answers

1. How many holomorphic sections does O(5) have on CP^1? **Answer:** six.
2. At an interior regular level of the standard circle moment map on CP^1, what is the reduced space? **Answer:** a single point.
3. If the quantization contains exactly one copy of weight two, what is the multiplicity of that character? **Answer:** one.
4. Why should we not apply the regular-value argument unchanged at a fixed pole? **Answer:** the pole is a critical level of the moment map and the action is not free there.

### Reading and source notes

- [Guillemin–Sternberg theorem exposition, Hochs](https://www.math.ru.nl/~hochs/momentum_new.pdf), regular symplectic reduction and invariant quantum spaces.
- [University of Chicago, Quantization Commutes with Reduction](https://math.uchicago.edu/~may/REU2020/REUPapers/Ren%2CQiuyu.pdf), compact Kähler setting and a proof under stated freeness hypotheses.
- [Hall and Kirwin, Unitarity in Quantization Commutes with Reduction](https://arxiv.org/abs/math/0610005), distinctions involving inner products and metaplectic correction.
