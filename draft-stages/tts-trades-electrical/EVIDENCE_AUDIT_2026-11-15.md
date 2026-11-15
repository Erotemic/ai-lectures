# Evidence audit: Electrical Systems opening lectures 001000–004000

**Date:** 2026-11-15 · **Status:** `source_audited_draft_not_professionally_approved` · **Scope:** sources, evidence fit, pinpoint citation, and attribution in four audio manuscripts. This is an editorial audit, not an electrical engineer's design verification or a test of real installations.

## Findings from the original four-lecture ZIP

The opening course structure was generally cautious about live work and regional differences. But bibliography lists alone were insufficient evidence for safety-critical material. The original source registry contained **16 distinct sources**, many referred to from multiple lectures; key physics assertions had no directly suited engineering/physics citations. Important model standards were cited by **public catalog abstract**, which only confirms scope/edition, not any specific requirement. Per-lecture metadata had references but no claim-to-source ledger. Assertions about neutral/ground fault paths and personnel protection needed narrower, more independently auditable support. Thus the original state was **not validated practical instruction**.

## Corrections included with this audit

| Issue | Action | Remaining boundary |
|---|---|---|
| Original 16-source bibliography lacked direct fundamental-physics citations | Added source-specific OpenStax §7.2, §9.1, §9.4, §9.5, §10.1, §15.2 and §15.4, with Ling–Moebs–Sanny authorship and narrow topic scope | Physics text cannot support field safety or conductor selection |
| Shock procedures and injury risk | Added CDC first-aid guidance; aligned spoken wording to seeking emergency help and avoiding contact with an energized victim | No first-aid instruction replaces formal practical training |
| Neutral potentially energized | Added OSHA July 7, 2003 **open-neutral interpretation**, directly supporting the warning; kept neutral distinct from protective grounding | OSHA interpretation has occupational scope; installation practices still depend on system |
| Residential U.S. split-phase systems | Attributed example to the PNNL/US DOE distribution report with its named authors and Appendix A location | Typical architecture is not universal, and report is not an adopted code |
| Ground-fault interruption | Added OSHA's construction GFCI technical explainer, explicitly including balanced-line-contact limitation | Other RCD device classes and ratings vary; simplified explainer is not all-inclusive |
| RCD without integral overcurrent | Added public IEC 61008-1:2024 scope with committee attribution | Abstract only; the 240-page normative standard was not audited |
| PV interconnection | Added IEEE 1547-2018 publisher scope to contextualize grid-interface claims | Full standard, utility rules and equipment-specific requirements not verified |
| Codes and regulations | Marked NFPA 70, 70E, IEC 60364, BS 7671, CSA C22.1 and AS/NZS 3000 listings as **scope/edition evidence only**; clarified OSHA workplace scope | No locally adopted edition/amendment or exact installation clause has been examined |
| Source traceability | Added explicit claim-ID maps for every opening lecture and structured `evidence_claims` in their JSON sidecars; named authors/organizations and pinpoint locations | Other claims, downstream lectures, and real applications still need independent review |
| Authorship | Named original discoverer Georg Simon Ohm where it fits; credited PNNL report authors and collectively authored standards to their organizations/committees | Do not infer individual standard authors without a named attribution record |

## Quantitative coverage (inventory, not a quality score)

- **Four** completed manuscripts with linked evidence maps, each with stable IDs.
- **38** explicit narrow claim-to-source ledger entries across the four lectures (8, 10, 10, 10).
- **30** bibliography entries after this pass, up from 16.
- Additional explanatory source links and context may appear in the manuscripts, but repeated citations from the same source are **not independent corroboration**.
- No imposed citation-per-paragraph, word-count, or ten-minute target. A high claim count is not sufficient unless the claimed source directly supports the exact statement.

## Red flags identified during checking

1. **Credible textbook does not mean safe installation authority.** OpenStax *University Physics*, vol. 2, §10.6 treats neutral as safe to touch. OSHA's 2003 open-neutral letter directly describes circumstances where a neutral remains energized. The course correctly warns against touching neutral; this audit explicitly avoids endorsing that textbook's unsafe safety passage. Physics sections of the same book remain useful for precise, limited claims.
2. **Ground/earth confusion.** A generic explanation suggesting current simply flows into soil cannot justify fault clearing in every system. Bonding and return-path architecture require system-specific treatment and normative text. OSHA's grounding eTool has a documented limitation in `metadata/sources.json`.
3. **Workplace jurisdiction does not establish homeowner legal requirements.** OSHA §1910.333 and §1910.304 can document sensible mechanisms and employer duties but cannot be used as proof of the NEC edition adopted by any U.S. city, a homeowner's right to perform work, or an inspector's required installation detail.
4. **Publisher abstract ≠ adopted standard.** The publicly readable IEC 61008-1 scope supports the existence of RCCBs without integral overcurrent protection, not a project-specific tripping criterion or product selection. IEEE 1547 publisher descriptions similarly cannot establish installed settings.
5. **Safety claims are not all independently corroborated.** A source map is a traceability improvement, not an evidence-grade guarantee. Some entries remain contextual rather than independent confirmations of the exact claim.

## Release gates still open

**Must be completed before treating the series as validated hands-on instructions:**

- Obtain documented review of the hazard and installation content by an appropriately qualified electrical practitioner; use independent reviewers where hazard severity and jurisdiction warrant. Review qualifications and actual scope of work, not only job titles.
- For any concrete U.S. code instruction, establish the exact local code adoption, effective date and amendments, and verify actual NFPA 70 clauses, article definitions, tables, exceptions, and listing instructions. Do analogous region-specific checks for IEC-adopting countries, UK, Canada and Australia/New Zealand. Do not infer national implementation from a publisher catalog.
- For advice about devices, batteries, inverters, transfers, grounded/ungrounded systems, arc fault ratings, GFCI/RCD thresholds or measurement instruments, document actual equipment type, tested/approved configuration, source constraints and limitations. No generic lecture should be an installation recipe.
- Independent second-source confirmation remains incomplete for some safety-critical claims. Continue cross-checking with authoritative original sources and record uncertainty instead of inflating the bibliography.
- Maintain the gap audit as the remaining 70-lecture roadmap is drafted. The 38 ledgers cover **only the opening four**, not future lectures.

## Reproduction and boundaries

Run `python tools/lecture_inventory.py` after applying the overlay. Successful extraction, bibliographic ID resolution, and source counts demonstrate **format consistency only**. They do not prove that the source is accurate, its claims are current, or the proposed action is safe. See `EVIDENCE_POLICY.md` for the required editorial workflow and revision controls.
