# Solving Equations Locally: Inverse and Implicit Functions

<!-- BEGIN SPOKEN LECTURE -->

# Solving Equations Locally: Inverse and Implicit Functions

A formula can define a quantity without telling us how to compute that quantity explicitly. A circle is defined by an equation in x and y; it is not defined first as a formula for y in terms of x. A calibration procedure may specify two target readings but require us to find two hidden controls. An equilibrium model may say that two forces must balance, without providing a closed formula for the resulting configuration.

The inverse and implicit function theorems answer a local question: when the targets change a little, can we solve for the unknowns nearby, and how fast does that solution change? Their central condition concerns a derivative matrix, but it helps to begin with a system we can solve by hand.

## Two equations and two unknowns

Fix a real parameter x. We seek two unknowns, y and z, satisfying the following equations. The first is y plus x times z equals one. The second is z plus x times y equals two.

At x equal to zero, the equations become y equals one and z equals two. Now let x move slightly away from zero. Because y appears in both equations and z appears in both, we cannot simply read off their values. But we can eliminate one unknown.

From the first equation, y equals one minus x times z. Substitute that into the second. We obtain z times one minus x squared equals two minus x. Therefore z equals two minus x divided by one minus x squared. Substituting back gives y equals one minus two x divided by one minus x squared.

Check a nonzero value. At x equal to one fifth, the first unknown is five eighths and the second is fifteen eighths. Indeed, five eighths plus one fifth of fifteen eighths equals one; fifteen eighths plus one fifth of five eighths equals two. The formulas are not just formal symbols. They predict the actual adjustment of the unknowns.

Notice what is happening near x equals zero. As x increases slightly, y falls at a rate close to two units per unit x and z falls at a rate close to one. We can find those derivatives without ever solving the system explicitly, and that is the point of the implicit function theorem.

## Differentiate the equations, not the solution formula

Differentiate the first defining equation with respect to x, remembering that both y and z depend on x. The derivative of y is y prime. The derivative of x times z is z plus x times z prime. So the first differentiated equation says y prime plus x times z prime equals minus z.

Likewise, differentiating the second equation gives x times y prime plus z prime equals minus y.

At x equal to zero, we already know y equals one and z equals two. The differentiated equations simplify immediately: y prime equals minus two; z prime equals minus one. We have recovered the sensitivity of both unknowns without differentiating the rational formulas found earlier.

This is more than a convenient trick. We can treat the two left-hand sides minus their target values as a vector-valued function of the parameter x and unknown vector consisting of y and z. Differentiate that function with respect to the unknowns. The resulting matrix has rows one, x and x, one. At x equals zero it is the identity matrix. Since it is invertible, small changes in the equations can be offset by a unique small change in the unknowns.

At a general x, the determinant is one minus x squared. As x gets close to one, the matrix becomes nearly singular. The solution may respond strongly to a small change in the parameter or target readings. This is a direct bridge from derivatives to conditioning.

At x equal to one, the equations are inconsistent: they demand y plus z equals one and also y plus z equals two. The obstacle is visible in the algebra. But the theorem does not say that every singular derivative produces inconsistency. It only tells us that the usual local guarantee no longer follows from the invertible-matrix argument.

## The implicit function theorem in words

Here is the general setup. A set of equations depends on an external parameter x and an unknown vector y. Assume the equations are continuously differentiable near a known solution. Form the square matrix of partial derivatives with respect to the unknown vector, not with respect to every input at once. If that matrix is invertible at the known solution, then in some neighborhood there is exactly one nearby unknown vector solving the equations for each nearby parameter value. The unknown vector depends continuously differentiably on the parameter.

The formula for its derivative is obtained exactly as we did above: differentiate the equation, move the direct parameter-change term to the other side, then solve a linear system in the unknown derivative. The negative inverse of the unknown-variable Jacobian, multiplied by the parameter-variable Jacobian, gives the sensitivity.

Be careful about two qualifications. The conclusion is local: it promises a solution near the one we started with, not that the equations have just one solution anywhere in the universe. And the square matrix that must be invertible is the part associated with the unknown variables we intend to solve for. If there are three equations for two unknowns, or if we declare the wrong variables unknown, the theorem as stated no longer applies.

## A local inverse is not a global inverse

Consider a map that turns two real numbers into a point in the plane. Let the first input control a radial scale by taking the exponential of that input. Let the second choose an angle. The output is the radial scale times cosine of the angle, together with the same radial scale times sine of the angle.

At the input zero, zero, the output is one, zero. A tiny increase in the first input moves the output right; a tiny increase in the second moves it upward. The derivative matrix at that point is the identity. More generally, its determinant is the exponential of twice the first input, which is never zero. The inverse function theorem guarantees an inverse around each input point.

Yet the full map has no global inverse. Angles separated by a full turn produce exactly the same output. An invertible derivative at every point does not eliminate distant repetitions of the map. The theorem grants an inverse on a sufficiently small neighborhood, where the angle can be chosen consistently. It does not make a periodic coordinate system one-to-one over all real angles.

This distinction matters for coordinate changes. Latitude and longitude may describe a patch of the Earth perfectly well without giving globally unique, nonsingular coordinates over the entire sphere. Local solvability is often exactly what we need.

## Singular does not mean impossible

It is tempting to reverse the inverse function theorem and say that a zero derivative means a function cannot be inverted. That is false.

On the real line, the map sending x to x cubed is one-to-one and has a continuous inverse, the cube-root function. Its derivative at zero is zero. What fails is the conclusion that the inverse has a finite, continuously varying derivative near the corresponding output. The cube root changes very quickly near zero.

Compare the map sending x to x squared. Its derivative at zero is also zero, but now values on opposite sides of zero are identical, so there is no two-sided local inverse. The same derivative condition fails, with different outcomes. The theorem gives a sufficient condition for a smooth inverse, not an if-and-only-if classification of invertibility.

In several dimensions, a singular Jacobian can indicate a fold, a branch crossing, a cusp, a loss of uniqueness, or simply a choice of coordinates that breaks down while the geometric object remains well behaved. Additional analysis is required to distinguish those cases.

## A numerical solver's viewpoint

We rarely get such convenient elimination formulas for real scientific systems. Suppose a nonlinear system is currently almost satisfied at a trial vector. A Newton step asks for an adjustment whose derivative-predicted change cancels the remaining residual. This produces a linear system with the Jacobian as its coefficient matrix.

When the Jacobian is well conditioned, a small residual leads to a modest correction, at least locally. When it is nearly singular, small changes in measurements or arithmetic can create large changes in the correction. A numerical solver might then need damping, a different parameterization, or information about which solutions are physically meaningful.

The implicit function theorem and Newton's method are two views of that same local linear algebra. The theorem says when a nearby solution exists and changes smoothly; Newton's method attempts to find that solution by repeatedly solving local linear models.

Return to our two-equation example. The original unknowns changed in response to x, but we could also change the two right-hand-side targets. The same invertible matrix predicts how the solution responds to those independent data changes. When the determinant approaches zero, the sensitivity increases. There is no magic dividing line between pure calculus, numerical analysis, and inverse problems; they are examining the same derivative from different perspectives.

To use this material reliably, always ask: What is known? What is being solved for? At which solution is the derivative evaluated? Which Jacobian block is supposed to be invertible? And is the conclusion local or global? Answer those questions before attempting a formula, and the implicit-function calculation becomes much less mysterious.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Worked two-by-two implicit system

Let
\[
H(x,y,z)=\binom{y+xz-1}{z+xy-2}=0,\qquad H(0,1,2)=0.
\]
The unknown block and parameter column are
\[
D_{(y,z)}H=\begin{pmatrix}1&x\\x&1\end{pmatrix},\qquad
D_xH=\binom{z}{y},\qquad \det D_{(y,z)}H=1-x^2.
\]
For \(|x|<1\), the implicit function theorem applies near the solution. Direct elimination gives
\[
y(x)=\frac{1-2x}{1-x^2},\qquad z(x)=\frac{2-x}{1-x^2}.
\]
At \(x=1/5\), \((y,z)=(5/8,15/8)\). Differentiating the system:
\[
\begin{pmatrix}1&x\\x&1\end{pmatrix}\binom{y'}{z'}=-\binom{z}{y},
\qquad (y'(0),z'(0))=(-2,-1).
\]
For general targets \(a,b\), replace \(1,2\) by \(a,b\), and obtain
\[
\binom{y}{z}=\frac{1}{1-x^2}\begin{pmatrix}1&-x\\-x&1\end{pmatrix}\binom{a}{b}.
\]
The solution's sensitivity to \((a,b)\) grows as \(|x|\to1\), although the precise behavior depends on the target direction.

### The implicit and inverse function theorems

Let \(H:\mathbb R^{k+m}\supset U\to\mathbb R^m\) be \(C^1\), with \(H(x_0,y_0)=0\) and \(D_yH(x_0,y_0)\) invertible. Then for \(x\) close to \(x_0\) there is a unique \(C^1\) function \(y=g(x)\) near \(y_0\) with \(H(x,g(x))=0\) and
\[
Dg(x)=-[D_yH(x,g(x))]^{-1}D_xH(x,g(x)).
\]
The inverse function theorem is the case of \(H(x,y)=F(y)-x\) for a \(C^1\) map \(F:\mathbb R^m\to\mathbb R^m\) with invertible \(DF(y_0)\).

### Local but not global inversion

For \(F(s,t)=e^s(\cos t,\sin t)\),
\[
DF(s,t)=e^s\begin{pmatrix}\cos t&-\sin t\\\sin t&\cos t\end{pmatrix},\qquad
\det DF(s,t)=e^{2s}>0.
\]
Nevertheless \(F(s,t)=F(s,t+2\pi)\). A local inverse exists about each point, while a globally single-valued angle does not.

The real functions \(x^3\) and \(x^2\) both have derivative zero at zero. The first is globally injective but its inverse \(x^{1/3}\) is not differentiable at zero; the second is not locally injective across zero.

### Exercises with answers

1. **Differentiate the given system.** Verify \(y'(0)=-2,z'(0)=-1\) without using elimination. **Answer:** evaluate \(D_yH\,(y',z')=-D_xH\) at \((0,1,2)\), giving the identity times the derivative column equal to \((-2,-1)\).
2. **Two target perturbations.** At \(x=1/2\), compute the change in \((y,z)\) when the first right-hand side increases by \(\epsilon\) and the second stays fixed. **Answer:** \(\delta(y,z)=(4\epsilon/3,-2\epsilon/3)\) exactly, because the equations are linear in the unknowns.
3. **Conditioning.** Why is the determinant small near \(x=1\)? **Answer:** the two rows of the unknown-variable Jacobian become almost equal; a difference in the two target readings becomes hard to satisfy without large changes in the solution.
4. **Periodic coordinates.** Give two distinct inputs with the same output under \(F(s,t)\). **Answer:** \((0,0)\) and \((0,2\pi)\) both map to \((1,0)\).
5. **Wrong converse.** Does \(f'(0)=0\) imply \(f\) is not locally invertible? **Answer:** No; \(f(x)=x^3\) is one-to-one, but its inverse is not differentiable at zero.

### Sources and further reading

- [OpenStax, *Calculus Volume 3*, §4.5](https://openstax.org/books/calculus-volume-3/pages/4-5-the-chain-rule), elementary implicit differentiation via the chain rule.
- [MIT OpenCourseWare 18.02SC](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), local invertibility and multivariable computations.
- [Wikipedia: Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem), standard hypotheses and derivative formula.
- [Wikipedia: Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem), precise local invertibility distinction.
- Related applied lecture: `multivariable-calculus:030000` builds on this formula for differentiable optimization.
