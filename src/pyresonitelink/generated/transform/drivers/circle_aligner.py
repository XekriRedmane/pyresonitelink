"""Generated component: CircleAligner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CircleAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The CircleAligner component is used to position a list of slots in a circle.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CircleAligner"

    def __init__(self, auto_add_children: primitives.Bool | None = None, axis: primitives.Float3 | None = None, radius: primitives.Float | None = None, offset: primitives.Float | None = None, arc: primitives.Float | None = None, fill_whole_arc: primitives.Bool | None = None, rotation_offset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            axis: Initial value for Axis.
            radius: Initial value for Radius.
            offset: Initial value for Offset.
            arc: Initial value for Arc.
            fill_whole_arc: Initial value for FillWholeArc.
            rotation_offset: Initial value for RotationOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if axis is not None:
            self.axis = axis
        if radius is not None:
            self.radius = radius
        if offset is not None:
            self.offset = offset
        if arc is not None:
            self.arc = arc
        if fill_whole_arc is not None:
            self.fill_whole_arc = fill_whole_arc
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset

    @property
    def auto_add_children(self) -> primitives.Bool | None:
        """Controls whether slots below this component's slot in the hierarchy are automatically added to ``Items``"""
        member = self.get_member("AutoAddChildren")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_children.setter
    def auto_add_children(self, value: primitives.Bool) -> None:
        """Set the AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddChildren", fields.FieldBool(value=value)
            )

    @property
    def auto_add_ignore_tags(self) -> members.SyncList | None:
        """If a slot has a Tag matching one of the tags in this list, it will not be auto added to ``Items``"""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set AutoAddIgnoreTags. If a slot has a Tag matching one of the tags in this list, it will not be auto added to ``Items``"""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def axis(self) -> primitives.Float3 | None:
        """The axis around which the slots will be aligned."""
        member = self.get_member("Axis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @axis.setter
    def axis(self, value: primitives.Float3) -> None:
        """Set the Axis field value."""
        member = self.get_member("Axis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Axis", fields.FieldFloat3(value=value)
            )

    @property
    def radius(self) -> primitives.Float | None:
        """The radius of the circle that the slots will be positioned on."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> primitives.Float | None:
        """Offsets the starting position of the circle."""
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
    def arc(self) -> primitives.Float | None:
        """360 by default. If smaller, the slots will only fill that section of a circle. Likewise, if it is larger than 360, the slots will wrap around the circle multiple times."""
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
    def fill_whole_arc(self) -> primitives.Bool | None:
        """If true, the last slot will be at the very end of the arch, otherwise there will be a gap after the last slots."""
        member = self.get_member("FillWholeArc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_whole_arc.setter
    def fill_whole_arc(self, value: primitives.Bool) -> None:
        """Set the FillWholeArc field value."""
        member = self.get_member("FillWholeArc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillWholeArc", fields.FieldBool(value=value)
            )

    @property
    def rotation_offset(self) -> primitives.Float | None:
        """An offset, in degrees, that is applied to the rotation of the target slots."""
        member = self.get_member("RotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_offset.setter
    def rotation_offset(self, value: primitives.Float) -> None:
        """Set the RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationOffset", fields.FieldFloat(value=value)
            )

    @property
    def items(self) -> members.SyncList | None:
        """The list of slots to be aligned."""
        member = self.get_member("Items")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items.setter
    def items(self, value: members.SyncList) -> None:
        """Set Items. The list of slots to be aligned."""
        self.set_member("Items", value)

