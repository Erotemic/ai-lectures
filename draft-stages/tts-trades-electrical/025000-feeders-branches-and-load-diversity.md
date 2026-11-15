# 025000 - Feeders, Branch Circuits, and the Demand a Building Actually Makes

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** distribution one-lines, panel schedules, hypothetical load profiles and demand calculations.

<!-- BEGIN SPOKEN LECTURE -->

# Feeders, Branch Circuits, and the Demand a Building Actually Makes

A modern house can contain dozens of electrical loads: lamps, refrigeration, cooking equipment, water heating, space conditioning, computers, tools, and perhaps an electric vehicle charger. If every appliance has a nameplate power, why not add all the numbers and select a supply large enough for the total?

Sometimes that sum provides a useful upper bound. Often it is a poor estimate of the power a building actually demands at one time. Some loads cycle on and off. Others have large starting currents but modest steady operating power. Some cannot operate simultaneously because they share control logic. Still others can run together continuously during extreme weather or a long cooking session.

Designing electrical distribution is therefore two problems at once. The first is **topology**: which conductors and protective devices feed which loads? The second is **demand**: what currents and thermal stresses will the system actually experience, over which time intervals and under which allowed operating conditions? Those problems meet in the words service, feeder, branch circuit, connected load, demand and diversity.

## Start with the one-line hierarchy

Imagine a supply entering service equipment. From a distribution bus, one protected circuit runs to lighting and receptacles; another runs to a large fixed appliance; a third serves a smaller distribution panel some distance away.

In common U.S. terminology, a **branch circuit** is the circuit conductors between the final overcurrent protective device protecting that circuit and the outlets or loads it supplies. A **feeder** generally supplies downstream branch-circuit overcurrent devices from service or other upstream distribution equipment. The definitions matter because they identify where fault protection, load calculations and conductor selection apply.

An outlet in electrical-code terminology is the point where current is taken to supply utilization equipment. It is not necessarily a wall receptacle. A hardwired luminaire or appliance can be supplied through an outlet without a familiar plug-and-socket connection. That vocabulary prevents a common misunderstanding when someone reads a plan that says 'outlet' next to lighting or mechanical equipment.

A house need not have a separate feeder for every branch. A main service panel can supply final branch circuits directly. A detached outbuilding or a distribution subpanel may be supplied by a feeder that in turn supplies several branch circuits. Large properties and commercial buildings may use a hierarchy of switchboards, distribution boards and final circuits, with multiple levels of coordination.

The difference is functional, not merely a matter of cable thickness. A feeder ends upstream of the final protective devices for the circuits it supplies. A branch circuit begins downstream of its final protective device. Equipment can combine several functions in one enclosure, so a diagram and device arrangement are more informative than the box's popular name.

## Protection is organized around current paths

Suppose a branch circuit supplies several receptacles. It has conductors and connections with current-carrying limits, an overcurrent protective device with particular time-current behavior, and a collection of loads whose currents may vary. The device should protect the wiring under applicable normal and abnormal conditions, subject to the selected design method and installation rules. A load label on a breaker is not enough to infer that every cable downstream has been chosen correctly.

A feeder has its own current-carrying and fault-withstand considerations. It can also feed a panel containing several branch protective devices. The upstream feeder protection and downstream branch protection may respond to different faults; their operating curves and settings influence how much of a building loses supply during a fault. This is one aspect of **selective coordination**, a concept treated more thoroughly in power-system protection studies.

The nameplate rating of a protective device is not the current at which it must instantly open. Thermal and magnetic or electronic trip characteristics differ by product and application. Nor is the interrupting rating the same as the current a device is intended to carry continuously. A twenty-ampere branch rating, an available fault current of several thousand amperes, and a breaker interrupting rating are answers to three distinct questions.

## Connected load is not the same as demand

**Connected load** is a sum based on the ratings or assigned values of connected equipment. **Demand** refers to the load actually called for under a defined operating scenario or measurement interval. **Maximum demand** is the greatest observed or calculated demand over some stated period and set of assumptions.

Imagine ten appliances, each with a two-kilowatt nameplate. The arithmetic total is twenty kilowatts. But suppose a carefully observed hypothetical operating period has no more than three appliances operating together, and one of those is cycling. The maximum observed power might be six kilowatts or less during that period. It does not follow that a six-kilowatt electrical supply is adequate for every allowable future operating condition. An observed profile is evidence about the past, not a proof that all higher coincidences are impossible.

Now suppose some of those appliances are in different apartments. Combining their nameplate ratings assumes every resident selects the most demanding operating state at exactly the same moment. That is a conservative hypothetical coincidence, but it may overpredict a large building's typical peak. Engineers use measured load profiles, operational constraints, diversity assumptions, and code-prescribed calculation methods to make the estimate defensible.

The relevant time interval matters. A short motor start, a ten-minute cooking interval, and a multi-hour electric heating load can have different effects on equipment, protective devices and conductors. Peak current, RMS current, apparent power, real energy over a billing interval and long-duration thermal loading are not synonyms. The model must name the quantity being sized.

## Diversity is useful vocabulary, but the convention matters

In careful statistical language, a **coincidence factor** is the maximum simultaneous demand of a group divided by the sum of the individual maximum demands over the relevant definition of the interval. This is at most one when the numerator and denominator describe the same set of loads and compatible observation conditions. The reciprocal is often called a **diversity factor**, so it is at least one.

Unfortunately, practitioners sometimes use the words differently. Schneider Electric's Electrical Installation Guide explicitly notes that tables labeled 'diversity factor' in practical installation discussions may actually use a simultaneity multiplier less than or equal to one. Consequently a factor of point six in a design document is not meaningful until you know whether the author means 'multiply connected load by point six' or is using the reciprocal ratio.

Take four identical hypothetical loads whose individual maxima are five kilowatts each. Their total individual maxima are twenty kilowatts. If the greatest simultaneous demand over the defined period is twelve kilowatts, the coincidence factor is zero point six. Its reciprocal diversity factor is about one point six seven. The information is the same, but the two numbers go in opposite directions. Calling both of them 'diversity factor' without definition creates a real risk of incorrect arithmetic.

Demand factors and diversity values are **not universal permissions** to reduce conductor capacity. Their relevance depends on the population of loads, intended operation, measurement evidence, installation code and exceptions. A table developed for an apartment block in France cannot be pasted into a North American detached-home calculation merely because both buildings contain kitchens and lights.

## The code calculation is a defined engineering model

In U.S. National Electrical Code practice, calculations distinguish branch circuits, feeders and services and prescribe when specific values or adjustments are allowed. The structure itself has changed between recent editions. The 2023 NEC placed much of this material in Article 220. The 2026 NEC reorganized the subject under a new Article 120. NFPA's own explanation of the 2026 revision identifies this reorganization and describes technical changes to some rules. That means a reference such as 'Article 220 says' is incomplete without an edition and the applicable locally adopted text.

International low-voltage installation guidance likewise uses defined demand and simultaneity approaches, but national implementations differ. IEC 60364 Part 5-52 addresses wiring systems, while IEC 60364 Part 5-54 addresses protective conductors and earthing arrangements. Those public publisher descriptions establish scope; they are not substitutes for selecting conductor sizes from the full applicable clauses and locally adopted modifications.

A real load calculation may need to consider floor area, equipment classifications, fixed appliances, motor starting, heating and cooling combinations, continuous operation, noncoincident loads, electric vehicle charging, and control systems that enforce a maximum demand. Which adjustments are permitted is a regulatory and equipment-specific question. The engineering motivation is to size components for plausible and authorized operating states without pretending every device's rated maximum occurs at once.

## A load manager changes the set of possible states

Suppose two loads would each draw four kilowatts, but an engineered controller prevents them from operating simultaneously. Their combined nameplate ratings are eight kilowatts. Their **controlled simultaneous demand** might be limited to four kilowatts under normal designed operation, plus any separately relevant auxiliary loads.

That is a different claim from 'historically these two loads were rarely used together'. In the first case an actual control architecture changes which operating states the design permits. In the second case a statistical guess describes human behavior. When a code allows certain load-control assumptions, the controller's reliability, default behavior, installation, product approval and scope become essential parts of the calculation.

The lesson extends to energy sources. A battery inverter may have a continuous apparent-power limit, a surge-current capability, conversion losses, and control rules for what loads can operate at once. A photovoltaic array has variable production. A household wiring system may be able to carry a current under one set of conditions while the inverter cannot supply the associated starting transient. Connected kilowatts, available instantaneous power, daily energy, and overload protection all need their own columns in the design.

## Voltage drop is about the whole current path

A feeder or branch circuit is not an ideal zero-resistance connection. Its voltage drop depends on conductor impedance, current, phase arrangement, power factor, length, joints and operating temperature. For a simple resistive classroom loop with one-hundred-fifty milliohms of total resistance, a twenty-ampere current causes three volts of drop. At that current, the loop dissipates sixty watts of heat, distributed along the modeled resistance.

That energy matters because it is converted into heat in the conductors and connections. But one formula does not give a complete conductor design. The cable's ampacity depends on installation conditions and material; its voltage drop depends on current and impedance; its protective device must address faults; and the equipment at the far end may have its own allowable input range. A long circuit can meet one constraint and fail another.

This also explains why reducing normal current can have several benefits. With the same resistance, halving current quarters resistive heating. Increasing distribution voltage can reduce current for a given ideal power when the rest of the comparison is appropriate. Those statements are physics, not approval to change nominal system voltage or conductor size arbitrarily.

## Panel schedules and real loads

A useful panel schedule identifies circuits by the loads or areas served, their overcurrent devices, conductor information where documented, source and panel relationships, and the drawing revision. A service or feeder schedule may also record load calculations, neutral assumptions, phase allocation, protective-device ratings and spare capacity. The documentation should explain whether values are connected loads, measured peak demands, or design assumptions.

On a split-phase service, allocation of one-hundred-twenty-volt loads across the two outer conductors affects current balance and the shared neutral. On a three-phase system, distribution across phases matters too, and nonlinear loads can complicate neutral calculations. Merely counting the number of breaker handles on each side of a panel is not a reliable load-balancing calculation; the actual current and phase relationships are what matter.

If planning a new workshop, laundry circuit, heat pump, or electric vehicle supply, begin with the equipment's actual electrical data and the intended usage pattern. Trace the proposed supply to the source, identify each protective boundary, record the service and feeder constraints, and separate calculated load from measured history. The result is a clear engineering question that can be checked against the applicable installation requirements.

The most important distinction is not between a small breaker and a large breaker. It is between **what is connected**, **what can operate simultaneously**, **what the conductors and equipment can continuously withstand**, and **what protective devices must interrupt under faults**. Once those become separate quantities, electrical distribution starts to look less like a collection of arbitrary ratings and more like a system with comprehensible design tradeoffs.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Source to load hierarchy

```text
SERVICE EQUIPMENT
  |-- final OCPD --> BRANCH CIRCUIT --> outlets / utilization loads
  |
  |-- FEEDER OCPD --> FEEDER --> distribution panel
                                 |-- final OCPD --> branch --> lighting
                                 |-- final OCPD --> branch --> appliance
```

The distinction follows the final overcurrent device, not the colloquial label of the enclosure. Actual code-defined feeder and branch boundaries must be checked for the adopted edition and source configuration.

### Demand calculations on an invented load profile

| Quantity | Definition for this example | Value |
|---|---|---:|
| Sum of four individual maxima | 4 loads x 5 kW | 20 kW |
| Observed group maximum | Greatest simultaneous sum over specified window | 12 kW |
| Coincidence factor | Group maximum / sum of individual maxima | 0.60 |
| Reciprocal diversity factor | Sum of maxima / group maximum | 1.667 |

The numeric values are hypothetical. A utilization factor or diversity assumption from a specific regulation is not inferred from them.

### Voltage-drop classroom model

At `I = 20 A` and `R_loop = 0.15 ohm`, `V_drop = I*R = 3 V` and `P_heat = I^2 R = 60 W`. This is *not* a conductor-selection procedure. It omits AC reactance, connection heating distribution, temperature effects, circuit geometry, installation methods and equipment requirements.

### Exercises - paper only

1. Is every circuit leaving a service panel a feeder? **Answer:** no. A circuit protected by the final branch protective device and serving end loads is a branch circuit, while a circuit supplying downstream branch protective devices may be a feeder.
2. Do four 5 kW nameplates prove a 20 kW service is required? **Answer:** no. They define a connected-load sum; a code-governed design-demand calculation and allowable operating states are distinct.
3. If a coincidence factor is 0.75, what is its reciprocal diversity factor? **Answer:** 4/3, about 1.333.
4. A one-hour average energy use is 4 kWh. Does that prove no higher instantaneous power occurred? **Answer:** no; energy integrates power over time.
5. A demand controller is supposed to prevent two loads from operating simultaneously. What documentation matters? **Answer:** permitted product/function, failure behavior, tested operating states, actual source topology and adopted-code treatment.

### Attribution, regulatory context, and scope

The distinction among connected load, coincidence factor and diversity factor is tied to Schneider Electric's published Electrical Installation Guide, which openly records inconsistent industry terminology. The U.S. National Electrical Code's load calculation framework is collectively developed by NFPA code-making panels, not by a named textbook author. NFPA's published 2026 reorganization article confirms the move of the general load-calculation material to Article 120; the 2023 edition's earlier organization is not silently applied to 2026. The lecture's sample numbers and calculations are instructional synthesis and do not implement a local load schedule. IEC 60364 source pages verify subject scope, not uninspected conductor sizing clauses.

## Claim-level source map

| Claim ID | Consequential claim | Source and exact support role | Limits / review |
|---|---|---|---|
| E025000-01 | Branch circuit is downstream of final circuit overcurrent device and supplies outlets | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Branch circuit definition; primary_us_regulation); [electrical-nfpa-service-point-record](https://docinfofiles.nfpa.org/files/AboutTheCodes/70/70_A2018_NEC_P01_SD_pcsubmittals.pdf) (Article 100 definitions context; standards_development_context) | OSHA is not an adopted residential NEC; Article 100 source is historical public process report. |
| E025000-02 | Feeder is upstream of final branch-circuit protective device | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Feeder definition; primary_us_regulation); [electrical-nfpa70](https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70) (NEC development and scope; separate_standards_context) | Exact adopted code edition remains locally specific. |
| E025000-03 | Outlet includes hardwired utilization point; receptacle is a separate device | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Outlet and Receptacle definitions; primary_us_regulation) | No universal terminology across all national systems. |
| E025000-04 | Overcurrent device rating differs from interrupting rating and time-current behavior | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Circuit breaker and overload definitions; primary_us_regulation); [electrical-osha304](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (1910.304(f) overcurrent protection and breaker rating; same_agency_context) | Two OSHA pages are not independent corroboration of product-specific curves. |
| E025000-05 | Connected nameplate load differs from coincident demand over a time interval | [electrical-se-diversity](https://www.electrical-installation.org/enwiki/Diversity_factor) (Definitions of maximum demand and simultaneity; technical_guide); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Power versus energy distinction; independent_physics) | Actual permitted design methods depend on jurisdiction. |
| E025000-06 | Individual maximum sum can exceed maximum simultaneous sum for multiple loads | [electrical-se-diversity](https://www.electrical-installation.org/enwiki/Diversity_factor) (Coincidence factor definition; technical_guide); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Time-dependent power context; independent_physics) | Hypothetical operating profile is not a regulatory load calculation. |
| E025000-07 | Some practice uses word diversity factor for inverse ratio and also for multiplier less than one | [electrical-se-diversity](https://www.electrical-installation.org/enwiki/Diversity_factor) (Coincidence/diversity definitions and wording note; direct_publisher_text) | Single technical guide; be explicit about chosen convention. |
| E025000-08 | Electrical load requirements depend on duration, start transients and RMS heating | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Joule heating and power; physics); [electrical-osha304](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (Overcurrent and conductor ability to safely carry current; independent_us_regulation) | Specific motor loading and protective curves are product dependent. |
| E025000-09 | Feeder protective coordination and branch protective device selection are separate design questions | [electrical-osha304](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (1910.304(f) protection; regulatory_context); [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Feeder and branch definitions; same_authority_context) | Selective coordination curves and requirements are not proven for any specific system. |
| E025000-10 | 2026 NEC reorganizes branch feeder service load calculations into new Article 120 | [electrical-nfpa-2026-loads](https://www.nfpa.org/news-blogs-and-articles/nfpa-journal/2025/04/29/2026-nec-changes) (2026 NEC change discussion and Article 120 mention; primary_standards_publisher) | Publisher explanation verified, not full adopted code; 2023 edition differed. |
| E025000-11 | IEC 60364 Part 5-52 scope includes wiring systems, ampacity and voltage drop topics | [electrical-iec60364-552-2024](https://webstore.iec.ch/en/publication/103734) (Official catalogue summary for 2024 consolidated edition; publisher_scope_only) | Normative sizing clauses and local adoption not examined. |
| E025000-12 | Load controls can change coincidence only when operating constraints are reliable and recognized | [electrical-se-diversity](https://www.electrical-installation.org/enwiki/Diversity_factor) (Simultaneity concept; general_context); [electrical-nfpa-2026-loads](https://www.nfpa.org/news-blogs-and-articles/nfpa-journal/2025/04/29/2026-nec-changes) (Article 120 reorganizes load methods; us_standards_context) | Specific power-control-system allowances and reliability criteria not verified. |
| E025000-13 | Voltage drop and I^2R heating follow current and loop resistance | [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (Ohm law; physics); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Power dissipation; physics) | 0.15 ohm example is classroom idealization, not a wiring design. |
| E025000-14 | Balanced currents and nonlinear waveforms affect neutral loading in distribution | [electrical-se-neutral-sizing](https://www.electrical-installation.org/enwiki/Sizing_the_neutral_conductor) (neutral and harmonic sizing discussion; technical_guide); [electrical-fluke-harmonics](https://www.fluke.com/en-us/learn/blog/power-quality/installation-harmonics) (harmonics technical discussion; independent_vendored_context) | Actual sizing requires measured or calculated waveform and adopted rules. |
| E025000-15 | A panel schedule should preserve source, circuit function and reliable revision data | [electrical-doe-prints-v1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1016-93_VOL1.pdf) (Drawing/document revision practices; related_technical_guide); [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Feeder branch service meanings; independent_regulatory_vocabulary) | Suggested documentation practice, not a prescribed residential panel schedule. |
| E025000-16 | Inverter continuous power and available surge cannot be inferred from connected load alone | [electrical-doe-solar-design](https://www.energy.gov/cmei/systems/solar-photovoltaic-system-design-basics) (PV system and inverter design fundamentals; energy_guide); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Energy versus power; independent_physics) | Exact inverter capability and transfer topology require manufacturer specifications. |
