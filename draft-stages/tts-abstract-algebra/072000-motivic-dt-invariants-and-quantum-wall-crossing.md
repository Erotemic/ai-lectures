# 072000 - Motivic Donaldson-Thomas Invariants and Quantum Wall Crossing

**Track:** Abstract Algebra. **Background:** stable objects in abelian and derived categories, quiver representations, Donaldson-Thomas invariants, and formal power series. **Central question:** why can a change of stability reorder quantum-dilogarithm factors without changing the total invariant?

<!-- BEGIN SPOKEN LECTURE -->

# Counting objects that change their stability

Suppose we have a category whose objects can be added and extended. A stability condition decides which objects qualify as stable. A small change in the stability parameters can reverse the relative stability of two classes. At the critical wall, an object may break into pieces, or a new extension of those pieces may become stable.

If we count stable objects on one side of the wall and then count on the other, the numbers can differ. The problem is not merely that our count was inaccurate. We changed the rules for which objects contribute. Wall-crossing theory asks for a relation that survives this change.

Motivic Donaldson-Thomas theory answers this in a refined setting. Instead of immediately assigning a number to a moduli problem, it retains geometric information in a ring of motivic classes. In the presence of a three-dimensional Calabi-Yau categorical structure and suitable orientation data, such counts can be assembled into elements of a quantum torus. The surprising outcome is that an ordered product of these elements remains invariant as the stability condition crosses a wall, even though the individual factors can change.

# The smallest model has two building blocks

Begin with two simple objects, call them A and B. Assume there can be a nontrivial extension that puts B inside a new object E, with quotient A. The new object is not just the direct sum of A and B. Its extension class records how the two pieces are glued.

Picture a quiver with two vertices and an arrow between them. A representation assigns vector spaces to the vertices and a linear map to the arrow. Simple representations occupy just one vertex. A representation with one-dimensional spaces at both vertices and a nonzero arrow can be indecomposable. Depending on stability parameters, that indecomposable may be stable, unstable, or strictly semistable.

The wall appears when the phases of the two simple classes align. On one side, an extension of one ordering may count as stable. On the other, stability favors a different factorization. The geometry of the category has not disappeared: the extensions are still there. What changes is the order and collection of semistable contributions.

# Why ordinary multiplication loses information

If the classes A and B interacted trivially, ordinary commuting variables might be enough to record them. But extensions are directional. The number and orientation of arrows matter. Motivic DT wall crossing uses a quantum torus whose generators do not necessarily commute.

Write two generators as X and Y and suppose that multiplying X by Y produces q times the result of multiplying Y by X. This relation captures a skew pairing of their underlying charge classes. Reversing their order introduces a power of q. Therefore we cannot reorder factors carelessly, and a wall-crossing identity is not merely a rearrangement of ordinary scalar functions.

The quantum dilogarithm is a formal generating series adapted to this noncommutative multiplication. Under a standard normalization, it satisfies a pentagon identity. On one side we multiply a factor associated with X and then one associated with Y. On the other, reversing their order requires a third factor associated with their combined charge. That middle factor represents the contribution of an extension class.

The three-factor expression is a small algebraic shadow of the new stable object that can appear at the wall. The identity is often presented as one of the first nontrivial examples of the Kontsevich-Soibelman wall-crossing formula.

# What the pentagon counts

The phrase quantum dilogarithm might suggest an analytic special function with a mysterious name. For our purpose, its important feature is formal. It is an infinite power series whose coefficients encode increasingly many copies of a stable charge. The precise powers of q depend on the chosen motivic or refined normalization.

Now multiply two such series in a quantum torus. Each coefficient mixes the charges of two stable constituents. Because the variables do not commute, the order also records their antisymmetric interaction. The pentagon identity says that the result can be refactored through a combined charge. This is the algebraic fingerprint of a stability change that admits or excludes the corresponding bound state.

A warning is essential. The two-vertex quiver alone is not automatically the full three-Calabi-Yau setting required for motivic DT invariants. It is a useful model of extensions, and the quantum pentagon becomes an actual motivic wall-crossing identity after placing the example in an appropriate Calabi-Yau or quiver-with-potential framework. Without such structure, the algebraic example remains an analogy rather than a complete DT construction.

# Why a motivic count contains more than a number

An ordinary Euler characteristic replaces a variety by an integer. Many geometrically different spaces can have the same Euler characteristic. A motivic class remembers more. For example, the affine line contributes a distinguished element, often denoted by the letter L, and the class of a projective line is one plus L rather than immediately two.

This refinement lets a counting theory distinguish phenomena that disappear under numerical specialization. The category of vanishing cycles, orientation data, and motivic integration supply further structure in the full Donaldson-Thomas construction. These ingredients are not optional decoration: they account for the geometry of critical loci and the signs or weights that arise when moduli spaces are singular.

If we then pass to a suitable quasi-classical limit, quantum-torus identities can induce transformations of an ordinary Poisson torus. The limit retains wall-crossing information in symplectic or cluster-like transformations. But taking a limit requires specifying a coefficient ring and handling denominators and completions; it is not always legal to substitute q equal to one directly into every term of a quantum-dilogarithm series.

# Ordered products and sectors

The general wall-crossing formula is organized by charges and their phases. Choose a sector in the complex plane of central charges. Form an ordered product of quantum-torus elements associated with stable classes whose central charges lie in that sector, sorted by phase.

As stability varies, a ray can cross another ray and the factors may have to be rearranged. Provided the hypotheses are met and no relevant ray crosses the boundary of the chosen sector, the total ordered product stays fixed. Individual invariants may jump, but their combined transport does not.

This is why the order matters. If the algebra were commutative, rearranging the factors would convey much less information. The noncommutativity forces correction factors that register extensions. What appears as a change in enumerative numbers is constrained by a stable algebraic identity.

# A change of accounting, not a loss of structure

The small pentagon example provides a useful mental picture. Before the wall, we count two constituent types in one order. After the wall, we count them in another order, and a stable extension may contribute between them. The generating-series factors change, but a conserved product relates the two sides.

The general theory is far richer: it involves derived categories, orientation data, motives, moduli stacks, and completed quantum tori. Still, its core insight is visible already. A stability condition chooses which objects count individually. The extension algebra remembers how they can combine. Wall-crossing identities ensure that changing the choice does not erase that information; it repackages it in a controlled way.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A standard toy quantum torus has generators X,Y with `XY=q YX`. The completed algebra admits formal quantum-dilogarithm series. In one common convention, with the central variable `Z=q^(-1/2)XY`, an appropriate quantum dilogarithm E obeys a pentagon identity of the form
\[
 \mathbb E(X)\mathbb E(Y)=\mathbb E(Y)\mathbb E(Z)\mathbb E(X).
\]
**Convention warning:** products, q-powers and inverses vary with the quantum dilogarithm definition and the sign convention for the skew Euler form. One must pick a normalization before doing coefficient arithmetic. This is an identity in a completed *noncommutative* algebra, not an ordinary identity for commuting variables.

For a 3-Calabi-Yau category with charge lattice Gamma, skew pairing `\langle-,-\rangle`, suitable motivic integration, and a stability condition, the DT factors `A_gamma` form an ordered sector product. Under wall crossing, the sector product is invariant when the boundary rays remain clear; the factors and their ordering can change. The Hall algebra describes extensions and underlies the identity. For a variety `P^1`, `[P^1]=1+L` in the Grothendieck ring of varieties, where `L=[A^1]`, whereas its topological Euler characteristic is two. This exhibits the loss of information in a numerical specialization.

### Exercises with answers

1. If `XY=qYX`, what is `YX` in terms of `XY`? **Answer:** `q^(-1)XY`.
2. Why is an extension not generally equivalent to a direct sum? **Answer:** a nonzero extension class can yield a nonsplit object.
3. What information does `[P^1]=1+L` retain that the number two forgets? **Answer:** the distinction between affine-line and point contributions in the motivic coefficient ring.
4. Can the pentagon identity be applied to an arbitrary category with two simple objects? **Answer:** not as a DT identity without the required Calabi-Yau, stability, and integration hypotheses.

### Reading and source notes

- [Kontsevich and Soibelman, Stability Structures, Motivic Donaldson-Thomas Invariants and Cluster Transformations](https://arxiv.org/abs/0811.2435), motivic invariants, quantum tori and ordered wall crossing.
- [Kontsevich and Soibelman, Motivic DT Invariants: Summary of Results](https://arxiv.org/abs/0910.4315), accessible summary of the refined theory.
- [Kontsevich and Soibelman, Wall-Crossing Structures and Mirror Symmetry](https://arxiv.org/abs/1303.3253), wall-crossing structure and integrable systems.
