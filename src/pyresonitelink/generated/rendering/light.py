"""Generated component: Light."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture import ITexture
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Light(GeneratedComponent, IRenderable, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Light.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Light"

    def __init__(self, intensity: primitives.Float | None = None, color: primitives.ColorX | None = None, shadow_strength: primitives.Float | None = None, shadow_near_plane: primitives.Float | None = None, shadow_map_resolution: primitives.Int | None = None, shadow_bias: primitives.Float | None = None, shadow_normal_bias: primitives.Float | None = None, range_: primitives.Float | None = None, spot_angle: primitives.Float | None = None, cookie: str | IAssetProvider[ITexture] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            intensity: Initial value for Intensity.
            color: Initial value for Color.
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
        if intensity is not None:
            self.intensity = intensity
        if color is not None:
            self.color = color
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
    def light_type(self) -> members.FieldEnum | None:
        """The LightType member."""
        member = self.get_member("LightType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @light_type.setter
    def light_type(self, value: members.FieldEnum) -> None:
        """Set the LightType member."""
        self.set_member("LightType", value)

    @property
    def intensity(self) -> primitives.Float | None:
        """The Intensity field value."""
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
        """The Color field value."""
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
    def shadow_type(self) -> members.FieldEnum | None:
        """The ShadowType member."""
        member = self.get_member("ShadowType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shadow_type.setter
    def shadow_type(self, value: members.FieldEnum) -> None:
        """Set the ShadowType member."""
        self.set_member("ShadowType", value)

    @property
    def shadow_strength(self) -> primitives.Float | None:
        """The ShadowStrength field value."""
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
        """The ShadowNearPlane field value."""
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
        """The ShadowMapResolution field value."""
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
        """The ShadowBias field value."""
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
        """The ShadowNormalBias field value."""
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
        """The Range field value."""
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
        """The SpotAngle field value."""
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
        """Target ID of the Cookie reference (targets IAssetProvider[ITexture])."""
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

