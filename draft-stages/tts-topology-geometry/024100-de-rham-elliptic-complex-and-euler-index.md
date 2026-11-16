# 024100 — An Index Theorem We Can Calculate: The de Rham Operator and Euler Characteristic

**Track:** Topology and Geometry. **Background:** Hodge star and codifferential, ellipticity, Fredholm index, de Rham cohomology. **Central question:** can we prove one analytic index equals one topological invariant without hiding all the steps?

<!-- BEGIN SPOKEN LECTURE -->

# An Index Theorem We Can Calculate: The de Rham Operator and Euler Characteristic

The Atiyah–Singer index theorem says, in great generality, that an analytic number defined by solutions of an elliptic differential equation can equal a topological number defined by geometry and characteristic classes. Its general formula requires substantial background. But one important case can be understood using tools we already know: the exterior derivative, its adjoint, Hodge theory, and the Euler characteristic.

In this lecture we will construct an elliptic operator on differential forms and compute its index for the circle, sphere, and torus. The result is a small index theorem with a complete chain of ideas: differential equations produce harmonic forms, harmonic forms represent cohomology, and an alternating count of cohomology dimensions produces the Euler characteristic.

## Even-degree forms and odd-degree forms

On an n-dimensional manifold, differential forms have degrees from zero through n. A function is a zero-form, a one-form measures directions, and a top-degree form measures oriented volume. The exterior derivative moves one degree upward. Its adjoint, the codifferential, moves one degree downward.

Now add those two operations into a single operator: exterior derivative plus codifferential. It changes parity. Even-degree forms are sent to odd-degree forms, and odd-degree forms are sent to even-degree forms. Restrict the operator to the direction from even forms to odd forms.

This parity split is what allows a nontrivial Fredholm index. We are comparing the dimensions of special even and odd solutions, rather than merely the kernel of a positive self-adjoint operator with itself.

## Why the operator is elliptic

At high frequencies, exterior differentiation acts like wedging with the frequency covector. Its adjoint acts like contraction with the same covector, with a sign. Adding them gives an algebraic operation analogous to Clifford multiplication.

The key identity is that applying this leading symbol twice gives minus the squared length of the frequency times the identity. If the frequency is nonzero, that algebraic map is invertible. Thus the de Rham operator is elliptic.

On a compact manifold without boundary, elliptic theory tells us that its even-to-odd restriction is Fredholm between suitable Sobolev spaces. Its kernel and cokernel are finite-dimensional, so the index is a well-defined integer. The analytical assumptions matter: on an open manifold or a manifold with boundary, the analogous claim requires more work and suitable domains or boundary conditions.

## What is in the kernel?

Square the full de Rham operator. Because the exterior derivative applied twice is zero, and likewise the codifferential squared is zero, the square reduces to the Hodge Laplacian.

On a compact closed manifold, a form is killed by the Laplacian exactly when it is both closed and co-closed. Such forms are harmonic. If an even form is in the kernel of the parity-restricted de Rham operator, the energy identity shows it is harmonic. Conversely, a harmonic even form is plainly in the kernel.

Thus the kernel is the space of harmonic even-degree forms. The formal adjoint of the even-to-odd operator is the same full de Rham operator restricted in the opposite direction. Its kernel consists of harmonic odd-degree forms. The cokernel of a Fredholm operator is represented by the kernel of its adjoint.

Therefore the index is the total dimension of harmonic even forms minus the total dimension of harmonic odd forms.

## Hodge theory turns analysis into topology

Hodge's theorem gives one and only one harmonic representative for each real de Rham cohomology class on a compact oriented Riemannian manifold without boundary. So the dimension of harmonic k-forms equals the kth Betti number.

Substitute that equality into the analytic index. What remains is an alternating sum of Betti numbers: degree zero contributes positively, degree one negatively, degree two positively, and so on. That alternating sum is the Euler characteristic.

We have proved the index formula for the de Rham operator, assuming the Hodge theorem and elliptic Fredholm facts already established: its index equals the Euler characteristic of the manifold.

The operator was built using a Riemannian metric. The Euler characteristic does not depend on the metric. This explains one form of index stability. Change the metric smoothly and the space of individual harmonic forms changes, but their alternating dimension difference remains topological. In fact, Hodge theory tells us each Betti number separately is fixed.

## Three complete examples

First, the circle. Harmonic zero-forms are constants, giving one even solution. Harmonic one-forms are constant multiples of the angle one-form, giving one odd solution. The index is one minus one, or zero. The circle's Euler characteristic is zero.

Second, the two-sphere. Harmonic zero-forms are constants. Harmonic two-forms are multiples of the oriented area class. There are no nonzero harmonic one-forms because the sphere has no first real cohomology. The even kernel has dimension two and the odd adjoint kernel has dimension zero. The index is two. The sphere's Euler characteristic is two.

Third, the flat two-torus. Constants give one harmonic zero-form, the two independent coordinate one-forms give two harmonic one-forms, and the area form gives one harmonic two-form. The even count is two, and the odd count is two. The index is zero, matching the torus's Euler characteristic.

No one needed to solve a complicated partial differential equation in coordinates for these examples. The topology supplied the dimensions through Hodge theory. But the PDE framework is still essential to know that the analytic operator has the claimed kernel and cokernel.

## What this does not prove

The full Atiyah–Singer theorem applies to broad classes of elliptic operators, not just the de Rham operator. It relates their symbol classes to characteristic-class expressions. Other operators require additional structures: spinor bundles, complex structures, twisting bundles, or specialized boundary conditions. It would be wrong to conclude that every elliptic operator has index equal to the Euler characteristic.

In particular, the spin and spin-C Dirac operators used in gauge theory are different operators, though they share the same general Dirac-type algebraic pattern. Their indices may involve the A-hat genus, Chern characters, and other characteristic-class data. The de Rham example is a foundation, not a substitute for those later formulas.

The important conceptual achievement is already here. We began with a local differential expression on forms. Ellipticity made its global kernel and cokernel finite-dimensional. Hodge theory identified them with topological cohomology. Their alternating dimension difference became the Euler characteristic. This is the analytic-to-topological bridge that an index theorem is designed to cross.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(M\) be compact, oriented, Riemannian and boundaryless. Let \(D=d+\delta:\Omega^*(M)\to\Omega^*(M)\). Since \(d^2=\delta^2=0\), \(D^2=\Delta\). Separate parity, \(D^+:\Omega^{\mathrm{even}}\to\Omega^{\mathrm{odd}}\), \(D^-:\Omega^{\mathrm{odd}}\to\Omega^{\mathrm{even}}\), with \((D^+)^*=D^-\).

The principal Clifford symbol (suppressing the harmless Fourier factor i) is \(c(\xi)=\varepsilon(\xi)-\iota_{\xi^\sharp}\). The identity \(c(\xi)^2=-|\xi|^2\operatorname{id}\) follows from the exterior algebra anticommutation relations, so \(D\) is elliptic. On a compact closed M, elliptic Fredholm theory applies. The Hodge energy identity gives \(\ker D^+=\mathcal H^{\mathrm{even}}\), \(\ker D^-=\mathcal H^{\mathrm{odd}}\). Hence
\[\operatorname{ind}D^+=\sum_{k\ \mathrm{even}}\dim\mathcal H^k-\sum_{k\ \mathrm{odd}}\dim\mathcal H^k=\sum_{k=0}^n(-1)^kb_k(M)=\chi(M).\]
For \(S^1\), \((b_0,b_1)=(1,1)\) and index zero; for \(S^2\), \((1,0,1)\) and index two; for \(T^2\), \((1,2,1)\) and index zero. This is the de Rham or Euler operator index formula, one special case in the general framework of Atiyah–Singer. The spin or spin-C Dirac operator has a different associated bundle and index formula; it is not identified with \(D\).

### Exercises with answers

1. **Parity.** Does d preserve parity of form degree? **Answer:** No. It raises degree by one and exchanges even with odd.
2. **Square.** Why is \((d+\delta)^2=d\delta+\delta d\)? **Answer:** The terms \(d^2\) and \(\delta^2\) vanish.
3. **Sphere.** Compute the index of \(D^+\) on \(S^2\). **Answer:** \(1+1-0=2\).
4. **Scope.** Must the spin-C Dirac operator on an arbitrary four-manifold have index equal to \(\chi(M)\)? **Answer:** No. Its index is governed by different characteristic data.

### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds, Fredholm notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- University of Notre Dame, [Elliptic operators on compact manifolds](https://academicweb.nd.edu/~lnicolae/Pseudo.pdf).
- Overviews: [Atiyah–Singer index theorem](https://en.wikipedia.org/wiki/Atiyah%E2%80%93Singer_index_theorem), [Hodge theory](https://en.wikipedia.org/wiki/Hodge_theory).
