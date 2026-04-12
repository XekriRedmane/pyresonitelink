"""Generated component: AxisRotationAligner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisRotationAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AxisRotationAligner can be used to keep a slot facing a direction relative to a space.

    Category: Transform/Drivers

    The defined ``LocalDirection`` will be rotated to line up with the
    ``TargetDirection`` inside ``DirectionSpace``'s coordinate space.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AxisRotationAligner"

    def __init__(self, local_direction: primitives.Float3 | None = None, target_direction: primitives.Float3 | None = None, local_rotation: primitives.FloatQ | None = None, rotation: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            local_direction: Initial value for LocalDirection.
            target_direction: Initial value for TargetDirection.
            local_rotation: Initial value for LocalRotation.
            rotation: Initial value for _rotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if local_direction is not None:
            self.local_direction = local_direction
        if target_direction is not None:
            self.target_direction = target_direction
        if local_rotation is not None:
            self.local_rotation = local_rotation
        if rotation is not None:
            self.rotation = rotation

    @property
    def local_direction(self) -> primitives.Float3 | None:
        """A vector direction in this slot's local space to align to ``TargetDirection`` via rotating this slot."""
        member = self.get_member("LocalDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_direction.setter
    def local_direction(self, value: primitives.Float3) -> None:
        """Set the LocalDirection field value."""
        member = self.get_member("LocalDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalDirection", fields.FieldFloat3(value=value)
            )

    @property
    def target_direction(self) -> primitives.Float3 | None:
        """The direction vector to align to."""
        member = self.get_member("TargetDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_direction.setter
    def target_direction(self, value: primitives.Float3) -> None:
        """Set the TargetDirection field value."""
        member = self.get_member("TargetDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetDirection", fields.FieldFloat3(value=value)
            )

    @property
    def direction_space(self) -> members.SyncObject | None:
        """The coordinate space that ``TargetDirection`` is in."""
        member = self.get_member("DirectionSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @direction_space.setter
    def direction_space(self, value: members.SyncObject) -> None:
        """Set DirectionSpace. The coordinate space that ``TargetDirection`` is in."""
        self.set_member("DirectionSpace", value)

    @property
    def local_rotation(self) -> primitives.FloatQ | None:
        """A rotation offset to the alignment."""
        member = self.get_member("LocalRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_rotation.setter
    def local_rotation(self, value: primitives.FloatQ) -> None:
        """Set the LocalRotation field value."""
        member = self.get_member("LocalRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def rotation(self) -> str | None:
        """The rotation field of the slot this component is on. Is driven to do the rotation alignment."""
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

