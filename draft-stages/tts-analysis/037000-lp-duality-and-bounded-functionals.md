# 037000 — The Dual View of a Function: Linear Measurements and L-p Duality

**Track:** Analysis from First Principles. **Background:** Lebesgue integration, Hölder's inequality, L-p completeness, and basic Hilbert geometry. **Question:** If a measurement of a function is linear and stable under small L-p changes, must it be an integral against another function?

<!-- BEGIN SPOKEN LECTURE -->

# The Dual View of a Function: Linear Measurements and L-p Duality

Suppose a sensor takes a signal, gives a single number, and reacts linearly. If you double the signal, the reading doubles. If you add two signals, their readings add. The sensor is not required to show you every value of the signal. It might measure an average, detect a frequency, compare the signal with a template, or weight one portion of the interval more heavily than another. Mathematically, it is a linear functional: a map from a space of functions to the real or complex numbers.

Linearity is only half the specification. We also want the sensor to be stable. If two functions are close in the norm we chose, their readings should be close. A measurement that sends arbitrarily small inputs to readings of arbitrarily large size cannot be reliably used with approximations.

Here is a first example. On the unit interval, assign to each integrable function its ordinary average. Two signals that are close in total absolute error must have close averages. Indeed, the absolute difference of the averages is at most the integral of the absolute difference. So averaging is linear and continuous on L-one.

Now try a different measurement: ask for the value of the signal exactly at the midpoint. For continuous functions this question has meaning, but on L-one, functions are identified whenever they agree almost everywhere. Two representatives can differ at the midpoint and still be the same L-one element. So the measurement is not even well-defined on L-one. On continuous functions equipped with the L-one norm, it is well-defined but not continuous: a narrow triangle of height one at the midpoint has value one there while its integral tends to zero.

This difference is the beginning of duality. We will ask not just which functions are in a space, but which continuous linear measurements can be made on that space. The collection of all such measurements is itself a normed vector space, called the continuous dual.

## The norm of a measurement

For a continuous linear functional, ask how large its reading can be when the input has norm at most one. The supremum of those absolute readings is its operator norm. If this supremum is finite, the measurement is bounded. Here bounded and continuous are equivalent, because of linearity.

Think of calibrating an instrument with unit-size test inputs. If the readings are all bounded by some number M, then for an arbitrary input, scaling it down to unit size shows its reading is bounded by M times the input norm. Conversely, if a linear measurement is continuous at zero, then some small ball has readings below one; rescaling yields a bound everywhere. We do not need a separate continuity check for every possible input.

In a function space, some especially natural measurements take the form of an integral. Choose a weight function g, multiply the signal f by that weight, and integrate. If the functions are complex-valued, we will conjugate g in this pairing. The conjugation matches the inner-product convention in which the first argument is linear.

Which weights produce bounded measurements? Hölder's inequality answers this immediately. If f is in L-p and g is in the corresponding L-q space, where the reciprocals of p and q add to one, then the integral of their product exists absolutely. Its absolute value is at most the L-p norm of f times the L-q norm of g. Thus every g in L-q defines a bounded linear functional on L-p.

But that only constructs a family of measurements. The interesting question is whether we have found all of them.

## A small example with an exact answer

Work on the unit interval and take L-two. Imagine that g is twice as large on the left half of the interval as on the right half. The associated measurement favors left-hand signal energy, with signed contributions because it integrates the signal against g. You can choose a signal aligned with g to get the largest possible reading relative to its L-two size.

For a real signal, equality in Cauchy–Schwarz occurs when f is a scalar multiple of g. For a complex signal, alignment also requires the phases to agree. After normalizing to unit L-two norm, the largest reading is the L-two norm of g. So the inequality from Hölder does not merely give a convenient upper bound: it gives the exact norm of the measurement.

The same fact holds for all conjugate exponents. When p is strictly between one and infinity, a weight proportional to the signed magnitude of g raised to the q-minus-one power is the extremizing input, after appropriate normalization. When p equals one, a test function can concentrate in a region where the absolute value of g nearly reaches its essential supremum. We may not have a single maximizing input, but we can make the reading arbitrarily close to the best possible bound. The operator norm is exactly the L-q norm of g in both cases.

For L-two there is an even stronger theorem. Every continuous linear functional is represented by an inner product with a unique element g of L-two. That is the Hilbert-space Riesz representation theorem. The question now is what changes away from p equals two.

## Why every L-p measurement has a weight

There is a remarkable answer. On a sigma-finite measure space, when p is at least one but finite, every continuous linear functional on L-p comes from integration against exactly one function in L-q, up to equality almost everywhere. Here q is the Hölder conjugate of p; when p is one, q means infinity.

The sigma-finite qualification gives us a way to cover the space by countably many sets of finite measure. We will use it to sketch why a function g has to exist, instead of just accepting that the collection of integral measurements happens to be large enough.

First restrict attention to a measurable region of finite measure. Every indicator function of a measurable subset belongs to L-p there. Feed those indicators into the functional, and call the resulting number the measure assigned to the subset. This new set function is countably additive. The reason is that indicators of disjoint unions converge in L-p when the measure of the omitted tail tends to zero. Continuity of the functional transfers that convergence into convergence of readings.

This new measure vanishes on null sets because indicators of null sets represent the zero element of L-p. The Radon–Nikodym theorem now says that the set function has a density with respect to the original measure. That density is our candidate weight. At this stage we know how the functional acts on indicators, and consequently on simple functions.

But the density cannot be an arbitrary integrable function. Continuity of the original measurement forces exactly the stronger L-q condition. To see the mechanism, use a test input that aligns its phase with the density and grows like an appropriate power of its magnitude. Truncate that test so it is bounded and supported on a set of finite measure. The norm bound for the functional then controls the integral of the q-th power of the density. Enlarging the truncations, we obtain a finite L-q norm. In the case p equals one, the same logic says the density must be essentially bounded.

Simple functions are dense in L-p for finite p. Once the equality between the original functional and integration against g holds on simple functions, boundedness makes it hold for all of L-p. On a sigma-finite space the densities constructed on finite-measure pieces agree where the pieces overlap, so they combine into one global g. This gives both existence and uniqueness.

This is a substantial representation theorem. Its point is not that we guessed a sensible integral formula. Its point is that under the hypotheses, there are no other bounded linear measurements hiding elsewhere in the dual space.

## The endpoints are not interchangeable

You might now expect that exchanging p and q always produces the same statement. If the dual of L-one is L-infinity, perhaps the dual of L-infinity is L-one. That conclusion is false on many measure spaces, including counting measure on the natural numbers.

On that space, L-infinity is the space of bounded sequences. A summable sequence g does define a bounded functional by multiplying coordinates and adding the results. But bounded sequences admit linear measurements that cannot be represented by a summable list of coordinate weights.

One example comes from ordinary limits. On the smaller space of convergent bounded sequences, sending a sequence to its limit is a bounded linear functional of norm one. There are ways to extend it to all bounded sequences without increasing its norm; we will study the extension principle in the Hahn–Banach theorem. Such an extension assigns one to the constant sequence of ones, yet assigns zero to every sequence that is one at a single coordinate and zero elsewhere. If it were given by a summable sequence of weights, each of those tests would force the corresponding weight to vanish. All weights would be zero, contradicting the reading of one on the constant sequence. So the entire dual of L-infinity is generally larger than L-one.

The endpoint asymmetry is not a technical inconvenience. It marks a change in what counts as a continuous linear measurement. For one through finite p, integration captures the whole dual under our sigma-finite assumption. At infinity, there can be additional measurements with no ordinary integrable density.

## Duality as a change in viewpoint

The dual space gives us a way to study a function by asking all stable linear questions about it. We can measure averages, correlations, local weighted responses, or generalized observations without insisting on pointwise values. A function becomes an object characterized by how every allowable measurement responds to it.

This viewpoint also helps explain why L-two is geometrically comfortable. Its continuous dual is itself, through the inner product. Other L-p spaces with p strictly between one and infinity come in conjugate pairs. L-one and L-infinity behave differently at the edge. The geometry of the function space determines the possible measurements, and the possible measurements tell us about the geometry.

One question remains. We have spent this lecture measuring functions with scalar outputs. What if the input and output are both vectors or functions? Then a measurement becomes an operator. We will need to distinguish linear maps that are stable from those that are not, and learn how to measure the size of an operator itself. The same boundedness idea will guide us, but the objects will be able to transform entire spaces rather than producing one number.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Dual norm and integral pairing

Let \(X\) be a normed space over \(\mathbb K\in\{\mathbb R,\mathbb C\}\). Its continuous dual is
\[
X^* = \{\Lambda:X\to\mathbb K :\Lambda\text{ is linear and continuous}\},
\qquad \|\Lambda\|=\sup_{\|x\|\le1}|\Lambda x|.
\]
For \(1\le p<\infty\), let \(1/p+1/q=1\), including \(q=\infty\) for \(p=1\). On a sigma-finite measure space,
\[
(L^p(\mu))^*\cong L^q(\mu),\qquad
\Lambda_g(f)=\int f\,\overline g\,d\mu,\qquad
\|\Lambda_g\|=\|g\|_q.
\]
The identification is conjugate-linear in \(g\) with this complex pairing convention; one can instead use \(\int fg\) for a linear identification. Elements are unique modulo a.e. equality. For \(1<p<\infty\), the standard duality theorem holds for arbitrary measure spaces; sigma-finiteness is used here to present a unified proof including \(p=1\).

### Norm equality for \(1<p<\infty\)

For \(g\in L^q\) with \(g\ne0\), take
\[
f=\frac{\operatorname{sgn}(g)|g|^{q-1}}{\|g\|_q^{q-1}},
\quad\operatorname{sgn}(g)=\begin{cases}g/|g|&g\ne0\\0&g=0.\end{cases}
\]
Then \(\|f\|_p=1\) because \((q-1)p=q\), and
\(\Lambda_g(f)=\|g\|_q\). For \(p=1\), approximate the essential supremum of \(|g|\) by normalized indicator tests on finite positive-measure subsets of \(\{|g|>\|g\|_\infty-\varepsilon\}\); sigma-finiteness supplies such a subset.

### Representation proof skeleton and its prerequisites

For \(\mu(E)<\infty\), set \(\nu(E)=\Lambda(\mathbf1_E)\). This is countably additive by \(L^p\)-convergence of indicators under disjoint unions, and \(\nu\ll\mu\). Restricted to each finite-measure set, \(\nu\) is a finite complex/signed measure, so Radon–Nikodym gives a density. A countable exhaustion patches densities. For \(p>1\), test on finite-measure sets against bounded truncations of \(\operatorname{sgn}(g)|g|^{q-1}\) to obtain \(\int|g|^q\le\|\Lambda\|^q\); for \(p=1\), testing the set where \(|g|>\|\Lambda\|+\varepsilon\) forces \(|g|\le\|\Lambda\|\) a.e. Density of simple functions finishes.

This outline *uses* Radon–Nikodym, not a proof of that theorem. An independent development of Radon–Nikodym is appropriate later in the curriculum.

### Why the infinity dual can be larger

Take \(X=\ell^\infty\), \(c\subset X\) the convergent sequences, and \(L:c\to\mathbb R\), \(L(x)=\lim_n x_n\). This is bounded with norm one. Hahn–Banach provides \(\widetilde L\in X^*\), \(\|\widetilde L\|=1\), extending \(L\). Since each standard coordinate vector \(e_n\) converges to zero, \(\widetilde L(e_n)=0\). Since \(\widetilde L(\mathbf1)=1\), no representation \(\widetilde L(x)=\sum_n a_nx_n\), \(a\in\ell^1\), is possible. This does not require choosing a shift-invariant Banach limit.

### Exercises and answers

1. **Evaluation in \(L^1\):** Show point evaluation does not descend to \(L^1([0,1])\). **Answer:** The indicators of a singleton and the zero function are the same \(L^1\) element but differ at that singleton.
2. **A finite-dimensional dual:** For \(\ell^p_2=(\mathbb R^2,\|\cdot\|_p)\), find the norm of \(\Lambda(x_1,x_2)=2x_1-x_2\) for \(p=1,2,\infty\). **Answer:** The dual norms are \(2,\sqrt5,3\), respectively.
3. **Sharp Hölder:** For \(g(x)=x\) in \(L^2([0,1])\), find the unit-norm input maximizing \(\int_0^1 f(x)g(x)\,dx\). **Answer:** \(f(x)=\sqrt3\,x\); the maximum is \(1/\sqrt3\).
4. **The endpoint trap:** Explain why \((L^\infty)^*=L^1\) is false for counting measure on \(\mathbb N\). **Answer:** Use the extension of ordinary limits from convergent sequences as above.

### References

- Sheldon Axler, *Measure, Integration & Real Analysis* (open access): https://measure.axler.net/.
- Terence Tao, *245B, Notes 6: Duality and the Hahn–Banach theorem*: https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/.
- MIT OpenCourseWare, *18.102 Introduction to Functional Analysis*, lectures on bounded operators and dual spaces: https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/.
