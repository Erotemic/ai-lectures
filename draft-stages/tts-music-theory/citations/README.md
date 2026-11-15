# Evidence map for the audio-production lessons

For lectures `025000`–`028000`, `metadata/<lecture-id>.json` now contains
`claim_evidence` records. Each record has:

- `anchor`: exact substring in the **spoken** lecture, for audit and refactoring;
- `source_ids`: bibliography keys from `metadata/sources.json`;
- `evidence_detail`: the *specific point* for which the reference is relevant,
  often including the source's document section;
- `provenance`: either sourced statement, supported interpretation, original
  derivation/calculation/example, or editorial inference.

The manuscript also includes a **display-only citation map** with direct links
and explicit explanations of what each cited authority does and does not prove.
An author example about a toy signal must not be represented as a result from
an external experiment merely because it cites a standard explaining the
underlying measurement method.

## Run

```bash
python draft-stages/tts-music-theory/citations/validate.py
python draft-stages/tts-music-theory/citations/validate.py 025000 026000 027000 028000
```

This verifies IDs, URL shape and anchor presence. It **cannot** independently
verify source credibility, quoted content, the accuracy of a reading, or whether
URLs change after publication. A substantive citation review must read each
primary source and check the relevant claim; the detailed companion maps make
that review possible.

Source order is not a quality ranking. Named ITU/EBU standards apply only to
the use cases and editions they actually cover. The original two-mix
comparison, invented impulse response, and sample calculations are authored
teaching illustrations, not claims taken from primary research.
