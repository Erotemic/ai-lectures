# 014000 — Reaction–Diffusion Systems and Turing Instability

**Track:** Differential Equations and Dynamical Systems. **Background:** PDE diffusion, linear systems, eigenvalues, stability and bifurcation. **Central question:** how can two individually diffusing chemical species destabilize a uniform equilibrium and select spatial patterns?

<!-- BEGIN SPOKEN LECTURE -->

# Reaction–Diffusion Systems and Turing Instability

Diffusion usually smooths differences. Put dye in water and its concentration spreads until sharp boundaries fade. One might therefore suppose that adding diffusion to a stable chemical system can only make it more stable. But two reacting species can behave differently: their combined reaction and diffusion can make a uniform equilibrium unstable to some spatial disturbances even when it is stable to disturbances that are uniform everywhere.

Alan Turing analyzed this possibility in his 1952 paper, The Chemical Basis of Morphogenesis. The mathematical mechanism is now called a Turing instability. It provides a model for how spatial structure can arise from locally uniform reaction rules. The mechanism is precise, but deriving a linear instability is not the same as proving that a particular stable biological pattern must emerge.

## Begin with reactions at one point

Let u and v denote the concentrations of two chemical species. Ignore space temporarily. Suppose their rates of change are given by functions f of u and v, and g of u and v. A homogeneous equilibrium is a pair of concentrations u star, v star where both reaction rates are zero.

To study small perturbations, linearize around this equilibrium. The result is a two-by-two Jacobian matrix J. Its entries record how each reaction rate changes when one concentration changes. Call them a and b in the first row, c and d in the second.

For a real two-by-two system, the equilibrium is linearly asymptotically stable if the trace a plus d is negative and the determinant a d minus b c is positive. These inequalities ensure that both eigenvalues have negative real parts. Without spatial effects, small disturbances decay.

## Add spatial diffusion

Now let concentrations vary with position. Suppose u diffuses with coefficient D u and v with coefficient D v, both positive. The equations add D u times the Laplacian of u to the first rate law, and D v times the Laplacian of v to the second.

Diffusion alone damps Fourier modes. A spatial mode with wave number q has a Laplacian contribution of negative q squared. After linearization, the matrix controlling that mode becomes the reaction Jacobian minus q squared times the diagonal matrix of diffusion coefficients.

At q equal to zero this reduces to the original reaction Jacobian. We assumed that this homogeneous mode is stable. At nonzero q, however, the two diagonal entries are shifted by different amounts. If the diffusion coefficients differ sufficiently and the species influence one another in the right way, an eigenvalue can cross into the positive half-plane.

The system becomes stable to uniform disturbances but unstable to disturbances with selected spatial wavelengths. That is the central mathematical surprise.

## Derive the instability test

The trace for wave number q is the original trace minus the sum of diffusion coefficients times q squared. Since the original trace was negative, the new trace stays negative for all nonnegative q squared. Therefore instability cannot arise by making the trace positive in this two-species setting.

The determinant provides the opening. Expand it. The result is the original positive determinant, minus q squared multiplied by a times D v plus d times D u, plus the product D u D v times q to the fourth power.

Think of this as an upward-opening quadratic in q squared. At q zero it is positive. At very large q it is positive again. For it to become negative in between, its minimum must lie at a positive value of q squared and fall below zero. That requires a times D v plus d times D u to be positive, and its square to exceed four times the product of the diffusion coefficients and the determinant of J.

Those inequalities give a clear necessary and, for continuously available positive wave numbers, sufficient linear diffusion-driven instability condition, assuming the original homogeneous equilibrium was linearly stable. On a finite domain, only particular spatial wave numbers are allowed by the geometry and boundary conditions. Even if a continuous band would be unstable, the finite domain may have no admissible mode in that band.

## Work through actual numbers

Take the reaction Jacobian with first row one and negative two, and second row two and negative three. Its trace is negative two, and its determinant is one. So the homogeneous equilibrium is linearly stable.

Let u diffuse with coefficient one and v with coefficient twenty. For a spatial mode with q squared equal to one quarter, the mode matrix has first diagonal entry three quarters and second diagonal entry negative eight. The off-diagonal entries remain negative two and two. Its determinant is negative two. The trace is negative seven and one quarter.

A negative determinant means the two eigenvalues have opposite signs. One is positive. Thus this spatial mode grows, even though the original homogeneous reaction system was stable. On a periodic interval of length four pi, a mode with wave number one half is admissible, so this example genuinely demonstrates a finite-domain linear instability.

The fast-diffusing v component acts like a spatially distributed influence. Each individual diffusion term damps its own concentration's spatial variation, but the reaction coupling can turn those unequal damping rates into amplification of the combined mode.

## Linear instability is not a finished pattern

An eigenvalue with positive real part tells us that sufficiently small perturbations in its eigendirection initially grow. It does not determine their eventual amplitude, their nonlinear shape, or whether the long-time state is steady, oscillatory, chaotic, or unstable in another way.

Nonlinear terms become important as growth proceeds. The solution may settle into a stable spatial pattern, but it may also develop traveling waves, oscillations, coarsening structures, or other dynamics depending on kinetics, geometry, and parameters. Additional bifurcation and nonlinear PDE analysis are needed to establish the final behavior.

Likewise, the presence of two species with one diffusing much faster than the other does not by itself guarantee a Turing instability. The reaction Jacobian must satisfy the inequalities, and an admissible spatial mode must lie in the unstable band.

## Relating this to the other PDE families

The wave equation from the preceding lecture propagates disturbances along characteristics at finite speed. A reaction–diffusion equation contains parabolic diffusion, which smooths spatial modes and does not have the same finite domain of dependence. Yet coupled nonlinear reaction terms can make certain modes grow over time.

These two mechanisms should not be conflated. Waves transport information. Diffusion dissipates gradients, while reaction coupling may amplify selected modes. Their mathematical stability analyses ask different questions.

Turing's contribution was to show that local reaction rules and unequal diffusion can produce a route from homogeneous chemistry toward spatial organization. The compelling idea survives only when we retain the precise conditions: stable homogeneous kinetics, diffusion-driven instability of some nonzero spatial mode, and a separate nonlinear analysis of what happens after the initial growth.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(D_u,D_v>0\), consider
\[u_t=f(u,v)+D_u\Delta u,\qquad v_t=g(u,v)+D_v\Delta v.\]
At a homogeneous equilibrium, write \(J=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), \(\tau=a+d\), \(\Delta_0=ad-bc\). Homogeneous linear asymptotic stability requires \(\tau<0\), \(\Delta_0>0\).

For a Laplacian eigenmode \(-q^2\), the evolution matrix is \(M(q)=J-q^2\operatorname{diag}(D_u,D_v)\), with
\[\operatorname{tr}M(q)=\tau-(D_u+D_v)q^2<0,\]
\[\det M(q)=\Delta_0-(aD_v+dD_u)q^2+D_uD_vq^4.\]
With continuously available \(q^2>0\), there is a diffusion-driven unstable band iff
\[aD_v+dD_u>0,\qquad (aD_v+dD_u)^2>4D_uD_v\Delta_0,\]
in addition to homogeneous stability. On bounded domains, a mode in the unstable band must actually belong to the Laplacian spectrum with the specified boundary conditions.

**Worked example:** \(J=\begin{pmatrix}1&-2\\2&-3\end{pmatrix}\), \((D_u,D_v)=(1,20)\), so \(\tau=-2\), \(\Delta_0=1\). At \(q^2=1/4\), \(M(q)=\begin{pmatrix}3/4&-2\\2&-8\end{pmatrix}\), \(\operatorname{tr}M=-29/4\), \(\det M=-(6)+4=-2\). On a periodic interval of length \(4\pi\), the Fourier mode \(q=1/2\) is available. One eigenvalue is positive. Nonlinear saturation and long-time pattern existence are not proved by this linearization.

### Exercises with answers

1. For \(J\) in the worked example, is the spatially uniform mode stable? **Yes:** trace \(-2<0\) and determinant \(1>0\).
2. If the determinant of a real two-by-two mode matrix is negative, what happens? **Answer:** its eigenvalues are real with opposite signs, so one mode grows exponentially.
3. Does a fast inhibitor alone guarantee patterns? **No:** reaction inequalities and admissible spatial eigenmodes are also required.
4. What does Turing's linear test *not* establish? **Answer:** existence and nonlinear stability of a particular finite-amplitude steady pattern.

### Reading and source notes

- Alan M. Turing, [*The Chemical Basis of Morphogenesis* (1952)](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/old_literature/Turing1952.pdf), original diffusion-driven instability mechanism and model limitations.
- [Andrew Hodges's bibliographic record of Turing's morphogenesis papers](https://www.turing.org.uk/sources/biblio3.html), historical attribution and 1952 publication details.
- [University of British Columbia teaching notes on reaction–diffusion and Turing patterns](https://personal.math.ubc.ca/~keshet/MCB2012/SlidesLEK/RDTuring_ppt.pdf), activator-inhibitor example and diffusion contrast.
