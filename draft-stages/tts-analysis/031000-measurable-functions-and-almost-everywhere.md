# 031000 — Measurable Functions: Seeing a Function Through Its Level Sets

**Track:** Analysis from First Principles. **Background:** sigma-algebras, null sets, real-valued sequences and continuity. **Question:** Which functions can we integrate by measuring the sets on which they take particular values?

<!-- BEGIN SPOKEN LECTURE -->

# Measurable Functions: Seeing a Function Through Its Level Sets

Suppose you are asked to integrate a function that is one at every rational number and zero at every irrational number on the unit interval. If you try to use Riemann sums, the function seems designed to defeat you. Every nonempty subinterval contains a rational and an irrational. Every upper sum is one, and every lower sum is zero. Making the partition finer does not resolve the difference.

Yet as a geometric area problem, the answer feels clear once we know how measure works. The rationals are countable, so their total Lebesgue measure is zero. The function is zero everywhere except on a set of measure zero. From the measure-theoretic point of view, it ought to have integral zero.

That intuition is correct, but a foundational question remains. We cannot integrate arbitrary functions merely because they have values. We need to know that the sets of inputs where their values meet a specified condition are measurable. The bridge between measuring sets and integrating functions is the concept of a *measurable function*.

## A function observed by threshold tests

Think of a function as a landscape, with its value representing height. Instead of inspecting the height at every single point, choose a threshold, perhaps one meter. Ask for the region where the landscape rises above that threshold. Choose two meters and ask again. Choose any real threshold and repeat.

If every region obtained in this way is measurable, then the function is measurable. More precisely, for a real-valued function defined on a measurable space, we require that the inputs at which the function exceeds a given real number form a measurable set, for every such threshold.

This is called measuring the *inverse image* of a half-line. We are not asserting that the set of output values itself must be measurable. We are asking about inputs whose outputs lie inside a given set. The direction matters. The preimage of a set of outputs is what connects a function to the sigma-algebra on its domain.

There are many equivalent versions of this condition. We can ask where the function is less than a threshold, or at most a threshold, or belongs to any open interval. The equivalence follows from complements and countable unions or intersections. For example, the region where a function is strictly greater than a is the union, over positive integers n, of regions where it is at least a plus one over n. Each of these is a countable threshold question. The countable nature of the sigma-algebra is what lets us change from one version to the other.

A continuous real-valued function is measurable when the domain has its Borel sigma-algebra. Indeed, the inverse image of an open subset of the real line is open, and open subsets belong to the Borel sigma-algebra. If we instead use the completed Lebesgue sigma-algebra on the domain, continuity still implies measurability because every Borel set remains Lebesgue measurable.

Now return to the rational-indicator function. The region where its value exceeds one half is precisely the rational numbers in the unit interval, a countable measurable set. The region where its value exceeds a threshold between zero and one is the same set, while other thresholds give either all points or none. It is measurable even though it is discontinuous everywhere.

So measurability is not a weaker form of continuity in the sense of a smaller uniform error. It is a different kind of regularity. It says the function can be observed through measurable threshold tests. It allows enormous discontinuity while still supporting integration.

## The two elementary building blocks

The simplest measurable functions are indicators: a function that equals one on a measurable set and zero outside it. If A is measurable, its indicator is measurable. This is immediate from the threshold test. In the other direction, if an indicator function is measurable, then the set it indicates must be measurable.

Now consider a function that takes only finitely many distinct values. For example, give value two to one measurable region, value five to a disjoint second region, and zero everywhere else. Such a function is called a *simple function*. It is measurable when all the regions on which it takes its values are measurable.

Why are simple functions useful? They are the function equivalent of measuring a region by breaking it into a finite number of pieces. Once we know the measure of each piece, the integral of a nonnegative simple function should simply be the sum of each height multiplied by the measure of the region supporting that height. No sophisticated limiting process is needed yet.

We then need a way to approximate less simple functions by simple ones, without losing measurability. For a nonnegative measurable function, divide the nonnegative output axis into small steps. Round the function's value *down* to the nearest step, and cap extremely high values at a finite ceiling. For the Nth approximation, use steps of size one over two to the N, and cap at height N. The result takes finitely many values and is therefore simple. Every region on which it takes a particular step value can be described by a pair of threshold inequalities, so those regions are measurable.

As N increases, the steps get finer and the ceiling rises. The approximations increase pointwise toward the original function, including functions that can take the value infinity. This is the constructive reason nonnegative measurable functions are manageable: we can approach them from below using finite-valued pieces whose measures are already meaningful.

Notice why rounding down is important. A sequence of approximations increasing toward a limit fits the countable monotone operations that measure handles especially well. We will exploit exactly that feature when defining the Lebesgue integral.

## What limits preserve

Suppose we have a sequence of measurable real-valued functions. Is the function obtained by taking their pointwise limit measurable, whenever that limit exists? Yes. More generally, the pointwise supremum and infimum of countably many measurable functions are measurable, even if their values may be infinite.

Here is the essential idea for a supremum. Asking whether the supremum exceeds a threshold is equivalent to asking whether at least one function in the sequence exceeds that threshold. That is a countable union of measurable sets. For an infimum, asking whether every function stays above a threshold can be reduced to a countable intersection, with a little care about strict inequalities. Once countable suprema and infima are measurable, so are limit superior and limit inferior, since those can be assembled from countable infima and suprema of tails.

If an ordinary pointwise limit exists, the limit superior and limit inferior agree. Their common value is therefore measurable. The key feature is that the limiting process uses countably many operations, not arbitrary unions of unrelated sets.

Arithmetic combinations also preserve measurability. Sums and products of finite real-valued measurable functions are measurable. One way to see this is to approximate both functions by simple functions and then pass to pointwise limits. Another is to use the fact that a continuous function of a finite vector of measurable coordinates is measurable. There is no magic shortcut that makes an undefined quotient meaningful: dividing by a function requires stating where its value is nonzero.

It is worth noticing a logical separation. Being measurable says that a function is eligible for integration. It does not say the integral is finite. The reciprocal of x on the interval from zero to one, with any measurable value assigned at zero, is measurable, but its nonnegative integral over that interval is infinite. Eligibility is not summability.

## The phrase almost everywhere

In measure theory, a statement holds *almost everywhere* when the set of points where it fails has measure zero. This is not the same as saying the statement holds at all but finitely many points, or at all but countably many points. The exceptional set might be uncountable, as the Cantor set demonstrates.

For example, the rational-indicator function equals zero almost everywhere on the unit interval, because it differs from zero only at rational inputs. But it does not equal zero at every point. The distinction is mathematically sharp: we are deliberately allowing exceptions, provided they fit inside a measurable null set.

A major convenience of the Lebesgue sigma-algebra is that it is complete. If two functions differ only on a null set, and one of them is measurable, then the other is measurable too, provided their values are defined in the usual real or extended-real target space. The exceptional modifications need not have any recognizable pattern. Every subset of a null set is measurable, so every threshold test on the modified function remains measurable.

The completeness assumption cannot be omitted silently in an arbitrary measure space. If the sigma-algebra omits subsets of a null measurable set, a modification on one of those omitted subsets could fail to be measurable. This is one reason Borel measurability and Lebesgue measurability need to be distinguished.

We will eventually define an integral that gives equal values to functions that agree almost everywhere, whenever their integrals are well defined. Later still, when we build spaces of integrable functions, we will identify two functions that differ only on a null set. Those spaces consist of equivalence classes rather than literally different pointwise graphs. The seed of that construction is already present in this simple phrase, almost everywhere.

## Almost everywhere is not uniform convergence

It is tempting to think that if a sequence of functions converges at almost every point, then sufficiently late functions must be close to the limit *simultaneously* throughout most of the domain. That intuition requires care.

Consider the functions x raised to the Nth power on the unit interval. At every x strictly below one, they converge to zero. At x equal to one, they stay equal to one. Thus the pointwise limit is zero almost everywhere. But the convergence is not uniform across the entire unit interval. No matter how large N becomes, some inputs very close to one still produce values near one.

If we throw away a thin interval near one, however, things improve. On the interval from zero to one minus a small positive number, all sufficiently late functions are uniformly small. The excluded interval can have as little length as we wish.

A theorem of Egoroff generalizes that observation. On a measurable set of *finite measure*, if a sequence of measurable real-valued functions converges almost everywhere to a finite-valued measurable limit, then for every positive tolerance in measure, we can remove a measurable exceptional subset of measure smaller than that tolerance and obtain uniform convergence on what remains.

This is nearly uniform convergence, not uniform convergence. The exceptional region depends on the requested measure tolerance, and it may contain infinitely many points. The theorem lets us exchange a small loss in domain size for a strong form of control over the sequence.

Why is the finite-measure hypothesis present? On the positive half-line, define the Nth function to be one on all inputs at least N, and zero elsewhere. At each fixed input, the function eventually becomes zero. Convergence is pointwise everywhere. Yet if we remove only a subset of finite measure, the remaining domain still contains points arbitrarily far to the right. For every N there are points where the Nth function is one. So uniform convergence cannot be recovered on the remainder. Egoroff's finite-measure assumption is essential.

## A different notion: convergence in measure

Another useful form of convergence does not demand that each fixed input eventually behave well. Instead, for every fixed positive error threshold, we ask for the measure of the set of inputs with errors larger than that threshold to tend to zero. This is convergence in measure.

On a finite-measure space, almost-everywhere convergence implies convergence in measure. We can understand this through Egoroff's theorem: outside an arbitrarily small exceptional set the errors eventually become uniformly small, and inside the exceptional set we control the measure directly.

The reverse implication does not generally hold for the whole sequence. An illuminating example is the typewriter sequence on the unit interval. First mark the left half, then the right half. Next mark the four quarter intervals one after another. Then the eight eighth-intervals, and so on. Each stage marks a progressively narrower interval; the measure of that interval tends to zero. Thus the indicators converge to zero in measure. But every point except possibly an endpoint belongs to marked intervals infinitely often and to unmarked intervals infinitely often. The pointwise values fail to converge.

The point is not to prefer one convergence over another. Each captures a distinct kind of control. Pointwise convergence is about eventual behavior at fixed inputs. Almost-everywhere convergence allows a null exceptional set. Uniform convergence demands a single index that works for every input. Convergence in measure asks that large errors occupy a shrinking amount of the domain. Keeping these quantifiers separate is indispensable when we begin exchanging limits and integrals.

## Why this framework is worth keeping

The function that defeats Riemann sums is now easy to describe: it is the indicator of a countable measurable set. The measurable-function definition has no difficulty with it. A nonnegative measurable function, no matter how complicated its graph appears, can be approximated increasingly by finite-valued step functions whose regions are measurable.

We also know what is safe under limits: countable pointwise limits preserve measurability, and modifications on null sets preserve measurability in a complete measure space. But we do *not* yet know that taking a pointwise limit of integrable functions preserves their integrals. That stronger claim is false without additional hypotheses.

The next construction begins with the finite sums attached to simple functions, takes suprema of integrals of approximations from below, and proves a theorem that makes monotone limits pass through integration. That theorem will explain why Lebesgue integration is so much more stable than the Riemann integral for sequences of measurable functions. We are not there yet, but every ingredient is now in place: measured sets, finite-valued functions built from them, and a way to pass from simple approximations to arbitrary nonnegative measurable functions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Measurability and simple approximation

For \((X,\Sigma)\) a measurable space, a function \(f:X\to\overline{\mathbb R}\) is measurable if \(\{x:f(x)>a\}\in\Sigma\) for every \(a\in\mathbb R\). This is equivalent to measurability of all Borel preimages. For nonnegative measurable \(f\), set
\[
s_n(x)=2^{-n}\left\lfloor 2^n\min(f(x),n)\right\rfloor,
\]
with \(\min(+\infty,n)=n\). Then \(s_n\) is finite-valued and measurable, \(s_n\le s_{n+1}\), and \(s_n(x)\uparrow f(x)\). (For example, \(n=1\) yields steps of size one half.)

If \(f_n\) are measurable extended-real-valued functions, then \(\sup_nf_n\), \(\inf_nf_n\), \(\limsup_nf_n\) and \(\liminf_nf_n\) are measurable. For strict threshold events on an infimum, one can write \(\{\inf_nf_n>a\}=\bigcup_{k\ge1}\bigcap_n\{f_n\ge a+1/k\}\), which avoids the false equivalence with \(\bigcap_n\{f_n>a\}\).

### Convergence concepts

For measurable real-valued \(f_n,f\) on \((X,\Sigma,\mu)\):

- \(f_n\to f\) **almost everywhere** if there exists \(N\in\Sigma\) with \(\mu(N)=0\) such that \(f_n(x)\to f(x)\) for all \(x\notin N\).
- \(f_n\to f\) **in measure** if \(\mu(\{|f_n-f|>\varepsilon\})\to0\) for each \(\varepsilon>0\).
- Egoroff's theorem on \(A\in\Sigma\) with \(\mu(A)<\infty\): almost-everywhere convergence of finite measurable functions to finite measurable \(f\) implies that for each \(\delta>0\) there exists measurable \(E\subseteq A\) with \(\mu(A\setminus E)<\delta\) and \(f_n\to f\) uniformly on \(E\).

**Egoroff proof outline:** for positive integers \(k,N\) let
\[
E_{k,N}=\bigcap_{n\ge N}\{x\in A:|f_n(x)-f(x)|\le1/k\}.
\]
For each fixed \(k\), these increase in \(N\) to a conull subset of \(A\). By continuity from below and \(\mu(A)<\infty\), select \(N_k\) with \(\mu(A\setminus E_{k,N_k})<\delta 2^{-k}\). Set \(E=\bigcap_kE_{k,N_k}\). Then \(\mu(A\setminus E)<\delta\), and for each \(k\), all \(n\ge N_k\) satisfy \(\sup_{x\in E}|f_n(x)-f(x)|\le1/k\).

### Exercises with answers

1. **Rationals.** Why is \(1_{\mathbb Q\cap[0,1]}\) measurable but nowhere continuous on \([0,1]\)? **Answer:** The rational set is countable and measurable; both it and its complement are dense, forcing discontinuity everywhere.
2. **Null modifications.** Why do arbitrary modifications on Lebesgue null sets preserve measurability? **Answer:** Lebesgue measure is complete: every subset of every null measurable set belongs to the sigma-algebra.
3. **Uniform control.** On \([0,1-\eta]\), bound \(x^n\). **Answer:** \(\sup x^n\le(1-\eta)^n\to0\) for each fixed \(\eta>0\).
4. **Typewriter sequence.** During stage \(m\), enumerate the half-open dyadic intervals of length \(2^{-m}\). Why do their indicators converge in measure but not pointwise on \([0,1)\)? **Answer:** Their supports have length \(2^{-m}\to0\). Every point belongs to exactly one interval per stage and lies outside the other intervals at that stage; so there are infinitely many ones and zeroes.

### Sources

- Sheldon Axler, *Measure, Integration & Real Analysis*, chapters on measurable functions and convergence.
- MIT OpenCourseWare, *18.125 Measure and Integration*, lectures 1–2 and 11–13 (measurability, simple functions, almost-everywhere convergence, Egoroff's theorem).
