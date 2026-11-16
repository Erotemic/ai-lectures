# 004000 — PoE Budgets, Voltage Drop, and Cable Runs

**Track:** Networking, Controls, and Automation. **Background:** Ethernet cable pairs, switch/router roles, IP, DHCP, and DNS. **Purpose:** explain powered-device compatibility as a circuit and power-allocation problem, not just a connector match.

<!-- BEGIN SPOKEN LECTURE -->

# The Switch Has Eight Ports. Can It Power Eight Cameras?

A network switch has eight Ethernet ports, each marked PoE. Eight cameras are connected, and six come online. The seventh starts to boot and restarts. The eighth stays dark. Is the cable bad? Is the camera defective? Perhaps. But the problem might be a power budget hidden behind those eight identical-looking ports.

Power over Ethernet, or PoE, lets a network cable carry both data and electrical power. On a standards-compliant system, the device delivering power is called the *power sourcing equipment*, or P S E. It may be a switch or an inline injector. The device consuming that power is the *powered device*, or P D. They do not merely share an electrical plug: compatible equipment participates in detection and classification procedures before normal power is supplied. That distinguishes standards-based PoE from improvised passive arrangements that put fixed voltage on a cable without the same negotiation.

## Three power numbers, not one

Begin with a camera labeled, for example, twelve watts maximum. The switch port may support a certain PoE type or class. The switch chassis may also have a smaller total budget than the sum of all its port ratings. And the power that leaves the switch is not all guaranteed to arrive at the far end of the cable: some is lost as heat in the conductors and connections.

Suppose a hypothetical four-port switch allows up to thirty watts on each port but has a sixty-five-watt shared budget. Four devices each requiring twenty watts would need eighty watts before accounting for how the equipment manages reserved versus measured power. Each device is individually within the per-port limit, yet the group exceeds the total budget. Another device may need only a few watts in idle mode but draw more when infrared lighting, a heater, a motor, or other features engage. Summing idle readings can therefore underestimate the maximum demand.

Standards terminology helps. IEEE 802.3af Type 1 provides up to 15.4 watts at the power source and specifies a lower minimum at the powered device. IEEE 802.3at Type 2, often called PoE plus, provides up to thirty watts at the source. IEEE 802.3bt types extend the system to higher powers using four pairs. The exact maximum power available at the device differs from the source rating. A label reading 'ninety-watt PoE' does not mean a distant device is guaranteed ninety watts of usable power.

## Why the cable has a power limit

Copper has resistance. Current flowing through it produces a voltage drop and heat. For a simple conductor the approximate resistance is resistivity times length divided by cross-sectional area. Longer cables and smaller copper cross sections generally have greater resistance, all else equal. The power dissipated in resistance is current squared times resistance. That square is important: a modest rise in current can increase cable heating disproportionately.

Power over Ethernet uses conductor pairs as part of a defined common-mode powering scheme, while the data signaling relies on differential behavior. Standards constrain how the circuit is implemented, including allowable electrical characteristics. Poor terminations, damaged conductors, and large differences in pair resistance can upset reliable power delivery even when a basic link test indicates that data sometimes passes. This is why a good installation distinguishes continuity testing from certification or appropriate verification of cabling performance.

Cable material matters. Solid-copper category-rated cable is not equivalent to every product advertised with an Ethernet-looking connector. Some low-cost products use copper-clad aluminum and should not be assumed suitable for a PoE design; their resistance and compliance characteristics differ. Installation environment matters too: heat, bundling, conduit, and cable construction affect thermal behavior. The normal structured-cabling channel length limit for common copper Ethernet applications is not permission to ignore loss, damaged pairs, or outdoor environmental requirements.

## Work through a camera example

Imagine three outdoor cameras. Their nameplates or data sheets show peak electrical demands of nine, twelve, and eighteen watts at the device, depending on features. A switch with a fifty-five-watt total sourcing budget might appear adequate because those numbers sum to thirty-nine watts. But you still have to ask whether every port supports the required PoE class, how the switch allocates reservations, what margins exist for cable loss, and whether switch power budget is measured at the source rather than at the cameras. A camera with motorized movement or nighttime heating may have a different peak demand from the value observed in daylight.

Next consider the run itself. One camera is attached through a short, professionally terminated indoor cable and remains reliable. Another is a long outdoor run near its application limits, with moisture-exposed connectors and questionable splices. If that camera reboots only when its heater activates, both power demand and cable resistance deserve investigation. If its network link stays active but DNS fails, that points to a different layer of the system. Good troubleshooting keeps electrical supply, physical link, addressing, and application service distinct.

## Design for margin and diagnosis

Start with a drawing that lists every port, the attached device, the required PoE standard and class, the device's maximum demand, the cable route, and the switch's total power budget. Add realistic allowance for loss and configuration behavior. Label which ports may be shed under budget pressure. Where uptime matters, plan the power supply and backup power of the switch itself, not just the cameras.

Eight PoE sockets are eight connection opportunities, not a guarantee of eight simultaneous maximum-power loads. A reliable network engineer treats PoE as a small electrical distribution system with source limits, conductor losses, and loads that change with operating conditions. That is the difference between a camera that happens to power on and one you can rely on when its most demanding feature activates.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Reference maxima for IEEE standards

| PoE type | Nominal maximum at PSE | Maximum budgeted at PD (standardized example) |
|---|---:|---:|
| IEEE 802.3af Type 1 | 15.4 W | 12.95 W |
| IEEE 802.3at Type 2 | 30 W | 25.5 W |
| IEEE 802.3bt Type 3 | 60 W | 51 W |
| IEEE 802.3bt Type 4 | 90 W | 71 W |

These are standardized endpoint power ceilings; actual class allocation, switch capabilities, pairsets, cable conditions and device demand determine feasibility. The 4-pair types and class negotiation are not equivalent to supplying the table's maximum to every connected device.

### Circuit intuition

For an assumed DC path, \(V_{drop}=IR\) and \(P_{loss}=I^2R\). This is a circuit-level approximation: real standards-based PoE distributes current over pairsets and controls signatures, classification and operating voltage. Do not treat a one-wire model as wiring instructions.

### Commissioning checklist

Match PD class and power requirement to each PSE port. Sum required allocations against the switch's shared budget, not just port count. Verify solid-copper, correctly rated cable and installation limits; test link and power under the device's actual high-demand mode. For outdoor runs, address protection, isolation and exposure using applicable equipment and installation standards. Avoid passive power injectors without verifying device-specific electrical compatibility.

## Selected reading and claim sources (non-spoken)

- `fluke-4pair-poe` — [Fluke Networks, 4-Pair PoE Standards and Cabling Guide](https://www.flukenetworks.com/expertise/learn-about/four-pair-power-over-ethernet-poe-and-your-cabling-plant). PSE, PD, class power limits, cabling current, four-pair PoE.
- `cisco-poe-brief` — [Cisco, PoE for Industrial Automation: Power, Data and Control over a Single Cable](https://www.cisco.com/c/en/us/products/collateral/networking/industrial-switches/poe-ind-data-control-single-cable-so.html). IEEE 802.3af/at/bt source and receiver limits and power over pairs.
- `cisco-poe` — [Cisco, What Is Power over Ethernet?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-power-over-ethernet.html). PoE standards family and source/device power relationships.
