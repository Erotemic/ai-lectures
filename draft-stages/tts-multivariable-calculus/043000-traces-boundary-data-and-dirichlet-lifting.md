# Traces and Boundary Data: How an Energy Solution Meets the Edge

**Track:** Multivariable Calculus from First Principles. **Focus:** the one-dimensional trace estimate, boundary layers, higher-dimensional Sobolev traces, inhomogeneous Dirichlet data, and the lifting method.

<!-- BEGIN SPOKEN LECTURE -->

# Traces and Boundary Data: How an Energy Solution Meets the Edge

Suppose a heated metal plate has its rim held at a prescribed temperature. Inside the plate, an energy calculation predicts a temperature field. We might expect the resulting function to have a value at every point, including every point of the rim. But the existence proof for a weak elliptic equation often produces something more modest: a function whose value and first weak derivatives are square integrable. Such a function is defined only up to changes on sets of zero area or volume. The boundary itself has zero interior volume. In that setting, writing that the temperature equals ten on the edge is not yet a mathematical condition.

There is a precise way to give the boundary a meaning. It is called a trace. Rather than insist that every energy solution possess an ordinary pointwise restriction, we ask whether boundary values of smooth functions extend continuously when we complete those functions in the energy norm.

This is a subject where a small calculation on a string teaches us more than a slogan about function spaces. Let us start with the interval from zero to one.

## Why the endpoint remembers the derivative

Take a smooth function u on the unit interval. The fundamental theorem of calculus says that its value at a point x equals its value at zero plus the integral of its derivative from zero to x. Now average this equation over all x between zero and one. When we reverse the order of integration, we find a useful identity: the value of u at zero equals its average over the interval, minus the integral of its derivative weighted by one minus x.

Apply Cauchy–Schwarz separately to those two integrals. The magnitude of the endpoint value is at most the L two norm of u, plus one over the square root of three times the L two norm of its derivative. That is a trace estimate in one dimension. A boundary measurement, which might initially look like a pointwise operation, is controlled by an integral norm involving one derivative.

The same argument works at the right endpoint. Since smooth functions are dense in the first-order Sobolev space H one on an interval, both endpoint evaluations extend continuously to all H one functions. In fact, each such function has an absolutely continuous representative, and its endpoint values agree with that representative. No guess about the values on a measure-zero set is required. The trace is determined by the equivalence class and the derivative energy.

What if we tried to measure the endpoint from the L two norm alone? Build a narrow triangular spike with height one at the left endpoint and width epsilon, vanishing outside that tiny interval. The squared area under the spike tends to zero as epsilon shrinks. Its endpoint value stays one. Therefore no inequality can bound endpoint evaluation by the L two norm alone. But the slope becomes as large as the reciprocal of epsilon, so its derivative energy grows instead of disappearing. Adding one derivative to the norm prevents us from hiding a nonzero boundary value in an arbitrarily narrow layer.

This is the difference between a measurement that is continuous in a function space and one that is not. An operation is not automatically well defined on weak solutions just because it makes sense on smooth trial functions.

## What changes for a membrane or a solid

On a bounded domain with a Lipschitz boundary, the first-order L two Sobolev space has a continuous trace map into a boundary Sobolev space of order one half. The boundary may have corners, but it must be regular enough for the usual extension and trace theorems. For a smooth function this trace is ordinary restriction. For a general H one function, approximate by smooth functions and take the limit of their boundary restrictions in the appropriate boundary norm.

Why one half of a derivative? A boundary has one fewer spatial dimension than the interior. Restriction concentrates information onto a thinner set. In Fourier descriptions on a half-space, the amount of tangential smoothness the interior H one norm controls is a half order. We do not need that Fourier proof to use the theorem, but we must remember its consequence: not every arbitrary L two boundary signal is an admissible Dirichlet trace of an H one interior field.

There is also a lifting theorem. Every boundary datum in the trace space can be extended into an H one function on the interior, and this extension can be chosen by a bounded linear operator. We call any such interior function a lift of the boundary data. The lift is generally not unique. That is a feature, not a problem: the boundary information determines a class of interiors, and the differential equation will select the one we seek.

The familiar space H naught one consists of limits, in the H one norm, of smooth functions supported away from the boundary. On bounded Lipschitz domains, it is exactly the set of H one functions with zero trace. Thus an equation with a fixed zero boundary value can be posed using H naught one as both its trial and test space. For a nonzero boundary value, we use an affine space instead: one chosen lift plus every function in H naught one.

This distinction between a linear space of variations and an affine space of admissible solutions is the same geometry we saw in constrained optimization. The data determine the constraint; the zero-boundary variations describe the permitted directions away from a given admissible state.

## Turning nonzero boundary data into a zero-boundary problem

Consider negative Laplacian u equals f on a bounded domain, with the trace of u prescribed as g. Pick an H one lift G whose trace is g. Write u as G plus w. The new unknown w has zero trace, so w belongs to H naught one.

The weak equation for u says the integral of the gradient of u dotted with the gradient of every zero-boundary test function v equals the applied load acting on v. Substitute G plus w. The integral involving w moves to the left, while the integral involving G moves to the right with a minus sign. The result is a standard zero-boundary problem for w, but with an adjusted forcing functional.

In symbols, as spoken rather than written: gradient w paired with gradient v equals the original forcing paired with v, minus gradient G paired with gradient v. The boundary data have not been discarded. They have become part of the right-hand side.

This makes the existence argument straightforward. The gradient bilinear form is coercive on H naught one by Poincaré's inequality. The original load is bounded when f is an appropriate weak source, and the extra term from G is bounded by Cauchy–Schwarz. Lax–Milgram therefore gives a unique w, hence a unique u with the requested trace. The size of u can be controlled in terms of the forcing and the trace norm of g, because the lifting operator is bounded.

There is a qualification worth hearing. The theorem is about an energy solution in H one. It does not say the solution has pointwise second derivatives or that the prescribed trace is continuous at every boundary point. Those are additional regularity questions. We will encounter a domain where the forcing is smooth but second derivatives are not square integrable near a corner.

## A complete one-dimensional lift

Let us carry out the substitution rather than leave it abstract. On the unit interval, solve negative u double prime equals two, with u at zero equal to one and u at one equal to two. An affine lift matching the two endpoints is G of x equals one plus x.

Write u equals G plus w. The function w must vanish at both endpoints. Since G has zero second derivative, w solves negative w double prime equals two with zero endpoint values. We can solve it directly: w of x equals x times one minus x. Therefore u of x is one plus x plus x times one minus x, or one plus two x minus x squared.

Check it. The second derivative is negative two, so the negative second derivative is two. At zero, u is one; at one, u is two. The weak problem also works: the derivative of G is the constant one, and its product with the derivative of a zero-endpoint test function integrates to the test function's endpoint difference, which is zero. Thus this particular lift introduces no additional weak forcing.

If instead we picked a curved lift, for example one plus x plus x times one minus x, we would get a different zero-boundary correction, and the extra gradient term on the right would no longer vanish. But the final u would be unchanged. A good lift is chosen for convenience or for estimates; it does not alter the physical boundary-value problem.

## Two kinds of data at the edge

So far the boundary temperature was prescribed. That is a Dirichlet condition, sometimes called an essential boundary condition in finite-element terminology. We encode it in the set of admissible functions. The test functions have zero trace wherever the temperature is fixed.

But perhaps the engineer does not prescribe temperature. Perhaps the engineer prescribes heat flux through the edge. Integration by parts then produces a normal-flux term on the boundary. Such Neumann data enter the right-hand side of the weak equation rather than the trial space. A weak solution in H one does not necessarily have a classical pointwise normal derivative, so the flux may have to be interpreted through a Green identity and a dual boundary pairing.

It would be a mistake to treat all boundary data as if they were pointwise restrictions of the same order. An H one solution has a trace in the fractional boundary space, while its normal derivative is not automatically defined as an ordinary function. The distinction is driven by the differential operator and the regularity actually available.

## Why a numerical method needs this distinction

When we approximate the problem with finite elements, we use basis functions that possess well-defined traces on the mesh boundary. To impose a Dirichlet condition, we may constrain boundary degrees of freedom or build an affine trial space. The discrete tests vanish on that boundary. To impose a Neumann condition, we usually leave those degrees of freedom available and integrate the flux data against boundary test functions.

An implementation can produce a plausible-looking numerical field even after confusing these choices. But it will solve a different variational problem. Boundary terms are not afterthoughts; they determine which solution the equation selects and whether a constant ambiguity remains.

The basic lesson is simple and exact. An energy solution is a function in a specified space, not necessarily a classical graph with meaningful values everywhere. The trace theorem converts the boundary from an informal drawing into a continuous mathematical operation. A lifting converts nonzero boundary data into a familiar zero-boundary variational problem. With those two tools, weak solutions can honor prescribed boundary values without pretending to have more smoothness than their existence proof supplied.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Endpoint trace estimate

For a smooth function on \((0,1)\),

\[
\int_0^1u(x)\,dx=u(0)+\int_0^1(1-t)u'(t)\,dt,
\qquad
|u(0)|\le \|u\|_{L^2}+\frac{1}{\sqrt3}\|u'\|_{L^2}.
\]

This extends continuously to \(H^1(0,1)\). There is no analogous \(L^2\)-only bound: if \(u_\varepsilon(x)=\max(1-x/\varepsilon,0)\), then \(u_\varepsilon(0)=1\), \(\|u_\varepsilon\|_2^2=\varepsilon/3\), and \(\|u_\varepsilon'\|_2^2=1/\varepsilon\).

### Traces, lifts, and the weak Dirichlet problem

For a bounded Lipschitz \(\Omega\), the bounded surjective trace \(\gamma:H^1(\Omega)\to H^{1/2}(\partial\Omega)\) has a bounded right inverse \(E\). Moreover, \(H_0^1(\Omega)=\ker\gamma\). For prescribed \(g\in H^{1/2}(\partial\Omega)\), set \(G=Eg\), \(u=G+w\), and solve

\[
\int_\Omega\nabla w\cdot\nabla v
=\langle f,v\rangle-\int_\Omega\nabla G\cdot\nabla v
\quad\forall v\in H_0^1(\Omega).
\]

Assuming the standard Poincaré inequality, Lax–Milgram gives unique \(w\), and a bound of the form \(\|u\|_{H^1}\le C(\|f\|_{H^{-1}}+\|g\|_{H^{1/2}})\). The constants depend on the domain. This uses the Laplacian; for elliptic diffusion coefficients replace the energy accordingly.

### Exact worked example

\[
-u''=2,\quad u(0)=1,\quad u(1)=2;
\quad G=1+x,\quad w=x(1-x),\quad u=1+2x-x^2.
\]

Check \(\int G'v'=v(1)-v(0)=0\) for \(v\in H_0^1(0,1)\).

### Exercises and answers

1. **A second endpoint estimate.** Prove \(|u(1)|\le \|u\|_2+\|u'\|_2/\sqrt3\). **Answer:** Average \(u(x)=u(1)-\int_x^1u'(t)dt\), then apply Cauchy–Schwarz.
2. **Different lift.** Take \(\widetilde G=1+x+x(1-x)\). Determine \(\widetilde w\). **Answer:** \(\widetilde w=0\) and the right-hand side of the weak equation vanishes because \(\widetilde G=u\).
3. **Trace versus pointwise evaluation.** Is a prescribed arbitrary \(g\in L^2(\partial\Omega)\) necessarily the trace of an \(H^1\) solution? **Answer:** No. The standard trace range is \(H^{1/2}(\partial\Omega)\), a proper subspace of \(L^2\) on ordinary boundaries.
4. **Space of variations.** Why is \(G+H_0^1\) affine rather than linear for nonzero \(g\)? **Answer:** It generally does not contain zero; differences of admissible states do belong to \(H_0^1\).

### Sources and further reading

- Long Chen, [*A Short Introduction to Sobolev Spaces*](https://www.math.uci.edu/~chenlong/226/Ch1Spaceshort.pdf), trace theorem, density, and bounded right inverse.
- Norwegian University of Science and Technology, [*Weak formulation of partial differential equations*](https://www.math.ntnu.no/emner/MA8502/2024h/lectures/html/chapter_01/weak_form_pdes.html), Dirichlet and Neumann spaces and weak boundary terms.
- [Wikipedia: Trace operator](https://en.wikipedia.org/wiki/Trace_operator), background and terminology; [Wikipedia: Sobolev space](https://en.wikipedia.org/wiki/Sobolev_space), definitions and weak derivatives.
- Companion within this library: `analysis:068000` presents the fractional trace and boundary regularity viewpoint at a more advanced level.
