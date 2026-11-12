# 009000 — Ordered separation and Theorem 5.2

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** sylvester. **Audience:** the Sylvester equation and Theorem 5.1, unbounded self-adjoint operators and form bounds, functional calculus.

<!-- BEGIN SPOKEN LECTURE -->

Ordered separation and Theorem 5.2

The window argument for the Sylvester equation needs one bounded coefficient. When both coefficients are unbounded, as when one spectrum runs up to plus infinity and the other down to minus infinity, there is no window, but there may still be a cut: everything in one spectrum lies above everything in the other, with a gap of delta between. Davis and Kahan's Theorem 5.2 handles this case. The proof given here replaces division by a spectral difference with an integral of decaying exponentials, a standard representation of the solution, and that integral is worth understanding on its own.

Here is what we will establish. Let C and B be self-adjoint, possibly unbounded, with C at least gamma plus delta and B at most gamma, in the sense of quadratic forms. Let X and Y be bounded, with X mapping the domain of B into the domain of C, and C X minus X B equal to Y there. Then delta times the norm of X is at most the norm of Y, in every unitarily invariant norm, and moreover X belongs to the ideal whenever Y does. The solution is the integral, from zero to infinity, of e to the minus t C, times Y, times e to the t B; the ordering makes the integrand decay like e to the minus t delta. The same result with the roles of C and B reversed covers the other orientation. Together with Theorem 5.1, this gives the sine-theta inequality for every gap configuration the theorem allows.

The scalar identity

Start with numbers. Suppose c and b are real, with c greater than b. Then one over c minus b equals the integral from zero to infinity of e to the minus t times c minus b, with respect to t. That is just the integral of a decaying exponential.

Now write the integrand as a product: e to the minus t c, times e to the t b. The first factor decays because c is large, the second may grow but only at rate b, and the product decays at rate c minus b. If c minus b is at least delta, the integrand is at most e to the minus t delta, and the integral is at most one over delta.

So the Sylvester equation in one dimension, c x minus x b equals y, has solution x equal to the integral of e to the minus t c times y times e to the t b. For example, if c is five and b is two, then x equals y over three, and the integral of e to the minus three t from zero to infinity is one third.

This form generalizes to operators in a way that division does not. For operators, we cannot divide Y by C minus B, because C and B act on different sides of X. But we can multiply Y on the left by e to the minus t C and on the right by e to the t B, and integrate.

The operator integral

Let C and B be bounded self-adjoint operators first, with C at least gamma plus delta and B at most gamma. Functional calculus defines the exponentials. Because the spectrum of C lies at or above gamma plus delta, the operator e to the minus t C has norm at most e to the minus t times gamma plus delta, for t at least zero. Because the spectrum of B lies at or below gamma, e to the t B has norm at most e to the t gamma. So the product e to the minus t C, times Y, times e to the t B, has norm at most e to the minus t delta times the norm of Y, and the same bound holds in any unitarily invariant norm, by the contraction law.

Define X as the integral from zero to infinity of that product. It converges, and its norm is at most the integral of e to the minus t delta times the norm of Y, which is the norm of Y divided by delta.

Does this X solve the equation? Differentiate the integrand with respect to t. The derivative of e to the minus t C is minus C e to the minus t C, and the derivative of e to the t B is e to the t B times B. So the derivative of the integrand is minus C times the integrand, plus the integrand times B. Integrating from zero to infinity, the integral of the derivative is the value at infinity minus the value at zero. At infinity the integrand vanishes; at zero it is Y. So minus C X plus X B equals minus Y, which is C X minus X B equals Y.

Uniqueness follows from the same estimate. If two solutions existed, their difference would solve the equation with Y equal to zero, and the estimate would force its norm to be at most zero. So every bounded solution is this integral, and every bounded solution satisfies delta times N of X at most N of Y.

Why no constant is lost

In the diagonal case, the integral reproduces division. If C and B are diagonal with entries c i and b j, the integrand has entries e to the minus t c i, times y i j, times e to the t b j, and integrating gives y i j over c i minus b j. So nothing new is computed. What is new is the estimate. Entrywise division by c i minus b j can enlarge the operator norm, as Davis and Kahan's two by two example showed when the spectra interlaced. When the spectra are ordered, each multiplier one over c i minus b j is an integral of products of a decaying exponential depending only on i and a decaying exponential depending only on j. Each such product is the composition of Y with two contractions, multiplied by e to the minus t delta. The operator norm survives composition with contractions, so it survives the integral, with constant one.

For interlaced spectra the integral representation fails: some differences c i minus b j are negative, and for those the integrand grows instead of decaying. One could integrate those entries backward in time, but no single direction of time makes every entry decay, and splitting the entries is exactly what destroys the operator-norm estimate.

Unbounded coefficients

Now let C and B be unbounded. The hypothesis C at least gamma plus delta means: for every x in the domain of C, the inner product of C x with x is at least gamma plus delta times the squared length of x. Similarly B at most gamma is an upper form bound on the domain of B. For self-adjoint operators these are the same as spectral bounds on half-lines.

The exponentials are still bounded. The function e to the minus t lambda is bounded on the half-line where lambda is at least gamma plus delta, by e to the minus t times gamma plus delta, so e to the minus t C is a bounded operator by functional calculus, even though C is not. The same holds for e to the t B on the half-line where B lives. So the integral still converges, and the estimate still holds.

The work lies in the equation. C X minus X B is only defined on the domain of B, and only if X maps that domain into the domain of C. Theorem 5.2 assumes exactly this: X and Y are bounded, X carries the domain of B into the domain of C, and C X minus X B equals Y on the domain of B. The differentiation step then has to be carried out on vectors in the domain, and the boundary terms checked on those vectors.

A concrete case: on square-summable sequences indexed from one, let C multiply the n-th entry by n plus delta, and B multiply the n-th entry by minus n. Then C is at least one plus delta and B is at most minus one, so with gamma equal to minus one, C is at least gamma plus two plus delta. Both operators are unbounded. Neither has a bounded inverse of the size Theorem 5.1 needs together with a bounded partner, because neither partner is bounded. Theorem 5.2 applies, with gap two plus delta.

Sharpness and orientation

The constant one is attained. In one dimension, with c exactly gamma plus delta and b exactly gamma, x equals y over delta exactly. Taking a direct sum of such one-dimensional examples gives equality in every unitarily invariant norm at once.

The orientation matters only up to symmetry. If instead C is at most gamma and B is at least gamma plus delta, integrate in the other direction, from minus infinity to zero, with e to the minus t C and e to the t B decaying as t goes to minus infinity; or take adjoints of the equation, which exchanges the roles of the two coefficients. Either way, delta times N of X is at most N of Y.

What Theorem 5.2 gives for the sine-theta theorem

The sine-theta theorem's ordered hypothesis says: for some b, the trial operator A zero is at least b plus delta and Lambda one is at most b, or the reverse. The Sylvester equation is Lambda one X minus X A zero equals F one star R. In the reverse orientation, with A zero at most b and Lambda one at least b plus delta, Theorem 5.2 applies with C equal to Lambda one and B equal to A zero. In the first orientation, apply the reversed form. Either way, delta times N of X is at most N of F one star R, which is at most N of R, and N of X equals N of the sine of Theta zero.

So the sine-theta inequality with constant one holds under the interval and exterior hypothesis, by Theorem 5.1 after shifting, and under the ordered hypothesis, by Theorem 5.2, including when both A zero and Lambda one are unbounded.

The argument gives slightly more than the printed theorem states: X belongs to the ideal of the norm whenever Y does, because every truncated integral does and the estimate controls the limit. Membership transfer is exactly what the general Ky Fan dominance hypothesis does not supply on its own, so this is a real addition for the ordered case.

To summarize. The reciprocal of a positive gap is an integral of a decaying exponential, and the operator version of this identity solves the Sylvester equation: X is the integral of e to the minus t C times Y times e to the t B. When C lies above gamma plus delta and B below gamma, the integrand is bounded by e to the minus t delta times Y in every unitarily invariant norm, so delta times the norm of X is at most the norm of Y. The exponentials are bounded even for unbounded coefficients, so both coefficients may be unbounded, provided the equation holds on the appropriate domains. Interlaced spectra admit no single direction of decay, which is why only the window and cut shapes give constant one in the operator norm.

The integral method uses the order structure of the real line. It needs every point of one spectrum above every point of the other. Separation that wraps around, with unwanted spectrum on both sides, is handled by Theorem 5.1 instead, and only when the trial spectrum is bounded.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Theorem 5.2

\(C,B\) self-adjoint (possibly unbounded), \(C\ge(\gamma+\delta)I\), \(B\le\gamma I\) (forms on domains); \(X,Y\) bounded, \(X\operatorname{dom}B\subseteq\operatorname{dom}C\), \(CX-XB=Y\) on \(\operatorname{dom}B\). Then for every unitarily invariant (ideal) norm \(N\): \(\delta N(X)\le N(Y)\).

### Proof sketch

\[
\frac1{c-b}=\int_0^\infty e^{-t(c-b)}\,dt,\qquad
X=\int_0^\infty e^{-tC}\,Y\,e^{tB}\,dt,
\]
\(\|e^{-tC}\|\le e^{-t(\gamma+\delta)}\), \(\|e^{tB}\|\le e^{t\gamma}\Rightarrow N(e^{-tC}Ye^{tB})\le e^{-t\delta}N(Y)\Rightarrow N(X)\le N(Y)/\delta\).
\(\frac{d}{dt}\bigl(e^{-tC}Ye^{tB}\bigr)=-Ce^{-tC}Ye^{tB}+e^{-tC}Ye^{tB}B\); integrating gives \(-CX+XB=-Y\). Uniqueness from the estimate with \(Y=0\).

Diagonal check: entries \(y_{ij}\int_0^\infty e^{-t(c_i-b_j)}dt=y_{ij}/(c_i-b_j)\).
Example: \(Ce_n=(n+\delta)e_n\), \(Be_n=-ne_n\): \(C\ge1+\delta\), \(B\le-1\), gap \(2+\delta\).

### Lean correspondence

`DavisKahan/Sources/DavisKahan1970/Section5.lean`, `namespace TauCeti.DavisKahan1970`:

```lean
/-- **Davis--Kahan 1970, Theorem 5.2.**  For self-adjoint closed operators with the
source's ordering `A ≥ c + δ > c ≥ B`, a bounded solution of the Sylvester equation
`A X = X B + R` satisfies the sharp inequality `δ · N(X) ≤ N(R)` in every Fan-dominant
unitarily invariant ideal gauge, and `X` lies in the ideal whenever `R` does. ... -/
alias theorem5_2 :=
  DavisKahan.Sylvester.directOrderedSylvesterEngine_lowerUpper
```

**Mapping notes.**

- Lean's `A, B, X, R` are the lecture's \(C, B, X, Y\).
- The ordering is stated with `TauCeti.LinearPMap.SemiboundedBelow A (c + δ)` and `TauCeti.LinearPMap.SemiboundedAbove B c`.
- The docstring distinguishes this ordered branch from the interval/exterior theorem `unbounded_sylvester_intervalExterior_uiNorm_of_spectra` and notes the membership conclusion, which the printed theorem does not state.
- Real and symmetric-norming variants: `theorem5_2_kyFanDominant_real`, `theorem5_2_symmetricNorming_complex`, `theorem5_2_symmetricNorming_real`.
- The same file aliases (5.1) as `Inequality5_1` (Hilbert–Schmidt, with membership as a conclusion) and (5.2) as `Inequality5_2`; its docstring notes the paper's `‖·‖₁` is the operator norm.
