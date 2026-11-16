# 006000 — Humidity, Dew Point, and Latent Cooling

**Track:** HVAC. **Background:** Heat pumps, load calculations, airflow, and ventilation. **Purpose:** distinguish moisture removal from sensible cooling and diagnose humidity problems mechanistically.

<!-- BEGIN SPOKEN LECTURE -->

# A cool room can still feel damp

An air conditioner lowers the temperature in a room, yet the walls sometimes feel clammy and the windows fog. The thermostat says the cooling system has met its goal. How can the room remain uncomfortable? Because dry-bulb temperature, the number most thermostats display, is only one state variable of indoor air. Water vapor matters too. Cooling a room and drying the air are related processes, but they are not identical.

Start with relative humidity. It compares actual water-vapor pressure with the saturation vapor pressure at the present temperature. As air cools, its capacity for water vapor at saturation becomes smaller. Even if no water is added or removed, relative humidity rises as temperature falls. Conversely, heating a fixed parcel of air can lower its relative humidity without removing a single molecule of water. That is why a humidity reading is meaningful only when considered together with temperature.

The dew point answers a different question. It is the temperature at which the existing water-vapor pressure would reach saturation. For a given air sample, lowering its temperature to the dew point invites condensation. A cold drink glass is a simple demonstration. In HVAC, the relevant cold surface is often the cooling coil.

## Sensible and latent heat

When a cooling coil is colder than the surrounding air, heat passes from the air to the refrigerant circuit. Part of the load is sensible heat: the energy associated with changing air temperature. Another part is latent heat: the energy involved when water vapor condenses into liquid. This second component is the reason an operating air conditioner usually needs a condensate drain.

Imagine two occupied rooms with the same air temperature. One is dry, the other has high moisture content from a shower, cooking, or outdoor air leakage. To make the second room equally comfortable, cooling may need to remove substantial water as well as reduce temperature. Cooling equipment has a finite total capacity that is divided, under particular operating conditions, between sensible and latent work. A thermostat that sees only temperature can stop the system before enough moisture has been removed.

A coil does not condense water just because the air is humid. Its surface must fall below the incoming air's dew point. Air speed, coil geometry, refrigerant conditions, and contact time affect both moisture removal and cooling. After condensation, water must be collected and drained without being blown back into the air or allowing microbial growth in a wet pan. A blocked drain can turn a comfort system into a water-damage problem.

## Oversizing can produce a cold, damp house

A larger air conditioner is not automatically a better dehumidifier. If equipment has too much sensible cooling capacity for the actual load, it may bring the room temperature down quickly and shut off. Short run times reduce the time available for sustained moisture removal, particularly when the coil must first become cold and wet. The result can be frequent cycling and a room that is cool but humid.

Equipment sizing therefore needs a calculation of design loads, not a guess from floor area alone. Local climate, glazing, shading, insulation, infiltration, occupancy, and internal moisture sources all affect the result. Variable-speed and staged systems can sometimes run longer at lower capacity while maintaining moisture removal, but their performance still depends on correct installation and controls.

Airflow is another tradeoff. Too little airflow across a cooling coil can make it excessively cold and risk icing, while too much airflow may reduce moisture removal under some conditions. Neither low nor high fan speed is a universal humidity fix. A diagnostic process checks the system design, filter condition, fan operation, coil condition, and condensate path before changing settings.

## Where the moisture comes from

An air conditioner cannot compensate indefinitely for an uncontrolled water source. Occupants add vapor through breathing, bathing, cooking, and drying clothes. Outdoor air entering through leaks or ventilation can carry a large moisture load in humid weather. Damp crawl spaces and wet building materials can add moisture. An improperly vented bathroom fan can deposit it directly into an attic.

Now consider an exhaust fan running in a tightly enclosed room. The removed air must be replaced. If the replacement comes through unsealed gaps from a humid crawl space, the fan may introduce a moisture problem while removing an odor. A balanced, intentional outdoor-air pathway can be easier to understand and control than uncontrolled leakage. But a ventilation system's benefits and latent load depend on climate and design. Energy-recovery and moisture-recovery devices are not interchangeable, and their behavior changes with seasonal conditions.

A dehumidifier primarily targets moisture rather than room temperature. It generally removes vapor at a cold coil and releases heat back to the room. That can reduce relative humidity while increasing room temperature. The heat is not a malfunction; the electrical energy consumed and the heat released from condensation must go somewhere. Dehumidification is therefore a separate design decision, especially in basements or shoulder seasons when moisture is present but there is little demand for cooling.

## Diagnose the state, not just the complaint

Suppose a room measures cool but has high relative humidity. First ask whether the measurement is reliable and where the sensor sits. Then check dew point or actual moisture content rather than treating relative humidity as a standalone amount of water. Record outdoor conditions, system run times, moisture-generating events, and whether condensate is being produced and drained. Look for obvious moisture ingress or disconnected ventilation.

Two rooms with the same relative humidity at different temperatures need not contain the same amount of vapor. A cold, damp basement may be near condensation on masonry even when an upstairs room at a higher temperature looks dry. The diagnostic goal is to understand both the air state and the temperatures of vulnerable surfaces.

Good HVAC practice follows energy and mass. Heat entering a room must be removed, and water vapor entering a room must either be exhausted, condensed, or otherwise controlled. Once you track those flows independently, the apparent paradox of a cool but damp room disappears.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Simplified energy and moisture balances

- Sensible cooling: `Q_s ≈ m_dot_air * c_p * (T_in - T_out)` under suitable approximations.
- Total cooling includes latent removal associated with condensed water mass and the corresponding enthalpy change; do not simply add air-temperature differences to obtain it.
- Relative humidity is `p_v / p_sat(T)`; dew point satisfies `p_sat(T_dew) = p_v`.

### Worked diagnostic thought experiment

A thermostat is satisfied after short cycles, but a hygrometer reports elevated indoor humidity. Consider short cycling, outdoor infiltration, over-ventilation, poor coil drainage, and a damp basement as competing explanations. Identify what measurement would test each one.

**Review boundary:** Equipment settings, appropriate RH bands, coil performance and allowable ventilation rates depend on climate, equipment and occupancy. Field recommendations require load calculation and system-specific assessment.

## Selected reading and evidence records (non-spoken)

- `ashrae-2025-res-loads` — [ASHRAE Handbook—Fundamentals (2025), Chapter 17, Residential Cooling and Heating Load Calculations](https://handbook.ashrae.org/handbooks/F25/IP/F25_Ch17/F25_Ch17_ip.aspx). Residential sensible and latent loads, short cycling and dehumidification.
- `epa-iaq-moisture` — [US EPA, Biological Contaminants and Indoor Air Quality: Moisture Control](https://www.epa.gov/indoor-air-quality-iaq/biological-contaminants-and-indoor-air-quality). Condensation, indoor humidity, and control of moisture sources.
