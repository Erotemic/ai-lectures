# 076000 - Projection-valued measures

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `010000-011000` orthogonal projections; `030000` finite spectral projections; `073000-075000` Borel sets, measures, and continuous functional calculus. **Next:** `077000` scalar spectral measures and polarization.

<!-- BEGIN SPOKEN LECTURE -->

# A measure whose values are projections

For a real symmetric matrix with three distinct eigenvalues, we can project onto any chosen subset of its eigenspaces. Each such projection keeps the selected eigenvector components and removes the others. Projecting onto two disjoint eigenvalue groups and adding the results gives the projection onto their union. Projecting onto the empty group gives zero, and projecting onto all three gives the identity.

In infinite-dimensional spectral theory, eigenvectors may be absent. Nevertheless, a self-adjoint operator still supplies projections associated with Borel sets of spectral values. The rule assigning a projection to each measurable set is a projection-valued measure.

The word measure signals countable additivity, but here the outputs are projections rather than numbers. For disjoint measurable spectral sets, the associated projections have orthogonal ranges. Their countable sum is interpreted through strong convergence on each Hilbert-space vector, not necessarily by operator-norm convergence.

We will derive the finite matrix example, state the countable-additivity requirement carefully, and then connect projection-valued measures to scalar measures obtained by taking inner products. That connection is what permits spectral integration and functional calculus.

## The definition

Let H be a complex Hilbert space. An orthogonal projection is an operator that keeps a closed subspace and discards its orthogonal complement; it is self-adjoint and idempotent. A Borel set is a set of real numbers built from open sets by complements and countable unions. A projection-valued measure, abbreviated P V M, assigns to each Borel subset B a bounded operator E of B on H.

Three requirements control the assignment. First, every E of B is an orthogonal projection: it is self-adjoint and its square equals itself. Second, E of the whole real line is the identity operator. Third, for pairwise disjoint Borel sets B-one, B-two, and so forth, E of their union is the sum of the individual projections, where the infinite sum converges strongly.

Strongly means the following. Choose any one vector x. The partial sums of E of B-n applied to x converge in norm to E of the union applied to x. We do not demand convergence of the operators themselves in operator norm.

An immediate consequence is that E of the empty set is zero. Another is monotonicity: if B is contained in C, then the range of E of B sits inside the range of E of C.

The product rule is even more useful: E of B times E of C equals E of their intersection. We can regard this either as part of an equivalent definition or derive it from the countable-additivity axioms. To see the derivation, split B and C into their intersection and disjoint remainders. Projections assigned to disjoint sets have orthogonal ranges. Multiplying the two decompositions eliminates every cross term except the common intersection.

Thus all spectral projections obtained from the same P V M commute with one another.

## Why strong convergence is the right requirement

Consider the Hilbert space of square-summable sequences. Let E of the singleton containing n project onto the n-th coordinate axis, with the spectrum indexed by positive integers. The projection onto the first N coordinates is the sum of the first N singleton projections.

For a fixed square-summable sequence, the squared norm of the discarded tail approaches zero. Hence these partial sums converge strongly to the identity.

But their operator-norm distance from the identity is always one: a unit vector supported in coordinate N plus one is completely missed by the partial sum. So operator-norm convergence fails at every finite stage.

This is not a pathology. It shows exactly why ordinary countable additivity of scalar measures cannot be copied into the operator norm. The infinite-dimensional spectral theorem uses strong operator convergence because that is what the geometry supplies.

## Scalar measures hidden inside a P V M

Fix a vector x in H. Define a nonnegative number for every Borel B by taking the inner product of E of B applied to x with x.

Because E of B is an orthogonal projection, this number is exactly the squared length of E of B applied to x. Call the resulting set function mu sub x.

Its total mass is the squared norm of x, because E of the whole line is the identity. For disjoint Borel sets, the projected pieces are orthogonal. The Pythagorean theorem then gives countable additivity by passing to the strong limit. Thus mu sub x is a finite positive measure.

This scalar measure answers a concrete question: how much of the squared length of x lies in each spectral region?

For the multiplication operator on the unit interval, E of B multiplies by the indicator of B. If x is represented by a function h of t, then mu sub x of B is the integral over B intersected with the unit interval of the squared magnitude of h.

For a diagonal matrix, mu sub x is a discrete measure: the mass at an eigenvalue is the squared length of the component of x in that eigenspace. For example, take a two-by-two diagonal matrix with eigenvalues zero and two. Give x the coordinates three and four. The spectral mass at zero is nine, the mass at two is sixteen, and the total is twenty-five, exactly the squared length of x. If we normalize x to a unit vector, those two masses become nine twenty-fifths and sixteen twenty-fifths. This makes the measure feel like a distribution of squared energy across spectral regions. The continuous and discrete examples are two versions of the same rule.

## Recovering a self-adjoint operator

Why do we call E a spectral measure? Because it allows us to reconstruct the operator by integration.

For a simple scalar function, meaning a finite combination of indicator functions, define its operator integral by replacing each indicator with the corresponding projection. If f takes value three on one Borel set and minus one on another disjoint set, its integral is three times the first projection minus the second.

When f is a bounded Borel function, the integral can be obtained by a controlled limit of simple functions.

In particular, when E comes from a bounded self-adjoint operator A, integrating the coordinate function lambda against E reproduces A. Symbolically we write A equals the integral of lambda with respect to E. The boundedness of A ensures its spectral measure is supported in a bounded region, so the coordinate is bounded on the relevant support.

One can then reconstruct each spectral projection by integrating the indicator of its Borel set. That is why the infinite spectral theorem replaces a finite sum over eigenvalues by an integral over spectral values.

## Constructing the projections from functional calculus

There is an important logical direction here. We should not define E by referring to eigenvectors, since multiplication operators may have none.

Start instead with the continuous functional calculus for bounded self-adjoint operators. For every vector x, the rule that sends a continuous function f to the inner product of x with f of A applied to x is positive and bounded. A measure-representation theorem assigns a finite positive measure mu sub x to that functional.

These diagonal measures describe all quadratic expressions. To recover off-diagonal expressions, use the polarization identity. That produces matrix elements for bounded Borel functions. The Riesz representation theorem then constructs a bounded operator for each such function.

The product and adjoint identities must be checked, not assumed. Once they hold, apply this Borel calculus to the indicator of B. Its square equals itself pointwise, so the resulting operator squares to itself. The indicator is real-valued, so the resulting operator is self-adjoint. It is therefore an orthogonal projection.

Indicators of intersections multiply to the indicator of the intersection, giving the product rule for spectral projections. Countable additivity follows at the level of scalar measures and then, using orthogonality and the Pythagorean theorem, at the level of vectors.

The construction has two intertwined parts: measure theory produces the countable-additive diagonal data, while Hilbert-space geometry converts that data into projections.

## A boundary example

Take again multiplication by t on the unit interval. Consider the intervals from zero up to, but not including, one half, and from zero through one half, including the endpoint.

As subsets of the real line they differ. Yet on ordinary Lebesgue L two, they produce the same spectral projection, because a single point has measure zero. Both simply keep the function on the left half, up to equality almost everywhere.

This does not mean all endpoints can be ignored. If the operator has an eigenvector with eigenvalue one half, the scalar spectral measure of that eigenvector has a nonzero atom there. Including the endpoint then adds an entire eigenspace.

Thus Borel sets are precise inputs, but the effect of changing a set depends on which spectral measures assign mass to the changed part.

## What we have constructed

A projection-valued measure assigns a compatible orthogonal decomposition of H to every Borel spectral region. Its countable additivity is strong, and each vector converts it into an ordinary finite positive measure.

The two-coordinate example shows the meaning: each vector splits into orthogonal pieces, and the scalar measure records their squared lengths. The projection-valued measure performs the splitting for all vectors simultaneously, even when the spectrum cannot be listed as eigenvalues. Strong countable additivity ensures that infinitely many pieces still reconstruct every fixed vector.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

For a bounded self-adjoint `A`, the spectral measure is a projection-valued measure `E` on the real Borel sets, characterized by `E(B)^* = E(B)`, `E(B)^2 = E(B)`, `E(R) = I`, `E(B) E(C) = E(B intersect C)`, and strong countable additivity. Each vector defines the finite positive measure `mu_x(B) = <x,E(B)x> = ||E(B)x||^2`. The construction here uses bounded Borel calculus; general scalar measure-representation and polarization results form earlier foundations.

### Two-level spectral energy calculation

Let \(A=\operatorname{diag}(0,2)\), with spectral PVM \(E\), and take \(x=(3,4)\). Then
\[
E(\{0\})=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
E(\{2\})=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\quad \mu_x=9\,\delta_0+16\,\delta_2,
\]
and \(\mu_x(\mathbb R)=25=\|x\|^2\). For \(x/5\), the two atom masses are \(9/25\) and \(16/25\). In \(L^2([0,1])\) with \(Af(t)=tf(t)\), the corresponding measure is \(\mu_x(B)=\int_{B\cap[0,1]}|x(t)|^2dt\), which may have no atoms at all.

**Lean bridge (verbatim source declaration headers).**

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/PVM.lean` - `specProj`:

```lean
noncomputable def specProj (B : Set ℝ) (hB : MeasurableSet B) : H →L[ℂ] H :=
```

An indicator of a relabelled measurable set becomes a bounded spectral projection. The parameter `ha` asserts normality of the ambient bounded operator, and `hκ` asserts measurability of the spectral coordinate change.

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/PVM.lean` - `inner_specProj_self`:

```lean
theorem inner_specProj_self (B : Set ℝ) (hB : MeasurableSet B) (ξ : H) :
    ⟪ξ, specProj ha hκ B hB ξ⟫_ℂ = (((specDiag ha κ ξ) B).toReal : ℂ) :=
```

This connects the projection to the finite positive diagonal measure of a vector; it is the scalar counting law underlying strong additivity.

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/PVM.lean` - `toProjValMeasure`:

```lean
noncomputable def toProjValMeasure : TauCeti.ProjValMeasure ℝ H where
```

The preceding projection, diagonal measure, identity and intersection laws are assembled into the upstream `TauCeti.ProjValMeasure` structure.

**Scope:** The excerpts are declaration headers, not complete proof bodies. Their enclosing modules supply scalar types, normality/self-adjointness assumptions, and typeclass instances. The prose derives the mathematical statements and does not claim that all of the pedagogical arguments have separate local Lean theorems.
