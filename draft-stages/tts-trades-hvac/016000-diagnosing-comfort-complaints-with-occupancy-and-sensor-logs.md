# 016000 — Diagnosing Comfort Complaints with Occupancy and Sensor Logs

<!-- BEGIN SPOKEN LECTURE -->

A resident says the bedroom is cold in winter. The thermostat is set to seventy degrees, the heating equipment runs, and the technician measures warm air at a supply register. That sounds like a heating system doing its job. Yet the resident may still be right. The measured air, the heat actually delivered to the room, the temperature of the room's surfaces, and the comfort of the person lying near a cold window are four different things.

A diagnostic log should help us see those differences without treating every complaint as a failed thermostat.

## Begin with the time pattern

Ask when the room becomes uncomfortable. Is it cold only when the door is shut, when wind blows, during long overnight setbacks, or during the first hour after the heating system starts? Does the issue follow occupancy, daylight, outdoor temperature, or equipment runtime? A response that says 'always cold' may become much more informative when mapped onto a twenty-four-hour schedule.

A household system has several control signals. The thermostat makes a call for heat or cooling; equipment may stage or modulate its output; a fan may run at a separate speed; a hydronic pump or zone valve may respond; and the room's surfaces lag behind all of these. A temperature log without equipment state can make normal cycling look like instability. At minimum, record room temperature, a comparison room, central setpoint, equipment call or runtime, and outdoor conditions. Occupancy and door position are useful event annotations rather than burdensome continuous measurements.

A logger samples a local environment. If it rests in sunlight, against a cold exterior wall, or beside a humidifier, it is not a neutral witness. Two sensors that disagree may be measuring two different microclimates, or one may be biased. Before interpreting small differences, compare the sensors side by side in a representative interior location for long enough to stabilize. Note offsets and then place each in its intended room at similar height and away from direct air currents. Exact laboratory calibration is unnecessary for seeing a multi-degree pattern, but consistent placement is essential.

## Follow the heat balance

A room loses heat through the envelope and through outdoor air that enters it. It gains heat from the supplied system, people, appliances, sun, and adjacent rooms. Even if supply air is warm, the flow rate may be insufficient to balance the loss. Delivered sensible heating in an airflow system depends approximately on how much air moves through the register and how much warmer it is than the room. A twenty-degree temperature difference with very little airflow is not equivalent to a twenty-degree difference with plenty of airflow. Likewise, a return-air path blocked by a closed bedroom door can alter the pressure difference across the door and reduce intended circulation.

One practical comparison is a room that stays cold during long steady heating calls while a nearby room reaches setpoint. That can indicate a mismatch in local load and delivery. A room that starts cold but eventually catches up could instead be affected by system cycling, thermal mass, or recovery strategy. A room that is only uncomfortable on windy days suggests leakage or surfaces cooled by wind-driven exposure. These are hypotheses, not automatic repair prescriptions.

For cooling complaints, humidity complicates the story. Dry-bulb temperature alone does not show the moisture load. A system that satisfies temperature quickly may leave high humidity if dehumidification has been inadequate. Warm surfaces or direct sunlight can create radiant discomfort at an otherwise reasonable air temperature. A ceiling fan can improve perceived comfort through air motion without lowering the room's stored heat. Ask what the occupant actually experiences rather than relying entirely on the thermostat's integer display.

## Turn notes into a defensible experiment

Consider two bedrooms that share a zone. Over five similar nights, bedroom A falls below bedroom B only when A's door is closed. Record whether a supply or return path exists, the position of each register, and the pressure or airflow effect of closing the door. A qualified assessment may measure room-to-hall pressure difference under operating conditions. The point is not to declare every door must remain open; it is to recognize that a distribution system needs a complete air path, not merely a supply opening.

Now consider a different room. Its temperature rises on sunny days even when the air conditioner operates as it does elsewhere. A log of window exposure and afternoon temperature suggests solar gain, not just refrigerant charge. Changing the thermostat can hide the symptom while making the rest of the building too cold. A shading test, documented under comparable conditions, can isolate a large part of the load.

A good log records interventions. If a filter is replaced, if a damper is adjusted, or if insulation is added, mark the exact date and keep settings comparable before and after. Without a change log, an apparent improvement might be caused by milder weather. Weather normalization need not begin with a sophisticated model: compare periods with similar outdoor temperatures and clear descriptions of wind and solar exposure before claiming an effect.

## Know what the log cannot prove

A few thermometers do not measure duct leakage, refrigerant flow, combustion quality, or equipment capacity. A room-temperature curve is influenced by building heat storage and user behavior, so it cannot uniquely identify the fault. Also, a sensor used in automation can become a control input: relocating it may alter the system you're trying to observe. Distinguish passive measurement from experiments that change the control loop.

The practical outcome is a concise issue description a contractor can reproduce: 'On overnight heating calls below this outdoor temperature, the north bedroom stays four degrees colder than the hall; the difference grows with the door shut and the return path is constrained.' That is better than 'The furnace is bad,' because it preserves the evidence without inventing a cause. Comfort diagnostics improve when the resident's experience, the room's physical behavior, and the equipment's control timeline are considered together.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Minimum log columns:** timestamp and timezone; two representative room temperatures; indoor humidity; outdoor temperature/weather; setpoint; heating/cooling/fan call; door and shade position; occupancy or unusual internal loads; interventions. Before comparison, co-locate temperature sensors to estimate offset and response lag.

**Sensible airflow relation (illustrative):** `Qdot ≈ ρ × c_p × Vdot × (T_supply − T_room)`; requires credible airflow data. A large `ΔT` without `Vdot` does not establish heat delivery. A cold radiant surface may cause discomfort despite acceptable air temperature.

**Diagnostic branches:** solar-correlated rise → investigate shading/load; wind-correlated drop → investigate envelope; closed-door divergence → investigate air path; all-room drift with continuous calls → review capacity or controls. None is a definitive diagnosis without direct measurements.

**Scope:** Airflow balance, combustion, refrigerant, and electrical work involve professional procedures and manufacturer-specific requirements.

## Selected reading and source locators (non-spoken)

- `energystar-ducts` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Duct leakage as an energy and air delivery problem.
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.
- `ashrae-2025-res-loads` — [ASHRAE Handbook—Fundamentals (2025), Chapter 17, Residential Cooling and Heating Load Calculations](https://handbook.ashrae.org/handbooks/F25/IP/F25_Ch17/F25_Ch17_ip.aspx). Residential sensible and latent loads, short cycling and dehumidification.
- `ca-hvac-pressure` — [California Energy Commission, Residential Compliance Manual: Chapter 4 HVAC, Air Distribution](https://www.energy.ca.gov/filebrowser/download/5126). Fan pressure budget, filter pressure drop, coil, ducts and registers.
