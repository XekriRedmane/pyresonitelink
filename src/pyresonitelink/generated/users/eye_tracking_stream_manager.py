"""Generated component: EyeTrackingStreamManager."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.ieye_data_source_component import IEyeDataSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EyeTrackingStreamManager(GeneratedComponent, IEyeDataSourceComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.EyeTrackingStreamManager.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EyeTrackingStreamManager"

    def __init__(self, user: str | User | None = None, convergence_distance: str | ValueStream[np.float32] | None = None, is_eye_tracking_active: str | ValueStream[bool] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the User reference (targets User)."""
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
        """Target ID of the ConvergenceDistance reference (targets ValueStream[np.float32])."""
        member = self.get_member("ConvergenceDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @convergence_distance.setter
    def convergence_distance(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the ConvergenceDistance reference by target ID or ValueStream[np.float32] instance."""
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
        """Target ID of the IsEyeTrackingActive reference (targets ValueStream[bool])."""
        member = self.get_member("IsEyeTrackingActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_eye_tracking_active.setter
    def is_eye_tracking_active(self, target: str | ValueStream[bool] | None) -> None:
        """Set the IsEyeTrackingActive reference by target ID or ValueStream[bool] instance."""
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
        """The LeftEyeStreams member."""
        member = self.get_member("LeftEyeStreams")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @left_eye_streams.setter
    def left_eye_streams(self, value: members.SyncObject) -> None:
        """Set the LeftEyeStreams member."""
        self.set_member("LeftEyeStreams", value)

    @property
    def right_eye_streams(self) -> members.SyncObject | None:
        """The RightEyeStreams member."""
        member = self.get_member("RightEyeStreams")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @right_eye_streams.setter
    def right_eye_streams(self, value: members.SyncObject) -> None:
        """Set the RightEyeStreams member."""
        self.set_member("RightEyeStreams", value)

