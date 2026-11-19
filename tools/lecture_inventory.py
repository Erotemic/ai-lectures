#!/usr/bin/env python3
"""Audit the playable TTS corpus against its per-track manifest indexes.

Only real numbered manuscripts are counted. Packs are discovered under content/;
track.json owns their public identities and manuscript order.
"""
from __future__ import annotations

from collections import Counter
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / 'content'
LECTURE_FILE = re.compile(r'([0-9]{6})-[^/]+\.md\Z')


def main() -> int:
    extractor_path = DRAFTS / 'g2' / 'extract_narration.py'
    spec = importlib.util.spec_from_file_location('lecture_narration_extractor', extractor_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot load {extractor_path}')
    extractor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(extractor)
    problems = []
    total = 0
    discovered = 0
    ids = set()
    for folder in sorted(DRAFTS.glob('*')):
        files = {p.name for p in folder.iterdir() if p.is_file() and LECTURE_FILE.fullmatch(p.name)}
        manifest = folder / 'track.json'
        if not manifest.is_file():
            if folder.name != 'g2' and files:
                problems.append(f'{folder.name}: numbered manuscripts without track.json')
            elif folder.name == 'g2':
                for name in sorted(files):
                    try:
                        extractor.extract(folder / name)
                    except (OSError, ValueError) as error:
                        problems.append(str(error))
                total += len(files)
                discovered += 1
                print(f'g2: {len(files)} indexed transcripts (filename order)')
            continue
        discovered += 1
        plan = {}
        try:
            plan = json.loads(manifest.read_text(encoding='utf-8'))
            track_id = plan['id']
            rows = plan['lectures']
            names = [row['file'] for row in rows]
            rowids = [row['id'] for row in rows]
            assert isinstance(track_id, str)
            if track_id in ids:
                problems.append(f'{folder.name}: duplicate track ID {track_id}')
            ids.add(track_id)
            expected = track_id
            if folder.name != expected or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', track_id):
                problems.append(f'{folder.name}: invalid track ID {track_id!r}')
            if len(set(names)) != len(names) or len(set(rowids)) != len(rowids):
                problems.append(f'{folder.name}: duplicate lecture ID or filename')
            for row in rows:
                if not LECTURE_FILE.fullmatch(row['file']) or row['id'] != row['file'][:6]:
                    problems.append(f'{folder.name}: bad row {row!r}')
            for name in sorted(set(names) - files):
                problems.append(f'{folder.name}: missing indexed manuscript {name}')
            for name in sorted(files - set(names)):
                problems.append(f'{folder.name}: unindexed manuscript {name}')
            source_path = folder / 'metadata' / 'sources.json'
            sources = json.loads((source_path if source_path.exists() else
                                  DRAFTS/'g2'/'metadata'/'sources.json').read_text())['sources']
            for row in rows:
                manuscript = folder / row['file']
                if not manuscript.is_file():
                    continue
                try:
                    spoken = extractor.extract(manuscript)
                    words = len(spoken.split())
                    if 'spoken_words' in row and abs(words - row['spoken_words']) > 3:
                        problems.append(f'{folder.name}/{row["file"]}: recorded {row["spoken_words"]} words, actual {words}')
                except (OSError, ValueError) as error:
                    problems.append(str(error))
                sidecar = folder / 'metadata' / f'{row["id"]}.json'
                if not sidecar.is_file():
                    problems.append(f'{folder.name}: no sidecar for {row["id"]}')
                    continue
                meta = json.loads(sidecar.read_text())
                if meta.get('transcript') not in (None, row['file']):
                    problems.append(f'{folder.name}: wrong sidecar transcript {row["id"]}')
                refs = [r.get('source_id') for r in meta.get('related_resources', [])]
                refs += [sid for claim in meta.get('historical_claims', []) for sid in claim.get('source_ids', [])]
                for sid in refs:
                    if sid not in sources:
                        problems.append(f'{folder.name}/{row["id"]}: undefined source {sid}')
        except (OSError, ValueError, KeyError, TypeError, AssertionError) as error:
            problems.append(f'{manifest}: {error}')
        total += len(files)
        print(f'{plan.get("id", folder.name)}: {len(files)} indexed transcripts (manifest order)')
    print(f'TOTAL: {total} existing transcripts, {discovered} tracks, {len(problems)} problems')
    for item in problems:
        print('ERROR:', item)
    return 1 if problems else 0


if __name__ == '__main__':
    raise SystemExit(main())
