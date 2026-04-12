"""Generated component: ProceduralSky."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.sun_type import SunType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.light import Light
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProceduralSky(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ProceduralSky texture is used to dynamically create a skybox using a sun rotation and intensity including sun color.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProceduralSky"

    def __init__(self, sun_quality: SunType | str | None = None, sun_size: primitives.Float | None = None, sun: str | Light | None = None, atmosphere_thickness: primitives.Float | None = None, sky_tint: primitives.ColorX | None = None, ground_color: primitives.ColorX | None = None, exposure: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sun_quality: Initial value for SunQuality.
            sun_size: Initial value for SunSize.
            sun: Initial value for Sun.
            atmosphere_thickness: Initial value for AtmosphereThickness.
            sky_tint: Initial value for SkyTint.
            ground_color: Initial value for GroundColor.
            exposure: Initial value for Exposure.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sun_quality is not None:
            self.sun_quality = sun_quality
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
    def sun_quality(self) -> SunType | None:
        """The quality preset of the sun in the sky."""
        member = self.get_member("SunQuality")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SunType(member.value)
        return None

    @sun_quality.setter
    def sun_quality(self, value: SunType | str) -> None:
        """Set SunQuality. The quality preset of the sun in the sky."""
        member = self.get_member("SunQuality")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SunQuality",
                members.FieldEnum(value=str(value)),
            )

    @property
    def sun_size(self) -> primitives.Float | None:
        """size of the sun in the sky"""
        member = self.get_member("SunSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sun_size.setter
    def sun_size(self, value: primitives.Float) -> None:
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
        """The light to use for rotation, intensity, and color of the sun on this material."""
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
    def atmosphere_thickness(self) -> primitives.Float | None:
        """How much the atmosphere will light up the scene. If this is low, the ``SkyTint`` color coming up from the lower region of the world won't make it up to the top of the world as well, and will gradient into black. good for thin atmosphere planets, or 0 for no atmosphere."""
        member = self.get_member("AtmosphereThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @atmosphere_thickness.setter
    def atmosphere_thickness(self, value: primitives.Float) -> None:
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
        """The tint of the atmosphere of the world."""
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
        """The tint of the sky below the horizon line."""
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
    def exposure(self) -> primitives.Float | None:
        """How much to light up or darken the sky color overall."""
        member = self.get_member("Exposure")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exposure.setter
    def exposure(self, value: primitives.Float) -> None:
        """Set the Exposure field value."""
        member = self.get_member("Exposure")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exposure", fields.FieldFloat(value=value)
            )

