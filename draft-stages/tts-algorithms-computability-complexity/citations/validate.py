#!/usr/bin/env python3
"""Validate mechanical source IDs and exact spoken-manuscript claim anchors.

This does not establish that a reference truly supports a claim, or that the
mathematical proof is correct. Those obligations require independent review.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN SPOKEN LECTURE -->'
END = '<!-- END SPOKEN LECTURE -->'
PROVENANCE = {
    'source_backed', 'supported_interpretation', 'original_calculation',
    'original_example', 'original_derivation', 'editorial_inference',
}


def check(ids: list[str]) -> tuple[int, int]:
    manifest = json.loads((ROOT / 'track.json').read_text(encoding='utf-8'))
    sources = json.loads((ROOT / 'metadata' / 'sources.json').read_text(encoding='utf-8'))['sources']
    rows = manifest['lectures']
    available = {row['id'] for row in rows}
    unknown = set(ids) - available
    if unknown:
        raise ValueError(f'Unknown lecture IDs: {sorted(unknown)}')
    chosen = set(ids) if ids else available
    checked = anchors = 0
    for row in rows:
        lid = row['id']
        if lid not in chosen:
            continue
        path = ROOT / row['file']
        content = path.read_text(encoding='utf-8')
        if content.count(START) != 1 or content.count(END) != 1:
            raise ValueError(f'{lid}: narration markers must occur once each')
        spoken = content.split(START, 1)[1].split(END, 1)[0]
        metadata = json.loads((ROOT / 'metadata' / f'{lid}.json').read_text(encoding='utf-8'))
        if metadata.get('lecture_id') != lid or metadata.get('transcript') != row['file']:
            raise ValueError(f'{lid}: manifest and sidecar disagree')
        for resource in metadata.get('related_resources', []):
            if resource['source_id'] not in sources:
                raise ValueError(f'{lid}: undefined related source {resource["source_id"]}')
        seen = set()
        for claim in metadata.get('claim_evidence', []):
            anchor = claim['anchor']
            if not anchor or spoken.count(anchor) != 1:
                raise ValueError(f'{lid}: expected one occurrence of spoken anchor {anchor!r}')
            if claim['id'] in seen:
                raise ValueError(f'{lid}: duplicate claim ID {claim["id"]}')
            seen.add(claim['id'])
            if claim.get('provenance') not in PROVENANCE or not claim.get('evidence_detail'):
                raise ValueError(f'{lid}: missing provenance or explanation')
            if not claim.get('source_ids') or not claim.get('source_locator'):
                raise ValueError(f'{lid}: missing source IDs or locator')
            for sid in claim['source_ids']:
                source = sources.get(sid)
                if source is None:
                    raise ValueError(f'{lid}: unknown source ID {sid}')
                url = urlsplit(source.get('url', ''))
                if url.scheme != 'https' or not url.netloc:
                    raise ValueError(f'{lid}: invalid source URL for {sid}')
            anchors += 1
        checked += 1
    return checked, anchors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ids', nargs='*', help='Lecture IDs, or omit for all indexed lectures')
    args = parser.parse_args()
    checked, anchors = check(args.ids)
    print(f'OK: {checked} lectures, {anchors} exact claim anchors, source IDs and URLs valid')
    print('Structural check only: external source interpretations are not verified.')


if __name__ == '__main__':
    main()
