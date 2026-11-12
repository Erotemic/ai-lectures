# 025000 — Harold Hotelling: How did subspace geometry become statistical inference?

**Track:** History · People and ideas. **Theme:** Statistical subspaces. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# Harold Hotelling: How did subspace geometry become statistical inference?

A data table may contain many correlated measurements. We can ask whether a few combinations of those measurements carry most of the variation. We can also ask how two sets of measurements relate to each other. Both questions lead to angles and spectral subspaces.

Harold Hotelling was an American statistician and mathematical economist. His 1933 treatment of principal components and his 1936 work on relations between two sets of variates helped establish these tools in multivariate statistics. The geometric ideas had earlier roots, including Karl Pearson's line-fitting work, but Hotelling placed them within a systematic statistical framework.

For principal components, start with a covariance matrix. Its largest eigenvalue describes the direction of greatest variance, and its leading eigenvector gives that direction. If we retain the top two eigenvectors, their span is a two-dimensional subspace capturing two important modes of variability. The details depend on the data and its scale, but the linear-algebra construction is exact.

Canonical correlation asks a related question involving two sets of variables. We seek one linear combination from each set with maximal correlation. After appropriate normalization and whitening, the calculation reduces to singular values of a cross-covariance-related matrix. Those singular values can be interpreted as cosines of angles between suitably constructed subspaces.

Now introduce sampling. The covariance matrices are not known exactly; they are estimated. A finite sample may rotate a leading eigenspace. If the first two population eigenvalues are nearly equal, their individual eigenvectors are hard to identify consistently. If the two-dimensional cluster is separated from the remaining spectrum, the two-dimensional subspace may still be reliably estimated.

This is the statistical version of the eigenvector rotation problem. The target is a population subspace, the observed object is a sample subspace, and the perturbation comes from estimation error. A Davis–Kahan-type bound relates covariance estimation error and an appropriate spectral gap to the angular discrepancy.

Hotelling's role is to make spectral geometry a language for variation and association in data. His questions gave later perturbation results a natural statistical application: how confident should we be that a pattern found in the sample represents a genuine direction in the population?

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

For centered random vector \(X\) with covariance \(\Sigma\),
\(\operatorname{Var}(u^*X)=u^*\Sigma u\) for a unit vector \(u\).
PCA maximizes this over \(u\). In a whitened canonical-correlation problem,
singular values of the normalized cross-covariance matrix give canonical
correlations. Hotelling's major PCA and CCA papers appeared in 1933 and 1936.

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
