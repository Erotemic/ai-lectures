# 004000 — What Continuity Guarantees: Roots, Bounds, and Extrema

**Track:** Analysis from First Principles. **Background:** real-number completeness, sequences, and continuity of functions. **Theme:** how local control of a function, together with a closed interval, forces global facts.

<!-- BEGIN SPOKEN LECTURE -->

# What Continuity Guarantees: Roots, Bounds, and Extrema

Suppose a physical model predicts that some quantity is negative under one setting and positive under another. It would be useful to know whether there must be a setting in between where the quantity is exactly zero. Perhaps that setting represents an equilibrium, a transition, or the location of a root of an equation.

A graph seems to offer a quick answer. Draw a curve between a point below the horizontal axis and a point above it. Surely the curve crosses zero. But that word, surely, hides assumptions. What prevents the function from jumping across the axis? What makes the crossing point exist as a real number, rather than as a gap approached forever?

The Intermediate Value Theorem answers these questions. And a close relative, the Extreme Value Theorem, guarantees something equally important: a continuous real function on a closed, bounded interval actually reaches a highest value and a lowest value. We will see why continuity alone is not enough, why the interval's endpoints matter, and how completeness supports both results.

## Finding a root without guessing its value

Consider the function obtained by cubing x, subtracting x, and subtracting one. At x equals one, its value is negative one. At x equals two, its value is positive five. Because this is a polynomial, it is continuous everywhere on the real line.

The Intermediate Value Theorem says there is at least one real number between one and two where the function is zero. It does not tell us that this number has a simple fraction or decimal representation. It does not, by itself, say the root is unique. Its conclusion is existence.

More generally, if a real-valued function is continuous on the entire interval from a to b, and its value at a lies below a particular target height while its value at b lies above that height, then somewhere on the interval the function attains exactly that target height. The statement also works with the inequalities reversed. If one endpoint already has the target value, the answer is immediate.

We can understand the theorem by watching a search procedure. Begin with a bracket whose left endpoint has a negative function value and whose right endpoint has a positive one. Look at the midpoint. If its function value is zero, we are finished. Otherwise, keep whichever half of the bracket still has a negative value at the left end and a positive value at the right end.

Each decision discards half of the previous interval without discarding the possibility of a root. After one decision the bracket is half as wide. After ten it is one part in a thousand of the original width, approximately. After twenty it is about one part in a million. The search can make the bracket as narrow as we wish.

But a shrinking bracket is not yet a proof that an exact root exists. We have to explain why the infinitely many nested brackets share a point and why the function vanishes at that point.

## Where completeness enters the proof

Call the left endpoint after each step the lower endpoint, and the right endpoint the upper endpoint. The lower endpoints never decrease; the upper endpoints never increase. They all stay between the original endpoints. The lengths of the brackets tend to zero.

Because the lower endpoints form a bounded, nondecreasing sequence of real numbers, the completeness of the real line guarantees that they converge. Let their limit be c. The upper endpoints have the same limit, since the distance between upper and lower endpoints becomes arbitrarily small.

Now use continuity. Each lower endpoint has a function value that is negative or zero, and those endpoints approach c. A continuous function sends that convergent sequence of inputs to a convergent sequence of outputs. So the function's value at c cannot be positive. Each upper endpoint has a function value that is positive or zero, and those endpoints approach the very same c. Therefore the function's value at c cannot be negative. The only possibility is zero.

That argument proves the existence of a root, not just the convergence of a numerical routine. The real line contributes a limit point for the nested intervals; continuity transfers the sign information to that point.

In the running cubic example, the root in the interval from one to two is also unique. If we choose two numbers in that interval, the larger number has a strictly larger function value. One way to see this is to factor the difference between the two function values: it equals the difference of the inputs multiplied by the sum of their two squares, their product, and negative one. On our interval the second factor is positive. The cubic is strictly increasing there, so it crosses zero only once.

The uniqueness conclusion came from extra information about this particular function. The Intermediate Value Theorem alone would allow several crossings.

## What the theorem does not say

Take a function that outputs negative one on the left half of an interval and positive one on the right half, jumping at the midpoint. Its endpoint values have opposite signs, but the function never outputs zero. The missing hypothesis is continuity.

Or take a continuous function whose values are both positive at the endpoints. It might still dip below zero in the middle and cross the axis twice. The Intermediate Value Theorem gives a sufficient condition for a crossing, not a test that detects all crossings. A failure of its endpoint condition does not prove that no root exists.

In computation, this matters. A sign-changing bracket is a certificate of existence only when we know the function is continuous on the bracket. Sampling two endpoints of a black-box program is not automatically enough. The program could implement a jump, have an undefined point inside, or return values affected by numerical error.

Bisection also gives an error guarantee. After n exact halvings, the current bracket has width equal to the original width divided by two to the n. The midpoint lies at most half that width from any root inside the bracket. Under the theorem's hypotheses, there is such a root. We obtain a numerical approximation and a mathematical reason to trust the interval containing it.

## A different global question: must a highest value exist?

Now suppose we are not hunting for a zero. We are optimizing a quantity. A machine's efficiency varies with a control parameter between zero and one. Can we assert that some allowed setting achieves the largest efficiency?

A continuous function on a closed, bounded real interval is guaranteed to achieve both a maximum and a minimum. This is the Extreme Value Theorem. The word achieve is essential. A function may have values that approach a best possible bound without ever attaining it.

Consider the function that simply returns its input, but restrict the allowed inputs to the interval from zero up to, but not including, one. The outputs are all less than one. They can get as close to one as we like, so one is their least upper bound. Yet no allowed input produces the value one. There is no maximum.

The function is perfectly continuous on its domain. What fails is that the interval omits an endpoint. On the closed interval from zero through one, the same function does attain its maximum at one.

Boundedness of the input interval is important too. On the entire real line, the function that returns x is continuous and has neither a global maximum nor a global minimum. Even on a closed set, continuity does not supply extrema unless the relevant compactness condition is present.

Why does the combination of continuity and a closed, bounded interval work so reliably? We need to understand a more general fact about sequences.

## Why bounded sequences have convergent subsequences

Take any infinite sequence of points within a closed interval. The sequence itself need not converge. It could alternate between the two endpoints. Nevertheless, we can always select an increasing list of indices so that the corresponding terms converge to some point of the interval. This is the Bolzano–Weierstrass property in its one-dimensional form.

Here is the idea behind a proof. Divide the interval into two closed halves. At least one half contains infinitely many terms of the sequence. Keep that half. Divide it again, and keep a half containing infinitely many terms. Repeat. The retained intervals nest inside one another and shrink to zero width.

Because the real numbers are complete, their endpoints converge to a common point c. Since the original interval is closed, c belongs to it. We can now choose one term from the first retained interval, a later term from the second, a still later term from the third, and so on. We can make the indices increase because every retained interval contains infinitely many sequence terms. The selected terms get trapped in shrinking intervals around c. They converge to c.

This argument turns boundedness into a supply of convergent subsequences. It does not force the original sequence to converge; the alternating endpoints still do not. But it ensures that no infinite sequence in a closed interval can avoid having at least one convergent part.

## Proving the existence of a maximum

Let f be continuous on the closed interval from a to b. Before asking whether f reaches a maximum, we must know whether its outputs are bounded above. Suppose they were not even bounded in absolute value. We could choose an input x at each positive integer stage n for which the magnitude of f at x exceeds n.

Those chosen inputs all lie in the closed interval. By the subsequence property, some subsequence of them converges to a point c inside the interval. Continuity then forces the corresponding outputs to converge to the finite number f at c. But their magnitudes grow beyond every bound. They cannot converge to a finite number. That contradiction shows the outputs of f are bounded.

Now let M be the least upper bound of all the output values. The supremum exists by completeness. For each positive integer n, the definition of least upper bound lets us choose an input whose output is greater than M minus one divided by n. These outputs approach M from below.

Again, the inputs have a convergent subsequence, with limit c inside the interval. Continuity tells us their output values converge to f at c. Since those same outputs approach M, uniqueness of limits gives f at c equal to M. The function attains its maximum. Apply the same argument to the negative of f to obtain a minimum.

This is the Extreme Value Theorem, built from three ingredients: completeness supplies a supremum; closed boundedness supplies a convergent subsequence that remains in the domain; and continuity carries the limiting input to the limiting output.

The proof is also a model for other areas of mathematics. To prove a best solution exists, one often constructs almost-best candidates, extracts a convergent subsequence, and shows that the objective function preserves their limiting value.

## The boundary of the guarantee

We should not turn a theorem into a slogan stronger than it really is. Continuity does not guarantee a maximum on every domain. It does not guarantee a root merely because two outputs have different signs if some intermediate inputs are forbidden. And neither theorem locates the root or optimizer with no additional work.

The role of the real line is especially important. The sign argument uses the order of real numbers: negative values on one side, positive values on the other, and zero between them. In the complex plane, there is no corresponding order. A continuous path can move from positive one to negative one by traveling around zero instead of through it. The Intermediate Value Theorem is a real-variable statement, not a claim about every possible kind of continuous motion.

Our two theorems make a useful contrast. The Intermediate Value Theorem says that continuity on an interval forbids jumping over intermediate output heights. The Extreme Value Theorem says that continuity on a closed, bounded interval prevents the best and worst output heights from escaping attainment. Both depend on exact hypotheses, and both illustrate why completeness of the underlying space matters.

A numerical experiment may suggest a crossing or an optimum. Theorems tell us when those features must exist. That difference—between observing a plausible shape and establishing a necessary consequence—is one of the main achievements of rigorous analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Intermediate Value Theorem.** If \(f:[a,b]\to\mathbb R\) is continuous and \(y\) lies between \(f(a)\) and \(f(b)\), then \(\exists c\in[a,b]\) with \(f(c)=y\). Equivalently, apply the zero-crossing version to \(g=f-y\).

**Sign-preserving bisection.** Assume \(f(a)<0<f(b)\). Unless a midpoint is a root, recursively retain a closed half-interval \([a_n,b_n]\) with \(f(a_n)<0<f(b_n)\). Then

\[
a_n\uparrow c,\qquad b_n\downarrow c,\qquad
b_n-a_n=\frac{b-a}{2^n},\qquad f(c)=0.
\]

If \(m_n=(a_n+b_n)/2\), the error satisfies \(|m_n-c|\le(b-a)/2^{n+1}\). The indexing starts with \(n=0\) for the original bracket.

**Running example.** \(f(x)=x^3-x-1\) has \(f(1)=-1\) and \(f(2)=5\), so a root exists in \((1,2)\). If \(1\le x<y\le2\), then

\[
f(y)-f(x)=(y-x)(x^2+xy+y^2-1)>0,
\]

which shows strict increase and hence uniqueness of the root within this interval.

**Bolzano–Weierstrass.** Every bounded real sequence has a convergent subsequence. The limit belongs to any closed interval containing the original sequence. Proof: nested closed-interval selection with infinitely many sequence terms and lengths tending to zero; extract strictly increasing indices.

**Extreme Value Theorem.** If \(f:[a,b]\to\mathbb R\) is continuous, then \(f([a,b])\) is bounded and there exist \(x_{\min},x_{\max}\in[a,b]\) such that

\[
f(x_{\min})\le f(x)\le f(x_{\max})\quad\text{for all }x\in[a,b].
\]

**Proof skeleton:** If \(f\) were unbounded, choose \(x_n\) with \(|f(x_n)|>n\); a convergent subsequence of \(x_n\) would contradict continuity. Set \(M=\sup f([a,b])\). Choose \(x_n\) with \(M-1/n<f(x_n)\le M\), extract \(x_{n_k}\to c\in[a,b]\), and use continuity to obtain \(f(c)=M\). Minimize via \(-f\).

**Failed hypotheses:** \(f(x)=x\) on \([0,1)\) is continuous but has no maximum. \(f(x)=x\) on \(\mathbb R\) is continuous but unbounded. \(f(x)=-1\) for \(x<0\), \(f(x)=1\) for \(x\ge0\) has sign-changing endpoints but no zero, because it is discontinuous.

### Exercises and guided answers

1. **Guaranteed crossing:** Show \(x^3+x-3=0\) has a real root in \((1,2)\). **Answer:** The polynomial is continuous and has values \(-1\) and \(7\) at the endpoints.
2. **Nonuniqueness:** Does the Intermediate Value Theorem prove uniqueness? **Answer:** No. \(f(x)=x(x-1)(x+1)\) has three roots on \([-2,2]\).
3. **Accuracy:** Starting from a length-one sign-changing bracket, how many bisections ensure the midpoint's error is at most \(1/2048\)? **Answer:** Ten, because \(1/2^{10+1}=1/2048\).
4. **Attainment versus supremum:** What is \(\sup\{x:0\le x<1\}\), and does the set have a maximum? **Answer:** Supremum 1; no maximum since 1 is excluded.
5. **Role of continuity:** Why does a convergent input subsequence help prove the Extreme Value Theorem? **Answer:** Continuity forces the corresponding output subsequence to converge to the value at its limiting input, which remains in the domain.

### References

- OpenStax, *Calculus Volume 1*, section 2.4, “Continuity” (Intermediate Value Theorem): https://openstax.org/books/calculus-volume-1/pages/2-4-continuity
- OpenStax, *Calculus Volume 1*, section 4.3, “Maxima and Minima” (Extreme Value Theorem): https://openstax.org/books/calculus-volume-1/pages/4-3-maxima-and-minima
- Stephen Abbott, *Understanding Analysis*, chapters on completeness, compact sets, and continuous functions.
- Terence Tao, *Analysis I*, chapters on the least upper bound property and continuous functions.
- [MIT OpenCourseWare, 18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/pages/lecture-notes/) — MIT 18.100B, lectures 11 and 14: IVT, EVT and compactness.
