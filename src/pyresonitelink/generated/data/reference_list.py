"""Generated component: ReferenceList."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceList(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceList<>.

    Category: Data

    Parameterize with a value type::

        ReferenceList[primitives.Float]
        ReferenceList[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceList<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceList<>"

    @property
    def references(self) -> members.SyncList | None:
        """The References member."""
        member = self.get_member("References")
        if isinstance(member, members.SyncList):
            return member
        return None

    @references.setter
    def references(self, value: members.SyncList) -> None:
        """Set the References member."""
        self.set_member("References", value)

