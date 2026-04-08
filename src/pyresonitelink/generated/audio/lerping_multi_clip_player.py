"""Generated component: LerpingMultiClipPlayer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LerpingMultiClipPlayer(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LerpingMultiClipPlayer.

    Category: Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LerpingMultiClipPlayer"

    def __init__(self, lerp: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            lerp: Initial value for Lerp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if lerp is not None:
            self.lerp = lerp

    @property
    def lerp(self) -> np.float32 | None:
        """The Lerp field value."""
        member = self.get_member("Lerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp.setter
    def lerp(self, value: np.float32) -> None:
        """Set the Lerp field value."""
        member = self.get_member("Lerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Lerp", fields.FieldFloat(value=value)
            )

    @property
    def tracks(self) -> members.SyncList | None:
        """The Tracks member."""
        member = self.get_member("Tracks")
        if isinstance(member, members.SyncList):
            return member
        return None

    @tracks.setter
    def tracks(self, value: members.SyncList) -> None:
        """Set the Tracks member."""
        self.set_member("Tracks", value)

