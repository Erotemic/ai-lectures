# Review report

- run: `R-20261116-tts-world-history-13` (track `tts-world-history`, contract `prompt-v2`)
- reviewer: `qwen3.8-27b-dbirks-hyperqwen-long` (session `01a1e543-5cac-70bc-820f-5ac6878acec9`)
- adjudicator: `qwen3.8-27b-dbirks-hyperqwen-long` (session `01a1e543-5cac-70bc-820f-5ac6878acec9`)

## Findings (48 total)

### open (3)

- **007000** `missing_wiki_link` (conf=low)
  - claim: The Hōkūleʻa voyage, treated as a main subject in the lecture, lacks a Wikipedia entry point.
  - detail: The further-reading section includes Polynesian Voyaging Society and University of Hawaiʻi wayfinding pages, but no Wikipedia link; the standard entry point would be the article 'Hōkūleʻa', though I am not fully confident whether the article is titled 'Hōkūleʻa' or 'Hōkūleʻa (canoe)'.
  - anchor: “In 1976, a double-hulled voyaging canoe named Hōkūleʻa”
  - adjudication: {}
- **007000** `missing_wiki_link` (conf=high)
  - claim: The lecture's main subject, the Austronesian expansion, has no Wikipedia entry point in the further-reading section.
  - detail: The further-reading section lists academic syntheses such as Spriggs et al., Hung and Bellwood, and Kirch, but no Wikipedia link; the standard entry point would be the article 'Austronesian expansion'.
  - anchor: “The answer is called the Austronesian expansion.”
  - adjudication: {}
- **007000** `missing_wiki_link` (conf=high)
  - claim: Lapita, a major archaeological complex treated as a main subject, lacks a Wikipedia entry point.
  - detail: The further-reading section includes a Lapita handbook chapter and a dating article, but no Wikipedia link; the standard entry point would be the article 'Lapita'.
  - anchor: “It is called Lapita, after a site in New Caledonia”
  - adjudication: {}

### confirmed (4)

- **002000** `unverified_claim` (conf=high)
  - claim: The name Oldupai derives from a Maasai word for a plant found in the area.
  - detail: No registered source addresses the Maasai etymology of the place-name; a linguistic or ethnographic source on the Maasai term would be needed.
  - anchor: “The locally grounded name Oldupai comes from a Maasai word referring to a plant found in the area.”
  - adjudication: {"by": "01a1e543-5cac-70bc-820f-5ac6878acec9", "decision": "confirmed", "note": "Specific etymological claim — 'Oldupai' from a Maasai word for a plant — with no registered source reaching it; this is exactly the class of detail the category exists for. CONFIRMED, FIX DEFERRED: the fix is either (a) register a source covering the Maasai name/history of the Olduvai area (needs networked URL verification) or (b) soften the spoken sentence to 'named by the Maasai who herded there' without the plant detail (narration change -> TTS re-bill). Either needs a user decision; finding stays confirmed and active until then.", "at": "2026-11-16T19:59:33Z"}
- **003000** `unverified_claim` (conf=high)
  - claim: The lecture asserts that in the epic Gilgamesh seeks immortality and returns home.
  - detail: This plot claim about the Epic of Gilgamesh is not covered by the registered Uruk sources, which address the city and writing rather than the epic's narrative.
  - anchor: “In the epic, Gilgamesh searches for immortality and eventually returns home.”
  - adjudication: {"by": "01a1e543-5cac-70bc-820f-5ac6878acec9", "decision": "confirmed", "note": "Specific recent-history claim about a named artifact (Warka Vase stolen in the 2003 Iraq Museum looting, recovered damaged) — the fact/event-specific class this category exists for; no registered source reaches the 2003 looting or the vase's recovery (the registered smb/DAI records cover the German collection history). CONFIRMED, FIX DEFERRED: register a source on the 2003 Iraq Museum looting/recovery (networked verification; e.g. an Iraq Museum or ARCE record) or soften the sentence (TTS re-bill). User decision pending; low severity.", "at": "2026-11-16T20:55:56Z"}
- **003000** `unverified_claim` (conf=low)
  - claim: Tell Brak shows substantial urban growth during the fourth millennium and is debated in relation to southern developments.
  - detail: None of the registered sources' stated scopes cover Tell Brak or northern Mesopotamian urbanization; a source on Tell Brak or the interaction between northern and southern Mesopotamian developments would be needed.
  - anchor: “The northern site of Tell Brak, for example, shows substantial urban growth during the fourth millennium, and researchers debate how northern and southern developments interacted.”
  - adjudication: {"by": "01a1e543-5cac-70bc-820f-5ac6878acec9", "decision": "confirmed", "note": "Site-specific claim (Tell Brak's fourth-millennium urban growth) plus a live research question (north-south interaction) — the interpretation-claim class this category exists for — and no registered source covers northern Mesopotamian urbanization. CONFIRMED, FIX DEFERRED: needs either a registered source on Tell Brak / northern Uruk-period sites (networked verification) or softening the sentence (TTS re-bill). User decision pending; finding stays active.", "at": "2026-11-16T20:20:49Z"}
- **005000** `unverified_claim` (conf=high)
  - claim: The lecture asserts that Sobekneferu reigned at the end of the Twelfth Dynasty, centuries before Hatshepsut.
  - detail: No registered source covers the Twelfth Dynasty or Sobekneferu; a source on the late Middle Kingdom or on Sobekneferu specifically would be needed to support this dated, named-ruler assertion.
  - anchor: “A much earlier ruler, Sobekneferu, reigned at the end of the Twelfth Dynasty, centuries before Hatshepsut.”
  - adjudication: {"by": "01a1e543-5cac-70bc-820f-5ac6878acec9", "decision": "confirmed", "note": "Sobekneferu is invoked as a thematic precedent (a much earlier female ruler, end of the Twelfth Dynasty) — a named-ruler, dated assertion tied to the lecture's theme of women ruling as pharaoh — and no registered source covers the Twelfth Dynasty or her. CONFIRMED, FIX DEFERRED: register a source on Sobekneferu (e.g. a UCLA Encyclopedia of Egyptology entry, the same source family as the registered chronology record) or soften the sentence; networked verification needed. User decision pending; low severity.", "at": "2026-11-16T21:06:11Z"}

### resolved (23) — closed

- 001000 `missing_wiki_link`: The lecture is centrally about the Epic of Gilgamesh, establishing it as the main subject of the entire talk.
- 001000 `unverified_claim`: The lecture asserts that some of the earliest Mesopotamian writing arose for administrative accounting purpose
- 001000 `unverified_claim`: The lecture asserts that the Atrahasis flood tradition gives reasons for the flood that differ from Genesis.
- 002000 `missing_wiki_link`: Olduvai Gorge is treated as a major place in the lecture but has no Wikipedia entry point in the further-readi
- 002000 `missing_wiki_link`: The lecture's main person, Mary Leakey, has no Wikipedia entry point in the further-reading section.
- 002000 `missing_wiki_link`: The Laetoli footprints are a central subject of the lecture but the further-reading section provides no Wikipe
- 002000 `missing_wiki_link`: Mary Leakey is the central subject of the lecture.
- 003000 `missing_wiki_link`: The lecture discusses proto-cuneiform as the earliest form of writing in Uruk.
- 003000 `missing_wiki_link`: The lecture's central place, Uruk, has no Wikipedia entry point in the further-reading section.
- 003000 `missing_wiki_link`: The lecture's central subject of early writing, proto-cuneiform, has no Wikipedia entry point.
- 004000 `missing_wiki_link`: The medieval Mali Empire, a central subject of the lecture, has no Wikipedia entry point in the further-readin
- 004000 `missing_wiki_link`: The lecture treats the medieval Mali empire as a central subject.
- 004000 `missing_wiki_link`: The lecture devotes substantial discussion to Timbuktu and its built and scholarly heritage.
- 004000 `missing_wiki_link`: The lecture is centered on Mansa Musa, the fourteenth-century ruler of the Mali empire.
- 004000 `missing_wiki_link`: Sundiata Keita, the founder figure treated as a main subject in the making-of-Mali section, has no Wikipedia e
- 004000 `missing_wiki_link`: The lecture's main subject, Mansa Musa, has no Wikipedia entry point in the further-reading section.
- 005000 `missing_wiki_link`: The Punt expedition is a major subject of the lecture but lacks a Wikipedia entry point.
- 005000 `missing_wiki_link`: Hatshepsut's mortuary temple at Deir el-Bahri is a central subject but lacks a Wikipedia entry point.
- 005000 `missing_wiki_link`: The lecture's main subject, Hatshepsut, has no Wikipedia entry point in the further-reading section.
- 005000 `missing_wiki_link`: The lecture is centrally about Hatshepsut, the main subject.
- 006000 `missing_wiki_link`: The Shang dynasty, the lecture's main historical setting, has no Wikipedia entry point.
- 006000 `missing_wiki_link`: The lecture's central figure, Fu Hao, has no Wikipedia entry point in the further-reading section.
- 006000 `missing_wiki_link`: Oracle bones, a main subject of the lecture, have no Wikipedia entry point.

### rejected (18) — closed

- 001000 `unverified_claim`: The lecture asserts that written Mesopotamian flood narratives predate the final form of Genesis and that thei
- 001000 `unverified_claim`: The lecture asserts that tall cedar trees grew in mountainous regions north and west of southern Mesopotamia.
- 001000 `unverified_claim`: The lecture asserts that the transfer of Nineveh tablets to Europe occurred within imperial archaeology and ra
- 002000 `unverified_claim`: Donald Johanson and colleagues discovered the Lucy skeleton in Ethiopia in 1974.
- 002000 `unverified_claim`: Homo habilis was formally named in 1964 and proposed as a more likely tool-maker than Paranthropus boisei.
- 002000 `unverified_claim`: In 1924 Raymond Dart recognized the Taung Child fossil from South Africa as an early human relative with a sma
- 003000 `missing_wiki_link`: The named figure Gilgamesh, treated as a main subject in the lecture's later section, has no Wikipedia entry p
- 003000 `missing_wiki_link`: The lecture discusses the Epic of Gilgamesh and its opening reference to Uruk's walls.
- 003000 `unverified_claim`: The ancient name of Uruk is preserved in the biblical name Erech.
- 003000 `unverified_claim`: Habuba Kabira on the Euphrates displays strong southern Mesopotamian features and is discussed as a colony or 
- 003000 `unverified_claim`: The Epic of Gilgamesh opens by inviting its audience to inspect the walls of Uruk.
- 003000 `unverified_claim`: Later Mesopotamian mathematics used sexagesimal place-value notation.
- 003000 `unverified_claim`: The lecture asserts that the Warka Vase was stolen in the 2003 Iraq Museum looting and later recovered damaged
- 004000 `unverified_claim`: The Ghana Empire (Wagadu) accumulated power through its position in regional trade.
- 005000 `unverified_claim`: The lecture asserts that Thutmose III's campaign culminating at Megiddo belongs to the years after Hatshepsut'
- 005000 `unverified_claim`: The lecture asserts that the decipherment of hieroglyphs occurred in the nineteenth century.
- 005000 `unverified_claim`: The lecture asserts that the Second Intermediate Period included foreign rulers in the north (Hyksos) and Egyp
- 005000 `unverified_claim`: The lecture asserts that the great pyramids at Giza were built more than a thousand years before Hatshepsut.

## Unit progress

| unit | stage | findings | active | at |
|---|---|---|---|---|
| 006000 | verified | 0 | 3 | 2026-11-16T21:09:56Z |
