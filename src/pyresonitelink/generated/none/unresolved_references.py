"""Generated component: UnresolvedReferences."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnresolvedReferences(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UnresolvedReferences component is internal to FrooxEngine and is found usually on a world root. It is used to store references that are unresolved by the load controller of the game for that world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UnresolvedReferences"

    @property
    def references(self) -> members.SyncList | None:
        """A list of references to keep a storage for."""
        member = self.get_member("References")
        if isinstance(member, members.SyncList):
            return member
        return None

    @references.setter
    def references(self, value: members.SyncList) -> None:
        """Set References. A list of references to keep a storage for."""
        self.set_member("References", value)

