# From One-Step Errors to Global Accuracy: Consistency, Convergence, and Step-Size Tests

<!-- BEGIN SPOKEN LECTURE -->

# From One-Step Errors to Global Accuracy

A numerical method may make an almost invisible error in its first step and still give a poor answer by the end of a long calculation. The reason is not mysterious: later steps are built on earlier approximations. A small error changes the next slope, which changes the following state, which changes the next slope again. In a sensitive system, those changes can grow. Even in a well-behaved system, there may be thousands of steps in which errors accumulate.

We need two different measurements. The first asks how faithfully a numerical rule advances the exact solution through one interval. The second asks how far the computed trajectory is from the true solution after many intervals. The two are connected, but they are not interchangeable. We will derive that connection, prove a useful bound in the Euler case, and learn how to estimate the order of an unfamiliar implementation by repeating the same problem with smaller steps.

## What happens if we start from the true value?

Imagine we could obtain the exact solution at some time t. We then hand that exact state to our numerical algorithm and ask it to take one step of size h. Compare the algorithm's predicted endpoint to the actual solution at time t plus h. That difference is the one-step defect, sometimes called the unscaled local truncation error.

In the Euler method, the predicted endpoint is the exact starting value plus h times the derivative there. Taylor's theorem says the actual endpoint also has a term equal to h squared divided by two, times the second derivative at some intermediate time, provided the solution is smooth enough. Euler has dropped that curvature term. Its one-step defect is therefore generally proportional to h squared.

This is where a vocabulary trap appears. Some textbooks call the defect itself the local truncation error. Others divide it by h and apply the same name to the result. With the first convention Euler's local error is of order h squared; with the second, it is of order h. Neither author has necessarily made a mistake. We will always say whether the one-step difference has been divided by h.

For explicit midpoint the one-step defect begins at order h cubed. For classical R K four, it begins at order h to the fifth power, given sufficient smoothness. This is why midpoint is called second order and classical R K four is called fourth order. Those names refer to the resulting convergence rate over a fixed time interval, not to the exponent in the unscaled one-step defect.

## The stored value is no longer exact

Now suppose we have already made an error. At step n, the stored number differs from the exact y at that time. Our next Euler update evaluates the derivative at the stored number, not at the exact state. That introduces a second kind of discrepancy, on top of the new curvature error.

To control it, assume the rate function f is Lipschitz continuous in the state over a region containing both the true and computed trajectories. In ordinary language, changing the state by a small amount can change the computed rate by at most a fixed multiple of that amount. Let that multiple be L. For a scalar problem it means the absolute difference between two rates at the same time is at most L times the distance between their states.

Write the existing error as e sub n. The next error is bounded by one plus h L times the previous error, plus the fresh one-step defect. If the second derivative of the exact solution is bounded in magnitude by M, the new defect is at most M h squared divided by two. Thus the error after each Euler step obeys a recurrence: new error no larger than one plus h L times old error, plus M h squared over two.

We do not need to solve this recurrence exactly to understand it. Repeat the inequality and the error becomes a sum of fresh defects, each multiplied by factors describing how later steps amplify it. The product of one plus h L over a fixed time interval is bounded by an exponential depending on L and elapsed time. There are roughly one over h steps in that interval. Combining one over h contributions of size h squared gives a total of order h.

That is the fundamental reason Euler has first-order global accuracy under the assumptions. It is also why midpoint's h-cubed one-step defect leads to second-order global accuracy, and R K four's h-to-the-fifth defect leads to fourth-order global accuracy, provided their error propagation is controlled. Higher order at a single step is valuable because many such steps have to fit together.

## A fully computable error experiment

Let the differential equation be y prime equals negative y, starting at one, and integrate to time one. The exact solution is exponential of negative t, so the exact endpoint is approximately point three six seven eight seven nine four.

Euler has an especially transparent rule on this problem. Each step multiplies the previous value by one minus h. With a step of point two, five steps take us to point eight raised to the fifth power, which is point three two seven six eight. The error is roughly point zero four zero two.

Halve the step to point one. Now take ten steps, each multiplying by point nine. The result is about point three four eight six eight, with error about point zero one nine two. Halve again to point zero five and take twenty steps, each multiplying by point nine five. The endpoint is about point three five eight four nine, with error about point zero zero nine three nine.

The error has roughly halved whenever we halved h. It did not halve exactly. Asymptotic error scaling is a limiting trend, not an identity at every coarse step. The observed sequence is what we expect from a first-order method. It is a better check of an implementation than simply noticing that all three numerical answers are positive and decreasing.

We can do a similar calculation for the midpoint method without deriving a new exact solution. For the equation y prime equals negative y, one explicit midpoint step multiplies by one minus h plus half h squared. After one over h steps, the computed endpoint is that factor raised to the corresponding power. For small h, the difference from exponential of negative one scales like h squared rather than h. This is a simple experiment in which an algorithm's advertised order can be checked numerically.

## Reading the rate at which error decreases

Suppose a method gives endpoint results on three meshes with step sizes h, h over two, and h over four. If its leading global error behaves as a constant times h to the p, then halving h should reduce that leading term by a factor of two to the p.

For a first-order method, expect a factor near two. For a second-order method, expect near four. For a fourth-order method, expect near sixteen. When the exact solution is available, compare each result to it. If no exact solution is known, compare consecutive approximations. The difference between results at h and h over two will generally have the same leading scaling, assuming they have entered the asymptotic regime and the coefficient of the leading error is nonzero.

This is called a refinement study. It can catch mistakes in the code, but it can also reveal that the step sizes are still too large for an asymptotic law, that a discontinuity has reduced the order, or that floating-point roundoff is dominating the differences. A nearly zero difference between two coarse answers is not proof that both are accurate. They may share a systematic error.

There is another subtlety. The derivative function may be implemented with its own approximation or inaccurate units. In that case shrinking the time step may converge beautifully toward the solution of the wrong differential equation. Numerical convergence tests check the algorithm relative to the model it is given; they do not establish that the model correctly describes the physical world.

## Sensitivity and the size of an error bound

The Lipschitz constant L appears inside an exponential factor in the bound. For a system in which nearby trajectories separate rapidly, that bound can be large. This does not mean every calculation attains the worst case. It tells us that local accuracy alone may be an inadequate guide if errors are strongly amplified.

Consider two genuine solutions of y prime equals y whose initial values differ slightly. Their difference also grows like exponential of t. A numerical method cannot make this genuine sensitivity disappear. It must work within it. Conversely, for a decaying equation, exact nearby solutions approach one another; but a badly chosen numerical method can still amplify numerical disturbances. That latter behavior is a stability problem of the algorithm itself, not of the continuous equation. We will analyze it explicitly with a fast-decay example.

For a vector-valued ODE, we use a norm in place of absolute value. The same Lipschitz and error-propagation arguments apply. However, different state components may have different units and scales. In practice a solver's absolute and relative tolerances are interpreted componentwise or through a weighted norm. A millimeter error in position is not directly comparable to a millisecond error in timing or a tiny concentration error without choosing a meaningful scale.

## What the convergence theorem does not promise

A convergence proof begins with a region where the exact and numerical solutions remain and where the rate function has the regularity needed for the estimates. It also fixes a finite interval of time. The guarantee is not that a method has a constant error forever, or that its declared order survives an actual blow-up, an unresolved switch in forcing, or a step too large for stability.

We can summarize the logic without treating it as a slogan. First, verify that a numerical step approximates the true short-time evolution to a known order when started exactly. Second, show that small input errors are not magnified without control over the relevant interval. Finally, combine these two pieces to estimate the discrepancy after repeated steps. This is the path from consistency to convergence for the one-step methods we have studied.

The lesson is practical as well as theoretical. Report the integration interval and the step size. Check the actual differential equation and the initial conditions. Repeat a calculation on a refined time grid. Observe whether the error decreases at the predicted rate. And remember that a method can be formally high order but unusable at a particular step size, because accuracy is only one side of the story. The other side is whether the discretized dynamics behave sensibly at all.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: a global Euler error bound and refinement checks

Consider \(y'=f(t,y)\) on \([0,T]\), with \(y(0)=y_0\), exact solution \(y\in C^2\), \(|y''(t)|\le M\), and \(f\) Lipschitz in \(y\) with constant \(L\) in a region containing the exact and numerical states. Let \(e_n=|y_n-y(t_n)|\) for Euler with \(t_n=nh\). Taylor's theorem gives one-step defect
\[
\delta_n=\left|y(t_{n+1})-y(t_n)-h f(t_n,y(t_n))\right|\le \frac M2 h^2.
\]
Consequently
\[
e_{n+1}\le(1+hL)e_n+\frac M2h^2,\qquad e_0=0.
\]
For \(L>0\), summing the geometric series yields
\[
e_n\le \frac{Mh}{2L}\bigl((1+hL)^n-1\bigr)\le\frac{Mh}{2L}(e^{LT}-1).
\]
If \(L=0\), instead \(e_n\le MT h/2\). This demonstrates \(O(h)\) *global* error over a fixed time interval, under the stated hypotheses. For a one-step method of order \(p\), a local defect \(O(h^{p+1})\) combined with suitable Lipschitz stability yields \(O(h^p)\) global error.

**Terminology note.** Some sources define *local truncation error* as \(\delta_n/h\) rather than \(\delta_n\). The exponent in a quoted local-error order depends on that normalization; the global-order statement does not.

### Exact refinement experiment for \(y'=-y\)

\[
y(1)=e^{-1}\approx 0.3678794412,\qquad y_N=(1-h)^N,\qquad Nh=1.
\]

| \(h\) | \(N\) | Euler \(y_N\) | Absolute error |
|---:|---:|---:|---:|
| \(0.20\) | 5 | \(0.8^5=0.3276800000\) | \(0.0401994412\) |
| \(0.10\) | 10 | \(0.9^{10}\approx0.3486784401\) | \(0.0192010011\) |
| \(0.05\) | 20 | \(0.95^{20}\approx0.3584859224\) | \(0.0093935188\) |

For explicit midpoint on the same test problem, \(y_N=(1-h+h^2/2)^N\); its global error is \(O(h^2)\). For Euler, taking logarithms gives
\[
\log y_N=\frac1h\log(1-h)=-1-\frac h2+O(h^2),\quad y_N=e^{-1}(1-h/2+O(h^2)).
\]
This independently confirms the observed first-order trend.

### Exercises with answers

1. **Local versus global.** If a one-step method has an unscaled defect \(O(h^3)\), what global order should you expect under appropriate stability? **Answer:** order two, i.e. \(O(h^2)\) at fixed finite time.
2. **Count error contributions.** Why does \(O(h^2)\) local Euler defect not automatically mean \(O(h^2)\) total error? **Answer:** \(O(1/h)\) steps contribute, and their errors propagate; the controlled total is generally \(O(h)\).
3. **Estimate an observed order.** If a fixed-time error decreases from \(0.016\) to \(0.004\) when h is halved, what order does that suggest? **Answer:** \(p=\log_2(4)=2\).
4. **Direct formula check.** Show that midpoint on \(y'=-y\) multiplies by \(1-h+h^2/2\). **Answer:** \(k_1=-y_n\), predicted midpoint \(y_n(1-h/2)\), \(k_2=-y_n(1-h/2)\), and \(y_{n+1}=y_n+h k_2\).
5. **Scope of a theorem.** Does the displayed Euler bound alone cover a solution that blows up before \(T\)? **Answer:** no; the bound presupposes a smooth exact solution with bounded second derivative and an appropriate Lipschitz region across \([0,T]\).

### Sources and further reading

- Stuart Brorson, [Forward Euler: Local truncation error versus global solution error](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29/02%3A_Forward_Euler_method/2.03%3A_Local_truncation_error_vs._global_solution_error) (note that error conventions vary by author).
- Stuart Brorson, [*Numerically Solving Ordinary Differential Equations*](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29).
- Wikipedia: [Truncation error (numerical analysis)](https://en.wikipedia.org/wiki/Truncation_error_(numerical_analysis)), [Convergence of numerical methods for ordinary differential equations](https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations).
