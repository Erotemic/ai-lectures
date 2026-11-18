# Why Boundaries Select Fourier Modes: Sturm–Liouville from Scratch

<!-- BEGIN SPOKEN LECTURE -->

# Why Boundaries Select Fourier Modes

A guitar string can vibrate with one broad hump, with two alternating humps, with three, or with many more. A heated rod can cool in spatial patterns resembling the same sine curves. These shapes are not inserted into a calculation because sines happen to be familiar functions. The differential equation and the conditions at the ends select them.

We can find this selection rule with calculus and the elementary equation for a harmonic oscillator. It will give us eigenvalues and eigenfunctions, two words that may sound more sophisticated than the calculation is. An eigenfunction is simply a nonzero shape that an operator changes only by multiplying it by a number. An eigenvalue is that multiplier. The number tells us how strongly the operation acts on the shape.

For a function X of x, our operator will take its second derivative and change the sign. If applying this operator to X produces lambda times X, we write, in words, negative X double prime equals lambda X. The boundary conditions decide which values of lambda permit a nonzero X. This is a boundary-value problem with the eigenvalue itself unknown.

## The fixed-end calculation

First require X to vanish at x equal to zero and at x equal to one. Suppose lambda is positive. Let its square root be k. Our equation becomes X double prime plus k squared times X equals zero. You know its solutions from oscillators: a cosine of kx and a sine of kx, with arbitrary coefficients.

At the left endpoint, cosine is one and sine is zero, so the zero-value condition forces the cosine coefficient to vanish. We are left with a multiple of sine of kx. At the right endpoint, the condition says that the multiple of sine of k must be zero. We are looking for a nonzero function, so the multiple cannot vanish. Sine of k therefore must be zero.

That happens when k is an integer multiple of pi. Since k is positive, the integer must be one, two, three, and so on. The allowed eigenvalues are pi squared, four pi squared, nine pi squared, and so forth. Each one corresponds to a sine shape, sine of pi x, sine of two pi x, sine of three pi x, and onward.

Before celebrating, we must check the other possibilities. If lambda is zero, X double prime is zero, so X is a straight line. A line that vanishes at both endpoints vanishes everywhere. No nonzero eigenfunction exists. If lambda is negative, the solutions are built from growing and decaying exponentials, or hyperbolic sines and cosines. Those cannot produce a nonzero function vanishing at both ends in this particular problem either. We therefore have found all the eigenvalues, not merely some of them.

The length of the interval matters. On a rod or string of length L, the sine shapes become sine of n pi x divided by L, and the eigenvalues become n squared pi squared divided by L squared. Halve the length and every eigenvalue quadruples. In a vibrating string that affects its oscillation frequencies; in a heated rod it affects its rate of cooling. Boundary geometry has entered a dynamical prediction before we have even written the time-dependent equation.

## Why the sine shapes do not interfere in an integral

Take two different eigenfunctions, say the first sine and the second sine. Their product is sometimes positive, sometimes negative. Its integral over the interval is zero. More generally, sine of m pi x and sine of n pi x are orthogonal when m and n are different positive integers.

We can prove a more general statement without memorizing trigonometric identities. Suppose X_m and X_n satisfy negative X double prime equals their respective eigenvalue times X, with the same zero boundary conditions. Multiply the first equation by X_n and the second by X_m. Subtract, then integrate. The difference of the second-derivative terms is an exact derivative, so integration by parts turns it into an endpoint expression. Both functions vanish at the endpoints, making that expression zero.

What remains is the difference between the two eigenvalues times the integral of X_m times X_n. If the eigenvalues are different, that integral must be zero. Orthogonality comes from the self-adjoint structure of the differential operator and its boundary conditions, not from a lucky coincidence of sine identities.

Orthogonality lets us measure how much of a complicated shape lies along one mode. Multiply the shape by a mode, integrate, and divide by the squared length of the mode. On the unit interval, the squared integral of sine of n pi x is one half, so the coefficient is twice the integral of the original shape times that sine. This is precisely the construction of a Fourier sine series.

There is an important logical distinction here. Orthogonality shows how to extract coefficients if an expansion is available. Showing that every sufficiently reasonable shape can be recovered from its infinite collection of coefficients is a separate completeness theorem. For the standard sine and cosine systems on a finite interval, that theorem is true in a mean-square sense. We should not silently assume analogous completeness for every differential equation merely because its first few eigenfunctions look attractive.

## Changing the ends changes the notes

Now insulate both ends, so the derivatives vanish at zero and one instead of the values. Solve the same eigenvalue equation. At the left endpoint, the derivative of sine is nonzero unless its coefficient vanishes, leaving a cosine shape. At the right endpoint, the derivative of cosine vanishes exactly when its frequency is an integer multiple of pi.

We again obtain a sequence of positive eigenvalues, but the eigenfunctions are cosines. There is also one new mode: the constant function. Its derivative is zero everywhere, its second derivative is zero, and it satisfies both insulated conditions. Its eigenvalue is zero.

This constant mode will have a physical consequence. A rod insulated at both ends can redistribute heat but cannot lose its average temperature through the boundaries. The zero eigenvalue says there is one spatial pattern the diffusion operator does not change: a constant. It also explains why the pure Neumann steady problem left a free additive constant.

Try a mixed pair of conditions: X is zero at the left, and its derivative is zero at the right. The left end still forces us to use a sine. But the right derivative now involves cosine of the frequency. It vanishes at pi over two, three pi over two, five pi over two, and so on. The corresponding eigenvalues are the squares of those half-integer multiples of pi. The lowest spatial mode has a quarter of the first Dirichlet eigenvalue on the same unit interval.

There is no mystery about the different lists. A wave that must vanish at an endpoint cannot have an antinode there. A wave that must have zero slope can. Changing the constraint changes the set of allowed spatial patterns, just as changing how a string is held changes the notes it can support.

## When an eigenvalue makes a forced problem unsolvable

Eigenfunctions are not only a way to build time-dependent solutions. They also warn us about steady forcing. Consider negative u double prime minus pi squared times u equals sine of pi x, with u equal to zero at both endpoints.

If you try a solution proportional to sine of pi x, the two terms on the left cancel exactly: the negative second derivative contributes pi squared times the sine, and the subtraction removes it. That trial function cannot generate the forcing on the right. Could a more complicated function succeed?

Multiply the equation by sine of pi x and integrate. By integration by parts and the zero endpoint conditions, the integral of negative u double prime times sine equals pi squared times the integral of u times sine. The two left-hand contributions cancel for any sufficiently smooth u satisfying the boundaries. Yet the right-hand integral is the integral of sine squared, which equals one half. We would be forced to say zero equals one half. So no solution exists.

This is a boundary resonance. The operator negative second derivative minus pi squared has a nonzero homogeneous solution, sine of pi x, and the proposed source points directly in that forbidden direction. The obstruction is not numerical. It is a contradiction in the boundary-value problem itself.

Change the forcing to sine of two pi x. Now we can use a multiple of the second mode. Its negative second derivative is four pi squared times itself. Subtract pi squared times itself and we are left with three pi squared times that mode. Divide by three pi squared to produce a particular solution. But there is not a unique answer: we can add any multiple of sine of pi x, because that mode lies in the homogeneous null space and satisfies the boundaries. This is the other half of resonance: compatible forcing can yield many solutions.

The exact same issue appears when solving a matrix equation. If a matrix has a zero eigenvalue, some right-hand sides are outside its range, and when a solution exists it may not be unique. The differential operator acts on functions instead of finite vectors, but the linear algebra analogy is accurate for these examples.

## The Sturm–Liouville generalization

Our constant-coefficient calculation is a special case of a wider class called regular Sturm–Liouville problems. Instead of the negative second derivative alone, consider a positive coefficient p of x multiplying the derivative, then differentiate that product and change its sign. Add a potential term q of x times the function. On the other side place lambda times a positive weight w of x times the function.

In exact notation, the companion records the equation and the boundary assumptions. What matters for the listening argument is the structure: p and w stay positive, and the boundary conditions are chosen so that the integration-by-parts endpoint terms cancel. The resulting eigenvalues are real; eigenfunctions with different eigenvalues are orthogonal when we integrate their product against the weight w. Under the usual regularity and separated self-adjoint boundary assumptions, there is an ordered sequence of eigenfunctions from which we can build weighted mean-square expansions.

One can also discover the sign and scale of an eigenvalue through energy. Multiply the fixed-end equation by its eigenfunction, integrate, and use integration by parts. The integral of the derivative squared equals lambda times the integral of the function squared. Unless the function is zero, both integrals are positive, which forces lambda to be positive. The ratio of these integrals is called a Rayleigh quotient. It measures how much spatial variation a shape has relative to its overall size.

That is a helpful interpretation of the frequency list. Higher sine modes change sign more often and have larger derivatives. Their Rayleigh quotients grow like the square of the mode number. When the spatial operator controls time evolution, that increasing eigenvalue produces either faster exponential damping or faster oscillation, depending on the equation.

## A bridge from Fourier analysis to evolution

We have built a library of spatial shapes and learned why the boundaries select them. The calculation was an ordinary differential equation in x, equipped with two endpoint conditions. Nothing required a heat equation or a wave equation yet.

Now suppose a time-dependent model contains that same negative second-derivative operator. The sine functions are natural building blocks because the spatial part acts on each without changing its shape. Only its coefficient in time needs to evolve. A partial differential equation can then reduce to a collection of scalar time equations, one for each mode.

For diffusion, those coefficients decay. For a vibrating string, they oscillate. The difference between heat and wave motion comes not from choosing a new Fourier basis, but from the different time derivatives in the physical law. This is why studying the boundary-value eigenproblem first is so useful: it separates the mathematics of space from the mathematics of time, allowing us to understand each before joining them.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: boundary spectra, orthogonality and resonance

### Dirichlet, Neumann and mixed eigenvalues

For \(-X''=\lambda X\) on \((0,L)\):

- **Dirichlet:** \(X(0)=X(L)=0\). Eigenpairs \(\lambda_n=(n\pi/L)^2\), \(X_n(x)=\sin(n\pi x/L)\), \(n=1,2,\dots\).
- **Neumann:** \(X'(0)=X'(L)=0\). Eigenpairs \(\lambda_n=(n\pi/L)^2\), \(X_n=\cos(n\pi x/L)\), \(n=0,1,\dots\), with \(X_0=1\), \(\lambda_0=0\).
- **Mixed:** \(X(0)=X'(L)=0\). Eigenpairs \(\lambda_n=((n+1/2)\pi/L)^2\), \(X_n=\sin((n+1/2)\pi x/L)\), \(n=0,1,\dots\).

The three cases can also be read as boundary restrictions on half-wavelengths.

### Orthogonality proof

If \(-X_m''=\lambda_m X_m\), \(-X_n''=\lambda_n X_n\), and both satisfy homogeneous Dirichlet data, then
\[
(\lambda_m-\lambda_n)\int_0^L X_m X_n\,dx
=\bigl[X_m X_n'-X_n X_m'\bigr]_{0}^{L}=0.
\]
For \(\lambda_m\ne\lambda_n\), the product integral vanishes. For normalized Dirichlet sines on \((0,L)\),
\[
\int_0^L\sin\frac{m\pi x}{L}\sin\frac{n\pi x}{L}\,dx=\frac L2\,\delta_{mn},\qquad
b_n=\frac2L\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx.
\]
The equality \(f=\sum b_nX_n\) holds in \(L^2\) for \(f\in L^2(0,L)\); pointwise conclusions require further hypotheses.

### Forced resonance example

For \(L=1\) consider
\[
-u''-\pi^2u=f(x),\qquad u(0)=u(1)=0.
\]
Testing against \(\sin(\pi x)\) forces \(\int_0^1 f(x)\sin(\pi x)\,dx=0\). Thus \(f=\sin(\pi x)\) is inconsistent. For \(f=\sin(2\pi x)\),
\[
u_p(x)=\frac{\sin(2\pi x)}{3\pi^2},\qquad
u(x)=u_p(x)+C\sin(\pi x)
\]
is the entire solution family.

### Regular Sturm–Liouville structure

\[
-(pX')'+qX=\lambda wX,\qquad p(x)>0,\ w(x)>0.
\]
Assume regular coefficients on the closed interval and separated self-adjoint boundary conditions. The operator is symmetric for the weighted inner product \(\langle f,g\rangle_w=\int_a^b f g w\,dx\). Distinct eigenfunctions are weighted-orthogonal. With homogeneous Dirichlet boundaries the Rayleigh quotient is
\[
\lambda=\frac{\int_a^b[p(X')^2+qX^2]dx}{\int_a^b wX^2dx}.
\]
Other boundary conditions can contribute boundary terms to this expression; do not silently use the Dirichlet formula for arbitrary Robin data.

### Exercises with answers

1. Find the lowest positive Dirichlet eigenvalue on \((0,2)\). **Answer:** \(\pi^2/4\), with eigenfunction \(\sin(\pi x/2)\).
2. For Neumann boundaries on \((0,1)\), identify a zero eigenfunction. **Answer:** \(X\equiv1\).
3. For \(X(0)=0,X'(1)=0\), find the lowest eigenvalue. **Answer:** \(\pi^2/4\), eigenfunction \(\sin(\pi x/2)\).
4. Solve \(-u''-\pi^2u=\sin(3\pi x)\) with zero Dirichlet values. **Answer:** \(u=\sin(3\pi x)/(8\pi^2)+C\sin(\pi x)\).
5. Why do different Dirichlet eigenfunctions have zero integral of their product? **Answer:** the integration-by-parts identity has vanishing boundary terms and nonzero eigenvalue difference.

### Sources and further reading

- [Jiří Lebl, *Differential Equations for Engineers*, Sturm–Liouville problems](https://math.libretexts.org/Bookshelves/Differential_Equations/Differential_Equations_for_Engineers_%28Lebl%29/5%3A_Eigenvalue_problems/5.1%3A_Sturm-Liouville_problems).
- [University of Victoria, *Differential Equations*, Sturm–Liouville problems](https://web.uvic.ca/~tbazett/diffyqs/slproblems_section.html).
- [MIT OpenCourseWare, 18.303 Linear PDE, course outline](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/pages/syllabus/).
