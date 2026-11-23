"""Deduplicated historical lecture rows, retaining legacy snapshot compatibility."""
import json

from .core import canonical, digest

SCHEMA = "shared-lecture-rows-v1"


def save_snapshot(db, release, rows):
    references = {}
    for key, row in rows.items():
        document = {field: value for field, value in row.items() if field != "origin"}
        identity = digest(document)
        db.execute("INSERT OR IGNORE INTO source_snapshot_rows VALUES (?,?)", (identity, canonical(document).decode()))
        references[key] = dict(row=identity, origin=row.get("origin"))
    db.execute("INSERT OR IGNORE INTO source_snapshots VALUES (?,?)",
               (release, canonical(dict(_schema=SCHEMA, lectures=references)).decode()))


def expand_snapshot(db, raw):
    catalog = json.loads(raw)
    if catalog.get("_schema") != SCHEMA:
        return catalog
    result = {}
    for key, reference in catalog["lectures"].items():
        stored = db.execute("SELECT document FROM source_snapshot_rows WHERE id=?", (reference["row"],)).fetchone()
        if stored is None:
            raise ValueError("Historical lecture row is missing")
        result[key] = json.loads(stored[0])
        if reference["origin"] is not None:
            result[key]["origin"] = reference["origin"]
    return result


def historical_lecture(db, release, lecture_id):
    path = "." + json.dumps(lecture_id)
    record = db.execute("""SELECT json_extract(catalog, '$._schema'),
        CASE WHEN json_extract(catalog, '$._schema')=?
        THEN json_extract(catalog, ?) ELSE json_extract(catalog, ?) END
        FROM source_snapshots WHERE release=?""",
        (SCHEMA, "$.lectures" + path, "$" + path, release)).fetchone()
    if record is None:
        return None
    if record[1] is None:
        raise KeyError(lecture_id)
    row = json.loads(record[1])
    if record[0] == SCHEMA:
        reference = row
        stored = db.execute("SELECT document FROM source_snapshot_rows WHERE id=?", (reference["row"],)).fetchone()
        if stored is None:
            raise ValueError("Historical lecture row is missing")
        row = json.loads(stored[0])
        if reference["origin"] is not None:
            row["origin"] = reference["origin"]
    return row
