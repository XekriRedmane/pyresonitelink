"""Generated component: Light."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.light_type import LightType
from pyresonitelink.generated._enums.shadow_type import ShadowType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture import ITexture
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Light(GeneratedComponent, IRenderable, ICustomInspector, IWorldEventReceiver):
    """The Light component is used to illuminate the render scene beyond skybox illumination. This component can be used for suns, spots, and points, but not area lights.

    Category: Rendering

    Spot light cookies use the alpha channel of a flat texture. If your
    texture lacks an alpha channel, you can go into the texture's component
    and press the Color to Alpha (White) button. The preview image may look
    incorrect unless you change it to render in Alpha instead of Opaque, but
    the texture itself will still work as a cookie. Point lights use a cube
    map. You can create a cube map with the wizard in the Create New >
    Editors menu of a Dev Tool. For optimization purposes, shadows are one
    of the most "expensive" rendering costs. This can be mitigated by only
    allowing specific lights to cast shadows. A point light can be as much
    as 6x more difficult to render than a spot light, especially with
    shadows enabled. In any case, limiting the range of lights is one of the
    greatest ways to improve performance in worlds with multiple lights.

    **See also**: * Skybox
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Light"

    def __init__(self, light_type: LightType | str | None = None, intensity: primitives.Float | None = None, color: primitives.ColorX | None = None, shadow_type: ShadowType | str | None = None, shadow_strength: primitives.Float | None = None, shadow_near_plane: primitives.Float | None = None, shadow_map_resolution: primitives.Int | None = None, shadow_bias: primitives.Float | None = None, shadow_normal_bias: primitives.Float | None = None, range_: primitives.Float | None = None, spot_angle: primitives.Float | None = None, cookie: str | IAssetProvider[ITexture] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            light_type: Initial value for LightType.
            intensity: Initial value for Intensity.
            color: Initial value for Color.
            shadow_type: Initial value for ShadowType.
            shadow_strength: Initial value for ShadowStrength.
            shadow_near_plane: Initial value for ShadowNearPlane.
            shadow_map_resolution: Initial value for ShadowMapResolution.
            shadow_bias: Initial value for ShadowBias.
            shadow_normal_bias: Initial value for ShadowNormalBias.
            range_: Initial value for Range.
            spot_angle: Initial value for SpotAngle.
            cookie: Initial value for Cookie.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if light_type is not None:
            self.light_type = light_type
        if intensity is not None:
            self.intensity = intensity
        if color is not None:
            self.color = color
        if shadow_type is not None:
            self.shadow_type = shadow_type
        if shadow_strength is not None:
            self.shadow_strength = shadow_strength
        if shadow_near_plane is not None:
            self.shadow_near_plane = shadow_near_plane
        if shadow_map_resolution is not None:
            self.shadow_map_resolution = shadow_map_resolution
        if shadow_bias is not None:
            self.shadow_bias = shadow_bias
        if shadow_normal_bias is not None:
            self.shadow_normal_bias = shadow_normal_bias
        if range_ is not None:
            self.range_ = range_
        if spot_angle is not None:
            self.spot_angle = spot_angle
        if cookie is not None:
            self.cookie = cookie

    @property
    def light_type(self) -> LightType | None:
        """The type of light. Can be Point, Directional, or Spot."""
        member = self.get_member("LightType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LightType(member.value)
        return None

    @light_type.setter
    def light_type(self, value: LightType | str) -> None:
        """Set LightType. The type of light. Can be Point, Directional, or Spot."""
        member = self.get_member("LightType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "LightType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def intensity(self) -> primitives.Float | None:
        """How intense the light is. This is a multiplier."""
        member = self.get_member("Intensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intensity.setter
    def intensity(self, value: primitives.Float) -> None:
        """Set the Intensity field value."""
        member = self.get_member("Intensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Intensity", fields.FieldFloat(value=value)
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The color of the light this source should project."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def shadow_type(self) -> ShadowType | None:
        """The type of shadow this light should use. Can be None, Hard, or Soft."""
        member = self.get_member("ShadowType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ShadowType(member.value)
        return None

    @shadow_type.setter
    def shadow_type(self, value: ShadowType | str) -> None:
        """Set ShadowType. The type of shadow this light should use. Can be None, Hard, or Soft."""
        member = self.get_member("ShadowType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ShadowType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shadow_strength(self) -> primitives.Float | None:
        """How dark the shadows are."""
        member = self.get_member("ShadowStrength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_strength.setter
    def shadow_strength(self, value: primitives.Float) -> None:
        """Set the ShadowStrength field value."""
        member = self.get_member("ShadowStrength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowStrength", fields.FieldFloat(value=value)
            )

    @property
    def shadow_near_plane(self) -> primitives.Float | None:
        """How far away shadows will render for this point light."""
        member = self.get_member("ShadowNearPlane")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_near_plane.setter
    def shadow_near_plane(self, value: primitives.Float) -> None:
        """Set the ShadowNearPlane field value."""
        member = self.get_member("ShadowNearPlane")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowNearPlane", fields.FieldFloat(value=value)
            )

    @property
    def shadow_map_resolution(self) -> primitives.Int | None:
        """How detailed the resolution for shadows is in pixels."""
        member = self.get_member("ShadowMapResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_map_resolution.setter
    def shadow_map_resolution(self, value: primitives.Int) -> None:
        """Set the ShadowMapResolution field value."""
        member = self.get_member("ShadowMapResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowMapResolution", fields.FieldInt(value=value)
            )

    @property
    def shadow_bias(self) -> primitives.Float | None:
        """added to the distance in the shadow map to ensure that pixels on the borderline definitely pass the comparison as they should."""
        member = self.get_member("ShadowBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_bias.setter
    def shadow_bias(self, value: primitives.Float) -> None:
        """Set the ShadowBias field value."""
        member = self.get_member("ShadowBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowBias", fields.FieldFloat(value=value)
            )

    @property
    def shadow_normal_bias(self) -> primitives.Float | None:
        """Makes surrounding lit areas encroach upon the center shadow, making the encroached area lit too."""
        member = self.get_member("ShadowNormalBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_normal_bias.setter
    def shadow_normal_bias(self, value: primitives.Float) -> None:
        """Set the ShadowNormalBias field value."""
        member = self.get_member("ShadowNormalBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowNormalBias", fields.FieldFloat(value=value)
            )

    @property
    def range_(self) -> primitives.Float | None:
        """How far for the light to shine in meters, where the range represents the point where the falloff stops."""
        member = self.get_member("Range")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_.setter
    def range_(self, value: primitives.Float) -> None:
        """Set the Range field value."""
        member = self.get_member("Range")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Range", fields.FieldFloat(value=value)
            )

    @property
    def spot_angle(self) -> primitives.Float | None:
        """The angle from 0-180 when on spot light mode to project the light at. 0 is no light, 60 is like car headlights, and 180 is extreme and unrealistic."""
        member = self.get_member("SpotAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spot_angle.setter
    def spot_angle(self, value: primitives.Float) -> None:
        """Set the SpotAngle field value."""
        member = self.get_member("SpotAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpotAngle", fields.FieldFloat(value=value)
            )

    @property
    def cookie(self) -> str | None:
        """The cookie texture is used to limit the light area to add texture and occlusion."""
        member = self.get_member("Cookie")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cookie.setter
    def cookie(self, target: str | IAssetProvider[ITexture] | None) -> None:
        """Set the Cookie reference by target ID or IAssetProvider[ITexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Cookie")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Cookie",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture>'),
            )

