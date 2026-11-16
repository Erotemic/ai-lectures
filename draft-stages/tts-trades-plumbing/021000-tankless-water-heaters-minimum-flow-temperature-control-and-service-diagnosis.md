# 021000 — Tankless Water Heaters: Minimum Flow, Temperature Control, and Service Diagnosis

<!-- BEGIN SPOKEN LECTURE -->

A homeowner replaces a storage water heater with a tankless unit. The shower works when it is wide open, but the kitchen faucet occasionally runs cold at a small trickle. Someone suggests increasing the heater's temperature. Another person blames the gas supply. To diagnose the complaint, we need to understand that a tankless heater is not a hot-water tank with different packaging. It is a heat exchanger and control system responding to a moving stream of water.

A storage heater maintains a quantity of hot water even when no tap is running. A tankless heater typically detects demand, enables its heat source and transfers heat to water while the flow continues. That means flow rate is both a signal to the control and a major part of the thermal load. A tiny stream may be below the unit's activation threshold. A very large stream may exceed the heat that can be added at the requested temperature rise.

## Flow and temperature rise are coupled

The basic energy accounting is straightforward. The faster water passes through the heater, the more thermal power is needed to raise its temperature by a given amount. If incoming water is very cold, the required temperature rise is larger. A unit that can supply several gallons per minute of pleasantly warm water in summer may deliver fewer gallons at the same setpoint in winter.

Consider a heater receiving water at forty-five degrees Fahrenheit and delivering it at one hundred twenty degrees. The required rise is seventy-five degrees. At two gallons per minute, the heating rate is about seventy-five thousand British thermal units per hour transferred to the water, before allowing for device efficiency. At four gallons per minute it is twice that. A heater has a finite maximum capacity. The controller may reduce delivery temperature or limit flow depending on its design and operating conditions.

But low flow causes a different problem. Many tankless units require a minimum flow to start firing, and a smaller, sometimes different threshold to remain firing. The numbers are model-specific. A manufacturer's minimum activation flow is not a universal plumbing specification. If a low-flow faucet draws less than the starting threshold, the heater can remain idle while cold water flows through it.

## Follow the complaint through the whole system

A useful diagnosis begins with an observation table: which fixture, hot only or mixed, what flow, how long until temperature changes, and whether other fixtures are operating. A shower mixing valve can alter the hot-side flow through the heater even when the total water flow seems high. Opening cold water farther at the shower can reduce the hot-side demand below a threshold. A clogged aerator or scale-blocked shower head can have the same effect.

If every hot-water fixture has weak flow, the shared piping, main supply, inlet strainer or heater may be involved. If only one has trouble, investigate its supply stop, cartridge, aerator and mixing behavior before blaming the central appliance. If the unit displays a flow reading, compare it to a safely measured volume-over-time test at the fixture. An inexpensive pitcher and timer can reveal whether the true flow is half the expected amount.

A tankless heater also has a control sequence. When demand begins it may confirm water flow, fan or combustion status for a gas model, ignition, flame supervision, temperature sensing and ongoing safe operation. Electric models have different power circuitry, but still have flow sensing and thermal controls. Diagnostic codes and service measurements must be interpreted in the context of the actual model. Resetting a fault repeatedly is not diagnosis.

## Why temperature can swing

Intermittent hot-water use can leave a slug of cooled water in the piping. When the tap is opened, previously heated water may reach the user first, followed by cooler water from the line while the new heating cycle begins. This is one mechanism behind what manufacturers call a cold-water sandwich. Long pipe runs, recirculation arrangements and rapidly cycling taps can make the experienced temperature pattern more complicated.

Another common issue is trying to use a very high heater setpoint while mixing in large amounts of cold water at the shower. Depending on the mixing valve and flow, the heater sees a smaller hot draw than the user expects. Conversely, a too-low setpoint cannot compensate for high simultaneous load and large winter temperature rise. The response should follow measured flow and temperature, not merely a hotter numerical setting. Excessively hot delivery introduces scald risk and conflicts with safe fixture-temperature design.

## Scaling, maintenance and the inlet conditions

Water hardness can create mineral deposits in the heat exchanger and restrict transfer or flow over time. Strainers can collect sediment. Combustion equipment depends on adequate air, venting and fuel conditions; electric equipment on suitable power delivery. These are distinct diagnostic branches. A home water treatment system upstream might reduce scaling, but it is not proof that the heat exchanger needs no maintenance. Manufacturer maintenance schedules and water-quality limits govern the appliance.

Imagine a winter case: two bathrooms simultaneously demand hot water, and both go lukewarm, but either works individually. This pattern suggests insufficient available heating capacity at the combined flow and cold inlet temperature. It does not, by itself, establish an ignition failure. Now imagine a single faucet runs cold at trickle flow while a shower remains hot: here activation flow and local restrictions are much more plausible first checks.

The useful mental model is a controlled heat exchanger with a minimum operating threshold, a maximum heat input, and sensors that must agree about demand and safe operation. Measure fixture flow, inlet and outlet temperatures, simultaneous demand and unit status. Then follow the manufacturer's diagnostic path. That approach turns an intermittent complaint into testable causes rather than a sequence of guessed replacements.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

**Energy balance:** Heat delivered to water, in BTU/h approximately `500 × flow(gpm) × temperature rise(°F)` for ordinary water and typical conditions. Example: 2 gpm × 75°F × 500 = 75,000 BTU/h of heat delivered to the water. Appliance fuel or electrical input will be higher depending on efficiency.

**Test plan:** Record cold inlet temperature, outlet setpoint, hot-only fixture flow, mixed fixture behavior, simultaneous draw, time history at a tap, and displayed status/fault. Do not treat published ignition thresholds for one model as applicable to another.

**Boundary:** Fuel combustion, venting, electrical connections, descaling process, anti-scald settings and pressure protection are appliance- and code-specific. Follow manufacturer service procedures and qualified service requirements. Do not disable safety switches to reproduce a symptom.

**Sources:** US DOE, *Measure Guideline: Transitioning to a Tankless Water Heater* (including cycling behavior); Rinnai residential FAQ (model-specific illustrative activation and sustaining flow rates); US DOE Energy Saver demand water heating pages.
