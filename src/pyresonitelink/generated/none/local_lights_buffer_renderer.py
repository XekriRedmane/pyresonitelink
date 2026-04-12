"""Generated component: LocalLightsBufferRenderer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.light_type import LightType
from pyresonitelink.generated._enums.shadow_type import ShadowType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture import ITexture
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalLightsBufferRenderer(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The Local Lights Buffer Renderer component is used to render the lights for a particle system.

    Used in particle systems.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalLightsBufferRenderer"

    def __init__(self, light_type: LightType | str | None = None, shadow_type: ShadowType | str | None = None, shadow_strength: primitives.Float | None = None, shadow_near_plane: primitives.Float | None = None, shadow_map_resolution: primitives.Int | None = None, shadow_bias: primitives.Float | None = None, shadow_normal_bias: primitives.Float | None = None, cookie: str | IAssetProvider[ITexture] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            light_type: Initial value for LightType.
            shadow_type: Initial value for ShadowType.
            shadow_strength: Initial value for ShadowStrength.
            shadow_near_plane: Initial value for ShadowNearPlane.
            shadow_map_resolution: Initial value for ShadowMapResolution.
            shadow_bias: Initial value for ShadowBias.
            shadow_normal_bias: Initial value for ShadowNormalBias.
            cookie: Initial value for Cookie.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if light_type is not None:
            self.light_type = light_type
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
        if cookie is not None:
            self.cookie = cookie

    @property
    def light_type(self) -> LightType | None:
        """The kind of light to use."""
        member = self.get_member("LightType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LightType(member.value)
        return None

    @light_type.setter
    def light_type(self, value: LightType | str) -> None:
        """Set LightType. The kind of light to use."""
        member = self.get_member("LightType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "LightType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shadow_type(self) -> ShadowType | None:
        """The light's shadow type."""
        member = self.get_member("ShadowType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ShadowType(member.value)
        return None

    @shadow_type.setter
    def shadow_type(self, value: ShadowType | str) -> None:
        """Set ShadowType. The light's shadow type."""
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
        """The light's shadow strength."""
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
        """The light's near plane."""
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
        """The light's shadow map resolution."""
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
        """The light's shadow bias."""
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
        """The light's normal bias."""
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
    def cookie(self) -> str | None:
        """The texture used for the spotlight cutout texture."""
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

