"""Generated component: TypeDictionary."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeDictionary(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TypeDictionary<>.

    Category: Data

    Parameterize with a value type::

        TypeDictionary[primitives.Float]
        TypeDictionary[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TypeDictionary<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.TypeDictionary<>"

    @property
    def types(self) -> members.SyncDictionary | None:
        """The Types member."""
        member = self.get_member("Types")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @types.setter
    def types(self, value: members.SyncDictionary) -> None:
        """Set the Types member."""
        self.set_member("Types", value)

