"""Generated type: IAudioSample."""

from typing import Generic, TypeVar

S = TypeVar('S')


class IAudioSample(Generic[S]):
    """Interface: [Elements.Assets]Elements.Assets.IAudioSample<>."""

    RESONITE_TYPE: str = "[Elements.Assets]Elements.Assets.IAudioSample<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

