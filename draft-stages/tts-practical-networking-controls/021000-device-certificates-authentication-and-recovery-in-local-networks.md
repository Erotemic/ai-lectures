# 021000 — Device Certificates, Authentication, and Recovery in Local Networks

<!-- BEGIN SPOKEN LECTURE -->

A home automation dashboard shows that all cameras have gone offline, yet their Ethernet links are up and a local ping still works. Yesterday the devices were trusted; today the controller rejects their connections. No hardware was replaced. The cause may be something invisible on a network diagram: a certificate expired, a device clock changed, or the controller lost the authority needed to recognize a device's identity.

Security credentials are not just a login screen. They are pieces of state with owners, lifetimes, renewal rules and recovery paths. If we want a local-first automation system to survive a cloud outage, we must design its identity and trust system to survive one too.

## Identity, authentication and authorization are separate

Identity answers which device or service we believe we are communicating with. Authentication supplies evidence supporting that claim. Authorization decides what the authenticated party is allowed to do. These are different questions. A camera might prove that it possesses the private key corresponding to a particular certificate, but that does not mean the camera should be permitted to unlock a door or change a thermostat.

In certificate-based authentication, a device may hold a private key and a certificate binding its public key to an identity under a trusted issuer. During a secure connection, the peer checks the certificate chain, validity period, name constraints and other policy; cryptographic handshake operations demonstrate possession of the appropriate private key. A certificate is not a secret password. Its associated private key is what must remain protected.

The certificate also has a time interval when it is considered valid. If the controller's clock is wrong, a perfectly legitimate certificate may appear to be from the future or already expired. An offline system with no working time source can therefore lose access to local devices despite having working power and network cables. This is why time synchronization belongs in an availability design as well as in a security design.

## The trust-anchor problem

Imagine a device whose certificate was issued by a private local certificate authority. The controller must recognize that authority as trusted. If the authority's certificate is replaced without updating clients, all the device certificates issued under it may become untrusted. If a certificate expires, replacing it with a fresh one is not enough when the corresponding device identity, key ownership or trust chain has not been updated correctly.

Now consider a private key leak. An attacker who obtains a usable key could impersonate a device if other authentication constraints do not stop them. Recovery must include invalidating or revoking the old credential and provisioning a new one. Deleting a suspicious certificate file while leaving a compromised copy of the key active somewhere else does not solve the problem.

Certificate systems need inventory: which device holds which credential, who issued it, what name it asserts, what service relies on it, when it expires and how it is replaced. The same inventory must track a trust anchor carefully, because losing it or rotating it incorrectly may affect every device in the household. The inventory should not casually contain exportable copies of all private keys.

## Offline availability is an architectural decision

A system described as local may still contact a cloud identity provider at enrollment, refresh a token remotely or validate a certificate through a network service outside the house. It can work fine with the Internet connected and fail weeks later when a token expires. Test the full lifecycle, not just the ability to switch a light once while the router's Internet cable is unplugged.

There are tradeoffs in revocation. An online revocation check can give a client fresher information, but can also create a dependency on another server. A system that ignores revocation completely may continue trusting a lost credential. Some deployments use short-lived credentials with automated renewal; others distribute revocation information locally. Whatever the approach, its failure behavior must be explicit. Does it fail closed for dangerous actuators? Does it preserve local monitoring? Can a new controller be enrolled without the manufacturer's cloud service?

Enrollment itself is a critical boundary. A factory-new device needs a way to establish a relationship with the local controller. That might involve a physically confirmed code, a provisioned certificate, a QR-based secret or a trusted onboarding channel. If anyone connected to Wi-Fi can claim to be a new lock or controller, strong encryption after enrollment does not repair the original trust failure.

## Designing an incident recovery drill

Suppose a controller is replaced after a disk failure. The device network still works, but the new controller has no credential database. Can it restore its own keys and certificate configuration from a protected backup? Can it re-establish trust without resetting every sensor? Does that backup create an unacceptable risk if stolen? Are the device credentials bound to hardware and deliberately non-exportable, requiring an enrollment procedure instead of copying keys?

A disciplined test uses a spare or noncritical device first. Record the current trust chain, expiration dates and backup process. Simulate an expired device certificate in a controlled environment, rotate a test certificate and confirm the controller recognizes the new identity while refusing the invalid old one. Verify that routine operation remains possible without an external authentication service, if offline continuity is a design requirement.

For high-consequence automation, define the safety state separately. A camera that cannot authenticate might stop transmitting, but a door lock or water shutoff needs an explicitly designed behavior under loss of communications. 'Fail secure,' 'fail safe,' and 'remain available' can demand different actions depending on the device and context. Security architecture cannot be chosen without understanding the physical system it controls.

The practical takeaway is that certificates are living configuration, not decorations added after installation. Their creation, inventory, renewal, loss and replacement are part of operating the network. A genuinely reliable local system must know who its devices are and must still be able to answer that question after an outage, an expired credential or a controller replacement.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

**Credential register:** Device; role; key generation and storage location; subject identity; issuer and trust anchor; certificate fingerprint; validity start/end; renewal owner; revocation mechanism; provisioning/replacement method; local/offline dependencies; recovery test date. Do not put secrets or private keys in the ordinary register.

**Failure matrix:** Controller clock inaccurate; device certificate expired; issuer certificate untrusted; key compromised; controller disk loss; token renewal depends on cloud; local DNS fails; safety-critical actuation loses identity. Distinguish a TLS connection failure from authorization denial after successful authentication.

**Test boundary:** Carry out renewal and trust-anchor drills on test devices first; changes to real locks, alarms, life-safety equipment or water valves require a designed rollback. A certificate does not grant authorization by itself.

**Sources:** NIST SP 800-57 Part 1 Rev. 5, *Recommendation for Key Management* (certificate inventories, expiration and recovery); NIST IoT onboarding guidance; NIST digital identity and derived credential lifecycle materials (conceptual comparison, not blanket application of federal PIV rules to home devices).
