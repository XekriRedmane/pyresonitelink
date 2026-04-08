"""Generated component: UnresolvedReferences."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnresolvedReferences(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UnresolvedReferences.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UnresolvedReferences"

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

