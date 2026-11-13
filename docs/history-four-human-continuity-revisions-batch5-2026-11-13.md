# Four operator-theory portraits: human history and narrative continuity

Updated the standalone History narrations at 010000–013000, retaining the mathematical companions and expanding historical metadata.

- **John von Neumann:** childhood education, sociability and teaching style, Ulam, Princeton, family, Klára Dán's separate computing contributions, and the personal/political complexity of wartime research.
- **Robert Schatten:** the Banach-school beginning, injury in U.S. military training, a precisely organized lecture style, his numbered-hook explanation of sequences, everyday habits, and careful handling of war losses.
- **Ky Fan:** textbook translation as an undergraduate, movement between mathematical communities during wartime, demanding teaching, and support for mathematical institutions in China.
- **Béla Szőkefalvi-Nagy:** his father's relocation from Kolozsvár, the lived Szeged mathematical culture, editorial work, and a disciplined yet approachable personality.

All additions are placed at points where they connect to mathematics, teaching, publication, or a career transition; no late biographical appendix was added. Claim anchors and resource links accompany the new biographical statements. Mathematical companions are intentionally untouched.

## Validated narrated lengths

- `010000`: 5,781 spoken words, approximately 39.9 minutes at 145 words/minute.
- `011000`: 6,196 spoken words, approximately 42.7 minutes at 145 words/minute.
- `012000`: 6,189 spoken words, approximately 42.7 minutes at 145 words/minute.
- `013000`: 6,458 spoken words, approximately 44.5 minutes at 145 words/minute.

## Verification

`pytest -q tests/test_audio_course_tracks.py tests/test_audio_lecture_library.py tests/test_course_graph.py -k "not world_history"`: 72 passed, 2 deselected. All historical anchors have source IDs present in the ledger. The four display-only mathematical companions were verified unchanged byte-for-byte. Corrected Ky Fan's birth date to 14 September 1914.
