"""Generated component: SavedReferenceTable."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SavedReferenceTable(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SavedReferenceTable.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SavedReferenceTable"

    @property
    def table(self) -> members.SyncDictionary | None:
        """The Table member."""
        member = self.get_member("Table")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @table.setter
    def table(self, value: members.SyncDictionary) -> None:
        """Set the Table member."""
        self.set_member("Table", value)

