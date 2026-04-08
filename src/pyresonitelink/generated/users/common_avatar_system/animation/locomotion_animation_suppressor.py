"""Generated component: LocomotionAnimationSuppressor."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationSuppressor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocomotionAnimationSuppressor.

    Category: Users/Common Avatar System/Animation
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationSuppressor"

    def __init__(self, suppress_feet_simulation: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            suppress_feet_simulation: Initial value for SuppressFeetSimulation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if suppress_feet_simulation is not None:
            self.suppress_feet_simulation = suppress_feet_simulation

    @property
    def suppress_feet_simulation(self) -> primitives.Bool | None:
        """The SuppressFeetSimulation field value."""
        member = self.get_member("SuppressFeetSimulation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @suppress_feet_simulation.setter
    def suppress_feet_simulation(self, value: primitives.Bool) -> None:
        """Set the SuppressFeetSimulation field value."""
        member = self.get_member("SuppressFeetSimulation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SuppressFeetSimulation", fields.FieldBool(value=value)
            )

