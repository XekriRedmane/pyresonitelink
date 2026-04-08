"""Generated component: SphereAligner."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SphereAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SphereAligner.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SphereAligner"

    def __init__(self, auto_add_children: bool | None = None, radius: np.float32 | None = None, distribution_offset: np.float32 | None = None, align_to_normal: bool | None = None, rotation_offset: primitives.FloatQ | None = None, normalized_start: np.float32 | None = None, normalized_end: np.float32 | None = None, horizontal_start: np.float32 | None = None, horizontal_end: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
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
    def auto_add_children(self) -> bool | None:
        """The AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_children.setter
    def auto_add_children(self, value: bool) -> None:
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
        """The AutoAddIgnoreTags member."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set the AutoAddIgnoreTags member."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def distribution_offset(self) -> np.float32 | None:
        """The DistributionOffset field value."""
        member = self.get_member("DistributionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distribution_offset.setter
    def distribution_offset(self, value: np.float32) -> None:
        """Set the DistributionOffset field value."""
        member = self.get_member("DistributionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistributionOffset", fields.FieldFloat(value=value)
            )

    @property
    def align_to_normal(self) -> bool | None:
        """The AlignToNormal field value."""
        member = self.get_member("AlignToNormal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @align_to_normal.setter
    def align_to_normal(self, value: bool) -> None:
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
        """The RotationOffset field value."""
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
    def normalized_start(self) -> np.float32 | None:
        """The NormalizedStart field value."""
        member = self.get_member("NormalizedStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_start.setter
    def normalized_start(self, value: np.float32) -> None:
        """Set the NormalizedStart field value."""
        member = self.get_member("NormalizedStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedStart", fields.FieldFloat(value=value)
            )

    @property
    def normalized_end(self) -> np.float32 | None:
        """The NormalizedEnd field value."""
        member = self.get_member("NormalizedEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_end.setter
    def normalized_end(self, value: np.float32) -> None:
        """Set the NormalizedEnd field value."""
        member = self.get_member("NormalizedEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedEnd", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_start(self) -> np.float32 | None:
        """The HorizontalStart field value."""
        member = self.get_member("HorizontalStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_start.setter
    def horizontal_start(self, value: np.float32) -> None:
        """Set the HorizontalStart field value."""
        member = self.get_member("HorizontalStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalStart", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_end(self) -> np.float32 | None:
        """The HorizontalEnd field value."""
        member = self.get_member("HorizontalEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_end.setter
    def horizontal_end(self, value: np.float32) -> None:
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
        """The Items member."""
        member = self.get_member("Items")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items.setter
    def items(self, value: members.SyncList) -> None:
        """Set the Items member."""
        self.set_member("Items", value)

