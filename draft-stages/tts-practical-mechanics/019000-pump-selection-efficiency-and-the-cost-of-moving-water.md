# 019000 — Pump Selection, Efficiency, and the Cost of Moving Water

<!-- BEGIN SPOKEN LECTURE -->

A pump that is too small may not deliver enough water. A pump that is much larger than necessary can also perform poorly, running far from its preferred operating point while throttles, bypasses and control cycles waste energy. To choose intelligently, we need to understand that the pump and the pipes together determine the flow. Neither one determines it alone.

The pump has a performance curve. For a centrifugal pump at a particular speed and impeller size, the curve shows how much head the pump can develop at different flow rates. Head is energy per unit weight of fluid, commonly expressed as an equivalent height of liquid. It is a way to compare pressure rise and elevation change in a common unit. The system has its own curve: how much head it needs to move each flow rate through the actual pipework, valves, filters and static elevation difference.

The operating point is where those two curves intersect. If we install a different pump or change the piping resistance, the operating point changes. This is why a pump's advertised maximum flow and maximum head cannot usually be achieved simultaneously. They tend to be opposite ends of its performance curve.

## A system that changes with demand

Consider a small circulation system with a pump pushing water through several branches and a heat exchanger. The elevation changes may largely cancel around a closed loop; much of the required head comes from friction and fittings. Contrast that with a well pump lifting water to a tank above it: the elevation change is a real static component of head. In both systems, pipe friction grows with flow, but their system curves have different shapes and offsets.

Now add a filter. As it accumulates material, its pressure drop at a given flow may increase. The system curve becomes steeper; the same pump moves less water. A technician who observes low delivered flow should not conclude that the pump motor is failing without checking filters, closed valves, air pockets and suction conditions. Replacing the pump can leave the true restriction in place.

Cavitation is another limit. If liquid pressure at the pump inlet becomes too low relative to its vapor pressure, bubbles can form and collapse through the pump, damaging the impeller and reducing performance. Net positive suction head, abbreviated NPSH, describes the available and required suction conditions in a more careful way than a vague instruction to 'keep the inlet open.' Available NPSH depends on absolute inlet pressure, fluid vapor pressure, elevation and losses. Required NPSH is a pump characteristic given for stated conditions. A pump selected near the edge of adequate suction conditions may fail even if its advertised head and flow seem sufficient.

## Efficiency has more than one layer

There is hydraulic power transferred to the liquid, mechanical shaft power delivered to the pump, and electrical power consumed by the motor and drive. These are not equal because each conversion incurs losses. The useful hydraulic power is fluid density times gravitational acceleration times volume flow rate times head, in consistent units.

Suppose water flows at two liters per second through a pump delivering twenty meters of total head. Two liters per second is 0.002 cubic meters per second. With water density approximated as one thousand kilograms per cubic meter, the hydraulic power is about 392 watts. If the hypothetical combined pump-and-motor efficiency is fifty percent, electrical input would be about 784 watts. These numbers are not specifications for a real pump. They show why we must distinguish the energy delivered to water from the energy purchased at the meter.

A pump can be mechanically healthy and still use excessive electricity when operated at an inefficient point. Centrifugal pump curves commonly identify a best efficiency point. That is not a guarantee that the entire installed system reaches the same efficiency. Pipework, controls, motor selection, suction conditions and operating schedules all matter. A pump that frequently runs at half the desired flow through a nearly closed throttling valve may merit a control or system redesign rather than just a new impeller.

## Choose the control method to fit the demand

For a variable-flow application, a variable-frequency drive can change pump speed and shift its performance curve. Under restricted conditions, fan and pump affinity relationships help explain how flow, head and power change with speed. They are approximations with assumptions, not an unconditional promise that reducing speed by ten percent will save an exact percentage of power in every installation. Static lift and changing system demands can defeat a simplistic scaling argument.

Other systems use on-off cycling, staging multiple pumps, a bypass or a pressure-regulating valve. The correct choice depends on required minimum flow, pressure limits, motor cooling, tank size and process needs. A domestic well system, for example, must coordinate the pump, pressure switch or controller, and pressure tank. Excessive cycling can shorten equipment life, but reducing cycle count by allowing improper pressure excursions would not be an improvement.

## Diagnose with a small set of simultaneous measurements

A useful field record includes the pump model, impeller and speed if known, electrical input, inlet and discharge pressures, flow, fluid temperature, filter condition and operating mode. Each pressure should be interpreted relative to the gauge location and elevation. A snapshot taken with the system fully open cannot be compared blindly with a later reading during throttled operation.

Imagine a pump that draws its normal motor current but delivers less flow than last month. Possibilities include a restricted suction screen, a partially closed valve, an air leak, an eroded or damaged impeller, a changed system resistance, or an instrumentation error. Head and flow measured together help distinguish these cases. A low current on some centrifugal pumps may accompany low flow, not proof that the motor has become more efficient. Electrical current by itself is not a reliable hydraulic diagnostic.

If efficiency is the question, compare measured electrical power with a carefully estimated useful hydraulic output, and account for the motor and drive. Verify that the measurement methods are appropriate before calculating a single percentage. Use the manufacturer's performance data to see whether the operating point lies in a reasonable part of the curve. Check whether the energy cost is significant enough to justify changes, and whether the process tolerates them.

Pump selection is therefore a matching problem. A good pump is not the pump with the largest number printed on its box. It is the pump whose curve meets the real system's needs over the operating range, with adequate suction margin, acceptable efficiency and controllable performance.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Power calculation.** `P_hydraulic = rho * g * Q * H`; for water at 1000 kg/m³, `Q=0.002 m³/s`, `H=20 m`, `P≈392 W`. At an illustrative 0.50 combined efficiency, `P_electrical≈784 W`. Include realistic fluid properties, gauge elevations, motor/drive losses and test uncertainty before using this on real equipment.

**Curve exercise.** Sketch a falling centrifugal pump head curve and a rising system curve. Show how a clogged filter moves the intersection to lower flow, how increased static lift offsets the system curve, and how a pump speed change shifts the pump curve.

**Safety/limits.** Pressure systems and rotating equipment carry stored-energy, injection, electrical and entanglement hazards. Use rated ports and suitable instruments. NPSH and efficiency must come from manufacturer curves or validated tests; do not infer from motor current alone.

**References.** U.S. DOE, *Improving Pumping System Performance: A Sourcebook for Industry*; DOE Better Plants, *Pumps*; Hydraulic Institute system-curve and pump-performance methods.
