"""Generated component: SegmentMesh."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SegmentMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SegmentMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SegmentMesh"

    def __init__(self, slot_a: str | Slot | None = None, slot_b: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            slot_a: Initial value for SlotA.
            slot_b: Initial value for SlotB.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if slot_a is not None:
            self.slot_a = slot_a
        if slot_b is not None:
            self.slot_b = slot_b

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: bool) -> None:
        """Set the OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideBoundingBox", fields.FieldBool(value=value)
            )

    @property
    def overriden_bounding_box(self) -> primitives.BoundingBox | None:
        """The OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overriden_bounding_box.setter
    def overriden_bounding_box(self, value: primitives.BoundingBox) -> None:
        """Set the OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverridenBoundingBox", fields.FieldBoundingBox(value=value)
            )

    @property
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

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
    def point_a(self) -> primitives.Float3 | None:
        """The PointA field value."""
        member = self.get_member("PointA")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point_a.setter
    def point_a(self, value: primitives.Float3) -> None:
        """Set the PointA field value."""
        member = self.get_member("PointA")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PointA", fields.FieldFloat3(value=value)
            )

    @property
    def point_b(self) -> primitives.Float3 | None:
        """The PointB field value."""
        member = self.get_member("PointB")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point_b.setter
    def point_b(self, value: primitives.Float3) -> None:
        """Set the PointB field value."""
        member = self.get_member("PointB")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PointB", fields.FieldFloat3(value=value)
            )

    @property
    def slot_a(self) -> str | None:
        """Target ID of the SlotA reference (targets Slot)."""
        member = self.get_member("SlotA")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slot_a.setter
    def slot_a(self, target: str | Slot | None) -> None:
        """Set the SlotA reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SlotA")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SlotA",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def slot_b(self) -> str | None:
        """Target ID of the SlotB reference (targets Slot)."""
        member = self.get_member("SlotB")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slot_b.setter
    def slot_b(self, target: str | Slot | None) -> None:
        """Set the SlotB reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SlotB")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SlotB",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def shading(self) -> members.FieldEnum | None:
        """The Shading member."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shading.setter
    def shading(self, value: members.FieldEnum) -> None:
        """Set the Shading member."""
        self.set_member("Shading", value)

