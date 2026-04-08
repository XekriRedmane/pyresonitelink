"""Generated component: LookAt."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LookAt(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LookAt.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LookAt"

    def __init__(self, target: str | Slot | None = None, target_point: primitives.Float3 | None = None, up: primitives.Float3 | None = None, rotation_offset: primitives.FloatQ | None = None, swing_reference: primitives.Float3 | None = None, twist_reference: primitives.Float3 | None = None, max_swing: np.float32 | None = None, max_twist: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            target_point: Initial value for TargetPoint.
            up: Initial value for Up.
            rotation_offset: Initial value for RotationOffset.
            swing_reference: Initial value for SwingReference.
            twist_reference: Initial value for TwistReference.
            max_swing: Initial value for MaxSwing.
            max_twist: Initial value for MaxTwist.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if target_point is not None:
            self.target_point = target_point
        if up is not None:
            self.up = up
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset
        if swing_reference is not None:
            self.swing_reference = swing_reference
        if twist_reference is not None:
            self.twist_reference = twist_reference
        if max_swing is not None:
            self.max_swing = max_swing
        if max_twist is not None:
            self.max_twist = max_twist

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets Slot)."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | Slot | None) -> None:
        """Set the Target reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target_point(self) -> primitives.Float3 | None:
        """The TargetPoint field value."""
        member = self.get_member("TargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_point.setter
    def target_point(self, value: primitives.Float3) -> None:
        """Set the TargetPoint field value."""
        member = self.get_member("TargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def target_point_space(self) -> members.SyncObject | None:
        """The TargetPointSpace member."""
        member = self.get_member("TargetPointSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_point_space.setter
    def target_point_space(self, value: members.SyncObject) -> None:
        """Set the TargetPointSpace member."""
        self.set_member("TargetPointSpace", value)

    @property
    def up(self) -> primitives.Float3 | None:
        """The Up field value."""
        member = self.get_member("Up")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @up.setter
    def up(self, value: primitives.Float3) -> None:
        """Set the Up field value."""
        member = self.get_member("Up")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Up", fields.FieldFloat3(value=value)
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
    def swing_reference(self) -> primitives.Float3 | None:
        """The SwingReference field value."""
        member = self.get_member("SwingReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @swing_reference.setter
    def swing_reference(self, value: primitives.Float3) -> None:
        """Set the SwingReference field value."""
        member = self.get_member("SwingReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SwingReference", fields.FieldFloat3(value=value)
            )

    @property
    def twist_reference(self) -> primitives.Float3 | None:
        """The TwistReference field value."""
        member = self.get_member("TwistReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @twist_reference.setter
    def twist_reference(self, value: primitives.Float3) -> None:
        """Set the TwistReference field value."""
        member = self.get_member("TwistReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TwistReference", fields.FieldFloat3(value=value)
            )

    @property
    def max_swing(self) -> np.float32 | None:
        """The MaxSwing field value."""
        member = self.get_member("MaxSwing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_swing.setter
    def max_swing(self, value: np.float32) -> None:
        """Set the MaxSwing field value."""
        member = self.get_member("MaxSwing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSwing", fields.FieldFloat(value=value)
            )

    @property
    def max_twist(self) -> np.float32 | None:
        """The MaxTwist field value."""
        member = self.get_member("MaxTwist")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_twist.setter
    def max_twist(self, value: np.float32) -> None:
        """Set the MaxTwist field value."""
        member = self.get_member("MaxTwist")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTwist", fields.FieldFloat(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the _target reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _target reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

