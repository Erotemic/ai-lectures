# 025000 — Harold Hotelling: How did subspace geometry become statistical inference?

**Track:** History · People and ideas. **Theme:** Statistical subspaces. **Background:** elementary covariance, eigenvectors, and correlation; the lecture introduces its statistical constructions.

<!-- BEGIN SPOKEN LECTURE -->

# Harold Hotelling: How did subspace geometry become statistical inference?

Imagine a school with thousands of pupils. Every pupil has a score in arithmetic, reading, writing, memory, and speed of response. Now imagine being handed a large table containing all those scores, without any explanation of what patterns you ought to seek. You could compute the average arithmetic score. You could look for pupils who excel in reading. But suppose that arithmetic and reading tend to rise together, while two different measures of speed tend to rise and fall together for other reasons. The table may contain many columns but fewer distinct directions of variation.

There are at least three mathematical questions hiding inside that observation. First, which linear combination of the scores varies the most? Second, if we divide the scores into two groups, which combination from the first group is most closely associated with a combination from the second? Third, when a sample suggests an association, how can we tell whether we have seen a dependable feature of the population or an accident of finite observations?

Harold Hotelling helped bring all three questions into the center of twentieth-century statistics. The first became the language of principal components. The second became canonical correlation. The third connects them to multivariate inference, to confidence regions, and eventually to the stability of estimated subspaces. There was geometry here before Hotelling. Karl Pearson and others had already studied best-fitting lines and planes. Hotelling's work made the geometric viewpoint part of a larger statistical enterprise: one with random samples, measurements made on individuals, estimates of population parameters, and formal statements about uncertainty.

The person behind these ideas was much broader than a name attached to an algorithm. He began in journalism, wrote a doctorate in topology, became an economist with a powerful interest in public policy, helped build professional mathematical statistics in the United States, and assembled research communities whose influence spread across the country. His own questions crossed boundaries that university departments tended to keep separate.

To understand his work, begin with a change in direction that occurred well before his famous papers.

## From Minnesota and Seattle to mathematics

Harold Hotelling was born on September twenty-ninth, eighteen ninety-five, in Fulda, Minnesota. His father worked in the hay business. This was a business connected to the transportation economy of its time: horses consumed hay, and horses still performed much of the moving of people and goods. As motor vehicles grew more important, the older trade was vulnerable. When Harold was a boy, his family moved to Seattle. The move placed him in a city offering more educational opportunities, but the family also faced financial difficulties.

Hotelling attended the University of Washington. His intended profession was journalism, and he worked on newspapers while studying. He read widely and had strong interests in mathematics, science, and economics. Military service interrupted his education during the First World War. After his discharge, he completed a bachelor's degree in journalism in nineteen nineteen. That degree was real preparation for the profession he had chosen, yet he soon discovered that a working life in journalism did not satisfy him.

An important intervention came from Eric Temple Bell, a mathematician who had taught him at Washington and recognized his ability. Bell urged him to return to mathematics. Hotelling did so, earning a master's degree in nineteen twenty-one. The decision was consequential: he had entered higher education as a prospective journalist and now looked toward mathematics as the foundation for research that might range far beyond mathematics itself.

Hotelling wanted to apply quantitative thought to economic and social problems. An attempt to enter graduate study in economics at Columbia did not succeed. He instead entered Princeton for doctoral work in mathematics under Oswald Veblen. His dissertation, completed in nineteen twenty-four, concerned topology and the geometry of states of motion. Topology asks what remains unchanged under continuous deformation. It is far removed from a modern spreadsheet, but its training in transformations and geometric structure proved useful to someone who would later ask how a statistical result changes when the coordinates used to describe data change.

Hotelling's next appointment took him to the Food Research Institute at Stanford. Agricultural production, food prices, and economic policy offered exactly the kind of substantive problems that attracted him. He also taught mathematics and statistical inference. By nineteen twenty-seven he was an associate professor in Stanford's mathematics department. His early research already ranged across mathematical economics, probability, and statistical distributions.

The connection between his doctoral training and his later work was more than a pleasing biographical coincidence. In nineteen twenty-seven he published a paper called An Application of Analysis Situs to Statistics. Analysis situs was an older name for topology. The paper came from a period in which methods from geometry, topology, and probability were still crossing into one another, and Hotelling saw no contradiction in being a topologist one year and a statistician the next. It is worth remembering that the later divisions between mathematical statistics, numerical linear algebra, and mathematical economics were not fixed walls for someone whose career was taking shape during the nineteen twenties.

The movement across subjects was deliberate. He did not treat statistics merely as arithmetic applied after a scientific question had been settled. He wanted a theory of how to draw conclusions from observations, and he found that the theory often required geometry. He was also drawn toward an emerging transformation in statistical thinking associated with Ronald Fisher.

## Learning from Fisher, and asking different questions

In the nineteen twenties Fisher was changing the way statisticians thought about sampling distributions, likelihood, experimental design, and significance tests. Much of that work was initially better known in Britain than in the United States. Hotelling reviewed Fisher's book, Statistical Methods for Research Workers, in nineteen twenty-seven and advocated its ideas to American readers. In nineteen twenty-nine he spent several months at the Rothamsted agricultural research station in England, working in Fisher's intellectual environment and building relationships with British statisticians.

Consider the distinction that mattered to both men. Suppose a set of observations has an average of ten. We can report ten as a description of the sample. But a statistician usually wants to say something about the unknown population that produced the observations. If the sample were collected again, its average would change. The distribution of that change determines whether a proposed population value is plausible. The mathematical problem includes the sampling process, not simply the calculation of an average.

Now let every observation be a vector. Instead of one test score, there might be a reading score and a mathematics score, or several physical measurements of a patient. The population mean is a point in a multidimensional space. We do not merely need an interval on a number line. We need a region of plausible mean vectors. And if the coordinates are correlated, the region is not generally a circle or sphere. It is stretched and tilted by the covariance matrix.

This was the setting of Hotelling's nineteen thirty-one paper, The Generalization of Student's Ratio. Student's t statistic concerns the distance between a sample mean and a hypothesized mean, measured in units of estimated standard error. Hotelling sought the corresponding construction when a single observation supplies several correlated numbers.

Here is the two-dimensional picture. Suppose a sample has an average reading score one point above a proposed population mean and an average arithmetic score one point above it. The displacement is the vector one, one. Is that a large departure? We cannot decide from the two differences alone. If each coordinate fluctuates greatly, the departure may be ordinary. If the differences point along a direction of very low variability, the same displacement may be much more telling.

The covariance matrix tells us which directions fluctuate. Its inverse allows the statistician to measure a displacement in a geometry that adjusts for those fluctuations. Hotelling's T squared statistic is the sample size multiplied by the mean displacement, transposed, times the inverse sample covariance, times the mean displacement. It is a squared distance, but the units are set by the estimated covariance rather than by the raw coordinate axes.

For a concrete calculation, suppose the sample covariance has variance four in the first variable, variance one in the second, and covariance one. Take ten observations, and suppose the displacement of the sample mean is one in each coordinate. The inverse covariance gives a squared standardized distance of exactly one. Multiplying by the sample size gives T squared equal to ten. The companion shows the small matrix calculation explicitly. The important point is what the calculation respects: changing the units, or applying any invertible linear transformation to all measurements, does not change T squared if the covariance and mean are transformed consistently.

There is a useful way to see why a covariance-adjusted distance is needed. Imagine two proposed population means separated by the same ordinary distance from the observed average. One difference lies along a high-variance diagonal in the cloud of measurements. The other lies across a narrow dimension of that cloud. A circle centered on the sample mean treats the two proposals alike. A covariance ellipsoid treats the second as less plausible, because a deviation in the narrow direction is harder to explain by ordinary sampling fluctuation. Rotating the coordinate axes does not change that judgment. This is geometric reasoning applied to inferential evidence, rather than geometry used only for drawing a picture.

Before Hotelling, there were already ways of combining measurements and of testing one variable at a time. His contribution was to produce a joint statistic with a tractable sampling distribution and an invariance property. It also changed the interpretation of a confidence region. We are not claiming that the unknown mean is randomly jumping around inside the ellipsoid. Under the repeated-sampling interpretation, the construction of the region has a prescribed long-run coverage when the statistical assumptions hold. Different samples produce different ellipsoids. The unknown population mean is fixed. This distinction is easy to lose when looking at one fitted diagram, yet it is central to the logic of statistical inference.

There is also a probability theorem. Under independent sampling from a nonsingular multivariate normal population, with the appropriate sample covariance and more observations than coordinates, a particular rescaling of T squared has an F distribution under the null hypothesis. That makes the quantity a test statistic with calibrated sampling uncertainty. In one dimension it reduces to the square of Student's t statistic.

One coordinate, one interval; several correlated coordinates, an ellipsoidal confidence region. The passage from a line to a geometric region was a profound extension of an everyday statistical question. It also explains why a list of separate single-variable tests is not equivalent to a properly constructed joint test. Correlation changes the shape of the problem.

## Economics before and alongside statistics

While Hotelling was doing this statistical work, he was also writing economic papers that became major reference points in their own fields. His nineteen twenty-five work on depreciation asked how the economic value of an asset changes as its expected future returns change. In nineteen twenty-nine he published Stability in Competition, examining how the physical location of sellers affects the choices of buyers. In nineteen thirty-one he published The Economics of Exhaustible Resources, asking how the scarcity of a finite resource ought to affect its price over time.

These subjects may seem remote from eigenvectors, but they reveal a common habit: replace a vague question with a model whose assumptions and objective can be written precisely. A model then produces consequences that can be tested against its assumptions.

Consider two stores along a straight street. Customers live along the street and prefer a shorter walk, all else equal. If the stores charge the same fixed price and customers are spread evenly, where will the stores choose to locate? A seller near an end risks leaving most customers closer to the competitor. For two sellers who choose locations while prices are fixed, putting both at the midpoint is a Nash equilibrium in this simple location game. Any small move away from the midpoint gives the moving seller less than half the customers. It is an elementary form of the pull toward the center associated with Hotelling's name.

But the assumptions are doing real work. If sellers also choose prices, a change in location changes price competition. Hotelling's original analysis of the combined location-and-price problem contained an error: local optimization conditions did not establish the proposed equilibrium. Later economists, notably d'Aspremont, Gabszewicz, and Thisse in nineteen seventy-nine, demonstrated the problem under the relevant linear transport-cost setting. The simple fixed-price example remains instructive, but it should not be presented as a proof of the stronger, flawed claim. A good mathematical model is precise enough for later researchers to discover exactly where it fails.

Hotelling's resource model offers another small calculation. Suppose owning one unit of an exhaustible resource gives you the option to sell it now or next year. Suppose the current net return, after extraction cost, is one hundred dollars, and suppose the interest rate is five percent. If you can sell today and invest, you have one hundred and five dollars next year. To make postponement equally attractive, the expected net return from selling the resource next year would also need to be one hundred and five dollars. In the idealized competitive, no-risk setting, the net scarcity rent must rise at the rate of interest. This is the core of Hotelling's rule.

Of course, actual resource markets also have uncertain discoveries, changing extraction costs, technological substitutions, regulations, and environmental damage. The simple rule isolates one intertemporal tradeoff; it does not exhaust the economics of resource management. Hotelling knew mathematics could clarify public choices, but the meaning of a model depends on what it has included.

He later wrote about public utility pricing, welfare, and the economic value of public recreation. In a nineteen forty-seven letter concerning national parks, he proposed using the costs people incur traveling to a park as evidence of the value they receive from visiting it. That insight helped establish the travel-cost approach to valuing recreation. His economics was not a brief detour before his statistical career. It was another persistent line of inquiry about what mathematics can say when observations, choices, and public consequences meet.

## Columbia, difficult years, and a research community

In nineteen thirty-one Hotelling moved to Columbia University as a professor in the economics department. He came to teach mathematical economics, but his strongest institutional ambition was to build modern mathematical statistics. A statistician, in the sense we now take for granted, did not always have a department or a recognized professional home in an American university. Methods courses were dispersed among fields, and the people assigned to teach statistics were not necessarily trained to develop it.

Hotelling assembled research associates and graduate students, secured outside support, and offered a coherent program of advanced courses. Among the people associated with the Columbia group were Abraham Wald, Samuel Wilks, Jacob Wolfowitz, W. Allen Wallis, and others who later helped develop statistical research and teaching elsewhere. His house in Mountain Lakes, New Jersey, became a gathering place for students and colleagues. Those who knew him remembered generosity with ideas and practical help for scholars displaced by European persecution.

His personal life also changed sharply during these years. His first wife, Floy Tracy, died in nineteen thirty-two, leaving two young children. He later married Susanna Porter Edmonson in nineteen thirty-four. His life at Columbia combined family responsibilities, the intellectual work of creating a discipline, and the rapid growth of statistical research during a time of economic depression and then global war.

His nineteen thirty-three work on principal components belongs to these years. It appeared in the Journal of Educational Psychology, in two installments, and its examples included test scores and other collections of related measurements. At the time, psychologists were debating whether a small number of latent factors could account for many observed abilities. Hotelling was careful about the mathematical freedom involved in rotating candidate factors. He wanted a reproducible way of choosing axes, rather than treating one arbitrary rotation as physically or psychologically distinguished.

The simplest statistical problem is this: if our measurements vary together, what direction captures the greatest variation? Start with a centered random vector X, meaning that we have subtracted the mean from each variable. The covariance matrix summarizes how the coordinates vary together. Choose a direction represented by a unit vector. Project each observation onto that direction by taking its dot product with the unit vector. The variance of that projected score is a quadratic form involving the covariance matrix.

The problem of finding the first principal component is to maximize that variance over all unit vectors. Linear algebra supplies the answer: use an eigenvector of the covariance matrix associated with the largest eigenvalue. The eigenvalue is the variance obtained along that direction. The result follows from the Rayleigh quotient. But it helps to calculate one by hand.

Suppose our covariance matrix has first diagonal entry five, second diagonal entry two, and both off-diagonal entries equal to two. Its eigenvalues are six and one. The direction of greatest variation points along two steps in the first coordinate for every one step in the second. After normalization, its components are two over the square root of five and one over the square root of five. The variance along that direction is six. The perpendicular direction has variance one. So the leading component captures six sevenths of the total variance.

Notice exactly what has happened. We began with two observable coordinates. We found two new perpendicular directions. Their scores are uncorrelated because the covariance matrix becomes diagonal in the eigenvector basis. One direction carries much more variation than the other. If we keep only the first component, we retain most of the spread, but we have thrown away a direction that still has some real variance. Whether that loss is acceptable depends on the scientific question.

## What a principal component does, and does not, say

Now suppose that we do not stop after one component. We choose a second direction perpendicular to the first and ask it to capture as much of the remaining variance as possible. Then a third, perpendicular to both earlier choices, and so on. The resulting directions form an orthonormal eigenbasis when the covariance matrix is symmetric, as every real covariance matrix is. Their variances are the ordered eigenvalues. Adding those eigenvalues gives the total variance of the original coordinates. There is no unexplained increase or disappearance of variance: we have redistributed it among new axes.

An analyst who keeps the first two components is asking about a plane. An analyst who keeps the first five is asking about a five-dimensional subspace. In each case the mathematical object is the span of several directions, not merely a printed list of eigenvector entries. If some selected eigenvalues are equal, different orthonormal bases can describe the same optimal subspace. This freedom is relevant whenever a scientist tries to assign a separate verbal meaning to each axis. The statistical procedure may determine a plane reliably while leaving the individual axes within that plane open to rotation.

Hotelling's formulation connects a geometric operation to a statistical one. There are earlier geometric precursors, including Pearson's nineteen hundred and one work on fitting lines and planes by minimizing perpendicular distances, and other nineteenth-century treatments of orthogonal fitting. For centered data, maximizing the variance of the projected points is equivalent to minimizing their mean squared perpendicular reconstruction error. Thus the nearest-subspace problem and the variance-maximization problem lead to the same principal directions under the relevant Euclidean conventions.

What changed with Hotelling was the context. He investigated components as variables defined across a population; discussed how to construct and estimate them; considered the effects of measurement reliability and sampling error; and tied the calculation to questions being asked by psychologists and other scientists. His paper also studied iterative calculation. In nineteen thirty-three, solving a large eigenvalue problem was not a routine computer command. A practical procedure that repeatedly multiplies by a matrix, increasing the relative influence of its largest eigenvalue, had immediate value.

There is an important logical distinction here. Principal components are uncorrelated linear combinations of variables. Uncorrelated does not necessarily mean independent. Independence follows in the multivariate normal model, because normal distributions have the special property that zero covariance between jointly normal components implies independence. In more general distributions, components can have zero correlation and still be linked by a nonlinear relationship. For example, if a symmetric random variable takes values distributed around zero, then the variable and its square may have zero covariance, even though knowing the first determines the second exactly.

There is another distinction. Large variance does not imply scientific significance. The variable with the largest numerical scale can dominate a raw covariance matrix. Measuring height in centimeters instead of meters multiplies its numerical variance by ten thousand. Standardizing every coordinate and analyzing the correlation matrix answers a different, equally legitimate question. Both methods have uses; the analyst must decide which differences should count as large. Hotelling's original paper frequently worked with standardized variables, especially in its psychological applications.

One final complication concerns interpretation. It is tempting to name the leading component as though it were a discovered hidden cause. But the component is defined by a mathematical optimization. Its eigenvector depends on the selected variables, their scaling, and the population from which they came. A strong first component may summarize several causes, or a common measurement artifact, or a shared background factor. It can be a valuable descriptive tool without being a proof that one latent psychological or physical mechanism has been found.

These cautions were important to the factor-analysis controversies of the era. A mathematical decomposition can be exact while the story attached to it remains conjectural. A careful statistician has to know which conclusion came from the calculation and which came from assumptions about the world.

## Two groups of measurements: the canonical correlation question

Principal components work with one set of measurements. But what if the measurements naturally come in two groups? For example, one group might contain several tests of academic preparation, while another contains several measures of later performance. We could calculate every pairwise correlation, making a large table. Yet the strongest relationship might occur between combinations of variables, even when no single pair stands out by itself.

Hotelling turned this problem into his nineteen thirty-six paper, Relations Between Two Sets of Variates, published in Biometrika. The question is to choose one linear combination of the first group and one linear combination of the second so that their correlation is as large as possible. The coefficients are chosen separately for each group. After finding the strongest pair, we can seek further pairs, with suitable orthogonality or uncorrelatedness conditions within their groups.

Here is a small example. Imagine two standardized measures on each side. Within the first group the two measures are uncorrelated and have unit variance; the same is true within the second group. Suppose that the correlation between the first coordinate of one group and the first of the other is point six. The corresponding second-coordinate correlation is also point six. The cross-correlations between opposite coordinates are point two. Thus each individual pair looks at most moderately correlated.

Now form, in each group, the normalized sum of the two coordinates. This combination has variance one because of our within-group assumptions. Its correlation with the matching normalized sum in the other group is point eight. The combinations have reinforced a shared direction. Form instead the normalized difference in each group, and their correlation is point four. In this example the canonical correlations are point eight and point four. The companion gives the two-by-two cross-correlation matrix and the singular-value calculation.

This is a different question from principal components. PCA wants a direction of large variance within one data set. Canonical correlation wants a pair of directions that have a large association across two data sets. An extremely variable direction may have no association with the other group. Conversely, a relatively quiet direction may predict something on the other side remarkably well. The correct optimization depends on what the scientist is trying to learn.

The modern construction is elegant. Let the two within-group covariance matrices be positive definite. We first rescale, or whiten, each group so that every direction within a group has unit variance and mutually perpendicular directions are uncorrelated. Then look at the cross-covariance between the whitened groups. Its singular values are the canonical correlations. The corresponding left and right singular vectors provide the coefficients in whitened coordinates. Translating them back gives the combinations of the original measured variables.

Why singular values? Because we are optimizing a bilinear expression in two separately normalized vectors. The largest singular value is the maximum achievable value of that expression. The next singular value is the corresponding optimum after enforcing the appropriate perpendicularity constraints. It is the same linear-algebra pattern that appears when one asks about principal angles between subspaces.

To understand the normalization step, imagine one group contains two measurements with very different units. If we simply maximize an unnormalized covariance between linear combinations, we can multiply one coefficient by a thousand and make the covariance arbitrarily large. That maximization has no answer. Correlation fixes the scale by dividing by the standard deviations. Whitening carries out that normalization for every direction at once. It turns the within-group covariance metric into an ordinary Euclidean metric. Only after this adjustment does a singular-value problem express the original correlation question.

Even then the two sides play different roles. The chosen weights on the first group define a score that is optimized for its relation to the other group, and the chosen weights on the second define its partner. They need not match. In a biological study, a combination of environmental measures could be related to a quite different combination of outcomes. The left and right singular vectors represent those different combinations. Treating the problem as one ordinary eigenvector calculation on the concatenated variables can obscure the separate choice being made on each side.

There is a precise geometric interpretation. Regard centered measurement columns across n subjects as vectors in an n-dimensional observation space. After choosing orthonormal bases for the column spaces of the two measurement groups, form the matrix of inner products between those bases. Its singular values are cosines of the principal angles between the subspaces. They are also the sample canonical correlations, when the sample within-group covariance matrices are nonsingular. Thus canonical correlation can be viewed as a statistical use of subspace geometry.

## When the geometry becomes too accommodating

The canonical-correlation construction also reveals an instructive failure case. Suppose we have only five subjects, but measure three variables in each of two groups. Center each column by subtracting its sample mean. Every centered column now lies in a space of dimension at most four, since the five entries must sum to zero. If the three columns in each group are linearly independent, each group spans a three-dimensional subspace inside that four-dimensional centered observation space.

Two three-dimensional subspaces inside a four-dimensional space must intersect in at least two dimensions. That conclusion comes from the dimension formula: three plus three exceeds four by two. Along those common directions the principal angle is zero, so its cosine is one. Therefore at least two sample canonical correlations are exactly one, even when the two groups arose from independent random quantities and there is no genuine population association. The data are simply too small relative to the number of variables.

The dimension argument does not rely on a contrived choice of observations. For almost any full-rank sample with these dimensions, the forced intersections occur. There is no need to manufacture matching columns or secretly copy a measurement from one group to the other. The problem is simply that centering five observations leaves only four independent directions in sample space, while each group is trying to fit a three-dimensional subspace. As soon as we insist that those large subspaces occupy the same small ambient space, overlap becomes inevitable.

This is a severe form of overfitting. The sample calculation can be mathematically perfect and scientifically misleading. It optimizes over enough coefficients to match much of the sample by construction. A correlation of one normally sounds decisive. Here the geometry forces it, regardless of the substantive relation we hoped to investigate.

Adding more measurements without adding more subjects may make this problem worse. The remedy is not to abandon the linear algebra. It is to restore the statistical question: what sampling process generated these measurements, how many parameters are we choosing, and what out-of-sample relationship can we expect? Modern techniques may regularize the covariance matrices, reduce dimension, or evaluate predictive performance on held-out data. Those are later developments, but the failure mode is visible directly in Hotelling's original question.

One can see a similar issue with principal components. A sample always has leading eigenvectors. They may look crisp, and the software may display many decimals. The population directions they supposedly estimate can nonetheless be poorly determined. A calculation can be exact for the observed matrix while uncertain as an estimate of an unknown matrix. Understanding that distinction leads toward another part of Hotelling's intellectual legacy.

## A population direction and an estimated direction

Return to a two-dimensional population whose covariance matrix is diagonal. Suppose the first variance is four and the second is one. The principal direction points along the first coordinate, and the eigenvalue gap is three. Now imagine that finite-sample error introduces an off-diagonal covariance of point four, leaving the two variances unchanged. The estimated leading eigenvector rotates, but only by about seven and a half degrees. The strong gap helps stabilize the direction.

Change the population so its two variances are two and one point nine. The eigengap is now only point one. Apply the same off-diagonal error of point four. The estimated leading eigenvector rotates by more than forty-one degrees. The error matrix is no larger than before; what changed is how much spectral separation the population supplied. If the two population eigenvalues were exactly equal, there would be no distinguished leading direction at all: every unit vector in their two-dimensional eigenspace would maximize variance.

This illustrates the modern perturbation principle behind Davis-Kahan-type results. An isolated spectral subspace can be stable when the perturbation is small relative to a suitable gap. A tiny or absent gap makes individual directions unstable. For a matrix with several close leading eigenvalues, the span of the leading eigenvectors may still be much more stable than any particular basis chosen within that span, provided the cluster is separated from the rest of the spectrum.

The sample covariance is a random estimate. Thus statistical uncertainty has two components. We need to understand the random size of the estimation error, and we need to understand how that matrix error affects the spectral object we are interested in. Probability bounds the error; perturbation theory converts the error into an angle. This combination has become standard in analyses of principal component estimation, canonical correlation, factor models, and other multivariate procedures.

Hotelling did not prove the later Davis-Kahan theorem; he died before it appeared. Nor should one read today's full theory of random matrices back into his nineteen thirty-three paper. But he explicitly treated sampling errors as a concern in constructing components. His statistical formulation made a question unavoidable: if an eigenvector is calculated from data, how confident are we that the direction is a feature of the population? It is a question that has continued to generate mathematics long after the original publications.

## Statistics in a world at war

Hotelling's work was never confined to the theory of components and correlation. In nineteen thirty-six, with Margaret Richards Pabst, he published research on rank correlation and significance testing without a normality assumption. Rank methods replace actual measurements with their order. They can retain information about association while reducing dependence on the numerical scales and some distributional assumptions. This was an early contribution to the development of nonparametric statistics.

During the Second World War Hotelling helped create and direct the Statistical Research Group at Columbia. Statistical inference had become directly relevant to industrial production, inspection, quality control, and military logistics. The group brought together researchers who would be influential after the war, including Wald, Wallis, and Wolfowitz. The problems were practical and pressing, yet their solutions helped refine ideas that would later be used in civilian applications.

The difference between a test derived for a normal distribution and a rank-based procedure points to a broad lesson. Every statistical theorem has a domain of validity. In the first, a normal model supplies a particular sampling distribution. In the second, replacing measurements by ranks can remove sensitivity to changes of numerical scale: taking logarithms of every positive measurement, for example, preserves the order and hence its ranks. Such transformations may profoundly alter the ordinary covariance matrix. A scientist choosing between the procedures is making a choice about what features of the measurements should count as evidence.

Hotelling also worried about who taught statistics. In nineteen forty he published The Teaching of Statistics. He observed that universities were allowing statistical courses to emerge in numerous departments without building a sufficient supply of teachers who knew the subject deeply. The resulting courses could be useful, but the fragmentation also made it difficult to develop a coherent discipline and to provide sound methodological advice across fields.

He also encouraged collaborations rather than assuming every field could be understood by one all-purpose technique. The agricultural scientist estimating crop variation, the economist modeling prices, and the psychologist analyzing test batteries all faced numerical uncertainty, but they did not face identical scientific questions. Building a statistical profession meant giving those researchers partners who could adapt inference to the design of the experiment and the structure of the observations. It was an institutional counterpart to his mathematical habit of specifying a criterion before maximizing anything.

His solution was to treat statistics as a professional intellectual field, with trained statisticians, a curriculum, research programs, and a place from which to collaborate with scientists in other disciplines. This was not only an argument about university organization. It was a claim about the reliability of scientific inference. A laboratory can buy a new measuring instrument. It also needs someone who understands what its measurements permit it to conclude.

Columbia did not create the independent department Hotelling wanted, despite the success of his courses and research group. In nineteen forty-six he accepted an invitation to the University of North Carolina at Chapel Hill, where he could help establish a Department of Mathematical Statistics. He moved at a point when many of the researchers he had trained were beginning to shape the postwar statistical profession. Chapel Hill became a major center of research in probability and mathematical statistics.

Hotelling's recruitment of colleagues mattered as much as his own later publication count. The community included scholars such as Raj Chandra Bose, Wassily Hoeffding, P. L. Hsu, Herbert Robbins, and S. N. Roy. Through teaching, collaboration, and graduate training, the ideas of mathematical statistics entered universities that had previously treated the subject as a collection of local techniques.

## A long view of inference and public life

The work that made Hotelling famous also displayed a tension. Statistics is an instrument for extracting structure from data, and mathematical models can make social questions more precise. But extracting a pattern does not by itself settle its cause, value, or policy implications. A principal component describes a direction of variation. A canonical correlation describes an optimized association. A T squared test assesses a hypothesized population mean under a specified sampling model. None of these automatically supplies a scientific explanation of the observations, and none replaces the need to examine how the observations were obtained.

The same care applies to the economic work. A rule about resource rents depends on assumptions about markets and future opportunities. A predicted clustering of stores depends on how competition and transportation costs have been modeled. The history of Hotelling's location theory is particularly instructive because later researchers were able to preserve a productive idea while exposing a serious error in an argument. The intellectual value of the question survived the revision of the proposed answer.

Those who worked with Hotelling emphasized another quality: he was willing to help people build careers and institutions, not simply defend an individual line of research. His support for displaced European scholars and his encouragement of students from backgrounds too often excluded from academic opportunity belonged to the same professional life as his statistical work. He retired from Chapel Hill in nineteen sixty-six and died there on December twenty-six, nineteen seventy-three.

There is a temptation, when looking back at a figure with many contributions, to identify one moment as the decisive breakthrough. In Hotelling's case there is no single moment that captures the whole portrait. The nineteen thirty-one T squared paper provided a geometric generalization of hypothesis testing. The nineteen thirty-three principal-components paper translated an older geometrical problem into the language of population variation. The nineteen thirty-six canonical-correlation paper asked how two groups of measurements can align. His economics developed mathematical methods for competition, resource scarcity, and welfare. His teaching and institutional work made it possible for others to study those questions systematically.

One thread does run through them. Measurements and decisions live in spaces with several directions. The right direction depends on the question: greatest variation, strongest association, largest evidence against a proposed mean, highest expected economic return. Once we choose that criterion, mathematics can identify an optimum. Then statistics asks whether the optimum can be trusted beyond the data in hand. And history asks what the problem, and the answer, meant to the people working on it.

In that combination of geometry, inference, and attention to real problems lies the enduring contribution of Harold Hotelling.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. Hotelling's T-squared statistic and its distribution

Let independent observations \(X_i\in\mathbb R^p\), \(i=1,\ldots,n\), have sample mean \(\bar X\) and unbiased sample covariance
\[
S=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)(X_i-\bar X)^T.
\]
For a hypothesis \(H_0:\mu=\mu_0\), let \(d=\bar X-\mu_0\), and suppose \(S\) is positive definite. Then
\[
T^2=n\,d^TS^{-1}d.
\]
If \(X_i\stackrel{\text{iid}}\sim N_p(\mu_0,\Sigma)\) with \(\Sigma\succ0\) and \(n>p\), under \(H_0\),
\[
\frac{n-p}{p(n-1)}T^2\sim F_{p,n-p}.
\]
For \(p=1\), \(T^2=t_{n-1}^2\sim F_{1,n-1}\). For any invertible \(B\), transforming data by \(X'_i=BX_i\) gives \(d'=Bd\), \(S'=BSB^T\), and \(T'^2=T^2\).

Running example: \(n=10\), \(S=\begin{bmatrix}4&1\\1&1\end{bmatrix}\), \(d=(1,1)^T\).
\[
S^{-1}=\tfrac13\begin{bmatrix}1&-1\\-1&4\end{bmatrix},\quad
S^{-1}d=(0,1)^T,\quad d^TS^{-1}d=1,\quad T^2=10.
\]
The matrix is positive definite (determinant \(3\)); the example illustrates a covariance-adjusted distance, not a particular decision threshold.

### 2. Population PCA and reconstruction error

For centered \(X\) with \(\Sigma=\operatorname{Cov}(X)\succeq0\), the variance of \(u^TX\) for \(\lVert u\rVert_2=1\) is \(u^T\Sigma u\). The Rayleigh maximum equals \(\lambda_1(\Sigma)\). For an orthonormal \(p\times k\) matrix \(U\),
\[
\mathbb E\lVert X-UU^TX\rVert_2^2
 =\operatorname{tr}\Sigma-\operatorname{tr}(U^T\Sigma U).
\]
Thus the leading \(k\) eigenspace minimizes expected squared orthogonal reconstruction error; its minimum error is \(\sum_{j>k}\lambda_j\). If there are eigenvalue ties across the cutoff, the optimizing subspace need not be unique.

Example:
\[
\Sigma=\begin{bmatrix}5&2\\2&2\end{bmatrix},\quad
(\lambda_1,\lambda_2)=(6,1),\quad
u_1=\frac1{\sqrt5}(2,1)^T,\quad
u_2=\frac1{\sqrt5}(-1,2)^T.
\]
The first principal component explains \(6/7\) of total population variance \(\operatorname{tr}\Sigma=7\).

### 3. Correlation versus independence and scaling

Uncorrelated transformed scores \(\nu_i^TX\) have diagonal covariance in an eigenbasis. Independence requires further assumptions: it follows for jointly Gaussian coordinates, but generally fails. If \(Z\) has a symmetric nondegenerate distribution with finite third moment, then \(\operatorname{Cov}(Z,Z^2)=0\) while \(Z^2\) depends entirely on \(Z\). Replacing variable \(X_j\) by \(cX_j\) changes covariance variances by \(c^2\). Standardizing each coordinate first produces correlation-based PCA, a distinct optimization problem.

### 4. Canonical correlation and whitening

Partition \(Z=(X^T,Y^T)^T\), with positive definite \(\Sigma_{XX}\) and \(\Sigma_{YY}\), and cross-covariance \(\Sigma_{XY}\). Optimize
\[
\rho_1=\max_{a,b}\frac{a^T\Sigma_{XY}b}
{\sqrt{a^T\Sigma_{XX}a}\sqrt{b^T\Sigma_{YY}b}}.
\]
Whiten the two groups with \(u=\Sigma_{XX}^{1/2}a\), \(v=\Sigma_{YY}^{1/2}b\). Then the problem is maximizing \(u^TCv\) for unit vectors, where
\[
C=\Sigma_{XX}^{-1/2}\Sigma_{XY}\Sigma_{YY}^{-1/2}.
\]
The singular values of \(C\) are the canonical correlations, in \([0,1]\). The associated singular vectors yield optimal linear combinations. With identity within-group covariance and
\[
C=\begin{bmatrix}0.6&0.2\\0.2&0.6\end{bmatrix},
\]
the canonical correlations are \(0.8\) and \(0.4\) with normalized sum and difference directions \((1,1)/\sqrt2\), \((1,-1)/\sqrt2\). The full block covariance \(\begin{bmatrix}I&C\\C^T&I\end{bmatrix}\) is positive definite because \(\lVert C\rVert_2=0.8<1\).

### 5. Principal-angle interpretation and sample-overfitting counterexample

For a centered sample with \(n\) observations, two column spans \(\mathcal U,\mathcal V\subset\mathbf1^\perp\subset\mathbb R^n\) have orthonormal basis matrices \(U,V\). The sample canonical correlations are the singular values of \(U^TV\), provided the within-group sample covariances have full rank. These equal \(\cos\theta_j\), the cosines of principal angles. If \(n=5\) and each group has \(p=q=3\) linearly independent centered columns, both spans are 3-dimensional inside the 4-dimensional centered space. Therefore
\[
\dim(\mathcal U\cap\mathcal V)\ge p+q-(n-1)=2.
\]
At least two principal angles are zero and at least two sample canonical correlations equal 1, regardless of population independence. This is a deterministic finite-sample rank effect.

### 6. Eigenvector rotation under estimation error

For \(\Sigma=\operatorname{diag}(\lambda_1,\lambda_2)\) with \(\lambda_1>\lambda_2\), consider
\[
\widehat\Sigma=\begin{bmatrix}\lambda_1&\varepsilon\\\varepsilon&\lambda_2\end{bmatrix},\quad
\tan(2\theta)=\frac{2\varepsilon}{\lambda_1-\lambda_2},\quad 0\le\theta<\pi/4
\]
for \(\varepsilon>0\), where \(\theta\) measures rotation of the leading eigenvector. At \(\varepsilon=0.4\), for \((\lambda_1,\lambda_2)=(4,1)\), \(\theta\approx7.466^\circ\). For \((2,1.9)\), \(\theta\approx41.437^\circ\). The perturbation operator norm equals \(0.4\) in both examples. For \(\lambda_1=\lambda_2\), the population leading direction is unidentified. Davis-Kahan-type sin-theta estimates were developed later; this example is a modern explanation of why sample PCA requires both concentration and a spectral gap.

### 7. Resource scarcity and spatial competition models

For fixed extraction cost \(c\), discount rate \(r\), and a competitive frictionless perfect-foresight model, the net scarcity rent \(q(t)=p(t)-c\) for a marginal in-ground unit follows \(q(t)=q(0)e^{rt}\) when the owner is indifferent across extraction dates. Two-period discretization: with \(q_0=100\) and \(r=0.05\), \(q_1=105\). This conditional result should not be read as a universal oil-price forecast.

In a fixed-price nearest-seller location game on \([0,1]\) with uniform demand and two sellers choosing locations, both at \(1/2\) form a pure-strategy equilibrium if tied demand divides evenly. This simple game does **not** validate Hotelling's original two-stage price-and-location equilibrium claim under linear transportation costs, criticized in d'Aspremont, Gabszewicz and Thisse (1979).

### 8. Dated contributions and historical distinctions

- 1895: Born in Fulda, Minnesota; later family move to Seattle.
- 1919 and 1921: Journalism bachelor's and mathematics master's at the University of Washington; Bell encouraged the transition.
- 1924: Princeton Ph.D. under Oswald Veblen on topology.
- 1924–1931: Stanford Food Research Institute and mathematics; 1929 visit to Fisher at Rothamsted.
- 1925: Depreciation and early statistical-distribution work.
- 1929: Spatial competition; confidence-band work with Holbrook Working.
- 1931: *The Generalization of Student's Ratio*; Columbia appointment; economic model of exhaustible resources.
- 1933: Two-part paper on principal components in *Journal of Educational Psychology* 24, 417–441 and 498–520.
- 1936: *Relations Between Two Sets of Variates* in *Biometrika* 28, 321–377; nonparametric work with M. R. Pabst.
- 1940: *The Teaching of Statistics*.
- 1942–1945: Columbia Statistical Research Group during World War II.
- 1946: Establishes mathematical-statistics department at UNC Chapel Hill.
- 1947: Travel-cost argument in correspondence concerning national-park valuation.
- 1966: Retirement; 1973: Death in Chapel Hill.

Pearson (1901) and earlier contributors studied closest-fitting subspaces. Hotelling's 1933 paper developed a statistical principal-components treatment, including standardized measures, iteration, and sampling questions. Principal-angle geometry precedes Hotelling's 1936 canonical correlation paper; the latter supplies a statistical optimization over two sets of variates. The later Davis-Kahan perturbation framework is a subsequent analytical development, not a result proved by Hotelling.

### 9. Selected readings

- Kenneth J. Arrow and E. L. Lehmann (2005), *Harold Hotelling*, National Academy of Sciences, *Biographical Memoirs*, volume 87, pp. 220–233. https://www.nationalacademies.org/read/11522/chapter/13
- MacTutor, *Harold Hotelling*. https://mathshistory.st-andrews.ac.uk/Biographies/Hotelling/
- Harold Hotelling (1931), *The Generalization of Student's Ratio*, *Annals of Mathematical Statistics* 2, 360–378.
- Harold Hotelling (1933), *Analysis of a Complex of Statistical Variables Into Principal Components*, *Journal of Educational Psychology* 24(6), 417–441, DOI: 10.1037/h0071325; and 24(7), 498–520, DOI: 10.1037/h0070888.
- Harold Hotelling (1936), *Relations Between Two Sets of Variates*, *Biometrika* 28, 321–377, DOI: 10.1093/biomet/28.3-4.321.
- Harold Hotelling (1940), *The Teaching of Statistics*, *Annals of Mathematical Statistics* 11, 457–470, DOI: 10.1214/aoms/1177731833.
- P. d'Aspremont, J.-J. Gabszewicz and J.-F. Thisse (1979), *On Hotelling's Stability in Competition*, *Econometrica* 47(5), 1145–1150.
- Marion Gaspard, Antoine Missemer and Thomas Michael Mueller (2024), *A Journey into Harold Hotelling's Economics*, *Journal of Economic Literature* 62(3), 1186–1212, DOI: 10.1257/jel.20231700.

Editorial source discrepancy: the NAS memoir summarizes Floy Tracy's death as occurring in 1934, but MacTutor provides October 1932; the spoken lecture uses 1932, matching the specific MacTutor chronology. Both references are supplied for review.
