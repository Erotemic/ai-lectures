# 024000 — Normal Families: Finding Convergent Functions in an Infinite Collection

**Track:** Analysis from First Principles. **Background:** compactness, uniform convergence on compact sets, Cauchy estimates, identity theorem, Rouché's theorem. **Question:** When does an arbitrary sequence of holomorphic functions contain a convergent subsequence, and what properties survive in its limit?

<!-- BEGIN SPOKEN LECTURE -->

# Normal Families: Finding Convergent Functions in an Infinite Collection

Suppose you are handed an endless list of holomorphic functions on the unit disk. Each function may look different from the others. You are not told that the sequence converges, and you are not allowed to select a single point and declare success merely because the function values happen to converge there. You want a subsequence that approaches a genuine holomorphic function *throughout the disk*, with enough control to exchange limits and derivatives.

It sounds like too much to ask without knowing the formulas. Remarkably, one common kind of bound is enough: if the functions are uniformly bounded on every compact set strictly inside the domain, then every sequence has a subsequence converging uniformly on every such compact set. This is Montel's theorem, in its finite-valued form. It turns local boundedness into compactness of families of holomorphic functions.

The theorem is more than an abstract existence statement. Its proof explains why complex differentiability prevents wild oscillation at arbitrarily small scales, and it provides a rigorous way to pass from a large collection of approximations to an analytic limit.

## A sequence that converges, but not uniformly to the rim

Begin with an explicit example: f sub n of z equals z to the n-th power, defined on the open unit disk. For each fixed input with magnitude less than one, repeated multiplication eventually drives the output toward zero. So the functions converge pointwise to the zero function on the disk.

Are they uniformly close to zero throughout the open disk? No. For every n, we can choose a point very close to the boundary where the magnitude of z to the n-th power is still close to one. The largest possible magnitude over the open disk is one as a supremum, even though that supremum is not attained inside. The convergence is not uniform on the entire domain.

Now choose a smaller closed disk, say radius three quarters. There the magnitude of every f sub n is at most three quarters raised to the n-th power, which tends to zero. The convergence is uniform on that smaller disk. The same argument works on any compact set contained strictly inside the unit disk, because every such set stays a positive distance from the boundary.

This is called locally uniform convergence: uniform convergence on *each compact subset* of the open domain. It is exactly the kind of convergence that complex analysis naturally gives us. We can control values and derivatives on a smaller region using information from a slightly larger one. We do not need uniform control right up to a boundary where the functions may behave very differently.

Notice how the quantifiers work. For any particular compact set and any requested error tolerance, there is an index after which all later functions satisfy the bound everywhere on that compact set. The index may depend on the compact set. That flexibility is not a weakness; it is the right notion for functions on open domains.

## A bound on values secretly controls slopes

What creates compactness for holomorphic functions? A familiar theorem from real analysis, Arzelà–Ascoli, says roughly that a uniformly bounded and equicontinuous family of functions on a compact metric space has convergent subsequences in the uniform norm. Equicontinuity means that one choice of how close two input points must be works for *every* function in the family.

In general, bounding a function's values does not bound how rapidly it can oscillate. You can draw a real-valued wave whose height never exceeds one but whose frequency grows without bound. These waves are uniformly bounded yet not equicontinuous. Their derivatives become larger and larger. A bound on values alone is insufficient for arbitrary continuous or differentiable functions.

Holomorphic functions behave differently. Cauchy's integral formula expresses their derivatives using values on a surrounding circle. If every function is bounded by M on a closed disk of radius r, then the magnitude of its derivative at the center is bounded by M divided by r. On a smaller concentric disk, we obtain a uniform derivative bound from the values on the larger circle. There is an important spatial margin: we keep the point where we estimate derivatives away from the boundary of the region where we know the value bound.

A derivative bound gives a common Lipschitz estimate along short line segments lying in the smaller disk. Therefore all the functions vary slowly over sufficiently short distances, with a distance threshold independent of which member of the family we choose. This supplies the equicontinuity that ordinary bounded functions do not possess.

So the chain of reasoning is concrete: local bounds on holomorphic values, Cauchy estimates on a slightly smaller region, common control of slopes, then equicontinuity. Complex differentiability converts a weak-looking value bound into a much stronger regularity estimate.

## From one compact disk to the entire open domain

There is still a problem. Arzelà–Ascoli gives a uniformly convergent subsequence on one compact set. Our domain contains infinitely many possible compact subsets. How can we choose one subsequence that works on all of them?

Use a compact exhaustion. In the unit disk, take nested closed disks with radii approaching one: one half, two thirds, three quarters, and so forth. Every compact subset of the open disk lies inside one of these eventually. For a general open domain, we can choose a countable increasing sequence of compact sets whose interiors cover the domain.

Apply Arzelà–Ascoli to the first compact set and select a subsequence converging uniformly there. From that subsequence, choose a further subsequence converging uniformly on the second compact set. Continue, narrowing the selected indices at each stage. Then take the diagonal subsequence: the first member from the first selection, the second from the second selection, and so on, with indices increasing appropriately.

For any fixed compact set in the exhaustion, all sufficiently late diagonal terms belong to a subsequence that converges uniformly on that set. Thus the diagonal subsequence converges locally uniformly across the whole domain.

This construction can sound like pure combinatorics until we recall its purpose. We want a single limiting function that makes consistent sense at every point, not a different limit for each disk. The nested subsequences guarantee agreement on overlaps, and the diagonal construction delivers one subsequence whose behavior can be examined on every fixed compact region.

## Why the limit remains holomorphic

Uniform limits of continuous functions are continuous, but holomorphicity is a stronger condition. Why does it survive locally uniform convergence? We can integrate along a small closed triangle or circle contained in the domain. Each holomorphic member has zero contour integral along a triangle. Because convergence is uniform on the compact contour, we can pass the limit through the integral. The limiting function also has zero integral around every sufficiently small triangle.

Morera's theorem then says the continuous limit is holomorphic. Another route uses Cauchy's integral formula: pass to the limit in the boundary integral to recover a Cauchy formula for the limit, then differentiate it. Either route shows that locally uniform limits of holomorphic functions are holomorphic.

Even better, the derivatives converge locally uniformly. Fix a small closed disk about a point and a larger surrounding circle that stays inside the domain. Uniform convergence on the circle means the Cauchy integral formula for each derivative converges uniformly on the smaller disk. So the sequence of first derivatives converges locally uniformly to the derivative of the limit, and the same is true for every higher derivative.

There is an important contrast with real-variable calculus. Uniform convergence of real differentiable functions does not by itself imply derivative convergence, or even differentiability of the limit. The holomorphic structure bridges that gap precisely because the derivative can be expressed by an integral using the function values on a surrounding contour.

Putting the pieces together gives Montel's theorem: a family of holomorphic functions that is uniformly bounded on every compact subset of a domain is normal, meaning every sequence in the family has a locally uniformly convergent subsequence whose limit is holomorphic. The version here requires a *finite-valued* holomorphic limit. Some advanced books use a broader convention involving convergence to infinity in the spherical metric; that is not the convention needed for this theorem's compactness argument.

## A boundary that can hide bad behavior

Return to the functions z to the n-th power. Every one of them has magnitude at most one on the unit disk. Montel therefore applies immediately. In fact the whole sequence converges locally uniformly to zero, not just a subsequence. But the convergence still fails to be uniform on the entire open disk.

This shows exactly what local boundedness buys us and what it does not buy us. Montel gives compactness in the topology of uniform convergence on compact sets. It gives no unconditional uniform convergence up to the boundary. A family can behave more and more sharply in a thin layer near the rim, even while its interior limits are perfectly regular.

For contrast, consider f sub n of z equals n times z. At every fixed nonzero input the values diverge in magnitude. Even in a small compact disk about zero, the largest values grow without bound as n grows. The family is not locally bounded. There is no subsequence converging locally uniformly to a finite holomorphic function on a neighborhood of zero.

This is the precise role of the assumption. A bound just at one chosen point would be insufficient: all of these functions equal zero at the origin, yet their behavior nearby becomes unbounded. We need a bound that applies uniformly to every function on *every compact neighborhood*, not a pointwise bound at one location.

## Zeros and nonzeros behave rigidly under convergence

A beautiful application is Hurwitz's theorem. Suppose a sequence of holomorphic functions converges locally uniformly on a connected domain, and none of the functions ever vanishes. What can happen to the limit? Either the limit never vanishes, or the limit is identically zero.

Why can we not create a single isolated zero out of nowhere? Suppose the limit had an isolated zero at a but were not identically zero. Choose a small circle around a on which the limit has no zeros. Uniform convergence along that circle makes each late approximating function uniformly close to the limit there. Rouché's theorem says the approximating function and the limit have the same number of zeros inside, counting multiplicity. But the approximating function has none, while the limit has at least one. Contradiction.

The exception for the identically zero limit is necessary. Constant functions equal to one divided by n never vanish, yet converge everywhere to zero. Hurwitz is not the false claim that nonvanishing automatically passes through every locally uniform limit. It is the more precise statement that an isolated newly created zero is impossible unless zeros already existed nearby in the approximants.

There is a related positive statement. If the limit is not identically zero and has a zero of order m at a, then on a sufficiently small disk centered at a, every sufficiently late approximating function has exactly m zeros, counted with multiplicity. Those zeros need not occur at precisely a, and they may split into several nearby zeros. For example, z squared plus one over n has two zeros that approach zero. The limiting function z squared has one *location* with multiplicity two. The zero count is stable even though the individual roots move.

## From scattered measurements to a limit function

Montel combines especially well with the identity theorem. Suppose a sequence of holomorphic functions is locally bounded on a connected domain. You do not know whether the entire sequence converges. But suppose the numerical values converge at every point in some set that has an accumulation point *inside* the domain. Does that sparse information determine a full locally uniform limit?

Yes. Montel says every subsequence contains a locally uniformly convergent further subsequence. Any such limit must agree with the given pointwise limits on the special set. By the identity theorem, two holomorphic limits agreeing there must agree everywhere on the connected domain. So there is at most one possible subsequential holomorphic limit.

Now assume the original sequence did not converge locally uniformly to that candidate. Then on some compact set, infinitely many terms would stay a fixed positive distance away from it. Select those terms as a subsequence. Montel gives a further locally uniformly convergent subsequence. But its limit must equal the same candidate, contradicting that fixed separation. Therefore the whole sequence converges locally uniformly.

This is a form of Vitali's convergence theorem. A local uniform bound plus convergence on a thin set with an interior accumulation point forces convergence everywhere on compact subsets. Compare that with arbitrary continuous functions, where values on such a thin set cannot generally determine a function. The identity theorem and compactness work together to transform sparse information into global analytic convergence.

The interior accumulation hypothesis matters. Data that accumulate only at a boundary point need not determine a holomorphic function in the domain. Likewise, without local boundedness, a sequence can agree at the sample points while diverging violently elsewhere.

## A compactness principle for analysis

Montel's theorem is an answer to a recurring problem in mathematics: how can we extract a meaningful limiting object from a collection that is too large to understand explicitly? In complex analysis, local boundedness supplies more structure than one might expect. Cauchy's formula turns value bounds into derivative bounds; derivative bounds supply equicontinuity; compactness yields a convergent subsequence; locally uniform convergence preserves holomorphicity and all derivatives.

Once that framework is available, Rouché's theorem protects zero counts, Hurwitz's theorem constrains nonvanishing limits, and the identity theorem can upgrade convergence on a sparse set to convergence throughout the domain. These are not independent magic tricks. Each depends on the same ability to turn local analytic control into a limit that behaves well under the operations we care about.

The important boundary of the result is just as clear. We have compactness *on compact subsets*, not automatically at the domain boundary. We have convergence of *some subsequence* under local boundedness, not necessarily convergence of the original sequence. With extra uniqueness information, as in Vitali's theorem, we can upgrade subsequential compactness to convergence of the full sequence. Making those distinctions is what turns a collection of impressive theorems into a usable method.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Local uniform convergence and local boundedness

Let \(\Omega\subset\mathbb C\) be open and \(\mathcal F\subset\mathcal O(\Omega)\).

- **Locally bounded:** For each compact \(K\subset\Omega\), there exists \(M_K<\infty\) such that \(|f(z)|\le M_K\) for all \(z\in K\) and \(f\in\mathcal F\).
- **Normal (finite-valued convention):** Each sequence in \(\mathcal F\) has a subsequence that converges uniformly on each compact subset of \(\Omega\) to a finite holomorphic limit.
- **Montel:** Local boundedness implies normality in this convention. The proof uses Cauchy derivative bounds on nested disks, equicontinuity, Arzelà–Ascoli on compact exhaustion sets, and a diagonal subsequence.

If \(\overline{D(a,R)}\subset\Omega\) and \(|f|\le M\) there, then for \(0<r<R\), a point \(z\in\overline{D(a,r)}\) has
\[
|f'(z)|\le\frac{MR}{(R-r)^2},
\]
by Cauchy's first derivative formula over \(|\zeta-a|=R\). Sharper estimates are possible with smaller circles centered at \(z\). The displayed bound suffices for equicontinuity on \(\overline{D(a,r)}\).

### Weierstrass convergence theorem

If \(f_n\in\mathcal O(\Omega)\) and \(f_n\to f\) locally uniformly, then \(f\) is holomorphic and \(f_n^{(k)}\to f^{(k)}\) locally uniformly for each fixed \(k\ge0\). Apply Cauchy's formula on a slightly larger circle and use uniform convergence on that contour.

### Hurwitz and stability of zeros

If \(\Omega\) is connected, \(f_n\) are holomorphic and zero-free on \(\Omega\), and \(f_n\to f\) locally uniformly, then either \(f\equiv0\) or \(f\) is nowhere zero. More generally, if \(f\not\equiv0\) has a zero of multiplicity \(m\) at \(a\), then for sufficiently small \(r>0\) with no other zeros of \(f\) on \(\overline{D(a,r)}\), the approximants have exactly \(m\) zeros (counting multiplicity) in \(D(a,r)\) for sufficiently large \(n\).

### Vitali convergence theorem (one formulation)

Let \(\Omega\) be a domain, \(f_n\in\mathcal O(\Omega)\) a locally bounded sequence, and \(E\subset\Omega\) have an accumulation point inside \(\Omega\). If \(f_n(z)\) converges for each \(z\in E\), then \(f_n\) converges locally uniformly on \(\Omega\) to a holomorphic function. Montel gives subsequential limits; the identity theorem makes them unique; a contradiction argument upgrades subsequence convergence to convergence of the whole sequence.

### Examples and exercises

1. For \(f_n(z)=z^n\) on \(\mathbb D\), prove local uniform convergence to zero but not uniform convergence on \(\mathbb D\). **Answer:** On \(|z|\le r<1\), \(\sup|f_n|\le r^n\to0\); on the whole disk, \(\sup|f_n|=1\).
2. Does \(f_n(z)=nz\) have a finite locally uniformly convergent subsequence on a disk about zero? **Answer:** No; for any nonzero \(z\), \(|f_n(z)|=n|z|\to\infty\).
3. Let \(f_n(z)=z^2+1/n\). What does Rouché say near zero? **Answer:** On any fixed small circle, for sufficiently large \(n\) the approximants have two zeros inside, counting multiplicity, matching \(z^2\).
4. Can nonvanishing \(f_n\) converge locally uniformly to zero? **Answer:** Yes; \(f_n\equiv1/n\). Hurwitz allows the identically zero limit.
5. Why must the accumulation point in Vitali's theorem be **inside** the domain? **Answer:** The identity theorem needs an accumulation point in the holomorphic domain; boundary accumulation alone does not ensure uniqueness.
6. Does Montel guarantee convergence of the full original sequence? **Answer:** No; it guarantees convergent subsequences. Additional uniqueness information, as in Vitali, can yield full convergence.

### Sources and further reading

- MIT OCW, *18.112 Functions of a Complex Variable*, Lecture 19, Normal Families: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- University of Wisconsin, A. Nagel, *Complex Analysis: Normal Families and Montel's Theorem*: https://people.math.wisc.edu/~ajnagel/Math722Lectures5.pdf.
- University of Jyväskylä, *Complex Analysis 2*, Arzelà–Ascoli and Montel: https://users.jyu.fi/~salomi/teaching/ca2_2024/Lecture_notes_eng.pdf.
