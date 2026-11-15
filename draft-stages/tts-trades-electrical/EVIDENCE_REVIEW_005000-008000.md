# Electrical foundations 005000–008000: evidence and field-review ledger

**Prepared:** 2026-11-15. **Authority:** educational source review only; neither qualified electrical inspection nor an adopted-code determination. **Scope:** four newly authored conceptual manuscripts. **Prior status:** lectures 001000–004000 unchanged in this overlay.

## Checked source families and their actual role

- **Physics textbook:** Samuel J. Ling, William Moebs and Jeff Sanny, *University Physics Volume 2* (OpenStax, 2016), exact §§8.3, 9.4–9.5, 10.2–10.5, 14.2–14.4 and 15.1–15.4 as listed in `metadata/sources.json`. Public explanatory sections were consulted for constitutive equations, RC/RL transients, RMS, impedance and sinusoidal power. This is **not** evidence for touching, installing or repairing home wiring. §10.6's neutral-contact misstatement, previously documented in the track evidence policy, is not adopted here.
- **Independent engineering pedagogy:** Anant Agarwal / Jeffrey H. Lang, MIT 6.002, course description and Agarwal's Lecture 2 transcript. The lecture's lumped-element assumptions and KCL/KVL formulation corroborate modern textbook teaching independently; a course syllabus alone does not verify a specific result.
- **Harmonic-power measurement research:** C. Martinsons, Y. Zong, C. Miller, Y. Ohno, F. Olive and N. Picard, CIE x038:2013 proceedings, NIST-hosted PDF. The abstract, §2 and §3 (including equations 1,2,8–10, pp. 290–293) support the distinction between harmonic content, source impedance and measured power. It is not a NIST regulatory mandate or a universal claim about all lamps.
- **Power quality in practice:** Fluke Corporation's public educational articles on power factor, harmonic currents, equipment and symptoms support only *contextual engineering explanations*. Their manufacturer status is disclosed. They do not certify homeowner wiring procedures or make all possible faults equally likely.
- **Legal/professional boundary:** OSHA 29 CFR 1910.333 and 1910.304 are cited only as *U.S. occupational* safeguards and examples of distinction between physical hazard and legal scope. IEC 60364-1 publisher abstract is cited as standards-family scope, **not** as an inspected clause or local adoption.

## Claim-specific limits to preserve

| Concern | What has been checked | What remains open |
|---|---|---|
| 005000: concentration of resistive heating | Ideal \(I^2R\) calculations from textbook | Independent qualified review of connector-failure discussion, ratings and environmental causes; no DIY torque or wiring instructions |
| 005000: KVL and field effects | MIT lumped abstraction and textbook Faraday induction | More advanced treatment of electromagnetic flux and non-lumped circuits, without implying KVL holds for every time-varying physical loop |
| 006000: waveform and RMS definitions | OpenStax §15.2, §15.4 and independently checked research on distorted power measurements | Application-specific metering instrument characteristics, non-sinusoidal conditions, and device ratings |
| 007000: residual stored energy | Textbook §§8.3,10.5,14.2–14.4 and OSHA occupational work-practice context | No field discharge or verification procedure has been qualified; stored-energy and product-specific manuals required before use |
| 008000: distortion and neutral currents | NIST/CSTB research for harmonics/power measurement; Fluke application note for system-level neutral issues | Independent peer-reviewed or standards-based corroboration for conditional neutral loading, plus relevant wiring system specifics |
| 008000: power-factor correction and billing | Fluke technical article, checked against resonance physics; general distinction between real and apparent power | No customer-specific tariff, no correction equipment recommendation, and no locally reviewed installation design |

## Publication gate

Every new lecture's `metadata/<id>.json` contains stable `E<ID>-NN` claims, source IDs, scope limits, and `professional_review: pending`. These records are an editorial trace, **not a certificate**. Before the course is promoted from educational draft to practical field guidance: obtain documented qualified electrician/engineer review of actual claims and jurisdiction; consult exact locally adopted code and manufacturer instructions; supply qualified field procedures for any live work, electrical protection, source transfer or meter connection. Do not ask a beginner to reproduce a high-energy example.

The mathematics of the four worked numerical examples has been independently recalculated in the authoring environment; that confirms arithmetic only. The lecture duration is not constrained by a target, maximum, minimum or word-count quota.
