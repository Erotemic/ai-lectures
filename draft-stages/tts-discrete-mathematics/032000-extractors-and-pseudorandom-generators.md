# 032000 — Randomness Extractors: Recovering Usable Random Bits

**Track:** Discrete Mathematics. **Background:** entropy, concentration, finite fields, hash functions and probability distributions. **Central question:** when can a weak source be transformed into bits that behave almost uniformly?

<!-- BEGIN SPOKEN LECTURE -->

# Random does not mean uniformly random

Imagine a physical sensor producing bits. Its output varies, but the zeros occur much more often than the ones. Or imagine a computer process that chooses uniformly from a secret set of a million possible strings, while the entire space of possible bit strings is vastly larger. In both cases the output has uncertainty, but it is not uniformly distributed.

Many algorithms assume access to independent fair bits. The question is whether we can take a weak random source and produce shorter bits that are nearly uniform. A randomness extractor provides a precise answer, but only after we specify how much uncertainty is guaranteed in the source and what extra randomness the extractor may use.

The most useful elementary measure is min-entropy. A random variable has min-entropy at least k if no particular outcome has probability larger than two to the minus k. This measures the difficulty of predicting the single most likely outcome. It is stronger than simply requiring a large Shannon entropy, and it is the right kind of promise for several extractor constructions.

# An information-theoretic obstruction

There is a reason extraction cannot be universally deterministic. Suppose a fixed function compresses n-bit strings to one output bit. At least half the inputs share the same output. An adversary can choose a source uniformly from that large preimage. The source has substantial min-entropy, yet the output is constant.

This proves that no single deterministic function can extract a nearly fair bit from every arbitrary high-min-entropy source unless the source family has more structure or the min-entropy promise is extremely strong. The extractor must use additional assumptions, multiple independent sources, or a short independent random seed.

A seeded extractor is a function of two inputs: the weak source and a seed of genuinely uniform bits independent of that source. It aims to make the joint distribution of seed and output close to the distribution of an independent uniform seed and uniform output. Such an extractor is called strong. Including the seed in the guarantee means it is safe to reveal which seed was used without destroying the statistical closeness of that one extraction.

# Universal hashing is an extractor

Consider a family of hash functions mapping n-bit strings to m-bit strings. The family is two-universal if, for any two distinct inputs, the chance that a randomly selected hash function sends them to the same output is at most two to the minus m.

A simple example uses a uniformly random binary matrix with m rows and n columns. Multiply the source vector by the matrix over the field of two elements. Distinct inputs have a difference vector that is nonzero, and each random row has an independent fair dot product with that difference. Thus the full collision probability is exactly two to the minus m.

The leftover hash lemma says that if the source has min-entropy k and the seed chooses a two-universal hash function independently, the output together with the seed is statistically close to uniform. One standard bound on total variation distance is one half times the square root of two raised to the power m minus k.

The lesson is quantitative. If we try to extract all k bits of guaranteed entropy, that bound is weak. If we leave a margin and extract m equal to k minus twice a positive security parameter, the distance becomes exponentially small in that margin. We spend some entropy to obtain a rigorous uniformity guarantee.

# A numerical example

Suppose a source has at least one hundred bits of min-entropy. Use an independent universal-hash seed to produce eighty output bits. The leftover hash bound is one half times the square root of two to the minus twenty. That is two to the minus eleven. Thus the seed-output pair is within about one part in two thousand in total variation distance of ideal independence and uniformity.

If we instead request ninety-eight output bits from the same source, the bound becomes one quarter. That is a poor guarantee. The source has not lost entropy; the theorem is telling us that near-total extraction cannot in general give very small statistical error without stronger conditions.

Notice that the simple random-matrix family uses many seed bits: m times n. This proves the information-theoretic principle but is not a seed-efficient implementation. More sophisticated extractor constructions use much shorter seeds. The efficiency of the seed, the computational cost of extraction, and the amount of source entropy consumed are separate engineering and mathematical questions.

# Extractors versus generators

A pseudorandom generator has a different promise. Starting from a short uniform seed, it produces a longer output intended to look random to some specified class of tests. In cryptography that often means no efficient algorithm can distinguish the output from uniform with significant advantage, under a computational hardness assumption.

An extractor cannot create information-theoretic entropy from nothing. Its output length must be supported by the uncertainty already present in the source, with some loss for statistical accuracy. A computational pseudorandom generator, by contrast, can stretch a short seed into a long sequence that is unpredictable to efficient observers, but the resulting distribution still has at most the seed's entropy. It is not statistically close to uniform on all long strings.

The same word pseudorandom sometimes appears in combinatorics for deterministic objects that imitate random behavior for a restricted set of statistics, such as small-bias sample spaces or expanders. Again the test class must be named. Passing a collection of Fourier tests is not identical to statistical closeness against every possible event.

# Independence and reuse are real assumptions

An extractor guarantee can fail if the seed is correlated with the weak source. Similarly, a strong extractor does not automatically justify reusing a fixed seed forever on arbitrarily correlated future samples. The theorem applies to a specified joint distribution with its independence hypotheses.

This is especially important when building randomness pipelines. A real sensor's entropy may drift. An estimated min-entropy rate is not the same as a proven bound under all operating conditions. Correlations between successive sensor readings matter, as do adversarial influences. A statistical test suite can find some defects but cannot certify the min-entropy of an arbitrary unknown physical process from one finite sample.

The information-theoretic goal is precise: a weak source with a verified min-entropy guarantee, an independent seed, and an extractor with a proved variation-distance bound. Only then can downstream algorithms safely replace ideal bits by extracted bits, paying an explicit amount in their error probabilities.

# Randomness as a resource with a budget

The surprising point is that even severely nonuniform randomness can yield almost fair bits if its unpredictability is quantified and we are willing to use a seed. Universal hashing gives an accessible proof, while sophisticated extractors improve seed length and computational efficiency.

A useful design question is not simply whether the output looks random. It is: random according to which test, under which entropy guarantee, with what error, and relative to which seed? Those four questions turn vague randomness claims into mathematics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A source X on `{0,1}^n` has `H_infty(X)=-log_2 max_x P[X=x]>=k`. A family H of maps to `{0,1}^m` is two-universal if for distinct x,x', `P_{h in H}[h(x)=h(x')]<=2^{-m}`. The leftover hash lemma gives, for independent uniform seed H,
\[
\Delta((H,H(X)),(H,U_m))\le\frac12\sqrt{2^{m-k}},
\]
where U_m is independent uniform, Delta is total variation distance, and the source is arbitrary subject to the entropy bound. (The standard collision-probability calculation yields this form.) For `k=100,m=80`, the bound equals `2^{-11}`. For `m=98`, it is `1/4`.

**Random-matrix family:** choose `A` uniformly from `F_2^{m x n}`. If `x != x'`, let `v=x-x' !=0`; each independent random row r has `r dot v` uniform. Then `P[Av=0]=2^{-m}`. The seed here is mn bits; this is a correctness example, not an optimal seed-length construction.

**No-go argument:** a fixed deterministic `f:{0,1}^n -> {0,1}` has an output fiber containing at least `2^{n-1}` inputs. A source uniform on that fiber has min-entropy at least `n-1` but constant f-output. This does not rule out deterministic extraction from structured source classes or multiple independent sources.

### Exercises with answers

1. For min-entropy k=120, what is the leftover-hash bound for m=100? **Answer:** `2^{-11}`.
2. Why can't a general deterministic extractor work for all high-entropy sources? **Answer:** an adversary can choose the source to lie entirely in one large output fiber of the fixed function.
3. Do pseudorandom generators increase Shannon entropy beyond their seed length? **Answer:** no; deterministic transformations cannot increase entropy.
4. Does strong extraction permit a correlated seed? **Answer:** no; independence is part of the stated guarantee.

### Reading and source notes

- [Nisan and Ta-Shma, Extracting Randomness: A Survey and New Constructions](https://doi.org/10.1006/jcss.1997.1546), extractor constructions and resource tradeoffs.
- [Dodis et al., Fuzzy Extractors: How to Generate Strong Keys from Biometrics and Other Noisy Data](https://eprint.iacr.org/2003/235), seeded extraction and related security models.
- [Vadhan, Pseudorandomness (lecture monograph)](https://people.seas.harvard.edu/~salil/pseudorandomness/), min-entropy, leftover hashing, extractors and pseudorandom generators.
