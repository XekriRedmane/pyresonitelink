"""Generated component: FingerPoseStreamManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.multi_value_stream import MultiValueStream
from pyresonitelink.generated._types.user_pose_controller import UserPoseController
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPoseStreamManager(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FingerPoseStreamManager.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerPoseStreamManager"

    def __init__(self, user: str | User | None = None, left_is_tracking: str | ValueStream[primitives.Bool] | None = None, right_is_tracking: str | ValueStream[primitives.Bool] | None = None, stream: str | MultiValueStream[primitives.FloatQ] | None = None, tracks_metacarpals: primitives.Bool | None = None, pose_controller: str | UserPoseController | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            left_is_tracking: Initial value for LeftIsTracking.
            right_is_tracking: Initial value for RightIsTracking.
            stream: Initial value for Stream.
            tracks_metacarpals: Initial value for TracksMetacarpals.
            pose_controller: Initial value for PoseController.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if left_is_tracking is not None:
            self.left_is_tracking = left_is_tracking
        if right_is_tracking is not None:
            self.right_is_tracking = right_is_tracking
        if stream is not None:
            self.stream = stream
        if tracks_metacarpals is not None:
            self.tracks_metacarpals = tracks_metacarpals
        if pose_controller is not None:
            self.pose_controller = pose_controller

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
    def left_is_tracking(self) -> str | None:
        """Target ID of the LeftIsTracking reference (targets ValueStream[primitives.Bool])."""
        member = self.get_member("LeftIsTracking")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_is_tracking.setter
    def left_is_tracking(self, target: str | ValueStream[primitives.Bool] | None) -> None:
        """Set the LeftIsTracking reference by target ID or ValueStream[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LeftIsTracking")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LeftIsTracking",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def right_is_tracking(self) -> str | None:
        """Target ID of the RightIsTracking reference (targets ValueStream[primitives.Bool])."""
        member = self.get_member("RightIsTracking")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_is_tracking.setter
    def right_is_tracking(self, target: str | ValueStream[primitives.Bool] | None) -> None:
        """Set the RightIsTracking reference by target ID or ValueStream[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("RightIsTracking")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RightIsTracking",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def stream(self) -> str | None:
        """Target ID of the Stream reference (targets MultiValueStream[primitives.FloatQ])."""
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream.setter
    def stream(self, target: str | MultiValueStream[primitives.FloatQ] | None) -> None:
        """Set the Stream reference by target ID or MultiValueStream[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, MultiValueStream) else target  # type: ignore[assignment]
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MultiValueStream<floatQ>'),
            )

    @property
    def tracks_metacarpals(self) -> primitives.Bool | None:
        """The TracksMetacarpals field value."""
        member = self.get_member("TracksMetacarpals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tracks_metacarpals.setter
    def tracks_metacarpals(self, value: primitives.Bool) -> None:
        """Set the TracksMetacarpals field value."""
        member = self.get_member("TracksMetacarpals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TracksMetacarpals", fields.FieldBool(value=value)
            )

    @property
    def pose_controller(self) -> str | None:
        """Target ID of the PoseController reference (targets UserPoseController)."""
        member = self.get_member("PoseController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pose_controller.setter
    def pose_controller(self, target: str | UserPoseController | None) -> None:
        """Set the PoseController reference by target ID or UserPoseController instance."""
        target_id: str | None = target.id if isinstance(target, UserPoseController) else target  # type: ignore[assignment]
        member = self.get_member("PoseController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PoseController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserPoseController'),
            )

