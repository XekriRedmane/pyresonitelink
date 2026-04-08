"""Generated component: AvatarFingerPoseInfo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarFingerPoseInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarFingerPoseInfo.

    Category: Users/Common Avatar System/Fingers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarFingerPoseInfo"

    def __init__(self, finger_pose_source: str | IFingerPoseSourceComponent | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            finger_pose_source: Initial value for FingerPoseSource.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if finger_pose_source is not None:
            self.finger_pose_source = finger_pose_source

    @property
    def finger_pose_source(self) -> str | None:
        """Target ID of the FingerPoseSource reference (targets IFingerPoseSourceComponent)."""
        member = self.get_member("FingerPoseSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @finger_pose_source.setter
    def finger_pose_source(self, target: str | IFingerPoseSourceComponent | None) -> None:
        """Set the FingerPoseSource reference by target ID or IFingerPoseSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IFingerPoseSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("FingerPoseSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FingerPoseSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFingerPoseSourceComponent'),
            )

