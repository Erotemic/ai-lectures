# 013000 — Heating System Commissioning: Supply, Controls, and Documentation

<!-- BEGIN SPOKEN LECTURE -->

A new heating system warms the thermostat to its setpoint. Is it commissioned? Not necessarily. The thermostat reports conditions at one location. The system might be delivering too little heat to distant rooms, circulating water inefficiently, short cycling, or operating with unsafe combustion conditions. Installation establishes that equipment is connected. Commissioning establishes, with recorded evidence, that it works as intended in the building where it was installed.

Commissioning is often confused with startup. Startup turns equipment on, checks that obvious faults are absent, and verifies basic operation. Commissioning relates observed performance to specified design intent: capacity, airflow or water flow, temperature differences, control sequences, and safety devices. It also produces the information that a future technician will need. A system can appear comfortable on a mild day and perform poorly under winter design conditions.

## Define the design before testing

A heating load is the rate at which a building loses heat under specified indoor and outdoor conditions. Heat moves through the enclosure and is carried away by ventilation and infiltration. If equipment is chosen without an estimate of those losses, the installation may be oversized, undersized, or mismatched to distribution capacity. An oversized burner may hit the room setpoint rapidly and then stop, but frequent starts and stops are not automatically evidence of good heating.

The commissioning plan should name the intended temperature conditions, equipment type, distribution system, and control sequence. With forced air, airflow through the heat exchanger or coil matters. With hydronic heating, water flow, supply and return temperature, pressure, air removal, and terminal-unit performance matter. The targets come from design calculations and manufacturer documentation, not a universal temperature difference copied from another home.

## Heat carried by air or water

Consider a hydronic loop. Warm water leaves the heat source, gives up energy to radiators or tubing, and returns cooler. The rate of heat transfer depends on both flow and temperature drop. A very high temperature difference can indicate strong heat delivery at the intended flow, but it can also indicate inadequate flow in a poorly balanced loop. A small difference may mean a room is already warm, an oversized flow rate, or an exchanger that is not transferring expected heat. Temperature alone is ambiguous.

The same principle holds for air. Supply temperature does not reveal heat delivery unless airflow is known. A duct may deliver hot air at the register yet move too little of it to satisfy the room load. Closing registers to force more air elsewhere can change system static pressure and produce consequences at the fan or other branches. We want measurements of both transport quantity and temperature, followed by reasoning about the full network.

Balancing is the process of distributing flow where needed. It begins with a plan for target room loads and branch flows, not with endlessly adjusting dampers until someone says the house feels better. A distant radiator may be cool because the pump lacks useful head, air is trapped, a valve is closed, or the terminal has little temperature difference from the room. These mechanisms require different corrections.

## Controls are a sequence, not a box

A modern heating system includes sensors and decisions: thermostat demand, operating mode, boiler or compressor start conditions, circulation commands, safety limits, and minimum run times. A heat pump in cold weather may temporarily enter defrost. A boiler may prioritize domestic hot water before space heating. Two zones may call at once and change the available flow. Commissioning should observe meaningful combinations of these states, not only one full-heat command.

A simple functional test can start from a satisfied thermostat, raise the call for heat, record the sequence in which equipment and circulators respond, and then observe how the system ends the call. For a zoned system, repeat with each zone and appropriate combinations. Confirm that a loss of sensor signal or a limit trip produces the intended documented response. Safety devices are part of the system's design; do not defeat them to make equipment run.

Combustion appliances demand special treatment. Flue integrity, adequate combustion air, venting, gas connections, and carbon-monoxide risk cannot be inferred from warm registers or a steady flame. The commissioning plan must include the manufacturer's required combustion and safety checks performed with suitable instruments and qualified practice. Ventilation and pressure interactions with the building are relevant because exhaust fans and tight envelopes can affect some installations.

## Record baseline performance

A useful commissioning record names the make and model, equipment settings, filter or strainer conditions, measured temperatures, pressures, electrical readings where applicable, zone behavior, and relevant control parameters. Include the date and outdoor conditions; a heating system's readings change with the weather and load. Record what could not be tested in the season of installation and how it will be evaluated later.

Suppose a complaint arises months afterward: the north bedroom is cold. The technician can compare current register flow, supply temperature, damper position, and thermostat behavior with the commissioning baseline. Without those numbers, diagnosis starts from memory and guesswork. Documentation converts a one-time installation into a maintainable system.

Commissioning is not a claim that every room will always have identical temperature. Solar gains, occupancy, open doors, and weather create legitimate variations. It is a demonstration that the system's controls, distribution, and heat source respond coherently under the conditions examined. A warm house is the outcome people notice. Commissioning is how we learn why it is warm, whether the system is performing as intended, and what evidence remains when it no longer does.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Heat-transfer relationship

For a liquid loop, `Q_dot = m_dot × c_p × (T_supply - T_return)`, where flow is mass per time and `c_p` is specific heat. A representative water-flow relationship in common US hydronics units is `BTU/h ≈ 500 × GPM × ΔT(°F)` near typical water properties; glycol solutions require different properties. This expression does **not** independently diagnose poor flow without design targets.

### Commissioning record fields

Design load and distribution plan; manufacturer setpoints; filter/strainer status; external static pressure and flow (air), or pump head/flow and air purge status (hydronic); supply/return temperatures; zones and functional states; control response; safety test records; weather at test; unresolved seasonal tests.

**Editorial boundary:** Combustion testing, refrigerant adjustment, electrical checks, and pressure-vessel safety require qualified procedures. Manufacturer and adopted code requirements supersede conceptual examples.

## Selected reading and evidence records (non-spoken)

- `energystar-hvac-quality` — [ENERGY STAR, HVAC Quality Installation](https://www.energystar.gov/saveathome/heating-cooling/hvac-quality-installation). Load-based sizing, airflow, refrigerant charge and duct performance.
- `doe-ba-hvac-renovation-guide` — [U.S. Department of Energy Building America, Energy Renovations: HVAC, a Guide for Contractors (2011)](https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/hvac_guide.pdf). Hydronic heating distribution and zoning examples.
- `ashrae-residential-hydronics` — [ASHRAE, 2023 Handbook Fundamentals, Chapter 1 Residential Space Conditioning: Hydronic Heating Systems](https://handbook.ashrae.org/handbooks/A23/IP/a23_ch01/a23_ch01_ip.aspx). Hydronic terminal units, forced circulation and zone/manifold arrangements.
- `energystar-ducts` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Duct leakage as an energy and air delivery problem.
- `acca-manual-j` — [Air Conditioning Contractors of America, ANSI/ACCA 2 Manual J: Residential Load Calculation](https://www.acca.org/standards/technical-manuals/manual-j). Room and whole-building heating/cooling design load factors.
