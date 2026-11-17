# Subsolutions and Supersolutions: Constructing a Nonlinear Solution Between Barriers

**Track:** Multivariable Calculus from First Principles. **Focus:** ordered barriers, the maximum principle, shifted monotone iteration, an exact first iterate, and the limits of the method.

<!-- BEGIN SPOKEN LECTURE -->

# Subsolutions and Supersolutions: Constructing a Nonlinear Solution Between Barriers

Imagine trying to solve a nonlinear boundary-value problem without knowing its answer. You may not be able to write the solution in closed form. But perhaps you can build one function that is definitely too small and another that is definitely too large. Can those two estimates do more than bound an unknown? Can they actually produce a solution?

For a broad class of semilinear elliptic problems, the answer is yes. The method is called the subsolution and supersolution method. Its power comes from the maximum principle, the same comparison tool we developed for linear elliptic equations. Its subtlety is that the nonlinear reaction need not increase with the unknown. If we blindly apply a linear comparison principle to a nonmonotone reaction, the argument breaks.

We will return to our model problem on the interval from zero to pi: negative u double prime equals lambda u minus u cubed, with zero endpoint values. This time fix lambda equal to two. We know, by an energy argument, that a positive solution exists. The goal here is to construct it by a completely different route.

## What counts as being below a solution?

A subsolution is a function whose negative second derivative is no greater than the reaction evaluated at that function. It must also lie below the prescribed boundary values. For our zero-Dirichlet problem that means the subsolution has boundary values at most zero. A supersolution reverses both inequalities: its negative second derivative is at least the reaction, and its boundary values are at least zero.

These conditions are not arbitrary. Suppose an ordinary solution lies above a subsolution at the boundary. If the nonlinearity behaved monotonically in the appropriate way, subtracting their equations and applying a maximum principle would keep the order throughout the interval. The barrier inequalities are designed so a comparison argument can run.

A subsolution need not itself be a genuine solution. Its residual may be strictly on one side of zero. Likewise a supersolution may fail the original differential equation by a large margin. That freedom is the useful part: simple trial functions can be barriers for a nonlinear solution we cannot explicitly calculate.

## Build an explicit lower barrier

The first Dirichlet eigenfunction is sine of x. Let our candidate lower barrier be one half times sine of x. It is zero at both endpoints and positive in between.

The negative second derivative of one half sine of x is again one half sine of x. The nonlinear reaction at that same function is twice the function minus its cube. The difference between the reaction and the negative second derivative is one half sine of x minus one eighth sine cubed of x.

Because sine of x lies between zero and one on the interval, that difference is nonnegative. In fact, it is strictly positive away from the endpoints. Our trial function is a subsolution. We did not guess the exact shape; we used a positive eigenfunction and selected a small enough amplitude to make the inequality go in the desired direction.

The same construction works for every lambda greater than one. A small multiple of sine of x satisfies the lower-barrier inequality whenever the square of its amplitude is no greater than lambda minus one. Here the eigenvalue threshold reappears, but now in a pointwise construction rather than an energy comparison.

## Build an upper barrier that ignores the boundary shape

For the supersolution, try something even simpler: a positive constant. Let that constant be the square root of two. Its second derivative vanishes. Its reaction equals twice that constant minus its cube, which also vanishes. So the differential inequality holds with equality.

At the endpoints the constant is positive while the prescribed solution value is zero, so it satisfies the required boundary inequality. It is a valid supersolution even though it does not satisfy the Dirichlet boundary condition exactly. This distinction is easy to miss. A supersolution must stand above the desired boundary data; it need not equal them.

The lower sine-shaped function stays below this constant everywhere. We now have an ordered pair of barriers: one strictly positive in the interior and zero at the ends, the other a horizontal ceiling. The theorem we want says there is at least one true solution between them.

## Why ordinary fixed-point iteration may fail

It is tempting to start with the lower barrier, solve a linear Poisson equation using the current guess on the right, and repeat. That would mean solving negative next-u double prime equals two times current-u minus current-u cubed.

The problem is that the reaction increases only up to a certain displacement and decreases after that. Its derivative is two minus three times the square of the displacement. At the upper barrier, that derivative is negative. Larger inputs can therefore produce smaller right-hand sides. There is no direct order-preserving argument for this naive iteration.

This is where the shifted operator enters. Add the same positive constant times u to both sides of the equation. We have not changed which functions solve it. But we can choose the constant so the modified right-hand side becomes increasing throughout the interval between the barriers.

Take the shift to be six. The new linear operator is negative second derivative plus six times the function. The modified reaction is eight times u minus u cubed. On inputs from zero to the square root of two, its derivative is eight minus three times the square of u, which stays at least two. Thus the modified reaction is increasing on exactly the range we will use.

## The actual iteration

Begin with our lower barrier. Given the current iterate, solve a linear boundary-value problem for the next one: negative next-u double prime plus six times next-u equals eight times current-u minus current-u cubed. Give the next iterate zero endpoint values.

Every step is a linear solve. The nonlinearity only appears in the known source term. The inverse of negative second derivative plus six preserves nonnegative order under zero Dirichlet data. Therefore, because our modified reaction is increasing, a larger current iterate produces a larger next iterate.

The first step lies above the subsolution. Why? Subtract the subsolution inequality from the equation defining the first iterate. The difference satisfies a linear equation with nonnegative forcing and nonnegative boundary data. The maximum principle says the difference cannot be negative.

The first step also lies below the supersolution. Compare the defining equation to the supersolution inequality, remembering that the supersolution is allowed to have larger boundary values. Applying the same linear maximum principle gives the upper bound.

By induction, each new iterate is at least as large as the previous one, and no iterate rises above the ceiling. We have built a monotone, pointwise bounded sequence of functions. That is a strong structural fact; it is much more useful than merely observing that a numerical iteration seems to settle down.

## An exact first step

We can even compute the first iterate without a numerical solver. The starting function is one half sine of x. Cubing it produces a first harmonic and a third harmonic. The shifted linear operator acts diagonally on sine modes: sine of x is multiplied by one plus six, while sine of three x is multiplied by nine plus six.

Working through the coefficients, the first iterate is one hundred twenty-five over two hundred twenty-four times sine of x, plus one over four hundred eighty times sine of three x. The leading amplitude is about zero point five five eight, larger than the original one half. The third-harmonic correction is small but nonzero.

This exact calculation matters for two reasons. It verifies the direction of the first improvement, and it reminds us that the iteration is constructing a genuine function, not just updating a single amplitude. A one-mode approximation and a complete linear solve are different operations.

## Why the sequence converges to a solution

The monotone sequence has a pointwise limit between the barriers. But pointwise convergence alone does not allow us to pass two derivatives through the limit. We use the equation itself to gain regularity. The source terms are uniformly bounded because all iterates lie between zero and the fixed ceiling. In one dimension, the shifted Dirichlet problem then gives uniform second-derivative control, and hence enough compactness to extract convergence in a topology that preserves the weak equation.

The pointwise limit must agree with the limit of such a convergent subsequence. Passing to the limit in the linear equations yields the nonlinear equation. The lower barrier is strictly positive inside, so the resulting solution is not zero. This is an existence proof, and it is constructive: it provides a sequence of linear problems whose solutions approach a nonlinear equilibrium.

A locally Lipschitz reaction is enough for a shifted monotone construction on a bounded interval of values. In more general domains or with rough coefficients, the function spaces and boundary regularity need to be adapted. The abstract idea remains the same, but it is not a theorem without hypotheses.

## Minimal solutions, uniqueness, and what is not promised

Starting from the lower barrier and iterating upward selects the smallest solution inside the chosen ordered interval, provided the usual comparison and compactness hypotheses hold. Starting from the upper barrier and iterating downward can select the largest. These extremes need not coincide for an arbitrary nonlinear reaction. There may be several distinct solutions trapped between the same barriers.

For our cubic reaction, the positive solution is in fact unique. That follows from additional information: the reaction divided by the displacement, for positive displacement, decreases strictly as the displacement grows. A comparison argument exploiting this ratio rules out two distinct positive solutions. It is not a consequence of monotone iteration alone.

Nor does the method automatically promise a rapid numerical rate. A monotone sequence can converge slowly, especially near a turning point or when the linearized problem is close to singular. And the method will not find a sign-changing state if we deliberately trap it between a positive lower barrier and a positive ceiling.

We have converted a nonlinear existence question into a controlled sequence of linear elliptic solves. The starting barriers certify an interval of possible functions. A shift repairs the loss of monotonicity in the reaction. The maximum principle protects the order. Compactness turns the bounded sequence into a true solution. This is one of the most practical connections between linear elliptic theory and nonlinear PDEs: the old comparison principle becomes the engine for constructing new equilibria.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Ordered sub- and supersolutions

For \(-u''=f(u)\) on \((0,\pi)\), \(u|_{\partial I}=0\), define \(\underline u\) and \(\overline u\) by
\[
-\underline u''\le f(\underline u),\quad \underline u|_{\partial I}\le0;
\qquad
-\overline u''\ge f(\overline u),\quad \overline u|_{\partial I}\ge0.
\]
Here \(f(s)=2s-s^3\), \(\underline u=\frac12\sin x\), and \(\overline u=\sqrt2\). Then
\[
f(\underline u)+\underline u''=\frac12\sin x-\frac18\sin^3x\ge\frac38\sin x\ge0,
\qquad
f(\overline u)=0=-\overline u''.
\]
They are ordered, \(0\le\underline u\le\overline u\).

### Shifted order-preserving iteration

Choose \(K=6\), so \(g(s)=f(s)+Ks=8s-s^3\) obeys
\[
g'(s)=8-3s^2\ge2\quad(0\le s\le\sqrt2).
\]
Put \(u_0=\underline u\), and for \(n\ge0\) solve
\[
-u_{n+1}''+6u_{n+1}=g(u_n),\qquad u_{n+1}(0)=u_{n+1}(\pi)=0.
\]
By the maximum principle for \(L_K=-\frac{d^2}{dx^2}+6\), one obtains
\[
\underline u=u_0\le u_1\le\cdots\le\overline u.
\]
For the base comparison, \(L_K(u_1-u_0)=g(u_0)-L_Ku_0=f(u_0)+u_0''\ge0\). For the ceiling, \(L_K(\overline u-u_1)=L_K\overline u-g(u_0)\ge g(\overline u)-g(u_0)\ge0\) and the boundary difference is positive. The induction repeats with monotonicity of \(g\).

Since \(\|g(u_n)\|_\infty\) is uniformly bounded, standard one-dimensional Dirichlet elliptic estimates bound \(u_n\) in \(W^{2,p}\) for finite \(p\), yielding compactness in \(C^1\) for suitable \(p>1\). A subsequential limit solves \(L_Ku=g(u)\); monotonicity forces every such subsequence to have the same pointwise limit.

### Exact first iterate

Using \(\sin^3x=(3\sin x-\sin3x)/4\),
\[
g(u_0)=4\sin x-\tfrac18\sin^3x
=\tfrac{125}{32}\sin x+\tfrac1{32}\sin3x.
\]
Since \(L_K\sin(nx)=(n^2+6)\sin(nx)\),
\[
\boxed{u_1(x)=\frac{125}{224}\sin x+\frac1{480}\sin3x.}
\]
This is an exact linear iterate, not an exact solution of the original cubic equation.

### Where the proof can fail

- If \(\underline u>\overline u\) somewhere, the ordered interval is empty.
- If \(f\) is not locally one-sided Lipschitz on the bounded order interval, a constant shift need not make \(f(s)+Ks\) increasing.
- If the linear inverse fails to preserve order, the induction cannot be justified by the maximum principle.
- A monotone limit needs compactness or other control to pass the differential equation to the limit.
- Order iteration detects solutions within the selected interval, not every sign-changing or disconnected solution branch.

### Exercises with answers

1. **Shift choice.** Could \(K=4\) work? **Answer:** yes, \(f'(s)+4=6-3s^2\ge0\) on \([0,\sqrt2]\).
2. **Subsolution range.** For general \(\lambda>1\), when does \(\varepsilon\sin x\) work? **Answer:** if \(0<\varepsilon^2\le\lambda-1\).
3. **Boundary order.** Why can the constant supersolution be nonzero at the endpoints? **Answer:** the supersolution boundary condition is an inequality, \(\overline u\ge0\).
4. **Derivative of reaction.** Why is naive Picard iteration not necessarily monotone? **Answer:** \(f'(s)=2-3s^2\) becomes negative on part of the barrier interval.
5. **Fourier coefficients.** Check the third-harmonic coefficient of \(u_1\). **Answer:** \((1/32)/(9+6)=1/480\).
6. **Uniqueness.** Does existence of monotone iterates alone imply a unique solution? **Answer:** no; the order interval may contain multiple solutions.

### Sources and further reading

- [Marcelo Montenegro and Augusto C. Ponce, *The Sub-Supersolution Method for Weak Solutions*](https://perso.uclouvain.be/augusto.ponce/18.pdf), classical method, weak extensions, and the regularity requirements of the iteration proof.
- [Holst and Meier, *Generalized Solutions to Semilinear Elliptic PDE*, Section 4](https://ccom.ucsd.edu/~mholst/pubs/dist/HoMe10a.pdf), shifted operator and order-preserving iteration proof.
- [Semilinear elliptic equation lecture notes, monotone methods](https://citeseerx.ist.psu.edu/document?doi=907cfddb6f918bd668593a494a021372d8bf65d3&repid=rep1&type=pdf), sub- and supersolutions and minimal/maximal solutions.
- [Wikipedia: Maximum principle](https://en.wikipedia.org/wiki/Maximum_principle), comparison principle background; library lectures `multivariable-calculus:047000`, `059000`.
