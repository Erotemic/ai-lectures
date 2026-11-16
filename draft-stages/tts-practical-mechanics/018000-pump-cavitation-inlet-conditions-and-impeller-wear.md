# 018000 — Pump Cavitation, Inlet Conditions, and Impeller Wear

<!-- BEGIN SPOKEN LECTURE -->

A pump that once ran quietly now sounds as though small stones are bouncing inside it. The flow may be low and the housing warmer than before. One possibility is cavitation: vapor bubbles form in a low-pressure region of the liquid and collapse as pressure rises. But not every rattling pump cavitates. Bearings, air ingestion, loose mounts, a damaged impeller, and operating far from the intended flow can sound similar. Understanding the inlet is the first step toward separating those causes.

## A pump does not create water at its inlet

A centrifugal pump uses a rotating impeller to add energy to liquid. The impeller accelerates and redirects the liquid, and the pump casing helps convert part of that energy into pressure. For the pump to operate reliably, water must reach its inlet at a pressure and flow compatible with the impeller's demands. A clogged suction strainer, a long narrow inlet, a partially closed valve, or excessive lift can reduce the available inlet pressure while the pump is trying to draw more liquid.

Every liquid has a vapor pressure that depends on temperature. If local absolute pressure falls sufficiently near that value, some liquid flashes into vapor. The bubbles then move toward higher-pressure regions and collapse. Repeated collapse can produce noise, vibration, performance loss, and pitted metal surfaces. The damage is not just from bubbles being visible in a pipe; it comes from their violent collapse and the localized stresses they create.

An important subtlety is that the ordinary gauge on a pump may read pressure relative to atmosphere. Cavitation depends on absolute pressure relative to the liquid's vapor pressure. A reading of minus a few pounds per square inch on a suction gauge is not directly the value to compare with vapor pressure without accounting for atmospheric pressure and measurement elevation. Temperature matters too: warmer water has a higher vapor pressure and a smaller margin against boiling under reduced pressure.

## Available head versus required head

Pump engineers express inlet margin with net positive suction head, or NPSH. The available NPSH comes from the actual installation: ambient pressure, elevation of the supply, suction losses, and liquid vapor pressure. Required NPSH is associated with a pump's behavior at a particular operating flow, obtained from appropriate manufacturer data. A real installation needs sufficient margin between them, not merely equality in an oversimplified calculation.

Consider two tanks. In the first, the pump sits below the tank's water surface, giving the inlet a favorable hydrostatic head. In the second, the pump stands above the water and must lift it through a long suction line with several elbows. All else equal, the second arrangement has less available inlet head. If a filter clogs or the water gets hotter, its margin may shrink further. This does not prove it is cavitating, but it gives an explanation for why symptoms appear after a change in conditions.

The pump curve tells another story. For a centrifugal pump, head developed typically varies with flow. The system curve describes how the piping and static elevations resist flow. Their intersection determines the operating point. A restriction downstream usually reduces flow; a restriction upstream can both change flow and depress inlet pressure. Throttling a discharge valve and throttling a suction valve are therefore not equivalent, even if both reduce measured delivery. Manufacturer recommendations govern the safe operating range and whether any throttling is permitted.

## Distinguish vapor cavitation from air ingestion

A suction-line leak may admit outside air when the line is below atmospheric pressure. Bubbles can then enter the pump without the local liquid pressure dropping to vapor pressure. The symptom may include loss of prime, unstable flow, air collecting at high points, or visible bubbles where a safe observation point exists. Entrained air can disrupt a pump and may accompany cavitation, but its remedy targets sealing, venting, and inlet arrangement rather than just raising inlet pressure.

A blocked discharge, worn impeller, failing bearing, or poorly aligned coupling can also give low output and vibration. Therefore, build evidence. Record pump speed, inlet and discharge conditions, water temperature, tank level, valve positions, filter condition, flow, motor current when appropriate, and the timing of the noise. Compare with the manufacturer curve. If the sound changes predictably as suction strainer loss increases or tank level falls, that pattern supports an inlet-related hypothesis. It remains a hypothesis until measured conditions and inspection corroborate it.

A familiar maintenance mistake is to replace a damaged impeller without correcting the inlet geometry that damaged it. A new impeller may restore performance briefly, then suffer the same wear. Another error is to oversize a pump to overcome low flow without examining the suction. A more powerful pump can demand more from an already inadequate inlet and worsen the problem.

## Diagnose without creating a hazard

Pumps may contain rotating shafts, hot liquids, pressurized lines, and stored electrical energy. Measurements should be made at designed service points with appropriate equipment; do not loosen a fitting on a running pressurized system to 'see whether there is air.' Any impeller inspection requires proper isolation, depressurization, cooling, and energy control. Do not reach through guarding or put a hand on a suspected rotating component.

Successful correction may involve a cleaned strainer, larger or shorter inlet piping, corrected tank placement, restored fluid level, proper air elimination, or selecting a pump whose operating range matches the real duty. If a damaged impeller is replaced, compare post-repair measurements at the same operating point. The goal is not merely a quieter sound, but adequate flow and inlet margin throughout expected conditions.

The pump is an effective teacher because it reveals a common engineering principle: the output is only as good as the supply conditions. Before blaming the machine that moves the fluid, understand what reaches it and at what pressure.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Key distinction.** Vapor cavitation involves local pressure below vapor pressure; air ingestion involves external gas entering the suction. They can coexist. Do not diagnose either from a recording of the noise alone.

**Illustrative NPSH balance.** NPSH_available ≈ (P_surface,absolute − P_vapor)/(ρg) + static liquid elevation above inlet − suction friction losses. Conventions, velocity head, and reference datum depend on the pump calculation. Use manufacturer required-NPSH data and safety margin.

**Trend log.** Flow, speed, temperature, tank level, suction absolute pressure, discharge pressure, strainer differential pressure, vibration, and noise chronology. Compare at consistent operating states.

**Safety and review.** Never open a pressurized or energized pump for a diagnostic shortcut. Pump configuration, margins, material choice, and operating point require model-specific engineering review.

## Selected reading and source locators (non-spoken)

- `doe-hi-pumping-sourcebook` — [US Department of Energy and Hydraulic Institute, Improving Pumping System Performance: A Sourcebook for Industry, Second Edition (2006)](https://www.energy.gov/sites/prod/files/2014/05/f16/pump.pdf). Pump and system curves, BEP, NPSH, pump selection and maintenance.
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `openstax-thermal` — [OpenStax College Physics 2e, §13.2: Thermal Expansion of Solids and Liquids](https://openstax.org/books/college-physics-2e/pages/13-2-thermal-expansion-of-solids-and-liquids). Linear thermal expansion, representative material coefficients, and holes expanding with heating.
- `osha-hazardous-energy` — [U.S. Occupational Safety and Health Administration, Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy/). Stored pneumatic, hydraulic and mechanical energy during servicing.
