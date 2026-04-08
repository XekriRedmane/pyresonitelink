"""Generated component: IKDraggableOffset."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ik_solver import IKSolver
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IKDraggableOffset(GeneratedComponent, IGrabbable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FinalIK.IKDraggableOffset.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FinalIK.IKDraggableOffset"

    def __init__(self, solver: str | IKSolver | None = None, position_target: str | Sync[primitives.Float3] | None = None, rotation_target: str | Sync[primitives.FloatQ] | None = None, weight: str | Sync[np.float32] | None = None, grabber: str | Grabber | None = None, grabbing_user: str | User | None = None, hold_slot: str | Slot | None = None, pos_offset: primitives.Float3 | None = None, rot_offset: primitives.FloatQ | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            solver: Initial value for Solver.
            position_target: Initial value for PositionTarget.
            rotation_target: Initial value for RotationTarget.
            weight: Initial value for Weight.
            grabber: Initial value for _grabber.
            grabbing_user: Initial value for _grabbingUser.
            hold_slot: Initial value for _holdSlot.
            pos_offset: Initial value for _posOffset.
            rot_offset: Initial value for _rotOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if solver is not None:
            self.solver = solver
        if position_target is not None:
            self.position_target = position_target
        if rotation_target is not None:
            self.rotation_target = rotation_target
        if weight is not None:
            self.weight = weight
        if grabber is not None:
            self.grabber = grabber
        if grabbing_user is not None:
            self.grabbing_user = grabbing_user
        if hold_slot is not None:
            self.hold_slot = hold_slot
        if pos_offset is not None:
            self.pos_offset = pos_offset
        if rot_offset is not None:
            self.rot_offset = rot_offset

    @property
    def solver(self) -> str | None:
        """Target ID of the Solver reference (targets IKSolver)."""
        member = self.get_member("Solver")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @solver.setter
    def solver(self, target: str | IKSolver | None) -> None:
        """Set the Solver reference by target ID or IKSolver instance."""
        target_id: str | None = target.id if isinstance(target, IKSolver) else target  # type: ignore[assignment]
        member = self.get_member("Solver")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Solver",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FinalIK.IKSolver'),
            )

    @property
    def position_target(self) -> str | None:
        """Target ID of the PositionTarget reference (targets Sync[primitives.Float3])."""
        member = self.get_member("PositionTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_target.setter
    def position_target(self, target: str | Sync[primitives.Float3] | None) -> None:
        """Set the PositionTarget reference by target ID or Sync[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("PositionTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PositionTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float3>'),
            )

    @property
    def rotation_target(self) -> str | None:
        """Target ID of the RotationTarget reference (targets Sync[primitives.FloatQ])."""
        member = self.get_member("RotationTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_target.setter
    def rotation_target(self, target: str | Sync[primitives.FloatQ] | None) -> None:
        """Set the RotationTarget reference by target ID or Sync[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("RotationTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RotationTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<floatQ>'),
            )

    @property
    def weight(self) -> str | None:
        """Target ID of the Weight reference (targets Sync[np.float32])."""
        member = self.get_member("Weight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @weight.setter
    def weight(self, target: str | Sync[np.float32] | None) -> None:
        """Set the Weight reference by target ID or Sync[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("Weight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Weight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float>'),
            )

    @property
    def grabber(self) -> str | None:
        """Target ID of the _grabber reference (targets Grabber)."""
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabber.setter
    def grabber(self, target: str | Grabber | None) -> None:
        """Set the _grabber reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

    @property
    def grabbing_user(self) -> str | None:
        """Target ID of the _grabbingUser reference (targets User)."""
        member = self.get_member("_grabbingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabbing_user.setter
    def grabbing_user(self, target: str | User | None) -> None:
        """Set the _grabbingUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_grabbingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabbingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def hold_slot(self) -> str | None:
        """Target ID of the _holdSlot reference (targets Slot)."""
        member = self.get_member("_holdSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hold_slot.setter
    def hold_slot(self, target: str | Slot | None) -> None:
        """Set the _holdSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_holdSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_holdSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def pos_offset(self) -> primitives.Float3 | None:
        """The _posOffset field value."""
        member = self.get_member("_posOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_offset.setter
    def pos_offset(self, value: primitives.Float3) -> None:
        """Set the _posOffset field value."""
        member = self.get_member("_posOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_posOffset", fields.FieldFloat3(value=value)
            )

    @property
    def rot_offset(self) -> primitives.FloatQ | None:
        """The _rotOffset field value."""
        member = self.get_member("_rotOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rot_offset.setter
    def rot_offset(self, value: primitives.FloatQ) -> None:
        """Set the _rotOffset field value."""
        member = self.get_member("_rotOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rotOffset", fields.FieldFloatQ(value=value)
            )

