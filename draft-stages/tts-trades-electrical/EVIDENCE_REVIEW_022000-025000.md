# Evidence and editorial review: electrical distribution 022000-025000

**State:** source-audited educational drafts, not professionally reviewed for a specific installation. No lecture-duration target applies. All source mappings and claims live in `metadata/<lecture_id>.json` and in the non-spoken companion of each manuscript.

## Scope and source quality

- **022000 - Services and boundaries.** Uses OSHA 29 CFR 1910.399 definitions *within their U.S. workplace scope*, an NFPA public Article 100 committee record as **historical standards-development evidence rather than the final enacted NEC**, and NYSEG public utility documents as a specific example of a service point, meter ownership and separate customer responsibilities. Schneider Electric provides independent engineering-network comparisons. Exact service-point position, tariff edition and ownership must be confirmed from the serving utility's current documentation.
- **023000 - Supply arrangements.** Uses OpenStax physics for ideal AC, transformer and power relationships and Schneider Electric's publicly available Electrical Installation Guide for North American center-tapped, 120/208 V wye, 230/400 V wye and other voltage arrangements. IEC 60038 is **reported secondarily** through Schneider; the full current edition and each national adoption have not been examined. Calculated 180-degree and 120-degree phasor examples are original algebra with stated balanced-waveform assumptions.
- **024000 - Neutral and protective conductors.** Uses OSHA published grounded/equipment-grounding conductor definitions, a primary OSHA open-neutral interpretation, and Schneider Electric's TT/TN/IT and PEN discussions. The official IEC 60364-5-54:2011+A1:2021 catalogue identifies the standard's scope and responsible IEC TC64 committee; the complete clauses have not been read. Open-PEN system mitigation, earthing electrode resistance, inverter neutral switching and required protective-device combinations remain **system-specific review tasks**.
- **025000 - Feeders, branches and load diversity.** Uses OSHA's public feeder, branch circuit and outlet definitions; Schneider Electric's explicit warning about conflicting use of the term 'diversity factor'; OpenStax's physics; and NFPA's own 2025 explanation that the 2026 NEC reorganized load calculations under Article 120. It does **not** claim that Article 120 has been legally adopted in a particular location. An IEC public 60364-5-52:2009+A1:2024 catalogue verifies scope and edition, not any exact conductor sizing clause.

## Major claims checked against independent perspectives

1. **Utility handoff is not automatically the property line or meter:** U.S. OSHA definitions and NYSEG descriptions support the distinction; an NFPA process report documents historical code terminology. Confirm local boundary for any actual project.
2. **120/240 V versus 120/208 V:** ideal transformer and phasor relationships agree with circuit theory and Schneider's published regional voltage descriptions. The hypothetical 2400 W / 240 V constant-resistance load becomes approximately 1803 W / 208 V when its resistance is held fixed. Real equipment voltage ratings are not inferred.
3. **Neutral, PE, PEN and earth electrode are different:** OSHA conductor rules and the Schneider installation-system framework support this distinction. A ground electrode alone does not demonstrate an adequate low-impedance fault-clearing path. The numeric electrode model illustrates impedance only and is **not** a protective-device timing calculation.
4. **Connected load versus simultaneous demand:** Schneider distinguishes coincidence from reciprocal diversity and discloses inconsistent terminology used in published practical tables. The four-by-five-kilowatt calculation is a classroom profile; it does not replace prescribed branch, feeder or service calculation methods.
5. **2026 NEC load-calculation reorganization:** NFPA publicly identifies the new Article 120, rather than silently reusing the 2023 Article 220. The adopted edition and its amendments remain a local question.

## Unresolved evidence and review items

- **Normative access:** public IEC abstracts and NFPA explanatory pages are not the full standards. The actual adopted NEC edition, IEC implementation, utility tariff clauses, local amendments and listed equipment instructions have not been checked for a real job.
- **Qualified electrical review:** still pending for multi-source disconnection boundaries, source switching, neutral/PEN behavior under open faults, protective device compatibility and practical circuit sizing.
- **Full utility tariff and metering rules:** NYSEG is one concrete case, not a universal allocation of ownership. The tariff excerpt is not a confirmed current service authorization for any address.
- **Three-phase and harmonics:** balanced sinusoidal formulas are verified as ideal calculations; actual power factor and neutral harmonic loading require valid measurement/simulation models.
- **Load control:** permitted derating based on controller behavior requires the actual locally adopted requirements, product capabilities, failure behavior and verification method. The example intentionally makes no reduction permission claim.
- **Source independence:** two Schneider Electric pages are still one publisher; they do not constitute two independent confirmations. OSHA and NFPA publications are different regulatory/standards bodies, but neither substitutes for the other when stating a binding code requirement.

## Editorial boundaries

The spoken text explains engineering mechanisms and interprets schematics without repeated generic safety disclaimers. Detailed boundary conditions are collected in the non-spoken companions. All exercises are paper/simulation only. No server modules, TTS config, shared registries, or other agents' content was modified. This evidence review is editorial; it is not a professional electrical or legal certification.
