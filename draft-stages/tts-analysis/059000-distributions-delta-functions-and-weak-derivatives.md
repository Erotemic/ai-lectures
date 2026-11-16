# 059000 — Distributions: Making Sense of Delta Functions and Rough Derivatives

**Track:** Analysis from First Principles. **Background:** Integrals, smooth test functions and integration by parts. **Central question:** How can a function have a derivative even where it has a corner or a jump?

<!-- BEGIN SPOKEN LECTURE -->

# Distributions: Making Sense of Delta Functions and Rough Derivatives

Imagine a string tied at one point and struck sharply with a hammer. The force is concentrated in a very short time. In a simple model we idealize it as an instantaneous impulse, a force with finite total effect but no ordinary finite height at the instant of impact. Physicists call it a delta impulse. How can such a thing belong to mathematics if it is not an ordinary function?

The idea behind distributions is to stop asking for the value of the object at a point and ask instead what it does when we test it against a smooth function. A delta concentrated at zero takes a smooth test function and returns that test function's value at zero. It is a linear measurement. We do not need to pretend the delta is an infinitely tall function.

The test functions are smooth and have compact support. Compact support means each test function vanishes outside some bounded region. We choose them because we can differentiate them as many times as needed, and when we integrate by parts their boundary terms disappear. A distribution is a continuous linear functional on this test-function space, with its special topology. The topology matters, but a first example makes the idea tangible.

Any locally integrable function f defines a distribution. Given a test function phi, multiply f by phi and integrate. If two functions agree almost everywhere, they define the same distribution. So distributions already contain the usual Lebesgue-function world. They simply give us a new way to describe what an object does rather than how it looks point by point.

Now take the step function that is zero on the negative half-line and one on the positive half-line. Classically its derivative is zero everywhere except at zero, where the derivative does not exist. But its height changes by one, and we would like the derivative to record that total jump. The distributional derivative does exactly that.

Here is the definition. The derivative of a distribution acts on a test function by taking the negative of the original distribution applied to the derivative of the test function. Why the minus sign? For ordinary smooth functions, integration by parts moves the derivative from one factor to the other and introduces a minus sign. We adopt that identity as the definition even when the original object is not differentiable in the classical sense.

Apply this rule to the step function. The result is minus the integral from zero to infinity of the derivative of phi. Since phi eventually vanishes, this equals phi at zero. But that is precisely what the delta distribution does. So the derivative of a unit step is a delta. A jump in position is recorded as an impulse in the derivative.

Try the absolute value function. It has a corner at zero. Its ordinary first derivative is minus one on the negative half-line and plus one on the positive half-line. That first derivative exists as an ordinary locally integrable function, so it also defines a distribution. Differentiate again using the distribution rule. The sign function jumps by two at zero, so its distributional derivative is twice the delta. The second derivative of absolute value is therefore twice a delta, not a classical function.

A related example comes from three-dimensional electrostatics, but it is simplest to hear in one dimension. A sharply localized source can create a potential that is continuous but has a kink. Differentiation once gives a change of slope; differentiation twice detects the localized source. That is the prototype for the Green-function method in differential equations: a fundamental solution is something whose differential operator produces a delta.

The Fourier transform fits this language. A delta at zero transforms into the constant function one under the convention without a normalization factor in the forward transform. This says a perfectly localized impulse contains all frequencies equally. Conversely, a constant signal has its Fourier transform concentrated at zero frequency, in the distributional sense. The location-frequency trade-off has reached its limiting case.

Distributional derivatives have another advantage: every distribution can be differentiated as many times as desired. But this does not mean every distribution has an ordinary derivative, nor that all these derivatives are functions. A useful question is whether a distributional derivative happens to be represented by an integrable or square-integrable function. If it is, we can begin to measure regularity, which will lead to Sobolev spaces.

Sometimes distributions are also called generalized functions. The term can mislead us into treating every distribution as if it had pointwise values. Most do not. We can evaluate a distribution on test functions and combine it with smooth coefficients; multiplying two arbitrary distributions is not generally defined. For example, the product of two delta distributions at the same point has no canonical value in standard distribution theory. This is a genuine obstacle in nonlinear partial differential equations, not a notation problem.

How should we interpret a differential equation in this language? Suppose a rough u and a source f satisfy an equation involving a derivative. We test the equation against every smooth compactly supported phi. Then we move the derivatives off u and onto phi by integration by parts. If the resulting equality holds for all test functions, we say the equation holds in the distributional sense. This can make sense even when u cannot be differentiated pointwise.

The central shift is from asking whether a formula holds at each point to asking whether every smooth probe detects the same result. For well-behaved functions, the two viewpoints agree. For jumps, concentrated sources, and rough solutions, the distributional viewpoint retains precisely the information that classical differentiation would otherwise lose.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The test-function space \(\mathcal D(\Omega)=C_c^\infty(\Omega)\) has its usual locally convex topology. A distribution \(T\in\mathcal D'(\Omega)\) is a continuous linear functional. Each \(f\in L^1_{\mathrm{loc}}(\Omega)\) gives \(T_f(\varphi)=\int_\Omega f\varphi\).

For a multiindex \(\alpha\), \(\langle\partial^\alpha T,\varphi\rangle=(-1)^{|\alpha|}\langle T,\partial^\alpha\varphi\rangle\). On \(\mathbb R\), \(\langle\delta_0,\varphi\rangle=\varphi(0)\), \(H(x)=\mathbf1_{(0,\infty)}(x)\), and
\[H'=\delta_0,\qquad (|x|)'=\operatorname{sgn}x,\qquad (|x|)''=2\delta_0\]
in \(\mathcal D'(\mathbb R)\).

For Schwartz-tempered distributions \(\mathcal S'\), Fourier transform extends by duality. With \(\widehat f(\xi)=\int f(x)e^{-ix\xi}\,dx\), one has \(\widehat{\delta_0}=1\) and \(\widehat{1}=2\pi\delta_0\), where identities are distributional.

**Caution:** Arbitrary products \(ST\) of distributions are not defined in ordinary distribution theory. Multiplication by \(a\in C^\infty\) is defined by \(\langle aT,\varphi\rangle=\langle T,a\varphi\rangle\).

### Exercises with answers

1. **Point force.** Compute \(\langle 3\delta_2,\varphi\rangle\). **Answer:** \(3\varphi(2)\).
2. **Jump of size c.** Find the distributional derivative of \(cH(x-a)\). **Answer:** \(c\delta_a\).
3. **Polynomial.** What is the distributional derivative of \(x^2\)? **Answer:** The regular distribution associated with \(2x\), because integration by parts holds.

### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)
