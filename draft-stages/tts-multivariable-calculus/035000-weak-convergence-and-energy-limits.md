# Weak Convergence: What Survives When Energy Is Bounded

**Track:** Multivariable Calculus from First Principles. **Focus:** weak versus strong convergence, bounded sequences in Hilbert spaces, energy lower semicontinuity, and the limits that arise in variational existence proofs.

<!-- BEGIN SPOKEN LECTURE -->

# Weak Convergence: What Survives When Energy Is Bounded

Imagine a succession of ever finer approximations to an elastic string. Each approximation has a different shape, but an experiment tells us that their stretching energies remain below a fixed budget. The energy is an integral of the square of the slope. Does that energy bound guarantee that the shapes settle toward a limiting shape? And if they do, can we conclude that the limit has no more energy than the approximations?

These are not merely questions about numerical accuracy. They are the questions one must answer to prove that an energy-minimizing function exists at all. In finite-dimensional optimization, a bounded sequence of vectors has a convergent subsequence. In an infinite-dimensional function space, the analogous statement fails if convergence means that the distance between functions approaches zero in the usual norm. There are infinitely many independent ways for a sequence to vary without becoming close to any one element.

The rescue is to ask for a weaker kind of convergence. We will build that idea from familiar dot products, find an explicit sequence whose energy remains fixed even as its shape settles to zero, and then understand why this weaker limit is still strong enough for an existence proof.

## Begin with a question about vectors

Let us work for a moment in a space of square-summable sequences. A vector is an infinite list of numbers whose squares add to a finite sum. The ordinary length is the square root of that sum, just as in Euclidean space.

For each positive integer n, consider the vector that has a one in position n and zeros everywhere else. Call it e n. Every such vector has length one. Any two distinct members are separated by the square root of two. Therefore the sequence cannot converge in length, and it has no length-convergent subsequence. It keeps moving to a fresh coordinate direction, always at the same distance from the origin.

Yet test it against one fixed square-summable vector g. The dot product with e n is simply the n-th coordinate of g. Because the squares of g's coordinates add to a finite number, those coordinates must approach zero. No fixed test vector can detect a lasting component in the moving direction. Against every fixed g, the dot product approaches the dot product of the zero vector with g.

That is weak convergence. A sequence converges weakly to a vector if its dot product with every fixed test vector approaches the corresponding dot product of the proposed limit. Ordinary, or strong, convergence asks the full distance to the limit to vanish. Strong convergence implies weak convergence, by the Cauchy–Schwarz inequality. Our moving unit vectors prove the converse is false.

There is an important restriction on the word every. We may not choose a different test vector each time in order to chase the moving one. If we do choose g equal to e n at step n, the dot product stays one, but that is a changing test, not the fixed test required by the definition. Weak convergence describes what is visible to any one observation that has been selected in advance.

## From coordinates to functions

For square-integrable functions on an interval, the dot product is the integral of the product of two functions. Strong convergence in L two means the integral of the squared difference tends to zero. Weak convergence in L two means that, for every fixed square-integrable test function g, the integral of the approximating function times g tends to the integral of the limit times g.

A memorable example comes from rapidly oscillating cosines. On the interval zero to one, take the cosine of two pi n x. Each has squared integral one half. Its L two distance from zero is always the square root of one half, so there is no strong convergence to zero. But a fixed, reasonably smooth test function cannot follow oscillations that become arbitrarily rapid. Positive and negative contributions nearly cancel. For a smooth g we can establish this by integration by parts; for a general L two test function, we approximate it by smooth functions and use Cauchy–Schwarz to control the approximation error. The integrals tend to zero. The cosines converge weakly to zero.

Now put the derivative into the story. Let u n of x be the sine of two pi n x divided by two pi n. Every u n vanishes at both endpoints. The height of the oscillations goes to zero, and in fact u n converges strongly to zero in L two. Its derivative, however, is precisely the cosine of two pi n x. That derivative has the same fixed L two size for every n. The functions converge weakly, but not strongly, in the Sobolev energy space called H naught one.

For this sequence the squared slope norm is one half, while the squared slope norm of the limit function, zero, is zero. The high-frequency slopes disappear under fixed observations but not under the energy measurement. This is the key example to keep in mind whenever we pass to a weak limit.

It also warns us against an invalid argument: a weakly convergent sequence does not generally have convergent energy. We may find that the limit has strictly less energy than the approximations. What saves energy minimization is a one-sided inequality, not equality.

## What weak convergence means for a Sobolev function

In H one on an interval, we track both a function and its weak derivative. The H one inner product adds two integrals: one of the products of the functions and one of the products of their derivatives. Thus a sequence converges weakly in H one exactly when its functions and first derivatives converge weakly in L two, with a common limiting function and its weak derivative.

Why do we insist on that consistency? Because a function and its derivative are not independent variables. Their relationship is encoded by integration by parts against smooth, compactly supported test functions. Passing to weak limits in that identity preserves the relationship. The candidate limit still has the required weak derivative. We have not left the space in which the variational problem is defined.

For zero-endpoint functions, the relevant space is H naught one: the closure of smooth, compactly supported functions in the H one norm. On an interval its members have continuous representatives that vanish at the endpoints. In higher dimensions, boundary values must generally be interpreted through traces rather than pointwise evaluation. The exact space is part of the mathematical model, not a footnote.

We can now ask whether energy-bounded sequences have weakly convergent subsequences. In a Hilbert space, every norm-bounded sequence does. This is a weak compactness theorem. It does not promise that the entire sequence converges, nor does it give strong convergence. It promises that there is at least one subsequence whose response to every fixed continuous linear observation converges to a common limit.

A proof can be pictured through coordinates in a countable orthonormal basis: choose a subsequence on which the first coordinate converges, then one on which the second converges, and so on, finally taking a diagonal subsequence. Boundedness ensures the limiting coordinates describe an element of the Hilbert space, and approximation by finite coordinate combinations extends convergence from basis vectors to arbitrary tests. This is a sketch; the theorem is broader and can be expressed in terms of reflexivity and dual spaces.

The distinction from ordinary compactness is essential. Closed bounded sets in infinite-dimensional Hilbert spaces are generally not compact in the norm. They are compact in the weaker sense needed to extract weak limits. If we forget which topology we are using, a plausible existence proof can become false in a single line.

## The energy inequality that makes limits useful

Suppose u n converges weakly to u in a Hilbert space. Then the length of u cannot exceed the limit inferior of the lengths of u n. To see the reason, first consider a unit test vector pointing in the direction of u. The dot products of u n with that test vector approach the length of u. Each dot product is bounded by the length of u n. The limit cannot exceed the smallest eventual limiting size of those lengths. If u is zero, the inequality is immediate.

In symbols, the norm of the weak limit is at most the lim inf of the norms. The same holds for the squared norm. This property is called weak lower semicontinuity.

Apply it to derivatives. If u n converges weakly in H one, then its derivatives converge weakly in L two. Therefore the integral of the squared derivative of the limit is at most the lim inf of the corresponding derivative energies of the approximations.

Look back at the small-amplitude sine waves. Each derivative energy is one half. The derivative energy of the limit is zero. So the inequality reads zero is at most one half. It is strict, which is perfectly allowed. What we cannot have is a hidden increase of derivative energy at the weak limit.

The inequality may initially feel backward. Why can energy disappear? Because weak tests can miss rapid oscillations or concentration. The energy bound still prevents the limit from mysteriously acquiring more energy than the approximations carry. That direction is exactly what we need when our approximations are trying to make energy as small as possible.

The statement does not apply to every energy merely because it is called an energy. The squared norm is special. Convexity and lower semicontinuity provide broad mechanisms for this property, but nonlinear integrands can fail it. A negative squared norm, for instance, reverses the inequality: the moving unit vectors all have negative-one energy, while the weak limit has energy zero. Zero is not less than or equal to negative one. We must prove lower semicontinuity for the functional we actually intend to minimize.

## The minimal existence argument, almost assembled

Consider an energy that penalizes slopes and rewards following a specified load. On the unit interval with fixed-zero endpoints, take one half the integral of squared slope, minus the integral of a prescribed square-integrable load times the function. This is the familiar energy whose stationary point solves a one-dimensional Poisson equation.

The load term cannot drive the energy to negative infinity, because Cauchy–Schwarz and Poincaré's inequality let us bound its size by a constant times the slope norm. A quadratic positive term eventually dominates a linear negative term. Consequently, any sequence whose energy approaches the infimum must remain bounded in H naught one.

That boundedness grants a weakly convergent subsequence. Its limit still vanishes at the endpoints. The squared-slope term is weakly lower semicontinuous. The load term is a continuous linear functional, so it actually converges along the weakly converging subsequence. Put those facts together: the energy of the limit cannot exceed the limiting infimum of the approximating energies.

But the approximating energies were already approaching the smallest possible value. Therefore the limit attains that value. A minimizer exists. This is the core of the direct method in the calculus of variations. We have not yet explained its nonlinear versions, but the logical structure is visible: obtain a bounded minimizing sequence, extract an appropriate limit, keep the constraints, and prevent the energy from jumping upward.

Notice that none of these steps begins by solving the Euler–Lagrange differential equation. We can establish that there is a minimizing function before we derive any pointwise equation or ask how many classical derivatives it possesses. That separation becomes especially valuable when the equation is nonlinear or when the solution has corners, interfaces, or contact regions.

## What the word compactness will mean next

Weak compactness has given us an admissible limit, but not enough convergence to handle every nonlinear term. For instance, knowing that u n converges weakly in L two does not by itself imply that the squares of u n converge to the square of u. Our oscillating cosine example makes that failure immediate: the functions converge weakly to zero, yet their squared integrals remain one half.

Sometimes a derivative bound contains more information than boundedness alone. On a bounded interval it prevents functions from forming arbitrarily sharp changes in height. We can then extract a subsequence that converges uniformly, or in a stronger integral norm, even though its derivatives may converge only weakly. This is the compactness behind Sobolev embeddings and the Rellich theorem.

It lets us separate two tasks. Weak convergence retains control of derivatives and the energy. Strong convergence of the functions themselves handles many nonlinear expressions depending on their values. Using both at once is how a limited energy budget can produce a genuine solution to a nonlinear variational problem.

The essential lesson is not that weak convergence is a poor substitute for strong convergence. It is the right notion for some questions and insufficient for others. An existence proof succeeds when it assigns each passage to a limit the type of convergence that actually justifies it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Definitions and the moving-coordinate example

For a real Hilbert space \(H\),

\[
x_n\rightharpoonup x\quad\Longleftrightarrow\quad
\langle x_n,y\rangle\to\langle x,y\rangle\qquad \forall y\in H.
\]

For \(H=\ell^2\), the standard orthonormal vectors \(e_n\) satisfy \(\|e_n\|=1\) and \(e_n\rightharpoonup0\). Indeed, if \(y=(y_1,y_2,\ldots)\in\ell^2\), then \(\langle e_n,y\rangle=y_n\to0\). Yet \(\|e_n-0\|=1\), so convergence is not strong. More generally Bessel's inequality gives \(\sum_n|\langle x,e_n\rangle|^2\le \|x\|^2\).

For \(u_n(x)=\sin(2\pi n x)/(2\pi n)\) in \(H_0^1(0,1)\),

\[
\|u_n\|_{L^2}^2=\frac{1}{8\pi^2n^2}\to0,
\qquad u_n'(x)=\cos(2\pi nx),
\qquad\|u_n'\|_{L^2}^2=\frac12.
\]

The Riemann–Lebesgue lemma (first on smooth tests, then by density on \(L^2\)) implies \(u_n'\rightharpoonup0\) in \(L^2\). Hence \(u_n\rightharpoonup0\) in \(H_0^1\), but not strongly. Both the \(L^2\) component and the derivative component converge weakly to the corresponding components of zero.

### Weak compactness and lower semicontinuity

Every bounded sequence in a Hilbert space has a weakly convergent subsequence. The analogous result holds in reflexive Banach spaces. Neither assertion holds for arbitrary nonreflexive Banach spaces without extra hypotheses.

If \(x_n\rightharpoonup x\), then

\[
\|x\|\le\liminf_n\|x_n\|,
\qquad\|x\|^2\le\liminf_n\|x_n\|^2.
\]

For \(x\ne0\), take the fixed test \(y=x/\|x\|\) and use
\(\langle x_n,y\rangle\le\|x_n\|\). Apply the squared-norm version to the weakly convergent gradients \(\nabla u_n\rightharpoonup\nabla u\) in \(L^2\):

\[
\int_\Omega|\nabla u|^2\,dx\le \liminf_{n\to\infty}
\int_\Omega|\nabla u_n|^2\,dx.
\]

The negative squared norm is a counterexample: \(F(e_n)=-1\) but \(F(0)=0\), so \(F(0)\le\liminf F(e_n)\) fails.

### A complete direct-method proof for the linear string

On \(V=H_0^1(0,1)\), for \(f\in L^2(0,1)\), set

\[
E(u)=\frac12\|u'\|_2^2-\int_0^1fu\,dx.
\]

With Poincaré constant \(C_P\), \(\|u\|_2\le C_P\|u'\|_2\), hence
\[
E(u)\ge\frac12\|u'\|_2^2-C_P\|f\|_2\|u'\|_2\to+\infty
\qquad\text{as }\|u\|_{H_0^1}\to\infty.
\]

The infimum is finite; a minimizing sequence is norm-bounded. Take a weakly convergent subsequence in \(V\). Because \(u\mapsto\int fu\) is bounded linear and \(u\mapsto\|u'\|_2^2\) is weakly lower semicontinuous,

\[
E(u_*)\le\liminf_{k\to\infty}E(u_{n_k})=\inf_{v\in V}E(v).
\]

The opposite inequality holds by the definition of the infimum, so equality follows. Strict convexity of the quadratic form on \(H_0^1\) also implies uniqueness. Differentiating *after* existence yields \(\int u_*'v'=\int fv\) for all \(v\in V\), namely the weak Poisson equation.

### Exercises with answers

1. **Moving directions:** Why is \(e_n\) weakly zero despite \(\langle e_n,e_n\rangle=1\)? **Answer:** Weak convergence keeps the test fixed; \(e_n\) changes with \(n\).
2. **Energy loss:** Compute \(\lim_n\int|u_n'|^2\) and \(\int|0'|^2\) for the oscillating sequence. **Answer:** The former is \(1/2\); the latter is zero. Weak lower semicontinuity allows strict inequality.
3. **Linear terms:** If \(u_n\rightharpoonup u\) in \(L^2\), what happens to \(\int fu_n\) for fixed \(f\in L^2\)? **Answer:** It tends to \(\int fu\), directly from weak convergence.
4. **Counterexample:** Let \(F(u)=-\|u\|^2\) in \(\ell^2\). Prove that \(F\) is not weakly lower semicontinuous. **Answer:** Use \(e_n\rightharpoonup0\): \(F(0)=0> -1=\liminf F(e_n)\).

### Sources and further reading

- J. C. Wei, [*The Direct Methods in the Calculus of Variations*, UBC lecture notes](https://personal.math.ubc.ca/~jcwei/MATH517-2018-Lectnotes2.pdf), for weak compactness and the coercive, weakly lower-semicontinuous existence theorem.
- Thomas Schmidt, [*Calculus of Variations*, Hamburg lecture notes](https://www.math.uni-hamburg.de/home/schmidt/lectures/CalcVar.pdf), for lower semicontinuity and direct-method reasoning.
- [Wikipedia: Weak convergence (Hilbert space)](https://en.wikipedia.org/wiki/Weak_convergence_%28Hilbert_space%29), for terminology and equivalent characterizations.
- [Wikipedia: Direct method in the calculus of variations](https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations), for the standard existence-proof architecture.

*Teaching connections:* `multivariable-calculus:033000` introduces weak solutions, `034000` constructs Galerkin approximations, and `linear-algebra:025000` treats energy minimization in Krylov methods. Weak convergence distinguishes bounded energy from norm convergence in all three settings.
