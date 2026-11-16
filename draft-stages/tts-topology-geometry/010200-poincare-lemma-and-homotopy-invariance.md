# 010200 - Poincare Lemma and Homotopy Invariance

**Track:** Topology and Geometry. **Background:** differential forms, exterior derivative, Stokes' theorem, homotopy. **Question:** why does closed imply exact locally, and what survives continuous deformation?

<!-- BEGIN SPOKEN LECTURE -->

# Poincare Lemma and Homotopy Invariance

A differential form can be closed without being exact. We have seen this on the punctured plane: the form measuring angle around the missing origin has zero exterior derivative, but its integral around a full loop is two pi. Yet if we zoom in to a small disk that avoids the origin, we can choose an angle function there, and the same form becomes its differential. The form is locally exact but globally not exact.

The Poincare lemma explains this local behavior in every degree. On a star-shaped open region in Euclidean space, every closed differential form of positive degree is exact. That statement is the analytic starting point for understanding why de Rham cohomology detects global topology rather than local failures of calculus.

## What star-shaped buys us

A region is star-shaped with respect to a chosen center if every straight segment connecting that center to a point in the region stays inside the region. An open ball is star-shaped, and so is any convex open set. A ring with a hole is not star-shaped with respect to any point, because some straight lines to the center would cross the missing region.

The geometry of a star-shaped region offers a simple deformation. Keep the center fixed, and move every point straight toward it. At time one we have the identity map; at time zero everything has collapsed to the center. This is a homotopy: a smoothly varying family of maps. Its existence gives us a method for constructing antiderivatives of forms.

## Recovering a potential by integrating along rays

First consider a closed one-form on a star-shaped plane region. Write it as P d x plus Q d y. Closed means the x derivative of Q equals the y derivative of P. Choose the star center as the origin for simplicity. Define a candidate potential at a point by integrating the one-form along the straight path from the origin to that point.

Why should this work? Differentiate the path integral with respect to the endpoint. The derivative consists of the local value of the form plus a correction measuring how the form changes along the ray. The equality of the mixed partial derivatives makes that correction collapse into the appropriate endpoint expression. The resulting differential of the potential is the original form.

For a familiar example, let the form be y d x plus x d y. The mixed-derivative condition holds: both relevant derivatives equal one. Integrating along the ray from zero to the point x,y gives x times y. Differentiate the function x y, and we indeed recover y d x plus x d y.

This local primitive is not unique. Adding a constant does not change its differential. On a connected region any two primitives of the same one-form differ by a constant. The star center and chosen integration paths give a construction, not a uniquely distinguished potential.

## The higher-degree problem

For a two-form, an antiderivative is a one-form; for a three-form, it is a two-form. Simply integrating one scalar along a path no longer captures all the alternating inputs. The general construction is a homotopy operator. It contracts the form with the radial direction and integrates that contraction as the point moves along its ray.

The crucial identity says that applying the exterior derivative after the homotopy operator, then adding the homotopy operator after the exterior derivative, equals the identity on positive-degree forms on a star-shaped region. More accurately, in every degree the difference between the identity map and pullback by the collapse to the center appears on the right. The collapse pulls positive-degree forms back to zero, so in those degrees the right side is simply the original form.

Now take a closed form omega. Its exterior derivative is zero. The identity becomes: omega equals the exterior derivative of the homotopy operator applied to omega. That is the antiderivative we wanted. This is the Poincare lemma, with an explicit construction behind the existence claim.

There is a special case in degree zero. A closed zero-form is a function whose differential is zero, hence is locally constant. On a connected star-shaped domain it is constant. It is not sensible to say that every constant function is the differential of a minus-one-form. The positive-degree qualification matters.

## From star-shaped regions to manifolds

A smooth manifold has coordinate neighborhoods diffeomorphic to open balls. Such neighborhoods allow the Poincare lemma to be transported through the chart. Therefore every closed smooth positive-degree form on a manifold is locally exact. Local exactness is the default. The interesting question is whether those local primitives can be reconciled to obtain a global primitive.

On the circle, the angular one-form has a local potential in every sufficiently small arc. But if we travel around the entire circle, a chosen angle increases by a full turn. No single-valued real function on the circle can serve as a global potential. The obstruction is a global mismatch among local choices, detected by integrating around the loop.

## Homotopy invariance

The radial collapse used in the proof suggests a larger principle. Suppose two smooth maps from M to N are smoothly homotopic. Pulling a closed form on N back along either map produces forms on M that differ by an exact form. Consequently, the two maps induce the same operation on de Rham cohomology. We say de Rham cohomology is homotopy invariant.

To see the mechanism, imagine the homotopy sweeping out a cylinder M times an interval. Pull the form to the cylinder, contract it with the direction of the interval, and integrate along that direction. This produces an operator whose exterior derivative compares the forms at the two ends of the homotopy. Once again the boundary of a deformation supplies the difference between endpoint data.

If two manifolds are homotopy equivalent, their de Rham cohomology groups are isomorphic. A disk is homotopy equivalent to a point, so its positive-degree de Rham cohomology vanishes. The punctured plane retracts onto a circle; its first cohomology is therefore the same as that of the circle, which is nonzero. These topological facts explain the two potential calculations above.

## What homotopy does not preserve

Homotopy invariance is a statement about cohomology, not a claim that every geometric property survives deformation. A circle and an annulus can have the same homotopy type while having different dimensions as manifolds. A Riemannian metric, curvature, area, and geodesic lengths require extra structure and are not determined by homotopy type.

Similarly, a global integral of a nonclosed form need not be invariant under deforming the integration cycle. The proof of invariance for closed forms uses the vanishing of the exterior derivative. The hypothesis is doing real work.

The Poincare lemma and homotopy invariance make a useful pair. The first says closed forms have local potentials on sufficiently simple regions. The second says the global obstruction to finding a potential is unchanged by suitable deformation of the underlying space. Local calculus gives us derivatives; global topology determines what those derivatives cannot resolve.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(U\subset\mathbb R^n\) be star-shaped about the origin. For \(\omega\in\Omega^k(U)\), \(k\ge1\), define
\[(K\omega)_x(v_1,\ldots,v_{k-1})=\int_0^1t^{k-1}\omega_{tx}(x,v_1,\ldots,v_{k-1})\,dt.\]
Then \(dK+Kd=\mathrm{id}-c_0^*\), where \(c_0(x)=0\); \(c_0^*\omega=0\) for \(k>0\). Thus \(d\omega=0\) implies \(\omega=d(K\omega)\). In degree zero, \(df=0\) implies \(f\) is constant on a connected domain.

For a smooth homotopy \(H:M\times[0,1]\to N\) between \(f_0,f_1\), the homotopy formula is
\[f_1^*-f_0^*=dK_H+K_Hd\]
on forms (with \(K_H\) of degree \(-1\)). Hence \([f_1^*\omega]=[f_0^*\omega]\) when \(d\omega=0\).

### Check your understanding

1. On \(\mathbb R^2\), find a primitive of \(y\,dx+x\,dy\). **Answer:** \(xy\).
2. Is a closed zero-form necessarily exact? **No:** the usual de Rham complex starts at degree zero, and closed zero-forms are locally constant.
3. Why is a small disk avoiding the origin different from the entire punctured plane? **Answer:** the disk contracts through points inside itself, while the punctured plane retains a noncontractible loop.

### Reading and sources

- MIT OCW, [Geometry of Manifolds, lecture on Poincare Lemma and homotopy invariance](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Poincare lemma](https://en.wikipedia.org/wiki/Poincar%C3%A9_lemma), [De Rham cohomology](https://en.wikipedia.org/wiki/De_Rham_cohomology).
