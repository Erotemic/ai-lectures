# Why Typical Sequences Can Be Compressed

**Track:** Information Theory: From Questions to Communication  
**Lecture:** 004000  
**Preparation:** Finite probability distributions, logarithms, entropy, and the law of large numbers.  
**Companion:** Typical sets, the asymptotic equipartition property, and the source coding theorem.

<!-- BEGIN SPOKEN LECTURE -->

An archive contains a million readings from a sensor. A reading can be zero or one, but zeros appear three quarters of the time. A literal archive uses a million bits, one per reading. Can we store it in substantially fewer bits without losing a single reading?

It is tempting to answer by counting. There are two to the million possible binary records. They cannot all fit into a shorter fixed-length string: a million-bit record could be any one of them. But our sensor does not produce these records with equal probability. Some are enormously more likely than others. Shannon's source coding theorem exploits that distinction between what is logically possible and what is statistically typical. The proof gives us a way to think about almost every long record at once, without claiming that rare records have ceased to exist.

Let the sensor emit independent bits. Each bit is zero with probability three quarters and one with probability one quarter. We have already met the entropy of this distribution. It is about point eight one one bits per symbol. The astonishing assertion is that a very long record can be represented at a rate approaching that fraction of a bit per sensor reading. For a million readings that suggests roughly eight hundred eleven thousand bits, rather than a million, plus an overhead that becomes negligible per reading.

The word "approaching" deserves care. A single sensor reading cannot be represented by point eight one one ordinary binary digits. Even if we give zero the word zero and one the word one, both words have length one. Compression at a fractional rate comes from encoding an entire block. Correlations are not required. Even independent observations provide an opportunity when their probabilities are unequal.

Consider one particular block, say one hundred sensor readings. Its probability is the product of the individual probabilities. If the block contains seventy-five zeros and twenty-five ones, its probability is three quarters raised to the seventy-fifth power, multiplied by one quarter raised to the twenty-fifth. Its negative base-two logarithm is approximately eighty-one bits. A record with ninety-nine zeros and one one has a different probability, and therefore a different information content. The quantity that will be predictable is not the record itself, but its negative log probability divided by its length.

For the first reading, define its surprise as the negative logarithm of the probability of the observed symbol. Do that for every reading. Because the readings are independent, the surprise of the whole block is the sum of the individual surprises. And because they all have the same distribution, the average surprise of each reading is the entropy of the source.

Now invoke the law of large numbers. With probability approaching one as the block gets longer, the observed average surprise is close to its expected value. Said differently, most long blocks have probability approximately two raised to minus the block length times the entropy. The approximation is exponential: a small error per symbol becomes a multiplicative range in the probability of a whole block. We control that error by choosing a tolerance and then making the block sufficiently long.

Call a block typical when its average surprise differs from the entropy by less than our chosen tolerance. Typicality does not mean that each symbol in the block looks ordinary. A typical block may contain very surprising bits. It means that their combined information content is close to the expected total. For an independent finite-alphabet source, almost all the probability mass eventually lies in this typical set. This is a version of the asymptotic equipartition property.

There are two facts to hold together. The typical set has probability approaching one. Yet each typical block has probability close to two to minus n times H, where n is the block length and H is the source entropy. How many such blocks can there be? If all their probabilities are roughly two to minus nH, and together they account for roughly unit probability, there must be roughly two to the nH of them.

The precise bounds are useful. A typical block has probability at least two to minus n times H plus the tolerance, so the typical set contains at most two to the n times H plus the tolerance blocks. For the other direction, typical blocks have probability at most two to minus n times H minus the tolerance. Since their total probability approaches one, there must be at least approximately two to the n times H minus the tolerance blocks. The two exponents pinch together as the tolerance tends to zero.

This is why we can compress. Imagine listing only the typical blocks, in an agreed order. Every typical block is identified by an index in a table of size approximately two to the nH. The index needs approximately nH bits. We have replaced the impossible task of encoding every possible block briefly with the manageable task of encoding the high-probability collection briefly.

But the archive must be lossless. What happens to an atypical block? A real compressor cannot discard it without warning. One construction starts its encoded record with a flag. If the block is typical, the flag says so and the rest is its short index. If not, the flag says "raw" and the rest stores the original block in full. Both cases are decoded exactly. Since atypical blocks become rare, their contribution to expected length can be made small relative to n. The flag itself costs one bit per block, which is negligible per symbol for large n.

There is a closely related theorem for fixed-length block codes that permit a vanishing probability of decoding failure. We can assign short indices to all typical blocks and accept that an atypical block may not be recovered. The probability of this failure tends to zero. This achieves rates arbitrarily near entropy with a fixed number of bits per block, but it is not an exactly lossless code at each finite length. The distinction between an asymptotically vanishing error and literal zero error is important.

Can we compress even further, below entropy? At first the counting argument seems to say nothing, because perhaps we could select a smaller collection that still catches nearly all the probability. But the typical-set bounds prohibit this. Suppose a decoder can recognize at most two to the nR different blocks, where R is smaller than H. Almost all blocks have individual probabilities no larger than about two to minus n times H minus a small tolerance. The total probability caught by only two to the nR such blocks is therefore at most about two to the n times R minus H plus the tolerance. That tends to zero if R is genuinely below H. Any decoder working at that rate misses almost every sufficiently long block, not just a tiny fraction.

That is the converse for fixed-length almost-lossless compression. For exact variable-length prefix coding, a different counting tool does the same work. Kraft's inequality limits how many short codewords can coexist, and the average prefix-code length cannot be smaller than the entropy. It is a one-block inequality, not merely an asymptotic claim.

There is also an almost embarrassingly simple existence proof for a prefix code near the entropy. Given a possible whole block with probability p, assign it a codeword length equal to the smallest integer not below minus log base two of p. The Kraft sum of these requested lengths is no more than the sum of all probabilities, which is one. A prefix code with those lengths therefore exists. The length of every codeword exceeds its ideal information content by less than one bit. Averaging gives an expected block length below the block entropy plus one bit. For independent readings, the block entropy is n times the single-symbol entropy. Divide by n, and that extra one bit becomes one divided by n.

Notice what we have proved without building a practical compressor. There exists a family of codes achieving an average rate approaching H. We have not proved that a particular table lookup, arithmetic coder, or implementation reaches that rate under memory and computation constraints. The counting argument and the prefix-length construction concern mathematical codebooks. They say what is possible, and they give design principles; they do not remove engineering work.

Let us revisit the one-million-reading sensor. Its most probable record is the all-zero record, but even that probability becomes tiny as the record grows. Typicality does not mean a handful of individually likely records. It means an exponentially large collection of records whose individual probabilities are tiny but comparable on the logarithmic scale. For our three-quarter-zero source, the typical collection occupies an exponentially small fraction of the full set of two-to-the-million records. Yet it carries almost all of the source's probability mass.

Now consider a fair coin instead. Its entropy is one bit per toss. Every length-n sequence has exactly probability two to minus n. The typical set is essentially the entire space. There is no smaller collection that captures nearly all the probability. The same proof that explains compression of the biased sensor also explains why uniform independent bits cannot be compressed on average without additional structure.

Another misunderstanding is that short codewords must go to entire records that contain mostly zeros. More zeros can make a record more probable under this model, but a good block code reflects the probability of the whole block. The counting theorem does not prescribe a unique ordering or a unique encoding. Huffman coding, arithmetic coding, and other approaches implement different versions of the same pressure: devote fewer symbols to more probable events while making the code unambiguously decodable.

There is also a limit to this model. We assumed the bits were independent and their distribution known. If the sensor changes behavior over time, yesterday's entropy need not describe tomorrow's data. If the source has memory, single-symbol entropy can overestimate the true compressible rate because past readings help predict future ones. We will encounter entropy rates when studying such processes. The typical-set argument can be extended, but it requires conditions different from the independent case proved here.

What makes the source coding theorem intellectually powerful is its combination of two arguments that fit exactly. The law of large numbers tells us what the overwhelming majority of emitted records look like in probability. Counting tells us how many binary labels can identify them. From those two facts we get both a coding construction and a limit no code can beat. Compression is possible because probable outcomes occupy only a portion of the logical possibility space. Entropy measures the exponential size of that portion.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(X_1,\ldots,X_n\) be iid on a finite alphabet \(\mathcal X\), with pmf \(p\) and entropy \(H(X)=\mathbb E[-\log_2 p(X)]\). Zero-probability symbols are omitted from the support. Define
\[
A_{\epsilon}^{(n)}=\left\{x^n:\left|-\frac1n\log_2 p(x^n)-H(X)\right|<\epsilon\right\}.
\]
The weak law implies \(P(X^n\in A_{\epsilon}^{(n)})\to1\) for every \(\epsilon>0\). For any typical \(x^n\),
\[
2^{-n(H+\epsilon)}<p(x^n)<2^{-n(H-\epsilon)}.
\]
Thus
\[
(1-\delta_n)2^{n(H-\epsilon)}<|A_{\epsilon}^{(n)}|<2^{n(H+\epsilon)},\qquad \delta_n=P(X^n\notin A_{\epsilon}^{(n)})\to0.
\]
A fixed-rate encoder with \(\lceil n(H+\epsilon)\rceil\) bits can index all typical blocks and fail only on atypical ones. Conversely if \(R<H-2\epsilon\), a decoder with at most \(2^{nR}\) outputs succeeds with probability at most \(\delta_n+2^{-n(H-\epsilon-R)}\to0\) for large \(n\). The encoded-message cardinality, not the encoder's construction, gives the bound.

For **exact** variable-length prefix coding, set \(\ell(x^n)=\lceil-\log_2 p(x^n)\rceil\) for each positive-probability block. Kraft's inequality is satisfied because \(\sum_{x^n}2^{-\ell(x^n)}\le\sum_{x^n}p(x^n)=1\). Consequently
\[
H(X^n)\le\mathbb E[\ell(X^n)]<H(X^n)+1=nH(X)+1.
\]
This construction concerns a block alphabet of size \(|\mathcal X|^n\), not an efficient executable codebook.

For \(p(0)=3/4\), \(p(1)=1/4\),
\[
H(X)=h_2(1/4)=-\tfrac34\log_2(3/4)-\tfrac14\log_2(1/4)\approx0.811278.
\]

### Exercises and solutions

1. **Fair source.** How many length-100 sequences are typical for a fair binary source? **Solution:** every sequence has surprise exactly 100 bits, so all \(2^{100}\) sequences satisfy any positive typicality tolerance.
2. **Block-prefix overhead.** What average bits per source symbol are guaranteed by the simple Shannon lengths for blocks of size 200? **Solution:** strictly less than \(H(X)+1/200\).
3. **Converse estimate.** If the source entropy is 0.81 bits/symbol, what happens to success probability of a fixed-length code at 0.6 bits/symbol as block size grows? **Solution:** it tends to zero for the iid model.
4. **Model change.** Does the proof automatically apply if every bit equals the preceding bit? **Solution:** no. Those bits are dependent; the single-symbol iid argument is not the correct model.

### Reading and sources

- MIT OCW 6.441 (2010), source coding and typical-sequence lectures: https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/lecture-notes/.
- MIT OCW 6.441 (2016), source coding and the asymptotic equipartition property: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- Cover and Thomas, *Elements of Information Theory*, second edition, chapters on the asymptotic equipartition property and source coding; bibliographic listing via the OCW reading map.
