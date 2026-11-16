# 016000 — Gearboxes, Lubrication, and Thermal Limits

<!-- BEGIN SPOKEN LECTURE -->

A geared machine runs smoothly for ten minutes and then begins to whine. Its housing is hot. The operator adds more oil, assuming friction is the cause. Sometimes insufficient lubrication does cause severe wear, but a gearbox can also run hot because it has *too much* lubricant, a misaligned shaft, a damaged bearing, an overloaded output, contaminated oil, or poor heat rejection. To investigate, first understand where the mechanical energy goes.

## What a gearbox actually transforms

A gear train transfers rotation between shafts. An ideal reduction gearbox turns a faster, lower-torque input into a slower, higher-torque output. Neglecting losses, the power is approximately the same at both ends. If speed is reduced by a factor of four, torque can increase by a factor of four. In a real gearbox there are losses: gear-tooth contact, bearings, seals, churning of lubricant, and sometimes ventilation or other auxiliary work. The difference between input and useful output becomes heat.

Suppose a machine draws one kilowatt of mechanical input and the gearbox transfers ninety percent of it to the load. The remaining one hundred watts of loss is heat generated within or around the transmission. That may sound small, but the housing can become hot if it cannot pass heat to surrounding air quickly enough. A heavy casting warms slowly; once hot, it may remain hot long after the machine stops. Thermal limits are therefore linked to duty cycle, ambient conditions, oil properties, and the housing's ability to reject heat—not simply the rated power stamped on the motor.

Gears produce force at their tooth contact points. Tooth geometry and bearing arrangement create radial and sometimes axial loads. A damaged bearing can increase friction and shift the meshing alignment. Excessive backlash can cause impacts, while inadequate backlash or distorted shafts can cause binding. A new lubricant cannot correct a shaft that is no longer held on the intended centerline. Likewise, a gear ratio that produces sufficient nominal torque may still overload the transmission during repeated starts and jams.

## Lubrication is a controlled film

The purpose of lubricant is not merely to make a surface feel slippery. In many operating conditions, a fluid film separates moving surfaces and carries load through pressure in the lubricant. At low speed, during startup, or under very high load, the contact may move into mixed or boundary lubrication, where surface chemistry and wear resistance matter more. Viscosity must therefore match operating temperature, speed, load, and gearbox design.

Oil that is excessively viscous at startup can resist movement and increase churning losses. Oil that becomes too thin at operating temperature may not sustain the needed film. An unsuitable additive package may be incompatible with certain materials or applications. Gearbox oil is not always interchangeable with engine oil or hydraulic fluid. Use the manufacturer's lubricant specification, not a guess based on thickness or color.

Oil level also matters. In a splash-lubricated gearbox, the rotating parts carry lubricant toward critical contacts. Too little oil starves them; too much may increase churning, aeration, leakage, and heat. A sight glass, dipstick, or level plug gives information only when used in the intended orientation and operating state. Filling to the top because 'more is safer' can create a new fault.

## Diagnose heat and noise as patterns

When did the noise appear? Does it occur only under load, at a particular input speed, when cold, or after the oil warms? A tooth defect often produces a periodic effect related to shaft or gear-mesh frequency, while bearing defects, imbalance, and loose mounts have different signatures. The sounds may overlap. Changes in vibration, housing temperature, output performance, lubricant condition, and current draw can help separate causes, but no single inexpensive sensor can identify every fault.

A thermal trend is useful when measurement conditions remain consistent. A surface temperature of fifty degrees Celsius may be acceptable for some designs and concerning for others. The key is the stated rating and how temperature changes with load and ambient conditions. Measure at repeatable locations, document duty cycle, and avoid touching hot rotating equipment. Infrared measurements on shiny metal can be misleading because emissivity varies. Do not use a thermometer reading alone to declare a gearbox safe.

Look at the lubricant without assuming its appearance tells the whole story. Water may cause cloudiness, corrosion, and poor film performance. Metal particles can signal wear; their size and composition matter. Foaming can indicate aeration, contamination, or level problems. A drain magnet or oil analysis program can supply evidence. Fresh oil might temporarily reduce noise while concealing ongoing damage; it is not proof that the mechanism was repaired.

## Model the surrounding machine

A gearbox is part of a larger system. A tight belt, poorly aligned coupling, bent shaft, or jammed driven component can load the gearbox beyond its intended operating condition. Before disassembly, inspect the coupling and mounting arrangement, look for looseness or soft foot, and confirm that output motion is not obstructed. Make those observations with the machine in a controlled state; unexpected startup and stored energy must be addressed before hands or tools approach drives.

Record the exact gearbox identifier, ratio, rated duty, oil specification, fill quantity, operating position, load, runtime, and prior changes. Compare that evidence against manufacturer limits. If the machine is outside rated load or temperature, changing bearings without fixing the underlying cause may simply start another short failure cycle.

The broader lesson is that heat in a transmission is a symptom of energy not reaching the useful output. Lubrication is one way to manage that loss, while alignment, load, speed, and cooling determine how much loss is generated and whether the machine can tolerate it. The diagnosis begins with the full mechanical path, not the oil bottle.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Illustrative balance:** `P_heat = P_input − P_output`. At `P_input = 1 kW` and assumed efficiency 90%, `P_heat ≈ 100 W`. Actual gearbox efficiency depends strongly on mechanism, ratio, speed, load, and thermal regime.

**Observations:** input/output speed; duty cycle; estimated load; gearbox ID and oil grade; oil level at manufacturer-specified condition; vibration/noise relative to speed; housing temperature and ambient; leaks, froth, water or particles; neighboring coupling alignment. Compare trends under repeatable loads.

**Diagnostic branches:** rising heat and noisy gears can involve lubricant starvation or excess, misalignment, load, tooth damage, bearing damage, or cooling limitation. Neither color nor temperature alone identifies a cause.

**Safety and scope:** Isolate hazardous energy and allow safe temperature before intrusive checks. Manufacturer-rated oil and service intervals control; do not substitute a general viscosity or fill instruction.

## Selected reading and source locators (non-spoken)

- `mit-gear-ratios` — [Martin Culpepper, MIT OpenCourseWare 2.72 Elements of Mechanical Design, Lecture 12: Transmission Ratios for Serial Gears](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/83d81a6f63d1c6f0fb775c08b207bc51_MIT2_72s09_lec12.pdf). Tooth-count and series gearing ratio derivations.
- `skf-grease` — [SKF Evolution, Grease Lubrication Mechanisms in Rolling Bearing Systems](https://evolution.skf.com/us/grease-lubrication-mechanisms-in-rolling-bearing-systems/). Grease churning, replenishment, starvation and film breakdown.
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
- `osha-hazardous-energy` — [U.S. Occupational Safety and Health Administration, Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy/). Stored pneumatic, hydraulic and mechanical energy during servicing.
