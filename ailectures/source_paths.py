"""Canonical source-pack locations, with explicit support for older handoffs."""
from pathlib import Path, PurePosixPath


def legacy_pack_name(namespace):
    return {"g2": "tts-lectures", "g3": "tts-paper"}.get(namespace, "tts-" + namespace)


def pack_directory(repository, namespace):
    """Prefer content/<namespace>; old checkouts and fixtures remain readable."""
    root = Path(repository)
    canonical = root / "content" / namespace
    legacy = root / "draft-stages" / legacy_pack_name(namespace)
    return canonical if canonical.exists() or not legacy.exists() else legacy


def pack_directories(repository):
    root = Path(repository)
    return sorted(p for p in (root / "content").glob("*") if p.is_dir()) + sorted(
        p for p in (root / "draft-stages").glob("tts-*") if p.is_dir()
    )


def relocated_path(repository, relative):
    """Resolve an old ZIP path only after its pack has actually moved.

    Keep the payload bytes and base hashes unchanged; normal conflict checking
    still applies. Files outside known source-pack roots are never redirected.
    """
    path = PurePosixPath(relative)
    if len(path.parts) >= 2 and path.parts[0] == "draft-stages" and path.parts[1].startswith("tts-"):
        old = path.parts[1]
        namespace = {"tts-lectures": "g2", "tts-paper": "g3"}.get(old, old.removeprefix("tts-"))
        canonical = PurePosixPath("content", namespace)
        root = Path(repository)
        legacy = root / Path(*path.parts[:2])
        has_legacy_sources = (legacy / "track.json").is_file() or any(
            p.name[:6].isdigit() and p.name[6:7] == "-" for p in legacy.glob("*.md")
        )
        if not has_legacy_sources and (root / Path(*canonical.parts)).is_dir():
            return str(canonical.joinpath(*path.parts[2:]))
    return str(path)
