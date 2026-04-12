"""Generated component: EyeTrackingStreamManager."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.ieye_data_source_component import IEyeDataSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EyeTrackingStreamManager(GeneratedComponent, IEyeDataSourceComponent, IWorldEventReceiver):
    """The EyeTrackingStreamManager component uses streaming data from the ValueStream data type (seen in the user Inspector) to control the left and right eyes on a user's avatar.

    Category: Users

    Used for Eye Tracking.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EyeTrackingStreamManager"

    def __init__(self, user: str | User | None = None, convergence_distance: str | ValueStream[primitives.Float] | None = None, is_eye_tracking_active: str | ValueStream[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            convergence_distance: Initial value for ConvergenceDistance.
            is_eye_tracking_active: Initial value for IsEyeTrackingActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if convergence_distance is not None:
            self.convergence_distance = convergence_distance
        if is_eye_tracking_active is not None:
            self.is_eye_tracking_active = is_eye_tracking_active

    @property
    def user(self) -> str | None:
        """The focused user to get streaming data from."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | User | None) -> None:
        """Set the User reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def convergence_distance(self) -> str | None:
        """The eye distance data from the headset."""
        member = self.get_member("ConvergenceDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @convergence_distance.setter
    def convergence_distance(self, target: str | ValueStream[primitives.Float] | None) -> None:
        """Set the ConvergenceDistance reference by target ID or ValueStream[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("ConvergenceDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConvergenceDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def is_eye_tracking_active(self) -> str | None:
        """Returns true if the eyes are being tracked from the headset."""
        member = self.get_member("IsEyeTrackingActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_eye_tracking_active.setter
    def is_eye_tracking_active(self, target: str | ValueStream[primitives.Bool] | None) -> None:
        """Set the IsEyeTrackingActive reference by target ID or ValueStream[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("IsEyeTrackingActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsEyeTrackingActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def left_eye_streams(self) -> members.SyncObject | None:
        """A set of fields for the left eye."""
        member = self.get_member("LeftEyeStreams")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @left_eye_streams.setter
    def left_eye_streams(self, value: members.SyncObject) -> None:
        """Set LeftEyeStreams. A set of fields for the left eye."""
        self.set_member("LeftEyeStreams", value)

    @property
    def right_eye_streams(self) -> members.SyncObject | None:
        """A set of fields for the right eye."""
        member = self.get_member("RightEyeStreams")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @right_eye_streams.setter
    def right_eye_streams(self, value: members.SyncObject) -> None:
        """Set RightEyeStreams. A set of fields for the right eye."""
        self.set_member("RightEyeStreams", value)

