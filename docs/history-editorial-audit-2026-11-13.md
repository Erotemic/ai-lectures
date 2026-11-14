# History track editorial audit — 13 November 2026

## Scope and results

This pass screened the spoken region of every promoted History-track lecture for repeated wording, awkward stage directions, episode references, duplicated material, weak paragraph transitions, missing section breaks, speech formatting, and metadata inconsistencies. The screening included full-corpus pattern and similarity checks, plus review and revision of selected problem passages. Mathematical companions were retained as written. This was an editorial pass rather than a new primary-source verification of the complete history corpus.

- **42 portraits**, **235,601 spoken words** after revision; all have one valid spoken start/end pair and remain above the existing substantive-length threshold.
- **28 portraits edited**; the remaining 14 were screened without a content change.
- **Opening formula**: 22 of 42 lectures originally began their first narrative paragraph with “Imagine”; after revising concrete scenarios rather than mechanically swapping synonyms, 9 still do.
- **Biography chronology**: Richard Courant's 1933 dismissal is now introduced before the paragraph discussing its personal cost, and the move to New York is placed before colleagues' retrospective description of his institute. His wartime marriages and appointments are no longer recounted twice. Frigyes Riesz's 1936 appointment rejection and his 1944 persecution are no longer told in consecutive duplicate accounts.
- **Spoken authoring instructions**: removed self-referential phrasing such as “the lecture should not invent one,” “the lecture's guiding question,” and “the earlier lectures within this portrait,” while retaining the substantive mathematical and historical qualifications.
- **Scene credibility**: the Ritz opening now describes a plate supported at its center and bowed along an edge, rather than a plate supposedly vibrating freely while resting on a table and being lifted. The Wedin opening clarifies that the tracked rigid segment is part of a lower leg.
- **Pagination and punctuation**: repaired isolated one-line paragraph joins in Hilbert, Kato, Davis, and Kahan, and six missing blank lines before section headings in Björck. The canonical pagination found no spoken sentence longer than the 600-character page limit.
- **Historical anchors**: normalized 18 claim anchors in Halmos, Wedin, Björck, Golub, and Stewart where italic Markdown had been copied into metadata although speech extraction removes it. Updated the Schatten anchor after its narrated wording changed. All **887** current claim anchors now match the extracted spoken text, and all catalog identifiers referenced by those claims and the sidecar reading lists exist among the **627** catalog entries.
- **Manifest**: recalculated spoken-word counts and estimated runtimes for every changed portrait.

The Courant marriage and war chronology was checked against the MacTutor biography and New York University special collections finding aid: https://mathshistory.st-andrews.ac.uk/Biographies/Courant/ and https://findingaids.library.nyu.edu/archives/mc_150/all/ .

## Remaining editorial candidates

1. **Longer mathematical digressions in portraits.** Davis (`018000`) includes a sustained comparison of ambient transporter norms, and Galois (`037000`) revisits quadratic field examples at several points. Both are mathematically purposeful; a listening pass would help distinguish useful reinforcement from material that could be trimmed without losing understanding.
2. **Limited personal evidence for contemporary researchers.** Yu, Wang, and Samworth (`026000`–`028000`) naturally have more research and institutional material than private correspondence or historical reminiscence. Further portrait expansion should depend on interviews, recollections, or similarly attributable material rather than biographical conjecture.
3. **Introductory rhythm.** Nine lectures still start with “Imagine,” but changing those automatically would degrade several effective mathematical openings. Future revisions can vary actual narrative structures by using a documented scene, a direct problem, a primary-source passage, or an immediate worked example.
4. **Listening-only polish.** Automatic extraction and pagination pass; audio pronunciation and pacing would benefit from targeted listening, particularly in technical names and long mathematical explanations. No audio was synthesized in this pass.

The prose audit deliberately retains historically consequential distinctions, including contested attributions, the political history of scientists, the limitations of mathematical models, and evidence gaps in ancient biographies.

## Coverage ledger

| ID | Person | Spoken words | This pass |
|---|---|---:|---|
| 001000 | James Joseph Sylvester | 5,057 | Edited |
| 002000 | Camille Jordan | 5,500 | Edited |
| 003000 | Lord Rayleigh | 5,620 | Edited |
| 004000 | Walther Ritz | 4,937 | Edited |
| 005000 | Hermann Weyl | 5,739 | Screened |
| 006000 | Richard Courant | 5,307 | Edited |
| 007000 | Ernst Sigismund Fischer | 6,488 | Edited |
| 008000 | David Hilbert | 4,689 | Edited |
| 009000 | Frigyes Riesz | 6,280 | Edited |
| 010000 | John von Neumann | 5,739 | Edited |
| 011000 | Robert Schatten | 6,194 | Edited |
| 012000 | Ky Fan | 6,173 | Edited |
| 013000 | Béla Szőkefalvi-Nagy | 6,453 | Edited |
| 014000 | Paul Halmos | 6,795 | Screened |
| 015000 | Jacques Dixmier | 6,405 | Edited |
| 016000 | Tosio Kato | 4,884 | Edited |
| 017000 | Marvin Rosenblum | 6,194 | Edited |
| 018000 | Chandler Davis | 4,690 | Edited |
| 019000 | William Kahan | 4,550 | Edited |
| 020000 | Per-Åke Wedin | 6,124 | Edited |
| 021000 | Åke Björck | 6,637 | Edited |
| 022000 | Gene H. Golub | 6,101 | Screened |
| 023000 | G. W. Stewart | 5,909 | Screened |
| 024000 | Karl Pearson | 5,941 | Edited |
| 025000 | Harold Hotelling | 6,295 | Edited |
| 026000 | Yi Yu | 4,913 | Screened |
| 027000 | Tengyao Wang | 5,146 | Screened |
| 028000 | Richard J. Samworth | 4,851 | Edited |
| 029000 | Sophie Germain | 5,321 | Edited |
| 030000 | Maryam Mirzakhani | 5,447 | Edited |
| 031000 | Carl Runge | 5,396 | Screened |
| 032000 | Martin Wilhelm Kutta | 5,066 | Edited |
| 033000 | Grace Hopper | 6,384 | Screened |
| 034000 | Ada Lovelace | 5,473 | Screened |
| 035000 | Isaac Newton | 5,006 | Edited |
| 036000 | Marie Curie | 4,818 | Edited |
| 037000 | Évariste Galois | 5,218 | Edited |
| 038000 | Kurt Gödel | 5,689 | Screened |
| 039000 | Gottfried Wilhelm Leibniz | 5,902 | Screened |
| 040000 | Pythagoras | 5,232 | Screened |
| 041000 | Joseph Fourier | 6,062 | Screened |
| 042000 | Hypatia of Alexandria | 4,976 | Screened |

## Validation

- `python -m pytest tests/test_audio_course_tracks.py -q`: **8 passed**.
- Source anchors in canonical extracted speech: **887/887 present**.
- Metadata source references: **all resolved** to the existing catalog.
- Forced splits of sentences over 600 characters: **0**.
- Unintended single-line joins between long narration paragraphs: **0**.
- Section headings joined to the preceding paragraph: **0**.
- Unchanged: mathematical display-only companions, lecture IDs, order, and the rest of the course tracks.
