"""Generated component: ConeGizmo."""

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
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConeGizmo(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """The ConeGizmo component is auto generated for interaction with a ConeMesh or ConeCollider via a Dev Tool.

    Generated automatically.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ConeGizmo"

    def __init__(self, target_slot: str | Slot | None = None, auto_position_at_target_slot: primitives.Bool | None = None, interacting_component: str | Component | None = None, material: str | OverlayFresnelMaterial | None = None, tool_point: str | Slot | None = None, active_point: str | Slot | None = None, line_root: str | Slot | None = None, line_segment: str | SegmentMesh | None = None, snap_highlight: str | Slot | None = None, target_angle: str | IField[primitives.Float] | None = None, target_radius: str | IField[primitives.Float] | None = None, target_height: str | IField[primitives.Float] | None = None, target_direction: str | IField[primitives.Float3] | None = None, target_rotation: str | IField[primitives.FloatQ] | None = None, fixed_angle: primitives.Float | None = None, fixed_height: primitives.Float | None = None, fixed_direction: primitives.Float3 | None = None, line_thickness: primitives.Float | None = None, min_height: primitives.Float | None = None, max_height: primitives.Float | None = None, min_angle: primitives.Float | None = None, max_angle: primitives.Float | None = None, visual_root: str | Slot | None = None, visual_rot: str | IField[primitives.FloatQ] | None = None, height_mesh: str | SegmentMesh | None = None, cone_line_mesh: str | SegmentMesh | None = None, *, component: workers.Component | None = None) -> None:
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
            target_angle: Initial value for TargetAngle.
            target_radius: Initial value for TargetRadius.
            target_height: Initial value for TargetHeight.
            target_direction: Initial value for TargetDirection.
            target_rotation: Initial value for TargetRotation.
            fixed_angle: Initial value for FixedAngle.
            fixed_height: Initial value for FixedHeight.
            fixed_direction: Initial value for FixedDirection.
            line_thickness: Initial value for LineThickness.
            min_height: Initial value for MinHeight.
            max_height: Initial value for MaxHeight.
            min_angle: Initial value for MinAngle.
            max_angle: Initial value for MaxAngle.
            visual_root: Initial value for _visualRoot.
            visual_rot: Initial value for _visualRot.
            height_mesh: Initial value for _heightMesh.
            cone_line_mesh: Initial value for _coneLineMesh.
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
        if target_angle is not None:
            self.target_angle = target_angle
        if target_radius is not None:
            self.target_radius = target_radius
        if target_height is not None:
            self.target_height = target_height
        if target_direction is not None:
            self.target_direction = target_direction
        if target_rotation is not None:
            self.target_rotation = target_rotation
        if fixed_angle is not None:
            self.fixed_angle = fixed_angle
        if fixed_height is not None:
            self.fixed_height = fixed_height
        if fixed_direction is not None:
            self.fixed_direction = fixed_direction
        if line_thickness is not None:
            self.line_thickness = line_thickness
        if min_height is not None:
            self.min_height = min_height
        if max_height is not None:
            self.max_height = max_height
        if min_angle is not None:
            self.min_angle = min_angle
        if max_angle is not None:
            self.max_angle = max_angle
        if visual_root is not None:
            self.visual_root = visual_root
        if visual_rot is not None:
            self.visual_rot = visual_rot
        if height_mesh is not None:
            self.height_mesh = height_mesh
        if cone_line_mesh is not None:
            self.cone_line_mesh = cone_line_mesh

    @property
    def target_slot(self) -> str | None:
        """The slot to translate and edit."""
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
        """Whether to automatically position this at the target slot."""
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
        """the component This is interacting with."""
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
        """The material being used for the visual."""
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
        """The point that follows the interacting tool's tip."""
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
        """The point that follows the gizmo visual."""
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
        """the root of the line visual from the gizmo to the interacting tool's tip."""
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
        """The segment mesh being used for the line visual."""
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
        """the root of the snap highlight for snapping."""
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
    def target_angle(self) -> str | None:
        """The field being edited for the angle of the cone."""
        member = self.get_member("TargetAngle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_angle.setter
    def target_angle(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the TargetAngle reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetAngle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetAngle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def target_radius(self) -> str | None:
        """The field being edited for the radius of the cone base."""
        member = self.get_member("TargetRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_radius.setter
    def target_radius(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the TargetRadius reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def target_height(self) -> str | None:
        """The field being edited for the height of the cone."""
        member = self.get_member("TargetHeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_height.setter
    def target_height(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the TargetHeight reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetHeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetHeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def target_direction(self) -> str | None:
        """The field being edited for the cone direction."""
        member = self.get_member("TargetDirection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_direction.setter
    def target_direction(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the TargetDirection reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetDirection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetDirection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def target_rotation(self) -> str | None:
        """The field being edited for the cone rotation."""
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
    def direction_space(self) -> members.SyncObject | None:
        """The space Transform of ``TargetDirection``."""
        member = self.get_member("DirectionSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @direction_space.setter
    def direction_space(self, value: members.SyncObject) -> None:
        """Set DirectionSpace. The space Transform of ``TargetDirection``."""
        self.set_member("DirectionSpace", value)

    @property
    def fixed_angle(self) -> primitives.Float | None:
        """The angle that the cone should be at (shape)."""
        member = self.get_member("FixedAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fixed_angle.setter
    def fixed_angle(self, value: primitives.Float) -> None:
        """Set the FixedAngle field value."""
        member = self.get_member("FixedAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixedAngle", fields.FieldFloat(value=value)
            )

    @property
    def fixed_height(self) -> primitives.Float | None:
        """The height that the cone mesh should be."""
        member = self.get_member("FixedHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fixed_height.setter
    def fixed_height(self, value: primitives.Float) -> None:
        """Set the FixedHeight field value."""
        member = self.get_member("FixedHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixedHeight", fields.FieldFloat(value=value)
            )

    @property
    def fixed_direction(self) -> primitives.Float3 | None:
        """The direction the cone should be facing."""
        member = self.get_member("FixedDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fixed_direction.setter
    def fixed_direction(self, value: primitives.Float3) -> None:
        """Set the FixedDirection field value."""
        member = self.get_member("FixedDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixedDirection", fields.FieldFloat3(value=value)
            )

    @property
    def line_thickness(self) -> primitives.Float | None:
        """The thickness of the lines of the visual."""
        member = self.get_member("LineThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_thickness.setter
    def line_thickness(self, value: primitives.Float) -> None:
        """Set the LineThickness field value."""
        member = self.get_member("LineThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LineThickness", fields.FieldFloat(value=value)
            )

    @property
    def min_height(self) -> primitives.Float | None:
        """The minimum height the cone can be set to."""
        member = self.get_member("MinHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_height.setter
    def min_height(self, value: primitives.Float) -> None:
        """Set the MinHeight field value."""
        member = self.get_member("MinHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinHeight", fields.FieldFloat(value=value)
            )

    @property
    def max_height(self) -> primitives.Float | None:
        """The maximum height the cone can be set to."""
        member = self.get_member("MaxHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_height.setter
    def max_height(self, value: primitives.Float) -> None:
        """Set the MaxHeight field value."""
        member = self.get_member("MaxHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxHeight", fields.FieldFloat(value=value)
            )

    @property
    def min_angle(self) -> primitives.Float | None:
        """The minimum tip angle the cone can be set to (shape)."""
        member = self.get_member("MinAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_angle.setter
    def min_angle(self, value: primitives.Float) -> None:
        """Set the MinAngle field value."""
        member = self.get_member("MinAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinAngle", fields.FieldFloat(value=value)
            )

    @property
    def max_angle(self) -> primitives.Float | None:
        """The maximum tip angle the cone can be set to (shape)."""
        member = self.get_member("MaxAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_angle.setter
    def max_angle(self, value: primitives.Float) -> None:
        """Set the MaxAngle field value."""
        member = self.get_member("MaxAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxAngle", fields.FieldFloat(value=value)
            )

    @property
    def visual_root(self) -> str | None:
        """The root slot of the visual for this gizmo."""
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
        """The rotation field of the ``_visualRoot`` slot."""
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
    def handles(self) -> members.SyncList | None:
        """A list of Handle objects this cone gizmo has."""
        member = self.get_member("_handles")
        if isinstance(member, members.SyncList):
            return member
        return None

    @handles.setter
    def handles(self, value: members.SyncList) -> None:
        """Set _handles. A list of Handle objects this cone gizmo has."""
        self.set_member("_handles", value)

    @property
    def height_mesh(self) -> str | None:
        """The mesh being used to signal the height of the cone."""
        member = self.get_member("_heightMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height_mesh.setter
    def height_mesh(self, target: str | SegmentMesh | None) -> None:
        """Set the _heightMesh reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_heightMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_heightMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def cone_line_mesh(self) -> str | None:
        """The line segment based mesh that shows the cone itself."""
        member = self.get_member("_coneLineMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cone_line_mesh.setter
    def cone_line_mesh(self, target: str | SegmentMesh | None) -> None:
        """Set the _coneLineMesh reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_coneLineMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_coneLineMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

