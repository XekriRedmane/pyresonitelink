"""Generated component: Slider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.active_user_handling import ActiveUserHandling
from pyresonitelink.generated._enums.vibrate_preset import VibratePreset
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Slider(GeneratedComponent, IGrabbable, IWorldEventReceiver):
    """The Slider component allows for an object to be grabbed and moved. See Usage for more information.

    Category: Transform/Interaction

    This can be used for NPC pickups, grabbing objects and moving them
    without parenting under a user, or for sliding doors. this can also be
    used for physical sliders like on audio boards like mixers.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Slider"

    def __init__(self, edit_mode_only: primitives.Bool | None = None, allow_steal: primitives.Bool | None = None, drop_on_disable: primitives.Bool | None = None, dont_drive: primitives.Bool | None = None, allow_only_physical_grab: primitives.Bool | None = None, active_user_filter: ActiveUserHandling | str | None = None, grabber: str | Grabber | None = None, hold_slot: str | Slot | None = None, pos: str | Sync[primitives.Float3] | None = None, rot: str | Sync[primitives.FloatQ] | None = None, scl: str | Sync[primitives.Float3] | None = None, legacy_active_user_root_only: primitives.Bool | None = None, grab_priority: primitives.Int | None = None, rotatable: primitives.Bool | None = None, scalable: primitives.Bool | None = None, range_: primitives.Float3 | None = None, origin: primitives.Float3 | None = None, min_scale: primitives.Float3 | None = None, max_scale: primitives.Float3 | None = None, vibration_offset: primitives.Float | None = None, vibration_preset: VibratePreset | str | None = None, snap_increment: primitives.Float | None = None, snap_time: primitives.Float | None = None, snap_on_release: primitives.Bool | None = None, pos_offset: primitives.Float3 | None = None, rot_offset: primitives.FloatQ | None = None, scale_reference: primitives.Float3 | None = None, reference_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            edit_mode_only: Initial value for EditModeOnly.
            allow_steal: Initial value for AllowSteal.
            drop_on_disable: Initial value for DropOnDisable.
            dont_drive: Initial value for DontDrive.
            allow_only_physical_grab: Initial value for AllowOnlyPhysicalGrab.
            active_user_filter: Initial value for ActiveUserFilter.
            grabber: Initial value for _grabber.
            hold_slot: Initial value for _holdSlot.
            pos: Initial value for _pos.
            rot: Initial value for _rot.
            scl: Initial value for _scl.
            legacy_active_user_root_only: Initial value for __legacyActiveUserRootOnly.
            grab_priority: Initial value for GrabPriority.
            rotatable: Initial value for Rotatable.
            scalable: Initial value for Scalable.
            range_: Initial value for Range.
            origin: Initial value for Origin.
            min_scale: Initial value for MinScale.
            max_scale: Initial value for MaxScale.
            vibration_offset: Initial value for VibrationOffset.
            vibration_preset: Initial value for VibrationPreset.
            snap_increment: Initial value for SnapIncrement.
            snap_time: Initial value for SnapTime.
            snap_on_release: Initial value for SnapOnRelease.
            pos_offset: Initial value for posOffset.
            rot_offset: Initial value for rotOffset.
            scale_reference: Initial value for scaleReference.
            reference_parent: Initial value for referenceParent.
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
        if active_user_filter is not None:
            self.active_user_filter = active_user_filter
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
        if rotatable is not None:
            self.rotatable = rotatable
        if scalable is not None:
            self.scalable = scalable
        if range_ is not None:
            self.range_ = range_
        if origin is not None:
            self.origin = origin
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale
        if vibration_offset is not None:
            self.vibration_offset = vibration_offset
        if vibration_preset is not None:
            self.vibration_preset = vibration_preset
        if snap_increment is not None:
            self.snap_increment = snap_increment
        if snap_time is not None:
            self.snap_time = snap_time
        if snap_on_release is not None:
            self.snap_on_release = snap_on_release
        if pos_offset is not None:
            self.pos_offset = pos_offset
        if rot_offset is not None:
            self.rot_offset = rot_offset
        if scale_reference is not None:
            self.scale_reference = scale_reference
        if reference_parent is not None:
            self.reference_parent = reference_parent

    @property
    def edit_mode_only(self) -> primitives.Bool | None:
        """Determines if this grabbable is effective only in Edit Mode"""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: primitives.Bool) -> None:
        """Set the EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeOnly", fields.FieldBool(value=value)
            )

    @property
    def allow_steal(self) -> primitives.Bool | None:
        """Other users can grab the slot this component is attached to. Like a flag in capture the flag."""
        member = self.get_member("AllowSteal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_steal.setter
    def allow_steal(self, value: primitives.Bool) -> None:
        """Set the AllowSteal field value."""
        member = self.get_member("AllowSteal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSteal", fields.FieldBool(value=value)
            )

    @property
    def drop_on_disable(self) -> primitives.Bool | None:
        """The parent slot will be dropped when this component is disabled."""
        member = self.get_member("DropOnDisable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drop_on_disable.setter
    def drop_on_disable(self, value: primitives.Bool) -> None:
        """Set the DropOnDisable field value."""
        member = self.get_member("DropOnDisable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DropOnDisable", fields.FieldBool(value=value)
            )

    @property
    def dont_drive(self) -> primitives.Bool | None:
        """Write the transforms every game tick, rather than driving it on the local machine and then sending the final value to the host."""
        member = self.get_member("DontDrive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dont_drive.setter
    def dont_drive(self, value: primitives.Bool) -> None:
        """Set the DontDrive field value."""
        member = self.get_member("DontDrive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DontDrive", fields.FieldBool(value=value)
            )

    @property
    def allow_only_physical_grab(self) -> primitives.Bool | None:
        """Only allow grab an object with a physical interaction - remote grabs are not allowed"""
        member = self.get_member("AllowOnlyPhysicalGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_only_physical_grab.setter
    def allow_only_physical_grab(self, value: primitives.Bool) -> None:
        """Set the AllowOnlyPhysicalGrab field value."""
        member = self.get_member("AllowOnlyPhysicalGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowOnlyPhysicalGrab", fields.FieldBool(value=value)
            )

    @property
    def active_user_filter(self) -> ActiveUserHandling | None:
        """Changes if this component can be grabbed based on who is the active user if any."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ActiveUserHandling(member.value)
        return None

    @active_user_filter.setter
    def active_user_filter(self, value: ActiveUserHandling | str) -> None:
        """Set ActiveUserFilter. Changes if this component can be grabbed based on who is the active user if any."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ActiveUserFilter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def grabber(self) -> str | None:
        """Automatically Assigned, the grabber that is grabbing this component."""
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
        """The slot that is "holding" this slot, but not actually acting as this slider's parent."""
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
        """The field this is currently driving for position."""
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
        """The field this is currently driving for rotation."""
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
        """The field this is currently driving for scale."""
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
    def legacy_active_user_root_only(self) -> primitives.Bool | None:
        """Automatically Assigned Legacy do not use. Used to handle whether only the active user can grab. Use ``ActiveUserFilter`` instead!"""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_active_user_root_only.setter
    def legacy_active_user_root_only(self, value: primitives.Bool) -> None:
        """Set the __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyActiveUserRootOnly", fields.FieldBool(value=value)
            )

    @property
    def grab_priority(self) -> primitives.Int | None:
        """The GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_priority.setter
    def grab_priority(self, value: primitives.Int) -> None:
        """Set the GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabPriority", fields.FieldInt(value=value)
            )

    @property
    def rotatable(self) -> primitives.Bool | None:
        """Whether the slider object is rotatable."""
        member = self.get_member("Rotatable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotatable.setter
    def rotatable(self, value: primitives.Bool) -> None:
        """Set the Rotatable field value."""
        member = self.get_member("Rotatable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rotatable", fields.FieldBool(value=value)
            )

    @property
    def scalable(self) -> primitives.Bool | None:
        """Whether the slider is scalable."""
        member = self.get_member("Scalable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scalable.setter
    def scalable(self, value: primitives.Bool) -> None:
        """Set the Scalable field value."""
        member = self.get_member("Scalable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scalable", fields.FieldBool(value=value)
            )

    @property
    def range_(self) -> primitives.Float3 | None:
        """The range that the object is allowed to move position wise."""
        member = self.get_member("Range")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_.setter
    def range_(self, value: primitives.Float3) -> None:
        """Set the Range field value."""
        member = self.get_member("Range")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Range", fields.FieldFloat3(value=value)
            )

    @property
    def origin(self) -> primitives.Float3 | None:
        """The origin of the range that the object is allowed to move."""
        member = self.get_member("Origin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @origin.setter
    def origin(self, value: primitives.Float3) -> None:
        """Set the Origin field value."""
        member = self.get_member("Origin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Origin", fields.FieldFloat3(value=value)
            )

    @property
    def min_scale(self) -> primitives.Float3 | None:
        """The minimum scale the object can be scaled to."""
        member = self.get_member("MinScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_scale.setter
    def min_scale(self, value: primitives.Float3) -> None:
        """Set the MinScale field value."""
        member = self.get_member("MinScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinScale", fields.FieldFloat3(value=value)
            )

    @property
    def max_scale(self) -> primitives.Float3 | None:
        """The maximum scale the object can be scaled to."""
        member = self.get_member("MaxScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_scale.setter
    def max_scale(self, value: primitives.Float3) -> None:
        """Set the MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxScale", fields.FieldFloat3(value=value)
            )

    @property
    def vibration_offset(self) -> primitives.Float | None:
        """The offset of the vibration intensity."""
        member = self.get_member("VibrationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vibration_offset.setter
    def vibration_offset(self, value: primitives.Float) -> None:
        """Set the VibrationOffset field value."""
        member = self.get_member("VibrationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VibrationOffset", fields.FieldFloat(value=value)
            )

    @property
    def vibration_preset(self) -> VibratePreset | None:
        """The preset for triggering vibration with this object."""
        member = self.get_member("VibrationPreset")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @vibration_preset.setter
    def vibration_preset(self, value: VibratePreset | str) -> None:
        """Set VibrationPreset. The preset for triggering vibration with this object."""
        member = self.get_member("VibrationPreset")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VibrationPreset",
                members.FieldEnum(value=str(value)),
            )

    @property
    def snap_increment(self) -> primitives.Float | None:
        """What increment the position of this object should snap to, instead of allowing smooth movement."""
        member = self.get_member("SnapIncrement")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_increment.setter
    def snap_increment(self, value: primitives.Float) -> None:
        """Set the SnapIncrement field value."""
        member = self.get_member("SnapIncrement")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapIncrement", fields.FieldFloat(value=value)
            )

    @property
    def snap_time(self) -> primitives.Float | None:
        """The time the object will take to move to a snap position when it snaps."""
        member = self.get_member("SnapTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_time.setter
    def snap_time(self, value: primitives.Float) -> None:
        """Set the SnapTime field value."""
        member = self.get_member("SnapTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapTime", fields.FieldFloat(value=value)
            )

    @property
    def snap_on_release(self) -> primitives.Bool | None:
        """Only snap to positions in ``SnapPositions`` when released rather than always."""
        member = self.get_member("SnapOnRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_on_release.setter
    def snap_on_release(self, value: primitives.Bool) -> None:
        """Set the SnapOnRelease field value."""
        member = self.get_member("SnapOnRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapOnRelease", fields.FieldBool(value=value)
            )

    @property
    def snap_positions(self) -> members.SyncList | None:
        """Positions to snap to while grabbing or when released."""
        member = self.get_member("SnapPositions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @snap_positions.setter
    def snap_positions(self, value: members.SyncList) -> None:
        """Set SnapPositions. Positions to snap to while grabbing or when released."""
        self.set_member("SnapPositions", value)

    @property
    def pos_offset(self) -> primitives.Float3 | None:
        """How much to offset the slider's position."""
        member = self.get_member("posOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_offset.setter
    def pos_offset(self, value: primitives.Float3) -> None:
        """Set the posOffset field value."""
        member = self.get_member("posOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "posOffset", fields.FieldFloat3(value=value)
            )

    @property
    def rot_offset(self) -> primitives.FloatQ | None:
        """How much to offset the slider's rotation."""
        member = self.get_member("rotOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rot_offset.setter
    def rot_offset(self, value: primitives.FloatQ) -> None:
        """Set the rotOffset field value."""
        member = self.get_member("rotOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "rotOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def scale_reference(self) -> primitives.Float3 | None:
        """The original scale reference value."""
        member = self.get_member("scaleReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_reference.setter
    def scale_reference(self, value: primitives.Float3) -> None:
        """Set the scaleReference field value."""
        member = self.get_member("scaleReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "scaleReference", fields.FieldFloat3(value=value)
            )

    @property
    def reference_parent(self) -> str | None:
        """The slot that is supposed to be this slider's parent."""
        member = self.get_member("referenceParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_parent.setter
    def reference_parent(self, target: str | Slot | None) -> None:
        """Set the referenceParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("referenceParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "referenceParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

