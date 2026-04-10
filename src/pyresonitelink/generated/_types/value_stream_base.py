"""Generated type: ValueStreamBase."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.implicit_stream import ImplicitStream

T = TypeVar('T')


class ValueStreamBase(ImplicitStream, Generic[T]):
    """Abstract class: [FrooxEngine]FrooxEngine.ValueStreamBase<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ValueStreamBase<>"

