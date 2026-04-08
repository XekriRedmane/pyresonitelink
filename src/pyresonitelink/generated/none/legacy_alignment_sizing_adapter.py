"""Generated component: LegacyAlignmentSizingAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.billboard_alignment import BillboardAlignment
from pyresonitelink.generated._types.mesh_alignment import MeshAlignment
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyAlignmentSizingAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.LegacyAlignmentSizingAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyAlignmentSizingAdapter"

    def __init__(self, length_scale: primitives.Float | None = None, velocity_scale: primitives.Float | None = None, particle_mesh: str | AssetRef[Mesh] | None = None, using_stretch: primitives.Bool | None = None, rotation_simulator: str | IField[primitives.Bool] | None = None, orient_by_velocity: str | IField[primitives.Bool] | None = None, pivot_module: str | IField[primitives.Bool] | None = None, use_local_rotation: str | IField[primitives.Bool] | None = None, size_modifier_enabled: str | IField[primitives.Bool] | None = None, size_offset_byvelocity_enabled: str | IField[primitives.Bool] | None = None, orient_up: str | IField[primitives.Float3] | None = None, length_size_multiplier: str | IField[primitives.Float3] | None = None, velocity_size_multiplier: str | IField[primitives.Float3] | None = None, pivot_multiplier: str | IField[primitives.Float3] | None = None, billboard_alignment: str | IField[BillboardAlignment] | None = None, mesh_alignment: str | IField[MeshAlignment] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            length_scale: Initial value for LengthScale.
            velocity_scale: Initial value for VelocityScale.
            particle_mesh: Initial value for ParticleMesh.
            using_stretch: Initial value for UsingStretch.
            rotation_simulator: Initial value for RotationSimulator.
            orient_by_velocity: Initial value for OrientByVelocity.
            pivot_module: Initial value for PivotModule.
            use_local_rotation: Initial value for UseLocalRotation.
            size_modifier_enabled: Initial value for SizeModifierEnabled.
            size_offset_byvelocity_enabled: Initial value for SizeOffsetByvelocityEnabled.
            orient_up: Initial value for OrientUp.
            length_size_multiplier: Initial value for LengthSizeMultiplier.
            velocity_size_multiplier: Initial value for VelocitySizeMultiplier.
            pivot_multiplier: Initial value for PivotMultiplier.
            billboard_alignment: Initial value for BillboardAlignment.
            mesh_alignment: Initial value for MeshAlignment.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if length_scale is not None:
            self.length_scale = length_scale
        if velocity_scale is not None:
            self.velocity_scale = velocity_scale
        if particle_mesh is not None:
            self.particle_mesh = particle_mesh
        if using_stretch is not None:
            self.using_stretch = using_stretch
        if rotation_simulator is not None:
            self.rotation_simulator = rotation_simulator
        if orient_by_velocity is not None:
            self.orient_by_velocity = orient_by_velocity
        if pivot_module is not None:
            self.pivot_module = pivot_module
        if use_local_rotation is not None:
            self.use_local_rotation = use_local_rotation
        if size_modifier_enabled is not None:
            self.size_modifier_enabled = size_modifier_enabled
        if size_offset_byvelocity_enabled is not None:
            self.size_offset_byvelocity_enabled = size_offset_byvelocity_enabled
        if orient_up is not None:
            self.orient_up = orient_up
        if length_size_multiplier is not None:
            self.length_size_multiplier = length_size_multiplier
        if velocity_size_multiplier is not None:
            self.velocity_size_multiplier = velocity_size_multiplier
        if pivot_multiplier is not None:
            self.pivot_multiplier = pivot_multiplier
        if billboard_alignment is not None:
            self.billboard_alignment = billboard_alignment
        if mesh_alignment is not None:
            self.mesh_alignment = mesh_alignment

    @property
    def length_scale(self) -> primitives.Float | None:
        """The LengthScale field value."""
        member = self.get_member("LengthScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @length_scale.setter
    def length_scale(self, value: primitives.Float) -> None:
        """Set the LengthScale field value."""
        member = self.get_member("LengthScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LengthScale", fields.FieldFloat(value=value)
            )

    @property
    def velocity_scale(self) -> primitives.Float | None:
        """The VelocityScale field value."""
        member = self.get_member("VelocityScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @velocity_scale.setter
    def velocity_scale(self, value: primitives.Float) -> None:
        """Set the VelocityScale field value."""
        member = self.get_member("VelocityScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VelocityScale", fields.FieldFloat(value=value)
            )

    @property
    def alignment(self) -> members.FieldEnum | None:
        """The Alignment member."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @alignment.setter
    def alignment(self, value: members.FieldEnum) -> None:
        """Set the Alignment member."""
        self.set_member("Alignment", value)

    @property
    def particle_mesh(self) -> str | None:
        """Target ID of the ParticleMesh reference (targets AssetRef[Mesh])."""
        member = self.get_member("ParticleMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @particle_mesh.setter
    def particle_mesh(self, target: str | AssetRef[Mesh] | None) -> None:
        """Set the ParticleMesh reference by target ID or AssetRef[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("ParticleMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParticleMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.Mesh>'),
            )

    @property
    def using_stretch(self) -> primitives.Bool | None:
        """The UsingStretch field value."""
        member = self.get_member("UsingStretch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @using_stretch.setter
    def using_stretch(self, value: primitives.Bool) -> None:
        """Set the UsingStretch field value."""
        member = self.get_member("UsingStretch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsingStretch", fields.FieldBool(value=value)
            )

    @property
    def rotation_simulator(self) -> str | None:
        """Target ID of the RotationSimulator reference (targets IField[primitives.Bool])."""
        member = self.get_member("RotationSimulator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_simulator.setter
    def rotation_simulator(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the RotationSimulator reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RotationSimulator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RotationSimulator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def orient_by_velocity(self) -> str | None:
        """Target ID of the OrientByVelocity reference (targets IField[primitives.Bool])."""
        member = self.get_member("OrientByVelocity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @orient_by_velocity.setter
    def orient_by_velocity(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the OrientByVelocity reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("OrientByVelocity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OrientByVelocity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def pivot_module(self) -> str | None:
        """Target ID of the PivotModule reference (targets IField[primitives.Bool])."""
        member = self.get_member("PivotModule")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pivot_module.setter
    def pivot_module(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the PivotModule reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PivotModule")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PivotModule",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def use_local_rotation(self) -> str | None:
        """Target ID of the UseLocalRotation reference (targets IField[primitives.Bool])."""
        member = self.get_member("UseLocalRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @use_local_rotation.setter
    def use_local_rotation(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the UseLocalRotation reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UseLocalRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UseLocalRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def size_modifier_enabled(self) -> str | None:
        """Target ID of the SizeModifierEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("SizeModifierEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_modifier_enabled.setter
    def size_modifier_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the SizeModifierEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SizeModifierEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SizeModifierEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def size_offset_byvelocity_enabled(self) -> str | None:
        """Target ID of the SizeOffsetByvelocityEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("SizeOffsetByvelocityEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_offset_byvelocity_enabled.setter
    def size_offset_byvelocity_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the SizeOffsetByvelocityEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SizeOffsetByvelocityEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SizeOffsetByvelocityEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def orient_up(self) -> str | None:
        """Target ID of the OrientUp reference (targets IField[primitives.Float3])."""
        member = self.get_member("OrientUp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @orient_up.setter
    def orient_up(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the OrientUp reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("OrientUp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OrientUp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def length_size_multiplier(self) -> str | None:
        """Target ID of the LengthSizeMultiplier reference (targets IField[primitives.Float3])."""
        member = self.get_member("LengthSizeMultiplier")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @length_size_multiplier.setter
    def length_size_multiplier(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the LengthSizeMultiplier reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LengthSizeMultiplier")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LengthSizeMultiplier",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def velocity_size_multiplier(self) -> str | None:
        """Target ID of the VelocitySizeMultiplier reference (targets IField[primitives.Float3])."""
        member = self.get_member("VelocitySizeMultiplier")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @velocity_size_multiplier.setter
    def velocity_size_multiplier(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the VelocitySizeMultiplier reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("VelocitySizeMultiplier")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VelocitySizeMultiplier",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def pivot_multiplier(self) -> str | None:
        """Target ID of the PivotMultiplier reference (targets IField[primitives.Float3])."""
        member = self.get_member("PivotMultiplier")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pivot_multiplier.setter
    def pivot_multiplier(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the PivotMultiplier reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PivotMultiplier")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PivotMultiplier",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def billboard_alignment(self) -> str | None:
        """Target ID of the BillboardAlignment reference (targets IField[BillboardAlignment])."""
        member = self.get_member("BillboardAlignment")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @billboard_alignment.setter
    def billboard_alignment(self, target: str | IField[BillboardAlignment] | None) -> None:
        """Set the BillboardAlignment reference by target ID or IField[BillboardAlignment] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("BillboardAlignment")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BillboardAlignment",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.BillboardAlignment>'),
            )

    @property
    def mesh_alignment(self) -> str | None:
        """Target ID of the MeshAlignment reference (targets IField[MeshAlignment])."""
        member = self.get_member("MeshAlignment")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh_alignment.setter
    def mesh_alignment(self, target: str | IField[MeshAlignment] | None) -> None:
        """Set the MeshAlignment reference by target ID or IField[MeshAlignment] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MeshAlignment")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MeshAlignment",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.MeshAlignment>'),
            )

