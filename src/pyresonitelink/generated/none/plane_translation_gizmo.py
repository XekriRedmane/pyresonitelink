"""Generated component: PlaneTranslationGizmo."""

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
from pyresonitelink.generated._types.box_collider import BoxCollider
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlaneTranslationGizmo(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PlaneTranslationGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlaneTranslationGizmo"

    def __init__(self, target_slot: str | Slot | None = None, auto_position_at_target_slot: primitives.Bool | None = None, interacting_component: str | Component | None = None, material: str | OverlayFresnelMaterial | None = None, tool_point: str | Slot | None = None, active_point: str | Slot | None = None, line_root: str | Slot | None = None, line_segment: str | SegmentMesh | None = None, snap_highlight: str | Slot | None = None, target_point: str | IField[primitives.Float3] | None = None, normal: primitives.Float3 | None = None, use_custom_visual: primitives.Bool | None = None, custom_visual_root: str | Slot | None = None, handle_size: primitives.Float2 | None = None, handle_offset: primitives.Float2 | None = None, create_undo_steps: primitives.Bool | None = None, visual_root: str | Slot | None = None, visual_rotation: str | IField[primitives.FloatQ] | None = None, visual_position: str | IField[primitives.Float3] | None = None, box_size: str | IField[primitives.Float3] | None = None, lines_root: str | Slot | None = None, line0: str | SegmentMesh | None = None, line1: str | SegmentMesh | None = None, collider: str | BoxCollider | None = None, *, component: workers.Component | None = None) -> None:
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
            target_point: Initial value for TargetPoint.
            normal: Initial value for Normal.
            use_custom_visual: Initial value for UseCustomVisual.
            custom_visual_root: Initial value for _customVisualRoot.
            handle_size: Initial value for HandleSize.
            handle_offset: Initial value for HandleOffset.
            create_undo_steps: Initial value for CreateUndoSteps.
            visual_root: Initial value for _visualRoot.
            visual_rotation: Initial value for _visualRotation.
            visual_position: Initial value for _visualPosition.
            box_size: Initial value for _boxSize.
            lines_root: Initial value for _linesRoot.
            line0: Initial value for _line0.
            line1: Initial value for _line1.
            collider: Initial value for _collider.
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
        if target_point is not None:
            self.target_point = target_point
        if normal is not None:
            self.normal = normal
        if use_custom_visual is not None:
            self.use_custom_visual = use_custom_visual
        if custom_visual_root is not None:
            self.custom_visual_root = custom_visual_root
        if handle_size is not None:
            self.handle_size = handle_size
        if handle_offset is not None:
            self.handle_offset = handle_offset
        if create_undo_steps is not None:
            self.create_undo_steps = create_undo_steps
        if visual_root is not None:
            self.visual_root = visual_root
        if visual_rotation is not None:
            self.visual_rotation = visual_rotation
        if visual_position is not None:
            self.visual_position = visual_position
        if box_size is not None:
            self.box_size = box_size
        if lines_root is not None:
            self.lines_root = lines_root
        if line0 is not None:
            self.line0 = line0
        if line1 is not None:
            self.line1 = line1
        if collider is not None:
            self.collider = collider

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
    def point_space(self) -> members.SyncObject | None:
        """The PointSpace member."""
        member = self.get_member("PointSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @point_space.setter
    def point_space(self, value: members.SyncObject) -> None:
        """Set the PointSpace member."""
        self.set_member("PointSpace", value)

    @property
    def target_point(self) -> str | None:
        """Target ID of the TargetPoint reference (targets IField[primitives.Float3])."""
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
    def normal(self) -> primitives.Float3 | None:
        """The Normal field value."""
        member = self.get_member("Normal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal.setter
    def normal(self, value: primitives.Float3) -> None:
        """Set the Normal field value."""
        member = self.get_member("Normal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Normal", fields.FieldFloat3(value=value)
            )

    @property
    def normal_space(self) -> members.SyncObject | None:
        """The NormalSpace member."""
        member = self.get_member("NormalSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @normal_space.setter
    def normal_space(self, value: members.SyncObject) -> None:
        """Set the NormalSpace member."""
        self.set_member("NormalSpace", value)

    @property
    def use_custom_visual(self) -> primitives.Bool | None:
        """The UseCustomVisual field value."""
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
        """Target ID of the _customVisualRoot reference (targets Slot)."""
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
    def handle_size(self) -> primitives.Float2 | None:
        """The HandleSize field value."""
        member = self.get_member("HandleSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @handle_size.setter
    def handle_size(self, value: primitives.Float2) -> None:
        """Set the HandleSize field value."""
        member = self.get_member("HandleSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandleSize", fields.FieldFloat2(value=value)
            )

    @property
    def handle_offset(self) -> primitives.Float2 | None:
        """The HandleOffset field value."""
        member = self.get_member("HandleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @handle_offset.setter
    def handle_offset(self, value: primitives.Float2) -> None:
        """Set the HandleOffset field value."""
        member = self.get_member("HandleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandleOffset", fields.FieldFloat2(value=value)
            )

    @property
    def create_undo_steps(self) -> primitives.Bool | None:
        """The CreateUndoSteps field value."""
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
    def visual_rotation(self) -> str | None:
        """Target ID of the _visualRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_visualRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_rotation.setter
    def visual_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _visualRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def visual_position(self) -> str | None:
        """Target ID of the _visualPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_visualPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_position.setter
    def visual_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _visualPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def box_size(self) -> str | None:
        """Target ID of the _boxSize reference (targets IField[primitives.Float3])."""
        member = self.get_member("_boxSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @box_size.setter
    def box_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _boxSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_boxSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_boxSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
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

    @property
    def collider(self) -> str | None:
        """Target ID of the _collider reference (targets BoxCollider)."""
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | BoxCollider | None) -> None:
        """Set the _collider reference by target ID or BoxCollider instance."""
        target_id: str | None = target.id if isinstance(target, BoxCollider) else target  # type: ignore[assignment]
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxCollider'),
            )

