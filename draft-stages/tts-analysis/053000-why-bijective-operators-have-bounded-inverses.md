# 053000 — Why a Bijective Operator Has a Bounded Inverse

**Track:** Analysis from First Principles. **Background:** Banach spaces, bounded linear maps, and the Baire category theorem. **Central question:** When does solving an equation depend continuously on the data?

<!-- BEGIN SPOKEN LECTURE -->

# Why a Bijective Operator Has a Bounded Inverse

Imagine a measurement device. A dial gives a number and the device returns a signal. You can reverse the procedure: given a signal, find the dial setting that produced it. But a question remains. If the measured signal changes by a tiny amount, can the inferred setting change enormously?

That is the distinction between finding an inverse and having a stable inverse. In linear algebra, a square matrix with nonzero determinant has an inverse, and because the setting is finite dimensional, that inverse is automatically continuous. In spaces of functions, neither the existence of an inverse nor its stability can be assumed. Two great results of functional analysis explain why completeness rescues stability.

Let us start with a familiar bad inverse. On the interval from zero to one, take a continuously differentiable function that vanishes at zero and measure only the size of its values, using the maximum absolute value. Differentiation turns this function into another continuous function. As an algebraic map, differentiation is one-to-one and onto: integrate any continuous output from zero to x to recover the input. Yet high-frequency sine waves can be tiny in height and large in slope. The inverse, integration, is stable in the maximum norm; differentiation itself is not stable in that norm. This warns us to specify both the spaces and their norms before saying that an equation is well posed.

A cleaner example of an unstable inverse uses sequences. Let a sequence x be square summable. Form another sequence by dividing its N-th entry by N. This is a bounded, one-to-one operator. Its inverse, where defined, multiplies the N-th entry by N. A sequence concentrated in a distant coordinate barely registers in the output. Recovering its amplitude magnifies noise by N. Here the problem is that the operator is not onto the entire square-summable space. The missing surjectivity matters.

Now suppose we have two Banach spaces. That name means they are normed spaces in which every Cauchy sequence has a limit. Assume a linear operator from the first to the second is bounded, meaning that a constant controls the output norm by the input norm. Suppose it is also one-to-one and onto. The bounded inverse theorem says its inverse is bounded. Thus a genuinely bounded bijection between complete normed spaces is stable in both directions.

What does completeness have to do with it? We can hear the main idea through the open mapping theorem. It says a bounded linear map from one Banach space onto another sends every open set to an open set. A small neighborhood of the zero input therefore reaches a whole, perhaps smaller, neighborhood of the zero output. Scaling by linearity then says that every output has a preimage whose size is controlled by the output size. If the map is one-to-one, that preimage is unique, giving the bounded inverse.

To see why the theorem is not trivial, imagine mapping the unit ball of inputs into an enormous but very thin set of outputs. Surjectivity says that, if we scale and combine enough such images, every output can eventually be reached. It does not immediately say the image of the unit ball contains any neighborhood of zero. Baire's category theorem supplies this missing interior. Very roughly, a complete space cannot be assembled as a countable union of sets that are each nowhere dense. The image of the whole input space is a countable union of scaled images of its unit ball. One closure must contain some open ball. Linearity recenters this information at zero. An iterative correction argument then turns approximate outputs into actual outputs with a controlled sum of input corrections.

There is a related theorem about closed graphs. The graph of an operator is the set of pairs consisting of an input and its output. The graph is closed when converging inputs and converging outputs remain compatible: if inputs approach x and their outputs approach y, then y really is the output of x. A bounded operator automatically has a closed graph. Remarkably, a linear operator defined on all of a Banach space with values in another Banach space is bounded whenever its graph is closed.

This is an efficient way to prove continuity. Sometimes direct estimates are hard, but passing to a limit in an equation is easy. If we can show any pair of limits still satisfies the defining equation, the closed graph theorem gives the norm estimate we wanted. Notice the phrase defined on all of a Banach space. Differential operators often act only on functions with enough derivatives; for them a closed graph does not imply boundedness with respect to the ambient norm.

Why is this important for differential equations? An operator may encode the relationship between a forcing function and a solution. A uniqueness proof tells us that two solutions with the same forcing cannot differ. An existence proof tells us every admissible forcing has a solution. If this relationship is described by a bounded operator between Banach spaces, the bounded inverse theorem supplies continuous dependence on the forcing. This is the third leg of well-posedness: existence, uniqueness, and stability.

The subtlety is in selecting spaces that reflect the equation. Solving a second-order equation may gain two derivatives in a suitable sense, while the second-derivative operator is not bounded on the original space of square-integrable functions. Changing to a norm that also measures derivatives can make a closed operator into a bounded one between the correct domain and output spaces. Mathematics does not erase instability. It tells us how to diagnose it and which hypotheses are strong enough to rule it out.

The practical test is simple. When someone writes the symbol T inverse, ask: onto what space, and with which norm? If those questions have satisfactory answers, the abstract theorems turn the word inverse from an algebraic promise into an analytical guarantee.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(X,Y\) be Banach spaces, \(T\in\mathcal B(X,Y)\). Open mapping: if \(T\) is surjective, then \(T(U)\) is open for each open \(U\subset X\). Bounded inverse: if \(T\) is bijective, then \(T^{-1}\in\mathcal B(Y,X)\). Closed graph: for a *linear, everywhere-defined* \(T:X\to Y\), closedness of \(G(T)\subset X\times Y\) implies boundedness.

A proof mechanism for open mapping: \(Y=\bigcup_{n\ge1}T(nB_X)\), hence by Baire some \(\overline{T(B_X)}\) has interior after rescaling. Linear translation gives \(B_Y(0,\delta)\subset\overline{T(B_X)}\). Successively approximate a target by errors of size \(2^{-n}\) with preimages of norm \(O(2^{-n})\). Completeness of \(X\) makes the corrections converge, yielding \(B_Y(0,c\delta)\subset T(B_X)\) for a suitable \(c>0\).

Counterexample to dropping surjectivity: \(T:\ell^2\to\ell^2\), \((Tx)_n=x_n/n\). It is bounded, injective, and \(\|Te_n\|=1/n\to0\) while \(\|e_n\|=1\). The range is dense but not closed. The inverse exists on \(\operatorname{ran}T\), yet is unbounded there.

Counterexample to dropping completeness of the domain: \(D:\{f\in C^1([0,1]):f(0)=0\}\to C([0,1])\), \(Df=f'\), with \(\|f\|_\infty\) on the domain. The map is a linear bijection whose inverse is bounded, but \(D\) is unbounded, since \(f_n(x)=\sin(n\pi x)/(n\pi)\) has vanishing sup norm while \(\|Df_n\|_\infty=1\). The domain under \(\|\cdot\|_\infty\) is incomplete.

### Exercises with answers

1. **Diagonal inverse.** For \(T e_n=n^{-1}e_n\), find \(\|T\|\). **Answer:** One. Its inverse on the range is unbounded.
2. **Closed graph.** If \(T\) is bounded and \(x_n\to x\), \(Tx_n\to y\), why is \(y=Tx\)? **Answer:** By continuity \(Tx_n\to Tx\), and limits are unique.
3. **Well posedness.** What does bijectivity alone fail to ensure in a noncomplete domain? **Answer:** Continuous dependence of solutions on inputs; bounded-inverse conclusions require complete spaces and a bounded forward map.

### Reading and source notes

- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
- [Sheldon Axler, Measure, Integration and Real Analysis](https://measure.axler.net/)
