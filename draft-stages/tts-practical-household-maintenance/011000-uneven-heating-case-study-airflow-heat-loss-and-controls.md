# 011000 — Uneven Heating Case Study: Airflow, Heat Loss, and Controls

<!-- BEGIN SPOKEN LECTURE -->

The living room is comfortable, the upstairs bedroom is cold, and the thermostat says the heat is on. The homeowner has three proposed solutions: replace the thermostat, buy an electric space heater, or hire someone to add more insulation. Each might affect comfort. But none should be selected before understanding why this room differs from the others.

This is a case study in diagnosing an integrated system. The room receives heat from the HVAC equipment, loses heat through walls and windows, exchanges air with adjacent rooms, and responds to solar gains and occupants. The thermostat measures conditions at one location; it does not know the temperature of every room. A symptom in one bedroom may therefore involve the room, the distribution network, or a control strategy designed for the house as a whole.

## Define the complaint precisely

First distinguish "always cold" from "cold only at night" and "doesn't warm while the furnace runs" from "cools unusually fast after shutdown." Measure temperatures in several rooms using comparable instruments and positions. Record outdoor temperature, time, solar exposure, door position, thermostat program, and whether heating equipment is actually operating. A snapshot taken at the same time every day may miss a problem tied to wind or sun.

Suppose the bedroom starts at sixty-four degrees and the hall at sixty-nine. When heat runs for twenty minutes, the hall rises several degrees but the bedroom hardly changes. That suggests inadequate delivery relative to loss during that operating period. If both rise similarly but the bedroom later cools much faster, a high room-specific heat loss or infiltration mechanism becomes more likely. The diagnosis is still open, but the two time histories point to different questions.

## Follow the heat delivery path

At a forced-air supply register, warm air means the system is delivering *some* heat. It does not reveal how much. A weak trickle of warm air can deliver far less power than a moderate flow. A long duct route, crushed flexible duct, poorly connected branch, high resistance, closed damper, or air leak can reduce delivery. A badly restricted filter or return may reduce system-wide flow. Inspect what is accessible and document before making changes that could alter equipment operation.

A room with a supply but little return path can behave differently when its door closes. Supply air must leave through the door undercut, a transfer path, or unintended gaps. The pressure difference can drive leakage and reduce intended airflow. If the room improves noticeably with the door open, that observation supports investigating return paths and room pressure. It does not prove which duct or register needs modification.

Now imagine a hydronic baseboard system rather than forced air. The same room complaint has a different fault tree: circulation, trapped air, water temperature, fin condition, control valves, and room load. Troubleshooting should begin by identifying equipment type. Carrying an air-duct hypothesis into a hot-water heating system wastes effort.

## Follow the loss path as well

The cold bedroom has two exterior walls, a large window, and an uninsulated knee wall facing an attic. Its design heat loss may be higher than that of an interior room. A temperature difference across an assembly drives heat transfer; wind can increase infiltration through leaks; a cold night sky and exposed windows change surface temperatures and comfort. Even if the air temperature were equal, cold surrounding surfaces could make the room feel less comfortable through radiant exchange.

A thermal camera can help visualize surface patterns, but a dark patch by itself is not a diagnosis. A stud, a missing insulation cavity, a cold supply pipe, wet sheathing, or an air leak can produce overlapping signatures. A blower-door test or other controlled method may reveal leakage pathways, but testing must respect combustion-appliance and ventilation safety. Start with geometry, history, and accessible evidence before assuming an expensive envelope intervention.

## Controls can create and conceal the symptom

A thermostat in a sunny hallway may satisfy its set point before a shaded bedroom warms. A sensor located near a supply register may also misrepresent average occupied conditions. Zoning can help some layouts, but adding dampers without understanding airflow and static pressure can increase strain on equipment. Smart thermostats that average room sensors may change the control decision while leaving distribution defects intact.

Short cycling, deadbands, setback schedules, heat-pump auxiliary heat decisions, and equipment capacity can complicate diagnosis. Make sure the control is commanding heat and determine how the system responds. A temperature set point tells you what the controller wants; it does not certify that the machine, ducts, and rooms are performing according to design.

## Prioritize tests by information gained

The homeowner now has a modest plan. Log room temperatures and equipment states over several days. Compare the bedroom's warming and cooling patterns under similar weather. Observe the supply and return arrangement. Inspect accessible ductwork, filter condition, attic boundaries, window hardware, and visible air-sealing gaps without disturbing hazardous materials. Then request targeted airflow, load, or building-envelope assessment if observations justify it.

The space heater is not a diagnosis. It may increase electricity use and introduce local fire or overload concerns if used improperly, while leaving the original problem unsolved. A new thermostat may improve scheduling but cannot repair a disconnected duct. Extra insulation may be useful, but will not correct a shut-off branch damper. Each intervention should correspond to evidence about a specific mechanism.

The lesson extends beyond a cold bedroom. Homes are coupled systems. When you know how to draw their energy, air, and control paths, you can choose observations that distinguish explanations instead of replacing parts on intuition. Good maintenance is the discipline of making a smaller, better-founded guess after every new measurement.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Observation log template

Date/time; outdoor weather; thermostat set/actual temperature; bedroom/hall/living-room temperatures; equipment on/off; door open/closed; register condition; sun/wind; notes about pressure or air movement. Use measurements as comparable trends rather than claiming laboratory-grade accuracy.

### Fault tree

- **Equipment**: no heat generation, low capacity, short cycles, control misbehavior.
- **Distribution**: duct leakage/restriction, return path, register delivery, branch balance, hydronic flow where relevant.
- **Envelope**: glazing and insulation heat loss, infiltration, thermal bridges, radiant surface temperature.
- **Occupant/control**: door closure, thermostat placement, schedules, solar exposure.

### Reference scope

DOE whole-house air/heat-flow guides, ENERGY STAR duct-sealing guidance, ACCA room-load methodology, EPA indoor-air advice. Manufacturer airflow limits and combustion safety are not determined from temperature logging. Remedial work requires equipment- and house-specific professional evaluation when warranted.

## Selected reading and evidence records (non-spoken)

- `energystar-duct-sealing-case` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Supply and return duct air leakage, comfort and delivery losses.
- `doe-air-vapor` — [DOE Building Science Education, Air Barriers vs Vapor Barriers](https://bsesc.energy.gov/energy-basics/building-enclosure-air-barriers-vs-vapor-barriers-continuous-sealed-wrb-walls). Different enclosure moisture pathways.
- `epa-maintenance` — [EPA WaterSense, Home Maintenance](https://www.epa.gov/watersense/home-maintenance). Leak monitoring and water-using systems.
