"""Generated component: SearchBarFacetPreset."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.radiant_search_bar import RadiantSearchBar
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SearchBarFacetPreset(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SearchBarFacetPreset.

    Category: Radiant UI/Facets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SearchBarFacetPreset"

    def __init__(self, search_bar: str | RadiantSearchBar | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            search_bar: Initial value for _searchBar.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if search_bar is not None:
            self.search_bar = search_bar

    @property
    def search_bar(self) -> str | None:
        """Target ID of the _searchBar reference (targets RadiantSearchBar)."""
        member = self.get_member("_searchBar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @search_bar.setter
    def search_bar(self, target: str | RadiantSearchBar | None) -> None:
        """Set the _searchBar reference by target ID or RadiantSearchBar instance."""
        target_id: str | None = target.id if isinstance(target, RadiantSearchBar) else target  # type: ignore[assignment]
        member = self.get_member("_searchBar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_searchBar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RadiantSearchBar'),
            )

