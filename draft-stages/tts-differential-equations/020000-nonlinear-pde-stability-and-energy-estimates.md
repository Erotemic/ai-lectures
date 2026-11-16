# 020000 — Nonlinear PDE Stability and Energy Estimates

**Track:** Differential Equations and Dynamical Systems. **Background:** diffusion, weak solutions, eigenfunctions, Grönwall inequalities, stability of equilibria. **Central question:** when can diffusion overcome nonlinear amplification?

<!-- BEGIN SPOKEN LECTURE -->

# Nonlinear PDE Stability and Energy Estimates

A reaction can amplify a disturbance while diffusion tries to smooth it. Which effect wins? The answer depends not only on the reaction law but also on the size of the domain and the boundary conditions. Energy estimates let us make that competition precise without solving the nonlinear partial differential equation explicitly.

Imagine a chemical concentration in a one-dimensional container. Its evolution has two parts. Diffusion, represented by a second spatial derivative, spreads concentration from high regions to low regions. A reaction function changes concentration locally, possibly increasing or decreasing it depending on the current value.

We would like to know whether two solutions that begin close together remain close, or even approach each other. Instead of finding each solution, subtract them. Call their difference w. It obeys a diffusion equation driven by the difference of the two reaction terms.

Now measure the squared size of w by integrating its square across the container. This is an energy, though not necessarily a physical thermodynamic energy. Differentiate it with respect to time. The diffusion term becomes negative after integration by parts, provided the boundary terms vanish. It is the negative of the integral of the squared spatial derivative of w.

## The key competition

Suppose the reaction term obeys a one-sided Lipschitz inequality. This says the product of the difference in reaction rates with the difference in states is bounded above by a constant L times the squared state difference. It does not require the reaction to be globally contractive. It tells us the maximum rate at which reaction can increase the squared distance between solutions.

The energy inequality now has one favorable term, from diffusion, and one potentially unfavorable term, from the reaction. We need a way to compare the spatial derivative energy to the ordinary energy of w.

On an interval of length ell with zero values prescribed at both endpoints, the Poincaré inequality does exactly that. It says the squared spatial derivative has integral at least pi squared divided by ell squared times the integral of w squared. In other words, a nonzero function pinned to zero at both ends must vary by a minimum amount.

If diffusion has coefficient D, the resulting contraction rate is at least D times pi squared divided by ell squared, minus the reaction's one-sided Lipschitz constant. When that expression is positive, the distance between the solutions decays exponentially.

This is a stability theorem derived entirely from inequalities. No closed-form solution of the nonlinear equation was required.

## An explicit nonlinear reaction

Consider the reaction f of u equal to u minus u cubed. Near zero, the linear term tries to amplify small disturbances. The negative cubic term restrains large positive or negative values. For any two real values a and b, the difference quotient of this reaction is one minus the sum of a squared, a times b, and b squared. The quadratic expression being subtracted is nonnegative, so the quotient is at most one.

Thus the reaction has one-sided Lipschitz constant one. With diffusion coefficient one, the energy estimate proves contraction between any two sufficiently regular solutions satisfying homogeneous Dirichlet boundary conditions if the interval is shorter than pi.

At the other end of the comparison, look at the zero equilibrium and linearize. The first spatial sine mode has growth rate one minus pi squared divided by ell squared. If the interval is longer than pi, this mode grows initially. The zero equilibrium is linearly unstable. The domain's size has changed which force dominates.

At the critical length pi, the linear rate is zero and this simple linear test is inconclusive. The cubic nonlinearity and higher-order analysis decide what happens. Treating the equality case as an automatic instability or stability result would go beyond the estimate.

## Boundary conditions matter

Why did the size of the interval enter? Because the fixed-zero boundary prevents constant nonzero differences. If we instead impose no-flux, or Neumann, boundary conditions, constant differences have zero spatial derivative. The Poincaré inequality with a strictly positive first eigenvalue no longer applies to arbitrary functions; we must separate out the spatial mean or impose another constraint.

The nonlinear equation has not changed, but the relevant function space has. That is why a stability statement that omits its boundary assumptions is incomplete.

## A priori bounds and actual solutions

An energy inequality is a powerful tool, but it must be used in the right order. First we need a solution in a class for which the manipulations are valid, or an approximation argument that justifies them. Then the inequality controls its size and helps establish uniqueness and continuous dependence. With suitable local-existence theory and a priori bounds, it may also contribute to proving global existence.

The estimate alone does not grant global existence for every nonlinear reaction. Some semilinear equations admit solutions that blow up in finite time. And an L-two bound need not automatically control every stronger norm that a nonlinear term requires.

The major idea is nevertheless general. Choose an energy adapted to the equation, differentiate it, use integration by parts, exploit coercivity or a spectral gap, and apply a differential inequality such as Grönwall's lemma. The result can explain why solutions converge or why disturbances grow, even when their exact shapes remain inaccessible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For regular solutions to \(u_t=D u_{xx}+f(u)\) on \((0,\ell)\) with homogeneous Dirichlet data and \(D>0\), consider two solutions u,v existing on the interval of time being studied. Let w=u-v. Assume
\[(f(a)-f(b))(a-b)\le L_f(a-b)^2\quad\text{for all }a,b\in\mathbf R.\]
Then by integration by parts, Poincaré's inequality and Grönwall,
\[\frac12\frac d{dt}\|w\|_{L^2}^2=-D\|w_x\|_{L^2}^2+\int_0^\ell w(f(u)-f(v))dx\le -\left(D\frac{\pi^2}{\ell^2}-L_f\right)\|w\|_{L^2}^2,\]
so if \(\mu=D\pi^2/\ell^2-L_f>0\),
\[\|u(t)-v(t)\|_{L^2}\le e^{-\mu t}\|u(0)-v(0)\|_{L^2}.\]
The standard Poincaré inequality here is \(\|w_x\|_2^2\ge(\pi/\ell)^2\|w\|_2^2\) for w in H_0^1(0,ell).

**Allen–Cahn-type example:** \(f(u)=u-u^3\) has \((f(a)-f(b))/(a-b)=1-(a^2+ab+b^2)\le1\) when a≠b, so \(L_f=1\). With D=1, \(\ell<\pi\) gives contraction. Linearizing at u=0 yields eigenvalues \(1-(n\pi/\ell)^2\). For ell>pi the n=1 eigenmode grows linearly; ell=pi is the borderline case requiring nonlinear analysis. The linear instability claim is about the zero equilibrium, not about every solution or equilibrium.

**Caveats:** Neumann conditions permit constant modes, making the zero-boundary Poincaré constant invalid for arbitrary differences. Weak solutions require justified testing by w, typically through approximation or monotone/energy methods. The estimate holds on any time interval where such solutions exist; it does not independently prove global existence.

### Exercises with answers

1. For D=4 and L_f=1, which interval lengths guarantee contraction? **Answer:** ell<2pi.
2. Why does integration by parts produce no boundary term with homogeneous Dirichlet conditions? **Answer:** w vanishes at both endpoints.
3. For ell=2pi, D=1, f(u)=u-u³, what is the first linearized growth rate? **Answer:** \(1-(\pi/2\pi)^2=3/4>0\).
4. Why can the contraction theorem fail with Neumann boundaries? **Answer:** a constant nonzero w has zero gradient, so diffusion supplies no coercive decay for that mode.

### Reading and source notes

- [University of Chicago PDE notes](https://www.math.uchicago.edu/~luis/pdenotes.pdf), heat-equation energy methods and boundary dependence.
- [Lawrence C. Evans, Partial Differential Equations, AMS](https://bookstore.ams.org/gsm-19-r), functional analysis and nonlinear PDE estimates.
