"""Generated component: TrigonometricIK."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrigonometricIK(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Added somewhere around: 2026.6.xx (Can't find in mention in devlog. Was added to Locale here )

Used for elbows and knees on Humanid rigs, where there is exactly one solution to the IK solve. The final version is also likely to include constraints.

It can also be used for things like robotic arms or jointed segments.

https://en.wikipedia.org/wiki/Inverse_kinematics

    Category: Transform/Inverse Kinematics

    **Video**: KhIYD_5jM4M
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrigonometricIK"

    def __init__(self, target_effector: str | Slot | None = None, bend_effector: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_effector: Initial value for TargetEffector.
            bend_effector: Initial value for BendEffector.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_effector is not None:
            self.target_effector = target_effector
        if bend_effector is not None:
            self.bend_effector = bend_effector

    @property
    def target_effector(self) -> str | None:
        """Target ID of the TargetEffector reference (targets Slot)."""
        member = self.get_member("TargetEffector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_effector.setter
    def target_effector(self, target: str | Slot | None) -> None:
        """Set the TargetEffector reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("TargetEffector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetEffector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def bend_effector(self) -> str | None:
        """Target ID of the BendEffector reference (targets Slot)."""
        member = self.get_member("BendEffector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bend_effector.setter
    def bend_effector(self, target: str | Slot | None) -> None:
        """Set the BendEffector reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("BendEffector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BendEffector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def base_bone(self) -> members.SyncObject | None:
        """The BaseBone member."""
        member = self.get_member("BaseBone")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @base_bone.setter
    def base_bone(self, value: members.SyncObject) -> None:
        """Set the BaseBone member."""
        self.set_member("BaseBone", value)

    @property
    def mid_bone(self) -> members.SyncObject | None:
        """The MidBone member."""
        member = self.get_member("MidBone")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @mid_bone.setter
    def mid_bone(self, value: members.SyncObject) -> None:
        """Set the MidBone member."""
        self.set_member("MidBone", value)

    @property
    def end_bone(self) -> members.SyncObject | None:
        """The EndBone member."""
        member = self.get_member("EndBone")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @end_bone.setter
    def end_bone(self, value: members.SyncObject) -> None:
        """Set the EndBone member."""
        self.set_member("EndBone", value)

