# 033000 — Dominated Convergence: When Limits May Pass Through Integrals

**Track:** Analysis from First Principles. **Background:** measurable functions, integrable functions, Fatou's lemma, and monotone convergence. **Question:** What quantitative control stops mass from concentrating or escaping when functions converge pointwise?

<!-- BEGIN SPOKEN LECTURE -->

# Dominated Convergence: When Limits May Pass Through Integrals

Imagine a room containing a fixed amount of smoke. You measure a sequence of density profiles and find that, at each chosen location, the density approaches zero. Has the total smoke disappeared? Not necessarily. The smoke could have gathered into an ever narrower plume, with the same total mass. Or it could have traveled farther and farther away, passing any fixed observer only finitely many times. In either case, every fixed location eventually reports zero while the total mass remains unchanged.

This is a problem about exchanging two operations. One operation takes a limit of functions, observing what happens point by point. The other operation takes an integral, aggregating a quantity over the entire domain. There is no general reason why applying them in one order should give the same answer as applying them in the other.

The dominated convergence theorem explains a powerful circumstance in which the exchange is legitimate. Its essential hypothesis is not a rate of convergence, and not a finite domain. It is the existence of one integrable function that controls the absolute size of every approximation. We will see why that fixed bound matters, prove the theorem from Fatou's lemma, and compare it with several tempting but inadequate substitutes.

## A disappearing graph can keep its area

Begin on the interval between zero and one. At stage n, draw a rectangle of height n and width one over n, just to the right of zero. Outside the rectangle the function is zero. The rectangle's area is always one. Yet for any fixed positive position, its width eventually becomes too small to reach you. At zero we can assign the value zero at every stage. So these functions converge to zero at every point, but the integrals remain one.

The issue is not that the graphs fail to become small in most places. In fact, at any one stage, the graph is nonzero on a set of very small measure. The problem is that the height increases just fast enough to preserve area. An ordinary bound by a different number at each stage says little about what the integral does. We need one function that holds the entire sequence in check.

Here is a second failure that looks entirely different. Work on the whole real line. At stage n, place a rectangle of height one and width one between n and n plus one. Its area is again one. Every fixed point of the line eventually lies to the left of the traveling rectangle, so the functions converge pointwise to zero. This time there is no concentration: the heights are uniformly bounded by one. Instead, the mass escapes to infinity. On a domain of infinite measure, the constant function one is not integrable, so it cannot serve as the bound required by dominated convergence.

These examples tell us what to look for. To control an integral, we must prevent both indefinitely high peaks on tiny sets and the migration of significant mass to ever more distant regions. An integrable majorant accomplishes both, without telling us exactly where the approximating functions are concentrated.

## What domination actually asserts

Consider a sequence of measurable real-valued functions on a measure space, converging almost everywhere to a function f. The domain could be a finite interval, the entire line, or an abstract space carrying a measure. Suppose there exists a single nonnegative measurable function g whose integral is finite and such that the absolute value of each approximating function never exceeds g, except perhaps on a null set.

The theorem then says two things. First, the limiting function f is integrable and its integral is the limit of the integrals. Second, something stronger is true: the integral of the absolute difference between the approximating function and f approaches zero. We call this convergence in the L-one norm.

The word *single* is doing work. If for every n you could choose a different integrable bound, you could simply bound a function by its own absolute value and learn nothing. Even if all those individual integrals are finite, there need not be a common integrable bound. What matters is a common envelope that limits the cost of the entire family.

Almost-everywhere convergence is enough. We do not ask for convergence at every exceptional point. On a complete measure space, changing function values on a null set does not change their Lebesgue integrals. On an arbitrary incomplete measure space, it is safer to work with measurable representatives and a specified measurable common exceptional null set. The theorem is about what the measure can detect, not about every microscopic pointwise detail.

Let us test the theorem before proving it. On the unit interval, let the nth function be x to the nth power. For any x below one, repeated multiplication eventually drives the value to zero. At the single endpoint x equals one, the value stays one. Thus the sequence converges almost everywhere to zero. Each function lies between zero and one; the constant function one is integrable on the unit interval. Dominated convergence predicts that their integrals tend to zero. Direct integration agrees: the integral is one divided by n plus one.

The exact formula is useful as a check, but the theorem applies to functions for which we cannot evaluate each integral explicitly. It converts qualitative information about a pointwise limit plus quantitative information about a uniform envelope into a statement about total mass.

## How Fatou's lemma does the work

The proof is particularly satisfying because the heavy machinery has already been developed. Fatou's lemma says that for nonnegative measurable functions, the integral of their pointwise lower limit is no greater than the lower limit of their integrals. It is a one-sided assertion; mass may disappear in the limit, as our examples show.

Why should adding an integrable envelope turn that one-sided result into an equality? Assume first that every function is real-valued. Because the absolute value of the nth function is at most g, both g plus that function and g minus that function are nonnegative. Since the nth function tends to f almost everywhere, these two nonnegative sequences tend, respectively, to g plus f and g minus f.

Apply Fatou's lemma to the first family. Its conclusion tells us that the integral of g plus f is no larger than the lower limit of the integrals of g plus the approximations. Every integral here is finite, because it is controlled by twice the integral of g. Subtract the fixed integral of g. We learn that the integral of f is at most the lower limit of the approximate integrals.

Now repeat the argument with g minus each function. The minus sign reverses the direction of the comparison when we rearrange. We obtain that the integral of f is at least the upper limit of the approximate integrals. But the lower limit can never exceed the upper limit. We have squeezed both between the same number, the integral of f. Therefore the integrals converge to the right answer.

That is the heart of the dominated convergence theorem: a positive buffer lets us apply a one-sided principle from both directions. The proof does not ask for a derivative, continuity, an interval domain, or a finite total measure. It uses measurability, almost-everywhere convergence, and the finite integral of the shared envelope.

There is an even sharper conclusion. Since both the limit and the approximations have absolute value at most g almost everywhere, the difference has absolute value at most twice g. The absolute difference itself tends to zero almost everywhere. Applying the same Fatou argument to this nonnegative sequence shows that its integral tends to zero. This is why dominated convergence gives not just the right total integral, but convergence in the L-one distance between functions.

For complex-valued functions, the same result holds. We can apply the real-valued theorem to real and imaginary parts, or handle the nonnegative absolute differences directly. The absolute value is what prevents cancellation from concealing a large error.

## What the theorem does not say

An integral being bounded is not the same as a family being dominated by one integrable function. Our narrow, tall rectangles have every integral equal to one. Even their absolute integrals equal one. But no single integrable function can lie above all of them, because near zero their heights grow without bound in a way that forces the envelope's integral to diverge.

Likewise, convergence in measure by itself is insufficient. A function can be large on an increasingly small exceptional set, and the exceptional set can carry all the mass. Convergence in measure says the location of significant error becomes rare; it says nothing about how high the error may become there.

Uniform convergence also needs to be interpreted with care. If two functions differ by at most epsilon everywhere on a domain of finite measure, the absolute difference of their integrals is at most epsilon times that total measure. That is strong. But on the whole real line, a tiny constant error spread over an infinite domain need not have a finite integral. Even uniform convergence does not by itself justify exchanging integrals over an infinite-measure space.

Nor does the theorem promise that a pointwise limit is differentiable, continuous, or free of sharp corners. It is a statement about integrals and L-one convergence. Additional preservation properties require additional hypotheses.

## A practical way to find the right envelope

Suppose a family of functions is produced by multiplying a fixed integrable density by a factor that never exceeds one in absolute value. Then the density itself is an integrable majorant. You can concentrate on verifying the pointwise limit of the factor. For instance, on the positive real line consider the density e to the minus x multiplied by a factor between zero and one, such as x divided by x plus n. At each fixed x, the factor tends to zero. The exponential is integrable on the half-line. So the integrals tend to zero without any clever substitution.

This technique is especially valuable with parameters. Imagine an integral depending on a parameter t. If the integrand approaches a limiting integrand at almost every point as t tends to a target, and if one integrable majorant works for every t sufficiently close to that target, then you may pass the parameter limit through the integral. That supplies a continuity theorem for a large class of parameter-dependent integrals.

Differentiation under an integral sign is subtler. There the objects to dominate are usually *difference quotients*, not merely the original integrands. A bound for the original functions alone cannot justify pulling a derivative through the integral. To do so, one proves that those difference quotients converge and are dominated by an integrable function, or invokes a more specialized theorem whose hypotheses guarantee the same control.

A useful diagnostic is to name the exact sequence to which the theorem will be applied. Is it the integrand itself? A family of difference quotients? A truncation? A series of partial sums? The correct dominating function must bound those very objects. Many invalid proofs hide the difficulty by saying only that the functions are bounded, without identifying a bound whose integral is finite.

## From exchanging limits to measuring error

The theorem can also be understood as a statement about approximation. If you replace a complicated integrable function by a sequence of easier ones, pointwise convergence alone is not enough to trust the total quantities. Under domination, the total absolute error tends to zero. This gives a reason numerical approximations and probabilistic expectations behave well when a common envelope is available.

There are more flexible theories of when integrals converge. One can sometimes replace a fixed majorant with uniform integrability together with control over mass that might escape to infinity. Those ideas matter in probability and functional analysis. But domination is the first general-purpose tool worth mastering because its proof is short, its conclusion is strong, and its failure examples explain exactly what it protects.

When you see an integral and a limit sitting next to one another, do not start by interchanging them. Ask where the mass could go. Could it spike? Could it travel away? Can one integrable function surround the whole family? If the answer to that last question is yes, and the pointwise limit exists almost everywhere, dominated convergence allows the exchange and says the functions themselves become close in total absolute error.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Dominated convergence theorem

Let \((X,\Sigma,\mu)\) be a measure space. Let \(f_n:X\to\mathbb C\) be measurable, with \(f_n\to f\) almost everywhere. If \(g\in L^1(\mu)\), \(g\ge0\), and \(|f_n|\le g\) almost everywhere for every \(n\), then \(f\in L^1\) and

\[
\lim_{n\to\infty}\int_X f_n\,d\mu=\int_X f\,d\mu,
\qquad \lim_{n\to\infty}\int_X|f_n-f|\,d\mu=0.
\]

Take a common conull set on which all the bounds and the pointwise convergence hold. For real functions, Fatou applied to \(g+f_n\) and \(g-f_n\) gives

\[
\int(g+f)\le\liminf_n\int(g+f_n),\qquad
\int(g-f)\le\liminf_n\int(g-f_n).
\]

Because \(\int g<\infty\), rearranging yields \(\int f\le\liminf_n\int f_n\le\limsup_n\int f_n\le\int f\). The second conclusion follows by applying the same theorem to \(|f_n-f|\le2g\) (or directly via Fatou applied to \(2g-|f_n-f|\), avoiding circularity). For complex functions use the real and imaginary parts.

### Three counterexamples and one good example

1. **Concentration:** \(f_n(x)=n1_{(0,1/n)}(x)\) on \([0,1]\); \(f_n\to0\) pointwise, but \(\int f_n=1\). No integrable common majorant exists.
2. **Escape to infinity:** \(f_n=1_{(n,n+1)}\) on \(\mathbb R\); \(0\le f_n\le1\) and \(f_n\to0\) pointwise, but \(\int f_n=1\). The constant majorant is not integrable on \(\mathbb R\).
3. **Convergence in measure is not enough:** The first example converges in measure and in fact pointwise everywhere, but not in \(L^1\).
4. **Domination:** \(f_n(x)=e^{-x}x/(x+n)\) on \((0,\infty)\) satisfies \(|f_n|\le e^{-x}\in L^1\) and \(f_n\to0\) pointwise, so \(\int f_n\to0\).

### Parameter differentiation: identify the dominated objects

If \(F(t)=\int_X h(t,x)\,d\mu(x)\) and for some \(t_0\) the difference quotients \([h(t_0+s,x)-h(t_0,x)]/s\) converge almost everywhere to \(k(x)\) as \(s\to0\), and their absolute values are bounded by a common \(G\in L^1\) for all sufficiently small nonzero \(s\), then \(F'(t_0)=\int k\,d\mu\). This requires \(F(t)\) to be defined in the neighborhood under discussion. Merely bounding \(|h(t,x)|\) is not a replacement for bounding difference quotients.

### Exercises with answers

1. **Finite domain:** Show that on \(\mu(X)<\infty\), \(|f_n|\le M\) and \(f_n\to f\) almost everywhere imply \(\|f_n-f\|_1\to0\). **Answer:** Take \(g=M1_X\in L^1\) and apply DCT.
2. **Narrow spikes:** Could a nonnegative \(g\in L^1([0,1])\) dominate every \(n1_{(0,1/n)}\)? **Answer:** No. DCT would contradict the constant integrals; directly, on \((1/(n+1),1/n)\) the envelope must be at least \(n\), producing a harmonic-type divergence.
3. **A singular but integrable envelope:** On \((0,1)\), let \(f_n(x)=x^{-1/2}1_{(1/n,1)}\). What is the limit of the integrals? **Answer:** The bound \(g(x)=x^{-1/2}\) is integrable with integral \(2\); DCT gives \(\int f_n\to2\).
4. **Where does continuity come from?** Let \(t\mapsto h(t,x)\) be continuous at \(t_0\) for almost every \(x\), and suppose \(|h(t,x)|\le g(x)\in L^1\) for \(t\) near \(t_0\). **Answer:** Apply DCT to every sequence \(t_n\to t_0\); \(F(t)=\int h(t,x)\,d\mu\) is continuous at \(t_0\).

### Sources

- Sheldon Axler, *Measure, Integration & Real Analysis*, integration and convergence chapters (open access at https://measure.axler.net/).
- MIT OpenCourseWare, *18.125 Measure and Integration*, lectures 4–5 and 12–13 (Fatou, dominated convergence, convergence in measure): https://ocw.mit.edu/courses/18-125-measure-and-integration-fall-2003/pages/lecture-notes/.
- Terence Tao, *An Introduction to Measure Theory*, material on convergence theorems: https://terrytao.wordpress.com/books/an-introduction-to-measure-theory/.
