# 024000 — Coding Bounds, Duality, and Probabilistic Codes

**Track:** Discrete Mathematics and Combinatorics. **Background:** finite fields, counting, random codes, Hamming distance, linear algebra. **Central question:** how many messages can we encode while guaranteeing correction of a given number of errors?

<!-- BEGIN SPOKEN LECTURE -->

# The geometry of reliable messages

Imagine sending a seven-bit word through a noisy channel. A few bits may flip during transmission. A code does not make corruption impossible. Instead, it chooses a restricted collection of allowed words so that the receiver can identify which allowed word was most likely sent.

We can visualize each binary word as a vertex of a high-dimensional cube. The Hamming distance between two words is the number of coordinates where they disagree. If a code has minimum distance three, then any two allowed words disagree in at least three places. A single corrupted bit cannot move one codeword all the way into the one-bit neighborhood of another.

The central tradeoff is between packing many codewords into the cube and keeping them far apart. Counting gives both upper bounds that no code can exceed and lower bounds proving that large codes exist.

## Hamming balls and the packing bound

A Hamming ball of radius one around a binary word contains the word itself and each word obtained by flipping exactly one bit. In length seven there are eight such words.

If a code corrects one error, these radius-one balls around distinct codewords must not overlap. Otherwise a received word in their intersection would be within one error of two different messages. Since the entire seven-dimensional cube has one hundred twenty-eight binary words, at most sixteen disjoint radius-one balls fit inside it.

That argument is the sphere-packing, or Hamming, bound. In length n, a radius-t ball has size equal to the sum of the binomial coefficients from n choose zero through n choose t. If the minimum distance is at least two t plus one, multiply the number of codewords by that ball volume; it cannot exceed two to the n.

The bound is necessary, not a promise that optimal packings exist at every length. In certain cases they do. The binary Hamming code of length seven has sixteen codewords and minimum distance three. Its radius-one balls fill the entire cube without gaps or overlaps. This is why that code is called perfect.

## A lower bound from greedy selection

Now approach the question from the opposite direction. Start with all binary words available. Pick one as a codeword, then discard all words closer than the required minimum distance. Pick another from the remaining set, discard its nearby words, and continue.

When the process stops, the chosen codewords have the desired minimum distance. Every unchosen word lies within distance d minus one of a chosen word, because otherwise we could add it. These larger balls cover the whole cube. Counting their volumes shows that the number of selected codewords is at least the size of the cube divided by the volume of a ball of radius d minus one.

This is the Gilbert bound, a form of the Gilbert-Varshamov existence argument. It is striking because it proves the existence of a code by covering, while the Hamming bound limits possible codes by packing. The two ball radii differ, leaving a gap between the general upper and lower bounds.

Random selection gives another existence strategy. Choose candidate codewords randomly and estimate the chance that any pair is too close. A union bound can prove a good code exists when the expected number of bad pairs is below one. Such a simple random-pair argument is generally weaker than the greedy volume estimate, but it illustrates the probabilistic method.

## Linear codes and their duals

If the code is a vector subspace over the field with two elements, we can describe it by a generator matrix. A linear code of dimension k contains exactly two to the k words, so its information rate is k divided by n. There is also a parity-check matrix, which defines the code as the set of words satisfying a collection of linear constraints.

The rows of a parity-check matrix span the dual code, the orthogonal complement under the standard dot product over the binary field. The dual does not usually have the same distance or error-correction ability as the original. Its role is to reveal the constraints, support syndrome decoding, and relate weight distributions through MacWilliams identities.

The seven-bit Hamming code is the kernel of a three-by-seven parity-check matrix whose columns are the seven nonzero three-bit vectors. Any single-bit error creates a syndrome equal to the corresponding column. Because the columns are distinct, the syndrome identifies which bit changed.

To see the minimum distance, notice that no column is zero and no two columns are equal, so a codeword of weight one or two cannot satisfy all parity checks. Three suitable columns do sum to zero, establishing distance three. The dimension is four, since the parity-check matrix has rank three. This gives sixteen codewords, exactly the number required for the perfect packing we counted earlier.

## Bounds guide construction

The Singleton bound gives yet another constraint: a length-n code with minimum distance d has at most two to the power n minus d plus one codewords. It follows by deleting any d minus one coordinate positions. Two codewords that became identical would originally differ in too few positions.

Different bounds emphasize different obstacles. Sphere packing limits error-correcting neighborhoods. Singleton limits how much redundancy can be removed. Gilbert-Varshamov shows that a substantial number of distant codewords must exist. Linear algebra turns abstract point sets into efficiently encoded and decoded families.

These bounds do not solve every optimal-coding problem. They define the region in which constructions can live. A good code is therefore both a geometric packing and an algorithmic object: it must place messages far apart, and its structure must let us recover them reliably.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a binary code `C subset F_2^n` with minimum distance `d`, unique correction of `t=floor((d-1)/2)` errors requires disjoint radius-t Hamming balls. Their volume is `V(n,t)=sum_{j=0}^t binom(n,j)`. Hence the Hamming bound:
\[
|C|\,V(n,t)\le 2^n.
\]
A maximal greedy distance-d code covers the cube by radius-(d-1) balls, so the Gilbert bound yields
\[
A_2(n,d)\ge \frac{2^n}{V(n,d-1)}.
\]
The Singleton bound follows by puncturing any `d-1` coordinates: `|C| <= 2^{n-d+1}`.

The `[7,4,3]` binary Hamming code has a `3 x 7` parity-check matrix H whose columns are the seven distinct nonzero members of `F_2^3`. Since `rank(H)=3`, `dim(ker H)=4`, so `|C|=16`. No column is zero or repeated, excluding weight-one and weight-two codewords. Any two distinct nonzero columns have a nonzero sum equal to a third column, producing a weight-three codeword. With `V(7,1)=8`, the packing bound is tight: `16 x 8=128=2^7`.

If `C` is linear of dimension k, then `C^perp` has dimension `n-k`; the dual typically has a different minimum distance. Syndrome decoding uses `s=Hy^T` and a low-weight error vector e satisfying `He^T=s`.

### Exercises with answers

1. Compute `V(5,1)`. **Answer:** `1+5=6`.
2. For a binary code with `n=7,d=3`, what is the Hamming bound on `|C|`? **Answer:** at most `128/8=16`.
3. Why does puncturing `d-1` coordinates preserve distinctness? **Answer:** otherwise two original codewords would differ in at most `d-1` places, contradicting minimum distance d.
4. What is the dimension of the dual of an `[n,k]` binary linear code? **Answer:** `n-k`.

### Reading and source notes

- [University of Maryland, Coding Theory and Applications](https://www.terpconnect.umd.edu/~abarg/ECC/), Gilbert-Varshamov, Hamming, Plotkin and duality lectures.
- [MIT, Essential Coding Theory course notes](https://people.csail.mit.edu/madhu/FT01/), coding constructions and distance bounds.
- [MacWilliams and Sloane, The Theory of Error-Correcting Codes](https://www.elsevier.com/books/the-theory-of-error-correcting-codes/macwilliams/978-0-444-85193-2), classical reference.
