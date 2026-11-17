# Bifurcation and Continuation: Following Nonlinear Solutions Through Singular Jacobians

**Track:** Multivariable Calculus from First Principles. **Focus:** Lyapunov–Schmidt reduction, simple-eigenvalue bifurcation, pitchforks versus folds, stability, and pseudo-arclength continuation.

<!-- BEGIN SPOKEN LECTURE -->

# Bifurcation and Continuation: Following Nonlinear Solutions Through Singular Jacobians

Suppose we solve a nonlinear boundary-value problem for one value of a parameter. Then we change the parameter a little and solve again. We might expect the solution to change smoothly. Often it does. But sometimes a parameter crosses a threshold and new solutions appear. Sometimes two solutions collide and disappear. At those moments, the derivative of the nonlinear equation with respect to the unknown becomes singular, precisely where ordinary Newton methods and the implicit function theorem become least informative.

This is the problem of bifurcation. The word describes a change in the structure of the solution set, not merely a large change in one numerical solution. We will connect it to the eigenvalue methods, weak formulations, and nonlinear solvers developed throughout this course.

Use our familiar boundary-value problem on the interval from zero to pi. The equation says that negative u double prime equals lambda u minus u cubed, with zero endpoint values. Its zero solution exists for every lambda. That makes a horizontal or trivial branch in a parameter-versus-amplitude diagram.

At lambda equal to one, the linearized operator about zero acquires a one-dimensional kernel, spanned by sine of x. The central question is what the *full nonlinear equation* does near that loss of invertibility.

## What the implicit function theorem would say away from the threshold

Write the residual as an operator F applied to lambda and u. It consists of negative u double prime, minus lambda u, plus u cubed. Solutions are precisely the zeros of F.

Differentiate with respect to u. At a general solution, the linearized operator applied to a perturbation v is negative v double prime, minus lambda v, plus three times u squared times v. This is the Jacobian of an infinite-dimensional nonlinear system.

If this operator has a bounded inverse between the chosen function spaces, an implicit-function theorem gives a locally unique smooth continuation of u as lambda varies. In the finite-element approximation, this is the condition that the assembled Jacobian matrix is nonsingular. A Newton correction can then be computed by solving a linearized system.

At the zero solution, however, the Jacobian is negative second derivative minus lambda. When lambda reaches one, applying that operator to sine of x gives zero. It cannot have an inverse. The ordinary implicit-function theorem no longer answers whether there is a nontrivial solution nearby.

Do not conclude that every singular Jacobian automatically creates a new branch. Singularity is a necessary condition for many common local bifurcations, not a sufficient condition by itself. We must examine how the parameter and nonlinear terms interact with the null direction.

## Separate the dangerous mode from the safe modes

Near lambda equal to one, write u as a times sine of x plus a remainder w that is orthogonal to sine of x. Here a is not a vague amplitude; it is the first Fourier sine coefficient, with a normalization chosen to make the decomposition unique.

On the space perpendicular to sine of x, negative second derivative minus one has a bounded inverse. Every higher sine mode has eigenvalue n squared minus one, and the smallest of these is three. So the part of the equation perpendicular to the first mode can be solved for w by the implicit function theorem, even though the full operator is singular.

This is the key move of Lyapunov–Schmidt reduction. We do not try to invert the singular operator on its whole domain. We solve in the complementary directions, then retain one scalar equation along the null direction.

The nonlinearity generates a third harmonic. The leading correction is a cubed divided by thirty-two times sine of three x. To obtain that coefficient, cube the first sine mode; its third-harmonic term has coefficient minus one quarter. The shifted linear operator multiplies sine of three x by eight. The correction that cancels the third-harmonic residual therefore has coefficient positive one thirty-second.

The surviving scalar equation, to lowest nontrivial order, says: one minus lambda times a, plus three quarters a cubed, equals zero. The trivial solution a equal to zero persists. A nonzero small solution requires lambda minus one to be approximately three quarters times a squared.

Thus the small solution amplitude grows like the square root of lambda minus one. There are two mirror-image branches, positive and negative, because the equation is unchanged under replacing u by minus u and then changing the overall sign. Together with the zero branch, they form a symmetric pitchfork.

## What makes the branch theorem rigorous?

The formal calculation predicts the branch, but we also want a theorem saying a true branch exists. One classical result is the Crandall–Rabinowitz theorem on bifurcation from a simple eigenvalue.

Its central conditions include a one-dimensional kernel of the linearization, a range of codimension one, and a transversality condition: the mixed derivative with respect to the parameter and the unknown, applied to the kernel vector, must point outside the range of the linearization.

For our model, the mixed derivative sends sine of x to negative sine of x. The range of the linearization at lambda equal to one consists of functions orthogonal to sine of x. Negative sine of x is therefore outside that range. The transversality condition holds.

With suitable smooth function spaces, the theorem gives a true local curve of nontrivial solutions meeting the trivial branch. The Lyapunov–Schmidt calculation then determines the first nonzero terms of that curve. The theorem and the expansion play different roles: one guarantees the curve's existence; the other explains its local shape.

There is another distinction worth guarding. The symmetry of our cubic equation makes the leading parameter change quadratic in the branch amplitude. A different nonlinearity might yield a branch with a linear parameter change instead. A simple eigenvalue crossing does not, by itself, guarantee a pitchfork.

## A fold is different from a pitchfork

Consider a much smaller nonlinear equation: a squared equals lambda. It has two solutions when lambda is positive, one at zero, and none when lambda is negative. At the origin, the two nonzero-looking curves turn around. There is no trivial solution branch continuing through all lambda values, so this is a fold, also called a saddle-node, rather than a pitchfork.

The derivative of a with respect to lambda equals one divided by two a. As a approaches zero, that derivative becomes unbounded. Trying to represent the solution as a single-valued differentiable function of lambda fails at the turning point. But if we describe the entire solution curve using a as the parameter, the curve is perfectly smooth: lambda equals a squared.

Nonlinear elliptic equations can exhibit folds too. Whether they do depends on the reaction law, geometry, and parameterization. One must not infer a fold for every semilinear equation just because one has seen a branch diagram in a textbook.

A useful finite-dimensional example has residual a cubed minus a plus lambda. Solving for lambda gives a minus a cubed. This curve has two turning points, where one minus three a squared equals zero. At those points, Newton's method for a fixed lambda encounters a zero derivative. Yet the solution curve itself remains smooth in the plane of a and lambda.

## Why numerical continuation changes the problem

Ordinary parameter continuation chooses lambda, solves for u, increases lambda, and repeats. It works when the solution can be expressed smoothly as a function of lambda. At a fold it can skip a branch or fail outright.

Pseudo-arclength continuation treats both u and lambda as unknowns. It adds one extra equation requiring the new pair to lie near a predicted point along the tangent to the existing solution curve. Instead of solving only the singular Jacobian with respect to u, it solves an augmented system with one extra column for the parameter derivative and one extra row for the tangent condition.

At a simple fold, this bordered matrix can remain invertible even though the original Jacobian is singular. In the scalar example, when the derivative with respect to a is zero, the derivative with respect to lambda is one. The tangent constraint supplies the missing direction. The two equations together still identify a local correction.

This does not make every singularity harmless. At a branch point, multiple tangents may meet, and a continuation algorithm needs branch switching or an additional strategy. For complicated PDE discretizations, tracking eigenvalues of the Jacobian, choosing step sizes, and controlling discretization error matter as much as the formal augmented equation.

## Stability is a related, but separate, question

A stationary branch may be stable or unstable for the associated time-dependent reaction-diffusion equation. Let u evolve by its second derivative plus lambda u minus u cubed. Linearize that evolution around a steady state. The resulting growth operator is the negative of the stationary Jacobian.

At zero, the first-mode growth rate is lambda minus one. So zero loses linear stability as lambda crosses one upward. Along the small positive and negative branches, the restoring cubic term changes the linearized operator. The critical stationary eigenvalue becomes positive, to leading order twice lambda minus one. Equivalently, the corresponding evolution growth rate is negative. Thus the new branches are linearly stable near onset for this gradient-flow model, while zero is unstable above onset.

The sign convention is important. A positive eigenvalue of the stationary energy Hessian is a stabilizing direction for negative-gradient evolution; the same sign would mean something different if we were speaking about the evolution operator itself. We also need to keep in mind that a statement about linear stability is not automatically a theorem of global nonlinear attraction.

## What the geometry of solutions tells us

We now have three complementary views of the same phenomenon. The energy landscape says a nonzero state becomes favorable past the first eigenvalue. The subsolution method constructs a positive equilibrium for every parameter above the threshold. Bifurcation theory resolves the local geometry of the solution set near the point where ordinary invertibility fails.

There is a numerical lesson too. A failed Newton solve may indicate bad scaling, a poor initial guess, or a genuine loss of invertibility. Those possibilities should not be confused. Inspecting a linearized eigenvalue and changing the continuation parameter can reveal a legitimate solution branch rather than simply hiding an error with more damping.

Semilinear elliptic equations are an entry point to a larger theory of nonlinear partial differential equations. Many new questions follow: when do solutions concentrate, how does a critical Sobolev exponent change compactness, and when do multiple branches carry different stability? But the essential bridge is already here. The linear elliptic operator supplies the spectrum, comparison principle, and inverse on stable modes. Nonlinear terms determine which branches exist and how they bend. Both parts are indispensable.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Function spaces and linearization

Let \(X=H^2(0,\pi)\cap H_0^1(0,\pi)\), \(Y=L^2(0,\pi)\), and
\[
F(\lambda,u)=-u''-\lambda u+u^3:X\to Y.
\]
In one dimension this is a smooth map. At \((1,0)\),
\[
D_uF(1,0)=L_0=-\frac{d^2}{dx^2}-1,
\quad \ker L_0=\operatorname{span}\{\phi\},\quad\phi(x)=\sin x.
\]
As \(L_0\) is self-adjoint with compact resolvent, its range is the closed codimension-one space \(\phi^\perp\subset L^2\). The mixed derivative is \(D_{\lambda u}F(1,0)\phi=-\phi\notin\operatorname{ran}L_0\), so the simple-eigenvalue transversality condition is satisfied. The relevant Crandall–Rabinowitz theorem gives a smooth local nontrivial curve under the displayed regularity and Fredholm assumptions.

### Lyapunov–Schmidt expansion

Define \(P h=(\langle h,\phi\rangle/\langle\phi,\phi\rangle)\phi\), \(Q=I-P\), \(u=a\phi+w\), \(Pw=0\), and \(\mu=\lambda-1\). The complement equation
\[
Q\big(L_0w-\mu(a\phi+w)+(a\phi+w)^3\big)=0
\]
uniquely determines \(w=w(a,\mu)\) near zero because \(L_0\) is invertible on \(\phi^\perp\). Odd symmetry and the structure imply \(w=O(a^3)\) along the branch. Expanding,
\[
\begin{aligned}
0&=P\big(-\mu a\phi+a^3\phi^3\big)+O(a^5)\\
 &=\big(-\mu a+\tfrac34a^3\big)\phi+O(a^5),\\
w&=\tfrac{a^3}{32}\sin3x+O(a^5),\\
\mu&=\tfrac34a^2+O(a^4).
\end{aligned}
\]
This yields a **true local pitchfork**, not an exact one-mode solution.

### Stability to leading order

The stationary Hessian is \(D_uF(\lambda,u_*)=-d^2/dx^2-\lambda+3u_*^2\). On the small nonzero branch,
\[
\frac{\langle\phi,D_uF(\lambda,u_*)\phi\rangle}{\|\phi\|_2^2}
=1-\lambda+\frac94a^2+O(a^4)
=\frac32a^2+O(a^4)
=2(\lambda-1)+O((\lambda-1)^2).
\]
The actual small eigenvalue has the same leading term by perturbation theory; all other stationary eigenvalues remain positive near \(\lambda=1\). For the gradient evolution \(u_t=-F(\lambda,u)\), the nonzero small branches are linearly stable and zero is unstable for \(\lambda>1\) near onset.

### Fold and pseudo-arclength examples

For \(G(a,\lambda)=a^2-\lambda\), the solution set is \(\lambda=a^2\): a fold at \((0,0)\), not a pitchfork. Parameter differentiation gives \(da/d\lambda=1/(2a)\) on nonzero branches, singular at the fold.

For \(H(a,\lambda)=a^3-a+\lambda\), folds occur at
\[
a=\pm\frac1{\sqrt3},\qquad \lambda=a-a^3=\pm\frac2{3\sqrt3}.
\]
At a predictor \((a_p,\lambda_p)\), an arclength corrector solves
\[
\begin{bmatrix}H_a&H_\lambda\\t_a&t_\lambda\end{bmatrix}
\begin{bmatrix}\delta a\\\delta\lambda\end{bmatrix}
=-\begin{bmatrix}H(a,\lambda)\\t_a(a-a_p)+t_\lambda(\lambda-\lambda_p)\end{bmatrix}.
\]
At a simple fold \(H_a=0\), \(H_\lambda=1\), and the tangent has \(t_a\ne0\), so this bordered matrix has nonzero determinant. This justifies continuation through the **simple fold**, not arbitrary multiple-kernel singularities.

### Exercises with answers

1. **Kernel.** Why does \(L_0\sin x=0\)? **Answer:** \(-\sin''x-\sin x=\sin x-\sin x=0\).
2. **Range.** Why is \(-\sin x\) outside \(\operatorname{ran}L_0\)? **Answer:** the self-adjoint range is orthogonal to \(\ker L_0\), whereas \(-\sin x\) is not.
3. **Coefficient.** Confirm the leading amplitude relation. **Answer:** projection of \(\sin^3x\) onto \(\sin x\) has coefficient \(3/4\).
4. **Fold versus pitchfork.** Is \(a^2-\lambda=0\) a pitchfork? **Answer:** no; no trivial branch exists for all \(\lambda\).
5. **Stability sign.** Which operator controls perturbations of \(u_t=-F(\lambda,u)\)? **Answer:** \(-D_uF(\lambda,u_*)\), not \(D_uF\).
6. **Continuation.** What restores nonsingularity at a simple fold? **Answer:** adding \(\lambda\) as an unknown and one tangent/arclength constraint.

### Sources and further reading

- [Michael G. Crandall and Paul H. Rabinowitz, *Bifurcation from Simple Eigenvalues*, Journal of Functional Analysis 8 (1971)](https://doi.org/10.1016/0022-1236(71)90015-2), original theorem and transversality conditions.
- [H. Uecker, *Continuation and Bifurcation in Nonlinear PDEs: Algorithms, Applications, and Experiments*](https://link.springer.com/article/10.1365/s13291-021-00241-5), computational branch tracking and pseudo-arclength continuation.
- [Christian Kuehn, *PDE Dynamics: An Introduction*, Chapter 5](https://epubs.siam.org/doi/10.1137/1.9781611975666.ch5), simple-eigenvalue bifurcation and stability context.
- [Wikipedia: Lyapunov–Schmidt reduction](https://en.wikipedia.org/wiki/Lyapunov%E2%80%93Schmidt_reduction), overview; [Wikipedia: Bifurcation theory](https://en.wikipedia.org/wiki/Bifurcation_theory), fold and pitchfork terminology.
- Library connections: `multivariable-calculus:021000`, `022000`, `029000`, `059000`, `061000`.
