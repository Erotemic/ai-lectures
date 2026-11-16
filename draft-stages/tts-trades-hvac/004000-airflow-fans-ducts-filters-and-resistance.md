# 004000 — Airflow: Fans, Ducts, Filters, and Resistance

**Track:** HVAC and Refrigeration. **Background:** Refrigeration cycles and heating/cooling loads. **Purpose:** explain distribution airflow as an operating point between a fan and an air-path resistance network.

<!-- BEGIN SPOKEN LECTURE -->

# The Fan Runs, but the Room Still Won't Cool

An air conditioner can be producing cold air and still fail to make a room comfortable. Imagine the equipment is running normally, but a distant bedroom receives very little airflow. The first instinct may be to buy a larger cooling unit. But the room's problem could lie in the ducts, filter, return path, or fan operating point. Delivering heat or cooling is not simply a matter of producing it at the central machine. The conditioned air has to reach the load and return.

Begin with a fan. It imparts energy to air, creating a pressure rise and flow. It does not force a fixed amount of air through any possible duct arrangement. Its achievable flow changes with the resistance of the system attached to it. A wide, smooth, short duct offers less resistance than a long narrow duct with many abrupt turns. A dirty filter, a constricted return grille, or a crushed flexible duct can add more resistance. The resulting operating point is where the fan's performance curve and the system's pressure-loss behavior meet.

## Pressure is the price paid for flow

Consider a straight duct. Air rubbing against the walls and air moving turbulently through bends loses mechanical energy. A filter makes air pass through porous media, which adds a pressure drop. An evaporator or heating coil also resists flow. Registers and grilles contribute. These losses do not just disappear because the thermostat requests more cooling.

For many turbulent-flow conditions in a fixed air-path geometry, pressure loss rises approximately with the square of airflow. That is a useful intuition, not a universal law for every filter or fan. Doubling flow can demand roughly four times the pressure drop under such a model. At the same time, a fan has its own limits and efficiency changes as it operates away from its design point. A system may become noisy, inefficient, or unable to deliver the requested flow before a casual observer recognizes the problem.

What does this mean for the person holding a thermometer? A cold supply register temperature does not tell you the total rate of cooling delivered to the room. Heat transfer depends on airflow and the temperature difference between supply and return air, with humidity changing the calculation further. A tiny trickle of very cold air can transfer less sensible cooling than a larger stream at a smaller temperature difference.

## Return air has to travel too

Many duct diagrams show supply branches with arrows toward rooms and forget about return paths. But supply air entering a closed bedroom must leave somewhere. If there is no adequate return duct, transfer grille, or designed under-door path, the room's pressure relative to adjacent spaces may rise. The resulting pressure difference can reduce delivery airflow and push conditioned air through leakage paths. The rest of the house may go negative or develop different pressure relationships. Closing one interior door can therefore change how the air system performs.

A leaking supply duct in an unconditioned attic sends some of the system's air where it is not useful. A leaking return duct in a crawlspace may pull hot, cold, damp, or contaminated air toward the air handler. Those are not symmetric problems, though both waste energy and alter pressure balance. Duct sealing and insulation help when chosen for the right boundaries and locations, but changing one path affects the network of flows elsewhere.

## More filter is not automatically more filtration

Air filters have two distinct attributes: how effectively they capture particles under specified conditions, and how much they resist airflow at a given rate. A higher-efficiency filter may add more pressure drop, depending on its size, media, loading, and construction. A larger filter face area can allow a suitable filter to operate with lower face velocity and pressure drop. A small filter crammed into a restrictive rack may perform poorly in the system even if its nominal particle rating is impressive.

As particles accumulate, many filters become more resistive. The fan response depends on whether it is single-speed, multi-speed, or controlled to try to maintain airflow. Some systems reduce flow; others increase fan effort and energy use. A fan struggling to compensate for excessive resistance can make duct noise louder. The right way to understand the interaction is to measure, not assume.

## How an airflow diagnosis becomes organized

Suppose the bedroom is warm. First ask whether the room load is larger than expected: sun, insulation, window area, and internal heat gains matter. Then ask whether the supply flow is low, whether the supply temperature differs significantly from nearby rooms, and whether the return path is available. A technician may measure total external static pressure across the air handler, pressure drops across particular components, and actual airflow using suitable methods. The measured values must be interpreted with the specific fan data and equipment ratings.

A particularly valuable distinction is between a *balancing* problem and an *insufficient total flow* problem. A system might move the right total amount of air but distribute it poorly. Or it might move too little air overall because the duct and filter network is overly restrictive. Closing many registers to force more into one distant branch can increase system resistance and reduce total flow, sometimes worsening the underlying problem.

Air systems are invisible networks until someone measures them. Once you picture a fan meeting a network of resistances and pressure boundaries, the diagnosis becomes tractable: map the paths, locate the restrictions and leaks, and check delivered flow against actual room needs. The refrigerant cycle makes conditioned air possible. Duct design makes that conditioning useful.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Flow and heat transfer

For approximately steady dry-air sensible heat transfer, \(\dot Q_s \approx \rho c_p \dot V\,(T_{return}-T_{supply})\). This does not include latent heat, mixing, leakage or nonuniform flow. In common U.S. HVAC rule-of-thumb units \(\dot Q_s \approx 1.08 \times \mathrm{CFM}\times\Delta T_{\mathrm{F}}\) at an assumed reference air density; do not apply that coefficient without understanding conditions. For a fixed duct geometry dominated by turbulent losses, \(\Delta p \approx K\dot V^2\) is a useful local model. Real filters and fans require measured pressure–flow curves.

### Diagnostic record

| Measurement | Interpretation limit |
|---|---|
| Supply-register temperature | Cannot determine delivered capacity without airflow |
| Room temperature | Also reflects load and control location |
| Fan external static pressure | Compare to equipment limits and component drops |
| Filter/coil pressure drop | Depends on flow, loading, equipment condition |
| Room-to-hall pressure with door shut | Indicates return-path imbalance, not alone its cause |

### Engineering scope

Airflow targets, duct leakage criteria, combustion-air interactions, fire dampers, condensation control and air-handler limits are equipment- and code-specific. Field pressure measurements and duct alterations should be interpreted by qualified HVAC personnel. Source concepts include fan curves, design pressure budgets, and ANSI/ACCA manuals rather than one universal pressure threshold.

## Selected reading and claim sources (non-spoken)

- `ca-hvac-pressure` — [California Energy Commission, Residential Compliance Manual: Chapter 4 HVAC, Air Distribution](https://www.energy.ca.gov/filebrowser/download/5126). Fan pressure budget, filter pressure drop, coil, ducts and registers.
- `energystar-ducts` — [ENERGY STAR, Duct Sealing](https://www.energystar.gov/saveathome/heating-cooling/duct-sealing). Duct leakage as an energy and air delivery problem.
