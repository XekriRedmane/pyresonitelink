"""Generated component: VolumeTranslationGizmo."""

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


class VolumeTranslationGizmo(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VolumeTranslationGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VolumeTranslationGizmo"

    def __init__(self, target_slot: str | Slot | None = None, auto_position_at_target_slot: primitives.Bool | None = None, interacting_component: str | Component | None = None, material: str | OverlayFresnelMaterial | None = None, tool_point: str | Slot | None = None, active_point: str | Slot | None = None, line_root: str | Slot | None = None, line_segment: str | SegmentMesh | None = None, snap_highlight: str | Slot | None = None, target_point: str | IField[primitives.Float3] | None = None, use_custom_visual: primitives.Bool | None = None, custom_visual_root: str | Slot | None = None, visual_root: str | Slot | None = None, cube_size: primitives.Float | None = None, create_undo_steps: primitives.Bool | None = None, collider_size: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
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
            use_custom_visual: Initial value for UseCustomVisual.
            custom_visual_root: Initial value for _customVisualRoot.
            visual_root: Initial value for _visualRoot.
            cube_size: Initial value for CubeSize.
            create_undo_steps: Initial value for CreateUndoSteps.
            collider_size: Initial value for _colliderSize.
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
        if use_custom_visual is not None:
            self.use_custom_visual = use_custom_visual
        if custom_visual_root is not None:
            self.custom_visual_root = custom_visual_root
        if visual_root is not None:
            self.visual_root = visual_root
        if cube_size is not None:
            self.cube_size = cube_size
        if create_undo_steps is not None:
            self.create_undo_steps = create_undo_steps
        if collider_size is not None:
            self.collider_size = collider_size

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
    def cube_size(self) -> primitives.Float | None:
        """The CubeSize field value."""
        member = self.get_member("CubeSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cube_size.setter
    def cube_size(self, value: primitives.Float) -> None:
        """Set the CubeSize field value."""
        member = self.get_member("CubeSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CubeSize", fields.FieldFloat(value=value)
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
    def cube_size(self) -> str | None:
        """Target ID of the _cubeSize reference (targets IField[primitives.Float3])."""
        member = self.get_member("_cubeSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cube_size.setter
    def cube_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _cubeSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cubeSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cubeSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def collider_size(self) -> str | None:
        """Target ID of the _colliderSize reference (targets IField[primitives.Float3])."""
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_size.setter
    def collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

