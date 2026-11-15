# Electrical protection and transformer lectures: evidence review (009000–013000)

**Date:** 2026-11-15. **Status:** source-audited educational drafts only. **Scope:** public textbooks, independently authored government engineering guides, safety agencies, UK regulator/IET guidance, manufacturer explanations, public UL/IEC scope excerpts and U.S. occupational regulation. This is not an independent professional review and not locally adopted code verification.

## Manuscript and source status

| Lecture | Focus | Main independent evidence lines | Open questions |
|---|---|---|---|
| 009000 | Field coupling, transformer ratios, losses, limits of isolation | OpenStax §15.6, U.S. Bureau of Reclamation 2005 §§2.1–2.10, DOE efficiency context | Protective-isolation product standards, inverter-specific transfer and fault behaviour, inrush under actual waveforms |
| 010000 | Shock paths, body effects, first aid | SBCTC non-electrician training (OSHA-funded **not authored by OSHA**); IEC 60479 published scope only; NHS inform and Mayo Clinic medical guidance | Full IEC 60479 physiological criteria; utility step-voltage primary reference; clinical reviewer, local emergency procedures |
| 011000 | Overload, available fault current, interrupting rating and coordination | OSHA 1910.303/304 (workplaces), Eaton Bussmann engineering, Schneider trip mechanisms, CPSC arc-fire distinctions | Exact installation current calculation, tested protective combinations, local code and product certification |
| 012000 | Earthing, protective bonding, TN/TT/IT, PE versus neutral | IET earthing/bonding guidance, OSHA 1910.304 and electrical-library diagram, Schneider Electric IEC-based earthing guide | Full IEC 60364 and BS 7671 normative clauses, local service bonding rules, qualified fault-loop commissioning |
| 013000 | GFCI/RCD, AFCI/AFDD, RCCB/RCBO, SPD functions | OSHA GFCI text, UK HSE safety guidance, CPSC publication 5133; public scopes of UL 943/1699/1449 and IEC 61008-1 | Actual listed product performance and compatible breaker, adopted code location requirements and waveforms |

## Key verified limitations and attribution

1. **Do not treat earth as the universal high-current return path.** Metallic fault-return behavior in common grounded U.S./TN-like arrangements is distinct from TT electrode/earth paths. Published OSHA introductory diagrams sometimes simplify soil, so read the exact OSHA regulation and IET/IEC-based arrangement discussion before writing a general claim.
2. **Neutral is not touch-safe.** An OSHA standard interpretation explicitly discusses energized open-neutral situations. No narration instructs touching a conductor to identify it.
3. **A GFCI/RCD is not universal personnel protection.** OSHA's public eTool explicitly identifies balanced line-to-neutral contact cases outside its protective function, and UK HSE states that RCD protection is secondary to safe isolation. The published IEC 61008-1 scope describes RCCBs *without* integral overcurrent protection.
4. **AFCI is not a hot-connection detector.** CPSC explains why some arcing hazards evade conventional overcurrent protection. UL 1699:2025 §1.3 says AFCIs are not intended to detect glowing connections. Only the published scope excerpt was directly reviewed, not the full normative text or a product test report.
5. **Official-looking PDFs require authorship checks.** The *Electrical Hazards for Non-Electricians* binder is written by California's State Building and Construction Trades Council and produced under an OSHA grant; its disclaimer says it does not necessarily reflect OSHA policies. It is not attributed as OSHA-authored training.
6. **No first-aid improvisation is taught.** NHS and Mayo Clinic sources support avoiding direct contact with a potentially energized casualty and summoning emergency help. Rescue techniques and clinical triage remain local, trained-response matters.
7. **No numerical threshold is a safe-touch permission.** Human physiology depends on path, contact condition and time; device trip ratings describe performance of tested equipment, not safe current through a particular person.
8. **Jurisdiction distinction.** OSHA 29 CFR regulations are workplace rules in covered U.S. situations, not universally applicable homeowner electrical-code requirements. Public NFPA/IEC/UL product pages establish edition and scope only; full local adoption and product ratings are separate decisions.

## Review gates and verification limits

- Complete independent electrical-engineer/electrician review of the technical safety claims before promoting this material to field guidance. Lectures 010000 and 013000 additionally benefit from medical/shock-protection specialization.
- Obtain qualified review of the complete adopted code and equipment instructions for any jurisdiction-specific prescription. Do not infer residential compliance from OSHA workplace law.
- Inspect complete normative standards or traceable excerpts for any future numerical protective limit, device response time, minimum electrode requirement or physical work procedure. Catalog abstracts do not suffice.
- Check whether the original induction discoveries are attributed with adequate historical primary sources if expanding historical treatment; current references support modern physical explanation but not a full history campaign.
- No panel opening, human-current experiments, manual GFCI-fault insertion, conductor-ground testing, or live-work procedure appears among exercises.
- Descriptive narration word counts must match canonical extraction. No duration/word-count quotas apply.

**Source-map method:** Every new manuscript ends with a non-spoken claim table. Companion `metadata/<id>.json` records claim IDs, exact source locations, support type, evidence gaps and review status; `metadata/sources.json` stores credited publication authors/standards committee, role, access and limitations. Different documents from the *same publisher* are not claimed as independent merely because they provide multiple URLs. Automated indexing cannot establish factual truth or competence to work with energized equipment.
