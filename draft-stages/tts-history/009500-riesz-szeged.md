# 009500 — Frigyes Riesz II: Szeged, persecution, and the mathematics of operators

**Track:** History · People and ideas. **Theme:** institution-building at Szeged, Nazi persecution, operator theory and mathematical legacy. **Background:** elementary sequences and linear operators; technical terms are explained.

<!-- BEGIN SPOKEN LECTURE -->

# Frigyes Riesz II: Szeged, persecution, and the mathematics of operators

## Rebuilding a mathematical institute after the war

In the early nineteen twenties, Frigyes Riesz was no longer the young secondary-school teacher who had first published his ideas about functions. He was an established mathematician helping a displaced university make a permanent home in Szeged. The university's own institutional history supplies a concrete picture of the beginning. The mathematics departments shared rooms on the ground floor of a building in Dugonics Square. One room held a library and an assistant; another was for journals. The mathematicians had a small number of rooms in which to teach, work, and receive visitors. The setting matters because the international reputation of the research school was not the result of generous facilities appearing fully formed.

Alfréd Haar was Riesz's essential colleague in this rebuilding. Together they organized a mathematics community and established the journal Acta Scientiarum Mathematicarum in nineteen twenty-two. The institute later formally took the Bolyai name. A journal was an infrastructure project as much as a publication: it could carry papers from Szeged to mathematicians abroad, draw foreign researchers into correspondence, and give students evidence that their local community belonged to an international conversation. Riesz edited and contributed to the journal. The Szeged research circle also included Tibor Radó, László Kalmár, Béla Kerékjártó, and others whose subjects ranged from topology and logic to geometry and mathematical physics.

University administration became part of Riesz's career. He held senior faculty responsibilities and served as rector in the academic year nineteen twenty-five to twenty-six. The university history records disagreements over appointments, classroom space, and the organization of departments. It also records a remarkable route by which support arrived. During a visit to Göttingen, a Hungarian education minister heard Richard Courant describe Szeged's international mathematical importance. Soon afterward the Szeged mathematics institute received additional backing. A researcher might write a brilliant paper, but it still took persuasion, ministers, buildings, assistants, and budgets to maintain the place where the next paper would be written.

## Working habits, visitors, and the limits of recollection

Accounts by people who knew Riesz describe an individual capable of great intellectual generosity but not always an easy collaborator. The American mathematician Edgar Raymond Lorch visited Szeged in nineteen thirty-four. He expected to speak French with Riesz; instead the older professor had recently taught himself English, partly through careful reading, and wanted to use it. Lorch remembered a deliberate, quiet manner, a sharp sense of humor, and an insistence on understanding the significance of theorems instead of recording a mere sequence of formal proofs. These are later recollections by a participant, rather than transcripts, and they should be presented as such.

Lorch also retold a story attributed to Tibor Radó about the difficulty of preparing a book with Riesz. Radó would organize lecture notes into a large draft, only to discover that Riesz had returned from the summer with a new way to present the subject. Whether every detail happened exactly as the anecdote was remembered is less important than the feature several accounts share: Riesz continued to rethink his explanations after the proof itself was known. The eventual functional-analysis textbook he produced with Béla Szőkefalvi-Nagy in nineteen fifty-two emerged from a much longer tradition of teaching, revision, and collaboration. Its joint authorship should never disappear behind the more famous senior name.

The Szeged community was not an idealized republic of equal opportunity. Departments disagreed about appointments, visitors depended on invitations, and a small number of students could study closely with a famous professor. Riesz's exacting expectations and particular temperament shaped who could learn from him directly. A later institute history says he often expected aspiring doctoral students to propose their own problems rather than await assignments. One of the things historical biography can provide is this picture of how a powerful mathematical style was transmitted—and of the people and arrangements that did the transmitting.

Other recollections complicate the portrait. Riesz liked the measured social world of rowing and fencing clubs, bridge, and the routines of Szeged, while remaining intensely absorbed in mathematics. He supported the younger László Kalmár and encouraged his development. István Vincze remembered a lecturer who could turn a digression into a lesson about how the field itself had grown. One should not confuse a quiet manner with a lack of temperament. Riesz could be amused, demanding, and occasionally impatient, traits that became particularly visible when younger colleagues tried to keep pace with his changing ideas.

The institutional story has a personal dimension. Riesz trained and influenced mathematicians in Hungary, and later worked with Béla Szőkefalvi-Nagy. Riesz and Szőkefalvi-Nagy jointly authored a major functional analysis textbook, first published in French in 1952. Its two parts combined integration, integral equations, linear functionals, and operator theory. The book drew on teaching carried out over years in Szeged and Budapest. It continued to appear in editions and translations, helping the subject acquire a common curriculum.

## Public recognition, a rejected appointment, and persecution

By nineteen thirty-six Riesz was widely recognized as a leading Hungarian mathematician. When a Budapest chair became available, Lipót Fejér wrote an extensive recommendation naming him the outstanding candidate. The university faculty nevertheless voted against the proposal. The ballot is documented; the motives of individual faculty members are not. The surrounding anti-Jewish climate makes discrimination an important issue for historians, but it would be poor history to assign private motives to every voter without evidence. Riesz continued his work at Szeged, including contributions to operator theory, ordered spaces, and ergodic ideas.

In March nineteen forty-four German forces occupied Hungary, and the situation for Jews deteriorated into organized persecution and deportation. Riesz, who came from a Jewish family, was forced from his professional position and subjected to anti-Jewish restrictions. Contemporary accounts describe efforts by colleagues and diplomatic representatives to shield him from more severe measures, but sources differ on the details and movements of his wartime survival. A planned visit to Geneva did not take place. None of those facts should be simplified into the claim that international fame made him safe. He survived; many members of the community around him did not.

The violence reached his family directly. His sister Margit, her husband Alfréd Szauer, and their daughter Zsuzsa were murdered at Auschwitz in nineteen forty-four. This is not a detail inserted to dramatize a mathematical career. It belongs to the documented family history and to the larger destruction of Jewish communities in Hungary. The surviving scholar's later honors do not cancel the loss. Nor can we reliably reconstruct every private thought he had about it from a university biography.

After the war, Riesz resumed institutional activity and ultimately moved to a Budapest professorship. In his final decade he took part in rebuilding Hungarian scientific life, received significant national and international recognition, and produced the French textbook with Szőkefalvi-Nagy. His last years were affected by declining health. Riesz died in Budapest in February nineteen fifty-six. The political regimes of his lifetime changed more than once, and the cities in which he worked acquired new names and borders. A historian cannot write that life as though an abstract theorem passed untouched through all those changes.

## The mathematical ideas behind the later career

These recollections and institutional records provide the setting. To understand the research that his colleagues recognized, we can now return to several mathematical ideas. The examples are deliberately small, and the hard theorems apply in much wider settings. The aim is to see what Riesz made possible in the theory of operators, not to turn his final decades into nothing but a catalogue of named results.

## From integral equations to compact operators

Consider an integral operator. It takes an input function, mixes its values according to a kernel, and produces a new function. Many such operators smooth their inputs. An oscillatory input may be transformed into a calmer output. That smoothing effect suggests that a very large collection of possible inputs might map into a comparatively constrained family of outputs.

In functional analysis, a compact operator is one for which the image of the unit ball has compact closure. In a metric setting, this means that every sequence of outputs from unit-length inputs has a convergent subsequence. The definition sounds abstract, so let us build a model using infinite sequences.

Take an input with coordinates x one, x two, x three, and so forth. Define an operator that leaves the first coordinate alone, divides the second by two, the third by three, and the nth by n. This is a diagonal operator with diagonal entries one, one half, one third, and so on. Every high-numbered coordinate is strongly suppressed.

To approximate this operator, keep its action on the first N coordinates and erase all later output coordinates. That approximation has finite-dimensional range. For an input of length at most one, the total length of the discarded output is at most one divided by N plus one. So the finite-rank operators approach the original operator in operator norm. In a Hilbert space, norm limits of finite-rank operators are compact. We have constructed a compact operator by suppressing infinitely many distant directions.

Compare that with the identity operator, which leaves every coordinate unchanged. The identity sends the unit coordinate vectors to themselves. Those vectors stay separated from one another by the same positive distance, so they have no convergent subsequence. The identity on infinite-dimensional square-summable sequence space is not compact. The difference is exactly what the diagonal entries did: when they tended to zero, far-away directions no longer survived at full size.

For a compact operator, nonzero spectral values behave in a way reminiscent of finite matrices. On an infinite-dimensional complex Banach space, every nonzero spectral point is an isolated eigenvalue of finite algebraic multiplicity, and zero is the only possible accumulation point of the spectrum. Zero itself requires care. It may be in the spectrum without being an eigenvalue, as happens for the diagonal example: none of its diagonal entries is zero, yet no bounded inverse exists because division by entries approaching zero would be unbounded.

This is a major part of Riesz's legacy in operator theory. In his 1918 work on linear functional equations, he treated questions of solvability and spectrum abstractly, in the tradition of Fredholm's theory of integral equations. The structure was useful precisely because the operator need not be presented as a symmetric matrix or admit an orthogonal eigenbasis. Compactness supplied enough control to recover a finite-dimensional obstruction to solving many equations.

## A small Fredholm calculation

We can see the obstruction without developing the entire theory. Use the diagonal compact operator just described, and consider an equation that asks for a vector x whose image under the operator called identity minus twice the compact operator equals a given vector y.

Look at the second coordinate. The compact operator divides it by two. Twice that is exactly the original second coordinate. When we subtract, the second coordinate disappears. No matter what number we choose for the second coordinate of x, the output's second coordinate is zero.

Two consequences follow. If the given vector y has a nonzero second coordinate, there can be no solution. If y has zero second coordinate, the second coordinate of x can be chosen freely, so a solution, when it exists, is not unique. The same one-dimensional eigendirection explains both the failure of existence for certain inputs and the failure of uniqueness for others.

In all the other coordinates, the corresponding diagonal multiplier is nonzero and bounded away from zero once we exclude the second coordinate. So those coordinates can be recovered by division, with a bounded inverse on the complementary subspace. The entire difficulty has been isolated in one finite-dimensional direction.

That is the flavor of the Fredholm alternative: for a compact perturbation of the identity, either the inverse exists or there is a nontrivial finite-dimensional obstruction, accompanied by precise solvability conditions. The formal theorem has hypotheses and an adjoint formulation that the companion spells out. The point of this calculation is to hear how an infinite system can fail for essentially finite-dimensional reasons.

It also explains why nonzero isolated spectral values are valuable. Around an isolated spectral point one can integrate the resolvent, the inverse of the operator shifted by a complex parameter, along a contour. The resulting spectral projection selects the associated invariant part. Such a projection provides a coordinate-independent way to discuss the spectral cluster, even when the operator is not normal. The modern Riesz projection construction is one of the tools that turns separation in the complex plane into a geometric decomposition of an operator.

## Order as another kind of structure

Riesz explored structures that did not begin with an inner product. Consider two real-valued functions on the same interval. We may compare them point by point. One lies below another if its value is never greater at any point. We can also form the function that takes the larger of the two values at each point, and the function that takes the smaller.

For a simple example, take the function whose value at position t is t, and another whose value is one minus t. On the left side of the interval, one minus t is larger. On the right side, t is larger. Their pointwise maximum makes a V-shaped corner at the midpoint, turned upward. It is still continuous. The pointwise minimum makes the complementary corner. These operations organize functions by order, without requiring a notion of angle.

A vector lattice, often called a Riesz space, is a vector space with a compatible order in which pairs of elements have a supremum and an infimum. It permits constructions such as positive and negative parts and absolute value within an ordered algebraic setting. Such structure is useful when inequalities, positivity, and monotone approximation are more natural than orthogonality. Riesz developed ideas leading to these spaces in the late 1920s and 1930s; further development involved other researchers, including Kantorovich and Freudenthal.

This is another reason to resist the idea that functional analysis is only Hilbert-space geometry. Some questions concern distance and perpendicularity. Others concern positive operators, monotonicity, or the order of functions. The same linear language can support different complementary structures. Knowing which structure a proof uses is often the key to understanding why a theorem is valid in one space but fails in another.

## Averages that settle down

Later in his career, Riesz also worked on ergodic theorems. Here the question changes from reconstructing a function to understanding repeated action over time. Suppose a transformation takes a vector to another vector of the same length. Apply it again and again. The individual states may keep moving forever. But perhaps their average stabilizes.

Picture a vector in the plane, rotated by a quarter turn each time. After four steps it returns to its starting position. It never approaches zero; its length is constant. Yet average its first four positions. The four arrows cancel exactly. If you average a very large number of successive positions, the result is close to zero because almost all terms can be grouped into complete four-step cycles.

Now add a third direction perpendicular to that plane, and suppose the transformation leaves this third direction fixed. Every rotated vector splits into two parts: a component in the rotating plane and a component along the fixed axis. The rotating part averages away. The fixed part survives unchanged. The long-time average is the orthogonal projection onto the subspace of fixed vectors.

For a unitary operator on a Hilbert space, the mean ergodic theorem makes this picture rigorous. The average of the first N iterates converges in norm to the projection onto the vectors unchanged by the operator. One way to understand the proof is to consider a vector of the form z minus its transform. When we average its successive images, the intermediate terms cancel. Only the first z and the final transformed z remain, divided by N. Because unitary transformations preserve length, that remainder tends to zero.

Vectors that can be approximated by such differences therefore have averages tending to zero. Vectors fixed by the transformation keep their value under averaging. A Hilbert-space decomposition then shows that these two kinds of behavior account for the whole space. The conclusion is a statement about average behavior; it does not say that the individual iterates converge.

John von Neumann established the mean ergodic theorem in the early 1930s. Riesz later contributed notably direct arguments and extensions, including work published in 1938. A theorem can gain new power from a proof that reveals which assumptions are essential. The rotating-vector picture shows why the argument is mathematical analysis rather than a claim that every orbit eventually settles down.

## What the representation idea made possible

We can now bring the mathematical threads together without collapsing their distinctions. In the Fourier problem, we began with a list of coefficients and asked for a function. Square-summability and completeness let us realize the data as a genuine object. In the Hilbert-space representation theorem, we began with a bounded measurement and found the vector hidden behind it. In the representation of functionals on continuous functions, we found that the correct representing object could instead be a measure. In compact-operator theory, a condition on the image of bounded sets helped us recover discrete spectral structure from an infinite-dimensional transformation.

Each step asks a similar type of question: what kind of object can be recovered from partial information, and what condition ensures that recovery is legitimate? But the hypotheses are different. The coefficient theorem uses orthogonality and square-summability. The Hilbert-space functional theorem uses a complete inner-product geometry and boundedness. The measure representation theorem uses the topology of continuous functions under the supremum norm. Compact-operator theory uses a form of finite-dimensional approximation. They belong to a common intellectual program without being special cases of one elementary formula.

These tools are still visible in contemporary spectral computation. An algorithm may represent a function by finitely many coordinates, approximate an operator by a matrix, and compute an approximate invariant subspace. The coordinate description is useful because of the correspondence with a larger function space. Bounded functionals allow residuals and outputs to be measured. Compactness or another spectral hypothesis may explain why particular eigenvalues are isolated. Orthogonal projection gives meaning to approximation error. And convergence in the appropriate norm is needed before any finite computation is allowed to speak for an infinite model.

The lesson is not that every modern perturbation bound follows from Riesz's papers. The historical connections are more specific. Riesz helped clarify what a vector may be, how an infinite family of coefficients can determine one, how linear measurements can be represented, and when infinite operators recover some of the tractability of matrices. His theorems gave later mathematicians reliable objects on which to formulate sharper questions about eigenvalues, invariant subspaces, and stability.

Return to the violin problem that helps make Riesz's early theorem concrete. Given an infinite list of tone strengths and the hope that they describe a sound, we can say what must be checked, what kind of convergence is promised, and what remains unresolved. We can construct a square-integrable waveform from square-summable orthogonal coefficients. We can measure it through bounded linear functionals. We can recognize that pointwise questions may require a different space and different tools. And when an operator acting on those objects has the necessary compactness, much of its nonzero spectrum can be studied through isolated, finite-dimensional pieces.

Frigyes Riesz's achievement was to make those transitions rigorous. His work showed how an infinite calculation can produce an actual function, how an abstract measurement can have a concrete representative, and how an infinite-dimensional operator can be understood through structural hypotheses rather than wishful analogy with finite matrices. The result was a language in which geometry, integration, and linear equations could be studied together—and a body of mathematics that endured even while the world containing its institutions was repeatedly disrupted.

From the rebuilding of Szeged to the persecution of nineteen forty-four, the story has not followed a smooth ascent toward scientific progress. It has followed a person who repeatedly had to work under changing institutional conditions, and who built a community while producing ideas now regarded as foundational. The functions, spaces, and operators remain worth learning in detail. Their history is richer once we remember the schools, journals, students, colleagues, and losses that surrounded them.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 5. Compact diagonal operator and Fredholm obstruction

Define \(T:\ell^2\to\ell^2\) by \((Tx)_n=x_n/n\). Its truncations \(T_N\) satisfy

\[
\|T-T_N\|=\sup_{n>N}\frac1n=\frac{1}{N+1}\longrightarrow0.
\]

Thus \(T\) is compact, with \(\sigma(T)=\{0\}\cup\{1/n:n\ge1\}\). The point 0 is spectral but is not an eigenvalue for this \(T\). For the equation \((I-2T)x=y\), the second coordinate requires \(y_2=0\). When this holds, \(x_2\) is arbitrary and the remaining coordinates have unique bounded recovery:

\[
x_n=\frac{y_n}{1-2/n}\quad(n\ne2).
\]

The denominators for \(n\ne2\) stay bounded away from zero, so this defines an element of \(\ell^2\). The example illustrates the finite-dimensional kernel/cokernel of a compact perturbation of the identity. It does not assert that an arbitrary bounded operator has discrete nonzero spectrum.

For a compact operator on a complex infinite-dimensional Banach space, nonzero spectral points are isolated eigenvalues of finite algebraic multiplicity, and zero is the only possible accumulation point. For an isolated spectral subset, the associated Riesz projection is defined by a contour integral of the resolvent; contour orientation and resolvent convention must be kept consistent:

\[
P=\frac{1}{2\pi i}\oint_\Gamma(zI-T)^{-1}\,dz.
\]

### 6. Order structure

In \(C([0,1],\mathbb R)\), set \(f(t)=t\) and \(g(t)=1-t\). The supremum in the pointwise order is
\((f\vee g)(t)=\max(t,1-t)\), and the infimum is \((f\wedge g)(t)=\min(t,1-t)\). Both are continuous. Lattice-ordered vector spaces (Riesz spaces) encode this structure without requiring inner products.

### 7. Mean ergodic averaging

For a unitary \(U\) on a Hilbert space,
\[
A_N=\frac1N\sum_{k=0}^{N-1}U^k,
\qquad
A_N(I-U)z=\frac{z-U^N z}{N}\xrightarrow[N\to\infty]{}0.
\]

On \(\operatorname{Fix}(U)\), \(A_N\) is the identity. Since
\(H=\operatorname{Fix}(U)\oplus\overline{\operatorname{Ran}(I-U)}\), the averages converge **in norm for each vector** to \(P_{\operatorname{Fix}(U)}\). This is a modern Hilbert-space exposition of the mean ergodic theorem; Riesz gave later elementary arguments and extensions, following von Neumann's earlier result.

### 8. Historical chronology and attribution

- **1880–1902:** Born in Győr, educated at Zürich, Budapest, Göttingen; doctorate in Budapest (1902). Frigyes Riesz and his younger brother Marcell Riesz had distinct research careers.
- **1907:** Three Riesz notes in *Comptes rendus* concerning orthogonal systems and \(L^2\), alongside Fischer's contemporary work. Horváth documents differences in formulation and inference.
- **1909:** Representation of functionals on continuous functions via bounded-variation/Stieltjes integration.
- **1911–1922:** Kolozsvár appointment; after geopolitical upheaval the university relocates to Szeged, where Riesz and Haar establish the Bolyai institute and *Acta Scientiarum Mathematicarum* (1922).
- **1918:** *Über lineare Funktionalgleichungen*, *Acta Mathematica* 41, 71–98, landmark abstract operator/Fredholm analysis.
- **Late 1920s–1930s:** Contributions to ordered vector spaces and ergodic analysis; 1938 mean-ergodic work.
- **1936–1945:** Budapest appointment rejected despite Fejér's strong recommendation (individual motives not documented); under 1944 German occupation Riesz is forced to retire and faces anti-Jewish restrictions. His sister Margit and her family are murdered in Auschwitz. He survives and resumes institutional service.
- **1952–1956:** *Leçons d'analyse fonctionnelle* with Béla Szőkefalvi-Nagy (1952); death in Budapest in February 1956.

## Reading notes (non-spoken)

The named sources in `metadata/009000.json` distinguish biographical chronology, Horváth's detailed reconstruction of the 1907 formulations, primary publications, institutional histories, and current explanations of compact-operator and representation theorems. Mathematical examples above are pedagogical constructions, not claims that Riesz used those particular coordinates. The 1936 rejection is documented; the motives of individual voters are not. Riesz and Fischer are separately credited for their original work, as are Fréchet, von Neumann, Haar, Szőkefalvi-Nagy, Markov, and Kakutani where relevant.

### Portrait readings and perspective (non-spoken)

- University of Szeged, *The history of the Institute*: https://www.math.u-szeged.hu/mathweb/index.php/en/erdekessegek/a-bolyai-intezet-toertenete
- Edgar Lorch and István Vincze, recollections hosted at MacTutor: https://mathshistory.st-andrews.ac.uk/Extras/Riesz_descriptions/
- Frigyes Riesz, MacTutor detailed biography: https://mathshistory.st-andrews.ac.uk/Biographies/Riesz/
- National Heritage Institute of Hungary, Riesz appointments and honors: https://intezet.nori.gov.hu/public/nemzeti-sirkert/budapest/fiumei-uti-sirkert/riesz-frigyes
- Frigyes Riesz, Wikipedia orientation: https://en.wikipedia.org/wiki/Frigyes_Riesz

The Lorch / Radó manuscript anecdote is a later secondhand recollection. The faculty rejection vote of 1936 is documented, but the individual voters' motives are not. The wartime sources agree on persecution and survival but differ in details of how Riesz avoided deportation; the narrative does not resolve this uncertainty by invention.
