"""Generated component: PositionAtUser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.user_node import UserNode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PositionAtUser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The PositionAtUser component drives the values in ``PositionDrive`` and ``RotationDrive`` to match the user's position and rotation as determined by the settings in ``PositionSource`` and ``RotationSource`` respectively.

    Category: Transform/Drivers

    **Behavior**: == Examples ==
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PositionAtUser"

    def __init__(self, target_user: str | User | None = None, position_at_local_user: primitives.Bool | None = None, target_position_offset: primitives.Float3 | None = None, target_rotation_offset: primitives.FloatQ | None = None, position_offset: primitives.Float3 | None = None, rotation_offset: primitives.FloatQ | None = None, position_source: UserNode | str | None = None, rotation_source: UserNode | str | None = None, position_drive: str | IField[primitives.Float3] | None = None, rotation_drive: str | IField[primitives.FloatQ] | None = None, run_after_final_pose_update: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_user: Initial value for TargetUser.
            position_at_local_user: Initial value for PositionAtLocalUser.
            target_position_offset: Initial value for TargetPositionOffset.
            target_rotation_offset: Initial value for TargetRotationOffset.
            position_offset: Initial value for PositionOffset.
            rotation_offset: Initial value for RotationOffset.
            position_source: Initial value for PositionSource.
            rotation_source: Initial value for RotationSource.
            position_drive: Initial value for PositionDrive.
            rotation_drive: Initial value for RotationDrive.
            run_after_final_pose_update: Initial value for RunAfterFinalPoseUpdate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_user is not None:
            self.target_user = target_user
        if position_at_local_user is not None:
            self.position_at_local_user = position_at_local_user
        if target_position_offset is not None:
            self.target_position_offset = target_position_offset
        if target_rotation_offset is not None:
            self.target_rotation_offset = target_rotation_offset
        if position_offset is not None:
            self.position_offset = position_offset
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset
        if position_source is not None:
            self.position_source = position_source
        if rotation_source is not None:
            self.rotation_source = rotation_source
        if position_drive is not None:
            self.position_drive = position_drive
        if rotation_drive is not None:
            self.rotation_drive = rotation_drive
        if run_after_final_pose_update is not None:
            self.run_after_final_pose_update = run_after_final_pose_update

    @property
    def target_user(self) -> str | None:
        """The user that will be used to calculate the parent slot position, unless ``PositionAtLocalUser`` is selected."""
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
    def position_at_local_user(self) -> primitives.Bool | None:
        """Position the parent slot at the Local User of each client, ignoring the value in ``TargetUser``"""
        member = self.get_member("PositionAtLocalUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_at_local_user.setter
    def position_at_local_user(self, value: primitives.Bool) -> None:
        """Set the PositionAtLocalUser field value."""
        member = self.get_member("PositionAtLocalUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionAtLocalUser", fields.FieldBool(value=value)
            )

    @property
    def target_position_offset(self) -> primitives.Float3 | None:
        """Position offset in the user's local space units. Respects the user's current scale and transforms."""
        member = self.get_member("TargetPositionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_position_offset.setter
    def target_position_offset(self, value: primitives.Float3) -> None:
        """Set the TargetPositionOffset field value."""
        member = self.get_member("TargetPositionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetPositionOffset", fields.FieldFloat3(value=value)
            )

    @property
    def target_rotation_offset(self) -> primitives.FloatQ | None:
        """Rotation offset in the user's local space unit. Respects the user's current scale and transforms."""
        member = self.get_member("TargetRotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_rotation_offset.setter
    def target_rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the TargetRotationOffset field value."""
        member = self.get_member("TargetRotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetRotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def position_offset(self) -> primitives.Float3 | None:
        """Position offset in global space units"""
        member = self.get_member("PositionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_offset.setter
    def position_offset(self, value: primitives.Float3) -> None:
        """Set the PositionOffset field value."""
        member = self.get_member("PositionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionOffset", fields.FieldFloat3(value=value)
            )

    @property
    def rotation_offset(self) -> primitives.FloatQ | None:
        """Rotation offset in global space units"""
        member = self.get_member("RotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_offset.setter
    def rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def position_source(self) -> UserNode | None:
        """The user node that the position will be calculated from"""
        member = self.get_member("PositionSource")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @position_source.setter
    def position_source(self, value: UserNode | str) -> None:
        """Set PositionSource. The user node that the position will be calculated from"""
        member = self.get_member("PositionSource")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositionSource",
                members.FieldEnum(value=str(value)),
            )

    @property
    def rotation_source(self) -> UserNode | None:
        """The user node that the rotation will be calculated from"""
        member = self.get_member("RotationSource")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @rotation_source.setter
    def rotation_source(self, value: UserNode | str) -> None:
        """Set RotationSource. The user node that the rotation will be calculated from"""
        member = self.get_member("RotationSource")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RotationSource",
                members.FieldEnum(value=str(value)),
            )

    @property
    def position_drive(self) -> str | None:
        """Target Float3 to drive with the calculated position value"""
        member = self.get_member("PositionDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_drive.setter
    def position_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the PositionDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PositionDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PositionDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rotation_drive(self) -> str | None:
        """Target FloatQ to drive with the calculated rotation value."""
        member = self.get_member("RotationDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_drive.setter
    def rotation_drive(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the RotationDrive reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RotationDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RotationDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def run_after_final_pose_update(self) -> primitives.Bool | None:
        """The RunAfterFinalPoseUpdate field value."""
        member = self.get_member("RunAfterFinalPoseUpdate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @run_after_final_pose_update.setter
    def run_after_final_pose_update(self, value: primitives.Bool) -> None:
        """Set the RunAfterFinalPoseUpdate field value."""
        member = self.get_member("RunAfterFinalPoseUpdate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RunAfterFinalPoseUpdate", fields.FieldBool(value=value)
            )

