"""Generated component: ArcLayout."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.direction import Direction
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ArcLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """The ArcLayout is a component primarily used in a user's context menu. It requires a set of slots under the slot the component is attached to, and each slot needs an OutlinedArc Component and an ArcSegmentLayout Component.

    Category: UIX/Layout

    **Related Components**: * ArcSegmentLayout
* OutlinedArc
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ArcLayout"

    def __init__(self, arc: primitives.Float | None = None, offset: primitives.Float | None = None, separation: primitives.Float | None = None, center_at_separation: primitives.Bool | None = None, proportional_size: primitives.Bool | None = None, item_direction: Direction | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            arc: Initial value for Arc.
            offset: Initial value for Offset.
            separation: Initial value for Separation.
            center_at_separation: Initial value for CenterAtSeparation.
            proportional_size: Initial value for ProportionalSize.
            item_direction: Initial value for ItemDirection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if arc is not None:
            self.arc = arc
        if offset is not None:
            self.offset = offset
        if separation is not None:
            self.separation = separation
        if center_at_separation is not None:
            self.center_at_separation = center_at_separation
        if proportional_size is not None:
            self.proportional_size = proportional_size
        if item_direction is not None:
            self.item_direction = item_direction

    @property
    def arc(self) -> primitives.Float | None:
        """The amount of the circle in degrees to cover with the arc elements."""
        member = self.get_member("Arc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc.setter
    def arc(self, value: primitives.Float) -> None:
        """Set the Arc field value."""
        member = self.get_member("Arc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Arc", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> primitives.Float | None:
        """the amount to rotate the arc elements around the center in degrees from the default position."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    @property
    def separation(self) -> primitives.Float | None:
        """how much to separate the elements from each other."""
        member = self.get_member("Separation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separation.setter
    def separation(self, value: primitives.Float) -> None:
        """Set the Separation field value."""
        member = self.get_member("Separation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Separation", fields.FieldFloat(value=value)
            )

    @property
    def center_at_separation(self) -> primitives.Bool | None:
        """Centers the separation point of this layout."""
        member = self.get_member("CenterAtSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @center_at_separation.setter
    def center_at_separation(self, value: primitives.Bool) -> None:
        """Set the CenterAtSeparation field value."""
        member = self.get_member("CenterAtSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CenterAtSeparation", fields.FieldBool(value=value)
            )

    @property
    def proportional_size(self) -> primitives.Bool | None:
        """Keep all segments of the arc proportional in size."""
        member = self.get_member("ProportionalSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @proportional_size.setter
    def proportional_size(self, value: primitives.Bool) -> None:
        """Set the ProportionalSize field value."""
        member = self.get_member("ProportionalSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProportionalSize", fields.FieldBool(value=value)
            )

    @property
    def item_direction(self) -> Direction | None:
        """How to arrange the elements in order from the initial position."""
        member = self.get_member("ItemDirection")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Direction(member.value)
        return None

    @item_direction.setter
    def item_direction(self, value: Direction | str) -> None:
        """Set ItemDirection. How to arrange the elements in order from the initial position."""
        member = self.get_member("ItemDirection")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ItemDirection",
                members.FieldEnum(value=str(value)),
            )

