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
    """The SkinnedMeshPositioner component drives a slot's transform so it stays locked to a specific triangle on a SkinnedMeshRenderer.

Normally you can attach things by parenting them to bones, which works okay. But for parts of the skinned mesh that are weighted to multiple bones and/or are affected by blendshapes, this will cause the object to "drift/slide" relative to the mesh. This component fixes that by computing the transform from the actual skinned mesh transform!"Skinned Mesh Positioner - attach objects to a fixed point on triangle!" - Frooxius on YouTube

    Category: Transform/Drivers

    To use this component, you should position a slot so that it is placed
    where you would like it to be anchored on the SkinnedMeshRenderer,
    attach this component to that slot, fill in the Skin field with a
    reference to the SkinnedMeshRenderer and select the Compute Parameters
    button in the Inspector. Once pressed, Resonite will fill in the
    TriangleIndex field with the index of the nearest triangle on the
    SkinnedMeshRenderer to that slot, fill in the BarycentricCoordinate,
    LocalPosition, LocalRotation & LocalScale fields with the values to keep
    the slot positioned where it was, relative to the selected triangle, and
    set the PositionDrive, RotationDrive & ScaleDrive fields to references
    to the respective slot fields.

    **Demo**: Overview and basic usage by Frooxius
cOuCitJ-ajI

    **See also**: * SkinnedMeshRenderer
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
        """The skinned mesh renderer to attach this object to"""
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
        """The index of the triangle in the mesh to attach this object to"""
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
        """How close the attachment point should be to each vertex of the triangle (barycentric coordinate system)."""
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
        """An offset to apply to the position of the object"""
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
        """An offset to apply to the rotation of the object"""
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
        """A multiplier to apply to the scale of the object"""
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
        """The position field of the slot to be driven with the position of the triangle in the SkinnedMeshRenderer"""
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
        """The rotation field of the slot to be driven with the rotation of the triangle in the SkinnedMeshRenderer"""
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
        """The scale field of the slot to be driven with the scale of the SkinnedMeshRenderer"""
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
        """Calculates parameters to position the slot at its current position, rotation & scale, relative to the nearest triangle on the specified SkinnedMeshRenderer

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ComputeParameters", {}, debug,
        )

