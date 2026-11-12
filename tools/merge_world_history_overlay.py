"""Merge concurrent World History lecture contributions without replacing others.

Usage:
    python tools/merge_world_history_overlay.py --zip ~/Downloads/new-series.zip
    python tools/merge_world_history_overlay.py --bundle path/to/recovery.json

An overlay may provide new transcripts, per-lecture metadata, and roadmaps, plus
track.json and metadata/sources.json. Shared catalogs are merged by identifier;
changes to already-known identifiers and differing existing files are rejected.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from zipfile import ZipFile

WORLD_HISTORY = Path('draft-stages/tts-world-history')
TRACK_PATH = WORLD_HISTORY / 'track.json'
SOURCES_PATH = WORLD_HISTORY / 'metadata/sources.json'
TRANSCRIPT_NAME = re.compile(r'^\d{6}-[^/]+\.md$')


class MergeConflict(ValueError):
    """An existing contribution conflicts with an incoming contribution."""


def _read_world_history_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def _serialize_world_history_json(data: dict):
    return (json.dumps(data, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def _merge_track(current: dict, incoming: dict):
    if current.get('id') != 'world-history' or incoming.get('id') != 'world-history':
        raise MergeConflict('Both catalogs must identify the world-history track')
    merged = dict(current)
    merged['sections'] = list(current.get('sections', []))
    for section in incoming.get('sections', []):
        if section not in merged['sections']:
            merged['sections'].append(section)
    rows = list(current['lectures'])
    by_id = {row['id']: row for row in rows}
    if len(by_id) != len(rows):
        raise MergeConflict('Current catalog has duplicate lecture IDs')
    files = {row['file']: row['id'] for row in rows}
    if len(files) != len(rows):
        raise MergeConflict('Current catalog has duplicate lecture filenames')
    incoming_ids = set()
    for row in incoming['lectures']:
        lecture_id = row['id']
        if lecture_id in incoming_ids:
            raise MergeConflict(f'Duplicate incoming lecture ID: {lecture_id}')
        incoming_ids.add(lecture_id)
        if row['file'][:6] != lecture_id or not TRANSCRIPT_NAME.fullmatch(row['file']):
            raise MergeConflict(f'Invalid lecture filename for {lecture_id}: {row["file"]}')
        previous = by_id.get(lecture_id)
        if previous is not None:
            if previous != row:
                raise MergeConflict(f'Lecture {lecture_id} differs from an existing record')
            continue
        if row['file'] in files:
            raise MergeConflict(f'{row["file"]} already belongs to {files[row["file"]]}')
        if row.get('section') not in merged['sections']:
            raise MergeConflict(f'Undeclared section for {lecture_id}')
        rows.append(row)
        by_id[lecture_id] = row
        files[row['file']] = lecture_id
    merged['lectures'] = rows
    return merged


def _merge_sources(current: dict, incoming: dict):
    if current.get('schema_version') != incoming.get('schema_version'):
        raise MergeConflict('Source catalog schema mismatch')
    merged = dict(current)
    sources = dict(current['sources'])
    for source_id, entry in incoming['sources'].items():
        if source_id in sources and sources[source_id] != entry:
            raise MergeConflict(f'Source {source_id} conflicts with an existing record')
        sources[source_id] = entry
    merged['sources'] = sources
    return merged


def _validate_inventory(root: Path, new_files: dict[Path, bytes], track: dict, sources: dict):
    folder = root / WORLD_HISTORY
    on_disk = {p.name for p in folder.iterdir() if p.is_file() and TRANSCRIPT_NAME.fullmatch(p.name)}
    incoming = {p.name for p in new_files if p.parent == WORLD_HISTORY and TRANSCRIPT_NAME.fullmatch(p.name)}
    listed = {row['file'] for row in track['lectures']}
    if listed != on_disk | incoming:
        missing = sorted((on_disk | incoming) - listed)
        absent = sorted(listed - (on_disk | incoming))
        raise MergeConflict(f'Catalog inventory differs; unlisted={missing}, missing_files={absent}')
    lecture_ids = [row['id'] for row in track['lectures']]
    if len(lecture_ids) != len(set(lecture_ids)):
        raise MergeConflict('Duplicate lecture IDs in merged catalog')
    for row in track['lectures']:
        lecture_id = row['id']
        if row['section'] not in track['sections']:
            raise MergeConflict(f'Unknown section for {lecture_id}')
        if row['file'][:6] != lecture_id:
            raise MergeConflict(f'ID and transcript filename disagree: {lecture_id}')
        metadata_path = WORLD_HISTORY / 'metadata' / f'{lecture_id}.json'
        if metadata_path in new_files:
            metadata = json.loads(new_files[metadata_path])
        else:
            metadata = _read_world_history_json(root / metadata_path)
        if metadata['lecture_id'] != lecture_id or metadata['transcript'] != row['file']:
            raise MergeConflict(f'Metadata does not match {lecture_id}')
        for ref in metadata.get('related_resources', []):
            if ref['source_id'] not in sources['sources']:
                raise MergeConflict(f'Missing source {ref["source_id"]} in {lecture_id}')


def _plan_merge(root: Path, incoming: dict[Path, bytes], track: dict, sources: dict):
    pending = {}
    for rel, data in incoming.items():
        if rel in (TRACK_PATH, SOURCES_PATH):
            continue
        destination = root / rel
        if destination.exists():
            if not destination.is_file() or destination.read_bytes() != data:
                raise MergeConflict(f'Refusing to overwrite an existing file: {rel}')
        else:
            pending[rel] = data
    current_track = _read_world_history_json(root / TRACK_PATH)
    current_sources = _read_world_history_json(root / SOURCES_PATH)
    merged_track = _merge_track(current_track, track)
    merged_sources = _merge_sources(current_sources, sources)
    _validate_inventory(root, pending, merged_track, merged_sources)
    if merged_track != current_track:
        pending[TRACK_PATH] = _serialize_world_history_json(merged_track)
    if merged_sources != current_sources:
        pending[SOURCES_PATH] = _serialize_world_history_json(merged_sources)
    return pending


def _zip_contents(archive: Path):
    with ZipFile(archive) as zf:
        entries = {}
        for member in zf.infolist():
            if member.is_dir():
                continue
            name = PurePosixPath(member.filename)
            if (name.is_absolute() or '..' in name.parts or not name.parts
                    or stat.S_IFMT(member.external_attr >> 16) == stat.S_IFLNK):
                raise MergeConflict(f'Unsafe ZIP path: {member.filename}')
            rel = Path(*name.parts)
            if (rel.parts[:len(WORLD_HISTORY.parts)] != WORLD_HISTORY.parts
                    or rel.suffix not in {'.md', '.json'}):
                raise MergeConflict(f'ZIP contains an out-of-scope file: {rel}')
            if rel in entries:
                raise MergeConflict(f'Duplicate ZIP path: {rel}')
            entries[rel] = zf.read(member)
    if TRACK_PATH not in entries or SOURCES_PATH not in entries:
        raise MergeConflict('Lecture overlay requires both shared JSON catalog proposals')
    track = json.loads(entries[TRACK_PATH])
    sources = json.loads(entries[SOURCES_PATH])
    return entries, track, sources



@contextmanager
def _catalog_lock(root: Path):
    """Serialize catalog writers working in the same local checkout."""
    digest = hashlib.sha256(str(root.resolve()).encode('utf-8')).hexdigest()[:20]
    lock_path = Path(tempfile.gettempdir()) / f'ai-lectures-world-history-{digest}.lock'
    with lock_path.open('a+b') as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def merge_world_history_overlay(root: Path, *, archive: Path | None = None, bundle: Path | None = None,
          dry_run: bool = False):
    if (archive is None) == (bundle is None):
        raise ValueError('Pass exactly one of --zip or --bundle')
    if archive is not None:
        files, proposed_track, proposed_sources = _zip_contents(archive)
    else:
        data = _read_world_history_json(bundle)
        files = {}
        proposed_track = {'id': 'world-history', 'sections': data.get('sections', []),
                          'lectures': data['lectures']}
        proposed_sources = {'schema_version': 1, 'sources': data['sources']}
    with _catalog_lock(root):
        pending = _plan_merge(root, files, proposed_track, proposed_sources)
        for rel in sorted(pending):
            print(('Would update' if dry_run else 'Updated') + f': {rel}')
        if not dry_run:
            # Validate all changes before modifying any file. Replacement by rename
            # prevents interrupted writes of the shared JSON catalogs.
            for rel, content in pending.items():
                dest = root / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                if rel in (TRACK_PATH, SOURCES_PATH):
                    temp = dest.with_suffix(dest.suffix + '.merge-tmp')
                    temp.write_bytes(content)
                    temp.replace(dest)
                else:
                    dest.write_bytes(content)
        print(f'{len(pending)} files {"would change" if dry_run else "updated"}.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choices = parser.add_mutually_exclusive_group(required=True)
    choices.add_argument('--zip', type=Path, help='ZIP overlay proposing new lectures')
    choices.add_argument('--bundle', type=Path, help='Catalog recovery bundle of existing lectures')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        merge_world_history_overlay(args.root.resolve(), archive=args.zip, bundle=args.bundle, dry_run=args.dry_run)
    except (MergeConflict, OSError, ValueError, KeyError) as exc:
        print(f'Catalog merge refused: {exc}', file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == '__main__':
    main()
