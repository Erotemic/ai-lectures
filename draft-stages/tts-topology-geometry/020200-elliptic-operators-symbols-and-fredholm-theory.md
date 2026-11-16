# 020200 — Elliptic Operators: From Their Symbols to Finite-Dimensional Obstructions

**Track:** Topology and Geometry. **Background:** partial derivatives, Hilbert spaces, Fourier modes, compactness, linear operators. **Central question:** why do some differential equations have only finitely many independent obstructions to being solved?

<!-- BEGIN SPOKEN LECTURE -->

# Elliptic Operators: From Their Symbols to Finite-Dimensional Obstructions

Consider the equation that asks for a function on a closed surface whose Laplacian equals a given source function. On a flat torus we can analyze the equation using Fourier modes. High-frequency modes are controlled strongly by the Laplacian, and the main difficulty occurs at the constant mode: the derivative of a constant is zero, so the Laplacian cannot distinguish one constant from another.

This example contains the central idea of elliptic theory. Although a differential operator acts on infinite-dimensional spaces of functions, its failure of invertibility can be confined to finite-dimensional kernel and cokernel spaces. The correct language for that phenomenon is Fredholm theory.

## The easiest necessary condition

Suppose the Laplacian of u equals f on a compact connected manifold without boundary. Integrate both sides over the manifold. Integration by parts tells us that the integral of the Laplacian is zero. Therefore the integral of f must be zero. A constant positive source cannot be the Laplacian of a globally defined smooth function on such a manifold.

The condition is also sufficient for this operator, once elliptic existence theory is available. If f has mean zero, there is a smooth solution, and any two solutions differ by a constant. The kernel consists of constants. The obstruction to solving the equation is the single scalar condition that f have integral zero.

That is a model of a Fredholm alternative: either the equation is solvable, or its right-hand side fails one or more compatibility conditions determined by solutions of the adjoint homogeneous equation.

## Look at high-frequency behavior

To understand why this can happen, examine how a differential operator acts on a rapidly oscillating wave. Differentiation multiplies an oscillation by its frequency. A second derivative multiplies it by frequency squared. For the negative Euclidean Laplacian, a wave with frequency vector xi is multiplied by the squared length of xi.

The highest-order part of an operator can be recorded as a function of position and frequency, called its principal symbol. For the Laplacian, that symbol is positive for every nonzero frequency. There is no direction in frequency space in which the leading derivative control disappears.

An operator is elliptic when its principal symbol is invertible for every nonzero cotangent vector. For scalar Laplace-type operators, this says that the leading symbol never vanishes away from zero frequency. For operators between vector bundles, it requires an invertible linear map between the fibers at every nonzero covector.

Ellipticity is a high-frequency condition. It does not assert that the operator itself is invertible. The Laplacian is elliptic but has constants in its kernel. The symbol tells us that its failure of invertibility cannot be caused by arbitrarily many unconstrained high-frequency modes on a compact manifold.

## What compactness contributes

Elliptic estimates say, roughly, that the stronger norm of a solution is controlled by a weaker norm of the input plus a lower-order term. On a compact manifold, bounded sets in a sufficiently strong Sobolev space are compact in a weaker Sobolev space. That compact embedding is a crucial second ingredient.

Together, elliptic regularity and compactness lead to finite-dimensional kernel and cokernel and closed range for an elliptic differential operator acting between appropriate Sobolev spaces. This is the Fredholm property. It is not generally guaranteed on a noncompact manifold or without adequate boundary conditions. A differential expression written in coordinates does not automatically specify a closed operator with a suitable domain.

Elliptic regularity adds another statement: a weak solution becomes smoother when the coefficients and forcing have appropriate regularity. On a compact manifold, a smooth forcing term produces smooth solutions to an elliptic equation, modulo the usual compatibility conditions.

## A first example with a nontrivial cokernel

Consider differentiation around a circle. The derivative of a periodic function has integral zero over a full period. Conversely, if a periodic target function has integral zero, integrating it produces a periodic antiderivative after choosing a constant of integration.

The kernel of differentiation consists of constants. Its image consists of mean-zero functions, so the cokernel can be represented by the missing constant direction. Both are one-dimensional. Their dimension difference is zero. Thus the derivative on the circle is a simple elliptic Fredholm operator with nonzero kernel and cokernel but index zero.

The principal symbol here is multiplication by a nonzero imaginary frequency, so it is invertible whenever the frequency is nonzero. The example makes clear that ellipticity concerns the leading behavior, while kernel and cokernel concern the full global operator.

## The index as a stable integer

For a Fredholm operator, define its index as the dimension of its kernel minus the dimension of its cokernel. An operator may lose a kernel vector under a perturbation while gaining an obstruction elsewhere. Yet the index remains stable under appropriate continuous Fredholm deformations, and in particular under compact perturbations.

For elliptic differential operators on a compact manifold, lower-order perturbations do not change the principal symbol and do not change the Fredholm index. This is why the index can be governed by the topology of the symbol rather than by every lower-order coefficient in a differential equation.

The Atiyah–Singer index theorem is the deep general result connecting the analytic index to topological data. We are not proving it here. We are making its two sides intelligible: the analytic side counts kernel and cokernel, while the symbol defines a topological object on the nonzero cotangent directions.

## How this supports Hodge theory

The Hodge Laplacian is elliptic. Its kernel is the space of harmonic differential forms, which is therefore finite-dimensional on a compact closed manifold. An elliptic decomposition also allows us to solve the Laplace equation orthogonally to that kernel. From there one obtains the exact, coexact, and harmonic decomposition of forms.

Thus the statement that each de Rham cohomology class has a unique harmonic representative depends on analytic facts: ellipticity, compactness, closed range, and regularity. These facts are not consequences of merely writing down the identity that the exterior derivative applied twice is zero.

Later gauge theory uses similar ideas. Linearizing a nonlinear equation produces a differential operator or elliptic complex. Its kernel models infinitesimal solutions, its image may include gauge directions, and its cokernel models obstructions. The Fredholm index predicts a virtual dimension even before a nonlinear moduli space is constructed.

That is the foundational insight: infinite-dimensional equations can have finite-dimensional obstruction theory. The principal symbol controls the high frequencies; compactness controls the global remainder; and the index records a stable algebraic difference. With those ideas in place, an index theorem is no longer an unexplained formula linking unrelated subjects.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a differential operator \(P\) of order m between bundles \(E\to M\), \(F\to M\), its principal symbol \(\sigma_m(P)(x,\xi):E_x\to F_x\) records highest-order derivatives. Ellipticity requires \(\sigma_m(P)(x,\xi)\) invertible for \(\xi\ne0\). For the positive Laplace–Beltrami operator \(\Delta=-\operatorname{div}\nabla\), \(\sigma_2(\Delta)(x,\xi)=|\xi|_g^2\).

On a smooth compact manifold without boundary, an elliptic differential operator has a Fredholm realization \(P:H^{s+m}(E)\to H^s(F)\) for appropriate Sobolev spaces. The Fredholm index is \(\operatorname{ind}P=\dim\ker P-\dim\operatorname{coker}P\), invariant under compact perturbations and continuous paths of Fredholm operators. For connected closed \(M\), \(\Delta u=f\) is solvable iff \(\int_M f\,dV=0\), with solutions unique modulo constants.

On \(S^1=\mathbf R/(2\pi\mathbf Z)\), \(P=\partial_\theta:H^{s+1}\to H^s\) has \(\ker P=\mathbf R\cdot1\), range the mean-zero functions, and \(\operatorname{coker}P\cong\mathbf R\). Thus \(\operatorname{ind}P=0\). Its first-order symbol (with Fourier convention) is \(i\xi\), invertible for \(\xi\ne0\). Boundaries and noncompact domains require additional hypotheses, domains, or boundary conditions for Fredholmness.

### Exercises with answers

1. **Laplacian compatibility.** Could \(\Delta u=1\) hold on a connected closed manifold? **Answer:** No. Integrating gives \(0=\operatorname{vol}(M)>0\).
2. **Derivative on a circle.** Can \(u'(\theta)=\cos\theta\) have a periodic solution? **Answer:** Yes, \(u=\sin\theta+C\).
3. **Obstruction.** Can \(u'(\theta)=2\) have a periodic solution? **Answer:** No, because the target has nonzero mean.
4. **Index.** If an operator has kernel dimension three and cokernel dimension one, what is its index? **Answer:** Two.

### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds, Fredholm operator lectures](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- University of Notre Dame, [Elliptic operators on compact manifolds](https://academicweb.nd.edu/~lnicolae/Pseudo.pdf).
- Overviews: [Elliptic operator](https://en.wikipedia.org/wiki/Elliptic_operator), [Fredholm operator](https://en.wikipedia.org/wiki/Fredholm_operator).
