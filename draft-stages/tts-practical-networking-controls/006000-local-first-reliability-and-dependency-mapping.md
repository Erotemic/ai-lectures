# 006000 — Local-First Reliability and Dependency Mapping

**Track:** Networking, Controls, and Automation. **Background:** IP addressing, PoE, sensors, actuators, and hysteresis. **Purpose:** design systems that behave predictably when pieces of the network fail.

<!-- BEGIN SPOKEN LECTURE -->

# A door that needs the internet to open

Imagine a motorized door controlled by a phone app. The motor is powered. The local network is running. Yet the door refuses to open because an account service somewhere else is unavailable. From the user’s point of view, the door is broken. From the manufacturer’s point of view, perhaps the door, app, and remote service are three components working according to a complicated system design. This difference reveals why control reliability cannot be judged by testing each device independently.

A reliable automation system has a chain of dependencies. A sensor detects a condition. A controller receives it, decides what to do, and sends a command. A relay or motor driver actuates the physical system. The result may be reported to a display, logged, or sent to a phone. Each step can depend on power, software, networking, naming, time, authentication, and remote services. If any essential link is unavailable, the intended function may disappear.

The engineering response begins with a dependency map, not with shopping for a stronger router.

## Distinguish three paths

Consider a smart light. The **control path** runs from a switch or sensor to the device that actually changes power to the lamp. The **observation path** reports whether the light is on and may record events. The **management path** allows setup, updates, and remote access. Some products combine all three paths in one cloud account. Other systems permit local actuation even when remote access is lost.

For an ordinary room light, useful design might allow the physical wall switch to work without Wi-Fi. For a motion-controlled lamp, the sensor and controller might communicate over a local link while cloud access remains optional. For a safety-critical actuator, still stronger requirements apply: certified hardware, safe default behavior, manual release, and an independent path for essential protective functions. Local-first automation improves some classes of availability but is not a substitute for safety engineering.

An essential question is what continues when the internet is disconnected. A second is what continues when the router reboots. A third is what continues when the controller or its power supply fails. These are different outages. They should be tested separately rather than summarized as 'offline'.

## A network has hidden dependencies

Two Ethernet devices connected to a switch may exchange data directly if they have suitable addresses and the application supports local operation. They do not necessarily require a public internet connection. But an application might use cloud-hosted authentication or a remote message broker even when both devices are physically close. It might resolve a device name through DNS, acquire an address using DHCP, or refuse operation when an access token expires. The cable does not tell you what the software depends on.

DHCP illustrates a subtle distinction. A device that already has a leased address may continue using it during a short server outage, depending on its implementation and lease state. That does not mean new devices can join or that the arrangement is immune to later lease expiry. A local DNS service or time source can similarly affect functions that appear unrelated to networking: a camera may record video while remote viewing fails, or scheduled events may drift if time synchronization is unavailable.

PoE combines electricity and data in one cable, which can simplify an installation but also concentrate failure. A single switch outage can darken several cameras, disable networked sensors, and break a controller’s communication simultaneously. A battery-backed switch may survive a brief power interruption while its upstream router does not. A complete diagram therefore shows power sources and communications separately.

## Design for graceful degradation

Graceful degradation means losing a nonessential convenience without losing the core function. A thermostat that can follow a local schedule without internet access has a different failure profile from one that continuously asks a remote server what temperature to maintain. A camera that records locally when a cloud service is unreachable may preserve evidence but still lose remote notifications. These differences should be described explicitly in acceptance criteria.

Not every automation must be fully local. Remote coordination can be valuable, and managing secure remote access may be better done through a reputable service than through an improvised public port. The key is to choose dependencies deliberately. A networked weather display can tolerate being stale. A sump-pump control or door-access system must be assessed for consequences of stale data or unresponsive commands, and ordinary consumer automations should not carry essential life-safety responsibility without suitable protections.

A controller can also be locally unreliable. Software may crash, a message queue may overflow, and sensors may report stale data. A robust design defines what a stale measurement means and how actuators should respond. A temperature reading that has not changed in six hours might indicate a stable room—or a frozen sensor stream. A command acknowledgment from software is not the same as confirmation that a motor moved; independent sensing may be warranted.

## A practical failure-mapping exercise

Draw a small system: a door sensor, a controller, a PoE switch, a local network, a cloud notification service, and a phone. Mark which connections are needed to open the door, which are needed only to see its status, and which are needed to send an alert. Then remove one component at a time on paper. What functions remain? Does the system return to normal automatically when a connection is restored, or does someone need to reset or reauthenticate it?

Testing is more informative when failures are injected deliberately. Temporarily disconnect WAN access in a safe test environment. Reboot the router. Power-cycle a device. Simulate a stale sensor reading. Record exactly what happened and how long recovery took, rather than relying on a vendor’s phrase 'works offline'. Preserve a manual means of operation where the task warrants it.

There is also a security dimension. Local connectivity is not automatically secure: poorly managed devices can expose services to other devices on the network. Isolation, authenticated access, update support, and the ability to recover configurations matter. Reliability and security share a basic need: know the system’s boundaries and who can affect them.

The goal of local-first design is not to forbid remote services. It is to keep dependencies proportional to the job. A device should not lose a basic physical function merely because an unrelated convenience service is unavailable—unless that dependency is a conscious, documented design choice.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Dependency table to build

For each function, list the required: power supply, switch/router, address assignment, name resolution, controller, remote service, time source, actuator, sensing feedback, and manual override. Classify failure as **unavailable**, **stale-but-visible**, or **available with reduced capability**.

### Fault-injection exercise

Test WAN loss, DHCP renewal failure, controller reboot, switch power loss, delayed sensor events, and certificate expiry in an isolated noncritical test setup. Keep a before/after observation log.

**Review boundary:** Local-first is an availability property, not a certification of security or functional safety. Safety-critical actuators need independent design and validation appropriate to the hazard.

## Selected reading and evidence records (non-spoken)

- `rfc2131` — [Ralph Droms, RFC 2131: Dynamic Host Configuration Protocol, IETF (1997)](https://www.rfc-editor.org/info/rfc2131/). DHCP address allocation and configuration.
- `rfc1034` — [Paul Mockapetris, RFC 1034: Domain Names — Concepts and Facilities, IETF (1987)](https://www.rfc-editor.org/info/rfc1034/). Domain names and DNS resolution architecture.
- `cisco-poe` — [Cisco, What Is Power over Ethernet?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-power-over-ethernet.html). PoE standards family and source/device power relationships.
- `cisco-poe-brief` — [Cisco, PoE for Industrial Automation: Power, Data and Control over a Single Cable](https://www.cisco.com/c/en/us/products/collateral/networking/industrial-switches/poe-ind-data-control-single-cable-so.html). IEEE 802.3af/at/bt source and receiver limits and power over pairs.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
