"""Generated component: AlwaysOnFacetModule."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AlwaysOnFacetModule(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AlwaysOnFacetModule.

    Category: Radiant UI/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AlwaysOnFacetModule"

    @property
    def targets(self) -> members.SyncList | None:
        """The _targets member."""
        member = self.get_member("_targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set the _targets member."""
        self.set_member("_targets", value)

