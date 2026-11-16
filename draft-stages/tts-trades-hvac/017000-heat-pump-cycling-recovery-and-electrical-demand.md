# 017000 — Heat Pump Cycling, Recovery, and Electrical Demand

<!-- BEGIN SPOKEN LECTURE -->

An electric utility bill rises sharply during a winter cold spell. The heat pump appears to be running most of the day. A homeowner wonders whether that means the equipment is failing, too small, or simply working hard. The answer cannot be read from runtime alone. We have to distinguish delivered heat, electrical power, control strategy, and how quickly the house loses energy to outdoors.

## Continuous operation and short cycling are different observations

A variable-speed heat pump may operate for long periods at reduced output. That can be normal: instead of switching fully on and off, it matches heat delivery more closely to the building's changing load. Long runtime is not itself a failure. In contrast, a unit starting for a short interval, shutting down, and restarting repeatedly may be short cycling. Repeated starts can arise from control settings, sensor placement, airflow problems, minimum output above the current load, or protection events. But not every brief cycle means the same defect.

A useful log records the indoor temperature, thermostat setpoint, outdoor temperature, compressor or outdoor-unit run state, auxiliary heat state, and the electrical demand where it can be measured appropriately. A smart thermostat's 'heating' display may not mean the compressor is active. Likewise, a fan may circulate air when no significant heat is being added. You need to know what each recorded state means for that particular system.

The basic energy balance is straightforward. At a steady indoor temperature, heat delivered must roughly match heat escaping through the envelope and ventilation. During warm-up, delivered heat must also replenish energy stored in air, walls, furniture, and floors. A house can require a large amount of heat to recover from a setback even when its normal steady load is modest.

## Electrical demand is not the same as heat output

A heat pump moves thermal energy using electricity. Under favorable conditions, it can deliver several units of heat per unit of electrical energy, though the ratio varies with temperature, speed, and operating mode. Electrical resistance heat converts electrical energy into heat directly, close to one unit of heat per unit of electricity at the appliance. Thus, two homes receiving similar heating can have very different electric demand if one relies frequently on resistance backup.

Demand is power at an instant, often measured in kilowatts. Consumption is energy over time, measured in kilowatt-hours. Imagine a system drawing two kilowatts for five hours. It consumes ten kilowatt-hours. A four-kilowatt auxiliary heater operating for one hour adds four kilowatt-hours. The larger peak may matter under demand-based pricing, while total energy determines much of an ordinary energy bill. This illustrative arithmetic does not tell you how much heat each device actually delivered.

When a thermostat jumps several degrees upward on a cold morning, some systems respond by engaging auxiliary heat to recover quickly. Other systems stage equipment differently. A strategy that appears sensible for a furnace may be costly for a heat pump with electric resistance backup. But avoiding all setbacks is not a universal rule: system design, climate, occupancy, electricity tariffs, and control algorithms matter. The defensible method is to observe measured performance under comparable weather and occupancy rather than declare every heat pump should use one schedule.

## Defrost and recovery can look like faults

In cold damp weather, frost forms on an outdoor coil during heating. Many heat pumps periodically reverse the refrigeration cycle or use another designed method to clear frost. During defrost, normal supply-air temperature and outdoor-unit behavior may temporarily change; some systems run auxiliary heat for comfort. A transient dip or demand spike during a defrost event need not indicate a failed compressor.

Persistent heavy ice that is not cleared, repeated protection trips, unusually weak heat output, or very frequent defrost under mild conditions are different concerns. Those patterns justify equipment-specific diagnosis, including airflow, sensor states, refrigerant circuit behavior, and defrost controls. Refrigerant-side pressure readings and charging cannot be interpreted responsibly without the correct operating mode, manufacturer procedures, and qualified service practices.

It also matters where you measure temperature. A thermostat in a warm hallway may turn heat off while a north bedroom stays cold. Occupants may then raise the setpoint, causing longer recovery and perhaps auxiliary heat, even though the real problem is uneven heat distribution or room-level heat loss.

## Separate four explanations using one log

Suppose consumption rises after a cold weekend. First, the outside temperature may simply have increased the heating load. Second, a larger setback may have created a morning recovery peak. Third, auxiliary heat may have operated because of equipment settings or a malfunction. Fourth, airflow or sensor faults may have reduced efficient heat delivery. A daily total cannot distinguish these possibilities. Plot the temperature difference across the envelope, thermostat commands, equipment states, and electrical demand through time. Mark defrost events and setbacks explicitly.

Normalize comparisons for weather as carefully as practical. Two days with different outdoor temperatures, solar gain, wind, and occupancy are not equivalent experiments. Weather normalization helps separate changes in building load from changes in system operation, but it will not remove every confounding factor. Electricity from hot-water heating, appliances, and vehicle charging can further obscure a whole-house meter trace.

After any control adjustment, verify comfort as well as energy. A setting that saves a few kilowatt-hours but leaves the house below its intended temperature is not a successful efficiency improvement. Nor is a setting that suppresses necessary defrost or protection. Preserve the system's safety logic and use appropriate service procedures.

The skill here is to interpret a heat pump as a controlled energy system. Long runtime, repeated starts, rapid setpoint recovery, and defrost are distinct behaviors. Measure when and why power is used, connect that usage to the building's heat requirement, and distinguish compressor heat from supplemental resistance heat. That makes a winter bill a source of hypotheses rather than a reason to replace equipment prematurely.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Key quantities:** instantaneous power P in kW; energy E in kWh = sum of power × duration; approximate COP = delivered heat / electrical input in consistent energy units. Cycling counts, compressor runtime, defrost events, auxiliary-heat runtime, and weather should be logged separately.

**Illustrative log:** 06:00 setback ends, setpoint jumps by 3 °C; 06:04 compressor starts; 06:06 auxiliary heat starts; 06:37 auxiliary heat ends; 07:10 setpoint achieved. This is a hypothetical sequence; it is not proof that the system is configured incorrectly.

**Interpretation table:** Long stable low-power cycles may be normal for variable speed. Frequent rapid starts can suggest short cycling. Periodic defrost in moist cold weather is expected; persistent ice or protective shutdown requires equipment diagnosis. Auxiliary heat may be intentional or a symptom depending on controls and load.

**Boundaries:** Do not defeat freeze, pressure, overcurrent or refrigerant controls. Metering mains demand and servicing refrigerant circuits require appropriate equipment and qualifications. Some measured setback studies are limited by their sample size and site conditions; do not generalize them to every climate and system.

## Selected reading and source locators (non-spoken)

- `doe-heatpumps` — [U.S. Department of Energy, Pump Up Your Savings With Heat Pumps](https://www.energy.gov/articles/pump-your-savings-heat-pumps). Heat transfer rather than direct heat generation.
- `energystar-ashp` — [ENERGY STAR, Air-Source Heat Pumps](https://www.energystar.gov/products/air_source_heat_pumps). Heating and cooling by reversing heat-transfer direction.
- `doe-heatpump-thermostat` — [US Department of Energy, Purchasing Energy-Efficient Residential Air-Source Heat Pumps](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-air-source-heat-pumps). Heat pump control, auxiliary resistance heat, and thermostat recovery behavior.
- `nrel-winkler-ramaraj-defrost` — [Jon Winkler and Sugi Ramaraj, Field Validation of Air-Source Heat Pumps for Cold Climates, National Renewable Energy Laboratory (2023)](https://heatpumpdata.energy.gov/system/files/files/cchp-2024-09/Winkler%20Ramaraj%20-%202023%20-%20Field%20Validation%20of%20Air-Source%20Heat%20Pumps%20for%20Cold%20Climates.pdf). Sections 4.1.6 and 5.6: reverse-cycle defrost, coil frost and energy impact; installation-dependent evidence.
