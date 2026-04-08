"""Generated component: AvatarRawEyeData."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarRawEyeData(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarRawEyeData.

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarRawEyeData"

    def __init__(self, convergence_distance: primitives.Float | None = None, timestamp: primitives.Double | None = None, active_user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            convergence_distance: Initial value for ConvergenceDistance.
            timestamp: Initial value for Timestamp.
            active_user: Initial value for _activeUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if convergence_distance is not None:
            self.convergence_distance = convergence_distance
        if timestamp is not None:
            self.timestamp = timestamp
        if active_user is not None:
            self.active_user = active_user

    @property
    def left_eye(self) -> members.SyncObject | None:
        """The LeftEye member."""
        member = self.get_member("LeftEye")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @left_eye.setter
    def left_eye(self, value: members.SyncObject) -> None:
        """Set the LeftEye member."""
        self.set_member("LeftEye", value)

    @property
    def right_eye(self) -> members.SyncObject | None:
        """The RightEye member."""
        member = self.get_member("RightEye")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @right_eye.setter
    def right_eye(self, value: members.SyncObject) -> None:
        """Set the RightEye member."""
        self.set_member("RightEye", value)

    @property
    def combined_eye(self) -> members.SyncObject | None:
        """The CombinedEye member."""
        member = self.get_member("CombinedEye")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @combined_eye.setter
    def combined_eye(self, value: members.SyncObject) -> None:
        """Set the CombinedEye member."""
        self.set_member("CombinedEye", value)

    @property
    def convergence_distance(self) -> primitives.Float | None:
        """The ConvergenceDistance field value."""
        member = self.get_member("ConvergenceDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @convergence_distance.setter
    def convergence_distance(self, value: primitives.Float) -> None:
        """Set the ConvergenceDistance field value."""
        member = self.get_member("ConvergenceDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ConvergenceDistance", fields.FieldFloat(value=value)
            )

    @property
    def timestamp(self) -> primitives.Double | None:
        """The Timestamp field value."""
        member = self.get_member("Timestamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timestamp.setter
    def timestamp(self, value: primitives.Double) -> None:
        """Set the Timestamp field value."""
        member = self.get_member("Timestamp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Timestamp", fields.FieldDouble(value=value)
            )

    @property
    def active_user(self) -> str | None:
        """Target ID of the _activeUser reference (targets User)."""
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_user.setter
    def active_user(self, target: str | User | None) -> None:
        """Set the _activeUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

