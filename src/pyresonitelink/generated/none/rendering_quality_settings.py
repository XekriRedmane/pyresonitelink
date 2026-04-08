"""Generated component: RenderingQualitySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class RenderingQualitySettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.RenderingQualitySettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RenderingQualitySettings"

    def __init__(self, per_pixel_lights: primitives.Int | None = None, shadow_distance: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            per_pixel_lights: Initial value for PerPixelLights.
            shadow_distance: Initial value for ShadowDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if per_pixel_lights is not None:
            self.per_pixel_lights = per_pixel_lights
        if shadow_distance is not None:
            self.shadow_distance = shadow_distance

    @property
    def per_pixel_lights(self) -> primitives.Int | None:
        """The PerPixelLights field value."""
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
    def shadow_cascades(self) -> members.FieldEnum | None:
        """The ShadowCascades member."""
        member = self.get_member("ShadowCascades")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shadow_cascades.setter
    def shadow_cascades(self, value: members.FieldEnum) -> None:
        """Set the ShadowCascades member."""
        self.set_member("ShadowCascades", value)

    @property
    def shadow_resolution(self) -> members.FieldEnum | None:
        """The ShadowResolution member."""
        member = self.get_member("ShadowResolution")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shadow_resolution.setter
    def shadow_resolution(self, value: members.FieldEnum) -> None:
        """Set the ShadowResolution member."""
        self.set_member("ShadowResolution", value)

    @property
    def shadow_distance(self) -> primitives.Float | None:
        """The ShadowDistance field value."""
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
    def skin_weight_mode(self) -> members.FieldEnum | None:
        """The SkinWeightMode member."""
        member = self.get_member("SkinWeightMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @skin_weight_mode.setter
    def skin_weight_mode(self, value: members.FieldEnum) -> None:
        """Set the SkinWeightMode member."""
        self.set_member("SkinWeightMode", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

