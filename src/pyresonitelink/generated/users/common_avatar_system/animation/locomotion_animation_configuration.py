"""Generated component: LocomotionAnimationConfiguration."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationConfiguration(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocomotionAnimationConfiguration.

    Category: Users/Common Avatar System/Animation
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationConfiguration"

    @property
    def global_parameters(self) -> members.SyncObject | None:
        """The GlobalParameters member."""
        member = self.get_member("GlobalParameters")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @global_parameters.setter
    def global_parameters(self, value: members.SyncObject) -> None:
        """Set the GlobalParameters member."""
        self.set_member("GlobalParameters", value)

    @property
    def gaits(self) -> members.SyncList | None:
        """The Gaits member."""
        member = self.get_member("Gaits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @gaits.setter
    def gaits(self, value: members.SyncList) -> None:
        """Set the Gaits member."""
        self.set_member("Gaits", value)

