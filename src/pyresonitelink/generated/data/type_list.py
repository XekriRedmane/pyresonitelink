"""Generated component: TypeList."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeList(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TypeList.

    Category: Data
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TypeList"

    @property
    def types(self) -> members.SyncList | None:
        """The Types member."""
        member = self.get_member("Types")
        if isinstance(member, members.SyncList):
            return member
        return None

    @types.setter
    def types(self, value: members.SyncList) -> None:
        """Set the Types member."""
        self.set_member("Types", value)

