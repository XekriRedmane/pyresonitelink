"""Generated component: EarmuffSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class EarmuffSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.EarmuffSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EarmuffSettings"

    def __init__(self, earmuff_enabled: bool | None = None, volume_attenuation: np.float32 | None = None, directionality: np.float32 | None = None, distance: np.float32 | None = None, angle: np.float32 | None = None, transition_start: np.float32 | None = None, transition_length: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            earmuff_enabled: Initial value for EarmuffEnabled.
            volume_attenuation: Initial value for VolumeAttenuation.
            directionality: Initial value for Directionality.
            distance: Initial value for Distance.
            angle: Initial value for Angle.
            transition_start: Initial value for TransitionStart.
            transition_length: Initial value for TransitionLength.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if earmuff_enabled is not None:
            self.earmuff_enabled = earmuff_enabled
        if volume_attenuation is not None:
            self.volume_attenuation = volume_attenuation
        if directionality is not None:
            self.directionality = directionality
        if distance is not None:
            self.distance = distance
        if angle is not None:
            self.angle = angle
        if transition_start is not None:
            self.transition_start = transition_start
        if transition_length is not None:
            self.transition_length = transition_length

    @property
    def earmuff_enabled(self) -> bool | None:
        """The EarmuffEnabled field value."""
        member = self.get_member("EarmuffEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @earmuff_enabled.setter
    def earmuff_enabled(self, value: bool) -> None:
        """Set the EarmuffEnabled field value."""
        member = self.get_member("EarmuffEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EarmuffEnabled", fields.FieldBool(value=value)
            )

    @property
    def volume_attenuation(self) -> np.float32 | None:
        """The VolumeAttenuation field value."""
        member = self.get_member("VolumeAttenuation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume_attenuation.setter
    def volume_attenuation(self, value: np.float32) -> None:
        """Set the VolumeAttenuation field value."""
        member = self.get_member("VolumeAttenuation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VolumeAttenuation", fields.FieldFloat(value=value)
            )

    @property
    def directionality(self) -> np.float32 | None:
        """The Directionality field value."""
        member = self.get_member("Directionality")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @directionality.setter
    def directionality(self, value: np.float32) -> None:
        """Set the Directionality field value."""
        member = self.get_member("Directionality")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Directionality", fields.FieldFloat(value=value)
            )

    @property
    def distance(self) -> np.float32 | None:
        """The Distance field value."""
        member = self.get_member("Distance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance.setter
    def distance(self, value: np.float32) -> None:
        """Set the Distance field value."""
        member = self.get_member("Distance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distance", fields.FieldFloat(value=value)
            )

    @property
    def angle(self) -> np.float32 | None:
        """The Angle field value."""
        member = self.get_member("Angle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle.setter
    def angle(self, value: np.float32) -> None:
        """Set the Angle field value."""
        member = self.get_member("Angle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Angle", fields.FieldFloat(value=value)
            )

    @property
    def transition_start(self) -> np.float32 | None:
        """The TransitionStart field value."""
        member = self.get_member("TransitionStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transition_start.setter
    def transition_start(self, value: np.float32) -> None:
        """Set the TransitionStart field value."""
        member = self.get_member("TransitionStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TransitionStart", fields.FieldFloat(value=value)
            )

    @property
    def transition_length(self) -> np.float32 | None:
        """The TransitionLength field value."""
        member = self.get_member("TransitionLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transition_length.setter
    def transition_length(self, value: np.float32) -> None:
        """Set the TransitionLength field value."""
        member = self.get_member("TransitionLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TransitionLength", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

