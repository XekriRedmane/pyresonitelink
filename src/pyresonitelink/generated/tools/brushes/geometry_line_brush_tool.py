"""Generated component: GeometryLineBrushTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.particle_system import ParticleSystem
from pyresonitelink.generated._types.mesh_emitter import MeshEmitter
from pyresonitelink.generated._types.color_dialog_interface import ColorDialogInterface
from pyresonitelink.generated._types.multi_line_mesh import MultiLineMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GeometryLineBrushTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GeometryLineBrushTool.

    Category: Tools/Brushes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GeometryLineBrushTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, fixed_minimum_point_distance: primitives.Float | None = None, position_smoothing: primitives.Float | None = None, rotation_smoothing: primitives.Float | None = None, pressure_smoothing: primitives.Float | None = None, max_stroke_length: primitives.Float | None = None, stroke_fade_in_length: primitives.Float | None = None, stroke_fade_out_length: primitives.Float | None = None, stroke_group_finish_wait_time: primitives.Float | None = None, activation_threshold: primitives.Float | None = None, deactivation_threshold_ratio: primitives.Float | None = None, menu_size_change: primitives.Float | None = None, snap_tip: primitives.Bool | None = None, snap_line: primitives.Bool | None = None, make_strokes_grabbable: primitives.Bool | None = None, position_strokes_to_tip: primitives.Bool | None = None, orient_strokes_to_tip: primitives.Bool | None = None, scale_strokes_to_user: primitives.Bool | None = None, pick_materials: primitives.Bool | None = None, pick_colors: primitives.Bool | None = None, current_material: str | IAssetProvider[Material] | None = None, particle_system: str | ParticleSystem | None = None, mesh_emitter_template: str | MeshEmitter | None = None, emission_rate_per_unit_length: primitives.Float | None = None, color_picker: str | ColorDialogInterface | None = None, picked_color: primitives.ColorX | None = None, last_used_material: str | IAssetProvider[Material] | None = None, last_created_material: str | IAssetProvider[Material] | None = None, pressure: primitives.Float | None = None, position: primitives.Float3 | None = None, rotation: primitives.FloatQ | None = None, last_point_delta: primitives.Float3 | None = None, velocity: primitives.Float3 | None = None, raw_delta: primitives.Float3 | None = None, raw_velocity: primitives.Float3 | None = None, raw_stroke_length: primitives.Float | None = None, stroke_length: primitives.Float | None = None, normalized_stroke_length: primitives.Float | None = None, stroke_fade_multiplier: primitives.Float | None = None, stroke_group_index: primitives.Int | None = None, stroke_group_active: primitives.Bool | None = None, tip_anchor: str | Slot | None = None, use_relative_minimum_point_distance: primitives.Bool | None = None, relative_minimum_point_distance_ratio: primitives.Float | None = None, pressure_affects_size: primitives.Bool | None = None, preview_mesh: str | MultiLineMesh | None = None, preview_mesh_offset: str | IField[primitives.Float3] | None = None, size_knob: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            fixed_minimum_point_distance: Initial value for FixedMinimumPointDistance.
            position_smoothing: Initial value for PositionSmoothing.
            rotation_smoothing: Initial value for RotationSmoothing.
            pressure_smoothing: Initial value for PressureSmoothing.
            max_stroke_length: Initial value for MaxStrokeLength.
            stroke_fade_in_length: Initial value for StrokeFadeInLength.
            stroke_fade_out_length: Initial value for StrokeFadeOutLength.
            stroke_group_finish_wait_time: Initial value for StrokeGroupFinishWaitTime.
            activation_threshold: Initial value for ActivationThreshold.
            deactivation_threshold_ratio: Initial value for DeactivationThresholdRatio.
            menu_size_change: Initial value for MenuSizeChange.
            snap_tip: Initial value for SnapTip.
            snap_line: Initial value for SnapLine.
            make_strokes_grabbable: Initial value for MakeStrokesGrabbable.
            position_strokes_to_tip: Initial value for PositionStrokesToTip.
            orient_strokes_to_tip: Initial value for OrientStrokesToTip.
            scale_strokes_to_user: Initial value for ScaleStrokesToUser.
            pick_materials: Initial value for PickMaterials.
            pick_colors: Initial value for PickColors.
            current_material: Initial value for CurrentMaterial.
            particle_system: Initial value for ParticleSystem.
            mesh_emitter_template: Initial value for MeshEmitterTemplate.
            emission_rate_per_unit_length: Initial value for EmissionRatePerUnitLength.
            color_picker: Initial value for _colorPicker.
            picked_color: Initial value for _pickedColor.
            last_used_material: Initial value for _lastUsedMaterial.
            last_created_material: Initial value for _lastCreatedMaterial.
            pressure: Initial value for Pressure.
            position: Initial value for Position.
            rotation: Initial value for Rotation.
            last_point_delta: Initial value for LastPointDelta.
            velocity: Initial value for Velocity.
            raw_delta: Initial value for RawDelta.
            raw_velocity: Initial value for RawVelocity.
            raw_stroke_length: Initial value for RawStrokeLength.
            stroke_length: Initial value for StrokeLength.
            normalized_stroke_length: Initial value for NormalizedStrokeLength.
            stroke_fade_multiplier: Initial value for StrokeFadeMultiplier.
            stroke_group_index: Initial value for StrokeGroupIndex.
            stroke_group_active: Initial value for StrokeGroupActive.
            tip_anchor: Initial value for TipAnchor.
            use_relative_minimum_point_distance: Initial value for UseRelativeMinimumPointDistance.
            relative_minimum_point_distance_ratio: Initial value for RelativeMinimumPointDistanceRatio.
            pressure_affects_size: Initial value for PressureAffectsSize.
            preview_mesh: Initial value for _previewMesh.
            preview_mesh_offset: Initial value for _previewMeshOffset.
            size_knob: Initial value for _sizeKnob.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tip_reference is not None:
            self.tip_reference = tip_reference
        if block_grip_equip is not None:
            self.block_grip_equip = block_grip_equip
        if block_remote_equip is not None:
            self.block_remote_equip = block_remote_equip
        if equip_name is not None:
            self.equip_name = equip_name
        if override_active_tool is not None:
            self.override_active_tool = override_active_tool
        if grip_poses_generated is not None:
            self.grip_poses_generated = grip_poses_generated
        if fixed_minimum_point_distance is not None:
            self.fixed_minimum_point_distance = fixed_minimum_point_distance
        if position_smoothing is not None:
            self.position_smoothing = position_smoothing
        if rotation_smoothing is not None:
            self.rotation_smoothing = rotation_smoothing
        if pressure_smoothing is not None:
            self.pressure_smoothing = pressure_smoothing
        if max_stroke_length is not None:
            self.max_stroke_length = max_stroke_length
        if stroke_fade_in_length is not None:
            self.stroke_fade_in_length = stroke_fade_in_length
        if stroke_fade_out_length is not None:
            self.stroke_fade_out_length = stroke_fade_out_length
        if stroke_group_finish_wait_time is not None:
            self.stroke_group_finish_wait_time = stroke_group_finish_wait_time
        if activation_threshold is not None:
            self.activation_threshold = activation_threshold
        if deactivation_threshold_ratio is not None:
            self.deactivation_threshold_ratio = deactivation_threshold_ratio
        if menu_size_change is not None:
            self.menu_size_change = menu_size_change
        if snap_tip is not None:
            self.snap_tip = snap_tip
        if snap_line is not None:
            self.snap_line = snap_line
        if make_strokes_grabbable is not None:
            self.make_strokes_grabbable = make_strokes_grabbable
        if position_strokes_to_tip is not None:
            self.position_strokes_to_tip = position_strokes_to_tip
        if orient_strokes_to_tip is not None:
            self.orient_strokes_to_tip = orient_strokes_to_tip
        if scale_strokes_to_user is not None:
            self.scale_strokes_to_user = scale_strokes_to_user
        if pick_materials is not None:
            self.pick_materials = pick_materials
        if pick_colors is not None:
            self.pick_colors = pick_colors
        if current_material is not None:
            self.current_material = current_material
        if particle_system is not None:
            self.particle_system = particle_system
        if mesh_emitter_template is not None:
            self.mesh_emitter_template = mesh_emitter_template
        if emission_rate_per_unit_length is not None:
            self.emission_rate_per_unit_length = emission_rate_per_unit_length
        if color_picker is not None:
            self.color_picker = color_picker
        if picked_color is not None:
            self.picked_color = picked_color
        if last_used_material is not None:
            self.last_used_material = last_used_material
        if last_created_material is not None:
            self.last_created_material = last_created_material
        if pressure is not None:
            self.pressure = pressure
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if last_point_delta is not None:
            self.last_point_delta = last_point_delta
        if velocity is not None:
            self.velocity = velocity
        if raw_delta is not None:
            self.raw_delta = raw_delta
        if raw_velocity is not None:
            self.raw_velocity = raw_velocity
        if raw_stroke_length is not None:
            self.raw_stroke_length = raw_stroke_length
        if stroke_length is not None:
            self.stroke_length = stroke_length
        if normalized_stroke_length is not None:
            self.normalized_stroke_length = normalized_stroke_length
        if stroke_fade_multiplier is not None:
            self.stroke_fade_multiplier = stroke_fade_multiplier
        if stroke_group_index is not None:
            self.stroke_group_index = stroke_group_index
        if stroke_group_active is not None:
            self.stroke_group_active = stroke_group_active
        if tip_anchor is not None:
            self.tip_anchor = tip_anchor
        if use_relative_minimum_point_distance is not None:
            self.use_relative_minimum_point_distance = use_relative_minimum_point_distance
        if relative_minimum_point_distance_ratio is not None:
            self.relative_minimum_point_distance_ratio = relative_minimum_point_distance_ratio
        if pressure_affects_size is not None:
            self.pressure_affects_size = pressure_affects_size
        if preview_mesh is not None:
            self.preview_mesh = preview_mesh
        if preview_mesh_offset is not None:
            self.preview_mesh_offset = preview_mesh_offset
        if size_knob is not None:
            self.size_knob = size_knob

    @property
    def equip_link(self) -> members.EmptyElement | None:
        """The _equipLink member."""
        member = self.get_member("_equipLink")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @equip_link.setter
    def equip_link(self, value: members.EmptyElement) -> None:
        """Set the _equipLink member."""
        self.set_member("_equipLink", value)

    @property
    def tip_reference(self) -> str | None:
        """Target ID of the TipReference reference (targets Slot)."""
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tip_reference.setter
    def tip_reference(self, target: str | Slot | None) -> None:
        """Set the TipReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def block_grip_equip(self) -> primitives.Bool | None:
        """The BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_grip_equip.setter
    def block_grip_equip(self, value: primitives.Bool) -> None:
        """Set the BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockGripEquip", fields.FieldBool(value=value)
            )

    @property
    def block_remote_equip(self) -> primitives.Bool | None:
        """The BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_remote_equip.setter
    def block_remote_equip(self, value: primitives.Bool) -> None:
        """Set the BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockRemoteEquip", fields.FieldBool(value=value)
            )

    @property
    def equip_name(self) -> primitives.String | None:
        """The EquipName field value."""
        member = self.get_member("EquipName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equip_name.setter
    def equip_name(self, value: primitives.String) -> None:
        """Set the EquipName field value."""
        member = self.get_member("EquipName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EquipName", fields.FieldString(value=value)
            )

    @property
    def override_active_tool(self) -> str | None:
        """Target ID of the _overrideActiveTool reference (targets InteractionHandler)."""
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_active_tool.setter
    def override_active_tool(self, target: str | InteractionHandler | None) -> None:
        """Set the _overrideActiveTool reference by target ID or InteractionHandler instance."""
        target_id: str | None = target.id if isinstance(target, InteractionHandler) else target  # type: ignore[assignment]
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overrideActiveTool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandler'),
            )

    @property
    def grip_poses_generated(self) -> primitives.Bool | None:
        """The _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_poses_generated.setter
    def grip_poses_generated(self, value: primitives.Bool) -> None:
        """Set the _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_gripPosesGenerated", fields.FieldBool(value=value)
            )

    @property
    def fixed_minimum_point_distance(self) -> primitives.Float | None:
        """The FixedMinimumPointDistance field value."""
        member = self.get_member("FixedMinimumPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fixed_minimum_point_distance.setter
    def fixed_minimum_point_distance(self, value: primitives.Float) -> None:
        """Set the FixedMinimumPointDistance field value."""
        member = self.get_member("FixedMinimumPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixedMinimumPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def position_smoothing(self) -> primitives.Float | None:
        """The PositionSmoothing field value."""
        member = self.get_member("PositionSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_smoothing.setter
    def position_smoothing(self, value: primitives.Float) -> None:
        """Set the PositionSmoothing field value."""
        member = self.get_member("PositionSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionSmoothing", fields.FieldFloat(value=value)
            )

    @property
    def rotation_smoothing(self) -> primitives.Float | None:
        """The RotationSmoothing field value."""
        member = self.get_member("RotationSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_smoothing.setter
    def rotation_smoothing(self, value: primitives.Float) -> None:
        """Set the RotationSmoothing field value."""
        member = self.get_member("RotationSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationSmoothing", fields.FieldFloat(value=value)
            )

    @property
    def pressure_smoothing(self) -> primitives.Float | None:
        """The PressureSmoothing field value."""
        member = self.get_member("PressureSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressure_smoothing.setter
    def pressure_smoothing(self, value: primitives.Float) -> None:
        """Set the PressureSmoothing field value."""
        member = self.get_member("PressureSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressureSmoothing", fields.FieldFloat(value=value)
            )

    @property
    def max_stroke_length(self) -> primitives.Float | None:
        """The MaxStrokeLength field value."""
        member = self.get_member("MaxStrokeLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_stroke_length.setter
    def max_stroke_length(self, value: primitives.Float) -> None:
        """Set the MaxStrokeLength field value."""
        member = self.get_member("MaxStrokeLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxStrokeLength", fields.FieldFloat(value=value)
            )

    @property
    def stroke_fade_in_length(self) -> primitives.Float | None:
        """The StrokeFadeInLength field value."""
        member = self.get_member("StrokeFadeInLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stroke_fade_in_length.setter
    def stroke_fade_in_length(self, value: primitives.Float) -> None:
        """Set the StrokeFadeInLength field value."""
        member = self.get_member("StrokeFadeInLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrokeFadeInLength", fields.FieldFloat(value=value)
            )

    @property
    def stroke_fade_out_length(self) -> primitives.Float | None:
        """The StrokeFadeOutLength field value."""
        member = self.get_member("StrokeFadeOutLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stroke_fade_out_length.setter
    def stroke_fade_out_length(self, value: primitives.Float) -> None:
        """Set the StrokeFadeOutLength field value."""
        member = self.get_member("StrokeFadeOutLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrokeFadeOutLength", fields.FieldFloat(value=value)
            )

    @property
    def stroke_group_finish_wait_time(self) -> primitives.Float | None:
        """The StrokeGroupFinishWaitTime field value."""
        member = self.get_member("StrokeGroupFinishWaitTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stroke_group_finish_wait_time.setter
    def stroke_group_finish_wait_time(self, value: primitives.Float) -> None:
        """Set the StrokeGroupFinishWaitTime field value."""
        member = self.get_member("StrokeGroupFinishWaitTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrokeGroupFinishWaitTime", fields.FieldFloat(value=value)
            )

    @property
    def activation_threshold(self) -> primitives.Float | None:
        """The ActivationThreshold field value."""
        member = self.get_member("ActivationThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activation_threshold.setter
    def activation_threshold(self, value: primitives.Float) -> None:
        """Set the ActivationThreshold field value."""
        member = self.get_member("ActivationThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivationThreshold", fields.FieldFloat(value=value)
            )

    @property
    def deactivation_threshold_ratio(self) -> primitives.Float | None:
        """The DeactivationThresholdRatio field value."""
        member = self.get_member("DeactivationThresholdRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @deactivation_threshold_ratio.setter
    def deactivation_threshold_ratio(self, value: primitives.Float) -> None:
        """Set the DeactivationThresholdRatio field value."""
        member = self.get_member("DeactivationThresholdRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeactivationThresholdRatio", fields.FieldFloat(value=value)
            )

    @property
    def menu_size_change(self) -> primitives.Float | None:
        """The MenuSizeChange field value."""
        member = self.get_member("MenuSizeChange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @menu_size_change.setter
    def menu_size_change(self, value: primitives.Float) -> None:
        """Set the MenuSizeChange field value."""
        member = self.get_member("MenuSizeChange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MenuSizeChange", fields.FieldFloat(value=value)
            )

    @property
    def snap_tip(self) -> primitives.Bool | None:
        """The SnapTip field value."""
        member = self.get_member("SnapTip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_tip.setter
    def snap_tip(self, value: primitives.Bool) -> None:
        """Set the SnapTip field value."""
        member = self.get_member("SnapTip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapTip", fields.FieldBool(value=value)
            )

    @property
    def snap_line(self) -> primitives.Bool | None:
        """The SnapLine field value."""
        member = self.get_member("SnapLine")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_line.setter
    def snap_line(self, value: primitives.Bool) -> None:
        """Set the SnapLine field value."""
        member = self.get_member("SnapLine")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapLine", fields.FieldBool(value=value)
            )

    @property
    def strokes_space(self) -> members.SyncObject | None:
        """The StrokesSpace member."""
        member = self.get_member("StrokesSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @strokes_space.setter
    def strokes_space(self, value: members.SyncObject) -> None:
        """Set the StrokesSpace member."""
        self.set_member("StrokesSpace", value)

    @property
    def make_strokes_grabbable(self) -> primitives.Bool | None:
        """The MakeStrokesGrabbable field value."""
        member = self.get_member("MakeStrokesGrabbable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @make_strokes_grabbable.setter
    def make_strokes_grabbable(self, value: primitives.Bool) -> None:
        """Set the MakeStrokesGrabbable field value."""
        member = self.get_member("MakeStrokesGrabbable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MakeStrokesGrabbable", fields.FieldBool(value=value)
            )

    @property
    def position_strokes_to_tip(self) -> primitives.Bool | None:
        """The PositionStrokesToTip field value."""
        member = self.get_member("PositionStrokesToTip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_strokes_to_tip.setter
    def position_strokes_to_tip(self, value: primitives.Bool) -> None:
        """Set the PositionStrokesToTip field value."""
        member = self.get_member("PositionStrokesToTip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionStrokesToTip", fields.FieldBool(value=value)
            )

    @property
    def orient_strokes_to_tip(self) -> primitives.Bool | None:
        """The OrientStrokesToTip field value."""
        member = self.get_member("OrientStrokesToTip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orient_strokes_to_tip.setter
    def orient_strokes_to_tip(self, value: primitives.Bool) -> None:
        """Set the OrientStrokesToTip field value."""
        member = self.get_member("OrientStrokesToTip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OrientStrokesToTip", fields.FieldBool(value=value)
            )

    @property
    def scale_strokes_to_user(self) -> primitives.Bool | None:
        """The ScaleStrokesToUser field value."""
        member = self.get_member("ScaleStrokesToUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_strokes_to_user.setter
    def scale_strokes_to_user(self, value: primitives.Bool) -> None:
        """Set the ScaleStrokesToUser field value."""
        member = self.get_member("ScaleStrokesToUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleStrokesToUser", fields.FieldBool(value=value)
            )

    @property
    def pick_materials(self) -> primitives.Bool | None:
        """The PickMaterials field value."""
        member = self.get_member("PickMaterials")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pick_materials.setter
    def pick_materials(self, value: primitives.Bool) -> None:
        """Set the PickMaterials field value."""
        member = self.get_member("PickMaterials")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PickMaterials", fields.FieldBool(value=value)
            )

    @property
    def pick_colors(self) -> primitives.Bool | None:
        """The PickColors field value."""
        member = self.get_member("PickColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pick_colors.setter
    def pick_colors(self, value: primitives.Bool) -> None:
        """Set the PickColors field value."""
        member = self.get_member("PickColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PickColors", fields.FieldBool(value=value)
            )

    @property
    def current_material(self) -> str | None:
        """Target ID of the CurrentMaterial reference (targets IAssetProvider[Material])."""
        member = self.get_member("CurrentMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_material.setter
    def current_material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the CurrentMaterial reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("CurrentMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CurrentMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def color_mappings(self) -> members.SyncList | None:
        """The ColorMappings member."""
        member = self.get_member("ColorMappings")
        if isinstance(member, members.SyncList):
            return member
        return None

    @color_mappings.setter
    def color_mappings(self, value: members.SyncList) -> None:
        """Set the ColorMappings member."""
        self.set_member("ColorMappings", value)

    @property
    def particle_system(self) -> str | None:
        """Target ID of the ParticleSystem reference (targets ParticleSystem)."""
        member = self.get_member("ParticleSystem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @particle_system.setter
    def particle_system(self, target: str | ParticleSystem | None) -> None:
        """Set the ParticleSystem reference by target ID or ParticleSystem instance."""
        target_id: str | None = target.id if isinstance(target, ParticleSystem) else target  # type: ignore[assignment]
        member = self.get_member("ParticleSystem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParticleSystem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ParticleSystem'),
            )

    @property
    def mesh_emitter_template(self) -> str | None:
        """Target ID of the MeshEmitterTemplate reference (targets MeshEmitter)."""
        member = self.get_member("MeshEmitterTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh_emitter_template.setter
    def mesh_emitter_template(self, target: str | MeshEmitter | None) -> None:
        """Set the MeshEmitterTemplate reference by target ID or MeshEmitter instance."""
        target_id: str | None = target.id if isinstance(target, MeshEmitter) else target  # type: ignore[assignment]
        member = self.get_member("MeshEmitterTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MeshEmitterTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.MeshEmitter'),
            )

    @property
    def particle_template_handling(self) -> members.FieldEnum | None:
        """The ParticleTemplateHandling member."""
        member = self.get_member("ParticleTemplateHandling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @particle_template_handling.setter
    def particle_template_handling(self, value: members.FieldEnum) -> None:
        """Set the ParticleTemplateHandling member."""
        self.set_member("ParticleTemplateHandling", value)

    @property
    def emission_rate_per_unit_length(self) -> primitives.Float | None:
        """The EmissionRatePerUnitLength field value."""
        member = self.get_member("EmissionRatePerUnitLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_rate_per_unit_length.setter
    def emission_rate_per_unit_length(self, value: primitives.Float) -> None:
        """Set the EmissionRatePerUnitLength field value."""
        member = self.get_member("EmissionRatePerUnitLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionRatePerUnitLength", fields.FieldNullableFloat(value=value)
            )

    @property
    def color_picker(self) -> str | None:
        """Target ID of the _colorPicker reference (targets ColorDialogInterface)."""
        member = self.get_member("_colorPicker")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_picker.setter
    def color_picker(self, target: str | ColorDialogInterface | None) -> None:
        """Set the _colorPicker reference by target ID or ColorDialogInterface instance."""
        target_id: str | None = target.id if isinstance(target, ColorDialogInterface) else target  # type: ignore[assignment]
        member = self.get_member("_colorPicker")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorPicker",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ColorDialogInterface'),
            )

    @property
    def picked_color(self) -> primitives.ColorX | None:
        """The _pickedColor field value."""
        member = self.get_member("_pickedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @picked_color.setter
    def picked_color(self, value: primitives.ColorX) -> None:
        """Set the _pickedColor field value."""
        member = self.get_member("_pickedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_pickedColor", fields.FieldColorX(value=value)
            )

    @property
    def hide_on_stroke(self) -> members.SyncList | None:
        """The _hideOnStroke member."""
        member = self.get_member("_hideOnStroke")
        if isinstance(member, members.SyncList):
            return member
        return None

    @hide_on_stroke.setter
    def hide_on_stroke(self, value: members.SyncList) -> None:
        """Set the _hideOnStroke member."""
        self.set_member("_hideOnStroke", value)

    @property
    def last_used_material(self) -> str | None:
        """Target ID of the _lastUsedMaterial reference (targets IAssetProvider[Material])."""
        member = self.get_member("_lastUsedMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_used_material.setter
    def last_used_material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the _lastUsedMaterial reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_lastUsedMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastUsedMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def last_created_material(self) -> str | None:
        """Target ID of the _lastCreatedMaterial reference (targets IAssetProvider[Material])."""
        member = self.get_member("_lastCreatedMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_created_material.setter
    def last_created_material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the _lastCreatedMaterial reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_lastCreatedMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastCreatedMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def pressure(self) -> primitives.Float | None:
        """The Pressure field value."""
        member = self.get_member("Pressure")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressure.setter
    def pressure(self, value: primitives.Float) -> None:
        """Set the Pressure field value."""
        member = self.get_member("Pressure")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pressure", fields.FieldFloat(value=value)
            )

    @property
    def position(self) -> primitives.Float3 | None:
        """The Position field value."""
        member = self.get_member("Position")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position.setter
    def position(self, value: primitives.Float3) -> None:
        """Set the Position field value."""
        member = self.get_member("Position")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Position", fields.FieldFloat3(value=value)
            )

    @property
    def rotation(self) -> primitives.FloatQ | None:
        """The Rotation field value."""
        member = self.get_member("Rotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation.setter
    def rotation(self, value: primitives.FloatQ) -> None:
        """Set the Rotation field value."""
        member = self.get_member("Rotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rotation", fields.FieldFloatQ(value=value)
            )

    @property
    def last_point_delta(self) -> primitives.Float3 | None:
        """The LastPointDelta field value."""
        member = self.get_member("LastPointDelta")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_point_delta.setter
    def last_point_delta(self, value: primitives.Float3) -> None:
        """Set the LastPointDelta field value."""
        member = self.get_member("LastPointDelta")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastPointDelta", fields.FieldFloat3(value=value)
            )

    @property
    def velocity(self) -> primitives.Float3 | None:
        """The Velocity field value."""
        member = self.get_member("Velocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @velocity.setter
    def velocity(self, value: primitives.Float3) -> None:
        """Set the Velocity field value."""
        member = self.get_member("Velocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Velocity", fields.FieldFloat3(value=value)
            )

    @property
    def raw_delta(self) -> primitives.Float3 | None:
        """The RawDelta field value."""
        member = self.get_member("RawDelta")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_delta.setter
    def raw_delta(self, value: primitives.Float3) -> None:
        """Set the RawDelta field value."""
        member = self.get_member("RawDelta")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RawDelta", fields.FieldFloat3(value=value)
            )

    @property
    def raw_velocity(self) -> primitives.Float3 | None:
        """The RawVelocity field value."""
        member = self.get_member("RawVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_velocity.setter
    def raw_velocity(self, value: primitives.Float3) -> None:
        """Set the RawVelocity field value."""
        member = self.get_member("RawVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RawVelocity", fields.FieldFloat3(value=value)
            )

    @property
    def raw_stroke_length(self) -> primitives.Float | None:
        """The RawStrokeLength field value."""
        member = self.get_member("RawStrokeLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_stroke_length.setter
    def raw_stroke_length(self, value: primitives.Float) -> None:
        """Set the RawStrokeLength field value."""
        member = self.get_member("RawStrokeLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RawStrokeLength", fields.FieldFloat(value=value)
            )

    @property
    def stroke_length(self) -> primitives.Float | None:
        """The StrokeLength field value."""
        member = self.get_member("StrokeLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stroke_length.setter
    def stroke_length(self, value: primitives.Float) -> None:
        """Set the StrokeLength field value."""
        member = self.get_member("StrokeLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrokeLength", fields.FieldFloat(value=value)
            )

    @property
    def normalized_stroke_length(self) -> primitives.Float | None:
        """The NormalizedStrokeLength field value."""
        member = self.get_member("NormalizedStrokeLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_stroke_length.setter
    def normalized_stroke_length(self, value: primitives.Float) -> None:
        """Set the NormalizedStrokeLength field value."""
        member = self.get_member("NormalizedStrokeLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedStrokeLength", fields.FieldFloat(value=value)
            )

    @property
    def stroke_fade_multiplier(self) -> primitives.Float | None:
        """The StrokeFadeMultiplier field value."""
        member = self.get_member("StrokeFadeMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stroke_fade_multiplier.setter
    def stroke_fade_multiplier(self, value: primitives.Float) -> None:
        """Set the StrokeFadeMultiplier field value."""
        member = self.get_member("StrokeFadeMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrokeFadeMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def stroke_group_index(self) -> primitives.Int | None:
        """The StrokeGroupIndex field value."""
        member = self.get_member("StrokeGroupIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stroke_group_index.setter
    def stroke_group_index(self, value: primitives.Int) -> None:
        """Set the StrokeGroupIndex field value."""
        member = self.get_member("StrokeGroupIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrokeGroupIndex", fields.FieldInt(value=value)
            )

    @property
    def stroke_group_active(self) -> primitives.Bool | None:
        """The StrokeGroupActive field value."""
        member = self.get_member("StrokeGroupActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stroke_group_active.setter
    def stroke_group_active(self, value: primitives.Bool) -> None:
        """Set the StrokeGroupActive field value."""
        member = self.get_member("StrokeGroupActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrokeGroupActive", fields.FieldBool(value=value)
            )

    @property
    def tip_anchor(self) -> str | None:
        """Target ID of the TipAnchor reference (targets Slot)."""
        member = self.get_member("TipAnchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tip_anchor.setter
    def tip_anchor(self, target: str | Slot | None) -> None:
        """Set the TipAnchor reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TipAnchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipAnchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def line_styles(self) -> members.SyncList | None:
        """The LineStyles member."""
        member = self.get_member("LineStyles")
        if isinstance(member, members.SyncList):
            return member
        return None

    @line_styles.setter
    def line_styles(self, value: members.SyncList) -> None:
        """Set the LineStyles member."""
        self.set_member("LineStyles", value)

    @property
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

    @property
    def use_relative_minimum_point_distance(self) -> primitives.Bool | None:
        """The UseRelativeMinimumPointDistance field value."""
        member = self.get_member("UseRelativeMinimumPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_relative_minimum_point_distance.setter
    def use_relative_minimum_point_distance(self, value: primitives.Bool) -> None:
        """Set the UseRelativeMinimumPointDistance field value."""
        member = self.get_member("UseRelativeMinimumPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseRelativeMinimumPointDistance", fields.FieldBool(value=value)
            )

    @property
    def relative_minimum_point_distance_ratio(self) -> primitives.Float | None:
        """The RelativeMinimumPointDistanceRatio field value."""
        member = self.get_member("RelativeMinimumPointDistanceRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @relative_minimum_point_distance_ratio.setter
    def relative_minimum_point_distance_ratio(self, value: primitives.Float) -> None:
        """Set the RelativeMinimumPointDistanceRatio field value."""
        member = self.get_member("RelativeMinimumPointDistanceRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RelativeMinimumPointDistanceRatio", fields.FieldFloat(value=value)
            )

    @property
    def pressure_affects_size(self) -> primitives.Bool | None:
        """The PressureAffectsSize field value."""
        member = self.get_member("PressureAffectsSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressure_affects_size.setter
    def pressure_affects_size(self, value: primitives.Bool) -> None:
        """Set the PressureAffectsSize field value."""
        member = self.get_member("PressureAffectsSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressureAffectsSize", fields.FieldBool(value=value)
            )

    @property
    def material_previews(self) -> members.SyncList | None:
        """The MaterialPreviews member."""
        member = self.get_member("MaterialPreviews")
        if isinstance(member, members.SyncList):
            return member
        return None

    @material_previews.setter
    def material_previews(self, value: members.SyncList) -> None:
        """Set the MaterialPreviews member."""
        self.set_member("MaterialPreviews", value)

    @property
    def preview_mesh(self) -> str | None:
        """Target ID of the _previewMesh reference (targets MultiLineMesh)."""
        member = self.get_member("_previewMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preview_mesh.setter
    def preview_mesh(self, target: str | MultiLineMesh | None) -> None:
        """Set the _previewMesh reference by target ID or MultiLineMesh instance."""
        target_id: str | None = target.id if isinstance(target, MultiLineMesh) else target  # type: ignore[assignment]
        member = self.get_member("_previewMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previewMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MultiLineMesh'),
            )

    @property
    def preview_mesh_offset(self) -> str | None:
        """Target ID of the _previewMeshOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_previewMeshOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preview_mesh_offset.setter
    def preview_mesh_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _previewMeshOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_previewMeshOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previewMeshOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def size_knob(self) -> str | None:
        """Target ID of the _sizeKnob reference (targets Slot)."""
        member = self.get_member("_sizeKnob")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_knob.setter
    def size_knob(self, target: str | Slot | None) -> None:
        """Set the _sizeKnob reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_sizeKnob")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sizeKnob",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

