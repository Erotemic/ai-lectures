"""Handouts use a movie frame when a scene contains only external video."""
from dkvis.presentation.build import handout_frame_file


def test_handout_selects_a_movie_frame_for_src_only_scene():
    assert handout_frame_file([{"file": "movie.mp4", "src": "movie.mp4"}]) == "movie.mp4"
    assert handout_frame_file([
        {"file": "drawn.mp4", "src": None},
        {"file": "movie.mp4", "src": "movie.mp4"},
    ]) == "drawn.mp4"
