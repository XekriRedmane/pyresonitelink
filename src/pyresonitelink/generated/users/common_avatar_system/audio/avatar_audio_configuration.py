"""Generated component: AvatarAudioConfiguration."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAudioConfiguration(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Avatar Audio Configuration is a component that allows for overriding Avatar Audio Output Manager voice configs in worlds using user injection.

    Category: Users/Common Avatar System/Audio

    attach this component as part of the hierarchy of a slot that is put
    into ``AutoInject`` on a Common Avatar Builder Component on the world
    root. When the component is injected, it will auto fill itself into the
    ``_audioConfiguration`` of the user's Avatar Audio Output Manager and
    allow for overriding the user's audio config.

    **Related Components**: * For how world injected modules work (which said injected slot can contain this component) see Common Avatar Builder Component
* For the component this overrides for user voices, see Avatar Audio Output Manager.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarAudioConfiguration"

    @property
    def normal(self) -> members.SyncObject | None:
        """The settings to override ``NormalConfig`` on an Avatar Audio Output Manager with."""
        member = self.get_member("Normal")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @normal.setter
    def normal(self, value: members.SyncObject) -> None:
        """Set Normal. The settings to override ``NormalConfig`` on an Avatar Audio Output Manager with."""
        self.set_member("Normal", value)

    @property
    def shout(self) -> members.SyncObject | None:
        """The settings to override ``ShoutConfig`` on an Avatar Audio Output Manager with."""
        member = self.get_member("Shout")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @shout.setter
    def shout(self, value: members.SyncObject) -> None:
        """Set Shout. The settings to override ``ShoutConfig`` on an Avatar Audio Output Manager with."""
        self.set_member("Shout", value)

    @property
    def broadcast(self) -> members.SyncObject | None:
        """The settings to override ``BroadcastConfig`` on an Avatar Audio Output Manager with."""
        member = self.get_member("Broadcast")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @broadcast.setter
    def broadcast(self, value: members.SyncObject) -> None:
        """Set Broadcast. The settings to override ``BroadcastConfig`` on an Avatar Audio Output Manager with."""
        self.set_member("Broadcast", value)

