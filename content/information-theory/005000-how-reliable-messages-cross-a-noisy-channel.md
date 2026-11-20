# How Reliable Messages Cross a Noisy Channel

**Track:** Information Theory: From Questions to Communication  
**Lecture:** 005000  
**Preparation:** Entropy, mutual information, elementary probability, and the idea of a typical set.  
**Companion:** Random codebooks, typical decoding, capacity achievability, and the Fano converse.

<!-- BEGIN SPOKEN LECTURE -->

Imagine a wire that flips one of every ten transmitted bits, independently at random. If you send a thousand-bit document by placing its bits directly onto the wire, there is almost no chance that the document arrives completely unchanged. At least one error is overwhelmingly likely. How, then, could anyone claim that this wire supports reliable communication?

The answer is not to make each physical bit more reliable. It is to change what counts as a message. Instead of treating a transmitted bit as the message, we treat an entire long string of transmitted bits as a codeword that represents one message out of a large collection. The receiver does not need to reconstruct each original transmission symbol as an independent obligation. It needs to identify which codeword was sent. If the codewords are organized well, even an imperfect received string can identify its intended message with very high probability.

Our model is a binary symmetric channel. Each transmitted zero emerges as a one with probability one tenth, and each transmitted one emerges as a zero with the same probability. The flips are independent across uses, and the receiver knows the model. This assumption is strong, but it gives us an exact theorem to study before considering more realistic noise.

The capacity of this channel is one minus the binary entropy of the flip probability. At ten percent flips it is about point five three one bits per use. The introductory account of information theory may already have told us that formula. The mathematical question now is why the number is achievable and why it is an upper limit. Those are separate proofs.

Suppose we use the wire n times. We want to communicate one of M equally likely messages, each represented by one of M length-n codewords. The information rate is log base two of M divided by n. If M equals two to the four-tenths n, the rate is point four bits per channel use. That is below the channel capacity. The channel coding theorem says there are codebooks and decoders for which the probability of decoding the entire message incorrectly tends to zero as n grows.

For a moment, forget decoding and consider only the noise pattern. It is a string of n bits that says which positions flipped. Because flips are independent, the number of flipped positions is concentrated near one tenth of n. A typical noise string has about ten percent ones. The number of such patterns grows roughly like two to the n times the binary entropy of one tenth, or about two to the point four six nine n.

This is an extraordinary compression of possibilities. There are two to the n logically possible flip patterns, but almost all the noise probability lies in a set of size roughly two to the point four six nine n. When we transmit one codeword, the receiver is therefore likely to observe a string in an associated cluster of about that many typical-noise outputs. Thinking geometrically, the cluster is close to a Hamming ball around the codeword: the strings differing from it in about ten percent of their coordinates. We must be careful about a ball of radius ten percent n versus a thin typical shell, but they have the same relevant exponential growth rate for this case.

The ambient space has two to the n possible received strings. If each message's likely output cluster occupies about two to the point four six nine n of them, a rough packing calculation leaves room for about two to the point five three one n clusters. That is where the capacity formula begins to appear. But the drawing of nonoverlapping circles is only intuition. Real clusters overlap, and the channel can occasionally produce an atypical error pattern. The proof has to bound how often these failures cause confusion.

Here is a way to do that using random codebooks. Select each codeword independently and uniformly from the space of all n-bit strings. A received string arrives. The decoder looks for a codeword whose difference from the received string resembles a typical noise pattern. If exactly one candidate passes, it outputs that message. If none or several pass, it declares an error or follows an agreed tie rule.

Two bad events can happen. First, the true noise pattern may not be typical. The law of large numbers says this event becomes rare for long blocks. Second, another codeword may accidentally look compatible with the received string. That is where the size of the typical noise set controls confusion.

Condition on the transmitted codeword and the actual received string. Every other randomly chosen codeword is independent and uniform. The chance that one random rival lands in the received string's typical-noise neighborhood is approximately the neighborhood size divided by two to the n. On the exponential scale, that is two to minus n times one minus binary entropy of the flip probability. For our ten-percent wire it is roughly two to minus point five three one n.

We have about two to the nR rival codewords. The union bound says the chance that any one of them is a false typical candidate is no greater than their number times the chance for one rival. This quantity decays exponentially whenever R is below one minus the noise entropy, provided we leave a small tolerance in the typical-set estimates. Add the rare event that the true noise itself was atypical, and the average decoding error tends to zero.

That is the heart of achievability. We chose a codebook at random, and we proved that the average error probability over the random choice becomes small. Therefore at least one deterministic codebook has error no greater than that average. The proof establishes existence. It does not tell an engineer how to build a fast decoder for the resulting code, and it does not insist that randomly selected codewords are the best practical design.

There is a subtlety about the meaning of average error. The most straightforward random-coding argument averages both over equiprobable messages and over channel noise. One could demand that every message have small error probability, not just the average. For symmetric models, one can often remove a small number of bad codewords, sacrificing a negligible portion of the rate, to control the maximum error. But the distinction needs to be stated; a guarantee under one error criterion is not automatically a guarantee under all criteria.

Now reverse the question. Could an ingenious code exceed point five three one bits per use while still decoding almost perfectly? The converse proof answers without inspecting the codebook. Let W be the uniformly chosen message, X the n transmitted symbols, and Y the n received symbols. The decoder observes Y and produces an estimate of W. If the decoder's error probability is tiny, the remaining uncertainty about W after seeing Y should also be tiny compared with the total message information.

Fano's inequality turns that expectation into a bound. If the message has M equally likely choices and the probability of error is P, then the conditional entropy of W given the received block is no more than one bit plus P times log base two of M. The one-bit term comes from accounting for whether the decoder was wrong, and the second term accounts for the remaining possibilities when it was wrong. If P tends to zero, nearly all the log M message bits must have been conveyed to the receiver.

There is a second inequality from the channel itself. The message is converted to a transmitted codeword before the channel produces its output. All influence of W on the received block passes through that transmitted block, so data processing tells us that mutual information between W and Y cannot exceed mutual information between X and Y. The memoryless property then bounds that latter information by n times the single-use capacity.

Combining the bounds gives a simple inequality: one minus P, times log base two of M, is no greater than n times capacity plus one. If P tends to zero, and we divide by n and let n increase, the communication rate cannot exceed capacity. It does not matter how clever the encoder, whether its codewords look random, or whether the decoder is computationally extravagant. The information bottleneck is in the channel model itself.

Observe the structural similarity to source coding. For compression, typical outputs occupy a smaller-than-possible set, and the number of labels needed to cover that set determines the rate. For communication, typical noise patterns create clusters around codewords, and the number of clusters that can be distinguished determines the rate. In both cases probability tells us what is typical and counting tells us what can be labeled. But the direction is different. Source coding removes redundant representation. Channel coding inserts carefully organized redundancy so a receiver can correct uncertainty introduced by the link.

The two operations are compatible under the familiar idealized separation theorem. If a memoryless source produces H bits of information per source symbol and the channel carries C reliable bits per use, then the rough budget is H source bits of essential information for every C channel uses of information-bearing capacity. With a suitable source-to-channel use ratio and large blocks, source compression followed by channel coding can attain the optimal asymptotic tradeoff under the appropriate assumptions. Low latency, delay-sensitive distortion, and mismatch between source and channel may make joint designs more attractive in applications.

What should the rate not be confused with? A communication rate of point four bits per use does not mean every use transports a fraction of a particular message bit. One message is encoded across the entire block. Nor does asymptotically vanishing block error mean that a finite block can be made infallible. On a channel where every output sequence has some positive probability, even an excellent code can receive a misleading pattern. As block length grows, its probability can diminish; it is not literally eliminated by the coding theorem.

Our one-in-ten flip wire remains noisy. The channel coding theorem does not repair it physically. It demonstrates that the space of possible long received records contains enough statistical structure to support reliable distinctions among exponentially many messages. Achievability says there is a way to place the messages in that space. The converse says no placement can transmit information faster than the channel allows. A noisy link becomes reliable not because noise disappears, but because the code uses enough coordinated redundancy to make the intended message recoverable with high probability.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a binary symmetric memoryless channel \(Y_i=X_i\oplus E_i\), with \(E_i\overset{iid}{\sim}\mathrm{Bernoulli}(p)\), define \(h_2(p)=-p\log_2 p-(1-p)\log_2(1-p)\). The capacity is
\[
C=\max_{P_X}I(X;Y)=1-h_2(p).
\]
For \(p=0.1\), \(h_2(p)\approx0.468996\) and \(C\approx0.531004\).

**Random coding outline.** Choose \(M=\lfloor2^{nR}\rfloor\) codewords independently and uniformly from \(\{0,1\}^n\). Decode to the unique codeword whose XOR with the received word lies in a typical set \(A_\epsilon^{(n)}\) for the noise distribution. With \(P(E^n\notin A_\epsilon^{(n)})\to0\) and \(|A_\epsilon^{(n)}|\le2^{n(h_2(p)+\epsilon)}\),
\[
\mathbb E_{\text{codebook}}P_e\le P(E^n\notin A_\epsilon^{(n)})+(M-1)2^{-n(1-h_2(p)-\epsilon)}.
\]
This tends to zero for \(R<1-h_2(p)-\epsilon\), hence all \(R<C\) are achievable by taking a sufficiently small \(\epsilon>0\). Duplicate independently selected codewords are counted in the same collision bound.

**Converse.** For uniform message \(W\in\{1,\ldots,M\}\), decoder \(\widehat W(Y^n)\), and average error \(P_e\), Fano gives
\[
H(W\mid Y^n)\le h_2(P_e)+P_e\log_2(M-1)\le1+P_e\log_2M.
\]
The Markov structure \(W\to X^n\to Y^n\) and memorylessness imply
\[
I(W;Y^n)\le I(X^n;Y^n)\le \sum_{i=1}^n I(X_i;Y_i)\le nC.
\]
Thus \((1-P_e)\log_2 M\le nC+1\), so \(P_e\to0\) forces \(\limsup_n(\log_2 M)/n\le C\). The proof uses an asymptotically vanishing average block-error criterion, not a finite-block zero-error guarantee.

### Exercises and solutions

1. **A useless channel.** What is the capacity at crossover probability \(p=1/2\)? **Solution:** zero, since output is independent of input.
2. **Inverting the output.** What is the capacity at \(p=1\)? **Solution:** one bit per use because the output determines the input exactly after inversion.
3. **Rate versus capacity.** At \(p=0.1\), is 0.4 bits/use strictly below capacity? **Solution:** yes, because \(C\approx0.531\).
4. **Where the limit appears.** Which step of the achievability proof fails when \(R>C\)? **Solution:** the union bound on false typical codewords no longer tends to zero; the converse shows that no other scheme with vanishing error can beat capacity.

### Reading and sources

- MIT OCW 6.441 (2010), capacity and channel coding theorem lectures: https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/lecture-notes/.
- MIT OCW 6.441 (2016), discrete memoryless channels and coding theorems: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- Cover and Thomas, *Elements of Information Theory*, second edition, chapters on channel capacity and random coding.
