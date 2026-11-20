# When Randomness Becomes a Strategy: Matrix Games and Minimax

<!-- BEGIN SPOKEN LECTURE -->

Imagine that Alice has to choose a route for a valuable message, and Bob has to choose which route to inspect. There are two routes, and both players know the rules. Alice wins if Bob inspects the wrong route; Bob wins if he finds the message. Alice can choose a route with perfect care and still fail, because Bob is not an obstacle with a fixed response. He is another decision maker, choosing at the same time. The best action depends on what he thinks Alice will do. And what he thinks depends on what he believes she thinks he will do.

This is a small instance of a strategic problem. In ordinary optimization, we may pick a variable to maximize a function whose other inputs are given. In a game, several people choose inputs, and each person's payoff depends on the whole collection of choices. A choice may be excellent against one opponent action and disastrous against another. The mathematical object is not just a set of actions. It is a family of payoff functions indexed by the participants.

A finite, simultaneous-move game specifies its players, an action set for each player, and a real-valued payoff for each possible joint action. The payoff numbers can represent money, utility, success, or whatever the model says the player values. Calling them payoffs does not make their measurement objectively correct. We must decide which differences in outcomes the numbers are intended to preserve. In the simplest model, each player prefers a larger own payoff, knows the payoff table, and chooses without observing the other's current move.

We will begin with two players whose interests are exactly opposed. Alice's payoff is Bob's loss. This is a zero-sum game. Such games have a remarkable theorem: even though each player is responding to an intelligent opponent, they can both choose randomized strategies that guarantee a common value. We will derive that value in a concrete example and see why the theorem is an instance of linear-programming duality.

## A table is a function of two choices

Let Alice choose a row and Bob a column. For each row-column pair, write Alice's payoff in a table. Bob's payoff is the negative of the same number. Suppose Alice has two rows, Top and Bottom. Bob has two columns, Left and Right. The four payoffs for Alice are these. Top against Left earns two. Top against Right loses one. Bottom against Left loses two. Bottom against Right earns three.

Before we permit randomization, try to select Alice's best pure action. If she chooses Top, Bob can respond with Right and hold her to negative one. If she chooses Bottom, Bob can respond with Left and hold her to negative two. If Alice expects Bob to pick the worst possible column for her, Top gives the better security guarantee: negative one.

Bob can do his own conservative calculation. If he chooses Left, Alice can earn at most two. If he chooses Right, Alice can earn at most three. So Bob chooses Left to keep her payoff at most two. We have two very different numbers: Alice can guarantee negative one; Bob can guarantee that Alice gets at most two. In between there is room for one player to exploit the other's predictable choice. No pure pair in this example has the property that neither party would want to deviate.

Now suppose Alice flips a private biased coin. She uses Top with probability p and Bottom with probability one minus p. Against Bob's Left, her expected payoff is two p minus two times one minus p. Simplifying, that is four p minus two. Against Right, it is negative p plus three times one minus p, or three minus four p.

Bob need not be indifferent to these two expressions. As Alice, however, we should care about the smaller one, since Bob can select the column that hurts us most. As p increases from zero, the first expression rises from negative two, while the second falls from three. The minimum of the two is highest where they meet. Set four p minus two equal to three minus four p. Eight p equals five. Thus p equals five eighths, and both columns give Alice an expected payoff of one half.

This is already striking. Neither pure row guarantees even zero, yet a carefully randomized row choice guarantees a positive one half. The numbers are not an artifact of Alice literally needing a coin. They describe what follows when Bob cannot predict which row will be chosen. Bob may know the probability distribution. What he must not know, in this simultaneous-move model, is the realization before committing to his column.

Bob should randomize too. Let q be his probability of choosing Left. Alice's expected payoff from Top becomes two q minus one times one minus q, which is three q minus one. Her payoff from Bottom is negative two q plus three times one minus q, which is three minus five q. Bob wants to minimize Alice's best available payoff, so he equalizes the rows. Three q minus one equals three minus five q. Thus q equals one half. Each row then yields one half.

Put these policies together. Alice plays Top with probability five eighths. Bob plays Left with probability one half. The expected payoff is one half. If Alice changes her mixture while Bob keeps his, her payoff cannot increase: both pure rows give one half, so any mixture gives one half. If Bob changes his mixture while Alice keeps hers, he cannot make Alice receive less than one half: both pure columns give one half. This pair is stable against unilateral changes. It is also a certificate. Alice proves the value is at least one half; Bob proves it is at most one half.

## Two inequalities meet

In any finite matrix game, Alice can ask: what is the largest payoff I can guarantee against every column strategy? Bob can ask: what is the smallest upper bound I can impose against every row strategy? The first is the maximin value. The second is the minimax value. Alice's guarantee can never exceed Bob's upper bound. This elementary direction, sometimes called the weak minimax inequality, needs no deep theorem. If Alice promises at least three and Bob promises at most two, both promises cannot hold for their joint play. One or both calculations must be wrong.

The extraordinary statement is equality. Von Neumann's minimax theorem says that for every finite two-person zero-sum game, allowing probability mixtures gives an optimal pair and makes these two numbers equal. Notice both qualifications. The theorem applies to finite action sets here, and it depends on the opposed-payoff structure. There is no corresponding assertion that arbitrary multi-person games all possess a single security value. Nash equilibrium will provide a different notion for general games, but it will not assign every player a mutually agreed numerical target.

To understand why minimax is true, we can translate Alice's problem into a linear program. Name her probability on each row and introduce a proposed guarantee v. Her probabilities must be nonnegative and sum to one. For each possible column, her expected payoff against that column must be at least v. She wants to maximize v. Every constraint is linear. Because expected payoff against a mixture of Bob's columns is an average of payoffs against individual columns, it suffices to impose the guarantee for each pure column.

Bob's problem is another linear program. His probabilities on the columns are nonnegative and sum to one. For each pure row Alice might play, Bob requires Alice's expected payoff to be at most a proposed upper bound w. He wants to minimize w. Again, these are linear constraints, and checking pure rows is sufficient because Alice's mixtures are convex combinations of them.

Let us make the certificate concrete. If Alice has probabilities p and one minus p, her constraints for our matrix are four p minus two at least v, and three minus four p at least v. At p equals five eighths, both inequalities are tight at one half. Bob's constraints are three q minus one at most w and three minus five q at most w. At q equals one half, both are tight at one half. The equality of lower and upper certificates proves optimality without appealing to the players' psychological sophistication.

This pattern is related to a general result in linear programming. The row player's maximization problem and the column player's minimization problem form a primal-dual pair, after accounting for the probability-sum constraints and the unrestricted value variables. Weak duality always says the maximized guarantee is no larger than the minimized ceiling. Strong duality, under the standard feasibility and boundedness conditions satisfied by these finite games, says their optimal values agree. That yields the minimax theorem. We have not proved strong duality from scratch, but we have exposed the exact place where a theorem from optimization enters the reasoning.

This connection also tells us how to compute equilibria for large matrix games. Instead of searching a space of probabilities by guessing which actions should have positive mass, we can solve a linear program. The primal gives an optimal random policy; the dual gives an opponent policy and a bound certifying its value. For exact rational payoff matrices, exact rational optimal solutions exist. Floating-point software may report approximations, so numerical tolerances enter if we want a machine-checkable certificate.

## Why some actions vanish

There is a related idea called dominance. Suppose one of Alice's rows gives a strictly lower payoff against every column than another row. Then the worse row should not appear in an optimal mixture: moving its probability to the better row improves Alice's expectation regardless of Bob's choice. In general-sum games, the same comparison is made using a player's own payoff against each fixed profile of opponents' actions. Strict dominance can simplify a game, but absence of dominance does not settle its equilibrium.

The equal-payoff calculation also has a useful qualification. At an optimum, actions used with positive probability must be best responses to the other player's mixture. Actions outside the support can be worse, sometimes strictly worse. For our two-by-two matrix both rows and both columns receive positive probability and become indifferent. In larger games, it is a mistake to equalize every row and column blindly; only supported actions must tie at the optimum. An unused row may have a lower expected payoff against Bob's strategy. An unused column may have a higher expected payoff against Alice's.

Consider one simple extreme. If Alice has a row earning four against every Bob column, and every other row can do no better than four, that pure row already guarantees four. Adding randomness is unnecessary. The minimax theorem permits pure optimal strategies as degenerate probability distributions. It does not command everyone to randomize. It says a strategy exists in the simplex of all probability distributions, including points that assign probability one to a single action.

We should distinguish a randomized policy from uncertainty about what someone else will do. Alice chooses a mixed strategy when she deliberately selects a distribution over her own pure actions. She has a belief about Bob's choice when she models Bob with a probability distribution. In equilibrium these distributions may coincide with the players' actual mixed strategies, but the concepts are different. A security strategy is attractive because it does not require the belief to be right: it protects Alice against every opposing strategy within the modeled game.

## What zero-sum leaves out

Our two-route contest was built on perfect conflict. In many strategic situations, Alice and Bob could both gain from coordination or both lose from a bad outcome. Their payoffs then cannot be represented by one matrix with opposite signs. Imagine two software services choosing incompatible communication protocols. If they choose the same one, both benefit; if they choose different ones, both suffer. There are two ways to coordinate, and the players may value them differently. The question is no longer simply how to defend against the worst opponent. It is which pair of choices each person can reasonably expect the other to maintain.

That is the territory of Nash equilibrium. It starts with a condition we already encountered in our minimax solution: no player wants to switch their own strategy while the others hold theirs fixed. In a general game, that condition can have several solutions or none among pure strategies. Mixed strategies can restore existence for finite games, but an equilibrium can be inefficient or fragile as a prediction. We should not mistake a formal stability property for a statement that people have found the ethically right outcome or that learning dynamics necessarily reach it.

The mathematical lesson of minimax is broader than adversarial games. A collection of local payoff inequalities can give a global certificate. Convex mixtures convert an apparently circular strategic problem into optimization over probability simplices. The lower guarantee and upper bound are not competing opinions. They are two halves of a proof. If they meet, the value is settled. We will reuse this way of thinking when studying equilibrium, mechanism design, and the verification of strategic algorithms.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a finite zero-sum matrix game with Alice's payoff matrix \(A\in\mathbb R^{m\times n}\), mixed strategies \(p\in\Delta_m\) and \(q\in\Delta_n\) give \(U(p,q)=p^TAq\). The minimax theorem states
\[
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^TAq
=\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^TAq.
\]
Alice's primal maximizes \(v\) subject to \(A^Tp\ge v\mathbf 1\), \(\mathbf1^Tp=1\), \(p\ge0\). Bob's dual minimizes \(w\) subject to \(Aq\le w\mathbf1\), \(\mathbf1^Tq=1\), \(q\ge0\). Strong LP duality gives equality; weak duality follows from \(v\le p^TAq\le w\) for any feasible pair.

Worked example:
\[
A=\begin{pmatrix}2&-1\\-2&3\end{pmatrix},\quad
p^*=(5/8,3/8),\quad q^*=(1/2,1/2),\quad v^*=1/2.
\]
For \(p=(p,1-p)\), the column payoffs are \(4p-2\) and \(3-4p\). For \(q=(q,1-q)\), the row payoffs are \(3q-1\) and \(3-5q\). Each is equal to \(1/2\) at the listed strategies. Both are feasible security certificates, so no other mixture can improve either side's objective.

**Exercises and solutions.** (1) For matching pennies with matrix \(\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\), find the value and strategies. *Solution:* both players choose either action with probability \(1/2\), value zero. (2) Explain why the primal constraints need only consider Bob's pure columns. *Solution:* a mixture is a convex combination of their expected payoffs; if every column payoff is at least \(v\), any mixture is too. (3) If a row is strictly dominated by another row, show it receives zero probability in any optimal mixed strategy whenever an improvement is possible at the current guarantee. *Solution:* moving its mass to the dominating row raises the payoff against every column; hence a positive mass cannot maximize the minimum. (4) State the theorem's scope. *Solution:* finite action sets, two players, zero-sum payoffs, independent mixed strategies.

### Sources and reading

- MIT OpenCourseWare, *Economic Applications of Game Theory*, Chapter 6 and Lecture 7 (Fall 2025): https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2025/resources/lecture-notes/
- Tomas Kroupa, *Computational Game Theory*, Chapter 4, minimax and linear programming: https://tomaskroupa.github.io/quarto-game-theory-course/lectures/04-two-player-zero-sum-games.html
- MIT OpenCourseWare, Gilbert Strang, *Matrix Methods*, Lecture 24, linear programming and two-person games: https://www.ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-24-linear-programming-and-two-person-games/

The routing contest and asymmetric matrix are independent teaching examples.
