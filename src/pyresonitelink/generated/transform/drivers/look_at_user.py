"""Generated component: LookAtUser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LookAtUser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LookAtUser.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LookAtUser"

    def __init__(self, target_user: str | User | None = None, target_at_local_user: primitives.Bool | None = None, source_position_offset: primitives.Float3 | None = None, invert: primitives.Bool | None = None, rotation_offset: primitives.FloatQ | None = None, around_axis: primitives.Bool | None = None, axis: primitives.Float3 | None = None, rotation_drive: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_user: Initial value for TargetUser.
            target_at_local_user: Initial value for TargetAtLocalUser.
            source_position_offset: Initial value for SourcePositionOffset.
            invert: Initial value for Invert.
            rotation_offset: Initial value for RotationOffset.
            around_axis: Initial value for AroundAxis.
            axis: Initial value for Axis.
            rotation_drive: Initial value for _rotationDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_user is not None:
            self.target_user = target_user
        if target_at_local_user is not None:
            self.target_at_local_user = target_at_local_user
        if source_position_offset is not None:
            self.source_position_offset = source_position_offset
        if invert is not None:
            self.invert = invert
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset
        if around_axis is not None:
            self.around_axis = around_axis
        if axis is not None:
            self.axis = axis
        if rotation_drive is not None:
            self.rotation_drive = rotation_drive

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
    def target_at_local_user(self) -> primitives.Bool | None:
        """The TargetAtLocalUser field value."""
        member = self.get_member("TargetAtLocalUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_at_local_user.setter
    def target_at_local_user(self, value: primitives.Bool) -> None:
        """Set the TargetAtLocalUser field value."""
        member = self.get_member("TargetAtLocalUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetAtLocalUser", fields.FieldBool(value=value)
            )

    @property
    def source_position_offset(self) -> primitives.Float3 | None:
        """The SourcePositionOffset field value."""
        member = self.get_member("SourcePositionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_position_offset.setter
    def source_position_offset(self, value: primitives.Float3) -> None:
        """Set the SourcePositionOffset field value."""
        member = self.get_member("SourcePositionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourcePositionOffset", fields.FieldFloat3(value=value)
            )

    @property
    def invert(self) -> primitives.Bool | None:
        """The Invert field value."""
        member = self.get_member("Invert")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @invert.setter
    def invert(self, value: primitives.Bool) -> None:
        """Set the Invert field value."""
        member = self.get_member("Invert")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Invert", fields.FieldBool(value=value)
            )

    @property
    def rotation_offset(self) -> primitives.FloatQ | None:
        """The RotationOffset field value."""
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
    def position_source(self) -> members.FieldEnum | None:
        """The PositionSource member."""
        member = self.get_member("PositionSource")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @position_source.setter
    def position_source(self, value: members.FieldEnum) -> None:
        """Set the PositionSource member."""
        self.set_member("PositionSource", value)

    @property
    def around_axis(self) -> primitives.Bool | None:
        """The AroundAxis field value."""
        member = self.get_member("AroundAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @around_axis.setter
    def around_axis(self, value: primitives.Bool) -> None:
        """Set the AroundAxis field value."""
        member = self.get_member("AroundAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AroundAxis", fields.FieldBool(value=value)
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
    def rotation_drive(self) -> str | None:
        """Target ID of the _rotationDrive reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_rotationDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_drive.setter
    def rotation_drive(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotationDrive reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotationDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotationDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

