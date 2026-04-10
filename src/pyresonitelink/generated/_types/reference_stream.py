"""Generated type: ReferenceStream."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.implicit_stream import ImplicitStream
from pyresonitelink.generated._types.iworld_element import IWorldElement

T = TypeVar('T')


class ReferenceStream(ImplicitStream, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.ReferenceStream<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ReferenceStream<>"

