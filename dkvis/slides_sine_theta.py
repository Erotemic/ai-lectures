"""Slides: an intuition-first introduction to the Davis--Kahan ``sin Theta`` theorem.

These visual bodies are reused by the narrated course edition. Build from
this repository's root with::

    make slides DECK=sine-theta-lecture QUALITY=l

The story:

1. a symmetric matrix is an ellipse, and its axes are the eigenvectors;
2. perturbing it barely moves the eigenvalues but can turn the axes, and
   without an eigenvalue gap the turn can be 45 degrees however small the
   perturbation;
3. the three ingredients: the angle ``sin Theta0``, the residual ``R``, the spectral separation
   ``delta``;
4. the theorem ``delta ||sin Theta0|| <= ||R||``;
5. why it holds (one vector, then the Sylvester equation), why the constant is
   sharp, what it says about perturbations, and what the Lean theorem states.

All numbers shown come from :mod:`dkvis.sine_theta_story` and
:mod:`dkvis.sine_theta`, whose models are checked by the test suite.
"""

from __future__ import annotations

import math as pymath

import numpy as np
from manim import (
    GrowFromCenter,
    TransformFromCopy,
    GrowArrow,
    LaggedStart,
    RoundedRectangle,
    Text,
    DOWN,
    LEFT,
    RIGHT,
    TAU,
    UL,
    UP,
    UR,
    Axes,
    BraceBetweenPoints,
    Create,
    DashedVMobject,
    Dot,
    FadeIn,
    FadeOut,
    GrowFromEdge,
    Line,
    Circle,
    Rectangle,
    ReplacementTransform,
    Transform,
    Triangle,
    ValueTracker,
    VGroup,
    VMobject,
    always_redraw,
    rate_functions,
)

from dkvis import sine_theta_story as story
from dkvis.notation import concept_color
from dkvis.sine_theta import SineThetaModel
from dkvis.slide_style import (
    CURRENT,
    FG,
    GAP,
    MONO_FONT,
    MUTED,
    OLD,
    PANEL,
    PERTURB,
    RESID,
    SINE,
    TRIAL,
    UNWANTED,
    WANTED,
    DeckSlide,
    boxed,
    dashed,
    math,
    para,
    tex,
)

from dkvis.components.common.geometry import (
    DEFAULT_ELLIPSE_ROTATION,
    Plane,
    angle_arc,
    ellipse,
    right_angle,
    segment,
    through_origin,
    vec,
)
from dkvis.components.common.layout import RIGHT_COL_W, RIGHT_COL_X, fit_right
from dkvis.components.common.readouts import live_matrix_2x2, readout_rows

# ----------------------------------------------------------------------------
# Drawing helpers
# ----------------------------------------------------------------------------


def column(*mobs, top: float, x: float = RIGHT_COL_X, buff: float = 0.35) -> VGroup:
    group = VGroup(*mobs).arrange(DOWN, aligned_edge=LEFT, buff=buff)
    group.move_to([x, top, 0], aligned_edge=UP + LEFT)
    for mob in mobs:
        fit_right(mob)
    return group


class RecallPanel(VGroup):
    """A "Recall" box of ``(symbol, meaning, colour)`` rows on a panel background.

    ``backgrounds[k]`` is the background sized to the first ``k`` rows, so a
    slide can show some rows first and grow the box later without moving them.
    """

    def __init__(self, rows, *, x: float, top: float, width: float = 5.9, size: float = 21):
        super().__init__()
        title = tex(r"Recall", size=size - 1, color=MUTED)
        keys = [
            tex(sym, size=size + 5) if color is None else tex(sym, size=size + 5, color=color)
            for sym, _, color in rows
        ]
        keys_w = max(k.width for k in keys)
        self.rows = VGroup()
        for key, (_, text, _) in zip(keys, rows):
            body = para(text, width=width - keys_w - 0.45, size=size)
            self.rows.add(VGroup(key, body).arrange(RIGHT, aligned_edge=UP, buff=0.22))
        self.rows.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        for row in self.rows:  # align the meanings in one column
            row[1].align_to(self.rows[0][0], LEFT).shift(RIGHT * (keys_w + 0.22))
        self.content = VGroup(title, self.rows).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        self.content.move_to([x + 0.18, top - 0.15, 0], aligned_edge=UP + LEFT)
        self.backgrounds = {}
        for k in range(1, len(self.rows) + 1):
            part = VGroup(title, *self.rows[:k])
            self.backgrounds[k] = Rectangle(
                width=width + 0.2,
                height=part.height + 0.3,
                fill_color=PANEL,
                fill_opacity=1,
                stroke_width=0,
            ).move_to([x + (width + 0.2) / 2, top - (part.height + 0.3) / 2, 0])
        self.title = title

    def show(self, k: int):
        """Background, title and the first ``k`` rows."""
        return VGroup(self.backgrounds[k], self.title, *self.rows[:k])


def text_col(body: str, size: float = 28, width: float = RIGHT_COL_W, color: str = FG) -> VMobject:
    return para(body, width=width, size=size, color=color)


# ----------------------------------------------------------------------------
# 0. Title
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# 0b. The setting
# ----------------------------------------------------------------------------


class S00bSetting(DeckSlide):
    title = "The setting: self-adjoint operators"
    kicker = r"A real symmetric matrix is the simplest instance, but not the only one"

    def body(self) -> None:
        levels = [
            (r"unbounded self-adjoint operators, e.g.\ $-\tfrac{d^2}{dx^2}$, quantum Hamiltonians", MUTED),
            (r"bounded self-adjoint operators, possibly infinite-dimensional", MUTED),
            (r"complex Hermitian matrices, $\ \sym{A}=\sym{A}^{*}$", FG),
            (r"real symmetric matrices, $\ \sym{A}=\sym{A}^{\mathsf T}$", FG),
        ]
        # Explicit nesting: (left, right, top, bottom) of each box.
        x_l, x_r = -6.8, 0.25
        tops = [self.content_top - 0.15, self.content_top - 1.05, self.content_top - 1.55, self.content_top - 2.05]
        bottoms = [-3.35, -3.15, -2.95, -2.75]
        boxes, labels = VGroup(), VGroup()
        for i, (label, color) in enumerate(levels):
            left, right = x_l + 0.25 * i, x_r - 0.25 * i
            box = RoundedRectangle(
                corner_radius=0.18,
                width=right - left,
                height=tops[i] - bottoms[i],
                stroke_color=color,
                stroke_width=2.6 if i == 3 else 1.8,
                fill_color=FG,
                fill_opacity=0.07 if i == 3 else 0.0,
            ).move_to([(left + right) / 2, (tops[i] + bottoms[i]) / 2, 0])
            lab = tex(label, size=22, color=color)
            lab.move_to([left + 0.2, tops[i] - 0.25, 0], aligned_edge=LEFT)
            if lab.width > right - left - 0.35:
                lab.scale((right - left - 0.35) / lab.width, about_edge=LEFT)
            boxes.add(box)
            labels.add(lab)
        outer_note = tex(r"$\uparrow$ scope of Davis--Kahan and our Lean theorem (separable spaces)", size=22, color=FG)
        if outer_note.width > x_r - x_l - 0.35:
            outer_note.scale((x_r - x_l - 0.35) / outer_note.width)
        outer_note.move_to([x_l + 0.2, tops[0] - 0.6, 0], aligned_edge=LEFT)
        inner = boxes[3]
        mini = math(r"\sym{A}=\begin{pmatrix}2&0.3\\0.3&1\end{pmatrix}", size=30, color=FG).move_to(
            inner.get_center() + np.array([0, 0.1, 0])
        )
        pictures = tex(r"the $\sin\Theta$ pictures in this talk: $2\times2$ and $3\times3$", size=22, color=MUTED).move_to(
            [inner.get_center()[0], bottoms[3] + 0.35, 0]
        )

        x0, w = 0.75, 6.1
        t1 = para(
            r"Throughout, $\sym{A}$ is \textbf{self-adjoint}: $\langle \sym{A}x,y\rangle=\langle x,\sym{A}y\rangle$ for all $x,y$. "
            r"For a real matrix that just means \emph{symmetric}, $\sym{A}=\sym{A}^{\mathsf T}$.",
            width=w,
            size=27,
        )
        t2 = para(
            r"In finite dimensions the spectral theorem gives real eigenvalues and \emph{perpendicular} "
            r"eigenvectors: a pure stretch along perpendicular axes. In infinite dimensions the corresponding "
            r"object is a decomposition into \emph{spectral subspaces}; eigenvectors need not span the space.",
            width=w,
            size=27,
        )
        t3 = para(
            r"Where it shows up: covariance matrices (PCA), graph Laplacians (spectral clustering), "
            r"Hamiltonians in quantum mechanics, vibration modes. The eigenspaces carry the meaning, "
            r"and the operator is often known only approximately.",
            width=w,
            size=25,
            color=MUTED,
        )
        col = VGroup(t1, t2, t3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        col.move_to([x0, self.content_top - 0.25, 0], aligned_edge=UP + LEFT)

        self.say(
            "First, the setting. Everything today is about self-adjoint operators: <Ax, y> = <x, Ay>. "
            "For a real matrix that is just a symmetric matrix. That is the innermost box here."
        )
        self.play(FadeIn(boxes[3]), FadeIn(labels[3]), FadeIn(mini), FadeIn(t1))

        self.say(
            "For a finite-dimensional symmetric or Hermitian matrix, the spectral theorem gives real eigenvalues "
            "and orthogonal eigendirections. In infinite dimensions the corresponding object is a decomposition "
            "into spectral subspaces; eigenvectors need not span the space. The class grows: complex Hermitian "
            "matrices, bounded operators "
            "on a Hilbert space, possibly infinite-dimensional, and unbounded ones like differential operators."
        )
        self.play(
            LaggedStart(*[FadeIn(VGroup(boxes[i], labels[i])) for i in (2, 1, 0)], lag_ratio=0.4),
            FadeIn(t2),
            run_time=2.0,
        )

        self.say(
            "The sin Theta pictures in this talk live in the innermost box, 2 by 2 and 3 by 3 real symmetric "
            "matrices; the Proposition 4.4 counterexample at the end lives in R^4. Davis and Kahan, and our "
            "Lean theorem, cover the outermost box, on separable Hilbert spaces. And these objects "
            "are everywhere: covariance matrices, graph Laplacians, quantum Hamiltonians."
        )
        self.play(FadeIn(pictures), FadeIn(outer_note), FadeIn(t3))


# ----------------------------------------------------------------------------
# 1. A symmetric matrix is an ellipse
# ----------------------------------------------------------------------------

ELLIPSE_BASE = DEFAULT_ELLIPSE_ROTATION


class S01Ellipse(DeckSlide):
    title = "Picturing a symmetric matrix"
    kicker = "For a positive-definite matrix, the unit circle maps to an ellipse"

    def body(self) -> None:
        lam1, lam2 = story.ELLIPSE_EIGENVALUES
        plane = Plane([-3.3, -0.75, 0], 1.25, rotate=ELLIPSE_BASE)
        A = np.diag([lam1, lam2])

        self.say(
            "Picture a symmetric matrix by what it does to the unit circle. This example is "
            "positive definite, with eigenvalues 2 and 1. Grey arrows are arbitrary unit "
            "vectors; the thick tan arrows are the two eigenvectors, tan being the color of A."
        )
        circle = ellipse(plane, np.eye(2), color=MUTED, width=2)
        sample_dirs = [story.unit(np.radians(22.5 + 45 * k)) for k in range(8)]
        samples = VGroup(*[vec(plane.origin, plane(d), FG, width=3).set_opacity(0.55) for d in sample_dirs])
        f1, f2 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
        eig_lines = VGroup(
            through_origin(plane, f1, 2.6, OLD, width=2, opacity=0.35),
            through_origin(plane, f2, 2.3, OLD, width=2, opacity=0.35),
        )
        e1 = vec(plane.origin, plane(f1), OLD, width=7)
        e2 = vec(plane.origin, plane(f2), OLD, width=7)
        intro = text_col(
            r"Take this positive-definite example, $\sym{A}$ with eigenvalues $2$ and $1$, "
            r"and watch where it sends the unit circle."
        )
        turned = text_col(
            r"Most vectors are stretched \emph{and turned}.\\[0.5em]"
            r"Eigenvectors are only stretched: "
            r"$\sym{A}f_i=\lambda_if_i$."
        )
        axes_text = text_col(
            r"The ellipse's axes point along the eigenvectors; in this example "
            r"the semi-axis lengths are the eigenvalues $2$ and $1$.\\[0.5em]"
            r"\cx{muted}{(For a general symmetric matrix the semi-axes are $|\lambda_i|$. "
            r"In $n$ dimensions the picture is an ellipsoid, and an \emph{eigenspace} "
            r"is spanned by some of its principal axes.)}"
        )
        column(intro, turned, axes_text, top=self.content_top - 0.2, buff=0.5)
        self.play(Create(circle), FadeIn(eig_lines), run_time=1.0)
        self.play(FadeIn(samples), FadeIn(e1), FadeIn(e2), FadeIn(intro))

        self.say(
            "Apply A. Generic vectors are stretched and turned. The eigenvectors are "
            "only stretched: A f = lambda f."
        )
        image = ellipse(plane, A, color=OLD, width=3)
        new_samples = VGroup(*[vec(plane.origin, plane(A @ d), FG, width=3).set_opacity(0.55) for d in sample_dirs])
        new_e1 = vec(plane.origin, plane(lam1 * f1), FG, width=7)
        new_e2 = vec(plane.origin, plane(lam2 * f2), FG, width=7)
        self.play(
            ReplacementTransform(circle, image),
            ReplacementTransform(samples, new_samples),
            ReplacementTransform(e1, new_e1),
            ReplacementTransform(e2, new_e2),
            FadeIn(turned),
            run_time=2.0,
        )

        self.say(
            "So the ellipse's axes point along the eigenvectors, and here the semi-axis lengths "
            "are the eigenvalues. For a general symmetric matrix they are the absolute values. "
            "In n dimensions it is an ellipsoid, and an eigenspace is spanned by principal axes."
        )
        l1 = math(r"\lambda_1 = 2", size=32).next_to(plane(lam1 * f1), RIGHT, buff=0.12)
        l2 = math(r"\lambda_2 = 1", size=32).next_to(plane(lam2 * f2), UP, buff=0.12)
        self.play(FadeOut(new_samples), FadeIn(l1), FadeIn(l2), FadeIn(axes_text))


# ----------------------------------------------------------------------------
# 2. Perturb it
# ----------------------------------------------------------------------------


class S02Perturb(DeckSlide):
    title = "Perturb the matrix"
    kicker = r"\cx{perturb}{PERTURBATION SETUP} --- $\sym{Ahat}=\sym{A}+\sym{H}$, with $\sym{H}$ small and symmetric"

    def body(self) -> None:
        eps = story.PERTURBATION_EPS
        gap = story.PERTURBATION_START_GAP
        pair = story.PerturbedPair(gap=gap, eps=eps)
        pair.verify()
        plane = Plane([-3.3, -0.75, 0], 1.25, rotate=ELLIPSE_BASE)

        self.say(
            "Start from the same ellipse, drawn with its axes. Now add a small symmetric H."
        )
        old = ellipse(plane, pair.A, color=OLD, width=2)
        old_axis = through_origin(plane, [1, 0], 3.0, OLD, width=3)
        old_axis2 = through_origin(plane, [0, 1], 2.0, OLD, width=3)
        eq = math(
            r"\sym{A}=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad "
            r"\sym{H}=\varepsilon\begin{pmatrix}0&1\\1&0\end{pmatrix},\ \ \varepsilon=0.12",
            size=30,
        )
        basis_note = tex(r"(written in the eigenbasis of $\sym{A}$)", size=22, color=MUTED)
        l_old = pair.A.diagonal()
        l_new = pair.perturbed_eigenvalues
        table = math(
            r"\begin{array}{lcc}"
            r" & \text{top} & \text{other}\\ \hline "
            rf"\sym{{A}} & {l_old[0]:.3f} & {l_old[1]:.3f}\\"
            rf"\sym{{Ahat}} & {l_new[0]:.3f} & {l_new[1]:.3f}"
            r"\end{array}",
            size=30,
        )
        weyl = tex(
            rf"Eigenvalues moved by ${pair.eigenvalue_shift:.3f} \le \norm{{\sym{{H}}}}_{{\rm op}} = {eps}$ (Weyl$^{{\ast}}$).",
            size=26,
        )
        weyl_note = para(
            r"$^{\ast}$\,\textbf{Weyl's inequality:} sort the eigenvalues of $\sym{A}$ and $\sym{Ahat}$; each moves by "
            r"at most $\norm{\sym{H}}_{\rm op}$ (the most $\sym{H}$ stretches any unit vector). It holds for every symmetric $\sym{A}$, "
            r"with no gap needed. Eigenvectors get no such guarantee.",
            width=RIGHT_COL_W,
            size=20,
            color=MUTED,
        )
        turn = tex(
            rf"Eigenvectors turned by \cx{{sine}}{{$\theta = {pymath.degrees(pair.theta):.1f}^\circ$}}.",
            size=26,
        )
        question = boxed(tex(r"How far can an eigenvector turn?", size=32), color=SINE)
        column(eq, basis_note, table, weyl, turn, question, top=self.content_top - 0.2, buff=0.24)
        basis_note.next_to(eq, DOWN, aligned_edge=LEFT, buff=0.12)
        weyl_note.move_to([RIGHT_COL_X, -3.28, 0], aligned_edge=DOWN + LEFT)
        self.play(Create(old), Create(old_axis), Create(old_axis2), FadeIn(eq), FadeIn(basis_note))

        self.say(
            "The ellipse of A hat is almost the same ellipse: the eigenvalues barely "
            "move. Weyl's inequality says they move by at most the norm of H. "
            "But the axes turn, by an angle theta."
        )
        new = ellipse(plane, pair.perturbed, color=CURRENT, width=3)
        v_new = pair.perturbed_top_eigenvector
        w_new = np.array([-v_new[1], v_new[0]])
        new_axis = through_origin(plane, v_new, 3.0, CURRENT, width=4)
        new_axis2 = through_origin(plane, w_new, 2.0, CURRENT, width=4)
        dashed_old = VGroup(
            DashedVMobject(through_origin(plane, [1, 0], 3.0, OLD, width=2), num_dashes=30),
            DashedVMobject(through_origin(plane, [0, 1], 2.0, OLD, width=2), num_dashes=20),
        )
        arc = angle_arc(plane, [1, 0], v_new, 2.9, SINE, width=4)
        theta = math(r"\sym{theta}", size=34).move_to(plane(3.25 * story.unit(pair.theta / 2)))
        self.play(
            ReplacementTransform(old_axis, dashed_old[0]),
            ReplacementTransform(old_axis2, dashed_old[1]),
            TransformFromCopySafe(old, new),
            Create(new_axis),
            Create(new_axis2),
            run_time=1.6,
        )
        self.play(Create(arc), FadeIn(theta), FadeIn(table), FadeIn(weyl), FadeIn(weyl_note), FadeIn(turn))

        self.say(
            "That is the question of the talk. Eigenvalue perturbation is easy "
            "(Weyl). How far can the eigenvectors, or more generally an invariant "
            "subspace, turn?"
        )
        self.play(FadeIn(question, shift=UP * 0.15))


def TransformFromCopySafe(source, target, **kwargs):
    """Grow ``target`` out of a copy of ``source`` (``source`` stays on screen)."""
    return ReplacementTransform(source.copy(), target, **kwargs)


# ----------------------------------------------------------------------------
# 3. No gap, no stability
# ----------------------------------------------------------------------------


class S03NoGap(DeckSlide):
    title = "How far can an eigenvector turn? It depends if there is a gap"
    kicker = r"\cx{perturb}{PERTURBATION SETUP} --- keep $\sym{H}$ fixed and shrink the gap of $\sym{A}$"

    def body(self) -> None:
        eps = story.PERTURBATION_EPS
        g_start, g_end = story.PERTURBATION_START_GAP, story.PERTURBATION_END_GAP
        g = ValueTracker(g_start)
        plane = Plane([-3.75, -0.25, 0], 1.1, rotate=ELLIPSE_BASE)
        reach = 2.3

        def pair() -> story.PerturbedPair:
            return story.PerturbedPair(gap=g.get_value(), eps=eps)

        def lam() -> tuple[float, float]:
            l1, l2 = pair().A.diagonal()
            return float(l1), float(l2)

        # A: dashed tan ellipse (the old matrix).  Its eigenvectors are drawn as the lines
        # they span (u and -u are the same eigendirection); the dots where the ellipse crosses them mark
        # its eigenvalues a_0 (top) and a_1.
        old = always_redraw(
            lambda: DashedVMobject(ellipse(plane, pair().A, color=OLD, width=2), num_dashes=60)
        )
        e_lines = VGroup(
            through_origin(plane, [1.0, 0.0], reach, OLD, width=3),
            through_origin(plane, [0.0, 1.0], reach, OLD, width=3),
        )
        e_dots = always_redraw(
            lambda: VGroup(Dot(plane([lam()[0], 0.0]), radius=0.07, color=OLD), Dot(plane([0.0, lam()[1]]), radius=0.07, color=OLD))
        )
        f1_lbl = always_redraw(lambda: math(r"a_0", size=28, color=OLD).next_to(plane([lam()[0], 0.0]), DOWN + LEFT * 0.6, buff=0.1))
        f2_lbl = always_redraw(lambda: math(r"a_1", size=28, color=OLD).next_to(plane([0.0, lam()[1]]), LEFT, buff=0.12))
        # A-hat: solid steel ellipse; its top eigenvector (the target) is blue, turned by theta.
        new = always_redraw(lambda: ellipse(plane, pair().perturbed, color=CURRENT, width=3))
        new_axis = always_redraw(lambda: through_origin(plane, pair().perturbed_top_eigenvector, reach, WANTED, width=3.5))
        new_lbl = always_redraw(
            lambda: tex(r"top eigenvector of $\sym{Ahat}$", size=20, color=concept_color("u")).next_to(
                plane(reach * pair().perturbed_top_eigenvector), RIGHT, buff=0.08
            )
        )
        e_lbls = VGroup(
            tex(r"top eigenvector of $\sym{A}$", size=20, color=OLD).next_to(plane([reach, 0.0]), DOWN, aligned_edge=LEFT, buff=0.1),
            tex(r"other eigenvector of $\sym{A}$", size=20, color=OLD).next_to(plane([0.0, reach]), UP, buff=0.08),
        )
        ellipse_key = VGroup(
            tex(r"\cx{old}{dashed: $\sym{A}$}", size=20),
            tex(r"\cx{current}{solid: $\sym{Ahat}$}", size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.06).move_to([-6.9, -2.05, 0], aligned_edge=UP + LEFT)
        arc = always_redraw(lambda: angle_arc(plane, [1, 0], pair().perturbed_top_eigenvector, 0.95, SINE, width=4))
        theta_lbl = always_redraw(
            lambda: math(r"\sym{theta}", size=30).move_to(plane(1.22 * story.unit(max(pair().theta, 0.16) / 2)))
        )

        # The eigenvalues of A on a number line, with the gap between them.
        lo, hi, x_lo, x_hi, y_nl = 0.75, 2.25, -6.4, -1.1, -3.0

        def X(v: float) -> np.ndarray:
            return np.array([x_lo + (v - lo) / (hi - lo) * (x_hi - x_lo), y_nl, 0.0])

        nl = Line(X(lo), X(hi), color=MUTED, stroke_width=2)
        nl_lbl = VGroup(
            tex(r"eigenvalues", size=20, color=MUTED),
            tex(r"\cx{old}{dots: $\sym{A}$} \ ticks: $\sym{Ahat}$, \cx{wanted}{top} and \cx{unwanted}{other}", size=18, color=MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.04).next_to(X(hi), RIGHT, buff=0.1)
        lam_dots = always_redraw(lambda: VGroup(*[Dot(X(v), radius=0.09, color=OLD) for v in lam()]))
        lam_lbls = always_redraw(
            lambda: VGroup(
                math(r"a_1", size=24, color=OLD).next_to(X(lam()[1]), DOWN, buff=0.12).shift(LEFT * 0.12),
                math(r"a_0", size=24, color=OLD).next_to(X(lam()[0]), DOWN, buff=0.12).shift(RIGHT * 0.12),
            )
        )
        new_ticks = always_redraw(
            lambda: VGroup(
                *[Line(X(v) + UP * 0.16, X(v) + DOWN * 0.16, color=c, stroke_width=3)
                  for v, c in zip(pair().perturbed_eigenvalues, (WANTED, UNWANTED))]
            )
        )

        def gap_marker():
            l1, l2 = lam()
            a, b = X(l2) + UP * 0.2, X(l1) + UP * 0.2
            if b[0] - a[0] > 0.3:
                mark = BraceBetweenPoints(a, b, direction=UP, color=GAP)
            else:
                mark = Line(a + UP * 0.1, b + UP * 0.1, color=GAP, stroke_width=4)
            label = tex(r"gap $g$", size=24, color=concept_color("g")).next_to(mark, UP, buff=0.06)
            return VGroup(mark, label)

        gap = always_redraw(gap_marker)

        axes = Axes(
            x_range=[0, 1.0, 0.25],
            y_range=[0, 45, 15],
            x_length=4.6,
            y_length=2.3,
            tips=False,
            axis_config={"color": MUTED, "stroke_width": 2, "include_ticks": True},
        ).move_to([4.0, 0.75, 0])
        x_lbl = math(r"\sym{g}", size=28).next_to(axes.x_axis, RIGHT, buff=0.15)
        y_lbl = math(r"\sym{theta}\ (\text{deg})", size=26).next_to(axes.y_axis, UP, buff=0.2)
        y_ticks = VGroup(*[math(str(v), size=22, color=MUTED).next_to(axes.c2p(0, v), LEFT, buff=0.1) for v in (15, 30, 45)])
        x_ticks = VGroup(*[math(f"{v:g}", size=22, color=MUTED).next_to(axes.c2p(v, 0), DOWN, buff=0.1) for v in (0.5, 1.0)])
        curve = axes.plot(
            lambda x: pymath.degrees(story.PerturbedPair(gap=x, eps=eps).theta),
            x_range=[0.005, 1.0],
            color=SINE,
            stroke_width=3,
        )
        dot = always_redraw(lambda: Dot(axes.c2p(g.get_value(), pymath.degrees(pair().theta)), color=SINE, radius=0.07))
        rows_l = readout_rows(
            [
                (r"\sym{g} =", lambda: g.get_value(), FG, 2, None),
                (r"\norm{\sym{H}}_{\rm op} =", lambda: eps, FG, 2, None),
            ],
            size=26,
        )
        rows_r = readout_rows(
            [
                (r"\max|\Delta\lambda| =", lambda: pair().eigenvalue_shift, FG, 3, None),
                (r"\sym{theta} =", lambda: pymath.degrees(pair().theta), SINE, 1, r"^\circ"),
            ],
            size=26,
        )
        rows_l.move_to([2.2, -1.2, 0])
        rows_r.move_to([5.0, -1.2, 0])

        self.say(
            "Tan dashed: the original A, drawn as its ellipse. Its eigenvectors are drawn as the lines they span, because "
            "an eigenvector only matters up to sign and length; the dots where the ellipse crosses them "
            "are the eigenvalues. Below, the same two eigenvalues on a number line; the violet bracket is "
            "the gap g between them. Solid steel: A hat, that is A + H, for a small H of size 0.12; its top eigenvector line, in blue, is "
            "turned by theta. Right: theta as a function of the gap."
        )
        left = VGroup(
            old, e_lines, e_dots, e_lbls, f1_lbl, f2_lbl, new, new_axis, new_lbl, ellipse_key, arc, theta_lbl,
            nl, nl_lbl, lam_dots, lam_lbls, new_ticks, gap,
        )
        self.add(left)
        self.play(
            FadeIn(left),
            Create(axes),
            FadeIn(x_lbl, y_lbl, y_ticks, x_ticks),
            Create(curve),
            FadeIn(rows_l, rows_r),
        )
        self.add(dot)

        self.say(
            "Now make A more and more round: its two eigenvalues slide together and the gap closes. "
            "The blue and cyan ticks, the eigenvalues of A hat, never move more than 0.12 from the tan dots, the eigenvalues of A. "
            "But the wanted eigenvector of A hat swings toward 45 degrees, however small H is."
        )
        self.play(g.animate.set_value(g_end), run_time=6.0, rate_func=rate_functions.ease_in_out_sine)
        takeaway = para(
            r"The same small $\sym{H}$ throughout. The eigenvalues move by at most $\norm{\sym{H}}_{\rm op}=0.12$; "
            r"the eigenvector turns further and further as the gap closes.",
            width=RIGHT_COL_W - 0.1,
            size=23,
        ).move_to([RIGHT_COL_X + 0.1, -1.95, 0], aligned_edge=UP + LEFT)
        self.play(FadeIn(takeaway, shift=UP * 0.1))


class S03cUnstable(DeckSlide):
    title = "Without a gap, an eigenvector can point anywhere"
    kicker = r"\cx{perturb}{PERTURBATION SETUP} --- turn fixed-size $\sym{H}$ once round and trace the eigenvector"

    def body(self) -> None:
        eps = story.PERTURBATION_EPS
        phi0 = pymath.pi / 2
        h_phi = ValueTracker(phi0)
        reach = 2.25

        class Panel:
            """A fixed ``A`` with gap ``g``, plus ``H(phi)`` of size ``eps`` turning as ``phi`` grows."""

            def __init__(panel, cx: float, gap: float, header: str):
                panel.ph = ValueTracker(phi0)
                panel.gap = gap
                plane = panel.plane = Plane([cx, 0.25, 0], 0.62, rotate=ELLIPSE_BASE)
                pair = panel.pair
                A = story.PerturbedPair(gap=gap, eps=0.0).A
                panel.header = tex(header, size=26).move_to([cx, 2.15, 0])
                panel.base = VGroup(
                    DashedVMobject(ellipse(plane, A, color=OLD, width=2), num_dashes=50),
                    through_origin(plane, [1.0, 0.0], reach, OLD, width=2.5),
                    through_origin(plane, [0.0, 1.0], reach, OLD, width=2.5),
                )
                panel.h_line = always_redraw(
                    lambda: DashedVMobject(through_origin(plane, pair().perturbation_direction, reach, PERTURB, width=2), num_dashes=22)
                )
                panel.new = always_redraw(lambda: ellipse(plane, pair().perturbed, color=CURRENT, width=2.5))
                panel.axis = always_redraw(lambda: through_origin(plane, pair().perturbed_top_eigenvector, reach, WANTED, width=3.5))
                # Leave a pink copy of the eigenvector line every few degrees of H's turn.
                steps = 72
                panel.trace = VGroup()
                state = {"next": 0}

                def grow(trace):
                    while state["next"] <= steps:
                        phi = phi0 + TAU * state["next"] / steps
                        if phi > panel.ph.get_value() + 1e-9:
                            break
                        d = story.PerturbedPair(gap=gap, eps=eps, phi=phi).perturbed_top_eigenvector
                        trace.add(through_origin(plane, d, reach, SINE, width=2, opacity=0.55))
                        state["next"] += 1

                panel.trace.add_updater(grow)

                # The two eigenvalues: dots for A, ticks for A-hat.
                lo, hi, half = 0.8, 2.2, 1.35
                y = -1.55

                def X(v: float) -> np.ndarray:
                    return np.array([cx - half + (v - lo) / (hi - lo) * 2 * half, y, 0.0])

                panel.line = VGroup(
                    Line(X(lo), X(hi), color=MUTED, stroke_width=2),
                    *[Dot(X(v), radius=0.07, color=OLD) for v in A.diagonal()],
                )
                panel.ticks = always_redraw(
                    lambda: VGroup(*[Line(X(v) + UP * 0.13, X(v) + DOWN * 0.13, color=c, stroke_width=2.5)
                                     for v, c in zip(pair().perturbed_eigenvalues, (WANTED, UNWANTED))])
                )

                def widest() -> float:
                    phis = np.linspace(phi0, panel.ph.get_value(), 181)
                    return max(pymath.degrees(story.PerturbedPair(gap=gap, eps=eps, phi=p).line_angle) for p in phis)

                panel.readout = readout_rows([(r"\text{widest turn} =", widest, SINE, 1, r"^\circ")], size=24)
                panel.readout.move_to([cx, -2.05, 0])

            def pair(panel) -> story.PerturbedPair:
                return story.PerturbedPair(gap=panel.gap, eps=eps, phi=panel.ph.get_value())

            def parts(panel) -> VGroup:
                return VGroup(panel.header, panel.base, panel.h_line, panel.new, panel.axis, panel.line, panel.ticks, panel.readout)

        with_gap = Panel(-5.0, story.PERTURBATION_START_GAP, rf"with a gap: $\sym{{g}}={story.PERTURBATION_START_GAP:g}$")
        no_gap = Panel(-1.55, story.PERTURBATION_END_GAP, rf"almost no gap: $\sym{{g}}={story.PERTURBATION_END_GAP:g}$")
        legend = VGroup(
            tex(r"\cx{old}{$\sym{A}$ and its eigenvectors} \quad \cx{current}{$\sym{Ahat}$}; \cx{perturb}{dashed: $\sym{H}$'s own direction}", size=18),
            tex(r"\cx{wanted}{blue: the top eigenvector of $\sym{Ahat}$}", size=18),
            tex(r"\cx{sine}{pink: every direction the top eigenvector of $\sym{Ahat}$ took}", size=18),
            tex(r"\cx{muted}{number lines: eigenvalues,} \cx{old}{dots $\sym{A}$,} ticks $\sym{Ahat}$ (\cx{wanted}{top}, \cx{unwanted}{other})", size=18),
        ).arrange(DOWN, buff=0.06).move_to([-3.3, -2.9, 0])

        text_w = RIGHT_COL_W - 0.5
        x0, top = RIGHT_COL_X + 0.55, self.content_top - 0.25
        t_intro = para(
            rf"Both panels use the same rotating perturbation $\sym{{H}}(\phi)$ with "
            rf"$\norm{{\sym{{H}}}}_{{\rm op}}={eps:g}$ throughout. The entries change while its size does not.",
            width=text_w, size=21,
        )
        h_matrix = live_matrix_2x2(
            lambda: story.PerturbedPair(gap=0.0, eps=eps, phi=h_phi.get_value()).H,
            label=r"\sym{H}(\phi)=",
            decimals=2,
            size=21,
            color=PERTURB,
        )
        h_note = tex(r"same $\sym{H}(\phi)$ in both panels", size=18, color=MUTED)
        h_display = VGroup(h_matrix, h_note).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
        t_gap = para(r"\textbf{With a gap}, the top eigenvector of $\sym{Ahat}$ stays within $7^\circ$.", width=text_w, size=22)
        t_nogap = para(
            r"\textbf{Without one}, it can point in \emph{any} direction: its direction is decided by $\sym{H}$, not by $\sym{A}$.",
            width=text_w, size=22,
        )
        t_flip = VGroup(
            math(
                r"\begin{pmatrix}1&\varepsilon\\ \varepsilon&1\end{pmatrix}\ \text{vs}\ "
                r"\begin{pmatrix}1&-\varepsilon\\ -\varepsilon&1\end{pmatrix}",
                size=24,
            ),
            tex(r"differ by $2\varepsilon$, but their eigenvectors are $\like{theta}{90^\circ}$ apart, for every $\varepsilon>0$", size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        t_rule = para(
            r"In this $2\times2$ example the switch is at $\norm{\sym{H}}_{\rm op}=\sym{g}/2$: below it the eigenvector only wobbles, "
            r"above it some $\sym{H}$ of that size points it anywhere.",
            width=text_w, size=21, color=MUTED,
        )
        t_sub = para(
            r"At $\sym{g}=0$ no single eigenvector is distinguished. "
            r"Davis--Kahan compares \emph{subspaces}.",
            width=text_w, size=20, color=MUTED,
        )
        column(t_intro, h_display, t_gap, t_nogap, t_flip, t_rule, t_sub, top=top, x=x0, buff=0.18)

        self.say(
            "Two copies of the same experiment. Left: A has a clear gap. Right: A is almost round. "
            "Both use the same rotating H, with norm 0.12. The live matrix shows H's entries. "
            "Watch the two wanted eigendirections rotate at the same time."
        )
        self.add(with_gap.trace, no_gap.trace)
        self.play(FadeIn(with_gap.parts(), no_gap.parts(), legend, t_intro, h_display))

        self.say(
            "With a gap, the top eigenvector of A hat moves only slightly; its traced fan is narrow. "
            "With almost no gap, it can turn in every direction. The same rotating H produces both "
            "outcomes. The eigenvalues in either panel still move by at most 0.12."
        )
        self.play(
            with_gap.ph.animate.set_value(phi0 + TAU),
            no_gap.ph.animate.set_value(phi0 + TAU),
            h_phi.animate.set_value(phi0 + TAU),
            run_time=7.0,
            rate_func=rate_functions.linear,
        )
        self.play(FadeIn(t_gap), FadeIn(t_nogap))

        self.say(
            "Two members of that family, as matrices: plus and minus epsilon off the diagonal. They "
            "differ by 2 epsilon, yet their eigenvectors are the two diagonals, 90 degrees apart. "
            "In this 2 by 2 example the switch happens when the size of H passes half the gap."
        )
        self.play(FadeIn(t_flip), FadeIn(t_rule))

        self.say(
            "With A exactly round, A is a multiple of the identity and every line is an eigenvector: "
            "there is no 'the' eigenvector to be stable. What is stable is the whole eigenspace. "
            "So Davis-Kahan works with subspaces: all the eigenvectors of an isolated cluster of eigenvalues."
        )
        self.play(FadeIn(t_sub))


# ----------------------------------------------------------------------------
# 3b. Which eigenvectors do we want?
# ----------------------------------------------------------------------------


class S03bWanted(DeckSlide):
    """Where "wanted" and "unwanted" come from: a choice made by eigenvalue."""

    title = "Which eigenvectors do we want?"
    kicker = "Rarely all of them: the ones belonging to a chosen part of the spectrum"

    def body(self) -> None:
        # Wanted: the two lowest eigenvalues, as for vibration modes and ground states.
        eigs = [0.35, 0.6, 1.45, 1.8, 2.2, 2.55, 2.85]
        wanted = [True, True] + [False] * 5
        lo, hi, x_lo, x_hi, y_nl = 0.1, 3.1, -6.4, -0.6, 1.25

        def X(t: float) -> np.ndarray:
            return np.array([x_lo + (t - lo) / (hi - lo) * (x_hi - x_lo), y_nl, 0.0])

        nl = Line(X(lo), X(hi), color=MUTED, stroke_width=2)
        nl_lbl = tex(r"eigenvalues of $\sym{Ahat}$", size=22, color=MUTED).next_to(X(hi), DOWN, buff=0.2).align_to(nl, RIGHT)
        # Wanted eigenvalues are filled blue dots, unwanted ones hollow cyan circles.
        dots = VGroup(*[
            Dot(X(t), radius=0.1, color=WANTED) if w else Circle(radius=0.09, color=UNWANTED, stroke_width=3).move_to(X(t))
            for t, w in zip(eigs, wanted)
        ])
        w_idx = [i for i, w in enumerate(wanted) if w]
        u_idx = [i for i, w in enumerate(wanted) if not w]
        w_box = Rectangle(
            width=X(eigs[w_idx[-1]])[0] - X(eigs[w_idx[0]])[0] + 0.5, height=0.6,
            stroke_color=WANTED, stroke_width=2, fill_color=WANTED, fill_opacity=0.12,
        ).move_to((X(eigs[w_idx[0]]) + X(eigs[w_idx[-1]])) / 2)
        w_lbl = tex(r"\cx{wanted}{wanted}", size=26).next_to(w_box, UP, buff=0.12)
        u_lbl = tex(r"\cx{unwanted}{unwanted}", size=26).next_to(
            (X(eigs[u_idx[0]]) + X(eigs[u_idx[-1]])) / 2, UP, buff=0.42
        )
        gap = BraceBetweenPoints(X(eigs[w_idx[-1]]) + DOWN * 0.2, X(eigs[u_idx[0]]) + DOWN * 0.2, direction=DOWN, color=GAP)
        gap_lbl = tex(r"wanted / unwanted split", size=21, color=concept_color("delta")).next_to(gap, DOWN, buff=0.06)
        spaces = VGroup(
            tex(r"wanted eigenvectors are the columns of $\sym{F0}$", size=24),
            tex(r"unwanted eigenvectors are the columns of $\sym{F1}$", size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to([x_lo, y_nl - 1.15, 0], aligned_edge=UP + LEFT)

        # A vibrating string: its lowest modes are the wanted eigenvectors.
        modes = VGroup()
        s = np.linspace(0.0, 1.0, 80)
        for k in range(1, 5):
            y = -1.3 - 0.56 * (k - 1)
            color = WANTED if k <= 2 else UNWANTED
            pts = [np.array([-6.2 + 3.4 * t, y + 0.2 * np.sin(k * np.pi * t), 0.0]) for t in s]
            curve = VMobject(color=color, stroke_width=3.5).set_points_smoothly(pts)
            ends = VGroup(Dot(pts[0], radius=0.04, color=MUTED), Dot(pts[-1], radius=0.04, color=MUTED))
            lbl = tex(rf"mode {k}" + (r" (lowest)" if k == 1 else ""), size=19, color=color).next_to(pts[-1], RIGHT, buff=0.2)
            modes.add(VGroup(curve, ends, lbl))
        modes_title = tex(r"a vibrating string: the lowest modes are wanted", size=19, color=MUTED).next_to(modes, UP, buff=0.12).align_to(modes, LEFT)

        x0, w = 0.6, 6.2
        t1 = para(
            r"A matrix has many eigenvectors, but an application usually needs only a few: "
            r"those whose eigenvalues lie in a chosen part of the spectrum.",
            width=w,
            size=25,
        )
        t1b = para(
            r"For a small dense matrix we can compute every eigenvector. But many applications produce enormous "
            r"sparse matrices, often by discretizing a differential operator, so eigensolvers compute only the few "
            r"modes the application asks for:",
            width=w,
            size=23,
            color=MUTED,
        )
        examples = VGroup(
            tex(r"\textbf{structures}: the lowest vibration modes", size=23),
            tex(r"\textbf{quantum mechanics}: the lowest-energy states of a Hamiltonian", size=23),
            tex(r"\textbf{spectral clustering}: the smallest graph-Laplacian modes", size=23),
            tex(r"\textbf{PCA}: the leading directions (largest eigenvalues)", size=23),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        t2 = para(
            r"``Wanted'' and ``unwanted'' is that choice, made by eigenvalue. Davis--Kahan compares a "
            r"trial frame $\sym{E0}$ with the exact wanted frame $\sym{F0}$, and the answer depends on how "
            r"well the relevant spectra are separated.",
            width=w,
            size=23,
        )
        col = VGroup(t1, t1b, examples, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col.move_to([x0, self.content_top - 0.2, 0], aligned_edge=UP + LEFT)
        for m in col:
            fit_right(m)

        self.say(
            "Before measuring errors: which eigenvectors are we even after? Rarely all of them. For a small dense "
            "matrix we could compute every eigenvector, but many applications produce enormous sparse matrices, "
            "often by discretizing a differential operator, so eigensolvers compute only the few modes the "
            "application asks for: the lowest vibration modes of a structure, the lowest-energy states in quantum "
            "mechanics, the smallest Laplacian modes in spectral clustering, the leading directions in PCA."
        )
        self.play(Create(nl), FadeIn(nl_lbl), FadeIn(dots, lag_ratio=0.1), FadeIn(t1), FadeIn(t1b), FadeIn(examples))

        self.say(
            "Those chosen eigenvalues are the wanted ones, in blue; collect their exact eigenvectors as the "
            "columns of F0. Everything else is unwanted, in cyan; collect those exact eigenvectors as F1. "
            "For a vibrating string, the lowest modes are wanted. The next step is to compare a trial frame E0 "
            "against the exact wanted frame F0."
        )
        self.play(FadeIn(w_box), FadeIn(w_lbl), FadeIn(u_lbl))
        self.play(GrowFromCenter(gap), FadeIn(gap_lbl), FadeIn(spaces), FadeIn(modes, modes_title), FadeIn(t2))


# ----------------------------------------------------------------------------
# 3d. Why not compute every eigenvector?
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# 4. Measuring the angle
# ----------------------------------------------------------------------------


class S04Angle(DeckSlide):
    title = "Measuring the error from two frames"
    kicker = r"\cx{muted}{GENERAL SETUP} --- $\sym{Ahat}=\sym{A}+\sym{H}$ is one case; the theorem studies any $\sym{Ahat}$"

    def body(self) -> None:
        th = ValueTracker(np.radians(35.0))
        plane = Plane([-5.12, -2.69, 0], 2.75)

        def model() -> SineThetaModel:
            return SineThetaModel(th.get_value())

        recall = RecallPanel(
            [
                (r"$\sym{E0}$", r"comparison frame for the operator under study", None),
                (r"$\sym{F0}$", r"orthonormal exact wanted frame of $\sym{Ahat}$: the target", None),
                (r"$\sym{F1}$", r"orthonormal exact unwanted frame; together $F_0,F_1$ fill the ambient space", None),
                (r"$\sym{Theta0}(\sym{E0},\sym{F0})$", r"principal angles between $\operatorname{range}(E_0)$ and $\operatorname{range}(F_0)$", None),
            ],
            x=-6.75,
            top=self.content_top - 0.1,
            width=5.75,
        )

        exact = through_origin(plane, [1, 0], 1.25, WANTED, width=4)
        exact.put_start_and_end_on(plane([-0.35, 0]), plane([1.25, 0]))
        exact_lbl = math(r"\operatorname{range}(\sym{F0})", size=31).next_to(plane([1.25, 0]), DOWN, buff=0.15)
        trial = always_redraw(
            lambda: Line(
                plane(-0.3 * model().trial_vector),
                plane(1.25 * model().trial_vector),
                color=TRIAL,
                stroke_width=3,
            ).set_opacity(0.65)
        )
        trial_lbl = always_redraw(
            lambda: math(r"\operatorname{range}(\sym{E0})", size=31).next_to(
                plane(1.25 * model().trial_vector), UP, buff=0.1
            )
        )
        e0 = always_redraw(lambda: vec(plane.origin, plane(model().trial_vector), TRIAL, width=7))
        e0_lbl = always_redraw(
            lambda: math(r"\sym{E0}", size=24).next_to(
                plane(model().trial_vector), UL, buff=0.05
            )
        )
        arc = always_redraw(lambda: angle_arc(plane, [1, 0], model().trial_vector, 0.9, SINE, width=3))
        th_lbl = always_redraw(
            lambda: math(r"\sym{theta}(\sym{E0},\sym{F0})", size=28).move_to(
                plane(0.38 * story.unit(model().theta / 2))
            )
        )

        self.say(
            "The perturbation model, A hat equals A plus H, was one way to obtain two subspaces. "
            "The general sine theta theorem does not require an original A or any H. Start with an operator "
            "A hat and a comparison frame E zero. The exact wanted invariant frame F zero of A hat is the "
            "reference for the theorem's conclusion. The comparison frame might be a numerical guess, "
            "or the true eigenspace of a latent A in the perturbation application. Either way, we want "
            "to compare the ranges of E zero and F zero. How should we measure their error?"
        )
        self.play(FadeIn(recall.show(2)), Create(exact), FadeIn(exact_lbl))
        self.add(trial, trial_lbl, e0, e0_lbl, arc, th_lbl)
        self.play(FadeIn(VGroup(trial, trial_lbl, e0, e0_lbl, arc, th_lbl)))

        self.say(
            "In this one-dimensional picture, project the trial column E0 onto the exact wanted line spanned by F0. "
            "The part left outside that line has length sin theta. This already has the same algebraic form as the "
            "operator used in the theorem."
        )
        proj = always_redraw(lambda: segment(plane.origin, plane(model().desired_projection), MUTED, width=5))
        perp = always_redraw(
            lambda: segment(plane(model().desired_projection), plane(model().trial_vector), SINE, width=8)
        )
        corner = always_redraw(
            lambda: right_angle(plane(model().desired_projection), [-1, 0], [0, 1], size=0.16)
        )
        perp_lbl = always_redraw(
            lambda: math(r"\sym{sintheta}", size=32).next_to(
                plane((model().desired_projection + model().trial_vector) / 2), RIGHT, buff=0.12
            )
        )
        proj_lbl = always_redraw(
            lambda: math(r"\sym{F0}\sym{F0}^{*}\sym{E0}", size=24).next_to(
                plane(model().desired_projection / 2), DOWN, buff=0.12
            )
        )
        f1 = math(
            r"\sym{sintheta}(\sym{E0},\sym{F0})"
            r"=\norm{(I-\sym{F0}\sym{F0}^{*})\sym{E0}}",
            size=30,
        )
        f1_note = tex(
            r"$\sym{F0}\sym{F0}^{*}$ projects onto $\operatorname{range}(\sym{F0})$",
            size=21,
            color=MUTED,
        )
        column(f1, f1_note, top=self.content_top - 0.25, buff=0.1)
        self.add(proj, perp, corner, perp_lbl, proj_lbl)
        self.play(FadeIn(VGroup(proj, perp, corner, perp_lbl, proj_lbl)), FadeIn(f1, f1_note))

        self.say(
            "Move the trial frame around: the pink leg is the error. It vanishes when the two ranges agree and "
            "reaches 1 when they are orthogonal. The same definition works without ever giving the ranges separate names."
            ,
            loop=True,
        )
        self.play(th.animate.set_value(np.radians(62)), run_time=2.0, rate_func=rate_functions.ease_in_out_sine)
        self.play(th.animate.set_value(np.radians(8)), run_time=2.8, rate_func=rate_functions.ease_in_out_sine)
        self.play(th.animate.set_value(np.radians(35)), run_time=1.8, rate_func=rate_functions.ease_in_out_sine)

        self.say(
            "For k columns, E0 and F0 determine k principal angles. The directed sin Theta0 operator is a function "
            "of those two frames. The rectangular blocks (I minus F0 F0 star) E0 and F1 star E0 have the same "
            "singular values, so proofs can compute with either block."
        )
        general = text_col(
            r"For $k$ columns there are $k$ \emph{principal angles} between "
            r"$\operatorname{range}(\sym{E0})$ and $\operatorname{range}(\sym{F0})$."
        )
        definition = boxed(
            para(
                r"$\sym{sinTheta0}(\sym{E0},\sym{F0})$ has eigenvalues "
                r"$\like{theta}{\sin\theta_1},\dots,\like{theta}{\sin\theta_k}$.",
                width=RIGHT_COL_W - 0.5,
                size=27,
            ),
            color=SINE,
            pad=0.18,
        )
        g_eq = math(
            r"\norm{\sym{sinTheta0}(\sym{E0},\sym{F0})}"
            r"=\norm{(I-\sym{F0}\sym{F0}^{*})\sym{E0}}"
            r"=\norm{\sym{F1}^{*}\sym{E0}}",
            size=29,
        )
        g_note = para(
            r"The three expressions have the same singular values, hence the same value in every "
            r"unitarily invariant norm.",
            width=RIGHT_COL_W,
            size=20,
            color=MUTED,
        )
        bridge = boxed(
            para(
                r"\textbf{General setting:} $\sym{E0}$ is a candidate/reference frame for $\sym{Ahat}$; "
                r"$\sym{F0}$ is exact. Their angle measures the discrepancy. Next: how can a residual bound it?",
                width=RIGHT_COL_W - 0.45,
                size=20,
            ),
            color=FG,
            pad=0.14,
        )
        right_col = column(
            VGroup(f1, f1_note).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            general,
            definition,
            g_eq,
            g_note,
            bridge,
            top=self.content_top - 0.25,
            buff=0.14,
        )
        if right_col.get_bottom()[1] < -3.45:
            right_col.scale((right_col.get_top()[1] + 3.45) / right_col.height, about_edge=UP + LEFT)
        self.play(
            Transform(recall.backgrounds[2], recall.backgrounds[4].copy()),
            FadeIn(recall.rows[2:]),
            FadeIn(VGroup(general, definition, g_eq, g_note), shift=UP * 0.1),
        )
        self.say(
            "That is the error we seek to bound. In a computed residual problem E zero can be known, "
            "while in a latent-truth perturbation problem E zero can be unknown. The formula for the "
            "angle applies to both. Next we will study the invariance defect, or residual."
        )
        self.play(FadeIn(bridge, shift=UP * 0.08))


# ----------------------------------------------------------------------------
# 5. The residual
# ----------------------------------------------------------------------------


class S05Residual(DeckSlide):
    """Motivate the residual from the information model before defining it."""

    title = "A computable signal: the residual"
    kicker = r"\cx{muted}{GENERAL THEOREM SETUP} --- the error needs exact $\sym{F0}$; the residual does not"

    def body(self) -> None:
        lam1, lam2 = story.RESIDUAL_EIGENVALUES
        phi = ValueTracker(np.radians(40.0))
        plane = Plane([-5.8, -2.7, 0], 2.45)

        def model() -> story.RayleighResidual:
            return story.RayleighResidual(lam1, lam2, phi.get_value())

        recall = RecallPanel(
            [
                (r"$\sym{Ahat}$", r"the matrix/operator whose invariant frame we want", None),
                (r"$\sym{v}$", r"a trial unit vector we already have; in one dimension $\sym{E0}=[\sym{v}]$", None),
                (r"$\sym{rho}$", r"the one-dimensional trial operator: $\sym{A0}=[\sym{rho}]$", None),
                (r"$\sym{F0}$", r"the exact wanted frame of $\sym{Ahat}$; needed for the true angle, usually unknown", None),
            ],
            x=-6.75,
            top=self.content_top - 0.1,
            width=6.15,
        )

        e_lines = VGroup(
            DashedVMobject(Line(plane([-0.2, 0]), plane([2.1, 0]), color=WANTED, stroke_width=2), num_dashes=24),
            DashedVMobject(Line(plane([0, -0.1]), plane([0, 1.2]), color=UNWANTED, stroke_width=2), num_dashes=14),
        ).set_opacity(0.7)
        exact_lbl = tex(r"$\operatorname{range}(\sym{F0})$ (exact, unknown)", size=20).next_to(
            plane([1.6, 0]), DOWN, buff=0.12
        )
        v = always_redraw(lambda: vec(plane.origin, plane(model().v), TRIAL, width=7))
        v_lbl = always_redraw(lambda: math(r"\sym{v}", size=32).next_to(plane(model().v), UL, buff=0.05))
        Av = always_redraw(lambda: vec(plane.origin, plane(model().Av), FG, width=5))
        Av_lbl = always_redraw(
            lambda: math(r"\sym{Ahat}\sym{v}", size=30).next_to(plane(model().Av), RIGHT, buff=0.1)
        )
        rho_v = always_redraw(lambda: segment(plane.origin, plane(model().rho_v), TRIAL, width=12).set_opacity(0.35))
        rho_lbl = always_redraw(
            lambda: math(r"\sym{rho}\,\sym{v}", size=28).next_to(plane(model().rho_v), LEFT, buff=0.12)
        )
        r = always_redraw(lambda: vec(plane(model().rho_v), plane(model().Av), RESID, width=7))
        r_lbl = always_redraw(
            lambda: math(r"\sym{r}", size=32).next_to(plane((model().rho_v + model().Av) / 2), UR, buff=0.06)
        )
        arc = always_redraw(lambda: angle_arc(plane, [1, 0], model().v, 0.55, SINE, width=4))
        th_lbl = always_redraw(
            lambda: math(r"\sym{theta}", size=30).move_to(plane(0.72 * story.unit(max(phi.get_value(), 0.12) / 2)))
        )

        x0, w, size = RIGHT_COL_X - 0.4, RIGHT_COL_W + 0.5, 24
        p2 = boxed(
            para(
                r"\textbf{Why introduce a residual?} The error $\sym{theta}(\sym{E0},\sym{F0})$ needs the exact "
                r"frame $\sym{F0}$. But we can test the trial using only $\sym{Ahat}$ and what we already have: "
                r"if $\sym{v}$ were an eigenvector, would $\sym{Ahat}\sym{v}$ point along $\sym{v}$?",
                width=w - 0.35,
                size=size - 1,
            ),
            color=FG,
            pad=0.14,
        )
        p3a = math(
            r"\sym{Ahat}\sym{v}=\underbrace{\sym{rho}\,\sym{v}}_{\text{best scaling}}"
            r"+\underbrace{\sym{r}}_{\text{residual}}",
            size=30,
        )
        rho_name = para(
            r"$\sym{rho}=\sym{v}^{*}\sym{Ahat}\sym{v}$ is the \textbf{Rayleigh quotient}: the scalar "
            r"trial operator for this one-dimensional frame.",
            width=w,
            size=size - 2,
        )
        p3b = para(
            r"$\sym{r}=\sym{Ahat}\sym{v}-\sym{rho}\sym{v}$ is the part the trial line cannot explain. "
            r"It uses no exact eigenvector or exact frame.",
            width=w,
            size=size - 2,
            color=MUTED,
        )
        p4 = readout_rows(
            [
                (r"\sym{theta}(\sym{E0},\sym{F0})\ (\text{needs exact }\sym{F0}) =", lambda: np.degrees(phi.get_value()), SINE, 1, r"^\circ"),
                (r"\norm{\sym{r}}\ (\text{from }\sym{Ahat},\sym{v}) =", lambda: model().residual_norm, RESID, 3, None),
            ],
            size=24,
        )
        p4b = tex(r"$\sym{r}=0$ exactly when the trial line is invariant.", size=size)
        p5a = math(
            r"\text{several columns:}\qquad \sym{R}=\sym{Ahat}\sym{E0}-\sym{E0}\sym{A0}",
            size=28,
        )
        p5c = para(
            r"For $\sym{Ahat}\in\mathbb C^{n\times n}$ and a $k$-column trial frame "
            r"$\sym{E0}\in\mathbb C^{n\times k}$, the trial operator $\sym{A0}$ is $k\times k$ and "
            r"$\sym{R}$ is $n\times k$. A common eigensolver choice is the Rayleigh--Ritz compression "
            r"$\sym{A0}=\sym{E0}^{*}\sym{Ahat}\sym{E0}$. In the perturbation application later, $\sym{A0}$ "
            r"instead comes from the exact wanted eigensystem of the original $\sym{A}$. In either case, $\sym{R}$ measures how much "
            r"$\sym{Ahat}\operatorname{range}(\sym{E0})$ leaves $\operatorname{range}(\sym{E0})$.",
            width=w,
            size=size - 2,
            color=MUTED,
        )
        p5b = boxed(
            tex(r"Does a small $\sym{R}$ force a small $\sym{sinTheta0}(\sym{E0},\sym{F0})$?", size=25),
            color=FG,
            pad=0.18,
        )
        col = VGroup(
            p2,
            VGroup(p3a, rho_name, p3b).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            VGroup(p4, p4b).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            VGroup(p5a, p5c, p5b).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
        )
        col.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        col.move_to([x0, self.content_top - 0.1, 0], aligned_edge=UP + LEFT)
        floor = -3.45
        if col.get_bottom()[1] < floor:
            col.scale((col.get_top()[1] - floor) / col.height, about_edge=UP + LEFT)
        for m in col:
            fit_right(m)
        for label, value in zip(p4[0], p4[1]):
            value.add_updater(lambda m, label=label: m.next_to(label, RIGHT, buff=0.15))

        self.say(
            "The information model is the point. A hat is the operator we are studying. The trial vector v is ours; "
            "in one dimension it is the single column of E0. The exact frame F0 is what we do not know, so the true "
            "angle is not available directly."
        )
        self.play(FadeIn(recall.show(4)), FadeIn(e_lines), FadeIn(exact_lbl))
        self.add(v, v_lbl, arc, th_lbl)
        self.play(FadeIn(VGroup(v, v_lbl, arc, th_lbl)))

        self.say(
            "So ask something testable. If v were an exact eigenvector of A hat, A hat v would point along v. "
            "The failure of that statement is the residual."
        )
        self.add(Av, Av_lbl)
        self.play(FadeIn(VGroup(Av, Av_lbl)), FadeIn(col[0]))

        self.say(
            "For this eigensolver-style example, the Rayleigh quotient rho is the natural scalar action on the trial line. "
            "Other applications can supply A0 differently. Split A hat v into rho v and "
            "the leftover r. Computing r needs A hat and v, but no F0. This is why residuals are useful as "
            "a posteriori information from an eigensolver."
        )
        self.add(rho_v, rho_lbl, r, r_lbl)
        self.play(FadeIn(VGroup(rho_v, rho_lbl, r, r_lbl)), FadeIn(col[1]))

        self.say(
            "Improve the trial direction: theta and the residual shrink together. We can monitor the residual; "
            "we cannot directly monitor the angle to F0."
        )
        self.play(FadeIn(col[2]))
        self.play(phi.animate.set_value(np.radians(6.0)), run_time=3.5, rate_func=rate_functions.ease_in_out_sine)

        self.say(
            "For several columns, replace v by the trial frame E0 and rho by the small trial operator A0. "
            "The residual is A hat E0 minus E0 A0. With Rayleigh--Ritz, A0 is E0 star A hat E0. The theorem asks "
            "whether a small, directly formed R plus spectral separation certifies a small angle to the exact frame F0."
        )
        self.play(FadeIn(col[3]), phi.animate.set_value(np.radians(40.0)), run_time=1.5)

# ----------------------------------------------------------------------------
# 6. The gap
# ----------------------------------------------------------------------------


class S06Gap(DeckSlide):
    title = r"The spectral separation $\sym{delta}$"
    kicker = r"\cx{muted}{GENERAL THEOREM SETUP} --- $\operatorname{spec}(\sym{A0})$ vs. the exact unwanted block $\sym{Lambda1}$ of $\sym{Ahat}$"

    def body(self) -> None:
        g = story.gap_picture_example()
        beta, alpha, delta = g["beta"], g["alpha"], g["delta"]
        y0 = 0.9
        scale = 1.95

        def X(t: float) -> np.ndarray:
            return np.array([scale * t, y0, 0.0])

        line = Line(X(-3.2), X(3.2), color=MUTED, stroke_width=2)
        window = Rectangle(
            width=scale * (alpha - beta + 2 * delta), height=0.9, fill_color=GAP, fill_opacity=0.14, stroke_width=0
        ).move_to(X((alpha + beta) / 2))
        window_edges = VGroup(
            DashedVMobject(Line(X(beta - delta) + DOWN * 0.45, X(beta - delta) + UP * 0.45, color=GAP, stroke_width=2), num_dashes=6),
            DashedVMobject(Line(X(alpha + delta) + DOWN * 0.45, X(alpha + delta) + UP * 0.45, color=GAP, stroke_width=2), num_dashes=6),
        )
        interval = Line(X(beta), X(alpha), color=TRIAL, stroke_width=8).set_opacity(0.45)
        ritz = VGroup(*[Dot(X(a), color=TRIAL, radius=0.1) for a in g["ritz"]])
        ritz_lbl = VGroup(
            tex(r"our trial-spectrum estimates", size=22),
            math(r"\operatorname{spec}(\sym{A0})\subset[\like{A0}{\beta},\like{A0}{\alpha}]", size=30),
        ).arrange(DOWN, buff=0.06).next_to(interval, UP, buff=0.4)
        ab = VGroup(
            math(r"\like{A0}{\beta}", size=28).next_to(X(beta), DOWN, buff=0.2),
            math(r"\like{A0}{\alpha}", size=28).next_to(X(alpha), DOWN, buff=0.2),
        )
        br_l = BraceBetweenPoints(X(beta - delta), X(beta), direction=DOWN, color=GAP).shift(DOWN * 0.45)
        br_r = BraceBetweenPoints(X(alpha), X(alpha + delta), direction=DOWN, color=GAP).shift(DOWN * 0.45)
        d_l = math(r"\sym{delta}", size=30).next_to(br_l, DOWN, buff=0.08)
        d_r = math(r"\sym{delta}", size=30).next_to(br_r, DOWN, buff=0.08)
        unwanted = VGroup(*[Dot(X(lam), color=UNWANTED, radius=0.1) for lam in g["unwanted"]])
        un_lbl_l = VGroup(
            tex(r"exact unwanted spectrum of $\sym{Ahat}$", size=22),
            math(r"\operatorname{spec}(\sym{Lambda1})", size=30),
        ).arrange(DOWN, buff=0.06).next_to(VGroup(*unwanted[:3]), UP, buff=0.4)
        un_lbl_r = VGroup(
            tex(r"exact unwanted spectrum of $\sym{Ahat}$", size=22),
            math(r"\operatorname{spec}(\sym{Lambda1})", size=30),
        ).arrange(DOWN, buff=0.06).next_to(VGroup(*unwanted[3:]), UP, buff=0.4)

        self.say(
            "The number line is the real axis of eigenvalues. Amber: the eigenvalues "
            "of the trial matrix A0, inside an interval [beta, alpha]."
        )
        self.play(Create(line), FadeIn(interval), FadeIn(ritz), FadeIn(ritz_lbl), FadeIn(ab))

        self.say(
            "Widen the trial-spectrum interval by delta on each side: the violet window. F1 is the exact unwanted "
            "frame of A hat, and Lambda1 is the operator on those unwanted coordinates: A hat F1 equals F1 Lambda1. "
            "The hypothesis says that the exact unwanted spectrum stays out of this window."
        )
        hyp = math(
            r"\like{A0}{\operatorname{spec}(A_0)}\subset[\like{A0}{\beta},\like{A0}{\alpha}],\qquad"
            r"\like{Lambda1}{\operatorname{spec}(\Lambda_1)}\cap"
            r"(\like{A0}{\beta}-\sym{delta},\,\like{A0}{\alpha}+\sym{delta})=\varnothing",
            size=32,
        ).move_to([0, -1.25, 0])
        lam_note = tex(
            r"$\sym{F1}$: exact unwanted frame; $\sym{Ahat}\sym{F1}=\sym{F1}\sym{Lambda1}$. "
            r"The theorem needs a certified lower separation, not necessarily the exact value of $\sym{delta}$."
            r"\quad The roles of $\sym{A0}$ and $\sym{Lambda1}$ may also be exchanged.",
            size=23,
            color=MUTED,
        ).next_to(hyp, DOWN, buff=0.25)
        self.play(FadeIn(window), FadeIn(window_edges), FadeIn(br_l, br_r, d_l, d_r))
        self.play(FadeIn(unwanted, lag_ratio=0.15), FadeIn(un_lbl_l), FadeIn(un_lbl_r), FadeIn(hyp), FadeIn(lam_note))

        self.say(
            "Delta is a spectral-separation certificate, not the original eigengap g from the perturbation example. "
            "Why an interval and not just 'every pair of eigenvalues is delta apart'? "
            "If the two spectra interleave, constant 1 survives only in the Frobenius "
            "norm (Davis-Kahan Theorem 6.2); in the operator norm it fails, and "
            "Section 5 of the paper gives an explicit 2x2 example."
        )
        warn = para(
            r"\cx{muted}{$\sym{delta}$ is not $\sym{g}$. Why an interval?} If the spectra are merely $\sym{delta}$ apart pairwise but "
            r"\emph{interleaved}, the bound with constant $1$ holds only in the Frobenius norm "
            r"(Davis--Kahan Thm~6.2); in the operator norm it can fail (\S5).",
            width=12.2,
            size=24,
        ).move_to([0, -3.05, 0])
        self.play(FadeIn(warn))


# ----------------------------------------------------------------------------
# 7. The theorem
# ----------------------------------------------------------------------------


class S07Theorem(DeckSlide):
    title = r"The $\like{theta}{\sin\Theta}$ theorem"
    kicker = r"\cx{muted}{GENERAL THEOREM} --- $\sym{Ahat}$, trial pair $(\sym{E0},\sym{A0})$, exact frame $\sym{F0}$, separation $\sym{delta}$; no $\sym{H}$ assumed"

    def body(self) -> None:
        self.say(
            "Now the relationship becomes useful. E0 and A0 are the trial data, F0 is the exact wanted frame, "
            "and R is the residual A hat E0 minus E0 A0. If the trial spectrum is separated from the exact unwanted "
            "spectrum by delta, Davis-Kahan bounds the unknown angle to F0."
        )
        stmt = math(
            r"\sym{delta}\,\norm{\sym{sinTheta0}(\sym{E0},\sym{F0})}"
            r"\ \le\ \norm{\sym{R}},\qquad "
            r"\sym{R}=\sym{Ahat}\sym{E0}-\sym{E0}\sym{A0}",
            size=48,
        )
        box = boxed(stmt, color=FG, pad=0.3).move_to([0, 1.65, 0])
        hyp = tex(
            r"$\operatorname{spec}(\sym{A0})\subset[\like{A0}{\beta},\like{A0}{\alpha}]$ and "
            r"$\operatorname{spec}(\sym{Lambda1})$ avoids "
            r"$(\like{A0}{\beta}-\sym{delta},\like{A0}{\alpha}+\sym{delta})$; "
            r"every unitarily invariant norm",
            size=25,
            color=MUTED,
        ).next_to(box, DOWN, buff=0.28)
        self.play(FadeIn(box, scale=0.95), FadeIn(hyp))

        self.say(
            "Read this as an information-flow statement. The angle needs F0, the exact frame we usually do not have. "
            "The residual is formed directly from A hat, E0 and A0. Delta is different: it is a spectral-separation "
            "hypothesis or certificate that must be established separately."
        )
        rows = VGroup(
            tex(
                r"$\norm{\sym{sinTheta0}(\sym{E0},\sym{F0})}$\quad target error; needs exact $\sym{F0}$",
                size=27,
            ),
            tex(
                r"$\norm{\sym{R}}$\quad directly formed from $\sym{Ahat},\sym{E0},\sym{A0}$",
                size=27,
            ),
            tex(
                r"$\sym{delta}$\quad certified separation of $\operatorname{spec}(\sym{A0})$ from $\operatorname{spec}(\sym{Lambda1})$",
                size=27,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        rows.next_to(hyp, DOWN, buff=0.35)
        self.play(FadeIn(rows, lag_ratio=0.3))

        self.say(
            "Rearranged: the subspace error is at most the residual norm divided by spectral separation. Notice what is absent: there is no original A "
            "and no perturbation H in the theorem itself. A hat is simply the operator whose exact frame F0 we want. "
            "On the next slide we add the extra perturbation structure A hat equals A plus H."
        )
        slogan = boxed(
            math(
                r"\norm{\sym{sinTheta0}(\sym{E0},\sym{F0})}"
                r"\ \le\ \frac{\norm{\sym{R}}}{\sym{delta}}"
                r"\qquad\text{error}\ \le\ \frac{\text{residual}}{\text{separation}}",
                size=31,
            ),
            color=SINE,
        ).next_to(rows, DOWN, buff=0.24)
        scope = para(
            r"\textbf{GENERAL:} $\sym{Ahat}$, $\sym{E0}$, $\sym{A0}$, exact $\sym{F0}$/$\sym{F1}$, and $\sym{delta}$. "
            r"\cx{perturb}{\textbf{PERTURBATION SPECIALIZATION (next):}} additionally set $\sym{Ahat}=\sym{A}+\sym{H}$ and choose "
            r"$\sym{E0},\sym{A0}$ from an exact wanted eigensystem of the original $\sym{A}$.",
            width=12.5,
            size=20,
            color=MUTED,
        ).next_to(slogan, DOWN, buff=0.16)
        self.play(FadeIn(slogan, shift=UP * 0.1))
        self.play(FadeIn(scope, shift=UP * 0.08))


# ----------------------------------------------------------------------------
# 8. Why: one trial vector
# ----------------------------------------------------------------------------


class S08Why(DeckSlide):
    """Why the theorem holds in one dimension of the exact spectral split.

    A trial vector ``v`` splits into the exact wanted direction ``f0`` and an
    exact unwanted direction ``f1``.  The residual scales the unwanted component
    by ``lambda1 - rho``; spectral separation makes that factor at least delta.
    """

    title = "Why it is true"
    kicker = r"\cx{muted}{GENERAL THEOREM MECHANISM} --- follow the part of $\sym{v}$ that points the wrong way"

    def body(self) -> None:
        ex = story.TWO_DIRECTIONS
        ex.verify()
        th, s_th = ex.theta, ex.sin_theta
        plane = Plane([-5.2, -1.55, 0], 2.55)
        e_u, e_w = np.array([1.0, 0.0]), np.array([0.0, 1.0])
        v = np.array([np.cos(th), s_th])

        u_axis = Line(plane([-0.35, 0]), plane([1.25, 0]), color=WANTED, stroke_width=3)
        w_axis = Line(plane([0, -0.15]), plane([0, 1.2]), color=UNWANTED, stroke_width=3)
        u_lbl = tex(r"$\sym{f0}$: exact wanted eigenvector", size=22).next_to(plane([1.25, 0]), DOWN, buff=0.12).shift(LEFT * 0.6)
        w_lbl = tex(r"$\sym{f1}$: exact unwanted eigenvector", size=22).next_to(plane([0, 1.2]), UP, buff=0.08)
        v_arrow = vec(plane.origin, plane(v), TRIAL, width=7)
        v_lbl = math(r"\sym{v}", size=32).next_to(plane(v), UR, buff=0.05)
        arc = angle_arc(plane, e_u, v, 0.45, SINE, width=3)
        th_lbl = math(r"\sym{theta}", size=28).move_to(plane(0.6 * story.unit(th / 2)))
        cos_part = segment(plane.origin, plane(np.cos(th) * e_u), WANTED, width=9).set_opacity(0.55)
        left = np.array([-0.045, 0.0])
        sin_part = segment(plane(left), plane(left + s_th * e_w), SINE, width=10)
        sin_lbl = math(r"\sym{sintheta}", size=28).next_to(plane(left + s_th * e_w), LEFT, buff=0.12)
        guides = VGroup(
            dashed(plane(v), plane(np.cos(th) * e_u), MUTED, 1.5),
            dashed(plane(v), plane(s_th * e_w), MUTED, 1.5),
        )

        # The residual's w-part, drawn beside the w-axis so it can be compared with sin(theta).
        off = np.array([0.045, 0.0])
        w_res = segment(plane(off), plane(off + ex.w_part * e_w), RESID, width=10)
        w_res_lbl = math(r"(\sym{lambda1}-\sym{rho})\sym{sintheta}", size=26).next_to(
            plane(off + ex.w_part * e_w), RIGHT, buff=0.12
        )
        r_arrow = vec(plane.origin, plane(ex.r), RESID, width=6)
        r_lbl = math(r"\sym{r}", size=30).next_to(plane(ex.r), UL, buff=0.05)
        r_guide = dashed(plane(ex.r), plane(ex.w_part * e_w), RESID, 1.5)

        # Eigenvalues on a number line under the picture.
        lo, hi, x_lo, x_hi, y_nl = 0.5, 2.9, -6.6, -1.6, -3.0

        def X(t: float) -> np.ndarray:
            return np.array([x_lo + (t - lo) / (hi - lo) * (x_hi - x_lo), y_nl, 0.0])

        nl = Line(X(lo), X(hi), color=MUTED, stroke_width=2)
        dots = VGroup(
            Dot(X(ex.lam_u), radius=0.08, color=WANTED),
            Dot(X(ex.lam_w), radius=0.08, color=UNWANTED),
        )
        dot_lbls = VGroup(
            math(r"\sym{lambda0}", size=24).next_to(X(ex.lam_u), DOWN, buff=0.12),
            math(r"\sym{lambda1}", size=24).next_to(X(ex.lam_w), DOWN, buff=0.12),
        )
        rho_mark = Triangle(color=TRIAL, fill_color=TRIAL, fill_opacity=1).scale(0.09).rotate(np.pi).move_to(X(ex.rho) + UP * 0.12)
        rho_lbl = math(r"\sym{rho}", size=24).next_to(X(ex.rho), DOWN, buff=0.12)
        gap_brace = BraceBetweenPoints(X(ex.rho) + UP * 0.2, X(ex.lam_w) + UP * 0.2, direction=UP, color=GAP)
        gap_lbl = tex(r"at least $\sym{delta}$", size=22, color=concept_color("delta")).next_to(gap_brace, UP, buff=0.04)
        spectrum = VGroup(nl, dots, dot_lbls, rho_mark, rho_lbl)

        # Right column, laid out once in final form; builds only add.
        x0, w, size = RIGHT_COL_X - 0.2, RIGHT_COL_W + 0.3, 25
        t1 = para(
            r"Split the trial vector $\sym{v}$ into the exact wanted direction $\sym{f0}$ and an exact "
            r"unwanted direction $\sym{f1}$.",
            width=w,
            size=size,
        )
        t1b = boxed(tex(r"$\sym{sintheta}$ = how much of $\sym{v}$ points the wrong way", size=size), color=SINE, pad=0.15)
        t2 = para(
            r"The residual $\sym{r}=(\sym{Ahat}-\sym{rho})\sym{v}$ multiplies each exact eigendirection by "
            r"its eigenvalue minus $\sym{rho}$. The $\sym{f1}$ component becomes "
            r"$(\sym{lambda1}-\sym{rho})\sym{sintheta}$, and the separation says $\sym{lambda1}$ is at "
            r"least $\sym{delta}$ from $\sym{rho}$.",
            width=w,
            size=size,
        )
        t3 = para(
            r"The residual may also have a $\sym{f0}$ component, so it is at least as long as its $\sym{f1}$ component:",
            width=w,
            size=size,
        )
        chain = math(
            r"\norm{\sym{r}}\ \ge\ |\sym{lambda1}-\sym{rho}|\,\sym{sintheta}\ \ge\ \sym{delta}\,\sym{sintheta}",
            size=32,
        )
        nums = tex(
            rf"here: $\norm{{\sym{{r}}}}={ex.model.residual_norm:.3f}\ \ge\ {abs(ex.w_part):.3f}"
            rf"=\sym{{delta}}\,\sym{{sintheta}}$",
            size=22,
            color=MUTED,
        )
        verdict = para(
            r"\textbf{The part of $\sym{v}$ pointing the wrong way always shows up in the residual, "
            r"scaled by at least $\sym{delta}$.}",
            width=w,
            size=size,
        )
        bridge = para(
            r"That is the one-vector mechanism. For whole subspaces the same spectral-separation idea becomes "
            r"a Sylvester equation; getting the sharp constant for every unitarily invariant norm is the "
            r"technical part of the full theorem.",
            width=w,
            size=size - 4,
            color=MUTED,
        )
        col = VGroup(
            VGroup(t1, t1b).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            t2,
            VGroup(t3, chain, nums).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            VGroup(verdict, bridge).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        col.move_to([x0, self.content_top - 0.1, 0], aligned_edge=UP + LEFT)
        floor = -3.45
        if col.get_bottom()[1] < floor:
            col.scale((col.get_top()[1] - floor) / col.height, about_edge=UP + LEFT)
        for m in col:
            fit_right(m)

        self.say(
            "Why should a small residual force a small angle? In the one-dimensional exact split, call the wanted "
            "eigenvector f0 and an unwanted one f1. Split the trial vector v into those exact directions. The pink "
            "unwanted component has length sin theta."
        )
        self.play(Create(u_axis), Create(w_axis), FadeIn(u_lbl, w_lbl))
        self.play(GrowArrow(v_arrow), FadeIn(v_lbl, arc, th_lbl))
        self.play(Create(guides), FadeIn(cos_part), FadeIn(sin_part), FadeIn(sin_lbl), FadeIn(col[0]))

        self.say(
            "Now the residual. A hat minus rho multiplies each exact eigendirection by its eigenvalue minus rho. "
            "So the unwanted component becomes lambda1 minus rho times sin theta. The separation certificate says "
            "that factor has magnitude at least delta."
        )
        self.play(FadeIn(spectrum), FadeIn(col[1]))
        self.play(GrowFromEdge(gap_brace, LEFT), FadeIn(gap_lbl))
        self.play(TransformFromCopy(sin_part, w_res), FadeIn(w_res_lbl), run_time=1.5)

        self.say(
            "The whole residual may also have a wanted component along f0, since rho need not equal lambda0. "
            "That can only make it longer. So the length of r is at least its f1 component, which is at least delta "
            "sin theta. The wrong part of v cannot hide from the residual when the unwanted spectrum is separated. For whole "
            "subspaces this becomes a Sylvester equation, and getting the sharp constant for every unitarily "
            "invariant norm is the technical part of the full theorem."
        )
        self.play(GrowArrow(r_arrow), FadeIn(r_lbl), Create(r_guide), FadeIn(col[2]))
        self.play(FadeIn(col[3]))


# ----------------------------------------------------------------------------
# 9. Many vectors: a Sylvester equation
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# 10. Sharpness
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# 11. Payoff: perturbation bound
# ----------------------------------------------------------------------------


class S11Payoff(DeckSlide):
    title = r"Back to perturbations: where $\sym{H}$ enters"
    kicker = r"\cx{perturb}{PERTURBATION SPECIALIZATION} --- $\sym{Ahat}=\sym{A}+\sym{H}$ and $\sym{A}\sym{E0}=\sym{E0}\sym{A0}$"

    def body(self) -> None:
        eps = story.PERTURBATION_EPS
        g = ValueTracker(story.PERTURBATION_START_GAP)

        def pair() -> story.PerturbedPair:
            return story.PerturbedPair(gap=g.get_value(), eps=eps)

        self.say(
            "Now add the perturbation relationship: A hat equals A plus H. In a statistical application, "
            "A is the latent true matrix and A hat is the observed estimate. E zero is a true eigenframe "
            "of A, even if we do not know it, and F zero is the eigenframe calculated from A hat. "
            "The proof uses A E zero equals E zero A zero, whether or not those objects are observable."
        )
        setup = math(
            r"\sym{Ahat}=\sym{A}+\sym{H},\qquad "
            r"\sym{A}\sym{E0}=\sym{E0}\sym{A0}",
            size=31,
        )
        residual = math(
            r"\sym{R}=\sym{Ahat}\sym{E0}-\sym{E0}\sym{A0}"
            r"=(\sym{A}+\sym{H})\sym{E0}-\sym{E0}\sym{A0}"
            r"=\sym{H}\sym{E0}",
            size=30,
        )
        consequence = boxed(
            math(
                r"\norm{\sym{sinTheta0}(\sym{E0},\sym{F0})}"
                r"\le\frac{\norm{\sym{R}}}{\sym{delta}}"
                r"\le\frac{\norm{\sym{H}}}{\sym{delta}}",
                size=35,
            ),
            color=SINE,
        )
        derivation = VGroup(setup, residual, consequence).arrange(RIGHT, buff=0.42)
        derivation.move_to([0, self.content_top - 0.2, 0], aligned_edge=UP)
        if derivation.width > 13.0:
            derivation.scale(13.0 / derivation.width)

        note = para(
            r"\textbf{Why $\norm{\sym{R}}\le\norm{\sym{H}}$:} $\sym{E0}$ has orthonormal columns, so "
            r"right-multiplying $\sym{H}$ by $\sym{E0}$ cannot increase a unitarily invariant norm. "
            r"Here $\sym{delta}$ separates $\operatorname{spec}(\sym{A0})$ --- the original wanted values --- "
            r"from $\operatorname{spec}(\sym{Lambda1})$, the exact unwanted values of $\sym{Ahat}$.",
            width=12.7,
            size=21,
            color=MUTED,
        ).next_to(derivation, DOWN, buff=0.16)
        self.play(FadeIn(derivation), FadeIn(note))

        plane = Plane([-4.7, -2.02, 0], 0.62, rotate=ELLIPSE_BASE)
        old = always_redraw(lambda: DashedVMobject(ellipse(plane, pair().A, color=OLD, width=2), num_dashes=50))
        new = always_redraw(lambda: ellipse(plane, pair().perturbed, color=CURRENT, width=3))
        old_axis = DashedVMobject(through_origin(plane, [1, 0], 2.3, TRIAL, width=2.5), num_dashes=24)
        new_axis = always_redraw(lambda: through_origin(plane, pair().perturbed_top_eigenvector, 2.0, WANTED, width=4))
        arc = always_redraw(lambda: angle_arc(plane, [1, 0], pair().perturbed_top_eigenvector, 1.35, SINE, width=4))

        axes = Axes(
            x_range=[0, 1.0, 0.25],
            y_range=[0, 1.0, 0.25],
            x_length=4.6,
            y_length=2.15,
            tips=False,
            axis_config={"color": MUTED, "stroke_width": 2},
        ).move_to([3.95, -1.64, 0])
        x_lbl = tex(r"original gap $\sym{g}$ of $\sym{A}$", size=18, color=MUTED).next_to(
            axes, DOWN, buff=0.36
        )
        y_ticks = VGroup(*[math(f"{v:g}", size=20, color=MUTED).next_to(axes.c2p(0, v), LEFT, buff=0.08) for v in (0.5, 1.0)])
        x_ticks = VGroup(*[math(f"{v:g}", size=20, color=MUTED).next_to(axes.c2p(v, 0), DOWN, buff=0.08) for v in (0.5, 1.0)])
        actual = axes.plot(lambda x: story.PerturbedPair(gap=x, eps=eps).sin_theta, x_range=[0.0, 1.0], color=SINE, stroke_width=4)
        bound = DashedVMobject(
            axes.plot(lambda x: story.PerturbedPair(gap=x, eps=eps).bound, x_range=[0.0, 1.0], color=RESID, stroke_width=3),
            num_dashes=45,
        )
        # The theorem's full formula is above. This plot uses a compact legend,
        # keeping label geometry outside the curves and the axis tick labels.
        plot_legend = tex(
            r"\cx{sine}{solid: angle error} \quad \cx{resid}{dashed: bound}",
            size=19,
        ).next_to(axes, UP, buff=0.08)
        d_actual = always_redraw(lambda: Dot(axes.c2p(g.get_value(), pair().sin_theta), color=SINE, radius=0.07))
        d_bound = always_redraw(lambda: Dot(axes.c2p(g.get_value(), pair().bound), color=RESID, radius=0.07))

        self.say(
            "Back to the two by two example with epsilon equals 0.12. The pink curve is the sine of the actual angle between range E0, "
            "the original wanted frame, and range F0, the exact wanted frame of A hat. Green dashed is the "
            "general residual-over-separation bound. The horizontal variable g is a different quantity: the original eigengap of A."
        )
        legend = VGroup(
            tex(r"\cx{old}{dashed: original $\sym{A}$}", size=20),
            tex(r"\cx{trial}{amber: $\operatorname{range}(\sym{E0})$ of $\sym{A}$}", size=20),
            tex(r"\cx{current}{solid: $\sym{Ahat}=\sym{A}+\sym{H}$}", size=20),
            tex(r"\cx{wanted}{blue: $\operatorname{range}(\sym{F0})$ of $\sym{Ahat}$}", size=20),
            tex(r"\cx{sine}{arc: $\Theta_0(\sym{E0},\sym{F0})$}", size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([-2.45, -0.75, 0], aligned_edge=UP + LEFT)
        self.add(old, new, old_axis, new_axis, arc)
        self.play(
            FadeIn(VGroup(old, new, old_axis, new_axis, arc, legend)),
            Create(axes),
            FadeIn(x_lbl, y_ticks, x_ticks),
            Create(actual),
            Create(bound),
            FadeIn(plot_legend),
        )
        self.add(d_actual, d_bound)
        self.play(g.animate.set_value(story.PERTURBATION_END_GAP), run_time=5.0, rate_func=rate_functions.ease_in_out_sine)

        self.say(
            "Keep g and delta separate. Here g compares wanted and unwanted eigenvalues of the original A. "
            "Delta compares spec A0, the old wanted block, with spec Lambda1, the new unwanted block of A hat. "
            "In this example those behave differently as g collapses."
        )
        remark = para(
            r"$\sym{g}$: wanted vs. unwanted spectrum of the original $\sym{A}$.\qquad "
            r"$\sym{delta}$: $\operatorname{spec}(\sym{A0})$ vs. exact unwanted "
            r"$\operatorname{spec}(\sym{Lambda1})$ of $\sym{Ahat}$. "
            r"A certified lower bound on $\sym{delta}$ is enough for the theorem.",
            width=12.6,
            size=21,
            color=MUTED,
        ).next_to(note, DOWN, buff=0.14)
        self.play(FadeIn(remark))


# ----------------------------------------------------------------------------
# 12. What Lean proves
# ----------------------------------------------------------------------------

# The statement exactly as `#check @TauCeti.DavisKahan1970.SectionTwo.sinTheta` prints
# it, with only instance-binder names dropped and the lines re-broken.  Re-check
# after any change to the alias (see the README).
LEAN_SIGNATURE = [
    "theorem TauCeti.DavisKahan1970.SectionTwo.sinTheta",
    "    {𝕜 : Type u_1} [RCLike 𝕜] {E F G H : Type u_2}",
    "    [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E]",
    "    [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F]",
    "    [NormedAddCommGroup G] [InnerProductSpace 𝕜 G] [CompleteSpace G]",
    "    [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]",
    "    [TopologicalSpace.SeparableSpace E]",
    "    (N : TauCeti.DavisKahan.ExactSinTheta.NormalizedSymmetricOperatorIdealFamily 𝕜)",
    "    (A : E →ₗ.[𝕜] E) (A₀ : F →ₗ.[𝕜] F) (Λ₁ : G →ₗ.[𝕜] G)",
    "    (E₀ : F →L[𝕜] E) (F₀ : H →L[𝕜] E) (F₁ : G →L[𝕜] E) (R : F →L[𝕜] E) :",
    "    IsSelfAdjoint A → IsSelfAdjoint A₀ → IsSelfAdjoint Λ₁ →",
    "    TauCeti.DavisKahan1970.IsTrialResidual A A₀ E₀ R →",
    "    TauCeti.DavisKahan1970.IsExactSpectralDecomposition A Λ₁ F₀ F₁ →",
    "    ∀ {δ : ℝ}, 0 < δ →",
    "    TauCeti.DavisKahan.Sylvester.FormBoundedSylvesterGap A₀ Λ₁ δ →",
    "    N.Mem (TauCeti.DavisKahan1970.sourceDirectedSinThetaOperator E₀ F₀) → N.Mem R →",
    "    δ * N.gaugeReal (TauCeti.DavisKahan1970.sourceDirectedSinThetaOperator E₀ F₀)",
    "      ≤ N.gaugeReal R",
]

# (first line, last line, label, colour) for the "reading it" build.
LEAN_READING = [
    (1, 1, r"scalars: $\mathbb{R}$ or $\mathbb{C}$", FG),
    (2, 6, r"separable Hilbert spaces", FG),
    (7, 7, r"every unitarily invariant norm", FG),
    (8, 8, r"possibly unbounded operators", FG),
    (10, 10, r"all self-adjoint", FG),
    (11, 11, r"slides: $\sym{R}=\sym{Ahat}\sym{E0}-\sym{E0}\sym{A0}$", RESID),
    (12, 12, r"slides: $\sym{Ahat}\sym{F1}=\sym{F1}\sym{Lambda1}$", UNWANTED),
    (14, 14, r"spectral separation $\sym{delta}$", GAP),
    (15, 15, r"where the norms are defined", MUTED),
    (16, 17, r"$\sym{delta}\norm{\sym{sinTheta0}(\sym{E0},\sym{F0})}\le\norm{\sym{R}}$", SINE),
]


class S12Lean(DeckSlide):
    title = "What we formalized: the full Lean theorem"
    kicker = r"\cx{muted}{GENERAL THEOREM IN LEAN} --- Lean's $A$ is our $\sym{Ahat}$; $\sym{H}$ is not an input"
    section = ""

    def body(self) -> None:
        size = 14
        probe = Text("M" * 20, font=MONO_FONT, font_size=size)
        char_w = probe.width / 20
        line_h = 0.275
        x0, top = -6.75, self.content_top - 0.15
        lines = VGroup()
        for i, raw in enumerate(LEAN_SIGNATURE):
            indent = len(raw) - len(raw.lstrip(" "))
            t = Text(raw.strip(), font=MONO_FONT, font_size=size, color=FG)
            t.move_to([x0 + indent * char_w, top - i * line_h, 0], aligned_edge=LEFT)
            lines.add(t)
        right_edge = 2.95
        if lines.get_right()[0] > right_edge:
            lines.scale((right_edge - x0) / (lines.get_right()[0] - x0), about_point=[x0, top, 0])
        bg = Rectangle(
            width=lines.width + 0.4, height=lines.height + 0.35, fill_color=PANEL, fill_opacity=1, stroke_width=0
        ).move_to(lines)
        caption = para(
            r"The theorem statement, with instance-binder names dropped and lines re-broken; "
            r"$\sin\Theta_0$ is \texttt{sourceDirectedSinThetaOperator E$_0$ F$_0$}. "
            r"\textbf{Notation translation:} Lean's \texttt{A} is this talk's $\sym{Ahat}$. "
            r"The talk's original $\sym{A}$ and perturbation $\sym{H}$ exist only in the perturbation specialization.",
            width=13.3,
            size=19,
            color=MUTED,
        ).next_to(bg, DOWN, aligned_edge=LEFT, buff=0.1)

        self.say(
            "This is the actual Lean statement of the sin Theta theorem, complete. Nobody should read it "
            "token by token; the point is that this is the real object the proof checker accepted."
        )
        self.play(FadeIn(bg), FadeIn(lines, lag_ratio=0.03), FadeIn(caption))

        self.say(
            "Reading it: real or complex scalars; separable Hilbert spaces, finite- or infinite-dimensional; every "
            "unitarily invariant norm; possibly unbounded self-adjoint operators; the paper's residual, "
            "spectral decomposition and separation; and the conclusion delta times the norm of sin Theta0 of E0 and F0 at most the norm of R. "
            "The highlighted labels translate Lean's ambient A into the talk's A hat without changing the Lean source text."
        )
        highlights, labels = VGroup(), VGroup()
        for first, last, label, color in LEAN_READING:
            block = VGroup(*lines[first : last + 1])
            box = Rectangle(
                width=block.width + 0.14, height=block.height + 0.1, stroke_color=color, stroke_width=1.6
            ).move_to(block)
            lab = tex(label, size=21, color=color)
            lab.move_to([right_edge + 0.35, block.get_center()[1], 0], aligned_edge=LEFT)
            fit_right(lab)
            highlights.add(box)
            labels.add(lab)
        highlighted = {i for first, last, _, _ in LEAN_READING for i in range(first, last + 1)}
        dim = [line.animate.set_opacity(0.4) for i, line in enumerate(lines) if i not in highlighted and i != 0]
        self.play(*dim, FadeIn(highlights, lag_ratio=0.1), FadeIn(labels, lag_ratio=0.1), run_time=1.6)


# ----------------------------------------------------------------------------
# 13. The family
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# 14. Summary
# ----------------------------------------------------------------------------


class S14Summary(DeckSlide):
    title = "What to take away"
    kicker = "Three lessons from a source-faithful formalization"

    def body(self) -> None:
        # A compact conclusion, with the mathematical qualifications carried
        # through in the text instead of hidden behind a generic success count.
        items = [
            (
                "1",
                r"LLMs can formalize substantial mathematics",
                r"Of the \textbf{29} counted result statements in Davis--Kahan (1970), "
                r"\textbf{28 are formalized in Lean}; the remaining proposition was "
                r"refuted as printed and repaired. This is Hilbert-space functional analysis, "
                r"including infinite-dimensional and unbounded operators.",
            ),
            (
                "2",
                r"Sine-theta gives an error bound",
                r"When the trial eigenvalues are separated from the unwanted exact eigenvalues "
                r"by $\sym{delta}>0$, the \textbf{subspace error is at most the residual "
                r"norm divided by that separation}: "
                r"$\norm{\sym{sinTheta0}(\sym{E0},\sym{F0})}"
                r"\le\norm{\sym{R}}/\sym{delta}$. "
                r"This limits how far the trial eigenspace can deviate, even if the exact one is unknown.",
            ),
            (
                "3",
                r"A classical statement was too broad",
                r"LLM-assisted review found a counterexample to Proposition~4.4's claim "
                r"for \emph{every} unitarily invariant norm. The impact is limited: "
                r"direct rotation is still optimal for acute pairs and \textbf{$Q$-norms} "
                r"(including operator and Frobenius norms), over $\mathbb{R}$ or $\mathbb{C}$, "
                r"without the paper's $60^\circ$ cutoff.",
            ),
        ]
        rows = VGroup()
        for number, headline, details in items:
            n = tex(number, size=52, color=MUTED)
            head = tex(r"\textbf{" + headline + "}", size=28, color=FG)
            body = para(details, width=11.1, size=24)
            block = VGroup(head, body).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            rows.add(VGroup(n, block).arrange(RIGHT, aligned_edge=UP, buff=0.34))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        # Keep all three takeaways above the deck footer on both themes.
        max_height = self.content_top + 2.90
        if rows.height > max_height:
            rows.scale_to_fit_height(max_height)
        if rows.width > 12.55:
            rows.scale_to_fit_width(12.55)
        rows.move_to([-6.30, self.content_top - 0.18, 0], aligned_edge=UP + LEFT)
        self.say(
            "Three takeaways. First, this was a substantial LLM-assisted formalization: "
            "the explicit inventory contains twenty-nine Davis-Kahan results. "
            "Lean proves twenty-eight at source scope. The remaining printed Proposition four point four "
            "is false and has a checked counterexample and repair. The work is functional analysis "
            "in Hilbert spaces, not just finite matrices. Second, the intuition for sine theta is "
            "that a perturbation only gives a useful guarantee when the trial eigenvalues "
            "are separated from the exact unwanted eigenvalues. The error in the eigenspace "
            "is at most the residual norm divided by that positive spectral separation, "
            "and can even certify closeness to an underlying true "
            "eigenspace whose vectors are unknown. Third, the agent-assisted search "
            "found a counterexample to a claim in a classical, widely cited paper. "
            "The consequence is limited: the failure is of the universal choice of "
            "unitarily invariant norm. The direct rotation remains optimal for "
            "Q norms, including operator and Frobenius norms, for acute pairs "
            "over real or complex spaces, without the claimed sixty-degree threshold. "
            "An application genuinely requiring every unitarily invariant norm "
            "would have to confront that invalid generalization."
        )
        # Complete static content is available in the handout.
        self.add(rows)
