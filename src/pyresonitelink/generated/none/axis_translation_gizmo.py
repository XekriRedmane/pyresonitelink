"""Generated component: AxisTranslationGizmo."""

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
from pyresonitelink.generated._types.arrow_mesh import ArrowMesh
from pyresonitelink.generated._types.cylinder_collider import CylinderCollider
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisTranslationGizmo(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """The AxisTranslationGizmo is the squares often seen on a Gizmo to translate it along 2 axies at the same time.

    Used For Gizmos.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AxisTranslationGizmo"

    def __init__(self, target_slot: str | Slot | None = None, auto_position_at_target_slot: primitives.Bool | None = None, interacting_component: str | Component | None = None, material: str | OverlayFresnelMaterial | None = None, tool_point: str | Slot | None = None, active_point: str | Slot | None = None, line_root: str | Slot | None = None, line_segment: str | SegmentMesh | None = None, snap_highlight: str | Slot | None = None, axis: primitives.Float3 | None = None, target_point: str | IField[primitives.Float3] | None = None, target_value: str | IField[primitives.Float] | None = None, use_custom_visual: primitives.Bool | None = None, custom_visual_root: str | Slot | None = None, arrow_length: primitives.Float | None = None, create_undo_steps: primitives.Bool | None = None, visual_root: str | Slot | None = None, visual_rot: str | IField[primitives.FloatQ] | None = None, arrow_vector: str | IField[primitives.Float3] | None = None, arrow: str | ArrowMesh | None = None, collider: str | CylinderCollider | None = None, lines_root: str | Slot | None = None, line0: str | SegmentMesh | None = None, line1: str | SegmentMesh | None = None, *, component: workers.Component | None = None) -> None:
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
            target_point: Initial value for TargetPoint.
            target_value: Initial value for TargetValue.
            use_custom_visual: Initial value for UseCustomVisual.
            custom_visual_root: Initial value for _customVisualRoot.
            arrow_length: Initial value for ArrowLength.
            create_undo_steps: Initial value for CreateUndoSteps.
            visual_root: Initial value for _visualRoot.
            visual_rot: Initial value for _visualRot.
            arrow_vector: Initial value for _arrowVector.
            arrow: Initial value for _arrow.
            collider: Initial value for _collider.
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
        if target_point is not None:
            self.target_point = target_point
        if target_value is not None:
            self.target_value = target_value
        if use_custom_visual is not None:
            self.use_custom_visual = use_custom_visual
        if custom_visual_root is not None:
            self.custom_visual_root = custom_visual_root
        if arrow_length is not None:
            self.arrow_length = arrow_length
        if create_undo_steps is not None:
            self.create_undo_steps = create_undo_steps
        if visual_root is not None:
            self.visual_root = visual_root
        if visual_rot is not None:
            self.visual_rot = visual_rot
        if arrow_vector is not None:
            self.arrow_vector = arrow_vector
        if arrow is not None:
            self.arrow = arrow
        if collider is not None:
            self.collider = collider
        if lines_root is not None:
            self.lines_root = lines_root
        if line0 is not None:
            self.line0 = line0
        if line1 is not None:
            self.line1 = line1

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
    def axis(self) -> primitives.Float3 | None:
        """The direction of the 2d plane this will translate along."""
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
        """The coordinate space of ``Axis``."""
        member = self.get_member("AxisSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @axis_space.setter
    def axis_space(self, value: members.SyncObject) -> None:
        """Set AxisSpace. The coordinate space of ``Axis``."""
        self.set_member("AxisSpace", value)

    @property
    def point_space(self) -> members.SyncObject | None:
        """The coordinate space of ``TargetPoint`` drive value."""
        member = self.get_member("PointSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @point_space.setter
    def point_space(self, value: members.SyncObject) -> None:
        """Set PointSpace. The coordinate space of ``TargetPoint`` drive value."""
        self.set_member("PointSpace", value)

    @property
    def target_point(self) -> str | None:
        """A field to drive with the target point position."""
        member = self.get_member("TargetPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_point.setter
    def target_point(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the TargetPoint reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def target_value(self) -> str | None:
        """The field to use for ``TargetPoint``"""
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
    def use_custom_visual(self) -> primitives.Bool | None:
        """Whether to use a custom visual rather than the default code generated one."""
        member = self.get_member("UseCustomVisual")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_custom_visual.setter
    def use_custom_visual(self, value: primitives.Bool) -> None:
        """Set the UseCustomVisual field value."""
        member = self.get_member("UseCustomVisual")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseCustomVisual", fields.FieldBool(value=value)
            )

    @property
    def custom_visual_root(self) -> str | None:
        """The root slot of the custom visual."""
        member = self.get_member("_customVisualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @custom_visual_root.setter
    def custom_visual_root(self, target: str | Slot | None) -> None:
        """Set the _customVisualRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_customVisualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_customVisualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def arrow_length(self) -> primitives.Float | None:
        """The length of the arrow this gizmo is attached to."""
        member = self.get_member("ArrowLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arrow_length.setter
    def arrow_length(self, value: primitives.Float) -> None:
        """Set the ArrowLength field value."""
        member = self.get_member("ArrowLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ArrowLength", fields.FieldFloat(value=value)
            )

    @property
    def create_undo_steps(self) -> primitives.Bool | None:
        """Whether to make edits done with this component undoable."""
        member = self.get_member("CreateUndoSteps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @create_undo_steps.setter
    def create_undo_steps(self, value: primitives.Bool) -> None:
        """Set the CreateUndoSteps field value."""
        member = self.get_member("CreateUndoSteps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreateUndoSteps", fields.FieldBool(value=value)
            )

    @property
    def visual_root(self) -> str | None:
        """The root slot of the visual for interaction."""
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
        """The rotation field of the visual."""
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
    def arrow_vector(self) -> str | None:
        """The vector field of the arrow mesh visual."""
        member = self.get_member("_arrowVector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arrow_vector.setter
    def arrow_vector(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _arrowVector reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arrowVector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arrowVector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def arrow(self) -> str | None:
        """The arrow mesh of the visual."""
        member = self.get_member("_arrow")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arrow.setter
    def arrow(self, target: str | ArrowMesh | None) -> None:
        """Set the _arrow reference by target ID or ArrowMesh instance."""
        target_id: str | None = target.id if isinstance(target, ArrowMesh) else target  # type: ignore[assignment]
        member = self.get_member("_arrow")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arrow",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ArrowMesh'),
            )

    @property
    def collider(self) -> str | None:
        """The collider of the visual."""
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
    def lines_root(self) -> str | None:
        """the root slot of the lines visual."""
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
        """The segment mesh being used for the first line."""
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
        """The segment mesh being used for the second line."""
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

