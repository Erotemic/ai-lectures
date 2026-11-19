# 007000 — Building an Integral from Finite Sums

**Track:** Analysis from First Principles. **Background:** continuity, completeness, bounded functions, and compact intervals. **Theme:** an integral exists only when upper and lower approximations can be forced to agree.

<!-- BEGIN SPOKEN LECTURE -->

# Building an Integral from Finite Sums

Suppose a reservoir receives water at a rate that changes throughout the day. A flow meter might report liters per minute at any instant. What we need at the end of the day is a quantity in liters: the total amount received.

If the flow rate were constant, we could multiply rate by duration. But with a varying rate, there is no single number that describes the whole interval. A natural idea is to cut the day into short pieces, treat the rate as nearly constant on each piece, multiply by the length of that piece, and add the results.

That idea leads to integration. But it also raises a mathematical question. Different sample times inside each piece can give different totals. Different partitions of the same interval can give different totals. Why should all these choices approach one well-defined number as the pieces become smaller?

The Riemann integral answers that question. It is not merely a symbol for area under a curve. It is the common value, when one exists, of increasingly accurate finite approximations to accumulated change.

## Starting with a function we can calculate

Consider the function that returns its input, on the interval from zero to one. If we think of its output as a rate, the rate grows steadily from zero to one. The total accumulation should be one half, corresponding geometrically to a triangle of base one and height one.

We can check that value without using the area formula. Divide the interval into n equal pieces. In each piece, sample the rate at the right endpoint. The first sample is one divided by n, the second is two divided by n, and the last is one. Each piece has width one divided by n.

The sum is one divided by n squared times the sum of the integers from one to n. The familiar formula for that integer sum tells us the approximation equals one half plus one divided by twice n. As n grows, the approximation approaches one half.

If we sample at left endpoints instead, the sum is one half minus one divided by twice n. Both choices approach the same number. Their difference is one divided by n. The calculation suggests that the sample choice becomes irrelevant as the partition becomes fine.

But we have proved this only for a particular function and two particular ways of sampling. A definition of integration must explain what happens for other functions, irregular partitions, and samples chosen in less convenient ways.

## The precise finite object

Begin with a bounded real-valued function on a closed interval from a to b. Choose finitely many points, starting at a and ending at b, in strictly increasing order. Those points partition the interval into smaller subintervals.

In each subinterval, select a sample point. Evaluate the function there, multiply the value by the width of that subinterval, and add the products. This is a tagged Riemann sum. It is a finite number. We can compute it without using an integral symbol or any limit.

The width of the largest subinterval is called the mesh of the partition. A partition is fine when its mesh is small, not simply when it contains many subintervals. We could split one tiny portion into a million pieces while leaving another large portion untouched. The number of pieces would be enormous, yet the approximation could remain poor where the rate varies in the long piece.

For a bounded function to be Riemann integrable, there must be one number I such that every tagged sum is close to I whenever the mesh is sufficiently small. The phrase every tagged sum is doing real work. We do not get to select only the convenient sample points or a special sequence of partitions.

Instead of handling all those choices directly, there is a useful equivalent test based on upper and lower bounds.

## Upper and lower sums as certificates

In a given subinterval, take the least upper bound of the function values in that subinterval, and also their greatest lower bound. These bounds exist because the function is bounded and the real numbers are complete. Multiply each bound by the subinterval width.

Adding the lower contributions gives a lower sum. Adding the upper contributions gives an upper sum. Every tagged sum for that partition lies between those two numbers. The lower sum is pessimistic and the upper sum optimistic, in the sense of bounding possible accumulation.

If we refine a partition by inserting more points, its lower sum cannot decrease and its upper sum cannot increase. Cutting a rectangle into more pieces allows its upper estimate to fit the function more closely, never more loosely, and similarly improves the lower estimate.

So the two families of estimates close in on whatever value the integral might have. We say the function is Riemann integrable exactly when, for every positive tolerance, some partition has an upper sum minus lower sum smaller than that tolerance.

Why does that criterion work? Because all lower sums are bounded above by all upper sums, even when they come from different partitions. We can combine the partitions into a common refinement to see this. The largest possible lower estimate and the smallest possible upper estimate are therefore well defined. If their gap can be made arbitrarily small, they must coincide. Their common value is the integral.

This supplies more than a picture. If we have found a partition whose upper and lower sums differ by at most one hundredth, then every tagged sum using that partition lies in a certified interval of width at most one hundredth. For integrability we need the stronger conclusion that sufficiently fine partitions, regardless of their tags, approach the same value.

## Why continuous functions are integrable

A continuous function on a closed, bounded interval is Riemann integrable. The proof reveals why closed bounded intervals are such effective domains in analysis.

Continuity at a point tells us that sufficiently close inputs have close outputs near that point. To control every subinterval in a partition with one common width, we need a stronger-sounding fact: uniform continuity. It says that for any desired output tolerance, there is one input tolerance that works everywhere on the interval, not a different one at each point.

A continuous function on a closed, bounded real interval is uniformly continuous. Here is the compactness idea behind that theorem. If no common input tolerance existed, we could find pairs of inputs getting arbitrarily close to each other while their outputs stayed separated by some fixed positive amount. The first inputs would have a convergent subsequence inside the closed interval. The paired inputs would converge to the same limit, since their distances tend to zero. Continuity would then force both sets of outputs toward the same number, contradicting the fixed separation.

Now choose a partition whose largest subinterval is smaller than the uniform-continuity tolerance. Throughout any one subinterval, the function values can differ by no more than the selected output tolerance. Therefore the difference between the upper and lower contribution from that piece is at most that output tolerance times the piece's width.

Add over all pieces. The widths sum to the length of the whole interval. Thus the total upper-minus-lower gap is at most the output tolerance times the interval length. We can make that gap as small as we wish. The function is integrable.

The proof has a useful shape. Compactness turns pointwise control into a single uniform scale. That uniform scale turns small subintervals into narrow upper-lower gaps. The sum of those gaps gives a global guarantee.

## Continuity is sufficient, not necessary

A function can have a jump and still be Riemann integrable. Consider a function that is zero before the midpoint of the interval from zero to one and one from the midpoint onward. It is discontinuous at one point.

If a partition contains the midpoint, every subinterval away from that point has constant function value. The only ambiguity occurs in the piece touching the jump. We can confine that piece to an arbitrarily small width. Its upper-minus-lower contribution is at most that width, and every other contribution is exact. The integral exists and equals one half.

So discontinuity at a single point does not necessarily obstruct integration. In fact, all monotone bounded functions on a closed interval are integrable, even though they may jump. For an increasing function, use equal-width pieces. On each piece, the difference between its upper and lower values is the increase from one endpoint to the other. When we add those increases, they telescope into the total rise from the first endpoint to the last. Multiply by the common piece width, and the gap tends to zero.

These are not just special tricks. They explain that integrability is about controlling the total influence of oscillation over the interval, not demanding a perfect absence of discontinuities.

## A bounded function that cannot be integrated this way

There is also a sharp counterexample. Define a function on the interval from zero to one that equals one at rational inputs and zero at irrational inputs.

Every nonempty open subinterval contains both rational and irrational numbers. Consequently, in every partition piece of positive length, the supremum of the function values is one and the infimum is zero. Every upper sum is one; every lower sum is zero. No matter how fine the partition becomes, the gap remains one.

This function is bounded, and every tagged sum is a perfectly legitimate finite calculation. But different choices of sample points can make the sums behave completely differently. If all sample points are rational, the sum is one. If all are irrational, the sum is zero. There is no single number to which all sufficiently fine sums must converge.

The function is not Riemann integrable. Calling it an area problem does not repair the missing convergence. To integrate broader classes of functions, mathematics develops other theories, including the Lebesgue integral. That broader theory is not needed to understand the Riemann definition, but the counterexample shows why an integral requires hypotheses.

## Signed accumulation and orientation

A further conceptual point is that an integral is a signed quantity. If a function is positive on one piece of an interval and negative on another, its contributions can cancel. That makes sense for velocity, where forward and backward motion affect net displacement differently, or for a flow rate that can reverse direction.

The integral of the absolute value of the rate, by contrast, measures a different quantity: accumulated magnitude rather than net change. Neither calculation should be confused with the other.

Also, reversing the integration interval reverses the sign of the integral. This is consistent with thinking of integration as oriented accumulation. Adding the contributions from a to c and from c to b gives the total contribution from a to b. Those rules follow from the finite sums and survive in the limit.

The quantity obtained by integrating a continuous rate over an interval is a number, not a function, although we can create a new function by allowing the upper endpoint to vary. That distinction will matter when we ask whether accumulation can be undone by differentiation.

## What has actually been constructed

We began with a changing flow rate and tried to recover a total amount. Finite sums provide approximations. Upper and lower sums tell us when different approximations are forced to agree, while completeness ensures that the common boundary value belongs to the real numbers.

Continuous functions on compact intervals pass the integrability test because they are uniformly continuous. Some discontinuous functions pass as well; highly oscillatory functions such as the rational-indicator example do not. The definition does not erase these differences.

The integral is therefore a rigorous form of accumulation, built from the behavior of approximating sums. It has not been defined as the reverse of a derivative. Instead we have two independently meaningful constructions: one measures local rates through ratios, and the other combines local contributions through sums. Their relationship, when its hypotheses hold, is one of the central results of calculus.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Tagged partitions.** Let \(f:[a,b]\to\mathbb R\) be bounded, \(a<b\). A partition is \(P=(a=x_0<\dots<x_n=b)\). Tags satisfy \(\xi_i\in[x_{i-1},x_i]\). Define
\[
 S(f,P,\xi)=\sum_{i=1}^n f(\xi_i)(x_i-x_{i-1}),\qquad
 \|P\|=\max_i(x_i-x_{i-1}).
\]
Riemann integrability means \(\exists I\in\mathbb R\) with \(\forall\varepsilon>0\,\exists\delta>0\) such that \(\|P\|<\delta\) implies \(|S(f,P,\xi)-I|<\varepsilon\) for every tagging \(\xi\).

**Upper and lower sums.** Write \(M_i=\sup_{x\in[x_{i-1},x_i]}f(x)\), \(m_i=\inf_{x\in[x_{i-1},x_i]}f(x)\), and
\[
 U(f,P)=\sum_i M_i\Delta x_i,\qquad L(f,P)=\sum_i m_i\Delta x_i.
\]
For any \(P\), \(L(f,P)\le S(f,P,\xi)\le U(f,P)\). The Darboux criterion states that \(f\) is Riemann integrable iff \(\inf_P U(f,P)=\sup_P L(f,P)\), equivalently \(\forall\varepsilon>0\,\exists P: U(f,P)-L(f,P)<\varepsilon\).

**Refinement and fine partitions.** If \(Q\) refines \(P\), then \(L(f,P)\le L(f,Q)\le U(f,Q)\le U(f,P)\). To prove the Darboux criterion yields the arbitrary-tag/mesh formulation, fix a partition \(P_0\) with small \(U-L\). For any fine partition \(Q\), only cells of \(Q\) crossing the finitely many boundaries of \(P_0\) need extra error control; boundedness bounds that error by a constant times the mesh of \(Q\). A common refinement then compares the estimates.

**Continuous functions.** Compactness plus continuity gives uniform continuity. For \(\varepsilon>0\), choose \(\delta>0\) so that \(|x-y|<\delta\Rightarrow|f(x)-f(y)|<\varepsilon/(b-a)\). Then \(\|P\|<\delta\Rightarrow U(f,P)-L(f,P)\le\varepsilon\).

**Monotone functions.** For nondecreasing \(f\), uniform partition width \(\Delta=(b-a)/n\) yields
\[
 U(f,P)-L(f,P)=\Delta\sum_{i=1}^n(f(x_i)-f(x_{i-1}))
 =\frac{b-a}{n}\bigl(f(b)-f(a)\bigr)\to0.
\]

**Two examples.** \(f(x)=x\) on \([0,1]\): right sums \((n+1)/(2n)\), left sums \((n-1)/(2n)\), integral \(1/2\). For \(f=1_{\mathbb Q\cap[0,1]}\), every partition has \(U=1,L=0\); thus it is not Riemann integrable.

### Exercises and guided answers

1. **Riemann sum:** Find the right-endpoint equal-partition sum for \(f(x)=2x\) on \([0,1]\). **Answer:** \((n+1)/n\), converging to \(1\).
2. **Mesh:** Can a partition have one million subintervals but mesh \(1/2\)? **Answer:** Yes; leave one subinterval of width \(1/2\), and partition the other half finely.
3. **Single jump:** Find the integral on \([0,1]\) of \(f(x)=0\) for \(x<1/2\) and \(f(x)=3\) for \(x\ge1/2\). **Answer:** \(3/2\).
4. **Non-integrability:** Why is the rational-indicator function not Riemann integrable? **Answer:** Every nondegenerate subinterval has infimum zero and supremum one, hence \(U-L=1\) for any partition.
5. **Net versus total:** Evaluate \(\int_{-1}^{1}x\,dx\) and \(\int_{-1}^{1}|x|\,dx\). **Answer:** Signed integral \(0\); absolute integral \(1\).

### References

- OpenStax, *Calculus Volume 1*, section 5.2, “The Definite Integral”: https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral
- Wikipedia, “Riemann integral”: https://en.wikipedia.org/wiki/Riemann_integral
- Stephen Abbott, *Understanding Analysis*, the Riemann integral and uniform continuity.
- Terence Tao, *Analysis I*, Riemann integration and Darboux sums.
- [MIT OpenCourseWare, 18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/pages/lecture-notes/) — MIT 18.100B, lectures 17–18: Riemann integral and integrability.
