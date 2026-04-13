"""Generated enum: StencilOperation."""

from enum import StrEnum


class StencilOperation(StrEnum):
    """Enum: [FrooxEngine]FrooxEngine.StencilOperation."""

    keep = "Keep"
    zero = "Zero"
    replace_ = "Replace"
    increment_saturate = "IncrementSaturate"
    decrement_saturate = "DecrementSaturate"
    invert = "Invert"
    increment_wrap = "IncrementWrap"
    decrement_wrap = "DecrementWrap"

