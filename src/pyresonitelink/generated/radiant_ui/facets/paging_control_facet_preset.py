"""Generated component: PagingControlFacetPreset."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.paging_control import PagingControl
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PagingControlFacetPreset(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PagingControlFacetPreset.

    Category: Radiant UI/Facets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PagingControlFacetPreset"

    def __init__(self, paging_control: str | PagingControl | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            paging_control: Initial value for _pagingControl.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if paging_control is not None:
            self.paging_control = paging_control

    @property
    def paging_control(self) -> str | None:
        """Target ID of the _pagingControl reference (targets PagingControl)."""
        member = self.get_member("_pagingControl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @paging_control.setter
    def paging_control(self, target: str | PagingControl | None) -> None:
        """Set the _pagingControl reference by target ID or PagingControl instance."""
        target_id: str | None = target.id if isinstance(target, PagingControl) else target  # type: ignore[assignment]
        member = self.get_member("_pagingControl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pagingControl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PagingControl'),
            )

