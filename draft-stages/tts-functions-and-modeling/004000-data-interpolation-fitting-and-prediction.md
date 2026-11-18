# From Data Points to a Predictive Function

**Track:** Functions, Scales, and Mathematical Modeling  
**Lecture:** 004000  
**Preparation:** Functions, coordinates, simple equations, mean and variation.  
**Companion:** Interpolation, least squares, residuals, validation and extrapolation.

<!-- BEGIN SPOKEN LECTURE -->

A student records the height of a plant on three mornings. At day zero it is one centimeter high. At day one it is two centimeters high. At day two it is one centimeter high. Perhaps the plant bent, perhaps the measurement changed, perhaps this isn't even a plausible plant. For now, treat the three pairs of numbers as data and ask a mathematical question: **what function do they determine?**

The answer is not one function. Infinitely many functions pass through three points. Draw straight line segments between them and you have one interpolation. Draw a smooth curve that passes through all three and you have another. Draw a function with small oscillations between the measured times and you have infinitely more. Observing three values does not reveal the complete rule that generated them.

One possible curve is a quadratic. Set height equal to one plus two times t minus t squared. At t equal to zero it gives one. At t equal to one it gives two. At t equal to two it returns to one. The curve passes through all three observations exactly. We have **interpolated** the observations. If we now ask for the predicted height on day three, the quadratic gives negative two centimeters. A prediction can be a mathematically correct consequence of a fitted formula and still be physically impossible. That is the danger of extrapolation: the observations constrain the model in the observed region much more strongly than beyond it.

Another model is a straight line. No single straight line passes through the three points. We therefore need a principle for choosing a line that makes a reasonable compromise. One common choice is **least squares**: calculate the difference between each observed height and the line's predicted height, square the differences, and choose the line whose total squared difference is smallest. Those differences are called residuals. Squaring makes positive and negative residuals contribute positively, and it makes large deviations count more heavily.

For this symmetric three-point dataset, the least-squares line is horizontal at four thirds of a centimeter. The observed values are one, two, and one. Their average is four thirds, and the symmetry around day one makes the best-fit slope zero. The residuals are negative one third, positive two thirds, and negative one third. Their sum is zero, and their squared sum is two thirds. We are not claiming the plant is really constant. We are describing the best line under a particular optimization criterion.

Notice that the quadratic has zero training error and the straight line has positive training error. Does that prove the quadratic is a better predictor? No. We deliberately gave it enough flexibility to interpolate the observed values. If observations contain noise, a flexible function may fit that noise as if it were a genuine pattern. This is one form of overfitting. A small training residual is not the same thing as a reliable forecast.

We can explain the distinction with a repeated-measurement example. Suppose the true temperature of a room is constant, but a cheap thermometer gives slightly different readings each minute. A high-degree polynomial could pass through every recorded value. The thermometer's random fluctuations would then appear as a complicated, smooth temperature trajectory. Extrapolate that curve and it may shoot upward or downward. A constant-temperature model could have a worse fit to the individual observations but much better predictions of later readings.

The best function family comes partly from what we know about the mechanism. A moving object with constant speed motivates a straight-line relationship between distance and time. Constant acceleration motivates a quadratic position-versus-time model, under the usual idealizations. A cooling process with a proportional temperature difference can motivate an exponential approach to ambient temperature. If we ignore the mechanism and try many formulas until one fits, the search itself contributes uncertainty that a displayed curve does not reveal.

There is a difference between **interpolation** and **regression**. Interpolation asks for a function matching the given points, typically exactly. Regression asks for parameters of a statistical relationship that need not pass through every observation. Both need assumptions. An interpolating spline specifies how to connect values between observations. A regression model specifies an average or conditional relationship and often an error distribution. Neither method can prove the data-generating mechanism just from a good fit.

Another distinction concerns predictions inside and outside the observed range. Estimating the temperature at eleven thirty from measurements at eleven and twelve is interpolation in time. Predicting the room's temperature a month later is extrapolation. The latter relies much more heavily on assumptions about how long the pattern continues. Likewise, predicting a price for a house with features represented in the training data is different from predicting for a type of house never observed.

Before trusting the fit, ask whether the residuals contain a pattern. Suppose a fitted line systematically underpredicts small inputs, overpredicts middle inputs, and underpredicts large ones. That curved residual pattern suggests the line missed structure. Suppose residuals grow with the fitted value. Then the variability may depend on scale, and an equal-error assumption may be inappropriate. A residual plot does not prove a model is correct when it looks random, but it can reveal important failures.

A useful test is to hold back observations that were not used to select the model, then ask how accurately it predicts those observations. For time-dependent data, the split should often respect time: predict the future from the past, not the past from the future. Randomly dividing strongly autocorrelated observations can make the test look much easier than the intended prediction problem. And when many models have been repeatedly tuned against the same holdout, that holdout is no longer a truly untouched test.

Uncertainty enters at several different levels. Measurements may be noisy. A finite sample may not determine the best parameters precisely. The chosen model family may omit mechanisms. Future conditions may differ from the past. Those are not interchangeable problems, and no single confidence band summarizes them all automatically. Statistical models can quantify some sources of uncertainty conditional on stated assumptions; they cannot certify that the assumptions will remain true.

A related trap is causality. Suppose the number of bicycles rented increases on warmer days. Temperature might help predict rentals, yet it does not follow that changing the temperature by one degree would cause the precise increase shown by a regression slope. Weekends, holidays, season, and other factors may move both variables. A fitted mathematical relationship is not automatically the effect of an intervention.

Here is a sound modeling workflow. Begin with the question you actually want to answer. List the allowed inputs, outputs, and units. Choose a family of functions because of geometry, mechanism, or an explicit statistical assumption. Fit its parameters to the available observations. Check residuals and physical constraints. Evaluate predictions on data that played no role in selecting the model. Then state which inputs and conditions the fitted function has earned the right to predict.

The three plant measurements did not give us a unique curve. They gave us a problem of inference. That is the bridge from functions and graphs to numerical optimization, probability, and scientific prediction: a mathematical model becomes informative not merely when it can draw a line through data, but when we can explain what the line assumes and how its predictions could fail.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Given observations \((x_i,y_i)\), polynomial interpolation of distinct abscissae \(x_i\) has a unique polynomial of degree at most \(n-1\), but many functions and higher-degree polynomials can fit the same \(n\) points. For \((0,1),(1,2),(2,1)\), the unique interpolating quadratic is \(q(x)=1+2x-x^2\), which predicts \(q(3)=-2\).

A least-squares line \(\hat y=a+bx\) minimizes \(S(a,b)=\sum_i(y_i-a-bx_i)^2\). With \(\bar x=1\) and \(\bar y=4/3\), \(\sum_i(x_i-\bar x)(y_i-\bar y)=0\), so \(b=0\) and \(a=4/3\). The residuals are \((-1/3,2/3,-1/3)\), giving \(S=1/9+4/9+1/9=2/3\). In vector notation, least squares is an orthogonal projection of \(y\) onto the column space of a design matrix when the Euclidean residual norm is used.

A fitted mean \(\hat m(x)\) is not automatically an individual-outcome prediction interval, a confidence interval for \(m(x)\), or a causal effect. Each requires additional assumptions and an appropriate uncertainty calculation.

### Exercises and solutions

1. **Interpolation.** Give two different functions that pass through \((0,0)\) and \((1,1)\). **Solution:** \(f(x)=x\) and \(g(x)=x^2\).
2. **Extrapolation.** Does a polynomial that matches all measured values guarantee sensible outputs beyond them? **Solution:** no; the interpolating quadratic here predicts negative height at day three.
3. **Residuals.** If an observed value is 7 and the fitted value is 9, what is the residual using observed-minus-fitted convention? **Solution:** \(-2\).
4. **Selection bias.** Why is evaluating many candidate models on the same holdout a problem? **Solution:** model selection adapts to its errors, making the holdout's apparent performance optimistic for a genuinely new sample.

### Reading and attribution

- OpenStax, *Introductory Statistics 2e*, regression and residual analysis: https://openstax.org/details/books/introductory-statistics-2e.
- NIST/SEMATECH, *e-Handbook of Statistical Methods*, regression and model checking: https://www.itl.nist.gov/div898/handbook/.
- The deliberately underdetermined plant measurements and explicit quadratic/linear calculation are original examples.
