# Proof reconstruction: residual estimates and the Davis-Kahan theorem families

<!-- BEGIN SPOKEN LECTURE -->

# Proof reconstruction: residual estimates and the Davis-Kahan theorem families

## A full proof-readiness assembly

Suppose the plane has two distinguished directions: horizontal and vertical. An operator A kills the horizontal component and multiplies the vertical component by five.

The horizontal line is an exact invariant subspace. We want to approximate it with a line tilted upward by thirty degrees.

Choose a unit vector u along that tilted line. Its horizontal coordinate is the square root of three divided by two. Its vertical coordinate is one half.

Apply A to u. The result is a vertical vector of length two and a half. If we propose zero as the trial eigenvalue, this output is exactly the residual: the error in the proposed eigenvalue equation.

Now notice something. The vertical component of u has length one half. That is the sine of its angle with the horizontal axis. And the residual has length five times one half.

The factor five is the spectral separation between the trial eigenvalue zero and the unwanted vertical eigenvalue five.

In this example, the relationship is exact: gap times sine of the angle equals residual norm.

We want to understand how that elementary calculation extends to Hilbert spaces, possibly unbounded self-adjoint operators, nonorthonormal trial coordinates, and symmetric operator ideals.

The proof has three main ideas. Project the residual into the unwanted spectral directions. Use a Sylvester equation and spectral separation to control that projection. Then remove any artificial scaling of the trial coordinates to recover an actual subspace angle.

### See the complementary equation in the plane

In our example, let the exact target line be the horizontal axis and its orthogonal complement be the vertical axis.

If we keep only the vertical coordinate of u, we get one half. Call that the complementary coordinate X.

The operator A acts on the vertical axis as multiplication by five. Our proposed trial eigenvalue is zero. So the complementary-coordinate equation is simply five times X minus X times zero equals the vertical component of the residual.

The right-hand side is two and a half. The left-hand side is five times one half, also two and a half.

That's a one-dimensional Sylvester equation.

We can already see the structure. The gap lets us divide the complementary residual by five. What we recover is the amount of the trial vector that lies outside the target space.

But before generalizing, there's one complication that a geometric angle shouldn't have: dependence on how we scale our coordinates.

### A trial map may not be normalized

Instead of sending the scalar one to u, suppose our trial map sends it to two u. The trial subspace is still exactly the same tilted line.

The complementary coordinate is now two times one half, which is one. The residual is also twice as large, with length five.

The Sylvester equation still reads five times X equals the complementary residual, and the resulting inequality is still sharp. But X is now one, while the sine of the geometric angle remains one half.

We need a separate normalization step.

In this scaled example, the trial map stretches every scalar by two. Its lower frame bound is two. Dividing X by that stretch recovers the sine of the angle.

This is why a general theorem involving a trial map needs a lower frame bound as well as a spectral gap.

### Identify the spaces one at a time

Now let H be a real or complex Hilbert space, and let A be a self-adjoint operator on H. It may be unbounded.

Choose an exact reducing subspace for A. Call its orthogonal projection P. Reducing means both that subspace and its orthogonal complement are preserved by the operator in the domain-aware sense.

Represent the exact target subspace by an isometric coordinate map F zero. Represent its orthogonal complement by another isometric coordinate map F one. The ranges of these maps are orthogonal and together fill H.

On the complement, the action of A is represented by a self-adjoint operator Lambda one. Think of Lambda one as multiplication by five in our plane example.

Now introduce a trial coordinate space and a bounded map E zero from that coordinate space into H. Its range is the trial subspace. We assume a positive lower frame bound epsilon: the length of E zero x is at least epsilon times the length of x.

This condition keeps the trial map from collapsing nonzero coordinates. It also ensures that its range is closed and its positive modulus is invertible on the trial coordinate space.

Finally, choose a self-adjoint trial operator A zero on the trial coordinate space. In a Rayleigh–Ritz setting, it may come from compression; the abstract argument also allows other choices.

Our residual compares applying the ambient operator after E zero with applying the trial operator before E zero. In the plane example, the trial operator was simply multiplication by zero.

### Make the residual legal when A is unbounded

If A is unbounded, it cannot be applied to every vector in H. So an expression like A applied to E zero x needs a domain hypothesis.

The common-domain condition says that E zero x belongs to the domain of A exactly when x belongs to the domain of A zero.

On that common domain, define the residual by A E zero x minus E zero A zero x. We require this expression to agree with a bounded map R from the trial coordinate space into H.

This bounded extension is what allows us to measure a residual in operator or ideal norms. The domain equality ensures that we haven't written down an expression that is undefined on half of its terms.

Because the exact complement reduces A, its coordinate map also respects the operator domain: applying A in H and then taking the complementary coordinate agrees with applying Lambda one to that coordinate.

That is the second domain fact we'll need.

### Compress the residual and find the Sylvester equation

Define X by first applying E zero and then taking the F one adjoint coordinate. In words, X reports how much each trial vector lies in the exact complementary subspace.

This map runs from the trial coordinate space into the complementary coordinate space. It is bounded.

Take an input x in the domain of the trial operator A zero. The residual identity says that A E zero x minus E zero A zero x equals R x.

Apply F one adjoint. The second term becomes X A zero x. The first becomes Lambda one X x, because the complement is reducing and the domain condition makes that composition legal.

The right-hand side becomes F one adjoint R x.

Thus Lambda one X minus X A zero equals F one adjoint R, as an equation on the domain of A zero.

This is exactly the scalar equation from the plane, now with operators between Hilbert spaces.

### Use the spectral gap to control X

Suppose the trial operator A zero and the complementary operator Lambda one satisfy a positive form-bounded Sylvester gap condition with parameter delta.

The allowed configurations include ordered half-line separation and the specified interval-versus-exterior case. Mere disjointness of two spectra is not enough for this particular constant-one symmetric-ideal estimate.

Also assume we're using a symmetric ideal family with Ky Fan dominance and that the bounded residual R belongs to this ideal.

The unbounded Sylvester theorem now says that X belongs to the ideal and that delta times its gauge is at most the gauge of F one adjoint R.

But F one is an isometry. Its adjoint is a contraction. Composing the residual with it cannot increase an ideal gauge.

Therefore delta times the gauge of X is at most the gauge of R.

That is the abstract version of five times the complementary coordinate being bounded by the vertical residual.

We still need to convert the possibly scaled trial coordinates into actual angle geometry.

### Remove the coordinate scaling

Take the polar decomposition of E zero. It factors as an isometry U followed by the positive modulus of E zero.

Because the trial map has lower bound epsilon, its modulus has a bounded inverse with norm at most one divided by epsilon.

U is the normalized coordinate map onto the trial subspace. Scaling E zero by two may change its modulus, but U still represents the same geometric line or subspace.

Recall that X equals F one adjoint E zero. Substitute the polar decomposition of E zero. Then X equals F one adjoint U followed by the modulus.

Multiply on the right by the inverse modulus. We obtain F one adjoint U as X followed by that bounded inverse.

The ideal-composition inequality gives: the gauge of F one adjoint U is at most one divided by epsilon times the gauge of X.

Combine this with the Sylvester bound. The conclusion is that delta times epsilon times the gauge of F one adjoint U is at most the gauge of R.

In our scaled plane example, delta is five, epsilon is two, and F one adjoint U is one half. The left-hand side is five. The residual norm is five. Equality is restored, and the angle no longer depends on the chosen coordinate scale.

### Recognize the directed sine

Let P project onto the exact target subspace. The component of the normalized trial map U outside that space is the complementary projection, one minus P, applied to U.

For a unit vector along a trial line, the length of that component is exactly the sine of the angle to the exact line.

In more dimensions, the corresponding positive modulus records the directed sine geometry of the trial subspace relative to the exact subspace.

Why can we use F one adjoint U to measure the same thing? Because F one provides isometric coordinates on the exact complement. Taking the Gram operator of F one adjoint U gives U adjoint times one minus P times U. The Gram operator of the ambient complementary map, one minus P applied to U, is exactly the same.

So both maps have the same modulus. The symmetric ideal gauge does not change when a map is replaced by its modulus, even if its source and target spaces differ.

Thus the estimate for F one adjoint U is precisely an estimate for the directed sine representative.

### What the theorem really says

The full statement is now visible.

We begin with a self-adjoint ambient operator, an exact reducing decomposition, a trial map with a positive lower frame bound, a self-adjoint trial operator, and a bounded residual satisfying the common-domain identity.

We assume a positive allowed gap between the trial operator and the exact complementary operator. In a symmetric ideal family with Ky Fan dominance, if the residual belongs to that ideal, then the directed sine belongs as well.

Its gauge, multiplied by the gap and by the lower frame bound, is at most the gauge of the residual.

The plane example shows why each factor is present: the gap converts complementary error into displacement, and the frame bound converts coordinates into geometry.

The proof's main operation is also simple to describe. Take only the part of the residual pointing into the wrong spectral subspace, solve a domain-aware Sylvester equation for that component, and normalize the trial map to measure a true angle.

A small residual alone does not identify which spectral subspace the trial map approximates. The gap hypothesis must separate the trial spectrum from the exact complement. With that separation and the domain conditions in place, the sine estimate follows.

## Proof practicum: reconstruct the 1970 theory

The residual calculation we have just developed is the starting point for a reconstruction of the wider theory. In the two-by-two example, the residual had length two and a half, the unwanted spectral gap was five, and the sine of the angle was one half. We can now use the roles of those three quantities to organize the theorem families.

Reconstruct the calculation without memorizing an inequality. First isolate the trial vector's component in the unwanted eigenspace. Second observe that applying the operator multiplies that component by five. Third write the residual equation and solve for the unwanted component. Fourth recognize that its length is the sine of the principal angle. The geometry, algebra and spectral gap each have one distinct job.

The original Davis–Kahan theory extends this pattern to multiple directions, different norms, and several kinds of spectral separation. An ambient-angle theorem needs both directions of leakage; the double-angle theorem uses reflection and has a branch ambiguity; the tangent theorem requires a graph condition. Infinite-dimensional results need operator domains and legitimate approximation arguments.

We will reconstruct these results as connected mathematics, checking their actual hypotheses rather than moving symbolically from one theorem name to another. A finite example supplies the intuition, while the formal companion records the exact equations and the strengthened assumptions needed for broader conclusions.

### Stage one: identify the correct geometric data

Let H be a finite-dimensional real or complex inner product space. Let A be self-adjoint, and let U be an A-invariant subspace. Because A is self-adjoint, U's orthogonal complement is invariant as well. Write P for orthogonal projection onto U, and Q for projection onto a trial subspace V of dimension d.

Choose an orthonormal coordinate embedding E from d-dimensional coordinate space into H, with range V. Choose an orthonormal embedding F into the exact orthogonal complement of U. The columns of F need to span that complement. We can then write F times F adjoint for the projection onto U perpendicular.

Your first task is to express the directed sine-angle operator using E and F. The answer is to form X equal to F adjoint E. Compute its Gram operator: X adjoint X equals E adjoint times the projection onto U perpendicular, times E. The eigenvalues of this positive operator are the squared sines of the directed principal angles from V to U. Therefore the singular values of X are the principal sines.

This identity is the geometric bridge. A bound on X in an operator or unitarily invariant norm is a bound on the trial space's angular leakage. Notice that if V and U have unequal dimensions, the directed sine list can contain additional right-angle directions. One must then say which direction of comparison is intended.

### Stage two: derive the residual equation

Form the Rayleigh–Ritz compression A zero, equal to E adjoint A E. Define the residual R to be A E minus E A zero. Since E adjoint R equals zero, R is orthogonal to the trial space. That is Galerkin orthogonality. It does not mean R is orthogonal to the exact subspace.

Define Lambda one as F adjoint A F, the restriction of A to U perpendicular expressed in orthonormal coordinates. Calculate F adjoint R. First, F adjoint R equals F adjoint A E minus F adjoint E A zero.

Because U perpendicular reduces A, the first term equals Lambda one times F adjoint E. Put X in both places. You obtain the complementary Sylvester equation: Lambda one X minus X A zero equals F adjoint R.

This calculation is short, but it carries much of the theorem. We have converted the unknown geometric overlap X into the solution of a linear operator equation. The forcing term is a compression of the residual. The spectral gap will determine whether that equation has a controlled inverse.

### Stage three: choose and prove the gap estimate

Suppose the spectrum of A zero is entirely below a real number a, while the spectrum of Lambda one is at least delta above a. Here delta is strictly positive. This is an ordered spectral separation hypothesis, stronger than merely requiring every cross-pair of eigenvalues to have distance at least delta.

Can you derive a bound on X? For bounded self-adjoint matrices, write the Sylvester inverse as an integral. If Lambda one lies above and A zero below, then X equals the integral from zero to infinity of the exponential of negative t Lambda one, times F adjoint R, times the exponential of t A zero. To make decay explicit, insert the same scalar center a with opposite signs in the two exponentials. The product bound then decays at least as the exponential of negative delta t.

Integrating gives the operator-norm inequality: delta times the norm of X is at most the norm of F adjoint R. Since F adjoint is a contraction, the latter is at most the norm of R. And because the singular values of X are the directed principal sines, we have proved the single-angle sine theorem for this ordered-gap finite-dimensional setting.

If instead we assume only that every eigenvalue of Lambda one is separated from every eigenvalue of A zero by delta, diagonalize the blocks and solve the Sylvester equation entry by entry. Each entry of X is the corresponding entry of F adjoint R divided by an eigenvalue difference. Squaring and summing gives the same constant-one estimate in Frobenius norm.

The entrywise argument yields a constant-one Frobenius estimate, but not the corresponding operator-norm estimate. The distinction between ordered and pairwise gaps, and between operator and Frobenius norms, is part of the theorem's mathematical content.

### Stage four: test a sharp two-dimensional case

Take A diagonal with entries zero and delta. Let the exact subspace U be the first coordinate axis. Take the trial unit vector E to have coordinates cosine theta and sine theta, for an angle strictly between zero and ninety degrees.

The compressed Rayleigh quotient A zero is delta times sine squared theta. The exact complementary block Lambda one is delta. The difference between their spectral values is delta times cosine squared theta. The complementary overlap X equals sine theta.

Calculate the residual's component along the second coordinate. It is delta times sine theta times cosine squared theta. Therefore the Sylvester equation has equality: the compressed gap, which is delta cosine squared theta, times the sine theta overlap equals that residual component.

This example teaches two checks. First, never substitute the original eigenvalue gap delta for the actual gap between Lambda one and the Ritz value A zero without verifying the needed inequality. Second, the compressed residual is not automatically the whole residual. In this example the full residual also has a component in the original exact subspace.

The standard two-level example, with every admissibility hypothesis checked, attains equality for the sharp sine, tangent, and doubled-angle estimates. Equality under the actual hypotheses proves that their coefficient one cannot be reduced; a numerical coincidence without those checks does not.

### Stage five: pass from a single angle to norm generality

Suppose a theorem claims a bound in every unitarily invariant norm, wherever that norm is defined. What must we prove beyond the operator-norm case?

We need control of the entire singular-value sequence, not just its largest member. In finite dimensions, the useful language is Ky Fan sums: for each positive integer k, sum the largest k singular values. An all-prefix comparison yields weak majorization. Under the hypotheses of the symmetric-gauge theorem, weak majorization gives the desired unitarily invariant norm inequality.

For the ambient sine theorem in Section six of the 1970 Davis–Kahan paper, there is another issue. One directed residual equation only controls one crossed block. To control the full ambient sine operator, derive both crossed Sylvester equations. Compare their block singular values, combine the estimates using the direct-sum Ky Fan lemma, and use the reflection-averaging pinching lemma to contract the relevant perturbation blocks.

In infinite dimensions, an arbitrary ideal norm may be infinite on a bounded operator. An ideal-norm inequality must establish the relevant membership, or assume it for the perturbation and derive it for the angle operator, before comparing finite ideal gauges.

### Stage six: reconstruct the other three angle families

Now explain how the proof changes for tangent theta. Represent the trial subspace as a graph over the exact subspace, provided the projection from the trial space to the exact space is invertible with bounded inverse. The graph map is the sine overlap divided by the cosine overlap. Its singular values are the tangents of the principal angles. An ordered Ritz gap and the appropriate residual equation then control the graph map. The invertibility assumption or a theorem deriving it cannot be omitted.

For the sine-of-twice-theta theorem, introduce the block reflection associated with one subspace. Reflecting the other subspace across it doubles the principal-plane angles, after the appropriate angular functional calculus. Off-diagonal perturbations anticommute with the reference reflection. This produces a doubled-angle residual with a factor of two. The doubled-angle sine estimate may be valid without knowing that the original angle is small.

For the tangent-of-twice-theta theorem, small-angle branch information matters. Tangent of twice an angle changes sign or becomes singular at forty-five degrees. Under the required ordered-gap, off-diagonal, and spectral-selection conditions, the appropriate reducing subspace stays in the small-angle branch and one obtains the sharp doubled-angle tangent inequality. Without that selection argument, a bound on sine of twice an angle could describe an angle near ninety degrees just as well as one near zero.

These are four theorem families, with different geometry and different gap requirements. A proof that establishes one does not automatically establish the others.

### Stage seven: restore the unbounded Hilbert-space machinery

In a Hilbert space, A may be self-adjoint and unbounded. Before writing A E, you must state that every trial vector lies in the domain of A. The exact reducing projection must preserve the domain, and the restricted operators have their own domains. For a Sylvester equation involving two unbounded blocks, the domain of X's input and the requirement that its image land in the other block's domain are essential.

Use bounded spectral cutoffs to make each intermediate calculation legal. Prove that cutoff vectors converge strongly, and that the operator images converge on vectors in the graph domain. Then pass through a closedness or resolvent argument to recover the original operator equation and norm estimate.

You will also need the spectral measure and Borel functional calculus to discuss reducing subspaces when the operator has continuous spectrum. In particular, a multiplication operator can have a substantial spectral projection even when it has no eigenvector for almost every individual spectral value. Finite eigenbasis calculations cannot be used as a substitute for that theory.

Finally, treat real and complex Hilbert spaces explicitly. The complex spectral calculus may be used after complexifying a real operator, but the operator norm, spectral restrictions, domains, and relevant ideal gauges must be transported back correctly. A theorem proved over complex scalars is not automatically a theorem over real scalars without that descent.

### Stage eight: close the original paper faithfully

The 1970 paper also develops direct rotation and an extremal claim about displacement. Reconstruct the polar intertwiner of two projections, state the crossed-defect matching criterion at right angles, and distinguish the canonical polar rotation from arbitrary unitary transports.

Then separate three objectives: displacement restricted to the source subspace, squared whole-space displacement, and unsquared whole-space displacement. The first two objectives admit valid optimality theorems under their stated hypotheses. The broad unsquared full-space claim of Proposition four point four is false; the explicit real four-dimensional example supplies the counterexample. The false proposition cannot be used in a proof.

The free-beam example is another endpoint test. To reproduce it, construct the fourth-order self-adjoint operator with its boundary conditions, compute the Ritz compression and residual matrices, verify the spectral separation, and apply the angle estimates. Its finite trial matrix does not erase the unbounded operator-domain obligations.

Finally, the original paper's Section ten asks questions that are broader than the results established in the main body. The established cases, counterexamples, and open questions must remain distinct; an analogy alone supplies no general theorem.

### Your final proof certificate

A complete reconstruction should contain, in order: the ambient Hilbert-space and scalar-field assumptions; the domains of all operators; the exact and trial subspaces; the residual and compressed blocks; the correct spectral-gap predicate; the Sylvester inverse and its norm class; the Gram identity identifying the angle; and the ideal membership and cutoff arguments where needed.

You should be able to present the finite single-angle proof on a blank page, then explain which pieces must be replaced or strengthened for the ambient, doubled-angle, and infinite-dimensional theorems. You should also be able to point to the direct-rotation correction and the free-beam example without confusing them with the hypotheses of the sine theorem.

The resulting inequalities are meaningful only with their spectral and norm hypotheses. A complete reconstruction explains the residual equation, the gap estimate, the geometry of angles, and the exact scope of each norm and optimality claim.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### A full proof-readiness assembly

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `011000` orthogonal projections, `021000` compressions, `042000–046000` principal-angle geometry, `093000–094000` unbounded Sylvester estimates, `098000–101000` operator ideals, `102000–104000` real complexification and transfer. **Placement:** advanced capstone after the residual and angle-theorem routes; review the matching and beam topics for the final reconstruction.

---

#### Companion: mathematics and Lean correspondence (display only)

Let `A` be self-adjoint on ambient `H`, let `F₀,F₁` define an exact reducing orthogonal decomposition, and let `E₀` have lower bound `‖E₀x‖ ≥ ε‖x‖` for `ε>0`. Require `HasCommonDomain A A₀ E₀`, the complement-domain intertwining property for `F₁` and `Λ₁`, and a bounded residual `R` agreeing with `A E₀−E₀ A₀` on the common domain. Then `X=F₁*E₀` satisfies the domain-aware Sylvester equation `Λ₁ X−X A₀=F₁*R`. A compatible unbounded gap `δ>0`, a symmetric ideal with Ky Fan dominance, and `Mem R` give `Mem X` and `δ gauge(X) ≤ gauge(R)`. The polar normalization `E₀=U|E₀|` with `‖|E₀|⁻¹‖≤1/ε` yields `δε gauge(F₁*U) ≤ gauge(R)`. Since `(F₁*U)* (F₁*U)=U* (I−P) U`, its modulus is the directed sine operator of the trial range relative to `P=F₀F₀*`.

##### Worked example: gap, normalization, and directed sine

On \(H=\mathbb R^2\), let \(A=\operatorname{diag}(0,5)\) and target \(P=\operatorname{diag}(1,0)\). Define \(u=(\sqrt3/2,1/2)\), \(E_0t=2tu\), and \(A_0=0\). With \(F_1t=(0,t)\), the complementary operator is \(\Lambda_1=5I\), the form gap is \(\delta=5\), and the lower trial-frame bound is \(\varepsilon=2\).

The residual is \(Rt=A E_0t=(0,5t)\), so \(\|R\|=5\). The complementary block is \(X=F_1^*E_0=I\), giving \(\Lambda_1X-XA_0=5I=F_1^*R\). The polar-normalized trial isometry is \(Ut=tu\), and \(F_1^*U=\tfrac12 I\). Thus \(\delta\varepsilon\|F_1^*U\|=5\cdot2\cdot\tfrac12=5=\|R\|\). The directed sine is \(\sin(30^\circ)=1/2\).

##### Actual Lean source declarations

`DavisKahan/Sources/DavisKahan1970/SineTheta/CommonDomain.lean` — `HasCommonDomain` (exact declaration header; proof omitted):

```lean
def HasCommonDomain
    (A : E →ₗ.[𝕜] E)
    (A₀ : F →ₗ.[𝕜] F)
    (X : F →L[𝕜] E) : Prop :=
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/CommonDomainTheorems.lean` — `toUnboundedSinThetaData` (exact declaration header; proof omitted):

```lean
noncomputable def toUnboundedSinThetaData
    {𝕜 : Type u} [RCLike 𝕜]
    {E F G H : Type v}
    [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E]
    [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F]
    [NormedAddCommGroup G] [InnerProductSpace 𝕜 G] [CompleteSpace G]
    [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]
    (P : CommonDomainSinThetaData 𝕜 E F G H) :
    UnboundedSinThetaData (𝕜 := 𝕜) (E := E) (F := F) (G := G) :=
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/CommonDomainTheorems.lean` — `result_every_unitarilyInvariantNorm` (exact declaration header; proof omitted):

```lean
theorem result_every_unitarilyInvariantNorm
    (P : RealCommonDomainTheorem61Data
      (E := E) (F := F) (G := G) (H := H))
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/ScalarGeneric.lean` — `sinTheta_unbounded_formGap_idealFamily_rclike` (exact declaration header; proof omitted):

```lean
theorem sinTheta_unbounded_formGap_idealFamily_rclike
    (N : TauCeti.SymmetricOperatorIdealFamily 𝕜)
    [N.toOperatorIdealFamily.IsKyFanDominant]
    (D : UnboundedSinThetaData (𝕜 := 𝕜) (E := E) (F := F) (G := G))
```

**Type and hypothesis map.** The exact common-domain predicate identifies the pullback of the ambient operator domain under the trial map with `A₀.domain`. The conversion to `UnboundedSinThetaData` preserves the source residual. The real common-domain Theorem 6.1 conclusion requires a lower trial-frame bound `ε`, a form-bounded gap `δ`, self-adjoint and exact-decomposition data, a sine representative and residual membership in a symmetric norm family. The scalar-generic internal theorem is written for an isometric trial map, before the paper-facing lower-frame normalization. It must not be read as dropping the `ε` hypothesis from the external theorem.

These Lean snippets are copied exactly from the supplied DKPS repository snapshot. The narration is an independent mathematical derivation; this appendix does not claim that the narrated text was compiled in Lean. Foundational results currently in `ForTauCeti` may have been developed in DKPS before upstreaming.

### Proof practicum: reconstruct the 1970 theory

**Draft status:** audio-first final proof practicum. **Prerequisites:** `001000–148000`, particularly `049000–051000`, `064000–071000`, `083000–105000`, `108000–129000` and `130000–141000`. **Course endpoint.**

---

#### Display-only proof certificate and Lean correspondence

##### Finite directed sine derivation

Let \(A=A^*\) act on finite-dimensional \(H\). Let \(U\) be reducing for \(A\), \(E:\mathbb K^d\to H\) an isometry with trial range \(V\), and \(F:\mathbb K^m\to H\) an isometry onto \(U^\perp\). Define

\[
A_0=E^*AE,\quad R=AE-EA_0,\quad
\Lambda_1=F^*AF,\quad X=F^*E.
\]

Then

\[
E^*R=0,\qquad F^*R=\Lambda_1X-XA_0,\qquad
X^*X=E^*P_{U^\perp}E.
\]

The singular values of \(X\) are the *directed* principal sines from \(V\) to \(U\). If the spectra of \(\Lambda_1\) and \(A_0\) have a suitably ordered gap \(\delta>0\), the self-adjoint Sylvester inverse obeys

\[
\delta\|X\|\le\|F^*R\|\le\|R\|.
\]

For a merely pairwise cross-spectral gap, diagonal entry division gives \(\delta\|X\|_F\le\|F^*R\|_F\), not a general constant-one operator-norm conclusion.

##### Two-dimensional consistency check

Take \(A=\mathrm{diag}(0,\delta)\), \(U=\mathrm{span}(e_1)\), and \(E=(\cos\theta,\sin\theta)^\top\), with \(0<\theta<\pi/2\). Then \(A_0=\delta\sin^2\theta\), \(\Lambda_1=\delta\), \(X=\sin\theta\), and \(F^*R=\delta\sin\theta\cos^2\theta\). The *actual* ordered separation between the two compressed scalars is \(\delta\cos^2\theta\).

##### Infinite-dimensional obligations

Replace unrestricted matrix multiplication with explicit domain inclusions. Require reducing projections to preserve the closed operator's domain and use spectral cutoffs and strong/graph convergence as appropriate. For a unitarily invariant ideal, show membership of the angle operator and perturbation in the ideal before applying its gauge. In the ambient Section 6 theorem, require both crossed-gap conditions and use the all-prefix direct-sum lemma and reflection pinching.

##### Practicum checkpoints

1. Derive \(F^*R=\Lambda_1X-XA_0\) without treating the Ritz frame as an exact invariant subspace.
2. State which gap controls operator norm and which controls Frobenius norm; construct a counterexample to an unjustified strengthening.
3. Identify the exact operator whose singular values are the directed principal sines.
4. Restore the second crossed block, Ky Fan comparison, pinching, and ideal membership for the ambient result.
5. State transversality for tangent bounds and spectral branch selection for double-angle bounds.
6. Explain where spectral cutoffs, graph domains, and real/complex transfer enter.
7. Distinguish the valid direct-rotation minima from the false printed Proposition 4.4, and verify the beam's boundary conditions before using its Ritz matrix.

#### Exact Lean declaration excerpts

**`proposition6_1_printedGap_sourceExact_complex`** — `DavisKahan/Sources/DavisKahan1970/Section6SourceScope.lean` (exact declaration header; proof body omitted):

```lean
theorem proposition6_1_printedGap_sourceExact_complex
    {E : Type v} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [TopologicalSpace.SeparableSpace E]
    (N : NormalizedUnitaryInvariantNorm.{0, v} ℂ)
    {A B : E →L[ℂ] E} (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {U V : Submodule ℂ E} [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hU : Submodule.IsReducing U A) (hV : Submodule.IsReducing V B)
    {δ : ℝ} (hδ : 0 < δ)
    {β α β' α' : ℝ} (hβα : β ≤ α) (hβα' : β' ≤ α')
    (hgapUV : DavisKahan.Sylvester.RealSpectrumIntervalExteriorGap
      (DavisKahanExt.PartialMap.boundedReducingBlock A U hU)
      (DavisKahanExt.PartialMap.boundedReducingBlockCompl B V hV) β α δ)
    (hgapVU : DavisKahan.Sylvester.RealSpectrumIntervalExteriorGap
      (DavisKahanExt.PartialMap.boundedReducingBlock B V hV)
      (DavisKahanExt.PartialMap.boundedReducingBlockCompl A U hU) β' α' δ)
    (hMem : N.Mem (B - A)) :
    N.Mem (cfc Real.sin (DavisKahan.Angle.angleOperator U V)) ∧
      δ * N.gauge (cfc Real.sin (DavisKahan.Angle.angleOperator U V)) ≤ N.gauge (B - A) :=
```

**`lemma61_all_kyFan`** — `DavisKahan/Sources/DavisKahan1970/SineTheta/Lemma61.lean` (exact declaration header; proof body omitted):

```lean
theorem lemma61_all_kyFan
    (Ω Γ : Submodule 𝕜 E)
    [Ω.HasOrthogonalProjection] [Γ.HasOrthogonalProjection]
    (K Ktilde L Ltilde : E →L[𝕜] E)
    (h₀ : ∀ k,
      ((projectionBlock Ω Γ K).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ω Γ L).kyFanGauge k : ℝ))
    (h₁ : ∀ k,
      ((projectionBlock Ωᗮ Γᗮ Ktilde).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ωᗮ Γᗮ Ltilde).kyFanGauge k : ℝ)) :
    ∀ k,
      ((projectionBlock Ω Γ K +
            projectionBlock Ωᗮ Γᗮ Ktilde).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ω Γ L +
            projectionBlock Ωᗮ Γᗮ Ltilde).kyFanGauge k : ℝ) := by
```

**`lemma6_2_separable`** — `DavisKahan/Sources/DavisKahan1970/Section6SourceScope.lean` (exact declaration header; proof body omitted):

```lean
theorem lemma6_2_separable {𝕜 : Type} [RCLike 𝕜]
    [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E]
    [TopologicalSpace.SeparableSpace E]
    (N : NormalizedUnitaryInvariantNorm.{0, v} 𝕜)
    (U V : Submodule 𝕜 E) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    {K : E →L[𝕜] E} (hK : N.Mem K) :
    N.Mem (diagonalPair U V K) ∧ N.gauge (diagonalPair U V K) ≤ N.gauge K :=
```

**`tanTheta_residual_le`** — `DavisKahan/FiniteDimensional/Residual/AngleEmbeddings.lean` (exact declaration header; proof body omitted):

```lean
theorem tanTheta_residual_le
    (N : UnitarilyInvariantSeminorm 𝕜 F E)
    {A : E →ₗ[𝕜] E} (hA : A.IsSymmetric) {U : Submodule 𝕜 E}
    [U.HasOrthogonalProjection] (hU : (U ∈ Module.End.invtSubmodule A))
    (X : F →ₗᵢ[𝕜] E) {M : F →ₗ[𝕜] F} (hM : M.IsSymmetric)
    (hGalerkin : M = compression A X)
    {δ : ℝ} (hδ : 0 < δ) (hgap : OrderedGap M ⊤ A Uᗮ δ) :
    δ * N (tanThetaEmbedding U X) ≤ N (residual A X M) :=
```

**`sinTwoTheta_residual_le`** — `DavisKahan/FiniteDimensional/DoubleAngle/SinTwoThetaResidual.lean` (exact declaration header; proof body omitted):

```lean
theorem sinTwoTheta_residual_le
    (N : UnitarilyInvariantSeminorm 𝕜 F E)
    {A : E →ₗ[𝕜] E} (hA : A.IsSymmetric) {U : Submodule 𝕜 E}
    [U.HasOrthogonalProjection] (hU : (U ∈ Module.End.invtSubmodule A))
    (X : F →ₗᵢ[𝕜] E) {M : F →ₗ[𝕜] F} (hM : M.IsSymmetric)
    {a b δ : ℝ} (hδ : 0 < δ)
    (hMspec : Module.End.PointSpectrumIn M ⊤ (Set.Icc a b))
    (hAspec : Module.End.PointSpectrumIn A Uᗮ {lam | lam ∉ Set.Ioo (a - δ) (b + δ)}) :
    δ * N (sinTwoThetaEmbedding U X) ≤ 2 * N (residual A X M) := by
```

**`shortRotation_fullDisplacement_refuted`** — `DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` (exact declaration header; proof body omitted):

```lean
theorem shortRotation_fullDisplacement_refuted :
    ∃ (U V : Submodule ℝ (EuclideanSpace ℝ (Fin 4)))
      (hacute : Submodule.IsAcute U V)
      (W : EuclideanSpace ℝ (Fin 4) ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin 4)),
      U.map W.toLinearMap = V ∧
      Submodule.principalAngles U V 0 ≤ Real.pi / 3 ∧
      (LinearMap.id - W.toLinearMap).kyFanSum 4 <
        (LinearMap.id - (directRotation U V hacute).toLinearMap).kyFanSum 4 :=
```

**`sinTheta_model_equality`** — `DavisKahan/FiniteDimensional/Sharpness.lean` (exact declaration header; proof body omitted):

```lean
theorem sinTheta_model_equality
    (N : UnitarilyInvariantSeminorm 𝕜 (Plane 𝕜) (Plane 𝕜))
    {a b θ : ℝ} (hab : a < b) (hθ0 : 0 ≤ θ) (hθ1 : θ < Real.pi / 2) :
    (b - a) * N ((Submodule.sinAngleOperator (modelSubspace (𝕜 := 𝕜)) (rotatedModelSubspace (𝕜 := 𝕜) θ)).toLinearMap) =
```
