# 035000 - Hypercontractivity: Why Boolean Functions Have Influential Coordinates

**Track:** Discrete Mathematics and Combinatorics. **Background:** Fourier characters on the Boolean cube, probability, expectations, and basic norm inequalities. **Central question:** how does adding independent noise constrain the high-degree behavior of a Boolean function?

<!-- BEGIN SPOKEN LECTURE -->

# A voting rule with millions of inputs

Imagine a decision made from millions of yes-or-no votes. We can ask whether one particular voter has substantial power to change the outcome. Or perhaps every voter has little individual power while the collective decision still responds sharply to a shift in public opinion. These questions sound political, but their mathematical content is about functions on a Boolean cube.

A Boolean function assigns an output of plus one or minus one to each vector of independent fair input bits. The Fourier expansion writes the function as a sum of products of coordinate variables. Each product corresponds to a subset of coordinates and has a coefficient measuring how much that interaction contributes.

A low-degree term depends on few coordinates. High-degree terms involve intricate interactions among many bits. Hypercontractivity is an inequality that constrains how concentrated a function can become after its higher-degree terms are suppressed. It is the bridge from algebraic Fourier expansions to inequalities about individual influences and sharp probability thresholds.

# Noise does not simply erase information

Introduce a noise operation. Start from an input vector, and independently keep each bit with some correlation parameter rho while refreshing the rest. The value of the original function and its value at the noisy input are correlated, but the correlation weakens as the noise increases.

In Fourier coordinates the noise operator is unusually simple: it multiplies a coefficient indexed by a subset of size d by rho to the power d. Degree zero is unchanged. Degree one is reduced by one factor of rho. Degree ten is reduced by ten such factors. The operator therefore damps complicated interactions more strongly than simple interactions.

This diagonal action is the first key insight. We can study noise by studying the degrees of Fourier coefficients, without following each possible noisy input separately. The analysis becomes a comparison between norms of a weighted polynomial.

# Two norms measure different kinds of size

The second moment of a function measures its average squared magnitude. The fourth moment is more sensitive to rare large values. A function that is usually near zero but occasionally very large can have a moderate second moment and a much larger fourth moment.

Hypercontractivity says that after enough noise has been applied, the fourth-moment norm cannot exceed the original second-moment norm. On the unbiased Boolean cube, a standard form is obtained when the correlation rho is at most one divided by the square root of three.

The phrase is worth unpacking. The noisy function may still contain many Fourier terms, but its large deviations are limited by the original energy. This is more informative than the elementary fact that noise decreases the second moment. We are controlling a stronger norm by a weaker one, made possible by smoothing.

# Check the inequality on two bits

Consider the function that adds the first two input bits. It can take values negative two, zero, or positive two. Its squared average is two, so its second-moment norm is the square root of two. Its fourth moment is eight, so its fourth-moment norm is the fourth root of eight.

After applying noise with correlation rho, both terms are simply multiplied by rho. The fourth-moment norm becomes rho times the fourth root of eight. If rho equals one over the square root of three, the result is smaller than the original second-moment norm, as hypercontractivity predicts.

This is not a proof of the theorem for arbitrary Boolean functions, but it makes the mechanism visible. A degree-one example has an easy response to noise. A high-degree monomial shrinks even faster. The difficulty is how many different monomials can combine to create large peaks. The tensor-product proof of hypercontractivity controls precisely that collective effect.

# From noise bounds to low-degree inequalities

Take a function whose Fourier expansion contains no degrees higher than d. We can start with a noisy version at correlation one over the square root of three and then compensate for the attenuation of each degree. Because each Fourier level is at most d, one obtains a bound on the fourth norm of the original low-degree polynomial by three to the power d over two times its second norm.

Thus low-degree functions cannot hide an arbitrarily large fourth moment while keeping the second moment fixed. The constant grows exponentially with degree, and this is appropriate: a polynomial of degree thirty can behave more sharply than a linear function. Hypercontractivity is not claiming that all Boolean functions are smooth or that high degrees are harmless.

The real use comes when a problem forces much of the Fourier mass to low levels, or when carefully chosen derivatives and restrictions have controlled degree. Then a moment inequality can translate algebraic structure into a probability bound.

# Influence measures sensitivity to one coordinate

The influence of coordinate i is the probability that flipping just that input bit changes the value of the function. For a plus-or-minus-one Boolean function, this equals a sum of squared Fourier coefficients over subsets containing i. The total influence equals the sum, over all nonempty subsets, of subset size times the squared Fourier coefficient.

This identity tells us where sensitivity lives in the Fourier spectrum. High-degree mass contributes strongly to total influence because each high-degree interaction includes many coordinates. But a function can distribute influence over many coordinates, making every single one small.

The Kahn-Kalai-Linial theorem places a limit on that distribution. For a balanced Boolean function on n unbiased independent bits, some coordinate has influence at least a constant times logarithm of n divided by n. This is stronger than the elementary average-influence lower bound of order one over n.

# Why a logarithm appears

A proof can be organized by taking discrete derivatives of the Boolean function, applying a hypercontractive inequality to those derivatives, and summing Fourier energies. If every derivative had too little mass, the variance of the original function could not remain as large as it is. The contradiction forces one influential coordinate.

Hypercontractivity enters because the derivatives are sparse in the sense that they are nonzero exactly when a bit is pivotal. Their second and higher moments encode the probability of that pivotal event. Comparing norms after noise turns tiny pivotal probabilities into a structural restriction on the Fourier coefficients.

The exact quantitative proof needs a choice of correlation parameter depending on the hypothesized maximal influence. That optimization is where the logarithm appears. It would be misleading to claim that one application of the moment inequality without any further argument already gives KKL.

# Sharp thresholds and the limits of the claim

Consider a monotone property of a randomly chosen subset: once the property holds, adding more elements cannot make it fail. Its probability increases as the inclusion probability rises. Russo's formula relates the derivative of this probability to the total influence at that inclusion probability. Thus influence lower bounds can imply that the transition from unlikely to likely happens over a narrow window.

But a sharp-threshold conclusion needs assumptions, such as monotonicity and conditions that prevent one coordinate from dominating. KKL in its usual form concerns Boolean-valued functions under a product measure. It cannot simply be transferred unchanged to arbitrary real-valued functions or arbitrary dependent inputs.

Examples clarify the scale. Majority voting has individual influences on the order of one over the square root of n. A carefully balanced tribes function spreads influence more evenly, with maximal influence of order logarithm n over n, showing the KKL scale is essentially optimal.

The lesson is that noisy smoothing can uncover rigidity. Fourier coefficients describe every interaction. Hypercontractivity controls how those interactions concentrate. Influence identities translate spectral energy into pivotal probabilities. Together they explain why a genuinely variable Boolean rule cannot hide all of its sensitivity equally well in every coordinate.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For uniform `x in {-1,1}^n`, define `chi_S(x)=product_(i in S) x_i`, `f=sum_S fhat(S) chi_S`, and `T_rho f=sum_S rho^|S| fhat(S)chi_S`. Bonami-Beckner hypercontractivity gives
\[
 \|T_\rho f\|_q\le\|f\|_p
 \quad\text{if }1<p\le q<\infty,\;0\le\rho\le\sqrt{\frac{p-1}{q-1}}.
\]
In particular, `||T_(1/sqrt(3)) f||_4 <= ||f||_2`. If `deg(f)<=d`, then `||f||_4<=3^(d/2)||f||_2`.

For `f:{-1,1}^n->{-1,1}`, `Inf_i(f)=Pr[f(x)!=f(x^(i))]=sum_(S includes i) fhat(S)^2`, and `I(f)=sum_S |S| fhat(S)^2`. For balanced Boolean f, the KKL theorem gives `max_i Inf_i(f)>=c log(n)/n` for an absolute c>0 and n>=2. General-variance versions require their corresponding constants and hypotheses. For `f(x)=x_1+x_2`, `E f^2=2`, `E f^4=8`, and `||T_rho f||_4=rho*8^(1/4)`.

### Exercises with answers

1. What does noise do to a Fourier coefficient of degree five? **Answer:** multiplies it by `rho^5`.
2. For `f=x_1 x_2 x_3`, what is `||T_rho f||_2`? **Answer:** `rho^3` for nonnegative rho.
3. If f is plus-or-minus-one valued, why is `Inf_i` a Fourier energy? **Answer:** the discrete derivative squared is the pivotal indicator, and Parseval sums the squared coefficients containing i.
4. Does KKL imply every input has influence of order `log(n)/n`? **Answer:** no, only that at least one coordinate does.

### Reading and source notes

- [Ryan O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf), hypercontractivity, KKL and sharp thresholds.
- [MIT OpenCourseWare, Analysis of Boolean Functions](https://ocw.mit.edu/courses/18-218-topics-in-combinatorics-analysis-of-boolean-functions-spring-2021/download/), lecture notes on influences and hypercontractivity.
- [Kahn, Kalai and Linial, The Influence of Variables on Boolean Functions](https://doi.org/10.1109/SFCS.1988.21923), original influence theorem and logarithmic lower bound.
