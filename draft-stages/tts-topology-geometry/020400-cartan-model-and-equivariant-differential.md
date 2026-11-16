# 020400 — The Cartan Model: An Exterior Derivative that Knows the Action

**Track:** Topology and Geometry. **Background:** differential forms, Lie derivative, contraction with vector fields. **Central question:** how can equivariant cohomology be calculated using differential forms on the original manifold?

<!-- BEGIN SPOKEN LECTURE -->

# The Cartan Model: An Exterior Derivative that Knows the Action

The homotopy quotient explains what equivariant cohomology is, but it is rarely where we want to do calculations. The auxiliary contractible space E G is infinite-dimensional in the standard models. We would rather work with differential forms on the original finite-dimensional manifold and a manageable symbol recording the group action.

For a smooth circle action, the Cartan model does exactly that. It modifies the exterior derivative by one operation from vector calculus: inserting the infinitesimal generator of the symmetry into a differential form.

## What contraction does

A vector field X tells us the direction in which a one-parameter group moves each point. A differential one-form assigns a number to a tangent vector. Contracting that one-form with X simply evaluates the form on X. For a two-form, contraction produces a one-form by placing X into the first slot. In general, contraction lowers form degree by one.

The usual exterior derivative raises form degree by one. If we want to subtract contraction from the exterior derivative while keeping a consistent total grading, we multiply contraction by a formal variable u of degree two. Then both terms raise total degree by one.

Define the equivariant differential by the ordinary exterior derivative minus u times contraction with X. This formula is often written d sub T. Different books use an overall sign change or another normalization of X; we will keep this convention fixed.

## Why the square is zero only for invariant forms

The square of the ordinary exterior derivative is zero. Contracting twice with the same vector field is also zero because alternating forms vanish when two slots receive the same vector. The remaining cross terms combine into the Lie derivative along X, by Cartan's identity.

Consequently the square of d sub T is minus u times the Lie derivative. This is not zero on an arbitrary differential form. It becomes zero on forms invariant under the circle action, because those have zero Lie derivative along X.

Thus the Cartan complex consists of circle-invariant differential forms with coefficients in the polynomial ring in u, equipped with d sub T. Its cohomology computes circle-equivariant cohomology with real coefficients, for a compact circle action. We have traded the abstract homotopy quotient for differential forms and a formal variable.

## Work out the freely rotating circle

Take M to be a circle with coordinate t modulo one. Let the circle act on itself by translation, so the generating vector field X is the derivative with respect to t. The invariant differential forms are combinations of constants and the one-form dt, with polynomial coefficients in u.

The ordinary exterior derivative of dt is zero. Its contraction with X is one. Therefore the equivariant differential of dt is minus u. That single calculation has a large consequence: u is an equivariant boundary. So are all its positive powers, since u to the k is the equivariant differential of minus u to the k minus one times dt.

What remains in equivariant cohomology is just the constant class. This matches the Borel calculation: a circle acting freely on itself has contractible homotopy quotient. We have reproduced that fact using an explicit two-term algebra of differential forms.

The result also explains why the polynomial variable is not automatically a nonzero class in every equivariant space. It exists in the complex, but a differential can kill it when the geometry of the action supplies an invariant one-form evaluating to one on X.

## A Hamiltonian action has a special closed form

Now let the circle act on a symplectic manifold with symplectic form omega. Suppose the generator X is Hamiltonian: contraction of omega with X equals the differential of a function mu, called a moment map component.

Consider the combination omega plus u times mu. Apply the equivariant differential. The derivative of omega vanishes because omega is symplectic. The remaining terms are u times the differential of mu minus u times the contraction of omega. They cancel exactly.

So omega plus u mu is equivariantly closed. This is a crucial bridge between symplectic geometry and localization. Ordinary omega carries area. The moment-map term records the action. Their sum is a single cohomology class in the Cartan complex.

It is essential that mu be a genuine global function. On a flat torus, translation in one coordinate preserves the area form but its contracted one-form may have a nonzero period; then no global mu exists. The Cartan combination cannot be constructed in that simple way for that action.

## A check at a fixed point

At a fixed point p, every positive-degree differential form on a point vanishes. The equivariant class omega plus u mu restricts to u times the number mu of p. A global symplectic form has become a polynomial, and its coefficient is the moment-map value at the fixed point.

Later the fixed-point tangent weights will appear in a denominator. The Cartan model has already given us the numerator. It makes the localization theorem less mysterious: the fixed-point formula evaluates a globally closed equivariant object where the symmetry stops moving the manifold.

The two calculations worth retaining are small. On a freely rotating circle, d sub T of dt equals minus u. For a Hamiltonian action, d sub T of omega plus u mu equals zero. These two identities explain much of the difference between free actions and actions with fixed points.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `X` be the infinitesimal generator of a period-one circle action. Work over R and set

\[
\Omega_{S^1}(M)=\big(\Omega^*(M)\otimes\mathbb R[u]\big)^{S^1},\quad
|u|=2,\quad d_T=d-u\iota_X.
\]

Cartan's identity `dι_X+ι_X d=L_X` gives `d_T²=-uL_X=0` on invariant forms. On `M=R/Z` with `X=∂_t`, `d_T(dt)=-u`; hence `H^*(\Omega_{S^1}(M),d_T)=R` in degree zero. For Hamiltonian `ι_X ω=dμ`, `d_T(ω+uμ)=0`. The moment map is defined only up to a constant; shifting μ adds a multiple of the equivariant class u.

### Exercises with answers

1. What degree must u have for `uι_X` to raise total degree by one? **Answer:** two.
2. Why is the Cartan differential square-zero only on invariant forms? **Answer:** `d_T²=-uL_X`; invariance gives `L_X=0`.
3. Calculate `d_T(u² dt)` for the free translation circle. **Answer:** `-u³`.
4. If `ι_Xω=dμ`, what is the simplest equivariantly closed extension of omega under this sign convention? **Answer:** `ω+uμ`.

### Sources and further reading

- L. Jeffrey, [Equivariant Cohomology lecture notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf), Cartan model and localization.
- [Cartan model](https://en.wikipedia.org/wiki/Equivariant_cohomology#The_Cartan_model); [Cartan's magic formula](https://en.wikipedia.org/wiki/Cartan%27s_magic_formula).
