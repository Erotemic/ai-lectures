# Sobolev Embeddings and Compactness: How Slopes Control Shapes

**Track:** Multivariable Calculus from First Principles. **Focus:** one-dimensional Sobolev estimates, compact embeddings, the effect of dimension, and loss of compactness at critical scales.

<!-- BEGIN SPOKEN LECTURE -->

# Sobolev Embeddings and Compactness: How Slopes Control Shapes

A bound on a function's squared slope is different from a bound on the function's values. Yet it can control those values, provided we know where the function lives and what happens at the boundary. That observation leads to one of the most productive ideas in the analysis of differential equations: if derivatives are controlled, the functions themselves may become compact in a stronger topology.

Here compactness means something specific. Given an infinite sequence of admissible functions with a shared norm bound, can we choose a subsequence that converges in a norm suited to the nonlinear term we want to analyze? Weak convergence is enough for many quadratic derivative energies, but not automatically enough for squares, cubes, or nonlinear material responses. The Sobolev embedding and Rellich compactness theorems explain when we can obtain that stronger convergence.

We will begin on an interval where the argument can almost be done by hand. Then we will ask what changes when the string becomes a membrane or a three-dimensional field. Finally we will deliberately construct a sequence that defeats compactness at a critical scale. The failure will tell us as much about the theorem as its success.

## A bound on slopes gives a bound on differences

Take a function u on the unit interval, with square-integrable weak derivative. In one dimension, such a function has an absolutely continuous representative. This is not an assumption of smoothness. It is a consequence of membership in H one: the difference between the values at two points is the integral of the weak derivative between those points.

Write u at y minus u at x as the integral of u prime from x to y. The Cauchy–Schwarz inequality gives an immediate estimate. The absolute value of that difference is at most the L two norm of the derivative, multiplied by the square root of the distance between x and y.

Suppose all our candidates have derivative norm at most M. Then all of them obey the same rule: at points a distance one hundredth apart, their heights can differ by at most M divided by ten. At points a distance one ten-thousandth apart, the allowed difference is at most M divided by one hundred. No member of the family can make an arbitrarily large jump over a sufficiently short interval.

This is called a uniform Hölder estimate, with exponent one half. It does not assert the function has an ordinary derivative at every point, and it does not say the derivative is itself continuous. It says the function has a controlled modulus of continuity. The conclusion is stronger than simply being integrable.

If we also impose u of zero equals zero, the same estimate gives a bound on height: the absolute value of u at x is at most M times the square root of x, and hence at most M throughout the unit interval. In the zero-boundary Sobolev space, one derivative norm therefore controls both the height of the curve and how rapidly its height can change.

Without any boundary condition, the derivative norm by itself cannot control height, because a huge constant function has derivative zero. We then need an L two bound on the function, a bound on its average, or an anchor at one point. The full H one norm provides that missing information. This distinction is precisely why Poincaré inequalities and boundary conditions are so important in the variational method.

## Turn a family of shapes into a convergent subsequence

Now imagine a sequence of functions all obeying a uniform height bound and the same Hölder estimate. Draw their values at the rational points of the interval. For the first rational point, the sequence of heights is bounded, so we can choose a subsequence on which those heights converge. Within that subsequence choose one on which the heights at the second rational converge, and continue. A diagonal selection gives convergence at every rational in our list.

Convergence at a dense set is not quite the end of the argument. The shared Hölder estimate fills in the gaps. If we know two functions are close at the nearby rational grid points, neither can wander too far between those points. By choosing a fine grid and then a sufficiently late part of the subsequence, we can make the two functions uniformly close at every real point of the interval.

This is the mechanism behind the Arzelà–Ascoli theorem. A uniformly bounded and equicontinuous family of continuous functions on a compact interval is relatively compact in the uniform norm. Every sequence in that family has a uniformly convergent subsequence.

For our Sobolev functions, the conditions are supplied by the H one bound. In one dimension, bounded sequences in H one have subsequences that converge uniformly, after choosing their continuous representatives. In particular, such subsequences converge in L two, in L four, and in any other finite L p norm on the interval.

Pause at the exact conclusion. We have extracted strong convergence of the functions, not necessarily strong convergence of their derivatives. The oscillating sequence with vanishing amplitude is still a useful counterexample: its heights converge uniformly to zero while its derivatives retain an L two norm of one divided by the square root of two. Compactness can improve one component without improving every component.

This is good news for nonlinear variational problems. If an energy contains the integral of the fourth power of the function, uniform convergence of a bounded sequence ensures that term converges along the subsequence. Meanwhile weak convergence of the derivatives gives lower semicontinuity of the squared-slope penalty. The two topologies work together.

## The language of continuous and compact embeddings

An embedding is a way to regard an element of one function space as an element of another. Saying H one embeds continuously into another normed space means there is a constant C so that the new norm is bounded by C times the H one norm. The embedding turns a bounded set in the first space into a bounded set in the second.

Compact embedding says more. Every bounded sequence in the first space has a subsequence that converges strongly in the second. In the one-dimensional case, H one embeds compactly into continuous functions on the closed interval when those functions are given the uniform norm. That is a consequence of the common Hölder and height estimates we just derived.

Continuous embedding and compact embedding answer different questions. A bound gives stability. Compactness gives subsequential convergence. Many nonlinear problems need the latter because their nonlinear terms behave well under strong convergence but may not behave well under weak convergence.

The word compact does not mean that the entire bounded sequence converges or that we can take the limit without selecting a subsequence. We might alternate between two different shapes forever. The sequence itself would fail to converge, but it would have a constant subsequence of either shape. Compactness is about the possibility of extracting a convergent subsequence from any bounded sequence.

## What changes in two and three dimensions

A string is one-dimensional. A membrane, temperature field, or displacement field lives in two or three dimensions. The preceding calculation depended on integrating a derivative along a line and applying a one-dimensional Cauchy–Schwarz inequality. For a general H one function in higher dimensions, point values may not even be well-defined in the same stable way.

The relevant bounds are expressed through Sobolev embeddings. On a bounded domain with a sufficiently regular, for example Lipschitz, boundary, H one functions in three dimensions are controlled in L six by their H one norm. They are also controlled in every L q with q between one and six on a bounded domain. In two dimensions the H one norm controls every finite L q norm, although it does not in general provide an L infinity bound. In one dimension the stronger continuous-representative estimate is available.

Those powers are not arbitrary. The critical exponent in dimensions greater than two is two times the dimension divided by the dimension minus two. For dimension three it is six; for dimension four it is four. As dimension increases, the range of powers that first derivatives control becomes narrower.

Now consider convergence instead of mere bounds. On a bounded Lipschitz domain, Rellich–Kondrachov compactness tells us that bounded H one sequences have strongly convergent subsequences in L two. In three dimensions we can in fact extract strong convergence in L q for q less than six, but the same statement does not generally extend to the critical exponent six. In two dimensions we have compactness into every finite L q. These are statements about a fixed bounded domain with a regular boundary, not about arbitrary open sets of infinite extent.

For nonlinear PDE analysis this determines whether, for example, a cubic response can be passed to the limit as a lower-order term. In three dimensions strong L four convergence is available because four is below the critical exponent six. In four dimensions the corresponding power four sits at the critical threshold. The argument must then use additional structure instead of assuming compactness gives the same result.

## A concentrated bump defeats critical compactness

Why does the critical exponent appear? Construct a smooth bump centered at one point in three-dimensional space. Now shrink its width by a factor epsilon while increasing its height by epsilon to the power negative one half. Make sure the bump remains inside the domain.

A derivative introduces one inverse factor of epsilon, while three-dimensional volume contributes a factor of epsilon cubed. When we square the derivative and integrate, these powers cancel. The squared gradient norm stays constant as epsilon shrinks. The bump becomes narrower and taller, but its derivative energy does not increase.

What happens to its size in L two? The squared height contributes one inverse factor of epsilon and the volume contributes epsilon cubed, leaving epsilon squared. Its L two norm goes to zero. In other words, the bump converges strongly to zero in L two.

Now raise its height to the sixth power instead. The sixth power contributes epsilon to the negative third power, exactly canceled by the shrinking volume. Its L six norm stays fixed. It cannot converge strongly to zero in L six, even though it converges strongly to zero in L two and has bounded H one energy.

This is a model of concentration. In three dimensions, bounded H one controls L six but does not make the embedding into L six compact. At the critical exponent, a function can concentrate its mass on a shrinking region without violating the derivative-energy budget. The same calculation generalizes to dimensions greater than two with the corresponding critical exponent.

The example explains why the Rellich theorem draws a line between powers strictly below the critical exponent and the critical power itself. It also foreshadows difficult nonlinear PDE questions about concentration, loss of compactness, and the possibility that a minimizing sequence becomes more localized instead of approaching an ordinary minimizer in the norm one might have preferred.

## Another way compactness can fail: escape to infinity

Even far below a critical exponent, an unbounded spatial domain creates a different obstruction. Choose one smooth bump of fixed height and shape, then translate it one unit farther to the right at each step. On the whole real line, every translated bump has exactly the same H one norm and L two norm. Yet the bumps march away from every fixed observation region.

If the translations become sufficiently separated, the sequence cannot have a strongly L two convergent subsequence. The L two distance between distinct, disjoint bumps remains fixed. The failure has nothing to do with tiny scales or growing heights. The mass simply escapes toward infinity.

That is why the hypotheses of a compact embedding theorem matter. The boundedness of the spatial domain prevents this particular escape, and a regular boundary supports the extension and localization arguments needed in standard proofs. One should not erase those hypotheses when applying the theorem to an equation on an infinite domain.

## How compactness serves the direct method

We can finally connect the estimates to minimization. Suppose an energy on the unit interval consists of a squared-slope term, a fourth-power term in the height, and a linear load. A minimizing sequence will often have its derivative norm bounded because the positive quadratic term dominates the load.

Weak compactness gives a subsequence converging weakly in H naught one. That is enough to handle the derivative energy through lower semicontinuity. One-dimensional Sobolev compactness then gives, along a further subsequence, uniform convergence of the heights. That stronger convergence lets us pass to the limit in the fourth-power term and in the load.

At this point the limit does not have to retain the approximate derivative energy exactly. It only needs to avoid an upward energy jump. If the candidates approach the infimum, the weak limit's energy cannot be any larger than that infimum, and therefore it must attain it. The direct method works because we choose convergence appropriate to each mathematical term.

In a higher-dimensional problem, the same proof may work with strong L four convergence, provided the dimension and embedding hypotheses supply it. At a critical exponent, the concentration example warns that the same compactness step may fail. We would then need convexity, a different lower semicontinuity theorem, a concentration-compactness argument, or a different formulation.

The critical habit is to separate three assertions: a norm bound, a convergent subsequence, and convergence of the expressions in the energy. None is an automatic synonym for the others. Sobolev estimates tell us what a derivative bound controls. Compactness tells us which limits we can extract. Only after that do we have the right to pass a nonlinear expression to the limit.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### One-dimensional estimate and Arzelà–Ascoli

For \(u\in H^1(0,1)\), use its absolutely continuous representative. For \(x,y\in[0,1]\),

\[
|u(x)-u(y)|=\left|\int_y^x u'(t)\,dt\right|
\le \|u'\|_{L^2}|x-y|^{1/2}.
\]

For \(u\in H_0^1(0,1)\), \(|u(x)|\le\|u'\|_2\). A uniformly \(H_0^1\)-bounded sequence is therefore uniformly bounded and equicontinuous, so Arzelà–Ascoli yields a uniformly convergent subsequence. A sequence bounded in the full \(H^1(0,1)\) norm has the same conclusion: for at least one point \(x_0\), \(|u(x_0)|\le\|u\|_2\), and the difference bound controls all other points. Compactness in \(C([0,1])\) does **not** imply strong convergence in \(H^1\).

### Dimension and the critical exponent

On a bounded Lipschitz domain \(\Omega\subset\mathbb R^d\), with \(d>2\), there is a continuous embedding

\[
H^1(\Omega)\hookrightarrow L^{2^*}(\Omega),\qquad
2^*=\frac{2d}{d-2},
\]

and a compact embedding \(H^1(\Omega)\Subset L^q(\Omega)\) for \(1\le q<2^*\). For \(d=2\), the embedding is compact into every finite \(L^q\); for \(d=1\), it is compact into \(C^0(\overline\Omega)\) for bounded intervals. For unbounded domains these compactness conclusions can fail without other constraints.

For \(d=3\), let \(\phi\in C_c^\infty(B_1(0))\) be nonzero and choose \(x_0\) in the interior of a domain. Define

\[
u_\varepsilon(x)=\varepsilon^{-1/2}\phi((x-x_0)/\varepsilon).
\]

For sufficiently small \(\varepsilon\), its support stays inside the domain, and change of variables gives

\[
\|\nabla u_\varepsilon\|_2^2=\|\nabla\phi\|_2^2,
\quad \|u_\varepsilon\|_2^2=\varepsilon^2\|\phi\|_2^2,
\quad \|u_\varepsilon\|_6^6=\|\phi\|_6^6.
\]

The bump converges in \(L^2\), but not in \(L^6\); the \(H^1\to L^6\) embedding is not compact. The critical Sobolev exponent is tied to this scale invariance.

### Escaping translations

For a nonzero \(\phi\in C_c^\infty(0,1)\) on \(\mathbb R\), define \(v_n(x)=\phi(x-2n)\). The \(H^1(\mathbb R)\) and \(L^2(\mathbb R)\) norms are constant, but the supports are disjoint and

\[
\|v_n-v_m\|_2^2=2\|\phi\|_2^2\qquad(n\neq m).
\]

Thus there is no strongly \(L^2\)-convergent subsequence. A derivative bound without a bounded domain or confinement condition does not grant Rellich compactness.

### Exercises with answers

1. **Hölder control:** If \(\|u'\|_2\le3\) and \(|x-y|\le1/100\), how far apart can the heights be? **Answer:** At most \(3/10\).
2. **Concentration:** In \(\mathbb R^3\), why does the bump \(u_\varepsilon\) keep its gradient norm? **Answer:** Squaring the derivative contributes \(\varepsilon^{-3}\) while the volume change contributes \(\varepsilon^{3}\).
3. **Critical power:** Is boundedness in \(H^1\) on a smooth bounded three-dimensional domain enough to extract a strongly \(L^6\)-convergent subsequence? **Answer:** No; the concentrated-bump example defeats compactness at \(q=6\), though \(q<6\) works.
4. **Two kinds of convergence:** If \(u_n\) is bounded in \(H_0^1(0,1)\), can a subsequence converge uniformly while its derivative norms do not converge to the limit's derivative norm? **Answer:** Yes; \(u_n=\sin(2\pi n x)/(2\pi n)\) is an explicit example.

### Sources and further reading

- [*Notes for Sobolev Spaces Seminar*, University of Alabama at Birmingham](https://people.cas.uab.edu/~mswyatt/Sobolev_Notes_June_6.pdf), for compact embeddings and their functional-analytic context.
- [*Part III: Analysis of Partial Differential Equations*, lecture notes, §3.7](https://giacomoageno.github.io/LectureNotesAPDE.pdf), for a precise Rellich–Kondrachov statement and its hypotheses.
- Thomas Schmidt, [*Calculus of Variations*, Hamburg lecture notes](https://www.math.uni-hamburg.de/home/schmidt/lectures/CalcVar.pdf), for how compactness enters direct-method proofs.
- [Wikipedia: Sobolev inequality](https://en.wikipedia.org/wiki/Sobolev_inequality) and [Rellich–Kondrachov theorem](https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem), for dimension-dependent embedding statements.

*Teaching connections:* `multivariable-calculus:035000` explains weak energy limits; `037000` uses compact embedding to control a nonlinear fourth-power term, and `differential-equations:028000` meets concentration phenomena in dispersive PDEs.
