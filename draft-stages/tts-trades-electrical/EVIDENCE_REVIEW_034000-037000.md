# Evidence review — electrical lectures 034000–037000

**Review date:** 2026-11-15. **Status:** educational drafts with source audits, not a certified field or jurisdiction review. Each manuscript contains an eight-claim evidence map, and each claim is linked to the relevant source record in `metadata/<id>.json`. Sources and publisher limitations are listed in `metadata/sources.json`. Spoken lectures teach the physical/engineering story; the full evidence caveats belong here.

## Source evaluation and attribution

- **034000 — water and outdoor routes.** OSHA 29 CFR 1910.305 provides full public U.S. workplace text covering damp/wet equipment and receptacle conditions; it is not a universal private-residence prescription. IEC 60529's publicly available publisher scope identifies IP coding but does not verify detailed ingress test clauses. Schneider Electric and Nidec/U.S. MOTORS independently explain NEMA enclosure designations, neither replacing the NEMA 250 normative text or product certification. UL Solutions discusses environmental accessories and fittings. A rated empty enclosure does not establish that an assembled cable-entry system preserves its rating. Buried routes need installation-specific cable, mechanical, and thermal evaluation; no arbitrary depth is recommended.
- **035000 — receptacles, switches and controls.** OSHA full text supports U.S. workplace receptacle and switching roles, while OpenStax Kirchhoff rules support the ideal changeover-switch circuit model. DOE's *2020 U.S. Lighting Market Characterization* is authored for DOE by Kyung Lee, Sean Donnelly, George Phillips, and Nicholas Panzo (Guidehouse) and describes controls and market patterns, not certified dimmer compatibility. GSA lighting material was search-indexed but not fully retrieved; it cannot be treated as direct primary verification of exact sensor claims. An older DOE Building America lighting guide contextualizes sensor design but is not a current device rule. Lutron Electronics directly documents that some of its two-wire dimmers pass enough current for an LED to glow or flicker while 'off'; this is product-specific evidence, not universal smart-switch behavior.
- **036000 — motors.** Schneider Electric's two motor chapters come from the same publisher; quoted direct-on-line startup-current ranges are illustrations, never equipment-specific predictions. DOE's historic Motor Challenge guide distinguishes motor efficiency and nameplate characteristics but does not establish current legal efficiency classes. Iowa State University's *Applied Industrial Electricity* and DOE Fundamentals Handbook *Electrical Science* Vol. 4 independently develop synchronous field speed and slip. U.S. workplace motor-related 29 CFR 1910.305 requirements concern a distinct scope. Motor-start and protective-device selection still depend on motor, starter, voltage, fault current and approved product data.
- **037000 — heating.** OpenStax derives Joule heating and specific heat (including the approximate water value) and provides the derivation for idealized thermal calculations. DOE technical and Energy Saver articles distinguish resistance heating, induction and heat pumps. The older DOE resistance-heat page is consulted via an archive; that makes it historical public guidance, not a current installation standard. The DOE induction article is credited to Vivien Bui (2023). Neither an induction-efficiency headline nor a generic resistive-heater discussion establishes a given product's performance or high-limit control construction.

## Outstanding technical and evidence questions

| Area | Outstanding question | Consequence |
|---|---|---|
| Exposure / enclosures | Obtain full adopted IP and NEMA test clauses and verify whole-assembly ratings, fittings, orientation, service access, corrosion and wet/underground classification | Secondary descriptions cannot establish actual listed equipment performance |
| Switching / lighting | Check actual LED driver, dimming protocol, control neutral architecture, occupancy-sensor behavior and applicable product documentation | Manufacturer compatibility and sensor detection are model-specific; the GSA index excerpt is not clause-level evidence |
| Motors | Obtain individual motor nameplate, starting method, rotor/load speed–torque curves, overload and short-circuit protection characteristics, power-system impedance | Starting current and voltage dip cannot be determined from generic multiples |
| Heating | Verify equipment-specific nameplate and independent high-limit design; obtain published method for comparable cooker/heater efficiency ratings | Generic heat-balance models do not validate a thermal appliance |
| Code / jurisdiction | Inspect the binding NEC, OSHA, IEC national-adoption or local rule and correct product instructions for each use case | Publisher abstracts and historical guides cannot prove a present enforceable requirement |

## Calculation spot checks

- A hypothetical 1,500 W heater at 120 V: `I = P/V = 12.5 A`. Continuous four-hour energy: `1.5 kW × 4 h = 6 kWh`; at a 40% on-duty fraction: `2.4 kWh` (assuming fixed energized power).
- A hypothetical two-kilowatt resistive heater at 230 V: `I = 2000/230 ≈ 8.70 A`.
- Three-phase motor thought experiment: `P_out = 3000 W`, `η = 0.88`, `PF = 0.84`, `V_LL = 400 V`; `I_line = 3000/(0.88 × √3 × 400 × 0.84) ≈ 5.86 A`.
- Ideal 4-pole induction motor field at 60 Hz: `n_s = 120 × 60 / 4 = 1800 rpm`; rotor runs below that speed when producing torque.
- Idealized 1 kg water temperature rise of 20 K, `c≈4180 J/(kg K)`: `Q≈83,600 J` and minimum heating time at 2 kW `83,600/2000≈41.8 s`, without vessel or environmental losses.

## Review boundary

The sources have been organized at claim level and the math spot-checked, but there has been no independent qualified electrical, firestop or equipment-listing review. Code and standards references retain explicit edition/access boundaries. Editorial checks do not certify real installations. No repository-wide testing, TTS generation or server actions are needed for this source-only batch.
