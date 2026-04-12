"""Generated component: FootstepEventDebugVisualizer."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifootstep_event_receiver import IFootstepEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FootstepEventDebugVisualizer(GeneratedComponent, IFootstepEventReceiver, IWorldEventReceiver):
    """The FootStepEventDebugVisualizer shows footstep collisions with a collider on the same Slot as the one it's attached on.

    Category: Debug

    **Usages**: Used to show footstep events for Debug purposes.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FootstepEventDebugVisualizer"

    def __init__(self, duration: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            duration: Initial value for Duration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if duration is not None:
            self.duration = duration

    @property
    def duration(self) -> primitives.Float | None:
        """How long the debug step visual should display for in seconds."""
        member = self.get_member("Duration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @duration.setter
    def duration(self, value: primitives.Float) -> None:
        """Set the Duration field value."""
        member = self.get_member("Duration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Duration", fields.FieldFloat(value=value)
            )

