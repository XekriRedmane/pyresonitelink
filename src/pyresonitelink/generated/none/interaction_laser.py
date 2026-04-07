"""Generated component: InteractionLaser."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.iinteraction_target import IInteractionTarget
from pyresonitelink.generated._types.ilaser_interaction_modifier import ILaserInteractionModifier
from pyresonitelink.generated._types.relay_touch_source import RelayTouchSource
from pyresonitelink.generated._types.bent_tube_mesh import BentTubeMesh
from pyresonitelink.generated._types.overlay_unlit_material import OverlayUnlitMaterial
from pyresonitelink.generated._types.static_texture2_d import StaticTexture2D
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.segment_mesh import SegmentMesh
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractionLaser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractionLaser.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractionLaser"

    def __init__(self, stick_point_space: str | Slot | None = None, handler: str | InteractionHandler | None = None, last_hit: str | Slot | None = None, last_interaction_target: str | IInteractionTarget | None = None, last_interaction_modifier: str | ILaserInteractionModifier | None = None, touch_source: str | RelayTouchSource | None = None, laser_mesh: str | BentTubeMesh | None = None, laser_material: str | OverlayUnlitMaterial | None = None, laser_texture: str | StaticTexture2D | None = None, behind_laser_tint: str | IField[primitives.ColorX] | None = None, laser_render_queue: str | IField[np.int32] | None = None, laser_front_texture_offset: str | IField[primitives.Float2] | None = None, laser_behind_texture_offset: str | IField[primitives.Float2] | None = None, direct_point: str | IField[primitives.Float3] | None = None, actual_point: str | IField[primitives.Float3] | None = None, start_color: str | IField[primitives.ColorX] | None = None, end_color: str | IField[primitives.ColorX] | None = None, point_slot: str | Slot | None = None, point_slot_pos: str | IField[primitives.Float3] | None = None, laser_visible: str | IField[bool] | None = None, cursor_visible: str | IField[bool] | None = None, cursor_root: str | Slot | None = None, cursor_image_root: str | Slot | None = None, cursor_texture: str | StaticTexture2D | None = None, cursor_material: str | OverlayUnlitMaterial | None = None, cursor_front_tint: str | IField[primitives.ColorX] | None = None, cursor_behind_tint: str | IField[primitives.ColorX] | None = None, cursor_render_queue: str | IField[np.int32] | None = None, cursor_orientation: str | IField[primitives.FloatQ] | None = None, direct_cursor_active: str | IField[bool] | None = None, direct_cursor_root: str | Slot | None = None, direct_cursor_image_root: str | Slot | None = None, direct_cursor_offset: str | IField[primitives.Float3] | None = None, direct_cursor_orientation: str | IField[primitives.FloatQ] | None = None, direct_line_target: str | IField[primitives.Float3] | None = None, direct_line_mesh: str | SegmentMesh | None = None, segment_color_front: str | IField[primitives.ColorX] | None = None, segment_color_behind: str | IField[primitives.ColorX] | None = None, segment_render_queue: str | IField[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            stick_point_space: Initial value for StickPointSpace.
            handler: Initial value for _handler.
            last_hit: Initial value for _lastHit.
            last_interaction_target: Initial value for _lastInteractionTarget.
            last_interaction_modifier: Initial value for _lastInteractionModifier.
            touch_source: Initial value for _touchSource.
            laser_mesh: Initial value for _laserMesh.
            laser_material: Initial value for _laserMaterial.
            laser_texture: Initial value for _laserTexture.
            behind_laser_tint: Initial value for _behindLaserTint.
            laser_render_queue: Initial value for _laserRenderQueue.
            laser_front_texture_offset: Initial value for _laserFrontTextureOffset.
            laser_behind_texture_offset: Initial value for _laserBehindTextureOffset.
            direct_point: Initial value for _directPoint.
            actual_point: Initial value for _actualPoint.
            start_color: Initial value for _startColor.
            end_color: Initial value for _endColor.
            point_slot: Initial value for _pointSlot.
            point_slot_pos: Initial value for _pointSlotPos.
            laser_visible: Initial value for _laserVisible.
            cursor_visible: Initial value for _cursorVisible.
            cursor_root: Initial value for _cursorRoot.
            cursor_image_root: Initial value for _cursorImageRoot.
            cursor_texture: Initial value for _cursorTexture.
            cursor_material: Initial value for _cursorMaterial.
            cursor_front_tint: Initial value for _cursorFrontTint.
            cursor_behind_tint: Initial value for _cursorBehindTint.
            cursor_render_queue: Initial value for _cursorRenderQueue.
            cursor_orientation: Initial value for _cursorOrientation.
            direct_cursor_active: Initial value for _directCursorActive.
            direct_cursor_root: Initial value for _directCursorRoot.
            direct_cursor_image_root: Initial value for _directCursorImageRoot.
            direct_cursor_offset: Initial value for _directCursorOffset.
            direct_cursor_orientation: Initial value for _directCursorOrientation.
            direct_line_target: Initial value for _directLineTarget.
            direct_line_mesh: Initial value for _directLineMesh.
            segment_color_front: Initial value for _segmentColorFront.
            segment_color_behind: Initial value for _segmentColorBehind.
            segment_render_queue: Initial value for _segmentRenderQueue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if stick_point_space is not None:
            self.stick_point_space = stick_point_space
        if handler is not None:
            self.handler = handler
        if last_hit is not None:
            self.last_hit = last_hit
        if last_interaction_target is not None:
            self.last_interaction_target = last_interaction_target
        if last_interaction_modifier is not None:
            self.last_interaction_modifier = last_interaction_modifier
        if touch_source is not None:
            self.touch_source = touch_source
        if laser_mesh is not None:
            self.laser_mesh = laser_mesh
        if laser_material is not None:
            self.laser_material = laser_material
        if laser_texture is not None:
            self.laser_texture = laser_texture
        if behind_laser_tint is not None:
            self.behind_laser_tint = behind_laser_tint
        if laser_render_queue is not None:
            self.laser_render_queue = laser_render_queue
        if laser_front_texture_offset is not None:
            self.laser_front_texture_offset = laser_front_texture_offset
        if laser_behind_texture_offset is not None:
            self.laser_behind_texture_offset = laser_behind_texture_offset
        if direct_point is not None:
            self.direct_point = direct_point
        if actual_point is not None:
            self.actual_point = actual_point
        if start_color is not None:
            self.start_color = start_color
        if end_color is not None:
            self.end_color = end_color
        if point_slot is not None:
            self.point_slot = point_slot
        if point_slot_pos is not None:
            self.point_slot_pos = point_slot_pos
        if laser_visible is not None:
            self.laser_visible = laser_visible
        if cursor_visible is not None:
            self.cursor_visible = cursor_visible
        if cursor_root is not None:
            self.cursor_root = cursor_root
        if cursor_image_root is not None:
            self.cursor_image_root = cursor_image_root
        if cursor_texture is not None:
            self.cursor_texture = cursor_texture
        if cursor_material is not None:
            self.cursor_material = cursor_material
        if cursor_front_tint is not None:
            self.cursor_front_tint = cursor_front_tint
        if cursor_behind_tint is not None:
            self.cursor_behind_tint = cursor_behind_tint
        if cursor_render_queue is not None:
            self.cursor_render_queue = cursor_render_queue
        if cursor_orientation is not None:
            self.cursor_orientation = cursor_orientation
        if direct_cursor_active is not None:
            self.direct_cursor_active = direct_cursor_active
        if direct_cursor_root is not None:
            self.direct_cursor_root = direct_cursor_root
        if direct_cursor_image_root is not None:
            self.direct_cursor_image_root = direct_cursor_image_root
        if direct_cursor_offset is not None:
            self.direct_cursor_offset = direct_cursor_offset
        if direct_cursor_orientation is not None:
            self.direct_cursor_orientation = direct_cursor_orientation
        if direct_line_target is not None:
            self.direct_line_target = direct_line_target
        if direct_line_mesh is not None:
            self.direct_line_mesh = direct_line_mesh
        if segment_color_front is not None:
            self.segment_color_front = segment_color_front
        if segment_color_behind is not None:
            self.segment_color_behind = segment_color_behind
        if segment_render_queue is not None:
            self.segment_render_queue = segment_render_queue

    @property
    def smooth_speed(self) -> np.float32 | None:
        """The SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_speed.setter
    def smooth_speed(self, value: np.float32) -> None:
        """Set the SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def smooth_modulate_start_angle(self) -> np.float32 | None:
        """The SmoothModulateStartAngle field value."""
        member = self.get_member("SmoothModulateStartAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_modulate_start_angle.setter
    def smooth_modulate_start_angle(self, value: np.float32) -> None:
        """Set the SmoothModulateStartAngle field value."""
        member = self.get_member("SmoothModulateStartAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothModulateStartAngle", fields.FieldFloat(value=value)
            )

    @property
    def smooth_modulate_end_angle(self) -> np.float32 | None:
        """The SmoothModulateEndAngle field value."""
        member = self.get_member("SmoothModulateEndAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_modulate_end_angle.setter
    def smooth_modulate_end_angle(self, value: np.float32) -> None:
        """Set the SmoothModulateEndAngle field value."""
        member = self.get_member("SmoothModulateEndAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothModulateEndAngle", fields.FieldFloat(value=value)
            )

    @property
    def smooth_modulate_exp(self) -> np.float32 | None:
        """The SmoothModulateExp field value."""
        member = self.get_member("SmoothModulateExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_modulate_exp.setter
    def smooth_modulate_exp(self, value: np.float32) -> None:
        """Set the SmoothModulateExp field value."""
        member = self.get_member("SmoothModulateExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothModulateExp", fields.FieldFloat(value=value)
            )

    @property
    def smooth_modulate_multiplier(self) -> np.float32 | None:
        """The SmoothModulateMultiplier field value."""
        member = self.get_member("SmoothModulateMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_modulate_multiplier.setter
    def smooth_modulate_multiplier(self, value: np.float32) -> None:
        """Set the SmoothModulateMultiplier field value."""
        member = self.get_member("SmoothModulateMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothModulateMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def stick_threshold(self) -> np.float32 | None:
        """The StickThreshold field value."""
        member = self.get_member("StickThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stick_threshold.setter
    def stick_threshold(self, value: np.float32) -> None:
        """Set the StickThreshold field value."""
        member = self.get_member("StickThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StickThreshold", fields.FieldFloat(value=value)
            )

    @property
    def show_in_desktop(self) -> bool | None:
        """The ShowInDesktop field value."""
        member = self.get_member("ShowInDesktop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_in_desktop.setter
    def show_in_desktop(self, value: bool) -> None:
        """Set the ShowInDesktop field value."""
        member = self.get_member("ShowInDesktop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowInDesktop", fields.FieldBool(value=value)
            )

    @property
    def max_touch_penetration_distance(self) -> np.float32 | None:
        """The MaxTouchPenetrationDistance field value."""
        member = self.get_member("MaxTouchPenetrationDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_touch_penetration_distance.setter
    def max_touch_penetration_distance(self, value: np.float32) -> None:
        """Set the MaxTouchPenetrationDistance field value."""
        member = self.get_member("MaxTouchPenetrationDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTouchPenetrationDistance", fields.FieldFloat(value=value)
            )

    @property
    def stick_point_space(self) -> str | None:
        """Target ID of the StickPointSpace reference (targets Slot)."""
        member = self.get_member("StickPointSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stick_point_space.setter
    def stick_point_space(self, target: str | Slot | None) -> None:
        """Set the StickPointSpace reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("StickPointSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StickPointSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def stick_point_position(self) -> primitives.Float3 | None:
        """The StickPointPosition field value."""
        member = self.get_member("StickPointPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stick_point_position.setter
    def stick_point_position(self, value: primitives.Float3) -> None:
        """Set the StickPointPosition field value."""
        member = self.get_member("StickPointPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StickPointPosition", fields.FieldFloat3(value=value)
            )

    @property
    def handler(self) -> str | None:
        """Target ID of the _handler reference (targets InteractionHandler)."""
        member = self.get_member("_handler")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handler.setter
    def handler(self, target: str | InteractionHandler | None) -> None:
        """Set the _handler reference by target ID or InteractionHandler instance."""
        target_id: str | None = target.id if isinstance(target, InteractionHandler) else target  # type: ignore[assignment]
        member = self.get_member("_handler")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handler",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandler'),
            )

    @property
    def last_hit(self) -> str | None:
        """Target ID of the _lastHit reference (targets Slot)."""
        member = self.get_member("_lastHit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_hit.setter
    def last_hit(self, target: str | Slot | None) -> None:
        """Set the _lastHit reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_lastHit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastHit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def last_interaction_target(self) -> str | None:
        """Target ID of the _lastInteractionTarget reference (targets IInteractionTarget)."""
        member = self.get_member("_lastInteractionTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_interaction_target.setter
    def last_interaction_target(self, target: str | IInteractionTarget | None) -> None:
        """Set the _lastInteractionTarget reference by target ID or IInteractionTarget instance."""
        target_id: str | None = target.id if isinstance(target, IInteractionTarget) else target  # type: ignore[assignment]
        member = self.get_member("_lastInteractionTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastInteractionTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IInteractionTarget'),
            )

    @property
    def last_interaction_modifier(self) -> str | None:
        """Target ID of the _lastInteractionModifier reference (targets ILaserInteractionModifier)."""
        member = self.get_member("_lastInteractionModifier")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_interaction_modifier.setter
    def last_interaction_modifier(self, target: str | ILaserInteractionModifier | None) -> None:
        """Set the _lastInteractionModifier reference by target ID or ILaserInteractionModifier instance."""
        target_id: str | None = target.id if isinstance(target, ILaserInteractionModifier) else target  # type: ignore[assignment]
        member = self.get_member("_lastInteractionModifier")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastInteractionModifier",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ILaserInteractionModifier'),
            )

    @property
    def hit_color(self) -> primitives.ColorX | None:
        """The _hitColor field value."""
        member = self.get_member("_hitColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hit_color.setter
    def hit_color(self, value: primitives.ColorX) -> None:
        """Set the _hitColor field value."""
        member = self.get_member("_hitColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_hitColor", fields.FieldColorX(value=value)
            )

    @property
    def laser_texture_speed(self) -> np.float32 | None:
        """The _laserTextureSpeed field value."""
        member = self.get_member("_laserTextureSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laser_texture_speed.setter
    def laser_texture_speed(self, value: np.float32) -> None:
        """Set the _laserTextureSpeed field value."""
        member = self.get_member("_laserTextureSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_laserTextureSpeed", fields.FieldFloat(value=value)
            )

    @property
    def touch_source(self) -> str | None:
        """Target ID of the _touchSource reference (targets RelayTouchSource)."""
        member = self.get_member("_touchSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @touch_source.setter
    def touch_source(self, target: str | RelayTouchSource | None) -> None:
        """Set the _touchSource reference by target ID or RelayTouchSource instance."""
        target_id: str | None = target.id if isinstance(target, RelayTouchSource) else target  # type: ignore[assignment]
        member = self.get_member("_touchSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_touchSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RelayTouchSource'),
            )

    @property
    def laser_mesh(self) -> str | None:
        """Target ID of the _laserMesh reference (targets BentTubeMesh)."""
        member = self.get_member("_laserMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_mesh.setter
    def laser_mesh(self, target: str | BentTubeMesh | None) -> None:
        """Set the _laserMesh reference by target ID or BentTubeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BentTubeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_laserMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BentTubeMesh'),
            )

    @property
    def laser_material(self) -> str | None:
        """Target ID of the _laserMaterial reference (targets OverlayUnlitMaterial)."""
        member = self.get_member("_laserMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_material.setter
    def laser_material(self, target: str | OverlayUnlitMaterial | None) -> None:
        """Set the _laserMaterial reference by target ID or OverlayUnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayUnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_laserMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayUnlitMaterial'),
            )

    @property
    def laser_texture(self) -> str | None:
        """Target ID of the _laserTexture reference (targets StaticTexture2D)."""
        member = self.get_member("_laserTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_texture.setter
    def laser_texture(self, target: str | StaticTexture2D | None) -> None:
        """Set the _laserTexture reference by target ID or StaticTexture2D instance."""
        target_id: str | None = target.id if isinstance(target, StaticTexture2D) else target  # type: ignore[assignment]
        member = self.get_member("_laserTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticTexture2D'),
            )

    @property
    def behind_laser_tint(self) -> str | None:
        """Target ID of the _behindLaserTint reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_behindLaserTint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @behind_laser_tint.setter
    def behind_laser_tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _behindLaserTint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_behindLaserTint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_behindLaserTint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def laser_render_queue(self) -> str | None:
        """Target ID of the _laserRenderQueue reference (targets IField[np.int32])."""
        member = self.get_member("_laserRenderQueue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_render_queue.setter
    def laser_render_queue(self, target: str | IField[np.int32] | None) -> None:
        """Set the _laserRenderQueue reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_laserRenderQueue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserRenderQueue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def laser_front_texture_offset(self) -> str | None:
        """Target ID of the _laserFrontTextureOffset reference (targets IField[primitives.Float2])."""
        member = self.get_member("_laserFrontTextureOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_front_texture_offset.setter
    def laser_front_texture_offset(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _laserFrontTextureOffset reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_laserFrontTextureOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserFrontTextureOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def laser_behind_texture_offset(self) -> str | None:
        """Target ID of the _laserBehindTextureOffset reference (targets IField[primitives.Float2])."""
        member = self.get_member("_laserBehindTextureOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_behind_texture_offset.setter
    def laser_behind_texture_offset(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _laserBehindTextureOffset reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_laserBehindTextureOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserBehindTextureOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def direct_point(self) -> str | None:
        """Target ID of the _directPoint reference (targets IField[primitives.Float3])."""
        member = self.get_member("_directPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_point.setter
    def direct_point(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _directPoint reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_directPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def actual_point(self) -> str | None:
        """Target ID of the _actualPoint reference (targets IField[primitives.Float3])."""
        member = self.get_member("_actualPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @actual_point.setter
    def actual_point(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _actualPoint reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_actualPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_actualPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def start_color(self) -> str | None:
        """Target ID of the _startColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_startColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @start_color.setter
    def start_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _startColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_startColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_startColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def end_color(self) -> str | None:
        """Target ID of the _endColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_endColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @end_color.setter
    def end_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _endColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_endColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_endColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def point_slot(self) -> str | None:
        """Target ID of the _pointSlot reference (targets Slot)."""
        member = self.get_member("_pointSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point_slot.setter
    def point_slot(self, target: str | Slot | None) -> None:
        """Set the _pointSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_pointSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pointSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def point_slot_pos(self) -> str | None:
        """Target ID of the _pointSlotPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_pointSlotPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point_slot_pos.setter
    def point_slot_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _pointSlotPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_pointSlotPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pointSlotPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def laser_visible(self) -> str | None:
        """Target ID of the _laserVisible reference (targets IField[bool])."""
        member = self.get_member("_laserVisible")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_visible.setter
    def laser_visible(self, target: str | IField[bool] | None) -> None:
        """Set the _laserVisible reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_laserVisible")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserVisible",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def cursor_visible(self) -> str | None:
        """Target ID of the _cursorVisible reference (targets IField[bool])."""
        member = self.get_member("_cursorVisible")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_visible.setter
    def cursor_visible(self, target: str | IField[bool] | None) -> None:
        """Set the _cursorVisible reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cursorVisible")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorVisible",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def cursor_root(self) -> str | None:
        """Target ID of the _cursorRoot reference (targets Slot)."""
        member = self.get_member("_cursorRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_root.setter
    def cursor_root(self, target: str | Slot | None) -> None:
        """Set the _cursorRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_cursorRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def cursor_image_root(self) -> str | None:
        """Target ID of the _cursorImageRoot reference (targets Slot)."""
        member = self.get_member("_cursorImageRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_image_root.setter
    def cursor_image_root(self, target: str | Slot | None) -> None:
        """Set the _cursorImageRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_cursorImageRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorImageRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def cursor_texture(self) -> str | None:
        """Target ID of the _cursorTexture reference (targets StaticTexture2D)."""
        member = self.get_member("_cursorTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_texture.setter
    def cursor_texture(self, target: str | StaticTexture2D | None) -> None:
        """Set the _cursorTexture reference by target ID or StaticTexture2D instance."""
        target_id: str | None = target.id if isinstance(target, StaticTexture2D) else target  # type: ignore[assignment]
        member = self.get_member("_cursorTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticTexture2D'),
            )

    @property
    def cursor_material(self) -> str | None:
        """Target ID of the _cursorMaterial reference (targets OverlayUnlitMaterial)."""
        member = self.get_member("_cursorMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_material.setter
    def cursor_material(self, target: str | OverlayUnlitMaterial | None) -> None:
        """Set the _cursorMaterial reference by target ID or OverlayUnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayUnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_cursorMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayUnlitMaterial'),
            )

    @property
    def cursor_front_tint(self) -> str | None:
        """Target ID of the _cursorFrontTint reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_cursorFrontTint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_front_tint.setter
    def cursor_front_tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _cursorFrontTint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cursorFrontTint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorFrontTint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def cursor_behind_tint(self) -> str | None:
        """Target ID of the _cursorBehindTint reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_cursorBehindTint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_behind_tint.setter
    def cursor_behind_tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _cursorBehindTint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cursorBehindTint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorBehindTint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def cursor_render_queue(self) -> str | None:
        """Target ID of the _cursorRenderQueue reference (targets IField[np.int32])."""
        member = self.get_member("_cursorRenderQueue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_render_queue.setter
    def cursor_render_queue(self, target: str | IField[np.int32] | None) -> None:
        """Set the _cursorRenderQueue reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cursorRenderQueue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorRenderQueue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def cursor_orientation(self) -> str | None:
        """Target ID of the _cursorOrientation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_cursorOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_orientation.setter
    def cursor_orientation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _cursorOrientation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cursorOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def cursor_tint(self) -> primitives.ColorX | None:
        """The _cursorTint field value."""
        member = self.get_member("_cursorTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_tint.setter
    def cursor_tint(self, value: primitives.ColorX) -> None:
        """Set the _cursorTint field value."""
        member = self.get_member("_cursorTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_cursorTint", fields.FieldColorX(value=value)
            )

    @property
    def direct_cursor_visuals_visible(self) -> bool | None:
        """The _directCursorVisualsVisible field value."""
        member = self.get_member("_directCursorVisualsVisible")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direct_cursor_visuals_visible.setter
    def direct_cursor_visuals_visible(self, value: bool) -> None:
        """Set the _directCursorVisualsVisible field value."""
        member = self.get_member("_directCursorVisualsVisible")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_directCursorVisualsVisible", fields.FieldBool(value=value)
            )

    @property
    def direct_cursor_active(self) -> str | None:
        """Target ID of the _directCursorActive reference (targets IField[bool])."""
        member = self.get_member("_directCursorActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_cursor_active.setter
    def direct_cursor_active(self, target: str | IField[bool] | None) -> None:
        """Set the _directCursorActive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_directCursorActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directCursorActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def direct_cursor_root(self) -> str | None:
        """Target ID of the _directCursorRoot reference (targets Slot)."""
        member = self.get_member("_directCursorRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_cursor_root.setter
    def direct_cursor_root(self, target: str | Slot | None) -> None:
        """Set the _directCursorRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_directCursorRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directCursorRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def direct_cursor_image_root(self) -> str | None:
        """Target ID of the _directCursorImageRoot reference (targets Slot)."""
        member = self.get_member("_directCursorImageRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_cursor_image_root.setter
    def direct_cursor_image_root(self, target: str | Slot | None) -> None:
        """Set the _directCursorImageRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_directCursorImageRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directCursorImageRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def direct_cursor_offset(self) -> str | None:
        """Target ID of the _directCursorOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_directCursorOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_cursor_offset.setter
    def direct_cursor_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _directCursorOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_directCursorOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directCursorOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def direct_cursor_orientation(self) -> str | None:
        """Target ID of the _directCursorOrientation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_directCursorOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_cursor_orientation.setter
    def direct_cursor_orientation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _directCursorOrientation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_directCursorOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directCursorOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def direct_line_target(self) -> str | None:
        """Target ID of the _directLineTarget reference (targets IField[primitives.Float3])."""
        member = self.get_member("_directLineTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_line_target.setter
    def direct_line_target(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _directLineTarget reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_directLineTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directLineTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def direct_line_mesh(self) -> str | None:
        """Target ID of the _directLineMesh reference (targets SegmentMesh)."""
        member = self.get_member("_directLineMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direct_line_mesh.setter
    def direct_line_mesh(self, target: str | SegmentMesh | None) -> None:
        """Set the _directLineMesh reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_directLineMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directLineMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def segment_color_front(self) -> str | None:
        """Target ID of the _segmentColorFront reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_segmentColorFront")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @segment_color_front.setter
    def segment_color_front(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _segmentColorFront reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_segmentColorFront")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_segmentColorFront",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def segment_color_behind(self) -> str | None:
        """Target ID of the _segmentColorBehind reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_segmentColorBehind")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @segment_color_behind.setter
    def segment_color_behind(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _segmentColorBehind reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_segmentColorBehind")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_segmentColorBehind",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def segment_render_queue(self) -> str | None:
        """Target ID of the _segmentRenderQueue reference (targets IField[np.int32])."""
        member = self.get_member("_segmentRenderQueue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @segment_render_queue.setter
    def segment_render_queue(self, target: str | IField[np.int32] | None) -> None:
        """Set the _segmentRenderQueue reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_segmentRenderQueue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_segmentRenderQueue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

