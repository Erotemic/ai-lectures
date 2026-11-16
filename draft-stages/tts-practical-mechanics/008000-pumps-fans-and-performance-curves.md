# 008000 — Pumps, Fans, and Performance Curves

**Track:** Mechanical Systems and Repair. **Background:** friction, bearings, seals, motors, and fault diagnosis. **Purpose:** learn how a machine and its connected flow system determine one another's actual performance.

<!-- BEGIN SPOKEN LECTURE -->

# A pump does not choose its own flow rate

Imagine two identical water pumps installed in different circuits. One moves water freely through a short, wide pipe. The other pushes through a tall rise, narrow pipes, several valves, and a clogged strainer. A catalog may give each pump the same nominal capacity, yet their measured flow rates differ. The pump is not behaving mysteriously. Its performance is coupled to the resistance imposed by the rest of the system.

A pump adds mechanical energy to a liquid. A fan adds it to a gas. In both cases a rotating impeller can create a pressure difference and sustain flow, but the outcome depends on the machine's geometry, speed, fluid properties, and connected system. A performance curve represents this interaction more usefully than a single advertised flow number.

## What head means

For a liquid pump, head describes energy imparted per unit weight of fluid and is often expressed in meters or feet of liquid. It is closely related to pressure but not identical in every context, because elevation and velocity contributions can matter. The system must overcome static head, if any, plus frictional losses through pipes, fittings, and components. The static contribution can remain even at zero flow; friction generally increases as flow rises.

A centrifugal pump typically has a pump curve where available head declines as flow increases at a fixed speed and impeller diameter. The system curve often rises with flow because losses increase. Draw both on the same axes. Their intersection is the operating point. A valve partly closed downstream raises resistance and moves the operating point toward less flow. Replacing a clogged filter can reduce resistance and change operating flow without touching the pump.

Suppose a pump is said to deliver fifty liters per minute. Does that number apply against a two-meter lift or a twenty-meter lift? Is it for clean water or a viscous fluid? At what speed? The stated quantity is incomplete without a test condition. The same caution applies to fans rated in cubic feet per minute. A free-air rating may say little about delivery through restrictive ducts and filters.

## The efficiency island

A pump converts electrical input through motor and shaft into useful hydraulic power, but some energy becomes heat, turbulence, and friction. Its efficiency changes with operating point. A best-efficiency point, or BEP, is a region where a given centrifugal pump often runs with relatively favorable hydraulic behavior. Far from that region, recirculation, vibration, noise, and component wear may increase. The correct operating point still needs to satisfy the actual duty; maximizing theoretical efficiency while failing to deliver required flow is not a successful design.

For water, useful hydraulic power can be estimated from density multiplied by gravity, flow rate, and developed head. The input mechanical or electrical power must exceed the useful output when losses are present. If a motor draws large power yet produces little useful flow, the system may be badly matched, obstructed, or mechanically defective. Power alone does not identify the cause, but it belongs in the evidence.

## Speed changes everything, but conditionally

For a geometrically unchanged centrifugal machine operating in comparable conditions, approximate affinity relationships say flow varies with rotational speed, head with the square of speed, and power with its cube. These are scaling relations for corresponding operating states, not guaranteed predictions for every installed system. A large static head, changing efficiency, cavitation, or a controller that changes the operating point can make naive scaling misleading.

That qualification explains a common energy-saving idea. Reducing fan or pump speed can reduce power substantially when the application permits lower flow. Throttling flow with a restrictive damper or valve may waste energy as pressure loss. But a variable-speed drive must still keep the process within required flow, minimum speed, cooling, and safety limits.

## Cavitation and the suction side

A pump also depends on the pressure available at its inlet. If local pressure falls sufficiently for vapor bubbles to form, the bubbles can collapse as they move to higher-pressure regions. Cavitation can cause noise, vibration, erosion, and lost performance. The concept of net positive suction head distinguishes the margin available in the installation from what the pump requires. It is not enough to calculate discharge pressure while ignoring a long, undersized suction line or elevated liquid temperature.

Fans have their own unstable regions, and filters become more restrictive as they collect dust. A whining motor, rattling housing, rising operating temperature, or declining flow may indicate mechanical wear, but it may also reflect a changed system curve. Diagnose both sides of the coupling.

## A curve is a conversation between components

The most productive troubleshooting sequence records the intended flow and pressure or head; collects the measured duty under known conditions; inspects filters, valves, air paths, and inlet conditions; and compares the observations with a credible machine curve. If an impeller is damaged, the machine curve itself may have changed. If a valve is partly shut, the system curve has changed. Those hypotheses point to different repairs.

A pump and a fan are excellent lessons in systems thinking. Neither supplies an independent fixed flow just because a nameplate says it can. Performance emerges from a machine pushing against a network, and proper diagnosis asks what changed in the machine, the network, or both.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Curve sketch and calculation

Plot **head** (vertical) versus **flow** (horizontal). Draw a falling centrifugal pump curve and a rising system curve `H_system = H_static + k Q²` (approximation for many turbulent-flow systems). Mark their intersection.

For water, hydraulic power is `P_h = ρ g Q H`. Example: `Q=0.002 m³/s` and `H=15 m` gives `1000 × 9.81 × 0.002 × 15 ≈ 294 W` of useful hydraulic power. If efficiency at that point is 60%, shaft input is about `490 W`, before motor/drive losses. This is **not** a pump or electrical-service selection specification.

### Fault discrimination

| Symptom | Machine-side possibility | System-side possibility |
|---|---|---|
| Low flow | Worn impeller, wrong speed | Blocked filter, closed valve, excessive head |
| Cavitation-like noise | Inappropriate pump selection | Low inlet pressure, hot liquid, restricted suction |
| High vibration | Damaged bearings/imbalance | Operating far from stable region, poorly supported piping |

**Review boundary:** Use OEM curves and procedures for a real pump or fan. Fluid compatibility, electrical controls, suction conditions, and containment pressure require equipment-specific engineering review.

## Selected reading and evidence records (non-spoken)

- `doe-hi-pumping-sourcebook` — [US Department of Energy and Hydraulic Institute, Improving Pumping System Performance: A Sourcebook for Industry, Second Edition (2006)](https://www.energy.gov/sites/prod/files/2014/05/f16/pump.pdf). Pump and system curves, BEP, NPSH, pump selection and maintenance.
