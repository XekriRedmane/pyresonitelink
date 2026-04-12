"""Generated component: ReferenceList."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceList(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The Reference List`1 component acts as a way to store a list of references as a stand alone component. like a ReferenceField, but for a list of items of the same type.

This component does not provide a way to index through its items. If you need this functionality, consider using a ReferenceMultiplexer Instead.

    Category: Data

    Can be used with Spatial variables.

    Parameterize with a value type::

        ReferenceList[primitives.Float]
        ReferenceList[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceList<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceList<>"

    @property
    def references(self) -> members.SyncList | None:
        """The stored reference list."""
        member = self.get_member("References")
        if isinstance(member, members.SyncList):
            return member
        return None

    @references.setter
    def references(self, value: members.SyncList) -> None:
        """Set References. The stored reference list."""
        self.set_member("References", value)

