# Exponential Growth, Logarithms, and the Meaning of a Rate

**Track:** Functions, Scales, and Mathematical Modeling  
**Lecture:** 002000  
**Preparation:** Functions, powers, fractions, and ratios.  
**Companion:** Discrete and continuous growth, half-lives, log fits, and saturation.

<!-- BEGIN SPOKEN LECTURE -->

Imagine two jars of microorganisms. In the first jar, twenty new organisms appear every hour, no matter how many were there before. In the second, the population increases by ten percent of its current size each hour. At first the jars may look similar. As time passes, the difference becomes decisive. One gains a fixed amount per hour; the other gains a fixed **fraction** per hour.

The first is modeled by a linear function. The second is modeled by an exponential function. That is a difference between addition and multiplication, not between slow growth and fast growth. Exponential decay can be fast or slow too, and a growth rate of one tenth of one percent is exponential even if it takes a long time to notice.

Suppose the population begins at one hundred. If twenty organisms arrive each hour, after three hours there are one hundred sixty. If the population grows by ten percent per hour, the count after the first hour is one hundred ten. After the second it is one hundred twenty-one. After the third it is one hundred thirty-three point one in the idealized continuous-valued model. The mathematical population may be fractional because we are modeling an expected or large-scale quantity; an actual count remains an integer.

For fractional growth, the repeated calculation is simple. Every hour multiplies the current value by one point one. After n hours, multiply the starting value by one point one raised to the n-th power. This is a geometric progression. If the factor were one point zero one, we would have one percent growth per interval. If it were point nine, we would have ten percent decay per interval. The formula depends on what counts as an interval. Ten percent per hour is not the same rule as ten percent per day.

Two questions arise naturally. Given a number of intervals, what will the value be? And given a target value, **how long will it take**? Exponentiation answers the first; logarithms answer the second.

Say a population doubles by a fixed factor each day. Starting at one hundred, after seven days it is one hundred times two to the seventh power: twelve thousand eight hundred. Now reverse the question: starting at one hundred, how many doublings are needed to exceed ten thousand? We seek n such that two to the n is greater than one hundred. Since two to the sixth is sixty-four and two to the seventh is one hundred twenty-eight, seven doublings suffice. A logarithm tells us where the threshold lies between those integer counts.

The logarithm base b of a positive number x is the exponent to which b must be raised to produce x. We require the base b to be positive and not equal to one. A logarithm does not mean dividing, nor does it tell us a number's magnitude by some mysterious rule. It is the inverse of a familiar operation: repeated multiplication generalized to real exponents. Because powers turn sums of exponents into products of outputs, logarithms turn products into sums. The logarithm of a product is the sum of the logarithms, when the quantities are positive and the base is fixed.

This addition property makes logarithms powerful for models. A ratio of ten thousand to one hundred is one hundred. We need the base-two logarithm of that ratio, about six point six four doublings. If only whole-day multiplications happen, the threshold occurs on day seven. We can distinguish the ideal mathematical threshold from the actual update schedule.

There is another subtlety: what if a rate is quoted as an annual percentage but interest is added monthly, daily, or continuously? If the stated nominal annual rate is r and the account credits interest n times per year, the multiplier after one year is the quantity one plus r divided by n, raised to the n-th power. Change n and the annual result changes. For r equal to one, the multipliers begin at two for annual crediting, two point two five for twice-yearly crediting, and approach a special number, about two point seven one eight, as the number of crediting periods grows without bound.

That limiting number is called e. The exponential function based on e is important because its instantaneous rate of change is proportional to its current value with the simplest possible constant. In a continuous-time model, if a quantity grows at a proportional rate k per unit time, we describe it as its initial value times e raised to k times time. If k is negative, the same formula gives decay.

Take a substance that has a half-life of five hours. Half-life means that after each five-hour interval, half of whatever remains is gone. After ten hours a quarter remains; after fifteen, one eighth remains. In continuous-time notation the decay constant is the natural logarithm of two, divided by five hours, with a negative sign in the exponent. This explains why a half-life is not the time required to remove a fixed mass. Each interval removes half of the remaining mass. Even after ten half-lives a small positive quantity remains in the ideal model.

The half-life is also independent of the starting amount, provided the proportional-decay model applies. A sample beginning with one gram and a sample beginning with one kilogram have the same half-life but very different absolute losses during the first interval. Saying 'the sample loses a tenth every hour' is a claim about its fractional rate, not its absolute rate.

Now look at the units. In the expression e to the power of k t, k has units of inverse time and t has units of time. Their product is dimensionless. If you measure time in minutes rather than hours, the numerical value of k must be converted too. A formula with the correct numerical shape but the wrong time units may give a wildly wrong prediction.

How would we test an exponential model? Take logarithms of the observed positive quantities. If the model says the quantity equals a fixed initial scale times e to the k t, the natural logarithm becomes a straight line in t, with slope k. This is called a **log-linear** relationship. It is useful for identifying rates, but there is a trap: logarithms change the error pattern. Fitting an ordinary straight line to logged data gives relatively more attention to proportional errors and is not generally the same as fitting the original measurements by least squares. Zero and negative observations cannot be logged without changing the statistical model.

There is also a practical limit to unlimited exponential growth. A culture needs nutrients and space. A population cannot keep multiplying by the same positive factor indefinitely in a finite container. One alternative is a logistic growth law, where the *fractional* growth rate decreases as the population approaches a carrying capacity. At small populations it can resemble exponential growth. Near the capacity it slows toward a plateau. The logistic curve is a model with its own assumptions, not a universal correction that makes every exponential safe.

It helps to distinguish three statements that are often collapsed. A variable can be increasing. Its increases can be accelerating. And it can be increasing **exponentially**, which means that under a fixed interval convention, the same multiplicative factor repeats. These are not synonyms. A function like time squared grows faster and faster without being exponential. A diminishing quantity can follow an exponential exactly.

The question to ask whenever a percentage appears is: a percentage **of what**, applied **when**, and compounded **how**? Logarithms answer inverse questions, exponential models describe proportional change, and unit-aware rates let us transfer the same idea from finance to chemistry, biology, and differential equations without confusing the underlying assumptions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Discrete recurrence \(x_{n+1}=(1+r)x_n\) gives \(x_n=x_0(1+r)^n\). For positive \(x_0\) and \(1+r>0\), the real-valued threshold time for \(x_n=K\) is \(n=\log(K/x_0)/\log(1+r)\), with integer updates requiring a ceiling when the direction of monotonicity is appropriate.

Compounding with nominal rate \(r\) and \(n\) subperiods per unit time yields \(x(1)=x_0(1+r/n)^n\to x_0e^r\) as \(n\to\infty\). A continuous model satisfying \(x'(t)=kx(t)\) has \(x(t)=x_0e^{kt}\). For decay \(k<0\), \(t_{1/2}=\ln 2/|k|\). In a full statistical model, parameter estimation should reflect the noise mechanism rather than silently log-transform all observations.

**Saturation contrast:** logistic ODE \(x'(t)=rx(t)(1-x(t)/K)\) has equilibria \(0\) and \(K\), and for \(0<x(0)<K\), solution \(x(t)=K/(1+A e^{-rt})\) with \(A=K/x(0)-1\). For \(x\ll K\), \(1-x/K\approx1\) and the model behaves approximately exponentially.

### Exercises and solutions

1. **Doublings.** A culture begins with 40 units and doubles every three hours. What is its idealized value after 12 hours? **Solution:** four doublings give \(40\cdot2^4=640\).
2. **Half-life.** What fraction remains after two and a half half-lives? **Solution:** \(2^{-2.5}\approx0.1768\), if continuous exponential decay underlies the half-life model.
3. **Compounding.** Explain why a stated 12% nominal annual interest compounded monthly is not 12% effective annual interest. **Solution:** the annual multiplier is \((1+0.12/12)^{12}\), approximately 1.1268, not 1.12.
4. **Dimensions.** If \(t\) is in hours, what units must \(k\) have in \(e^{-kt}\)? **Solution:** inverse hours.

### Reading and attribution

- OpenStax, *Precalculus 2e*, Chapter 4, exponential and logarithmic functions: https://openstax.org/books/precalculus-2e/pages/preface.
- OpenStax, *Calculus Volume 2*, differential equations and growth/decay: https://openstax.org/details/books/calculus-volume-2.
- The paired jar thought experiment and unit-based comparisons are original exposition.
