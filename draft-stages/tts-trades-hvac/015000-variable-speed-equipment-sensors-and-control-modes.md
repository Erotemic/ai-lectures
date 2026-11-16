# 015000 — Variable-Speed Equipment, Sensors, and Control Modes

<!-- BEGIN SPOKEN LECTURE -->

Two heating systems can deliver the same amount of heat over a winter day while behaving very differently. One runs at full output, shuts off, and starts again when the room cools. Another adjusts its output for long periods, matching the building's changing load. If the second system runs almost continuously, that may be exactly what it is designed to do. Diagnosing variable-speed HVAC equipment begins by abandoning the assumption that 'running' and 'not running' are the only useful operating states.

## Capacity is an adjustable quantity

In a simple fixed-capacity air conditioner or heat pump, the compressor operates at roughly its intended on-speed while a thermostat requests heating or cooling. Capacity is managed by runtime: more minutes on, more energy moved. Systems with staged compressors offer a few discrete capacities. Inverter-driven systems can vary compressor speed over an operating range; variable-speed indoor fans and electronic expansion valves may coordinate with it. The controller's objective is not usually maximum instantaneous heat flow. It is adequate comfort, stable operation, and efficiency under the equipment's limits.

There are still boundaries. Every compressor has a usable speed range; a unit cannot keep lowering output indefinitely. At very small building loads it may still cycle. At very high loads, it can run at its maximum allowed output without fully maintaining the setpoint. The manufacturer's performance tables specify actual capacity under particular indoor and outdoor conditions. Calling a system 'variable-speed' does not mean it has unlimited heating capacity in cold weather.

A useful conceptual model has a building with a load of two kilowatts at some mild outdoor condition. A fixed-output unit that supplies four kilowatts must cycle or use some storage mechanism to avoid gradually overheating the room. A variable-capacity unit may be able to supply roughly two kilowatts for a sustained period. The figures are illustrative; real equipment efficiency, minimum output, coil conditions, humidity control, and control algorithms all matter. But the difference in behavior explains why long, quiet operation can be evidence of modulation rather than a malfunction.

## Sensors describe an imperfect world

A controller cannot measure comfort directly. It reads sensors: room temperature, supply or return-air temperature, outdoor temperature, coil temperature, refrigerant pressure or temperature, humidity, and sometimes airflow or motor load. A sensor mounted in sunlight may report a different value from an occupant's shaded seating area. An outdoor sensor near an exhaust discharge can misrepresent ambient conditions. A return-air sensor may see air from several rooms mixed together, hiding the problem in the one room that is cold.

The controller compares a target with its measurements and chooses a response. Some use proportional or more sophisticated feedback; others use tables, hysteresis, and timed state transitions. None can overcome incorrect input. If a sensor reads low, the system may heat when it should not. If a filter blocks airflow, the compressor may be delivering thermal capacity into a system that cannot distribute it adequately. Those are different faults, and swapping the thermostat does not repair a blocked duct.

A variable-speed fan may intentionally change speed to keep a particular airflow target as filter resistance changes. But as resistance rises, the fan may use more power or eventually reach its allowable limit. A fan reporting one hundred percent command is not proof that the actual airflow is correct. Commanded speed, measured speed, static pressure, and delivered flow are related but distinct quantities.

## Humidity and temperature do not always favor the same mode

In cooling, the indoor coil may lower air temperature enough that water vapor condenses. A fast-moving stream of air spends a different time in contact with the coil than a slow one, and coil temperature changes with compressor operation. Humidity control can therefore call for a different combination of compressor and fan speeds than temperature control alone. Some units have a separate dehumidification mode; others cannot control humidity well at very low sensible load.

A resident might notice that a variable-speed system keeps the air temperature stable but indoor humidity drifts upward in mild rainy weather. That is not necessarily fixed by making the thermostat colder. We should record indoor dew point or humidity, equipment runtime, fan behavior, and how the system is configured. Ventilation, moisture sources, drainage, and the building envelope also belong in the diagnosis.

Heating has its own special transitions. Heat pumps may reverse cycle for outdoor-coil defrost. Auxiliary heat may operate under specific outdoor conditions or thermostat-recovery rules. A variable-speed controller may impose oil-return, pressure, or temperature constraints that temporarily change capacity. A homeowner looking only at the thermostat display can mistake a designed transition for random behavior.

## Build a useful operational log

Suppose a room is intermittently chilly. Instead of immediately turning up a fan speed, record outdoor temperature, thermostat setpoint, actual room temperature, return and supply readings where they can be measured safely, filter state, mode, and compressor or fan command if the equipment provides it. Compare periods when the room is comfortable with periods when it is not. Check whether the complaint follows wind, sun, occupancy, defrost, or a particular equipment transition.

Look at the heat-delivery path. A return-air restriction can reduce useful circulation, and supply leakage can lose conditioned air before it reaches the room. Variable controls can mask some problems by increasing speed, so apparent setpoint stability should not end the inspection. Conversely, a long compressor run at low speed need not be corrected just because an older system cycled more frequently.

Equipment logs and sensors are evidence, not automatic truth. Labels may show commanded values instead of measured values, proprietary fault codes may be context-dependent, and a replacement control board must match the unit's approved configuration. A diagnostic observation that seems to require opening a refrigerant circuit, bypassing a safety switch, or energizing exposed electrical parts belongs to a properly equipped technician. The general homeowner skill is to gather a coherent history and distinguish air, control, moisture, and refrigeration symptoms.

An effective diagnosis asks: what was the load, what was the controller trying to do, what did the sensors report, and what heat or air actually reached the room? Variable-speed technology becomes far easier to understand once we separate those four things.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Control-state log

| Timestamp | Outdoor / indoor condition | Commanded mode and capacity | Relevant sensor readings | Observed delivery |
|---|---|---|---|---|
| Morning recovery | Warm-up load may be high | Compressor stage / auxiliary status | Thermostat + return / supply if accessible | Room warm-up rate |
| Mild steady-state | Low load | Low or cycling capacity | Humidity, fan speed / static-pressure indication | Stable comfort / dew point |
| Defrost interval | Frost conditions | Defrost mode and timed transitions | Coil/outdoor sensors; equipment log | Indoor delivery changes |

Distinguish commanded fan percentage from measured airflow, and named compressor speed from delivered capacity. A continuous run is not evidence of inefficiency by itself.

**Technical boundary:** Refrigerant and high-voltage testing, safety interlocks, charge adjustment, and equipment configuration require model-specific service procedures and appropriately qualified personnel; source material does not certify a field diagnostic process.

## Selected reading and source locators (non-spoken)

- `doe-heatpumps` — [U.S. Department of Energy, Pump Up Your Savings With Heat Pumps](https://www.energy.gov/articles/pump-your-savings-heat-pumps). Heat transfer rather than direct heat generation.
- `doe-thermal-systems-guide` — [U.S. DOE Better Buildings, Decarbonizing Building Thermal Systems: A How-to Guide for Heat Pump Systems and Beyond](https://betterbuildingssolutioncenter.energy.gov/sites/default/files/attachments/87812.pdf). Inverter-based variable-speed compressors, feedback sensor controls and capacity modulation.
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.
- `ashrae-2025-res-loads` — [ASHRAE Handbook—Fundamentals (2025), Chapter 17, Residential Cooling and Heating Load Calculations](https://handbook.ashrae.org/handbooks/F25/IP/F25_Ch17/F25_Ch17_ip.aspx). Residential sensible and latent loads, short cycling and dehumidification.
- `doe-heatpump-thermostat` — [US Department of Energy, Purchasing Energy-Efficient Residential Air-Source Heat Pumps](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-air-source-heat-pumps). Heat pump control, auxiliary resistance heat, and thermostat recovery behavior.
