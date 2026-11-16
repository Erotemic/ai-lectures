# 007000 — Thermostats, Controls, and Diagnostic Patterns

**Track:** HVAC and Refrigeration. **Background:** Heating and cooling loads, airflow, refrigeration, and humidity. **Purpose:** understand the control loop, staging, and evidence needed to diagnose system behavior.

<!-- BEGIN SPOKEN LECTURE -->

# The number on the wall is not the whole system

A room thermostat shows a temperature and a setting. Between those two numbers sits an entire control system: sensors, software or electromechanical contacts, time delays, fans, pumps, burners, compressors, valves, and the thermal mass of a building. When a home feels uncomfortable, adjusting the number is tempting because the interface makes it look as though the thermostat directly sets the room temperature. It does not. It requests heating or cooling from equipment that has limited capacity and an operating strategy.

The simplest thermostat is a feedback controller. It measures a condition, compares it with a target, and issues a call for heating or cooling. If the measured temperature is below a heating target by enough, the controller calls for heat. When the room recovers, the call ends. Many systems include a deadband or hysteresis to prevent rapid switching around a single exact temperature. Without a deadband, tiny sensor noise could cause a compressor or relay to chatter.

## A call is not proof of delivery

Follow a winter heating call. The thermostat detects a demand. A controller may check safeties, start a combustion sequence, or request a heat-pump compressor. A circulation fan may wait until a heat exchanger is warm or start according to a programmed sequence. The result depends on fuel or electrical availability, equipment state, airflow, and whether the distribution system can move the produced heat into the occupied rooms.

If the thermostat displays 'heating' while the room stays cold, several stages may explain the discrepancy. The demand may not reach the equipment. The equipment may enter a lockout or protective delay. It may operate but deliver insufficient heat because of poor airflow, blocked transfer, or outdoor conditions. Or the building may lose heat as quickly as it is delivered. The display tells you a requested state, not necessarily the actual heat transfer.

Similarly, if a cooling system runs continuously in extreme weather, that fact alone does not establish a failure. Equipment near its design limit may operate for a long interval. Short, frequent cycles can be more suspicious, especially when accompanied by poor humidity control, but the cause could be sensor placement, staging, an oversized unit, restricted flow, or a control problem. Observe actual room temperature trajectories and operating conditions before assigning blame.

## Time matters

A building has thermal inertia. Floors, furniture, walls, and water in pipes store heat. A thermostat responds to a local sensor, while other rooms may respond more slowly. Place the sensor in sun, near a supply register, next to an exterior draft, or behind a heat-producing appliance, and the measurement may fail to represent the space people care about. A perfect controller attached to a misleading sensor can make poor decisions.

Controls also include intentional delays. Some compressors must wait before restarting to protect equipment. A heat pump may periodically defrost its outdoor coil. A furnace may keep the fan operating after fuel shuts off to remove residual heat. An observer who expects immediate simultaneous changes can mistake these designed sequences for faults. The task is to compare observed operation with the appropriate equipment sequence, not with an imagined universal sequence.

Multi-stage systems raise another question: which equipment is doing the work? A heat pump may have variable compressor output, auxiliary electric resistance heat, or a separate backup system. When a thermostat raises the target sharply, some control schemes request extra stages. Other modern systems can recover gradually without the same penalty. Whether setback saves energy depends on the control logic, equipment, weather, and building; a rule that is useful for a conventional furnace need not describe a particular heat pump correctly.

## Heating, cooling, and humidity are coupled

In cooling mode, an evaporator coil can remove both sensible heat and moisture. But moisture removal requires suitable coil temperature, air contact, and run time. If the thermostat is satisfied quickly, indoor relative humidity may remain high despite adequate cooling of the sensor location. Turning the temperature lower is not a robust diagnosis. It might create more dehumidification under some operating conditions while wasting energy or making surfaces uncomfortably cold.

Control settings can also expose duct or ventilation issues. A system may deliver normal air in one room and little in another. An air filter may be dirty. A return path may be constricted by a closed door. A thermostat that displays an error about an equipment sensor may be reporting a component-specific problem rather than a room-temperature error. Distinguish sensor signals, commands, actual physical outputs, and the resulting comfort conditions.

## Diagnose in chronological order

Imagine a heat pump that runs loudly every morning after a large nighttime setback. Record outdoor temperature, the room temperature before recovery, the requested setpoint, which stages are active, and the time required to recover. A peak in power use may be an intended high-capacity or auxiliary-heat response. If the same equipment is quiet and efficient under a nearly constant setting, the comparison identifies a control-and-use interaction. It does not by itself establish a defective compressor.

Or imagine a room that is warm even though the thermostat says the house is cool. Record which room contains the thermostat, door positions, air-supply differences, direct sunlight, and the time at which the complaint occurs. The pattern may reveal a distribution or sensor-placement problem rather than insufficient cooling capacity.

Diagnostic observation is different from bypassing safeties. High-voltage equipment, combustion systems, and refrigerant circuits require appropriately qualified work. A useful homeowner or trainee can still document symptoms, measure accessible environmental variables, check manufacturer-listed user settings, and observe fault indications without defeating protective devices.

The central idea is feedback with delays and limits. A thermostat commands equipment based on an imperfect measurement of a spatially distributed building. Good diagnosis follows the chain from measured state to requested action, actual equipment state, delivered energy, and finally the building's response.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Conceptual heat-balance model

`C dT/dt = Q_delivered − UA(T_indoor − T_outdoor) − Q_other_losses + Q_internal` for a simplified single-zone model. `C` summarizes effective thermal capacitance; the real building is multi-zone and has additional moisture and ventilation states. This is a reasoning tool, not a sizing method.

### Time-stamped observation sheet

Record timestamp, indoor sensor temperature, independent room temperature, target, outdoor temperature, stage/fan status, fault indicator and comfort observation. Compare the **call** with the **actual equipment state** and **temperature trend**. Note any documented startup, anti-short-cycle or defrost interval.

**Review boundary:** Do not bypass interlocks or infer wiring terminals from generic diagrams. Manufacturer sequences, refrigerant handling, fuel-burning equipment and local requirements must be evaluated separately.

## Selected reading and evidence records (non-spoken)

- `doe-heatpump-thermostat` — [US Department of Energy, Purchasing Energy-Efficient Residential Air-Source Heat Pumps](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-air-source-heat-pumps). Heat pump control, auxiliary resistance heat, and thermostat recovery behavior.
- `ashrae-2025-res-loads` — [ASHRAE Handbook—Fundamentals (2025), Chapter 17, Residential Cooling and Heating Load Calculations](https://handbook.ashrae.org/handbooks/F25/IP/F25_Ch17/F25_Ch17_ip.aspx). Residential sensible and latent loads, short cycling and dehumidification.
- `energystar-ducts` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Duct leakage as an energy and air delivery problem.
