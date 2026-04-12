"""Generated component: LocomotionAnimationConfiguration."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationConfiguration(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LocomotionAnimationConfiguration component is used to customize the user's locomotion animations using a list of gaits and a global settings menu as well.

    Category: Users/Common Avatar System/Animation

    Can be used to customize the user's procedural animations when walking.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationConfiguration"

    @property
    def global_parameters(self) -> members.SyncObject | None:
        """The settings to use for all gaits regardless of user speed."""
        member = self.get_member("GlobalParameters")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @global_parameters.setter
    def global_parameters(self, value: members.SyncObject) -> None:
        """Set GlobalParameters. The settings to use for all gaits regardless of user speed."""
        self.set_member("GlobalParameters", value)

    @property
    def gaits(self) -> members.SyncList | None:
        """The list of gaits to use at different speeds of user movement."""
        member = self.get_member("Gaits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @gaits.setter
    def gaits(self, value: members.SyncList) -> None:
        """Set Gaits. The list of gaits to use at different speeds of user movement."""
        self.set_member("Gaits", value)

