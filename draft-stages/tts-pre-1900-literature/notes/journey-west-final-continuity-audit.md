# Journey to the West — final expanded-retelling continuity and evidence audit

**Checked:** 16 November 2026, after writing selected-witness chapters 94–100. **Scope:** this project's **literary** retelling in `draft-stages/tts-pre-1900-literature/`, section `late-ming-chinese-novel-journey-to-the-west-expanded-retelling`. This is an audit of chapter-to-manuscript coverage, playback order, source registration, narration boundaries, principal story links, and seven new manuscripts. It is **not** a scholarly variorum or a word-for-word collation against every early printing.

## Result and inventory

**All 100 selected-witness chapters are covered exactly once by 85 currently playable manuscripts.** The programmatic check maps current manuscript IDs to chapter numbers and requires that the resulting counter equal chapters 1–100 with multiplicity one for each. A complete inventory appears in the [source and playback map](journey-west-expanded-retelling-source-map.md) and the [current writer-to-maintainer handoff](journey-west-continuation-handoff.md).

| Part | Selected Chinese chapters | Playable manuscripts | Format |
| --- | --- | ---: | --- |
| Early consolidation | 1–21 | 13 | Existing consolidated chapters and natural arcs; 61 earlier writing components retained only in the archival ledger |
| Middle natural arcs | 22–45 | 17 | One manuscript per scene-complete arc, sometimes spanning adjacent chapters |
| Later chapters | 46–100 | 55 | One manuscript for each selected-witness chapter |
| **Total** | **1–100** | **85** | Continuous playable expanded retelling |

The pre-1900-literature **pack** contains **136 indexed manuscripts**, of which 85 are the expanded *Journey to the West* narrative. Other literary texts and the separate brief *Journey to the West* overview are **not** counted as part of these 85 entries. In the final seven-chapter batch, `567000`–`573000` add **15,099 spoken-section words** and **221 exact text anchors** in seven evidence sidecars. The full 85-manuscript spoken sections total **239,173 whitespace-delimited words**, including spoken headings. These are descriptive measurements, not an intended target duration or measure of fidelity.

### Descriptive count normalization

The 13 **early consolidated** manuscripts (chapters 1–21) had inherited recorded word counts from an earlier composition/counting procedure. Those counts differed from the current convention (whitespace words **inside** the spoken markers, including their headings) by 1–10 words per manuscript. During this final pass, the descriptive word-count fields for those 13 entries were normalized to the current calculation, and three listening-time entries shifted by **0.1 minutes**. Current playback tables and the README duration index were aligned. **No earlier narration, evidence sidecar, source record, or original archival component ledger was rewritten.** The historical component ledger keeps the original component-level measurements for provenance.

## Chapter-to-manuscript assignment

The current 85 entry map resolves precisely as follows; chapters listed together are narrated by the **same** playable manuscript:

- **Chapters 1–21:** `441000` (1), `442000` (2), `443000` (3), `444000` (4–5), `448000` (6–7), `452000` (8–9), `458000` (10–12), `466000` (13–14), `473000` (15–16), `480000` (17), `484000` (18), `488000` (19), `493000` (20–21).
- **Chapters 22–45:** `502000` (22), `503000` (23), `504000` (24–26), `505000` (27), `506000` (28), `507000` (29–30), `508000` (31), `509000` (32–33), `510000` (34–35), `511000` (36), `512000` (37–38), `513000` (39), `514000` (40), `515000` (41), `516000` (42), `517000` (43), `518000` (44–45).
- **Chapters 46–100:** one chapter per manuscript: `519000`–`573000`, with chapter number equal to the first three digits of the lecture ID **minus 473** (for example, `519000` = chapter 46; `573000` = chapter 100). No manuscript repeats or skips a selected chapter.

The playback collection `journey-west-expanded` refers to the **section**, not an independently maintained static list of 85 IDs; this keeps the sequence synchronized with `track.json`. The README, `navigation.json`, `track.json`, and handoff show the completed chapters **1–100**. The reader-facing chapter group guides end with [94–100](journey-west-chapters-94-100-reading-guide.md), rather than leaving an unfinished “continue” instruction.

## Concluding narrative and earlier promises

These checks are intended to catch the errors likely to be introduced at boundaries between independently authored chapter batches. They were compared against the selected Chinese chapter texts for **94–100**, and against the previously completed manuscripts and reading guides for preceding context.

| Setup or transition | Resolution / boundary | Check |
| --- | --- | --- |
| Chapter 14 introduces the tightening fillet and painful spell governing Wukong | Chapter 100: after his appointment as Victorious Fighting Buddha, Wukong asks to remove it and discovers it has **already vanished** | Retained in `573000`; not portrayed as something he physically breaks |
| Chapters 47–49 introduce Chen family child sacrifices and the **old turtle's request** to ask the Buddha about its future | Chapter 99: Xuanzang has **forgotten**, the turtle dumps them into the water, and the scriptures are damaged; the grown Chen children and their thanksgiving temple reappear | Retained in `572000`; the turtle's grievance is not excused away |
| Chapters 93–94: the true Tianzhu princess is imprisoned at Gold-Spreading Temple while a false princess directs Xuanzang's marriage | Chapter 95: **Taiyin reclaims the lunar Jade Rabbit**, and the king and queen release and recognize their **actual daughter** | Distinct characters and outcomes; no premature reveal in `567000` |
| Chapter 96: Kou Hong completes his vow by feeding the last four of 10,000 monks and offers prolonged hospitality | Chapter 97: **bandits**, not the pilgrims, kill him; recovered stolen goods support a mistaken prosecution until the host's resurrection | Retained as two causal stages; generosity does not make the pilgrims robbers |
| Chapter 98: first library allotment comprises **wordless** scrolls; then Xuanzang gives the emperor's **purple-gold bowl** and receives **5,048 written** scrolls | Chapter 99: some pages of the *Sutra of the Buddha's Life* tear on a drying stone; chapter 100: the surviving scriptures reach **Chang'an** and copying is ordered | Three distinct consequences; neither perfect scriptures nor an uneventful eastward return is invented |
| Chapter 99: the guardians carry the travelers **east** after the last ordeal | Chapter 100: Taizong receives them, then guardians bring the pilgrims **back to Spirit Mountain** for appointments | Return to Chang'an is not confused with the final appointment site |
| Chapter 100: reward for five companions | Xuanzang **Candana Merit Buddha**; Wukong **Victorious Fighting Buddha**; Bajie **Cleanser of Altars**; Sha **Golden-Bodied Arhat**; dragon-horse **Eight-Section Heavenly Dragon Horse** | Ranks are differentiated; Bajie is not incorrectly called a Buddha; horse regains dragon form |

Within the final seven chapters, the ending boundaries were checked individually: chapter 94 ends at the bee's whispered reassurance; chapter 95 ends after the princess is restored; chapter 96 precedes the fatal robbery; chapter 97 concludes the false accusation; chapter 98 concludes with written scriptures and the heavenly escort; chapter 99 includes the turtle, damaged pages and Chen family, but not the court delivery; and chapter 100 performs the delivery and final appointments. The narrative does not import chapter 100 into chapter 99 or add an unwritten postscript adventure.

## Primary-language evidence and edition limits

**Primary source for chapters 94–100:** individual chapters of the later-transmitted Chinese *Xiyou ji* available on Wikisource: [94](https://zh.wikisource.org/wiki/%E8%A5%BF%E9%81%8A%E8%A8%98/%E7%AC%AC094%E5%9B%9E), [95](https://zh.wikisource.org/wiki/%E8%A5%BF%E9%81%8A%E8%A8%98/%E7%AC%AC095%E5%9B%9E), [96](https://zh.wikisource.org/wiki/%E8%A5%BF%E9%81%8A%E8%A8%98/%E7%AC%AC096%E5%9B%9E), [97](https://zh.wikisource.org/wiki/%E8%A5%BF%E9%81%8A%E8%A8%98/%E7%AC%AC097%E5%9B%9E), [98](https://zh.wikisource.org/wiki/%E8%A5%BF%E9%81%8A%E8%A8%98/%E7%AC%AC098%E5%9B%9E), [99](https://zh.wikisource.org/wiki/%E8%A5%BF%E9%81%8A%E8%A8%98/%E7%AC%AC099%E5%9B%9E), and [100](https://zh.wikisource.org/wiki/%E8%A5%BF%E9%81%8A%E8%A8%98/%E7%AC%AC100%E5%9B%9E). All 100 chapter-specific source identifiers `cl-jtw-ch1` through `cl-jtw-ch100` are present in the pack's source registry, along with literary-context reference `cl-jtw-novel-overview`.

Every new narrative paragraph of chapters 94–100 has a traceable **exact-substring anchor in its own spoken manuscript**, classified as a **fictional narrative event** and linked to the appropriate Chinese chapter and narrated scene. Anchor matching detects editing drift; it does **not** independently prove the correctness of each adaptation against every alternative Chinese recension. The final seven chapters received a focused source review; a comprehensive source-to-manuscript claim-by-claim historical scholarship audit of all earlier 93 chapters was **not** repeated in this batch.

The selected Chinese witness is **not a photographic first-edition facsimile**. The attribution to [Wu Cheng'en](https://en.wikipedia.org/wiki/Wu_Cheng%27en) is traditional but debated. In particular, the **River Child / Chen Guangrui episode** appearing in the early `452000` adaptation is **edition-sensitive**: chapter numbering and inclusion vary across witnesses. Neither that inserted narrative nor the conventional 100-chapter numbering should be claimed to appear verbatim in every sixteenth-century copy. The historical monk [Xuanzang](https://en.wikipedia.org/wiki/Xuanzang) is not identified with the novel's supernatural plot as documentary fact. All spoken English prose is newly composed, not lifted from a modern copyrighted translation.

## Validation, scope of completion, and future maintenance

The final authoring pass checks: coverage of all 100 distinct selected-witness chapters; **85** indexed playable retelling entries with unique IDs; all 85 existing spoken marker pairs, files and sidecar links; recorded word counts and reading-duration estimates; navigation collection section membership; all seven final primary-source registrations; **221** newly created unique exact evidence anchors; no rewriting of any preexisting narration or sidecar; and preservation of all non-Journey content in the pack. A separate importer check validates the one ZIP overlay against the immediately previous chapter-93 repository state.

**Complete means:** the text manuscripts, evidence sidecars, source references, playback index, and chapter guides cover the novel through chapter 100. **It does not mean** a human listening review was conducted, TTS audio generated or aligned, or the retelling independently collated against every historical textual witness. Future work should concern editorial refinements, pronunciation/listening QA, and checking source interpretation as needed rather than drafting nonexistent chapters 101 onward.
