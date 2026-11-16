# 020000 — Configuration as Code and Repeatable Device Commissioning

<!-- BEGIN SPOKEN LECTURE -->

An automated door works perfectly until its controller is replaced. The replacement has the same model number, the same wiring and even the same name in the application, yet a sensor event now triggers the wrong action. The difference may be buried in a default setting, a changed firmware version, a retained cloud association or an undocumented automation rule.

In a small automation installation, manual configuration can feel convenient. But as the system grows, the problem changes. You must be able to state what the system is supposed to do, reproduce that state on new equipment and detect when the installed state differs from the intended one. This is the purpose of configuration as code, understood broadly: treating configuration as a reviewable, versioned description rather than as a collection of clicks whose history has been forgotten.

## Identity is not configuration

Start by separating physical identity, network identity and functional identity. A controller has a serial number or hardware identifier. It may receive a different IP address after reboot. It can also have a logical name such as 'garage-light-relay.' Replacing hardware while preserving the logical purpose requires a mapping between these identities. A fixed IP address by itself does not guarantee the replacement behaves correctly.

Then separate desired state from observed state. The desired state says a relay starts off after power restoration, accepts commands only from specified local services and turns on for a defined period after a sensor transition. The observed state might include its actual firmware, enabled services, current network address, relay state and most recent successful command. Configuration management is the process of comparing and reconciling them.

A useful configuration record may include device type, firmware and protocol versions, logical role, safe initial outputs, network placement, sensor-to-actuator mappings, thresholds, timeouts, permissions, and dependency on any remote service. Secrets need special handling: a plain-text configuration in version control should not casually include device passwords, tokens or private keys. Instead record how credentials are provisioned and rotated, while keeping the secret material in an appropriate protected store.

## A change should be repeatable and reviewable

Imagine three humidity controllers installed in different rooms. Each has an 'on above threshold' and 'off below threshold' setting to prevent rapid toggling. One was configured manually with a different threshold. Months later, an operator sees a fan running more often and suspects defective equipment. A versioned configuration lets you distinguish a changed policy from a changed sensor or a mechanical problem.

The principle of idempotence is useful here. An operation is idempotent when repeating it does not continue changing the desired result. 'Set the output to off' is often easier to retry safely than 'toggle the output.' Similarly, 'ensure this named automation exists with these parameters' is safer to reconcile than 'create another automation every time the setup runs.' Actual devices may not support a clean desired-state interface, so a commissioning script must sometimes read before writing and verify afterward.

## Commissioning is more than deployment

A new device should be identified, placed in the intended network segment, authenticated, loaded with approved configuration, and tested against expected inputs and outputs. Record the result. Try a cold boot. Try a network outage. Check whether the physical output returns to the intended safe state and whether stale retained messages create an unwanted action after reconnection.

For instance, a presence-triggered light may reasonably turn on again after an outage, while a garage door motor should not replay a stale 'open' instruction when a message broker reconnects. That difference belongs in the system's state-machine design, not in a one-size-fits-all retry mechanism. A controller that reports successful configuration application but has the relay wired to another circuit has not passed functional commissioning.

Versioning alone is not enough. The deployed environment also includes device firmware, radio quality, sensor calibration, network services, power supplies and physical wiring. A faithful backup of a dashboard may omit a critical setting stored in an end device. Test restoration on a spare unit or in a controlled maintenance window, recording what could not be reproduced automatically.

## How to design the handover

Suppose you are giving the system to someone else. Could that person answer which device controls the basement fan, what its expected startup behavior is, which service sends commands, which credentials it requires and how to verify that it has recovered after a power cut? If the answer requires the original installer to remember every step, the installation is not yet reproducible.

A small but effective handover might consist of a device inventory, exported configuration files, a readable diagram of command flows, a credential-management plan, tested restoration steps and a list of acceptance checks. You can keep these in ordinary text files when the system supports it. Stable naming matters more than elaborate infrastructure.

The goal is not to impose software-development ceremony on every light switch. It is to make replacement and recovery predictable. A practical automation system should be understandable from its saved intent and observable behavior, even after the person who installed it has forgotten the details.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

**Example desired-state declaration (illustrative, vendor-neutral):** device logical ID, hardware ID, approved firmware, network segment, safe startup output, sensors, threshold/hysteresis, maximum runtime, allowable command senders, dependencies and restoration test. Store no secret values in public configuration.

**Acceptance checks.** Fresh-device provisioning; idempotent reapplication; authentication and authorization; offline behavior; cold boot; retained-message handling; rollback; human/manual override. Reconciliation is not a substitute for functional output testing.

**Sources.** NIST IoT Device Cybersecurity Requirement Catalog—Device Configuration and NISTIR 8259A family; IETF HTTP semantics for idempotent methods as an analogy, not a universal guarantee for non-HTTP actuators. Device-specific protocols and firmware determine actual feasibility. Different services and hardware may not offer declarative configuration or reliable export.
