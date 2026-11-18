"""Optional browsing metadata, independent of lecture and pack identities.

Only pre-existing namespaces need these compatibility defaults. New packs supply
their own labels and need no registration here. These are browsing preferences,
not access rules or teaching prerequisites.
"""

LEGACY_CATEGORIES = {
    **dict.fromkeys(
        (
            "g1",
            "g2",
            "g3",
            "analysis",
            "numerical-analysis",
            "category-theory",
            "logic-types",
            "optimization-duality",
            "probability-measure",
        ),
        "Mathematics",
    ),
    **dict.fromkeys(
        ("history", "world-history", "world-reconsidered", "modern-world"),
        "History and society",
    ),
    **dict.fromkeys(("deep-time", "physical-world"), "Science and nature"),
    **dict.fromkeys(("music-theory", "audio-production"), "Music and sound"),
    **dict.fromkeys(
        ("modern-literature", "fiction-writing", "comedy-history"),
        "Literature and arts",
    ),
    "trades-electrical": "Practical skills",
    "bedtime-stories": "Children's Stories",
}

# Reconcile labels used by older installed releases as well as live sources.
CATEGORY_ALIASES = {
    "Literature": "Literature and arts",
    "History": "History and society",
    "History & Culture": "History and society",
    "Bedtime stories": "Children's Stories",
    "Children's Bedtime Stories": "Children's Stories",
    "Children's Bedtime Stories — Episodic": "Children's Stories",
    "Children's Bedtime Stories — Vehicles & Animals (Episodic)": "Children's Stories",
}


def categories(value):
    return list(
        dict.fromkeys(CATEGORY_ALIASES.get(label, label) for label in labels(value))
    )


def labels(value):
    if isinstance(value, str):
        value = [value]
    return (
        list(
            dict.fromkeys(
                item.strip() for item in value if isinstance(item, str) and item.strip()
            )
        )
        if isinstance(value, list)
        else []
    )


def topic_tags(value):
    """Portable descriptive topics, not prerequisite claims or access rules."""
    result, seen = [], set()
    for tag in labels(value):
        if len(tag) > 80 or any(ord(char) < 32 or ord(char) == 127 for char in tag):
            continue
        if tag.casefold() not in seen:
            seen.add(tag.casefold())
            result.append(tag)
        if len(result) == 64:
            break
    return result


def browse_sections(value, namespace):
    """A source-owned subject directory may refer to optional installed packs."""
    from .core import qualified

    if not isinstance(value, list):
        return []
    result = []
    for section in value[:32]:
        if not isinstance(section, dict) or not isinstance(section.get("title"), str):
            continue
        title = section["title"].strip()
        if not title or len(title) > 256 or not isinstance(section.get("collections"), list):
            continue
        references = []
        for reference in section["collections"][:128]:
            if not isinstance(reference, str):
                continue
            try:
                key = qualified(reference if ":" in reference else f"{namespace}:{reference}")
            except ValueError:
                continue
            if key not in references:
                references.append(key)
        if references:
            row = dict(title=title, collections=references)
            if isinstance(section.get("summary"), str):
                row["summary"] = section["summary"][:2000]
            result.append(row)
    return result


def collection_metadata(plan, namespace):
    grouping = categories(plan.get("categories", plan.get("category")))
    result = dict(
        categories=grouping or [LEGACY_CATEGORIES.get(namespace, "Other collections")],
        audiences=labels(plan.get("audiences", plan.get("audience"))),
        tags=topic_tags(plan.get("tags")),
    )
    if directory := browse_sections(plan.get("browse_sections"), namespace):
        result["browse_sections"] = directory
    if guides := categories(plan.get("guide_for")):
        result["guide_for"] = guides
    if "chronology" in plan:
        from .chronology import normalize_chronology
        if dates := normalize_chronology(plan["chronology"]):
            result["chronology"] = dates
    for field in (
        "age_range",
        "age_range_label",
        "genre",
        "series_title",
        "format",
        "sequence_recommended",
    ):
        if field in plan:
            result[field] = plan[field]
    return result


def item_organization(row, collections):
    context = [
        collection for collection in collections if row["id"] in collection["lectures"]
    ]
    # A compatibility archive can mix subjects; curated routes own browsing
    # labels once an item has been assigned to them.
    curated = [
        collection for collection in context if collection.get("role") != "archive"
    ]
    if curated:
        context = curated
    if not context:
        # Unindexed manuscripts retain categories without becoming ordered members.
        context = [
            collection
            for collection in collections
            if collection["id"].split(":")[0] == row["id"].split(":")[0]
        ]
    defaults = collection_metadata({}, row["id"].split(":")[0])
    metadata = row.get("metadata", {})
    if not isinstance(metadata, dict):
        metadata = {}
    from .discovery import discovery_fields

    return {
        **discovery_fields(row),
        "categories": categories(metadata.get("categories", metadata.get("category")))
        or list(
            dict.fromkeys(
                label
                for collection in context
                for label in collection.get("categories", [])
            )
        )
        or defaults["categories"],
        "audiences": labels(metadata.get("audiences", metadata.get("audience")))
        or list(
            dict.fromkeys(
                label
                for collection in context
                for label in collection.get("audiences", [])
            )
        ),
    }
