"""Narrated sine-theta lecture with a stable authored scene sequence."""
from dkvis.deck_spec import DeckSpec,uses
from dkvis.lectures import lecture_path
from dkvis.quiz import quiz_uses

SINE_THETA_LECTURE=DeckSpec(
    name='sine-theta-lecture',
    description='The short sine-theta visuals with authored narration and study questions.',
    footer='Davis–Kahan sine theta: residuals and spectral separation',
    narration=lecture_path('sine_theta'),
    slides=uses('dkvis.learning.sine_theta.scenes', (
        'S00TitleShort',
        'S00bSetting',
        'S01Ellipse',
        'S02Perturb',
        'S03bWanted',
        'S03NoGap',
        'S03cUnstable',
        'S04Angle',
        'S05Residual',
        'S06Gap',
        'S07Theorem',
        'S08Why',
        'S11Payoff',
        'D01Planes',
        'S12Lean',
        'P01Claim',
        'P02Counterexample',
        'S14Summary',
    ))+quiz_uses(),
)
