"""Generated component: RandomEventGenerator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RandomEventGenerator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RandomEventGenerator.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RandomEventGenerator"

    def __init__(self, min_interval: primitives.Float | None = None, max_interval: primitives.Float | None = None, random_point_generator: str | IPointGenerator | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_interval: Initial value for MinInterval.
            max_interval: Initial value for MaxInterval.
            random_point_generator: Initial value for RandomPointGenerator.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_interval is not None:
            self.min_interval = min_interval
        if max_interval is not None:
            self.max_interval = max_interval
        if random_point_generator is not None:
            self.random_point_generator = random_point_generator

    @property
    def min_interval(self) -> primitives.Float | None:
        """The MinInterval field value."""
        member = self.get_member("MinInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_interval.setter
    def min_interval(self, value: primitives.Float) -> None:
        """Set the MinInterval field value."""
        member = self.get_member("MinInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinInterval", fields.FieldFloat(value=value)
            )

    @property
    def max_interval(self) -> primitives.Float | None:
        """The MaxInterval field value."""
        member = self.get_member("MaxInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_interval.setter
    def max_interval(self, value: primitives.Float) -> None:
        """Set the MaxInterval field value."""
        member = self.get_member("MaxInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxInterval", fields.FieldFloat(value=value)
            )

    @property
    def random_point_generator(self) -> str | None:
        """Target ID of the RandomPointGenerator reference (targets IPointGenerator)."""
        member = self.get_member("RandomPointGenerator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @random_point_generator.setter
    def random_point_generator(self, target: str | IPointGenerator | None) -> None:
        """Set the RandomPointGenerator reference by target ID or IPointGenerator instance."""
        target_id: str | None = target.id if isinstance(target, IPointGenerator) else target  # type: ignore[assignment]
        member = self.get_member("RandomPointGenerator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RandomPointGenerator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IPointGenerator'),
            )

