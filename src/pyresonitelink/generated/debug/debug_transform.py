"""Generated component: DebugTransform."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugTransform(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugTransform component is used to show the parent hiearchy of a slot in the form of text to a specific ``ShowToUser``.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugTransform"

    @property
    def show_to_user(self) -> members.SyncObject | None:
        """Shows the debug visual to this user only."""
        member = self.get_member("ShowToUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @show_to_user.setter
    def show_to_user(self, value: members.SyncObject) -> None:
        """Set ShowToUser. Shows the debug visual to this user only."""
        self.set_member("ShowToUser", value)

