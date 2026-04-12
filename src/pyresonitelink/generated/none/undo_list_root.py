"""Generated component: UndoListRoot."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UndoListRoot(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UndoListRoot component acts as a marker for a particular user's undo actions list. For more information on undos, see Undo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.UndoListRoot"

    @property
    def owner_user(self) -> members.SyncObject | None:
        """the owner of this undo list."""
        member = self.get_member("OwnerUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @owner_user.setter
    def owner_user(self, value: members.SyncObject) -> None:
        """Set OwnerUser. the owner of this undo list."""
        self.set_member("OwnerUser", value)

