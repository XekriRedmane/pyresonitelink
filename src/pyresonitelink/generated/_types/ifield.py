"""Generated type: IField."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IField(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.IField<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.IField<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

