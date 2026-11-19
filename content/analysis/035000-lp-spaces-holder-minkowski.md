# 035000 — Measuring Functions: L-p Spaces, Hölder, and Minkowski

**Track:** Analysis from First Principles. **Background:** Lebesgue integration, almost-everywhere equivalence, and convergence theorems. **Question:** How can we measure the size of a whole function, and what inequalities turn those measurements into geometry?

<!-- BEGIN SPOKEN LECTURE -->

# Measuring Functions: L-p Spaces, Hölder, and Minkowski

A number has a size. A vector has a length. But how should we measure the size of a function?

One possible answer is to look at its largest absolute value. This is natural if you want to guarantee that an error never exceeds a tolerance. A second answer is to add its absolute value over the domain. That measures total unsigned error. A third is to square the absolute value, integrate, and take a square root. That gives extra weight to large deviations and is intimately connected with geometry, least squares, and orthogonality.

These are not three unrelated tricks. They belong to a family of spaces conventionally called L-p spaces. The letter p records which power of the absolute value we measure. This family will let us talk about convergent sequences of functions as geometrical objects, not just as separate formulas defined at every point.

The central challenge is that the integral alone does not automatically give a norm, a notion of length satisfying the triangle inequality. For that we need two inequalities: Hölder's inequality, which controls the integral of a product, and Minkowski's inequality, which controls the size of a sum. We will build the spaces, prove the inequalities, and see why functions that differ only on null sets must be treated as the same element.

## Three ways to measure one signal

Imagine a signal defined on the unit interval. It is zero most of the time, but on an interval of length one hundredth it jumps to height ten. Its maximum height is ten. Its total absolute area is one tenth. The integral of its square is one, so its square-integral size is one after taking the square root.

Each measurement tells a different story. The maximum detects the worst instantaneous deviation. The absolute area records accumulated deviation. The squared size penalizes large excursions more severely than small ones. A rare but tall spike can be nearly invisible to one metric and conspicuous in another.

For a measurable function f and a real number p at least one but less than infinity, take the absolute value of f, raise it to the pth power, integrate, and then take the pth root. If the integral is finite, we say f belongs to L-p. For p equal to one, this is total absolute mass. For p equal to two, it is the square root of total squared mass.

At the endpoint called L-infinity, we use a different definition: the *essential supremum* of the absolute value. This is the least bound that works outside some null set. If a function is five at one isolated point and zero everywhere else, its ordinary supremum is five, but its essential supremum is zero. For integration and approximation, the exceptional point carries no weight.

That observation reveals a subtle issue. A function that is nonzero at only one point can have L-one size zero. But a genuine norm must be zero only for the zero object. The solution is not to ban such functions. Instead, L-p treats two measurable functions as the same element when they agree almost everywhere. An element of L-p is therefore an equivalence class of functions, not a particular list of values at every point.

Once we identify almost-everywhere equal functions, these sizes can become honest norms. In L-infinity the measure-theoretic maximum replaces the pointwise maximum, and changing an individual representative on a null set changes nothing.

## The first inequality comes from a product

Why should integration of a product be controlled by the individual sizes of the factors? Suppose you are measuring the interaction between two signals. If one is large precisely where the other is large, their product can be substantial. But a certain balance between the sizes of the two signals gives an upper limit on the total interaction.

Let p be greater than one, and choose a companion exponent q so that one over p plus one over q equals one. These exponents are called conjugate. For example, when p equals two, q also equals two. When p equals three, q equals three halves.

Hölder's inequality says that the integral of the absolute product of f and g is no greater than the L-p size of f times the L-q size of g. Both sizes have to be finite. The resulting product is a useful numerical estimate even if the integral of the product is impossible to evaluate explicitly.

To see the reason, first normalize. If either norm is zero, the inequality is immediate because that function vanishes almost everywhere. Otherwise, divide f by its L-p norm and g by its L-q norm. The integrals of the pth and qth powers of these normalized functions are both one.

Now use an elementary numerical inequality: for nonnegative a and b, the product a times b does not exceed a to the pth power divided by p plus b to the qth power divided by q. This is Young's inequality for conjugate powers, a consequence of convexity. Apply it pointwise to the normalized absolute functions. Integrate. The right side becomes one over p plus one over q, which is one. Undo the normalization and Hölder's inequality follows.

There is something instructive about this proof. The geometry of functions came from a one-line inequality for real numbers, applied at every point and summed by integration. The exponents are not arbitrary bookkeeping: the conjugate relationship is exactly what makes the two normalized power integrals combine to one.

At the endpoints, the partner of L-one is L-infinity. If g is essentially bounded, the integral of the product is at most the essential maximum of g times the integral of the absolute value of f. That is the endpoint Hölder inequality, and it needs no finite measure assumption.

When both exponents are two, Hölder becomes the Cauchy–Schwarz inequality: the integral of a product is controlled by the product of the square-root-of-square-integral sizes. This will become the defining control inequality for an inner product in L-two.

## The triangle inequality for functions

Now turn to sums. We know the pointwise triangle inequality: the absolute value of f plus g is at most the absolute value of f plus the absolute value of g. But if we raise both sides to a power and integrate, the desired triangle inequality for the L-p sizes does not immediately fall out. We need one more step.

Minkowski's inequality says that the L-p size of a sum is no greater than the sum of the L-p sizes. It is the analog of the familiar statement that the length of one side of a triangle cannot exceed the lengths of the other two combined.

For p equal to one, this follows immediately by integrating the pointwise triangle inequality. For p equal to infinity, it follows from taking essential suprema. The interesting case is p strictly between one and infinity.

Suppose f and g belong to L-p, and write h for their sum. Begin with the pth power of the absolute value of h. It is the absolute value of h times its own absolute value to the power p minus one. Use the pointwise bound on the first factor to split the integral into two terms: one involving the absolute value of f times the remaining power of h, and one involving g times that power.

Apply Hölder's inequality to each term. The first contributes no more than the L-p norm of f times the p-minus-one power of the L-p norm of h. The second contributes the analogous term involving g. Add them. If h is not the zero element, divide by the common power of its norm. You obtain exactly Minkowski's inequality.

One technical detail deserves explicit attention: before dividing, we must know that h has finite L-p size. It does, because the pth power of the sum's absolute value is bounded by a constant depending only on p times the sum of the pth powers of the individual absolute values. The two integrals are finite. This preliminary estimate avoids a circular proof.

The conclusion is that L-p has all three properties of a norm: nonnegative length, zero length only for the zero almost-everywhere class, and the triangle inequality. Scalar multiplication behaves as expected as well. With a notion of distance defined by the norm of the difference, we can now ask whether a sequence of functions converges in L-p without asking for pointwise convergence.

## Functions can be close in one sense and far in another

Return to a spike on the unit interval. Give it height n and width one over n squared. Its total absolute area is one over n, so its L-one norm tends to zero. But the integral of its square equals one; its L-two norm is always one. Its essential maximum is n, which tends to infinity. The very same function sequence approaches zero in L-one, does not approach zero in L-two, and becomes unbounded in L-infinity.

This is not a paradox. Each norm answers a different approximation question. L-one says the total absolute discrepancy disappears. L-two says the total squared discrepancy does not. L-infinity says the worst local error grows. When someone claims that a sequence of functions converges, it is essential to ask *in what sense*.

On a finite-measure domain, there is a useful ordering. If q is larger than p, belonging to L-q implies belonging to L-p. Hölder's inequality proves an estimate involving the total measure of the domain. A stronger power-integrability assumption buys control of a weaker one. On an infinite-measure domain, this containment need not hold. A function may decay just fast enough to belong to one L-p space and not another, and behavior near zero can favor one exponent while behavior at infinity favors a different exponent.

For example, on the interval between zero and one, consider the function one divided by x to a positive power alpha. Its pth power integrates near zero precisely when alpha times p is less than one. A small change in p can therefore move the function across the border between finite and infinite norm. L-p spaces classify singularities by how much integrable power they can carry.

## Why p starts at one

We chose p at least one for a reason. One can still integrate the pth power of the absolute value when p lies between zero and one, but the pth-root construction no longer satisfies the usual triangle inequality. Take two functions supported on disjoint sets, each with the same p-size one. Their sum has p-size two to the power one over p. Since one over p exceeds one, that number is greater than two, violating the triangle inequality.

There are useful spaces with exponents below one, and they carry a different kind of geometry, often called quasi-norm geometry. But the ordinary normed-space theory we are building begins at p equals one. The distinction is structural, not a convention chosen for convenience.

## A bridge to approximation and duality

Hölder and Minkowski have immediate consequences. If we approximate an integrable function by a simpler one in L-p, then any linear functional formed by multiplying by an L-q function and integrating is continuous: Hölder bounds the error in the functional by the L-p approximation error times the L-q norm of the test function.

That observation foreshadows dual spaces, which study all continuous linear measurements of a function. For suitable measure spaces and exponents between one and infinity, such measurements are represented by L-q functions. Endpoint cases require care, especially the dual of L-infinity, which is generally larger than L-one. We are not proving the full duality theorem here, but we can already see why conjugate exponents arise naturally.

One step is still missing before L-p deserves to be treated like Euclidean space. If functions become closer and closer in L-p, is there necessarily a function in L-p they are approaching? A normed space with that property is called complete. Completeness is what lets us pass from finite approximations to genuine infinite limits without stepping outside the space. We will prove it directly, then use the special geometry of L-two to understand orthogonal projections and Fourier coefficients.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Definitions and equivalence classes

On a measure space \((X,\Sigma,\mu)\), for \(1\le p<\infty\) define

\[
L^p(X,\mu)=\{[f]:f\text{ measurable},\ \int_X|f|^p\,d\mu<\infty\},\qquad
\|f\|_p=\left(\int_X|f|^p\,d\mu\right)^{1/p}.
\]

Classes \([f]\) identify functions equal \(\mu\)-almost everywhere. The space \(L^\infty\) consists of a.e.-bounded measurable functions with norm \(\operatorname{ess\,sup}|f|\). Scalars may be real or complex.

### Hölder's inequality

If \(1<p,q<\infty\) and \(p^{-1}+q^{-1}=1\), then

\[
\int_X|fg|\,d\mu\le\|f\|_p\|g\|_q.
\]

Young's inequality \(ab\le a^p/p+b^q/q\), applied to \(a=|f|/\|f\|_p\) and \(b=|g|/\|g\|_q\), and integrated, gives the proof. If a norm vanishes, the result is immediate. The endpoint \((p,q)=(1,\infty)\) follows from \(|fg|\le\|g\|_\infty|f|\) a.e.

### Minkowski's inequality

For \(1\le p\le\infty\),

\[
\|f+g\|_p\le\|f\|_p+\|g\|_p.
\]

For \(1<p<\infty\), let \(h=f+g\). First \(|h|^p\le2^{p-1}(|f|^p+|g|^p)\), so \(h\in L^p\). Then

\[
\|h\|_p^p\le \int |f||h|^{p-1}+\int |g||h|^{p-1}
\le(\|f\|_p+\|g\|_p)\|h\|_p^{p-1}.
\]

Divide when \(\|h\|_p\neq0\). Cases \(p=1,\infty\) are direct. Together with definiteness on equivalence classes, this makes \(L^p\) a normed vector space.

### Finite-measure inclusion and singular examples

If \(\mu(X)<\infty\) and \(1\le p<q\le\infty\), then

\[
\|f\|_p\le\mu(X)^{1/p-1/q}\|f\|_q,
\]

with \(1/\infty=0\). On \((0,1)\), \(f(x)=x^{-\alpha}\) lies in \(L^p\) exactly when \(\alpha p<1\). No universal inclusion \(L^p\subset L^q\) or \(L^q\subset L^p\) holds on arbitrary infinite-measure spaces.

For \(0<p<1\), choose disjoint sets of measure one and take their indicators \(f,g\). Then \(\|f\|_p=\|g\|_p=1\), but \(\|f+g\|_p=2^{1/p}>2\).

### Exercises with answers

1. **Spikes across norms:** Let \(f_n=n1_{(0,n^{-2})}\) on \((0,1)\). Find the \(L^1\), \(L^2\), and \(L^\infty\) sizes. **Answer:** \(n^{-1}\), \(1\), and \(n\), respectively.
2. **Conjugate powers:** Find \(q\) for \(p=4\). **Answer:** \(q=4/3\).
3. **An integral pairing:** Show \(|\int_0^1 f(x)g(x)\,dx|\le\|f\|_2\|g\|_2\). **Answer:** \(|\int fg|\le\int|fg|\), then Hölder with \(p=q=2\).
4. **Finite measure:** Prove \(\|f\|_1\le\|f\|_2\) on \([0,1]\). **Answer:** Apply Hölder to \(|f|\cdot1\), and \(\|1\|_2=1\).
5. **Null sets:** Why must \(1_{\{1/2\}}\) represent zero in \(L^p([0,1])\)? **Answer:** It vanishes almost everywhere, so its integral norm is zero.

### Sources

- MIT OpenCourseWare, *18.125 Measure and Integration*, lectures 14–17 (Hölder, Minkowski, L-p definitions and inclusions): https://ocw.mit.edu/courses/18-125-measure-and-integration-fall-2003/pages/lecture-notes/.
- Sheldon Axler, *Measure, Integration & Real Analysis*, chapters on L-p spaces and functional analysis: https://measure.axler.net/.
- Terence Tao, *An Introduction to Measure Theory*, L-p estimates and measure-theoretic inequalities: https://terrytao.wordpress.com/books/an-introduction-to-measure-theory/.
