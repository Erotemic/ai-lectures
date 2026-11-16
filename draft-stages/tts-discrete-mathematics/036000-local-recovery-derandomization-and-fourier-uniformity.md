# Local recovery, derandomization, and Fourier uniformity

<!-- BEGIN SPOKEN LECTURE -->

# Local recovery, derandomization, and Fourier uniformity

## Local Correction and List Decoding: Recovering Information from Few Queries

Suppose a message is encoded into a very long codeword. Some positions are corrupted. Traditional decoding asks for the entire original message. But perhaps we only need one particular bit. Must we read the whole received word to recover that one bit?

A locally decodable code answers no. Its decoder may inspect only a few codeword positions, chosen with randomness, and return a requested message symbol with high probability despite a controlled fraction of adversarial corruption. This is an algorithmic guarantee about the number of queries. It is not the same as ordinary error correction, because decoding only one symbol is the task.

The simplest convincing example is the binary Hadamard code. Its length is enormous relative to the message, but its local recovery rule is so elementary that we can derive it in a few lines. The example exposes both the strength and the cost of local decoding.

## Every possible parity becomes a codeword symbol

Take a message x consisting of k binary bits. For every binary query vector a of length k, store the parity of the coordinates where x and a both have a one. There are two to the power k possible query vectors, so the codeword has length two to the power k.

Each coordinate of the codeword is therefore a linear function of the message. These coordinates are also precisely the characters of the binary vector space that appear in Walsh-Fourier analysis. The same algebra serves both coding theory and analysis of Boolean functions.

To recover message bit i from an uncorrupted codeword, choose any query vector a. Read the encoded parity at a, and also at a plus the unit vector in direction i. Add those two parity bits modulo two. Every message coordinate other than i appears twice and cancels. The coordinate i appears once, leaving exactly the desired message bit.

This identity is true for every choice of a. That redundancy lets us randomize the queries when corruption is present.

## Why random queries defeat a fixed error pattern

Assume an adversary has corrupted at most a fraction delta of the positions in the encoded word. The adversary chooses its error locations before seeing the decoder's fresh random queries. Choose a uniformly random query vector a, and inspect positions a and a plus the i-th unit vector.

Each position is uniformly distributed over the codeword coordinates. The chance that the first query lands in a corrupted position is at most delta. The same is true of the second. By the union bound, the chance that either is corrupted is at most two delta. If neither is corrupted, the parity cancellation gives the correct bit.

Thus our two-query decoder succeeds with probability at least one minus two delta. The two error events need not be independent; the union bound requires no independence. At corruption rate one tenth, the lower bound is four fifths. The decoder uses two queries no matter how large k is.

But the codeword has exponential length. We gained query efficiency by sacrificing storage. The example does not promise a practical short code with two-query correction. Indeed there are significant lower bounds on the length of two-query locally decodable codes, which help explain why this naive construction is so large.

## Repeat for confidence, but count queries honestly

One run of the decoder has a constant chance of failure when the corruption rate is bounded below one quarter. Independent repetitions and majority voting can reduce that failure probability exponentially in the number of repetitions. Doing so increases the number of queries by the number of trials.

If the adversary can choose which positions are corrupted after seeing each fresh query, the fixed-error-pattern guarantee no longer applies. The randomized decoder assumes an error word fixed independently of its private randomness. Likewise, if corruption exceeds the stated limit, the success bound may become uninformative.

Local decoding is a statement with parameters: number of message bits, codeword length, fraction of corruption, query complexity, and success probability. Omitting those parameters turns a theorem into a slogan.

## When unique decoding is the wrong question

Now consider a received word that is very far from every codeword under the usual unique-decoding radius. There might be several plausible original messages. Instead of insisting on one answer, list decoding asks for all codewords whose distance from the received word is below a specified threshold.

The distinction is logical. A code has a minimum distance, so two distinct codewords cannot both lie too close to the same received word. Beyond half the minimum distance, uniqueness may fail. A list decoder allows several candidates and tries to keep the list short.

The Hadamard code again offers a remarkable Fourier explanation. Express the received binary word as a function taking values plus one or minus one. Each Hadamard codeword corresponds to a Fourier character. The correlation of the received word with a character measures how well that codeword agrees with it.

If the relative Hamming distance is at most one half minus epsilon, the correlation is at least twice epsilon. Thus nearby codewords correspond exactly to large Fourier coefficients.

## Parseval limits the number of candidates

The squared Fourier coefficients of a plus-or-minus-one function sum to one. Suppose every candidate codeword has correlation at least tau. Each contributes at least tau squared to that total. Therefore there can be at most one divided by tau squared candidates.

This is a strong bound. Even though the code contains two to the power k distinct codewords, only a small number can agree with an arbitrary received word significantly better than random guessing. The proof requires no sophisticated combinatorics: it is just orthogonality of characters followed by a counting inequality.

For example, if a codeword must have correlation at least one quarter, there are at most sixteen such codewords. In terms of Hamming distance, that threshold corresponds to distance at most three eighths of the code length. The bound holds even if finding the list is computationally difficult.

## Finding the heavy coefficients

An existence bound on list size is different from an efficient list-decoding algorithm. The Goldreich-Levin method shows how to locate large Walsh-Fourier coefficients using randomized oracle access, without scanning the full exponentially long codeword. Its complexity depends polynomially on the message length and the inverse threshold, under the standard query model.

This brings together two strands of ideas. Local correction recovers a selected message bit from carefully paired codeword queries. List decoding locates all messages whose Hadamard encodings correlate strongly with a received function. Both rely on linearity and parity, but one assumes enough proximity to a single intended codeword to answer a specific query, while the other allows multiple plausible codewords.

A list alone also does not tell us which candidate message was intended. Additional structure, a checksum, side information, or a stronger decoding guarantee may be necessary. No amount of clever enumeration can conjure unique information absent from the received word.

## Locality as a mathematical resource

The Hadamard construction is not a practical final answer to every storage problem. It is a reference point for asking what is possible. Can we shorten the codeword while keeping a constant number of queries? Can we tolerate more corruption? Can we recover symbols over larger alphabets? Can a decoder be locally correctable without first reconstructing the message?

More advanced locally decodable and locally correctable codes answer these questions through algebraic curves, polynomial restrictions, matching-vector families, and other constructions. The lesson from the elementary case remains: redundancy can be arranged so that a few random local observations reveal a global message symbol, and Fourier orthogonality can bound how many global explanations remain plausible.

## Small-Bias Spaces and Derandomization

Suppose an algorithm asks for n independent fair coin flips. A direct implementation needs n random bits. But perhaps the algorithm only ever examines the parity of selected groups of coordinates. In that case, asking for full independence may be wasteful.

A distribution on bit strings is called epsilon-biased if every nonempty parity has expectation close to zero when represented as a plus-or-minus-one sign. Under genuinely uniform independent bits, every nontrivial parity is perfectly balanced. Under a small-bias distribution, its bias is at most epsilon. This is a test-dependent version of pseudorandomness. The distribution is designed to fool a family of observers, not every conceivable observer.

The major achievement of explicit small-bias constructions is that a surprisingly short random seed can produce a long bit string that looks almost uniform to every linear parity test. Constructions of Naor and Naor use a seed whose length grows logarithmically with the output length and with the reciprocal error, rather than linearly with the output length.

## Fourier characters explain the definition

For a selected set of coordinates, multiply a sign of negative one for every selected one-bit. The result is positive for even parity and negative for odd parity. Such parity signs are also called Fourier characters.

Each nonempty subset has its own character. The small-bias requirement says the expectation of each nonconstant character is close to zero. In Fourier language, every nontrivial character has small correlation with the distribution. The trivial character is always one; forcing it close to zero would be nonsensical because every probability distribution has total mass one.

Why focus on characters? Because every real-valued function on the Boolean cube can be written as a linear combination of them. If a function has small total absolute Fourier weight outside the constant term, then small bias controls how much its expectation under the pseudorandom distribution can differ from its uniform expectation.

This is a meaningful guarantee, but not a universal one. An arbitrary Boolean function may have enormous total absolute Fourier weight, or may be designed explicitly to recognize the small support of the pseudorandom distribution. The Fourier expansion gives a bound, not a miracle.

## Pairwise independence is a weaker promise

Consider the four three-bit strings zero-zero-zero, zero-one-one, one-zero-one, and one-one-zero, sampled uniformly. Every individual bit is fair. Every pair of bits is jointly uniform. In fact, any parity involving one or two of the bits is perfectly balanced.

Yet the parity of all three bits is always even. The third-order parity test distinguishes this distribution from three independent uniform bits with certainty. It is pairwise independent but not three-wise independent, and it fails the small-bias definition with an error less than one because one nonempty parity has full bias.

This four-string example prevents a common confusion. Limited independence controls tests involving only a bounded number of coordinates. Small bias controls parity tests involving arbitrary numbers of coordinates. Neither promise automatically fools every nonlinear function, and their seed-length tradeoffs depend on the exact requirements.

## Support size and seed length

A generator using s uniform random seed bits produces a distribution supported on at most two to the power s outputs. If s is logarithmic in n and in one over epsilon, the support can be polynomial in n and one over epsilon.

Compare that with the two to the n possible output strings of a truly uniform distribution. When n is large, a polynomial-sized support occupies only a tiny fraction of the cube. An observer allowed to inspect the entire output string and ask “is this string in the generator's support?” can easily distinguish it from uniform.

So there is no contradiction between a very short seed and the information-theoretic impossibility of approximating the full uniform distribution in total variation with tiny support. Small-bias generators achieve a narrower, precisely stated goal. Their success comes from limiting which statistical tests need to be fooled.

This distinction is central to derandomization. Algorithms typically do not use every property of their random bits. They use specific concentration inequalities, moment identities, or low-complexity tests. Replacing full independence with a smaller pseudorandom space is valid only after identifying which of those properties the algorithm actually needs.

## How an explicit construction is used

An explicit small-bias family gives a deterministic way to list or evaluate the outputs associated with short seeds. If an algorithm's desired behavior is certified by the average of a controlled family of parity tests, we can replace an exponential search over all n-bit strings with a much smaller search over generator seeds.

For a single parity, choosing a small-bias output at random gives nearly equal chances of the two answers. For an algorithm with several parity checks, a union-bound or Fourier argument may control the overall behavior. However, simply declaring that an algorithm is “linear” is not enough. We must identify the exact observable, calculate its Fourier structure or moment dependence, and bound the accumulated error.

A useful mathematical pattern is to prove the randomized algorithm works under an ideal distribution, then isolate the properties of that distribution used by the proof. The pseudorandom generator is a replacement for those properties, not for an abstract notion of randomness.

## Almost independence and small bias

Small bias also relates to approximate k-wise independence. The probability of a prescribed pattern on k selected coordinates can be expanded using Fourier characters supported on those coordinates. If all nontrivial character biases are at most epsilon, the error of a specified pattern probability can be bounded by a multiple of epsilon. Summing over all patterns gives a total-variation error bound that grows with k.

For small fixed k, this can be very useful. For k increasing with n, the numerical dependence matters. One should not write “epsilon-biased implies epsilon-almost k-wise independent” without defining which distance is used and how the constants depend on k.

There is also a converse direction in some settings: k-wise independent distributions have zero bias for all nonempty parities involving at most k coordinates, but they need not control characters with larger support. The even-parity example with three bits already demonstrates the missing guarantee.

## A Fourier estimate with no hand waving

Let a function have a Fourier expansion consisting of a constant term and coefficients multiplying nonempty parity characters. Under uniform random bits, every nonempty character has expectation zero, so the expected value is just the constant coefficient.

Under an epsilon-biased distribution, each such character has expectation with magnitude at most epsilon. By the triangle inequality, the change in the function's expectation is bounded by epsilon times the sum of the absolute values of its nonconstant Fourier coefficients.

This derivation is short but potent. It tells us exactly which functions are fooled well: those with controlled Fourier absolute weight. It also tells us why a uniformly small bias parameter alone may not be enough for a large family of tests. The number and sizes of coefficients can dominate the error budget.

## What derandomization actually proves

An explicit seed generator is valuable because it turns a probabilistic existence argument into a finite, structured search. But the statement of correctness belongs to the pair consisting of the generator and the class of tests it fools. Without the class of tests, “pseudorandom” is incomplete terminology.

For parity observers, small-bias spaces deliver the intended approximation with far fewer random bits than full independence. For nonlinear observers, extra Fourier bounds, bounded-independence constructions, or stronger pseudorandom generators may be needed. The mathematical lesson is that the most useful form of randomness is often not maximum randomness, but exactly enough randomness to support the argument one is trying to make.

## Sharp Thresholds, Influences, and the Tribes Function

Imagine a random graph that gradually receives more edges. At very low density it is almost certainly disconnected. At high density it is almost certainly connected. Somewhere in between, the probability of connectivity rises from near zero to near one. How narrow is that transition window?

The same question arises for reliability of networks, satisfiability of random formulas, and monotone Boolean functions whose inputs are independent biased bits. Such transitions are called thresholds. A sharp threshold means the passage from unlikely to likely occurs in a narrow region, once the appropriate scale is specified. A coarse threshold means a larger relative change in the parameter is needed.

We need care with language. For a threshold near zero, an interval whose absolute width tends to zero need not be sharp relative to the threshold location. The property that at least one of n bits is one has a transition near density one over n, but its relative transition window remains of constant order. Different threshold theorems formalize sharpness in different parameter regimes.

## The derivative is a count of pivotal coordinates

Consider a monotone Boolean function. A coordinate is pivotal for a given choice of the other coordinates when changing that coordinate changes the output from false to true. Its influence under a biased product measure is the probability that it is pivotal.

Russo's formula states that the derivative of the probability of a monotone event with respect to the input density equals the sum of these pivotal probabilities. The derivative is therefore not an unrelated analytic quantity. It measures how much influence the input coordinates collectively have over the event.

This identity gives a strategy for proving sharp transitions. Show that when the event's probability is bounded away from zero and one, its total influence must be large. Then the probability curve must have a large slope and cannot remain in the middle range for long.

But the strategy needs structural assumptions. A property depending only on one selected coordinate always has probability equal to the density. Its derivative is one, no matter how many irrelevant coordinates we add. There is no increasing collective influence. The function simply ignores most of its input.

## Symmetry limits the possibility of a dictator

One way to rule out a single dominant coordinate is symmetry. If a transitive group of coordinate permutations preserves a Boolean property, no coordinate is intrinsically distinguished. Influence inequalities then imply lower bounds on total influence in nontrivial probability regimes.

For monotone transitive properties under a product measure away from the extreme endpoints, these bounds can force transition windows to shrink as the number of coordinates grows. More general sharp-threshold theorems relate coarse thresholds to approximate dependence on only a few coordinates, called juntas.

This does not say every function with many inputs has a sharp threshold. The function may genuinely depend on only one of them. Nor does it automatically apply uniformly when the density goes to zero at a rate that changes the natural scale. The location and normalization of the threshold are part of the statement.

## Build the tribes function

A particularly illuminating example divides n input bits into disjoint groups, or tribes, each containing m bits. The function is true if at least one tribe consists entirely of ones. It is an OR of ANDs, and it is monotone.

Suppose there are k tribes. A given tribe is all ones with probability two to the negative m when the input bits are unbiased. The events for distinct tribes are independent, so the probability that no tribe is complete is one minus two to the negative m, raised to the kth power. Therefore the probability of the function being true is one minus that expression.

Choose k proportional to two to the m, with the constant chosen so the event probability is near one-half. Then the function is balanced: it is neither almost always true nor almost always false. Yet each individual bit has only a small influence, because changing it matters only when every other bit in its tribe is one and no other tribe is already complete.

The influence of a specific bit is two to the power minus m plus one, multiplied by the probability that the other tribes are incomplete. There are k times m bits, so multiplying by the total number of bits gives total influence on the order of m. Since n is about m times two to the m, m is on the order of log n.

This produces a balanced monotone function whose derivative with respect to the input density grows logarithmically with n, even though no individual bit has large influence. The threshold becomes sharper as the system expands.

## Tribes demonstrate a collective effect

The tribes example illustrates why influence is the right bridge between local decisions and global thresholds. Each coordinate is rarely pivotal, but there are many coordinates. Their contributions add to a large total derivative.

The calculation also shows that small individual influence does not imply stability of the event under changes in density. An individual bit barely matters, yet a modest coordinated increase in the bias can transform the event's overall probability.

This is different from asking how the function reacts to random noise that flips a small number of bits. Noise sensitivity depends on its Fourier spectrum and on the noise model. Threshold sharpness depends on changing the bias of the input distribution. The two subjects are related through influences and Fourier analysis, but they are not interchangeable definitions.

## The significance of the junta theorem

Friedgut's junta theorem gives another side of the story. Roughly, a Boolean function with bounded total influence can be approximated in probability by a function depending on relatively few coordinates, with the number of required coordinates controlled by influence and the desired approximation accuracy.

A function with low total influence therefore has a low-dimensional explanation at the chosen measure, even if its formal input list is enormous. This helps interpret coarse threshold behavior: failure of a sufficiently sharp transition may signal that a small amount of local information has disproportionate power.

Quantitative versions depend on the bias, approximation error, and influence definitions. One should not repeat an unbiased-cube junta bound unchanged at densities collapsing toward zero or one. The technical dependence is exactly what distinguishes a useful threshold theorem from a slogan.

## Apply the framework to a network

For a random graph, each possible edge is a Boolean input and the event of connectivity is monotone. Adding an edge cannot destroy connectivity. The coordinates are symmetric under relabeling of vertices, so influence inequalities are natural tools for understanding its transition.

A full proof of the graph-connectivity threshold uses additional combinatorics. In the classical independent-edge model, isolated vertices play a decisive role near the connectivity threshold. The threshold scale is roughly log n divided by n, not simply one over n. Understanding the precise limiting probability requires counting the relevant small obstructions and showing others become negligible.

The Boolean-influence viewpoint supplies a structural explanation for why a collective transition is possible, while the graph argument identifies the location and the dominant obstruction. Sharpness and threshold location are different questions, and a serious analysis addresses both.

## A reliable checklist

When someone claims a sharp threshold, ask four things. What parameter is changing? Which probability level defines the threshold location? Is width measured absolutely or relative to that location? And what symmetry or influence theorem makes a narrow window unavoidable?

Russo's identity answers how the probability changes. The tribes function demonstrates a balanced event with logarithmically growing total influence. Junta theory explains why low influence points toward dependence on a few coordinates. Together they turn the idea of a sudden transition into a quantitative study of who can change an event and how many such pivotal opportunities exist.

## Polynomial Codes and Local Testability

Suppose a table contains one value for every point in a large finite-dimensional grid over a finite field. The table is too large to read. Someone claims that every entry is produced by a polynomial of small total degree. Can we test that claim without examining every point?

A low-degree polynomial is highly constrained. Knowing its values on well-chosen points determines many others. If the table is corrupted in some locations, the constraint can become an error-detecting code: a Reed–Muller code. The question changes from exact interpolation to a probabilistic one. If the table is far from every low-degree polynomial, will a random local check likely find a violation?

This is local testability. It should not be confused with local correction. A tester asks whether the entire table is close to some codeword; a corrector tries to recover the value of that codeword at one chosen point. The two tasks use related structure but require different analyses.

## Build the code from evaluations

Choose a finite field with q elements and m variables. For each polynomial of total degree at most d, form a word whose coordinates are its values at all q to the m points. The family of these words is the Reed–Muller code of degree d.

If d is smaller than q, the Schwartz–Zippel bound gives a simple distance guarantee. A nonzero polynomial of total degree at most d vanishes on at most a fraction d divided by q of the grid. The difference of two distinct codeword polynomials is nonzero and has the same degree bound. Therefore the two words disagree in at least a fraction one minus d over q of their positions.

The distance is what makes correction imaginable. A word close to one codeword cannot be close to another when the errors are fewer than half the minimum distance. It also supports local tests: if a word claims to be a codeword, we can sample patterns on which a low-degree restriction is easy to recognize.

## Why lines make the problem one-dimensional

Restrict a multivariate polynomial of total degree d to an affine line. Along that line it becomes a univariate polynomial of degree at most d. This gives a local test. Select a random affine line, query values of the alleged table along it, and check whether they agree with any univariate polynomial of degree at most d.

A genuine Reed–Muller codeword passes every line. If a table is far from the code, soundness theorems show that it fails a positive fraction of the tested lines under suitable parameter assumptions. The dependence on field size, degree, dimension, and testing distribution matters. There is no single universal rejection bound valid for every version of a low-degree test.

A simple instance uses the field with three elements and degree one. Three points determine whether the restriction to a line is affine. If the three values are y-zero, y-one, and y-two, the second finite difference must vanish modulo three.

## An exact three-point example

Take the polynomial x plus y on the grid of pairs over the field with three elements. Look at the line through the points with coordinates zero and one, one and two, and two and zero. Parametrize it by starting at zero and one and adding the vector one, one each time, reducing modulo three.

The polynomial values along this line are one, zero, and two. Subtract twice the middle value from the sum of the outside values. One plus two is three, which is zero modulo three. The line passes the affine test, as it must.

Now change just the middle table entry to one. The three values become one, one, and two. Their second difference is one minus two plus two, equal to one modulo three, so this line is rejected. That does not tell us how far the entire modified table is from the Reed–Muller code. It establishes an exact local witness of inconsistency.

## Correction from other points

For affine functions over the field with three elements, a particularly small correction mechanism is available. To recover the value at a chosen point, select a random nonzero direction. Query the other two points on the line, not the target point. Since an affine function has zero second difference, the target value equals twice the first queried value minus the second queried value, with arithmetic modulo three.

If neither queried position was corrupted, the reconstruction is exact even when the target position itself was corrupted. With a received word close to a fixed affine codeword, a union bound controls the probability of encountering an error in the two queried positions. Repetition can reduce the failure probability.

This does not imply that arbitrary high-degree codes admit two-query correction. It works here because degree one and field size three make the entire line relation unusually short. For larger d, more samples and stronger algebraic machinery are generally required.

## Why a local test proves anything global

The central theorem behind local testability is not the easy direction, that true codewords always pass. It is the converse: if the table passes almost all selected local constraints, then there must exist a single global polynomial close to the table.

That assertion is a local-to-global theorem. Line after line can have its own apparently good polynomial fit. The proof must show that those local fits are mutually compatible and glue to one low-degree object. Agreement theorems and robust low-degree tests quantify precisely how much compatibility is enough.

The distinction is important for applications such as probabilistically checkable proofs. A verifier samples a tiny portion of an enormous claimed proof, but the soundness theorem must rule out a globally false claim whose local checks are mostly convincing.

## What small queries buy us

Polynomial codes trade redundancy for structure. Their codewords are large, but membership is constrained by low-degree algebra. Random line restrictions turn enormous evaluation tables into familiar interpolation problems. Minimum distance guarantees codewords are separated. Local correction uses that separation and interpolation to reconstruct entries. Local testing requires an additional soundness theorem to move from sampled agreements to global closeness.

These ingredients are related, but none replaces the others. A polynomial formula by itself is not a code construction until its domain is fixed. A passing sample is not a membership certificate without a quantified rejection probability. And a corrector that works below a distance threshold cannot be used beyond that threshold by optimism alone.

The payoff is that a small amount of algebra can certify meaningful information about a vast combinatorial object. The whole table need not be read to discover whether its local patterns are compatible with a global law.

## Additive Combinatorics and Fourier Uniformity

Consider the three integers zero, one, and two. They form an arithmetic progression because the difference between neighboring terms is constant. But a subset of a much larger collection can look scattered while still containing many progressions. Additive combinatorics asks how large a set must be, or how uniformly it must be distributed, before such patterns are unavoidable.

A three-term arithmetic progression consists of x, x plus d, and x plus twice d. The common difference d may be positive, negative, or zero. The zero case produces a trivial progression, all three entries equal. Usually the existence theorem concerns a nonzero difference.

There is an exact way to count all these configurations in a finite cyclic group. Given a function that is one on the chosen set and zero elsewhere, average the product of its values at x, x plus d, and x plus twice d, over all choices of x and d. The average equals the number of ordered progressions divided by the square of the group size.

So the question becomes an analytic one: how can we estimate a trilinear average?

## Frequencies test uniformity

A finite Fourier transform decomposes a function on a cyclic group into additive characters. Each frequency asks whether the function has a bias toward a particular rotating phase. A uniformly distributed set should have a large average value at frequency zero and small Fourier coefficients at all other frequencies.

The three-term progression count has a concise Fourier formula. Sum over frequencies the square of the Fourier coefficient at that frequency times the coefficient at negative twice that frequency. The zero-frequency term is the cube of the density of the set. Every nonzero frequency describes a departure from the behavior expected of an independent random selection of the same density.

For example, work modulo five and take the set zero, one, two. There are five ordered three-term progressions if the zero-difference cases are included: three trivial progressions and the two orientations of zero, one, two. The normalized progression average is five twenty-fifths, or one fifth. Its density is three fifths, whose cube is twenty-seven one hundred twenty-fifths. The two numbers are close but not equal. The difference is the contribution from nonzero Fourier frequencies.

This example is small enough that the distinction between trivial and nontrivial progressions cannot be ignored. In a large group, the number of trivial progressions grows only linearly with the group size, while random-looking nontrivial progressions grow quadratically.

## The dichotomy behind Roth's theorem

Roth's theorem states that a subset of the positive integers with positive upper density contains a nontrivial three-term arithmetic progression. More quantitative finite versions say that a progression-free subset of the first N integers occupies a proportion tending to zero as N grows.

A Fourier approach uses a dichotomy. If every nonzero Fourier coefficient is small, then the progression count is close to what the zero frequency predicts. For sufficiently large sets this gives a nontrivial progression.

If a coefficient is large, the set is not Fourier-uniform. That does not mean the proof has failed. A large Fourier coefficient reveals structure: along a suitable long arithmetic progression, the set can have density noticeably higher than its density in the original interval. One can then repeat the analysis inside that more structured region.

The density cannot increase indefinitely because it never exceeds one. Iterating a quantitative form of this argument is the density-increment strategy. However, every step costs something in progression length. Controlling those costs is the hard part of a complete proof. It would be incorrect to state that simply finding one large coefficient proves Roth's theorem.

## What happens for longer patterns

A second complication appears if we replace three terms by four. Ordinary Fourier coefficients are no longer sufficient to control every four-term arithmetic progression count. There are structured functions whose first-order Fourier coefficients are small but whose quadratic phases strongly affect four-term configurations.

The Gowers uniformity norms were designed to measure these higher-order correlations. The U-two norm reflects the fourth powers of Fourier coefficients. It is appropriate for three-term arithmetic progressions. Longer progression problems require higher norms and more elaborate inverse theorems.

This hierarchy matters because the word pseudorandom does not describe one universal property. A set might look random to linear characters but conspicuously patterned to quadratic phases. Which test is useful depends on the configuration we want to count.

## From a count to a structural theorem

Additive combinatorics repeatedly turns counting into a choice between randomness and structure. In the uniform branch, a configuration count behaves approximately as expected. In the structured branch, a large correlation produces information about where the set concentrates.

The finite Fourier identity makes that trade-off explicit for three-term progressions. Density supplies the zero-frequency prediction. The other frequencies record deviations. Roth's theorem shows how to use those deviations constructively, not merely label them as noise.

This perspective also connects directly to coding theory, pseudorandomness, and complexity. All ask which patterns a limited family of tests can detect. Arithmetic progressions are a mathematical laboratory where the tests, the patterns, and the resulting structural obstructions can be written down exactly.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Local Correction and List Decoding: Recovering Information from Few Queries

**Track:** Discrete Mathematics and Combinatorics. **Background:** binary linear codes, Hamming distance, Walsh-Fourier characters, and elementary probability. **Central question:** how can one recover a bit of a long encoded message without reading the entire corrupted codeword?

#### Mathematical companion (not spoken)

Let `x in F_2^k` and define the Hadamard code `C_x(a)=<x,a> mod 2` for `a in F_2^k`. Its block length is `N=2^k`, with distance `N/2` between distinct codewords. For unit vector `e_i`,
\[
 C_x(a)+C_x(a+e_i)=x_i\pmod2.
\]
For a received word with at most `delta N` fixed corruptions, uniform random a yields two uniform positions; by the union bound the failure probability is at most `2delta`, so success is at least `1-2delta`.

Write the received word as `f(a)=(-1)^r(a)`. For `chi_x(a)=(-1)^<x,a>`, correlation `fhat(x)=E_a[f(a)chi_x(a)]=1-2 dist(r,C_x)/N`. Parseval gives `sum_x fhat(x)^2=1`. Hence for `tau>0` at most `1/tau^2` characters have `|fhat(x)|>=tau`; when requiring positively correlated candidates the same bound holds. `dist/N<=1/2-epsilon` implies correlation at least `2epsilon` and list size at most `1/(4epsilon^2)`.

**Distinctions:** A list-size bound is not an efficient decoder by itself. Goldreich-Levin provides an algorithmic heavy-coefficient search. Local correction assumes a corruption pattern independent of fresh decoder randomness; unique recovery beyond half the minimum distance is not guaranteed.

##### Exercises with answers

1. For k=12, what is the Hadamard block length? **Answer:** `2^12=4096`.
2. If delta is one eighth, what two-query success bound follows? **Answer:** at least three quarters.
3. If a candidate has correlation one fifth, what upper bound does Parseval give on the number of such large-correlation candidates? **Answer:** at most twenty-five.
4. Why is returning every nearby codeword not the same as identifying the transmitted one? **Answer:** the received word may be compatible with more than one candidate.

##### Reading and source notes

- [Guruswami, Rudra, and Sudan, Essential Coding Theory](https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/), local correction, Hadamard codes and list decoding.
- [Stanford CS250/EE387, Coding Theory and Applications](https://web.stanford.edu/class/cs250/), notes on locally correctable and list-decodable codes.
- [Goldreich and Levin, A Hard-Core Predicate for All One-Way Functions](https://doi.org/10.1145/73007.73010), heavy Fourier coefficient search and its coding-theoretic interpretation.

### Small-Bias Spaces and Derandomization

**Track:** Discrete Mathematics. **Background:** parity, probability spaces, finite fields, and Fourier analysis on the Boolean cube. **Central question:** how few random bits can fool every nontrivial parity test?

#### Mathematical companion (not spoken)

For `x in {0,1}^n`, `a in {0,1}^n`, let `chi_a(x)=(-1)^{a dot x}`. A distribution `D` is `epsilon`-biased when
\[
|\mathbb E_D\chi_a(X)|\le\epsilon\quad\text{for every }a\ne0.
\]
If `f(x)=sum_a \hat f(a)chi_a(x)`, then
\[
|\mathbb E_D f-\mathbb E_U f|\le\epsilon\sum_{a\ne0}|\hat f(a)|.
\]
The uniform distribution over `{000,011,101,110}` is pairwise independent but has `chi_(111)(X)=+1` always. Small-bias constructions can use `O(log n + log(1/epsilon))` random seed bits (with constants and explicitness subject to the construction). Small support does **not** imply small total variation distance from full uniformity.

##### Exercises with answers

1. Which Fourier character is exempt from the small-bias condition? **Answer:** the constant character `a=0`.
2. What is the bias of the parity of all three bits in the even-parity example? **Answer:** one.
3. Does epsilon bias fool every bounded function with error epsilon? **Answer:** not without further Fourier norm or test-class restrictions.
4. Why does a seed of length `O(log n)` imply polynomial support? **Answer:** at most `2^{O(log n)}=n^{O(1)}` strings are generated.

##### Reading and source notes

- [Naor and Naor, Small-Bias Probability Spaces](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/bias.pdf), explicit short-seed constructions and applications.
- [O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/boolean-analysis/), Fourier characters, influences, and pseudorandomness context.

### Sharp Thresholds, Influences, and the Tribes Function

**Track:** Discrete Mathematics. **Background:** monotone Boolean functions, product measures, derivatives of expectations, and Fourier influences. **Central question:** when does the probability of a property change abruptly as its input density changes?

#### Mathematical companion (not spoken)

Let `f:{0,1}^n -> {0,1}` be monotone and `mu_p` the independent Bernoulli-p measure. With `Inf_i^p(f)` defined as the `mu_p` probability over other coordinates that flipping bit `i` changes `f`, Russo's formula gives
\[
\frac{d}{dp}\mathbb E_p[f]=\sum_{i=1}^n \mathrm{Inf}_i^p(f).
\]
For tribes with `n=km`, `f=OR_{j=1}^k AND_{i in tribe j} x_i`,
\[
\mathbb P_p(f=1)=1-(1-p^m)^k,
\quad \mathrm{Inf}_i^p(f)=p^{m-1}(1-p^m)^{k-1}.
\]
At `p=1/2`, choose `k ~ (ln 2)2^m`; the event is balanced and total influence `km 2^{-(m-1)}(1-2^{-m})^{k-1}=Theta(m)=Theta(log n)`. This statement is asymptotic for large m and integer choices of k. For `OR_n` the critical density is `Theta(1/n)` and the relative window does not shrink; an absolutely small window alone is not the standard notion of sharpness near a vanishing threshold.

##### Exercises with answers

1. What is the derivative of `P_p(OR_n=1)`? **Answer:** `n(1-p)^{n-1}`.
2. What makes a coordinate pivotal for a monotone function? **Answer:** setting that coordinate from zero to one changes the output, holding the others fixed.
3. Why can a function of one coordinate have a coarse threshold? **Answer:** its probability is exactly p and total influence is one.
4. For tribes, why does any one coordinate have small influence? **Answer:** all other bits in its tribe must be one and every other tribe incomplete.

##### Reading and source notes

- [O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/boolean-analysis/), Russo's lemma, influence bounds, juntas, and tribes.
- [Friedgut, Boolean Functions with Low Average Sensitivity Depend on Few Coordinates](https://doi.org/10.1007/PL00009809), the junta theorem and structural meaning of low influence.

### Polynomial Codes and Local Testability

**Track:** Discrete Mathematics. **Background:** finite fields, error-correcting codes, polynomial interpolation, and probabilistic algorithms. **Central question:** how can a few evaluations provide evidence that a huge table is the evaluation of one low-degree polynomial?

#### Mathematical companion (not spoken)

Let `RM_q(m,d)` be evaluations of total-degree-`<=d` polynomials `f:F_q^m -> F_q`, with `d<q` for the simple distance statement. Schwartz–Zippel gives
\[
\Pr_{x\in\mathbb F_q^m}[f(x)=0]\le d/q \quad(f\ne0),
\qquad \delta_{\min}\ge1-d/q.
\]
For `q=3,d=1`, nonconstant nonzero affine differences vanish on exactly a third of the grid, so the minimum relative distance is `2/3` (constant differences have distance 1).

On the line `(x,y)=(t,1+t)` in `F_3^2`, `f=x+y` has values `(1,0,2)` at `t=0,1,2`, with `f(0)-2f(1)+f(2)=0 mod 3`. Given uncorrupted values at `t=1,2`, interpolation recovers `f(0)=2f(1)-f(2) (mod 3)`. Random-line test soundness and local correction probabilities depend on the test, corruption model, and parameters; do not treat the existence of a line test as a proof of a uniform soundness constant.

##### Exercises with answers

1. What is the lower bound on relative distance for `RM_5(m,2)`? **Answer:** `1-2/5=3/5`.
2. Do the values `(0,1,2)` on a line over `F_3` satisfy an affine restriction? **Answer:** Yes; `0-2+2=0` modulo 3.
3. Can a single passing random line certify membership in the code? **Answer:** No; a quantitative soundness argument needs many possible samples.
4. Why are local testing and correction different? **Answer:** Testing checks global proximity to a code, while correction reconstructs one coordinate of a nearby codeword.

##### Reading and source notes

- [Arora and Safra, Probabilistic Checking of Proofs: a New Characterization of NP](https://doi.org/10.1145/273865.273901), role of low-degree tests in proof checking.
- [Sudan, Decoding of Reed–Solomon Codes Beyond the Error-Correction Bound](https://doi.org/10.1006/jcom.1997.0439), algebraic decoding context (Reed–Solomon is the univariate member of the evaluation-code family).
- [Kaufman and Sudan, Algebraic Property Testing: The Role of Invariance](https://doi.org/10.1145/1374376.1374434), algebraic local testing and global constraints.

### Additive Combinatorics and Fourier Uniformity

**Track:** Discrete Mathematics and Combinatorics. **Background:** finite groups, Fourier series, counting, and probability. **Central question:** when does the additive structure of a set force it to contain arithmetic progressions?

#### Mathematical companion (not spoken)

Let `G=\mathbb Z/N\mathbb Z` with `N` odd. For `f:G\to\mathbb C`, normalize
\[
\widehat f(r)=\mathbb E_{x\in G} f(x)e^{-2\pi i rx/N},\qquad
T_3(f)=\mathbb E_{x,d\in G}f(x)f(x+d)f(x+2d).
\]
Fourier inversion and orthogonality give
\[
T_3(f)=\sum_{r\in G}\widehat f(r)^2\widehat f(-2r).
\]
For `f=1_A`, `\widehat f(0)=\alpha=|A|/N`; hence the zero-frequency term is `\alpha^3`. By the triangle inequality and Parseval,
\[
|T_3(f)-\alpha^3|\le \max_{r\ne0}|\widehat f(-2r)|\sum_{r\ne0}|\widehat f(r)|^2
\le \alpha \max_{r\ne0}|\widehat f(r)|,
\]
since multiplication by `-2` permutes frequencies for odd `N`. The `d=0` progressions contribute `\alpha/N`, so `T_3(f)>\alpha/N` guarantees a nontrivial progression.

For `N=5`, `A={0,1,2}`, exactly five ordered pairs `(x,d)` work: `(0,0),(1,0),(2,0),(0,1),(2,-1)`. Therefore `T_3(1_A)=5/25=1/5`, while `\alpha^3=27/125`.

The normalized Gowers `U^2` norm satisfies `\|f\|_{U^2}^4=\sum_r|\widehat f(r)|^4`. This measures a higher moment of the Fourier spectrum, not merely the maximum coefficient.

##### Exercises with answers

1. What is `T_3(1_G)`? **Answer:** `1`, since every `(x,d)` qualifies.
2. How many trivial progressions are in a set of size k? **Answer:** `k`, one for each `(x,0)`.
3. Under the stated uniformity bound, when must a nontrivial progression exist? **Answer:** when `\alpha^3-\alpha\max_{r\ne0}|\hat f(r)|>\alpha/N`.
4. Why is U-two insufficient for arbitrary four-term progressions? **Answer:** quadratic-phase correlations can be invisible to linear Fourier tests.

##### Reading and source notes

- [Soundararajan, Additive Combinatorics and Roth's Theorem Lecture Notes](https://www.math.cmu.edu/~af1p/Teaching/AdditiveCombinatorics/Soundararajan.pdf), Fourier proof methods and density increments.
- [Tao and Vu, Additive Combinatorics (book information)](https://terrytao.wordpress.com/books/additive-combinatorics/), general structure and uniformity methods.
