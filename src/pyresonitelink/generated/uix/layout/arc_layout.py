"""Generated component: ArcLayout."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ArcLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ArcLayout.

    Category: UIX/Layout
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ArcLayout"

    def __init__(self, arc: primitives.Float | None = None, offset: primitives.Float | None = None, separation: primitives.Float | None = None, center_at_separation: primitives.Bool | None = None, proportional_size: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            arc: Initial value for Arc.
            offset: Initial value for Offset.
            separation: Initial value for Separation.
            center_at_separation: Initial value for CenterAtSeparation.
            proportional_size: Initial value for ProportionalSize.
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

    @property
    def arc(self) -> primitives.Float | None:
        """The Arc field value."""
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
        """The Offset field value."""
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
        """The Separation field value."""
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
        """The CenterAtSeparation field value."""
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
        """The ProportionalSize field value."""
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
    def item_direction(self) -> members.FieldEnum | None:
        """The ItemDirection member."""
        member = self.get_member("ItemDirection")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @item_direction.setter
    def item_direction(self, value: members.FieldEnum) -> None:
        """Set the ItemDirection member."""
        self.set_member("ItemDirection", value)

