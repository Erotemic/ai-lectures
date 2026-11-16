# 030000 — The Maslov Index: Why a Classical Orbit Acquires a Quantum Half-Step

**Track:** Topology and Geometry. **Background:** Hamiltonian mechanics, symplectic phase space, and elementary wave asymptotics. **Central question:** what geometric phase correction appears when semiclassical waves pass through turning points?

<!-- BEGIN SPOKEN LECTURE -->

# A missing half in a quantum energy formula

The quantum harmonic oscillator has energy levels separated by a fixed amount. Its energies are not zero, one, two, and so on times that amount. They are one half, one and a half, two and a half, and so on. The one-half offset matters: even the ground state carries positive energy.

There is a geometric explanation for the offset. A semiclassical wave accumulates phase as it moves along a classical orbit. But when its path passes through a turning point, the usual local oscillatory description breaks down. Matching the wave across that turning point adds a phase correction.

The Maslov index is an integer that packages these corrections. It tells us why the naive rule of counting whole wavelengths around a classical orbit misses a half-step in a one-dimensional potential well.

# The classical action around an orbit

Consider a particle of mass m moving in a smooth confining potential. Its classical energy is kinetic energy plus potential energy. At a fixed energy, the momentum is positive as the particle moves right and negative as it returns left.

Draw the orbit in the phase plane, with position horizontally and momentum vertically. For a bound one-dimensional motion, the orbit is a closed loop. The integral of momentum against position around that loop is called the action. Geometrically, it is the area enclosed by the orbit, with a chosen orientation.

In the simplest old semiclassical rule, one demands that this action be an integer multiple of Planck's constant. That idea captures much of the spectrum at high energies, but it neglects the behavior at turning points, the positions where classical momentum becomes zero and the wave changes from oscillatory to exponentially decaying.

# What goes wrong at a turning point?

Away from a turning point, a semiclassical wave can be written approximately as a rapidly oscillating exponential whose phase comes from integrating momentum over position. The amplitude is inversely related to the square root of the local momentum.

That amplitude formula becomes singular when the momentum vanishes. The actual physical wave need not be singular. Instead, the approximation has become invalid. Near a simple turning point, one rescales the equation, and the leading local behavior is governed by an Airy function. Matching the Airy behavior to the oscillatory solutions supplies a phase shift.

Each ordinary soft turning point contributes a specific fraction of a full oscillation in the matching condition. For a one-dimensional well bounded by two simple turning points, their combined correction becomes a half-integer shift in the quantization rule.

This is a geometric correction, not a freely fitted constant. It follows from how local wave phases join as the classical orbit passes through places where the projection from phase space onto position space becomes singular.

# The Maslov index

In more geometric language, a family of tangent subspaces to the classical trajectory defines a path of Lagrangian directions. There is a distinguished set of directions where a chosen projection becomes singular. Crossing that set changes the phase of the semiclassical amplitude.

The Maslov index counts these crossings with signs and multiplicities under the chosen convention. In the ordinary one-dimensional bound-state problem with two soft turning points, the relevant index is two.

The improved quantization rule says that the action around the orbit is two pi times reduced Planck's constant, multiplied by the integer quantum number plus one quarter of the Maslov index. For index two, one quarter of the index is one half.

Different sign conventions may reverse an oriented index, but once the action orientation and phase convention are consistent, the physical quantization condition is unchanged.

# Calculate the harmonic oscillator

Now choose a harmonic potential: half the mass times the squared angular frequency times the squared position. The classical phase-plane orbit is an ellipse. Its area is the action integral. The ellipse has maximum position given by the oscillation amplitude and maximum momentum equal to mass times angular frequency times that amplitude.

Multiplying the two semi-axes and pi, we find that the enclosed area is two pi times the energy divided by the angular frequency.

Insert this action into the corrected quantization rule. Two pi times energy divided by frequency must equal two pi times reduced Planck's constant times the integer plus one half. Divide by two pi and multiply by frequency. The energy is reduced Planck's constant times angular frequency times the integer plus one half.

This is exactly the harmonic-oscillator spectrum. The semiclassical formula happens to reproduce the exact eigenvalues for this quadratic system. For a general potential well, it is an approximation, typically improved in the semiclassical or high-energy limit. The exactness of the oscillator does not license an exact spectral formula for every smooth potential.

# A comparison without turning points

Consider a free particle moving around a circle. Its classical trajectory has no turning point in the angular coordinate. The wave must be single-valued after one trip around the circle, but there is no Airy matching at a soft reflection. In the basic rotor model, the corresponding Maslov correction vanishes.

The angular momentum is an integer multiple of reduced Planck's constant, and the energy is proportional to the square of that integer. The contrast with the oscillator is instructive: both systems involve closed classical orbits, but only the oscillator's projected orbit has the two ordinary turning points responsible for the half-step.

# A topological index with spectral consequences

In higher-dimensional semiclassical mechanics, phase corrections arise at caustics where families of rays focus. The same underlying Maslov-index principle appears in wave propagation, Fourier integral operators, and geometric quantization.

The index is topological in the sense that it records how a path of Lagrangian subspaces winds relative to a singular set. Yet its effect is measurable as a shift in an energy quantization condition. The remarkable bridge is that topology of phase-space geometry changes the phase of a wave and therefore the allowed quantum states.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `H=p^2/(2m)+V(q)` with two simple turning points at energy E and a closed phase-plane orbit `gamma_E`, the leading corrected Bohr–Sommerfeld/EBK rule is
\[
\oint_{\gamma_E} p\,dq=2\pi\hbar\left(n+\frac\mu4\right),
\quad n=0,1,2,\ldots,
\]
where in the standard orientation and two-soft-turning-point convention `mu=2`. This is a *semiclassical* rule with regularity and nondegeneracy assumptions, not a general exact eigenvalue formula.

For `V(q)=m omega^2 q^2/2`, write the turning-point amplitude `a=sqrt(2E/(m omega^2))`. The phase-plane orbit is an ellipse with semi-axes `a` and `m omega a`, so
\[
\oint p\,dq=\pi a(m\omega a)=\frac{2\pi E}{\omega}.
\]
For `mu=2` the rule gives `E_n=hbar omega(n+1/2)`, which coincides with the exact spectrum for this quadratic Hamiltonian.

For a free rotor with coordinate theta on the circle, the action integral is `2 pi L` and the simple model has `mu=0`. Hence `L=n hbar`, `E_n=n^2 hbar^2/(2I)` for integer n (positive and negative momentum sectors). Different boundary conditions or nontrivial line bundles can shift rotor quantization, so this example specifies the ordinary periodic boundary condition.

### Exercises with answers

1. Compute the Maslov correction `mu/4` for two soft turning points. **Answer:** `2/4=1/2`.
2. What is the classical action of a harmonic oscillator with energy E and frequency omega? **Answer:** `2 pi E/omega`.
3. Why does the naive WKB amplitude fail at a turning point? **Answer:** it contains inverse powers of momentum, which vanishes there; an Airy-type uniform approximation is needed.
4. Does the corrected Bohr–Sommerfeld rule give exact eigenvalues for every potential? **Answer:** no; exact agreement for the harmonic oscillator is a special feature of the quadratic problem.

### Reading and source notes

- [MIT 5.73 Lecture Notes, Harmonic Oscillator and WKB](https://web.mit.edu/5.73/oldwww/Fall02/notes07.pdf), turning-point matching and oscillator quantization.
- [University of Toronto, Bohr–Sommerfeld Approximation](https://www.math.toronto.edu/ivrii/APM-textbook/Chapter6/L6.3.html), semiclassical spectral approximation and the Maslov index.
- [Bohr–Sommerfeld Quantization Lecture Notes](https://everettyou.github.io/teaching/PHYS130B/notes/ch3_path-integral/3-3-3-bohr-sommerfeld-quantization.html), phase corrections and the half-integer rule.
