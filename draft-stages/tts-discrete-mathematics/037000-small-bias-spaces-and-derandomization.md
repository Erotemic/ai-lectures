# 037000 - Small-Bias Spaces and Derandomization

**Track:** Discrete Mathematics. **Background:** parity, probability spaces, finite fields, and Fourier analysis on the Boolean cube. **Central question:** how few random bits can fool every nontrivial parity test?

<!-- BEGIN SPOKEN LECTURE -->

# Random-looking does not mean uniformly random

Suppose an algorithm asks for n independent fair coin flips. A direct implementation needs n random bits. But perhaps the algorithm only ever examines the parity of selected groups of coordinates. In that case, asking for full independence may be wasteful.

A distribution on bit strings is called epsilon-biased if every nonempty parity has expectation close to zero when represented as a plus-or-minus-one sign. Under genuinely uniform independent bits, every nontrivial parity is perfectly balanced. Under a small-bias distribution, its bias is at most epsilon. This is a test-dependent version of pseudorandomness. The distribution is designed to fool a family of observers, not every conceivable observer.

The major achievement of explicit small-bias constructions is that a surprisingly short random seed can produce a long bit string that looks almost uniform to every linear parity test. Constructions of Naor and Naor use a seed whose length grows logarithmically with the output length and with the reciprocal error, rather than linearly with the output length.

# Fourier characters explain the definition

For a selected set of coordinates, multiply a sign of negative one for every selected one-bit. The result is positive for even parity and negative for odd parity. Such parity signs are also called Fourier characters.

Each nonempty subset has its own character. The small-bias requirement says the expectation of each nonconstant character is close to zero. In Fourier language, every nontrivial character has small correlation with the distribution. The trivial character is always one; forcing it close to zero would be nonsensical because every probability distribution has total mass one.

Why focus on characters? Because every real-valued function on the Boolean cube can be written as a linear combination of them. If a function has small total absolute Fourier weight outside the constant term, then small bias controls how much its expectation under the pseudorandom distribution can differ from its uniform expectation.

This is a meaningful guarantee, but not a universal one. An arbitrary Boolean function may have enormous total absolute Fourier weight, or may be designed explicitly to recognize the small support of the pseudorandom distribution. The Fourier expansion gives a bound, not a miracle.

# Pairwise independence is a weaker promise

Consider the four three-bit strings zero-zero-zero, zero-one-one, one-zero-one, and one-one-zero, sampled uniformly. Every individual bit is fair. Every pair of bits is jointly uniform. In fact, any parity involving one or two of the bits is perfectly balanced.

Yet the parity of all three bits is always even. The third-order parity test distinguishes this distribution from three independent uniform bits with certainty. It is pairwise independent but not three-wise independent, and it fails the small-bias definition with an error less than one because one nonempty parity has full bias.

This four-string example prevents a common confusion. Limited independence controls tests involving only a bounded number of coordinates. Small bias controls parity tests involving arbitrary numbers of coordinates. Neither promise automatically fools every nonlinear function, and their seed-length tradeoffs depend on the exact requirements.

# Support size and seed length

A generator using s uniform random seed bits produces a distribution supported on at most two to the power s outputs. If s is logarithmic in n and in one over epsilon, the support can be polynomial in n and one over epsilon.

Compare that with the two to the n possible output strings of a truly uniform distribution. When n is large, a polynomial-sized support occupies only a tiny fraction of the cube. An observer allowed to inspect the entire output string and ask “is this string in the generator's support?” can easily distinguish it from uniform.

So there is no contradiction between a very short seed and the information-theoretic impossibility of approximating the full uniform distribution in total variation with tiny support. Small-bias generators achieve a narrower, precisely stated goal. Their success comes from limiting which statistical tests need to be fooled.

This distinction is central to derandomization. Algorithms typically do not use every property of their random bits. They use specific concentration inequalities, moment identities, or low-complexity tests. Replacing full independence with a smaller pseudorandom space is valid only after identifying which of those properties the algorithm actually needs.

# How an explicit construction is used

An explicit small-bias family gives a deterministic way to list or evaluate the outputs associated with short seeds. If an algorithm's desired behavior is certified by the average of a controlled family of parity tests, we can replace an exponential search over all n-bit strings with a much smaller search over generator seeds.

For a single parity, choosing a small-bias output at random gives nearly equal chances of the two answers. For an algorithm with several parity checks, a union-bound or Fourier argument may control the overall behavior. However, simply declaring that an algorithm is “linear” is not enough. We must identify the exact observable, calculate its Fourier structure or moment dependence, and bound the accumulated error.

A useful mathematical pattern is to prove the randomized algorithm works under an ideal distribution, then isolate the properties of that distribution used by the proof. The pseudorandom generator is a replacement for those properties, not for an abstract notion of randomness.

# Almost independence and small bias

Small bias also relates to approximate k-wise independence. The probability of a prescribed pattern on k selected coordinates can be expanded using Fourier characters supported on those coordinates. If all nontrivial character biases are at most epsilon, the error of a specified pattern probability can be bounded by a multiple of epsilon. Summing over all patterns gives a total-variation error bound that grows with k.

For small fixed k, this can be very useful. For k increasing with n, the numerical dependence matters. One should not write “epsilon-biased implies epsilon-almost k-wise independent” without defining which distance is used and how the constants depend on k.

There is also a converse direction in some settings: k-wise independent distributions have zero bias for all nonempty parities involving at most k coordinates, but they need not control characters with larger support. The even-parity example with three bits already demonstrates the missing guarantee.

# A Fourier estimate with no hand waving

Let a function have a Fourier expansion consisting of a constant term and coefficients multiplying nonempty parity characters. Under uniform random bits, every nonempty character has expectation zero, so the expected value is just the constant coefficient.

Under an epsilon-biased distribution, each such character has expectation with magnitude at most epsilon. By the triangle inequality, the change in the function's expectation is bounded by epsilon times the sum of the absolute values of its nonconstant Fourier coefficients.

This derivation is short but potent. It tells us exactly which functions are fooled well: those with controlled Fourier absolute weight. It also tells us why a uniformly small bias parameter alone may not be enough for a large family of tests. The number and sizes of coefficients can dominate the error budget.

# What derandomization actually proves

An explicit seed generator is valuable because it turns a probabilistic existence argument into a finite, structured search. But the statement of correctness belongs to the pair consisting of the generator and the class of tests it fools. Without the class of tests, “pseudorandom” is incomplete terminology.

For parity observers, small-bias spaces deliver the intended approximation with far fewer random bits than full independence. For nonlinear observers, extra Fourier bounds, bounded-independence constructions, or stronger pseudorandom generators may be needed. The mathematical lesson is that the most useful form of randomness is often not maximum randomness, but exactly enough randomness to support the argument one is trying to make.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `x in {0,1}^n`, `a in {0,1}^n`, let `chi_a(x)=(-1)^{a dot x}`. A distribution `D` is `epsilon`-biased when
\[
|\mathbb E_D\chi_a(X)|\le\epsilon\quad\text{for every }a\ne0.
\]
If `f(x)=sum_a \hat f(a)chi_a(x)`, then
\[
|\mathbb E_D f-\mathbb E_U f|\le\epsilon\sum_{a\ne0}|\hat f(a)|.
\]
The uniform distribution over `{000,011,101,110}` is pairwise independent but has `chi_(111)(X)=+1` always. Small-bias constructions can use `O(log n + log(1/epsilon))` random seed bits (with constants and explicitness subject to the construction). Small support does **not** imply small total variation distance from full uniformity.

### Exercises with answers

1. Which Fourier character is exempt from the small-bias condition? **Answer:** the constant character `a=0`.
2. What is the bias of the parity of all three bits in the even-parity example? **Answer:** one.
3. Does epsilon bias fool every bounded function with error epsilon? **Answer:** not without further Fourier norm or test-class restrictions.
4. Why does a seed of length `O(log n)` imply polynomial support? **Answer:** at most `2^{O(log n)}=n^{O(1)}` strings are generated.

### Reading and source notes

- [Naor and Naor, Small-Bias Probability Spaces](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/bias.pdf), explicit short-seed constructions and applications.
- [O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/boolean-analysis/), Fourier characters, influences, and pseudorandomness context.
