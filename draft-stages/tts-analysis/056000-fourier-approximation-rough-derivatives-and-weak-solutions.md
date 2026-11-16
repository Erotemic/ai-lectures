# Fourier approximation, rough derivatives, and weak solutions

<!-- BEGIN SPOKEN LECTURE -->

# Fourier approximation, rough derivatives, and weak solutions

## Fourier Series, Convolution, and the Shape of Approximation

Picture a tone played on a violin. Its shape in time can be complicated, but a listener hears a pitch and a collection of overtones. Fourier analysis takes that observation seriously: many functions can be described by the strength and phase of elementary oscillations.

For a periodic function, the elementary oscillations are the integer-frequency sines and cosines, or their compact expression as complex exponentials. To find how much of frequency N is present, multiply the function by an oscillation running backward at that frequency and average over one period. Rapid oscillations then cancel, while the matching frequency survives. The resulting number is the Fourier coefficient.

Begin with a simple wave: one sine at frequency one plus half a sine at frequency three. Its coefficients are nonzero only at those frequencies and their negative partners in complex notation. There is no mystery about reconstruction: put those components together and you recover the original signal exactly.

A more interesting function might have a jump, like a square wave that switches instantly between two values. Its Fourier series has infinitely many frequencies. Finite partial sums oscillate around the jump, and pointwise convergence becomes delicate. It would be a mistake to treat this as failure of Fourier analysis. We need to ask in which sense the approximation is intended to work.

In the Hilbert space L two on the circle, the complex exponentials form an orthonormal basis after normalization. The Fourier partial sums are orthogonal projections onto finite collections of frequencies. The Pythagorean theorem then tells us that these projections converge in mean square. This does not claim uniform convergence, nor convergence at every point. It is an energy statement. Many rough signals still have finite energy even when their graphs are not smooth.

There is another way to approach approximation, one that leads directly to convolution. Suppose we replace each value of a function by a weighted average of nearby values. Let the weights be given by a kernel whose total integral is one. When the kernel becomes increasingly concentrated near zero, we expect this averaging to reproduce the original function. Such a family is called an approximate identity.

Think of photographing a sharp edge through a blurred lens. The recorded image is the original intensity convolved with a blur kernel. If the blur is narrow and nonnegative, most of the recorded intensity near a point comes from nearby points. As the blur width shrinks, the image approaches the original in appropriate norms, though the exact value at a discontinuity may be more subtle.

Convolution is the operation that takes two functions and averages one against translated copies of the other. It has an important algebraic property: when the relevant integrals converge, convolution is commutative and associative. That makes repeated smoothing relatively easy to analyze. But convolution also carries a deeper spectral property: Fourier coefficients turn convolution on the circle into multiplication, up to the convention used for normalizing the integral.

Why does that happen? Each complex exponential is an eigenfunction of translation. If we shift an oscillation, we change only its phase. Convolution averages many shifts, so each frequency is multiplied by one scalar determined by the kernel. The calculation is the same functional-calculus idea we met when an operator acted diagonally on eigenvectors. Here the operator is smoothing and the eigenvectors are Fourier modes.

Consider the heat equation on a circle. An initial temperature pattern can be decomposed into Fourier modes. Under heat flow, the N-th mode decays at a rate proportional to N squared. In other words, the heat kernel is an approximate identity at short times and a powerful low-pass filter at longer times. The two perspectives—averaging in physical space and multiplying in frequency space—describe the same operation.

But not every approximate identity produces pointwise convergence everywhere. We generally obtain convergence in L p for finite p under standard assumptions. With suitable kernels we get convergence at points of continuity, or almost everywhere for functions in the right class. A discontinuity is not an excuse to suppress these qualifications. They tell us exactly what kind of reconstruction the Fourier tools guarantee.

The Fejér kernel makes a particularly clear example. Rather than taking the first N Fourier modes with equal weight, it averages the first N partial sums. The resulting multipliers taper from one near frequency zero toward zero at the cutoff. These kernels are nonnegative and have total mass one. Thus the averaged Fourier sums converge uniformly for every continuous periodic function. For square-integrable functions, they converge in mean square. A small change in how we combine Fourier modes makes an enormous difference to the behavior near jumps.

This leads to a useful principle for applications. If a computation repeatedly smooths or filters data, ask what its multipliers do to high frequencies. If a numerical solution develops ringing near a discontinuity, distinguish sharp spectral truncation from a positive averaging kernel. If a theorem promises reconstruction, identify the norm or pointwise notion in which it is valid.

Fourier series and convolution are therefore not separate tricks. They are dual views of translation-invariant operations: one in terms of localized averages, and one in terms of frequency multipliers. The first connects to differential equations and probability; the second connects directly to functional calculus and numerical algorithms.

## The Fourier Transform: Plancherel, Derivatives, and the Heat Equation

Periodic sounds invite Fourier series because their frequencies come in integer multiples of one fundamental rhythm. What about a single clap, a pulse of light, or a temperature profile on an entire line? Those signals do not repeat. Their frequency description must be continuous rather than a list of integer coefficients.

The Fourier transform provides that description. Given a rapidly decaying function, multiply it by a complex oscillation of frequency xi running backward, then integrate over the entire line. The result is a function of xi. Large values mean that the original signal contains a strong component at that frequency; the complex phase remembers how those components line up in physical space.

A narrow pulse illustrates the trade-off between location and frequency. Consider a bell-shaped Gaussian. Its Fourier transform is another Gaussian. Make the pulse very narrow in space, and its transform becomes broad in frequency. Make the pulse broad in space, and its transform becomes narrow. This is not a numerical artifact. It is a structural constraint: pinpointing a signal in one domain spreads it in the other.

The inverse transform rebuilds the original function by integrating all frequencies with the matching forward phase. Exact constants depend on our convention. If we define the transform without a normalization factor in the forward integral, the inverse has a factor of one divided by two pi in one dimension. Consistency is the important point, because the derivative and convolution rules inherit those constants.

Take a smooth function that decays sufficiently rapidly. What happens to its derivative under the Fourier transform? Integrate by parts. The boundary term disappears because the function decays. A derivative in physical space becomes multiplication by imaginary frequency in transform space. A second derivative becomes multiplication by minus frequency squared.

This single rule explains why Fourier analysis is so natural for differential equations. The heat equation says that the time derivative equals the second spatial derivative. After taking the Fourier transform in space, the differential equation becomes a separate ordinary equation for each frequency. Each frequency decays exponentially at a rate proportional to its square. Inverting the transform yields the evolving temperature profile.

The transformation also changes convolution into multiplication. If an input signal is blurred by averaging it against a kernel, the output's transform is the input transform times the kernel transform. Conversely, multiplying by a frequency filter corresponds to convolution with a spatial kernel when the required integrability holds. The same two operations can look complicated in one representation and simple in another.

So far our integrals seem to require functions that are integrable over the line. But an energy signal may be square integrable without being absolutely integrable. What should its Fourier transform mean if the defining integral does not converge in the usual sense?

Plancherel's theorem gives the answer. Begin with smooth rapidly decaying functions, where all the formulas are safe. Their Fourier transforms preserve squared L two energy up to the normalization constant. Since those functions are dense in L two, the transform extends uniquely by continuity to every L two function. We no longer need to interpret the transform as a pointwise integral for arbitrary inputs. It is an operator defined by a convergent sequence in the L two norm.

This is a powerful conceptual step. Mathematics often extends a formula from a well-behaved dense class to a larger space by showing it preserves or controls the relevant norm. The same idea built continuous functional calculus from polynomial approximations and now builds the Fourier transform for finite-energy signals.

Plancherel also reveals an elegant form of the spectral theorem. On the line, differentiation is not a bounded operator on L two; its domain contains functions with square-integrable weak derivatives. But the Fourier transform turns the derivative into multiplication by imaginary frequency. The negative second derivative becomes multiplication by nonnegative frequency squared. If we know how to apply a scalar function to multiplication by frequency squared, we can apply that function to the spatial differential operator. That recovers heat filters, wave propagators, and fractional powers of the Laplacian.

There is a catch. When a multiplier grows with frequency, not every L two signal remains in L two after multiplication. The operator has a domain: those inputs whose frequency content decays enough to counter the growth. This is exactly the domain condition from unbounded functional calculus, expressed in concrete frequency language.

For example, a function may have finite energy while its gradient does not. Squared energy only measures the integral of the magnitude squared of the function. Gradient energy weights the high frequencies by frequency squared. Such a function lies in L two but not in the first-order Sobolev space. We are approaching the need for weak derivatives and Sobolev spaces, where the Fourier picture will give both precise definitions and estimates.

Fourier transforms are therefore not simply a change of coordinates for signals. They turn translation-invariant differential operators into multipliers, make energy preservation transparent through Plancherel, and give a practical way to measure regularity by examining how much high-frequency energy a function carries.

## Frequency Localization: Why Derivatives Measure High Frequencies

Imagine looking at an aerial photograph from farther and farther away. Individual leaves disappear first; roads and coastlines remain. Each change of scale discards fine details and preserves coarser structure. Fourier analysis gives a mathematical way to separate those scales. Instead of blurring everything at once, we can ask what happens in one band of frequencies at a time.

Start with a square-integrable signal on the line. Its Fourier transform describes how its energy is distributed across frequencies. Build a filter that keeps low frequencies and suppresses high ones. In physical space this is a convolution with a kernel. The filter is a multiplier in frequency space, because it simply scales the contribution of each frequency.

There are two different kinds of filters. A sharp cutoff keeps all frequencies below a threshold and discards the rest. A smooth cutoff gradually transitions between keeping and discarding. Both can be useful, but a sharp cutoff has a spatial kernel that decays slowly and oscillates. A smooth cutoff generally gives better spatial localization. This is a version of the same trade-off we saw with Gaussian pulses: selecting a compact range of frequencies creates spread in space.

Why split a signal into bands instead of just low and high? Because derivatives act differently at different scales. For a single sine wave at frequency N, differentiation multiplies its amplitude by N, and a second derivative multiplies it by N squared, apart from a sign. So when a signal lives mainly near frequency N, its derivative norm is approximately N times its original norm. This is much easier to reason about than differentiating an arbitrary complicated waveform point by point.

Suppose we filter a function to frequencies with magnitude roughly between N and twice N. In L two, differentiating that filtered function multiplies each component by a number between N and twice N. By Plancherel's theorem the derivative norm is therefore between N and twice N times the original norm, assuming the band and weights are chosen appropriately. That gives a precise relationship between smoothness and frequency location.

Now think about a function whose energy is spread over many scales. If we assign a weight increasing like N to the contribution from each band, we penalize fine-scale oscillations. A Sobolev norm of first order does exactly this, in a quadratically combined form. A general fractional Sobolev norm weights frequency xi by a power of one plus xi squared. Regularity is not an all-or-nothing declaration that a derivative exists at every point. It is a quantitative statement about how much energy the high frequencies carry.

This is why rough functions can have fractional smoothness. An image edge may not have an ordinary derivative at the jump. Yet a softened version might have a finite fractional regularity measure. To understand what numerical smoothing does to such data, we ask which frequency bands it attenuates and by how much.

Frequency localization is also a way to compare two operators. Consider the resolvent of one minus the second derivative. In frequency coordinates, solving the equation one minus the second derivative applied to u equals f means dividing each frequency component by one plus frequency squared. High frequencies become strongly damped. A forcing f with finite L two energy produces a solution whose second derivatives, interpreted in the weak L two sense, also have finite energy. The multiplier immediately suggests a gain of two derivatives.

A different multiplier might grow with frequency instead of decaying. Multiplying by the square root of one plus frequency squared has the effect of taking one derivative's worth of regularity. Its domain is not all of L two. We can ask which functions survive that multiplier as L two functions; the answer is the first-order Sobolev space.

There is an important caveat when moving beyond L two. Plancherel makes it easy to bound an operator from a bounded multiplier: just take the maximum magnitude of the multiplier. But an arbitrary bounded function of frequency does not necessarily define a bounded multiplier on L p when p is different from two. For those spaces, additional smoothness or structure in the multiplier is needed. This is where deeper theorems, such as the Mikhlin multiplier theorem, begin.

Even in L two, not every claim about sharp pointwise regularity follows from a simple multiplier estimate. A finite-frequency projection is smooth in the classical sense, but limits of those projections may converge only in L two. To recover derivatives or continuity of the limit, we need uniform control in a stronger norm, and that is precisely the role of Sobolev estimates.

These observations prepare a practical bridge to differential equations. Constant-coefficient linear equations can often be solved frequency by frequency. Variable-coefficient equations couple different frequencies, so the simple diagonal picture no longer holds. Nevertheless, estimates organized by scale remain useful: they reveal where energy can move, which terms cost derivatives, and where a nonlinear interaction can create fine structure.

Frequency localization lets us hear an equation at different resolutions. It tells us not only which oscillations are present, but how strongly a differential operator acts on each one. This makes abstract statements about weak derivatives, smoothing, and regularity much more concrete.

## Distributions: Making Sense of Delta Functions and Rough Derivatives

Imagine a string tied at one point and struck sharply with a hammer. The force is concentrated in a very short time. In a simple model we idealize it as an instantaneous impulse, a force with finite total effect but no ordinary finite height at the instant of impact. Physicists call it a delta impulse. How can such a thing belong to mathematics if it is not an ordinary function?

The idea behind distributions is to stop asking for the value of the object at a point and ask instead what it does when we test it against a smooth function. A delta concentrated at zero takes a smooth test function and returns that test function's value at zero. It is a linear measurement. We do not need to pretend the delta is an infinitely tall function.

The test functions are smooth and have compact support. Compact support means each test function vanishes outside some bounded region. We choose them because we can differentiate them as many times as needed, and when we integrate by parts their boundary terms disappear. A distribution is a continuous linear functional on this test-function space, with its special topology. The topology matters, but a first example makes the idea tangible.

Any locally integrable function f defines a distribution. Given a test function phi, multiply f by phi and integrate. If two functions agree almost everywhere, they define the same distribution. So distributions already contain the usual Lebesgue-function world. They simply give us a new way to describe what an object does rather than how it looks point by point.

Now take the step function that is zero on the negative half-line and one on the positive half-line. Classically its derivative is zero everywhere except at zero, where the derivative does not exist. But its height changes by one, and we would like the derivative to record that total jump. The distributional derivative does exactly that.

Here is the definition. The derivative of a distribution acts on a test function by taking the negative of the original distribution applied to the derivative of the test function. Why the minus sign? For ordinary smooth functions, integration by parts moves the derivative from one factor to the other and introduces a minus sign. We adopt that identity as the definition even when the original object is not differentiable in the classical sense.

Apply this rule to the step function. The result is minus the integral from zero to infinity of the derivative of phi. Since phi eventually vanishes, this equals phi at zero. But that is precisely what the delta distribution does. So the derivative of a unit step is a delta. A jump in position is recorded as an impulse in the derivative.

Try the absolute value function. It has a corner at zero. Its ordinary first derivative is minus one on the negative half-line and plus one on the positive half-line. That first derivative exists as an ordinary locally integrable function, so it also defines a distribution. Differentiate again using the distribution rule. The sign function jumps by two at zero, so its distributional derivative is twice the delta. The second derivative of absolute value is therefore twice a delta, not a classical function.

A related example comes from three-dimensional electrostatics, but it is simplest to hear in one dimension. A sharply localized source can create a potential that is continuous but has a kink. Differentiation once gives a change of slope; differentiation twice detects the localized source. That is the prototype for the Green-function method in differential equations: a fundamental solution is something whose differential operator produces a delta.

The Fourier transform fits this language. A delta at zero transforms into the constant function one under the convention without a normalization factor in the forward transform. This says a perfectly localized impulse contains all frequencies equally. Conversely, a constant signal has its Fourier transform concentrated at zero frequency, in the distributional sense. The location-frequency trade-off has reached its limiting case.

Distributional derivatives have another advantage: every distribution can be differentiated as many times as desired. But this does not mean every distribution has an ordinary derivative, nor that all these derivatives are functions. A useful question is whether a distributional derivative happens to be represented by an integrable or square-integrable function. If it is, we can begin to measure regularity, which will lead to Sobolev spaces.

Sometimes distributions are also called generalized functions. The term can mislead us into treating every distribution as if it had pointwise values. Most do not. We can evaluate a distribution on test functions and combine it with smooth coefficients; multiplying two arbitrary distributions is not generally defined. For example, the product of two delta distributions at the same point has no canonical value in standard distribution theory. This is a genuine obstacle in nonlinear partial differential equations, not a notation problem.

How should we interpret a differential equation in this language? Suppose a rough u and a source f satisfy an equation involving a derivative. We test the equation against every smooth compactly supported phi. Then we move the derivatives off u and onto phi by integration by parts. If the resulting equality holds for all test functions, we say the equation holds in the distributional sense. This can make sense even when u cannot be differentiated pointwise.

The central shift is from asking whether a formula holds at each point to asking whether every smooth probe detects the same result. For well-behaved functions, the two viewpoints agree. For jumps, concentrated sources, and rough solutions, the distributional viewpoint retains precisely the information that classical differentiation would otherwise lose.

## Mollifiers and Weak Derivatives: Smooth Approximations to Rough Functions

A photograph taken through a lens is never infinitely sharp. Yet if we choose a sequence of finer lenses, the blurred images can approach the original scene. Mathematical smoothing works in a similar way. It gives us an approximation procedure for rough functions, and that procedure is the bridge between classical calculus and weak calculus.

Choose a smooth nonnegative function, call it rho, supported in a small region around zero, whose integral is one. We can rescale it to make it narrower and taller while keeping total area one. Convolve an integrable function f with this scaled rho. The result averages f over a neighborhood whose width is controlled by the scale. We call rho a mollifier.

Why is this powerful? Even if f is merely locally integrable, the convolved function is smooth wherever the convolution is defined appropriately. To differentiate the result, we differentiate the mollifier, not the rough f. The smooth kernel does the analytic work. Moreover, as the scale approaches zero, the mollified functions converge to f in L p for finite p, under the standard whole-space assumptions or locally on an open set.

Consider the step function that jumps from zero to one. Its mollification replaces the jump with a smooth transition. The transition becomes steeper as the mollifier gets narrower. The first derivative of each smoothed step is an ordinary nonnegative bump with total integral one. In the limit, those derivatives do not approach an ordinary L one function. They approach the delta distribution. This is a concrete reason to distinguish convergence of functions from convergence of their derivatives.

Now suppose f has a weak derivative g that lies in L p. By definition, the integration-by-parts identity holds: when we integrate f against the derivative of a test function, we get minus the integral of g against the test function. Convolving both f and g with the mollifier preserves that relationship. The derivative of the smoothed f is exactly the smoothed g. As the scale shrinks, f and its derivative approach f and g in the relevant L p norms. Thus a weak derivative can be approximated by classical derivatives in a controlled way.

One example is the absolute value function on a bounded interval. It has a corner, so it is not continuously differentiable there. But its weak first derivative is the sign function, which is bounded and hence square integrable on that interval. The absolute value function therefore belongs to a first-order Sobolev space there. Its second distributional derivative is twice a delta, which is not an L two function. So it generally fails to belong to the second-order Sobolev space on any interval containing the corner.

Another example is a genuine jump. The indicator of the positive half-line has distributional derivative delta. On a bounded interval containing zero, that delta cannot be represented by an L one function, much less an L two function. The step is therefore not in the first-order Sobolev space when the interval crosses the jump. The contrast is instructive: a corner in the function can be acceptable at first order, while a jump cannot.

Why bother with weak derivatives instead of smoothing every physical solution and calling it good? Because we want a stable notion that survives limits. In a PDE computation, we might have a sequence of smooth approximate solutions whose ordinary derivatives are bounded in L two. Under suitable compactness or weak-convergence arguments, a limiting function can inherit a weak derivative even if its pointwise derivative is impossible to discuss. We need weak derivatives to formulate what the limit satisfies.

There is a delicate issue at boundaries. On the whole real line, convolution with a compactly supported smooth kernel is straightforward. On a bounded interval or a region with a curved boundary, the kernel may sample outside the domain. We can mollify safely in the interior, or use extension theorems when the domain has suitable geometry. We cannot claim that naive convolution automatically preserves boundary conditions. For example, smoothing a function that vanishes at the boundary can produce one that does not vanish there unless the construction is arranged carefully.

This issue motivates another space: the closure of smooth compactly supported functions under the first-order Sobolev norm. The functions in that closure are said to have zero trace in the appropriate sense, under standard domain assumptions. The trace is the generalized boundary value needed for weak boundary-value problems. A Sobolev function may lack ordinary pointwise boundary values, yet still possess a well-defined trace if its interior regularity and the boundary geometry are suitable.

Mollification has an intellectual role beyond merely obtaining differentiable formulas. It lets us prove an identity for smooth functions, obtain an estimate independent of the smoothing scale, and pass to the limit. This is a recurring proof pattern. One uses easy algebra where derivatives exist, then transfers the estimate to a larger space by completeness and controlled convergence.

The key is not to silently exchange limits and operations. We must know which quantities converge in L p, which only converge weakly, and which converge as distributions. When the relevant norms are controlled, mollification turns rough analysis into a rigorous extension of familiar calculus rather than a collection of new rules invented for difficult functions.

## Sobolev Spaces: Measuring Smoothness Without Pointwise Derivatives

In an elementary calculus course, a function is smooth if its derivatives exist and behave nicely at every point. In a differential equation, we often know much less. We may know that the energy of a solution is finite and that certain integrals of its derivatives are bounded. Is that enough to control the solution in a useful way? Sobolev spaces were designed to answer that question.

A first-order Sobolev function on an interval is a function whose value and weak first derivative both lie in a chosen L p space. We measure it by combining the sizes of those two pieces. The derivative is weak in the integration-by-parts sense, so the function need not be classically differentiable at every point. But it must have enough controlled variation that the derivative is represented by an ordinary L p function rather than a point mass.

A striking fact emerges in one dimension. If a function and its weak derivative are both square integrable on a bounded interval, the function has a continuous representative. More than that, the difference between its values at two points can be controlled by the square root of their distance times the L two norm of the derivative. This follows from writing the difference as an integral of the derivative and applying Cauchy–Schwarz.

So a norm that was defined in terms of integrals gives a conclusion about pointwise continuity. That is a Sobolev embedding: a quantitative bridge from integral regularity to more visible regularity. In one dimension, relatively little derivative control buys continuity. In higher dimensions, the relationship is more demanding.

Imagine a narrow spike in a two-dimensional image. A function can keep its integral small by concentrating its amplitude in a tiny region. Derivatives penalize concentration, but how strongly depends on the dimension and the exponent used. The Sobolev embedding theorem captures that balance. Roughly, a first-order derivative in L p controls extra integrability when p is below the spatial dimension, and can control continuity when p is above the dimension, with precise assumptions and critical cases.

The threshold is not merely a detail. At the critical exponent, naive statements can fail. In two dimensions, a first-order L two bound by itself does not guarantee a continuous representative. We can construct sequences that concentrate on smaller sets while keeping the relevant norm controlled. Stronger assumptions, special structures, or logarithmic estimates may provide substitutes, but there is no universal shortcut across the critical threshold.

On a bounded interval, we can see how derivative control suppresses oscillation. Take a sequence of sine waves whose frequencies rise while their amplitudes stay fixed. Their L two norms do not shrink, but their derivative norms grow proportionally to frequency. They cannot remain bounded in the first-order Sobolev norm. If we reduce their amplitudes enough to keep the derivative norms bounded, their function values tend to zero in L two. High-frequency energy cannot hide from derivative control indefinitely.

This observation leads to compactness theorems. On a bounded domain with suitable boundary regularity, a bounded family in the first-order Sobolev space has a subsequence that converges strongly in a lower-order L two norm, under the standard Rellich compactness hypotheses. The sequence need not converge in the full Sobolev norm. Derivatives may oscillate while functions converge. Compactness gives us just enough convergence to pass to limits in many nonlinear terms.

Consider approximate solutions to a boundary-value problem. An energy estimate might give a uniform bound on the square integral of the gradient. With a zero boundary condition and Poincaré's inequality, that gradient bound also controls the size of the function itself. We can extract a weakly convergent subsequence in the Sobolev space. Rellich compactness may then promote convergence of the functions to strong L two convergence. In a nonlinear equation, that distinction can be decisive, because products generally do not behave well under weak convergence alone.

The zero boundary condition requires care. A Sobolev function may have no classical value at an individual boundary point in higher dimensions, but a trace operator assigns its boundary data in an appropriate function space. The subspace often written H zero one consists of Sobolev functions whose trace vanishes, for suitable domains. It is the right energy space for a string or membrane held fixed at its boundary.

The Fourier viewpoint supplies a second description when we work on the whole line or Euclidean space. A first-order L two Sobolev norm is essentially the energy of the function's Fourier transform weighted by one plus frequency squared. That shows why derivatives control high-frequency oscillation. It also motivates fractional Sobolev spaces: weight by a fractional power instead of an integer one. These spaces measure smoothness between classical derivative orders.

We should not confuse Sobolev regularity with classical smoothness. A first-order Sobolev function in high dimension can be discontinuous. A bounded Sobolev sequence can converge weakly without converging strongly at the same derivative order. And derivatives in an integral sense ignore changes on sets of measure zero. All three facts are features of the function-space framework, not defects.

The reward is that we can now speak meaningfully about energy estimates, convergence, and boundary conditions for functions too rough for classical calculus. When a differential equation is solved by taking limits of approximations, Sobolev spaces are often the place where those limits can live and the equation can still be interpreted.

## A Differential Equation Without Second Derivatives: Weak Poisson Problems

Suppose a thin elastic sheet is fastened along its edge and pushed by a distributed load. Its equilibrium shape is often described by Poisson's equation: minus the Laplacian of the displacement equals the applied force. In ordinary calculus language, the Laplacian means adding the second derivatives in all spatial directions. But if the load is rough, why should the shape have classical second derivatives everywhere?

A weak formulation avoids demanding more differentiability than the physics supplies. It begins with an energy principle. A stretched sheet stores energy proportional to the square of its gradient: steep slopes cost energy. The applied load does work against the displacement. Equilibrium is the configuration that balances these effects, subject to the sheet remaining fixed at its boundary.

To derive the weak equation, multiply the classical Poisson equation by an arbitrary smooth test displacement that vanishes at the boundary, and integrate over the region. Integration by parts moves one derivative from the unknown displacement to the test function. The result says: the integral of the dot product of their gradients equals the integral of the force times the test function.

Notice what has changed. The unknown no longer needs two classical derivatives. It needs a weak first derivative with finite squared integral. That puts it in the Sobolev energy space H zero one, which incorporates the zero boundary condition. The test function is taken from the same space by density, so we can test against many more functions than the initial smooth probes.

In one dimension we can make the result explicit. On the interval from zero to one, hold the displacement at zero at both ends and apply a uniform unit load. The classical solution is one half times x times one minus x. Its graph is a parabola rising to one eighth at the midpoint. Differentiate once: the slope is one half minus x. The slope is square integrable, so the solution belongs to the energy space.

Test the weak equation with the solution itself. The left side is the integral of the squared slope. The right side is the integral of the load times the displacement. This is the energy identity. It says the work applied by the load equals the energy measured by the gradient in this normalization. The identity also gives control of the size of the solution in terms of the forcing.

Now let the forcing be an arbitrary square-integrable function rather than a constant. We may not have a formula for the solution. But a powerful theorem, Lax–Milgram, can prove there is a unique weak solution without solving the differential equation point by point.

Here is the idea. Define a bilinear form that takes two candidate functions and integrates the dot product of their gradients. This form is continuous: Cauchy–Schwarz bounds its absolute value by the product of the energy norms. It is coercive: when we insert the same function twice, we obtain the squared gradient norm, which controls the full H zero one norm through Poincaré's inequality. The forcing defines a bounded linear functional by integration against a test function. Lax–Milgram says there is exactly one function in the energy space whose pairing through the bilinear form matches that forcing functional for every test function.

The abstract theorem is not magic. On a Hilbert space, a continuous coercive bilinear form behaves like a stable invertible positive operator. It excludes directions along which the energy could vanish without the function itself vanishing. Once the boundary condition removes the constant-function ambiguity, the energy gives enough control to make the solution both unique and stable.

Consider what would happen if we removed the boundary condition and used a pure Neumann problem, fixing only the normal derivative at the boundary. Then adding any constant to a solution would produce another solution. The gradient energy cannot see constants. Uniqueness fails unless we impose an additional normalization such as zero mean, and the forcing must satisfy a compatibility condition. This resembles the Fredholm alternative: a kernel creates an obstruction to uniqueness and an orthogonality condition for solvability.

Finite-element methods are built directly from the weak formulation. Instead of trying to approximate second derivatives at every point, choose a finite-dimensional set of candidate displacement functions. Require the weak equation only for test functions in that finite-dimensional space. The resulting algebraic system uses integrals of gradients and load terms. When the energy form is coercive, the discrete problem is a stable approximation of the continuous one.

A weak solution is not necessarily a classical one. On a smooth domain with a smooth forcing, further regularity theorems can show the solution has more derivatives. On a domain with corners, with discontinuous coefficients, or with rough loading, that improvement may be limited. Existence in the energy space and regularity beyond it are two separate mathematical questions.

This is the principal lesson of weak PDE theory. We can formulate an equation in a way that reflects the actual energy estimates available. We can then prove existence, uniqueness, and stability before asking whether a twice-differentiable graph exists. The weak formulation is not a compromise made for computers. It is often the natural mathematical expression of the underlying balance law.

## Elliptic Regularity: Why Solutions Gain Derivatives

Imagine sending a rough signal through a device that smooths out its sharp corners. A mathematical version of that device is the inverse of a positive elliptic differential operator. Elliptic operators arise in equilibrium problems, electrostatics, and steady diffusion. Their defining feature is not that every coefficient is positive, but that their highest-order part controls changes in every spatial direction.

Start with the simplest one-dimensional equation on the entire line: one minus the second derivative applied to u equals a forcing f. Why include the one? Because minus the second derivative alone has issues near zero frequency. Adding the identity makes the operator invertible and gives a clean formula.

Take Fourier transforms. The second derivative becomes multiplication by minus frequency squared. So our equation becomes one plus frequency squared, multiplied by the Fourier transform of u, equals the Fourier transform of f. Solve for each frequency: divide by one plus frequency squared. High-frequency components are suppressed by approximately the inverse square of their frequency.

Now ask what happens if f merely has finite L two energy. Multiplying the transform of u by one plus frequency squared recovers the transform of f, which is square integrable. This means u belongs to the second-order Sobolev space H two. In this precise sense the solution gains two derivatives. We did not need to compute a classical second derivative at every point; we used an L two multiplier estimate.

The same idea works for the operator one minus the Laplacian in any Euclidean dimension. Its Fourier multiplier is one plus the squared length of the frequency vector. It controls two derivative orders in every direction. This is the model of ellipticity: the highest-order symbol does not vanish for a nonzero frequency vector.

Suppose instead we had an operator that differentiated only in the first spatial direction. Then frequencies that oscillate purely in the second direction would not be penalized. We could not conclude that the solution gains derivatives in every direction. Ellipticity is exactly what rules out that kind of blind spot.

For constant-coefficient equations on the whole space, Fourier multipliers make the reasoning nearly transparent. Real boundary-value problems are harder. Coefficients may vary with position, and the domain may have corners or a curved edge. We can no longer diagonalize the whole operator with one global Fourier transform. A standard strategy is local: freeze the coefficients near a point, compare with the constant-coefficient model, estimate the error, then combine the estimates with a partition of unity.

The regularity conclusion also depends on where we are. If the forcing is L two and the coefficients are sufficiently smooth and uniformly elliptic, we often obtain H two regularity on every compact subregion of the domain. But to obtain H two regularity all the way to the boundary, we need additional assumptions on the boundary and the boundary data. A re-entrant corner can produce a weak solution that is not globally H two even when the forcing is smooth.

There is a one-dimensional calculation that brings this difference into focus. On an interval with zero boundary values, solving minus u double prime equals a square-integrable forcing gives u double prime equal to minus the forcing almost everywhere. In one dimension, with the boundary conditions and basic regularity, this puts u in H two. In two dimensions with a sharply re-entrant corner, a harmonic function may vary like a fractional power of the distance from the corner. Its second derivatives may fail to be square integrable near that corner. Geometry enters the regularity story.

Elliptic regularity is also an engine for bootstrapping. Suppose the forcing is not just L two but has one weak derivative in L two. Under suitable coefficients and domain conditions, the solution may gain three derivative orders. If the forcing and coefficients are smooth and we stay in the interior, repeated estimates can lead to a smooth solution. A rough weak solution may turn out to be classical after all, but that conclusion is earned by a theorem rather than assumed at the start.

What happens with nonlinear equations? If a nonlinear expression of u serves as the forcing, we must know that expression belongs to the necessary function space. For example, a product may not be in L two merely because its two factors are in L two; the product is guaranteed only in L one by Cauchy–Schwarz. Sobolev embeddings and dimension determine when nonlinearities have enough integrability to permit bootstrapping. This is why higher-dimensional nonlinear PDEs can require far more delicate estimates than the elementary linear theory.

Elliptic regularity also explains why discretized elliptic problems can be well behaved after the right preconditioning. The inverse operator suppresses high frequencies, but its action on different scales is highly nonuniform. Multigrid methods exploit that scale structure, and finite-element error estimates quantify how well a discrete approximation captures the regularity that the true solution actually has.

The guiding question is always: which frequencies, directions, and regions does the operator control? On the full line, the answer may be read from a multiplier. In a bounded or variable-coefficient problem, it requires local estimates and careful boundary hypotheses. The general principle remains: an elliptic equation turns control of the forcing into control of higher derivatives of the solution.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Fourier Series, Convolution, and the Shape of Approximation

**Track:** Analysis from First Principles. **Background:** Hilbert spaces, trigonometric functions and Lebesgue integration. **Central question:** How does averaging isolate frequencies and approximate a function?

#### Mathematical companion (not spoken)

On \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), choose normalized Haar measure \(dm=dx/(2\pi)\). Fourier coefficients and convolution are
\[\widehat f(n)=\int_{\mathbb T}f(x)e^{-inx}\,dm(x),\qquad (f*g)(x)=\int_{\mathbb T}f(x-y)g(y)\,dm(y).\]
Then \(\widehat{f*g}(n)=\widehat f(n)\widehat g(n)\), and Parseval is \(\|f\|_{L^2(dm)}^2=\sum_{n\in\mathbb Z}|\widehat f(n)|^2\). Fourier partial sums converge in \(L^2\), not necessarily pointwise at every x.

The Fejér kernel \(F_N(x)=\frac1N|\sum_{k=0}^{N-1}e^{ikx}|^2\), \(N\ge1\), has \(F_N\ge0\), \(\int F_Ndm=1\), and Fourier multiplier \(\widehat F_N(n)=(1-|n|/N)_+\). For continuous periodic \(f\), \(F_N*f\to f\) uniformly; for \(1\le p<\infty\), convergence holds in \(L^p\).

For the heat equation \(u_t=\partial_x^2u\) on the circle, \(\widehat u(t,n)=e^{-tn^2}\widehat u_0(n)\). The kernel tends to the periodic delta distribution as \(t\downarrow0\), and \(u(t)\to u_0\) in \(L^2\) for \(u_0\in L^2\).

##### Exercises with answers

1. **Three frequencies.** Which Fourier frequencies occur in \(f(x)=\sin x+\tfrac12\sin3x\)? **Answer:** \(n=\pm1,\pm3\).
2. **Mean preservation.** If \(\int k\,dm=1\), why does convolution preserve the integral? **Answer:** Fubini and translation invariance give \(\int k*f\,dm=(\int k\,dm)(\int f\,dm)\).
3. **Heat filtering.** Compare frequencies two and five after time t. **Answer:** Multipliers are \(e^{-4t}\) and \(e^{-25t}\), so frequency five decays faster.

##### Reading and source notes

- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)

### The Fourier Transform: Plancherel, Derivatives, and the Heat Equation

**Track:** Analysis from First Principles. **Background:** Lebesgue integration, L-two Hilbert geometry, and Fourier series. **Central question:** What replaces a list of integer frequencies for a signal that does not repeat?

#### Mathematical companion (not spoken)

On \(\mathbb R\), for Schwartz \(f\), set \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}\,dx\) and \(f(x)=(2\pi)^{-1}\int\widehat f(\xi)e^{ix\xi}\,d\xi\). Then
\[\widehat{f'}(\xi)=i\xi\widehat f(\xi),\quad\widehat{f''}(\xi)=-\xi^2\widehat f(\xi),\quad\widehat{f*g}=\widehat f\,\widehat g.\]
Plancherel extends this to a unitary \(\mathcal F:L^2(dx)\to L^2(d\xi/(2\pi))\):
\[\int |f(x)|^2dx=\frac1{2\pi}\int|\widehat f(\xi)|^2d\xi.\]

For \(u_t=u_{xx}\) with suitable L2 initial data, \(\widehat u(t,\xi)=e^{-t\xi^2}\widehat u_0(\xi)\). Its inverse is convolution with \(G_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)}\), \(t>0\). For Schwartz \(f(x)=e^{-x^2/(2\sigma^2)}\), \(\widehat f(\xi)=\sqrt{2\pi}\sigma e^{-\sigma^2\xi^2/2}\).

The operator \(-\partial_x^2\) is the multiplier \(\xi^2\) with domain \(\{f\in L^2:\xi^2\widehat f\in L^2\}\), equal to \(H^2(\mathbb R)\) under standard conventions.

##### Exercises with answers

1. **Derivative.** What Fourier multiplier corresponds to \(-u''\)? **Answer:** \(\xi^2\).
2. **Widening.** What happens to the Fourier transform of a Gaussian when its spatial width \(\sigma\) decreases? **Answer:** Its characteristic frequency width grows like \(1/\sigma\).
3. **Heat norm.** Why does heat evolution not increase L2 norm? **Answer:** \(|e^{-t\xi^2}|\le1\) and Plancherel.

##### Reading and source notes

- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)

### Frequency Localization: Why Derivatives Measure High Frequencies

**Track:** Analysis from First Principles. **Background:** Fourier transform, convolution, Hilbert-space norms. **Central question:** How can a frequency filter reveal regularity and scale?

#### Mathematical companion (not spoken)

For \(f\in L^2(\mathbb R)\), a bounded measurable Fourier multiplier \(m\in L^\infty\) defines \(T_mf=\mathcal F^{-1}(m\widehat f)\), with \(\|T_m\|_{L^2\to L^2}\le\|m\|_\infty\). The actual operator norm is the essential supremum of \(|m|\) with respect to Lebesgue measure.

If \(\widehat f\) vanishes outside \(\{\xi:N\le|\xi|\le2N\}\), \(N>0\), then Plancherel yields
\[N\|f\|_2\le\|f'\|_2\le2N\|f\|_2.\]

Define \(H^s(\mathbb R)=\{f\in\mathcal S':(1+\xi^2)^{s/2}\widehat f\in L^2(d\xi)\}\), with the usual Fourier–Plancherel normalization, and norm \(\|f\|_{H^s}^2=(2\pi)^{-1}\int(1+\xi^2)^s|\widehat f(\xi)|^2d\xi\).

For \((I-\partial_x^2)u=f\) on \(\mathbb R\), \(\widehat u=(1+\xi^2)^{-1}\widehat f\). Therefore \(\|u\|_{H^2}=\|f\|_2\) with this particular Bessel-potential norm. A bound for the operator on \(L^p\), \(p\ne2\), requires more than \(m\in L^\infty\).

##### Exercises with answers

1. **Band derivative.** If all frequencies lie between 10 and 20 in magnitude, bound \(\|f'\|_2/\|f\|_2\). **Answer:** Between 10 and 20 for nonzero f.
2. **Elliptic gain.** What factor does \((I-\partial_x^2)^{-1}\) give to frequency 100? **Answer:** \(1/(1+10000)\).
3. **Wrong norm.** Why can we not directly transfer the L2 multiplier estimate to every Lp space? **Answer:** Plancherel is an L2 isometry; the assertion is false for arbitrary bounded multipliers when \(p\ne2\).

##### Reading and source notes

- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)

### Distributions: Making Sense of Delta Functions and Rough Derivatives

**Track:** Analysis from First Principles. **Background:** Integrals, smooth test functions and integration by parts. **Central question:** How can a function have a derivative even where it has a corner or a jump?

#### Mathematical companion (not spoken)

The test-function space \(\mathcal D(\Omega)=C_c^\infty(\Omega)\) has its usual locally convex topology. A distribution \(T\in\mathcal D'(\Omega)\) is a continuous linear functional. Each \(f\in L^1_{\mathrm{loc}}(\Omega)\) gives \(T_f(\varphi)=\int_\Omega f\varphi\).

For a multiindex \(\alpha\), \(\langle\partial^\alpha T,\varphi\rangle=(-1)^{|\alpha|}\langle T,\partial^\alpha\varphi\rangle\). On \(\mathbb R\), \(\langle\delta_0,\varphi\rangle=\varphi(0)\), \(H(x)=\mathbf1_{(0,\infty)}(x)\), and
\[H'=\delta_0,\qquad (|x|)'=\operatorname{sgn}x,\qquad (|x|)''=2\delta_0\]
in \(\mathcal D'(\mathbb R)\).

For Schwartz-tempered distributions \(\mathcal S'\), Fourier transform extends by duality. With \(\widehat f(\xi)=\int f(x)e^{-ix\xi}\,dx\), one has \(\widehat{\delta_0}=1\) and \(\widehat{1}=2\pi\delta_0\), where identities are distributional.

**Caution:** Arbitrary products \(ST\) of distributions are not defined in ordinary distribution theory. Multiplication by \(a\in C^\infty\) is defined by \(\langle aT,\varphi\rangle=\langle T,a\varphi\rangle\).

##### Exercises with answers

1. **Point force.** Compute \(\langle 3\delta_2,\varphi\rangle\). **Answer:** \(3\varphi(2)\).
2. **Jump of size c.** Find the distributional derivative of \(cH(x-a)\). **Answer:** \(c\delta_a\).
3. **Polynomial.** What is the distributional derivative of \(x^2\)? **Answer:** The regular distribution associated with \(2x\), because integration by parts holds.

##### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)

### Mollifiers and Weak Derivatives: Smooth Approximations to Rough Functions

**Track:** Analysis from First Principles. **Background:** Convolution, distributions and L-p spaces. **Central question:** How can we justify calculus by approximating a rough function with smooth ones?

#### Mathematical companion (not spoken)

Choose \(\rho\in C_c^\infty(\mathbb R^d)\), \(\rho\ge0\), \(\int\rho=1\), and \(\rho_\varepsilon(x)=\varepsilon^{-d}\rho(x/\varepsilon)\). For \(f\in L^p(\mathbb R^d)\), \(1\le p<\infty\),
\[\rho_\varepsilon*f\in C^\infty(\mathbb R^d),\qquad\rho_\varepsilon*f\to f\text{ in }L^p.\]
For \(f\in W^{k,p}(\mathbb R^d)\), \(D^\alpha(\rho_\varepsilon*f)=\rho_\varepsilon*(D^\alpha f)\) for \(|\alpha|\le k\), and \(\rho_\varepsilon*f\to f\) in \(W^{k,p}\).

A weak derivative \(g=\partial_jf\) on \(\Omega\) means \(\int_\Omega f\partial_j\varphi=-\int_\Omega g\varphi\) for all \(\varphi\in C_c^\infty(\Omega)\). For \(f=|x|\) on \((-1,1)\), \(f'=\operatorname{sgn}x\in L^p\) for finite p, but \(f''=2\delta_0\notin L^p\). For \(H\), \(H'=\delta_0\), so \(H\notin W^{1,p}((-1,1))\) for \(p\ge1\).

On a bounded Lipschitz domain, the trace map \(\operatorname{Tr}:W^{1,p}(\Omega)\to\) an appropriate boundary trace space is bounded for \(1\le p<\infty\), and \(W^{1,p}_0(\Omega)\) is its kernel under usual hypotheses. Interior mollification does not by itself preserve boundary conditions.

##### Exercises with answers

1. **Mass of mollifier.** Verify \(\int \rho_\varepsilon dx=1\). **Answer:** Substitute \(y=x/\varepsilon\).
2. **Corner or jump?** Which of \(|x|\) and \(H(x)\) belongs to \(W^{1,2}((-1,1))\)? **Answer:** Only \(|x|\).
3. **Derivative transfer.** Explain \(D(f*\rho_\varepsilon)=f*(D\rho_\varepsilon)\). **Answer:** Differentiate the smooth kernel under the integral; for weakly differentiable f it also equals \((Df)*\rho_\varepsilon\).

##### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [John K. Hunter, Measure Theory notes](https://www.math.ucdavis.edu/~hunter/m206/intro_measure_notes.pdf)

### Sobolev Spaces: Measuring Smoothness Without Pointwise Derivatives

**Track:** Analysis from First Principles. **Background:** L-p spaces, weak derivatives and basic Fourier multipliers. **Central question:** What does a bound on weak derivatives actually tell us about a function?

#### Mathematical companion (not spoken)

On \(\Omega\subset\mathbb R^d\), \(W^{1,p}(\Omega)=\{u\in L^p(\Omega):D_ju\in L^p(\Omega)\}\), with derivatives distributional, \(1\le p\le\infty\). Set \(H^1=W^{1,2}\). If \(u\in H^1(a,b)\), then u has an absolutely continuous representative and
\[|u(x)-u(y)|\le |x-y|^{1/2}\|u'\|_{L^2(a,b)}.\]

For bounded Lipschitz \(\Omega\subset\mathbb R^d\), \(1\le p<d\), Sobolev embedding gives \(W^{1,p}(\Omega)\hookrightarrow L^{p^*}(\Omega)\), \(p^*=dp/(d-p)\). For \(p>d\), Morrey yields a Hölder-continuous representative of exponent \(1-d/p\) (with the usual care at boundary and endpoint). No comparable general \(W^{1,d}\to C^0\) embedding holds.

For bounded Lipschitz \(\Omega\), \(H^1_0(\Omega)\hookrightarrow L^2(\Omega)\) is compact. Poincaré: \(\|u\|_2\le C_\Omega\|\nabla u\|_2\) for \(u\in H^1_0(\Omega)\). On \(\mathbb R^d\), the embedding \(H^1\hookrightarrow L^2\) is not compact due to translations; \(u_n(x)=u(x-n e_1)\) is bounded in H1 but has no strongly convergent L2 subsequence for nonzero compactly supported u.

##### Exercises with answers

1. **One-dimensional bound.** If \(\|u'\|_2\le3\), bound \(|u(1/4)-u(0)|\) on an interval containing both. **Answer:** At most \(3/2\).
2. **High frequencies.** For \(u_n(x)=\sin(nx)\) on \((0,2\pi)\), how does \(\|u_n'\|_2\) scale? **Answer:** Like n.
3. **Noncompactness.** Why does translation obstruct compact embedding on the full line? **Answer:** Translated pulses retain their L2 norm and eventually have disjoint supports, so cannot have a strongly Cauchy subsequence.

##### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)

### A Differential Equation Without Second Derivatives: Weak Poisson Problems

**Track:** Analysis from First Principles. **Background:** H-one Sobolev spaces, integration by parts, bounded linear functionals. **Central question:** How can we prove existence and uniqueness of a boundary-value solution that may not be twice differentiable?

#### Mathematical companion (not spoken)

Let \(\Omega\subset\mathbb R^d\) be bounded Lipschitz, \(f\in L^2(\Omega)\). Find \(u\in H^1_0(\Omega)\) with
\[a(u,v)=F(v)\quad\forall v\in H^1_0(\Omega),\qquad a(u,v)=\int_\Omega\nabla u\cdot\nabla v,\quad F(v)=\int_\Omega fv.\]
Cauchy–Schwarz and Poincaré show \(|a(u,v)|\le\|u\|_V\|v\|_V\), \(a(v,v)=\|v\|_V^2\), and \(|F(v)|\le C_P\|f\|_2\|v\|_V\), with \(\|v\|_V=\|\nabla v\|_2\). The Lax–Milgram theorem yields a unique solution and \(\|\nabla u\|_2\le C_P\|f\|_2\).

For \(\Omega=(0,1)\), \(f=1\), \(u=x(1-x)/2\) satisfies \(-u''=1\), \(u(0)=u(1)=0\). Its energy identity is
\[\int_0^1|u'|^2dx=\int_0^1u\,dx=\frac1{12}.\]

If the Neumann condition is instead prescribed with zero flux, \(-\Delta u=f\) is solvable only if \(\int_\Omega f=0\) and u is unique only modulo constants on a connected domain.

##### Exercises with answers

1. **Parabola height.** What is the maximum of \(u(x)=x(1-x)/2\) on \([0,1]\)? **Answer:** \(1/8\) at \(x=1/2\).
2. **Energy.** Why does \(a(u,u)=0\) imply \(u=0\) for \(u\in H^1_0\)? **Answer:** The gradient vanishes a.e.; Poincaré then forces zero L2 norm.
3. **Neumann source.** Can \(-u''=1\) with \(u'(0)=u'(1)=0\) have a solution? **Answer:** No: integrating gives \(-u'(1)+u'(0)=1\), a contradiction.

##### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)

### Elliptic Regularity: Why Solutions Gain Derivatives

**Track:** Analysis from First Principles. **Background:** Fourier transforms, Sobolev norms, weak Poisson equations. **Central question:** When does solving a PDE produce a smoother function than its forcing?

#### Mathematical companion (not spoken)

With Fourier convention \(\widehat{\partial_j u}=i\xi_j\widehat u\), the Bessel-potential operator \(I-\Delta\) has symbol \(1+|\xi|^2\). For any \(s\in\mathbb R\),
\[(I-\Delta):H^{s+2}(\mathbb R^d)\longrightarrow H^s(\mathbb R^d)\]
is an isometric isomorphism under the Bessel-potential norm, because \(\widehat u=(1+|\xi|^2)^{-1}\widehat f\).

Uniform ellipticity for divergence-form \(-\partial_i(a^{ij}(x)\partial_j u)\) means \(\sum_{ij}a^{ij}(x)\xi_i\xi_j\ge\lambda|\xi|^2\) for \(\lambda>0\) a.e. and real \(\xi\) (symmetric part relevant). For \(a^{ij}\) sufficiently regular (e.g. Lipschitz locally), an H1 weak solution to an elliptic equation with \(f\in L^2\) enjoys interior H2 estimates. Global H2 requires additional boundary regularity and compatible boundary conditions; a Lipschitz domain alone does not suffice.

**Counterexample to non-elliptic smoothing.** On \(\mathbb R^2\), the operator \(I-\partial_x^2\) has symbol \(1+\xi_x^2\), which fails to control large \(|\xi_y|\). A forcing oscillating rapidly in y can remain equally rough in that direction after inversion.

##### Exercises with answers

1. **Frequency damping.** At frequency \(|\xi|=10\), what is the multiplier for \((I-\Delta)^{-1}\)? **Answer:** \(1/101\).
2. **Second derivative gain.** If \(f\in L^2(\mathbb R)\) and \((I-\partial_x^2)u=f\), which Sobolev space contains u? **Answer:** \(H^2(\mathbb R)\).
3. **Boundary qualification.** Does interior H2 imply global H2 on a polygon with re-entrant corners? **Answer:** No; corner singularities can prevent global H2 regularity.

##### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)
