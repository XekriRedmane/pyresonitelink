"""Generated component: DebugSphereRaycast."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugSphereRaycast(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugSphereRaycast component is used to show the multiple hit normals (1 per collider) of a sweep raycast of a sphere. This essentially acts as a fat raycast, which has thickness. Unfortunately this raycast is only for Debug purposes. Is simulated on the host machine.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugSphereRaycast"

    def __init__(self, direction: primitives.Float3 | None = None, radius: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            direction: Initial value for Direction.
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if direction is not None:
            self.direction = direction
        if radius is not None:
            self.radius = radius

    @property
    def direction(self) -> primitives.Float3 | None:
        """the direction and distance the raycast should go."""
        member = self.get_member("Direction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction.setter
    def direction(self, value: primitives.Float3) -> None:
        """Set the Direction field value."""
        member = self.get_member("Direction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Direction", fields.FieldFloat3(value=value)
            )

    @property
    def radius(self) -> primitives.Float | None:
        """How far the raycasts created should go."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

