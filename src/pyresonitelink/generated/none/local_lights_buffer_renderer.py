"""Generated component: LocalLightsBufferRenderer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture import ITexture
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalLightsBufferRenderer(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocalLightsBufferRenderer.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalLightsBufferRenderer"

    def __init__(self, shadow_strength: np.float32 | None = None, shadow_near_plane: np.float32 | None = None, shadow_map_resolution: np.int32 | None = None, shadow_bias: np.float32 | None = None, shadow_normal_bias: np.float32 | None = None, cookie: str | IAssetProvider[ITexture] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            shadow_strength: Initial value for ShadowStrength.
            shadow_near_plane: Initial value for ShadowNearPlane.
            shadow_map_resolution: Initial value for ShadowMapResolution.
            shadow_bias: Initial value for ShadowBias.
            shadow_normal_bias: Initial value for ShadowNormalBias.
            cookie: Initial value for Cookie.
            component: Existing Component to wrap.
        """
        super().__init__(component)
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
    def shadow_strength(self) -> np.float32 | None:
        """The ShadowStrength field value."""
        member = self.get_member("ShadowStrength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_strength.setter
    def shadow_strength(self, value: np.float32) -> None:
        """Set the ShadowStrength field value."""
        member = self.get_member("ShadowStrength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowStrength", fields.FieldFloat(value=value)
            )

    @property
    def shadow_near_plane(self) -> np.float32 | None:
        """The ShadowNearPlane field value."""
        member = self.get_member("ShadowNearPlane")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_near_plane.setter
    def shadow_near_plane(self, value: np.float32) -> None:
        """Set the ShadowNearPlane field value."""
        member = self.get_member("ShadowNearPlane")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowNearPlane", fields.FieldFloat(value=value)
            )

    @property
    def shadow_map_resolution(self) -> np.int32 | None:
        """The ShadowMapResolution field value."""
        member = self.get_member("ShadowMapResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_map_resolution.setter
    def shadow_map_resolution(self, value: np.int32) -> None:
        """Set the ShadowMapResolution field value."""
        member = self.get_member("ShadowMapResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowMapResolution", fields.FieldInt(value=value)
            )

    @property
    def shadow_bias(self) -> np.float32 | None:
        """The ShadowBias field value."""
        member = self.get_member("ShadowBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_bias.setter
    def shadow_bias(self, value: np.float32) -> None:
        """Set the ShadowBias field value."""
        member = self.get_member("ShadowBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowBias", fields.FieldFloat(value=value)
            )

    @property
    def shadow_normal_bias(self) -> np.float32 | None:
        """The ShadowNormalBias field value."""
        member = self.get_member("ShadowNormalBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_normal_bias.setter
    def shadow_normal_bias(self, value: np.float32) -> None:
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

