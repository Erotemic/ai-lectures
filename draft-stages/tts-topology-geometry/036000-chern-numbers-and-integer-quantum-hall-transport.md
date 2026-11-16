# 036000 - Chern Numbers and the Integer Quantum Hall Effect

**Track:** Topology and Geometry. **Background:** Berry connections, differential forms, line bundles, and basic quantum mechanics. **Central question:** how can a continuously varying band structure produce an electrical response pinned to an integer?

<!-- BEGIN SPOKEN LECTURE -->

# An integer hiding in a continuous spectrum

In a crystal, electrons move through a periodic environment. Energy bands depend continuously on momentum, and their eigenstates can twist continuously as momentum changes. One might expect all transport coefficients to vary continuously under small changes of the crystal. Yet the integer quantum Hall effect displays plateaus: a transverse conductance proportional to an integer number of natural units.

The mathematical source of that integer is a Chern number. It measures the global twisting of the occupied band states over momentum space. Berry curvature provides the local density of that twisting; integration over the closed momentum-space surface produces an integer under the appropriate gap and bundle assumptions.

The important relationship is not that every integral of a curvature form is an integer. It is that the curvature of a complex line bundle represents an integral cohomology class after division by two pi, using a consistent connection convention. The band states form such a bundle when a band is separated from its neighbors throughout momentum space.

# Momentum space is a torus

For a two-dimensional crystal with periodic boundary conditions, momentum is defined modulo reciprocal lattice translations. The Brillouin zone is therefore topologically a two-dimensional torus. A nondegenerate band assigns a one-dimensional complex eigenspace to each point of that torus.

An eigenvector is not uniquely determined, because multiplying it by a phase changes the vector but not the physical state. If we choose a normalized eigenvector at each point, we have selected a local gauge. Around a different patch, another normalized eigenvector may differ by a momentum-dependent phase.

That phase freedom is not a nuisance added after the mathematics. It is exactly the transition rule of a complex line bundle. If one cannot choose a globally smooth, periodic eigenvector, the obstruction may be measured by a nonzero first Chern class.

# The Berry connection and its curvature

Given a smoothly chosen normalized band eigenvector, Berry's connection is a one-form built from the inner product of that vector with its derivative. It tracks the phase accumulated during slow changes in momentum. Under a gauge change, the connection one-form changes by a derivative of the phase.

The curvature is the exterior derivative of the connection. Because taking a derivative kills the additional exact gauge term, Berry curvature is gauge invariant. Local formulas for the connection can change from patch to patch, but the curvature agrees on their overlaps.

A natural question follows. If the curvature is just a locally computed differential form, why does its integral over the torus become an integer? The answer lies in transition functions. On overlaps, gauge choices are related by maps into the unit circle. Around closed loops, the phase winds an integer number of times. Stokes' theorem converts the integrated curvature into those winding numbers.

# A calculation on the sphere

We can see the idea without a crystal. Consider a two-level Hamiltonian proportional to a unit vector n dotted with the three Pauli matrices. Let n range over the sphere. The lower-energy eigenspaces form a complex line bundle over that sphere.

Near the north pole we can select one smooth eigenvector. Near the south pole we select another. Around the equator, the two eigenvectors differ by a phase whose winding number is one, up to orientation and sign conventions. No single smooth eigenvector can cover both poles without a patch change.

The corresponding Berry curvature is half the usual area form on the sphere, again with a sign set by the chosen eigenstate and connection convention. Its integral over the sphere has magnitude two pi. Dividing by two pi gives a Chern number of magnitude one.

This small calculation is essential because it shows where the integer comes from. The curvature itself varies smoothly from point to point. The integral is pinned by topology because the bundle's transition function has an integer winding number.

# From the sphere back to a torus

A two-band crystal Hamiltonian can often be written in terms of a vector of three functions of momentum. Normalize that vector wherever the energy gap is nonzero. We then obtain a map from the Brillouin torus into the unit sphere.

The occupied eigenspaces are the pullback of a line bundle on the sphere. The first Chern number is determined by the topological degree of the normalized Hamiltonian map, with a sign depending on which band is occupied and which Berry convention is used.

A map from a torus to a sphere can have degree zero, plus one, minus one, or another integer. Small continuous changes in the Hamiltonian cannot change that degree as long as the normalized map remains defined everywhere. But if the band gap closes, the vector can vanish, normalization fails, and the topology can change. Thus a gap closing is the mathematical doorway between Hall plateaus.

# How the conductance sees the integer

In a noninteracting, two-dimensional, gapped band insulator with completely filled occupied bands, the transverse electrical conductance is proportional to the sum of their Chern numbers. The proportionality unit is the square of the elementary charge divided by Planck's constant. This is the Thouless-Kohmoto-Nightingale-den Nijs formula, commonly abbreviated TKNN.

The original analysis connects a Kubo linear-response calculation to the integrated Berry curvature. The geometry supplies the integral invariant; the response theory explains why that invariant controls transport. The formula is not obtained merely by saying that both sides are topological. The Kubo-to-curvature calculation is an essential bridge.

This also explains what the theorem does not say. Partially filled metallic bands do not generally yield quantized Hall conductance in this simple form. Strongly interacting fractional quantum Hall states need a different mathematical treatment. Disorder can preserve quantization under broader hypotheses, including mobility gaps, but the elementary translation-invariant Bloch bundle picture is then replaced or extended.

# Why edges matter without replacing the bulk argument

A sample has boundaries, and robust edge states are associated with nontrivial bulk Chern numbers. The bulk-boundary correspondence relates the net number of chiral edge modes to the bulk topological invariant under appropriate assumptions. It provides a second, physically vivid way to understand robust transport.

Yet bulk-boundary correspondence and TKNN conductance quantization are related theorems, not the same sentence repeated twice. The bulk Chern number is computed from occupied states over momentum space. The edge picture concerns spectral flow in a system with a physical boundary. Their equality demands an argument connecting these setups.

The value of the bundle perspective is its precision. Curvature is local and can vary. The Chern number is global and integral. A nonzero value obstructs a globally smooth band gauge. Changing it requires passing through a gap closing or leaving the theorem's assumptions. Electrical quantization then emerges when response theory identifies the bulk invariant with Hall conductance.

# A useful hierarchy of statements

It helps to separate four levels. A smooth isolated band defines an eigenbundle. Its Berry connection has curvature. The curvature integrates to an integer Chern number. Finally, under the physical assumptions of the integer quantum Hall setting, a Kubo formula converts that integer into a quantized response.

Each level has its own hypotheses. Keeping them distinct makes the result more powerful, not less. A geometric topological invariant does not magically imply every physical observation, but when the connection is established, it explains why a measured quantity can remain stable while the underlying microscopic Hamiltonian changes continuously.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth normalized local occupied eigenvector `|u(k)>`, define the convention `A=i<u|du>` and `F=dA`. Under `|u> -> e^(i chi)|u>`, `A -> A-d chi`; F is invariant. The first Chern number on an oriented closed Brillouin torus is
\[
 C_1=\frac{1}{2\pi}\int_{T^2}F\in\mathbb Z.
\]
For a two-band `H(k)=d(k) . sigma` with `d(k)!=0`, the eigenline bundle is the pullback under `n=d/|d|:T^2->S^2` of a Hopf-type line bundle; `C_1` equals a signed `deg(n)` depending on the occupied eigenstate and conventions. On the parameter sphere for `H=n . sigma`, the lower-band convention above has `F=(1/2)sin(theta)dtheta wedge dphi`, so `C_1=1`. Reversing band or orientation reverses the sign.

For a noninteracting, gapped, integer quantum Hall band insulator at zero temperature with completely filled bands, the TKNN formula gives `sigma_xy=(e^2/h) sum_(occupied bands) C_n` up to the chosen sign for Hall conductivity and orientation. The bundle invariant persists under smooth gap-preserving deformations. Metallic bands or fractional Hall states are outside this elementary Bloch-bundle result.

### Exercises with answers

1. If Berry curvature integrates to `6 pi`, what is the Chern number? **Answer:** three.
2. Can a band with nonzero Chern number admit a globally smooth periodic normalized eigenvector? **Answer:** no; such a vector would trivialize its line bundle.
3. What must fail for a smooth two-band Hamiltonian to change its Chern number? **Answer:** the spectral gap must close somewhere, or one of the other structural assumptions must fail.
4. Does every band automatically produce quantized Hall conductance? **Answer:** no; one requires an appropriate occupied, gapped band system and a valid response-theory setting.

### Reading and source notes

- [Thouless, Kohmoto, Nightingale, and den Nijs, Quantized Hall Conductance in a Two-Dimensional Periodic Potential](https://doi.org/10.1103/PhysRevLett.49.405), the original TKNN relation.
- [Niu, Thouless, and Wu, Quantized Hall Conductance as a Topological Invariant](https://doi.org/10.1103/PhysRevB.31.3372), topological response beyond the simplest periodic setting.
- [David Tong, Lectures on the Quantum Hall Effect](https://www.damtp.cam.ac.uk/user/tong/qhe.html), pedagogical treatment of Berry phases, Chern numbers and transport.
