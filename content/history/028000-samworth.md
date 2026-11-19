# 028000 — Richard J. Samworth: How can statistical methods remain trustworthy when data are scarce or complicated?

**Track:** History · People and ideas. **Theme:** Shape constraints, resampling, high-dimensional statistics, and spectral inference. **Background:** probability, elementary statistics, eigenvalues and covariances; the lecture defines its particular methods.

<!-- BEGIN SPOKEN LECTURE -->

# Richard J. Samworth: How can statistical methods remain trustworthy when data are scarce or complicated?

A researcher has sixty observations and five hundred possible measurements for each one. She wants to predict an outcome, discover which measurements are useful, and report how certain she is. A classical statistical approach might estimate an enormous covariance matrix, invert it, and test a model fitted to all the measurements. But a matrix with five hundred rows and columns cannot have full sample covariance rank when it is estimated from only sixty centered observations. Even if a computer returns numbers, there may be no defensible reason to trust them.

There are several ways out. We might assume that only a small set of measurements is important. We might assume that the probability distribution has a particular shape. We might take repeated subsamples and ask whether a selected variable persists. We might compress the data into lower-dimensional projections. Or we might seek a theorem that translates a small matrix-estimation error into a reliable statement about the directions of largest variation.

Richard J. Samworth has worked on all these kinds of questions. His research in nonparametric and high-dimensional statistics asks what can be inferred without forcing reality into a convenient but inaccurate statistical model. He is a professor of statistical science at the University of Cambridge, director of its Statistical Laboratory, and a fellow of Saint John's College. His research touches classification, density estimation, variable selection, independence testing, missing observations, and change-point detection. He is also a coauthor with Yi Yu and Tengyao Wang of a widely used 2015 refinement of the Davis–Kahan subspace perturbation theorem.

There are two complementary stories in this portrait. One concerns a mathematician and a research community at Cambridge in the decades after the turn of the millennium. The other concerns a family of statistical techniques that respond to the same recurring difficulty: the data we have are finite, noisy, and imperfectly observed, but our conclusions are meant to describe something larger than the sample.

## Cambridge and the rise of high-dimensional inference

Samworth completed his doctorate in statistics at Cambridge in two thousand four. He was subsequently a research fellow at Saint John's College before taking a position in the Statistical Laboratory. In two thousand seventeen he was appointed to the Professorship of Statistical Science. Cambridge identifies him as director of the Statistical Laboratory and lists research interests ranging from shape-constrained estimation to statistical foundations of artificial intelligence. He was elected a Fellow of the Royal Society in two thousand twenty-one, a recognition of his contributions to statistical theory and methodology.

This chronology is documented in institutional biographies and publication records. The public sources give abundant information about his mathematics, students, collaborators and professional positions, but little detail about his childhood or private life. It would be inappropriate to manufacture a more colorful personal history. His intellectual trajectory can instead be followed through the problems he and his collaborators chose, the methods they developed, and the influence of those methods on statistical reasoning.

When he entered research, statistical applications were undergoing a major change. Improvements in measurement and computation made it possible to record thousands or millions of variables. Genomics, imaging, and complex scientific instruments all produced data where the number of candidate features could rival or exceed the number of independent observations. The difficulty was deeper than having a large spreadsheet. Many familiar estimators had been designed for situations where the number of parameters stayed small as the sample size grew. In a high-dimensional setting that approximation could be badly misleading.

Consider the sample covariance matrix of a data table with sixty rows and five hundred columns. After centering each column, the matrix of observations has rank at most fifty-nine. Multiplying its transpose by itself produces a five-hundred-by-five-hundred covariance matrix, but the rank is still at most fifty-nine. At least four hundred forty-one directions have estimated sample variance exactly zero. Those zeros need not mean the population has zero variation in those directions; they are a consequence of limited observations.

If we tried to build a classical discriminant classifier using the inverse of that covariance, the inverse would not exist. If we attempted to identify the true explanatory variables by simply fitting the response with all five hundred predictors, multiple coefficient vectors could give identical fits. Even an excellent numerical algorithm cannot recover information the data do not contain without additional assumptions. The right response is to ask which structural assumptions are plausible and which inferential guarantee follows from them.

That question connects Samworth's contributions to a broad tradition in mathematical statistics. He has repeatedly returned to ways of making relatively weak, interpretable assumptions yield precise performance bounds. Two especially revealing themes are probability distributions whose shape is constrained, and procedures whose stability is tested by perturbing the data.

## A probability density with a controlled shape

Suppose we observe the heights of many adults and want to estimate a smooth probability density. A conventional technique places a small bump at every observation and averages the bumps. This is kernel density estimation. The width of each bump has a large effect on the answer. Too small a bandwidth produces many artificial peaks. Too large a bandwidth smooths away real structure. Selecting the bandwidth is a statistical problem of its own.

But imagine we have a reason to expect the density to be log-concave. This means that the logarithm of the density is a concave function wherever the density is positive. A normal distribution satisfies that condition. So do many other distributions. Log-concavity is more flexible than choosing one named parametric family, but it restricts the density to a coherent class. In one dimension a log-concave density cannot have two separated interior peaks with a valley between them. It has a strong unimodal structure, although a probability density can have flat regions or skewness.

For a simple example, take a density proportional to the exponential of minus the absolute value of x. The logarithm is a constant minus the absolute value of x. Since absolute value is convex, its negative is concave. The density therefore satisfies log-concavity. Its graph has a sharp peak at zero rather than the rounded peak of a Gaussian. A second example is the uniform distribution on an interval, interpreted as a log-concave density whose support is convex. These examples show that the assumption defines a broad shape class instead of one bell curve.

In two thousand ten Madeleine Cule, Richard Samworth and Michael Stewart published a major paper on maximum likelihood estimation of a multidimensional log-concave density. Their analysis established existence and almost-sure uniqueness of the log-concave maximum likelihood estimator under the stated sampling conditions, and investigated how to compute it using convex optimization and computational geometry. The method can estimate a multivariate density without a smoothing bandwidth specified by the user.

Why does concavity help? Suppose we want to maximize the product of the estimated density values at our observations, subject to the requirement that the density integrates to one. In an unrestricted class of densities, likelihood can be made arbitrarily large by placing narrow spikes at the observations. There may be no sensible maximizing density. The log-concavity constraint prevents this kind of spike-by-spike overfitting and gives the optimization a more tractable mathematical structure.

We can visualize that constraint from three points in one dimension. If the estimated log density has a certain height at the first and third points, concavity forces its height at an intermediate point to lie above the straight chord connecting them. We cannot put a deep artificial valley between two high values. In higher dimensions the same principle applies along every line segment in the support. Convex geometry becomes part of statistical estimation.

Shape constraints are not a universal cure. If the real population distribution has two separated modes, perhaps representing two distinct subpopulations, then a single log-concave density may be systematically inappropriate. As the sample grows, the estimator can converge toward an optimal log-concave approximation rather than the true non-log-concave density. The value of the method depends on whether the structural assumption fits the scientific question.

Samworth later surveyed developments in log-concave density estimation, describing both the mathematical theory and methods for making the estimator computationally practical. This body of work illustrates a characteristic trade-off in modern statistics: by replacing an arbitrary smoothness tuning parameter with a structural assumption, we can gain mathematical control, but the assumption must remain visible to users of the method.

## A variable that survives a second sample

Now return to the researcher with five hundred candidate predictors. Suppose a selection algorithm finds twelve variables associated with an outcome. Are these twelve real signals, or did the procedure latch onto accidental correlations in the sample? One natural diagnostic is to rerun the analysis on subsets of the data. A useful variable should often appear again. A fragile false positive might disappear when a few observations are changed.

The idea of stability selection was introduced by Nicolai Meinshausen and Peter Bühlmann. Its essential move is to repeatedly select subsets of observations, apply a variable-selection procedure, and record how frequently each variable is selected. A high frequency provides evidence of stability. But turning that frequency into a guarantee about erroneous selections is subtle. We must distinguish how the algorithm behaves under subsampling from what is actually true about the underlying population.

In a paper published in the Journal of the Royal Statistical Society, Rajen Shah and Richard Samworth developed complementary pairs stability selection. They paired disjoint subsets of the observations and used the joint behavior of the selection procedure to derive error bounds. Their theory controlled, under minimal or explicitly stated additional assumptions, quantities such as the expected number of variables selected frequently even though their ordinary selection probabilities were low. It also studied the reverse error: high-probability variables excluded by the stability rule.

Try a small thought experiment. We have six candidate variables, and the base algorithm selects two on each run. A genuinely persistent variable is selected in nine of ten runs. Another is selected in three. A third appears only once. If our threshold is eight out of ten, only the first survives. The threshold is easy to apply, but the mathematical issue is whether it controls false inclusions, how dependent the runs are, and what properties of the base selection procedure can be assumed. Reusing overlapping subsets does not magically create independent observations.

Complementary pairs help the analysis because the two halves of a partition can be studied together. There are useful inequalities linking the probability of selection in both halves to the original selection probability. The precise error estimates depend on how many variables the base procedure selects and on the shape assumptions imposed on the distribution of selection frequencies. It is not correct to say that every highly selected variable is necessarily scientifically causal or even genuinely associated. The guarantee has a specific target, and its assumptions have to be checked.

An important feature of the Shah–Samworth work is that their basic bounds avoid imposing a full stochastic model for every predictor. They examine the selection procedure as an object whose random response to data perturbation can be controlled. This theme runs through many later statistical methods: use randomization and repetition to reveal which part of an analysis is robust, then turn that empirical behavior into a mathematical statement.

## From covariance error to the angle between subspaces

The 2015 paper by Yi Yu, Tengyao Wang and Richard Samworth addresses a different form of statistical uncertainty. Instead of asking whether a list of selected variables is stable, suppose we have estimated a covariance matrix and want to know whether its leading eigenvectors are close to those of the population covariance. The connection to inference is immediate: a principal-component model may be used to compress many measurements into a few directions, but those directions were computed from finite data. How accurately have we recovered the population subspace?

Let us begin with a two-dimensional example. A population covariance matrix has variance three along the horizontal direction and variance one along the vertical. Its leading principal component is the horizontal axis. Now suppose the estimated covariance has the same diagonal entries but a small off-diagonal entry of one half. The estimate says the two coordinates are somewhat correlated. Its leading eigenvector is tilted relative to the true horizontal direction.

How far does it tilt? For a symmetric two-by-two matrix with diagonal entries a and d and off-diagonal entry b, the angle theta of a leading eigenvector satisfies a double-angle relation: the tangent of twice theta is two b divided by a minus d, when the leading eigenvalue is simple and the branch is chosen correctly. Here twice b is one and a minus d is two. So twice the angle has tangent one half, and the angle itself is about thirteen degrees. The rotation is visible but moderate.

Now keep the off-diagonal entry one half and bring the population variances closer together, say from three and one to two point one and one point nine. The denominator in the double-angle relation has fallen from two to point two. Twice the angle now has tangent five, and the leading direction turns by about thirty-nine degrees. We made no increase in the off-diagonal error. We merely reduced the population eigengap. The same observed correlation can produce a small or large change in the principal direction depending on how distinct that direction was to begin with.

If the two population variances become exactly equal, the population covariance has no preferred one-dimensional eigendirection. Every axis is a leading eigenvector. Asking whether an estimated leading vector is close to a unique population direction no longer makes sense. A statistical theorem must represent that ambiguity, rather than hide it behind a numerical tolerance.

Classical Davis–Kahan perturbation theory provides bounds on the principal angles between invariant subspaces of symmetric or self-adjoint operators. But a frequently used version requires a spectral separation involving both population and estimated eigenvalues. In statistics the estimated eigenvalues are random; establishing their separation can require another layer of argument. That motivated the 2015 collaboration. Yu, Wang and Samworth derived a useful variant controlled by a gap between population eigenvalues alone.

The result is easiest to understand for one leading direction. Suppose the population covariance has a strict gap between its largest and second-largest eigenvalue. The sample covariance is the population matrix plus an error matrix. Then the sine of the angle between leading eigenvectors can be bounded above by a constant times the operator norm of that error divided by the population gap. The familiar constant in the paper's general statement is two. This remains a valid upper bound even when it exceeds one and offers no useful information. The guarantee becomes informative when the estimation error is small compared with the eigengap.

For a block of several adjacent eigenvectors, the theorem measures the angles between the spans. The correct comparison is between subspaces rather than between a particular pair of bases. If the target block contains two nearby or repeated population eigenvalues but is well separated from the rest, the whole two-dimensional space may be stable even when individual eigenvectors within it are free to rotate substantially. That is important when a scientific application cares about a low-dimensional representation rather than the names attached to its coordinate axes.

There is an additional choice of matrix error measure. The Frobenius norm squares and sums all matrix entries. The operator norm takes the largest amplification of a unit vector. For a target block of d directions, the 2015 theorem uses the smaller of the Frobenius norm of the perturbation and the square root of d times its operator norm, with a factor of two and the population eigengap in the denominator. Thus a large ambient dimension does not automatically make the bound pay the full cost of all its entries.

This gives the statistician a clean proof pattern. First, prove that an estimated covariance differs from the population covariance by at most epsilon in operator norm, with probability at least ninety-five percent, under a specified sampling model. Second, apply the deterministic subspace inequality on every sample outcome where that error bound holds. The resulting statement gives a ninety-five percent probability guarantee for the principal-angle error, provided the fixed population gap is positive. The perturbation theorem supplies the geometry. The concentration theorem supplies the probability.

The authors also treated singular subspaces for nonsquare matrices, where a rectangular data or signal matrix has different left and right singular directions. One cannot simply assume that an eigenvector theorem for symmetric covariance matrices solves every such problem. The rectangular statement follows by careful use of singular-value geometry, with an appropriate gap in squared singular values and terms depending on the dimensions and spectrum of the matrices. This generalization made the work relevant to low-rank matrix estimation and related high-dimensional procedures.

The historical attribution is shared: this is a joint result of Yu, Wang and Samworth. The mathematicians' research programs crossed in the Cambridge Statistical Laboratory, and the paper grew out of a statistical need that classical spectral geometry could address more conveniently after its hypotheses were reorganized. Samworth's wider contribution is clearer when this paper is placed among his research on the limits of estimation, rather than treated as an isolated improvement to a matrix inequality.

## Compressing a dataset without deciding its important coordinates in advance

There is another way to handle five hundred measurements and only sixty observations. Perhaps the information needed for classification lives largely in a low-dimensional subspace, but we do not know which original variables matter. Selecting a few coordinate columns would then be too restrictive. We might instead choose random linear combinations of all the columns and perform classification on the resulting smaller vectors.

This is the starting point of random-projection classification. A random projection sends a high-dimensional vector to a vector in a much smaller space. We can imagine choosing a plane through a cloud of points in ten dimensions and looking at the shadow cast onto that plane. Some shadows conceal the distinction between two groups. Others reveal it. If the original groups differ along a low-dimensional combination of coordinates, a suitable projection can make that difference accessible to a simpler classifier.

In two thousand seventeen Timothy Cannings and Richard Samworth published Random-projection ensemble classification. Their method repeatedly creates lower-dimensional projections, fits base classifiers, compares candidate projections using estimated classification performance, and combines the results. It can be used with different base classifiers rather than requiring one fixed parametric discriminant model. Their analysis quantifies how ensemble approximation changes as the number of projections grows and studies conditions under which its excess classification risk can be controlled without a direct dependence on the original ambient dimension.

For a tiny example, imagine observations of two species, recorded using one hundred measurements each. Only a certain combination of measurements strongly separates them, and the direction is not aligned with any single original coordinate. Projecting onto the first five raw coordinates may throw away the signal. A random five-dimensional projection has some chance of retaining part of the separating direction. A collection of candidate projections increases the chance that at least some reveal useful separation. Aggregating their predictions helps reduce dependence on any one accidental projection.

There is a tempting but incorrect interpretation here. Because random projections sometimes preserve distances approximately, one might infer that every random low-dimensional projection preserves the information needed for classification. That is false. If the target dimension is too small, or if the predictive direction has been badly compressed, the classes may overlap almost completely in the projection. The useful mathematical statement depends on assumptions about the classification boundary and the projection-selection procedure, not simply on the presence of randomness.

The work also makes us distinguish an algorithm from its idealized limit. An ensemble with infinitely many random projections is a mathematical object whose classification risk can be studied. A computer uses finitely many projections, and its prediction may fluctuate across random seeds. A good theorem should say something about the approximation introduced by using a finite ensemble, as well as the quality of the underlying statistical decision rule.

This connects to the problem of stability selection, but with a different output. In one case, resampling helps assess which variables persist in a selected set. In the other, random projections help construct many lower-dimensional views whose predictions are combined. Both methods recognize that a high-dimensional analysis can gain strength from deliberately varying part of its computation and studying what survives.

## The difference between detecting dependence and explaining it

Samworth's research also addresses independence testing. Suppose we observe paired measurements: a person's time outdoors and a measure of sleep. We want to know whether the variables are independent. Correlation offers a familiar first check, but it measures a particular kind of linear association. Two variables can have zero correlation yet be strongly dependent. If one is the square of a symmetrically distributed other, for example, its correlation with the original variable may be zero even though one is determined by the other.

A general independence test should be sensitive to much more than correlation. One strategy compares a joint distribution with the product of its marginal distributions. Under independence, those two distributions are equal. Departures from equality indicate dependence. But in a very broad class of possible distributions, distinguishing independence from every imaginable dependence pattern is impossible with uniform statistical power at a fixed sample size. A dependency can be concentrated in a small, irregular part of the sample space, making it hard to detect without structural assumptions.

In two thousand twenty-one Thomas Berrett, Ioannis Kontoyiannis and Richard Samworth developed a theory of independence testing using U-statistics and permutation calibration. Their work studied optimal rates under smoothness assumptions and showed why some restrictions are necessary for powerful nonparametric tests. The idea of permutation calibration is intuitive. If two sequences of observations are independent under the null hypothesis, pairing the first sequence with a randomly shuffled order of the second should not systematically change the distribution of a test statistic. We can compare the observed statistic with the statistics obtained after many such shuffles.

Imagine four paired observations where one variable is the square of the other. The original pairings display a rigid relationship. After shuffling the second coordinates, that pattern is usually disrupted. A statistic designed to detect general dependence may therefore be large for the original sample compared with most shuffled versions. The exact type-one error control of a permutation test depends on exchangeability under the null and the calibration procedure. It is not a guarantee of high power against every dependent alternative.

The use of smoothness assumptions in the Berrett–Kontoyiannis–Samworth analysis makes the general message concrete: statistical reliability often comes from stating what kinds of hidden structure we can reasonably hope to detect. If the class of possibilities is unrestricted, even a perfectly calibrated test may be ineffective against some alternatives. A theorem is valuable when it states both the achievable rate and the limits of the method.

## What happens when the data were never recorded?

A theme of Samworth's later work is the distinction between an observation that happens to be missing and an observation that is missing for a reason. Suppose a hospital collects blood pressure measurements and a lengthy questionnaire. Patients who are very ill may be less likely to complete the questionnaire. If we analyze only the patients who answered every question, the resulting sample can be systematically different from the group we hoped to describe.

Statisticians distinguish several missing-data regimes. Under missing completely at random, the chance that a measurement is missing does not depend on either observed or unobserved values. Under missing at random, the missingness may depend on what we have observed but, conditional on those observations, does not depend further on the missing value. When neither condition holds, the missingness mechanism can itself carry information about the unobserved outcome. Different assumptions lead to different identification and estimation problems.

Consider a binary survey question whose true population answer is yes for half of respondents. If answers are missing completely at random, the fraction of yes responses among the people who replied remains an unbiased estimator of the population fraction, assuming everyone has the same response probability. But suppose a yes answer makes someone much less likely to reply. The responders will contain too few yes answers. Repeating the survey with a larger sample reduces sampling variability but does not remove that bias. We need additional information or restrictions on the response mechanism.

In two thousand twenty-two Zhu, Wang and Samworth studied high-dimensional principal component analysis with heterogeneous missingness. Some matrix entries are observed reliably, while others are missing at different rates. Ordinary principal components computed after naïvely filling missing entries with zeros can point in the wrong direction. The challenge is to estimate a low-rank structure while accounting for where observations are absent. One aspect of the research is computational, because different observation patterns change which spectral algorithms are effective. Another is statistical, because some low-rank directions may be much harder to identify than others.

By two thousand twenty-six, Samworth's publication record included joint research on estimation beyond the familiar missing-completely-at-random framework, as well as other methods for inference with missing covariates. These problems are not reducible to the 2015 angle theorem. They show the breadth of a program concerned with what data permit us to conclude under explicitly stated limitations.

Take a rectangular signal matrix with a strong rank-one structure. If every row is observed but half the columns are missing systematically for one subgroup, estimating the shared direction is not the same problem as if each cell were independently deleted with the same probability. A method designed for one missingness pattern can fail for the other. The geometry of the signal, the probability law governing which entries are observed, and the amount of missing data all contribute to the error guarantee.

The same pattern of reasoning appears across these problems. A statistician first specifies the object to be estimated, then a model for what is observed, and finally an inequality translating observable or controllable error into the target of interest. Shape constraints, stability selection, spectral perturbation, random projections and missing-data methods make different assumptions. Their common discipline is to state those assumptions instead of overlooking them.

## The research community and the role of mathematical statistics

Cambridge's Statistical Laboratory has a long history as a place where theoretical research meets problems drawn from science and public life. Samworth's career has involved doctoral supervision, teaching, editorship and the maintenance of such a research community. His institutional profile describes work in nonparametric and high-dimensional statistics, including classification, change points, independence tests, density estimation and methods connected with modern artificial intelligence. The Cambridge Statistics Clinic, which he runs, gives researchers from other areas of the university access to statistical advice. That practical role is part of what it means for mathematical statistics to be a living discipline rather than a sequence of abstract probability proofs.

Recognition followed this research. He received the COPSS Presidents' Award and the Royal Statistical Society's Guy Medal in Bronze, among other honors. In two thousand twenty-one he was elected to the Royal Society. In two thousand twenty-five he received the Guy Medal in Silver and was one of the inaugural recipients of the David Cox Medal for Statistics, an award recognizing contributions to methodology and theory, particularly shape-constrained modeling and change-point analysis. He also held a European Research Council Advanced Grant supporting continuing research. These are facts about an active career, not a final summary of someone whose work has ended.

Samworth's career is ongoing. His published research already traces a path from nonparametric density estimation through stability and classification to spectral statistics, independence testing, and missing-data inference. These topics are linked by an interest in statistical conclusions that remain reliable when the available information is incomplete or high-dimensional.

Return to the investigator with sixty observations and five hundred measurements. We cannot promise that any mathematical trick will extract the truth without assumptions. A log-concavity restriction may make density estimation manageable, but it can distort a multimodal distribution. Subsampling can reveal an unstable selection, but repeated selection is not proof of causality. Random projections can make a classifier practical, but they can erase a predictive direction. A population eigengap can turn a covariance-error bound into an angle guarantee, but the result weakens as the gap vanishes. A permutation test can control false positives under its null, while having limited power against some alternatives. And a larger sample can still be biased when missingness depends on the outcome.

What Samworth's research helps clarify is the division of labor in a trustworthy statistical argument. The scientific problem determines what we want to learn. A model records the assumptions we are willing to make. An estimator or test supplies a procedure that can run on finite data. A theorem then states how the procedure behaves and where its limits lie. When those pieces are kept distinct, sophisticated matrix geometry and high-dimensional probability become tools for reasoning about evidence rather than sources of confidence that the data have not earned.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. Rank of the sample covariance

For \(n\) centered observations \(x_i\in\mathbb R^p\), the sample covariance \(\widehat\Sigma=X^{\mathsf T}X/(n-1)\), where the rows of \(X\) sum to zero, obeys
\[
\operatorname{rank}(\widehat\Sigma)\le\min(p,n-1).
\]
With \(n=60\), \(p=500\), at least \(500-59=441\) zero sample eigenvalues exist regardless of the true covariance's rank.

### 2. Log-concavity and its role

A density \(f\) is log-concave when \(f(tx+(1-t)y)\ge f(x)^t f(y)^{1-t}\) for \(0<t<1\), with the usual conventions on zero values. The Laplace density \(f(x)=\frac12\exp(-|x|)\) is log-concave; the uniform density on any convex body is also log-concave, with extended-real log density. The unrestricted nonparametric likelihood need not have a well-behaved maximum, while Cule–Samworth–Stewart (2010) establish almost-sure existence/uniqueness of the log-concave MLE for their sampling setting and study its computation.

### 3. Complementary pairs stability selection

For a base selector \(\widehat S\) run on subsamples, define selection frequency \(\widehat\pi_j\) for feature \(j\); retain features above a chosen threshold. Pairing disjoint half samples makes it possible to estimate joint selection behavior and bound false inclusion/exclusion quantities. Shah–Samworth (2013) gives bounds for variables with selection probabilities under/over specified thresholds. These results do not make variable inclusion a proof of causality or automatically guarantee model-free family-wise error control.

### 4. Two-dimensional eigenvector rotation

For \(M=\left(\begin{smallmatrix}a&b\\b&d\end{smallmatrix}\right)\) with \(a>d\), the leading eigenvector makes \(\theta=\tfrac12\arctan(2b/(a-d))\) with the horizontal axis. With \((a,d,b)=(3,1,0.5)\), \(\theta\approx 0.2318238\) radians, or \(13.2825^\circ\). With \((2.1,1.9,0.5)\), \(\theta\approx0.6867004\) radians, or \(39.3450^\circ\). The off-diagonal perturbation has identical norm in both examples, but the population eigengap changes.

Yu–Wang–Samworth (2015), for adjacent block positions \(r,\ldots,s\) and positive \(\delta=\min(\lambda_{r-1}-\lambda_r,\lambda_s-\lambda_{s+1})\), omitting nonexistent boundary terms, provides
\[
\|\sin\Theta(\widehat V,V)\|_F
\le \frac{2\min\{\sqrt{d}\,\|\widehat\Sigma-\Sigma\|_{\mathrm{op}},\,\|\widehat\Sigma-\Sigma\|_F\}}{\delta},\qquad d=s-r+1.
\]
This is a theorem about symmetric matrices and the corresponding indexed eigenspaces, not an assertion that a covariance concentration bound holds without sampling assumptions. The rectangular variant has additional spectral and dimension-dependent factors and should be consulted in the original paper rather than replaced by the symmetric formula.

### 5. Random projections and conditional limitations

Cannings–Samworth (2017) combine random low-dimensional projections, projection selection by estimated classification risk, and aggregation. Their theoretical performance statements involve boundary and classification assumptions; a random projection does not preserve arbitrary labels or sufficient predictive information automatically.

### 6. Permutation inference

Berrett–Kontoyiannis–Samworth (2021) study \(D(f)=\int (f(x,y)-f_X(x)f_Y(y))^2\,dx\,dy\) where densities exist and integrability holds, with U-statistic-based permutation tests. The smoothness assumptions are essential for some minimax-rate conclusions. Permutation calibration under the null and power against specified alternatives are distinct questions.

### 7. Biographical chronology and source guidance

- PhD in Statistics, University of Cambridge, 2004; subsequently a research fellow at St John's and later member of the Statistical Laboratory.
- Professor of Statistical Science from 2017; director of the Cambridge Statistical Laboratory; elected Fellow of the Royal Society in 2021.
- 2010: Cule–Samworth–Stewart log-concave density MLE. 2013: Shah–Samworth complementary pairs stability selection. 2015: Yu–Wang–Samworth population-gap perturbation theorem.
- 2017: Cannings–Samworth random-projection ensemble classification. 2021: Berrett–Kontoyiannis–Samworth independence testing. 2022: Zhu–Wang–Samworth high-dimensional PCA with heterogeneous missingness.
- 2025: inaugural David Cox Medal and Royal Statistical Society Guy Medal in Silver. Relevant 2026 publications concern missing data and inferential procedures.

The subject is living. This portrait uses public career and bibliographic material and does not invent family background, motives, or private biographical incidents. Sources and dates are recorded in `metadata/sources.json`.
