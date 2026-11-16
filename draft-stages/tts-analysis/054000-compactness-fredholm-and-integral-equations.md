# 054000 — Compact Operators, Fredholm Alternatives, and Integral Equations

**Track:** Analysis from First Principles. **Background:** Hilbert-space operators, spectra and bounded inverse theorem. **Central question:** Why does a nearly finite-dimensional operator behave differently from an arbitrary infinite-dimensional one?

<!-- BEGIN SPOKEN LECTURE -->

# Compact Operators, Fredholm Alternatives, and Integral Equations

A system of one thousand equations can be solved by matrix elimination, at least in principle. A system with infinitely many unknowns is different. Even a linear equation that seems perfectly harmless can have an inverse that amplifies small errors without bound. Compact operators occupy a middle ground: they act on infinite-dimensional spaces, yet they preserve enough of the finite-dimensional picture to recover a useful existence theory.

A compact operator is one that sends the unit ball into a set whose closure is compact. That means every bounded sequence of inputs has a subsequence whose outputs converge. Notice the asymmetry: the input sequence itself need not have any convergent subsequence. The operator is doing the compression.

Consider a diagonal operation on square-summable sequences. Keep the first coordinate unchanged, divide the second by two, divide the third by three, and so on. The outputs of high-coordinate basis vectors approach zero. If we discard all coordinates beyond N, we get a finite-rank operator. The difference between the original operation and the truncation has norm at most one divided by N plus one. Thus the full operator is a norm limit of finite-rank operators and is compact.

Contrast that with the identity. Apply it to the sequence of standard basis vectors: each vector has norm one and any two are separated by the square root of two. No subsequence converges. So identity is not compact on an infinite-dimensional Hilbert space. Compactness is a strong form of smoothing or loss of fine-scale detail, not merely boundedness.

Now turn to an integral equation. Imagine an unknown function u that contributes to an observed value at x by an average over all other locations. We can write the output as the integral of a kernel K of x and y multiplied by u of y. If K is square integrable over the pair of variables, this integral operator is compact on the corresponding L two space. One can see why by approximating the kernel by a finite sum of separated terms: one function of x times another function of y. Each separated term extracts a single scalar measurement from u and produces a fixed output shape. A finite sum has finite-dimensional range. Approximate the kernel in square-integral norm, and the resulting operators approach in operator norm.

The central equation is u minus K applied to u equals f. This looks like a perturbed identity. In finite dimensions, either the associated matrix has an inverse or the homogeneous equation has a nonzero solution. For a compact K, the Fredholm alternative recovers essentially this dichotomy even though the space is infinite dimensional.

Specifically, for a compact operator K on a Hilbert space, if the equation u minus K u equals zero has only the zero solution, then one minus K is invertible. In other words, uniqueness for the homogeneous equation forces existence and uniqueness for every forcing f. When the homogeneous equation has nonzero solutions, compatibility conditions appear. The forcing must be orthogonal to solutions of the adjoint homogeneous equation.

The adjoint condition is worth hearing slowly. Suppose v is annihilated by one minus the adjoint of K. If f equals u minus K u, take the inner product of f with v. Move K onto the other side of the inner product. The result is the inner product of u with v minus the adjoint of K applied to v, which is zero. Hence any solution f must be orthogonal to every such v. This is not an arbitrary technical constraint. It expresses a conservation law in the linear algebra of the problem: there are directions of the output space that the operator cannot reach.

A concrete rank-one example makes the whole theory visible. On L two of the interval from zero to one, let K send every function to its average, treated as a constant function. Apply K twice: taking the average of a constant changes nothing. So K is a projection. If we try to solve u minus K u equals f, take averages of both sides. The left side has average zero. Thus the forcing must have average zero. If that holds, u can be chosen equal to f plus any constant. We have infinitely many possible constants, one-dimensional nonuniqueness, and one linear compatibility condition. The kernel of one minus K is exactly the constant functions.

Now scale K by a number smaller than one in magnitude. The perturbed operator one minus alpha K is invertible. On constant functions it multiplies by one minus alpha; on mean-zero functions it acts as the identity. Its inverse can therefore be written down without any infinite series. As alpha approaches one, the inverse becomes large on constants. We can see the instability approaching the resonance where the homogeneous equation develops a solution.

This is the practical role of the Fredholm alternative in boundary-value problems and integral equations. A compact perturbation of identity has a finite-dimensional obstruction to solvability rather than an uncontrolled infinite-dimensional failure. But the theorem does not say every integral operator is compact, nor that a compact operator itself is invertible. Indeed, a compact operator on an infinite-dimensional space cannot be both boundedly invertible and onto the same space. If it were, the identity would be compact as a composition of its inverse with it, contradicting the basis-vector example.

The right mental model is not that infinity disappears. It is that a smoothing operation can isolate the troublesome directions into a finite-dimensional part. We can then analyze resonance, compatibility, and stability much as we would for a matrix, while retaining the functional setting needed for real differential and integral equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For compact \(K:H\to H\) on a Hilbert space, the Fredholm alternative for \(I-K\) states: its kernel and cokernel are finite dimensional, its range is closed, and
\[ \operatorname{ran}(I-K)=\ker(I-K^*)^\perp. \]
The Fredholm index is zero: \(\dim\ker(I-K)=\dim\ker(I-K^*)\). In particular, injectivity is equivalent to surjectivity. More generally \(I-\lambda K\), \(\lambda\in\mathbb C\), is Fredholm of index zero.

If \(k\in L^2((0,1)^2)\), the Hilbert–Schmidt operator \((Ku)(x)=\int_0^1k(x,y)u(y)\,dy\) is compact. Finite-rank approximations arise from dense finite sums \(\sum_j a_j(x)b_j(y)\). Hilbert–Schmidt norm controls operator norm.

For \(Pu=(\int_0^1u)\mathbf 1\), \(P^2=P=P^*\), \(\operatorname{ran}P=\operatorname{span}\{\mathbf1\}\). The equation \((I-P)u=f\) is solvable iff \(\int_0^1f=0\), and then \(u=f+c\). If \(\alpha\ne1\),
\[ (I-\alpha P)^{-1}=I+\frac{\alpha}{1-\alpha}P. \]

### Exercises with answers

1. **Compact diagonal.** Why is \(K e_n=n^{-1}e_n\) compact on \(\ell^2\)? **Answer:** Truncate at N; the operator norm error is \((N+1)^{-1}\).
2. **Solvability.** What must \(f\) satisfy to solve \((I-P)u=f\)? **Answer:** Zero integral over the interval.
3. **Near resonance.** What happens to the inverse bound as real \(\alpha\to1\)? **Answer:** The eigenvalue on constants is \(1-\alpha\), hence inverse norm grows at least \(|1-\alpha|^{-1}\).

### Reading and source notes

- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
