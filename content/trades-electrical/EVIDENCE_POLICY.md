# Evidence, attribution, and safety review policy for electrical trades lectures

**Status:** mandatory authoring standard for this track, adopted 2026-11-15. Applies to every existing and future lecture. This document is an editorial policy, not an electrical standard or authority to perform installations. The examples deliberately distinguish pedagogy from professional qualifications.

## Purpose and organizing principle

A listener may act upon a lecture about electrical systems, unlike a lecture about a mathematical theorem. An incorrect premise can lead to severe injury, fire, equipment damage, or unsafe modifications. Do not treat polished prose, a citation, mathematical correctness in an ideal circuit, or an automated test as sufficient evidence of safe application. A scientifically valid generalization may still be inappropriate for a particular system. **Safety-relevant claims must be traceable, matched to an appropriate type of source, and explicit about their limits.**

No lecture has a ten-minute target, minimum word count, or runtime quota. Thorough explanation of failure modes, limitations, and source scope takes priority over brevity. A short lecture that is completely supported is preferable to a longer lecture containing unsupported actionable advice; a longer lecture is appropriate when the material demands it.

## Five different kinds of claims — do not mix their authority

1. **Physical principles:** voltage, current, Joule heating, energy transfer, electromagnetism. Verify against primary scientific literature or reputable engineering/physics texts, with exact sections and attribution to original discoverers when historically germane. These texts explain physics, not permission to wire a home.
2. **Engineering and protection mechanisms:** current return paths, fault clearing, GFCI/RCD operation, touch voltage, environmental ratings, PV/battery source interfaces. Favor engineering standards, manufacturer specifications, accident investigations, laboratory testing, and independent technical publications. Identify simplifying assumptions and failure modes.
3. **Hazards, emergency response, and procedures:** use applicable regulatory language, workplace standards, accredited safety training, CDC/medical guidance, and incident data. Separate conceptual explanation from procedures requiring competent or qualified personnel. Where sources conflict, prefer safety-preserving statements and record the discrepancy. Do not teach inexperienced listeners to perform energized tests or manipulate household equipment to create faults.
4. **Normative code requirements:** identify **jurisdiction, legal adoption, exact standard identifier and edition, article/clause/table, exceptions, amendments, effective date, and applicability**. A 2026 NEC edition or IEC abstract is not evidence that a particular home must comply with its uninspected text. OSHA requirements apply to their occupational scope, not automatically to private homeowners. Verification against the locally adopted text is required before describing a mandatory installation method.
5. **Product-specific requirements:** use exact model/version, listing/certification scope, installation instructions, environmental/electrical ratings, compatibility, and conditions of use. A general vendor brochure or compatible-looking connector is not enough to conclude a specific combination is safe.

## Attribution is more than a URL

- Credit named authors or organizations that wrote the **particular** referenced material, not merely the site hosting it. Where the historical origin of a principle matters, distinguish its discoverer, subsequent improvements, and the modern source explaining it. Credit standards committees or standards organizations for collectively authored documents instead of inventing an individual author.
- Give an exact, stable reference where possible: author, title, edition/year, section, page or clause, public URL and date checked. A source must support the **specific** claim attached to it. A link about "electrical safety" is not evidence for a particular breaker rating or disconnection procedure.
- Label the source's role: direct primary text, secondary explanation, historical attribution, contextual background, standards **scope only**, or independent corroboration. Two websites repeating the same agency's explanation are not independent confirmation. A secondary source that mentions the same topic but not the actual claim is context, not corroboration.
- If the full normative text is paywalled or otherwise not examined, mark `publisher_scope_abstract_only`; never imply its internal clauses were verified. Record statements whose support is absent as `unverified` or `requires expert review` rather than fabricating a clause or source.
- Avoid lengthy copyrighted excerpts. Write original narration and short paraphrases with precise citations; record the original paper, authorship, engineering report, or standard when known.

## Claim-ledger workflow

For every manuscript, retain a **source map outside the spoken lecture** so listeners receive fluent narration but reviewers can find supporting evidence. Its companion `metadata/<id>.json` has `evidence_claims`; every consequential claim gets a stable ID, text, kind, source ID, exact location, `verification_level`, limitations and reviewer status. Bibliography records live in the track-local `metadata/sources.json`, not a shared register. Source records must state scope, authorship, review date, whether the public text or only an abstract was checked, and material limitations.

Do not enforce a citation count or citation-per-word quota. Instead, enumerate **all safety-critical and jurisdiction-specific assertions**, including assertions embedded in worked examples and exercises. For physically consequential decisions, seek at least two genuinely independent and suitable evidence lines when feasible; if not feasible, mark the gap explicitly and do not present the detail as validated practical instruction. Do not generate citations merely to hit a numeric target.

Every new lecture should include:

- A claim-by-claim source map identifying the section in the lecture where the idea is explained, with independent corroboration or a marked evidence gap for consequential claims.
- Original authors/researchers where relevant and reliably established, standard committee attribution for normative texts, and dates/editions for changing guidance.
- A distinction between the principle, the protective objective, and the locally adopted requirement. No U.S. default assumptions for all regions.
- A companion section listing assumptions, boundary conditions, counterexamples and cases where the protection fails; in particular, avoid implying neutral is safe to touch, earthing alone clears every fault, or a protective device guarantees prevention of all injuries.
- Exercises classified as calculation, paper schematic, isolated low-energy teaching kit under trained oversight, observation without opening equipment, or professional-only. A lecture cannot instill competence to perform live electrical tasks.

## Required human and jurisdictional verification

Before describing a lecture as **field-validated**, obtain independent review from a qualified electrician or electrical engineer knowledgeable about the actual application and jurisdiction. Procedures involving energized measurement, work on panels/service equipment, batteries/inverters, source transfer, and utility interconnection need application-specific professional review and the proper product and adopted-code documents. Emergency-response claims should be aligned to reputable first-aid/medical guidance. The reviewer must document what they actually evaluated; a credential alone does not validate content outside the reviewer's competence.

Editors must distinguish these states: `draft` → `source_audited` → `professionally_reviewed_for_stated_scope` → `jurisdiction_and_product_verified_for_specific_application`. The opening four lectures currently remain **source-audited drafts**. No professional validation, field testing or full adopted-code verification is claimed.

## Counterexample: apparent credibility is not safety evidence

OpenStax's *University Physics, Volume 2*, §10.6, **Household Wiring and Electrical Safety**, calls a neutral conductor safe to touch and offers simplified earth-return explanations. That is **not a safe general rule**: an open neutral can remain energized, as OSHA's July 7, 2003 interpretation explicitly documents. Use the OpenStax book's accurately scoped physics sections for current, voltage, and power, but do not use that chapter as installation safety authority. See:

- [OpenStax §10.6 (identified safety misstatement)](https://openstax.org/books/university-physics-volume-2/pages/10-6-household-wiring-and-electrical-safety)
- [OSHA interpretation of energized open-neutral conditions (July 7, 2003)](https://www.osha.gov/laws-regs/standardinterpretations/2003-07-07-1)
- [OSHA §1910.333(b)(2)(iv), qualified verification of deenergization in covered workplaces](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333)

Do not turn this into a general indictment of the textbook: the finding applies to a specific safety claim. **Cross-check source suitability claim by claim** and record conflicts. Another example: OSHA's introductory grounding pages can suggest that soil is the fault-current return. Installation-specific fault paths depend on the grounding/earthing system; the eTool alone cannot support a general design conclusion.

## Change control and repeat review

- When revising a lecture's spoken content, update its `spoken_words` **descriptive** count from the repository's canonical extractor, but never treat words or minutes as a quality threshold.
- Recheck any changed citation links and record revision dates; standards, code adoption, utility policies, manufacturer instructions, and official medical recommendations can change. Keep older source links with explicit dates where they document historical practice.
- Every overlay changes only this track's paths and includes no binary assets. The inventory tool checks that a manuscript is indexed and that source IDs exist; **it cannot establish factual truth or safety**.
- A failed citation audit, unresolved contradictory source, or missing qualified review should be visible in the audit, not hidden by automated green checks. Separate the publication or practical-action gate from the ability to play the lecture as an educational draft.
