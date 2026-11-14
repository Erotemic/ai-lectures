# 024000 — Karl Pearson: Why is a principal component an optimization problem?

**Track:** History · People and ideas. **Theme:** Karl Pearson's life, the rise of biometry and mathematical statistics, geometric closest-fit subspaces, statistical limits and the institutional history of eugenics. **Background:** vectors, orthogonality, elementary eigenvalues and averages. The examples introduce covariance and principal components locally.

<!-- BEGIN SPOKEN LECTURE -->

# Karl Pearson: Why is a principal component an optimization problem?

A naturalist has assembled a table of measurements. Each specimen has a recorded length, width, perhaps a weight, and perhaps a dozen other quantities. The table is too large to picture directly. Some measurements rise together. Others behave almost independently. The naturalist wants to know whether the apparent complexity conceals a simpler pattern.

There are several possible meanings of simpler. We might want a formula that predicts width from length. We might want to place the specimens along a single line while throwing away as little information as possible. Or we might want to distinguish genuine structure from accidental variations in a small sample. Those requests lead to related calculations, but they are not identical.

Karl Pearson helped transform problems of this kind into mathematical statistics. His nineteen-oh-one paper on lines and planes of closest fit supplied an influential geometric formulation of what would later be recognized as principal component analysis. In that construction, the line itself is the unknown. Its direction is chosen to minimize the total squared distance from all the observations to the line. The optimum eventually reveals itself as an eigenvector.

It is a beautiful problem. But Pearson's biography also asks a harder historical question: what happens when powerful mathematical methods are developed inside an institution that attaches them to harmful judgments about human worth? Pearson built methods that remain central to science. He also championed eugenics and helped give it an academic home. Both parts of the story belong in the account of his life.

## A mathematician whose interests would not stay in one subject

Karl Pearson was born in London on the twenty-seventh of March, eighteen fifty-seven. His father, William Pearson, was a barrister, and his mother was Fanny Smith. The family gave the boy the name Carl, with a C. As a young man he changed the spelling to Karl. Later observers connected the choice to his enthusiasm for German intellectual life and socialist ideas; the spelling is a small trace of the changing ambitions of his youth.

He attended University College School, was educated for a period by a private tutor following illness, and won a scholarship to King's College, Cambridge. Mathematics at Cambridge was then dominated by the demanding examination known as the Mathematical Tripos. In eighteen seventy-nine Pearson finished as third wrangler, meaning third in that year's mathematical ranking. That performance could have pointed toward a conventional career in mathematical physics. Instead, his interests kept escaping the syllabus.

He read philosophy and religious history, and he was fascinated by literature. After Cambridge he traveled to Heidelberg and Berlin, studying subjects ranging from physics and metaphysics to German literature and Roman law. He encountered socialist thought during the German years. He later trained in law in London and was called to the bar, though he did not establish a legal practice. He lectured for adult educational audiences about mechanics, history, religion and politics.

This was more than youthful indecision. Pearson was searching for a way to bring varied kinds of knowledge within a common conception of science. He wrote on free thought, edited mathematical works, and published essays and books outside the disciplines for which he would become famous. His eighteen ninety-two book, The Grammar of Science, tried to explain what scientific knowledge can legitimately claim: the relationships among observations, the concepts used to describe them, and the limits of explanation.

There is a productive tension already visible. Pearson was skeptical of claims that science could reveal a thing's hidden essence beyond observation. Yet he would later make strong claims about the nature and prospects of entire human populations on the strength of imperfect measurements and contentious assumptions. His statistical methods could quantify relationships; his political interpretation of those relationships often claimed more than the methods established.

## London, teaching, and a circle of collaborators

In eighteen eighty-four Pearson was appointed to the Goldsmid Chair of Applied Mathematics and Mechanics at University College London. He taught mechanics and geometry, worked on elasticity, and edited or completed demanding mathematical projects left unfinished by other authors. One was William Kingdon Clifford's Common Sense of the Exact Sciences. Another was Isaac Todhunter's history of elasticity. These were not statistical works. They demanded patience with geometry, equations, physical models and the history of ideas.

He also helped establish the Men and Women's Club in eighteen eighty-five, where participants debated relations between the sexes. There he met Maria Sharpe. They married in eighteen ninety, and later had three children, among them Egon, who would become a major statistician. Their household and friendships connect the early Pearson to debates about equality, education and social reform. It would be misleading to read his later political commitments backward as though every stage of the young man's thinking had been predetermined.

At the same time, his London environment exposed a growing demand for quantitative answers in biology. Darwin's theory had made variation a central scientific subject. If natural selection acts on differences among organisms, how should those differences be measured? If children resemble their parents, how strong is that resemblance across a large population? How can one investigate continuous characters such as height, when inheritance does not produce a small number of tidy categories?

The zoologist Walter Frank Raphael Weldon became the crucial partner in Pearson's change of direction. Weldon was appointed to a chair at University College in eighteen ninety. He brought biological measurements and questions about natural selection. Pearson brought the analytic machinery to examine them. Francis Galton's Natural Inheritance, published in eighteen eighty-nine, supplied another important stimulus. Galton had already explored regression toward the mean and correlations among human measurements.

Here is the important division of labor. A field biologist might measure a large population of crabs or mollusks and find that their dimensions vary. A mathematician can turn the table into distributions, average sizes and relationships among variables. But there is a third task: deciding what those observed relationships imply about biological mechanisms. That third task requires independent scientific assumptions and experimental evidence. The collaborators did not always keep those tasks sufficiently separate.

## How numbers became a research technology

It is easy to imagine a statistician at a modern computer, drawing a scatter plot, asking for a correlation matrix, and receiving an answer in less than a second. Pearson and his collaborators worked in a different computational world. Data had to be collected by hand, copied into tables, checked, organized into frequency classes, and subjected to lengthy arithmetic. Tables of mathematical functions were themselves scientific infrastructure. Every additional variable could multiply the labor.

This changes how we should picture his laboratory. People collecting skull measurements, recording life histories, transcribing biological observations and performing arithmetic were essential to the published results. So were the researchers who questioned whether the samples represented the populations they purported to describe. A formula published under one professor's name could depend on the work of a whole research establishment.

The huge appetite for observations partly explains why Pearson's project seemed revolutionary to contemporaries. It offered methods for comparing thousands of measurements that would otherwise remain separate anecdotes. It also increased the risk of hiding weak assumptions beneath tables of precisely calculated numbers. Measurement can be precise without its scientific interpretation being correct. A laboriously computed standard error does not make a poorly defined category coherent.

When Pearson promoted statistics as a discipline requiring trained specialists, he was responding to an authentic problem. Numerical techniques can be misused by people who do not understand their derivation. Yet expertise brings obligations beyond technical competence. Choosing meaningful variables, sharing credit and resisting unjustified extrapolations are also part of scientific practice. Those issues were already present in the methods and institutions that Pearson was building.

## From a scatter of measurements to a correlation

Consider ten plants. For each, record stem height and leaf length. Put height on a horizontal axis and leaf length on a vertical axis. If tall plants tend to have long leaves, the points tilt upward. If the sizes are unrelated, the cloud may look nearly round. A single numerical summary can help compare two datasets, but what should it measure?

Pearson developed and systematized methods for correlation and regression in a series of papers during the eighteen nineties, building on Galton and other predecessors. A correlation coefficient compares how two quantities move around their respective averages. It first measures the average product of their deviations: when both rise together, that product is positive. Then it divides by the typical scale of variation in each quantity. The result has no physical unit and lies between minus one and plus one, provided the two variables actually vary.

Take three observations of one quantity: one, two and three. Suppose the second quantity is two, four and six. Each is twice the first. Their deviations from their means line up perfectly and the correlation is plus one. But now suppose the two quantities are the number of people entering a park and the amount of ice cream sold at a nearby kiosk. Weather might make both increase. A perfect or near-perfect correlation would not show that visitors cause purchases or that buying ice cream causes park attendance. Nor does a statistical relationship establish heredity when family circumstances and shared environments may be involved.

Regression answers a different question: if one measurement is known, how should we predict another? Ordinary least squares for predicting leaf length from stem height treats the horizontal values as given and penalizes vertical differences between actual and predicted leaf lengths. Its fitted line minimizes the total of those vertical squared errors. Reverse which measurement is predicted and you generally obtain a different fitted line. The choice of response variable is part of the problem.

Pearson's research in this period made such choices explicit and calculable. His papers on evolutionary variation developed regression formulas, correlation, and ways to describe distributions that were asymmetric rather than bell-shaped. He helped popularize the name standard deviation. These were instruments for empirical scientists who wanted to move beyond the impression that two diagrams merely looked similar.

The lesson is that a good statistic is not a substitute for a good question. It is an answer to a particular, carefully defined question. This will become decisive when we ask what the best fitting line means.

## Counting discrepancies: Pearson's chi-square test

Not every biological observation is a length or a weight. Sometimes the observations are counts in categories: how many seeds fall into each class, how many births have different recorded outcomes, or how many observations occupy each range in a frequency table. If a model predicts certain category frequencies, how can the data be compared with it?

Pearson's nineteen hundred paper introduced a general chi-square goodness-of-fit criterion. Its basic idea is to compare observed counts with expected counts, squaring each discrepancy and scaling by its expected size. The scaling recognizes that a difference of five observations is striking when the expected count is one, but less striking when the expected count is ten thousand.

Imagine a coin tossed fifty times, with thirty heads and twenty tails. A model of a fair coin expects twenty-five of each. The deviations are plus five and minus five. Square five to get twenty-five, divide by twenty-five to get one for heads, and do the same for tails. The total chi-square statistic is two. This number alone is not a verdict of unfairness. Under independent tosses of a fair coin and an appropriate approximation, a statistic at least this large is not especially rare.

The statistical calibration requires attention to how many counts are free to vary. The fifty tosses fix the total, so after specifying the head count the tail count is determined. There is one independent count deviation. If parameters have been estimated from the same data, additional constraints can change the appropriate degrees of freedom. Pearson's early treatment did not fully handle this distinction. Ronald Fisher clarified important aspects of it in the nineteen twenties, and the dispute over degrees of freedom became part of the history of modern statistics.

This story reveals how statistical theory develops: a useful test can come first, followed by correction of the conditions under which it is valid. The statistic is still widely used, but it does not license arbitrary conclusions from small expected counts, dependent observations, selected categories, or a model whose assumptions were never examined.

## Two ways to draw a line through the same points

To see why the distinction between regression and closest-fit geometry is substantial, imagine a nearly vertical group of points. They have almost the same horizontal coordinate but vary greatly in their vertical positions. If we insist on predicting vertical position from horizontal position, a small horizontal measurement error can produce a very steep regression line. In the limit where all horizontal coordinates are identical, a slope-based vertical regression has no uniquely determined slope at all.

The perpendicular-distance problem behaves differently. A vertical line can be a perfectly valid best-fit geometric line. Its direction is described by an arrow pointing upward, with no need to express the line as vertical position equals a finite slope times horizontal position. The set of possible directions includes the vertical axis without any exceptional algebraic case.

Now reverse the regression problem and predict horizontal position from vertical position. That is a third objective, and it usually produces another line. One dataset has generated three legitimate optimization problems. They need not agree because they measure three different kinds of error.

The geometric formulation has its own assumptions, however. Squared perpendicular distance treats the two axes as commensurable after scaling. If horizontal and vertical measurement errors have different variances, an error-weighted distance may be scientifically more appropriate. Pearson's criterion is exactly optimal for the ordinary Euclidean loss it specifies. Identifying a physically meaningful loss function is part of applying the result.

## A line that belongs to the data, not to one coordinate

Now return to the cloud of measured points. Suppose we have observations of two traits and want to summarize them with one direction. Neither variable has been designated as the response. We want a line through the middle of the cloud that is close to the points in an ordinary geometric sense. Distance is measured perpendicular to the line. A point far above the line and a point far to its side are treated according to their shortest distances, after the chosen coordinate scales have been fixed.

This is the problem Pearson addressed in his nineteen-oh-one paper, On Lines and Planes of Closest Fit to Systems of Points in Space. The paper appeared in the Philosophical Magazine. It is an early landmark in the geometry of dimension reduction. It did not present a modern software implementation or use the later terminology of principal component analysis. It asked a recognizable geometric optimization question and found the optimal subspace using algebra.

Before we calculate the direction, locate the line. Suppose the cloud is clustered around the point with horizontal coordinate one hundred and vertical coordinate twenty. A line through the origin would describe the position of the cluster poorly, even if its direction were excellent. The best affine line can be moved to pass through the mean point. Subtracting the mean from each observation leaves a cloud centered at the origin, and now we need only select the direction.

The two operations have different jobs. Centering chooses where the line passes. Optimization chooses which way it points. Mixing them up is a common source of error in applied principal component analysis. When the data are uncentered, the leading direction of a raw matrix can point mainly toward the mean rather than describe the variation around it.

We can now describe the candidate line by a unit arrow. Project every centered data point onto that arrow. The projection is the part of the point that runs along the arrow; the remainder points at right angles to it. The squared length of that remainder is the error for that observation. The best arrow minimizes the sum of those squared remainders.

## A four-point example you can work by hand

Consider four centered observations. One point is three units right and one up. Another is three left and one down. A third is one right and one down. A fourth is one left and one up. Opposite points balance, so the average is the origin. The cloud extends much farther horizontally than vertically, but its longest direction is slightly tilted.

If we choose the horizontal axis as our line, the perpendicular errors are simply the vertical distances: one for every point. Their squares add to four. That is a reasonable fit, but a small rotation should improve it, because the long right-up point and long left-down point lean together.

We can record the squared spread of the coordinates in a two-by-two matrix. Average the squared horizontal coordinates: nine, nine, one and one, giving five. Average the squared vertical coordinates: one every time, giving one. Average the products of the coordinates: three, three, negative one, negative one, giving one. These three averages make a symmetric matrix with five and one along its diagonal and one in each off-diagonal position.

The matrix tells us how much variation lies in any direction. For a unit arrow with horizontal and vertical components, multiply by this matrix and take the arrow's dot product with the result. That number is the average squared length of the projected data. Along the horizontal axis it is five. Along the vertical axis it is one. Along the forty-five-degree diagonal it is four.

The greatest possible value is three plus the square root of five, about five point two three six. The associated direction is rotated only about thirteen degrees above horizontal. Since the total average squared length of the data is six, the average squared perpendicular error is six minus five point two three six, about zero point seven six four. For four points, the total error is about three point zero five six, better than the horizontal line's four.

We have obtained a best fitting direction from a small table of measurements. The arithmetic also exposes why simply picking the variable with the largest variance is sometimes inferior to choosing a diagonal combination. Even a fairly small positive cross-correlation tilts the best line.

## Why the maximum-variance and minimum-distance problems agree

The key mathematical step is Pythagoras. For each centered point, its projection along the chosen unit direction is at right angles to what remains. Its total squared length equals the squared projected length plus the squared remainder. Add this identity over every observation. The sum of original squared lengths does not depend on which line we choose.

Therefore, if we reduce the total squared perpendicular remainder, we must increase the total squared projected length by exactly the same amount. Finding the line closest to all the points is equivalent to finding the direction with the greatest projected squared spread. The two optimization problems have the same answers because their objectives sum to a constant.

To find that maximum, introduce the symmetric matrix of second moments of the centered data, often called the sample covariance matrix up to a choice of normalizing factor. A unit direction produces a quadratic expression using this matrix. The spectral theorem says the matrix has perpendicular eigenvectors with real, nonnegative eigenvalues. Write any unit direction as a combination of these eigenvectors. Its projected variance is an average of the eigenvalues weighted by squared coefficients. No such average can exceed the largest eigenvalue. Choosing an eigenvector for that largest eigenvalue reaches the maximum.

That argument explains the algebra without relying on a memorized rule. The eigenvector emerges because it is the direction that maximizes a constrained quadratic expression. In our example, the largest eigenvalue tells us the average squared spread retained along the best line. The smaller eigenvalue tells us the average squared error that must remain after one-dimensional compression.

If the two eigenvalues are equal, every line is equally good. The data have no preferred one-dimensional axis. If the top eigenvalue is repeated in a larger problem, there may be several equally optimal leading directions. That is an important qualification: an optimization problem can be well defined even when it has no uniquely determined answer.

## From a line to a plane, and from a matrix to singular values

Pearson's paper also considered planes. In modern language we can ask for a subspace of dimension two, or three, or any smaller number of dimensions than the original data space. For every point, keep its orthogonal projection onto the chosen subspace and discard the perpendicular remainder. Choose the subspace that makes the total squared discarded length as small as possible.

The best subspace is spanned by eigenvectors associated with the largest covariance eigenvalues. If we retain two directions, we capture the sum of the two largest amounts of variance. If we retain five, we capture the sum of the five largest. The discarded error equals the sum of the remaining eigenvalues, times the chosen normalization for the dataset.

There is a closely related computational view. Arrange the centered data in a rectangular matrix, with observations as rows and measured variables as columns. The singular value decomposition finds perpendicular coordinate systems in which this matrix stretches along independent directions. The right singular vectors of the centered data matrix are the covariance eigenvectors. Their squared singular values, after division by the sample-size normalization, are the covariance eigenvalues.

In current scientific computing, the singular value decomposition is often the preferable algorithmic route because explicitly forming a covariance matrix can amplify conditioning difficulties. This is part of a later numerical history, not a claim that Pearson used the modern SVD algorithm. His contribution was to formulate an optimal geometric fitting problem and connect it to its algebraic solution.

The dimension-reduction idea is powerful because it lets the data choose a plane rather than requiring an observer to specify a convenient pair of coordinate axes. But when a scientist says that the first two components explain ninety percent of the variance, the word variance refers to the spread measured using these particular coordinates and their scales. It does not automatically mean that ninety percent of the scientifically meaningful information has been retained.

## When the measurement scale changes the answer

Imagine that the two coordinates of the four-point example are lengths. The horizontal measurement was recorded in centimeters, while the vertical was recorded in meters. Even if the physical measurements were made correctly, the numerical lengths are on different scales. Converting one column from meters to centimeters multiplies its entries by one hundred. Its squared variation grows by ten thousand. The principal direction can swing toward that column without any specimen having changed.

This is why the definition of distance belongs inside the scientific problem. Orthogonal distance in the raw coordinate plane is meaningful only relative to the units and relative importance assigned to its axes. Standardizing each variable by its standard deviation changes the geometry. It may be appropriate when each trait deserves equal relative weight. It may be inappropriate when absolute physical error is the relevant quantity. Neither choice can be justified by the eigenvector calculation alone.

Large deviations introduce another difficulty. Squaring distances gives extreme points disproportionate influence. One erroneous measurement far from the rest may substantially rotate the fitted line. Pearson's least-squares formulation is mathematically coherent, but the coherence does not make it immune to measurement error, selection bias, or outliers. Later robust statistics developed other ways to fit directions when such problems are expected.

There is a further distinction between a direction that describes variation well and a direction that predicts a specific outcome well. A principal component may capture the largest variation in a collection of physical measurements and still be irrelevant to the quantity an engineer wants to forecast. Conversely, a quiet, low-variance direction can carry a crucial signal. Optimization only promises what its objective asks for.

## What sampling can do to an apparently clear direction

A scientist rarely measures every member of a population. The covariance matrix comes from a sample. Imagine that the true population has a clear long axis, but a particular sample happens to contain a few points that lean in another direction. Its estimated leading eigenvector tilts. How confident should we be in that estimated direction?

Two quantities are important. One is the size of the error in the estimated covariance matrix. The other is the difference between the largest eigenvalue and the eigenvalue immediately below it. That second quantity is the spectral gap. When the gap is large relative to the perturbation, the leading direction cannot rotate very far. When two eigenvalues nearly agree, a small perturbation can produce a large change in the selected direction.

To picture the effect, consider an ideal covariance matrix whose horizontal variance is five and vertical variance is one, with no cross term. The leading direction is exactly horizontal and the gap is four. Now introduce a cross term of zero point two. The leading direction rotates by just under three degrees. If the two original variances were one point one and one, their gap would be only one tenth. The same cross term of zero point two would rotate the leading direction by almost thirty-eight degrees.

The precise spectral perturbation theorems that quantify such behavior were developed decades after Pearson, notably in work associated with Davis and Kahan. We should not credit Pearson with the later theorem. His fitting problem created an object whose stability is governed by eigenvalue separation. The geometry of principal components and the geometry of spectral subspaces meet at exactly this point.

Even a stable direction need not imply that the sample represents the population fairly. If a survey misses whole groups of people or uses instruments calibrated differently across groups, a small algebraic perturbation bound cannot repair that missing information. The choice of sample and the definition of the variables come before the spectral calculation.

## A laboratory, a journal, and an ambitious statistical program

Pearson's statistical work did not take place in isolation. In nineteen-oh-one he and Weldon founded Biometrika, with Galton associated with the enterprise. Its purpose was to provide a home for quantitative biological research at a time when some conventional biological venues resisted statistical methods. Publication was becoming part of a new scientific infrastructure: measurement programs, trained researchers, mathematical tables, new terminology, and a journal dedicated to arguments built from data.

The first issue presented a variety of biological measurements and statistical studies. The ambition was methodological as well as biological. Pearson wanted statistical research to be recognized as a specialized mathematical discipline, practiced by people trained to understand how a method worked and where it could fail. His laboratory became a place where mathematical calculations and large data-collection programs could be organized together.

Several women played significant roles in this circle. Alice Lee worked on statistical questions involving measurements of the human skull. Her research challenged claims that larger skulls demonstrated greater intellectual capacity, a claim sometimes used to rationalize the exclusion of women from intellectual life. Mary Beeton contributed to analyses of longevity and inherited traits. Their work reminds us that neither the mathematical labor nor the empirical challenges were the achievement of one professor alone.

That collaborative setting also raises hard questions about authority. Whose observations were treated as reliable? Who could decide the interpretation of a disputed relationship? Who received recognition for collecting, processing, and criticizing a dataset? Statistical institutions inherit the hierarchies of their time unless those hierarchies are themselves questioned. Pearson could support access to certain forms of education while also defending discriminatory hierarchies in his research program.

After Galton's death in nineteen eleven, Pearson became the first holder of the endowed Galton Chair of Eugenics at University College London. He directed a combined enterprise in applied statistics and eugenic research. The academic standing of the statistical methods and the institutional standing of the eugenic program reinforced one another. To describe the latter as an irrelevant sideline would misrepresent the way he organized his career.

## The scientific and moral failure of eugenics

Eugenics was a movement that proposed improving human populations by controlling reproduction according to judgments of supposedly desirable and undesirable inherited traits. It often used the language of biology and statistical inheritance to justify social classifications, restrictions, exclusion and coercion. Pearson was a committed advocate, and Francis Galton's money helped him establish the Galton Laboratory for National Eugenics in nineteen-oh-seven.

Pearson's published advocacy included racist descriptions of peoples and immigrants, concerns about the supposed decline of British racial stock, and arguments that presented racial competition as a force of human progress. The detailed UCL history of its eugenics programs documents his particular hostility toward Jewish immigrant communities in London's East End. Those positions are part of the historical record of the institution, rather than an incidental misunderstanding of a mathematical paper.

Why could mathematical statistics appear to lend authority to such ideas? A correlation between two measured traits can be mistaken for an innate biological relationship. A difference between group averages can be presented as a fixed difference in human worth. A distribution can be made to seem like a ranking of individuals that a government ought to enforce. Every move requires assumptions about what was measured, who was included, what causes the differences, and what moral conclusions could follow. Neither a covariance matrix nor a chi-square statistic supplies those assumptions.

For example, suppose a dataset shows that children of parents with more formal education tend to achieve higher examination scores. Even if the association is accurately measured, the children may also have access to different schools, resources, social networks and expectations. A regression coefficient by itself cannot partition that association into genetic and environmental causes. A principal direction through the data makes no causal claim at all. And even knowledge of a causal mechanism would not establish that people should be ranked in dignity or denied reproductive freedom.

Pearson did not merely happen to work during a period in which eugenics was popular. He taught, published and built an institution to promote it. A responsible history of his mathematics can recognize that his technical constructions remain valid while also explaining how his institutional and political choices helped legitimize a destructive movement. The moral harm is connected to decisions people made about applying and interpreting quantitative evidence.

## Disputes about inheritance and the limits of an apparent opposition

Around nineteen hundred, British biologists argued fiercely about inheritance. Weldon and Pearson emphasized continuous variation across populations. William Bateson and others studied discrete patterns associated with Gregor Mendel's work. A tidy textbook version would say that the biometricians rejected Mendelism and the geneticists rejected statistics. The real dispute was more complicated.

Historians have shown that Pearson considered several possible theories of inheritance. In certain settings he accepted a fundamental Mendelian idea for discontinuous variation and later discussed possible synthesis. The parties nevertheless disagreed about evidence, methods, and how much each account could explain. Personal quarrels, publication choices and public accusations intensified the scientific disagreement. Weldon died in nineteen-oh-six, leaving Pearson without the collaborator who had originally brought so many of the biological questions to him.

The distinction between continuous measurements and inheritance mechanisms is fundamental. A set of heights might show a smooth bell-shaped distribution even if the underlying genetic influences involve many discrete variants, combined with environmental factors. Continuous data do not logically rule out particulate inheritance. Conversely, a simple inheritance rule does not predict the detailed statistical behavior of every observed trait. The later development of population and quantitative genetics drew on both the genetics of inheritance and the mathematics of variation.

Pearson also had difficult intellectual relations with Ronald Fisher, whose statistical innovations addressed estimation, likelihood and the chi-square degrees-of-freedom problem. Fisher would become a major architect of twentieth-century statistics and population genetics. Pearson's son Egon later collaborated with Jerzy Neyman on a different framework for statistical testing. Their work is important in its own right, and the older Pearson's scientific authority should not be confused with an exclusive ownership of the methods that came after him.

Pearson's career joined influential mathematical work to contentious scientific arguments and harmful political commitments. The broader network generated mathematical methods of enormous scope, even as its participants disagreed about biology, probability, and society.

## How principal components acquired their later form

Pearson's nineteen-oh-one geometric fitting paper is now one of the standard early references in the history of principal components. But the modern subject did not spring fully formed from one article. Other nineteenth-century researchers had considered closely related orthogonal fitting questions. And in nineteen thirty-three Harold Hotelling recast principal components as a statistical analysis of several correlated variables, introducing an influential systematic terminology and motivation.

Hotelling's problem asked whether many observed variables could be represented through a smaller number of components with specified variance and correlation properties. That is close to Pearson's geometric line and plane, but the statistical framing changed the kinds of data, interpretation and applications that occupied center stage. Later generations connected principal components to matrix factorization, numerical algorithms, image analysis, spectroscopy and many other uses.

Consider an image represented by thousands of pixel values. A dataset of many similar images may vary primarily in illumination, pose or a small number of recurring patterns. An orthogonal low-dimensional approximation can compress the dataset effectively. But the leading directions may describe lighting or camera artifacts rather than the features a researcher wants to understand. The exact same mathematical objective can be useful for data compression and misleading for scientific interpretation.

This difference captures something important about Pearson's intellectual legacy. His mathematical technique provides a way to reduce a complicated cloud of measurements to a geometry of directions and distances. It also provides a temptation to treat those directions as objectively meaningful traits. The former is a theorem about minimizing squared error. The latter needs a scientific argument, including a careful account of measurement and causation.

## Retirement, remembrance, and the questions he leaves us

Pearson remained influential as an editor and institution builder for decades. He founded the Annals of Eugenics in nineteen twenty-five. He retired from University College London in nineteen thirty-three. Egon Pearson succeeded him in a central leadership role in the statistical department. Karl Pearson died on the twenty-seventh of April, nineteen thirty-six, in Surrey.

His memory has been reassessed as universities and historians have investigated the eugenics movement and its institutional connections. In June twenty twenty, University College London removed Pearson's name from named spaces, along with those honoring Galton. The university's own accounts document both the history of the research and the choices by which eugenics was established and supported. Changing commemorative names does not erase the statistical papers. It changes how an institution publicly expresses honor.

What remains of the mathematics? Start with the original four-point cloud. Center it. Choose any unit direction. Project each point onto that direction and measure the squared perpendicular loss. Pythagoras turns minimizing the loss into maximizing retained spread. The covariance matrix records the relevant quadratic expression, and the top eigenvector gives the optimum. In more dimensions, the leading eigenspace is the best orthogonal least-squares subspace of the requested dimension. This is a precise, useful and reproducible result.

What remains of the historical challenge? The best-fitting line is only best for a particular definition of error, using a particular set of measurements and a particular sample. Statistical accuracy does not confer moral authority. Causal claims and political judgments require arguments the eigenvalue calculation does not provide. Pearson's life brings these two lessons into the same room: a remarkably productive mathematical method, and the danger of asking mathematics to certify a hierarchy that the evidence and ethics cannot justify.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. The 1901 optimization problem and the role of centering

Let observations be `z_1,...,z_n ∈ R^d` and `m=(1/n)∑ z_i`. A candidate affine `k`-plane has the form `a+L`, with `dim L=k` and orthogonal projector `P_L`. Its residual is

\[
F(a,L)=\sum_{i=1}^n\|(I-P_L)(z_i-a)\|_2^2.
\]

Writing `x_i=z_i-m` and expanding the squares, using `∑x_i=0`, gives

\[
F(a,L)=\sum_i\|(I-P_L)x_i\|_2^2
+n\|(I-P_L)(a-m)\|_2^2.
\]

Thus an optimal affine plane passes through the sample mean; its displacement along `L` is immaterial. We may choose `a=m` and minimize over linear `L`. This is the **orthogonal-distance** problem, unlike ordinary vertical-residual regression. Pearson's 1901 article is an early geometric treatment; the terminology and statistical principal-components formulation were developed later.

### 2. Proof of the leading eigenvector and best `k`-subspace

Put the centered observations in a matrix `X∈R^{n×d}`, one row per observation, and define `S=X^T X/n`. The choice of divisor `n` rather than `n-1` scales eigenvalues without changing eigenvectors. Let `u` be a unit vector. Its orthogonal projection operator is `uu^T`. Pointwise Pythagoras gives

\[
\|x_i\|_2^2=|u^Tx_i|^2+\|x_i-uu^Tx_i\|_2^2.
\]

Therefore

\[
\begin{aligned}
F(u)&=\sum_i\|x_i-uu^T x_i\|_2^2
=\|X\|_F^2-nu^T S u,\\
\arg\min_{\|u\|=1}F(u)&=\arg\max_{\|u\|=1}u^T S u.
\end{aligned}
\]

For an orthonormal eigenbasis `v_1,...,v_d` of positive semidefinite `S` with `λ_1≥...≥λ_d≥0`, write `u=∑ a_j v_j`, `∑ a_j²=1`. Then `u^TSu=∑ λ_j a_j²≤λ_1`. Equality holds for a leading eigenvector and, if the leading eigenvalue is repeated, for every unit vector in its eigenspace.

For a rank-`k` orthogonal projector `P`,

\[
F(P)=\sum_i\|(I-P)x_i\|_2^2=\|X\|_F^2-n\operatorname{tr}(PS).
\]

The variational principle for eigenvalues gives `max_{rank P=k} tr(PS)=∑_{j=1}^k λ_j`. Thus a best `k`-plane is a span of leading eigenvectors, with minimum loss `n∑_{j>k} λ_j`. Uniqueness of the **subspace** of dimension `k` is ensured by a strict boundary gap `λ_k>λ_{k+1}`. The chosen eigenvector basis within the subspace need not be unique.

### 3. Four centered observations, checked arithmetic

Use rows

\[
X=\begin{pmatrix}3&1\\-3&-1\\1&-1\\-1&1\end{pmatrix},\qquad
S=\frac14 X^T X=\begin{pmatrix}5&1\\1&1\end{pmatrix}.
\]

Its eigenvalues are `3±√5`, or approximately `5.2360679775` and `0.7639320225`. The top eigendirection can be taken as `u=(1,√5-2)^T / sqrt(1+(√5-2)^2)`, with angle

\[
\theta=\tfrac12\arctan\!\left(\frac{2}{5-1}\right)
\approx13.28252559^\circ.
\]

The horizontal line retains average squared spread `5` and incurs total perpendicular loss `4`. The 45-degree line retains average spread `4` and has loss `8`. The optimal line retains `3+√5`, yielding

\[
F_{\min}=4\bigl(6-(3+\sqrt5)\bigr)=4(3-\sqrt5)
\approx3.0557280900.
\]

This example is newly constructed for teaching and is not claimed to appear in Pearson's paper.

### 4. SVD, covariance, normalization, and scale

If `X=UΣV^T`, then `S=(1/n)VΣ^2V^T`. The right singular vectors are covariance eigenvectors; covariance eigenvalues equal squared singular values divided by `n`. Directly forming `X^T X` squares the condition number of nonzero singular values (in exact arithmetic), so numerical implementations commonly prefer SVD or QR-based methods for ill-conditioned data.

Under a diagonal re-scaling `D`, the transformed covariance is `D S D`, and its principal axes generally rotate. Thus raw PCA depends on units. Standardizing columns gives a correlation-matrix version of PCA, changing the objective. Other objectives (robust loss, error weights, predictive loss) can be scientifically preferable. None is implied by the 1901 Euclidean criterion itself.

### 5. Perturbation and gap: an interpretable `2×2` illustration

For

\[
S_0=\begin{pmatrix}a&0\\0&b\end{pmatrix},\quad a>b,\qquad
S=S_0+\begin{pmatrix}0&\varepsilon\\\varepsilon&0\end{pmatrix},
\]

the top eigendirection rotates from the first coordinate axis by

\[
\theta=\frac12\arctan\left(\frac{2\varepsilon}{a-b}\right)
\quad \text{for } \varepsilon\ge 0.
\]

For `(a,b,ε)=(5,1,0.2)`, `θ≈2.85529657°`; for `(1.1,1,0.2)`, `θ≈37.98187827°`. Same perturbation magnitude, different initial gap. Later Davis–Kahan inequalities generalize the relationship between subspace rotation, the perturbation and a suitable separation assumption. These later results are not attributed to Pearson.

### 6. Chi-square and regression: distinct objectives

For category counts `O_i` and hypothesized expected counts `E_i>0`, Pearson's statistic is

\[
\chi^2=\sum_i\frac{(O_i-E_i)^2}{E_i}.
\]

With observed counts `(30,20)` and fixed expected counts `(25,25)`, the value is `2`. For a two-category multinomial total with no estimated probabilities, one free category-count deviation yields asymptotic `χ²_1`; the upper-tail probability at `2` is approximately `0.1573`. Model fitting and dependence may alter degrees of freedom; the chi-square asymptotic approximation also needs suitable expected counts. Fisher's later work clarified parameter-estimation corrections to Pearson's original calibration.

For points `(x_i,y_i)`, ordinary regression of `y` on `x` minimizes `∑ (y_i-α-βx_i)^2`, treating vertical error as the objective. Orthogonal fitting minimizes `∑dist((x_i,y_i),L)^2` over affine lines `L`, permitting vertical lines. Neither is universally the right measurement model; they solve different optimization problems.

### 7. Statistics, causes and the eugenics program

Correlation, regression, chi-square tests and PCA describe numerical relationships under stated models. They do not establish genetic determination, causal effects, race-based hierarchies, or normative policies. Pearson's racist and eugenic advocacy and his role establishing the Galton Laboratory are documented in UCL's own historical and archival accounts. UCL removed honorific names for Pearson and Galton from campus spaces in 2020.

A specific interpretive risk is the inference from `Cov(X,Y)≠0` to an inherent causal relationship between `X` and `Y`. Common causes, selection effects, measurement definitions, and other variables can produce the same observed covariance. That observation is mathematical and conceptual; it does not make statistical inference impossible. It identifies the additional design and causal assumptions needed.

### 8. Chronology and sources

- **1857:** Born March 27 in London. Family initially named him Carl; adopted Karl in youth.
- **1875–1879:** King's College, Cambridge; third wrangler in 1879.
- **1879–1882:** Heidelberg and Berlin studies, then legal education in London; called to the bar in 1881 (some biographies state 1882).
- **1884–1890:** Goldsmid Chair of Applied Mathematics and Mechanics at UCL; Men and Women's Club in 1885; marriage to Maria Sharpe in 1890.
- **1889–1892:** Galton's *Natural Inheritance* (1889), Weldon's appointment at UCL (1890), Pearson's *The Grammar of Science* (1892).
- **1893–1900:** *Mathematical Contributions to the Theory of Evolution*, correlation and regression, skew distributions, Pearson's 1900 chi-square paper.
- **1901:** Founding of *Biometrika* with Weldon and Galton associated; Pearson's *On Lines and Planes of Closest Fit to Systems of Points in Space*, *Philosophical Magazine*, Series 6, vol. 2, no. 11, pp. 559–572, DOI `10.1080/14786440109462720`; Alice Lee and Pearson's work on skull correlation.
- **1906–1911:** Weldon's death (1906); Francis Galton Laboratory for National Eugenics established in 1907; Galton's death in 1911; Pearson becomes first holder of endowed Galton eugenics chair.
- **1925–1936:** *Annals of Eugenics* founded 1925; retired 1933; died April 27, 1936, at Coldharbour, Surrey.
- **1933 and after:** Hotelling's *Analysis of a Complex of Statistical Variables into Principal Components*; subsequent SVD-based computation and spectral perturbation theory.
- **2020:** UCL renames campus spaces honoring Pearson and Galton as part of its institutional response to its eugenics history.

### Reading notes (non-spoken)

**Primary mathematical papers:** Pearson (1900), *On the Criterion that a Given System of Deviations from the Probable ...*, *Philosophical Magazine* 50, pp. 157–175; Pearson (1901), *On Lines and Planes of Closest Fit to Systems of Points in Space*, *Philosophical Magazine*, Series 6, 2, pp. 559–572, DOI `10.1080/14786440109462720`; Hotelling (1933), *Analysis of a Complex of Statistical Variables into Principal Components*, *Journal of Educational Psychology* 24, pp. 417–441 and 498–520. Later historical research by R. W. Farebrother (2022) discusses predecessors to Pearson's orthogonal fitting construction; the 1901 paper should not be framed as inventing every element of modern PCA.

**Biography and historical scholarship:** MacTutor's Pearson biography; the Royal Society's personal record; UCL's Karl Pearson archive guide and institutional history; UCL's *History of Eugenics Inside UCL*; M. Eileen Magnello (1998), *Karl Pearson's Mathematization of Inheritance*, which complicates the simple biometrician-versus-Mendelian story; Alice Lee's biographical and published work; and UCL's 2020 denaming announcement. Each documented historical assertion has an anchored reference in `metadata/024000.json` and its URL in `metadata/sources.json`.

**Provenance of worked examples:** The four-point covariance, two rotation examples, and fifty-toss chi-square illustration are constructed instructional examples; they are independent of the historical papers' specific data. Mathematical identities are derived above and were independently recalculated for this lecture.
