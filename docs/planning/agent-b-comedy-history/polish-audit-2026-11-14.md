# Comedy track: source and editorial polish audit

Date: 2026-11-14. Scope: Agent B's completed `001000`–`006000` and `030500`–`049000` manuscripts (26 lectures). Historical course slots `007000`–`030000` are **not yet manuscripts** and were not examined or counted. This audit makes no assumptions about their future length.

## Methods and editorial scope

Read each manuscript's narrated sections and companions, all 26 `metadata/<id>.json` records, the track manifest, and the shared track-local bibliography. Inspected claim anchors, narration delimiters, source-key integrity and the distinction between original teaching scenes and historical testimony. Selected original publishers, academic catalogues, and research article pages were independently checked for bibliographic facts. This was **not** an exhaustive page-by-page historical source-verification exercise and not an exhaustive live URL crawl of every bibliography entry. Where a book is cited by an abstract or publisher description, the lecture should not represent that as direct engagement with the entire book.

## Corrections in this overlay

1. **Raskin date (030500, 031000):** *Semantic Mechanisms of Humor* is listed by Springer as copyright 1984, with 1984 hardcover publication. Corrected spoken mention, companion bibliography, source key, and sidecars. Source: https://link.springer.com/book/10.1007/978-94-009-6472-3
2. **Suls conflation (030500, 032000):** Previous source entry was labeled as Suls's 1972 chapter but linked to Olivier Couder's **2019** critique. It now points to the 1972 original chapter, while Couder's open article has its own record. This matters because the later article does not establish authorship of the original model. Sources: https://doi.org/10.1016/B978-0-12-288950-9.50010-9 and https://doi.org/10.1515/jls-2019-2005
3. **Hobbes (001000):** Added the primary chapter of *Leviathan* for "sudden glory," and made the spoken paraphrase match his limited and sometimes critical account. Source: https://en.wikisource.org/wiki/Leviathan_(1651)/Chapter_6
4. **Post-alternative history (036000):** Added Leon Hunt's independent chapter on cult TV and post-alternative institutions to avoid describing alternative comedy as only a change in joke technique. Source: https://doi.org/10.7228/manchester/9780719083778.003.0001
5. **Ngai (036000):** Replaced an author-profile URL with a bibliographic record for her 2012 monograph *Our Aesthetic Categories*. Source: https://books.google.com/books/about/Our_Aesthetic_Categories.html?id=Lyz3ugAACAAJ
6. **Original improv books (042000, 044000):** Distinguished Viola Spolin's 1963 first edition from the linked 1999 revised edition. Added the publisher record for *Truth in Comedy* (1994), replacing reliance on Del Close's obituary as the book's principal citation. Sources: https://nupress.northwestern.edu/9780810140080/improvisation-for-the-theater/ and https://meriwetherpublishing.com/ProductDetail.asp?id=18&pc=TRUTHINCOM
7. **Stand-up methodology (046000, 047000):** Added Paul Sturges's interview-based research on how participating working comedians described material, authenticity, and online testing. Both lectures now distinguish reported practice from a universal or experimentally established writing formula. Source: https://doi.org/10.1177/2158244015612521
8. **Lecoq publication date (048000):** Rick Kemp's article first appeared online in 2016 but was published in volume 29 (2017), and its contribution is interpretive, not a causal training experiment. Corrected bibliography and sidecar. Source: https://doi.org/10.1080/09540091.2016.1233521
9. **Reader-accessible bibliography (031000–041000):** Added curated sources-and-further-reading listings to eleven manuscripts that already had metadata references but lacked direct links in the lecture companions. The lists are **outside the spoken boundaries** and do not affect narration.
10. **Dead index item:** Removed one unreferenced commedia resource from the track-local bibliography; it was not cited by any completed lecture.

## What did not need rewriting

The manuscripts explicitly flag invented classroom vignettes, and do not claim those scenes are historical transcripts. The modern-theory sequence generally distinguishes explanatory theories, social-critical perspectives, and historical artistic movements rather than equating them. No missing manuscript entries were discovered among the 26 completed lectures; every record has its own sidecar. Length has **no target or cap**: the manifest's word counts and listening estimates are observations after editing, not quality rules.

## Deferred research and editorial opportunities

- The track's early and cross-cultural histories are bounded introductions, not source-complete histories of Sanskrit drama, noh/kyogen, rakugo/manzai, or xiangsheng; a second pass with specialist monographs and primary performances could develop further detail.
- Some cited monographs are represented by publisher descriptions or abstracts. Deeper source-specific claims would require consulting the full works, especially critical philosophy and the more historically specific improv traditions.
- A systematic live HTTP/DOI availability check across the full bibliography was not performed. Links were retained rather than replaced with unverified guessed targets.
- The reserved `007000`–`030000` historical curriculum is a content backlog, not an indexing defect.

## Verification commands

```bash
python tools/lecture_inventory.py
python -m pytest -q tests/test_audio_course_tracks.py tests/test_audio_lecture_library.py
```

The agent's pre-packaging QA additionally checks each manuscript's two marker delimiters, exact manifest order/counts, text-only contents, all sidecar anchor occurrences, all source-key references, and that changes remain inside Agent B's exclusive directories.
