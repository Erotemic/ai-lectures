#!/usr/bin/env python3
"""Check mechanical claim-to-source references for the music-theory lectures.

The validator checks exact narration anchors and repository source IDs/URLs.
It DOES NOT verify that a citation's text actually supports a claim; source
interpretation and historical correctness still require human review.
Pure standard library; no external network requests or TTS dependencies.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN SPOKEN LECTURE -->'
END = '<!-- END SPOKEN LECTURE -->'
PROVENANCE = frozenset({
    'source_backed', 'supported_interpretation', 'original_calculation',
    'original_example', 'original_derivation', 'editorial_inference',
})


def validate(root: Path = ROOT, lecture_ids: list[str] | None = None) -> tuple[int, int]:
    manifest = json.loads((root / 'track.json').read_text(encoding='utf-8'))
    source_data = json.loads((root / 'metadata' / 'sources.json').read_text(encoding='utf-8'))['sources']
    entries = manifest['lectures']
    allowed = set(lecture_ids) if lecture_ids else None
    checked, anchors = 0, 0
    for entry in entries:
        lecture_id = entry['id']
        if allowed is not None and lecture_id not in allowed:
            continue
        manuscript = root / entry['file']
        if not manuscript.is_file():
            raise ValueError(f'{lecture_id}: missing manuscript {manuscript}')
        content = manuscript.read_text(encoding='utf-8')
        if content.count(START) != 1 or content.count(END) != 1:
            raise ValueError(f'{lecture_id}: wrong count of narration markers')
        spoken = content.split(START, 1)[1].split(END, 1)[0]
        sidecar = root / 'metadata' / f'{lecture_id}.json'
        data = json.loads(sidecar.read_text(encoding='utf-8'))
        if data['lecture_id'] != lecture_id or data['transcript'] != entry['file']:
            raise ValueError(f'{lecture_id}: mismatch between manifest and sidecar')
        for res in data.get('related_resources', []):
            sid = res['source_id']
            if sid not in source_data:
                raise ValueError(f'{lecture_id}: unknown resource {sid}')
        for row in data.get('claim_evidence', []):
            anchor = row['anchor']
            if not anchor or anchor not in spoken:
                raise ValueError(f'{lecture_id}: claim anchor no longer in spoken passage: {anchor}')
            if row.get('provenance') not in PROVENANCE:
                raise ValueError(f'{lecture_id}: undefined provenance: {row.get("provenance")}')
            if not row.get('evidence_detail') or not row.get('source_ids'):
                raise ValueError(f'{lecture_id}: missing evidence explanation/source')
            for sid in row['source_ids']:
                src = source_data.get(sid)
                if src is None:
                    raise ValueError(f'{lecture_id}: undefined claim source {sid}')
                url = src.get('url', '')
                parts = urlsplit(url)
                if parts.scheme != 'https' or not parts.netloc:
                    raise ValueError(f'{lecture_id}: invalid citation URL {sid}: {url}')
            anchors += 1
        checked += 1
    if allowed is not None and {entry['id'] for entry in entries} & allowed != allowed:
        raise ValueError(f'Unknown requested lecture IDs: {allowed - {entry["id"] for entry in entries}}')
    return checked, anchors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ids', nargs='*', help='Optional lecture IDs; omit for the whole track')
    args = parser.parse_args()
    checked, anchored = validate(lecture_ids=args.ids)
    print(f'Validated citations for {checked} indexed music lectures; {anchored} exact claim anchors.')
    print('This validates reference structure, NOT the external source interpretation.')


if __name__ == '__main__':
    main()
