# 008000 — Equipment Sizing, Commissioning, and Performance Checks

**Track:** HVAC and Refrigeration. **Background:** heating and cooling loads, airflow, humidity, and controls. **Purpose:** distinguish a correctly selected machine from a correctly performing installed system.

<!-- BEGIN SPOKEN LECTURE -->

# A heat pump is not a promise printed on a box

A homeowner replaces an air conditioner with a newer unit that has an impressive efficiency rating. The house is still uncomfortable. Certain rooms remain hot, others become cold, the equipment cycles frequently, and the humidity stays high. Nothing in that story yet proves the unit is defective. The important distinction is between the rated performance of a product and the actual performance of a system after it has been installed in a building.

The building has a heating and cooling load that depends on weather, enclosure, internal gains, sunlight, ventilation, infiltration, and occupant behavior. The equipment has a capacity that changes with operating conditions. The distribution system must deliver that capacity to rooms. Controls decide when the equipment operates. Commissioning is the process of checking that all of those pieces work together according to a specified design, rather than merely observing that the fan turns on.

## First find the load

A load calculation estimates the rate of heating or cooling required at selected conditions. In the United States, residential designers commonly use ACCA Manual J or an accepted equivalent. Inputs include building geometry and orientation, envelope performance, glass areas, infiltration assumptions, and indoor and outdoor design conditions. A rule of thumb based only on square footage throws away much of the information that determines real demand.

Suppose a building has a calculated design heating load of twenty thousand British thermal units per hour at a particular outdoor temperature. That does not mean it requires a machine sold as 'twenty thousand Btu per hour' in every climate or at every operating point. A heat pump may deliver less capacity as outdoor temperature falls, and defrost and controls affect the system. Selection should use equipment performance data at the relevant conditions and account for the intended backup strategy. Likewise, cooling involves both sensible heat, which changes air temperature, and latent heat, which removes water vapor.

A very large unit is not automatically a better unit. Oversizing can produce short cycles, uneven comfort, and weak humidity control. An undersized unit may run continually and still fail to maintain the intended indoor condition during design weather. Variable-capacity equipment gives more flexibility, but does not erase distribution constraints or make flawed sizing irrelevant.

## Airflow is part of capacity

A fan must move air against the resistance of ducts, grilles, coils, and filters. This resistance is often summarized using external static pressure, but a pressure measurement alone is not a complete measurement of airflow. Fan curves and operating settings determine the relationship. A duct that is undersized or has multiple tight bends may starve a coil of air even though the compressor can move refrigerant perfectly well.

Low airflow can lead to poor temperature control, freezing in some cooling conditions, and ineffective delivery to distant rooms. Excessive airflow may reduce moisture removal or create noise and drafts. The correct target comes from the equipment manufacturer's performance requirements and the distribution design, not a universal airflow value copied from another system.

Duct leakage is an additional loss mechanism. Air supplied into an attic or drawn from a dusty crawlspace changes both efficiency and indoor-air conditions. A balanced-looking register layout does not prove that the network is sealed or that every room receives the design flow. Measurement at accessible points and comparison with specified values are essential.

## Refrigerant and controls complete the circuit

Refrigerant charge affects compressor and heat-exchanger performance. The commissioning process can include manufacturer-defined temperature, pressure, superheat, subcooling, or other tests as appropriate for the equipment and conditions. No single refrigerant-pressure reading establishes correct charge across all technologies or outdoor temperatures. Modern equipment may offer built-in diagnostic modes, but they still need interpretation in context.

Controls require similar care. A thermostat might be set correctly while its sensor is exposed to a hot wall or sunlight. An auxiliary heater might run due to staging settings rather than an equipment failure. A heat-pump defrost cycle can temporarily change the delivered air temperature without indicating a problem. A system diagnosis therefore records operating mode, outdoor and indoor conditions, measured airflow and temperatures, and whether the machine is at steady state.

## What does successful commissioning look like?

A useful handoff includes the design load and equipment selection rationale, manufacturer performance tables, duct and airflow verification, refrigerant commissioning records, control settings, and a demonstration of major modes. The homeowner should know where filters are, how to interpret ordinary changes such as defrost, what warning indicators mean, and which conditions should prompt service.

Imagine someone complaining that the main bedroom is too warm. Swapping the thermostat may have no effect if a long duct has insufficient flow or the room has a strong west-facing solar load. Ask which physical path is inadequate. Compare the calculated room load, measured delivery, duct loss, and control behavior. Correcting one component without testing the rest can move the symptom rather than resolve it.

An efficient piece of equipment is only a component of an efficient HVAC system. Commissioning makes that statement operational: we define expected performance, collect evidence under specified conditions, compare against the design, correct deviations, and leave a record that later technicians can use. Installation is not complete when the equipment starts. It is complete when its intended functions have been demonstrated.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Simplified selection thought experiment

A calculated heating load of `20,000 Btu/h` at a chosen outdoor design temperature is a **requirement**, not a model number. If manufacturer data give `15,000 Btu/h` at that temperature, there is a `5,000 Btu/h` shortfall to address through equipment selection, envelope work, or a designed supplemental heat strategy. Do not use a nominal capacity measured under different conditions as an equivalent value.

### Evidence table

| Design question | Record |
|---|---|
| Required heating/cooling output | Building/room load calculation and design conditions |
| Equipment can meet requirement | Capacity and efficiency tables at specified conditions |
| Air reaches rooms | Fan settings, duct layout, measured static pressure/airflow as applicable |
| Refrigeration circuit correct | OEM-defined commissioning data under valid test conditions |
| Control behavior correct | Mode/stage transition and sensor observations |

**Review boundary:** Refrigerant handling, combustion safety, electrical connections, and system commissioning are equipment-specific regulated technical work. The lecture teaches selection and evidence reasoning, not procedures for accessing charged circuits.

## Selected reading and evidence records (non-spoken)

- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.
- `acca-manual-j` — [Air Conditioning Contractors of America, ANSI/ACCA 2 Manual J: Residential Load Calculation](https://www.acca.org/standards/technical-manuals/manual-j). Room and whole-building heating/cooling design load factors.
