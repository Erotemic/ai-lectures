"""Compile a frozen local voice profile and process saved audio once per page."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import tempfile

from .voice_profiles import PIPELINE
from .narration import TITLE_POLICY


def compile_recipe(profile, backend):
    recipe = profile["recipe"]
    from dkvis.presentation.audio_quality import VERSION

    if (
        recipe["processing"].get("enabled")
        and recipe.get("processing_version", VERSION) != VERSION
    ):
        raise ValueError(
            "Audio processing implementation changed; save a new profile revision"
        )
    if recipe["pipeline"] != PIPELINE or recipe["title_policy"] != TITLE_POLICY:
        raise ValueError(
            "Rendering implementation changed; save a new profile revision"
        )
    if not backend.get("available") or recipe["config"]["model"] != backend["model"]:
        raise ValueError("The saved profile backend/model is unavailable")
    config = deepcopy(recipe["config"])
    config.update(
        endpoint=backend["endpoint"],
        reader_frozen=True,
        reader_profile_revision=profile["revision"],
        reader_cache_backend=backend["id"],
        reader_long_form=recipe["body_mode"] == "paragraph",
        reader_segment_chars=recipe["reader"]["segment_chars"],
        reader_segment_words=recipe["reader"]["segment_words"],
        reader_segment_seconds=recipe["reader"]["segment_seconds"],
        title_instruction_field=recipe["title_instruction_field"] or "none",
        title_instruction=recipe["title_instruction"],
        title_cfg_scale=recipe["title_cfg_scale"],
        title_pause_before_seconds=recipe["title_pause_before"],
        title_pause_after_seconds=recipe["title_pause_after"],
    )
    cap = recipe["capabilities"]
    if cap != backend["capabilities"]:
        raise ValueError("Backend capabilities changed; save a new profile revision")
    # The engine's legacy speed parameter controls Kokoro natively. Other
    # declared native-rate adapters receive an explicit request field.
    speed = recipe["native_rate"] if cap["adapter"] == "kokoro" else 1.0
    if cap["native_rate"] and cap["adapter"] != "kokoro":
        config.setdefault("request", {})[cap["native_rate_field"]] = (
            1 / recipe["native_rate"]
            if cap["native_rate_field"] == "duration_factor"
            else recipe["native_rate"]
        )
    return dict(profile=profile["id"], profiles={profile["id"]: config}), speed


def page_processor(recipe):
    if recipe["tempo"] == 1 and not recipe["processing"].get("enabled"):
        return None

    def process(path, output_format, task):
        from dkvis.presentation.media import duration
        from dkvis.presentation.audio_quality import process_chunk

        path = Path(path)
        before = duration(path)
        timing_path = path.with_name(path.name + ".timings.json")
        with tempfile.TemporaryDirectory(
            prefix=".voice-processing-", dir=path.parent
        ) as directory:
            source = process_chunk(path, Path(directory), recipe["processing"])
            target = Path(directory) / ("processed." + output_format)
            command = [
                "ffmpeg",
                "-nostdin",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(source),
                "-vn",
            ]
            if recipe["tempo"] != 1:
                command += ["-af", f"atempo={recipe['tempo']:g}"]
            command += (
                [
                    "-codec:a",
                    "libopus",
                    "-b:a",
                    "96k",
                    "-vbr",
                    "on",
                    "-application",
                    "audio",
                    "-f",
                    "ogg",
                ]
                if output_format == "ogg"
                else ["-codec:a", "libmp3lame", "-q:a", "3", "-f", "mp3"]
            )
            task.check_cancelled()
            subprocess.run(
                command + [str(target)], check=True, capture_output=True, timeout=180
            )
            after = duration(target)
            if abs(after - before / recipe["tempo"]) > max(0.15, before * 0.02):
                raise ValueError("Postprocessing changed the expected audio duration")
            if timing_path.is_file():
                timing = json.loads(timing_path.read_text())
                scale = after / before
                timing["duration"] = after
                for item in timing.get("chunks", []):
                    item["start"] *= scale
                    item["end"] *= scale
                timing_path.write_text(json.dumps(timing) + "\n")
            task.check_cancelled()
            target.replace(path)

    return process
