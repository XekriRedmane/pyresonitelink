"""Generated component: ColorHSV_RangeInitializer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorHSV_RangeInitializer(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ColorHSV_RangeInitializer.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorHSV_RangeInitializer"

    def __init__(self, hue_min: np.float32 | None = None, hue_max: np.float32 | None = None, saturation_min: np.float32 | None = None, saturation_max: np.float32 | None = None, value_min: np.float32 | None = None, value_max: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hue_min: Initial value for HueMin.
            hue_max: Initial value for HueMax.
            saturation_min: Initial value for SaturationMin.
            saturation_max: Initial value for SaturationMax.
            value_min: Initial value for ValueMin.
            value_max: Initial value for ValueMax.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hue_min is not None:
            self.hue_min = hue_min
        if hue_max is not None:
            self.hue_max = hue_max
        if saturation_min is not None:
            self.saturation_min = saturation_min
        if saturation_max is not None:
            self.saturation_max = saturation_max
        if value_min is not None:
            self.value_min = value_min
        if value_max is not None:
            self.value_max = value_max

    @property
    def hue_min(self) -> np.float32 | None:
        """The HueMin field value."""
        member = self.get_member("HueMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hue_min.setter
    def hue_min(self, value: np.float32) -> None:
        """Set the HueMin field value."""
        member = self.get_member("HueMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HueMin", fields.FieldFloat(value=value)
            )

    @property
    def hue_max(self) -> np.float32 | None:
        """The HueMax field value."""
        member = self.get_member("HueMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hue_max.setter
    def hue_max(self, value: np.float32) -> None:
        """Set the HueMax field value."""
        member = self.get_member("HueMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HueMax", fields.FieldFloat(value=value)
            )

    @property
    def saturation_min(self) -> np.float32 | None:
        """The SaturationMin field value."""
        member = self.get_member("SaturationMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @saturation_min.setter
    def saturation_min(self, value: np.float32) -> None:
        """Set the SaturationMin field value."""
        member = self.get_member("SaturationMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaturationMin", fields.FieldFloat(value=value)
            )

    @property
    def saturation_max(self) -> np.float32 | None:
        """The SaturationMax field value."""
        member = self.get_member("SaturationMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @saturation_max.setter
    def saturation_max(self, value: np.float32) -> None:
        """Set the SaturationMax field value."""
        member = self.get_member("SaturationMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaturationMax", fields.FieldFloat(value=value)
            )

    @property
    def value_min(self) -> np.float32 | None:
        """The ValueMin field value."""
        member = self.get_member("ValueMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_min.setter
    def value_min(self, value: np.float32) -> None:
        """Set the ValueMin field value."""
        member = self.get_member("ValueMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ValueMin", fields.FieldFloat(value=value)
            )

    @property
    def value_max(self) -> np.float32 | None:
        """The ValueMax field value."""
        member = self.get_member("ValueMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_max.setter
    def value_max(self, value: np.float32) -> None:
        """Set the ValueMax field value."""
        member = self.get_member("ValueMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ValueMax", fields.FieldFloat(value=value)
            )

