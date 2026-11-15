# 027000 — The Riemann Mapping Theorem: A Shape-Free Disk and a Proof by Extremality

**Track:** Analysis from First Principles. **Background:** simple connectivity, holomorphic logarithms, maximum modulus, Schwarz lemma, normal families, Hurwitz theorem. **Question:** Why does every proper simply connected plane domain have exactly one normalized conformal map onto the disk?

<!-- BEGIN SPOKEN LECTURE -->

# The Riemann Mapping Theorem: A Shape-Free Disk and a Proof by Extremality

A circular disk and the interior of a jagged polygon hardly look like the same geometric object. A disk has a smooth boundary. A polygon has corners. A domain bounded by a wildly irregular curve may have no simple formula at all. Yet complex analysis makes a remarkable promise: provided the region is open and connected, has no holes, and is not the entire complex plane, there is a one-to-one holomorphic map from the region onto the disk whose inverse is also holomorphic.

This is the Riemann mapping theorem. It is easy to say and surprisingly difficult to prove. In earlier lectures we transformed half-planes, strips, and wedges using explicit formulas. The Riemann mapping theorem asserts existence even when no useful closed formula is known. So the problem changes character. We are no longer trying to guess a map by algebra. We need a principle that forces *some* map to exist.

The proof we will develop is one of the best examples of a recurring strategy in modern analysis. Instead of solving the desired problem directly, choose an entire family of partial candidates and optimize a simple quantity over that family. Compactness produces a maximizing candidate. Rigidity then forces the maximizer to solve the original, stronger problem.

Before discussing the details, let us pin down the claim. A domain is an open connected subset of the complex plane. Simply connected means, in this setting, that every closed loop in the domain can be continuously shrunk to a point while staying within the domain. For plane domains, that condition ensures every holomorphic nonzero function has a holomorphic logarithm. The domain must be a proper subset of the complex plane. Otherwise the result is impossible: any holomorphic map from the entire plane into the bounded disk would be constant by Liouville's theorem.

Choose one particular point of the domain, called the base point. The theorem says there is exactly one conformal equivalence onto the unit disk that sends the base point to zero and has positive real derivative there. The point condition removes freedom to move the disk center. The derivative condition removes freedom to rotate the disk. Without these normalizations, a whole family of equivalent answers exists.

We will prove existence by three stages: build at least one injective map into the disk; choose one that maximizes its derivative at the base point; then show that a maximizer cannot omit any point of the disk. The last stage is where the geometry becomes unexpectedly ingenious.

## The first obstacle: how do we get even a small image into the disk?

Take a simply connected domain U that does not fill the complex plane. Choose one point b outside U. Because z minus b is never zero in U, and U is simply connected, we can choose one holomorphic branch of the logarithm of z minus b throughout U. Divide that logarithm by two and exponentiate. This defines a holomorphic square root of z minus b on the entire domain. Call the resulting map s.

Why use a square root? It has a useful separation property. If s of one point equaled s of another, squaring both sides would make those points equal, so s is injective. More surprisingly, the image of s cannot overlap its own negative. If s of one point equaled minus s of another, squaring would again make the inputs equal. But at that single input, the value of s cannot equal its negative, because the square root is never zero. Therefore the sets s of U and minus s of U are disjoint.

Picture one of these two images as an open patch somewhere in the complex plane. The reflected patch through the origin, its negative, never meets the first patch. Choose a point of the reflected patch. Because the reflected patch is open, a small disk around that point is entirely disjoint from the first patch. We have found a disk that s of U never enters.

Now take the reciprocal of the difference between s and the center of that missed disk. Because the denominator never becomes small, this reciprocal is bounded. Because s is injective and reciprocal is injective away from its pole, the new function is also injective and holomorphic. Multiply by a small enough positive constant to make its magnitude strictly less than one everywhere. We have produced a holomorphic injection from U into the unit disk.

The function probably does not cover the whole disk. That is fine. We only needed a starting candidate. Apply a disk automorphism to make the base point go to zero, and rotate so its derivative at that point is positive real. We now have at least one map of the required normalized kind.

Notice where the hypotheses entered. We needed U to omit a point to begin with. We needed simple connectivity to define a single-valued holomorphic square root. We needed the open mapping property to find a disk missing from the square-root image. This first stage does real work; it is not safe to replace it by the vague statement that any domain can obviously be squeezed into a disk with a holomorphic map.

## Choose the best candidate by looking at one derivative

Let F be the collection of all injective holomorphic maps from U into the unit disk that send our chosen base point to zero and have positive real derivative there. We have just shown that F is nonempty.

We need a way to compare candidates. Here is a natural but slightly mysterious choice: evaluate the derivative at the base point and prefer the largest value. Geometrically, this selects the map that expands infinitesimal distances at that point as much as possible while remaining an injection into the disk.

Could derivatives grow without bound? No. Take a small closed disk centered at the base point that stays inside U. Every candidate has magnitude at most one there, so Cauchy's derivative estimate puts a finite bound on its derivative at the center. The precise bound depends on the radius of that little disk, but it is the same for every candidate. Thus the positive derivatives have a finite supremum. Call it M.

A supremum is not always attained. We can choose a sequence of candidates whose derivatives get closer and closer to M, but they might oscillate too much to converge. This is exactly where the earlier theory of normal families enters. Every candidate takes values in the unit disk. The entire family is uniformly bounded, hence locally bounded. Montel's theorem guarantees that from our maximizing sequence we can extract a subsequence converging uniformly on every compact subset of U.

Let f be the limit. Locally uniform convergence preserves holomorphicity. Cauchy's derivative formula then gives convergence of derivatives as well. The derivative of f at the base point is M, positive, so f cannot be constant. Since each candidate has magnitude below one, the limit has magnitude at most one. The maximum modulus principle upgrades that weak inequality to a strict one everywhere: if the nonconstant limit touched the unit circle at an interior point, it would violate the maximum modulus principle.

One issue remains. Could a sequence of injective functions collapse two distinct inputs together in the limit? In general, limits of injective maps need care. Here we can use Hurwitz's theorem. Fix one input a. For every member of the sequence, the function obtained by subtracting its value at a has no zeros away from a, because the member is injective. The locally uniform limit is f of z minus f of a. On any small disk disjoint from a, Hurwitz says that the limit is either zero-free or identically zero. Since f is nonconstant, it cannot be identically equal to f of a on an open disk. Thus it cannot have a zero at any other point b. Therefore f is injective.

We have reached a significant conclusion: f is a normalized injective holomorphic map into the disk, and its derivative at the base point is as large as any candidate's. But this is still only an *into* map. Why should it hit every point in the disk? Our argument so far has not ruled out a small hole in its image.

## The missed-point trick

Suppose, for contradiction, that the maximizing map f does omit some point a in the unit disk. Because f sends the base point to zero, the omitted point a cannot be zero.

We will create a different injective map that stays inside the disk, still sends the base point to zero, but has a *larger* derivative there. That would contradict the definition of M. The construction uses two disk automorphisms with a square root between them.

First move the omitted point a to zero. The standard disk automorphism does exactly that: subtract a from the output of f and divide by one minus the conjugate of a times that output. Call this new map q. Since f never took the value a, q never takes the value zero. It remains holomorphic, injective, and valued in the disk.

Because U is simply connected and q never vanishes, it has a holomorphic square root on U. Call that square root s. Its magnitude remains below one. It is injective: if two values of s agreed, their squares would agree, and injectivity of q would force the inputs to agree.

At our base point, f is zero. The first automorphism sends zero to minus a. Thus s at the base point is a square root of minus a, a nonzero complex number of magnitude equal to the square root of the magnitude of a. Call this value b. We are still inside the unit disk, but s does not send the base point to zero.

So apply one more disk automorphism, this one sending b to zero. Finally rotate the result to make its derivative at the base point positive real. We have created another member of our candidate family. Let us call it h.

The key question is whether this square-root construction has increased the derivative. The arithmetic looks unpleasant at first, but the comparison simplifies beautifully. Let r denote the magnitude of b. We know that r is strictly between zero and one. Direct differentiation of the two disk automorphisms and the square root shows that the magnitude of h prime at the base point is the magnitude of f prime there multiplied by one plus r squared, divided by two r.

Now listen to that last factor. One plus r squared is strictly larger than two r whenever r is between zero and one, because their difference is the square of one minus r. Therefore the factor is strictly larger than one. The new candidate expands more at the base point than the supposed maximizer. Contradiction.

The missing point a cannot exist. So f maps U *onto* the whole disk. We already know it is injective and holomorphic with nonzero derivative everywhere, since the derivative of an injective holomorphic function cannot vanish. Its inverse is holomorphic by the complex inverse function theorem. We have obtained the desired conformal equivalence.

This is the central proof mechanism. If the image omitted a disk point, that omission would make a global square root available; taking that root and renormalizing would improve our extremal quantity. But we have chosen a maximizer. The only way out is that nothing is omitted. A missing value creates an improvement, so extremality forces surjectivity.

## Why the normalization is unique

Suppose two conformal equivalences, call them f and g, both take U onto the unit disk, both send our base point to zero, and both have positive real derivative there. Form g after the inverse of f. This is an automorphism of the unit disk fixing zero. Schwarz's lemma, applied to it and to its inverse, says it must be a rotation. Its derivative at zero equals the positive real derivative of g divided by the positive real derivative of f. The only rotation with positive real derivative is the identity. Therefore g and f coincide everywhere.

The uniqueness argument is short because existence did the difficult work. It also explains why normalization matters. Without fixing a base point and a tangent direction, the automorphisms of the disk create many different maps between the same domains.

## What the theorem does and does not say

We should now compare the conclusion to the assumptions. The theorem does not require a smooth boundary. It does not require a bounded domain. An upper half-plane, a long strip, and a domain with wildly irregular boundary can all qualify. Nor does it give us a practical formula. The proof selects a limit of a maximizing sequence in a family whose members are themselves often nonconstructive. It establishes existence, but not a fast numerical algorithm.

The theorem does require simple connectivity. An annulus, with a genuine hole, cannot be conformally equivalent to the disk; such an equivalence would also be a homeomorphism and would contradict the difference in their loops. And it cannot include the entire plane, because a bounded entire function is constant.

Most importantly, the theorem makes a claim about the *interior*. The map and its inverse are holomorphic on their open domains. We have not yet proved that the map extends continuously to the original boundary, that different boundary points remain distinct, or that a corner maps smoothly to a circle. Those are separate problems, and they become especially interesting when the boundary is complicated.

We began with the apparently impossible task of finding a conformal map for a domain whose shape we could barely describe. The proof did not approximate the boundary or guess a formula. It constructed one candidate, used compactness to obtain a best candidate, and then used the algebra of a missed disk value to show that the best candidate could not fail. This is a powerful pattern to remember: compactness provides existence at an optimum, and a strict improvement argument identifies the optimum as the object we actually wanted.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Precise theorem

Let \(U\subsetneq\mathbb C\) be nonempty, open, connected and simply connected, and \(z_0\in U\). There exists a unique biholomorphism \(f:U\to\mathbb D\) such that \(f(z_0)=0\) and \(f'(z_0)\in(0,\infty)\).

### Proof, with all normalization factors

**1. Nonempty candidate family.** Choose \(p\notin U\). Since \(U\) is simply connected, \(z-p\) has a holomorphic logarithm; set \(s(z)=\exp(\tfrac12\log(z-p))\). Then \(s\) is injective and \(s(U)\cap[-s(U)]=\varnothing\). Choose \(z_1\in U\). Since \(-s(U)\) is open, some \(\delta>0\) obeys \(B(-s(z_1),\delta)\cap s(U)=\varnothing\). Then

\[
q(z)=\frac{\delta/2}{s(z)+s(z_1)}
\]

maps \(U\) injectively into \(\mathbb D\). Compose with a disk automorphism and a rotation to get \(f(z_0)=0,\ f'(z_0)>0\). Thus the class \(\mathcal F\) of normalized injections is nonempty.

**2. Derivative maximizer.** Choose a closed disk \(\overline{D(z_0,R)}\subset U\). Cauchy's estimate yields \(0<f'(z_0)\le1/R\) for \(f\in\mathcal F\). Let \(M=\sup_{f\in\mathcal F}f'(z_0)>0\). Choose \(f_n\) with \(f_n'(z_0)\to M\). Montel gives a locally uniformly convergent subsequence. The limit \(f\) has \(f'(z_0)=M\) and \(f(z_0)=0\); it is nonconstant and satisfies \(|f|<1\) by maximum modulus. Hurwitz applied to \(f_n(z)-f_n(w)\), for fixed \(w\), shows \(f\) is injective. Thus \(f\in\mathcal F\) and maximizes the derivative.

**3. Surjectivity by derivative improvement.** Suppose \(a\in\mathbb D\setminus f(U)\). Necessarily \(a\ne0\). Define the automorphism \(T_a(w)=(w-a)/(1-\bar a w)\). Since \(T_a\circ f\) is nonzero on simply connected \(U\), it has a holomorphic square root \(s\). Put \(b=s(z_0)\); then \(b^2=-a\) and \(r=|b|=\sqrt{|a|}\in(0,1)\). Set

\[
h_0(z)=T_b(s(z)),\qquad
h(z)=e^{i\theta}h_0(z),
\]

with \(\theta\) chosen so that \(h'(z_0)>0\). Then \(h\in\mathcal F\). At \(z_0\),

\[
|T_a'(0)|=1-|a|^2=1-r^4,\quad
|s'(z_0)|=\frac{1-r^4}{2r}|f'(z_0)|,\quad
|T_b'(b)|=\frac1{1-r^2}.
\]

Therefore

\[
h'(z_0)=\frac{1-r^4}{2r(1-r^2)}f'(z_0)
=\frac{1+r^2}{2r}f'(z_0)>f'(z_0),
\]

since \((1-r)^2>0\). Contradiction. Hence \(f(U)=\mathbb D\).

**4. Uniqueness.** If \(f,g\) are two normalized biholomorphisms, then \(g\circ f^{-1}\) is a disk automorphism fixing 0. It must be \(e^{i\theta}z\); positivity of its derivative implies \(e^{i\theta}=1\).

### Critical hypotheses and counterexamples

- \(U=\mathbb C\): any holomorphic \(U\to\mathbb D\) is constant by Liouville.
- \(U=\mathbb D\setminus\{0\}\): not simply connected; no homeomorphism to \(\mathbb D\), hence no conformal equivalence.
- Normality alone does not give injectivity of limits; the nonconstant limit and Hurwitz are essential.
- \(|f|\le1\) in the limit is not yet \(|f|<1\); apply maximum modulus and nonconstancy.
- The theorem does *not* guarantee continuous boundary extension without further boundary hypotheses.

### Exercises and answers

1. **Bound the objective.** If \(D(z_0,R)\subset U\) and \(f:U\to\mathbb D\) is holomorphic, show \(|f'(z_0)|\le1/R\). **Answer:** Cauchy's derivative estimate on circles of radii below \(R\), then let the radius increase to \(R\).
2. **Explain root injectivity.** Why is the holomorphic square root \(s\) of \(T_a\circ f\) injective? **Answer:** If \(s(z_1)=s(z_2)\), then \(T_a(f(z_1))=T_a(f(z_2))\), and injectivity of both maps gives \(z_1=z_2\).
3. **Strict factor.** Show \((1+r^2)/(2r)>1\) for \(0<r<1\). **Answer:** The difference from 1 equals \((1-r)^2/(2r)>0\).
4. **Where Hurwitz enters.** What could fail if a locally uniform limit of univalent maps were constant? **Answer:** A constant map is not injective; positive limiting derivative at \(z_0\) excludes it.
5. **Existence versus construction.** Which step is nonconstructive? **Answer:** Montel subsequence extraction plus extremal limit provides existence but no general explicit formula or computational convergence rate.

### References

- [Guangqiu Liang, *Riemann Mapping Theorem* (Emory Mathematics, 2020)](https://www.math.emory.edu/~gliang7/RMT.pdf).
- [Yum-Tong Siu, Math 213a notes (Harvard), section on the Riemann mapping theorem](https://people.math.harvard.edu/~siu/math213a/schwarz_christoffel_transformation.pdf).
- [Wikipedia, Riemann mapping theorem](https://en.wikipedia.org/wiki/Riemann_mapping_theorem).
- [Wikipedia, Montel's theorem](https://en.wikipedia.org/wiki/Montel%27s_theorem).
