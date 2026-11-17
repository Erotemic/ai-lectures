# Calderón–Zygmund: Second Derivatives When the Source Is Only Integrable

**Track:** Multivariable Calculus from First Principles. **Focus:** local W-two-p regularity, Fourier and singular-integral arguments, endpoint failures, and the distinction from Schauder estimates.

<!-- BEGIN SPOKEN LECTURE -->

# Calderón–Zygmund: Second Derivatives When the Source Is Only Integrable

A source term measured in an experiment may be noisy, discontinuous, or only known through an integral norm. It may not have the Hölder continuity needed for the Schauder estimates. Does the Poisson equation still force its solution to have two derivatives?

In an important sense, yes. The second derivatives may exist as weak derivatives and be integrable to the same power as the source, even when we cannot bound them uniformly or insist that they are continuous. The results that make this precise are closely connected with Calderón–Zygmund theory, a cornerstone of harmonic analysis.

We will build the result from the case where it is almost transparent, examine why extending it is hard, and construct a bounded source whose solution has unbounded second derivatives. That last example is essential. It shows exactly why an estimate in an integral norm is not an estimate in the supremum norm.

## First choose the right meaning of regularity

The Sobolev space W two comma p consists of functions whose weak derivatives through order two belong to L p. Here p is at least one, and L p means that the p-th power of the absolute value is integrable. When p equals two, this is the Hilbert-space setting familiar from energy arguments. When p is large, the norm penalizes large values more strongly, but it still permits spikes on sufficiently small sets.

A weak derivative does not have to be continuous or even defined at every point in the classical sense. It is a function that represents differentiation when we integrate against smooth test functions. This is the right object for a Poisson equation with discontinuous forcing: the equation can make exact sense in distributions even when the classical Hessian fails to exist at certain points.

For the Laplacian and exponents strictly between one and infinity, a standard interior regularity theorem says the following. If negative Laplacian of u equals f, with f in L p, then under the usual local weak-solution assumptions u belongs to W two comma p on every smaller region compactly inside the domain. Quantitatively, the W two comma p norm on the smaller region is controlled by the L p norm of f and an L p norm of u on a larger region.

The u term is not an accident. Harmonic functions solve the homogeneous equation, so their size is not controlled by the forcing alone. Interior estimates must also account for the uncontrolled harmonic component and how far we remain from the boundary.

## The p equals two proof is visible in Fourier space

Consider a smooth rapidly decaying function on the whole Euclidean space, and let f be its negative Laplacian. The Fourier transform replaces differentiation by multiplication with frequency. Each first derivative contributes one frequency factor; the negative Laplacian contributes the squared length of the frequency vector.

Consequently the Fourier transform of the second partial derivative in directions i and j is the transform of f multiplied by minus the product of the i-th and j-th frequency coordinates, divided by the squared frequency length.

The absolute value of that multiplier is at most one. Plancherel's theorem says that the L two norm of a function equals, up to the chosen Fourier normalization, the L two norm of its transform. So each second derivative has L two norm no larger than the L two norm of f.

Even better, sum the squares of the L two norms over every pair of second-derivative directions. At each nonzero frequency, the sum of the squares of all those multipliers equals one. The numerator becomes the sum over i and j of the products of the squared coordinate frequencies; that is just the square of the total squared frequency length. The denominator is the same. The result is an exact identity: the total L two energy of the Hessian equals the L two energy of the Laplacian, for a sufficiently regular whole-space function.

We have proved a two-derivative estimate without differentiating the forcing. That is one of the clearest illustrations of elliptic regularity. The equation controls not just the trace of the Hessian in an integral sense, but the entire Hessian.

On a bounded domain there can be boundary terms if we try to repeat the integration-by-parts argument globally. The clean identity belongs to the whole-space or appropriately controlled setting; interior estimates use localization and include an additional term measuring u.

## Why p other than two needs another idea

Fourier multipliers solved the L two problem because Plancherel gives an exact isometry. For p different from two, there is no identical argument that simply takes the maximum absolute value of the multiplier. A bounded multiplier function does not automatically define a bounded operator on every L p space.

In physical space, the second derivatives of a Newtonian potential take the form of singular integrals. The kernel is roughly inverse distance to the dimension, with angular cancellation. That is a borderline singularity: it cannot be handled by taking absolute values before integrating.

Calderón and Zygmund developed machinery that preserves the cancellation and proves a strong L p bound for this class of operators when p lies strictly between one and infinity. A typical strategy first obtains the L two bound. Then a Calderón–Zygmund decomposition splits an integrable function into a controlled part and pieces whose average on selected cubes is zero. The zero-average property makes distant contributions from each piece cancel. This gives a weak L one estimate, meaning a quantitative bound on the size of the set where the output exceeds a given threshold.

Interpolation carries that information to strong L p bounds between one and two. Duality extends the result above two. The full argument is a theorem in harmonic analysis, not something hidden in the algebra of the Poisson equation. The PDE regularity estimate is a particularly useful consequence of it.

There is a subtle distinction between a strong L one estimate and a weak L one estimate. The latter controls how large the set of exceptionally big output values can be. It does not assert that the output has an integrable absolute value bounded by a constant times the input's L one norm. Losing that distinction would produce an incorrect endpoint theorem.

## A bounded source can still produce an unbounded Hessian

Now construct a counterexample in the plane. Away from the origin, define u of x and y to equal x times y times the natural logarithm of the distance to the origin. Near the origin, this function approaches zero, and its first derivatives also approach zero. Thus we can extend it continuously with a continuous gradient at the origin.

Compute its Laplacian away from zero. The result is four x y divided by x squared plus y squared. That quotient is bounded in absolute value by two, because twice the absolute value of x y is no greater than x squared plus y squared. Hence the negative Laplacian is a bounded function, although its angular value changes as we approach the origin.

But take the mixed second derivative of u. It contains the logarithm of the distance plus terms that remain bounded as the origin is approached. The logarithm tends to negative infinity. So the mixed Hessian entry is unbounded in every neighborhood of the origin.

If we want a compactly supported example, multiply u by a smooth cutoff that equals one near the origin and vanishes outside a larger disk. In the cutoff annulus everything is smooth and bounded, so the right-hand side remains bounded. Near the origin we have the same unbounded mixed second derivative. There is no hidden point-source delta at the origin: the first derivatives tend to zero sufficiently fast, and the displayed Poisson equation holds distributionally with a bounded source.

This example rules out a general estimate asserting that the supremum norm of the Hessian is controlled by the supremum norm of the forcing. It is not a pathology caused by forcing that becomes infinite: the forcing is bounded. The failure is specifically at the endpoint where p is infinity.

At the same time, the logarithmic divergence is integrable to every finite power on a small disk. The area element contributes a factor of radius, and the integral of radius times the p-th power of the absolute logarithm is finite for every finite p. Thus our example belongs to W two comma p locally for every finite p, even though its Hessian is unbounded. That is entirely consistent with the Calderón–Zygmund theorem.

## What changes at the endpoints?

The strong L p estimates work for one less than p less than infinity. At p equals one, singular integral operators have a weak-type substitute in general, rather than a uniform strong L one bound. At p equals infinity, the natural substitute involves bounded mean oscillation, often abbreviated B M O, rather than a uniform bound on the output.

Bounded mean oscillation measures how much a function fluctuates around its average on each ball, uniformly over all balls. It can contain unbounded functions: a logarithmic singularity is a standard example. Thus it is plausible that a bounded source can generate second derivatives in bounded mean oscillation without generating bounded second derivatives.

We will not prove the full endpoint theory here. Its role is to show why the permissible exponents are part of the theorem, not a technical decoration. Replacing strictly less than infinity with less than or equal to infinity would change a true regularity statement into a false one.

## Recover pointwise information with Sobolev embedding

Integral regularity does not mean we must abandon all continuity conclusions. Sobolev and Morrey embeddings can convert sufficiently strong L p control of derivatives into Hölder control of lower-order derivatives.

For example, in n dimensions, if p is larger than n, then W two comma p locally embeds into C one comma gamma locally, with gamma equal to one minus n over p. This yields a continuously differentiable representative whose gradient is Hölder continuous. In the plane, choosing p equals four gives gamma equals one half.

Notice the derivative count. From an L p bound on the Hessian we obtained Hölder continuity of the gradient, not necessarily continuity of the Hessian itself. By contrast, a Schauder estimate with Hölder forcing can directly control the Hölder seminorm of the Hessian. The estimates answer related but different questions.

The theorem must still be applied to the correct operator. For the constant-coefficient Laplacian the L p theory is particularly clean. For variable-coefficient nondivergence equations, Calderón–Zygmund-type W two comma p estimates can survive under suitable coefficient regularity, such as appropriate continuity or vanishing mean oscillation assumptions. They do not automatically hold for arbitrary bounded measurable coefficients. For divergence-form equations with rough coefficients, one ordinarily targets first-order Sobolev control instead of two derivatives without additional coefficient regularity.

Boundary estimates require additional hypotheses too. Interior W two comma p regularity does not grant global W two comma p regularity on a polygon with a reentrant corner. We have already seen exact harmonic corner singularities that obstruct such conclusions. Regularity must be compatible with the geometry and the boundary conditions.

## Choosing the right estimate

When should one use which theory? If the forcing and the coefficients have controlled Hölder oscillation, and we need classical pointwise information about the Hessian, Schauder estimates are natural. If the forcing is known mainly through an L p norm, perhaps because it is noisy or discontinuous, Calderón–Zygmund estimates provide a quantitative Sobolev description. If we need positivity or comparison, neither estimate substitutes for a maximum principle. If we need boundary growth, Hopf's lemma has its own geometry and sign assumptions.

For a numerical method, this distinction influences which error bounds are justified. A method with an error estimate requiring global second derivatives may still be useful with an L p Hessian, but its analysis must be formulated in the appropriate norms. Pointwise Hessian smoothness should not be silently inferred from a bounded load. Conversely, when high regularity is genuinely available, it can support stronger approximation results.

There is a single organizing principle behind these facts: elliptic equations transfer regularity from data to solutions, but the kind of regularity transferred depends on how we measure the data. Hölder norms, integral norms, weak derivatives, and boundary traces encode different information. Choosing the correct language is part of proving the correct theorem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Interior \(W^{2,p}\) estimate for the Laplacian

Let \(1<p<\infty\), \(B_1\Subset B_2\), and suppose \(-\Delta u=f\) holds in distributions with \(f\in L^p(B_2)\) and suitable local integrability for \(u\). Then \(u\in W^{2,p}(B_1)\), and a representative estimate is
\[
\boxed{\|u\|_{W^{2,p}(B_1)}\le C_{n,p}\bigl(\|f\|_{L^p(B_2)}+\|u\|_{L^p(B_2)}\bigr).}
\]
One can use general nested domains \(U\Subset V\), with constants depending on distance to boundary. The displayed estimate is a regularity result for the Laplacian, not an assumption that every measurable coefficient matrix yields the same bound.

### Fourier-space proof when \(p=2\)

For \(u\in C_c^\infty(\mathbb R^n)\) and \(f=-\Delta u\), with Fourier convention \(\widehat{D_iu}=i\xi_i\hat u\),
\[
\widehat{D_{ij}u}(\xi)=-\frac{\xi_i\xi_j}{|\xi|^2}\hat f(\xi),\qquad \xi\ne0.
\]
By Plancherel and \(\sum_{i,j}\xi_i^2\xi_j^2=|\xi|^4\),
\[
\sum_{i,j=1}^n\|D_{ij}u\|_{L^2(\mathbb R^n)}^2
=\int_{\mathbb R^n}\frac{\sum_{ij}\xi_i^2\xi_j^2}{|\xi|^4}|\hat f(\xi)|^2\,d\xi
=\|f\|_{L^2(\mathbb R^n)}^2.
\]
This is a whole-space identity under sufficient decay; it does not assert the same identity for arbitrary bounded-domain boundary conditions.

### Bounded forcing with unbounded Hessian

For \(r=\sqrt{x^2+y^2}>0\), let \(v(x,y)=xy\log r\). Direct differentiation gives
\[
\Delta v=\frac{4xy}{r^2},\qquad
\partial_{xy}v=\log r+1-\frac{2x^2y^2}{r^4}.
\]
Since \(|4xy/r^2|\le2\) but \(\partial_{xy}v\to-\infty\) along any ray as \(r\to0\), \(D^2v\notin L^\infty_{\rm loc}\). Choose \(\eta\in C_c^\infty(B_{1/2})\), \(\eta=1\) on \(B_{1/4}\), and set \(u=\eta v\), extended by \(u(0)=0\). Then \(f=-\Delta u\in L^\infty\), and the distributional equation holds without a delta mass at zero because \(\nabla v=O(r|\log r|)\) near zero. Yet \(D^2u\notin L^\infty\). For finite \(p\),
\[
\int_0^{1/4} r|\log r|^p\,dr<\infty,
\]
so \(u\in W^{2,p}_{\mathrm{loc}}\) for every finite \(p\).

### Morrey embedding and its limits

If \(p>n\), \(W^{2,p}(B_1)\hookrightarrow C^{1,\gamma}(B_{1/2})\) with \(\gamma=1-n/p\). In particular, in two dimensions \(p=4\) gives \(\gamma=1/2\). The embedding controls gradients pointwise but does **not** give a uniformly bounded Hessian. Schauder's \(C^{2,\alpha}\) conclusions use additional Hölder assumptions on coefficients and source.

### Exercises and worked answers

1. **Fourier symbol.** Compute the sum over all \(i,j\) of \(|\xi_i\xi_j/|\xi|^2|^2\). **Answer:** It equals \(1\) when \(\xi\ne0\).
2. **Bounded forcing.** Why is \(4xy/(x^2+y^2)\) bounded near zero? **Answer:** \(2|xy|\le x^2+y^2\), so its absolute value is at most \(2\).
3. **Mixed Hessian.** Along \(x=y=r/\sqrt2\), compute \(\partial_{xy}v\). **Answer:** \(\log r+1/2\), which diverges negatively.
4. **Power integrability.** Show \(\int_0^\varepsilon r|\log r|^pdr<\infty\) for finite p. **Answer:** Substitute \(r=e^{-t}\) to obtain \(\int_{-\log\varepsilon}^\infty e^{-2t}t^pdt<\infty\).
5. **Which regularity?** If a planar Poisson source lies in \(L^4_{\rm loc}\), what follows for the gradient? **Answer:** Local \(W^{2,4}\), hence a locally \(C^{0,1/2}\) gradient representative; not a bounded classical Hessian.

### Sources and further reading

- [MIT OpenCourseWare, *Differential Analysis II*, lectures 26–27](https://ocw.mit.edu/courses/18-156-differential-analysis-ii-partial-differential-equations-and-fourier-analysis-spring-2016/pages/lecture-notes/), Calderón–Zygmund inequalities.
- [University of Jyväskylä, *Partial Differential Equations 2* notes, section on local \(L^p\) regularity](https://users.jyu.fi/~miparvia/lecturenote2025PDE2.pdf), local \(W^{2,p}\) regularity for Poisson's equation.
- [Russell Brown, *Singular Integral Operators* lecture notes (University of Kentucky)](https://www.ms.uky.edu/~rbrown/courses/ma773.s.08/notes.pdf), Calderón–Zygmund kernels and \(L^p\) theory.
- [Wikipedia: Singular integral](https://en.wikipedia.org/wiki/Singular_integral); [Wikipedia: Sobolev inequality](https://en.wikipedia.org/wiki/Sobolev_inequality), background on singular integrals and Morrey embedding.
- Library connection: `multivariable-calculus:053000` (Schauder versus \(W^{2,p}\) spaces).
