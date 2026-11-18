#!/usr/bin/env python3
"""Preview or append source-grounded discovery metadata without changing speech.

Use --apply to write sidecars under the shared source lock. Existing authored
fields win. Rules use explicit titles/sections and curated work identities;
there is no extraction of arbitrary place/date mentions from narrative prose.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ailectures.descriptions import lecture_outline, short_text
from ailectures.organization import topic_tags
from ailectures.source_updates import atomic_bytes, source_lock

LITERATURE = {'literature-survey', 'pre-1900-literature', 'modern-literature'}
HISTORICAL = {'world-history', 'history', 'modern-world', 'ancient-medieval-world'}


def normalized(text):
    text = unicodedata.normalize('NFKD', text).casefold().replace('’', "'").replace('ʻ', "'").replace('ʿ', "'")
    return ''.join(c for c in text if not unicodedata.combining(c))


def propose(entry, metadata, text, namespace, rules):
    """Return additive metadata and a trace of the source fields used."""
    result = dict(metadata)
    title, section = entry.get('title', text.splitlines()[0].removeprefix('# ')), entry.get('section', '')
    evidence = []
    override = rules.get('description_overrides', {}).get(namespace + ':' + entry['id'])
    if override and 'description' not in result:
        result['description'] = override
        evidence.append('curated lecture coverage summary')
    geography = rules.get('geography_overrides', {}).get(namespace + ':' + entry['id'])
    if geography:
        if not geography.get('anchor') or geography['anchor'] not in text:
            raise ValueError(f"Geography evidence no longer matches {namespace}:{entry['id']}")
        result['places'] = topic_tags(topic_tags(result.get('places')) + geography['places'])
        evidence.append('curated geographic coverage verified against authored manuscript anchor')
    if namespace not in LITERATURE | HISTORICAL:
        return result, evidence
    geography = metadata.get('geography')
    places = topic_tags(geography.get('work_setting_or_source_context')) if isinstance(geography, dict) else []
    if places:
        evidence.append('existing authored work-setting or source-context geography')
    for place in rules['title_places']:
        if re.search(r'(?<!\w)' + re.escape(place) + r'(?!\w)', title, re.I):
            places.append(place)
    periods = [label for term, label in rules['period_terms'].items()
               if re.search(r'(?<!\w)' + re.escape(term).replace(r'\-', '[- ]') + r'(?!\w)', title + ' ' + section, re.I)]
    if places:
        result['places'] = topic_tags(topic_tags(result.get('places')) + places)
        evidence.append('places named in lecture title')
    if section_places := rules.get('section_places', {}).get(section):
        result['places'] = topic_tags(topic_tags(result.get('places')) + section_places)
        evidence.append('curated geographic association of authored literary or historical section; not a story-setting or nationality claim')
    if periods:
        result['periods'] = topic_tags(topic_tags(metadata.get('periods')) + periods)
        evidence.append('period names in title or authored section')
    if namespace in HISTORICAL - {'history'}:
        dates = re.search(r'(?<!\d)([12]\d{3})\s*[–−-]\s*([12]\d{3})(?!\d)', title)
        if dates and int(dates[1]) <= int(dates[2]):
            chronology = metadata.get('chronology', {})
            if isinstance(chronology, dict) and 'period' not in chronology:
                result['chronology'] = dict(chronology, period=dict(start=int(dates[1]), end=int(dates[2]),
                    approximate=False, basis='lecture_title', note='Explicit covered-year range in the authored lecture title; not a publication, life, or fictional-setting date.'))
                evidence.append('explicit year range in lecture title')
    if namespace in LITERATURE or 'literature' in section or section == 'world-literary-epics-and-classics':
        work = next((rule for rule in rules['works'] if re.search(r'(?<!\w)(?:' + rule['pattern'] + r')(?!\w)', title, re.I)), None)
        if work:
            result.setdefault('creators', work['creators'])
            result['places'] = topic_tags(topic_tags(result.get('places')) + work.get('places', []))
            if not result['places']:
                result.pop('places', None)
            evidence.append('curated work identity; see manuscript and reading records')
        genre_tags = [label for term, label in {'novel':'Novels', 'drama':'Drama', 'poetry':'Poetry', 'epic':'Epic', 'fable':'Fables', 'saga':'Saga', 'oral':'Oral traditions'}.items() if term in section]
        result['tags'] = topic_tags(topic_tags(metadata.get('tags')) + ['Literature'] + genre_tags + (work.get('tags', []) if work else []))
        if 'description' not in result:
            outline = lecture_outline(text)
            overview = work.get('overview', '') if work else ''
            scope = metadata.get('scope') if isinstance(metadata.get('scope'), str) else ''
            parts = [overview or title.rstrip('.') + '.']
            if scope and scope not in parts[0]:
                parts.append(scope.rstrip('.') + '.')
            if outline:
                # Preserve this installment's actual coverage; the complete
                # structured outline is separately exposed by the catalog.
                topics = outline[:3] + ([outline[-1]] if len(outline) > 3 else [])
                topics = [re.sub(r'^(?:Story|Analysis|Reading)(?:,? Part [^:]+)?:\s*', '', item.split(' — ')[-1]).strip() for item in topics]
                parts.append('Covers ' + '; '.join(topics) + '.')
            result['description'] = short_text(' '.join(parts), 600)
            evidence.append('curated work overview, authored scope, and lecture headings')
    elif namespace == 'history':
        result['tags'] = topic_tags(topic_tags(metadata.get('tags')) + ['History of science and mathematics'])
    return result, evidence


def run(repository, apply=False, only=()):
    rules = json.loads((ROOT / 'tools/data/discovery-rules.json').read_text())
    only = set(only)
    counts = Counter()
    missing_creators = []
    changes = []
    for track in sorted(list((repository / 'content').glob('*/track.json')) + list((repository / 'draft-stages').glob('tts-*/track.json'))):
        plan = json.loads(track.read_text())
        namespace = plan['id']
        if namespace not in LITERATURE | HISTORICAL and not any(key.startswith(namespace + ':') for key in [*rules.get('description_overrides', {}), *rules.get('geography_overrides', {})]):
            continue
        for entry in plan.get('lectures', []):
            if only and namespace + ':' + entry['id'] not in only:
                continue
            path = track.parent / 'metadata' / (entry['id'] + '.json')
            if not path.is_file():
                continue
            metadata = json.loads(path.read_text())
            text = (track.parent / entry['file']).read_text()
            proposed, evidence = propose(entry, metadata, text, namespace, rules)
            if namespace in LITERATURE and not proposed.get('creators'):
                missing_creators.append(f'{namespace}:{entry["id"]} {entry.get("title")}')
            if proposed == metadata:
                continue
            counts[namespace] += 1
            changes.append(dict(file=str(path.relative_to(repository)), fields=[field for field in proposed if proposed[field] != metadata.get(field)], evidence=evidence))
            if apply:
                atomic_bytes(path, (json.dumps(proposed, ensure_ascii=False, indent=2) + '\n').encode())
    return dict(changed=dict(counts), missing_creators=missing_creators, changes=changes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', type=Path, default=ROOT)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--report', type=Path)
    parser.add_argument('--lecture', action='append', default=[], help='Limit to a qualified lecture ID; repeat to select several')
    args = parser.parse_args()
    with source_lock(args.repository):
        result = run(args.repository, args.apply, args.lecture)
    if args.report:
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'changes'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
