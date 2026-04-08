"""Generated component: AxisRotationGizmo."""

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
from pyresonitelink.generated._types.torus_mesh import TorusMesh
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisRotationGizmo(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AxisRotationGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AxisRotationGizmo"

    def __init__(self, target_slot: str | Slot | None = None, auto_position_at_target_slot: primitives.Bool | None = None, interacting_component: str | Component | None = None, material: str | OverlayFresnelMaterial | None = None, tool_point: str | Slot | None = None, active_point: str | Slot | None = None, line_root: str | Slot | None = None, line_segment: str | SegmentMesh | None = None, snap_highlight: str | Slot | None = None, axis: primitives.Float3 | None = None, target_rotation: str | IField[primitives.FloatQ] | None = None, target_value: str | IField[primitives.Float] | None = None, circle_radius: primitives.Float | None = None, circle_thickness: primitives.Float | None = None, visual_root: str | Slot | None = None, visual_rot: str | IField[primitives.FloatQ] | None = None, circle: str | TorusMesh | None = None, circle_collider_mesh: str | TorusMesh | None = None, reference_line: str | SegmentMesh | None = None, lines_root: str | Slot | None = None, line0: str | SegmentMesh | None = None, line1: str | SegmentMesh | None = None, *, component: workers.Component | None = None) -> None:
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
            axis: Initial value for Axis.
            target_rotation: Initial value for TargetRotation.
            target_value: Initial value for TargetValue.
            circle_radius: Initial value for CircleRadius.
            circle_thickness: Initial value for CircleThickness.
            visual_root: Initial value for _visualRoot.
            visual_rot: Initial value for _visualRot.
            circle: Initial value for _circle.
            circle_collider_mesh: Initial value for _circleColliderMesh.
            reference_line: Initial value for _referenceLine.
            lines_root: Initial value for _linesRoot.
            line0: Initial value for _line0.
            line1: Initial value for _line1.
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
        if axis is not None:
            self.axis = axis
        if target_rotation is not None:
            self.target_rotation = target_rotation
        if target_value is not None:
            self.target_value = target_value
        if circle_radius is not None:
            self.circle_radius = circle_radius
        if circle_thickness is not None:
            self.circle_thickness = circle_thickness
        if visual_root is not None:
            self.visual_root = visual_root
        if visual_rot is not None:
            self.visual_rot = visual_rot
        if circle is not None:
            self.circle = circle
        if circle_collider_mesh is not None:
            self.circle_collider_mesh = circle_collider_mesh
        if reference_line is not None:
            self.reference_line = reference_line
        if lines_root is not None:
            self.lines_root = lines_root
        if line0 is not None:
            self.line0 = line0
        if line1 is not None:
            self.line1 = line1

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
    def axis(self) -> primitives.Float3 | None:
        """The Axis field value."""
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
    def axis_space(self) -> members.SyncObject | None:
        """The AxisSpace member."""
        member = self.get_member("AxisSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @axis_space.setter
    def axis_space(self, value: members.SyncObject) -> None:
        """Set the AxisSpace member."""
        self.set_member("AxisSpace", value)

    @property
    def rotation_space(self) -> members.SyncObject | None:
        """The RotationSpace member."""
        member = self.get_member("RotationSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @rotation_space.setter
    def rotation_space(self, value: members.SyncObject) -> None:
        """Set the RotationSpace member."""
        self.set_member("RotationSpace", value)

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
    def target_value(self) -> str | None:
        """Target ID of the TargetValue reference (targets IField[primitives.Float])."""
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_value.setter
    def target_value(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the TargetValue reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def circle_radius(self) -> primitives.Float | None:
        """The CircleRadius field value."""
        member = self.get_member("CircleRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_radius.setter
    def circle_radius(self, value: primitives.Float) -> None:
        """Set the CircleRadius field value."""
        member = self.get_member("CircleRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CircleRadius", fields.FieldFloat(value=value)
            )

    @property
    def circle_thickness(self) -> primitives.Float | None:
        """The CircleThickness field value."""
        member = self.get_member("CircleThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_thickness.setter
    def circle_thickness(self, value: primitives.Float) -> None:
        """Set the CircleThickness field value."""
        member = self.get_member("CircleThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CircleThickness", fields.FieldFloat(value=value)
            )

    @property
    def visual_root(self) -> str | None:
        """Target ID of the _visualRoot reference (targets Slot)."""
        member = self.get_member("_visualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_root.setter
    def visual_root(self, target: str | Slot | None) -> None:
        """Set the _visualRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def visual_rot(self) -> str | None:
        """Target ID of the _visualRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_visualRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_rot.setter
    def visual_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _visualRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def circle(self) -> str | None:
        """Target ID of the _circle reference (targets TorusMesh)."""
        member = self.get_member("_circle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @circle.setter
    def circle(self, target: str | TorusMesh | None) -> None:
        """Set the _circle reference by target ID or TorusMesh instance."""
        target_id: str | None = target.id if isinstance(target, TorusMesh) else target  # type: ignore[assignment]
        member = self.get_member("_circle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_circle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TorusMesh'),
            )

    @property
    def circle_collider_mesh(self) -> str | None:
        """Target ID of the _circleColliderMesh reference (targets TorusMesh)."""
        member = self.get_member("_circleColliderMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @circle_collider_mesh.setter
    def circle_collider_mesh(self, target: str | TorusMesh | None) -> None:
        """Set the _circleColliderMesh reference by target ID or TorusMesh instance."""
        target_id: str | None = target.id if isinstance(target, TorusMesh) else target  # type: ignore[assignment]
        member = self.get_member("_circleColliderMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_circleColliderMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TorusMesh'),
            )

    @property
    def reference_line(self) -> str | None:
        """Target ID of the _referenceLine reference (targets SegmentMesh)."""
        member = self.get_member("_referenceLine")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_line.setter
    def reference_line(self, target: str | SegmentMesh | None) -> None:
        """Set the _referenceLine reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_referenceLine")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_referenceLine",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def lines_root(self) -> str | None:
        """Target ID of the _linesRoot reference (targets Slot)."""
        member = self.get_member("_linesRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lines_root.setter
    def lines_root(self, target: str | Slot | None) -> None:
        """Set the _linesRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_linesRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linesRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def line0(self) -> str | None:
        """Target ID of the _line0 reference (targets SegmentMesh)."""
        member = self.get_member("_line0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line0.setter
    def line0(self, target: str | SegmentMesh | None) -> None:
        """Set the _line0 reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_line0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_line0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def line1(self) -> str | None:
        """Target ID of the _line1 reference (targets SegmentMesh)."""
        member = self.get_member("_line1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line1.setter
    def line1(self, target: str | SegmentMesh | None) -> None:
        """Set the _line1 reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_line1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_line1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

