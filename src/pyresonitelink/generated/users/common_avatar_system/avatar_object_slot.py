"""Generated component: AvatarObjectSlot."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.body_node import BodyNode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object import IAvatarObject
from pyresonitelink.generated._types.avatar_pose_smooth_lerp import AvatarPoseSmoothLerp
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarObjectSlot(GeneratedComponent, IComponent, IWorldEventReceiver):
    """For detailed information on how this functions for mix and match body parts. Please also see Equipping Multiple Avatars.

Avatar Object slot is a component that is used to move and drive certain parts of the avatar like the head and hand body parts.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot"

    def __init__(self, priority: primitives.Int | None = None, equipped: str | IAvatarObject | None = None, node: BodyNode | str | None = None, is_tracking: primitives.Bool | None = None, is_active: primitives.Bool | None = None, is_simulated: primitives.Bool | None = None, drive_active: primitives.Bool | None = None, drive_scale: primitives.Bool | None = None, do_not_simulate: primitives.Bool | None = None, auto_smoothing: str | AvatarPoseSmoothLerp | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            equipped: Initial value for Equipped.
            node: Initial value for Node.
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
        if node is not None:
            self.node = node
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
    def priority(self) -> primitives.Int | None:
        """Whether to do the equip checking on this AvatarObjectSlot before other AvatarObjectSlots"""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
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
        """Usually an Avatar Pose Node that is on one of the proxies on an avatar."""
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
    def node(self) -> BodyNode | None:
        """the body node of the avatar this component's slot is. Unless already specified by a Biped Rig Component higher up in the hierarchy."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BodyNode(member.value)
        return None

    @node.setter
    def node(self, value: BodyNode | str) -> None:
        """Set Node. the body node of the avatar this component's slot is. Unless already specified by a Biped Rig Component higher up in the hierarchy."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Node",
                members.FieldEnum(value=str(value)),
            )

    @property
    def is_tracking(self) -> primitives.Bool | None:
        """Whether this component is currently being simulated by the procedural animation system."""
        member = self.get_member("IsTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_tracking.setter
    def is_tracking(self, value: primitives.Bool) -> None:
        """Set the IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsTracking", fields.FieldBool(value=value)
            )

    @property
    def is_active(self) -> primitives.Bool | None:
        """Whether this component is currently active and controlling an avatar."""
        member = self.get_member("IsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_active.setter
    def is_active(self, value: primitives.Bool) -> None:
        """Set the IsActive field value."""
        member = self.get_member("IsActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsActive", fields.FieldBool(value=value)
            )

    @property
    def is_simulated(self) -> primitives.Bool | None:
        """Whether this object slot is being controlled by the procedural animation system."""
        member = self.get_member("IsSimulated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_simulated.setter
    def is_simulated(self, value: primitives.Bool) -> None:
        """Set the IsSimulated field value."""
        member = self.get_member("IsSimulated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSimulated", fields.FieldBool(value=value)
            )

    @property
    def drive_active(self) -> primitives.Bool | None:
        """Whether to drive the active of this slot when hooked into by an Avatar Pose Node."""
        member = self.get_member("DriveActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drive_active.setter
    def drive_active(self, value: primitives.Bool) -> None:
        """Set the DriveActive field value."""
        member = self.get_member("DriveActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DriveActive", fields.FieldBool(value=value)
            )

    @property
    def drive_scale(self) -> primitives.Bool | None:
        """Whether to drive the scale of this slot when hooked into by an Avatar Pose Node."""
        member = self.get_member("DriveScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drive_scale.setter
    def drive_scale(self, value: primitives.Bool) -> None:
        """Set the DriveScale field value."""
        member = self.get_member("DriveScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DriveScale", fields.FieldBool(value=value)
            )

    @property
    def do_not_simulate(self) -> primitives.Bool | None:
        """Whether to not control this with the procedural locomotion system"""
        member = self.get_member("DoNotSimulate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @do_not_simulate.setter
    def do_not_simulate(self, value: primitives.Bool) -> None:
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
        """Filters that are currently effecting this and their priorities. See Avatar Pose Filters"""
        member = self.get_member("Filters")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @filters.setter
    def filters(self, value: members.SyncObject) -> None:
        """Set Filters. Filters that are currently effecting this and their priorities. See Avatar Pose Filters"""
        self.set_member("Filters", value)

    @property
    def auto_smoothing(self) -> str | None:
        """The Component currently smoothing the transform changes of this Avatar Object slot."""
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

