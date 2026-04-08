"""Generated component: SkinnedMeshPositioner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.skinned_mesh_renderer import SkinnedMeshRenderer
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SkinnedMeshPositioner(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SkinnedMeshPositioner.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SkinnedMeshPositioner"

    def __init__(self, skin: str | SkinnedMeshRenderer | None = None, triangle_index: primitives.Int | None = None, barycentric_coordinate: primitives.Float3 | None = None, local_position: primitives.Float3 | None = None, local_rotation: primitives.FloatQ | None = None, local_scale: primitives.Float3 | None = None, position_drive: str | IField[primitives.Float3] | None = None, rotation_drive: str | IField[primitives.FloatQ] | None = None, scale_drive: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            skin: Initial value for Skin.
            triangle_index: Initial value for TriangleIndex.
            barycentric_coordinate: Initial value for BarycentricCoordinate.
            local_position: Initial value for LocalPosition.
            local_rotation: Initial value for LocalRotation.
            local_scale: Initial value for LocalScale.
            position_drive: Initial value for PositionDrive.
            rotation_drive: Initial value for RotationDrive.
            scale_drive: Initial value for ScaleDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if skin is not None:
            self.skin = skin
        if triangle_index is not None:
            self.triangle_index = triangle_index
        if barycentric_coordinate is not None:
            self.barycentric_coordinate = barycentric_coordinate
        if local_position is not None:
            self.local_position = local_position
        if local_rotation is not None:
            self.local_rotation = local_rotation
        if local_scale is not None:
            self.local_scale = local_scale
        if position_drive is not None:
            self.position_drive = position_drive
        if rotation_drive is not None:
            self.rotation_drive = rotation_drive
        if scale_drive is not None:
            self.scale_drive = scale_drive

    @property
    def skin(self) -> str | None:
        """Target ID of the Skin reference (targets SkinnedMeshRenderer)."""
        member = self.get_member("Skin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @skin.setter
    def skin(self, target: str | SkinnedMeshRenderer | None) -> None:
        """Set the Skin reference by target ID or SkinnedMeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, SkinnedMeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Skin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Skin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SkinnedMeshRenderer'),
            )

    @property
    def triangle_index(self) -> primitives.Int | None:
        """The TriangleIndex field value."""
        member = self.get_member("TriangleIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triangle_index.setter
    def triangle_index(self, value: primitives.Int) -> None:
        """Set the TriangleIndex field value."""
        member = self.get_member("TriangleIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriangleIndex", fields.FieldInt(value=value)
            )

    @property
    def barycentric_coordinate(self) -> primitives.Float3 | None:
        """The BarycentricCoordinate field value."""
        member = self.get_member("BarycentricCoordinate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @barycentric_coordinate.setter
    def barycentric_coordinate(self, value: primitives.Float3) -> None:
        """Set the BarycentricCoordinate field value."""
        member = self.get_member("BarycentricCoordinate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BarycentricCoordinate", fields.FieldFloat3(value=value)
            )

    @property
    def local_position(self) -> primitives.Float3 | None:
        """The LocalPosition field value."""
        member = self.get_member("LocalPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_position.setter
    def local_position(self, value: primitives.Float3) -> None:
        """Set the LocalPosition field value."""
        member = self.get_member("LocalPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalPosition", fields.FieldFloat3(value=value)
            )

    @property
    def local_rotation(self) -> primitives.FloatQ | None:
        """The LocalRotation field value."""
        member = self.get_member("LocalRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_rotation.setter
    def local_rotation(self, value: primitives.FloatQ) -> None:
        """Set the LocalRotation field value."""
        member = self.get_member("LocalRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def local_scale(self) -> primitives.Float3 | None:
        """The LocalScale field value."""
        member = self.get_member("LocalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_scale.setter
    def local_scale(self, value: primitives.Float3) -> None:
        """Set the LocalScale field value."""
        member = self.get_member("LocalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalScale", fields.FieldFloat3(value=value)
            )

    @property
    def position_drive(self) -> str | None:
        """Target ID of the PositionDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("PositionDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_drive.setter
    def position_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the PositionDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PositionDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PositionDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rotation_drive(self) -> str | None:
        """Target ID of the RotationDrive reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("RotationDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_drive.setter
    def rotation_drive(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the RotationDrive reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RotationDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RotationDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def scale_drive(self) -> str | None:
        """Target ID of the ScaleDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("ScaleDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_drive.setter
    def scale_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the ScaleDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ScaleDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ScaleDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    async def compute_parameters(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ComputeParameters sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ComputeParameters", {}, debug,
        )

