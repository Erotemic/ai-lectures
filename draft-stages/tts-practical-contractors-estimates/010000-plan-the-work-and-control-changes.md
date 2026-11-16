# Plan the work and control changes

<!-- BEGIN SPOKEN LECTURE -->

# Plan the work and control changes

## Project Schedules, Sequencing, and Dependencies

A contractor says a kitchen renovation will take six weeks. The cabinet installer needs finished walls. The electrician needs some walls open. The countertops cannot be measured accurately until the cabinets are installed. The plumber needs the countertop and sink available before final connections. A schedule that merely lists everyone's dates can fail because it ignores the relationships that make those dates possible.

### A project is a network of dependencies

Some tasks can occur in parallel. Others must wait for a predecessor to finish, or at least for a specific deliverable to be ready. Framing may have to precede rough-in work. Inspections may need to happen before finishes conceal work. Fabrication may begin before the site is ready but cannot be completed until accurate field measurements exist. This is a dependency network, not simply a line of appointments.

Think of each task as a node and each prerequisite as a directed connection. If task B requires completion of A, then A must be complete before B can finish or start according to the specific dependency. A directed acyclic graph, a network without loops, is a useful abstraction because it lets us ask which sequences control the earliest possible completion date.

The critical path is the longest duration path through that dependency network under the schedule's assumptions. Tasks on it have no schedule slack in the simple model: delaying one delays completion unless something else changes. Tasks off the critical path may have float, meaning they can be delayed by some amount without affecting the final date. This does not mean they are unimportant. Float can disappear when another task runs late, when resources are shared, or when an inspection appointment becomes scarce.

### Work through a small schedule

Suppose framing takes two days. Rough electrical work and rough plumbing can each take two days after framing, in parallel. A required inspection takes one day after both are complete. Closing and finishing the wall takes three days after inspection. In this simplified network, the earliest completion is two plus two plus one plus three, or eight working days. If an electrician needs four days rather than two, the corresponding path becomes ten days. The plumbing crew's early completion does not erase the longer electrical dependency.

This example assumes crews and materials are available, tasks can overlap safely, and the inspection takes one day. Real schedules include permit lead times, drying and cure periods, fabrication, site access, and weather. A small change in task duration may have no effect when float exists, or a large effect when it strikes a bottleneck. The schedule is a model for decisions, not a guarantee that the calendar must obey it.

### Work often has hidden release conditions

An inspection is not only a calendar event. It may require completed work, approved documents, access, and readiness to demonstrate particular conditions. Delivery of a cabinet may require a clear storage area and protection from moisture. A floor finish may require acceptable substrate conditions and a minimum curing time. A concrete pour may depend on formwork, reinforcement inspection, forecast weather, and material availability.

When an estimate says 'paint: three days,' ask what allows painting to start. Is drywall already finished and dry? Are the windows installed? Will another trade return and open the wall? These start conditions determine whether a task can be scheduled meaningfully. Frequent rework is a sign that dependency assumptions were missing, not necessarily that individual tradespeople worked slowly.

The reverse problem occurs when a supplier needs long lead time. A special-order door may need measurement and approval weeks before installation. If the job waits until the wall is finished to order it, the entire project can stall. Purchasing and submittal approvals therefore belong in the schedule, even if no one is physically on the job site during that interval.

### Resources are another kind of constraint

Two tasks might be technically independent but both need the same worker, lift, scaffold, or temporary power connection. They cannot occur simultaneously just because a dependency diagram permits it. A project manager must coordinate both logical dependencies and resource availability. For small household projects this often means understanding when the owner must provide access, when the contractor can return, and what areas remain usable.

A realistic schedule also considers weather and exposure. Opening a roof just before a storm has different consequences from painting a sheltered interior wall. Exterior coatings have temperature, substrate-moisture, and curing limits; scheduling them solely by calendar date can produce poor work. Sometimes a task should move earlier or later to preserve conditions, even if the schedule becomes longer.

### Milestones tell us what is finished

A useful milestone is not merely 'phase two complete.' It describes an observable deliverable. 'Rough plumbing installed and ready for inspection' is more testable than 'plumbing mostly done.' 'Windows flashed and water-management inspection completed' is more useful than 'windows in.' A milestone should have acceptance criteria and an owner responsible for confirming it.

Payment milestones should also be defined carefully. A large payment due just because a date arrived may be different from one due after an independently verifiable stage of work. Contract rules vary by jurisdiction, but the general management problem is the same: money, evidence of completion, and remaining obligations should have explicit relationships. Documentation of inspections, change orders, and final punch-list work makes those relationships visible.

### The schedule must respond to new information

Suppose opening a wall reveals rotten framing. The contractor proposes a repair and the owner approves a change order. That changes the work, perhaps requiring additional inspection, material procurement, and drying. A useful update states which tasks are delayed, which can proceed in parallel, and the new earliest completion date. Writing 'two weeks added' without showing dependencies conceals the basis of the number.

A simple weekly review can ask: what was completed, what is next, what is blocked, what decision is needed from the owner, and what has changed on the critical path? Keep a current version of the schedule and distinguish original baseline from approved revisions. Without a baseline, neither side can explain whether a delay is caused by design changes, access, hidden conditions, material supply, or execution.

A schedule is not a weapon for blaming whichever worker appears late. It is a tool for making dependencies explicit while there is still time to change decisions. When it works, each trade arrives to a site that is ready, inspections occur before work is concealed, materials are available when needed, and the owner understands what completion actually means. The calendar is the output of this reasoning, not its substitute.

## Material Procurement, Substitutions, and Lead Times

The schedule depends not only on the order of trades, but also on when the required materials can actually arrive.

A renovation is scheduled to start in six weeks. The contractor has arranged a crew, the walls are ready for new windows, and the homeowner has chosen the product line. Then the supplier says the selected window is twelve weeks away. Suddenly material selection has become a scheduling problem. A different window is available tomorrow, but it has different dimensions, glass performance, flashing details, and warranty conditions. Choosing the substitute by color and price alone can create failures that outlast the delayed delivery.

### A material is not just a line on an estimate

Every specified item performs one or more jobs in the assembly. A window must fit an opening, resist weather, satisfy thermal and structural requirements, and integrate with interior and exterior finishes. A pump has pressure and flow characteristics, mounting connections, controls, and service conditions. A flooring material has thickness, movement characteristics, underlayment needs, and moisture limits. When an item changes, related work may need to change too.

Read a specification as a set of requirements rather than a brand wish list. Record the required dimensions, material, tested performance, accessories, installation conditions, compatible fasteners or adhesives, finish, and warranty. If a proposed alternative differs, list each difference. 'Or equal' is not self-executing; somebody with the appropriate authority has to decide whether the substitute actually satisfies the intended functions.

Submittals and product data can help document that decision. A data sheet provides the manufacturer's description and installation conditions. A shop drawing may show how the supplier proposes to fabricate or fit the item. Approval of a submittal under a particular contract does not necessarily transfer responsibility for unrelated design or installation errors. The contract determines who reviews, who decides, and who pays when a substitution changes work.

### Lead time is not delivery time alone

A quoted manufacturing lead time may begin only when a supplier receives complete, approved information or a deposit. It may exclude shop drawing review, shipping, customs, delivery appointments, site unloading, inspection for damage, or replacement of a wrong part. A material that must be installed after other work can become a bottleneck even if it is not the most expensive purchase.

Consider a simple dependency chain. Windows must be specified before fabrication. Openings must match the confirmed dimensions. Flashing and exterior weather protection follow installation. Interior finish work may need the building closed in first. If the window arrival slips, several downstream activities slip too. Another product might avoid that delay, but only if it fits the opening, installation method, and performance requirements without creating new work.

A good procurement schedule separates decision deadline, approved order date, confirmed production slot, expected shipping, delivery, and installation-ready date. Attach the person responsible for each. A supplier's early estimate is not a firm promise unless its terms say so. Update the schedule when approval or manufacturing status changes rather than treating the original date as a fact that must somehow remain true.

### Where cost changes hide

The purchase price is only one part of substitution cost. A substitute can require new framing, different electrical connections, extra waterproofing, revised permits, more labor, a different tool, or an added maintenance obligation. It may be cheaper at the distributor while raising the total installed cost. A later substitute can also leave the owner with a warranty gap if one party blames another's product or installation.

Suppose the originally selected window costs eight hundred dollars installed under an existing scope. A seemingly comparable unit is seventy dollars cheaper, but it requires resizing trim and additional flashing materials. The net installed change might exceed the savings. These numbers are illustrative; the key is to compare **scope-adjusted installed cost**, not catalog price. Written change records should capture both added and deleted work, schedule effects, and any performance differences.

Early purchasing has risks too. A product stored on site may be damaged, stolen, or become obsolete when dimensions change. Someone must be responsible for inspecting delivered goods and storing them according to the manufacturer's conditions. Paying for materials that are not yet installed may have contract, insurance, and lien implications. Written ownership and risk-of-loss arrangements are more useful than an informal assurance that the product is 'reserved for the job'.

### A repeatable substitution decision

When a contractor proposes an alternative, first ask why. Is the original unavailable, discontinued, incompatible with field dimensions, or simply more costly? Then ask for manufacturer and model information and a side-by-side comparison against the approved performance requirements. Include dimensions, fire or weather performance where relevant, energy characteristics, certifications, installation instructions, lead time, complete installed cost, and warranty.

Next ask who has authority to accept the change and whether it affects design, inspection, or permit obligations. A product that meets a manufacturer's marketing promise may still fail a contractual or adopted-code requirement. Record the approval before purchase or installation, not after the wall is closed. Keep the rejected options and rationale in the project record; they explain later why a particular product was chosen.

Procurement decisions can also be staged. Standard hardware may be easy to replace at short notice. Custom windows, fabricated steel, specialty tile, and made-to-order cabinets often need earlier decisions. Design work should identify such items before the crew depends on their arrival. A critical-path schedule can then show which lead times truly control completion and which have usable float.

### The practical check at delivery

When the material arrives, verify the model, quantity, dimensions, visible condition, accessories, and storage instructions. Compare the shipment to the approved order and submittals. Photograph damage and discrepancies before installation. A substitute that was correctly approved can still be delivered in the wrong configuration. Catching that mismatch at unloading is cheaper than discovering it after the product is concealed.

Good procurement is not shopping as cheaply as possible. It is preserving functional requirements while managing time, money, and responsibility. When the right item is available, a clear specification keeps everyone aligned. When it is not, a disciplined comparison turns the substitution into a conscious engineering and contractual choice rather than a hurried guess.

## Change Orders and Hidden Conditions

A contractor estimates a bathroom renovation. The agreed scope covers removing the old tile, installing new surfaces and reconnecting existing fixtures. Then the wall is opened and the crew finds water-damaged framing. The work cannot simply proceed as though the original estimate described the actual wall. Someone must decide whether to repair the damage, who will do it, what it costs, and whether the project schedule changes.

This is the world of change orders and concealed conditions. A change order is a documented change to an existing agreement. It might add work, remove work, replace an originally specified material, change completion dates or alter price. Not every change is evidence of misconduct. Buildings conceal real surprises. Yet an undocumented change can make the final bill impossible to reconcile with the work that was authorized.

### A base contract is a hypothesis about the job

An estimate is built from assumptions about quantities, access, materials and the state of existing systems. Some conditions are visible during a site visit; others cannot be inspected without demolition. A credible contract should make the boundary clear: what is included, what has been assumed, which work is excluded, what allowances or unit prices apply, and how unexpected conditions will be handled.

For example, 'replace two windows' is not sufficient detail to resolve rotted framing that appears beneath one window. Does the base scope include repairing the rough opening? Does it assume sound structural members? Is there a rate or allowance for replacing damaged material? Does the repair require a permit or additional inspection? The answers belong in the written scope and any amendments rather than in a conversation remembered differently by each party.

### Three different kinds of change

The first is an owner-requested variation. You decide to add built-in shelving or substitute a more expensive finish. That is new work relative to the contracted design. A contractor can reasonably price the additional material, labor and scheduling effects.

The second is a discovered condition: damaged framing, hidden plumbing, asbestos-containing material, unexpectedly shallow footing, or an unsupported previous alteration. These conditions may require investigation and a redesigned method, or specialist services beyond the original scope. Good documentation identifies what was discovered and why it changes the work. A photograph alone may not establish the correct remedy, but it can help preserve evidence before surfaces are closed.

The third is an error or omission in the original estimate or execution. If work explicitly included in the fixed scope was simply forgotten by the contractor, that is not automatically an owner-funded extra. The contract's allocation of risk and the governing law determine the answer. A useful negotiation begins by identifying which category the proposed charge actually belongs to rather than arguing over a single number.

### Build a change order that can be checked

Suppose the wall requires six additional feet of framing replacement. A meaningful change order describes the observed condition, the proposed remedy, the affected location, and the material and labor scope. It specifies additional or reduced cost, schedule effects, inspection or testing implications, and who must approve it before the change proceeds. It also states whether this amendment changes any previous warranty or responsibility.

A vague statement such as 'extra repairs as needed, price to be determined' leaves the homeowner without a way to evaluate or compare options. There may be emergencies where immediate stabilization is necessary to protect the property, but that does not remove the need for subsequent records and agreement on continuing work.

A written change order can include a fixed price, a unit rate, or time-and-material billing with agreed documentation and limits. The best method depends on how well the scope can be bounded. Unit pricing works when quantities are unknown but each unit is defined, such as an agreed per-linear-foot repair under specified conditions. It fails when the 'unit' hides an undefined level of difficulty. Time-and-material can be transparent when labor rates, material markups, daily records and a not-to-exceed amount are agreed; without them it may transfer more financial uncertainty than either party expects.

### Compare the cost of doing nothing

The presence of hidden damage does not mean every proposed repair is equally necessary. Ask what the consequence of leaving the condition is, whether code or structural requirements mandate a particular remedy, and whether independent diagnosis would change the decision. A compromised structural member and a cosmetic blemish require different urgency. The contractor's ability to expose the condition does not automatically make them the appropriate specialist to design the remedy.

Delaying a project also has costs. A paused crew may need to reschedule, materials may sit on site, and opened surfaces may require temporary protection. These are legitimate considerations that should be identified rather than silently rolled into an unexplained final total. Approval sequence matters because an owner who learns the price only after the work is hidden cannot evaluate the same choices.

### Keep the record coherent

A project ledger can have one line for each authorized change: date, reason, reference photographs, scope, price adjustment, schedule adjustment, approval, completion evidence and payment status. The running contract total is original price plus accepted additions minus accepted credits. A change to time should be recorded separately from money. A verbal promise to 'make it up later' is hard to verify once crews and subcontractors move on.

Specific legal requirements differ by jurisdiction. For example, New York home-improvement contract law addresses written contracts and amendments, and New York Attorney General consumer guidance advises recording verbal changes in writing. Those rules do not automatically apply nationwide, and some projects have additional municipal requirements. The general reasoning principle is broader: authorize a change with enough information to judge what changed and why.

An experienced customer or project manager does not reject every change order. They insist on converting uncertainty into an explicit decision. Open the wall, discover the condition, document it, evaluate solutions, agree on revised scope and cost, and only then lose access to the evidence by closing the wall again. That sequence protects both the person paying and the person performing the work.

## Scope Creep, Change Orders, and Cost Tracking: A Case Study

The change-control principles become easier to evaluate when several small changes accumulate in one project.

A homeowner contracts for a bathroom renovation at a fixed price. Two weeks later, the contractor explains that additional plumbing work is necessary and will cost several thousand dollars. The owner feels ambushed. The contractor says the original estimate could not include what was hidden inside the wall. Both statements may contain part of the truth. The missing piece is a clear method for deciding what is in the agreed scope, what is genuinely new, and how a change affects cost, schedule, and verification.

A construction project begins with a shared description of work, not merely a price. That description should identify the area, materials, quality expectations, access assumptions, what will be demolished, what will be preserved, what inspections are expected, and what is explicitly excluded. A fixed price can be meaningful only relative to a sufficiently defined scope and agreed treatment of unknown conditions.

### Scope is a boundary

Suppose the contract says, 'Replace the shower surround with tile.' Does it include demolishing existing backer board? Waterproofing the substrate? Moving a valve? Repairing subfloor rot? Repainting nearby walls? Each item affects materials, labor, and responsibility. A broad phrase can conceal disagreements until somebody has already removed the old tile.

A more informative scope identifies the intended finished assembly and who supplies or installs each component. It can specify that demolition will expose framing for inspection, that concealed damage requires documentation and an approved change, and that particular finish materials carry stated allowances. The intent is not to write an encyclopedia. It is to reduce ambiguity at boundaries where one trade's work becomes another's.

### Distinguish a defect from a new request

Three categories deserve different treatment. First, the contractor may discover hidden conditions that could not reasonably be seen before demolition, such as saturated framing or an undocumented pipe route. Second, the owner may request a design change, such as a different tile layout or an added niche. Third, the original work may have been incomplete or incorrectly performed. Calling every item a 'change order' can obscure which category applies.

A contractor's correction of work already within the agreed requirements should not automatically be treated as new paid scope. Conversely, a truly changed owner requirement can justify additional cost and time. Hidden conditions may trigger contract provisions that allocate risk or require the parties to approve a plan. The governing agreement and local law matter; no universal verbal rule settles every case.

### A change order is a small new contract

Before changed work proceeds, the parties should understand exactly what changes: the original scope item, the new description, materials, pricing method, schedule effect, inspection implications, and acceptance criteria. A signed change order or other agreed documented authorization provides a shared record. In a genuine emergency, immediate work may be necessary to prevent damage, but the facts, authorization, and resulting scope should still be documented as promptly and clearly as the circumstances permit.

Consider a shower replacement estimated at eighteen thousand dollars. During demolition, the contractor finds a section of damaged subfloor. The proposed repair is two thousand four hundred dollars, and the contractor expects it to add two workdays. The owner also decides to add a niche costing six hundred dollars and one more day. If both changes are approved, the authorized contract value becomes twenty-one thousand dollars. The schedule may increase by three days, but only if the work lies on the critical path; some tasks may overlap without delaying completion.

The bookkeeping matters because money already paid, work completed, and work authorized are different numbers. An estimate of a possible change is not necessarily approval. An invoice may include deposits or prior payments, so simply adding all invoices is not a reliable measure of total project cost.

### Keep a change ledger

A basic ledger has one row per change, with a unique identifier and date. Include who requested it, whether it was caused by concealed conditions or a design choice, scope description, price breakdown or agreed unit price, schedule impact, approval status, and evidence. Link photographs of hidden conditions taken before they are covered, relevant drawings, and inspection outcomes.

Use statuses such as proposed, approved, rejected, and completed. Do not include unapproved possibilities in the authorized contract total as though they are agreed obligations. A separate forecast can include pending risks, but it should say they are forecasts. This distinction becomes especially important when several independent contractors are working in the same space.

Allowances add another layer. A contract may include a set amount for fixtures whose exact models have not yet been selected. Replacing a fixture allowance with a more expensive product should account for the unused allowance amount, any applicable markup, labor change, and how the selection affects delivery. Otherwise the owner can accidentally pay for both the assumed fixture and the replacement.

### Schedule effects follow dependencies

A two-day activity does not always delay a project by two days. If an extra plumbing task can be done while materials are being delivered, it might not affect the completion date. If it must finish before waterproofing, tile, or inspection, its delay may cascade. A useful change record therefore identifies what work depends on the changed task and whether the completion milestone actually moves.

Consider the subfloor repair. It must be inspected and complete before the waterproofing system is installed. The added work may delay all finishing tasks in that room. The optional niche, however, might be framed during the same open-wall period and produce little additional schedule impact. A blanket statement that 'each change adds a week' is not meaningful without this dependency reasoning.

### Verify what the new money bought

Cost tracking should connect to acceptance. A repair to damaged framing should be documented while visible. The record should show what material was removed, why the replacement was selected, what inspection or structural criteria apply, and whether moisture conditions were addressed. A change to tile appearance should be checked against an approved layout or sample. Without acceptance criteria, the financial record may be complete while the quality dispute remains unresolved.

At closeout, reconcile original price, approved additions, approved credits, completed work, payments, retainage if any, and outstanding claims. Preserve warranties, product details, inspection records, and the final as-built description. A contractor who receives clear decisions and an owner who receives clear documentation are less likely to argue about what was authorized months later.

The lesson is not that change orders are inherently bad. Construction exposes conditions, and owners legitimately change their minds. The risk is invisible change: work begins without a shared description, cost is mixed with assumption, and schedule is discussed only after the fact. A good change process makes those decisions explicit while they are still possible to influence.

## Progress Payments, Warranties, and Liens

A homeowner hires a contractor to rebuild a porch. The written proposal describes excavation, footings, framing, railings, and final cleanup. The contractor requests half the price before any work begins and promises that the project will be finished quickly. Later, the footings have been poured and some framing erected, but the contractor requests another substantial payment before materials arrive. What should the homeowner examine before deciding whether the request makes sense?

A payment schedule should connect money to identifiable work, materials, and project risk. That sounds simple, but it involves several distinct issues: financing the contractor's purchases, confirming work performed, avoiding payment for defective or incomplete work, and understanding what obligations may remain after the prime contractor is paid. A progress payment is not only a bank transfer. It is a decision about how much uncertainty each party will carry.

### Tie milestones to things you can verify

A useful milestone is observable. 'After footings are inspected and accepted' is more specific than 'after phase one.' 'After windows are delivered and correctly installed' is easier to evaluate than 'at substantial progress.' The contract should define what qualifies for payment, which inspections must occur first, and how incomplete or disputed work will be treated.

This does not mean every payment should wait until the last nail. Contractors have legitimate costs for labor, materials, equipment, and subcontractors. A sensible schedule distributes financial risk rather than forcing one party to finance the entire project. It can include a reasonable deposit, progress payments linked to measurable stages, and a final balance after completion and outstanding corrections. The details depend on the jurisdiction and project.

The critical distinction is between work that **looks** complete and work that has been verified. A tiled shower can appear finished while its waterproofing was never inspected. A deck can look sturdy while its concealed ledger connection is wrong. Photographs at appropriate stages, inspection reports, and clear written acceptance criteria help prevent payment from outrunning evidence.

### Materials, deposits, and ownership

A contractor may request money to purchase special-order materials. What exactly happens if the project is delayed or the contractor disappears? Are the materials identified, delivered, insured, or held elsewhere? Who owns them once paid for? These questions should be answered by the contract and applicable law rather than assumed from a receipt.

Some states regulate the handling of home-improvement deposits or progress payments. New York, for example, has specific rules for covered home-improvement contracts and for protecting advance payments through escrow or bond arrangements. Those are state statutory rules, not a universal national template. The useful habit is to verify the actual law governing the project before treating a particular deposit practice as acceptable.

### What a warranty does and does not establish

A warranty is a promise about particular defects or performance for a defined period, subject to conditions and exclusions. It is not the same as a manufacturer's warranty on a component, and neither is equivalent to proof that the installation met the contract. A roof membrane might carry a product warranty while flashing workmanship is handled separately. A new HVAC unit may have parts coverage that depends on registration or maintenance, while labor coverage has a different term.

Read who provides each warranty, what is covered, who pays to diagnose and access the failed component, what maintenance is required, and how a claim is made. If a contractor offers a 'lifetime warranty,' ask whose lifetime and what the exclusions are. A durable written record and a verifiable responsible business matter more than an impressive phrase.

Warranties also do not replace ordinary contract rights, building standards, or statutory consumer protections. A contractor cannot necessarily disclaim every duty by writing a short guarantee. Conversely, a warranty may legitimately exclude damage from misuse or from changes made by others. The exact boundary is legal and jurisdiction-specific.

### The lien problem

A mechanic's lien, in the construction context, can allow eligible unpaid contractors, subcontractors, or suppliers to assert a claim against property under applicable law. This creates a risk that may surprise owners: paying the prime contractor does not always mean every participant in the project has been paid. The exact rights, notices, deadlines, and waivers vary substantially by jurisdiction.

Some contracts use lien waivers or releases tied to progress payments and final payment. These can be useful documents when they are valid, properly timed, and matched to the work or payment they describe. But a document labeled 'lien waiver' is not automatically a complete defense in every state. Its wording, statutory form, conditional status, and the identity of the signing party matter. For a consequential project, local legal guidance may be appropriate.

The practical point is to follow the payment chain. Know who is performing major work, who is supplying expensive materials, and what records demonstrate payment. If a contractor asks for a large additional payment because a subcontractor is unpaid, clarify the underlying obligations before responding. Do not rely on a casual verbal assurance when the amounts are significant.

### Closeout is a stage of work

At the end of a project, hold a walkthrough against the scope. Make a punch list of incomplete or defective items with photographs and agreed remedies. Confirm required inspections, permits, manuals, operating instructions, and warranty documents. Retain the contract, modifications, invoices, and proof of payments. The final balance should follow the agreed closeout requirements and applicable law.

This is not about mistrusting every contractor. Good contractors benefit from clear scopes, predictable cash flow, and prompt documentation, just as owners benefit from verifiable work. Conflicts often arise when one side believes 'finished' means appearance and the other believes it includes inspection, cleanup, and documentation.

The general principle is to make money trace the project. Tie payment to specified evidence, identify which promises survive completion, and understand who might still have a financial claim. That discipline is part of knowing how to commission a successful repair, not merely how to negotiate a price.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Project Schedules, Sequencing, and Dependencies

### 010000 — Project Schedules, Sequencing, and Dependencies

#### Technical companion (non-spoken)

##### Example directed acyclic graph

```text
Framing (2 days)
   ├─ Rough electrical (2 days) ─┐
   └─ Rough plumbing (2 days) ───┤
                                 v
                           Inspection (1 day)
                                 |
                           Finish wall (3 days)
```

- Minimum duration in the stated simplified conditions: `2 + max(2,2) + 1 + 3 = 8 working days`.
- Change electrical to 4 days: `2 + max(4,2) + 1 + 3 = 10 working days`.
- Define start-to-start and finish-to-start relationships explicitly for any overlap; calendars, weekends, and shared crews create additional constraints.

##### Review checklist

For every milestone: predecessor deliverables, trade/owner, earliest feasible start, material arrival, permits/inspections, weather/curing dependencies, objective acceptance test, and effects on payment.

##### Limits

Critical-path scheduling is a model. Contractual delay rights, liquidated damages, lien waivers, notice periods, and payment terms depend on actual agreements and governing law. Construction-management references support concepts, not any one legally enforceable schedule.

#### Selected reading and evidence records (non-spoken)

- `pmi-critical-path-risk` — [Project Management Institute, Schedule Risk Analysis Simplified](https://www.pmi.org/learning/library/schedule-risk-analysis-simplified-10573). Critical path, float, network dependencies, and limits of deterministic schedule assumptions
- `nyag-hiring-contractors` — [Office of the New York State Attorney General, Hiring a Home-Improvement Contractor](https://ag.ny.gov/publications/hiring-home-improvement-contractor). Local license checks, insurance, permits/inspections and written scope; NY guidance only

### Material Procurement, Substitutions, and Lead Times

### 015000 — Material Procurement, Substitutions, and Lead Times

#### Technical companion (non-spoken)

##### Substitution comparison worksheet

| Field | Original specified item | Proposed alternative | Change approval |
|---|---|---|---|
| Manufacturer/model/edition | | | |
| Dimensions, interfaces, accessories | | | |
| Performance/certification requirements | | | |
| Compatible installation details | | | |
| Full installed cost and change scope | | | |
| Submittal/permit/warranty implications | | | |
| Order date, delivery date, recovery plan | | | |

##### Milestones

`selection freeze → approved data/submittal → purchase authorization → production confirmation → shipping → receiving/inspection → installation → acceptance`. Put dependencies and owner of each action in the project schedule, not only the requested delivery date.

**Contract boundary:** Lien, deposit, stored-material payment, inspection, and substitution rights are contract- and jurisdiction-dependent. Written approval and change-order terms must follow the applicable agreement.

#### Selected reading and source locators (non-spoken)

- `ftc-improvement` — [Federal Trade Commission, How To Avoid a Home Improvement Scam](https://consumer.ftc.gov/articles/how-avoid-home-improvement-scam). Written estimates, contracts, licenses and payment caution.
- `aba-contract` — [American Bar Association, The Law & Your Home: What Should a Contract Include?](https://www.americanbar.org/groups/public_education/resources/law_issues_for_consumers/law-and-your-home/contract-include/). Scope, materials, change orders, responsibility and payment terms.
- `aia-lima-submittals` — [Gustavo A. Lima, AIA, According to Hoyle: The Submittal Process (American Institute of Architects Community, 2025)](https://communityhub.aia.org/blogs/gustavo-a-lima-aia/2025/09/26/according-to-hoyle-the-submittal-process). AIA A201 distinction between submittals and contract documents; contract dependent.
- `pmi-critical-path-risk` — [Project Management Institute, Schedule Risk Analysis Simplified](https://www.pmi.org/learning/library/schedule-risk-analysis-simplified-10573). Critical path, float, network dependencies, and limits of deterministic schedule assumptions.

### Change Orders and Hidden Conditions

**Track:** Contracts, Estimates, and Contractor Literacy. **Background:** written scopes, allowances, pricing and permit roles. **Purpose:** distinguish legitimate discoveries from vague open-ended charges during a project.

#### Technical companion (non-spoken)

##### Change-order record template

`CO number | discovery date | location | evidence/photos | original assumption | changed condition | corrective scope | excluded scope | price basis | tax/markup if applicable | schedule impact | permits/inspection | approval date | approvers | completion evidence`.

##### Worked reconciliation

Illustrative original contract: `$12,000`. Approved hidden-condition repair: `+$1,400`. Approved deletion of a fixture: `-$350`. Revised contract value: `$13,050`. The arithmetic is simple; ensuring that both approvals refer to unambiguous scopes is the difficult part. Do not pay for an unapproved or disputed scope merely because a revised running total appears in an invoice.

##### Legal-review scope

Record jurisdiction and contract type. Written amendment and signature requirements vary; New York General Business Law §771 and NY Attorney General guidance supply one state-specific example, not a national template. Some emergency stabilization may require immediate action under other rules; document such decisions separately.

#### Selected reading and claim sources (non-spoken)

- `nyag-hiring-contractors` — [Office of the New York State Attorney General, Hiring a Home-Improvement Contractor](https://ag.ny.gov/publications/hiring-home-improvement-contractor). Local license checks, insurance, permits/inspections and written scope; NY guidance only.
- `nysenate-gbl771` — [New York State Legislature, General Business Law §771: Contract Provisions](https://www.nysenate.gov/legislation/laws/GBS/771). Writing and signatures for home-improvement contract amendments under specific state law.

### Scope Creep, Change Orders, and Cost Tracking: A Case Study

### 014000 — Scope Creep, Change Orders, and Cost Tracking: A Case Study

#### Technical companion (non-spoken)

##### Illustrated contract ledger

| Item | Category | Status | Cost change | Schedule impact |
|---|---|---|---:|---|
| Original renovation | Agreed scope | Executed | $18,000 | Original completion |
| CO-01 damaged subfloor | Concealed condition | Approved | +$2,400 | +2 critical-path workdays assumed |
| CO-02 shower niche | Owner request | Approved | +$600 | +1 workday estimated; overlap TBD |
| Possible new light fixture | Potential owner request | Proposed | Excluded | Not agreed |

**Authorized value:** `$18,000 + $2,400 + $600 = $21,000`. Schedule should be separately recalculated from dependencies; the listed days are illustrative rather than automatically additive.

##### Change record fields

Unique ID, discovery date, requesting party, original scope reference, reason, photos before concealment, options, explicit exclusions, material/labor price basis, allowance adjustment, time impact, permit/inspection impact, owner/contractor approval, acceptance evidence, final payment accounting.

**Review boundary:** Contract remedies, notice requirements, lien rights, change authorization and consumer protections vary by jurisdiction and agreement. This is a project-management teaching example, not legal advice or a model contract clause.

#### Selected reading and evidence records (non-spoken)

- `aba-contract` — [American Bar Association, The Law & Your Home: What Should a Contract Include?](https://www.americanbar.org/groups/public_education/resources/law_issues_for_consumers/law-and-your-home/contract-include/). Scope, materials, change orders, responsibility and payment terms.
- `ftc-improvement` — [Federal Trade Commission, How To Avoid a Home Improvement Scam](https://consumer.ftc.gov/articles/how-avoid-home-improvement-scam). Written estimates, contracts, licenses and payment caution.
- `nyag-hiring-contractors` — [Office of the New York State Attorney General, Hiring a Home-Improvement Contractor](https://ag.ny.gov/publications/hiring-home-improvement-contractor). Local license checks, insurance, permits/inspections and written scope; NY guidance only.
- `md-allowances` — [Maryland People’s Law Library, Home Improvement: Contract Tips](https://peoples-law.com/node/348/printable/print). Allowances and differences between fixed price and time/materials.
- `pmi-critical-path-risk` — [Project Management Institute, Schedule Risk Analysis Simplified](https://www.pmi.org/learning/library/schedule-risk-analysis-simplified-10573). Critical path, float, network dependencies, and limits of deterministic schedule assumptions.
- `aia-lima-submittals` — [Gustavo A. Lima, AIA, According to Hoyle: The Submittal Process (American Institute of Architects Community, 2025)](https://communityhub.aia.org/blogs/gustavo-a-lima-aia/2025/09/26/according-to-hoyle-the-submittal-process). AIA A201 distinction between submittals and contract documents; contract dependent.

### Progress Payments, Warranties, and Liens

**Track:** Contractor Literacy and Estimates. **Background:** Scopes, estimates, change orders, permits, and inspections. **Purpose:** understand how money and evidence should follow delivered work.

#### Technical companion (non-spoken)

##### Sample milestone review

| Milestone | What can be observed | Records to request |
|---|---|---|
| Mobilization/materials | Delivered items, identified special orders | Contract terms, invoice, ownership/insurance evidence |
| Concealed work | Footings, rough framing, waterproofing | Photos, inspection/approval documentation |
| Near completion | Operating equipment and finished surfaces | Functional tests, punch list |
| Closeout | Corrected deficiencies | Final inspections, warranties, releases if valid/applicable |

##### Legal distinction

New York State Attorney General guidance identifies contracts, progress payments, escrow or bond arrangements, and liens for covered home-improvement work. Other states may have materially different schemes. This lecture does not supply a national lien-waiver form or legal conclusion.

**Review boundary:** The contract and local law control payment and lien rights. For substantial disputes or potential liens, seek appropriate local legal review.

#### Selected reading and evidence records (non-spoken)

- `nyag-home-improvement-fact` — [Office of the New York State Attorney General, Home Improvement Fact Sheet](https://ag.ny.gov/home-improvement-fact-sheet). New York progress payments, escrow/bond rules, warranties and lien-related risks.
- `nyag-hiring-contractors` — [Office of the New York State Attorney General, Hiring a Home-Improvement Contractor](https://ag.ny.gov/publications/hiring-home-improvement-contractor). Local license checks, insurance, permits/inspections and written scope; NY guidance only.
- `nysenate-gbl771` — [New York State Legislature, General Business Law §771: Contract Provisions](https://www.nysenate.gov/legislation/laws/GBS/771). Writing and signatures for home-improvement contract amendments under specific state law.
