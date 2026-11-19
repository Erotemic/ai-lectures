#!/usr/bin/env python3
"""Compare a source migration with a pre-move catalog snapshot, without TTS.

Use --record before moving sources, then --compare after the migration. Snapshot
files are local verification artifacts, not authored content or media exports.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from ailectures.catalog import RepositoryCatalog


def encoded_bytes(value):
    result = {"bytes_sha256": hashlib.sha256(value).hexdigest()}
    try:
        result["text"] = value.decode("utf-8")
    except UnicodeDecodeError:
        pass
    return result


def snapshot(root):
    return json.loads(json.dumps(RepositoryCatalog(root).snapshot(), default=encoded_bytes))


def normalized(value):
    if isinstance(value, dict):
        if "bytes_sha256" in value and "text" in value:
            return normalized(value["text"])
        return {key: normalized(item) for key, item in value.items() if key not in {"revision", "warnings"}}
    if isinstance(value, list):
        return [normalized(item) for item in value]
    if isinstance(value, str):
        import re
        value = re.sub(r"\.\./tts-([a-z0-9-]+)(?=/)", lambda m: "../" + {"lectures": "g2", "paper": "g3"}.get(m[1], m[1]), value)
        return re.sub(r"draft-stages/tts-([a-z0-9-]+)", lambda m: "content/" + {
            "lectures": "g2", "paper": "g3"
        }.get(m[1], m[1]), value)
    return value


def compare(before, after):
    assert before.keys() == after.keys(), "Source-pack identities changed"
    totals = {"packs": len(after), "lectures": 0, "collections": 0, "companions": 0, "changed_revisions": 0}
    for namespace, old in before.items():
        new = after[namespace]
        assert old['lectures'].keys() == new['lectures'].keys(), namespace
        assert old['courses'] == new['courses'], f"Listening routes changed in {namespace}"
        assert old.get('relationships') == new.get('relationships'), namespace
        assert normalized(old.get('extra_files')) == normalized(new.get('extra_files')), f"Companion bytes changed in {namespace}"
        totals['lectures'] += len(new['lectures'])
        totals['collections'] += len(new['courses'])
        for key, row in old['lectures'].items():
            current = new['lectures'][key]
            assert row['transcript'] == current['transcript'], f"Speech changed: {key}"
            assert row['spoken_sha256'] == current['spoken_sha256'], key
            for field in ['metadata', 'sources', 'tags', 'tag_paths', 'companions', 'title', 'description', 'section', 'source']:
                assert normalized(row.get(field)) == normalized(current.get(field)), f"{field} changed: {key}"
            totals['companions'] += len(current.get('companions', []))
            totals['changed_revisions'] += row['revision'] != current['revision']
    return totals


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', type=Path, default=ROOT)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--record', type=Path)
    action.add_argument('--compare', type=Path)
    args = parser.parse_args()
    current = snapshot(args.repository)
    if args.record:
        args.record.write_text(json.dumps(current, ensure_ascii=False))
        print(f"Recorded {len(current)} packs to {args.record}")
    else:
        print(json.dumps(compare(json.loads(args.compare.read_text()), current), indent=2))


if __name__ == '__main__':
    main()
