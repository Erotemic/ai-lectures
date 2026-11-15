"""Reading records and their lecture context, independent of production."""

from .core import digest


def reference_index(lectures):
    records = {}
    for row in lectures:
        for source_id, source in row.get("sources", {}).items():
            key = (row["id"].split(":")[0], source_id, digest(source))
            entry = records.setdefault(
                key,
                dict(
                    id=source_id,
                    namespace=key[0],
                    source=source,
                    used_by=[],
                    reasons=[],
                ),
            )
            entry["used_by"].append({"id": row["id"], "title": row["title"]})
            readings = row.get("metadata", {}).get("related_resources", [])
            for reading in readings if isinstance(readings, list) else []:
                if (
                    isinstance(reading, dict)
                    and reading.get("source_id") == source_id
                    and isinstance(reading.get("reason"), str)
                    and reading["reason"] not in entry["reasons"]
                ):
                    entry["reasons"].append(reading["reason"])
    return list(records.values())
