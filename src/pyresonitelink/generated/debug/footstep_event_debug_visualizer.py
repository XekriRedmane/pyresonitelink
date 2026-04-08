"""Generated component: FootstepEventDebugVisualizer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifootstep_event_receiver import IFootstepEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FootstepEventDebugVisualizer(GeneratedComponent, IFootstepEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FootstepEventDebugVisualizer.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FootstepEventDebugVisualizer"

    def __init__(self, duration: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            duration: Initial value for Duration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if duration is not None:
            self.duration = duration

    @property
    def duration(self) -> np.float32 | None:
        """The Duration field value."""
        member = self.get_member("Duration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @duration.setter
    def duration(self, value: np.float32) -> None:
        """Set the Duration field value."""
        member = self.get_member("Duration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Duration", fields.FieldFloat(value=value)
            )

