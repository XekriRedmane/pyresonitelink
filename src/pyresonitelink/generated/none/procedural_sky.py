"""Generated component: ProceduralSky."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.light import Light
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProceduralSky(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProceduralSky.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProceduralSky"

    def __init__(self, sun_size: np.float32 | None = None, sun: str | Light | None = None, atmosphere_thickness: np.float32 | None = None, sky_tint: primitives.ColorX | None = None, ground_color: primitives.ColorX | None = None, exposure: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sun_size: Initial value for SunSize.
            sun: Initial value for Sun.
            atmosphere_thickness: Initial value for AtmosphereThickness.
            sky_tint: Initial value for SkyTint.
            ground_color: Initial value for GroundColor.
            exposure: Initial value for Exposure.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sun_size is not None:
            self.sun_size = sun_size
        if sun is not None:
            self.sun = sun
        if atmosphere_thickness is not None:
            self.atmosphere_thickness = atmosphere_thickness
        if sky_tint is not None:
            self.sky_tint = sky_tint
        if ground_color is not None:
            self.ground_color = ground_color
        if exposure is not None:
            self.exposure = exposure

    @property
    def sun_quality(self) -> members.FieldEnum | None:
        """The SunQuality member."""
        member = self.get_member("SunQuality")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sun_quality.setter
    def sun_quality(self, value: members.FieldEnum) -> None:
        """Set the SunQuality member."""
        self.set_member("SunQuality", value)

    @property
    def sun_size(self) -> np.float32 | None:
        """The SunSize field value."""
        member = self.get_member("SunSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sun_size.setter
    def sun_size(self, value: np.float32) -> None:
        """Set the SunSize field value."""
        member = self.get_member("SunSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SunSize", fields.FieldFloat(value=value)
            )

    @property
    def sun(self) -> str | None:
        """Target ID of the Sun reference (targets Light)."""
        member = self.get_member("Sun")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sun.setter
    def sun(self, target: str | Light | None) -> None:
        """Set the Sun reference by target ID or Light instance."""
        target_id: str | None = target.id if isinstance(target, Light) else target  # type: ignore[assignment]
        member = self.get_member("Sun")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Sun",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Light'),
            )

    @property
    def atmosphere_thickness(self) -> np.float32 | None:
        """The AtmosphereThickness field value."""
        member = self.get_member("AtmosphereThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @atmosphere_thickness.setter
    def atmosphere_thickness(self, value: np.float32) -> None:
        """Set the AtmosphereThickness field value."""
        member = self.get_member("AtmosphereThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AtmosphereThickness", fields.FieldFloat(value=value)
            )

    @property
    def sky_tint(self) -> primitives.ColorX | None:
        """The SkyTint field value."""
        member = self.get_member("SkyTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sky_tint.setter
    def sky_tint(self, value: primitives.ColorX) -> None:
        """Set the SkyTint field value."""
        member = self.get_member("SkyTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SkyTint", fields.FieldColorX(value=value)
            )

    @property
    def ground_color(self) -> primitives.ColorX | None:
        """The GroundColor field value."""
        member = self.get_member("GroundColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ground_color.setter
    def ground_color(self, value: primitives.ColorX) -> None:
        """Set the GroundColor field value."""
        member = self.get_member("GroundColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroundColor", fields.FieldColorX(value=value)
            )

    @property
    def exposure(self) -> np.float32 | None:
        """The Exposure field value."""
        member = self.get_member("Exposure")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exposure.setter
    def exposure(self, value: np.float32) -> None:
        """Set the Exposure field value."""
        member = self.get_member("Exposure")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exposure", fields.FieldFloat(value=value)
            )

