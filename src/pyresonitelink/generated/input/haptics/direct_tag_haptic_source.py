"""Generated component: DirectTagHapticSource."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idirect_haptic_source import IDirectHapticSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DirectTagHapticSource(GeneratedComponent, IDirectHapticSource, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DirectTagHapticSource.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DirectTagHapticSource"

    def __init__(self, haptic_tag: str | None = None, force: np.float32 | None = None, temperature: np.float32 | None = None, pain: np.float32 | None = None, vibration: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            haptic_tag: Initial value for HapticTag.
            force: Initial value for Force.
            temperature: Initial value for Temperature.
            pain: Initial value for Pain.
            vibration: Initial value for Vibration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if haptic_tag is not None:
            self.haptic_tag = haptic_tag
        if force is not None:
            self.force = force
        if temperature is not None:
            self.temperature = temperature
        if pain is not None:
            self.pain = pain
        if vibration is not None:
            self.vibration = vibration

    @property
    def haptic_tag(self) -> str | None:
        """The HapticTag field value."""
        member = self.get_member("HapticTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @haptic_tag.setter
    def haptic_tag(self, value: str) -> None:
        """Set the HapticTag field value."""
        member = self.get_member("HapticTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HapticTag", fields.FieldString(value=value)
            )

    @property
    def force(self) -> np.float32 | None:
        """The Force field value."""
        member = self.get_member("Force")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force.setter
    def force(self, value: np.float32) -> None:
        """Set the Force field value."""
        member = self.get_member("Force")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Force", fields.FieldFloat(value=value)
            )

    @property
    def temperature(self) -> np.float32 | None:
        """The Temperature field value."""
        member = self.get_member("Temperature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @temperature.setter
    def temperature(self, value: np.float32) -> None:
        """Set the Temperature field value."""
        member = self.get_member("Temperature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Temperature", fields.FieldFloat(value=value)
            )

    @property
    def pain(self) -> np.float32 | None:
        """The Pain field value."""
        member = self.get_member("Pain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pain.setter
    def pain(self, value: np.float32) -> None:
        """Set the Pain field value."""
        member = self.get_member("Pain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pain", fields.FieldFloat(value=value)
            )

    @property
    def vibration(self) -> np.float32 | None:
        """The Vibration field value."""
        member = self.get_member("Vibration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vibration.setter
    def vibration(self, value: np.float32) -> None:
        """Set the Vibration field value."""
        member = self.get_member("Vibration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vibration", fields.FieldFloat(value=value)
            )

