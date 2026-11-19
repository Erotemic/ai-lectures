# 036000 — Complete Spaces of Functions: Riesz–Fischer, Hilbert Geometry, and Fourier Projection

**Track:** Analysis from First Principles. **Background:** L-p norms, Hölder and Minkowski inequalities, monotone convergence, Fatou's lemma. **Question:** Why do Cauchy sequences in L-p have limits within L-p, and what new geometry appears when p equals two?

<!-- BEGIN SPOKEN LECTURE -->

# Complete Spaces of Functions: Riesz–Fischer, Hilbert Geometry, and Fourier Projection

Imagine you are approximating a complicated signal. You build one approximation, then a better one, and each refinement changes the signal less than the refinement before it. Eventually the approximations are so close in total squared error that you can barely distinguish them. Does that guarantee there is a genuine signal inside the mathematical space that they approach?

In the familiar real numbers, the answer is yes. A Cauchy sequence—one whose later terms become arbitrarily close to each other—converges to a real number. That completeness property was essential to the foundations of real analysis. But for spaces of functions, completeness is a separate theorem. A collection of perfectly reasonable functions can be closed under addition, possess a norm, and still fail to contain the limits of all its Cauchy sequences.

Consider continuous functions on an interval equipped with the total absolute-error norm. One can approximate a step function by continuous ramps that become increasingly steep near the step. The ramps approach the discontinuous step in total absolute error. There is no continuous function agreeing almost everywhere with that step. Thus the continuous functions are not complete for that norm. To solve the problem we must broaden the space, admitting measurable functions and identifying those that differ only on null sets.

The Riesz–Fischer theorem says that the L-p spaces are complete for every exponent from one through infinity. When p equals two, an additional structure emerges: an inner product. That makes L-two a Hilbert space, where orthogonality, best approximation, and Fourier coefficients can be developed with a geometry remarkably close to ordinary Euclidean vectors.

## What completeness buys us

A sequence of functions is Cauchy in L-p when the L-p norm of the difference between sufficiently late terms becomes as small as we wish. Notice that this is a statement about *integrated difference*, not about values at each particular point. A sequence might behave badly at individual points on small sets and still converge in L-p.

Completeness asks whether every such Cauchy sequence has a limit measured by the same norm. It is not automatic from the fact that the underlying real or complex values are complete. Pointwise convergence, when it happens, does not by itself tell us that the limit is p-integrable or that the L-p distance tends to zero.

The right proof has a clever architecture: extract a subsequence whose consecutive differences have rapidly summable norms, build a measurable function that bounds the accumulated changes, and use the convergence theorems to recover an almost-everywhere limit. The Cauchy property then brings the full sequence along.

This is a standard and reusable proof pattern. We have seen something similar when proving completeness of metric spaces by forcing steps to shrink rapidly. Here the steps are functions, and we need a measure-theoretic argument to turn small integrated steps into almost-everywhere control.

## Extract a sequence whose changes are summable

Suppose first that p is finite and at least one. Start with an L-p Cauchy sequence of functions. We can choose a subsequence so that the L-p norm of the difference between each selected function and the next is at most one half, one quarter, one eighth, and so on. More generally, choose any positive sequence of error allowances whose sum is finite.

At each point, form a running total of the absolute values of these successive differences. This gives a nonnegative sequence of partial-sum functions. As we add one more difference, each partial sum increases. That makes monotone convergence available.

Minkowski's inequality bounds the L-p norm of each partial sum by the sum of the L-p norms of its terms. Our choice of the subsequence makes that upper bound a fixed finite number, independent of how many terms we include.

Now take the pointwise increasing limit of the partial sums. Monotone convergence applied to the pth powers tells us that the integral of the pth power of the limit is bounded by the pth power of our fixed norm bound. Thus the total variation of the selected differences defines a function in L-p. In particular, that sum is finite at almost every point.

At any point where the total sum of absolute successive changes is finite, the telescoping series of changes converges absolutely. So our selected functions converge pointwise there to some finite value f. The exceptional points form a null set. This is the bridge from an L-p estimate to an almost-everywhere statement.

We must still show that f itself belongs to L-p. Each selected function belongs to L-p, and the differences between f and a fixed selected function are bounded by the remaining tail of our integrable total-variation function. By Minkowski and Fatou, the limit is p-integrable. Indeed, the L-p norm of the difference between f and the kth selected function is no greater than the sum of the chosen error allowances from that step onward. Those tail sums tend to zero. Hence the selected subsequence converges to f in L-p.

Finally, return to the entire original sequence. It was Cauchy. Given a small tolerance, choose a sufficiently late selected subsequence term that is close to f. Every sufficiently late term of the original sequence is close to that selected term, because all late terms are mutually close. The triangle inequality then makes the original term close to f. This proves completeness.

The exact powers of two are not essential. Their purpose is to make the norm bounds summable, which is enough to construct an almost-everywhere absolutely convergent telescoping series.

## What happens at the infinity endpoint

L-infinity deserves a separate argument. A Cauchy sequence in essential-supremum norm is eventually uniformly close outside small exceptional sets, each of measure zero. There are only countably many pairs of functions in the sequence, so we may take a single countable union of their exceptional null sets.

Outside that union, the sequence is uniformly Cauchy in the ordinary sense. At each remaining point, completeness of the real or complex numbers gives a limit. The same uniform bounds show that the essential supremum of the difference goes to zero. The limit is essentially bounded, and the L-infinity space is complete too.

The endpoint proof avoids pretending that the essential supremum is an actual maximum. We may have to ignore different null sets for different pairs of approximations, but a countable union of null sets is still null. That countable stability is exactly the measure-theoretic feature we need.

## When the norm comes from an inner product

All L-p spaces with p at least one are Banach spaces: complete normed vector spaces. But L-two is special. For complex-valued functions, define an inner product by integrating f times the complex conjugate of g. This convention makes the inner product linear in its first argument. The squared L-two norm is the inner product of f with itself.

Hölder's inequality at exponents two and two—the Cauchy–Schwarz inequality—ensures this integral exists and that the absolute value of the inner product is no greater than the product of the two norms. We now have the analog of a dot product on an infinite-dimensional space of functions.

Why is two special? In any inner-product space, the norm satisfies the parallelogram identity: the squared lengths of a sum and a difference add to twice the squared lengths of the original vectors. In L-two this follows immediately by expanding squares and integrating. For general L-p, that identity usually fails, so the norm does not arise from an inner product. On measure spaces with enough independent nonzero directions, p equal to two is the exponent that provides this precise notion of right angle and Pythagorean addition. Degenerate one-dimensional spaces can satisfy the identity for other exponents as well.

Because L-two is both an inner-product space and complete, it is a Hilbert space. That one word packages two capabilities: reliable limits of Cauchy approximations, and an orthogonal geometry in which we can choose best approximations.

## The best constant approximation

Let's make the geometry tangible. On the unit interval, consider the function whose value at x is simply x. Suppose we want the best constant approximation in squared error. Choose a constant c, subtract it from x, square the error, and integrate over the interval. The resulting expression is minimized when c equals one half—the average value of x.

There is a geometrical explanation rather than merely a calculus exercise. The constant functions form a one-dimensional subspace of L-two. The constant function one is a unit vector because the interval has length one. The inner product of x with this unit vector is the integral of x, which is one half. That coefficient tells us exactly how much of x points in the constant direction.

Subtract the projection, which is the constant function one half. The remaining error has inner product zero with every constant function; its positive and negative deviations balance in the integrated sense. The squared norm of that error is one twelfth. By the Pythagorean theorem, adding any further constant shift can only increase the squared error. So the average is not just a plausible guess. It is the unique best constant approximation in L-two.

The same idea works for a finite collection of mutually orthogonal functions. Project the target onto each direction by taking an inner product. Add those projections. The remainder is perpendicular to every direction in the chosen finite-dimensional subspace, giving the least squared-error approximation there.

## Infinite orthogonal families and Fourier analysis

Now imagine using more and more orthogonal directions. On the unit interval, complex exponentials that complete an integer number of oscillations over the interval are orthonormal in L-two. Integrating one exponential against the conjugate of a different one gives zero; integrating it against its own conjugate gives one.

For a square-integrable function, its Fourier coefficients are the inner products with these oscillatory directions. The finite sum of the first several projected directions is the best approximation among combinations of those directions. Pythagoras says that the squared norm of the projection is the sum of the squares of its coefficients.

Because an orthogonal projection cannot increase a vector's squared length, those coefficient squares have a finite total sum bounded above by the squared L-two norm of the function. This is Bessel's inequality. It follows from finite-dimensional projection geometry and requires no assertion that the Fourier exponentials span every function.

To prove that Fourier partial sums actually converge to every L-two function, we need an additional and substantive theorem: the exponentials must form a complete orthonormal system. That density result can be established using approximation of continuous functions by trigonometric polynomials and density of continuous functions in L-two. Once completeness of the orthonormal family is known, Parseval's identity strengthens Bessel's inequality to equality, and the Fourier series converges in L-two. Without that separate density argument, the inequality alone does not guarantee reconstruction.

This difference between an *orthonormal family* and an *orthonormal basis* is one of the places where mathematical language matters. Pairwise perpendicular vectors do not necessarily supply every possible direction. The completeness of L-two as a metric space does not by itself say that a particular orthonormal family is complete as a spanning system. The two uses of the word complete are related only through further arguments.

## Closed subspaces and limits of approximation

The projection idea extends beyond finite-dimensional spans. Every closed linear subspace of a Hilbert space has a unique nearest point to any given vector. The difference between the vector and that nearest point is orthogonal to the subspace.

One way to prove existence is to take a sequence of candidate points whose distances to the target approach the smallest possible distance. The parallelogram identity shows that two sufficiently good candidates must be close together; otherwise their midpoint, which remains in the subspace, would be strictly better. Thus the candidates form a Cauchy sequence. Hilbert-space completeness supplies a limit, and closedness of the subspace keeps the limit inside it. Orthogonality follows by varying the candidate point in every subspace direction.

Notice how both halves of Hilbert geometry cooperate. Orthogonality explains the form of a best approximation; completeness makes sure that the best approximation actually exists. Without completeness, the minimizing sequence could approach a missing point of the space. Without the inner product, the orthogonal decomposition would have no meaning, even if the normed space were complete.

## The passage from local measurements to functional geometry

This brings the measure-theory story to a useful resting point. We began by assigning sizes to sets, then integrating functions, then justifying exchanges of limits and integrals. We used those integrals to define distances between functions. Hölder and Minkowski made the distances compatible with algebra, and Riesz–Fischer made the resulting spaces complete.

At p equals two, the integral becomes a dot product and lets us project, approximate, and decompose signals. This is the setting in which Fourier series, orthogonal polynomials, least squares, spectral theory, and much of modern mathematical physics naturally live. The framework does not make all infinite-dimensional arguments automatic, but it tells us which parts follow from geometry and which require a separate density or convergence theorem.

A final distinction is worth keeping. Pointwise convergence asks what happens at a fixed location. L-p convergence asks what happens to an integrated size of the error. Completeness of L-p guarantees limits in that second sense, not necessarily pointwise limits of an entire sequence. The subsequence in our proof converged almost everywhere because we selected it carefully; the full sequence could converge in L-p while exhibiting complicated pointwise behavior.

With that distinction clear, the move from analysis of individual formulas to analysis of spaces of functions becomes mathematically secure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Riesz–Fischer completeness theorem

For every measure space \((X,\Sigma,\mu)\) and \(1\le p\le\infty\), \(L^p(X,\mu)\) is complete in its norm.

For \(1\le p<\infty\), let \((f_n)\) be Cauchy. Choose \(n_k\) so that

\[
\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k},\qquad k\ge1.
\]

Set \(g_N=\sum_{k=1}^N|f_{n_{k+1}}-f_{n_k}|\). Minkowski gives \(\|g_N\|_p\le1\). Monotone convergence applied to \(g_N^p\uparrow g^p\) yields \(g\in L^p\). Hence \(g<\infty\) almost everywhere, and the telescope converges absolutely to \(f\) almost everywhere. For fixed \(m\), Fatou and Minkowski give

\[
\|f-f_{n_m}\|_p\le\sum_{k=m}^\infty2^{-k}\longrightarrow0.
\]

Because \(f=f_{n_1}+\sum_{k\ge1}(f_{n_{k+1}}-f_{n_k})\) a.e., \(f\in L^p\). The Cauchy property upgrades subsequence convergence to full-sequence convergence. For \(p=\infty\), remove a countable union of null exceptional sets and use uniform Cauchy convergence there.

### Hilbert structure and projection onto constants

Over complex scalars use the convention

\[
\langle f,g\rangle=\int_Xf(x)\overline{g(x)}\,d\mu(x),\qquad
\|f\|_2^2=\langle f,f\rangle.
\]

On \([0,1]\), let \(f(x)=x\), \(e(x)=1\). The orthogonal projection onto constants is \(\langle f,e\rangle e=\tfrac12\), and

\[
\|f-\tfrac12\|_2^2=\int_0^1(x-\tfrac12)^2\,dx=\tfrac1{12}.
\]

For any constant \(c\), orthogonality yields

\[
\|f-c\|_2^2=\|f-\tfrac12\|_2^2+|c-\tfrac12|^2.
\]

### Bessel inequality and the extra Fourier completeness theorem

For any orthonormal family \((e_k)\subset H\) in a Hilbert space and finite index set \(F\),

\[
\sum_{k\in F}|\langle f,e_k\rangle|^2
=\left\|\sum_{k\in F}\langle f,e_k\rangle e_k\right\|^2\le\|f\|^2.
\]

The full sum is thus bounded by \(\|f\|^2\) for a countable family. Equality (Parseval) and reconstruction require the additional condition that the closed span of the family equals \(H\).

On \(L^2([0,1])\), the exponentials \(e_n(x)=e^{2\pi inx}\), \(n\in\mathbb Z\), form an orthonormal family. Their spanning completeness follows from density of trigonometric polynomials, **not** merely from completeness of \(L^2\) as a Banach space.

### Exercises with answers

1. **Why a subsequence?** What role does \(\sum 2^{-k}<\infty\) play? **Answer:** It controls the L-p norms of accumulated absolute differences, yielding an a.e. absolutely convergent telescope.
2. **Counterexample to completeness of continuous functions under L-one:** Construct continuous ramps converging in L-one on \([0,1]\) to \(1_{(1/2,1]}\). **Answer:** Take continuous functions equal to zero to the left of \(1/2-1/n\), equal to one to the right of \(1/2+1/n\), and linear between; their L-one distance to the step is at most \(2/n\), but no continuous function equals the step a.e.
3. **Orthogonality:** Check \(\int_0^1(x-1/2)\,dx=0\). **Answer:** The integral is \(1/2-1/2=0\), so the error is orthogonal to constants.
4. **Fourier orthogonality:** Compute \(\int_0^1 e^{2\pi i(n-m)x}\,dx\). **Answer:** Zero for integers \(n\ne m\), and one for \(n=m\).
5. **Two meanings of complete:** Does completeness of the ambient Hilbert space imply that any orthonormal sequence spans it? **Answer:** No. A family can be orthonormal yet omit directions; density of its span is a distinct property.

### Sources

- MIT OpenCourseWare, *18.125 Measure and Integration*, lectures 15–17 (Riesz–Fischer completeness and L-p spaces): https://ocw.mit.edu/courses/18-125-measure-and-integration-fall-2003/pages/lecture-notes/.
- Sheldon Axler, *Measure, Integration & Real Analysis*, chapters on Banach/Hilbert spaces and Fourier analysis: https://measure.axler.net/.
- Terence Tao, *An Introduction to Measure Theory*, convergence arguments and L-p properties: https://terrytao.wordpress.com/books/an-introduction-to-measure-theory/.
