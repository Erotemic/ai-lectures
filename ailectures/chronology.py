"""Optional portable dates, without inferring chronology from prose or IDs.

Years use historical numbering: negative BCE, positive CE, and no year zero.
Invalid optional records are omitted; they never prevent lecture playback.
"""


AXES = ("work", "period", "setting", "life", "witness", "composition")
MAX_YEAR = 10**12
_TEXT_LIMITS = {"label": 512, "basis": 128, "note": 8000}
_MAX_SOURCE_IDS = 512
_MAX_SOURCE_ID_LENGTH = 256


def _year(value):
    return type(value) is int and value != 0 and abs(value) <= MAX_YEAR


def _label(start, end, approximate=False):
    def number(year):
        year = abs(year)
        return f"{year:,}" if year >= 10000 else str(year)

    if start == end:
        text = f"{number(start)} {'BCE' if start < 0 else 'CE'}"
    elif end < 0:
        text = f"{number(start)}–{number(end)} BCE"
    elif start > 0:
        text = f"{number(start)}–{number(end)} CE"
    else:
        text = f"{number(start)} BCE–{number(end)} CE"
    return ("c. " if approximate else "") + text


def _text(value, limit, *, multiline=False):
    if not isinstance(value, str) or len(value) > limit:
        return None
    allowed_controls = {"\n", "\r", "\t"} if multiline else set()
    if any((ord(char) < 32 and char not in allowed_controls) or ord(char) == 127
           for char in value):
        return None
    return value.strip()


def _record(value):
    if not isinstance(value, dict):
        return None
    start, end = value.get("start"), value.get("end", value.get("start"))
    if not _year(start) or not _year(end) or start > end:
        return None
    approximate = value.get("approximate", False)
    if not isinstance(approximate, bool):
        return None
    result = dict(start=start, end=end, approximate=approximate)
    for field, limit in _TEXT_LIMITS.items():
        if field not in value:
            continue
        text = _text(value[field], limit, multiline=field == "note")
        if text is None:
            return None
        if text:
            result[field] = text
    if "source_ids" in value:
        sources = value["source_ids"]
        if not isinstance(sources, list) or len(sources) > _MAX_SOURCE_IDS:
            return None
        normalized = [_text(item, _MAX_SOURCE_ID_LENGTH) for item in sources]
        if any(not item for item in normalized):
            return None
        result["source_ids"] = list(dict.fromkeys(normalized))
    result.setdefault("label", _label(start, end, approximate))
    return result


def normalize_chronology(value):
    """Return fresh valid axis records, ignoring unknown axes and bad records.

    ``end`` defaults to ``start`` and ``approximate`` to false. Nonempty authored
    labels, basis, notes and source IDs are retained. A malformed known optional
    field invalidates that axis rather than guessing its intended confidence.
    """
    if not isinstance(value, dict):
        return {}
    value = dict(value)
    if 'setting' not in value and 'fictional_setting' in value:
        value['setting'] = value['fictional_setting']
    result = {}
    for axis in AXES:
        record = _record(value.get(axis))
        if record is not None:
            result[axis] = record
    return result


def chronology_for(row):
    """Read metadata dates plus direct canonical dates, with direct precedence.

    Precedence is per valid axis: a malformed direct record does not hide valid
    source metadata for another axis, or erase its own valid metadata fallback.
    """
    if not isinstance(row, dict):
        return {}
    metadata = row.get("metadata")
    result = normalize_chronology(metadata.get("chronology")) if isinstance(metadata, dict) else {}
    result.update(normalize_chronology(row.get("chronology")))
    return result


def _contents_record(axis, records):
    start = min(record["start"] for record in records)
    end = max(record["end"] for record in records)
    approximate = any(record["approximate"] for record in records)
    bases = list(dict.fromkeys(record.get("basis") for record in records))
    notes = list(dict.fromkeys(record["note"] for record in records if record.get("note")))
    sources = list(dict.fromkeys(source for record in records for source in record.get("source_ids", [])))
    shared_work = axis == "work" and all(
        (record["start"], record["end"], record.get("basis")) == (start, end, bases[0])
        for record in records
    )
    result = dict(start=start, end=end, approximate=approximate)
    if shared_work:
        labels = {record["label"] for record in records}
        result["label"] = next(iter(labels)) if len(labels) == 1 else _label(start, end, approximate)
        if bases[0] is not None:
            result["basis"] = bases[0]
    else:
        result["label"] = "Range of dated contents: " + _label(start, end, approximate)
        result["basis"] = "mixed" if len(bases) > 1 else "contents"
        if any(basis is not None for basis in bases):
            notes.insert(0, "Content date bases: " + "; ".join(basis or "unspecified" for basis in bases) + ".")
    if notes:
        result["note"] = "\n\n".join(notes)
        if not shared_work and len(result["note"]) > _TEXT_LIMITS["note"]:
            # A broad anthology can have thousands of words of member notes.
            # Describe the aggregation instead of truncating those qualifications
            # or making a fully dated anthology appear undated.
            result["note"] = (
                "This range spans all member dates on this axis. "
                "Member-specific qualifications remain with each lecture; "
                "consult its date notes for composition, publication and uncertainty."
            )
            if any(basis is not None for basis in bases):
                result["note"] += " Content date bases: " + "; ".join(basis or "unspecified" for basis in bases) + "."
    if sources or any("source_ids" in record for record in records):
        result["source_ids"] = sources
    # Never truncate a shared work's qualifications or source identities.
    # If those annotations exceed the schema, leave this optional axis absent.
    return _record(result)


def collection_chronology(collection, by_id):
    """Explicit dates win; otherwise require dates on every unique member.

    Derivation is independent for each axis. A missing member or date prevents
    that derived axis, without discarding explicit collection dates or other
    fully dated axes. Derived ranges describe dated contents, not the date the
    collection was created. Identical work dates/bases retain that work date.
    """
    result = chronology_for(collection)
    if not isinstance(collection, dict) or not isinstance(by_id, dict):
        return result
    members = collection.get("lectures")
    if not isinstance(members, list) or not members or any(
        not isinstance(key, str) or not key.strip() for key in members
    ):
        return result
    members = list(dict.fromkeys(members))
    if any(key not in by_id or not isinstance(by_id[key], dict) for key in members):
        return result
    dates = [chronology_for(by_id[key]) for key in members]
    for axis in AXES:
        if axis not in result and all(axis in date for date in dates):
            record = _contents_record(axis, [date[axis] for date in dates])
            if record is not None:
                result[axis] = record
    return result
