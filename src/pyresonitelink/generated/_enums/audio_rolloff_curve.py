"""Generated enum: AudioRolloffCurve."""

from enum import StrEnum


class AudioRolloffCurve(StrEnum):
    """Enum: [Awwdio]Awwdio.AudioRolloffCurve."""

    logarithmic_infinite = "LogarithmicInfinite"
    logarithmic = "Logarithmic"
    logarithmic_clamped = "LogarithmicClamped"
    logarithmic_fade_off = "LogarithmicFadeOff"
    linear = "Linear"

