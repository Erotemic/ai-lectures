# 024300 - Elliptic Regularity: From Weak Solutions to Smooth Fields

**Track:** Topology and Geometry. **Background:** weak derivatives, Sobolev spaces, principal symbols, Hodge Laplacian. **Central question:** why does an elliptic differential equation often improve a rough solution's regularity?

<!-- BEGIN SPOKEN LECTURE -->

# Elliptic Regularity: From Weak Solutions to Smooth Fields

In the previous lecture, a bound on derivatives let us define limits, but it did not make those limits smooth. Advanced geometry often begins with weak solutions because weak limits are available; it then ends by proving that those solutions were smooth after all. What closes that gap?

The answer is elliptic regularity. An elliptic differential operator cannot ignore oscillations in one spatial direction while controlling another. Its leading symbol is invertible at every nonzero frequency. That condition turns a differential equation into an estimate for all derivatives of the unknown, up to some finite-dimensional obstruction.

## A circle where we can see every frequency

Work first on a circle with angular coordinate theta. Let the operator be minus the second derivative. Suppose the forcing term is a sine wave with frequency ten. A solution is the same sine wave divided by one hundred. More generally, at frequency k, solving the equation divides the Fourier coefficient by k squared.

That is two derivatives of improvement. High-frequency oscillations become progressively smaller in the solution than they were in the forcing term. If the forcing term has square-integrable size, the nonconstant part of the solution has two square-integrable derivatives. If the forcing term is smoother, the solution becomes smoother still.

There is a catch: constants are killed by the second derivative. The equation has a solution on the circle only if the forcing term has average zero, and solutions are then determined only up to an additive constant. This is a tiny example of Fredholm theory. We do not need the operator to be invertible to control all the components perpendicular to its kernel.

## An estimate is not an inverse formula

On a compact closed manifold, an elliptic operator of order m gives an estimate of the following shape: the Sobolev norm of a section with s plus m derivatives is bounded by a constant times the Sobolev norm of the operator applied to that section with s derivatives, plus a lower-order norm of the section itself.

That extra lower-order term is not mere bookkeeping. It prevents us from claiming that a kernel element has to vanish. The constants on the circle are the simplest example. More complicated elliptic operators have finite-dimensional kernels corresponding to harmonic forms, spinors, or infinitesimal deformations.

To derive such an estimate, one freezes coefficients at a point, uses the inverse of the principal symbol for high frequencies, and then repairs the lower-order error. On a manifold, local constructions are patched with a partition of unity. A full proof requires pseudodifferential or carefully organized energy-estimate methods. The geometric insight is that nonzero frequencies are uniformly controlled, while zero modes and global topology survive as finite-dimensional data.

## Bootstrapping a nonlinear equation

Now suppose the equation is nonlinear. Write it schematically as an elliptic operator on a field equals a product of fields and their lower derivatives. We can start with a weak solution whose derivatives lie in a Sobolev space. Sobolev multiplication may place the right-hand side in a better integrability space. An elliptic estimate can then give the solution additional derivatives. Repeat, and under suitable smoothness and dimensional hypotheses the solution becomes smooth.

But the words 'under suitable hypotheses' carry serious weight. At a critical exponent, a quadratic term may not improve the integrability enough for a naive iteration. There may also be gauge redundancy, meaning the ungauged differential operator is not elliptic. In gauge theory one first imposes a slice or gauge condition and then proves the regularity statement for the resulting elliptic system.

A common mistake is to see the word elliptic in a theorem about one operator and silently transfer every regularity result to a nonlinear gauge-invariant equation. We have to identify the operator, its domain, the chosen gauge, the regularity of coefficients, and the source term.

## Hodge theory as a regularity machine

Recall the Laplacian on differential forms. It is elliptic. A harmonic form solves the equation with zero forcing. Initially we can interpret that equation weakly in a Sobolev space. Elliptic regularity says a weak harmonic form on a closed smooth manifold is in fact smooth.

That is one reason Hodge theory can compare analytic objects with classical de Rham cohomology. We need not assume that every object in a Hilbert-space kernel was smooth to begin with. The equation makes it smooth. This also justifies speaking of a finite-dimensional space of smooth harmonic representatives after defining a self-adjoint elliptic operator using functional analysis.

## Two kinds of compactness

We can now distinguish two steps in a standard existence argument. Functional analysis may produce a weakly convergent subsequence of approximate solutions. The equation and elliptic estimates may upgrade regularity of the limit. If the estimates are uniform on the whole family, compact Sobolev embeddings can yield strong convergence in a lower norm, and sometimes smooth convergence after bootstrapping.

But curvature concentrations in four dimensions can prevent uniform estimates in the needed gauges. Then elliptic regularity is still available on regions where curvature stays controlled, while small balls around concentration points require separate treatment. This is the beginning of the Uhlenbeck compactness story, not a failure of elliptic regularity itself.

The general method is worth remembering. First choose a complete space in which limits exist. Second obtain an elliptic equation or gauge-fixed system. Third prove an estimate that gains derivatives. Fourth establish whatever compactness is needed to pass from approximations to a solution. Advanced geometry becomes more comprehensible when these steps are explicit instead of being compressed into the single phrase 'standard elliptic theory.'

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(L=-\partial_\theta^2\) on \(S^1\), write \(f=\sum_k f_ke^{ik\theta}\), \(u=\sum_k u_ke^{ik\theta}\). The equation \(Lu=f\) is solvable iff \(f_0=0\); then \(u_k=f_k/k^2\) for \(k\ne0\), while \(u_0\) is arbitrary. For \(s\in\mathbb R\), \(\|u-u_0\|_{H^{s+2}}\le C\|f\|_{H^s}\).

For a smooth elliptic differential operator \(P\) of order \(m\) on a closed manifold,
\[\|u\|_{H^{s+m}}\le C_s(\|Pu\|_{H^s}+\|u\|_{H^s}).\]
For suitable distributional solutions \(Pu=f\), this estimate plus localization and approximation yields \(f\in H^s\Rightarrow u\in H^{s+m}\) locally (and globally on a closed manifold), provided the coefficients are smooth. Elliptic regularity is distinct from invertibility: \(\ker P\) may be nonzero.

For the Hodge Laplacian \(\Delta=d\delta+\delta d\), \(\sigma_2(\Delta)(x,\xi)=|\xi|^2\operatorname{id}\) up to Fourier-sign convention. Weak harmonic forms therefore are smooth.

### Exercises with answers

1. **Fourier solution.** Solve \(-u''=\sin(3\theta)\). **Answer:** \(u=\sin(3\theta)/9+C\).
2. **Compatibility.** Can \(-u''=1\) have a periodic solution? **Answer:** no; the right side has nonzero average.
3. **Kernel.** Does ellipticity force an operator to have trivial kernel? **Answer:** no; constants lie in the kernel of the circle Laplacian.
4. **Gauge.** Why can a gauge-invariant curvature equation fail to be elliptic before choosing a slice? **Answer:** variations along gauge orbits are redundant directions in the principal symbol of the naive linearization.

### Sources and further reading

- Harvard Math 212b, [Elliptic Engineering](https://people.math.harvard.edu/archive/212_spring01/lectures/ellipticity.pdf), including estimates and interior regularity.
- MIT OpenCourseWare, [Geometry of Manifolds lecture notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overviews: [Elliptic partial differential equation](https://en.wikipedia.org/wiki/Elliptic_partial_differential_equation), [Elliptic regularity](https://en.wikipedia.org/wiki/Elliptic_operator).
