# 025900 — Why Floer Boundaries Cancel: Moduli Spaces and Differential Squared

**Track:** Topology and Geometry. **Background:** Morse chain complexes, Fredholm index, regular Floer cylinders, compactness and broken trajectories. **Central question:** exactly which analytic facts make the algebraic Floer boundary square to zero?

<!-- BEGIN SPOKEN LECTURE -->

# Why Floer Boundaries Cancel: Moduli Spaces and Differential Squared

We have finally assembled the objects needed for a Floer chain complex. There are periodic Hamiltonian orbits, the critical points of action. There are Floer cylinders connecting those orbits, obtained from negative gradient flow. There is a Fredholm index predicting the dimensions of solution families. And there are compactness results describing how such families can degenerate.

Now comes the algebraic claim: applying the Floer boundary operator twice gives zero. The proof is geometric, and every analytic hypothesis has a role.

## Begin with a finite-dimensional rehearsal

Imagine a hill landscape with several critical points. In Morse homology, the boundary of an index-two critical point counts downward gradient trajectories to index-one critical points. Each trajectory is considered up to translating the time at which we start watching it.

To compute the boundary twice, we count two-step paths: from an index-two point to an index-one point, then from that point to an index-zero point.

Why do these counts cancel? Because the two-step configurations are endpoints of one-dimensional families of unbroken trajectories between the original endpoints. A compact one-dimensional manifold is a collection of circles and closed intervals. Every interval has two endpoints, and every circle has none. Modulo two, the total number of boundary points is therefore zero.

The same structure drives Floer homology. But the phrase 'one-dimensional manifold' now refers to a space of solutions of an elliptic PDE, not a family of ordinary integral curves.

## Generators and rigid cylinders

Choose a closed symplectic manifold with no nonconstant holomorphic spheres, and a Hamiltonian whose one-periodic orbits in the chosen class are nondegenerate. Choose suitable almost-complex data so the relevant cylinder moduli spaces are regular.

Build a vector space over the field with two elements, one basis generator for each orbit. For now, work modulo two so we do not need to construct coherent orientations.

Between two orbits x and y, consider the set of Floer cylinders from x to y. Divide nonconstant solutions by translation along the length of the cylinder. If the relative index is one, the expected dimension after this quotient is zero. Under the needed compactness, there are finitely many such rigid cylinders.

Define the boundary of x by summing, for each y of index one lower, the number of rigid cylinders from x to y, reduced modulo two, times the generator y.

We have defined an actual linear operator, not just a metaphor. Its input is one orbit, and its output is a finite combination of other orbits.

## Expand the boundary twice

Apply the boundary once to x. Each term is an intermediate orbit y weighted by the count of rigid cylinders from x to y. Apply the boundary again. A term involving a final orbit z counts pairs of rigid cylinders: the first from x to y, the second from y to z, summed over all y.

So the coefficient of z in the boundary squared is a count of broken two-stage trajectories.

How can we see that it is zero? Look at unbroken cylinders from x to z whose relative index is two. After translation is removed, their expected dimension is one. Under regularity, this is locally a smooth one-dimensional moduli space.

The compactness theorem says that a sequence in this space can converge either to another unbroken cylinder or to a broken pair of rigid cylinders, provided bubbling and escape have been ruled out in the relevant dimension.

## Compactification and gluing must agree

Compactness alone is not enough. It tells us what limits can occur, but it does not automatically say that every broken pair is the endpoint of precisely the right local family of unbroken solutions.

A gluing theorem supplies the missing direction. Start with two rigid cylinders that meet at the same intermediate orbit. Cut off their distant ends, insert a long neck, and solve away the small error produced by the approximate joining. Under suitable transversality and uniform inverse estimates, one obtains a nearby genuine cylinder. As the neck becomes longer, it approaches the broken pair.

Thus the compactified one-dimensional moduli space has boundary points exactly corresponding to the two-stage configurations counted in the boundary squared. The total number of endpoints of this compact one-manifold is even. Therefore every coefficient in the boundary squared vanishes over the field with two elements.

With integer coefficients, orientations assign signs to boundary points, and the signed sum is zero. That requires coherent orientation data; it is not obtained by merely replacing the number two with the integers.

## A circle calculation to keep the picture concrete

Take a cosine function on a circle. It has one maximum and one minimum. For an appropriate metric, there are two gradient trajectories descending from the maximum to the minimum, one along each arc of the circle.

Over the field with two elements, those two trajectories cancel. The Morse differential is zero. The chain groups have one generator in degree one and one in degree zero, giving the homology of a circle.

For a small graph of the derivative of cosine in the cotangent bundle of a circle, the Lagrangian intersection picture has the same two generators. Under a suitable small-graph correspondence, rigid Floer strips reproduce the Morse trajectories. That makes the cancellation visible in a genuine geometric example, not only in the abstract moduli-space proof.

## Where the proof can fail

If we count strips with boundaries on nonexact Lagrangians, holomorphic disks can bubble off. Such bubbles may contribute additional ends to what we hoped was a one-dimensional moduli space. Then the naive count of broken pairs need not be the complete boundary count.

Likewise, sphere bubbles may matter in a general closed target, and loss of control at infinity matters in noncompact targets. Multiple covers and failed transversality may prevent the moduli space from being an ordinary smooth manifold of the expected dimension.

The general theory has sophisticated ways to address these issues: monotonicity hypotheses, Novikov coefficients, coherent perturbations, virtual cycles, and higher algebraic corrections. We do not need to implement all of those systems to understand the foundational proof. We do need to know why the simpler proof is valid only after its assumptions are checked.

## What the new homology can say

Because the boundary squared is zero, we can take the kernel of the boundary modulo its image, just as for any chain complex. Under suitable continuation arguments, changing the Hamiltonian or almost-complex structure does not change the resulting Floer homology.

When this invariant agrees with ordinary homology in a small-Hamiltonian model, it can give a lower bound on the number of periodic orbits for more complicated Hamiltonians. That is how topology can force dynamics.

The foundational result of this lecture is therefore not merely an equation. It is a chain of implications: regularity gives a one-dimensional moduli space; compactness classifies its degenerations; gluing identifies its boundary; and the elementary fact that boundaries of one-manifolds cancel gives the algebraic identity.

This is what it means to build homology from solutions of a partial differential equation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

In a closed symplectically aspherical setting \(\omega|_{\pi_2(M)}=0\), \(c_1(TM)|_{\pi_2(M)}=0\), for nondegenerate orbits \(x,y\), assume standard Floer regularity and compactness. The unparameterized moduli space \(\mathcal M(x,y)/\mathbb R\) of nonconstant cylinders has expected real dimension \(\mu(x)-\mu(y)-1\) for the compatible grading and index convention. Define over \(\mathbb F_2\)
\[
\partial x=\sum_{\mu(x)-\mu(y)=1}\#_2(\mathcal M(x,y)/\mathbb R)\,y.
\]
The compactification of a one-dimensional quotient moduli space \(\mu(x)-\mu(z)=2\) has boundary strata \(\coprod_y(\mathcal M(x,y)/\mathbb R)\times(\mathcal M(y,z)/\mathbb R)\) with each relative index one. Under compactness, no bubbling or escape, and gluing, this is the entire boundary, so \(\partial^2=0\) by even boundary count. Integral coefficients require coherent orientations. If Lagrangian disk bubbling contributes to codimension-one strata, naive \(\partial^2=0\) may fail, motivating obstruction and \(A_\infty\)-structures.

For \(f(q)=\cos(2\pi q)\) on \(S^1\), there are two descending gradient arcs from the maximum to the minimum. Their count vanishes in \(\mathbb F_2\), giving the ordinary circle Morse complex \(C_1=C_0=\mathbb F_2\), \(\partial=0\). This is not yet a proof of the general Hamiltonian Floer comparison, only its finite-dimensional model.

### Exercises with answers

1. **Rigid dimension.** What relative index gives zero-dimensional unparameterized regular Floer cylinders? **Answer:** one.
2. **Square.** Which configurations appear in a coefficient of \(\partial^2 x\)? **Answer:** pairs of rigid cylinders through an intermediate orbit.
3. **Boundary count.** Why does a compact one-manifold have even total boundary cardinality? **Answer:** each interval contributes two endpoints and each circle contributes none.
4. **Caveat.** Name one degeneration that invalidates the simple broken-only boundary description. **Answer:** nonconstant holomorphic sphere bubbling or boundary disk bubbling, depending on the setup.

### Sources and further reading

- Andreas Floer, [Morse Theory for Lagrangian Intersections](https://doi.org/10.4310/JDG/1214442477), original chain-count construction.
- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), gluing, compactness, and invariance.
- Michael Hutchings, [Floer Theory course notes](https://math.berkeley.edu/~hutching/teach/277-2008/index.html), Morse-to-Floer progression.
- [Floer homology](https://en.wikipedia.org/wiki/Floer_homology).
