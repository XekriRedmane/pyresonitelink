"""Generated component: ObjectScroller."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectScroller(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ObjectScroller component acts as a way to scroll a list of items with sizes by offsetting them within a region they should appear within. Objects outside of the region get disabled until the ``Offset`` allows them to appear within it again.

    Category: Transform/Drivers

    Attach to a slot and add/setup ``Items`` entries to begin use.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ObjectScroller"

    def __init__(self, offset: primitives.Float3 | None = None, region_size: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            region_size: Initial value for RegionSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset
        if region_size is not None:
            self.region_size = region_size

    @property
    def items(self) -> members.SyncList | None:
        """A list of items to move and activate/deactivate if they are within/outside of the ``RegionSize``"""
        member = self.get_member("Items")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items.setter
    def items(self, value: members.SyncList) -> None:
        """Set Items. A list of items to move and activate/deactivate if they are within/outside of the ``RegionSize``"""
        self.set_member("Items", value)

    @property
    def offset(self) -> primitives.Float3 | None:
        """How much to offset the positions of ``Items`` in order to scroll them."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def region_size(self) -> primitives.Float3 | None:
        """The size area objects have to be touching from their current position and size after ``Offset`` is applied in order to stay visible."""
        member = self.get_member("RegionSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @region_size.setter
    def region_size(self, value: primitives.Float3) -> None:
        """Set the RegionSize field value."""
        member = self.get_member("RegionSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RegionSize", fields.FieldFloat3(value=value)
            )

