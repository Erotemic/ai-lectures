# 013000 — Power Failures, UPS Design, and Recovery Testing

<!-- BEGIN SPOKEN LECTURE -->

A home has a battery-backed router. The electricity fails, the router stays lit, and yet nothing works. The fiber terminal in the basement has lost power. Or the network switch still runs but a powered camera has shut down. Or the server recovered before its storage drive was ready and never resumed service. This is why backup power should be designed around a service path rather than around the one device whose status light is easiest to see.

A networked service is a chain of dependencies. A phone accessing a local camera may need the camera, its power source, a PoE switch, the local network, an address, and sometimes a name-resolution service. Remote access may also require an optical terminal or cable modem, the provider's functioning outside network, a gateway, and a reachable authentication service. Backing up one link protects only the parts of the chain downstream from it.

## Draw the dependency graph

Begin with a question specific enough to test. “Keep local cameras recording during a short outage” defines a different system from “keep internet access available.” For local recording, perhaps cameras, switch, network video recorder, and local storage all need power. For remote access, the modem or optical network terminal and any necessary external communications equipment join the critical set. Some communication services still fail when the utility and provider infrastructure are down, even if every device inside the house is protected.

Draw a line between each service and everything it needs. Label components with steady operating power, expected startup behavior, and whether they are essential. Include devices that provide time, DNS, DHCP, or authentication if the service relies on them. Ask what happens if a component is unavailable but its network link remains active. A system can have electrical power and still fail at software dependencies.

## Understand UPS capacity

An uninterruptible power supply has at least two distinct ratings: how much instantaneous power it can deliver, and how much usable stored energy it has. A UPS labeled in volt-amperes describes an apparent-power capability, not a promise of that many watts or hours. Its watt rating and the actual load's electrical behavior must both be respected. Runtime depends on battery capacity, age, discharge rate, conversion efficiency, and temperature.

For a rough calculation, suppose the essential equipment draws eighty watts continuously and you want forty-five minutes of operation. Ignoring losses, eighty watts times three quarters of an hour equals sixty watt-hours. The battery must supply more than that because conversion and battery losses exist, and some margin is needed. This rough energy calculation is a screening tool, not a manufacturer runtime specification. High inrush currents and power factors can determine whether the UPS supports the load even when the steady watts appear modest.

PoE complicates the accounting. The switch consumes power for its own electronics and delivers additional power to devices through cables. A camera advertised as drawing six watts on average may consume more with heaters, infrared illumination, or motors activated. The sum of the switch's port ratings is not necessarily the shared PoE budget, and the UPS sees the switch's input draw, including losses. Measure or conservatively estimate the full operating modes rather than multiplying one average number by the camera count.

## Design a recovery sequence

An outage ends in stages. Power may flicker several times. The UPS may shift to battery, shut down at low charge, and return when electricity reappears. Some switches power on immediately, while a recording server may require storage checks. A service that depends on DNS or authentication can come up before those dependencies are ready. Startup order is therefore a functional requirement, even for a modest home network.

A controlled shutdown can protect storage from an abrupt power loss. A UPS with compatible signaling may tell a computer to stop writes and shut down when remaining runtime falls below a threshold. It is also important that the computer can restart afterward, whether through firmware power settings, a management controller, or deliberate human action. Automated restart must be designed so it does not repeatedly power-cycle defective equipment or defeat protections.

Power cycling is not identical to resilience. An internet modem may require network synchronization after restart. A local automation controller may reboot, lose time, or restore a relay to an unsafe state. Decide the desired recovery behavior of each critical actuator, and treat personnel safety as a separate engineered function rather than as a convenience script in a home automation platform.

## Test the actual outage, not just the battery

A UPS self-test says something about the battery and circuitry under that test. It does not demonstrate that a local camera recording can survive a long outage, nor that all services recover when electricity returns. After documenting the current setup, conduct a controlled and appropriate outage simulation with the responsible equipment and its required shutdown procedures. Record which devices stayed powered, when recording stopped, whether time stamps remained coherent, and which services required manual intervention. Do not remove power abruptly from equipment that cannot be safely interrupted.

Repeat the test after major configuration or wiring changes. Battery capacity declines with age; local temperature and the manufacturer's replacement guidance matter. Keep the UPS itself accessible for inspection, and do not overload extension wiring or block ventilation.

The most useful distinction is between power availability, service availability, and safe recovery. A light on a router proves only that the router has power. A resilient network proves that the service the user actually needs remains available—or returns predictably—across the outage conditions it was designed to tolerate.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Screening calculation

For an illustrative 80 W load over 0.75 h, `energy_at_load = 60 Wh`. Required battery energy is greater after efficiency losses, discharge constraints, aging reserve, and UPS electronics. Verify with the manufacturer's runtime curve for the **actual load and model**; VA capacity does not equal energy capacity.

### Dependency and test record

List essential service; modem/ONT; gateway/router; switches and PoE loads; cameras; recorder/storage; DNS/DHCP/time/authentication dependencies; steady and peak power; UPS watt and VA limits; shutdown signal method; restart behavior; controlled test results. Record outage duration and any lost footage or missing events.

**Editorial boundary:** Mains wiring, battery handling, connected-load limits, and life-safety controls follow approved products and qualified practice. An indoor UPS does not guarantee that the external service provider's network remains operational.

## Selected reading and evidence records (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `cisco-poe` — [Cisco, What Is Power over Ethernet?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-power-over-ethernet.html). PoE standards family and source/device power relationships.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.
