# Diagnose starting, charging, and intermittent electrical faults

<!-- BEGIN SPOKEN LECTURE -->

# Diagnose starting, charging, and intermittent electrical faults

## Batteries, Charging, and Electrical Diagnosis

A car makes a clicking noise when someone tries to start it. The dashboard lights may appear normal, but the starter cannot turn the engine. The immediate temptation is to replace the battery. Sometimes that is exactly the repair required. Other times the battery is healthy but insufficient current reaches the starter because of a poor connection, an inadequate charging system, or another fault.

Electrical diagnosis begins with a simple principle: voltage measured with almost no current flowing can look healthy even when the system cannot deliver power under load. A weak battery has an elevated effective internal resistance or insufficient stored charge. A corroded terminal has added resistance in the connection. Both can create a large voltage drop when the starter draws substantial current. The location of that drop distinguishes them.

### Three different electrical jobs

In a conventional internal-combustion vehicle, the 12-volt lead-acid battery stores electrical energy and supplies high current for starting. The alternator or other charging system then supplies electrical loads and replenishes the battery when the engine runs. The starter motor draws electrical energy to rotate the engine. These roles interact, but they are not identical. A battery that goes flat after a night may be undercharged, failing to hold charge, or repeatedly drained by an electrical load when the vehicle is off.

A battery is rated by several characteristics. Capacity describes how much charge it can supply over time under specified test conditions. Cold-cranking performance characterizes high-current starting ability in the cold. Terminal voltage depends on state of charge, temperature, recent charging, and load. A single resting-voltage reading is a clue, not an exhaustive battery health assessment.

Modern vehicles complicate the story. Some use controlled alternator output, battery management, stop-start systems, and auxiliary batteries. Hybrid and electric vehicles may use a DC-to-DC converter to maintain the low-voltage system from a high-voltage traction battery. Their control strategies and service requirements differ. Measuring the nominal 12-volt bus does not give permission to inspect or open high-voltage components.

### Why voltage drop matters

Ohm's law makes the mechanism concrete. Suppose a connection develops only five hundredths of an ohm of resistance. At a modest current of one ampere, the drop is just five hundredths of a volt. At two hundred amperes, the same resistance would produce a ten-volt drop and two kilowatts of heat if maintained under those simplified conditions. Real starting current and connection heating change during the event, but the example shows why a terminal that seems electrically continuous can fail during starting.

A loaded voltage-drop test compares voltage across parts of the circuit while current flows. Excessive drop across a ground connection points toward a different repair from excessive drop inside a battery or across a positive cable. Likewise, a low system voltage with the engine running does not automatically prove a failed alternator; control strategy, load, connection condition, and measurement location matter.

### Reading the sequence of events

Ask four questions. What is the battery's state before starting? What happens to voltage during the starting attempt? What happens after the engine starts and the charging system engages? And does charge remain when the vehicle is parked? These observations separate an initial energy-storage problem from a delivery problem, a replenishment problem, and an unintended load.

Imagine that the battery is charged and passes an appropriate load test, but the starter barely turns. A high-resistance cable or ground becomes more likely. Imagine instead that starting improves after external charging but the battery soon becomes discharged during normal operation. The charging system or a continuous electrical load deserves investigation. Or suppose the vehicle starts normally after daily use but fails after sitting a week. An abnormal parasitic current draw, an aging battery, or adverse temperature conditions could be involved.

Battery terminals also corrode physically. Clean conductive connections are essential, but visible corrosion should prompt a search for damaged terminals, inappropriate fastening, and possible electrolyte leakage. A wire that is bright at its exposed tip may be corroded inside insulation. Visual inspection and electrical measurement are complementary.

### Safety belongs to the circuit model

Lead-acid batteries can supply enormous short-circuit currents and contain corrosive electrolyte. Charging can generate explosive gas under certain conditions. A tool bridging a positive terminal and grounded metal can create serious heat, burns, and fire. Jump-starting requires the correct manufacturer procedure, especially on modern vehicles with designated connection points or battery management systems. The lesson is not to avoid electrical measurement; it is to treat stored energy and the physical return path as real.

An efficient diagnostic process does not start with purchasing the part whose name appears in the symptom. It separates storage, generation, load, wiring, and control. Replace the component only after the observations support that diagnosis, and verify that the repair restores the expected behavior under a realistic load. That approach is useful in vehicles, motor equipment, and almost every low-voltage electrical system.

## Diagnosing Intermittent Electrical Faults

An electrical path can appear normal during one test and fail under another condition, so intermittency requires its own evidence plan.

A car's headlights dim for a fraction of a second as it crosses a pothole. The dashboard display resets, but the engine keeps running. The driver takes the vehicle to a workshop, where everything works normally. Intermittent electrical faults are difficult precisely because the evidence often disappears before anyone can measure it. The solution is not to replace whichever component is most associated with the symptom. It is to build a test that can capture the failure when it occurs.

Vehicle electrical systems are networks of power, ground, switching devices, sensors, actuators, and communication modules. A fault may interrupt the source voltage, create excessive resistance at a connection, open a signal wire, or confuse several modules through a shared ground or communication fault. Modern vehicles also contain software that logs some problems but not all of them.

### Start with the pattern

A reset over bumps suggests movement-related behavior, but it does not uniquely identify a loose battery terminal. A connector, ground strap, fuse holder, relay contact, or harness damaged near a mounting point may also change resistance as the body flexes. A failure only after the engine has warmed may indicate a heat-sensitive semiconductor, relay, winding, or expansion at a connector. A fault after rain can point toward water ingress, but condensation and operating conditions must also be considered.

Write down the state when the problem occurred: temperature, engine speed, road condition, speed, wet or dry weather, which electrical loads were active, and exactly which systems failed together. A single lost audio speaker and a simultaneous dashboard reset are very different patterns. Shared symptoms help locate shared dependencies, while a fault confined to one component points closer to its branch.

### Use circuit theory, not a parts catalog

Ohm's law describes the voltage drop across a resistance when current flows. In a healthy low-resistance connection, the voltage drop is small at the intended load. Suppose a corroded connector develops an extra resistance of one tenth of an ohm. At twenty amperes, that creates a two-volt drop and dissipates forty watts in the connection. The joint may heat and degrade further. Under almost no load, a high-impedance voltmeter could still read near normal battery voltage and miss the problem.

This explains why loaded voltage-drop measurements can be more informative than a continuity beep on a disconnected wire. Measure across the suspected connection while the relevant circuit is operating, using the vehicle's approved diagnostic procedure and appropriate instrument limits. A meter that reports “voltage present” at an open connector has not proved that the circuit can deliver useful current.

A ground path deserves equal attention. Modules sharing a high-resistance ground may show failures that appear unrelated. Testing only positive wires can miss a return-path defect. A wiring diagram identifies intended common points; physical inspection determines whether those points are actually intact and free of corrosion.

### What diagnostic codes can and cannot tell us

An onboard diagnostic trouble code identifies a condition the vehicle detected under a particular monitoring rule. It may indicate an out-of-range signal, a communication timeout, or an emissions-system condition. A code is not automatically a verdict that the named part is defective. A low-voltage episode can create several secondary codes. A sensor may report a real process fault caused by wiring, mechanical conditions, or another module's behavior.

Preserve available freeze-frame and event information before clearing codes. If possible, compare the time order of multiple codes. The first meaningful event is often more informative than the largest number of downstream complaints. Some intermittent faults leave no useful stored code, particularly if the monitor never reached its enabling conditions.

A scan tool that records live data can reveal sudden changes in supply voltage or sensor readings while the fault occurs. But sampled data may be too slow to capture a millisecond dropout. An oscilloscope, logger, or carefully chosen min/max measurement can be needed for brief events. The instrument must be connected and secured in a way that does not interfere with driving or expose anyone to moving components.

### Reproduce without creating new hazards

Controlled diagnosis changes one variable at a time: electrical load, temperature, connector movement in a stationary service setting, or a measured circuit path. A random “wiggle test” performed near belts and fans with the engine running is not a method worth imitating. Do not repeatedly disable safety-critical circuits on public roads to reproduce the symptom. High-voltage traction systems in hybrids and electric vehicles require specialized isolation, equipment, and qualifications.

When a repair is made, document the original failure evidence, the replaced or reworked connection, and the final loaded measurement. Confirm that the component works in the conditions that originally caused trouble. One successful ignition cycle is weak evidence for a fault that formerly appeared once every week. Monitoring may be needed over multiple cycles with clear observations.

The strength of electrical diagnosis is that a hidden fault still has consequences somewhere: a voltage drop, an absent current, a missing signal, a lost message, or an unexpected reset. We make progress by identifying where the consequence begins, then narrowing toward the cause. The most efficient repair is often the one that prevents a second round of guessing.

## Starting Circuits, Parasitic Draw, and Battery Health

A vehicle starts reliably after a highway drive but struggles after sitting for three days. The first instinct may be to replace the battery. That might solve the immediate symptom, but it would not tell us whether the battery is worn out, the charging system is failing to replenish it, or some circuit remains awake while the vehicle is parked. All three can produce a low battery voltage when the next start is attempted. The diagnosis begins by separating energy storage from energy use.

### The battery is an energy reservoir with limits

A common starting battery is designed to supply a very high current for a short time. The starter motor must overcome engine friction and compression, so its current demand rises sharply during cranking. Voltage at the battery terminals drops under this load because the battery has internal resistance and because chemical processes cannot respond instantaneously without loss. A weak battery may look acceptable with no load, then collapse under starting demand.

State of charge and state of health are not the same. A battery may be temporarily discharged but otherwise healthy; recharging restores it. An aged battery may have lost capacity or gained internal resistance, so it performs poorly even when charged. Cold conditions can make the starting problem more demanding because the engine is harder to turn while battery chemistry delivers less available current.

Nominal voltage does not reveal everything. Measuring a rested battery under controlled conditions can inform state-of-charge assessment for a given chemistry, but batteries can retain surface charge after a drive. A voltage test shortly after charging differs from one after a rest. Battery conductance or load testing can provide additional information when conducted using a suitable procedure and rating.

### Trace the starting path

When the driver requests a start, a control circuit commands a high-current path through a starter relay or solenoid. The starter motor draws current through large positive and return conductors. A corroded terminal, damaged ground strap, or failing contact can introduce resistance into this path. Because the current is high, even a small resistance can create a significant voltage drop and substantial heat.

Imagine a connector with only twenty milliohms of added resistance. At two hundred amperes, Ohm's law predicts a four-volt drop across it. That is enormous in a nominal twelve-volt system. The same resistance dissipates eight hundred watts while the current flows. The short cranking interval may prevent sustained heating, but the electrical performance can be severely affected. This is why measuring voltage drops under the actual load can reveal a connection problem that is invisible to a no-load continuity test.

A slow starter can therefore result from an exhausted battery, excessive starter demand, mechanical engine resistance, or voltage lost in connections. The sound alone does not determine which.

### Charging is another subsystem

With the engine running, an alternator or other charging architecture supplies electrical power and replenishes the battery under the vehicle's control strategy. Modern vehicles may vary charging voltage intentionally. A single fixed 'correct alternator voltage' is not a reliable diagnostic rule for every model and operating state. A charging system can fail through belt slip, wiring resistance, temperature-dependent faults, failed components, or misinterpreted current sensors.

A battery that dies after parking may have been inadequately charged before shutdown. To test that possibility, examine the charging system under conditions specified for the particular vehicle and verify the battery's condition first. Otherwise a parasitic-draw test can be performed on an already unhealthy energy reservoir and produce misleading conclusions.

### What 'parasitic draw' actually means

Cars consume some electrical power while parked. Memory, remote-entry receivers, security functions, and control modules may remain partially active. Many vehicles go through a staged sleep sequence: a module remains awake for a period after a door closes, then reduces its consumption. Opening a door or connecting a scan tool can wake the network again. If we measure current immediately after shutdown and assume it is the stable parked load, we may mistake ordinary transition behavior for a fault.

Parasitic current is measured in amperes; battery capacity is often stated in ampere-hours. If a persistent load is one hundred milliamperes, that is one tenth of an ampere. Over forty-eight hours, the simple arithmetic gives four point eight ampere-hours of consumption. This does not directly tell us how many starts remain. Starting requires adequate terminal voltage under very high current, available capacity depends on temperature and battery condition, and a battery cannot necessarily deliver its entire rated capacity in that use.

Some faults produce intermittent draw rather than a constant one. A glovebox light may stay on. A relay may remain energized. A control module may repeatedly wake others through the communication network. An aftermarket accessory may fail to enter standby mode. The clues come from timing, event history, and controlled comparisons.

### A diagnostic plan that avoids creating the fault

Record when the failure occurs, battery age and type, charging history, climate, aftermarket accessories, and any recent repairs. Test the battery state and performance. Inspect the high-current cables and grounds. Observe charging behavior using the vehicle-specific procedure.

If parked current is being investigated, allow the modules to enter their documented sleep state, preserve door and hood latch conditions as appropriate, and monitor the circuit without disrupting the system. Disconnecting a cable or removing a fuse can itself wake modules, reset learned state, and erase the event pattern. Some procedures use a current clamp or a carefully installed shunt so measurement does not interrupt power. The method must be appropriate to the vehicle and instrument.

If current rises intermittently, correlate the change with a module, light, relay, or external trigger. A good diagnosis identifies the circuit responsible and why it remains active; it does not merely keep removing fuses until a number drops once. The final test is whether the vehicle reliably starts after the parked interval that previously exposed the fault.

The battery, starter, cables, alternator, and parked electronics form one energy system. A disciplined diagnosis asks where energy is stored, where it is lost, and what condition reveals the loss. Replacing parts without separating those questions may hide the symptom while leaving its cause in place.

## Starting and Charging Faults Across Hot and Cold Conditions

Temperature changes provide another controlled comparison for the same starting-and-charging system.

A car turns over sluggishly on a freezing morning, then starts normally that afternoon. Another starts when cold but refuses after a short hot stop. A third has a new battery yet drains it after a week of short trips. These stories sound like 'battery trouble,' but the electrical and mechanical causes can differ. Temperature changes the battery, the engine, and the connections, and the charging system may be doing exactly what its controller commands.

### What starting asks of the system

In a conventional combustion-engine vehicle, a starter motor must deliver enough torque to turn the engine through compression and internal friction. The battery supplies a large current over a short period. Cold temperatures generally reduce the useful power a lead-acid battery can deliver, while cold lubricant can make the engine harder to turn. Both effects push in the wrong direction on a winter morning. A starter circuit that was barely adequate in mild weather may become visibly weak in cold weather.

The starting system includes far more than the battery case. Current travels through cable connections, contactors or solenoids, the starter motor, and return paths through ground straps and the engine or chassis. A small resistance in a corroded or loose connection can create a substantial voltage drop when hundreds of amperes flow. An open-circuit battery reading after the car has been parked may look respectable while the voltage at the starter collapses under load.

That is why diagnosis should not rely on a single voltage number. The test conditions matter: state of charge, battery temperature, cranking load, cable condition, and the specified battery test procedure. A conductance or load test can characterize a battery, but a bad terminal or cable can still keep a healthy battery from delivering power to the starter. Conversely, replacing dirty terminals will not restore capacity to a severely degraded battery.

### Hot starting is a different experiment

A hot engine is not simply the same engine with a warmer battery. Engine-management sensors, fuel delivery, injectors, starter heat, and electrical connections can behave differently after heat soak. Some mechanical components expand and change clearances. A marginal starter or solenoid may operate cold and fail hot. A temperature-sensitive electronic component can interrupt the crank request or fuel control. The fact that the battery is warm does not prove that the battery is the cause or that it cannot be involved.

First separate **no crank** from **crank but no start**. If the starter does not rotate the engine, investigate permission to crank, battery and starter circuits, and mechanical constraints. If the engine cranks briskly but does not fire, the cause may lie in fuel, ignition, compression, sensors, or control logic. The distinction avoids changing a battery to address a fuel-related hot-start fault. Record what lights and sounds were present, engine temperature, whether the starter engaged, and whether the symptom disappears after cooling.

### Charging is no longer a simple fixed voltage

An alternator or other charging device restores energy used during starting and supports the vehicle's electrical loads while the engine runs. Many modern vehicles adjust charging voltage and alternator loading according to battery state, temperature, operating conditions, or fuel-economy strategy. A voltage reading that differs from an old textbook's nominal value is not automatically a failed alternator. The vehicle-specific service data and control mode determine what to expect.

Charging performance also has to be measured under appropriate conditions. A failing belt drive, loose cable, damaged alternator, or control fault can cause inadequate charging. Yet an extended sequence of short trips can leave even a functioning system unable to replenish repeated starting losses and accessory use. A battery kept at partial charge may age differently from one maintained appropriately. 'The alternator tested good once' and 'the battery is always fully charged' are not the same statement.

When charging diagnostics involve engine-running measurements, moving belts, fans that can start unexpectedly, and high-current electrical connections change the hazard. Probing methods must protect both the technician and electronics, and hybrid and electric vehicles add high-voltage architectures that should not be treated as conventional 12-volt starter systems.

### Use time and temperature as clues

A repeatable cold-only symptom supports a different list of hypotheses from a hot-only symptom. Record ambient temperature, time parked, trip duration, battery age and type, accessories used, starter behavior, and warning indicators. If available, note whether the vehicle reports a battery-management or charging-system fault. Intermittent no-start problems benefit from recording evidence while the fault is actually occurring, before a restart or tow changes conditions.

Imagine a vehicle that starts poorly after three frosty nights. Its owner replaces the battery, and the symptom improves temporarily. But the car continues making only five-minute trips with a seat heater, blower, and window defroster active. Weeks later the symptom returns. The owner now has to distinguish insufficient charging opportunity, parasitic load while parked, battery condition, and poor electrical connections. Replacing the battery again without examining the energy balance may repeat the same repair.

A useful test plan can compare battery state after a full, appropriate charge; cranking behavior; and charging operation after an adequate driving or service interval. But a multimeter's voltage reading alone cannot reveal every battery defect or battery-management decision. Avoid guessing exact cutoff voltages without the test specification.

The lesson is to treat starting as a short, high-power demand and charging as an energy-replenishment system. Cold changes available starting power and mechanical load; heat can reveal intermittent faults; short trips and stored electrical loads change state of charge. A good diagnosis keeps these mechanisms separate until evidence links them.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Batteries, Charging, and Electrical Diagnosis

**Track:** Automotive and Small-Engine Maintenance. **Background:** engines and motors, lubricants, braking, and diagnostic codes. **Purpose:** understand starting, charging, and voltage-drop diagnosis without treating a battery as an isolated component.

#### Technical companion (non-spoken)

##### Loaded connection example

`V_drop = I R`. At `I = 200 A` and hypothetical `R = 0.05 Ω`, `V_drop = 10 V`, `P = I²R = 2,000 W`. This illustrates why **connection resistance** must be evaluated under load; it is not a normal acceptable cable resistance or a recommended test load.

##### Diagnostic evidence ledger

| Observation | Hypothesis supported | Competing explanations |
|---|---|---|
| Good rest voltage, poor crank | Delivery drop or battery internal weakness | Starter mechanical fault |
| Starts after charge, later weak | Poor charging, excessive resting load, battery deterioration | Very short trips/cold temperature |
| Voltage differs across cable while cranking | Resistance in that path | Probe placement or transient readings |

**Review boundary:** Use vehicle-specific service procedures, proper measurement methods, and protective equipment. Do not apply ordinary 12 V diagnostics to high-voltage traction circuits, or infer a universal alternator charging-voltage threshold for smart-controlled vehicles.

#### Selected reading and evidence records (non-spoken)

- `openstax-ohms-law` — [OpenStax, College Physics 2e, 20.2 Ohm's Law: Resistance and Simple Circuits](https://openstax.org/books/college-physics-2e/pages/20-2-ohms-law-resistance-and-simple-circuits). Voltage drop I × R, resistive heating and limitations of linear Ohm model.
- `sae-dtc-j2012-2025` — [SAE Vehicle E E System Diagnostic Standards Committee, SAE J2012_202509: Diagnostic Trouble Code Definitions (2025)](https://saemobilus.sae.org/standards/j2012_202509-diagnostic-trouble-code-definitions). Standardized DTC definitions; standards page abstract, full text may require purchase.

### Diagnosing Intermittent Electrical Faults

### 013000 — Diagnosing Intermittent Electrical Faults

#### Technical companion (non-spoken)

##### Worked loss

A connection with `R = 0.1 Ω` at `I = 20 A` has `V_drop = I R = 2 V` and `P = I²R = 40 W`. This is an explanatory example, **not** an acceptable voltage-drop specification; actual limits depend on the circuit and manufacturer.

##### Evidence sheet

Symptom; simultaneous module effects; road/weather/load/temperature conditions; available DTCs and freeze frames; wiring diagram version; measured loaded supply/ground drops; test time resolution; repair performed; conditions repeated to verify. Preserve codes before reset.

**Editorial boundary:** Electrical repairs around airbags, restraint systems, high-voltage propulsion, and moving machinery require manufacturer-specific safety procedures. Do not probe unknown terminals or clear codes merely to make a warning light disappear.

#### Selected reading and evidence records (non-spoken)

- `openstax-ohms-law` — [OpenStax, College Physics 2e, 20.2 Ohm's Law: Resistance and Simple Circuits](https://openstax.org/books/college-physics-2e/pages/20-2-ohms-law-resistance-and-simple-circuits). Voltage drop I × R, resistive heating and limitations of linear Ohm model.
- `sae-dtc-j2012-2025` — [SAE Vehicle E E System Diagnostic Standards Committee, SAE J2012_202509: Diagnostic Trouble Code Definitions (2025)](https://saemobilus.sae.org/standards/j2012_202509-diagnostic-trouble-code-definitions). Standardized DTC definitions; standards page abstract, full text may require purchase.
- `nhtsa-maintain-vehicle` — [National Highway Traffic Safety Administration, Maintain Your Vehicle: Vehicle Safety Checklist](https://www.nhtsa.gov/sites/nhtsa.gov/files/hs810732.pdf). Vehicle service records, tire/fluids/light checks and owner manual priority.

### Starting Circuits, Parasitic Draw, and Battery Health

### 014000 — Starting Circuits, Parasitic Draw, and Battery Health

#### Technical companion (non-spoken)

##### Worked electrical examples

- Series connection resistance `R = 0.020 Ω` at cranking current `I = 200 A`: `V_drop = I R = 4 V`, `P = I²R = 800 W` during the load interval.
- Continuous parked consumption `I = 0.10 A` for 48 h consumes `4.8 Ah` nominally; actual state-of-charge and start capability are not directly inferable from this alone.
- Battery measured immediately after charging may carry surface-charge effects. Use a chemistry- and model-appropriate evaluation procedure.

##### Fault tree

Slow cranking: weak/discharged battery → cable/ground voltage drop → starter demand or mechanical drag. Battery discharges while parked: inadequate recharge → persistent or intermittent parked load → battery capacity/health. Record tests *under specified conditions*.

**Review boundary:** Modern electrical architectures, high-voltage hybrid/EV systems, and battery-management procedures require model-specific service instructions. Avoid interrupting power or wiring test meters into high-current paths without appropriate methods and protection.

#### Selected reading and evidence records (non-spoken)

- `openstax-ohms-law` — [OpenStax, College Physics 2e, 20.2 Ohm's Law: Resistance and Simple Circuits](https://openstax.org/books/college-physics-2e/pages/20-2-ohms-law-resistance-and-simple-circuits). Voltage drop I × R, resistive heating and limitations of linear Ohm model.
- `nhtsa-maintain-vehicle` — [National Highway Traffic Safety Administration, Maintain Your Vehicle: Vehicle Safety Checklist](https://www.nhtsa.gov/sites/nhtsa.gov/files/hs810732.pdf). Vehicle service records, tire/fluids/light checks and owner manual priority.

### Starting and Charging Faults Across Hot and Cold Conditions

### 015000 — Starting and Charging Faults Across Hot and Cold Conditions

#### Technical companion (non-spoken)

##### Fault classification

| Observation | Main decision |
|---|---|
| Starter silent / click / no rotation | Was crank request permitted? Battery path, starter and engine condition |
| Starter slow when cold | Battery cold-cranking performance, connection drop, oil/engine load |
| Starter cranks normally but engine will not fire | Fuel, ignition, engine control and sensor mechanisms |
| Failure only after hot soak | Temperature-dependent contacts, starter/solenoid, control and fuel/ignition |
| Repeated low state of charge | Trip energy balance, charging control, parked parasitic loads, battery aging |

Illustrative power identity: `P = I × V`; connection loss approximately `P_loss = I² × R` for a resistive path. Under high starter current, small added resistance matters.

**Service boundary:** Battery testing, voltage-drop procedure, charging targets, jump-start methods and hybrid/EV distinctions are manufacturer-specific. Do not work near exposed rotating or high-current parts without suitable procedures.

#### Selected reading and source locators (non-spoken)

- `nhtsa-winter-battery` — [U.S. NHTSA, Winter Weather Driving Tips: Prepare Your Vehicle](https://www.nhtsa.gov/winter-driving-tips). Cold weather reduces battery power and engine starting can require more power; service system check.
- `nhtsa-maintain-vehicle` — [National Highway Traffic Safety Administration, Maintain Your Vehicle: Vehicle Safety Checklist](https://www.nhtsa.gov/sites/nhtsa.gov/files/hs810732.pdf). Vehicle service records, tire/fluids/light checks and owner manual priority.
- `openstax-ohms-law` — [OpenStax, College Physics 2e, 20.2 Ohm's Law: Resistance and Simple Circuits](https://openstax.org/books/college-physics-2e/pages/20-2-ohms-law-resistance-and-simple-circuits). Voltage drop I × R, resistive heating and limitations of linear Ohm model.
