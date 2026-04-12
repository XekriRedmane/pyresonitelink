"""Generated component: AlwaysOnFacetModule."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AlwaysOnFacetModule(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AlwaysOnFacetModule component allows apart of a facet to remain active while the dashboard is closed.

    Category: Radiant UI/Utility

    **Behavior**: This component only applies to Facets.

When a Facets is installed in a dashboard, all of the children of a slot containing a AlwaysOnFacetModule are reparented to a Slot outside of the dashboard. This slot is active when the dashboard is closed, otherwise the facet is inactive due to being under an inactive Slot.

Do not manually modify the _targets list, as it is managed during the normal lifetime of the component. Manually modifying the list may cause unexpected behavior.

This will change the hierarchy of the Facets, if you rely on your facet using dynamic variables they may disconnect due to reparenting (many parts of facets are re-parented, be warned).

Avoid putting this above the UIX elements of the Facets, as it will reparent them and they will no longer show up or may break the canvas.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AlwaysOnFacetModule"

    @property
    def targets(self) -> members.SyncList | None:
        """A list of Slots that should remain active when the dash is closed."""
        member = self.get_member("_targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set _targets. A list of Slots that should remain active when the dash is closed."""
        self.set_member("_targets", value)

