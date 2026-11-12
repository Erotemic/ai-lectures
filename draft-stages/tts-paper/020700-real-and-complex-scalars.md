# 020700 — Real and complex scalars

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** sine-theta. **Audience:** the sine-theta theorem, the direct rotation, Ky Fan norms and dominance, principal angles.

<!-- BEGIN SPOKEN LECTURE -->

Real and complex scalars

The Davis–Kahan paper states its theorems for Hilbert spaces over the real numbers or over the complex numbers. Much of the machinery behind them, though, is complex: resolvents and contour integrals, the functional calculus that defines square roots and angle operators in general, and the spectra of unitary operators, which live on the unit circle in the complex plane. This lecture explains how results proved with complex tools are carried back to real spaces, and where the real and complex cases genuinely differ. The difference matters: it is the source of both the counterexample to Proposition 4.4 and the matching theorem.

Here is what we will establish. First, complexification: a real Hilbert space E can be enlarged to a complex one, whose vectors are x plus i y with x and y in E, and every real operator extends to it. Self-adjointness, projections, isometries, spectra, domains, and form bounds all carry over, and the complexified operator has exactly the same singular values as the original. Second, transfer: because Ky Fan norms are unchanged by complexification, an inequality between Ky Fan norms of complexified operators is the same inequality for the real operators, and Ky Fan dominance then gives every norm. This is how the sine-theta theorem, and the other perturbation bounds, pass from the complex case to the real case. Third, what does not transfer: minimization over transports. A complex unitary can multiply a vector by a phase, which no real orthogonal map can do on a single plane. As a result, the smallest trace-norm displacement of a transport is twice the sum of the sines of the principal angles over the complex numbers, but generally larger over the real numbers, where pairs of principal planes must cooperate to imitate a phase.

Why complex tools appear

For a real symmetric matrix, the spectral theorem holds over the real numbers: there is a real orthonormal eigenbasis. For many purposes, real is enough.

But several tools are naturally complex. The resolvent integral that produces a spectral projection integrates around a contour in the complex plane. The continuous functional calculus, which defines the square root of a positive operator, the arc cosine of a cosine operator, or the exponential of a self-adjoint operator, is developed most generally for operators on complex Hilbert spaces. And a real orthogonal matrix that is not symmetric, such as a rotation of the plane, has no real eigenvalues; its eigenvalues are e to the plus and minus i theta. Davis and Kahan's characterization of the direct rotation as the square root of a product of reflections with spectrum in the closed right half-plane is a statement about complex spectra, and for a real direct rotation the paper reads it through the complexification.

Complexification

Given a real Hilbert space E, form the complex Hilbert space whose vectors are formal sums x plus i y, with x and y in E. Addition is componentwise, multiplication by a complex number uses i squared equals minus one, and the inner product of x plus i y with u plus i v is defined so that its real part is the sum of the real inner products of x with u and of y with v. As a real vector space, the complexification is two copies of E.

A real operator T extends by acting on both parts: T of x plus i y is T x plus i T y. Call this the complexification of T. Many properties are preserved.

If T is self-adjoint, so is its complexification. If T is an orthogonal projection, so is its complexification, and its range is the complexification of the range of T. If T is an isometry, so is its complexification. If T is unbounded with domain D, the complexification has domain consisting of the x plus i y with both x and y in D. The quadratic form of the complexification at x plus i y equals the quadratic form of T at x plus the quadratic form of T at y. So a form bound such as T at least c times the identity holds for the complexification exactly when it holds for T, and the spectrum of a self-adjoint T is unchanged by complexification.

Singular values are preserved. The complexified Gram operator acts as T star T on the real part and on the imaginary part separately, so it has the same eigenvalues as T star T, with the same multiplicities counted over the complex numbers. So the complexification of T has the same singular values as T, and every Ky Fan norm, and every unitarily invariant norm, is unchanged. Going in the other direction, regarding a complex space as a real space of twice the dimension, doubles every multiplicity: a complex operator with singular values two and zero becomes a real operator with singular values two, two, zero, zero. That direction, called realification, will matter shortly.

Transferring inequalities

Suppose we want to prove a real inequality of the form delta times N of X at most N of Y, for every unitarily invariant norm N, where X and Y are real operators. By Ky Fan dominance, it is enough to prove delta times the Ky Fan k-norm of X at most the Ky Fan k-norm of Y, for every k.

Now suppose the complex theorem, applied to the complexified data, gives delta times every Ky Fan norm of the complexified X at most the same Ky Fan norm of the complexified Y. Those Ky Fan norms are the Ky Fan norms of X and Y themselves. So the real Ky Fan inequality holds for every k, and dominance gives every norm.

For this to apply to the sine-theta theorem, each hypothesis must survive complexification, and each does. The trial frame, the exact frames, and the residual are complexified; the residual identity and the intertwining identity hold for the complexified operators on the complexified domains; the gap configuration is a statement about spectra or quadratic forms, which are unchanged; and the sine of Theta zero for the complexified pair is the complexification of the real sine. So the complex sine-theta theorem implies the real one. This is how the real statements follow from the complex ones, and for unbounded operators it requires complexifying each operator together with its domain.

Where real and complex differ: transport

Now consider a different kind of question: among all maps of the whole space that carry U onto V, which moves the space least? Over the complex numbers, the competitors are unitary maps. Over the real numbers, they are orthogonal maps. Complexifying a real orthogonal map gives a complex unitary map, but most complex unitary maps are not complexifications of anything real. The complex minimization therefore ranges over more competitors, and its minimum can be smaller. Transfer fails, because a minimum over a larger set is not a statement about each real competitor.

The difference already appears in one principal plane. Take a complex two-dimensional space, with the source line spanned by the first basis vector and the target line at angle theta. The direct rotation is the matrix with cosine theta on the diagonal and i times sine theta off the diagonal. It is unitary, it carries the source line onto the target line, and its eigenvalues are e to the plus i theta and e to the minus i theta. The displacement, the identity minus the rotation, has singular values the distances from one to these eigenvalues, each two sine of theta over two, so its trace norm is four sine of theta over two.

Now multiply the direct rotation by the phase e to the i theta. Multiplying a unitary by a unit complex number gives another unitary, and it still carries the source line onto the target line, since multiplying a vector by a phase does not change the line it spans. The eigenvalues become e to the two i theta and one. The displacement now has singular values two sine theta and zero, so its trace norm is two sine theta. That is smaller than four sine of theta over two, for every angle between zero and ninety degrees. At thirty degrees, the direct rotation's trace norm is about one point zero four and the phased map's is exactly one. This is Davis and Kahan's Example 4.2, a complex phase modification that decreases the trace norm of the full displacement.

Two sine theta is also a lower bound. Every transport carrying U onto V has full displacement whose trace norm is at least the trace norm of P minus Q, which in this plane is two sine theta. Over the complex numbers, this lower bound is attained for every pair of equal-dimensional subspaces in finite dimensions: the minimum trace-norm displacement is twice the sum of the sines of the principal angles.

Over the real numbers, the phase trick is unavailable on a single plane. A real orthogonal map of the plane is either a rotation, with eigenvalues e to the plus and minus i of an angle, or a reflection, with eigenvalues one and minus one. To carry the horizontal line onto the line at angle theta, a rotation costs at least four sine of theta over two in trace norm, and a reflection costs two. Neither reaches two sine theta.

Realification: imitating a phase with two planes

There is a way around this. Identify complex two-dimensional space with real four-dimensional space, letting multiplication by i act as a quarter turn in each of two real planes. Under this identification, the complex phased map becomes a real orthogonal map of four-dimensional space, carrying a real two-dimensional source subspace onto a real two-dimensional target subspace, with both principal angles equal to theta. Its displacement has singular values two sine theta, two sine theta, zero, zero, so its trace norm is four sine theta, which is twice the sum of the sines of the two angles. The real direct rotation of that four-dimensional pair, by contrast, rotates each of the two principal planes separately and has trace norm eight sine of theta over two.

This is precisely the real counterexample to Proposition 4.4 in the journal paper: the complex Example 4.2, realified. A real map that couples two principal planes can imitate a complex phase, and so beat the direct rotation in trace norm, even though no map acting on one plane at a time can.

What happens when the two angles differ? Coupling two planes with angles theta i and theta j costs four sine of half their sum, while the complex lower bound for the same two angles is two sine theta i plus two sine theta j. By the sum-to-product identity, the latter equals four sine of half the sum times cosine of half the difference, which is smaller unless the angles are equal. So for unequal angles, coupling is worth less, and leaving a plane alone, or reflecting it, may be better. With angles of twenty and fifty degrees, coupling costs about two point two nine, against the complex bound of about two point two two. Deciding which planes to couple, and which to treat alone, is exactly the weighted matching problem that the paper's final theorem solves.

To summarize. Complexification extends a real Hilbert space and its operators while preserving self-adjointness, projections, isometries, domains, form bounds, and spectra, and it doubles singular-value multiplicities when viewed over the reals. Since Ky Fan sums of a doubled list are twice the original Ky Fan sums, any Ky Fan inequality proved for complexified data transfers to the real data, and dominance then gives every unitarily invariant norm; this is how the perturbation theorems hold over both fields. Minimization over transports does not transfer, because complex unitaries include phases. Over the complex numbers, the minimum trace-norm displacement is twice the sum of the sines of the principal angles. Over the real numbers it is generally larger, and reaching it requires coupling principal planes in pairs, which is the mechanism of both the Proposition 4.4 counterexample and the matching theorem.

The real and complex theories agree for inequalities that hold for every operator satisfying hypotheses; they can disagree for statements about the best operator in a class, because the class itself depends on the field.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Complexification

\(E_{\mathbb C}=E\oplus iE\), \(\langle x+iy,u+iv\rangle\) with real part \(\langle x,u\rangle+\langle y,v\rangle\); \(T_{\mathbb C}(x+iy)=Tx+iTy\); \(\operatorname{dom}T_{\mathbb C}=\operatorname{dom}T+i\operatorname{dom}T\).
Preserved: self-adjointness, projections, isometries, \(\sigma(T)\) (self-adjoint case), \(\operatorname{Re}\langle T_{\mathbb C}(x+iy),x+iy\rangle=\langle Tx,x\rangle+\langle Ty,y\rangle\).
\(s_j(T_{\mathbb C})=s_j(T)\) with the same complex multiplicities, so \(\|T_{\mathbb C}\|_{(k)}=\|T\|_{(k)}\). Realification (regarding a complex operator as real on twice the dimension) doubles multiplicities: \(T_{\mathbb C}\) viewed over \(\mathbb R\) is \(T\oplus T\).

**Transfer:** \(\delta\|X_{\mathbb C}\|_{(k)}\le\|Y_{\mathbb C}\|_{(k)}\ \forall k\Rightarrow\delta\|X\|_{(k)}\le\|Y\|_{(k)}\ \forall k\Rightarrow\delta N(X)\le N(Y)\).

### Transport costs (one principal angle \(\theta\))

| Field | Map | eigenvalues | \(\|I-W\|_1\) |
|---|---|---|---|
| ℂ | direct rotation \(\begin{pmatrix}c&is\\is&c\end{pmatrix}\) | \(e^{\pm i\theta}\) | \(4\sin(\theta/2)\) |
| ℂ | phased \(e^{i\theta}D\) (Example 4.2) | \(e^{2i\theta},1\) | \(2\sin\theta\) |
| ℝ | rotation | \(e^{\pm i\theta}\) | \(4\sin(\theta/2)\) |
| ℝ | reflection | \(1,-1\) | \(2\) |

At \(30^\circ\): \(4\sin15^\circ\approx1.035\), \(2\sin30^\circ=1\). Lower bound \(\|P-Q\|_1=2\sum_i\sin\theta_i\le\|I-W\|_1\).
Realification of the phased map (\(i\mapsto J\)): \(\mathbb R^4\), both angles \(\theta\), singular values \((2\sin\theta,2\sin\theta,0,0)\), trace \(4\sin\theta\); real direct rotation \(8\sin(\theta/2)\).
Pairing unequal angles: \(e_{ij}=4\sin\tfrac{\theta_i+\theta_j}2\ge2(\sin\theta_i+\sin\theta_j)=4\sin\tfrac{\theta_i+\theta_j}2\cos\tfrac{\theta_i-\theta_j}2\); \((20^\circ,50^\circ)\): \(2.294\) vs \(2.216\).

### Lean correspondence

`DavisKahan/FiniteDimensional/DirectRotation/ComplexTracePrincipalAngles.lean`, `namespace TauCeti.DavisKahan.FiniteDimensional.ComplexTraceOptimality`:

```lean
theorem exists_global_complex_trace_minimizer_with_principalAngles
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection]
    (hUV : finrank ℂ U = finrank ℂ V) :
    ∃ W : H ≃ₗᵢ[ℂ] H,
      U.map W.toLinearMap = V ∧
      (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) =
        (U.starProjection.toLinearMap - V.starProjection.toLinearMap).kyFanSum (finrank ℂ H) ∧
      (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) =
        2 * ∑ j : Fin (finrank ℂ U), Real.sin (Submodule.principalAngles U V (j : ℕ)) ∧
      ∀ Z : H ≃ₗᵢ[ℂ] H, U.map Z.toLinearMap = V →
        (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) ≤
          (LinearMap.id - Z.toLinearMap).kyFanSum (finrank ℂ H)
```

Complexification of possibly unbounded operators: `ForTauCeti/Analysis/InnerProductSpace/LinearPMap/Complexification.lean` (`complexificationDomain`, `complexificationLinearMap`); real continuous functional calculus through complexification: `ForTauCeti/Analysis/InnerProductSpace/RealContinuousFunctionalCalculus.lean` (`complexifiedCfcHom`). Real versions of the source theorems carry the suffix `_real` (e.g. `proposition6_1_real`, `theorem6_1_real`, `proposition3_3_real_forward`).
