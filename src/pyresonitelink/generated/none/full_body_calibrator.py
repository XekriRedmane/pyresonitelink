"""Generated component: FullBodyCalibrator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.grabbable import Grabbable
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.tracked_device_positioner import TrackedDevicePositioner
from pyresonitelink.generated._types.full_body_calibrator_dialog import FullBodyCalibratorDialog
from pyresonitelink.generated._types.vrik_avatar import VRIKAvatar
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.fresnel_material import FresnelMaterial
from pyresonitelink.generated._types.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.static_texture_2d import StaticTexture2D
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FullBodyCalibrator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FullBodyCalibrator.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FullBodyCalibrator"

    def __init__(self, target_user: str | User | None = None, use_symmetry_for_trackers: primitives.Bool | None = None, use_symmetry_for_avatar: primitives.Bool | None = None, show_body_overlay: primitives.Bool | None = None, show_avatar_overlay: primitives.Bool | None = None, height_compensation: primitives.Float | None = None, avatar_height_compensation: primitives.Float | None = None, calibrating_pose: primitives.Bool | None = None, space_offset: primitives.Float3 | None = None, grabbable: str | Grabbable | None = None, head_reference: str | Slot | None = None, left_hand_reference: str | Slot | None = None, right_hand_reference: str | Slot | None = None, hips_source: str | TrackedDevicePositioner | None = None, chest_source: str | TrackedDevicePositioner | None = None, left_foot_source: str | TrackedDevicePositioner | None = None, right_foot_source: str | TrackedDevicePositioner | None = None, left_elbow_source: str | TrackedDevicePositioner | None = None, right_elbow_source: str | TrackedDevicePositioner | None = None, left_knee_source: str | TrackedDevicePositioner | None = None, right_knee_source: str | TrackedDevicePositioner | None = None, dialog: str | FullBodyCalibratorDialog | None = None, left_hand_override: str | Slot | None = None, right_hand_override: str | Slot | None = None, target_custom_avatar: str | VRIKAvatar | None = None, avatar_hips_offset: str | Slot | None = None, avatar_left_foot_offset: str | Slot | None = None, avatar_right_foot_offset: str | Slot | None = None, avatar_left_knee_default_offset: str | Slot | None = None, avatar_right_knee_default_offset: str | Slot | None = None, avatar_hip_handle: str | Slot | None = None, avatar_left_foot_handle: str | Slot | None = None, avatar_right_foot_handle: str | Slot | None = None, avatar_left_knee_handle: str | Slot | None = None, avatar_right_knee_handle: str | Slot | None = None, avatar_left_knee_offset: str | IField[primitives.Float3] | None = None, avatar_right_knee_offset: str | IField[primitives.Float3] | None = None, ground: str | Slot | None = None, visualization_root: str | Slot | None = None, body_node_material: str | FresnelMaterial | None = None, calibration_reference_material: str | OverlayFresnelMaterial | None = None, left_hand_override_material: str | OverlayFresnelMaterial | None = None, right_hand_override_material: str | OverlayFresnelMaterial | None = None, left_hand_override_front_color: str | IField[primitives.ColorX] | None = None, left_hand_override_behind_color: str | IField[primitives.ColorX] | None = None, right_hand_override_front_color: str | IField[primitives.ColorX] | None = None, right_hand_override_behind_color: str | IField[primitives.ColorX] | None = None, pattern_tex: str | StaticTexture2D | None = None, title: str | TextRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_user: Initial value for TargetUser.
            use_symmetry_for_trackers: Initial value for UseSymmetryForTrackers.
            use_symmetry_for_avatar: Initial value for UseSymmetryForAvatar.
            show_body_overlay: Initial value for ShowBodyOverlay.
            show_avatar_overlay: Initial value for ShowAvatarOverlay.
            height_compensation: Initial value for HeightCompensation.
            avatar_height_compensation: Initial value for AvatarHeightCompensation.
            calibrating_pose: Initial value for _calibratingPose.
            space_offset: Initial value for _spaceOffset.
            grabbable: Initial value for _grabbable.
            head_reference: Initial value for _headReference.
            left_hand_reference: Initial value for _leftHandReference.
            right_hand_reference: Initial value for _rightHandReference.
            hips_source: Initial value for _hipsSource.
            chest_source: Initial value for _chestSource.
            left_foot_source: Initial value for _leftFootSource.
            right_foot_source: Initial value for _rightFootSource.
            left_elbow_source: Initial value for _leftElbowSource.
            right_elbow_source: Initial value for _rightElbowSource.
            left_knee_source: Initial value for _leftKneeSource.
            right_knee_source: Initial value for _rightKneeSource.
            dialog: Initial value for _dialog.
            left_hand_override: Initial value for _leftHandOverride.
            right_hand_override: Initial value for _rightHandOverride.
            target_custom_avatar: Initial value for _targetCustomAvatar.
            avatar_hips_offset: Initial value for _avatarHipsOffset.
            avatar_left_foot_offset: Initial value for _avatarLeftFootOffset.
            avatar_right_foot_offset: Initial value for _avatarRightFootOffset.
            avatar_left_knee_default_offset: Initial value for _avatarLeftKneeDefaultOffset.
            avatar_right_knee_default_offset: Initial value for _avatarRightKneeDefaultOffset.
            avatar_hip_handle: Initial value for _avatarHipHandle.
            avatar_left_foot_handle: Initial value for _avatarLeftFootHandle.
            avatar_right_foot_handle: Initial value for _avatarRightFootHandle.
            avatar_left_knee_handle: Initial value for _avatarLeftKneeHandle.
            avatar_right_knee_handle: Initial value for _avatarRightKneeHandle.
            avatar_left_knee_offset: Initial value for _avatarLeftKneeOffset.
            avatar_right_knee_offset: Initial value for _avatarRightKneeOffset.
            ground: Initial value for _ground.
            visualization_root: Initial value for _visualizationRoot.
            body_node_material: Initial value for _bodyNodeMaterial.
            calibration_reference_material: Initial value for _calibrationReferenceMaterial.
            left_hand_override_material: Initial value for _leftHandOverrideMaterial.
            right_hand_override_material: Initial value for _rightHandOverrideMaterial.
            left_hand_override_front_color: Initial value for _leftHandOverrideFrontColor.
            left_hand_override_behind_color: Initial value for _leftHandOverrideBehindColor.
            right_hand_override_front_color: Initial value for _rightHandOverrideFrontColor.
            right_hand_override_behind_color: Initial value for _rightHandOverrideBehindColor.
            pattern_tex: Initial value for _patternTex.
            title: Initial value for _title.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_user is not None:
            self.target_user = target_user
        if use_symmetry_for_trackers is not None:
            self.use_symmetry_for_trackers = use_symmetry_for_trackers
        if use_symmetry_for_avatar is not None:
            self.use_symmetry_for_avatar = use_symmetry_for_avatar
        if show_body_overlay is not None:
            self.show_body_overlay = show_body_overlay
        if show_avatar_overlay is not None:
            self.show_avatar_overlay = show_avatar_overlay
        if height_compensation is not None:
            self.height_compensation = height_compensation
        if avatar_height_compensation is not None:
            self.avatar_height_compensation = avatar_height_compensation
        if calibrating_pose is not None:
            self.calibrating_pose = calibrating_pose
        if space_offset is not None:
            self.space_offset = space_offset
        if grabbable is not None:
            self.grabbable = grabbable
        if head_reference is not None:
            self.head_reference = head_reference
        if left_hand_reference is not None:
            self.left_hand_reference = left_hand_reference
        if right_hand_reference is not None:
            self.right_hand_reference = right_hand_reference
        if hips_source is not None:
            self.hips_source = hips_source
        if chest_source is not None:
            self.chest_source = chest_source
        if left_foot_source is not None:
            self.left_foot_source = left_foot_source
        if right_foot_source is not None:
            self.right_foot_source = right_foot_source
        if left_elbow_source is not None:
            self.left_elbow_source = left_elbow_source
        if right_elbow_source is not None:
            self.right_elbow_source = right_elbow_source
        if left_knee_source is not None:
            self.left_knee_source = left_knee_source
        if right_knee_source is not None:
            self.right_knee_source = right_knee_source
        if dialog is not None:
            self.dialog = dialog
        if left_hand_override is not None:
            self.left_hand_override = left_hand_override
        if right_hand_override is not None:
            self.right_hand_override = right_hand_override
        if target_custom_avatar is not None:
            self.target_custom_avatar = target_custom_avatar
        if avatar_hips_offset is not None:
            self.avatar_hips_offset = avatar_hips_offset
        if avatar_left_foot_offset is not None:
            self.avatar_left_foot_offset = avatar_left_foot_offset
        if avatar_right_foot_offset is not None:
            self.avatar_right_foot_offset = avatar_right_foot_offset
        if avatar_left_knee_default_offset is not None:
            self.avatar_left_knee_default_offset = avatar_left_knee_default_offset
        if avatar_right_knee_default_offset is not None:
            self.avatar_right_knee_default_offset = avatar_right_knee_default_offset
        if avatar_hip_handle is not None:
            self.avatar_hip_handle = avatar_hip_handle
        if avatar_left_foot_handle is not None:
            self.avatar_left_foot_handle = avatar_left_foot_handle
        if avatar_right_foot_handle is not None:
            self.avatar_right_foot_handle = avatar_right_foot_handle
        if avatar_left_knee_handle is not None:
            self.avatar_left_knee_handle = avatar_left_knee_handle
        if avatar_right_knee_handle is not None:
            self.avatar_right_knee_handle = avatar_right_knee_handle
        if avatar_left_knee_offset is not None:
            self.avatar_left_knee_offset = avatar_left_knee_offset
        if avatar_right_knee_offset is not None:
            self.avatar_right_knee_offset = avatar_right_knee_offset
        if ground is not None:
            self.ground = ground
        if visualization_root is not None:
            self.visualization_root = visualization_root
        if body_node_material is not None:
            self.body_node_material = body_node_material
        if calibration_reference_material is not None:
            self.calibration_reference_material = calibration_reference_material
        if left_hand_override_material is not None:
            self.left_hand_override_material = left_hand_override_material
        if right_hand_override_material is not None:
            self.right_hand_override_material = right_hand_override_material
        if left_hand_override_front_color is not None:
            self.left_hand_override_front_color = left_hand_override_front_color
        if left_hand_override_behind_color is not None:
            self.left_hand_override_behind_color = left_hand_override_behind_color
        if right_hand_override_front_color is not None:
            self.right_hand_override_front_color = right_hand_override_front_color
        if right_hand_override_behind_color is not None:
            self.right_hand_override_behind_color = right_hand_override_behind_color
        if pattern_tex is not None:
            self.pattern_tex = pattern_tex
        if title is not None:
            self.title = title

    @property
    def target_user(self) -> str | None:
        """Target ID of the TargetUser reference (targets User)."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_user.setter
    def target_user(self, target: str | User | None) -> None:
        """Set the TargetUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def use_symmetry_for_trackers(self) -> primitives.Bool | None:
        """The UseSymmetryForTrackers field value."""
        member = self.get_member("UseSymmetryForTrackers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_symmetry_for_trackers.setter
    def use_symmetry_for_trackers(self, value: primitives.Bool) -> None:
        """Set the UseSymmetryForTrackers field value."""
        member = self.get_member("UseSymmetryForTrackers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSymmetryForTrackers", fields.FieldBool(value=value)
            )

    @property
    def use_symmetry_for_avatar(self) -> primitives.Bool | None:
        """The UseSymmetryForAvatar field value."""
        member = self.get_member("UseSymmetryForAvatar")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_symmetry_for_avatar.setter
    def use_symmetry_for_avatar(self, value: primitives.Bool) -> None:
        """Set the UseSymmetryForAvatar field value."""
        member = self.get_member("UseSymmetryForAvatar")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSymmetryForAvatar", fields.FieldBool(value=value)
            )

    @property
    def show_body_overlay(self) -> primitives.Bool | None:
        """The ShowBodyOverlay field value."""
        member = self.get_member("ShowBodyOverlay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_body_overlay.setter
    def show_body_overlay(self, value: primitives.Bool) -> None:
        """Set the ShowBodyOverlay field value."""
        member = self.get_member("ShowBodyOverlay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowBodyOverlay", fields.FieldBool(value=value)
            )

    @property
    def show_avatar_overlay(self) -> primitives.Bool | None:
        """The ShowAvatarOverlay field value."""
        member = self.get_member("ShowAvatarOverlay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_avatar_overlay.setter
    def show_avatar_overlay(self, value: primitives.Bool) -> None:
        """Set the ShowAvatarOverlay field value."""
        member = self.get_member("ShowAvatarOverlay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowAvatarOverlay", fields.FieldBool(value=value)
            )

    @property
    def height_compensation(self) -> primitives.Float | None:
        """The HeightCompensation field value."""
        member = self.get_member("HeightCompensation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_compensation.setter
    def height_compensation(self, value: primitives.Float) -> None:
        """Set the HeightCompensation field value."""
        member = self.get_member("HeightCompensation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightCompensation", fields.FieldFloat(value=value)
            )

    @property
    def avatar_height_compensation(self) -> primitives.Float | None:
        """The AvatarHeightCompensation field value."""
        member = self.get_member("AvatarHeightCompensation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @avatar_height_compensation.setter
    def avatar_height_compensation(self, value: primitives.Float) -> None:
        """Set the AvatarHeightCompensation field value."""
        member = self.get_member("AvatarHeightCompensation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AvatarHeightCompensation", fields.FieldFloat(value=value)
            )

    @property
    def calibrating_pose(self) -> primitives.Bool | None:
        """The _calibratingPose field value."""
        member = self.get_member("_calibratingPose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @calibrating_pose.setter
    def calibrating_pose(self, value: primitives.Bool) -> None:
        """Set the _calibratingPose field value."""
        member = self.get_member("_calibratingPose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_calibratingPose", fields.FieldBool(value=value)
            )

    @property
    def space_offset(self) -> primitives.Float3 | None:
        """The _spaceOffset field value."""
        member = self.get_member("_spaceOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @space_offset.setter
    def space_offset(self, value: primitives.Float3) -> None:
        """Set the _spaceOffset field value."""
        member = self.get_member("_spaceOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_spaceOffset", fields.FieldFloat3(value=value)
            )

    @property
    def grabbable(self) -> str | None:
        """Target ID of the _grabbable reference (targets Grabbable)."""
        member = self.get_member("_grabbable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabbable.setter
    def grabbable(self, target: str | Grabbable | None) -> None:
        """Set the _grabbable reference by target ID or Grabbable instance."""
        target_id: str | None = target.id if isinstance(target, Grabbable) else target  # type: ignore[assignment]
        member = self.get_member("_grabbable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabbable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabbable'),
            )

    @property
    def head_reference(self) -> str | None:
        """Target ID of the _headReference reference (targets Slot)."""
        member = self.get_member("_headReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @head_reference.setter
    def head_reference(self, target: str | Slot | None) -> None:
        """Set the _headReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_headReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_hand_reference(self) -> str | None:
        """Target ID of the _leftHandReference reference (targets Slot)."""
        member = self.get_member("_leftHandReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_reference.setter
    def left_hand_reference(self, target: str | Slot | None) -> None:
        """Set the _leftHandReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_hand_reference(self) -> str | None:
        """Target ID of the _rightHandReference reference (targets Slot)."""
        member = self.get_member("_rightHandReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_reference.setter
    def right_hand_reference(self, target: str | Slot | None) -> None:
        """Set the _rightHandReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def hips_source(self) -> str | None:
        """Target ID of the _hipsSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_hipsSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hips_source.setter
    def hips_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _hipsSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_hipsSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hipsSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def chest_source(self) -> str | None:
        """Target ID of the _chestSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_chestSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chest_source.setter
    def chest_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _chestSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_chestSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_chestSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def left_foot_source(self) -> str | None:
        """Target ID of the _leftFootSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_leftFootSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_source.setter
    def left_foot_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _leftFootSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def right_foot_source(self) -> str | None:
        """Target ID of the _rightFootSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_rightFootSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_source.setter
    def right_foot_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _rightFootSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def left_elbow_source(self) -> str | None:
        """Target ID of the _leftElbowSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_leftElbowSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_elbow_source.setter
    def left_elbow_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _leftElbowSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_leftElbowSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftElbowSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def right_elbow_source(self) -> str | None:
        """Target ID of the _rightElbowSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_rightElbowSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_elbow_source.setter
    def right_elbow_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _rightElbowSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_rightElbowSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightElbowSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def left_knee_source(self) -> str | None:
        """Target ID of the _leftKneeSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_leftKneeSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_knee_source.setter
    def left_knee_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _leftKneeSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_leftKneeSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftKneeSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def right_knee_source(self) -> str | None:
        """Target ID of the _rightKneeSource reference (targets TrackedDevicePositioner)."""
        member = self.get_member("_rightKneeSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_knee_source.setter
    def right_knee_source(self, target: str | TrackedDevicePositioner | None) -> None:
        """Set the _rightKneeSource reference by target ID or TrackedDevicePositioner instance."""
        target_id: str | None = target.id if isinstance(target, TrackedDevicePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_rightKneeSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightKneeSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrackedDevicePositioner'),
            )

    @property
    def dialog(self) -> str | None:
        """Target ID of the _dialog reference (targets FullBodyCalibratorDialog)."""
        member = self.get_member("_dialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dialog.setter
    def dialog(self, target: str | FullBodyCalibratorDialog | None) -> None:
        """Set the _dialog reference by target ID or FullBodyCalibratorDialog instance."""
        target_id: str | None = target.id if isinstance(target, FullBodyCalibratorDialog) else target  # type: ignore[assignment]
        member = self.get_member("_dialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_dialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FullBodyCalibratorDialog'),
            )

    @property
    def platform_body(self) -> members.SyncObject | None:
        """The _platformBody member."""
        member = self.get_member("_platformBody")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @platform_body.setter
    def platform_body(self, value: members.SyncObject) -> None:
        """Set the _platformBody member."""
        self.set_member("_platformBody", value)

    @property
    def user_body(self) -> members.SyncObject | None:
        """The _userBody member."""
        member = self.get_member("_userBody")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user_body.setter
    def user_body(self, value: members.SyncObject) -> None:
        """Set the _userBody member."""
        self.set_member("_userBody", value)

    @property
    def custom_avatar(self) -> members.SyncObject | None:
        """The _customAvatar member."""
        member = self.get_member("_customAvatar")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @custom_avatar.setter
    def custom_avatar(self, value: members.SyncObject) -> None:
        """Set the _customAvatar member."""
        self.set_member("_customAvatar", value)

    @property
    def left_hand_override(self) -> str | None:
        """Target ID of the _leftHandOverride reference (targets Slot)."""
        member = self.get_member("_leftHandOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_override.setter
    def left_hand_override(self, target: str | Slot | None) -> None:
        """Set the _leftHandOverride reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_hand_override(self) -> str | None:
        """Target ID of the _rightHandOverride reference (targets Slot)."""
        member = self.get_member("_rightHandOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_override.setter
    def right_hand_override(self, target: str | Slot | None) -> None:
        """Set the _rightHandOverride reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target_custom_avatar(self) -> str | None:
        """Target ID of the _targetCustomAvatar reference (targets VRIKAvatar)."""
        member = self.get_member("_targetCustomAvatar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_custom_avatar.setter
    def target_custom_avatar(self, target: str | VRIKAvatar | None) -> None:
        """Set the _targetCustomAvatar reference by target ID or VRIKAvatar instance."""
        target_id: str | None = target.id if isinstance(target, VRIKAvatar) else target  # type: ignore[assignment]
        member = self.get_member("_targetCustomAvatar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetCustomAvatar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FinalIK.VRIKAvatar'),
            )

    @property
    def avatar_hips_offset(self) -> str | None:
        """Target ID of the _avatarHipsOffset reference (targets Slot)."""
        member = self.get_member("_avatarHipsOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_hips_offset.setter
    def avatar_hips_offset(self, target: str | Slot | None) -> None:
        """Set the _avatarHipsOffset reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarHipsOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarHipsOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_left_foot_offset(self) -> str | None:
        """Target ID of the _avatarLeftFootOffset reference (targets Slot)."""
        member = self.get_member("_avatarLeftFootOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_left_foot_offset.setter
    def avatar_left_foot_offset(self, target: str | Slot | None) -> None:
        """Set the _avatarLeftFootOffset reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarLeftFootOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarLeftFootOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_right_foot_offset(self) -> str | None:
        """Target ID of the _avatarRightFootOffset reference (targets Slot)."""
        member = self.get_member("_avatarRightFootOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_right_foot_offset.setter
    def avatar_right_foot_offset(self, target: str | Slot | None) -> None:
        """Set the _avatarRightFootOffset reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarRightFootOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarRightFootOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_left_knee_default_offset(self) -> str | None:
        """Target ID of the _avatarLeftKneeDefaultOffset reference (targets Slot)."""
        member = self.get_member("_avatarLeftKneeDefaultOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_left_knee_default_offset.setter
    def avatar_left_knee_default_offset(self, target: str | Slot | None) -> None:
        """Set the _avatarLeftKneeDefaultOffset reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarLeftKneeDefaultOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarLeftKneeDefaultOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_right_knee_default_offset(self) -> str | None:
        """Target ID of the _avatarRightKneeDefaultOffset reference (targets Slot)."""
        member = self.get_member("_avatarRightKneeDefaultOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_right_knee_default_offset.setter
    def avatar_right_knee_default_offset(self, target: str | Slot | None) -> None:
        """Set the _avatarRightKneeDefaultOffset reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarRightKneeDefaultOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarRightKneeDefaultOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_hip_handle(self) -> str | None:
        """Target ID of the _avatarHipHandle reference (targets Slot)."""
        member = self.get_member("_avatarHipHandle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_hip_handle.setter
    def avatar_hip_handle(self, target: str | Slot | None) -> None:
        """Set the _avatarHipHandle reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarHipHandle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarHipHandle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_left_foot_handle(self) -> str | None:
        """Target ID of the _avatarLeftFootHandle reference (targets Slot)."""
        member = self.get_member("_avatarLeftFootHandle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_left_foot_handle.setter
    def avatar_left_foot_handle(self, target: str | Slot | None) -> None:
        """Set the _avatarLeftFootHandle reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarLeftFootHandle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarLeftFootHandle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_right_foot_handle(self) -> str | None:
        """Target ID of the _avatarRightFootHandle reference (targets Slot)."""
        member = self.get_member("_avatarRightFootHandle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_right_foot_handle.setter
    def avatar_right_foot_handle(self, target: str | Slot | None) -> None:
        """Set the _avatarRightFootHandle reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarRightFootHandle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarRightFootHandle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_left_knee_handle(self) -> str | None:
        """Target ID of the _avatarLeftKneeHandle reference (targets Slot)."""
        member = self.get_member("_avatarLeftKneeHandle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_left_knee_handle.setter
    def avatar_left_knee_handle(self, target: str | Slot | None) -> None:
        """Set the _avatarLeftKneeHandle reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarLeftKneeHandle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarLeftKneeHandle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_right_knee_handle(self) -> str | None:
        """Target ID of the _avatarRightKneeHandle reference (targets Slot)."""
        member = self.get_member("_avatarRightKneeHandle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_right_knee_handle.setter
    def avatar_right_knee_handle(self, target: str | Slot | None) -> None:
        """Set the _avatarRightKneeHandle reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_avatarRightKneeHandle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarRightKneeHandle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def avatar_left_knee_offset(self) -> str | None:
        """Target ID of the _avatarLeftKneeOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_avatarLeftKneeOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_left_knee_offset.setter
    def avatar_left_knee_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _avatarLeftKneeOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_avatarLeftKneeOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarLeftKneeOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def avatar_right_knee_offset(self) -> str | None:
        """Target ID of the _avatarRightKneeOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_avatarRightKneeOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_right_knee_offset.setter
    def avatar_right_knee_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _avatarRightKneeOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_avatarRightKneeOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarRightKneeOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def platform_body_material_sets(self) -> members.SyncList | None:
        """The _platformBodyMaterialSets member."""
        member = self.get_member("_platformBodyMaterialSets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @platform_body_material_sets.setter
    def platform_body_material_sets(self, value: members.SyncList) -> None:
        """Set the _platformBodyMaterialSets member."""
        self.set_member("_platformBodyMaterialSets", value)

    @property
    def ground(self) -> str | None:
        """Target ID of the _ground reference (targets Slot)."""
        member = self.get_member("_ground")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ground.setter
    def ground(self, target: str | Slot | None) -> None:
        """Set the _ground reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_ground")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_ground",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def trackers(self) -> members.SyncList | None:
        """The _trackers member."""
        member = self.get_member("_trackers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @trackers.setter
    def trackers(self, value: members.SyncList) -> None:
        """Set the _trackers member."""
        self.set_member("_trackers", value)

    @property
    def visualization_root(self) -> str | None:
        """Target ID of the _visualizationRoot reference (targets Slot)."""
        member = self.get_member("_visualizationRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visualization_root.setter
    def visualization_root(self, target: str | Slot | None) -> None:
        """Set the _visualizationRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visualizationRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualizationRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def body_node_material(self) -> str | None:
        """Target ID of the _bodyNodeMaterial reference (targets FresnelMaterial)."""
        member = self.get_member("_bodyNodeMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @body_node_material.setter
    def body_node_material(self, target: str | FresnelMaterial | None) -> None:
        """Set the _bodyNodeMaterial reference by target ID or FresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, FresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_bodyNodeMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_bodyNodeMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FresnelMaterial'),
            )

    @property
    def calibration_reference_material(self) -> str | None:
        """Target ID of the _calibrationReferenceMaterial reference (targets OverlayFresnelMaterial)."""
        member = self.get_member("_calibrationReferenceMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @calibration_reference_material.setter
    def calibration_reference_material(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _calibrationReferenceMaterial reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_calibrationReferenceMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_calibrationReferenceMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def left_hand_override_material(self) -> str | None:
        """Target ID of the _leftHandOverrideMaterial reference (targets OverlayFresnelMaterial)."""
        member = self.get_member("_leftHandOverrideMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_override_material.setter
    def left_hand_override_material(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _leftHandOverrideMaterial reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandOverrideMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandOverrideMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def right_hand_override_material(self) -> str | None:
        """Target ID of the _rightHandOverrideMaterial reference (targets OverlayFresnelMaterial)."""
        member = self.get_member("_rightHandOverrideMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_override_material.setter
    def right_hand_override_material(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _rightHandOverrideMaterial reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandOverrideMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandOverrideMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def left_hand_override_front_color(self) -> str | None:
        """Target ID of the _leftHandOverrideFrontColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_leftHandOverrideFrontColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_override_front_color.setter
    def left_hand_override_front_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _leftHandOverrideFrontColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandOverrideFrontColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandOverrideFrontColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def left_hand_override_behind_color(self) -> str | None:
        """Target ID of the _leftHandOverrideBehindColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_leftHandOverrideBehindColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_override_behind_color.setter
    def left_hand_override_behind_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _leftHandOverrideBehindColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandOverrideBehindColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandOverrideBehindColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def right_hand_override_front_color(self) -> str | None:
        """Target ID of the _rightHandOverrideFrontColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_rightHandOverrideFrontColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_override_front_color.setter
    def right_hand_override_front_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _rightHandOverrideFrontColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandOverrideFrontColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandOverrideFrontColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def right_hand_override_behind_color(self) -> str | None:
        """Target ID of the _rightHandOverrideBehindColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_rightHandOverrideBehindColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_override_behind_color.setter
    def right_hand_override_behind_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _rightHandOverrideBehindColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandOverrideBehindColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandOverrideBehindColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def pattern_tex(self) -> str | None:
        """Target ID of the _patternTex reference (targets StaticTexture2D)."""
        member = self.get_member("_patternTex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pattern_tex.setter
    def pattern_tex(self, target: str | StaticTexture2D | None) -> None:
        """Set the _patternTex reference by target ID or StaticTexture2D instance."""
        target_id: str | None = target.id if isinstance(target, StaticTexture2D) else target  # type: ignore[assignment]
        member = self.get_member("_patternTex")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_patternTex",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticTexture2D'),
            )

    @property
    def title(self) -> str | None:
        """Target ID of the _title reference (targets TextRenderer)."""
        member = self.get_member("_title")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title.setter
    def title(self, target: str | TextRenderer | None) -> None:
        """Set the _title reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_title")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_title",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

