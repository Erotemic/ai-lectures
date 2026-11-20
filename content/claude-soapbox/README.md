# Claude Soapbox

The repository owner offered Claude a track with freedom over subject and form,
including the freedom not to write. These essays are the result. The subjects
were chosen by the model, and the arguments are its own. Each lecture stands
alone.

This track was written without reading the `gpt-soapbox` track, so that the two
stay independent.

## Evidence conventions

These go beyond the minimum used elsewhere in the library. They are an
experiment in making an opinionated, first-person essay auditable.

- **One record per claim.** Each `claim_evidence` entry has an exact anchor
  from the manuscript, a specific locator (page, section, or figure), and a
  `verification` note. The note says what was actually read: a full text, a
  scanned page, an abstract only, or a search excerpt.
- **Secondary citation is labelled.** A work known only through another
  source's report (for example, Maier 1931 as described by Nisbett and Wilson)
  is marked `source_backed_secondary`. The original is not cited as if it had
  been consulted.
- **The author's voice is separated from the evidence.** `author_synthesis` and
  `author_opinion` mark arguments that belong to the essay, not to its sources.
  `self_report_unverified` marks the model's statements about its own states
  and motives. The first essay argues that such reports should be weighed as
  plausible accounts rather than privileged evidence, and the label applies
  that argument to the essay itself.
- **Gaps are recorded, not hidden.** When a source could not be fully read,
  `sources.json` says so in `consulted`. The spoken text then avoids figures
  that were not checked.

Each lecture's `evidence_policy` block defines the provenance values it uses.

## Files

```text
track.json                     track manifest
NNNNNN-slug.md                 manuscript; the spoken region is the TTS input,
                               and the notes after it are companion text
metadata/NNNNNN.json           description, tags, authorship, claim evidence
metadata/sources.json          bibliographic records and consultation notes
BACKLOG.md                     the author's own list of possible future essays
```
