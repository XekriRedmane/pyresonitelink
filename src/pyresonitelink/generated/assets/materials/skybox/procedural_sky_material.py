"""Generated component: ProceduralSkyMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.sun_type import SunType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.light import Light
from pyresonitelink.generated._types.iskybox_material import ISkyboxMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProceduralSkyMaterial(GeneratedComponent, ISkyboxMaterial, ICustomInspector, IWorldEventReceiver):
    """The Procedural Sky Material component is used to make a on-the-fly generated skybox using a light object and some values for atmosphere and sun size.

    Category: Assets/Materials/Skybox

    Used commonly in sky boxes found in grid spaces, and serves as a quick
    and simple way of making a sky that can be changed on the fly.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProceduralSkyMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, sun_quality: SunType | str | None = None, sun_size: primitives.Float | None = None, sun: str | Light | None = None, atmosphere_thickness: primitives.Float | None = None, sky_tint: primitives.ColorX | None = None, ground_color: primitives.ColorX | None = None, exposure: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
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
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
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
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def shader(self) -> str | None:
        """Target ID of the _shader reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shader.setter
    def shader(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _shader reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shader",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def sun_quality(self) -> SunType | None:
        """The SunQuality enum value."""
        member = self.get_member("SunQuality")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SunType(member.value)
        return None

    @sun_quality.setter
    def sun_quality(self, value: SunType | str) -> None:
        """Set the SunQuality enum value."""
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
        """The SunSize field value."""
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
    def atmosphere_thickness(self) -> primitives.Float | None:
        """The AtmosphereThickness field value."""
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
    def exposure(self) -> primitives.Float | None:
        """The Exposure field value."""
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

