# 038000 - The Loads That Change a Building's Electrical Life

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** equipment nameplates, time-dependent load diagrams, energy and demand calculations, and comparisons of motor, resistance, heat-pump, and EV-charging loads.

<!-- BEGIN SPOKEN LECTURE -->

# The Loads That Change a Building's Electrical Life

Imagine a house that has served its occupants without much attention to the electrical system. Then several things change. An old furnace gives way to a heat pump. An electric water heater is replaced with a hybrid heat-pump model. A well pump is replaced, and someone buys an electric car. Each appliance has a rating, but the ratings alone do not tell us what the house will demand of its electrical supply. Some loads change quickly, some last for hours, and some have operating modes with dramatically different currents.

An electrical designer must understand the *shape* of the load: when it begins, how much it draws while operating, what happens at startup, whether other equipment operates with it, and whether a controller changes those relationships. A single number in watts is a useful entry point. It is not a complete electrical portrait.

## A building's load is a function of time

For a resistive load at a fairly stable voltage, instantaneous power is approximately voltage times current. For a general alternating-current load, the real power also depends on waveform and power factor. Energy is the integral of power over time. The electrical system, however, must also withstand particular currents at particular moments.

Consider two hypothetical devices. One consumes two kilowatt-hours by drawing two kilowatts for an hour. The other consumes the same two kilowatt-hours by drawing half a kilowatt for four hours. Their energy is the same, but their demands while operating are not. Now add a motor that briefly draws much more current during acceleration. Its startup may matter for voltage dip and protective-device behavior even though those few seconds contribute little to an electricity bill.

We can describe each load with several attributes. First is *rated* or *nameplate* current, which must be interpreted according to the kind of rating provided. Second is operating current across normal modes. Third is starting or transient behavior. Fourth is duration and duty cycle. Fifth is control: a thermostat, pressure switch, timer, inverter or vehicle charger may make the load appear only under certain conditions. Sixth is interaction with other loads. These are different questions, not six synonyms for watts.

## HVAC is several electrical machines, not one box

A conventional split air-conditioning system has a compressor and at least one fan. An air handler may contain a separate blower motor. A heat pump adds the ability to reverse heat flow, and it may have a defrost sequence or supplementary electric resistance heat. Electrically, those components do not always run together and their combined profile is not necessarily constant.

The compressor moves refrigerant and is driven by an electric motor. A traditional fixed-speed compressor may have a distinct starting transient; an inverter-controlled compressor can vary motor frequency and operating speed. The difference changes both instantaneous current and how the machine follows the building's changing thermal demand. A nameplate describing one rated operating point should not be mistaken for a continuous trace of power during the season.

A heating load is partly set by the building envelope. Heat loss increases when indoor and outdoor temperatures diverge, and air infiltration can add a substantial load. A thermostat calls for heating because the building is losing heat, not because an electric heater is intrinsically efficient or inefficient. A heat pump often delivers several units of heat per unit of electrical input in favorable conditions, but its coefficient of performance varies with temperatures, defrost operation and equipment design.

Here is a particularly important architectural detail: some heat-pump systems include supplementary resistance elements. A house might have an outdoor compressor drawing a few kilowatts and, in some circumstances, a bank of resistance heaters that draws several more. Whether those elements operate independently, in stages, or simultaneously with the compressor is a matter of control logic and equipment configuration. It is possible for a heat-pump conversion to lower annual electrical energy used for heating while still creating a demanding electrical peak under some conditions. Annual savings and maximum simultaneous current can both be true.

The U.S. Department of Energy's building-science education material explains auxiliary heating and defrost as operating modes, not as a single invariant schedule. The real questions are which modes this equipment actually supports, what its electrical ratings specify, and how often its controls choose those modes under the local climate.

## Pumps convert electrical input into pressure and flow

A well pump, hydronic circulator, sump pump and pool pump all move fluid, but their load profiles differ. A sump pump may sit idle for days and then start repeatedly during a storm. A hydronic circulator may run for long periods, sometimes at variable speed. A well pump starts in response to a pressure tank and switch, and the length of each cycle depends on water demand, tank behavior and the pumping system.

For a centrifugal pump, the operating point comes from the intersection of a pump curve and a system curve. The curve relates flow, pressure head and speed; the system curve describes resistance from piping, fittings, elevation and other effects. Changing speed can greatly reduce power when friction losses dominate. The familiar pump affinity-law approximation predicts flow proportional to speed, head roughly proportional to speed squared, and absorbed power approximately proportional to speed cubed for comparable operating conditions. That is not a universal promise of savings: static elevation, efficiency shifts and control objectives change the result.

Electrically, a variable-speed drive may also change startup current compared with a direct-on-line motor. A motor nameplate and a pump's horsepower do not determine every starting current or operating interval. And a motor's mechanical output rating is not its electric input: efficiency and power factor separate those quantities.

A useful thought experiment is a sump pump that usually runs for twenty seconds every few hours. Its annual electricity consumption may be modest. Its ability to start during an adverse supply condition may nevertheless be operationally important. This is why reliability planning and energy accounting sometimes rank the same load very differently.

## Water heating is a thermal store attached to a power system

A tank water heater stores hot water so that heating power and hot-water demand do not have to match from instant to instant. Its electrical input depends on the elements or compressor that replenish the stored heat, not directly on the flow through the tap at every moment. A conventional electric resistance tank may energize one or more elements according to its wiring and control sequence. Some designs have multiple elements that are deliberately not simultaneously energized; other products have different arrangements. Reading the equipment's actual electrical specifications is therefore more informative than assuming two visible elements must double the simultaneous demand.

A heat-pump water heater extracts heat from surrounding air and moves it into water. The Department of Energy explains that hybrid models may add electric resistance heat for higher recovery demand or particular operating conditions. These modes can have quite different input powers, recovery times and effects on the room containing the unit. A high efficiency rating describes an energy relationship over defined test conditions. It is not a guarantee about the highest instantaneous current.

A tankless electric heater reverses the storage strategy. Without a large hot-water reserve, it must deliver much of the requested heating rate while water is flowing. Imagine raising water temperature by twenty-five degrees Celsius at a flow of six liters per minute. Six liters per minute is about one-tenth of a kilogram per second. Using a specific heat near 4.19 kilojoules per kilogram-degree, the ideal water-heating rate is about ten and a half kilowatts. That is a large electric load even though it operates only during a draw. The calculation ignores heat loss and temperature-dependent details, but it shows why a device that never runs overnight can still dominate a short electrical peak.

## EV charging makes duration part of the design

Electric-vehicle supply equipment, usually called EVSE, negotiates and controls the supply available to a vehicle. For ordinary home AC charging, power conversion into the traction battery is generally performed by the vehicle's onboard charger. The wall-mounted EVSE is not simply an appliance that delivers a fixed advertised wattage regardless of the vehicle. Its available current, configured limit, vehicle capability, battery state, temperature and charge schedule all matter.

The U.S. Department of Energy's Alternative Fuels Data Center distinguishes Level 1 AC charging, commonly using 120 volts in North America, from Level 2 AC charging, commonly 208 or 240 volts. Different vehicles and installations support different rates. Consider a hypothetical AC EV load limited to twenty-four amperes at 240 volts. Its apparent input is 5.76 kilovolt-amperes. If its input power factor is near unity, real input is close to 5.76 kilowatts. Operated for four hours at that input, it draws roughly twenty-three kilowatt-hours from the supply. Battery energy gained would be less because charging and auxiliary systems have losses.

Unlike a kettle, the charger may maintain substantial current for several consecutive hours. It is therefore important to know not only the current rating but also the applicable rules for loads expected to run for extended periods. The branch-circuit design and the service-level load study are related, but separate. One cannot infer the required circuit rating simply from the nominal vehicle battery size or from the car's maximum advertised charging speed.

Charge scheduling and managed charging change the profile. If the car can replenish its daily energy during a long overnight window, lowering the instantaneous charging limit may be acceptable. Some listed control systems can adjust EV current based on other measured loads. The effectiveness of such a system depends on its approved operating conditions and failure behavior, not merely on having a phone app labeled 'smart'.

## Time alignment is the invisible connection

Take our imagined house and draw one horizontal axis: time of day. Mark when the compressor runs; when supplementary heat might come on; when the water heater recovers after morning showers; when the well pump starts; and when the car begins charging. The instantaneous building demand is the sum of the simultaneous contributions, including phase allocation and power-factor effects where relevant.

There are multiple plausible peaks. A cold morning might align space heating and water recovery. A summer afternoon might align cooling, cooking and pumping. A car charging at midnight might create a long plateau in demand, even though lighting and cooking have stopped. An appliance's own nameplate does not tell us which of these patterns will occur.

The decisive habit is to separate three ledgers: **energy** consumed over time, **sustained demand** during overlapping operation, and **short transients** during starts or switching. They matter to different parts of design. An efficient appliance can still require substantial circuit capacity. A rare motor start can matter more for supply voltage than for monthly energy. And a carefully managed long-duration load can be easier to accommodate than its unconstrained maximum would suggest.

Understanding a building begins by understanding what its equipment actually does, rather than assuming the total of nameplate watts is either its electrical bill or its unavoidable service peak. The next analytical step is to turn this equipment knowledge into a defensible load inventory.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Three different load measures

Define active input `P(t)`, RMS voltage `V(t)`, RMS current `I(t)`, and power factor `PF(t)` for a sinusoidal single-phase approximation: `P(t) = V(t) I(t) PF(t)`. For nonsinusoidal waveforms, compute average real power from instantaneous `v(t)i(t)`. For the energy interval `[0,T]`, `E = integral P(t) dt`. Peak measured real power averaged over a demand window `Delta` is `max_tau (1/Delta) integral_tau^(tau+Delta) P(t) dt`, not the same quantity as instantaneous motor-start current.

### Worked calculations

1. **Water heating rate:** `m_dot = 6 L/min * (1 kg/L) / 60 = 0.1 kg/s`; `Delta T=25 K`; `c_p = 4.19 kJ/(kg K)`; `Q_dot = m_dot c_p Delta T = 10.475 kW` of useful water heating. Electric input differs with efficiency and other losses.
2. **AC EV charging:** `V = 240 V`, `I = 24 A`; `S = 5.76 kVA`. At `PF=0.99`, `P=5.7024 kW` and four-hour input energy `22.8096 kWh` if conditions remain constant. `5.76 kW` is the common unity-PF approximation, not a guaranteed output to the battery.
3. **Pump speed thought experiment:** under affinity-law conditions, `N2/N1=0.8`, predicted `Q2/Q1=0.8`, `H2/H1=0.64`, and `P2/P1=0.512`. Significant static head or changed efficiency invalidates a naive universal power prediction.
4. **Same energy, different peaks:** `2 kW x 1 h = 0.5 kW x 4 h = 2 kWh`. The active demands while operating are not equal.

### Desk exercise: compare hypothetical equipment

| Equipment | Rated supply and input | Operating modes | Peak/duration question |
|---|---|---|---|
| Inverter heat pump | Nameplate voltage and minimum/maximum current | Cooling, heating, defrost, auxiliary heat | Which elements can overlap? |
| Well pump | Motor output and actual input/current | Start, run, idle | Does starting create a transient constraint? |
| Hybrid water heater | Compressor and element ratings | Efficient, hybrid, high-demand | Which modes determine highest input? |
| EVSE | Configured current, supply voltage | Scheduled charge, active charge, load-managed | How long can current be sustained? |

Draw a 24-hour hypothetical profile and identify separately (a) energy, (b) highest 15-minute average input, (c) motor startup transient. Do not conflate those with a code load calculation.

### Limits and counterexamples

- The pump affinity laws require comparable operating conditions; static lift and changing efficiency matter.
- A heat pump can reduce annual energy but still have high combined auxiliary-heating demand under some conditions.
- Two water-heater elements do not necessarily run simultaneously; the equipment diagram determines switching.
- EVSE may advertise a maximum the vehicle will not accept; AC input is not battery energy delivered.
- Electrical capacity, protective-device ratings and continuous-load definitions require actual listed equipment data and adopted rules, not this hypothetical profile.

## Claim-level source map

| Claim ID | Consequential statement | Source and location | Boundaries |
|---|---|---|---|
| E038000-01 | Energy and peak electrical demand are distinct temporal quantities | [electrical-openstax-acpower](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (AC real power); [electrical-eia-home-electricity](https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php) (annual residential electricity categories) | EIA annual end uses do not establish a particular dwelling's peak demand |
| E038000-02 | Heat pump electric input varies by heating, defrost and supplementary-heating mode | [electrical-doe-heatpump-defrost](https://bsesc.energy.gov/sites/default/files/2024-09/CEE_You_Installed_an_ASHP_Now_What_TRC_01.16.24_1.pdf) (defrost and auxiliary-heating FAQ); [electrical-doe-heat-pumps](https://www.energy.gov/articles/pump-your-savings-heat-pumps) (heat transfer and varying performance) | Actual concurrent heater/compressor operation requires model-specific diagrams |
| E038000-03 | Centrifugal pump speed changes can strongly change flow, head and power | [electrical-doe-variable-speed-pumping](https://www.energy.gov/sites/prod/files/2014/05/f16/variable_speed_pumping.pdf) (Effects of Speed Variation, affinity laws) | Static head and different efficiency curves can invalidate simple cubic scaling |
| E038000-04 | Motor startup and normal running electrical behavior differ | [electrical-se-motor-starters](https://www.electrical-installation.org/enwiki/Motor_starter_configurations) (direct and controlled starting); [electrical-doe-motor-guide](https://www.energy.gov/sites/default/files/2014/04/f15/mc-0382.pdf) (rated motor quantities) | No generic current multiple applies to every motor |
| E038000-05 | Hybrid heat-pump water heaters can use resistance backup and have different operating modes | [electrical-doe-hpwh-building-science](https://bsesc.energy.gov/energy-basics/hvac-heat-pump-water-heaters) (what/how, hybrid backup); [electrical-doe-hpwh-femp](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-water-heaters) (operating modes) | Mode details and input ratings are equipment-specific; two DOE pages are not independent institutional corroboration |
| E038000-06 | Heat needed to warm flowing water follows mass flow times specific heat times temperature rise | [electrical-openstax-heat](https://openstax.org/books/university-physics-volume-2/pages/1-4-heat-transfer-specific-heat-and-calorimetry) (Q=mc Delta T) | The 10.475 kW example is idealized heat delivered to water, not a certified product load |
| E038000-07 | AC home EVSE supplies a controlled AC connection; charging power varies by vehicle and supply | [electrical-afdc-charging](https://afdc.energy.gov/fuels/electricity-stations) (AC levels, onboard charging limits); [electrical-afdc-home](https://afdc.energy.gov/fuels/electricity-charging-home) (home charging modes) | Details evolve; check vehicle/EVSE ratings and current product standards |
| E038000-08 | Managed timing can redistribute EV demand across hours | [electrical-afdc-home](https://afdc.energy.gov/fuels/electricity-charging-home) (home charging and charging settings); [electrical-eia-recs](https://www.eia.gov/consumption/residential/) (regional/monthly variations) | These sources do not validate any particular energy-management control algorithm |
| E038000-09 | Circuit loading and service-level coincidence are separate design questions | [electrical-nfpa-2026-loads](https://www.nfpa.org/news-blogs-and-articles/nfpa-journal/2025/04/29/2026-nec-changes) (branch, feeder, service load distinctions); [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (workplace equipment characteristics and protection) | Neither establishes the code calculation for an unspecified jurisdiction |

