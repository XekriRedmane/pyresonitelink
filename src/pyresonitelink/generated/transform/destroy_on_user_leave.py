"""Generated component: DestroyOnUserLeave."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyOnUserLeave(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DestroyOnUserLeave.

    Category: Transform
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyOnUserLeave"

    @property
    def target_user(self) -> members.SyncObject | None:
        """The TargetUser member."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_user.setter
    def target_user(self, value: members.SyncObject) -> None:
        """Set the TargetUser member."""
        self.set_member("TargetUser", value)

