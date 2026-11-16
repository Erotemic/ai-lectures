# 014000 — Diagnosing Heat Loss with Utility Data and Weather Normalization

<!-- BEGIN SPOKEN LECTURE -->

Suppose the heating bill rises by thirty percent. Is the house leaking more heat? Perhaps. Or the winter may have been colder, the thermostat higher, somebody may be home all day, or a furnace may have become less efficient. A bill is a measurement of purchased energy, not a direct measurement of the envelope. To learn from it, we need a model that separates weather, activity, and equipment from the building itself.

## Begin with an energy balance

On a cold day, heat leaves the conditioned space by conduction through walls, windows, floors, and roof; by exchange of indoor and outdoor air; and sometimes through uncontrolled paths into unconditioned rooms. Solar radiation, appliances, occupants, and heating equipment supply heat. When indoor temperature stays approximately constant, those gains balance the losses. A simple engineering model writes heat-loss rate as an overall heat-loss coefficient multiplied by the indoor-to-outdoor temperature difference. That coefficient, often called H or U A for a collection of assemblies, has units of power per degree of temperature difference.

This is not the same as an appliance's energy consumption. A gas furnace burns fuel to replace a portion of the lost heat, but the useful fraction depends on the furnace and distribution system. An electric resistance heater converts electrical energy to heat near where it operates. A heat pump delivers heat by moving it from outside, so electrical consumption depends on its coefficient of performance and operating conditions. Two houses with equal physical heat losses can have quite different bills.

Even the word heat loss needs care. If a heat pump supplies four kilowatt-hours of thermal energy using one kilowatt-hour of electricity, a one kilowatt-hour change in the meter does not necessarily mean the house gained or lost only one kilowatt-hour of thermal energy. A useful comparison must keep the equipment and operating mode in view.

## Degree days: putting weather on a common scale

A heating degree day measures how far, and for how long, outdoor conditions fall below a selected reference or balance-point temperature. A common published reference is sixty-five degrees Fahrenheit. If the day's average temperature is fifty-five degrees, that day contributes ten heating degree days on that basis. A twenty-degree difference sustained for two days contributes forty. Accumulating these numbers gives a compact measure of heating-weather severity for a billing period.

The sixty-five-degree convention is useful for comparison but is not the exact temperature at which every building starts heating. Internal and solar gains let some buildings coast without heat at outdoor temperatures below sixty-five degrees. A different house, or a house with unusually high ventilation, may have another balance point. Weather normalization removes one major source of variation; it does not remove every source.

Take a deliberately simple gas-heated house. Its summer bill, when space heating is off, averages twenty therms a month for water heating and cooking. In an illustrative winter billing period with eight hundred heating degree days, the meter shows one hundred therms. Subtracting the estimated twenty-therm non-heating baseline leaves eighty therms associated with heating. That is one tenth of a therm per heating degree day. If another winter has nine hundred and sixty heating degree days, the same slope predicts ninety-six heating therms, plus the baseline, or about one hundred sixteen total. A higher bill in that colder month is not evidence of a degraded enclosure by itself.

Notice how fragile the example becomes if the baseline changes. More showers, visitors, a gas fireplace, or an inaccurate billing-period alignment can spoil the estimate. We need several observations to distinguish a trend from noise.

## Fit a pattern, not a single ratio

Collect at least a season of bills, preferably several seasons if conditions were comparable. Record actual billing start and end dates rather than assigning the whole bill to a calendar month. Convert meter readings into consistent energy units. Pair each interval with heating degree days from an appropriate weather station. Plot energy use against degree days.

If the building behaves consistently, points for the heating season may form an approximately straight rising band. The intercept represents weather-independent consumption in a simple model; the slope estimates the additional purchased energy for each degree day. A sudden change in slope can signal altered equipment performance, occupancy, thermostat behavior, envelope leakage, or how heat is being distributed. A jump in intercept can suggest a base load that changed even without colder weather.

A fitted line is a diagnostic summary, not proof of a particular cause. Examine outlying points. Was a door left open during renovation? Did a vacation reduce occupancy? Was auxiliary resistance heat used during a cold spell? Were the meters estimated instead of read? Was the heat pump operated at a different setpoint? Corrections should be documented rather than silently discarded to make the graph look tidy.

## A useful boundary for inference

Electric bills often combine heating with lighting, cooking, computing, drying clothes, and cooling. When a home uses both a heat pump and resistance backup, a linear fit can hide two different operating regimes. Solar gains, wind, and humidity also matter. A more capable model may include cooling degree days, measured indoor temperature, equipment run time, or a separate cold-weather regime. But adding parameters to a small dataset can create a very persuasive fit with little predictive value.

A whole-house utility model cannot reveal whether the attic, a window, or an unsealed rim joist causes the heat loss. That is the job of additional observations and, where justified, measurements. An infrared camera shows apparent surface temperature patterns under certain conditions. A blower door measures air leakage at a prescribed pressure. Room-temperature logging, equipment service records, and duct inspections help determine whether heat is being delivered where it is needed.

## Assess the repair without rewarding a warmer winter

Imagine weather-sealing and attic work completed in October. Comparing November's bill directly with last November's confounds the retrofit with outdoor weather and changing household behavior. Instead, calculate what the pre-retrofit model predicts for this season's weather, then compare that prediction with actual consumption. Report the uncertainty, the changes in thermostat schedule and occupancy, and any changes to the heating equipment.

For a more credible comparison, keep fuel conversions consistent, examine several billing periods, and ask whether the predicted reduction is larger than ordinary month-to-month variation. If the improvement is small compared with noise, the honest conclusion is that the available bills cannot establish it. If the change is large and persistent, investigate whether an unrelated equipment or usage change could explain it before assigning all the savings to insulation.

The real power of weather normalization is not that it turns bills into a precise building audit. It teaches us to ask a better question: how much energy did the home require under comparable conditions? That question can guide an investigation and help evaluate a repair while leaving room for the uncertainty that real households introduce.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Model and worked calculation

- Simple billing model: `E_interval ≈ E_base + b × HDD_interval`, where `E_base` must reflect the **interval duration**; for bills of varying length, consider daily base use multiplied by days.
- On a 65°F basis: a day with mean outdoor temperature 55°F contributes `max(0, 65 − 55) = 10 HDD65`.
- Illustrative baseline: 20 therm / 30-day bill, 100 therm observed, 800 HDD65 gives `b = (100 − 20)/800 = 0.10 therm/HDD`. Under 960 HDD and the same 30-day baseline, model prediction is 116 therm. This is an *illustration*, not a home efficiency rating.
- Compare with `E_heat = H × ∫(Tin − Tout)_+ dt / effective equipment efficiency` only when the energy-input/thermal-output conventions are explicit.

### Audit worksheet

| Recorded field | Why it matters |
|---|---|
| Meter read dates and whether actual/estimated | Avoid false calendar alignment |
| Fuel and unit conversions | Separate therm, kWh, delivered fuel, useful heat |
| Daily temperature / HDD source | Weather adjustment, uncertainty of station relevance |
| Thermostat, occupancy, hot-water and appliance changes | Confounding loads |
| Heating equipment mode and maintenance | Fuel-to-heat conversion not fixed across conditions |
| Notes on retrofits and dates | Establish pre/post comparison boundary |

**Review boundary:** Energy bills alone do not certify insulation, air leakage, HVAC efficiency, or predicted savings. A fixed 65°F base can be inappropriate for a particular building; weather-normalized regression, balance-point selection, and causal claims need independent review where consequential.

## Selected reading and evidence records (non-spoken)

- `epa-energy-star-degree-days` — [U.S. Environmental Protection Agency ENERGY STAR Portfolio Manager, Degree Days Calculator](https://portfoliomanager.energystar.gov/pm/degreeDaysCalculator). 65°F reference heating/cooling degree days and weather-normalized energy use.
- `ashrae-2025-energy-estimating` — [ASHRAE Handbook 2025 Fundamentals, Chapter 19: Energy Estimating and Modeling Methods](https://handbook.ashrae.org/Handbooks/F25/IP/F25_Ch19/F25_Ch19_ip.aspx). Degree-day and change-point regression models, base use and weather-dependent slope.
- `doe-energy-star-window-basics` — [US Department of Energy, Building Science Education: ENERGY STAR for Windows](https://bsesc.energy.gov/energy-basics/energy-star-windows). Whole-window U-factor and SHGC and their separate heat-flow functions.
