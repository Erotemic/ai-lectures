# Information Through Noise: Dependence, Data Processing, and Channel Capacity

**Track:** Information Theory: From Questions to Communication  
**Lecture:** 003000  
**Preparation:** Conditional probability, entropy, and finite distributions.  
**Companion:** Mutual information, data processing, noisy channels, and coding capacity.

<!-- BEGIN SPOKEN LECTURE -->

A coin is placed under one of two cups, left or right, chosen with equal probability. You cannot see the placement. A friend gives you a signal: the word 'left' or 'right'. But your friend is unreliable. Three quarters of the time the signal names the correct cup, and one quarter of the time it names the wrong one. The signal clearly helps. Yet it does not tell you exactly where the coin is. How much information has it given you?

Before hearing the signal, the coin's location has two equally likely possibilities, so its entropy is one bit. After hearing 'left', your best estimate is that the coin is under the left cup with probability three quarters and under the right with probability one quarter. The same uncertainty remains after hearing 'right', with the labels exchanged. The entropy of that posterior distribution is about point eight one one bits. Your uncertainty fell from one bit to about point one eight nine bits **less** than before.

That reduction is called **mutual information**. It measures how much knowing one random variable reduces uncertainty about another on average. Unlike the surprise of a single outcome, mutual information belongs to the **joint distribution** of two variables. It is zero when the variables are independent, and positive when observations of one change the probability distribution of the other in a systematic way.

We need to make the ingredients precise. Let X represent the true cup and Y the reported cup. The pair X and Y has a joint probability distribution. If each cup is initially equally likely, and the reporting error is independent of the placement with probability one quarter, then the probability of 'left' placement and 'left' signal is three eighths. The probability of 'left' placement and 'right' signal is one eighth. By symmetry the other two possibilities have probabilities one eighth and three eighths. All four joint probabilities add to one.

The **joint entropy**, H of X and Y, is the uncertainty in the pair considered as one combined random outcome. It can be calculated by taking the average negative logarithm of those four joint probabilities. But it has a more revealing decomposition: joint entropy equals entropy of X plus the remaining uncertainty in Y **given** X. If we learn the true placement first, the only randomness in the report comes from the error. That conditional entropy is the binary entropy of one quarter, about point eight one one bits. Thus the joint entropy is about one point eight one one bits.

The **chain rule** for entropy is a bookkeeping identity with a conceptual payoff. To specify both X and Y, we may describe X and then Y using what we already learned about X. Or we can describe Y first and then X given Y. Both descriptions concern the same pair, so H of X plus H of Y given X equals H of Y plus H of X given Y. This identity is useful in statistics, compression, and communication theory because it makes 'what is left to learn' a mathematical quantity.

Mutual information can now be written in two equivalent ways: entropy of X minus entropy of X given Y, or entropy of Y minus entropy of Y given X. In our symmetric example, the result is one minus the binary entropy of one quarter, approximately point one eight nine bits. The signal's usefulness is not one full bit merely because it has two possible words. Some of its variation comes from error rather than knowledge of the true cup.

Let's test the extremes. If the friend is always correct, the report determines the placement; conditional entropy becomes zero and mutual information is one bit. If the friend is correct exactly half the time and errors are independent of the true placement, the report is a fair coin toss unrelated to the cup; mutual information is zero. If the friend is always wrong, the report still determines the cup, because you can reverse the label. Mutual information returns to one bit. Information measures how well two variables are linked, not whether the link uses labels you personally prefer.

Another subtle point: mutual information is **symmetric**. How much the signal tells us about the cup is numerically the same as how much the cup tells us about the signal. Causal influence is not symmetric. The friend sees the placement and produces a signal, not the other way around. Mutual information alone cannot determine which variable caused the other, or whether both are driven by a third variable. That is why a high statistical dependency should not be advertised as proof of a mechanism.

One formula for mutual information is an average of log ratios. For each joint outcome, compare its actual joint probability with what the joint probability would be if X and Y were independent. Take the log of the ratio and average under the actual joint distribution. A pair occurring more often than independence predicts contributes positively; one occurring less often contributes negatively. The overall average cannot be negative. This is an instance of relative entropy, which we will examine directly in another lecture.

Now add a second unreliable messenger. The first friend sends a report Y; the second friend hears Y, occasionally mishears it, and passes along a new message Z. The second friend's message depends only on Y and on additional independent noise, not on direct access to the hidden coin. Can Z tell us more about X than Y did?

No. The **data processing inequality** says that when information flows in a Markov chain X to Y to Z, mutual information between X and Z cannot exceed mutual information between X and Y. Extra randomization can erase distinctions; it cannot reconstruct distinctions that were absent from its input. A deterministic function of Y is a special case: taking a summary of a report cannot increase its information about X.

A proof can be heard as two ways of revealing the same three variables. First write how much the pair Y and Z tells us about X by starting with Y. Once Y is known, Z adds no further information about X, by the Markov assumption. Thus the pair tells us exactly what Y tells us. Now reverse the order, starting with Z and then revealing Y. Learning Y after Z cannot have negative information. Therefore Z alone cannot tell us more than the pair, which tells us no more than Y. That is the essence of the inequality.

The assumption matters. If the second messenger secretly knows the cup's true location, or receives an independent clue about it, then Z is not generated from Y alone. The inequality has not been violated; the communication diagram was incomplete. Mathematical conclusions are only as strong as the conditional-independence statements behind them.

For a concrete numerical variation, suppose each messenger independently flips the label with probability one quarter. The resulting signal Z disagrees with the true cup when exactly one messenger flips. That probability is one quarter times three quarters, plus three quarters times one quarter, or three eighths. The second signal has an error probability closer to one half and therefore carries less mutual information than the first. In a binary symmetric system, noise compounded with noise has washed out some knowledge.

This is a more powerful idea than the simple slogan that 'information gets lost'. An algorithm can discard irrelevant detail while preserving all information relevant to a particular target. For instance, if the task is only to know whether a recorded temperature exceeds a threshold, a one-bit summary may retain everything needed for that particular decision even though it loses most information about the exact temperature. The data processing inequality compares information about a **specified** variable, not an informal total value of a dataset.

Conditional entropy asks what remains unknown after observing something. Mutual information asks how much the observation helped. And data processing explains a limit on how processing an observation can improve knowledge without introducing new evidence. These are the connections through which information theory enters statistical prediction, feature engineering, sensor systems, and the theory of noisy communication.

# From a noisy observation to reliable communication

We have measured how much a noisy observation can tell us. Now turn the question around: if we may choose a long sequence of signals, can we use an unreliable observation process to convey messages reliably?

Imagine a radio link that sometimes flips a transmitted bit. You send zero; the receiver occasionally hears one. You send one; the receiver occasionally hears zero. Suppose each transmitted bit is flipped independently with probability one tenth, and suppose the receiver knows that error rate. How can you communicate reliably through a device that you know will sometimes change the message?

One answer is repetition. To send zero, transmit zero three times. To send one, transmit one three times. If the receiver hears zero zero one, it takes the majority vote and decides zero. When a single bit is flipped, the original message is recovered. Two or three flips defeat the majority. The probability of a decoding error is the probability of exactly two flips plus the probability of three flips.

At a flip probability of point one, exactly two flips occur with probability three times point one squared times point nine. Three flips occur with probability point one cubed. Add them and the error rate is point zero two eight. Repetition has reduced the chance of mistaking a bit from ten percent to two point eight percent. It works by adding deliberate redundancy: one information bit occupies three uses of the channel.

But three transmissions for one information bit is expensive. The **rate** of the repetition code is one third information bit per channel use. And simply repeating everything three times does not tell us the highest reliable rate that the channel could support. Can a more sophisticated code use less redundancy while still driving the error probability down?

To ask the question precisely, information theory models the link as a **binary symmetric channel**. Each use accepts one binary input, produces one binary output, and flips the input with a fixed probability p between zero and one. Channel uses are independent, and the flip probability does not depend on whether the input was zero or one. Those are modeling assumptions. Wireless interference and burst errors can violate them, so a code designed for this model needs further analysis before deployment in a real system.

For p equal to one half, the receiver's output is an independent fair bit, no matter what was sent. There is no information about the input in the output. The reliable communication rate is zero. For p equal to zero, the channel is perfect and one bit per use is possible. For p equal to one, the channel flips every bit deterministically; the receiver can simply invert each received bit. Reliable communication is again possible at one bit per use. An error rate of one hundred percent is not a loss of information when the error rule is known and perfectly predictable.

The amount of information a single output Y carries about a single input X depends on the input distribution. If we use zeros ninety-nine percent of the time, there is little uncertainty in what we intended to send. A fair input uses the channel most effectively under this symmetric model. For a fair input, the output is also fair; it contains one bit of entropy. But even after knowing the input, the output remains uncertain because of the flip. That conditional uncertainty is the binary entropy of p. Therefore input-output mutual information is one minus the binary entropy of p.

For the binary symmetric memoryless channel, this is not merely the information conveyed by one particular signaling scheme. It is also the channel's **capacity**: the highest asymptotic information rate at which a long sequence of messages can be transmitted with a decoding error probability tending to zero as block length grows. Capacity is measured in bits of message per channel use. At p equal to point one, binary entropy is about point four six nine, and capacity is approximately point five three one bits per use.

Compare that with our threefold repetition rate of one third. We traded considerable rate for a quick reduction in one-bit error probability. The capacity tells us that, in principle, long block codes can operate at rates much nearer point five three one while making the probability of decoding a whole message arbitrarily small, under the stated channel assumptions. That is much stronger than sending the same bit repeatedly.

Here is the core intuition. A message consists of many bits, and an encoder maps each possible message to a longer binary **codeword**. A noisy channel moves that codeword to a nearby received string, usually by flipping roughly a fraction p of its bits over a long block. If the codewords are spaced sufficiently far apart, the decoder can decide which codeword was most likely sent. A code must balance two competing demands: pack many codewords into the space of all binary strings, yet leave enough room around each codeword to survive typical noise.

The word 'typical' is important. With n independent flips of probability p, the fraction of flipped positions is usually close to p when n is large. There are still rare noise patterns that flip many more positions. Reliable coding does not guarantee that **every** possible pattern of flips is corrected. Instead, the probability of the uncorrectable patterns tends toward zero. This distinction is at the heart of probabilistic communication theory.

One can outline why a rate below capacity is achievable. Choose long codewords suitably, for example through a random coding argument. A received string is likely to resemble the transmitted codeword in the sense described by the channel probabilities. When the number of possible codewords is not too large relative to the available typical output patterns, a decoder can identify the right codeword with probability approaching one. The full proof is more delicate; it carefully controls collisions and decoding errors, but the packing picture gives its direction.

There is also a **converse**. Suppose someone claims to send at a rate higher than capacity with vanishing decoding error. Fano's inequality relates the decoder's remaining uncertainty about the original message to its error probability. If the error probability vanishes, the receiver must learn almost all of the message's information. But the channel can transfer at most its capacity per use in the appropriate asymptotic sense. Those two demands contradict a rate above capacity. Thus capacity is both an achievable limit from below and a barrier from above.

This theorem has a specific scope. It concerns a discrete memoryless channel under a chosen error criterion and arbitrarily long blocks. At finite block lengths, there is a tradeoff among rate, error probability, latency, and code complexity. With strict delay limits, the asymptotic capacity is not the whole engineering answer. Likewise, a channel with memory, feedback, changing noise, or a power constraint requires its own precise model; the formula one minus binary entropy is not universally applicable.

We can now distinguish the two directions of coding. When we compress a source, we exploit predictability to use fewer bits on average. When we protect the compressed bits against channel errors, we add carefully chosen redundancy. There are mathematical theorems explaining when source coding and channel coding can be designed separately for memoryless idealizations. Real systems make additional compromises for computation, buffering, delay, and robustness.

The paradox at the beginning is resolved. An unreliable physical link can carry reliable information, not by making each individual transmission perfect, but by spreading each message across many channel uses in a structured way. Error probabilities, entropy, and a counting problem about the space of possible codewords tell us how much reliable communication is possible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Part I

For finite random variables \(X,Y\) with joint mass \(p(x,y)\),
\[
H(X,Y)=-\sum_{x,y}p(x,y)\log_2p(x,y), \quad H(X\mid Y)=\sum_y p(y)H(X\mid Y=y).
\]
The chain rule states \(H(X,Y)=H(Y)+H(X\mid Y)=H(X)+H(Y\mid X)\). Mutual information is
\[
I(X;Y)=H(X)-H(X\mid Y)=H(Y)-H(Y\mid X)=\sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{p(x)p(y)}.
\]
For a fair bit X and independent error bit E with \(P(E=1)=\varepsilon\), let \(Y=X\oplus E\). Then \(H(X)=H(Y)=1\), \(H(X\mid Y)=h_2(\varepsilon)\), and \(I(X;Y)=1-h_2(\varepsilon)\), where \(h_2(p)=-p\log_2p-(1-p)\log_2(1-p)\). For \(\varepsilon=1/4\), \(h_2(1/4)\approx0.811278\), giving \(I\approx0.188722\) bits.

**Data processing proof.** If \(X\to Y\to Z\) is a Markov chain, \(I(X;Z\mid Y)=0\). Apply the chain rule for mutual information in two orders:
\[
I(X;Y,Z)=I(X;Y)+I(X;Z\mid Y)=I(X;Z)+I(X;Y\mid Z).
\]
As conditional mutual information is nonnegative, \(I(X;Z)\le I(X;Y)\).

With two independent bit flips of probability \(1/4\), the compound crossover probability is \(2(1/4)(3/4)=3/8\), and \(I(X;Z)=1-h_2(3/8)\approx0.045566\) bits.

### Exercises and solutions

1. **Independent clues.** If X and Y are independent, what is \(I(X;Y)\)? **Solution:** zero, because \(H(X\mid Y)=H(X)\).
2. **Perfect inversion.** If Y is always the opposite of a fair bit X, how much mutual information is there? **Solution:** one bit; Y determines X exactly.
3. **Chain rule.** Explain why \(H(X,Y)\) is at least \(H(X)\). **Solution:** the difference is \(H(Y\mid X)\ge0\).
4. **A hidden clue.** Why is the data processing inequality inapplicable if Z also observes X directly? **Solution:** generally \(X\) and \(Z\) are not conditionally independent given \(Y\); the claimed Markov chain fails.

### Reading and attribution

- MIT OpenCourseWare, 6.441 *Information Theory* (2010), Lectures 1–2, entropy identities and data processing: https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/lecture-notes/.
- MIT OpenCourseWare, 6.441 (2016), Chapter 2, mutual information and data processing: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- The two-messenger cup experiment and complete numerical calculation are original examples.

### Part II: From a noisy observation to reliable communication

A binary symmetric channel \(\mathrm{BSC}(p)\) has \(Y=X\oplus E\) with independent \(E\sim\mathrm{Bernoulli}(p)\). Its capacity is
\[
C=\max_{P_X}I(X;Y)=1-h_2(p)\quad\text{bits per channel use},\qquad 0\le p\le1,
\]
with capacity achieved by the uniform input distribution. The formula is symmetric about \(p=1/2\) and gives \(C=1\) at \(p=0\) and \(p=1\).

For a repetition-3 majority decoder, \(P_{\mathrm{err}}=\binom32p^2(1-p)+p^3=3p^2-2p^3\). At \(p=0.1\), the error probability is \(0.028\), with coding rate \(1/3\). The capacity is \(1-h_2(0.1)\approx0.531004\) bits per use.

**Asymptotic qualification.** For finite-alphabet discrete memoryless channels, the channel coding theorem identifies capacity as the supremum of rates achievable with block error probability tending to zero along increasing blocklengths. A separate finite-blocklength analysis is needed to trade error, rate, and delay. A repetition-3 scheme alone is not a proof of that theorem.

### Exercises and solutions

1. **All-noise case.** What is \(C\) for \(p=1/2\)? **Solution:** zero bits per channel use.
2. **Perfect inversion.** Why is \(p=1\) still usable? **Solution:** every bit is flipped deterministically, so invert the received bit and recover the input.
3. **Majority vote.** For \(p=0.2\), compute the repetition-3 block error probability. **Solution:** \(3(0.2)^2-2(0.2)^3=0.104\).
4. **Rates.** Can a rate exceeding \(1-h_2(p)\) guarantee vanishing block error on the same BSC under its memoryless model? **Solution:** no; it is above the channel's capacity.

### Reading and attribution

- MIT OpenCourseWare, 6.441 *Information Theory* (2010), Lectures 8–10 and 13, channel capacity and coding theorem: https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/lecture-notes/.
- MIT OpenCourseWare, 6.441 *Information Theory* (2016), Chapters 14–16, capacity and achievability: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- The repetition-code and numerical comparisons are independently calculated didactic examples.
