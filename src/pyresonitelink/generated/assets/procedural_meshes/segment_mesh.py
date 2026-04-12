"""Generated component: SegmentMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.shading import Shading
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SegmentMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The SegmentMesh component is an evolved form of SlotSegmentMesh the behavior is identical, except when not provided slots it will use local coordinate points instead.

    Category: Assets/Procedural Meshes

    Attach to a slot and insert into a MeshRenderer to see the geometry.
    Don't forget to use a Material.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SegmentMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, radius: primitives.Float | None = None, point_a: primitives.Float3 | None = None, point_b: primitives.Float3 | None = None, slot_a: str | Slot | None = None, slot_b: str | Slot | None = None, shading: Shading | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            radius: Initial value for Radius.
            point_a: Initial value for PointA.
            point_b: Initial value for PointB.
            slot_a: Initial value for SlotA.
            slot_b: Initial value for SlotB.
            shading: Initial value for Shading.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if profile is not None:
            self.profile = profile
        if radius is not None:
            self.radius = radius
        if point_a is not None:
            self.point_a = point_a
        if point_b is not None:
            self.point_b = point_b
        if slot_a is not None:
            self.slot_a = slot_a
        if slot_b is not None:
            self.slot_b = slot_b
        if shading is not None:
            self.shading = shading

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> primitives.Bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: primitives.Bool) -> None:
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
    def profile(self) -> ColorProfile | None:
        """The Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set the Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def radius(self) -> primitives.Float | None:
        """The radius of the line from ``PointA``/``SlotA`` to ``PointB``/``SlotB``"""
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
    def point_a(self) -> primitives.Float3 | None:
        """The starting point of the generated line in local space."""
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
        """The ending point of the generated line in local space."""
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
        """The starting point of the generated line. This will be used instead of ``PointA`` if provided."""
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
        """The ending point of the generated line. This will be used instead of ``PointB`` if provided."""
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
    def shading(self) -> Shading | None:
        """Whether to use different shading like smooth or flat."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Shading(member.value)
        return None

    @shading.setter
    def shading(self, value: Shading | str) -> None:
        """Set Shading. Whether to use different shading like smooth or flat."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Shading",
                members.FieldEnum(value=str(value)),
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

