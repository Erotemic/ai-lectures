# 021300 — Darboux and Moser: Why Symplectic Forms Are Locally Simple

**Track:** Topology and Geometry. **Background:** forms and pullbacks, Lie derivatives, flows, cohomology, the symplectic plane. **Central question:** how can a differential equation transform one symplectic form into another?

<!-- BEGIN SPOKEN LECTURE -->

# Darboux and Moser: Why Symplectic Forms Are Locally Simple

In Riemannian geometry, curvature can distinguish two spaces even when we inspect them through a microscope. A sphere has positive curvature, while a flat plane has zero curvature. Symplectic geometry behaves differently: every symplectic manifold has local coordinates in which its area form looks exactly like the standard one.

That is Darboux's theorem. Why should it be true, and why does it not imply that all symplectic manifolds are globally the same? The key idea is a method of moving differential forms by flowing points. It is often called Moser's method.

## Begin with two area forms

Picture a sphere with two ways to measure area. One form gives larger weight near the northern hemisphere; the other gives larger weight near the southern hemisphere. Suppose both forms are positive everywhere, and suppose their total areas are equal.

They do not agree point by point. But there is a diffeomorphism of the sphere that carries one area measurement to the other. The map redistributes area without tearing the surface. It need not preserve the latitude circles, and there is no reason for it to be unique.

Total area is an obvious necessary condition. A change of coordinates cannot alter the integral of a pulled-back top-degree form on a closed oriented manifold. Moser's argument shows that, on a compact connected oriented surface, equality of total area is also sufficient for positive area forms.

## Connect the forms by a path

Instead of trying to find the final coordinate change in one step, imagine a continuous movie of forms. At time zero, we see the first form. At time one, we see the second. In between, use a weighted average of the two.

On a surface, any positive weighted average of positive area forms remains positive. So every frame of the movie is still symplectic. In higher dimensions, a straight-line average of symplectic forms might become degenerate, and we cannot skip checking this condition.

Equality of total area on a sphere means the forms represent the same de Rham cohomology class. Their difference is the exterior derivative of a one-form. That one-form will be the input for a vector field designed to undo the change in area measurement.

## Find a moving coordinate system

We seek a family of diffeomorphisms that pulls each moving form back to the original one. What should its velocity be?

The rate of change of a pulled-back form contains two contributions. First the form itself is changing with time. Second the diffeomorphism is moving points through the form. The latter is described by the Lie derivative along the motion's vector field.

Cartan's formula expresses the Lie derivative of a closed form as the exterior derivative of its contraction with the vector field. This is the opening: the time derivative of our family of forms is also an exterior derivative. We can arrange for the two contributions to cancel by choosing the vector field whose contraction with the current symplectic form is minus the one-form measuring the difference.

Nondegeneracy guarantees a unique vector field satisfying that equation at each point. Smooth dependence on time makes it into a time-dependent flow. On a compact manifold the flow exists throughout the finite time interval. When we differentiate the pullback along this flow, its derivative is zero. The pulled-back symplectic form is therefore constant throughout the movie.

At the end we have the desired coordinate transformation.

## Darboux's theorem is a local application

For Darboux's theorem we do not start with two global area forms on one sphere. We stand near one point of an arbitrary symplectic manifold. Choose ordinary local coordinates and make a linear adjustment so that the given symplectic form agrees with the standard form at that point.

Now interpolate between the constant standard form and the actual varying form. Because they agree at the center, shrinking the coordinate neighborhood ensures that all intermediate forms remain nondegenerate. A local version of the same flow argument supplies new coordinates in which the symplectic form becomes exactly standard.

Every symplectic manifold of dimension two n therefore has local coordinates consisting of n position directions and n momentum directions, with the standard sum of position-momentum area pairings.

The local theorem does not state that all symplectic manifolds are diffeomorphic, nor that every symplectic form on a fixed manifold belongs to the same global cohomology class. The existence of one local coordinate system says almost nothing about how the systems must fit together over the whole manifold.

## Why global topology survives

Return to the sphere. Its area form cannot be the derivative of a globally defined one-form. If it were, Stokes' theorem would say its total area is zero, contradicting positivity. So a symplectic sphere cannot be globally equivalent to a region of the standard phase plane in a way that pulls back the standard exact symplectic form to its whole area form.

The same obstruction reappears in prequantization. Integrating a symplectic form over closed surfaces produces periods of a cohomology class. Those periods do not disappear under local coordinate changes.

Moser's method also has limitations. On a higher-dimensional manifold, cohomologous symplectic forms need not be linked by a path of symplectic forms. Without such a path the basic isotopy argument cannot even begin. Compactness or suitable control at infinity matters too, because the chosen vector field must have a flow for the intended time interval.

## A technique you will see again

This method is more general than a theorem about symplectic coordinates. It teaches a recurring strategy: express variation as an exact differential, find a vector field that cancels the variation, and integrate the vector field to transport structure.

Later we will study moduli spaces where choosing coordinates that follow a family of objects is not nearly so easy. Moser's calculation is a first example of how local infinitesimal solvability can, under explicit hypotheses, be turned into a global geometric equivalence. Keep the distinction clear: the local equations are flexible, while global topology and completeness impose the constraints.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(\omega_t\) be a smooth family of symplectic forms on a compact manifold with constant de Rham class. Suppose \(\dot\omega_t=d\sigma_t\). Solve \(\iota_{X_t}\omega_t=-\sigma_t\), and let \(\phi_t\) be the flow of \(X_t\), \(\phi_0=\operatorname{id}\). Then
\[
\frac{d}{dt}\phi_t^*\omega_t=\phi_t^*(\dot\omega_t+\mathcal L_{X_t}\omega_t)=\phi_t^*(d\sigma_t+d\iota_{X_t}\omega_t)=0,
\]
using \(d\omega_t=0\). Hence \(\phi_t^*\omega_t=\omega_0\). The assertion requires a path remaining symplectic and a flow defined for the full time interval.

On \(S^2\), positive area forms of equal total area are cohomologous; their convex interpolation remains positive. For Darboux, choose coordinates in which \(\omega(0)=\omega_0\), put \(\omega_t=(1-t)\omega_0+t\omega\), shrink the neighborhood until all \(\omega_t\) are symplectic, and apply a local relative version of the argument. In higher dimensions, cohomology equality alone does not imply equivalence of arbitrary symplectic forms.

### Exercises with answers

1. **Necessity.** Why do pulled-back area forms on a compact oriented surface have equal total area? **Answer:** change of variables for top-degree forms.
2. **Moser equation.** What vector field equation cancels \(\dot\omega_t=d\sigma_t\)? **Answer:** \(\iota_{X_t}\omega_t=-\sigma_t\).
3. **Global obstruction.** Why can a positive area form on \(S^2\) not be globally exact? **Answer:** Stokes would force its positive total area to vanish.
4. **Limitation.** Is every convex combination of symplectic forms in dimension four symplectic? **Answer:** no; nondegeneracy may fail in between.

### Sources and further reading

- Jürgen Moser, [On the Volume Elements on a Manifold](https://doi.org/10.1090/S0002-9947-1965-0182927-5), *Transactions of the AMS* 120 (1965), 286–294; source of the moving-volume-form method.
- Dusa McDuff and Dietmar Salamon, [Introduction to Symplectic Topology](https://global.oup.com/academic/product/introduction-to-symplectic-topology-9780198794905), Darboux and Moser arguments.
- [Darboux's theorem](https://en.wikipedia.org/wiki/Darboux%27s_theorem_(symplectic_geometry)); [Moser's theorem](https://en.wikipedia.org/wiki/Moser%27s_trick).
