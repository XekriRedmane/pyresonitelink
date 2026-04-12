"""Generated component: DestroyOnUserLeave."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyOnUserLeave(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DestroyOnUserLeave component causes the parent slot to be deleted when the user specified in ``User`` leaves the world.

    Category: Transform

    **Behavior**: == Examples ==
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyOnUserLeave"

    @property
    def target_user(self) -> members.SyncObject | None:
        """The user that will cause the parent slot to be deleted upon leaving"""
        member = self.get_member("TargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_user.setter
    def target_user(self, value: members.SyncObject) -> None:
        """Set TargetUser. The user that will cause the parent slot to be deleted upon leaving"""
        self.set_member("TargetUser", value)

