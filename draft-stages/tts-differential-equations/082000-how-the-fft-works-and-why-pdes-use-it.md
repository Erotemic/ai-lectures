# How the FFT Works and Why PDEs Use It: Fast Transforms from First Principles

<!-- BEGIN SPOKEN LECTURE -->

# How the FFT Works and Why PDEs Use It

We can now transform a finite array into frequency coefficients and back again. For four samples the arithmetic is manageable. But what if the instrument measures a million samples, or a numerical PDE solver contains a million grid values? Applying the definition of the discrete Fourier transform separately for every output frequency would demand roughly a million times a million contributions. That is a formidable amount of work if the transform must be repeated at every time step.

The fast Fourier transform, usually called the FFT, changes the cost. It does not define a new kind of spectrum. It computes the same discrete Fourier transform by reorganizing the arithmetic so that calculations are reused. For many common transform lengths the work grows like N times the logarithm of N, rather than N squared. The essential idea is so simple that we can derive it from even-numbered and odd-numbered samples.

We will first build that decomposition by hand. Then we will use a tiny numerical heat equation to show why fast transforms matter beyond audio and pictures. The same Fourier basis that analyzes measured signals also separates the modes of a periodic spatial difference operator.

## The redundant work hidden in a Fourier sum

Recall the forward discrete transform. For each frequency index k, multiply every sample by a complex rotation and sum. There are N samples and N output coefficients. If we compute the rotations and products independently, the direct method uses on the order of N squared operations. That is a faithful implementation of the definition, but it ignores the repeating structure of the complex rotations.

Suppose N is even. Separate the samples into those at even positions and those at odd positions. The even samples are the original samples at indices zero, two, four, and so on. The odd samples are at indices one, three, five, and so on. Each group has N divided by two entries.

When we substitute an even index into the transform's complex exponential, the phase becomes exactly the phase that appears in an N-over-two-point discrete transform. When we substitute an odd index, the phase splits into a factor that depends only on the output frequency k and the same smaller transform phase. Thus, the full N-point answer can be built from the transforms of the even and odd subsequences, plus one extra complex multiplication and addition for each needed combination.

The extra frequency-dependent factor is called a twiddle factor. The name is less important than its role. It is one complex rotation that aligns the odd contribution with the even contribution. We do not calculate the entire original sum again. We combine two shorter sums already computed.

There is an even better symmetry. In the first half of the output array, a coefficient is the even-transform coefficient plus the rotated odd-transform coefficient. In the second half, the corresponding coefficient is the even one minus that same rotated odd term. We obtain two outputs using almost the same intermediate quantities. The addition-and-subtraction pattern is commonly called a butterfly, because its dataflow diagram has two crossing paths.

## A four-point FFT by hand

Take the four samples one, two, three, four. The even-position subsequence is one, three. The odd-position subsequence is two, four. A two-point transform is particularly easy: it produces the sum of its entries and their difference. So the even subsequence transforms to four and negative two. The odd subsequence transforms to six and negative two.

Now combine them. For frequency index zero the twiddle factor is one. Add four and six to obtain ten. Subtract the same values to get negative two at index two. For index one the twiddle factor is a quarter-turn in the negative complex direction, or negative i. Multiplying negative two by negative i gives positive two i. Add this to the even coefficient negative two and we obtain negative two plus two i. The corresponding second-half output is negative two minus two i.

The complete four-point transform is ten, negative two plus two i, negative two, and negative two minus two i. You can check it against the original DFT definition. The FFT has produced exactly the same coefficients, not a faster approximation to different coefficients.

This also explains the sign conventions. The forward transform rotates with negative angles. The inverse transform uses positive angles and divides by N in our convention. Reversing a sign in the butterfly changes the answer. An implementation should be checked against a tiny array whose transform we can calculate independently.

## From four to a million

Suppose N is a power of two. After splitting an N-point transform into two half-size transforms, split each half again. Continue until every smallest piece has one entry. A one-point transform needs no work. Combining the pieces costs an amount proportional to N at each level of the decomposition, and there are logarithm base two of N levels. This gives the familiar N log N growth.

For a million or so samples, the logarithm base two is only around twenty. The conceptual difference is between a number of elementary operations scaling like a million squared and one scaling like a million times twenty, though the exact cost depends on the implementation, architecture, and transform shape. The FFT is therefore a major algorithmic improvement even though it does not change the mathematical transform.

Our even-odd derivation is a radix-two method, meaning it repeatedly factors a size into factors of two. It is convenient for understanding the algorithm, not a rule that FFTs require powers of two. Practical libraries use mixed-radix decompositions, specialized transforms, and algorithms for difficult lengths. Selecting the transform length can affect performance, but the ability to compute a valid discrete Fourier transform is not restricted to powers of two.

We should also not equate faster arithmetic with perfect physical accuracy. FFT routines use floating-point operations, so computed values may differ slightly from exact results. The FFT has the same aliasing and finite-record interpretation as the DFT it computes. It cannot identify a high frequency that the sample rate has folded into a low one, and it cannot make a one-second recording contain four seconds of observations.

## A useful connection to convolution

In the frequency representation, circular convolution becomes coefficient-by-coefficient multiplication. To convolve two periodic arrays, we can transform both, multiply their Fourier coefficients, and apply the inverse transform. With FFTs the operation can be efficient for long arrays, although for very short kernels a direct calculation may still be cheaper.

The word periodic is crucial. The transform performs circular convolution unless we pad the arrays enough to prevent wraparound. If we want ordinary linear convolution of an array of length L with one of length M, padding to at least L plus M minus one positions avoids overlap between the physical output and its periodic copies. The FFT is an accelerator for a chosen operation. It does not decide whether we meant linear or circular convolution.

The same principle underlies fast filtering. A frequency response multiplies each Fourier mode by a chosen factor. We can transform a signal, multiply by the factors, and reconstruct the filtered signal. But a sharp cutoff in frequency may create ringing in time, and a filter on a finite periodic array may have effects near the endpoints. We still need to understand the mathematical operation that we are accelerating.

## Why a spatial grid likes Fourier modes

Now consider a ring of equally spaced points, with temperature stored at each point. Heat flows between neighboring points. The simplest periodic finite-difference model says the rate of temperature change at a point is proportional to the temperature on its left, minus twice its own temperature, plus the temperature on its right. This is the discrete version of the second spatial derivative.

In our earlier method-of-lines lectures, this produced a system of ordinary differential equations. The unknown is an entire vector of grid temperatures. A computer can evolve that vector directly. But on a periodic, equally spaced grid, something special happens: a discrete Fourier mode is an eigenvector of this second-difference operator.

Why? A complex Fourier mode changes by the same fixed rotation every time we move one grid cell. Its left neighbor is the current value multiplied by the opposite rotation, and its right neighbor is multiplied by the forward rotation. Add the two and subtract twice the center. The result is the original mode multiplied by one number. The spatial coupling has become multiplication by a scalar eigenvalue.

For the zero-frequency mode that eigenvalue is zero. A constant temperature has no gradient and remains constant. For every other mode the eigenvalue is negative. Heat makes those modes decay, and the highly oscillatory modes tend to decay faster. This is the grid version of the continuous Fourier-transform solution of the heat equation, where the decay rate depends on the square of spatial frequency.

The statement depends on the geometry and boundary conditions. On a periodic grid, the ordinary complex DFT basis exactly diagonalizes the standard constant-coefficient second-difference matrix. With fixed zero-temperature endpoints, sine modes are more natural. With variable coefficients or irregular geometry, plain Fourier modes generally do not diagonalize the operator. We must not use a periodic FFT and silently claim it solves a different boundary-value problem.

## A four-cell heat problem with no matrix inversion

Let's compute one example completely. Place four equally spaced temperature values around a ring, one unit apart. Take a diffusion coefficient of one in compatible units. At time zero, let the first cell have temperature one and the other three have temperature zero. The initial vector is one, zero, zero, zero. Its four-point DFT has coefficient one at every frequency because the only nonzero sample is at index zero.

The four Fourier modes of the periodic second-difference operator have decay rates zero, negative two, negative four, and negative two. Thus, at time t their coefficients are one, e to the negative two t, e to the negative four t, and e to the negative two t. We have solved four independent scalar differential equations, one for each mode.

Apply the inverse DFT. The temperature at the initially warm cell is one quarter times the sum of one, twice e to the negative two t, and e to the negative four t. The cell opposite it has one quarter times one minus twice e to the negative two t plus e to the negative four t. Each of the two neighboring cells has one quarter times one minus e to the negative four t.

Check time zero. The first expression becomes one, and the others become zero. Check very late times. Every exponential decays and all four cells approach one quarter. The sum of the four temperatures remains one throughout, expressing conservation of total heat in this simplified model. All those facts can be read directly from the Fourier modes: the constant mode is preserved, while every nonconstant mode decays.

We did not have to solve a coupled four-by-four system at every instant. We changed coordinates once, evolved four scalar modes, and changed back. On a large periodic grid, an FFT makes the coordinate changes efficient. Similar reasoning supports spectral methods and fast solvers for some constant-coefficient PDEs.

## A stability condition reappears

Suppose instead of evolving these modes exactly, we use forward Euler with time step h sub t. A mode with decay rate lambda is multiplied after each step by one plus h sub t times lambda. To avoid growing oscillations, the magnitude of that factor must not exceed one for each mode. The fastest-decaying grid mode is therefore often the one that restricts an explicit time step.

For the standard one-dimensional periodic second-difference operator with even N, the most negative eigenvalue is negative four divided by the spatial step squared. Multiplying by the diffusion coefficient and applying the Euler stability condition gives the familiar limit: the diffusion coefficient times the time step divided by the spatial step squared must be no greater than one half. We encountered this condition when working directly with grid update coefficients. Fourier modes give a second derivation and explain it as a statement about the worst eigenmode.

The transform has not abolished numerical stability restrictions. It has made them visible as independent scalar inequalities. The same idea extends to stability analysis of linear periodic discretizations and to spectral filtering, although nonperiodic boundaries, nonlinear terms and variable coefficients bring their own complications.

## What the FFT does, and what it does not

We can now separate four claims that are often blurred together. Sampling turns a continuous signal into an array and may cause aliasing. The discrete Fourier transform gives an exact frequency representation of that array. The FFT computes that transform efficiently by reusing arithmetic. A spectral method then uses frequency coordinates to approximate or solve a particular mathematical model, subject to its own boundary conditions, discretization errors, and stability requirements.

These are four different decisions. A wrong sampling rate will not be rescued by an excellent FFT library. An incorrect boundary condition will not be repaired by a correct transform. And a numerically accurate FFT does not make a flawed physical model accurate. But when each decision is made carefully, the chain is powerful: measure or discretize a phenomenon, analyze its finite frequency modes, use those modes to calculate responses or evolution, and reconstruct a checked result in the original coordinates.

That is the value of the FFT. The cleverness of the algorithm is not just that it is fast. It turns Fourier analysis from a beautiful finite calculation into a practical coordinate system for large numerical problems. We can still recognize the mathematics in every step of the computation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: radix-two FFT and periodic heat modes

Define \(W_N=e^{-2\pi i/N}\). For even \(N\), let \(E_k\) be the \(N/2\)-point transform of even-indexed samples and \(O_k\) the transform of odd-indexed samples. Then for \(0\le k<N/2\),
\[
 X_k=E_k+W_N^kO_k,\qquad X_{k+N/2}=E_k-W_N^kO_k.
\]
This identity follows by splitting \(\sum_{n=0}^{N-1}x_nW_N^{kn}\) into \(n=2m\) and \(n=2m+1\), with \(W_N^{2km}=W_{N/2}^{km}\). In the second-half relation the odd-subsequence factor changes sign because \(W_N^{N/2}=-1\), while the even-subsequence factor is unchanged. Recursive radix-two work satisfies \(T(N)=2T(N/2)+O(N)=O(N\log_2 N)\).

For \(x=(1,2,3,4)\), the even and odd two-point transforms are \(E=(4,-2)\) and \(O=(6,-2)\). With \(W_4^0=1\), \(W_4^1=-i\), obtain
\[
 X=(10,-2+2i,-2,-2-2i).
\]

On a periodic grid of \(N\) points spaced by \(h\), set
\[
(L_h u)_j=\frac{u_{j-1}-2u_j+u_{j+1}}{h^2},\quad u_{j+N}=u_j.
\]
The mode \(v_j^{(k)}=e^{2\pi i kj/N}\) is an eigenvector with
\[
\lambda_k=\frac{e^{-2\pi i k/N}-2+e^{2\pi i k/N}}{h^2}
=-\frac{4}{h^2}\sin^2\left(\frac{\pi k}{N}\right).
\]
For semidiscrete heat \(\dot u=\kappa L_h u\), each DFT coefficient evolves as \(\widehat u_k(t)=e^{\kappa\lambda_k t}\widehat u_k(0)\). For even \(N\), forward Euler satisfies \(|1+\kappa\lambda_k\Delta t|\le 1\) for every mode when \(\kappa\Delta t/h^2\le 1/2\).

For \(N=4,h=\kappa=1\), \(u(0)=(1,0,0,0)\), \(\widehat u(0)=(1,1,1,1)\), and \(\lambda=(0,-2,-4,-2)\). With \(a=e^{-2t}\), \(b=e^{-4t}\),
\[
 u(t)=\frac14\big(1+2a+b,\;1-b,\;1-2a+b,\;1-b\big).
\]
It has sum one, starts at \((1,0,0,0)\), and tends to the constant state \((1/4,1/4,1/4,1/4)\).

### Exercises with worked answers

1. Compute the FFT butterfly for four samples \((1,2,3,4)\). **Answer:** the four coefficients are \((10,-2+2i,-2,-2-2i)\).
2. For \(N=8\), how many radix-two combination levels are needed? **Answer:** three, since \(\log_2 8=3\).
3. If the input has a million samples, does using an FFT remove aliasing from an inadequately sampled waveform? **Answer:** no. FFT and direct DFT compute the same transform of the same samples.
4. Derive the eigenvalue of the periodic second difference for mode \(e^{2\pi i kj/N}\). **Answer:** factor out the mode and simplify \(e^{-i\theta}-2+e^{i\theta}=-4\sin^2(\theta/2)\).
5. In the four-cell heat example, find the long-time temperature. **Answer:** one quarter at every cell, because only the zero-frequency mode remains.
6. For \(\kappa=2,h=1/4\), find the largest forward-Euler step allowed by the basic one-dimensional periodic diffusion condition for even \(N\). **Answer:** \(\Delta t\le h^2/(2\kappa)=1/64\).
7. Why can't a plain complex periodic FFT be substituted without thought for sine modes on an interval with fixed-zero endpoint temperatures? **Answer:** the boundary conditions and eigenfunctions differ; the periodic transform diagonalizes the periodic discrete operator, not the Dirichlet one.

### Sources and further reading

- [FFTW User Manual: Tutorial](https://www.fftw.org/doc/Tutorial.html).
- [FFTW User Manual: What FFTW Really Computes](https://fftw.org/fftw3_doc/What-FFTW-Really-Computes.html).
- [NumPy: Discrete Fourier Transform and FFT routines](https://numpy.org/doc/stable/reference/routines.fft.html).
- [MIT OpenCourseWare 18.086: Mathematical Methods for Engineers II](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/).
- [Wikipedia: Cooley–Tukey FFT algorithm](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm).
