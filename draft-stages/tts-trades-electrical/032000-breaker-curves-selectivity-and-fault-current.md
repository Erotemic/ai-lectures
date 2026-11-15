# 032000 - Which Breaker Trips? Time-Current Curves, Selectivity, and Fault Current

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** hypothetical time-current graphs, device data sheets, fault-loop models and coordination studies.

<!-- BEGIN SPOKEN LECTURE -->

# Which Breaker Trips? Time-Current Curves, Selectivity, and Fault Current

A fault develops in a machine at the far end of a workshop. The machine has a branch breaker. The workshop has a feeder breaker. The building has a main breaker. Which one will open?

You might expect the nearest breaker to the fault to operate and the other two to remain closed. That is a sensible design goal, but it is not a consequence of the drawing alone. A pair of breakers labeled twenty amperes and one hundred amperes does not guarantee that the smaller one always clears first.

The question belongs to *protection coordination*: choosing and evaluating protective devices so that they interrupt faults within their capabilities, protect conductors and equipment, and, where required, preserve supply to unaffected circuits. It joins several things that are often taught separately: fault current, trip behavior, interrupting capacity, and the energy released before a circuit is disconnected.

## Current is not enough; we need time

A protective device does not simply answer yes or no to the question, Is the current above the printed rating? Many overcurrent devices have time-dependent behavior. A moderately elevated current may be tolerated for a period that depends on its magnitude. A severe short circuit may trigger a much faster response. The protection characteristic is therefore a relationship between current and operating time.

For a circuit breaker, this is represented by a time-current characteristic, often on logarithmic axes. The horizontal axis is current. The vertical axis is time. Depending on design, there may be a long-time region responding to sustained overloads, a short-time region, and an instantaneous region intended for high fault currents. Thermal, magnetic and electronic trip mechanisms implement these functions in different ways.

A manufacturer often presents not a perfectly thin line but a band. Tolerances, temperature, prior heating, settings and manufacturing variation mean that operation is expected within a range. A drawing with just one ideal trip point is a teaching simplification. Actual selection must use the characteristics of the exact devices and settings.

Fuses also have current-dependent melting and clearing behavior. Their time-current information may distinguish pre-arcing or melting time from total clearing time. A fuse and a breaker therefore cannot be compared merely by matching their nominal ampere labels.

## What fault current is available?

A protective device cannot be selected only from the normal running current of a motor or a building's demand estimate. It also sees the current that a fault could produce. A low-impedance supply and a fault near the source can create a very large prospective short-circuit current. Farther down a long cable, the additional conductor and source impedance may reduce the current considerably.

For a deliberately simplified single-phase fault loop, the rough relationship is current equals the driving voltage divided by the total fault-loop impedance. Imagine a one-hundred-twenty-volt source and a hypothetical loop impedance of zero point one two ohms. The simple quotient is one thousand amperes. If another scenario has one point two ohms, the quotient is one hundred amperes. This is a model, not a breaker-sizing calculation: real faults include source regulation, reactance, arcing, transformer behavior, conductor temperature and different possible fault paths.

Those two values reveal a design tension. The *maximum* prospective fault current matters because the device must safely interrupt the available current at its installation point. The *minimum* prospective current matters because a distant or high-impedance fault must still be cleared in the time needed to protect the circuit and people. A breaker that can interrupt a huge fault is not necessarily guaranteed to operate promptly for a weak one.

Schneider Electric's installation guide makes this maximum-versus-minimum distinction explicit in its discussions of short-circuit levels and protection. The original device manufacturer supplies the actual trip characteristics and interrupting capabilities; the guide supplies a method of reasoning about them.

## Interrupting rating is not the same as trip setting

Consider a breaker marked with a fifteen-ampere operating rating and a separate interrupting rating expressed in thousands of amperes. These numbers answer different questions. The operating rating belongs to the circuit's intended continuous and overload behavior under specified conditions. The interrupting rating describes the device's tested ability to open a fault current of a stated magnitude at the applicable voltage and conditions.

A device may attempt to trip at a current that exceeds what it can interrupt safely. That is why the prospective fault current and the installation voltage must be compared with the applicable interrupting rating. OSHA's U.S. workplace regulation requires equipment intended to interrupt fault current to have an interrupting rating sufficient for current available at its line terminals. The rule has an occupational scope, but the engineering distinction is much broader.

There is another rating nearby that should not be silently conflated with interrupting capacity: the short-circuit current rating of an equipment assembly, often abbreviated S-C-C-R. A motor controller or industrial control panel may have an assembly rating governed by more than the breaker inside it. The protective device's own interrupting rating does not, by itself, assign an equal short-circuit rating to every assembly in which it is installed.

International standards use their own definitions and tests. IEC 60947-2 is a circuit-breaker standard for specified low-voltage switchgear applications, with terms such as ultimate and service short-circuit breaking capacities. North American equipment markings and IEC categories cannot be translated by relabeling the numbers without considering the standards and application conditions. The publisher's public abstract establishes scope; it is not a substitute for those detailed tests.

## Selectivity is a promise about a range, not about labels

Return to the branch and feeder breakers. Coordination aims to let the downstream device interrupt a fault while the upstream device remains closed. In a time-current graph, one seeks appropriate separation between the devices' operating regions, accounting for the applicable characteristics and tolerances.

At modest overload currents, the smaller downstream device may have a much shorter trip time. But at large short-circuit currents, both devices may enter their instantaneous regions. If their operating bands overlap, there may be no reliable way to predict that only the downstream device operates. A larger rating on the upstream breaker does not fix this automatically.

Engineers distinguish *total selectivity* over a specified fault-current range from *partial selectivity* up to a stated limit. Manufacturer coordination tables may establish combinations that achieve selectivity in circumstances where a simple visual comparison of curves would not, particularly with current-limiting devices and dynamic energy behavior. That manufacturer evidence is part of the design, not an optional decoration.

Sometimes continuity of service is worth the complexity of adjustable trips, intentional delays, or communication between protection devices. In other cases, a simple architecture is better. Hospitals, essential safety systems and industrial processes may have different continuity obligations from an ordinary residential circuit. The correct coordination objective follows the load, the source, the jurisdiction and the consequence of interruption.

A conceptual example shows why the range matters. Imagine that a downstream breaker clears a one-hundred-ampere fault in approximately a tenth of a second, while the upstream device takes several tenths of a second. That suggests selective operation at that current. At two thousand amperes, suppose both devices are in fast-acting regions. The earlier timing comparison tells us almost nothing about selectivity at the higher fault level. We need the actual curves, energy-limiting behavior and tested coordination data.

## The energy tradeoff behind delay

Why not simply make every upstream device slower? Because the circuit experiences fault energy while the device waits to clear. A simplified measure of thermal stress is the integral of current squared over time, often written I squared t. For a constant-current example, one thousand amperes for one hundredth of a second gives ten thousand ampere-squared seconds. One hundred amperes for one second gives the same numerical I-squared-t value. This comparison describes an electrical stress measure, not equal arc-flash injury, equal equipment damage or an approved clearing time.

Conductors and equipment withstand fault energy according to material, geometry, heat transfer, starting temperature and short-circuit duration. Electrodynamic forces and arcing introduce further phenomena. Introducing a trip delay to improve selectivity can therefore increase downstream thermal or incident-energy exposure. Protective coordination must balance interruption speed, selectivity, device withstand capability and the system's consequences of losing power.

A current-limiting device can change the picture by limiting the let-through peak current and energy relative to an unrestricted prospective fault. But its behavior is specific to the model and application. A series-rated combination or a manufacturer-tested coordination pairing should never be imagined from two independently printed nameplate values.

## Different sources make different faults

The earlier examples assumed a relatively stiff supply. But a system can be supplied from the grid, a transformer, a generator, an uninterruptible power supply, or an inverter. Their short-circuit behavior may differ greatly. An inverter's current control can limit fault current to a fraction of what a utility transformer could deliver at the same nominal voltage. A generator may provide a large initial current that decays with time. Protective devices that work predictably with one source might behave differently after a transfer to another.

The sensible method is to characterize the credible operating modes and fault locations. What is the maximum available fault current at each device? What is the minimum fault current at the remote ends? Which devices respond, with which actual settings, and what happens to the protected conductors before disconnection? What continuity requirements must be met? A selective coordination study answers these questions with a documented source model and device data, not with the superficial order of breaker ampere ratings.

## A protection diagram is a model of decisions

A one-line diagram shows the devices in electrical order. A time-current study shows how they behave through time. A short-circuit study supplies the currents to which the curves are applied. An equipment schedule gives the actual ratings and approvals. A reliability plan tells us which outages matter. All four belong together.

A designer who understands these relationships can explain why a small branch fault sometimes trips the building main, why an upgraded utility transformer may force a review of interrupting ratings, and why a long circuit can fail to produce the instantaneous current imagined by a simplified diagram.

The important distinction is between *clearing a fault safely* and *clearing only the nearest device*. Both can be objectives. Neither follows automatically from a breaker label. Coordination is the engineering of their relationship across the currents, sources and times that the system can actually experience.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### A simple two-device picture

Model a radial supply as `source -> upstream breaker A -> feeder -> downstream breaker B -> load`. Assume a fault beyond B. The design objective may be that B operates within its applicable clearing limit while A remains closed. At some high currents both may operate; therefore selectivity must be stated **up to which prospective fault current**, with tested pairing data or actual time-current curves.

### Three different current checks

| Quantity | What it asks | Typical evidence |
|---|---|---|
| Normal and overload current | Does the protective device protect the conductor and tolerate intended loads? | Loads, cable ratings, device characteristics |
| Maximum prospective short-circuit current | Can equipment safely interrupt or withstand the largest credible fault? | Source/transformer impedance, upstream system, manufacturer ratings |
| Minimum prospective fault current | Will the protection clear a remote/high-impedance fault sufficiently promptly? | Longest relevant loop, temperature/source assumptions, trip characteristics |

A calculated prospective current is not an installation approval by itself.

### Toy-model arithmetic

Assume `U = 120 V` and a simplified real fault-loop impedance `Z`:

- `Z = 0.12 Ω` gives `I = 1000 A`.
- `Z = 1.2 Ω` gives `I = 100 A`.

Do not substitute these figures for measurements or short-circuit studies. The actual calculation uses proper source impedance, voltage, phase configuration, asymmetry and fault models.

At fixed current, define simplified fault thermal stress `J = ∫ i(t)² dt`. For `1000 A` during `0.01 s`, `J = 10,000 A²s`; for `100 A` during `1 s`, `J = 10,000 A²s`. Equal values of `J` do **not** imply equal arc energy, electromechanical force, cable temperature or person exposure.

### What a time-current curve cannot establish alone

A curve needs device type, setting, tolerances, fault-current reference and upstream/downstream pairing. Current-limiting and series-tested schemes may require manufacturer-specific data beyond simple band separation. Assembly SCCR, breaker interrupting rating and downstream cable thermal withstand are separate checks.

### Exercise: partial or total selectivity? (desk)

A hypothetical pair of breakers is selective for prospective currents from `100 A` through `800 A` according to a manufacturer table, but a study finds a possible downstream short-circuit current of `1.8 kA`. What can you conclude? **Only** that the claimed data support selectivity through `800 A`; behavior at `1.8 kA` requires additional device-specific evidence. The correct next action is to request tested combination data or another coordinated design, not to infer that the nominally smaller breaker will win.

### Context: which standards actually govern?

IEC 60947-2:2024 was developed under IEC TC 121/SC 121A; the public publisher page verifies product scope and edition, not each device's applicable Icu/Ics figure. OSHA 29 CFR 1910.303(b)(4) states the interrupting-rating obligation for covered U.S. workplace installations. Actual breaker selection also depends on product listing, local adopted regulations, equipment markings and the particular supply arrangement.

## Claim-level source map

| Claim ID | Consequential statement | Specific source support | Boundaries / review |
|---|---|---|---|
| E032000-01 | Overcurrent protective devices have current-versus-time characteristics; nominal amperes alone do not specify clearing | [electrical-se-coordination](https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers) (current/time/energy selectivity; engineering_guide); [electrical-se-min-shortcircuit](https://www.electrical-installation.org/enwiki/Calculation_of_minimum_levels_of_short-circuit_current) (clearing at minimum fault current; same_publisher_related_guide) | Exact bands, instantaneous regions and fuse conventions are device-specific |
| E032000-02 | Time-current characteristics involve tolerances and actual settings | [electrical-se-coordination](https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers) (time-based and current-based selectivity; engineering_guide) | No specific product setting or band claimed |
| E032000-03 | Maximum available fault current at installation governs interrupting rating | [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (1910.303(b)(4) interrupting rating; primary_workplace_rule); [electrical-ul-sccr-machinery](https://www.ul.com/resources/determining-short-circuit-current-rating-sccr-machinery) (available fault current relative to machine supply; independent_equipment_explainer) | OSHA applies to covered workplaces; actual equipment may use other standards |
| E032000-04 | Minimum fault current at far/high-impedance points must still operate protection within design limits | [electrical-se-min-shortcircuit](https://www.electrical-installation.org/enwiki/Calculation_of_minimum_levels_of_short-circuit_current) (minimum Isc versus trip characteristic and conductor withstand; engineering_guide); [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (1910.303(b)(5) circuit impedance and characteristics; independent_workplace_principle) | Source, wiring, temperature and time behavior all matter |
| E032000-05 | Simple fault-loop models use I≈U/Z; adding impedance can greatly reduce prospective current | [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (§9.4 Ohm’s law and resistance; physics); [electrical-se-min-shortcircuit](https://www.electrical-installation.org/enwiki/Calculation_of_minimum_levels_of_short-circuit_current) (loop-impedance fault-current models; independent_engineering_application) | AC, arcing and changing source conditions complicate actual values; worked numbers hypothetical |
| E032000-06 | Interrupting rating is not the operating ampere rating or a guarantee of total installation protection | [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (1910.303(b)(4); workplace_rating_rule); [electrical-ul-sccr-machinery](https://www.ul.com/resources/determining-short-circuit-current-rating-sccr-machinery) (assembly rating and fault current; independent_product_context) | Device rating must match voltage, waveform and specific listing |
| E032000-07 | An equipment assembly SCCR is different from the interrupting rating of a breaker within it | [electrical-ul-sccr-machinery](https://www.ul.com/resources/determining-short-circuit-current-rating-sccr-machinery) (machinery/panel SCCR and available fault current; UL_product_guidance) | UL reference focuses on industrial machinery and 2021 NFPA 79; must not generalize code jurisdiction |
| E032000-08 | IEC 60947-2:2024 is a particular IEC circuit breaker product standard developed under TC121/SC121A | [electrical-iec60947-2-2024](https://webstore.iec.ch/en/publication/66277) (publisher page, title/edition/TC and scope; publisher_scope_only) | Publisher abstract only; not full Icu/Ics clauses or national acceptance |
| E032000-09 | Protection selectivity is total or partial over specified fault-current ranges | [electrical-se-coordination](https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers) (Principles of Selectivity: total versus partial; engineering_guide) | Only manufacturer-verified combinations establish a particular limit |
| E032000-10 | Two breakers with different normal-current ratings are not guaranteed selective at high fault current | [electrical-se-coordination](https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers) (total/partial, instantaneous and energy-based selectivity; engineering_guide); [electrical-ul-sccr-machinery](https://www.ul.com/resources/determining-short-circuit-current-rating-sccr-machinery) (series-rated combinations require acceptable paired equipment; separate_UL_context) | Instantaneous overlap, energy-limiting and series systems may need actual pairing evidence |
| E032000-11 | Trip delay changes downstream I²t stress and can trade speed against selectivity | [electrical-se-coordination](https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers) (time-based selectivity and short-time delays; engineering_guide); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (power and energy proportional to I²R; physics_model) | Equal I²t does not prove equal incident energy or thermal damage |
| E032000-12 | Different utility/generator/inverter source modes can change fault currents and device behavior | [electrical-se-coordination](https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers) (selectivity checked for grid or generator modes; engineering_guide); [electrical-se-min-shortcircuit](https://www.electrical-installation.org/enwiki/Calculation_of_minimum_levels_of_short-circuit_current) (source/fault current dependence; same_publisher_related_guide) | Specific generator/inverter limits unverified without equipment data |
| E032000-13 | A short-circuit study, time-current curves, ratings and critical-load objectives answer separate parts of protection design | [electrical-se-coordination](https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers) (principles and applications of protection selectivity; engineering_guide); [electrical-ul-sccr-machinery](https://www.ul.com/resources/determining-short-circuit-current-rating-sccr-machinery) (assembly SCCR separate from breaker selection; independent_product_context) | Not a substitute for a complete coordination/incident-energy design |
