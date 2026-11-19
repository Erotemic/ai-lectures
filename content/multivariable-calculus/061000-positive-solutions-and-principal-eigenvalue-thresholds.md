# Positive Solutions and Principal Eigenvalues: When a Nonlinear State Can Exist

**Track:** Multivariable Calculus from First Principles. **Focus:** the first Dirichlet eigenvalue, a necessary and sufficient existence threshold, positivity, uniqueness, scaling with domain size, and the first Fourier correction.

<!-- BEGIN SPOKEN LECTURE -->

# Positive Solutions and Principal Eigenvalues: When a Nonlinear State Can Exist

A reaction term can encourage a positive population, a chemical concentration, or a deflection to grow. Diffusion acts in the opposite direction: it smooths the profile and allows material to escape through the boundary. Which effect wins? The answer often depends on a single number supplied by the linear part of the equation: the principal eigenvalue.

We will make this statement exact for our model problem. On the interval between zero and pi, let the negative second derivative of u equal lambda u minus u cubed, with u equal to zero at both endpoints. We are looking for a solution that is strictly positive in the interior. The claim is simple to state: such a solution exists precisely when lambda is greater than one. Moreover, there is exactly one positive solution for each such lambda.

That conclusion is stronger than saying the equation has a nonzero solution. It identifies a parameter threshold, specifies the sign of the solution, and rules out two different positive equilibria. We will separate the proof into necessity, construction, and uniqueness, because each uses a different piece of mathematics.

## Why the first eigenfunction is the right test

The first Dirichlet eigenfunction on this interval is sine of x. It is positive inside and zero at the endpoints. Its eigenvalue is one, meaning its negative second derivative equals itself.

Suppose a positive solution exists. Multiply its equation by sine of x and integrate. Move the second derivative onto the sine function by integrating twice by parts. The endpoint contributions vanish because both functions are zero there.

The left-hand side becomes the integral of u times sine of x. The right-hand side is lambda times that same integral, minus the integral of u cubed times sine of x. Rearranging says: lambda minus one, multiplied by the integral of u times sine of x, equals the integral of u cubed times sine of x.

Every factor on the right is positive in the interior. The integral is strictly positive. The integral multiplying lambda minus one is also strictly positive. Hence lambda minus one must be positive. There can be no positive solution at lambda equal to one or below.

This proof is economical, but it is not just an algebraic trick. The positive eigenfunction measures the component of u along the least costly spatial mode. Its associated eigenvalue is the minimum diffusion cost under the boundary constraint. The reaction must exceed that cost before a positive state can be sustained.

## Constructing a solution above the threshold

Now suppose lambda exceeds one. A small multiple of sine of x provides a positive subsolution. As long as the square of its amplitude is at most lambda minus one, the reaction at that function is large enough to dominate its negative second derivative.

For an upper bound, choose the constant square root of lambda. Its negative second derivative is zero; its reaction is also zero. At the boundary it stands above the required zero values. So it is a supersolution. With the lower amplitude chosen small enough, the two barriers are ordered.

The subsolution and supersolution theorem then provides a solution trapped between them. Because the lower barrier is positive in the interior, the solution is positive there. That proves sufficiency, not merely plausibility.

The construction works in a smooth, bounded, connected domain in higher dimensions too, with the first positive Dirichlet eigenfunction replacing sine of x. The threshold becomes the domain's principal Dirichlet eigenvalue. One still has to check regularity and the precise function spaces, but the organizing idea is the same.

We have now proved that lambda greater than the principal eigenvalue is both necessary and sufficient for a positive solution of this cubic reaction problem.

## A bound supplied by the maximum principle

Before discussing uniqueness, we can constrain how high the positive solution rises. It reaches a positive maximum at an interior point. There its second derivative is nonpositive, so its negative second derivative is nonnegative.

The equation therefore says that lambda times the maximum minus its cube is nonnegative. Dividing by the positive maximum gives the inequality that the square of the maximum is at most lambda. In other words, the entire solution stays below the constant square root of lambda.

This bound has a useful interpretation. The cubic term prevents unlimited local growth, and the maximum principle transfers that pointwise reaction balance to a global amplitude estimate. It agrees with the constant supersolution we just used. It is not a bound on derivatives, nor does it by itself prove anything about spatial uniqueness.

## Why two positive profiles cannot coexist here

Let us examine what is special about the cubic reaction. Divide the reaction by the displacement, assuming the displacement is positive. The result is lambda minus displacement squared. That quantity decreases strictly as the displacement increases.

This property makes a scaling comparison possible. Imagine two positive solutions, u and v. If we multiply v by a factor greater than one, the scaled function becomes a strict supersolution wherever v is positive. The reason is that the cubic reaction at the scaled function grows less than linearly with the scaling factor: the negative cubic term becomes three powers larger while the diffusion term scales with only one.

Choose a scale large enough that the scaled v lies above u. In one dimension, both positive solutions meet the zero endpoints with nonzero inward slopes, by the Hopf boundary lemma or directly from the ordinary differential equation. Their ratio is therefore controlled even near the endpoints. We can decrease the scale until the profiles first touch.

If the first touching scale were greater than one, the strict differential inequality for the scaled v and the strong comparison principle would forbid that interior contact. A boundary contact at a zero endpoint is handled by comparing the boundary slopes. Therefore u cannot exceed v anywhere. Interchanging u and v gives equality.

This outlines the uniqueness proof. Its essential hypothesis is that the reaction divided by the positive unknown is strictly decreasing, combined with a connected domain and appropriate comparison and boundary regularity. We should not turn this into a blanket claim that semilinear elliptic equations have unique positive solutions. For other reactions, the ratio may not decrease, and multiple positive branches can occur.

## Why the size of the domain matters

Now repeat the same model on an interval of length L rather than pi. The first eigenfunction is sine of pi x divided by L, and the first Dirichlet eigenvalue is pi squared divided by L squared.

The threshold for positive solutions becomes lambda greater than that eigenvalue. Make the interval narrower and the eigenvalue rises. The same growth parameter may support a positive state on a large interval but not on a small one. That is a concrete mathematical statement about the competition between diffusion and reaction.

One can picture the boundary as absorbing material. A narrow region places every interior point close to an absorbing end, so sustaining a positive profile requires stronger growth. This intuition is not a proof for arbitrary domains, but domain monotonicity of the principal Dirichlet eigenvalue makes the same qualitative conclusion rigorous under set inclusion.

The geometry enters the nonlinear existence problem through a linear spectral quantity. That is a recurring theme in elliptic equations and in the study of stability of their time-dependent counterparts.

## The positive branch near the threshold

What does the solution look like just above lambda equal to one? Since the nonzero state emerges from zero, we expect its amplitude to be small. Write it as a times sine of x, plus a correction involving higher harmonics.

Projecting the equation onto the first sine mode gives, to leading order, lambda minus one equals three quarters times the square of a. Therefore the leading amplitude is about the square root of four thirds times lambda minus one.

This is a square-root law, not a linear law. Doubling the distance past the threshold does not double the amplitude; near onset it multiplies the amplitude by the square root of two.

But the cubic nonlinearity produces a third harmonic. If we calculate one order further, the first correction to the profile is a cubed over thirty-two times sine of three x. The coefficient is small when a is small. The shape is very close to a pure sine wave near onset, but it is not exactly a pure sine wave.

These statements can be made rigorous with a local bifurcation calculation. The approximate amplitude and the higher-mode correction are not guesswork once we specify how a is defined: take a to be the first sine Fourier coefficient of u. Then the correction is orthogonal to sine of x, and a local implicit-function argument solves for it in terms of a.

There is an important distinction between the existence theorem and this expansion. The barrier method gives positive solutions for every lambda above the threshold. The local expansion tells us their shape for lambda close to the threshold. The first does not require the amplitude to be small. The second does.

## The role of the linearized problem

The same eigenvalue appears when we ask whether the zero state is stable for the reaction-diffusion evolution. A small perturbation in the first sine shape grows at rate lambda minus one. It decays below the threshold and grows above it. This does not automatically identify the stability of every nonlinear equilibrium, but it explains why the zero branch changes character exactly where the positive and negative branches emerge.

The system has a symmetry: if u is a solution, so is minus u. Therefore a positive branch has a mirror-image negative branch. At the threshold the three branches meet at the zero state. In a diagram of amplitude against the parameter, the resulting shape is the characteristic pitchfork of a symmetric bifurcation.

If we replace the cubic reaction with a different law, both the shape and the uniqueness statement can change. For example, if the reaction has several positive zeros, the existence of constant upper barriers may remain easy while uniqueness fails. If a parameter controls a source term rather than a linear growth rate, the zero solution might not exist for every parameter, and the branch diagram can turn back rather than split symmetrically.

Here is the main conclusion. The positive eigenfunction is not merely a handy trial function. It detects the exact threshold for positive equilibria. Sub- and supersolutions prove that the threshold is sufficient. The maximum principle bounds the resulting solution. A decreasing reaction-to-displacement ratio establishes uniqueness. And a small-amplitude expansion reveals how the nonzero profile emerges from zero. These are distinct tools, coordinated around the same model.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Exact threshold and maximum bound

For \(I=(0,\pi)\), let \(\phi_1=\sin x\) and \(\lambda_1=1\). A positive solution of \(-u''=\lambda u-u^3\), \(u|_{\partial I}=0\), satisfies
\[
(\lambda-1)\int_0^\pi u\phi_1\,dx=\int_0^\pi u^3\phi_1\,dx>0.
\]
Necessarily \(\lambda>1\). Conversely, for \(\lambda>1\), choose
\[
\underline u=\varepsilon\sin x,\quad
0<\varepsilon^2\le\lambda-1,
\qquad
\overline u=\sqrt\lambda.
\]
Then \(-\underline u''\le\lambda\underline u-\underline u^3\), while \(-\overline u''=0=\lambda\overline u-\overline u^3\), and \(\underline u\le\overline u\). Standard sub/supersolution theory yields \(0<\underline u\le u\le\overline u\) in the interior. If \(M=\max_Iu\) occurs at \(x_*\), then \(0\le-u''(x_*)=M(\lambda-M^2)\), hence \(M\le\sqrt\lambda\).

### Why the unique positive state is a special result

For \(s>0\), \(f(s)/s=\lambda-s^2\) strictly decreases. In a smooth bounded connected domain the standard scaling comparison argument gives uniqueness of positive Dirichlet solutions when \(f(s)/s\) is strictly decreasing in the appropriate solution range, with strong comparison and Hopf-type boundary control. On the interval the required regularity and boundary slopes follow from ODE theory. This **does not** establish uniqueness of all sign-changing solutions.

### General interval scaling

On \((0,L)\), \(\phi_1(x)=\sin(\pi x/L)\), \(\lambda_1=(\pi/L)^2\), and a positive cubic-reaction solution exists if and only if \(\lambda>\lambda_1\). For connected smooth higher-dimensional domains the analogous first-eigenfunction comparison works, subject to the usual regularity and solution-class hypotheses.

### The small-amplitude expansion, with a precise coefficient

Write \(u=a\sin x+w\), \(\int_0^\pi w\sin x\,dx=0\), and \(\mu=\lambda-1\). Let \(L_0=-d^2/dx^2-1\). The residual is
\[
F(\mu,u)=L_0u-\mu u+u^3.
\]
The first-mode equation implies \(\mu=\tfrac34a^2+O(a^4)\). The orthogonal equation at cubic order is
\[
L_0w=\tfrac14a^3\sin3x+O(a^5).
\]
Since \(L_0\sin3x=8\sin3x\),
\[
\boxed{u(x)=a\sin x+\frac{a^3}{32}\sin3x+O(a^5),
\qquad \lambda=1+\frac34a^2+O(a^4).}
\]
The remainder is meant in a sufficiently regular Dirichlet function-space norm along the local solution branch, not as an unconditional formula for arbitrary \(\lambda\). The 062000 companion constructs the underlying Lyapunov–Schmidt reduction.

### Exercises with answers

1. **Necessary condition.** Why is the first eigenfunction positive? **Answer:** its interior positivity lets the projected cubic integral have a strict sign.
2. **Maximum point.** Prove \(\|u\|_\infty\le\sqrt\lambda\). **Answer:** at an interior maximum, \(-u''\ge0\), so \(u(\lambda-u^2)\ge0\).
3. **Narrow domain.** What happens to the threshold if the interval length is halved? **Answer:** \(\lambda_1\) quadruples.
4. **Amplitude law.** If \(\lambda-1\) is multiplied by four, what happens to the leading amplitude? **Answer:** it doubles.
5. **Third mode.** Why is its coefficient \(1/32\)? **Answer:** the cubic forces \(\sin3x\) with amplitude \(a^3/4\) and the shifted eigenvalue is 8.
6. **Uniqueness scope.** Does the argument rule out sign-changing excited states? **Answer:** no; it establishes uniqueness only among positive solutions.

### Sources and further reading

- [Delgado and Suárez, positive-solution and principal-eigenvalue framework](https://d-nb.info/1328194299/34), existence and uniqueness for logistic-type elliptic equations; cubic calculations here are derived explicitly.
- [Jean-Pierre Puel, *Semilinear elliptic equations*](https://pantheon.ufrj.br/items/d094491a-14db-450f-8508-0298c1366e0c), eigenvalue and monotone-method foundations.
- [Michael G. Crandall and Paul H. Rabinowitz, *Bifurcation from simple eigenvalues*](https://doi.org/10.1016/0022-1236(71)90015-2), rigorous local bifurcation near the first eigenvalue.
- [Wikipedia: Eigenvalues and eigenfunctions](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors), background; library connections `multivariable-calculus:059000`, `060000`, `050000`.
