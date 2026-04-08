"""Generated component: UserJoinAudioIndicator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserJoinAudioIndicator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserJoinAudioIndicator.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserJoinAudioIndicator"

    def __init__(self, spatialize: bool | None = None, volume: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            spatialize: Initial value for Spatialize.
            volume: Initial value for Volume.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if spatialize is not None:
            self.spatialize = spatialize
        if volume is not None:
            self.volume = volume

    @property
    def joined_clips(self) -> members.SyncList | None:
        """The JoinedClips member."""
        member = self.get_member("JoinedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @joined_clips.setter
    def joined_clips(self, value: members.SyncList) -> None:
        """Set the JoinedClips member."""
        self.set_member("JoinedClips", value)

    @property
    def left_clips(self) -> members.SyncList | None:
        """The LeftClips member."""
        member = self.get_member("LeftClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @left_clips.setter
    def left_clips(self, value: members.SyncList) -> None:
        """Set the LeftClips member."""
        self.set_member("LeftClips", value)

    @property
    def spatialize(self) -> bool | None:
        """The Spatialize field value."""
        member = self.get_member("Spatialize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialize.setter
    def spatialize(self, value: bool) -> None:
        """Set the Spatialize field value."""
        member = self.get_member("Spatialize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Spatialize", fields.FieldBool(value=value)
            )

    @property
    def volume(self) -> np.float32 | None:
        """The Volume field value."""
        member = self.get_member("Volume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume.setter
    def volume(self, value: np.float32) -> None:
        """Set the Volume field value."""
        member = self.get_member("Volume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Volume", fields.FieldFloat(value=value)
            )

