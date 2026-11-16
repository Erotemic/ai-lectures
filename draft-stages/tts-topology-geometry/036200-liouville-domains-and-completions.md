# 036200 — Liouville Domains and Completions: Turning a Boundary into Infinity

**Track:** Topology and Geometry. **Background:** symplectic two-forms, exterior derivatives, contact forms and vector fields. **Question:** how can a compact symplectic region be enlarged while retaining geometric control near infinity?

<!-- BEGIN SPOKEN LECTURE -->

# Liouville Domains and Completions: Turning a Boundary into Infinity

A compact symplectic region has a boundary. Many Floer-theoretic problems, however, need a noncompact space on which Hamiltonian trajectories may travel farther and farther out. A Liouville completion provides a controlled way to attach an infinite cylindrical end. The crucial point is that the added infinity has a simple formula rather than arbitrary geometry.

## An exact symplectic form has a primitive

A symplectic form omega is a closed, nondegenerate two-form. If it can be written globally as the exterior derivative of a one-form lambda, we call the symplectic manifold exact. The one-form lambda is a primitive of omega. Exactness is a global property; a symplectic form always has local primitives on sufficiently simple coordinate neighborhoods, but may lack a global primitive.

For a cotangent bundle, the geometry supplies a preferred primitive. In the position-momentum coordinates used in our track, omega is d q wedge d p and lambda is minus p d q. Differentiating lambda gives d q wedge d p. Different texts often choose the opposite convention for omega and lambda. We retain this pair so the Hamiltonian convention and action formula remain consistent with the earlier lectures.

A vector field Z is called Liouville if inserting it into omega gives lambda. By the Cartan formula, the flow of Z expands omega: its Lie derivative along Z equals omega. Thus Liouville flow rescales the symplectic structure rather than preserving it. In cotangent coordinates, Z points radially outward in the momentum directions.

## A Liouville domain

A Liouville domain is a compact manifold with boundary, equipped with a one-form lambda such that omega equals d lambda is symplectic and its Liouville vector field points strictly outward along the boundary. Outward transversality is the condition that lets us regard the boundary as the entrance to a radial end.

Restrict lambda to the boundary and call the resulting one-form alpha. This is a contact form. To understand why, notice that the Liouville vector field is transverse to the boundary. Contracting the nonvanishing top symplectic volume form with that outward direction gives a nonvanishing volume form on the boundary. Up to a positive scale, the resulting expression is alpha wedged with the appropriate number of copies of d alpha. That is precisely the contact condition.

In other words, a boundary of contact type carries a contact structure because the ambient exact symplectic geometry supplies a preferred normal scaling direction and a nondegenerate area form on the remaining tangent hyperplanes.

## The collar formula

Follow the Liouville vector field outward from the boundary. Introduce a radial coordinate r which equals one on the original boundary and grows along this flow. The primitive on the collar has the form r times alpha. Taking its exterior derivative produces two terms: d r wedge alpha and r times d alpha. This simple formula is the basis of the completion.

Attach a half-infinite end consisting of boundary points and radial values greater than or equal to one. Keep lambda equal to r alpha and omega equal to its exterior derivative there. The resulting noncompact exact symplectic manifold is the completion of the Liouville domain. Its infinity is not featureless. Each large-radius slice carries a scaled copy of the same contact structure, and the Reeb dynamics on the boundary remain visible.

This is why Liouville completions are natural for wrapped Floer theory. A Hamiltonian that grows with r acquires a predictable vector field along the Reeb direction. We can relate new periodic Hamiltonian trajectories and Lagrangian chords to Reeb orbits and chords on the original contact boundary.

## The cotangent disk as a model

Let Q be a closed smooth manifold with a Riemannian metric. Its cotangent bundle consists of all covectors attached to points of Q. Use the metric to define the norm of a covector. The disk cotangent bundle is the part where that norm is at most one. Its boundary is the unit cotangent bundle. With the canonical primitive and symplectic form, this disk bundle is a Liouville domain: radial scaling of covectors points outward at norm one.

Its completion is the full cotangent bundle. Every covector of length greater than one lies on the attached radial end. This correspondence explains why wrapped Floer homology of a cotangent fiber can recover information about paths or loops in Q. The relevant Hamiltonian motion is able to explore large momenta, but the geometry there is organized by the contact dynamics of unit covectors.

For the circle Q, the unit cotangent boundary has two components, corresponding to positive and negative momentum. The Reeb directions on these components point in opposite coordinate directions under our sign convention. The completed cotangent cylinder contains all momentum values, so trajectories can wind in either direction around the base circle. Both windings matter in the based-loop calculation.

## Exactness controls energy, not everything

Exactness has a powerful analytic consequence. If a closed surface is mapped into an exact symplectic manifold, the integral of the pulled-back symplectic form is zero by Stokes' theorem. A nonconstant compatible holomorphic sphere would have positive area, so it cannot exist in an exact symplectic manifold. This removes one important source of sphere bubbling in Floer compactness arguments.

But exactness by itself does not prevent trajectories from escaping to infinity. The completed manifold is noncompact. To control solutions of the Floer equation, one also needs appropriate Hamiltonians, almost-complex structures, and boundary or asymptotic conditions. A maximum principle or no-escape lemma supplies this additional control in settings where its hypotheses hold.

The distinction is worth preserving. Exactness gives algebraic control of symplectic area and suppresses certain bubbles. Cylindrical geometry gives a structured end. Analytic estimates then show which trajectories stay in a compact region. Wrapped Floer theory depends on all three pieces, not on any one of them in isolation.

A Liouville completion is therefore more than a convenient way to remove the boundary from a picture. It turns contact dynamics at a finite boundary into symplectic dynamics at a controlled infinity, while retaining a primitive that makes action and energy estimates possible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

An exact symplectic manifold has \(\omega=d\lambda\). Its Liouville vector field \(Z\) satisfies \(\iota_Z\omega=\lambda\), so \(\mathcal L_Z\omega=d\iota_Z\omega=d\lambda=\omega\). A Liouville domain \((W,\lambda)\) has compact boundary and outward-transverse \(Z\); \(\alpha=\lambda|_{\partial W}\) is contact. On its completion \(\widehat W=W\cup_{\partial W}([1,\infty)\times\partial W)\),
\[
\lambda=r\alpha,\qquad \omega=d(r\alpha)=dr\wedge\alpha+r\,d\alpha,\qquad Z=r\partial_r.
\]
For \(T^*Q\) with local coordinates \((q,p)\), fix \(\lambda=-\sum_i p_i\,dq_i\), \(\omega=d\lambda=\sum_i dq_i\wedge dp_i\); then \(Z=\sum_i p_i\partial_{p_i}\). With a Riemannian metric, the unit disk cotangent bundle is a Liouville domain. For a \(J\)-holomorphic sphere \(u:S^2\to\widehat W\) compatible with \(\omega=d\lambda\), \(E(u)=\int_{S^2}u^*\omega=\int_{S^2}d(u^*\lambda)=0\), hence u is constant.

### Exercises with answers

1. Differentiate \(r\alpha\) on a cylindrical end. **Answer:** \(dr\wedge\alpha+r\,d\alpha\).
2. What is the Liouville field of \(-p\,dq\) on the cotangent plane with \(dq\wedge dp\)? **Answer:** \(p\partial_p\).
3. Why is a nonconstant compatible holomorphic sphere impossible in an exact symplectic manifold? **Answer:** its positive energy would equal an exact symplectic area integral, which vanishes by Stokes.
4. Does exactness alone prevent a noncompact Floer trajectory from escaping? **Answer:** no; geometric and analytic end controls are still needed.

### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), symplectic fillings, contact-type boundaries and exactness.
- Denis Auroux, [A Beginner's Introduction to Fukaya Categories](https://arxiv.org/abs/1301.7056), exact symplectic geometry and Fukaya-theoretic context.
- [Symplectic manifold](https://en.wikipedia.org/wiki/Symplectic_manifold); [Cotangent bundle](https://en.wikipedia.org/wiki/Cotangent_bundle).
