# 031200 — Continuation Maps: Why Floer Homology Survives Changing the Hamiltonian

**Track:** Topology and Geometry. **Background:** Floer equation, energy identity, chain homotopy, compactness, Morse homology. **Central question:** why does a chain complex built from one Hamiltonian still give information about a different Hamiltonian?

<!-- BEGIN SPOKEN LECTURE -->

# Continuation Maps: Why Floer Homology Survives Changing the Hamiltonian

If we build Floer homology by counting periodic orbits and cylinders for a particular Hamiltonian, the answer might seem tied to that choice. Change the Hamiltonian and the periodic trajectories change. Some are born, some disappear, and their actions shift.

Yet under suitable hypotheses, the resulting Floer homology is invariant. This is what allows a calculation with a very small, almost trivial Hamiltonian to constrain a complicated Hamiltonian system.

The mathematical device is a continuation map. Instead of studying a single fixed Hamiltonian along an entire cylinder, we let the Hamiltonian gradually change as we move down the cylinder.

## Interpolate between two Hamiltonians

Choose an incoming Hamiltonian H minus and an outgoing Hamiltonian H plus. Along the s direction of a cylinder, use a smooth family that equals the incoming Hamiltonian far to the left and the outgoing one far to the right.

At each location along the cylinder, impose the Floer equation using that local Hamiltonian and a compatible almost-complex structure that may vary as well. Solutions should approach periodic orbits of the incoming system on one end and orbits of the outgoing system on the other.

Such solutions are called continuation trajectories. Counting the appropriate rigid solutions defines a linear map from the chain complex for the first Hamiltonian to the chain complex for the second.

Why should this map respect the differentials? Consider one-dimensional families of continuation trajectories. Their compactified boundaries include an ordinary Floer cylinder attached before the continuation region, or an ordinary Floer cylinder attached after it. Counting those two kinds of ends gives exactly the equation saying that continuation is a chain map.

## What happens to the energy identity?

The Hamiltonian now depends on s, so the action function itself changes as we move along the cylinder. The derivative of action has two pieces: the negative squared norm of the Floer gradient, and an additional term coming from the explicit s derivative of the Hamiltonian.

After integration, the energy is the incoming action minus the outgoing action, minus the integral of the s derivative of the interpolating Hamiltonian evaluated along the trajectory, under our sign convention.

This correction is important. We cannot blindly reuse the unchanging-Hamiltonian energy identity. But if the interpolation is controlled and the target is compact, the correction can be bounded. That restores the energy estimates needed for compactness of the continuation moduli spaces.

## Chain maps versus isomorphisms

Construct a continuation map from H minus to H plus, then another map going back. Are the composites equal to the identity on the nose? Usually not at chain level. Instead, under suitable continuation and compactness arguments, they are chain homotopic to the identity.

A chain homotopy is an explicit algebraic witness that two chain maps induce the same map on homology. A two-parameter family of continuation data provides geometric moduli spaces whose boundaries encode such a homotopy.

Consequently, the two continuation maps induce inverse isomorphisms on Floer homology. The chain generators can change substantially, but the homology remains the same.

This is the same logical pattern as in ordinary Morse theory. Different Morse functions and metrics produce different chain complexes, but continuation maps show that the homology does not depend on those auxiliary choices.

## Calculate a small example on the torus

The two-torus has one unit of ordinary homology in degree zero, two in degree one, and one in degree two, over a field. Its total Betti number is four.

Choose a very small generic autonomous Hamiltonian related to a Morse function with exactly four critical points: a minimum, two saddles, and a maximum. With the right smallness and nondegeneracy conditions, the contractible one-periodic Hamiltonian orbits correspond to those critical points, and its Floer complex identifies with a Morse-type complex up to grading convention.

The resulting Floer homology has total rank four. Now replace that small Hamiltonian by an arbitrary generic time-dependent Hamiltonian on the torus, still considering its contractible one-periodic orbits. Continuation invariance says the homology rank is still four.

The chain complex of the new Hamiltonian needs at least four generators to have homology of total rank four. Therefore the new Hamiltonian has at least four contractible one-periodic trajectories if they are nondegenerate.

These trajectories correspond to fixed points of its time-one Hamiltonian diffeomorphism. We have obtained a concrete instance of the Arnold fixed-point bound without solving the new Hamiltonian equations explicitly.

## Hamiltonian versus merely symplectic

There is a key restriction. The conclusion applies to Hamiltonian diffeomorphisms, not all symplectic diffeomorphisms. A translation of the torus by an irrational displacement preserves the area form and may have no fixed points.

But such a translation is not the time-one map of a globally defined periodic Hamiltonian isotopy in the required sense. It is not a counterexample to the bound. The distinction between preserving a symplectic form and being generated by a Hamiltonian is built into the action functional and continuation theory.

This example is a warning against overstating the theorem. The type of symmetry matters, not merely the fact that area is preserved.

## Why continuation is not purely formal

If moduli spaces were not compact or if bubbling created unaccounted boundary components, the chain-map and chain-homotopy proofs could fail. If transversality were not achieved, the relevant spaces might not be smooth of the predicted dimensions. If the Hamiltonian grew too rapidly at infinity, a continuation trajectory might escape the region where the estimate applies.

Thus continuation invariance is a theorem supported by the same analytic foundation as the differential squared zero. It is not a consequence of writing down the word 'homotopy' next to two Hamiltonians.

## The payoff for advanced lectures

When an advanced symplectic topology lecture uses Floer homology to prove that a periodic orbit exists, the hidden engine has three stages. First calculate Floer homology where the complex resembles ordinary Morse theory. Second show that changing the Hamiltonian induces an isomorphism. Third infer that the new Hamiltonian must possess enough orbit generators to support that invariant.

The torus bound makes those steps explicit. It is a model for a much broader family of existence and rigidity arguments, including ones that need Novikov coefficients, action filtrations, and more sophisticated compactness machinery.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(H_s\) equal \(H_-\) for \(s\ll0\) and \(H_+\) for \(s\gg0\), with compatible \(J_{s,t}\). A continuation solution satisfies \(\partial_su+J_{s,t}(u)(\partial_tu-X_{H_s,t}(u))=0\) and tends to capped periodic orbits \(x_-\), \(x_+\). With \(\mathcal A_H=-\int u^*\omega-\int Hdt\),
\[
E(u)=\mathcal A_{H_-}(x_-)-\mathcal A_{H_+}(x_+)
-\int_{\mathbb R\times S^1}\partial_sH_s(t,u(s,t))\,ds\,dt.
\]
This follows by differentiating the time-dependent action along \(s\). On a closed target the correction is bounded using \(\int\max_M|\partial_sH_s|\). Under standard regularity, compactness, and gluing hypotheses, counting rigid continuation cylinders defines a chain map. Reversed interpolations and two-parameter homotopies show the maps are inverse on homology.

On \(T^2\), \(\pi_2(T^2)=0\), so there is no sphere bubbling or capping ambiguity for contractible loops. For a sufficiently small generic Hamiltonian, \(HF_*(H)\cong H_{*+n}(T^2;\mathbb F_2)\) up to conventional grading shift (here n=1), giving total rank \(1+2+1=4\). A nondegenerate Hamiltonian time-one map therefore has at least four contractible fixed-point orbits. This does not apply to a non-Hamiltonian symplectic translation.

### Exercises with answers

1. **Corrected energy.** What extra term appears when H depends explicitly on s? **Answer:** minus the integral of \(\partial_sH_s\) along the continuation solution under the stated action convention.
2. **Chain homotopy.** Do continuation maps need to be literal inverses on the chain level? **Answer:** no; they are inverses on homology via chain homotopies.
3. **Torus bound.** What is the total Betti number of the two-torus over \(\mathbb F_2\)? **Answer:** four.
4. **Scope.** Does the four-fixed-point conclusion include arbitrary area-preserving torus translations? **Answer:** no; it concerns Hamiltonian time-one maps under nondegeneracy.

### Sources and further reading

- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), continuation and invariance chapters.
- Andreas Floer, [Symplectic Fixed Points and Holomorphic Spheres](https://doi.org/10.1007/BF01260388), Hamiltonian fixed-point theory.
- [Arnold conjecture](https://en.wikipedia.org/wiki/Arnold_conjecture); [Floer homology](https://en.wikipedia.org/wiki/Floer_homology).
