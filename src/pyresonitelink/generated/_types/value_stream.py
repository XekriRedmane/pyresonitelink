"""Generated type: ValueStream."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.value_stream_base import ValueStreamBase
from pyresonitelink.generated._types.ivalue import IValue

T = TypeVar('T')


class ValueStream(ValueStreamBase, IValue, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.ValueStream<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ValueStream<>"

