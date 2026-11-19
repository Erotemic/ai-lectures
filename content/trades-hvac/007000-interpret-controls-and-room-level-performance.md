# Interpret controls and room-level performance

<!-- BEGIN SPOKEN LECTURE -->

# Interpret controls and room-level performance

## Thermostats, Controls, and Diagnostic Patterns

A room thermostat shows a temperature and a setting. Between those two numbers sits an entire control system: sensors, software or electromechanical contacts, time delays, fans, pumps, burners, compressors, valves, and the thermal mass of a building. When a home feels uncomfortable, adjusting the number is tempting because the interface makes it look as though the thermostat directly sets the room temperature. It does not. It requests heating or cooling from equipment that has limited capacity and an operating strategy.

The simplest thermostat is a feedback controller. It measures a condition, compares it with a target, and issues a call for heating or cooling. If the measured temperature is below a heating target by enough, the controller calls for heat. When the room recovers, the call ends. Many systems include a deadband or hysteresis to prevent rapid switching around a single exact temperature. Without a deadband, tiny sensor noise could cause a compressor or relay to chatter.

### A call is not proof of delivery

Follow a winter heating call. The thermostat detects a demand. A controller may check safeties, start a combustion sequence, or request a heat-pump compressor. A circulation fan may wait until a heat exchanger is warm or start according to a programmed sequence. The result depends on fuel or electrical availability, equipment state, airflow, and whether the distribution system can move the produced heat into the occupied rooms.

If the thermostat displays 'heating' while the room stays cold, several stages may explain the discrepancy. The demand may not reach the equipment. The equipment may enter a lockout or protective delay. It may operate but deliver insufficient heat because of poor airflow, blocked transfer, or outdoor conditions. Or the building may lose heat as quickly as it is delivered. The display tells you a requested state, not necessarily the actual heat transfer.

Similarly, if a cooling system runs continuously in extreme weather, that fact alone does not establish a failure. Equipment near its design limit may operate for a long interval. Short, frequent cycles can be more suspicious, especially when accompanied by poor humidity control, but the cause could be sensor placement, staging, an oversized unit, restricted flow, or a control problem. Observe actual room temperature trajectories and operating conditions before assigning blame.

### Time matters

A building has thermal inertia. Floors, furniture, walls, and water in pipes store heat. A thermostat responds to a local sensor, while other rooms may respond more slowly. Place the sensor in sun, near a supply register, next to an exterior draft, or behind a heat-producing appliance, and the measurement may fail to represent the space people care about. A perfect controller attached to a misleading sensor can make poor decisions.

Controls also include intentional delays. Some compressors must wait before restarting to protect equipment. A heat pump may periodically defrost its outdoor coil. A furnace may keep the fan operating after fuel shuts off to remove residual heat. An observer who expects immediate simultaneous changes can mistake these designed sequences for faults. The task is to compare observed operation with the appropriate equipment sequence, not with an imagined universal sequence.

Multi-stage systems raise another question: which equipment is doing the work? A heat pump may have variable compressor output, auxiliary electric resistance heat, or a separate backup system. When a thermostat raises the target sharply, some control schemes request extra stages. Other modern systems can recover gradually without the same penalty. Whether setback saves energy depends on the control logic, equipment, weather, and building; a rule that is useful for a conventional furnace need not describe a particular heat pump correctly.

### Heating, cooling, and humidity are coupled

In cooling mode, an evaporator coil can remove both sensible heat and moisture. But moisture removal requires suitable coil temperature, air contact, and run time. If the thermostat is satisfied quickly, indoor relative humidity may remain high despite adequate cooling of the sensor location. Turning the temperature lower is not a robust diagnosis. It might create more dehumidification under some operating conditions while wasting energy or making surfaces uncomfortably cold.

Control settings can also expose duct or ventilation issues. A system may deliver normal air in one room and little in another. An air filter may be dirty. A return path may be constricted by a closed door. A thermostat that displays an error about an equipment sensor may be reporting a component-specific problem rather than a room-temperature error. Distinguish sensor signals, commands, actual physical outputs, and the resulting comfort conditions.

### Diagnose in chronological order

Imagine a heat pump that runs loudly every morning after a large nighttime setback. Record outdoor temperature, the room temperature before recovery, the requested setpoint, which stages are active, and the time required to recover. A peak in power use may be an intended high-capacity or auxiliary-heat response. If the same equipment is quiet and efficient under a nearly constant setting, the comparison identifies a control-and-use interaction. It does not by itself establish a defective compressor.

Or imagine a room that is warm even though the thermostat says the house is cool. Record which room contains the thermostat, door positions, air-supply differences, direct sunlight, and the time at which the complaint occurs. The pattern may reveal a distribution or sensor-placement problem rather than insufficient cooling capacity.

Diagnostic observation is different from bypassing safeties. High-voltage equipment, combustion systems, and refrigerant circuits require appropriately qualified work. A useful homeowner or trainee can still document symptoms, measure accessible environmental variables, check manufacturer-listed user settings, and observe fault indications without defeating protective devices.

The central idea is feedback with delays and limits. A thermostat commands equipment based on an imperfect measurement of a spatially distributed building. Good diagnosis follows the chain from measured state to requested action, actual equipment state, delivered energy, and finally the building's response.

## Heat Pump Defrost, Cold Weather, and Controls

A heat pump’s cold-weather behavior shows why a control decision has to be interpreted within the equipment’s operating mode.

A heat pump is heating a house on a damp winter morning. The outdoor unit is covered in frost. Then the fan stops, a cloud of steam rises, and the compressor continues making noise. A few minutes later the fan starts and the house heats normally again. To someone accustomed to a furnace, this can resemble a breakdown. It may instead be a normal defrost cycle: the machine is temporarily spending heat to restore its ability to collect heat.

### Why frost forms on a machine that is heating

An air-source heat pump takes energy from outdoor air and moves it indoors using a refrigerant cycle. In heating mode, the outdoor coil is an evaporator. Refrigerant there must be at a temperature low enough to absorb heat from the air passing over the coil. The outside air might be above freezing while parts of the coil are below freezing. Water vapor can deposit on the cold surfaces as frost, or condense and then freeze. Frost restricts airflow and adds thermal resistance between outdoor air and the refrigerant.

Frost does not by itself mean that a heat pump has stopped extracting heat. The outdoor coil must be colder than its heat source to absorb energy. A white coating shortly before a normal defrost cycle is different from a solid block of ice that keeps growing around the base and obstructs the fan. The practical question is whether the system can manage the accumulation before airflow and operation are impaired.

Outdoor temperature alone does not determine frost severity. Humidity, dew point, wind, coil temperature, airflow, load, and run time all contribute. In some climates, damp weather near freezing can produce substantial frost, while much colder, drier air supplies less moisture. A defrost algorithm based only on a wall clock cannot perfectly account for changing conditions.

### A reversible machine has two temporary jobs

A conventional reversible heat pump uses a four-way reversing valve to change which heat exchanger is rejecting heat and which is absorbing heat. For a common reverse-cycle defrost, the system temporarily routes hot refrigerant to the outdoor coil to melt accumulated ice. In effect, the refrigerant cycle briefly resembles cooling operation. Some systems employ additional control strategies; the exact sequence is model dependent.

During defrost, the outdoor fan may stop, making it easier to warm the coil. The indoor side can receive less heat or temporarily tend to cool, so a controller may stop an indoor fan, engage supplemental heat, or use other measures to limit cold air delivery. These are design choices, not universal behavior. Steam at the outdoor unit can be water vapor from melting frost, rather than smoke from a fault. Meltwater should have a path away from the base without freezing into a persistent obstruction.

A useful energy budget keeps three quantities separate: thermal energy delivered to the rooms, electrical energy consumed by the system, and thermal energy required to defrost the outdoor coil. During normal heating, a heat pump may deliver several units of heat for every unit of electrical input under particular rating conditions. Defrost consumes time and energy without providing the same useful heating to occupied space. A seasonal coefficient of performance therefore includes effects not visible in an idealized steady-state test.

### The thermostat is only one controller

The room thermostat asks for a temperature outcome. The refrigeration controls have to manage compressor operation, coil temperatures, pressure protections, fan speed, refrigerant metering, defrost initiation, and termination. Modern variable-speed systems may change compressor and fan operation continuously. A single displayed setpoint does not reveal every internal operating decision.

Older or simpler controls may schedule defrost according to accumulated compressor run time combined with temperature conditions. Demand defrost strategies use sensor measurements and control logic to infer when a cycle is worthwhile. Both approaches depend on correct sensors, airflow, and programming. A defective coil-temperature sensor can lead to unnecessary cycles or insufficient frost removal. A controller may also enforce minimum run times and delays that prevent destructive rapid cycling.

Some heat pumps have auxiliary electric resistance heating. Its presence does not mean the heat pump is ineffective, but unnecessary use can raise electricity consumption because resistance heating delivers approximately one unit of thermal energy per unit of electric energy at the point of use. A heat pump's performance depends on outdoor conditions, supply temperature, capacity, and system configuration. In a properly sized cold-climate system, low outdoor temperature alone should not be interpreted as proof that the unit must abandon heat-pump heating entirely.

### Distinguish frost, snow, and frozen drainage

Consider four symptoms. First: a thin frost layer accumulates, a brief cycle clears it, and operation resumes. That is consistent with normal defrost. Second: ice remains thick across much of the coil after repeated cycles. That suggests checking actual defrost performance, sensors, refrigerant operation, and airflow. Third: the coil clears but a thick slab of ice grows below the unit and eventually reaches the fan. That suggests meltwater drainage and installation geometry deserve attention. Fourth: the unit has poor airflow because leaves, snow, or other debris obstruct its intake or outlet. Defrost timing cannot compensate for a blocked air path.

A unit placed beneath a roof dripline may receive repeated meltwater from above that freezes on the coil or housing. A unit installed too close to a wall or hedge may recirculate cold discharge air or restrict flow. Snow accumulation changes available clearance. Location is part of machine performance. So are mounting height, drain configuration, and the design of an appropriate snow or ice management strategy.

### Diagnose by recording a complete cycle

A sensible service history includes outdoor temperature, humidity or weather, time between cycles, duration of defrost, whether frost clears, whether the fan behaves as expected, and whether condensate can leave the unit. Also record supply-air behavior and whether supplemental heating engages. One clip of the machine steaming is not enough to diagnose it. Nor is a single wattage reading: compressors and heaters can draw very different power at different moments.

Do not bypass protection controls or force refrigerant operations as a homeowner experiment. The observational distinction is valuable without doing that. A heat pump is a machine balancing heat transfer, humidity, and control logic. Defrost reveals that the outdoor coil is not an inert metal radiator. It interacts with the weather, and sometimes the most efficient way to keep heating the house is to interrupt heating briefly and clear the frost.

## Duct Leakage, Zoning, and Temperature Imbalance

A homeowner says the furnace runs, but the bedroom at the end of the hall stays cold. It is tempting to blame the thermostat or buy a larger furnace. Yet the room might need no additional heat from the machine. It may need a larger share of heat already produced, less heat lost through the building envelope, or a way for supplied air to return to the system.

A forced-air heating system is a network. A blower raises air pressure, ducts carry that air, registers deliver it to rooms, return paths bring air back, and the furnace or heat pump changes its temperature. The pressure difference moves air, but every bend, filter, grille, branch, and duct wall adds resistance. The same blower operating with a different duct network can produce a different total flow and a very different distribution among rooms.

### Delivery is not merely supply temperature

The heat delivered to a room by supply air depends on how much air enters, how different its temperature is from the room, and the properties of the air. A register blowing hot air very weakly may deliver less useful heat than a moderately warm register with adequate flow. Conversely, a generous airflow can still leave a room cold if it loses heat faster than the system supplies it during the design condition.

Begin with observation. Are all the rooms slow to warm, or only one? Is the temperature difference present during sunny afternoons, windy evenings, and overnight? Does it increase with outdoor temperature difference? Does the problematic room have a long duct run, a closed door, or unusually large exposed surfaces? These observations divide the problem among equipment capacity, distribution, return paths, and enclosure loads.

### Leaks alter more than efficiency

Suppose a supply duct leaks into an attic. Heated or cooled air may be lost before reaching its intended register. The same leak can alter air pressure in the occupied space. If the blower supplies less air to a room than it removes through its return, the room may draw air through cracks from outside or adjacent spaces. A return-side leak in an attic or basement may entrain unconditioned air into the system. The resulting thermal and moisture consequences differ, and the leakage may depend on blower operation and duct pressure.

Sealing accessible ducts can help, but identifying the leak is part of the work. A joint may look loosely connected while leaking little; a hidden connection may leak significantly. Duct leakage testing intentionally pressurizes or depressurizes the duct system under controlled conditions to quantify the air escaping. A pressure reading is not itself a volumetric leakage rate; test procedures relate pressure and flow to a defined standard. Field standards, equipment specifications, and boundary definitions matter.

### Closed doors change the circuit

Consider a bedroom with a supply register but no dedicated return. When its door is closed, the return path may be a narrow door undercut or transfer grille. Supply air entering the room must leave somewhere. If the return path has high resistance, the bedroom may become positively pressurized relative to the hallway, pushing conditioned air through exterior leaks. Meanwhile the central return zone may become relatively negative and pull in outside air. This is why a closed door can change system behavior even when the blower runs at the same setting.

A zone damper introduces another control variable. Closing a damper reduces flow through one branch, but it also changes the resistance seen by the blower. This can shift pressure, airflow, and noise elsewhere. Some systems manage those changes through variable-speed equipment, controls, or engineered bypass arrangements; improvising many closed registers is not a substitute for proper zoning design. Restricting airflow beyond equipment specifications can impair performance or lead to overheating or coil problems.

### Balance is a measurement problem

Balancing a duct system is the deliberate distribution of airflow. It requires knowing desired room loads and actual or estimated flows. A technician may use airflow hoods, pressure measurements, temperature measurements, and blower-performance information. Measuring air speed at one spot on a grille is not automatically the same as determining reliable total volume flow, because velocity varies across the opening and some grilles introduce swirl.

The return side deserves equal attention. A very restrictive filter or blocked return can reduce total airflow even when supply ducts are intact. Fan curves describe how much flow a blower can deliver against different resistance. At high resistance, the operating point may move to lower flow, depending on fan and control type. Increasing fan speed is not a universal solution: it can increase noise, energy use, and pressure stress while leaving the underlying restriction in place.

### A structured cold-bedroom investigation

First record room temperatures under repeatable conditions and note thermostat schedule, outdoor weather, doors, and fan state. Second, compare supply-air temperature and approximate delivery with other rooms; assess filter condition and obvious obstructions without defeating protective components. Third, investigate the return path and pressure effects of door closure. Fourth, inspect accessible duct connections, insulation, and routing. Finally, evaluate the room's heat loss and possible envelope defects. Only then decide whether equipment capacity, ductwork, controls, insulation, or a combination needs attention.

The most important result is not a particular fix. It is a distinction: a room can be cold because heat is not generated, because heat is not delivered, because air does not circulate properly, or because the room loses heat too fast. Forced-air systems become comprehensible when you follow energy and pressure along separate paths and test both.

## Variable-Speed Equipment, Sensors, and Control Modes

Two heating systems can deliver the same amount of heat over a winter day while behaving very differently. One runs at full output, shuts off, and starts again when the room cools. Another adjusts its output for long periods, matching the building's changing load. If the second system runs almost continuously, that may be exactly what it is designed to do. Diagnosing variable-speed HVAC equipment begins by abandoning the assumption that 'running' and 'not running' are the only useful operating states.

### Capacity is an adjustable quantity

In a simple fixed-capacity air conditioner or heat pump, the compressor operates at roughly its intended on-speed while a thermostat requests heating or cooling. Capacity is managed by runtime: more minutes on, more energy moved. Systems with staged compressors offer a few discrete capacities. Inverter-driven systems can vary compressor speed over an operating range; variable-speed indoor fans and electronic expansion valves may coordinate with it. The controller's objective is not usually maximum instantaneous heat flow. It is adequate comfort, stable operation, and efficiency under the equipment's limits.

There are still boundaries. Every compressor has a usable speed range; a unit cannot keep lowering output indefinitely. At very small building loads it may still cycle. At very high loads, it can run at its maximum allowed output without fully maintaining the setpoint. The manufacturer's performance tables specify actual capacity under particular indoor and outdoor conditions. Calling a system 'variable-speed' does not mean it has unlimited heating capacity in cold weather.

A useful conceptual model has a building with a load of two kilowatts at some mild outdoor condition. A fixed-output unit that supplies four kilowatts must cycle or use some storage mechanism to avoid gradually overheating the room. A variable-capacity unit may be able to supply roughly two kilowatts for a sustained period. The figures are illustrative; real equipment efficiency, minimum output, coil conditions, humidity control, and control algorithms all matter. But the difference in behavior explains why long, quiet operation can be evidence of modulation rather than a malfunction.

### Sensors describe an imperfect world

A controller cannot measure comfort directly. It reads sensors: room temperature, supply or return-air temperature, outdoor temperature, coil temperature, refrigerant pressure or temperature, humidity, and sometimes airflow or motor load. A sensor mounted in sunlight may report a different value from an occupant's shaded seating area. An outdoor sensor near an exhaust discharge can misrepresent ambient conditions. A return-air sensor may see air from several rooms mixed together, hiding the problem in the one room that is cold.

The controller compares a target with its measurements and chooses a response. Some use proportional or more sophisticated feedback; others use tables, hysteresis, and timed state transitions. None can overcome incorrect input. If a sensor reads low, the system may heat when it should not. If a filter blocks airflow, the compressor may be delivering thermal capacity into a system that cannot distribute it adequately. Those are different faults, and swapping the thermostat does not repair a blocked duct.

A variable-speed fan may intentionally change speed to keep a particular airflow target as filter resistance changes. But as resistance rises, the fan may use more power or eventually reach its allowable limit. A fan reporting one hundred percent command is not proof that the actual airflow is correct. Commanded speed, measured speed, static pressure, and delivered flow are related but distinct quantities.

### Humidity and temperature do not always favor the same mode

In cooling, the indoor coil may lower air temperature enough that water vapor condenses. A fast-moving stream of air spends a different time in contact with the coil than a slow one, and coil temperature changes with compressor operation. Humidity control can therefore call for a different combination of compressor and fan speeds than temperature control alone. Some units have a separate dehumidification mode; others cannot control humidity well at very low sensible load.

A resident might notice that a variable-speed system keeps the air temperature stable but indoor humidity drifts upward in mild rainy weather. That is not necessarily fixed by making the thermostat colder. We should record indoor dew point or humidity, equipment runtime, fan behavior, and how the system is configured. Ventilation, moisture sources, drainage, and the building envelope also belong in the diagnosis.

Heating has its own special transitions. Heat pumps may reverse cycle for outdoor-coil defrost. Auxiliary heat may operate under specific outdoor conditions or thermostat-recovery rules. A variable-speed controller may impose oil-return, pressure, or temperature constraints that temporarily change capacity. A homeowner looking only at the thermostat display can mistake a designed transition for random behavior.

### Build a useful operational log

Suppose a room is intermittently chilly. Instead of immediately turning up a fan speed, record outdoor temperature, thermostat setpoint, actual room temperature, return and supply readings where they can be measured safely, filter state, mode, and compressor or fan command if the equipment provides it. Compare periods when the room is comfortable with periods when it is not. Check whether the complaint follows wind, sun, occupancy, defrost, or a particular equipment transition.

Look at the heat-delivery path. A return-air restriction can reduce useful circulation, and supply leakage can lose conditioned air before it reaches the room. Variable controls can mask some problems by increasing speed, so apparent setpoint stability should not end the inspection. Conversely, a long compressor run at low speed need not be corrected just because an older system cycled more frequently.

Equipment logs and sensors are evidence, not automatic truth. Labels may show commanded values instead of measured values, proprietary fault codes may be context-dependent, and a replacement control board must match the unit's approved configuration. A diagnostic observation that seems to require opening a refrigerant circuit, bypassing a safety switch, or energizing exposed electrical parts belongs to a properly equipped technician. The general homeowner skill is to gather a coherent history and distinguish air, control, moisture, and refrigeration symptoms.

An effective diagnosis asks: what was the load, what was the controller trying to do, what did the sensors report, and what heat or air actually reached the room? Variable-speed technology becomes far easier to understand once we separate those four things.

## Diagnosing Comfort Complaints with Occupancy and Sensor Logs

The control model can now be tested against the occupied room’s recorded conditions rather than a single thermostat reading.

A resident says the bedroom is cold in winter. The thermostat is set to seventy degrees, the heating equipment runs, and the technician measures warm air at a supply register. That sounds like a heating system doing its job. Yet the resident may still be right. The measured air, the heat actually delivered to the room, the temperature of the room's surfaces, and the comfort of the person lying near a cold window are four different things.

A diagnostic log should help us see those differences without treating every complaint as a failed thermostat.

### Begin with the time pattern

Ask when the room becomes uncomfortable. Is it cold only when the door is shut, when wind blows, during long overnight setbacks, or during the first hour after the heating system starts? Does the issue follow occupancy, daylight, outdoor temperature, or equipment runtime? A response that says 'always cold' may become much more informative when mapped onto a twenty-four-hour schedule.

A household system has several control signals. The thermostat makes a call for heat or cooling; equipment may stage or modulate its output; a fan may run at a separate speed; a hydronic pump or zone valve may respond; and the room's surfaces lag behind all of these. A temperature log without equipment state can make normal cycling look like instability. At minimum, record room temperature, a comparison room, central setpoint, equipment call or runtime, and outdoor conditions. Occupancy and door position are useful event annotations rather than burdensome continuous measurements.

A logger samples a local environment. If it rests in sunlight, against a cold exterior wall, or beside a humidifier, it is not a neutral witness. Two sensors that disagree may be measuring two different microclimates, or one may be biased. Before interpreting small differences, compare the sensors side by side in a representative interior location for long enough to stabilize. Note offsets and then place each in its intended room at similar height and away from direct air currents. Exact laboratory calibration is unnecessary for seeing a multi-degree pattern, but consistent placement is essential.

### Follow the heat balance

A room loses heat through the envelope and through outdoor air that enters it. It gains heat from the supplied system, people, appliances, sun, and adjacent rooms. Even if supply air is warm, the flow rate may be insufficient to balance the loss. Delivered sensible heating in an airflow system depends approximately on how much air moves through the register and how much warmer it is than the room. A twenty-degree temperature difference with very little airflow is not equivalent to a twenty-degree difference with plenty of airflow. Likewise, a return-air path blocked by a closed bedroom door can alter the pressure difference across the door and reduce intended circulation.

One practical comparison is a room that stays cold during long steady heating calls while a nearby room reaches setpoint. That can indicate a mismatch in local load and delivery. A room that starts cold but eventually catches up could instead be affected by system cycling, thermal mass, or recovery strategy. A room that is only uncomfortable on windy days suggests leakage or surfaces cooled by wind-driven exposure. These are hypotheses, not automatic repair prescriptions.

For cooling complaints, humidity complicates the story. Dry-bulb temperature alone does not show the moisture load. A system that satisfies temperature quickly may leave high humidity if dehumidification has been inadequate. Warm surfaces or direct sunlight can create radiant discomfort at an otherwise reasonable air temperature. A ceiling fan can improve perceived comfort through air motion without lowering the room's stored heat. Ask what the occupant actually experiences rather than relying entirely on the thermostat's integer display.

### Turn notes into a defensible experiment

Consider two bedrooms that share a zone. Over five similar nights, bedroom A falls below bedroom B only when A's door is closed. Record whether a supply or return path exists, the position of each register, and the pressure or airflow effect of closing the door. A qualified assessment may measure room-to-hall pressure difference under operating conditions. The point is not to declare every door must remain open; it is to recognize that a distribution system needs a complete air path, not merely a supply opening.

Now consider a different room. Its temperature rises on sunny days even when the air conditioner operates as it does elsewhere. A log of window exposure and afternoon temperature suggests solar gain, not just refrigerant charge. Changing the thermostat can hide the symptom while making the rest of the building too cold. A shading test, documented under comparable conditions, can isolate a large part of the load.

A good log records interventions. If a filter is replaced, if a damper is adjusted, or if insulation is added, mark the exact date and keep settings comparable before and after. Without a change log, an apparent improvement might be caused by milder weather. Weather normalization need not begin with a sophisticated model: compare periods with similar outdoor temperatures and clear descriptions of wind and solar exposure before claiming an effect.

### Know what the log cannot prove

A few thermometers do not measure duct leakage, refrigerant flow, combustion quality, or equipment capacity. A room-temperature curve is influenced by building heat storage and user behavior, so it cannot uniquely identify the fault. Also, a sensor used in automation can become a control input: relocating it may alter the system you're trying to observe. Distinguish passive measurement from experiments that change the control loop.

The practical outcome is a concise issue description a contractor can reproduce: 'On overnight heating calls below this outdoor temperature, the north bedroom stays four degrees colder than the hall; the difference grows with the door shut and the return path is constrained.' That is better than 'The furnace is bad,' because it preserves the evidence without inventing a cause. Comfort diagnostics improve when the resident's experience, the room's physical behavior, and the equipment's control timeline are considered together.

## Heat Pump Cycling, Recovery, and Electrical Demand

An electric utility bill rises sharply during a winter cold spell. The heat pump appears to be running most of the day. A homeowner wonders whether that means the equipment is failing, too small, or simply working hard. The answer cannot be read from runtime alone. We have to distinguish delivered heat, electrical power, control strategy, and how quickly the house loses energy to outdoors.

### Continuous operation and short cycling are different observations

A variable-speed heat pump may operate for long periods at reduced output. That can be normal: instead of switching fully on and off, it matches heat delivery more closely to the building's changing load. Long runtime is not itself a failure. In contrast, a unit starting for a short interval, shutting down, and restarting repeatedly may be short cycling. Repeated starts can arise from control settings, sensor placement, airflow problems, minimum output above the current load, or protection events. But not every brief cycle means the same defect.

A useful log records the indoor temperature, thermostat setpoint, outdoor temperature, compressor or outdoor-unit run state, auxiliary heat state, and the electrical demand where it can be measured appropriately. A smart thermostat's 'heating' display may not mean the compressor is active. Likewise, a fan may circulate air when no significant heat is being added. You need to know what each recorded state means for that particular system.

The basic energy balance is straightforward. At a steady indoor temperature, heat delivered must roughly match heat escaping through the envelope and ventilation. During warm-up, delivered heat must also replenish energy stored in air, walls, furniture, and floors. A house can require a large amount of heat to recover from a setback even when its normal steady load is modest.

### Electrical demand is not the same as heat output

A heat pump moves thermal energy using electricity. Under favorable conditions, it can deliver several units of heat per unit of electrical energy, though the ratio varies with temperature, speed, and operating mode. Electrical resistance heat converts electrical energy into heat directly, close to one unit of heat per unit of electricity at the appliance. Thus, two homes receiving similar heating can have very different electric demand if one relies frequently on resistance backup.

Demand is power at an instant, often measured in kilowatts. Consumption is energy over time, measured in kilowatt-hours. Imagine a system drawing two kilowatts for five hours. It consumes ten kilowatt-hours. A four-kilowatt auxiliary heater operating for one hour adds four kilowatt-hours. The larger peak may matter under demand-based pricing, while total energy determines much of an ordinary energy bill. This illustrative arithmetic does not tell you how much heat each device actually delivered.

When a thermostat jumps several degrees upward on a cold morning, some systems respond by engaging auxiliary heat to recover quickly. Other systems stage equipment differently. A strategy that appears sensible for a furnace may be costly for a heat pump with electric resistance backup. But avoiding all setbacks is not a universal rule: system design, climate, occupancy, electricity tariffs, and control algorithms matter. The defensible method is to observe measured performance under comparable weather and occupancy rather than declare every heat pump should use one schedule.

### Defrost and recovery can look like faults

In cold damp weather, frost forms on an outdoor coil during heating. Many heat pumps periodically reverse the refrigeration cycle or use another designed method to clear frost. During defrost, normal supply-air temperature and outdoor-unit behavior may temporarily change; some systems run auxiliary heat for comfort. A transient dip or demand spike during a defrost event need not indicate a failed compressor.

Persistent heavy ice that is not cleared, repeated protection trips, unusually weak heat output, or very frequent defrost under mild conditions are different concerns. Those patterns justify equipment-specific diagnosis, including airflow, sensor states, refrigerant circuit behavior, and defrost controls. Refrigerant-side pressure readings and charging cannot be interpreted responsibly without the correct operating mode, manufacturer procedures, and qualified service practices.

It also matters where you measure temperature. A thermostat in a warm hallway may turn heat off while a north bedroom stays cold. Occupants may then raise the setpoint, causing longer recovery and perhaps auxiliary heat, even though the real problem is uneven heat distribution or room-level heat loss.

### Separate four explanations using one log

Suppose consumption rises after a cold weekend. First, the outside temperature may simply have increased the heating load. Second, a larger setback may have created a morning recovery peak. Third, auxiliary heat may have operated because of equipment settings or a malfunction. Fourth, airflow or sensor faults may have reduced efficient heat delivery. A daily total cannot distinguish these possibilities. Plot the temperature difference across the envelope, thermostat commands, equipment states, and electrical demand through time. Mark defrost events and setbacks explicitly.

Normalize comparisons for weather as carefully as practical. Two days with different outdoor temperatures, solar gain, wind, and occupancy are not equivalent experiments. Weather normalization helps separate changes in building load from changes in system operation, but it will not remove every confounding factor. Electricity from hot-water heating, appliances, and vehicle charging can further obscure a whole-house meter trace.

After any control adjustment, verify comfort as well as energy. A setting that saves a few kilowatt-hours but leaves the house below its intended temperature is not a successful efficiency improvement. Nor is a setting that suppresses necessary defrost or protection. Preserve the system's safety logic and use appropriate service procedures.

The skill here is to interpret a heat pump as a controlled energy system. Long runtime, repeated starts, rapid setpoint recovery, and defrost are distinct behaviors. Measure when and why power is used, connect that usage to the building's heat requirement, and distinguish compressor heat from supplemental resistance heat. That makes a winter bill a source of hypotheses rather than a reason to replace equipment prematurely.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Thermostats, Controls, and Diagnostic Patterns

**Track:** HVAC and Refrigeration. **Background:** Heating and cooling loads, airflow, refrigeration, and humidity. **Purpose:** understand the control loop, staging, and evidence needed to diagnose system behavior.

#### Technical companion (non-spoken)

##### Conceptual heat-balance model

`C dT/dt = Q_delivered − UA(T_indoor − T_outdoor) − Q_other_losses + Q_internal` for a simplified single-zone model. `C` summarizes effective thermal capacitance; the real building is multi-zone and has additional moisture and ventilation states. This is a reasoning tool, not a sizing method.

##### Time-stamped observation sheet

Record timestamp, indoor sensor temperature, independent room temperature, target, outdoor temperature, stage/fan status, fault indicator and comfort observation. Compare the **call** with the **actual equipment state** and **temperature trend**. Note any documented startup, anti-short-cycle or defrost interval.

**Review boundary:** Do not bypass interlocks or infer wiring terminals from generic diagrams. Manufacturer sequences, refrigerant handling, fuel-burning equipment and local requirements must be evaluated separately.

#### Selected reading and evidence records (non-spoken)

- `doe-heatpump-thermostat` — [US Department of Energy, Purchasing Energy-Efficient Residential Air-Source Heat Pumps](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-air-source-heat-pumps). Heat pump control, auxiliary resistance heat, and thermostat recovery behavior.
- `ashrae-2025-res-loads` — [ASHRAE Handbook—Fundamentals (2025), Chapter 17, Residential Cooling and Heating Load Calculations](https://handbook.ashrae.org/handbooks/F25/IP/F25_Ch17/F25_Ch17_ip.aspx). Residential sensible and latent loads, short cycling and dehumidification.
- `energystar-ducts` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Duct leakage as an energy and air delivery problem.

### Heat Pump Defrost, Cold Weather, and Controls

### 010000 — Heat Pump Defrost, Cold Weather, and Controls

#### Technical companion (non-spoken)

##### System boundary and definitions

- Heating mode: outdoor coil functions as evaporator; indoor coil functions as condenser in a typical reversible vapor-compression arrangement.
- Frost when coil surface is below freezing and air moisture can deposit or freeze there. Ambient temperature alone is not sufficient to predict frosting.
- Reverse-cycle defrost sends heat to outdoor coil; user-visible behavior differs by manufacturer and control strategy.
- Seasonal efficiency includes defrost, fan energy, standby effects, and supplemental heat. Avoid comparing heating COP at one test point with seasonal performance.

##### Diagnostic contrast

| Observation | Hypotheses to investigate |
|---|---|
| Frost clears in normal cycle | Expected defrost behavior |
| Coil remains iced | Defrost sensor/control, refrigerant, airflow, or installation fault |
| Ice accumulates below unit | Meltwater path, snow clearance, mounting, roof dripline |
| Auxiliary heat remains on | Controller setting, sizing/temperature, service issue; check equipment literature |

##### Review boundary

Refrigerant handling and charge checks require appropriate qualifications. Model-specific service manuals, local electrical requirements, and weather/installation details govern commissioning. The evidence supports mechanisms, not a universal defrost timing threshold.

#### Selected reading and evidence records (non-spoken)

- `nrel-winkler-ramaraj-defrost` — [Jon Winkler and Sugi Ramaraj, Field Validation of Air-Source Heat Pumps for Cold Climates, National Renewable Energy Laboratory (2023)](https://heatpumpdata.energy.gov/system/files/files/cchp-2024-09/Winkler%20Ramaraj%20-%202023%20-%20Field%20Validation%20of%20Air-Source%20Heat%20Pumps%20for%20Cold%20Climates.pdf). Sections 4.1.6 and 5.6: reverse-cycle defrost, coil frost and energy impact; installation-dependent evidence
- `energystar-ashp` — [ENERGY STAR, Air-Source Heat Pumps](https://www.energystar.gov/products/air_source_heat_pumps). Heating and cooling by reversing heat-transfer direction
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance

### Duct Leakage, Zoning, and Temperature Imbalance

### 011000 — Duct Leakage, Zoning, and Temperature Imbalance

#### Technical companion (non-spoken)

##### Simplified heat-delivery relationship

For steady sensible heat transport, \(\dot Q_{sensible} \approx \dot m c_p (T_{supply}-T_{room})\). This omits latent heat, mixing, transients, duct losses, and register measurement uncertainty. Duct resistance, blower curve, and air-side equipment specifications jointly determine usable air delivery.

##### Comparative experiment

Record room-to-hallway pressure differences with door open and closed using an appropriate low-range manometer, and record equipment state. Compare supply and return assumptions without modifying electrical or combustion equipment. Do not infer whole-system leakage from one pressure reading.

##### Evidence and boundaries

US DOE and ENERGY STAR duct-sealing and ventilation sources; ACCA load-calculation methodology; EPA indoor air guidance. Local construction and commissioning standards, manufacturer airflow limits, and duct leakage requirements differ; an HVAC specialist may be needed for airflow measurement, system changes, and safety-critical commissioning.

#### Selected reading and evidence records (non-spoken)

- `energystar-ducts` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Duct leakage as an energy and air delivery problem.
- `ca-hvac-pressure` — [California Energy Commission, Residential Compliance Manual: Chapter 4 HVAC, Air Distribution](https://www.energy.ca.gov/filebrowser/download/5126). Fan pressure budget, filter pressure drop, coil, ducts and registers.
- `acca-manual-j` — [Air Conditioning Contractors of America, ANSI/ACCA 2 Manual J: Residential Load Calculation](https://www.acca.org/standards/technical-manuals/manual-j). Room and whole-building heating/cooling design load factors.
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.

### Variable-Speed Equipment, Sensors, and Control Modes

### 015000 — Variable-Speed Equipment, Sensors, and Control Modes

#### Technical companion (non-spoken)

##### Control-state log

| Timestamp | Outdoor / indoor condition | Commanded mode and capacity | Relevant sensor readings | Observed delivery |
|---|---|---|---|---|
| Morning recovery | Warm-up load may be high | Compressor stage / auxiliary status | Thermostat + return / supply if accessible | Room warm-up rate |
| Mild steady-state | Low load | Low or cycling capacity | Humidity, fan speed / static-pressure indication | Stable comfort / dew point |
| Defrost interval | Frost conditions | Defrost mode and timed transitions | Coil/outdoor sensors; equipment log | Indoor delivery changes |

Distinguish commanded fan percentage from measured airflow, and named compressor speed from delivered capacity. A continuous run is not evidence of inefficiency by itself.

**Technical boundary:** Refrigerant and high-voltage testing, safety interlocks, charge adjustment, and equipment configuration require model-specific service procedures and appropriately qualified personnel; source material does not certify a field diagnostic process.

#### Selected reading and source locators (non-spoken)

- `doe-heatpumps` — [U.S. Department of Energy, Pump Up Your Savings With Heat Pumps](https://www.energy.gov/articles/pump-your-savings-heat-pumps). Heat transfer rather than direct heat generation.
- `doe-thermal-systems-guide` — [U.S. DOE Better Buildings, Decarbonizing Building Thermal Systems: A How-to Guide for Heat Pump Systems and Beyond](https://betterbuildingssolutioncenter.energy.gov/sites/default/files/attachments/87812.pdf). Inverter-based variable-speed compressors, feedback sensor controls and capacity modulation.
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.
- `ashrae-2025-res-loads` — [ASHRAE Handbook—Fundamentals (2025), Chapter 17, Residential Cooling and Heating Load Calculations](https://handbook.ashrae.org/handbooks/F25/IP/F25_Ch17/F25_Ch17_ip.aspx). Residential sensible and latent loads, short cycling and dehumidification.
- `doe-heatpump-thermostat` — [US Department of Energy, Purchasing Energy-Efficient Residential Air-Source Heat Pumps](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-air-source-heat-pumps). Heat pump control, auxiliary resistance heat, and thermostat recovery behavior.

### Diagnosing Comfort Complaints with Occupancy and Sensor Logs

### 016000 — Diagnosing Comfort Complaints with Occupancy and Sensor Logs

#### Technical companion (non-spoken)

**Minimum log columns:** timestamp and timezone; two representative room temperatures; indoor humidity; outdoor temperature/weather; setpoint; heating/cooling/fan call; door and shade position; occupancy or unusual internal loads; interventions. Before comparison, co-locate temperature sensors to estimate offset and response lag.

**Sensible airflow relation (illustrative):** `Qdot ≈ ρ × c_p × Vdot × (T_supply − T_room)`; requires credible airflow data. A large `ΔT` without `Vdot` does not establish heat delivery. A cold radiant surface may cause discomfort despite acceptable air temperature.

**Diagnostic branches:** solar-correlated rise → investigate shading/load; wind-correlated drop → investigate envelope; closed-door divergence → investigate air path; all-room drift with continuous calls → review capacity or controls. None is a definitive diagnosis without direct measurements.

**Scope:** Airflow balance, combustion, refrigerant, and electrical work involve professional procedures and manufacturer-specific requirements.

#### Selected reading and source locators (non-spoken)

- `energystar-ducts` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Duct leakage as an energy and air delivery problem.
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.
- `ashrae-2025-res-loads` — [ASHRAE Handbook—Fundamentals (2025), Chapter 17, Residential Cooling and Heating Load Calculations](https://handbook.ashrae.org/handbooks/F25/IP/F25_Ch17/F25_Ch17_ip.aspx). Residential sensible and latent loads, short cycling and dehumidification.
- `ca-hvac-pressure` — [California Energy Commission, Residential Compliance Manual: Chapter 4 HVAC, Air Distribution](https://www.energy.ca.gov/filebrowser/download/5126). Fan pressure budget, filter pressure drop, coil, ducts and registers.

### Heat Pump Cycling, Recovery, and Electrical Demand

### 017000 — Heat Pump Cycling, Recovery, and Electrical Demand

#### Technical companion (non-spoken)

**Key quantities:** instantaneous power P in kW; energy E in kWh = sum of power × duration; approximate COP = delivered heat / electrical input in consistent energy units. Cycling counts, compressor runtime, defrost events, auxiliary-heat runtime, and weather should be logged separately.

**Illustrative log:** 06:00 setback ends, setpoint jumps by 3 °C; 06:04 compressor starts; 06:06 auxiliary heat starts; 06:37 auxiliary heat ends; 07:10 setpoint achieved. This is a hypothetical sequence; it is not proof that the system is configured incorrectly.

**Interpretation table:** Long stable low-power cycles may be normal for variable speed. Frequent rapid starts can suggest short cycling. Periodic defrost in moist cold weather is expected; persistent ice or protective shutdown requires equipment diagnosis. Auxiliary heat may be intentional or a symptom depending on controls and load.

**Boundaries:** Do not defeat freeze, pressure, overcurrent or refrigerant controls. Metering mains demand and servicing refrigerant circuits require appropriate equipment and qualifications. Some measured setback studies are limited by their sample size and site conditions; do not generalize them to every climate and system.

#### Selected reading and source locators (non-spoken)

- `doe-heatpumps` — [U.S. Department of Energy, Pump Up Your Savings With Heat Pumps](https://www.energy.gov/articles/pump-your-savings-heat-pumps). Heat transfer rather than direct heat generation.
- `energystar-ashp` — [ENERGY STAR, Air-Source Heat Pumps](https://www.energystar.gov/products/air_source_heat_pumps). Heating and cooling by reversing heat-transfer direction.
- `doe-heatpump-thermostat` — [US Department of Energy, Purchasing Energy-Efficient Residential Air-Source Heat Pumps](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-air-source-heat-pumps). Heat pump control, auxiliary resistance heat, and thermostat recovery behavior.
- `nrel-winkler-ramaraj-defrost` — [Jon Winkler and Sugi Ramaraj, Field Validation of Air-Source Heat Pumps for Cold Climates, National Renewable Energy Laboratory (2023)](https://heatpumpdata.energy.gov/system/files/files/cchp-2024-09/Winkler%20Ramaraj%20-%202023%20-%20Field%20Validation%20of%20Air-Source%20Heat%20Pumps%20for%20Cold%20Climates.pdf). Sections 4.1.6 and 5.6: reverse-cycle defrost, coil frost and energy impact; installation-dependent evidence.
