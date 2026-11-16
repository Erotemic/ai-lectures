# 033000 — Berry Curvature: Holonomy in a Family of Quantum States

**Track:** Topology and Geometry. **Background:** complex line bundles, connections, curvature, eigenvectors, and the two-sphere. **Central question:** why can slowly transporting an eigenstate around a closed loop change its phase even if its energy returns to its original value?

<!-- BEGIN SPOKEN LECTURE -->

# A state can return without its phase returning

Imagine a quantum system whose Hamiltonian depends on a controllable direction. Turn a magnetic-field direction slowly around a closed loop and bring it back to the starting point. If the system begins in a nondegenerate eigenstate and the evolution is sufficiently adiabatic, it remains in the corresponding instantaneous eigenspace, up to a phase.

One part of that phase depends on how long the trip took and on the energy along the route. That is the dynamical phase. There can be another part that depends only on the path through parameter space. This is the Berry phase. It is geometric rather than simply dynamical.

At first it seems that an arbitrary choice of eigenvector phase could remove such a phenomenon. At each parameter value, multiplying an eigenvector by a complex number of magnitude one gives another eigenvector for the same eigenvalue. But choosing a phase independently at every point is not the same as choosing one consistently around a loop. The obstruction is holonomy: the failure of parallel transport to return a vector exactly to its starting value.

# Eigenvectors define a line bundle

Suppose the Hamiltonian depends smoothly on parameters and one eigenvalue stays isolated and nondegenerate. At each parameter, its eigenvectors form a one-dimensional complex vector space. Assemble those spaces over the parameter domain. They form a complex line bundle.

A line bundle may not admit one globally smooth, nonvanishing choice of normalized eigenvector. Even when it does, a connection can have nontrivial curvature. These are distinct issues. Bundle topology constrains what global choices exist; the connection specifies how to compare phases at nearby points.

Given a local normalized eigenvector u, the Berry connection is built from the inner product of u with its differential. It is a real-valued one-form in the standard convention. When we change gauge by multiplying u by an exponential phase, the connection changes by a derivative. But the curvature, the exterior derivative of the connection, does not change.

A loop integral of the connection gives the geometric phase modulo a whole turn, provided the gauge patches are handled correctly. Over a surface, Stokes' theorem relates that loop integral to curvature flux. The form of this statement should sound familiar from electromagnetism, but the connection here lives on a bundle of eigenspaces rather than on physical space itself.

# A two-level Hamiltonian makes curvature visible

Consider the two-by-two Hamiltonian obtained by taking a unit vector n and dotting it with the three Pauli matrices. The parameter n moves on the ordinary two-sphere. The Hamiltonian has two eigenvalues, plus one and minus one, separated by a fixed gap.

Focus on the lower eigenvalue. Its eigenvectors form a line bundle over the sphere of directions. In spherical coordinates, its Berry curvature is one half of the ordinary area form of the unit sphere, with the sign determined by the choice of lower state and Berry-connection convention.

Integrate over the whole sphere. The area of the unit sphere is four pi. Half that area is two pi. Dividing the curvature integral by two pi gives the integer one. This is the first Chern number of the lower eigenstate line bundle in the convention we have chosen.

That nonzero integer has an immediate consequence. There cannot be a single smooth phase choice for the lower eigenvector over the entire sphere. Any explicit formula must have a gauge singularity somewhere, or else we must use overlapping charts with a nontrivial phase transition function.

# Solid angle controls the holonomy

Take a loop on the sphere bounding a region of solid angle Omega. Its geometric phase for the lower eigenstate is half that solid angle, modulo two pi, with the same sign convention as our curvature calculation.

For a small loop near the north pole, the sphere looks nearly flat and the phase is approximately one half the area enclosed in parameter space. For a loop around the equator that bounds a hemisphere, the enclosed solid angle is two pi, so the Berry phase is pi. A complex amplitude multiplied by the exponential of i pi changes sign.

This result is easy to misinterpret. The lower eigenstate as a ray returns to the same physical eigenspace; a minus sign does not make it a different ray. The phase becomes observable through interference with another path or reference state. A gauge-invariant phase difference, not an arbitrary eigenvector label, is the measurable quantity.

# Where does the curvature come from?

One can compute the Berry curvature without choosing an eigenvector. The spectral projector onto an isolated eigenstate depends smoothly on the parameters. By differentiating the projector and taking a trace, one obtains a gauge-invariant curvature formula.

For the two-level example, the projector onto the lower eigenvalue is one half of the identity minus the Pauli matrices dotted with n. Its derivative records how the eigenline rotates as n changes. The algebra of Pauli matrices produces the oriented area form on the sphere.

This calculation explains the topological charge in a second way. The map from parameters to the Bloch sphere wraps the target sphere once. The curvature integral records that winding. If the gap closes at a parameter value, the projector ceases to be defined there, and the Chern number can change as a family passes through that degeneracy.

# Adiabaticity and topology have different roles

The adiabatic theorem has hypotheses: a separated eigenvalue, sufficient smoothness, and a time scale slow relative to the relevant gap. Berry curvature itself can be defined as geometric data of an isolated eigenbundle without evolving a system in time. The adiabatic theorem is what makes that geometric data govern the phase of an evolving quantum state.

A nonzero local Berry curvature does not require a nontrivial Chern number. On a contractible parameter domain, the line bundle is topologically trivial, yet the connection may still have curvature and loops can have nonzero holonomy. Conversely, the integral Chern number is a global property that remains unchanged under smooth perturbations preserving the spectral gap.

The distinction matters in band theory and topological phases. Berry connections and curvatures can be computed from Bloch eigenstates as momentum varies. Integrating curvature over a closed momentum-space surface can produce an integer topological invariant. The same geometry that explains a slowly rotated spin also helps explain quantized transport in periodic materials.

Berry phase is therefore an example of how a local choice and a global invariant can coexist. We may freely choose the phase of an eigenvector at each point. We cannot freely choose the curvature of the associated connection or its integrated topological charge. The phase accumulated around a loop is the observable trace of that geometry.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a normalized eigenstate section `u(lambda)`, use `A=i<u,du>` and `F=dA`, so a gauge change `u -> e^{i chi}u` sends `A -> A-d chi` and leaves F invariant. With this convention the Berry phase is `gamma=oint A mod 2pi` (the dynamical phase is separate).

Take `H(n)=n_x sigma_x+n_y sigma_y+n_z sigma_z` for `n in S^2`. The negative-energy projector is `P_-=(I-n.sigma)/2`. The gauge-independent curvature form is `F_-=i Tr(P_- dP_- wedge dP_-)`. The Pauli identity `sigma_a sigma_b=delta_ab I + i epsilon_abc sigma_c` gives
\[
F_-=\frac14\varepsilon_{abc}n_c\,dn_a\wedge dn_b
=\frac12\sin\theta\,d\theta\wedge d\phi,
\qquad c_1(L_-)[S^2]=\frac1{2\pi}\int_{S^2}F_-=1.
\]
For a loop bounding a patch with oriented solid angle Omega, `gamma=Omega/2 mod 2pi`. The positive-energy eigenline has the opposite Chern number. Reversing Berry-connection sign conventions reverses all these displayed signs consistently, not the physical phase difference.

### Exercises with answers

1. Compute the Berry phase for a loop bounding one quarter of the sphere. **Answer:** the solid angle is pi, so phase is pi/2 modulo 2pi.
2. Can one choose a globally smooth normalized negative-energy eigenvector over the whole sphere? **Answer:** no; its first Chern number is one.
3. If `u -> e^{i chi}u`, what happens to curvature? **Answer:** nothing; the connection shifts by an exact form and `d^2chi=0`.
4. Must a topologically trivial eigenbundle have zero Berry curvature? **Answer:** no; topology and the chosen connection are different kinds of data.

### Reading and source notes

- [Barry Simon, Holonomy, the Quantum Adiabatic Theorem, and Berry's Phase](https://authors.library.caltech.edu/records/2pepc-k9f58), interpretation as line-bundle holonomy.
- [Kohei Kawabata, Berry phase of a two-level system](https://kawabata.issp.u-tokyo.ac.jp/lectures/2024CMP/Berry_twolevel.pdf), spin-half example and Chern-number calculation.
- [M. V. Berry, Quantal phase factors accompanying adiabatic changes](https://doi.org/10.1098/rspa.1984.0023), original geometric-phase formulation.
