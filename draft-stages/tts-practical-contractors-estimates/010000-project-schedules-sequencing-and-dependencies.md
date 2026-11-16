# 010000 — Project Schedules, Sequencing, and Dependencies

<!-- BEGIN SPOKEN LECTURE -->

A contractor says a kitchen renovation will take six weeks. The cabinet installer needs finished walls. The electrician needs some walls open. The countertops cannot be measured accurately until the cabinets are installed. The plumber needs the countertop and sink available before final connections. A schedule that merely lists everyone's dates can fail because it ignores the relationships that make those dates possible.

## A project is a network of dependencies

Some tasks can occur in parallel. Others must wait for a predecessor to finish, or at least for a specific deliverable to be ready. Framing may have to precede rough-in work. Inspections may need to happen before finishes conceal work. Fabrication may begin before the site is ready but cannot be completed until accurate field measurements exist. This is a dependency network, not simply a line of appointments.

Think of each task as a node and each prerequisite as a directed connection. If task B requires completion of A, then A must be complete before B can finish or start according to the specific dependency. A directed acyclic graph, a network without loops, is a useful abstraction because it lets us ask which sequences control the earliest possible completion date.

The critical path is the longest duration path through that dependency network under the schedule's assumptions. Tasks on it have no schedule slack in the simple model: delaying one delays completion unless something else changes. Tasks off the critical path may have float, meaning they can be delayed by some amount without affecting the final date. This does not mean they are unimportant. Float can disappear when another task runs late, when resources are shared, or when an inspection appointment becomes scarce.

## Work through a small schedule

Suppose framing takes two days. Rough electrical work and rough plumbing can each take two days after framing, in parallel. A required inspection takes one day after both are complete. Closing and finishing the wall takes three days after inspection. In this simplified network, the earliest completion is two plus two plus one plus three, or eight working days. If an electrician needs four days rather than two, the corresponding path becomes ten days. The plumbing crew's early completion does not erase the longer electrical dependency.

This example assumes crews and materials are available, tasks can overlap safely, and the inspection takes one day. Real schedules include permit lead times, drying and cure periods, fabrication, site access, and weather. A small change in task duration may have no effect when float exists, or a large effect when it strikes a bottleneck. The schedule is a model for decisions, not a guarantee that the calendar must obey it.

## Work often has hidden release conditions

An inspection is not only a calendar event. It may require completed work, approved documents, access, and readiness to demonstrate particular conditions. Delivery of a cabinet may require a clear storage area and protection from moisture. A floor finish may require acceptable substrate conditions and a minimum curing time. A concrete pour may depend on formwork, reinforcement inspection, forecast weather, and material availability.

When an estimate says 'paint: three days,' ask what allows painting to start. Is drywall already finished and dry? Are the windows installed? Will another trade return and open the wall? These start conditions determine whether a task can be scheduled meaningfully. Frequent rework is a sign that dependency assumptions were missing, not necessarily that individual tradespeople worked slowly.

The reverse problem occurs when a supplier needs long lead time. A special-order door may need measurement and approval weeks before installation. If the job waits until the wall is finished to order it, the entire project can stall. Purchasing and submittal approvals therefore belong in the schedule, even if no one is physically on the job site during that interval.

## Resources are another kind of constraint

Two tasks might be technically independent but both need the same worker, lift, scaffold, or temporary power connection. They cannot occur simultaneously just because a dependency diagram permits it. A project manager must coordinate both logical dependencies and resource availability. For small household projects this often means understanding when the owner must provide access, when the contractor can return, and what areas remain usable.

A realistic schedule also considers weather and exposure. Opening a roof just before a storm has different consequences from painting a sheltered interior wall. Exterior coatings have temperature, substrate-moisture, and curing limits; scheduling them solely by calendar date can produce poor work. Sometimes a task should move earlier or later to preserve conditions, even if the schedule becomes longer.

## Milestones tell us what is finished

A useful milestone is not merely 'phase two complete.' It describes an observable deliverable. 'Rough plumbing installed and ready for inspection' is more testable than 'plumbing mostly done.' 'Windows flashed and water-management inspection completed' is more useful than 'windows in.' A milestone should have acceptance criteria and an owner responsible for confirming it.

Payment milestones should also be defined carefully. A large payment due just because a date arrived may be different from one due after an independently verifiable stage of work. Contract rules vary by jurisdiction, but the general management problem is the same: money, evidence of completion, and remaining obligations should have explicit relationships. Documentation of inspections, change orders, and final punch-list work makes those relationships visible.

## The schedule must respond to new information

Suppose opening a wall reveals rotten framing. The contractor proposes a repair and the owner approves a change order. That changes the work, perhaps requiring additional inspection, material procurement, and drying. A useful update states which tasks are delayed, which can proceed in parallel, and the new earliest completion date. Writing 'two weeks added' without showing dependencies conceals the basis of the number.

A simple weekly review can ask: what was completed, what is next, what is blocked, what decision is needed from the owner, and what has changed on the critical path? Keep a current version of the schedule and distinguish original baseline from approved revisions. Without a baseline, neither side can explain whether a delay is caused by design changes, access, hidden conditions, material supply, or execution.

A schedule is not a weapon for blaming whichever worker appears late. It is a tool for making dependencies explicit while there is still time to change decisions. When it works, each trade arrives to a site that is ready, inspections occur before work is concealed, materials are available when needed, and the owner understands what completion actually means. The calendar is the output of this reasoning, not its substitute.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Example directed acyclic graph

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

### Review checklist

For every milestone: predecessor deliverables, trade/owner, earliest feasible start, material arrival, permits/inspections, weather/curing dependencies, objective acceptance test, and effects on payment.

### Limits

Critical-path scheduling is a model. Contractual delay rights, liquidated damages, lien waivers, notice periods, and payment terms depend on actual agreements and governing law. Construction-management references support concepts, not any one legally enforceable schedule.

## Selected reading and evidence records (non-spoken)

- `pmi-critical-path-risk` — [Project Management Institute, Schedule Risk Analysis Simplified](https://www.pmi.org/learning/library/schedule-risk-analysis-simplified-10573). Critical path, float, network dependencies, and limits of deterministic schedule assumptions
- `nyag-hiring-contractors` — [Office of the New York State Attorney General, Hiring a Home-Improvement Contractor](https://ag.ny.gov/publications/hiring-home-improvement-contractor). Local license checks, insurance, permits/inspections and written scope; NY guidance only
