# 017000 — Validated Integration of Ordinary Differential Equations

**Track:** Numerical Analysis and Reliable Computation. **Background:** local existence, Taylor methods, interval arithmetic, floating-point rounding. **Central question:** how can a computer return a set guaranteed to contain every true solution arising from an initial uncertainty set?

<!-- BEGIN SPOKEN LECTURE -->

# Validated Integration of Ordinary Differential Equations

A numerical integrator takes an initial state and produces a succession of approximate states. It may use very small time steps. It may compare two methods of different orders and report a tiny estimated error. Yet none of that alone proves the exact solution lies inside a particular interval.

Validated integration has a stronger goal. It constructs an enclosure: a region of state space guaranteed to contain the exact solution throughout a time step, or at least at the step's endpoint. The guarantee must account for uncertainty in initial conditions, truncation error in the numerical method, and floating-point rounding.

Start with the simplest differential equation: the rate of change of x equals x. At time zero, suppose x lies between one and one point zero one. The exact solutions are exponential curves, and after a short time the uncertainty interval expands. A standard numerical method might give a good approximation to its midpoint. A validated method must surround the entire family of possible exact trajectories.

## First prove the solution stays inside a box

The first task is not to take a numerical step. It is to find a region Y that provably contains the solution over the whole proposed time interval. Consider a short interval from zero to one tenth. Suppose we choose Y from point nine to one point two.

Inside Y, the derivative x is between point nine and one point two. Over one tenth of a time unit, its total contribution to change is between zero and one tenth times that derivative range. Starting anywhere between one and one point zero one, the integral equation therefore maps candidate paths back inside our chosen box.

This is an a priori enclosure. With a locally Lipschitz vector field and a suitable inclusion test, a fixed-point argument establishes the existence of a solution inside Y, with uniqueness under the standard hypotheses. The value of the test is that the region is known before we trust any approximate trajectory.

The box may be deliberately broad. Its purpose is correctness. Once we know where the solution can go, we can bound higher derivatives and obtain a much tighter enclosure for the endpoint.

## Taylor expansions with a certified remainder

For the exponential example, write a second-order Taylor approximation: the initial value multiplied by one plus the step size plus half the step size squared. A Taylor theorem tells us that the omitted third-order remainder depends on the third derivative at an intermediate time.

Here every time derivative of x equals x, and the a priori box bounds x above by one point two. The remainder over a step of one tenth is therefore at most one point two times one tenth cubed, divided by six. That is two ten-thousandths.

The endpoint then lies in a specific interval obtained by evaluating the Taylor polynomial over the entire initial interval and adding the rigorous remainder interval. Unlike an empirical step-size controller, this computation gives an inclusion that can be checked mathematically.

If we implement it using floating-point numbers, we must round interval endpoints outward. Rounding to nearest can quietly exclude a valid solution. Libraries for validated numerics therefore use directed rounding or exact rational arithmetic where practical.

## Why narrow intervals become wide

Validated does not mean automatically tight. Interval arithmetic can lose correlations. Suppose two quantities are known to be equal. Their difference is zero, but if we replace each with the same broad interval and subtract them independently, the resulting interval contains a whole range of possible differences.

Over many ODE steps this dependency problem can cause interval enclosures to grow far faster than the true uncertainty set. The geometric effect is called wrapping: a narrow, rotated, or curved set is repeatedly boxed in axis-aligned rectangles, and the empty corners accumulate as apparent uncertainty.

More sophisticated validated integrators track changes of coordinates, use interval or Taylor models with correlated remainders, and split or refine sets when necessary. These techniques do not weaken the proof. They help the proof remain informative over longer trajectories.

## An integrator can fail honestly

What happens if a proposed step is too large? The inclusion test for the a priori enclosure may fail. A rigorous solver should reduce the step, choose a better set representation, or report that it could not validate the step. It must not silently replace a failed proof with a plausible-looking floating-point answer.

Notice the distinction between a solver failure and a mathematical singularity. A rigorous method may fail because its enclosure became too wide, even though the true solution continues smoothly. Conversely, a numerical method may continue returning numbers while the mathematical solution approaches finite-time blow-up.

Validated integration therefore offers a new kind of computational contract. An accepted step comes with a mathematically justified containing set. An unaccepted step makes no such claim. Together with interval methods for root finding and verified linear algebra, this is one of the ways numerical computation can produce evidence suitable for later mathematical proofs.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(x'(t)=f(x(t))\), initial set \(X_0\subset\mathbf R^d\), and step \([0,h]\), one sufficient enclosure test is to find a compact convex box Y with
\[X_0+[0,h]f(Y)\subset\operatorname{int}(Y)\]
and a locally Lipschitz f on a neighborhood of Y. Under standard integral-operator fixed-point conditions this gives existence of trajectories in Y for all initial values in X_0 over [0,h]; Lipschitz continuity ensures uniqueness. The inclusion is sufficient, not necessary, and more general ODE methods use sharper operators.

**Verified example:** \(x'=x\), \(X_0=[1,1.01]\), h=0.1, Y=[0.9,1.2]. Then \(f(Y)=[0.9,1.2]\) and \(X_0+[0,0.1]f(Y)\subseteq[1,1.13]\subset\operatorname{int}Y\).

Second-order Taylor with the certified third-derivative bound \(|x'''|=|x|\le1.2\) gives
\[x(h)\in X_0\left(1+h+\frac{h^2}2\right)+[0,1.2h^3/6]\subseteq[1.105,1.11625].\]
The exact endpoint set is \([e^{0.1},1.01e^{0.1}]\), which lies inside this interval. These numerical endpoints are rational decimals and can be evaluated without floating-point uncertainty; an implementation using binary floats must enclose them outward.

**Error mechanisms:** truncation remainder, initial uncertainty, rounding error, and the dependency/wrapping effect. A numerical error estimate without a certified bound does not prove containment. An inclusion failure does not imply ODE nonexistence.

### Exercises with answers

1. For x'=x and X_0=[1,1.01], is Y=[0.9,1.2] a valid a priori box over h=0.1? **Answer:** yes; the integral-image interval lies in [1,1.13] inside the interior of Y.
2. Why is the third derivative bound 1.2 valid? **Answer:** x'''=x for this ODE, and the a priori enclosure bounds x along the step by 1.2.
3. What is wrong with subtracting the interval [1,2] from itself to infer x-x=0? **Answer:** ordinary interval subtraction loses the equality dependency and returns [-1,1].
4. What must a validated solver report when its inclusion test fails? **Answer:** no validated enclosure for that step; it may retry with a smaller step or better set representation, but may not assert containment.

### Reading and source notes

- [CAPD DynSys documentation, rigorous interval Poincaré maps](https://capd.sourceforge.net/capdDynSys/docs/html/a05237.html), certified integration and return maps.
- [CAPD DynSys documentation, interval set representations](https://capd.sourceforge.net/capdDynSys/docs/html/a05202.html), practical control of wrapping.
- [CAPD DynSys documentation, one-step Taylor method](https://capd.sourceforge.net/capdDynSys/docs/html/a05230.html), introduction to Taylor-method integration (non-rigorous and interval variants must be distinguished).
