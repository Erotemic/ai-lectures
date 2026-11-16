# 026000 — Front Pinning: When a Traveling Wave Stops

**Track:** Differential Equations. **Background:** reaction–diffusion equations, traveling waves, phase planes, perturbation theory. **Central question:** why does a front that propagates through a uniform medium sometimes stop at a spatial defect?

<!-- BEGIN SPOKEN LECTURE -->

# A boundary that moves

A reaction–diffusion front separates regions in different states. Imagine a chemical reaction that has already converted the material on the left but not on the right. Diffusion spreads the chemicals, while reaction terms favor one state or the other. In a uniform medium, a front may propagate with a fixed shape and speed.

But what if the medium varies from place to place? A region with lower reaction rates or different local stability can slow the front. A sufficiently strong defect may hold the interface in place. This is front pinning. When a control parameter crosses a threshold and the front starts moving again, the transition is called depinning.

These terms describe mathematically distinct phenomena. A stationary front can exist because two states are exactly balanced in a uniform medium. Pinning by heterogeneity is different: an otherwise moving front can become trapped by spatial variation.

## A bistable reaction model

A convenient model is a scalar equation with diffusion plus a cubic reaction term. The reaction has three uniform equilibria: zero, an intermediate value a between zero and one, and one. The outer states are locally stable, while the middle state is unstable.

Seek a traveling profile U depending only on position minus speed times time. A decreasing front runs from state one on the left to state zero on the right. Its motion is governed by a second-order ordinary differential equation. In the classical cubic model there is an explicit logistic-shaped profile and an exact speed.

The speed is proportional to one minus twice a. If a is below one half, state one invades state zero in our chosen orientation. If a is above one half, the front moves the other way. At a equals one half, the two stable states are balanced and the front is stationary.

This exact example is useful because it separates profile shape from the direction of travel. Diffusion sets the front's width. The imbalance between the two stable states determines the sign of its speed.

## Where the speed formula comes from

There is a qualitative energy argument behind the exact formula. Multiply the traveling-wave equation by the derivative of the profile and integrate across the real line. The diffusion term becomes a boundary contribution and vanishes for a front whose derivative decays at both ends. The speed term becomes the speed times an integral of the squared profile derivative. The reaction term becomes an integral of the reaction function from one state to the other.

The integral of the reaction term measures the difference between the wells of the associated reaction potential. At the balanced value a equals one half, the integral vanishes and the front's speed is zero. Away from that balance, its sign decides which state invades.

This makes one point precise: the front's speed is connected to a global difference in potential, not only to the local slope of the reaction near either equilibrium.

## A heterogeneous medium

Suppose the intermediate threshold a varies with position. Now the equation is no longer invariant under translations. We cannot expect every translate of a fixed wave profile to remain a solution. The front may have preferred locations where the local reaction environment balances the force that would otherwise move it.

To understand the possibility of pinning, we can approximate the motion by a collective coordinate X, the current center of the front. In a weakly heterogeneous problem, a solvability calculation based on the translation mode of the uniform front can lead to an effective equation for X. The front speed is replaced by a function of position.

Consider the illustrative reduced model in which X prime equals c zero minus epsilon times sine X. Here c zero is the speed of the unperturbed front and epsilon is the strength of a periodic inhomogeneity. A stationary position must satisfy sine X equals c zero divided by epsilon. Such a position exists only if the absolute value of c zero is no greater than epsilon.

Within that range, stable and unstable fixed positions alternate. A small perturbation of a stable pinned position moves the front back toward the defect. If the driving speed exceeds epsilon in magnitude, no equilibrium remains, and the reduced front drifts through the medium.

This toy differential equation captures a depinning threshold and the loss of equilibria, often through a saddle-node mechanism. It is not a universal exact reduction of every reaction–diffusion equation. The actual threshold and the reduced forcing function depend on the spatial profile, the front's adjoint mode, the domain, and the size of the heterogeneity.

## Pinning is a stability question

Even if a stationary front exists, we must ask whether it is stable. A stationary interface might be delicately balanced and move away after a small disturbance. To analyze this, we linearize the full PDE around the stationary profile and inspect its spectrum or construct energy estimates appropriate to the problem.

In a uniform medium, translation invariance typically produces a neutral eigenfunction: shifting the front slightly gives another stationary or traveling profile. Heterogeneity breaks this invariance and can move that neutral mode into a stable or unstable direction. Pinning can therefore be understood as a change in the dynamics of the translation mode.

There are additional complications. Strong heterogeneity can distort the front's shape; it may create multiple stationary interfaces, or make fronts interact with boundaries. In more than one dimension, curvature and geometry also influence motion. A single coordinate X cannot describe every deformation of the interface.

Yet the reduced model provides a meaningful conceptual guide. If the unperturbed front has a net drive, a defect can oppose it. When the maximal opposing effect is strong enough, the front can stop. When the drive overcomes that effect, the front moves again. The precise result must come from the PDE and its hypotheses, not from drawing a sine curve alone.

Front pinning shows how spatial structure changes dynamics. A uniform equation offers a family of translates and a constant wave speed. A heterogeneous equation chooses locations, introduces thresholds, and can replace continuous drift with stable stationary states. The study of traveling waves becomes the study of how geometry and local material properties select motion or rest.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `D>0`, `0<a<1`, consider
\[
u_t=D u_{xx}+u(1-u)(u-a).
\]
The decreasing traveling wave `u(t,x)=U(x-ct)` has the explicit form
\[
U(z)=\frac{1}{1+e^{z/\sqrt{2D}}},\qquad
c=\sqrt{\frac D2}(1-2a).
\]
Indeed `U'=-U(1-U)/sqrt(2D)` and `D U''+cU'+U(1-U)(U-a)=0` at the stated c. Multiplying the traveling-wave equation by `U'` and integrating gives
\[
c\int_{\mathbb R}(U')^2 dz=\int_0^1 s(1-s)(s-a)\,ds=\frac{1-2a}{12},
\]
consistent with the explicit speed and with the sign convention that c is positive for a<1/2.

For the illustrative collective-coordinate ODE `X'=c_0-epsilon sin X` with `epsilon>0`, equilibria exist iff `|c_0|<=epsilon`. At an equilibrium, the derivative of the vector field is `-epsilon cos X`, so equilibria with `cos X>0` are asymptotically stable and those with `cos X<0` unstable. At `|c_0|=epsilon`, equilibria merge in a saddle-node threshold. This is a reduced model, not a theorem that the full heterogeneous PDE always reduces to a sinusoidally forced scalar ODE.

### Exercises with answers

1. What happens to the explicit front speed at `a=1/2`? **Answer:** it becomes zero.
2. For `D=2,a=1/4`, what is c? **Answer:** `sqrt(2/2)*(1-1/2)=1/2`.
3. In `X'=0.3-0.5 sin X`, can pinned equilibria exist? **Answer:** yes, since `0.3<0.5`.
4. Does the existence of a stationary front guarantee stability? **Answer:** no; one must study perturbations or the linearized PDE.

### Reading and source notes

- [Fife and McLeod, The Approach of Solutions of Nonlinear Diffusion Equations to Travelling Front Solutions](https://doi.org/10.1007/BF00250432), bistable front dynamics and stability.
- [Keener, Homogenization and Propagation in the Bistable Equation](https://doi.org/10.1016/S0167-2789(99)00151-7), spatial heterogeneity and front propagation.
- [Xin, Front Propagation in Heterogeneous Media](https://doi.org/10.1137/S0036144599364296), front behavior in inhomogeneous settings.
