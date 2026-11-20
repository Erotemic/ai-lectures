# Credible Threats and the Arithmetic of Repeated Cooperation

<!-- BEGIN SPOKEN LECTURE -->

A new company is deciding whether to enter a market. An established company says that, if entry occurs, it will cut prices so aggressively that the entrant will lose money. The entrant believes the threat and stays out. The incumbent then enjoys the market alone. This story can be a Nash equilibrium of a simple game. It can also be a prediction that disintegrates as soon as we ask what the incumbent would actually prefer after entry happened.

The issue is time. In a simultaneous game, a strategy is an action chosen without observing the other current actions. In a sequential game, a strategy is a complete plan specifying an action at every decision point the player might reach. A plan can contain an instruction for a situation that the plan itself is supposed to prevent. Nash equilibrium checks whether each complete plan is a best response to the others. It does not automatically demand that every off-path instruction would be sensible if that point were reached.

Game theorists use backward induction and subgame-perfect equilibrium to close this gap. The mathematics is a recursion on the game tree: solve the decisions that come last, then move backward, replacing each branch by the payoff rationally anticipated at its endpoint. When we repeat an interaction indefinitely, another aspect of time appears. A future reward or punishment may make behavior that is irrational in a one-shot encounter individually sustainable. We will calculate exactly how patient players must be in a model where that happens.

## The market entry game

There are two players, an entrant and an incumbent. First, the entrant chooses Out or Enter. If it stays Out, the game ends: the entrant receives zero and the incumbent receives three. If it Enters, the incumbent observes that choice and selects Accommodate or Fight. Accommodation gives the entrant two and the incumbent two. Fighting gives the entrant negative one and the incumbent zero. These numbers encode a simple idea. The incumbent likes its monopoly payoff of three best, but if entry has already happened, accommodation is more profitable than a costly price war.

Draw the game as a tree. At the first node the entrant chooses. One branch stops at the pair zero, three. The other branch reaches the incumbent's node. From that node, accommodation leads to two, two; fighting leads to negative one, zero. At each leaf the first number belongs to the entrant, the second to the incumbent. The tree is not a decorative alternative to a payoff table. It records an information fact: the incumbent observes entry before making its choice.

Work backward. After Enter, the incumbent compares its own payoff of two from Accommodate with zero from Fight. It strictly prefers Accommodate. Knowing this, the entrant compares the zero payoff from staying Out with the two payoff it anticipates from Enter. It chooses Enter. The backward-induction outcome is entry followed by accommodation, with payoffs two and two.

But there is another Nash equilibrium of the complete strategic-form representation. The incumbent can announce the plan Fight if entry occurs, and the entrant can choose Out. Given that announced plan, an entrant deviating alone to Enter would earn negative one rather than zero. It therefore has no incentive to deviate. Given that the entrant stays Out, the incumbent earns three whatever it planned to do after Enter. Changing its off-path action from Fight to Accommodate changes nothing that actually happens. So the profile Out with Fight is a Nash equilibrium.

This apparent deterrence relies on a noncredible threat. If entry actually occurred, the incumbent would prefer to abandon the promised fight. A subgame-perfect Nash equilibrium requires that the prescribed strategies constitute a Nash equilibrium in **every** subgame, including subgames off the expected path. The subgame starting at the incumbent's decision has a unique optimal action, Accommodate. Therefore Out with Fight fails subgame perfection, and Enter with Accommodate passes.

A subgame is not just any fragment of a game tree. With imperfect information, a proposed fragment must not cut across an information set that a player cannot distinguish. Our simple market-entry game has perfect information, so the incumbent's decision node forms an ordinary subgame. In games where players move without observing previous actions, we must track information sets and sometimes use stronger refinements than subgame perfection to reason about beliefs at unreached information sets.

## Commitments change the game, not merely the language

One way to make a threat credible is to alter the payoffs or the available actions. Suppose the incumbent has irreversibly bought a technology that makes competition cheap enough that fighting would now yield a payoff of four after entry, while accommodation yields two. If the entrant knows this and the technology genuinely changes the later choice, Fight can become the incumbent's best response after Enter. The first mover's incentives then change. A costly move made earlier can create a strategic benefit by making later behavior predictable.

The word 'irreversibly' carries real mathematical weight. A public statement with no enforcement is not the same as a binding contract, a sunk investment that changes costs, or an automated rule that removes later discretion. We should not model all four with the same game tree and then wonder why the answers differ. A commitment device modifies the available strategies or their consequences. Backward induction reasons about the modified game.

Backward induction also has boundaries. If the game has chance moves, players take expectations at the chance nodes. If a player is uncertain about another's payoff type, it may not know which terminal comparison the opponent will make. If the horizon is infinite, there need not be a last move from which to start. And when information is imperfect, a perfect-information game tree can misrepresent what anyone can condition their decisions on. A mathematical solution must respect the informational structure, not just the chronological one.

## The same dilemma played again

Now suppose Alice and Bob repeatedly face a prisoner's dilemma. In each period they simultaneously choose Cooperate or Defect. The payoffs are three each when both cooperate; five for the sole defector and zero for the cooperator when only one defects; and one each when both defect. In a one-shot encounter, Defect strictly dominates Cooperate for both players, so the unique Nash equilibrium is mutual defection.

If the same game is played for a known finite number of rounds and each round's actions are observed, and these stage-game payoffs remain the same, then the unique equilibrium path under subgame-perfect backward induction is mutual defection every round. To see why, look at the final round. With no future consequences, both defect. At the previous round, the future final round is already fixed regardless of today's cooperation or defection, so both again defect. The argument proceeds backward through every round.

This conclusion depends on the assumptions. It is not a claim that real people never cooperate in short repeated encounters. Changes in incomplete information, social preferences, uncertainty about the ending, linked interactions, or other punishments can change the game. The mathematical statement is that a known finite repetition of this particular complete-information stage game, with a unique stage Nash outcome, has mutual defection along every subgame-perfect equilibrium path under the standard additive payoff model.

An indefinitely repeated game is different because there is no known final period. Suppose each player discounts next period's payoff by a factor delta, between zero and one. A payoff received one period later counts delta times as much as a payoff now; two periods later counts delta squared. Rather than dividing by one minus delta at every step, we can think of a current payoff followed by a discounted continuation value.

Consider the following rule, called grim trigger. Start by cooperating. Continue cooperating as long as both players have cooperated in every previous round. If anyone defects, defect in every later round. The rule is harsh and depends on perfectly observing past actions, but its simplicity makes a useful test case.

While cooperation lasts, a player receives three every period. Its discounted value is three plus three delta plus three delta squared and so on. For delta below one, the geometric series sums to three divided by one minus delta. If instead the player defects once while the other cooperates, it receives five now. From the next period onward, the trigger rule produces mutual defection, worth one every period. So the deviator's value is five plus delta times one divided by one minus delta.

Cooperation is incentive-compatible precisely when the first value is at least the second. Multiply both sides by one minus delta, which is positive. We obtain three at least five minus four delta. Rearranging, four delta at least two. Therefore delta must be at least one half.

That threshold is an actual mathematical prediction of this model. At delta equals one quarter, future losses are too heavily discounted; the immediate temptation to collect five wins. At delta equals three quarters, the long stream of future cooperation is valuable enough to make keeping the agreement privately optimal. The model does not assume goodwill. It shows how future consequences can change a best-response comparison.

We must also check that the threatened punishment is credible. Once a defection has occurred, the prescribed future behavior is mutual defection. That is a stage-game Nash equilibrium: a player facing Defect gets one from Defect and zero from Cooperate. No player wishes to leave the punishment phase by cooperating unilaterally. Under perfect observation, public strategies, and the infinite discounted model, grim trigger is therefore subgame perfect whenever delta is at least one half. We verified behavior both on the cooperative path and in the punishment continuation.

## One deviation at a time

There are infinitely many possible complete plans in a repeated game. Why can we analyze only a player's immediate decision to defect, rather than all exotic plans involving many future switches? Under standard conditions for discounted repeated games with finite action sets and perfect recall, a one-shot deviation principle says a strategy profile is subgame perfect if and only if no player can profit by deviating at a single information set and then returning to the prescribed strategy. Discounting makes sufficiently distant consequences small, allowing a profitable complex deviation to be reduced to an earliest profitable one-shot deviation.

This principle is a theorem with assumptions, not a universal trick. It requires suitable continuity and informational structure. In our grim-trigger example it helps because a single defection is the strategically decisive event. After cooperation has broken, a one-time attempt to cooperate during punishment is unprofitable, and after cooperation has not broken, a one-time defection is unprofitable if delta passes the threshold. These checks establish the equilibrium property for the complete continuation strategies.

The same arithmetic can be generalized. Write R for the payoff from mutual cooperation, T for the temptation payoff from unilateral defection, and P for the payoff under mutual punishment, with T greater than R greater than P. Cooperation has value R divided by one minus delta. Defection followed by permanent punishment has value T plus delta P divided by one minus delta. The no-deviation condition becomes delta at least the ratio of T minus R to T minus P. For our example it is two divided by four, or one half. The formula also shows why a more severe credible punishment can support cooperation with less patience.

There is a profound practical limitation. In an environment where actions are noisy or hard to observe, the grim-trigger rule can misinterpret an accident as betrayal and lock the players into unnecessary punishment. If players only observe an imperfect public signal, the equilibrium analysis must include that signal's distribution. More forgiving strategies, reputation models, and belief updates become relevant. A threat can be credible yet inefficient; a punishment rule can satisfy mathematical incentives and still be a poor institution.

## The shape of an incentive argument

The market-entry game and the repeated prisoner's dilemma use the same logical tool. At each decision point, compare the reward for obeying a proposed strategy with the reward for a deviation, given the continuation that would follow. In the entry game the incumbent's threat fails that test after entry. In the repeated game the punishment phase passes it, and the cooperation phase passes it only when the discount factor is high enough.

This is also a useful template for mathematical formalization. Define a game state or history, define which actions are available and what each player observes, define a continuation value, and state a predicate saying no unilateral change improves that value. A proof must quantify over off-path histories when the equilibrium concept requires it. If the algorithm computing a strategy uses backward induction, an inductive invariant can assert that each solved subtree returns an optimal continuation for the player who moves at its root. When the horizon is infinite, a fixed-point or dynamic-programming argument replaces finite recursion.

The broader insight is that the future is part of a strategic action's payoff. A promise and a threat are not stable because they sound forceful. They are stable, if at all, because following them will remain optimal when the time comes. A long relationship is not automatically cooperative. It can be cooperative because future consequences create inequalities that differ from those in a single encounter. The logic is exact, and the assumptions deserve to be equally exact.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Market-entry tree.** Entrant chooses Out or Enter. Out gives \((0,3)\). Enter leads to incumbent Accommodate \((2,2)\) or Fight \((-1,0)\). Strategic-form Nash equilibria include \((\mathrm{Out},\mathrm{Fight})\) and \((\mathrm{Enter},\mathrm{Accommodate})\), but only the latter is subgame perfect. Backward induction: choose Accommodate at the incumbent's node since \(2>0\), then Enter at the entrant's node since \(2>0\).

**Repeated prisoner dilemma.** Payoffs \((C,C)=(3,3)\), \((D,C)=(5,0)\), \((C,D)=(0,5)\), \((D,D)=(1,1)\). With infinite horizon, perfect public monitoring, geometric discount \(\delta\in[0,1)\), and grim-trigger strategies:
\[
V_C=\sum_{t=0}^{\infty}3\delta^t=\frac{3}{1-\delta},\qquad
V_D=5+\sum_{t=1}^{\infty}\delta^t=5+\frac{\delta}{1-\delta}.
\]
Condition \(V_C\ge V_D\) is \(\delta\ge1/2\). More generally \(\delta\ge(T-R)/(T-P)\) for temptation \(T>R>P\) when the punishment is permanent and credible.

**Exercises and solutions.** (1) If the incumbent's payoff from Fight after entry rises to four, what is the backward-induction outcome? *Solution:* Fight is optimal after entry, so the entrant stays Out, with payoffs \((0,3)\). (2) If the cooperation payoff rises from three to four, keeping temptation five and punishment one, find the threshold. *Solution:* \((5-4)/(5-1)=1/4\). (3) Why does grim trigger's punishment remain credible? *Solution:* after the trigger, the profile is perpetual (D,D), and D is a best response to D in every period. (4) If the game lasts exactly two periods and has a unique stage Nash of mutual defection, explain the first-period outcome. *Solution:* the second period is mutual defection in every subgame; this fixed continuation leaves the first period strategically identical to the one-shot game, so both defect.

### Sources and reading

- MIT OpenCourseWare, *Economic Applications of Game Theory*, Chapters 9, 11, and 12 (Fall 2025): https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2025/resources/lecture-notes/
- Open Yale Courses, Ben Polak, *Game Theory*, Lectures 13-22 on backward induction and repeated games: https://oyc.yale.edu/economics/econ-159
- MIT OpenCourseWare, *Game Theory with Engineering Applications*, syllabus topics on extensive games, repeated games, and trigger strategies: https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/pages/syllabus/

The entry payoffs and the discount-threshold example are independently specified teaching models.
