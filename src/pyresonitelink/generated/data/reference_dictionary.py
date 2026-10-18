"""Generated component: ReferenceDictionary."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceDictionary(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceDictionary<,>.

    Category: Data
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceDictionary<,>"

    @property
    def references(self) -> members.SyncDictionary | None:
        """The References member."""
        member = self.get_member("References")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @references.setter
    def references(self, value: members.SyncDictionary) -> None:
        """Set the References member."""
        self.set_member("References", value)

