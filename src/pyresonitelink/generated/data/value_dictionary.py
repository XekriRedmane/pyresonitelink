"""Generated component: ValueDictionary."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueDictionary(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueDictionary<,>.

    Category: Data
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueDictionary<,>"

    @property
    def values(self) -> members.SyncDictionary | None:
        """The Values member."""
        member = self.get_member("Values")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @values.setter
    def values(self, value: members.SyncDictionary) -> None:
        """Set the Values member."""
        self.set_member("Values", value)

