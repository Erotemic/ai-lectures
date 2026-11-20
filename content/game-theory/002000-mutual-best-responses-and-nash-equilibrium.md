# Mutual Best Responses: Nash Equilibrium Without a Common Objective

<!-- BEGIN SPOKEN LECTURE -->

Two colleagues must decide which software standard to adopt. They will be able to communicate if they choose the same one, and they will waste months building adapters if they choose different ones. Alice prefers Standard A; Bob prefers Standard B. Neither preference is strong enough to make a failed connection worthwhile. Each would rather coordinate on the other's favorite than fail to coordinate at all.

There are two good outcomes, not one. That is the first reason the mathematics is different from zero-sum minimax. The second is that Alice's best choice depends on Bob's choice, while Bob's best choice depends on Alice's. We can no longer maximize a single payoff function and call the answer the solution of the whole game. We need a condition on the choices made together.

A **best response** is an action or probability distribution that maximizes a player's own expected payoff when the other players' strategies are held fixed. A **Nash equilibrium** is a collection of strategies in which every player's strategy is a best response to the others. The definition is deceptively modest. It does not claim that an equilibrium is fair, efficient, easy to compute, or likely to emerge during play. It states something precise about unilateral deviations: no single player can improve their own payoff by changing their own strategy alone.

## Two stable answers to one question

Let Alice and Bob choose between standards A and B simultaneously. Give Alice two payoff units if both choose A and one if both choose B. Give Bob one if both choose A and two if both choose B. If they disagree, give each zero. These four pairs form a normal-form game. Every cell contains two numbers, one for each player. The first number is not automatically the second player's negative. They both gain from coordination, even though they disagree about the preferred convention.

If Alice chooses A and Bob chooses A, neither wants to switch alone. Alice would fall from two to zero and Bob from one to zero. So A with A is a Nash equilibrium. Likewise, B with B is a Nash equilibrium. Alice would fall from one to zero by switching to A while Bob stays at B, and Bob would fall from two to zero by switching to A while Alice stays at B.

The cells A with B and B with A are not equilibria. At either mismatch, someone can switch and gain a positive payoff. A game may therefore have multiple pure equilibria. Predicting exactly which one will be played requires more than the equilibrium definition: conventions, communication, history, or asymmetry in the available information might matter. Game theory gives a set of internally consistent possibilities; it does not magically resolve the selection problem.

Now consider randomized choices. Suppose Alice selects A with probability p and Bob selects A with probability q, and their randomizations are independent. Alice's expected payoff from committing to A is two q. Her payoff from committing to B is one minus q. If q exceeds one third, A is her unique best response. If q falls below one third, B is her unique best response. At exactly one third, she is indifferent and may randomize freely.

Bob has a different indifference equation. His payoff from choosing A is p. His payoff from choosing B is two times one minus p. He is indifferent when p equals two thirds. Thus there is a mixed equilibrium in which Alice uses A with probability two thirds and Bob uses A with probability one third. Each is indifferent between their own pure actions, so neither can gain by altering their own distribution.

This calculation is worth reading carefully. Alice's probability is determined by what makes **Bob** indifferent; Bob's probability is determined by what makes **Alice** indifferent. The numbers may seem backward if one thinks that a player's mixture should be chosen by maximizing that player's payoff against a fixed environment. Equilibrium requires the two optimization problems to fit together. Each player's strategy determines the environment in which the other is indifferent.

At the mixed equilibrium, Alice's expected payoff is two thirds. Bob's is also two thirds. Contrast that with the pure equilibria, where the payoffs are two and one, or one and two. The mixed equilibrium produces disagreement with positive probability and is worse for both players than the average outcome in which an agreed convention is used. It is stable against independent unilateral deviations, but stability is not the same as coordinating efficiently.

## Indifference is conditional, not universal

For a player to put positive probability on two actions at equilibrium, those actions must yield the same maximal expected payoff against the opponents' strategies. Otherwise the player could move a little probability from the worse action to the better one and improve. This is sometimes called the support indifference condition. It is a necessary property of a mixed best response. It does not say that every available action must tie. An unused action may yield less payoff, and the inequalities for unused actions must still be checked.

This yields an algorithm for small games. Guess which actions each player might use with positive probability. Solve the equality equations that make the supported actions equally good. Require the probabilities to be nonnegative and add up to one. Finally check every action left out of the support: none may do better than the supported actions. If you omit this last step, you can produce a mathematically neat but false equilibrium candidate.

For two-by-two games, the procedure often reduces to solving two linear equations. For larger games, the number of possible supports grows, and there can be many equilibria or a continuum of them. This is one reason equilibrium computation is an algorithmic subject in its own right. Existence of a solution does not promise a cheap method to find it.

There is also a simpler class of games with no need to guess supports: those with dominant actions. A player's action is strictly dominant if it gives a higher payoff than every alternative action regardless of what everyone else does. In a prisoner's dilemma, the players can have the following payoffs. If both cooperate, each receives three. If Alice defects while Bob cooperates, Alice receives five and Bob zero. Reverse the roles and the payoffs reverse. If both defect, each receives one.

Defecting gives a better payoff to Alice whether Bob cooperates or defects: five rather than three in the first case, one rather than zero in the second. The same is true for Bob. Thus both defect is the unique Nash equilibrium. But both cooperating would give each three, strictly higher than the equilibrium payoff of one. The game exhibits a failure of individually stable behavior to maximize either joint welfare or both players' payoffs. There is no contradiction. Each player is comparing unilateral deviations with the other player's action held fixed, not imagining an enforceable joint agreement.

It is useful to distinguish this dilemma from the coordination problem. In the coordination problem, multiple equilibria create a selection issue; the players could benefit by communicating which standard to adopt. In the prisoner's dilemma, communication alone does not change the dominance inequalities. Even after agreeing to cooperate, each player still has an incentive to defect if the agreement is nonbinding and the game is played once. Enforceable commitments and repeated interactions change the strategic environment, which will become important later.

## Why mixed equilibria always exist in finite games

The coordination problem had both pure and mixed equilibria. Some games have no pure equilibrium at all. Think of matching pennies: Alice wins when two hidden choices match, Bob wins when they differ. Whichever pure pair is chosen, one player wants to switch. Yet the game has a mixed equilibrium: each randomizes equally. In fact, Nash's existence theorem says that **every finite game** has at least one equilibrium in mixed strategies, even when it is not zero-sum.

It is worth seeing the mathematical structure behind the result. For each player, the set of mixed strategies is a simplex: a closed, bounded, convex set of probability vectors. The full space of mixed-strategy profiles is a product of these simplexes. Expected payoff is a polynomial in the players' probabilities and is linear in any one player's probabilities when the others are held fixed. A best response exists because a continuous function reaches its maximum on the compact simplex.

One route to the theorem uses a fixed-point argument. If each player looks at the opponents' current mixture and selects a best response, we get a best-response **correspondence**, not necessarily a single continuous function: ties can create several equally good responses. The correspondence has nonempty convex values because any mixture of equally good pure responses remains equally good. Its continuity properties and the convex, compact strategy spaces permit an application of a fixed-point theorem, commonly Kakutani's. At a fixed point, each strategy belongs to its player's best-response set, which is exactly Nash equilibrium.

A different proof constructs a continuous map and applies Brouwer's fixed-point theorem. The construction starts from a strategy profile, assigns positive correction weight to pure actions that would improve a player's current payoff, and renormalizes each player's probabilities. A fixed point cannot have a profitable action left over: if any pure action strictly improved the payoff, the renormalization would change the profile. Brouwer then guarantees a fixed point in the finite-dimensional product of simplexes.

Those proofs are not psychological theories. Nobody needs to calculate a fixed point in their head for the existence theorem to hold. Nor does the theorem say that a sequence of selfish best responses will converge to it. Some adjustment processes cycle, some depend on asynchronous timing, and some games have equilibria that are computationally hard to find. The theorem is an existence result about the mathematical model.

We should also separate pure strategies from behavioral rules in sequential games. A strategy there can prescribe what a player would do after every possible history, including histories that never occur under the equilibrium path. In a simultaneous game with one move per player, that extra machinery is unnecessary. But when threats, promises, and information depend on a sequence of choices, a Nash equilibrium may allow off-path prescriptions that are not credible. We will need a refinement to judge those situations.

## Correlation changes the feasible patterns

Return to the coordination game. Suppose a trusted device flips a fair coin and recommends either A to both players or B to both players. Each player receives a recommendation and knows that the other received the same one, but cannot control the device. If Alice is told A, she knows Bob was told A; obeying earns two, while deviating alone earns zero. If told B, obeying earns one, while deviating earns zero. The same reasoning applies to Bob. So neither player wants to disobey a recommendation, conditional on having received it.

This is a correlated equilibrium. The mediator creates a joint distribution over actions that need not factor into independent personal mixtures. Each player may still act autonomously; the crucial condition is that following the recommendation is optimal given what the recommendation reveals. In this example the expected payoffs are one and a half for both, much better than the independent mixed Nash equilibrium's two thirds. The mediator has solved the coordination problem without changing the underlying payoff table.

Correlated equilibrium is mathematically attractive because its incentive conditions are linear inequalities on a joint probability distribution. One can optimize a chosen welfare measure over correlated equilibria by linear programming. This is a separate result from saying every Nash equilibrium is correlated. Every independent Nash distribution induces a correlated equilibrium, but the set of correlated equilibria is generally larger. It accommodates coordination signals that Nash's independent mixing does not.

The contrast reveals something important about solution concepts. A model chooses not only which actions are available but also which information and commitments are available. With the same two payoff matrices, allowing or forbidding a public coordination device changes the strategic possibilities. The phrase 'the game has this solution' is meaningful only once we say what constitutes a strategy, what each player knows, and which deviations our notion of equilibrium tests.

## Equilibrium as a local certificate

Nash equilibrium gives us a compact statement to prove. For every player, and for every possible alternative strategy of that player, holding the other players fixed, the equilibrium strategy yields at least as much expected payoff. In finite games, we can verify this by checking each pure alternative because expected payoff is linear in the player's own mixture. This is an excellent property for formal mathematics: one can describe a game as a finite function, define a predicate expressing unilateral optimality, and separately prove that a particular strategy profile satisfies it.

Yet a certified equilibrium answers only the question encoded by its inequalities. It does not certify Pareto efficiency, social desirability, or robustness to coalitions. Those would require separate definitions and theorems. The coordination game and the prisoner's dilemma are not exceptions that embarrass the concept; they explain its boundary.

We have moved from one shared value in a zero-sum game to a set of mutual best-response conditions in a general game. In both cases probability mixtures turn discrete choices into a convex mathematical domain. But the objective has changed. Minimax proves matching security bounds for opponents whose gains cancel. Nash equilibrium proves consistency of each person's optimization against the others' choices. The next complication is time. If actions are taken in sequence, a threat made today may need to be optimal tomorrow. Stable plans then require us to examine not only the decisions we expect to see, but the decisions that would follow a surprise.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A finite normal-form game has players \(i\in\{1,\ldots,n\}\), pure actions \(A_i\), and payoff functions \(u_i:\prod_j A_j\to\mathbb R\). Mixed strategies \(\sigma_i\in\Delta(A_i)\) produce independent joint distribution \(\prod_i\sigma_i\). A profile \(\sigma^*\) is a Nash equilibrium iff
\[
\forall i\;\forall\tau_i\in\Delta(A_i):\quad U_i(\sigma^*)\ge U_i(\tau_i,\sigma^*_{-i}).
\]
It suffices to check pure \(\tau_i\). Positive-probability support actions must maximize \(U_i(a_i,\sigma_{-i})\).

Coordination example, with Alice rows and Bob columns:

| | Bob A | Bob B |
|:--|:--:|:--:|
| Alice A | (2,1) | (0,0) |
| Alice B | (0,0) | (1,2) |

Pure Nash equilibria: (A,A) and (B,B). Mixed Nash: Alice \(P(A)=2/3\), Bob \(P(A)=1/3\). Indifference: \(2q=1-q\) yields \(q=1/3\), and \(p=2(1-p)\) yields \(p=2/3\). Mixed expected payoffs both \(2/3\). Correlated recommendation choosing (A,A) and (B,B) with probability \(1/2\) each gives both \(3/2\). Conditional deviations yield zero and are unprofitable.

Prisoner's dilemma used in narration:

| | Bob C | Bob D |
|:--|:--:|:--:|
| Alice C | (3,3) | (0,5) |
| Alice D | (5,0) | (1,1) |

(D,D) is the unique pure and mixed Nash equilibrium because D strictly dominates C for both players.

**Exercises and solutions.** (1) Check Alice's expected payoff in the mixed coordination equilibrium. *Solution:* \(P(A,A)=2/9\) pays 2 and \(P(B,B)=2/9\) pays 1, total \(2/3\). (2) Prove every pure Nash equilibrium induces a correlated equilibrium concentrated at that action profile. *Solution:* the recommendation equals the equilibrium action with probability one; unilateral deviation cannot help by the Nash property. (3) Can the support of a mixed best response include a strictly suboptimal action? *Solution:* no; moving positive mass to a better action increases payoff. (4) Does existence imply best-response dynamics converge? *Solution:* no; existence and dynamic convergence are different mathematical claims.

### Sources and reading

- MIT OpenCourseWare, *Economic Applications of Game Theory*, Chapters 3-6, Nash equilibrium: https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2025/resources/lecture-notes/
- Open Yale Courses, Ben Polak, *Game Theory*, Lectures 4-10, pure and mixed Nash equilibrium: https://oyc.yale.edu/economics/econ-159
- MIT OpenCourseWare, *Game Theory with Engineering Applications*, syllabus for correlated equilibria and equilibrium computation: https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/pages/syllabus/

The software-standard coordination game and its numerical payoffs are original examples of standard coordination-game structure.
