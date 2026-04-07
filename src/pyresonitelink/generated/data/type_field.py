"""Generated component: TypeField."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeField(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TypeField.

    Category: Data
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TypeField"

    @property
    def type_(self) -> members.Member | None:
        """The Type member."""
        member = self.get_member("Type")
        if isinstance(member, members.Member):
            return member
        return None

    @type_.setter
    def type_(self, value: members.Member) -> None:
        """Set the Type member."""
        self.set_member("Type", value)

