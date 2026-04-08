"""Generated component: SmoothTransform."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SmoothTransform(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SmoothTransform.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SmoothTransform"

    def __init__(self, target_position: primitives.Float3 | None = None, target_rotation: primitives.FloatQ | None = None, target_scale: primitives.Float3 | None = None, position: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, scale: str | IField[primitives.Float3] | None = None, smooth_speed: np.float32 | None = None, update_index: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_position: Initial value for TargetPosition.
            target_rotation: Initial value for TargetRotation.
            target_scale: Initial value for TargetScale.
            position: Initial value for Position.
            rotation: Initial value for Rotation.
            scale: Initial value for Scale.
            smooth_speed: Initial value for SmoothSpeed.
            update_index: Initial value for _updateIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_position is not None:
            self.target_position = target_position
        if target_rotation is not None:
            self.target_rotation = target_rotation
        if target_scale is not None:
            self.target_scale = target_scale
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if scale is not None:
            self.scale = scale
        if smooth_speed is not None:
            self.smooth_speed = smooth_speed
        if update_index is not None:
            self.update_index = update_index

    @property
    def interpolation_space(self) -> members.SyncObject | None:
        """The InterpolationSpace member."""
        member = self.get_member("InterpolationSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @interpolation_space.setter
    def interpolation_space(self, value: members.SyncObject) -> None:
        """Set the InterpolationSpace member."""
        self.set_member("InterpolationSpace", value)

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
    def target_scale(self) -> primitives.Float3 | None:
        """The TargetScale field value."""
        member = self.get_member("TargetScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_scale.setter
    def target_scale(self, value: primitives.Float3) -> None:
        """Set the TargetScale field value."""
        member = self.get_member("TargetScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetScale", fields.FieldFloat3(value=value)
            )

    @property
    def position(self) -> str | None:
        """Target ID of the Position reference (targets IField[primitives.Float3])."""
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rotation(self) -> str | None:
        """Target ID of the Rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("Rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation.setter
    def rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the Rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def scale(self) -> str | None:
        """Target ID of the Scale reference (targets IField[primitives.Float3])."""
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Scale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def smooth_speed(self) -> np.float32 | None:
        """The SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_speed.setter
    def smooth_speed(self, value: np.float32) -> None:
        """Set the SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def update_index(self) -> np.int32 | None:
        """The _updateIndex field value."""
        member = self.get_member("_updateIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_index.setter
    def update_index(self, value: np.int32) -> None:
        """Set the _updateIndex field value."""
        member = self.get_member("_updateIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_updateIndex", fields.FieldInt(value=value)
            )

