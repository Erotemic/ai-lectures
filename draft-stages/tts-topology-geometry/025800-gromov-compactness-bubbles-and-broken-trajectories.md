# 025800 — Compactness for Holomorphic Curves: Bubbles, Breaking, and Escape

**Track:** Topology and Geometry. **Background:** J-holomorphic area–energy, elliptic estimates, Floer cylinders, topology of spheres and disks. **Central question:** what can a bounded-energy sequence of holomorphic curves do instead of converging smoothly?

<!-- BEGIN SPOKEN LECTURE -->

# Compactness for Holomorphic Curves: Bubbles, Breaking, and Escape

We now know how to write the Floer equation, how to calculate the energy of a solution, and how to predict the dimension of its moduli space. None of that, by itself, means we can count solutions.

Imagine that we have infinitely many distinct cylinders, each with energy at most a fixed constant. If they fail to converge to an ordinary cylinder, where can they go? The answer organizes one of the central subjects of symplectic analysis: compactness up to carefully classified degenerations.

## Bounded total energy is not a pointwise derivative bound

A function can have a derivative that grows very large inside a region whose area becomes very small, while the integral of the squared derivative remains bounded. A total-energy bound sees the amount of variation but may not see where the variation is becoming concentrated.

For holomorphic maps, the elliptic equation prevents completely arbitrary concentration. Small-energy regularity gives control when sufficiently little energy is present in a small neighborhood. Thus a sequence with uniformly bounded total energy can have only finitely many separate regions containing a fixed positive amount of concentrated energy, provided the relevant energy quantization and geometry hypotheses hold.

Away from those regions, elliptic estimates can often upgrade weak convergence to smooth convergence. Near a concentration point we zoom in instead.

## A sphere map shrinking to a point

Take the Riemann sphere and the degree-one holomorphic maps that send z to z divided by a small positive number epsilon. Each is an automorphism of the sphere and has normalized symplectic energy one.

As epsilon tends to zero, at every fixed point other than z equals zero, the image tends toward the point at infinity. The maps appear to become constant across almost the whole sphere. But the total energy remains one. Where did it go?

Look near z equals zero using the new coordinate w equal to z divided by epsilon. In that magnified view, the map is simply w itself. A nonconstant holomorphic sphere reappears. The sequence did not lose energy; it concentrated it at a vanishing scale.

This is a simple model of sphere bubbling. The limiting object can consist of a main curve and one or more holomorphic sphere components attached at nodes. A correct compactification records that extra geometry.

## Breaking is a different degeneration

Floer cylinders have a long s direction. Even without any pointwise blow-up, a sequence of cylinders can develop a very long middle region that is almost a periodic orbit. After shifting each end separately along s, we may see one cylinder from orbit x to orbit y and another from y to orbit z.

The sequence has converged to a broken trajectory: a two-stage chain of cylinders. Each stage has finite energy, and the total action drop is the sum of the drops through the intermediate orbit.

Breaking is the Floer analogue of broken gradient trajectories in finite-dimensional Morse theory. Sphere bubbling is an additional phenomenon caused by the two-dimensional map equation. They must not be conflated.

## Disks can bubble from Lagrangian boundaries

For a strip with its lower edge on one Lagrangian and its upper edge on another, concentration may occur near a boundary point. Rescaling can produce a holomorphic disk whose boundary lies on one Lagrangian.

The disk may change the algebraic boundary of moduli spaces. It is one reason the most general Lagrangian Floer theory cannot be reduced to simply counting strips and declaring the differential squared zero.

Exactness gives a transparent way to eliminate this particular degeneration in a useful model. If the symplectic form is exact and each relevant Lagrangian is exact, a holomorphic disk with boundary on one Lagrangian has zero area by Stokes' theorem. The area–energy identity then forces it to be constant.

Likewise, a symplectically aspherical target has no nonconstant holomorphic spheres. These two conditions remove two major classes of bubbles, though they do not remove breaking.

## The problem of noncompact targets

A cotangent bundle is generally noncompact. Even if we have ruled out all nonconstant sphere and disk bubbles, a sequence of maps might run farther and farther out along momentum directions. Its image might leave every compact set.

Therefore exactness alone is not a global compactness theorem. A Floer theory on a noncompact target needs additional control at infinity: an appropriate Hamiltonian growth condition, geometry that supports a maximum principle, or another valid confinement argument.

On a closed symplectic manifold the image cannot escape the target, but sphere bubbling may remain. One has traded one compactness problem for another. Choosing the right hypotheses depends on the situation being studied.

## The meaning of Gromov compactness

Gromov compactness does not usually mean that every bounded-energy sequence has a smooth limit on the original fixed domain. It says that under precise assumptions, after passing to a subsequence and allowing reparameterizations and controlled degenerations, the sequence converges to a richer object such as a stable holomorphic map with bubble components.

For Floer trajectories, the suitable compactification may also contain broken cylinders. In favorable aspherical situations, for the lowest-dimensional moduli spaces, breaking is the only boundary phenomenon that survives.

This is exactly the situation we need for the Floer differential. A one-dimensional moduli space of unbroken cylinders, after dividing by translation, should compactify to something like a collection of closed intervals and circles. The endpoints of the intervals are broken pairs of rigid trajectories.

If a sphere or disk bubble can also appear as a boundary point, that simple algebraic picture may fail. If the curves can escape to infinity, there may be no finite boundary count at all. Thus the compactness hypotheses are part of the definition's correctness, not technical footnotes.

## Why this is stronger than a vague convergence statement

When you read an advanced theorem, ask four separate questions. Is total energy bounded? Can local derivatives become unbounded? Can a solution break along the cylinder? Can the target or domain geometry escape the compact region under consideration?

Different hypotheses answer different questions. Symplectic asphericity removes nonconstant sphere bubbles. Exact Lagrangians remove nonconstant boundary disks in the exact setting. Nondegenerate asymptotics and finite-energy analysis identify the ends of broken cylinders. Proper confinement or compactness of the target prevents escape.

Once these mechanisms are separated, the later proof that a differential squares to zero becomes intelligible. It is an assertion about the entire boundary of a compactified one-dimensional moduli space, not merely a symbolic cancellation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A concrete bubble sequence on \(\mathbb{CP}^1\) is \(u_\epsilon(z)=z/\epsilon\), \(\epsilon\downarrow0\), extended by \(\infty\mapsto\infty\). With \(\int_{\mathbb{CP}^1}\omega_{FS}=1\), \(E(u_\epsilon)=1\) for every \(\epsilon\), but \(u_\epsilon\to\infty\) locally smoothly on \(\mathbb{CP}^1\setminus\{0\}\). Under rescaling \(z=\epsilon w\), \(u_\epsilon(\epsilon w)=w\), revealing a degree-one bubble. Domain reparameterization and stable-map convergence provide the correct compactification.

For Floer trajectories \(u_k\), a broken limit may contain \(u^1:x_-\to y\) and \(u^2:y\to x_+\), with \(E(u^1)+E(u^2)=\mathcal A(x_-)-\mathcal A(x_+)\). On a closed symplectically aspherical target, nonconstant holomorphic sphere bubbles are impossible; for exact \((M,\omega=d\lambda)\) with exact Lagrangians \(\lambda|_{L_i}=df_i\), nonconstant disk bubbles on one \(L_i\) are impossible. Both conclusions use the energy–area identity. Additional regularity and nonescape hypotheses are still necessary for compactness.

### Exercises with answers

1. **Bubble.** What is the energy of every map \(z\mapsto z/\epsilon\) on the normalized Riemann sphere? **Answer:** one, since it has degree one.
2. **Breaking.** If a Floer cylinder breaks through an intermediate orbit \(y\), how do the action drops combine? **Answer:** additively: \(A(x_-)-A(y)+A(y)-A(x_+)=A(x_-)-A(x_+)\).
3. **Disk.** Which hypothesis rules out nonconstant boundary bubbles by Stokes in the model? **Answer:** exact symplectic form and exact boundary Lagrangians.
4. **Escape.** Can noncompact cotangent-bundle targets have escape to infinity even when sphere and disk bubbles are excluded? **Answer:** yes, without extra confinement estimates.

### Sources and further reading

- Mikhail Gromov, [Pseudo-holomorphic Curves in Symplectic Manifolds](https://doi.org/10.1007/BF01388806), original holomorphic-curve compactness framework.
- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), bubble-tree and stable-map compactness proofs.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), energy quantization and compactness.
- [Gromov compactness theorem](https://en.wikipedia.org/wiki/Gromov%27s_compactness_theorem_%28topology%29).
