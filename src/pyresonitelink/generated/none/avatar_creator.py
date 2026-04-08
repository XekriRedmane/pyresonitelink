"""Generated component: AvatarCreator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarCreator(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AvatarCreator.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarCreator"

    def __init__(self, headset_point: str | Slot | None = None, left_point: str | Slot | None = None, right_point: str | Slot | None = None, left_foot_point: str | Slot | None = None, right_foot_point: str | Slot | None = None, pelvis_point: str | Slot | None = None, headset_reference: str | Slot | None = None, pelvis_reference: str | Slot | None = None, left_reference: str | Slot | None = None, right_reference: str | Slot | None = None, left_foot_reference: str | Slot | None = None, right_foot_reference: str | Slot | None = None, initialized: bool | None = None, show_anchors: bool | None = None, use_symmetry: bool | None = None, setup_volume_meter: bool | None = None, setup_protection: bool | None = None, setup_eyes: bool | None = None, setup_face_tracking: bool | None = None, calibrate_feet: bool | None = None, calibrate_pelvis: bool | None = None, can_protect: bool | None = None, symmetry_setup: bool | None = None, scale: np.float32 | None = None, protect_avatar_enabled: str | IField[bool] | None = None, create_enabled: str | IField[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            headset_point: Initial value for _headsetPoint.
            left_point: Initial value for _leftPoint.
            right_point: Initial value for _rightPoint.
            left_foot_point: Initial value for _leftFootPoint.
            right_foot_point: Initial value for _rightFootPoint.
            pelvis_point: Initial value for _pelvisPoint.
            headset_reference: Initial value for _headsetReference.
            pelvis_reference: Initial value for _pelvisReference.
            left_reference: Initial value for _leftReference.
            right_reference: Initial value for _rightReference.
            left_foot_reference: Initial value for _leftFootReference.
            right_foot_reference: Initial value for _rightFootReference.
            initialized: Initial value for _initialized.
            show_anchors: Initial value for _showAnchors.
            use_symmetry: Initial value for _useSymmetry.
            setup_volume_meter: Initial value for _setupVolumeMeter.
            setup_protection: Initial value for _setupProtection.
            setup_eyes: Initial value for _setupEyes.
            setup_face_tracking: Initial value for _setupFaceTracking.
            calibrate_feet: Initial value for _calibrateFeet.
            calibrate_pelvis: Initial value for _calibratePelvis.
            can_protect: Initial value for _canProtect.
            symmetry_setup: Initial value for _symmetrySetup.
            scale: Initial value for _scale.
            protect_avatar_enabled: Initial value for _protectAvatarEnabled.
            create_enabled: Initial value for _createEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if headset_point is not None:
            self.headset_point = headset_point
        if left_point is not None:
            self.left_point = left_point
        if right_point is not None:
            self.right_point = right_point
        if left_foot_point is not None:
            self.left_foot_point = left_foot_point
        if right_foot_point is not None:
            self.right_foot_point = right_foot_point
        if pelvis_point is not None:
            self.pelvis_point = pelvis_point
        if headset_reference is not None:
            self.headset_reference = headset_reference
        if pelvis_reference is not None:
            self.pelvis_reference = pelvis_reference
        if left_reference is not None:
            self.left_reference = left_reference
        if right_reference is not None:
            self.right_reference = right_reference
        if left_foot_reference is not None:
            self.left_foot_reference = left_foot_reference
        if right_foot_reference is not None:
            self.right_foot_reference = right_foot_reference
        if initialized is not None:
            self.initialized = initialized
        if show_anchors is not None:
            self.show_anchors = show_anchors
        if use_symmetry is not None:
            self.use_symmetry = use_symmetry
        if setup_volume_meter is not None:
            self.setup_volume_meter = setup_volume_meter
        if setup_protection is not None:
            self.setup_protection = setup_protection
        if setup_eyes is not None:
            self.setup_eyes = setup_eyes
        if setup_face_tracking is not None:
            self.setup_face_tracking = setup_face_tracking
        if calibrate_feet is not None:
            self.calibrate_feet = calibrate_feet
        if calibrate_pelvis is not None:
            self.calibrate_pelvis = calibrate_pelvis
        if can_protect is not None:
            self.can_protect = can_protect
        if symmetry_setup is not None:
            self.symmetry_setup = symmetry_setup
        if scale is not None:
            self.scale = scale
        if protect_avatar_enabled is not None:
            self.protect_avatar_enabled = protect_avatar_enabled
        if create_enabled is not None:
            self.create_enabled = create_enabled

    @property
    def headset_point(self) -> str | None:
        """Target ID of the _headsetPoint reference (targets Slot)."""
        member = self.get_member("_headsetPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @headset_point.setter
    def headset_point(self, target: str | Slot | None) -> None:
        """Set the _headsetPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_headsetPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headsetPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_point(self) -> str | None:
        """Target ID of the _leftPoint reference (targets Slot)."""
        member = self.get_member("_leftPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_point.setter
    def left_point(self, target: str | Slot | None) -> None:
        """Set the _leftPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_point(self) -> str | None:
        """Target ID of the _rightPoint reference (targets Slot)."""
        member = self.get_member("_rightPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_point.setter
    def right_point(self, target: str | Slot | None) -> None:
        """Set the _rightPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_foot_point(self) -> str | None:
        """Target ID of the _leftFootPoint reference (targets Slot)."""
        member = self.get_member("_leftFootPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_point.setter
    def left_foot_point(self, target: str | Slot | None) -> None:
        """Set the _leftFootPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_foot_point(self) -> str | None:
        """Target ID of the _rightFootPoint reference (targets Slot)."""
        member = self.get_member("_rightFootPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_point.setter
    def right_foot_point(self, target: str | Slot | None) -> None:
        """Set the _rightFootPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def pelvis_point(self) -> str | None:
        """Target ID of the _pelvisPoint reference (targets Slot)."""
        member = self.get_member("_pelvisPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_point.setter
    def pelvis_point(self, target: str | Slot | None) -> None:
        """Set the _pelvisPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def headset_reference(self) -> str | None:
        """Target ID of the _headsetReference reference (targets Slot)."""
        member = self.get_member("_headsetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @headset_reference.setter
    def headset_reference(self, target: str | Slot | None) -> None:
        """Set the _headsetReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_headsetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headsetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def pelvis_reference(self) -> str | None:
        """Target ID of the _pelvisReference reference (targets Slot)."""
        member = self.get_member("_pelvisReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_reference.setter
    def pelvis_reference(self, target: str | Slot | None) -> None:
        """Set the _pelvisReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_reference(self) -> str | None:
        """Target ID of the _leftReference reference (targets Slot)."""
        member = self.get_member("_leftReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_reference.setter
    def left_reference(self, target: str | Slot | None) -> None:
        """Set the _leftReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_reference(self) -> str | None:
        """Target ID of the _rightReference reference (targets Slot)."""
        member = self.get_member("_rightReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_reference.setter
    def right_reference(self, target: str | Slot | None) -> None:
        """Set the _rightReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_foot_reference(self) -> str | None:
        """Target ID of the _leftFootReference reference (targets Slot)."""
        member = self.get_member("_leftFootReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_reference.setter
    def left_foot_reference(self, target: str | Slot | None) -> None:
        """Set the _leftFootReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_foot_reference(self) -> str | None:
        """Target ID of the _rightFootReference reference (targets Slot)."""
        member = self.get_member("_rightFootReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_reference.setter
    def right_foot_reference(self, target: str | Slot | None) -> None:
        """Set the _rightFootReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def initialized(self) -> bool | None:
        """The _initialized field value."""
        member = self.get_member("_initialized")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initialized.setter
    def initialized(self, value: bool) -> None:
        """Set the _initialized field value."""
        member = self.get_member("_initialized")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_initialized", fields.FieldBool(value=value)
            )

    @property
    def show_anchors(self) -> bool | None:
        """The _showAnchors field value."""
        member = self.get_member("_showAnchors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_anchors.setter
    def show_anchors(self, value: bool) -> None:
        """Set the _showAnchors field value."""
        member = self.get_member("_showAnchors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_showAnchors", fields.FieldBool(value=value)
            )

    @property
    def use_symmetry(self) -> bool | None:
        """The _useSymmetry field value."""
        member = self.get_member("_useSymmetry")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_symmetry.setter
    def use_symmetry(self, value: bool) -> None:
        """Set the _useSymmetry field value."""
        member = self.get_member("_useSymmetry")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_useSymmetry", fields.FieldBool(value=value)
            )

    @property
    def setup_volume_meter(self) -> bool | None:
        """The _setupVolumeMeter field value."""
        member = self.get_member("_setupVolumeMeter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_volume_meter.setter
    def setup_volume_meter(self, value: bool) -> None:
        """Set the _setupVolumeMeter field value."""
        member = self.get_member("_setupVolumeMeter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_setupVolumeMeter", fields.FieldBool(value=value)
            )

    @property
    def setup_protection(self) -> bool | None:
        """The _setupProtection field value."""
        member = self.get_member("_setupProtection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_protection.setter
    def setup_protection(self, value: bool) -> None:
        """Set the _setupProtection field value."""
        member = self.get_member("_setupProtection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_setupProtection", fields.FieldBool(value=value)
            )

    @property
    def setup_eyes(self) -> bool | None:
        """The _setupEyes field value."""
        member = self.get_member("_setupEyes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_eyes.setter
    def setup_eyes(self, value: bool) -> None:
        """Set the _setupEyes field value."""
        member = self.get_member("_setupEyes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_setupEyes", fields.FieldBool(value=value)
            )

    @property
    def setup_face_tracking(self) -> bool | None:
        """The _setupFaceTracking field value."""
        member = self.get_member("_setupFaceTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_face_tracking.setter
    def setup_face_tracking(self, value: bool) -> None:
        """Set the _setupFaceTracking field value."""
        member = self.get_member("_setupFaceTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_setupFaceTracking", fields.FieldBool(value=value)
            )

    @property
    def calibrate_feet(self) -> bool | None:
        """The _calibrateFeet field value."""
        member = self.get_member("_calibrateFeet")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @calibrate_feet.setter
    def calibrate_feet(self, value: bool) -> None:
        """Set the _calibrateFeet field value."""
        member = self.get_member("_calibrateFeet")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_calibrateFeet", fields.FieldBool(value=value)
            )

    @property
    def calibrate_pelvis(self) -> bool | None:
        """The _calibratePelvis field value."""
        member = self.get_member("_calibratePelvis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @calibrate_pelvis.setter
    def calibrate_pelvis(self, value: bool) -> None:
        """Set the _calibratePelvis field value."""
        member = self.get_member("_calibratePelvis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_calibratePelvis", fields.FieldBool(value=value)
            )

    @property
    def can_protect(self) -> bool | None:
        """The _canProtect field value."""
        member = self.get_member("_canProtect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @can_protect.setter
    def can_protect(self, value: bool) -> None:
        """Set the _canProtect field value."""
        member = self.get_member("_canProtect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_canProtect", fields.FieldBool(value=value)
            )

    @property
    def symmetry_setup(self) -> bool | None:
        """The _symmetrySetup field value."""
        member = self.get_member("_symmetrySetup")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @symmetry_setup.setter
    def symmetry_setup(self, value: bool) -> None:
        """Set the _symmetrySetup field value."""
        member = self.get_member("_symmetrySetup")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_symmetrySetup", fields.FieldBool(value=value)
            )

    @property
    def anchors(self) -> members.SyncList | None:
        """The _anchors member."""
        member = self.get_member("_anchors")
        if isinstance(member, members.SyncList):
            return member
        return None

    @anchors.setter
    def anchors(self, value: members.SyncList) -> None:
        """Set the _anchors member."""
        self.set_member("_anchors", value)

    @property
    def scale(self) -> np.float32 | None:
        """The _scale field value."""
        member = self.get_member("_scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: np.float32) -> None:
        """Set the _scale field value."""
        member = self.get_member("_scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_scale", fields.FieldFloat(value=value)
            )

    @property
    def protect_avatar_enabled(self) -> str | None:
        """Target ID of the _protectAvatarEnabled reference (targets IField[bool])."""
        member = self.get_member("_protectAvatarEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @protect_avatar_enabled.setter
    def protect_avatar_enabled(self, target: str | IField[bool] | None) -> None:
        """Set the _protectAvatarEnabled reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_protectAvatarEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_protectAvatarEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def create_enabled(self) -> str | None:
        """Target ID of the _createEnabled reference (targets IField[bool])."""
        member = self.get_member("_createEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @create_enabled.setter
    def create_enabled(self, target: str | IField[bool] | None) -> None:
        """Set the _createEnabled reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_createEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_createEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    async def create_biped_avatar(self, resolink: protocols.ResoniteLinkClient, biped: str, head_reference: str, left_hand_reference: str, right_hand_reference: str, left_foot_reference: str, right_foot_reference: str, hips_reference: str, setup_eyes: bool, setup_protection: bool, setup_volume_meter: bool, setup_face_tracking: bool, debug: bool = False) -> dict:
        """Call the CreateBipedAvatar sync method.

        Args:
            resolink: Connected ResoniteLink client.
            biped: The biped parameter.
            head_reference: The headReference parameter.
            left_hand_reference: The leftHandReference parameter.
            right_hand_reference: The rightHandReference parameter.
            left_foot_reference: The leftFootReference parameter.
            right_foot_reference: The rightFootReference parameter.
            hips_reference: The hipsReference parameter.
            setup_eyes: The setupEyes parameter.
            setup_protection: The setupProtection parameter.
            setup_volume_meter: The setupVolumeMeter parameter.
            setup_face_tracking: The setupFaceTracking parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "CreateBipedAvatar", {"biped": biped, "headReference": head_reference, "leftHandReference": left_hand_reference, "rightHandReference": right_hand_reference, "leftFootReference": left_foot_reference, "rightFootReference": right_foot_reference, "hipsReference": hips_reference, "setupEyes": setup_eyes, "setupProtection": setup_protection, "setupVolumeMeter": setup_volume_meter, "setupFaceTracking": setup_face_tracking}, debug,
        )

