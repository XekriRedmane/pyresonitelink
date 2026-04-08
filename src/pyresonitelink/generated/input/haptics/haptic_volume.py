"""Generated component: HapticVolume."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ihaptic_source import IHapticSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HapticVolume(GeneratedComponent, IHapticSource, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HapticVolume.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HapticVolume"

    def __init__(self, intensity: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            intensity: Initial value for Intensity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if intensity is not None:
            self.intensity = intensity

    @property
    def sensation(self) -> members.FieldEnum | None:
        """The Sensation member."""
        member = self.get_member("Sensation")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sensation.setter
    def sensation(self, value: members.FieldEnum) -> None:
        """Set the Sensation member."""
        self.set_member("Sensation", value)

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
    def sensation_hints(self) -> members.SyncList | None:
        """The SensationHints member."""
        member = self.get_member("SensationHints")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sensation_hints.setter
    def sensation_hints(self, value: members.SyncList) -> None:
        """Set the SensationHints member."""
        self.set_member("SensationHints", value)

