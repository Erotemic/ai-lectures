# Nonlinear Least Squares: Residual Geometry and Gauss–Newton

**Track:** Multivariable Calculus from First Principles. **Focus:** distinguish the derivative of a residual vector from the derivative of its squared length; derive Gauss–Newton and identify the assumptions behind its success.

<!-- BEGIN SPOKEN LECTURE -->

# Nonlinear Least Squares: Residual Geometry and Gauss–Newton

Suppose you are trying to infer a physical parameter by matching a model to observations. Your model predicts an observable at each measurement location. The measurements do not agree exactly, perhaps because the instrument is noisy, perhaps because the model is incomplete. You have several disagreements, and several parameters to adjust. How should you turn those disagreements into one mathematical objective?

A natural choice is to square each difference and add. It creates a scalar objective, but its structure is richer than that of an arbitrary scalar function. That structure gives us the Gauss–Newton method, which is often a better starting point for fitting than forming the full Hessian and applying ordinary optimization Newton.

Our aim is to understand what calculation Gauss–Newton performs, why it can be fast, and why it can still fail. The distinctions will matter later when we discuss damping, singular values and uncertainty about the fitted parameters.

## From measurements to a residual vector

Let the parameter vector be called theta, with n components. Suppose there are m measurements. For observation number i, the model predicts a quantity depending on theta, and the observed quantity is fixed. Define residual number i as prediction minus observation. The sign convention could be reversed without changing the sum of squares, but consistency matters when constructing a Jacobian.

Collect the residuals into a vector r of theta. The vector has m components, even though theta has n. These are different spaces: parameter space, where we change the model, and measurement space, where we assess the consequences.

Our objective F of theta is one half the squared Euclidean length of the residual vector. The factor of one half is convenient because differentiating a square introduces a two. If errors have different known standard deviations, we should standardize or whiten them before taking squares. For now, imagine that the residuals are comparable in their units and accuracy.

What does a single parameter step accomplish? A small change p in parameter space produces, to first order, a change J times p in measurement space. Here J is the residual Jacobian: row i records how observation i's residual changes with each parameter. This rectangular matrix is not a Hessian. It maps a proposed parameter correction to predicted changes in the residuals.

The central approximation is therefore: the residual vector after the step is approximately the current residual vector plus J times p. Instead of asking the nonlinear model itself for an optimum, we can temporarily solve a linear least-squares problem: choose p that makes the length of this predicted residual vector as small as possible.

This distinction is a useful way to think about scientific fitting. A Jacobian does not say that a nonlinear prediction is globally linear. It says which corrections the data would see, locally, in each parameter direction.

## Derive the normal equations from the local model

Call the local objective m of p. It is one half the squared length of r plus J p, with r and J frozen at the current parameter vector. Expand its square. There is a constant term equal to one half the squared length of r; a linear term given by p dotted with J transpose r; and a quadratic term equal to one half p transpose J transpose J p.

Differentiate with respect to p. The gradient of this local model is J transpose r plus J transpose J p. Set that gradient equal to zero. We obtain the Gauss–Newton normal equations: J transpose J times p equals minus J transpose r.

When J has independent columns, J transpose J is positive definite and the normal equations have a unique solution. If J lacks full column rank, the minimizer need not be unique. The linear least-squares problem still makes sense, but writing the inverse of J transpose J does not.

Why does the condition J transpose r equals zero look familiar? Because the exact gradient of F with respect to theta is J transpose r. We can derive it by applying the chain rule to each squared residual. Thus at a stationary fitted parameter vector, r is orthogonal to every column of J. The data mismatch that remains cannot be reduced to first order by moving along any available parameter direction.

But orthogonality is not the same as perfect agreement. Consider one parameter x with residual vector whose entries are x and one. The objective is one half of x squared plus one. It has a unique minimizer x equals zero, at which the residual vector is zero and one, not the zero vector. Its derivative vanishes because the remaining residual is perpendicular to the one direction the model can change. The best fit need not be an exact solution of every measurement equation.

## Where the missing part of the Hessian went

For a general scalar objective, ordinary Newton's method uses the full Hessian. Let us derive that Hessian for a least-squares objective instead of guessing what Gauss–Newton omits.

Differentiate the gradient J transpose r. One derivative acts on r, giving J transpose J. The other acts on the entries of J, and produces a sum over residuals of residual number i times the Hessian of residual number i. So the exact Hessian of F consists of two terms: the Gram matrix J transpose J, and a residual-weighted sum of residual Hessians.

Gauss–Newton keeps the first term and discards the second. This is not a claim that the residuals themselves have no curvature. It is a choice of approximate Hessian based on the structure of the objective.

There are at least two circumstances in which that choice is promising. One is that the residuals are small near a good fit, so their coefficients in the omitted term are small, provided the individual residual Hessians remain controlled. Another is that the residual functions are nearly linear over the current region, so their second derivatives are small even if some residuals remain.

Neither is guaranteed simply because a problem is labeled least squares. A large nonzero residual combined with strong curvature can make the omitted term decisive. Worse, Gauss–Newton's local linear model can be convincing at the current point while being wildly misleading one long step away.

The positive semidefinite matrix J transpose J does offer an advantage: when J has full column rank, its negative-gradient solution is a descent direction whenever the gradient is nonzero. The calculation comes from multiplying the normal equation by p transpose: the directional derivative, gradient dotted with p, is minus the squared length of J p. A full unguarded step may still increase the actual objective. Descent direction is a local property; successful finite step is a separate question.

## Fit an exponential law by hand

Let's follow the whole construction in a small example. Suppose a model predicts y at time t as a times the exponential of b t. The two parameters are amplitude a and growth rate b. We observe a value of one at time zero and a value of two at time one.

The first residual is a minus one. The second is a times the exponential of b minus two. Start at a equals one and b equals zero. The predicted measurements are one and one. Our residual vector is zero and minus one. The objective is one half.

Now compute the two rows of the Jacobian. The first residual changes by one unit for a unit change in amplitude and does not depend on b; its row is one, zero. The second changes with a at a rate equal to the exponential of b, and with b at a rate equal to a times that exponential. At our starting point the row is one, one.

We seek a correction to the two parameters that makes the linearized residual zero. From the first row, the change in amplitude should be zero. From the second row, the change in b should be one. The Gauss–Newton step is therefore zero in a and plus one in b.

Evaluate the nonlinear model at the new parameters. We now predict one and the number e, about two point seven one eight. The second residual has changed from minus one to about plus zero point seven one eight. Our objective decreases from one half to about zero point two five eight. We overshot the exact fit, but the step improved it.

A further Gauss–Newton correction, still holding a at one, changes b by two divided by e minus one, approximately minus zero point two six four. The next growth-rate estimate is about zero point seven three six, approaching the exact value natural logarithm of two. In this two-observation problem there is an exact fit; in a larger or noisy data set the residual may not become zero.

Notice the difference between solving the linearized model and solving the nonlinear one. The first local correction says that a unit change in b would correct the missing second observation at the current tangent. It does not say the exponential will change by exactly one. Recomputing both residuals and Jacobian after the step is what makes the method iterative.

## Geometry, rank and computation

The columns of J describe the patterns in the measurements produced by adjusting individual parameters. If two columns are nearly parallel, the data struggle to tell the corresponding parameter changes apart. If a column is zero, changing that parameter has no first-order effect on the observations at the current point. If there are fewer independent measurement directions than parameter directions, the local inverse problem is underdetermined.

When J has full column rank, the Gauss–Newton step projects minus the residual onto the column space of J and finds the corresponding parameter correction. The part of the residual orthogonal to that space remains in the linear model. A small local model residual does not automatically imply a small parameter error: a nearly singular J can require a huge change in parameters to create a tiny measured change.

For an actual numerical computation, one should normally solve the least-squares problem using QR factorization or a singular-value decomposition, rather than explicitly forming an inverse of J transpose J. Forming the normal equations squares the two-norm condition number when J is full rank. That can magnify the numerical difficulty of a fit whose parameters are already hard to distinguish. The normal equations are indispensable for deriving the method, but they are not automatically the best implementation.

There are also choices about obtaining J. When derivatives of the model are available, analytic or automatically differentiated Jacobians can be accurate and efficient. Finite differences are useful but must balance truncation and rounding errors; scales of parameters and observations matter. Any approximation to J changes the quality of the local model, so it belongs in the error budget rather than being treated as invisible machinery.

## What rate should we expect?

It is tempting to transfer the quadratic-convergence claim of Newton's method straight to Gauss–Newton. That would be wrong without additional conditions. At an exact fit, where the residual vector vanishes, the omitted residual-Hessian term vanishes at the solution. If the residual Jacobian has full column rank there and is sufficiently regular, Gauss–Newton can attain local quadratic convergence. The linearized correction then cancels the leading error, and the remaining residual changes at second order.

At a best fit with nonzero residual, the omitted second-derivative term generally remains. The method may converge only linearly, and large curvature or poor conditioning can prevent convergence. It is possible for it to work very well despite a nonzero residual; the magnitude of the ignored curvature and the geometry of J determine the local behavior. The label nonlinear least squares is not a convergence certificate.

Gauss–Newton has given us a way to translate a nonlinear fitting problem into repeated linear least-squares problems. The step is mathematically motivated, computationally accessible, and often effective. But our exponential example already showed overshoot, and more strongly nonlinear examples can cause a full step to make the objective much worse. To turn this local model into a dependable algorithm, we must decide how far to trust it. That leads to damping and trust regions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Definitions and exact identities

For residuals \(r:\mathbb R^n\to\mathbb R^m\), twice differentiable near \(\theta\), and \(F(\theta)=\frac12\|r(\theta)\|_2^2\), write \(J=Dr(\theta)\). Then

\[
\nabla F(\theta)=J^\top r,\qquad
\nabla^2 F(\theta)=J^\top J+\sum_{i=1}^m r_i\nabla^2r_i.
\]

The Gauss–Newton step minimizes \(m(p)=\frac12\|r+Jp\|_2^2\) and therefore solves \(J^\top Jp=-J^\top r\), with unique step iff \(J\) has full column rank. If \(g=J^\top r\ne0\) and \(J\) has full column rank, then

\[
 g^\top p=-p^\top J^\top J p=-\|Jp\|_2^2<0.
\]

The normal equations are an identity defining the local least-squares minimizer, not an instruction to form \((J^\top J)^{-1}\) numerically.

### Exponential example

\[
 r(a,b)=\begin{bmatrix}a-1\\ae^b-2\end{bmatrix},\quad
 J(a,b)=\begin{bmatrix}1&0\\e^b&ae^b\end{bmatrix}.
\]

At \((a,b)=(1,0)\), \(r=(0,-1)^\top\), \(J=\left[\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right]\), so \(p=(0,1)^\top\). Then \(F(1,0)=1/2\), \(F(1,1)=\frac12(e-2)^2\approx0.25796\), with exact zero-residual parameters \((1,\log 2)\). At the next iterate, \(p=(0,2/e-1)\).

### Exercises with answers

1. **Nonzero residual optimum.** For \(r(x)=(x,1)^\top\), find the stationary point and residual norm. **Answer:** \(J=(1,0)^\top\), \(J^\top r=x\); the optimum is \(x=0\), with \(\|r\|=1\).
2. **The dropped Hessian.** For \(r(x)=x^2-1\), calculate both terms in \(F''\) at \(x=1/2\). **Answer:** \(J^\top J=(2x)^2=1\); \(r\,r''=(x^2-1)2=-3/2\); the exact Hessian is \(-1/2\). Gauss–Newton and optimization Newton use different curvature at this point.
3. **An exact local model.** If \(r(\theta)=A\theta-b\), compare Gauss–Newton and linear least squares. **Answer:** \(J=A\) is constant and all residual Hessians vanish. One full Gauss–Newton step reaches a linear least-squares minimizer if the subproblem is solved exactly; uniqueness requires full column rank.
4. **Local identifiability.** Show that two identical columns of \(J\) create a direction unseen by the local residual model. **Answer:** If columns \(j_1=j_2\), the parameter direction \((1,-1,0,\ldots,0)\) satisfies \(Jp=0\).

### Sources and further reading

- K. Madsen, H. B. Nielsen, and O. Tingleff, [*Methods for Non-Linear Least Squares Problems*, 2nd edition](https://www2.imm.dtu.dk/pubdb/edoc/imm3215.pdf), especially §3.1.
- [SciPy `least_squares` reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html), algorithm variants, Jacobians, and practical conditioning.
- [Wikipedia: Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm), for notation and introductory orientation.

*Teaching connections:* `multivariable-calculus:021000` introduces Newton corrections; `linear-algebra:021000` derives stable QR least squares; `multivariable-calculus:025000` studies singular parameter directions. These do not replace the mathematical assumptions stated above.
