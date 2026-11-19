# 038000 — Bounded Linear Operators: When Transformations of Functions Are Stable

**Track:** Analysis from First Principles. **Background:** Normed spaces, complete L-p spaces, continuous linear functionals, and basic examples of functions and sequences. **Question:** Which linear transformations of infinite-dimensional spaces respect approximation, and what does their norm tell us?

<!-- BEGIN SPOKEN LECTURE -->

# Bounded Linear Operators: When Transformations of Functions Are Stable

Suppose you have a function that represents a noisy measurement. You may want to smooth it, average it, shift it in time, differentiate it, or reconstruct a new signal from it. Each of these operations takes a function as input and produces another function as output. Many are linear: applying the operation to a sum is the same as summing the two results, and scaling the input scales the output.

Yet some linear transformations respect small errors and others amplify them without bound. When we say that an operator is bounded, we mean it has a uniform limit on how much it can amplify input size, measured in specified norms. The norms matter. A derivative may be unstable when we control only function height but perfectly stable when we also control the derivative in the input norm.

Begin with two ordinary signals. The first is zero. The second is a sine wave with tiny amplitude but many oscillations. In the supremum norm, which records the largest absolute height, the two signals can be arbitrarily close. Differentiate them, however, and the oscillations multiply the slope by their frequency. If amplitude shrinks at the same rate frequency grows, the derivative stays of fixed size even though the original function approaches zero uniformly.

This shows why differentiation, while linear, is not continuous from continuously differentiable functions equipped only with the supremum norm to continuous functions equipped with that same norm. It is not enough to say, “the input functions look close.” We must say close in which sense, and close enough to control which operation.

## A single bound controls every input

Let X and Y be normed vector spaces. A linear operator T takes each vector in X to a vector in Y, preserving addition and scalar multiplication. We call T bounded if there is a finite constant M such that the norm of T applied to x is at most M times the norm of x, for every x in X.

We also call a linear operator continuous if small changes in input lead to small changes in output. For linear operators, the two conditions are equivalent. The key observation is that the difference between T of x and T of y is T of x minus y. So a bound at zero immediately gives a bound for the effect of perturbing any input.

Why does continuity give a global bound? Suppose continuity at zero tells us that sufficiently small inputs produce outputs of size less than one. We can scale any nonzero vector until its norm lies inside that small ball, apply continuity there, and scale back. This creates a single constant that works for every vector. There is no need to inspect the behavior separately in different regions of X.

The smallest such constant is the operator norm. Equivalently, it is the supremum of output norms over inputs in the unit ball. Think of the unit ball as a set of standardized test inputs and the operator norm as the worst amplification of any one of them.

The operator norm does not tell us that the amplification is actually achieved by some unit vector. In infinite dimensions, there may be no maximizing input. But we can find inputs that come arbitrarily close to the supremum. That distinction becomes important when discussing spectral theory and optimal estimates.

## Smoothing and differentiation pull in opposite directions

Consider the operator that takes an L-two function on the unit interval and, at each point x, outputs the integral of the function from zero up to x. This operation turns an integrable signal into an accumulated signal. It is linear. By Cauchy–Schwarz, the absolute output at any x is no more than the L-two norm of the input times the square root of x. Since x is at most one, the output supremum norm is no greater than the input L-two norm.

So this accumulation operator is bounded from L-two into continuous functions. It does not need pointwise values of the input: changing the input on a null set does not affect the integral. Moreover, comparing outputs at two nearby points shows their difference is at most the L-two norm times the square root of the separation. Accumulation produces a particular kind of continuity, often called one-half Hölder continuity.

Differentiation tries to reverse accumulation. But the domain and norms decide whether that reversal is stable. Consider the functions that take x to sine of n times x divided by n. Their heights go to zero, while their derivatives are cosines of n times x, whose supremum norms remain one. There cannot be one constant bounding the derivative supremum norm by a multiple of the original function supremum norm for all these inputs.

We can stabilize differentiation by changing the input space. Give a continuously differentiable function a norm equal to its maximum height plus its maximum slope. In that stronger norm, differentiation is bounded into continuous functions: the derivative's maximum height is already one of the terms we agreed to measure. Thus the phrase “differentiation is unbounded” is incomplete unless we name its domain, codomain, and norms.

That lesson carries into partial differential equations, numerical approximation, and signal recovery. Regularity assumptions are not decorative: they specify which potentially dangerous operations can be controlled.

## Operators form their own normed space

If T and S are bounded linear operators with the same input and output spaces, their sum is bounded. Multiplying one operator by a scalar keeps it bounded. The operator norm obeys the triangle inequality. We can therefore regard bounded operators themselves as vectors in a new normed space, commonly written as B of X to Y.

If one bounded operator maps X into Y, and another maps Y into Z, we can compose them. The operator norm of the composition is no greater than the product of the two individual norms. The proof is simply to apply the output bound for the first operation, then apply the bound for the second. This inequality is the basic bookkeeping rule behind stable pipelines of linear transformations.

When the output space Y is complete, the space of bounded operators from X to Y is complete in operator norm. Notice that X does not have to be complete for this conclusion. To see why, imagine a Cauchy sequence of operators: once the sequence is sufficiently far along, any two operators act almost the same on every unit-size input, with one uniform error tolerance. Fix an input x. Its sequence of outputs is Cauchy in Y and therefore converges. Use those pointwise limits to define a new transformation T.

Because the original operators were uniformly Cauchy in operator norm, their common bounds pass to T. Linearity passes through the limit as well. More strongly, the sequence converges to T in operator norm, not merely on each individual input. This makes B of X to Y a Banach space when Y is Banach.

Completeness here protects us from a new kind of missing limit: an operator obtained as the uniform limit of stable operators remains stable.

## Convergence of operators is not one thing

There are two ways we might say a sequence of operators approaches a limiting operator. We could demand that the operator norm of the difference tends to zero. That controls errors uniformly over the whole unit ball. Or we could demand only that for each fixed input x, the outputs converge. That is called strong operator convergence.

Operator-norm convergence implies strong convergence, but the converse can fail. A particularly clear example lives in the space of square-summable sequences. Let P-n keep the first n coordinates and erase every coordinate afterward. For any fixed square-summable input, the tail eventually contributes arbitrarily little squared mass. Therefore P-n of x approaches x in norm. The operators converge strongly to the identity.

But for every n, there is a unit vector supported entirely beyond the first n coordinates. P-n erases it completely. Consequently, the operator norm of P-n minus the identity stays equal to one. The convergence is not uniform across all possible unit inputs.

This difference matters in approximation theory. An algorithm can converge for every fixed input without possessing one uniform accuracy guarantee for all inputs of norm one. If the input varies with n, it can always hide in the coordinates the algorithm has not reached.

Another simple operator shifts a sequence one place to the right, adding zero at the front. It preserves the square-sum norm exactly, so its operator norm is one. Yet it is not onto: no shifted output can have a nonzero first coordinate. Norm preservation does not imply invertibility when the space is infinite-dimensional.

## Inverse operations require their own estimates

Suppose a linear bounded operator T has an inverse defined on its entire output space. Should we assume that inverse is bounded too? In finite-dimensional normed spaces, yes. In infinite dimensions, not without further hypotheses. A bounded bijection between Banach spaces does have a bounded inverse, but that is a theorem—the bounded inverse theorem—and its proof uses completeness in an essential way.

We will meet the theorem later with the Baire category argument. For now it helps to separate four properties: linearity, boundedness, injectivity, and surjectivity. None of them should be silently substituted for another. A bounded operator can fail to be injective, as a projection does. It can fail to be onto, as the shift does. And an algebraically invertible linear transformation may have an inverse that behaves badly unless the spaces satisfy the right conditions.

## The space of questions about an operator

A continuous linear functional is simply a bounded linear operator whose output space contains only scalars. Given a more general operator T from X to Y, every bounded linear measurement on Y can be applied after T. This gives a new measurement on X.

Thus T has a dual, or transpose, operator that sends a measurement of outputs to a measurement of inputs. If a functional tells us how to observe the result, the transpose tells us what we were effectively observing in the original input. The transpose is bounded, and its norm is the same as T's norm; proving the reverse norm inequality in full generality uses the existence of enough norm-attaining measurements, a fact supplied by Hahn–Banach.

In a Hilbert space this construction becomes the familiar adjoint operator. The inner product lets us transfer T from one side of a pairing to the other. Matrix transposes and conjugate transposes are its finite-dimensional shadows.

We can now study linear measurements and transformations using one language: norms, continuity, composition, approximation, and dual action. But an important question has been postponed. How do we know that a normed space contains enough continuous linear functionals to distinguish its points, or to extend a measurement defined only on a subspace? The Hahn–Banach theorem answers that question and provides the foundation for the weak viewpoint on convergence.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Boundedness and continuity

For a linear map \(T:X\to Y\) between normed vector spaces,
\[
T\text{ continuous}\iff T\text{ continuous at }0\iff
\exists M<\infty\ \forall x\in X:\ \|Tx\|_Y\le M\|x\|_X.
\]
The operator norm is \(\|T\|=\sup_{\|x\|\le1}\|Tx\|\), and for bounded \(S:Y\to Z\),
\[
\|S\circ T\|\le\|S\|\,\|T\|.
\]
If \(Y\) is Banach, then \(\mathcal B(X,Y)\) is Banach for any normed \(X\). In particular \(X^*=\mathcal B(X,\mathbb K)\) is always Banach.

### Two function operators

On \([0,1]\) with Lebesgue measure define
\[
(Jf)(x)=\int_0^x f(t)\,dt,\qquad J:L^2[0,1]\to C[0,1].
\]
For \(0\le x<y\le1\),
\[
|(Jf)(y)-(Jf)(x)|\le (y-x)^{1/2}\|f\|_2,
\quad \|Jf\|_\infty\le\|f\|_2.
\]
Taking \(f=1\) shows \(\|J\|=1\). In contrast,
\[
D:(C^1[0,1],\|\cdot\|_\infty)\to(C[0,1],\|\cdot\|_\infty),\quad Df=f'
\]
is linear and unbounded: \(f_n(x)=\sin(nx)/n\) satisfies \(\|f_n\|_\infty\le1/n\) and \(\|Df_n\|_\infty=1\). With \(\|f\|_{C^1}=\|f\|_\infty+\|f'\|_\infty\), differentiation is bounded, \(\|D\|\le1\). (The supremum-normed domain in the unbounded example is **not** a Banach space; it presents no contradiction with the closed graph theorem.)

### Strong versus norm convergence

On \(\ell^2\), set \(P_n(x_1,x_2,\ldots)=(x_1,\ldots,x_n,0,\ldots)\). Then \(P_nx\to x\) for every fixed \(x\in\ell^2\), while
\[
\|P_n-I\|=1\quad\text{for all }n.
\]
The unilateral right shift \(S(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots)\) is an isometry with \(\|S\|=1\) and has closed proper range \(\{x:x_1=0\}\).

### Banach adjoint / transpose

Given \(T\in\mathcal B(X,Y)\), define \(T^*:Y^*\to X^*\) by \(T^*\lambda=\lambda\circ T\). Always \(\|T^*\|\le\|T\|\), and Hahn–Banach proves equality. On complex Hilbert spaces using \(\langle x,y\rangle\) linear in the first slot, the Hilbert adjoint \(T^{\dagger}\) is determined by \(\langle Tx,y\rangle=\langle x,T^{\dagger}y\rangle\). Distinguish this from the Banach transpose, which acts on linear duals.

### Exercises and answers

1. **A multiplication operator:** For \(h\in L^\infty\), show \(M_hf=hf\) is bounded on \(L^p\), \(1\le p\le\infty\), with \(\|M_h\|=\|h\|_\infty\). **Answer:** The upper bound is immediate; use normalized indicators on a finite positive-measure subset of \(\{|h|>\|h\|_\infty-\epsilon\}\) for \(p<\infty\) on a sigma-finite space, and the indicator itself for \(p=\infty\).
2. **A projection:** Compute the norm of \(P_n\) on \(\ell^2\). **Answer:** One; it decreases norm and fixes unit vectors supported on the first n coordinates.
3. **Finite-rank approximation:** Are the \(P_n\) convergent to \(I\) in operator norm? **Answer:** No, \(\|I-P_n\|=1\) for every n, despite strong convergence.
4. **Operator Cauchy limit:** Explain why the proof of completeness of \(\mathcal B(X,Y)\) needs completeness of the codomain Y, not X. **Answer:** For each fixed x, \(T_nx\) is Cauchy in Y, where its limit must exist. The uniform operator Cauchy estimate is then inherited by the limit.

### References

- MIT OpenCourseWare, *18.102 Introduction to Functional Analysis* (2021), Lectures 1–4: https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/.
- Terence Tao, *245B, Notes 6: Duality and the Hahn–Banach theorem*: https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/.
- Sheldon Axler, *Measure, Integration & Real Analysis*, operator/Hilbert chapters: https://measure.axler.net/.
