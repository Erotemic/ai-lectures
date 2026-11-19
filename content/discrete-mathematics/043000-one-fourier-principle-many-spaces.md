# One Fourier Principle in Several Different Mathematical Worlds

**Track:** Discrete Mathematics and Combinatorics  
**Lecture:** 043000  
**Preparation:** Sine and cosine as rotations, complex numbers, elementary sums and probabilities; linear algebra helps with spectral language.  
**Companion:** Fourier transform on a cyclic group, convolution, characteristic functions, and random walks.

<!-- BEGIN SPOKEN LECTURE -->

A vibrating string is made of many notes. A blurred picture can be studied through spatial frequencies. A random walk around a circular network has patterns that decay at different rates. Adding independent random numbers changes their probability distributions, yet there is an algebraic way to turn that addition into multiplication. And in number theory, we can study congruence classes using waves whose angles are rational fractions of a complete turn.

Those may sound like unrelated tricks. The common mechanism is that a **translation** acts very simply on certain special functions. Those functions are Fourier modes. Once we describe a problem in those modes, some operations that were complicated in the original description become multiplication by numbers. We will see this first in an exact, finite setting, where there is no need to worry about infinite series or integration. Then we will identify what survives when the underlying space changes.

Imagine four positions arranged on a ring, numbered zero, one, two, and three. After three comes zero again. We can describe a function on this ring by four numbers, one attached to each position. For example, one, zero, zero, zero represents a unit of mass concentrated at position zero. Shifting the function one step around the ring moves the mass from zero to one. This is a simple operation, but its matrix in the position basis rearranges coordinates rather than multiplying them separately.

We need patterns that retain their shape when shifted, changing only by a constant factor. The constant pattern, one at every position, is one such pattern: shifting does nothing. A second pattern alternates plus one, minus one, plus one, minus one: shifting reverses its sign. The two remaining patterns are most naturally written using complex numbers, rotating through successive quarter-turns in the complex plane. The four patterns are called the **characters** of the four-position cyclic group.

A character here is a function whose value at a sum of positions equals the product of its values at the two positions, with positions added modulo four. That is a precise algebraic statement. For a ring of N positions, the basic characters assign to position x a complex number whose angle is two pi times k times x divided by N, where k is a whole-number frequency index. One may use Euler's formula to write them as complex exponentials. Their magnitudes are one, so they describe pure rotations in phase, not growing or shrinking amplitudes.

Why do these modes help? Shift a character by one position. Every value receives the same phase factor determined by k. The shape of the character is unchanged. We say it is an **eigenfunction of translation**. A general function on the ring is a sum of these characters with suitable coefficients, just as a vector is a sum of basis vectors. The coefficients are its discrete Fourier transform. This is a change of coordinates, chosen not because the original coordinates were wrong but because the translation operation is simpler in the new coordinates.

Let's calculate the most concentrated possible input. Put one unit of mass at position zero and zero elsewhere. Its discrete Fourier transform has the same coefficient, one, at each of the four frequencies, under the convention in which the forward transform does not include a factor of one over four. A single spike uses **all** frequencies. If we instead spread the same mass evenly over all four positions, every nonzero frequency coefficient vanishes; only the constant mode remains. Localization in position and concentration in frequency are different properties.

Now imagine combining two patterns by a rule called **convolution**. To compute the output at a position x, shift one pattern against another, multiply corresponding values and sum over the ring. For probability distributions, convolution gives the distribution of the sum of two **independent** random positions modulo four. The second pattern describes one random step; the first describes the current location. Convolving them produces the next location distribution.

Convolution looks like a collection of intertwined sums in position space. In Fourier coordinates it becomes pointwise multiplication: the Fourier coefficient of the convolution equals the product of the Fourier coefficients. This is the central computational payoff. A complicated accumulation of shifted contributions becomes a separate one-number calculation for each frequency. It is the same reason that convolutional filters can be studied with transfer functions, that Fourier transforms help solve constant-coefficient differential equations, and that probability characteristic functions are useful for sums of independent variables.

Let's work through an actual random walk. Start with a particle at position zero on our four-position ring. At each tick it moves one step clockwise or one step counterclockwise, each with probability one half. The constant Fourier mode stays unchanged. The two quarter-turn modes acquire a factor of zero in one step: their contributions disappear immediately. But the alternating mode acquires a factor of negative one. After one step the particle can be at positions one or three. After another it returns to the even positions. It never settles into a uniform distribution over all four positions at a fixed large time; parity keeps alternating.

That is an instructive counterexample. A finite connected random walk need not converge to the uniform distribution at each time. Periodicity matters. Its alternating eigenmode has magnitude one, so no decay occurs in that direction. The Fourier calculation identifies the obstruction exactly instead of merely showing us a numerical simulation with persistent oscillation.

There is a standard repair. Make the walk **lazy**: at each tick, with probability one half it stays where it is; with probability one quarter it moves clockwise and with probability one quarter counterclockwise. The alternating mode now has multiplier zero, the quarter-turn modes have multiplier one half, and the constant mode still has multiplier one. Every nonconstant mode shrinks, while the constant one persists. Thus the distribution approaches uniformity. This is an example of spectral mixing: convergence is governed by the magnitudes of eigenvalues other than the stationary one.

Notice how close this is to heat diffusion. The heat equation smooths out spatial variations while preserving the average temperature on a periodic insulated domain. In a Fourier expansion, the constant mode remains and the higher-frequency modes decay at rates related to their squared frequencies. The random walk on the ring has a discrete version of this smoothing. The exact multipliers differ, but the architecture is shared: decompose into modes, evolve each mode separately, and recombine.

There is a difference worth keeping. A graph Laplacian on an arbitrary graph also has eigenvectors, and those eigenvectors can be used as graph Fourier modes. But an arbitrary graph does not have the same group structure as a cyclic ring, so its eigenvectors need not be characters of a translation group. **Spectral decomposition** is the broader idea; harmonic characters arise when the underlying symmetries make translation operators commute in the right way.

What happens on the ordinary number line? Instead of a finite ring, we have a continuum of positions. Translations by any real amount still have special eigenfunctions: complex exponentials whose phase increases linearly with position. Rather than a finite sum of Fourier coefficients, we describe many integrable functions with a continuous Fourier transform, defined by an integral against those exponentials. The exact inversion and convergence statements require appropriate hypotheses. We cannot simply carry every finite-dimensional identity into an infinite-dimensional setting without checking those hypotheses.

For probability, a closely related object is the **characteristic function** of a real-valued random variable. At frequency t, take the expected value of the complex exponential of i times t times the variable. If independent random variables X and Y are added, their characteristic functions multiply. This is the continuous analogue of the finite-ring convolution law. Independence is essential: without it, the expectation of the product need not factor into a product of expectations.

A characteristic function is useful even when a random variable has no probability density. It describes the distribution through expectations rather than through a density formula. With suitable moment conditions, derivatives of the characteristic function at zero recover mean and higher moments. In probability limit theorems, convergence of characteristic functions under the right conditions lets us understand convergence in distribution. The Fourier idea is not just a method for solving an integral; it is a way of representing probability laws.

Number theory supplies another variation. A function on residue classes modulo N can be decomposed into additive characters, exactly the finite cyclic Fourier modes. Multiplicative characters, such as Dirichlet characters, arise instead from the group of invertible residues under multiplication. They also obey character orthogonality, but the operation being diagonalized is different. We should not equate additive and multiplicative characters merely because both use complex values and orthogonality sums.

At this point the common pattern is visible. Identify the operation that matters: shifting a signal, adding independent random variables, evolving diffusion, or combining residue classes. Find functions that respond to that operation by scalar multiplication. Expand complicated inputs in those functions. Compute the effect mode by mode, and finally reconstruct the answer. In the right coordinates, interaction becomes multiplication.

Fourier analysis is not one formula copied unchanged into every subject. Finite cyclic groups use finite sums. The line uses integrals and assumptions about function spaces. Arbitrary graphs use eigenvectors of graph operators. Nonabelian groups generally require matrix-valued representations instead of only scalar characters. The details matter precisely because the principle is so widely applicable.

When you encounter a new Fourier transform, ask: what is the underlying space, what is its notion of translation or symmetry, what are its characters or eigenfunctions, how is the transform normalized, and which operation becomes multiplication? Those questions turn a catalog of Fourier tricks into a connected theory, spanning algebra, probability, signal processing, and differential equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(G=\mathbb Z/N\mathbb Z\). For \(k,x\in G\), characters are \(\chi_k(x)=e^{2\pi i kx/N}\). Under the convention
\[
\widehat f(k)=\sum_{x=0}^{N-1} f(x)e^{-2\pi i kx/N},\qquad f(x)=\frac1N\sum_{k=0}^{N-1}\widehat f(k)e^{2\pi i kx/N},
\]
characters diagonalize translations, and with convolution \((f*g)(x)=\sum_y f(y)g(x-y)\), one has \(\widehat{f*g}(k)=\widehat f(k)\widehat g(k)\). Orthogonality: \(\sum_x\chi_k(x)\overline{\chi_\ell(x)}=N\delta_{k\ell}\).

**Four-cycle random walk.** With \(P f(x)=\tfrac12(f(x-1)+f(x+1))\), each \(\chi_k\) is an eigenfunction and eigenvalue is \(\lambda_k=\cos(2\pi k/4)\), i.e. \(1,0,-1,0\) for \(k=0,1,2,3\). The \(-1\) mode preserves its magnitude and reverses sign every step. For lazy walk \(P_L=(I+P)/2\), eigenvalues become \(1,1/2,0,1/2\). For any starting probability vector, nonconstant modes decay, giving convergence to uniform distribution.

**Continuum:** for an integrable density p on \(\mathbb R\), the characteristic function is \(\varphi_X(t)=\int_\mathbb R e^{itx}p(x)\,dx\). For arbitrary real random variables, define \(\varphi_X(t)=\mathbb E[e^{itX}]\). If X and Y are independent, \(\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)\). Depending on transform sign convention, the characteristic function is a Fourier transform evaluated at a negative frequency. On an arbitrary finite graph, Laplacian eigenvectors form a spectral basis when the operator is real symmetric, but they are not necessarily group characters.

### Exercises and solutions

1. **Delta spike.** For \(f=(1,0,0,0)\) on \(\mathbb Z/4\mathbb Z\), compute \(\widehat f(k)\). **Solution:** every coefficient is one.
2. **Constant function.** For \(g=(1,1,1,1)\), what are its Fourier coefficients? **Solution:** \(\widehat g(0)=4\) and the other three vanish.
3. **Alternating mode.** Why does the non-lazy nearest-neighbor walk on a four-cycle fail to mix at fixed times? **Solution:** it has an eigenmode of eigenvalue \(-1\), so the parity component oscillates rather than decays.
4. **Independence.** Does \(\varphi_{X+Y}=\varphi_X\varphi_Y\) always hold? **Solution:** no, not for dependent X and Y in general. It holds under independence.
5. **Normalization.** Why is there a factor of \(1/N\) in the inverse transform? **Solution:** because the chosen forward transform is an unnormalized sum; character orthogonality sums to N on matching frequencies.

### Reading and attribution

- MIT OpenCourseWare, *Mathematics for Computer Science* (2015), finite groups, convolution and discrete Fourier themes: https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/.
- MIT OpenCourseWare, *Information Theory* (2016), information measures and characteristic-function connections: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- Terence Tao, *Lecture Notes 9 for 247B: Fourier analysis on finite abelian groups*: https://www.math.ucla.edu/~tao/247b.1.07w/notes9.pdf.
- MIT OpenCourseWare, 6.003 *Signals and Systems*, Fourier and convolution lectures: https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/lecture-notes/.
- The explicit lazy four-cycle random walk and comparisons among transformation settings are original worked exposition.
