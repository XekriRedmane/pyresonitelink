"""Generated component: ColorHSV_OverLifetimeStartEnd."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorHSV_OverLifetimeStartEnd(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ColorHSV_OverLifetimeStartEnd.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorHSV_OverLifetimeStartEnd"

    def __init__(self, start_hue: np.float32 | None = None, start_saturation: np.float32 | None = None, start_value: np.float32 | None = None, end_hue: np.float32 | None = None, end_saturation: np.float32 | None = None, end_value: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            start_hue: Initial value for StartHue.
            start_saturation: Initial value for StartSaturation.
            start_value: Initial value for StartValue.
            end_hue: Initial value for EndHue.
            end_saturation: Initial value for EndSaturation.
            end_value: Initial value for EndValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if start_hue is not None:
            self.start_hue = start_hue
        if start_saturation is not None:
            self.start_saturation = start_saturation
        if start_value is not None:
            self.start_value = start_value
        if end_hue is not None:
            self.end_hue = end_hue
        if end_saturation is not None:
            self.end_saturation = end_saturation
        if end_value is not None:
            self.end_value = end_value

    @property
    def start_hue(self) -> np.float32 | None:
        """The StartHue field value."""
        member = self.get_member("StartHue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_hue.setter
    def start_hue(self, value: np.float32) -> None:
        """Set the StartHue field value."""
        member = self.get_member("StartHue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartHue", fields.FieldFloat(value=value)
            )

    @property
    def start_saturation(self) -> np.float32 | None:
        """The StartSaturation field value."""
        member = self.get_member("StartSaturation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_saturation.setter
    def start_saturation(self, value: np.float32) -> None:
        """Set the StartSaturation field value."""
        member = self.get_member("StartSaturation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartSaturation", fields.FieldFloat(value=value)
            )

    @property
    def start_value(self) -> np.float32 | None:
        """The StartValue field value."""
        member = self.get_member("StartValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_value.setter
    def start_value(self, value: np.float32) -> None:
        """Set the StartValue field value."""
        member = self.get_member("StartValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartValue", fields.FieldFloat(value=value)
            )

    @property
    def end_hue(self) -> np.float32 | None:
        """The EndHue field value."""
        member = self.get_member("EndHue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_hue.setter
    def end_hue(self, value: np.float32) -> None:
        """Set the EndHue field value."""
        member = self.get_member("EndHue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndHue", fields.FieldFloat(value=value)
            )

    @property
    def end_saturation(self) -> np.float32 | None:
        """The EndSaturation field value."""
        member = self.get_member("EndSaturation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_saturation.setter
    def end_saturation(self, value: np.float32) -> None:
        """Set the EndSaturation field value."""
        member = self.get_member("EndSaturation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndSaturation", fields.FieldFloat(value=value)
            )

    @property
    def end_value(self) -> np.float32 | None:
        """The EndValue field value."""
        member = self.get_member("EndValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_value.setter
    def end_value(self, value: np.float32) -> None:
        """Set the EndValue field value."""
        member = self.get_member("EndValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndValue", fields.FieldFloat(value=value)
            )

