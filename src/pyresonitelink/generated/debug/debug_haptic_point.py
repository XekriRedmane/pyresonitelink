"""Generated component: DebugHapticPoint."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ihaptic_source import IHapticSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugHapticPoint(GeneratedComponent, IHapticSource, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugHapticPoint.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugHapticPoint"

    def __init__(self, intensity: np.float32 | None = None, index: np.int32 | None = None, position: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            intensity: Initial value for Intensity.
            index: Initial value for Index.
            position: Initial value for Position.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if intensity is not None:
            self.intensity = intensity
        if index is not None:
            self.index = index
        if position is not None:
            self.position = position

    @property
    def intensity(self) -> np.float32 | None:
        """The Intensity field value."""
        member = self.get_member("Intensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intensity.setter
    def intensity(self, value: np.float32) -> None:
        """Set the Intensity field value."""
        member = self.get_member("Intensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Intensity", fields.FieldFloat(value=value)
            )

    @property
    def index(self) -> np.int32 | None:
        """The Index field value."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: np.int32) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def position(self) -> str | None:
        """The Position field value."""
        member = self.get_member("Position")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position.setter
    def position(self, value: str) -> None:
        """Set the Position field value."""
        member = self.get_member("Position")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Position", fields.FieldString(value=value)
            )

