# 047000 — Spectral Projections: Filtering an Operator by Frequency

**Track:** Analysis from First Principles. **Background:** Orthogonal projections, self-adjoint operators, Borel sets, and L-two measure. **Question:** How can we select part of a spectrum when there is no eigenvector basis?

<!-- BEGIN SPOKEN LECTURE -->

# Spectral Projections: Filtering an Operator by Frequency

Imagine a recording that contains low and high tones. A filter that keeps only the low tones does not need to assign a separate name to every frequency. It needs a rule that distinguishes one region of frequencies from another. The result should be a projection: applying the same filter twice does nothing more than applying it once.

A spectral projection performs this kind of selection for a self-adjoint operator. It extracts the component of a vector associated with a chosen set of spectral values. For a finite self-adjoint matrix, the projection is just the sum of projections onto eigenspaces whose eigenvalues lie in that set. In infinite dimensions we need the same idea even when there are no eigenvectors.

## Begin with a matrix switch

Suppose a two-by-two self-adjoint matrix has eigenvalues one and three, with perpendicular eigenspaces. We can ask for the part of an input associated with spectral values below two. That filter keeps the eigenvector component at one and discards the component at three.

The filter is an orthogonal projection. It is self-adjoint, because it treats measurements symmetrically. It is idempotent, meaning its square equals itself. It is also positive, since the squared norm of the retained component is nonnegative.

If we select two disjoint spectral regions and apply both filters in succession, the result is zero. If we select a region and then its complement, the retained pieces add back to the original vector. These are exactly the algebraic rules we want in any dimension.

## Multiplication operators make the rule visible

Take A to be multiplication by t on square-integrable functions on the interval zero to one. For a chosen subset B of the interval, let E of B multiply a function by the indicator of B. In ordinary language, keep the function inside B and erase it outside B.

This is an orthogonal projection. Applying it twice is the same as once. Applying the projections for B and C in succession keeps only their intersection. Selecting the empty set gives the zero operator; selecting the whole interval gives the identity.

Even though A has no eigenvectors, these filters are perfectly meaningful. For the subset from zero to one half, E keeps the left half of a function. For the subset from one half to one, it keeps the right half. We have split a vector by spectral region without finding an eigenvector.

This example also reveals why spectral sets must be measurable. For arbitrary pathological subsets, multiplying by the indicator may not preserve the class of measurable functions we use to define L two. Borel subsets are a standard collection on which the spectral construction works.

## Countably many spectral bands

A finite sum of mutually perpendicular spectral projections behaves just like a finite sum of coordinate projections. But an operator's spectrum can require infinitely many bands. We therefore need countable additivity: if spectral sets are disjoint, the projection for their union is the strong limit of the sum of their projections.

The word strong means that, after applying the partial sums to any fixed vector, the resulting vectors converge in Hilbert-space norm. We do not demand operator-norm convergence of those partial sums. That distinction is necessary when infinitely many spectral pieces are present.

A rule assigning such projections to Borel sets is called a projection-valued measure, or PVM. It looks like a probability measure, but instead of producing a nonnegative number from a set, it produces an orthogonal projection. The analogy becomes exact only after we choose a vector and measure how much of it lies in the projected component.

## From projections to scalar measures

Fix a vector x and consider the squared norm of E of B applied to x. This quantity is nonnegative. It is zero if x has no component in the region B, and the squared norm of x if B is the entire real line.

For disjoint regions, the squared norms of their projected components add, because the components are orthogonal. Thus every vector x produces an ordinary finite measure on the spectral line. This is called its scalar spectral measure.

For the interval multiplication operator, the measure of B is the integral over B of the squared magnitude of x. A vector concentrated on the left side places most of its spectral mass there; a vector concentrated on the right places most of its mass there.

For a diagonal matrix, the measure consists of atoms at the eigenvalues, weighted by squared lengths of the corresponding components. This lets us describe the same mathematics with sums in the diagonal case and integrals in the continuous case.

## A subtle point about a single spectral value

The number one half belongs to the spectrum of multiplication by t. But the projection E of the singleton containing one half is zero. Why? A square-integrable function supported on one point represents the zero vector. The scalar spectral measure assigns that singleton zero mass for every vector.

So a spectral value does not have to carry its own nonzero spectral projection. The spectrum records where the operator cannot be inverted; the projection-valued measure records how vectors distribute across spectral regions. Confusing these two ideas leads to false claims about continuous spectrum.

A small interval around one half can have a nonzero projection, even though the singleton at its center has zero projection. In that sense the spectrum is visible through arbitrarily narrow neighborhoods, not necessarily through point masses.

## Reconstructing an operator from its filters

Consider partitioning the spectrum into many small intervals. Choose one representative number for each interval. Multiply that number by the projection for the corresponding interval, and sum the results. This creates a step-function approximation to the original operator.

As the intervals become finer, the step-function values approach the spectral variable. For bounded self-adjoint operators, we can arrange uniform control over the spectrum, and the approximating operators converge in operator norm. Symbolically, we write A as the integral of lambda against the projection-valued measure E.

Do not imagine that this integral adds projections one physical frequency at a time. It is the limit of finite spectral filters, just as an ordinary Lebesgue integral is built from simple functions.

This is the spectral theorem in projection-valued-measure language. Once we can integrate the identity function of the spectral variable, we can integrate many other functions. In particular, a spectral filter associated with a set B is what we obtain by integrating the indicator function of B.

The spectral theorem therefore gives us a precise way to say, “keep these modes and discard the others,” even if there are no modes represented by individual eigenvectors. It replaces a list of frequencies by a geometry of spectral regions, orthogonal components, and their measures.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a bounded self-adjoint \(A\) on a complex Hilbert space, there is a unique projection-valued measure \(E_A:\mathcal B(\mathbb R)\to\mathcal B(H)\) with
\[
E_A(\varnothing)=0,\quad E_A(\mathbb R)=I,\quad E_A(B)E_A(C)=E_A(B\cap C),
\]
and \(E_A(\bigsqcup_n B_n)x=\sum_nE_A(B_n)x\) in Hilbert norm for all x. Its support is \(\sigma(A)\), meaning \(E_A(U)\ne0\) for every open U meeting the spectrum.

For each x, \(\mu_x(B)=\langle E_A(B)x,x\rangle=\|E_A(B)x\|^2\) is a finite positive Borel measure with total mass \(\|x\|^2\). Polarization yields complex measures \(\mu_{x,y}(B)=\langle E_A(B)x,y\rangle\). One writes \(A=\int\lambda\,dE_A(\lambda)\) and for bounded Borel f, \(\langle f(A)x,y\rangle=\int f\,d\mu_{x,y}\).

For \(M_t\) on \(L^2[0,1]\), \((E_A(B)x)(t)=\mathbf1_B(t)x(t)\) and \(\mu_x(B)=\int_{B\cap[0,1]}|x(t)|^2dt\). In particular \(E_A(\{1/2\})=0\), although \(1/2\in\sigma(A)\).

### Exercises with answers

1. **Two filters.** Prove \(E_A(B)E_A(C)=E_A(B\cap C)\) for a diagonal finite matrix. **Answer:** Both sides retain precisely those eigenspace components whose eigenvalues belong to both sets.
2. **Probability analogy.** If x is a unit vector, what is \(\mu_x(\mathbb R)\)? **Answer:** One, so \(\mu_x\) is a probability measure.
3. **Singleton.** Why can a spectral singleton have zero projection? **Answer:** The corresponding spectral mass may have no atom, as for multiplication on an interval.
4. **Strong additivity.** Does countable additivity of a PVM mean operator-norm convergence of finite sums? **Answer:** No; it means strong operator convergence of the sums on every fixed vector.

### Reading and source notes

- [Kelly Davis, Spectral Theorem for Bounded Self-Adjoint Operators](https://kellyjdavis.github.io/functional-analysis/spectral-theorems/).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
