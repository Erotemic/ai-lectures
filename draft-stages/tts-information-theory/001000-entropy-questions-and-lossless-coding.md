# From Information to Compression: Entropy, Questions, and Codes

**Track:** Information Theory: From Questions to Communication  
**Lecture:** 001000  
**Preparation:** Probabilities summing to one, powers and logarithms.  
**Companion:** Entropy, prefix codes, Kraft inequality, and source coding.

<!-- BEGIN SPOKEN LECTURE -->

You are about to open a box that contains one of three colored cards. The red card is inside half the time; blue and green each appear one quarter of the time. Before opening the box you know these probabilities, but not the color. You may ask questions with yes-or-no answers. What is the most efficient strategy for discovering the card?

Ask first whether it is red. If the answer is yes, we are finished after one question. If the answer is no, ask whether it is blue, and the remaining possibilities are settled. Half the time we ask one question. Half the time we ask two. The average is one and a half questions. Compare this with an unhelpful strategy that asks about blue first: a blue card takes one question, but red and green each take two, giving an average of one and three quarters. The shape of the uncertainty tells us where to ask.

This example suggests that information can be measured by the number of binary distinctions needed to resolve uncertainty. But it also raises a problem: how can we assign a numerical amount of information to a single outcome, and how do we average information across outcomes of different probabilities?

Suppose an outcome has probability one half. Learning that it happened selects one of two equally likely possibilities; we call its information content one bit. If an outcome has probability one quarter, learning it corresponds to selecting one of four equally likely possibilities and carries two bits of surprise. If its probability is one eighth, the surprise is three bits. A rule that fits all three cases is the negative base-two logarithm of the probability.

Why a logarithm? Imagine two independent events. If the first has probability one quarter and the second one eighth, their joint probability is one thirty-second. We would like the information learned from both to equal the sum of the information learned from each: two bits plus three bits, or five bits. The logarithm converts multiplying independent probabilities into adding information. This is a mathematical motivation, not the claim that all information in ordinary speech can be counted by how surprised a person feels.

Rare events carry more information when they occur. A daily event that happens with probability ninety-nine percent is not a big surprise. The event of the same type happening only once in a million trials would be. Yet the rare event does not necessarily make the overall experiment highly uncertain. To measure uncertainty **before** the box is opened, we average the surprise of possible outcomes, weighted by their probabilities. That average is called **Shannon entropy**.

For the colored cards, red occurs with probability one half and contributes one half times one bit. Blue and green each have probability one quarter and contribute one quarter times two bits. Add them: one half plus one half plus one half gives one and a half bits. This matches the expected number of binary questions in the strategy we found. The match is exact here because the outcome probabilities fit neatly into halves and quarters. In general an entropy can be fractional even when any individual question yields only a whole yes-or-no answer.

Entropy belongs to a probability distribution, not simply to the number of labels on a box. Three equally likely cards would have entropy log base two of three, about one point five eight five bits—slightly more than our red-blue-green distribution. A box with a card that appears ninety-nine percent of the time and two very rare alternatives has much less uncertainty despite still having three possible labels. The outcome count tells us how many labels exist; the probabilities tell us how difficult it is, on average, to identify the actual one.

There is a simple upper bound. For N possible outcomes, entropy is at most log base two of N, with equality when the outcomes are equally likely. Uniform probabilities maximize uncertainty because none of the possible labels is favored. This fact can be proved using the concavity of the logarithm or the nonnegativity of relative entropy, which we will develop later. You need not interpret the maximum as a law of physical disorder; it is a precise statement about a finite probability distribution.

One might ask whether a highly unlikely outcome contains infinite information. If an event has exactly zero probability in the chosen model, its negative logarithm is not a finite number. But it never occurs under that model, so when computing the expected entropy we adopt the convention that a zero-probability outcome contributes zero to the average. If such an outcome is actually observed, that is evidence the model was wrong or incomplete, not an observation we should quietly squeeze into an existing finite-information budget.

The unit called a bit depends on logarithm base two. If we use natural logarithms instead, information is measured in **nats**. Changing the logarithm base merely changes the unit by a constant factor. What matters are the probability weights and the principle that independent pieces of information add.

What does entropy **not** tell us? It does not tell us whether the content is important or true. A random series of coin flips can have high entropy while being useless as a message to someone who wanted a weather forecast. A highly structured theorem might have low surprise to a mathematician who already knows its proof, yet enormous intellectual significance. Shannon's quantity measures statistical uncertainty relative to a specified probabilistic description. It deliberately does not measure semantic value.

The question strategy also has a hidden assumption. We treated each yes-or-no answer as equally costly, and we allowed any question whose truth divides the possible outcomes. If some questions are expensive or forbidden, a new optimization problem appears. Likewise, the card distribution must be known or estimated; if probabilities drift, the best question tree may change.

There is an additional payoff from thinking in questions. When we encode a symbol as a string of zeros and ones, each digit is like one binary answer. A code word of length three makes three binary distinctions. If we give short words to frequent symbols and long words to rare symbols, we can reduce the average number of digits. This leads from entropy to compression and the rigorous limits of what a prefix code can achieve.

The main idea is now in place. Probability describes uncertainty. Negative logarithms describe the information of a realized event. Averaging those logarithms gives entropy, a numerical measure of the uncertainty before we know what happens. What began as a game with three cards will turn into a theory of codes, channels, statistics, and the limits of reliable communication.

# How uncertainty becomes a code

The same mathematical uncertainty that determines the number of useful questions also determines how efficiently symbols can be represented as binary strings.

Suppose a tiny weather station sends one of four symbols each hour. The possible messages are clear, cloudy, rainy, and snowy. Clear appears half the time, cloudy a quarter, and rainy and snowy an eighth each. You want to transmit the messages using zeros and ones. Must every symbol use two binary digits because there are four symbols?

If we insist on fixed-length words, yes: two binary digits can distinguish four possibilities. But the symbols are not equally common. We could give clear the code zero, cloudy the code one zero, rainy the code one one zero, and snowy the code one one one. The frequently sent clear condition needs one digit; the rare snow condition needs three. Over many messages, that saves space.

Can the receiver read a stream of these words without spaces or commas? Yes. When the next digit is zero, it recognizes clear immediately. When the next digit is one, it knows to read more. If the second digit is zero, that means cloudy. If the first two digits are both one, a third distinguishes rainy from snowy. No complete code word is the beginning of another code word. This is the defining property of a **prefix code**.

Prefix codes are convenient because decoding can proceed from left to right without looking ahead indefinitely. A tree makes the rule visible. Each binary digit chooses left or right. The symbols occupy leaves, not internal nodes. A code word ending at a leaf cannot be the beginning of a longer code word, because a leaf has no descendants.

What is the average word length in this example? Clear contributes half a message times one bit: one half. Cloudy contributes one quarter times two bits: another half. Rainy and snowy each contribute one eighth times three bits: three eighths each. Sum them and the expected length is one and three quarters bits per symbol. That is better than the fixed two bits.

Now calculate the entropy of the source. The information contents are one bit for clear, two for cloudy, and three for each rare outcome. Weighted by the same probabilities, entropy is also one and three quarters bits. Our prefix code has achieved that lower limit exactly. The coincidence comes from the probabilities being powers of one half, so the ideal bit lengths are whole numbers.

Is there a way to make every symbol's code one bit long? No. A one-bit prefix code has only two distinct leaves. Four possible symbols cannot each be represented by a different one-bit word. This counting argument generalizes. Picture a complete binary tree whose leaves lie at various depths. A leaf at depth one occupies half of the possible infinite paths through the tree; a leaf at depth two occupies a quarter; a leaf at depth three occupies an eighth. Because prefix-code leaves do not overlap, the total fractions must not exceed one. In symbols, the sum of two raised to minus each code length is at most one. That is **Kraft's inequality**.

Kraft's inequality is both a necessary condition for binary prefix codes and, for finite collections of positive integer lengths, a sufficient one. If the length fractions fit into the unit capacity of a binary tree, there exists a prefix code with those lengths. It is a packing theorem for code words. The inequality does not say which word represents which symbol or whether a particular code is optimal for a given source.

How do we find a good prefix code when the probabilities are not tidy powers of one half? One method, due to David Huffman, repeatedly joins the two least probable symbols or groups into a single branch. The resulting binary tree gives a prefix code with minimum **expected length among binary prefix codes for individual symbols**, assuming the probabilities are known and the symbol costs are all one bit per branch. We can understand the greedy step: in an optimal binary tree, two least probable leaves can be placed as siblings at maximum depth. Merging them reduces the problem to a smaller code tree. Repeat until there is one root.

The phrase 'among prefix codes' matters. Compression algorithms can exploit blocks of symbols, relationships between symbols, or other structure. A Huffman code applied separately to each symbol is not automatically the best conceivable compressor for a long message.

A general lower bound ties coding to entropy. For any binary prefix code, the average code length is at least the source entropy. One proof uses Kraft's inequality and a mathematical inequality called relative entropy nonnegativity. The intuitive reason is that a code tree cannot allocate too many short names. A short name spends a large fraction of the available binary paths. If all probable symbols could have names shorter than their negative log probabilities, the available paths would be overbooked.

There is also a simple upper bound. Give symbol x a code length equal to the ceiling of minus log base two of its probability. The resulting lengths satisfy Kraft's inequality, and each length is strictly less than its ideal information length plus one. Therefore there exists a prefix code whose expected length lies between entropy and entropy plus one bit per symbol, for positive probabilities. Huffman coding can do at least as well among single-symbol prefix codes.

The extra one bit may be a large overhead for a very low-entropy source. One remedy is to encode blocks. Instead of assigning a separate word to each weather observation, treat a block of n observations as one large symbol. If the observations are independent and identically distributed, its entropy is n times the original entropy. Applying the entropy-plus-one bound to blocks gives average bits per original observation less than entropy plus one over n. That overhead tends to zero as the block length grows. This is one gateway to the source coding theorem.

The qualifications are essential. We have been speaking about the distribution of a symbol or an independent block source, not claiming that any individual finite file can be compressed. There is no one-to-one compressor that makes every possible n-bit string strictly shorter. A simple counting argument forbids it: there are more n-bit strings than there are binary strings of length less than n. Compression works by using unequal code lengths, giving shorter representations to some messages while making others at least as long or longer.

Real messages also contain memory. Tomorrow's weather is not independent of today's. A model that assigns probabilities to sequences can exploit those dependencies. The relevant limiting measure of information may be an **entropy rate** rather than the entropy of one isolated observation. A compressing algorithm that learns repeated patterns can outperform a code that ignores temporal correlations. But it cannot conjure predictable structure from a sequence that truly has none under the model.

Compression has a companion problem: what happens when the data must cross a noisy communication link? A source code tries to remove predictable redundancy. A channel code intentionally adds structured redundancy so that errors can be detected or corrected. The two goals are not contradictory. They solve different problems. The first asks how few bits represent the source; the second asks how reliably those bits survive transmission.

Think again about the weather station. By giving the common message a short name, we reduced average usage from two bits to one and three quarters. The achievement was not a clever trick with four labels. It was a consequence of probability, a tree-packing constraint, and a precise lower bound. That combination makes compression a mathematical subject rather than just a collection of file formats.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Part I

For a finite alphabet \(\mathcal X\), probability mass function \(p(x)\), and \(p(x)>0\), self-information in bits is \(\imath(x)=-\log_2 p(x)\). Shannon entropy is
\[
H(X)=-\sum_{x\in\mathcal X}p(x)\log_2 p(x),\qquad 0\log 0:=0.
\]
For \(p=(1/2,1/4,1/4)\), \(H(X)=\tfrac12\cdot1+2\cdot\tfrac14\cdot2=1.5\) bits. A decision tree with code lengths \((1,2,2)\) achieves expected cost 1.5 binary questions. For \(N\) possible labels, \(0\leq H(X)\leq\log_2 N\), with the maximum at the uniform distribution. When \(X,Y\) are independent, \(H(X,Y)=H(X)+H(Y)\), but without independence the joint entropy need not equal the sum.

### Exercises and solutions

1. **Fair coin.** What is the entropy of one fair coin flip? **Solution:** one bit.
2. **Certainty.** What is the entropy of a random variable whose outcome is known with probability one? **Solution:** zero bits.
3. **Surprise.** What is the self-information of an event of probability \(1/16\)? **Solution:** four bits.
4. **Three-card strategy.** Compute the expected number of questions if blue is asked about first. **Solution:** \((1/4)\cdot1+(3/4)\cdot2=1.75\).

### Reading and attribution

- MIT OpenCourseWare, 6.441 *Information Theory*, 2010, Lecture 1, introduction and entropy: https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/lecture-notes/.
- MIT OpenCourseWare, 6.441, 2016, Chapter 1, entropy and divergence: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- The three-card question-tree example is original worked exposition.

### Part II: How uncertainty becomes a code

For a binary instantaneous (prefix-free) code with lengths \(\ell_i\in\mathbb{Z}_{>0}\), Kraft inequality states \(K=\sum_i2^{-\ell_i}\leq1\). Conversely, any finite integer lengths with \(K\leq1\) can be realized by a binary prefix code. The expected length is \(L=\sum_i p_i\ell_i\).

For \(p=(1/2,1/4,1/8,1/8)\) and codewords \((0,10,110,111)\), \(L=\tfrac12+\tfrac12+\tfrac38+\tfrac38=7/4\). Also \(H(p)=7/4\) bits. The code is optimal since no prefix code can have \(L<H(p)\).

**Lower bound proof.** Let \(q_i=2^{-\ell_i}/K\). Then \(D_2(p\Vert q)=\sum_i p_i\log_2(p_i/q_i)=L+\log_2 K-H(p)\geq0\), so \(L\geq H(p)-\log_2 K\geq H(p)\). The divergence inequality follows from \(\ln z\leq z-1\), including the usual support conventions.

**Upper bound.** Set \(\ell_i=\lceil-\log_2 p_i\rceil\) for positive \(p_i\). Then \(2^{-\ell_i}\leq p_i\), so Kraft holds, and \(\ell_i<-\log_2 p_i+1\), hence \(H(p)\leq L<H(p)+1\) for a source with more than one positive-probability symbol. Coding blocks of n independent symbols gives per-symbol overhead below \(1/n\) if a separate block prefix code is constructed.

### Exercises and solutions

1. **Decode.** Using codewords \(0,10,110,111\), decode `0101110`. **Solution:** `0|10|111|0`, or clear, cloudy, snowy, clear.
2. **Kraft test.** Can three symbols all have code length one? **Solution:** no, since \(3\cdot2^{-1}=3/2>1\).
3. **Average length.** If the four weather events become equally likely, what is the average length of the displayed variable-length code? **Solution:** \((1+2+3+3)/4=9/4\) bits, worse than a fixed two-bit code.
4. **Compression impossibility.** Why cannot a lossless code shorten every n-bit message? **Solution:** fewer than \(2^n\) bitstrings have length less than n, so an injective encoding of all \(2^n\) inputs into shorter strings cannot exist.

### Reading and attribution

- MIT OpenCourseWare, 6.441 *Information Theory* (2010), Lectures 5–6, Kraft inequality and Huffman coding: https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/lecture-notes/.
- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory*, 2nd ed., 2006, Chapters 5–6; course reading map: https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/readings/.
- The four-symbol weather station and explicit prefix calculations are original worked exposition.
