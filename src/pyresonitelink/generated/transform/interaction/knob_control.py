"""Generated component: KnobControl."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class KnobControl(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.KnobControl.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.KnobControl"

    def __init__(self, target: str | IField[np.float32] | None = None, rotation_axis: primitives.Float3 | None = None, rate: np.float32 | None = None, min: np.float32 | None = None, max: np.float32 | None = None, last_rotation: np.float32 | None = None, last_axis: primitives.Float3 | None = None, last_user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            rotation_axis: Initial value for RotationAxis.
            rate: Initial value for Rate.
            min: Initial value for Min.
            max: Initial value for Max.
            last_rotation: Initial value for _lastRotation.
            last_axis: Initial value for _lastAxis.
            last_user: Initial value for _lastUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if rotation_axis is not None:
            self.rotation_axis = rotation_axis
        if rate is not None:
            self.rate = rate
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if last_rotation is not None:
            self.last_rotation = last_rotation
        if last_axis is not None:
            self.last_axis = last_axis
        if last_user is not None:
            self.last_user = last_user

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[np.float32])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[np.float32] | None) -> None:
        """Set the Target reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def rotation_axis(self) -> primitives.Float3 | None:
        """The RotationAxis field value."""
        member = self.get_member("RotationAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_axis.setter
    def rotation_axis(self, value: primitives.Float3) -> None:
        """Set the RotationAxis field value."""
        member = self.get_member("RotationAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationAxis", fields.FieldFloat3(value=value)
            )

    @property
    def rate(self) -> np.float32 | None:
        """The Rate field value."""
        member = self.get_member("Rate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rate.setter
    def rate(self, value: np.float32) -> None:
        """Set the Rate field value."""
        member = self.get_member("Rate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rate", fields.FieldFloat(value=value)
            )

    @property
    def min(self) -> np.float32 | None:
        """The Min field value."""
        member = self.get_member("Min")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min.setter
    def min(self, value: np.float32) -> None:
        """Set the Min field value."""
        member = self.get_member("Min")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Min", fields.FieldFloat(value=value)
            )

    @property
    def max(self) -> np.float32 | None:
        """The Max field value."""
        member = self.get_member("Max")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max.setter
    def max(self, value: np.float32) -> None:
        """Set the Max field value."""
        member = self.get_member("Max")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Max", fields.FieldFloat(value=value)
            )

    @property
    def last_rotation(self) -> np.float32 | None:
        """The _lastRotation field value."""
        member = self.get_member("_lastRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_rotation.setter
    def last_rotation(self, value: np.float32) -> None:
        """Set the _lastRotation field value."""
        member = self.get_member("_lastRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastRotation", fields.FieldFloat(value=value)
            )

    @property
    def last_axis(self) -> primitives.Float3 | None:
        """The _lastAxis field value."""
        member = self.get_member("_lastAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_axis.setter
    def last_axis(self, value: primitives.Float3) -> None:
        """Set the _lastAxis field value."""
        member = self.get_member("_lastAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastAxis", fields.FieldFloat3(value=value)
            )

    @property
    def last_user(self) -> str | None:
        """Target ID of the _lastUser reference (targets User)."""
        member = self.get_member("_lastUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_user.setter
    def last_user(self, target: str | User | None) -> None:
        """Set the _lastUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_lastUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

