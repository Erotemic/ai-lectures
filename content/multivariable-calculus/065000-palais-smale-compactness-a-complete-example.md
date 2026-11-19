# Palais–Smale Compactness: A Complete Nonlinear Boundary-Value Example

**Track:** Multivariable Calculus from First Principles. **Focus:** checking mountain-pass geometry, bounding almost-critical sequences, one-dimensional Sobolev compactness, strong convergence, and nontrivial weak-solution existence.

<!-- BEGIN SPOKEN LECTURE -->

# Palais–Smale Compactness: A Complete Nonlinear Boundary-Value Example

The mountain-pass theorem can guarantee a critical point of an energy, but only if a suitable almost-critical sequence has a strongly convergent subsequence. That condition is called Palais–Smale compactness. It is easy to state, and easy to leave as a black box. This lecture will not leave it there. We will verify the condition step by step for an explicit nonlinear boundary-value problem.

Our problem is set on the interval from zero to pi. Seek a function u, equal to zero at both endpoints, such that its negative second derivative equals u cubed. Zero is an obvious solution. We want to prove that a nonzero solution exists, without guessing its formula.

The energy is one half of the integral of the squared slope, minus one quarter of the integral of u to the fourth power. We will first check that the energy has a positive barrier around zero and becomes negative along a particular path. Then we will confront the central difficulty: an almost-critical sequence might have wildly varying shapes, and a sequence of functions is not guaranteed to converge merely because some of its integrals are bounded.

## What counts as an admissible shape?

For a fixed-endpoint string, an appropriate space is the collection of functions with square-integrable first weak derivative and zero values at the endpoints. Mathematicians call it H zero one of the interval, or H naught one. The norm we use is the square root of the integral of the squared derivative.

Why not insist on twice differentiable functions at the beginning? Because the energy uses only the first derivative. Minimizing or finding critical points in a smaller, unnecessarily smooth space can make the existence argument fail for artificial reasons. The energy space is large enough to admit limits while retaining exactly the derivatives the energy needs.

On this interval, a function in our energy space has a continuous representative. Its value at a point equals the integral of its derivative from the left endpoint. The Cauchy–Schwarz inequality therefore says that its absolute value is at most the square root of pi times the slope norm. This single estimate already controls the nonlinear term: the integral of the fourth power of u is at most pi cubed times the fourth power of the slope norm.

The numerical constant is not sharp, and it does not need to be. What matters is the difference of powers. If the slope norm t is small, the energy is at least one half t squared minus pi cubed divided by four times t to the fourth. A positive quadratic dominates a quartic near zero. So choose a sufficiently small positive radius in the energy norm. On the sphere with that radius, energy is bounded below by one positive number. That is our mountain-pass barrier.

## A path whose energy eventually drops

Take the shape sine of x. It vanishes at zero and pi and is clearly not the zero function. Consider all its multiples: t times sine of x, with t ranging from zero upward. The energy along this one-dimensional path is an explicit quartic polynomial in t.

The integral of cosine squared over the interval is pi divided by two. The integral of sine to the fourth power is three pi divided by eight. Substituting into the energy gives pi over four times t squared, minus three pi over thirty-two times t to the fourth.

Near t equal to zero, that expression is positive. At t equal to two, it is negative pi divided by two. So the path connects the zero shape to a negative-energy shape outside the small sphere.

We can also locate its highest point. Differentiate the polynomial in t. Apart from t equal to zero, its maximum occurs when t squared equals four thirds. The corresponding energy is pi divided by six. The true mountain-pass level is the least possible maximum across every path, not only this sine-wave path. We have not computed that true level. But we do know it is positive and no larger than pi divided by six. Both facts will be useful.

The geometry is established. Now let us check compactness.

## Start with an almost-critical sequence

Suppose we have a sequence of shapes whose energies approach some finite number, and whose first variations become small in norm. This is what the theorem will produce at the mountain-pass level. Our job is to show that such a sequence has a subsequence converging strongly in the slope norm.

A warning first: the energy itself does not obviously bound the slope norm. It contains a positive quadratic term and a negative quartic term. If both become very large, their difference might stay bounded. To rule that out, we combine the energy with its derivative.

The derivative of our energy, evaluated in the direction u itself, equals the integral of the squared slope minus the integral of u to the fourth power. Subtract one quarter of this derivative value from the energy. The quartic terms cancel exactly. What remains is one quarter of the slope norm squared.

This is the decisive algebraic identity. Applied to a nearly critical function, it says that one quarter of its slope norm squared equals its bounded energy, minus one quarter of a small derivative functional acting on that function. The final term can be bounded by the derivative norm times the slope norm. So if the slope norm were to grow without bound, a quadratic quantity would be bounded by a constant plus a quantity only linear in that norm, with a coefficient tending to zero. That is impossible.

We have proved that the almost-critical shapes are bounded in the energy space.

## Weak limits and a compactness upgrade

A bounded sequence in this Hilbert space has a weakly convergent subsequence. Weak convergence means that continuous linear measurements, including integrals of the derivative against any fixed square-integrable test function, approach the corresponding measurements of a limiting function u.

Weak convergence is not enough for our nonlinear term. To handle u cubed, we use a special feature of one dimension. The Cauchy–Schwarz inequality applied between two positions says that the change in u between those positions is bounded by the square root of their distance times the slope norm. Because the slope norms of our sequence are uniformly bounded, the functions are uniformly bounded and uniformly equicontinuous.

Arzelà–Ascoli tells us that a subsequence converges uniformly to a continuous function. We can select it from the weakly convergent sequence, so the uniform limit is the same u. Uniform convergence means that the cubic powers also converge uniformly. This lets us pass to the limit in the weak equation. The result is that u itself is stationary: its first variation vanishes for every admissible test function.

But we promised strong convergence in the energy norm, not just uniform convergence of the values. There is one more step.

Test the almost-critical derivative at the n-th function against the difference between that function and the limit. Because the derivative norm tends to zero and the differences have bounded energy norm, the resulting number tends to zero. Expand the expression. It is the integral of the n-th slope times the difference of slopes, minus the integral of the n-th function cubed times the difference of functions.

The second integral tends to zero by uniform convergence. The first therefore tends to zero. By weak convergence, the cross term involving the n-th slope and the limiting slope approaches the integral of the limiting slope squared. Consequently, the squared norms of the n-th slopes converge to the squared norm of the limiting slope.

In a Hilbert space, weak convergence plus convergence of norms implies strong convergence. So the slopes converge in square-integral norm. This is precisely the Palais–Smale compactness we needed.

## The existence result

Now combine the pieces. The energy is continuously differentiable on the fixed-endpoint energy space. It has a positive barrier on a small sphere around zero. The sine-wave path reaches a negative-energy shape outside that sphere. And every sequence with bounded energy and vanishing derivative has a strongly convergent subsequence.

The mountain-pass theorem therefore gives a critical function u whose energy is positive. It cannot be identically zero, because the zero function has energy zero. This critical function is a nontrivial weak solution of negative u double prime equals u cubed, with zero endpoint values.

The weak solution is actually more regular. In one dimension the function is continuous, so its cube is continuous. The equation then tells us its second weak derivative is continuous. Standard one-dimensional regularity upgrades u to a twice continuously differentiable classical solution. We did not have to require that smoothness in advance.

This proof does not tell us the exact shape of u. It does not claim uniqueness. In fact the equation is unchanged if we replace u by negative u, so every nonzero solution has a sign-reversed companion. The theorem has established existence, not a complete classification of solutions.

## Why the proof worked here

We should name the parts that were specific to this example. The quartic nonlinearity allowed a cancellation between energy and derivative that bounded the Palais–Smale sequence. The finite interval and one spatial dimension supplied compact convergence for bounded-energy functions. The cubic term then behaved well under limits. Finally, the structure of the derivative converted weak convergence into strong convergence of the slopes.

If we change the dimension or the nonlinearity, some of these steps may break. In higher dimensions, controlled slopes do not always imply uniformly convergent functions. There is a threshold exponent at which concentration can preserve both derivative energy and nonlinear mass while the functions themselves approach zero almost everywhere. At that threshold, the compactness proof we just used cannot be copied.

For now we have something complete: a nonzero nonlinear boundary-value solution proved to exist by an explicit energy argument, not by guessing its formula, and with the compactness hypothesis verified rather than assumed. That is the working power of the mountain-pass method.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Setup and geometry

Let \(H=H_0^1(0,\pi)\), \(\|u\|=\|u'\|_{2}\), and
\[
 J(u)=\frac12\|u'\|_2^2-\frac14\|u\|_4^4,
 \quad J'(u)[v]=\int_0^\pi u'v'-\int_0^\pi u^3v.
\]
By Cauchy–Schwarz and the zero trace,
\[
 \|u\|_\infty\leq\sqrt\pi\|u'\|_2,
 \qquad \|u\|_4^4\leq\pi^3\|u'\|_2^4.
\]
On the sphere \(\|u\|=r=\pi^{-3/2}\),
\[
 J(u)\geq\frac12r^2-\frac{\pi^3}{4}r^4=\frac1{4\pi^3}>0.
\]
For \(\phi(x)=\sin x\),
\[
 J(t\phi)=\frac\pi4t^2-\frac{3\pi}{32}t^4,
 \quad \max_{t\in[0,2]}J(t\phi)=\frac\pi6
 \quad\text{at}\quad t=2/\sqrt3,
\]
and \(J(2\phi)=-\pi/2\). Hence the mountain-pass minimax level satisfies \(1/(4\pi^3)\leq c\leq\pi/6\).

### Palais–Smale bound

Suppose \(J(u_n)\to c\in\mathbb R\) and \(\delta_n:=\|J'(u_n)\|_{H^*}\to0\). Then
\[
 J(u_n)-\frac14J'(u_n)[u_n]=\frac14\|u_n\|^2.
\]
Therefore \(\|u_n\|^2/4\leq C+\delta_n\|u_n\|/4\); the sequence \((\|u_n\|)\) is bounded.

A subsequence converges weakly in \(H\) to some \(u\). The estimate
\[
 |u_n(x)-u_n(y)|\leq \|u_n'\|_2\,|x-y|^{1/2}
\]
and \(\|u_n\|_\infty\leq\sqrt\pi\,\|u_n'\|_2\) give equicontinuity and boundedness. Arzelà–Ascoli yields uniform convergence along a further subsequence. Its limit agrees with the weak \(H\) limit. Thus \(u_n^3\to u^3\) uniformly and \(J'(u)=0\).

Finally,
\[
 J'(u_n)[u_n-u]
 =\int u_n'(u_n'-u')-\int u_n^3(u_n-u)\to0.
\]
The nonlinear integral tends to zero by uniform convergence. Weak convergence gives \(\int u_n'u'\to\|u'\|_2^2\), so \(\|u_n'\|_2^2\to\|u'\|_2^2\). Weak convergence plus convergence of norms in a Hilbert space implies \(\|u_n'-u'\|_2\to0\). This proves \((PS)\) at every finite level for this particular \(J\).

### Exercises with answers

1. **Derivative check.** Compute \(J'(u)[u]\). **Answer:** \(\|u'\|_2^2-\|u\|_4^4\).
2. **Cancellation.** What is \(J(u)-J'(u)[u]/4\)? **Answer:** \(\|u'\|_2^2/4\).
3. **One-mode test.** Where is the maximum of \(J(t\sin x)\) for \(t\ge0\)? **Answer:** \(t=2/\sqrt3\), with value \(\pi/6\).
4. **Compactness.** Why does uniform convergence help the cubic nonlinearity? **Answer:** \(u_n\to u\) uniformly and uniform boundedness imply \(u_n^3\to u^3\) uniformly.
5. **Nontriviality.** Why is the mountain-pass solution nonzero? **Answer:** Its energy \(c\) is strictly positive, whereas \(J(0)=0\).
6. **Sign symmetry.** If \(u\) solves \(-u''=u^3\), what about \(-u\)? **Answer:** It also solves, by oddness of the cubic term.

### Sources and further reading

- [University of Pisa, *Metodi Variazionali*, §§6–7](https://poisson.phc.dm.unipi.it/~fpmaiale/notes/MetodiVariazionali.pdf), compactness and a mountain-pass proof.
- [Wang, *Palais–Smale Approaches*, Electronic Journal of Differential Equations Monograph 6 (2004)](https://ejde.math.txstate.edu/Monographs/06/wang.pdf), semilinear elliptic variational examples.
- [Wikipedia: Sobolev space](https://en.wikipedia.org/wiki/Sobolev_space), energy spaces and weak derivatives.
- [Wikipedia: Arzelà–Ascoli theorem](https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem), the compactness theorem used here.
- Library preparation: `multivariable-calculus:063000`, `064000`, `033000`, `036000`.
