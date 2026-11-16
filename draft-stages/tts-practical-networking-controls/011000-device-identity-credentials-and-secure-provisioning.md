# 011000 — Device Identity, Credentials, and Secure Provisioning

<!-- BEGIN SPOKEN LECTURE -->

A home automation device arrives in a box. You connect it to power, scan a code, and the application announces that it is online. But what has happened to the device's identity? Who decided that it belongs on your network, what credentials were installed, and what happens when it is sold, reset, or abandoned by its manufacturer? Those are practical questions for any household or workshop using networked sensors and actuators.

The first distinction is between recognizing a device and authorizing what it can do. A network address tells other machines where to send traffic; it does not prove that the machine is trustworthy. A MAC address is useful for local delivery and inventory, but it can be copied or changed. A hostname identifies a service for convenience. Neither is a sufficiently strong identity credential on its own. Authentication asks for evidence that a claimed identity is legitimate; authorization decides which actions that authenticated party may perform.

## What provisioning actually supplies

Provisioning is the process of giving a device the configuration needed for participation: local network access, credentials, time and name information, service endpoints, and sometimes permissions. In a Wi-Fi device, that may include network credentials or a secure onboarding mechanism. For an Ethernet sensor, network access may appear automatic, but the application may still need enrollment keys or certificates. Some systems use shared passwords; others use unique secrets, cryptographic key pairs, or certificates chained to a trusted issuer.

A shared password grants the same secret to multiple devices. If one device leaks that secret, the consequences can extend to the others. A per-device credential can restrict the damage and support revocation of one compromised unit without replacing every device's credentials. The feasibility depends on hardware, firmware, onboarding protocol, and administration, not just an app setting labeled secure.

The National Institute of Standards and Technology's work on trusted network-layer onboarding treats this as an entire lifecycle problem. Before network credentials are entrusted to a device, the network may need evidence of its identity or security posture. The device, meanwhile, should avoid silently joining an unauthorized network. There are different ways to achieve these objectives, but the goal is to establish trust rather than assume that mere physical proximity proves ownership.

## Bootstrap credentials are not operational credentials

Manufacturers often need an initial way to enroll a device before it possesses your site's credentials. A printed setup code, temporary pairing mode, factory certificate, or physical button can be part of that bootstrapping step. Each has different attack surfaces. A code photographed and posted publicly can lose its intended secrecy. A pairing mode that remains open indefinitely may expose unintended connections. A certificate without a trustworthy validation process is little better than an unexplained identifier.

In a well-designed workflow, initial enrollment establishes the authority to issue the operational credentials. The setup channel can then be closed or restricted. You should understand what a factory reset changes: does it erase local Wi-Fi credentials, cloud registration, cryptographic keys, device-generated data, and user permissions? Products vary. Resetting an app's state is not necessarily equivalent to removing its authority from the network.

## Separate device, service, and human access

A security camera needs to send video to an authorized recorder. It may not need to reach arbitrary Internet servers, printers, and laptops. A temperature sensor may need to publish readings to a local broker but never administer that broker. A person managing the system needs a distinct identity from the sensor that reports temperatures. These are separate principals with separate privileges.

Network segmentation and firewall rules can limit which destinations a device can contact. Application-level authorization can limit which topics it can publish or control commands it can issue. Segmentation is not encryption, and encryption alone does not tell a service which device is allowed to unlock a door. Good designs combine appropriate identity, confidentiality, integrity, and permission boundaries without depending on one mechanism to do every job.

## Provision for the day the vendor disappears

Device security includes continuing operation and removal. If a camera requires a vendor relay for routine local viewing, a future cloud shutdown can disable functionality that looked local. If the vendor stops publishing fixes, an Internet-facing device may accumulate vulnerability risk. Look for documented local protocols, exportable configurations, maintainable firmware, replacement options, and a clear procedure to revoke a lost or sold device's access.

Keep an asset record containing model, serial or local identifier, firmware version, network location, administrator and service roles, update method, and the date credentials last changed. Do not put secrets in an ordinary inventory spreadsheet. Record *where* credentials are secured and how access will be recovered if the usual administrator becomes unavailable. Backup plans must preserve confidentiality as well as convenience.

## A commissioning and retirement exercise

Take a hypothetical PoE camera. At first connection, it receives an address through DHCP. That is network configuration, not proof of ownership. An administrator then enrolls it using an authenticated management process, changes or establishes unique credentials, sets a time source, limits service exposure, and verifies video reaches the local recorder without unnecessary external dependencies. The camera's firmware and configuration are documented.

Now suppose the camera must be replaced. What happens to its old credentials, its local recording permissions, its fixed address reservation, and its private key? What happens to stored video or configuration on the removed unit? A good retirement plan revokes access and wipes or controls residual data before disposal or transfer. Hardware that no longer operates is not automatically a device that can no longer authenticate.

Secure provisioning is a form of systems engineering. Every device enters a network through a boundary, acquires authority, performs a limited role, and eventually leaves. If you can explain who vouches for its identity, what permissions it holds, how its software is maintained, and how to revoke it, you are no longer relying on the reassuring phrase "connected successfully." You understand the actual trust relationships.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Identity and authorization table

| Attribute | What it is | What it does not prove |
|---|---|---|
| IP address | Current network locator | Cryptographic device identity |
| MAC address | Link-layer identifier | That a claimant is genuine |
| Certificate/key pair | Potential authentication mechanism, with validation | That the holder should access every service |
| Application role | Permission to perform named actions | Trustworthiness of firmware |

### Provisioning exercise

Write a commissioning checklist for a locally operated PoE camera: bootstrap, unique credentials, time sync, minimum network access, local storage, logging, firmware maintenance, backup recovery, revocation, disposal. For each step define what could go wrong and how one would verify success without leaking credentials.

### Original references

NIST CSWP 42 (Fagan, Marron, Souppaya, Watrobski, Kent, Mulugeta, Symington; final 2025) and NIST IR 8350 (Symington et al.; final 2025) distinguish network-layer onboarding and lifecycle management. Product-specific support for certificates, Matter, Wi-Fi Easy Connect, or other mechanisms must be verified rather than assumed.

## Selected reading and evidence records (non-spoken)

- `nist-cswp42-iot-onboarding` — [Michael Fagan, Jeffrey Marron, Murugiah Souppaya, Paul Watrobski, Karen Kent, Blaine Mulugeta and Susan Symington, NIST CSWP 42, Towards Automating IoT Security: Implementing Trusted Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/cswp/42/towards-automating-iot-security-implementing-trust/final). Device/network trust and secure provisioning of local network credentials.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
