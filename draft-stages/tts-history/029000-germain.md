# 029000 — Sophie Germain: How can a mathematician prove something beyond the reach of her world?

**Track:** History · People and ideas. **Theme:** The arithmetic of Fermat's equation, correspondence networks, and the mathematics of vibrating surfaces. **Background:** primes, elementary congruences, the idea of a derivative; more advanced concepts are explained locally.

<!-- BEGIN SPOKEN LECTURE -->

# Sophie Germain: How can a mathematician prove something beyond the reach of her world?

Imagine a sheet of metal sprinkled with fine sand. Draw a violin bow along its edge and the plate begins to sing. The sand jumps away from the regions that move and collects along the lines that remain almost still. Some patterns are simple crosses. Others branch into delicate curves. Change the way the plate is held, or the frequency of the bow, and the pattern changes. Two questions arise. Can an equation predict these pictures? And if an equation predicts a particular picture, does that mean we understand why the plate moves as it does?

Now imagine an entirely different problem. Three whole numbers might satisfy the Pythagorean equation: the square of three plus the square of four equals the square of five. What happens when every square becomes a fifth power? Or an eleventh power? How could we rule out all possible whole-number solutions without checking numbers forever?

Sophie Germain worked seriously on both questions. She lived in Paris from seventeen seventy-six to eighteen thirty-one, in a period of revolutions, wars, the emergence of new technical institutions, and intense mathematical innovation. She did not receive the educational access that her male contemporaries enjoyed. She learned through books, lecture manuscripts, correspondence, and persistent independent work. She became an original number theorist and an important early contributor to the theory of elastic surfaces. Her manuscripts also reveal a wider research program than the single theorem that eventually carried her name.

To understand Germain's achievement, it helps to keep the mathematics in view. Her career is neither a story of exclusion alone nor a simple victory tale in which every proposed proof succeeds. She made discoveries; she took wrong turns; she revised arguments; she pursued hard problems that had defeated specialists. Both her achievements and the limits of her results are part of the history.

## A reader in revolutionary Paris

Germain was born in Paris on April the first, seventeen seventy-six. Her family had the resources for books and education, but university mathematics was not presented as a respectable career for a girl. The French Revolution began when she was thirteen. Books became the opening through which she entered higher mathematics, and the revolutionary politics of her family made that private education part of a larger life.

Her household gives a more specific picture of the opportunities and restrictions around her. Her father, Ambroise-François Germain, was a prosperous merchant who participated in the public politics of the French Revolution and later held a position at the Bank of France. There were political and philosophical discussions around the family, and a substantial library. Germain was thirteen in seventeen eighty-nine, when Paris became the center of a revolution. A young person seeing the streets and institutions of her city being overturned could encounter antiquity and mathematics inside a book while the political future outside the house was uncertain. In the family library she found a history of mathematics by Étienne Montucla. Its account of Archimedes, so absorbed in geometrical problems that he failed to notice a soldier approaching, made a lasting impression according to later biographical accounts. The story belongs to her intellectual formation, even though details such as frozen ink in the family library have also accumulated the embellishments of retelling.

Her education in mathematics was self-directed. She learned to work with the language of equations, then studied the authors whose books would have been part of a male student's formal training. Mathematics was expanding beyond Euclidean geometry. Calculus had made motion, growth, and curvature subjects for equations. Number theory asked how the indivisible pieces of arithmetic, the prime numbers, control relations among integers. These subjects demanded different habits. In calculus one might replace a difficult curve with a manageable approximation; in number theory a single exception can destroy an alleged proof about all integers.

Her decision was not universally welcomed at home. The best-known account says her family tried to interrupt the late-night studying, and eventually gave up when it became clear she would continue. The familiar scene of blankets and an unheated room comes from biographical tradition; it illustrates how later writers remembered her determination, but it need not be recited as a witnessed event. What we can establish is that she kept teaching herself from serious mathematical books. She worked through Bézout's textbooks, Cousin's calculus, and the writing of Newton and Euler. Her family continued to support her materially. That mixture of opposition and support complicates the simple story of a daughter escaping an entirely hostile household.

In seventeen ninety-four, when Germain was eighteen, the École Polytechnique was founded in Paris to train engineers and scientists. Women could not enroll as students. But notes from lectures circulated, and student work could reach professors. Germain acquired these materials and submitted some of her calculations under the name Monsieur Le Blanc, the name of a male student. This allowed her work to be assessed before its author was identified as a woman. She eventually entered a professional relationship with Joseph-Louis Lagrange, who recognized her mathematical abilities.

We should be careful with what this story means. An adopted name let her take part in a limited written exchange. It did not confer a degree, access to every classroom, a salary, or the daily conversation available to enrolled students. An essential resource in mathematics is the chance to ask a badly formed question in front of people who know the subject and to have it repaired before months of work build on a mistake. Germain often had to recreate that feedback process through letters.

She corresponded with Adrien-Marie Legendre, one of France's leading number theorists, and later with Carl Friedrich Gauss in Göttingen. At first Gauss also knew her as Le Blanc. During the French occupation of German territories, she arranged through a French officer to check on Gauss's safety. When the intervention disclosed her identity, Gauss replied with admiration for her mathematical resolve. Their letters are valuable historical evidence because they show a living exchange about number-theoretic ideas, rather than simply a list of famous names attached to a biography.

There is a revealing episode in the correspondence with Gauss. When French troops occupied the region around his home in Brunswick, Germain remembered the story of Archimedes killed during a city's capture. She feared that a mathematician might again be at risk in a military occupation. Through a family connection she asked a French general to look after Gauss. Gauss could not identify the woman who had intervened for him, and her action forced the disclosure that his correspondent Monsieur Le Blanc was Sophie Germain. In her explanation she acknowledged that she had concealed her sex because being known as a learned woman could invite ridicule. Gauss responded with admiration. The episode shows concern for a colleague whom she knew chiefly through mathematical letters, and it gives the pseudonym a far more personal meaning than a mere trick to submit homework.

## Fermat's problem, one exponent at a time

The theorem now called Fermat's Last Theorem states that if an exponent is greater than two, three nonzero integers cannot satisfy the equation: the first to that exponent, plus the second to that exponent, equals the third to that exponent. The familiar squares case is possible; three squared plus four squared equals five squared. The cubes case is impossible. So are all the higher cases, although the general proof was not completed until the late twentieth century.

Why do mathematicians focus on prime exponents? Suppose an exponent is divisible by an odd prime, say fifteen is divisible by five. A hypothetical solution with fifteenth powers would also give a solution with fifth powers by grouping each number into a cube first. Even exponents divisible by four reduce to the fourth-power case. This means that to establish the whole theorem it suffices to handle exponent four and every odd prime exponent. Germain could concentrate on a prime she called p and ask which arithmetic restrictions any counterexample would have to satisfy.

Start with a simpler task: checking an equation modulo a small prime. Modulo eleven, for example, we regard numbers that differ by eleven as equivalent. Twelve acts like one; twenty-two acts like zero. This does not solve the equation over the integers, but it lets us test a necessary condition. A genuine integer solution must remain a solution after every reduction modulo a prime.

Take p equal to five and reduce fifth powers modulo eleven. One way to calculate all ten possible nonzero fifth powers would be to make a table. A more revealing way uses a basic theorem of Fermat: when a number a is not divisible by eleven, the tenth power of a leaves remainder one modulo eleven. The tenth power is the square of the fifth power. Therefore the fifth power of a must be either one or minus one modulo eleven. There are only two possibilities. All ten nonzero inputs collapse into two output classes.

Let's see a concrete pair. Two to the fifth power is thirty-two, which leaves remainder ten modulo eleven: that is minus one. Three to the fifth power is two hundred forty-three, which leaves remainder one. The point is not to memorize the table. It is to notice what happened to the enormous search space. A fifth power, modulo eleven, is either zero, one, or minus one.

Suppose for contradiction that x to the fifth plus y to the fifth equals z to the fifth. If none of x, y, and z were divisible by eleven, then each of their fifth powers would be plus or minus one modulo eleven. But the sum of two values chosen from plus and minus one is minus two, zero, or plus two. None of those is plus or minus one modulo eleven. This is impossible. So a hypothetical solution must have at least one of x, y, and z divisible by eleven.

That is a genuine deduction, but it is not yet Fermat's theorem. We have said that eleven divides one of the three numbers. We need to exclude solutions in which five divides none of them. Why should a statement about eleven have anything to do with divisibility by five? Germain found ways to link these two primes through the arithmetic of p-th power residues. That additional step is the difficult part of the argument, and pretending that the first modular observation already completes it would misrepresent her theorem.

## A modular argument as an instrument of proof

There is a useful way to think about modular arithmetic that makes Germain's method more than a trick for large numbers. Suppose someone claims to possess three enormous integers that solve a fifth-power equation. The integers might have hundreds of digits, so we cannot examine all possibilities. Instead we give that person a sequence of small tests. What are your numbers modulo eleven? What are they modulo five? What happens modulo another prime chosen for a special reason? Each test discards many proposed solutions at once, because a true integer equality has to pass every modular test.

The important word is necessary. Passing a modular test does not certify a solution. It only means that this particular test has not ruled it out. For example, three numbers might leave remainders that satisfy a fifth-power congruence modulo a given prime and still fail the original integer equation completely. Mathematics has to distinguish a filter from a characterization. Germain's achievement was to design filters strong enough to prove that a whole class of alleged solutions cannot exist.

For an exponent p, imagine listing the p-th powers modulo a prime q. If those powers cover every nonzero remainder, an equation between them may have many possible residue-level solutions. That prime is not necessarily helpful. But if only two residues occur, or if the residues have large gaps in a precise arithmetic sense, the equation has little room to operate. The choice of the prime is part of the ingenuity of the proof.

An auxiliary prime is therefore not a magical numerical constant. It is a deliberately chosen coordinate system for an arithmetic contradiction. We use the prime because it transforms exponentiation into a controlled finite pattern. This is also why infinitely many primes would have been so valuable to Germain's larger plan. Each additional prime with the right property could impose another independent divisibility demand on a hypothetical solution. To turn that vision into a theorem, however, one must establish that such primes exist in the required abundance. Experimental patterns or calculations for many exponents cannot replace that step.

Even the phrase first case deserves attention. A case distinction may sound like mere bookkeeping, but it can identify a genuine dividing line between possible proofs. When the exponent p divides none of x, y, and z, one set of divisibility arguments becomes available. When p divides one of them, different congruences and factorization phenomena arise. A proof restricted to the first case can be general across infinitely many prime exponents and still leave the harder second case untouched. Germain's work taught number theorists to recognize that distinction.

## The extra prime that changes everything

A prime p is now called a Sophie Germain prime when twice p plus one is also prime. For p equal to five, twice five plus one is eleven. For p equal to eleven, the partner is twenty-three. The definition packages a useful arithmetic coincidence: the number of nonzero remainders modulo the larger prime is exactly twice the exponent p.

When q equals twice p plus one and is prime, Fermat's little theorem gives a raised to the power two p equal to one, modulo q, for every nonzero remainder a. So its p-th power has square one. Since we are working modulo a prime, the only roots of that equation are plus and minus one. That collapses all the nonzero p-th powers to two values, just as it did for five and eleven.

To finish the classical first-case argument, Germain needed another condition: p itself must not be a p-th power modulo the auxiliary prime. For an odd prime p with q equal to twice p plus one also prime, p is neither plus one nor minus one modulo q, so that condition holds. Her theorem then says something much stronger than the first modular observation: in any integer solution to Fermat's equation for exponent p, at least one of the three terms must be divisible by p squared. In particular, there cannot be a solution in which none of the three numbers is divisible by p. That is called the first case of Fermat's Last Theorem.

Notice the distinction. First case means p divides none of the three integers. Second case means p divides at least one. A theorem that excludes the first case is a major partial result, but it does not establish the second case. For p equal to five, eleven is a valid auxiliary prime, and Germain's theorem eliminates first-case solutions. The same method does not automatically finish the full fifth-power equation.

There is a more general version of the method. Instead of requiring q to equal twice p plus one, one searches for an auxiliary prime with two properties. No two nonzero p-th power residues differ by one modulo q; and p is not itself a p-th power residue modulo q. With these conditions, Germain's conclusion about the first case still follows. The elementary observation that a sum of two powers must match a third is transformed into a systematic search for primes with carefully controlled residue classes.

At this point it is tempting to think that success consists merely of checking more primes. But Germain had a much more ambitious idea. She sought to show that, for each exponent, there were infinitely many auxiliary primes of suitable forms and that these would force an alleged solution into arithmetic restrictions too strong to satisfy. The surviving manuscripts reveal calculations, algorithms, and structural arguments toward that objective. The full program was not proved, and the later solution of Fermat's Last Theorem followed a different route.

It is also worth remembering the physical form of that correspondence. Germain worked without the daily seminar, graduate students, or colleagues that sustain modern research. A proof would be drafted at home, copied into a letter, sent across Europe, and perhaps discussed months later. Gauss admired her command of his book, but the correspondence eventually thinned. Legendre remained a significant mathematical contact. Their exchanges show both intellectual reciprocity and the asymmetry of a woman without a formal appointment seeking judgment from men who occupied the profession's established institutions. Her ambitious investigations of auxiliary primes developed under those conditions, with uncertainty about how, when, or whether the results would be seen.

## What the manuscripts changed about the history

For a long time, discussions of Germain's number theory centered on a theorem published through Legendre's work in eighteen twenty-three. It is an important result, and Legendre acknowledged her contribution. Yet judging Germain's entire research program by that one published fragment left much of her mathematics out of sight.

Reinhard Laubenbacher and David Pengelley studied her unpublished manuscripts in detail and published a reassessment in two thousand ten. They found a developed strategy for attacking the whole Fermat problem, including forms of auxiliary-prime analysis that went beyond the popular textbook statement of her theorem. Their work describes her effort to establish a condition forbidding consecutive nonzero power residues. That condition is exactly the sort of obstruction we encountered in the small example with fifth powers modulo eleven.

Consider what consecutive means here. Suppose two nonzero numbers are both p-th powers modulo q, and one is exactly one more than the other. That gives two residue values separated by one. If we can prove such a pair cannot exist, then the difference of two nonzero p-th powers cannot equal one modulo q. Fermat's equation, after dividing by an appropriate nonzero power when permitted, would demand just such a relation. A modular contradiction becomes possible. Germain investigated when this can happen for q of the form twice N times p plus one, with N a positive integer.

Her research was more than a lucky observation about two primes. She searched for a family of obstructions and tried to understand which auxiliary primes obeyed them. The manuscripts include a conjectural step she could not establish: enough favorable primes should exist to force the desired contradiction for each exponent. A conjecture can be fruitful without being a theorem. Here the uncompleted step explains both the reach and the limitation of the project.

The letters also show that Germain repeatedly divided her time between number theory and elasticity. This was not a distraction from a single central passion. Both subjects held open problems where a new mathematical structure could bring an immense collection of cases under a small set of principles. In one, the cases were infinitely many integers. In the other, the cases were infinitely many possible movements of a surface.

## Sound from a thin sheet

In eighteen hundred eight, Ernst Chladni demonstrated vibrating plates in Paris. Sand spread over a plate gathers on nodal curves: places where a particular mode of vibration has zero displacement. The visible pattern is a snapshot of an invisible standing wave. A plate can bend in many ways, so a successful theory must say which shapes can vibrate steadily and at what frequencies.

Start with a string stretched between two supports. If its ends cannot move, some standing waves fit and others do not. One pattern has a single hump. The next has two humps, separated by a point that does not move. More complicated patterns have more nodes. There is a whole ladder of permitted frequencies. For an ideal string under fixed tension, the frequencies grow in proportion to the mode number: the second mode has twice the fundamental frequency.

A metal plate resists bending rather than merely stretching. This changes the governing mathematics. Curvature, not just slope, measures deformation. A plate's bending energy depends on how sharply the surface curves, and the equation of motion contains higher spatial derivatives than the string equation. In modern thin-plate theory a familiar idealized model is mass per area times the second time derivative of displacement, plus bending stiffness times the spatial biharmonic of displacement, equal to zero. The biharmonic is what results when we apply the two-dimensional Laplacian twice.

That modern formula is useful for understanding the problem, but it should not be presented as a line copied directly from Germain's work. The eventual theory of elastic plates required contributions from several mathematicians and engineers, including Lagrange, Poisson, Navier, and Kirchhoff, with careful attention to mechanical assumptions and boundary conditions. Germain's efforts belong to the early development of that theory. Some of her proposed principles lacked a complete mechanical derivation.

The Academy of Sciences offered a prize for a mathematical description of elastic surfaces consistent with experiment. Germain entered the competition in eighteen eleven. Her first submission did not win. Lagrange identified errors and advanced a corrected equation. The competition was extended; Germain submitted again and received honorable recognition, but the derivation was still unsatisfactory. On a third attempt, judged in eighteen sixteen, she received the Academy's prize. The award recognized a substantial achievement even though doubts about the foundation of her model remained.

The elasticity competition made these circumstances more visible. Germain entered repeated prize rounds and met criticism from some of the strongest analysts in France. Lagrange helped improve the mathematical framework; Poisson challenged aspects of her reasoning and advanced competing analyses. The friction was intellectual and institutional at once. She needed her physical model to match Chladni's experimental patterns, but she also needed the Academy to recognize the method as sound. Winning the prize in eighteen sixteen was therefore an accomplishment shadowed by an unfinished theoretical problem. Germain did not become a salaried academic after the award. Recognition provided no ordinary professional security, and she continued working largely through a network of letters.

It is worth spending time on that distinction. A theory can give plausible numerical predictions for observed patterns while resting on an incomplete derivation. Theories of physical systems need both: agreement with experiments and an understanding of the forces and conservation laws producing the equation. Germain pressed against the boundary of what contemporary analysis and mechanics could explain. Her prize did not mean that every technical question about elastic plates had been settled.

## Why the boundary changes the music

Let's use a simpler one-dimensional object, a narrow bending beam, to understand the main feature of the plate problem. Imagine a beam supported so that its ends cannot move vertically but can rotate. When the beam bends into a smooth arch, the curvature tells us how strongly it resists deformation. A mode with many alternating bends has much greater curvature than a mode with one gentle bend.

For an ideal simply supported uniform beam, the permitted shapes are sine waves. The first has one hump, the second has two, and so on. For a stretched string the frequency of the second pattern is twice the first. For the bending beam, in the ideal Euler–Bernoulli model, it is four times the first. The reason is that bending introduces a fourth spatial derivative: the frequency grows like the square of the mode number rather than linearly.

Now return to the two-dimensional plate. There is more room for shapes. One can bend across the width, across the length, or in combinations. The outline of the plate and the way its edges are restrained affect which patterns are allowed. A circular plate supported at its edge is a different mathematical problem from a square plate held along one side. This is why merely writing a differential equation without specifying what happens at the boundary is not enough to predict Chladni figures.

The sand images are therefore evidence about both the physical law and the constraints. If our mathematical model predicts the wrong nodal lines, perhaps the stiffness is modeled incorrectly, perhaps the plate is not uniform, or perhaps the support condition has been described badly. The picture gives a way to test an abstraction. Germain was working at a time when mathematicians were still developing the language for all these parts of the problem.

One reason her elastic-surface research is easy to oversimplify is that later engineering successes invite retroactive credit. Thin-plate theory contributes to modern structural design, and Germain is sometimes connected in popular accounts to the Eiffel Tower. That is not evidence that she designed the tower or established the final engineering equations on her own. A fair historical account credits her early theoretical work and the Academy recognition, while distinguishing the later development of the subject.

## The mathematics of a standing-wave pattern

We can make the relation between a visible nodal pattern and an equation more precise. Suppose a plate oscillates in such a way that its shape keeps returning to the same outline. The displacement at a point can then be approximated as a fixed spatial shape multiplied by a periodic function of time. At one instant the plate bulges upward in some regions and downward in others. Half a period later the signs reverse. Along the nodal curves the spatial shape is zero, so those points stay still throughout the motion.

Finding such a shape is an eigenvalue problem. The equation for bending takes a proposed spatial pattern as input and produces another spatial function. A standing wave is one of the special patterns that the operator returns as a multiple of itself. The multiplier determines the frequency after the mass and stiffness factors are included. This is the same general kind of idea that appears in matrix eigenvectors: a transformation preserves a direction, changing its magnitude by a scalar. On the plate, the direction is an entire function, one possible pattern of displacement.

This perspective also explains why mathematics alone cannot predict exactly what a real plate will do without information from physics. The plate has a material thickness and density. The force law determines bending stiffness. A clamp prevents rotations and displacements that a free edge would allow. Those choices alter the eigenvalue problem. The observed Chladni figures are valuable precisely because a candidate theory can be held against a real pattern and tested.

The eigenvalue language used here belongs to later, developed mathematical analysis. Germain worked before the modern framework of spectral theory had been assembled. We can use that language to explain the structure of the problem without projecting all of its later concepts backward onto her own proofs.

## A philosopher of mathematical explanation

Germain also wrote about philosophy, science, and the character of intellectual discovery. Her writing reflects a belief that mathematical patterns reveal connections between domains that first appear unrelated. The order of mathematical ideas intrigued her, as did the extent to which discoveries in one science could reshape others. She was not simply interested in solving contest problems. She wanted to understand why certain forms of reasoning could travel from one subject to another.

Her relationships with other scientific readers extended beyond the more famous exchanges with Gauss and Legendre. Letters to Joseph Fourier survive, including correspondence about elasticity in the eighteen twenties. Fourier was someone who had also fought to establish a new mathematical theory of a physical phenomenon, and their exchange belongs to the lively but contentious culture of French applied analysis. Germain also wrote extensively about philosophy and the creative imagination in science. Her nephew Amand-Jacques Lherbette helped preserve and publish aspects of her literary legacy after her death. The record shows a person with broad intellectual interests, family relationships, and a life beyond the two theorems usually associated with her name.

Her experience helps explain that interest. She had studied across what would now be separate disciplines, including arithmetic, geometry, mathematical physics, and philosophical writing. She learned outside a normal sequence of examinations and appointments. That intellectual independence sometimes made it harder to acquire technical tools at the right moment. It also left her free to ask whether an approach in one field suggested a new strategy elsewhere.

At the same time, independence should never be romanticized as a substitute for institutions. When Germain's elasticity submissions were criticized, the criticism often concerned real mathematical difficulties. Formal study and collaborative scrutiny can be productive, not merely restrictive. What was unjust was the way an entire class of students was prevented from obtaining those resources on equal terms.

Germain's own professional circumstances illustrate the cost. Correspondence could yield encouragement but not necessarily the continuous review enjoyed by someone in a research seminar. Her work on Fermat's equation circulated incompletely. Some of her number-theoretic methods were not fully appreciated for nearly two centuries. The historical record is partly a record of ideas and partly a record of which ideas could enter the public conversation of mathematics.

## What her results actually proved

Let's return one last time to p equal to five and the auxiliary prime eleven. We can give a concise, fully reconstructible chain of reasoning for the first step. A number not divisible by eleven has tenth power one modulo eleven. Therefore its fifth power is plus or minus one. If three numbers are all nonzero modulo eleven, two fifth powers cannot add to a third. Any hypothetical fifth-power solution must have a factor of eleven in at least one entry.

That observation is a beginning. Germain's theorem uses further modular arithmetic and the fact that five is not a fifth power modulo eleven to conclude that in any integer solution at least one entry would have to be divisible by twenty-five. The conclusion eliminates the first case, in which five divides none of the entries. To exclude every fifth-power solution, the second case must also be addressed through additional ideas.

Her broader plan was to find auxiliary primes in sufficient abundance to attack more than that one case. She studied conditions on residues, looked for systematic patterns, and developed algorithms in support of the search. Historians who examined the surviving notebooks have shown how much of this work was lost from the simplified story that only the famous prime condition survived.

And the plate problem teaches a parallel lesson. Sand patterns make the mathematics visible. They can suggest an equation and provide tests of it. But a complete account also needs a principled model of bending, physical dimensions, and boundary behavior. Germain's calculations moved that question forward while leaving technical work for others.

## A career measured by more than a prize

Germain died in Paris on June the twenty-seventh, eighteen thirty-one, at the age of fifty-five. In her lifetime she was recognized by major mathematicians, awarded the Academy's prize for elastic-surface research, and able to participate in a profession that had denied her ordinary entry. She did not hold a conventional university appointment or receive the public standing her research might have earned under different conditions.

Her mathematical legacy cannot be summarized by saying she nearly proved Fermat's Last Theorem. That wording would be both too sweeping and too dismissive. She established a powerful first-case theorem, pursued a serious larger program, and left manuscripts that changed the historical assessment of her work. Nor should her elasticity prize be described as the final solution to the dynamics of plates. It was a recognized contribution during the development of a theory that required many further steps.

The connecting thread in her life is the effort to turn an infinite collection of possibilities into something constrained enough to reason about. For Fermat's equation, she searched for primes that force a supposed solution into impossible residue classes. For a vibrating plate, she searched for equations whose permissible motions are the observed standing-wave patterns. In both domains, she asked for a mathematical reason why a vast universe of cases takes the form it does. She found some of those reasons, and she left other questions open for the next generation.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. Reduction to prime exponents

To prove Fermat's Last Theorem for all integers \(n>2\), it suffices to handle \(n=4\) and odd primes \(p\). If \(p\mid n\), then \((x^{n/p})^p+(y^{n/p})^p=(z^{n/p})^p\). If \(4\mid n\), reduce to exponent 4.

### 2. The fifth powers modulo eleven

For \(a\not\equiv0\pmod{11}\), Fermat's little theorem gives \(a^{10}\equiv1\). Thus \((a^5)^2\equiv1\), so \(a^5\equiv\pm1\pmod{11}\), since 11 is prime. The possible fifth powers modulo 11 are exactly \(0,1,-1\); examples include \(2^5\equiv-1\), \(3^5\equiv1\). If \(x,y,z\not\equiv0\pmod{11}\), \(x^5+y^5\in\{-2,0,2\}\) and \(z^5\in\{-1,1\}\); these sets are disjoint modulo 11. Hence a candidate solution forces \(11\mid xyz\). **This step alone does not imply** \(5\mid xyz\).

### 3. Germain's theorem and its hypotheses

Let \(p\ge3\) be an odd prime. If there is a prime \(q\) such that (i) no two **nonzero** \(p\)-th-power residues modulo \(q\) differ by 1, and (ii) \(p\) is not a \(p\)-th-power residue modulo \(q\), then any coprime nonzero integer solution \(x^p+y^p=z^p\) has \(p^2\mid xyz\). In particular, the first case \(p\nmid xyz\) cannot occur. This is the classical Sophie Germain theorem; see the historically informed statement at Agnes Scott and Laubenbacher–Pengelley. For the special prime \(q=2p+1\), nonzero \(p\)-th powers are \(\pm1\), and \(p\not\equiv\pm1\pmod q\) for odd \(p\ge3\). The zero/nonzero restriction in (i) is essential. The proof of the full assertion involves congruence and divisibility arguments beyond the first easy modulo-\(q\) observation.

### 4. Idealized elastic beam and plate models

A modern uniform Euler–Bernoulli beam is modeled by \(\rho A u_{tt}+EI u_{xxxx}=0\). For ideal simply supported ends, eigenmodes \(\sin(n\pi x/L)\) have frequencies \(\omega_n=(n\pi/L)^2\sqrt{EI/(\rho A)}\), hence \(\omega_2/\omega_1=4\). A stretched string with the analogous boundary conditions instead has \(\omega_n\propto n\). A modern isotropic Kirchhoff–Love plate satisfies \(\rho h u_{tt}+D\Delta^2u=0\) in a simplified setting, with physical boundary conditions required for a spectral problem. These are **modern explanatory models**, not equations attributed verbatim to Germain.

### 5. Chronology and attribution

- 1776: born in Paris. 1794: École Polytechnique established; Germain obtains lecture materials and corresponds under the name Le Blanc. 1807: identity disclosed to Gauss and his celebrated reply.
- 1808: Chladni's plate demonstrations in Paris. Academy competitions: submission in 1811, later honorable mention, prize decided in 1816 despite remaining mechanical gaps.
- 1819: letter to Gauss describing continued number-theoretic efforts. 1823: Legendre published her first-case result with attribution.
- 1831: died in Paris. 2010: Laubenbacher and Pengelley study Germain's extensive, largely unpublished Fermat manuscripts and reconstruct her larger strategy.

### 6. Sources and reading

See `metadata/029000.json` and `metadata/sources.json` for institutional biography, original manuscript scholarship, rigorous number-theory references, and the history of the elasticity competition. Distinguish Germain's demonstrated first-case theorem from her incomplete grand plan, and her Academy-recognized elastic-surface work from modern plate equations.

### Historical source notes: human-portrait revision

The additional biographical scenes in the spoken lecture are grounded in the following documentary records. They concern historical context; the mathematical calculations and theorem hypotheses are unchanged.

- `history-fourier-germain-correspondence` — Correspondence of Sophie Germain, including Fourier letters of May and June 1823. https://fr.wikisource.org/wiki/%C5%92uvres_philosophiques_de_Sophie_Germain/Correspondance
- `history-germain-gauss-2012` — Del Centina and Fiocca, The Correspondence between Sophie Germain and Carl Friedrich Gauss (2012). https://www.jstor.org/stable/23319292
- `history-germain-mactutor` — Sophie Germain, MacTutor History of Mathematics. https://mathshistory.st-andrews.ac.uk/Biographies/Germain/

Source claims are indexed by exact spoken anchors in `metadata/029000.json`.
