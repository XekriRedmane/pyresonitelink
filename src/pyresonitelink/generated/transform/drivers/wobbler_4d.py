"""Generated component: Wobbler4D."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Wobbler4D(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Wobbler4D component can be used to make a value randomly change in a smooth fashion.

    Category: Transform/Drivers

    * Wobble things with the Wobbler by ProbablePrime
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Wobbler4D"

    def __init__(self, target: str | IField[primitives.Float4] | None = None, offset: primitives.Float4 | None = None, speed: primitives.Float4 | None = None, magnitude: primitives.Float4 | None = None, seed: primitives.Float4 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            offset: Initial value for Offset.
            speed: Initial value for Speed.
            magnitude: Initial value for Magnitude.
            seed: Initial value for Seed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if offset is not None:
            self.offset = offset
        if speed is not None:
            self.speed = speed
        if magnitude is not None:
            self.magnitude = magnitude
        if seed is not None:
            self.seed = seed

    @property
    def target(self) -> str | None:
        """The field to wobble."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float4] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float4>'),
            )

    @property
    def offset(self) -> primitives.Float4 | None:
        """The starting point of the wobble."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float4) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat4(value=value)
            )

    @property
    def speed(self) -> primitives.Float4 | None:
        """how fast to wobble."""
        member = self.get_member("Speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: primitives.Float4) -> None:
        """Set the Speed field value."""
        member = self.get_member("Speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Speed", fields.FieldFloat4(value=value)
            )

    @property
    def magnitude(self) -> primitives.Float4 | None:
        """the amount to wobble from ``Offset``"""
        member = self.get_member("Magnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @magnitude.setter
    def magnitude(self, value: primitives.Float4) -> None:
        """Set the Magnitude field value."""
        member = self.get_member("Magnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Magnitude", fields.FieldFloat4(value=value)
            )

    @property
    def seed(self) -> primitives.Float4 | None:
        """the value to use as a seed for the randomness."""
        member = self.get_member("Seed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seed.setter
    def seed(self, value: primitives.Float4) -> None:
        """Set the Seed field value."""
        member = self.get_member("Seed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Seed", fields.FieldFloat4(value=value)
            )

