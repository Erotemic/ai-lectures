"""Searchable topic, place and time associations from authored metadata.

Dates retain their axis and uncertainty. Names are associations, not assertions
about modern borders, exhaustive geographic coverage, or historical influence.
No dates or places are guessed from manuscript prose, filenames or lecture IDs.
"""
from .chronology import chronology_for
from .organization import topic_tags

AXIS_LABELS = {
    "work": "Work date", "period": "Historical period", "setting": "Story setting",
    "life": "Lifetime", "witness": "Surviving witness",
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
    places = topic_tags(topic_tags(row.get('places')) + topic_tags(metadata.get('places')))
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
    # Respect the shared tag limit while returning all normalized facets as data.
    return dict(tags=topic_tags(tags + derived), places=places, periods=periods, time_coverage=time, creators=credits)
