"""Optional image and equation placements in the lecture reader."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import os
from pathlib import Path
import re
import tempfile
import threading
from xml.etree import ElementTree

from .core import contained, file_digest, name, read_json, relative

DISPLAY_SIZES = (480, 960)
MEDIA_TYPES = {"PNG": "image/png", "JPEG": "image/jpeg", "WEBP": "image/webp"}
MATHML = "http://www.w3.org/1998/Math/MathML"
MATH_TAGS = {
    "math", "mrow", "mi", "mn", "mo", "mtext", "msub", "msup", "msubsup",
    "mfrac", "msqrt", "mroot", "munder", "mover", "munderover",
}


def equation_figure(figure):
    markup = figure["mathml"]
    if not isinstance(markup, str) or "<!" in markup:
        raise ValueError("An equation needs presentation MathML")
    try:
        equation = ElementTree.fromstring(markup)
    except ElementTree.ParseError as exc:
        raise ValueError("Invalid equation MathML") from exc
    # Packs are portable inputs. Allow only presentation nodes so their markup
    # never carries external references, embedded HTML, or active attributes.
    for node in equation.iter():
        node.tag = node.tag.removeprefix(f"{{{MATHML}}}")
        allowed_attrs = node is equation and node.attrib == {"display": "block"}
        if node.tag not in MATH_TAGS or (node.attrib and not allowed_attrs):
            raise ValueError("Unsupported MathML element or attribute")
    if equation.tag != "math" or not len(equation):
        raise ValueError("An equation needs a nonempty math element")
    equation.set("xmlns", MATHML)
    equation.set("display", "block")
    try:
        result = {"mathml": ElementTree.tostring(equation, encoding="unicode")}
    except RecursionError as exc:
        raise ValueError("Equation MathML is nested too deeply") from exc
    if isinstance(figure.get("caption"), str) and figure["caption"].strip():
        result["caption"] = figure["caption"].strip()
    return result


def transcript_placement(transcript, after):
    """Address a unique passage by the number of spoken words through its end."""
    passage = " ".join(after.split())
    if not passage:
        raise ValueError("An inline visual needs a spoken passage")
    spoken = " ".join(transcript.split())
    matches = list(re.finditer(r"(?<!\S)" + re.escape(passage) + r"(?!\S)", spoken))
    if len(matches) != 1:
        raise ValueError("An inline visual must match exactly one spoken passage")
    return len(spoken[:matches[0].end()].split())


def apply_visuals(path, lectures, courses, issue):
    if not path.is_file():
        return
    try:
        plan = read_json(path)
        sections = plan.get("sections", {})
        placements = plan.get("lectures", {})
        images = plan.get("images", {})
        equations = plan.get("equations", {})
        if not all(isinstance(part, dict) for part in (images, equations, sections, placements)):
            raise ValueError("images, equations, sections and lectures must be objects")
    except (OSError, AttributeError, TypeError, ValueError, KeyError) as exc:
        issue(f"{path.name}: {exc}")
        return

    def reference(identifier):
        image = images[name(identifier)]
        alt = image["alt"]
        if not isinstance(alt, str) or not alt.strip():
            raise ValueError("An image needs descriptive alt text")
        figure = {"path": relative(image["path"]), "alt": alt.strip()}
        if isinstance(image.get("caption"), str) and image["caption"].strip():
            figure["caption"] = image["caption"].strip()
        return figure

    covers = {}
    for section, identifier in sections.items():
        try:
            covers[section] = reference(identifier)
        except (AttributeError, TypeError, ValueError, KeyError) as exc:
            issue(f"{path.name}, section {section}: {exc}")
    for row in lectures.values():
        local_id = row["id"].split(":", 1)[1]
        cover = covers.get(row.get("section"))
        inline = []
        entry = placements.get(local_id, {})
        if not isinstance(entry, dict):
            issue(f"{path.name}, lecture {local_id}: expected a placement object")
            entry = {}
        if "cover" in entry:
            try:
                cover = reference(entry["cover"])
            except (AttributeError, TypeError, ValueError, KeyError) as exc:
                issue(f"{path.name}, lecture {local_id}: {exc}")
        entries = entry.get("inline", [])
        if not isinstance(entries, list):
            issue(f"{path.name}, lecture {local_id}: inline must be a list")
            entries = []
        for placement in entries:
            try:
                if ("image" in placement) == ("equation" in placement):
                    raise ValueError("An inline placement needs one image or equation")
                figure = (
                    equation_figure(equations[name(placement["equation"])])
                    if "equation" in placement else reference(placement["image"])
                )
                inline.append({
                    "after_word": transcript_placement(row["transcript"], placement["after"]),
                    "figure": figure,
                })
            except (AttributeError, TypeError, ValueError, KeyError) as exc:
                issue(f"{path.name}, lecture {local_id}: {exc}")
        if cover or inline:
            row["visuals"] = {
                **({"cover": cover} if cover else {}),
                **({"inline": sorted(inline, key=lambda item: item["after_word"])} if inline else {}),
            }
    for course in courses.values():
        ordered_sections = dict.fromkeys(
            lectures[key].get("section") for key in course["lectures"] if key in lectures
        )
        figures = {section: covers[section] for section in ordered_sections if section in covers}
        if figures:
            course["section_visuals"] = figures


def section_figures(course):
    entries = course.get("section_visuals", {})
    return entries if isinstance(entries, dict) else {}


def lecture_figures(row):
    entries = row.get("visuals")
    if not isinstance(entries, dict):
        return None, []
    inline = entries.get("inline")
    placements = [
        placement for placement in inline
        if isinstance(placement, dict) and type(placement.get("after_word")) is int
        and placement["after_word"] >= 0 and "figure" in placement
    ] if isinstance(inline, list) else []
    return entries.get("cover"), sorted(placements, key=lambda item: item["after_word"])


def figure_path(figure):
    if isinstance(figure, dict) and isinstance(figure.get("alt"), str):
        try:
            return relative(figure.get("path"))
        except ValueError:
            pass
    return None


def declared_figures(snapshot):
    for course in snapshot["courses"].values():
        yield from section_figures(course).values()
    for row in snapshot["lectures"].values():
        cover, placements = lecture_figures(row)
        yield cover
        for placement in placements:
            yield placement["figure"]


@lru_cache(maxsize=1)
def image_libraries():
    try:
        from PIL import Image, ImageOps, features
    except ImportError:
        return None
    return Image, ImageOps, features.check("webp")


@lru_cache(maxsize=512)
def inspect_image(path, _stamp):
    libraries = image_libraries()
    if not libraries:
        # Portable offline exports install only pure-Python dependencies.
        with path.open("rb") as stream:
            header = stream.read(24)
        if header.startswith(b"\x89PNG\r\n\x1a\n") and len(header) == 24 and header[12:16] == b"IHDR":
            width = int.from_bytes(header[16:20])
            height = int.from_bytes(header[20:24])
            return file_digest(path), "image/png", width, height, False
        if header.startswith(b"\xff\xd8\xff"):
            return file_digest(path), "image/jpeg", None, None, False
        if header.startswith(b"RIFF") and header[8:12] == b"WEBP":
            return file_digest(path), "image/webp", None, None, False
        raise ValueError("Unsupported illustration format")

    Image, _, optimized = libraries
    try:
        with Image.open(path) as image:
            media_type = MEDIA_TYPES[image.format]
            width, height = image.size
            if image.getexif().get(274, 1) in {5, 6, 7, 8}:
                width, height = height, width
    except Image.DecompressionBombError as exc:
        raise ValueError("Illustration is too large") from exc
    return file_digest(path), media_type, width, height, optimized


def image_stamp(path):
    stat = path.stat()
    return stat.st_mtime_ns, stat.st_ctime_ns, stat.st_size, stat.st_ino


@dataclass(frozen=True)
class ImageAsset:
    path: Path
    stamp: tuple[int, int, int, int]
    digest: str
    media_type: str
    width: int | None
    height: int | None
    optimized: bool


class VisualStore:
    def __init__(self, root, cache):
        self.root = Path(root)
        self.cache = Path(cache)
        self._lock = threading.Lock()
        self._generation = None
        self._paths = set()
        self._by_digest = {}

    def refresh(self, snapshot):
        """Only stat declared files. Image changes have their own catalog stamp."""
        with self._lock:
            if self._generation != snapshot["generation"]:
                self._paths = {path for figure in declared_figures(snapshot) if (path := figure_path(figure))}
                self._generation = snapshot["generation"]
            assets = {}
            for relative_path in sorted(self._paths):
                asset = self._asset(relative_path)
                if asset:
                    assets[relative_path] = asset
            self._by_digest.update((asset.digest, asset) for asset in assets.values())
            return tuple((key, item.digest, item.optimized) for key, item in assets.items())

    def _asset(self, relative_path):
        try:
            path = contained(self.root, relative_path)
            if not path.is_file():
                return None
        except (OSError, ValueError):
            return None
        try:
            stamp = image_stamp(path)
            return ImageAsset(path, stamp, *inspect_image(path, stamp))
        except (OSError, KeyError, ValueError):
            return None

    def describe(self, figure):
        if isinstance(figure, dict) and "mathml" in figure:
            try:
                return equation_figure(figure)
            except ValueError:
                return None
        relative_path = figure_path(figure)
        asset = self._asset(relative_path) if relative_path else None
        if not asset:
            return None
        width, height = asset.width, asset.height
        with self._lock:
            self._by_digest[asset.digest] = asset
        base = f"/api/library/visuals/{asset.digest}/"
        result = {
            "alt": figure["alt"],
            **({"caption": figure["caption"]} if isinstance(figure.get("caption"), str) else {}),
            "width": width,
            "height": height,
            "src": base + "original",
            "original": base + "original",
        }
        if asset.optimized:
            widths = {
                max(1, round(width * min(1, size / max(width, height)))): size
                for size in reversed(DISPLAY_SIZES)
            }
            result["src"] = base + str(DISPLAY_SIZES[0])
            result["srcset"] = ", ".join(
                f"{base}{size} {actual}w" for actual, size in sorted(widths.items())
            )
        return result

    def media(self, digest, size):
        if size not in {"original", *map(str, DISPLAY_SIZES)}:
            raise KeyError("Unknown display size")
        asset = self._by_digest.get(digest)
        if not asset:
            raise KeyError("Unknown visual")
        if image_stamp(asset.path) != asset.stamp:
            raise KeyError("Visual has changed")
        if size == "original":
            return asset.path, asset.media_type
        if not asset.optimized:
            raise KeyError("Display renditions are unavailable")
        target = self.cache / f"{digest}-{size}.webp"
        if not target.is_file():
            self._render(asset.path, asset.stamp, int(size), target)
        return target, "image/webp"

    def _render(self, path, stamp, size, target):
        Image, ImageOps, _ = image_libraries()

        self.cache.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=self.cache) as directory:
            temporary = Path(directory) / "rendition.webp"
            with Image.open(path) as original:
                image = ImageOps.exif_transpose(original)
                image = image.convert("RGBA" if "A" in image.getbands() or "transparency" in image.info else "RGB")
                image.thumbnail((size, size), Image.Resampling.LANCZOS)
                image.save(temporary, format="WEBP", quality=85)
            if image_stamp(path) != stamp:
                raise KeyError("Visual has changed")
            # Move a complete temporary rendition into the cache atomically.
            os.replace(temporary, target)
