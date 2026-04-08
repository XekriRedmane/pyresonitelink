"""Generated component: HapticPointData."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HapticPointData(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HapticPointData.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HapticPointData"

    def __init__(self, index: np.int32 | None = None, force: np.float32 | None = None, temperature: np.float32 | None = None, pain: np.float32 | None = None, vibration: np.float32 | None = None, total_activation_intensity: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            index: Initial value for Index.
            force: Initial value for Force.
            temperature: Initial value for Temperature.
            pain: Initial value for Pain.
            vibration: Initial value for Vibration.
            total_activation_intensity: Initial value for TotalActivationIntensity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if index is not None:
            self.index = index
        if force is not None:
            self.force = force
        if temperature is not None:
            self.temperature = temperature
        if pain is not None:
            self.pain = pain
        if vibration is not None:
            self.vibration = vibration
        if total_activation_intensity is not None:
            self.total_activation_intensity = total_activation_intensity

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
    def user(self) -> members.SyncObject | None:
        """The User member."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set the User member."""
        self.set_member("User", value)

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

    @property
    def total_activation_intensity(self) -> np.float32 | None:
        """The TotalActivationIntensity field value."""
        member = self.get_member("TotalActivationIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_activation_intensity.setter
    def total_activation_intensity(self, value: np.float32) -> None:
        """Set the TotalActivationIntensity field value."""
        member = self.get_member("TotalActivationIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalActivationIntensity", fields.FieldFloat(value=value)
            )

