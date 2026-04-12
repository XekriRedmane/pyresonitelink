"""Generated component: RenderingQualitySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.shadow_cascade_mode import ShadowCascadeMode
from pyresonitelink.generated._enums.shadow_resolution_mode import ShadowResolutionMode
from pyresonitelink.generated._enums.skin_weight_mode import SkinWeightMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class RenderingQualitySettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RenderingQualitySettings"

    def __init__(self, per_pixel_lights: primitives.Int | None = None, shadow_cascades: ShadowCascadeMode | str | None = None, shadow_resolution: ShadowResolutionMode | str | None = None, shadow_distance: primitives.Float | None = None, skin_weight_mode: SkinWeightMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            per_pixel_lights: Initial value for PerPixelLights.
            shadow_cascades: Initial value for ShadowCascades.
            shadow_resolution: Initial value for ShadowResolution.
            shadow_distance: Initial value for ShadowDistance.
            skin_weight_mode: Initial value for SkinWeightMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if per_pixel_lights is not None:
            self.per_pixel_lights = per_pixel_lights
        if shadow_cascades is not None:
            self.shadow_cascades = shadow_cascades
        if shadow_resolution is not None:
            self.shadow_resolution = shadow_resolution
        if shadow_distance is not None:
            self.shadow_distance = shadow_distance
        if skin_weight_mode is not None:
            self.skin_weight_mode = skin_weight_mode

    @property
    def per_pixel_lights(self) -> primitives.Int | None:
        """How many lights can affect a single pixel on screen."""
        member = self.get_member("PerPixelLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @per_pixel_lights.setter
    def per_pixel_lights(self, value: primitives.Int) -> None:
        """Set the PerPixelLights field value."""
        member = self.get_member("PerPixelLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PerPixelLights", fields.FieldInt(value=value)
            )

    @property
    def shadow_cascades(self) -> ShadowCascadeMode | None:
        """How many shadows can be affecting an area."""
        member = self.get_member("ShadowCascades")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ShadowCascadeMode(member.value)
        return None

    @shadow_cascades.setter
    def shadow_cascades(self, value: ShadowCascadeMode | str) -> None:
        """Set ShadowCascades. How many shadows can be affecting an area."""
        member = self.get_member("ShadowCascades")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ShadowCascades",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shadow_resolution(self) -> ShadowResolutionMode | None:
        """The max resolution allowed for shadows."""
        member = self.get_member("ShadowResolution")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ShadowResolutionMode(member.value)
        return None

    @shadow_resolution.setter
    def shadow_resolution(self, value: ShadowResolutionMode | str) -> None:
        """Set ShadowResolution. The max resolution allowed for shadows."""
        member = self.get_member("ShadowResolution")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ShadowResolution",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shadow_distance(self) -> primitives.Float | None:
        """The max distance to render shadows from the camera."""
        member = self.get_member("ShadowDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_distance.setter
    def shadow_distance(self, value: primitives.Float) -> None:
        """Set the ShadowDistance field value."""
        member = self.get_member("ShadowDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowDistance", fields.FieldFloat(value=value)
            )

    @property
    def skin_weight_mode(self) -> SkinWeightMode | None:
        """How many skin weights to allow for skinned mesh renderers."""
        member = self.get_member("SkinWeightMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SkinWeightMode(member.value)
        return None

    @skin_weight_mode.setter
    def skin_weight_mode(self, value: SkinWeightMode | str) -> None:
        """Set SkinWeightMode. How many skin weights to allow for skinned mesh renderers."""
        member = self.get_member("SkinWeightMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SkinWeightMode",
                members.FieldEnum(value=str(value)),
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

