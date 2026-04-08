"""Generated component: UndoListRoot."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UndoListRoot(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Undo.UndoListRoot.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.UndoListRoot"

    @property
    def owner_user(self) -> members.SyncObject | None:
        """The OwnerUser member."""
        member = self.get_member("OwnerUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @owner_user.setter
    def owner_user(self, value: members.SyncObject) -> None:
        """Set the OwnerUser member."""
        self.set_member("OwnerUser", value)

