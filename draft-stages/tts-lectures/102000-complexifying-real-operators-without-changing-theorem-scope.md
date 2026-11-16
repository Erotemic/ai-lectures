# Complexifying real operators without changing theorem scope

<!-- BEGIN SPOKEN LECTURE -->

# Complexifying real operators without changing theorem scope

## Real Hilbert complexification

Imagine rotating a vector in the real plane by ninety degrees.

Point right and the rotation sends you up. Point up and it sends you left. If you apply the rotation twice, you get a half turn, which is multiplication by negative one.

Could this rotation have an eigenvector? Over the real numbers, no. There is no nonzero direction that a ninety-degree rotation leaves on its own line.

But if we allow complex scalars, the rotation has eigenvalues i and negative i. The missing spectral description appears when we enlarge our scalars.

This gives us a reason to complexify a real Hilbert space. We want access to complex spectral theory while preserving the original real geometry. We also want to know which results can be brought back to the real setting without changing their constants.

### One complex vector is two real vectors

Start with a real Hilbert space E. It could be the plane, or it could be an infinite-dimensional space of real square-summable sequences.

Construct a new space whose elements are pairs of real vectors, x and y. We write the pair as x plus i y.

This notation is literal: x is the real component and y is the imaginary component. Both belong to E.

Addition works component by component. To multiply x plus i y by a complex number a plus i b, use ordinary complex multiplication: the new real component is a x minus b y, and the new imaginary component is b x plus a y.

Try multiplying by i alone. It sends x plus i y to negative y plus i x. Do it a second time and you get negative x minus i y. So multiplication by i really does square to negative one.

We have constructed a complex vector space from the original real one.

There is one dimension point worth keeping straight. The real plane becomes a complex space with complex dimension two, even though it has four real coordinates when viewed without its complex structure. We have not thrown away the original plane. It sits inside as vectors whose imaginary component is zero.

### Preserve lengths and completeness

We need more than complex scalar multiplication. A Hilbert space has a notion of distance, and it must be complete.

Define the squared norm of x plus i y to be the squared norm of x plus the squared norm of y.

This makes geometric sense. The two copies of E are perpendicular in the underlying real geometry. Multiplying by i exchanges those copies with a sign, so it preserves length.

For example, if x has length three and y has length four, the complexified vector has length five.

The complex inner product is chosen to extend the original real inner product, with the appropriate cross terms. Its value on a vector paired with itself is precisely the squared norm we just defined.

Completeness is inherited coordinatewise. A Cauchy sequence of these pairs has a Cauchy sequence of real components and a Cauchy sequence of imaginary components. Since E is complete, both converge. Their pair is the limit in the complexification.

So we've genuinely built a complex Hilbert space, not just adopted a notation.

### Apply the same real operator to both coordinates

Suppose T is a bounded real-linear operator from a real Hilbert space E to another real Hilbert space F.

Define its complexification in the obvious way: apply T to x, and separately apply T to y. Thus x plus i y is sent to T x plus i T y.

It's important to check that this is complex linear. Multiplication by i exchanges the two real coordinates with a sign, and applying a real-linear T commutes with that exchange. The same holds for any complex scalar.

Complexification also respects composition and addition. If one real operator is applied after another, doing that first and complexifying gives the same result as complexifying both and then composing.

Let's look at a simple diagonal matrix. Suppose T multiplies the first real coordinate by two and the second by five. Applied to a complex vector, it multiplies the first complex coordinate by two and the second by five. No new stretching has appeared.

In fact, the operator norm is exactly preserved for every bounded real-linear T.

### Why the norm does not change

Take any vector x plus i y. The squared length of its image under complexified T is the sum of the squared lengths of T x and T y.

Each term is at most the square of the original operator norm times the squared length of its input. Add the two inequalities. The norm of complexified T cannot exceed the norm of T.

Now restrict the input to vectors with imaginary component zero. On those vectors, the complexified operator behaves exactly like T, with exactly the same lengths. That gives the reverse inequality.

So the two operator norms are equal.

This is stronger than saying complexification is continuous. Any quantitative estimate that depends only on bounded operator norms can carry over with its numerical constant intact, provided the other hypotheses also survive.

### Adjoints, self-adjointness, and conjugation

The adjoint is defined by an inner-product relation: pairing T x with a target vector equals pairing x with the adjoint applied to that target vector.

Because the complex inner product was built from the real one, this relation holds separately for the real and imaginary components and their cross terms. The complexification of the real adjoint is the adjoint of the complexified operator.

Consequently, a bounded real self-adjoint operator becomes a bounded complex self-adjoint operator. Its Gram operator also transfers: complexifying T adjoint T gives the Gram operator of complexified T.

Now consider the operation of complex conjugation. It sends x plus i y to x minus i y. The original real vectors are exactly the ones fixed by this operation.

Every complexified real operator commutes with conjugation. You get the same result whether you conjugate the input first or conjugate the output afterward.

There's also a converse. Suppose a bounded complex-linear operator on this complexified space commutes with conjugation. It must send real fixed vectors to real fixed vectors. Restrict it to that real copy of E, and it becomes a bounded real-linear operator. Complexifying the restriction reconstructs the original complex operator.

That gives us a test for whether an operator constructed in complex space really comes from the real space.

### Revisit the rotation

Our ninety-degree real rotation has no real eigenvectors. Its complexification has two complex eigenvalues, i and negative i. So complexification can reveal spectral features that aren't expressible as real eigenvalues.

But the rotation is not self-adjoint. For self-adjoint operators, the complex spectrum lies on the real axis. That observation makes the transfer of their spectral information much cleaner.

We have to keep the two claims separate. Complexifying any bounded real map preserves its norm and algebraic structure. Complexifying a self-adjoint real map also makes complex spectral theory available, but recovering a particular spectral projection requires checking that the construction respects conjugation.

The useful mental picture is a real space embedded inside two coordinated real copies. Operators extend by acting on each copy in the same way. Their norms and adjoints stay intact. And conjugation tells us exactly which bounded complex operators can be returned to the real setting.

## Real and complex spectra and functional calculus

Take a real diagonal matrix with eigenvalues negative two and three. Suppose you want to keep the first eigendirection and discard the second.

There's an obvious answer: use the projection that keeps the first coordinate and kills the second.

But let's construct that projection in a different way, without writing down the eigenvectors.

Consider the function that takes a number t to three minus t, divided by five. At negative two, the function is one. At three, it is zero.

Now apply that function to the matrix. Since the function is a polynomial, this means take three times the identity, subtract the matrix, and divide by five. The resulting matrix is exactly the projection we wanted.

We've selected a spectral subspace by applying a scalar function to an operator. This is the basic idea of functional calculus.

Now imagine that the available spectral theorem was proved over complex Hilbert spaces, while the operator and the subspace we care about are real. Can we use the complex theorem and recover a genuine real projection, with no change in norms or spectral gaps?

### First preserve the resolvent test

A real Hilbert space can be complexified by replacing each real vector with a pair, written x plus i y. A bounded real operator T becomes a complex operator by applying T separately to x and to y.

The original real space sits inside as the vectors with imaginary part zero. Complex conjugation identifies that real copy: it fixes x plus i zero.

Suppose we shift T by a real number t. The question is whether T minus t times the identity has a bounded inverse.

If it has a real inverse, complexify the inverse. It undoes the complexified shifted operator, so the complex inverse exists.

Conversely, suppose the complexified shifted operator has a bounded inverse. The shifted operator commutes with conjugation, and its inverse must commute with conjugation as well. Therefore that inverse carries real vectors to real vectors. Restricting to the real copy gives a bounded real inverse.

So for a real scalar t, the shifted operator is invertible over the reals exactly when its complexification is invertible at that same t.

This proves agreement of the real-scalar resolvent tests. We have not said that an arbitrary real operator has the same entire spectrum in every sense. For example, a real ninety-degree rotation acquires the complex eigenvalues i and negative i after complexification.

### Self-adjointness makes spectral location transfer

Now assume T is self-adjoint on the real Hilbert space.

Its complexification is also self-adjoint, because complexification respects adjoints. The complex spectral theorem then places its spectrum on the real number line.

That removes the extra nonreal spectral possibilities. The real spectrum of T, defined through real-scalar invertibility, agrees with the complex spectrum of its complexification after identifying real numbers with points on the real axis.

In our diagonal example, both versions have spectral values negative two and three. The same separation survives complexification.

Why do we care about exact preservation? If an estimate depends on a gap of five, changing fields should not replace that number with a weaker constant. The norm-preserving complexification and the matching real spectral locations let us keep the original numerical bound.

### From polynomials to continuous functions

The polynomial in our example was chosen to be one on the selected eigenvalue and zero on the other. But a matrix with many eigenvalues, or an operator with a continuous spectrum, may need a less elementary function.

For a bounded self-adjoint operator, continuous functional calculus assigns an operator to every continuous function on its spectrum. It respects addition, multiplication, adjoints, and norm limits.

Start with real polynomials. The complexified real operator commutes with conjugation. Powers of it commute with conjugation; so do real scalar multiples and sums. Thus every real polynomial applied to it commutes with conjugation.

Continuous real-valued functions on a compact real spectrum can be uniformly approximated by real polynomials. Applying the functional calculus and passing to the operator-norm limit preserves the conjugation relation.

Therefore a continuous real-valued function of a complexified real self-adjoint operator commutes with conjugation. It restricts to a bounded real operator.

Positivity and order estimates come back too. If the function is nonnegative at every spectral value, the resulting operator is positive. If it lies between two real constants on the spectrum, the operator's quadratic form lies between the corresponding bounds. Restricting to real vectors preserves those inequalities.

This is the central transfer principle for continuous spectral calculus.

### Why the gap is useful when selecting a projection

An indicator function takes the value one on a chosen set and zero outside it. Applied through spectral calculus, it should produce the projection onto that spectral part.

Indicators are generally discontinuous. This is where a spectral gap helps.

Return to the matrix with eigenvalues negative two and three. There are no spectral values between them. We are free to choose a continuous function that is one on the lower spectral component, transitions across the empty gap, and is zero on the upper component.

The function doesn't have to jump at a point in the spectrum. On the spectrum itself, it agrees exactly with the desired indicator.

Our simple polynomial, three minus t divided by five, already does the job on those two spectral points. In a more general bounded self-adjoint operator, we can choose a continuous real-valued function that equals one on one isolated closed spectral piece and zero on the other. Continuous functional calculus produces a self-adjoint idempotent operator: an orthogonal projection.

Because the function is real valued, the projection commutes with conjugation. Its restriction is the corresponding real projection, whose range is a real spectral subspace.

The open gap did two jobs: it identified a genuinely isolated part of the spectrum, and it let us use continuous rather than discontinuous functional calculus to select that part.

### What changes at a spectral boundary

Now replace the matrix with multiplication by the coordinate on square-integrable functions over the interval from zero to one.

The spectrum fills the entire interval. Suppose we want to keep the functions supported below one half and discard those supported above one half.

The required projection multiplies each function by an indicator: one for inputs below one half, zero for inputs above it. It is a perfectly well-defined bounded orthogonal projection.

But the indicator jumps at one half, right in the spectrum. There is no continuous function on the entire spectral interval that agrees with it point by point.

The continuous functional calculus alone therefore doesn't give this projection through a continuous symbol. We need bounded Borel functional calculus, or another argument that handles the discontinuity.

Real spectral measures do admit such projections, but the descent from complex space needs the corresponding conjugation-invariance argument for Borel operations. A proof that handled only uniform limits of polynomials is not enough.

This distinction is especially important for spectral selections whose boundary touches the spectrum.

### The numerical value of preserving spectra

Suppose t lies a positive distance delta away from the spectrum of a real self-adjoint operator. The norm of the shifted inverse in complex Hilbert space equals the reciprocal of that distance.

The complex inverse commutes with conjugation, so it descends to the real shifted inverse. Since complexification preserves operator norms, the same resolvent bound holds in real space with the same delta.

This illustrates the full pattern. We transfer the operator, preserve its self-adjointness and real spectral location, apply the complex theorem, and recognize the resulting bounded operator by its conjugation symmetry.

The result is a real operator with the same norm estimate. For spectral projections, a genuine gap makes the construction accessible through continuous functional calculus; a spectral boundary inside the spectrum calls for the stronger Borel theory.

## Real versions of unbounded Sylvester bounds

Consider two real diagonal matrices. Let A have diagonal entries three and five. Let B have diagonal entries negative one and negative two.

We want to find a matrix X satisfying this equation: A times X, minus X times B, equals a given matrix C.

For a single entry of X, the equation is simple. The entry is multiplied by an eigenvalue of A minus an eigenvalue of B.

For the upper-left entry, that number is three minus negative one, or four. So if C has a one in its upper-left corner and zeros elsewhere, X has one quarter there and zeros elsewhere.

Why is the number four important? Every eigenvalue of A is at least three, and every eigenvalue of B is at most negative one. There is a gap of four between the two spectral regions.

That gap gives a uniform scale for the solution. For our particular C, the norm of X is exactly one quarter of the norm of C.

Our goal is to extend this reasoning to possibly unbounded self-adjoint operators on real Hilbert spaces, and to symmetric operator ideal gauges. We'll use complexification to transport a complex Sylvester theorem back to the real setting without changing the gap constant.

### From entrywise division to an operator estimate

In the matrix example, each entry of X is the corresponding entry of C divided by the difference between one eigenvalue of A and one of B.

It is tempting to say that since all denominators have absolute value at least four, every matrix norm must shrink by at least a factor of four.

That conclusion doesn't follow from entrywise comparison for an arbitrary matrix norm. Singular values depend on how entries combine. We need an argument that controls the whole operator.

For ordered self-adjoint spectral regions, a useful argument comes from an integral. When A is positive and B is negative in the appropriate shifted sense, we can build X by integrating the operators that decay under A on the left and under B on the right.

In our example, A is at least three and B is at most negative one. For positive time t, the norm of the left decay factor is at most the exponential of negative three t. The norm of the right factor is at most the exponential of negative one t. Together they give the exponential of negative four t.

Integrating that scalar upper bound over all positive times gives one quarter. This explains the operator-level constant for an ordered gap, without pretending that entrywise bounds alone prove it.

For general unbounded operators and general symmetric ideals, we must also justify the domains, the exact gap condition, and ideal membership.

### The domain-aware real problem

Let A be a possibly unbounded self-adjoint operator on a real Hilbert space E. Let B be a possibly unbounded self-adjoint operator on another real Hilbert space F.

The unknown X and the given right-hand side C are bounded real-linear maps from F to E.

The Sylvester equation is A X minus X B equals C.

That formula needs a precise meaning when A and B are unbounded. We require X to take each vector in the domain of B into the domain of A. Only then can A X be applied to that input.

On every vector in the domain of B, we require A X x minus X B x to equal C x.

Notice the asymmetry. B acts first on the input space F, while A acts after X has carried the input to E. The domain condition ensures that both sides are legal.

We also require a positive number delta and a particular form-bounded spectral-gap hypothesis. Ordered separation is one covered configuration. An interval-versus-exterior configuration is another. Arbitrarily disjoint spectra are not enough to invoke every constant-one ideal estimate.

### Complexifying an unbounded domain

Here's the important step that doesn't appear in elementary matrix algebra.

If A is defined only for certain real vectors, then its complexification must be defined only for x plus i y when both x and y belong to the domain of A.

Why both? Because multiplication by i exchanges the real and imaginary components. A domain containing x plus i y but rejecting negative y plus i x would fail to be a complex vector subspace.

On this complexified domain, define the new operator by applying A separately to x and to y.

The original graph of A is closed because A is self-adjoint. The graph of the complexification is built from two copies of that closed graph, so it is closed too. Density of the domain transfers coordinatewise.

The adjoint-domain relation transfers as well, and with it self-adjointness. Thus the complexified A and B are legitimate complex self-adjoint operators.

Now take the real Sylvester equation. X maps the domain of B into the domain of A. Applying that statement separately to x and y shows that complexified X maps the complexified B domain into the complexified A domain.

Apply the real equation to both components and combine them. We obtain the complex Sylvester equation with complexified C on the right.

The operator equation survives because its domain conditions have survived.

### Check that the spectral gap survives

Suppose A is bounded below by three and B is bounded above by negative one, as in our example. Their complexified quadratic forms at x plus i y are sums of the corresponding real quadratic forms at x and y.

Therefore the same lower and upper bounds hold, giving the same ordered gap of four.

The argument also handles reversed ordering. For the covered interval-versus-exterior form-gap branch, preservation of self-adjoint spectral information and resolvent behavior supplies the corresponding transfer.

What we gain is precise: the complex operators satisfy the same kind of hypothesis, with the same positive delta. Complexification does not turn an arbitrary pairwise gap into a stronger ordered gap.

We can now apply the complex unbounded Sylvester estimate.

### Why finite Ky Fan sums come first

For a fixed positive integer k, the Ky Fan gauge sums the first k approximation singular values of a bounded operator.

The complex Sylvester theorem gives an estimate of this form: delta times the k-th Ky Fan gauge of complexified X is at most the k-th gauge of complexified C.

But we're after a theorem about real operators. How do we know the complexification hasn't changed the relevant singular-value data?

For a finite real matrix, the answer is clear: viewing the same real matrix over the complex numbers doesn't change its singular values.

For arbitrary Hilbert-space operators, the appropriate fact is equality of approximation numbers. One direction follows by complexifying real finite-rank approximations. For the reverse direction, the singular-value min–max characterization shows that the real and complex problems have the same lower-bound witnesses after extending their spans appropriately.

Thus every approximation number is preserved by complexification, and every finite Ky Fan prefix is preserved exactly.

We can remove the word complexified from the inequality. For each k, delta times the real k-th Ky Fan gauge of X is at most that of C.

No extra factor appears.

### From prefixes to an arbitrary symmetric ideal

A finite-prefix inequality is not yet a theorem about an entire operator ideal.

Some ideals contain only a proper subset of bounded operators. To say that X has finite trace norm, for example, we must first know that X is trace class.

Assume we're working with a real symmetric ideal family that has Ky Fan dominance, and assume C belongs to that ideal.

We have shown that every finite Ky Fan prefix of X is bounded by the corresponding prefix of C divided by delta. The dominance property now supplies both conclusions: X also belongs to the ideal, and its ideal gauge is at most the gauge of C divided by delta.

For our two-dimensional example with C supported in the upper-left corner, this estimate is an equality in operator norm, Hilbert–Schmidt norm, and trace norm. Both the gap and the factor of one are visible directly from the solution with entry one quarter.

If we replace the two coordinates with infinitely many real coordinates and let the diagonal entries grow without bound, A and B can be unbounded. We then have to restrict their domains so their weighted output sequences remain square summable. The same complexification and gap reasoning still applies.

The completed conclusion has three essential ingredients: a legal domain-aware Sylvester equation, an allowed positive form-gap hypothesis, and ideal membership of C together with Ky Fan dominance. Under those assumptions, X belongs to the ideal and delta times its gauge is no greater than the gauge of C.

This is why complexification is effective. It allows the complex spectral argument to do the analytic work while returning the same real operator estimate, the same ideal membership, and the same numerical gap.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Real Hilbert complexification

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `007000` real and complex scalars, `009000` inner products, `012000` adjoints, `100000` modulus and ideal invariance. **Next:** `103000` real and complex spectra and functional calculus.

---

#### Companion: mathematics and Lean correspondence (display only)

The construction is `RealComplexification E = E ⊕₂ E`, with complex multiplication `(a+ib) • (x,y) = (ax−by,bx+ay)`. The real embedding `ofReal x = (x,0)` is isometric. For `T : E →L[ℝ] F`, `complexify T` acts on both coordinates, satisfies `‖complexify T‖=‖T‖`, respects composition and adjoint, and commutes with canonical conjugation.

##### Worked example: the real plane and rotation

For \(E=\mathbb R^2\), the complexification has complex dimension two and is canonically identifiable with \(\mathbb C^2\). The real rotation
\[
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]
satisfies \(R^2=-I\). Its complexification has eigenvalues \(i\) and \(-i\), while the real operator has no nonzero real eigenvector. For \(T=\operatorname{diag}(2,5)\), \(\|\operatorname{complexify}T\|=\|T\|=5\).

##### Actual Lean source declarations

`ForTauCeti/Analysis/InnerProductSpace/Complexification/Basic.lean` — `complexify` (exact declaration header; proof omitted):

```lean
def complexify [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    [NormedAddCommGroup F] [InnerProductSpace ℝ F]
    (T : E →L[ℝ] F) : RealComplexification E →L[ℂ] RealComplexification F := by
```

`ForTauCeti/Analysis/InnerProductSpace/Complexification/Basic.lean` — `norm_complexify` (exact declaration header; proof omitted):

```lean
theorem norm_complexify [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    [NormedAddCommGroup F] [InnerProductSpace ℝ F]
    (T : E →L[ℝ] F) : ‖complexify T‖ = ‖T‖ := by
```

`ForTauCeti/Analysis/InnerProductSpace/Complexification/Basic.lean` — `complexify_isSelfAdjoint_iff` (exact declaration header; proof omitted):

```lean
theorem complexify_isSelfAdjoint_iff [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    [CompleteSpace E] (T : E →L[ℝ] E) :
    IsSelfAdjoint (complexify T) ↔ IsSelfAdjoint T := by
```

`ForTauCeti/Analysis/InnerProductSpace/Complexification/FunctionalCalculus.lean` — `complexify_adjoint` (exact declaration header; proof omitted):

```lean
theorem complexify_adjoint (T : E →L[ℝ] F) :
    complexify T.adjoint = (complexify T).adjoint := by
```

**Type and hypothesis map.** `complexify` takes a real continuous linear map `E →L[ℝ] F` to a complex continuous linear map between the two real complexifications. The norm theorem is an equality. The self-adjointness equivalence adds a complete real Hilbert space assumption; the adjoint bridge handles rectangular maps. These are bounded operator declarations, distinct from the later unbounded partial-map transport.

These Lean snippets are copied exactly from the supplied DKPS repository snapshot. The narration is an independent mathematical derivation; this appendix does not claim that the narrated text was compiled in Lean. Foundational results currently in `ForTauCeti` may have been developed in DKPS before upstreaming.

### Real and complex spectra and functional calculus

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `032000` finite functional calculus, `075000` continuous functional calculus, `079000` Borel calculus, `102000` real Hilbert complexification. **Next:** `104000` real versions of unbounded Sylvester bounds.

---

#### Companion: mathematics and Lean correspondence (display only)

For `T : E →L[ℝ] E`, invertibility at a real scalar parameter is preserved and reflected by complexification. If `T` is self-adjoint, the complexified operator is self-adjoint and its complex spectrum lies in `ℝ`; the real spectra agree. The operator-conjugation involution fixes `complexify T`. Continuous real-valued functional calculus preserves this fixed-point algebra. In a genuine gap, a continuous `spectralGapSymbol` agrees on the spectrum with the half-line indicator, permitting descent of the selected spectral projection and its range.

##### Worked example: a real spectral projection via functional calculus

Let \(A=\operatorname{diag}(-2,3)\) on \(\mathbb R^2\). The real polynomial \(f(t)=(3-t)/5\) satisfies \(f(-2)=1\) and \(f(3)=0\). Therefore
\[
f(A)=\frac{3I-A}{5}=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]
which projects onto the lower eigenspace. A continuous function agreeing with the indicator on two disjoint closed spectral components produces the corresponding gap projection. For multiplication by \(t\) on \(L^2([0,1])\), the indicator of \([0,1/2]\) is discontinuous on the spectrum, so its projection requires Borel rather than continuous functional calculus.

##### Actual Lean source declarations

`ForTauCeti/Analysis/InnerProductSpace/Complexification/Spectrum.lean` — `mem_spectrum_complexify_iff` (exact declaration header; proof omitted):

```lean
theorem mem_spectrum_complexify_iff (T : E →L[ℝ] E) (r : ℝ) :
    (r : ℂ) ∈ spectrum ℂ (complexify T) ↔ r ∈ spectrum ℝ T := by
```

`ForTauCeti/Analysis/InnerProductSpace/Complexification/FunctionalCalculus.lean` — `conjugateOperator_cfcHom` (exact declaration header; proof omitted):

```lean
theorem conjugateOperator_cfcHom
    (C : RealComplexification E →L[ℂ] RealComplexification E) (hC : IsSelfAdjoint C)
    (hfix : conjugateOperator C = C) (g : C(spectrum ℝ C, ℝ)) :
    conjugateOperator (cfcHom hC g) = cfcHom hC g := by
```

`DavisKahan/SpectralTheory/Complexification/BoundedGapProjection.lean` — `realBoundedSpectralProjectionIicOfGap` (exact declaration header; proof omitted):

```lean
noncomputable def realBoundedSpectralProjectionIicOfGap
    (B : E →L[ℝ] E) (hB : IsSelfAdjoint B)
    (alpha delta : ℝ) (_hdelta : 0 < delta)
    (_hgap : realSpectrum B ⊆ Set.Iic alpha ∪ Set.Ici (alpha + delta)) :
    E →L[ℝ] E :=
```

`DavisKahan/SpectralTheory/Complexification/BoundedGapProjection.lean` — `complexify_realBoundedSpectralProjectionIicOfGap` (exact declaration header; proof omitted):

```lean
theorem complexify_realBoundedSpectralProjectionIicOfGap
    (B : E →L[ℝ] E) (hB : IsSelfAdjoint B)
    (alpha delta : ℝ) (hdelta : 0 < delta)
    (hgap : realSpectrum B ⊆ Set.Iic alpha ∪ Set.Ici (alpha + delta)) :
    complexify (realBoundedSpectralProjectionIicOfGap B hB alpha delta hdelta hgap) =
      boundedSelfAdjointSpectralProjection (complexify B)
        (ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mp
          ((complexify_isSelfAdjoint_iff B).2 hB))
        (Set.Iic alpha) measurableSet_Iic := by
```

**Type and hypothesis map.** The spectral membership theorem compares **real scalar parameters** for the real operator and its complexification. `conjugateOperator_cfcHom` assumes a self-adjoint complexified-space operator fixed by conjugation and a real-valued continuous symbol. The real spectral projection constructor requires a strictly positive gap and spectral containment in two separated half-lines; the companion theorem identifies its complexification with the selected complex spectral projection. The cited declarations do not by themselves assert descent for every arbitrary Borel indicator.

These Lean snippets are copied exactly from the supplied DKPS repository snapshot. The narration is an independent mathematical derivation; this appendix does not claim that the narrated text was compiled in Lean. Foundational results currently in `ForTauCeti` may have been developed in DKPS before upstreaming.

### Real versions of unbounded Sylvester bounds

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `090000` form gaps, `093000` domain-aware Sylvester equations, `094000` unbounded Sylvester estimates, `096000` approximation numbers, `102000–103000` real complexification and spectral descent. **Next:** `105000` proof-readiness assembly.

---

#### Companion: mathematics and Lean correspondence (display only)

The domain-aware real equation has `A : E →ₗ.[ℝ] E`, `B : F →ₗ.[ℝ] F`, `X C : F →L[ℝ] E`, `X(B.domain) ⊆ A.domain`, and `(AX−XB)x=Cx` on `B.domain`. Partial-map complexification transports closed domains, self-adjointness, resolvents, form bounds, and the Sylvester equation. Approximation numbers and all finite Ky Fan prefixes are exactly preserved. A real `SymmetricOperatorIdealFamily` needs `IsKyFanDominant` and `N.Mem C` to derive `N.Mem X` together with `δ N.gaugeReal X ≤ N.gaugeReal C`.

##### Worked example: ordered-gap real Sylvester equation

Let \(A=\operatorname{diag}(3,5)\) and \(B=\operatorname{diag}(-1,-2)\) on \(\mathbb R^2\). The ordered form gap is \(\delta=4\). For \(C=e_1e_1^*\), the solution to \(AX-XB=C\) is \(X=\tfrac14e_1e_1^*\), attaining \(\delta\|X\|_{\mathcal I}=\|C\|_{\mathcal I}\) for operator, Hilbert–Schmidt and trace norms.

If \(A=\operatorname{diag}(n+2)\) and \(B=\operatorname{diag}(-n)\) on real \(\ell^2(\mathbb N_{\ge1})\), both are unbounded self-adjoint diagonal operators on their maximal weighted-square-summability domains. The same ordered lower and upper bounds produce \(\delta=4\). Their complexifications have domains consisting of pairs of vectors in the corresponding real domains.

##### Actual Lean source declarations

`DavisKahan/SpectralTheory/PartialMap/Complexification.lean` — `mem_domain_iff` (exact declaration header; proof omitted):

```lean
@[simp] theorem mem_domain_iff
    (A : E →ₗ.[ℝ] E)
    (z : Eℂ) :
    z ∈ domain A ↔ re z ∈ A.domain ∧ im z ∈ A.domain := by
```

`DavisKahan/SpectralTheory/PartialMap/Complexification.lean` — `closedSylvesterEquation_complexify` (exact declaration header; proof omitted):

```lean
theorem closedSylvesterEquation_complexify
    {A : E →ₗ.[ℝ] E}
    {B : F →ₗ.[ℝ] F}
    {X C : F →L[ℝ] E}
    (hEq : _root_.LinearPMap.SylvesterEquation A B X C) :
    _root_.LinearPMap.SylvesterEquation (complexify A) (complexify B)
      (RealComplexification.complexify X)
      (RealComplexification.complexify C) := by
```

`DavisKahan/SpectralTheory/PartialMap/Complexification.lean` — `isSelfAdjoint_complexify` (exact declaration header; proof omitted):

```lean
theorem isSelfAdjoint_complexify
    {A : E →ₗ.[ℝ] E}
    (hA : IsSelfAdjoint A) :
    _root_.IsSelfAdjoint (complexify A) := by
```

`DavisKahan/OperatorIdeal/ComplexificationApproximation.lean` — `kyFanApproximationGauge_complexify` (exact declaration header; proof omitted):

```lean
theorem kyFanApproximationGauge_complexify
    (T : E →L[ℝ] F) (k : ℕ) :
    ((RealComplexification.complexify T).kyFanGauge k : ℝ) =
      (T.kyFanGauge k : ℝ) := by
```

`DavisKahan/Sylvester/RealUnbounded.lean` — `davisKahan1970_sylvester_real` (exact declaration header; proof omitted):

```lean
theorem davisKahan1970_sylvester_real
    (N : TauCeti.SymmetricOperatorIdealFamily ℝ)
    [N.toOperatorIdealFamily.IsKyFanDominant]
    {A : E →ₗ.[ℝ] E}
    {B : F →ₗ.[ℝ] F}
    (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {X C : F →L[ℝ] E} {δ : ℝ}
    (hδ : 0 < δ)
    (hgap : FormBoundedSylvesterGap A B δ)
    (hEq : _root_.LinearPMap.SylvesterEquation A B X C)
    (hC : N.Mem C) :
    N.Mem X ∧
      δ * N.gaugeReal X ≤
        N.gaugeReal C := by
```

**Type and hypothesis map.** The complex partial-map domain has real and imaginary coordinates in the original domain. `closedSylvesterEquation_complexify` transports an equation with legal domain compositions; self-adjointness and the form-gap conditions are transported separately. Finite Ky Fan gauges are preserved exactly for real bounded maps. The real Sylvester conclusion assumes a `SymmetricOperatorIdealFamily ℝ`, its `IsKyFanDominant` instance, positive `δ`, a `FormBoundedSylvesterGap`, the domain-aware equation, and `N.Mem C`; it returns both `N.Mem X` and the scaled real gauge bound.

These Lean snippets are copied exactly from the supplied DKPS repository snapshot. The narration is an independent mathematical derivation; this appendix does not claim that the narrated text was compiled in Lean. Foundational results currently in `ForTauCeti` may have been developed in DKPS before upstreaming.
