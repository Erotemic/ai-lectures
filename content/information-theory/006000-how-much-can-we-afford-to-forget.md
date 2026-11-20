# How Much Can We Afford to Forget?

**Track:** Information Theory: From Questions to Communication  
**Lecture:** 006000  
**Preparation:** Entropy, conditional entropy, mutual information, and block coding.  
**Companion:** Distortion functions, the rate-distortion function, and the binary Hamming example.

<!-- BEGIN SPOKEN LECTURE -->

Imagine a telescope taking a binary image of a distant star field. Each pixel records either dark or bright. The instrument can send a limited number of bits to Earth. If every original pixel has to be recovered exactly, the Shannon source coding theorem gives a lower limit on the transmission budget. But suppose the scientific question allows a small fraction of pixel values to be wrong. What compression becomes possible when the receiver is permitted to reconstruct something close to the original rather than something identical?

That word "close" changes the mathematics. Entropy alone is no longer the right answer. We must specify what errors cost, how much error is tolerable on average, and how many bits are needed under that tolerance. The subject is rate-distortion theory. It is not simply a collection of tricks for lossy audio or image files. It is a precise optimization problem about how much information one representation must retain about another.

Start with a deliberately simple source. Each pixel is an independent fair bit, zero or one with equal probability. Its entropy is exactly one bit. There is no exact lossless compression opportunity on average. Every binary image of n pixels is equally likely, and an exact decoder needs essentially n bits to identify it.

Now define the cost of a reconstructed pixel. If the decoder reproduces the bit correctly, the cost is zero. If it gets the bit wrong, the cost is one. Over a whole image we take the average fraction of incorrect pixels. This is called Hamming distortion. Notice that we are not yet talking about visual perception or astronomy; we have stipulated a mathematical cost function, and every theorem will be relative to that choice.

Let D be the allowed expected fraction of wrong pixels. At D equal to zero, exact recovery is required and the rate is one bit per pixel. At D equal to one half, the decoder can ignore the input entirely and always output zero: half the fair source bits are wrong on average. That requires zero information about the actual image. Between these extremes, a beautiful formula appears. The minimum asymptotic rate, in bits per source pixel, is one minus the binary entropy of D.

Take D equal to one tenth. Binary entropy at one tenth is about point four six nine. So the required rate is about point five three one bits per pixel. If we can tolerate ten percent mistakes on average, an independent fair binary source can be represented using only a little over half a bit per pixel, in the limit of long blocks. At D equal to one quarter, the minimum falls to about point one eight nine bits per pixel. There is a large saving, but the source is not being reproduced exactly.

Before deriving the formula, separate three things. The encoder sees an actual source block. It emits a finite index, a compressed message. The decoder reads that index and produces a reconstruction block. The distortion is measured between the original block and that reconstruction. A rate-distortion code is allowed to assign the same index to many distinct original blocks, because different originals may be acceptably approximated by one reconstruction.

What limits the rate from below? Think about the uncertainty the decoder still has about an original source bit after seeing its reconstruction. If the reconstruction is correct almost always, very little uncertainty remains. If it is no better than a coin toss, almost all uncertainty remains. Mutual information measures how much knowledge of the reconstruction reduces uncertainty about the original.

For a fair source bit X, entropy is one. The mutual information between X and its reconstruction, which we may call X-hat, equals one minus the conditional entropy of X given X-hat. Thus the smaller that conditional entropy, the more information must have crossed from original to reconstruction.

Introduce an error indicator E that equals one when the reconstructed bit differs from the original and zero otherwise. Once we know the reconstruction and E, the original bit is determined: it is either the reconstruction itself or its opposite. Therefore the uncertainty of X given X-hat equals the uncertainty of E given X-hat. Conditional entropy cannot exceed unconditional entropy, so this is at most the entropy of E. If the probability of error is D, the entropy of E is the binary entropy of D. We conclude that the reconstruction must preserve at least one minus h of D bits of mutual information about the fair source bit.

That already looks like the rate-distortion formula. But a compression algorithm works on long blocks, and perhaps correlations among reconstruction errors could beat this single-letter argument. We need the block version. Begin with n independent fair source bits, so the whole block has n bits of entropy. The uncertainty of the whole block after seeing the reconstruction cannot exceed the sum of the separate per-position uncertainties. Each one is at most the binary entropy of that position's error probability. Finally, by the concavity of binary entropy, the average of those entropies is at most the binary entropy at the average error rate.

In symbols, the whole reconstruction preserves at least n times one minus h of D bits of information. A message consisting of at most nR transmitted bits cannot convey more than nR bits of information. The data processing inequality gives the needed bridge: information about the source can only be lost as we pass from source through compressed index to reconstruction. So R must be at least one minus h of D. This is the converse. Every coding method, clever or primitive, obeys it under our assumptions.

It remains to show that the limit is achievable. Here a geometric picture is particularly clear. There are two to the n possible binary images of length n. Fix one candidate reconstruction, a string of n bits. Which original images is it an acceptable approximation for? Those that differ from it in no more than roughly nD positions. They form a Hamming ball around the reconstruction.

How large is that ball? Choose which positions are wrong. For exactly k errors there are n choose k possibilities; summing from zero up to nD gives the number of originals that a single reconstruction can cover. For a fixed D strictly between zero and one half, the exponential growth rate of that sum is two to the n times h of D.

Compare the ball to the full space. A typical reconstruction covers a fraction roughly two to minus n times one minus h of D of all possible originals. Thus it takes approximately two to the n times one minus h of D reconstruction centers to cover enough of the space. The logarithm of that number is the compressed bit budget. It matches the converse.

To turn the picture into a proof of achievable expected distortion, choose many candidate reconstructions independently and uniformly at random. For any fixed original image, the chance that one random reconstruction falls within its allowed Hamming ball is the fraction we just computed. The chance that none of M random reconstructions falls within the ball is one minus that fraction, raised to the Mth power. If M is two to the nR and R is strictly larger than one minus h of D, that failure probability tends rapidly to zero.

The encoder can then select a nearby reconstruction and transmit its index. The decoder outputs the selected center. When there is no sufficiently close center, the encoder uses a predetermined fallback index, and we bound the distortion of that rare event. Averaging over the random codebook shows that some deterministic codebook achieves expected distortion approaching D. Taking a slightly smaller target distortion inside the construction accommodates a strict prescribed limit. The two proof directions meet at one minus h of D.

There is a delightful reversal here. For channel coding, we spaced codewords apart so noise would not make their received neighborhoods confusing. For lossy source coding, we deliberately allow a reconstruction neighborhood to stand for many original strings. One problem packs distinguishable messages into a noisy space. The other covers source strings with acceptable approximations. The very same Hamming-ball counting appears, but one problem uses it to prevent overlap and the other to permit overlap.

Now return to the telescope. A ten percent pixel error rate is not necessarily scientifically acceptable. One missed faint star could be more consequential than a hundred incorrect background pixels. We would then change the distortion function: perhaps a missed bright object incurs a higher penalty, or perhaps errors near an object boundary matter more. The theorem does not choose the distortion rule for us. It calculates the best rate once the source model and acceptable cost are specified.

The general mathematical definition makes that explicit. Let X be a source symbol and X-hat a possible reconstruction. Choose a distortion cost d of X and X-hat. Now imagine all possible probabilistic ways to produce reconstructions from originals, called test channels. Restrict attention to those whose expected distortion is no larger than D. Among them, minimize the mutual information between the original and the reconstruction. For finite-alphabet memoryless sources with additive per-letter distortion, that minimum is the rate-distortion function.

The word "test channel" can be misleading. It is not necessarily a noisy physical link. It is a mathematical conditional distribution describing the joint behavior of originals and good reconstructions. For the fair binary source under Hamming distortion, taking X-hat to be X independently flipped with probability D realizes mutual information one minus h of D. Together with the converse, that shows the single-letter minimum equals the formula we derived through covering.

For biased sources the answer changes. If zeros are extremely common and a ten percent error rate is allowed, always outputting zero may already satisfy the distortion budget, giving zero required bits. The formula one minus h of D cannot be blindly reused because the source is no longer fair. For a nonbinary source, a different distortion function, or data with memory, the optimization can look different still.

Nor should the asymptotic rate be confused with the length of an actual image file. The theorem assumes large blocks and a specified probabilistic source. A real codec has finite blocks, headers, computational limits, and source mismatch. It may exploit spatial correlations the independent-pixel model excludes. Some file formats optimize for human perception; others preserve measurements relevant to downstream analysis. Calling one of them "optimal" without specifying its distortion and source model would be meaningless.

Rate-distortion theory teaches us an unusually sharp way of thinking about compromise. The question is not vaguely how much quality must be sacrificed to save bandwidth. It is: under a declared probability law and a declared loss function, what information must necessarily survive the compression map? The binary example shows how a nonzero error allowance changes an exact recovery limit into a smooth tradeoff. It also shows why compression and communication, although they use similar counting arguments, solve different problems. How much may we forget? Once the meaning of forgetting has been made mathematical, information theory can answer.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For iid \(X_i\sim\mathrm{Bernoulli}(1/2)\), Hamming distortion \(d(x,\widehat x)=\mathbf1\{x\ne\widehat x\}\), and average distortion \(\frac1n\sum_i d(X_i,\widehat X_i)\), the rate-distortion function is
\[
R(D)=\begin{cases}1-h_2(D),&0\le D\le1/2,\\0,&D\ge1/2.\end{cases}
\]
For a general finite-alphabet memoryless source and bounded additive distortion,
\[
R(D)=\min_{P_{\widehat X\mid X}:\,\mathbb E[d(X,\widehat X)]\le D}I(X;\widehat X).
\]
The minimization is over conditional pmfs, not over physical communication channels.

**Converse.** Let a compressed index \(J\) have at most \(2^{nR}\) values and let \(\widehat X^n\) be its decoded reconstruction. Write \(D_i=P(X_i\ne\widehat X_i)\) and \(\frac1n\sum_iD_i\le D\le1/2\). Then
\[
\begin{aligned}
nR&\ge H(J)\ge I(X^n;\widehat X^n)\\
&=n-H(X^n\mid\widehat X^n)\\
&\ge n-\sum_iH(X_i\mid\widehat X_i)\\
&= n-\sum_iH(E_i\mid\widehat X_i)\\
&\ge n-\sum_i h_2(D_i)\\
&\ge n\bigl(1-h_2(D)\bigr).
\end{aligned}
\]
The equality involving \(E_i=X_i\oplus\widehat X_i\) uses a bijection given \(\widehat X_i\). The final inequality uses concavity and monotonicity of \(h_2\) on \([0,1/2]\).

**Achievability for the fair binary case.** The Hamming ball size
\[
V_n(D)=\sum_{k=0}^{\lfloor nD\rfloor}\binom nk
\]
satisfies \(\frac1n\log_2V_n(D)\to h_2(D)\) for fixed \(0<D<1/2\). Choose \(M=\lceil2^{nR}\rceil\) reproduction codewords independently uniformly. For every source sequence, the probability none lies within distortion \(D\) is \((1-V_n(D)/2^n)^M\). It tends to zero if \(R>1-h_2(D)\). Select the first acceptable codeword when possible and a fallback otherwise. Its expected distortion is at most \(D+o(1)\). For a strict distortion constraint use a slightly smaller internal \(D'\) and take the limit. Endpoints follow from direct codes.

For \(D=0.1\), \(R(D)\approx0.531004\). For \(D=0.25\), \(R(D)\approx0.188722\). Both values are measured in **bits per source symbol**.

### Exercises and solutions

1. **Two extremes.** Find \(R(0)\) and \(R(1/2)\) for a fair binary source. **Solution:** one bit per symbol and zero bits per symbol.
2. **Wrong source model.** If a source is 95 percent zeros, is always reconstructing zero acceptable at a 10 percent expected Hamming distortion budget? **Solution:** yes; expected distortion is 5 percent, so zero communication suffices.
3. **A lower bound.** Why can't a 0.3-bit-per-symbol code attain expected Hamming distortion 0.1 for independent fair bits? **Solution:** the converse requires rate at least \(1-h_2(0.1)\approx0.531\).
4. **Different costs.** Why may the binary Hamming result be unsuitable for medical images? **Solution:** equal pixel mismatches may have very different downstream consequences, so the distortion function needs to represent the intended task.

### Reading and sources

- MIT OCW 6.441 (2016), chapters 23-25, rate-distortion definitions, achievability, and evaluation: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- Cover and Thomas, *Elements of Information Theory*, second edition, rate-distortion chapters.
