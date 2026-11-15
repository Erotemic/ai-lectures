#!/usr/bin/env python3
"""Install an independently authored, text-only ZIP within one agent's namespace.

Preflight all paths and the merged track index *before* modifying any files.
The four agent namespaces are disjoint. This installer does not run ZIP code,
commit files, delete files, or attempt concurrent edits to a shared checkout.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import stat
from zipfile import ZipFile

OWNERS = {
    'a': 'fiction-writing',
    'b': 'comedy-history',
    'c': 'analysis',
    'd': 'music-theory',
}
TEXT_SUFFIXES = frozenset({'.md', '.json', '.txt', '.yaml', '.yml', '.tsv', '.toml', '.py', '.html'})
NUMBERED = re.compile(r'[0-9]{6}-[^/]+\.md\Z')


def apply(repo: Path, agent: str, archive: Path, check_only: bool = False) -> list[str]:
    track_id = OWNERS[agent]
    track_root = f'draft-stages/tts-{track_id}/'
    plan_root = f'docs/planning/agent-{agent}-{track_id}/'
    test_root = f'tests/agent-{agent}-{track_id}/'
    paths = []
    with ZipFile(archive) as z:
        for entry in z.infolist():
            name = entry.filename
            if entry.is_dir():
                continue
            path = PurePosixPath(name)
            if ('\\' in name or name.startswith('/') or '..' in path.parts
                    or '.' in path.parts or len(path.parts) < 3
                    or not name.startswith((track_root, plan_root, test_root))
                    or path.suffix not in TEXT_SUFFIXES
                    or '__pycache__' in path.parts):
                raise ValueError(f'Agent {agent.upper()} cannot write {name!r}')
            mode = (entry.external_attr >> 16) & 0o170000
            if mode not in (0, stat.S_IFREG):
                raise ValueError(f'Non-regular ZIP file disallowed: {name}')
            if name in paths:
                raise ValueError(f'Duplicate ZIP path: {name}')
            contents = z.read(name)
            try:
                contents.decode('utf-8')
            except UnicodeDecodeError as error:
                raise ValueError(f'ZIP payload is not UTF-8 text: {name}') from error
            if b'\x00' in contents:
                raise ValueError(f'ZIP contains binary content: {name}')
            paths.append(name)
        if not paths:
            raise ValueError('ZIP contains no owned text files')
        # The effective catalog contains on-disk files and newly added files.
        # Existing files may be updated; deletion by overlay is unsupported.
        directory = repo / track_root
        actual = {p.name for p in directory.glob('[0-9][0-9][0-9][0-9][0-9][0-9]-*.md') if p.is_file()}
        actual.update(PurePosixPath(p).name for p in paths
                      if p.startswith(track_root) and NUMBERED.fullmatch(PurePosixPath(p).name))
        manifest_name = track_root + 'track.json'
        if manifest_name in paths:
            plan = json.loads(z.read(manifest_name))
        elif (directory / 'track.json').exists():
            plan = json.loads((directory / 'track.json').read_text(encoding='utf-8'))
        else:
            plan = None
        if actual and plan is None:
            raise ValueError(f'Missing {manifest_name} for numbered manuscripts')
        if plan is not None:
            if plan.get('id') != track_id:
                raise ValueError(f'Manifest ID must equal {track_id!r}')
            rows = plan.get('lectures')
            if not isinstance(rows, list):
                raise ValueError('Manifest lectures must be a list')
            names = [row['file'] for row in rows]
            ids = [row['id'] for row in rows]
            if (len(set(names)) != len(names) or len(set(ids)) != len(ids)
                    or any(not NUMBERED.fullmatch(name) or name[:6] != row_id
                           for name, row_id in zip(names, ids))
                    or set(names) != actual):
                raise ValueError(f'{track_id} index mismatch: missing {sorted(set(names)-actual)}, '
                                 f'unindexed {sorted(actual-set(names))}')
        for name in paths:
            target = repo / name
            if target.is_symlink() or any(p.is_symlink() for p in target.parents if p != repo.parent):
                raise ValueError(f'Symlink destination disallowed: {name}')
        if not check_only:
            for name in paths:
                target = repo / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(z.read(name))
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('agent', type=str.lower, choices=OWNERS)
    parser.add_argument('zipfile', type=Path)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true', help='preflight only; change no files')
    args = parser.parse_args()
    paths = apply(args.repo.resolve(), args.agent, args.zipfile, args.check)
    print(f'{"Checked" if args.check else "Applied"} {len(paths)} owned files for agent {args.agent.upper()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
