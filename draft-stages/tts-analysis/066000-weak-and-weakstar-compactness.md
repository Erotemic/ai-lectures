# 066000 — Weak and Weak-Star Convergence: Compactness Without Norm Convergence
**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

<!-- BEGIN SPOKEN LECTURE -->
# Weak and Weak-Star Convergence: Compactness Without Norm Convergence

Imagine a sequence of vectors whose lengths all equal one, while their nonzero entries march farther and farther along an infinite list of coordinates. The first vector has a one in the first position, the next in the second, and so on. In the ordinary norm, no two of these vectors become close. Yet if we take the inner product with a fixed square-summable vector, the answer tends to zero: the test vector's coordinates must themselves become small. This sequence converges in one sense and fails to converge in another.

Norm convergence demands that every part of a vector become close simultaneously. Weak convergence asks a more modest question: do all continuous linear measurements agree in the limit? Think of each measurement as a fixed experiment. If every such experiment eventually sees the same answer, we call the sequence weakly convergent. The marching unit vectors converge weakly to zero in the Hilbert space of square-summable sequences, even though their distance from zero is always one.

The distinction becomes useful for approximation schemes. An approximate solution may have uniformly bounded energy but retain fine oscillations. The function need not have a strongly convergent subsequence in the energy norm. Weak convergence may be available, and a weak limit can still satisfy linear equations. Convexity lets us retain something else: the norm of the limit cannot exceed the limit inferior of the norms. Energy does not suddenly increase when we take a weak limit.

But a bounded sequence does not automatically have a weakly convergent subsequence in every Banach space. Reflexivity matters. Informally, a space is reflexive when taking its continuous dual twice returns the original space without losing elements. Hilbert spaces, and L-p spaces for p strictly between one and infinity, have this property. On these spaces, closed bounded sets have the right kind of weak compactness. The spaces L-one and L-infinity generally behave differently.

A second notion, weak-star convergence, applies to functionals. Suppose our objects are themselves measurements on a space X. Rather than test them with all measurements on the dual space, we evaluate each functional at every fixed vector in X. When these values converge, we have weak-star convergence. It is deliberately weaker than weak convergence on the dual, because fewer tests are required.

Here is a concrete example. A bounded sequence of numbers defines a functional on absolutely summable sequences by multiplying corresponding coordinates and adding the results. Consider again a sequence with one nonzero coordinate moving to the right, now treated as a bounded sequence. Against any absolutely summable test sequence, the value tends to zero. So it converges weak-star to zero as an element of the dual of the absolutely summable sequences. The argument uses the fact that the coordinates of an absolutely summable sequence go to zero.

Banach–Alaoglu says something remarkable: the closed unit ball in the dual of a normed space is compact in the weak-star topology. The word compact here concerns the topology of these evaluations; it does not mean norm compact. And in general it concerns convergent subnets, not necessarily subsequences. If the underlying space is separable, the weak-star topology on the dual unit ball is metrizable, and subsequence arguments become available.

Why is this not just an abstract curiosity? Think of a sequence of bounded linear measurements, or a family of probability measures on a compact space. Their numerical responses to continuous test functions may stabilize even when there is no meaningful point-by-point density convergence. Weak-star compactness is one reason variational limits and measure-valued limits can be constructed.

The discipline is to name the topology. A proof that has produced weak convergence has not produced convergence of norms, products, or pointwise values. If a nonlinear term is involved, an extra compactness argument or some structural monotonicity may be required. Weak compactness is a powerful way to obtain candidates for solutions; it does not by itself certify that every operation passes to the limit.
<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(X\) be a Banach space. \(x_n\rightharpoonup x\) in \(X\) means \(\phi(x_n)\to\phi(x)\) for every \(\phi\in X^*\). For \(\phi_n\in X^*\), \(\phi_n\overset{*}{\rightharpoonup}\phi\) means \(\phi_n(x)\to\phi(x)\) for each \(x\in X\).

For \(e_n\in\ell^2\), \(\langle e_n,y\rangle=y_n\to0\) for every \(y\in\ell^2\), so \(e_n\rightharpoonup0\) but \(\|e_n\|_2=1\). Similarly \(e_n\in\ell^\infty=(\ell^1)^*\) converges \(\sigma(\ell^\infty,\ell^1)\)-weak-star to zero. Weak lower semicontinuity: \(\|x\|\le\liminf_n\|x_n\|\) when \(x_n\rightharpoonup x\).

Banach–Alaoglu: the dual unit ball \(B_{X^*}\) is compact in \(\sigma(X^*,X)\), by embedding it as a closed subset of \(\prod_{x\in X}\{z:|z|\le\|x\|\}\). This is not generally sequential compactness; if \(X\) is separable, the weak-star topology on bounded subsets of \(X^*\) is metrizable.

If \(X\) is reflexive, its closed bounded subsets are relatively weakly compact. In a Banach space, Eberlein–Šmulian also relates weak compactness and weak sequential compactness; reflexivity is a *hypothesis*, not a consequence of boundedness.

### Exercises with answers

1. **Coordinate test.** Why is \(e_n\rightharpoonup0\) in \(\ell^2\)? **Answer:** For each \(y\in\ell^2\), \(y_n\to0\), hence \(\langle e_n,y\rangle\to0\).
2. **Norm test.** Does \(\|e_n\|_2\to0\)? **Answer:** No; every norm equals one.
3. **Weak limit energy.** If \(u_n\rightharpoonup u\) and \(\|u_n\|\le4\), what follows? **Answer:** \(\|u\|\le4\), by weak lower semicontinuity.

### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)
- [Princeton MAT520 Functional Analysis lecture notes](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT520_fall_2025/MAT520_Lecture_Notes.pdf)
