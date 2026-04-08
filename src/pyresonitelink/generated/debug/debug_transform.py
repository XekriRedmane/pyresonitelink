"""Generated component: DebugTransform."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugTransform(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugTransform.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugTransform"

    @property
    def show_to_user(self) -> members.SyncObject | None:
        """The ShowToUser member."""
        member = self.get_member("ShowToUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @show_to_user.setter
    def show_to_user(self, value: members.SyncObject) -> None:
        """Set the ShowToUser member."""
        self.set_member("ShowToUser", value)

