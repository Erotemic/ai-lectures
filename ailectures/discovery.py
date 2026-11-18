"""Searchable topic, place and time associations from authored metadata.

Dates retain their axis and uncertainty. Names are associations, not assertions
about modern borders, exhaustive geographic coverage, or historical influence.
No dates or places are guessed from manuscript prose, filenames or lecture IDs.
"""
from .chronology import chronology_for
from .organization import topic_tags
from .tagging import tag_paths, normalize_paths

AXIS_LABELS = {
    "work": "Work date", "period": "Historical period", "setting": "Story setting",
    "life": "Lifetime", "witness": "Surviving witness", "composition": "Composition date", "context": "Historical setting",
}


def _year_label(year):
    return f"{abs(year):,} {'BCE' if year < 0 else 'CE'}" if abs(year) >= 10000 else f"{abs(year)} {'BCE' if year < 0 else 'CE'}"


def date_label(record):
    start, end = record['start'], record['end']
    label = _year_label(start) if start == end else f"{_year_label(start)}–{_year_label(end)}"
    return ('c. ' if record['approximate'] else '') + label


def _century(year):
    # Consecutive indexes: -1 = first century BCE, 0 = first century CE.
    return (year - 1) // 100 if year > 0 else -((-year - 1) // 100 + 1)


def _century_label(index):
    number = index + 1 if index >= 0 else -index
    suffix = 'th' if 10 <= number % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"{number}{suffix} century {'CE' if index >= 0 else 'BCE'}"


def time_buckets(record):
    """At most eight overlapping century bins; broad ranges stay explicit.

    This bounds work for geological times and avoids pretending that a broad
    date range supplies detailed coverage of every intervening century.
    """
    first, last = _century(record['start']), _century(record['end'])
    if last - first >= 8:
        return ['Broad range: ' + date_label(record)]
    return [_century_label(index) for index in range(first, last + 1)]


def time_paths(axis, record):
    """Bounded coarse-to-fine associations, keeping the authored date meaning."""
    prefix = AXIS_LABELS[axis] + ': '
    first, last = _century(record['start']), _century(record['end'])
    paths = []
    def millennium(index):
        return _century_label(index).replace('century', 'millennium')
    if last - first >= 8:
        start, end = first // 10, last // 10
        if end - start < 8:
            paths = [[prefix + ('BCE' if index < 0 else 'CE'), prefix + millennium(index)] for index in range(start, end+1)]
        else:
            paths = [[prefix + era] for era in ('BCE', 'CE') if
                     (record['start'] < 0 if era == 'BCE' else record['end'] > 0)]
        return paths + [[prefix + date_label(record)]]
    for index in range(first, last+1):
        branch = [prefix + ('BCE' if index < 0 else 'CE'), prefix + millennium(index // 10), prefix + _century_label(index)]
        # Enumerate at most eight intersecting decades; never expand a wide
        # range into implied coverage of each individual year.
        lower = max(record['start'], index*100+1 if index >= 0 else index*100)
        upper = min(record['end'], (index+1)*100 if index >= 0 else (index+1)*100-1)
        begin = lower // 10 if lower > 0 else -((-lower-1)//10+1)
        end = upper // 10 if upper > 0 else -((-upper-1)//10+1)
        if end - begin < 8:
            for decade in range(begin, end+1):
                a, b = (max(1, decade*10), decade*10+9) if decade >= 0 else (decade*10, (decade+1)*10-1)
                leaf = branch + [prefix + _year_label(a) + '–' + _year_label(b)]
                if record['start'] == record['end']:
                    leaf += [prefix + date_label(record)]
                paths.append(leaf)
        else:
            paths.append(branch)
    return paths


CREATOR_ROLES = {'author', 'attributed_author', 'compiler', 'translator', 'oral_tradition', 'anonymous', 'storyteller'}


def creators(value):
    if not isinstance(value, list):
        return []
    result, seen = [], set()
    for item in value[:32]:
        if not isinstance(item, dict) or item.get('role', 'author') not in CREATOR_ROLES:
            continue
        if not isinstance(item.get('name'), str):
            continue
        names = topic_tags(item['name'])
        if len(names) != 1:
            continue
        role = item.get('role', 'author')
        key = (names[0].casefold(), role)
        if key in seen:
            continue
        seen.add(key)
        record = dict(name=names[0], role=role)
        if isinstance(item.get('note'), str):
            from .descriptions import short_text
            if note := short_text(item['note'], 1000):
                record['note'] = note
        result.append(record)
    return result


def discovery_fields(row):
    metadata = row.get('metadata')
    metadata = metadata if isinstance(metadata, dict) else {}
    geography = metadata.get('geography')
    associations = geography.get('work_setting_or_source_context') if isinstance(geography, dict) else []
    places = topic_tags(topic_tags(row.get('places')) + topic_tags(metadata.get('places')) + topic_tags(associations))
    periods = topic_tags(topic_tags(row.get('periods')) + topic_tags(metadata.get('periods')))
    tags = topic_tags(topic_tags(row.get('tags')) + topic_tags(metadata.get('tags')) + topic_tags(metadata.get('themes')))
    credits = creators(metadata.get('creators')) or creators(row.get('creators'))
    dates = chronology_for(row)
    time = {axis: time_buckets(record) for axis, record in dates.items()}
    derived = [f'Author: {credit["name"]}' for credit in credits if credit['role'] in {'author', 'attributed_author'}]
    derived += [f'Place: {label}' for label in places] + [f'Period: {label}' for label in periods]
    for axis, record in dates.items():
        prefix = AXIS_LABELS[axis]
        derived.append(f'{prefix}: {date_label(record)}')
        derived.extend(f'{prefix}: {label}' for label in time[axis])
    paths = tag_paths(tags, places, normalize_paths(row.get('tag_paths')) + normalize_paths(metadata.get('tag_paths')))
    paths += [path for axis, record in dates.items() for path in time_paths(axis, record)]
    # Respect the shared tag limit while returning all normalized facets as data.
    return dict(tag_paths=paths, tags=topic_tags(tags + derived + [label for path in paths for label in path]), places=places, periods=periods, time_coverage=time, creators=credits)
