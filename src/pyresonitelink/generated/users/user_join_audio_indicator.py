"""Generated component: UserJoinAudioIndicator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserJoinAudioIndicator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserJoinAudioIndicator component plays an audio clip when a user joins and leaves a session.

    Category: Users

    Attach to a slot and provide some audio clips to play. The next time a
    user joins or leaves the session, a clip from the corresponding list
    will play.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserJoinAudioIndicator"

    def __init__(self, spatialize: primitives.Bool | None = None, volume: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
        """A list of random audio clips to choose from when a user joins the session. Each one will have a different weight."""
        member = self.get_member("JoinedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @joined_clips.setter
    def joined_clips(self, value: members.SyncList) -> None:
        """Set JoinedClips. A list of random audio clips to choose from when a user joins the session. Each one will have a different weight."""
        self.set_member("JoinedClips", value)

    @property
    def left_clips(self) -> members.SyncList | None:
        """A list of random audio clips to choose from when a user leaves the session. Each one will have a different weight."""
        member = self.get_member("LeftClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @left_clips.setter
    def left_clips(self, value: members.SyncList) -> None:
        """Set LeftClips. A list of random audio clips to choose from when a user leaves the session. Each one will have a different weight."""
        self.set_member("LeftClips", value)

    @property
    def spatialize(self) -> primitives.Bool | None:
        """Whether to play the sounds from the slot this component is on or globally."""
        member = self.get_member("Spatialize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialize.setter
    def spatialize(self, value: primitives.Bool) -> None:
        """Set the Spatialize field value."""
        member = self.get_member("Spatialize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Spatialize", fields.FieldBool(value=value)
            )

    @property
    def volume(self) -> primitives.Float | None:
        """How loud the audio clips should be by default."""
        member = self.get_member("Volume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume.setter
    def volume(self, value: primitives.Float) -> None:
        """Set the Volume field value."""
        member = self.get_member("Volume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Volume", fields.FieldFloat(value=value)
            )

