# 010000 — Heat Pump Defrost, Cold Weather, and Controls

<!-- BEGIN SPOKEN LECTURE -->

A heat pump is heating a house on a damp winter morning. The outdoor unit is covered in frost. Then the fan stops, a cloud of steam rises, and the compressor continues making noise. A few minutes later the fan starts and the house heats normally again. To someone accustomed to a furnace, this can resemble a breakdown. It may instead be a normal defrost cycle: the machine is temporarily spending heat to restore its ability to collect heat.

## Why frost forms on a machine that is heating

An air-source heat pump takes energy from outdoor air and moves it indoors using a refrigerant cycle. In heating mode, the outdoor coil is an evaporator. Refrigerant there must be at a temperature low enough to absorb heat from the air passing over the coil. The outside air might be above freezing while parts of the coil are below freezing. Water vapor can deposit on the cold surfaces as frost, or condense and then freeze. Frost restricts airflow and adds thermal resistance between outdoor air and the refrigerant.

This is why frost is not evidence that the machine stopped extracting heat. The coil needs to be colder than its heat source to absorb energy. What matters is whether frost accumulation remains within the system's ability to manage it. A uniformly white coating shortly before a defrost cycle is different from a solid ice block that builds around the base and obstructs the fan.

Outdoor temperature alone does not determine frost severity. Humidity, dew point, wind, coil temperature, airflow, load, and run time all contribute. In some climates, damp weather near freezing can produce substantial frost, while much colder, drier air supplies less moisture. A defrost algorithm based only on a wall clock cannot perfectly account for changing conditions.

## A reversible machine has two temporary jobs

A conventional reversible heat pump uses a four-way reversing valve to change which heat exchanger is rejecting heat and which is absorbing heat. For a common reverse-cycle defrost, the system temporarily routes hot refrigerant to the outdoor coil to melt accumulated ice. In effect, the refrigerant cycle briefly resembles cooling operation. Some systems employ additional control strategies; the exact sequence is model dependent.

During defrost, the outdoor fan may stop, making it easier to warm the coil. The indoor side can receive less heat or temporarily tend to cool, so a controller may stop an indoor fan, engage supplemental heat, or use other measures to limit cold air delivery. These are design choices, not universal behavior. Steam at the outdoor unit can be water vapor from melting frost, rather than smoke from a fault. Meltwater should have a path away from the base without freezing into a persistent obstruction.

A useful energy budget keeps three quantities separate: thermal energy delivered to the rooms, electrical energy consumed by the system, and thermal energy required to defrost the outdoor coil. During normal heating, a heat pump may deliver several units of heat for every unit of electrical input under particular rating conditions. Defrost consumes time and energy without providing the same useful heating to occupied space. A seasonal coefficient of performance therefore includes effects not visible in an idealized steady-state test.

## The thermostat is only one controller

The room thermostat asks for a temperature outcome. The refrigeration controls have to manage compressor operation, coil temperatures, pressure protections, fan speed, refrigerant metering, defrost initiation, and termination. Modern variable-speed systems may change compressor and fan operation continuously. A single displayed setpoint does not reveal every internal operating decision.

Older or simpler controls may schedule defrost according to accumulated compressor run time combined with temperature conditions. Demand defrost strategies use sensor measurements and control logic to infer when a cycle is worthwhile. Both approaches depend on correct sensors, airflow, and programming. A defective coil-temperature sensor can lead to unnecessary cycles or insufficient frost removal. A controller may also enforce minimum run times and delays that prevent destructive rapid cycling.

Some heat pumps have auxiliary electric resistance heating. Its presence does not mean the heat pump is ineffective, but unnecessary use can raise electricity consumption because resistance heating delivers approximately one unit of thermal energy per unit of electric energy at the point of use. A heat pump's performance depends on outdoor conditions, supply temperature, capacity, and system configuration. In a properly sized cold-climate system, low outdoor temperature alone should not be interpreted as proof that the unit must abandon heat-pump heating entirely.

## Distinguish frost, snow, and frozen drainage

Consider four symptoms. First: a thin frost layer accumulates, a brief cycle clears it, and operation resumes. That is consistent with normal defrost. Second: ice remains thick across much of the coil after repeated cycles. That suggests checking actual defrost performance, sensors, refrigerant operation, and airflow. Third: the coil clears but a thick slab of ice grows below the unit and eventually reaches the fan. That suggests meltwater drainage and installation geometry deserve attention. Fourth: the unit has poor airflow because leaves, snow, or other debris obstruct its intake or outlet. Defrost timing cannot compensate for a blocked air path.

A unit placed beneath a roof dripline may receive repeated meltwater from above that freezes on the coil or housing. A unit installed too close to a wall or hedge may recirculate cold discharge air or restrict flow. Snow accumulation changes available clearance. Location is part of machine performance. So are mounting height, drain configuration, and the design of an appropriate snow or ice management strategy.

## Diagnose by recording a complete cycle

A sensible service history includes outdoor temperature, humidity or weather, time between cycles, duration of defrost, whether frost clears, whether the fan behaves as expected, and whether condensate can leave the unit. Also record supply-air behavior and whether supplemental heating engages. One clip of the machine steaming is not enough to diagnose it. Nor is a single wattage reading: compressors and heaters can draw very different power at different moments.

Do not bypass protection controls or force refrigerant operations as a homeowner experiment. The observational distinction is valuable without doing that. A heat pump is a machine balancing heat transfer, humidity, and control logic. Defrost reveals that the outdoor coil is not an inert metal radiator. It interacts with the weather, and sometimes the most efficient way to keep heating the house is to interrupt heating briefly and clear the frost.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### System boundary and definitions

- Heating mode: outdoor coil functions as evaporator; indoor coil functions as condenser in a typical reversible vapor-compression arrangement.
- Frost when coil surface is below freezing and air moisture can deposit or freeze there. Ambient temperature alone is not sufficient to predict frosting.
- Reverse-cycle defrost sends heat to outdoor coil; user-visible behavior differs by manufacturer and control strategy.
- Seasonal efficiency includes defrost, fan energy, standby effects, and supplemental heat. Avoid comparing heating COP at one test point with seasonal performance.

### Diagnostic contrast

| Observation | Hypotheses to investigate |
|---|---|
| Frost clears in normal cycle | Expected defrost behavior |
| Coil remains iced | Defrost sensor/control, refrigerant, airflow, or installation fault |
| Ice accumulates below unit | Meltwater path, snow clearance, mounting, roof dripline |
| Auxiliary heat remains on | Controller setting, sizing/temperature, service issue; check equipment literature |

### Review boundary

Refrigerant handling and charge checks require appropriate qualifications. Model-specific service manuals, local electrical requirements, and weather/installation details govern commissioning. The evidence supports mechanisms, not a universal defrost timing threshold.

## Selected reading and evidence records (non-spoken)

- `nrel-winkler-ramaraj-defrost` — [Jon Winkler and Sugi Ramaraj, Field Validation of Air-Source Heat Pumps for Cold Climates, National Renewable Energy Laboratory (2023)](https://heatpumpdata.energy.gov/system/files/files/cchp-2024-09/Winkler%20Ramaraj%20-%202023%20-%20Field%20Validation%20of%20Air-Source%20Heat%20Pumps%20for%20Cold%20Climates.pdf). Sections 4.1.6 and 5.6: reverse-cycle defrost, coil frost and energy impact; installation-dependent evidence
- `energystar-ashp` — [ENERGY STAR, Air-Source Heat Pumps](https://www.energystar.gov/products/air_source_heat_pumps). Heating and cooling by reversing heat-transfer direction
- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance
