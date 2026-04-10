"""Generated type: MultiValueStream."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.value_stream_base import ValueStreamBase

T = TypeVar('T')


class MultiValueStream(ValueStreamBase, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.MultiValueStream<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.MultiValueStream<>"

