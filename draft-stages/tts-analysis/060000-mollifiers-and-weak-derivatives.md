# 060000 — Mollifiers and Weak Derivatives: Smooth Approximations to Rough Functions

**Track:** Analysis from First Principles. **Background:** Convolution, distributions and L-p spaces. **Central question:** How can we justify calculus by approximating a rough function with smooth ones?

<!-- BEGIN SPOKEN LECTURE -->

# Mollifiers and Weak Derivatives: Smooth Approximations to Rough Functions

A photograph taken through a lens is never infinitely sharp. Yet if we choose a sequence of finer lenses, the blurred images can approach the original scene. Mathematical smoothing works in a similar way. It gives us an approximation procedure for rough functions, and that procedure is the bridge between classical calculus and weak calculus.

Choose a smooth nonnegative function, call it rho, supported in a small region around zero, whose integral is one. We can rescale it to make it narrower and taller while keeping total area one. Convolve an integrable function f with this scaled rho. The result averages f over a neighborhood whose width is controlled by the scale. We call rho a mollifier.

Why is this powerful? Even if f is merely locally integrable, the convolved function is smooth wherever the convolution is defined appropriately. To differentiate the result, we differentiate the mollifier, not the rough f. The smooth kernel does the analytic work. Moreover, as the scale approaches zero, the mollified functions converge to f in L p for finite p, under the standard whole-space assumptions or locally on an open set.

Consider the step function that jumps from zero to one. Its mollification replaces the jump with a smooth transition. The transition becomes steeper as the mollifier gets narrower. The first derivative of each smoothed step is an ordinary nonnegative bump with total integral one. In the limit, those derivatives do not approach an ordinary L one function. They approach the delta distribution. This is a concrete reason to distinguish convergence of functions from convergence of their derivatives.

Now suppose f has a weak derivative g that lies in L p. By definition, the integration-by-parts identity holds: when we integrate f against the derivative of a test function, we get minus the integral of g against the test function. Convolving both f and g with the mollifier preserves that relationship. The derivative of the smoothed f is exactly the smoothed g. As the scale shrinks, f and its derivative approach f and g in the relevant L p norms. Thus a weak derivative can be approximated by classical derivatives in a controlled way.

One example is the absolute value function on a bounded interval. It has a corner, so it is not continuously differentiable there. But its weak first derivative is the sign function, which is bounded and hence square integrable on that interval. The absolute value function therefore belongs to a first-order Sobolev space there. Its second distributional derivative is twice a delta, which is not an L two function. So it generally fails to belong to the second-order Sobolev space on any interval containing the corner.

Another example is a genuine jump. The indicator of the positive half-line has distributional derivative delta. On a bounded interval containing zero, that delta cannot be represented by an L one function, much less an L two function. The step is therefore not in the first-order Sobolev space when the interval crosses the jump. The contrast is instructive: a corner in the function can be acceptable at first order, while a jump cannot.

Why bother with weak derivatives instead of smoothing every physical solution and calling it good? Because we want a stable notion that survives limits. In a PDE computation, we might have a sequence of smooth approximate solutions whose ordinary derivatives are bounded in L two. Under suitable compactness or weak-convergence arguments, a limiting function can inherit a weak derivative even if its pointwise derivative is impossible to discuss. We need weak derivatives to formulate what the limit satisfies.

There is a delicate issue at boundaries. On the whole real line, convolution with a compactly supported smooth kernel is straightforward. On a bounded interval or a region with a curved boundary, the kernel may sample outside the domain. We can mollify safely in the interior, or use extension theorems when the domain has suitable geometry. We cannot claim that naive convolution automatically preserves boundary conditions. For example, smoothing a function that vanishes at the boundary can produce one that does not vanish there unless the construction is arranged carefully.

This issue motivates another space: the closure of smooth compactly supported functions under the first-order Sobolev norm. The functions in that closure are said to have zero trace in the appropriate sense, under standard domain assumptions. The trace is the generalized boundary value needed for weak boundary-value problems. A Sobolev function may lack ordinary pointwise boundary values, yet still possess a well-defined trace if its interior regularity and the boundary geometry are suitable.

Mollification has an intellectual role beyond merely obtaining differentiable formulas. It lets us prove an identity for smooth functions, obtain an estimate independent of the smoothing scale, and pass to the limit. This is a recurring proof pattern. One uses easy algebra where derivatives exist, then transfers the estimate to a larger space by completeness and controlled convergence.

The key is not to silently exchange limits and operations. We must know which quantities converge in L p, which only converge weakly, and which converge as distributions. When the relevant norms are controlled, mollification turns rough analysis into a rigorous extension of familiar calculus rather than a collection of new rules invented for difficult functions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Choose \(\rho\in C_c^\infty(\mathbb R^d)\), \(\rho\ge0\), \(\int\rho=1\), and \(\rho_\varepsilon(x)=\varepsilon^{-d}\rho(x/\varepsilon)\). For \(f\in L^p(\mathbb R^d)\), \(1\le p<\infty\),
\[\rho_\varepsilon*f\in C^\infty(\mathbb R^d),\qquad\rho_\varepsilon*f\to f\text{ in }L^p.\]
For \(f\in W^{k,p}(\mathbb R^d)\), \(D^\alpha(\rho_\varepsilon*f)=\rho_\varepsilon*(D^\alpha f)\) for \(|\alpha|\le k\), and \(\rho_\varepsilon*f\to f\) in \(W^{k,p}\).

A weak derivative \(g=\partial_jf\) on \(\Omega\) means \(\int_\Omega f\partial_j\varphi=-\int_\Omega g\varphi\) for all \(\varphi\in C_c^\infty(\Omega)\). For \(f=|x|\) on \((-1,1)\), \(f'=\operatorname{sgn}x\in L^p\) for finite p, but \(f''=2\delta_0\notin L^p\). For \(H\), \(H'=\delta_0\), so \(H\notin W^{1,p}((-1,1))\) for \(p\ge1\).

On a bounded Lipschitz domain, the trace map \(\operatorname{Tr}:W^{1,p}(\Omega)\to\) an appropriate boundary trace space is bounded for \(1\le p<\infty\), and \(W^{1,p}_0(\Omega)\) is its kernel under usual hypotheses. Interior mollification does not by itself preserve boundary conditions.

### Exercises with answers

1. **Mass of mollifier.** Verify \(\int \rho_\varepsilon dx=1\). **Answer:** Substitute \(y=x/\varepsilon\).
2. **Corner or jump?** Which of \(|x|\) and \(H(x)\) belongs to \(W^{1,2}((-1,1))\)? **Answer:** Only \(|x|\).
3. **Derivative transfer.** Explain \(D(f*\rho_\varepsilon)=f*(D\rho_\varepsilon)\). **Answer:** Differentiate the smooth kernel under the integral; for weakly differentiable f it also equals \((Df)*\rho_\varepsilon\).

### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [John K. Hunter, Measure Theory notes](https://www.math.ucdavis.edu/~hunter/m206/intro_measure_notes.pdf)
