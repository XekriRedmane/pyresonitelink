"""Generated component: SphereAligner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SphereAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Sphere aligner is a component that has a list of child slots under ``Items`` and aligns those items into a spherical shape.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SphereAligner"

    def __init__(self, auto_add_children: primitives.Bool | None = None, radius: primitives.Float | None = None, distribution_offset: primitives.Float | None = None, align_to_normal: primitives.Bool | None = None, rotation_offset: primitives.FloatQ | None = None, normalized_start: primitives.Float | None = None, normalized_end: primitives.Float | None = None, horizontal_start: primitives.Float | None = None, horizontal_end: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            radius: Initial value for Radius.
            distribution_offset: Initial value for DistributionOffset.
            align_to_normal: Initial value for AlignToNormal.
            rotation_offset: Initial value for RotationOffset.
            normalized_start: Initial value for NormalizedStart.
            normalized_end: Initial value for NormalizedEnd.
            horizontal_start: Initial value for HorizontalStart.
            horizontal_end: Initial value for HorizontalEnd.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if radius is not None:
            self.radius = radius
        if distribution_offset is not None:
            self.distribution_offset = distribution_offset
        if align_to_normal is not None:
            self.align_to_normal = align_to_normal
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset
        if normalized_start is not None:
            self.normalized_start = normalized_start
        if normalized_end is not None:
            self.normalized_end = normalized_end
        if horizontal_start is not None:
            self.horizontal_start = horizontal_start
        if horizontal_end is not None:
            self.horizontal_end = horizontal_end

    @property
    def auto_add_children(self) -> primitives.Bool | None:
        """Controls whether slots below this component's slot in the hierarchy are automatically added to ``_targets``"""
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
        """Do not add slots to the list of children automatically if it's tag is contained in this list."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set AutoAddIgnoreTags. Do not add slots to the list of children automatically if it's tag is contained in this list."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def radius(self) -> primitives.Float | None:
        """The radius of the sphere to align items into"""
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
    def distribution_offset(self) -> primitives.Float | None:
        """Shift the positions of the items along the sphere surface, redistributes."""
        member = self.get_member("DistributionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distribution_offset.setter
    def distribution_offset(self, value: primitives.Float) -> None:
        """Set the DistributionOffset field value."""
        member = self.get_member("DistributionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistributionOffset", fields.FieldFloat(value=value)
            )

    @property
    def align_to_normal(self) -> primitives.Bool | None:
        """Whether to rotate the items to align them to the surface of the sphere"""
        member = self.get_member("AlignToNormal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @align_to_normal.setter
    def align_to_normal(self, value: primitives.Bool) -> None:
        """Set the AlignToNormal field value."""
        member = self.get_member("AlignToNormal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlignToNormal", fields.FieldBool(value=value)
            )

    @property
    def rotation_offset(self) -> primitives.FloatQ | None:
        """How much to rotate the sphere of aligned items by their individual origins"""
        member = self.get_member("RotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_offset.setter
    def rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def normalized_start(self) -> primitives.Float | None:
        """What point to start the alignment of items from top to bottom of the sphere."""
        member = self.get_member("NormalizedStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_start.setter
    def normalized_start(self, value: primitives.Float) -> None:
        """Set the NormalizedStart field value."""
        member = self.get_member("NormalizedStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedStart", fields.FieldFloat(value=value)
            )

    @property
    def normalized_end(self) -> primitives.Float | None:
        """What point to end the alignment of items from top to bottom of the sphere."""
        member = self.get_member("NormalizedEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_end.setter
    def normalized_end(self, value: primitives.Float) -> None:
        """Set the NormalizedEnd field value."""
        member = self.get_member("NormalizedEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedEnd", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_start(self) -> primitives.Float | None:
        """What point to start the alignment of items along the equator of the sphere."""
        member = self.get_member("HorizontalStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_start.setter
    def horizontal_start(self, value: primitives.Float) -> None:
        """Set the HorizontalStart field value."""
        member = self.get_member("HorizontalStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalStart", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_end(self) -> primitives.Float | None:
        """What point to end the alignment of items along the equator of the sphere."""
        member = self.get_member("HorizontalEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_end.setter
    def horizontal_end(self, value: primitives.Float) -> None:
        """Set the HorizontalEnd field value."""
        member = self.get_member("HorizontalEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalEnd", fields.FieldFloat(value=value)
            )

    @property
    def items(self) -> members.SyncList | None:
        """A list of items to align into the sphere shape."""
        member = self.get_member("Items")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items.setter
    def items(self, value: members.SyncList) -> None:
        """Set Items. A list of items to align into the sphere shape."""
        self.set_member("Items", value)

