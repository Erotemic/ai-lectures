# 008000 — Interpolation: Why More Data Points Can Make an Approximation Worse

**Track:** Numerical Analysis and Reliable Computation. **Background:** polynomial algebra, functions, elementary derivatives. **Question:** when do exact matches at sampled points provide a trustworthy approximation between the points?

<!-- BEGIN SPOKEN LECTURE -->

# Interpolation: Why More Data Points Can Make an Approximation Worse

Suppose we have measured a function at five locations, and we want its value halfway between two of those locations. One approach is to construct a polynomial that passes through every measured point and evaluate it at the new location. There is a precise theorem that says exactly one polynomial of degree at most four does this, provided the five input locations are distinct.

That sounds reassuring. We have a uniquely determined answer that agrees with every observation. Yet the resulting curve might oscillate between the observations, and adding more evenly spaced measurements can actually make the approximation worse near the ends of an interval. A mathematical existence-and-uniqueness theorem is not an accuracy guarantee.

Interpolation is a useful place to bring together three questions we have already encountered in numerical analysis: what is the exact mathematical object, how sensitive is it to the data, and how accurately can an algorithm compute it?

## Construct the polynomial

Given n plus one distinct input nodes, labeled x zero through x n, and their corresponding values, we seek a polynomial p of degree at most n that reproduces all the values. A convenient construction uses a different basis polynomial for each node. The j-th basis polynomial equals one at node j and zero at every other node. To build it, multiply the factors x minus x k for all k other than j, and divide by the same product evaluated at x j. The distinctness of the nodes guarantees that none of the denominators vanish.

Multiply each basis polynomial by the corresponding observed value and add the results. At node j, every basis polynomial except the j-th vanishes and the j-th equals one, so the sum gives exactly the required observed value. That proves existence.

For uniqueness, suppose p and q are both polynomials of degree at most n matching the same n plus one values. Their difference is a polynomial of degree at most n with n plus one distinct roots. A nonzero polynomial of degree at most n cannot have that many distinct roots. Therefore the difference is identically zero, and p equals q. The construction and the root-counting argument establish a theorem, not a numerical procedure we should necessarily use literally.

## A simple exact example

Let the nodes be zero, one, and two, with observed values zero, one, and four. The unique polynomial of degree at most two through these points is x squared. At x equal to one half, it predicts one quarter. In this particular example, if the underlying function truly is x squared, interpolation is exact everywhere, not merely at the nodes.

Now change only the underlying function. Suppose the observations come from a smooth function that is not a polynomial. The interpolant still agrees at the sampled nodes, but in between it can differ. We need an error theorem to say anything useful about that difference.

If the underlying function has n plus one continuous derivatives on the interval containing the nodes and our evaluation point, then its interpolation error equals a derivative of order n plus one evaluated at some intermediate point, divided by n plus one factorial, times the product of the distances from the evaluation point to all interpolation nodes. The location of that intermediate point generally depends on the point where we evaluate the error.

This formula reveals two distinct influences. The derivative measures how complicated the underlying function is at the relevant scale. The product measures how the nodes are placed. We cannot guarantee a small error from the number of nodes alone, because neither influence has been controlled merely by increasing n.

## Why equispaced points can misbehave

Consider the smooth function one divided by one plus twenty-five times x squared on the interval from negative one to one. It has a rounded peak at zero and is small at both endpoints. This function is a standard example for the Runge phenomenon: high-degree interpolation at evenly spaced nodes can develop large oscillations near the endpoints, with errors that become worse as we raise the degree along an equispaced sequence.

There is no contradiction with the interpolation theorem. Each polynomial does pass through the assigned nodes, and each is unique. The problem is not a failure to solve the interpolation equations. The problem is that matching more nodes does not by itself force a high-degree polynomial to stay close to the function between the nodes.

The general warning goes beyond this example. If we have noisy measurements, the polynomial passes exactly through the noise as well as the signal. If the sample points are poorly placed, some small perturbations of their values can produce large changes in the interpolant between nodes. Exact agreement with data can be a form of overfitting rather than evidence of accuracy.

## Choose the nodes intelligently

One important alternative is to place more nodes near the ends of the interval. Chebyshev nodes have this property. On the interval from negative one to one, one common choice is the set of zeros of a Chebyshev polynomial: angles equally spaced between zero and pi are mapped to their cosines. The resulting nodes cluster toward the endpoints.

Why would moving nodes help? Look again at the interpolation-error formula. The product of distances from the evaluation point to the nodes is a monic polynomial with those nodes as zeros. Chebyshev polynomials, after normalization to make their leading coefficient one, minimize the largest absolute value of this product over the interval. This gives them an optimal worst-case property for that particular part of the error bound.

For sufficiently smooth functions, and especially for functions analytic in a suitable complex neighborhood of the interval, Chebyshev interpolation can converge rapidly as the degree grows. The precise convergence rate depends on how far the function can be analytically continued and on the location of its complex singularities. We should not claim that one node set cures every possible approximation problem.

For the Runge function, the singularities in the complex plane lie at imaginary values one fifth above and below zero. Although the function is infinitely differentiable on the real interval, those nearby complex singularities limit how favorable high-degree polynomial approximation can be. Chebyshev nodes handle this example far better than equally spaced nodes, even though both choices match the data exactly at their respective sample points.

## Sensitivity and the Lebesgue constant

Suppose the function values at the nodes are each slightly perturbed, perhaps because a sensor has limited precision. The new interpolating polynomial differs from the old one by a sum of the data errors multiplied by the Lagrange basis polynomials. Taking absolute values gives a bound by the maximum data error times the sum of absolute values of the basis polynomials at the evaluation point.

The largest such sum over the interval is called the Lebesgue constant for the chosen nodes. It measures the worst possible amplification of errors in the sampled values when we evaluate the polynomial between the samples. A large Lebesgue constant warns that the interpolation operator is sensitive, even when the data are represented exactly.

The same quantity connects interpolation to best approximation. If E is the smallest uniform error attainable by any degree-n polynomial, the interpolation error in the uniform norm is no more than one plus the Lebesgue constant times E. The proof compares the interpolant to a best approximating polynomial. Since interpolation reproduces polynomials of degree at most n, subtract that comparison polynomial, apply the interpolation operator to the remaining error, and use the triangle inequality.

This argument is important because it separates two questions. How well *could* some degree-n polynomial approximate the function? And how much additional error does our choice of nodes introduce? The Lebesgue constant links the two. For common Chebyshev grids it grows only logarithmically with n, while equispaced grids can have dramatically worse amplification.

## Computation is a third problem

Even with well-chosen nodes and a good mathematical interpolant, we can evaluate it badly. Expanding a high-degree polynomial into ordinary powers of x can produce coefficients with large cancellations. Solving a Vandermonde linear system in a careless representation may be ill-conditioned. Evaluating such a power-series form can lose accuracy even when the underlying interpolation problem is well behaved.

A practical alternative is the barycentric form of Lagrange interpolation. It computes the interpolant through node-dependent weights and ratios rather than forming all the expanded coefficients. Its efficient and stable use is documented in the numerical analysis literature. We still need appropriate handling of evaluation directly at a node, where the naive barycentric ratio would have a zero denominator, and we still need to account for floating-point errors.

There are other alternatives to one global high-degree polynomial. Piecewise polynomial interpolation, such as splines, fits lower-degree polynomials on smaller subintervals and imposes continuity conditions where they meet. That often gives better control for large data sets or locally varying functions. The appropriate method depends on what is known about the function, the noise, and the required smoothness.

## What we can honestly conclude

Interpolation has three distinct layers. At the algebraic layer, n plus one distinct nodes determine a unique polynomial of degree at most n. At the approximation layer, derivatives, node placement, and function regularity determine how close that polynomial lies to the function between samples. At the computational layer, representation and floating-point evaluation determine whether the machine accurately computes the polynomial we intended.

More samples can improve a model, but more constraints can also amplify errors or magnify oscillations if we choose the wrong approximation space. The reliable question is not, “Did the polynomial pass through every measured point?” It is, “What theorem connects those sampled values, this node geometry, and this computational method to the error we are willing to claim?”

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Given distinct \(x_0,\ldots,x_n\) and values \(y_j\), the degree-\(\le n\) interpolant is
\[
p_n(x)=\sum_{j=0}^n y_j\ell_j(x),\qquad
\ell_j(x)=\prod_{k\ne j}\frac{x-x_k}{x_j-x_k}.
\]
For \(f\in C^{n+1}\) on the containing interval, for each \(x\) there exists \(\xi_x\) such that
\[
f(x)-p_n(x)=\frac{f^{(n+1)}(\xi_x)}{(n+1)!}
\prod_{j=0}^n(x-x_j).
\]
The Lebesgue constant is
\[
\Lambda_n=\max_{x\in[a,b]}\sum_{j=0}^n|\ell_j(x)|,
\quad\|f-p_n\|_\infty\le(1+\Lambda_n)E_n(f),
\]
where \(E_n(f)\) is the best uniform degree-\(\le n\) polynomial approximation error. For noisy node data \(|\delta y_j|\le\epsilon\), \(\|\delta p_n\|_\infty\le\Lambda_n\epsilon\).

Chebyshev zeros are \(x_j=\cos((2j+1)\pi/(2(n+1)))\) for \(j=0,\ldots,n\). Standard barycentric weights are \(w_j=1/\prod_{k\ne j}(x_j-x_k)\), and off nodes,
\[
p_n(x)=\frac{\sum_j w_jy_j/(x-x_j)}{\sum_jw_j/(x-x_j)}.
\]
At a node, return its data value directly.

### Exercises with answers

1. How many data points determine a polynomial of degree at most three? **Answer:** Four distinct nodes with four prescribed values.
2. What is the degree-at-most-two interpolant to \(f(x)=x^2\) at three distinct nodes? **Answer:** Exactly \(x^2\) everywhere.
3. Does an interpolant's zero residual at its nodes prove small error between them? **Answer:** No; the Runge example shows possible divergence for equispaced nodes.
4. What does the Lebesgue constant measure? **Answer:** Worst-case sup-norm amplification of nodal data error by the polynomial interpolation operator.

### Reading

Jean-Paul Berrut and Lloyd N. Trefethen, “Barycentric Lagrange Interpolation,” *SIAM Review* 46(3), 2004; Lloyd N. Trefethen, *Approximation Theory and Approximation Practice*; MIT 18.330 Introduction to Numerical Analysis, interpolation and approximation lecture materials.
