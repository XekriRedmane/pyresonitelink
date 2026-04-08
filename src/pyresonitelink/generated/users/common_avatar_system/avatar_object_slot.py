"""Generated component: AvatarObjectSlot."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object import IAvatarObject
from pyresonitelink.generated._types.avatar_pose_smooth_lerp import AvatarPoseSmoothLerp
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarObjectSlot(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot"

    def __init__(self, priority: np.int32 | None = None, equipped: str | IAvatarObject | None = None, is_tracking: bool | None = None, is_active: bool | None = None, is_simulated: bool | None = None, drive_active: bool | None = None, drive_scale: bool | None = None, do_not_simulate: bool | None = None, auto_smoothing: str | AvatarPoseSmoothLerp | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            equipped: Initial value for Equipped.
            is_tracking: Initial value for IsTracking.
            is_active: Initial value for IsActive.
            is_simulated: Initial value for IsSimulated.
            drive_active: Initial value for DriveActive.
            drive_scale: Initial value for DriveScale.
            do_not_simulate: Initial value for DoNotSimulate.
            auto_smoothing: Initial value for _autoSmoothing.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if priority is not None:
            self.priority = priority
        if equipped is not None:
            self.equipped = equipped
        if is_tracking is not None:
            self.is_tracking = is_tracking
        if is_active is not None:
            self.is_active = is_active
        if is_simulated is not None:
            self.is_simulated = is_simulated
        if drive_active is not None:
            self.drive_active = drive_active
        if drive_scale is not None:
            self.drive_scale = drive_scale
        if do_not_simulate is not None:
            self.do_not_simulate = do_not_simulate
        if auto_smoothing is not None:
            self.auto_smoothing = auto_smoothing

    @property
    def priority(self) -> np.int32 | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: np.int32) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def equipped(self) -> str | None:
        """Target ID of the Equipped reference (targets IAvatarObject)."""
        member = self.get_member("Equipped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @equipped.setter
    def equipped(self, target: str | IAvatarObject | None) -> None:
        """Set the Equipped reference by target ID or IAvatarObject instance."""
        target_id: str | None = target.id if isinstance(target, IAvatarObject) else target  # type: ignore[assignment]
        member = self.get_member("Equipped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Equipped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.IAvatarObject'),
            )

    @property
    def node(self) -> members.FieldEnum | None:
        """The Node member."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @node.setter
    def node(self, value: members.FieldEnum) -> None:
        """Set the Node member."""
        self.set_member("Node", value)

    @property
    def is_tracking(self) -> bool | None:
        """The IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_tracking.setter
    def is_tracking(self, value: bool) -> None:
        """Set the IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsTracking", fields.FieldBool(value=value)
            )

    @property
    def is_active(self) -> bool | None:
        """The IsActive field value."""
        member = self.get_member("IsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_active.setter
    def is_active(self, value: bool) -> None:
        """Set the IsActive field value."""
        member = self.get_member("IsActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsActive", fields.FieldBool(value=value)
            )

    @property
    def is_simulated(self) -> bool | None:
        """The IsSimulated field value."""
        member = self.get_member("IsSimulated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_simulated.setter
    def is_simulated(self, value: bool) -> None:
        """Set the IsSimulated field value."""
        member = self.get_member("IsSimulated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSimulated", fields.FieldBool(value=value)
            )

    @property
    def drive_active(self) -> bool | None:
        """The DriveActive field value."""
        member = self.get_member("DriveActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drive_active.setter
    def drive_active(self, value: bool) -> None:
        """Set the DriveActive field value."""
        member = self.get_member("DriveActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DriveActive", fields.FieldBool(value=value)
            )

    @property
    def drive_scale(self) -> bool | None:
        """The DriveScale field value."""
        member = self.get_member("DriveScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drive_scale.setter
    def drive_scale(self, value: bool) -> None:
        """Set the DriveScale field value."""
        member = self.get_member("DriveScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DriveScale", fields.FieldBool(value=value)
            )

    @property
    def do_not_simulate(self) -> bool | None:
        """The DoNotSimulate field value."""
        member = self.get_member("DoNotSimulate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @do_not_simulate.setter
    def do_not_simulate(self, value: bool) -> None:
        """Set the DoNotSimulate field value."""
        member = self.get_member("DoNotSimulate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoNotSimulate", fields.FieldBool(value=value)
            )

    @property
    def filters(self) -> members.SyncObject | None:
        """The Filters member."""
        member = self.get_member("Filters")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @filters.setter
    def filters(self, value: members.SyncObject) -> None:
        """Set the Filters member."""
        self.set_member("Filters", value)

    @property
    def auto_smoothing(self) -> str | None:
        """Target ID of the _autoSmoothing reference (targets AvatarPoseSmoothLerp)."""
        member = self.get_member("_autoSmoothing")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_smoothing.setter
    def auto_smoothing(self, target: str | AvatarPoseSmoothLerp | None) -> None:
        """Set the _autoSmoothing reference by target ID or AvatarPoseSmoothLerp instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseSmoothLerp) else target  # type: ignore[assignment]
        member = self.get_member("_autoSmoothing")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autoSmoothing",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseSmoothLerp'),
            )

