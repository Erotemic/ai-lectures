# 066000 — Unitary and semigroup representations

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `039000–041000` exponentials and unitary flows; `063000–065000` Sylvester equations and ordered semigroups. **Next:** Rosenblum's contour method.

<!-- BEGIN SPOKEN LECTURE -->

# When two spectral directions move in opposite ways

Consider a map from the real numbers into the plane. It sends the number one to the column with entries two and four. Call the map C. On the plane, let A stretch the horizontal direction by negative two and the vertical direction by positive two. On the input line, let B be zero.

We want a map X for which A applied to X, minus X followed by B, equals C. Because B is zero, we can solve this one by inspection. The horizontal entry of X is negative one, and the vertical entry is positive two. Applying A gives back two and four.

The two coordinates tell us something important. One spectral difference is negative two and the other is positive two. Both are safely away from zero. But a method that requires every spectral difference to have the same sign cannot handle this example as a single decaying evolution. We need to understand two kinds of time evolution and the different inverse formulas they support.

## A Sylvester equation as a moving map

Let A be a bounded self-adjoint operator on an output Hilbert space, and B a bounded self-adjoint operator on an input Hilbert space. The unknown X maps inputs to outputs. Its equation is A X minus X B equals C, where C is a known map with the same input and output spaces as X.

First forget about inversion. Imagine observing a map as the two spaces evolve independently. At time t, evolve the output using the exponential of i times t A. Evolve the input using the exponential of i times t B, and undo that evolution on the right. The resulting map is called F of t. At time zero it is the original map.

Because A and B are self-adjoint, both evolutions are unitary. Unitary means they preserve lengths. Left and right unitary multiplication therefore preserve both the operator norm and, when applicable, the Hilbert-Schmidt norm of the map they transport.

Differentiate F in finite dimensions. The left exponential contributes i A F. Differentiating the reversed right evolution contributes negative i F B. Putting the pieces together, the derivative is i times the Sylvester expression A F minus F B.

This is the mental model: the Sylvester operator measures the instantaneous relative motion of a map under two different unitary evolutions. It is an operator acting on operators.

## Hear the two frequencies in the example

Return to the diagonal A with values negative two and positive two, and B equal to zero. Apply the unitary transport to the column C with entries two and four.

Its horizontal component acquires a complex phase that winds at frequency negative two. Its vertical component acquires a phase that winds at frequency positive two. Both keep their magnitudes. The components rotate in opposite directions in the complex plane.

A phase of negative two must eventually produce the reciprocal negative one half. A phase of positive two must produce positive one half. Multiplying those reciprocals by two and four gives our solution column, negative one and positive two.

The question is how an integral over time can perform that division without referring to a particular eigenbasis.

## Why an ordered gap gives a simpler integral

Suppose, unlike our example, that every spectral value of A is at least delta greater than every spectral value of B, with delta positive. Evolve by ordinary exponentials rather than imaginary ones: apply the exponential of negative t A on the left, and the exponential of positive t B on the right.

Every difference of spectral values is now positive. Consequently, each coefficient of the transported C decays at least as rapidly as the exponential of negative delta times t. Integration from time zero to infinity divides a coefficient by its positive spectral difference. The integral of the common decay envelope is one over delta.

This gives a Sylvester solution and a constant-one norm estimate: delta times the norm of X is at most the norm of C. The proof works because the entire operator decays under one common bound, not because we divided individual entries and added their sizes.

Try that orientation on our two-coordinate example. The positive-two component decays, but the negative-two component grows. Reversing the orientation merely exchanges which one grows. The ordered semigroup argument has failed to meet its own hypothesis; the Sylvester equation has not failed to be solvable.

## Build a two-sided oscillatory inverse

Return to unitary evolution, where neither component grows. Instead of integrating the orbit without a weight, multiply it by a suitable scalar function of time and integrate over all real times, both positive and negative.

The weight is chosen by its Fourier transform. At every frequency whose absolute value is at least delta, its transform must equal the reciprocal of that frequency. In our example delta is two, so the transform must take negative two to negative one half and positive two to positive one half.

Why specify the weight only outside the gap around zero? The reciprocal function becomes singular at zero. But zero cannot occur as a spectral difference under the assumed separation. We may modify the Fourier multiplier near zero to obtain an integrable time weight without changing any frequency needed by the equation.

There is a construction whose total absolute mass is pi divided by twice delta. This number measures the size of the integral kernel; it is not the time for a physical evolution, and it is not the actual cost of our two-coordinate example.

Integrating the weighted unitary orbit of C now reconstructs X. On each pair of spectral values, the Fourier transform supplies exactly one over their difference. In our example the two resulting entries are negative one and positive two.

## From a formula to a norm estimate

Each unitary factor preserves norms, so the size of the transported C never exceeds the size of C. Multiplying by the weight contributes its absolute value. The norm of an operator-valued integral is at most the integral of the norms.

We therefore obtain the operator-norm bound: delta times the norm of X is at most pi over two times the norm of C. The gap need only separate every left spectral value from every right spectral value. It does not impose an order on them.

Notice what the constant records. For the ordered semigroup we integrated a decaying envelope of total mass one over delta. For general separated spectra we use a two-sided oscillatory kernel whose absolute mass is pi over two delta. The latter is a general bound, even though a particular solution may be considerably smaller.

## What survives without eigenvectors

In an infinite-dimensional Hilbert space, a self-adjoint operator need not have a basis of eigenvectors. The finite coefficient story remains a guide, but a proof must use the spectral theorem.

For bounded self-adjoint A and B, approximate each by a finite spectral step operator, assembled from orthogonal spectral projections. Choose step values inside the original spectral sets. That choice preserves the lower bound on every cross-spectral difference.

The weighted integral works on each pair of spectral blocks. As the spectral steps approach A and B in operator norm, their unitary exponentials converge at each fixed time. The same integrable kernel dominates all these integrands. Dominated convergence gives the representation for the original bounded operators.

For unbounded self-adjoint operators, exponential evolution still gives strongly continuous unitary groups, but differentiating requires vectors in the generator's domain. One cannot replace that domain argument by a formal infinite power series. The distinction is between a valid group representation and a derivative identity that is meaningful only on its domain.

## A second Hilbert space made of maps

There is also a useful change of viewpoint. Hilbert-Schmidt maps form a Hilbert space whose squared norm sums the squared magnitudes of matrix entries in orthonormal bases. Left-right unitary transport acts unitarily on this new Hilbert space.

Its generator is i times the Sylvester operator. The spectral differences become the generator's frequencies. In the Hilbert-Schmidt norm, orthogonality of distinct spectral blocks permits a sharper constant-one estimate even when positive and negative differences coexist.

Our small example thus has three readings. Direct division solves it. A semigroup cannot use a single decaying orientation because the differences have opposite signs. The unitary Fourier method handles both signs and gives a general operator-norm bound, while the Hilbert-Schmidt geometry supplies additional square-summable control. The hypotheses on the spectrum and the norm determine which argument is available.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

For bounded self-adjoint \(A,B\), set \(U_A(t)=e^{itA}\), \(U_B(t)=e^{itB}\). Then
\[
\frac d{dt}\bigl(U_A(t)XU_B(-t)\bigr)
=iU_A(t)(AX-XB)U_B(-t).
\]
For \(\operatorname{dist}(\sigma(A),\sigma(B))\ge\delta>0\), choose \(\mu_\delta\in L^1(\mathbb R,\mathbb C)\) with
\[
\int_\mathbb R \mu_\delta(t)e^{it\omega}\,dt=\omega^{-1}
\quad(|\omega|\ge\delta),\qquad
\|\mu_\delta\|_{L^1}=\frac{\pi}{2\delta}.
\]
Then the separated-spectrum Sylvester inverse has representation
\[
X=\int_\mathbb R\mu_\delta(t)e^{itA}Ce^{-itB}\,dt,
\qquad \|X\|\le\frac\pi{2\delta}\|C\|.
\]
The source proves bounded infinite-dimensional reconstruction using finite spectral step approximations and dominated convergence. Compare `065000` for the better constant-one ordered case.

**One column through both signs.** With
\[
 A=\operatorname{diag}(-2,2),\quad B=[0],\quad
 C=\begin{bmatrix}2\\4\end{bmatrix},\quad
 X=\begin{bmatrix}-1\\2\end{bmatrix},
\]
we have \(AX-XB=C\), \(\delta=2\),
\(\|C\|=2\sqrt5\), and \(\|X\|=\sqrt5\).
The two spectral differences are \(-2\) and \(2\), with reciprocal multipliers
\(-\tfrac12\) and \(\tfrac12\). This particular column attains
\(\delta\|X\|=\|C\|\) even though the general operator-norm Fourier bound is
\(\delta\|X\|\le(\pi/2)\|C\|\). The universal upper bound need not be sharp
for a given pair of operators.

**Ordered comparison.** If \(A\ge aI\), \(B\le bI\), and \(a-b\ge\delta>0\),
then for bounded self-adjoint \(A,B\),
\[
 X=\int_0^\infty e^{-tA}Ce^{tB}\,dt,
 \quad \|e^{-tA}Ce^{tB}\|\le e^{-\delta t}\|C\|.
\]
The integral is operator-norm convergent. The two-sided example does not
satisfy this ordering, although its spectra are pairwise separated.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `separatedSylvesterMultiplier_identity`:

```lean
theorem separatedSylvesterMultiplier_identity
    (d : ℝ) (hd : 0 < d) (a b : ℝ) (hab : d ≤ |a - b|) :
    (∫ t : ℝ, separatedSylvesterMultiplier d hd t *
      Complex.exp ((((t * (a - b) : ℝ) : ℂ) * Complex.I))) =
      (((a - b)⁻¹ : ℝ) : ℂ) := by
```

The complex Fourier identity supplies reciprocal spectral differences outside the gap.

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `l1_norm_separatedSylvesterMultiplier`:

```lean
theorem l1_norm_separatedSylvesterMultiplier (d : ℝ) (hd : 0 < d) :
    (∫ t : ℝ, ‖separatedSylvesterMultiplier d hd t‖) =
      Real.pi / (2 * d) := by
```

The exact scalar `L¹` mass produces the `π/2` constant; this is distinct from the ordered exponential estimate.

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `separatedSylvester_reconstruction_complex`:

```lean
theorem separatedSylvester_reconstruction_complex
    {A : F →L[ℂ] F} {B : E →L[ℂ] E}
    (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {d : ℝ} (hd : 0 < d) (hsep : SpectraSeparated A ⊤ B ⊤ d)
    (X C : E →L[ℂ] F)
    (hEq : A ∘L X - X ∘L B = C) :
    X = ∫ t : ℝ, separatedSylvesterMultiplier d hd t •
      (unitaryGroup A t ∘L C ∘L unitaryGroup B (-t)) := by
```

The complex Hilbert-space theorem reconstructs a known solution using unitary conjugation and a pairwise spectral gap. The finite spectral-step limit appears in its proof.

