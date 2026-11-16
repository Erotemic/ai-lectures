# 036000 - Local Correction and List Decoding: Recovering Information from Few Queries

**Track:** Discrete Mathematics and Combinatorics. **Background:** binary linear codes, Hamming distance, Walsh-Fourier characters, and elementary probability. **Central question:** how can one recover a bit of a long encoded message without reading the entire corrupted codeword?

<!-- BEGIN SPOKEN LECTURE -->

# Recover one bit, not the whole file

Suppose a message is encoded into a very long codeword. Some positions are corrupted. Traditional decoding asks for the entire original message. But perhaps we only need one particular bit. Must we read the whole received word to recover that one bit?

A locally decodable code answers no. Its decoder may inspect only a few codeword positions, chosen with randomness, and return a requested message symbol with high probability despite a controlled fraction of adversarial corruption. This is an algorithmic guarantee about the number of queries. It is not the same as ordinary error correction, because decoding only one symbol is the task.

The simplest convincing example is the binary Hadamard code. Its length is enormous relative to the message, but its local recovery rule is so elementary that we can derive it in a few lines. The example exposes both the strength and the cost of local decoding.

# Every possible parity becomes a codeword symbol

Take a message x consisting of k binary bits. For every binary query vector a of length k, store the parity of the coordinates where x and a both have a one. There are two to the power k possible query vectors, so the codeword has length two to the power k.

Each coordinate of the codeword is therefore a linear function of the message. These coordinates are also precisely the characters of the binary vector space that appear in Walsh-Fourier analysis. The same algebra serves both coding theory and analysis of Boolean functions.

To recover message bit i from an uncorrupted codeword, choose any query vector a. Read the encoded parity at a, and also at a plus the unit vector in direction i. Add those two parity bits modulo two. Every message coordinate other than i appears twice and cancels. The coordinate i appears once, leaving exactly the desired message bit.

This identity is true for every choice of a. That redundancy lets us randomize the queries when corruption is present.

# Why random queries defeat a fixed error pattern

Assume an adversary has corrupted at most a fraction delta of the positions in the encoded word. The adversary chooses its error locations before seeing the decoder's fresh random queries. Choose a uniformly random query vector a, and inspect positions a and a plus the i-th unit vector.

Each position is uniformly distributed over the codeword coordinates. The chance that the first query lands in a corrupted position is at most delta. The same is true of the second. By the union bound, the chance that either is corrupted is at most two delta. If neither is corrupted, the parity cancellation gives the correct bit.

Thus our two-query decoder succeeds with probability at least one minus two delta. The two error events need not be independent; the union bound requires no independence. At corruption rate one tenth, the lower bound is four fifths. The decoder uses two queries no matter how large k is.

But the codeword has exponential length. We gained query efficiency by sacrificing storage. The example does not promise a practical short code with two-query correction. Indeed there are significant lower bounds on the length of two-query locally decodable codes, which help explain why this naive construction is so large.

# Repeat for confidence, but count queries honestly

One run of the decoder has a constant chance of failure when the corruption rate is bounded below one quarter. Independent repetitions and majority voting can reduce that failure probability exponentially in the number of repetitions. Doing so increases the number of queries by the number of trials.

If the adversary can choose which positions are corrupted after seeing each fresh query, the fixed-error-pattern guarantee no longer applies. The randomized decoder assumes an error word fixed independently of its private randomness. Likewise, if corruption exceeds the stated limit, the success bound may become uninformative.

Local decoding is a statement with parameters: number of message bits, codeword length, fraction of corruption, query complexity, and success probability. Omitting those parameters turns a theorem into a slogan.

# When unique decoding is the wrong question

Now consider a received word that is very far from every codeword under the usual unique-decoding radius. There might be several plausible original messages. Instead of insisting on one answer, list decoding asks for all codewords whose distance from the received word is below a specified threshold.

The distinction is logical. A code has a minimum distance, so two distinct codewords cannot both lie too close to the same received word. Beyond half the minimum distance, uniqueness may fail. A list decoder allows several candidates and tries to keep the list short.

The Hadamard code again offers a remarkable Fourier explanation. Express the received binary word as a function taking values plus one or minus one. Each Hadamard codeword corresponds to a Fourier character. The correlation of the received word with a character measures how well that codeword agrees with it.

If the relative Hamming distance is at most one half minus epsilon, the correlation is at least twice epsilon. Thus nearby codewords correspond exactly to large Fourier coefficients.

# Parseval limits the number of candidates

The squared Fourier coefficients of a plus-or-minus-one function sum to one. Suppose every candidate codeword has correlation at least tau. Each contributes at least tau squared to that total. Therefore there can be at most one divided by tau squared candidates.

This is a strong bound. Even though the code contains two to the power k distinct codewords, only a small number can agree with an arbitrary received word significantly better than random guessing. The proof requires no sophisticated combinatorics: it is just orthogonality of characters followed by a counting inequality.

For example, if a codeword must have correlation at least one quarter, there are at most sixteen such codewords. In terms of Hamming distance, that threshold corresponds to distance at most three eighths of the code length. The bound holds even if finding the list is computationally difficult.

# Finding the heavy coefficients

An existence bound on list size is different from an efficient list-decoding algorithm. The Goldreich-Levin method shows how to locate large Walsh-Fourier coefficients using randomized oracle access, without scanning the full exponentially long codeword. Its complexity depends polynomially on the message length and the inverse threshold, under the standard query model.

This brings together two strands of ideas. Local correction recovers a selected message bit from carefully paired codeword queries. List decoding locates all messages whose Hadamard encodings correlate strongly with a received function. Both rely on linearity and parity, but one assumes enough proximity to a single intended codeword to answer a specific query, while the other allows multiple plausible codewords.

A list alone also does not tell us which candidate message was intended. Additional structure, a checksum, side information, or a stronger decoding guarantee may be necessary. No amount of clever enumeration can conjure unique information absent from the received word.

# Locality as a mathematical resource

The Hadamard construction is not a practical final answer to every storage problem. It is a reference point for asking what is possible. Can we shorten the codeword while keeping a constant number of queries? Can we tolerate more corruption? Can we recover symbols over larger alphabets? Can a decoder be locally correctable without first reconstructing the message?

More advanced locally decodable and locally correctable codes answer these questions through algebraic curves, polynomial restrictions, matching-vector families, and other constructions. The lesson from the elementary case remains: redundancy can be arranged so that a few random local observations reveal a global message symbol, and Fourier orthogonality can bound how many global explanations remain plausible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `x in F_2^k` and define the Hadamard code `C_x(a)=<x,a> mod 2` for `a in F_2^k`. Its block length is `N=2^k`, with distance `N/2` between distinct codewords. For unit vector `e_i`,
\[
 C_x(a)+C_x(a+e_i)=x_i\pmod2.
\]
For a received word with at most `delta N` fixed corruptions, uniform random a yields two uniform positions; by the union bound the failure probability is at most `2delta`, so success is at least `1-2delta`.

Write the received word as `f(a)=(-1)^r(a)`. For `chi_x(a)=(-1)^<x,a>`, correlation `fhat(x)=E_a[f(a)chi_x(a)]=1-2 dist(r,C_x)/N`. Parseval gives `sum_x fhat(x)^2=1`. Hence for `tau>0` at most `1/tau^2` characters have `|fhat(x)|>=tau`; when requiring positively correlated candidates the same bound holds. `dist/N<=1/2-epsilon` implies correlation at least `2epsilon` and list size at most `1/(4epsilon^2)`.

**Distinctions:** A list-size bound is not an efficient decoder by itself. Goldreich-Levin provides an algorithmic heavy-coefficient search. Local correction assumes a corruption pattern independent of fresh decoder randomness; unique recovery beyond half the minimum distance is not guaranteed.

### Exercises with answers

1. For k=12, what is the Hadamard block length? **Answer:** `2^12=4096`.
2. If delta is one eighth, what two-query success bound follows? **Answer:** at least three quarters.
3. If a candidate has correlation one fifth, what upper bound does Parseval give on the number of such large-correlation candidates? **Answer:** at most twenty-five.
4. Why is returning every nearby codeword not the same as identifying the transmitted one? **Answer:** the received word may be compatible with more than one candidate.

### Reading and source notes

- [Guruswami, Rudra, and Sudan, Essential Coding Theory](https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/), local correction, Hadamard codes and list decoding.
- [Stanford CS250/EE387, Coding Theory and Applications](https://web.stanford.edu/class/cs250/), notes on locally correctable and list-decodable codes.
- [Goldreich and Levin, A Hard-Core Predicate for All One-Way Functions](https://doi.org/10.1145/73007.73010), heavy Fourier coefficient search and its coding-theoretic interpretation.
