# 028000 — Spectral Sequences: Recovering Homology in Stages

**Track:** Abstract Algebra. **Background:** chain complexes, homology, long exact sequences, filtrations and quotient modules. **Central question:** how can a complicated homology calculation be assembled from simpler layers without losing the interactions between them?

<!-- BEGIN SPOKEN LECTURE -->

# Spectral Sequences: Recovering Homology in Stages

A chain complex packages a sequence of maps whose successive compositions are zero. Its homology detects classes killed by one map but not produced by the preceding map. In simple examples we can compute all kernels and images directly. In a large filtered complex, or in a double complex with two differentials, that direct calculation may be impractical.

A spectral sequence is a method for solving such a calculation in stages. It does not magically make difficult homology disappear. Instead it organizes approximations to the answer, together with a succession of correction maps that remove apparent classes that do not survive in the full complex.

## Begin with a filtration

Suppose we have a cochain complex C, so its differential raises degree by one. Give it a decreasing filtration: C is built from subcomplexes F zero containing F one containing F two, and so on. Because each F p is a subcomplex, the differential preserves the filtration. We first look at the associated graded pieces: each F p divided by F p plus one.

Think of the filtration as layers of an archaeological site. On one layer we see a particular class, but part of the relation that kills it may lie in another layer. The associated graded complex forgets some interactions between layers. It is easier to compute, but it can show classes that are not genuine classes of the total complex.

The first page, often called E zero, is built from those associated graded pieces with the part of the differential that stays within one layer. Taking the cohomology of that first page gives E one. The later pages are obtained by taking the cohomology of correction differentials. A class surviving one page can still be killed by a differential that changes filtration level further.

## A two-term example where the first answer is wrong

Consider a cochain complex over a field k with one generator x in degree zero and one generator y in degree one. The differential sends x to y. Because that map is an isomorphism, the total cohomology is zero in both degrees.

Now filter the complex so y occupies the deeper layer: F zero is the whole complex; F one contains y but not x; F two is zero. The first associated graded page contains x in the first layer and y in the second. On that associated graded page, the differential is zero, because the map from x to y jumps across the filtration. So both x and y initially look like cohomology classes.

But the first correction differential sees the very map we had hidden. It sends the class of x to the class of y. It is an isomorphism. On the following page, both classes disappear. The limiting page is zero, matching the true cohomology of the original complex.

This is the essential behavior of a spectral sequence in miniature. A page is a provisional calculation. A class on page one is not necessarily a class of the total object. We must let the permitted differentials act before claiming survival.

## The indices carry information

One common convention for a decreasing filtration of a cochain complex labels terms E r with two indices, p and q. Their sum is the total cohomological degree. The page-r differential moves p to p plus r and moves q to q minus r plus one. It therefore raises total degree by one, as a cochain differential must.

The index r measures how far the differential jumps between filtration layers. The first page handles local information; later pages handle more distant interactions. This is why a spectral sequence can stop quickly when the grading forces all potential targets of later differentials to be zero.

On each page, a class is meaningful only modulo the classes that entered as boundaries on that page. After taking cohomology, the next page contains classes that survived that test. This repeated quotienting is precisely what makes the calculation systematic.

## Convergence does not mean literal equality

Under suitable boundedness and convergence hypotheses, the pages stabilize to E infinity. It is tempting to say E infinity *is* the cohomology of the total complex. That is often too strong. E infinity is generally the associated graded object of a filtration on the total cohomology.

Knowing the graded pieces need not tell us how they fit together as an unfiltered object. For abelian groups, two graded pieces each isomorphic to the integers modulo two might assemble to the direct sum of two copies, or to the integers modulo four, depending on extension data. The earlier Ext lecture tells us how to describe exactly that ambiguity.

Over a field, finite-dimensional filtered vector spaces split noncanonically, so dimensions can often be reconstructed by adding graded dimensions. But even then the splitting is not a canonical identification. Over rings the extension problem can change the isomorphism type.

## Double complexes give two routes

A double complex has objects arranged in a grid and two differentials, one moving horizontally and the other vertically, with the required anticommutation relation. By combining them with signs we form a total complex whose differential squares to zero.

We can filter the total complex by columns or by rows. Each choice leads to a spectral sequence. With a column filtration, one often computes vertical cohomology first, then learns how the horizontal maps act on it. With a row filtration, the order is reversed.

The two spectral sequences may look different at the beginning yet, under appropriate boundedness conditions, they converge to the same total cohomology. This ability to choose the cheaper first calculation is a major practical advantage. In geometry and homological algebra it often turns a large combined problem into a sequence of tractable local calculations.

## What a proof must check

Before using a spectral sequence, ask four questions. What exact complex is filtered? Which convention is used for indices and differentials? What hypotheses ensure convergence to the intended object? And, once E infinity is obtained, are there unresolved extension problems?

A diagram of boxes with arrows is not a proof without those answers. The method is powerful precisely because its conventions and convergence statements have exact mathematical content.

We can now see why spectral sequences appear whenever a mathematical object is assembled in layers: a filtered complex, a fibration, a group extension, or a derived functor composed with another. The first approximation finds candidate classes. Successive differentials decide which survive. The limiting information describes the graded pieces of the answer, and extension data may finish the reconstruction. A spectral sequence is a disciplined way to keep track of what each layer conceals about the others.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \((C^\bullet,d)\) be a cochain complex with a decreasing filtration \(F^pC^\bullet\) by subcomplexes. A standard convention is
\[E_0^{p,q}=F^p C^{p+q}/F^{p+1}C^{p+q},\quad E_1^{p,q}=H^{p+q}(\operatorname{gr}^p_F C^\bullet),\quad d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}.\]
Each \(E_{r+1}\) is the cohomology of \((E_r,d_r)\). Under appropriate boundedness / exhaustive and separated convergence hypotheses, \(E_\infty^{p,q}\cong\operatorname{gr}^p_F H^{p+q}(C)\). This does **not** specify the extension classes necessary to reconstruct the unfiltered cohomology.

**Toy example:** \(C^0=k\langle x\rangle\xrightarrow{d}C^1=k\langle y\rangle\), \(d(x)=y\). Put \(F^0C=C\), \(F^1C^0=0\), \(F^1C^1=C^1\), \(F^2C=0\). Then \(d_0=0\) on the associated graded, \(E_1^{0,0}=k\langle[x]\rangle\), \(E_1^{1,0}=k\langle[y]\rangle\), and \(d_1([x])=[y]\) is an isomorphism. Therefore \(E_2=E_\infty=0=H^\bullet(C)\).

**Extension caution:** an associated graded abelian group with two successive quotients \(\mathbb Z/2\) need not determine whether the full group is \((\mathbb Z/2)^2\) or \(\mathbb Z/4\). Differential and filtration-index conventions vary across homological and cohomological versions; convert them explicitly when citing formulas.

### Exercises with answers

1. Why is \(d_r\) of total cohomological degree one? **Answer:** its index changes total degree by \(r+(-r+1)=1\).
2. In the toy example, why does the E-one page have nonzero terms although total cohomology vanishes? **Answer:** the only differential raises filtration and is invisible to \(d_0\); it is detected by \(d_1\).
3. Does \(E_\infty\) uniquely determine \(H^\bullet(C)\) as an abelian group? **Not in general:** one must solve extension problems.
4. If a differential's target term is zero, can that differential kill the source class? **No:** but another page or an incoming differential may still affect the class unless all possibilities are ruled out.

### Reading and source notes

- [Stacks Project, Section 12.24: Spectral sequences from filtered complexes](https://stacks.math.columbia.edu/tag/012K), precise grading and differential conventions.
- Allen Hatcher, [Algebraic Topology and supplementary spectral-sequence materials](https://pi.math.cornell.edu/~hatcher/), geometric spectral-sequence applications and convergence.
- Charles A. Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), spectral sequences and derived functors.
