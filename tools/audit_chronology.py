#!/usr/bin/env python3
"""Report date metadata coverage in indexed source tracks, without altering speech.

Unknown dates are gaps in metadata, not proof that a subject lacks a setting.
Use --output to save the full list for editorial follow-up. Narrative settings,
composition, publication, historical coverage and manuscripts remain separate.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ailectures.chronology import AXES, chronology_for


def audit(repository):
    rows = {}
    tracks = sorted(list((repository / 'content').glob('*/track.json')) +
                    list((repository / 'draft-stages').glob('tts-*/track.json')))
    for path in tracks:
        plan = json.loads(path.read_text())
        for entry in plan.get('lectures', []):
            key = plan['id'] + ':' + entry['id']
            sidecar = path.parent / 'metadata' / (entry['id'] + '.json')
            metadata = json.loads(sidecar.read_text()) if sidecar.exists() else {}
            row = dict(entry, metadata=metadata)
            dates = chronology_for(row)
            rows[key] = dict(id=key, title=entry.get('title', entry['id']),
                namespace=plan['id'], metadata=str(sidecar.relative_to(repository)),
                dated_axes=list(dates), missing_axes=[axis for axis in AXES if axis not in dates])
    packs = []
    for namespace in sorted({row['namespace'] for row in rows.values()}):
        members = [row for row in rows.values() if row['namespace'] == namespace]
        counts = Counter(axis for row in members for axis in row['dated_axes'])
        packs.append(dict(namespace=namespace, lectures=len(members), dated=dict(counts)))
    counts = Counter(axis for row in rows.values() for axis in row['dated_axes'])
    return dict(scope='Indexed source tracks; optional dates may be unknown or inapplicable.',
                lectures=len(rows), dated=dict(counts), packs=packs, items=list(rows.values()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = audit(args.repository)
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key != 'items'}, indent=2))


if __name__ == '__main__':
    main()
