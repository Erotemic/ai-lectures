# 002000 — The geometry of spectral gaps

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** spectral. **Audience:** spectra of self-adjoint operators, reducing decompositions, trial operators and residuals.

<!-- BEGIN SPOKEN LECTURE -->

The geometry of spectral gaps

Every Davis–Kahan estimate divides a residual or a perturbation by a number delta, a spectral gap. But the phrase "a gap of delta" hides a choice. Two sets of numbers can be separated by delta in different geometric ways, and the theorems of the paper are sensitive to which way. A hypothesis that suffices for one theorem can be too weak for another, and the same delta can mean different things in different statements. This lecture sorts out the shapes of separation and which operators each theorem compares.

Here is what we will establish. There are three shapes. In the interval and exterior shape, one spectrum lies in a closed interval and the other stays at least delta outside it, on either or both sides. In the ordered shape, one spectrum lies entirely below some number b and the other entirely above b plus delta; both may be unbounded. In the distance-only shape, every point of one spectrum is at least delta from every point of the other, but the two may interlace. The first two shapes give the sine-theta estimate with constant one in every unitarily invariant norm. The distance-only shape gives constant one in the Hilbert–Schmidt norm, but not in the operator norm. And each theorem of the paper states which pair of operators its gap compares: the trial operator against the complementary exact block, the two exact blocks against each other, or the two blocks of the unperturbed operator.

Three pictures on a number line

Take two finite sets of real numbers, call them the trial spectrum and the unwanted spectrum, and draw them on a line.

First picture. The trial spectrum is one and three, and the unwanted spectrum is minus one half and five. Put the trial spectrum in the interval from one to three. The unwanted points lie outside, one to the left at distance one and a half, and one to the right at distance two. Enlarge the interval by one and a half on each side, to run from minus one half to four and a half; no unwanted point lies strictly inside the enlarged interval. This is the interval and exterior shape, with delta equal to one and a half. The unwanted spectrum surrounds the trial spectrum.

Second picture. The trial spectrum is ten, eleven, twelve, and every larger integer, and the unwanted spectrum is eight, seven, six, and every smaller integer. Everything wanted lies above nine and a half, everything unwanted lies below eight and a half. Choose b equal to eight; then the unwanted spectrum is at most b and the trial spectrum is at least b plus two. This is the ordered shape with delta equal to two. Neither set fits in a finite interval, so the interval and exterior shape does not apply. The ordered shape is the one the paper uses to allow both operators to be unbounded.

Third picture. The trial spectrum is one and three, and the unwanted spectrum is two. Every unwanted point is at distance one from every trial point, so the distance between the sets is one. But two lies between one and three. No interval containing the trial spectrum avoids it, and no single cut separates the sets into below and above. This is the distance-only shape, and it is genuinely weaker than the other two.

The first two shapes can be described by a single cut or a single window: the unwanted spectrum lies beyond a cut, or outside a window around the trial spectrum. The third cannot. That difference turns out to be decisive for the operator norm.

The shapes as operator hypotheses

For operators, the statements are made about spectra or, in the ordered case, quadratic forms.

Interval and exterior separation for a pair of self-adjoint operators B and C means: for some interval from beta to alpha, the spectrum of B lies in that interval and the spectrum of C does not meet the open interval from beta minus delta to alpha plus delta; or the same with B and C exchanged. The operator whose spectrum lies in the interval is bounded, because its spectrum is bounded. The other may be unbounded, with spectrum extending to infinity on one or both sides.

Ordered separation means: for some number b, B is at most b times the identity and C is at least b plus delta times the identity, in the sense of quadratic forms on their domains; or the same with B and C exchanged. For self-adjoint operators this is the same as saying the spectrum of B lies in the half-line up to b and the spectrum of C in the half-line from b plus delta. Both may be unbounded.

Distance-only separation means the distance between the two spectra is at least delta.

Ordered separation and interval and exterior separation overlap but neither contains the other. A trial spectrum in the interval from one to three, with unwanted spectrum at five and beyond, satisfies both. Unwanted spectrum on both sides of the trial interval satisfies only the interval shape. Two unbounded spectra, one above and one below, satisfy only the ordered shape. Both shapes imply distance-only separation.

Why the shape matters

Here is a first look at why a window or a cut is better than mere distance. The proofs, which come later in the course, rest on a Sylvester equation: an operator X satisfying C X minus X B equals Y, where Y comes from the residual. The question is how large X can be, given Y.

With a window, shift the scale so that the window is centered at zero. Then the operator B inside the window has norm at most a, the half-width of the window, and the operator C outside has every spectral point at least a plus delta in absolute value, so its inverse has norm at most one over a plus delta. Rearranging the equation, X equals C inverse times the quantity Y plus X B. Taking norms, the norm of X is at most one over a plus delta, times the norm of Y plus a times the norm of X. Multiply out and subtract: delta times the norm of X is at most the norm of Y. The constant is one, and the argument used only the multiplicative property of the norm, so it works for every unitarily invariant norm.

With a cut, a different argument gives the same constant: an integral representation of the solution in terms of exponentials of the two operators, which decay because of the ordering. That argument handles unbounded operators on both sides.

With only distance separation, neither argument applies, and the constant one fails in the operator norm. Davis and Kahan give a two by two example. Let B be the diagonal matrix with entries one and minus one, and C the diagonal matrix with entries zero and two. Their spectra, minus one and one against zero and two, interlace, and the distance between them is one. Let X be the symmetric matrix with rows three, minus three and minus three, one. Computing B X minus X C gives the symmetric matrix with rows three, three and three, minus three. The operator norm of that right-hand side is three root two, about four point two four. The operator norm of X is two plus root ten, about five point one six. So X is larger than the right-hand side divided by delta, which is one. No estimate with constant one can hold in the operator norm for distance-separated spectra.

In the Hilbert–Schmidt norm, the same example is harmless: the squared Hilbert–Schmidt norm of X is twenty-eight and that of the right-hand side is thirty-six. Davis and Kahan prove that distance-only separation always gives constant one in the Hilbert–Schmidt norm, and an operator-norm bound with an extra factor of the square root of the rank. Davis and Kahan asked whether the square root of the rank could be replaced by a universal constant. It can, and the best universal constant for distance-only separation in the operator norm is now known to be pi over two, larger than one.

Which operators each theorem compares

The second source of confusion is not the shape but the pair of operators. The paper works with a reference operator A and a perturbed operator A hat, equal to A plus H. The reference operator splits relative to the trial subspace into blocks A zero and A one; the perturbed operator splits relative to its exact subspace into blocks Lambda zero and Lambda one. Each theorem places its gap between a specific pair.

The sine-theta theorem compares the trial operator A zero with the complementary exact block Lambda one, and accepts either the interval and exterior shape or the ordered shape. The trial operator may be any self-adjoint operator, not necessarily a block of A, as long as the residual is formed with it.

The tangent-theta theorem asks for the ordered shape between the same two operators: the trial spectrum in an interval with top alpha, and the spectrum of Lambda one at or above alpha plus delta. It also needs the Rayleigh–Ritz condition, that the trial operator is the compression of A hat.

The doubled-sine theorem compares the two exact blocks of the perturbed operator, Lambda zero and Lambda one, in the interval and exterior shape. No hypothesis on the trial operator is needed for that estimate.

The doubled-tangent theorem compares the two blocks of the reference operator, A zero and A one, in the ordered shape, and assumes the perturbation has no diagonal blocks, H zero and H one both zero.

The symmetric sine theorem in Section 6 asks for two separations at once: A zero against Lambda one, and A one against Lambda zero. The second generalized sine theorem asks only for distance separation between the spectra of A zero and Lambda one, and concludes the Hilbert–Schmidt bound.

The two spectral-selection theorems of Section 8 use, respectively, an ordered gap between the reference blocks, and the doubled-sine hypothesis on the perturbed blocks together with a condition placing the reference block A zero within half of delta of the interval containing Lambda zero.

So a reader of the paper should ask two questions at every hypothesis: which shape, and between which operators.

The free beam

The paper's numerical example illustrates the most common case. The trial operator is zero, on the span of the two rigid motions of a free beam, so the trial spectrum is the single point zero. The perturbed operator's complementary spectrum, the unwanted part, lies above five hundred. Choose the interval from zero to zero. The unwanted spectrum lies at least five hundred above it and nothing lies below it, so both the interval and exterior shape and the ordered shape hold, with delta at least five hundred. The beam operator is unbounded, and its unwanted spectrum runs off to infinity; that is allowed, because the bounded side of the window is the trial spectrum.

If instead the trial operator is taken to be the Rayleigh–Ritz compression, its eigenvalues are about zero point two one epsilon and zero point seven nine epsilon, and the gap is measured from the top of that interval, so it becomes five hundred minus about zero point seven nine epsilon. The residual shrinks too. Each choice comes with its own gap and its own residual.

A test case for reading hypotheses

Return to the third picture, trial spectrum one and three, unwanted spectrum two, distance one. If a theorem's hypothesis is interval and exterior separation, it does not apply: the unwanted point two is inside every interval containing the trial spectrum. If the hypothesis is ordered separation, it does not apply either. If the hypothesis is distance separation, it applies with delta equal to one, and what follows is the Hilbert–Schmidt estimate with constant one, or an operator-norm estimate with a larger constant. It would be a mistake to read a statement with distance separation and conclude the operator-norm estimate with constant one.

To summarize. Spectral separation comes in three shapes: a window, where one spectrum lies in an interval and the other outside it enlarged by delta; a cut, where one spectrum lies below b and the other above b plus delta, both possibly unbounded; and mere distance, where interlacing is allowed. Windows and cuts give the sine-theta constant one in every unitarily invariant norm; distance gives constant one in the Hilbert–Schmidt norm but not in the operator norm, as the two by two example with spectra one, minus one, and zero, two shows. And each theorem fixes which pair of operators its gap compares: trial against complementary exact block for the sine and tangent theorems, the two exact blocks for the doubled sine, the two reference blocks for the doubled tangent.

A gap, however shaped, is only an assumption about spectra. Whether it holds for a given problem must be certified separately, for example from eigenvalue bounds such as Weyl's inequality, and an incorrectly shaped gap gives no conclusion at all.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Shapes

For self-adjoint \(B,C\) and \(\delta>0\):

- **Interval/exterior** \(\mathcal I_\delta(B,C)\): \(\sigma(B)\subseteq[\beta,\alpha]\), \(\sigma(C)\cap(\beta-\delta,\alpha+\delta)=\varnothing\), or roles exchanged.
- **Ordered** \(\mathcal O_\delta(B,C)\): \(B\le bI\), \(C\ge(b+\delta)I\) (forms on domains); equivalently \(\sigma(B)\subseteq(-\infty,b]\), \(\sigma(C)\subseteq[b+\delta,\infty)\).
- **Distance**: \(\operatorname{dist}(\sigma(B),\sigma(C))\ge\delta\).
- \(\mathrm{SineGap}(B,C):=\mathcal I_\delta(B,C)\vee\mathcal O_\delta(B,C)\vee\mathcal O_\delta(C,B)\).

Examples: \(\{1,3\}\) vs \(\{-\tfrac12,5\}\): \(\mathcal I_{3/2}\) only. \(\{10,11,\dots\}\) vs \(\{\dots,7,8\}\): \(\mathcal O_2\) only. \(\{1,3\}\) vs \(\{2\}\): distance \(1\) only.

### Window argument (Theorem 5.1 shape)

Center the window: \(\|B\|\le a\), \(\|C^{-1}\|\le(a+\delta)^{-1}\). From \(CX-XB=Y\): \(X=C^{-1}(Y+XB)\), so \(\|X\|\le(\|Y\|+a\|X\|)/(a+\delta)\), i.e. \(\delta\|X\|\le\|Y\|\); the same for any norm with \(N(KXL)\le\|K\|\,N(X)\,\|L\|\).

### Interlaced obstruction

\[
B=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\ C=\begin{pmatrix}0&0\\0&2\end{pmatrix},\ X=\begin{pmatrix}3&-3\\-3&1\end{pmatrix},\ BX-XC=\begin{pmatrix}3&3\\3&-3\end{pmatrix}.
\]
\(\delta=1\); \(\|X\|_{\rm op}=2+\sqrt{10}\approx5.162>3\sqrt2\approx4.243\); \(\|X\|_{\rm HS}^2=28\le36\). Best operator-norm constant for distance separation: \(\pi/2\) (Bhatia, *Matrix Analysis*, Section VII.2).

### Which pair each result compares

| Result | Gap | Operators | Other hypotheses |
|---|---|---|---|
| S2 sin θ | \(\mathrm{SineGap}\) | \(A_0,\Lambda_1\) | — |
| S2 tan θ | \(\mathcal O_\delta\) (\(A_0\) below) | \(A_0,\Lambda_1\) | \(H_0=0\) (Rayleigh–Ritz) |
| S2 sin 2θ | \(\mathcal I_\delta\) | \(\Lambda_0,\Lambda_1\) | common domain |
| S2 tan 2θ | \(\mathcal O_\delta\) | \(A_0,A_1\) | \(H_0=H_1=0\) |
| Prop 6.1 | \(\mathrm{SineGap}\) twice | \((A_0,\Lambda_1)\), \((A_1,\Lambda_0)\) | \(H\) bounded |
| Thm 6.2 | distance | \(A_0,\Lambda_1\) | HS conclusion; \(\sqrt{\operatorname{rank}R}\) for op norm |
| Thm 8.1 | \(\mathcal O_\delta\) | reference blocks | \(H_0=H_1=0\) |
| Thm 8.2 | central interval | \(\Lambda_0\) in \([\beta,\alpha]\), \(\Lambda_1\) outside; \(A_0\) in \([\beta-\delta/2,\alpha+\delta/2]\) | \(\|H\|\) or \(\|R\|<\delta/2\) |

### Lean correspondence

`DavisKahan/Sylvester/Gap.lean` (`namespace TauCeti.DavisKahan.Sylvester`):

```lean
def RealSpectrumIntervalExteriorGap
    (A : E →ₗ.[𝕜] E) (B : F →ₗ.[𝕜] F) (β α δ : ℝ) : Prop :=
  (_root_.LinearPMap.realSpectrum A ⊆ Set.Icc β α ∧
    _root_.LinearPMap.realSpectrum B ⊆ {x | x ≤ β - δ ∨ α + δ ≤ x}) ∨
  (_root_.LinearPMap.realSpectrum B ⊆ Set.Icc β α ∧
    _root_.LinearPMap.realSpectrum A ⊆ {x | x ≤ β - δ ∨ α + δ ≤ x})

inductive FormBoundedSylvesterGap
    (A : E →ₗ.[𝕜] E) (B : F →ₗ.[𝕜] F) (δ : ℝ) : Prop where
  | intervalExterior {β α : ℝ} (hβα : β ≤ α)
      (hgap : RealSpectrumIntervalExteriorGap A B β α δ)
  | leftAboveRightBelow (c : ℝ)
      (hA : TauCeti.LinearPMap.SemiboundedBelow A (c + δ))
      (hB : TauCeti.LinearPMap.SemiboundedAbove B c)
  | leftBelowRightAbove (c : ℝ)
      (hA : TauCeti.LinearPMap.SemiboundedAbove A c)
      (hB : TauCeti.LinearPMap.SemiboundedBelow B (c + δ))
```

The distance-only hypothesis appears as `PairwiseSpectrumGap` in the pairwise-gap estimates, e.g. `opNorm_sylvester_le_of_pairwiseSpectrumGap` (conclusion `δ * ‖X‖ ≤ ‖C‖ * Real.sqrt r` for `C.rank ≤ r`) in `DavisKahan/Sources/DavisKahan1970/Sylvester/OperatorNormEstimate.lean`.
