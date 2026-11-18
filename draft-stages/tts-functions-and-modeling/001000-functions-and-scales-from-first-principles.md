# Functions and Scales: Inputs, Models, and Dimensional Reasoning

**Track:** Functions, Scales, and Mathematical Modeling  
**Lecture:** 001000  
**Preparation:** Arithmetic, variables, and solving simple equations.  
**Companion:** Functions, units, inverses, composition, power laws, and dimensional reasoning.

<!-- BEGIN SPOKEN LECTURE -->

A city rents bicycles. There is a fixed fee of five dollars and a further charge of two dollars for every hour you keep the bicycle. Someone writes down the formula, five plus two times h, and calls it the price. It is a useful formula, but it leaves questions unanswered. Are partial hours allowed? Does a rental of negative three hours make sense? Are the first two hours included in the fixed fee? Is there a maximum rental period? What counts as one rental?

To turn the formula into a mathematical model, we must say what information goes in, what comes out, and what the rules mean. That is the business of functions.

A function assigns exactly one output to each permitted input. It need not be given by an algebraic expression: a table, a program, a geometric construction, or a physical measurement rule may define a function. What matters is that after we have fixed the input, there is no ambiguity about which output the rule assigns. The output may be a number, a vector, a word, or even another function.

Let's begin with the bicycle fee. If h is measured in hours and we allow any nonnegative real duration, the cost function is five dollars plus two dollars per hour times h hours. The multiplication gives dollars, so the sum has consistent units. We can call the function C and write C of h. Notice how a unit check protects the meaning. Five dollars plus two hours would not be a sensible price formula. Five dollars plus two dollars per hour times h hours is.

The **domain** of a function is the collection of inputs it permits. In this model the domain might be all nonnegative real numbers. For a rental shop that rounds up to whole hours, the domain can still be nonnegative real durations, but the function itself changes: it uses the ceiling of h, the smallest integer at least as large as h. For a subscription plan billed only in whole-hour packages, we might instead decide that the inputs are whole numbers. The same symbols can represent different mathematical objects when their domains differ.

The **codomain** is a declared set in which outputs live. For C we might declare nonnegative dollar amounts. The **range** is the outputs actually attained. If C of h equals five plus two h for nonnegative h, its range is all real prices at least five dollars, within the idealization that any duration is allowed. The range is not automatically the codomain. A function can map integers into the real numbers while attaining only a few real values.

A graph makes these distinctions visible. Put duration horizontally and cost vertically. The rule five plus two h is a straight line starting at a height of five on the vertical axis and climbing two units of money for each hour. But do not draw the portion to the left of zero if negative durations are excluded. A graph is not the decoration of a formula; it is a picture of the formula **together with its domain**.

There is also a distinction between an equation and a function. The equation y squared equals x can describe two possible y values for a positive x, one positive and one negative. As written it does not specify one y for each x. We can create a function by choosing the nonnegative root and using nonnegative x as its domain. Or we can use x as the output and y as the input. Saying which direction we are mapping matters.

Functions let us combine processes. Suppose a bicycle dock is a fifteen-minute walk from home. The time from leaving home to returning might be the rental duration plus half an hour of walking. Call that rule T: T of h is h plus one half. Suppose a second rule converts total hours into minutes, M of t equals sixty t. Applying T and then M gives M of T of h, or sixty times the quantity h plus one half. This operation is called **composition**. We have connected two rules whose units match: hours emerge from the first and enter the second.

Order matters. First charging for a ride and then adding a dollar surcharge is different from adding an hour to the rental duration and then calculating the charge. Compare C of h plus one and C of the quantity h plus one. The first means the bill for h hours, then an extra dollar. The second means the bill for an extra hour and therefore an extra two dollars. Parentheses are a record of what happened when.

A useful way to test composition is to ask whether the output type of the inner function is an allowed input of the outer function. If one rule returns dollars and another expects meters, the symbols can be written but the proposed process has no physical meaning. The algebra alone will not catch that.

Now suppose we are given a bill of thirteen dollars and want to infer the rental duration. Subtract the five-dollar fixed fee: eight dollars remain. Divide by two dollars per hour: the rental was four hours. We have reversed the rule. In mathematical language the function C, on the stated domain, has an **inverse**, and its inverse sends a cost to the corresponding duration. The inverse has the range of C as its domain: a bill of three dollars cannot come from this model, and asking the inverse what duration produced it is outside the defined problem.

Not every function has an inverse. Consider the function that assigns a person's age in whole years to their exact height. If this is modeled as a unique height at each age, several ages may give the same height. From the height alone, we cannot necessarily recover the age. Or take the simpler rule that squares a number: both three and negative three give nine. To invert squaring, we need more information, such as a restriction to nonnegative inputs. A function has a genuine inverse precisely when it pairs every input with a distinct output, and when we use its actual range as the inverse's domain.

There are other ways that one formula can hide multiple rules. A taxi fare might be five dollars for the first mile, then a dollar for each additional mile. The cost depends on which interval the distance occupies. A **piecewise function** specifies one rule for the first interval and a second for the remaining distances. At the boundary we need to decide which rule applies and whether both produce the same value. A threshold creates a jump if the price changes suddenly; not all models are continuous.

A relationship can also be represented without an explicit formula. Suppose we record the temperature once per hour. The table maps observation times to temperatures. Between observations the table alone tells us nothing. Drawing straight lines between the dots adds an interpolation rule. Drawing a smooth physical curve adds another assumption. Neither was contained in the original measurements.

One final distinction is useful. A function is a rule; a model is a claim that the rule appropriately describes something. The rental-price function may be exact because the shop chose the tariff. A formula for body temperature or plant growth is not exact merely because it is written mathematically. Its value is in making assumptions explicit and predictions checkable.

The central skill is therefore not to memorize a notation. For each new function, ask four questions. What may enter? What comes out, and in what units? What changes if the input changes? And if I combine this rule with another, what process does that combination describe? With these questions in place, formulas, graphs, inverse functions, and eventually calculus all have something precise to work on.

# What multiplying the input really changes

We have learned how to specify a function. A particularly useful next question is how the output reacts when we multiply an input instead of adding to it.

A builder makes a box twice as wide, twice as high, and twice as deep as the original. The new box looks like the same box, only larger. Yet its volume is not twice the old volume. It is eight times the old volume. Its surface area is four times as large. Its longest straight-line dimension is twice as large. One change of scale has produced three different numerical effects.

This simple observation explains why so many mathematical models begin with powers. Length scales like the first power of size. Area scales like the second. Volume scales like the third. If all linear dimensions are multiplied by a positive factor s, the dimensions of an ideal similar object transform by s, s squared, and s cubed. Those powers are not mysterious coefficients obtained from data. They come from the geometry of multiplying dimensions.

Suppose a cube has side length three centimeters. Its area is not three times three centimeters; that product has units of square centimeters. The cube's volume is three times three times three cubic centimeters, or twenty-seven cubic centimeters. Changing its side to six centimeters multiplies volume by eight. Units help reveal why: cubic centimeters are built from three independent lengths.

A **power law** has the form y equals a constant times x raised to some exponent. The exponent tells us how outputs respond to a multiplicative change of inputs. If y is proportional to x squared, doubling x multiplies y by four. If y is proportional to the inverse square of x, doubling x divides y by four. If the exponent is one half, multiplying x by four multiplies y by two. The exponent may be negative or fractional; it does not have to be a whole number.

This is different from a linear relationship, which tells us the effect of **adding** a fixed amount to the input. In the linear function five plus two x, increasing x by one always increases the output by two. In a pure power law, multiplying x by a constant produces a fixed multiplicative effect instead. Confusing additive and multiplicative changes is one of the easiest ways to misread data.

Think of a square garden. If you double its side, you quadruple the area. To double the area, you multiply the side by the square root of two, approximately one point four one. Someone who mistakes the first kind of doubling for the second will order the wrong amount of material.

Scaling laws also reveal tradeoffs. Imagine a long, narrow storage container whose volume we want to keep fixed. Make its height twice as great and its base area must become half as great. Here we have an inverse relationship, not because height is intrinsically bad but because we imposed a fixed total volume. A formula is always attached to what is being held constant.

What about a polynomial such as three plus two x plus x squared? It is not a single power law. At small x, several terms may matter. For sufficiently large positive x, the squared term dominates the constant and linear terms in relative size. We say the leading power describes the polynomial's **asymptotic scale**. This is a useful approximation, but it is not a claim that the discarded terms vanish or that x is large enough in a particular application. You must check the error at the values of interest.

Dimensional analysis gives us another way to examine formulas. Suppose a falling object's height is predicted to change by a quantity proportional to gravitational acceleration times elapsed time squared. Acceleration is distance per time squared. Multiply by time squared and you obtain distance. The units fit. By contrast, acceleration times time has units of speed, not distance. It cannot by itself be added to a height. A dimensionally correct expression is not guaranteed to be physically true, but a dimensionally incorrect expression cannot be a correct equation between physical quantities.

A related rule concerns exponentials and logarithms. We cannot meaningfully apply the ordinary exponential function to a bare physical quantity with units. An expression like the exponential of three meters has no invariant meaning when a meter is replaced by a centimeter. What can appear inside an exponential is a **dimensionless ratio**. A decay model uses the product of a rate, measured in inverse seconds, and a duration, measured in seconds. The units cancel. This will matter when we study exponential growth and decay.

The same discipline helps with graphing. A plot with distance in meters on the horizontal axis and seconds on the vertical axis has a slope measured in seconds per meter. Exchange the axes and the slope's units become meters per second. Numerical slope is not a free-floating property of a picture. It is attached to what was chosen as input and output.

Power laws are particularly clear on logarithmic axes. If y equals a times x to the k, with x and y positive, take logarithms: the log of y equals the log of a plus k times the log of x. In coordinates where both axes display logarithms, the graph is a straight line of slope k. This can help identify a scaling exponent. But it also creates a temptation. A short curved region can resemble a straight line. Measurement noise, thresholds, and changing physical regimes can produce misleading slopes.

Here is a modeling example. You measure the time required for a pendulum to swing once as you change its length. A model for small oscillations predicts that period is proportional to the square root of length when gravity is held fixed. If you make the pendulum four times as long, the period should be twice as long. That conclusion follows from the model's one-half exponent. It is not true for every conceivable pendulum motion: large-amplitude swings require correction, and changing the gravitational environment also changes the proportionality factor.

There is a deeper reason to respect those qualifications. A model can have several characteristic scales. A boat's behavior may change when it is small enough for viscosity to dominate, or large enough for wave generation to dominate. A material may be elastic for small deformations and fail under large ones. A power law that is accurate in one regime is not a law of nature for all input sizes.

Consider two competing models for a population. One says population doubles when land area doubles; another says population grows like the square root of available area because of a limiting resource. Both can fit a narrow range of observations if we adjust their constants. To choose between them, we need data across a wider range, a mechanism that motivates the relationship, or experiments that separate their predictions. It is not enough to prefer whichever curve looks smoother.

Scaling turns equations into questions we can ask before calculating. What happens when an input doubles? Which quantities are conserved? Which ratios have no units? Which terms dominate at large or small scales? And what would make this relationship stop working? These questions connect school algebra to geometry, mechanics, differential equations, asymptotic analysis, and practical model criticism.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Part I

A function is a map \(f:A\to B\), where \(A\) is its domain and \(B\) its codomain; its image is \(f(A)=\{f(a):a\in A\}\subseteq B\). The *graph* is \(\{(a,f(a)):a\in A\}\subseteq A\times B\). A function can have identical images for distinct inputs but cannot assign two images to the same input.

For the bicycle tariff, write \(C:[0,\infty)\to\mathbb{R}\), \(C(h)=5+2h\). Its image is \([5,\infty)\). The inverse \(C^{-1}:[5,\infty)\to[0,\infty)\) is \(C^{-1}(c)=(c-5)/2\). As always with inverse functions, \(C^{-1}\circ C=\mathrm{id}_{[0,\infty)}\) and \(C\circ C^{-1}=\mathrm{id}_{[5,\infty)}\).

If \(f:A\to B\) and \(g:B\to C\), then \(g\circ f:A\to C\) is defined by \((g\circ f)(a)=g(f(a))\). Composition need not commute: \(f\circ g\neq g\circ f\), even when both exist.

A tariff rounded up to whole hours can be written \(C(h)=5+2\lceil h\rceil\) for \(h\geq0\); note that \(C(0)=5\), so one might choose a different rule for a rental of zero duration. This illustrates the need to state boundary conventions explicitly.

### Exercises and solutions

1. **Domain and image.** Let \(f(x)=1/(x-2)\) with real inputs. Find its maximal real domain and image. **Solution:** domain \(\mathbb{R}\setminus\{2\}\), image \(\mathbb{R}\setminus\{0\}\).
2. **Composition.** Let \(f(x)=3x+1\) and \(g(x)=x^2\). Compute \(g(f(2))\) and \(f(g(2))\). **Solution:** \(g(7)=49\) versus \(f(4)=13\).
3. **Inverting a restriction.** Why does \(f(x)=x^2\) have an inverse on \([0,\infty)\) but not on \(\mathbb R\)? **Solution:** squaring is strictly increasing on the restricted domain, while \(f(-x)=f(x)\) on the whole real line.
4. **Units.** A travel formula uses \(d(t)=8+3t\) where \(t\) is hours and \(d\) is kilometers. What units must the coefficients have? **Solution:** eight kilometers and three kilometers per hour.

### Reading and attribution

- OpenStax, *Precalculus 2e*, Chapters 1–2, functions, domains, graphs, composition and inverses: https://openstax.org/books/precalculus-2e/pages/preface.
- The bicycle tariff and its unit/domain variants are original didactic examples.

### Part II: What multiplying the input really changes

For \(y=A x^k\) with \(x>0\), \(y(sx)/y(x)=s^k\) when \(A\ne0\). The logarithmic derivative satisfies \(d\log y/d\log x=k\) when \(A>0\). Thus the slope of a log-log plot measures a local scaling exponent in a general differentiable positive model.

**Dimensional consistency.** With base dimensions length \(L\) and time \(T\), acceleration has dimension \(LT^{-2}\). Hence \(at^2\) has dimension \(L\), while \(at\) has dimension \(LT^{-1}\). A dimensionless quantity such as \(t/\tau\), where \(\tau\) is a characteristic time, can appear as the argument of an exponential.

**Pendulum example.** For a point mass on a massless string under the small-angle approximation, \(T\approx 2\pi\sqrt{\ell/g}\), with \([\ell]=L\), \([g]=LT^{-2}\), and \([T]=T\). The approximation fails progressively as angular amplitude increases, because the small-angle approximation \(\sin\theta\approx\theta\) becomes inaccurate.

**Polynomial asymptotics.** For \(p(x)=x^2+2x+3\), \(p(x)/x^2=1+2/x+3/x^2\to1\) as \(x\to+\infty\). At \(x=2\), however, the ratio is \(11/4\): the asymptotic formula is not a good numerical approximation there.

### Exercises and solutions

1. **Similarity.** If a geometrically similar container's side lengths triple, what happens to area and volume? **Solution:** area multiplies by nine and volume by twenty-seven.
2. **Inverse scaling.** An object travels a fixed distance at speed \(v\), so \(t=d/v\). What happens to time if speed doubles? **Solution:** time halves, assuming \(d\) stays fixed.
3. **Units.** Is \(e^{-0.2t}\) meaningful when \(t\) is measured in seconds? **Solution:** only if \(0.2\) carries inverse-second units. The argument of \(e\) must be dimensionless.
4. **Asymptotic fit.** For \(f(x)=x^3+100x\), which term dominates when \(x\) is very large and why might \(x=5\) not qualify? **Solution:** \(x^3\) dominates asymptotically, but at \(x=5\) the linear term is 500 and the cubic term only 125.

### Reading and attribution

- OpenStax, *Precalculus 2e*, Chapters 2–4, power, polynomial, and rational functions: https://openstax.org/books/precalculus-2e/pages/preface.
- Richard Feynman, Robert Leighton, and Matthew Sands, *The Feynman Lectures on Physics*, Volume I, units and dimensional considerations: https://www.feynmanlectures.caltech.edu/I_05.html.
- The geometric and model-comparison examples are original worked exposition.
