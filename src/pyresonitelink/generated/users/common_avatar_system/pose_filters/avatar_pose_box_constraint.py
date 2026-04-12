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
    """The AvatarPoseBoxConstraint component is a BodyPoseFilter that can be used in the construction of tool tips, anchors, grabbable items, and more. This pose filter is used to force the slot corresponding to a body node (In the case of a hand for example, it will constrict the position of the hand bone position, rather than the whole hand) to stay within a rotatable box specified.

    Category: Users/Common Avatar System/Pose Filters

    This is widely used in seats where the user's legs and hips are posed in
    a sitting position, like when sitting in a car.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseBoxConstraint"

    def __init__(self, box_size: primitives.Float3 | None = None, default_pose_reference: str | Slot | None = None, process_simulated_poses: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """the size of the box that a user's body node should be constrained within. (0,0,0) is valid for this field."""
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
        """the slot which the box will be positioned, rotated, and scaled by. If null, this is the slot this component is on."""
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
    def process_simulated_poses(self) -> primitives.Bool | None:
        """Whether to affect simulated poses like from the animation system."""
        member = self.get_member("ProcessSimulatedPoses")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_simulated_poses.setter
    def process_simulated_poses(self, value: primitives.Bool) -> None:
        """Set the ProcessSimulatedPoses field value."""
        member = self.get_member("ProcessSimulatedPoses")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessSimulatedPoses", fields.FieldBool(value=value)
            )

