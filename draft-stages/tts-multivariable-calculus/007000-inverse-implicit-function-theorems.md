# 007000 — Inverse and Implicit Functions: Solving Nearby Equations

**Track:** Multivariable Calculus from First Principles. **Background:** Jacobians, matrix inverses, chain rule. **Question:** when can we solve equations for variables without an explicit formula?

<!-- BEGIN SPOKEN LECTURE -->

# Inverse and Implicit Functions: Solving Nearby Equations

The algebra of two equations in two unknowns is straightforward when the equations are linear. For nonlinear equations, even writing down an explicit inverse can be impossible. Yet we often need only a local answer: if the data change slightly, is there one nearby solution, and how quickly does that solution move? The inverse and implicit function theorems answer this question through the derivative matrix.

Begin with an invertible linear map. If u equals x plus y and v equals x minus y, the inverse gives x as one half of u plus v and y as one half of u minus v. The Jacobian has rows one comma one and one comma minus one. Its determinant is minus two, which is nonzero. A small change in the output determines a unique small change in the input.

A nonlinear map is approximately linear near a differentiable point. If its derivative matrix is invertible there, the inverse function theorem says the map is locally invertible, provided the derivative behaves continuously in a neighborhood. The inverse is differentiable, and its derivative is the matrix inverse of the original Jacobian, evaluated at the corresponding point.

## A map that has local but not global inverses

Consider the transformation from polar-like coordinates s and t to plane coordinates x equals exponential s times cosine t, and y equals exponential s times sine t. Its Jacobian determinant is exponential of twice s, always positive. Therefore near every input point, a small output change can be inverted uniquely. But t and t plus two pi produce the same output. There is no one-to-one global inverse on the entire s–t plane. Nonzero determinant guarantees local invertibility, not global uniqueness.

This distinction is important whenever coordinates wrap around a circle, overlap, or omit a point. A perfectly valid local coordinate chart may fail to cover a whole manifold or may repeat points beyond its chosen domain.

## Solve one variable as a function of another

Now consider the unit circle, whose equation is x squared plus y squared equals one. We can write this as F of x and y equals zero, where F is x squared plus y squared minus one. Near the point zero comma one, there is a unique branch of the circle with y near one. It can be described as y as a smooth function of x. We could solve explicitly using the positive square root of one minus x squared, but the implicit function theorem works without such a formula.

The key condition is that the partial derivative of F with respect to the variable we want to solve for, here y, is nonzero. At zero comma one, that derivative is two. We can therefore differentiate the equation F of x comma y of x equals zero. The chain rule gives F sub x plus F sub y times y prime equals zero. Solve to obtain y prime equals negative F sub x divided by F sub y. For the circle this becomes negative x divided by y. At the top of the circle the derivative is zero, so the tangent is horizontal.

At the point one comma zero, F sub y is zero. We cannot solve locally for y as a smooth function of x near that point in the same way. The circle has a vertical tangent; nearby values of x less than one correspond to two values of y, one positive and one negative. Yet F sub x is nonzero there, so we can instead solve for x as a smooth function of y. The failure concerns the chosen variable, not smoothness of the circle itself.

## General systems and the block Jacobian

For several equations F of x comma y equals zero, where y represents the unknowns we wish to solve and x represents parameters, the derivative with respect to y is a square matrix. If that matrix is invertible, the implicit function theorem gives a local solution y of x. Its derivative is minus the inverse of the y-Jacobian times the x-Jacobian. The dimensions make the formula readable: it converts a change of parameters into the corresponding change of the solved variables.

This provides a sensitivity calculation even if no explicit nonlinear solution formula is available. A parameter may be a temperature, a measurement or an applied force. The theorem tells us how the nearby equilibrium responds, as long as the relevant linearization is invertible.

## Why invertibility matters

If the linearized map loses rank, nearby solutions can branch, disappear, or change multiplicity. The scalar equation y squared equals x illustrates the issue at the origin. For x positive it has two nearby values of y. For x negative it has no real solution. The derivative with respect to y is zero at the origin. A smooth unique branch through that point is not guaranteed.

Failure of the hypothesis does not prove that a solution is impossible. It means the theorem cannot certify a smooth local inverse. One must analyze the particular equation by other means.

The inverse and implicit function theorems connect linear algebra to nonlinear geometry. They explain why invertible Jacobians permit local coordinates, why regular level sets are smooth, and why a constraint can often be solved for some variables without writing them down explicitly.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Inverse function theorem.** If \(F:U\subset\mathbb R^n\to\mathbb R^n\) is \(C^1\) and \(\det DF(a)\ne0\), there exist neighborhoods of \(a\) and \(F(a)\) on which \(F\) is a \(C^1\) diffeomorphism, with
\[
D(F^{-1})(F(a))=[DF(a)]^{-1}.
\]
**Implicit function theorem.** If \(F:U\subset\mathbb R^p\times\mathbb R^q\to\mathbb R^q\) is \(C^1\), \(F(a,b)=0\), and \(D_yF(a,b)\) is invertible, then locally \(y=\phi(x)\) and
\[
D\phi(x)=-[D_yF(x,\phi(x))]^{-1}D_xF(x,\phi(x)).
\]
On \(x^2+y^2=1\) with \(y\ne0\), \(dy/dx=-x/y\). The map \((s,t)\mapsto(e^s\cos t,e^s\sin t)\) has determinant \(e^{2s}\) but is globally periodic in \(t\).

### Exercises with answers

1. For \(F(x,y)=(x+y,x-y)\), compute \(DF^{-1}\). **Answer:** \(\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\).
2. Implicitly differentiate \(x^2+xy+y^2=3\) where \(x+2y\ne0\). **Answer:** \(y'=-(2x+y)/(x+2y)\).
3. At \((1,0)\) on the circle, which variable is locally a function of the other? **Answer:** \(x\) is locally a smooth function of \(y\).
4. Does nonzero Jacobian determinant imply global injectivity? **Answer:** no; the exponential polar map repeats after one full turn.

### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), implicit functions.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), derivatives and applications.
- [Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem); [Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem).
