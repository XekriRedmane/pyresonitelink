"""Generated component: Joint."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Joint(GeneratedComponent, IGrabbable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Joint.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Joint"

    def __init__(self, edit_mode_only: bool | None = None, allow_steal: bool | None = None, drop_on_disable: bool | None = None, dont_drive: bool | None = None, allow_only_physical_grab: bool | None = None, grabber: str | Grabber | None = None, hold_slot: str | Slot | None = None, pos: str | Sync[primitives.Float3] | None = None, rot: str | Sync[primitives.FloatQ] | None = None, scl: str | Sync[primitives.Float3] | None = None, legacy_active_user_root_only: bool | None = None, grab_priority: np.int32 | None = None, max_swing: np.float32 | None = None, max_twist: np.float32 | None = None, axis: primitives.Float3 | None = None, twist_reference_axis: primitives.Float3 | None = None, position_twist_threshold_angle: np.float32 | None = None, vibration_angle: np.float32 | None = None, snap_increment: np.float32 | None = None, snap_time: np.float32 | None = None, snap_on_release: bool | None = None, orig_rotation: primitives.FloatQ | None = None, rot_reference: primitives.FloatQ | None = None, dir_reference: primitives.Float3 | None = None, twist_reference: primitives.Float3 | None = None, use_position_twist: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            edit_mode_only: Initial value for EditModeOnly.
            allow_steal: Initial value for AllowSteal.
            drop_on_disable: Initial value for DropOnDisable.
            dont_drive: Initial value for DontDrive.
            allow_only_physical_grab: Initial value for AllowOnlyPhysicalGrab.
            grabber: Initial value for _grabber.
            hold_slot: Initial value for _holdSlot.
            pos: Initial value for _pos.
            rot: Initial value for _rot.
            scl: Initial value for _scl.
            legacy_active_user_root_only: Initial value for __legacyActiveUserRootOnly.
            grab_priority: Initial value for GrabPriority.
            max_swing: Initial value for MaxSwing.
            max_twist: Initial value for MaxTwist.
            axis: Initial value for Axis.
            twist_reference_axis: Initial value for TwistReferenceAxis.
            position_twist_threshold_angle: Initial value for PositionTwistThresholdAngle.
            vibration_angle: Initial value for VibrationAngle.
            snap_increment: Initial value for SnapIncrement.
            snap_time: Initial value for SnapTime.
            snap_on_release: Initial value for SnapOnRelease.
            orig_rotation: Initial value for origRotation.
            rot_reference: Initial value for rotReference.
            dir_reference: Initial value for dirReference.
            twist_reference: Initial value for twistReference.
            use_position_twist: Initial value for usePositionTwist.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if allow_steal is not None:
            self.allow_steal = allow_steal
        if drop_on_disable is not None:
            self.drop_on_disable = drop_on_disable
        if dont_drive is not None:
            self.dont_drive = dont_drive
        if allow_only_physical_grab is not None:
            self.allow_only_physical_grab = allow_only_physical_grab
        if grabber is not None:
            self.grabber = grabber
        if hold_slot is not None:
            self.hold_slot = hold_slot
        if pos is not None:
            self.pos = pos
        if rot is not None:
            self.rot = rot
        if scl is not None:
            self.scl = scl
        if legacy_active_user_root_only is not None:
            self.legacy_active_user_root_only = legacy_active_user_root_only
        if grab_priority is not None:
            self.grab_priority = grab_priority
        if max_swing is not None:
            self.max_swing = max_swing
        if max_twist is not None:
            self.max_twist = max_twist
        if axis is not None:
            self.axis = axis
        if twist_reference_axis is not None:
            self.twist_reference_axis = twist_reference_axis
        if position_twist_threshold_angle is not None:
            self.position_twist_threshold_angle = position_twist_threshold_angle
        if vibration_angle is not None:
            self.vibration_angle = vibration_angle
        if snap_increment is not None:
            self.snap_increment = snap_increment
        if snap_time is not None:
            self.snap_time = snap_time
        if snap_on_release is not None:
            self.snap_on_release = snap_on_release
        if orig_rotation is not None:
            self.orig_rotation = orig_rotation
        if rot_reference is not None:
            self.rot_reference = rot_reference
        if dir_reference is not None:
            self.dir_reference = dir_reference
        if twist_reference is not None:
            self.twist_reference = twist_reference
        if use_position_twist is not None:
            self.use_position_twist = use_position_twist

    @property
    def edit_mode_only(self) -> bool | None:
        """The EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: bool) -> None:
        """Set the EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeOnly", fields.FieldBool(value=value)
            )

    @property
    def allow_steal(self) -> bool | None:
        """The AllowSteal field value."""
        member = self.get_member("AllowSteal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_steal.setter
    def allow_steal(self, value: bool) -> None:
        """Set the AllowSteal field value."""
        member = self.get_member("AllowSteal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSteal", fields.FieldBool(value=value)
            )

    @property
    def drop_on_disable(self) -> bool | None:
        """The DropOnDisable field value."""
        member = self.get_member("DropOnDisable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drop_on_disable.setter
    def drop_on_disable(self, value: bool) -> None:
        """Set the DropOnDisable field value."""
        member = self.get_member("DropOnDisable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DropOnDisable", fields.FieldBool(value=value)
            )

    @property
    def dont_drive(self) -> bool | None:
        """The DontDrive field value."""
        member = self.get_member("DontDrive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dont_drive.setter
    def dont_drive(self, value: bool) -> None:
        """Set the DontDrive field value."""
        member = self.get_member("DontDrive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DontDrive", fields.FieldBool(value=value)
            )

    @property
    def allow_only_physical_grab(self) -> bool | None:
        """The AllowOnlyPhysicalGrab field value."""
        member = self.get_member("AllowOnlyPhysicalGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_only_physical_grab.setter
    def allow_only_physical_grab(self, value: bool) -> None:
        """Set the AllowOnlyPhysicalGrab field value."""
        member = self.get_member("AllowOnlyPhysicalGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowOnlyPhysicalGrab", fields.FieldBool(value=value)
            )

    @property
    def active_user_filter(self) -> members.FieldEnum | None:
        """The ActiveUserFilter member."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @active_user_filter.setter
    def active_user_filter(self, value: members.FieldEnum) -> None:
        """Set the ActiveUserFilter member."""
        self.set_member("ActiveUserFilter", value)

    @property
    def grabber(self) -> str | None:
        """Target ID of the _grabber reference (targets Grabber)."""
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabber.setter
    def grabber(self, target: str | Grabber | None) -> None:
        """Set the _grabber reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

    @property
    def hold_slot(self) -> str | None:
        """Target ID of the _holdSlot reference (targets Slot)."""
        member = self.get_member("_holdSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hold_slot.setter
    def hold_slot(self, target: str | Slot | None) -> None:
        """Set the _holdSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_holdSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_holdSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def pos(self) -> str | None:
        """Target ID of the _pos reference (targets Sync[primitives.Float3])."""
        member = self.get_member("_pos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pos.setter
    def pos(self, target: str | Sync[primitives.Float3] | None) -> None:
        """Set the _pos reference by target ID or Sync[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("_pos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float3>'),
            )

    @property
    def rot(self) -> str | None:
        """Target ID of the _rot reference (targets Sync[primitives.FloatQ])."""
        member = self.get_member("_rot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rot.setter
    def rot(self, target: str | Sync[primitives.FloatQ] | None) -> None:
        """Set the _rot reference by target ID or Sync[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("_rot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<floatQ>'),
            )

    @property
    def scl(self) -> str | None:
        """Target ID of the _scl reference (targets Sync[primitives.Float3])."""
        member = self.get_member("_scl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scl.setter
    def scl(self, target: str | Sync[primitives.Float3] | None) -> None:
        """Set the _scl reference by target ID or Sync[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("_scl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float3>'),
            )

    @property
    def legacy_active_user_root_only(self) -> bool | None:
        """The __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_active_user_root_only.setter
    def legacy_active_user_root_only(self, value: bool) -> None:
        """Set the __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyActiveUserRootOnly", fields.FieldBool(value=value)
            )

    @property
    def grab_priority(self) -> np.int32 | None:
        """The GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_priority.setter
    def grab_priority(self, value: np.int32) -> None:
        """Set the GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabPriority", fields.FieldInt(value=value)
            )

    @property
    def max_swing(self) -> np.float32 | None:
        """The MaxSwing field value."""
        member = self.get_member("MaxSwing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_swing.setter
    def max_swing(self, value: np.float32) -> None:
        """Set the MaxSwing field value."""
        member = self.get_member("MaxSwing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSwing", fields.FieldFloat(value=value)
            )

    @property
    def max_twist(self) -> np.float32 | None:
        """The MaxTwist field value."""
        member = self.get_member("MaxTwist")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_twist.setter
    def max_twist(self, value: np.float32) -> None:
        """Set the MaxTwist field value."""
        member = self.get_member("MaxTwist")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTwist", fields.FieldFloat(value=value)
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
    def twist_reference_axis(self) -> primitives.Float3 | None:
        """The TwistReferenceAxis field value."""
        member = self.get_member("TwistReferenceAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @twist_reference_axis.setter
    def twist_reference_axis(self, value: primitives.Float3) -> None:
        """Set the TwistReferenceAxis field value."""
        member = self.get_member("TwistReferenceAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TwistReferenceAxis", fields.FieldFloat3(value=value)
            )

    @property
    def position_twist_threshold_angle(self) -> np.float32 | None:
        """The PositionTwistThresholdAngle field value."""
        member = self.get_member("PositionTwistThresholdAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_twist_threshold_angle.setter
    def position_twist_threshold_angle(self, value: np.float32) -> None:
        """Set the PositionTwistThresholdAngle field value."""
        member = self.get_member("PositionTwistThresholdAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionTwistThresholdAngle", fields.FieldFloat(value=value)
            )

    @property
    def vibration_angle(self) -> np.float32 | None:
        """The VibrationAngle field value."""
        member = self.get_member("VibrationAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vibration_angle.setter
    def vibration_angle(self, value: np.float32) -> None:
        """Set the VibrationAngle field value."""
        member = self.get_member("VibrationAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VibrationAngle", fields.FieldFloat(value=value)
            )

    @property
    def vibration_preset(self) -> members.FieldEnum | None:
        """The VibrationPreset member."""
        member = self.get_member("VibrationPreset")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vibration_preset.setter
    def vibration_preset(self, value: members.FieldEnum) -> None:
        """Set the VibrationPreset member."""
        self.set_member("VibrationPreset", value)

    @property
    def snap_increment(self) -> np.float32 | None:
        """The SnapIncrement field value."""
        member = self.get_member("SnapIncrement")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_increment.setter
    def snap_increment(self, value: np.float32) -> None:
        """Set the SnapIncrement field value."""
        member = self.get_member("SnapIncrement")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapIncrement", fields.FieldFloat(value=value)
            )

    @property
    def snap_time(self) -> np.float32 | None:
        """The SnapTime field value."""
        member = self.get_member("SnapTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_time.setter
    def snap_time(self, value: np.float32) -> None:
        """Set the SnapTime field value."""
        member = self.get_member("SnapTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapTime", fields.FieldFloat(value=value)
            )

    @property
    def snap_on_release(self) -> bool | None:
        """The SnapOnRelease field value."""
        member = self.get_member("SnapOnRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_on_release.setter
    def snap_on_release(self, value: bool) -> None:
        """Set the SnapOnRelease field value."""
        member = self.get_member("SnapOnRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapOnRelease", fields.FieldBool(value=value)
            )

    @property
    def snap_orientations(self) -> members.SyncList | None:
        """The SnapOrientations member."""
        member = self.get_member("SnapOrientations")
        if isinstance(member, members.SyncList):
            return member
        return None

    @snap_orientations.setter
    def snap_orientations(self, value: members.SyncList) -> None:
        """Set the SnapOrientations member."""
        self.set_member("SnapOrientations", value)

    @property
    def orig_rotation(self) -> primitives.FloatQ | None:
        """The origRotation field value."""
        member = self.get_member("origRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orig_rotation.setter
    def orig_rotation(self, value: primitives.FloatQ) -> None:
        """Set the origRotation field value."""
        member = self.get_member("origRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "origRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def rot_reference(self) -> primitives.FloatQ | None:
        """The rotReference field value."""
        member = self.get_member("rotReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rot_reference.setter
    def rot_reference(self, value: primitives.FloatQ) -> None:
        """Set the rotReference field value."""
        member = self.get_member("rotReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "rotReference", fields.FieldFloatQ(value=value)
            )

    @property
    def dir_reference(self) -> primitives.Float3 | None:
        """The dirReference field value."""
        member = self.get_member("dirReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dir_reference.setter
    def dir_reference(self, value: primitives.Float3) -> None:
        """Set the dirReference field value."""
        member = self.get_member("dirReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "dirReference", fields.FieldFloat3(value=value)
            )

    @property
    def twist_reference(self) -> primitives.Float3 | None:
        """The twistReference field value."""
        member = self.get_member("twistReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @twist_reference.setter
    def twist_reference(self, value: primitives.Float3) -> None:
        """Set the twistReference field value."""
        member = self.get_member("twistReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "twistReference", fields.FieldFloat3(value=value)
            )

    @property
    def use_position_twist(self) -> bool | None:
        """The usePositionTwist field value."""
        member = self.get_member("usePositionTwist")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_position_twist.setter
    def use_position_twist(self, value: bool) -> None:
        """Set the usePositionTwist field value."""
        member = self.get_member("usePositionTwist")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "usePositionTwist", fields.FieldBool(value=value)
            )

