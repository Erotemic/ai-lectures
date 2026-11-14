# 002000 — Small Errors, Large Consequences: Rounding and Error Propagation

**Track:** Numerical Analysis and Reliable Computation. **Background:** arithmetic, powers of two, and the idea of an approximation. **Theme:** separate rounding errors from conditioning, derive practical bounds, and identify stable ways to perform the same mathematical operation.

<!-- BEGIN SPOKEN LECTURE -->

# Small Errors, Large Consequences: Rounding and Error Propagation

You run two programs intended to calculate the same sum. One returns zero. The other returns one. Both use ordinary floating-point arithmetic, neither crashes, and neither reports an overflow. How can that happen? Consider just three numbers: ten quadrillion, one, and negative ten quadrillion. Their exact mathematical sum is one. But a common finite-precision calculation adds the first two, rounds away the one, and then subtracts ten quadrillion to obtain zero.

This example is not a mysterious hardware defect. It is the predictable consequence of representing a vast range of magnitudes with a finite number of bits. Numerical analysis begins when we ask what operations a computer actually performed, how rounding affected the result, and what guarantee we can make about the intended mathematical answer.

The distinction becomes important in scientific computing, optimization, machine learning, statistics, simulation, and any program whose result is supposed to carry mathematical meaning. A program can be free of memory errors and still deliver an answer with little numerical value. Reliability needs an account of the arithmetic itself.

## An arithmetic system with only a few digits

Before thinking about billions of binary numbers, imagine a toy calculator that keeps exactly three significant decimal digits after every operation. It can represent one point zero zero and one point zero one. It cannot represent one point zero zero four exactly at that scale. If rounding to nearest, the mathematical result one point zero zero four rounds back to one point zero zero.

Now repeatedly add zero point zero zero four, beginning at one point zero zero. After the first addition, the calculator returns one point zero zero. The next addition starts from the same rounded value and produces the same answer. Repeat this 250 times. The computed result can still be one point zero zero, even though the exact mathematical result is two.

This is an exaggerated toy example, but it illustrates a general phenomenon. The result of each operation becomes the input to the next. Once a small contribution has been discarded, subsequent operations may have no way to recover it. The error is caused by the sequence of rounding operations, not by an incorrect mathematical definition of addition.

Rearrange the arithmetic. Add the 250 small increments together first. Their exact sum is one, which the toy system can represent. Then add that one to the starting value and obtain two. Same mathematical terms, different numerical order, different result.

Floating-point addition is therefore not generally associative in the way real-number addition is. The identity 'a plus b plus c equals a plus b plus c regardless of parentheses' is a theorem for exact real arithmetic, but cannot simply be imported as a guaranteed property of rounded calculations.

## What a floating-point number contains

A typical floating-point representation has a sign, a significand, and an exponent. The exponent sets the scale; the significand stores a fixed amount of precision. Binary64, the common IEEE double-precision format, has 53 bits of significand precision when counting the implicit leading bit for normal numbers.

Near one, the gap between adjacent positive binary64 values is two to the power negative fifty-two. The unit roundoff under rounding to nearest is half that spacing, two to the power negative fifty-three. That is roughly one point one times ten to the negative sixteen. At much larger magnitudes, the absolute spacing is much larger. That is why adding one to ten quadrillion can disappear: neighboring representable numbers around that scale are separated by more than one.

We should keep two terms distinct. A unit in the last place, often called an ulp, refers to a spacing scale near a floating-point value, although exact conventions differ at exponent boundaries. Unit roundoff is the maximum relative rounding factor in the standard model for ordinary operations with normal results and no exceptional conditions. They are related, but they are not interchangeable constants in every formula.

The IEEE standard also specifies special values, signed zeros, infinities, NaNs, subnormal numbers, and rounding rules. These cases are important in practice. A simple relative error estimate that works for normal finite results may fail near underflow or on overflow. Every mathematical error bound is a conditional claim about a particular arithmetic model.

## The one-operation model

For a basic arithmetic operation with a real exact result that lies in the appropriate range, a widely used idealized model writes the computed result as the exact result multiplied by one plus a small error. The small relative error has magnitude at most the unit roundoff.

In symbols, we can say: floating point of a operation b equals the exact result times one plus delta, with delta's absolute value at most u. For correctly rounded operations under the model's hypotheses, this gives an accessible local guarantee. It does not mean that adding two nearby values always produces an accurate answer to the larger mathematical problem, because the inputs may already be approximations or the intended final answer may be sensitive to perturbations.

Consider a program that subtracts two nearly equal numbers. If those numbers are represented exactly, the subtraction itself may be exact under some circumstances. Yet if each operand was previously rounded, the difference can be extremely sensitive to the small errors they carried. Saying 'subtraction causes error' misses that distinction. The severe loss may come from *exposing* earlier input or evaluation errors through cancellation.

Suppose the exact quantities are one point two three four five six and one point two three four five five. Their difference is one hundred-thousandth. If we had rounded both values first to four significant decimal digits, both might become one point two three five, and their computed difference would be zero. The problem's relevant information was already lost before subtraction.

The condition number of subtraction captures the sensitivity. When the intended result is a minus b, a relative perturbation in a and b can be amplified by a factor on the order of the sum of their magnitudes divided by the magnitude of their difference. If the difference is tiny while the operands are large, the factor becomes enormous.

This is why we must distinguish a badly conditioned mathematical problem from an unstable algorithm. An algorithm can be well behaved relative to slightly perturbed inputs and still produce a large forward error when the underlying problem is highly sensitive. Conversely, a well-conditioned problem can be solved poorly by an algorithm that accumulates avoidable rounding.

## An exact sum, several floating-point answers

Let's revisit ten quadrillion, one, and negative ten quadrillion in binary64. The large positive and large negative values are representable at this magnitude, as is one. Adding the first two values mathematically produces ten quadrillion plus one, but rounding to binary64 loses the increment. Subtract the large number and the result is zero.

Change the order. First add the large positive and negative values. The result is exactly zero. Add one and the final result is one. For this triple, a different summation order recovers the exact answer.

This does not imply that always sorting values by size solves every summation problem. The behavior depends on signs, cancellations, distribution of magnitudes, and the accuracy required. Pairwise summation, compensation, and extended-precision accumulation offer different tradeoffs.

A useful practical lesson is to treat reduction order as part of an algorithm's numerical design. Parallel computations can group terms differently depending on execution scheduling or data partitioning. When a numerical result changes slightly between runs or hardware configurations, the reason may be a change in the order of rounded operations. That possibility should be investigated rather than treated as proof of a race condition or of random behavior.

## How errors accumulate in a long sum

Suppose we add n floating-point numbers one by one, from left to right. If each of the n minus one additions incurs a small relative rounding error, the errors can compound. A standard bound introduces a factor called gamma sub n minus one. It is the product of n minus one and the unit roundoff, divided by one minus that product, provided the product is less than one.

Then the absolute difference between the computed sum and the exact sum is bounded above by this gamma factor times the sum of the absolute values of all the terms. This is a worst-case bound for the standard model under appropriate assumptions, including no problematic underflow or overflow.

Notice the right-hand side uses the sum of *absolute* values, not the absolute value of the exact sum. If positive and negative terms nearly cancel, the exact sum can be small while the bound remains large. That is precisely when a modest absolute error can become a devastating relative error.

For a simple scale estimate, in binary64 the unit roundoff is about one point one times ten to the negative sixteen. After a million sequential additions, the gamma factor is approximately one point one times ten to the negative ten, if the denominator is near one. Multiply that by the sum of absolute input magnitudes to obtain a conservative error estimate. The bound does not assert that a particular million-term sum has that much error; it tells us what the model permits in the worst case.

This also shows why a numerical certificate should state both what is bounded and under which hypotheses. A small bound on absolute error may still be inadequate when the exact result is close to zero. A relative bound may be impossible without additional information about the inputs.

## Pairwise sums and compensation

One way to improve summation is to add terms in a balanced tree. Instead of accumulating every contribution into one running total, combine pairs, then pairs of partial sums, and so on. This reduces the number of rounding stages along any input's path from approximately n to approximately the logarithm of n. Under standard hypotheses, pairwise summation can have a substantially better worst-case error bound than naïve sequential summation.

Another approach is compensated summation, associated especially with William Kahan. It maintains a correction variable intended to capture small contributions lost during earlier rounding. At each step, the new input is adjusted by the correction, the sum is updated, and a new correction estimates what was lost in that update.

The method cannot conjure arbitrary information from nowhere. Its properties depend on the floating-point arithmetic and on how the code is compiled and executed. But it can improve accuracy dramatically in many practical sums. A careful implementation should be tested against a high-accuracy reference on datasets designed to expose cancellation and large differences of scale.

Kahan's work also reflects a broader philosophy of numerical software: mathematical identities and real hardware behavior must be examined together. A short program with a beautiful algebraic formula can be less reliable than a slightly longer version designed around the actual rounding model.

## A second route: change the formula before evaluating it

Suppose you want to evaluate the square root of one plus x, minus one, all divided by x, when x is a tiny positive number. Mathematically the expression is well defined for x nonzero and greater than negative one. Numerically, if x is small, the square root of one plus x is close to one, so subtracting one can destroy useful digits.

We can transform the expression algebraically. Multiply numerator and denominator by the conjugate, the square root of one plus x, plus one. The numerator becomes x. Cancel x, and the result is one divided by the square root of one plus x, plus one.

This second expression avoids subtracting two nearly equal numbers. For tiny x, it stays close to one half even if one plus x rounds to one. The mathematical functions are equal wherever the original expression is defined, but the floating-point evaluations can behave very differently.

If x is exactly zero, the original expression is undefined, even though the transformed expression evaluates to one half. The latter is the continuous extension at zero. A numerical routine must decide whether its contract is to evaluate the original partial function or to provide a continuous extension at that point. That is a specification decision, not just an optimization.

This is a powerful habit: before increasing precision or adding tests, ask whether the algebra can be reorganized into a better-conditioned evaluation pathway. Logarithmic and exponential functions have similar stable variants designed for small arguments. Stable numerical analysis often begins with mathematical reformulation.

## Error propagation can be predicted before running a program

Let's study a simpler computation: multiply ten measured quantities together. Suppose each input may be wrong by at most one percent relative to its true value. Even with exact arithmetic, the product can differ appreciably from the ideal product. If every factor is one percent too high, the combined factor is one point zero one raised to the tenth power, a little over one point one zero four six. So a collection of small input errors can produce more than ten percent output error.

That is sensitivity of the mathematical operation to uncertainty in its inputs. Rounding errors incurred while multiplying the represented values would add another layer of error. A careful computation should not combine those two sources and call them one vague 'floating-point inaccuracy.' Different remedies apply: better measurements address input uncertainty; improved evaluation order or precision addresses arithmetic effects.

For sufficiently small relative perturbations, a first-order estimate often adds the individual relative contributions. But a first-order approximation is not always a rigorous bound, especially when errors are large or the function is nonlinear near a sensitive point. If we need certification, we should derive an inequality with explicit ranges rather than rely only on a differential approximation.

## Conditioning belongs to the problem; stability belongs to the method

Consider a linear system with two equations whose coefficients are almost dependent. A tiny change in the input can change its solution greatly. That is conditioning: how sensitive is the exact answer to changes in the problem data?

Now choose an algorithm for solving it. A backward-stable algorithm returns the exact solution to a nearby problem, in an appropriate sense. This is an algorithmic property. It is valuable even for an ill-conditioned system, because it tells us that the computation has not introduced more error than can be accounted for by a small perturbation of the original data.

But backward stability does not promise a small error in the solution itself. If the problem is highly sensitive, nearby problems can have very different exact solutions. A responsible numerical report distinguishes 'we solved a nearby problem accurately' from 'our answer is close to the exact solution of this particular problem.'

The same distinction applies to summation. The exact sum of input numbers may be sensitive to small relative errors when large positive and negative terms cancel. A stable summation strategy can reduce avoidable arithmetic error while still leaving the final answer sensitive to uncertainty in the input values.

## What can a program actually certify?

A printed decimal with sixteen digits is not a sixteen-digit guarantee. Its apparent precision may reflect a formatting choice. To assess the answer, start with a mathematical specification. What quantity is intended? Are the input values exact measurements or estimates? Which operations are being performed? What floating-point format and rounding rules are assumed?

Next identify a useful error measure. Absolute error is the magnitude of computed minus exact. Relative error divides by the exact magnitude when it is nonzero. Backward error measures the smallest change in input data that makes the computed result exact. These quantities answer different questions; none replaces the others in every application.

A residual can be easy to calculate. For example, after computing a candidate solution to a linear system, multiply the matrix by the candidate and subtract the right-hand side. A small residual is evidence that the candidate nearly satisfies the equations. But converting that into a small forward error requires information about how the system responds to perturbations, often expressed through a condition number or another stability estimate.

For still stronger guarantees, one can use interval arithmetic with directed rounding, validated bounds, or exact rational checks where feasible. Such methods provide certificates with explicit assumptions and costs. Their purpose is to bridge the gap between ideal mathematics and finite arithmetic, rather than pretending the gap is absent.

## An experiment worth performing

Here is a small numerical study that can be run in almost any language with binary64 arithmetic. Compute the sum of ten quadrillion, one, and negative ten quadrillion in the listed order. Then compute it in the order large positive, large negative, one. Compare the results to the exact sum.

Next create a million small positive values and add them to a large accumulator. Compare ordinary sequential summation with a balanced or compensated method and with a high-accuracy summation routine. Observe not only which answer is closest, but how the result changes when the order changes.

Finally test the unstable square-root expression and its algebraically transformed version for successively smaller positive x. Observe where the direct expression loses resolution or becomes zero. Explain the behavior in terms of representable spacing and cancellation, rather than simply labeling the computer wrong.

This is the style of evidence that numerical software needs. Experiments expose behavior; mathematical bounds explain why it is possible; independent reference calculations establish the intended value when they can. Each part supports the others.

## The meaning of a trustworthy number

Return to the three-number sum. The exact answer is one. A floating-point calculation can return zero because it performed a sequence of rounded operations. Another ordering can return one. Neither outcome contradicts the laws of arithmetic; the two calculations implement distinct finite-precision procedures.

The deepest lesson is that numerical correctness is more specific than obtaining a plausible-looking decimal. We need a clear mathematical target, an implementation whose rounding behavior is understood, and a meaningful relationship between the returned value and the target.

Once we learn to ask which errors are inevitable, which are algorithmic, and which are amplified by the problem itself, numerical computation becomes something we can reason about. We can choose stable formulas, build error bounds, design independent checks, and sometimes prove that a returned answer lies within a certified range. That is how finite arithmetic can support rigorous conclusions about a mathematical world of exact numbers.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Standard relative error model.** For an operation \(\circ\in\{+,-,\times,/\}\) with normal finite result, correct rounding, no exceptional overflow/underflow, and representable inputs, \(\mathrm{fl}(a\circ b)=(a\circ b)(1+\delta)\), with \(|\delta|\le u\) under the usual model. For IEEE binary64, \(u=2^{-53}\).

**Sequential summation.** If \(s=\sum_{i=1}^n x_i\) and \(\hat s\) is a left-to-right floating sum, a standard absolute bound is \(|\hat s-s|\le \gamma_{n-1}\sum_i|x_i|\), where \(\gamma_k=ku/(1-ku)\), provided \(ku<1\) and the arithmetic satisfies the model.

**Condition of subtraction.** For \(f(a,b)=a-b\), a relative perturbation scale is \(\kappa\sim(|a|+|b|)/|a-b|\) for nonzero result; near cancellation it can be very large.

**Algebraic stabilization.** For \(x\neq0\), \(x>-1\), \((\sqrt{1+x}-1)/x=1/(\sqrt{1+x}+1)\). The second expression has a continuous extension to \(x=0\) with value \(1/2\).

**Binary64 sanity:** \(\mathrm{fl}(10^{16}+1)=10^{16}\) under round-to-nearest-even; hence \(\mathrm{fl}(\mathrm{fl}(10^{16}+1)-10^{16})=0\) but \(\mathrm{fl}(\mathrm{fl}(10^{16}-10^{16})+1)=1\).

### Exercises with answers

1. **Exercise:** Why does \(\sum_i|x_i|\) appear in a summation error bound? **Answer:** A near-zero exact sum may result from cancellation of large terms; the error can depend on the large intermediate magnitudes.
2. **Exercise:** Why is an ulp distinct from unit roundoff? **Answer:** The former describes local spacing; the latter is a relative bound in the standard rounding model.
3. **Exercise:** When is a backward-stable answer still far from the exact solution? **Answer:** When the mathematical problem is ill-conditioned, so a small input perturbation can yield a large solution change.
4. **Exercise:** What is the stable evaluation for \((\sqrt{1+x}-1)/x\) when \(x\) is small and nonzero? **Answer:** \(1/(\sqrt{1+x}+1)\).

### References

- David Goldberg, “What Every Computer Scientist Should Know About Floating-Point Arithmetic” (1991), https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, second edition, SIAM.
- James H. Wilkinson, *Rounding Errors in Algebraic Processes*, SIAM.
- William Kahan, “Further Remarks on Reducing Truncation Errors” and subsequent compensated summation analyses.
- IEEE 754 standard for binary floating-point arithmetic; consult the applicable edition for exact exceptional-case and rounding semantics.
