"""Generated component: VectorGizmo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.component import Component
from pyresonitelink.generated._types.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.segment_mesh import SegmentMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.cylinder_collider import CylinderCollider
from pyresonitelink.generated._types.arrow_mesh import ArrowMesh
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VectorGizmo(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VectorGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VectorGizmo"

    def __init__(self, target_slot: str | Slot | None = None, auto_position_at_target_slot: primitives.Bool | None = None, interacting_component: str | Component | None = None, material: str | OverlayFresnelMaterial | None = None, tool_point: str | Slot | None = None, active_point: str | Slot | None = None, line_root: str | Slot | None = None, line_segment: str | SegmentMesh | None = None, snap_highlight: str | Slot | None = None, target_vector: str | IField[primitives.Float3] | None = None, target_rotation: str | IField[primitives.FloatQ] | None = None, fix_magnitude: primitives.Bool | None = None, fixed_magnitude: primitives.Float | None = None, visual_magnitude_scale: primitives.Float | None = None, visual_thickness: primitives.Float | None = None, collider_rotation: str | IField[primitives.FloatQ] | None = None, collider: str | CylinderCollider | None = None, mesh: str | ArrowMesh | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_slot: Initial value for TargetSlot.
            auto_position_at_target_slot: Initial value for AutoPositionAtTargetSlot.
            interacting_component: Initial value for _interactingComponent.
            material: Initial value for _material.
            tool_point: Initial value for _toolPoint.
            active_point: Initial value for _activePoint.
            line_root: Initial value for _lineRoot.
            line_segment: Initial value for _lineSegment.
            snap_highlight: Initial value for _snapHighlight.
            target_vector: Initial value for TargetVector.
            target_rotation: Initial value for TargetRotation.
            fix_magnitude: Initial value for FixMagnitude.
            fixed_magnitude: Initial value for FixedMagnitude.
            visual_magnitude_scale: Initial value for VisualMagnitudeScale.
            visual_thickness: Initial value for VisualThickness.
            collider_rotation: Initial value for _colliderRotation.
            collider: Initial value for _collider.
            mesh: Initial value for _mesh.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_slot is not None:
            self.target_slot = target_slot
        if auto_position_at_target_slot is not None:
            self.auto_position_at_target_slot = auto_position_at_target_slot
        if interacting_component is not None:
            self.interacting_component = interacting_component
        if material is not None:
            self.material = material
        if tool_point is not None:
            self.tool_point = tool_point
        if active_point is not None:
            self.active_point = active_point
        if line_root is not None:
            self.line_root = line_root
        if line_segment is not None:
            self.line_segment = line_segment
        if snap_highlight is not None:
            self.snap_highlight = snap_highlight
        if target_vector is not None:
            self.target_vector = target_vector
        if target_rotation is not None:
            self.target_rotation = target_rotation
        if fix_magnitude is not None:
            self.fix_magnitude = fix_magnitude
        if fixed_magnitude is not None:
            self.fixed_magnitude = fixed_magnitude
        if visual_magnitude_scale is not None:
            self.visual_magnitude_scale = visual_magnitude_scale
        if visual_thickness is not None:
            self.visual_thickness = visual_thickness
        if collider_rotation is not None:
            self.collider_rotation = collider_rotation
        if collider is not None:
            self.collider = collider
        if mesh is not None:
            self.mesh = mesh

    @property
    def target_slot(self) -> str | None:
        """Target ID of the TargetSlot reference (targets Slot)."""
        member = self.get_member("TargetSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_slot.setter
    def target_slot(self, target: str | Slot | None) -> None:
        """Set the TargetSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TargetSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def auto_position_at_target_slot(self) -> primitives.Bool | None:
        """The AutoPositionAtTargetSlot field value."""
        member = self.get_member("AutoPositionAtTargetSlot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_position_at_target_slot.setter
    def auto_position_at_target_slot(self, value: primitives.Bool) -> None:
        """Set the AutoPositionAtTargetSlot field value."""
        member = self.get_member("AutoPositionAtTargetSlot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoPositionAtTargetSlot", fields.FieldBool(value=value)
            )

    @property
    def interacting_component(self) -> str | None:
        """Target ID of the _interactingComponent reference (targets Component)."""
        member = self.get_member("_interactingComponent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interacting_component.setter
    def interacting_component(self, target: str | Component | None) -> None:
        """Set the _interactingComponent reference by target ID or Component instance."""
        target_id: str | None = target.id if isinstance(target, Component) else target  # type: ignore[assignment]
        member = self.get_member("_interactingComponent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_interactingComponent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Component'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets OverlayFresnelMaterial)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _material reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def tool_point(self) -> str | None:
        """Target ID of the _toolPoint reference (targets Slot)."""
        member = self.get_member("_toolPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool_point.setter
    def tool_point(self, target: str | Slot | None) -> None:
        """Set the _toolPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_toolPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_toolPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def active_point(self) -> str | None:
        """Target ID of the _activePoint reference (targets Slot)."""
        member = self.get_member("_activePoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_point.setter
    def active_point(self, target: str | Slot | None) -> None:
        """Set the _activePoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_activePoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activePoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def line_root(self) -> str | None:
        """Target ID of the _lineRoot reference (targets Slot)."""
        member = self.get_member("_lineRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_root.setter
    def line_root(self, target: str | Slot | None) -> None:
        """Set the _lineRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_lineRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lineRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def line_segment(self) -> str | None:
        """Target ID of the _lineSegment reference (targets SegmentMesh)."""
        member = self.get_member("_lineSegment")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_segment.setter
    def line_segment(self, target: str | SegmentMesh | None) -> None:
        """Set the _lineSegment reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_lineSegment")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lineSegment",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def snap_highlight(self) -> str | None:
        """Target ID of the _snapHighlight reference (targets Slot)."""
        member = self.get_member("_snapHighlight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @snap_highlight.setter
    def snap_highlight(self, target: str | Slot | None) -> None:
        """Set the _snapHighlight reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_snapHighlight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_snapHighlight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def vector_space(self) -> members.SyncObject | None:
        """The VectorSpace member."""
        member = self.get_member("VectorSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @vector_space.setter
    def vector_space(self, value: members.SyncObject) -> None:
        """Set the VectorSpace member."""
        self.set_member("VectorSpace", value)

    @property
    def target_vector(self) -> str | None:
        """Target ID of the TargetVector reference (targets IField[primitives.Float3])."""
        member = self.get_member("TargetVector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_vector.setter
    def target_vector(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the TargetVector reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetVector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetVector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def target_rotation(self) -> str | None:
        """Target ID of the TargetRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("TargetRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_rotation.setter
    def target_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the TargetRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def fix_magnitude(self) -> primitives.Bool | None:
        """The FixMagnitude field value."""
        member = self.get_member("FixMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fix_magnitude.setter
    def fix_magnitude(self, value: primitives.Bool) -> None:
        """Set the FixMagnitude field value."""
        member = self.get_member("FixMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixMagnitude", fields.FieldBool(value=value)
            )

    @property
    def fixed_magnitude(self) -> primitives.Float | None:
        """The FixedMagnitude field value."""
        member = self.get_member("FixedMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fixed_magnitude.setter
    def fixed_magnitude(self, value: primitives.Float) -> None:
        """Set the FixedMagnitude field value."""
        member = self.get_member("FixedMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixedMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def visual_magnitude_scale(self) -> primitives.Float | None:
        """The VisualMagnitudeScale field value."""
        member = self.get_member("VisualMagnitudeScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visual_magnitude_scale.setter
    def visual_magnitude_scale(self, value: primitives.Float) -> None:
        """Set the VisualMagnitudeScale field value."""
        member = self.get_member("VisualMagnitudeScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualMagnitudeScale", fields.FieldFloat(value=value)
            )

    @property
    def visual_thickness(self) -> primitives.Float | None:
        """The VisualThickness field value."""
        member = self.get_member("VisualThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visual_thickness.setter
    def visual_thickness(self, value: primitives.Float) -> None:
        """Set the VisualThickness field value."""
        member = self.get_member("VisualThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualThickness", fields.FieldFloat(value=value)
            )

    @property
    def collider_rotation(self) -> str | None:
        """Target ID of the _colliderRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_colliderRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_rotation.setter
    def collider_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _colliderRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def collider(self) -> str | None:
        """Target ID of the _collider reference (targets CylinderCollider)."""
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | CylinderCollider | None) -> None:
        """Set the _collider reference by target ID or CylinderCollider instance."""
        target_id: str | None = target.id if isinstance(target, CylinderCollider) else target  # type: ignore[assignment]
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CylinderCollider'),
            )

    @property
    def mesh(self) -> str | None:
        """Target ID of the _mesh reference (targets ArrowMesh)."""
        member = self.get_member("_mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | ArrowMesh | None) -> None:
        """Set the _mesh reference by target ID or ArrowMesh instance."""
        target_id: str | None = target.id if isinstance(target, ArrowMesh) else target  # type: ignore[assignment]
        member = self.get_member("_mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ArrowMesh'),
            )

