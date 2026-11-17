"""Slides: the sine-theta theorem in three dimensions, built on the VTK demo.

Stills and movies come from :mod:`dkvis.vtk_sine_theta_3d` and are written to
``media/vtk3d/`` by :func:`prepare` (``dkvis.presentation.build`` calls it).  Still
builds show a VTK render beside LaTeX text; movie builds are full-frame VTK
videos that loop until the presenter advances.  The same scene runs live::

    uv run --extra vtk python -m dkvis.vtk_sine_theta_3d

D01Planes is retained for the narrated sine-theta lecture.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, Group, ImageMobject, Rectangle, VGroup

from dkvis.palette import OUTPUT_SUFFIX
from dkvis.slide_style import MUTED, DeckSlide, para

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "media" / f"vtk3d{OUTPUT_SUFFIX}"
ASSET_NAMES = [
    "still-exact.png",
    "still-planes.png",
    "still-sine.png",
    "still-residual.png",
    "still-perturb.png",
    "app.png",
    "orbit.mp4",
    "sweep-theta.mp4",
    "sweep-lambda3.mp4",
    "perturb.mp4",
]


def prepare(refresh: bool = False) -> None:
    """Render the VTK stills and movies these slides use (a few minutes)."""
    if not refresh and all((ASSETS / name).exists() for name in ASSET_NAMES):
        return
    cmd = [sys.executable, "-m", "dkvis.vtk_sine_theta_3d", "--slide-assets", str(ASSETS)]
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)


def asset(name: str) -> Path:
    path = ASSETS / name
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing; run `make assets` (with the same DKVIS_THEME) to render it")
    return path


TEXT_X = 0.75
TEXT_W = 6.1


def picture(name: str) -> Group:
    """An uncropped still within the actual left column of the 3D slides.

    Earlier versions set the *height* to 6.1 units.  At the VTK stills' wide
    aspect ratio that produced an 11-unit-wide image, cropping the left edge
    and overlapping the explanatory text.  Fit the width instead, with a
    quiet outline; the full-screen movie builds retain their native size.
    """
    img = ImageMobject(str(asset(name)))
    img.width = 6.65
    img.move_to([-3.35, -0.35, 0])
    border = Rectangle(
        width=img.width + 0.06,
        height=img.height + 0.06,
        stroke_color=MUTED,
        stroke_width=1.0,
    ).move_to(img)
    return Group(border, img)


def text_block(*paras: str, top: float, size: float = 27) -> VGroup:
    group = VGroup(*[para(p, width=TEXT_W, size=size) for p in paras])
    group.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
    group.move_to([TEXT_X, top, 0], aligned_edge=UP + LEFT)
    return group


class D3Slide(DeckSlide):
    section = "The Davis--Kahan $\\sin\\Theta$ theorem $\\cdot$ in three dimensions"

    def swap_picture(self, old: Group | None, name: str, *extra) -> Group:
        new = picture(name)
        anims = [FadeIn(new)] + ([FadeOut(old)] if old is not None else []) + [FadeIn(m) for m in extra]
        self.play(*anims, run_time=0.8)
        return new


class D01Planes(D3Slide):
    title = "The same picture in three dimensions"
    kicker = r"Subspaces, not just vectors: two planes in $\mathbb{R}^3$"

    def body(self) -> None:
        top = self.content_top - 0.2
        paras = [
            r"With positive eigenvalues, $\sym{Ahat}=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$ maps the unit "
            r"sphere of $\mathbb{R}^3$ to an ellipsoid. "
            r"The exact wanted frame $\sym{F0}=[f_1\ f_2]$ spans the plane of the two short axes; "
            r"$\sym{F1}=[f_3]$ spans the exact unwanted direction and $\sym{Lambda1}=[\like{Lambda1}{\lambda_3}]$.",
            r"A trial plane $\operatorname{range}(\sym{E0})$, tilted by $\sym{theta}$ about a line in $\operatorname{range}(\sym{F0})$. "
            r"Two planes in $\mathbb{R}^3$ always share a line, so the principal angles are $(\theta,0)$.",
            r"One nonzero sine: $\norm{\sym{sinTheta0}}=\norm{\sym{F1}^{\mathsf T}\sym{E0}}=\sin\theta$, "
            r"the pink drop from $\operatorname{range}(\sym{E0})$ to $\operatorname{range}(\sym{F0})$.",
            r"With the Rayleigh--Ritz choice $A_0=E_0^{\mathsf T}\sym{Ahat}E_0$ we get $E_0^{\mathsf T}R=0$: "
            r"the \cx{resid}{residuals} leave $\operatorname{range}(\sym{E0})$ at right angles.",
        ]
        texts = text_block(*paras, top=top, size=25)

        self.say(
            "Same story, one dimension up. This A hat has positive eigenvalues, so it maps the unit sphere "
            "to an ellipsoid. The wanted "
            "exact wanted frame F0 spans the plane of the two short axes, f1 and f2; F1 is the unwanted direction."
        )
        img = self.swap_picture(None, "still-exact.png", texts[0])

        self.say(
            "Now range E0 is a trial plane, tilted by theta about a line in range F0. Two planes in R^3 always "
            "meet in a line, so one principal angle is zero and the other is theta."
        )
        img = self.swap_picture(img, "still-planes.png", texts[1])

        self.say(
            "So sin Theta0 has one nonzero singular value: sin theta, the pink drop from the "
            "tilted trial vector to range F0. Its norm is the same in every unitarily invariant norm."
        )
        img = self.swap_picture(img, "still-sine.png", texts[2])

        self.say(
            "With the Rayleigh-Ritz trial matrix, E0-transpose R is zero: the residual of each "
            "trial vector sticks straight out of the trial plane."
        )
        img = self.swap_picture(img, "still-residual.png", texts[3])

        self.say(
            "The whole configuration, orbiting. This is a VTK render of the live demo. (Loops.)",
            src=asset("orbit.mp4"),
            loop=True,
        )
