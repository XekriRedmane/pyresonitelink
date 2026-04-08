"""Generated component: UserInterfacePositioner."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserInterfacePositioner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserInterfacePositioner.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserInterfacePositioner"

    def __init__(self, use_head: bool | None = None, rotate_vertical_only: bool | None = None, position_speed: np.float32 | None = None, rotation_speed: np.float32 | None = None, activation_distance: np.float32 | None = None, activation_angle: np.float32 | None = None, deactivation_distance: np.float32 | None = None, deactivation_angle: np.float32 | None = None, target_position: primitives.Float3 | None = None, target_rotation: primitives.FloatQ | None = None, position: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_head: Initial value for UseHead.
            rotate_vertical_only: Initial value for RotateVerticalOnly.
            position_speed: Initial value for PositionSpeed.
            rotation_speed: Initial value for RotationSpeed.
            activation_distance: Initial value for ActivationDistance.
            activation_angle: Initial value for ActivationAngle.
            deactivation_distance: Initial value for DeactivationDistance.
            deactivation_angle: Initial value for DeactivationAngle.
            target_position: Initial value for TargetPosition.
            target_rotation: Initial value for TargetRotation.
            position: Initial value for _position.
            rotation: Initial value for _rotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_head is not None:
            self.use_head = use_head
        if rotate_vertical_only is not None:
            self.rotate_vertical_only = rotate_vertical_only
        if position_speed is not None:
            self.position_speed = position_speed
        if rotation_speed is not None:
            self.rotation_speed = rotation_speed
        if activation_distance is not None:
            self.activation_distance = activation_distance
        if activation_angle is not None:
            self.activation_angle = activation_angle
        if deactivation_distance is not None:
            self.deactivation_distance = deactivation_distance
        if deactivation_angle is not None:
            self.deactivation_angle = deactivation_angle
        if target_position is not None:
            self.target_position = target_position
        if target_rotation is not None:
            self.target_rotation = target_rotation
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation

    @property
    def target_user(self) -> members.SyncObject | None:
        """The TargetUser member."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_user.setter
    def target_user(self, value: members.SyncObject) -> None:
        """Set the TargetUser member."""
        self.set_member("TargetUser", value)

    @property
    def use_head(self) -> bool | None:
        """The UseHead field value."""
        member = self.get_member("UseHead")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_head.setter
    def use_head(self, value: bool) -> None:
        """Set the UseHead field value."""
        member = self.get_member("UseHead")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseHead", fields.FieldBool(value=value)
            )

    @property
    def rotate_vertical_only(self) -> bool | None:
        """The RotateVerticalOnly field value."""
        member = self.get_member("RotateVerticalOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotate_vertical_only.setter
    def rotate_vertical_only(self, value: bool) -> None:
        """Set the RotateVerticalOnly field value."""
        member = self.get_member("RotateVerticalOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotateVerticalOnly", fields.FieldBool(value=value)
            )

    @property
    def position_speed(self) -> np.float32 | None:
        """The PositionSpeed field value."""
        member = self.get_member("PositionSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_speed.setter
    def position_speed(self, value: np.float32) -> None:
        """Set the PositionSpeed field value."""
        member = self.get_member("PositionSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionSpeed", fields.FieldFloat(value=value)
            )

    @property
    def rotation_speed(self) -> np.float32 | None:
        """The RotationSpeed field value."""
        member = self.get_member("RotationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_speed.setter
    def rotation_speed(self, value: np.float32) -> None:
        """Set the RotationSpeed field value."""
        member = self.get_member("RotationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def activation_distance(self) -> np.float32 | None:
        """The ActivationDistance field value."""
        member = self.get_member("ActivationDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activation_distance.setter
    def activation_distance(self, value: np.float32) -> None:
        """Set the ActivationDistance field value."""
        member = self.get_member("ActivationDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivationDistance", fields.FieldFloat(value=value)
            )

    @property
    def activation_angle(self) -> np.float32 | None:
        """The ActivationAngle field value."""
        member = self.get_member("ActivationAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activation_angle.setter
    def activation_angle(self, value: np.float32) -> None:
        """Set the ActivationAngle field value."""
        member = self.get_member("ActivationAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivationAngle", fields.FieldFloat(value=value)
            )

    @property
    def deactivation_distance(self) -> np.float32 | None:
        """The DeactivationDistance field value."""
        member = self.get_member("DeactivationDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @deactivation_distance.setter
    def deactivation_distance(self, value: np.float32) -> None:
        """Set the DeactivationDistance field value."""
        member = self.get_member("DeactivationDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeactivationDistance", fields.FieldFloat(value=value)
            )

    @property
    def deactivation_angle(self) -> np.float32 | None:
        """The DeactivationAngle field value."""
        member = self.get_member("DeactivationAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @deactivation_angle.setter
    def deactivation_angle(self, value: np.float32) -> None:
        """Set the DeactivationAngle field value."""
        member = self.get_member("DeactivationAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeactivationAngle", fields.FieldFloat(value=value)
            )

    @property
    def target_position(self) -> primitives.Float3 | None:
        """The TargetPosition field value."""
        member = self.get_member("TargetPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_position.setter
    def target_position(self, value: primitives.Float3) -> None:
        """Set the TargetPosition field value."""
        member = self.get_member("TargetPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetPosition", fields.FieldFloat3(value=value)
            )

    @property
    def target_rotation(self) -> primitives.FloatQ | None:
        """The TargetRotation field value."""
        member = self.get_member("TargetRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_rotation.setter
    def target_rotation(self, value: primitives.FloatQ) -> None:
        """Set the TargetRotation field value."""
        member = self.get_member("TargetRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def position(self) -> str | None:
        """Target ID of the _position reference (targets IField[primitives.Float3])."""
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
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

