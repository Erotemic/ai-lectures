#!/usr/bin/env python3
"""Finalize the history-track ZIP overlay by moving deferred root drafts.

ZIP extraction alone does not delete the old root-level files. This idempotent
script reads the curated archive manifest and moves any remaining original
drafts and metadata into stubs/. Local revisions to the draft are retained.
"""
import json
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1] / 'draft-stages' / 'tts-history'
archive = json.loads((root / 'stubs' / 'manifest.json').read_text(encoding='utf-8'))
for row in archive['lectures']:
    source = root / row['file']
    archived = root / 'stubs' / row['file']
    if source.is_file():
        archived.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(archived))
    sidecar = root / 'metadata' / (row['id'] + '.json')
    archived_sidecar = root / 'stubs' / 'metadata' / sidecar.name
    if sidecar.is_file():
        archived_sidecar.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(sidecar), str(archived_sidecar))
    assert archived.is_file() and archived_sidecar.is_file(), row['id']
print(f"Archived {len(archive['lectures'])} deferred history drafts.")
