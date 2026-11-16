# 012000 — Hydronic Heating: Pumps, Loops, Radiators, and Balancing

<!-- BEGIN SPOKEN LECTURE -->

In a house heated by hot-water radiators, one room is too warm and another never reaches its set temperature. The boiler is running. The supply pipe feels hot. Does that mean the boiler is too small? Not necessarily. The problem may lie in how heat is being moved from the heat source to the rooms.

Hydronic heating uses liquid, usually water or a treated water mixture, as a transport medium. A heat source warms the water. A circulator drives it through pipes and heat emitters. The water releases energy to indoor air and surfaces, then returns cooler to be reheated. Radiators, baseboards, and embedded radiant floors are different ways of delivering that energy. Their operating temperatures and response times may differ markedly.

## Water carries energy by changing temperature

A hydronic loop transfers useful heat at a rate controlled by mass flow and temperature difference. In simplified steady operation, heat transfer equals mass flow times the water's specific heat capacity times the temperature drop through the emitters. Increase flow while preserving the same temperature difference, and more heat would be transported; in a real system, the temperature difference itself usually changes with flow and room conditions. The point is to think in terms of water moving energy, not merely whether the water feels hot.

Imagine two identical rooms with identical radiators, except that one loop receives little flow. The inlet to that radiator may be hot while much of its surface stays relatively cool. A large temperature difference across a radiator can indicate low flow, but it also depends on load and emitter design. Conversely, a very small supply-return temperature difference does not automatically mean the system is healthy; there could be high flow with inadequate heat extraction or limited temperature difference at the heat source.

## The circulator works against a hydraulic system

A circulator supplies pressure difference to drive flow through the resistance of pipes, elbows, valves, heat exchangers, and emitters. In a closed, filled loop, the pump does not ordinarily have to continuously lift the full building-height column of water; static head largely balances around the loop. It must overcome frictional and component pressure losses and sustain stable operation. In an open or improperly filled system, or one with air and unsuitable pressure, the picture changes.

Pumps have performance curves. The operating point emerges from the pump curve and the system resistance curve. A larger pump is not automatically better: unnecessary high flow can create noise, erosion concerns, control instability, and electrical consumption. Too little flow can prevent heat delivery or cause temperature limits to be reached. Pump and system selection requires actual design data.

## Parallel branches and balancing

Suppose a manifold supplies three radiator branches. If one branch is short and unobstructed while another is long with many fittings, the branches do not necessarily receive equal flow. Flow tends to favor lower-resistance paths. Balancing valves add controlled resistance where needed so design flow can be distributed among emitters. Closing every easy branch at random may appear to warm a cold room but can cause other problems. Commissioning is based on the intended heat load, emitter capacity, pipe layout, and available measurements.

Zone valves and individual circulators serve different arrangements. A zone valve may open or close one branch while a common pump serves several branches; multiple pumps may serve circuits with different characteristics. Controls need to handle what happens when only one zone calls, when all zones close, and when a heat source requires minimum flow. There are hydraulic design patterns such as bypasses, variable-speed circulators, or hydraulic separation that address these issues, but they are not interchangeable parts chosen by guesswork.

## Pressure, air, and expansion matter

As water heats, it expands. A closed hydronic system uses an appropriate expansion device and pressure-control components so temperature changes do not produce uncontrolled pressure rise. A gauge reading should be interpreted in the context of the specific boiler and system, not compared blindly with somebody else's home. Air can collect at high points or in poorly vented emitters, interrupting flow, making noise, or reducing effective heat transfer. Air elimination, fill pressure, and circulation interact.

A technician facing a cold radiator might investigate whether its supply and return connections are functioning, whether a valve is closed, whether air is present, whether the pump is moving water, or whether another branch is taking most of the flow. The evidence should drive the next measurement. A hot boiler and a cold room do not by themselves identify the failed component.

## Radiant systems have different dynamics

An embedded floor has thermal mass. It may take longer to change room temperature than a finned baseboard, and its surface temperature must be controlled within the assembly's design limits. Mixing valves and outdoor-reset controls are ways to manage water temperature when a heat source and emitter require different operating conditions. A boiler may use higher water temperatures than a low-temperature radiant circuit; supplying one circuit directly from the other without understanding the design can create comfort or material problems.

Diagnostic reasoning is most effective when it separates heat generation, heat transport, and heat release. Is the source delivering energy? Is the water flowing through the intended paths? Are the emitters releasing enough heat to match each room's loss? Then examine controls, measurements, and system states that distinguish these stages.

Hydronic heat is not complicated because the water has mysterious properties. It is complicated because heat transfer, pump behavior, branch resistance, expansion, and controls are coupled. Once those parts are separated conceptually, room-by-room differences become tractable engineering questions rather than invitations to replace the boiler.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Useful equations

- Heat carried by loop: `Q_dot = m_dot * c_p * (T_supply - T_return)` (steady-state idealization, consistent units).
- Circulator input and hydraulic output are different; efficiency and system resistance matter.
- Closed-loop static lift and friction head must be distinguished; pump selection uses its curve and the network resistance.

### Symptom matrix

| Observation | Possible causes | Check context |
|---|---|---|
| One cold emitter, other rooms heat | Air, valve state, branch restriction, poor balance | Branch temperatures, actual flow evidence |
| Many zones heat poorly | Source temperature, circulator, shared flow fault | Supply/return and pump states |
| Piping noise | Air, excess velocity, poor restraint, pressure transient | Timing with valves and pump transitions |
| Pressure climbs substantially when hot | Expansion control, fill/pressure fault | Manufacturer limits and qualified hydronic assessment |

**Editorial boundary:** Pressure-vessel, combustion, scalding, and electrical components have equipment-specific requirements. No generalized pressure or temperature setpoint is asserted. Avoid treating a warm pipe as proof of safe circulation or relief operation.

## Selected reading and evidence records (non-spoken)

- `ashrae-residential-hydronics` — [ASHRAE, 2023 Handbook Fundamentals, Chapter 1 Residential Space Conditioning: Hydronic Heating Systems](https://handbook.ashrae.org/handbooks/A23/IP/a23_ch01/a23_ch01_ip.aspx). Hydronic terminal units, forced circulation and zone/manifold arrangements.
- `doe-ba-hvac-renovation-guide` — [U.S. Department of Energy Building America, Energy Renovations: HVAC, a Guide for Contractors (2011)](https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/hvac_guide.pdf). Hydronic heating distribution and zoning examples.
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.
