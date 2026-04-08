"""Generated component: AvatarPoseBoxConstraint."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_pose_filter import IAvatarPoseFilter
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarPoseBoxConstraint(GeneratedComponent, IAvatarPoseFilter, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseBoxConstraint.

    Category: Users/Common Avatar System/Pose Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseBoxConstraint"

    def __init__(self, box_size: primitives.Float3 | None = None, default_pose_reference: str | Slot | None = None, process_simulated_poses: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            box_size: Initial value for BoxSize.
            default_pose_reference: Initial value for DefaultPoseReference.
            process_simulated_poses: Initial value for ProcessSimulatedPoses.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if box_size is not None:
            self.box_size = box_size
        if default_pose_reference is not None:
            self.default_pose_reference = default_pose_reference
        if process_simulated_poses is not None:
            self.process_simulated_poses = process_simulated_poses

    @property
    def box_size(self) -> primitives.Float3 | None:
        """The BoxSize field value."""
        member = self.get_member("BoxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @box_size.setter
    def box_size(self, value: primitives.Float3) -> None:
        """Set the BoxSize field value."""
        member = self.get_member("BoxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BoxSize", fields.FieldFloat3(value=value)
            )

    @property
    def default_pose_reference(self) -> str | None:
        """Target ID of the DefaultPoseReference reference (targets Slot)."""
        member = self.get_member("DefaultPoseReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_pose_reference.setter
    def default_pose_reference(self, target: str | Slot | None) -> None:
        """Set the DefaultPoseReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("DefaultPoseReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultPoseReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def process_simulated_poses(self) -> bool | None:
        """The ProcessSimulatedPoses field value."""
        member = self.get_member("ProcessSimulatedPoses")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_simulated_poses.setter
    def process_simulated_poses(self, value: bool) -> None:
        """Set the ProcessSimulatedPoses field value."""
        member = self.get_member("ProcessSimulatedPoses")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessSimulatedPoses", fields.FieldBool(value=value)
            )

