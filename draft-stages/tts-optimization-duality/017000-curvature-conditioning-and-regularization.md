# Curvature, Conditioning, and Regularization: Why Optimization Speed Is Geometric

<!-- BEGIN SPOKEN LECTURE -->

# Curvature, Conditioning, and Regularization: Why Optimization Speed Is Geometric

Why can gradient descent race to a solution on one problem and crawl on another that looks almost identical? Two quadratic functions may both have a unique minimum, both be smooth, and both have gradients that are easy to compute. Yet one is solved in a few steps while the other takes hundreds or thousands. The difference often comes from geometry: how quickly the objective bends in different directions.

This connects the eigenvalues of a matrix to the speed of an optimization algorithm. It also clarifies why preconditioning and regularization are different operations. One changes how we travel toward the optimum. The other changes which optimum we seek. A statistical estimator may use both, but the reasons must be kept separate.

## A quadratic whose valley is narrow

Consider a function of two variables, x and y. Its value is one half times the sum of x squared and one hundred times y squared. The minimum lies at the origin, where the function is zero. Its gradient has first component x and second component one hundred y. Its Hessian matrix is diagonal, with entries one and one hundred.

The graph looks like a bowl, but the curvature is much greater in the y direction than the x direction. Move a small amount along y and the function changes quickly. Move the same amount along x and it changes slowly. A circle of equal coordinate distances is not a contour of equal objective value. The level curves are elongated ellipses.

The ratio of the largest Hessian eigenvalue to the smallest is one hundred. This is the spectral condition number of the positive-definite Hessian in the Euclidean coordinates we chose. It measures the contrast between steep and shallow directions. We should not confuse it with a universal count of gradient-descent iterations, but it is a useful predictor of difficulty for simple first-order methods.

Gradient descent with fixed step size alpha subtracts alpha times the gradient from the current point. For our function, the new x coordinate is the old x multiplied by one minus alpha. The new y coordinate is the old y multiplied by one minus one hundred alpha. We can analyze the method without any simulation because each coordinate evolves independently.

## Why a safe step can be painfully slow

To make both coordinates converge to zero, each multiplier must have absolute value less than one. For the x direction, alpha must be between zero and two. For the y direction, alpha must be between zero and two hundredths. The steep direction forces a much smaller step than the shallow direction would prefer.

Choose alpha equal to one hundredth. Then the y coordinate reaches zero in one iteration. But the x coordinate retains ninety-nine percent of its previous value at every iteration. After a hundred iterations its magnitude is still about thirty-seven percent of the initial magnitude. The method is not broken. It is obeying the stability requirement imposed by one direction while making very slow progress in another.

We can choose a fixed step that balances the two contraction factors. For a positive-definite quadratic with smallest Hessian eigenvalue mu and largest eigenvalue L, the minimax constant step for worst-case Euclidean error on this quadratic is two divided by L plus mu. The resulting worst-case contraction factor is L minus mu divided by L plus mu. With eigenvalues one and one hundred, that factor is ninety-nine divided by one hundred one, roughly ninety-eight percent per iteration.

This is better than ninety-nine percent, but still slow. The narrow valley persists. The problem is not a poor line of code for computing the derivative. It is the mismatch between a single uniform step size and an objective with very different curvatures.

## Preconditioning changes the geometry of a step

Instead of taking a step against the raw gradient, multiply the gradient by a positive-definite matrix that compensates for the objective's shape. For our quadratic, choose the inverse Hessian: diagonal entries one and one hundredth. Multiplying this inverse by the gradient gives the vector x, y. A step of length one against that preconditioned direction moves directly to the origin in one iteration.

This is the simplest possible illustration of a Newton step. A quadratic with a constant positive-definite Hessian is solved exactly by the full Newton step, because its local quadratic model is the exact objective. For a nonquadratic function, the Hessian changes with position and may not be positive definite. A full Newton step can fail to decrease the objective if the local model is inappropriate, so practical methods may use line searches, trust regions, damping, or modified Hessians.

Even on the quadratic, computing an exact inverse is rarely the preferred implementation for a large problem. A preconditioner is often a cheaper approximation to the inverse curvature that makes the main directions more balanced. The algorithm applies this approximation through a solve or structured operation rather than constructing a dense inverse matrix.

The relation to geometry is direct. If a positive-definite matrix G defines a metric in parameter space, a metric-gradient step uses G inverse times the ordinary gradient coefficients. Preconditioning gradient descent with G inverse is therefore a choice of step geometry. A well-chosen metric can reduce the effect of anisotropic curvature. A poorly chosen one can make convergence worse.

## From eigenvalues to a convergence proof

The two-coordinate example lets us inspect exact multipliers, but there is a broader theorem. Suppose a differentiable function is strongly convex with parameter mu greater than zero. Roughly, its graph bends upward by at least mu times a quadratic in every direction. Suppose also that its gradient is L-Lipschitz, meaning the gradient cannot change faster than L times the distance moved.

Strong convexity supplies a lower curvature bound and the Lipschitz gradient supplies an upper one. For twice continuously differentiable functions, these assumptions correspond to all Hessian eigenvalues lying between mu and L throughout the relevant convex domain.

Under these assumptions, gradient descent with step size one divided by L decreases the objective. The smoothness inequality shows that after one step, the function value is no greater than the old value minus the squared gradient norm divided by twice L.

We also need to relate the size of the gradient to the remaining objective error. Strong convexity does that. For any current point x, compare the strongly convex lower bound at the minimizer. Rearranging and completing a square gives the inequality that the current objective gap above the minimum is no greater than the squared gradient norm divided by twice mu.

Combine the two facts. Each one-over-L step reduces the objective gap by at least a mu-over-L fraction of its present size. Therefore the gap after the step is at most one minus mu over L times the old gap. Repeating produces a geometric convergence bound.

The ratio L divided by mu appears naturally: a small mu gives little guaranteed progress in flat directions, while a large L limits safe step sizes in steep directions. The proof says why conditioning matters rather than merely reporting that it does.

This result has hypotheses. Without strong convexity, a minimizer may not be unique, or the curvature lower bound may be zero. Without a suitable smoothness bound, the chosen fixed step may be unsafe. A constrained feasible set changes the update and analysis. A stochastic gradient introduces noise, so deterministic monotone decrease need not occur at every step.

## A certificate from a gradient, and its limits

The same strong-convexity argument yields an error certificate. If mu is a valid lower curvature bound and we have computed the gradient exactly, then the objective value at x exceeds the optimum by no more than the squared gradient norm divided by twice mu.

This is useful because we rarely know the true minimizer or its objective value in advance. We may be able to compute a candidate and its gradient, together with a justified lower bound on curvature. A small gradient can then certify near-optimality.

But it would be a mistake to quote this bound without a valid mu. If the objective is nearly flat in some direction, the same small gradient could correspond to a much larger parameter error. And a numerical gradient computed inaccurately may be misleading. The certificate is conditional on the model, the curvature bound, and the reliability of the computed derivative.

For a positive-definite quadratic, we can also bound the distance to the minimizer using the inverse of the smallest eigenvalue: the distance is no greater than the gradient norm divided by mu. This makes the connection between curvature and sensitivity explicit.

## Regularization is not a faster way to solve the same problem

Now consider least squares. The data matrix X maps a coefficient vector beta to predicted observations. The ordinary objective is one half of the squared length of X beta minus y. Its Hessian is X transpose X. If the columns of X are nearly dependent, this Hessian has a very small eigenvalue. We encounter both slow optimization and uncertainty about the fitted coefficients.

One remedy for the algorithm alone is to use a more stable factorization or a preconditioner. QR or SVD can make the numerical calculation more trustworthy without redefining which least-squares solution we want. By contrast, ridge regularization adds a penalty, one half lambda times the squared coefficient norm. The new Hessian is X transpose X plus lambda times the identity.

Every eigenvalue of X transpose X is shifted upward by lambda. This can make the condition number of the new objective smaller, and if lambda is positive, the new Hessian is positive definite even when X is rank deficient. But the target coefficient vector generally changes. Ridge is not merely a preconditioner. It encodes a preference for smaller coefficients and trades some bias for potentially lower variance under a statistical model.

To see that tradeoff in the simplest setting, imagine one noisy measurement y of a scalar parameter beta, with measurement noise having mean zero and variance sigma squared. Ordinary least squares estimates beta by y. Ridge with penalty lambda estimates beta by y divided by one plus lambda. The ridge estimate has expected value beta divided by one plus lambda, so it is biased toward zero. Its variance is sigma squared divided by the square of one plus lambda. Whether its mean squared error is better depends on the true beta, the noise variance, and lambda. There is no single lambda that is best for every possible unknown parameter.

Preconditioning aims to solve the chosen problem efficiently. Regularization changes the chosen problem to express a modeling or inferential preference. A practical pipeline often needs both, but they should not be conflated when interpreting results.

## The same geometry across disciplines

The Hessian in optimization tells us how an objective bends. The Gram matrix in least squares tells us which parameter directions the observations distinguish. The Fisher information in a regular statistical model describes local sensitivity of probability distributions to parameters. Under appropriate conditions these matrices can all act as local metrics or curvature operators, though they are not interchangeable and their definitions carry different assumptions.

This family resemblance explains why a single linear-algebra skill recurs in many areas: eigenvalues and singular values expose directions of strong or weak sensitivity; matrix factorization helps solve systems reliably; quadratic forms express both curvature and uncertainty.

The narrow quadratic valley began as a simple example of slow gradient descent. It led to step-size stability, eigenvalue conditioning, metric-aware descent, rigorous convergence rates, and the distinction between preconditioning and regularization. When an optimization algorithm struggles, the right first question is not simply whether to try more iterations. Ask what geometry the problem presents, what algorithmic geometry the method assumes, and whether changing the objective would also change the scientific claim you intend to make.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Exact quadratic iteration

\[
 f(x,y)=\frac12(x^2+100y^2),\qquad H=\nabla^2f=\operatorname{diag}(1,100),\qquad \kappa_2(H)=100.
\]

Fixed-step gradient descent gives \(x_{k+1}=(1-\alpha)x_k\), \(y_{k+1}=(1-100\alpha)y_k\). Convergence for every initial state requires \(0<\alpha<2/100\). For \(\alpha=1/100\), the slow component contracts by \(0.99\). The best fixed \(\alpha\) for worst-case Euclidean vector contraction on the SPD quadratic is \(2/(L+\mu)\), with factor \((L-\mu)/(L+\mu)=99/101\). The inverse-Hessian-preconditioned step with \(\alpha=1\) solves this quadratic in one step.

### Convergence and certificates

If \(f\) is differentiable, \(\mu\)-strongly convex and \(L\)-smooth on \(\mathbb R^n\), with \(0<\mu\le L\), then
\[
 f\!\left(x-\tfrac1L\nabla f(x)\right)\le f(x)-\frac{\|\nabla f(x)\|^2}{2L},
\quad f(x)-f_*\le\frac{\|\nabla f(x)\|^2}{2\mu},
\]
thus \(f(x_{k+1})-f_*\le(1-\mu/L)(f(x_k)-f_*)\). The distance bound \(\|x-x_*\|\le\|\nabla f(x)\|/\mu\) also follows from strong monotonicity of \(\nabla f\). These are *conditional* bounds; no such finite constant can be asserted when \(\mu=0\).

### Ridge versus preconditioning

\[
 f_{\rm ridge}(\beta)=\tfrac12\|X\beta-y\|^2+\tfrac\lambda2\|\beta\|^2,
\qquad \nabla^2 f_{\rm ridge}=X^TX+\lambda I.
\]

For scalar \(y=\beta+\varepsilon\) with \(E\varepsilon=0\), \(\operatorname{Var}(\varepsilon)=\sigma^2\), ridge gives \(\hat\beta_\lambda=y/(1+\lambda)\). Bias \(-\lambda\beta/(1+\lambda)\), variance \(\sigma^2/(1+\lambda)^2\), and mean squared error \((\lambda^2\beta^2+\sigma^2)/(1+\lambda)^2\). This illustrates why improved conditioning does not automatically mean improved estimation of the original parameter.

### Exercises and solutions

1. **Exact multipliers.** For \(f=(x^2+9y^2)/2\), what fixed step sizes converge from every starting point? **Answer:** \(0<\alpha<2/9\).
2. **Optimal scalar step.** What is the minimax constant step for the preceding quadratic? **Answer:** \(\alpha=2/(1+9)=1/5\), giving worst-coordinate contraction \(4/5\).
3. **Certificate.** If \(\mu=2\) is a valid strong-convexity bound and \(\|\nabla f(x)\|=0.1\), bound the objective gap. **Answer:** at most \(0.1^2/(4)=0.0025\).
4. **Rank deficiency.** For \(X=\begin{pmatrix}1&1\\2&2\end{pmatrix}\), what is \(\mu\) for ordinary least squares in all coefficient directions? **Answer:** zero; \(X^TX\) is singular.
5. **Scalar ridge.** With \(\beta=0\) and \(\sigma^2=1\), what is the mean squared error of ridge with \(\lambda=1\)? **Answer:** \(1/4\), compared with \(1\) for the unbiased ordinary estimator. For nonzero \(\beta\), bias contributes.

### Sources and further reading

- [Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), convexity, strong convexity, numerical optimization and regularization.
- [Neal Parikh and Stephen Boyd, *Proximal Algorithms*](https://web.stanford.edu/~boyd/papers/prox_algs.html), first-order methods and proximal perspectives.
- [Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*](https://people.maths.ox.ac.uk/trefethen/text.html), spectral conditioning and solvers.
- Related lectures: `optimization-duality:005000`, `linear-algebra:025000`, `multivariable-calculus:020000`, `linear-algebra:028000`, `multivariable-calculus:071000`.
