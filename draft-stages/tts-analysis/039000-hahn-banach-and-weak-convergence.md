# 039000 — Hahn–Banach: Extending Measurements and Seeing Weak Convergence

**Track:** Analysis from First Principles. **Background:** Normed and Banach spaces, bounded linear functionals and dual norms, and the distinction between norm and pointwise operator convergence. **Question:** Can a bounded linear measurement defined on a subspace be extended to the whole space without increasing its sensitivity, and what does this reveal about convergence?

<!-- BEGIN SPOKEN LECTURE -->

# Hahn–Banach: Extending Measurements and Seeing Weak Convergence

Imagine that you have learned to measure signals of a very specific form. Perhaps your measuring device was designed only for signals that are constant across an interval. Or perhaps it was calibrated on the finite-dimensional subspace spanned by a small collection of waveforms. On that familiar subspace, the measurement is linear and its output is bounded by the size of the input.

Now the larger space contains many more signals. Can we extend the measurement to every signal while retaining exactly the same sensitivity bound? We do not want to invent an extension that produces huge readings on small inputs. And we are not asking whether there is a unique extension: many different extensions may agree on the calibrated subspace.

The Hahn–Banach theorem answers the existence question with a remarkable yes. Every bounded linear functional on a subspace of a normed vector space extends to the entire space without increasing its norm. The theorem is true for real and complex spaces, and the full space does not even have to be complete.

This is one of the structural facts that makes the idea of a dual space powerful. It says that a measurement on a small part of a space can be made globally consistent with the same numerical bound. And it implies that the continuous dual has enough measurements to detect every nonzero vector and distinguish a point from a closed linear subspace.

## First, an extension you can see

Take the ordinary plane, but measure vector size by the larger of the absolute values of its two coordinates. Focus only on the diagonal line: vectors whose two coordinates agree. Along that line, define a measurement that returns the common coordinate. The measurement has norm one. An input of size one cannot produce a reading larger than one.

One extension to the whole plane returns the first coordinate. Another returns the second coordinate. Both agree on the diagonal and both have norm one. A third returns the average of the two coordinates. Again the same norm, again the same values on the diagonal. In fact, there is a whole interval of norm-preserving extensions.

So the theorem is about existence with controlled size, not unique recovery. The information known on a subspace may leave the off-subspace behavior underdetermined. That is important in applications: extending a linear observable without increasing its norm is an abstract mathematical guarantee, not a method for recovering the one physically intended measurement.

The question is why the same principle works in spaces with infinitely many independent directions. We will first add just one direction and see the key inequality that makes the proof possible.

## Adding one new direction without breaking the bound

Suppose the space is real. We have a linear functional on a subspace M, and its readings are bounded by a constant times the input norm. Choose a vector x-zero outside M. Every vector in the enlarged span has a unique form: a vector m from M plus a scalar multiple of x-zero. If we choose the value of the extended functional on x-zero, linearity determines all other new values.

So one extension step boils down to selecting one real number, call it a. The old measurement and the value a must cooperate so that the bound still holds for every vector in this larger span.

The condition imposes both upper and lower restrictions on a. Vary the vector m, and you get a collection of permissible lower bounds. Vary it another way, and you get upper bounds. At first it seems possible that the lower restrictions force a above the upper restrictions, making any extension impossible.

But the triangle inequality—the same inequality that defines our norm—guarantees those ranges do not cross. It lets us compare the lower requirement from one old vector with the upper requirement from another by adding the two old vectors and cancelling the new direction. The old functional already obeys the norm bound, so the cancellation makes the inequality work.

Choose any a in the resulting interval. Now the measurement extends to one more independent direction without changing its norm. Nothing in this step depends on the dimension being finite.

To reach an arbitrary space, we organize all possible norm-preserving extensions by inclusion: an extension is larger if it is defined on a larger subspace and agrees with the smaller one. Every totally ordered family of such extensions has a consistent union. A maximal-extension principle, commonly formulated as Zorn's lemma, then gives an extension that cannot be enlarged. If its domain were not the whole space, the one-direction construction would enlarge it. That contradiction finishes the real theorem.

For complex vector spaces, the proof needs another step because one complex direction contains two real directions. We apply the real theorem to the real part of the functional and then reconstruct the complex-linear functional from that real-linear extension. The norm is preserved. The result is the complex Hahn–Banach theorem.

This proof is not an explicit recipe for writing down an extension in every infinite-dimensional case. The maximal-extension step invokes a choice principle. What it provides is a global existence theorem with a sharp bound.

## No vector can hide from every bounded measurement

Choose a nonzero vector x in any normed space. Define a measurement on the one-dimensional subspace spanned by x: ask for the coefficient of x, multiplied by the norm of x. This functional has norm one and reads exactly the norm of x when applied to x itself.

Hahn–Banach extends that measurement to the entire space without increasing its norm. Therefore, for every nonzero x, there is some bounded linear functional of norm one whose absolute reading on x equals the norm of x.

Notice the distinction from an operator necessarily attaining its norm. We are choosing a functional *in response to a specified vector*. We are not claiming that every pre-existing functional has a maximizing vector. Hahn–Banach tells us that the entire family of functionals is rich enough to find one tailored to any given nonzero input.

This immediately yields a dual formula for the norm: the norm of x is the supremum of the absolute values of all norm-one-bounded measurements applied to x. One inequality follows because every such measurement is bounded by the input norm. The other follows from the norm-one functional we just constructed.

Now consider a closed linear subspace M and a point x outside it. We can separate x from M with a bounded linear functional that vanishes on all of M and is nonzero on x. In fact, we can arrange its value on x to equal the distance from x to M while its norm is one. The construction passes to the quotient space X modulo M, where vectors differing by an element of M are treated as equivalent. The quotient norm of x is precisely that distance. A norming functional on the quotient pulls back to the desired measurement on X.

Closedness matters. If x lay in the closure of M, every continuous functional vanishing on M would also have to vanish at x. We cannot demand a strictly separating continuous measurement where no positive distance exists.

## Convergence viewed through every observer

We can now define a weaker kind of convergence. A sequence of vectors converges weakly to x if every bounded linear functional assigns readings that converge to the reading of x. In other words, no fixed continuous linear measurement can distinguish the later vectors from x in the limit.

Norm convergence implies weak convergence: a bounded functional cannot amplify a norm-small difference by more than its norm. But weak convergence does not require the vectors themselves to become close in norm. Different observers can all see convergence without a common uniform error bound over every possible observer.

Think of the standard basis in the Hilbert space of square-summable sequences. The first vector has a one in the first coordinate and zeros elsewhere; the second has a one in the second coordinate; and so on. Every vector in the sequence has norm one, so the vectors do not approach zero in norm.

Yet choose any fixed continuous linear functional. In this Hilbert space, it is represented by an inner product with some square-summable coefficient sequence. Applying the functional to the n-th basis vector picks out the n-th coefficient. Since the coefficients form a square-summable sequence, they must tend to zero. Therefore every fixed bounded linear measurement tends to zero, and the basis vectors converge weakly to zero.

This is a genuine change of viewpoint. Norm convergence asks for one uniform bound covering all unit-norm measurements simultaneously. Weak convergence allows the accuracy threshold to depend on which measurement was selected. Every observer eventually sees a tiny reading, but observers chosen differently at each stage can keep finding a full-size discrepancy.

## Weak convergence is not automatic in every sequence space

It is tempting to conclude that standard basis vectors always converge weakly to zero in any infinite-dimensional sequence space. That is false. In the space of absolutely summable sequences, the functional that sums all coordinates is bounded: its absolute value cannot exceed the sum of their absolute values. Applied to each standard basis vector, that functional returns one. So the sequence cannot converge weakly to zero in L-one's sequence counterpart, usually called ell-one.

The contrast between ell-one and ell-two is informative. The geometric and dual structures differ; the available measurements differ; and hence the weak convergence behavior differs. The same coordinatewise picture does not guarantee the same weak limit.

We should also avoid confusing weak convergence of vectors with weak-star convergence of functionals. If we consider elements of X-star as vectors in their own right, weak convergence there uses every element of its dual, the double dual. Weak-star convergence of functionals means only testing each functional against fixed vectors in X. Those are different collections of observers, and weak-star convergence can be strictly weaker.

The double dual gives us a natural map from each vector x into the functional on X-star that sends a measurement to its value on x. Our norm formula shows this map preserves norm. When it happens to be onto, the space is called reflexive. Hilbert spaces and L-p spaces for p strictly between one and infinity are reflexive; many endpoint spaces are not. A full proof of these characterizations requires more work, but the language explains why functionals can themselves be analyzed as mathematical objects.

## What must come next

There is an important assertion we have not proved: a weakly convergent sequence is bounded in norm. It sounds plausible, but its quantifiers are delicate. Weak convergence tells us that for each fixed functional, its readings on the sequence are bounded. It does not directly give a single bound uniform across all functionals, and Hahn–Banach's norm formula is a supremum over many different functionals.

The missing tool is the uniform boundedness principle. It converts pointwise boundedness of a family of continuous linear operators into a uniform operator norm bound, provided the common input space is complete. Its proof begins not with linear algebra, but with a topological theorem about complete metric spaces: the Baire category theorem.

The path from extension of one measurement to control of whole families may seem indirect. It is not. Hahn–Banach guarantees there are enough measurements to recognize the size and location of a vector. Baire category will tell us when pointwise control of those measurements can be upgraded to a global bound. Together they make weak convergence into a serious tool rather than just a change in vocabulary.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Norm-preserving Hahn–Banach

If \(M\subseteq X\) is a linear subspace of a real or complex normed space and \(f\in M^*\), there exists \(F\in X^*\) with
\[
F|_M=f,\qquad \|F\|=\|f\|.
\]
The more general real form: given sublinear \(p:X\to\mathbb R\), and real-linear \(f:M\to\mathbb R\) with \(f(m)\le p(m)\) for every \(m\in M\), extend \(f\) to all of \(X\) so that \(F(x)\le p(x)\) for every \(x\in X\).

### The one-step inequality

For \(x_0\notin M\), set \(F(m+t x_0)=f(m)+t a\). A value \(a\in\mathbb R\) is admissible whenever
\[
\sup_{m\in M}[f(m)-p(m-x_0)]\ \le a\ \le
\inf_{m\in M}[p(m+x_0)-f(m)].
\]
The left side does not exceed the right: for \(m,n\in M\), linearity and subadditivity imply
\(f(m)+f(n)=f(m+n)\le p(m+n)\le p(m-x_0)+p(n+x_0)\).
Zorn's lemma yields a maximal extension after iterating the one-dimensional argument. In the complex case, extend \(u=\operatorname{Re}f\) on the underlying real space and recover \(F(x)=u(x)-i u(ix)\), with the same norm.

### Norming functionals and subspace separation

For any \(x\ne0\), there exists \(f\in X^*\) with \(\|f\|=1\) and \(f(x)=\|x\|\). Consequently,
\[
\|x\|=\sup_{\|f\|\le1}|f(x)|.
\]
For a **closed** subspace \(M\subset X\) and \(x_0\notin M\), its quotient \(X/M\) is normed and \(d=\operatorname{dist}(x_0,M)>0\). Hahn–Banach on the quotient supplies \(f\in X^*\) with \(f|_M=0\), \(\|f\|=1\), and \(f(x_0)=d\).

### Weak and weak-star convergence

\[
x_n\rightharpoonup x \quad\Longleftrightarrow\quad
\forall f\in X^*:\ f(x_n)\to f(x).
\]
For \(f_n\in X^*\), weak-star convergence \(f_n\overset{w^*}{\rightharpoonup}f\) means \(f_n(x)\to f(x)\) for all \(x\in X\); weak convergence in \(X^*\) tests against all elements of \(X^{**}\).

On \(\ell^2\), \(e_n\rightharpoonup0\) but \(\|e_n\|=1\), since any \(y\in\ell^2\) has \(y_n\to0\) and \(\langle e_n,y\rangle=\overline{y_n}\) with the convention linear in the first slot. On \(\ell^1\), the functional \(x\mapsto\sum_n x_n\) witnesses that \(e_n\) is not weakly null.

### Exercises with answers

1. **Non-unique extensions:** On \((\mathbb R^2,\|\cdot\|_\infty)\), define \(f(t,t)=t\). Find two different norm-one extensions. **Answer:** \(F_1(x,y)=x\) and \(F_2(x,y)=y\).
2. **A separating functional:** In \(\mathbb R^2\) with Euclidean norm, find a norm-one functional vanishing on the horizontal axis and taking value \(2\) at \((1,2)\). **Answer:** \(F(x,y)=y\).
3. **Two weak behaviors:** Why is \(e_n\) weakly null in \(\ell^2\) but not \(\ell^1\)? **Answer:** All \(\ell^2\) representing coefficients tend to zero, while the bounded \(\ell^1\) functional summing coordinates remains one.
4. **The embedding into the double dual:** Define \(J:X\to X^{**}\) by \(J(x)(f)=f(x)\). Why is \(J\) an isometry? **Answer:** \(\|Jx\|=\sup_{\|f\|\le1}|f(x)|=\|x\|\) by Hahn–Banach.

### References

- Terence Tao, *245B, Notes 6: Duality and the Hahn–Banach theorem*: https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/.
- Terence Tao, *245B, Notes 11: The strong and weak topologies*: https://terrytao.wordpress.com/2009/02/21/245b-notes-11-the-strong-and-weak-topologies/.
- MIT OpenCourseWare, *18.102 Introduction to Functional Analysis* (2021), lecture 5 on Zorn's lemma and Hahn–Banach: https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/.
