from django.utils.translation import gettext_lazy as _

EASY_INTERVALS = [
    ('1', _('Unison')),
    ('3m', _('Minor Third')),
    ('3M', _('Major Third')),
    ('4', _('Perfect Fourth')),
    ('5', _('Perfect Fifth')),
    ('8', _('Octave')),
]

MEDIUM_INTERVALS = sorted(EASY_INTERVALS + [
    ('6m', _('Minor Sixth')),
    ('6M', _('Major Sixth')),
])

HARD_INTERVALS = sorted(MEDIUM_INTERVALS + [
    ('4Aum', _('Augmented Fourth')),
    ('5Dim', _('Diminished Fourth')),
    ('5Aum', _('Augmented Fourth')),
    ('7m', _('Minor Seventh')),
    ('7M', _('Major Seventh')),
])

DIFICULTY_CHOICES = (
    (_('easy'), _('easy')),
    (_('medium'), _('medium')),
    (_('hard'), _('hard')),
)
