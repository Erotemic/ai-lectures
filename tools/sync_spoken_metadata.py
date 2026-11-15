#!/usr/bin/env python3
"""Measure narration and repair stale *descriptive* manifest fields.

No length policy is enforced. The only changes are `spoken_words` and the
corresponding `estimated_minutes_at_145_wpm` of existing lecture rows.
The script never changes transcripts, sidecars, IDs, or source records.
Run without --write to preview; opt in to changes using --write.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / 'draft-stages'


def extractor_module():
    source = DRAFTS / 'tts-lectures' / 'extract_narration.py'
    spec = importlib.util.spec_from_file_location('lecture_text_extractor', source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'No narration extractor: {source}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(tracks: list[str], write: bool) -> int:
    extract = extractor_module().extract
    changed_rows = 0
    changed_manifests = 0
    for track in tracks:
        directory = DRAFTS / ('tts-paper' if track == 'g3' else f'tts-{track}')
        manifest = directory / 'track.json'
        if not manifest.is_file():
            raise FileNotFoundError(f'No manifest for track {track}: {manifest}')
        original = manifest.read_text(encoding='utf-8')
        data = json.loads(original)
        if data['id'] != track:
            raise ValueError(f'{manifest}: wrong track id {data["id"]!r}')
        pending = []
        for row in data['lectures']:
            transcript = directory / row['file']
            if not transcript.is_file():
                raise FileNotFoundError(f'Indexed transcript missing: {transcript}')
            if not transcript.name.startswith(str(row['id']) + '-'):
                raise ValueError(f'Lecture ID/file mismatch: {transcript}')
            spoken_words = len(extract(transcript).split())
            estimated = round(spoken_words / 145, 1)
            differences = []
            for field, value in (
                ('spoken_words', spoken_words),
                ('estimated_minutes_at_145_wpm', estimated),
            ):
                if field in row and row[field] != value:
                    differences.append(f'{field}: {row[field]} -> {value}')
                    row[field] = value
            if differences:
                pending.append((row['id'], differences))
        if pending:
            for lecture_id, differences in pending:
                print(f'{track}:{lecture_id}: {", ".join(differences)}')
            changed_rows += len(pending)
            changed_manifests += 1
            if write:
                manifest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    status = 'Wrote' if write else 'Would update'
    print(f'{status} {changed_rows} lecture row(s) in {changed_manifests} manifest(s)')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tracks', nargs='+', default=None,
                        help='Track IDs to inspect (default: every manifest track)')
    parser.add_argument('--write', action='store_true',
                        help='write repaired manifests (otherwise report only)')
    args = parser.parse_args()
    if args.tracks is None:
        args.tracks = sorted(json.loads(p.read_text(encoding='utf-8'))['id']
                             for p in DRAFTS.glob('tts-*/track.json'))
    return run(args.tracks, args.write)


if __name__ == '__main__':
    raise SystemExit(main())
