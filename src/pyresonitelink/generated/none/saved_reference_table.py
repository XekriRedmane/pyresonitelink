"""Generated component: SavedReferenceTable."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SavedReferenceTable(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Used solely by SpawnOrDestroy to store the data of a destroyed object to restore later.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SavedReferenceTable"

    @property
    def table(self) -> members.SyncDictionary | None:
        """The table to save destroyed object data."""
        member = self.get_member("Table")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @table.setter
    def table(self, value: members.SyncDictionary) -> None:
        """Set Table. The table to save destroyed object data."""
        self.set_member("Table", value)

