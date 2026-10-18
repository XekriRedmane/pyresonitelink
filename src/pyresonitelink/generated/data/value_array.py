"""Generated component: ValueArray."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueArray(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueArray<>.

    Category: Data

    Parameterize with a value type::

        ValueArray[primitives.Float]
        ValueArray[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueArray<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueArray<>"

    @property
    def values(self) -> members.Member | None:
        """The Values member."""
        member = self.get_member("Values")
        if isinstance(member, members.Member):
            return member
        return None

    @values.setter
    def values(self, value: members.Member) -> None:
        """Set the Values member."""
        self.set_member("Values", value)

