"""Slides: Davis--Kahan Proposition 4.4 is false as printed.

The printed claim: over a real space, if every principal angle between ``U``
and ``V`` is at most ``pi/3``, then among all orthogonal ``W`` with
``W(U) = V`` the direct rotation minimizes ``||I - W||`` in every unitarily
invariant norm.  The repository refutes it with an explicit ``R^4`` witness
(both principal angles ``pi/4``) and proves the repair for ``Q``-norms.

Every number comes from :class:`dkvis.prop44.Prop44Model`, the same checked
model covered by the numerical regression tests.
"""

from __future__ import annotations

import math as pymath
from pathlib import Path

import numpy as np
from manim import (
    DOWN,
    LEFT,
    UP,
    Arc,
    Arrow,
    Circle,
    Create,
    DashedLine,
    FadeIn,
    Line,
    Rectangle,
    Transform,
    ValueTracker,
    VGroup,
    always_redraw,
    rate_functions,
)

from dkvis.prop44 import Prop44Model
from dkvis.slide_style import (
    WANTED,
    FAINT,
    FG,
    MUTED,
    PANEL,
    REFUTED,
    SINE,
    TRIAL,
    DeckSlide,
    boxed,
    math,
    para,
    tex,
)

MODEL = Prop44Model()


def norms(singular_values: np.ndarray) -> dict[str, float]:
    sv = np.asarray(singular_values)
    return {"op": float(sv.max()), "fro": float(np.sqrt((sv**2).sum())), "trace": float(sv.sum())}


R_NORMS = norms(MODEL.direct_singular_values)
W_NORMS = norms(MODEL.competitor_singular_values)


def arrow(start, end, color, width=6.0):
    return Arrow(start, end, buff=0, color=color, stroke_width=width, max_tip_length_to_length_ratio=0.22)


def p3(x, y) -> np.ndarray:
    return np.array([x, y, 0.0])


class P4Slide(DeckSlide):
    section = "Davis--Kahan Proposition 4.4 $\\cdot$ a printed claim that is false"


# ----------------------------------------------------------------------------
# The claim
# ----------------------------------------------------------------------------


class P01Claim(P4Slide):
    title = "A second result: Proposition 4.4 is false"
    kicker = "Which orthogonal map carries one subspace onto another with the least motion?"

    def body(self) -> None:
        theta = np.radians(35.0)
        scale = 1.2

        def panel(center):
            c = np.asarray(center, float)
            U = Line(c + p3(-1.35, 0) * scale, c + p3(1.35, 0) * scale, color=WANTED, stroke_width=4)
            d = np.array([np.cos(theta), np.sin(theta), 0.0])
            V = Line(c - 1.35 * scale * d, c + 1.35 * scale * d, color=TRIAL, stroke_width=4)
            lu = math(r"\sym{U}", size=28).next_to(c + p3(1.35, 0) * scale, DOWN, buff=0.08)
            lv = math(r"\sym{V}", size=28).next_to(c + 1.35 * scale * d, UP, buff=0.05)
            return VGroup(U, V, lu, lv)

        top_c, bot_c = p3(-3.9, 0.85), p3(-3.9, -2.05)
        top, bot = panel(top_c), panel(bot_c)
        top_lbl = tex(r"direct rotation", size=26, color=FG).move_to(top_c + p3(-2.3, 1.5), aligned_edge=LEFT)
        bot_lbl = tex(r"a reflection", size=26, color=FG).move_to(bot_c + p3(-2.3, 1.5), aligned_edge=LEFT)

        e1, e2 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
        rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        refl = np.array([[np.cos(theta), np.sin(theta)], [np.sin(theta), -np.cos(theta)]])

        def frame(center, M=np.eye(2)):
            c = np.asarray(center, float)
            a = arrow(c, c + scale * p3(*(M @ e1)), FG)
            b = arrow(c, c + scale * p3(*(M @ e2)), MUTED)
            return VGroup(a, b)

        def moves(center, M):
            c = np.asarray(center, float)
            return VGroup(
                *[
                    DashedLine(c + scale * p3(*x), c + scale * p3(*(M @ x)), color=SINE, stroke_width=4, dash_length=0.07)
                    for x in (e1, e2)
                ]
            )

        x_text, w_text = 0.2, 6.6
        t1 = para(
            r"Many orthogonal maps carry the subspace $\sym{U}$ onto $\sym{V}$. "
            r"The \emph{direct rotation} turns by exactly the principal angles and does nothing else.",
            width=w_text,
            size=25,
        )
        t2 = para(
            r"A reflection also carries $U$ onto $V$, but it moves other vectors much further. "
            r"(\cx{sine}{Pink}: how far each vector moves.)",
            width=w_text,
            size=25,
        )
        claim = boxed(
            para(
                r"\textbf{Proposition 4.4 (as printed).} Over $\mathbb{R}$, if every principal angle is "
                r"at most $\pi/3$, then among all orthogonal $W$ with $W(U)=V$ the direct rotation "
                r"minimizes $\norm{I-W}$, in \emph{every} unitarily invariant norm.",
                width=w_text - 0.4,
                size=25,
            ),
            color=FG,
            pad=0.2,
        )
        t3 = para(
            r"A \emph{norm} turns $I-W$, the displacement matrix, into a measure of size. "
            r"Different norms combine motion across directions differently; the printed claim "
            r"says the direct rotation wins for \emph{every} one.",
            width=w_text,
            size=22,
            color=MUTED,
        )
        verdict = boxed(
            tex(r"False as printed: there is a counterexample in $\mathbb{R}^4$.", size=27),
            color=REFUTED,
            pad=0.2,
        )
        col = VGroup(t1, t2, claim, t3, verdict).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        col.move_to([x_text, self.content_top - 0.1, 0], aligned_edge=UP + LEFT)
        for m in col:
            if m.get_right()[0] > 6.85:
                m.scale((6.85 - x_text) / (m.get_right()[0] - x_text), about_edge=LEFT)

        self.say(
            "The second result of the project. Take two subspaces U and V. Many orthogonal maps carry U onto V. "
            "Davis and Kahan single out the direct rotation: it turns by exactly the principal angles."
        )
        f_top = frame(top_c)
        self.play(FadeIn(top), FadeIn(top_lbl), FadeIn(f_top), FadeIn(t1))
        self.play(Transform(f_top, frame(top_c, rot)), FadeIn(moves(top_c, rot)), run_time=1.5)

        self.say(
            "A reflection across the bisector also carries U onto V, but the other direction gets thrown "
            "across the plane. The pink segments show how far each vector moved."
        )
        f_bot = frame(bot_c)
        self.play(FadeIn(bot), FadeIn(bot_lbl), FadeIn(f_bot), FadeIn(t2))
        self.play(Transform(f_bot, frame(bot_c, refl)), FadeIn(moves(bot_c, refl)), run_time=1.5)

        self.say(
            "Proposition 4.4 says the direct rotation always moves space the least, measured by any "
            "unitarily invariant norm of I minus W, provided the angles are at most pi over 3. "
            "In the plane this is right, which makes it believable."
        )
        self.play(FadeIn(claim), FadeIn(t3))

        self.say("But as printed it is false, and we can exhibit the counterexample.")
        self.play(FadeIn(verdict, shift=UP * 0.1))


# ----------------------------------------------------------------------------
# The counterexample
# ----------------------------------------------------------------------------

# The two candidate maps are told apart by neutral styling (the direct rotation white, the
# competitor gray), not by blue and amber, which mean U and V everywhere in the talk.
PLANES = [
    # (column, row, label, angle, colour)
    (0, 0, r"plane $\langle e_0,e_3\rangle$", np.pi / 4, FG),
    (0, 1, r"plane $\langle e_1,e_2\rangle$", np.pi / 4, FG),
    (1, 0, r"moving plane", np.pi / 2, MUTED),
    (1, 1, r"fixed plane", 0.0, MUTED),
]


class P02Counterexample(P4Slide):
    title = r"The counterexample in $\mathbb{R}^4$"
    kicker = r"Both principal angles are $\pi/4$; two maps carry $U$ onto $V$"

    def body(self) -> None:
        radius = 0.78
        centers = {(0, 0): p3(-5.35, 0.75), (0, 1): p3(-5.35, -1.65), (1, 0): p3(-2.55, 0.75), (1, 1): p3(-2.55, -1.65)}
        t = ValueTracker(0.0)

        heads = VGroup(
            tex(r"direct rotation $\mathcal R$", size=26, color=FG).move_to(centers[(0, 0)] + p3(0, 1.3)),
            tex(r"competitor $W$", size=26, color=MUTED).move_to(centers[(1, 0)] + p3(0, 1.3)),
        )
        panels = VGroup()
        for col, row, label, alpha, color in PLANES:
            c = centers[(col, row)]
            circ = Circle(radius=radius, color=FAINT, stroke_width=2).move_to(c)
            start = c + radius * p3(1, 0)
            base = Line(c, start, color=MUTED, stroke_width=3)

            def tip(c=c, alpha=alpha):
                a = alpha * t.get_value()
                return c + radius * p3(np.cos(a), np.sin(a))

            spoke = always_redraw(lambda c=c, color=color, tip=tip: Line(c, tip(), color=color, stroke_width=5))
            ch = always_redraw(lambda start=start, tip=tip: Line(start, tip(), color=SINE, stroke_width=6))
            arc = always_redraw(
                lambda c=c, alpha=alpha: Arc(
                    radius=0.3, start_angle=0, angle=max(alpha * t.get_value(), 1e-3), arc_center=c, color=FG, stroke_width=2.5
                )
            )
            deg = tex(rf"${pymath.degrees(alpha):.0f}^\circ$", size=24, color=FG).move_to(c + p3(0, -radius - 0.25))
            lbl = tex(label, size=20, color=MUTED).move_to(c + p3(0, radius + 0.22))
            panels.add(VGroup(circ, base, spoke, ch, arc, deg, lbl))

        x0, w = 0.05, 6.7
        intro = para(
            r"Measure each map by $\norm{I-T}$, the size of its displacement. "
            r"Norms differ in how they combine motion across directions. "
            r"A plane turned by $\alpha$ contributes two equal singular values "
            r"of $I-T$: the \cx{sine}{chord} $2\sin(\alpha/2)$.",
            width=w,
            size=22,
        )
        intro.move_to([x0, self.content_top - 0.15, 0], aligned_edge=UP + LEFT)

        self.say(
            "Here are both maps, one two-dimensional plane at a time. The direct rotation turns two "
            "planes by 45 degrees each. The competitor turns one plane by 90 degrees and "
            "leaves the other fixed. Both carry U onto V. A norm measures the size of the "
            "displacement matrix I minus T. Different norms emphasize different aspects "
            "of the same motion."
        )
        self.play(FadeIn(heads), *[FadeIn(p) for p in panels], FadeIn(intro))
        self.play(t.animate.set_value(1.0), run_time=2.5, rate_func=rate_functions.ease_in_out_sine)

        # A rotation through alpha contributes TWO copies of the chord to the
        # singular values of I - T. The trace norm adds all four values.
        unit = 1.50
        bar_h = 0.28

        def stacked(lengths, color, y):
            segs, x = VGroup(), x0 + 0.55
            for length in lengths:
                if length < 1e-9:
                    continue
                seg = Rectangle(
                    width=unit * length,
                    height=bar_h,
                    fill_color=color,
                    fill_opacity=0.85,
                    stroke_color=PANEL,
                    stroke_width=2,
                )
                seg.move_to([x, y, 0], aligned_edge=LEFT)
                segs.add(seg)
                x += unit * length
            return segs

        y_r, y_w = intro.get_bottom()[1] - 0.68, intro.get_bottom()[1] - 1.12
        r_sv, w_sv = MODEL.direct_singular_values, MODEL.competitor_singular_values
        bars = VGroup(
            tex(r"$\mathcal R$", size=24, color=FG).move_to([x0 + 0.2, y_r, 0]),
            stacked(r_sv, FG, y_r),
            tex(rf"${R_NORMS['trace']:.3f}$", size=24, color=FG).move_to(
                [x0 + 0.75 + unit * R_NORMS["trace"], y_r, 0], aligned_edge=LEFT
            ),
            tex(r"$W$", size=24, color=MUTED).move_to([x0 + 0.2, y_w, 0]),
            stacked(w_sv, MUTED, y_w),
            tex(rf"${W_NORMS['trace']:.3f}$", size=24, color=MUTED).move_to(
                [x0 + 0.75 + unit * W_NORMS["trace"], y_w, 0], aligned_edge=LEFT
            ),
        )
        bars_title = tex(
            r"Trace norm $=$ sum of all four chord lengths",
            size=23,
            color=MUTED,
        ).move_to([x0, y_r + 0.40, 0], aligned_edge=LEFT)

        self.say(
            "Each two-dimensional rotated plane contributes two identical chord lengths "
            "as singular values of I minus T. The trace norm adds all four. The direct "
            "rotation has four chords of about zero point seven six five. The competitor "
            "has two chords of about one point four one four, plus two zeros."
        )
        self.play(FadeIn(bars_title), FadeIn(bars, lag_ratio=0.15))

        # Build the comparison from individual cells: the red outline hugs the
        # actual trace row rather than assuming an array row's rendered height.
        title = tex(
            r"Norm choice matters: the trace norm refutes the claim",
            size=23,
            color=FG,
        )
        if title.width > w:
            title.scale_to_fit_width(w)
        title.move_to([x0, bars.get_bottom()[1] - 0.28, 0], aligned_edge=UP + LEFT)
        norm_x = x0 + 0.12
        r_x, sign_x, w_x = x0 + 3.39, x0 + 4.48, x0 + 5.60
        header_y = title.get_bottom()[1] - 0.32
        header = VGroup(
            tex(r"norm", size=21, color=MUTED).move_to(
                [norm_x, header_y, 0], aligned_edge=LEFT
            ),
            math(r"\norm{I-\mathcal R}", size=23).move_to([r_x, header_y, 0]),
            math(r"\norm{I-W}", size=23).move_to([w_x, header_y, 0]),
        )
        rule_y = header.get_bottom()[1] - 0.13
        rule = Line(p3(x0 + 0.02, rule_y), p3(x0 + 6.4, rule_y), color=FAINT, stroke_width=2)
        labels = (
            ("operator", "op"),
            ("Frobenius", "fro"),
            ("trace", "trace"),
        )
        table_rows = VGroup()
        for i, (label, key) in enumerate(labels):
            y = rule_y - 0.32 - i * 0.38
            sign = "<" if R_NORMS[key] < W_NORMS[key] else ">"
            table_rows.add(VGroup(
                tex(label, size=22).move_to([norm_x, y, 0], aligned_edge=LEFT),
                math(rf"{R_NORMS[key]:.3f}", size=23).move_to([r_x, y, 0]),
                math(sign, size=25, color=REFUTED if key == "trace" else FG).move_to([sign_x, y, 0]),
                math(rf"{W_NORMS[key]:.3f}", size=23).move_to([w_x, y, 0]),
            ))
        failure_outline = Rectangle(
            width=6.42,
            height=table_rows[2].height + 0.14,
            stroke_color=REFUTED,
            stroke_width=2.7,
            fill_opacity=0.0,
        ).move_to([x0 + 3.23, table_rows[2].get_center()[1], 0])

        # Keep the explanatory material above the footer at any supported theme
        # while keeping the numerical comparison and all highlight geometry aligned.
        right_content = VGroup(intro, bars_title, bars, title, header, rule, table_rows, failure_outline)
        floor = -3.13
        if right_content.get_bottom()[1] < floor:
            right_content.scale(
                (right_content.get_top()[1] - floor) / right_content.height,
                about_edge=UP + LEFT,
            )

        self.say(
            "Operator norm looks at the worst single displacement, Frobenius norm at "
            "the root sum of squared displacements, and trace norm at their sum. "
            "The first two norms favor the direct rotation. The choice of norm matters."
        )
        self.play(FadeIn(title), FadeIn(header), Create(rule), FadeIn(table_rows[0]), FadeIn(table_rows[1]))

        self.say(
            "The highlighted trace norm is where the printed proposition fails: "
            "three point zero six one is greater than two point eight two eight. "
            "Both maps send U onto V, and both principal angles are 45 degrees, "
            "within the claimed 60-degree limit."
        )
        self.play(FadeIn(table_rows[2]), Create(failure_outline))


# ----------------------------------------------------------------------------
# Why, and details
# ----------------------------------------------------------------------------


# Pull the displayed theorem *verbatim* from Lean, rather than retyping it in
# TeX (which can silently change Lean syntax or binder interpretation).
LEAN_ROOT = Path(__file__).resolve().parents[2]
COUNTEREXAMPLE_SOURCE = (
    LEAN_ROOT / "DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean"
)
QNORM_SOURCE = LEAN_ROOT / "DavisKahan/FiniteDimensional/DirectRotation/QNorm.lean"
