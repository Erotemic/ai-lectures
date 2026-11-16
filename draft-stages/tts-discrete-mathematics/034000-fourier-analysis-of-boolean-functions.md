# 034000 — Fourier Analysis on the Boolean Cube

**Track:** Discrete Mathematics and Combinatorics. **Background:** probability, orthogonality, Boolean functions, and elementary harmonic analysis. **Central question:** how can a function of many bits be decomposed into independent interaction terms, and what does that reveal about noise and influence?

<!-- BEGIN SPOKEN LECTURE -->

# Harmonic analysis on a finite space

Fourier analysis often begins with waves on a circle. A complicated signal is decomposed into simple oscillations, each with a frequency and a coefficient. The Boolean cube seems like a completely different object. Its points are strings of plus ones and minus ones. There is no continuously varying angle, only a collection of discrete choices.

Yet the same strategy works. A function on n bits can be decomposed into components indexed by subsets of the n coordinates. One component is constant. Some depend on individual bits. Others measure two-way interactions, three-way interactions, and all the way up to a term involving every bit at once.

The basic building blocks are parity characters. Given a set of coordinates S, multiply the input bits whose positions lie in S. That product is either plus one or minus one. For the empty set it is always one. For a singleton it is just the chosen bit. For the full coordinate set it is the parity of all bits, expressed in the plus-minus convention.

These characters form an orthonormal basis for real-valued functions on the Boolean cube when inputs are uniformly random. This turns a discrete function into a vector of Fourier coefficients. The coefficients tell us which interactions the function uses.

# Orthogonality is almost free

Take two distinct parity characters. Multiply them together. Any coordinate belonging to both sets appears twice and cancels, because a bit squared equals one. What remains is the parity character of the symmetric difference of the two sets.

If that difference is nonempty, at least one independent uniformly random bit appears exactly once. Averaging over that bit produces zero. Therefore the expected product of distinct characters is zero. The expected square of a character is one. That proves orthonormality with almost no machinery.

There are two to the n subsets of n coordinates and exactly two to the n possible inputs. So we have exactly enough orthonormal characters to form a basis for every function on this finite space.

The Fourier coefficient at a set S is the average value of the function multiplied by the parity character of S. Add all those coefficients times their characters, and the original function is recovered exactly. This is an identity on every input, not a statistical approximation.

# Parseval turns function size into coefficient energy

There is a finite version of Parseval's identity. The expected square of the function equals the sum of squares of all its Fourier coefficients. For a Boolean function taking only plus one and minus one, the expected square is always one. Thus its Fourier coefficients have squared magnitudes summing to one.

This is powerful because it converts nonlinear-looking questions about a function into ordinary sums over subsets. A function that puts most of its Fourier energy on small subsets is dominated by low-order interactions. A parity of all n coordinates puts all its energy on the full set. Both are perfectly legitimate Boolean functions, but they respond differently to random noise.

Consider majority on three bits. It outputs the sign of the sum of the three inputs, so there is never a tie. Its Fourier expansion is one half times the sum of the three individual bits, minus one half times their triple product. The three singleton coefficients and the triple coefficient each have absolute value one half. Their squared magnitudes sum to four quarters, exactly one.

That expansion shows that three-bit majority is mostly a linear vote, with a three-way correction. One can verify it by substituting all eight inputs, but the Fourier basis explains why those terms are the right ones.

# Influence measures susceptibility to one flipped bit

To study sensitivity, choose an input uniformly at random and flip one selected coordinate. Ask how often the output changes. The probability of change is called the influence of that coordinate for a Boolean output.

Fourier analysis gives an exact identity. A character involving coordinate i changes sign when i is flipped; a character not involving i does not change. Squaring the difference and averaging removes cross terms by orthogonality. The influence of coordinate i becomes the sum of squared Fourier coefficients over all subsets containing i.

The total influence sums over coordinates. Every coefficient indexed by S is then counted once for each coordinate in S, giving the sum of the coefficient squares weighted by the size of S. High-degree Fourier components contribute more to sensitivity.

For parity on all n bits, flipping any one bit always flips the output. Every coordinate has influence one. For majority on three bits, each coordinate has influence one half. The distinction is now numerical rather than intuitive.

# Noise stability is a spectral filter

Suppose each input bit is independently kept with some probability and flipped otherwise. Let rho denote the correlation between the original bit and the noisy bit. If a parity character involves k distinct coordinates, its expected product before and after noise is rho raised to k. Each coordinate contributes one factor of rho.

Consequently the expected product of the function on the original input and on the noisy input is a sum of squared Fourier coefficients weighted by rho to the size of their subsets. This is the noise-stability formula.

For full parity, the answer is rho to the n. At any fixed correlation strictly between zero and one, parity loses correlation rapidly as n grows. For three-bit majority, noise stability is three quarters times rho plus one quarter times rho cubed. The low-degree Fourier energy keeps it more stable for moderate noise.

The same operator that shrinks degree-k Fourier coefficients by rho to the k is called the noise operator. It smooths functions on the cube by suppressing high-degree interactions. It is a discrete counterpart of familiar heat or smoothing operators in continuous analysis.

# A useful inequality from the same coefficients

Let the variance of a function measure the part not explained by its constant Fourier coefficient. Parseval says the variance is the sum of squared coefficients over all nonempty subsets.

Every nonempty subset has size at least one. So the variance is at most the sum of subset sizes times squared coefficients. But that last sum is total influence. We have obtained the Boolean Poincaré inequality: variance is bounded above by total influence.

This inequality has a useful reading. If a function varies significantly across inputs, flipping coordinates must have some aggregate chance of affecting it. The statement does not say any one coordinate must have large influence, but more sophisticated theorems, such as Kahn–Kalai–Linial, derive individual-coordinate information under additional assumptions.

# Which assumptions are being used?

All these clean formulas assume uniformly distributed, independent input bits and the plus-minus representation. For biased product distributions one builds a different orthonormal basis. For correlated inputs the characters need not be orthogonal. For real-valued outputs, Parseval still works, but the interpretation of influence as a flip probability requires modification.

Fourier analysis on the Boolean cube is useful precisely because it forces us to specify the probability space and the functions being studied. Once those details are fixed, arguments about majority votes, parity checks, randomized algorithms, threshold phenomena, and social choice can be made through the same coefficient language. A high-dimensional discrete problem becomes a set of spectral identities that can be calculated, compared, and bounded.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On the uniform cube `{-1,1}^n`, for `S subseteq [n]` define `chi_S(x)=prod_{i in S}x_i`. Then
\[
\widehat f(S)=\mathbb E[f(X)\chi_S(X)],\quad f(x)=\sum_{S}\widehat f(S)\chi_S(x),\quad
\mathbb E[f^2]=\sum_S\widehat f(S)^2.
\]
Because `chi_S chi_T=chi_{S triangle T}`, distinct characters are orthogonal. For Boolean `f in {-1,1}`, define influence `Inf_i(f)=P[f(X) != f(X^{(i)})]` with coordinate i flipped. Then
\[
\mathrm{Inf}_i(f)=\sum_{S\ni i}\widehat f(S)^2,\quad I(f)=\sum_S |S|\widehat f(S)^2,\quad
\mathrm{Var}(f)=\sum_{S\ne\varnothing}\widehat f(S)^2\le I(f).
\]
For a rho-correlated pair `(X,Y)` obtained by independently flipping X coordinates with probability `(1-rho)/2`, the noise stability is
\[
\mathbb E[f(X)f(Y)]=\sum_S\rho^{|S|}\widehat f(S)^2.
\]
For majority on three bits, `Maj_3(x)=(x_1+x_2+x_3-x_1x_2x_3)/2`. Fourier weights are `1/2` on each singleton and `-1/2` on the triple. Thus each influence is `1/2`, the total influence is `3/2`, and noise stability is `(3/4)rho+(1/4)rho^3`. For n-bit parity `f=chi_[n]`, each influence is 1 and stability is `rho^n`.

### Exercises with answers

1. Find the Fourier coefficient of `f(x)=x_1x_3`. **Answer:** coefficient one at `{1,3}` and zero elsewhere.
2. What is total influence of full parity on n bits? **Answer:** n.
3. Evaluate three-bit majority noise stability at rho=0. **Answer:** zero.
4. Explain the Boolean Poincaré inequality in one line. **Answer:** `sum_{S!=empty} fhat(S)^2 <= sum_{S!=empty}|S| fhat(S)^2` because `|S|>=1`.

### Reading and source notes

- [Ryan O'Donnell, Analysis of Boolean Functions](https://arxiv.org/abs/2105.10386), Fourier coefficients, influences, and noise stability.
- [Ryan O'Donnell, Analysis of Boolean Functions (book site)](https://www.cs.cmu.edu/~odonnell/), text and accompanying materials.
- [Ryan O'Donnell, author and book information](https://www.cs.cmu.edu/~odonnell/), official book and course resources.
