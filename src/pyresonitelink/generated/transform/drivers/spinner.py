"""Generated component: Spinner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Spinner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Spinner component is used to make something rotate on 1 or more axis at a constant rate.

    Category: Transform/Drivers

    Note: While this component works very well for fixed or discrete speed
    steps, it might not behave as expected when the speed field is
    continuously changing, even a very small change can cause the component
    to 'jerk' on each change. If you want to make something speed up or slow
    down smoothly, one option is to use rotational maths to recreate this
    component in flux, for example using AxisAngle
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Spinner"

    def __init__(self, range_: primitives.Float3 | None = None, target: str | IField[primitives.FloatQ] | None = None, offset: primitives.FloatQ | None = None, speed: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            range_: Initial value for Range.
            target: Initial value for _target.
            offset: Initial value for _offset.
            speed: Initial value for _speed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if range_ is not None:
            self.range_ = range_
        if target is not None:
            self.target = target
        if offset is not None:
            self.offset = offset
        if speed is not None:
            self.speed = speed

    @property
    def range_(self) -> primitives.Float3 | None:
        """how much each axis can go up to from 0 before wrapping around."""
        member = self.get_member("Range")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_.setter
    def range_(self, value: primitives.Float3) -> None:
        """Set the Range field value."""
        member = self.get_member("Range")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Range", fields.FieldFloat3(value=value)
            )

    @property
    def target(self) -> str | None:
        """The rotation field to spin."""
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

    @property
    def offset(self) -> primitives.FloatQ | None:
        """the offset rotation to start at world start from."""
        member = self.get_member("_offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.FloatQ) -> None:
        """Set the _offset field value."""
        member = self.get_member("_offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_offset", fields.FieldFloatQ(value=value)
            )

    @property
    def speed(self) -> primitives.Float3 | None:
        """how fast to rotate on each axis, in Degrees per Second. Negative values go in reverse."""
        member = self.get_member("_speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: primitives.Float3) -> None:
        """Set the _speed field value."""
        member = self.get_member("_speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_speed", fields.FieldFloat3(value=value)
            )

