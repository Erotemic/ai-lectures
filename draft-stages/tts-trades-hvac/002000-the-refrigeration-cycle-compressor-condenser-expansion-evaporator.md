# 002000 — The Refrigeration Cycle: Compressor, Condenser, Expansion, Evaporator

**Track:** HVAC and Refrigeration. **Background:** Heat transfer, heat pumps and airflow. **Purpose:** follow energy and refrigerant through a vapor-compression system without confusing temperature, pressure and phase.

<!-- BEGIN SPOKEN LECTURE -->

# How a Heat Pump Moves Heat Uphill

A refrigerator keeps its interior cold while warming the room. An air conditioner cools indoor air while rejecting heat outdoors. A heat pump operated in heating mode does almost the opposite: it collects heat from a colder outside environment and delivers it into a warmer house. These machines appear to disobey the everyday rule that heat moves from hot to cold. They do not. They use work to maintain a cycle in which the refrigerant repeatedly changes pressure, temperature and phase, arranging for heat to enter at one place and leave at another.

There are four components worth knowing by name: evaporator, compressor, condenser, and expansion device. Their names describe functions, not fixed physical locations. In a reversible heat pump the indoor and outdoor coils exchange roles as the operating mode changes.

## Begin at the evaporator

Imagine refrigerant flowing through a coil that is colder than the surrounding air. Heat moves from the air into the refrigerant. As heat arrives, some liquid refrigerant can boil into vapor at the pressure maintained there. This coil is the evaporator. The refrigerant does not need to be as hot as boiling water. The boiling temperature of any substance depends on its pressure, and refrigerants are chosen so useful phase changes occur in the operating range of the machine.

A phase change carries a large amount of energy without requiring the temperature to climb greatly. That is why evaporation is a powerful means of moving heat. The air moving over the coil cools. If the coil surface is below the air's dew point, water may condense from the air; below freezing, frost may develop. The refrigeration system must manage these side effects, and an air conditioner must manage condensate drainage.

The compressor should receive vapor in ordinary vapor-compression operation, not a stream of liquid. Liquid reaching a compressor can cause mechanical damage because liquids are much less compressible than gases. Actual systems use control of refrigerant charge, expansion behavior and superheat to manage the operating conditions at the compressor inlet.

## What the compressor buys us

The compressor consumes electrical or mechanical work and raises the pressure of the refrigerant vapor. Compression generally raises its temperature as well. We have not made heat out of nothing; we have added energy to the refrigerant and changed its state so that it can reject heat at a temperature above the destination environment.

Picture the evaporator pulling heat from chilly outdoor air. The resulting vapor may be too cold to warm the house directly. The compressor raises its pressure and temperature. Now the refrigerant can pass through an indoor coil hotter than the room air and send heat across that temperature difference. In the heating mode, that indoor coil is the condenser.

## At the condenser, heat goes where it can

The condenser receives higher-pressure, hotter refrigerant and transfers energy to the sink, typically indoor air or water in heating mode. The refrigerant releases heat as it cools and condenses to liquid. The heat delivered at the condenser is the sum of heat gathered at the evaporator and work supplied to the compressor, neglecting smaller details for the moment.

That energy balance is the key to why a heat pump can move more heat into the home than the electric energy it uses. If an idealized system extracts two units of heat from outdoors and adds one unit of electrical work, it can deliver approximately three units indoors. The ratio of useful heating output to work input is its coefficient of performance, or C O P. In this example the heating C O P is three. Real C O P varies continuously with outdoor conditions, supply temperatures, compressor design, cycling, defrost, auxiliary heat and equipment boundaries. It is not a fixed promise about an individual installation.

## The expansion device closes the loop

After the condenser, the refrigerant is mostly high-pressure liquid. It passes through a restriction or metering device, such as an expansion valve. Pressure drops sharply; some of the liquid may flash into vapor and the mixture becomes colder. The device itself does not act like a tiny compressor running backward and recovering substantial work in ordinary systems. Throttling is approximately an enthalpy-conserving process. The colder low-pressure mixture then returns to the evaporator and absorbs heat again.

This sequence repeats: absorb heat, compress vapor, reject heat and condense, reduce pressure, absorb heat again. A textbook diagram draws a clean loop; operating systems contain fans, pumps, sensors, accumulators, reversing valves, refrigerant piping and electronic controls. Those additions help the real machine stay inside its useful operating envelope.

## Why the temperature lift matters

A heat pump serving low-temperature floor heating may work more efficiently than the same general technology required to produce very hot water, because the compressor often has to create a smaller temperature lift between source and sink. As outdoor air becomes colder, an air-source heat pump may have less available heat and may need greater compression lift. This is why rated heating performance is specified at particular conditions and why sizing cannot be reduced to one advertised efficiency number.

Airflow matters just as much as refrigerant-side physics. A clogged indoor filter or poorly designed duct can reduce heat transfer at a coil and alter refrigerant operating conditions. Dirty outdoor coils can do the same. Yet a room that feels underheated could also have a control, distribution, envelope or equipment-capacity problem. A cold room is a symptom; it is not a refrigerant diagnosis.

## Reversal and defrost

In cooling mode the indoor coil usually evaporates refrigerant and the outdoor coil condenses it. In heating mode a reversing valve changes the flow arrangement so the outdoor coil becomes the evaporator and the indoor coil the condenser. When humid outdoor air deposits frost on a cold outdoor coil, the equipment may temporarily enter a defrost sequence to melt it. This uses energy and changes the near-term heat delivered indoors. A white coating during certain winter conditions can be part of ordinary operation, while persistent ice, drainage problems or abnormal cycling may point to a fault. Context matters.

## Diagnose by following energy, not by memorizing sounds

A service technician uses the system's temperatures, pressures, electrical inputs, airflow, refrigerant specifications and control state to reason about operating conditions. One pressure reading cannot uniquely identify a fault. The same low heating output might arise from poor airflow, incorrect charge, a sensor problem, insufficient equipment capacity, extreme weather or an envelope that loses too much heat. The machine and the building must be analyzed together.

Return to the apparent paradox. A heat pump does not persuade heat to flow uphill unassisted. It arranges a cold evaporator where heat enters, a hot condenser where heat leaves, and a compressor that supplies the necessary work. Once you can mentally walk the loop, refrigeration stops being mysterious. It becomes a carefully managed account of energy, pressure and phase.

<!-- END SPOKEN LECTURE -->

## Technical companion: energy and state changes

For a steady simplified vapor-compression cycle, denote refrigerant state points as: `1` compressor inlet, `2` compressor outlet, `3` condenser outlet, `4` expansion-device outlet. Approximate specific enthalpy differences: compressor work `w_in = h2-h1`, condenser heat `q_hot = h2-h3`, evaporator heat `q_cold = h1-h4`, throttling `h3≈h4`. For heating, `COP_H ≈ q_hot/w_in`, with `q_hot ≈ q_cold+w_in`. Real auxiliary loads and system boundaries change system C O P.

**Working distinctions:** The evaporator is defined by absorbing heat into refrigerant and promoting evaporation; its *location* depends on mode. Refrigerant pressures and saturated temperatures depend on refrigerant identity and operating state, not universal numbers. The illustrative COP 3 is an energy-balance example, not a rated performance claim.

**Sources:** DOE/Better Buildings heat pump fundamentals and ENERGY STAR air-source heat pump guidance. Refrigerant handling, pressure testing, electrical work, charge adjustment and recovery are governed by specialized training, equipment manuals and environmental requirements; this lesson gives a functional model, not service instructions.

**Exercise:** Draw the four boxes of the refrigeration cycle. Label which two exchange heat with the surroundings, which consumes work, and where liquid/vapor is expected. Repeat for heating and cooling without renaming the components.

## Selected reading and evidence (non-spoken)

- `doe-heat-pump-cycle` — [U.S. DOE Better Buildings, Heat Pump Basics (2025)](https://betterbuildingssolutioncenter.energy.gov/sites/default/files/2025-08/Get%20Pumped%21%20-%20Slides.pdf). Schematic refrigeration cycle and component names.
- `iea-cycle` — [International Energy Agency, How a Heat Pump Works](https://www.iea.org/reports/the-future-of-heat-pumps/how-a-heat-pump-works). Heat pump work and output heat balances.
- `doe-heatpumps` — [U.S. Department of Energy, Pump Up Your Savings With Heat Pumps](https://www.energy.gov/articles/pump-your-savings-heat-pumps). Heat transfer rather than direct heat generation.
- `energystar-ashp` — [ENERGY STAR, Air-Source Heat Pumps](https://www.energystar.gov/products/air_source_heat_pumps). Heating and cooling by reversing heat-transfer direction.
