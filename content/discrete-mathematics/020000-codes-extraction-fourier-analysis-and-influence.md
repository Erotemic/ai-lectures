# Codes, extraction, Fourier analysis, and influence

<!-- BEGIN SPOKEN LECTURE -->

# Codes, extraction, Fourier analysis, and influence

## Block Designs, Finite Planes, and Hamming Codes

Suppose an experiment has seven treatments, and each trial can include three of them. We want to compare every pair fairly. Can we arrange the trials so that each pair of treatments appears together exactly once? The question sounds like scheduling. The answer is a piece of geometry, and the same geometry builds an error-correcting code.

Call the seven treatments points and the three-treatment trials blocks. There is no requirement that the points lie on a physical plane. The assignment of points to blocks determines the construction.

A balanced incomplete block design is specified by four numbers. There are v points, each block contains k points, and every pair of distinct points appears together in exactly lambda blocks. The number of blocks and the number of blocks containing one point are additional parameters. We do not get to choose all six numbers independently: simple counting forces equations between them.

### Two double counts

Count incidences of a point in a block. If there are b blocks of size k, there are b times k incidences. If each of the v points appears in r blocks, the same incidences number v times r. Those quantities must agree.

Now fix a point P. In each of its r blocks, P is paired with k minus one other points. Across all blocks through P, each of the v minus one other points appears exactly lambda times. Thus r times k minus one equals lambda times v minus one.

The equalities are elementary, but powerful. They can rule out proposed designs before we try to construct anything. For seven points, blocks of size three, and one appearance per pair, the second relation gives r equal to three. The first then gives b equal to seven. We must find seven triples, each point in three triples, covering every pair exactly once.

### The Fano plane without a drawing

Take the seven nonzero vectors in three-dimensional vector space over the field with two elements. For any two distinct nonzero vectors u and v, their sum is a third nonzero vector different from either one. Make a block from u, v, and their sum.

Why does this construction work? Every two distinct nonzero vectors determine a two-dimensional subspace. That subspace has four vectors in all: zero and three nonzero ones. So it determines a unique block of size three. Each pair belongs to exactly one such block. The seven points and seven blocks form the Fano plane.

The word plane is justified by its incidence axioms: any two points lie on a unique line and any two lines meet in a unique point. But the geometry is finite. It uses addition modulo two instead of distances and angles. Its symmetry comes from the linear algebra of a small field.

### Counting is a structural test, not an existence proof

The parameter equations are necessary, not sufficient. A proposed collection of numbers can satisfy the incidence counts without any design existing. Additional divisibility, parity, and geometric obstructions may intervene.

This is a lesson worth remembering when using counting arguments. A successful count verifies that a construction is possible in principle; it does not produce the construction. The Fano plane is valuable precisely because the vector-space model supplies both the necessary counts and an explicit family of blocks.

### From geometry to a parity check

Now arrange those same seven nonzero binary vectors as the columns of a matrix with three rows. Interpret the matrix as a parity-check operator. A seven-bit string is accepted as a codeword if multiplying its column vector by the matrix gives the zero vector over the field with two elements.

The matrix has rank three, so its kernel is four-dimensional. There are sixteen codewords among the one hundred twenty-eight possible seven-bit strings. This is the binary Hamming code of length seven and dimension four.

Why can it correct one bit error? If exactly one bit flips, the syndrome is the corresponding column of the parity-check matrix. Since all seven columns are distinct and nonzero, the syndrome tells us exactly which position was corrupted. A zero syndrome means the received word passes the parity checks, although it does not guarantee that no two or more errors occurred.

The smallest nonzero codeword has weight three. To see why, no one column is zero, and no two distinct columns add to zero. Yet every line of the Fano plane consists of three columns that add to zero. Thus the minimum distance is exactly three. By the standard distance criterion, the code can correct any one error or detect any two errors.

### A common combinatorial skeleton

The experimental design asks for balanced pair coverage. The finite geometry asks for unique lines through pairs of points. The error-correcting code asks for a sparse way to distinguish possible error locations. They are not three separate coincidences. They are consequences of the same incidence structure in a vector space over a finite field.

That is a recurring role of combinatorics: an arrangement first invented for one purpose may encode information useful in a different problem. When the relationships are exact, the translation can be proved, not merely suggested.

## Coding Bounds, Duality, and Probabilistic Codes

Imagine sending a seven-bit word through a noisy channel. A few bits may flip during transmission. A code does not make corruption impossible. Instead, it chooses a restricted collection of allowed words so that the receiver can identify which allowed word was most likely sent.

We can visualize each binary word as a vertex of a high-dimensional cube. The Hamming distance between two words is the number of coordinates where they disagree. If a code has minimum distance three, then any two allowed words disagree in at least three places. A single corrupted bit cannot move one codeword all the way into the one-bit neighborhood of another.

The central tradeoff is between packing many codewords into the cube and keeping them far apart. Counting gives both upper bounds that no code can exceed and lower bounds proving that large codes exist.

### Hamming balls and the packing bound

A Hamming ball of radius one around a binary word contains the word itself and each word obtained by flipping exactly one bit. In length seven there are eight such words.

If a code corrects one error, these radius-one balls around distinct codewords must not overlap. Otherwise a received word in their intersection would be within one error of two different messages. Since the entire seven-dimensional cube has one hundred twenty-eight binary words, at most sixteen disjoint radius-one balls fit inside it.

That argument is the sphere-packing, or Hamming, bound. In length n, a radius-t ball has size equal to the sum of the binomial coefficients from n choose zero through n choose t. If the minimum distance is at least two t plus one, multiply the number of codewords by that ball volume; it cannot exceed two to the n.

The bound is necessary, not a promise that optimal packings exist at every length. In certain cases they do. The binary Hamming code of length seven has sixteen codewords and minimum distance three. Its radius-one balls fill the entire cube without gaps or overlaps. This is why that code is called perfect.

### A lower bound from greedy selection

Now approach the question from the opposite direction. Start with all binary words available. Pick one as a codeword, then discard all words closer than the required minimum distance. Pick another from the remaining set, discard its nearby words, and continue.

When the process stops, the chosen codewords have the desired minimum distance. Every unchosen word lies within distance d minus one of a chosen word, because otherwise we could add it. These larger balls cover the whole cube. Counting their volumes shows that the number of selected codewords is at least the size of the cube divided by the volume of a ball of radius d minus one.

This is the Gilbert bound, a form of the Gilbert-Varshamov existence argument. It is striking because it proves the existence of a code by covering, while the Hamming bound limits possible codes by packing. The two ball radii differ, leaving a gap between the general upper and lower bounds.

Random selection gives another existence strategy. Choose candidate codewords randomly and estimate the chance that any pair is too close. A union bound can prove a good code exists when the expected number of bad pairs is below one. Such a simple random-pair argument is generally weaker than the greedy volume estimate, but it illustrates the probabilistic method.

### Linear codes and their duals

If the code is a vector subspace over the field with two elements, we can describe it by a generator matrix. A linear code of dimension k contains exactly two to the k words, so its information rate is k divided by n. There is also a parity-check matrix, which defines the code as the set of words satisfying a collection of linear constraints.

The rows of a parity-check matrix span the dual code, the orthogonal complement under the standard dot product over the binary field. The dual does not usually have the same distance or error-correction ability as the original. Its role is to reveal the constraints, support syndrome decoding, and relate weight distributions through MacWilliams identities.

The seven-bit Hamming code is the kernel of a three-by-seven parity-check matrix whose columns are the seven nonzero three-bit vectors. Any single-bit error creates a syndrome equal to the corresponding column. Because the columns are distinct, the syndrome identifies which bit changed.

To see the minimum distance, notice that no column is zero and no two columns are equal, so a codeword of weight one or two cannot satisfy all parity checks. Three suitable columns do sum to zero, establishing distance three. The dimension is four, since the parity-check matrix has rank three. This gives sixteen codewords, exactly the number required for the perfect packing we counted earlier.

### Bounds guide construction

The Singleton bound gives yet another constraint: a length-n code with minimum distance d has at most two to the power n minus d plus one codewords. It follows by deleting any d minus one coordinate positions. Two codewords that became identical would originally differ in too few positions.

Different bounds emphasize different obstacles. Sphere packing limits error-correcting neighborhoods. Singleton limits how much redundancy can be removed. Gilbert-Varshamov shows that a substantial number of distant codewords must exist. Linear algebra turns abstract point sets into efficiently encoded and decoded families.

These bounds do not solve every optimal-coding problem. They define the region in which constructions can live. A good code is therefore both a geometric packing and an algorithmic object: it must place messages far apart, and its structure must let us recover them reliably.

## Randomness Extractors: Recovering Usable Random Bits

Imagine a physical sensor producing bits. Its output varies, but the zeros occur much more often than the ones. Or imagine a computer process that chooses uniformly from a secret set of a million possible strings, while the entire space of possible bit strings is vastly larger. In both cases the output has uncertainty, but it is not uniformly distributed.

Many algorithms assume access to independent fair bits. The question is whether we can take a weak random source and produce shorter bits that are nearly uniform. A randomness extractor provides a precise answer, but only after we specify how much uncertainty is guaranteed in the source and what extra randomness the extractor may use.

The most useful elementary measure is min-entropy. A random variable has min-entropy at least k if no particular outcome has probability larger than two to the minus k. This measures the difficulty of predicting the single most likely outcome. It is stronger than simply requiring a large Shannon entropy, and it is the right kind of promise for several extractor constructions.

## An information-theoretic obstruction

There is a reason extraction cannot be universally deterministic. Suppose a fixed function compresses n-bit strings to one output bit. At least half the inputs share the same output. An adversary can choose a source uniformly from that large preimage. The source has substantial min-entropy, yet the output is constant.

This proves that no single deterministic function can extract a nearly fair bit from every arbitrary high-min-entropy source unless the source family has more structure or the min-entropy promise is extremely strong. The extractor must use additional assumptions, multiple independent sources, or a short independent random seed.

A seeded extractor is a function of two inputs: the weak source and a seed of genuinely uniform bits independent of that source. It aims to make the joint distribution of seed and output close to the distribution of an independent uniform seed and uniform output. Such an extractor is called strong. Including the seed in the guarantee means it is safe to reveal which seed was used without destroying the statistical closeness of that one extraction.

## Universal hashing is an extractor

Consider a family of hash functions mapping n-bit strings to m-bit strings. The family is two-universal if, for any two distinct inputs, the chance that a randomly selected hash function sends them to the same output is at most two to the minus m.

A simple example uses a uniformly random binary matrix with m rows and n columns. Multiply the source vector by the matrix over the field of two elements. Distinct inputs have a difference vector that is nonzero, and each random row has an independent fair dot product with that difference. Thus the full collision probability is exactly two to the minus m.

The leftover hash lemma says that if the source has min-entropy k and the seed chooses a two-universal hash function independently, the output together with the seed is statistically close to uniform. One standard bound on total variation distance is one half times the square root of two raised to the power m minus k.

The lesson is quantitative. If we try to extract all k bits of guaranteed entropy, that bound is weak. If we leave a margin and extract m equal to k minus twice a positive security parameter, the distance becomes exponentially small in that margin. We spend some entropy to obtain a rigorous uniformity guarantee.

## A numerical example

Suppose a source has at least one hundred bits of min-entropy. Use an independent universal-hash seed to produce eighty output bits. The leftover hash bound is one half times the square root of two to the minus twenty. That is two to the minus eleven. Thus the seed-output pair is within about one part in two thousand in total variation distance of ideal independence and uniformity.

If we instead request ninety-eight output bits from the same source, the bound becomes one quarter. That is a poor guarantee. The source has not lost entropy; the theorem is telling us that near-total extraction cannot in general give very small statistical error without stronger conditions.

Notice that the simple random-matrix family uses many seed bits: m times n. This proves the information-theoretic principle but is not a seed-efficient implementation. More sophisticated extractor constructions use much shorter seeds. The efficiency of the seed, the computational cost of extraction, and the amount of source entropy consumed are separate engineering and mathematical questions.

## Extractors versus generators

A pseudorandom generator has a different promise. Starting from a short uniform seed, it produces a longer output intended to look random to some specified class of tests. In cryptography that often means no efficient algorithm can distinguish the output from uniform with significant advantage, under a computational hardness assumption.

An extractor cannot create information-theoretic entropy from nothing. Its output length must be supported by the uncertainty already present in the source, with some loss for statistical accuracy. A computational pseudorandom generator, by contrast, can stretch a short seed into a long sequence that is unpredictable to efficient observers, but the resulting distribution still has at most the seed's entropy. It is not statistically close to uniform on all long strings.

The same word pseudorandom sometimes appears in combinatorics for deterministic objects that imitate random behavior for a restricted set of statistics, such as small-bias sample spaces or expanders. Again the test class must be named. Passing a collection of Fourier tests is not identical to statistical closeness against every possible event.

## Independence and reuse are real assumptions

An extractor guarantee can fail if the seed is correlated with the weak source. Similarly, a strong extractor does not automatically justify reusing a fixed seed forever on arbitrarily correlated future samples. The theorem applies to a specified joint distribution with its independence hypotheses.

This is especially important when building randomness pipelines. A real sensor's entropy may drift. An estimated min-entropy rate is not the same as a proven bound under all operating conditions. Correlations between successive sensor readings matter, as do adversarial influences. A statistical test suite can find some defects but cannot certify the min-entropy of an arbitrary unknown physical process from one finite sample.

The information-theoretic goal is precise: a weak source with a verified min-entropy guarantee, an independent seed, and an extractor with a proved variation-distance bound. Only then can downstream algorithms safely replace ideal bits by extracted bits, paying an explicit amount in their error probabilities.

## Randomness as a resource with a budget

The surprising point is that even severely nonuniform randomness can yield almost fair bits if its unpredictability is quantified and we are willing to use a seed. Universal hashing gives an accessible proof, while sophisticated extractors improve seed length and computational efficiency.

A useful design question is not simply whether the output looks random. It is: random according to which test, under which entropy guarantee, with what error, and relative to which seed? Those four questions turn vague randomness claims into mathematics.

## Fourier Analysis on the Boolean Cube

Fourier analysis often begins with waves on a circle. A complicated signal is decomposed into simple oscillations, each with a frequency and a coefficient. The Boolean cube seems like a completely different object. Its points are strings of plus ones and minus ones. There is no continuously varying angle, only a collection of discrete choices.

Yet the same strategy works. A function on n bits can be decomposed into components indexed by subsets of the n coordinates. One component is constant. Some depend on individual bits. Others measure two-way interactions, three-way interactions, and all the way up to a term involving every bit at once.

The basic building blocks are parity characters. Given a set of coordinates S, multiply the input bits whose positions lie in S. That product is either plus one or minus one. For the empty set it is always one. For a singleton it is just the chosen bit. For the full coordinate set it is the parity of all bits, expressed in the plus-minus convention.

These characters form an orthonormal basis for real-valued functions on the Boolean cube when inputs are uniformly random. This turns a discrete function into a vector of Fourier coefficients. The coefficients tell us which interactions the function uses.

## Orthogonality is almost free

Take two distinct parity characters. Multiply them together. Any coordinate belonging to both sets appears twice and cancels, because a bit squared equals one. What remains is the parity character of the symmetric difference of the two sets.

If that difference is nonempty, at least one independent uniformly random bit appears exactly once. Averaging over that bit produces zero. Therefore the expected product of distinct characters is zero. The expected square of a character is one. That proves orthonormality with almost no machinery.

There are two to the n subsets of n coordinates and exactly two to the n possible inputs. So we have exactly enough orthonormal characters to form a basis for every function on this finite space.

The Fourier coefficient at a set S is the average value of the function multiplied by the parity character of S. Add all those coefficients times their characters, and the original function is recovered exactly. This is an identity on every input, not a statistical approximation.

## Parseval turns function size into coefficient energy

There is a finite version of Parseval's identity. The expected square of the function equals the sum of squares of all its Fourier coefficients. For a Boolean function taking only plus one and minus one, the expected square is always one. Thus its Fourier coefficients have squared magnitudes summing to one.

This is powerful because it converts nonlinear-looking questions about a function into ordinary sums over subsets. A function that puts most of its Fourier energy on small subsets is dominated by low-order interactions. A parity of all n coordinates puts all its energy on the full set. Both are perfectly legitimate Boolean functions, but they respond differently to random noise.

Consider majority on three bits. It outputs the sign of the sum of the three inputs, so there is never a tie. Its Fourier expansion is one half times the sum of the three individual bits, minus one half times their triple product. The three singleton coefficients and the triple coefficient each have absolute value one half. Their squared magnitudes sum to four quarters, exactly one.

That expansion shows that three-bit majority is mostly a linear vote, with a three-way correction. One can verify it by substituting all eight inputs, but the Fourier basis explains why those terms are the right ones.

## Influence measures susceptibility to one flipped bit

To study sensitivity, choose an input uniformly at random and flip one selected coordinate. Ask how often the output changes. The probability of change is called the influence of that coordinate for a Boolean output.

Fourier analysis gives an exact identity. A character involving coordinate i changes sign when i is flipped; a character not involving i does not change. Squaring the difference and averaging removes cross terms by orthogonality. The influence of coordinate i becomes the sum of squared Fourier coefficients over all subsets containing i.

The total influence sums over coordinates. Every coefficient indexed by S is then counted once for each coordinate in S, giving the sum of the coefficient squares weighted by the size of S. High-degree Fourier components contribute more to sensitivity.

For parity on all n bits, flipping any one bit always flips the output. Every coordinate has influence one. For majority on three bits, each coordinate has influence one half. The distinction is now numerical rather than intuitive.

## Noise stability is a spectral filter

Suppose each input bit is independently kept with some probability and flipped otherwise. Let rho denote the correlation between the original bit and the noisy bit. If a parity character involves k distinct coordinates, its expected product before and after noise is rho raised to k. Each coordinate contributes one factor of rho.

Consequently the expected product of the function on the original input and on the noisy input is a sum of squared Fourier coefficients weighted by rho to the size of their subsets. This is the noise-stability formula.

For full parity, the answer is rho to the n. At any fixed correlation strictly between zero and one, parity loses correlation rapidly as n grows. For three-bit majority, noise stability is three quarters times rho plus one quarter times rho cubed. The low-degree Fourier energy keeps it more stable for moderate noise.

The same operator that shrinks degree-k Fourier coefficients by rho to the k is called the noise operator. It smooths functions on the cube by suppressing high-degree interactions. It is a discrete counterpart of familiar heat or smoothing operators in continuous analysis.

## A useful inequality from the same coefficients

Let the variance of a function measure the part not explained by its constant Fourier coefficient. Parseval says the variance is the sum of squared coefficients over all nonempty subsets.

Every nonempty subset has size at least one. So the variance is at most the sum of subset sizes times squared coefficients. But that last sum is total influence. We have obtained the Boolean Poincaré inequality: variance is bounded above by total influence.

This inequality has a useful reading. If a function varies significantly across inputs, flipping coordinates must have some aggregate chance of affecting it. The statement does not say any one coordinate must have large influence, but more sophisticated theorems, such as Kahn–Kalai–Linial, derive individual-coordinate information under additional assumptions.

## Which assumptions are being used?

All these clean formulas assume uniformly distributed, independent input bits and the plus-minus representation. For biased product distributions one builds a different orthonormal basis. For correlated inputs the characters need not be orthogonal. For real-valued outputs, Parseval still works, but the interpretation of influence as a flip probability requires modification.

Fourier analysis on the Boolean cube is useful precisely because it forces us to specify the probability space and the functions being studied. Once those details are fixed, arguments about majority votes, parity checks, randomized algorithms, threshold phenomena, and social choice can be made through the same coefficient language. A high-dimensional discrete problem becomes a set of spectral identities that can be calculated, compared, and bounded.

## Hypercontractivity: Why Boolean Functions Have Influential Coordinates

Imagine a decision made from millions of yes-or-no votes. We can ask whether one particular voter has substantial power to change the outcome. Or perhaps every voter has little individual power while the collective decision still responds sharply to a shift in public opinion. These questions sound political, but their mathematical content is about functions on a Boolean cube.

A Boolean function assigns an output of plus one or minus one to each vector of independent fair input bits. The Fourier expansion writes the function as a sum of products of coordinate variables. Each product corresponds to a subset of coordinates and has a coefficient measuring how much that interaction contributes.

A low-degree term depends on few coordinates. High-degree terms involve intricate interactions among many bits. Hypercontractivity is an inequality that constrains how concentrated a function can become after its higher-degree terms are suppressed. It is the bridge from algebraic Fourier expansions to inequalities about individual influences and sharp probability thresholds.

## Noise does not simply erase information

Introduce a noise operation. Start from an input vector, and independently keep each bit with some correlation parameter rho while refreshing the rest. The value of the original function and its value at the noisy input are correlated, but the correlation weakens as the noise increases.

In Fourier coordinates the noise operator is unusually simple: it multiplies a coefficient indexed by a subset of size d by rho to the power d. Degree zero is unchanged. Degree one is reduced by one factor of rho. Degree ten is reduced by ten such factors. The operator therefore damps complicated interactions more strongly than simple interactions.

This diagonal action is the first key insight. We can study noise by studying the degrees of Fourier coefficients, without following each possible noisy input separately. The analysis becomes a comparison between norms of a weighted polynomial.

## Two norms measure different kinds of size

The second moment of a function measures its average squared magnitude. The fourth moment is more sensitive to rare large values. A function that is usually near zero but occasionally very large can have a moderate second moment and a much larger fourth moment.

Hypercontractivity says that after enough noise has been applied, the fourth-moment norm cannot exceed the original second-moment norm. On the unbiased Boolean cube, a standard form is obtained when the correlation rho is at most one divided by the square root of three.

The phrase is worth unpacking. The noisy function may still contain many Fourier terms, but its large deviations are limited by the original energy. This is more informative than the elementary fact that noise decreases the second moment. We are controlling a stronger norm by a weaker one, made possible by smoothing.

## Check the inequality on two bits

Consider the function that adds the first two input bits. It can take values negative two, zero, or positive two. Its squared average is two, so its second-moment norm is the square root of two. Its fourth moment is eight, so its fourth-moment norm is the fourth root of eight.

After applying noise with correlation rho, both terms are simply multiplied by rho. The fourth-moment norm becomes rho times the fourth root of eight. If rho equals one over the square root of three, the result is smaller than the original second-moment norm, as hypercontractivity predicts.

This is not a proof of the theorem for arbitrary Boolean functions, but it makes the mechanism visible. A degree-one example has an easy response to noise. A high-degree monomial shrinks even faster. The difficulty is how many different monomials can combine to create large peaks. The tensor-product proof of hypercontractivity controls precisely that collective effect.

## From noise bounds to low-degree inequalities

Take a function whose Fourier expansion contains no degrees higher than d. We can start with a noisy version at correlation one over the square root of three and then compensate for the attenuation of each degree. Because each Fourier level is at most d, one obtains a bound on the fourth norm of the original low-degree polynomial by three to the power d over two times its second norm.

Thus low-degree functions cannot hide an arbitrarily large fourth moment while keeping the second moment fixed. The constant grows exponentially with degree, and this is appropriate: a polynomial of degree thirty can behave more sharply than a linear function. Hypercontractivity is not claiming that all Boolean functions are smooth or that high degrees are harmless.

The real use comes when a problem forces much of the Fourier mass to low levels, or when carefully chosen derivatives and restrictions have controlled degree. Then a moment inequality can translate algebraic structure into a probability bound.

## Influence measures sensitivity to one coordinate

The influence of coordinate i is the probability that flipping just that input bit changes the value of the function. For a plus-or-minus-one Boolean function, this equals a sum of squared Fourier coefficients over subsets containing i. The total influence equals the sum, over all nonempty subsets, of subset size times the squared Fourier coefficient.

This identity tells us where sensitivity lives in the Fourier spectrum. High-degree mass contributes strongly to total influence because each high-degree interaction includes many coordinates. But a function can distribute influence over many coordinates, making every single one small.

The Kahn-Kalai-Linial theorem places a limit on that distribution. For a balanced Boolean function on n unbiased independent bits, some coordinate has influence at least a constant times logarithm of n divided by n. This is stronger than the elementary average-influence lower bound of order one over n.

## Why a logarithm appears

A proof can be organized by taking discrete derivatives of the Boolean function, applying a hypercontractive inequality to those derivatives, and summing Fourier energies. If every derivative had too little mass, the variance of the original function could not remain as large as it is. The contradiction forces one influential coordinate.

Hypercontractivity enters because the derivatives are sparse in the sense that they are nonzero exactly when a bit is pivotal. Their second and higher moments encode the probability of that pivotal event. Comparing norms after noise turns tiny pivotal probabilities into a structural restriction on the Fourier coefficients.

The exact quantitative proof needs a choice of correlation parameter depending on the hypothesized maximal influence. That optimization is where the logarithm appears. It would be misleading to claim that one application of the moment inequality without any further argument already gives KKL.

## Sharp thresholds and the limits of the claim

Consider a monotone property of a randomly chosen subset: once the property holds, adding more elements cannot make it fail. Its probability increases as the inclusion probability rises. Russo's formula relates the derivative of this probability to the total influence at that inclusion probability. Thus influence lower bounds can imply that the transition from unlikely to likely happens over a narrow window.

But a sharp-threshold conclusion needs assumptions, such as monotonicity and conditions that prevent one coordinate from dominating. KKL in its usual form concerns Boolean-valued functions under a product measure. It cannot simply be transferred unchanged to arbitrary real-valued functions or arbitrary dependent inputs.

Examples clarify the scale. Majority voting has individual influences on the order of one over the square root of n. A carefully balanced tribes function spreads influence more evenly, with maximal influence of order logarithm n over n, showing the KKL scale is essentially optimal.

The lesson is that noisy smoothing can uncover rigidity. Fourier coefficients describe every interaction. Hypercontractivity controls how those interactions concentrate. Influence identities translate spectral energy into pivotal probabilities. Together they explain why a genuinely variable Boolean rule cannot hide all of its sensitivity equally well in every coordinate.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Block Designs, Finite Planes, and Hamming Codes

**Track:** Discrete Mathematics and Combinatorics. **Background:** incidence counting, finite fields, vector spaces, elementary coding theory. **Central question:** how can a small collection of subsets be balanced enough to support both experiments and error correction?

#### Mathematical companion (not spoken)

A \(2\text{-}(v,k,\lambda)\) design has b blocks, each of size k, such that each unordered pair of distinct points occurs in exactly \(\lambda\) blocks. If every point occurs in r blocks, incidence counting gives
\[vr=bk,\qquad r(k-1)=\lambda(v-1),\qquad b=\frac{\lambda v(v-1)}{k(k-1)}.\]
These are necessary conditions. For the Fano plane, \((v,b,r,k,\lambda)=(7,7,3,3,1)\).

**Explicit construction.** Let points be \(V=\mathbf F_2^3\setminus\{0\}\). For distinct u,v in V, the unique line through them is \(\{u,v,u+v\}\). There are \(\binom72/\binom32=21/3=7\) lines. Each nonzero vector belongs to three lines. A seven-by-seven incidence matrix B (rows points, columns lines) has \(BB^T=(r-\lambda)I+\lambda J=2I+J\) over the integers, not modulo two.

For the binary Hamming code, form \(H\in\mathbf F_2^{3\times7}\) whose columns are the seven nonzero binary triples. Then C=ker H has dimension \(7-3=4\) and minimum Hamming distance 3. For any line \(\{u,v,u+v\}\), its three indicator coordinates give a codeword because \(u+v+(u+v)=0\). A single error at position j has syndrome \(He_j=h_j\), identifying its column.

##### Exercises with answers

1. For a \(2\text{-}(9,3,1)\) design, what values of r and b are required? **Answer:** \(r=(9-1)/(3-1)=4\), \(b=9\cdot4/3=12\) (such designs exist as affine planes of order three).
2. Why can a parity-check matrix with two identical nonzero columns not correct every single error? **Answer:** flips in those positions give the same syndrome.
3. How many weight-three codewords arise from the Fano lines? **Answer:** seven, one for each line.
4. Why is minimum distance at least three for the seven-column construction? **Answer:** a nonzero kernel word of weight one needs a zero column; one of weight two needs two equal columns; neither exists.

##### Reading and source notes

- [MIT OpenCourseWare, Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), counting and finite-field prerequisites.
- [Encyclopedia of Mathematics, Block design](https://encyclopediaofmath.org/wiki/Block_design), incidence parameters and balance.
- [MIT OpenCourseWare, Information and Entropy, Chapter 4](https://ocw.mit.edu/courses/6-050j-information-and-entropy-spring-2008/71667aa5e13663096278c6617fca34e5_MIT6_050JS08_chapter4.pdf), the (7,4,3) Hamming code.

### Coding Bounds, Duality, and Probabilistic Codes

**Track:** Discrete Mathematics and Combinatorics. **Background:** finite fields, counting, random codes, Hamming distance, linear algebra. **Central question:** how many messages can we encode while guaranteeing correction of a given number of errors?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Compute `V(5,1)`. **Answer:** `1+5=6`.
2. For a binary code with `n=7,d=3`, what is the Hamming bound on `|C|`? **Answer:** at most `128/8=16`.
3. Why does puncturing `d-1` coordinates preserve distinctness? **Answer:** otherwise two original codewords would differ in at most `d-1` places, contradicting minimum distance d.
4. What is the dimension of the dual of an `[n,k]` binary linear code? **Answer:** `n-k`.

##### Reading and source notes

- [University of Maryland, Coding Theory and Applications](https://www.terpconnect.umd.edu/~abarg/ECC/), Gilbert-Varshamov, Hamming, Plotkin and duality lectures.
- [MIT, Essential Coding Theory course notes](https://people.csail.mit.edu/madhu/FT01/), coding constructions and distance bounds.
- [MacWilliams and Sloane, The Theory of Error-Correcting Codes](https://www.elsevier.com/books/the-theory-of-error-correcting-codes/macwilliams/978-0-444-85193-2), classical reference.

### Randomness Extractors: Recovering Usable Random Bits

**Track:** Discrete Mathematics. **Background:** entropy, concentration, finite fields, hash functions and probability distributions. **Central question:** when can a weak source be transformed into bits that behave almost uniformly?

#### Mathematical companion (not spoken)

A source X on `{0,1}^n` has `H_infty(X)=-log_2 max_x P[X=x]>=k`. A family H of maps to `{0,1}^m` is two-universal if for distinct x,x', `P_{h in H}[h(x)=h(x')]<=2^{-m}`. The leftover hash lemma gives, for independent uniform seed H,
\[
\Delta((H,H(X)),(H,U_m))\le\frac12\sqrt{2^{m-k}},
\]
where U_m is independent uniform, Delta is total variation distance, and the source is arbitrary subject to the entropy bound. (The standard collision-probability calculation yields this form.) For `k=100,m=80`, the bound equals `2^{-11}`. For `m=98`, it is `1/4`.

**Random-matrix family:** choose `A` uniformly from `F_2^{m x n}`. If `x != x'`, let `v=x-x' !=0`; each independent random row r has `r dot v` uniform. Then `P[Av=0]=2^{-m}`. The seed here is mn bits; this is a correctness example, not an optimal seed-length construction.

**No-go argument:** a fixed deterministic `f:{0,1}^n -> {0,1}` has an output fiber containing at least `2^{n-1}` inputs. A source uniform on that fiber has min-entropy at least `n-1` but constant f-output. This does not rule out deterministic extraction from structured source classes or multiple independent sources.

##### Exercises with answers

1. For min-entropy k=120, what is the leftover-hash bound for m=100? **Answer:** `2^{-11}`.
2. Why can't a general deterministic extractor work for all high-entropy sources? **Answer:** an adversary can choose the source to lie entirely in one large output fiber of the fixed function.
3. Do pseudorandom generators increase Shannon entropy beyond their seed length? **Answer:** no; deterministic transformations cannot increase entropy.
4. Does strong extraction permit a correlated seed? **Answer:** no; independence is part of the stated guarantee.

##### Reading and source notes

- [Nisan and Ta-Shma, Extracting Randomness: A Survey and New Constructions](https://doi.org/10.1006/jcss.1997.1546), extractor constructions and resource tradeoffs.
- [Dodis et al., Fuzzy Extractors: How to Generate Strong Keys from Biometrics and Other Noisy Data](https://eprint.iacr.org/2003/235), seeded extraction and related security models.
- [Vadhan, Pseudorandomness (lecture monograph)](https://people.seas.harvard.edu/~salil/pseudorandomness/), min-entropy, leftover hashing, extractors and pseudorandom generators.

### Fourier Analysis on the Boolean Cube

**Track:** Discrete Mathematics and Combinatorics. **Background:** probability, orthogonality, Boolean functions, and elementary harmonic analysis. **Central question:** how can a function of many bits be decomposed into independent interaction terms, and what does that reveal about noise and influence?

#### Mathematical companion (not spoken)

On the uniform cube `{-1,1}^n`, for `S subseteq [n]` define `chi_S(x)=prod_{i in S}x_i`. Then
\[
\widehat f(S)=\mathbb E[f(X)\chi_S(X)],\quad f(x)=\sum_{S}\widehat f(S)\chi_S(x),\quad
\mathbb E[f^2]=\sum_S\widehat f(S)^2.
\]
Because `chi_S chi_T=chi_{S triangle T}`, distinct characters are orthogonal. For Boolean `f in {-1,1}`, define influence `Inf_i(f)=P[f(X) != f(X^{(i)})]` with coordinate i flipped. Then
\[
\mathrm{Inf}_i(f)=\sum_{S\ni i}\widehat f(S)^2,\quad I(f)=\sum_S |S|\widehat f(S)^2,\quad
\mathrm{Var}(f)=\sum_{S\ne\varnothing}\widehat f(S)^2\le I(f).
\]
For a rho-correlated pair `(X,Y)` obtained by independently flipping X coordinates with probability `(1-rho)/2`, the noise stability is
\[
\mathbb E[f(X)f(Y)]=\sum_S\rho^{|S|}\widehat f(S)^2.
\]
For majority on three bits, `Maj_3(x)=(x_1+x_2+x_3-x_1x_2x_3)/2`. Fourier weights are `1/2` on each singleton and `-1/2` on the triple. Thus each influence is `1/2`, the total influence is `3/2`, and noise stability is `(3/4)rho+(1/4)rho^3`. For n-bit parity `f=chi_[n]`, each influence is 1 and stability is `rho^n`.

##### Exercises with answers

1. Find the Fourier coefficient of `f(x)=x_1x_3`. **Answer:** coefficient one at `{1,3}` and zero elsewhere.
2. What is total influence of full parity on n bits? **Answer:** n.
3. Evaluate three-bit majority noise stability at rho=0. **Answer:** zero.
4. Explain the Boolean Poincaré inequality in one line. **Answer:** `sum_{S!=empty} fhat(S)^2 <= sum_{S!=empty}|S| fhat(S)^2` because `|S|>=1`.

##### Reading and source notes

- [Ryan O'Donnell, Analysis of Boolean Functions](https://arxiv.org/abs/2105.10386), Fourier coefficients, influences, and noise stability.
- [Ryan O'Donnell, Analysis of Boolean Functions (book site)](https://www.cs.cmu.edu/~odonnell/), text and accompanying materials.
- [Ryan O'Donnell, author and book information](https://www.cs.cmu.edu/~odonnell/), official book and course resources.

### Hypercontractivity: Why Boolean Functions Have Influential Coordinates

**Track:** Discrete Mathematics and Combinatorics. **Background:** Fourier characters on the Boolean cube, probability, expectations, and basic norm inequalities. **Central question:** how does adding independent noise constrain the high-degree behavior of a Boolean function?

#### Mathematical companion (not spoken)

For uniform `x in {-1,1}^n`, define `chi_S(x)=product_(i in S) x_i`, `f=sum_S fhat(S) chi_S`, and `T_rho f=sum_S rho^|S| fhat(S)chi_S`. Bonami-Beckner hypercontractivity gives
\[
 \|T_\rho f\|_q\le\|f\|_p
 \quad\text{if }1<p\le q<\infty,\;0\le\rho\le\sqrt{\frac{p-1}{q-1}}.
\]
In particular, `||T_(1/sqrt(3)) f||_4 <= ||f||_2`. If `deg(f)<=d`, then `||f||_4<=3^(d/2)||f||_2`.

For `f:{-1,1}^n->{-1,1}`, `Inf_i(f)=Pr[f(x)!=f(x^(i))]=sum_(S includes i) fhat(S)^2`, and `I(f)=sum_S |S| fhat(S)^2`. For balanced Boolean f, the KKL theorem gives `max_i Inf_i(f)>=c log(n)/n` for an absolute c>0 and n>=2. General-variance versions require their corresponding constants and hypotheses. For `f(x)=x_1+x_2`, `E f^2=2`, `E f^4=8`, and `||T_rho f||_4=rho*8^(1/4)`.

##### Exercises with answers

1. What does noise do to a Fourier coefficient of degree five? **Answer:** multiplies it by `rho^5`.
2. For `f=x_1 x_2 x_3`, what is `||T_rho f||_2`? **Answer:** `rho^3` for nonnegative rho.
3. If f is plus-or-minus-one valued, why is `Inf_i` a Fourier energy? **Answer:** the discrete derivative squared is the pivotal indicator, and Parseval sums the squared coefficients containing i.
4. Does KKL imply every input has influence of order `log(n)/n`? **Answer:** no, only that at least one coordinate does.

##### Reading and source notes

- [Ryan O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf), hypercontractivity, KKL and sharp thresholds.
- [MIT OpenCourseWare, Analysis of Boolean Functions](https://ocw.mit.edu/courses/18-218-topics-in-combinatorics-analysis-of-boolean-functions-spring-2021/download/), lecture notes on influences and hypercontractivity.
- [Kahn, Kalai and Linial, The Influence of Variables on Boolean Functions](https://doi.org/10.1109/SFCS.1988.21923), original influence theorem and logarithmic lower bound.
