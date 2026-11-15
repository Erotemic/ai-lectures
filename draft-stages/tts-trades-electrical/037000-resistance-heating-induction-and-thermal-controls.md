# 037000 - Electric Heating: From Current to Temperature

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** energy and thermal calculations, equipment nameplates, control-block diagrams, and comparison of resistance, induction and heat-pump systems.

<!-- BEGIN SPOKEN LECTURE -->

# Electric Heating: From Current to Temperature

A baseboard heater, an electric kettle, an induction cooktop and a heat pump may all draw electric power, but they do not use electricity to deliver heat in the same way. Two deliberately turn electrical energy into thermal energy in a resistance. One uses changing magnetic fields to heat cookware. One moves thermal energy from one place to another with a refrigerant cycle.

Understanding these differences helps explain nameplate ratings, temperature controls, operating cost, circuit demand and the surprising fact that an electrically heated room can be called one hundred percent efficient while a heat pump supplying the same room can use much less electricity.

The starting point is not the appliance's appearance. It is the path from electrical input to useful heat, the path from that heat to the object or space being warmed, and the controller that regulates the process.

## A conductor that is meant to get hot

In ordinary wiring, heating is usually a loss to be controlled. In a resistance heater, it is the intended effect. Current through a resistive material dissipates power. For a fixed resistance, the familiar equations are power equals current squared times resistance, or voltage squared divided by resistance. The material's geometry and resistivity determine how that heat is distributed.

An electric element is designed around materials and geometry that can tolerate its intended operating temperature. It may be an alloy wire supported by electrical insulation, a sheathed element embedded in a thermally conducting medium, or a controlled resistive film. A kettle places heat close to water. A baseboard heater transfers heat to surrounding air and nearby surfaces. An electric oven uses elements and insulation to maintain a much hotter enclosed environment.

These systems differ in more than their wattage. Their operating temperatures and thermal paths are chosen for different purposes. The element has to reject heat as quickly, on average, as the control system allows it to produce heat. If the heat-transfer path changes, the element temperature can change even when the electrical input is unchanged.

A simplified heating equilibrium occurs when electrical input power equals heat lost to the environment. Before equilibrium, the net input raises the internal energy of the heated material. Thermal mass matters because energy must be stored in the material before its temperature changes. This is why a thin radiant element can respond quickly while a thick slab of heated concrete responds slowly even if the installed electrical power is large.

## Watts are the rate; kilowatt-hours are the accumulated energy

Imagine a portable heater rated at fifteen hundred watts. On a nominal one-hundred-twenty-volt supply, a simple resistive steady-state calculation gives twelve and a half amperes. That is a substantial instantaneous load, even if the heater operates for only part of an hour. A two-kilowatt heater on a two-hundred-thirty-volt supply would draw about eight point seven amperes under the same ideal assumptions.

Electrical energy is power integrated over time. If a fifteen-hundred-watt heater were on continuously for four hours, it would consume six kilowatt-hours. If a thermostat kept it energized only forty percent of those four hours, it would consume about two point four kilowatt-hours. That does not reduce its instantaneous current while the element is energized. Circuit demand, energy cost and thermostat duty cycle answer different questions.

A room's heating demand also changes with outdoor temperature, infiltration, insulation and occupant behavior. A thermostat cannot create extra heating capacity. It regulates how long the available heater runs in response to its measurements. If the heat loss from a building exceeds the available heating power under some condition, continuous operation may still fail to reach the requested temperature.

Heating elements are not always exactly constant resistances. Resistivity can depend on temperature. Some designs deliberately exploit a strong positive temperature coefficient, so the element's resistance increases as it warms. Others use separate temperature sensors, thermostats and high-limit devices to regulate or limit temperature. The difference matters when interpreting the relationship between nominal voltage, element resistance and operating power.

## The thermostat is only one part of thermal control

A room thermostat measures temperature at a particular location and decides whether to call for heat. The measured point may not represent every object or person in the room. A heated floor introduces delay because a large slab must gain or lose heat. A wall-mounted heater may warm nearby air more quickly than distant furniture. A radiant panel can change how warm a person feels before a room sensor reports much change.

Control systems therefore have different objectives. Some hold a roughly constant temperature through on-off cycling. Others vary delivered power, use multiple stages, or respond to a schedule. A setback schedule can save energy when lower temperatures reduce building losses, but for a system with significant thermal mass it may take time to restore comfort. The controller's settings should follow the physical response of the heated space rather than assuming every device responds instantly.

Separate protective devices may monitor abnormal temperatures. A high-temperature limit and a normal room thermostat are not interchangeable. The thermostat seeks comfort or process setpoint; a limit device addresses conditions outside intended operation. An appliance's nameplate, listing and instructions define what the installed product is designed to do and how it must be supplied and protected.

## One hundred percent is not the end of the efficiency discussion

At the point where an electric resistance heater operates inside a heated space, essentially all of its electrical input ultimately becomes heat within that space, assuming the energy does not escape directly elsewhere. In that specific sense, it is close to one hundred percent efficient at converting delivered electricity into local heat.

But that description answers only one question. It does not say how much electricity was used to generate and deliver the power. It does not say how well the building retains heat. And it does not compare the heater with another electrical machine that moves heat rather than producing it resistively.

A heat pump uses an electrically driven cycle to absorb thermal energy from a cooler source and release it into a warmer location. Its coefficient of performance, or COP, is useful heat delivered divided by electrical energy consumed. In a suitable operating condition, COP can be greater than one because the electricity powers heat transfer. A COP of three means three units of delivered heat per unit of electric input under the stated conditions. It does not violate conservation of energy: the other two units were extracted from the heat source.

COP changes with temperatures, equipment and operating conditions. It is not a permanent efficiency number printed on all winter days. The U.S. Department of Energy explains why heat pumps can markedly reduce electricity used for space heating compared with resistance systems; the exact comparison requires climate and equipment performance. A household with poor insulation can still waste considerable heat no matter how efficient its appliance is.

The meaningful question is therefore not “Is resistance heat inefficient?” without specifying a boundary. It is: how much electrical energy is required to deliver the desired heat to the desired location over the relevant period?

## Induction cooking heats the vessel differently

On a conventional electric radiant cooktop, electrical elements heat a surface or radiant assembly, which transfers energy to the pan. An induction cooktop instead uses power electronics to drive an alternating current through a coil beneath its surface. The changing magnetic field couples energy into suitable cookware, producing currents and magnetic losses that heat the pan itself. The hot pan then heats the food.

That changes the location of primary heat generation. The cooktop can respond rapidly to power commands, and the glass may receive heat mainly from the hot cookware above it rather than from a resistive burner beneath it. The glass can nevertheless remain hot after the pan is removed; “induction” is not a promise of a cold cooking surface.

Cookware matters. Coupling depends on the vessel's material, shape and position. Ferromagnetic cookware is commonly used, but the detailed compatibility of a particular pan depends on the appliance and materials. A magnet test is a useful screening clue, not a complete proof of performance for every product. A manufacturer may specify a particular diameter, flatness and material arrangement.

Induction is often advertised as more efficient than conventional cooking methods because it reduces some intermediate heating losses. That can be true, but an efficiency percentage depends on what is measured: energy reaching the water, energy absorbed by the pan, time to boil, or whole cooking-cycle consumption. Those are not interchangeable metrics. The DOE discussion of induction explains the mechanism and reported efficiency advantages; equipment-specific performance requires a comparable test method.

## Heating is also a circuit-design question

A heater may have a nearly unity power factor and a relatively straightforward operating current, while an induction cooktop uses power electronics and has a different input profile. A heat pump includes motors, inverters and possibly resistance backup elements. An electric water heater may cycle elements over a long period. A cooking appliance may operate several heating zones and controls at once. The branch circuit, overcurrent protection, conductors, switching apparatus and load calculation must reflect the actual appliance and installation design.

A nameplate gives a starting point, but it is important to distinguish instantaneous maximum demand from energy accumulated over a day. A thermostat may mean a heater is on for only fifteen minutes of an hour. That does not permit us to assume its circuit must be able to support only one quarter of its instantaneous current. Simultaneous equipment operation and the governing rating and code rules must be evaluated separately.

Imagine comparing three proposals for a workshop: a resistance heater, a mini-split heat pump and an induction-heated process tool. A useful comparison records the desired thermal output, ambient conditions, operating schedule, control precision, input-current profile, installation environment, and maintenance demands. The cheapest installed appliance may not consume the least energy. The lowest running-energy option may not be the easiest to maintain. The best choice depends on the actual task.

The underlying lesson is the same for a kettle and a whole-building heating system. Start with the energy balance, locate where heat is generated or transferred, trace its path to the intended target, and understand the feedback and protective controls. Electrical current is only the first link in a longer chain from power to temperature.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Electrical input versus energy

For an ideal resistive load: `P = VI = I²R = V²/R`.

| Hypothetical equipment | Supply | Rated power | Ideal current |
|---|---:|---:|---:|
| Portable resistance heater | 120 V | 1500 W | 12.5 A |
| Room heater | 230 V | 2000 W | 8.70 A |
| Heating element | 240 V | 2400 W | 10.0 A |

Energy is `E = ∫P(t) dt`. If a 1.5 kW heater is on 40% of a four-hour interval, `E = 1.5 × 4 × 0.40 = 2.4 kWh`; instantaneous current while on remains the full rated current under these assumptions.

### Thermodynamics sanity check

Approximate sensible heating of water: `Q = m c ΔT`, with specific heat `c ≈ 4.18 kJ/(kg K)` near room temperature. Heating `1 kg` of water by `20 K` requires about `83.6 kJ = 0.0232 kWh`. With `2 kW` of perfectly transferred input power, the lower-bound ideal heating time is about `41.8 s`. Real systems include vessel heat capacity, heat loss, temperature variation and control behavior; no appliance test result is implied.

### Resistance heating versus heat pump

If a delivered heat requirement is `6 kWh_thermal`:

- An ideal on-site resistance heater of COP≈1 consumes approximately `6 kWh_electric`.
- A heat pump operating at an assumed *average* COP of 3 consumes approximately `2 kWh_electric`.

Both figures ignore distribution/standby losses and describe only the stated performance boundary. A real COP depends on temperature and operating mode.

### System comparison

| System | Where thermal energy appears | Principal controls and constraints |
|---|---|---|
| Resistance baseboard | Element, then air/surfaces | Thermostat, element temperature, location/clearance |
| Electric kettle | Immersed or bonded resistive element to water | Boil/temperature cutoff, heat transfer, scale |
| Radiant heated slab | Embedded element and thermal mass | Long response time, floor and material limits |
| Induction cooktop | Conductive/magnetic cookware | Coil electronics, vessel compatibility and pan temperature |
| Heat pump | Refrigerant cycle transfers heat | COP versus conditions, compressor/inverter and defrost/backup |

### Exercises (desk)

1. Compare energy drawn by a 1.5 kW heater at 30%, 60% and 100% duty over five hours. Explain which quantity changes and which does not.
2. Sketch a heat-flow diagram for an electric resistance panel and a heat pump. Mark system boundaries before using the word “efficiency.”
3. Given an induction cooktop and a radiant cooktop with the same nameplate maximum watts, list the additional observations needed for an actual cooking-energy comparison.
4. Given a floor-heating slab's thermal mass, explain why a thermostat's effect may lag significantly behind a power command.

### Limits and counterexamples

- “100% efficient” for resistance heat is a restricted site energy-conversion statement, not a whole-grid or heat-pump comparison.
- Heater duty cycle affects energy consumed, not the device's on-state peak current.
- Nameplate wattage does not by itself establish a building's maximum diversified demand or circuit rating.
- Induction cookware and electronics must be evaluated as a coupled system; a magnetic pan is not proof of rated performance.
- Normal thermostats and high-temperature limit controls have different functions.
- The material does not assert numeric branch-circuit, clearance or thermostat installation requirements for an unidentified product and jurisdiction.

## Claim-level source map

| Claim ID | Consequential statement | Specific source support | Boundaries |
|---|---|---|---|
| E037000-01 | Resistive electrical loads convert local electrical input to heat by Joule heating | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (§9.5 P=I²R); [electrical-doe-process-heat](https://www.energy.gov/cmei/ito/what-are-different-kinds-process-heating-systems) (DOE process heating examples) | Element temperature and losses affect actual operation |
| E037000-02 | Power, duty and elapsed time determine accumulated electrical energy | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (§9.5 power and energy) | Duty-cycle example assumes constant on-state input |
| E037000-03 | Resistance heat site conversion can approach 100%, while heat pumps move heat with COP>1 | [electrical-doe-resistance-heat](https://webarchive-beta.loc.gov/playback-services/general/20240224010919mp_/https%3A/www.energy.gov/energysaver/electric-resistance-heating) (DOE Energy Saver resistance/heat-pump distinction); [electrical-doe-heat-pumps](https://www.energy.gov/articles/pump-your-savings-heat-pumps) (heat transfer rather than resistance generation) | COP, grid boundary and end-use conditions explicitly differ; archival link used for legacy DOE page |
| E037000-04 | Induction cooking uses changing magnetic fields to heat cookware rather than directly heating a radiant element | [electrical-doe-induction](https://stage.energy.gov/articles/making-switch-induction-stoves-or-cooktops) (DOE, Vivien Bui, How it Works); [electrical-doe-process-heat](https://www.energy.gov/cmei/ito/what-are-different-kinds-process-heating-systems) (DOE industrial induction heating overview, independent agency division) | Same department and high-level mechanism, not independent lab verification of performance figures |
| E037000-05 | Reported cooking efficiency depends on the metric and tested appliance | [electrical-doe-induction](https://stage.energy.gov/articles/making-switch-induction-stoves-or-cooktops) (qualitative efficiency comparisons) | No particular percentage is used as universal; comparable test method not checked |
| E037000-06 | Heat-storage mass delays temperature response | [electrical-openstax-heat](https://openstax.org/books/university-physics-volume-2/pages/1-4-heat-transfer-specific-heat-and-calorimetry) (specific heat and Q=mc delta T); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (energy input) | Specific heat varies with temperature; no-loss thermal models do not predict real appliance response |
| E037000-07 | Appliances carry nameplate electrical ratings and supply requirements | [electrical-osha305](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.305) (§1910.305(j)(3)(iii), primary U.S. workplace marking rule) | Field wiring/rating selection belongs to actual adopted code and model instructions |
| E037000-08 | Control thermostat and abnormal high-temperature limit provide different functions | [electrical-doe-resistance-heat](https://webarchive-beta.loc.gov/playback-services/general/20240224010919mp_/https%3A/www.energy.gov/energysaver/electric-resistance-heating) (thermostat and heater type context) | Model-specific independent source for protective high-limit behavior still required; do not claim design certification |
