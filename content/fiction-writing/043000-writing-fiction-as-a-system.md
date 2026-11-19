# 043000 - Writing Fiction as a System: Interactive and Computational Authorship

**Track:** Fiction Writing and Worldbuilding. **Unit:** Forms, Workshops, History, and Systems. **Audience:** Writers designing narrative choices, simulations, and computational story tools. **Prerequisites:** None; no programming experience assumed. **Method:** Design a small invented floodgate story as both branching fiction and a stateful simulated world.

<!-- BEGIN SPOKEN LECTURE -->

# Writing Fiction as a System: Interactive and Computational Authorship

A town has an old floodgate. During a storm, the person on duty can open it to divert water into a public meadow, risking the homes beside the meadow, or keep it closed, risking the shops along the river. A council engineer has warned that the gate mechanism may jam. The worker has twelve minutes before the level reaches the top of the retaining wall.

In an ordinary short story, we can choose whose perspective to enter and which action they take. The reader experiences the consequence of a decision the author has arranged. In an interactive story, the reader might be asked to choose whether to open the gate. That sounds like a minor alteration, but it changes the work's basic contract. The author can no longer count on one sequence of events. What happens when the reader asks to check the gauge again? Can the worker phone the meadow residents? What if a reader makes the same choice after discovering evidence the first version of the scene concealed?

A computational narrative gives some of its formal responsibility to a system: a set of rules that determines what can happen, what the text remembers, and how new passages are selected. This does not remove authorship. It moves authorship partly into the design of possibilities and constraints. A writer still chooses what matters, which actions are imaginable, what the system can represent, and where its limits will be visible.

The history of this work includes parser-based interactive fiction, branching hypertext, game dialogue systems, procedural storytelling, and experiments in text generation. These traditions overlap but should not be treated as interchangeable. A linked website with choices, a text adventure with a world model, and a generative character simulator make different promises about agency and explanation.

## Two ways of asking the reader to act

First write a simple branching version of the floodgate scene. The opening offers two choices: open the gate or keep it closed. Opening it sends water toward the meadow. Keeping it closed protects the meadow but increases the river's level in the commercial district. Each option leads to an ending describing a different consequence.

This is a small choice-based story. Its structure resembles a map of passages connected by decisions. The reader chooses a path among text segments prepared by the author. A good choice can expose competing values. But the mere presence of two buttons does not make the story morally complex. If the author writes 'Open the gate: save everyone' and 'Keep it closed: everyone dies,' the reader has been given a quiz with one obvious answer. Agency is meaningful when the options involve differences the reader can understand, and when later text takes the choice seriously.

Now write a parser-based version. The player reads: 'You are in the floodgate control room. A gauge is mounted beside the door. A telephone sits on the desk. A key hangs from the wall.' They can type actions such as looking at the gauge, taking the key, calling the council office, or opening the door. The story must understand some collection of possible actions and respond to them coherently. Its author is building a small model of a world, not simply linking two pages.

In *Twisty Little Passages*, published in 2003, Nick Montfort placed interactive fiction in a history that includes riddles, *Adventure*, *Zork*, commercial text games, and independent experiments. The book helped articulate interactive fiction as a literary form as well as a game form. Its history is a reminder that reader action is not one technology invented by contemporary websites. Questions of navigation, interpretation, and simulated worlds have been central to the medium for decades.

For a writer, the difference between the two designs is practical. In a branching story, you can know in advance that the reader sees the gauge in passage four. In a world-model story, the reader may examine the gauge first, last, repeatedly, or not at all. The author must decide how the narrative responds to all those possibilities, including actions that make no sense at the current time. A simulation can support curiosity beyond an explicit menu, but it also introduces many opportunities for incoherence.

## Twine and Inform: different authoring grammars

Twine is an open-source tool for creating nonlinear, choice-based stories. It can produce simple linked passages without programming, and it can also use variables and conditional rules to track what has happened. It publishes work as HTML. Writers have used it for many purposes, from personal narrative to experimental fiction and games. A tool's affordances do not dictate one aesthetic, but they change how easily certain structures can be authored and revised.

Inform 7, developed under Graham Nelson's direction, represents a different approach. Its authoring language uses English-like rules to describe places, objects, actions, and conditions. It supports parser interaction and simulated world behavior. Its documentation includes extensive examples of the sorts of rules a story needs to represent ordinary objects, actions, and relations. Inform 7 became publicly available in 2006, after years of development; that date marks the release of a particular system, not the origin of interactive fiction.

We can build the floodgate story in either way. In Twine, a passage might ask whether to inspect the gauge. If the reader does, the system records that they know the warning threshold. Later the choice to open the gate can present different text depending on that knowledge. In Inform, the gauge can be an object in the room, with a value that changes as the storm progresses; opening the gate can be an action allowed only when the player has a key or has found another method of releasing the mechanism.

The design question is not whether variables or objects are technologically impressive. It is what a reader is being invited to understand. If checking the gauge changes only a decorative sentence, the choice may feel inconsequential. If checking it supplies evidence that changes the reader's moral interpretation, then the program is part of the storytelling. The system controls access to knowledge, and knowledge changes responsibility.

## State is the memory of the story

Suppose we record three facts about our floodgate story: whether the player has inspected the gauge, whether the meadow residents have been warned, and whether the gate is open. At every moment, the text should be consistent with those facts. If the player has already opened the gate, a later passage should not ask them to open it for the first time. If the player called the meadow, a character might thank them or accuse them of exaggerating the danger. If the reader never examined the gauge, the narrator should not suddenly assert that they know the water crossed the red line.

This sounds like ordinary continuity editing, and in one sense it is. In a fixed novel, continuity can be checked along one arranged sequence. In interactive fiction, it must be checked along many possible sequences. As a story grows, combinations multiply: opened or closed, warned or unwarned, inspected or not inspected. Add a broken telephone, a deputy engineer who may be present, and a gate that may jam, and the writer has created many states that need some meaningful response.

The temptation is to add a different ending for every combination. That can make the project impossible to maintain. A more useful design often has a smaller set of consequential states and many details that modify how the reader experiences them. Whether the meadow has been warned might matter at the ending. Whether the character looked at a painting in the control room might enrich the prose without requiring a separate final chapter. Distinguish dramatic state from incidental memory.

Another strategy is to make several paths converge on a shared scene without pretending that earlier choices never happened. The storm reaches the critical level no matter which room the player visited. But the confrontation with the engineer changes because the player may have inspected a maintenance notice, warned residents, or delayed action. Convergence controls scope; recognition preserves agency. The writer's task is to decide which consequences the shared scene must carry.

## Systems produce a different kind of characterization

In fixed prose, character often emerges through a sequence of selected actions. In a simulated story, some behavior results from rules. The engineer may refuse to operate the gate while anyone is standing on the maintenance platform. That refusal is not simply a branch of dialogue. It is a consistent constraint. The player may learn to predict it, resent it, test it, and eventually understand its rationale. Character is partly constructed by how the system responds across situations.

This makes system design an ethical and aesthetic act. If the engineer always obeys an order from the player regardless of danger, the simulation may imply a kind of authority the fictional world has not justified. If residents always evacuate immediately after one phone call, the system erases their jobs, disabilities, distrust, and other constraints. A rule can smuggle a simplification into every scene more efficiently than a single paragraph can.

We can revise the floodgate model. Warned residents do not always leave. Some have transport; others do not. Opening the gate does not instantly cause one predictable level of damage; the meadow has different elevations. The game's representation remains selective: no finite model can account for the entirety of a town. The point is not to simulate everything, but to know what assumptions have been made and how those assumptions affect the story's moral world.

At this stage a useful distinction appears between *agency* and *control*. A reader may have agency because their choice expresses a stance and changes the narrative, even if they cannot guarantee the outcome. In fact, promising total control over consequences can undermine a story whose subject is uncertainty. The player might choose to warn the meadow, but not decide whether every resident believes the warning. A system that respects agency can still resist the player's intentions, as a good fictional world resists the intentions of its characters.

## Procedural writing and generated language

Computational fiction need not ask a player to choose at all. A program may arrange fragments according to rules, select from a vocabulary, generate scenes, or simulate characters' competing goals. Such works raise a different question: what is written by the author, and what is determined at runtime?

Suppose the floodgate story includes a bulletin board that produces a report after each turn. The author writes a set of possible statements: 'The water has reached the second mark,' 'A call from the meadow has gone unanswered,' or 'The southern road is closed.' The program selects statements consistent with the current state. This is procedural text generation, but not free improvisation. The system composes a report from authored parts according to explicit rules. It can produce variety while preserving a verifiable relationship to the fictional world.

Now replace that template with a language model asked to generate the bulletin. The prose may become varied and fluent, but we must still decide which facts it is allowed to assert. Without constraints, it may invent a new emergency route or claim the gate has opened when its state remains closed. The problem is not that generated prose is inherently invalid as fiction. It is that surface plausibility is not the same as consistency with a shared world.

A workable design separates the authoritative state of the story from the language that presents it. The system records what is true. The prose generator receives the facts it may describe. After generation, the authoring process checks for contradictions and keeps stable identities, chronology, and consequences. Human writers still need to judge voice, rhythm, surprise, and meaning. A technically valid branch can be dull; a beautifully written branch can still break the story if it grants the protagonist knowledge they did not acquire.

There is also a literary opportunity. A machine-written public report can differ sharply from a character's private testimony. The official bulletin may be syntactically tidy while concealing uncertainty. A resident's message can be fragmented and emotionally precise. The contrast becomes part of the narrative, not a demonstration of how much text the system can produce.

## A small specification before you author prose

For our example, write the reader's governing situation in a sentence: 'During a storm, a worker must decide whether and when to operate a gate that redistributes danger across a town.' Then define what the story knows: storm level, gate position, whether the gauge was inspected, whether a warning was sent, and whether the engineer is available. Define which actions can change those facts. Define which facts must never be contradicted by later scenes.

Next choose the reader's central uncertainty. Is the question which district should bear risk? Is it whether the engineer's warnings can be trusted? Is it how quickly public information becomes action? These lead to different mechanics. If the story is about trust, evidence-gathering and conflicting testimony should matter. If it is about tradeoffs, the different costs of operating the gate should be legible. If it is about institutional delay, the timing of communication may matter more than the player's willingness to be heroic.

You can now draft a short interactive sequence: an opening state, three actions, one important state change, and two endings. Play it deliberately in the wrong order. Try to operate a gate after it has already opened. Try to warn a district when the telephone is broken. Try to make a character thank you for a warning you never sent. If the narrative contradicts itself, you have discovered a design problem, not a need to write more exposition.

You should also test for false choices. If all routes lead to identical outcomes, ask whether the act of choosing still has interpretive meaning. A story may deliberately reveal the limits of an individual's power, but then it should be clear that this is the point. Otherwise the reader may experience the choice as decoration. On the other hand, if every action produces an entirely separate story, the project may lack a stable thematic center. A bounded system can have meaningful variation without needing infinite possible outcomes.

## The author's responsibility has moved, not vanished

A writer designing an interactive story works at several levels at once. There is the quality of each sentence. There is the sequence in which readers learn facts. There is the set of choices offered. There are rules that determine consequences. And there is the larger interpretation created by the options the system makes possible or impossible.

Consider a final version of the floodgate scene. The storm reaches the red line. The engineer is on the telephone, describing the risk to the meadow. The player knows the road there is partly closed because they checked a map. They have warned some residents but could not reach others. They can open the gate now, wait for more information, or close access to the control room while calling for assistance. None of these actions is framed as a correct button. Each expresses what the player has learned to value, and each leads to consequences consistent with the world's rules.

In a noninteractive novel, we might end by showing one worker's decision. Here the authored story is the larger structure that makes several decisions imaginable and several consequences accountable. The author has not disappeared behind the reader's freedom. The author has chosen the world in which that freedom means something.

Interactive and computational writing expands the craft of fiction by turning sequence, knowledge, and causality into things an author can formally specify. But the fundamental question is still literary: what experience does this arrangement make possible for a reader? The best system is not the one that generates the most branches. It is the one whose rules make the story's central human questions more difficult, more intelligible, and more alive.

<!-- END SPOKEN LECTURE -->

## Companion (display only)

**Historical boundary:** Montfort's *Twisty Little Passages* appeared in 2003. Inform 7 was released publicly in 2006; its documentation describes a rule- and world-model approach. Twine's official website describes an open-source nonlinear storytelling tool that publishes HTML and can use variables and conditions. The floodgate story and authoring model are original teaching examples, not examples drawn from those books or tools. The discussion of language models is an analysis of a possible authoring workflow, not a claim that generated fiction is necessarily accurate or coherent.

**Practice:** Specify a stateful story with five authoritative facts, three actions, two endings, and at least one convergent scene whose text changes according to earlier choices. Test contradictory action orders. Compare the experience with a linear scene using the same moral situation.

**Further reading:** [Nick Montfort, *Twisty Little Passages* (MIT Press, 2003)](https://mitpress.mit.edu/9780262134361/twisty-little-passages/); [Twine official website](https://twinery.org/); [Inform 7 documentation](https://ganelson.github.io/inform-website/doc/); [Nick Montfort, 'Announcing Inform 7' (2006)](https://grandtextauto.soe.ucsc.edu/2006/04/30/announcing-inform-7/).

**Orientation link:** [Wikipedia: Interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction). This overview is background reading; the cited primary and scholarly sources carry the historical claims.
