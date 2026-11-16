# 031100 — Action Filtrations and Novikov Series: Keeping Infinite Floer Counts Finite

**Track:** Topology and Geometry. **Background:** capped Hamiltonian action, sphere classes, chain complexes, formal power series. **Central question:** what algebra is needed when one periodic orbit admits infinitely many topologically different cappings?

<!-- BEGIN SPOKEN LECTURE -->

# Action Filtrations and Novikov Series: Keeping Infinite Floer Counts Finite

A finite-dimensional Morse complex is usually easy to write down as a vector space: one generator for each critical point. On a compact manifold, a generic Morse function has finitely many critical points. The boundary of one generator is a finite sum of other generators.

Hamiltonian Floer theory can look similar when the symplectic manifold is aspherical. But on a general symplectic manifold, a periodic orbit may be equipped with many different capping disks. The same geometric loop can then represent infinitely many generators carrying different action values and gradings.

To keep the differential meaningful, we must control infinite sums. The relevant algebra is a Novikov completion, organized by symplectic area.

## One loop, several cappings

Take a contractible loop in the symplectic sphere. Fill it by one disk. Then change that filling by attaching a sphere once, twice, or many times. These fillings have different total symplectic areas even though their boundary loop is unchanged.

Under our action convention, attaching a sphere with positive area decreases the action by that area. If the sphere has normalized area one, repeating the attachment creates a sequence of actions differing by integers.

The corresponding capped orbits must be distinguished if we want real-valued action and an unambiguous integer grading. The Floer differential can connect different cappings when a cylinder carries a nontrivial relative homotopy class. Consequently, even a finite set of geometric orbits can support an infinite formal chain module.

The right question is not whether every possible coefficient is eventually zero. It is whether the series behaves well with respect to energy and action, so that any calculation at a fixed energy cutoff contains only finitely many relevant terms.

## Action decreases along Floer trajectories

Recall the energy identity. For an s-independent Hamiltonian, the energy of a Floer trajectory equals the action at its incoming capped orbit minus the action at its outgoing capped orbit.

A nonconstant trajectory consumes positive energy. Thus the differential is filtered by action: terms in the boundary move toward lower action. In a chain complex with infinitely many possible cappings, we may organize generators by their action values and complete the chain group in the direction allowed by this decrease.

Think of the chain as an infinite formal sum where there are only finitely many terms above any specified action threshold, subject to the precise Novikov finiteness rule. Then extracting all terms with action above that threshold gives a finite problem.

This is the basic reason action filtrations are useful. They remember more than the eventual homology group. They track the amount of action at which algebraic information appears or disappears.

## The simplest Novikov series

Suppose the possible sphere areas lie in the integer multiples of a positive number alpha. Introduce a formal symbol T, with exponent recording area.

A simple Novikov series can look like a zero-degree term, a term with one power of T, another with two powers, and so on without end. We allow infinitely many terms with increasing exponents, but we require only finitely many terms whose exponents lie below any fixed upper bound.

This is analogous to ordinary formal power series, except that the exponents need not be integers in more general examples, and their ordering comes from an area homomorphism. Multiplication adds the exponents. That mirrors the geometric fact that attaching two sphere classes adds their symplectic areas.

Different authors reverse the sign of the action or the Novikov exponent. We must specify which direction the completion uses instead of relying on the letter T alone. The principle is stable: formal sums are restricted so that bounded-energy portions of a count are finite.

## Recapping also changes the grading

The action ambiguity and the grading ambiguity arise from two different characteristic evaluations. Symplectic area changes the action. The first Chern class evaluated on the attached sphere changes the relevant Conley–Zehnder grading, by twice the Chern number up to the sign convention.

If symplectic area vanishes on spheres, action does not depend on the capping. If the first Chern class also vanishes on spheres, an absolute integer grading can be defined more simply. These conditions hold on a torus and allow the clean first model of Floer homology.

On a sphere, neither condition generally holds. This does not mean Floer homology ceases to exist. It means its algebra needs to remember the missing topological information.

## Why filtering does not solve analysis

A Novikov ring does not magically produce compactness of pseudoholomorphic curves. It organizes the contributions after analytic control has established what solutions exist and how their energies behave.

If sphere bubbling contributes to a boundary stratum of the moduli space, one still needs a theory that accounts for the bubbles. If transversality fails for a multiple cover, a formal variable T does not repair it. If a cylinder can escape to infinity in a noncompact target, finiteness of formal coefficients alone does not bring it back.

This separation is fundamental. The Novikov condition is an algebraic completion. Gromov compactness and virtual perturbation methods are analytic-geometric inputs. They cooperate, but neither replaces the other.

## From filtrations to spectral invariants

Once the complex is equipped with an action filtration, a homology class may be representable by cycles whose action lies below a particular level. One can ask for the smallest level, in a suitable sense, at which that class appears. Such questions lead to spectral invariants.

Those invariants can extract quantitative information about Hamiltonian dynamics, not just qualitative information about the existence of periodic orbits. Under suitable hypotheses they relate to displacement energy, Hofer geometry, and symplectic capacities.

For now we do not need the full construction. We need the reason it can work: an action-filtered chain complex retains a numerical measure of the geometric cost of the trajectories being counted.

## The conceptual boundary

Finite-dimensional Morse theory begins with a function on a finite-dimensional space. Hamiltonian Floer theory begins with a potentially multivalued action on loop space. Cappings resolve the ambiguity by enlarging the set of generators. Novikov completions then control the resulting infinite sums.

Whenever an advanced lecture speaks of a completed Floer complex, a Novikov coefficient ring, or action-filtered homology, remember those three separate operations: label the topology, calculate the area shift, and impose a finiteness condition compatible with energy. The formal algebra is answering a concrete geometric problem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A\in\pi_2(M)\), recapping \((x,u)\) by \(A\) gives
\[
\mathcal A_H([x,u\#A])=\mathcal A_H([x,u])-\omega(A).
\]
The Conley–Zehnder index changes by \(\pm2\langle c_1(TM),A\rangle\) depending on the chosen capping and index conventions. The action completion is generally taken so that for every real cutoff \(C\), only finitely many generators in a formal chain have action \(>C\) (for a bounded set of underlying periodic orbits and the usual downward action filtration). The equivalent Novikov coefficient convention can be written
\[
\Lambda_{\Gamma}=\Big\{\sum_{A\in\Gamma} a_A T^{\omega(A)}:\
\#\{A:a_A\ne0,\ \omega(A)\le C\}<\infty\text{ for every }C\in\mathbb R\Big\},
\]
for an appropriate quotient \(\Gamma\) of \(\pi_2(M)\) and coefficient field; the precise quotient and completion depend on the theory. In the one-generator area group \(\omega(\Gamma)=\alpha\mathbb Z\), \(\alpha>0\), this includes formal Laurent series \(\sum_{k\ge k_0}a_k T^{k\alpha}\). A real action filtration and a grading may require distinct group data.

### Exercises with answers

1. **Action shift.** A capped orbit has action five. After adding a sphere of area two, what is its action? **Answer:** three under the stated convention.
2. **Series.** Does \(\sum_{k=0}^\infty T^{k\alpha}\) satisfy the one-generator Novikov finiteness rule? **Answer:** yes, if \(\alpha>0\).
3. **Bad direction.** Does \(\sum_{k=0}^\infty T^{-k\alpha}\) satisfy that rule? **Answer:** no; infinitely many nonzero terms have exponent at most zero.
4. **Analysis.** Does Novikov completion alone exclude holomorphic sphere bubbling? **Answer:** no; separate geometric and analytic hypotheses are needed.

### Sources and further reading

- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), Novikov rings and action values.
- Yong-Geun Oh, [Lectures on Floer Theory and Spectral Invariants](https://cgp.ibs.re.kr/~yongoh/oh-finalfinal.pdf), filtered Floer theory.
- [Novikov ring](https://en.wikipedia.org/wiki/Novikov_ring); [Symplectic aspherical manifold](https://en.wikipedia.org/wiki/Aspherical_space#Symplectically_aspherical_manifolds).
