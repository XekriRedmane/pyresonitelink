"""Generated component: AvatarAudioConfiguration."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAudioConfiguration(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AvatarAudioConfiguration.

    Category: Users/Common Avatar System/Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarAudioConfiguration"

    @property
    def normal(self) -> members.SyncObject | None:
        """The Normal member."""
        member = self.get_member("Normal")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @normal.setter
    def normal(self, value: members.SyncObject) -> None:
        """Set the Normal member."""
        self.set_member("Normal", value)

    @property
    def shout(self) -> members.SyncObject | None:
        """The Shout member."""
        member = self.get_member("Shout")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @shout.setter
    def shout(self, value: members.SyncObject) -> None:
        """Set the Shout member."""
        self.set_member("Shout", value)

    @property
    def broadcast(self) -> members.SyncObject | None:
        """The Broadcast member."""
        member = self.get_member("Broadcast")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @broadcast.setter
    def broadcast(self, value: members.SyncObject) -> None:
        """Set the Broadcast member."""
        self.set_member("Broadcast", value)

