# 056000 — Fourier Series, Convolution, and the Shape of Approximation

**Track:** Analysis from First Principles. **Background:** Hilbert spaces, trigonometric functions and Lebesgue integration. **Central question:** How does averaging isolate frequencies and approximate a function?

<!-- BEGIN SPOKEN LECTURE -->

# Fourier Series, Convolution, and the Shape of Approximation

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

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), choose normalized Haar measure \(dm=dx/(2\pi)\). Fourier coefficients and convolution are
\[\widehat f(n)=\int_{\mathbb T}f(x)e^{-inx}\,dm(x),\qquad (f*g)(x)=\int_{\mathbb T}f(x-y)g(y)\,dm(y).\]
Then \(\widehat{f*g}(n)=\widehat f(n)\widehat g(n)\), and Parseval is \(\|f\|_{L^2(dm)}^2=\sum_{n\in\mathbb Z}|\widehat f(n)|^2\). Fourier partial sums converge in \(L^2\), not necessarily pointwise at every x.

The Fejér kernel \(F_N(x)=\frac1N|\sum_{k=0}^{N-1}e^{ikx}|^2\), \(N\ge1\), has \(F_N\ge0\), \(\int F_Ndm=1\), and Fourier multiplier \(\widehat F_N(n)=(1-|n|/N)_+\). For continuous periodic \(f\), \(F_N*f\to f\) uniformly; for \(1\le p<\infty\), convergence holds in \(L^p\).

For the heat equation \(u_t=\partial_x^2u\) on the circle, \(\widehat u(t,n)=e^{-tn^2}\widehat u_0(n)\). The kernel tends to the periodic delta distribution as \(t\downarrow0\), and \(u(t)\to u_0\) in \(L^2\) for \(u_0\in L^2\).

### Exercises with answers

1. **Three frequencies.** Which Fourier frequencies occur in \(f(x)=\sin x+\tfrac12\sin3x\)? **Answer:** \(n=\pm1,\pm3\).
2. **Mean preservation.** If \(\int k\,dm=1\), why does convolution preserve the integral? **Answer:** Fubini and translation invariance give \(\int k*f\,dm=(\int k\,dm)(\int f\,dm)\).
3. **Heat filtering.** Compare frequencies two and five after time t. **Answer:** Multipliers are \(e^{-4t}\) and \(e^{-25t}\), so frequency five decays faster.

### Reading and source notes

- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
