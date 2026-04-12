"""Generated component: SmoothTransform."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SmoothTransform(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Smooth transform is a component that is used to create a "lag behind" or "trailing" effect on slots or objects that follow another object. The slot this controls will try to return to it's rest position, iteratively getting closer and closer until in eventuality reaching it's target location at rest.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SmoothTransform"

    def __init__(self, target_position: primitives.Float3 | None = None, target_rotation: primitives.FloatQ | None = None, target_scale: primitives.Float3 | None = None, position: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, scale: str | IField[primitives.Float3] | None = None, smooth_speed: primitives.Float | None = None, update_index: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
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
        """The coordinate space that should be used to check the delta of the transforms in. If set to user space and parented under the user's hand, this slot will only lag behind (or smooth) when the user moves their hand, but not when they walk around. This can also be set to a slot for similar effects without a user."""
        member = self.get_member("InterpolationSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @interpolation_space.setter
    def interpolation_space(self, value: members.SyncObject) -> None:
        """Set InterpolationSpace. The coordinate space that should be used to check the delta of the transforms in. If set to user space and parented under the user's hand, this slot will only lag behind (or smooth) when the user moves their hand, but not when they walk around. This can also be set to a slot for similar effects without a user."""
        self.set_member("InterpolationSpace", value)

    @property
    def target_position(self) -> primitives.Float3 | None:
        """The local transform position that this slot is trying to get to."""
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
        """the local transform rotation that this slot is trying to get to."""
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
        """The local transform scale that this slot is trying to get to."""
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
        """The position field to drive with the smoothed value (auto filled with the position field of the slot this is on."""
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
        """The rotation field to drive with the smoothed value (auto filled with the rotation field of the slot this is on."""
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
        """The scale field to drive with the smoothed value (auto filled with the scale field of the slot this is on."""
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
    def smooth_speed(self) -> primitives.Float | None:
        """How fast or slow this slot is at catching up to it's target location. Not a set number of seconds since this component iteratively smooths."""
        member = self.get_member("SmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_speed.setter
    def smooth_speed(self, value: primitives.Float) -> None:
        """Set the SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def update_index(self) -> primitives.Int | None:
        """Whether to do this smooth transform before or after other smooth transforms in the same slot hiearchy."""
        member = self.get_member("_updateIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_index.setter
    def update_index(self, value: primitives.Int) -> None:
        """Set the _updateIndex field value."""
        member = self.get_member("_updateIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_updateIndex", fields.FieldInt(value=value)
            )

