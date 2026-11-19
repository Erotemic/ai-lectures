# The Upgrade Nobody Can Install Alone

<!-- BEGIN SPOKEN LECTURE -->

At four fifty in the morning, on the third of September, nineteen sixty-seven, the vehicles allowed onto Swedish roads were ordered to stop.

The drivers had been using the left side of the road. Now they were told to move carefully across to the right and wait. At five o'clock, permitted traffic could proceed on the new side. Most other drivers had to wait until six. Road signs had been changed. Signals and intersections had been prepared. Newspapers, radio programs, and an elaborate public campaign had spent years explaining what was about to happen.

Sweden was switching from driving on the left to driving on the right.

I like this story partly because it is difficult to imagine a more literal example of a social convention. There is no physical law requiring a car to travel on the right side of a road. In other countries, the left side works perfectly well. What matters is that the people using a particular road follow a common rule. You can be an excellent driver, with an excellent car, and be catastrophically wrong if you follow a different rule from everyone around you.

Sweden had already wrestled with the decision for decades. In a nineteen fifty-five referendum, a large majority voted against changing sides. The parliament approved the change in nineteen sixty-three anyway, with an implementation date four years later. Those facts complicate any tidy story of universal agreement. The transition was a substantial public undertaking, not the spontaneous consequence of everyone deciding simultaneously that the right side seemed nicer.

Yet the mechanics of the change were almost comically simple. Stop. Move over. Start again.

Of course, that simplicity was manufactured. Thousands of less visible preparations made it possible. Some public rules become difficult to change precisely because they work. They work so consistently that everybody depends on them without giving them much thought.

I want to talk about what happens when such a rule needs to change.

Not whether we should have standards. Not whether agreement between strangers is valuable. I am interested in a more difficult situation: a shared agreement has become inadequate, a better alternative exists, and almost nobody can adopt it successfully by themselves.

It is tempting to say, "Then install the better version." But a standard is not a piece of software running on one computer. It is a relationship between many participants, and it works only when enough of them understand one another.

That makes improving a successful system a peculiar engineering problem. You must change what everyone relies upon while continuing to provide what everyone relies upon. Sometimes you need a coordinated moment like Sweden's five o'clock. Sometimes you need decades of coexistence. And sometimes the most elegant transition is one in which most people never notice that a fundamental definition changed at all.

## Why the better answer may be the wrong move

Imagine two villages joined by a narrow bridge. The bridge is safe enough for ordinary traffic, but it was built for a lighter age. A new design would carry more weight, require less maintenance, and serve the villages better for the next century.

The proposal is sound. There is one difficulty. The old bridge is also the route by which the materials for the new bridge would arrive.

This is not an impossible situation. Engineers can design temporary supports, alternate routes, partial closures, and carefully staged work. But the existence of a better design does not answer the practical question of how to get there.

The same difficulty appears in any network of people who have learned to interact in a particular way. A protocol, a vocabulary, a file format, a timetable, a rule about which side of a road to use: each participant has invested in the expectation that other participants will continue to behave as they did yesterday.

Consider a tiny imaginary communications network. Ten people send messages using Format A. Format B is easier to understand and has a number of technical improvements. If all ten switch together, they are better off. If one person switches alone and cannot read messages in the old format, that person loses contact with the other nine. The old format is inferior in design but superior in immediate usefulness.

The problem is not irrational attachment to tradition. The first person to switch may be making an entirely rational decision to wait. The second may do the same. So may the ninth. A network can remain trapped in a convention that nearly all of its members would prefer to replace.

In game theory this resembles a coordination problem: the payoff from an individual's choice depends on what others choose. It need not be a prisoner's dilemma, and it need not imply that participants are selfish or foolish. The simple fact that our choices interact is enough.

Notice something else. "Better" is not a complete specification. Better for whom? Better immediately, or after years of adjustment? Better if everyone adopts, or also if only a minority can afford to? Better on paper, or better after compatibility equipment, training, security risks, and administrative work are included?

When a new standard is proposed, its advantages are often described in the language of the destination. Faster. Safer. More accurate. More open. These are reasonable things to want. But the journey has its own engineering requirements, and those requirements may determine whether the destination is ever reached.

I think this is one of the costs of the word "disruption." It can make continuity sound like an embarrassment. As though the need to keep hospitals working, records readable, payments possible, and old devices connected were simply evidence that somebody lacked imagination.

The people who have to live through a change are not obstacles scattered across the path to progress. Their continued ability to function is one of the things progress is supposed to protect.

## A day with two sides of the road

Return to Sweden. I want to think about the design of that transition rather than merely marvel at its scale.

The organizers could not reasonably tell drivers that they were free to adopt right-hand traffic whenever it suited them. Two opposing conventions on the same road would have been dangerous. Nor could each town switch at its own convenience without considering the roads connecting it to its neighbors. The rule had to change across an interconnected system, with clear exceptions and carefully arranged boundaries.

That is why the date and hour mattered. They supplied what engineers sometimes call a flag day: a coordinated moment at which participants are expected to switch from one convention to another. A flag day has enormous advantages when coexistence would be hazardous or incomprehensible. Instead of teaching every driver to negotiate with two possible traffic regimes at every encounter, the organizers arranged a temporary interruption and one new, widely understood rule.

The national campaign was not just advertising. It was part of the mechanism. Signs, vehicles, habits, maps, bus stops, and expectations all had to move together. Radio broadcasts and printed instructions were ways of synchronizing a very large collection of human decisions. The fact that the change could be described in a sentence did not make its implementation small.

I find the nineteen fifty-five referendum especially instructive. Roughly eighty-three percent of voters opposed the proposed change, yet the later parliamentary decision initiated the transition. That is a historical fact, not by itself a verdict on the legitimacy of the choice. The referendum, the change in circumstances, the parliamentary decision, and the experience of affected people are different pieces of the political story. A technical rationale does not settle whether a government has earned consent.

We should also be careful with stories of success. Contemporary and retrospective accounts describe an orderly switch and fewer traffic deaths in the immediate period afterward. That does not mean driving on the right is inherently safer than driving on the left. Temporary caution, altered speeds, and other factors complicate the comparison. The useful lesson is narrower: a coordinated change that seems impossible when imagined as millions of separate decisions can sometimes be carried out through planning and a common clock.

A flag day, however, becomes less practical as the system becomes less centralized, less bounded, or less capable of stopping. Sweden could issue traffic rules within a jurisdiction. Nobody can tell every device connected to the global internet to turn off on Saturday night and start again using a new packet format on Sunday morning.

That problem leads us to a very different kind of upgrade.

## The internet that cannot take a weekend off

Most people who use the internet do not need to know what an I P address is. It is enough that a message reaches the right destination. But networks need addresses, and the older widely deployed version of Internet Protocol provides them in thirty-two-bit fields. That is a finite address space. Practical allocation rules and reserved ranges make the stock of generally usable addresses smaller still.

As the internet expanded, engineers developed Internet Protocol version six, usually called I P v six. It uses a much larger address space and changes other aspects of the packet format and network behavior. Versions of the specification were published in the nineteen nineties, and the later Internet Standard, R F C eight two zero zero, was published in twenty seventeen.

Here comes the less glamorous part. An ordinary device that only understands I P v four packets does not become capable of understanding I P v six just because engineers have published a better specification. Routers, operating systems, applications, access providers, data centers, and network administrators participate in the exchange. Some can upgrade quickly. Others cannot. Some networks are tightly managed. Others contain forgotten machines with unknown dependencies.

Suppose a manufacturer adopts the new protocol but the customer's network has not. The new feature may be useless to that customer. Suppose the access provider upgrades but an important service remains accessible only through the old protocol. The provider still has to arrange a way for the customer to reach it.

There is no global five o'clock.

The resulting transition looks less like flipping a traffic sign and more like maintaining two road networks, building connections between them, and slowly shifting traffic from one to the other. A two-protocol device can speak both I P v four and I P v six. That arrangement is commonly called dual stack. Some systems carry new-protocol traffic through portions of an old-protocol network. Others perform translation at boundaries. An Internet Engineering Task Force document from twenty eleven, R F C six one four six, describes one translation mechanism, called N A T sixty-four, for allowing certain connections from I P v six clients to I P v four servers.

None of this is magic. Translation adds equipment, state, operational complexity, and potential failure modes. It does not preserve every possible application behavior transparently. A dual-stack installation has more than one network configuration to secure and maintain. A route that works in one protocol can fail in the other. The engineering effort is real.

Yet the alternatives are not merely to keep the old protocol forever or to abandon everyone who still depends on it. Coexistence can allow an improvement to reach people in stages.

I am not telling this story as a lament that I P v six has taken so long. The timeline is a revealing feature of the problem. Engineers did not forget how to design a packet header. They were trying to replace part of an enormous, distributed agreement without requiring all of its participants to move together.

If that sounds slow, consider the other side. The internet remained usable to people who never attended a protocol meeting, never read a specification, and never understood why their connection continued to work. That continuity was not free. It was produced by people who built the bridges between incompatible generations.

## The translators and their debts

There is an attractive fantasy about technological progress in which every new version cleanly supersedes the old one. The obsolete version is deleted. History becomes an orderly sequence of improvements, like pages in a textbook.

Real systems are more likely to develop layers. One program translates an old file. Another emulates a discontinued instruction set. A database promises to read a prior schema. A web service accepts a deprecated request while warning clients to change. A company retains a spare part for equipment it stopped selling years ago.

These arrangements are often dismissed as ugly compatibility work. Sometimes they really are ugly. They can hide fragile dependencies, multiply testing requirements, and prolong exposure to weaknesses that a clean replacement would remove.

But I want to defend a particular part of that ugliness. A translator can be a promise to people who arrived before the upgrade.

When somebody built their work around a published interface, they may have had good reason to expect it would remain usable for a period of time. A change imposed without warning can destroy the value of that work. Even when the new system is technically superior, making everyone else absorb the migration cost is not automatically a triumph of engineering.

Think of a program that saves a decade of scientific observations in a well-documented but aging file format. A new version of the program could discard the old reader. This would simplify the code. It would also turn some perfectly legitimate old data into an excavation project. Keeping a converter may be less exciting than adding a feature, but it protects a promise between software makers and the people whose work the software stores.

There are limits. If old behavior creates an unacceptable security risk, support may need to end. If a legacy interface structurally excludes people, refusing to change it can perpetuate harm. A compatibility layer can become the excuse for never making the necessary transition. A promise to yesterday's users is important, but it is not the only promise a system makes.

The question is how to end support responsibly. Give notice where possible. Explain what will break. Offer conversion paths and understandable tests. Document the data that must survive. Account for people who do not control the devices they use. A transition that cannot be made harmless can often be made less arbitrary.

This is why I resist the idea that the technical specification alone defines the quality of an upgrade. The behavior of the new system matters. So does the treatment of the people still living in the old one.

## The kilogram that changed without changing

Let us switch from communication networks to a small metal cylinder.

For more than a century, the international definition of the kilogram depended on a specific platinum-iridium artifact maintained near Paris. Laboratories around the world built systems of comparison and calibration that ultimately linked measurements to the agreed reference. It was an effective piece of international cooperation, but it placed the definition of mass on a particular physical object.

On the twentieth of May, twenty nineteen, the definition changed. The kilogram was no longer defined by that artifact. Instead, the revised International System of Units defined it using a fixed numerical value of the Planck constant, together with the other defining constants of the system. Instruments and methods such as the Kibble balance and silicon-crystal approaches made it possible to realize the unit without depending on one unique metal object.

Here is the part I find extraordinary: the new definition was chosen so that the magnitude of the kilogram would remain continuous with the old one. A customer buying one kilogram of flour was not expected to discover a new amount in the bag. Factories did not need to re-label every weight. Every scientific equation did not suddenly acquire a conversion factor.

The foundation changed while the ordinary meaning of the measurement was preserved.

There are technical qualifications. The revised S I affected multiple base-unit definitions, and some extremely precise electrical measurements had small adjustments when practical conventions were brought into alignment. But for the mass scale itself, continuity was a central design requirement. The International Bureau of Weights and Measures stated explicitly that most users would not notice the transition.

Compare this with Sweden. Swedish drivers needed to change their behavior at a particular hour. In metrology, people who measured mass in everyday contexts were meant to continue behaving as before, while the mechanism that justified and realized the common unit changed beneath the surface.

Public spectacle is a poor measure of whether reform is real. We sometimes speak as if genuine reform must look dramatic. A visible rupture is easy to photograph. A new definition that quietly preserves the measurements people rely upon can be an intellectual revolution with very little public spectacle.

And this was not accomplished by declaring that the new approach was correct and insisting that everyone cope. Metrologists had to make measurements, compare methods, assess uncertainty, establish the relation between the old mass scale and the new definitions, and produce practical guidance for how units could continue to be realized and disseminated. The institutions doing this work were not deciding whether Planck's constant would behave itself. They were deciding how to attach a stable, usable human unit to physical invariants while preserving the utility of earlier measurements.

Notice how different the three examples are. In Sweden, participants synchronized their outward behavior on a single day. In I P v six deployment, old and new systems coexist, often for years, through extra interfaces. In the kilogram redefinition, the fundamental specification changed while everyday use was designed to remain almost indistinguishable.

There is no universal migration recipe. The right design depends on what must remain compatible: behavior, connections, numerical meaning, historical records, or some combination of them.

## Who receives the bill?

At this point I want to ask a question that is too often left to the end of engineering discussions.

Who pays for the upgrade?

I do not mean just who funds a standards meeting or buys replacement hardware. I mean who spends time learning the new rule, who takes the risk during the period of uncertainty, and who loses access if their circumstances prevent them from moving.

Suppose a new digital identity format eliminates an ambiguity that has caused many errors. The improvement is real. But a person with a device that no longer receives software updates may suddenly be unable to identify themselves. A small organization with an aging database may have to spend its operating budget on conversion. The team proposing the standard may have accounted for its own implementation work and almost none of these downstream costs.

That example is hypothetical. Its point is not that a particular identity standard has caused these outcomes. It is that there is no reason to assume the cost of a transition falls on the same parties who benefit from it.

A standard's advantages are often distributed across a network. Its transition costs may be concentrated on the people least able to absorb them. This can create a perverse result: a system improves on average while becoming inaccessible to a significant minority.

A serious transition plan ought to identify at least several distinct burdens. There is the cost of understanding the change; the cost of modifying equipment or software; the cost of operating both versions during a transition; the cost of failures and mistakes; and the cost borne by people who cannot switch at all.

The last group is particularly easy to forget because its members may not be present in the room where the design is chosen. People with limited money, access, technical skill, or authority over their tools can be underrepresented in a standards process without anybody having deliberately excluded them.

This is not a reason to demand unanimity before any change. Unanimity is often impossible. But it is a reason to refuse the comforting assumption that an upgrade is harmless merely because most of the people who designed it will experience it as effortless.

There is a related question about incentives. If one company pays to build a bridge that many competitors can use, it may not receive all the benefit from its investment. If another can delay its own upgrade while relying on everybody else's compatibility work, delay can be individually attractive. Technical transition plans have to contend with these economic facts as much as with packet formats and file readers.

Sometimes the answer is shared funding. Sometimes it is an orderly deadline, a subsidy, a mandated minimum, or a compatibility obligation. Sometimes there is no satisfying answer, only a transparent argument about whose interests take priority. The uncomfortable truth is that changing a common technical rule can involve distributive decisions, even when everyone agrees on the engineering.

## Technical consensus is not political consent

How should those decisions be made?

One answer comes from the Internet Engineering Task Force, whose discussion of rough consensus explicitly resists treating technical decisions as mere headcounts. A good technical objection can matter even if only one person raises it. A majority can agree on a poor design. Demanding perfect unanimity, on the other hand, can allow one participant to block every change. An influential document by Pete Resnick, R F C seven two eight two, argues for taking objections seriously and evaluating whether they have been addressed rather than interpreting the loudest hum as a vote.

There is wisdom in that approach. If an engineer demonstrates that a proposed format loses information, the objection should not be overruled simply because most people in the room are tired of talking. The physics of a broken bridge is not settled by voting for the bridge to remain standing.

But technical consensus is not the whole of legitimacy.

Who was able to attend the meeting? Who was permitted to define the problem? Whose resources made it possible to spend months discussing the specification? Which users depend on the result but have no reason to know the name of the committee? Whose ability to object is purely theoretical because the cost of understanding the proposal is too high?

A standards body is not automatically a miniature democracy. Nor should every protocol parameter be decided by national referendum. The appropriate mechanism depends on the consequences of the decision, the community involved, the legal authority being exercised, and the rights of people who may be affected without choosing to participate.

Sweden's driving-side change was a government decision with legal force. The IETF develops technical specifications that participants may deploy through many independent decisions. The international metrology system rests on treaty institutions, expert measurement practice, and coordination among national laboratories. These are not interchangeable forms of authority.

One reason I am wary of treating every social problem as an engineering problem is that an engineered interface can hide a political choice beneath a technical description. Suppose a public service requires a particular digital credential. The credential might have excellent cryptography. It can still be a poor public policy if people who lack a compatible device cannot obtain the service. No cryptographic proof resolves the question of who should be allowed to participate.

Good experts should identify what their expertise can establish. A protocol designer can explain whether two systems can exchange messages. They cannot, on technical grounds alone, decide whose messages deserve to be heard.

I want experts in the room. I want the people who understand the machinery to speak clearly and sometimes insistently about what will work and what will fail. But I also want an open account of the values and burdens that do not fit inside the specification. The existence of a technically effective solution cannot absolve institutions of the duty to justify using it.

## Sometimes the old rule has to go

Let me argue against a possible misreading of everything I have said.

Perhaps it sounds as though the most ethical design is always the one that preserves compatibility. Keep every old interface. Protect every established expectation. Never require anybody to change until they feel ready.

That would be a terrible rule.

Old conventions can be harmful. A technical system may contain a serious security weakness. A building standard may prevent access. A public procedure may embody an exclusion that should never have been accepted. Waiting for everybody to adopt a better rule voluntarily may amount to making the victims of the old rule wait indefinitely.

There are cases where preserving continuity is itself the problem. Then the sensible question is not how to avoid all breakage. It is how to make the necessary break while reducing avoidable damage.

This requires a distinction between a justified transition and a comfortable transition. They are not the same. A decision can be justified even if some participants strongly dislike its costs. A new standard can be worth adopting even if the migration is difficult. The fact that an old convention was widely relied upon creates obligations to manage the consequences of changing it; it does not create a perpetual veto over improvement.

Conversely, calling something urgent does not excuse a badly designed rollout. Speed is a design constraint, not an argument that other constraints cease to exist. Even an emergency replacement benefits from clear notice, fallbacks where feasible, ways to identify failures, and attention to people left behind.

An organization facing a severe vulnerability might have to disable an old interface immediately rather than announce a leisurely deprecation period. That can be the responsible decision. The same organization can still document the reason, provide a migration path, and help users recover work where possible. Urgency changes the available choices. It does not eliminate the obligation to think about consequences.

There is also a category of transitions in which the old system and the new one cannot safely coexist. Sweden's traffic switch is a vivid example. In such cases, the effort devoted to synchronization is not bureaucratic delay. It is how the change becomes possible.

I would put the principle this way: preservation is a value, not an idol. Improvement is a value, not an incantation. Responsible change means asking what deserves to survive, what must end, and who gets injured by the crossing between them.

## Designing a future that can be revised

What should we build differently if we take all of this seriously?

First, we should think about change while designing the original system. It is much easier to create version markers, conversion paths, and public descriptions before an interface has accumulated twenty years of undocumented dependencies. A rule that assumes it will never change is not especially stable. It may be merely storing up a more expensive failure.

Second, we should keep the stable part as small as the task allows. A shared interface should specify what must be shared, without unnecessarily deciding everything inside the participating systems. If every internal implementation detail becomes part of the public promise, changing anything becomes an international negotiation. If nothing is specified, interoperability is fiction. The work lies in identifying the right boundary.

Third, when change is necessary, we should give the transition a design of its own. That can include a common cutover date, version negotiation, temporary translators, compatibility tests, public reference implementations, planned sunsets, or practical assistance for affected users. These are not ornamental appendices to the real engineering. They are engineering.

Fourth, we should measure success in the world of use, not only in the laboratory of design. A new protocol can pass its own tests while leaving some services unreachable. A new public procedure can be logically consistent while excluding people. A measurement definition can be scientifically improved but still needs calibration and traceability to become useful. The point is not to distrust the abstract specification. It is to remember that the specification was written to serve reality.

Fifth, we need institutions capable of revising their own decisions. There should be an intelligible way to raise objections, publish evidence, correct mistakes, and propose alternatives. The procedure should not require a person to become famous, wealthy, or socially powerful before an error is worth investigating.

Finally, we should resist the temptation to treat eventual compatibility as proof that the transition was well managed. When the new standard becomes ordinary, the people who paid the largest costs may disappear from the historical account. It is worth asking what was lost along the way, even if the destination turned out well.

None of these proposals guarantees a painless change. A society cannot promise continuous improvement while also promising that nothing will ever stop working. Those promises contradict each other. What it can promise, at least as an aspiration, is that change will be deliberate, its burdens visible, and its successes judged by more than the elegance of the new design.

## After five o'clock

There is a photographable moment in Sweden's traffic story: the cars crossing to the other side of the road at five in the morning. It is natural to treat that as the instant in which the future arrived.

But a great deal of the future arrived earlier. It arrived in roadwork, meetings, printed instructions, revised bus stops, arguments over costs, and people practicing an unfamiliar habit. The dramatic moment was possible because somebody had taken the undramatic responsibilities seriously.

Elsewhere, the future arrives through a network connection that still works while its underlying protocols change. Or through a scale that continues to report the same mass after the scientific foundation of its unit has been rebuilt. Or through a converter that lets a researcher open a file created by someone who has been dead for years.

The new version may be better. That does not mean the old version was worthless. Nor does it mean that the people who relied on it owe the future an effortless passage.

I think an important test of engineering maturity is whether we can admire a better design while keeping our obligations to the world that the older design made possible. Inventing the new rule takes intelligence. Making it possible for strangers to adopt the new rule without losing everything they built under the old one takes a different intelligence, and just as much of it.

At four fifty, everybody stopped. At five, they started again.

The difficult part was all the work that made those ten minutes possible.

<!-- END SPOKEN LECTURE -->

## Source notes and distinctions (not spoken)

This essay is original argument rather than a neutral synthesis. The Swedish chronology, the Internet Engineering Task Force specifications, and the BIPM records are evidence for particular historical and technical claims, not endorsements of the normative conclusions. The opening Swedish scene is a reconstruction from the official transition schedule and contemporary histories; it does not attribute thoughts or dialogue to an individual driver.

1. [Swedish National Museums of Transport History, *Högertrafik*](https://www.statensmuseermtf.se/vara-museer-och-samlingar/vara-samlingar/transporthistoria/vaghistoriska-samlingarna/trafikhistoria/hogertrafik) — official historical schedule of the 1967 change: restrictions from 01:00, stoppage and repositioning at 04:50, permitted traffic from 05:00, general travel from 06:00; broader planning and background. The source is in Swedish.
2. [Sveriges Radio, *Sweden marks 50th anniversary of right-hand side driving* (2017)](https://www.sverigesradio.se/artikel/6767655) — corroborates the September 3 date, 1955 referendum result, 1963 parliamentary decision, public campaign, and the transition schedule. Statements about accident trends are treated cautiously rather than as proof of the inherent safety of one driving side.
3. [S. Deering and R. Hinden, RFC 8200, *Internet Protocol, Version 6 (IPv6) Specification* (2017)](https://www.rfc-editor.org/rfc/rfc8200.html) — description of the newer IP packet format; RFC 8200 obsoletes the 1998 RFC 2460, not an assertion that IPv6 deployment began in 2017.
4. [E. Nordmark and R. Gilligan, RFC 4213, *Basic Transition Mechanisms for IPv6 Hosts and Routers* (2005)](https://www.rfc-editor.org/rfc/rfc4213.html) — dual-stack and configured tunneling mechanisms; the technical problem of coexistence with deployed IPv4.
5. [M. Bagnulo, P. Matthews, I. van Beijnum, RFC 6146, *Stateful NAT64* (2011)](https://www.rfc-editor.org/rfc/rfc6146.html) — specific applicability and limitations of translating selected IPv6-client traffic to IPv4 servers.
6. [International Bureau of Weights and Measures, *How the kilogram is realized*](https://www.bipm.org/en/physical-metrology-department/kilogram-realization) — pre-2019 kilogram artifact, revised definition, Kibble balance and independent realizations; consulted as the BIPM's technical explainer.
7. [BIPM, *SI base units*](https://www.bipm.org/en/measurement-units/si-base-units) — four redefined base units and the 2019 change.
8. [BIPM, *Resolution 1, 26th General Conference on Weights and Measures* (2018)](https://www.bipm.org/en/committees/cg/cgpm/26-2018/resolution-1) — primary institutional adoption of the revised SI, effective May 20, 2019.
9. [BIPM, *Information for users about the redefinition of the SI* (updated 20 May 2019)](https://www.bipm.org/documents/20126/52505189/SI-statement.pdf/a42e1340-2a8f-7cf4-e5c6-ee090d908200) — official contemporaneous explanation of continuity, the expectation that most users would not notice, and the small corrections to specialist electrical metrology.
10. [Pete Resnick, RFC 7282, *On Consensus and Humming in the IETF* (2014)](https://www.rfc-editor.org/rfc/rfc7282.html) — consensus framed as substantive assessment of objections, not vote-counting; it is an informational document and not an account of political democracy.

The imaginary two-village bridge, ten-person messaging network, legacy scientific file format, and digital-identity migration are constructed examples, not historical events. Discussion of the migration burden, the obligations of compatibility, and legitimacy is the essay's normative analysis. No quantitative claim about the present share of IPv4 or IPv6 deployment is made. No one transition mechanism is presented as universally preferable.
