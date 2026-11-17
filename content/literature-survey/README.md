# Literature: standalone introductions and narrative readings

This independently owned pack supplies standalone readings of literary works.
Some have longer studies elsewhere in the library; the new ancient narratives
are complete, source-supported readings in their own right. The introductions establish
their own characters, settings, narrative arcs, and interpretive questions.
They discuss endings. Exact episode durations are descriptive estimates, not
conditions for acceptance.

Currently indexed:

- `001000`: **The Decameron: A World Made by Telling**. The complete frame and
  selected tales explain the structure and interpretive range of the whole book.
  This is not a retelling of all one hundred tales. Extended study:
  `pre-1900-literature:decameron`.
- `002000`: **Three Kingdoms: The Price of Loyalty**. The received novel's entire
  political arc, from the oath to reunification, with historical and fictional
  evidence distinguished. Extended study: `world-history:three-kingdoms`.
- `003000`: **Shahnameh: Kings, Heroes, and the World They Lose**. The poem's
  whole arc through selected episodes, with legendary and historical modes
  distinguished. Extended study: `world-history:shahnameh`.

- `006000`: **The Aeneid: The Cost of a Promised Future**. All twelve books,
  including the fall of Troy, Dido, the underworld, the Italian war, and the last
  killing. Standalone addition to the ancient route.
- `007000`: **The Argonautica: Medea and the Voyage of the Argo**. The full
  outward voyage, quest, and return in Apollonius's four-book poem, with Medea's
  agency and the Apsyrtus episode retained.
- `008000`: **Metamorphoses: A World That Will Not Stay Still**. A connected
  traversal of all fifteen books through representative scenes, *not* every tale
  in the collection.
- `009000`: **Nala and Damayanti: The King Who Lost at Dice**. The entire embedded
  Mahabharata episode, including the second wager's ethically difficult terms.
  Companion to `world-history:024000`, which introduces the tale briefly.

- `010000`: **Gunditjmara: Budj Bim and the Living Country**. An attributed
  educational encounter with a **living** Gunditjmara creation account and the
  linked Stone Country/Sea Country landscape; includes kooyang aquaculture,
  colonisation, and water restoration. This is **not** a reproduction or an
  authorized Gunditjmara songline performance. Its claim records and cultural-IP
  boundaries are in `metadata/010000.json` and the manuscript companion.

- `011000`: **Klamath: Llao, Skell, and the Heart at Crater Lake**. A
  narrative reading of the stolen heart, its recovery, the battle with
  Llao and the Wizard Island ending, with a distinct creation account
  attributed to Perry Chocktoot and geological context. The main story
  relies on scholarly **synopses** of Robert David's Klamath-language
  record; Barker (1963) pp. 71–75 remain to be checked directly. Not an
  authorized Klamath performance. See `metadata/011000.json`.

The reader also exposes five period routes assembled from existing recordings
across packs. Those routes link to extended studies and explicitly identify
unfinished openings. Further introductory prose is optional future authoring;
organization does not depend on completing every expansion or synopsis.

The authoring boundaries and optional IDs are recorded in
[the authoring scope](notes/authoring-scope.md).
Only usable manuscripts appear in `track.json`. Source records, claim anchors,
and transcript attribution accompany each indexed lecture. The separate
`provenance.yaml` records authorship of these new texts; it does not reassign
authorship of the earlier deep dives or the primary literary works.

The reader discovers this pack without a registry edit. No synthesis or runtime
pack build is necessary to review a source addition. Run focused source checks
with `python -m pytest -q tests/test_literature_survey_pack.py`.

## Ancient epics, narrative literature, and the next written-work expansion

- `012000`: **Theogony: The Violent Birth of Order**. Hesiod's entire surviving poem traversed in narrative order, including the opening Muses, divine births, Cronus, Prometheus, the Titan war, Typhoeus and Zeus's settlement. Does not merge Pandora's jar from *Works and Days*.
- `013000`–`015000`: **Genesis, three narrative parts**. Received chapters 1–11 (creation through Babel); 12–36 (Abraham, Sarah, Hagar, Isaac, Rebekah, Esau, Jacob, Leah, Rachel, Dinah); 37–50 (Joseph, Judah and Tamar, famine, reconciliation and Joseph's coffin). Literary history and theological interpretation are distinguished from independently verified history.
- `016000`: **Oresteia: The House That Could Not Stop Killing**. All three surviving plays: *Agamemnon*, *Libation Bearers* and *Eumenides*, ending with the contested tied acquittal and Athena's accommodation of the Furies. Not an invented reconstruction of the lost *Proteus*.
- `017000`–`018000`: **The Panchatantra**, a two-part retelling of the five principal book frames and selected nested stories. The identified text is Purnabhadra's 1199 Sanskrit recension, read through Arthur Ryder's 1925 translation; this is not the lost ancient urtext.

The sixteenth-century or modern history of a work's translations is not treated as its original date. Each new lecture has independently checkable plot anchors, source locators, public-domain orientation links, and measured speech counts. The written-work queue remains open for further full narratives.

## Ancient narrative works — next full-story batch (2026-11-16)

The next four roadmap commissions are now **authored and indexed** as nine recordings, using the previous IDs and source names unchanged. Their speaking durations are measurements, not editing targets.

| IDs | Received work | Scope |
|---|---|---|
| `019000`–`020000` | *Zhuangzi* | Inner Chapters 1–7 and explicitly separate selected Outer Chapter parables; no fiction of a continuous original novel or uniformly identifiable single author. |
| `021000`–`023000` | Apuleius, *The Golden Ass* | Books I–XI; Lucius, the framed Cupid-and-Psyche tale, changing masters, and Isis/Osiris ending. Not Ovid. |
| `024000`–`026000` | *Exodus* | Received chapters 1–40; oppression and escape, wilderness and law, tabernacle plan, golden calf and renewal, completion and cloud. |
| `027000` | Kālidāsa, *Śakuntalā* | Seven-act recognition drama; kept distinct from the epic *Mahābhārata* version. |

Individual manuscripts list their primary-text/translation boundaries, public sources and Wikipedia orientation links. Claim anchors in `metadata/0xxxxx.json` point to specific received chapters, books or acts; interpretation is original narration, not a quotation of a translation. No generated audio or images are included.

## Homeric Hymns and Sophocles — full narratives (2026-11-16)

Six new original narrations follow separately transmitted Greek works rather than a fabricated single mythological novel.

- `028000`: **The Homeric Hymn to Demeter: The Season of Loss** (2,099 spoken words; 14.5 minutes at 145 wpm). Claim locators: `metadata/028000.json`.
- `029000`: **The Homeric Hymn to Apollo: The Island and the Mountain** (2,031 spoken words; 14 minutes at 145 wpm). Claim locators: `metadata/029000.json`.
- `030000`: **The Homeric Hymn to Hermes: A Newborn Thief and a New Song** (1,954 spoken words; 13.5 minutes at 145 wpm). Claim locators: `metadata/030000.json`.
- `031000`: **The Homeric Hymn to Aphrodite: The Goddess on the Mountain** (1,860 spoken words; 12.8 minutes at 145 wpm). Claim locators: `metadata/031000.json`.
- `032000`: **Sophocles, Oedipus Tyrannus: The King Who Investigated Himself** (2,694 spoken words; 18.6 minutes at 145 wpm). Claim locators: `metadata/032000.json`.
- `033000`: **Sophocles, Antigone: The Law and the Dead** (2,439 spoken words; 16.8 minutes at 145 wpm). Claim locators: `metadata/033000.json`.

The four long hymns are anonymous poems collected under a conventional Homeric label. The Delian and Pythian movements of the Apollo hymn may have distinct composition histories. Sophocles's tragedies are separately composed plays, not a single Theban trilogy; their legendary sequence need not match production chronology. Companion and source records distinguish received-story claims from historical evidence. No audio, slides or other binary media are included.

## Sumerian, Egyptian and Ugaritic narratives — source-bounded retellings (2026-11-16)

- `034000`: **Lugalbanda in the Mountain Cave: The Soldier Left Behind** (1,673 spoken words; 11.5 min at 145 wpm; 17 source checkpoints). `metadata/034000.json`.
- `035000`: **Lugalbanda and the Anzud Bird: The Gift of Speed** (1,768 spoken words; 12.2 min at 145 wpm; 18 source checkpoints). `metadata/035000.json`.
- `036000`: **The Contendings of Horus and Seth: The Trial That Would Not End** (1,832 spoken words; 12.6 min at 145 wpm; 18 source checkpoints). `metadata/036000.json`.
- `037000`: **The Report of Wenamun: The Man Who Went to Buy Timber** (1,749 spoken words; 12.1 min at 145 wpm; 19 source checkpoints). `metadata/037000.json`.
- `038000`: **Kirta: The King Who Asked for an Heir** (1,757 spoken words; 12.1 min at 145 wpm; 21 source checkpoints). `metadata/038000.json`.
- `039000`: **Aqhat: The Bow and the Unfinished Revenge** (1,693 spoken words; 11.7 min at 145 wpm; 20 source checkpoints). `metadata/039000.json`.

The two Lugalbanda poems are distinct Sumerian compositions accessed through Oxford ETCSL. Horus/Seth follows the Ramesside Papyrus Chester Beatty I, and Wenamun is limited to the surviving Papyrus Moscow 120 ending at Alashiya. Kirta (KTU 1.14–1.16) and Aqhat (KTU 1.17–1.19) are transmitted in damaged tablets: their narrative endpoints are not invented; the Ugaritic manuscripts also cite a directly viewed online column-divided English KTU rendering, supported by scholarship, while a complete modern print critical edition was not separately inspected. Primary records, source access and interpretive boundaries appear in metadata and each manuscript companion. No binary images or generated audio are included.

## Ancient works — Westcar, Enmerkar, Sāvitrī, Jātaka and Little Clay Cart (2026-11-16)

| IDs | Narrative | Spoken words / scope |
|---|---|---|
| `040000` | Westcar Papyrus: Stories at Khufu’s Court | 1,816; claim-linked source companion at `metadata/040000.json` |
| `041000` | Enmerkar and the Lord of Aratta: Seven Mountains and a Clay Message | 1,586; claim-linked source companion at `metadata/041000.json` |
| `042000` | Sāvitrī and Satyavān: The Woman Who Followed Death | 1,507; claim-linked source companion at `metadata/042000.json` |
| `043000` | Three Jātaka Tales: The Deer, the Hare, and the Promise | 1,489; claim-linked source companion at `metadata/043000.json` |
| `044000` | Vessantara: The Elephant and the Road to Exile | 1,344; claim-linked source companion at `metadata/044000.json` |
| `045000` | Vessantara: The Children and the Return | 1,519; claim-linked source companion at `metadata/045000.json` |
| `046000` | The Little Clay Cart: The Gems and the Storm | 1,673; claim-linked source companion at `metadata/046000.json` |
| `047000` | The Little Clay Cart: The Carts, the Trial, and the Rescue | 1,896; claim-linked source companion at `metadata/047000.json` |

Narration follows named received English translations, with the Westcar and Enmerkar textual gaps visible; Pāli commentarial tales carry their precise tale numbers and the ten-act Sanskrit drama is not treated as a dated historical record. Source links, version boundaries, Wikipedia orientation and claim anchors are in the non-spoken companions. No fixed duration target or generated media.

## Egyptian, Hurrian–Hittite, Akkadian and Aramaic narratives (2026-11-16)

Six new source-bounded original narrations cover four commissioned works. Their claim-level records are in `metadata/<id>.json`; none of the ancient texts is replaced by imagined gap-fill.

- `048000`: **Eloquent Peasant: The Case That Would Not End** (2,039 spoken words; 14.1 min at 145 wpm; 24 source-linked anchors).
- `049000`: **Song of Ullikummi: The Stone Raised Against the Storm** (1,808 spoken words; 12.5 min at 145 wpm; 21 source-linked anchors).
- `050000`: **Erra and Ishum: The Seven and the Empty Sanctuary** (1,535 spoken words; 10.6 min at 145 wpm; 19 source-linked anchors).
- `051000`: **Erra and Ishum: The Burning Cities and the Quieting of Wrath** (1,673 spoken words; 11.5 min at 145 wpm; 19 source-linked anchors).
- `052000`: **Ahiqar: The Nephew and the Hidden Sage** (1,765 spoken words; 12.2 min at 145 wpm; 21 source-linked anchors).
- `053000`: **Ahiqar in Later Retellings: The Sage and the Impossible Tasks** (1,851 spoken words; 12.8 min at 145 wpm; 22 source-linked anchors).

The *Ahiqar* Elephantine papyrus ends before the later Egyptian riddle contest; that later transmitted form has its own separate recording. The *Ullikummi* text is damaged, and the *Erra* tablet sequence contains interpretive ambiguities. Bibliographic records link relevant Wikipedia articles only as orientation. No generated media or binary illustrations are included.


## Geographic rotation — Greek, South Asian, Chinese, Avestan and Egyptian works (2026-11-16)

This seven-lecture batch rotates across five areas rather than staying with one literature for an entire installment. Titles are separate source-bound narratives, not claims about the historical truth of divine or supernatural events.

- `054000`: **Euripides, Medea: A House with No Safe Door** (1,822 spoken words; `metadata/054000.json`). Specific Euripidean version of Medea. Jason’s later characterization in Apollonius’s Argonautica is a separate later witness.
- `055000`: **Buddhacarita, Part One: The Prince Who Saw Suffering** (1,520 spoken words; `metadata/055000.json`). Literary devotional biography, not an independently attested royal itinerary; Sanskrit received-text layer only.
- `056000`: **Buddhacarita, Part Two: The Long Night of Awakening** (1,488 spoken words; `metadata/056000.json`). Sanskrit stops partway through canto XIV; subsequent awakening phrasing identified as later transmitted tradition, not claimed verbatim surviving Sanskrit.
- `057000`: **Buddhacarita, Part Three: The Teacher and His Last Journey** (1,618 spoken words; `metadata/057000.json`). This is a Chinese-transmitted narrative witness, not a reconstruction of missing Sanskrit verses or an independently verified biography.
- `058000`: **Li Sao: The Road Out of Chu** (1,614 spoken words; `metadata/058000.json`). The narrator’s self-description is read as poetic voice, not established autobiography; Wang Yi’s Qu Yuan reading is later interpretation.
- `059000`: **Zamyad Yasht: The Glory No King Can Own** (1,503 spoken words; `metadata/059000.json`). Narrates a hymn with episodic catalogues, not a fabricated continuous novel. Middle Persian/Shahnameh analogues not silently inserted as original Avestan text.
- `060000`: **Setne: The Book from the Tomb** (1,959 spoken words; `metadata/060000.json`). Ancient Egyptian fiction written in Ptolemaic era about a much older royal prince; missing papyrus introduction is reconstructed, not recovered.

Primary-text boundaries: Euripides lines 1–1419; *Buddhacarita* Sanskrit cantos I–XIV plus a **separately identified Chinese** continuation XV–XXVIII; full received Chinese *Li Sao* with the caution against equating narrator and documented Qu Yuan biography; Avestan *Yasht* 19 in episodic order; Demotic *Setne I* with the opening two pages lost. Source and orientation links are in each manuscript companion and source catalog. No audio or binary images are included.

## Ancient narratives eighth expansion — geographic rotation (2026-11-16)

Nine source-linked, independently understandable lectures from five areas, ordered as a geographic rotation in `navigation.json`. The Hebrew books and Greek play have complete surviving narrative arcs; the Hittite texts preserve damage and two distinct Illuyanka variants; the Chinese and Vedic selections are independent poems, not forced into a single invented story.

- `061000` **Ruth: The Road Back to Bethlehem** — 1,644 spoken words; `061000-ruth-the-road-back-to-bethlehem.md`; companion `metadata/061000.json`. Four-chapter Hebrew literary witness. Levirate redemption/land law is interpreted, not presented as an unambiguous code; threshing floor sexual action not invented.
- `062000` **Jonah: The City and the Shade** — 1,401 spoken words; `062000-jonah-the-city-and-the-shade.md`; companion `metadata/062000.json`. Great fish is not specifically named a whale; chapter 4 plant species disputed; the final theological question is intentionally unanswered.
- `063000` **Bacchae: The God at the Gate** — 1,639 spoken words; `063000-bacchae-the-god-at-the-gate.md`; companion `metadata/063000.json`. Dionysus and Pentheus are mythic characters; second messenger account and Agave recognition distinct; lacunose exodos not treated as continuous unbroken original.
- `064000` **Kumarbi: The Throne of Heaven** — 1,193 spoken words; `064000-kumarbi-the-throne-of-heaven.md`; companion `metadata/064000.json`. CTH 344 damaged after well-attested succession opening; Storm-god birth reconstruction, stone substitution and later succession are marked with their uncertainties.
- `065000` **Illuyanka: Two Ways to Defeat a Serpent** — 1,362 spoken words; `065000-illuyanka-two-ways-to-defeat-a-serpent.md`; companion `metadata/065000.json`. First version Inara, Hupasiya, banquet, house and damaged personal ending; second version heart, eyes, marriage, son killed. No merging.
- `066000` **Shijing: The Fields and the Voices** — 1,430 spoken words; `066000-shijing-the-fields-and-the-voices.md`; companion `metadata/066000.json`. Five individually numbered poems and distinct voices; received anthology and later Confucian commentary distinguished from first-performance claims.
- `067000` **Shijing: Ancestors and the Land** — 1,416 spoken words; `067000-shijing-ancestors-and-the-land.md`; companion `metadata/067000.json`. Four ritual praise poems, distinct from historical eyewitness evidence; narrative units are not fused into a fabricated continuous epic.
- `068000` **Rigveda: Urvashi and Pururavas at the Parting** — 1,167 spoken words; `068000-rigveda-urvashi-and-pururavas.md`; companion `metadata/068000.json`. Only the Vedic hymn is narrated as primary; later Brahmana and classical Sanskrit additions are identified as later, with verse-voice ambiguities acknowledged.
- `069000` **Rigveda: The Messenger and the Forbidden Proposal** — 1,268 spoken words; `069000-rigveda-sarama-yama-and-yami.md`; companion `metadata/069000.json`. No combination into one ancient myth; the first ends with the release of the cattle as invoked, and the second ends with refusal rather than an invented subsequent event.

Claim-level anchors match the extracted spoken text. Source locators identify canonical chapters, Greek lines, Hittite text catalogues and manuscript loci, numbered Shijing odes, and Rigveda hymns/verses. No generated audio or images are included.

## Major world literary gaps — first importance-first installment (2026-11-16)

The earlier queue is superseded for priority purposes by [WORLD_CLASSICS_GAP_AUDIT.md](WORLD_CLASSICS_GAP_AUDIT.md). Nine additional lecture manuscripts cover four consequential world classics, preserving explicitly named historical textual witnesses and marking early-medieval works as such. No generated audio or binary images are included.

- `070000` **Bhagavad Gita I: The Warrior Who Lowered His Bow** — 1,729 spoken words; `070000-bhagavad-gita-the-warrior-who-lowered-his-bow.md`; claim sources `metadata/070000.json`.
- `071000` **Bhagavad Gita II: The Form and the Choice** — 1,527 spoken words; `071000-bhagavad-gita-the-form-and-the-choice.md`; claim sources `metadata/071000.json`.
- `072000` **Beowulf I: The Hall and the Dark Water** — 1,635 spoken words; `072000-beowulf-the-hall-and-the-dark-water.md`; claim sources `metadata/072000.json`.
- `073000` **Beowulf II: The Dragon and the Last Fire** — 1,572 spoken words; `073000-beowulf-the-dragon-and-the-last-fire.md`; claim sources `metadata/073000.json`.
- `074000` **Thousand and One Nights I: The Woman Who Told Stories** — 1,385 spoken words; `074000-thousand-and-one-nights-the-woman-who-told-stories.md`; claim sources `metadata/074000.json`.
- `075000` **Thousand and One Nights II: The Fisherman and the Sealed Jar** — 1,476 spoken words; `075000-thousand-and-one-nights-the-fisherman-and-the-sealed-jar.md`; claim sources `metadata/075000.json`.
- `076000` **Kojiki I: The Islands and the Hidden Sun** — 1,233 spoken words; `076000-kojiki-the-islands-and-the-hidden-sun.md`; claim sources `metadata/076000.json`.
- `077000` **Kojiki II: The Hare and the Heavenly Descent** — 1,311 spoken words; `077000-kojiki-the-hare-and-the-heavenly-descent.md`; claim sources `metadata/077000.json`.
- `078000` **Kojiki III: The Road to Yamato and the White Bird** — 1,292 spoken words; `078000-kojiki-the-road-to-yamato-and-the-white-bird.md`; claim sources `metadata/078000.json`.

**Coverage labels:** Gita 1–18 and the complete received Beowulf poem; initial *Nights* selections only; selected narrative arcs from all three *Kojiki* books, not an exhaustive retelling. Medieval composition and modern translation dates never become claims about prehistoric antiquity.

Earlier integration checkpoint (17 November 2026): 76 indexed manuscripts at that stage. The 18 additions 061000–078000 preserve their source boundaries. Beowulf, the Nights selections, and Kojiki are reachable from the medieval route; the earlier received texts join the ancient-narratives route. No audio is included.

## Major world literary gaps — China, Tamil South India, Arabia (2026-11-17)

This importance-first geographic rotation adds eleven independent narrations, `079000`–`089000`, with source-linked metadata and identified textual witnesses. The navigation chapters rotate across three traditions while the two connected Xiang Yu lectures remain adjacent.

- `079000`–`082000`: **Sima Qian's *Shiji*** — four **selected** chapter-centered readings: Jing Ke (86), Xiang Yu and Liu Bang (7–8; two parts), and Lin Xiangru with Lian Po (81). This is **not** complete coverage of the *Shiji*'s 130 chapters; attributed speeches and competing reports remain literary-historical witnesses.
- `083000`–`085000`: **Tamil *Silappatikaram*** — the central story across all three books (which contain thirty episodes), from Puhar and Madhavi through Madurai and the burning of the city to Vanji and Pattini's enshrinement. This is a narrative treatment of the three-book arc, not a canto-by-canto rendering of every song and performance; literary scenes are not taken as independent proof of historical royal campaigns.
- `086000`–`089000`: **The classical seven *Mu'allaqat*** — all seven received odes, grouped for audio listening but kept textually separate: Imru al-Qays; Tarafa and Zuhayr; Labid and Antarah; Amr ibn Kulthum and al-Harith ibn Hillizah. These are independent poems, **not** a single unified epic; no performance, transcription of a contemporary translation, or factual claim that gold copies hung at the Kaaba.

The companions link relevant Wikipedia orientation and primary or named translated sources, with granular passage locators and boundaries. No fixed duration target and no generated audio or binary art are included.

Current integration checkpoint (17 November 2026): 87 indexed manuscripts; new IDs 079000–089000 add Shiji selections, the three-book Silappatikaram narrative arc, and the classical seven Muallaqat odes. Existing medieval route placement, source records and chronology are preserved.

## Medieval and mid-history literature: whole-work overviews (17 November 2026)

The new overview format distinguishes **story** (one or two complete, continuous
narrations) from **analysis** (one or two separate treatments as needed). There
is no requirement to proceed chapter by chapter; full original source chapters,
fragmented witness histories and close readings can be covered in separate deep
studies. Durations are measured descriptions, not quotas or editing targets.

Fourteen original manuscripts, `090000`–`103000`, are registered as six grouped
works and available in both the Medieval Literature route and the Compact
Introductions route:

| Work | Story ID(s) | Analysis ID | Specific boundary |
|---|---|---|---|
| *The Tale of Genji* | `090000`, `091000` | `092000` | The received 54-chapter arc including Uji and Ukifune's unresolved refusal; no invented Genji death scene. |
| *The Song of Roland* | `093000` | `094000` | The complete Oxford-text epic through Baligant, Ganelon's trial and the final summons; literary depiction of Muslims distinguished from actual Islam. |
| Four Branches of the *Mabinogi* | `095000` | `096000` | Pwyll, Branwen, Manawydan, Math as connected tales, not the full later *Mabinogion* collection. |
| *The Tale of the Heike* | `097000`, `098000` | `099000` | From Kiyomori to the Initiates' Book, including Kenreimon-in; the Kakuichi tradition is a later medieval recension of the twelfth-century events. |
| *Nibelungenlied* | `100000` | `101000` | Kriemhild's complete two-movement plot through Hagen's death and her own; medieval manuscripts differ. |
| Attar's *Conference of the Birds* | `102000` | `103000` | The complete allegorical frame, selected defining exempla, seven valleys, and the thirty-birds resolution, not all embedded anecdotes. |

Each manuscript has a non-spoken companion identifying sources, distinct
textual traditions, plot loci, interpretive boundaries and relevant Wikipedia
orientation. `metadata/<id>.json` contains recorded source identifiers and
exact spoken-text anchors. These are original paraphrases and interpretations;
no translation is reproduced, no generated audio or images are supplied, and
not all source witnesses have been collated exhaustively. The active lecture
index now contains **101** entries; their authoring scope is specific to
`content/literature-survey/`.

## Importance-first overview rotation: Vietnam and Iceland (17 November 2026)

Five authored lectures, `104000`–`108000`, continue the independent
**story/analysis** format without imposing chapter-level divisions on works.

| Work | Story narration | Separate analysis | Boundary |
|---|---|---|---|
| Nguyễn Du, *The Tale of Kiều* | `104000` (whole received 3,254-line narrative) | `105000` | Adaptation in Vietnamese lục bát, specific Nôm witness, no invented original chapters; reunion includes Kiều's choice of non-conjugal companionship |
| *Poetic Edda* | `106000` (three separate mythological poems); `107000` (selected Sigurðr and Guðrún heroic lays) | `108000` | **Selected** poetry coverage, not all Eddic poems; *Völuspá*, *Þrymskviða* and *Hávamál* kept distinct; damaged codex and divergent heroic versions identified |

The introduction route and appropriate nineteenth-century/medieval routes
register each complete lecture and maintain story-before-analysis order.
Actual speech durations, source records and claim-level anchors are saved in the
track and sidecars. All narration is original English prose; no text of a
modern copyrighted translation has been reproduced, and no audio or image
assets are bundled. The active catalog now contains **106** indexed lectures.

## Mande West Africa and early Japanese prose — importance-first overviews (17 November 2026)

| IDs | Work | Scope and source basis |
|---|---|---|
| `109000`–`110000` | *Sundiata* / *Sunjata* | One complete narrative from the **Mamadou Kouyaté / D. T. Niane** published line, followed by separate performance/history/literary analysis. Distinct jeliw performances are named and **not** assembled into a fictional urtext. The 1960 book and its English translation are copyrighted; these are original explanatory scripts, not a quotation, translated substitute, or authorized public performance. Full copyrighted edition was not collated in this pass; available attributed excerpts and source studies support the event-level overview. |
| `111000`–`112000` | *The Tale of the Bamboo Cutter* | Full prose story with **all five suitors** and outcomes, emperor, lunar envoys and Fuji ending, then a separate analysis. Japanese base witness follows named *Kokubun taikan* edition via Koten Library; modern website chapter headings are not original chapters. |

Each manuscript has a non-spoken edition/rights companion and scene-specific
claim references in `metadata/`. The two pairs are indexed and reachable from
`navigation.json` in both the medieval route and the compact overview route.
Word counts and durations are measurements, not acceptance thresholds.

## Qing China and Arabic/Persian framed narratives — next importance-first overviews (17 November 2026)

| IDs | Work | Recorded scope |
|---|---|---|
| `113000`–`115000` | Cao Xueqin / received *Dream of the Red Chamber* | Two story lectures cover the *received 120-chapter plot* (not chapter by chapter) and a separate analysis of feeling, gender, household economy, poetry, and the stone frame. The source distinction is essential: early manuscripts transmit roughly the first 80 chapters; the 1791 Cheng/ Gao print supplies the familiar final 40; its authorship is disputed. The story tells the received ending without attributing every scene to Cao. |
| `116000`–`118000` | *One Thousand and One Nights* continuing selected cycles | The Porter and the Three Ladies of Baghdad, the Three Apples through its pardon, and analysis of Shahrazad's framed narrative, source layers, Galland, Hannā Diyāb, and English translators. New story narrations use **John Payne Volume I**; the previous `074000`–`075000` retain **Burton Volume I**. *This is not complete collection coverage*. |

These six manuscripts have unique claim/scene anchors and non-spoken source
companions in `metadata/`, plus `track.json`, `navigation.json`, and
`provenance.yaml` registration. The recordings do not require listeners to
follow source chapters and they include the endings. Text only: no audio or
image media. Counts and durations are descriptive, never acceptance gates.

**Nights remaining priority cycles:** the Hunchback's Tale (including framed
barber stories), the family story of Nur al-Din Ali and Badr al-Din Hasan,
the voyages of Sindbad from an identified textual tradition, and the
Galland–Hannā Diyāb Aladdin and Ali Baba repertoires. They must be cataloged
as selected tales, not treated as a lost unified original manuscript.

## One Thousand and One Nights — Aladdin, Ali Baba, Hunchback and Sindbad (17 November 2026)

Ten authored lectures (`119000`–`128000`) add four substantial, complete-arc
Nights cycles as **story-first overviews followed by separate analysis**.

| Story | Story lectures | Analysis | Controlling narrative witness |
|---|---|---|---|
| *Aladdin* | `119000` including the false Fatima and roc egg | `120000` | Longman 1898 Galland-derived English text; Galland–Hannā Diyāb history named |
| *Ali Baba and the Forty Thieves* | `121000` including Morgiana's final rescue | `122000` | Galland-derived 1909 English witness; enslaved status and moral costs retained |
| Hunchback cycle | `123000`–`124000`, four confessors, three embedded histories, tailor and barber plus **all six brothers**, then fishbone resolution | `125000` | John Payne 1882 vol. I, with sub-stories cited individually; barber's stories originally told at tailor's dinner |
| *Sindbad the Sailor* | `126000`–`127000`, the landsman's frame and **all seven voyages** | `128000` | Laurence Housman's named 1907 retelling, with seventh-voyage alternatives signposted |

*Aladdin* and *Ali Baba* are **Galland-era additions associated with Hannā
Diyāb**, not falsely presented as recoverable medieval Arabic tales. The
Hunchback and Sindbad narratives likewise have different manuscript and print
transmission histories. Selected variants and evidence links live in
non-spoken companions and `metadata/*.json`. The earlier Nights episodes
`074000`–`075000` and `116000`–`118000` remain unchanged. This is an expanding
selection, **not the entirety of One Thousand and One Nights**.

The manuscripts are original English narration, not chapter-by-chapter
commentary and not reproductions of modern copyrighted translations. Actual
word counts and descriptive durations are recorded in `track.json`; no
fixed narration length is required. One content pack, text and metadata only,
with no audio or binary imagery. Total literature-survey catalog: **126 indexed
lectures**.


## Icelandic and Mexican fiction — a temporal and geographic rotation (17 November 2026)

Five original manuscripts are registered as whole-work overviews outside the
*One Thousand and One Nights* cycle. They follow the existing **story first,
analysis second** listening format, with source companions and paragraph-level
evidence anchors. The first two narrations of *Njáls saga* preserve Gunnar's
life and death, the foster-son's killing, the burning, law-court conflicts and
the final Flosi–Kári reconciliation; the third treats law, honor, class, gender,
Christian memory and late-medieval manuscript transmission.

| IDs | Work | Story / analysis boundary |
|---|---|---|
| `129000`–`131000` | Anonymous *Njáls saga* / *Brennu-Njáls saga* | Two story parts and one original analysis, using George Webbe Dasent's 1861 public-domain translation; no claim that late-13th-century written saga is eyewitness history of 10th–11th-century Iceland |
| `132000`–`133000` | Juan Rulfo, *Pedro Páramo* (1955) | One selective whole-work story, one analysis; preserve an unnumbered-fragment structure and the grave narrator; source evidence from Mexican literary encyclopedia and named critics, **not a full collation of the copyrighted novel** |

Both works are now available through the medieval/20th-century routes and the
Compact Introductions route. The pack contains 131 indexed lectures. These
manuscripts are original English summaries and analysis rather than verbatim
translations or copies of copyrighted texts. No audio or images are bundled.


## Oghuz heroic cycle and Portuguese Renaissance epic (17 November 2026)

Six new narrated manuscripts (`134000`–`139000`) continue the **impact-first
geographic and chronological rotation** beyond the *Nights*: Oghuz Turkic
heroic storytelling, then a sixteenth-century Portuguese maritime epic.

| Work | Story | Analysis | Textual scope |
|---|---|---|---|
| *Book of Dede Korkut* | `134000`–`135000` | `136000` | Dresden manuscript **all twelve** tales, grouped into two listener-friendly narrative sweeps without inventing a single protagonist or continuous plot. Ending includes Beyrek's death in the Inner–Outer Oghuz feud. Narratives follow the Dresden manuscript custodian's plot synopses, *not* full independent collation of the original-language witness or 1972 copyrighted English translation. |
| Camões, *The Lusiads* (*Os Lusíadas*, 1572) | `137000`–`138000` | `139000` | All ten cantos, starting on the East African coast and including the narrative flashbacks, Inês de Castro, Restelo, Adamastor, Calicut, the Island of Love, the cosmological vision and homecoming. Direct public-domain primary Portuguese text and Burton's 1880 English translation are identified. |

Claim anchors in `metadata/<id>.json` point to the corresponding numbered
Dresden tale or Camões canto. Each manuscript has a separate non-spoken text
and evidence companion with Wikipedia orientation links and explicit source
boundaries. Recorded word counts are descriptive, not length targets. Both
works are discoverable via period routes and Compact Introductions.
**The pack now contains 137 indexed lectures.** No audio or binary image assets.
