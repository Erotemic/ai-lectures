# 003000 — From Nearby Inputs to Nearby Outputs: Limits and Continuity

**Track:** Analysis from First Principles. **Background:** real numbers, absolute value, inequalities, and sequence convergence. **Theme:** how output tolerances become input tolerances, including the difference between approaching a point and evaluating at the point.

<!-- BEGIN SPOKEN LECTURE -->

# From Nearby Inputs to Nearby Outputs: Limits and Continuity

Here is a function that appears to have a problem at the number one. Its formula says: square the input, subtract one, and divide by the input minus one. Enter two, and the answer is three. Enter one point one, and the answer is two point one. Enter zero point nine, and the answer is one point nine. But enter exactly one and the denominator is zero. The rule gives no output.

Now ask a different question. Not what is the value at one, but what happens to the output as the input gets arbitrarily close to one? Factoring the numerator reveals that, wherever the original formula is defined, it is simply the input plus one. The values approach two. There is a hole in the domain, but no uncertainty about the number the outputs approach.

This example exposes a distinction at the heart of analysis. A function's value at a point is information about one input. Its limit at that point concerns an entire neighborhood of inputs. Continuity is the condition that the two pieces of information fit together.

## What a limit asks us to control

Suppose a function takes real inputs and gives real outputs. We are interested in inputs approaching a particular number a, and we suspect that the outputs approach a number L. We could inspect increasingly accurate samples, but a graph or a table cannot settle a question about every possible nearby input. There could always be a narrow spike we missed.

Instead, we make a guarantee. A function approaches L as its input approaches a if, for every requested positive output error epsilon, there is a positive input distance delta with this property: whenever an allowed input differs from a by less than delta, but is not equal to a, its output differs from L by less than epsilon.

Epsilon measures how accurate an output must be. Delta tells us how close the input must be. The precise sizes can depend on the function, the location a, and the requested tolerance. The guarantee has to hold for every allowed input in that punctured neighborhood—not merely for some well-chosen sequence of test points.

Why exclude the input a itself? Because a limit describes approach, not evaluation. Our opening function is undefined at one, yet has a perfectly good limit there. We could even assign it the value seventeen at one without changing that limit. The behavior around the point would remain the same.

For the factored formula, the proof is almost immediate. Away from one, the output is the input plus one. Its error relative to two equals the input's distance from one. Whatever positive output tolerance someone asks for, we can choose the input tolerance to be exactly that amount. Every allowed input satisfying the distance requirement then gives an output satisfying the error requirement. We have proved the limit is two.

Notice how different this is from plugging one into an undefined expression. We never had to make sense of division by zero. We used valid inputs near one, and a bound that works for all of them.

## A proof in which choosing delta requires work

The factored example had a convenient feature: output error and input error were equal. Usually they are not. Consider squaring. Suppose we want to prove that the square of x approaches four when x approaches two.

The difference between x squared and four factors as x minus two, times x plus two. The first factor is small when x is near two. The second factor creates a difficulty: if we do not know how large x plus two is, simply saying that the first factor is small does not yet provide an error bound.

The solution is to restrict attention to inputs within one unit of two. Then x lies between one and three, so x plus two lies between three and five. Its absolute value is less than five. Consequently, the output error is less than five times the input distance.

Now a skeptic hands us any positive epsilon. We choose delta to be the smaller of one and epsilon divided by five. The distance from two is then smaller than one, allowing our bound on the second factor. It is also smaller than epsilon divided by five, forcing the product to be smaller than epsilon. That finishes the proof.

This little argument has a reusable structure. To control a product, first keep the supposedly harmless factor bounded in a neighborhood, and then make the genuinely small factor small enough. One learns to choose delta by working backward from the desired output error.

A formula often behaves differently at different input locations. Around x equals two, squaring changes by approximately four times a small change in x. Around x equals one hundred, the same input error can produce a much larger output error. Continuity promises the existence of a suitable delta at each point; it does not automatically promise one delta that works everywhere on the entire number line.

## What continuity adds

A function is continuous at an input a when it is defined at a and its outputs approach the actual value at a as nearby valid inputs approach a. In other words, the limit exists and equals the function value.

For the formula with a hole at one, the limit is two. If we leave the function undefined at one, it is not continuous there. If we define its value at one to be seventeen, it is still not continuous: nearby outputs approach two, but the assigned value is seventeen. If we instead define the value at one to be two, the hole is repaired. The function becomes exactly x plus one at every real input, and it is continuous at one.

We call this a removable discontinuity because one carefully chosen definition at the missing or incorrect point repairs continuity. Not every discontinuity can be repaired that way.

Think of a light switch. Define a function that outputs zero for every negative input and one for every input that is zero or positive. As we approach zero from the left, the outputs stay at zero. As we approach from the right, they stay at one. No single real number can be the limit from both directions. Changing only the value at zero cannot make these two sides agree.

There are also functions whose values grow without bound near a point, such as one divided by the square of x as x approaches zero through nonzero inputs. That behavior differs from both a removable hole and a finite jump. The phrase discontinuity names a failure of the continuity condition; the reason for failure still matters.

For a function defined on an interval, continuity at an endpoint is interpreted using inputs within its domain. The square-root function, for example, is continuous at zero when viewed as a real-valued function on the nonnegative real numbers. We approach zero from the side where the function is defined. There is no obligation to evaluate real square roots at negative inputs.

## Turning continuity into algebra

Individual epsilon-delta proofs need not be repeated from scratch for every familiar expression. Limit laws let us build new continuous functions from known ones. The sum of two functions continuous at a is continuous there: given a desired total output error, make each summand's error less than half that amount. Use the smaller of the two input tolerances so both promises hold at once.

Products need a little more care, just as squaring did. Near a, a continuous function is bounded: its values stay near its finite value at a. Once that factor is bounded, differences of products can be controlled by splitting them into two terms. Division is continuous wherever the denominator is nonzero. The nonzero condition matters because a tiny input change can otherwise pass through division by zero.

It follows that polynomials are continuous everywhere on the real line, and rational expressions are continuous wherever their denominators do not vanish. Composition works too: if an inner function is continuous at a, and an outer function is continuous at the inner function's value, then their composition is continuous at a. This is why a long expression built from familiar continuous operations usually behaves predictably—provided we check its domain.

The limit laws are theorems with hypotheses, not permission to perform every symbolic substitution. Canceling a factor in the opening example was legitimate only away from one. The cancellation established a limit, but did not retroactively define the original expression at the excluded input.

## A second definition using sequences

There is a striking alternative to the epsilon-delta formulation. A function is continuous at a if every sequence of allowed inputs converging to a produces a sequence of outputs converging to the actual value of the function at a.

To see the easy direction, assume continuity. Take any input sequence approaching a. Ask for an arbitrary output tolerance. Continuity gives an input tolerance that guarantees it. Because the input sequence converges, all its sufficiently late terms fall within that input tolerance. Therefore all the corresponding outputs fall within the requested output tolerance. The outputs converge to the value at a.

What about the converse? Suppose continuity fails. Then there is some fixed positive output error that cannot be controlled, no matter how close we demand the inputs be. For each positive integer n, choose an allowed input within one divided by n of a whose output still misses the target by at least that fixed error. The chosen inputs converge to a, yet the outputs do not converge to the function value. This contradicts the sequence test.

So the two formulations are equivalent for functions on subsets of the real line. One describes whole neighborhoods at once. The other tests every possible approach through a sequence. This equivalence connects the analysis of functions to the analysis of infinite lists, and it becomes especially valuable when the inputs are vectors, matrices, or other mathematical objects with a notion of distance.

An important warning: checking one sequence, or even ten thousand, is not enough to prove continuity. The sequential criterion says **every** converging sequence of valid inputs. But finding just one offending sequence is enough to disprove continuity. For the switch function, positive inputs approaching zero give outputs one, whereas negative inputs approaching zero give outputs zero.

## From pointwise control to mathematical confidence

Continuity does not mean that every function is smooth, differentiable, or physically gentle. The absolute-value function is continuous at zero even though its graph has a sharp corner there. Nor does continuity assert that a change of one fixed size in input is always safe everywhere. Its promise is local: for each point and each output tolerance, an appropriate input tolerance exists.

What it does provide is a way to transfer accuracy. If measurements or calculations bring the input sufficiently close to a chosen point, continuity guarantees that the output approaches the correct value there. If the guarantee fails, a graph or a long list of sample values may conceal the failure.

The hole at one began as a question that looked computational: what happens when a denominator becomes zero? The more useful mathematical question was whether outputs at nearby valid inputs settle toward a definite number. Once that number is known, continuity asks whether the function's actual value agrees with it.

That distinction—approach versus evaluation, and requested accuracy versus guaranteed input control—is the foundation for treating functions rigorously rather than trusting pictures alone.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(D\subseteq\mathbb R\) and let \(a\) be an accumulation point of \(D\). A function \(f:D\to\mathbb R\) has limit \(L\) at \(a\) if

\[
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ |f(x)-L|<\varepsilon.
\]

The accumulation-point qualification prevents vacuous limits at isolated inputs. If \(a\in D\), continuity at \(a\) means \(\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\ |x-a|<\delta\Rightarrow |f(x)-f(a)|<\varepsilon\). This relative-domain formulation also handles isolated points (where continuity holds trivially).

**Removable hole.** For \(x\ne1\),

\[
f(x)=\frac{x^2-1}{x-1}=x+1,\qquad
|f(x)-2|=|x-1|.
\]

Thus \(\lim_{x\to1}f(x)=2\) with \(\delta=\varepsilon\). Extending by \(f(1)=2\) makes the function continuous at 1; assigning a different value does not change the punctured limit.

**Quadratic epsilon-delta proof.** If \(|x-2|<1\), then \(|x+2|<5\), so \(|x^2-4|=|x-2||x+2|<5|x-2|\). Set \(\delta=\min\{1,\varepsilon/5\}\).

**One-sided discontinuity.** For \(s(x)=0\) if \(x<0\), \(s(x)=1\) if \(x\ge0\), the left limit at zero is 0 and the right limit is 1. No two-sided real limit exists.

**Sequential criterion.** For \(a\in D\), \(f\) is continuous at \(a\) if and only if for every sequence \(x_n\in D\) with \(x_n\to a\), one has \(f(x_n)\to f(a)\). For the converse, if continuity fails, choose \(\varepsilon_0>0\) and \(x_n\in D\) with \(|x_n-a|<1/n\) and \(|f(x_n)-f(a)|\ge\varepsilon_0\).

**Local limit laws.** If \(f(x)\to L\) and \(g(x)\to M\) as \(x\to a\), then \(f+g\to L+M\) and \(fg\to LM\). If \(M\ne0\), then \(f/g\to L/M\) on a suitable punctured neighborhood where \(g\ne0\).

### Exercises and guided answers

1. **Epsilon-delta witness:** Prove \(\lim_{x\to3}(2x+1)=7\). **Answer:** \(|(2x+1)-7|=2|x-3|\); use \(\delta=\varepsilon/2\).
2. **A repaired hole:** Set \(h(x)=(x^2-9)/(x-3)\) for \(x\ne3\). What value makes the extension continuous? **Answer:** Six, because \(h(x)=x+3\) off 3.
3. **A jump:** Why does changing only \(s(0)\) fail to make the switch function continuous? **Answer:** The left and right limits still disagree.
4. **Disproof by sequence:** For \(f(x)=1\) if \(x=0\) and \(f(x)=0\) otherwise, choose \(x_n=1/n\). **Answer:** Inputs converge to 0, outputs equal 0 and do not converge to \(f(0)=1\).
5. **Domain matters:** Why is \(\sqrt x\) continuous at 0 on \([0,\infty)\)? **Answer:** For \(x\ge0\), \(|\sqrt x-0|<\varepsilon\) whenever \(0\le x<\varepsilon^2\).

### References

- OpenStax, *Calculus Volume 1*, sections 2.4 and 2.5: https://openstax.org/books/calculus-volume-1/pages/2-4-continuity and https://openstax.org/books/calculus-volume-1/pages/2-5-the-precise-definition-of-a-limit
- Stephen Abbott, *Understanding Analysis*, sections on the functional limit and continuity.
- Terence Tao, *Analysis I*, continuity and limits of functions.
- [MIT OpenCourseWare, 18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/pages/lecture-notes/) — MIT 18.100B, lectures 9–11: limits and continuity.
