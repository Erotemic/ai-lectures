# 011000 — Hydraulic Circuits, Valves, and Actuators

<!-- BEGIN SPOKEN LECTURE -->

A hydraulic jack can raise a vehicle with modest effort at its handle, but it cannot create energy. The operator moves a small volume of oil through a pressure-generating pump; the larger lifting piston converts pressure acting over area into a larger force, at the cost of moving a shorter distance. Hydraulics are an application of force, fluid continuity, and controlled resistance.

The simplest hydraulic system has a reservoir, a pump, a pressure path, a directional control, an actuator, and a return path. It may also have filtration, check valves, relief valves, pressure regulation, and thermal management. The fluid transmits force and carries power; the circuit determines what moves, when, and how fast. A drawing that labels only the pump and cylinder omits the components that make the motion predictable.

## Pressure is not the same as flow

Pressure measures force per unit area. A cylinder piston with effective area A under a pressure difference P can exert approximately P times A in the intended direction, neglecting friction and other losses. A larger piston produces more force at the same pressure, but to move it the same distance requires more fluid volume. Flow rate determines how quickly volume is delivered, so it strongly influences actuator speed. High pressure with near-zero flow may hold a load; substantial flow through a restriction can produce heat without useful movement.

Consider two cylinders connected to a pump, one with twice the effective piston area. Under the same pressure difference, the larger one can exert roughly twice the force, but it moves about half as fast under the same delivered volumetric flow. This simple comparison assumes similar motion direction and neglects rod area and leakage. It is a way of understanding the design tradeoff, not a complete equipment rating.

## Why valves make circuits intelligible

A check valve permits flow primarily in one direction, allowing a jack or accumulator to retain pressure in a designed state. A directional valve routes pressure to one side or the other of an actuator and provides an appropriate return path. A flow-control valve changes the restriction in a branch, affecting actuator speed. A pressure-relief valve limits excessive system pressure by opening a path when its set condition is reached. These functions are distinct even when packaged in one manifold.

The valve state must always be considered with the load. Imagine an elevated platform held by a cylinder. Moving a valve to neutral does not automatically make the platform safe: spool leakage, line rupture, thermal expansion, and load-induced motion may still matter. Counterbalance valves, load-holding valves, mechanical supports, and other safeguards are engineered for particular failure modes. Never treat hydraulic pressure alone as a positive mechanical lock when people are at risk.

## The pump sets a possible flow, not a guaranteed actuator behavior

A positive-displacement pump moves approximately a defined volume per shaft revolution, but actual output varies with speed, internal leakage, pressure, and wear. The required input torque rises with pressure for a given displacement. If a pump continues forcing fluid into a blocked circuit without suitable pressure control, pressure can rise dangerously. That is why relief and control arrangements cannot be omitted from a practical power unit.

A hydraulic motor reverses the mechanical role of the pump, turning pressure and flow into torque and rotation. In both directions, power is approximately pressure difference multiplied by volumetric flow, subject to efficiency. Frictional pressure losses, throttling, and internal leakage convert a portion of that power into heat. A system that becomes progressively hotter may be sending excessive power through an unwanted restriction or bypass path.

## Common failures have different signatures

Air trapped in a hydraulic system changes its apparent stiffness and can make motion spongy or erratic. A suction restriction can contribute to pump starvation or cavitation, where vapor bubbles form and collapse in damaging conditions. Contamination can erode valves and seals or cause a small spool to stick. An external leak loses fluid visibly; an internal leak may cause slow actuator drift or loss of performance without a wet floor.

Temperature affects viscosity and sealing. Cold oil may move sluggishly and cause greater pressure losses; overheated oil can reduce lubrication or seal life, depending on fluid and materials. A blocked return filter can alter circuit pressures. Replacing a leaking cylinder seal without evaluating rod damage, alignment, and contamination may reproduce the same failure. Hydraulic diagnosis requires observing the circuit under a known load, including pump speed, pressure, flow if measurable, and fluid condition.

## Stored energy changes the repair procedure

Pressurized oil, raised loads, springs, and gas-charged accumulators can store energy after a motor stops. A hose that appears motionless may still contain dangerous pressure. A tiny high-pressure jet can penetrate skin and cause a medical emergency, even if the wound looks small. Before servicing, correctly isolate sources, support loads mechanically, follow manufacturer depressurization procedures, and verify the state with appropriate equipment. Do not use a hand to search for leaks.

Hydraulics become manageable when you draw each boundary and energy store. Trace where fluid flows, where pressure is developed, where it is relieved, and what holds the load if any component fails. The same thinking transfers from a floor jack to an excavator, a power-steering system, and an industrial press: force comes from pressure over area, motion from fluid volume, and safe operation from the entire circuit rather than a powerful pump alone.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Core relationships

- Ideal cylinder force: \(F=\Delta p A\). For a cylinder extending with pressurized cap end, use actual effective area; rod-end annular area is smaller.
- Ideal speed: \(v=Q/A\); ideal hydraulic power: \(P=\Delta p Q\).
- Example: \(\Delta p=10\,\mathrm{MPa}\) across \(A=10\,\mathrm{cm^2}\) yields approximately \(10\,000\,\mathrm{N}\). To move at 0.01 m/s requires about 0.00001 m³/s (0.6 L/min), ignoring leakage. Check units carefully.

### Fault table

| Symptom | Distinguishing possibilities |
|---|---|
| Slow under load | Flow shortage, restrictions, internal leakage, pump wear |
| Spongy motion | Entrained air, compliant hoses, load behavior |
| Rapid heat buildup | Throttling loss, relief-flow bypass, poor cooling |
| Uncommanded drift | Valve leakage, cylinder bypass, external leakage, load-holding design |

### Safety and sourcing

Hydraulic energy requires support, isolation, manufacturer-specific pressure relief, and positive verification. Avoid touching suspected leaks under pressure; suspected injection injuries need emergency medical care. Source framing: fundamental fluid mechanics (Pascal/continuity and energy conservation), hydraulic power systems engineering, and manufacturer hydraulic circuit training materials; equipment operating limits are not inferred from the ideal equations.

## Selected reading and evidence records (non-spoken)

- `nfpa-fluid-power-curriculum` — [National Fluid Power Association, Fluid Power Curriculum and System Dynamics](https://www.nfpa.com/fluid-power-curriculum). Hydraulic pressure, flow, valves, actuators, energy balances and component concepts.
- `osha-hydraulic-injection-case` — [OSHA, Accident Report 120339.015: High-Pressure Hydraulic Injection Injury](https://www.osha.gov/ords/imis/accidentsearch.accident_detail?id=120339.015). Documented danger of high-pressure fluid injection through skin.
