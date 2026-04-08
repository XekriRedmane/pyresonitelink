"""Generated component: AutoLookAtUser."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AutoLookAtUser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AutoLookAtUser.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AutoLookAtUser"

    def __init__(self, retarget_distance: np.float32 | None = None, lerp_speed: np.float32 | None = None, targeted_user: str | User | None = None, auto_target: bool | None = None, exclude_active_user: bool | None = None, swing_reference: primitives.Float3 | None = None, twist_reference: primitives.Float3 | None = None, max_swing: np.float32 | None = None, max_twist: np.float32 | None = None, rotation: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            retarget_distance: Initial value for RetargetDistance.
            lerp_speed: Initial value for LerpSpeed.
            targeted_user: Initial value for TargetedUser.
            auto_target: Initial value for AutoTarget.
            exclude_active_user: Initial value for ExcludeActiveUser.
            swing_reference: Initial value for SwingReference.
            twist_reference: Initial value for TwistReference.
            max_swing: Initial value for MaxSwing.
            max_twist: Initial value for MaxTwist.
            rotation: Initial value for _rotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if retarget_distance is not None:
            self.retarget_distance = retarget_distance
        if lerp_speed is not None:
            self.lerp_speed = lerp_speed
        if targeted_user is not None:
            self.targeted_user = targeted_user
        if auto_target is not None:
            self.auto_target = auto_target
        if exclude_active_user is not None:
            self.exclude_active_user = exclude_active_user
        if swing_reference is not None:
            self.swing_reference = swing_reference
        if twist_reference is not None:
            self.twist_reference = twist_reference
        if max_swing is not None:
            self.max_swing = max_swing
        if max_twist is not None:
            self.max_twist = max_twist
        if rotation is not None:
            self.rotation = rotation

    @property
    def retarget_distance(self) -> np.float32 | None:
        """The RetargetDistance field value."""
        member = self.get_member("RetargetDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @retarget_distance.setter
    def retarget_distance(self, value: np.float32) -> None:
        """Set the RetargetDistance field value."""
        member = self.get_member("RetargetDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RetargetDistance", fields.FieldFloat(value=value)
            )

    @property
    def lerp_speed(self) -> np.float32 | None:
        """The LerpSpeed field value."""
        member = self.get_member("LerpSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_speed.setter
    def lerp_speed(self, value: np.float32) -> None:
        """Set the LerpSpeed field value."""
        member = self.get_member("LerpSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpSpeed", fields.FieldFloat(value=value)
            )

    @property
    def targeted_user(self) -> str | None:
        """Target ID of the TargetedUser reference (targets User)."""
        member = self.get_member("TargetedUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @targeted_user.setter
    def targeted_user(self, target: str | User | None) -> None:
        """Set the TargetedUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("TargetedUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetedUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def auto_target(self) -> bool | None:
        """The AutoTarget field value."""
        member = self.get_member("AutoTarget")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_target.setter
    def auto_target(self, value: bool) -> None:
        """Set the AutoTarget field value."""
        member = self.get_member("AutoTarget")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoTarget", fields.FieldBool(value=value)
            )

    @property
    def exclude_active_user(self) -> bool | None:
        """The ExcludeActiveUser field value."""
        member = self.get_member("ExcludeActiveUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_active_user.setter
    def exclude_active_user(self, value: bool) -> None:
        """Set the ExcludeActiveUser field value."""
        member = self.get_member("ExcludeActiveUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludeActiveUser", fields.FieldBool(value=value)
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
    def rotation(self) -> str | None:
        """Target ID of the _rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation.setter
    def rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

